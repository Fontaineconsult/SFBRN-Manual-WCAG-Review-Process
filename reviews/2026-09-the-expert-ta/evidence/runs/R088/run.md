# Test Run R088 — S8

| | |
|---|---|
| **Run ID** | R088 |
| **Date/time** | 2026-09-11 14:13 |
| **View / sample** | S8 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentSolutionsV2.aspx?z=1&vmid=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W49) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19), LV4 fail (red values — V-F23), LV9 fail (figure images of math — V-F24); LV2, LV3, LV5, LV6, LV7, LV8 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; tr right=1300; td right=1300; div#TemplateMenu1_divUserMenu right=1300 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — "fine at 400" (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O6 — red variable values and red MathJax numbers "both fail AAA and only [pass] large AA" — regular-size text → fail (reviewer, eyedropper) → V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O7 — "final passes" (reviewer) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O6 — "no hover or focus behaviour" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O5 — "fine at 400" (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (209 inline + 33 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | fail | O5 — "images blur at 400" — the same problem figures carrying mathematical text (reviewer) → V-F24 |

**view_probe 2026-09-11:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R088-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; table right=1300; tbody right=1300; tr right=1300; td right=1300; tr right=1300; td right=1300; div#TemplateMenu1_divUserMenu right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (209 inline + 33 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: View Assignment Solutions, 400 % zoom, 2026-09-15, reviewer, W49): "fine at 400, images blur at 400" — nothing lost, focus fine; the solution figures (the same images-of-math as Take Assignment) pixelate.
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass; LV7 / WCAG 2.4.7, 2.4.11 → pass; LV9 / WCAG 1.4.5 → fail → V-F24 (S8 already listed)
- O6 [classified] (state: View Assignment Solutions, 100 %, 2026-09-15, reviewer, eyedropper, W49): red variable values (`#FF6347`) and red MathJax numbers (`#FF0000`) "both fail AAA and only large AA" — regular-size text, so below 4.5:1; "no hover or focus behaviour".
  - Classified: LV4 / WCAG 1.4.3 → fail → V-F23 (S8 already listed); LV6 / WCAG 1.4.13 → pass
- O7 [classified] (state: View Assignment Solutions, 2026-09-15, reviewer): "final passes" — the page's controls meet 3:1.
  - Classified: LV5 / WCAG 1.4.11 → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R088-<what>.png)

## Findings raised from this run

- V-F19 (1.4.10), V-F23 (1.4.3), V-F24 (1.4.5) — recorded under S1/S3 in 04 §B; confirmed on S8 by this run
