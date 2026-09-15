# Test Run R037 — S5

| | |
|---|---|
| **Run ID** | R037 |
| **Date/time** | 2026-09-11 14:07 |
| **View / sample** | S5 |
| **Page URL / location** | https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547 |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | probe; reviewer (W46 aside) |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works with issues |

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

**Result reasoning.** Revised 2026-09-15: the reviewer found YouTube embeds in the editor's Library panel (O6) whose captions are YouTube auto-generated — captions exist but are not authored/accurate, so NH1 = partial (finding V-F26); NH2–NH4 n/a. Works with issues.

## Checks (no-hearing)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NH1 — Prerecorded video has accurate captions | partial | O6 — YouTube embeds in the expanding area under Library; captions present but **auto-generated** (reviewer) → V-F26; the probe's O2 n/a was measured on the view as loaded, before the panel was opened |
| NH2 — Live audio content has captions | n/a | O3 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547) |
| NH3 — Audio-only content has a transcript | n/a | O4 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547) |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | n/a | O5 — no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547); no Audio()/AudioContext use in scripts (126 inline + 54 external scripts scanned, 1 unreadable) |
**view_probe 2026-09-11:** answered NH1=n/a, NH2=n/a, NH3=n/a, NH4=n/a by measurement; facts in `R037-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547)
  - Classified: NH1 / WCAG 1.2.2 / measured → n/a — **superseded by O6** (the probe saw only the loaded state)
- O3 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547)
  - Classified: NH2 / WCAG 1.2.4 / measured → n/a
- O4 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547)
  - Classified: NH3 / WCAG 1.2.1 / measured → n/a
- O5 [measured] (state: view as loaded, 2026-09-11 view_probe): no video, audio, media embed/iframe or media link on the view as loaded (https://dei56mo.theexpertta.com/Common/AssignmentEditor.aspx?m=2&eid=3373&aid=17547); no Audio()/AudioContext use in scripts (126 inline + 54 external scripts scanned, 1 unreadable)
  - Classified: NH4 / WCAG 1.1.1, 1.4.2 / measured → n/a
- O6 [classified] (state: `UI: Assignment Editor → Library → the expanding area under Library` — YouTube embeds; 2026-09-15, reviewer, during W46): "There are videos discovered in the AssignmentEditor, they have captions and are YouTube embeds." Clarified: "the videos are in the expanding area under library, they are auto generated." "videos do not autoplay" (reviewer, 2026-09-15 → 1.4.2 n/a). Still open: audio description / transcript (NV11 on R035) — moot for the sample since the view was removed 2026-09-15, kept for the record.
  - Classified: NH1 / WCAG 1.2.2 / Major (assistant's rating — reviewer to confirm) → finding V-F26; NH2, NH3 stay n/a (no live audio, no audio-only); NH4 stays n/a (no sound-only feedback in the UI)

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R037-<what>.png)

## Findings raised from this run

- V-F26 (1.2.2 — auto-generated captions on the Library videos; recorded under S5 in 04 §B)
