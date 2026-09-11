# Test Run R020 — S1

| | |
|---|---|
| **Run ID** | R020 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | — |
| **Modality** | no-hearing |
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

## Checks (no-hearing)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NH1 — Prerecorded video has accurate captions | n/a | O2 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh) |
| NH2 — Live audio content has captions | n/a | O3 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh) |
| NH3 — Audio-only content has a transcript | n/a | O4 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh) |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | n/a | O5 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh); no Audio()/AudioContext use in scripts (57 inline + 51 external scripts scanned, 1 unreadable) |
**view_probe 2026-09-11:** answered NH1=n/a, NH2=n/a, NH3=n/a, NH4=n/a by measurement; facts in `R020-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh)
  - Classified: NH1 / WCAG 1.2.2 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh)
  - Classified: NH2 / WCAG 1.2.4 / measured → n/a
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh)
  - Classified: NH3 / WCAG 1.2.1 / measured → n/a
- O5 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/common/default.aspx, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh, https://dei56mo.theexpertta.com/DXR.axd?r=1_0-MM_qh); no Audio()/AudioContext use in scripts (57 inline + 51 external scripts scanned, 1 unreadable)
  - Classified: NH4 / WCAG 1.1.1, 1.4.2 / measured → n/a

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R020-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
