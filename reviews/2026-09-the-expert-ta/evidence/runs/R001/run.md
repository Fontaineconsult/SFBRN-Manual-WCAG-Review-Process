# Test Run R001 — S1

| | |
|---|---|
| **Run ID** | R001 |
| **Date/time** | 2026-09-10 10:33 |
| **View / sample** | S1 |
| **Page URL / location** | https://dei56mo.theexpertta.com/common/default.aspx |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 151 debug profile); classification pending reviewer |
| **Result** | Works with issues |

**Result reasoning.** 2026-09-17, triage closed. Every axe violation is now either a confirmed finding (V-F1, V-F7, V-F8, V-F23, V-F29, T1-F3) or dismissed with a written reason, and every `incomplete` is answered. "Works with issues" describes the **sweep**, not the page — the page itself is Broken without vision (R015). The sweep penetrated: axe's structure output agrees with what NVDA found (W3), so its zero-headings result is real, not instrument-blindness.

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | pass | O1–O8, closed 2026-09-17 against the walks that have since happened: O1→V-F7, O2→V-F8, O4→V-F23, O5/O6→V-F1, O7→T1-F3 (all confirmed by the reviewer on R015/R019); O3→V-F29 (measured, O11); O8 dismissed as informational |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O9 (bypass) answered by the NVDA walk — R015 O9: the first Tab stop is instruction text, not a skip, and R015 O6 finds no landmark or heading route; O10 (⋮ glyph contrast) measured 2026-09-17 by pixel sampling → O12, 21:1, pass |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | pass | Cross-checked 2026-09-14 against the **NVDA** walk (R015 — the reviewer's own AT; no JAWS walk of S1 exists): axe reports 0 headings / 0 landmarks and NVDA finds none either (R015 O6 — `H` no heading, `D` no landmark, NVDA+F7 no route). Instrument and AT agree, so the structure output stands and the sweep is not instrument-blind |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [new] (state: Class Management, standard mode, class "Testing Course for CSU East Bay" selected): axe `label` (critical) — the two DevExpress combo-box inputs (Classes `#MainContent_cbClasses_I`, Class Menu `#MainContent_lbClassLBMenu_lbMenu_I`) have no label, title, placeholder or ARIA name. Matches the AX-tree probe (2 unnamed textboxes). Visible captions "Classes" / "Class Menu" are styled `<b>` text, not associated.
  - Classified: W1 / WCAG 1.3.1, 4.1.2 / Major → **V-F7**, confirmed 2026-09-14 by the reviewer's NVDA walk (R015 O8: each editor announces a long instruction sentence and no label; the purpose is first heard on the adjacent Go button)
- O2 [new] (state: as O1): axe `aria-command-name` (serious) — `#top_of_page_jump_point` is a `div role="button" tabindex="0"` with no accessible name (the vendor's "focus box" jump point, also present on this page). Its instruction text is inside the element but hidden from the name computation.
  - Classified: W1 / WCAG 4.1.2 / folded into **V-F8**, confirmed 2026-09-14 (R015 O9: the jump point "reads exactly what is in the div" — its instruction text as content, no control name)
- O3 [new] (state: as O1): axe `aria-hidden-focus` (serious) — the header logo link `a[href="http://theexpertta.com/"]` is `aria-hidden="true"` yet focusable; keyboard users tab to an element AT does not announce.
  - Classified: W1 / WCAG 4.1.2 / Minor → **V-F29**, confirmed 2026-09-17. Both halves are now evidenced: it **is** in the keyboard tab order (O11 — stop 8, measured with real dispatched Tab keys) and it **is** hidden from the AT (the reviewer's NVDA links list was empty, R015 O13, because the whole subtree is `aria-hidden`). Severity is the reviewer's to confirm → W71
- O4 [new] (state: as O1): axe `color-contrast` (serious), ancestor background resolved to #FFFFFF so the numbers are reliable per testing-tools.md: "Classes" and "Class Menu" captions #48848C on white = **4.23:1** (16 px bold — not large text, needs 4.5:1); "Class Assignments" #EFBB75 on white = **1.74:1**; "Class News" #E58F65 on white = **2.48:1**; Class News body text #808080 on white = **3.94:1**.
  - Classified: W1 / WCAG 1.4.3 / Major → **V-F23**, confirmed by the reviewer's eyedropper 2026-09-15 (R019 O6: teal captions 4.23:1, orange "Class Assignments" 1.74:1, grey news text 3.94:1 — the axe numbers held)
- O5 [new] (state: as O1): axe `landmark-one-main` + `region` (moderate, best-practice tags) — no `main`, no landmarks; all 28 content nodes outside any region. Consistent with the exploration probes on every view.
  - Classified: W1 / WCAG 1.3.1 supporting evidence → folded into **V-F1**, confirmed 2026-09-14 (R015 O6). Not raised alone — `landmark-one-main` and `region` are best-practice rules, not SC failures in themselves
- O6 [new] (state: as O1): axe `page-has-heading-one` (moderate, best practice) — no headings at all on the page ("Classes", "Class Menu", "Class Assignments", "Class News" are bold text).
  - Classified: W1 / WCAG 1.3.1 / Major → **V-F1**, confirmed 2026-09-14 (R015 O6: `H` finds no heading on the page — the prediction held)
- O7 [new] (state: as O1): DevExpress assignment grid is a `<table>` with an "Actions"-less first column; row action menu opens on cell click (`actionMenu(...)` on `div`s) — not reported by axe (no violation) but the AX-tree probe shows the row cells are plain `cell`s with no button/menu semantics.
  - Classified: routed and answered → **T1-F3**. R015 O10: nothing in the row is focusable, Enter/Space/Applications do nothing, "only way to nav is by clicking the table row"; R015 O12: the mouse-opened menu is not announced. The recon question is settled — the menu is pointer-only
- O8 [new] (state: as O1): passes 33 / inapplicable 51 recorded in `R001-axe.json`; no `image-alt` violation (header logo image has alt), `html-has-lang` passes (`lang="en"`).
  - dismissed: informational
- O9 [new] (state: as O1): axe **incomplete** `bypass` — no skip link / landmarks / headings detected; axe cannot decide. The vendor's focus-box jump points may be the intended bypass.
  - Classified: W2, answered 2026-09-14 → R015 O9: the first Tab stop reads the visually hidden instruction div in full — instruction text, not a skip mechanism; no landmark or heading route either (R015 O6). The jump points are not a bypass
- O10 [new] (state: as O1): axe **incomplete** `color-contrast` on the row action-menu glyph "⋮" (`nonBmp` — axe skips non-BMP glyphs).
  - Classified: W2, measured 2026-09-17 → O12: **21:1**, pass on both readings (1.4.3 and 1.4.11). The reviewer's eyedropper pass had left it unmeasured (R019 O7)

- O11 [measured] (state: Class Management standard mode, as loaded, 2026-09-17; real `Input.dispatchKeyEvent` Tab presses from the top of the document — never `.focus()`, which bypasses the app's own key handling): the header logo link **is** a real keyboard stop. Tab order: 1 the hidden instruction div, 2 theExpertTA.com, 3 My Account, 4 Log Out, 5 Class Management, 6 Instructor, 7 Help, **8 `<a href="http://theexpertta.com/">` wrapping `ETA_LogoForWeb_White.png` (alt "The Expert TA"), inside `aria-hidden="true"`**, then the page's own controls. A keyboard user lands on it; because the subtree is `aria-hidden` the AT is given nothing there — not even the img's alt. Confirms axe O3, and matches the reviewer's empty NVDA links list (R015 O13). Product-wide: the same header is on every signed-in view (PW-C).
  - Classified: W1 / WCAG 4.1.2 / Minor → **V-F29**
- O12 [measured] (state: as O11, 2026-09-17; **pixel sampling**, not ancestor-walking): the assignment row's ⋮ action-menu glyph (`div.actionMenu#divActionMenu17547`, 16×16 px) renders as solid black dots — ink `rgb(0,0,0)` on a sampled background of `rgb(255,255,255)` = **21:1**. The method matters here: the element's computed background is `rgba(0,0,0,0)`, exactly the transparent case where walking ancestors invents a white background and a fictional 21:1, so the number is taken from the rendered pixels of a ×10 screenshot (`R001-glyph-contrast.png`), in which the dots are visibly black on white. The two grid expand glyphs measure the same. This answers the `nonBmp` incomplete that axe could not evaluate.
  - Classified: W2 / WCAG 1.4.3, 1.4.11 / **pass** — no finding

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, injected into the signed-in debug-profile tab at 2026-09-10 17:33 UTC.
Counts: violations 7 (rules), incomplete 2, passes 33, inapplicable 51. Page state: standard (non-accessibility) mode; one assignment row; roster empty.
Contrast numbers in O4 come from axe with an opaque ancestor background (#FFFFFF) found — reliable per testing-tools.md; the ⋮ glyph (O10) is unmeasured.
The same page in Accessibility Mode (S2) is a different DOM and needs its own sweep — not done this session (session invalidated, see 03 §2.6).

## Evidence files in this folder

- `R001-axe.json` — raw axe output (280,808 bytes)
- `R001-glyph-contrast.png` — ×10 screenshot of the ⋮ action-menu glyph, the pixels O12's 21:1 is sampled from

## Findings raised from this run

- **V-F29** (new, 2026-09-17) — the `aria-hidden` header logo link is a keyboard stop with nothing announced (O3 + O11).
- Confirmed elsewhere and evidenced by this sweep: **V-F1** (O5, O6), **V-F7** (O1), **V-F8** (O2), **V-F23** (O4), **T1-F3** (O7).
- Dismissed: O8 (informational). Measured pass: O12 (⋮ glyph 21:1).
