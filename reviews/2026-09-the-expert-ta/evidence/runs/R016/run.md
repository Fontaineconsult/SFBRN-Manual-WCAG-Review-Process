# Test Run R016 — S2

| | |
|---|---|
| **Run ID** | R016 |
| **Date/time** | 2026-09-10 12:09 |
| **View / sample** | S2 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default2.aspx |
| **Task / process** | T1 |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA 2026.2, baseline B5); assistant records |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O1 — title "Class Management Accessibility Mode" announced on load and on NVDA+T |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O2, O3 — no headings (H), no landmarks (D); section titles are focusable divs; both grids share one generic caption. Column header IS announced per cell ("row 3 Actions column 1") — headers are associated |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O4 (skip links: link role, wording), O5 (title divs), O10 (Actions select unnamed), O11 (top selects: identical instruction as name, visible captions not announced), O12 (jump point: unnamed, Enter only toggles "No Shortcuts"); O9 (Go/table nav with NVDA) unresolved |
| NV4 — Images announce appropriate alternatives; decorative images are silent |  | not narrated (W6 skipped — logo image, ⊞ expand icons); ask at session end |
| NV5 — Reading order matches the meaning of the visual order |  | not narrated (W6 skipped); ask at session end |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | fail | O7 (popup forms unlabeled), O11 (Classes / Class Menu selects: visible labels "Classes:" / "Class Menu:" not announced; both share one instruction text as their name) |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | pass | O13 — Actions → Take Assignment → Go: page change announced ("Take Homework Assignment") |
| NV8 — Nothing is conveyed only by visual position, shape, or size | fail | O3 — the two grids are distinguishable only by position/order (identical captions) |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | lang="en"; no pronunciation issue reported |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [clarified] (state: Class Management, **Accessibility Mode** `default2.aspx`, class selected, one assignment row): page load and NVDA+T both announce "Class Management Accessibility Mode".
  - Classified: NV1 / 2.4.2 / pass
- O2 [clarified] (state: as O1): `H` reports no next/previous heading; `D` reports no next/previous landmark; the NVDA elements list (NVDA+F7) offers no route to the content — reviewer reaches the main content by `T` (next table) or by tabbing. Confirms R005 O4 (axe: 0 headings, 0 landmarks) — axe was not instrument-blind (W3 of R005 → pass).
  - Classified: NV2 / WCAG 1.3.1 (visible section titles are not headings), 2.4.1 (no landmark/heading bypass) / Major → finding V-F1
- O3 [clarified] (state: as O1): pressing `T` announces "Data table related to the headers above, table clickable with x rows and x columns" for **both** grids — the same generic caption — so the reviewer cannot tell whether the Class Assignments or the Class News table is selected. Tabbing into the area announces "Class Assignments" / "Class News" (the focusable title divs, `#assignmentsTitle` `tabindex=0`), which is how the tables are told apart. Each DevExpress grid is split into a "Headers for the data table below" table and a "Data table related to the headers above" table, i.e. column headers and data cells live in different tables. Reviewer: "the table is announced and I can navigate it successfully."
  - Classified: NV2 / WCAG 1.3.1 / **Minor** (revised 2026-09-10) → finding V-F2. Answer: on Tab into the table the generic description is read and no header names are listed, but per-cell navigation does announce the column header ("row 3 Actions column 1" — Speech Viewer, O10). So headers are associated; the defect is table identification (identical captions) and the entry announcement.
- O4 [clarified] (state: as O1): the skip mechanism "Tab for Assignments, Enter to skip. To navigate Assignments table…" is exposed as a **link** (`href="javascript:skipper('News')"`) but is not a link; activating it "doesn't seem to do anything". Same for "Tab for Class News, Enter to skip".
  - Classified (revised 2026-09-10): **the skip links work** — activating "Tab for Assignments, Enter to skip" moves focus to the next skip link ("Tab for Class News, Enter to skip"), i.e. it skips the assignments section. Remaining defects: exposed as links (`href="javascript:…"`) rather than buttons, and wording that reads as an instruction rather than a control ("Tab for Assignments, Enter to skip" = press Enter to skip the assignments). NV3 / WCAG 4.1.2 / **Minor** → finding V-F3 (rewritten); 2.4.1 is **met on this page** by these links plus the top-of-page jump point.
- O5 [clarified] (state: as O1): section titles are `div tabindex="0"` wrapping a coloured `<b>` span (reviewer pasted `#assignmentsTitle`): focusable, no role, not headings; the reviewer described the pattern of using links and focusable divs as page-navigation elements as "strange".
  - Classified: NV3 / folded into V-F1 (heading semantics) — a focusable div with no role is a tab stop that announces as plain text
- O6 [clarified] (state: Class Menu → a popup item opened (DevExpress popup iframe: Create Class / Edit Class / Registration / Create News / Copy)): the popup "can't be escaped out of" with the keyboard.
  - Clarified 2026-09-10: opened Create Class, Edit Class, Create News (and others). Each popup has a Close/Cancel button that is exposed and works; **Esc does not close** the popup. Focus can leave via the button, so this is **not a keyboard trap** (2.1.2 requires an exit by standard keys, which exists). Recorded as advisory only (Esc-to-close is convention, not a WCAG requirement; whether NVDA announced a dialog role is still unknown — ask in the S11 run). → V-F4 **withdrawn**; 05 2.1.2 reverted to Not Evaluated.
- O7 [clarified] (state: as O6): the popup form is laid out as a table; inputs do not appear to be labelled; the "labels" are text in an adjacent table column. Confirms R002 O1 (axe: 6 unlabeled inputs on eClass.aspx).
  - Classified: NV6 / WCAG 1.3.1, 3.3.2, 4.1.2 / Major → finding V-F5
- O8 [new] (state: session start): the account was **already in Accessibility Mode** when the reviewer loaded the page (the assistant had restored standard mode at 10:49). Someone toggled it in between (shared account) or the reviewer did. The S1 standard-mode pass (R015) is still owed.
  - Answered 2026-09-10: **yes, the reviewer switched to Accessibility Mode** before W4. No third-party change to the shared account.
- O9 [new] (state: as O1, Class Assignments data table): on Tab into the table NVDA lands in the first data row on the row's Actions combo box; the reviewer can pick an option and Tab to the row's **Go** button, but from Go neither NVDA table navigation (Ctrl+Alt+arrows) nor arrow keys move to column 2 and beyond — "the GO button appears to be a trap". Tabbing past the table and Shift+Tabbing back lands in the **last** column, from where arrowing around the table works.
  - Assistant hypothesis (asked): NVDA focus mode after the combo box. Reviewer's retry 2026-09-10: **with NVDA turned off, keyboard navigation of the grid works** (the grid's own arrow-key scheme — "left arrow to go left, right arrow to go right" per the page's instruction text). So keyboard-only (motor) is fine here; with NVDA running the arrow scheme is not usable from the Go button. Whether `NVDA+Space` (focus mode, arrows passed to the grid) resolves it was not tried. Classified: not a finding yet — carried to the S2/S3 no-vision follow-up as "grid arrow-key scheme vs. screen-reader modes"; note for the report that DevExpress grids require the user to know to switch NVDA modes.
- O10 [clarified] (state: as O1): Speech Viewer on tabbing into the row: "Create Assignment  Go  Assignment Menu - Click To Activate  row 3  Actions  column 1  combo box  Create Assignment  collapsed". Reading: cell content is spoken first ("Create Assignment Go Assignment Menu - Click To Activate"), then the position and column header ("row 3, Actions, column 1"), then the control ("combo box, Create Assignment, collapsed"). The combo box therefore has **no name of its own** (confirms axe `select-name`, R005 O1); NVDA's cell reading supplies "Assignment Menu - Click To Activate" from nearby text, which a focus-mode Tab would not read.
  - Classified: NV3 / WCAG 4.1.2 / **Minor** (revised from Major — the cell text mitigates in browse mode) → folded into V-F5's family? No — kept as its own item under V-F6.
- O11 [clarified] (state: as O1, top of page): Tab to the first `<select>` — Speech Viewer: "First make your selection here and then click Go button to confirm your choice.  combo box  Testing Course for CSU East Bay  collapsed". The second select announces the same instruction sentence. The visible captions "Classes:" and "Class Menu:" are **not announced**; both controls carry the identical instruction as their accessible name, so a screen-reader user cannot tell which select is which except by its current value.
  - Classified: NV3, NV6 / WCAG 1.3.1 (visible label not associated), 2.5.3 (visible label text not in the accessible name), 4.1.2 / **Major** → finding V-F7
- O12 [clarified] (state: as O1, first tab stop region): the top-of-page jump point (`#top_of_page_jump_point`, `div role=button tabindex=0`, no name): pressing Enter switches its text to "No Shortcuts" and does not navigate anywhere on this page — no shortcuts menu opened.
  - Classified: NV3 / WCAG 4.1.2 (button without an accessible name; state change without a name) / **Minor on this page** (may rise on Take Assignment where the menu is expected — W11) → finding V-F8 (product-wide family: R001 O2, R004–R014 `aria-command-name`)
- O13 [clarified] (state: row Actions select → "Take Assignment" → Go): NVDA announced the page change, "Take Homework Assignment". Task T1 step 3 completed in Accessibility Mode.
  - Classified: NV7 / pass; T1 step 3 → S3 run R017

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

2026-09-10 — Reviewer narration (NVDA 2026.2, Chrome 153 debug profile). Exact Speech Viewer excerpts still to be pasted for O3 ("Data table related to the headers above, table clickable with x rows and x columns") and O4. Result not set until NV4/NV5/NV7–NV9 are covered (W6–W8 on this page).

## Evidence files in this folder

- (none yet — Speech Viewer excerpt for O3/O4 requested)

## Findings raised from this run

- V-F1, V-F2, V-F3 (revised), V-F5, V-F6, V-F7, V-F8 (04 §B); V-F4 withdrawn; T1-F1 (04 §A, revised)
