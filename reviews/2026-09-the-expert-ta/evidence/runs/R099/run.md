# Test Run R099 — S1

| | |
|---|---|
| **Run ID** | R099 |
| **Date/time** | 2026-09-11 15:55 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-21, reviewer's grayscale pass. The page still works — nothing on it is operated by colour — but the headings that label the two grids wash out, and V-F2 says position is the only thing left to tell them apart. Works with issues, not Broken.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | partial | O4 — no colour-coded *status* on this page; what fails is the section headings "Class Assignments" and "Class News", which are the only visual label telling the two grids apart and wash out in grayscale (reviewer: "class assignment and class news fail") |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O3 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-17; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O4 — with colour gone the two grids lose their headings, and V-F2 already records that they are otherwise told apart only by position. Reviewer: "all contrast fails in greyscale" |

**view_probe 2026-09-11:** answered NC2=pass by measurement; facts in `R099-probe.json`.

**view_probe 2026-09-17:** answered NC2=n/a by measurement; facts in `R099-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): all 3 link(s) in running text carry a non-colour cue (underline/border/weight) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → pass

- O3 [measured] (state: view as loaded, 2026-09-17 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-17; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a

- O4 [clarified] (state: Class Management standard mode under a grayscale filter, reviewer, 2026-09-21 — step W32): *"class assignment and class news fail"*, and generally *"all contrast fails in greyscale"*. The two section headings are the only visual label distinguishing the Class Assignments grid from the Class News grid, and they are not readable with colour removed. No status, error or required-field state on this page is carried by colour.
  - Classified: NC1 / partial (no colour-coded status; the headings are a labelling failure) → **V-F31**; NC3 / WCAG 1.4.1, and the contrast half under **V-F23** (1.4.3) / fail

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R099-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
