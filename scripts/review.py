"""Review process CLI — manage isolated review folders under reviews/.

Each review is a self-contained directory: reviews/<YYYY-MM>-<product-slug>/
holding the six stage files, evidence/, and vendor-acr/. Nothing is shared
between reviews except the templates they were scaffolded from.

Commands:
  new "Product Name" [--enclosure NAME]
                         scaffold a new review from templates/review/,
                         optionally seeding scope exploration from an enclosure
  list                   list all reviews with product, decision, progress
  status <review>        progress detail for one review (stages, tasks, criteria)
  validate <review>      completeness checks; exit code 1 if issues remain
  enclosures             list available enclosure templates (archetypes + products)
  seed <review> --enclosure NAME
                         apply an enclosure to an existing review's scope file
                         (overwrites its Step 2 and process skeletons)
  save-enclosure <review> [--name NAME] [--force]
                         save the review's documented enclosure (Step 2 +
                         processes) to enclosures/products/ for reuse
  log-test <review> --view ID --tool NAME [--modality M] [--url URL]
                    [--baseline ID] [--task ID] [--tester NAME]
                         log a test run (which page, when, which modality,
                         which tool): creates evidence/runs/R###/run.md for
                         notes and evidence, appends to evidence/test-log.md
  runs <review>          list logged test runs
  matrix <review>        views × modalities coverage grid built from the run
                         log. Modalities are the Section 508 Functional
                         Performance Criteria (no-vision, low-vision,
                         no-color, no-hearing, no-speech, motor, cognition);
                         tools are instruments serving them
  next <review>          suggest the highest-value uncovered view×modality
                         cell to test next — vendor-claim discrepancies
                         (Does Not Support > Partially Supports) first, then
                         coverage order; prints the ready log-test command

<review> may be the full directory name or any unique substring of it.
Enclosure names resolve the same way against enclosures/. Add --json to
list/status/validate/enclosures for machine-readable output.
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates" / "review"
REVIEWS = ROOT / "reviews"
ENCLOSURES = ROOT / "enclosures"

STAGES = [
    "01-intake.md",
    "02-vendor.md",
    "03-scope-and-sample.md",
    "04-task-testing.md",
    "05-results.md",
    "06-report.md",
]
OUTCOMES = ["Supports", "Partially Supports", "Does Not Support",
            "Not Applicable", "Not Evaluated"]
# The three procurement outcomes, named for what the office does next rather
# than for a judgement on the product (reviewer, 2026-09-25 -- previously
# "Needs TAAP" and "Denied"). Fixed vocabulary: never a synonym.
DECISIONS = ["Approved", "Approved with TAAP", "Do Not Purchase"]
DECISION_PLACEHOLDER = " / ".join(DECISIONS)
VERDICT_PLACEHOLDER = "Not run / Pass / Pass with barriers / Fail"


def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def read(path):
    return path.read_text(encoding="utf-8") if path.exists() else ""


def resolve(query):
    """Resolve a review by exact directory name or unique substring."""
    if not REVIEWS.exists():
        sys.exit("No reviews/ directory yet. Create one with: review.py new \"Product\"")
    dirs = sorted(d for d in REVIEWS.iterdir() if d.is_dir())
    exact = [d for d in dirs if d.name == query]
    if exact:
        return exact[0]
    matches = [d for d in dirs if query.lower() in d.name.lower()]
    if len(matches) == 1:
        return matches[0]
    if not matches:
        sys.exit(f"No review matches '{query}'. Existing: "
                 + (", ".join(d.name for d in dirs) or "(none)"))
    sys.exit(f"'{query}' is ambiguous: " + ", ".join(d.name for d in matches))


def product_name(review):
    m = re.search(r"^# Review Intake — (.+)$", read(review / STAGES[0]), re.M)
    return m.group(1).strip() if m else review.name


def decision(review):
    m = re.search(r"\|\s*\*\*Decision\*\*\s*\|\s*(.+?)\s*\|",
                  read(review / STAGES[5]))
    if not m:
        return "Pending"
    cell = m.group(1).strip()
    # any cell still offering a choice is the template's, not a decision --
    # this also catches the pre-2026-09-25 placeholder after the rename
    if not cell or " / " in cell or cell.startswith("Pending"):
        return "Pending"
    return cell


def criteria_counts(review):
    text = read(review / STAGES[4])
    counts = {o: 0 for o in OUTCOMES}
    other = 0
    for m in re.finditer(r"- \*\*Outcome:\*\*\s*(.*)", text):
        val = m.group(1).strip()
        # Same rule as review_db.py: the ACR term the cell *starts with*
        # ("Supports (provisional)" → Supports), so the file check and the
        # database never disagree (they did on 2026-09-14).
        term = next((o for o in OUTCOMES if val.startswith(o)), None)
        if term:
            counts[term] += 1
        else:
            other += 1
    counts["(unrecognized)"] = other
    return counts


def tasks(review):
    """Return [(task id, name, verdict)] from 04-task-testing.md."""
    text = read(review / STAGES[3])
    out = []
    blocks = re.split(r"(?=^### Task )", text, flags=re.M)
    for block in blocks:
        head = re.match(r"### Task (\S+) — (.*)", block)
        if not head:
            continue
        v = re.search(r"\|\s*\*\*Verdict\*\*\s*\|\s*(.+?)\s*\|", block)
        verdict = v.group(1) if v else "?"
        if verdict == VERDICT_PLACEHOLDER:
            verdict = "Not run"
        out.append((head.group(1), head.group(2).strip(), verdict))
    return out


def findings(review):
    """Return [(finding id, criteria-cell text)] from 04-task-testing.md."""
    text = read(review / STAGES[3])
    out = []
    blocks = re.split(r"(?=^#### Finding )", text, flags=re.M)
    for block in blocks:
        head = re.match(r"#### Finding (\S+)", block)
        if not head:
            continue
        c = re.search(r"\|\s*\*\*WCAG criteria failed\*\*\s*\|\s*(.*?)\s*\|", block)
        out.append((head.group(1), c.group(1) if c else ""))
    return out


PROCESS_SKELETON_START = "#### Process P1 — (name) — implements F1"

RUN_TEMPLATE = """# Test Run {rid} — {view}

| | |
|---|---|
| **Run ID** | {rid} |
| **Date/time** | {stamp} |
| **View / sample** | {view} |
| **Page URL / location** | {url} |
| **Task / process** | {task} |
| **Modality** | {modality} |
| **Tool** | {tool} |
| **Baseline** | {baseline} |
| **Tester** | {tester} |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks ({modality_label})

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

{checks}

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

(none yet)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named {rid}-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
"""


def run_dirs(review):
    runs = review / "evidence" / "runs"
    return sorted(d for d in runs.iterdir() if d.is_dir()) if runs.exists() else []


def run_meta(run_dir):
    """Parse the metadata table of a run.md into a dict."""
    meta = {"run": run_dir.name}
    for key, field in [("date", "Date/time"), ("view", "View / sample"),
                       ("url", "Page URL / location"), ("task", "Task / process"),
                       ("modality", "Modality"), ("tool", "Tool"),
                       ("baseline", "Baseline"),
                       ("tester", "Tester"), ("result", "Result")]:
        m = re.search(rf"\|\s*\*\*{re.escape(field)}\*\*\s*\|\s*(.*?)\s*\|",
                      read(run_dir / "run.md"))
        meta[key] = m.group(1) if m else ""
    if meta["result"].startswith("Not set"):
        meta["result"] = "Not set"
    else:
        # accept "**Broken** — reasoning…" but normalise to the bare term; the
        # reasoning belongs in the **Result reasoning.** paragraph (RUN_TEMPLATE)
        bare = meta["result"].strip("*` ")
        for term in ("Works with issues", "Works", "Broken", "N/A"):
            if bare.startswith(term):
                meta["result"] = term
                break
    return meta


# Sensory/functional modalities per Section 508 Functional Performance
# Criteria (302.1-302.9, collapsed where testing is identical); see
# ontology/modality-checks.md. Tools (jaws, wave, ...) are instruments, not
# modalities.
REQUIRED_MODALITIES = ["no-vision", "low-vision", "no-color", "no-hearing",
                       "no-speech", "motor", "cognition"]

# Tools that satisfy the per-view automated-sweep requirement (run with no
# --modality). axe = scripts/axe_scan.py (shadow-DOM capable, assistant-
# runnable); wave = WAVE extension (reviewer-run; blind on shadow-DOM apps —
# see ontology/testing-tools.md).
SWEEP_TOOLS = {"axe", "wave"}

# Default instrument + baseline per modality (see ontology/modality-checks.md)
MODALITY_DEFAULTS = {
    "no-vision": ("jaws", "B1"),
    "low-vision": ("zoom", "B3"),
    "no-color": ("grayscale", "—"),
    "no-hearing": ("inspection", "—"),
    "no-speech": ("inspection", "—"),
    "motor": ("keyboard", "B2"),
    "cognition": ("inspection", "—"),
}


def modality_checklist(modality):
    """Return [(check id, check text)] for a modality (or the WAVE sweep when
    modality is empty) from ontology/modality-checks.md."""
    text = read(ROOT / "ontology" / "modality-checks.md")
    if modality in (None, "", "—"):
        sec = re.search(r"(?ms)^## Supporting instrument.*?(?=^## |\Z)", text)
    else:
        sec = re.search(rf"(?ms)^## {re.escape(modality)} — .*?(?=^## |\Z)", text)
    if not sec:
        return []
    return re.findall(r"(?m)^\|\s*([A-Z]+\d+)\s*\|\s*([^|]+?)\s*\|", sec.group(0))


def sc_to_modalities():
    """Map WCAG SC number -> set of modalities whose checks cover it."""
    text = read(ROOT / "ontology" / "modality-checks.md")
    mapping = {}
    for m in REQUIRED_MODALITIES:
        sec = re.search(rf"(?ms)^## {re.escape(m)} — .*?(?=^## |\Z)", text)
        if not sec:
            continue
        for sc in set(re.findall(r"\b\d+\.\d+\.\d+\b", sec.group(0))):
            mapping.setdefault(sc, set()).add(m)
    return mapping


# ---- Criterion / POUR-principle / 508-FPC coverage --------------------------
# The matrix answers "which views × modalities have a run"; these answer
# "which criteria have an answered check, and does 05 agree" — the unit of
# reliability is the check row (ontology/modality-checks.md §Coverage
# tracking).

PRINCIPLES = {"1": "Perceivable", "2": "Operable", "3": "Understandable", "4": "Robust"}

# Section 508 Functional Performance Criteria per matrix modality
# (36 CFR 1194 Chapter 3; collapsed where testing is identical).
FPC = {
    "no-vision": [("302.1", "Without Vision")],
    "low-vision": [("302.2", "With Limited Vision")],
    "no-color": [("302.3", "Without Perception of Color")],
    "no-hearing": [("302.4", "Without Hearing"), ("302.5", "With Limited Hearing")],
    "no-speech": [("302.6", "Without Speech")],
    "motor": [("302.7", "With Limited Manipulation"),
              ("302.8", "With Limited Reach and Strength")],
    "cognition": [("302.9", "With Limited Language, Cognitive, and Learning Abilities")],
}

# A check row is `| ID — text | outcome | observations |`. The dash is written
# by hand often enough that all three are accepted: em, en, plain hyphen.
# ONE pattern, imported by every parser -- six copies of this regex had drifted
# to em-dash-only while the close-run writer accepted a hyphen, so a
# hyphen-dashed row could be answered by the CLI and still be invisible to
# `gaps`, to the mirror and to completion.
# A view code anywhere in a sentence: "Practice Area (S12) - on selection".
# Anchoring this to the start of the cell is what lost 29 of 43 findings.
VIEWCODE_RE = re.compile(r"\b([SR]\d{1,2})\b")

CHECK_DASH = "[\u2014\u2013-]"
CHECK_ROW_RE = re.compile(
    rf"(?m)^\|\s*([A-Z]+\d+)\s*{CHECK_DASH}\s*(.+?)\s*\|(.*?)\|(.*?)\|?\s*$")
CHECK_ROW_SHORT_RE = re.compile(
    rf"(?m)^\|\s*([A-Z]+\d+)\s*{CHECK_DASH}\s*.+?\s*\|(.*?)\|")
CHECK_ROW_HEAD_RE = re.compile(rf"^\|\s*[A-Z]+\d+\s*{CHECK_DASH}")


CHECK_OUTCOMES = {"pass": "pass", "fail": "fail", "partial": "partial",
                  "n/a": "n/a", "na": "n/a"}
# Checks that legitimately map to no WCAG criterion (FPC-only) — anything
# else without a criterion is a map error.
FPC_ONLY_CHECKS = {"NS1"}


def sc_key(sc):
    return [int(x) for x in sc.split(".")]


def sc_targets():
    """[(sc, name, level)] — the conformance target, from the 05 template."""
    return re.findall(r"(?m)^### (\d+\.\d+\.\d+) (.+?) \(Level (A+)\)",
                      read(TEMPLATES / "05-results.md"))


def check_map():
    """check id -> {"modality", "sc": set, "text"} for every check row in
    ontology/modality-checks.md (sweep checks W# map to modality "" and no SC)."""
    text = read(ROOT / "ontology" / "modality-checks.md")
    out = {}
    for m in REQUIRED_MODALITIES + [None]:
        if m is None:
            sec = re.search(r"(?ms)^## Supporting instrument.*?(?=^## |\Z)", text)
        else:
            sec = re.search(rf"(?ms)^## {re.escape(m)} — .*?(?=^## |\Z)", text)
        if not sec:
            continue
        for line in sec.group(0).splitlines():
            mm = re.match(r"^\|\s*([A-Z]+\d+)\s*\|(.*)\|\s*$", line)
            if not mm:
                continue
            cells = [c.strip() for c in mm.group(2).split("|")]
            wcag = cells[1] if len(cells) > 1 else ""
            out[mm.group(1)] = {"modality": m or "",
                                "sc": set(re.findall(r"\b\d+\.\d+\.\d+\b", wcag)),
                                "text": cells[0]}
    return out


def run_checks(run_dir):
    """[(check id, outcome, notes)] from a run's Checks table. Outcome is
    normalised to pass/fail/partial/n/a, "" (unanswered) or "?" (unrecognised)."""
    rows = []
    for cid, _label, outcome, notes in CHECK_ROW_RE.findall(
            read(run_dir / "run.md")):
        raw = outcome.strip().strip("*`_ ").lower()   # runs sometimes bold the outcome
        norm = "" if not raw else CHECK_OUTCOMES.get(raw.split()[0].rstrip(",;:"), "?")
        rows.append((cid, norm, notes.strip()))
    return rows


def criteria_outcomes(review):
    """sc -> ACR outcome (normalised to OUTCOMES vocabulary) from 05-results.md."""
    out = {}
    for block in re.split(r"(?=^### )", read(review / STAGES[4]), flags=re.M):
        h = re.match(r"### (\d+\.\d+\.\d+) ", block)
        o = re.search(r"- \*\*Outcome:\*\* (.+)", block)
        if h and o:
            raw = o.group(1).strip()
            out[h.group(1)] = next((x for x in OUTCOMES if raw.startswith(x)), raw)
    return out


def coverage_data(review):
    targets = sc_targets()
    cmap = check_map()
    outcomes = criteria_outcomes(review)
    runs = [(run_meta(d), run_checks(d)) for d in run_dirs(review)]

    per_sc = {}
    for sc, name, level in targets:
        per_sc[sc] = {"sc": sc, "name": name, "level": level,
                      "checks": sorted(c for c, v in cmap.items() if sc in v["sc"]),
                      "answered": [], "failed": [],
                      "outcome": outcomes.get(sc, "Not Evaluated")}

    stale, unrecognised = [], []
    per_mod = {m: {"runs": 0, "views": set(), "answered": 0, "unanswered": 0,
                   "fails": 0, "na_runs": 0} for m in REQUIRED_MODALITIES}
    for meta, checks in runs:
        mod = meta["modality"].lower()
        if mod in REQUIRED_MODALITIES:
            pm = per_mod[mod]
            pm["runs"] += 1
            pm["views"].add(meta["view"].upper())
            if meta["result"] == "N/A":
                pm["na_runs"] += 1
            expected = [cid for cid, _ in modality_checklist(mod)]
            have = {cid for cid, _, _ in checks}
            missing = [c for c in expected if c not in have]
            if missing:
                stale.append({"run": meta["run"], "missing": missing})
        for cid, outcome, _ in checks:
            if outcome == "?":
                unrecognised.append(f"{meta['run']} {cid}")
                continue
            if mod in REQUIRED_MODALITIES:
                per_mod[mod]["answered" if outcome else "unanswered"] += 1
                if outcome in ("fail", "partial"):
                    per_mod[mod]["fails"] += 1
            if not outcome:
                continue
            for sc in cmap.get(cid, {}).get("sc", ()):
                if sc in per_sc:
                    per_sc[sc]["answered"].append(
                        {"run": meta["run"], "view": meta["view"], "check": cid, "outcome": outcome})
                    if outcome in ("fail", "partial"):
                        per_sc[sc]["failed"].append(
                            {"run": meta["run"], "view": meta["view"], "check": cid})

    principles = []
    for p, pname in PRINCIPLES.items():
        rows = [v for sc, v in per_sc.items() if sc.startswith(p + ".")]
        principles.append({
            "principle": f"{p} {pname}",
            "criteria": len(rows),
            "with_check_row": sum(1 for v in rows if v["checks"]),
            "answered": sum(1 for v in rows if v["answered"]),
            "failed": sum(1 for v in rows if v["failed"]),
            "outcome_set": sum(1 for v in rows if v["outcome"] != "Not Evaluated"),
            "unanswered": sorted((v["sc"] for v in rows if not v["answered"]), key=sc_key),
        })

    n_views = len(sample_views(review))
    fpc_rows = []
    for m in REQUIRED_MODALITIES:
        pm = per_mod[m]
        if pm["runs"] == 0:
            status = "not exercised"
        elif pm["answered"] == 0:
            status = "runs logged, nothing answered"
        elif pm["unanswered"] or pm["views"] and len(pm["views"]) < n_views:
            status = "in progress"
        else:
            status = "complete"
        fpc_rows.append({"modality": m,
                         "fpc": ", ".join(f"{c} {n}" for c, n in FPC[m]),
                         "runs": pm["runs"], "views": sorted(pm["views"]),
                         "sample_views": n_views,
                         "answered": pm["answered"], "unanswered": pm["unanswered"],
                         "fails": pm["fails"], "na_runs": pm["na_runs"],
                         "status": status})

    evidence_gaps = [f"{v['sc']} ({v['outcome']}; checks {', '.join(v['checks']) or 'none'})"
                     for v in per_sc.values()
                     if v["outcome"] != "Not Evaluated" and not v["answered"]]
    rollup_gaps = [f"{v['sc']} (05 still Not Evaluated; failed "
                   + ", ".join(f"{f['check']}@{f['run']}" for f in v["failed"]) + ")"
                   for v in per_sc.values()
                   if v["failed"] and v["outcome"] == "Not Evaluated"]
    no_check_row = [v["sc"] for v in per_sc.values() if not v["checks"]]
    orphan_checks = [c for c, v in cmap.items()
                     if v["modality"] and not v["sc"] and c not in FPC_ONLY_CHECKS]
    fpc_unexercised = [r["fpc"] for r in fpc_rows if r["answered"] == 0]

    return {"review": review.name,
            "criteria": list(per_sc.values()),
            "principles": principles,
            "fpc": fpc_rows,
            "evidence_gaps": evidence_gaps,
            "rollup_gaps": rollup_gaps,
            "stale_runs": stale,
            "unrecognised_outcomes": unrecognised,
            "fpc_unexercised": fpc_unexercised,
            "static": {"no_check_row": no_check_row, "orphan_checks": orphan_checks}}


def db_sync(review):
    """Refresh the SQLite mirror for a review (scripts/review_db.py). Quiet;
    never fatal — the files remain the record if the DB cannot be written."""
    try:
        import review_db
        review_db.sync(review, quiet=True)
        return True
    except Exception as e:  # noqa: BLE001
        print(f"(db sync skipped: {e})", file=sys.stderr)
        return False


def vendor_claims(review):
    """Map SC number -> vendor claim string from 05-results.md."""
    claims = {}
    for block in re.split(r"(?=^### )", read(review / STAGES[4]), flags=re.M):
        h = re.match(r"### (\d+\.\d+\.\d+) ", block)
        v = re.search(r"- \*\*Vendor claim:\*\* (.+)", block)
        if h and v:
            claims[h.group(1)] = v.group(1).strip()
    return claims


REMOVED_RE = re.compile(r"—\s*removed\s+(\d{4}-\d{2}-\d{2})\s*(?::\s*(.*))?$", re.I)


def sample_views(review, include_removed=False):
    """Return [(id, name)] for sampled views (S#/R# rows with a view name)
    from 03-scope-and-sample.md. A row whose name ends in
    " — removed YYYY-MM-DD: <reason>" has been taken out of the sample
    (its ID, runs and findings stay on record) and is skipped unless
    include_removed is set."""
    text = read(review / STAGES[2])
    views = []
    for m in re.finditer(r"(?m)^\|\s*([SR]\d+)\s*\|\s*([^|]*?)\s*\|", text):
        if m.group(2) and (include_removed or not REMOVED_RE.search(m.group(2))):
            views.append((m.group(1), m.group(2)))
    return views


def removed_views(review):
    """[(id, name, date, reason)] for views taken out of the sample."""
    out = []
    for vid, name in sample_views(review, include_removed=True):
        m = REMOVED_RE.search(name)
        if m:
            out.append((vid, name[:m.start()].rstrip(), m.group(1), (m.group(2) or "").strip()))
    return out


def frontmatter(text):
    """Return (meta dict, body) for a file with ----delimited frontmatter."""
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def enclosure_paths():
    if not ENCLOSURES.exists():
        return []
    return sorted(ENCLOSURES.glob("*/*.md"))


def resolve_enclosure(query):
    paths = enclosure_paths()
    exact = [p for p in paths if p.stem == query]
    if exact:
        return exact[0]
    matches = [p for p in paths if query.lower() in p.stem.lower()]
    if len(matches) == 1:
        return matches[0]
    names = ", ".join(p.stem for p in paths) or "(none)"
    if not matches:
        sys.exit(f"No enclosure matches '{query}'. Available: {names}")
    sys.exit(f"'{query}' is ambiguous: " + ", ".join(p.stem for p in matches))


def apply_enclosure(review, enc_path):
    """Splice an enclosure's Step 2 and process skeletons into 03-scope-and-sample.md."""
    scope_path = review / STAGES[2]
    scope = read(scope_path)
    meta, body = frontmatter(read(enc_path))

    step2 = re.search(r"(?ms)^## Step 2 .*?(?=^## |\Z)", body)
    if not step2:
        sys.exit(f"Enclosure {enc_path.name} has no '## Step 2' section.")
    new_step2 = step2.group(0).rstrip()
    # §2.6 (exploration notes / recon) is review-specific, so enclosures do not
    # carry it. Preserve the template's block when the enclosure lacks one —
    # otherwise the review loses the only sanctioned home for recon.
    if not re.search(r"(?m)^### 2\.6 ", new_step2):
        recon = re.search(r"(?ms)^### 2\.6 .*?(?=^## Step 3 )", scope)
        if recon:
            new_step2 += "\n\n" + recon.group(0).rstrip()
    new_scope, n = re.subn(r"(?ms)^## Step 2 .*?(?=^## Step 3 )",
                           new_step2 + "\n\n", scope)
    if not n:
        sys.exit(f"{scope_path} has no Step 2 section to replace (already customized?).")

    processes = re.search(r"(?ms)^## Process skeletons\s*\n(.*)\Z", body)
    if processes:
        new_scope, n = re.subn(
            r"(?ms)^" + re.escape(PROCESS_SKELETON_START) + r".*\Z",
            processes.group(1).strip() + "\n", new_scope)
        if not n:
            print(f"note: default process skeleton not found in {scope_path.name}; "
                  "process skeletons from the enclosure were not applied.")

    note = (f"> Seeded from enclosure `{enc_path.stem}` "
            f"({meta.get('description', 'no description')}). Rows in Step 2 and the\n"
            f"> process skeletons are hypotheses — confirm, correct, or delete them\n"
            f"> during exploration.\n\n")
    new_scope = re.sub(r"(?m)^## Step 1 ", note + "## Step 1 ", new_scope, count=1)

    scope_path.write_text(new_scope, encoding="utf-8")
    print(f"Seeded {scope_path.relative_to(ROOT)} from enclosure '{enc_path.stem}'.")


def emit(data, as_json, text_fn):
    if as_json:
        print(json.dumps(data, indent=2))
    else:
        text_fn(data)


def cmd_new(args):
    today = datetime.date.today()
    review_id = f"{today.year}-{today.month:02d}-{slugify(args.product)}"
    dest = REVIEWS / review_id
    if dest.exists():
        sys.exit(f"Review already exists: {dest}")
    dest.mkdir(parents=True)
    (dest / "evidence").mkdir()
    (dest / "vendor-acr").mkdir()
    for tpl in sorted(TEMPLATES.glob("*.md")):
        text = (tpl.read_text(encoding="utf-8")
                .replace("{{PRODUCT_NAME}}", args.product)
                .replace("{{REVIEW_ID}}", review_id)
                .replace("{{DATE}}", today.isoformat()))
        (dest / tpl.name).write_text(text, encoding="utf-8")
    db_sync(dest)
    print(f"Review scaffolded: {dest}")
    if args.enclosure:
        apply_enclosure(dest, resolve_enclosure(args.enclosure))
    print("Start with 01-intake.md.")


def cmd_log_test(args):
    review = resolve(args.review)
    runs_root = review / "evidence" / "runs"
    runs_root.mkdir(parents=True, exist_ok=True)
    rid = f"R{len(run_dirs(review)) + 1:03d}"
    run_dir = runs_root / rid
    run_dir.mkdir()

    stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    checklist = modality_checklist(args.modality)
    if checklist:
        checks = ("| Check | Outcome | Observations |\n"
                  "|-------|---------|--------------|\n"
                  + "\n".join(f"| {cid} — {ctext} | | |" for cid, ctext in checklist))
    else:
        checks = "(no checklist found for this modality — see ontology/modality-checks.md)"
    fields = dict(rid=rid, stamp=stamp, view=args.view, url=args.url or "—",
                  task=args.task or "—", modality=args.modality or "—",
                  tool=args.tool, baseline=args.baseline or "—",
                  tester=args.tester or "—",
                  modality_label=args.modality or f"{args.tool} sweep",
                  checks=checks)
    (run_dir / "run.md").write_text(RUN_TEMPLATE.format(**fields), encoding="utf-8")

    log_path = review / "evidence" / "test-log.md"
    if not log_path.exists():
        log_path.write_text(
            f"# Test Log — {review.name}\n\n"
            "One row per test run; details and evidence in `runs/<Run>/`.\n\n"
            "| Run | Date | View | URL / location | Modality | Tool | Baseline | Task | Tester |\n"
            "|-----|------|------|----------------|----------|------|----------|------|--------|\n",
            encoding="utf-8")
    with log_path.open("a", encoding="utf-8") as f:
        f.write(f"| {rid} | {stamp} | {args.view} | {fields['url']} "
                f"| {fields['modality']} | {args.tool} "
                f"| {fields['baseline']} | {fields['task']} | {fields['tester']} |\n")

    db_sync(review)
    print(f"Run {rid} logged: {run_dir.relative_to(ROOT)}")
    print(f"  view={args.view}  modality={fields['modality']}  tool={args.tool}  "
          f"baseline={fields['baseline']}")
    print(f"  Notes and evidence go in {run_dir.relative_to(ROOT)}\\run.md "
          f"and {rid}-*.png files alongside it.")


RESULTS = ["Works", "Works with issues", "Broken", "N/A"]
CHECK_ID_RE = re.compile(rf"^\\s*((?:NV|LV|NC|NH|NS|MO|CO|W)\\d+)\\s*{CHECK_DASH}")


def answer_check_rows(text, answers):
    """Fill named check rows: {check_id: (outcome, note)}. Returns (text, n)."""
    n = 0
    out = []
    for line in text.split("\n"):
        parts = line.split("|")
        if len(parts) == 5 and line.lstrip().startswith("|"):
            m = CHECK_ID_RE.match(parts[1])
            if m and m.group(1) in answers:
                outcome, note = answers[m.group(1)]
                parts[2] = f" {outcome} "
                parts[3] = f" {note} "
                line = "|".join(parts)
                n += 1
        out.append(line)
    return "\n".join(out), n


def set_run_result(run_dir, result, reason, answer_open=None, note=None, answers=None):
    """Write a run's Result, its reasoning, and optionally its open check rows.

    The Result cell must hold the bare term and nothing else -- `matrix`
    matches it against those exact strings and prints anything else verbatim,
    which blew the grid apart on 2026-08-14. The reasoning goes in the
    `**Result reasoning.**` paragraph under the table, where there is no
    length limit.

    Returns (changed_result, rows_answered)."""
    f = run_dir / "run.md"
    text = read(f)
    if not text:
        raise SystemExit(f"{run_dir.name}: no run.md")

    m = re.search(r"(\|\s*\*\*Result\*\*\s*\|)(\s*.*?\s*)(\|)", text)
    if not m:
        raise SystemExit(f"{run_dir.name}: no Result row in the metadata table")
    text = text[:m.start()] + f"| **Result** | {result} |" + text[m.end():]

    # the reasoning paragraph: replace the template's guidance if it is still
    # there, otherwise insert directly after the metadata table
    guidance = re.search(r"\n\*\*When you set the Result.*?\n\n", text, re.S)
    para = f"\n**Result reasoning.** {reason}\n\n"
    if re.search(r"\n\*\*Result reasoning\.\*\*.*?\n\n", text, re.S):
        text = re.sub(r"\n\*\*Result reasoning\.\*\*.*?\n\n", para, text, count=1, flags=re.S)
    elif guidance:
        text = text[:guidance.start()] + para + text[guidance.end():]
    else:
        end = text.index("\n## ")
        text = text[:end] + "\n" + para.rstrip("\n") + "\n" + text[end:]

    answered = 0
    if answers:
        text, answered = answer_check_rows(text, answers)
    if answer_open:
        out = []
        for line in text.split("\n"):
            parts = line.split("|")
            if (len(parts) == 5 and line.lstrip().startswith("|")
                    and CHECK_ID_RE.match(parts[1]) and not parts[2].strip()):
                parts[2] = f" {answer_open} "
                obs = parts[3].strip()
                parts[3] = f" {obs + ' — ' if obs else ''}{note or reason} "
                line = "|".join(parts)
                answered += 1
            out.append(line)
        text = "\n".join(out)

    f.write_text(text, encoding="utf-8")
    return True, answered


def parse_answers(specs):
    """`--answer W1=pass=note text` → {"W1": ("pass", "note text")}."""
    out = {}
    for spec in specs or []:
        cid, _, rest = spec.partition("=")
        outcome, _, note = rest.partition("=")
        if not cid or outcome not in set(CHECK_OUTCOMES.values()):
            raise SystemExit(f"--answer must read CHECK=outcome=note, got: {spec}")
        out[cid.strip()] = (outcome.strip(), note.strip())
    return out


def cmd_close_run(args):
    """Set the Result on one or more runs, with the reason, in one pass."""
    review = resolve(args.review)
    if args.result not in RESULTS:
        raise SystemExit(f"--result must be one of: {', '.join(RESULTS)}")
    if args.answer_open and args.answer_open not in set(CHECK_OUTCOMES.values()):
        raise SystemExit("--answer-open must be one of: "
                         + ", ".join(sorted(set(CHECK_OUTCOMES.values()))))

    dirs = {d.name: d for d in run_dirs(review)}
    if args.runs:
        missing = [r for r in args.runs if r not in dirs]
        if missing:
            raise SystemExit(f"no such run(s): {', '.join(missing)}")
        targets = [dirs[r] for r in args.runs]
    elif args.removed_views:
        # Runs against a view that has since left the sample. They can never
        # be finished -- the page is out of scope -- but leaving them at
        # "Not set" makes the review look permanently unfinished, and the
        # definition of done counts them.
        gone = {v.lower() for v, _, _, _ in removed_views(review)}
        targets = [d for d in run_dirs(review)
                   if run_meta(d)["view"].lower() in gone]
    else:
        raise SystemExit("name the runs, or pass --removed-views")

    targets = [d for d in targets if args.force or run_meta(d)["result"] == "Not set"]
    if not targets:
        print("Nothing to close — every named run already has a Result "
              "(use --force to overwrite).")
        return

    for d in targets:
        meta = run_meta(d)
        if args.dry_run:
            print(f"{d.name}  view={meta['view']:<4} modality={meta['modality']:<11} "
                  f"→ {args.result}")
            continue
        _, n = set_run_result(d, args.result, args.reason, args.answer_open, args.note,
                              parse_answers(args.answer))
        print(f"{d.name}  view={meta['view']:<4} → {args.result}"
              + (f"  ({n} check row{'s' if n != 1 else ''} answered)" if n else ""))

    if args.dry_run:
        print(f"\n{len(targets)} run(s) would be closed. Drop --dry-run to write.")
        return
    print(f"\n{len(targets)} run(s) closed as {args.result}.")
    db_sync(review)
    print("Database resynced. Run `review.py validate` to see the new completion.")


def cmd_runs(args):
    review = resolve(args.review)
    rows = [run_meta(d) for d in run_dirs(review)]

    def text(rows):
        if not rows:
            print("No test runs logged yet. Start one with: "
                  "review.py log-test <review> --view S1 --tool jaws|wave")
            return
        for r in rows:
            print(f"{r['run']}  {r['date']}  view={r['view']:<6} "
                  f"modality={r['modality']:<11} tool={r['tool']:<6} "
                  f"baseline={r['baseline']:<4} task={r['task']:<4} "
                  f"result={r['result']:<18} {r['url']}")

    emit(rows, args.json, text)


def page_state(review, vid):
    """Everything known about one page: per modality, the run and its open checks.

    The unit of work is a page, not a view x modality cell. A page is finished
    when every modality has a resulted run, every check row in those runs is
    answered, and the automated sweep has been triaged -- and until it is, the
    open rows here ARE the session's question list for it."""
    runs = [run_meta(d) | {"dir": d} for d in run_dirs(review)]
    mine = [r for r in runs if r["view"].upper() == vid.upper()]
    out = {"view": vid, "modalities": {}, "sweep": None, "open": 0, "unresulted": 0}
    for m in REQUIRED_MODALITIES:
        r = next((x for x in mine if x["modality"] == m), None)
        checks = modality_checklist(m)
        if r is None:
            cell = {"run": None, "result": None,
                    "open": [(cid, txt) for cid, txt in checks]}
        else:
            answered = {cid: o for cid, o, _n in run_checks(r["dir"])}
            cell = {"run": r["run"], "result": r["result"],
                    "open": [(cid, txt) for cid, txt in checks if not answered.get(cid)]}
            if r["result"] == "Not set":
                out["unresulted"] += 1
        out["open"] += len(cell["open"])
        out["modalities"][m] = cell
    sweep = next((x for x in mine if x["tool"].lower() in ("axe", "wave")), None)
    if sweep:
        answered = {cid: o for cid, o, _n in run_checks(sweep["dir"])}
        open_w = [(cid, txt) for cid, txt in modality_checklist(None) if not answered.get(cid)]
        raw = sorted(f.name for f in sweep["dir"].glob("*-axe.json"))
        out["sweep"] = {"run": sweep["run"], "result": sweep["result"], "open": open_w, "raw": raw}
        out["open"] += len(open_w)
        if sweep["result"] == "Not set":
            out["unresulted"] += 1
    return out


def page_blockers(st):
    """Why a page is not finished, in the order a session should fix them."""
    bad = []
    if st["sweep"] is None:
        bad.append("no automated sweep run (axe_scan.py --view %s --url ...)" % st["view"])
    elif not st["sweep"]["raw"]:
        bad.append(f"{st['sweep']['run']}: sweep has no saved R###-axe.json")
    for m, cell in st["modalities"].items():
        if cell["run"] is None:
            bad.append(f"{m}: no run logged ({len(cell['open'])} checks unanswered)")
        elif cell["result"] in (None, "Not set"):
            bad.append(f"{m}: {cell['run']} has no Result")
    if st["open"]:
        bad.append(f"{st['open']} check row(s) unanswered")
    return bad


def cmd_page(args):
    """One page's full state — the per-page checklist, and what is left on it."""
    review = resolve(args.review)
    names = dict(sample_views(review, include_removed=True))
    vids = [args.view] if args.view else [v for v, _ in sample_views(review)]
    data = []
    for vid in vids:
        st = page_state(review, vid)
        st["name"] = names.get(vid, "")
        st["blockers"] = page_blockers(st)
        data.append(st)

    def text(rows):
        for st in rows:
            done = "DONE" if not st["blockers"] else f"{len(st['blockers'])} blocker(s)"
            print(f"\n{st['view']} {st['name'][:56]}  [{done}]")
            if st["sweep"]:
                raw = ", ".join(st["sweep"]["raw"]) or "NO RAW JSON"
                print(f"   sweep   {st['sweep']['run']:<6} {st['sweep']['result'] or '—':<18} {raw}")
            else:
                print("   sweep   —      not run")
            for m, cell in st["modalities"].items():
                mark = "ok" if cell["run"] and not cell["open"] and cell["result"] not in (None, "Not set") else "  "
                print(f"   {mark} {m:<11} {cell['run'] or '—':<6} {cell['result'] or '—':<18}"
                      + (f"{len(cell['open'])} open" if cell["open"] else ""))
            for b in st["blockers"]:
                print(f"      - {b}")
        if len(rows) > 1:
            shut = sum(1 for r in rows if not r["blockers"])
            print(f"\n{shut}/{len(rows)} page(s) closed.")

    emit(data, args.json, text)


def cmd_close_page(args):
    """Refuse, with reasons, unless the page is genuinely finished."""
    review = resolve(args.review)
    st = page_state(review, args.view)
    bad = page_blockers(st)
    if bad:
        print(f"{args.view} is NOT closed — {len(bad)} thing(s) outstanding:")
        for b in bad:
            print(f"  - {b}")
        for m, cell in st["modalities"].items():
            for cid, txt in cell["open"][:40]:
                print(f"      [ ] {m:<11} {cid} — {txt[:80]}")
        if st["sweep"]:
            for cid, txt in st["sweep"]["open"]:
                print(f"      [ ] sweep       {cid} — {txt[:80]}")
        raise SystemExit(1)
    print(f"{args.view} closed: every modality resulted, every check answered, sweep triaged"
          + (f" ({', '.join(st['sweep']['raw'])})" if st["sweep"] else ""))
    return 0


def cmd_gaps(args):
    """The session's question list: every check row still without an outcome.

    Taken from the SAMPLE, not from the run folders. Reading the folders meant
    a sampled view with no runs reported "no unanswered check rows" -- so a
    fresh review, and every untested page in it, was told its question list
    was empty while CLAUDE.md said never to improvise one."""
    review = resolve(args.review)
    if args.view:
        vids = [args.view]
    else:
        vids = [v for v, _ in sample_views(review)]
    if not vids:
        print("No sampled views yet. Define the sample in 03 §3.1 before testing "
              "(see the review phases in CLAUDE.md).")
        return
    rows = []
    for vid in vids:
        st = page_state(review, vid)
        for m, cell in st["modalities"].items():
            for cid, txt in cell["open"]:
                rows.append({"view": vid, "modality": m, "run": cell["run"],
                             "result": cell["result"], "check": cid, "label": txt.strip()})
        if st["sweep"]:
            for cid, txt in st["sweep"]["open"]:
                rows.append({"view": vid, "modality": "sweep", "run": st["sweep"]["run"],
                             "result": st["sweep"]["result"], "check": cid, "label": txt.strip()})
        elif not args.view:
            rows.append({"view": vid, "modality": "sweep", "run": None, "result": None,
                         "check": "—", "label": "no automated sweep run on this page yet"})

    def text(rows):
        if not rows:
            print("No unanswered check rows"
                  + (f" on {args.view}" if args.view else "")
                  + " — every sampled page is answered end to end.")
            return
        by = {}
        for r in rows:
            by.setdefault((r["view"], r["modality"]), []).append(r)
        for (vid, m), items in by.items():
            run = items[0]["run"] or "no run"
            print(f"{vid}  {m:<11} {run:<8} ({len(items)} unanswered)")
            for r in items:
                print(f"    [ ] {r['check']} — {r['label'][:86]}")
        print(f"\nTOTAL unanswered check rows"
              + (f" on {args.view}" if args.view else "") + f": {len(rows)}")

    emit(rows, args.json, text)


def cmd_next(args):
    """Name the next page to work, and what is open on it.

    Page-shaped on purpose. Ranking view x modality cells sent sessions
    hopping between pages and left every page half-done; the reviewer pays
    for that twice, once in context-switching and once in re-reading a page
    they have already walked."""
    review = resolve(args.review)
    views = sample_views(review)
    if not views:
        print("No sampled views yet.\n"
              "  The sample comes third. Map the product into 03 §2.1, choose the sample in\n"
              "  03 §3.1, define the cross-page processes in 03 §3.3 — then test.\n"
              "  See 'A review, start to finish' in CLAUDE.md.")
        return

    # score modalities by vendor-claim discrepancy: verifying claimed failures
    # (and shaky Partially Supports) first produces decision-relevant evidence
    # fastest -- used to order pages, not to fragment them
    sc2mod = sc_to_modalities()
    weights, reasons = {}, {}
    for sc, claim in vendor_claims(review).items():
        w = 3 if "Does Not Support" in claim else 1 if "Partially Supports" in claim else 0
        if not w:
            continue
        for m in sc2mod.get(sc, ()):
            weights[m] = weights.get(m, 0) + w
            reasons.setdefault(m, []).append(f"{sc} ({'DNS' if w == 3 else 'PS'})")

    pages = []
    for order, (vid, name) in enumerate(views):
        st = page_state(review, vid)
        st["name"], st["order"] = name, order
        st["blockers"] = page_blockers(st)
        st["started"] = any(c["run"] for c in st["modalities"].values()) or bool(st["sweep"])
        st["score"] = sum(weights.get(m, 0) for m, c in st["modalities"].items() if c["open"])
        pages.append(st)

    open_pages = [x for x in pages if x["blockers"]]
    # an already-started page outranks a fresh one: closing it out is what
    # stops the review accumulating half-walked pages
    open_pages.sort(key=lambda x: (not x["started"], -x["score"], x["order"]))
    # a cell still offering the template's choice is not a verdict
    tasks = [t for t in parse_tasks_light(review)
             if not t[1] or t[1].startswith("Not run") or " / " in t[1]]

    data = {"review": review.name, "pages_open": len(open_pages), "pages": len(pages),
            "next": open_pages[0]["view"] if open_pages else None,
            "tasks_unrun": [t[0] for t in tasks]}

    def text(_d):
        if open_pages:
            top = open_pages[0]
            print(f"Next page: {top['view']} — {top['name'][:60]}"
                  f"   ({len(pages) - len(open_pages)}/{len(pages)} pages closed)")
            if top["started"]:
                print("  (already started — finish it before opening another page)")
            for b in top["blockers"]:
                print(f"  - {b}")
            for m, cell in top["modalities"].items():
                if cell["run"] is None:
                    tool, baseline = MODALITY_DEFAULTS.get(m, ("inspection", "—"))
                    print(f"  python scripts/review.py log-test {review.name} "
                          f"--view {top['view']} --modality {m} --tool {tool} --baseline {baseline}")
                    break
            print(f"  python scripts/review.py gaps {review.name} --view {top['view']}"
                  "      # the page's question list")
            print(f"  python scripts/review.py close-page {review.name} {top['view']}"
                  "   # when it is finished")
            if len(open_pages) > 1:
                print("then: " + ", ".join(x["view"] for x in open_pages[1:6]))
        elif tasks:
            print(f"Every page is closed ({len(pages)}/{len(pages)}). "
                  f"{len(tasks)} task cluster(s) still to walk — §A of 04 is where the "
                  f"report's task verdicts come from:")
            for tid, _v, nm in tasks:
                print(f"  - {tid}: {nm[:70]}")
        else:
            print("Every page is closed and every task cluster has a verdict.\n"
                  "  Remaining: `review_db.py completion` for anything still open, then\n"
                  "  regenerate both reports (C13).")

    emit(data, args.json, text)


def parse_tasks_light(review):
    """[(task id, verdict, name)] from 04 §A — enough for `next` to see them."""
    out = []
    for tid, name, verdict in re.findall(
            r"(?m)^### Task (T\d+)\s*—\s*(.+?)\s*$[\s\S]*?^\|\s*\*\*Verdict\*\*\s*\|\s*(.*?)\s*\|",
            read(review / STAGES[3])):
        out.append((tid, verdict, name))
    return out


def cmd_matrix(args):
    review = resolve(args.review)
    views = sample_views(review)
    runs = [run_meta(d) for d in run_dirs(review)]

    def cell(view_id, modality):
        hits = [r for r in runs
                if r["view"].lower() == view_id.lower()
                and r["modality"].lower() == modality]
        if not hits:
            return {"result": "Not run", "runs": []}
        latest = hits[-1]
        return {"result": latest["result"] if latest["result"] != "Not set"
                else "Run logged, result not set",
                "runs": [h["run"] for h in hits]}

    grid = [{"view": vid, "name": name,
             "cells": {m: cell(vid, m) for m in REQUIRED_MODALITIES}}
            for vid, name in views]
    gaps = sum(1 for row in grid for c in row["cells"].values()
               if c["result"] == "Not run")
    data = {"review": review.name, "modalities": REQUIRED_MODALITIES,
            "views": grid, "gaps": gaps, "removed": removed_views(review),
            "note": None if views else
            "No sampled views (S#/R# rows with names) defined in 03 §3.1/§3.2 yet."}

    def text(d):
        if not d["views"]:
            print(d["note"])
            return
        abbrev = {"Not run": "—", "Works": "OK",
                  "Works with issues": "ISSUES", "Broken": "BROKEN",
                  "N/A": "n/a", "Run logged, result not set": "run?"}
        wv = max(len(f"{r['view']} {r['name']}") for r in d["views"])
        widths = {m: max(len(m), 6) for m in d["modalities"]}
        print(f"{'view':<{wv}}  "
              + "  ".join(f"{m:<{widths[m]}}" for m in d["modalities"]))
        for r in d["views"]:
            label = f"{r['view']} {r['name']}"
            cells = "  ".join(
                f"{abbrev.get(r['cells'][m]['result'], r['cells'][m]['result']):<{widths[m]}}"
                for m in d["modalities"])
            print(f"{label:<{wv}}  {cells}")
        print(f"\n{d['gaps']} view×modality cell(s) not yet run "
              f"({len(d['views'])} views × {len(d['modalities'])} modalities).")
        if d["removed"]:
            print("Removed from the sample (kept on record): "
                  + "; ".join(f"{v} {n} ({dt}: {r})" if r else f"{v} {n} ({dt})" for v, n, dt, r in d["removed"]))

    emit(data, args.json, text)


def cmd_coverage(args):
    """Criterion / POUR-principle / 508-FPC coverage from answered checks."""
    review = resolve(args.review)
    db_sync(review)
    d = coverage_data(review)

    def text(d):
        print(f"Coverage — {d['review']}  (criteria → POUR principles → 508 FPC; "
              "from answered check rows in logged runs, cross-checked with 05)\n")
        print(f"{'Principle':<18}{'criteria':>9}{'check row':>11}{'answered':>10}"
              f"{'failed':>8}{'05 set':>8}")
        for p in d["principles"]:
            print(f"{p['principle']:<18}{p['criteria']:>9}{p['with_check_row']:>11}"
                  f"{p['answered']:>10}{p['failed']:>8}{p['outcome_set']:>8}")
        tot = {k: sum(p[k] for p in d["principles"])
               for k in ("criteria", "with_check_row", "answered", "failed", "outcome_set")}
        print(f"{'Total':<18}{tot['criteria']:>9}{tot['with_check_row']:>11}"
              f"{tot['answered']:>10}{tot['failed']:>8}{tot['outcome_set']:>8}\n")

        wf = max(len(r["fpc"]) for r in d["fpc"])
        print(f"{'508 FPC':<{wf}}  {'modality':<11}{'runs':>5}{'views':>8}"
              f"{'answered':>10}{'blank':>7}{'fails':>7}  status")
        for r in d["fpc"]:
            print(f"{r['fpc']:<{wf}}  {r['modality']:<11}{r['runs']:>5}"
                  f"{len(r['views']):>4}/{r['sample_views']:<3}"
                  f"{r['answered']:>10}{r['unanswered']:>7}{r['fails']:>7}  {r['status']}")

        print("\nCriteria with no answered check yet:")
        for p in d["principles"]:
            if p["unanswered"]:
                print(f"  {p['principle']}: {', '.join(p['unanswered'])}")
        if not any(p["unanswered"] for p in d["principles"]):
            print("  none — every target criterion has at least one answered check")

        flags = []
        for g in d["evidence_gaps"]:
            flags.append(f"05 Outcome set without an answered check: {g}")
        for g in d["rollup_gaps"]:
            flags.append(f"check failed, 05 needs a decision: {g}")
        for r in d["stale_runs"]:
            flags.append(f"{r['run']} is behind the checklist — missing "
                         f"{', '.join(r['missing'])} (run: review.py sync-checks)")
        for u in d["unrecognised_outcomes"]:
            flags.append(f"unrecognised check outcome (use pass/fail/partial/n/a): {u}")
        for f in d["fpc_unexercised"]:
            flags.append(f"508 FPC not exercised on any view: {f}")
        for sc in d["static"]["no_check_row"]:
            flags.append(f"target criterion has no check row in modality-checks.md: {sc}")
        for c in d["static"]["orphan_checks"]:
            flags.append(f"check maps to no criterion and is not FPC-only: {c}")
        print("\nRELIABILITY FLAGS" + ("" if flags else ": none"))
        for f in flags:
            print(f"  - {f}")

    emit(d, args.json, text)


def cmd_sync_checks(args):
    """Append check rows added to ontology/modality-checks.md after a run was
    logged, so gaps/coverage see them as unanswered instead of absent."""
    review = resolve(args.review)
    today = datetime.date.today().isoformat()
    changed = 0
    for d in run_dirs(review):
        meta = run_meta(d)
        mod = meta["modality"].lower()
        if mod not in REQUIRED_MODALITIES:
            continue
        expected = modality_checklist(mod)
        have = {cid for cid, _, _ in run_checks(d)}
        missing = [(cid, text) for cid, text in expected if cid not in have]
        if not missing:
            continue
        path = d / "run.md"
        lines = read(path).splitlines(keepends=True)
        last = max(i for i, ln in enumerate(lines)
                   if CHECK_ROW_HEAD_RE.match(ln))
        eol = "\r\n" if lines[last].endswith("\r\n") else "\n"
        new = [f"| {cid} — {text} | | (row added {today} by sync-checks — "
               f"not part of the original session; answer or mark n/a) |{eol}"
               for cid, text in missing]
        lines[last + 1:last + 1] = new
        path.write_text("".join(lines), encoding="utf-8")
        changed += 1
        print(f"{meta['run']} ({meta['view']} × {mod}): added "
              + ", ".join(cid for cid, _ in missing))
    if changed:
        db_sync(review)
    print(f"{changed} run(s) updated." if changed else "All runs match the current checklist.")


def cmd_enclosures(args):
    rows = []
    for p in enclosure_paths():
        meta, _ = frontmatter(read(p))
        rows.append({
            "name": p.stem,
            "kind": p.parent.name.rstrip("s"),  # archetypes -> archetype
            "description": meta.get("description", ""),
        })

    def text(rows):
        if not rows:
            print("No enclosures found under enclosures/.")
            return
        w = max(len(r["name"]) for r in rows)
        for r in rows:
            print(f"{r['name']:<{w}}  [{r['kind']}]  {r['description']}")

    emit(rows, args.json, text)


def cmd_seed(args):
    review = resolve(args.review)
    apply_enclosure(review, resolve_enclosure(args.enclosure))


def cmd_save_enclosure(args):
    review = resolve(args.review)
    scope = read(review / STAGES[2])
    step2 = re.search(r"(?ms)^## Step 2 .*?(?=^## Step 3 )", scope)
    if not step2:
        sys.exit(f"No Step 2 section found in {review.name}/{STAGES[2]}.")
    # Drop §2.6 — dated recon belongs to the review, not to the reusable map.
    step2_text = re.sub(r"(?ms)^### 2\.6 .*\Z", "", step2.group(0)).rstrip()
    processes = re.search(r"(?ms)^#### Process .*\Z", scope)

    product = product_name(review)
    name = args.name or slugify(product)
    dest = ENCLOSURES / "products" / f"{name}.md"
    if dest.exists() and not args.force:
        sys.exit(f"{dest} exists. Use --force to overwrite.")
    dest.parent.mkdir(parents=True, exist_ok=True)

    parts = [
        "---",
        f"name: {name}",
        f"description: Enclosure for {product}, documented during review {review.name}",
        "---",
        "",
        step2_text,
        "",
    ]
    if processes:
        parts += ["## Process skeletons", "", processes.group(0).rstrip(), ""]
    dest.write_text("\n".join(parts), encoding="utf-8")
    print(f"Enclosure saved: {dest.relative_to(ROOT)}")


def cmd_list(args):
    dirs = sorted(d for d in REVIEWS.iterdir() if d.is_dir()) if REVIEWS.exists() else []
    rows = []
    for d in dirs:
        counts = criteria_counts(d)
        evaluated = sum(v for k, v in counts.items() if k not in ("Not Evaluated", "(unrecognized)"))
        total = evaluated + counts["Not Evaluated"]
        t = tasks(d)
        rows.append({
            "review": d.name,
            "product": product_name(d),
            "decision": decision(d),
            "criteria_evaluated": f"{evaluated}/{total}",
            "tasks": len(t),
            "tasks_run": sum(1 for _, _, v in t if v not in ("Not run", "?")),
        })

    def text(rows):
        if not rows:
            print("No reviews yet. Create one with: review.py new \"Product\"")
            return
        w = max(len(r["review"]) for r in rows)
        for r in rows:
            print(f"{r['review']:<{w}}  decision={r['decision']:<10}  "
                  f"criteria={r['criteria_evaluated']:<6} "
                  f"tasks run={r['tasks_run']}/{r['tasks']}")

    emit(rows, args.json, text)


def _completion_summary(review):
    """Compact definition-of-done summary from the mirror, for status."""
    if not db_sync(review):
        return None
    import review_db
    con = review_db.connect(review)
    rows = review_db.completion(con, review.name, review)
    con.close()
    short = [f"{r['name'].split(' ')[0]} {r['done']}/{r['total']}" for r in rows if not (r['total'] and r['done'] >= r['total'])]
    return {"satisfied": sum(1 for r in rows if r['total'] and r['done'] >= r['total']),
            "predicates": len(rows), "short": short}


def cmd_status(args):
    review = resolve(args.review)
    counts = criteria_counts(review)
    t = tasks(review)
    f = findings(review)
    data = {
        "review": review.name,
        "product": product_name(review),
        "decision": decision(review),
        "stages_present": {s: (review / s).exists() for s in STAGES},
        "criteria": counts,
        "tasks": [{"id": i, "name": n, "verdict": v} for i, n, v in t],
        "findings": len(f),
        "test_runs": len(run_dirs(review)),
        "completion": _completion_summary(review),
        "evidence_files": len([p for p in (review / "evidence").rglob("*")
                               if p.is_file() and p.name not in ("run.md", "test-log.md")])
        if (review / "evidence").exists() else 0,
    }

    def text(d):
        print(f"{d['review']} — {d['product']}")
        print(f"  decision: {d['decision']}")
        missing = [s for s, ok in d["stages_present"].items() if not ok]
        print(f"  stages: {'all present' if not missing else 'MISSING ' + ', '.join(missing)}")
        print("  criteria: " + ", ".join(f"{k}={v}" for k, v in d["criteria"].items() if v))
        print(f"  findings recorded: {d['findings']}   test runs: {d['test_runs']}   "
              f"evidence files: {d['evidence_files']}")
        for task in d["tasks"]:
            print(f"  task {task['id']}: {task['verdict']}  ({task['name']})")
        if d["completion"]:
            c = d["completion"]
            print(f"  completion (db): {c['satisfied']}/{c['predicates']} predicates — "
                  + ", ".join(c["short"]))

    emit(data, args.json, text)


def cmd_validate(args):
    """The finish line, measured in the database (ontology/data-store.md).

    Three layers, all from one command:
      [md]  extraction health — the files still have the shapes the templates
            define (a parse regression is a broken edit, CLAUDE.md);
      [done] the definition of done — review_db.COMPLETION, every predicate
            a query over the mirror;
      [db]  integrity — cross-file consistency the markdown cannot express.
    """
    review = resolve(args.review)
    issues = []

    # ---- [md] extraction health
    for st in STAGES:
        if not (review / st).exists():
            issues.append(f"[md] missing stage file: {st}")
    counts = criteria_counts(review)
    if counts["(unrecognized)"]:
        issues.append(f"[md] {counts['(unrecognized)']} Outcome lines in 05-results.md not using ACR vocabulary")
    if not tasks(review):
        issues.append("[md] no task clusters defined in 04-task-testing.md")
    runs = [run_meta(d) for d in run_dirs(review)]
    no_locator = [r["run"] for r in runs
                  if not (("http" in r["url"]) or r["url"].startswith("UI:"))
                  or any(ph in r["url"] for ph in ("recorded when", "TBD", "TBC"))]
    if no_locator:
        issues.append(f"[md] {len(no_locator)} run(s) without a replicable URL/locator "
                      f"(real URL or 'UI: <action path>'): {', '.join(no_locator)}")
    cov = coverage_data(review)
    if cov["static"]["no_check_row"]:
        issues.append(f"[md] {len(cov['static']['no_check_row'])} target criteria have no check row in "
                      f"ontology/modality-checks.md: {', '.join(cov['static']['no_check_row'])}")
    if cov["static"]["orphan_checks"]:
        issues.append("[md] check rows mapping to no criterion (and not FPC-only): "
                      + ", ".join(cov["static"]["orphan_checks"]))
    if cov["stale_runs"]:
        issues.append(f"[md] {len(cov['stale_runs'])} run(s) behind the checklist (review.py sync-checks): "
                      + ", ".join(r["run"] for r in cov["stale_runs"]))

    # ---- [done] + [db] from the mirror
    done_rows, complete = [], False
    if db_sync(review):
        import review_db
        con = review_db.connect(review)
        done_rows = review_db.completion(con, review.name, review)
        for r in done_rows:
            if r["total"] and r["done"] >= r["total"]:
                continue
            head = ", ".join(str(m) for m in r["missing"][:6]) + (f" … +{len(r['missing']) - 6}" if len(r["missing"]) > 6 else "")
            issues.append(f"[done] {r['name']}: {r['done']}/{r['total']} — {r['description']}"
                          + (f" — missing: {head}" if head else ""))
        for i in review_db.integrity(con, review.name):
            head = "; ".join(i["items"][:4]) + (f"; … {i['count'] - 4} more" if i["count"] > 4 else "")
            issues.append(f"[db] {i['check']} ({i['count']}): {head}")
        con.close()
        complete = all(r["total"] and r["done"] >= r["total"] for r in done_rows)
    else:
        issues.append("[db] mirror unavailable — completion not measured")

    data = {"review": review.name, "issues": issues, "completion": done_rows,
            "complete": complete and not issues}

    def text(d):
        sat = sum(1 for r in d["completion"] if r["total"] and r["done"] >= r["total"])
        if d["complete"]:
            print(f"{d['review']}: complete — {sat}/{len(d['completion'])} predicates satisfied, no issues.")
        else:
            print(f"{d['review']}: {len(d['issues'])} issue(s); completion {sat}/{len(d['completion'])} predicates")
            for i in d["issues"]:
                print(f"  - {i}")

    emit(data, args.json, text)
    sys.exit(0 if data["complete"] else 1)


def main():
    p = argparse.ArgumentParser(prog="review.py",
                                description="Manage isolated accessibility reviews under reviews/")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_new = sub.add_parser("new", help="scaffold a new review")
    p_new.add_argument("product", help='product name, e.g. "Adobe Express"')
    p_new.add_argument("--enclosure", help="enclosure template to seed scope exploration from")
    p_new.set_defaults(fn=cmd_new)

    p_log = sub.add_parser("log-test", help="log a test run before testing a view")
    p_log.add_argument("review", help="review directory name or unique substring")
    p_log.add_argument("--view", required=True, help="sample ID or view name (e.g. S1)")
    p_log.add_argument("--modality",
                       choices=REQUIRED_MODALITIES,
                       help="sensory/functional modality tested (508 FPC; omit for "
                            "pure tool sweeps like WAVE)")
    p_log.add_argument("--tool", required=True, help="instrument used (e.g. jaws, wave, keyboard, zoom)")
    p_log.add_argument("--url", help="page URL or location/path of the view")
    p_log.add_argument("--baseline", help="baseline combination ID from 03 §1.3 (e.g. B1)")
    p_log.add_argument("--task", help="task/process this run belongs to (e.g. T1)")
    p_log.add_argument("--tester", help="who ran the test")
    p_log.set_defaults(fn=cmd_log_test)

    for name, fn, needs_review in [("list", cmd_list, False),
                                   ("status", cmd_status, True),
                                   ("validate", cmd_validate, True),
                                   ("enclosures", cmd_enclosures, False),
                                   ("runs", cmd_runs, True),
                                   ("matrix", cmd_matrix, True),
                                   ("coverage", cmd_coverage, True),
                                   ("next", cmd_next, True)]:
        sp = sub.add_parser(name, help=f"{name}")
        if needs_review:
            sp.add_argument("review", help="review directory name or unique substring")
        sp.add_argument("--json", action="store_true", help="machine-readable output")
        sp.set_defaults(fn=fn)

    p_close = sub.add_parser("close-run",
                             help="set a run's Result (and optionally its open check rows)")
    p_close.add_argument("review")
    p_close.add_argument("runs", nargs="*", help="run IDs, e.g. R006 R007")
    p_close.add_argument("--result", required=True,
                         help="Works / Works with issues / Broken / N/A")
    p_close.add_argument("--reason", required=True,
                         help="goes in the **Result reasoning.** paragraph")
    p_close.add_argument("--answer-open", dest="answer_open",
                         help="also answer every blank check row: pass / fail / partial / n/a")
    p_close.add_argument("--note", help="observations text for those rows (default: the reason)")
    p_close.add_argument("--answer", action="append",
                         help="answer one row with its own reasoning: CHECK=outcome=note (repeatable)")
    p_close.add_argument("--removed-views", dest="removed_views", action="store_true",
                         help="select every run against a view that has left the sample")
    p_close.add_argument("--force", action="store_true", help="overwrite a Result already set")
    p_close.add_argument("--dry-run", dest="dry_run", action="store_true")
    p_close.set_defaults(fn=cmd_close_run)

    p_page = sub.add_parser("page", help="one page's full state: every modality, every open check")
    p_page.add_argument("review")
    p_page.add_argument("--view", help="a single sample ID (default: every sampled page)")
    p_page.add_argument("--json", action="store_true")
    p_page.set_defaults(fn=cmd_page)

    p_cp = sub.add_parser("close-page", help="assert a page is finished; refuses with reasons if not")
    p_cp.add_argument("review")
    p_cp.add_argument("view")
    p_cp.set_defaults(fn=cmd_close_page)

    p_gaps = sub.add_parser("gaps",
                            help="unanswered check rows — the reviewer session's question list")
    p_gaps.add_argument("review", help="review directory name or unique substring")
    p_gaps.add_argument("--view", help="limit to one sample ID (e.g. S1)")
    p_gaps.add_argument("--json", action="store_true", help="machine-readable output")
    p_gaps.set_defaults(fn=cmd_gaps)

    p_sync = sub.add_parser("sync-checks",
                            help="append check rows added to modality-checks.md since each run was logged")
    p_sync.add_argument("review", help="review directory name or unique substring")
    p_sync.set_defaults(fn=cmd_sync_checks)

    p_seed = sub.add_parser("seed", help="apply an enclosure to an existing review")
    p_seed.add_argument("review", help="review directory name or unique substring")
    p_seed.add_argument("--enclosure", required=True, help="enclosure name or unique substring")
    p_seed.set_defaults(fn=cmd_seed)

    p_save = sub.add_parser("save-enclosure",
                            help="save a review's enclosure to enclosures/products/")
    p_save.add_argument("review", help="review directory name or unique substring")
    p_save.add_argument("--name", help="override the enclosure name (default: product slug)")
    p_save.add_argument("--force", action="store_true", help="overwrite an existing enclosure")
    p_save.set_defaults(fn=cmd_save_enclosure)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
