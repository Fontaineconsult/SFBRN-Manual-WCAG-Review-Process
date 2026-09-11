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
**Feedback:** _(pending)_

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
**Feedback:** _(pending)_

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
**Feedback:** _(pending)_

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
**Feedback:** _(pending)_

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
**Feedback:** _(pending)_

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
**Feedback:** _(pending)_

### W31 — Text spacing and orientation (LV3, LV8)

**Do:** Apply a text-spacing bookmarklet/stylesheet (line-height 1.5, letter
0.12 em, word 0.16 em, paragraph 2 em) on Take Assignment; then rotate /
resize to a portrait-shaped window.
**Tell me:** Any clipped or overlapping text (MathJax, keypad buttons, the
problem navigator), and whether portrait works.
**Feedback:** _(pending)_

---

## Part G — No-color pass (grayscale)

Runs:
```
python scripts/review.py log-test the-expert-ta --view S3 --modality no-color --tool grayscale --task T2 --url "UI: Class Management → assignment row → Take Assignment"
python scripts/review.py log-test the-expert-ta --view S4 --modality no-color --tool grayscale --task T5 --url https://dei56mo.theexpertta.com/Common/GradeSheetGradeReport.aspx?z=1&eid=3373&aid=17547
```
Windows Settings → Accessibility → Color filters → Grayscale.

### W32 — Grayscale read of the assignment and the grade report (NC1, NC2, NC3)

**Do:** In grayscale: on Take Assignment, can you still tell the randomized
variable values (red) from the rest of the statement, the "detailed view"
link from text, and the problem status symbols (☑ ☒ ☐) apart? On the grade
report: is a late submission identifiable other than by red date text? Are
the blue **[?]** links distinguishable?
**Tell me:** Each yes/no, with what else (bold, symbol, wording) carries the
meaning if colour does not.
**Feedback:** _(pending)_

---

## Part H — No-hearing / no-speech (confirm N/A)

### W33 — Any audio or voice features in the sample? (NH1–NH4, NS1)

**Do:** Across the views used above, note any video, audio, or voice-input
feature (none was seen in exploration; the vendor's video library lives on
the marketing site).
**Tell me:** "None" — or where you found one. The assistant then logs
no-hearing and no-speech runs as **N/A** for the sampled views, which counts
as coverage.
**Feedback:** _(pending)_

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
