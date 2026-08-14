# Test Run R014 — S3

| | |
|---|---|
| **Run ID** | R014 |
| **Date/time** | 2026-08-06 15:35 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | — |
| **Result** | Works with issues |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes | fail | O1 → V-F10 (real); **O2 → 4 contrast violations DISMISSED as false positives**; O3 best-practice, dismissed as findings |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | pass | O4, O5 routed; O6 video-caption assessed |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) | partial | O7 — axe penetrated the DOM, but is **wholly blind to the canvas**, which is this view's principal risk |

## Observations

axe-core 4.10.3, full ruleset, on the authenticated S3 editor ("Text Test"
document). **violations 7, incomplete 3, passes 43, inapplicable 42.** Raw
output: `R014-axe.json` (4.41 MB — the editor is 3,971 elements across 960
open shadow roots, roughly double S1).

Triaged 2026-08-06. **Only 2 of the 7 violations survive triage**: four are
best-practice rules that are not WCAG criteria, and one — the
`color-contrast` group — is a demonstrated **false positive**.

- O1 [classified] (violation `aria-command-name`, serious, **wcag2a
  wcag412**): `<sp-button id="more-menu-button"
  data-testid="page-nav-more-menu-button">` inside `x-mini-page-navigation`
  — the editor's **page-navigation "more" menu button** — has no accessible
  name by any mechanism (no text, no `aria-label`, no `aria-labelledby`, no
  `title`).
  - **A different control from V-F4.** V-F4 is the community icon in the
    shared home header; this is an editor-specific control on the page
    navigation. Same rule, same criterion, different component and view.
  - Classified: W1 / WCAG 4.1.2 / Major → **new finding V-F10**. Reviewer
    confirmation by ear is still wanted in the S3 no-vision run — S1's
    experience showed axe and NVDA agreeing on names, but also showed an
    elements-list rendering that nearly produced a false finding (R012 O9).
- O2 [**DISMISSED — false positives, all 4 nodes**] (violation
  `color-contrast`, serious, wcag2aa wcag143): axe reported the editor
  header text as failing catastrophically — the "Adobe Express" app name at
  **1.08:1** and the document title at **1.14:1**, both against a claimed
  background of `#e9e9e9`.
  - **Verified and refuted by rendered-pixel sampling** (the documented
    method for this case, testing-tools.md §zoom case 3): a CDP
    `Page.captureScreenshot` sampled at the text positions gives the real
    painted background as **`rgb(29,29,29)`** — the dark header — not
    `#e9e9e9`. Measured contrast: **app name 15.06:1**, **document title
    12.18:1**. Both pass comfortably.
  - **Why axe got it wrong, and why this matters beyond these four nodes:**
    an ancestor walk from these elements finds **no opaque background at
    all** (confirmed independently). Rather than reporting *incomplete* —
    which is what it does elsewhere in this app for exactly this
    situation (R009 O4, R011) — axe substituted an assumed background and
    emitted confident numeric **violations**. A reviewer copying axe output
    into the ACR would have recorded two fabricated serious 1.4.3 failures
    against the vendor.
  - **Distinguishing signal, now recorded as process guidance:** axe's
    contrast numbers are trustworthy when the background is DOM-resolvable
    (S1's `.browse-text` 3.96:1 was independently corroborated, R002 O2 /
    R009 O1) and **untrustworthy when it is not**. Check the ancestor walk
    before believing a contrast violation on this product.
  - Dismissed: measurement error by the instrument, not a product defect.
- O3 [dismissed as findings, substance retained] (violations
  `landmark-one-main`, `page-has-heading-one`, `region` (21 nodes),
  `landmark-no-duplicate-banner`, `landmark-unique` — **all tagged
  best-practice, none a WCAG criterion**):
  - **`landmark-one-main`: the editor has NO `main` landmark.** This
    confirms the exploration prediction (03 §2.6) from an independent
    instrument. Not a WCAG failure by itself — but it removes the basis of
    the **V-F3 amendment**, which narrowed 2.4.1 to keyboard-only users
    precisely because S1's `main` gave screen-reader users an ARIA11
    bypass. **That reasoning does not transfer to S3.** Do not inherit S1's
    2.4.1 scope here; re-test under MO11/NV2.
  - `page-has-heading-one`: no `h1` — also as predicted. Headings start at
    `h2` ("Untitled…", "Daniel Fontaine", "Canvas", "Search").
  - `region`: **21 nodes** of content outside any landmark, including the
    header brand, the asset-panel heading container, and the content search
    input. Far worse than S1 (4 nodes). Feeds NV2 in the manual run.
  - `landmark-no-duplicate-banner` / `landmark-unique`: the asset panel
    contains a second `<header>`, giving the document two unlabelled banner
    landmarks. Feeds NV2.
  - Dismissed as findings (best-practice tags); all five routed as evidence
    into the S3 no-vision run.
- O4 [classified] (incomplete `aria-allowed-attr`, critical, wcag412):
  `aria-orientation="vertical"` on `x-asset-category-select`. **Same class
  of defect as S2's `x-masonry`** (R011 O1), where `aria-orientation` on
  `role="row"` was an outright violation; here axe is unsure whether the
  attribute is merely ignored. Routed to NV3.
- O5 [classified] (incomplete `aria-valid-attr-value`, critical, 2 nodes):
  `aria-controls` targets that cannot be resolved while closed — the account
  button (**third view running**, shared header) and the editor's content
  search input (`aria-controls="search-results-menu…"`). Routed; resolve
  once by opening each.
- O6 [classified] (incomplete `video-caption`, critical, **wcag2a
  wcag122**): a `<video muted loop playsinline>` in the asset panel's search
  row — a **silent auto-looping preview thumbnail**, not user-facing media
  with an audio track.
  - Assessment: captions under 1.2.2 apply to prerecorded *synchronized
    media*; a muted decorative preview with no audio track is very likely
    out of scope. **Not raised.**
  - **But it confirms the scouting call that S3's no-hearing cell must not
    be N/A** (03 §2.6). The live question is not this preview — it is the
    **Videos, Music and Sound effects assets a user can insert into a
    document**, which are real media and were not exercised by this sweep.
    Plan a genuine no-hearing run for S3.
- O7 [classified] (W3 instrument sanity — **the most important limitation of
  this run**): axe traversed the editor's DOM and shadow roots fine, and its
  structural picture (no `main`, no `h1`, two banners) matches the
  exploration probe. **But it reported nothing whatsoever about the
  canvas** — no violation, no incomplete, not even an inapplicable note.
  - That is expected and is the point: `<canvas>` content is opaque to
    automated checkers. The editor paints the entire user document into one
    2328×1145 canvas with no `role`, no `aria-label` and no fallback
    children, and the visible "Text Test" element appears nowhere in the DOM
    (03 §2.4).
  - **So the single largest accessibility risk on this view is invisible to
    the sweep.** A clean-looking automated result here would mean nothing.
    43 passes must not be read as reassurance. Everything that matters on
    S3 rests on the manual no-vision run.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R014-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
