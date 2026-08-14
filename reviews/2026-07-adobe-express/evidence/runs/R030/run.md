# Test Run R030 — S3

| | |
|---|---|
| **Run ID** | R030 |
| **Date/time** | 2026-08-13 13:48 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | reviewer (D. Fontaine) — video edit window capability inspection |
| **Result** | N/A |

## Checks (no-hearing)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NH1 — Prerecorded video has accurate captions | n/a | O1 — the editor's *own* UI carries no prerecorded AV content; media enters only by user insertion. The caption question for *inserted* video is an authoring-output matter → O1/O2, routed to 06 §504 |
| NH2 — Live audio content has captions | n/a | no live audio anywhere in the product observed |
| NH3 — Audio-only content has a transcript | n/a | no audio-only content in the editor UI |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | pass | no sound-alone feedback encountered across all reviewer sessions on this view |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
Reviewer inspection 2026-08-13 (narrated during the S4 session's W26
closures). The determination that stayed open since the S3 axe sweep —
whether the editor's insertable media makes no-hearing a live modality —
is resolved: **for the editor's own UI it is N/A; for the product's
authoring output it is a §504 capability question, half-answered well.**

- O1 [classified] (video edit window — **capability positive, credit it**):
  *"in the video edit window there is a CC button that allows
  auto-generated captions."* Express **does** provide a captioning
  capability for user-inserted video — unlike alt text for images
  (R016 O10), where no capability exists at all.
  - Classified: authoring capability (508 §504.2 / ATAG B.2.3-supporting)
    — recorded in 06 §Concerns; not a WCAG check outcome for this view.
- O2 [classified] (same window — **the gap**): *"no apparent way to upload
  professional captions."* No visible path to supply an authored caption
  file (SRT/VTT) or, by extension, to substitute corrected captions for the
  auto-generated ones. Consequences for output conformance: auto-generated
  captions are, as a class, insufficient for published-content 1.2.2
  (accuracy, speaker identification, meaningful sound description), and
  institutions with professional captioning workflows — standard in CSU
  practice — **cannot inject their caption files** into Express-produced
  video. Whether auto-captions are at least *editable* in place was not
  established — worth one follow-up look; editability would soften this
  materially.
  - Classified: 508 §504.2 gap (partial capability), sibling of the
    alt-text concern — recorded in 06 §Concerns, **not** as a WCAG finding
    against the editor UI.
- O3 [classified] (no-speech, all views — reviewer): **"no voice input"**
  anywhere in the product. Strengthens the N/A determinations in
  R025/R026/R028 with reviewer confirmation on top of inspection.
  - Classified: NS1 n/a confirmed.
- Open question routed to W16 (export walk): **do captions survive
  export/publish** — does downloaded or webpage-published video carry the
  caption track?

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R030-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
