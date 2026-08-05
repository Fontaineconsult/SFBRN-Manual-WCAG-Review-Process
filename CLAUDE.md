# Agent operating manual — SFBRN Manual WCAG Review Process

This repo runs a **fixed, already-developed process**. Your job is to execute
it, not to rediscover or improve it ad hoc. The ontology docs are the law;
this file only routes you to them. When in doubt, read the routed doc before
acting — never guess structure, IDs, or workflow.

## Session start (every session, before anything else)

1. `python scripts/review.py list` — reviews and their states.
2. Working a review? `python scripts/review.py status <review>` then
   `validate <review>` — the gap list IS the to-do list.
3. Testing? `python scripts/review.py next <review>` names the target.
   Don't invent priorities; `next` already encodes them (vendor-claim
   discrepancies first).

Never trust memory or this file for review state — the CLI reads the files
live.

## Task routing

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
| Change the process itself | the doc being changed | `ontology/` + `templates/` + `scripts/` + README together — never just deviate in-session |

## Hard rules

- **CLI only** for scaffolding, run logging, coverage, validation. Never
  hand-create review directories, run folders, or IDs.
- **IDs are stable once assigned** (C/F/S/P/T/R and finding IDs). Append new
  ones; never renumber or reuse.
- **Findings cite runs.** Exploration observations are recon → `03` §2.6,
  phrased "verify X under check Y in a run". No run, no finding.
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
