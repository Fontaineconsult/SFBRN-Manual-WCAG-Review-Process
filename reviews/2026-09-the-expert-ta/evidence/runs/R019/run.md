# Test Run R019 — S1

| | |
|---|---|
| **Run ID** | R019 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W38/W42) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19, Major) and LV4 fail (heading/caption/notice contrast — V-F23, Major); LV3's measured clipping overruled to pass by the reviewer; LV2, LV5, LV6, LV7, LV8, LV9 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1343 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1343; tbody right=1343; tr right=1343; td right=1343; table right=1343; tbody right=1343; tr right=1343; td right=1343; tr right=1343; td right=1343; div#TemplateMenu1_divUserMenu right=1343 (measured); O5 — confirmed by the reviewer at real 400 % zoom, 2026-09-15 |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — nothing hidden, lost or overlapping at 400 % (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override applied: 5 container(s) newly clip their text: td#MainContent_gv2_tccell0_4 "Aug 01, 2026 12:01 AM"; td#MainContent_gv2_tccell0_5 "Sep 01, 2026 12:01 AM"; td#MainContent_gv2_tccell0_6 "Sep 08, 2026 11:59 PM"; td#MainContent_gv2_tccell0_7 "Sep 08, 2026 11:59 PM"; div "Welcome to Testing Course for CSU East B" (measured); reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O6 — teal captions 4.23:1, orange "Class Assignments" 1.74:1, grey welcome/news text 3.94:1 (eyedropper, reviewer) |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O7 — teal controls ≥ 3:1 on white (reviewer); the ⋮ glyph and the image-painted Go button not measured |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O8 — the only focus-revealed content is the inline accessibility-instructions text; nothing appears on hover |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O5 — focus ring visible on every Tab stop at 400 % (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (57 inline + 51 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O5 — no text goes blurry at 400 % on this page (reviewer) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=fail, LV8=pass by measurement; facts in `R019-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1343 (two-dimensional scrolling); non-exempt overflow: div#container right=1300; table right=1343; tbody right=1343; tr right=1343; td right=1343; table right=1343; tbody right=1343; tr right=1343; td right=1343; tr right=1343; td right=1343; div#TemplateMenu1_divUserMenu right=1343 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override applied: 5 container(s) newly clip their text: td#MainContent_gv2_tccell0_4 "Aug 01, 2026 12:01 AM"; td#MainContent_gv2_tccell0_5 "Sep 01, 2026 12:01 AM"; td#MainContent_gv2_tccell0_6 "Sep 08, 2026 11:59 PM"; td#MainContent_gv2_tccell0_7 "Sep 08, 2026 11:59 PM"; div "Welcome to Testing Course for CSU East B" (measured)
  - Classified: LV3 / WCAG 1.4.12 / measured → fail; overruled → pass by the reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (57 inline + 51 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: Class Management, standard mode, 2026-09-15, reviewer, ~1280 px window at 400 % browser zoom, walkthrough W38): Reviewer 2026-09-15, real 400 % zoom in a ~1280 px window: "nothing is hidden or lost at 400%, but no reflow" — the page keeps its fixed-width layout and needs sideways scrolling to read a line; nothing is cut off, hidden or overlapping, and every control stays reachable.
  - Classified: LV1 / WCAG 1.4.10 / Major → finding V-F19 (confirms O2); LV2 / WCAG 1.4.10, 1.4.4 → pass
- O5a [classified] (state: Class Management, standard mode, 400 % zoom, 2026-09-15, reviewer, W42): "focus ring visible with tab"; "no text goes blurry".
  - Classified: LV7 / WCAG 2.4.7, 2.4.11 → pass; LV9 / WCAG 1.4.5 → pass
- O6 [classified] (state: Class Management, standard mode, 100 %, 2026-09-15, reviewer, eyedropper, W42): teal captions "Classes" / "Class Menu" (`#48848C` on white): "Large pass, Fail regular for AA" — the captions are 16 px, not large text → 4.23:1 fails 4.5:1. "Class Assignments" heading (`#EFBB75` on white): "fail for all levels" (1.74:1). Grey `#808080` text on white (the welcome / Class News body line): "fails over white for AAA and only passes for large in AA" — the line is 12 px → 3.94:1 fails 4.5:1. The "Class News" heading (`#E58F65`, axe 2.48:1) was not eyedroppered separately; same family of decorative heading colours.
  - Classified: LV4 / WCAG 1.4.3 / Major (assistant's rating — reviewer to confirm) → finding V-F23
- O7 [classified] (state: as O6): "Pass for UI component" — the teal control borders and focus ring on white are ≥ 3:1. Not measured: the ⋮ row-menu glyph (axe: nonBmp) and the image-painted Go button.
  - Classified: LV5 / WCAG 1.4.11 → pass (unmeasured items noted)
- O8 [classified] (state: as O6): "Only thing that appears when tabbed that is otherwise hidden is the accessibility instructions" — the inline instruction text revealed on focus (the first Tab stop, R015 O3); it does not obscure other content and goes away when focus leaves. Nothing appears on hover.
  - Classified: LV6 / WCAG 1.4.13 → pass
- O9 [new] (state: Class Management, standard mode, 125 % default zoom, override applied over CDP, 2026-09-15, assistant): `R019-textspacing-5.png` (due-date cell outlined) — under the override every date cell of the assignment row drops its AM/PM ("Aug 01, 2026 12:01", "Sep 08, 2026 11:59") and the Start cell also loses its last minute digit ("Sep 01, 2026 12:0"); the "Weight" header reads "Weigh"; the welcome / news text wraps inside its box with a scrollbar (no loss). Awaiting the reviewer's confirmation that the lost AM/PM is content loss (W39b).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- `R019-textspacing.png`, `R019-textspacing-N.png` — the page under the 1.4.12 text-spacing override, crops of each container that newly clips (assistant, 2026-09-15, for W39b)

## Findings raised from this run

- V-F19 (1.4.10 — no reflow; recorded under S1 in 04 §B)
- V-F23 (1.4.3 — text contrast; recorded under S1 in 04 §B)
