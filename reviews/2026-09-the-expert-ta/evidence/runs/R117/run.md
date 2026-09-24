# Test Run R117 — S13

| | |
|---|---|
| **Run ID** | R117 |
| **Date/time** | 2026-09-15 13:07 |
| **View / sample** | S13 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | probe; keyboard (reviewer, 2026-09-24) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-24, every row answered. Everything is reachable and operable, including the mathematics — which is exposed as buttons (V-F45), so it takes focus even though it cannot say what it is. Only the bypass mechanism fails.

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
| MO1 — Every interactive element can be reached with the keyboard | pass | reviewer 2026-09-24, keyboard pass: **yes** — every interactive element on the view is reachable with the keyboard. Reachability holds even though the page's mathematics is exposed as buttons (V-F45) — they can be tabbed to; what they cannot do is announce what they are |
| MO2 — Every reached element can be operated (activate, select, dismiss) | pass | O— reviewer 2026-09-24: **"m02 all operable"**. This row asks whether every element that **is reached** can be activated, selected or dismissed, and it can. Controls the keyboard cannot reach at all (S1's row menu, the Calendar grid, the Practice Area's selects and checkboxes) are **MO1** failures and are recorded there; repeating them here would count one defect twice |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | Reviewer 2026-09-24, across the whole review: **"I have not encountered any keyboard traps through all reviews, those would stand out."** Ten views walked with keyboard and screen reader over five sessions, including every modal and the widget-heavy Take Assignment. Nothing held focus |
| MO4 — A visible focus indicator exists at all times | pass | O— focus indicator observed by the reviewer on this view during the zoom pass (LV7, which carries the same criteria 2.4.7/2.4.11): R118 O6 — no focus issue (reviewer). Recorded here because the observation was about the ring itself, not about zoom |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O— reviewer 2026-09-24: **"m05, focus order follows meaning"**. Focus moves in an order that matches how the view reads and operates, on every view walked |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | Product-wide, established 2026-09-24: every shortcut this application defines is a **modifier chord** (`Ctrl+Shift+1`–`5` on Take Assignment). MO6 governs **single-character** bindings, and the review found none on any view |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | No dragging, multipoint or path-based gesture on this view — the sample's only such interaction is Problem 3's drag-and-drop ranking on Take Assignment (S3), which ships a non-dragging alternative form (R017 O18) |
| MO8 — Pointer actions can be cancelled (up-event activation) | pass | Reviewer 2026-09-24: **"pointer cancelation passes"** — pressing the pointer down on a control, moving off it and releasing does not activate it. Tested on the product's shared control set, which is the same DevExpress and ASP.NET furniture on every view |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O2 — 10 visible targets measured; 8 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (81 inline + 29 external scripts scanned, 1 unreadable) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | fail | O— reviewer 2026-09-24: **"same issues with bypass mechanisms as seen before"**. The product's only bypass is the hidden jump-point mechanism, and it does not work as one: on Class Management, Enter swaps the instruction text for a **"no shortcuts"** message and moves nothing (R022 O4); on the Printable Assignment the jump controls are **"unlabled so they are useless"** (R113 O13). No headings or landmarks exist as an alternative route on any view but the Solutions page → V-F8, V-F1 |

**view_probe 2026-09-15:** answered MO9=pass, MO10=n/a by measurement; facts in `R117-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-15 view_probe): 10 visible targets measured; 8 under 24×24 px, all spacing-exempt (no other target within a 24 px circle) or inline/user-agent-sized
  - Classified: MO9 / WCAG 2.5.8 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-15 view_probe): no devicemotion/deviceorientation use in scripts (81 inline + 29 external scripts scanned, 1 unreadable)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R117-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
