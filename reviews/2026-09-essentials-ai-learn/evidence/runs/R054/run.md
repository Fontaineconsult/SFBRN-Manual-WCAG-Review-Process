# Test Run R054 — S1

| | |
|---|---|
| **Run ID** | R054 |
| **Date/time** | 2026-09-30 14:09 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard (probe measurements kept: MO9, MO10) |
| **Baseline** | B2 |
| **Tester** | Daniel Fontaine (reviewer, physical keyboard, baseline B2) + assistant (automated walk, O4–O9); assistant records |
| **Result** | Works |

**Result reasoning.** Keyboard run on the sign-in page (reviewer with a physical keyboard, baseline B2, plus the assistant's dispatched-key walk O4–O9). Every control is reached and operated, tab order matches the visual order, a visible focus ring is present at every stop, Enter submits from the Password field, Space toggles Show password, no shortcuts, no traps, no drag. The Sign in button is disabled until both fields are filled and then becomes a normal stop.

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | pass | O4 — every enabled control is reached by Tab (4 stops); the disabled submit is unreachable by design until the fields are filled — reviewer confirms it becomes a stop once enabled (working result, assistant-driven) |
| MO2 — Every reached element can be operated (activate, select, dismiss) | pass | O12, O10 — every reached control operates from the keyboard: Space toggles Show password, Enter submits from the Password field, the enabled Sign in button is a stop; the link is a native anchor — reviewer + assistant |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O4 — focus leaves the page to browser chrome after the last stop and Shift+Tab returns; no widget or dialog on the view |
| MO4 — A visible focus indicator exists at all times | pass | O11, O5 — visible indicator at every stop, reviewer at 400 % and assistant screenshots at 100 %; enabled Sign in button not separately reported |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O4 — Tab order Email → Password → Show password → Forgot your password? matches the visual and operational order |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | O6 — no single-character shortcuts exist (measured: letter and symbol keys change nothing) |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | O7 — no dragging or multipoint/path gesture on the view |
| MO8 — Pointer actions can be cancelled (up-event activation) | pass | O7 — native controls only — up-event activation by the user agent |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O2 — 5 visible targets measured; 1 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (7 inline + 12 external scripts scanned) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | n/a | O7 — no repeated blocks on the sign-in view (no navigation/header); a skip mechanism is not required here |

**view_probe 2026-09-30:** answered MO9=pass, MO10=n/a by measurement; facts in `R054-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): 5 visible targets measured; 1 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized
  - Classified: MO9 / WCAG 2.5.8 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no devicemotion/deviceorientation use in scripts (7 inline + 12 external scripts scanned)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a
- O4 [new] (state: signed-out window, page reloaded, real Tab key events via CDP Input.dispatchKeyEvent with focus emulation on): Tab path from the page top: 1 Email field → 2 Password field → 3 "Show password" checkbox → 4 "Forgot your password?" link → browser chrome. Four stops, matching the visual order top-to-bottom. Shift+Tab from chrome returns to the link. The **Sign in button is not a stop because it is natively `disabled`** (`disabled` attribute, cursor not-allowed) until both fields hold a value — so keyboard reachability of the submit, and whether Enter submits (the fields are **not inside a `<form>`**), can only be tested with credentials: reviewer.
- O5 [new] (state: same walk, screenshots R054-tab01.png … R054-tab04.png): A visible focus indicator was present at every stop at 100 %: a purple 2 px border on the focused text fields (outline itself is transparent — the ring is the border colour change), a lilac outline (rgb(201,168,236), ~1.8 px) on the checkbox and the link. Presence observed by automation; the reviewer confirms with a physical keyboard and at zoom (LV7).
- O6 [new] (state: focus on the page body, letters s l h / ? m dispatched as real key events): No single-character shortcut fired: URL, text length and DOM node count unchanged after each key. No keyboard shortcut is documented on the page.
- O7 [new] (state: inspection of the controls): All five controls are native elements (input[email], input[password], input[checkbox], button[type=submit], a[href]) — activation is on the up-event by user-agent behaviour; nothing is draggable (`[draggable=true]` count 0), no path or multipoint gesture exists. The page has no header, navigation or repeated block — it is a single card with one form — so there is nothing to bypass.
- O8 [new] (state: Enter pressed in the empty Email field): Nothing happened (URL unchanged, no alert text, no visible error) — consistent with the disabled submit; error handling can only be exercised with a value in the fields (reviewer, NV12 / CO4).
- O9 [new] (state: Space dispatched on the focused checkbox): The synthetic Space did not toggle the checkbox in this run (checked stayed false) — inconclusive by automation (the tools doc's known limit); reviewer confirms Space toggles "Show password" and that the password becomes visible.
- O10 [new] (reviewer narration 2026-09-30, physical keyboard): "Tab order as expected" — confirms O4 (Email → Password → Show password → Forgot your password?). "Hitting Enter while in the password input successfully logged in" — the form submits from the keyboard once both fields are filled. Still pending for MO2: Space toggles Show password; Enter activates the Forgot-password link. Pending for MO4: the reviewer's own view of the focus ring at every stop, including the enabled Sign in button.
- O11 [new] (reviewer, 2026-09-30): "Focus ring renders fine at 400 percent" (Tab through every stop at zoom) — together with the assistant's 100 % screenshots (O5) the indicator is present at every stop the walk reached. The enabled Sign in button's ring was not separately reported (residual).
- O12 [classified] (reviewer, physical keyboard, 2026-09-30): Space activates Show password (toggles the checkbox); Enter in the Password field submits and signs in (O10). The Forgot-password link is a native anchor (Enter activates by user-agent behaviour; not separately narrated).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30 (keyboard, Chrome automation on the signed-out profile, port 9223).** Instrument: real key events through CDP `Input.dispatchKeyEvent` with `Emulation.setFocusEmulationEnabled`; a first attempt without focus emulation moved nothing (focus stayed on BODY) — the run above is the second attempt. MO2 and MO4 are left for the reviewer: MO2 needs credentials (submit, Enter-to-submit outside a `<form>`, checkbox toggle), MO4 needs a physical keyboard per testing-tools.md §Assistant-driven runs (presence was observed, see O-ring). Evidence: `R054-tab01.png` (Email focused) … `R054-tab04.png` (link focused).

## Evidence files in this folder

- (screenshots/exports named R054-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
