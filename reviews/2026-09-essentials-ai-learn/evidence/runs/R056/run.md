# Test Run R056 — S1

| | |
|---|---|
| **Run ID** | R056 |
| **Date/time** | 2026-09-30 14:09 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | no-color |
| **Tool** | probe |
| **Baseline** | — |
| **Tester** | assistant (view_probe) |
| **Result** | Works |

**Result reasoning.** No-color run on the sign-in page (reviewer with the OS grayscale filter; probe emulation screenshot R056-grayscale.png). The only colour-coded state, the disabled vs enabled Sign in button, is distinguishable by luminance and focusability; no links in running text; error is text.

## Checks (no-color)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NC1 — Nothing is conveyed by color alone (status, errors, required fields, chart series, selected states) | pass | O4, O3 — the only colour-coded state (disabled vs enabled button) is also distinguishable by luminance and by not being focusable; nothing else is colour-only — reviewer in grayscale |
| NC2 — Links are distinguishable from surrounding text without color | n/a | O2 — no links inside running text on the view (links are standalone controls/menu items) — measured |
| NC3 — Everything remains operable and understandable in grayscale | pass | O4, O3 — the page has one form and one link; all remain identifiable and operable in grayscale (reviewer's grayscale look; error text and states are textual) |

**view_probe 2026-09-30:** answered NC2=n/a by measurement; facts in `R056-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no links inside running text on the view (links are standalone controls/menu items) — measured
  - Classified: NC2 / WCAG 1.4.1 / measured → n/a
- O3 [new] (state: R056-grayscale.png (achromatopsia emulation, written by the probe) inspected): The only state the view conveys by colour is the Sign in button's disabled look (grey vs purple when enabled). In grayscale the disabled and enabled buttons differ by luminance (mid-grey vs dark) and the disabled one also cannot be focused or clicked, so the state is not colour-only — reviewer confirms by looking at the enabled state in grayscale. Link "Forgot your password?" is standalone (not in running text) and underlines on hover. Required fields are not marked at all (neither by colour nor text).
- O4 [classified] (reviewer, grayscale, 2026-09-30): "Yes there is a difference in grey" — the disabled and the enabled Sign in button are distinguishable without colour (luminance). Nothing else on the page is colour-coded (O3: required fields are not marked at all, the link is standalone, the error is text).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30.** NC1 and NC3 are left for the reviewer's grayscale look (OS filter or the emulation screenshot); the facts above are what to check.

## Evidence files in this folder

- (screenshots/exports named R056-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
