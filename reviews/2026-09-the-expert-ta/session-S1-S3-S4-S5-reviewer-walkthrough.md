# Reviewer Session Walkthrough — Tasks T1–T5 across S1, S2, S3, S4, S5 (2026-09-10)

A **functional evaluation**: you perform the tasks a student and an instructor
are expected to perform, with each assistive-technology instrument in turn,
and narrate what happens. Every axe finding from R001–R014 is met *inside* a
task step, never as an abstract check — so each barrier is recorded as
"task T# fails/stumbles at step N because…", which is what the report needs.

Work top to bottom; narrate freely at each step. The assistant records your
words in the **Feedback** line, converts them into observations and check
outcomes in the named run, promotes confirmed items to findings in `04`, and
updates `05` and `03` as you go. "The radio buttons just say *radio button
not checked*" is enough — no formal phrasing needed.

Steps are `W#`. Say the step number when you start one. Skip or reorder
freely — just say so. **KEY STEP** marks a step that confirms or refutes a
pending finding or a vendor claim.

**Where things are:** app `https://dei56mo.theexpertta.com/`; class "Testing
Course for CSU East Bay" (eid=3373); assignment "Chapter 5 Sample Assignment"
(aid=17547, 9 problems, past due 2026-09-08 — late-work rules apply to any
submission, which is itself a test step, W-T3.2). Shared demo instructor
account; work only in the **debug-profile Chrome window** — the app rejects a
second session ("Multiple Session Instances"), which is what stalled the axe
batch earlier today.

**Screen reader keystrokes** are given for NVDA first (what you used last
review) with the JAWS equivalent in brackets. Speech transcript: NVDA
**Speech Viewer** (NVDA+N → Tools) [JAWS: Insert+Space then H]. Never press
Insert+Space in NVDA — it toggles browse/focus mode.

---

## Setup

### W1 — Versions and instrument (feeds 03 §1.3, §1.5)

**Do:** Note the screen reader you will use and its version (NVDA: NVDA+N →
Help → About; JAWS: Help → About), Chrome (`chrome://version`, the
debug-profile window — it is 153.0.8010.36 as of this morning), Windows
build.
**Tell me:** Which screen reader (this decides whether runs log as B1 JAWS or
B5 NVDA), and the version strings.
**Feedback:** 2026-09-10 — Instrument: **NVDA 2026.2** (running; reviewer confirmed) → runs log as `--tool nvda --baseline B5`. JAWS 2026 installed, not used. Chrome 153.0.8010.36 (debug profile), Windows 11 Home 10.0.26200 (build 26200.9168). Recorded in 03 §1.3 (B5 confirmed, B1 annotated) and §1.5.

### W2 — Environment hygiene

**Do:** Close every other Expert TA tab or window (including your everyday
Chrome). Confirm the debug window shows "Class Management" at
`/common/default.aspx`, standard mode (button reads "Accessibility Page",
not "Non-Accessibility Page"). Start the screen reader.
**Tell me:** "Ready" — or what the page shows instead.
**Feedback:** 2026-09-10 — Verified by the assistant over CDP: one page tab in the debug window, `/common/default.aspx` "Class Management", standard mode (button reads "Accessibility Page"), assignment row present, NVDA 2026.2 running. Incident during this step: the assistant's probe attached to a blank second tab and opened the app there → immediate "Multiple Session Instances" invalidation; duplicate tab closed, original reloaded, session intact. Probe scripts fixed so it cannot recur (03 §2.6). Reviewer to confirm no everyday-browser window is on the site.

### W3 — Baseline check of the account state

**Do:** In Class Assignments, note the row: weight, dates, and open the row's
action menu (click ⋮) to see "Take Assignment" → the assignment should show
**5 Submissions Remaining** on Problem 9 and no attempts on any problem.
**Tell me:** Whether anything has been submitted already (someone else shares
this account).
**Feedback:** 2026-09-10 — Read by the assistant over CDP (same tab; no submission made; returned to Class Management). Row: weight 1, publish Aug 01, start Sep 01, due/end Sep 08 2026 11:59 PM, grade prefs "Instructor Default". Per problem — submissions remaining / hints remaining: P1 3/0 (4 parts), P2 3/1 (3 parts), P3 3/2, P4 3/5 (2 parts), P5 3/3, P6 3/1 (5 parts), P7 3/1 (4 parts), P8 5/3, P9 4/2. Deductions 0 % and Potential 100 % on every problem, so no graded attempt is recorded; the differing "remaining" counts look like per-problem settings rather than used attempts, except P9 (4 vs P8's 5) which may have had one prior submission by another account holder. State is unchanged from this morning's exploration (P2 showed 3 remaining / 1 hint then too). Reviewer: say if you know of any submission made on this account before today.

---

## Part A — Task T1: open an assignment and read a problem (screen reader, no-vision)

Runs (the assistant logs each the moment the step starts; commands shown so
either of us can run them — replace `--tool jaws --baseline B1` with
`--tool nvda --baseline B5` per W1):

```
python scripts/review.py log-test the-expert-ta --view S1 --modality no-vision --tool jaws --baseline B1 --task T1 --url https://dei56mo.theexpertta.com/common/default.aspx
python scripts/review.py log-test the-expert-ta --view S3 --modality no-vision --tool jaws --baseline B1 --task T1 --url "UI: Class Management → assignment row → Take Assignment"
```

Screen ignored; browse mode / virtual cursor.

### W4 — Land on Class Management (NV1, NV9)

**Do:** Reload `/common/default.aspx` with the screen reader running. Listen
to the load announcement. Then press `NVDA+T` [JAWS: Insert+T] for the title.
**Tell me:** The title as spoken; whether the page language sounds right
(this page declares `lang="en"`; Take Assignment does **not** — W10).
**Feedback:** 2026-09-10 — Reviewer was on **Accessibility Mode** (`default2.aspx`), i.e. S2: "Class Management Accessibility Mode" announced on load and on NVDA+T → R016 O1, NV1 pass. Standard-mode S1 (R015) still owed — repeat W4–W9 there after switching with "Non-Accessibility Page".

### W5 — Headings and landmarks (NV2) — KEY STEP

**Do:** Press `H` repeatedly, then `D` [JAWS: `R`] for landmarks, then open
the elements list `NVDA+F7` [JAWS: Insert+F6 headings, Insert+Ctrl+R
regions].
**Tell me:** What is listed — or that the keys report "no headings" / "no
landmarks". Then say how you *would* find the assignments table without
them.
**Why it matters:** axe (R001 O5/O6) and the accessibility-tree probe both
say the page has zero headings and zero landmarks; the visible "Classes",
"Class Menu", "Class Assignments", "Class News" captions are bold text. This
step turns that into a confirmed 1.3.1/2.4.6 finding — or refutes it if the
screen reader finds structure the tools missed (then the sweep's W3 is
"instrument-blind").
**Feedback:** 2026-09-10 (on S2) — No next/previous heading with H; no landmark with D; NVDA+F7 gives no route to the tables. Content reached by `T` or Tab. `T` announces "Data table related to the headers above, table clickable with x rows and x columns" for both grids — cannot tell Class Assignments from Class News; tabbing in announces the focusable title divs. Section titles are `div tabindex=0` + coloured `<b>` (reviewer pasted `#assignmentsTitle`). → R016 O2, O3, O5; V-F1, V-F2; T1-F1. axe R005 W3 confirmed (not instrument-blind). **Open:** are column headers announced when moving across cells?

### W6 — Read the page top to bottom (NV5, NV8)

**Do:** From the top, arrow down through the whole page in browse mode.
**Tell me:** Whether the order makes sense (header → menu → Classes →
Class Menu → assignments → news), and anything announced that a sighted
user does not see, or vice versa. Note especially what is announced for the
**first focusable item** — the site logo link is marked `aria-hidden` but
is still in the tab order (R001 O3): press Tab once from the top and tell me
what, if anything, is spoken.
**Feedback:** 2026-09-14 (on S1, standard mode, during W34) — arrowing down
follows the expected order; nothing extra or missing reported apart from the
grids' meaningless captions/columns (V-F2). The first Tab stop is the hidden
accessibility-instruction div (read in full), not the logo link — the
`aria-hidden` logo was not reported as a stop → R015 O7, O9.

### W7 — The Classes and Class Menu combo boxes (NV3, NV6) — KEY STEP

**Do:** Tab to the first combo box (visually "Classes"), then the second
("Class Menu"). In each: listen to what is announced on focus; press
`Alt+Down` to open it and arrow through the options; press `Esc`.
**Tell me:** Exact announcement on focus for each — role, name (if any),
current value. Could you tell which combo is which without the screen?
**Why it matters:** axe `label` critical (R001 O1): both DevExpress
editors have no label; the tree shows two unnamed textboxes. Same defect
family recurs on every instructor page (R006 59 fields, R009, R010, R011,
R012) — this is the product-wide finding's confirmation.
**Feedback:** 2026-09-10 (done on S2, native selects): both announce "First make your selection here and then click Go button to confirm your choice. combo box <value> collapsed"; the visible captions "Classes:" / "Class Menu:" are not announced → R016 O11, V-F7 (Major; 1.3.1, 2.5.3, 4.1.2). Standard-mode DevExpress combos (S1) still to be heard under R015.

### W8 — Jump-point button and the "accessibility shortcuts menu" (NV3, NV7) — KEY STEP

**Do:** Tab from the top of the page until you land on something that reads
its instruction text ("Use the tab key to progress through actionable
items…" — the vendor's *focus box* / jump point, `#top_of_page_jump_point`).
Press `Enter` on it.
**Tell me:** (1) What was announced when it received focus — a role? a
name? just text? (2) What Enter did — did a menu open, what was in it, could
you arrow through it, and did Esc close it?
**Why it matters:** the vendor's headline claim is context-specific menus
while tabbing (email 2026-08-17). axe reports the element as a `button`
with no accessible name (R001 O2; 4 of them on Take Assignment, 32 on the
grade report, 33 on the solutions page). This step decides whether they are a
help or an unlabelled obstacle.
**Feedback:** 2026-09-10 (on S2): Enter on the jump point switches its text to "No Shortcuts" and navigates nowhere; no menu opened → R016 O12, V-F8 (Minor here; re-rate at W11 on the assignment page).

### W9 — Reach and open the assignment's action menu (NV3, MO1/MO2 preview) — KEY STEP

**Do:** Navigate to the Class Assignments table (`T` for next table). Read
the row ("Chapter 5 Sample Assignment"). Try to open its action menu
**without the mouse**: Tab to whatever is focusable in the row, try Enter,
Space, and the Applications/context-menu key on the row and on the ⋮ cell.
**Tell me:** What is focusable in the row and what each key did. If nothing
opens the menu, say so plainly — then open it with the mouse, and read the
menu items with the arrow keys.
**Why it matters:** the tree shows the row as plain table cells with a click
handler (R001 O7). If the menu cannot be opened from the keyboard, T1 fails
at step 3 for keyboard and screen-reader users in standard mode — and the
"Accessibility Page" (W-T1a) becomes the only route.
**Feedback:** 2026-09-10 (on S2 only): reached via the row's Actions select → "Take Assignment" → Go; NVDA announced the page change → R016 O13, NV7 pass. Grid keyboard note: with NVDA **off** the grid's arrow-key scheme works from the Go button; with NVDA on it does not (R016 O9 — mode question left open). The standard-mode row action menu (S1) is still untested — R015.

### W10 — Take Assignment: title, language, navigator (NV1, NV9, NV3)

**Do:** Choose "Take Assignment". On load: title (`NVDA+T`), then `K` [JAWS:
Tab or `U`] through the problem links on the left.
**Tell me:** The title; whether the voice/pronunciation changed (this page
has **no `lang` attribute**, R004 O2 — with a non-English default synthesizer
voice this matters; with an English one you may hear nothing); what each
problem link announces (expected: "Problem 1 Click To Activate, link" —
say whether "Click To Activate" helps or clutters).
**Feedback:** 2026-09-10 — page change announced as "Take Homework Assignment" on arrival (R016 O13). `K` walks all nine problem links; Enter activates a problem but focus is not placed in the problem region and, with no headings, it is unclear how to get there → R017 O1, **T1-F2** (2.4.3, 1.3.1, Major). Language/pronunciation: nothing reported.

### W11 — Jump points on the assignment and the Ctrl+Shift chords (NV3, NV7) — KEY STEP

**Do:** Tab through the jump points (top of page → problems → problem
statement → Part a). On the "Part" one press `Enter` and explore the menu.
Then, with focus inside Problem 9's answer area, press `Ctrl+Shift+5`
(instructions), `Ctrl+Shift+4` (details), `Ctrl+Shift+2` (read my answer).
**Tell me:** Whether each chord produced speech (the text goes into a polite
live region, `#calc-announce`), the wording, and whether the screen reader
swallowed any chord. Also whether `Ctrl+Shift+1` moved you to the previous
part on a multi-part problem (try on Problem 1 later, W15).
**Why it matters:** these are the vendor's designed screen-reader path
(ETACore/ETAAccessibilityFunctions). If they work, several barriers below
have a documented workaround; if the chords are eaten by the screen reader or
the live region is silent, the path does not exist for the user. Feeds 4.1.3.
**Feedback (part 1):** 2026-09-10 — Tabbing reaches a visually hidden div: "Press tab to go to problems. Press enter to open the accessibility shortcuts menu.  button". Enter mounts new links (the shortcuts menu) that move around the page; a keyboard user can Tab to them, NVDA needed browse mode. Reviewer: "very confusing for a screen reader user" — discoverable only by tabbing into a hidden area → R017 O2, V-F8 re-rated Major. **Part 2:** Ctrl+Shift+5 moves NVDA to the alert region: "Multiple Choice. Press Ctrl+Shift+2 keys to read out your answer. Supplemental answer not available. Ctrl+Shift+4 keys for details. Ctrl+Shift+5 keys for instructions." — works. **Ctrl+Shift+2 reads raw MathJax HTML markup** (≈4,400 characters of span/style/attribute source around the answer "T₂ is less than T₁") → R017 O4, **V-F9** (4.1.3, 1.3.1; Blocker for the read-back). Evidence `runs/R017/R017-ctrlshift2-speech.txt`. Ctrl+Shift+4 (details): works, clean text. Ctrl+Shift+2 on a plain-text option: reads correctly; on a math option ("½ g"): raw markup again → V-F9 is math-specific.

### W12 — Read Problem 8 (multiple choice): statement, math, figure (NV4, NV5) — KEY STEP

**Do:** Activate Problem 8. Read the statement with the arrow keys. Listen
to how *M₁* and *M₂* are spoken. Then find the figure (`G` for next
graphic).
**Tell me:** (1) How the math is read (MathJax is present; the vendor claims
"human-friendly" read-out like "cosine of forty five point two" and a toggle
to the literal form — did you get either, and where is the toggle?);
(2) what the figure announces — the two-blocks-and-pulley diagram on
Problems 6–9 has an **empty alt** in the DOM (exploration) while Problems 1,
4, 5 have descriptive alt; does anything (the Ctrl+Shift+4 "details")
describe it?
**Why it matters:** 1.1.1 on the figures; and the solutions page shows the
alt-text markup is broken by a missing quote (R014 O1) — this tells us
whether the same authoring bug hits the student-facing view.
**Feedback:** 2026-09-10 — M₁/M₂ announce as "table" in **focus mode**; in **browse mode** the math is read when the cursor enters the MathJax item → V-F10 withdrawn as a failure (advisory: user must know to switch modes). Figure: `G` finds no graphic, image cannot be right-clicked — empty alt → R017 O8, **V-F12** (1.1.1, Major). Ctrl+Shift+2 reads raw markup in both modes (V-F9 stands). **Still open:** the human-friendly read-out toggle (not seen).

### W13 — The answer radio buttons on Problems 8 and 9 (NV3, NV6) — KEY STEP (likely Blocker)

**Do:** On Problem 8, Tab (or `F` for next form field) to the first answer
option and arrow through all six; repeat on Problem 9 (five options).
**Tell me:** The exact announcement for each option: does it speak the
option text ("g", "The value cannot be determined", …) or only "radio
button, not checked, 1 of 6"? Can you tell which option you are on **without
the screen**?
**Why it matters:** axe `label` critical on all 5/6 radios (R004 O1); the
accessibility tree shows them nameless. If confirmed, a blind student cannot
answer any multiple-choice part → T2 **Fail** for no-vision, severity
Blocker. The vendor's own read-back (`Ctrl+Shift+2`, W11) may mitigate after
selection but cannot substitute for knowing what you are selecting.
**Feedback:** 2026-09-10 — Arrowing between the radios in browse mode: plain-text options read correctly (NVDA reads the adjacent cell); the math option "½ g" announces only "row 4 table 1" → R017 O6, **V-F11** (1.3.1, 4.1.2; Major, Blocker for math options). Focus mode (Shift+Tab from Submit): enters as "table"; arrowing auto-selects and announces "Radio Button Checked X of X" plus the column-two answer text; MathJax inside options does not reliably play, must leave focus mode to hear it; mixed text+math auto-read breaks → R017 O9, V-F11 updated.

### W-T1a — Branch P1-a: the same task in Accessibility Mode (S2) — KEY STEP

Run:
```
python scripts/review.py log-test the-expert-ta --view S2 --modality no-vision --tool jaws --baseline B1 --task T1 --url https://dei56mo.theexpertta.com/common/default2.aspx
```
**Do:** Back on Class Management, activate the "Accessibility Page" button.
Repeat W5–W9 quickly on this version: headings/landmarks; the first Tab
stop ("Tab for Assignments, Enter to skip" — press Enter, where does focus
go?); the two `<select>`s and their "Go" buttons; then the **Actions select
in the assignment row** → choose "Take Assignment" → Go.
**Tell me:** Whether the skip links work (feeds 2.4.1 for this mode);
whether the two top selects announce their instruction as a name (they
should: "First make your selection here and then click Go button…"); and
what the **row's Actions select** announces — axe says it has **no name**
(R005 O1), the one control that leads to the assignment.
**Feedback:** 2026-09-10 — Reviewer started here (switched the mode on deliberately). Skip links: first impression "does nothing"; clarified: Enter moves focus to the next section's skip link — they work, but are links by role with instruction-like wording → R016 O4, V-F3 (Minor); 2.4.1 met on this page. Class Menu popups (Create, Edit, Create News…): Close/Cancel button exposed and works, Esc does nothing → not a trap; V-F4 withdrawn, advisory only. Popup forms: inputs unlabelled, labels in an adjacent table column → R016 O7, V-F5. Row Actions select: Speech Viewer "Create Assignment  Go  Assignment Menu - Click To Activate  row 3  Actions  column 1  combo box  Create Assignment  collapsed" — no name of its own, cell text read in browse mode → V-F6 (Minor); column header announced. **Open (O9):** from the row's Go button, NVDA table navigation does not move to column 2+; Shift+Tab back in lands in the last column and arrows work. Assistant asks: retry from Go after `NVDA+Space` (browse mode). **Done:** top selects (V-F7), jump point (V-F8), Actions → Take Assignment → Go (page change announced). **Skipped:** W6 read-through / first Tab stop (logo link) — ask at session end. Reviewer note: with NVDA off, the grid's arrow keys work from Go.
**Why it matters:** this is the vendor's conforming alternate version. The
review has to say (a) whether a student can complete T1 here when standard
mode fails, and (b) that the accessible version still has no headings or
landmarks (R005 O4). **Afterwards, switch back with "Non-Accessibility
Page"** — the mode is stored on the shared account.
**Feedback:** see the dated feedback above (S2 pass recorded under R016).
Mode was still Accessibility Mode when the reviewer moved on to Take
Assignment; switch back before the S1 (standard-mode) pass under R015.

---

## Part B — Task T2: answer and submit (screen reader continues; then keyboard-only)

Screen-reader run continues in the S3 no-vision run from Part A. Keyboard
run:
```
python scripts/review.py log-test the-expert-ta --view S3 --modality motor --tool keyboard --baseline B2 --task T2 --url "UI: Class Management → assignment row → Take Assignment"
```
**Submitting consumes attempts on the shared account** (5 per part). Use the
parts named below so we know which attempts were spent, and stop after one
submission per part unless a step says otherwise.

### W14 — Submit a multiple-choice answer (Problem 9) (NV7, NV6)

**Do:** With the screen reader, select any option on Problem 9 and activate
**Submit**. Listen.
**Tell me:** What was announced after submitting — correct/incorrect,
deduction, "4 Submissions Remaining"? Did focus move? Did you have to hunt
for the result? Then press `Ctrl+Shift+2`: does it read back your answer?
**Why it matters:** 4.1.3 status messages and 3.3.1 error identification —
the grade summary sits below the buttons; the live region is the vendor's
answer to this.
**Feedback:** 2026-09-10 — Submit opens a mini dialog that voices correct/failure with further options; works as expected. Focus moves to a div close control announced "click to activate" → R017 O10, NV7 pass for submission feedback. One P9 attempt used.

### W15 — Multi-part problem, symbolic entry (Problem 2, Part a) (NV6, MO1, MO5) — KEY STEP

**Do:** Screen reader on, keyboard only. Activate Problem 2, reach Part (a)
"F_NET =" and type an expression (`m*a`). Notice the on-screen symbol
palette (β, θ, a, d, … 7 8 9, HOME, ←) below the field.
**Tell me:** (1) What the input field announces on focus (label? the
"F_NET =" prefix?); (2) how many Tab presses from the field to the Submit
button — i.e. **are the ~45 palette buttons in the tab order**, and what do
they announce; (3) whether `Ctrl+Shift+1` moved you between Parts (a)–(c);
(4) submit once and report the result announcement.
**Why it matters:** 2.4.3 focus order and 2.1.1 — a keyboard user tabbing
through 45 buttons per part is a Major burden; the palette buttons carry
titles, so they may be named but still in the way. Also the math read-out of
"F sub NET".
**Feedback:** 2026-09-10 — (2) Tab from the field lands directly on Submit: palette not in the tab order → R017 O12 (open: keyboard symbol entry, W20). (3) Ctrl+Shift+1 moves to the first hidden accessibility guide, not the previous part → O13, folded into V-F8. (4) Submit: "Submission Details  dialog  Correct Answer Continue to the next question Click To Activate Close and stay on this question - Click To Activate"; focus on "Continue to the next question, visited link" → O14, pass. Also captured the P9 repeat-answer dialog: "Submission Details  dialog  Incorrect Answer You have previously used this answer. Please refer to your submission history. Close and stay on this question - Click To Activate." — dialog role and close-control name are fine (O11). (1) Nothing identifies the field as F_NET — the MathJax prefix is not associated → R017 O15, **V-F13** (1.3.1, 3.3.2, 4.1.2; Major). Exact focus announcement still to capture. Reviewer (2026-09-10): the F_NET row is the calculator — a separate component (→ W15b); Ctrl+Shift+2 reads the field's content but there is no natural way to navigate to it (R017 O16).

### W15b — The calculator widget (Problem 2 Part (a): answer field + palette) (NV3, NV6, MO1, MO2) — added 2026-09-10

**Do:** From the top of Problem 2, try to reach the F_NET answer field by the
natural routes only: Tab from the part's jump point; `E`/`F` (next edit /
form field) in browse mode; then the palette buttons (β, θ, … 7 8 9, √, ←).
Insert one symbol from the palette (e.g. θ) and one typed character; press
`Ctrl+Shift+3` (answer with cursor position).
**Tell me:** (1) Which route, if any, lands on the field and what it
announces on focus; (2) whether the palette buttons are reachable by
keyboard at all and what they announce; (3) whether a palette insertion is
announced and appears in the read-back; (4) whether the read-back is clean
text or markup (V-F9 pattern).
**Why it matters:** this is the input surface for every symbolic and
numeric part — the reviewer identified it as a separate component; V-F13
and the keyboard-symbol question (R017 O12) are decided here.
**Feedback:** 2026-09-10 (done on Problem 5's function keypad) — All calculator
buttons exposed, named and Tab-reachable, linear Tab only (no arrow keys
within the keypad). No direct way to reach the entry area except tabbing to
the nearest element and arrowing in; the area is a `div.problemanswer`
(reviewer-pasted markup) with a blinking-caret span — not a form control.
Ctrl+Shift+2 reads it: empty "Alert your answer in degrees", populated
left-to-right "not PEMDAS". Caret moves with on-screen ←/→/HOME/END, but no
feedback on where the caret sits in the formula → R017 O21, O22; **V-F13
expanded** (4.1.2, 1.3.1, 3.3.2, 2.4.3; Major). Ctrl+Shift+3 does report
the caret position on request. W15b complete.

### W16 — Numeric entry with units (Problem 5) (NV6, MO2)

**Do:** Activate Problem 5. Reach the numeric field, type a value, then find
and choose a **unit radio button** next to it, then Submit.
**Tell me:** Announcements for the field, the function keypad (sin(), cos()
…) if you tab through it, and the unit radios (are *these* radios named,
unlike Problems 8/9?). Result announcement after Submit.
**Feedback:** 2026-09-10 — Unit radios function as expected (named). Keypad
and entry area: see W15b. Submit result on this problem not narrated
(dialog behaviour already established at W14/W15).

### W17 — Drag-and-drop ranking (Problem 3) with the keyboard (MO7, NV3) — KEY STEP (vendor claim)

**Do:** Activate Problem 3. Find the "Show/Hide Accessibility Statement"
icon (image button) and open it — it explains the keyboard method. Follow
it: move the four trial cards into the ranked area in some order, keyboard
only, screen reader on. Press `Ctrl+Shift+3` (unmatched items) and
`Ctrl+Shift+2` (your answer) along the way. Submit once.
**Tell me:** (1) Was the form toggle (the accessibility icon at the top
right of the part) reachable, and was it clear what it opens? (2) In the
form (found 2026-09-10: a Bucket / Order / Item table with custom combo boxes,
"Add Item", "Reset", and a ✖ per row — R017 O18, screenshot in R017): what
each combo box announces on focus, on opening, while arrowing through the
options, and after choosing; whether "Add Item" moves focus as its label
promises; whether the ✖ delete has a name. (3) What the visual cards
announce outside the form — they are images with empty alt, so does anything
there give you "½m, 2F"? (4) Whether a placement or the ranked result is
announced (live region), and what Submit reported.
**Why it matters:** the vendor states sorting/ranking drag-and-drop is fully
compliant (email 2026-08-17) while labeling drag-and-drop is not. This is
the claim test. 2.1.1 / 2.5.7 / 1.1.1 / 4.1.2.
**Feedback:** 2026-09-10 — (1) Toggle is an exposed button, Tab-reachable,
announced "Show drag and drop accessibility table button"; activating it
moves focus into the form. (2) To hear the answer you must use Ctrl+Shift+2;
the read-back reads only the Item column and runs rows together "like a long
paragraph" with no announcement of a new item — "not unusable". (4) Placement
/ ranking not announced in any designed way; derivable by navigating the
table → R017 O19, **V-F14** (4.1.3, Minor). Vendor's ranking claim largely
holds on the mechanism. Combo boxes and ✖ delete properly announced; the
visual cards announce nothing outside the form (empty alt; the form is the
accessible alternative); Submit → same "Submission Details" dialog, announces
correct/incorrect. W17 complete.

### W18 — Free-body diagram (Problem 1, Part a) with the keyboard (MO1, MO2, NV3) — KEY STEP (vendor claim)

**Do:** Activate Problem 1. In the interactive area: reach **Add Force**
with the keyboard, add a force, then set its angle and length through the
force table (Force Name / Angle / Adjust Angle / Adjust Length / Delete).
Press `Ctrl+Shift+3` (force totals). Submit once (any answer).
**Tell me:** Whether every part of that was possible without a mouse; what
the table headers and controls announce (axe could not tell whether the
`th`s are empty — R004 O11); whether the diagram state was ever described.
**Why it matters:** the vendor says the FBD question "was difficult to
implement" but is accessible. A drawing task that passes both keyboard and
screen reader would be unusual; document exactly how far it goes.
**Feedback:** 2026-09-10 — All of it succeeded without a mouse (Add Force,
angle/length via the force table, Ctrl+Shift+3 totals, Submit); "the
readback feature is quite robust" → R017 O20, pass; vendor claim confirmed
for this problem. axe's empty-table-header incomplete (R004 O11) dismissed.

### W19 — Hints, Feedback, "I give up!" (NV7, CO3, CO4)

**Do:** On any problem with attempts left: activate **Hint**, then
**Feedback** (it may be disabled until after a wrong answer), then, on a
part you don't mind losing, **I give up!**.
**Tell me:** What each announced, whether the deduction percentages ("4%
deduction per hint") were spoken, and whether "I give up!" asked for
confirmation before forfeiting the part.
**Feedback:** 2026-09-10 — Hint: the hint appears below the problem area but
is not announced (Speech Viewer: "table with 3 rows and 1 column Submissions
Info." — `R017-hint-speech.txt`) and there is no clear way to navigate into
it → R017 O23, **V-F15** (4.1.3, 2.4.3; Major). Deductions are spoken. "I give
up!" opens a modal with a warning and Continue / Cancel links → O24, pass.

### W20 — Keyboard-only pass over the whole assignment page (MO1–MO5, MO9, MO11)

**Do:** Screen reader **off**, mouse away. Reload the assignment. Tab from
the top and count stops until the first answer field. Then: is the focus
indicator visible on every stop (jump points, problem links, keypad
buttons, Submit)? Can you get *out* of the keypad/palette area with
Tab/Shift+Tab? Are the small ⊞/⋮/keypad targets at least 24 px?
**Tell me:** The stop count; any stop with no visible focus ring; any place
focus got stuck or jumped somewhere unexpected; whether the first Tab stop is
a usable skip (the jump point) — this settles 2.4.1 for the standard pages.
**Feedback:** 2026-09-10 (NVDA off) — (1) ~20 Tab stops to the first answer
field. (2) No hidden stops: focus visible throughout. (3) No traps. (4) The
jump-point stops are not skips — each is an opportunity to press Enter and
open a hidden accessibility menu, and several of them do the same thing.
(5) θ / β / √ entered on Problem 2 without the mouse — success → R018
(MO1–MO5, MO7 pass; MO11 partial: mechanism exists but is not a skip link).
Reviewer's ruling on R017's Result: **Broken** — "if they can't complete the
entire problem set because a single problem is inaccessible then the whole
problem set is not accessible." T2 verdict → Fail.

---

## Part C — Task T5: check grades (screen reader)

Run:
```
python scripts/review.py log-test the-expert-ta --view S4 --modality no-vision --tool jaws --baseline B1 --task T5 --url https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547
```

### W21 — Open your grade report after the submissions above (NV2, NV3, NV5)

**Do:** Class Management → assignment row → "View Grade Report (shows your
detailed work)". Read the report for the problems you submitted in Part B.
**Tell me:** How you found your problem's score; what the **32 jump-point
buttons** (one per problem and part) sound like when tabbing — help or
noise; whether the per-part submission tables read as tables (headers
announced with cells) now that they contain rows; what the blue **[?]** links
announce; and whether "late" submissions are identified in words or only by
red text (also NC1, W29).
**Why it matters:** R007 — this is the page where the jump-point pattern is
at its densest, and where lateness is conveyed by colour.
**Feedback:** **Reopened 2026-09-21 — the assistant got this wrong.** It was
first closed as "not answerable, the account has no graded work", from your
"there are no grades to view in the test account". You have since clarified
that you meant the **gradebook**, not this page. Measuring the grade report
found it fully populated — 1120 text elements, the formula
`Student Grade = 100 - 100 - 9 = 0%`, 14 dated submissions, part-level late
notices — so every part of this step has something to read. The coverage
limitation has been withdrawn from `03` §1.1 and task **T5** is no longer
marked blocked.

**One of the five questions is already answered** (R100 O7): lateness is
stated **in words** at part level — "Late submissions were made on this
part…" — and by **red date-time alone** at individual-submission level, under
the page's own legend "Red submission date times indicate late work". So the
answer to "in words or only by red?" is *both, at different levels* → V-F31.

**Still open, and this is the last no-vision step on a populated page:** with
NVDA on — how you find your problem's score; what the **32 jump-point
buttons** sound like when tabbing (help or noise); whether the per-part
submission tables read as tables, headers announced with cells, now that they
contain rows; and what the blue **[?]** links announce. → W57 covers the same
page; do them together.

### W22 — Instructor side: class grade sheet (P5 step 4) (NV3, NV5)

Run:
```
python scripts/review.py log-test the-expert-ta --view S9 --modality no-vision --tool jaws --baseline B1 --task T5 --url https://dei56mo.theexpertta.com/Common/GradeSheetClassAssignments.aspx?m=1&eid=3373
```
**Do:** Class Menu → "View/Manage Class Grades". Read the pivot grid; try the
export control; try the student filter box.
**Tell me:** Whether the pivot grid reads as a table; whether the column
headers can be sorted from the keyboard; what the filter box and the Points
View check box announce (both unlabeled per R009); what the **Export**
control announces (on the spreadsheet view it is a `div` with an
`aria-label` but no role — R013 O3).
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

---

## Part D — Task T3: time limits and accommodations

Run (cognition is an inspection run — no baseline needed):
```
python scripts/review.py log-test the-expert-ta --view S3 --modality cognition --tool inspection --task T3 --url "UI: Class Management → assignment row → Take Assignment"
```

### W23 — Late-work rules are perceivable before submitting (CO3, NV5)

**Do:** On the assignment header, read Begin/Due/End dates and the grade
summary block ("Late Work % 50%", "Late Potential 50%").
**Tell me:** Whether a student would understand *before* submitting that the
assignment is past due and what the penalty is — is that stated in words
anywhere, or only implied by the dates and the "Late Potential" number?
**Feedback:** _(pending)_

### W24 — Session timeout and extension (CO7 / 2.2.1) — KEY STEP

**Do:** Leave the assignment page idle with an answer typed but not
submitted. Wait for a warning (the page loads `SessionExtend.js`). Note the
time to warning, what it says, how long you get to respond, and whether
extending keeps your typed answer. If nothing appears within 25 minutes, try
Submit and report what happens.
**Tell me:** Interval, wording, whether the dialog was announced by the
screen reader (leave it running), whether Esc/Enter worked, and the outcome.
**Why it matters:** 2.2.1 requires the user be warned and able to extend
with a simple action, at least 20 s before expiry — and the earlier session
bounce ("Multiple Session Instances") suggests expiry may be abrupt.
**Feedback:** _(pending)_

### W25 — Grant an extension / extended time (instructor; branch P3-a) (CO3, A4)

**Do:** Assignment Editor → **Extensions** button. Look for a per-student
extended-time or new-due-date control (roster is empty, so it may show no
one — say so). Also check the roster page (`Class Menu → View/Manage Class
Roster`) for an accommodation column.
**Tell me:** Where the accommodation lives, what it is called, and whether it
is per student. This fills §2.5 A4 in the scope file. Do **not** save a
change on the shared account unless you note it here.
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

---

## Part E — Task T4: author an assignment (instructor; keyboard + screen reader)

Runs:
```
python scripts/review.py log-test the-expert-ta --view S5 --modality no-vision --tool jaws --baseline B1 --task T4 --url "https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=1&eid=3373"
python scripts/review.py log-test the-expert-ta --view S5 --modality motor --tool keyboard --baseline B2 --task T4 --url "https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=1&eid=3373"
```
This part **creates artifacts** (assignments in the shared demo class). Name
them so they are obviously ours: `CSU-A11Y-review-accessible` and
`CSU-A11Y-review-inaccessible-types`. The assistant registers both in 03
§2.6 the moment they exist.

### W26 — Create an assignment with the "Accessibility(AA) Only" filter (NV6, MO1, MO2) — KEY STEP (TAAP dependency)

**Do:** Class Menu → "Create Class Assignment". Keyboard only, screen reader
on: enter a name and weight; in **Library** choose a book and chapter; find
and tick **"Accessibility(AA) Only"** (Sections row); observe the problem
list change; add three problems; **Save & Exit**.
**Tell me:** What the Name, Description, Weight, Grade/Integrity Preferences
fields announce (all unlabeled per R006 — 59 fields); whether you could find
the Accessibility(AA) check box by its name from the keyboard; how the
problem list changed when ticked (did the count drop? were drag-and-drop
labeling / hotspot / vector problems removed?); whether "add to assignment"
was operable without the mouse; and whether Save worked.
**Why it matters:** the campus TAAP tells faculty to avoid the inaccessible
formats. That instruction is only enforceable if an instructor can find and
use this filter — and the filter itself is one of the unlabeled controls.
**Feedback:** _(pending)_

### W27 — Branch P4-a: build the inaccessible-types assignment

**Do:** Repeat with the filter **off**: add one **drag-and-drop labeling**,
one **hotspot / click-on-image** (the vendor says 0 exist in physics —
confirm by searching), and one **vector practice** problem (17 exist).
Mouse allowed for speed. Save & Exit.
**Tell me:** The problem IDs you added (e.g. "5.3.x"), and whether the
library shows any marking that tells an instructor a problem is
inaccessible *before* they add it.
**Feedback:** _(pending)_

### W28 — Student pass on the three admitted types (screen reader, then keyboard) — KEY STEP (vendor admission, TAAP scope)

Run:
```
python scripts/review.py log-test the-expert-ta --view S3 --modality no-vision --tool jaws --baseline B1 --task T2 --url "UI: Class Management → CSU-A11Y-review-inaccessible-types → Take Assignment"
```
**Do:** Take the new assignment. For each of the three problems try to
answer, first with the screen reader, then keyboard only.
**Tell me:** For each type: what is exposed (anything to read? any control
to operate?), whether any answer at all can be entered without a mouse, and
whether the labeling drag-and-drop uses **images of text** that do not scale
(the campus's original concern, 1.4.5). Say clearly which of the three is a
complete stop and which is merely hard.
**Why it matters:** these are the barriers the TAAP is written around; the
report needs each one's severity from observation, not from the vendor's
email.
**Feedback:** _(pending)_

---

## Part F — Low-vision confirmations (zoom + eyedropper)

Runs:
```
python scripts/review.py log-test the-expert-ta --view S1 --modality low-vision --tool zoom --baseline B3 --task T1 --url https://dei56mo.theexpertta.com/common/default.aspx
python scripts/review.py log-test the-expert-ta --view S3 --modality low-vision --tool zoom --baseline B3 --task T2 --url "UI: Class Management → assignment row → Take Assignment"
```
Window 1280 px wide, `Ctrl+plus` to 400 %. Use the eyedropper
(Windows PowerToys Color Picker or DevTools) on the rendered pixel, not the
CSS value — axe's numbers below already resolved an opaque background, so
they should match; DevExpress buttons it could not measure at all.

### W29 — Reflow at 400 % on Class Management and Take Assignment (LV1, LV2, LV7) — KEY STEP

**Do:** At 400 %: does Class Management reflow to one column or need
horizontal scrolling? Same on Take Assignment (header dates, the problem
navigator, the keypad, the FBD area). Tab a few stops and look for the
focus ring.
**Tell me:** Where two-dimensional scrolling is required, anything clipped
or overlapping (the anti-cheating watermark text over the problem?), and any
stop with the focus ring hidden.
**Why it matters:** both pages already scroll horizontally at 1280 px; axe
cannot test 1.4.10.
**Measured 2026-09-11 (view_probe, LV1):** at 320 CSS px every one of the 14 views scrolls horizontally — the page is a fixed 1300 px container (`div#container`; S1 scrollWidth 1343, S3 1300, S5 1373). Recorded as a measured fail on each view's low-vision run (R019, R024, R030, R036, R042, R048, R054, R060, R066, R072, R078, R083, R088, R094). **What remains for you:** confirm at real 400 % zoom that content or functionality is lost or overlaps (LV2) and that the focus indicator stays visible (LV7).
**Feedback:** **Superseded 2026-09-15 — do not run.** Session 3 walked zoom page by page (W42–W55) and answered LV2 and LV7 on every sampled view; the reflow fail became **V-F19** and the popup case **V-F25**. Nothing is left of this step. Kept for the record, closed as answered elsewhere.

### W30 — Contrast eyedropper (LV4, LV5)

**Do:** Measure these (axe values in brackets; confirm or correct):
Class Management "Classes"/"Class Menu" captions `#48848C` on white
[4.23:1]; "Class Assignments" `#EFBB75` [1.74:1]; "Class News" `#E58F65`
[2.48:1]; news body grey `#808080` [3.94:1]; the ⋮ row-menu glyph
[unmeasured]. Take Assignment: hint/feedback deduction "4%"/"5%" `#FF9900`
[2.14:1]; red randomized-variable values `#FF6347` [2.94:1] (Problem 1:
"25", "13"); problem-navigator numbers `#3A7C89` on `#F5F5F5` [4.35:1];
"Part (b)" identifiers [4.35:1]. Calendar event bar white on `#8EA9DB`
[2.37:1]. Assignment Editor toolbar button captions (Save Only, Extensions)
[unmeasured — bgImage]. Sign-in "User Name:" `#3A7C89` on `#EDEDED`
[4.05:1].
**Tell me:** Each measured ratio, or "matches". Note which of these are
information a student must act on (deduction %, variable values) versus
decoration.
**Feedback:** **Superseded 2026-09-15 — do not run.** Session 3's eyedropper pass (W42–W55) answered LV4 and LV5 across the sample; the axe numbers held and became **V-F23** (text contrast) and **V-F27** (table/grid lines). The two items this step left unmeasured are also closed: the ⋮ row-menu glyph measured **21:1** by pixel sampling 2026-09-17 (R001 O12, a pass), and the image-painted button captions stay recorded as unmeasured-by-design. Only **S13's LV5** is still open, and it is one line in W68.

### W31 — Text spacing and orientation (LV3, LV8)

**Do:** Apply a text-spacing bookmarklet/stylesheet (line-height 1.5, letter
0.12 em, word 0.16 em, paragraph 2 em) on Take Assignment; then rotate /
resize to a portrait-shaped window.
**Tell me:** Any clipped or overlapping text (MathJax, keypad buttons, the
problem navigator), and whether portrait works.
**Measured 2026-09-11 (view_probe, LV3/LV8):** the text-spacing override clips the date cells on Class Management (both modes), the Calendar and Take Assignment (measured fail: R019, R024, R042, R083); the other ten views tolerate it (pass). Orientation: no orientation media query or lock on any view (LV8 pass everywhere). **What remains for you:** a glance at the four clipping views with the override on, to confirm the clipped text is real content loss.
**Feedback:** **Superseded 2026-09-15 — do not run.** Session 3 photographed the clipping over CDP and you ruled **no content loss**, which set 1.4.12 to Supports. LV3 and LV8 are answered on every view. Nothing left here.

---

## Part G — No-color pass (grayscale)

Runs:
```
python scripts/review.py log-test the-expert-ta --view S3 --modality no-color --tool grayscale --task T2 --url "UI: Class Management → assignment row → Take Assignment"
python scripts/review.py log-test the-expert-ta --view S4 --modality no-color --tool grayscale --task T5 --url https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547
```
Windows Settings → Accessibility → Color filters → Grayscale.

### W32 — The grayscale pass (NC1, NC3 — expanded 2026-09-21) — KEY STEP

**This is the whole of 302.3 — Without Perception of Color, and it is the
largest block of unanswered rows left in the review: NC1 and NC3 are blank on
all ten pages.** NC2 (links) is already measured everywhere, so this step is
the two rows a person has to judge, and one sitting closes the FPC.

**Setup, once:** Windows Settings → Accessibility → Colour filters →
**Grayscale**, on. No screen reader needed. Leave it on for W41 and W73 below,
which are the same kind of question.

**The two rows, in plain words:**
- **NC1** — is anything told to you *only* by colour? A status, an error, a
  required field, a "this one is late", a value you are meant to act on.
- **NC3** — with colour gone, can you still work the page and understand it?

**Where colour actually carries meaning** — measured, so you can go straight
to these rather than hunting:

| Page | Look at | The question |
|---|---|---|
| **Take Assignment** (`/Common/TakeTutorialAssignment…`, Problem 1) | the **red randomised variable values** (`#FF6347`, e.g. "25", "13") inside the problem statement | these are the numbers you must calculate with. In grey, can you still tell which numbers are yours? |
| **Take Assignment**, hint/feedback area | the **orange deduction percentages** (`#FF9900` — "4%", "5%", "25") | these say what a hint costs. In grey, is the cost still identifiable as a warning? |
| **Take Assignment**, problem navigator | the per-problem status marks | is status carried by a **symbol or wording**, or only by colour? |
| **View Grade Report** (assignment row → View Grade Report) | the **red "late" date text**, and the blue **[?]** links | is "late" said anywhere in words, or only in red? Are the [?] links findable? |
| **Calendar** (top menu → Calendar) | the event bar, white on `#8EA9DB` | does the bar still read as an event? |
| **View Assignment Solutions** | the same red value token as Take Assignment | same question as row 1 |

**The other four pages** — Class Management (both modes), Student Practice
Area, Printable Assignment, Sign in, Password reset — carry no colour-coded
status that the sweeps could find, so "nothing conveyed by colour here, page
still works" is a complete answer for each. I have an achromatopsia capture of
every page in `evidence/runs/*/R*-grayscale.png` if you would rather judge
from those than switch the filter on.

**Tell me:** for each row above, yes or no, and if colour is *not* the only
carrier, what else carries it (bold, a symbol, wording). Then one line for the
other pages.
**Why it matters:** 302.3 is one of three FPC still open, and 1.4.1 is the
only criterion in the review with failed checks and no `05` decision. This
step plus W41 and W73 finishes both.
**Feedback:** 2026-09-21 — answered, and it decided 1.4.1. *"The contrast of
the orange-red numbers are very hard to see when at greyscale … all contrast
fails in greyscale … hint fails, random values fail, navigator fail, status
marks pass … class assignment and class news fail … no grades to view … in
calendar, the name of the assignment in the calendar, the bar that extends
across days, fails totally … the orange-red colors use for numbers in the
ViewAssignmentSolution fails."*

Recorded: **Take Assignment** NC1/NC3 fail (R109 O5, Result **Broken** for
this modality — the randomised values are the numbers that go into the
calculation); **Calendar** fail, "totally" (R102 O3, Broken); **View
Assignment Solutions** fail (R110 O5, Broken); **Class Management** NC1
partial / NC3 fail (R099 O4, Works with issues — nothing is *operated* by
colour, but the headings labelling the two grids wash out). The
**status marks passing** is recorded as the exception and the fix: a symbol
carries them, so colour is not their only channel. → finding **V-F31**
(Major, proposed) and `05` **1.4.1 → Does Not Support**, which clears the
review's last integrity flag of that kind. The contrast half of the same
elements stays under V-F23 (1.4.3) — "hard to see" and "colour is the only
carrier" are two different failures and both are recorded.

**Closed 2026-09-21 by your same-styles ruling** — *"the styles are the same
across the app, if the other views use the same colors lets assume they also
fail."* Taken as the conditional it is: each remaining view was scanned for the
tokens you failed, so the rule is applied where it holds and not where it does
not (`evidence/colour-token-scan-2026-09-21.json`).
- **Printable Assignment** → **fail**. `#FF6347` on 10 elements, and the
  sample text is "25", "13", "9.5" — the randomised values themselves. Same
  token, same job as Take Assignment. Run **Broken**. It matters twice here:
  this page is the candidate alternate route for *reading* an assignment.
- **Student Practice Area** → NC1 partial, NC3 fail. Only `#EFBB75`, on the
  "Library" heading — the "Class Assignments" case again. **Works with issues**.
- **Sign in** and **Password reset** → **NC1 pass**. Their only shared token is
  teal on headings and field labels — "Log In", "User Name:" — words that
  already say what they are. None of the tokens that carry *meaning* is on
  either page. The ruling does not fail them, so they are not failed.
- **Accessibility Mode** → **not measured.** `default2.aspx` redirects to
  `default.aspx` (the trap from 2026-09-11), and reaching it means pressing
  "Accessibility Page", which is **stored on your account** — not the
  assistant's to change. One line from you when you are next in that mode.

**And a correction on View Grade Report** — see **W74**.

---

## Part H — No-hearing / no-speech (confirm N/A)

### W33 — Any audio or voice features in the sample? (NH1–NH4, NS1)

**Do:** Across the views used above, note any video, audio, or voice-input
feature (none was seen in exploration; the vendor's video library lives on
the marketing site).
**Tell me:** "None" — or where you found one. The assistant then logs
no-hearing and no-speech runs as **N/A** for the sampled views, which counts
as coverage.
**Feedback:** 2026-09-11 — closed by measurement (view_probe; the no-hearing and no-speech runs of every sampled view, R020/R021 … R095/R096): no `<video>`, `<audio>`, media embed/iframe or media link and no speech-input API or microphone control on any of the 14 views. NH1–NH4 and NS1 are n/a everywhere; those runs are closed as N/A. Nothing for the reviewer here.

---

## Close-out (assistant's duties when the parts above are done)

1. Every **Feedback** line filled or the step explicitly skipped, with the
   reason.
2. Each run's checks table completed and its **Result** set (Works / Works
   with issues / Broken / N/A); axe runs R001–R014 get their W1/W3 outcomes
   from what you confirmed or dismissed here.
3. Confirmed items promoted to findings in `04` — task findings under
   T1–T5 ("T2 fails at step 1 for screen-reader users: answer radios have no
   name"), view findings under §B; product-wide defects written once with
   the per-view list.
4. `05-results.md` rollup for every criterion touched; vendor-claim
   discrepancies flagged (the VPAT answers everything "Supports").
5. `03` updated: artifacts from W27 registered in §2.6; A4 location from
   W25 in §2.5; the B1/B5 decision from W1 in §1.3; any view or state found
   during the tasks added as S rows.
6. `review.py validate` and `matrix` re-run; `next` decides the following
   session (remaining view×modality cells: S6, S8, S9, S10, S11, S12, R1, R2
   under the manual modalities, and cognition on S1/S5).

---

## 2026-09-14 — Session 2: what is left, in order

**State at open** (`review_db.py state`): done 3/12 — 9/55 criteria decided,
1/5 tasks with a verdict, 13 of the steps above still pending, and 40
fail/partial check outcomes on criteria whose `05` block is still Not
Evaluated (37 of them measured by the probe on 2026-09-11 and waiting on
your confirmation). Since 2026-09-11 the assistant closed R017's NV10 row
from your narration and drafted three `05` outcomes as *provisional* (W36).

**Pre-flight (assistant, 2026-09-14):** the debug-profile Chrome (port 9222)
was not running; relaunched with the full flag set and it landed on
`login.theexpertta.com` — the shared session has expired. **Sign in there
before W34** (the assistant never authenticates). Nothing browser-side can
be measured until then (the hover check in W35 (d), any re-probe).

**Order for this session:** W34 → W35 → W36 → W37 → W6 → W21 → W22 → W23 →
W24 → W25 → W26 → W27 → W28 → W29 → W30 → W31 → W32. W34 first because T1's
verdict depends on it and it has been owed since 2026-09-10; W35/W36 next
because each is a one-word answer that decides a `05` block.

### W34 — Standard-mode Class Management with NVDA (S1, run R015) — KEY STEP (T1 verdict)

**Do:** On Class Management, look at the mode button. If it reads
**"Non-Accessibility Page"** you are still in Accessibility Mode (the shared
account stores the mode; it was left there on 2026-09-10) — activate it. The
button must read "Accessibility Page" and the URL must be `default.aspx`,
not `default2.aspx`. Then repeat W4–W9 on this page: `NVDA+T`; `H`, `D`,
`NVDA+F7`; arrow from the top to the bottom; Tab once from the top (the
`aria-hidden` logo link, R001 O3); focus the two DevExpress editors
"Classes" / "Class Menu" and open each with `Alt+Down`; the jump point;
the assignment row's **⋮** action menu without the mouse (Enter, Space,
Applications key on the row and on the ⋮ cell); `G` for any graphic.
**Tell me:** one line per row of R015 — NV2 headings/landmarks; NV3
the editors' and the ⋮ menu's name/role/value on focus; NV4 what `G` finds
and what the logo announces; NV5 reading order; NV6 whether the editors
announce "Classes"/"Class Menu" at all; NV7 what is announced when the ⋮
menu opens (if it opens); NV8 anything you could only place by position;
NV10 the link texts you heard.
**Why it matters:** standard mode is what every student lands on; the only
human run of Class Management is R016 on the vendor's alternate page (S2).
It decides whether V-F1, V-F7 and V-F8 (all "also S1 per axe") are
confirmed on S1, whether the ⋮ menu is keyboard-operable (T1 step 3 — if
not, T1 fails in standard mode and the Accessibility Page is the only
route), and it lets T1 get a verdict.
**Feedback:** 2026-09-14 — Done in standard mode (assistant asked first: the
tab was still on `default2.aspx` and the first narration matched S2; reviewer
confirmed the switch — "the table is different, no Go button"). Title
"Class Management" (NV1). No headings or landmarks (NV2 → V-F1 confirmed on
S1). First Tab stop: the hidden accessibility-instruction div, read out in
full. Reading order as expected; the grid captions and columns are not
meaningful for Class Management vs Class News (NV8 → V-F2 confirmed).
Classes / Class Menu editors: an instruction on focus, no meaningful label,
the purpose first heard at the Go button (NV6 → V-F7 confirmed). Jump point
reads the div text. **⋮ row menu: not focusable — "Only way to nav is by
clicking the table row"** → R015 O10, **T1-F3** (2.1.1, 4.1.2; Major, Blocker
for the page alone), **T1 verdict drafted Fail**, 05 2.1.1 → Does Not
Support (provisional). Logo has alt; two "collapsed graphic clickable"
expand controls without role or name → **V-F16** (Minor). **Open:** NV7 (is
the mouse-opened menu announced?) and NV10 (Links list) — two questions in
R015; Result is set to Broken once answered. Reviewer to confirm the T1
verdict and the alternate-version ruling on T1-F3.
**Update 2026-09-14 (later the same day, recorded in `04`/`05`):** the reviewer
overruled the draft — T1-F3 re-rated **Minor** (Accessibility Mode accepted as
the alternate route: "not an ideal solution, but it does allow access. Not
fail"), **T1 verdict = Pass with barriers**, `05` 2.1.1 → **Partially
Supports**. NV7/NV10 closed under W40; R015 Result = Broken. W34 is done.

### W35 — Confirm or rule out the measured fails (six `05` decisions) — KEY STEP

Each item was measured by `view_probe` on 2026-09-11 in the run(s) named. A
measured fail is not a finding until you confirm it or rule an exception
(modality-checks.md §Assistant-answerable). Answer each with **confirmed**,
**exception — <reason>**, or **look again — <what>**. On "confirmed" the
assistant writes the finding named, the `05` outcome, and sets each run's
rows; nothing is written before your word.

- **(a) 1.4.10 Reflow — every one of the 14 views.** The layout is a fixed
  1300 px container (`div#container`); at 320 CSS px every page scrolls in
  two dimensions (LV1 fail on R019, R024, R030, R036, R042, R048, R054,
  R060, R066, R072, R078, R083, R088, R094; S11's popup measures 589 px,
  the sign-in page 1024 px). Proposed: **V-F19**, Major, 1.4.10,
  product-wide; `05` → Does Not Support. W29's real-zoom look still decides
  LV2 (loss/overlap) and LV7 (focus ring) — those are separate rows.
- **(b) 1.4.12 Text Spacing — S1, S2, S3, S6.** Under the override, text is
  newly clipped in: S1 the four date cells of the assignment row and the
  "Welcome to Testing Course…" line; S2 the assignment-name cell and a
  grid caption; S3 the assignment-code div ("6M79-C9-72-46-B37E-17547");
  S6 a calendar event ("30311 Chapter 5 Sample Assignment…"). The other ten
  views tolerate it (LV3 fail on R019, R024, R083, R042). Proposed:
  **V-F20**, Minor if the clipped text is still readable / Major if the due
  dates on S1 are cut off; `05` → Partially Supports. W31 is the look.
- **(c) 2.5.8 Target Size — S1, S3, S5.** S1: the row's **⋮** menu
  (16×16 px) beside the 9×10 px expand glyph (R022). S3: the nine
  problem-navigator links are **8×18 px** and adjacent to each other
  (R018). S5: the DevExpress spin/time editor up/down buttons are 16×9 px,
  14 of them (R039). Proposed: **V-F21**, Minor (the ⋮ has an equivalent
  — the Accessibility Page's Actions select; the S3 problem links have
  none), 2.5.8; `05` → Partially Supports. Your ruling per group:
  essential / equivalent-exempt / confirmed.
- **(d) 1.4.1 Use of Color — links in running text told apart by colour
  only, six views.** S4 and S8 the class and assignment links at the top;
  S3 "detailed view"; S6 "Select All" / "Only"; R2 the "Grade Sheet -
  Class" link; S2 the "Tab for Class News" skip link (NC2 fail on R100,
  R110, R109, R102, R107, R111). The probe measured the resting state only.
  Proposed: **V-F22**, Minor, 1.4.1; `05` → Partially Supports **unless**
  the links gain an underline on hover and focus and sit at ≥ 3:1 against
  the surrounding text (the accepted technique) — the assistant measures
  hover/focus over CDP once you are signed in, before you answer. W32's
  grayscale look (NC1, NC3) is separate.
- **(e) 1.3.5 Identify Input Purpose — Sign in (S7).** The "User Name:"
  field carries no `autocomplete` (CO9 fail on R098, signed-out profile).
  Proposed: **V-F17**, Minor, 1.3.5; `05` → Partially Supports. Question:
  is the user name an email address or a username (both have an
  `autocomplete` token, so the fail stands either way), and does the
  password field carry one (the probe listed only the user-name field)?
- **(f) 3.1.1 Language of Page — S3, S7, S11.** No `lang` on Take
  Assignment (R004 O2 axe; R017 NV9 partial), Sign in (R093) and the Edit
  Class popup (R077); the other 11 views declare `en`. Proposed: **V-F18**,
  Minor (an English default voice masks it; a user whose synthesizer
  defaults to another language hears the assignment mispronounced), 3.1.1;
  `05` → Partially Supports. 3.1.2 is drafted in W36.

**Feedback:** 2026-09-14 — Reviewer: "(a) no reflow detected. (b) can't
reproduce. Also, I don't know what S1 S2 S3 S4 means, update your guidance
to refer to specific pages and page states for me to reproduce your
findings. (c) again I don't know what that means. (e) no app-specific
autocomplete but works fine with Chrome password manager. (f) your call."
Recorded: **(e)** → **V-F17** (1.3.5, Minor, the password-manager
mitigation in the finding), 05 → Partially Supports. **(f)** → **V-F18**
(3.1.1, Minor, on delegation), 05 → Partially Supports. **(a), (b), (c) not
answerable as written** — the steps named view codes and gave no
reproduction recipe; rewritten as W38–W40 below with the page named in
words and the exact setup. Process fixed the same day (testing-loop.md
§How to build one step 5; modality-checks.md §Assistant-answerable). The
remaining proposals are renumbered: (a) V-F19, (b) V-F20, (c) V-F21,
(d) V-F22. **(d) measured 2026-09-14** (probe extended: hover cue from the
stylesheets, focus cue by focusing the link, link-vs-text contrast; "running
text" now means the parent has its own text around the link, which dropped
the breadcrumb-style link lists): the Calendar's "Select All"/"Only", the
spreadsheet's grade-sheet link, Take Assignment's "detailed view" and the
Accessibility Mode skip link are **not in running text** → NC2 n/a on
R102, R107, R109, R111. What remains: on **View Grade Report** and **View
Assignment Solutions**, in the title line at the top ("Grade Sheet - Class:
Testing Course for CSU East Bay - Assignment: Chapter 5 Sample
Assignment"), the class name and the assignment name are links with **the
same colour as the surrounding text (1:1)**, no underline; they gain an
underline on hover and an outline on focus (R100, R110). → W41.

### W36 — Four `05` judgments drafted from your 2026-09-10 narration — confirm or overrule

Written into `05` as **(provisional)** on 2026-09-14; the remark of each
block carries the reasoning. Say "agree" or give the outcome you want.

- **2.4.6 Headings and Labels → Supports (provisional).** The criterion
  requires headings and labels *that exist* to be descriptive; it does not
  require headings. No-headings is V-F1 / T1-F1 under 1.3.1; the visible
  captions and labels are descriptive; their missing association is 1.3.1
  / 3.3.2 / 4.1.2.
- **1.3.3 Sensory Characteristics → Supports (provisional).** No
  instruction relies on shape, position, size or colour; the position-only
  identification NV8 recorded (grids, math option, hint) are consequences
  of the 1.3.1 / 4.1.3 defects already found.
- **3.1.2 Language of Parts → Not Applicable (provisional).** No passage in
  another language in the sample.
- **3.3.1 Error Identification → still Not Evaluated, on purpose.** The NV6
  fails on R016/R017 are *label* defects (3.3.2). Error identification has
  one pass so far — the "Incorrect Answer … refer to your submission
  history" dialog (R017 O11) — and no test of a validated form (sign-in
  with a wrong password, the Create/Edit Assignment popup with an empty
  Name). Process change 2026-09-14: NV6 now covers labels only and a new
  row **NV12** covers errors (3.3.1); `sync-checks` added NV12 to every
  no-vision run. NV12 on S7 (sign in, wrong password) and S11 (empty
  required field) are the two steps that decide 3.3.1 — W37.

**Feedback:** _(pending)_

### W37 — Error identification on a validated form (NV12, CO4) — decides 3.3.1

Runs: the existing no-vision runs for S11 (R077) and S7 (R093 — signed-out
profile only; never point the signed-in tab at the sign-in page).
**Do:** (1) S11: Class Menu → "Edit Class" (or Create Assignment) popup;
clear the Name field; Save. (2) S7, in the **signed-out** window on port
9223 only: enter a wrong password; submit.
**Tell me:** For each: is an error message announced without hunting; does
it say *which* field and *what* is wrong; is the field itself marked
(`aria-invalid`, the label changing); is a fix suggested (CO4 / 3.3.3).
**Feedback:** _(pending)_

### Page key — what the view codes mean (added 2026-09-14 at the reviewer's request)

The codes are the process's bookkeeping. Every step from here on names the
page in words; this table is the translation for anything above.

| Code | Page, in words | How to get there |
|---|---|---|
| S1 | **Class Management, standard mode** | `https://dei56mo.theexpertta.com/common/default.aspx` — the mode button reads "Accessibility Page" |
| S2 | **Class Management, Accessibility Mode** | same page after pressing "Accessibility Page" (`default2.aspx`) — the button then reads "Non-Accessibility Page" |
| S3 | **Take Assignment** — "Chapter 5 Sample Assignment", problems 1–9 | Class Management → assignment row → Take Assignment (row ⋮ menu in standard mode; Actions select → Go in Accessibility Mode) |
| S4 | **View Grade Report** for that assignment | assignment row → "View Grade Report (shows your detailed work)" |
| S5 | **Assignment Editor** (editing the assignment) | Class Menu → Edit Class Assignment (or the row's Edit) |
| S6 | **Calendar** | top menu → Calendar (`/common/calendar.aspx`) |
| S7 | **Sign in** | `https://login.theexpertta.com/Login.aspx` — **only in the signed-out window** (port 9223); opening it in the signed-in window ends the session |
| S8 | **View Assignment Solutions** | assignment row → View Solutions |
| S9 | **Class Assignments Grade Sheet** (instructor pivot grid) | Class Menu → View/Manage Class Grades |
| S10 | **Manage Class Roster** | Class Menu → View/Manage Class Roster |
| S11 | **Edit Class popup** | Class Management → Class Menu → Edit Class → Go (opens in a popup) |
| S12 | **Student Practice Area** (the student library browser) | direct address `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` — the top-menu "Practice" link goes elsewhere (Practice Mode for the assignment, which the demo does not enable; corrected 2026-09-15) |
| R1 | **Academic Integrity Preferences** | Class Menu → Academic Integrity Preferences |
| R2 | **View Grades, spreadsheet view** | Class Menu → View/Manage Class Grades → spreadsheet view |

### W38 — Reflow: does the page fit a narrow window without sideways scrolling? (replaces W35 (a); decides 1.4.10)

**Page:** Class Management, standard mode (`/common/default.aspx`), then
Take Assignment (any problem).
**Setup — do exactly this:** make the Chrome window about **1280 px wide**
(Windows key + Left snaps it to half of a 2560-wide screen; on a 1920
screen un-maximise and drag it to roughly two-thirds width). Then press
`Ctrl` + `+` until the zoom indicator in the address bar reads **400%**
(eight presses from 100%). Press `Ctrl` + `0` afterwards to reset.
**Look at:** the bottom edge of the window. A **horizontal scrollbar**
appears if the page does not reflow; drag it or press `Shift` + scroll to
see the right-hand part of the page.
**What "fail" looks like:** at 400% you must scroll sideways to read a
line of text or to reach a control (the assignment row's ⋮, the Go
buttons, the problem's Submit button). What "pass" looks like: the page
re-stacks into one column and only vertical scrolling is needed.
**What the instrument says:** the layout is a fixed 1300 px-wide box
(`div#container`), so at 400% on a 1280 px window it should overflow by a
factor of four on every page.
**Tell me:** "sideways scrollbar, yes/no" for each of the two pages, and
whether anything is cut off or overlaps (the anti-cheating watermark,
the problem navigator, the keypad).
**Feedback:** 2026-09-15 — Class Management (`default.aspx`): "nothing is
hidden or lost at 400%, but no reflow". Take Assignment: "nothing is lost,
but no reflow". → LV1 confirmed fail on R019 and R083 (O5 each), LV2 pass
on both; finding **V-F19** (1.4.10, Major, product-wide — the same fixed
container measured on all 14 pages); `05` 1.4.10 → **Does Not Support**.

### W39 — Text spacing: does widened text get clipped? (replaces W35 (b); decides 1.4.12)

**Page:** Class Management, standard mode, then Take Assignment.
**Setup — do exactly this:** create a bookmark whose address is the line
below (Chrome: `Ctrl` + `Shift` + `O` → ⋮ → Add new bookmark → paste the
line into the URL field, name it "Text spacing"), then click it while on
the page:

```
javascript:(function(){var s=document.createElement('style');s.textContent='*{line-height:1.5!important;letter-spacing:0.12em!important;word-spacing:0.16em!important}p{margin-bottom:2em!important}';document.head.appendChild(s);})();
```

Reload the page to undo it.
**Look at:** the assignment row's four date cells (publish / start / due /
end), the "Welcome to Testing Course…" line, and on Take Assignment the
assignment code under the title (looks like `6M79-C9-72-46-B37E-17547`).
**What "fail" looks like:** text is cut off mid-word, the end of a date is
hidden, or two texts overlap after the bookmarklet runs. "Pass": everything
is still readable, just more spread out.
**What the instrument says:** the date cells and the welcome line on Class
Management, the assignment name cell in Accessibility Mode, the assignment
code on Take Assignment and one Calendar event clip under this override.
**Tell me:** which of those texts (if any) is actually unreadable after the
bookmarklet, and whether the due date is one of them.
**Feedback:** 2026-09-15 — Reviewer: "bookmarklet don't know what this
means"; at 400 % without the override "nothing in the list is cut off"
(that is the LV2 answer, already recorded under W38 — not LV3). Step
re-done by the assistant: the override is applied over the debug Chrome
and the clipped spots are screenshotted into each run folder
(`R019-textspacing*.png`, `R083-textspacing*.png`, `R042-textspacing*.png`)
so the question becomes "look at these pictures — is the cut-off text
still readable?" → see W39b below. Still open.

### W39b — Text spacing: look at three pictures (replaces the bookmarklet; decides 1.4.12)

The assistant applied the text-spacing override through the debug Chrome
and photographed the spots that clip. Open the files (they are in the
review folder under `evidence/runs/`) and answer per picture.

1. **`R019/R019-textspacing-5.png`** — Class Management. Every date on the
   assignment row has lost its **AM/PM** ("Sep 08, 2026 11:59" — no PM)
   and the Start date its last minute digit. *Is a due date without AM/PM
   information a student needs?* → "confirmed" (content loss) or
   "exception — <why>".
2. **`R083/R083-textspacing-2.png`** — Take Assignment. The red box under
   the Submit / Hint buttons is where the assignment code
   (`6M79-C9-72-46-B37E-17547`) normally shows; under the override it is
   **empty** — the code is pushed out of its box. *Does a student ever need
   that code (support requests, integrity checks)?* → confirmed / exception.
3. **`R042/R042-textspacing-1.png`** — Calendar. A scrollbar appears over
   the grid and covers the right half of every **Saturday date number**;
   the event bars are intact. → confirmed / exception (minor).

Accessibility Mode (S2) could not be photographed — the account is in
standard mode and `default2.aspx` redirects — its measured clip is the
assignment-name cell and a grid caption, the same table as picture 1.
**Tell me:** three words — one per picture — and, if any is "confirmed",
whether you rate the finding Minor (cosmetic clipping) or Major (the
due-date AM/PM).
**Feedback:** 2026-09-15 — "no issues noted with text spacing" → LV3 pass
on R019, R024, R083, R042 (reviewer's ruling over the measurement; the
pictures and measurements stay in the runs); no finding; `05` 1.4.12 →
**Supports**. R019 Result → **Works with issues** (V-F19, V-F23).

### W40 — Small click targets (replaces W35 (c); decides 2.5.8)

WCAG 2.5.8 says a clickable thing should be at least **24 × 24 px**, or
have empty space around it so a neighbouring target is not hit by mistake
— unless the same action is available another way on the page, or the
size is essential. The instrument found three groups smaller than that
with a neighbour inside the 24 px circle. You rule on each group.

**Page 1 — Class Management, standard mode:** the assignment row's **⋮**
menu icon (16 × 16 px) sits right beside the small **+** expand glyph
(9 × 10 px). *Question:* is there another way, on this same page, to do
what the ⋮ menu does? (If the only alternative is switching to
Accessibility Mode, say so — that is a different page.)
**Page 2 — Take Assignment:** the nine **problem-number links** in the
navigator on the left are 8 × 18 px each, side by side. *Question:* is
there another way on the page to move to a given problem (the
Ctrl+Shift chords? the "Continue to the next question" link after a
submit?), or is the navigator the only route?
**Page 3 — Assignment Editor:** the tiny **up/down arrows** on the Weight
spinner and the three time fields (16 × 9 px each). *Question:* can the
same values be typed into the field directly? (If yes, the arrows are
exempt — an equivalent control exists.)
**Tell me:** for each of the three groups: "exempt — <the other way>" or
"confirmed — no other way".
**Feedback:** 2026-09-14 — (1) "no other way found" → confirmed; (2) "no
alternative found" → confirmed; (3) "yes, can be typed directly" → exempt.
→ R022 MO9 fail, R018 MO9 fail (confirmed), R039 MO9 → pass (exempt);
finding **V-F21** (2.5.8, Minor, S1 + S3); 05 2.5.8 → Partially Supports.
Also closed from the same message: R015 NV7 — the ⋮ menu's opening is not
announced, items only on mouse-over (O12); R015 NV10 — the Links list is
empty (O13, n/a). R015 Result → **Broken**.

### W41 — Are the two title-line links recognisable as links? (replaces W35 (d); decides 1.4.1)

**Page:** View Grade Report (Class Management → assignment row → "View
Grade Report"), then View Assignment Solutions (assignment row → "View
Assignment Solutions").
**Look at:** the title line at the top of each page: "Grade Sheet - Class:
Testing Course for CSU East Bay - Assignment: Chapter 5 Sample Assignment".
The class name and the assignment name are links to the class grade sheet
and the assignment grade sheet.
**What the instrument says:** both links are the **same colour as the rest
of the line** and have no underline until the mouse is over them (then
underlined) or they have keyboard focus (then outlined).
**Tell me:** without moving the mouse over them, can you tell they are
links at all? If not: "confirmed" (they are indistinguishable at rest —
1.4.1 / F73); if something I have not measured marks them (a different
weight, an icon), say what.
**Feedback:** _(pending)_

## 2026-09-15 — Session 3: complete no-vision (302.1) and low-vision (302.2) on every page

**State at open** (dashboard §1): no-vision tested on 2 of 14 pages
(Class Management standard mode R015, Take Assignment R017 — both Broken);
low-vision on 0 of 14. Every cell already has a run — the probe's — so no
`log-test` is needed: your narration completes **that run** (the assistant
sets its Tool/Baseline to the instrument you used). The rows still open:

| Instrument | Pages | Rows per page |
|---|---|---|
| NVDA (no-vision) | 11 pages: NV2 NV3 NV4 NV5 NV6 NV7 NV8 NV10 NV12; Accessibility Mode only NV4 NV5 NV12 | 9 (3 on Accessibility Mode) |
| Zoom + eyedropper (low-vision) | all 14 pages: LV2 LV4 LV5 LV6 LV7 LV9 (LV1/LV3/LV8 measured; W38/W39 decide LV1/LV3) | 6 |

**Pre-flight (assistant, 2026-09-15):** the debug-profile Chrome (port 9222)
is on `login.theexpertta.com` — the shared session expired again. **Sign in
there first** (the assistant never authenticates). Sign-in page steps use
the signed-out window on port 9223 only.

**Order:** W38 → W39 (two answers that close LV1/LV3 on all 14 runs) →
Part I zoom, one page at a time (W42–W55) → Part J NVDA, one page at a time
(W56–W67). Zoom first because it needs no screen reader and the eyedropper
targets are already listed; switch NVDA on once for Part J. Say the step
number when you start; skip or reorder freely — just say so.

### Part I — Low-vision, page by page (LV2, LV4, LV5, LV6, LV7, LV9)

**Setup once:** window about 1280 px wide (Windows key + Left on a wide
screen). For each page: press `Ctrl` + `+` until the address bar reads
**400%** (eight presses), look, then `Ctrl` + `0` back to 100 % for the
eyedropper. Eyedropper: PowerToys Color Picker (`Win+Shift+C`) or DevTools;
measure the rendered pixel, not the CSS value. The axe ratios in brackets
already resolved a plain background — say "matches" when they do.

**Every page, the same five things to tell me:**
- **(LV2) at 400 %** — is anything cut off, overlapping, or no longer
  reachable (a control you cannot scroll to)? Ignore the sideways scrolling
  itself — W38 records that.
- **(LV7) at 400 %** — Tab through three or four controls: is the focus
  ring visible each time, and not hidden under a sticky header or edge?
- **(LV9) at 400 %** — is any text actually a picture (it goes blurry or
  blocky instead of crisp)? Logos are exempt.
- **(LV4/LV5) at 100 %** — eyedropper the elements listed for the page.
  Text needs 4.5:1 (3:1 if it is 18 pt+ or 14 pt bold); control borders,
  icons and the focus ring need 3:1. DevExpress buttons (Go, Save, the
  toolbar) are painted with an image, so axe could not measure them —
  measure one on each page that has them.
- **(LV6)** — does anything appear when you hover or Tab onto something
  (a tooltip, a popover)? If yes: can you dismiss it with `Esc`, can you
  move the mouse onto it without it vanishing, does it stay until you move
  away? If nothing appears anywhere on the page, say "nothing" → n/a.

### W42 — Class Management, standard mode (S1, run R019)

**Page:** `https://dei56mo.theexpertta.com/common/default.aspx` — the mode
button reads "Accessibility Page".
**Eyedropper:** "Classes" / "Class Menu" captions teal `#48848C` on white
[4.23:1 — fails 4.5]; "Class Assignments" heading `#EFBB75` [1.74:1]; "Class
News" heading `#E58F65` [2.48:1]; the grey "Welcome to Testing Course…" line
`#808080` [3.94:1]; the **⋮** row-menu glyph [unmeasured]; the **Go** button
text and border [unmeasured, image background]; the Classes / Class Menu
editor borders [unmeasured].
**Feedback:** 2026-09-15 — LV2 pass (from W38). "focus ring visible with
tab" → LV7 pass. "no text goes blurry" → LV9 pass (the blurry assignment
figures belong to Take Assignment → R083 O6, W44). Eyedropper: teal on
white "Large pass, Fail regular for AA" (captions are 16 px → fail);
`#EFBB75` "fail for all levels"; `#808080` "only passes for large in AA"
(12 px → fail) → LV4 fail, finding **V-F23** (1.4.3, Major — confirm the
rating), `05` 1.4.3 → Partially Supports. "Pass for UI component" → LV5
pass. "Only thing that appears when tabbed … is the accessibility
instructions" → LV6 pass. R019 now waits only on LV3 (W39b).

### W43 — Class Management, Accessibility Mode (S2, run R024)

**Page:** press "Accessibility Page" (`default2.aspx`); the button then
reads "Non-Accessibility Page".
**Eyedropper:** "Class Assignments" `#EFBB75` [1.74:1]; "Class News" `#E58F65`
[2.48:1]; grey welcome line `#808080` [3.94:1]; the native **Go** buttons and
the Actions select border [unmeasured].
**Feedback:** 2026-09-15 — "no for accessibility mode at 400" → LV2 pass.
"No blurry text other than the images. Focus ring is fine, Go button
passes contrast and is not blurry." → LV9, LV7, LV5 pass. LV4 fail on the
same heading/notice colours as standard mode (V-F23; axe R005 measured the
identical hex values the reviewer eyedroppered on S1). "no hover issues" →
LV6 pass. **R024 Result → Works with issues** (V-F19, V-F23).

### W44 — Take Assignment (S3, run R083)

**Page:** assignment row → Take Assignment; look at Problem 1 (free-body
diagram), Problem 2 (symbolic entry + palette), Problem 8 (multiple choice
with math).
**At 400 % also:** the problem navigator on the left, the keypad / palette,
the anti-cheating watermark over the problem text, the MathJax formulas
(MathJax renders as text — it should stay crisp).
**Eyedropper:** hint/feedback deduction "4%" orange `#FF9900` [2.14:1]; red
randomized-variable values `#FF6347` (Problem 1: "25", "13") [2.94:1];
problem-navigator numbers `#3A7C89` on `#F5F5F5` [4.35:1 — fails 4.5];
"Part (b)" identifiers [4.35:1]; the **Submit** button; the palette keys.
**Feedback:** 2026-09-15 — LV2 pass (W38). "No new issues are obvious for
assignment pages at 400: this can be passed" → LV7 pass. "The blurry images
do contain text, usually math" → LV9 fail; "1 and 6 contain images that
fail color contrast as they contain text over a graphic" → LV4 fail;
finding **V-F24** (1.4.5 + 1.4.3, Major — confirm the rating), `05` 1.4.5
→ Partially Supports. Also: View Printable Assignment
(`/Common/ViewAssignmentDetails.aspx`) recorded as **S13** in 03 §3.1 at
the reviewer's request → W68/W69. "Submit button and others pass
contrast, Nothing." → LV5 pass, LV6 pass. **R083 Result → Works with
issues** (V-F19, V-F23, V-F24). Take Assignment low-vision complete.

### W45 — View Grade Report (S4, run R030)

**Page:** assignment row → "View Grade Report (shows your detailed work)".
**Eyedropper:** red variable values `#FF6347` [2.94:1]; red "11000"-style
MathJax values `#FF0000` [3.99:1]; grey italic "All date times are displayed
in Pacific Standard Time" `#808080` [3.94:1]; red "Red submission date times
indicate late work." `#FF0000` [3.99:1] — this one also carries meaning by
colour; note it for the grayscale pass (W32).
**At 400 % also:** the per-problem tables — data tables may scroll sideways,
but nothing in them should be cut off.
**Feedback:** 2026-09-15 — "at 400 nothing cut off, requires horizontal
scrolling, same images don't scale and are blurry" → LV2 pass, LV1
confirmed (V-F19), LV9 fail (V-F24 extended to this page). "Red on white
fails AAA, passes large AA and fails regular AA, same for grey, randomized
math values fail all color contrast" → LV4 fail (V-F23). "no hover or focus
issues" → LV6 pass, LV7 pass. "line borders are too small and fail color
contrast at all levels" → LV5 fail, finding **V-F27** (1.4.11, Minor —
confirm), `05` 1.4.11 → Partially Supports. **R030 Result → Works with
issues.** View Grade Report low-vision complete.

### W46 — Assignment Editor (S5, run R036)

**Page:** Class Menu → Edit Class Assignment (or the row's Edit).
**Eyedropper:** "Assignment Details" heading `#DB715C` [3.21:1]; "Library"
heading `#EFBB75` [1.74:1]; "Books" `#3A7C89` on `#EDEDED` [4.05:1]; the
toolbar buttons (Save Only, Extensions, Messages) [unmeasured — image
background]; the spin-button arrows on Weight [unmeasured, UI component,
3:1].
**At 400 % also:** the library browser panel and the details panel side by
side — does one hide the other?
**Feedback:** 2026-09-15 — "everything is reachable at 400. Nothing hidden"
→ LV2 pass. "Assignment Details fails AAA contrast and only passes large
for AA, Library fails All" → LV4 fail (V-F23). "No hover or focus issues"
→ LV6, LV7 pass. "Just the buttons are blurry" (the image-painted faces,
not the captions) → LV9 pass. "contrast is fine" → LV5 pass. **R036 Result
→ Works with issues** (V-F19, V-F23). Videos found "in the expanding area
under library … they are auto generated" → R037 NH1 partial, finding
**V-F26** (1.2.2, Major — confirm), `05` 1.2.2 → Partially Supports; still
owed: autoplay? audio description / transcript? Aside from the same message: the **Edit Class
popup is unreachable above 175 % zoom** ("we can't scroll the page when
it is active") → R078 LV2 fail, finding **V-F25** (1.4.4 + 1.4.10, Major /
Blocker for the popup — confirm the rating), `05` 1.4.4 → Partially
Supports.

### W47 — Calendar (S6, run R042)

**Page:** top menu → Calendar (`/common/calendar.aspx`).
**Eyedropper:** the event bar "Chapter 5 Sample Assignment" white on blue
`#8EA9DB` [2.37:1]; the "Select All" / "Only" controls; the calendar grid
lines and today-marker [UI component, 3:1].
**At 400 % also:** does the month grid stay usable — can you reach every
day and the event?
**Feedback:** 2026-09-15 — "all cells reachable, no blurry text, event bar
passes, no hover or focus" → LV2, LV9, LV4, LV6, LV7 pass (the reviewer's
eyedropper overrides axe's 2.37:1 on the event bar). "grid lines fail all
contrast" → LV5 fail (V-F27 extended). **R042 Result → Works with issues.**
Also noted, for W64: "keyboard tabbing
it appears the calendar itself isn't reachable" (R045 O4) and "table desc
doesn't expose that this is a calendar, T will find the table" (R041 O3).

### W48 — Sign in (S7, run R094) — signed-out window (port 9223) only

**Page:** `https://login.theexpertta.com/Login.aspx` in the **signed-out**
debug window. Never in the signed-in one.
**Eyedropper:** "User Name:" label `#3A7C89` on `#EDEDED` [4.05:1]; the
Log In button; the field borders.
**Feedback:** 2026-09-15 — "nothing cut off at 400 at sign in window" → LV2
pass; "username fails AAA and fails regular AA" → LV4 fail (V-F23); "No
hover or focus" → LV6, LV7 pass. "login field borders ok and no blurry
text" → LV5, LV9 pass. **R094 Result → Works with issues.**

### W49 — View Assignment Solutions (S8, run R088)

**Page:** assignment row → View Solutions.
**Eyedropper:** red variable values `#FF6347` [2.94:1]; red MathJax values
`#FF0000` [3.99:1].
**At 400 % / LV9 especially:** the solution figures are images
(`…png` files, 14 without alt) — is any of them a picture of an equation
or of text that a student must read? Say which problem.
**Feedback:** 2026-09-15 — "fine at 400, images blur at 400. both fail AAA
and only large AA, no hover or focus behaviour" → LV2, LV7, LV6 pass; LV9
fail (V-F24); LV4 fail (V-F23). "final passes" → LV5 pass. **R088 Result →
Works with issues.**

### W50 — Class Assignments Grade Sheet (S9, run R048)

**Page:** Class Menu → View/Manage Class Grades.
**Eyedropper:** the grid header row and cell borders; the export-format
select and its button [image background]; "Points view" checkbox.
**At 400 % also:** the pivot grid — a data table may scroll sideways; is
the header still readable and are the filter controls reachable?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W51 — Manage Class Roster (S10, run R054)

**Page:** Class Menu → View/Manage Class Roster.
**Eyedropper:** grey "No data to display" `#808080` [3.94:1]; the class
select, code filter and export controls [image background].
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W52 — Edit Class popup (S11, run R078)

**Page:** Class Management → Class Menu → Edit Class → Go.
**Eyedropper:** the popup's Save / Cancel buttons [image background —
unmeasured]; the field borders; the field labels.
**At 400 % also:** does the popup fit — can you reach Save and Cancel, and
does the popup scroll or is it cut off by the window edge? (The probe
measured the popup at 589 px wide.)
**Feedback:** 2026-09-15 (partial, from W46) — LV2 fail: not reachable
above 175 % zoom, the page cannot scroll while the modal is active →
V-F25. Still open: LV4/LV5 (Save / Cancel, field borders, labels), LV6,
LV7, LV9.
**Update 2026-09-15:** remaining rows skipped — view removed from the sample (not student-facing).

### W53 — Student Practice Area (S12, run R060)

**Page:** paste `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` into the address bar (the top-menu "Practice" link opens the assignment's Practice Mode instead, which the demo does not enable — 2026-09-15).
**If that address gives "Warning: An Error Occurred" — the link is not the problem (2026-09-21).** The product allows **one session in one tab**, and its error page says so itself: *"You are using Expert TA in more than one tab in your browser."* It appeared because the assistant was driving one tab over CDP while you worked in another. **Close the extra Expert TA tab, keep the one you are in, reload.** `preflight.py` now fails on a duplicate product tab so this is caught before a walk rather than during one.
**Eyedropper:** "Library" heading `#EFBB75` [1.74:1]; "Books" `#3A7C89` on
`#EDEDED` [4.05:1]; the difficulty checkboxes and their labels; the Books /
Chapters selects [image background].
**Feedback:** 2026-09-15 — "main contrast issue is the tutorial text fails
AAA only fails regular AA" → LV4 fail (V-F23). The rest of the narration was
keyboard and NVDA — recorded on R063 (MO1, MO4 fail) and R059 (NV2, NV3,
NV6 fail) → finding **V-F28** (Blocker for this page — confirm). "nothing cut off at 400, focus ring is limited, but not due to zoom … no
hover issue" → LV2, LV7, LV6 pass. "final passes" → LV5, LV9 pass.
**R060 Result → Works with issues.**

### W54 — Academic Integrity Preferences (R1, run R066)

**Page:** Class Menu → Academic Integrity Preferences.
**Eyedropper:** the selected profile "Instructor Default" white on grey
`#A0A0A0` [2.61:1]; the template-options select; the grid's checkboxes.
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W55 — View Grades, spreadsheet view (R2, run R072)

**Page:** Class Menu → View/Manage Class Grades → spreadsheet view.
**Eyedropper:** the spreadsheet cell text and grid lines; the
"Grade Sheet - Class" link (same colour as text — W41 decides its 1.4.1
side; here measure it against the background).
**At 400 % also:** the spreadsheet is a data table — sideways scrolling is
allowed; frozen header/first column must not cover cells.
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### Part J — No-vision with NVDA, page by page (NV2 NV3 NV4 NV5 NV6 NV7 NV8 NV10 NV12)

**Setup once:** NVDA on, Speech Viewer open (NVDA+N → Tools → Speech
Viewer) so exact announcements can be pasted. `Ctrl+0` zoom reset. The
page title (NV1) and language (NV9) are already recorded by measurement —
skip them unless the title you hear is wrong.

**Every page, the same nine things to tell me** (one line each is enough;
"same as Class Management" is a valid answer when it is true):
- **(NV2)** `H` then `Shift+H` — any headings? `D` — any landmarks?
  `NVDA+F7` → Headings / Landmarks lists — anything in them?
- **(NV3)** Tab through the controls; on each, what NVDA says — name, role,
  state (e.g. "Go button", "Please Select combo box collapsed"). Name any
  control that announces nothing, or a wrong role.
- **(NV4)** `G` (next graphic) — what each graphic announces; any
  "graphic" with no name, or a picture that carries information but says
  nothing (figures, solution images).
- **(NV5)** arrow down from the top: does the order make sense, or does
  anything come out of sequence or in pieces?
- **(NV6)** on each form field (`F` next form field): is the visible label
  what NVDA reads on focus? Name the fields where it is not.
- **(NV7)** do something that changes the page without reloading (Go,
  filter, expand a row, save): is the change announced, and does focus
  stay where you were?
- **(NV8)** anything you could only identify by where it sits (two tables
  with the same caption, a value with no label)?
- **(NV10)** `NVDA+F7` → Links: any "click here"/"view"/"more" or two
  identical link texts going to different places? Paste the list if short.
- **(NV12)** if the page has a required or validated field: clear it (or
  enter something invalid) and submit — is the error announced, does it
  say which field and what is wrong? If the page has no validated input
  at all, say "no validated input" → n/a.

### W56 — Class Management, Accessibility Mode (S2, run R016) — three rows only

**Page:** `default2.aspx` (button reads "Non-Accessibility Page").
**Tell me:** **(NV4)** `G` — the logo and any other graphic. **(NV5)** arrow
down from the top — the order across the skip links, the two grids, the
news. **(NV12)** no validated input here? then n/a.
**Feedback:** 2026-09-21 — answered, and **R016 is now complete (Result: Works
with issues)**. *"no headings no landmarks, 1 collapsed graphic clickable 'g',
arrow order makes sense, f — form fields generally don't have labels, but they
are contained in tables and the tables do custom voicing, nv7 is as expected,
nv8 no, nv10 no all have names, no fields."*
- **NV4 fail** — one graphic, "collapsed graphic clickable", no name, no role
  → **V-F16** now covers this page too. (The logo is not reachable by `G` at
  all; it sits inside `aria-hidden`.)
- **NV5 pass**, **NV12 n/a**.
- **NV8 revised fail → pass** on your direct answer, and O3's own text backs
  it: `T` gives both grids the same generic caption, but tabbing in announces
  "Class Assignments" / "Class News" from the title divs, so they are not
  told apart by position. **V-F2 stands** — it is about the generic caption
  (1.3.1), which is an NV2/NV3 defect, not a position-only one.
- **NV10** — "all have names" does not overturn the recorded fail: V-F3 is
  not about missing names but about skip-control text that states no
  destination ("Tab for Assignments, Enter to skip…"). You answered the
  "bare click here / more" half; that half is clean.
- **NV6** — your phrase *"contained in tables and the tables do custom
  voicing"* names the mechanism, and it is the same one as the password reset
  page (V-F30). Recorded as the product-wide pattern it is.

**On "how are we missing this work" — it was not missing.** Nine of R016's
twelve rows were recorded from your 2026-09-10 walk and have been in the file
since. Three were open, and the file says why: **NV4 and NV5 read "not
narrated (W6 skipped)"** — W6 is the read-the-page-top-to-bottom step, skipped
on the day — and **NV12 did not exist as a row until 2026-09-14**, when
sync-checks split it out of NV6. The assistant's task list named the three
rows but not that history, which is what made it read as redoing finished
work. Fixed in `ontology/testing-loop.md` so a resumed page always states what
is already recorded and why the remainder is open.

### W57 — View Grade Report (S4, run R029)

**Page:** assignment row → "View Grade Report (shows your detailed work)".
**Also:** axe found 9 images with no alt (the per-problem "signature"
images) — do they announce anything under `G`? The red-means-late legend:
is "late" available any other way in the table (NV8)?
**Feedback:** 2026-09-21 — walked with W21; **R029 complete, Result Broken.**
*"no buttons have labels, there are no headings or landmarks … without
headings there is no way to jump between problems … more noise than help,
but with concerted effort the page is probably navigable … [?] are all
unlabled and announce only Visited Link … Tables have headings, however the
tables contain images in the cells which have no alt text and are therefore
fully not accessible for purpose."*
NV2/NV3/NV4/NV8/NV10 fail, NV5 pass, NV7 partial, NV6 and NV12 **n/a by
measurement** (the view has no form fields at all, so neither row needed your
time). New: **V-F33** (22 `[?]` links, entire text is punctuation → empty
name) and **V-F34** (20 images, all in table cells, 16 with no alt — the
rendering of the student's own submitted work). Your split decided the
Result: navigable with effort, but the substance is not there.
**One row left partial — NV7:** when Enter opens the accessibility menu, does
NVDA *announce* that it appeared, or do you only discover it by tabbing on?
One line closes the row.

### W58 — View Assignment Solutions (S8, run R087)

**Page:** assignment row → View Solutions.
**Also:** 14 solution images without alt — what does `G` say on each, and
does any carry the solution itself (NV4)? MathJax in the solutions — read
in browse mode or "table" (as on Take Assignment, R017 O7)?
**Feedback:** 2026-09-21 — **R087 complete, Result Works with issues.**
*"headings work, graphics have no meaningful alt text, just random characters
are announced an 'unlabled graphic clickable', math expressions on this page
voice as expected"*, then *"generally yes, controls announce name and role,
there is a sensible order, this page seems static, so no reloads, nothing only
id by position."*
**This is the best-built page in the sample for a screen reader** — NV2, NV3,
NV5, NV8, NV10 all pass, NV6/NV7/NV12 n/a. The heading outline is real (h1 +
one h2 per problem) and it is the only one in the product; recorded as a
positive in `04` because it turns V-F1 from "please add headings" into "do
what this page already does". The math voicing correctly is the positive
control for V-F9 — the notation is fine, the answer read-back is what fails
on Take Assignment.
**One fail, and it is the content:** 14 of 15 figures have no `alt`, so NVDA
reads the file name. 7 of them are written `src="….png alt="` — the
alternative text was authored and lost to a missing quote → **V-F35**,
the cheapest fix in the review. NV10 closed by measurement (10 links, all
distinctly named, no duplicates) rather than costing you another pass.

### W59 — Class Assignments Grade Sheet (S9, run R047)

**Page:** Class Menu → View/Manage Class Grades.
**Also:** the code filter field, the "Points view" checkbox and the export
select are unlabeled per axe — what do they announce on focus (NV6)? Does
`T` reach the pivot grid, and do its column/row headers read with the cells
(NV3/NV5)? Apply the filter — announced (NV7)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W60 — Manage Class Roster (S10, run R053)

**Page:** Class Menu → View/Manage Class Roster.
**Also:** class select, code filter, export select — labels on focus (NV6)?
"No data to display" — is it read (NV5)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W61 — Assignment Editor (S5, run R035)

**Page:** Class Menu → Edit Class Assignment.
**Also:** axe found 59 unlabeled fields (Name, Grade Template, Description,
Academic Integrity Template, Grade Weight, the time fields…) — take the
first six: what does each announce on focus (NV6)? The toolbar buttons
(Save Only, Extensions, Messages) — name and role (NV3)? Clear **Name** and
Save — the error (NV12)? The library browser: can the "Accessibility(AA)
Only" filter be found and its state heard (NV3)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W62 — Edit Class popup (S11, run R077)

**Page:** Class Management → Class Menu → Edit Class → Go.
**Also:** on opening — is the popup announced and is focus inside it
(NV7)? Class Name, Description, Time Zone, Academic Year, Semester — labels
on focus (NV6)? Clear Class Name and Save — the error (NV12)? The
`clear.gif` image — silent (NV4)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W63 — Sign in (S7, run R093) — signed-out window (port 9223), NVDA on

**Page:** `https://login.theexpertta.com/Login.aspx` in the **signed-out**
window only.
**Also:** the logo image (no alt per axe) and the unnamed link at the
bottom right (NV4/NV10); User Name / Password labels on focus (NV6); a
wrong password → is the error announced and does it say what to fix
(NV12)?
**Feedback:** _(pending)_

### W64 — Calendar (S6, run R041)

**Page:** top menu → Calendar.
**Also:** the month grid — does `T` find it, do day cells read with the
weekday/date (NV3/NV5)? The event "Chapter 5 Sample Assignment" — a link
or plain text (NV3)? "Select All" / "Only" — announced with a name (NV3)?
Changing month — announced (NV7)?
**Feedback:** 2026-09-21 — **R041 complete, Result Broken.** *"there is no way
to tab into the calendar, T enters calendar as its a table … the assignment is
not announced as spanning multiple days … we hear the assignment name
'clickable' but we dont hear that the assignment spans or ends on the 8th … if
we click the assignment a modal opens, no annoncement on open, the modal looks
like a form but is not, the form fielnds are not labled, there is a start due
end date, but they are calendar selection widget and not actually just info on
the assignment … month change not announced."*
Four findings: **V-F38** (no keyboard route into the grid; the event announces
"clickable" but has `tabIndex -1`), **V-F39** (the span and end date are
carried by the bar alone), **V-F40** (nothing announced — measured cause: no
`role=dialog`, no `aria-modal`, **zero** live regions on the page), **V-F41**
(unlabelled modal field, and read-only dates rendered as date pickers).
**Both sensory routes lose the same fact:** you found the bar failing
"totally" without colour, and the span unannounced without sight. A calendar
exists to say *when* something is due, and that is the one thing this one
conveys by presentation only. NV4, NV5, NV10 pass; NV12 n/a on your ruling
that the modal is not really a form.

### W65 — Student Practice Area (S12, run R059)

**Page:** paste `https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373` into the address bar (the top-menu "Practice" link opens the assignment's Practice Mode instead, which the demo does not enable — 2026-09-15).
**Also:** Books / Chapters selects and the difficulty checkboxes — labels on
focus (NV6, axe lists 12 unlabeled)? Choosing a book — do the chapters
update with an announcement (NV7)?
**Feedback:** 2026-09-15 (partial, from the W53 narration) — NV2 fail (no
headings, uncaptioned tables), NV3 fail (expand images unnamed / not
controls, checkboxes are spans), NV6 fail (no labels) → V-F28, V-F1, V-F5,
V-F16. Still open: NV4 (`G`), NV5 (reading order), NV7 (choosing a book —
announced?), NV8, NV10 (links list), NV12 (n/a if no validated input). Also
re-check NV11 / NH1: the first practice problem says "watch the following
brief video".

### W66 — Academic Integrity Preferences (R1, run R065)

**Page:** Class Menu → Academic Integrity Preferences.
**Also:** the profile list ("Instructor Default"), the template-options
select and the grid checkboxes — labels and states on focus (NV3/NV6,
12 unlabeled per axe)? Changing an option — announced (NV7)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W67 — View Grades, spreadsheet view (R2, run R071)

**Page:** Class Menu → View/Manage Class Grades → spreadsheet view.
**Also:** does `T` reach the spreadsheet; do row/column headers read with
each cell (NV3/NV5)? The "Grade Sheet - Class" link text — clear on its own
(NV10)?
**Feedback:** 2026-09-15 — skipped: view removed from the sample (not student-facing — reviewer's scope decision, 03 §1.1).

### W68 — View Printable Assignment at 400 % and 100 % (S13, new view)

**Page:** Class Management → assignment row → View Printable Assignment
(`/Common/ViewAssignmentDetails.aspx`) — the plain HTML rendering of the
nine problems.
**Tell me:** the same five things as Part I (LV2 at 400 %, LV7 focus ring,
LV9 — the same figure images as Take Assignment blur here too?, LV4/LV5
eyedropper on anything coloured, LV6 hover/focus content). The assistant
runs the axe sweep and the probe on it first.
**Feedback:** 2026-09-15 — "nothing cut off, figures are still blurry, same
contrast issues as before with the red values, no hover or focus issues" →
LV2, LV6, LV7 pass; LV9 fail (V-F24); LV4 fail (V-F23). **Open: LV5** —
the header links / any control at 3:1 ("same as the other pages" is enough).

### W69 — View Printable Assignment with NVDA (S13, new view)

**Page:** as W68, NVDA on.
**Tell me:** the same nine things as Part J — in particular NV2 (does
this page have headings per problem, like the Solutions page?), NV4 (the
figures — alt or silent?), NV5 (reading order of statement, math, parts).
**Why it matters:** if a screen-reader user can *read* every problem here,
this page is the alternate route for T1's reading step; answering still
needs Take Assignment.
**Feedback:** _(pending)_

## 2026-09-17 — Session 4 opening (assistant, no reviewer yet)

**Done without you:** the last no-color cell the instrument could reach —
the **sign-in page** (run R120, measured in the signed-out window on port
9223, so your session was never touched). That completes the probe's share
of no-color and motor: every page now has NC2 measured and MO9/MO10
measured. Everything still blank in those two modalities needs your eyes
(NC1, NC3) or your hands (MO1-MO8, MO11).

**Before anything else:** the debug-profile Chrome on port 9222 is sitting
on `login.theexpertta.com` — the shared session has expired again. **Sign in
there** (the assistant never authenticates); until then no page behind the
login can be measured or walked.

### W70 — Is the password-reset link recognisable as a link? (sign-in page; feeds 1.4.1 with W41)

**Page:** the Expert TA **sign-in page**,
`https://login.theexpertta.com/Login.aspx` — the page you land on when
signed out. No zoom, no screen reader, normal window.
**Look at:** the sentence under the User Name / Password fields that offers
a password reset — the "(e-mail reset)" link inside it.
**What the instrument says:** that link is **1.7:1 against the text around
it** — below the 3:1 the technique needs — and carries no underline, border
or weight of its own until you hover it (underline) or focus it (outline).
The other five colour-only links on the page measure at or above 3:1 and do
pass.
**Tell me:** with the mouse away from it, can you tell that "(e-mail reset)"
is a link rather than ordinary text? "Confirmed" = you cannot; or name what
marks it that I have not measured.
**Why it matters:** this and W41 are the only open 1.4.1 evidence; both
answered, `05` 1.4.1 can be decided and the review's last integrity flag
clears. **KEY STEP**
**Feedback:** 2026-09-21 — two parts. (1) The reviewer followed the link
through to the **reset page** and reported the form there (unlabelled
user-name field → **V-F30**; page sampled as **S14**). (2) On the link itself:
*"e-mail reset appears as a link to NVDA and is tabbable."* That settles the
**programmatic** side — role exposed, keyboard reachable, so 4.1.2 and 2.1.1
are fine for this control → recorded on R120.
**Still open, and it is a different question:** 1.4.1 asks about the
**visual** presentation for someone who cannot use colour to tell text apart —
a sighted user with colour blindness, no screen reader. Reframed as **W73**
with the grayscale evidence attached, because the answer is no longer obvious
in the instrument's favour: in the achromatopsia render the link *is* slightly
lighter than the bold text it sits in. → W73.

### W71 — The silent 8th Tab stop on every page (confirms V-F29's severity)

**Page:** **Class Management in standard mode** —
`https://dei56mo.theexpertta.com/common/default.aspx`, the page you land on
after signing in (the button top-right reads "Accessibility Page"). NVDA on,
normal window, no zoom.
**Do:** click once in the address bar, then press **Tab eight times** to walk
into the page from the top. Stops 1–7 are: the hidden instruction text,
theExpertTA.com, My Account, Log Out, Class Management, Instructor, Help.
**Look at stop 8** — the focus ring lands on the Expert TA **logo** at the
top-left.
**What the instrument says:** that logo is a link that still takes Tab focus,
but it sits inside `aria-hidden="true"`, so the screen reader should be given
nothing at all there — not even the image's alt text, "The Expert TA".
Measured 2026-09-17 with real key presses (R001 O11); it is on every
signed-in page, and it is why your NVDA links list came back empty on this
page (R015 O13).
**Tell me:** (a) at stop 8, what does NVDA say — nothing, or something?
(b) Severity: I have it at **Minor** — one silent stop, early in the order,
and pressing Enter there leaves the app for the vendor's marketing site. Does
that match how disruptive it feels, or is it worse than Minor?
**Why it matters:** this is the last open item from the S1 and S3 sweep
triage; your answer settles V-F29's rating. Everything else those two sweeps
reported is now either a confirmed finding or dismissed with a reason.
**Feedback:** 2026-09-21 — **"The ExperTa graphic visited link"**. Not silent:
NVDA gives name, role and visited state. The prediction behind the finding was
wrong — `aria-hidden` did not suppress the announcement in NVDA + Chrome — so
**V-F29 is withdrawn** and kept only as an advisory (the markup is still a
defect, with no demonstrated effect on this AT). Your answer also overturned
this run's **NV10**: it had been marked n/a because the links-list dialog came
back empty, and the logo you just heard announced as a *link* shows that
dialog was not listing the page's links → reopened as W72. → R015 O14, O15.

### W72 — Do the links on Class Management announce a clear purpose? (reopens NV10 on R015)

**Page:** **Class Management in standard mode** —
`https://dei56mo.theexpertta.com/common/default.aspx`, NVDA on.
**Why this is being asked again:** on 2026-09-14 this row was closed as "not
applicable" because NVDA's links-list dialog (NVDA+F7 → Links) came back
**empty** — read at the time as "this page exposes no links". W71 disproved
that: the logo you heard is announced as a *link*, and there are six more real
links at Tab stops 2–7 (theExpertTA.com, My Account, Log Out, Class
Management, Instructor, Help) that are not hidden from the AT at all. So the
dialog was not showing the page's links, and nothing can be concluded from its
emptiness.
**Do:** Tab from the top through those first eight stops and listen to each.
**Tell me:** does any of them announce a purpose you could not act on — a bare
"click here", "more", "link", or two that sound identical but go to different
places? A plain "they all named themselves fine" closes the row.
**One more while you are there (MO11, found stranded by the 2026-09-21
audit):** on stop 1, the hidden instruction div — **press Enter**. R015 O9
routed this question to the motor run R022 on 2026-09-14 and it was never
picked up: does Enter on that jump point do anything, and if so what? It is
the only routed item in the review that never landed.
**Why it matters:** NV10 is the 2.4.4 evidence for this page, and it is
currently resting on nothing. This is the process's own rule in action —
confirm control names **on focus**, never from an AT's elements list.
**Feedback:** _(pending)_

### W73 — Can you see that "(e-mail reset)" is a link, without colour? (decides 1.4.1 with W41)

**Page:** the **sign-in page**, `https://login.theexpertta.com/Login.aspx`.
Screen reader off for this one — it is a pure looking question.
**Look at:** the line **"Trouble Logging in? (e-mail reset)"**, under the User
Name box. "(e-mail reset)" is the link.
**What the instrument says:** it is **1.7:1** against the bold text beside it
— under the 3:1 that the accepted technique (G183) needs — and it gains no
underline until you hover or focus it. But the grayscale capture
(`evidence/runs/R120/R120-grayscale.png`, attached) is not clear-cut: with all
colour removed, "(e-mail reset)" still reads as slightly **lighter** than
"Trouble Logging in?" next to it. Note the contrast with the other links on
the same page — "contact us", "here", "View detailed information" all sit in
*normal-weight* sentences and are **bold**, so they carry a weight cue that
survives colour blindness. "(e-mail reset)" does not: the text it sits in is
bold too.
**Tell me:** looking at that line — ideally with a grayscale filter on, or at
the attached capture — would you know "(e-mail reset)" is clickable? Either
"confirmed, it just looks like part of the sentence" (1.4.1 fail) or "no, the
lightness is enough" (exception — and I will record your call over the
measurement).
**Why it matters:** with W41 this is the last 1.4.1 evidence; both answered,
`05` 1.4.1 can be decided and the review's only integrity flag clears.
**KEY STEP**
**Feedback:** _(pending)_

### W74 — View Grade Report: it is not empty, and two colours share one symbol (NC1, NC3 — decides the last 302.3 rows)

**Page:** Class Management → assignment row → "View Grade Report (shows your
detailed work)". Grayscale filter on.
**Why you are being asked again:** you told me on the 21st there are no grades
to view, and I recorded that as a coverage limitation. Measuring the page for
the colour scan contradicts part of it: **the page renders 1120 text elements
in 11 colours**, and the colour-coding W32 asked about is all there. So
whatever is missing from the demo account, this page is not blank and its
colour use *is* testable. I would rather re-ask than leave a limitation on the
record that the measurement disputes.
**Two specific things, both already located:**
- **Orange and purple both sit on "%" — 66 elements each.** Two different
  colours doing something to the same symbol, in equal numbers, looks like two
  meanings told apart by colour alone. What are they? If nothing in the words
  distinguishes them, that is a clean 1.4.1 failure and the strongest one on
  the page.
- **Red on 48 elements, and the sample text is a sentence** — *"Late
  submissions were made on this part"*. If lateness is stated in words like
  that, then it is **not** colour-only, and that part of NC1 **passes** — the
  opposite of what the 2026-09-10 note assumed. Worth confirming, because it
  is the one place the page may do better than predicted.
**Also tell me:** what "no grades to view" meant, so the limitation in `03`
§1.1 and against task T5 can be narrowed to what is actually missing (scores?
feedback text? a second submission?) rather than reading as "the page is
blank", which it is not.
**Why it matters:** these are the last unanswered no-color rows besides
Accessibility Mode; answering them finishes 302.3.
**Feedback:** 2026-09-21 — *"in GradeSheetGradeReport the colored text fails
contrast in grey, except the dark blue, that passes; it should also be pointed
out that the images used also fail contrast in some ways when in grey; assume
the red and orange fail in all views."* Recorded: **NC1 fail, NC3 fail, Result
Broken** (R100 O6–O8).

The two open questions were settled by measurement rather than sent back to
you a third time:
- **Orange vs purple** — they are two different deductions. Orange is
  *"Deduction for Final Submission"*, purple *"Deductions for Incorrect
  Submissions, Hints and Feedback"*. Next to their labels the words carry
  them; in the summary line `Student Grade = 100 - 100 - 9 = 0%` they do not —
  the first number is orange, the second purple, and **nothing but hue says
  which is which**. No title, no aria-label, no legend. That is the clearest
  colour-only case in the review.
- **Red** — both, and the split matters. Part-level lateness is a **sentence**
  ("Late submissions were made on this part…"), so that much is not
  colour-only and is recorded as a **pass**. But 14 individual submissions are
  marked late by a red date-time only, under the product's own legend **"Red
  submission date times indicate late work."** A legend that names a colour
  does not satisfy 1.4.1 — someone who cannot see red still cannot tell which
  dates it applies to.

**Your "images also fail contrast in grey"** is recorded against **V-F24**: the
figures do not only pixelate at zoom, they lose internal contrast with colour
removed, so detail inside the diagram goes too. **"Assume red and orange fail
in all views"** is applied — it confirms the two views already failed by
measurement (Printable Assignment, Student Practice Area) and adds nothing new,
because Sign in and Password reset carry no red or orange at all.

**The report gains its own recommendation from this.** Two places on the
product already do it right — the problem-navigator **status marks** (a
symbol) and part-level lateness (a **sentence**) — and the dark blue [?] links
are the one colour that survives grayscale. The fix is the product's own
pattern applied to the rest, which is a much easier thing to ask a vendor for
than "improve your colours".

**Still not answered, and it only affects a limitation note:** what "no grades
to view" meant. The page is plainly not blank — 1120 text elements, a real
grade formula, real submission dates. If what is missing is something narrower
(a second attempt? instructor feedback text?), say which, and the limitation in
`03` §1.1 and against **T5** can be narrowed to it instead of reading as
"the page cannot be tested", which the measurement disproves.

## 2026-09-21 — Recording audit: is no-vision really only 2 of 10?

The reviewer asked whether the low no-vision count reflects work that was done
but never written down. **It does not — the count is real** — but the audit
found a different gap. Four passes over every run file of a live view:

1. **Observations classified to a check whose row is blank in the same run:**
   exactly one, `R015 NV10`, which is the row deliberately reopened on
   2026-09-21 (W72). Nothing else is stranded.
2. **Observations classified to a check that has no row in the run they sit
   in** (narration filed under the wrong modality): four, all of them
   *routing* notes, and three of the three routable ones landed — R004's
   LV4/LV9/NC2 → R083 and R109; R017's MO1/MO2/MO5/MO7 → R018 (all answered,
   MO11 partial); R121's LV1 → R123. **One did not:** R015 O9 routed
   "MO11 on R022 to confirm what Enter does on the jump point" and R022's MO11
   is still blank. It needs a keystroke from the reviewer, so it is pending,
   not lost → folded into W72.
3. **Findings whose evidence is a screen-reader claim:** all 19 cite a
   no-vision run (R015, R016, R017, R059, R121) or a sweep/motor run. None
   rests on a low-vision run, so no narration was filed against the wrong run
   and then inherited by a finding.
4. **Walkthrough feedback mentioning NVDA:** every instance is from
   2026-09-10 on S2 and S3, and all of it is present in R016 (14 observations,
   3 rows left) and R017 (24 observations, complete).

**Conclusion:** no-vision is genuinely 2 of 10 resulted because only four
views have ever had a screen reader on them — S1 and S3 fully, S2 three rows
short (W56), S12 partially from the W53 narration (W65), plus S14's single row
from 2026-09-21. **S4, S6, S7, S8 and S13 have never been walked with NVDA at
all**; their runs hold the probe's three measured rows and nothing else.

**The gap the audit did find:** six axe sweeps are still untriaged —
**R003 (S7), R005 (S2), R007 (S4), R008 (S6), R011 (S12), R014 (S8)** — each
with five to seven proposed classifications and both W1 and W3 blank. That is
18 rows, and it is the same state R001 and R004 were in until 2026-09-17.

**They are downstream of the walks, not independent of them.** W3 asks for the
sweep's structure output to be cross-checked against a screen-reader walk, and
four of these six views have no walk to check against; the view-specific
violations need the same walk to confirm. R001 and R004 closed almost for free
once R015 and R017 existed. So the efficient order is **NVDA walks first**
(W56, W57 with W21, W58, W63, W64, W69) — each one closes its view's no-vision
cell *and* unlocks its sweep triage.

## 2026-09-21 — Session 5 plan: finish no-vision (302.1)

**Why this order:** every sweep triage still open is downstream of a walk
(audit above), so each page you do closes its own no-vision cell *and* unlocks
its axe sweep. 62 rows are open; this clears them in nine sittings, smallest
first so the early ones bank quickly.

**The nine standing questions** (Part J preamble has the full wording — this
is the short form). On each page, NVDA on:

| | Ask |
|---|---|
| NV2 | `H` for headings, `D` for landmarks, NVDA+F7 — is there any structural route? |
| NV3 | Tab each control — name, role, state. Name anything silent or wrongly typed. |
| NV4 | `G` for graphics — what does each announce? Any picture carrying information that says nothing? |
| NV5 | Arrow from the top — does the order make sense? |
| NV6 | `F` for form fields — is the visible label what NVDA reads? |
| NV7 | Change something without a reload — announced? Does focus stay put? |
| NV8 | Anything you could only identify by where it sits? |
| NV10 | NVDA+F7 → Links — bare "click here"/"more", or identical texts going to different places? **Confirm on focus too** — the list lies on this product (2026-09-21). |
| NV12 | A required/validated field — clear it and submit. Is the error announced, and does it say which field and what is wrong? "No validated input" → n/a. |

**A "nothing to report" is a complete answer for any row.** Say the row number
and move on; I only need detail where something is wrong.

**Order, with what each one costs and buys:**

| # | Page | Rows | Step | Why here |
|---|---|---|---|---|
| 1 | **Class Management, Accessibility Mode** (`default2.aspx`, button reads "Non-Accessibility Page") | **3** — NV4, NV5, NV12 | W56 | Fifteen minutes' work sets R016's Result and closes the vendor's own accessible page. |
| 2 | **Class Management, standard mode** (`common/default.aspx`) | **1** — NV10, plus the Enter question | W72 | One row. It is the review's only integrity flag and the only routed item that never landed. |
| 3 | **View Grade Report** (assignment row → "View Grade Report") | **9** | W57 + W21 | The page you thought had no data. It is populated, and it is where T5's student half gets its verdict. |
| 4 | **View Assignment Solutions** (assignment row → View Solutions) | **9** | W58 | 14 solution images with no alt, and MathJax — the two things axe cannot see. |
| 5 | **View Printable Assignment** (assignment row → View Printable Assignment) | **9** | W69 | **The highest-stakes page left.** If a screen-reader user can read every problem here, this is T1's conforming alternate for reading. If not, that argument dies. |
| 6 | **Calendar** (top menu → Calendar) | **9** | W64 | Already Broken for colour; does the event bar exist for a screen reader at all? |
| 7 | **Student Practice Area** (paste `…/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373`) | **6** | W65 | Half done from your 2026-09-15 narration; V-F28 (Blocker) came from here. |
| 8 | **Password reset** (`login.theexpertta.com/ResetPassword.aspx`) | **7** | W75 | Signed-out window, **port 9223**. You have already done NV6 here. |
| 9 | **Sign in** (`login.theexpertta.com/Login.aspx`) | **9** | W63 | Same window as 8 — do them together. Includes a wrong-password attempt for NV12. |

**Then, NVDA off and a grayscale filter on** — two looking questions that
decide nothing else is left on 1.4.1: **W41** (the Grade Report and Solutions
title-line links) and **W73** (the sign-in page's "(e-mail reset)").

**After each page** I write the rows, set the Result, roll findings into `05`,
and close that page's axe sweep. Say the page name when you start; skip or
reorder freely.

### W75 — Password reset with NVDA, the remaining seven rows

**Page:** `https://login.theexpertta.com/ResetPassword.aspx`, reached from the
sign-in page's "Trouble Logging in?" link — **signed-out window (port 9223)
only**, never the tab you are signed in on.
**Already answered here (2026-09-21):** NV6 — the user-name field has no
label and tabbing in reads out the whole layout table, which you ruled
"accessible, but not best practice" (V-F30). NV1, NV9 and NV11 are measured.
**Still needed:** NV2, NV3, NV4, NV5, NV7, NV10, NV12 — the standing nine
minus what is done. For **NV12**, submit the form with the field empty (or
with an address that is not an account) and say whether the error is announced
and whether it names the field and the problem.
**Why it matters:** this is the only account-recovery path in the demo, so a
student locked out of the product cannot reach any other view without it.
**Feedback:** _(pending)_

### Close-out for session 3 (assistant)

After each step: the run's rows and observations, Tool/Baseline set to the
instrument used, the Result (or the outstanding row named), findings in
`04` §B, `05` rollup, `03` enclosure if a new state appeared. Then
`validate`, `coverage`, `review_db.py state --log`, and the dashboard §1
should read no-vision 14/14 and low-vision 14/14.
