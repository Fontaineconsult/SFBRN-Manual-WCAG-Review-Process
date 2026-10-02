# Test Run R015 — S2

| | |
|---|---|
| **Run ID** | R015 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | grayscale (probe: NC2 measured, achromatopsia screenshot) |
| **Baseline** | — |
| **Tester** | Daniel Fontaine (reviewer, OS grayscale filter); assistant records |
| **Result** | Works |

**Result reasoning.** No-color run on My Courses (reviewer with the OS grayscale filter; probe achromatopsia screenshot). Current sidebar item and selected tab remain identifiable without colour; no links in running text; everything operable.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O4, O3 — current item and selected tab are distinguishable without colour — reviewer in grayscale |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O2 — no links inside running text on the view (links are standalone controls/menu items) — measured |
| NC3 — Everything remains operable and understandable in grayscale | pass | O4 — everything operable and understandable in grayscale — reviewer |

**view_probe 2026-09-30:** answered NC2=n/a by measurement; facts in `R015-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a
- O3 [new] (state: R015-grayscale.png (achromatopsia emulation) inspected): Colour-coded states on the view: (1) the current sidebar item "My Courses" — lavender pill + purple text; in grayscale the pill remains a lighter block behind the text, and an icon precedes every item; (2) the selected tab "Classic" — bold dark text vs grey for the unselected; weight and luminance both differ; (3) the "Start course" button — filled block with an icon. No links in running text. Reviewer confirms with the OS filter (NC1, NC3).
- O4 [classified] (reviewer, OS grayscale, 2026-10-02): "Yes with grayscale" — the current sidebar item and the selected tab remain identifiable (pill + icon; bold vs grey), everything operable.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02.** Facts only; NC1/NC3 stay with the reviewer's grayscale look.

## Evidence files in this folder

- (screenshots/exports named R015-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
