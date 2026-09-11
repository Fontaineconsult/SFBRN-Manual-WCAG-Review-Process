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
| **Result** | Not set — NC1, NC3 need the reviewer — judge from `R104-grayscale.png` (achromatopsia emulation) or the OS filter |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | | |
| NC2 — Links are distinguishable from surrounding text without color | pass | O2 — all 3 link(s) in running text carry a non-colour cue (underline/border/weight) — measured |
| NC3 — Everything remains operable and understandable in grayscale | | |

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
