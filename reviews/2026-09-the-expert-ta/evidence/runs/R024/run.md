# Test Run R024 — S2

| | |
|---|---|
| **Run ID** | R024 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S2 |
| **Page URL / location** | UI: Class Management → "Accessibility Page" button (lands on /common/default2.aspx; the URL alone redirects to default.aspx) |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom (reviewer, W43) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19) and LV4 fail (heading/notice contrast — V-F23); LV3 overruled to pass by the reviewer; LV2, LV5, LV6, LV7, LV8, LV9 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1335 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — nothing cut off or unreachable at 400 % (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override applied: 2 container(s) newly clip their text: td#MainContent_gv2_tccell0_1 "Chapter 5 Sample Assignment"; div "Data table related to the headers above " (measured); reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O6 — the same heading and notice colours as standard mode: "Class Assignments" `#EFBB75` 1.74:1, "Class News" `#E58F65` 2.48:1, grey `#808080` 3.94:1 (axe R005; the identical hex values eyedroppered by the reviewer on S1, R019 O6) → V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O7 — "Go button passes contrast" (reviewer, eyedropper) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O8 — "no hover issues" (reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O7 — "Focus ring is fine" at 400 % (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (49 inline + 51 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O7 — "No blurry text"; the Go button "is not blurry" (reviewer) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=fail, LV8=pass by measurement; facts in `R024-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1335 (two-dimensional scrolling); non-exempt overflow: div#container right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override applied: 2 container(s) newly clip their text: td#MainContent_gv2_tccell0_1 "Chapter 5 Sample Assignment"; div "Data table related to the headers above " (measured)
  - Classified: LV3 / WCAG 1.4.12 / measured → fail; overruled → pass by the reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (49 inline + 51 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: Class Management, Accessibility Mode, 400 % zoom, 2026-09-15, reviewer, W43): "no for accessibility mode at 400" — nothing cut off, overlapping or unreachable.
  - Classified: LV2 / WCAG 1.4.10, 1.4.4 → pass
- O6 [classified] (state: Class Management, Accessibility Mode, 100 %, 2026-09-15): the section headings and grey notice text use the same colours as standard mode — axe R005 measured `#EFBB75` 1.74:1, `#E58F65` 2.48:1, `#808080` 3.94:1 on this page; the reviewer eyedroppered those same values on the standard page (R019 O6) and rated them fails.
  - Classified: LV4 / WCAG 1.4.3 → fail → finding V-F23
- O7 [classified] (state: Class Management, Accessibility Mode, 2026-09-15, reviewer, W43): "No blurry text other than the images. Focus ring is fine, Go button passes contrast and is not blurry." (this page has no figure images — the images remark belongs to Take Assignment).
  - Classified: LV7 / WCAG 2.4.7, 2.4.11 → pass; LV5 / WCAG 1.4.11 → pass; LV9 / WCAG 1.4.5 → pass
- O8 [classified] (state: Class Management, Accessibility Mode, 2026-09-15, reviewer, W43): "no hover issues" — nothing appears on hover or focus beyond the page's own skip links.
  - Classified: LV6 / WCAG 1.4.13 → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R024-<what>.png)

## Findings raised from this run

- V-F19 (1.4.10, recorded under S1); V-F23 (1.4.3, recorded under S1)
