# Task-Based Testing — The Expert TA

WCAG-EM 2.0 step 4: evaluate the selected sample set. Testing clusters around
the **tasks** (user stories / complete processes from `03-scope-and-sample.md`
§3.3), so findings read as *"this task fails at this step, because of these
WCAG criteria."* The per-criterion rollup in `05-results.md` cites the finding
IDs recorded here — record each finding once, here only.

Evaluation is against all five WCAG 2 conformance requirements at the target
level (WCAG 2.2 AA): (1) conformance level, (2) full pages, (3) complete
processes, (4) only accessibility-supported ways of using technologies,
(5) non-interference.

**Finding IDs:** `T<task>-F<n>` for task findings (T1-F2 = task 1, finding 2);
`V-F<n>` for view-sweep findings.

**Severity:** **Blocker** — the task cannot be completed by an affected user
group; **Major** — completion is substantially burdened; **Minor** — barrier
with a reasonable workaround.

**Task verdicts:** **Pass** — completable by all baseline combinations without
significant barriers; **Pass with barriers** — completable, but Major or Minor
findings exist; **Fail** — not completable by at least one affected user group
within the accessibility support baseline.

**Test runs & evidence:** every test session is logged as a run *before*
testing starts:

```
python scripts/review.py log-test <review> --view S1 --url <page-url> \
    --modality no-vision --tool jaws --baseline B1 [--task T1] [--tester NAME]
```

This records which page/view was tested, when, with which tool and baseline
(the WCAG-EM "evaluation specifics" record), appends to `evidence/test-log.md`,
and creates `evidence/runs/R###/` with a `run.md` for notes — JAWS
action/announced/expected notes or WAVE summary counts — and the run's
screenshots/exports (`R###-*.png`). Capture conventions per tool:
`ontology/testing-tools.md`. Findings below cite run IDs and files in their
**Evidence** row.

---

## A. Task clusters (WCAG-EM step 4.2 — complete processes)

One cluster per process in 03 §3.3. Walk the default sequence, then each
branch sequence, with each baseline combination (03 §1.3). Evaluate the
content that changes along the process — form and dialog interaction, input
confirmations, error messages, and other feedback are all in scope.

### Task T1 — Open an assignment and read a problem — process P1

| | |
|---|---|
| **User story** | As a student, I need to reach my class, open an assignment, and read a problem (text, math, figure) so that I can learn and work the material. (F1) |
| **Verdict** | Not run |
| **Baselines run** | B5 (NVDA) on S2 — R016; B5 on S1 pending (R015); B2, B3 pending |
| **Date(s) tested** | 2026-09-10 |

**Sequence notes:** (verdict stays Not run until steps 4–5 are walked; no-vision on S2 so far points to Pass with barriers) 2026-09-10, NVDA, Accessibility Mode (S2): step 1 sign-in not walked (already signed in). Step 2 Class Management: title fine (R016 O1); no headings/landmarks, the skip links are inert, and the two grids share one generic caption — the reviewer reaches the assignments table by `T`/Tab and identifies it by the focusable title div (R016 O2–O5). Step 3 (Accessibility Mode): row Actions select → "Take Assignment" → Go; page change announced (R016 O13) — completable. The Classes / Class Menu selects at step 2 are not distinguishable by name (V-F7). Step 4 (R017): problem links work with `K`/Enter but focus does not move into the activated problem and there are no headings to find it (T1-F2); the hidden problems jump point mounts a shortcuts menu only after Enter, and NVDA users must switch to browse mode to use it (V-F8). Step 5 pending.

#### Finding T1-F1

| | |
|---|---|
| **Where** | Step 2, Class Management in Accessibility Mode (S2) — reaching the assignments table |
| **Observed** | A screen-reader user arriving on the page has no headings (`H`) and no landmarks (`D`) to move by. The two data grids are reachable with `T` but carry the same generic caption ("Data table related to the headers above"), so the user cannot tell the assignments table from the news table until tabbing onto a focusable title div. The page's skip links do work (revised 2026-09-10: Enter moves focus to the next section's skip link) but are exposed as links with instruction-like wording. Task remains completable (reviewer: "I can navigate it successfully") by linear reading, the skip links, or table-key trial. Details: V-F1, V-F2, V-F3. Open: whether table navigation from the row's Go button works in browse mode (R016 O9). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1, 4.1.2 |
| **Severity** | Major |
| **Evidence** | R016 (O2–O5); R005 `R005-axe.json` (0 headings / 0 landmarks, link-shaped skip) |

#### Finding T1-F2

| | |
|---|---|
| **Where** | Step 4, Take Assignment (S3) — moving from the problem navigator into a problem |
| **Observed** | The problem links ("Problem N Click To Activate") are reachable with `K` and activate the problem, but focus stays where it was; the activated problem's content is not focused and the page has no headings, so a screen-reader user has no structural way to find the problem they just opened. The vendor's alternative — a visually hidden "Press tab to go to problems. Press enter to open the accessibility shortcuts menu" button that mounts jump links on Enter — requires discovering a hidden tab stop and, under NVDA, a mode switch (V-F8). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 2.4.3, 1.3.1 |
| **Severity** | Major |
| **Evidence** | R017 O1, O2 |

---

### Task T2 — Answer and submit a problem — process P2, implements F2 and F8

| | |
|---|---|
| **User story** | As a student, I need to enter an answer with the part's widget (multiple choice, numeric with keypad, symbolic expression, drag-and-drop ranking, free-body diagram), submit it, and perceive the result, using hints or feedback when stuck. |
| **Verdict** | Fail |
| **Baselines run** | B5 (NVDA) on S3 — R017 (steps 1–3, multiple choice); B2, B3 pending |
| **Date(s) tested** | 2026-09-10 |

**Sequence notes:** 2026-09-10, NVDA, S3 Problem 9 (multiple choice): step 1 select an option — possible; text options are heard, math options are not (V-F11). Step 2 Submit — a dialog opens and voices correct/incorrect with further options; focus moves to its close control (R017 O10) — works. Step 3 result perceivable — yes via the dialog. Read-back of the chosen answer (Ctrl+Shift+2) unusable for math (V-F9). Branch P2-b (symbolic, Problem 2 a): typing `m*a` and Submit works; "Submission Details" dialog announces Correct Answer and offers Continue / Close controls with proper names; Tab from the field goes straight to Submit (palette not in tab order — keyboard symbol entry still to check, W20); the field itself carries no label identifying it as F_NET (V-F13). Ctrl+Shift+1 goes to the top jump point, not the previous part (R017 O13). Branch P2-c (drag-and-drop ranking, Problem 3): an alternative form (exposed "Show drag and drop accessibility table" button, focus moves into a Bucket/Order/Item table with combo boxes) makes the ranking operable without dragging; placements are not announced and the Ctrl+Shift+2 read-back runs items together (V-F14, Minor). Branch P2-d (free-body diagram, Problem 1 a): Add Force, angle/length via the force table, Ctrl+Shift+3 totals and Submit all completed keyboard-only with NVDA — pass, vendor claim confirmed (R017 O20). Branch P2-a (numeric with units, Problem 5): unit radios named and operable; the entry area is the same non-control `div` as the symbolic part (V-F13). Branch P2-e (Hint / Feedback): deductions spoken, but the inserted hint is not announced and cannot be found easily (V-F15). Branch P2-f (I give up!): confirmation modal with Continue / Cancel — pass. Branch P2-g (detailed view / Ctrl+Shift+2): read-back covered under V-F9. Screen-reader pass of T2 complete. **Verdict Fail** (reviewer, 2026-09-10): a screen-reader user cannot complete the assignment because multiple-choice parts whose options contain math cannot be answered knowingly (V-F11, V-F9) — "if they can't complete the entire problem set because a single problem is inaccessible then the whole problem set is not accessible." Keyboard-only (R018): ~20 Tab stops to the first answer field, focus visible on every stop, no traps, palette-only symbols (θ, β, √) enterable by keyboard; the jump-point stops are Enter-to-open hidden menus rather than skips. Low-vision pending.

(no findings yet)

---

### Task T3 — Complete an assignment under time limits and accommodations — process P3, implements F3

| | |
|---|---|
| **User story** | As a student, I need to work within begin/due/end dates, late-work rules, submission limits and the session timeout — with an extended-time accommodation applied when granted — so that I am not timed out or penalised for my disability. |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B1, B2, B3 |
| **Date(s) tested** | |

**Sequence notes:** (per-step observations; identify the step where each
barrier occurs)

(no findings yet)

---

### Task T4 — Author an assignment from the library (instructor) — process P4, implements F7

| | |
|---|---|
| **User story** | As an instructor, I need to create an assignment, filter the library to accessible problems (or deliberately include the three admitted inaccessible types for the review), add problems, and save. |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B1, B2, B3 |
| **Date(s) tested** | |

**Sequence notes:** (per-step observations; identify the step where each
barrier occurs)

(no findings yet)

---

### Task T5 — Check grades and feedback — process P5, implements F4 and F6

| | |
|---|---|
| **User story** | As a student I need to read my grade report for an assignment; as an instructor I need to read the class grade sheet and grade a part manually. |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B1, B2, B3 |
| **Date(s) tested** | |

**Sequence notes:** (per-step observations; identify the step where each
barrier occurs)

(no findings yet)

---

## B. View sweep (WCAG-EM step 4.1 — per-view modality checks)

Every sampled view (03 §3.1/§3.2) is checked under **every sensory/functional
modality** (Section 508 Functional Performance Criteria: no-vision,
low-vision, no-color, no-hearing, no-speech, motor, cognition) using the
standardized per-view checklists in `ontology/modality-checks.md`, plus a
WAVE sweep per view. One run per view×modality (`log-test --modality`), with
the run's **Result** set to Works / Works with issues / Broken / N/A.
Failures become findings below, citing the check ID (e.g., `MO4`) and run ID.

`review.py matrix <review>` shows the views × modalities grid and remaining
gaps; `validate` fails while cells are unrun or results unset.

Check the full view — all components and significant states — without
initiating processes (those are covered in §A). Repeated components (header,
navigation, footer) need re-checking only where they appear or behave
differently.

### View S1 — Class Management (standard mode)

| | |
|---|---|
| **Baselines run** | (pending — R015 open; axe R001) |
| **Date tested** | |
| **Findings** | (none yet — R001 observations await confirmation) |

### View S2 — Class Management, Accessibility Mode

| | |
|---|---|
| **Baselines run** | B5 NVDA (R016, in progress); axe (R005) |
| **Date tested** | 2026-09-10 |
| **Findings** | V-F1, V-F2, V-F3, V-F5, V-F6, V-F7, V-F8 (V-F4 withdrawn) |

#### Finding V-F1

| | |
|---|---|
| **Where** | S2 Class Management (Accessibility Mode) — whole page; also S1 (axe R001) and every other signed-in view (axe R004–R014) |
| **Observed** | No headings and no landmarks: NVDA `H` and `D` report none; the elements list offers no route to the content. The visible section titles ("Classes", "Class Menu", "Class Assignments", "Class News") are `div tabindex="0"` elements wrapping a coloured bold span — focusable, no role, not headings — so they announce as plain text when tabbed to. The "accessible version" of the page adds skip links and captions but no structure. |
| **Affected users** | Screen reader users (no structural navigation); keyboard users (extra tab stops with no purpose) |
| **WCAG criteria failed** | 1.3.1 (visual headings not programmatically determinable); 2.4.1 in combination with V-F3 |
| **Severity** | Major |
| **Evidence** | R016 O2, O5 (reviewer-pasted markup of `#assignmentsTitle`); R005 `R005-axe.json` (`page-has-heading-one`, `landmark-one-main`, `region` ×29); R001 for S1 |

#### Finding V-F2

| | |
|---|---|
| **Where** | S2 Class Management — Class Assignments and Class News grids (DevExpress) |
| **Observed** | Each grid is rendered as two tables: a header table captioned "Headers for the data table below" and a body table captioned "Data table related to the headers above". Both grids use the identical generic captions, so `T`-key navigation announces "Data table related to the headers above, table clickable with x rows and x columns" for either and the user cannot tell which table they are in; on entering, no header names are listed. Column headers **are** announced per cell during table navigation ("row 3, Actions, column 1" — R016 O10), so the header–cell relationship holds; the defect is identification. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1 (table identification) |
| **Severity** | Minor (revised 2026-09-10) |
| **Evidence** | R016 O3; R005 `R005-axe.json` (captions in DOM) |

#### Finding V-F3

| | |
|---|---|
| **Where** | S2 Class Management — the skip links "Tab for Assignments, Enter to skip…" and "Tab for Class News, Enter to skip" |
| **Observed** | The section skip controls ("Tab for Assignments, Enter to skip…", "Tab for Class News, Enter to skip") **do work**: Enter moves focus to the next section's skip control, skipping the section (revised 2026-09-10 from the reviewer's first impression that nothing happened). They are exposed as links (`href="javascript:skipper('News')"`) although they act as buttons, and their wording reads as an instruction rather than as the name of a control, so a user hears "Tab for Assignments, Enter to skip, link" and cannot tell what will be skipped. Together with the top-of-page jump point they satisfy 2.4.1 on this page. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (role); 2.4.4 (link purpose from its text) |
| **Severity** | Minor |
| **Evidence** | R016 O4; R005 `R005-axe.json` (`bypass` incomplete; the `a[href^=javascript:skipper]` elements) |

#### Finding V-F4

| | |
|---|---|
| **Where** | S11 — the Class Menu popups (Create Class / Edit Class / Student-TA Registration / Create News / Copy Assignment: DevExpress popup iframes over S2/S1) |
| **Observed** | **Withdrawn 2026-09-10.** First impression: the Class Menu popups (Create Class, Edit Class, Create News, …) "can't be escaped out of". Clarified: each popup has an exposed, working Close/Cancel button; only **Esc** does nothing. Focus can leave by a standard key path, so 2.1.2 is not failed. Kept as an advisory note (Esc-to-close convention; dialog role/announcement to be checked in the S11 keyboard run). ID retained for stability. |
| **Affected users** | — |
| **WCAG criteria failed** | none (withdrawn) |
| **Severity** | — (advisory) |
| **Evidence** | R016 O6; R002 `R002-axe.json` (popup document; no dialog semantics in DOM per 03 §2.6) |

#### Finding V-F5

| | |
|---|---|
| **Where** | S11 — the popup forms (e.g. Edit Class: Class Name, Class Description, Time Zone, Academic Year, Semester, Subject) |
| **Observed** | Form inputs are not labelled; the visible "labels" are text in an adjacent table column of the layout table, not associated with the inputs. Confirms axe `label` ×6 on the same document (R002 O1). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1, 3.3.2, 4.1.2 |
| **Severity** | Major |
| **Evidence** | R016 O7; R002 `R002-axe.json` |

#### Finding V-F6

| | |
|---|---|
| **Where** | S2 Class Management (Accessibility Mode) — the per-row **Actions** `<select>` in the Class Assignments grid, the control that leads to Take Assignment |
| **Observed** | The select has no accessible name of its own (axe `select-name`, R005 O1). In NVDA browse mode the cell text is read before the control — Speech Viewer: "Create Assignment  Go  Assignment Menu - Click To Activate  row 3  Actions  column 1  combo box  Create Assignment  collapsed" — so the user hears "Assignment Menu - Click To Activate" from the cell, followed by "combo box, Create Assignment, collapsed"; a focus-mode Tab onto the control would announce only the combo box and its current value. Column header "Actions" is announced. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (name) |
| **Severity** | Minor |
| **Evidence** | R016 O10 (Speech Viewer excerpt); R005 `R005-axe.json` |

#### Finding V-F7

| | |
|---|---|
| **Where** | S2 Class Management (Accessibility Mode) — the "Classes:" and "Class Menu:" `<select>` controls at the top of the page |
| **Observed** | Both selects announce the same accessible name — "First make your selection here and then click Go button to confirm your choice." — followed by role and current value (Speech Viewer: "First make your selection here and then click Go button to confirm your choice.  combo box  Testing Course for CSU East Bay  collapsed"). The visible captions "Classes:" and "Class Menu:" are not announced at all. A screen-reader user cannot tell which select is the class chooser and which is the action menu except from the current value. |
| **Affected users** | Screen reader users; speech-input users (the visible label is not in the name) |
| **WCAG criteria failed** | 1.3.1, 2.5.3, 4.1.2 |
| **Severity** | Major |
| **Evidence** | R016 O11 (Speech Viewer excerpt) |

#### Finding V-F8

| | |
|---|---|
| **Where** | S2 (and S1) Class Management — the top-of-page "jump point" (`#top_of_page_jump_point`, `div role="button" tabindex="0"`), the first focusable control on every signed-in view |
| **Observed** | The controls have no accessible name (axe `aria-command-name` on all 14 views) — NVDA reads only their instruction text plus "button". On Class Management, Enter changes the text to "No Shortcuts" and navigates nowhere. On Take Assignment (R017 O2) the problems jump point is a **visually hidden** tab stop; Enter mounts the "accessibility shortcuts menu" links, which keyboard users can Tab to but NVDA users reach only after switching to browse mode. The reviewer judged the pattern "very confusing for a screen reader user": the bypass mechanism exists but is discoverable only by tabbing into a hidden area. The documented `Ctrl+Shift+1` (previous part) chord moves focus to the top jump point instead (R017 O13). |
| **Affected users** | Screen reader users; keyboard users |
| **WCAG criteria failed** | 4.1.2; 2.4.3 |
| **Severity** | Major (re-rated 2026-09-10 on Take Assignment) — pending the keyboard run's check of focus visibility on the hidden stop (2.4.7) |
| **Evidence** | R016 O12; R017 O2 (Speech Viewer: "Press tab to go to problems. Press enter to open the accessibility shortcuts menu.  button"); R005 / R001 / R004 `*-axe.json` |

### View S3 — Take Assignment

| | |
|---|---|
| **Baselines run** | B5 NVDA (R017, in progress); axe (R004, four states) |
| **Date tested** | 2026-09-10 |
| **Findings** | V-F9, V-F11, V-F12, V-F13, V-F14, V-F15 (V-F10 withdrawn — advisory; plus T1-F2 in §A; V-F8 applies here) |

#### Finding V-F9

| | |
|---|---|
| **Where** | S3 Take Assignment — the `Ctrl+Shift+2` "read out your answer" function (live region `#calc-announce`), Problem 9 multiple choice with MathJax in the option text |
| **Observed** | After selecting an option, `Ctrl+Shift+2` places the option's **raw MathJax HTML source** in the alert live region. NVDA reads roughly 4,400 characters of element, class, style and attribute markup ("span class MathJax_Preview style color inherit display none … data minus mathml ltmath xmlns quot http divided by divided by www.w3.org …") before and around the actual answer text (T₂ is less than T₁). `Ctrl+Shift+5` (instructions) works correctly on the same region, so the mechanism is sound and the defect is the content injected for math-bearing answers. This is the vendor's compensating read-back for parts whose radio buttons have no names (R004 O1), and its "human-friendly spoken math" claim. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.3, 1.3.1 |
| **Severity** | Blocker for the read-back function (unusable output); Major for Task T2 |
| **Evidence** | R017 O3, O4; `evidence/runs/R017/R017-ctrlshift2-speech.txt` |

#### Finding V-F10

| | |
|---|---|
| **Where** | S3 Take Assignment — MathJax-rendered mathematics in problem statements (observed: Problem 8, M₁ and M₂) and in multiple-choice options (Problem 8, "½ g") |
| **Observed** | **Withdrawn as a failure 2026-09-10.** First reading: M₁/M₂ announced as "table". Clarified: that is NVDA **focus-mode** behaviour; in browse mode the browse cursor enters the MathJax item and the math is read (MathJax's assistive MathML is exposed). The statement math is therefore programmatically available. Kept as an advisory: the answer widgets keep NVDA in focus mode, so a user must know to switch modes to read the math around them, and MathJax inside answer options does not reliably play in either mode (that part remains in V-F11). |
| **Affected users** | — (advisory) |
| **WCAG criteria failed** | none (withdrawn) |
| **Severity** | — (advisory) |
| **Evidence** | R017 O7 (revised), O9 |

#### Finding V-F11

| | |
|---|---|
| **Where** | S3 Take Assignment — multiple-choice answer radio buttons (Problems 8 and 9) |
| **Observed** | The radios have no accessible name (axe `label` ×5/6, R004 O1; accessibility tree shows unnamed radios). Browse mode: arrowing between options reads the adjacent cell text, so plain-text options are usable; a math option ("½ g") announces only "row 4 table 1". Focus mode (Shift+Tab from Submit, 2026-09-10): the group is entered as "table"; arrowing auto-selects and announces "Radio Button Checked X of X" plus the column-two answer text, but MathJax inside an option does not reliably play and the user must leave focus mode to hear it; the auto-read of an option mixing text and math breaks. `Ctrl+Shift+2` read-back of a math option is unusable in both modes (V-F9). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1, 4.1.2 |
| **Severity** | Major (Blocker for parts whose options contain math) |
| **Evidence** | R017 O6, O9; R004 `R004-axe.json` |

#### Finding V-F12

| | |
|---|---|
| **Where** | S3 Take Assignment — the problem figure (observed: Problem 8, two blocks and a pulley; exploration found the same on Problems 6, 7, 9) |
| **Observed** | NVDA `G` (next graphic) finds no graphic on the page; the figure cannot be right-clicked. The figure `<img>` has an **empty alt**, so it is treated as decorative and hidden from the screen reader, although the statement refers to it ("as shown") and it carries the physical setup. Problems 1, 4, 5 carry descriptive alt (exploration) — so this is per-problem authoring, and the solutions page shows a broken `alt=` quote on some figures (R014 O1). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.1.1 |
| **Severity** | Major |
| **Evidence** | R017 O8; exploration 03 §2.6 (empty alt on P6–P9); R014 `R014-axe.json` |

#### Finding V-F13

| | |
|---|---|
| **Where** | S3 Take Assignment — the formula/number entry area of symbolic ("Equation") and numeric ("Algorithm") parts; observed on Problem 2 Part (a) and Problem 5 |
| **Observed** | The entry area is not a form control: it is a `div` (`<div class="problemanswer" id="problem_answer">332 fact( exp( | ) )</div>`, reviewer-pasted) holding the typed expression and a blinking-caret span — no role, no name, no value exposed, not in the Tab order. Nothing announces it as the F_NET (or other quantity) answer: the visible "F_NET =" prefix is a MathJax expression beside it, not an associated label. A screen-reader user cannot reach it directly — only by tabbing to a neighbouring element and arrowing into it in browse mode — and hears its content only through `Ctrl+Shift+2` (empty: "Alert your answer in degrees"; populated: read left to right with no nesting conveyed). The caret can be moved with on-screen ←/→/HOME/END buttons; its position is not announced as it moves, but `Ctrl+Shift+3` reports it on request. Typing works and the keypad buttons are Tab-reachable, so entry is possible once the area is found. |
| **Affected users** | Screen reader users; keyboard users (no focusable, visible entry stop) |
| **WCAG criteria failed** | 4.1.2, 1.3.1, 3.3.2, 2.4.3 |
| **Severity** | Major |
| **Evidence** | R017 O15, O16, O17, O22 |

#### Finding V-F14

| | |
|---|---|
| **Where** | S3 Take Assignment — Problem 3 drag-and-drop ranking, the alternative "drag and drop accessibility table" form |
| **Observed** | The alternative form is discoverable and operable: an exposed button ("Show drag and drop accessibility table") reachable by Tab moves focus into a Bucket / Order / Item table of combo boxes with "Add Item" and "Reset". But a placement, and the resulting ranking, are not announced in any designed way; the user can only derive the state by navigating the table. The `Ctrl+Shift+2` read-back reads only the Item column and runs the rows together "like a long paragraph" with no boundary between items, so the user cannot tell which item is being referenced. The combo boxes and the ✖ delete buttons are properly announced; the visual cards outside the form announce nothing (empty alt), the form's item descriptions being the only accessible rendering of them. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.3 |
| **Severity** | Minor ("not unusable" — reviewer) |
| **Evidence** | R017 O18 (DOM structure, `R017-p3-dnd-accessible-form.png`), O19 |

#### Finding V-F15

| | |
|---|---|
| **Where** | S3 Take Assignment — the **Hint** button (and, by the same mechanism, Feedback) on any part |
| **Observed** | Activating Hint inserts the hint text below the problem area, but nothing is announced: NVDA's Speech Viewer at that moment shows only "table with 3 rows and 1 column Submissions Info." The reviewer found no clear way to navigate to the inserted hint. Requesting a hint costs a deduction (the percentages are spoken), so a screen-reader user pays for content they are not told has arrived and cannot easily find. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.3, 2.4.3 |
| **Severity** | Major |
| **Evidence** | R017 O23; `evidence/runs/R017/R017-hint-speech.txt` |

---

## C. Sample comparison (WCAG-EM step 4.3 — random vs structured)

Check that the random samples (03 §3.2) show no content types or findings
absent from the structured set. If they do, the structured sample was not
representative: return to step 3, extend the sample set, and test the
additions. Repeat until no new types or findings appear.

| Random sample | New content type? | New findings? | Action taken |
|---------------|-------------------|---------------|--------------|
| R1 | | | |

---

## D. Coverage check

Before moving to `05-results.md`:

- [ ] Every process in 03 §3.3 has a task cluster with a verdict
- [ ] Every branch sequence was walked, not just default sequences
- [ ] Every non-process sample has a view-sweep entry
- [ ] Every finding names at least one WCAG criterion, a severity, and evidence
- [ ] Random-vs-structured comparison completed (and sample extended if needed)
- [ ] `05-results.md` updated: every failed criterion cites finding IDs from this file
