# Test Run R109 — S3

| | |
|---|---|
| **Run ID** | R109 |
| **Date/time** | 2026-09-11 15:57 |
| **View / sample** | S3 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/TakeTutorialAssignment.aspx?z=1&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-21, reviewer's grayscale pass. Broken for this modality: the randomised variable values are the numbers the student must put into the calculation, and with colour removed there is nothing that marks them as theirs ("random values fail"). The hint deduction percentages — what a hint costs — and the problem navigator fail with them. Only the status marks survive, because a symbol carries them.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | fail | O5 — three colour-only carriers fail with colour removed: the randomised variable values a student must calculate with, the hint/feedback deduction percentages, and the problem navigator. The per-problem status marks **pass** — a symbol carries them, not colour (reviewer) |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O4 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O5 — the reviewer cannot tell which numbers in the statement are their randomised values, so the problem cannot be worked reliably in grayscale |

**view_probe 2026-09-11:** answered NC2=fail by measurement; facts in `R109-probe.json`.

**view_probe 2026-09-14:** answered NC2=fail by measurement; facts in `R109-probe.json`.

**view_probe 2026-09-14:** answered NC2=n/a by measurement; facts in `R109-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 1 of 4 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: detailed view → #
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [measured] (state: view as loaded, 2026-09-14 view_probe): 1 of 4 link(s) in running text are told from the surrounding text by colour only — no underline/border/weight at rest and the G183 fallback (≥ 3:1 against the text plus a non-colour cue on hover AND on focus) does not hold — measured: detailed view → # [1:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O4 [measured] (state: view as loaded, 2026-09-14 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a

- O5 [clarified] (state: Take Assignment, Problem 1, under a grayscale filter, reviewer, 2026-09-21 — step W32): *"the contrast of the orange-red numbers are very hard to see when at greyscale … hint fails, random values fail, navigator fail, status marks pass."* Three of the four colour carriers on this view fail: the **randomised variable values** (`#FF6347`) that the student must use in the calculation, the **hint/feedback deduction percentages** (`#FF9900`) that state what a hint costs, and the **problem navigator**. The **status marks pass** — they are carried by a symbol, so colour is not their only channel, which is the one place this view does it right.
  - Classified: NC1, NC3 / WCAG 1.4.1 / Major → **V-F31**; the low-contrast half of the same elements stays under **V-F23** (1.4.3)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R109-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
