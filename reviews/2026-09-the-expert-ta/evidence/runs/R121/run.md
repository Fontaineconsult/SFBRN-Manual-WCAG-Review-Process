# Test Run R121 — S14

| | |
|---|---|
| **Run ID** | R121 |
| **Date/time** | 2026-09-21 13:29 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA); assistant records |
| **Result** | Not set — NV2, NV3, NV4, NV5, NV6, NV7, NV8, NV10, NV12 need the reviewer (jaws, B1); measured fail on NV9 awaits confirmation |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Expert TA - Reset Password" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | | |
| NV3 — Every control announces an accurate name, role, and value/state | | |
| NV4 — Images announce appropriate alternatives; decorative images are silent | | |
| NV5 — Reading order matches the meaning of the visual order | | |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | fail | O5 — the user-name field carries no proper label; what the reviewer hears on tabbing in is the whole reset **table** read out. Usable, not labelled — the reviewer's ruling is "accessible, but not best practice" → V-F30 (Minor). Confirmed by axe `label` (critical, 1 node, R122) |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | | |
| NV8 — Nothing is conveyed only by visual position, shape, or size | partial | O5 — the field's purpose is carried by its position in the layout table rather than by a label; the reviewer could still work it out from the table read-out, so this is not a blocking case → V-F30 |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | fail | O4 — <html> has no lang attribute (measured — 3.1.1) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | | |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | | |

**view_probe 2026-09-21:** answered NV11=n/a, NV1=pass, NV9=fail by measurement; facts in `R121-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-21 view_probe): document.title = "Expert TA - Reset Password" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-21 view_probe): <html> has no lang attribute (measured — 3.1.1)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → fail

- O5 [clarified] (state: Password reset page as loaded, `https://login.theexpertta.com/ResetPassword.aspx`, reviewer on NVDA, 2026-09-21): **"The form field for the user name in password reset isn't properly labeled, and like the rest of the app the whole reset form is structured in a table — tabbing into the form field launches a voice notification describing the whole reset table, so it is accessible, but not best practice."** The field has no label of its own; what the screen reader announces on focus is the surrounding layout table, from which the reviewer could work out what to type. The reviewer's ruling is explicit: **accessible, not a failure of the task** — the defect is the labelling, not the reachability. Independently confirmed by axe on the same page: `label` (critical) on one form element (R122).
  - Classified: NV6 / WCAG 1.3.1, 3.3.2, 4.1.2 / Minor (the reviewer's "not best practice") → finding **V-F30**; NV8 / partial (purpose carried by table position)
- O6 [measured] (state: as O5, 2026-09-21 view_probe): `<html>` on this page declares **no `lang`** attribute — the fourth page in the sample to do so, after Take Assignment (S3), Sign in (S7) and the Edit Class popup (S11).
  - Classified: NV9 / WCAG 3.1.1 / Minor → extends **V-F18** to S14
- O7 [measured] (state: as O5, 2026-09-21 view_probe): the page does not reflow — content still needs 1024 px at the 320 px viewport, the same fixed-width container as every other page.
  - Classified: LV1 (recorded on the low-vision run R123) / WCAG 1.4.10 → extends **V-F19** to S14

## Notes

2026-09-21 — The reviewer walked the password reset page with NVDA and reported the labelling of the user-name field. The page had never been sampled: it was on record as part of the authentication surface (`03` §1 C1 and A3) but carried no view ID, so it is added as **S14** (proposed — the reviewer confirms the sample addition) and swept (axe R122) and probed the same day. Only NV6/NV8 come from the reviewer; NV1/NV9/NV11 are measured; the rest of the no-vision rows are still open.

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R121-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
