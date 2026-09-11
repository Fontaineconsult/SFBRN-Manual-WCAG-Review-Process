# Test Run R018 — S3

| | |
|---|---|
| **Run ID** | R018 |
| **Date/time** | 2026-09-10 16:38 |
| **View / sample** | S3 |
| **Page URL / location** | UI: Class Management → assignment row → Take Assignment |
| **Task / process** | T2 |
| **Modality** | motor |
| **Tool** | keyboard |
| **Baseline** | B2 |
| **Tester** | Daniel Fontaine (reviewer, keyboard only, NVDA off); assistant records |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | pass | O1 — problem links, jump points, keypad buttons, radios, Submit/Hint/Feedback/Give up, drag-and-drop form, FBD controls all reachable; palette-only symbols enterable by typing (O5) |
| MO2 — Every reached element can be operated (activate, select, dismiss) | pass | O1, O5; operation of each widget type established under R017 with the keyboard |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O3 — no traps found |
| MO4 — A visible focus indicator exists at all times | pass | O2 — "no hidden stops": focus visible on every stop, including the jump points |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O1 — ~20 Tab stops from the top to the first answer field; order follows the page; no unexpected jumps |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | no single-character shortcuts; the vendor's chords are Ctrl+Shift+digit |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | pass | drag-and-drop ranking has the alternative form (R017 O18/O19); FBD via force table (R017 O20) |
| MO8 — Pointer actions can be cancelled (up-event activation) | | pending — quick mouse check on a keypad button and a problem link (press, move off, release) |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | | pending — assistant measurement over CDP once the debug window is back (keypad buttons, ⊞ expand icons, ✖ delete) |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | no motion-actuated function |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | partial | O4 — the first Tab stop is a jump point: not a skip, but Enter opens a hidden accessibility menu whose links move around the page (R017 O2); several stops do the same thing. Mechanism exists; it is not a skip link and is not self-explanatory |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [clarified] (state: Take Assignment reloaded, NVDA off, keyboard only): about **20 Tab stops** from the top of the page to the first answer field.
  - Classified: MO1, MO5 / pass (burden noted for the report; not a failure)
- O2 [clarified] (state: as O1): no hidden stops — a visible focus indicator on every stop, including the vendor's jump points.
  - Classified: MO4 / pass (resolves the 2.4.7 question left open in V-F8)
- O3 [clarified] (state: as O1): no focus traps; nothing jumped anywhere unexpected.
  - Classified: MO3, MO5 / pass
- O4 [clarified] (state: as O1): "the tab stops are not actually skips" — each jump point is an opportunity to press Enter and open a hidden accessibility menu; there are multiple such stops that do the same thing.
  - Classified: MO11 / partial → supports V-F8 (mechanism exists, is not a skip link, and its purpose is not evident from the stop itself)
- O5 [clarified] (state: Problem 2, symbol palette not in the Tab order): θ, β and √ entered **without the mouse** — success.
  - Classified: MO1, MO2 / pass (closes R017 O12's open question)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R018-<what>.png)

## Findings raised from this run

- none new; O4 cited by V-F8; O2 closes V-F8's focus-visibility question
