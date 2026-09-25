# Test Run R112 — S13

| | |
|---|---|
| **Run ID** | R112 |
| **Date/time** | 2026-09-15 13:06 |
| **View / sample** | S13 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/ViewAssignmentDetails.aspx |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Broken |

**Result reasoning.** This page was sampled to test whether it is a conforming alternate route for reading an assignment, and it is not. It has no headings and no landmarks, eight of fourteen figures carry no usable alternative, and every equation announces as an unnamed button that opens a menu instead of being read. A screen-reader user gets neither the diagrams, nor the mathematics, nor a way to move between problems.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O1-O4 closed against the reviewer's NVDA walk of this page. O1 (`select-name` on the hidden accessibility menu) is the control the walk had to use to move at all; O2 (`color-contrast` on the randomised values) -> V-F23, confirmed at 400 % zoom; O3 (`aria-command-name`, `aria-hidden-focus`) -> V-F8 and V-F43; O4 (no landmarks, no `main`, no `h1`, `region` x29) -> V-F1. O5 is counts and the product-wide `bypass` incomplete, dismissed. |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | The single incomplete is `bypass`, the product-wide question settled once on S1. |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | Cross-checked against the NVDA walk of this page. axe reported no headings and no landmarks; the reviewer found the same and had to navigate by a hidden custom menu whose controls are unnamed. The instrument penetrated -- what it could not see is the mathematics, which announces as unnamed buttons (V-F45) and is invisible to a rule that only checks for a name. |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [classified] (state: View Printable Assignment, the nine problems of "Chapter 5 Sample Assignment" rendered on one page): axe `select-name` (critical) ×1 — the accessibility-menu select in the custom hidden header has no accessible name.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — the reviewer reached this page's navigation only through that hidden menu (W69) → folded into **V-F45**'s neighbours; the unnamed navigation controls are recorded there.
- O2 [classified] (state: as O1): `color-contrast` (serious) ×3 — the randomised-variable values in the problem statements, the same `#FF6347` on white token measured at **2.94:1** elsewhere.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major → **V-F23**; the reviewer confirmed at 400 % zoom (W68: "same contrast issues as before with the red values").
- O3 [classified] (state: as O1): `aria-command-name` ×1 and `aria-hidden-focus` ×1 — the jump point and the header logo link (PW-B, PW-C).
  - Proposed: fold into **V-F8** (jump points) and **V-F43** (logo link).
- O4 [classified] (state: as O1): `region` ×29, `landmark-one-main`, `page-has-heading-one` — no landmarks, no `main`, no `h1`.
  - Proposed: → **V-F1**; confirmed by the walk (W69: "no headings, uses the custom hidden accessibility menue").
- O5 [classified] (state: as O1): passes 36 / inapplicable 51; **incomplete** `bypass` ×1.
  - dismissed: counts are informational; the `bypass` incomplete is the product-wide question settled once on S1 (PW-E).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R112-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
