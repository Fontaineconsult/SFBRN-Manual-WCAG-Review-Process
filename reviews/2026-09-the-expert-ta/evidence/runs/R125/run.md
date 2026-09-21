# Test Run R125 — S14

| | |
|---|---|
| **Run ID** | R125 |
| **Date/time** | 2026-09-21 13:30 |
| **View / sample** | S14 |
| **Page URL / location** | https://login.theexpertta.com/ResetPassword.aspx |
| **Task / process** | — |
| **Modality** | no-speech |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | N/A |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-speech)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NS1 — No function requires speech input; any voice feature has a full non-speech alternative | n/a | O2 — no SpeechRecognition/getUserMedia/speechSynthesis use and no microphone/voice control (2 inline + 7 external scripts scanned) |
**view_probe 2026-09-21:** answered NS1=n/a by measurement; facts in `R125-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-21 view_probe): no SpeechRecognition/getUserMedia/speechSynthesis use and no microphone/voice control (2 inline + 7 external scripts scanned)
  - Classified: NS1 / WCAG FPC / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R125-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
