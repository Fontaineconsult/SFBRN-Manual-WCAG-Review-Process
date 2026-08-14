# Per-Criterion Results — Adobe Express

The criterion-level **rollup** of the findings recorded in
`04-task-testing.md`. One block per WCAG 2.2 success criterion, grouped like
VPAT 2.5 WCAG-edition tables, so this file renders directly into ACR format.

Do not record new findings here — record them in `04-task-testing.md` and cite
their IDs in **Task findings** (e.g., `T1-F1, V-F3`). The **Outcome** must be
consistent with the cited findings: a criterion with a Blocker/Major finding on
essential functionality is at most Partially Supports; with no findings and
relevant content tested, Supports.

**Outcome vocabulary (ACR terms):**

- **Supports** — the functionality of the product has at least one method that meets the criterion without known defects or meets with equivalent facilitation.
- **Partially Supports** — some functionality of the product does not meet the criterion.
- **Does Not Support** — the majority of product functionality does not meet the criterion.
- **Not Applicable** — the criterion is not relevant to the product.
- **Not Evaluated** — not yet tested (initial state; must not remain in a final report).

For each criterion record: the **Outcome**; the **Vendor claim** (from their
ACR, `02-vendor.md`); **Task findings** (IDs from `04-task-testing.md` — which
tasks and views failed this criterion); and **Remarks** (what was tested, on
which sample items, with which tool/method — evidence lives with the findings).

---

## Vendor evidence gap — the ACR is a WCAG 2.1 document (recorded 2026-08-06)

This is a property of the vendor's evidence, not a test result, and it bears
on procurement independently of anything found on any view.

The conformance target for this review is **WCAG 2.2 Level AA** (03 §1.2) —
55 A/AA criteria. The vendor's report
(`vendor-acr/adobe-express-webapp-2023-acr.html`, dated 2023) contains
**exactly 50 criteria**, and the arithmetic identifies it exactly:

| | Count |
|---|---|
| Criteria in scope (WCAG 2.2 A + AA) | 55 |
| Criteria the vendor claims | 50 |
| — of which obsolete: **4.1.1 Parsing**, removed in WCAG 2.2 | 1 |
| **Vendor claims that bear on an in-scope criterion** | **49** |
| **In-scope criteria with no vendor claim of any kind** | **6** |

50 − 1 obsolete + 6 new = 55. The gap is not arbitrary: the six unclaimed
criteria are exactly the six added in WCAG 2.2 —

- **3.2.6 Consistent Help** (A)
- **3.3.7 Redundant Entry** (A)
- **2.4.11 Focus Not Obscured (Minimum)** (AA)
- **2.5.7 Dragging Movements** (AA)
- **2.5.8 Target Size (Minimum)** (AA)
- **3.3.8 Accessible Authentication (Minimum)** (AA)

**Why it matters for the decision.** For roughly 11% of the standard being
procured against, the vendor has asserted nothing — so there is no claim to
verify, and no vendor position to hold them to later. These six are also not
a random slice: they are the criteria WCAG 2.2 added to protect **motor and
cognitive** users specifically (drag alternatives, target size, not
re-typing data, authentication that is not a memory test). A reviewer
reading only the ACR would see a document that looks complete and would not
notice the omission — the criteria simply are not listed.

**Consequence for this review:** every one of the six requires independent
primary evidence; none can be resolved by verifying a claim. Two are
already resolved on S1 by direct measurement (2.5.8 → Supports, R004 O4;
2.4.11 partially, via LV7/MO4). This is not a finding against the product —
an ACR is properly dated to the standard it was written against — but the
report must state that the vendor's evidence does not reach the target
standard, rather than presenting 50 claims as full coverage.

---

## Table 1: Success Criteria, Level A

### 1.1.1 Non-text Content (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F7, T1-F2
- **Remarks:** **The two tested views fail this criterion in opposite directions**, which is worth stating plainly in the report. **S2 is the serious one:** walking graphics with `G` finds **no graphics at all** on a view built entirely from template thumbnails (R013 O12). Those thumbnails are informative — with no accessible name on the grid items (T1-F2), the picture is the only thing distinguishing one template from another — yet they are absent from the accessibility tree, so there is no alternative to hear and nothing to attach one to. **S1 is the mild one:** card graphics announce as "Clickable Figure {name}, **Unlabeled Graphic**" (R012 O14, reviewer, NVDA 2026.1.1) — the figure supplies the meaningful alternative but the inner image is neither given an alternative nor marked decorative, so an unnamed graphic is announced on every card. Verbosity rather than lost information → Minor. **Agrees with the vendor's own claim**, including the specific wording of their exception ("The decorative image is not hidden from screen readers"), which they attribute to another screen; it occurs on S1 too. Separately confirmed *not* a defect on S1: the Recent-file card link carries its name in an `sr-only` span and its thumbnail has proper alt (R009 O7 — an earlier recon suspicion, refuted). Pending S2/S3/S4.

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.2 Captions (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.1 Info and Relationships (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F9, V-F11, T1-F2
- **Remarks:** Splits sharply by view. **S1 passes** — heading outline and landmarks confirmed by two independent screen readers and Chrome's tree (R012 O5/O7). **S2 fails** on both counts: only two headings, "Explore" and "Filters", and those mis-levelled (V-F9, corroborated by axe `heading-order`, R011 O3); and the template grid conveys neither its own boundaries nor its items' structure (T1-F2). **Root cause now identified and specific:** the grid container is `<x-masonry role="row">` with **no required parent** — axe `aria-required-parent`, critical, mapped to wcag131: *"Required ARIA parents role not present: grid, rowgroup, table, treegrid"* (R011 O1). An orphaned `row` supplies no structure for an AT to navigate, which is why arrow-key movement through the grid is silent and item boundaries are imperceptible (R013 O5). Two instruments agree, and the reviewer's session predates the axe triage, so this is corroboration rather than confirmation bias. **Product-wide as of 2026-08-10 (V-F11):** counting every sampled view, **17 of 18 grids carry no accessible name** (the sole exception being the editor's layers list), and `role="grid"` is applied to horizontal card carousels that have no row/column relationship — so grouping that exists is unnamed while tabular structure that does not exist is asserted. Orphaned `role="row"` elements (no grid/table/rowgroup ancestor) occur on S1, S2 and S4 as well, making the S2 root cause a product-wide pattern rather than one broken component. Remediation is cheap and worth stating in the report: each section already has an exposed adjacent heading, so one `aria-labelledby` per grid would fix the naming half. Agrees with the vendor's own claim. Pending S4 modality runs.

### 1.3.2 Meaningful Sequence (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.3 Sensory Characteristics (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** T1-F2
- **Remarks:** **Below the vendor's claim of Supports.** S1 passes — reviewer confirmed nothing on the home dashboard is conveyed by position, shape or size alone (R012, NV8). S2 does not: template grid items carry no accessible name, so the *only* thing distinguishing one template from another is its visual thumbnail (T1-F2, R013 O7). A user choosing a template is being asked to rely on a purely visual characteristic. Third criterion where independent testing lands below Adobe's own assessment (with 2.4.2 / V-F8 and 1.4.13 / V-F1). Pending S3/S4.

### 1.4.1 Use of Color (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:** S1 grayscale pass (R003) — selected states and badges survive; NC2 observation open (link hover/focus cues to confirm). Other views pending.

### 1.4.2 Audio Control (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.1.1 Keyboard (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F14
- **Remarks:** Extensively exercised under B2 (physical keyboard, NVDA off, 2026-08-13): S1's full 33-stop traversal is reachable and operable (R004 O5); document creation, renaming, text authoring and canvas **translation and z-order** all work by keyboard (R016, R029, R031). The confirmed failures: **rotation (any object) and resize of non-text objects are pointer-drag only** (V-F14, broadened 2026-08-13) — for shapes and images "only translate is available"; text resizes via the Edit panel (whose +/− steppers announce no value — the feedback pattern again). And on S4, **the file-card checkbox does not respond to the Space bar** (V-F12 extended, R033 O1), making bulk file selection keyboard-unavailable. Also relevant: an earlier assistant Blocker claim against this criterion ("editing is pointer-only") was **withdrawn** when the reviewer found the keyboard route (R015 O7) — the surviving 2.1.1 failure is rotation, narrowly scoped. Narrower than the vendor's blanket Does Not Support.

### 2.1.2 No Keyboard Trap (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.1.4 Character Key Shortcuts (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** V-F15
- **Remarks:** **Settings checked 2026-08-13 (R031 O7): no keyboard-customization options exist.** The editor's "T" shortcut (creates a text box) can be neither disabled nor remapped; the focus-scoping defense is implausible since the canvas cannot receive focus (R015 O2). The criterion's entire subject matter — character-key shortcuts — fails, hence Does Not Support. **Fifth criterion verified worse than the vendor's claim** (Supports claimed). Also recorded: shortcut documentation and implementation out of sync in both directions (documented rename shortcut broken; working shortcuts undocumented — R031 O2/O6).

### 2.2.1 Timing Adjustable (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.2.2 Pause, Stop, Hide (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): nothing moving, blinking or auto-updating on any view (also instrumented: 0 animations page-wide at 68s, R010 O1). The once-suspected rotating placeholder is static in steady state and hidden from AT. Load-window rotation, if any, is under 5s after dozens of observed loads. Agrees with vendor.

### 2.3.1 Three Flashes or Below Threshold (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.1 Bypass Blocks (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** V-F3
- **Remarks:** S1: **reviewer-confirmed with a physical keyboard 2026-08-13 (R004 O5): no skip link; 19 Tab stops to the left rail, 33 to the Recent strip** — the earlier assistant caveat is resolved and the vendor's *Supports* is contradicted by direct test. Screen-reader users bypass via landmarks on S1 (ARIA11, confirmed in both JAWS and NVDA) and in the editor via its region landmarks ("Edit page", "Canvas", "Allows for adding and deleting pages" — R015 O11; no `main` element, but regions are navigable). REVIEWER DECISION still open in name — though the evidence now firmly supports keeping the failure for keyboard-without-AT users: keep as Does Not Support, or reclassify Supports + advisory. Outcome stands as Does Not Support.

### 2.4.2 Page Titled (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F8
- **Remarks:** **Product-wide, not view-specific.** The document title is "Adobe Express" on every SPA view and never changes on navigation — reviewer-confirmed with NVDA 2026.1.1 across views, and independently corroborated by reading `document.title` on Home (S1), Explore (S2), Your stuff (S4) and Brands: **4 views, 1 distinct title**. An opened document *does* retitle, so the capability exists and is simply unused for the main views. Outcome is **worse than the vendor's claim**: "Partially Supports" implies some views are titled adequately, but no view in the sample is distinguishable by title, so the majority of product functionality does not meet the criterion. This is one of the two criteria found so far where independent testing lands *below* Adobe's own assessment (the other is 1.4.13 / V-F1). Note the methodological point for the report: this defect is invisible to a per-view sweep and to every automated checker — each view has *a* title; only comparing views exposes it.

### 2.4.3 Focus Order (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** T1-F1, T1-F2 (V-F6 was raised and withdrawn — see 04)
- **Remarks:** Splits by view, and the split is instructive. **S1 passes everything tested** (R012 O8/O13): the "Get started" modal moves focus in on open, contains it correctly (Tab cycles modal → browser chrome → modal, never into the page behind), and closes on `Esc`. **S2 fails twice** during task T1: navigating Home → Explore leaves focus stranded on the rail button while the whole view is replaced (T1-F1), and inside the template grid each item costs four tab stops with its name on a different stop from the item, after which focus leaves the grid unannounced (T1-F2). So the vendor's blanket "Does Not Support" is too harsh for S1 and well-earned on S2. Still unrun: **MO5 — systematic focus-order walk with a physical keyboard** (R004, baseline B2); these findings all come from a screen-reader session. Pending S3/S4.

### 2.4.4 Link Purpose (In Context) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.1 Pointer Gestures (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.2 Pointer Cancellation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.3 Label in Name (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.4 Motion Actuation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.1.1 Language of Page (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.1 On Focus (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): no unexpected context changes on focus anywhere across four views and all sessions. Agrees with vendor.

### 3.2.2 On Input (Level A)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): no unexpected context changes on input; filter/search inputs change results only (their *silence* is the separate 4.1.3 pattern, not a context change). **Better than the vendor's Partially Supports.**

### 3.2.6 Consistent Help (Level A)
- **Outcome:** Supports
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): help ('?') appears in a consistent location on every view. **Independent primary evidence — one of the six WCAG 2.2 criteria absent from the vendor ACR.** Help *content* (C7) still unopened — location consistency is what 3.2.6 requires.

### 3.3.1 Error Identification (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.2 Labels or Instructions (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.7 Redundant Entry (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 4.1.2 Name, Role, Value (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F4
- **Remarks:** S1: header community button has no accessible name — **reviewer-confirmed 2026-08-06 with NVDA 2026.1.1 (R012 O1)**, corroborated by Chrome's accessibility tree and axe-core (R009). Extent on S1 is now established and is **narrow**: exactly one control of 48 exposed interactive nodes. The worse hypothesis — systemic mis-mapping of Spectrum web components to the platform API — was tested and refuted, so the vendor's blanket "Does Not Support" looks materially harsher than S1 warrants. Still pending: aria-controls target existence on "More apps" and account-button state toggling (R009 O5, W5); JAWS behaviour on this control is untested (R001 suspended when testing moved to NVDA — see 03 §1.3). **Extent across views now established (2026-08-13):** S3 adds the page-nav "more" button (V-F10), the unlabelled floating text toolbar and the unnamed edit textarea (R015), the create chooser's six unnamed category tabs' options (T2-F1); S4 adds the per-card checkbox and action button (V-F12, reviewer-confirmed). The defects are specific, recurrent, and all of the same cheap-to-fix class — missing accessible names on custom controls — rather than systemic component mis-mapping (R012 O1 refuted that). Outcome stays Partially Supports.

---

## Table 2: Success Criteria, Level AA

### 1.2.4 Captions (Live) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.5 Audio Description (Prerecorded) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.4 Orientation (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.5 Identify Input Purpose (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.3 Contrast (Minimum) (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F2
- **Remarks:** S1: "browse" link 3.96:1 at 11px — confirmed by two independent instruments (computed sample R002; axe-core violation R009, same node). **Updated 2026-08-06:** the 15 axe-*incomplete* nodes were not one "gradient" group and are now 8 resolved / 7 open. The Adobe app bar is an SVG image, not a CSS gradient (which is why both instruments returned "indeterminate"); re-rendering that self-contained SVG same-origin on a canvas and sampling it gives all 8 labels **11.18:1–11.71:1 — pass** (R009 O8 / R002 O6). Still open: 4 start-card `h2`s + 1 row `h2` over card art (colour painted by a pseudo-element/non-hit-testable image — ancestor-walking returns a false 21:1 and was discarded; needs rendered-pixel sampling), and 2 rotating-placeholder words. So the only *confirmed* S1 failure remains the single "browse" link. Vendor's own claim admits failure; the measured scope is so far markedly narrower than "Does Not Support" implies.

### 1.4.4 Resize Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.5 Images of Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.10 Reflow (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Measured on **all four sampled views** at a 320 CSS px viewport (CDP device emulation — the equivalence 1.4.10 itself defines; runs R002/R018/R019/R020, 2026-08-13): **zero horizontal overflow everywhere**; layouts re-stack to a single column. The editor's drawing canvas is exempt content under this criterion. **Better than the vendor's claim** — a genuine product strength worth stating. One scoped caveat, not a defect: at 320px the editor goes panel-over-canvas (asset panel covers the document); whether the canvas is *reachable* at that width is an open interactive check (R019 O1) that belongs to 1.4.4/usability rather than reflow itself. Revisit if that check fails.

### 1.4.11 Non-text Contrast (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Does Not Support (Web)
- **Task findings:**
- **Remarks:**

### 1.4.12 Text Spacing (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** S1 passes with full visual confirmation (R002 O1 screenshot + 2026-08-13 re-capture at 320px). S2/S3/S4 pass **by overflow metric** under the standard override (no layout growth, R018–R020); the visual confirmation screenshots stalled on those views — a documented instrument limit (renderer never stabilizes under global spacing injection on heavy shadow-DOM views), not a product signal. Agrees with the vendor. Downgrade only if a reviewer spot-check ever shows clipping the metric missed.

### 1.4.13 Content on Hover or Focus (Level AA)
- **Outcome:** Does Not Support
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F1
- **Remarks:** S1 left-rail hover flyout: not hoverable, not dismissible via Esc, persists stuck over content (R002, corroborated R003). Assistant-driven, pending reviewer confirmation with continuous pointer movement. Worse than vendor claim if confirmed.

### 2.4.5 Multiple Ways (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.6 Headings and Labels (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F5
- **Remarks:** S1: **headings pass** — the outline is well-formed and descriptive, confirmed independently by two screen readers (JAWS R001 O3; NVDA R012 O2/O5) and Chrome's accessibility tree: `h1` "How would you like to start?", `h2` section headings, `h3` "Recent". **Labels fail in the "Get started" modal** — ten chooser buttons share the identical accessible name "Browse templates" with nothing to distinguish them (V-F5, reviewer-confirmed with NVDA, count verified in the accessibility tree). So the criterion splits cleanly: headings good, one labelling defect in a modal state. That is materially better than the vendor's blanket "Does Not Support", but not a pass. Pending: S2/S3/S4, and whether the button→category association is programmatically determinable (would add 1.3.1).

### 2.4.7 Focus Visible (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.11 Focus Not Obscured (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 2.5.7 Dragging Movements (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** V-F14
- **Remarks:** **Independent primary evidence — no vendor claim exists** (one of the six WCAG 2.2 criteria absent from the 2023 ACR; see §Vendor evidence gap). Tested on the two drag-heavy surfaces: the upload card's drag-drop has a working non-drag alternative ("browse", B2-verified, R004 O5); canvas object **translation** has a keyboard route and **z-order** a menu route, but **rotation is drag-only with no alternative found, and the corner-drag resize has no keyboard equivalent for non-text objects** (V-F14, R031 O4/O7). The S2 masonry and S4 lists involve no dragging.

### 2.5.8 Target Size (Minimum) (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** none
- **Remarks:** S1 only — **independent primary evidence, no vendor claim to
  verify** (see §Vendor evidence gap). Full-page geometry measurement of all
  51 distinct interactive targets across the app's 303 open shadow roots
  (R004 O4, 2026-08-06, assistant): five fall under 24×24 CSS px — three
  "View all" links at 40×15, the account button at 24×24, the search input
  at 657×24. All five meet the **spacing exception**: the nearest
  centre-to-centre distance to any other target is 104 px, over 4× the 24 px
  threshold, because the undersized links sit alone beside section headings
  rather than in clusters. Measured at 2328×1145; **re-check at narrow
  widths and 400% zoom**, where reflow can pack these links against
  neighbouring controls and invalidate the spacing exception (fold into
  W10/LV1). Outcome is scoped to S1 — S2/S3/S4 untested, and the editor
  (S3) with its dense tool rails is the likeliest place for this to fail.

### 3.1.2 Language of Parts (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.3 Consistent Navigation (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): navigation consistent across S1–S4 (rail, header, ordering). Agrees with vendor.

### 3.2.4 Consistent Identification (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): components identified consistently across views. Agrees with vendor.

### 3.3.3 Error Suggestion (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.8 Accessible Authentication (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 4.1.3 Status Messages (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** T1-F2, T2-F2, V-F13
- **Remarks:** **Four independent instances across three views — a consistent product pattern, not isolated slips.** S4: changing the file filter updates the list with no announcement of any kind (V-F13, reviewer-confirmed, R029 O4). S3: inserting an image reports nothing, and **"Generate with AI"** — an asynchronous, heavily-promoted operation taking many seconds — announces no progress, completion or failure, so a screen-reader user cannot distinguish working from finished from failed (T2-F2, R016 O7). The inconsistency makes it clear-cut: the same panel announced *text* insertion ("edit selected add text") one step earlier, so the capability exists and is simply not applied to images. S2: the template grid loads results lazily on scroll and **their arrival is not announced** — combined with silent arrow navigation and unnamed items, the reviewer could find no reliable way to search the grid by ear (T1-F2, R013 O3/O8, NVDA 2026.1.1). Entering the grid region is likewise unannounced. **Confirmed a second time via the search path** (R013 O13): running a template search updates the results with no announcement of any kind — no count, no "results updated" — so a user cannot tell whether their search returned anything. S1 partial evidence is more favourable: opening the "Get started" modal announces (over-announces, R010/R012 O15) rather than staying silent. Agrees with the vendor's claim. Pending S3/S4 — the editor's autosave and export progress indicators are the next place this matters.
