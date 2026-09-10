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

**Sequence notes:** (verdict stays Not run until steps 4–5 are walked; no-vision on S2 so far points to Pass with barriers) 2026-09-10, NVDA, Accessibility Mode (S2): step 1 sign-in not walked (already signed in). Step 2 Class Management: title fine (R016 O1); no headings/landmarks, the skip links are inert, and the two grids share one generic caption — the reviewer reaches the assignments table by `T`/Tab and identifies it by the focusable title div (R016 O2–O5). Step 3 (Accessibility Mode): row Actions select → "Take Assignment" → Go; page change announced (R016 O13) — completable. The Classes / Class Menu selects at step 2 are not distinguishable by name (V-F7). Steps 4–5 → R017.

#### Finding T1-F1

| | |
|---|---|
| **Where** | Step 2, Class Management in Accessibility Mode (S2) — reaching the assignments table |
| **Observed** | A screen-reader user arriving on the page has no headings (`H`) and no landmarks (`D`) to move by. The two data grids are reachable with `T` but carry the same generic caption ("Data table related to the headers above"), so the user cannot tell the assignments table from the news table until tabbing onto a focusable title div. The page's skip links do work (revised 2026-09-10: Enter moves focus to the next section's skip link) but are exposed as links with instruction-like wording. Task remains completable (reviewer: "I can navigate it successfully") by linear reading, the skip links, or table-key trial. Details: V-F1, V-F2, V-F3. Open: whether table navigation from the row's Go button works in browse mode (R016 O9). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1, 4.1.2 |
| **Severity** | Major |
| **Evidence** | R016 (O2–O5); R005 `R005-axe.json` (0 headings / 0 landmarks, link-shaped skip) |

---

### Task T2 — Answer and submit a problem — process P2, implements F2 and F8

| | |
|---|---|
| **User story** | As a student, I need to enter an answer with the part's widget (multiple choice, numeric with keypad, symbolic expression, drag-and-drop ranking, free-body diagram), submit it, and perceive the result, using hints or feedback when stuck. |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B1, B2, B3 |
| **Date(s) tested** | |

**Sequence notes:** (per-step observations; identify the step where each
barrier occurs)

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
| **Observed** | The control has no accessible name (axe `aria-command-name` on all 14 views). On Class Management, Enter changes its text to "No Shortcuts" and navigates nowhere; no shortcuts menu opens. The user meets an unnamed button whose activation produces an unexplained state change. |
| **Affected users** | Screen reader users; keyboard users |
| **WCAG criteria failed** | 4.1.2 |
| **Severity** | Minor on this page (to be re-rated on Take Assignment, where the shortcuts menu is expected — R017) |
| **Evidence** | R016 O12; R005 / R001 `*-axe.json` |

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
