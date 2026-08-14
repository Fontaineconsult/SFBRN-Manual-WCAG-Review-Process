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
| **Result** | Works with issues |

**Result reasoning** (set 2026-08-14, all eight checks now answered).
LV1/LV2/LV3/LV7/LV8 pass — reflow, no loss at zoom, text-spacing
tolerance, focus visible and unobscured at 400%, and both orientations.
**LV6 passes on reviewer confirmation, retiring V-F1.** Two fail: **LV4**
(the "browse" link at 3.96:1 — V-F2, re-verified on Chrome 151) and
**LV5** (buttons/icons below 3:1 against their backgrounds — V-F18). Both
are real but bounded, so the view is usable with issues rather than
broken.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O7 — 320 CSS px viewport via CDP device emulation (the documented 1.4.10 equivalence): scrollWidth 320, zero horizontal overflow |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O7 — single column, nothing clipped/overlapped in top/mid screenshots; app-switcher bar removed at narrow width (noted, not a loss of Express functionality) |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O1 |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O2 (fail → V-F2); O3 superseded by O6 — app bar measured and passes; 5 headings over card art still open |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | **fail** | O-LV16 — reviewer with Color Contrast Checker, 2026-08-14: **text passes, but the buttons/icons holding it do not** when measured against the background. Confirmed on S1 Home *and* the editor → **V-F18** |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | **pass** | **O-LV17 — reviewer, 2026-08-14: *"no issues with hover, pass it."* Supersedes O4/O5, which were assistant-driven synthetic hover teleports → finding V-F1 WITHDRAWN** |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O-LV15 — reviewer at **400% zoom, 2026-08-14**: *"everything is navigable still"*. Nothing is lost or trapped behind sticky content at that magnification → closes **2.4.11 Focus Not Obscured** |
| LV8 — The view works in both portrait and landscape | pass | O-LV14 — landscape 900x400 by CDP emulation, 2026-08-14: **zero horizontal overflow**. Closes the check that previously stalled on an unstable screenshot — the metric answers it without one |

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
- O3 [superseded] (state: default): Adobe app-switcher bar labels (12px,
  white on purple gradient) and several badge/overlay texts sit on gradients
  or indeterminate backgrounds — computed-style sampling cannot measure
  these; eyedropper (CCA) needed. Also feeds LV5 (icons, control borders).
  - **Superseded 2026-08-06 by O6** for the app-bar labels (measured, pass).
    The premise was also wrong in one detail: the bar is not a CSS gradient
    but an SVG image, which is why *both* instruments (computed-style here,
    axe in R009) returned "indeterminate" rather than a number. LV5 (icons,
    control borders) remains open.
- O6 [classified] (state: default — resolves O3 for the app bar; full method
  and per-label figures in R009 O8): the app-bar background SVG
  (`express_background.svg`) is self-contained, so it was re-rendered
  same-origin as a data URI on a canvas at the bar's true rendered size and
  sampled directly — an exact measurement, not an estimate. Label colour
  `rgb(248,248,248)` at 12px/500 → normal text, 4.5:1 required. All eight
  labels (Adobe Home, Firefly, Express, Photoshop, Lightroom, Acrobat,
  Fonts, Stock) fall between **11.18:1 and 11.71:1**; darkest background
  sampled anywhere under them is `rgb(46,38,138)`. Excluded the obvious
  confounder: no translucent overlay is painted over the bar (all
  `sp-underlay` hidden/`opacity:0`; the one live `x-coachmark-underlay` is
  fully transparent).
  - Classified: LV4 / WCAG 1.4.3 / pass — no finding. **W13's eyedropper
    queue drops from 15 nodes to 7.**
  - Still open under LV4 (R009 O9): four start-card `h2`s and one row `h2`
    sit on card art whose colour is painted by a pseudo-element or
    non-hit-testable image — neither ancestor-walking nor
    `elementsFromPoint` can retrieve it. An ancestor walk returns a bogus
    "white, 21:1" here; that result was discarded, not recorded. Needs
    rendered-pixel sampling (CDP screenshot) or the eyedropper.
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

- O7 [classified] (2026-08-13, assistant — **instrument unblocked**): the
  2026-08-04 blocker ("window resize ignored; zoom keystrokes unavailable")
  applied to the *extension* channel. The **CDP channel does it properly**:
  `Emulation.setDeviceMetricsOverride` to a **320 CSS px viewport** — the
  equivalence testing-tools.md §zoom explicitly accepts for 1.4.10. Results
  on S1: reflow to a single column with **zero horizontal overflow**
  (scrollWidth 320); no content/functionality loss visible in top and
  mid-scroll captures (the Adobe app-switcher bar is *removed* at narrow
  width — noted; it is excluded third-party chrome, and its removal
  incidentally deletes the V-F3 tab-stop burden at this width); text-spacing
  override still clean at 320px (re-confirms O1); 900×320 landscape renders
  and scrolls with a note that the sticky Recent bar consumes about a third
  of the short-viewport height. Evidence: R002-lv-baseline-1280.png,
  R002-lv-reflow-320.png, R002-lv-reflow-320-mid.png,
  R002-lv-textspacing-320.png, R002-lv-landscape-900x320.png.
  - Classified: LV1, LV2, LV8 / WCAG 1.4.10, 1.4.4, 1.3.4 / pass — no
    finding. An earlier mis-navigation captured Your stuff instead of Home;
    those two PNGs were **deleted**, not retained (wrong-view evidence).

- **O-LV14 [classified]** (2026-08-14, assistant — CDP measurement on the
  clean debug profile, Chrome 151, extensions inert): low-vision
  measurement pass on S1.

  | Condition | Horizontal overflow |
  |---|---|
  | Baseline 1280 | 0px |
  | **Landscape 900x400** | **0px** |
  | **Text scaled 2x (text-only)** | **0px** |

  - **LV8 / 1.3.4 closes: pass.** Landscape holds with no overflow. The
    earlier attempt stalled on a screenshot that never stabilised; the
    metric settles it without one.
  - **1.4.4 Resize Text: the layout holds, but text clips.** Under
    text-only doubling, horizontal overflow stays at zero — yet
    **26 text block(s)** overflow fixed-height containers whose
    `overflow` is hidden: start-card `h2`s need 146px in 97px containers; quick-edit labels 1198-2072px in 616px.
  - **Outcome is Supports regardless**, because 1.4.4 is satisfied by
    browser zoom (Understanding 1.4.4) and this product reflows cleanly at
    the 320px/400% equivalence. The clipping affects users who scale
    **text only** rather than zooming the page — a distinct group, and one
    that skews low-vision. **Wants a reviewer visual check** to see what a
    user actually gets: truncation, ellipsis, or a scrollbar.
  - **Instrument honesty:** an earlier version of this measurement
    reported 57 clipped blocks on S1. Those were
    screen-reader-only elements (`height:1px`, clipped) whose scrollHeight
    explodes when fonts are scaled — **not** visible clipped text. The
    filter now excludes zero-area and visually-hidden nodes. The first
    number was discarded rather than recorded.
  - Classified: LV8 / 1.3.4 / pass; LV1 / 1.4.4 / pass with a recorded
    caveat — no finding

- **O-LV16 [classified]** (LV5 / 1.4.11 — **reviewer**, 2026-08-14, tool:
  *Color Contrast Checker*): **the text passes; the controls holding it do
  not.** Reviewer's words: *"home page all the text passes color contrast,
  but some of the button/icons holding the text don't when measured against
  the background. Same in the content edit view — text itself has enough
  contrast, but button doesn't."*
  - **This is precisely the split 1.4.11 exists to catch, and it is a
    genuinely easy one to miss.** 1.4.3 governs *text* against its
    background; 1.4.11 governs the **boundary of the control** against
    what surrounds it. A button can carry perfectly legible 7:1 label text
    and still fail, because a low-vision user must first perceive **that
    there is a button there** — and the control's own edge against the page
    is what conveys that.
  - **Confirmed on two views, which makes it a pattern rather than a slip:
    S1 Home and S3 the editor.** Two views, different components, same
    defect class.
  - **This is the LV5 check that four low-vision runs have been waiting on
    since 2026-08-13**, and it is the criterion the assistant tried and
    failed three times to measure automatically (R042 O6). The reviewer's
    eyedropper answered it in one pass — the outcome that instrument work
    was routed toward, exactly as testing-tools.md §zoom now prescribes.
  - **What is deliberately NOT claimed here:** no ratio, and no count. The
    reviewer reported *"some"* controls failing, without enumerating which
    or by how much. Recording a number would be inventing one. The finding
    is sized on the pattern, and the enumeration is named as remediation
    work for the vendor rather than guessed at here.
  - Classified: LV5 / WCAG **1.4.11** / Major → finding **V-F18**

- **O-LV17 [classified]** (LV6 / 1.4.13 — **reviewer**, 2026-08-14):
  **"no issues with hover, pass it."** Confirmed with a real pointer.
  → **finding V-F1 WITHDRAWN; 1.4.13 moves from Does Not Support to
  Supports.**
  - **This supersedes the assistant evidence, and the reason matters.**
    O4/O5 were produced by **synthetic hover teleports** — the pointer was
    jumped from coordinate to coordinate rather than moved continuously.
    That is not how a hover interaction works: a flyout that dismisses
    when the pointer *teleports* away may behave perfectly when the
    pointer *travels* onto it along a path. The original finding recorded
    this caveat and explicitly asked for pointer confirmation; the
    confirmation came back negative.
  - **The instrument hierarchy applied as written** (CLAUDE.md): the
    reviewer's direct interaction outranks an assistant probe, and the
    probe's own recorded limitation is what flagged it for confirmation
    in the first place. The process worked — a doubtful finding was
    marked doubtful, routed, and retired rather than shipped.
  - **Fourth assistant hypothesis retired by reviewer testing** on this
    review, after the 2.1.1 "pointer-only editing" Blocker, "invisible
    editing", and the claim that the editor lacks landmark bypass. All
    four were caught before reaching the report. Worth stating plainly in
    the report's methodology note: **assistant-driven interaction findings
    on this product have a poor track record and must be reviewer-gated.**
  - Classified: LV6 / WCAG **1.4.13** / **pass** — **V-F1 withdrawn**

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
