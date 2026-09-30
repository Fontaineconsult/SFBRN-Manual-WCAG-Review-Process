# Test Run R013 — S2

| | |
|---|---|
| **Run ID** | R013 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — MO1, MO2, MO3, MO4, MO5, MO6, MO7, MO8, MO11 need the reviewer (keyboard, B2); measured fail on MO9 awaits confirmation |

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
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | fail | O2 — 1 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): a.sr-only.rounded-md "Skip to main content" 32×16 px next to a.flex.items-center "AI EssentialsLMS" |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (7 inline + 5 external scripts scanned) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | | |

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

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30 (probe caveat).** The MO9 measured fail names the "Skip to main content" link, which is a visually-hidden skip link (`sr-only`, shown only while focused). While hidden it is not a pointer target, so 2.5.8 does not apply to it in that state; while focused it is a keyboard stop. The probe measured it because its visibility test did not exclude clipped/off-screen elements (fixed in `view_probe.py` the same day). Reviewer decides when closing this run: expect n/a or pass unless the focused link itself is under 24×24 px and clashes.

## Evidence files in this folder

- (screenshots/exports named R013-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
