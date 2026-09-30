# Test Run R027 — S4

| | |
|---|---|
| **Run ID** | R027 |
| **Date/time** | 2026-08-13 12:30 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | assistant (DOM media audit, R023 O1) |
| **Result** | N/A |

## Checks (no-hearing)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NH1 — Prerecorded video has accurate captions | n/a | O1 |
| NH2 — Live audio content has captions | n/a | O1 |
| NH3 — Audio-only content has a transcript | n/a | O1 |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | n/a | O1 |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, assistant inspection): N/A — S4 Your stuff holds no audio or audio-video content: DOM media audit found 0 <audio> and 0 <video> elements (R023 O1).
  - Classified: all checks n/a — Result N/A per modality-checks.md §Result semantics (counts as covered).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R027-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
