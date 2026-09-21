# Test Run R102 — S6

| | |
|---|---|
| **Run ID** | R102 |
| **Date/time** | 2026-09-11 15:55 |
| **View / sample** | S6 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/calendar.aspx |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Broken |

**Result reasoning.** 2026-09-21, reviewer's grayscale pass. Broken for this modality: the calendar conveys an assignment and its span entirely through the coloured event bar, and with colour removed the reviewer's verdict is that it "fails totally" — neither the assignment name nor the days it covers survives.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | fail | O3 — the assignment's name and the bar that spans its days are carried by the event colour alone; reviewer: "the name of the assignment in the calendar, the bar that extends across days, fails totally" |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O4 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O3 — the event is not identifiable as an event with colour removed; "fails totally" (reviewer) |

**view_probe 2026-09-11:** answered NC2=fail by measurement; facts in `R102-probe.json`.

**view_probe 2026-09-14:** answered NC2=pass by measurement; facts in `R102-probe.json`.

**view_probe 2026-09-14:** answered NC2=n/a by measurement; facts in `R102-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 2 of 5 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: Select All → #; Only → #
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [measured] (state: view as loaded, 2026-09-14 view_probe): 2 of 5 link(s) in running text are colour-only at rest but satisfy G183 (≥ 3:1 against the text, non-colour cue on hover and on focus) — measured: Select All → # [4.42:1 vs text; hover cue: a:hover; focus: outline]; Only → # [4.42:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → pass

- O4 [measured] (state: view as loaded, 2026-09-14 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a

- O3 [clarified] (state: Calendar under a grayscale filter, reviewer, 2026-09-21 — step W32): *"in calendar, the name of the assignment in the calendar, the bar that extends across days, fails totally."* The event bar (white on `#8EA9DB`) is the only carrier of both the assignment's identity and the range of days it covers. With colour removed neither survives — the strongest of the day's grayscale failures.
  - Classified: NC1, NC3 / WCAG 1.4.1 / Major → **V-F31**

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R102-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
