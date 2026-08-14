# Test Run R019 — S3

| | |
|---|---|
| **Run ID** | R019 |
| **Date/time** | 2026-08-13 11:53 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom |
| **Baseline** | B3 |
| **Tester** | assistant (CDP 320px device emulation) |
| **Result** | Not set — reflow measured (chrome reflows; **canvas hidden behind full-width panel at 320px — interactive reachability check needed, see O1**); LV4–LV8 remain |

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O1 — scrollWidth 320, zero overflow; the one visible canvas is 1.4.10-exempt content |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | partial | O1 — chrome reflows, **but the asset panel occupies the full width and the canvas is not visible**; whether the document is reachable at 320px (panel closable, canvas usable) needs an interactive check. Also noted: File menu label truncates to "F" |
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
- O1 [classified] (editor, "Text Test" doc, Search panel open — 2026-08-13,
  assistant, CDP 320px emulation): **the editor chrome reflows** — single
  column, zero horizontal overflow, rail intact with labels, asset panel
  full-width. **The canvas is not visible in this state**: at 320px the
  open panel covers the document entirely (mobile-style panel-over-canvas).
  This is a plausible responsive pattern, **not recorded as a failure** —
  but LV2 cannot pass until an interactive check shows the panel can be
  closed and the canvas used at this width. Also noted: the top-bar File
  menu label truncates to a bare **"F"** (name/label survives to AT
  presumably — visible-label truncation only; check 2.5.3 relevance if the
  accessible name stays "File", which would then *contain* more than the
  visible label — acceptable direction). Evidence: R019-lv-baseline-1280,
  R019-lv-reflow-320, R019-lv-reflow-320-mid PNGs.
  - Classified: LV1 / 1.4.10 / pass (canvas exempt); LV2 / 1.4.10, 1.4.4 /
    partial — routed to the S3 walkthrough Part E as one interactive
    question: *close the panel at 320px — is the document usable?*

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R019-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
