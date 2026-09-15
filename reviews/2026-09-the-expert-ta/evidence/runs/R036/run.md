# Test Run R036 — S5

| | |
|---|---|
| **Run ID** | R036 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S5 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W46) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19) and LV4 fail (section-heading contrast — V-F23); LV2, LV3, LV5, LV6, LV7, LV8, LV9 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1373 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1373; tbody right=1373; tr right=1373; td right=1373; table right=1373; tbody right=1373; tr right=1373; td right=1373; tr right=1373; td right=1373; div#TemplateMenu1_divUserMenu right=1373 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — "everything is reachable at 400. Nothing hidden" (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O6 — "Assignment Details" heading fails regular-size AA (3.21:1), "Library" heading fails at every level (1.74:1) (reviewer, eyedropper) → V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O8 — toolbar buttons and spinner arrows: "contrast is fine" (reviewer, eyedropper) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O7 — "No hover or focus issues" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O7 — "No hover or focus issues" at 400 % (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (126 inline + 54 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O5a — only the image-painted button faces blur; the captions are real text over them ("Just the buttons are blurry", reviewer; axe reports the captions as text over a background image) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R036-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1373 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1373; tbody right=1373; tr right=1373; td right=1373; table right=1373; tbody right=1373; tr right=1373; td right=1373; tr right=1373; td right=1373; div#TemplateMenu1_divUserMenu right=1373 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (126 inline + 54 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: Assignment Editor, 400 % zoom, 2026-09-15, reviewer, W46): "AssignmentEditor everything is reachable at 400. Nothing hidden" — the library and details panels do not hide each other; the toolbar buttons stay reachable.
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass
- O5a [classified] (state: as O5): "Some buttons or checkboxes are blurry" — clarified 2026-09-15: "Just the buttons are blurry" — the DevExpress button faces (background images) pixelate at 400 %; the captions are real text (axe measured them as text over a background image, `bgImage`), so nothing textual is an image. Cosmetic.
  - Classified: LV9 / WCAG 1.4.5 → pass
- O6 [classified] (state: Assignment Editor, 100 %, 2026-09-15, reviewer, eyedropper, W46): "Assignment Details fails AAA contrast and only passes large for AA" (16 px regular → fail, axe 3.21:1); "Library fails All" (1.74:1).
  - Classified: LV4 / WCAG 1.4.3 → fail → V-F23 (S5 already listed)
- O7 [classified] (state: as O5/O6): "No hover or focus issues" — nothing appears on hover or focus; focus ring visible at zoom.
  - Classified: LV6 / WCAG 1.4.13 → pass; LV7 / WCAG 2.4.7, 2.4.11 → pass
- O8 [classified] (state: Assignment Editor, 100 %, 2026-09-15, reviewer, eyedropper): toolbar buttons and the Weight spinner arrows — "contrast is fine".
  - Classified: LV5 / WCAG 1.4.11 → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R036-<what>.png)

## Findings raised from this run

- V-F19 (1.4.10), V-F23 (1.4.3) — recorded under S1 in 04 §B; confirmed on S5 by this run
