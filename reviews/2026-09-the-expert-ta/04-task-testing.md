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
| **Verdict** | Pass with barriers |
| **Baselines run** | B5 (NVDA) on S2 — R016; B5 on S1 — R015 (2026-09-14); B2, B3 pending |
| **Date(s) tested** | 2026-09-10, 2026-09-14 |

**Sequence notes:** **Verdict Pass with barriers (reviewer, 2026-09-14):** in standard mode — the page every student lands on — step 3 cannot be completed from the keyboard: the assignment row's action menu opens only by mouse click (T1-F3). The reviewer accepts the Accessibility Mode page as the vendor's alternate route: "not an ideal solution, but it does allow access. Not fail." So the task passes through branch P1-a (Accessibility Mode, S2 → S3) with the barriers T1-F1, T1-F2 and T1-F3's discoverability cost (the user must find the "Accessibility Page" button first; the mode is then stored on the account). 2026-09-14, NVDA, standard mode (S1, R015): title "Class Management"; no headings/landmarks (V-F1 confirmed); reading order fine but the grids are told apart by position (V-F2 confirmed); the Classes / Class Menu editors announce an instruction, not a label (V-F7 confirmed); the first Tab stop is the hidden instruction div; the grids' expand controls are unnamed clickable graphics (V-F16). Earlier: 2026-09-10, NVDA, Accessibility Mode (S2): step 1 sign-in not walked (already signed in). Step 2 Class Management: title fine (R016 O1); no headings/landmarks, the skip links are inert, and the two grids share one generic caption — the reviewer reaches the assignments table by `T`/Tab and identifies it by the focusable title div (R016 O2–O5). Step 3 (Accessibility Mode): row Actions select → "Take Assignment" → Go; page change announced (R016 O13) — completable. The Classes / Class Menu selects at step 2 are not distinguishable by name (V-F7). Step 4 (R017): problem links work with `K`/Enter but focus does not move into the activated problem and there are no headings to find it (T1-F2); the hidden problems jump point mounts a shortcuts menu only after Enter, and NVDA users must switch to browse mode to use it (V-F8). Step 5 pending.

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

#### Finding T1-F3

| | |
|---|---|
| **Where** | Step 3, Class Management in standard mode (S1) — opening the assignment row's action menu (⋮) to reach "Take Assignment" |
| **Observed** | In standard mode the Class Assignments grid row has no focusable control: Tab reaches nothing in the row, and Enter, Space and the Applications key do nothing on the row or the ⋮ cell. The reviewer: "Only way to nav is by clicking the table row." The action menu, and with it "Take Assignment", "View Grade Report" and the rest, opens by mouse click only; when it is opened with the mouse, its appearance is not announced to NVDA and its items are read only on mouse-over (R015 O12). The Accessibility Mode page (S2) replaces the menu with an Actions select plus Go button that does work (R016 O13), so the route exists only after the user finds the "Accessibility Page" button and switches modes; the mode is stored on the account. The exploration record (R001 O7) showed the row as plain cells with a click handler; this confirms it. |
| **Affected users** | Keyboard-only users; screen reader users (the default page dead-ends the core task) |
| **WCAG criteria failed** | 2.1.1 (menu operable by pointer only); 4.1.2 (no control exposed for the row action) |
| **Severity** | Minor (reviewer's ruling 2026-09-14: the Accessibility Mode page is accepted as a conforming alternate version — "not an ideal solution, but it does allow access" — so the defect is the standard page's own operability and the discoverability of the alternate, not a task stop. Would be a Blocker for the standard page alone.) |
| **Evidence** | R015 O10; R001 `R001-axe.json` (row cells with click handler, no role) |

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

**Scope note 2026-09-15:** the reviewer removed every instructor-facing view from the sample (03 §1.1 Exclusions); this task is instructor-only, so it is not walked unless the reviewer rules otherwise. Verdict stays Not run.

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

**Blocked 2026-09-21 — no data in the demo.** The reviewer: "there are no grades to view in the test account." The student half of this task (read your grade report for an assignment) cannot be walked: the pages load and have been swept and zoomed (S4 View Grade Report — R007, R029, R100), but they contain no score, no feedback and no late state, so the jump-point density, the per-part submission tables and the red "late" convention that W21 asks about have nothing to read. The instructor half (class grade sheet) left the sample 2026-09-15 as instructor-facing. Verdict stays Not run and this is a **coverage limitation** in `03` §1.1, not a pass — closing it needs a seeded graded assignment.

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
| **Baselines run** | B5 NVDA (R015, 2026-09-14 — NV7/NV10 open); axe (R001); probe runs R019–R023 |
| **Date tested** | 2026-09-14 |
| **Findings** | T1-F3 (§A); V-F1, V-F2, V-F7 confirmed on this view (recorded under S2); V-F8 (jump point); V-F16; V-F19 (product-wide, confirmed here and on S3); V-F21 (also S3); V-F23 (text contrast; also S2, S3, S4, S5, S6, S7, S8, S10, S12, R1 per axe); V-F29 (product-wide, recorded here) |

#### Finding V-F19

| | |
|---|---|
| **Where** | Every sampled page — the whole application is laid out in a fixed-width 1300 px box (`div#container`); measured on all 14 views (S1–S12, R1, R2) and confirmed by the reviewer on Class Management, standard mode (S1) and Take Assignment (S3). |
| **Observed** | At 320 CSS px wide (the 1.4.10 reflow viewport, ≈ 400 % zoom in a 1280 px window) every page scrolls in two dimensions — the content does not re-stack into one column (probe, 2026-09-11: S1 scrollWidth 1343, S3 1300, S5 1373; the Edit Class popup 589 px, the sign-in page 1024 px). Reviewer 2026-09-15 at real 400 % zoom: "nothing is hidden or lost at 400%, but no reflow" on both pages — everything stays reachable, but a line of text or a row of controls is read by scrolling sideways and back for each line. No data table, canvas or image exemption applies to the page layout itself. |
| **Affected users** | Low-vision users who enlarge content with browser zoom; anyone on a narrow viewport (a phone, a split screen, a magnifier's reduced viewport) |
| **WCAG criteria failed** | 1.4.10 |
| **Severity** | Major |
| **Evidence** | R019 O2, O5 (S1); R083 O2, O5 (S3); measured LV1 O2 on R024, R030, R036, R042, R048, R054, R060, R066, R072, R078, R088, R094 (`R###-probe.json` each) |

#### Finding V-F23

| | |
|---|---|
| **Where** | Class Management, standard mode (S1) — the "Classes" / "Class Menu" captions, the "Class Assignments" and "Class News" section headings, and the grey welcome / news body text. The same colour family recurs across the product (axe `color-contrast` violations on 11 of 14 views): the orange section headings on the Assignment Editor (S5) and Student Practice Area (S12); grey 12 px notice text on View Grade Report (S4) and Manage Class Roster (S10); red randomized-variable values (`#FF6347`, 2.94:1) and red MathJax values (`#FF0000`, 3.99:1) on View Grade Report (S4), View Assignment Solutions (S8) and View Printable Assignment (S13, confirmed 2026-09-15); the orange deduction percentage (`#FF9900`, 2.14:1) on Take Assignment (S3); the Calendar event bar (white on `#8EA9DB`, 2.37:1); "User Name:" on Sign in (4.05:1); the selected profile on Academic Integrity Preferences (white on `#A0A0A0`, 2.61:1). |
| **Observed** | Eyedropper by the reviewer, 2026-09-15, Class Management at 100 %: teal captions `#48848C` on white — "Large pass, Fail regular for AA" (the captions are 16 px, so the 4.5:1 threshold applies; 4.23:1); "Class Assignments" `#EFBB75` on white — "fail for all levels" (1.74:1); grey `#808080` text — "fails over white for AAA and only passes for large in AA" (12 px body text; 3.94:1). The other pages' values are axe measurements (R001–R014 `R###-axe.json`) confirmed page by page in W43–W55; the Take Assignment deduction percentage and the grade-report variable values are information a student acts on, not decoration. |
| **Affected users** | Low-vision users and anyone reading on a dim or glare-lit screen; colour-vision-deficient users for the orange/red items |
| **WCAG criteria failed** | 1.4.3 |
| **Severity** | Major (confirmed by the reviewer 2026-09-15) |
| **Evidence** | R019 O6 (S1, eyedropper); R024 O6 (S2); R030 O6 (S4, eyedropper); axe R001 (S1), R005 (S2), R004 (S3), R007 (S4), R006 (S5), R008 (S6), R003 (S7), R014 (S8), R010 (S10), R011 (S12), R012 (R1) `violations:color-contrast` |

#### Finding V-F21

| | |
|---|---|
| **Where** | Class Management, standard mode (S1) — the assignment row's **⋮** menu icon (16 × 16 px) beside the **+** expand glyph (9 × 10 px); Take Assignment (S3) — the nine **problem-number links** in the left navigator (8 × 18 px each, adjacent). The Assignment Editor's spinner/time arrows (S5, 16 × 9 px) were measured too but are exempt: the values can be typed directly (R039). |
| **Observed** | Measured by the probe (targets under 24 × 24 CSS px with another target inside the 24 px circle). The reviewer ruled on the exceptions 2026-09-14: the ⋮ menu — "no other way found" on this page (the Accessibility Mode page's Actions select is a different page); the problem links — "no alternative found" (the Ctrl+Shift chords and the post-submit "Continue" link do not replace direct problem selection); the editor arrows — exempt, "yes, can be typed directly". A pointer user with a tremor or a coarse pointer hits the neighbouring target: the wrong problem, or the expand glyph instead of the menu. |
| **Affected users** | Users with limited fine motor control; touch and coarse-pointer users |
| **WCAG criteria failed** | 2.5.8 |
| **Severity** | Minor |
| **Evidence** | R022 O2 (S1, element list in `R022-probe.json`); R018 O6 (S3, `R018-probe.json`); R039 O2 (S5, exempt) |

#### Finding V-F16

| | |
|---|---|
| **Where** | S1 Class Management (standard mode) — the + expand controls of the Class Assignments and Class News grids |
| **Observed** | `G` (next graphic) stops on two controls announced as "collapsed graphic clickable": the DevExpress detail-expand glyphs (`img.dxGridView_gvDetailCollapsedButton`). They are clickable images with no role (not a button) and no name — a screen-reader user hears that something collapsed is clickable but not what it expands. The site logo, the only other graphic, has alt text. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (no name, no role); 1.1.1 (an actionable image with no text alternative) |
| **Severity** | Minor |
| **Evidence** | R015 O11; R022 O2 (the same glyphs measured at 9×10 px for 2.5.8); R059 O3 (S12, 2026-09-15: the sections grid's expand image — `alt="[Collapse]"`, onclick, no role, not focusable) |

#### Finding V-F29

| | |
|---|---|
| **Where** | Product-wide on every signed-in page — the header logo link (`<a href="http://theexpertta.com/">` wrapping `ETA_LogoForWeb_White.png`), measured on S1 Class Management (standard mode). It is the **8th Tab stop** from the top of the page. |
| **Observed** | The logo link sits inside `aria-hidden="true"` but is still in the keyboard tab order. Measured 2026-09-17 with real dispatched Tab keys from the top of the document (R001 O11): stop 1 the hidden instruction div, 2 theExpertTA.com, 3 My Account, 4 Log Out, 5 Class Management, 6 Instructor, 7 Help, **8 the aria-hidden logo link**. A keyboard user lands on it and can activate it — it leaves the application for the vendor's marketing site. A screen-reader user is given nothing at that stop: because the whole subtree is `aria-hidden`, even the image's `alt="The Expert TA"` is suppressed. That is why the reviewer's NVDA links list came back empty on this page (R015 O13) — the only link in the header region is hidden from the AT while remaining focusable. axe flagged it as `aria-hidden-focus` on every view swept (R001 O3, PW-C). |
| **Affected users** | Screen reader users (a silent stop that still navigates away from the app when activated); keyboard-only users (an unlabelled stop with no visible purpose) |
| **WCAG criteria failed** | 4.1.2 (a focusable control with no exposed name or role) |
| **Severity** | Minor (proposed 2026-09-17 — one stop, early in the order, and the destination is harmless; the reviewer confirms or overrules at W71) |
| **Evidence** | R001 O3 (axe `aria-hidden-focus`), R001 O11 (tab-order measurement); R015 O13 (NVDA links list empty) |

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
| **Evidence** | R059 O3 (S12 confirmed 2026-09-15: "no headings, no tabs"); R016 O2, O5 (reviewer-pasted markup of `#assignmentsTitle`); R005 `R005-axe.json` (`page-has-heading-one`, `landmark-one-main`, `region` ×29); R015 O6 (S1 confirmed with NVDA 2026-09-14); R001 for S1 |

#### Finding V-F2

| | |
|---|---|
| **Where** | S2 Class Management — Class Assignments and Class News grids (DevExpress) |
| **Observed** | Each grid is rendered as two tables: a header table captioned "Headers for the data table below" and a body table captioned "Data table related to the headers above". Both grids use the identical generic captions, so `T`-key navigation announces "Data table related to the headers above, table clickable with x rows and x columns" for either and the user cannot tell which table they are in; on entering, no header names are listed. Column headers **are** announced per cell during table navigation ("row 3, Actions, column 1" — R016 O10), so the header–cell relationship holds; the defect is identification. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1 (table identification) |
| **Severity** | Minor (revised 2026-09-10) |
| **Evidence** | R016 O3; R015 O7 (S1 confirmed 2026-09-14: same generic captions and headers in standard mode); R005 `R005-axe.json` (captions in DOM) |

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
| **Evidence** | R016 O7; R002 `R002-axe.json`; R059 O3 (S12 confirmed 2026-09-15: "no forms have labels" — Books / Chapters selects, difficulty checkboxes; R011 `R011-axe.json` 12 unlabeled) |

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
| **Evidence** | R016 O11 (Speech Viewer excerpt); R015 O8 (S1 confirmed 2026-09-14: the DevExpress editors in standard mode announce the same instruction sentence and no label; the purpose is first heard on the adjacent Go button) |

#### Finding V-F8

| | |
|---|---|
| **Where** | S2 (and S1) Class Management — the top-of-page "jump point" (`#top_of_page_jump_point`, `div role="button" tabindex="0"`), the first focusable control on every signed-in view |
| **Observed** | The controls have no accessible name (axe `aria-command-name` on all 14 views) — NVDA reads only their instruction text plus "button". On Class Management, Enter changes the text to "No Shortcuts" and navigates nowhere. On Take Assignment (R017 O2) the problems jump point is a **visually hidden** tab stop; Enter mounts the "accessibility shortcuts menu" links, which keyboard users can Tab to but NVDA users reach only after switching to browse mode. The reviewer judged the pattern "very confusing for a screen reader user": the bypass mechanism exists but is discoverable only by tabbing into a hidden area. The documented `Ctrl+Shift+1` (previous part) chord moves focus to the top jump point instead (R017 O13). |
| **Affected users** | Screen reader users; keyboard users |
| **WCAG criteria failed** | 4.1.2; 2.4.3 |
| **Severity** | Major (re-rated 2026-09-10 on Take Assignment) — pending the keyboard run's check of focus visibility on the hidden stop (2.4.7) |
| **Evidence** | R016 O12; R017 O2 (Speech Viewer: "Press tab to go to problems. Press enter to open the accessibility shortcuts menu.  button"); R005 / R001 / R004 `*-axe.json`; R063 O4 (S12, 2026-09-15: "their ctrl alt 1 doesn't do anything") |

### View S3 — Take Assignment

| | |
|---|---|
| **Baselines run** | B5 NVDA (R017, in progress); axe (R004, four states) |
| **Date tested** | 2026-09-10 |
| **Findings** | V-F9, V-F11, V-F12, V-F13, V-F14, V-F15, V-F18, V-F19 (recorded under S1), V-F21 (recorded under S1), V-F23 (recorded under S1), V-F24 (V-F10 withdrawn — advisory; plus T1-F2 in §A; V-F8 applies here) |

#### Finding V-F24

| | |
|---|---|
| **Where** | Take Assignment (S3) — the problem figures (`<img>` per problem; the same images on View Grade Report, S4 — confirmed 2026-09-15 — View Assignment Solutions, S8, and View Printable Assignment, S13). Problems 1 and 6 in particular: text drawn over the graphic. |
| **Observed** | The figures are low-resolution raster images that contain text — "usually math" (reviewer, 2026-09-15): labels, values and formulas a student needs to solve the problem are pixels, not text, although the same page renders its statement mathematics with MathJax (real text). At 400 % zoom they "don't scale well … they are blurry" — the math in them stops being readable exactly when a low-vision user enlarges it. On Problems 1 and 6 the text sits over a graphic and "fail[s] color contrast" (reviewer, eyedropper). Related: the same images have empty `alt` for screen-reader users (V-F12, 1.1.1). |
| **Affected users** | Low-vision users (zoom, magnification); users with colour-vision or contrast sensitivity loss; screen-reader users via V-F12 |
| **WCAG criteria failed** | 1.4.5, 1.4.3 |
| **Severity** | Major (confirmed by the reviewer 2026-09-15) |
| **Evidence** | R083 O6, O8, O9 (S3); R030 O5 (S4); R014 `R014-axe.json` (S8: 14 figure images without alt); V-F12 (R017 O8) |

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

#### Finding V-F18

| | |
|---|---|
| **Where** | Take Assignment (S3, `/Common/TakeTutorialAssignment…`), Sign in (S7, `login.theexpertta.com/Login.aspx`), the Edit Class popup (S11, Class Management → Class Menu → Edit Class → Go) and Password reset (S14, `login.theexpertta.com/ResetPassword.aspx` — added 2026-09-21) — the `<html>` element |
| **Observed** | These three pages declare no `lang` attribute; the other eleven sampled views declare `lang="en"`. A screen reader whose synthesizer defaults to another language reads the assignment, the sign-in form and the popup with the wrong voice; with an English default nothing is audible (the reviewer heard no mispronunciation, R017 NV9). Measured by axe (R004 O2, `html-has-lang`) and the probe (R093, R077); confirmed as a finding by the reviewer's delegation 2026-09-14 ("your call"). |
| **Affected users** | Screen reader users whose default synthesizer language is not English |
| **WCAG criteria failed** | 3.1.1 |
| **Severity** | Minor |
| **Evidence** | R017 NV9; R004 O2 `R004-axe.json`; R093 O4, R077 O4 (`R093-probe.json`, `R077-probe.json`) |

### View S12 — Student Practice Area

| | |
|---|---|
| **Baselines run** | axe (R011); probe runs R059–R064, R105; reviewer 2026-09-15 — NVDA (R059), keyboard (R063), eyedropper (R060) |
| **Date tested** | 2026-09-11 (measured), 2026-09-15 (reviewer) |
| **Findings** | V-F28; V-F1, V-F5, V-F16, V-F19, V-F23 confirmed here; V-F8 (inert Ctrl+Alt+1) |

#### Finding V-F28

| | |
|---|---|
| **Where** | Student Practice Area (S12) — `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` (Class Menu → Student Practice Area → Go): the sections grid that holds the practice problems ("Problems to Help Students Learn Expert TA" and the chapter sections), its expand controls and its per-problem checkboxes. |
| **Observed** | Reviewer, 2026-09-15: "this page is hard to navigate … the sections table requires an expansion to view the content, but the expand buttons are not appropriately labeled, no forms have labels, no headings, tabbing focus is lost outside of the initial buttons and dropdowns, their ctrl alt 1 doesn't do anything. can't tab into the check boxes, there is no obvious way to find the tutorial content". The markup the reviewer saved (`R059-sections-table.html`) explains it: the content is four nested tables with no captions, headers or headings; the expand control is an `<img alt="[Collapse]">` with an `onclick` and no role or tabindex; the problem checkboxes are DevExpress `<span>`s, not inputs. So a keyboard user's Tab stops at the Books / Chapters selects and the buttons and then focus vanishes — the practice problems can never be reached or selected; a screen-reader user has no heading, landmark or caption to find them and hears unnamed graphics and unlabeled fields. This is the student's self-study entry point (F1 access course content). |
| **Affected users** | Keyboard-only and switch users (cannot reach the content at all); screen-reader users (cannot find or identify it); low-vision users navigating by focus |
| **WCAG criteria failed** | 2.1.1, 2.4.7, 1.3.1, 4.1.2 |
| **Severity** | Blocker for this page (assistant's rating — reviewer to confirm) |
| **Evidence** | R063 O4 (keyboard); R059 O3 (NVDA); `R059-sections-table.html` (reviewer-saved markup); R011 `R011-axe.json` (12 unlabeled fields, no headings, no landmarks) |

### View S4 — View Grade Report

| | |
|---|---|
| **Baselines run** | axe (R007); probe runs R029–R034, R100; zoom + eyedropper (R030, 2026-09-15 — reviewer) |
| **Date tested** | 2026-09-11 (measured), 2026-09-15 (reviewer) |
| **Findings** | V-F19, V-F23 (recorded under S1) and V-F24 (recorded under S3) confirmed here; V-F27 |

#### Finding V-F27

| | |
|---|---|
| **Where** | View Grade Report (S4) — the per-problem grade tables (score / submission date / answer cells); Calendar (S6) — the month grid's lines (confirmed 2026-09-15). |
| **Observed** | The tables' cell borders "are too small and fail color contrast at all levels" (reviewer, eyedropper, 2026-09-15): thin lines below 3:1 against white, so the cell boundaries that separate one submission's date and score from the next are hard to make out for a low-vision reader; the table is the page's only presentation of the grade breakdown. |
| **Affected users** | Low-vision users; users with reduced contrast sensitivity |
| **WCAG criteria failed** | 1.4.11 |
| **Severity** | Minor (confirmed by the reviewer 2026-09-15) |
| **Evidence** | R030 O8 (S4); R042 O8 (S6) |

### View S5 — Assignment Editor

| | |
|---|---|
| **Baselines run** | axe (R006); probe runs R035–R040, R101; zoom + eyedropper (R036, 2026-09-15 — reviewer) |
| **Date tested** | 2026-09-11 (measured), 2026-09-14 (W40 ruling), 2026-09-15 (reviewer) |
| **Findings** | V-F19, V-F23 (recorded under S1) confirmed here; V-F21 exempt here (spinner values typeable); V-F26 |

#### Finding V-F26

| | |
|---|---|
| **Where** | Assignment Editor (S5) — the videos in the expanding area under **Library** (YouTube embeds), `UI: Assignment Editor → Library → expand`. |
| **Observed** | The videos carry captions, but they are YouTube **auto-generated** captions (reviewer, 2026-09-15: "they have captions and are YouTube embeds … they are auto generated"). Auto-generated captions are not an equivalent for the audio — speaker attribution, punctuation and, in physics content, symbols and units are unreliable — so 1.2.2 is not met by them. Not yet checked: whether the videos autoplay (1.4.2) and whether an audio description or transcript exists (1.2.3 / 1.2.5 — NV11 on R035). The probe's media sweep missed these embeds because the panel opens on demand. |
| **Affected users** | Deaf and hard-of-hearing users; users watching without sound |
| **WCAG criteria failed** | 1.2.2 |
| **Severity** | Major (confirmed by the reviewer 2026-09-15). **Kept in the report at the reviewer's ruling 2026-09-15 although the Assignment Editor (S5) left the sample as instructor-facing.** |
| **Evidence** | R037 O6 (reviewer); R035 (NV11 reopened) |

### View S7 — Sign in

| | |
|---|---|
| **Baselines run** | probe (R093–R098, signed-out profile); axe (R003) |
| **Date tested** | 2026-09-11 (measured), 2026-09-14 (reviewer) |
| **Findings** | V-F17; V-F18 applies here |

#### Finding V-F17

| | |
|---|---|
| **Where** | Sign in (S7, `login.theexpertta.com/Login.aspx`) — the "User Name:" field |
| **Observed** | The user-name field carries no `autocomplete` attribute, so its purpose (username) is not programmatically identified for browsers and assistive technologies that fill or label fields from it (1.3.5 requires the token on fields collecting the user's own data). The reviewer notes the practical mitigation: "no app specific autocomplete but works fine with chrome password manager" — Chrome's heuristic fill still works, which is why the severity is Minor. |
| **Affected users** | Users with cognitive or motor disabilities who rely on autofill and purpose-aware AT |
| **WCAG criteria failed** | 1.3.5 |
| **Severity** | Minor |
| **Evidence** | R098 O3 (`R098-probe.json`) |

---

### View S11 — Edit Class popup

| | |
|---|---|
| **Baselines run** | axe (R002); probe runs R073–R078; zoom (R078, 2026-09-15 — reviewer) |
| **Date tested** | 2026-09-11 (measured), 2026-09-15 (reviewer) |
| **Findings** | V-F5 (recorded under S2); V-F18 applies here; V-F25 |

#### Finding V-F25

| | |
|---|---|
| **Where** | Edit Class popup (S11) — `UI: Class Management → Class Menu → Edit Class → Go`; by construction the same for the other Class Menu popups (Create Class, Student/TA Registration, Create New Assignment). |
| **Observed** | The popup is a fixed-size (589 px) modal and the page behind it is locked against scrolling while it is open. Once browser zoom passes 175 % the popup no longer fits the viewport and "we can't scroll the page when it is active" (reviewer, 2026-09-15) — the fields, and the Save / Cancel buttons at the bottom, that fall outside the viewport cannot be reached by any means. At 200 % zoom (the 1.4.4 threshold) the form cannot be completed; at 400 % most of it is unreachable. Elsewhere in the product zoom loses nothing (LV2 pass on S1–S5). |
| **Affected users** | Low-vision users working at 200 % zoom or more; anyone on a small or narrow window |
| **WCAG criteria failed** | 1.4.4, 1.4.10 |
| **Severity** | Major (Blocker for the popup alone; confirmed by the reviewer 2026-09-15). **Kept in the report at the reviewer's ruling 2026-09-15 although the Edit Class popup (S11) left the sample as instructor-facing.** |
| **Evidence** | R078 O5 (reviewer); R078 O2 (probe: popup width 589 px, `R078-probe.json`) |

### View S14 — Password reset

| | |
|---|---|
| **Baselines run** | B5 NVDA (R121, 2026-09-21 — reviewer, NV6/NV8 only); axe (R122); probe runs R123–R128 |
| **Date tested** | 2026-09-21 |
| **Findings** | V-F30; V-F18 applies here (no `lang`); V-F19 applies here (no reflow) |

#### Finding V-F30

| | |
|---|---|
| **Where** | Password reset (S14, `login.theexpertta.com/ResetPassword.aspx`, reached from Sign in → "Trouble Logging in?") — the user-name field |
| **Observed** | The field has no label of its own. Tabbing into it, NVDA does not announce a label — it reads out the surrounding layout **table**, the same table-based construction used throughout the application. The reviewer: *"The form field for the user name in password reset isn't properly labeled, and like the rest of the app the whole reset form is structured in a table, tabbing into the form field and launch a voice notification describing the whole reset table, so it is accessible, but not best practice."* A screen-reader user can therefore work out what to type, from context rather than from a label, and the reviewer rules the page **usable**. axe reports the same defect independently on the same page (`label`, critical, one form element — R122). This is the account-recovery path: a student locked out of the product has no other route back in, which is why a merely-inferable field label matters more here than the Minor rating suggests. |
| **Affected users** | Screen reader users (the purpose is inferred from a table read-out, not stated); users with cognitive disabilities (a verbose table announcement in place of a field name) |
| **WCAG criteria failed** | 1.3.1 (label not programmatically associated); 3.3.2 (no label or instruction for a required input); 4.1.2 (no accessible name) |
| **Severity** | Minor (the reviewer's ruling 2026-09-21: "accessible, but not best practice" — the table read-out carries the meaning, so this is a quality defect, not a barrier) |
| **Evidence** | R121 O5 (reviewer, NVDA); R122 (`R122-axe.json`, `label` critical) |

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
