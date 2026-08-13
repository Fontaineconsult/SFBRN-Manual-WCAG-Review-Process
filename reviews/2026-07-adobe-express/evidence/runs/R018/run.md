# Test Run R018 — S2

| | |
|---|---|
| **Run ID** | R018 |
| **Date/time** | 2026-08-13 11:53 |
| **View / sample** | S2 |
| **Page URL / location** | https://new.express.adobe.com/explore/templates |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom |
| **Baseline** | B3 |
| **Tester** | assistant (CDP 320px device emulation per testing-tools §zoom) |
| **Result** | Not set — reflow/spacing closed by measurement; LV4/LV5 (contrast), LV6 (hover), LV7 (focus), LV8 (landscape shot stalled) remain — see O1 |

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O1 — 320px CDP emulation: scrollWidth 320, zero overflow |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O1 — masonry re-stacks single-column, filters collapse; top+mid screenshots |
| LV3 — The view tolerates text-spacing overrides without loss | partial | O1 — no-overflow metric passes; visual confirmation shot stalled (instrument) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | | |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | | |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | | |
| LV7 — Focus indicator remains visible and unobscured at zoom | | |
| LV8 — The view works in both portrait and landscape | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (default grid, 2026-08-13, assistant — CDP 320 CSS px
  device emulation per testing-tools §zoom): Explore reflows cleanly —
  scrollWidth exactly 320 (no 2D scrolling), masonry re-stacks to a single
  column, filter sidebar collapses; evidence R018-lv-baseline-1280.png,
  R018-lv-reflow-320.png, R018-lv-reflow-320-mid.png. Text-spacing override
  (1.4.12 values, injected across shadow roots): no new overflow by metric;
  the confirmation screenshot **stalled — known instrument limit**, the
  renderer never reaches a stable frame under global spacing injection on
  heavy views (same stall on S3/S4; landscape shot not reached for the same
  reason).
  - Classified: LV1, LV2 / 1.4.10, 1.4.4 / pass; LV3 / 1.4.12 / partial —
    no finding. Remaining rows (LV4–LV8) queued for measurement/reviewer.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R018-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
