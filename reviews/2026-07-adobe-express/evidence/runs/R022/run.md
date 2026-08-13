# Test Run R022 — S3

| | |
|---|---|
| **Run ID** | R022 |
| **Date/time** | 2026-08-13 12:22 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | grayscale |
| **Baseline** | — |
| **Tester** | assistant (CSS grayscale proxy) |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | partial | O1 — chrome passes (boxed rail selection); **canvas selected-object highlight not capturable in this state** — reviewer question |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O1 — no body-text links in the captured editor chrome |
| NC3 — Everything remains operable and understandable in grayscale | partial | O1 — chrome yes; canvas interaction untested in grayscale |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, assistant — CSS grayscale proxy; narrow
  responsive state, Search panel open over canvas): editor chrome carries
  selection without color (boxed rail item). **The canvas questions — does
  the selected-object highlight survive grayscale; is anything on-canvas
  color-coded — could not be captured in this state** and go to the S3
  walkthrough Part G. Media audit this state: 0 audio / 0 video — but R014
  previously found a muted `<video>` in the asset panel, so S3's
  no-hearing determination stays **reviewer-gated** (insertable
  Videos/Music/Sound effects), and no N/A run is logged for it. Evidence:
  R022-nc-grayscale-top.png, R022-nc-grayscale-mid.png.
  - Classified: NC1/NC3 partial — no finding; canvas questions routed.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R022-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
