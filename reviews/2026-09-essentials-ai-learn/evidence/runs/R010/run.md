# Test Run R010 — S2

| | |
|---|---|
| **Run ID** | R010 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom (probe measurements kept: LV1, LV3, LV8; assistant contrast sampling) |
| **Baseline** | B3 |
| **Tester** | Daniel Fontaine (reviewer, browser zoom 400 %, baseline B3) + assistant (contrast sampling); assistant records |
| **Result** | Works |

**Result reasoning.** Low-vision run on My Courses (reviewer at 400 % browser zoom; assistant contrast sampling incl. rendered-pixel measurement of the gradient card). Reflow, text spacing, orientation, zoom, focus ring and every text contrast pass; component contrast passes with the focus-ring question delegated by the reviewer and recorded.

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O2 — at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 320: no horizontal scrolling (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O10 — reviewer at 400 %: no content or functionality lost, nothing clips; fully responsive |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 1 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | pass | O5, O6 — every text ≥ 4.5:1 (or 3:1 large) by computed-style sampling on solid backgrounds and band-pixel sampling on the gradient card and tab strip; tightest is "Gamified" at 4.57:1 |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O11, O7 — reviewer's 1.4.11 call (delegated on the ring): components are identifiable — filled button, bordered tab strip, bold/grey tab states; the ring is visible (2.4.7) and its 3:1 figure is the AAA 2.4.13 bar, not AA |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | n/a | O8 — no content appears on hover or focus |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O10, O11, O7 — no clipping at 400 %, the same outline ring on every stop (screenshots R013-tab01…10.png); ring questions delegated to the measurement by the reviewer |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (7 inline + 5 external scripts scanned) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O9 — real text throughout; logo and a decorative photo are the only images |

**view_probe 2026-09-30:** answered LV1=pass, LV3=pass, LV8=pass by measurement; facts in `R010-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 320: no horizontal scrolling (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 1 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): no orientation media query and no screen.orientation.lock use (7 inline + 5 external scripts scanned) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [new] (state: 1280×1000, 100 %, computed-style sampling against opaque ancestor backgrounds (case 1)): Text on solid backgrounds all pass: wordmark 16.7:1, "LMS" 7.0:1, sidebar links 9.0–9.4:1, "Test User" 16.7:1, "Learner" 5.2:1, avatar initials 9.0:1, "Learning" 4.95:1, h1 15.95:1, intro and "Two ways…" 4.95:1, "Start course" white on purple 7.0:1.
- O6 [new] (state: rendered-pixel sampling (case 2/3): Page.captureScreenshot at 1280×1000 (R010-mycourses-1280.png, verified visually against the layout), background taken ONLY from a 3–6 px band outside each text box so anti-aliased glyph edges never count): The seven texts axe could not resolve (gradient course card, translucent tab strip): "Classic" 14.6:1, "Gamified" 4.57:1 (grey rgb(112,106,124) on the tab strip — the tightest pass), both count badges 4.95:1, "Start here" 6.4:1, h2 "AI Foundations - Sonoma State University" 15.3:1 (large), "This is the first course…" median 9.0:1 with one outlier band pixel from the adjacent thumbnail excluded. All pass. This settles axe R008 O1 (`color-contrast` incomplete ×3).
- O7 [new] (state: inspection + measurement (LV5 facts; reviewer rules)): Component boundaries: the selected sidebar item is a lavender pill rgb(244,237,252) with purple text; the tab strip has a light border; the active tab is distinguished by bold dark text (rgb(34,26,46)) vs grey (rgb(112,106,124)) — contrast between the two states ≈ 3.2:1 against each other; "Start course" is a filled purple button (≈ 7:1 against the card). Focus ring lilac rgb(201,168,236) on white ≈ 2.1:1 — visible, below the AAA 3:1 (2.4.13), not an AA requirement. Screenshot `R010-focus-nav.png`.
- O8 [new] (state: inspection): No `title` attributes, tooltips or hover-revealed content on the view (the avatar menu opens on click, not hover).
- O9 [new] (state: inspection): Images: the logo (alt "AI Essentials logo") and the course thumbnail (a photo, alt="" decorative). No images of text.
- O10 [classified] (reviewer, 400 % browser zoom, 2026-10-02): "No clips, site is fully responsive" — nothing clipped, overlapped or lost at 400 %; the layout reflows (sidebar collapses).
- O11 [classified] (reviewer, 2026-10-02, eyedropper on the focus ring): "I can't get the focus ring to stay when selecting the eyedropper, but just pass it" — the reviewer **delegated** the focus-ring contrast question to the assistant's measurement (O7: lilac rgb(201,168,236) ≈ 2.1:1 on white, ≈ 6.7:1 border change on fields; visible in every screenshot) and passed LV5 on the other components (selected-tab weight/luminance change, filled purple button). Delegation recorded per modality-checks.md.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (zoom instrument, partial).** Contrast measured two ways as testing-tools.md §zoom requires: computed-style on solid backgrounds, rendered pixels (band outside the text box) where axe reported a gradient/translucent background — the screenshot was checked visually first. LV2, LV5 and LV7 stay with the reviewer at 400 % browser zoom; LV5 facts in O-ui.

## Evidence files in this folder

- (screenshots/exports named R010-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
