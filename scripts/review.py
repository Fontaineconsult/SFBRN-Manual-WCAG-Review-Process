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
DECISION_PLACEHOLDER = "Approved / Needs TAAP / Denied"
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
    if not m or m.group(1) == DECISION_PLACEHOLDER:
        return "Pending"
    return m.group(1)


def criteria_counts(review):
    text = read(review / STAGES[4])
    counts = {o: 0 for o in OUTCOMES}
    other = 0
    for m in re.finditer(r"- \*\*Outcome:\*\*\s*(.*)", text):
        val = m.group(1).strip()
        if val in counts:
            counts[val] += 1
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


def vendor_claims(review):
    """Map SC number -> vendor claim string from 05-results.md."""
    claims = {}
    for block in re.split(r"(?=^### )", read(review / STAGES[4]), flags=re.M):
        h = re.match(r"### (\d+\.\d+\.\d+) ", block)
        v = re.search(r"- \*\*Vendor claim:\*\* (.+)", block)
        if h and v:
            claims[h.group(1)] = v.group(1).strip()
    return claims


def sample_views(review):
    """Return [(id, name)] for sampled views (S#/R# rows with a view name)
    from 03-scope-and-sample.md."""
    text = read(review / STAGES[2])
    views = []
    for m in re.finditer(r"(?m)^\|\s*([SR]\d+)\s*\|\s*([^|]*?)\s*\|", text):
        if m.group(2):
            views.append((m.group(1), m.group(2)))
    return views


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

    print(f"Run {rid} logged: {run_dir.relative_to(ROOT)}")
    print(f"  view={args.view}  modality={fields['modality']}  tool={args.tool}  "
          f"baseline={fields['baseline']}")
    print(f"  Notes and evidence go in {run_dir.relative_to(ROOT)}\\run.md "
          f"and {rid}-*.png files alongside it.")


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


def cmd_gaps(args):
    """The assistant's question list: every check row still without an outcome.

    testing-loop.md step 5 says gap questions come from deterministic gaps,
    not improvisation — this is where that list comes from. `validate` says
    which runs lack a Result; this says which *checks* are unanswered, which
    is what a reviewer session actually works through.
    """
    review = resolve(args.review)
    rows = []
    for d in run_dirs(review):
        meta = run_meta(d)
        if args.view and meta["view"].lower() != args.view.lower():
            continue
        txt = read(d / "run.md")
        checks = re.findall(
            r"^\|\s*((?:NV|LV|NC|NH|NS|MO|CO|W)\d+)\s*—\s*(.+?)\s*\|(.*?)\|",
            txt, re.M)
        for cid, label, outcome in checks:
            if not outcome.strip():
                rows.append({"run": meta["run"], "view": meta["view"],
                             "modality": meta["modality"], "tool": meta["tool"],
                             "check": cid, "label": label.strip(),
                             "result": meta["result"]})

    def text(rows):
        if not rows:
            print("No unanswered check rows"
                  + (f" on {args.view}" if args.view else "")
                  + ". Every logged run's checklist is complete.")
            return
        by_run = {}
        for r in rows:
            by_run.setdefault(r["run"], []).append(r)
        for run, items in by_run.items():
            head = items[0]
            print(f"{run}  view={head['view']}  modality={head['modality']}  "
                  f"tool={head['tool']}  ({len(items)} unanswered)")
            for r in items:
                print(f"    [ ] {r['check']} — {r['label'][:88]}")
            print()
        print(f"TOTAL unanswered check rows"
              + (f" on {args.view}" if args.view else "") + f": {len(rows)}")

    emit(rows, args.json, text)


def cmd_next(args):
    review = resolve(args.review)
    views = sample_views(review)
    if not views:
        print("No sampled views defined yet — add your initial page(s) as S# rows "
              "in 03 §3.1 (view name + URL), then run next again.")
        return
    runs = [run_meta(d) for d in run_dirs(review)]
    covered = {(r["view"].lower(), r["modality"].lower()) for r in runs}
    swept = {r["view"].lower() for r in runs if r["tool"].lower() in SWEEP_TOOLS}

    # score modalities by vendor-claim discrepancy value: verifying claimed
    # failures (and shaky Partially Supports) first produces decision-relevant
    # evidence fastest
    sc2mod = sc_to_modalities()
    weights = {}
    reasons = {}
    for sc, claim in vendor_claims(review).items():
        w = 3 if "Does Not Support" in claim else 1 if "Partially Supports" in claim else 0
        if not w:
            continue
        for m in sc2mod.get(sc, ()):
            weights[m] = weights.get(m, 0) + w
            reasons.setdefault(m, []).append(f"{sc} ({'DNS' if w == 3 else 'PS'})")

    candidates = []
    for vi, (vid, name) in enumerate(views):
        for mi, m in enumerate(REQUIRED_MODALITIES):
            if (vid.lower(), m) not in covered:
                candidates.append({"view": vid, "name": name, "modality": m,
                                   "score": weights.get(m, 0),
                                   "why": reasons.get(m, []),
                                   "order": (vi, mi)})
    candidates.sort(key=lambda c: (-c["score"], c["order"]))
    data = {"review": review.name,
            "next": candidates[:5],
            "unswept_views": [vid for vid, _ in views if vid.lower() not in swept]}

    def text(d):
        if not d["next"]:
            print("All view×modality cells have runs."
                  + (f" Automated sweeps (axe/wave) still missing: {', '.join(d['unswept_views'])}"
                     if d["unswept_views"] else " Coverage complete."))
            return
        top = d["next"][0]
        tool, baseline = MODALITY_DEFAULTS.get(top["modality"], ("inspection", "—"))
        n_checks = len(modality_checklist(top["modality"]))
        print(f"Next: {top['view']} ({top['name']}) × {top['modality']}"
              f"  [{n_checks} checks]")
        if top["why"]:
            print(f"  why: vendor claims to verify — {', '.join(top['why'])}")
        print(f"  python scripts/review.py log-test {d['review']} "
              f"--view {top['view']} --modality {top['modality']} "
              f"--tool {tool} --baseline {baseline}")
        if len(d["next"]) > 1:
            print("then:")
            for c in d["next"][1:]:
                print(f"  {c['view']} ({c['name']}) × {c['modality']}"
                      + (f"  [score {c['score']}]" if c["score"] else ""))
        if d["unswept_views"]:
            print(f"Automated sweeps (axe/wave) still missing: {', '.join(d['unswept_views'])}")

    emit(data, args.json, text)


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
            "views": grid, "gaps": gaps,
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

    emit(data, args.json, text)


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

    emit(data, args.json, text)


def cmd_validate(args):
    review = resolve(args.review)
    issues = []

    for s in STAGES:
        if not (review / s).exists():
            issues.append(f"missing stage file: {s}")

    counts = criteria_counts(review)
    if counts["Not Evaluated"]:
        issues.append(f"{counts['Not Evaluated']} criteria still 'Not Evaluated' in 05-results.md")
    if counts["(unrecognized)"]:
        issues.append(f"{counts['(unrecognized)']} Outcome lines in 05-results.md not using ACR vocabulary")

    t = tasks(review)
    if not t:
        issues.append("no task clusters defined in 04-task-testing.md")
    for tid, name, verdict in t:
        if verdict in ("Not run", "?"):
            issues.append(f"task {tid} has no verdict")

    real_findings = 0
    for fid, crit in findings(review):
        if not crit or crit.startswith("(e.g.") or crit.startswith("(step"):
            issues.append(f"finding {fid} lists no WCAG criteria failed")
        else:
            real_findings += 1
    if real_findings and not run_dirs(review):
        issues.append(f"{real_findings} finding(s) recorded but no test runs logged "
                      "(log-test) — findings need replicable run evidence")

    runs = [run_meta(d) for d in run_dirs(review)]
    unset = [r["run"] for r in runs if r["result"] == "Not set"]
    if unset:
        issues.append(f"{len(unset)} run(s) without a Result "
                      f"(Works / Works with issues / Broken): {', '.join(unset)}")
    # Every run needs a replicable locator: a real URL, or an explicit
    # UI-action path ("UI: ...") for states with no address. Placeholders
    # ("recorded when created", TBD/TBC) and empty fields fail review
    # replication and vendor rebuttal alike.
    no_locator = [r["run"] for r in runs
                  if not (("http" in r["url"]) or r["url"].startswith("UI:"))
                  or any(p in r["url"] for p in ("recorded when", "TBD", "TBC"))]
    if no_locator:
        issues.append(f"{len(no_locator)} run(s) without a replicable URL/locator "
                      f"(real URL or 'UI: <action path>'): {', '.join(no_locator)}")
    views = sample_views(review)
    if views:
        gaps = [f"{vid}×{m}" for vid, _ in views for m in REQUIRED_MODALITIES
                if not any(r["view"].lower() == vid.lower()
                           and r["modality"].lower() == m for r in runs)]
        if gaps:
            issues.append(f"modality coverage: {len(gaps)} view×modality cell(s) "
                          "not yet run (see review.py matrix)")
        unswept = [vid for vid, _ in views
                   if not any(r["view"].lower() == vid.lower()
                              and r["tool"].lower() in SWEEP_TOOLS for r in runs)]
        if unswept:
            issues.append(f"automated sweep (axe/wave) missing for view(s): {', '.join(unswept)}")

    unchecked = len(re.findall(r"^- \[ \]", read(review / STAGES[3]), re.M))
    if unchecked:
        issues.append(f"{unchecked} coverage-check boxes unchecked in 04-task-testing.md")

    if decision(review) == "Pending":
        issues.append("procurement decision not set in 06-report.md")

    data = {"review": review.name, "issues": issues, "complete": not issues}

    def text(d):
        if d["complete"]:
            print(f"{d['review']}: complete — no validation issues.")
        else:
            print(f"{d['review']}: {len(d['issues'])} issue(s)")
            for i in d["issues"]:
                print(f"  - {i}")

    emit(data, args.json, text)
    sys.exit(0 if not issues else 1)


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
                                   ("next", cmd_next, True)]:
        sp = sub.add_parser(name, help=f"{name}")
        if needs_review:
            sp.add_argument("review", help="review directory name or unique substring")
        sp.add_argument("--json", action="store_true", help="machine-readable output")
        sp.set_defaults(fn=fn)

    p_gaps = sub.add_parser("gaps",
                            help="unanswered check rows — the reviewer session's question list")
    p_gaps.add_argument("review", help="review directory name or unique substring")
    p_gaps.add_argument("--view", help="limit to one sample ID (e.g. S1)")
    p_gaps.add_argument("--json", action="store_true", help="machine-readable output")
    p_gaps.set_defaults(fn=cmd_gaps)

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
