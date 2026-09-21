# Test Run R126 — S14

| | |
|---|---|
| **Run ID** | R126 |
| **Date/time** | 2026-09-21 13:30 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — MO1, MO2, MO3, MO4, MO5, MO6, MO7, MO8, MO11 need the reviewer (keyboard, B2) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | | |
| MO2 — Every reached element can be operated (activate, select, dismiss) | | |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | | |
| MO4 — A visible focus indicator exists at all times | | |
| MO5 — Focus order follows the meaning and operation order of the view | | |
| MO6 — Single-character shortcuts can be switched off or remapped | | |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | | |
| MO8 — Pointer actions can be cancelled (up-event activation) | | |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O2 — 4 visible targets measured; 4 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (2 inline + 7 external scripts scanned) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | | |

**view_probe 2026-09-21:** answered MO9=pass, MO10=n/a by measurement; facts in `R126-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): 4 visible targets measured; 4 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized
  - Classified: MO9 / WCAG 2.5.8 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-21 view_probe): no devicemotion/deviceorientation use in scripts (2 inline + 7 external scripts scanned)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R126-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
