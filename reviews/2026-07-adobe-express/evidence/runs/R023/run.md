# Test Run R023 — S4

| | |
|---|---|
| **Run ID** | R023 |
| **Date/time** | 2026-08-13 12:22 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
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
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O1 — boxed rail selection; numeric filter badge; "In:Files" filled chip |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O1 — no body-text links in captured state ("View all" below fold covered by S1's W18 pattern) |
| NC3 — Everything remains operable and understandable in grayscale | pass | O1 — top+mid captures |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, assistant — CSS grayscale proxy, narrow
  responsive state): Your stuff conveys selection and filter state without
  color (boxed rail item, numeric badge on the filter, filled scoped-search
  chip). Media audit: **0 audio / 0 video** (feeds S4 no-hearing N/A,
  R027). Evidence: R023-nc-grayscale-top.png, R023-nc-grayscale-mid.png.
  - Classified: NC1, NC3 / 1.4.1 / pass — no finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R023-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
