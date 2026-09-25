# Test Run R039 — S5

| | |
|---|---|
| **Run ID** | R039 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S5 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | N/A |

**Result reasoning.** The view was withdrawn from the sample on 2026-09-15 as not student-facing (03 §3.1), after the walk-throughs established that the page is reachable only by an instructor account. This run was logged before that decision and cannot be completed: its open check rows ask what a user experiences on a page that is no longer in scope, and answering them would put weight on evidence the review does not rely on. The measurements already in this folder — the axe output and the probe JSON — stay on record and can be reopened unchanged if the scope is ever extended to instructor-facing pages.

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO2 — Every reached element can be operated (activate, select, dismiss) | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO4 — A visible focus indicator exists at all times | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO5 — Focus order follows the meaning and operation order of the view | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO8 — Pointer actions can be cancelled (up-event activation) | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O2 — 14 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): div#MainContent_seGradeWeight_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_seGradeWeight_I.dxeEditArea.dxeEditAreaSys "1"; div#MainContent_seGradeWeight_B-3.dxeButton.dxeButtonEditButton "" 16×10 px next to input#MainContent_seGradeWeight_I.dxeEditArea.dxeEditAreaSys "1"; div#MainContent_teAssignmentVisibleTime_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teAssignmentVisibleTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teAssignmentVisibleTime_B-3.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teAssignmentVisibleTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teStartTime_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teStartTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teStartTime_B-3.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teStartTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM" Reviewer 2026-09-14: exempt — the values "can be typed directly" into the fields, so an equivalent control exists (2.5.8 exception); the measurement stands as a record, the outcome is pass. |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | O3 — no devicemotion/deviceorientation use in scripts (126 inline + 54 external scripts scanned, 1 unreadable) |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |

**view_probe 2026-09-11:** answered MO9=fail, MO10=n/a by measurement; facts in `R039-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 14 target(s) under 24×24 px with another target inside the 24 px circle (measured; reviewer confirms which are essential/equivalent-exempt): div#MainContent_seGradeWeight_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_seGradeWeight_I.dxeEditArea.dxeEditAreaSys "1"; div#MainContent_seGradeWeight_B-3.dxeButton.dxeButtonEditButton "" 16×10 px next to input#MainContent_seGradeWeight_I.dxeEditArea.dxeEditAreaSys "1"; div#MainContent_teAssignmentVisibleTime_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teAssignmentVisibleTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teAssignmentVisibleTime_B-3.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teAssignmentVisibleTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teStartTime_B-2.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teStartTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"; div#MainContent_teStartTime_B-3.dxeButton.dxeButtonEditButton "" 16×9 px next to input#MainContent_teStartTime_I.dxeEditArea.dxeEditAreaSys "12:01 AM"
  - Classified: MO9 / WCAG 2.5.8 / measured → fail → reviewer 2026-09-14: exempt (typed entry) → pass
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no devicemotion/deviceorientation use in scripts (126 inline + 54 external scripts scanned, 1 unreadable)
  - Classified: MO10 / WCAG 2.5.4 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R039-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
