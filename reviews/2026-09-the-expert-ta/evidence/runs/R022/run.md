# Test Run R022 — S1

| | |
|---|---|
| **Run ID** | R022 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
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
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | fail | O2 — 2 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): img.dxGridView_gvDetailCollapsedButton "" 9×10 px next to div#divActionMenu17547.actionMenu "⋮"; div#divActionMenu17547.actionMenu "⋮" 16×16 px next to img.dxGridView_gvDetailCollapsedButton "" Reviewer 2026-09-14: confirmed — "no other way found" on this page for the ⋮ menu / expand glyph → finding V-F21. |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (57 inline + 51 external scripts scanned, 1 unreadable) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | fail | O4 — reviewer 2026-09-21: the first Tab stop **is** reachable and Enter **does** respond, but all it does is swap the instruction text for a **"no shortcuts"** message; no focus move, no menu, no skip. A mechanism that announces it has nothing to offer is not a bypass → supports V-F8 and 2.4.1 |

**view_probe 2026-09-11:** answered MO9=fail, MO10=n/a by measurement; facts in `R022-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 2 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): img.dxGridView_gvDetailCollapsedButton "" 9×10 px next to div#divActionMenu17547.actionMenu "⋮"; div#divActionMenu17547.actionMenu "⋮" 16×16 px next to img.dxGridView_gvDetailCollapsedButton ""
  - Classified: MO9 / WCAG 2.5.8 / measured → fail → reviewer 2026-09-14: confirmed → V-F21
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no devicemotion/deviceorientation use in scripts (57 inline + 51 external scripts scanned, 1 unreadable)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a

- O4 [clarified] (state: Class Management standard mode, first Tab stop — the visually hidden accessibility-instruction div — Enter pressed, reviewer 2026-09-21 — step W72): **"When pressing enter, the accessibility instructions change to a 'no shortcuts' text, no other actions."** The jump point is keyboard-operable, so it is not an inert control; what it is not is a bypass. On Take Assignment the same pattern mounts a shortcuts menu after Enter (R017, V-F8); on this page it answers that there are none, and focus does not move. This closes the question R015 O9 routed here on 2026-09-14 — the only routed item in the review that had never landed (found by the 2026-09-21 recording audit).
  - Classified: MO11 / WCAG 2.4.1 / fail — folded into **V-F8**; no new finding

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R022-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
