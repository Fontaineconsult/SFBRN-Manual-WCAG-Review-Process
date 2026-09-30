# Agent operating manual — SFBRN Manual WCAG Review Process

This repo runs a **fixed, already-developed process**. Your job is to execute
it, not to rediscover or improve it ad hoc. The ontology docs are the law;
this file only routes you to them. When in doubt, read the routed doc before
acting — never guess structure, IDs, or workflow.

## What this process produces (read this before the routing table)

**Findings come from a human testing the product.** The reviewer drives the
product and narrates; the assistant converts narration into observations,
check outcomes, findings, and the rollup. That loop *is* the deliverable.

Automated tools (axe, WAVE) are **supporting instruments, not sources of
findings**. Every violation is human-confirmed → finding, or dismissed with
a written reason; every `incomplete` is routed to a modality check. A scan
result written straight into `05` as an outcome is a process violation, and
so is any finding whose evidence is only a tool's output. Measurement can
*support* a criterion (and is worth doing — it removes work from the
reviewer's plate), but it never substitutes for the walk.

Corollary: if the reviewer is not available, the honest assistant output is
a **sharper question list**, not more findings.

### Why the assistant's probes mislead (2026-08-06: three wrong hypotheses in one run)

Structural probes answer *"what exists in this state, right now"*. They do
**not** answer *"what a user can reach"* — and reachability is the whole
question in a stateful application. Every one of these was caught only
because the assistant asked before recording:

- **Absence in a snapshot ≠ absence of a mechanism.** No editable field
  existed anywhere in the DOM or the accessibility tree, so the assistant
  concluded text editing was pointer-only — a 2.1.1 Level A Blocker. Wrong:
  the field is *created on demand* when edit mode is entered. Probe each
  state, or ask.
- **Programmatic `.click()`/`.focus()` bypasses the app's own key
  handling.** Reproducing a reviewer's keyboard path that way landed on a
  different panel entirely. Use real dispatched key events
  (`Input.dispatchKeyEvent`) or the reviewer's own account.
- **An unexplained state change is not evidence of a defect.** A document's
  text changed mid-session; the assistant hypothesised silent
  keystroke-capture. The reviewer had simply edited it with the mouse.

**Instrument hierarchy when they disagree** — trust in this order:
1. the **reviewer's AT** (what a user actually experiences);
2. the **accessibility tree** (CDP `Accessibility.getFullAXTree`) — what the
   AT is given;
3. **DOM inspection / markup tools** — weakest, and routinely wrong here.
   `headingsMap` reported a "Canvas" heading that NVDA could not reach: the
   `<h2>` exists in markup and never becomes a heading in the tree. Never
   let a markup tool contradict a screen reader.

Also: confirm control names **on focus**, never from an AT's elements list —
NVDA's list rendered labelled tabs as "Unlabeled" on S2 and nearly produced
a false Major finding. The rule covers **presence as well as names**: on
2026-09-14 an empty NVDA links-list dialog was read as "this page exposes no
links" and closed a 2.4.4 row as n/a; on 2026-09-21 the reviewer tabbed the
same page and the logo announced as "The ExperTa graphic visited link", with
six more real links at stops 2–7. An elements list is not an inventory —
absence from it is not absence from the page.

## A review, start to finish

**Six phases, in order.** Each one has to exist before the next is worth
starting; going out of order is how a review ends up with findings on pages
nobody chose and tasks nobody walked.

| # | Phase | You are done when | Command |
|---|---|---|---|
| 1 | **Intake** — what the product is, who asked, what the vendor claims | `01`, `02` filled; vendor ACR imported if there is one | `review.py new`, `import_acr.py` |
| 2 | **Site map** — what pages the product actually has | `03` §2.1 lists the product's views with real URLs, §2.2 the user stories, §2.4 the technologies | `crawl_map.py harvest` then `map` |
| 3 | **Sample** — which of those pages get tested | `03` §3.1 structured sample, §3.2 random sample; each row an `S#`/`R#` with a durable locator | reviewer decides; `review.py status` shows the sample |
| 4 | **Processes** — the tasks that span several pages | `03` §3.3: each process a step→view table; every view in a sequence is in the sample. `04` §A gets a task cluster per process | reviewer decides |
| 5 | **Test, page by page** — automate first, ask the reviewer what is left, close the page | every sampled page closes | `review.py next` → `page` → `gaps --view` → `close-page` |
| 6 | **Decide and publish** — the verdict, then the two reports | C1–C13 satisfied | `review_db.py completion`, `export_acr.py … --docx` (×2) |

**Phase 5 is the loop you will spend the review in, and it is per page:**

1. `review.py next <review>` names the page — it prefers a page already
   started, because half-walked pages are how reviews rot.
2. **Automate everything measurable first**, before the reviewer is asked
   anything: `axe_scan.py --view S# --url …` (saves `R###-axe.json`) and
   `view_probe.py --view S# --url …` (answers ~17 checks by measurement and
   names the rest). Never point the authenticated tab at the sign-in page.
3. `review.py gaps <review> --view S#` — **that is the reviewer's question
   list for this page**, and it is now complete even before any run exists.
4. Reviewer walks the page and narrates; the assistant records observations,
   answers check rows, raises findings, rolls them up.
5. `review.py close-page <review> S#` — it refuses, with reasons, until every
   modality has a resulted run, every check row is answered, and the sweep is
   triaged. **Do not open the next page until this passes.**

**Then the tasks.** When every page is closed, `next` names the task clusters
still to walk. §A of `04` is where the reports' task verdicts come from, and a
review that only ever swept views has not done the work.

**The deliverables are generated, never written.** `05-results.md` is the
source; `06-report.md` is the decision record, not a report. If you are
writing report prose anywhere but a `Plain summary` or a `Remediation` line,
you are in the wrong file.

## Session start (every session, before anything else)

0. **No review yet?** `python scripts/review.py new` and work the phases
   above in order. Everything below assumes a review already exists.
1. `python scripts/review.py list` — reviews and their states, then
   `python scripts/review_db.py state <review> --log` — the review-state
   dashboard (definition of done, POUR, FPC, matrix, findings, vendor
   delta, what moves the needle), logged as a row in
   `reviews/<id>/state-log.md` so progress between sessions is a diff of
   two rows. `status`
   ends with the completion line (predicates of the definition of done
   satisfied, from the database). The same data as a page:
   `reviews/<id>/<id>-dashboard.html` (`scripts/dashboard.py`, regenerated
   by every sync; `--open` shows it) — the reviewer's map of the review,
   every run and step a link. Point the reviewer at it; never hand-edit it.
2. Working a review? `python scripts/review.py status <review>` then
   `validate <review>` — the gap list IS the to-do list — then
   `coverage <review>`, and read the `[db]` lines of `validate` — integrity
   queries over the SQLite mirror (`ontology/data-store.md`). Which criteria, POUR principles and 508 FPC have an
   **answered** check, and its reliability flags (an Outcome with no check
   behind it, a failed check not rolled up, runs behind the checklist).
3. **Is a session already in flight?** `ls reviews/<id>/session-*-walkthrough.md`.
   A walkthrough with `**Feedback:** _(pending)_` lines **is** the saved
   place — it holds the ordered remaining steps, why each matters, and what
   the last session established. Read it before planning anything; do not
   regenerate one that already carries feedback (append dated steps
   instead). The newest run folder tells you which part was active.
4. Read the two lines most agents skim past:
   - **`task T#: Not run`** — §A of `04` is the heart of this process
     (findings that read "this task fails at this step"). An empty §A with
     findings piling up in §B means the review has been doing view sweeps
     and never walked a process. Say so out loud; don't quietly keep
     sweeping.
   - **runs without a Result** — these are half-finished sessions, usually
     blocked on the reviewer, not on you.
5. **Reduce the reviewer's workload first.** Every sampled view gets
   `python scripts/view_probe.py <review> --view S# --url URL` before the
   reviewer is asked anything: it answers by measurement what a structural
   fact decides (no video → captions n/a; no speech API → NS1 n/a; `lang`,
   title, target size, reflow, text spacing, autocomplete) and names the
   rest. The reviewer's question list is what `gaps` shows *after* that.
   Never point the authenticated tab at the sign-in page (it ends the
   session) — sign-in views use the signed-out profile on port 9223.
6. Testing? `python scripts/review.py next <review>` names the target.
   Don't invent priorities; `next` already encodes them (vendor-claim
   discrepancies first). Then
   `python scripts/review.py gaps <review> --view S#` prints the unanswered
   check rows — **that is the session's question list**; never improvise one
   or ask the reviewer things the runs already answer.
7. **Environment pre-flight — only if this session will run tools.**
   `python scripts/preflight.py [--launch --url <product home>] [--anon]`
   runs every check below in one call and exits 1 on any failure; with
   `--launch` it starts the debug-profile Chrome (full flag set) when its
   port is dead. A sign-in tab is reported as the reviewer's next action —
   never yours. The checks, for when you need to do one by hand — they rot
   silently between sessions (dead on 2026-08-06 and again on 2026-09-14
   having worked the session before):
   - `python -c "import websocket"` — `axe_scan.py`'s dependency; a machine
     change or Python upgrade loses it.
     Fix: `python -m pip install -r requirements.txt` (added 2026-09-15;
     `websocket-client` for the CDP clients, `python-docx` for the export).
   - `%LOCALAPPDATA%\sfbrn-a11y-chrome` exists **and** port 9222 answers
     **and** the tab is authenticated **and** no **store** extension is
     running — Chrome's own component workers are persistent on Chrome 153
     and are fine; a `chrome-extension://` target whose ID is unpacked under
     the profile's `Default\Extensions` is not (that profile still holds 21
     of them, Stylus and SkipTo Landmarks included, inert only while
     `--disable-extensions` is passed) — see testing-tools.md §axe-core.
     The profile can vanish; SSO usually re-authenticates it silently, so
     check rather than asking the reviewer to sign in. Launch it only
     with the full flag set in that doc: without `--disable-extensions
     --disable-sync`, Chrome's first-run promo syncs the reviewer's
     personal extensions into the profile (2026-08-14: 22 of them,
     including Stylus and SkipTo Landmarks, which respectively falsify
     contrast measurement and *add* the skip link 2.4.1 is about).

Never trust memory or this file for review state — the CLI reads the files
live.

## Task routing

**The trigger is what you are about to touch, not what the user called it.**
Match on the *file or artifact*, not on the user's wording — vague prompts
("situate yourself", "make this useful", "get the browser working") route to
nothing and are the main way agents end up improvising. In particular: if
you are about to write into any `reviews/<id>/` file or `evidence/runs/`,
you are in the testing loop — **read `ontology/testing-loop.md` first**, even
if nobody said the word "test".

| Task | Read first | Write into |
|------|-----------|------------|
| Start a new review | README §"The review CLI" | `review.py new` + seed enclosure — never hand-create dirs |
| Intake / vendor info | the stage file's own template text | `01-intake.md`, `02-vendor.md` |
| Import a vendor ACR | `scripts/import_acr.py --help` | `vendor-acr/`, claim lines in `05-results.md` |
| Explore the product (WCAG-EM step 2) | `ontology/assisted-exploration.md` | `03-scope-and-sample.md` §1.1, §2, §3.1 proposals |
| Take work off the reviewer before a session (instrument-answerable checks) | `ontology/modality-checks.md` §Assistant-answerable checks, `ontology/testing-tools.md` §view_probe | `scripts/view_probe.py` → the cell's run (pass / n/a / measured fail + `R###-probe.json`); sign-in views only via the signed-out profile |
| Test (the loop) | `ontology/testing-loop.md`, `ontology/modality-checks.md`, `ontology/testing-tools.md` | run file → `04-task-testing.md` → `05-results.md` → enclosure |
| Log/scaffold a run | `review.py log-test` (only way) | `evidence/runs/R###/` |
| Close a run (set its Result) | `review.py close-run --help`, ontology/testing-loop.md §Closing a run | the run's Result cell + `**Result reasoning.**` — never by hand; every note names its basis |
| Reviewer-driven session (JAWS, zoom, confirmations) | `ontology/testing-loop.md` §Reviewer session walkthroughs | `reviews/<id>/session-<sample>-reviewer-walkthrough.md` + the runs it feeds |
| Results rollup | `05` template text | `05-results.md` — the source **both** reports generate from |
| Record the procurement decision (human) | `06` template text | `06-report.md` — the decision, its rationale, the vendor-ACR audit and this review's limits. Never a report: everything else is generated |
| Finish a review | `review.py validate` until clean (C1–C13) | both reports regenerated (`export_acr.py <review> --docx` and `--internal --docx`), then `save-enclosure` |
| Export the report for distribution | `scripts/export_report.py --help`, ontology/reporting.md §Distribution | `reviews/<id>/<id>-report.docx` — generated output; edit the .md and re-export, never the .docx |
| Export an ACR (VPAT-shaped, for a counterparty who needs the grid) | ontology/reporting.md §Third output | `reviews/<id>/<id>-acr.html` (+ `-acr.docx` with `--docx`) — generated from the **database only**, never from notes or prose; fix `05` and regenerate. Branding comes from `branding.json` (copy `branding.example.json`) or `--org`/`--logo` |
| Export the internal report (campus-facing: what a user cannot do, feeds a TAAP) | ontology/reporting.md §Fourth output, `ontology/TAAP Version 3_2 051225.docx` | `reviews/<id>/<id>-internal.html` — `export_acr.py <review> --internal`; same database, never carries the procurement decision |
| Verify a result, count, or cross-reference | `ontology/data-store.md` | nothing — `python scripts/review_db.py query "SQL"` / `check <review>`; the SQLite mirror is the place to verify, the files stay the record |
| Change the process itself | the doc being changed | `ontology/` + `templates/` + `scripts/` + README together — never just deviate in-session |

## Hard rules

- **CLI only** for scaffolding, run logging, coverage, validation. Never
  hand-create review directories, run folders, or IDs. Run the CLI from the
  repo root — `Set-Location` there first; a bare `python scripts/review.py`
  from a review subdirectory fails on the path.
- **Don't inline Python in the shell.** PowerShell strips quotes when
  passing to native exes, so `python -c "..."` and here-strings mangle any
  script containing quotes or regex. Write the script to the scratchpad
  directory and run it by path — two calls instead of four failed ones.
- **Never round-trip file content through PowerShell string ops.**
  `Get-Content` (PS 5.1) reads UTF-8 files as ANSI by default, so a
  `Get-Content | -replace | Set-Content` pipeline mojibakes every em-dash,
  §, and × in the file and adds a BOM — it corrupted `05` and `06` on
  2026-08-13 (repaired by reversing the double-encoding in Python). All
  content edits go through Edit/Write or a Python script.
- **IDs are stable once assigned** (C/F/S/P/T/R and finding IDs). Append new
  ones; never renumber or reuse.
- **Markdown authors, the database measures.** The stage files and run
  files are the first artifact — write there, with all the detail the
  narrative needs. What gets extracted into `reviews/<id>/<id>.sqlite` is fixed
  by the extraction contract in `ontology/data-store.md`; **review
  completion is the database's verdict** (`review_db.py completion`, the
  `[done]` lines of `validate`), never a reading of the files. If a fact
  must count toward completion it must be in an extracted field — a
  sentence in prose does not count.
- **Verify with SQL, not by re-reading markdown.** Every structured fact
  (criteria, checks, runs, check outcomes, observations, findings, 05
  outcomes, tasks, probe/axe measurements) is mirrored deterministically into
  `reviews/<id>/<id>.sqlite` (`scripts/review_db.py`; rebuilt by `validate`,
  `coverage`, `log-test`, the probe). Before asserting a count, a
  cross-reference ("finding X is rolled up under 1.3.1"), or a comparison
  across reviews, run the query. The markdown remains the record; the DB is
  how you check it. `review_db.py check <review>` lists what the files
  contradict.
- **Coverage is tracked at the check row, not the run.** A criterion counts
  as tested only when a check mapped to it is answered (pass/fail/partial/n/a)
  in a logged run; `05` Outcomes without that are validate failures. Every
  WCAG 2.2 AA criterion has a check row and every check maps to a criterion
  or FPC (modality-checks.md §Completeness contract). If you add or rename a
  check row, run `review.py sync-checks` on every in-flight review. Report
  coverage in POUR and 508-FPC terms (`coverage`), never as run counts.
- **Every finding carries a `Plain summary`** — one authored sentence, present
  tense, about the product, naming what a user cannot do; no IDs, dates,
  reviewer or tool names; ≤ 200 chars. It is the only text in the record
  written for a reader, it is what the ACR publishes, and `review_db.py check`
  enforces the rules (ontology/reporting.md §Plain summary). Never write report
  prose in a generator; write it once, here.
- **Every published criterion carries a `Remediation`** — one authored,
  imperative instruction in `05`, covering *all* of that criterion's findings
  and naming the product's own working example where one exists; says what to
  build, never which framework; ≤ 450 chars. Required wherever the outcome is
  Does Not Support, or Partially Supports at Level A — the set the ACR's
  Priorities section publishes. `Plain summary` says what is wrong;
  `Remediation` says what to do. `review_db.py check` enforces both
  (ontology/reporting.md §Remediation).
- **Findings cite runs.** Exploration observations are recon → `03` §2.6,
  phrased "verify X under check Y in a run". No run, no finding.
- **Every run carries a replicable locator** — validate enforces it. A real
  URL (durable form: strip transient params like `?category=`/`?pageId=`;
  for documents use the `/id/urn:aaid:…` ID, never the display name — names
  drift, IDs don't; the review keeps a document registry in `03` §2.6), or
  an explicit `UI: <action path>` for states with no address (e.g.
  `UI: Home → "Start new design" → Get started modal`). Resolve
  placeholders like "(ID recorded when created)" the moment the artifact
  exists, not later — R016's stayed unresolved for four days and the
  document's display name had changed by the time it was chased.
- **"Unmeasured" is a valid result; a confident wrong number is not.** When
  an instrument cannot reach something, record that plus the instrument that
  could, and move on. The trap that catches agents: contrast by
  ancestor-walking silently falls back to white when the background is
  painted by a pseudo-element or image, yielding a clean-looking 21:1 that
  is pure fiction (testing-tools.md §zoom lists the three background cases
  and which method each needs). Discard it — never write it into a run.
- **Step-2 statements** are either `confirmed <date>` or an explicit
  hypothesis — never silently mixed.
- **Write-back order** during testing (testing-loop.md step 6): run checks +
  observations → run Result → findings in `04` → rollup in `05` → enclosure
  in `03`. Immediately, not at session end.
- **Keep template table shapes and headings intact** — `review.py`
  status/validate/matrix parse them. After editing review files, re-run
  `status` + `validate`; a parse regression is a broken edit.
- **The decision is human.** Never set the `06-report.md` procurement
  decision (Approved / Approved with TAAP / Do Not Purchase) yourself; draft the evidence,
  the reviewer decides.
- **Browser work** follows `ontology/assisted-exploration.md` preconditions:
  the reviewer is signed in with the review's test account; you never
  authenticate, create accounts, purchase, permanently delete, or submit
  forms. Record any artifact your exploration creates (e.g., an Untitled
  document).
- **Every sampled view gets an automated sweep run** — validate enforces
  it. Primary: `python scripts/axe_scan.py <review> --view S# --url URL`
  (assistant-runs it; logs the run, saves raw `R###-axe.json`; needs the
  dedicated debug-profile Chrome — setup in testing-tools.md §axe-core;
  default-profile debugging does not work on Chrome 136+). WAVE is
  secondary and reviewer-run — blind on shadow-DOM apps (testing-tools.md).
- **Vocabulary is fixed:** procurement decisions (Approved / Approved with
  TAAP / Do Not Purchase — `rv.DECISIONS`, checked by `review_db.py check`),
  ACR outcomes (Supports / Partially Supports /
  Does Not Support / Not Applicable / Not Evaluated), task verdicts (Pass /
  Pass with barriers / Fail), run results (Works / Works with issues /
  Broken / N/A), modalities (no-vision, low-vision, no-color, no-hearing,
  no-speech, motor, cognition). Never invent synonyms.

## The ratchet (process-gap rule)

If you had to figure something out — a workflow wasn't documented, a doc was
ambiguous, a command was missing — the process failed, not you. Fix the
process artifact (ontology doc, template, script, this file) **in the same
session**, so the next agent inherits the answer instead of re-deriving it.
That is the only sanctioned way the process changes.

## Map

- `README.md` — process overview and CLI reference
- `ontology/` — method docs (law): wcag-em, testing-loop,
  assisted-exploration, modality-checks, testing-tools,
  selecting-evaluation-tools
- `templates/review/` — stage-file templates (structure contract for the CLI)
- `enclosures/` — archetype + saved product enclosures
- `reviews/<id>/` — the system of record, one dir per review
- `scripts/review.py` — the management CLI; `scripts/import_acr.py` — ACR
  importer; `scripts/review_db.py` — the SQLite mirror (`reviews/<id>/<id>.sqlite`,
  one per review, committed, rebuilt deterministically from the files) and its integrity checks
- `tools/` — W3C evaluation-tools catalog
