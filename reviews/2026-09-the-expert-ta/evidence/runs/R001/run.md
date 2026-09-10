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
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O8 recorded with proposed classifications; each needs reviewer confirm/dismiss before W1 can pass |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O9 (bypass) → no-vision NV / keyboard checks on S1; O10 (⋮ glyph contrast, nonBmp) → low-vision run, measure by eyedropper |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check against the JAWS walk of S1 when it happens: axe reports 0 headings / 0 landmarks, matching the DOM and AX-tree probes of 2026-09-10 — expected to be real, not instrument-blindness (no shadow DOM, no canvas) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [new] (state: Class Management, standard mode, class "Testing Course for CSU East Bay" selected): axe `label` (critical) — the two DevExpress combo-box inputs (Classes `#MainContent_cbClasses_I`, Class Menu `#MainContent_lbClassLBMenu_lbMenu_I`) have no label, title, placeholder or ARIA name. Matches the AX-tree probe (2 unnamed textboxes). Visible captions "Classes" / "Class Menu" are styled `<b>` text, not associated.
  - Proposed: W1 / WCAG 1.3.1 + 4.1.2 (A) / Major — confirm with JAWS (what is announced on focus?) → finding
- O2 [new] (state: as O1): axe `aria-command-name` (serious) — `#top_of_page_jump_point` is a `div role="button" tabindex="0"` with no accessible name (the vendor's "focus box" jump point, also present on this page). Its instruction text is inside the element but hidden from the name computation.
  - Proposed: W1 / WCAG 4.1.2 (A) / Minor–Major depending on what JAWS says on focus — confirm in the JAWS run (it may announce the inner text as content)
- O3 [new] (state: as O1): axe `aria-hidden-focus` (serious) — the header logo link `a[href="http://theexpertta.com/"]` is `aria-hidden="true"` yet focusable; keyboard users tab to an element AT does not announce.
  - Proposed: W1 / WCAG 4.1.2 (A), 2.4.3 / Minor — confirm with a Tab walk + JAWS (silent stop?)
- O4 [new] (state: as O1): axe `color-contrast` (serious), ancestor background resolved to #FFFFFF so the numbers are reliable per testing-tools.md: "Classes" and "Class Menu" captions #48848C on white = **4.23:1** (16 px bold — not large text, needs 4.5:1); "Class Assignments" #EFBB75 on white = **1.74:1**; "Class News" #E58F65 on white = **2.48:1**; Class News body text #808080 on white = **3.94:1**.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Major (section captions are the page's only visual structure) — confirm by eyedropper in the low-vision run, then → finding
- O5 [new] (state: as O1): axe `landmark-one-main` + `region` (moderate, best-practice tags) — no `main`, no landmarks; all 28 content nodes outside any region. Consistent with the exploration probes on every view.
  - Proposed: W1 / WCAG 1.3.1 / 2.4.1 supporting evidence (best-practice rule, not itself an SC failure) — fold into the structure finding from the JAWS run rather than raise alone
- O6 [new] (state: as O1): axe `page-has-heading-one` (moderate, best practice) — no headings at all on the page ("Classes", "Class Menu", "Class Assignments", "Class News" are bold text).
  - Proposed: W1 / WCAG 1.3.1 (A) (visual headings not programmatic) / Major for no-vision — confirm with JAWS H key (expect "no headings") → finding
- O7 [new] (state: as O1): DevExpress assignment grid is a `<table>` with an "Actions"-less first column; row action menu opens on cell click (`actionMenu(...)` on `div`s) — not reported by axe (no violation) but the AX-tree probe shows the row cells are plain `cell`s with no button/menu semantics.
  - Proposed: route to the no-vision and motor runs on S1 (NV: can the action menu be reached/opened by keyboard at all in standard mode?) — recon, not a finding
- O8 [new] (state: as O1): passes 33 / inapplicable 51 recorded in `R001-axe.json`; no `image-alt` violation (header logo image has alt), `html-has-lang` passes (`lang="en"`).
  - dismissed: informational
- O9 [new] (state: as O1): axe **incomplete** `bypass` — no skip link / landmarks / headings detected; axe cannot decide. The vendor's focus-box jump points may be the intended bypass.
  - Proposed: W2 → no-vision run on S1 (2.4.1): is the first Tab stop a usable "skip"?
- O10 [new] (state: as O1): axe **incomplete** `color-contrast` on the row action-menu glyph "⋮" (`nonBmp` — axe skips non-BMP glyphs).
  - Proposed: W2 → low-vision run, measure the glyph by eyedropper (1.4.11 if treated as a control icon, 1.4.3 if text)

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

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
