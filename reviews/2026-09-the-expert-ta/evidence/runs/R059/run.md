# Test Run R059 — S12

| | |
|---|---|
| **Run ID** | R059 |
| **Date/time** | 2026-09-11 14:09 |
| **View / sample** | S12 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373 |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W53/W65, complete 2026-09-24) |
| **Baseline** | B5 |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-24, every row answered. Broken was already established on 2026-09-15 by **V-F28** — this is a student-facing page whose content cannot be reached by keyboard and cannot be found with a screen reader. The rows completed since do not soften it: `G` stops on anonymous decoration (O8), 27 uncaptioned layout tables make position unknowable (O9), and every selection re-reads the entire page identically so the user is never told what changed (O10). What does work — reading order, link purpose, nothing carried by position — works in a page the user cannot operate.

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
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Student Practice Area" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O3 — "no headings, no tabs"; the practice content sits in nested tables with no captions (reviewer; markup confirms 0 headings, 0 captions) → V-F1, V-F28 |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O3 — "the expand buttons are not appropriately labeled": the expand control is an image with an onclick, no role; the checkboxes are spans (reviewer + markup) → V-F28, V-F16 |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O8 — `G` walks onto graphics that say nothing about themselves: first "table with x columns and x rows", then images the reviewer could only describe as "what appears to be the YouTube thumbs … there is no information about what they are, just generic graphic". Measured: they are **DevExpress UI sprites** (`DXR.axd`) with `alt=""`, `alt="v"` or `alt="[Collapse]"` — decoration that should be silent, exposed instead as anonymous graphics → V-F16 |
| NV5 — Reading order matches the meaning of the visual order | pass | O9 — "the order makes sense", with the reviewer's qualifier recorded: "their use of tables for layout makes moving through confusing since the tables are not well labled". Measured: **27 tables on the view and not one caption**. The sequence is right; what is missing is any signal of where you are in it → V-F2, V-F5 |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | fail | O3 — "no forms have labels" (reviewer; axe R011: 12 unlabeled fields; markup: 0 `<label>`) → V-F5 |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | fail | O10 — choosing a book re-announces **the whole page** rather than what changed, and "its always the same thing" whichever selection is made: document, form landmark, table, then the entire menu chain, twice. Measured: **zero live regions** on the view, so the update is a full re-render with nothing marked as the status message → V-F42 |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O9 — reviewer 2026-09-21: "nv8 no" — nothing is identifiable only by where it sits |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | pass | O9 — reviewer 2026-09-21: "nv10 no" — no link announces a purpose that could not be acted on |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O9 — reviewer 2026-09-21: "no input validation" on this view |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R059-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [classified] (state: Student Practice Area, NVDA, 2026-09-15, reviewer, W53 narration): "this page is hard to navigate, none of the tables of descriptions, the sections table requires an expansion to view the content, but the expand buttons are not appropriately labeled, no forms have labels, no headings, tabbing focus is lost outside of the initial buttons and dropdowns, their ctrl alt 1 doesn't do anything. can't tab into the check boxes, there is no obvious way to find the tutorial content, no headings, no tabs, they are in a table". Markup facts from the table the reviewer saved (`R059-sections-table.html`, 22 KB): 4 nested tables, 0 `<caption>`, 0 `<th>`, 0 headings, 0 `<label>`, 0 ARIA roles; the expand control is an `<img alt="[Collapse]">` with an `onclick` and no role or tabindex; the checkboxes are `<span class="dxWeb_edtCheckBoxUnchecked">` DevExpress spans, not `<input>` elements, so nothing in the grid can take keyboard focus; the section title "Problems to Help Students Learn Expert TA" is plain text. Note for later: the first practice problem's text says "Please watch the following brief video" — a video may exist inside the problem once opened (the probe saw no media on the page as loaded; NV11/NH1 to re-check on W65).
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 → fail → V-F1 (extended to S12), V-F28; NV3 / WCAG 4.1.2, 2.5.3 → fail → V-F28 (and V-F16 for the expand image); NV6 / WCAG 3.3.2 → fail → V-F5 (extended to S12)
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "Student Practice Area" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

- O8 [clarified + measured] (state: Student Practice Area, NVDA, reviewer 2026-09-24 — step W65): **"first G does something im not expecting … pressing G puts us into the table in the grid and pressing G i hear 'Table with x colums and x rows', pressing it again enters the what appears to be the YouTube thumbs, but there is no information about what they are, just generic graphic."** The reviewer's hedge is the finding: they could not tell what the graphics were. Measured on the state they were in — **they are not video thumbnails**. The view's 26 `img` elements are all DevExpress interface sprites served from `DXR.axd`, carrying `alt=""`, `alt="v"` or `alt="[Collapse]"`, and **the page contains no `iframe`, no `video`, no `audio`, and not one occurrence of "youtube" or "video" in 111 KB of HTML**. So `G` is stopping on decoration that should be silent and announcing it as an anonymous graphic, which is exactly why it cannot be identified.
  - Classified: NV4 / WCAG 1.1.1, 4.1.2 / Minor → **V-F16** (decorative sprites exposed as unnamed graphics)
- O9 [clarified] (state: as O8): **"the order makes sense but their use of tables for layout makes moving through confusing since the tables are not well labled, they use forms here but not proper `<form>` tag … nv8 no, nv10 no, no input validation."** Measured alongside: **27 tables, none with a caption**, and a single real `<form>` element with no `role=form` anywhere — so the "form landmark" the reviewer hears is the one ASP.NET wrapper around the entire page, not a labelled grouping of the controls.
  - Classified: NV5 / pass (with the layout-table qualifier → V-F2, V-F5); NV8 / pass; NV10 / pass; NV12 / n/a
- O10 [clarified + measured] (state: as O8, after choosing a book): the reviewer pasted what NVDA says on update — *"Potential Energy and Mechanical Energy / Student Practice Area document / form landmark / table / Class Management Instructor Help Library Take Tutorial Assignment Take Tutorial Assignment Clear Selection Clear Selection Sections row 1 column 1 / table / … row 2 column 2"* — and the key remark: **"that is what is announced on update, its always the same thing."** The whole page is re-read, including the menu chain, twice, and it is identical whichever selection was made, so nothing in it tells the user what changed. Measured: **zero `aria-live`, `role=status` or `role=alert` regions** on the view. The update is a full re-render with no status message.
  - Classified: NV7 / WCAG 4.1.3 / Major → finding **V-F42**
- O11 [measured] (state: as O8, 2026-09-24 — closing out the media question this view has carried since 2026-09-15): the page holds **no media of any kind** — no `iframe`, `video`, `audio`, embed or YouTube reference. The "watch the following brief video" the reviewer reported on 2026-09-15 therefore belongs to the **practice problem reached through "Take Tutorial Assignment"**, which is a different page and is **not in the sample**. The probe's NH1–NH4 and NV11 `n/a` on *this* view stand; the media question moves to a scope item rather than a reopened row.
  - Classified: NV11, NH1–NH4 / n/a confirmed for this view; the unsampled practice problem recorded in `03` §2.6

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- `R059-sections-table.html` — the sections grid's markup, copied by the reviewer 2026-09-15 ("ive copied the html of the table in to table.html for your inspection")

## Findings raised from this run

- V-F28 (2.1.1, 2.4.7, 1.3.1, 4.1.2 — recorded under S12); V-F1, V-F5, V-F16 extended to this view
