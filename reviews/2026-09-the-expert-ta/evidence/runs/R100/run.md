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
| **Result** | Broken |

**Result reasoning.** 2026-09-21. Broken for this modality. This is the page where a student finds out what they scored and why, and two of the things it explains are carried by colour alone: which of the two deductions each number in the grade formula belongs to, and which submissions were late. The reviewer confirms every coloured text on the page fails in grayscale except the dark blue [?] links, and adds that the images fail too. A student who cannot use colour can read the total but cannot check how it was arrived at.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | fail | O6, O7 — two carriers are colour-only: in the grade formula the two deduction types are told apart **only** by orange vs purple, and individual late submissions **only** by a red date-time (the page's own legend says so). The per-part lateness sentence and the labelled deduction rows do carry words — partial credit where it is due |
| NC2 — Links are distinguishable from surrounding text without color | fail | O4 — 2 of 2 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373 [1:1 vs text; hover cue: a:hover; focus: outline]; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 [1:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O8 — reviewer 2026-09-21: "the colored text fails contrast in grey, except the dark blue, that passes", and "the images used also fail contrast in some ways when in grey" |

**view_probe 2026-09-11:** answered NC2=fail by measurement; facts in `R100-probe.json`.

**view_probe 2026-09-14:** answered NC2=fail by measurement; facts in `R100-probe.json`.

**view_probe 2026-09-14:** answered NC2=fail by measurement; facts in `R100-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 2 of 5 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [measured] (state: view as loaded, 2026-09-14 view_probe): 2 of 5 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373 [1:1 vs text; hover cue: a:hover; focus: outline]; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 [1:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O4 [measured] (state: view as loaded, 2026-09-14 view_probe): 2 of 2 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: Testing Course for CSU East Bay → GradeSheetClassAssignments.aspx?eid=3373 [1:1 vs text; hover cue: a:hover; focus: outline]; Chapter 5 Sample Assignment → GradeSheetClassAssignmentProblems.aspx?eid=3373&aid=17547 [1:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O5 [measured] (state: View Grade Report as loaded, 2026-09-21 — colour-token scan, `evidence/colour-token-scan-2026-09-21.json`): **the page is not empty.** It renders **1120 text-bearing elements in 11 distinct text colours**, and four of them are colour-coded in ways W32 asked about: `rgb(255,165,0)` orange on **66** elements whose text is "%", `rgb(128,0,128)` purple on **66** more, also "%", `rgb(255,0,0)` red on **48**, sample text *"Late submissions were made on this part"*, and `rgb(0,0,255)` blue on **44**, the **[?]** links. It also carries `#FF6347` on 10 elements. Two observations follow. First, lateness **is stated in words** here — the red run is a sentence, not just a red date — which is the opposite of what the 2026-09-10 note predicted and may make that part of NC1 a pass. Second, **two different colours, orange and purple, both sit on "%"** in equal numbers, which looks like two meanings distinguished by colour alone; that would be a 1.4.1 failure, and no wording in the scan distinguishes them.
  - Classified: NC1, NC3 — **still open**, deliberately. This is a measurement, not a judgement, and the two questions it raises need eyes → W74. It also qualifies the "no grades to view" limitation: whatever is missing from the demo account, this page is not blank and its colour coding is testable

- O6 [measured] (state: View Grade Report as loaded, 2026-09-21 — element inspection following O5): the two "%" colours are two **different deduction types**. Orange (`rgb(255,165,0)`) is *"Deduction for Final Submission"*; purple (`rgb(128,0,128)`) is *"Deductions for Incorrect Submissions, Hints and Feedback"*. In the labelled rows each is next to its name, so the words carry it. **In the summary line they are not**: `Student Grade = 100 - 100 - 9 = 0%` renders the first 100 in orange and the 9 in purple, and nothing but that colour says which deduction each number is. Neither carries a `title` or `aria-label`; there is no legend for them anywhere on the page.
  - Classified: NC1 / WCAG 1.4.1 / Major → **V-F31** (the grade formula is the clearest colour-only case found in the review — two numbers, one sentence, told apart by hue alone)
- O7 [measured] (state: as O6): lateness is carried **two ways, one of which is colour-only**. At part level a red sentence states it in words — *"Late submissions were made on this part and a late work deduction may have been applied."* (25 such elements), which is not colour-dependent. At individual-submission level, 14 red date-times mark which submissions were late, and the page's own legend confirms the mechanism: **"Red submission date times indicate late work."** A legend naming a colour does not rescue 1.4.1 — a user who cannot see red still cannot tell which dates it applies to. The 2026-09-10 prediction that lateness is conveyed by red alone was therefore half right, and the half that is wrong is worth reporting: the per-part sentence is the pattern the date-times should copy.
  - Classified: NC1 / WCAG 1.4.1 / Major → **V-F31**; the per-part sentence recorded as a **pass** and as the in-product fix
- O8 [clarified] (state: View Grade Report under a grayscale filter, reviewer, 2026-09-21 — step W74): *"in GradeSheetGradeReport the colored text fails contrast in grey, except the dark blue, that passes"*, and *"it should also be pointed out that the images used also fail contrast in some ways when in grey."* So of the five colours on the page the orange, purple, red and `#FF6347` runs all fail with colour removed, and only the blue **[?]** links survive. The images failing in grayscale is a new observation and applies beyond this view → recorded against V-F24.
  - Classified: NC3 / WCAG 1.4.3 in grayscale / fail → the contrast half stays under **V-F23**; the blue [?] links pass and are recorded as the exception

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R100-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
