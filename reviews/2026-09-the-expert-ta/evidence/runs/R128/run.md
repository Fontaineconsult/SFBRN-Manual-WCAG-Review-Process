# Test Run R128 — S14

| | |
|---|---|
| **Run ID** | R128 |
| **Date/time** | 2026-09-21 13:30 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-21. The no-color rows pass on measurement under the reviewer's same-styles ruling: this page has six text elements, no colour-coded status and no links inside running text (NC2 n/a). It is "Works with issues" rather than "Works" only because the run carries the page's other defect — the unlabelled user-name field, V-F30 — which is not a colour matter.

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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O2 — measured: six text-bearing elements in all; the only failing token is **#3A7C89** on "Request Password Reset", "User Name:" and "Note" — headings and labels, not status |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O2 — no links inside running text on the view (links are standalone controls/menu items) — measured |
| NC3 — Everything remains operable and understandable in grayscale | pass | O2 — one field, one button, no colour-coded state; the page reads and works with colour removed (`R128-grayscale.png`) |

**view_probe 2026-09-21:** answered NC2=n/a by measurement; facts in `R128-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a

- O2 [measured] (state: password reset page as loaded, 2026-09-21 — colour-token scan under the reviewer's same-styles ruling): six text-bearing elements, three distinct text colours. The only failing token present is `#3A7C89` on "Request Password Reset", "User Name:" and "Note" — headings and a field label. No status, error or required-field state is carried by colour anywhere on the page, and there is nothing to lose in grayscale.
  - Classified: NC1 / pass; NC3 / pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R128-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
