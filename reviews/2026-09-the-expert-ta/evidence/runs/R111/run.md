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
| **Result** | Works with issues |

**Result reasoning.** 2026-09-21. Same verdict as the standard page (R099) on the reviewer's ruling that Accessibility Mode does not change the palette: nothing here is operated by colour, but the headings that label the two grids wash out.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | partial | O6 — reviewer 2026-09-21: "accessibility mode does not change the color on the page", so this view carries the same palette as S1: no colour-coded status, but the grid headings wash out (R099 O4) |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O4 — no links inside running text on the view (links are standalone controls/menu items) — measured (re-measured 2026-09-14; replaces the earlier resting-state measurement) |
| NC3 — Everything remains operable and understandable in grayscale | fail | O6 — as S1: the headings labelling the two grids are lost with colour removed, and V-F2 records that the grids are otherwise told apart only by position |

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

- O5 [new] (state: attempted 2026-09-21, colour-token scan): **not measured.** Navigating to `default2.aspx` landed on `default.aspx` — the redirect recorded in `03` §2.6 and guarded against since 2026-09-11 — so the scan would have measured the standard page under the Accessibility Mode label. Reaching this view means pressing the "Accessibility Page" button, and the mode is **stored on the account** (T1-F3), so the assistant did not switch it: that changes the reviewer's environment. The same-styles ruling is therefore **not** applied to this view; its NC1/NC3 rows stay blank until the reviewer is in that mode anyway.
  - Classified: NC1, NC3 / not measured — the reviewer answers these the next time they are on the Accessibility Page → W74

- O6 [clarified] (state: Class Management Accessibility Mode, 2026-09-21 — step W32/W74): the assistant could not measure this view directly (O5: `default2.aspx` redirects, and the mode is stored on the reviewer's account). The reviewer settled it instead: **"accessibility mode does not change the color on the page."** The palette is therefore S1's, and S1's no-color outcome applies unchanged — NC1 partial, NC3 fail (R099 O4). This supersedes O5's "not measured".
  - Classified: NC1 / partial; NC3 / WCAG 1.4.1 / fail → **V-F31**

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R111-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
