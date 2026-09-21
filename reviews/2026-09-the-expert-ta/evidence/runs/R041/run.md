# Test Run R041 — S6

| | |
|---|---|
| **Run ID** | R041 |
| **Date/time** | 2026-09-11 14:08 |
| **View / sample** | S6 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/calendar.aspx |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe; nvda (reviewer, W64) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-21, every row answered. A calendar exists to say **when** something is due, and that is the one thing this one does not tell a screen-reader user: the assignment's name is announced in the cell where it starts, and its span and end date are carried only by the coloured bar (V-F39) — the same information the no-color run also found lost (R102). Beyond that, the grid cannot be entered from the keyboard at all without a screen reader (V-F38), and opening the event gives a modal that announces nothing, labels nothing, and offers date pickers in place of the dates it is meant to report (V-F40, V-F41). Table navigation and link naming are sound; the content they lead to is not.

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
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Calendar" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O8 — the only visible heading is "September 2026" (O5); there is no heading or landmark route to the grid, and the reviewer reaches it only with `T`: "calendar has to be naved as a table" → V-F1 |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O8, O9 — **"there is no way to tab into the calendar"**; the event announces as the assignment name plus "clickable", which is a state and not a role, on an element that cannot take focus (O7); the modal's controls are date-picker widgets standing in for read-only information → V-F38, V-F41 |
| NV4 — Images announce appropriate alternatives; decorative images are silent | pass | O10 — measured: the view has one image, the site logo, and it carries `alt="The Expert TA"`. Nothing on this view conveys information as a graphic |
| NV5 — Reading order matches the meaning of the visual order | pass | O8 — the reviewer navigates the grid cell by cell with table commands and reports no content out of sequence; what is missing from the cells is a separate row (NV8). Recorded from the narration — say so if an ordering problem was seen and this flips |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | fail | O6, O9 — **"the form fields are not labeled"**. Measured: the modal's `#modal-title` is an editable `input type=text` with no label, no `aria-label` and no `title`; the two filter checkboxes have no name mechanism either → V-F41 |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | fail | O9, O10 — **"no announcement on open"** for the modal and **"month change not announced"**. Measured cause: the page carries **no `role=dialog`, no `aria-modal`, and zero live regions**, so neither change has any mechanism by which it could be announced → V-F40 |
| NV8 — Nothing is conveyed only by visual position, shape, or size | fail | O9 — **"the assignment is not announced as spanning multiple days … we dont hear that the assignment spans or ends on the 8th"**. The event text sits in one day cell while the coloured bar covers the range (O7), so the duration is carried by the bar's visual extent alone → V-F39 |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | pass | O10 — measured: 60 visible links, all with distinct descriptive names, none bare and none pointing two ways. The single unnamed link is the header logo, which is inside `aria-hidden` and so absent from the AT's link list (the V-F29 advisory) |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O9 — the reviewer's ruling: the modal **"looks like a form but is not"** — it presents the assignment's dates rather than collecting input, and no validation was exercised. Recorded n/a on that basis; if the modal does validate anything, it is untested |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R041-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [new] (state: Calendar, September 2026, NVDA, 2026-09-15, reviewer, during W47): "table desc doesn't expose that this is a calendar, T will find the table" — the month grid is a plain table with no caption or accessible name saying it is the calendar; `T` reaches it, but nothing announces what it is. To classify under NV2/NV3 on the full NVDA pass (W64): what does NVDA say on entering the table, and do day cells read with their weekday header?
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "Calendar" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

- O5 [measured] (state: Calendar as loaded, 2026-09-21 — structural scan ahead of the NVDA walk, so the reviewer is not asked what the markup already answers): the view has **14 `h2` elements but only one of them is visible** — "September 2026", the month. The other 13 are `display:none` and are not headings at all in meaning: they are the field captions of a hidden event-detail panel — "Class:", "Title:", "Description:", "Start:", "Due:", "End:", "Publish:", repeated per event. So `<h2>` is being used as a styling device for labels. The reviewer should therefore find exactly one heading with `H`, and if the panel is ever shown, a burst of headings that are really labels.
  - Classified: NV2 — measured input for the reviewer's walk; heading semantics used for presentation → 1.3.1
- O6 [measured] (state: as O5): the two filter checkboxes, `#classFilter-3373` (the class filter) and `#hlpCheckbox`, have **no `label[for]`, no `aria-label` and no `title`** — there is no mechanism by which either could acquire an accessible name. These are the "Select All" / "Only" controls.
  - Classified: NV6 — measured fail awaiting the reviewer's confirmation on focus
- O7 [measured] (state: as O5): the assignment event is a **plain `div`** — no `href`, no `onclick`, no `role`, no `title`, `tabIndex = -1` — sitting as text inside one day cell, whose full text reads "1 Chapter 5 Sample Assignment". Two consequences worth putting to the reviewer. It is **not a link and not focusable**, so it answers W64's first question by measurement. And because the event lives in **one** cell while the coloured bar spans several, the assignment's **duration** is carried by the bar alone — the same information the no-color run found failing "totally" (R102 O3). A screen reader reading the grid cell by cell would meet the title once and nothing on the other days.
  - Classified: NV3, NV8 — measured input; the duration question is the one this view turns on

- O8 [clarified] (state: Calendar, NVDA, reviewer 2026-09-21 — step W64): **"there is no way to tab into the calendar, T enters calendar as its a table … calendar has to be naved as a table."** The month grid is reachable only through table-navigation commands. A keyboard user without a screen reader has no route into it at all, and the pre-walk measurement says why: the event is a `div` with `tabIndex = -1` and nothing else in the grid takes focus (O7).
  - Classified: NV2 / WCAG 1.3.1, 2.4.1 → V-F1; NV3 / WCAG 2.1.1, 4.1.2 / Major → finding **V-F38**; NV5 / pass
- O9 [clarified] (state: as O8, entering the cell where the assignment starts, then activating it): **"when we enter the cell where the assignment starts, we hear the assignment name 'clickable' but we dont hear that the assignment spans or ends on the 8th. If we click the assignment a modal opens, no annoncement on open, the modal looks like a form but is not, the form fields are not labled, there is a start due end date, but they are calendar selection widget and not actually just info on the assignment. Month change not announced."** Four distinct defects in one sequence: the event's **duration is not conveyed**; the modal **opens silently**; its fields are **unlabelled**; and the assignment's dates are rendered as **date-picker widgets** although nothing there is editable in intent.
  - Classified: NV8 / WCAG 1.3.1 / Major → finding **V-F39**; NV7 / WCAG 4.1.3 / Major → finding **V-F40**; NV6 / WCAG 3.3.2 and NV3 / 4.1.2 / Major → finding **V-F41**
- O10 [measured] (state: as loaded, 2026-09-21, confirming the reviewer's report): **no `role="dialog"`, no `aria-modal`, and zero `aria-live` / `role=status` / `role=alert` regions anywhere on the view** — so there is no mechanism by which the modal's appearance or a month change could be announced; the silence the reviewer heard is structural, not a timing artefact. The modal's `#modal-title` is an **editable `input type=text`, not read-only and not disabled**, with no label of any kind. Also measured: one image (the logo, with alt); 60 links, all distinctly named, no duplicates, the only unnamed one being the `aria-hidden` logo link.
  - Classified: NV7 / fail (cause established); NV6 / fail; NV4 / pass; NV10 / pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R041-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
