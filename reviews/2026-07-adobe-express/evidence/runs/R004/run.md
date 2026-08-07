# Test Run R004 — S1

| | |
|---|---|
| **Run ID** | R004 |
| **Date/time** | 2026-08-04 15:44 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard |
| **Baseline** | B2 |
| **Tester** | assistant (Claude, Chrome automation) |
| **Result** | Not set — run incomplete: instrument caveat, reviewer real-keyboard pass required (see Notes) |

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | | O1 partial signal; reviewer full Tab sweep needed |
| MO2 — Every reached element can be operated (activate, select, dismiss) | | reviewer |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | | reviewer (include "Get started" modal) |
| MO4 — A visible focus indicator exists at all times | | O2 positive signals only; full sweep needed |
| MO5 — Focus order follows the meaning and operation order of the view | | O1; reviewer |
| MO6 — Single-character shortcuts can be switched off or remapped | | reviewer |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | | reviewer (Upload card drag-drop has "browse" alternative — pre-verified visually) |
| MO8 — Pointer actions can be cancelled (up-event activation) | | reviewer |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | pass | O4 (full-page geometry measurement, 2026-08-06) |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | desktop web view; no motion features |

## Observations

- O1 [classified] (state: default, from page load): ~15 Tab presses stayed
  within the top Adobe app-switcher bar region (stops observed: app-bar
  product tiles, "+" pin button). **No skip link surfaced on the first Tab
  press.** Keyboard users must traverse the cross-product app bar before
  reaching Express content on every visit.
  - Classified: MO11 / WCAG 2.4.1 / Major → finding V-F3 — pending reviewer
    confirmation with a physical keyboard (see instrument caveat)
- O2 [clarified] (state: default): Focus indicators that were observed are
  visible: the app-bar "+" button shows a solid ~2px outline
  (R004-tab15-plusbutton-focus.jpg); the Photoshop tile a box-shadow focus
  style. Positive MO4 signal for the app bar only — not yet a pass for the
  whole view.
- O4 [classified] (state: default, whole page — session 2026-08-06,
  assistant, geometry measurement rather than eyeballing): enumerated every
  interactive target across all 303 open shadow roots
  (`button, a[href], input, select, textarea, [role=button|link|checkbox|
  tab|menuitem], [tabindex="0"], sp-action-button, sp-button, sp-link`),
  excluded zero-size/hidden/`opacity:0` nodes, and collapsed
  wrapper+inner pairs sharing a box (e.g. `sp-link` around its inner `a`) so
  one control counts once. **51 distinct targets** on S1 at 2328×1145.
  Five measure under 24 CSS px in one dimension:
  | Target | Size | Nearest other target (centre-to-centre) |
  |---|---|---|
  | "View all" — Quick edits | 40×15 | 115 px |
  | "View all" — File formats | 40×15 | 104 px |
  | "View all" — Templates (below fold) | 40×15 | 320 px |
  | Account/avatar button | 24×24 | 36 px |
  | Search input | 657×24 | 261 px |
  2.5.8 Target Size (Minimum) is met when a 24 px-diameter circle centred on
  the target intersects no other target's circle — i.e. centres ≥ 24 px
  apart. The closest neighbour anywhere in this set is **104 px**, over four
  times the threshold: the three undersized "View all" links sit alone
  beside their section headings, not in a cluster. **All five clear 2.5.8
  via the spacing exception**; the account button and search input are at
  the 24 px boundary and clear it outright as well.
  - Classified: MO9 / WCAG 2.5.8 / pass — no finding. Note this criterion
    has **no vendor claim at all** (the 2023 ACR predates WCAG 2.2 — see
    05 §"Vendor evidence gap"), so this is independent primary evidence,
    not a verification.
- O3 [new] (instrument): During the first five synthesized Tab presses,
  `document.activeElement` reported BODY while the page visibly rendered a
  focus state — focus attribution through the app's shadow DOM was
  unreliable under automation. Later stops attributed correctly. Recorded as
  an instrument caveat (guidance updated), not a product observation.

## Notes

Assistant-driven run. Tab-walk with per-stop `activeElement` queries
(piercing open shadow roots) + screenshots. The attribution instability (O3)
means absence-of-focus or unreachable-element conclusions from this run are
not trustworthy; **presence** observations (visible outlines, app-bar stops,
no skip link in first-Tab screenshots) are. Reviewer should repeat with a
physical keyboard: full Tab sweep to the Recent strip, operate one card,
open the "Get started" modal via keyboard, verify Esc exit (MO3) — note
R002's flyout Esc failure suggests Esc handling is weak.

## Evidence files in this folder

- R004-tab5-focus.jpg — after 5 Tabs (no skip link visible; focus in header region)
- R004-tab15-plusbutton-focus.jpg — app-bar "+" button with visible focus outline

## Findings raised from this run

- V-F3 (2.4.1 — no skip mechanism ahead of the cross-product app bar),
  recorded in 04-task-testing.md §B, pending reviewer confirmation
