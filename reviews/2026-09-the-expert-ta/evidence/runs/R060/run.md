# Test Run R060 — S12

| | |
|---|---|
| **Run ID** | R060 |
| **Date/time** | 2026-09-11 14:09 |
| **View / sample** | S12 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W53) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19) and LV4 fail (tutorial text contrast — V-F23); LV2, LV3, LV5, LV6, LV7, LV8, LV9 pass. No Blocker under this modality (the page's Blocker, V-F28, is keyboard / screen reader), so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: ul right=353; li right=353; a right=353; li#TemplateHeader1_liChangePassword right=353; a right=353; li right=353; a right=353; div#container right=1300 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O6 — "nothing cut off at 400" (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O5 — "the tutorial text fails AAA, only fails regular AA" — regular-size text below 4.5:1 (reviewer, eyedropper; axe: `#3A7C89` on `#EDEDED` 4.05:1, "Library" 1.74:1) → V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O7 — "final passes" (reviewer, eyedropper: selects and checkboxes) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O6 — "no hover issue" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O6 — "focus ring is limited, but not due to zoom": where focus exists it stays visible and unobscured at 400 %; the missing focus on the grid is the keyboard defect V-F28 (R063 MO4), not a zoom effect (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (38 inline + 49 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O7 — no blurry text (reviewer) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=pass, LV8=pass by measurement; facts in `R060-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: ul right=353; li right=353; a right=353; li#TemplateHeader1_liChangePassword right=353; a right=353; li right=353; a right=353; div#container right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (38 inline + 49 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: Student Practice Area, 100 %, 2026-09-15, reviewer, eyedropper, W53): "main contrast issue is the tutorial text fails AAA only fails regular AA".
  - Classified: LV4 / WCAG 1.4.3 → fail → V-F23 (S12 already listed)
- O6 [classified] (state: Student Practice Area, 400 % zoom, 2026-09-15, reviewer, W53): "nothing cut off at 400, focus ring is limited, but not due to zoom, the actual text content in the tutorial fails AAA and only half of AA. no hover issue".
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass; LV7 / WCAG 2.4.7, 2.4.11 → pass (zoom does not obscure; the limited focus is V-F28); LV6 / WCAG 1.4.13 → pass; LV4 reconfirmed
- O7 [classified] (state: as O6, 2026-09-15, reviewer): "final passes" — the selects / checkboxes meet 3:1 and no text is blurry.
  - Classified: LV5 / WCAG 1.4.11 → pass; LV9 / WCAG 1.4.5 → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R060-<what>.png)

## Findings raised from this run

- V-F19 (1.4.10), V-F23 (1.4.3) — recorded under S1; confirmed on S12
