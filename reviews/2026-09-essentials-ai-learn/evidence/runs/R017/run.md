# Test Run R017 — S3

| | |
|---|---|
| **Run ID** | R017 |
| **Date/time** | 2026-09-30 14:07 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker` (video lesson); Classic experience |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom (probe measurements kept: LV1, LV3 measured fail, LV8; assistant contrast sampling) |
| **Baseline** | B3 |
| **Tester** | assistant (contrast sampling); reviewer completes at 400 % — assistant records |
| **Result** | Not set — LV2, LV4, LV5, LV6, LV7, LV9 need the reviewer (zoom, B3); measured fail on LV3 awaits confirmation |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O2 — at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 305: no horizontal scrolling (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | | |
| LV3 — The view tolerates text-spacing overrides without loss | fail | O3 — text-spacing override applied: 3 container(s) newly clip their text: span "What is AI? Breaking it Down"; span "⚠️ Ask So You Can Check It! ⚠️"; span "Finding Scholarships with AI" (measured) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | pass | O5 — every text ≥ 4.5:1 on solid backgrounds (tightest 4.54:1); nothing unmeasured |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | | |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | n/a | O8 — no custom content on hover or focus (native tooltips only) |
| LV7 — Focus indicator remains visible and unobscured at zoom | | |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (4 inline + 11 external scripts scanned) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O9 — no images of text; text inside the video is video content |

**view_probe 2026-09-30:** answered LV1=pass, LV3=fail, LV8=pass by measurement; facts in `R017-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 305: no horizontal scrolling (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): text-spacing override applied: 3 container(s) newly clip their text: span "What is AI? Breaking it Down"; span "⚠️ Ask So You Can Check It! ⚠️"; span "Finding Scholarships with AI" (measured)
  - Classified: LV3 / WCAG 1.4.12 / measured → fail
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): no orientation media query and no screen.orientation.lock use (4 inline + 11 external scripts scanned) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [new] (state: 1280×1000, 100 %, computed-style sampling — every text on the view sits on a solid background (page, white cards, purple button)): All 70 text samples pass: outline lesson titles 9.4:1, section titles 16.7:1, counts/durations 4.5–5.2:1 (tightest: the "0m" duration labels at 4.54:1), h1 16.7:1, Transcript summary 10.2:1, transcript body 9.4:1, "Complete & continue" white on purple 7.0:1, "Up next" 4.95:1 / 8.9:1. Nothing was unmeasured. Screenshot `R017-icebreaker-1280.png`.
- O6 [new] (state: text-spacing override injected (line-height 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) — screenshot `R017-icebreaker-text-spacing.png`): The outline's lesson titles are single-line with `overflow:hidden; text-overflow:ellipsis` **by design** — long titles are already truncated at default spacing ("How AI is Changing the Way St…"). Under the override 14 of 21 titles truncate (the probe counted the 3 *newly* truncated ones as the measured LV3 fail). Nothing else on the view clips or overlaps; the lesson body, video, transcript and buttons are intact. The full title is always available as the lesson page's h1 once opened. **Reviewer rules LV3:** does ellipsis-truncation of outline titles that are already truncated by design count as loss of content under 1.4.12?
- O7 [new] (state: inspection + measurement (LV5 facts)): Components: outline buttons are text on white with a lavender highlight for the current lesson; the progress bar is a thin track (grey) with a purple fill at 0 %; the video control bar is user-agent; the Transcript disclosure is text + icon; "Complete & continue" is a filled purple button. Focus ring lilac ≈ 2.1:1 on white (AA requires visibility only).
- O8 [new] (state: inspection): `title` attributes exist on "Hide lessons" ("Hide lesson list") and on the video ("Icebreaker") — native tooltips only; no custom hover/focus content.
- O9 [new] (state: inspection): No `<img>` on the view. The video shows its own on-screen titles ("Best Friday Ever…") and open captions as part of the picture — video content is exempt from 1.4.5; the burned-in captions' legibility at zoom is the reviewer's 1.4.4 note (03 §2.6).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (zoom instrument, partial).** LV2, LV5, LV7 and the LV3 ruling stay with the reviewer at 400 % (open the outline, play a few seconds of video to see the burned-in captions at zoom).

## Evidence files in this folder

- (screenshots/exports named R017-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
