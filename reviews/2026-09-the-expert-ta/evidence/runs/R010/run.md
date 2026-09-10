# Test Run R010 — S10

| | |
|---|---|
| **Run ID** | R010 |
| **Date/time** | 2026-09-10 10:48 |
| **View / sample** | S10 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/vwMates.aspx?m=1&eid=3373 |
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
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O4 (Save button caption, bgImage) → low-vision eyedropper; O5 (bypass) → settled on S1 |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of the roster (A4 candidate view) |

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

- O1 [new] (state: Manage Class Roster, "No data to display"): axe `label` (critical) ×3 — Classes combo `#MainContent_ASPxCallbackPanel1_cbClasses_I`, student-filter text box, export-format combo (PW-A).
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — add to the unlabeled-editors finding after JAWS confirmation
- O2 [new] (state: as O1): `color-contrast` ×1 — grid empty-state text "No data to display" `#808080` on white = **3.94:1** at 12 px.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Minor — same grey token as R001 O4 (news body) — add to that finding
- O3 [new] (state: as O1): `aria-command-name` ×1, `aria-hidden-focus` ×1, `region` ×19, `landmark-one-main`, `page-has-heading-one` (PW-B/C/D); passes 26 / inapplicable 58.
  - Proposed: fold into product-wide findings
- O4 [new] (state: as O1): **incomplete** `color-contrast` ×1 — Save (export) button caption (PW-F).
  - Proposed: W2 → low-vision eyedropper
- O5 [new] (state: as O1): **incomplete** `bypass` (PW-E).
  - Proposed: settled on S1

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:48 UTC. Counts: violations 7, incomplete 2, passes 26, inapplicable 58. Direct URL. Roster is empty in the demo — the extended-time (A4) controls, if they live here, were not visible; re-scan once a test student is enrolled.

## Evidence files in this folder

- `R010-axe.json` — raw axe output (239,034 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
