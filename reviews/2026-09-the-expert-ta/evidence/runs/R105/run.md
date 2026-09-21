# Test Run R105 — S12

| | |
|---|---|
| **Run ID** | R105 |
| **Date/time** | 2026-09-11 15:56 |
| **View / sample** | S12 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Tutorial/ClassTutorialSelection.aspx?m=1&eid=3373 |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-21. Mirrors Class Management (R099): nothing here is *operated* by colour — the failing token present is the section heading, which loses its emphasis in grayscale. Works with issues, not Broken.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | partial | O3 — no colour-coded status on the view; the only failing token present is **#EFBB75** on the "Library" section heading, the same token as "Class Assignments" on S1, which the reviewer failed; applied under the reviewer's ruling 2026-09-21 — "the styles are the same across the app, if the other views use the same colors lets assume they also fail" — after **measuring** which tokens this view actually uses (the ruling is a conditional; the antecedent is established, not assumed) |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O3 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-17; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O3 — the section heading that labels the library area washes out, as on S1 (R099 O4) |

**view_probe 2026-09-11:** answered NC2=pass by measurement; facts in `R105-probe.json`.

**view_probe 2026-09-17:** answered NC2=n/a by measurement; facts in `R105-probe.json`.

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

- O3 [clarified] (state: Student Practice Area as loaded, 2026-09-21 — measured colour-token scan, applying the reviewer's same-styles ruling from W32): of the tokens failed on 2026-09-21 this view uses only **`#EFBB75`**, once, on the "Library" section heading — the same token as "Class Assignments" on S1. The teal `#3A7C89` appears as a navigation background, not as a carrier of meaning. No randomised values, no deduction percentages, no event bar.
  - Classified: NC1 / partial (no colour-coded status; a heading that washes out); NC3 / WCAG 1.4.1 / fail → **V-F31**

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R105-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
