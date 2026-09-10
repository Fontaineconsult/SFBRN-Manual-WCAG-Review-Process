# Test Run R012 — R1

| | |
|---|---|
| **Run ID** | R012 |
| **Date/time** | 2026-09-10 10:48 |
| **View / sample** | R1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Instructor/AcademicIntegrityTemplates.aspx |
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
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O4 recorded; reviewer to confirm/dismiss |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O5 (honor-code textarea and Save Preferences button, unmeasured) → low-vision eyedropper |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | One of only two views with a `main` landmark — cross-check that JAWS lands on it (random-sample comparison, 04 §C) |

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

- O1 [new] (state: Academic Integrity Preferences, profile "Instructor Default" selected): axe `label` (critical) ×12 — the profile list box keyboard field (`_KBS`, PW-G), the template-options combo, the Yes/No radio state fields for "Display Honor Code" and "Display Terms of Service", and the two `textarea`s (Honor Code, Terms of Service) (PW-A).
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — add to the unlabeled-editors finding after JAWS confirmation
- O2 [new] (state: as O1): `color-contrast` ×1 — the selected list-box item "Instructor Default" (white text on the DevExpress selection colour; ratio in JSON).
  - Proposed: W1 / WCAG 1.4.3 (AA) / Minor — eyedropper in the low-vision run
- O3 [new] (state: as O1): `aria-command-name` ×1, `aria-hidden-focus` ×1, `region` ×13, `page-has-heading-one` — but **`landmark-one-main` passes**: this page has a `main` (PW-D partially met here).
  - Proposed: fold into product-wide findings; record the `main` as the exception for the random-vs-structured comparison
- O4 [new] (state: as O1): passes 31 / inapplicable 55.
  - dismissed: informational
- O5 [new] (state: as O1): **incomplete** `color-contrast` ×2 — Honor Code textarea text and "Save Preferences" button caption (PW-F).
  - Proposed: W2 → low-vision eyedropper

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:48 UTC. Counts: violations 6, incomplete 1, passes 31, inapplicable 55. Random-sample view R1. Direct URL; nothing changed or saved.

## Evidence files in this folder

- `R012-axe.json` — raw axe output (280,320 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
