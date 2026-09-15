# Test Run R030 — S4

| | |
|---|---|
| **Run ID** | R030 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S4 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W45) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19), LV4 fail (red/grey notice text and red variable values — V-F23), LV5 fail (table borders below 3:1 — V-F27), LV9 fail (figure images of math — V-F24); LV2, LV3, LV6, LV7, LV8 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured); O5 — \"requires horizontal scrolling\" at 400 % (reviewer, 2026-09-15) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — "at 400 nothing cut off" (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 97 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O6 — red and grey notice text fail regular-size AA; randomized math values fail at every level (reviewer, eyedropper) → V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | fail | O8 — the grade tables' line borders "are too small and fail color contrast at all levels" (reviewer, eyedropper) → V-F27 |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O7 — "no hover or focus issues" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O7 — "no hover or focus issues" at 400 % (reviewer; read as the focus ring being visible — correct if not) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (97 inline + 37 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | fail | O5 — the same problem figures as Take Assignment "don't scale and are blurry" (reviewer) → V-F24 |

**view_probe 2026-09-11:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R030-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 97 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (97 inline + 37 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: View Grade Report, 400 % zoom, 2026-09-15, reviewer, W45): "at 400 nothing cut off, requires horizontal scrolling, same images don't scale and are blurry" — the per-problem tables stay complete; the page as a whole scrolls sideways (the fixed container, V-F19); the problem figures repeated on this page are the same low-resolution images of mathematical text as on Take Assignment.
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass; LV1 / WCAG 1.4.10 → fail confirmed (V-F19); LV9 / WCAG 1.4.5 → fail → V-F24 (extended to S4)
- O6 [classified] (state: View Grade Report, 100 %, 2026-09-15, reviewer, eyedropper, W45): "Red o[n] white fails AAA, passes large AA and fails regular AA, same for grey, randomized math values fail all color contrast." — the red "Red submission date times indicate late work." and the grey "All date times are displayed in Pacific Standard Time" lines are regular-size (13 px) text → fail; the red randomized-variable values (`#FF6347`, axe 2.94:1) fail outright.
  - Classified: LV4 / WCAG 1.4.3 → fail → V-F23 (S4 already listed)
- O7 [classified] (state: as O5/O6): "no hover or focus issues" — nothing appears on hover or focus; focus ring visible at zoom.
  - Classified: LV6 / WCAG 1.4.13 → pass; LV7 / WCAG 2.4.7, 2.4.11 → pass
- O8 [classified] (state: View Grade Report, 100 %, 2026-09-15, reviewer, eyedropper, W45): "line borders are too small and fail color contrast at all levels" — the cell borders of the per-problem grade tables are thin and below 3:1 against the white background, so the boundaries between the score, date and answer cells are hard to see.
  - Classified: LV5 / WCAG 1.4.11 / Minor (assistant's rating — reviewer to confirm) → finding V-F27

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R030-<what>.png)

## Findings raised from this run

- V-F19 (1.4.10), V-F23 (1.4.3), V-F24 (1.4.5) — recorded under S1/S3 in 04 §B, confirmed on S4; V-F27 (1.4.11 — table borders, recorded under S4)
