# Test Run R008 — S6

| | |
|---|---|
| **Run ID** | R008 |
| **Date/time** | 2026-09-10 10:48 |
| **View / sample** | S6 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/calendar.aspx |
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
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O5 (`aria-prohibited-attr` ×8 — FullCalendar `aria-label` on elements with no role) → no-vision run: are the day-of-week headers announced?; O6 (contrast on adjacent-month day numbers, 12 nodes) → low-vision eyedropper |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Calendar is the one view with a heading (h2 month title) — cross-check that JAWS lists it |

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

- O1 [new] (state: Calendar, September 2026, class filter checked, "Hide late work" unchecked): axe `color-contrast` ×2 — the assignment event bar "Chapter 5 Sample Assignment" is white text on `#8EA9DB` = **2.37:1** at 12 px.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major (the only content on the calendar) — confirm by eyedropper → finding
- O2 [new] (state: as O1): `aria-command-name` ×1 (`#top_of_page_jump_point`, PW-B), `aria-hidden-focus` ×1 (PW-C).
  - Proposed: fold into product-wide findings
- O3 [new] (state: as O1): `region` ×12 (incl. the class filter panel `#byClass`), `landmark-one-main` — but **`page-has-heading-one` does not fire**: the month title is an `h2`, so this page has a heading outline (h2 only).
  - Proposed: fold into structure finding with the note that Calendar is the exception
- O4 [new] (state: as O1): passes 40 / inapplicable 46 — the FullCalendar grid itself (`role=grid`, day cells with `aria-label="August 30, 2026"` …) passes axe's ARIA rules.
  - dismissed: informational
- O5 [new] (state: as O1): **incomplete** `aria-prohibited-attr` ×8 — FullCalendar's day-of-week header `<a aria-label="Sunday">Sun</a>` (no href, no role → `aria-label` is prohibited on a generic element) and the view harness `aria-labelledby` on a plain div.
  - Proposed: W2 → no-vision run on S6: what does JAWS announce for the column headers? (4.1.2 if the label is dropped)
- O6 [new] (state: as O1): **incomplete** `color-contrast` ×12 — adjacent-month day numbers (30, 31, Oct 1–10) whose background axe could not resolve.
  - Proposed: W2 → low-vision run, eyedropper one of them (they render light grey — likely below 4.5:1)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 17:48 UTC. Counts: violations 6, incomplete 2, passes 40, inapplicable 46. Direct URL. Calendar component is FullCalendar (class prefix `fc-`), not DevExpress.

## Evidence files in this folder

- `R008-axe.json` — raw axe output (656,733 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
