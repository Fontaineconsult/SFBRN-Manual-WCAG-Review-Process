# Test Run R051 — S1

| | |
|---|---|
| **Run ID** | R051 |
| **Date/time** | 2026-09-30 14:09 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | low-vision |
| **Tool** | zoom (probe measurements kept: LV1, LV3, LV8; assistant contrast sampling O5–O8) |
| **Baseline** | B3 |
| **Tester** | Daniel Fontaine (reviewer, browser zoom 400 %, baseline B3) + assistant (contrast sampling); assistant records |
| **Result** | Works with issues |

**Result reasoning.** Low-vision run on the sign-in page (reviewer at 400 % browser zoom, baseline B3, plus assistant contrast sampling). Reflow, text spacing, orientation, zoom and focus ring at zoom all pass; the one failure is the Email field's placeholder text at 3.5:1 (LV4, confirmed by the reviewer 2026-09-30) — finding V-F1, Minor. Field boundary contrast ruled acceptable by the reviewer (LV5).

## Checks (low-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| LV1 — At 400% zoom content reflows to one column — no two-dimensional scrolling (except exempt content such as data tables, canvases, maps) | pass | O2 — at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 320: no horizontal scrolling (measured) |
| LV2 — No content or functionality is lost at zoom; nothing overlaps or clips | pass | O9 — reviewer at 400 % browser zoom: no content or functionality lost, nothing overlaps or clips |
| LV3 — The view tolerates text-spacing overrides without loss | pass | O3 — text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override) |
| LV4 — Text contrast ≥ 4.5:1 (3:1 for large text) | fail | O5 — measured 3.5:1 on the Email placeholder text (needs 4.5:1); every other text passes — reviewer confirms (a fail on placeholder-only text may be rated Minor); **confirmed by the reviewer 2026-09-30** (O11) → finding V-F1 (Minor) |
| LV5 — UI component and meaningful graphic contrast ≥ 3:1 | pass | O13, O6 — reviewer's 1.4.11 ruling: the visible label identifies each field, so the faint resting border is not a failure; focus ring ≈ 6.7:1, checkbox border ≈ 5.2:1 (measured) |
| LV6 — Content appearing on hover/focus is dismissible, hoverable, persistent | n/a | O7 — no content appears on hover or focus |
| LV7 — Focus indicator remains visible and unobscured at zoom | pass | O12 — reviewer at 400 % zoom: focus ring visible and unobscured at every stop |
| LV8 — The view works in both portrait and landscape | pass | O4 — no orientation media query and no screen.orientation.lock use (7 inline + 12 external scripts scanned) — content is not restricted to one orientation |
| LV9 — Text is real text, not images of text (logos and essential presentation excepted) — at 400% zoom image text pixelates or stops reflowing | pass | O8 — real text throughout; logo is the only image |

**view_probe 2026-09-30:** answered LV1=pass, LV3=pass, LV8=pass by measurement; facts in `R051-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): at 320 CSS px (≈400 % zoom of 1280) scrollingElement.scrollWidth = 320: no horizontal scrolling (measured)
  - Classified: LV1 / WCAG 1.4.10 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): text-spacing override (line 1.5, letter 0.12 em, word 0.16 em, paragraph 2 em) applied: no newly clipped text container (measured; 0 container(s) were already clipped before the override)
  - Classified: LV3 / WCAG 1.4.12 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): no orientation media query and no screen.orientation.lock use (7 inline + 12 external scripts scanned) — content is not restricted to one orientation
  - Classified: LV8 / WCAG 1.3.4 / measured → pass
- O5 [new] (state: 1280 px window, 100 %, computed-style sampling against the first opaque ancestor background (case 1 of testing-tools.md §zoom — every sampled element had a solid background: page rgb(250,249,252) or card white)): Text contrast measured: "AI Essentials" 15.95:1 (large); "Readiness · Learning · Growth" 6.69:1 at 11 px; h1 "Sign in" 16.73:1; labels Email / Password 9.36:1; "Show password" 5.2:1; "Forgot your password?" 7.02:1; footer "Access is provisioned…" 4.95:1 — all ≥ 4.5:1. **Two below 4.5:1:** (a) the Email field's placeholder text "you@school.edu" rgb(139,135,149) on white = **3.5:1** at 13 px — placeholder is visible text and is the only example of the expected format; (b) the disabled Sign in button, white on rgb(139,135,149) = 3.5:1 — **exempt** as an inactive component while disabled (1.4.3 exception); its enabled colour is measured on the walk once the fields are filled.
- O6 [new] (state: same sampling, component edges (facts only — LV5 is the reviewer's eyedropper call per testing-tools.md)): Text-field boundary: 0.6 px border rgb(234,230,242) on a white field inside a white card — ≈ 1.15:1 against its surroundings, i.e. the field's edge is essentially invisible at rest; the field is identifiable only by its placeholder (Email) or by nothing (Password). Checkbox border rgb(112,106,124) ≈ 5.2:1. Focus ring on fields: purple border ≈ 6.7:1 (screenshot R051-signin-focus-email.png). Reviewer decides 1.4.11 for the resting field boundary.
- O7 [new] (state: inspection): No tooltip, popover or other content appears on hover or focus anywhere on the view (no `title` attributes, no hover-revealed elements).
- O8 [new] (state: inspection): The only image is the logo (`<img alt="AI Essentials">`); the wordmark "AI Essentials" beneath it and every other string is real text — no images of text beyond the logo exception.
- O9 [new] (reviewer narration 2026-09-30, 400 % browser zoom): "No render issues at 400 zoom" — nothing clipped, overlapped or lost. Pending for LV7: whether the focus ring stayed visible and unobscured at 400 %.
- O10 [clarified] (reviewer narration 2026-09-30, contrast): "Color contrast fails on all but large AA" — **clarification pending before any outcome changes**: which element(s) and which instrument/ratio. The assistant's sampling (O5) found every text ≥ 4.5:1 except two pairs at 3.5:1 — the Email placeholder and the disabled Sign in button — and 3.5:1 is exactly a pair that fails AA normal text and passes AA large text (3:1); if the reviewer measured those, the statements agree. If the reviewer measured the labels or body text, the instruments disagree and the rendered pixels decide (testing-tools.md §zoom).
- O11 [finding:V-F1] (reviewer, 2026-09-30, contrast tool): Clarified: the contrast failure is the **placeholder text inside the Email field** ("you@school.edu") — fails AA normal text, passes AA large only. Agrees with the assistant's 3.5:1 (O5). No other text was reported failing. → confirms the LV4 measured fail; finding V-F1.
- O12 [new] (reviewer, 2026-09-30, 400 % browser zoom, Tab through the stops): "Focus ring renders fine at 400 percent" — visible and unobscured at every stop.
- O13 [classified] (reviewer, 2026-09-30): 1.4.11 call on the text-field boundary (O6 facts: 0.6 px border ≈ 1.15:1 at rest): "label is fine for 1.4.11" — the field is identified by its label above it and by its focus ring; the resting border is not the component's only identification.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30 (zoom instrument, partial, Chrome automation).** Contrast by computed-style sampling — valid here because every text sits on a solid colour (no gradient, image or pseudo-element background found by the ancestor walk; the alert live region is empty). LV2, LV5 and LV7 stay with the reviewer at real browser zoom (400 % in a 1280 px window): LV5 needs the eyedropper on the text-field edge (facts in O-ui), LV7 the focus ring at zoom. Evidence: `R051-signin-1280.png` (resting), `R051-signin-focus-email.png` (Email focused).

## Evidence files in this folder

- (screenshots/exports named R051-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
