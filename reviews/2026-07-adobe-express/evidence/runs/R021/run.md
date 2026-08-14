# Test Run R021 — S2

| | |
|---|---|
| **Run ID** | R021 |
| **Date/time** | 2026-08-13 12:22 |
| **View / sample** | S2 |
| **Page URL / location** | https://new.express.adobe.com/explore/templates |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | grayscale |
| **Baseline** | — |
| **Tester** | assistant (CSS grayscale proxy per 03 s1.5) |
| **Result** | Works |

**Result reasoning** (set 2026-08-14). NC1 and NC3 pass; **NC2 closes 2026-08-14** - the link hover/focus cue question it was waiting on is answered by the reviewer's hover confirmation (R002 O-LV17). No colour-alone cue was found on this view.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O1 — selected chip = filled pill; selected rail item = boxed; checked filters = real checkmarks; filter count numeric |
| NC2 — Links are distinguishable from surrounding text without color | pass | O1 + reviewer hover confirmation 2026-08-14 (R002 O-LV17) — the hover/focus cue check this row was deferred for is answered |
| NC3 — Everything remains operable and understandable in grayscale | pass | O1 — top+mid captures |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, assistant — CSS `grayscale(100%)` proxy per
  03 §1.5; captured in the narrow responsive state the window was left in,
  which is noted, not hidden): selected states on Explore do not rely on
  color — filled pill (active content-type), boxed rail item, real
  checkmarks, numeric filter count. Media audit: **0 audio / 0 video
  elements** (feeds the S2 no-hearing N/A, R024). Evidence:
  R021-nc-grayscale-top.png, R021-nc-grayscale-mid.png.
  - Classified: NC1, NC3 / 1.4.1 / pass; NC2 partial (reviewer hover cue) —
    no finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R021-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
