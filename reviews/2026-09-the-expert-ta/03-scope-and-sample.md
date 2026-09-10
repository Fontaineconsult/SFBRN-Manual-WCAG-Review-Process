# Scope & Sample — The Expert TA

WCAG-EM 2.0 steps 1–3 (see `ontology/wcag-em.md`). Work through the sections in
order; WCAG-EM allows returning to an earlier step as exploration or testing
reveals new information.

> Seeded from enclosure `lms` (Learning management system / courseware — courses, assignments, quizzes, grades, discussions). Rows in Step 2 and the
> process skeletons are hypotheses — confirm, correct, or delete them
> during exploration.

## Step 1 — Define the evaluation scope

### 1.1 Scope of the product (principle of product enclosure)

The scope must enclose the **full product**: all views, states, and
functionality, without excluding specific parts. Define the boundary
unambiguously (URL patterns, app areas, screen lists) so that for any view it
is clear whether it is in scope.

| Field | Value |
|-------|-------|
| Product boundary | (proposed 2026-09-10 — confirm) The signed-in application at `https://dei56mo.theexpertta.com/` — every `/Common/*`, `/Instructor/*`, `/Tutorial/*` and `/controls/*` page, in **both** UI modes (standard, and the "Accessibility Mode" variant reached by the Accessibility Page button) — plus authentication at `https://login.theexpertta.com/` and class registration at `https://reg.theexpertta.com/`. The `dei56mo` host prefix is the deployment the login redirects to; treat it as the product host. |
| Easily missed inclusions | (proposed 2026-09-10) Accessibility Mode (`/common/default2.aspx`, a parallel version of Class Management, persisted per account); DevExpress popup iframes that host whole sub-forms inside Class Management (Create/Edit Class `eClass.aspx`, Student/TA Registration `eClassRegistration.aspx`, Create News `eNews.aspx`, Copy Assignment `eAssignmentCopy.aspx`); Practice Mode and Printable Assignment views; the per-question "Show/Hide Accessibility Statement" panels; the instructor preference pages under the Instructor menu; the on-screen symbol/number keypads inside answer widgets. |
| Third-party content / services | (confirmed 2026-09-10) DevExpress ASP.NET controls (`DXR.axd` resources, `ASPx.*` client API — grids, combo boxes, popups); MathJax 2.7.4 from `cdn.theexpertta.com`; jQuery 1.x + jQuery UI + jquery-migrate; Backbone + lodash; Zwibbler 2 (drawing canvas library, loaded on the assignment page); Google Forms (anonymous feedback link on Class Management); marketing/help site `theexpertta.com` (Help menu targets). Not reachable in the demo: Canvas LTI launch, Respondus LockDown Browser. |
| Exclusions and justification | (proposed 2026-09-10 — reviewer decides) `theexpertta.com` marketing and help pages — separate content site; sample only the two support pages reached from the in-app Help menu (A2), because Section 508 Ch. 6 covers support documentation. `reg.theexpertta.com` student self-registration and payment — not exercisable without creating a paid account; record as a coverage limitation, not a pass. Canvas LTI launch and grade pass-back — blocked until the campus enables the integration, which happens only after this review; coverage limitation. |

### 1.2 Conformance target

**Primary: WCAG 2.1 Level AA** — the ADA Title II baseline binding CSU as a
public entity. **Additionally evaluated: WCAG 2.2 Level AA** (the six added
criteria; 4.1.1 treated as met per the WCAG 2.2 erratum). Optionally note
higher-level (AAA) criteria observed as
advisory findings.

### 1.3 Accessibility support baseline

The minimum operating system + browser + assistive technology combinations the
product is expected to work with. Task testing (`04-task-testing.md`) runs
against these. Extend the baseline (add rows) if additional combinations are
used during evaluation.

| ID | OS | Browser | Assistive technology / input |
|----|----|---------|-----------------------------|
| B1 | Windows 11 | Chrome | JAWS 2026 (installed; not the instrument in use — see B5, W1 2026-09-10) |
| B2 | (any) | (any) | Keyboard only (no pointer) |
| B3 | (any) | (any) | 400% zoom / reflow |
| B4 | macOS | Safari | VoiceOver (optional) |
| B5 | Windows 11 Home 10.0.26200 (build 26200.9168) | Chrome 153.0.8010.36 (debug profile) | **NVDA 2026.2** — confirmed 2026-09-10 (W1) as the screen reader for this review's no-vision runs. JAWS 2026 is installed on the same machine (B1) but not in use unless a step says so; the vendor states its testing covered JAWS, NVDA and VoiceOver, so NVDA verifies that claim for one of the three. |

### 1.4 Additional evaluation requirements (optional)

(e.g., report every occurrence rather than representative examples; analyze
specific user groups; involve users with disabilities.)

- CSU East Bay reviews to WCAG 2.1 Level A/AA (Zach Oshri, 2026-09-01); this
  review additionally records the WCAG 2.2 AA criteria per §1.2.
- A TAAP is already in draft (Jonathan Hale, 2026-08-13) on the strength of the
  vendor's admitted drag-and-drop labeling barrier. Testing should establish
  whether the instructor-side question filter makes the faculty remediation
  enforceable, and whether the three admitted question types are the *only*
  barriers — that is what the TAAP's scope depends on.
- Report every occurrence for the three vendor-admitted question types; the
  vendor's ~99% coverage figure (6,719 of 6,790 physics questions) is a claim to
  check against the question browser, not to repeat.

### 1.5 Testing tools

The declared instruments for this review — versions recorded before testing
starts, updated if they change. Capture conventions per tool:
`ontology/testing-tools.md`. Every test session is logged with
`review.py log-test`, which records the page/view, date, tool, and baseline,
and creates the run's evidence folder.

| Tool | Type | Version used | Purpose | Output captured per run |
|------|------|--------------|---------|-------------------------|
| JAWS (Freedom Scientific) | Screen reader — manual testing | 2026 installed (2026-09-10); not in use | Walk task sequences and inspect views as a screen reader user | Action/announced/expected notes, speech history excerpts, screenshots |
| NVDA (NV Access) | Screen reader — manual testing (reviewer-driven), baseline B5 | 2026.2 (2026-09-10); in use | Walk task sequences and inspect views as a screen reader user | Action/announced/expected notes, Speech Viewer excerpts, screenshots |
| WAVE (WebAIM) browser extension | Automated checker | | Sweep every sampled view and state | Summary counts, error list, annotated screenshots |
| axe-core via `scripts/axe_scan.py` | Automated checker (primary sweep) | 4.10.3 in Chrome 153.0.8010.36 | Sweep every sampled view and state over CDP (no shadow DOM here, so WAVE is usable too) | Raw `R###-axe.json` + summary |
| CDP exploration probes (`scripts/crawl_map.py`, `scripts/cdp_probe.py`) | Recon instrument — step 2 only | Chrome 151 debug profile | Fingerprints, accessibility-tree summaries, screenshots during mapping; never a source of findings | `crawl-map-<date>.md` beside the review |

## Step 2 — Explore the target product

Seeded from the LMS archetype. Every row is a hypothesis: confirm it exists,
correct the details, delete what doesn't apply, and add what exploration
reveals. Test both student and instructor roles.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Sign in | `https://login.theexpertta.com/Login.aspx` — confirmed 2026-09-10: ASP.NET WebForms form (user name = e-mail, password, "Trouble Logging in?" → `/ResetPassword.aspx`); requires JavaScript + cookies; redirects to the app host after sign-in. No campus SSO in the demo. |
| C2 | Dashboard / course list — **"Class Management"** | `https://dei56mo.theexpertta.com/common/default.aspx` — confirmed 2026-09-10. Single page = C2 and C3: Classes combo box, Class Menu combo box (13 actions), Class Assignments grid (DevExpress; each row opens a 13-item action menu on click), Class News, Calendar and Accessibility Page buttons. No landmarks, no headings, layout tables. |
| C3 | Course home | Same page as C2 (confirmed 2026-09-10 — one class per view, selected in the Classes combo). |
| C4 | Module / content page | No LMS-style content pages in this product (confirmed 2026-09-10). Nearest read-only content views: View Printable Assignment `https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx` and View Assignment Solutions `https://dei56mo.theexpertta.com/Common/ViewAssignmentSolutionsV2.aspx` (the only view with a real heading outline: h1 + h2 per problem). The vendor's eReader/eBook is **not provisioned in the demo** (hypothesis — ask vendor). |
| C5 | Assignment view + submission — **"Take Assignment"** | `https://dei56mo.theexpertta.com/Common/TakeTutorialAssignment.aspx` — confirmed 2026-09-10; reached via `UI: Class Management → assignment row → Take Assignment`. The core working surface: problem/status navigator (9 problems), problem statement with MathJax, per-part answer widgets, Submit / Hint / Feedback / I give up, grade summary, submission history, Instructor/TA Admin toggle. |
| C6 | Quiz / exam | Same surface as C5 with dates and deductions (confirmed 2026-09-10). Practice Mode `https://dei56mo.theexpertta.com/Common/TakeAssignmentInPracticeMode.aspx` exists but the sample assignment is not configured for it. Secure/timed exams and Respondus not provisioned in the demo (hypothesis). |
| C7 | Grades | Student-facing: View Grade Report `https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547` — confirmed 2026-09-10. Instructor: Class grade sheet `https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignments.aspx?m=1&eid=3373`, assignment spreadsheet `https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignmentProblems.aspx?m=1&eid=3373&aid=17547`, Manage Grades `https://dei56mo.theexpertta.com/Common/AssignmentGrade.aspx?m=2&eid=3373&aid=17547` — all confirmed 2026-09-10. |
| C8 | Discussion board | **Absent** (confirmed 2026-09-10) — no discussion feature; "Class News" is one-way instructor announcements. |
| C9 | Calendar / notifications | Calendar `https://dei56mo.theexpertta.com/common/calendar.aspx` — confirmed 2026-09-10: month grid (h2 month title, class filter checkboxes, prev/next/today). No notification centre found; `ViewAssignmentNotifications.aspx` is referenced in page source (hypothesis). |
| C10 | Class Management — **Accessibility Mode** | `https://dei56mo.theexpertta.com/common/default2.aspx` — confirmed 2026-09-10. Parallel version of C2 toggled by the "Accessibility Page" / "Non-Accessibility Page" button and **persisted server-side per account** (`default.aspx` redirects here while on). Native `<select>` + "Go" buttons replace the DevExpress combos and row menu; skip links ("Tab for Assignments, Enter to skip"), table captions, and inline keyboard instructions are added. Only this page has a variant — C5, C9 etc. are identical in both modes. |
| C11 | Assignment Editor | `https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547` (edit) / `?m=1&eid=3373` (create) — confirmed 2026-09-10: details form, problem list, library browser (Books / Chapters / Sections, difficulty filters) with the **"Accessibility(AA) Only"** checkbox, default unchecked; toolbar incl. Extensions, Security, Messages, Preview. |
| C12 | Class roster | `https://dei56mo.theexpertta.com/Common/vwMates.aspx?m=1&eid=3373` — confirmed 2026-09-10 (empty roster in the demo). |
| C13 | Problem library browsers | Problem Solutions `https://dei56mo.theexpertta.com/Instructor/ClassProblemSolutionSelection.aspx?m=1&eid=3373` and Student Practice Area `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` — confirmed 2026-09-10 (same layout: Books / Chapters / filters). |
| C14 | Analytics | Class Analytics `https://dei56mo.theexpertta.com/Common/ClassAnalytics.aspx?z=1&vmid=1&eid=3373`, Assignment Analytics `https://dei56mo.theexpertta.com/Common/AssignmentAnalytics.aspx?m=2&eid=3373&aid=17547` — confirmed 2026-09-10. |
| C15 | Account & preferences | My Account `https://dei56mo.theexpertta.com/Common/MyAccount.aspx`, Change Password `https://dei56mo.theexpertta.com/Common/ePassword.aspx`, Grade Preferences `https://dei56mo.theexpertta.com/Instructor/InstructorGradeTemplates.aspx`, Academic Integrity Preferences `https://dei56mo.theexpertta.com/Instructor/AcademicIntegrityTemplates.aspx`, Randomized Variables Phrases `https://dei56mo.theexpertta.com/Common/RandomizedVariablesPhrases.aspx`, Restore Deleted Assignments `https://dei56mo.theexpertta.com/Common/RestoreDeletedAssignment.aspx` — confirmed 2026-09-10 (the two Instructor/* pages are the only ones with a `main` landmark). |
| C16 | Popup sub-forms inside Class Management | Create Class / Edit Class (`/Common/eClass.aspx?m=1|2&eid=3373`), Student/TA Registration (`/Common/eClassRegistration.aspx?eid=3373`), Create News (`/Common/eNews.aspx?m=1&eid=3373`), Copy Assignment (`/Common/eAssignmentCopy.aspx?m=2&eid=3373&aid=17547`) — confirmed 2026-09-10: each loads in a DevExpress popup **iframe** over C2/C10 (`UI: Class Management → Class Menu → <item> → Go`). |
| C17 | Other instructor tools | Copy Assignment/Clone Class `https://dei56mo.theexpertta.com/Common/CopyAssignmentCloneClass.aspx?z=1&vmid=1&eid=3373`, Batch Date/Time Update `https://dei56mo.theexpertta.com/Common/AssignmentDates.aspx?z=1&vmid=1&eid=3373`, Consolidate/Export Grades `https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignmentsMultiClass.aspx?z=1&vmid=1&eid=3373`, Export Text Answers `https://dei56mo.theexpertta.com/Common/TextBasedAnswers.aspx?m=2&eid=3373&aid=17547` — confirmed 2026-09-10. |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a student, I need to access course content including embedded media, so that I can learn the material. | Core purpose |
| F2 | As a student, I need to answer and submit homework problems — numeric, symbolic-expression, multiple-choice, drag-and-drop ranking, and free-body-diagram parts — so that my work is graded. (No file upload in this product — confirmed 2026-09-10.) | High stakes |
| F3 | As a student, I need to complete an assignment under its due/end dates and submission limits — including with an extended-time accommodation — so that I can demonstrate learning without being timed out. | High stakes; timing = 2.2.1 (session extension script present — see §2.6) |
| F4 | As a student, I need to check my grades and feedback, so that I know my standing. | Core workflow |
| F5 | ~~Discussions~~ — **not applicable**: the product has no discussion feature (confirmed 2026-09-10). Kept for ID stability. | — |
| F6 | As an instructor, I need to manage grades (grade sheet, manual grading, export) and the roster, so that the course runs. | Staff-facing side |
| F7 | As an instructor, I need to author an assignment from the problem library — including using the "Accessibility(AA) Only" filter — so that students get accessible problems. (added 2026-09-10; essential because the campus TAAP relies on this filter — reviewer to confirm) | Staff-facing; TAAP dependency |
| F8 | As a student, I need to use hints and feedback, see submissions remaining and deductions, and read my grade report, so that I can manage my grade. (added 2026-09-10 — reviewer to confirm essentiality) | Core workflow |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Answer widgets — multiple choice / true-false / multiple select | Native radio/checkbox inputs with MathJax labels | S3 problems 8–9 (confirmed 2026-09-10) |
| Answer widgets — numeric ("Algorithm") | Text input + on-screen function/number keypad (~45 buttons) + unit radios | S3 problems 4, 5, 7 (confirmed 2026-09-10) |
| Answer widgets — symbolic expression ("Equation") | The **calculator**: custom answer field + variable/symbol palette keypad (reviewer's term, 2026-09-10); a distinct component to test for reachability, button naming, insertion and read-back | S3 problems 1, 2, 6, 7 (confirmed 2026-09-10) |
| Answer widgets — free-body diagram | SVG drawing tool: Add Force / Reset All, force table (angle, length, delete) | S3 problems 1, 6 (confirmed 2026-09-10) |
| Answer widgets — drag-and-drop ranking/sorting | jQuery-UI-style draggables into a ranked drop zone; per-question "Show/Hide Accessibility Statement" | S3 problem 3 (confirmed 2026-09-10) |
| Answer widgets — vendor-admitted inaccessible types | Drag-and-drop labeling, hotspot / click-on-image, vector practice | **Not in the sample assignment** — reviewer must author one (P4) |
| Answer widgets — other | Schematic choice/select, short response, essay (with drawing interface), graded simulation | Schematic choice in S3 problem 2 (confirmed 2026-09-10); rest hypothesis |
| Math content | MathJax 2.7.4 rendering with MathML exposed to the accessibility tree; "human-friendly" spoken math claimed | S3 (confirmed 2026-09-10) |
| Data tables | DevExpress grids: assignments list, grade sheets, roster, submission history | S1, S4, S9, S10 (confirmed 2026-09-10) |
| Timed interactions | Assignment begin/due/end dates, late-work percentage, submissions remaining; session-extension script | S3 (confirmed 2026-09-10); session timeout behaviour hypothesis |
| Rich text editors | None seen yet; Create News and Assignment Description may carry one | Hypothesis — check S11 / C16 |
| File upload | None found (confirmed 2026-09-10) | — |
| Modals & popups | DevExpress popup iframes (Create/Edit Class, Registration, News, Copy), assignment row action menu, jQuery bubble popups | S1, S11 (confirmed 2026-09-10) |
| Alternate-version UI | Class Management "Accessibility Mode" with native selects, skip links, instruction text | S2 (confirmed 2026-09-10) |
| Keyboard/speech assistance layer | Focus-box jump points, Enter-opened shortcuts menu, Ctrl+Shift+1…5 read-out functions into an `aria-live` region | S3 (confirmed 2026-09-10) |
| Content pages | Printable assignment, assignment solutions (h1/h2 outline) | S8 (confirmed 2026-09-10) |
| Calendar | Month grid with class filters | S6 (confirmed 2026-09-10) |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript / WAI-ARIA | Confirmed 2026-09-10: ASP.NET WebForms (`.aspx`, `WebResource.axd`, postbacks/callbacks) with **DevExpress ASPx** controls; jQuery 1.x + jQuery UI + jquery-migrate; Backbone + lodash; vendor scripts `ETACore`, `ETAProbNav`, `ETAAccessibilityFunctions`, `ETADND`, `ETAVec`, `ETACOI`, `ETALibGFBD`, `ETAMQ`. Layout tables everywhere (15–20 per page); **no shadow DOM**; ARIA limited to `aria-live` regions, `.sr-only` text, `title` attributes. JavaScript and cookies required. |
| Landmarks / headings | Confirmed 2026-09-10: no landmarks on any view except a `main` on the two Instructor preference pages; no headings on any view except Calendar (h2) and View Assignment Solutions (h1 + h2s). |
| Rich text editor | Unknown — none seen; hypothesis for Create News / Assignment Description / essay questions |
| Embedded media players | None seen in the demo (vendor claims captions/transcripts/audio description for its video library — hypothesis) |
| PDF and office documents | None seen; eReader/eBook not provisioned in the demo (hypothesis) |
| Iframes | Confirmed 2026-09-10: DevExpress popup iframes host Create/Edit Class, Registration, News, Copy Assignment inside Class Management; `DXR.axd` helper frames |
| LTI / SSO | LTI 1.1 and 1.3 launches from Canvas, Blackboard, Brightspace/D2L, Moodle; grade pass-back (vendor-stated). No SSO in the demo; direct login only. |
| MathJax | Confirmed 2026-09-10: MathJax **2.7.4** (config `ETAMQ_240412`, served from `cdn.theexpertta.com`) with assistive MathML — `MathMLMath` nodes present in the accessibility tree; the visible rendering duplicates each expression (rendered + hidden MathML). |
| Drawing / canvas | Free-body diagram tool renders **SVG** (no `<canvas>`); Zwibbler 2 canvas library is loaded but unused on the sampled problems (hypothesis: used by essay-with-drawing / vector practice). |
| Drag-and-drop | Confirmed 2026-09-10: vendor `ETADND` on jQuery UI; draggable cards into a ranked drop zone; keyboard alternative claimed via the shortcuts layer. |
| On-screen keypads | Confirmed 2026-09-10: numeric and symbolic answer parts render 40–50 `<button>`s (digits, functions, symbols, HOME/END/arrows). |
| Live regions / speech layer | Confirmed 2026-09-10: `#calc-announce` (`aria-live=polite`) and `#calc-live`; `role=alert` container; Ctrl+Shift+1 previous part, +2 read answer, +3 supplemental/cursor/unmatched items, +4 details, +5 instructions; Ctrl+Alt+J jump points; focus-box jump points (top of page, problems, problem statement, each part) with instruction text and an Enter-opened "accessibility shortcuts menu". |
| Respondus LockDown Browser | Secure-exam delivery path — hypothesis; outside the browser baseline unless procurement includes it |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | Public: https://theexpertta.com/about/accessibility-statement/ and https://theexpertta.com/support/accessibility/. In-app (confirmed 2026-09-10): the "Accessibility Page" mode toggle on Class Management (S1 ↔ S2) and the per-question "Show/Hide Accessibility Statement" icon on drag-and-drop parts (S3 problem 3). |
| A2 | Help / student support | In-app Help menu (confirmed 2026-09-10) → external: http://theexpertta.com/help-links/, https://theexpertta.com/support/instructor-support/, https://theexpertta.com/support/student-support/, https://theexpertta.com/contact-us/. "For help on this page click here" links on Assignment Editor and Manage Grades (target not yet followed). |
| A3 | Authentication | https://login.theexpertta.com/Login.aspx (confirmed 2026-09-10; direct login, no SSO; password reset `/ResetPassword.aspx`). LTI launch from Canvas is the campus path — not testable in the demo. |
| A4 | Accommodation settings (extra time, etc.) | Not yet located. Candidates (hypothesis 2026-09-10): the roster page `/Common/vwMates.aspx` (vendor says "roster-level") and the **Extensions** button on the Assignment Editor toolbar. |
| A5 | Notification preferences | None found (confirmed 2026-09-10). Assignment-level **Messages** button on the Assignment Editor and `ViewAssignmentNotifications.aspx` in page source — hypothesis. |

### 2.6 Exploration notes (recon for testing — not yet findings)

Dated observations from exploration sessions (see
`ontology/assisted-exploration.md`): machine-extraction results, suspected
issues phrased as "verify X under check Y in a run", artifacts created during
exploration, and replication quirks (e.g., SPA views whose URL does not
change). Nothing here is a finding until a logged run verifies it.

Pre-exploration recon from the procurement email thread (`evidence/email.txt`,
2026-07-27 → 2026-09-01) and the web scout of 2026-09-08 — nothing below has
been seen in the product yet:

- **Drag-and-drop labeling questions** — vendor admits non-compliant (54 physics
  questions); campus reports they contain images of text that do not scale
  independently. Verify under 1.4.5 / 1.4.4 (low-vision zoom check), 2.1.1
  (keyboard alternative), and 2.5.1 / 2.5.2 (pointer gestures, cancellation) in
  a run on a sampled assignment containing one.
- **Hotspot / click-on-image questions** — vendor admits non-compliant; states
  0 exist in the physics library. Verify the count claim in the instructor
  question browser; if any can be authored, verify under 2.1.1 and 1.1.1.
- **Vector practice questions** (17) — vendor admits non-compliant. Verify what
  the interaction is and record the modality it blocks.
- **Instructor "filter out non-WCAG-AA questions" checkbox** — vendor's
  mitigation. Verify it exists, what it excludes, and whether it defaults on;
  this determines whether the TAAP faculty remediation is enforceable.
- **Free-body-diagram drawing question** — vendor claims fully accessible.
  Verify under no-vision (JAWS) and motor (keyboard-only) checks; a drawing
  interaction that passes both would be unusual.
- **Sorting and ranking drag-and-drop** — vendor claims compliant. Verify the
  keyboard alternative (2.1.1) and the announced state changes (4.1.3).
- **Context-specific keyboard menus while tabbing** (modelled on ada.gov) —
  vendor claim. Verify under 2.4.3 focus order and 3.2.1 on-focus (a menu
  appearing on focus must not be a context change) and 1.4.13.
- **Human-friendly spoken math** ("cosine of forty five point two") with a
  toggle to the literal form — verify what JAWS actually receives (MathJax
  accessibility extension vs. MathML vs. hidden text) and where the toggle is.
- **Extended-time roster setting** — verify it exists and is per-student
  (2.2.1 timing adjustable; §2.5 A4).
- **1.4.3 / 1.4.5** — the vendor's own VPAT remarks describe exceptions;
  contrast measurement is worth doing early on the assignment view.
- **Login requires JavaScript and cookies** (login page message) — not a WCAG
  failure by itself; note whether the no-JS message is itself accessible.
- **Replication:** the demo is direct login (ASP.NET `.aspx` pages) — expect
  postback URLs that do not identify views; record `UI:` paths where the URL
  is not durable. The shared account means other campus staff may change the
  course state between sessions; record the assignment name and ID at each
  session start.
- **Out of reach in this environment:** Canvas LTI launch and grade
  pass-back; student self-registration and payment; Respondus LockDown
  Browser exams. Record as coverage limitations in `06`, not as passes.

Session 2026-09-10, exploration only, signed in as the shared demo instructor
account on the debug-profile Chrome 151 (CDP probes: `crawl_map.py` harvest/map
plus ad-hoc screenshot / text / control / accessibility-tree probes; no
browser extension). Raw map: `crawl-map-2026-09-10.md`. **No forms were submitted and
no answers were submitted**; the only state changes were toggling Accessibility
Mode on and back off (restored) and opening problems 1–9 of the sample
assignment (problem 9 left active — someone had left problem 8 active before).

- **Machine extraction is complete here** — no shadow DOM, the DOM and the
  accessibility tree agree, and `Accessibility.getFullAXTree` returns 300–550
  nodes per view. What it shows: layout tables everywhere, **no landmarks**
  and **no headings** on Class Management, Take Assignment, My Account,
  grade sheets, roster, editor (see §2.4). Verify under the no-vision
  structure checks (1.3.1, 2.4.1, 2.4.6) in JAWS runs on S1 and S3 — the
  visually obvious section titles ("Classes", "Class Menu", "Class
  Assignments", "Problem 8:", "Part (a)") are styled text, not headings.
- **Two-mode architecture** (S1 ↔ S2): the Accessibility Page button toggles
  Class Management into a native-controls variant and the choice is persisted
  per account (server-side; `default.aspx` redirects to `default2.aspx` while
  on). Verify: (a) which mode a **new student** lands in by default; (b)
  whether the non-accessibility page meets WCAG on its own, or whether the
  product relies on the conforming-alternate-version provision (the toggle is
  reachable from the inaccessible page — that condition looks met); (c) every
  run on S1/S2 must record which mode was active. Only Class Management has
  the variant — every other view is single-mode.
- **Unnamed radio buttons** — on S3 problems 8 and 9 all 6 (resp. 5)
  `<input type=radio>` answer options have **no accessible name** in the
  accessibility tree (the option text sits in adjacent MathJax spans/cells,
  not in a label). Verify under 1.3.1 / 4.1.2 with JAWS: does it announce
  "radio button, not checked" with no option text? Four unnamed `button`
  nodes also appear in the tree on S3 (identify them in the run).
- **Keyboard/speech layer is real and substantial** (§2.4). Recon to verify
  with JAWS on S3: do the Ctrl+Shift+digit chords reach the page under JAWS
  (JAWS may consume some), and are the `aria-live=polite` read-outs actually
  spoken (4.1.3)? Do the focus-box jump points appear in the tab order for a
  sighted keyboard user with a visible focus indicator (2.4.7), and does
  Enter on one open the "accessibility shortcuts menu" as the instruction
  text says? Is any of this discoverable without reading the vendor's page?
- **Question-type inventory of "Chapter 5 Sample Assignment" (aid=17547):**
  P1 FBD + Equation×2 + Algorithm (5.3.5 iFBD); P2 Equation + Schematic
  Choice + Algorithm (5.3.2); P3 Drag-and-drop ranking (c5.3.8); P4
  Algorithm×2 with unit radios (5.3.22); P5 Algorithm (5.3.18); P6 FBD +
  Equation×2 + Algorithm×2 (5.3.12 iFBD); P7 Equation + Algorithm×3 (5.3.9);
  P8, P9 Multiple choice (c5.3.1, c5.3.2). **None of the three vendor-admitted
  inaccessible types (labeling DnD, hotspot, vector practice) is in the
  sample** — the reviewer must author a second assignment containing them
  (process P4, with the Accessibility(AA) filter *off*) and register the
  artifact here.
- **"Accessibility(AA) Only" library filter** confirmed on the Assignment
  Editor (S5), a checkbox in the Library → Sections row, **default
  unchecked**. Verify in P4 that it removes exactly the admitted types and
  nothing else; the campus TAAP's faculty remediation depends on it.
- **Figure images:** the problem figure on P1, P4, P5 carries descriptive
  alt text; on P6, P7, P8, P9 the figure `<img>` has **empty alt** although
  it conveys the physical setup (pulley/blocks). Verify under 1.1.1 with JAWS
  (is the diagram described anywhere else — e.g. in the "details" read-out?).
- **On-screen keypads** put 40–50 buttons per numeric/symbolic part into the
  page. Verify under 2.4.3 / motor checks whether they sit in the tab order
  (a keyboard user would tab through ~45 buttons per part) and whether they
  have names (`title`s were present on the ones sampled).
- **Reflow:** both Class Management modes and Take Assignment show a
  horizontal scrollbar at a 1280 px-wide viewport (DevExpress grid and the
  assignment header overflow). Verify under 1.4.10 at 320 CSS px (400 %
  zoom) — likely a real failure, but measure it.
- **Anti-cheating watermark** — the signed-in e-mail and a hash are painted
  faintly across the problem area on S3. Verify it is not exposed to AT and
  does not sit under text for the contrast measurement (1.4.3).
- **Session extension script** (`SessionExtend.js`) is loaded on S3 —
  expect a session timeout with a warning/extend dialog. Verify under 2.2.1
  (timing adjustable) and 2.2.6 advisory; find the timeout length.
- **Popup sub-forms** (C16) open as DevExpress iframes over Class Management
  with no `role=dialog` / `aria-modal` found in the DOM. Verify focus
  movement into and out of the popup and Escape handling (2.4.3, 4.1.2) in a
  keyboard run on S11.
- **Practice Mode** returns "not currently configured to allow practice mode"
  for the sample assignment; the Extensions button on the editor and the
  roster are the candidates for the extended-time accommodation (A4) — walk
  them with the reviewer (side-effectful forms).
- **Harvest technique for this app:** the standard-mode navigation is JS/
  combo-box driven (root harvest found 9 links), but in Accessibility Mode
  the assignment action `<select>` carries every action URL as its option
  values, and the Class Menu select + Go button reaches every class tool —
  that is how the C11–C17 URLs were confirmed.
- **Replication:** URLs are durable with `eid=3373` (class "Testing Course
  for CSU East Bay") and `aid=17547` ("Chapter 5 Sample Assignment"); the
  `z=1` / `m=1|2` / `vmid=1` parameters are mode switches, keep them as seen.
  Take Assignment has no assignment parameter in its URL — use the `UI:` path.
- **Single-session enforcement (2026-09-10, during the axe batch):** after
  the S1 sweep (R001), every navigation in the debug tab bounced to
  `/WSInvalidAccess.aspx` ("Multiple Session Instances … you are using Expert
  TA in more than one tab"), and the session stayed invalid until re-login.
  The direct `eClass.aspx` and the login page still rendered (R002, R003).
  **Cause established later the same day:** opening the app in a *second tab
  of the same profile* produces `/WSInvalidAccess.aspx` immediately (the probe
  attached to a blank tab and navigated it while Class Management was open in
  another). Closing the duplicate tab and reloading the original restored the
  session without re-login. Consequence for testing: exactly one Expert TA tab
  in one window; the CDP scripts now attach only to that tab (ratchet in
  `crawl_map.py` / `cdp_probe.py`). Resolved the
  same day: the debug-profile Chrome had been closed; relaunching it found
  the profile's session still valid and all remaining sweeps ran
  (R004–R014). Recon to verify: whether the timeout warning promised by
  `SessionExtend.js` ever appeared (2.2.1) — nothing was shown in the tab
  before the bounce.
- **Axe sweep pattern across all 14 sampled views (2026-09-10, R001–R014):**
  every signed-in view shares the same five defects — unlabeled DevExpress
  editors, unnamed `focus-box` jump-point buttons, a focusable
  `aria-hidden` logo link, no landmarks/headings, and section-caption
  colours below 4.5:1 — so the findings should be written once product-wide
  with a per-view list, not 14 times. View-specific items to chase first:
  unnamed answer radios on multiple-choice parts (R004 O1), the broken
  `alt=` markup on figure images (R014 O1 — check whether Take Assignment's
  empty-alt figures are the same bug), the unnamed per-row Actions select
  in Accessibility Mode (R005 O1), and the `#FF6347` randomized-variable
  colour at 2.94:1 on S3/S4/S8 (R004 O10).
- **Mode state (2026-09-10, W4):** the shared account was in **Accessibility Mode** when the reviewer started (the assistant had restored standard mode at 10:49). The reviewer switched it on before W4 (answered). Every run now records the mode; the S1 (standard) no-vision pass is still owed under R015.
- **Document registry:** class eid=3373 "Testing Course for CSU East Bay";
  assignment aid=17547 "Chapter 5 Sample Assignment" (9 problems, weight 1,
  due 2026-09-08 — already past due: late-work rules apply to any
  submission; the instructor may need to extend the end date before the
  reviewer submits answers). Roster is empty. No artifacts created this
  session.

## Step 3 — Select the representative sample set

If feasible (few views, or a document), evaluate the entire product and skip
sampling — record that decision here.

### 3.1 Structured sample set

Must reflect **all** of: common views (2.1), essential functionality (2.2),
sample types (2.3), technologies relied upon (2.4), and other relevant samples
(2.5). One sample may represent several of these — record what it represents.

| ID | View / screen | Location / path | Represents (C/F/type/tech/A refs) |
|----|---------------|-----------------|-----------------------------------|
| S1 | Class Management (standard mode) — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/common/default.aspx` | C2, C3; F4, F6; data tables, DevExpress combos, row action menu, popups; tech: DevExpress |
| S2 | Class Management — Accessibility Mode — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/common/default2.aspx` (`UI: Class Management → "Accessibility Page"`) | C10; A1; alternate-version UI, native selects, skip links |
| S3 | Take Assignment — "Chapter 5 Sample Assignment", problems 1–9 — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/TakeTutorialAssignment.aspx` via `UI: Class Management → assignment row → Take Assignment` | C5, C6; F2, F3, F8; every answer-widget type in the sample, MathJax, keypads, DnD, FBD, live regions, session timer |
| S4 | View Grade Report — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547` | C7; F4, F8; data tables |
| S5 | Assignment Editor (edit) — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547` | C11; F7; library browser, "Accessibility(AA) Only" filter, Extensions/Messages (A4/A5 candidates) |
| S6 | Calendar — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/common/calendar.aspx` | C9; calendar grid, checkboxes |
| S7 | Sign in — proposed 2026-09-10 | `https://login.theexpertta.com/Login.aspx` | C1; A3; form, no-JS message |
| S8 | View Assignment Solutions — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/ViewAssignmentSolutionsV2.aspx` via `UI: Class Management → assignment row → View Assignment Solutions` | C4; content page with heading outline, MathJax, figures |
| S9 | Class Assignments Grade Sheet — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignments.aspx?m=1&eid=3373` | C7 (instructor); F6; data tables, export controls |
| S10 | Manage Class Roster — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/vwMates.aspx?m=1&eid=3373` | C12; F6; A4 candidate; data table |
| S11 | Edit Class popup — proposed 2026-09-10 | `UI: Class Management → Class Menu → Edit Class → Go` (iframe `/Common/eClass.aspx?m=2&eid=3373`) | C16; popup iframe/modal semantics, form fields |
| S12 | Student Practice Area — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` | C13; student-facing library browser |

### 3.2 Randomly selected sample set

Size: **10% of the structured sample set**, selected randomly from in-scope
views not already sampled. Record the selection method (crawler, full listing,
server logs…) so the selection is replicable. These are compared against the
structured set in `04-task-testing.md` §C.

| ID | View / screen | Location / path |
|----|---------------|-----------------|
| R1 | Academic Integrity Preferences — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Instructor/AcademicIntegrityTemplates.aspx` |
| R2 | View Grades (Spreadsheet) — proposed 2026-09-10 | `https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignmentProblems.aspx?m=1&eid=3373&aid=17547` |

**Selection method:** (proposed 2026-09-10) 12 structured samples → 10 % rounded up = 2. Pool = the 20 confirmed in-scope views not in §3.1 (listed in `crawl-map-2026-09-10.md`); drawn with Python `random.Random(20260910).sample(pool, 2)` in the order the pool is listed there. Re-draw if the structured set changes.

### 3.3 Complete processes — task sequences

Expand each essential-functionality user story (2.2) into a process. Record
the **default sequence** (standard use case: no input errors, no optional
branches) and the **critical branch sequences** (commonly used or critical
alternatives; a branch ends where it re-enters the default sequence). Every
view in a sequence must be in the sample set. Record the action needed to move
from each step to the next so any evaluator can replicate the run.

#### Process P1 — Open an assignment and read a problem — implements F1

**User story:** As a student, I need to reach my class, open an assignment, and read a problem (text, math, figure) so that I can learn and work the material. *(rewritten 2026-09-10 from the seeded "access course content" — this product has no content modules; the problem is the content.)*

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Sign in (S7) | Enter e-mail + password, submit (reviewer) |
| 2 | Class Management (S1 or S2 — record the mode) | Locate "Chapter 5 Sample Assignment" in Class Assignments |
| 3 | Class Management — row action menu (S1) / Actions select + Go (S2) | Choose "Take Assignment" |
| 4 | Take Assignment (S3), problem navigator | Move to Problem 8 (multiple choice) |
| 5 | Take Assignment (S3), problem statement | Read statement, math (M₁, M₂) and the figure; reach Part (a) |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | 2 | Switch to Accessibility Mode with the "Accessibility Page" button, then continue | 3 |
| P1-b | 4 | Use the jump points / shortcuts menu (Enter on a focus box, Ctrl+Shift+5 instructions) instead of tabbing | 5 |
| P1-c | 5 | Open a multi-part problem (P1 or P6) and move between Parts (a)–(d) | 5 |

#### Process P2 — Answer and submit a problem — implements F2, F8

**User story:** As a student, I need to enter an answer with the part's widget, submit it, and perceive the result (correct/incorrect, deductions, submissions remaining), using hints or feedback when stuck. *(rewritten 2026-09-10; no file upload exists.)* **Submitting consumes attempts on the shared demo account — the reviewer submits, and the run records which problem/part was used.**

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Take Assignment (S3), Problem 9 (multiple choice) | Select an option (radio) |
| 2 | Take Assignment (S3) | Submit |
| 3 | Take Assignment (S3), grade summary / submission history | Perceive result, deductions, submissions remaining |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P2-a | 1 | Numeric part (Problem 5): type a value / use the on-screen keypad, choose units | 2 |
| P2-b | 1 | Symbolic part (Problem 2 a): build an expression with the symbol palette | 2 |
| P2-c | 1 | Drag-and-drop ranking (Problem 3): order the four trials — keyboard alternative via the accessibility statement's method | 2 |
| P2-d | 1 | Free-body diagram (Problem 1 a): Add Force, set angle/length in the force table | 2 |
| P2-e | 1 | Hint / Feedback buttons: read the hint, note the deduction | 1 |
| P2-f | 2 | "I give up!" path (confirmation? deduction?) | 3 |
| P2-g | 3 | "detailed view" of submission history; Ctrl+Shift+2 read-back of the answer | 3 |

#### Process P3 — Complete an assignment under time limits and accommodations — implements F3

**User story:** As a student, I need to work within the assignment's begin/due/end dates, late-work rules, submission limits and session timeout — with an extended-time accommodation applied when granted — so that I am not timed out or penalised for my disability. *(rewritten 2026-09-10; there is no quiz timer in the sample — the timing surfaces are due/end dates, late-work %, and the session timeout.)*

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Class Management (S1) | Read Start / Due / End for the assignment |
| 2 | Take Assignment (S3) header | Read Begin/Due/End dates, late-work % and late potential |
| 3 | Take Assignment (S3) | Stay idle until the session-timeout warning appears (find the interval) |
| 4 | Session warning | Extend the session; verify the work is intact |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P3-a | 1 | Instructor: grant an extension / extended time (Assignment Editor → Extensions, or roster — A4) for the test student (reviewer-run; record the artifact) | 2 |
| P3-b | 2 | Past-due assignment: confirm late-work rules are perceivable before submitting | 2 |
| P3-c | 3 | Calendar (S6): find the assignment's dates from the calendar instead | 2 |

#### Process P4 — Author an assignment from the library — implements F7 (instructor)

**User story:** As an instructor, I need to create an assignment, filter the library to accessible problems (or deliberately include the three admitted inaccessible types for the review), add problems, and save. *(added 2026-09-10; reviewer-run because it creates an artifact — register it in §2.6.)*

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Class Management (S1) | Class Menu → Create Class Assignment |
| 2 | Assignment Editor (S5) | Name the assignment; set weight |
| 3 | Assignment Editor (S5), Library | Choose Book / Chapter; tick "Accessibility(AA) Only"; observe the list change |
| 4 | Assignment Editor (S5) | Add problems to the assignment; Save & Exit |
| 5 | Class Management (S1) | New assignment row visible |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P4-a | 3 | Untick the filter; add a drag-and-drop labeling, a hotspot, and a vector-practice problem (the review's inaccessible-types assignment) | 4 |
| P4-b | 4 | Preview a problem from the editor | 4 |

#### Process P5 — Check grades and feedback — implements F4, F6

**User story:** As a student I need to read my grade report for an assignment; as an instructor I need to read the class grade sheet and grade a part manually. *(added 2026-09-10.)*

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Class Management (S1) | Assignment row → View Grade Report |
| 2 | View Grade Report (S4) | Read per-problem/part scores and deductions |
| 3 | Class Management (S1) | Class Menu → View/Manage Class Grades |
| 4 | Class Assignments Grade Sheet (S9) | Read the table; open export controls |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P5-a | 4 | Assignment row → Manage Grades (Grade Manually): change a score (reviewer-run) | 4 |
