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
| **Result** | Works with issues |

**Result reasoning.** 2026-09-17, triage closed. Every axe violation is now a confirmed finding (V-F1, V-F8, V-F9, V-F11, V-F14, V-F18, V-F23) or dismissed with a written reason, and every `incomplete` is answered by the run it was routed to. "Works with issues" describes the **sweep**, not the page — the page is Broken without vision (R017). The sweep penetrated for HTML structure (W3), but it is blind to the two things that decide this view: MathML content and the answer widgets' behaviour. Both were settled by the reviewer's NVDA walk, not by axe.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O1–O13, closed 2026-09-17 against the walks that have since happened: O1→V-F11, O2→V-F18, O4/O10→V-F23, O5→V-F8, O6→V-F1, O9→V-F9, O12→V-F14 (all confirmed by the reviewer on R017/R083); O3 dismissed (announced to nobody — R017 O8); O7, O8 dismissed as informational; O13 routed to the motor run (R018) |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | All three routed and answered. O14 (navigator link contrast) → low-vision R083 O9, folded into **V-F23**; O15 (`detailed view` link-in-text-block) → no-color R109, **n/a** — the link is not inside running text (re-measured 2026-09-14 under the G183 rule); O11 (`empty-table-header` ×5 on the force table) → no-vision R017 O20, **dismissed: the headers are announced in use** and the reviewer calls the force-table read-back "quite robust" |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | Cross-checked 2026-09-10 against the **NVDA** walk (R017 — the reviewer's own AT; no JAWS walk of S3 exists): axe sees 0 headings / 0 landmarks and NVDA finds none either (R017 O1), so the structure output stands. Recorded blind spots, not counted as passes: axe does not inspect **MathML** content (the math read-out is AT-only — R017 O7, V-F9) and reports nothing about the **answer widgets' behaviour** (drag-and-drop placements V-F14, hint insertion V-F15 — all AT-only). Zero axe findings on those is not evidence |

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
  - Classified: W1 / WCAG 1.3.1, 4.1.2 / Major, **Blocker for parts whose options contain math** → **V-F11**, confirmed 2026-09-10 by the reviewer's NVDA walk (R017 O6/O9: the radios carry no name and an option is identified only by its table position, "row 4 table 1")
- O2 [new] (state: as O1): axe `html-has-lang` (serious) — `<html>` has no `lang` (Class Management has `lang="en"`; this page and several others do not).
  - Classified: W1 / WCAG 3.1.1 / Minor → **V-F18**, recorded 2026-09-14 on the reviewer's delegation ("your call"); one finding lists all three affected views (S3, S7, S11) against the eleven that declare `en`
- O3 [new] (state: as O1): axe `image-alt` (critical) — `img src="https://cdn.theexpertta.com/ai/cmt/sig.gif?tid=…"` 0×1 px tracking/signature images with no alt (2 on P9; up to 5 on P1). Invisible; decorative.
  - dismissed 2026-09-17: **announced to nobody**. The condition the proposal set was met — R017 O8 reports that `G` (next graphic) finds **no** graphic anywhere on the view, so the 0×1 px `sig.gif` tracking images are silent to the screen reader. A technical 1.1.1 failure with no user impact; not raised. (The real 1.1.1 defect on this view is the opposite case — the informative problem figure that is also hidden, V-F24/R017 O8.)
- O4 [new] (state: as O1): axe `color-contrast` (serious), opaque white background resolved: hint/feedback/submission deduction percentages "4%", "5%", "25" in `#FF9900` on white = **2.14:1** at 13 px.
  - Classified: W1 / WCAG 1.4.3 / Major → **V-F23**, confirmed 2026-09-15 (R083 O9: the reviewer's low-vision pass carries the deduction percentages at 2.14:1 under V-F23)
- O5 [new] (state: as O1): `aria-command-name` — 4 unnamed jump-point buttons on this view (top of page, problems, problem statement, current part) (PW-B).
  - Classified: W1 / WCAG 4.1.2 → folded into **V-F8**, confirmed 2026-09-10 (R017 O2: the jump point announces its instruction text, not a control name)
- O6 [new] (state: as O1): `region` — 17 content nodes outside landmarks incl. `#probSelectorsList` (the problem navigator) (PW-D).
  - Classified: W1 / WCAG 1.3.1 supporting evidence → folded into **V-F1**, confirmed 2026-09-10 (R017 O1: no headings, and after activating a problem there is no structural route to it)
- O7 [new] (state: as O1): no `select-name`/`button-name` violations — Submit / Hint / Feedback / I give up carry `title`s that axe accepts as names; problem-navigator links carry `aria-label="Problem N Click To Activate"`.
  - dismissed: informational (names exist; whether "Click To Activate" is a good name is a JAWS-run judgement)
- O8 [new] (state: as O1): passes 31 / inapplicable 52 in `R004-axe.json`.
  - dismissed: informational
- O9 [new] (state: as O1): the `#calc-announce` live region and `role=alert` container produce no axe output (no `aria-prohibited-attr`, no `aria-allowed-role`) — their behaviour is a JAWS question (4.1.3).
  - Classified: routed and answered → R017 O3/O4. `Ctrl+Shift+5` works; `Ctrl+Shift+2` reads raw MathJax markup for math answers → **V-F9**. The live region's behaviour was an AT question and axe was right to say nothing
- O10 [new] (state: Problem 1 — free-body diagram + equation parts, `R004-axe-p1-fbd-equation.json`): `color-contrast` ×9 — randomized-variable values (`span.variable`, `#FF6347` "tomato" on white = **2.94:1**, on #F5F5F5 = 2.70:1) at 12 px bold; part identifiers "Part (b)/(c)/(d)" (`#3A7C89` on #F5F5F5, 4.35:1 — below 4.5:1); deduction percentages (2.14:1). Also `aria-command-name` ×7 (one jump point per part) and `image-alt` ×5 (sig.gif).
  - Classified: W1 / WCAG 1.4.3 / Major → **V-F23**, confirmed 2026-09-15 (R083 O9 carries the red variable values at 2.94:1 and the navigator numbers at 4.35:1 under V-F23; the same colour token on S4 and S8 is covered by the same finding)
- O11 [new] (state: Problem 1): **incomplete** `empty-table-header` ×5 on the FBD force table (`#forceHeader` "Force Name", "Angle", "Adjust Angle", "Adjust Length", "Delete") — axe considers the header text possibly empty because of how the cells are built.
  - dismissed 2026-09-17 → **R017 O20**: with NVDA and keyboard only, Add Force, setting angle and length **through the force table**, the `Ctrl+Shift+3` read-back and Submit all succeeded — the headers are announced in use. axe's `empty-table-header` was an artefact of how the cells are built
- O12 [new] (state: Problem 3 — drag-and-drop ranking, `R004-axe-p3-dragdrop.json`): 8 rule violations, all product-wide (PW-A…D) plus `image-alt` ×2 (sig.gif) and `color-contrast` ×2 (deduction percentages). **axe reports nothing about the draggable cards themselves** — their four `img`s had empty alt in exploration (decorative per axe) although each card is the answer content (a labelled block diagram).
  - Classified: routed and answered → **V-F14** (R017 O19: placements are not announced; Minor, "not unusable" — reviewer). On the alt question: R017 O18 found the accessible alternative form, whose Item picker options **are** text descriptions of the cards, so the card content is available by another route and the empty alt on the visual cards is not raised separately
- O13 [new] (state: Problem 4 — numeric parts with keypad, `R004-axe-p4-numeric-keypad.json`): 8 rule violations, product-wide plus `image-alt` ×3 (sig.gif) and `color-contrast` ×4. The ~45 keypad `<button>`s are **not** flagged (they have text or titles).
  - Classified: routed → motor run **R018** (10 of 11 rows answered). R017 O20–O21 record every widget on this view — symbol palette, keypad, drag-and-drop alternative form, free-body diagram — as operable without a mouse
- O14 [new] (state: all four states): **incomplete** `color-contrast` ×20–25 — mostly the nine problem-navigator links (`#3A7C89` on `#F5F5F5` = **4.35:1**, computed but flagged incomplete because of overlap) and MathJax glyphs (`nonBmp`, `shortTextContent`).
  - Classified: W2, answered → R083 O9: the navigator numbers (4.35:1) are carried under **V-F23**; the reviewer's own low-vision fail on this view is the text **inside the figure images** (LV4/LV9 → V-F24), which no automated contrast check can reach
- O15 [new] (state: all states): **incomplete** `link-in-text-block` — the "detailed view" link in the submission-history line.
  - Classified: W2, answered → no-color **R109**: NC2 **n/a**. Re-measured 2026-09-14 under the G183 rule — the "detailed view" link is not inside running text (its parent has no sentence around it), so 1.4.1 has nothing to judge here

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

- No new finding is raised by this sweep. Every violation it reported is evidenced by a finding the reviewer confirmed on the walks: **V-F1** (O6), **V-F8** (O5), **V-F9** (O9), **V-F11** (O1), **V-F14** (O12), **V-F18** (O2), **V-F23** (O4, O10, O14).
- Dismissed with reasons: O3 (`sig.gif` — silent to the AT, no user impact), O7 and O8 (informational), O11 (`empty-table-header` — headers announced in use, R017 O20).
- Routed: O13 → R018 (motor), O15 → R109 (no-color, n/a).
