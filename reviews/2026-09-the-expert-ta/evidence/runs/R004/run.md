# Test Run R004 — S3

| | |
|---|---|
| **Run ID** | R004 |
| **Date/time** | 2026-09-10 10:46 |
| **View / sample** | S3 |
| **Page URL / location** | UI: Class Management → assignment row → Take Assignment (Problem 9 active) |
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
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O9 recorded (Problem 9 state) plus O10–O13 from the three extra-state scans; reviewer to confirm/dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O14 (problem-navigator link contrast 4.35:1 on #F5F5F5, 24 nodes) → low-vision run, eyedropper; O15 (`detailed view` link-in-text-block) → no-color run; P1 state: `empty-table-header` ×5 on the force table → no-vision run (are the FBD table headers announced?) |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of S3: axe sees 0 headings / 0 landmarks; MathML is present (MathMLMath nodes) — axe does not inspect MathML content, so the math read-out is JAWS-only |

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

- O1 [new] (state: Take Assignment, Problem 9 multiple choice active): axe `label` (critical) — all five `input type=radio name="choicegroup"` answer options have no label/title/ARIA name. Matches the exploration AX-tree probe (5 unnamed radios on P9, 6 on P8). The option text (MathJax + text) sits in adjacent cells.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / **Blocker for no-vision on multiple-choice parts** — a screen-reader user cannot tell which radio is which — confirm with JAWS on P8/P9 → finding
- O2 [new] (state: as O1): axe `html-has-lang` (serious) — `<html>` has no `lang` (Class Management has `lang="en"`; this page and several others do not).
  - Proposed: W1 / WCAG 3.1.1 (A) / Minor — product-wide inconsistency; confirm → one finding listing the affected views (S3, S7, S11)
- O3 [new] (state: as O1): axe `image-alt` (critical) — `img src="https://cdn.theexpertta.com/ai/cmt/sig.gif?tid=…"` 0×1 px tracking/signature images with no alt (2 on P9; up to 5 on P1). Invisible; decorative.
  - Proposed: W1 / WCAG 1.1.1 (A) / Minor — confirm whether JAWS announces "graphic sig" inside the problem statement; if silent, dismiss as no user impact but still a technical failure
- O4 [new] (state: as O1): axe `color-contrast` (serious), opaque white background resolved: hint/feedback/submission deduction percentages "4%", "5%", "25" in `#FF9900` on white = **2.14:1** at 13 px.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major (these numbers tell the student what a hint costs) — confirm by eyedropper → finding
- O5 [new] (state: as O1): `aria-command-name` — 4 unnamed jump-point buttons on this view (top of page, problems, problem statement, current part) (PW-B).
  - Proposed: fold into the PW-B finding after the JAWS run establishes what is announced on focus
- O6 [new] (state: as O1): `region` — 17 content nodes outside landmarks incl. `#probSelectorsList` (the problem navigator) (PW-D).
  - Proposed: fold into structure finding
- O7 [new] (state: as O1): no `select-name`/`button-name` violations — Submit / Hint / Feedback / I give up carry `title`s that axe accepts as names; problem-navigator links carry `aria-label="Problem N Click To Activate"`.
  - dismissed: informational (names exist; whether "Click To Activate" is a good name is a JAWS-run judgement)
- O8 [new] (state: as O1): passes 31 / inapplicable 52 in `R004-axe.json`.
  - dismissed: informational
- O9 [new] (state: as O1): the `#calc-announce` live region and `role=alert` container produce no axe output (no `aria-prohibited-attr`, no `aria-allowed-role`) — their behaviour is a JAWS question (4.1.3).
  - Proposed: route to no-vision run on S3
- O10 [new] (state: Problem 1 — free-body diagram + equation parts, `R004-axe-p1-fbd-equation.json`): `color-contrast` ×9 — randomized-variable values (`span.variable`, `#FF6347` "tomato" on white = **2.94:1**, on #F5F5F5 = 2.70:1) at 12 px bold; part identifiers "Part (b)/(c)/(d)" (`#3A7C89` on #F5F5F5, 4.35:1 — below 4.5:1); deduction percentages (2.14:1). Also `aria-command-name` ×7 (one jump point per part) and `image-alt` ×5 (sig.gif).
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major — the red variable values are the numbers a student must use in the calculation — confirm by eyedropper → finding (same colour token appears on S4 and S8)
- O11 [new] (state: Problem 1): **incomplete** `empty-table-header` ×5 on the FBD force table (`#forceHeader` "Force Name", "Angle", "Adjust Angle", "Adjust Length", "Delete") — axe considers the header text possibly empty because of how the cells are built.
  - Proposed: W2 → no-vision run on S3 P1: does JAWS read the column headers in the force table?
- O12 [new] (state: Problem 3 — drag-and-drop ranking, `R004-axe-p3-dragdrop.json`): 8 rule violations, all product-wide (PW-A…D) plus `image-alt` ×2 (sig.gif) and `color-contrast` ×2 (deduction percentages). **axe reports nothing about the draggable cards themselves** — their four `img`s had empty alt in exploration (decorative per axe) although each card is the answer content (a labelled block diagram).
  - Proposed: route to the no-vision run: what does JAWS announce for each draggable card, and does the Ctrl+Shift+3 "unmatched items" read-out substitute for image alt? (1.1.1 / 4.1.2)
- O13 [new] (state: Problem 4 — numeric parts with keypad, `R004-axe-p4-numeric-keypad.json`): 8 rule violations, product-wide plus `image-alt` ×3 (sig.gif) and `color-contrast` ×4. The ~45 keypad `<button>`s are **not** flagged (they have text or titles).
  - Proposed: keypad tab-order question stays with the motor run (see 03 §2.6)
- O14 [new] (state: all four states): **incomplete** `color-contrast` ×20–25 — mostly the nine problem-navigator links (`#3A7C89` on `#F5F5F5` = **4.35:1**, computed but flagged incomplete because of overlap) and MathJax glyphs (`nonBmp`, `shortTextContent`).
  - Proposed: W2 → low-vision run: eyedropper the navigator links (likely a real 1.4.3 miss by a small margin) and one MathJax expression
- O15 [new] (state: all states): **incomplete** `link-in-text-block` — the "detailed view" link in the submission-history line.
  - Proposed: W2 → no-color run on S3

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset. Four scans of the same URL in different states: the run's scan (17:46 UTC) with Problem 9 active, then ad-hoc scans with Problem 1 (FBD + equation), Problem 3 (drag-and-drop) and Problem 4 (numeric + keypad) active, saved beside it. Counts — P9: violations 9 / incomplete 2 / passes 31; P1: 7 / 5 / 28; P3: 8 / 2 / 32; P4: 8 / 2 / 33.
Problems were switched with the app's own `ETAProbNav.clickProblem()`; no answer was entered or submitted; submissions remaining unchanged (5 on P9).
Contrast numbers quoted come with an opaque ancestor background resolved (reliable per testing-tools.md); everything reported as 0 / bgImage / nonBmp is unmeasured.

## Evidence files in this folder

- `R004-axe.json` — Problem 9 (multiple choice) state, the run's scan
- `R004-axe-p1-fbd-equation.json` — Problem 1 state (ad-hoc)
- `R004-axe-p3-dragdrop.json` — Problem 3 state (ad-hoc)
- `R004-axe-p4-numeric-keypad.json` — Problem 4 state (ad-hoc)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
