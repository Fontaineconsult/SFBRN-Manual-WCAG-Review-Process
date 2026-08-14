# Test Run R009 — S1

| | |
|---|---|
| **Run ID** | R009 |
| **Date/time** | 2026-08-04 16:38 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (Claude, scripts/axe_scan.py; dedicated debug-profile Chrome, reviewer-authenticated) |
| **Result** | Works with issues |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**) is human-confirmed → finding, or dismissed with a written reason in the run notes | fail | O1 (V-F2 corroborated), O2 (new V-F4), O3 (best-practice, held as observation) |
| W2 — Every warning (axe **incomplete**) is reviewed; relevant ones investigated in the matching modality | pass | O4, O5, O6 routed; O8 resolves 8 of the 15 contrast nodes (pass), O9 holds the other 7 open with a named method |
| W3 — Structure output sane and cross-checked against the JAWS walk | pass | O3, O7 — axe penetrated the shadow DOM (unlike WAVE, R007); its landmark picture matches JAWS |

## Observations

axe-core 4.10.3, full ruleset: **violations 3, incomplete 3, passes 47,
inapplicable 42.** Raw output: `R009-axe.json` (1.65 MB).

- O1 [classified] (violation `color-contrast`, serious, wcag143): the exact
  node is `.browse-text` — the Upload card's "browse" link. **Independently
  corroborates finding V-F2** (R002's computed 3.96:1). Two instruments now
  agree.
  - Classified: W1 / WCAG 1.4.3 / Minor → finding V-F2 (evidence added)
- O2 [classified] (violation `aria-command-name`, serious, wcag412): icon-only
  `sp-action-button` inside `x-community-discovery-trigger` (the "community"
  people-icon in the header) has **no accessible name** — its x-icon is
  aria-hidden with an empty label. Vendor claims Does Not Support for 4.1.2 —
  consistent.
  - Classified: W1 / WCAG 4.1.2 / Major → finding V-F4 — JAWS confirmation in
    W5 (what announces on that button?)
- O3 [classified] (violation `region`, moderate, **best-practice tag — not a
  WCAG criterion**): the entire Recent bar (`x-home-recent-bar`: "Recent" h3,
  file card, "View all") sits **outside all landmarks**. Explains the W4
  reading-order oddity (Recent reads 3rd: it precedes `main` in the DOM).
  - Held as observation (no WCAG criterion failed); feeds the W4 NV5
    discussion — dismissal or finding is the reviewer's call there.
- O4 [classified] (incomplete `color-contrast`, serious, 15 nodes): the Adobe
  app-bar labels on the purple gradient (Adobe Home, Firefly, Express…) —
  axe cannot compute gradient backgrounds either. **Exactly the W13
  eyedropper queue** (matches R002 O3).
  - Routed: W13 (low-vision eyedropper measurements)
  - **AMENDED 2026-08-06 (O8):** the 15 nodes are not one group. They split
    into 8 app-bar labels (resolved, O8), 2 rotating-placeholder words, and
    5 headings over card art (both still open, O9). W13's queue is 8 nodes
    smaller than recorded.
- O8 [classified] (resolves 8 of O4's 15 nodes; session 2026-08-06,
  assistant, Chrome extension): the app-bar background is **not a CSS
  gradient** — it is a self-contained SVG
  (`express_background.svg`, `viewBox 0 0 1440 56`,
  `preserveAspectRatio="none"`, painted at `background-size: 100% 100%`),
  which is why axe returned *"background color could not be determined due
  to a background image"* rather than a ratio. Because the SVG references no
  external resources, it can be re-rendered same-origin as a data URI on a
  canvas and sampled exactly — no eyedropper needed. Method: draw at the
  container's rendered size (2328×56), sample a 13×7 grid across each
  label's box, compute WCAG contrast against the label colour
  `rgb(248,248,248)` (12px/500 → **normal text, 4.5:1 required**).
  Worst ratio per label: Adobe Home 11.23, Firefly 11.18, Express 11.23,
  Photoshop 11.43, Lightroom 11.64, Acrobat 11.71, Fonts 11.64, Stock 11.59.
  Darkest sampled background `rgb(46,38,138)`; the SVG's base fill is
  `#110036` and the two radial gradients (`#3236a8`, `#800081`) only lighten
  it slightly. **All 8 pass 1.4.3 with ~2.5× headroom.** Confounder checked
  and excluded: every `sp-underlay` in the tree is `visibility:hidden` /
  `opacity:0` (not painted) and the one painted `x-coachmark-underlay` is
  `rgba(0,0,0,0)` — nothing translucent sits over the bar.
  - Classified: W2 / WCAG 1.4.3 / pass — no finding. **Removes 8 nodes from
    the W13 reviewer queue.**
- O9 [new] (the other 7 of O4's 15 nodes — NOT resolved): these cannot be
  settled by DOM inspection and must not be guessed.
  (a) **5 headings over card art** — the four start-card `h2`s ("Start new
  design", "Edit photos", "Set up brand kit", "Generate presentation") and
  one `x-home-row` `h2`. Ancestor-walking returns *no painted background at
  all* (every ancestor `rgba(0,0,0,0)`, no background-image), and
  `elementsFromPoint` through the shadow roots is transparent the whole way
  down — the card colour is painted by a pseudo-element or a
  non-hit-testable image. An ancestor walk here yields a false "white
  background, 21:1"; that number is wrong and was discarded rather than
  recorded.
  (b) **2 rotating-placeholder words** — axe: "partially obscured by another
  element", because the rotator keeps the outgoing and incoming word in the
  DOM simultaneously (see R010 O1).
  - **RESOLVED 2026-08-14 (O10) — all 7 nodes measured and passing.**
  - Routed: rendered-pixel sampling via CDP `Page.captureScreenshot` on the
    debug-profile Chrome (exact coordinates recorded above), or the W13
    eyedropper. Method noted in testing-tools.md.
- O5 [classified] (incomplete `aria-valid-attr-value`, critical, 2 nodes):
  (a) "More apps" button has `aria-controls="spillover-dialog"` — verify the
  target ID exists when closed; (b) profile-thumbnail (account button)
  `aria-expanded`/`aria-haspopup="dialog"` — verify states toggle. Routed to
  W5 (JAWS behavior on both controls).
- O6 [classified] (incomplete `aria-required-children`, critical, 1 node):
  an **empty** `div role="list"` in the app bar (secondary app tiles) — no
  list items. Likely a latent/harmless empty container; verify it stays
  empty and silent in JAWS (W5); dismiss if so.
- O7 [classified]: **Refutation of an exploration recon item**: the
  Recent-file card link is NOT unlabeled — it contains
  `<span class="sr-only">Kaiser Permanente Mobile App - Letter Details</span>`
  and the thumbnail img has proper alt. The 2026-08-04 DOM-walk recon
  (03 §2.6) read only the light text and missed the sr-only span. Recon note
  corrected. axe reports no name violation on it.
  - Classified: W1 / — / recon corrected, no finding

- **O10 [classified]** (2026-08-14, assistant — resolves **all 7** remaining
  nodes from O4/O9, closing the axe-incomplete contrast queue entirely):
  measured from **rendered pixels** in the saved 1280×900 capture
  `R002/R002-lv5-uicontrast-reference-1280.png`.

  | Node | Text | Card / field | Contrast | 1.4.3 |
  |---|---|---|---|---|
  | Upload | `rgb(0,0,0)` | `rgb(233,233,233)` | **17.30:1** | pass |
  | Start new design | `rgb(0,0,0)` | `rgb(254,219,158)` | **15.84:1** | pass |
  | Edit photos | `rgb(0,0,0)` | `rgb(171,207,252)` | **13.06:1** | pass |
  | Set up brand kit | `rgb(0,0,0)` | `rgb(222,192,246)` | **12.98:1** | pass |
  | Generate presentation (2 lines) | `rgb(0,0,0)` | `rgb(255,182,168)` | **12.51:1** | pass |
  | Search placeholder, static part | `rgb(80,80,80)` | `rgb(255,255,255)` | **8.06:1** | pass |
  | Search placeholder, rotating word | `rgb(80,80,80)` | `rgb(255,255,255)` | **8.06:1** | pass |

  - **Every node clears 4.5:1 — the stricter threshold — with margin**, so
    the large-text allowance (3:1, which these ~19px bold headings would
    qualify for) does not need to be relied on.
  - **Method, and why it is not the method that failed in R042 O6.** That
    attempt mapped `getBoundingClientRect` coordinates onto screenshot
    pixels and was defeated by a ~56px offset between the two spaces. **No
    coordinate translation happens here**: the sampling regions were read
    off the rendered image itself and sampled from that same image — one
    coordinate space, self-consistent. Within each region the dominant
    colour is the card background and the luminance extreme is the glyph.
  - **Cross-check that the regions were right:** the sampled backgrounds
    reproduce the cards' visible colours — grey, yellow, blue, purple,
    coral, in that order across the row. Had the regions been misaligned,
    they would not have matched what is visibly on screen.
  - **This is the number an ancestor walk gets wrong.** DOM inspection
    returned *no painted background at all* on these nodes (every ancestor
    `rgba(0,0,0,0)`), which yields a false "white, 21:1". The rendered
    values above are the real ones — and note they still **pass**, so the
    discarded false number would have produced the right verdict for the
    wrong reason. Recording measured values rather than a lucky guess is
    the point.
  - **The rotating placeholder resolves too:** axe returned "partially
    obscured" because the rotator holds the outgoing and incoming word in
    the DOM simultaneously, but only one is painted in steady state
    (consistent with R010 O1 — 0 animations at 68s), so the rendered pixels
    settle it.
  - Classified: LV4 / WCAG 1.4.3 / **pass** — no finding. **The
    axe-incomplete contrast queue for S1 is now fully dispositioned: 15 of
    15 nodes resolved** (8 by the app-bar SVG measurement in O8, 7 here).

## Notes

First production run of `scripts/axe_scan.py` (see testing-tools.md §axe-core
for setup). Instrument reach confirmed: axe traversed the open shadow DOM
(node targets show full custom-element paths) — contrast with WAVE's
blindness (R007). Remaining blind spots: closed shadow roots, cross-origin
iframes.

Process bug found and fixed in the same session: the script logged the run
before attempting the CDP connection, orphaning R008 when the connection
failed. Fixed — connection now precedes logging.

## Evidence files in this folder

- R009-axe.json — raw axe-core output (violations, incomplete, passes,
  inapplicable, full node targets/HTML)

## Findings raised from this run

- V-F2 (corroborating evidence added), V-F4 (new — 4.1.2 unnamed community
  button); recorded in 04-task-testing.md §B
