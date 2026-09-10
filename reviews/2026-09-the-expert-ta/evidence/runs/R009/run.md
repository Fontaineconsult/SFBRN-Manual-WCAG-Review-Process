# Test Run R009 — S9

| | |
|---|---|
| **Run ID** | R009 |
| **Date/time** | 2026-09-10 10:48 |
| **View / sample** | S9 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignments.aspx?m=1&eid=3373 |
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
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O3 recorded; reviewer to confirm/dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O4 (pivot-grid header and button contrast, 6 nodes, bgOverlap/bgImage) → low-vision eyedropper; O5 (bypass) → settled on S1 |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of the grade sheet (P5 step 4) — the DevExpress pivot grid is the structure question here |

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

- O1 [new] (state: Class Assignments Grade Sheet, empty roster): axe `label` (critical) ×3 — the student-filter text box `#MainContent_txtCodeFilter`, the "Points View" check-box state field (PW-G) and the export-format combo `#MainContent_listExportFormat_I`.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — PW-A; confirm with JAWS → add to the unlabeled-editors finding
- O2 [new] (state: as O1): `aria-command-name` ×1, `aria-hidden-focus` ×1, `region` ×21, `landmark-one-main`, `page-has-heading-one` (PW-B/C/D). No `color-contrast` violation on this view.
  - Proposed: fold into product-wide findings
- O3 [new] (state: as O1): passes 27 / inapplicable 57. The DevExpress **pivot grid** (`ASPxPivotGrid1`) raises no ARIA violation — axe does not judge whether a pivot grid built from `td`s with `onclick` sort handlers is operable.
  - Proposed: route to the no-vision and motor runs on S9 (sortable headers reachable/announced?)
- O4 [new] (state: as O1): **incomplete** `color-contrast` ×6 — pivot-grid header cells (`bgOverlap`) and the Save button (`bgImage`, PW-F): unmeasured.
  - Proposed: W2 → low-vision run, eyedropper a header cell and the "Averages" / "Assignment Weight" rows (light-blue background)
- O5 [new] (state: as O1): **incomplete** `bypass` (PW-E).
  - Proposed: settled on S1

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:48 UTC. Counts: violations 6, incomplete 2, passes 27, inapplicable 57. Direct URL; roster empty so the grid shows averages only — re-scan once a test student has a grade.

## Evidence files in this folder

- `R009-axe.json` — raw axe output (241,050 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
