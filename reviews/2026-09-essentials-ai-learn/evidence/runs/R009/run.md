# Test Run R009 — S2

| | |
|---|---|
| **Run ID** | R009 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda (probe measurements kept: NV1, NV9, NV11) |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA 2024.1, baseline B5); assistant records |
| **Result** | Works with issues |

**Result reasoning.** NVDA 2024.1 walk of My Courses (reviewer, baseline B5; probe rows for title, language and media kept). Title, landmarks, headings, reading order, logo alt, link names, tab selected-state announcements and the account menu all pass. One Minor defect: the account-menu button is named only with the user's initials ("TU") — finding V-F3 (2.4.6).

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "My Courses · AI Readiness OS" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | pass | O8 — landmarks and a hierarchical heading outline exist and support navigation — reviewer, NVDA 2024.1 |
| NV3 — Every control announces an accurate name, role, and value/state | partial | O9, O10, O11, O6 — every control announces role and state correctly (tabs "selected", menu button "collapsed"), and every name is accurate except the avatar's ("TU") — Minor finding V-F3 |
| NV4 — Images announce appropriate alternatives; decorative images are silent | pass | O12 — logo announces "AI Essentials logo"; the decorative thumbnail is silent — reviewer, NVDA 2024.1 |
| NV5 — Reading order matches the meaning of the visual order | pass | O12 — arrow reading order matches the visual order — reviewer, NVDA 2024.1 |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | n/a | O5 — no form field on the view |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | pass | O10, O11 — tab activation announces "Selected" and the menu's opening/items are announced, without moving focus unexpectedly — reviewer, NVDA 2024.1 |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O13 — nothing conveyed by position or shape alone — reviewer |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | pass | O9 — every link's text states its target (sidebar links, course title, "Start course") — reviewer, NVDA 2024.1 |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | O5 — no validated input on the view |

**view_probe 2026-09-30:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R009-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): document.title = "My Courses · AI Readiness OS" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass
- O5 [new] (state: Accessibility.getFullAXTree, signed-in window — recon for the NVDA walk, not outcomes): Tree: link "Skip to main content" → complementary (sidebar: link "AI Essentials logo AI Essentials LMS", navigation "Main" with list of 3 links, footer paragraphs "Test User" / "Learner") → banner (button **"TU"** — the avatar's only name is the initials; aria-haspopup=menu) → main: "Learning", heading 1 "My Courses", intro, **tablist "Course experience"** with tabs "Classic 1" (selected) / "Gamified 1", "Two ways through…", card: "Start here", link + heading 2 "AI Foundations - Sonoma State University", intro, link "Start course"; thumbnail image alt="" (decorative); one empty `alert` live region. No unnamed control. Things to listen for: what the avatar button announces ("TU button menu"? — a user cannot tell it is the account menu), how the tabs announce selected state and whether switching announces anything (no tabpanel role exists), the duplicated link+heading on the card, "Start course" (two links to the same course).
- O6 [finding:V-F3] (reviewer, NVDA 2024.1, 2026-10-02, Tab to the avatar): Announced: "banner landmark, TU, menu button, collapsed, subMenu" — role (menu button), state (collapsed) and the popup are exposed; the **name is the initials "TU"** only. Reviewer's ruling 2026-10-02: **Minor finding** — "the role is not meaningful": a user cannot tell from the name that this is the account menu. → V-F3 (2.4.6).
- O7 [new] (reviewer, 2026-10-02, tabs by keyboard): Tabs switch with Enter (not arrows) — see R013 O10. Pending: what NVDA announces on the switch (NV7) and the tabs' selected state on focus (NV3).
- O8 [classified] (reviewer, NVDA 2024.1, 2026-10-02): "Title, landmarks and headings are good" — title, the banner/complementary/navigation/main landmarks and the h1 "My Courses" / h2 course title are found and navigable, matching the tree (O5) and axe (R008).
- O9 [classified] (reviewer, NVDA 2024.1, 2026-10-02, Tab through all stops): "All other tab stops are reachable and announce role and value well" — sidebar links, both tabs (with selected state), course title link and "Start course" announce correctly; the only naming defect is the avatar (O6 → V-F3).
- O10 [classified] (reviewer, NVDA 2024.1, 2026-10-02, Enter on a tab): "Selected" is announced when a tab is activated with Enter — the state change is spoken; focus stays on the tab; the page does not reload (Classic left selected).
- O11 [classified] (reviewer, NVDA 2024.1, 2026-10-02, avatar menu): Enter opens the menu; the arrow keys move through "Profile & sessions" and "Sign out" as expected.
- O12 [classified] (reviewer, NVDA 2024.1, 2026-10-02, arrow read top to bottom): "Top to bottom tab and arrow order is correct"; the logo announces "AI Essentials logo"; the course thumbnail (alt="") is not announced.
- O13 [classified] (reviewer, 2026-10-02): "Nothing" is conveyed only by position, shape or size.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02.** No outcome written — NVDA decides every row. Recon above.

## Evidence files in this folder

- (screenshots/exports named R009-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
