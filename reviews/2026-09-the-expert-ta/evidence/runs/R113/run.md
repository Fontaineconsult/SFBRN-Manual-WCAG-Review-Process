# Test Run R113 — S13

| | |
|---|---|
| **Run ID** | R113 |
| **Date/time** | 2026-09-15 13:07 |
| **View / sample** | S13 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W69) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — NV2, NV3, NV4, NV5, NV6, NV7, NV8, NV10, NV12 need the reviewer (jaws, B1) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "View Printable Assignment" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O5 — reviewer 2026-09-21: "no headings, uses the custom hidden accessibility menu". Measured: **0 headings, 0 `role=heading`**. The Solutions page's outline is not here, so there is no structural way to reach a problem → V-F1, V-F8 |
| NV3 — Every control announces an accurate name, role, and value/state | | |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O6 — "only a few of the images have proper alt text, other 'images' don't seem to register as images at all and have no right click". Measured: of 14 figures, **4 carry real descriptions**, 6 have no `alt`, 4 have empty `alt` — and **2 are CSS `background-image` on a `div`**, which is why they are not images to the AT at all → V-F36 |
| NV5 — Reading order matches the meaning of the visual order | pass | O5, O7 — "the order is fine". Recorded with the reviewer's qualifier: "the page has not been optimized, many 'blank' voicings" — 13 empty layout-table cells are announced as blank while reading (O7 → V-F37). The sequence is right; the noise sits inside it |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | n/a | O7 — measured 2026-09-21: no visible input, select or textarea; the view is a read-only rendering of the problems |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | | |
| NV8 — Nothing is conveyed only by visual position, shape, or size | | |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | | |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O7 — measured: no form fields, so no validated input to submit |

**view_probe 2026-09-15:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R113-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-15 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-15 view_probe): document.title = "View Printable Assignment" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-15 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

- O5 [clarified] (state: View Printable Assignment, NVDA, reviewer 2026-09-21 — step W69): **"no headings, uses the custom hidden accessibility menu … the order is fine, but the page has not been optimized, many 'blank' voicings."** Measured alongside: **0 headings and 0 `role=heading`** on the view. This is the answer to the question the step existed to ask — the Solutions page's per-problem outline is **not** replicated here, so this page offers no structural route to a problem either, only the same unnamed jump-point mechanism as everywhere else.
  - Classified: NV2 / WCAG 1.3.1, 2.4.1 / Major → V-F1, V-F8; NV5 / pass
- O6 [clarified + measured] (state: as O5): **"only a few of the images have proper alt text, other 'images' don't seem to register as images at all and have no right click."** Measured, and the page turns out to do three different things with its 14 figures: **4 carry real descriptive alternatives** (“A red block with mass m rests on a frict…”, “The image shows a car stuck in the mud o…”) — proof the vendor writes good alt text when it writes any; **6 have no `alt` attribute**; **4 have empty `alt`**; and **2 are not `<img>` elements at all** but `div`s painted with a CSS `background-image` (`/images/x3j4awcq.tk5.png`, `/images/r3fze21y.3sa.png`). The last pair is exactly what the reviewer describes — no `G` stop, no right-click, because a CSS background is not in the accessibility tree and **cannot be given alternative text without changing the markup**.
  - Classified: NV4 / WCAG 1.1.1 / Major → finding **V-F36**
- O7 [measured] (state: as loaded, 2026-09-21): no visible input, select or textarea. The "blank voicings" the reviewer reports are located: **13 of the view's 73 table cells are empty**, and no interactive control on the page lacks a name (0 of 157 focusable stops are unnamed). So the blank announcements come from empty *layout* table cells being read as content, not from unnamed controls.
  - Classified: NV6 / n/a; NV12 / n/a; the empty cells → finding **V-F37**

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R113-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
