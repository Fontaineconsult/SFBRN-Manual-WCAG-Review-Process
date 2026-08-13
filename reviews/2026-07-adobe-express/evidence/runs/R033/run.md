# Test Run R033 — S4

| | |
|---|---|
| **Run ID** | R033 |
| **Date/time** | 2026-08-13 15:27 |
| **View / sample** | S4 |
| **Page URL / location** | https://new.express.adobe.com/your-stuff/files/recent?filter=express |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard |
| **Baseline** | B2 |
| **Tester** | reviewer (D. Fontaine), physical keyboard, NVDA off |
| **Result** | Works with issues |

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | pass | O1 — "can tab across whole screen fine" |
| MO2 — Every reached element can be operated (activate, select, dismiss) | fail | O1 — **the file-card checkbox is not operable with the Space bar**; the "…" menu is operable → V-F12 extended (2.1.1) |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O1 — no traps during full traversal |
| MO4 — A visible focus indicator exists at all times | pass | O1 — "all focus is visible" (explicit) |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O1 — no anomalies narrated |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | none observed on this view |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | no drag interactions on this view |
| MO8 — Pointer actions can be cancelled (up-event activation) | n/a | not testable under B2 |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | partial | not measured on S4; no visibly small target reported (R029 O5) |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | desktop web |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | fail | shared header, no skip mechanism — V-F3 (product-wide) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, reviewer, B2 — full sweep): reach and focus
  visibility are clean ("can tab across whole screen fine, all focus is
  visible"); the "…" per-card menu operates. **The file-card checkbox does
  not respond to the Space bar** — the standard (and only) keyboard
  activation for a checkbox — so **bulk file selection is unavailable to a
  keyboard-only user**. The same control NVDA users cannot identify
  (V-F12's missing name) is one keyboard users cannot operate: two defects,
  one control, both directions of the same neglect.
  - The "…" menu offers per-file actions, but nothing narrated suggests it
    provides multi-select/bulk equivalents — so no workaround is
    established.
  - Classified: MO2 / WCAG 2.1.1 / Major → **V-F12 extended** (criteria now
    4.1.2 + 2.1.1); MO11 fail via shared-header V-F3.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R033-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
