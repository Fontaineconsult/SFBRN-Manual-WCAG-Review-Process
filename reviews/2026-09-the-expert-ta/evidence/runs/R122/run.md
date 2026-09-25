# Test Run R122 — S14

| | |
|---|---|
| **Run ID** | R122 |
| **Date/time** | 2026-09-21 13:30 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Broken |

**Result reasoning.** A user who cannot see the screen can enter the form and reach the submit control, so the page is not unusable, but the one field it contains has no label of its own and the first focusable element is a logo link named after its image file. Password reset is the route back in after a lockout, which is what makes an unlabelled field here more serious than the same defect elsewhere.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O1-O5 closed against the reviewer's walk of the reset form. O1 (`label` on the user-name field) -> V-F30, confirmed: tabbing into the field makes the screen reader announce the whole reset table instead of a label. O2 (logo `image-alt` + `link-name`) -> V-F43, confirmed by tabbing on 2026-09-21. O3 (`html-has-lang`) -> V-F18. O4 (`color-contrast` on the field captions) -> V-F23. O5 (no landmarks, no `main`, no `h1`) -> V-F1. O6 is counts and the `bypass` incomplete, dismissed. |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | The single incomplete is `bypass`, dismissed here for the same reason as the sign-in page: one short form under a short header, with nothing to skip past. |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | Cross-checked against the reviewer's NVDA walk of this page. axe reported no headings and no landmarks and the walk confirmed it, adding what the rule cannot see: the form is built as a layout table, so the field's caption is a sibling cell and the whole table is announced on entry. The instrument penetrated. |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [classified] (state: Password reset page, reached from the sign-in page, no error shown): axe `label` (critical) ×1 — the user-name field has no label of its own; the whole reset form is laid out in a table and the caption is a sibling cell.
  - Proposed: W1 / WCAG 1.3.1 + 3.3.2 + 4.1.2 (A) / Major → **V-F30**; the reviewer confirmed that tabbing into the field makes NVDA announce the whole reset table rather than a label.
- O2 [classified] (state: as O1): `image-alt` (critical) ×1 and `link-name` (serious) ×1 — the logo, which is the first focusable element, has no alternative text and names its link with the file.
  - Proposed: W1 / WCAG 1.1.1 + 2.4.4 + 4.1.2 (A) / Major → **V-F43**; the reviewer tabbed it on 2026-09-21 and heard "The ExperTa graphic visited link".
- O3 [classified] (state: as O1): `html-has-lang` (serious) ×1 — `<html>` carries no `lang`.
  - Proposed: W1 / WCAG 3.1.1 (A) / Minor → **V-F18**, which names this as one of the four pages without a language.
- O4 [classified] (state: as O1): `color-contrast` (serious) ×2 — the same `#3A7C89` on `#EDEDED` field captions measured at **4.05:1** on the sign-in page.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Minor → **V-F23**.
- O5 [classified] (state: as O1): `region` ×5, `landmark-one-main`, `page-has-heading-one` — no landmarks, no `main`, no `h1`.
  - Proposed: → **V-F1**.
- O6 [classified] (state: as O1): passes 16 / inapplicable 71; **incomplete** `bypass` ×1.
  - dismissed: counts are informational; `bypass` is dismissed here for the same reason as the sign-in page — one short form under a short header, with nothing to skip past.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R122-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
