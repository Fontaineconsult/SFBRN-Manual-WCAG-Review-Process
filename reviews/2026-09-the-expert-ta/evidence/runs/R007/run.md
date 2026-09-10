# Test Run R007 — S4

| | |
|---|---|
| **Run ID** | R007 |
| **Date/time** | 2026-09-10 10:47 |
| **View / sample** | S4 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 153 debug profile); classification pending reviewer |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O5 recorded; reviewer to confirm/dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O6 (99 contrast incompletes, mostly SVG diagram text) → low-vision eyedropper on one FBD label; O7 (`link-in-text-block` ×22 — the blue [?] help links) → no-color run; O8 (`th-has-data-cells` ×22) → no-vision run: are the per-part tables real data tables? |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of the grade report (P5) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

Product-wide items seen on every signed-in view (first recorded in R001; not repeated as separate observations here, but they apply to this view too):
- **PW-A** DevExpress editors without labels (`label` critical) — see R001 O1.
- **PW-B** the vendor's `focus-box` jump points are `div role="button" tabindex="0"` with no accessible name (`aria-command-name` serious) — see R001 O2. The count grows with content (4 on Take Assignment, 32 on the grade report, 33 on the solutions page — one per problem and part).
- **PW-C** header logo link is `aria-hidden="true"` yet focusable (`aria-hidden-focus`) — see R001 O3.
- **PW-D** no `main`, no landmarks, no `h1` (best-practice rules `landmark-one-main`, `region`, `page-has-heading-one`) — see R001 O5/O6; fold into the structure finding from the JAWS run.
- **PW-E** `bypass` incomplete — whether the jump points count as a bypass mechanism is settled once, in the no-vision run on S1.
- **PW-F** DevExpress buttons paint their background with an image, so axe reports their captions as contrast 0 = **unmeasured** (`bgImage`) — eyedropper in the low-vision run; never a finding from axe alone.
- **PW-G** DevExpress check boxes / list boxes carry a hidden `input type=text readonly style="opacity:0"` state field (`_S` / `_KBS` ids) that axe flags under `label`. Whether it is focusable (and therefore a real unlabeled stop) is a keyboard-run question; propose treating it as one issue product-wide, not per field.

- O1 [new] (state: View Grade Report for "Chapter 5 Sample Assignment", instructor's own (empty) attempt — all 9 problems expanded): axe `aria-command-name` **×32** — one unnamed jump-point button per problem and per part (PW-B at scale).
  - Proposed: fold into the PW-B finding; note this is the view where a screen-reader user meets 32 nameless buttons in a row
- O2 [new] (state: as O1): `color-contrast` **×62** — randomized-variable values (`#FF6347` on white, **2.94:1**, 16 px bold) repeated per problem; the grey italic "All Date times are displayed in Pacific Standard Time." (`#808080`, **3.94:1**); the red italic "Red submission date times indicate late work." (`#FF0000`, **3.99:1**) — the latter also signals lateness by colour alone.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major — same variable-colour token as R004 O10; add this view. Separately route "red = late" to the no-color run (1.4.1)
- O3 [new] (state: as O1): `image-alt` ×9 — one `sig.gif` tracking pixel per problem (see R004 O3).
  - Proposed: same disposition as R004 O3
- O4 [new] (state: as O1): `aria-hidden-focus` ×1, `region` ×18, `landmark-one-main`, `page-has-heading-one` (PW-C/D).
  - Proposed: fold into product-wide findings
- O5 [new] (state: as O1): passes 31 / inapplicable 54; raw JSON is 2.7 MB because every problem's statement, figure SVG and part tables are on one page.
  - dismissed: informational
- O6 [new] (state: as O1): **incomplete** `color-contrast` ×99 — SVG `tspan` labels inside the FBD diagrams (F, θ, total,x …) and MathJax glyphs; axe cannot measure text over SVG.
  - Proposed: W2 → low-vision run: eyedropper two diagram labels
- O7 [new] (state: as O1): **incomplete** `link-in-text-block` ×22 — the blue bold "[?]" help links (to blog.theexpertta.com/hints-and-feedback) inside table text.
  - Proposed: W2 → no-color run on S4 (1.4.1): bold + colour, no underline?
- O8 [new] (state: as O1): **incomplete** `th-has-data-cells` ×22 — per-part submission tables whose `th`s may have no data cells (empty attempt history).
  - Proposed: W2 → no-vision run on S4 after the reviewer has submitted at least one answer (P2), so the tables have rows

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:48 UTC. Counts: violations 7 (62 contrast nodes, 32 unnamed commands), incomplete 3, passes 31, inapplicable 54. Direct URL with `eid`/`aid`; valid with a live session.
The report is for the instructor account's own attempt, which has no submissions — tables are empty; re-scan after P2 produces a submission.

## Evidence files in this folder

- `R007-axe.json` — raw axe output (2,677,211 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
