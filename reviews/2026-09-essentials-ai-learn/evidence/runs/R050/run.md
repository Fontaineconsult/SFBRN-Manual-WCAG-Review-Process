# Test Run R050 — S1

| | |
|---|---|
| **Run ID** | R050 |
| **Date/time** | 2026-09-30 14:09 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda (probe measurements kept: NV1, NV9, NV11) |
| **Baseline** | B5 |
| **Tester** | Daniel Fontaine (reviewer, NVDA 2024.1, baseline B5); assistant records |
| **Result** | Works with issues |

**Result reasoning.** NVDA 2024.1 walk of the sign-in page (reviewer, baseline B5; probe measurements for title, language and media kept). Title, one main landmark and one h1, reading order, logo alt, links list, every control's name/role/state, the automatically announced sign-in error and the announced landing title all pass. One Minor defect: the Password field's name includes the Show-password checkbox's label ("Password Show password") — finding V-F2 (4.1.2).

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O3 — document.title = "Sign in · AI Readiness OS" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | pass | O12, O11 — one main landmark and one level-1 heading "Sign in" — the page's only section, navigable by landmark and heading (reviewer, NVDA 2024.1) |
| NV3 — Every control announces an accurate name, role, and value/state | pass | O13, O14 — every control announces name, role and state on focus (edit / protected / has autocomplete / check box not checked / link / button); the disabled Sign in button is correctly absent from the tab order until enabled — reviewer, NVDA 2024.1 |
| NV4 — Images announce appropriate alternatives; decorative images are silent | pass | O15 — the only image, the logo, announces "AI Essentials" graphic — reviewer, NVDA 2024.1 |
| NV5 — Reading order matches the meaning of the visual order | pass | O16 — reading order with the arrow keys matches the visual order — reviewer, NVDA 2024.1 |
| NV6 — Form fields announce labels and instructions (the visible label is the accessible name, or the name says the same thing) | partial | O17, O13 — Email is labelled correctly; the Password field's name carries the Show-password checkbox's label as well ("Password Show password") — Minor finding V-F2; instructions (placeholder, autocomplete) are announced |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | pass | O8, O9 — the sign-in error is announced automatically without moving focus; the new page title is announced on successful navigation (reviewer, NVDA 2024.1) |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | O16 — nothing is conveyed by position or shape alone — reviewer |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | O4 — <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists) |
| NV10 — Every link's purpose is clear from its link text alone or from its programmatic context (Links list: no bare "click here"/"more", no identical texts pointing to different targets) | pass | O15 — links list holds only "Forgot your password?", whose text alone states its purpose — reviewer, NVDA 2024.1 |
| NV11 — Prerecorded video has audio description or a text media alternative (**n/a** when the view has no video) | n/a | O2 — no <video>, media iframe or embed on the view |
| NV12 — Input errors are identified in text — which field, what is wrong — and the screen reader hears it (submit a form with a missing/invalid value; **n/a** when the view has no validated input) | pass | O8 — error identified in text and spoken by NVDA: "That email and password don't match an account. Check them and try again." — names the credential pair (security-appropriate) and what to do |

**view_probe 2026-09-30:** answered NV11=n/a, NV1=pass, NV9=pass by measurement; facts in `R050-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no <video>, media iframe or embed on the view
  - Classified: NV11 / WCAG 1.2.3, 1.2.5 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): document.title = "Sign in · AI Readiness OS" (non-empty, specific; the reviewer's NVDA+T confirms wording on the walk)
  - Classified: NV1 / WCAG 2.4.2 / measured → pass
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): <html lang="en"> present and well-formed (measured; pronunciation of passages is the reviewer's call if any foreign-language content exists)
  - Classified: NV9 / WCAG 3.1.1, 3.1.2 / measured → pass
- O5 [new] (state: Accessibility.getFullAXTree on the signed-out window — recon for the JAWS walk, not outcomes): Tree: RootWebArea "Sign in · AI Readiness OS" → main → image "AI Essentials" → heading (h1) "Sign in" → textbox "Email" → textbox **"Password Show password"** → checkbox "Show password" → button "Sign in" (disabled) → link "Forgot your password?" → an empty `alert` live region. No unnamed control. The password field carries two labels (its own `<label>` wraps both the field and the Show-password checkbox's label), which is why axe flagged `form-field-multiple-labels` (R006 O1) and why the name reads "Password Show password". JAWS confirms on focus what each control announces (NV3, NV6) and whether the extra words mislead.
- O6 [new] (reviewer narration 2026-09-30, NVDA, wrong password submitted): "Feedback for wrong password announced" — the error after a failed sign-in is spoken by NVDA. Pending from the reviewer before NV7 / NV12 / CO4 are answered: the error's wording (which field, what to fix), whether it was spoken without a keystroke (live region) and whether focus moved.
- O7 [new] (reviewer narration 2026-09-30, NVDA, correct credentials): "Hitting Enter while in the password input successfully logged in" — Enter submits from the Password field although the fields are not inside a `<form>`. Pending: what NVDA announced on landing on My Courses and where focus went.
- O8 [classified] (reviewer, NVDA 2024.1, 2026-09-30, wrong password): Error announced automatically on submit, focus did not move. Announced text = the visible text: "That email and password don't match an account. Check them and try again." Names both fields as a pair (a deliberate security choice — 3.3.1 satisfied: the error is identified in text and spoken; 3.3.3: the suggestion is "check them and try again", the most a credential form may say).
- O9 [classified] (reviewer, NVDA 2024.1, 2026-09-30, successful sign-in): On Enter in the Password field with valid credentials: NVDA announces "My Courses AI Readiness OS" on the new page — the landing page's title is spoken on navigation.
- O10 [new] (reviewer, NVDA 2024.1, 2026-09-30, Tab into the Password field): Announced: "Password Show Password Edit Protected Show Blank" — the accessible name carries both the field's label and the Show-password checkbox's label (the wrapping `<label>`, axe R006 O1). Role and state (edit, protected, blank) correct. Visible label "Password" is contained in the name (2.5.3 satisfied). Pending the reviewer's call on whether the extra words are a Minor 4.1.2/3.3.2 finding or acceptable.
- O11 [new] (reviewer, NVDA 2024.1, 2026-09-30, page load): Title announced "Sign in Readiness OS" (document title is "Sign in · AI Readiness OS" — NVDA wording as heard). Landmarks: "Main landmark" found. Email field announces "has autocomplete" (the `autocomplete=email` attribute is exposed).
- O12 [classified] (reviewer, NVDA 2024.1, 2026-09-30, headings list): One heading: "Sign in", level 1. With the main landmark (O11) the structure NVDA finds is exactly what axe/the AX tree reported (one main, one h1).
- O13 [classified] (reviewer, NVDA 2024.1, 2026-09-30, Tab through the form, fields empty): Speech viewer, verbatim: "Email edit has auto complete you@school.edu blank" / "Password Show password edit protected has auto complete blank" / "Show password check box not checked" / "Forgot your password? link". The Sign in button is not a stop while the fields are empty (disabled).
- O14 [classified] (reviewer, NVDA 2024.1, 2026-09-30, Tab through the form, fields filled): "Email edit has auto complete selected access@sfsu.edu" / "Password Show password edit protected has auto complete selected ••••••••" / "Show password check box not checked" / "Sign in button" — the button becomes a stop once both fields hold a value; the placeholder is read as the field's value hint while empty.
- O15 [classified] (reviewer, NVDA 2024.1, 2026-09-30, logo and links): The logo announces "AI Essentials" graphic. Links list: only "Forgot your password?".
- O16 [classified] (reviewer, NVDA 2024.1, 2026-09-30, arrow keys top to bottom): "Arrows follow correct order" — reading order matches the visual order; nothing on the page relies on position or shape alone.
- O17 [finding:V-F2] (reviewer decision 2026-09-30): The password field's accessible name "Password Show password" (O10, O13, O14) is a **Minor finding**: the field announces the neighbouring checkbox's label as part of its own name. → V-F2 (4.1.2).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30.** No outcome written here — every no-vision row is answered from the reviewer's JAWS walk (testing-tools.md: JAWS is always reviewer-driven). The AX recon above tells the walk where to listen: the password field's name, the disabled Sign in button (JAWS should say "unavailable"), the empty alert region (does a failed sign-in announce?), the logo alt.

## Evidence files in this folder

- (screenshots/exports named R050-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
