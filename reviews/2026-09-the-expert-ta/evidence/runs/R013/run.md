# Test Run R013 — R2

| | |
|---|---|
| **Run ID** | R013 |
| **Date/time** | 2026-09-10 10:49 |
| **View / sample** | R2 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignmentProblems.aspx?m=1&eid=3373&aid=17547 |
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
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O2 recorded; reviewer to confirm/dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O3 (`aria-prohibited-attr` on the Export button div) → no-vision run: is "Export button" announced?; O4 (pivot header/button contrast ×6) → low-vision eyedropper |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with a JAWS pass over the pivot grid (random-sample comparison, 04 §C) |

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

- O1 [new] (state: View Grades (Spreadsheet) for the sample assignment, empty roster): the cleanest sweep of the set — **no `label`, no `color-contrast` violation**; only `aria-command-name` ×1, `aria-hidden-focus` ×1, `region` ×20, `landmark-one-main`, `page-has-heading-one` (PW-B/C/D).
  - Proposed: fold into product-wide findings
- O2 [new] (state: as O1): passes 35 / inapplicable 52.
  - dismissed: informational
- O3 [new] (state: as O1): **incomplete** `aria-prohibited-attr` — the Export control is a `div` with `aria-label="Export button"` and `title="Export and save"` but **no role**, so the label is prohibited and may be dropped by AT.
  - Proposed: W2 → no-vision run: what does JAWS announce on the Export control? (4.1.2)
- O4 [new] (state: as O1): **incomplete** `color-contrast` ×6 — Export caption (`bgImage`, PW-F) and pivot-grid header cells (`bgOverlap`).
  - Proposed: W2 → low-vision eyedropper

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:49 UTC. Counts: violations 5, incomplete 2, passes 35, inapplicable 52. Random-sample view R2. Direct URL; roster empty.

## Evidence files in this folder

- `R013-axe.json` — raw axe output (277,748 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
