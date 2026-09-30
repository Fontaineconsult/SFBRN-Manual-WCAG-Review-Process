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
- **Remarks:** **The two tested views fail this criterion in opposite directions**, which is worth stating plainly in the report. **S2 is the serious one:** walking graphics with `G` finds **no graphics at all** on a view built entirely from template thumbnails (R013 O12). Those thumbnails are informative — with no accessible name on the grid items (T1-F2), the picture is the only thing distinguishing one template from another — yet they are absent from the accessibility tree, so there is no alternative to hear and nothing to attach one to. **S1 is the mild one:** card graphics announce as "Clickable Figure {name}, **Unlabeled Graphic**" (R012 O14, reviewer, NVDA 2026.1.1) — the figure supplies the meaningful alternative but the inner image is neither given an alternative nor marked decorative, so an unnamed graphic is announced on every card. Verbosity rather than lost information → Minor. **Agrees with the vendor's own claim**, including the specific wording of their exception ("The decorative image is not hidden from screen readers"), which they attribute to another screen; it occurs on S1 too. Separately confirmed *not* a defect on S1: the Recent-file card link carries its name in an `sr-only` span and its thumbnail has proper alt (R009 O7 — an earlier recon suspicion, refuted). Pending S2/S3/S4. **Held pending a scope decision (V-F16, R037 O6, 2026-08-14):** the product's *published output* — a design shared via a `/publishedV2/` link — announces as **"canvas graphic"** and nothing else, so the whole page is non-text content with no alternative. If the reviewer scopes published output into the conformance target, this criterion moves to **Does Not Support**; it is not counted here while that scope call is open, because published pages are not among the four sampled views.

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
- **Outcome:** Not Applicable
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer determination 2026-08-14: **no audio-only or video-only content in the product.** The criterion governs media that presents information *without* a second channel — a podcast with no transcript, or a silent instructional animation with no text alternative. Express's media does not fit: **Learn's tutorial videos carry both audio and captions** (R039 O1), so they are synchronised media governed by 1.2.2/1.2.3/1.2.5 rather than by this criterion; and the asset panel's `<video>` elements are **muted decorative previews of insertable stock**, not content presenting information to the user (R014 O6, assessed out of 1.2.2 scope on the same basis). **Note the direction of the disagreement:** the vendor claims *Partially Supports*, implying such content exists and is imperfectly handled; testing finds none. **Revisit if** an audio-only feature appears — a voiceover or podcast tool would engage this immediately.

### 1.2.2 Captions (Prerecorded) (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Cursory pass 2026-08-14 (R039 O1, reviewer): **Learn's tutorial videos and insertable media both carry captions.** This closes the gap the report has flagged since the matrix completed — Learn is the one surface where 1.2.x applies to Adobe's *own published content* rather than to an authoring capability. Consistent with the rest of the caption evidence: auto-captions are available for user-inserted video (R030) and **captions survive video export** (R037 O5). **Captioning is the one media affordance this product handles consistently well**, and it is worth saying so in a report that is otherwise critical of its media story. **Basis limit, stated rather than implied:** this establishes the *presence* of caption tracks. Accuracy, synchronisation, speaker identification and sound description were **not** assessed, and the separate §504 concern stands — professionally-authored caption files cannot be uploaded, and auto-generated captions are as a class insufficient for published-content conformance. Agrees with vendor.

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Cursory pass 2026-08-14 (R039 O2, reviewer): **no audio-described video anywhere.** Captions do not satisfy this criterion — captions carry *dialogue*, whereas 1.2.3 exists to convey the *visual* information a non-sighted user cannot see. **Worse than the vendor's claim of Supports** (a seventh such criterion). **One unchecked escape route, named precisely:** 1.2.3 accepts *either* audio description **or** a full media alternative, so **if Learn provides transcripts this rises to Supports**. That was not checked in a cursory pass and is the single question that would change the outcome — it should be answered before the report goes FINAL. **Why this bites harder here than on most products:** Learn's videos teach a *visual design tool*, so their content is disproportionately visual — "drag this here, the panel looks like this" — which is exactly what audio description exists to convey. The user most in need of instruction in a canvas application is the least served by it.

### 1.3.1 Info and Relationships (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F9, V-F11, T1-F2
- **Remarks:** Splits sharply by view. **S1 passes** — heading outline and landmarks confirmed by two independent screen readers and Chrome's tree (R012 O5/O7). **S2 fails** on both counts: only two headings, "Explore" and "Filters", and those mis-levelled (V-F9, corroborated by axe `heading-order`, R011 O3); and the template grid conveys neither its own boundaries nor its items' structure (T1-F2). **Root cause now identified and specific:** the grid container is `<x-masonry role="row">` with **no required parent** — axe `aria-required-parent`, critical, mapped to wcag131: *"Required ARIA parents role not present: grid, rowgroup, table, treegrid"* (R011 O1). An orphaned `row` supplies no structure for an AT to navigate, which is why arrow-key movement through the grid is silent and item boundaries are imperceptible (R013 O5). Two instruments agree, and the reviewer's session predates the axe triage, so this is corroboration rather than confirmation bias. **Product-wide as of 2026-08-10 (V-F11):** counting every sampled view, **17 of 18 grids carry no accessible name** (the sole exception being the editor's layers list), and `role="grid"` is applied to horizontal card carousels that have no row/column relationship — so grouping that exists is unnamed while tabular structure that does not exist is asserted. Orphaned `role="row"` elements (no grid/table/rowgroup ancestor) occur on S1, S2 and S4 as well, making the S2 root cause a product-wide pattern rather than one broken component. Remediation is cheap and worth stating in the report: each section already has an exposed adjacent heading, so one `aria-labelledby` per grid would fix the naming half. Agrees with the vendor's own claim. Pending S4 modality runs. **Held pending the same scope decision as 1.1.1 (V-F16, R037 O6):** published output carries no programmatically determinable structure at all — not sparse structure, none — which would move this criterion to **Does Not Support** if published pages are scoped in.

### 1.3.2 Meaningful Sequence (Level A)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from the reviewer's screen-reader sweeps of all four views (R012 S1, R013 S2, R015/R016 S3, R029 S4, all NVDA 2026.1.1): **across every session, no content was reported as read in a nonsensical order.** Headings, landmarks, panel contents and card collections were all narrated in the order they appear. **Better than the vendor's claim.**
  **Two things this outcome is careful *not* to absorb, because they are different criteria and are already recorded elsewhere.** (1) The editor's **focus order** places the work surface at tab stop 32, behind the whole application (R015 O3) — that is **2.4.3 Focus Order**, recorded under T1-F1/T2-F4, and focus order is not reading order. (2) **Canvas objects have no representation in the accessibility tree at all** (R015 O9, T2-F4) — content that is absent has no sequence to be wrong about; that absence is recorded under 4.1.2 and 1.3.1. 1.3.2 asks whether the sequence of content that *is* exposed conveys meaning correctly, and it does.
  **The residual, named:** a full browse-mode read-through of the editor top to bottom was never performed (R015 NV5 is recorded partial for exactly this). S1, S2 and S4 were walked thoroughly; S3's chrome was walked but not read end to end.

### 1.3.3 Sensory Characteristics (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** T1-F2
- **Remarks:** **Below the vendor's claim of Supports.** S1 passes — reviewer confirmed nothing on the home dashboard is conveyed by position, shape or size alone (R012, NV8). S2 does not: template grid items carry no accessible name, so the *only* thing distinguishing one template from another is its visual thumbnail (T1-F2, R013 O7). A user choosing a template is being asked to rely on a purely visual characteristic. Third criterion where independent testing lands below Adobe's own assessment (with 2.4.2 / V-F8 and 1.4.13 / V-F1). Pending S3/S4.

### 1.4.1 Use of Color (Level A)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from checks **NC1–NC3** across all four grayscale runs (R003, R021, R022, R023). **No defect was found on any view.** Selected and status states survive grayscale everywhere through non-colour means: filled pills for the active content type, boxed rail selection, real checkmarks on filters, numeric filter counts, "In:Files" chips. S4 and S3 both close cleanly as **Works** (R023, R022). **The substantive risk is now cleared — reviewer, 2026-08-14 (R022 O2):** the canvas selected-object highlight, which the grayscale instrument could not capture at all, is *"clearly visible selected with a bounding box, edge circles for resize"* — **geometric cues, not chromatic**, which survive grayscale intact. That mattered more than any other open item on this criterion because it sits on the product's core surface: had selection been a coloured glow, 1.4.1 would have failed where users spend their time. **One minor check remains:** link hover/focus cues in grayscale on S1 and S2 (NC2 partial in R003/R021 — an instrument capture cannot produce hover states). **Downgrade trigger:** that check finding a colour-only hover cue would move this to Partially Supports. Recorded as Supports on the same basis as 1.4.12 — every measurement taken passes, and the one outstanding item is named with the instrument that closes it. **Better than the vendor's claim.**

### 1.4.2 Audio Control (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 (R039 O3) from the four completed no-hearing determinations (R024, R026, R027, R030): **the product's own interface emits no audio**, and the asset panel's video previews are **muted** (R014 O6). There is no auto-playing audio for the criterion to govern — nothing starts on load, nothing exceeds three seconds. Agrees with vendor. Note this is about the *product's* audio, not about media a user inserts, which the user controls.

### 2.1.1 Keyboard (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F14
- **Remarks:** Extensively exercised under B2 (physical keyboard, NVDA off, 2026-08-13): S1's full 33-stop traversal is reachable and operable (R004 O5); document creation, renaming, text authoring and canvas **translation and z-order** all work by keyboard (R016, R029, R031). The confirmed failures: **rotation (any object) and resize of non-text objects are pointer-drag only** (V-F14, broadened 2026-08-13) — for shapes and images "only translate is available"; text resizes via the Edit panel (whose +/− steppers announce no value — the feedback pattern again). And on S4, **the file-card checkbox does not respond to the Space bar** (V-F12 extended, R033 O1), making bulk file selection keyboard-unavailable. Also relevant: an earlier assistant Blocker claim against this criterion ("editing is pointer-only") was **withdrawn** when the reviewer found the keyboard route (R015 O7) — the surviving 2.1.1 failure is rotation, narrowly scoped. Narrower than the vendor's blanket Does Not Support.

### 2.1.2 No Keyboard Trap (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from check **MO3** across the four motor runs (B2, physical keyboard, reviewer). **Three views pass explicitly:** S1 — the "Get started" modal opens by Tab+Enter and exits on Esc (R004 O5, a B2 confirmation of the NVDA result R012 O13); S2 — templates open and exit cleanly, no traps in a full traversal (R032 O1); S4 — no traps in a full traversal (R033 O1). **S3 is a partial, and the reason is stated rather than smoothed over:** no trap was encountered in any editor session, but MO3 was not systematically swept there (R031). Given the editor is the most modal surface in the product, that is the one place a trap could still hide. Recorded as Supports because four independent sessions — three of them full traversals, plus the NVDA walks that moved in and out of edit mode repeatedly (R015, R016) — produced no trap of any kind. **Downgrade trigger:** any reviewer report of being unable to Tab or Esc out of an editor widget. Agrees with vendor.

### 2.1.4 Character Key Shortcuts (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** V-F15
- **Remarks:** **Settings checked 2026-08-13 (R031 O7): no keyboard-customization options exist.** The editor's "T" shortcut (creates a text box) can be neither disabled nor remapped; the focus-scoping defense is implausible since the canvas cannot receive focus (R015 O2). The criterion's entire subject matter — character-key shortcuts — fails, hence Does Not Support. **Fifth criterion verified worse than the vendor's claim** (Supports claimed). Also recorded: shortcut documentation and implementation out of sync in both directions (documented rename shortcut broken; working shortcuts undocumented — R031 O2/O6).

### 2.2.1 Timing Adjustable (Level A)
- **Outcome:** Not Applicable
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** **No time limit was encountered in any session across the review's ten days** — 42 runs, including reviewer sessions running long enough to exhaust a typical timeout, and a debug-profile browser left authenticated across multiple days. Nothing in the product imposes a countdown, auto-advance, or timed submission: there is no checkout, no quiz, no expiring cart, and autosave is continuous rather than deadline-driven. **Session expiry, the one candidate, belongs to the institution's SSO and is off the reviewed path** (the same scoping that puts 3.3.8 out of scope — R041 O5), and in practice SSO re-authenticated the debug profile silently rather than presenting a timed prompt.
  **Recorded as an absence observed, not as a deliberate test:** no session was run specifically to provoke a timeout. If a campus deployment configures a shorter session lifetime at the IdP, that timing behaviour is the IdP's to evaluate, not Express's. **Note the direction:** the vendor claims *Partially Supports*, implying timed content exists and is imperfectly handled; testing found no timed content at all.

### 2.2.2 Pause, Stop, Hide (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer cross-view closure 2026-08-13 (runs R010, R034–R036): nothing moving, blinking or auto-updating on any view (also instrumented: 0 animations page-wide at 68s, R010 O1). The once-suspected rotating placeholder is static in steady state and hidden from AT. Load-window rotation, if any, is under 5s after dozens of observed loads. Agrees with vendor.

### 2.3.1 Three Flashes or Below Threshold (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from the same evidence base that closed 2.2.2: **nothing flashes, blinks or strobes anywhere in the product.** Instrumented — **0 animations page-wide at 68s** on S1 (R010 O1) — and confirmed by reviewer cross-view closure across all four views (R010, R034–R036): nothing moving, blinking or auto-updating. The once-suspected rotating placeholder is static in steady state and hidden from AT. **No content in the product approaches the three-flash threshold**, which is unsurprising for a calm productivity UI, and the measurement plus four reviewer sweeps is stronger evidence than the criterion usually receives. Agrees with vendor. **Scope note:** this concerns the product's own interface. Video a user *inserts* is their content, outside the product's conformance.

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
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Measured across all four views 2026-08-14 (R042 O3): **29 visible links, 0 unnamed** — S1 2, S2 17, S3 1, S4 9. The duplicate names found (S2 "Templates"/"Photos"/"Videos" ×2; S4 "Files"/"Projects" ×2) are the same destinations surfaced in two places, which the criterion permits. Corroborated by reviewer testimony: S4's file-card **links are named and operable**, explicitly scoped as *not* part of V-F12 (R029). **Better than the vendor's claim.**
  **The precision that matters, and it protects the report from an easy rebuttal:** this product has real and repeated naming defects, but **none of them are on links.** Template grid items expose conflicting form-element/button roles (T1-F2); the ten "Browse templates" controls are `sp-button`s (V-F5); the community icon and page-nav "more" are buttons (V-F4, V-F10); layer rows are grid cells (T2-F4). Every one is recorded under **4.1.2 / 2.4.6**, where it belongs. Rolling them into 2.4.4 would double-count the same defects and hand the vendor a correction.

### 2.5.1 Pointer Gestures (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** V-F14
- **Status:** **Confirmed by reviewer ruling 2026-08-14 (R031 O8)** — no longer provisional.
- **Remarks:** Rolled up 2026-08-14 from check **MO7**, which `ontology/modality-checks.md` maps to **both 2.5.7 and 2.5.1**. MO7 passes on S1 (the upload card's drag-and-drop has a working "browse" alternative, B2-verified — R004 O5), is n/a on S2 and S4 (no drag interactions), and **fails on S3**: canvas **rotation of any object** and **resize of non-text objects** are pointer-drag only, with no keyboard or single-pointer alternative found (V-F14, R031 O4/O7).
  **The interpretive question is settled — reviewer ruling, 2026-08-14 (R031 O8).** The reviewer described how rotation is actually performed: *"pressing and holding on the rotate button on a selected object then moving the finger in an arc."* The arc **is** the input — the path travelled determines the angle — which is the defining property of a path-based gesture, so 2.5.1 is engaged rather than avoided. And the alternative does not exist: *"I've yet to see a dedicated 'Translate' tool window that would allow, using a slider, X, Y, Z or Rotate, or resize."* No angle field, no rotate-by-90° command, no stepper. The **"essential" exception fails too** — a numeric rotation field would perform the same function, so the gesture is not intrinsic to the task.
  **Three criteria, one defect, three different reasons — keep them distinct, because they have different remedies.** 2.5.1 fails for want of a *single-pointer non-path* alternative; 2.5.7 for want of a *non-dragging* alternative; 2.1.1 for want of a *keyboard* route. A properties-panel transform control with typed values closes all three simultaneously, which is what makes it the highest-leverage item in the remediation exhibit — and the reviewer's own assessment of the ask is *"low hanging fruit for the dev."*
  Note the asymmetry for the report: 2.5.7 has **no vendor claim at all** (WCAG 2.2 addition), whereas 2.5.1 is claimed **Supports** — so this is a sixth criterion verified worse than claimed. **Baseline caveat, stated rather than buried:** the touch description was made on a touchscreen, outside the four declared baselines (03 §1.3). It establishes *how the gesture works*; the outcome rests on the **absence of an alternative**, which was established under B2 (R031 O4/O7).

### 2.5.2 Pointer Cancellation (Level A)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Reviewer pointer check 2026-08-14 (MO8, R041 O6): **no down-event activation found across a large random sample of controls.** Nothing fires on press; pressing and dragging off a control before release aborts the action, which is the abort mechanism 2.5.2 requires. Agrees with vendor.
  **Worth the check rather than assuming it:** standard HTML buttons pass by default, but this product's interactive layer is built almost entirely from **custom Spectrum web components** (`sp-button`, `sp-action-button`, `x-toolbar-button`, `hz-sortable-list`) — the same component family that produced V-F4, V-F10, V-F12 and T2-F4. A custom component wiring its handler to `pointerdown` is a realistic defect, and the sample size is what makes the negative result meaningful.
  **Who this protects:** users with tremor or imprecise pointing, who rely on being able to slide off a mis-pressed control to cancel it — the same population served by 2.5.8 Target Size (also **Supports** here). Both are quiet strengths in a product whose *motor* story is otherwise mixed (V-F14 rotation, V-F12's Space-dead checkbox).

### 2.5.3 Label in Name (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F19
- **Remarks:** Measured 2026-08-14 across all four views (R042 O7) by comparing **visible text against computed accessible name** for every control carrying visible text — 64 controls; icon-only controls are out of scope, since with no visible label there is nothing for 2.5.3 to govern (their missing names are 4.1.2 / V-F4 / V-F10). **63 of 64 pass.** All **25** controls whose `aria-label` overrides the visible text — the only mechanism that can break this criterion — reproduce that text exactly ("Photos" → "photos", "Files" → "files", "Premium member" → "premium member"), so the product handles this correctly and deliberately almost everywhere.
  **One exception (V-F19, Minor):** the editor's zoom control shows only a percentage ("100%") while its accessible name is **"View options"** — no shared words, so a speech-input user saying what they see would not activate it. **An interpretive question is flagged rather than decided:** the percentage is arguably a *value* rather than a *label*, and on that reading the criterion is not engaged and the outcome rises to **Supports**. Recorded as a failure with the ambiguity stated, as 2.5.1 was before the reviewer ruled — the call is cheap either way, since the severity is Minor on both readings.
  **Also closed here:** R001 O8 raised 2.5.3 as *"a live candidate on the search field"* — that candidate is **refuted**; the search control's visible and accessible names agree. And V-F5's exclusion of 2.5.3 is confirmed by measurement: the ten "Browse templates" buttons have visible text matching their accessible name exactly, so their defect is 2.4.6 (uninformative label) and not this criterion. Agrees with vendor.

### 2.5.4 Motion Actuation (Level A)
- **Outcome:** Not Applicable
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from check **MO10**, recorded n/a on all four motor runs (R004, R031, R032, R033): the product in scope is a **desktop web application** and exposes no device-motion or device-orientation feature — nothing is operated by shaking, tilting or gesturing at the device, so there is no functionality for the criterion to govern. **Not Applicable rather than Supports**, which is the more precise term when a criterion has no relevant content (and the difference matters in an ACR-shaped record: "Supports" implies something was there and met the requirement). **Scope note that keeps this honest:** this review covers the web app only (03 §1.1). Adobe Express also ships mobile applications, where motion actuation is a live question — the vendor's "Supports" may be answering for those. Nothing here should be read as a statement about the mobile product.

### 3.1.1 Language of Page (Level A)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Measured 2026-08-14 over CDP on the clean debug profile: `<html lang="en-US">` on **S1 Home** and on **S3 the editor** — a valid, correctly-formed language tag matching the content. Adobe Express is a single-page application serving all views from one document, so S2 and S4 inherit the same root element; that is an inference from the architecture and is labelled as one rather than presented as four measurements. **Better than the vendor's claim of Partially Supports**, and the criterion is narrow enough that the measurement settles it — 3.1.1 asks only for a programmatically determinable default page language. **Not settled by this, and tracked separately:** 3.1.2 Language of Parts, which needs an audit of any passage in another language, and NV9 pronunciation, which is an ear-check no run has performed (recorded partial in R015/R016 for exactly this reason).

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
- **Outcome:** Not Applicable
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Probed 2026-08-14 (R041 O1, reviewer): *"it is not clear to me where I would produce a failure; it doesn't seem any of the functionality here would allow a wrong input."* **3.3.1 is a conditional criterion** — it applies *"if an input error is automatically detected"* — so a product that detects no input errors does not engage it. Consistent with the whole record: Express has no checkout, no multi-field forms, no required-field submissions and no validated text entry; its inputs are a search box, a document-name field, an AI prompt (all accepting any string) and a file picker. **Ten reviewer sessions and five automated sweeps have never surfaced an error message of any kind**, which had been read as a coverage gap and is better explained as an absence. **Note the direction of the disagreement:** the vendor claims *Partially Supports*, implying error identification exists and is imperfect; testing finds no error identification to assess. **One probe would firm "none found" into "none exists" and is named rather than assumed:** uploading a file the product should reject (`.exe`, `.zip`, oversized). If that produces a message, this criterion becomes live and the outcome is superseded.

### 3.3.3 Error Suggestion (Level AA)
- **Outcome:** Not Applicable
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Same basis and same conditional structure as 3.3.1 (R041 O1). 3.3.3 is triggered only where an input error *is* detected and a suggestion could be offered; no such path was found. Subject to the same upload probe — if rejection messages exist, 3.3.3 becomes live and would be the harder of the two to pass, since products commonly identify an error without suggesting the fix.

### 3.3.2 Labels or Instructions (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none new — evidence drawn from R010, R015, R016, R029
- **Remarks:** Rolled up 2026-08-14 from input-labelling evidence already on file, without a new session — 3.3.2 asks whether inputs carry labels *before* anything goes wrong, which the review has exercised extensively. **The inputs that are labelled, and they are the majority:** the S1 search control carries a stable `aria-label` (R010 O2); the editor's text-styling panel exposes combobox "Font family", combobox "Font style", textbox "Font size" and textbox "Text styles", all correctly named (R015 O4); the document-name field is reachable, labelled and operable by keyboard and NVDA, and a rename succeeded through it (R016 O4); S4's filter and scoped search are labelled (R029). **The one that is not:** the edit-mode `<textarea>` — the field carrying the user's own document content — has **no accessible name** (R015 O8), so a user reaches the single most important input in the product and is not told what it is.
  **Scope note that keeps this honest:** the product has very few validated inputs, so this outcome rests on a small population. The *instructions* half of the criterion is largely untested — no input in the product was observed to need format guidance, but that has not been swept deliberately. **Not to be confused with the error criteria** (3.3.1/3.3.3), which concern what happens *after* input is rejected and are being provoked separately (`session-error-paths-reviewer-walkthrough.md`). Agrees with vendor.

### 3.3.7 Redundant Entry (Level A)
- **Outcome:** Not Applicable
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** none
- **Remarks:** **Independent determination — one of the six WCAG 2.2 criteria absent from the vendor ACR, so there is no claim to verify.** 3.3.7 governs information the user has already supplied being **required again within the same process**. No such process exists in scope: creating a design, authoring, exporting and file management are all single-pass, with no multi-step data entry anywhere (the same structural fact that makes 3.3.1 and 3.3.3 Not Applicable — see R041 O1). Authentication, the classic redundant-entry surface, is handled by the institution's SSO and is off the reviewed path (R041 O5, and see 3.3.8). The one repeated-entry candidate observed anywhere in the review — a rejected rename forcing retyping — was folded into the error-path probe and no rejection path was found to exist.
  **Revisit if either changes:** a multi-step flow is added, or a deployment without SSO brings Adobe's own sign-in onto the path.

### 4.1.2 Name, Role, Value (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F4, T2-F3
- **Remarks:** S1: header community button has no accessible name — **reviewer-confirmed 2026-08-06 with NVDA 2026.1.1 (R012 O1)**, corroborated by Chrome's accessibility tree and axe-core (R009). Extent on S1 is now established and is **narrow**: exactly one control of 48 exposed interactive nodes. The worse hypothesis — systemic mis-mapping of Spectrum web components to the platform API — was tested and refuted, so the vendor's blanket "Does Not Support" looks materially harsher than S1 warrants. Still pending: aria-controls target existence on "More apps" and account-button state toggling (R009 O5, W5); JAWS behaviour on this control is untested (R001 suspended when testing moved to NVDA — see 03 §1.3). **Extent across views now established (2026-08-13):** S3 adds the page-nav "more" button (V-F10), the unlabelled floating text toolbar and the unnamed edit textarea (R015), the create chooser's six unnamed category tabs' options (T2-F1); S4 adds the per-card checkbox and action button (V-F12, reviewer-confirmed). The defects are specific, recurrent, and all of the same cheap-to-fix class — missing accessible names on custom controls — rather than systemic component mis-mapping (R012 O1 refuted that). **Export flow added 2026-08-14 (T2-F3, R037):** neither the export popover (`hz-themed-overlay` → `sp-popover`) nor the subsequent "downloading" dialog conveys a dialog role, and the download dialog's Cancel is discoverable only by enumerating buttons. Sized Minor — everything in the flow is reachable, labelled and Escape-dismissible, so this is a *role* omission rather than a naming failure, and it is the mildest instance of the pattern found anywhere in the product. Outcome stays Partially Supports.

---

## Table 2: Success Criteria, Level AA

### 1.2.4 Captions (Live) (Level AA)
- **Outcome:** Not Applicable
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** No live or streamed time-based media exists anywhere in the product surface examined — Learn's videos are prerecorded, asset-panel media is prerecorded stock, and no broadcast, streaming or real-time collaboration-with-audio feature was found across the exploration crawl (03 §2.5) or any of the 39 runs. With no live media, the criterion has no relevant content. **Revisit if a live feature appears** — this is an absence-of-feature determination, and features get added.

### 1.2.5 Audio Description (Prerecorded) (Level AA)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Cursory pass 2026-08-14 (R039 O2, reviewer): **no audio-described video.** Unlike 1.2.3, this criterion has **no alternative route** — a transcript does not satisfy it; audio description is required specifically. So this outcome is not contingent on the transcript question that keeps 1.2.3 open: **it fails either way.** **Worse than the vendor's claim of Supports.** Cheapest credible remediation is to add audio description to Learn's core tutorials rather than the whole library.

### 1.3.4 Orientation (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Measured 2026-08-14 across **all four sampled views** by CDP device emulation at **900×400 (landscape)**: **zero horizontal overflow on every view**, layouts adapt without restriction. Taken with the portrait/narrow measurements already on file (320 CSS px, zero overflow — runs R002/R018/R019/R020), the product operates in both orientations and locks neither. This closes **LV8**, which had previously stalled — the earlier attempt failed on a *screenshot* that never stabilised, and the metric answers the criterion without one. Agrees with vendor.

### 1.3.5 Identify Input Purpose (Level AA)
- **Outcome:** Not Applicable
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Measured across all four views 2026-08-14 (R042 O2): the product's visible inputs are **search boxes and selection checkboxes** — 2 on S1, 13 on S2, 1 on S3, 12 on S4. **None collects information about the user.** No name, email, address, phone or payment field appears anywhere in the sample, so none of the 53 defined input purposes applies. **This is the same structural fact that makes 3.3.1, 3.3.3, 3.3.7 and 1.3.5 all Not Applicable together:** Express does not gather data about its users — it is a design tool operating on documents, and the one place personal data would be collected (authentication) belongs to the institution's SSO and is off the reviewed path (see 3.3.8).

### 1.4.3 Contrast (Minimum) (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F2
- **Remarks:** S1: "browse" link 3.96:1 at 11px — confirmed by two independent instruments (computed sample R002; axe-core violation R009, same node). **Updated 2026-08-06:** the 15 axe-*incomplete* nodes were not one "gradient" group and are now 8 resolved / 7 open. The Adobe app bar is an SVG image, not a CSS gradient (which is why both instruments returned "indeterminate"); re-rendering that self-contained SVG same-origin on a canvas and sampling it gives all 8 labels **11.18:1–11.71:1 — pass** (R009 O8 / R002 O6). **Closed 2026-08-14 (R009 O10) — the axe-incomplete queue is now fully dispositioned, 15 of 15 nodes.** The last 7 were measured from rendered pixels: the four start-card `h2`s and the row `h2` over card art return **12.51:1–17.30:1** (black text on pastel cards), and both rotating-placeholder words **8.06:1** — all clearing 4.5:1 with margin, so the large-text allowance is not even needed. These are exactly the nodes where ancestor-walking returns a false "white, 21:1"; the measured values pass too, but they are measured rather than assumed. So the only *confirmed* S1 failure remains the single "browse" link. Vendor's own claim admits failure; the measured scope is so far markedly narrower than "Does Not Support" implies. **Re-verified 2026-08-14 on Chrome 151 (R040 O2): still 3.96:1**, with the background resolved from a real element rather than the white fallback — so the finding survives a browser major version, which under 03 §1.5 strengthens rather than qualifies it. **A reviewer WAVE sweep of five pages the same day reported zero contrast errors (R040 O1) and is recorded as N/A, not as a pass** — WAVE parses only the light DOM of a 351-shadow-root application, so its clean result is a demonstrated false negative against a failure three other measurements confirm. It changes nothing about this criterion's outcome.

### 1.4.4 Resize Text (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** **Satisfied by browser zoom, which is what the criterion asks.** Understanding 1.4.4 is explicit that if the user agent's zoom enlarges text to 200% without loss of content or functionality, the criterion is met — and this product reflows cleanly at a **320 CSS px viewport, the 400% equivalence**, with zero horizontal overflow on all four views (R002/R018/R019/R020, 1.4.10 Supports). **Better than the vendor's claim.**
  **A real caveat, measured and recorded because it affects a distinct user group.** Under **text-only** scaling — fonts doubled with page dimensions held constant, 2026-08-14 — horizontal overflow stays at **zero on all four views** (the layout holds), but text **clips inside fixed-height containers**: S1 26 blocks, S2 17, S4 10, **S3 zero**. The pattern is systematic rather than incidental — S4's eight file-name labels each need 59px in a 40px container, S1's start-card `h2`s need 146px in 97px, S2's category cards 219–364px in 120px. Containers do not grow because their heights are fixed, so the text is truncated rather than reflowed.
  This does **not** move the outcome, because a conforming method (browser zoom) exists. It does affect users who scale **text only** — an OS or browser font-size setting rather than page zoom — who are precisely the low-vision users least likely to want everything else magnified too. **Worth a reviewer visual check** to confirm what a user actually sees (truncation vs ellipsis vs scroll), since this rests on the metric alone; the instrument's aggressive `font-size !important` injection is a harder test than browser text zoom. **The editor (S3) is clean on this**, which is notable given it fails so much else.

### 1.4.5 Images of Text (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** **Reasoned from the review's accumulated evidence rather than from a dedicated audit — the basis is stated so it can be weighed.** Every interactive label, heading and body string this review has exercised is **real text**, not a picture of text: headings were walked with `H` and enumerated in the accessibility tree (R012 O5), control names were confirmed on focus across four views, and the 2026-08-14 text-scaling pass grew **1,924 text-bearing elements on S1 alone** — an image of text would not scale. Where text failed to appear it was *absent from the tree*, never *present as an image*.
  The images that do exist (S1 58, S2 93, S3 14, S4 63) are template thumbnails, card art and file previews. Template thumbnails **do** depict text, but they are pictures *of designs* — the text is the subject of the image, which 1.4.5 exempts as essential, in the same way a screenshot or a logotype is exempt. **Their real defect is a different criterion**: they carry no text alternative and are absent from the accessibility tree (T1-F2, 1.1.1), which is recorded there and not double-counted here.
  **Not done, and it would be needed to call this exhaustive:** no OCR or visual audit of card art was performed, so a decorative graphic with baked-in text could exist unnoticed. Agrees with vendor.

### 1.4.10 Reflow (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Measured on **all four sampled views** at a 320 CSS px viewport (CDP device emulation — the equivalence 1.4.10 itself defines; runs R002/R018/R019/R020, 2026-08-13): **zero horizontal overflow everywhere**; layouts re-stack to a single column. The editor's drawing canvas is exempt content under this criterion. **Better than the vendor's claim** — a genuine product strength worth stating. One scoped caveat, not a defect: at 320px the editor goes panel-over-canvas (asset panel covers the document); whether the canvas is *reachable* at that width is an open interactive check (R019 O1) that belongs to 1.4.4/usability rather than reflow itself. Revisit if that check fails.

### 1.4.11 Non-text Contrast (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F18
- **Remarks:** Measured by the reviewer with *Color Contrast Checker*, 2026-08-14 (R002 O-LV16): **the text passes, the controls holding it do not** — *"all the text passes color contrast, but some of the button/icons holding the text don't when measured against the background"*, confirmed on **S1 Home and S3 the editor**. This is the split the criterion exists to catch: 1.4.3 governs text against its background, 1.4.11 governs the **control's boundary** against what surrounds it, and a button with legible 7:1 label text still fails if a user cannot perceive that the button is there.
  **Partially Supports rather than Does Not Support**, on the reviewer's own scoping: *"some"* controls fail, not most. Other non-text contrast evidence is positive — grayscale passes on all four views with selection conveyed by shape (1.4.1 Supports), the app bar's own elements measure 11.18:1–11.71:1 (R009 O8), and canvas selection uses a bounding box with resize handles (R022 O2). **Narrower than the vendor's blanket Does Not Support**, and the fifth criterion where the ACR is harsher than testing warrants.
  **No ratio or count is recorded, deliberately** — the reviewer reported the pattern without enumerating which controls or by how much, and a fabricated number would be worse than none. Enumeration is remediation work for the vendor, who holds the design tokens; this is a token-level fix rather than a per-component one.
  **Methodological note worth carrying to the report:** this defect is invisible to every automated instrument used in this review — axe flagged nothing of the kind on any view, WAVE reported zero contrast errors across five pages (R040), and an assistant rendered-pixel sweep was built, produced three wrong answers, and was abandoned (R042 O6). **A reviewer with an eyedropper answered it in one pass.**

### 1.4.12 Text Spacing (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** S1 passes with full visual confirmation (R002 O1 screenshot + 2026-08-13 re-capture at 320px). S2/S3/S4 pass **by overflow metric** under the standard override (no layout growth, R018–R020); the visual confirmation screenshots stalled on those views — a documented instrument limit (renderer never stabilizes under global spacing injection on heavy shadow-DOM views), not a product signal. Agrees with the vendor. Downgrade only if a reviewer spot-check ever shows clipping the metric missed.

### 1.4.13 Content on Hover or Focus (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none — **V-F1 withdrawn 2026-08-14**
- **Remarks:** **Reversed on reviewer confirmation, and the reversal is the honest result.** This criterion previously stood at *Does Not Support* on V-F1, which claimed the S1 left-rail flyout failed all three 1.4.13 conditions. That evidence was **assistant-driven synthetic hover teleports** — the pointer jumped between coordinates rather than travelling continuously — and the finding recorded that limitation and asked for pointer confirmation. The reviewer tested it with a real pointer on 2026-08-14: **"no issues with hover, pass it"** (R002 O-LV17). LV6 passes; V-F1 is withdrawn (04 §B); the criterion moves to **Supports**, which is also **better than the vendor's claim**.
  **Consequence for the ACR reliability count, stated because it moves a number the report cites:** 1.4.13 was one of the criteria recorded as *worse than claimed*. It now moves to *better than claimed*, a two-place swing in the vendor's favour.
  **Methodological note for the report:** this is the **fourth** assistant hypothesis retired by reviewer testing on this review (after the 2.1.1 "pointer-only editing" Blocker, "invisible editing", and the claim that the editor lacks landmark bypass). Every one was caught before publication because the assistant recorded its instrument's limitation and routed the item. The durable lesson: **assistant-driven *interaction* findings on this product must be reviewer-gated**, while assistant *measurement* — contrast, geometry, reflow, accessible-name comparison — has held up throughout.

### 2.4.5 Multiple Ways (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Measured 2026-08-14 (R042 O4): **S1, S2 and S4 each expose a search control *plus* 2–4 navigation landmarks** — two independent mechanisms, where the criterion asks for more than one. Users can reach a design through the left-rail navigation, through search, or through the Your stuff listing. **S3 the editor has neither (0 search, 0 nav landmarks) and needs neither:** 2.4.5 explicitly exempts a page that is *"a step in a process"*, which the editor is by definition — it is where the design process happens and is reached from the views that do provide navigation. Agrees with vendor.
  **Worth noting against the wider picture:** navigation *mechanisms* being present is a different question from navigation being *usable by ear*, which this review has found badly wanting (T1-F1 unannounced view changes, V-F8 one title product-wide, V-F3 no bypass). 2.4.5 asks only whether the mechanisms exist. They do.

### 2.4.6 Headings and Labels (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F5
- **Remarks:** S1: **headings pass** — the outline is well-formed and descriptive, confirmed independently by two screen readers (JAWS R001 O3; NVDA R012 O2/O5) and Chrome's accessibility tree: `h1` "How would you like to start?", `h2` section headings, `h3` "Recent". **Labels fail in the "Get started" modal** — ten chooser buttons share the identical accessible name "Browse templates" with nothing to distinguish them (V-F5, reviewer-confirmed with NVDA, count verified in the accessibility tree). So the criterion splits cleanly: headings good, one labelling defect in a modal state. That is materially better than the vendor's blanket "Does Not Support", but not a pass. Pending: S2/S3/S4, and whether the button→category association is programmatically determinable (would add 1.3.1).

### 2.4.7 Focus Visible (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** none
- **Remarks:** Rolled up 2026-08-14 from check **MO4** across the four motor runs. **Two views carry explicit reviewer confirmation, in their own words:** S2 — *"focus indicator is always visible"* (R032 O1); S4 — *"all focus is visible"* (R033 O1). S1 and S3 are recorded partial for an honest reason: the reviewer completed full sighted traversals (33 stops on S1) without reporting a single missing indicator, but no per-stop confirmation was narrated, so the evidence is a successful traversal rather than an enumeration (R004, R031). **Zero counter-evidence exists on any view or in any session.** **Better than the vendor's claim** — the sixth criterion where independent testing lands above Adobe's own assessment, and a genuine product strength worth stating alongside reflow and cognition. Note the scope limit: 2.4.7 asks whether an indicator is *visible*, not whether it is *unobscured at zoom* (2.4.11, still open via LV7) or whether it meets 2.4.13's appearance thresholds (AAA, outside target).

### 2.4.11 Focus Not Obscured (Minimum) (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** none
- **Remarks:** **Independent primary evidence — one of the six WCAG 2.2 criteria absent from the 2023 ACR, so there is no claim to verify.** Reviewer at **400% zoom, 2026-08-14**: *"everything is navigable still"* (LV7, closed across R002/R018/R019/R020). 2.4.11 asks whether the focused element gets hidden by author-created content — sticky headers, floating toolbars, overlays — and 400% is where that fails on most products, because magnification leaves sticky chrome occupying a large share of the viewport. It does not fail here. Consistent with the other focus evidence: visible focus indicators on every view with no counter-example anywhere (2.4.7 Supports), and correct focus containment in dialogs (R012 O8/O13). **Focus discipline is one of this product's genuine strengths** — a useful counterweight in a report that is critical of its naming and feedback. **Scope note:** this is the *Minimum* (AA) criterion, which permits partial obscuring; 2.4.12 (Enhanced, AAA) is outside the target.

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
- **Outcome:** Not Applicable
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Measured across all four sampled views 2026-08-14 (R042 O1): the document language is `en-us` on every view, and **zero elements carry a `lang` differing from it**. No foreign-language passage exists for the criterion to govern. Distinct from **3.1.1**, which asks for the *page's* default language and is verified **Supports** on the same measurement. **Revisit if localisation changes the picture** — this is an English-locale session, and a product serving other locales may mix languages within a view.

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

### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (Web)
- **Task findings:** none
- **Remarks:** Probed 2026-08-14 (R041 O2/O4, reviewer). **File deletion — the only path in scope that modifies or deletes user-controllable data** (there is no checkout, legal commitment or test submission in this product) — **is guarded by a modal that is announced and offers an explicit cancel/delete choice.** 3.3.4 requires just one of Reversible, Checked or Confirmed; this is Confirmed. The product's most destructive action is properly protected, and the review should say so plainly. **Profile name was raised and assessed:** it is editable with no undo, but re-entering the previous value is ordinary user-reversible editing, so the Reversible route is satisfied without a dedicated undo. Agrees with vendor.
  **A finding-adjacent observation worth carrying to the report (R041 O3): the delete modal *is* announced, while the export popover and download dialog are not (T2-F3).** Same product, same component library, opposite outcomes — a fifth instance of this review's recurring shape, *the capability exists and is applied unevenly*. It strengthens remediation item 20 materially: announcing the export dialogs is not a new capability to build but an existing internal pattern to apply consistently.

### 3.3.8 Accessible Authentication (Minimum) (Level AA)
- **Outcome:** Not Applicable
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:** none
- **Remarks:** Resolved by scope, not by test (R041 O5, reviewer 2026-08-14): *"my sign in is via SSO, which is accessible; can't test Adobe's directly."* **In this deployment the authentication step belongs to the institution's identity provider, not to Adobe Express.** The IdP is a different product outside the boundary this review declares (03 §1.1 — authenticated app content at `new.express.adobe.com`); evaluating it would be a separate review with its own sample set. Adobe's native sign-in is consequently **not on the path under review**, and cannot be reached without leaving the deployment configuration being assessed.
  **The residual, stated plainly because it is the only one of its kind in this review.** A campus that adopts Express **without** SSO puts its users on Adobe's own authentication — for which there is **no independent evidence here** and **no vendor claim either**, 3.3.8 being one of the six WCAG 2.2 additions absent from the 2023 ACR. Every other criterion in this review has at least one of the two; this configuration has neither. **It converts into a procurement question rather than a test: require Adobe to state a 3.3.8 position for Adobe ID sign-in, and record SSO as the assumed deployment mode in any agreement.**

### 4.1.3 Status Messages (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** T1-F2, T2-F2, V-F13, T2-F3
- **Remarks:** **Four independent instances across three views — a consistent product pattern, not isolated slips.** S4: changing the file filter updates the list with no announcement of any kind (V-F13, reviewer-confirmed, R029 O4). S3: inserting an image reports nothing, and **"Generate with AI"** — an asynchronous, heavily-promoted operation taking many seconds — announces no progress, completion or failure, so a screen-reader user cannot distinguish working from finished from failed (T2-F2, R016 O7). The inconsistency makes it clear-cut: the same panel announced *text* insertion ("edit selected add text") one step earlier, so the capability exists and is simply not applied to images. S2: the template grid loads results lazily on scroll and **their arrival is not announced** — combined with silent arrow navigation and unnamed items, the reviewer could find no reliable way to search the grid by ear (T1-F2, R013 O3/O8, NVDA 2026.1.1). Entering the grid region is likewise unannounced. **Confirmed a second time via the search path** (R013 O13): running a template search updates the results with no announcement of any kind — no count, no "results updated" — so a user cannot tell whether their search returned anything. S1 partial evidence is more favourable: opening the "Get started" modal announces (over-announces, R010/R012 O15) rather than staying silent. Agrees with the vendor's claim. **Export walked 2026-08-14 (R037) — and the pattern did not hold there, which is recorded deliberately.** A fifth instance looked near-certain going in; instead **download progress and completion are announced** (beeps, then completion on initiation). Two qualifications keep this honest in both directions: the feedback comes from the **browser's** download UI rather than from Express, so it meets the user's need without evidencing product-emitted status messages; and the app's own "downloading" dialog does appear unannounced (T2-F3, Minor). Net effect on the criterion: the four established instances stand, the export path is **not** a fifth, and the outcome remains Partially Supports. Still pending: the editor's autosave indicator.
