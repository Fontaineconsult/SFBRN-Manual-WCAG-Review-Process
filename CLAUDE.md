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
a false Major finding.

## Session start (every session, before anything else)

1. `python scripts/review.py list` — reviews and their states.
2. Working a review? `python scripts/review.py status <review>` then
   `validate <review>` — the gap list IS the to-do list.
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
5. Testing? `python scripts/review.py next <review>` names the target.
   Don't invent priorities; `next` already encodes them (vendor-claim
   discrepancies first). Then
   `python scripts/review.py gaps <review> --view S#` prints the unanswered
   check rows — **that is the session's question list**; never improvise one
   or ask the reviewer things the runs already answer.
6. **Environment pre-flight — only if this session will run tools.** It rots
   silently between sessions (both of these were dead on 2026-08-06 having
   worked on 2026-08-04):
   - `python -c "import websocket"` — `axe_scan.py`'s dependency; the repo
     has no manifest, so a machine change or Python upgrade loses it.
     Fix: `python -m pip install websocket-client`.
   - `%LOCALAPPDATA%\sfbrn-a11y-chrome` exists **and** port 9222 answers
     **and** the tab is authenticated — see testing-tools.md §axe-core.
     The profile can vanish; SSO usually re-authenticates it silently, so
     check rather than asking the reviewer to sign in.

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
| Test (the loop) | `ontology/testing-loop.md`, `ontology/modality-checks.md`, `ontology/testing-tools.md` | run file → `04-task-testing.md` → `05-results.md` → enclosure |
| Log/scaffold a run | `review.py log-test` (only way) | `evidence/runs/R###/` |
| Reviewer-driven session (JAWS, zoom, confirmations) | `ontology/testing-loop.md` §Reviewer session walkthroughs | `reviews/<id>/session-<sample>-reviewer-walkthrough.md` + the runs it feeds |
| Results rollup / report | `05`/`06` template text | `05-results.md`, `06-report.md` |
| Finish a review | `review.py validate` until clean | `06-report.md`, then `save-enclosure` |
| Export the report for distribution | `scripts/export_report.py --help`, ontology/reporting.md §Distribution | `reviews/<id>/<id>-report.docx` — generated output; edit the .md and re-export, never the .docx |
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
- **IDs are stable once assigned** (C/F/S/P/T/R and finding IDs). Append new
  ones; never renumber or reuse.
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
  decision (Approved / Needs TAAP / Denied) yourself; draft the evidence,
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
- **Vocabulary is fixed:** ACR outcomes (Supports / Partially Supports /
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
  importer
- `tools/` — W3C evaluation-tools catalog
