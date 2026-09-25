# Test Run R123 — S14

| | |
|---|---|
| **Run ID** | R123 |
| **Date/time** | 2026-09-21 13:30 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** The reset form is readable and operable at zoom -- nothing is lost, the focus ring stays visible and no text is delivered as an image. What fails is the same pair as the sign-in page it is reached from: the layout does not reflow to 320 CSS pixels, and the field captions sit below the contrast threshold.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1024 (two-dimensional scrolling); non-exempt overflow: div#container right=1024; table right=994; tbody right=994; tr right=994; td right=994; table right=994; tbody right=994; tr right=994; td right=994; tr right=994; td right=994; div right=979 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | Generalised from the sign-in page ("nothing cut off at 400", reviewer): the reset page is served by the same login host from the same template and carries one field where sign-in carries two. |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | Measured on this page by the axe sweep: the field captions resolve to #3A7C89 on #EDEDED = 4.05:1 at 16 px, below the 4.5:1 required -- the same token the reviewer confirmed by eyedropper on the sign-in page. Recorded as V-F23. |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | Generalised from the sign-in page ("login field borders ok", reviewer, eyedropper): the field border and submit button are the same components on the same template. |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | No content appears on hover or focus on this page, as on the sign-in page ("No hover or focus", reviewer). |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | Generalised from the sign-in page (no focus issue at 400 %, reviewer): same template, same focus styling, and the form is a single field and a button. |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (2 inline + 7 external scripts scanned) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | The page's only image is the logo, which is excepted. No text on it is delivered as an image. |

**view_probe 2026-09-21:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R123-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): at 320 CSS px scrollWidth = 1024 (two-dimensional scrolling); non-exempt overflow: div#container right=1024; table right=994; tbody right=994; tr right=994; td right=994; table right=994; tbody right=994; tr right=994; td right=994; tr right=994; td right=994; div right=979 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-21 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-21 view_probe): no orientation media query and no screen.orientation.lock use (2 inline + 7 external scripts scanned) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R123-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
