# Test Run R111 — S2

| | |
|---|---|
| **Run ID** | R111 |
| **Date/time** | 2026-09-11 15:58 |
| **View / sample** | S2 |
| **Page URL / location** | UI: Class Management → "Accessibility Page" button (lands on /common/default2.aspx) |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Not set — NC1, NC3 need the reviewer — judge from `R111-grayscale.png` (achromatopsia emulation) or the OS filter |

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
| NC2 — Links are distinguishable from surrounding text without color | n/a | O4 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | | |

**view_probe 2026-09-11:** answered NC2=fail by measurement; facts in `R111-probe.json`.

**view_probe 2026-09-14:** answered NC2=pass by measurement; facts in `R111-probe.json`.

**view_probe 2026-09-14:** answered NC2=n/a by measurement; facts in `R111-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): 1 of 4 link(s) in running text differ from surrounding text by colour only (no underline, border, weight or style change) — measured: Tab for Class News, Enter to skip → javascript:skipper('Feedback');
  - Classified: NC2 / WCAG 1.4.1 / measured → fail

- O3 [measured] (state: view as loaded, 2026-09-14 view_probe): 1 of 4 link(s) in running text are colour-only at rest but satisfy G183 (≥ 3:1 against the text, non-colour cue on hover and on focus) — measured: Tab for Class News, Enter to skip → javascript:skipper('Feedback'); [4.42:1 vs text; hover cue: a:hover; focus: outline] (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → pass

- O4 [measured] (state: view as loaded, 2026-09-14 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement)
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R111-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
