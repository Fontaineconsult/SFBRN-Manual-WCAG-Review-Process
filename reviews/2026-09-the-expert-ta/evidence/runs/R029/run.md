# Test Run R029 — S4

| | |
|---|---|
| **Run ID** | R029 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S4 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W57/W21) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-21, every row answered. The reviewer's own split decides it: the page is **"probably navigable with concerted effort"**, but its content is **"fully not accessible for purpose"**. Navigation and substance come apart here. The purpose of this page is to show a student their detailed work and how the grade was reached; the work itself is 16 unlabelled images inside the table cells (O8), and the arithmetic that explains the grade distinguishes its two deductions by colour alone (O10). A screen-reader user can move around the page and still not learn either thing. Broken.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "View Grade Report (Shows your detail work)" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O5 — no headings, no landmarks. The product substitutes a custom tab region for them, and the reviewer's verdict on the substitute is that it does not do the job: "without headings there is no way to jump between problems" → V-F1, V-F8 |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O5, O6, O7 — "no buttons have labels"; the 22 **[?]** help links announce only "Visited Link"; and an **unlabelled button sits at the end of every problem area**, which on Enter opens the next problem's hidden menu → V-F8, V-F33 |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O8 — "none of the graphics are presented as graphics and no alt text". Measured: 20 images, **all inside table cells**, 16 of them with no alt → V-F34 |
| NV5 — Reading order matches the meaning of the visual order | pass | O5 — the reviewer describes entering a problem and arrowing through it to its end without reporting anything out of sequence; the unlabelled control they meet there is a naming defect (NV3), not an ordering one |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | n/a | O9 — measured 2026-09-21: the view has **no visible input, select or textarea**. It is a read-only report; there are no form fields to label |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | partial | O6 — the dynamic updates do work and are usable: Enter in the custom tab region opens the "accessibility menu" offering tab options into a specific problem, and the end-of-problem button opens the next problem's menu. What the narration does not settle is whether NVDA **announces** the menu's appearance — the one open question on this view |
| NV8 — Nothing is conveyed only by visual position, shape, or size | fail | O10 — the grade formula `Student Grade = 100 - 100 - 9 = 0%` distinguishes its two deduction types **only by colour** (R100 O6), which a screen reader cannot convey at all: the numbers are read out with nothing to say which deduction each one is → V-F31 seen from the no-vision side |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | fail | O7 — measured and heard agree: **22** help links whose entire text is `[?]`, all pointing to the same page, none carrying `title` or `aria-label`. Punctuation is not spoken, so the accessible name is effectively empty and NVDA falls back to "Visited Link" → V-F33 |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O9 — measured 2026-09-21: no form fields at all on the view, so there is no validated input to submit |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R029-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "View Grade Report (Shows your detail work)" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

- O5 [clarified] (state: View Grade Report, NVDA, reviewer 2026-09-21 — step W57/W21): **"no buttons have labels, there are no headings or landmarks. Tabbing has a custom feature that is attempting to replace headings, but without headings there is no way to jump between problems."** The vendor's jump-point pattern is on this page at its densest (axe counted 32, one per problem and part) and the reviewer's judgement of it is explicit: **"help or noise, more noise than help"** — though **"with concerted effort the page is probably navigable."**
  - Classified: NV2 / WCAG 1.3.1, 2.4.1 / Major → V-F1 and V-F8 on this view; NV3 / 4.1.2 / Major → V-F8
- O6 [clarified] (state: as O5): **"pressing enter when in the custom tab region will open the 'accessibility menu' which gives other tab options to enter into the specific problem. A side effect is that when we enter a problem then arrow through it, at the end of the problem area we hit an unlabeled button, which on enter opens the next problem's hidden accessibility menu."** So the mechanism does work — it is the only way to move between problems — but it is built out of controls with no names, and reaching the next problem means arrowing to the end of the current one and pressing Enter on something that announces nothing.
  - Classified: NV3 / WCAG 4.1.2 / Major → V-F8; NV7 / partial — the update is usable, but whether its appearance is announced is not established
- O7 [clarified + measured] (state: as O5): **"[?] are all unlabled and announce only Visited Link."** Measured the same day: **22** links whose entire text content is `[?]`, every one pointing at `blog.theexpertta.com/hints-and-feedback`, none with `title` or `aria-label`. Punctuation is not spoken, so the computed name is empty and the screen reader has only the visited state left to announce. A user cannot tell what help is on offer, or that all 22 lead to the same page.
  - Classified: NV3, NV10 / WCAG 2.4.4, 4.1.2 / Major → finding **V-F33**
- O8 [clarified + measured] (state: as O5): **"none of the graphics are presented as graphics and no alt text … Tables have headings, however the tables contain images in the cells which have no alt text and are therefore fully not accessible for purpose."** Measured: **20 images on the view, every one of them inside a table cell, and 16 carry no alt** (`/images/bz41ko5n.52q.png` and similar — the per-problem rendering of the student's own submitted work). The table structure is sound — the reviewer confirms the headers — but the cells the headers lead to are empty to a screen reader.
  - Classified: NV4 / WCAG 1.1.1 / **Blocker for this view's purpose** → finding **V-F34**
- O9 [measured] (state: as loaded, 2026-09-21): the view has **no visible input, select or textarea** — it is a read-only report.
  - Classified: NV6 / n/a; NV12 / n/a
- O10 [measured] (state: as loaded, cross-referenced from the no-color run R100 O6): the grade formula `Student Grade = 100 - 100 - 9 = 0%` marks its two deduction types by colour alone — orange for "Deduction for Final Submission", purple for "Deductions for Incorrect Submissions, Hints and Feedback". A screen reader conveys no colour, so it reads three bare numbers with nothing to say which deduction each is. The same defect that fails 1.4.1 for a colour-blind user (V-F31) removes the explanation entirely for a screen-reader user.
  - Classified: NV8 / WCAG 1.3.1 / Major → **V-F31** (recorded here as its no-vision consequence)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R029-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
