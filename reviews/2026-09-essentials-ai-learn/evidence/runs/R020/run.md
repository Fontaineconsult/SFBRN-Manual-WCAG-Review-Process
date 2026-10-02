# Test Run R020 — S3

| | |
|---|---|
| **Run ID** | R020 |
| **Date/time** | 2026-09-30 14:07 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker` (video lesson); Classic experience |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | inspection (probe measurements kept: CO6, CO9) |
| **Baseline** | — |
| **Tester** | assistant (inspection); reviewer completes CO1/CO8/CO12 — assistant records |
| **Result** | Not set — CO1, CO2, CO3, CO4, CO5, CO7, CO8, CO10, CO11, CO12 need the reviewer (inspection) |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | | |
| CO2 — Help (if offered) appears in a consistent location | n/a | O4 — no help is offered on this view (A2 recorded; vendor claims 3.2.6) |
| CO3 — Labels and instructions make the required input clear | n/a | O4 — no input on the view |
| CO4 — Errors suggest how to fix the problem | n/a | O4 — no input, no error state |
| CO5 — Previously entered information is not demanded again | n/a | O4 — nothing is entered |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | n/a | O2 — no password field and no sign-in form on the view — authentication happens elsewhere |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | O4 — no time limit; the video is user-controlled with a native pause; no auto-moving content beyond a sub-second progress animation |
| CO8 — Focus/input does not trigger unexpected context changes | | |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | n/a | O3 — no field collects the user's own information (name/email/phone/address/… not present) |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | pass | O4 — reachable via the outline, the sequential Up-next flow and My Courses |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | O4 — Complete & continue records progress only; nothing legal, financial or destructive |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | | |

**view_probe 2026-09-30:** answered CO6=n/a, CO9=n/a by measurement; facts in `R020-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no password field and no sign-in form on the view — authentication happens elsewhere
  - Classified: CO6 / WCAG 3.3.8 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no field collects the user's own information (name/email/phone/address/… not present)
  - Classified: CO9 / WCAG 1.3.5 / measured → n/a
- O4 [new] (state: inspection): No form field on the view. No help link or support contact (A2). No time limit; the only moving content is the video, user-initiated with a native pause control (and the progress-bar fill animation, < 1 s, on load). The lesson is reached via the outline, via "Up next"/"Complete & continue" sequencing, and the player via My Courses → Start course — more than one way. "Complete & continue" records progress; it is the only state-changing action and progress can be re-opened (lessons stay available after completion) — not legal/financial. The outline, header and lesson body are identified the same way on every lesson (S4, R1 share the player).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (inspection).** CO1 (consistency with the other lesson views and the shell), CO8 (does selecting a lesson or completing one move focus/context unexpectedly) and CO12 (the video content — the reviewer watches for flashing) stay with the reviewer.

## Evidence files in this folder

- (screenshots/exports named R020-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
