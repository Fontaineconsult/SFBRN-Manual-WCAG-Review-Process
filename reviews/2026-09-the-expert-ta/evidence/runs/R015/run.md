# Test Run R015 — S1

| | |
|---|---|
| **Run ID** | R015 |
| **Date/time** | 2026-09-10 11:17 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | T1 |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA 2026.2); assistant records |
| **Result** | Broken |

**Result reasoning.** 2026-09-14, every row answered at the time; **NV10 was reopened 2026-09-21** (O15 — the empty links-list dialog it rested on proves nothing) and does not bear on this verdict, which stands on O10 and O12. Broken for this page on its own: the assignment row's action menu — the page's core function — is mouse-only (O10) and, once opened, is not announced (O12), so a screen-reader user cannot open an assignment here. The reviewer accepts the Accessibility Mode page as the alternate route (T1 verdict Pass with barriers, T1-F3 Minor); that ruling is about the task, not this view — the standard page itself does not work without vision.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Class Management" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O6 — no headings (`H`), no landmarks (`D`), NVDA+F7 offers no route; same as S2 (R016 O2). V-F1 confirmed on S1 |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O8 (Classes / Class Menu editors: an instruction sentence as the name, no label); O10 (the assignment row's action menu is not focusable — no control exists for the keyboard); O11 (two table expand controls announce "collapsed graphic clickable" — no role, no name) |
| NV4 — Images announce appropriate alternatives; decorative images are silent | pass | O11 — the only meaningful graphic, the logo, has alt text; the two expand graphics are controls without names (an NV3 defect, not an alternative-text one) |
| NV5 — Reading order matches the meaning of the visual order | pass | O7 — arrowing down follows the expected order (header → menu → Classes → Class Menu → assignments → news) |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | fail | O8 — the two editors carry the instruction text as their name; the visible captions "Classes:" / "Class Menu:" are not announced; the reviewer learns each editor's purpose only on reaching the adjacent Go button. V-F7 confirmed on S1 |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | fail | O12 — opening the row's ⋮ menu (mouse, the only way — O10) is not announced; the items are announced only on mouse-over. Nothing tells a screen-reader user a menu appeared |
| NV8 — Nothing is conveyed only by visual position, shape, or size | fail | O7 — the two grids' captions and column headers are not meaningful for Class Management vs Class News; the tables are told apart by position. V-F2 confirmed on S1 |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | | **Reopened 2026-09-21** (was n/a on O13). O13 read an empty NVDA links-list dialog as "nothing is exposed as a link". That inference is unsafe: O14 shows the header logo announcing as a **link** on focus, and the tab-order measurement (R001 O11) finds six more `<a>` elements at stops 2–7 that are not `aria-hidden` at all. Whatever the dialog was showing, it was not the page's link inventory. The row needs the method the process already mandates — confirm on focus, not from an elements list → W72 |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | the view has no validated input of its own; the Class Menu popup forms are S11 (R077) |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R015-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "Class Management" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass
- O5 [clarified] (state: arriving from Accessibility Mode via "Non-Accessibility Page", 2026-09-14, NVDA 2026.2): page-load announcement and `NVDA+T` both give "Class Management" (Accessibility Mode gives "Class Management Accessibility Mode").
  - Classified: NV1 / pass (confirms O3's wording on the walk)
- O6 [clarified] (state: as loaded): `H` finds no heading, `D` no landmark, NVDA+F7 offers no route to the content — the same as the Accessibility Mode page (R016 O2).
  - Classified: NV2 / WCAG 1.3.1 / Major → V-F1 now confirmed on S1 (was "also S1 per axe R001")
- O7 [clarified] (state: browse mode, arrowing from the top): the reading order is the expected one. The two grids' captions and column headers are not meaningful for telling Class Management (assignments) from Class News; the tables are told apart by position, as on S2.
  - Classified: NV5 / pass; NV8 / WCAG 1.3.1 / Minor → V-F2 confirmed on S1
- O8 [clarified] (state: Tab to the Classes editor, then the Class Menu editor): each announces a long instruction sentence on focus; neither has a meaningful label of its own ("not really" distinguishable without the screen). Tabbing on to the adjacent Go button is where the reviewer first hears what the dropdown is for. Standard-mode Go buttons are as narrated by the reviewer — the exploration record showed only the two DevExpress editors (R001 O1); the assistant will read the DOM when the tab is free.
  - Classified: NV3, NV6 / WCAG 1.3.1, 2.5.3, 4.1.2 / Major → V-F7 confirmed on S1
- O9 [clarified] (state: Tab from the top, and the jump-point stop): the first Tab stop reads the visually hidden div of accessibility instructions ("Use the tab key to progress through actionable items…"), the same hidden div as on S2; the jump point "reads exactly what is in the div" — text, no control name.
  - Classified: NV3 / folded into V-F8 (jump point announces its instruction text as its name); 2.4.1 for S1 — the first stop is instruction text, not a skip (MO11 on R022 to confirm what Enter does)
- O10 [clarified] (state: Class Assignments table, "Chapter 5 Sample Assignment" row, keyboard only): the standard-mode table is different from Accessibility Mode — there is **no Actions select and no Go button in the row**. Nothing in the row is focusable; Enter, Space and the Applications key do nothing. "Only way to nav is by clicking the table row" — the row's action menu (⋮) opens by mouse click only. The screen-reader user cannot reach "Take Assignment" from this page; the route exists only on the Accessibility Page (R016 O13).
  - Classified: NV3 / WCAG 2.1.1 (Level A), 4.1.2 / **Major** (Blocker for this page alone; the Accessibility Page is the vendor's alternate route — reviewer rules whether the alternate-version argument holds) → finding **T1-F3** (task T1 fails at step 3 in standard mode)
- O11 [clarified] (state: `G` next graphic): the only meaningful graphic is the site logo, which has alt text. Two further stops announce "collapsed graphic clickable" — the + expand controls of the two grids: clickable graphics with no role and no name.
  - Classified: NV4 / pass for the logo; NV3 / WCAG 4.1.2 / Minor → finding **V-F16** (unnamed, role-less expand controls)
- O12 [clarified] (state: ⋮ menu opened with the mouse, NVDA running): "No announcement when the ⋮ menu is selected by NVDA, but items are announced when moused over." The menu's appearance is silent; only pointer hovering reads its items.
  - Classified: NV7 / WCAG 4.1.3 (no status message for the opened menu), 4.1.2 / folded into **T1-F3** (the menu is neither operable nor announced without a mouse)
- O13 [clarified] (state: NVDA+F7 → Links): "links do not show up in link list" — the list is empty. The top menu, the row actions and the expand controls are not links; the logo link is `aria-hidden`.
  - Classified: NV10 / n/a (nothing exposed as a link to judge); the missing semantics are already T1-F3 / V-F16

- O14 [clarified] (state: Class Management standard mode, NVDA, tabbing in from the address bar, 2026-09-21 — step W71): at the 8th Tab stop, the `aria-hidden="true"` header logo link, NVDA announces **"The ExperTa graphic visited link"**. Name (the image's alt), role (link) and state (visited) are all spoken. The assistant had predicted silence from the markup — `aria-hidden` should remove the subtree from the accessibility tree — and the screen reader contradicts it: in NVDA + Chrome the focused element is announced regardless. **The reviewer's AT wins** (CLAUDE.md instrument hierarchy). V-F29 is withdrawn on this observation; the markup defect survives as an advisory only.
  - Classified: NV3 / **pass** for this control (name, role and state exposed) → **V-F29 withdrawn**; and it invalidates O13's reading of the links list → NV10 reopened
- O15 [clarified] (state: as O14): O14 also settles what the empty links-list dialog of 2026-09-14 (O13) meant — **not** that the page has no links. The logo is a link and is announced as one on focus; six further `<a>` elements sit at Tab stops 2–7 (theExpertTA.com, My Account, Log Out, Class Management, Instructor, Help) and none of them is inside `aria-hidden` (R001 O11). The dialog was not showing the page's links, for a reason this run has not established. Nothing may be concluded from its emptiness.
  - Classified: NV10 reopened; the earlier n/a is superseded, not merely amended

## Notes

2026-09-21 — W71 answered. The reviewer's NVDA overturned a finding the assistant had raised from markup (V-F29, withdrawn) and, with it, the basis of this run's NV10 answer. Both corrections are recorded above rather than edited away: O13 stays on the record with O15 explaining why its inference does not hold.

2026-09-14 — Reviewer narration (NVDA 2026.2, standard mode confirmed: the tab was on `default2.aspx` at the start and the reviewer switched with "Non-Accessibility Page"; answers on the table shape and the absent Go button confirm the page). Assistant asked before recording because the first narration matched Accessibility Mode features; reviewer clarified: the hidden instruction div still appears on this page, the table is different, there is no Go button, and the row is mouse-only. Open questions for NV7 and NV10 are in the rows.

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R015-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
