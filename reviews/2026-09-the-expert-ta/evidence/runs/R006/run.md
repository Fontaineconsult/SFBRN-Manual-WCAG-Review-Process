# Test Run R006 — S5

| | |
|---|---|
| **Run ID** | R006 |
| **Date/time** | 2026-09-10 10:47 |
| **View / sample** | S5 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547 |
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
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O6 (22 unmeasured button captions, bgImage) → low-vision eyedropper on two representative buttons; O7 (bypass) → settled on S1 |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS/keyboard walk of the editor (P4) |

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

- O1 [new] (state: Assignment Editor, editing "Chapter 5 Sample Assignment", library on "Expert TA: Introduction to Physics"): axe `label` (critical) — **59 nodes**: Assignment Name, Description (textarea), Grade Preferences and Integrity Preferences combos, Assignment Weight spin editor, the "Use the sum of Problem Weights" check box state field (PW-G), the `probsel` radio buttons in the problem list, and the library filter check boxes' hidden state fields — including the **"Accessibility(AA) Only"** filter itself.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major (the whole authoring form is unlabeled; PW-A at scale) — confirm with JAWS forms mode in P4 → finding; call out the Accessibility(AA) filter specifically because the TAAP relies on instructors finding it
- O2 [new] (state: as O1): `color-contrast` ×8 — section titles "Assignment Details", "Assignment Dates", "Additional Configuration" (`#DB715C` on white = **3.21:1**, 16 px); "Library" (`#EFBB75`, **1.74:1**); "Books", "Chapters", "Sections", "Filter by Problem Difficulty and Type" (`#3A7C89` on `#EDEDED` = **4.05:1**).
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major — same colour tokens as R001 O4; add this view to that finding
- O3 [new] (state: as O1): `aria-command-name` ×1, `aria-hidden-focus` ×1, `region` ×89, `landmark-one-main`, `page-has-heading-one` (PW-B/C/D).
  - Proposed: fold into product-wide findings
- O4 [new] (state: as O1): no violation on the toolbar buttons (Save Only, Save & Exit, …, Extensions, Security, Messages) — they have names.
  - dismissed: informational
- O5 [new] (state: as O1): passes 27 / inapplicable 57.
  - dismissed: informational
- O6 [new] (state: as O1): **incomplete** `color-contrast` ×22 — every DevExpress toolbar button caption (PW-F, `bgImage`).
  - Proposed: W2 → low-vision run, eyedropper "Save Only" and a disabled one ("Delete Assignment")
- O7 [new] (state: as O1): **incomplete** `bypass` (PW-E).
  - Proposed: settled on S1

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:47 UTC. Counts: violations 7 (59 `label` nodes), incomplete 2, passes 27, inapplicable 57. Reached by direct URL (valid with a live session). Nothing was changed or saved.

## Evidence files in this folder

- `R006-axe.json` — raw axe output (911,058 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
