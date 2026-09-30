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
| **Result** | Works |

**Result reasoning** (set 2026-08-14). Every applicable check passes: NC1
and NC3 pass once the reviewer answered the canvas question the instrument
could not reach (O2 — selection is a bounding box with edge resize
circles, both geometric cues), and NC2 is n/a (no body-text links in the
editor chrome). No colour-alone cue was found anywhere on this view.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O1 — chrome passes (boxed rail selection); **O2 closes the canvas question 2026-08-14 (reviewer): selection is a bounding box + edge resize circles — geometry, not colour** |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O1 — no body-text links in the captured editor chrome |
| NC3 — Everything remains operable and understandable in grayscale | pass | O1 — chrome yes; O2 — the canvas's one state cue (selection) is perceivable without colour, so the work surface remains operable in grayscale |

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
- **O2 [classified]** (2026-08-14, **reviewer** — the canvas question O1
  could not capture): **a selected object is clearly marked by a bounding
  box with edge circles for resize.** Both cues are **geometric, not
  chromatic** — a shape and a set of handles, which survive grayscale
  intact and remain perceivable to a user who cannot distinguish colours
  at all.
  - This closes the one substantive 1.4.1 risk in the review. It mattered
    because it sits on the product's **core surface**: had selection been
    marked by a coloured glow or a colour-only border, 1.4.1 would have
    failed on the view where users spend their time, not on a peripheral
    control.
  - **Note how it was answered.** The instrument could not reach it —
    selection state is painted into the canvas and the grayscale proxy
    captured no selected object. This is the pattern CLAUDE.md describes:
    the probe answers "what exists in this snapshot", the reviewer answers
    "what a user perceives". The honest interim record was *unmeasured*,
    not a guess in either direction.
  - Classified: NC1, NC3 / WCAG 1.4.1 / **pass** — no finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R022-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
