# Test Run R082 — S11

| | |
|---|---|
| **Run ID** | R082 |
| **Date/time** | 2026-09-11 14:10 |
| **View / sample** | S11 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/eClass.aspx?m=2&eid=3373 |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | N/A |

**Result reasoning.** The view was withdrawn from the sample on 2026-09-15 as not student-facing (03 §3.1), after the walk-throughs established that the page is reachable only by an instructor account. This run was logged before that decision and cannot be completed: its open check rows ask what a user experiences on a page that is no longer in scope, and answering them would put weight on evidence the review does not rely on. The measurements already in this folder — the axe output and the probe JSON — stay on record and can be reopened unchanged if the scope is ever extended to instructor-facing pages.

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO2 — Help (if offered) appears in a consistent location | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO3 — Labels and instructions make the required input clear | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO4 — Errors suggest how to fix the problem | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO5 — Previously entered information is not demanded again | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | n/a | O2 — no password/authentication field on the view |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO8 — Focus/input does not trigger unexpected context changes | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | n/a | O3 — no field collects the user's own information (name/email/phone/address/… not present) |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | n/a | View out of scope from 2026-09-15 — not answerable against a page no student reaches. |

**view_probe 2026-09-11:** answered CO6=n/a, CO9=n/a by measurement; facts in `R082-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no password/authentication field on the view
  - Classified: CO6 / WCAG 3.3.8 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no field collects the user's own information (name/email/phone/address/… not present)
  - Classified: CO9 / WCAG 1.3.5 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R082-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
