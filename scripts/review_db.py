#!/usr/bin/env python3
r"""review_db.py — the deterministic store: review data as SQLite, queryable.

Why: the stage files (01–06) and run.md files are the human-readable record,
but every number the process reports (coverage, validate, the report) is
re-parsed out of markdown by regex at read time. That is fragile and
un-queryable. This module keeps a normalised SQLite mirror of the structured
facts — criteria and their metadata, checks, views, runs, check outcomes,
observations, findings, criterion outcomes (05), tasks, probe/axe
measurements — rebuilt deterministically from the files, plus integrity
checks that markdown cannot express (a finding citing a criterion that no
05 block rolls up; a Supports next to a Blocker; a run cited that does not
exist).

Authority (phase 1, 2026-09-11): the files stay the system of record; the
database is rebuilt from them (`sync`) and is the place to VERIFY. Every
`validate`/`coverage` run re-syncs first, so the DB is never staler than the
files. Phase 2 (a reviewer decision, not yet taken): flip authority for the
structured tables — check outcomes and 05 outcomes written to the DB first
and the markdown tables generated from it. See ontology/data-store.md.

Usage
    python scripts/review_db.py sync [<review>|--all]  # rebuild a review's database from its files
    python scripts/review_db.py check <review>       # integrity queries (exit 1 on issues)
    python scripts/review_db.py query "SELECT …" --review <r> | --all   # read-only SQL (--json)
    python scripts/review_db.py tables <review>      # schema overview with row counts
    python scripts/review_db.py criteria [--level A|AA] [--principle N]

Database: one per review, reviews/<id>/<id>.sqlite, **committed** with the
review. Byte-stable: a sync that changes nothing leaves the file untouched
(no timestamps inside; rebuilt in a temp file and swapped in only when the
canonical dump differs), so a commit diff on the .sqlite means the review's
data changed. `sync` rebuilds it from the files in seconds.
"""
import argparse
import datetime
import hashlib
import json
import pathlib
import re
import sqlite3
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import review as rv  # noqa: E402

ROOT = rv.ROOT
def db_path(review):
    """One database per review, inside the review folder, committed with it."""
    return pathlib.Path(review) / f"{pathlib.Path(review).name}.sqlite"

for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

SCHEMA = """
CREATE TABLE IF NOT EXISTS wcag_criteria (
  sc TEXT PRIMARY KEY,            -- '1.4.3'
  name TEXT NOT NULL,
  level TEXT NOT NULL,            -- A / AA / AAA
  principle_no INTEGER NOT NULL,  -- 1..4
  principle TEXT NOT NULL,        -- Perceivable …
  guideline_no TEXT NOT NULL,     -- '1.4'
  guideline TEXT NOT NULL,        -- Distinguishable
  version_added TEXT NOT NULL,    -- 2.0 / 2.1 / 2.2
  in_target INTEGER NOT NULL,     -- 1 = part of the WCAG 2.2 AA target (the 55)
  understanding_url TEXT,
  sort_key TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS fpc (
  code TEXT PRIMARY KEY,          -- '302.1'
  name TEXT NOT NULL,
  modality TEXT NOT NULL          -- matrix modality that tests it
);
CREATE TABLE IF NOT EXISTS checks (
  check_id TEXT PRIMARY KEY,      -- 'NV3'
  modality TEXT NOT NULL,         -- '' for sweep checks W#
  text TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS check_criteria (
  check_id TEXT NOT NULL REFERENCES checks(check_id),
  sc TEXT NOT NULL REFERENCES wcag_criteria(sc),
  PRIMARY KEY (check_id, sc)
);
CREATE TABLE IF NOT EXISTS reviews (
  review_id TEXT PRIMARY KEY,
  product TEXT,
  decision TEXT,
  report_status TEXT,
  source_sha TEXT               -- sha256 over the stage files (no timestamps: the file is byte-stable)
);
CREATE TABLE IF NOT EXISTS views (
  review_id TEXT NOT NULL, view_id TEXT NOT NULL, name TEXT, locator TEXT, represents TEXT,
  kind TEXT,                      -- structured / random
  PRIMARY KEY (review_id, view_id)
);
CREATE TABLE IF NOT EXISTS tasks (
  review_id TEXT NOT NULL, task_id TEXT NOT NULL, name TEXT, verdict TEXT,
  baselines TEXT, dates TEXT,
  PRIMARY KEY (review_id, task_id)
);
CREATE TABLE IF NOT EXISTS runs (
  review_id TEXT NOT NULL, run_id TEXT NOT NULL, date TEXT, view_id TEXT, locator TEXT,
  task_id TEXT, modality TEXT, tool TEXT, baseline TEXT, tester TEXT,
  result TEXT,                    -- Works / Works with issues / Broken / N/A / Not set
  result_note TEXT,               -- the full Result cell
  PRIMARY KEY (review_id, run_id)
);
CREATE TABLE IF NOT EXISTS check_outcomes (
  review_id TEXT NOT NULL, run_id TEXT NOT NULL, check_id TEXT NOT NULL,
  outcome TEXT NOT NULL,          -- pass / fail / partial / n/a / '' (unanswered) / '?' (unrecognised)
  raw TEXT, note TEXT,
  PRIMARY KEY (review_id, run_id, check_id)
);
CREATE TABLE IF NOT EXISTS observations (
  review_id TEXT NOT NULL, run_id TEXT NOT NULL, obs_id TEXT NOT NULL,
  status TEXT, text TEXT, classified TEXT,
  PRIMARY KEY (review_id, run_id, obs_id)
);
CREATE TABLE IF NOT EXISTS findings (
  review_id TEXT NOT NULL, finding_id TEXT NOT NULL,
  section TEXT,                   -- task / view
  view_id TEXT, task_id TEXT, where_text TEXT, observed TEXT, affected TEXT,
  severity TEXT, evidence TEXT, withdrawn INTEGER NOT NULL DEFAULT 0,
  fields_json TEXT,
  PRIMARY KEY (review_id, finding_id)
);
CREATE TABLE IF NOT EXISTS finding_criteria (
  review_id TEXT NOT NULL, finding_id TEXT NOT NULL, sc TEXT NOT NULL,
  PRIMARY KEY (review_id, finding_id, sc)
);
CREATE TABLE IF NOT EXISTS finding_runs (
  review_id TEXT NOT NULL, finding_id TEXT NOT NULL, run_id TEXT NOT NULL,
  PRIMARY KEY (review_id, finding_id, run_id)
);
CREATE TABLE IF NOT EXISTS criterion_outcomes (
  review_id TEXT NOT NULL, sc TEXT NOT NULL,
  outcome TEXT NOT NULL,          -- normalised ACR vocabulary
  outcome_raw TEXT, vendor_claim TEXT, task_findings TEXT, remarks TEXT,
  PRIMARY KEY (review_id, sc)
);
CREATE TABLE IF NOT EXISTS criterion_findings (
  review_id TEXT NOT NULL, sc TEXT NOT NULL, finding_id TEXT NOT NULL,
  PRIMARY KEY (review_id, sc, finding_id)
);
CREATE TABLE IF NOT EXISTS measurements (
  review_id TEXT NOT NULL, run_id TEXT NOT NULL, kind TEXT NOT NULL,  -- probe / axe
  key TEXT NOT NULL, value TEXT,  -- JSON
  PRIMARY KEY (review_id, run_id, kind, key)
);
CREATE TABLE IF NOT EXISTS walkthrough_steps (
  review_id TEXT NOT NULL, file TEXT NOT NULL, step_id TEXT NOT NULL, ordinal INTEGER NOT NULL,
  title TEXT, key_step INTEGER NOT NULL, feedback TEXT,     -- '' = pending
  PRIMARY KEY (review_id, file, step_id)
);
CREATE TABLE IF NOT EXISTS coverage_boxes (
  review_id TEXT NOT NULL, box_no INTEGER NOT NULL, text TEXT, checked INTEGER NOT NULL,
  PRIMARY KEY (review_id, box_no)
);
CREATE TABLE IF NOT EXISTS sync_log (
  review_id TEXT NOT NULL, file TEXT NOT NULL, sha256 TEXT NOT NULL,
  PRIMARY KEY (review_id, file)
);
CREATE INDEX IF NOT EXISTS ix_co_sc ON criterion_outcomes(sc);
CREATE INDEX IF NOT EXISTS ix_ck_run ON check_outcomes(review_id, run_id);
CREATE INDEX IF NOT EXISTS ix_fc_sc ON finding_criteria(review_id, sc);
"""

GUIDELINES = {"1.1": "Text Alternatives", "1.2": "Time-based Media", "1.3": "Adaptable",
              "1.4": "Distinguishable", "2.1": "Keyboard Accessible", "2.2": "Enough Time",
              "2.3": "Seizures and Physical Reactions", "2.4": "Navigable", "2.5": "Input Modalities",
              "3.1": "Readable", "3.2": "Predictable", "3.3": "Input Assistance", "4.1": "Compatible"}
ADDED_21 = {"1.3.4", "1.3.5", "1.4.10", "1.4.11", "1.4.12", "1.4.13", "2.1.4",
            "2.5.1", "2.5.2", "2.5.3", "2.5.4", "4.1.3"}
ADDED_22 = {"2.4.11", "2.5.7", "2.5.8", "3.2.6", "3.3.7", "3.3.8"}
FINDING_ID = r"\b[A-Z]+\d*-F\d+\b"


def connect(target):
    """Open a review's database (pass the review dir), a raw path, or ':memory:'."""
    if target == ":memory:":
        path = ":memory:"
    else:
        t = pathlib.Path(target)
        path = db_path(t) if t.is_dir() else t
    con = sqlite3.connect(str(path))
    con.execute("PRAGMA foreign_keys = OFF")
    con.executescript(SCHEMA)
    return con


def dump_hash(path):
    """Canonical content hash of a database (schema + rows), independent of page layout."""
    if not pathlib.Path(path).exists():
        return None
    con = sqlite3.connect(str(path))
    h = hashlib.sha256()
    for line in con.iterdump():
        h.update(line.encode("utf-8")); h.update(b"\n")
    con.close()
    return h.hexdigest()


def sort_key(sc):
    return ".".join(f"{int(x):03d}" for x in sc.split("."))


def slug(name):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", name.lower())).strip("-")


# --------------------------------------------------------------------------
def seed(con):
    """Criteria (from the 05 template — the conformance target), FPC, checks."""
    rows = []
    for sc, name, level in rv.sc_targets():
        g = ".".join(sc.split(".")[:2])
        ver = "2.2" if sc in ADDED_22 else "2.1" if sc in ADDED_21 else "2.0"
        rows.append((sc, name, level, int(sc[0]), rv.PRINCIPLES[sc[0]], g, GUIDELINES[g], ver, 1,
                     f"https://www.w3.org/WAI/WCAG22/Understanding/{slug(name)}.html", sort_key(sc)))
    con.executemany("INSERT OR REPLACE INTO wcag_criteria VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows)
    con.executemany("INSERT OR REPLACE INTO fpc VALUES (?,?,?)",
                    [(code, name, m) for m, lst in rv.FPC.items() for code, name in lst])
    cmap = rv.check_map()
    con.execute("DELETE FROM check_criteria")
    con.execute("DELETE FROM checks")
    con.executemany("INSERT INTO checks VALUES (?,?,?)",
                    [(cid, v["modality"], v["text"]) for cid, v in cmap.items()])
    con.executemany("INSERT INTO check_criteria VALUES (?,?)",
                    [(cid, sc) for cid, v in cmap.items() for sc in sorted(v["sc"])])
    con.commit()
    return len(rows), len(cmap)


# --------------------------------------------------------------------------
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_views(review):
    text = rv.read(review / rv.STAGES[2])
    out = []
    for m in re.finditer(r"(?m)^\|\s*([SR]\d+)\s*\|(.*)$", text):
        cells = [c.strip() for c in m.group(2).strip().strip("|").split("|")]
        name = cells[0] if cells else ""
        if not name:
            continue
        out.append((m.group(1), name, cells[1] if len(cells) > 1 else "",
                    cells[2] if len(cells) > 2 else "",
                    "random" if m.group(1).startswith("R") else "structured"))
    return out


def parse_tasks(review):
    text = rv.read(review / rv.STAGES[3])
    out = []
    for block in re.split(r"(?=^### Task )", text, flags=re.M):
        head = re.match(r"### Task (\S+) — (.*)", block)
        if not head:
            continue
        def cell(label):
            m = re.search(rf"\|\s*\*\*{re.escape(label)}\*\*\s*\|\s*(.*?)\s*\|", block)
            return m.group(1) if m else ""
        verdict = cell("Verdict")
        if verdict == rv.VERDICT_PLACEHOLDER:
            verdict = "Not run"
        out.append((head.group(1), head.group(2).strip(), verdict, cell("Baselines run"), cell("Date(s) tested")))
    return out


def parse_findings(review):
    text = rv.read(review / rv.STAGES[3])
    section = "view"
    out = []
    for block in re.split(r"(?=^#### Finding |^## [A-D]\. )", text, flags=re.M):
        if block.startswith("## A."):
            section = "task"
        elif re.match(r"## [B-D]\.", block):
            section = "view"
        head = re.match(r"#### Finding (\S+)", block)
        if not head:
            continue
        fields = {m.group(1): m.group(2).strip()
                  for m in re.finditer(r"(?m)^\|\s*\*\*([^*]+)\*\*\s*\|\s*(.*?)\s*\|\s*$", block)}
        crit_cell = fields.get("WCAG criteria failed", "")
        criteria = sorted(set(re.findall(r"\b\d\.\d\.\d+\b", crit_cell)))
        observed = fields.get("Observed", "")
        withdrawn = 1 if re.search(r"withdrawn", crit_cell + " " + observed[:120] + " " + fields.get("Severity", ""), re.I) else 0
        where = fields.get("Where", "") or fields.get("Step", "")
        vm = re.match(r"\s*([SR]\d+)\b", where)
        tm = re.match(r"T(\d+)-", head.group(1))
        evidence = fields.get("Evidence", "")
        runs = sorted(set(re.findall(r"\bR\d{3}\b", evidence + " " + observed)))
        out.append({"id": head.group(1), "section": section,
                    "view": vm.group(1) if vm else "", "task": f"T{tm.group(1)}" if tm else "",
                    "where": where, "observed": observed, "affected": fields.get("Affected users", ""),
                    "severity": fields.get("Severity", ""), "evidence": evidence, "withdrawn": withdrawn,
                    "criteria": criteria, "runs": runs, "fields": fields})
    return out


def parse_criterion_outcomes(review):
    out = []
    for block in re.split(r"(?=^### )", rv.read(review / rv.STAGES[4]), flags=re.M):
        h = re.match(r"### (\d+\.\d+\.\d+) ", block)
        if not h:
            continue
        def cell(label):
            # [ \t]* not \s*: an empty cell must not swallow the next line
            m = re.search(rf"- \*\*{label}:\*\*[ \t]*(.*)", block)
            return m.group(1).strip() if m else ""
        raw = cell("Outcome")
        norm = next((x for x in rv.OUTCOMES if raw.startswith(x)), raw or "Not Evaluated")
        tf = cell("Task findings")
        out.append((h.group(1), norm, raw, cell("Vendor claim"), tf, cell("Remarks"),
                    sorted(set(re.findall(FINDING_ID, tf)))))
    return out


def parse_observations(run_dir):
    text = rv.read(run_dir / "run.md")
    out = []
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = re.match(r"^- O(\d+)\s*(?:\[([^\]]+)\])?\s*(.*)$", ln)
        if not m:
            continue
        classified = ""
        for nxt in lines[i + 1:i + 4]:
            c = re.match(r"^\s+- Classified:\s*(.*)$", nxt)
            if c:
                classified = c.group(1).strip()
                break
        out.append((f"O{m.group(1)}", m.group(2) or "", m.group(3).strip(), classified))
    return out


def parse_measurements(run_dir):
    rows = []
    for pj in run_dir.glob("*-probe.json"):
        try:
            F = json.loads(pj.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            rows.append(("probe", "parse_error", json.dumps(str(e))))
            continue
        summary = {"title": F.get("title"), "lang": F.get("lang"), "href": F.get("href"),
                   "media": F.get("media"), "passwordFields": F.get("passwordFields"),
                   "script_hits": (F.get("scripts") or {}).get("hits"),
                   "targets_total": (F.get("targets") or {}).get("total"),
                   "targets_small": len((F.get("targets") or {}).get("small", [])),
                   "targets_failing": len((F.get("targets") or {}).get("failing", [])),
                   "reflow_scrollWidth": ((F.get("measurements") or {}).get("reflow") or {}).get("scrollWidth"),
                   "text_spacing_new_clips": len(((F.get("measurements") or {}).get("text_spacing") or {}).get("after", [])),
                   "animation": F.get("animation"), "inputs": F.get("inputs")}
        rows.append(("probe", "summary", json.dumps(summary, ensure_ascii=False)))
        rows.append(("probe", "facts", json.dumps(F, ensure_ascii=False)))
    for aj in run_dir.glob("*-axe.json"):
        try:
            A = json.loads(aj.read_text(encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            rows.append(("axe", "parse_error", json.dumps(str(e))))
            continue
        res = A.get("results", A) if isinstance(A, dict) else {}
        for bucket in ("violations", "incomplete"):
            for item in res.get(bucket, []) or []:
                rows.append(("axe", f"{bucket}:{item.get('id')}",
                             json.dumps({"impact": item.get("impact"), "nodes": len(item.get("nodes", [])),
                                         "tags": item.get("tags"), "help": item.get("help")}, ensure_ascii=False)))
        rows.append(("axe", "summary", json.dumps({b: len(res.get(b, []) or []) for b in ("violations", "incomplete", "passes", "inapplicable")})))
    return rows


def sync_review(con, review):
    rid = review.name
    cur = con.cursor()
    for t in ("views", "tasks", "runs", "check_outcomes", "observations", "findings", "finding_criteria",
              "finding_runs", "criterion_outcomes", "criterion_findings", "measurements", "coverage_boxes",
              "walkthrough_steps", "sync_log"):
        cur.execute(f"DELETE FROM {t} WHERE review_id = ?", (rid,))
    status = re.search(r"\|\s*\*\*Report status\*\*\s*\|\s*(.*?)\s*\|", rv.read(review / rv.STAGES[5]))
    source = hashlib.sha256(b"".join((review / st).read_bytes() for st in rv.STAGES if (review / st).exists())).hexdigest()
    cur.execute("INSERT OR REPLACE INTO reviews VALUES (?,?,?,?,?)",
                (rid, rv.product_name(review), rv.decision(review), status.group(1) if status else "", source))
    cur.executemany("INSERT INTO views VALUES (?,?,?,?,?,?)",
                    [(rid, vid, n, loc, rep, kind) for vid, n, loc, rep, kind in parse_views(review)])
    cur.executemany("INSERT INTO tasks VALUES (?,?,?,?,?,?)",
                    [(rid, *t) for t in parse_tasks(review)])
    boxes = re.findall(r"(?m)^- \[( |x|X)\]\s*(.*)$", rv.read(review / rv.STAGES[3]))
    cur.executemany("INSERT INTO coverage_boxes VALUES (?,?,?,?)",
                    [(rid, i + 1, text.strip(), 0 if mark == " " else 1) for i, (mark, text) in enumerate(boxes)])
    # reviewer-session walkthroughs: each "### W# — title" step and whether its
    # **Feedback:** line is still _(pending)_ — "where we left off" as data
    for wf in sorted(review.glob("session-*walkthrough.md")):
        text = rv.read(wf)
        steps = list(re.finditer(r"(?m)^### (W[\w-]+) — (.+?)\s*$", text))
        for i, m in enumerate(steps):
            body = text[m.end():steps[i + 1].start() if i + 1 < len(steps) else len(text)]
            fbs = re.findall(r"(?m)^\*\*Feedback[^*]*:\*\*\s*(.*)$", body)
            pending = (not fbs) or all(re.match(r"_\(pending\)_", f.strip()) for f in fbs)
            cur.execute("INSERT OR REPLACE INTO walkthrough_steps VALUES (?,?,?,?,?,?,?)",
                        (rid, wf.name, m.group(1), i + 1, m.group(2).strip(),
                         1 if "KEY STEP" in m.group(2) else 0,
                         "" if pending else " / ".join(f.strip()[:200] for f in fbs if not f.strip().startswith("_(pending)_"))))
        cur.execute("INSERT OR REPLACE INTO sync_log VALUES (?,?,?)", (rid, wf.name, sha(wf)))
    for f in parse_findings(review):
        cur.execute("INSERT INTO findings VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (rid, f["id"], f["section"], f["view"], f["task"], f["where"], f["observed"],
                     f["affected"], f["severity"], f["evidence"], f["withdrawn"],
                     json.dumps(f["fields"], ensure_ascii=False)))
        cur.executemany("INSERT OR IGNORE INTO finding_criteria VALUES (?,?,?)", [(rid, f["id"], sc) for sc in f["criteria"]])
        cur.executemany("INSERT OR IGNORE INTO finding_runs VALUES (?,?,?)", [(rid, f["id"], r) for r in f["runs"]])
    for sc, norm, raw, claim, tf, remarks, fids in parse_criterion_outcomes(review):
        cur.execute("INSERT INTO criterion_outcomes VALUES (?,?,?,?,?,?,?)", (rid, sc, norm, raw, claim, tf, remarks))
        cur.executemany("INSERT OR IGNORE INTO criterion_findings VALUES (?,?,?)", [(rid, sc, fid) for fid in fids])
    for d in rv.run_dirs(review):
        meta = rv.run_meta(d)
        full = re.search(r"\|\s*\*\*Result\*\*\s*\|\s*(.*?)\s*\|", rv.read(d / "run.md"))
        cur.execute("INSERT INTO runs VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (rid, meta["run"], meta["date"], meta["view"], meta["url"], meta["task"], meta["modality"],
                     meta["tool"], meta["baseline"], meta["tester"], meta["result"], full.group(1) if full else ""))
        raw_rows = re.findall(r"(?m)^\|\s*([A-Z]+\d+)\s*—\s*.+?\s*\|(.*?)\|", rv.read(d / "run.md"))
        raw_map = {cid: o.strip() for cid, o in raw_rows}
        cur.executemany("INSERT OR REPLACE INTO check_outcomes VALUES (?,?,?,?,?,?)",
                        [(rid, meta["run"], cid, outcome, raw_map.get(cid, ""), note)
                         for cid, outcome, note in rv.run_checks(d)])
        cur.executemany("INSERT OR REPLACE INTO observations VALUES (?,?,?,?,?,?)",
                        [(rid, meta["run"], *o) for o in parse_observations(d)])
        cur.executemany("INSERT OR REPLACE INTO measurements VALUES (?,?,?,?,?)",
                        [(rid, meta["run"], *m) for m in parse_measurements(d)])
        cur.execute("INSERT OR REPLACE INTO sync_log VALUES (?,?,?)", (rid, f"evidence/runs/{d.name}/run.md", sha(d / "run.md")))
    for s in rv.STAGES:
        p = review / s
        if p.exists():
            cur.execute("INSERT OR REPLACE INTO sync_log VALUES (?,?,?)", (rid, s, sha(p)))
    con.commit()
    counts = {t: cur.execute(f"SELECT COUNT(*) FROM {t} WHERE review_id=?", (rid,)).fetchone()[0]
              for t in ("views", "tasks", "runs", "check_outcomes", "observations", "findings",
                        "criterion_outcomes", "measurements")}
    return counts


def sync(review=None, quiet=False):
    """Public entry point used by review.py / view_probe.py: rebuild one or all
    review databases. Byte-stable: the rebuild happens in a temp file and
    replaces reviews/<id>/<id>.sqlite only when the canonical dump differs."""
    targets = [review] if review else [d for d in rv.REVIEWS.iterdir() if d.is_dir() and (d / rv.STAGES[0]).exists()]
    out = {}
    for r in targets:
        final = db_path(r)
        tmp = final.with_suffix(".sqlite.tmp")
        if tmp.exists():
            tmp.unlink()
        con = connect(tmp)
        seed(con)
        counts = sync_review(con, r)
        con.execute("VACUUM")
        con.close()
        changed = dump_hash(tmp) != dump_hash(final)
        if changed:
            tmp.replace(final)
        else:
            tmp.unlink()
        counts["changed"] = changed
        out[r.name] = counts
        # the HTML dashboard is derived from the database exactly as the
        # database is derived from the files — regenerate it here so it is
        # never more than one command behind (scripts/dashboard.py)
        try:
            import dashboard
            dashboard.write(r)
        except Exception as ex:  # noqa: BLE001 — the DB is the measure; the page is a view of it
            if not quiet:
                print(f"(dashboard not rendered: {ex})", file=sys.stderr)
        if not quiet:
            print(f"synced {r.name} → {final.relative_to(ROOT)}"
                  + (" (updated)" if changed else " (unchanged — file untouched)") + ": "
                  + ", ".join(f"{k}={v}" for k, v in counts.items() if k != "changed"))
    return out


# --------------------------------------------------------------------------
INTEGRITY = [
    ("outcome without check evidence",
     "05 Outcome set but no check mapped to the criterion is answered in any run",
     """SELECT co.sc || ' (' || co.outcome || ')' FROM criterion_outcomes co
        WHERE co.review_id=:r AND co.outcome <> 'Not Evaluated'
          AND NOT EXISTS (SELECT 1 FROM check_outcomes ck JOIN check_criteria cc ON cc.check_id=ck.check_id
                          WHERE ck.review_id=co.review_id AND cc.sc=co.sc AND ck.outcome IN ('pass','fail','partial','n/a'))
        ORDER BY co.sc"""),
    ("failed check, 05 undecided",
     "a fail/partial check outcome on a criterion whose 05 Outcome is still Not Evaluated",
     """SELECT DISTINCT cc.sc || ' via ' || ck.check_id || '@' || ck.run_id FROM check_outcomes ck
        JOIN check_criteria cc ON cc.check_id=ck.check_id
        JOIN criterion_outcomes co ON co.review_id=ck.review_id AND co.sc=cc.sc
        WHERE ck.review_id=:r AND ck.outcome IN ('fail','partial') AND co.outcome='Not Evaluated'
        ORDER BY cc.sc"""),
    ("finding not rolled up",
     "a live finding names a criterion whose 05 block does not cite the finding",
     """SELECT f.finding_id || ' → ' || fc.sc FROM findings f JOIN finding_criteria fc USING (review_id, finding_id)
        WHERE f.review_id=:r AND f.withdrawn=0
          AND NOT EXISTS (SELECT 1 FROM criterion_findings cf WHERE cf.review_id=f.review_id AND cf.sc=fc.sc AND cf.finding_id=f.finding_id)
        ORDER BY f.finding_id"""),
    ("05 cites unknown finding",
     "a 05 block cites a finding ID that does not exist in 04",
     """SELECT cf.sc || ' cites ' || cf.finding_id FROM criterion_findings cf
        WHERE cf.review_id=:r AND NOT EXISTS (SELECT 1 FROM findings f WHERE f.review_id=cf.review_id AND f.finding_id=cf.finding_id)"""),
    ("05 cites withdrawn finding",
     "a 05 block still cites a finding marked withdrawn",
     """SELECT cf.sc || ' cites ' || cf.finding_id FROM criterion_findings cf JOIN findings f USING (review_id, finding_id)
        WHERE cf.review_id=:r AND f.withdrawn=1"""),
    ("Supports despite live finding",
     "05 says Supports on a criterion that a live finding says fails",
     """SELECT DISTINCT fc.sc || ' (' || f.finding_id || ', ' || f.severity || ')' FROM finding_criteria fc
        JOIN findings f USING (review_id, finding_id) JOIN criterion_outcomes co ON co.review_id=fc.review_id AND co.sc=fc.sc
        WHERE fc.review_id=:r AND f.withdrawn=0 AND co.outcome IN ('Supports','Not Applicable')"""),
    ("finding cites missing run",
     "a finding's evidence names a run folder that does not exist",
     """SELECT fr.finding_id || ' cites ' || fr.run_id FROM finding_runs fr
        WHERE fr.review_id=:r AND NOT EXISTS (SELECT 1 FROM runs r WHERE r.review_id=fr.review_id AND r.run_id=fr.run_id)"""),
    ("finding without run evidence",
     "a live finding cites no run at all (CLAUDE.md: no run, no finding)",
     """SELECT f.finding_id FROM findings f WHERE f.review_id=:r AND f.withdrawn=0
        AND NOT EXISTS (SELECT 1 FROM finding_runs fr WHERE fr.review_id=f.review_id AND fr.finding_id=f.finding_id)"""),
    ("finding cites unknown criterion",
     "a finding names a criterion outside the WCAG 2.2 AA target",
     """SELECT fc.finding_id || ' → ' || fc.sc FROM finding_criteria fc
        WHERE fc.review_id=:r AND fc.sc NOT IN (SELECT sc FROM wcag_criteria)"""),
    ("Result set with blank checks",
     "a run has a Result but unanswered check rows (Works requires every check answered)",
     """SELECT r.run_id || ' (' || r.result || '): ' || GROUP_CONCAT(ck.check_id) FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
        WHERE r.review_id=:r AND r.result NOT IN ('Not set','N/A') AND ck.outcome='' GROUP BY r.run_id"""),
    ("Works with a failed check",
     "a run says Works but a check in it failed",
     """SELECT r.run_id || ': ' || GROUP_CONCAT(ck.check_id) FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
        WHERE r.review_id=:r AND r.result='Works' AND ck.outcome IN ('fail','partial') GROUP BY r.run_id"""),
    ("run on unsampled view",
     "a run names a view that is not an S#/R# row in 03",
     """SELECT r.run_id || ' → ' || r.view_id FROM runs r WHERE r.review_id=:r
        AND NOT EXISTS (SELECT 1 FROM views v WHERE v.review_id=r.review_id AND UPPER(v.view_id)=UPPER(r.view_id))"""),
    ("unrecognised check outcome",
     "outcome cell is not pass/fail/partial/n/a",
     """SELECT run_id || ' ' || check_id || ' = ' || raw FROM check_outcomes WHERE review_id=:r AND outcome='?'"""),
]


def integrity(con, rid):
    issues = []
    for title, desc, sql in INTEGRITY:
        rows = [r[0] for r in con.execute(sql, {"r": rid}).fetchall()]
        if rows:
            issues.append({"check": title, "description": desc, "count": len(rows), "items": rows})
    return issues


# --------------------------------------------------------------------------
# Definition of done — the DB is the measure of review completion
# (ontology/data-store.md §Definition of done). Each predicate is a pair of
# queries: done / total, plus a query listing what is missing.
# --------------------------------------------------------------------------
COMPLETION = [
    ("C1 criteria decided", "every target criterion has a 05 Outcome other than Not Evaluated",
     "SELECT COUNT(*) FROM criterion_outcomes WHERE review_id=:r AND outcome<>'Not Evaluated'",
     "SELECT COUNT(*) FROM wcag_criteria WHERE in_target=1",
     "SELECT sc FROM criterion_outcomes WHERE review_id=:r AND outcome='Not Evaluated' ORDER BY sc"),
    ("C2 criteria evidenced", "every target criterion has at least one answered check in a run",
     """SELECT COUNT(DISTINCT cc.sc) FROM check_outcomes ck JOIN check_criteria cc USING (check_id)
        WHERE ck.review_id=:r AND ck.outcome IN ('pass','fail','partial','n/a')""",
     "SELECT COUNT(*) FROM wcag_criteria WHERE in_target=1",
     """SELECT sc FROM wcag_criteria w WHERE in_target=1 AND NOT EXISTS (
          SELECT 1 FROM check_outcomes ck JOIN check_criteria cc USING (check_id)
          WHERE ck.review_id=:r AND cc.sc=w.sc AND ck.outcome IN ('pass','fail','partial','n/a')) ORDER BY sort_key"""),
    ("C3 tasks verdict", "every task cluster has a verdict",
     "SELECT COUNT(*) FROM tasks WHERE review_id=:r AND verdict IN ('Pass','Pass with barriers','Fail')",
     "SELECT COUNT(*) FROM tasks WHERE review_id=:r",
     "SELECT task_id || ' (' || verdict || ')' FROM tasks WHERE review_id=:r AND verdict NOT IN ('Pass','Pass with barriers','Fail')"),
    ("C4 runs resulted", "every run has a Result",
     "SELECT COUNT(*) FROM runs WHERE review_id=:r AND result IN ('Works','Works with issues','Broken','N/A')",
     "SELECT COUNT(*) FROM runs WHERE review_id=:r",
     "SELECT run_id FROM runs WHERE review_id=:r AND result NOT IN ('Works','Works with issues','Broken','N/A')"),
    ("C5 checks answered", "every check row in every run has an outcome",
     "SELECT COUNT(*) FROM check_outcomes WHERE review_id=:r AND outcome IN ('pass','fail','partial','n/a')",
     "SELECT COUNT(*) FROM check_outcomes WHERE review_id=:r",
     "SELECT run_id || ' ' || check_id FROM check_outcomes WHERE review_id=:r AND outcome NOT IN ('pass','fail','partial','n/a')"),
    ("C6 cells run", "every sampled view × modality has a run with a Result",
     """SELECT COUNT(*) FROM views v CROSS JOIN fpc_mod m WHERE v.review_id=:r AND EXISTS (
          SELECT 1 FROM runs r WHERE r.review_id=v.review_id AND UPPER(r.view_id)=UPPER(v.view_id)
          AND r.modality=m.modality AND r.result IN ('Works','Works with issues','Broken','N/A'))""",
     "SELECT COUNT(*) FROM views v CROSS JOIN fpc_mod m WHERE v.review_id=:r",
     """SELECT v.view_id || '×' || m.modality FROM views v CROSS JOIN fpc_mod m WHERE v.review_id=:r AND NOT EXISTS (
          SELECT 1 FROM runs r WHERE r.review_id=v.review_id AND UPPER(r.view_id)=UPPER(v.view_id)
          AND r.modality=m.modality AND r.result IN ('Works','Works with issues','Broken','N/A'))"""),
    ("C7 views swept", "every sampled view has an automated sweep run (axe/wave)",
     """SELECT COUNT(*) FROM views v WHERE v.review_id=:r AND EXISTS (
          SELECT 1 FROM runs r WHERE r.review_id=v.review_id AND UPPER(r.view_id)=UPPER(v.view_id) AND LOWER(r.tool) IN ('axe','wave'))""",
     "SELECT COUNT(*) FROM views WHERE review_id=:r",
     """SELECT view_id FROM views v WHERE v.review_id=:r AND NOT EXISTS (
          SELECT 1 FROM runs r WHERE r.review_id=v.review_id AND UPPER(r.view_id)=UPPER(v.view_id) AND LOWER(r.tool) IN ('axe','wave'))"""),
    ("C8 FPC exercised", "every 508 FPC has an answered check on at least one view",
     """SELECT COUNT(*) FROM fpc f WHERE EXISTS (
          SELECT 1 FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
          WHERE r.review_id=:r AND r.modality=f.modality AND ck.outcome IN ('pass','fail','partial','n/a'))""",
     "SELECT COUNT(*) FROM fpc",
     """SELECT code || ' ' || name FROM fpc f WHERE NOT EXISTS (
          SELECT 1 FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
          WHERE r.review_id=:r AND r.modality=f.modality AND ck.outcome IN ('pass','fail','partial','n/a'))"""),
    ("C9 findings evidenced", "every live finding names a criterion, a severity and a run",
     """SELECT COUNT(*) FROM findings f WHERE review_id=:r AND withdrawn=0 AND severity<>''
        AND EXISTS (SELECT 1 FROM finding_criteria fc WHERE fc.review_id=f.review_id AND fc.finding_id=f.finding_id)
        AND EXISTS (SELECT 1 FROM finding_runs fr WHERE fr.review_id=f.review_id AND fr.finding_id=f.finding_id)""",
     "SELECT COUNT(*) FROM findings WHERE review_id=:r AND withdrawn=0",
     """SELECT finding_id FROM findings f WHERE review_id=:r AND withdrawn=0 AND NOT (severity<>''
        AND EXISTS (SELECT 1 FROM finding_criteria fc WHERE fc.review_id=f.review_id AND fc.finding_id=f.finding_id)
        AND EXISTS (SELECT 1 FROM finding_runs fr WHERE fr.review_id=f.review_id AND fr.finding_id=f.finding_id))"""),
    ("C10 coverage boxes", "every 04 §D coverage box is checked",
     "SELECT COUNT(*) FROM coverage_boxes WHERE review_id=:r AND checked=1",
     "SELECT COUNT(*) FROM coverage_boxes WHERE review_id=:r",
     "SELECT 'box ' || box_no || ': ' || substr(text,1,60) FROM coverage_boxes WHERE review_id=:r AND checked=0"),
    ("C11 integrity clean", "no integrity issue (see `check`)",
     None, None, None),
    ("C12 decision (human)", "06 procurement decision set and report status FINAL — the reviewer's act, never the assistant's",
     """SELECT (decision NOT IN ('Pending','')) + (report_status LIKE 'FINAL%') FROM reviews WHERE review_id=:r""",
     "SELECT 2",
     """SELECT CASE WHEN decision IN ('Pending','') THEN 'decision not set' END FROM reviews WHERE review_id=:r
        UNION ALL SELECT CASE WHEN report_status NOT LIKE 'FINAL%' THEN 'report status ' || report_status END FROM reviews WHERE review_id=:r"""),
]


def completion(con, rid):
    """Rows of the definition of done: name, description, done, total, missing[]."""
    con.execute("DROP VIEW IF EXISTS fpc_mod")
    con.execute("CREATE TEMP VIEW fpc_mod AS SELECT DISTINCT modality FROM fpc")
    rows = []
    for name, desc, q_done, q_total, q_missing in COMPLETION:
        if q_done is None:  # integrity
            iss = integrity(con, rid)
            n_iss = sum(i["count"] for i in iss)
            rows.append({"name": name, "description": desc, "done": 0 if n_iss else 1, "total": 1,
                         "missing": [f"{i['check']} ({i['count']})" for i in iss]})
            continue
        done = con.execute(q_done, {"r": rid}).fetchone()[0] or 0
        total = con.execute(q_total, {"r": rid}).fetchone()[0] or 0
        missing = [r[0] for r in con.execute(q_missing, {"r": rid}).fetchall() if r[0]]
        rows.append({"name": name, "description": desc, "done": done, "total": total, "missing": missing})
    return rows


def print_completion(rid, rows):
    satisfied = sum(1 for r in rows if r["total"] and r["done"] >= r["total"])
    print(f"Completion — {rid}: {satisfied}/{len(rows)} predicates satisfied"
          f"  ({'COMPLETE' if satisfied == len(rows) else 'INCOMPLETE'})\n")
    w = max(len(r["name"]) for r in rows)
    for r in rows:
        ok = r["total"] and r["done"] >= r["total"]
        pct = f"{100 * r['done'] / r['total']:5.1f}%" if r["total"] else "   —  "
        mark = "✓" if ok else "✗"
        print(f"  {mark} {r['name']:<{w}}  {r['done']:>4}/{r['total']:<4} {pct}  {r['description']}")
        if not ok and r["missing"]:
            head = ", ".join(str(m) for m in r["missing"][:8])
            more = f" … +{len(r['missing']) - 8}" if len(r["missing"]) > 8 else ""
            print(f"      missing: {head}{more}")


# --------------------------------------------------------------------------
# Review state — one deterministic dashboard from the mirror, repeatable
# (same files → same text) and loggable (--log appends a snapshot row to
# reviews/<id>/state-log.md and prints the delta since the previous one).
# --------------------------------------------------------------------------
MOD_ABBR = {"no-vision": "NV", "low-vision": "LV", "no-color": "NC", "no-hearing": "NH",
            "no-speech": "NS", "motor": "MO", "cognition": "CO"}
RESULT_GLYPH = {"Works": "✓", "Works with issues": "!", "Broken": "✗", "N/A": "n", "Not set": "?"}
CLAIM_RANK = {"Supports": 3, "Not Applicable": 3, "Partially Supports": 2, "Does Not Support": 1}


def bar(done, total, width=20):
    if not total:
        return "·" * width
    n = round(width * min(done, total) / total)
    return "█" * n + "░" * (width - n)


def state_data(con, rid):
    q = lambda sql, **kw: con.execute(sql, {"r": rid, **kw}).fetchall()  # noqa: E731
    rev = con.execute("SELECT product, decision, report_status, source_sha FROM reviews WHERE review_id=?", (rid,)).fetchone()
    done = completion(con, rid)
    # POUR
    pour = []
    for pno, pname in sorted(rv.PRINCIPLES.items()):
        crit = [r[0] for r in q("SELECT sc FROM wcag_criteria WHERE principle_no=:p AND in_target=1", p=int(pno))]
        decided = q("SELECT COUNT(*) FROM criterion_outcomes WHERE review_id=:r AND outcome<>'Not Evaluated' AND sc IN (SELECT sc FROM wcag_criteria WHERE principle_no=:p)", p=int(pno))[0][0]
        failing = q("SELECT COUNT(*) FROM criterion_outcomes WHERE review_id=:r AND outcome IN ('Partially Supports','Does Not Support') AND sc IN (SELECT sc FROM wcag_criteria WHERE principle_no=:p)", p=int(pno))[0][0]
        evidenced = q("""SELECT COUNT(DISTINCT cc.sc) FROM check_outcomes ck JOIN check_criteria cc USING (check_id)
                         JOIN wcag_criteria w ON w.sc=cc.sc WHERE ck.review_id=:r AND w.principle_no=:p
                         AND ck.outcome IN ('pass','fail','partial','n/a')""", p=int(pno))[0][0]
        pour.append({"principle": f"{pno} {pname}", "criteria": len(crit), "decided": decided,
                     "evidenced": evidenced, "failing": failing})
    # FPC
    n_views = q("SELECT COUNT(*) FROM views WHERE review_id=:r")[0][0]
    fpc = []
    for m in rv.REQUIRED_MODALITIES:
        codes = ", ".join(c for c, _ in rv.FPC[m])
        views_resulted = q("""SELECT COUNT(DISTINCT UPPER(view_id)) FROM runs WHERE review_id=:r AND modality=:m
                              AND result IN ('Works','Works with issues','Broken','N/A')""", m=m)[0][0]
        views_any = q("SELECT COUNT(DISTINCT UPPER(view_id)) FROM runs WHERE review_id=:r AND modality=:m", m=m)[0][0]
        ans, blank, fails = q("""SELECT SUM(ck.outcome IN ('pass','fail','partial','n/a')), SUM(ck.outcome=''),
                                 SUM(ck.outcome IN ('fail','partial')) FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
                                 WHERE r.review_id=:r AND r.modality=:m""", m=m)[0]
        fpc.append({"fpc": codes, "modality": m, "views_resulted": views_resulted, "views_any": views_any,
                    "views": n_views, "answered": ans or 0, "blank": blank or 0, "fails": fails or 0})
    # matrix
    views = q("SELECT view_id, name FROM views WHERE review_id=:r ORDER BY CASE WHEN view_id LIKE 'S%' THEN 0 ELSE 1 END, CAST(substr(view_id,2) AS INTEGER)")
    matrix = []
    for vid, name in views:
        cells = {}
        for m in rv.REQUIRED_MODALITIES:
            row = q("SELECT result FROM runs WHERE review_id=:r AND UPPER(view_id)=UPPER(:v) AND modality=:m ORDER BY run_id DESC LIMIT 1", v=vid, m=m)
            cells[m] = RESULT_GLYPH.get(row[0][0], "?") if row else "·"
        swept = bool(q("SELECT 1 FROM runs WHERE review_id=:r AND UPPER(view_id)=UPPER(:v) AND LOWER(tool) IN ('axe','wave') LIMIT 1", v=vid))
        matrix.append({"view": vid, "name": name, "cells": cells, "swept": swept})
    # findings
    sev = {"Blocker": 0, "Major": 0, "Minor": 0, "unrated": 0}
    for (s,) in q("SELECT severity FROM findings WHERE review_id=:r AND withdrawn=0"):
        m = re.search(r"Blocker|Major|Minor", s or "")
        sev[m.group(0) if m else "unrated"] += 1
    withdrawn = q("SELECT COUNT(*) FROM findings WHERE review_id=:r AND withdrawn=1")[0][0]
    tasks_ = q("SELECT task_id, verdict FROM tasks WHERE review_id=:r ORDER BY task_id")
    # vendor
    worse = better = same = 0
    for claim, outcome in q("SELECT vendor_claim, outcome FROM criterion_outcomes WHERE review_id=:r AND outcome<>'Not Evaluated'"):
        c = next((k for k in ("Partially Supports", "Does Not Support", "Not Applicable", "Supports") if (claim or "").startswith(k)), None)
        if not c:
            continue
        d = CLAIM_RANK.get(outcome, 0) - CLAIM_RANK[c]
        worse += d < 0; better += d > 0; same += d == 0
    integ = integrity(con, rid)
    # measured fails awaiting a decision, grouped
    measured = q("""SELECT cc.sc, ck.check_id, COUNT(*) FROM check_outcomes ck JOIN check_criteria cc USING (check_id)
                    JOIN criterion_outcomes co ON co.review_id=ck.review_id AND co.sc=cc.sc
                    WHERE ck.review_id=:r AND ck.outcome IN ('fail','partial') AND co.outcome='Not Evaluated'
                    GROUP BY cc.sc, ck.check_id ORDER BY 3 DESC, 1""")
    unanswered_by_mod = q("""SELECT r.modality, COUNT(*) FROM runs r JOIN check_outcomes ck USING (review_id, run_id)
                             WHERE r.review_id=:r AND ck.outcome='' GROUP BY r.modality ORDER BY 2 DESC""")
    walkthrough = q("""SELECT file, step_id, title, key_step FROM walkthrough_steps WHERE review_id=:r AND feedback=''
                       ORDER BY file, ordinal""")
    wt_total = q("SELECT COUNT(*) FROM walkthrough_steps WHERE review_id=:r")[0][0]
    return {"review": rid, "product": rev[0] if rev else "", "decision": rev[1] if rev else "",
            "walkthrough_pending": [{"file": f, "step": s, "title": t, "key": bool(k)} for f, s, t, k in walkthrough],
            "walkthrough_total": wt_total,
            "report_status": rev[2] if rev else "", "source_sha": rev[3] if rev else "",
            "runs": q("SELECT COUNT(*) FROM runs WHERE review_id=:r")[0][0],
            "findings_live": sum(sev.values()), "findings_withdrawn": withdrawn, "severity": sev,
            "tasks": [{"task": t, "verdict": v} for t, v in tasks_],
            "completion": done, "pour": pour, "fpc": fpc, "matrix": matrix,
            "vendor": {"decided": worse + better + same, "worse": worse, "better": better, "same": same},
            "integrity": [{"check": i["check"], "count": i["count"]} for i in integ],
            "measured_pending": [{"sc": s, "check": c, "runs": n} for s, c, n in measured],
            "unanswered_by_modality": [{"modality": m, "rows": n} for m, n in unanswered_by_mod]}


def render_state(d):
    L = []
    sat = sum(1 for r in d["completion"] if r["total"] and r["done"] >= r["total"])
    L.append(f"REVIEW STATE — {d['review']} · {d['product']}")
    L.append(f"decision {d['decision']} · report {d['report_status'] or '—'} · runs {d['runs']} · "
             f"findings {d['findings_live']} live / {d['findings_withdrawn']} withdrawn · "
             f"tasks " + " ".join(f"{t['task']}={t['verdict']}" for t in d["tasks"]))
    L.append("")
    L.append(f"DEFINITION OF DONE  {sat}/{len(d['completion'])}  {bar(sat, len(d['completion']), 12)}")
    w = max(len(r["name"]) for r in d["completion"])
    for r in d["completion"]:
        ok = r["total"] and r["done"] >= r["total"]
        pct = f"{100 * r['done'] / r['total']:3.0f}%" if r["total"] else "  —"
        L.append(f"  {'✓' if ok else '✗'} {r['name']:<{w}}  {bar(r['done'], r['total'])} {pct}  {r['done']}/{r['total']}")
    L.append("")
    L.append(f"{'POUR':<18}{'criteria':>9}{'decided':>9}{'evidenced':>11}{'failing':>9}")
    for p in d["pour"]:
        L.append(f"{p['principle']:<18}{p['criteria']:>9}{p['decided']:>9}{p['evidenced']:>11}{p['failing']:>9}")
    L.append("")
    L.append(f"{'508 FPC':<14}{'modality':<12}{'views done':>11}{'answered':>10}{'blank':>7}{'fails':>7}")
    for f in d["fpc"]:
        L.append(f"{f['fpc']:<14}{f['modality']:<12}{f['views_resulted']:>4}/{f['views']:<6}{f['answered']:>10}{f['blank']:>7}{f['fails']:>7}")
    L.append("")
    wv = min(max(len(f"{m['view']} {m['name']}") for m in d["matrix"]) if d["matrix"] else 10, 58)
    L.append(f"{'VIEWS × MODALITIES (latest run)':<{wv}}  " + "  ".join(f"{MOD_ABBR[m]:>2}" for m in rv.REQUIRED_MODALITIES) + "  axe")
    for m in d["matrix"]:
        label = f"{m['view']} {m['name']}"[:wv]
        L.append(f"{label:<{wv}}  " + "  ".join(f"{m['cells'][k]:>2}" for k in rv.REQUIRED_MODALITIES) + f"   {'✓' if m['swept'] else '·'}")
    L.append("  ✓ works  ! with issues  ✗ broken  n n/a  ? logged, no result  · not run")
    L.append("")
    s = d["severity"]
    L.append(f"FINDINGS  Blocker {s['Blocker']} · Major {s['Major']} · Minor {s['Minor']}"
             + (f" · unrated {s['unrated']}" if s["unrated"] else ""))
    v = d["vendor"]
    L.append(f"VENDOR CLAIM vs VERIFIED  {v['decided']} decided: {v['worse']} worse than claimed · {v['better']} better · {v['same']} as claimed")
    L.append("INTEGRITY  " + (" · ".join(f"{i['check']} {i['count']}" for i in d["integrity"]) if d["integrity"] else "clean"))
    L.append("")
    L.append("WHAT MOVES THE NEEDLE")
    if d["walkthrough_pending"]:
        wp = d["walkthrough_pending"]
        L.append(f"  walkthrough: {len(wp)}/{d['walkthrough_total']} steps pending — "
                 + ", ".join(f"{s['step']}{'*' if s['key'] else ''}" for s in wp[:14])
                 + (f" … +{len(wp) - 14}" if len(wp) > 14 else "") + "   (* = KEY STEP)")
    if d["measured_pending"]:
        top = d["measured_pending"][:5]
        L.append("  05 decisions on measured fails: " + ", ".join(f"{m['sc']} ({m['check']}×{m['runs']})" for m in top)
                 + (f" … +{len(d['measured_pending']) - 5}" if len(d["measured_pending"]) > 5 else ""))
    if d["unanswered_by_modality"]:
        L.append("  unanswered check rows: " + ", ".join(
            f"{'sweep triage W1–W3' if u['modality'] in ('—', '') else u['modality']} {u['rows']}" for u in d["unanswered_by_modality"]))
    not_run = [t["task"] for t in d["tasks"] if t["verdict"] not in ("Pass", "Pass with barriers", "Fail")]
    if not_run:
        L.append("  task walks without a verdict: " + ", ".join(not_run))
    unexercised = [f["fpc"] for f in d["fpc"] if f["answered"] == 0]
    if unexercised:
        L.append("  FPC never exercised: " + ", ".join(unexercised))
    return "\n".join(L)


def log_state(review, d, con):
    """Append a snapshot row to reviews/<id>/state-log.md; return the previous row (dict) if any."""
    path = review / "state-log.md"
    cols = ["date", "done"] + [r["name"].split(" ")[0] for r in d["completion"]] + ["runs", "findings", "integrity"]
    vals = [datetime.date.today().isoformat(),
            f"{sum(1 for r in d['completion'] if r['total'] and r['done'] >= r['total'])}/{len(d['completion'])}"] \
        + [f"{r['done']}/{r['total']}" for r in d["completion"]] \
        + [str(d["runs"]), str(d["findings_live"]), str(sum(i["count"] for i in d["integrity"]))]
    prev = None
    if path.exists():
        rows = [ln for ln in path.read_text(encoding="utf-8").splitlines() if ln.startswith("| 20")]
        if rows:
            cells = [c.strip() for c in rows[-1].strip().strip("|").split("|")]
            prev = dict(zip(cols, cells))
    else:
        path.write_text(f"# State log — {review.name}\n\nOne row per `review_db.py state --log` (the definition of done, from the database). "
                        "Append-only; the delta between rows is the review's progress.\n\n"
                        "| " + " | ".join(cols) + " |\n|" + "|".join("---" for _ in cols) + "|\n", encoding="utf-8")
    now = dict(zip(cols, vals))
    # idempotent: an unchanged state is not a new row (only the date would differ)
    if prev and all(prev.get(k) == now[k] for k in cols if k != "date"):
        return prev, None
    with path.open("a", encoding="utf-8") as f:
        f.write("| " + " | ".join(vals) + " |\n")
    return prev, now


def tabulate(cur, rows, limit=200):
    cols = [d[0] for d in cur.description] if cur.description else []
    rows = rows[:limit]
    if not cols:
        print("(no columns)")
        return
    widths = [max(len(str(c)), *(len(str(r[i])[:60]) for r in rows)) if rows else len(str(c)) for i, c in enumerate(cols)]
    print("  ".join(str(c).ljust(w) for c, w in zip(cols, widths)))
    print("  ".join("-" * w for w in widths))
    for r in rows:
        print("  ".join(str(v)[:60].ljust(w) for v, w in zip(r, widths)))
    print(f"({len(rows)} row(s){' — truncated' if len(rows) == limit else ''})")


def main():
    ap = argparse.ArgumentParser(description="SQLite mirror + integrity checks for review data")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("init", help="create a review's database (same as sync)")
    p.add_argument("review")
    p = sub.add_parser("sync", help="rebuild a review's database from its files (or --all)")
    p.add_argument("review", nargs="?")
    p.add_argument("--all", action="store_true")
    p = sub.add_parser("check", help="integrity queries for a review")
    p.add_argument("review")
    p.add_argument("--json", action="store_true")
    p.add_argument("--no-sync", action="store_true", help="check the DB as it is, without re-importing")
    p = sub.add_parser("completion", help="definition of done — the measure of review completion")
    p.add_argument("review")
    p.add_argument("--json", action="store_true")
    p.add_argument("--no-sync", action="store_true")
    p = sub.add_parser("state", help="review state dashboard from the database (repeatable; --log snapshots it)")
    p.add_argument("review")
    p.add_argument("--json", action="store_true")
    p.add_argument("--log", action="store_true", help="append a snapshot row to reviews/<id>/state-log.md and show the delta")
    p.add_argument("--no-sync", action="store_true")
    p = sub.add_parser("query", help="read-only SQL over one review's database (--review) or every review (--all)")
    p.add_argument("sql")
    p.add_argument("--review", help="review directory name or unique substring")
    p.add_argument("--all", action="store_true", help="run against every review database in turn")
    p.add_argument("--json", action="store_true")
    p.add_argument("--limit", type=int, default=200)
    p = sub.add_parser("tables", help="schema overview with row counts")
    p.add_argument("review")
    p = sub.add_parser("criteria", help="list the criteria table")
    p.add_argument("--level")
    p.add_argument("--principle", type=int)
    args = ap.parse_args()

    if args.cmd == "init":
        sync(rv.resolve(args.review))
    elif args.cmd == "sync":
        if not args.all and not args.review:
            sys.exit("give a review or --all")
        sync(None if args.all else rv.resolve(args.review))
    elif args.cmd == "check":
        review = rv.resolve(args.review)
        if not args.no_sync:
            sync(review, quiet=True)
        con = connect(review)
        issues = integrity(con, review.name)
        if args.json:
            print(json.dumps(issues, indent=1, ensure_ascii=False))
        elif not issues:
            print(f"{review.name}: integrity clean — {len(INTEGRITY)} checks, no issues.")
        else:
            print(f"{review.name}: {sum(i['count'] for i in issues)} issue(s) across {len(issues)} check(s)")
            for i in issues:
                print(f"\n  [{i['check']}] — {i['description']}  ({i['count']})")
                for it in i["items"][:25]:
                    print(f"      {it}")
                if i["count"] > 25:
                    print(f"      … {i['count'] - 25} more")
        sys.exit(1 if issues else 0)
    elif args.cmd == "completion":
        review = rv.resolve(args.review)
        if not args.no_sync:
            sync(review, quiet=True)
        con = connect(review)
        rows = completion(con, review.name)
        if args.json:
            print(json.dumps(rows, indent=1, ensure_ascii=False))
        else:
            print_completion(review.name, rows)
        sys.exit(0 if all(r["total"] and r["done"] >= r["total"] for r in rows) else 1)
    elif args.cmd == "state":
        review = rv.resolve(args.review)
        if not args.no_sync:
            sync(review, quiet=True)
        con = connect(review)
        d = state_data(con, review.name)
        if args.json:
            print(json.dumps(d, indent=1, ensure_ascii=False))
        else:
            print(render_state(d))
        if args.log:
            prev, now = log_state(review, d, con)
            print()
            if now is None:
                print(f"state unchanged since {prev['date']} — not logged (state-log.md is append-only, one row per change)")
            elif prev:
                changed = [f"{k} {prev[k]} → {now[k]}" for k in now if k != "date" and prev.get(k) != now[k]]
                print(f"LOGGED to {review.name}/state-log.md — since {prev['date']}: " + ", ".join(changed))
            else:
                print(f"LOGGED first snapshot to {review.name}/state-log.md")
    elif args.cmd == "query":
        if args.all:
            targets = [d for d in sorted(rv.REVIEWS.iterdir()) if d.is_dir() and db_path(d).exists()]
        elif args.review:
            targets = [rv.resolve(args.review)]
        else:
            targets = [d for d in sorted(rv.REVIEWS.iterdir()) if d.is_dir() and db_path(d).exists()]
            if len(targets) != 1:
                sys.exit("give --review <review> or --all")
        all_rows = []
        for t in targets:
            con = sqlite3.connect(f"file:{db_path(t)}?mode=ro", uri=True)
            cur = con.execute(args.sql)
            rows = cur.fetchall()
            if args.json:
                cols = [d[0] for d in cur.description]
                all_rows += [dict(zip(cols, r), _review=t.name) for r in rows[:args.limit]]
            else:
                if len(targets) > 1:
                    print(f"== {t.name}")
                tabulate(cur, rows, args.limit)
            con.close()
        if args.json:
            print(json.dumps(all_rows, indent=1, ensure_ascii=False))
    elif args.cmd == "tables":
        con = connect(rv.resolve(args.review))
        for (name,) in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
            n = con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
            cols = [r[1] for r in con.execute(f"PRAGMA table_info({name})")]
            print(f"{name:<20} {n:>6} rows   {', '.join(cols)}")
    elif args.cmd == "criteria":
        con = connect(":memory:")
        seed(con)
        where, params = ["in_target=1"], []
        if args.level:
            where.append("level=?"); params.append(args.level)
        if args.principle:
            where.append("principle_no=?"); params.append(args.principle)
        cur = con.execute(f"SELECT sc, name, level, version_added, guideline FROM wcag_criteria WHERE {' AND '.join(where)} ORDER BY sort_key", params)
        tabulate(cur, cur.fetchall())


if __name__ == "__main__":
    main()
