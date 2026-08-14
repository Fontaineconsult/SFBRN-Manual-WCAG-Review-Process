# Test Run R032 — S2

| | |
|---|---|
| **Run ID** | R032 |
| **Date/time** | 2026-08-13 15:21 |
| **View / sample** | S2 |
| **Page URL / location** | https://new.express.adobe.com/explore/templates |
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
| MO1 — Every interactive element can be reached with the keyboard | pass | O1 — "can tab across all chrome elements"; grid items reachable |
| MO2 — Every reached element can be operated (activate, select, dismiss) | pass | O1 — Space operates tabs/filters; templates activatable via Space |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | pass | O1 — template open/exit works; no traps |
| MO4 — A visible focus indicator exists at all times | pass | O1 — **"focus indicator is always visible"** (explicit) |
| MO5 — Focus order follows the meaning and operation order of the view | pass | O1 — no anomalies narrated during full traversal |
| MO6 — Single-character shortcuts can be switched off or remapped | n/a | no single-character shortcuts observed on this view (editor "T" is S3 — V-F15) |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | n/a | no drag interactions on this view |
| MO8 — Pointer actions can be cancelled (up-event activation) | n/a | not testable under B2 (no pointer) |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | partial | not measured on S2 (S1 measured pass; grid cards visibly large) |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | desktop web |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | fail | same shared header, no skip mechanism — V-F3 applies on every view (19 stops to rail measured on S1, R004 O5) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (2026-08-13, reviewer, B2 — full sweep): *"can tab across
  all chrome elements and focus indicator is always visible. Space works,
  templates accessible via Space and can be exited."* All rail/tab/filter/
  search controls reachable and operable; template items activatable and
  exitable; focus visible throughout; no traps.
  - A deliberate contrast for the report: for a **sighted keyboard-only
    user this view works well** — the same grid that is unusable by ear
    (T1-F2: unnamed items, silent arrows) is fully operable by eye and
    keyboard. The S2 defects are AT-exposure defects, not input defects.
  - Classified: MO1–MO5 / 2.1.1, 2.4.7, 2.4.3 / pass; MO11 fail via the
    shared-header V-F3 — no new finding.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R032-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
