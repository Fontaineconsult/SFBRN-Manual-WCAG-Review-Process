# Test Run R100 — S4

| | |
|---|---|
| **Run ID** | R100 |
| **Date/time** | 2026-09-11 15:55 |
| **View / sample** | S4 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — NC1, NC3 need the reviewer — judge from `R100-grayscale.png` (achromatopsia emulation) or the OS filter; measured fail on NC2 awaits confirmation |

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | | |
| NC2 — Links are distinguishable from surrounding text without color | fail | O2 — 2 of 5 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 |
| NC3 — Everything remains operable and understandable in grayscale | | |

**view_probe 2026-09-11:** answered NC2=fail by measurement; facts in `R100-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 2 of 5 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R100-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
