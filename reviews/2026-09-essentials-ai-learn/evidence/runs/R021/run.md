# Test Run R021 — S3

| | |
|---|---|
| **Run ID** | R021 |
| **Date/time** | 2026-09-30 14:07 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker` (video lesson); Classic experience |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — NC1, NC3 need the reviewer — judge from `R021-grayscale.png` (achromatopsia emulation) or the OS filter |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | | |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O2 — no links inside running text on the view (links are standalone controls/menu items) — measured |
| NC3 — Everything remains operable and understandable in grayscale | | |

**view_probe 2026-09-30:** answered NC2=n/a by measurement; facts in `R021-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a
- O3 [new] (state: R021-grayscale.png inspected): Colour-coded states: the current lesson (lavender highlight + filled circle icon), completed vs not-completed lessons (circle icons — none completed yet), the progress bar fill. In grayscale the current lesson keeps its highlight block and icon; status circles differ by fill, not only hue. Reviewer confirms with the OS filter, ideally after one lesson is completed so the completed-state icon can be judged.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02.** Facts only; NC1/NC3 stay with the reviewer.

## Evidence files in this folder

- (screenshots/exports named R021-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
