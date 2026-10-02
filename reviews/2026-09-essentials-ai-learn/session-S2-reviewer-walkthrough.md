# Reviewer walkthrough — S2 My Courses (`https://learn.essentials-ai.com/learning`)

Generated 2026-10-02 from `review.py gaps --view S2` after the automated work
(axe R008, probe R009–R015, assistant keyboard walk, contrast sampling, tree
recon). Work top to bottom and narrate freely; the assistant records feedback
in place and writes it into the runs, findings and rollup as it lands.

**Where this page already stands.** 38 rows were open; **19 are left**.
Answered by measurement and inspection (basis in each run): title, language,
no media/speech/motion, reflow, text spacing, orientation, no animation,
target size, every text's contrast (the gradient card measured on rendered
pixels — all pass), no hover content, no images of text, tab order (skip link
→ logo → three sidebar links → avatar → two tabs → two card links), focus
ring presence, skip link first, no shortcuts, Escape closes the account menu
and returns focus, no inputs so no labels/errors, no help offered, no timer,
reachable several ways. Sweep: no violations; its one contrast warning is
settled.

**Two things the automation could not settle — both KEY STEPS:**

- My synthetic **Enter** and **arrow keys did nothing on the Classic /
  Gamified tabs**, and Enter did not open the avatar menu (Space did). A
  pointer switches the tabs fine. If a physical keyboard cannot switch the
  tabs, that is a 2.1.1 failure on the page's only control that changes
  content.
- The avatar button's only accessible name is **"TU"** (the initials). NVDA
  will say something like "TU button menu" — can a user tell it is the
  account menu?

**Window.** The signed-in debug window (port 9222) is on My Courses, or use
your everyday Chrome signed in as the test learner. Close the assistant
panel before the NVDA steps.

---

## Part A — NVDA, no-vision (run R009) — My Courses [S2]

### W1 — Title, landmarks, headings (NV2; settles the sweep's W3)
**Do:** Load My Courses. `Insert+T`. `D` to cycle landmarks (NVDA), `Insert+F7`
→ Headings.
**Tell me:** the title; the landmarks found (tree shows banner,
complementary, navigation "Main", main); the headings (expected h1 "My
Courses", h2 "AI Foundations - Sonoma State University").
**Feedback:** 2026-10-02 — done: title, landmarks and headings good → NV2 pass; sweep W3 pass.

### W2 — Every control on focus (NV3) — KEY STEP for the avatar
**Do:** `Tab` through all ten stops; copy the speech viewer.
**Tell me:** what each announces, especially (a) the avatar button — does
it say anything beyond "TU"? (b) the two tabs — "tab selected 1 of 2"? (c)
the course title link and "Start course" (two links to the same place).
**Feedback:** 2026-10-02 — done: all stops reachable, role and value announced well; avatar name "TU" → V-F3 (Minor, 2.4.6) → NV3 partial.

### W3 — Switch the course experience with the keyboard (NV3 state, NV7, CO8) — KEY STEP
**Do:** `Tab` to "Gamified", press `Enter`; if nothing, `Space`; if nothing,
`Right arrow`. Then back to Classic the same way.
**Tell me:** which key (if any) switches the tab; what NVDA announces when
it switches; whether focus stays on the tab; whether the page content
changes under you unexpectedly. **Leave Classic selected when done.**
Why it matters: a pointer switches it; my automated keys did not. This is
the page's only content-changing control — 2.1.1 / 4.1.2 / 4.1.3 / 3.2.2.
**Feedback:** 2026-10-02 — done: Tab + Enter switch the tabs (arrows don't — advisory); "Selected" announced → NV7, CO8 pass.

### W4 — Open the account menu with the keyboard (NV3, NV7) — KEY STEP
**Do:** `Tab` to the avatar, press `Enter`; if nothing, `Space`. Then
`Down arrow` twice, then `Escape`.
**Tell me:** which key opens it; what is announced on opening (menu, user
name/e-mail, items "Profile & sessions" and "Sign out"); whether the arrows
move through the items; whether Escape closes it and returns you to the
avatar.
**Feedback:** 2026-10-02 — done: Enter opens the menu, arrows move as expected, Escape returns (automation) → MO2 pass.

### W5 — Reading order, images, links (NV4, NV5, NV8, NV10)
**Do:** `Ctrl+Home`, `Down arrow` to the bottom. `Insert+F7` → Links.
**Tell me:** the order (sidebar first, then header avatar, then main?); how
the logo announces (alt "AI Essentials logo" inside the link); whether the
course thumbnail is silent (decorative); the links list — are "AI
Foundations - Sonoma State University" and "Start course" both clear, and
do you mind two links to the same course?
**Feedback:** 2026-10-02 — done: order correct, logo announced, thumbnail silent, nothing position-only → NV4, NV5, NV8, NV10 pass.

### W6 — Forms and errors (NV6, NV12)
No form on this page. Say "none" and I write n/a.
**Feedback:** 2026-10-02 — n/a written (no form).

## Part B — Zoom, low-vision (run R010) — My Courses [S2]

### W7 — 400 % in a 1280 px window (LV2, LV7)
**Do:** `Ctrl+plus` to 400 %. `Tab` through the stops. Open the avatar menu
(Space) at that zoom.
**Tell me:** anything clipped, overlapped, lost (the sidebar collapses to a
drawer at narrow widths — does the "Hide/show" control appear and work?);
focus ring visible and unobscured at every stop; the open menu fully
visible.
**Feedback:** 2026-10-02 — done: "no clips, site is fully responsive" → LV2, LV7 pass.

### W8 — Component contrast (LV5)
**Do:** At 100 %, eyedropper: the lilac focus ring (≈ 2.1:1 on white — AA
needs only visibility, 3:1 is the AAA 2.4.13 figure); the tab strip border
and the difference between the selected (bold dark) and unselected (grey)
tab; the "Start course" button edge on the card.
**Tell me:** your 1.4.11 call on each. Evidence: `R010-mycourses-1280.png`,
`R010-focus-nav.png`.
**Feedback:** 2026-10-02 — ring eyedropper not reproducible by the reviewer, delegated ("just pass it"); other components pass → LV5 pass (delegation recorded, R010 O11).

## Part C — Grayscale, no-color (run R015) — My Courses [S2]

### W9 — OS grayscale (NC1, NC3)
**Do:** `Win+Ctrl+C`. Look at the current sidebar item, the selected tab,
and the Start course button.
**Tell me:** can you tell which sidebar item is current and which tab is
selected without colour (pill + icon; bold vs grey)? Everything operable?
**Feedback:** 2026-10-02 — done: "yes with grayscale" → NC1, NC3 pass.

## Part D — Physical keyboard (run R013) — My Courses [S2]

### W10 — Focus ring and operation (MO4, MO2) — KEY STEP (same question as W3/W4)
**Do:** Pointer aside. Reload, `Tab` through all stops; `Enter` on the skip
link (does focus land in main?); `Enter`/`Space`/arrows on the tabs; `Enter`
then `Space` on the avatar; `Enter` on "Start course" and `Alt+Left` back.
**Tell me:** ring visible at every stop (my screenshots `R013-tab01…10.png`
say yes at 100 %); which keys operate the tabs and the menu; skip link
works.
**Feedback:** 2026-10-02 — done: tabs via Enter, menu via Enter + arrows, ring visible → MO2, MO4 pass.

## Part E — Cognition (run R014) — My Courses [S2]

### W11 — Consistency and context (CO1, CO8)
**Tell me:** is the shell (sidebar, header, avatar) identical on My
Certificates and My Profile; does switching Classic/Gamified change the
page in an expected way only (same page, same place)?
**Feedback:** 2026-10-02 — done: "shell is consistent"; tab switch stays in place → CO1, CO8 pass.

## Part F — Sweep (run R008) — My Courses [S2]

### W12 — W3
Closes from W1's landmark/heading answer. W1 and W2 are already passed
(no violations; the contrast warning measured on rendered pixels).
**Feedback:** 2026-10-02 — W3 pass from W1; R008 complete.

---

## Close-out (assistant)

**2026-10-02:** every Feedback line filled. R008 closed Works; R009 Works with issues (V-F3); R010, R013, R014, R015 Works. `close-page S2` next.

### Original plan

1. Every Feedback line filled or skipped with a reason.
2. Write-back: R009 / R010 / R013 / R014 / R015 rows and observations →
   `close-run` each → R008 W3 → findings into `04` §B (View S2) if W3/W4
   fail or the avatar name is ruled a defect → rollup in `05` → 03 §2.6
   recon resolved (tablist semantics, Gamified toggle).
3. `review.py close-page 2026-09-essentials-ai-learn S2`, `validate`,
   regenerate both reports, `next`.
