# Test Run R104 — S10

| | |
|---|---|
| **Run ID** | R104 |
| **Date/time** | 2026-09-11 15:56 |
| **View / sample** | S10 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/vwMates.aspx?m=1&eid=3373 |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | N/A |

**Result reasoning.** The view was withdrawn from the sample on 2026-09-15 as not student-facing (03 §3.1), after the walk-throughs established that the page is reachable only by an instructor account. This run was logged before that decision and cannot be completed: its open check rows ask what a user experiences on a page that is no longer in scope, and answering them would put weight on evidence the review does not rely on. The measurements already in this folder — the axe output and the probe JSON — stay on record and can be reopened unchanged if the scope is ever extended to instructor-facing pages.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NC2 — Links are distinguishable from surrounding text without color | pass | O2 — all 3 link(s) in running text carry a non-colour cue (underline/border/weight) — measured |
| NC3 — Everything remains operable and understandable in grayscale | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |

**view_probe 2026-09-11:** answered NC2=pass by measurement; facts in `R104-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): all 3 link(s) in running text carry a non-colour cue (underline/border/weight) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R104-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
