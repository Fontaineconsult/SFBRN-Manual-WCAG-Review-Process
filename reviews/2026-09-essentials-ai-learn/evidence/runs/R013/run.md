# Test Run R013 — S2

| | |
|---|---|
| **Run ID** | R013 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard (probe measurements kept: MO9, MO10) |
| **Baseline** | B2 |
| **Tester** | Daniel Fontaine (reviewer, physical keyboard, baseline B2) + assistant (automated walk O4–O9); assistant records |
| **Result** | Works |

**Result reasoning.** Keyboard run on My Courses (reviewer with a physical keyboard plus the assistant's dispatched-key walk). Skip link first, ten stops in visual order, visible ring at every stop, tabs switch with Tab + Enter (arrows not implemented — advisory), account menu opens with Enter, arrows move through it, Escape returns focus; no shortcuts, no drag. MO9 re-answered 2026-10-02: the probe's measured fail was the visually-hidden skip link (clip rect(0,0,0,0)), not a pointer target — instrument artefact fixed in view_probe.py 2026-09-30; every visible target is ≥ 24×24 px or spacing-exempt (R013-probe.json).

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | pass | O4 — every interactive element is a Tab stop (10 stops incl. skip link, nav, avatar, both tabs, both card links) — assistant walk, working result |
| MO2 — Every reached element can be operated (activate, select, dismiss) | pass | O11, O10, O6 — every reached control operates from the keyboard: skip link, links, tabs (Enter), avatar menu (Enter + arrows, Escape) — reviewer |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O6, O4 — Escape closes the account menu and returns focus to its button; Tab leaves the page after the last stop |
| MO4 — A visible focus indicator exists at all times | pass | O12, O5 — visible indicator at every stop (assistant screenshots at 100 %, reviewer's 400 % pass; ring question delegated) |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O4 — tab order header → sidebar → main matches the visual and operational order |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | O8 — no single-character shortcuts (measured) |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | O9 — no drag or gesture on the view |
| MO8 — Pointer actions can be cancelled (up-event activation) | pass | O9 — native links/buttons — up-event activation |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O2 re-read 2026-10-02: the only sub-24 px target the probe listed is the sr-only skip link, clipped to nothing until focused and not a pointer target (Notes); all 9 visible targets pass or are spacing-exempt; the reviewer's keyboard walk used the skip link normally |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (7 inline + 5 external scripts scanned) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | pass | O4, O9 — "Skip to main content" is the first Tab stop (target `#main-content` exists) |

**view_probe 2026-09-30:** answered MO9=fail, MO10=n/a by measurement; facts in `R013-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): 1 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): a.sr-only.rounded-md "Skip to main content" 32×16 px next to a.flex.items-center "AI EssentialsLMS"
  - Classified: MO9 / WCAG 2.5.8 / measured → fail
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no devicemotion/deviceorientation use in scripts (7 inline + 5 external scripts scanned)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a
- O4 [new] (state: signed-in window 1280×1000, page reloaded, real Tab key events via CDP with focus emulation): Tab path: 1 "Skip to main content" (first stop) → 2 logo link "AI Essentials LMS" → 3 My Courses → 4 My Certificates → 5 My Profile → 6 avatar button "TU" (aria-haspopup=menu, aria-expanded=false) → 7 tab "Classic 1" (selected) → 8 tab "Gamified 1" → 9 course-card title link → 10 "Start course" link → browser chrome. Ten stops, visual order (header → sidebar → main). Both tabs are separate Tab stops (no roving tabindex).
- O5 [new] (state: same walk, screenshots R013-tab01.png … R013-tab10.png): Visible focus indicator at every stop: a white + lilac double ring on the skip link, a lilac outline (rgb(201,168,236) ≈ 1.8 px) on every other control. Presence observed by automation; reviewer confirms on a physical keyboard.
- O6 [new] (state: avatar button focused, keys dispatched): **Space** opens the account menu (role=menu: "Profile & sessions", "Sign out"; aria-expanded → true; screenshot R013-account-menu-open.png). **Escape** closes it and focus returns to the avatar button. **Enter** and **ArrowDown** did *not* open it in two attempts, and ArrowDown inside the open menu did not move focus to the first item — either an automation limit (Radix menus listen for pointer/keydown combinations the synthetic events may not satisfy) or a real keyboard gap. Reviewer decides (MO2).
- O7 [new] (state: Course-experience tablist, keys dispatched): With focus on the selected tab "Classic", **ArrowRight/ArrowLeft changed nothing** (selection and focus unchanged). With focus on "Gamified", **Enter did not select it** (aria-selected stayed on Classic; no role=tabpanel exists on the page). On 2026-09-30 a programmatic `.click()` did switch the tabs, so the control works by pointer. Not concluded from automation — **KEY question for the reviewer: can the Classic/Gamified switch be operated from the keyboard at all (Enter, Space, arrows)?**
- O8 [new] (state: focus on body, letters s l h / ? g c dispatched): No single-character shortcut: URL, text length and DOM unchanged.
- O9 [new] (state: inspection): Controls are native links/buttons (up-event activation); nothing draggable; no gesture. A skip link is the first Tab stop and targets `#main-content`.
- O10 [clarified] (reviewer, physical keyboard, 2026-10-02): "Classic/Gamified respond to Tab and Enter, but not arrows" — the course-experience tabs ARE keyboard-operable: Tab reaches each tab, Enter selects it. Arrow-key movement (the ARIA tabs pattern) is not implemented — not a WCAG requirement since Tab+Enter works; noted as advisory. Resolves O7's open question (no 2.1.1 failure).
- O11 [classified] (reviewer, physical keyboard, 2026-10-02): Enter opens the avatar menu and the arrows move through its items (the automated Enter/ArrowDown failure in O6 was an automation limit); Escape closes it and returns focus (O6). Tabs switch with Enter (O10).
- O12 [classified] (reviewer, 2026-10-02): Reviewer delegated the focus-ring question ("just pass it"); the automated walk showed a visible ring at every one of the ten stops (O5, screenshots) and the reviewer's zoom pass reported nothing lost.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (keyboard, Chrome automation, signed-in debug profile).** Real key events via CDP with focus emulation (same method as S1). Left for the reviewer: **MO2** — (a) does Enter open the avatar menu and do the arrow keys move through it, (b) can the Classic/Gamified tabs be switched from the keyboard — the automated Enter and arrows did nothing, which would be a 2.1.1 failure if a physical keyboard confirms it; **MO4** — presence observed at every stop (O-ring), reviewer confirms. Evidence: `R013-tab01.png`…`R013-tab10.png`, `R013-account-menu-open.png`.

**Assistant, 2026-09-30 (probe caveat).** The MO9 measured fail names the "Skip to main content" link, which is a visually-hidden skip link (`sr-only`, shown only while focused). While hidden it is not a pointer target, so 2.5.8 does not apply to it in that state; while focused it is a keyboard stop. The probe measured it because its visibility test did not exclude clipped/off-screen elements (fixed in `view_probe.py` the same day). Reviewer decides when closing this run: expect n/a or pass unless the focused link itself is under 24×24 px and clashes.

## Evidence files in this folder

- (screenshots/exports named R013-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
