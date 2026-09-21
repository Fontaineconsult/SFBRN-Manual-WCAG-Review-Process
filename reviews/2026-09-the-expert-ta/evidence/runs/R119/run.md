# Test Run R119 — S13

| | |
|---|---|
| **Run ID** | R119 |
| **Date/time** | 2026-09-15 13:07 |
| **View / sample** | S13 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-21. Broken for this modality by the reviewer's same-styles ruling, applied after measurement: this page carries the randomised values in #FF6347 ten times over, the same token and the same job as on Take Assignment (R109) and View Assignment Solutions (R110), both of which the reviewer failed. Since this page is the candidate conforming-alternate route for *reading* an assignment, the failure matters twice over.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | fail | O3 — the view paints the randomised variable values in **#FF6347 ×10** ("25", "13", "9.5") — the identical token and identical use the reviewer failed on Take Assignment and View Assignment Solutions; applied under the reviewer's ruling 2026-09-21 — "the styles are the same across the app, if the other views use the same colors lets assume they also fail" — after **measuring** which tokens this view actually uses (the ruling is a conditional; the antecedent is established, not assumed) |
| NC2 — Links are distinguishable from surrounding text without color | fail | O2 — 2 of 2 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: Class: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373 [1:1 vs text; hover cue: a:hover; focus: none]; Assignment: Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 [1:1 vs text; hover cue: a:hover; focus: none] |
| NC3 — Everything remains operable and understandable in grayscale | fail | O3 — a student cannot tell which numbers in the printable problems are their randomised values with colour removed, exactly as on Take Assignment |

**view_probe 2026-09-15:** answered NC2=fail by measurement; facts in `R119-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-15 view_probe): 2 of 2 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: Class: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373 [1:1 vs text; hover cue: a:hover; focus: none]; Assignment: Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 [1:1 vs text; hover cue: a:hover; focus: none]
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [clarified] (state: View Printable Assignment as loaded, 2026-09-21 — measured colour-token scan, applying the reviewer's same-styles ruling from W32): the page uses **`#FF6347` on 10 elements**, and the sample text is the randomised values themselves — "25", "13", "9.5". That is the same token, in the same role, that the reviewer failed on S3 and S8. It also carries pure red (`rgb(255,0,0)`) on 8 elements. Measured, not assumed: the scan enumerates every visible text colour on the view and matches it against the tokens failed on 2026-09-21.
  - Classified: NC1, NC3 / WCAG 1.4.1 / Major → **V-F31** (this view added by the same-styles ruling)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R119-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
