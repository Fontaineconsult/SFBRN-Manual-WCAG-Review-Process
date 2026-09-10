# Test Run R005 — S2

| | |
|---|---|
| **Run ID** | R005 |
| **Date/time** | 2026-09-10 10:47 |
| **View / sample** | S2 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default2.aspx |
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
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O6 (bypass) — this page has explicit skip links ("Tab for Assignments, Enter to skip"), so propose pass once the no-vision run confirms they work |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of S2 (the mode the vendor built for AT users) |

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

- O1 [new] (state: Class Management, Accessibility Mode, one assignment row): axe `select-name` (critical) — the per-row Actions `<select id="assignmentSelectMenu-17547">` has no accessible name (no label, title or aria-label). The two top selects (Classes, Class Menu) **do** carry names ("First make your selection here and then click Go button…") — so the accessible version fixes the combo-box naming that the standard page (R001 O1) lacks, except for this one.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major (this select is how a student reaches "Take Assignment" in this mode) — confirm with JAWS → finding
- O2 [new] (state: as O1): `color-contrast` ×3 — the same section captions as R001 O4: "Class Assignments" 1.74:1, "Class News" 2.48:1, news body 3.94:1. The "Classes"/"Class Menu" captions were restyled in this mode and no longer fail.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major — same finding as R001 O4, add this view to it
- O3 [new] (state: as O1): `aria-command-name` ×1 (`#top_of_page_jump_point`, PW-B) and `aria-hidden-focus` ×1 (PW-C).
  - Proposed: fold into the product-wide findings
- O4 [new] (state: as O1): `region` ×29, `landmark-one-main`, `page-has-heading-one` (PW-D) — the accessible version still has no landmarks or headings; it relies on skip links and inline instruction text instead.
  - Proposed: fold into structure finding; note in the report that the alternate version does not add structure
- O5 [new] (state: as O1): passes 36 / inapplicable 49; the `label` rule now passes (native selects with names).
  - dismissed: informational
- O6 [new] (state: as O1): **incomplete** `bypass` — skip links exist ("Tab for Assignments, Enter to skip" → `javascript:skipper('News')`).
  - Proposed: W2 → no-vision run: confirm the skip links move focus (2.4.1 pass for this mode)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:47 UTC. Counts: violations 7, incomplete 1, passes 36, inapplicable 49.
Mode toggled with the "Accessibility Page" button on the standard page, scanned, then toggled back with "Non-Accessibility Page" and verified (`default.aspx` renders "Class Management" again). The account was left in standard mode.

## Evidence files in this folder

- `R005-axe.json` — raw axe output (303,162 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
