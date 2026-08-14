# Test Run R020 — S4

| | |
|---|---|
| **Run ID** | R020 |
| **Date/time** | 2026-08-13 11:53 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom |
| **Baseline** | B3 |
| **Tester** | assistant (CDP 320px device emulation) |
| **Result** | Not set — reflow/spacing closed by measurement; LV4–LV8 remain (contrast, hover, focus, landscape) |

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O1 — scrollWidth 320, zero overflow |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O1 — file cards stack single-column; tabs/controls present; top+mid screenshots |
| LV3 — The view tolerates text-spacing overrides without loss | partial | O1 — no-overflow metric passes; confirmation shot stalled (instrument) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | | |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | | |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | | |
| LV7 — Focus indicator remains visible and unobscured at zoom | | |
| LV8 — The view works in both portrait and landscape | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (file listing, 2026-08-13, assistant — CDP 320px
  emulation): Your stuff reflows cleanly — cards stack to one column, zero
  horizontal overflow; text-spacing no-overflow by metric (confirmation
  shot stalled — same instrument limit as R018/R019). Evidence:
  R020-lv-baseline-1280, R020-lv-reflow-320, R020-lv-reflow-320-mid PNGs.
  - Classified: LV1, LV2 / 1.4.10, 1.4.4 / pass; LV3 / partial — no finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R020-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
