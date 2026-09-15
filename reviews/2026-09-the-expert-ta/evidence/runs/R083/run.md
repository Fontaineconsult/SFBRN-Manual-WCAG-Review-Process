# Test Run R083 — S3

| | |
|---|---|
| **Run ID** | R083 |
| **Date/time** | 2026-09-11 14:13 |
| **View / sample** | S3 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/TakeTutorialAssignment.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | probe; zoom + eyedropper (reviewer, W38/W44) |
| **Baseline** | B3 |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Every row answered 2026-09-15: LV1 fail (no reflow — V-F19), LV4 fail (figure-image text over graphics on Problems 1 and 6 — V-F24; UI text colours — V-F23), LV9 fail (figures are images of mathematical text that blur at 400 % — V-F24); LV3 overruled to pass by the reviewer; LV2, LV5, LV6, LV7, LV8 pass. No Blocker, so Works with issues.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | fail | O2 — at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: ul right=353; li right=353; a right=353; li#TemplateHeader1_liChangePassword right=353; a right=353; li right=353; a right=353; div#container right=1300 (measured); O5 — confirmed by the reviewer at real 400 % zoom, 2026-09-15 |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O5 — nothing hidden, lost or overlapping at 400 % (reviewer) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override applied: 1 container(s) newly clip their text: div "6M79-C9-72-46-B37E-17547" (measured); reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O9 — Problems 1 and 6: text inside the figure images sits over a graphic below 4.5:1 (reviewer); the UI text colours (deduction % 2.14:1, red variable values 2.94:1, navigator numbers 4.35:1) are axe measurements under V-F23 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O10 — "Submit button and others pass contrast" (reviewer, eyedropper) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | pass | O10 — nothing appears on hover or focus ("Nothing", reviewer) |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O8 — "no new issues are obvious for assignment pages at 400: this can be passed" (reviewer) |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (16 inline + 39 external scripts scanned, 1 unreadable) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | fail | O6 — the problem figures are low-resolution images that contain text, "usually math", and blur at 400 % (reviewer) |

**view_probe 2026-09-11:** answered LV1=fail, LV3=fail, LV8=pass by measurement; facts in `R083-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): at 320 CSS px scrollWidth = 1300 (two-dimensional scrolling); non-exempt overflow: ul right=353; li right=353; a right=353; li#TemplateHeader1_liChangePassword right=353; a right=353; li right=353; a right=353; div#container right=1300 (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): text-spacing override applied: 1 container(s) newly clip their text: div "6M79-C9-72-46-B37E-17547" (measured)
  - Classified: LV3 / WCAG 1.4.12 / measured → fail; overruled → pass by the reviewer's ruling 2026-09-15 (W39b): "no issues noted with text spacing" — measured clipping not rated a loss
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no orientation media query and no screen.orientation.lock use (16 inline + 39 external scripts scanned, 1 unreadable) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [classified] (state: Take Assignment, 2026-09-15, reviewer, ~1280 px window at 400 % browser zoom, walkthrough W38): Reviewer 2026-09-15, real 400 % zoom in a ~1280 px window: "nothing is hidden or lost at 400%, but no reflow" — the page keeps its fixed-width layout and needs sideways scrolling to read a line; nothing is cut off, hidden or overlapping, and every control stays reachable.
  - Classified: LV1 / WCAG 1.4.10 / Major → finding V-F19 (confirms O2); LV2 / WCAG 1.4.10, 1.4.4 → pass
- O7 [new] (state: Take Assignment, Problem 3, 125 % default zoom, override applied over CDP, 2026-09-15, assistant): `R083-textspacing-2.png` (the assignment-code box under the Submit / Hint / Feedback / I give up! buttons outlined) — the box is empty: the code "6M79-C9-72-46-B37E-17547" is pushed out of its 35 px-high, overflow-hidden container and is not visible at all. Everything else on the page (problem text, navigator, buttons, grade summary) survives the override. Awaiting the reviewer's ruling on whether the code is content a student needs (W39b).
- O6 [classified] (state: Take Assignment, 400 % zoom, 2026-09-15, reviewer, W42/W44): "images used in the assignments are low resolution and don't scale well at 400, they are blurry." Clarified 2026-09-15: "The blurry images do contain text, usually math." — the figures carry mathematical text as pixels, which MathJax renders as real text elsewhere on the same page, so the image form is not essential.
  - Classified: LV9 / WCAG 1.4.5 / Major (assistant's rating — reviewer to confirm) → finding V-F24
- O8 [classified] (state: Take Assignment and View Printable Assignment, 400 % zoom, 2026-09-15, reviewer, W44): "No new issues are obvious for assignment pages at 400: this can be passed." — focus ring visible, nothing further lost.
  - Classified: LV7 / WCAG 2.4.7, 2.4.11 → pass (LV2 already pass, O5)
- O9 [classified] (state: Take Assignment, Problems 1 and 6, 100 %, 2026-09-15, reviewer, eyedropper, W44): "1 and 6 contain images that fail color contrast as they contain text over a graphic."
  - Classified: LV4 / WCAG 1.4.3 → fail → finding V-F24 (with the 1.4.5 defect; the page's UI text colours are under V-F23)
- O10 [classified] (state: Take Assignment, 100 %, 2026-09-15, reviewer, W44): "Submit button and others pass contrast, Nothing." — the Submit button, palette keys and navigator controls are ≥ 3:1; no hover- or focus-revealed content on the page.
  - Classified: LV5 / WCAG 1.4.11 → pass; LV6 / WCAG 1.4.13 → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- `R083-textspacing.png`, `R083-textspacing-N.png` — the page under the 1.4.12 text-spacing override with each newly clipping container outlined in red (assistant, 2026-09-15, W39b)

## Findings raised from this run

- V-F19 (1.4.10 — recorded under S1); V-F23 (1.4.3 — recorded under S1); V-F24 (1.4.5, 1.4.3 — the figure images, recorded under S3)
