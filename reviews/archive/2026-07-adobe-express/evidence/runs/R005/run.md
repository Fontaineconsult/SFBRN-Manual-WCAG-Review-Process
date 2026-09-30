# Test Run R005 — S1

| | |
|---|---|
| **Run ID** | R005 |
| **Date/time** | 2026-08-04 15:44 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | assistant (Claude, Chrome automation) |
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

- O1 [classified] (state: default): DOM scan across shadow roots found zero
  `<audio>`/`<video>` elements and no autoplaying media; visual inspection
  confirms no audio or audio-video content on the home dashboard. Template
  card thumbnails are static images on this view.
  - Classified: NH1–NH4 / — / n/a — no finding

## Notes

Assistant-driven inspection. N/A justification: the view presents no audio
or audio-video content. Re-run if the home view gains media previews with
sound (some template categories autoplay in the Explore view — check there
when S2 is tested).

## Evidence files in this folder

- none (nothing to evidence for an N/A result; DOM scan recorded in
  Observations)

## Findings raised from this run

- none
