# Test Run R002 — S11

| | |
|---|---|
| **Run ID** | R002 |
| **Date/time** | 2026-09-10 10:35 |
| **View / sample** | S11 |
| **Page URL / location** | UI: Class Management → Class Menu → Edit Class → Go (popup iframe /Common/eClass.aspx?m=2&eid=3373) |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 151 debug profile); classification pending reviewer |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O6 recorded; reviewer to confirm. Note the document scanned is the popup's iframe source, opened directly — the popup chrome (DevExpress frame, close button) around it is NOT in this scan |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O7 (bypass) → not applicable to an in-popup form, propose dismiss; O8 (Save/Cancel contrast, bgImage) → low-vision run, eyedropper |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check against a keyboard/JAWS walk of the popup as opened from Class Management (S11 locator) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [new] (state: /Common/eClass.aspx?m=2&eid=3373 loaded directly, form pre-filled with the class name — real form content, so the scan is valid despite the session error that followed): axe `label` (critical) — six DevExpress inputs have no label: Class Name, Class Description, Time Zone, Academic Year, Academic Semester, Subject (disabled). Captions are adjacent `<td>` text.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — confirm with JAWS forms mode in the popup → finding (same root cause as R001 O1: DevExpress editors without labels)
- O2 [new] (state: as O1): axe `html-has-lang` (serious) — the iframe document has no `lang` attribute (the host page has `lang="en"`).
  - Proposed: W1 / WCAG 3.1.1 (A) / Minor — confirm; note whether JAWS switches language inside the iframe
- O3 [new] (state: as O1): axe `image-alt` (critical) — spacer `img src="/images/clear.gif"` with no alt attribute (not even empty).
  - Proposed: W1 / WCAG 1.1.1 (A) / Minor (decorative spacer announced as "graphic clear") — confirm with JAWS; likely a real but low-impact failure
- O4 [new] (state: as O1): `landmark-one-main`, `region`, `page-has-heading-one` (best practice) — "Edit Class" title is a styled `span`, no headings/landmarks.
  - Proposed: fold into the structure finding (see R001 O5/O6)
- O5 [new] (state: as O1): passes 16 / inapplicable 68 in `R002-axe.json`.
  - dismissed: informational
- O6 [new] (state: as O1): the popup as actually used sits in a DevExpress popup iframe over Class Management with no `role=dialog`/`aria-modal` found in exploration — not covered by this scan of the inner document.
  - Proposed: route to the keyboard (motor) and no-vision runs on S11 as opened from the UI path (2.4.3 focus into/out of the popup, Escape)
- O7 [new] (state: as O1): axe **incomplete** `bypass`.
  - Proposed: dismiss for this document — a single short form inside a popup has no repeated blocks (reviewer to agree)
- O8 [new] (state: as O1): axe **incomplete** `color-contrast` on the Save and Cancel button captions — DevExpress buttons paint their background with an image (`bgImage`), so axe reports 0:1 = **unmeasured**, not a failure.
  - Proposed: W2 → low-vision run, eyedropper on the rendered button

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 2026-09-10 17:35 UTC. Counts: violations 6, incomplete 2, passes 16, inapplicable 68.
Scanned document: the popup's iframe source `/Common/eClass.aspx?m=2&eid=3373` navigated to directly (form fields pre-filled with the class data, confirming a real render). The popup chrome is not in this scan.
No form was submitted.

## Evidence files in this folder

- `R002-axe.json` — raw axe output (165,147 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
