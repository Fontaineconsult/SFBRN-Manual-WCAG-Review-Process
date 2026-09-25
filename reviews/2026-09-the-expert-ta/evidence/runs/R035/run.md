# Test Run R035 — S5

| | |
|---|---|
| **Run ID** | R035 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S5 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | N/A |

**Result reasoning.** The view was withdrawn from the sample on 2026-09-15 as not student-facing (03 §3.1), after the walk-throughs established that the page is reachable only by an instructor account. This run was logged before that decision and cannot be completed: its open check rows ask what a user experiences on a page that is no longer in scope, and answering them would put weight on evidence the review does not rely on. The measurements already in this folder — the axe output and the probe JSON — stay on record and can be reopened unchanged if the scope is ever extended to instructor-facing pages.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Assignment Editor" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV3 — Every control announces an accurate name, role, and value/state | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV4 — Images announce appropriate alternatives; decorative images are silent | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV5 — Reading order matches the meaning of the visual order | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV8 — Nothing is conveyed only by visual position, shape, or size | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 superseded — the reviewer found YouTube embeds inside the editor 2026-09-15 (R037 O6); reviewer to say whether they carry audio description or a transcript — View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | n/a | (row added 2026-09-14 by sync-checks — not part of the original session; answer or mark n/a) — View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
**view_probe 2026-09-11:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R035-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a — **superseded 2026-09-15**: videos exist in a panel the probe did not open (R037 O6); row reopened
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): document.title = "Assignment Editor" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R035-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
