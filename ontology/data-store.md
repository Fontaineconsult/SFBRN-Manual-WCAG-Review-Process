# The data store — markdown authors, the database measures

Added 2026-09-11, when the reviewer raised the risk that every number this
process reports is re-parsed out of markdown at read time. The decision
taken that day, in the reviewer's words: **use the markdown as the first
artifact** (it is more flexible and holds more detail), **fix a rule set
for what in the markdown gets put into the database**, and **use the
database as the measure of review completion**.

## Roles

| | Markdown (01–06, `run.md`) | `reviews/<id>/<id>.sqlite` (`scripts/review_db.py`) |
|---|---|---|
| Role | **the first artifact** — humans and agents write here, with all the narrative, reasoning and evidence the review needs | **the measure** — a deterministic extraction of the structured facts, queried for completion, integrity, counts and comparisons |
| Authority | the record (git-versioned) | derived: rebuilt from the files by `sync`; nothing lives only here |
| Freshness | — | `validate`, `status`, `coverage`, `log-test`, `sync-checks` and the probe re-sync before they read |
| Completion | never read off the files | `review_db.py completion <review>` — the definition of done below; `validate` reports it as `[done]` lines and exits 1 until every predicate holds |

**The rule that follows:** if a fact must count toward completion, it must
be in an *extracted field* (a table cell, an outcome cell, a checkbox, a
Result term). A sentence in prose is for humans; the database does not see
it, and a review does not become complete by writing prose.

## Extraction contract — what is taken from the markdown, and how

Everything not listed stays markdown-only by design (sequence notes,
result reasoning, narration, remarks prose, walkthrough files, screenshots).

| Artifact | Extracted | Table | Normalisation / rule |
|---|---|---|---|
| `01-intake.md` H1 | product name | `reviews.product` | text after "Review Intake — " |
| `06-report.md` header table | `**Decision**` cell; `**Report status**` cell | `reviews.decision`, `reviews.report_status` | decision placeholder → `Pending` |
| `03` §3.1 / §3.2 rows | `\| S# \| name \| locator \| represents \|`; `\| R# \| name \| locator \|` | `views` | row exists only if the name cell is non-empty; kind = structured / random; `removed` = `YYYY-MM-DD: reason` when the name ends in ` — removed YYYY-MM-DD: reason` (the view stays on record but leaves the sample: C6, C7, the FPC counts, the matrix and the dashboard use `removed=''` only; integrity still recognises its runs) |
| `04` §A `### Task T# — name — …` blocks | task id, name, `**Verdict**`, `**Baselines run**`, `**Date(s) tested**` cells | `tasks` | verdict placeholder → `Not run`; only the four fixed verdict terms count as decided |
| `04` `#### Finding <ID>` blocks | every `\| **Label** \| value \|` row (kept whole as JSON); `Where`, `Observed`, `Affected users`, `Severity`, `Evidence` | `findings` (+ `fields_json`) | section = task if under `## A.`, else view; view = leading `S#`/`R#` of *Where*; task = `T#` prefix of the ID |
| … `**WCAG criteria failed**` cell | every `d.d.d` token | `finding_criteria` | a finding "fails" exactly the criteria named here, nowhere else |
| … `**Evidence**` + `**Observed**` cells | every `R###` token | `finding_runs` | this is the evidence trail `validate` enforces (no run, no finding) |
| … withdrawn flag | the word *withdrawn* in the criteria cell, the first 120 chars of *Observed*, or *Severity* | `findings.withdrawn` | withdrawn findings never count; a `05` block citing one is an integrity issue |
| `05` `### d.d.d Name (Level X)` blocks | `- **Outcome:**`, `- **Vendor claim:**`, `- **Task findings:**`, `- **Remarks:**` | `criterion_outcomes` | outcome normalised to the ACR term it *starts with* (`Partially Supports (provisional)` → `Partially Supports`); anything else is `[md]` unrecognised |
| … `**Task findings**` cell | every finding-ID token (`T1-F2`, `V-F11`) | `criterion_findings` | the rollup link; must match `finding_criteria` in both directions |
| `04` §D | every `- [ ]` / `- [x]` line | `coverage_boxes` | completion needs all checked |
| `session-*walkthrough.md` | every `### W# — title` step and its `**Feedback…:**` line(s) | `walkthrough_steps` | pending = no Feedback line or all still `_(pending)_`; KEY STEP flagged; a `**Measured …:**` note does not close a step — only a Feedback line does. "Where we left off" is `SELECT … WHERE feedback=''` |
| `run.md` metadata table | Date/time, View, URL/location, Task, Modality, Tool, Baseline, Tester, **Result** | `runs` | Result normalised to the bare term it starts with (`**Broken** — …` → `Broken`); `Not set — …` → `Not set`; full cell kept in `result_note` |
| `run.md` Checks table | every `\| ID — text \| outcome \| observations \|` row | `check_outcomes` | outcome = first token, bold/backticks stripped, in {pass, fail, partial, n/a}; blank = unanswered; anything else = `?` (integrity issue) |
| `run.md` Observations | `- O# [status] (state): text` lines and their `- Classified:` line | `observations` | status tag and classification kept verbatim |
| `R###-probe.json` | summary (title, lang, media, targets, reflow, text-spacing, script hits) + full facts | `measurements` (`probe`) | JSON; queryable with `json_extract` |
| `R###-axe.json` | each violation / incomplete rule (impact, node count, tags) + bucket counts | `measurements` (`axe`) | one row per rule per bucket |
| `ontology/modality-checks.md` | check rows and their WCAG cells; the modality → FPC table | `checks`, `check_criteria`, `fpc` | re-seeded on every sync |
| `templates/review/05-results.md` | the 55 target criteria | `wcag_criteria` | plus principle, guideline, version added, Understanding URL |

**Changing the contract** (a new extracted field, a new table): edit
`review_db.py` (`SCHEMA` + the parser in `sync_review`) *and* this table in
the same session, and re-run `sync --all`. Changing a template shape is a
contract change (the ratchet).

## Definition of done — `review_db.py completion <review>`

Twelve predicates, each a query over the mirror. A review is complete when
all twelve hold; `validate` exits 0 only then.

| # | Predicate | Numerator / denominator |
|---|---|---|
| C1 | criteria decided | `05` outcomes ≠ Not Evaluated / 55 |
| C2 | criteria evidenced | criteria with ≥ 1 answered check in a run / 55 |
| C3 | tasks verdict | tasks with Pass / Pass with barriers / Fail / tasks |
| C4 | runs resulted | runs with Works / Works with issues / Broken / N/A / runs |
| C5 | checks answered | check rows with an outcome / check rows |
| C6 | cells run | view × modality cells with a resulted run / views × 7 |
| C7 | views swept | views with an axe or WAVE run / views |
| C8 | FPC exercised | FPC with an answered check on some view / 9 |
| C9 | findings evidenced | live findings with criterion + severity + run / live findings |
| C10 | coverage boxes | boxes checked / boxes in `04` §D |
| C11 | integrity clean | 0 issues from the integrity queries |
| C12 | decision (human) | decision set + report status FINAL / 2 — the reviewer's act, never the assistant's |

C1–C11 are the assistant's and reviewer's shared work; C12 is the
reviewer's alone. `status` prints the unsatisfied ones in one line so the
opening of every session states the distance to done in database terms.

## Review state — `review_db.py state <review> [--log]`

One console dashboard, entirely from the mirror, **repeatable**: the same
files render the same text (sorted, no timestamps in the body), so two
renders can be diffed. Sections: header (decision, report status, runs,
findings, task verdicts); the definition of done with bars; POUR
(criteria / decided / evidenced / failing); 508 FPC (views done,
answered, blank, fails); views × modalities with the latest run's Result
as a glyph and an axe column; findings by severity; vendor claim vs
verified (worse / better / as claimed); integrity counts; and "what
moves the needle" — the 05 decisions waiting on measured fails, the
unanswered rows by modality, task walks without a verdict, FPC never
exercised. `--json` gives the same data for tooling.

`--log` appends one row to **`reviews/<id>/state-log.md`** (date, done,
C1–C12, runs, findings, integrity) and prints the delta since the previous
row. The log is append-only and idempotent — an unchanged state adds no
row — so the review's progress is the diff between rows, versioned with
the review. Open every session with it; log again at the end.

## The dashboard page — `scripts/dashboard.py <review> [--open]`

`reviews/<id>/<id>-dashboard.html` is the reviewer's map of the review,
built from the database. It answers three questions, in this order
(redesigned 2026-09-15 at the reviewer's request — the first version "was
very cluttered and didn't tell me what I need to know"):

1. **508 FPC — did we test every view for each modality?** One row per
   functional performance criterion (302.1 … 302.9, one row per modality):
   views tested / views sampled as a bar, check rows answered / blank /
   failing, and the **views still owed** by name (linked to the run when
   one is logged without a Result, "not run" otherwise). A view counts as
   tested for a modality when its latest run under that modality has a
   Result (Works / Works with issues / Broken / N/A).
2. **Views — what are we tracking, and is each one complete?** One row per
   sampled view (03 §3.1): the page in words (linked to its locator), the
   sweep run with its triage count (W1–W3 answered), one cell per modality
   with the latest run's Result as a glyph (blank-row count on a run with
   no Result), **done n/8** — seven modality cells with a Result plus a
   triaged sweep — and the live findings recorded on the view.
3. **WCAG 2.2 AA — what passes and what fails?** Headline counts (passing
   = Supports; failing = Partially Supports or Does Not Support; not
   applicable; undecided, split into *decision needed* — a failing check
   row with no `05` outcome — *undecided with evidence*, and *untested*),
   then per principle a table of the 55 criteria: outcome (with
   "(provisional)" when the `05` remark says so), the findings rolled up
   under it, the check evidence (answered / failing rows), and the
   vendor's claim with worse / same / better.

Then **Next** — pending walkthrough steps, `05` decisions waiting on a
failing check, task walks without a verdict — and, folded under
`<details>`, the definition of done, the findings table, the vendor
delta, integrity, runs with blank rows and the state-log history. Every
run, step and stage file is a relative link. The console `state` command
keeps its own denser layout; the page is for orientation, `state` for
the session log.

Rules: it is **derived from the database exactly as the database is derived
from the files** — `review_db.py sync` regenerates it (so `validate`,
`status`, `coverage`, `log-test` and the probe all keep it current), it
carries no timestamp (the header shows the source hash) so a diff on the
committed page means the review changed, and it is never hand-edited.
Colour never carries meaning alone: every status has a glyph and a word,
and a hover title spells out what the cell holds. Regular Chrome cannot
open `file://` pages through the browser extension; `--open` uses the
default browser, or serve the folder (`python -m http.server`) when a
screenshot is needed.

## Integrity checks — `review_db.py check <review>` (the `[db]` lines of `validate`, and C11)

| Check | What it catches |
|---|---|
| outcome without check evidence | a `05` Outcome with no answered check behind it |
| failed check, 05 undecided | fail/partial check on a criterion still Not Evaluated |
| finding not rolled up | a live finding names a criterion whose `05` block does not cite it |
| 05 cites unknown / withdrawn finding | rollup pointing at nothing, or at a withdrawn finding |
| Supports despite live finding | `05` Supports / N-A on a criterion a live finding fails |
| finding cites missing run / no run | evidence trail broken |
| finding cites unknown criterion | typo or out-of-target criterion |
| Result set with blank checks / Works with a failed check | run Result contradicts its own rows |
| run on unsampled view | a run for a view that is not in `03` |
| unrecognised check outcome | outcome cell outside pass/fail/partial/n/a |

## Verifying with SQL

Before asserting a count, a cross-reference ("V-F3 is rolled up under
2.4.4"), a comparison ("worse than the vendor claimed on N criteria"), or a
coverage figure, run the query — `review_db.py query --review <id> "…"`
(read-only; `--review` or `--all` is required even when the SQL names the
review — the database is per review and the command has to know which
file to open. `--json` for tooling).

    -- vendor claim vs verified outcome, where they differ
    SELECT sc, vendor_claim, outcome FROM criterion_outcomes
    WHERE review_id = '2026-09-the-expert-ta' AND outcome <> 'Not Evaluated'
      AND vendor_claim NOT LIKE outcome || '%';

    -- every measured fail awaiting confirmation, with its evidence
    SELECT run_id, check_id, note FROM check_outcomes
    WHERE review_id = '2026-09-the-expert-ta' AND outcome = 'fail' AND note LIKE '%measured%';

    -- probe facts: which views have a fixed-width layout at 320 px
    SELECT run_id, json_extract(value, '$.reflow_scrollWidth') AS w FROM measurements
    WHERE kind = 'probe' AND key = 'summary' AND review_id = '2026-09-the-expert-ta';

    -- axe rules that fired on the most views
    SELECT key, COUNT(*) AS runs FROM measurements
    WHERE review_id = '2026-09-the-expert-ta' AND kind = 'axe' AND key LIKE 'violations:%'
    GROUP BY key ORDER BY runs DESC;

## Rules

- **Never hand-edit the DB.** It is rebuilt; edits vanish. Fix the file, re-sync.
- **Never make a review "complete" in prose.** Completion is C1–C12.
- **Parsing is the contract.** The extraction table above and
  `review_db.py` change together.
- **Tool-originated data** (probe, axe) goes into `measurements` as JSON so
  the schema does not churn per instrument.
- **Phase 2 (open, the reviewer's call):** write check outcomes, run Results
  and `05` outcomes to the DB first and generate the markdown tables from it.
  The schema supports it; only the write path changes.
