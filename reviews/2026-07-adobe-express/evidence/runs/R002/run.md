# Test Run R002 — S1

| | |
|---|---|
| **Run ID** | R002 |
| **Date/time** | 2026-08-04 15:44 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom |
| **Baseline** | B3 |
| **Tester** | assistant (Claude, Chrome automation) |
| **Result** | Not set — run incomplete: LV1/LV2/LV7/LV8 need a reviewer session (see Notes) |

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | | not testable by automation in this environment — reviewer: real browser zoom 400% at 1280px window (see Notes) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | | reviewer, with LV1 |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O1 |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O2 (fail), O3 (gradient areas pending eyedropper) |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | | pending — needs eyedropper measurement of icons/controls (O3) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | fail | O4, O5 — pending reviewer confirmation with continuous pointer movement |
| LV7 — Focus indicator remains visible and unobscured at zoom | | reviewer, with LV1 |
| LV8 — The view works in both portrait and landscape | | reviewer (device/emulation) |

## Observations

- O1 [classified] (state: default): Text-spacing override (line-height 1.5,
  letter 0.12em, word 0.16em, paragraph 2em) applied via injected CSS at
  normal viewport. Labels wrap ("Start new design", rail "Templates") but
  nothing clips, overlaps, or loses function. Transient: "Premium member"
  badge text absent in first capture, present in later ones — re-verify.
  - Classified: LV3 / WCAG 1.4.12 / pass — no finding
- O2 [classified] (state: default): "browse" link on the Upload card — 11px
  text, computed contrast 3.96:1 against the card background (needs 4.5:1).
  Consistent with vendor ACR claim of Does Not Support for 1.4.3.
  - Classified: LV4 / WCAG 1.4.3 / Minor → finding V-F2
- O3 [new] (state: default): Adobe app-switcher bar labels (12px, white on
  purple gradient) and several badge/overlay texts sit on gradients or
  indeterminate backgrounds — computed-style sampling cannot measure these;
  eyedropper (CCA) needed. Also feeds LV5 (icons, control borders).
- O4 [classified] (state: left-rail hover flyout): Hovering a rail item
  (Templates) opens a "Get inspired" flyout panel. Moving the pointer from
  the rail item onto the flyout dismissed it (hover content not hoverable).
  Caveat: synthetic hover teleports; confirm with continuous pointer travel.
  - Classified: LV6 / WCAG 1.4.13 / Major → finding V-F1
- O5 [classified] (state: left-rail hover flyout): With the flyout open,
  Esc did not dismiss it (not dismissible). The flyout also remained open
  through several subsequent interactions with the pointer elsewhere
  (visible in R003-grayscale-home.jpg, taken minutes later).
  - Classified: LV6 / WCAG 1.4.13 / Major → finding V-F1

## Notes

Assistant-driven run (Chrome automation; conventions:
`ontology/testing-tools.md` §Assistant-driven runs).

Instrument limitations hit in this environment (recorded per the ratchet —
guidance updated):
- Window resize was ignored (maximized/managed window; reported success but
  `innerWidth` unchanged at 2328 CSS px), and browser-zoom keystrokes are
  unavailable to the automation tool.
- CSS `zoom` was tried and **rejected as instrument**: it magnifies without
  re-evaluating responsive breakpoints — layout does not reflow, producing
  false LV1/LV2 failures. Screenshots from that attempt were discarded.
- Therefore LV1/LV2/LV7/LV8 require the reviewer at real browser zoom
  (Ctrl+plus to 400% in a 1280px-wide window).

Contrast sampling method (O2): computed color vs nearest ancestor solid
background, WCAG relative-luminance formula. Indicative — solid-background
results (the 3.96:1 "browse" link) are reliable; gradient/indeterminate
backgrounds (O3) are not measured.

Replication quirk: mouse-wheel scrolling over the content area did not
scroll this view during automation; the app manages its own scroll
containers.

## Evidence files in this folder

- R002-textspacing-home.jpg — S1 with text-spacing override applied (O1)
- R002-upload-card-browse.png — Upload card, "browse" link (O2)
- R002-flyout-hover.jpg — rail hover flyout mid-fade during hoverability
  test (O4)

## Findings raised from this run

- V-F1 (1.4.13 — hover flyout not hoverable / not dismissible), V-F2
  (1.4.3 — "browse" link contrast); both recorded in 04-task-testing.md §B,
  pending reviewer confirmation
