# Test Run R042 — S6

| | |
|---|---|
| **Run ID** | R042 |
| **Date/time** | 2026-09-11 14:08 |
| **View / sample** | S6 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/calendar.aspx |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W47) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19) and LV5 fail (calendar grid lines below 3:1 — V-F27); LV3 overruled to pass by the reviewer; LV2, LV4, LV6, LV7, LV8, LV9 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1330 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O6 — "all cells reachable" at 400 % (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override applied: 1 container(s) newly clip their text: div "30311 Chapter 5 Sample Assignment23456 C" (measured); reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | pass | O7 — "event bar passes" (reviewer, eyedropper; axe's 2.37:1 on R008 resolved a different background than the rendered pixel — the reviewer's measurement stands) |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | fail | O8 — the month grid's lines "fail all contrast" (reviewer, eyedropper) → V-F27 |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O7 — "no hover or focus" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O7 — no focus issue on the reachable controls; the grid itself takes no focus (see R045 O4) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (11 inline + 33 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O6 — "no blurry text" (reviewer) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=fail, LV8=pass by measurement; facts in `R042-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1330 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override applied: 1 container(s) newly clip their text: div "30311 Chapter 5 Sample Assignment23456 C" (measured)
  - Classified: LV3 / WCAG 1.4.12 / measured → fail; overruled → pass by the reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (11 inline + 33 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O6 [classified] (state: Calendar, September 2026, 400 % zoom, 2026-09-15, reviewer, W47): "all cells reachable, no blurry text".
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass; LV9 / WCAG 1.4.5 → pass
- O7 [classified] (state: Calendar, 100 %, 2026-09-15, reviewer, eyedropper, W47): "event bar passes, no hover or focus" — the white-on-blue event text measures above 4.5:1 on the rendered pixel (axe had 2.37:1 against a resolved background); nothing appears on hover or focus.
  - Classified: LV4 / WCAG 1.4.3 → pass; LV6 / WCAG 1.4.13 → pass; LV7 / WCAG 2.4.7, 2.4.11 → pass
- O8 [classified] (state: Calendar, 100 %, 2026-09-15, reviewer, eyedropper, W47): "grid lines fail all contrast" — the lines separating the day cells are below 3:1 against white.
  - Classified: LV5 / WCAG 1.4.11 → fail → V-F27 (extended to S6)
- O5 [new] (state: Calendar, September 2026, 125 % default zoom, override applied over CDP, 2026-09-15, assistant): `R042-textspacing-1.png` (month grid outlined) — the grid overflows its box by 4 px, a vertical scrollbar appears and covers the right half of every Saturday date number (5, 12, 19, 26); both "Chapter 5 Sample Assignment" event bars stay fully readable. Awaiting the reviewer's ruling (W39b).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- `R042-textspacing.png`, `R042-textspacing-1.png` — the Calendar under the 1.4.12 text-spacing override, the clipping grid outlined in red (assistant, 2026-09-15, W39b)

## Findings raised from this run

- V-F19 (1.4.10, recorded under S1); V-F27 (1.4.11 — grid lines; recorded under S4, extended to this view)
