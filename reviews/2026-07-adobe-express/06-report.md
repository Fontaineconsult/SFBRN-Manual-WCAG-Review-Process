# ICT Accessibility Review Report — Adobe Express

Independent verification by the CSU System-level ICT accessibility review
team, serving campus RFPs and systemwide purchase agreements. This is **not
a vendor VPAT/ACR** — the vendor's self-attestation is audited in §Vendor
ACR audit; the per-criterion technical record is `05-results.md`.
Derivation rules: `ontology/reporting.md`.

| | |
|---|---|
| **Review ID** | 2026-07-adobe-express |
| **Report status** | **INTERIM — testing in progress** (see §Coverage & limitations) |
| **Report date** | |
| **Reviewer(s)** | |
| **Product & version** | Adobe Express (web app, new.express.adobe.com) |
| **Vendor ACR reviewed** | "Adobe Express Web App" ACR, 2023 — written against WCAG 2.1 (see §Vendor ACR audit) |
| **Conformance target** | WCAG 2.2 Level AA |
| **Methodology** | WCAG-EM 2.0 (scope & sample: `03-scope-and-sample.md`) |
| **Instruments & baselines** | NVDA 2026.1.1 + Chrome 150.0.7871.187 (B4); axe-core 4.10.3 (assistant-run sweeps); keyboard-only (B2) and 400% zoom (B3) pending; JAWS (B1) suspended pending a scope decision |

## Procurement decision

| | |
|---|---|
| **Decision** | Approved / Needs TAAP / Denied |
| **Decision date** | |
| **Decided by** | |
| **Rationale** | |

**Decision buckets** — driven by the task verdicts in `04-task-testing.md`;
apply the first bucket whose conditions all hold:

- **Approved** — the product may enter the campus ecosystem. No task verdict
  of **Fail**, no Blocker findings, and no "Does Not Support" outcome or
  Major finding that substantially burdens an essential task for any affected
  user group.
- **Needs TAAP** — the product may be procured only with a Technology
  Accessibility Accommodation Plan. Task failures or Major barriers exist,
  but every essential task remains achievable through accommodation, and the
  vendor commits to a remediation roadmap.
- **Denied** — the product may not enter the campus ecosystem. One or more
  essential tasks are blocked for an affected user group with no workable
  accommodation, or the vendor will not commit to remediation.

## At a glance

| | |
|---|---|
| **Headline** | A screen-reader user can **author** a design end to end, but cannot readily **choose** a template by name, **revise** existing work, or **tell when operations complete**. |
| **Essential tasks** | 2 defined: T1 (create from template) **Pass with barriers**; T2 (author from scratch) in progress — authoring steps pass, feedback steps fail |
| **Criteria verified** | **23 of 55**: 9 Supports · 10 Partially Supports · 4 Does Not Support |
| **Findings** | **14 active** (0 Blocker · 12 Major · 2 Minor) + 1 raised-and-withdrawn, retained for the record; at least 3 product-wide |
| **Vendor ACR coverage** | 2023, written against **WCAG 2.1**: 6 of the 55 target criteria unaddressed (all six WCAG 2.2 additions), 1 claim obsolete (4.1.1) |
| **Vendor ACR reliability** | Of 23 verified: **5 worse than claimed · 7 better · 8 agree** (+3 with no claim to check) |
| **Remediation outlook** | Mostly **additive and cheap** (names, announcements — see exhibit); one structural item (canvas object identity) |
| **Coverage of this review** | 9 of 28 view×modality cells run; **all screen-reader evidence is NVDA-only** |

## Executive summary

Adobe Express (web) was evaluated against WCAG 2.2 Level AA using WCAG-EM,
with task-based testing by a screen-reader-using reviewer across the home
dashboard, template gallery, and editor. The product's fundamentals are
sound — a user was able to author, name, and populate a design entirely by
keyboard and screen reader — but a consistent product-wide pattern of
missing names and missing status feedback means the same user cannot choose
between visually-distinguished options, revise existing work, or tell when
asynchronous operations finish. The vendor's ACR predates the target
standard and misstates roughly a third of the criteria verified so far, in
both directions. Testing is incomplete; this interim report exists to
support early procurement conversation, not a final decision.

## Character of the barriers

**The product is broadly operable and fails on feedback, not on
mechanics.** Across three views tested to date, the baseline semantics are
sound: real headings, real buttons, landmark structure on most views,
keyboard reachability of essentially everything, and — where tested —
correct focus containment in dialogs. Very little is outright broken.

**What is thin is the supplementary layer that conveys *meaning* — and in
this product that is the layer that matters most.** This is an application
for producing **visual artifacts**, so a user who cannot see the artifact
depends entirely on what the interface tells them. More feedback should be
expected here than in an ordinary web application, not less. The evidence
is consistent on this point:

- **Grouping exists but is unnamed** — 17 of 18 grids across all sampled
  views carry no accessible name (V-F11), while the headings that would
  name them sit unused beside them.
- **Selection is not conveyed** — choosing any object on the canvas
  announces "Canvas" or "Canvas Graphic", identically for a text box, an
  image or a shape (R015 O9, R016 O8).
- **Navigation is not conveyed** — moving between views announces "current
  page, current page" and never changes the page title (T1-F1, V-F8).
- **Completion is not conveyed** — search results, lazily-loaded content,
  image insertion and AI generation all finish silently (T1-F2, T2-F2).
- **Identity is not conveyed** — template items, six of the seven
  create-flow categories, and the text-editing field itself carry no
  accessible names (T1-F2, T2-F1, R015 O8).

**The exceptions prove it is a choice, not a limitation.** Where the product
does supply ARIA, it works well: the layers list carries a genuinely
instructive label including its keyboard shortcuts; adding new text
announces "edit selected add text"; document creation announces "Loading
Document"; renaming is fully operable by keyboard. The same codebase does
this correctly in some places and omits it in most.

**Framing that survives vendor rebuttal.** Two easy claims are *not*
supported: "the editor is inaccessible" (a user authored a design end to
end) and "tables are misused for navigation" (these are ARIA `grid` roles
misapplied to carousels, not layout tables). The defensible statements:
**a screen-reader user can author a design but cannot readily revise one**
— including their own work in a later session (R016 O6); remediation is
mostly additive; and almost none of this is visible to automated testing
(the editor sweep returned 43 passes and said nothing about the canvas).

## Task outcomes

| Task | User story | Verdict | WCAG criteria failed | Findings |
|------|-----------|---------|----------------------|----------|
| T1 | Create a design from a template (F1 — core purpose) | **Pass with barriers** (B4/NVDA; Fail was considered and rejected by reviewer decision — see 04 §A) | 4.1.2, 1.1.1, 1.3.1, 2.4.3, 4.1.3, 1.3.3, 2.4.2 | T1-F1, T1-F2 (+V-F8, V-F9) |
| T2 | Author a design from scratch: add text, add an image, save (F2+F5) | **In progress** — create/rename/add-text pass cleanly; image feedback fails; export not yet walked | 4.1.2, 1.1.1, 4.1.3 (so far) | T2-F1, T2-F2 |

## Key findings, by user impact

### 1. Existing designs cannot readily be revised — the authoring/revising asymmetry (R015, R016 O6)

- **Impact:** A screen-reader user can create content but cannot
  practically return to it — their own later drafts, or a colleague's file.
  Selecting any canvas object announces only "Canvas"/"Canvas Graphic" with
  no name, type or content; the layers list (the only route to existing
  objects) appears in no NVDA navigation view and sits ~32 tab stops deep;
  the editing field, once reached, has no accessible name.
- **Where:** S3 Editor, all object types tested.
- **Root cause:** canvas objects have no representation in the
  accessibility tree; the on-demand `<textarea>` is unnamed.
- **Evidence:** R015 O2/O3/O8/O9; R016 O6, O8, O9.

### 2. Choosing between visual options is guesswork — templates and create-flow (T1-F2, T2-F1, V-F5)

- **Impact:** The product's selling point is choosing among
  visually-distinguished designs; a screen-reader user cannot tell the
  options apart. Template-grid items have no names and their thumbnails are
  absent from the accessibility tree; six of seven create-chooser categories
  announce every option as "Clickable Figure Template Button"; ten modal
  buttons share one name.
- **Where:** S2 Explore grid; S1/"Get started" chooser.
- **Root cause (grid):** `<x-masonry role="row">` with **no grid parent**
  (axe critical, R011 O1) — and a correctly-built list sits on the same
  view (the search results list, R013 O13), proving the pattern is
  achievable in this codebase.
- **Evidence:** R013 O3–O8; R016 O1/O2; R011 O1.

### 3. Operations complete silently — three instances of the same 4.1.3 defect (T1-F2, T2-F2)

- **Impact:** Search results arrive, lazy content loads, images insert, and
  AI generation runs for many seconds — none of it announced. "Still
  working", "finished" and "failed" are indistinguishable. Sharpest on
  **Generate with AI**, the product's most promoted capability.
- **The clincher:** the same panel announces *text* insertion ("edit
  selected add text") — the capability exists and is unevenly applied.
- **Evidence:** R013 O3/O8/O13; R016 O7.

### 4. No orientation across views — titles and navigation (V-F8, T1-F1)

- **Impact:** The document title is "Adobe Express" on every view (4 views
  verified, 1 title) and rail navigation announces only "current page,
  current page" while focus stays behind — so moving through the app gives
  a screen-reader user no signal of where they are. Verified worse than the
  vendor's own claim (2.4.2: claimed Partially Supports, verified **Does
  Not Support**). Documents *do* retitle, so the capability exists.
- **Evidence:** R012 O16; R013 O1; title comparison in R012.

### 5. Product-wide unnamed grids (V-F11)

- **Impact:** 17 of 18 grids across all four sampled views have no
  accessible name; users land in anonymous "grid"/"table" containers.
  ARIA `grid` is also misapplied to one-dimensional carousels.
- **Remediation is one line per grid** — each already has an adjacent
  exposed heading; `aria-labelledby` closes it.
- **Evidence:** R015 O10 (counts across S1/S2/S3/S4).

### 6. Keyboard-only users have no bypass (V-F3 — reviewer decision pending)

- **Impact:** No skip link; ~15 tab stops of Adobe cross-product chrome
  precede content on every page. Screen-reader users bypass via landmarks
  (confirmed in both JAWS and NVDA), so this is scoped to keyboard-without-AT
  users. Held at Does Not Support pending the reviewer's 2.4.1 call — note
  the editor (S3) has **no `main` landmark**, so the landmark bypass does
  not exist there.
- **Evidence:** R004 O1; R001 O7; R012 O7; R014 O3.

### 7. Hover flyout violates all three 1.4.13 conditions (V-F1 — pointer confirmation pending)

- **Impact:** The left-rail flyout dismisses when approached, ignores Esc,
  and then persists indefinitely over content. Worse than the vendor's
  claim if confirmed with continuous pointer movement.
- **Evidence:** R002 O4/O5; R003.

### 8. Unnamed icon controls and a stateless toggle (V-F4, V-F10, R015 O6)

- **Impact:** The header community button (every view) and the editor's
  page-nav "more" button announce as bare "button"; the floating
  text-toolbar's Bold/Italic/Underline carry no labels; Italic exposes no
  pressed state. Scope verified narrow — these are specific misses, not a
  systemic component failure (48 of 49 controls on S1 are correctly named).
- **Evidence:** R012 O1; R014 O1; R015 O6.

### Positives that shape the decision

- **Authoring works end to end**: blank document created, named
  ("Test-With-Keyboard"), text added with correct announcements, edit mode
  entered automatically, content confirmable by ear (R016 O4/O5).
- **The "Get started" modal is exemplary on focus**: focus moves in, is
  contained, Esc closes (R012 O8/O13 — a Major finding was raised against
  it in error and formally withdrawn, V-F6).
- **2.5.8 Target Size: Supports** — measured across all 51 interactive
  targets; independent evidence for a criterion the vendor never addressed.
- **App-bar contrast passes at 11–12:1** where two automated instruments
  returned "indeterminate" (and axe's two *failing* contrast numbers on the
  editor were proven false positives by pixel measurement).

## Findings by sensory/functional modality (Section 508 FPC)

*Procurement reads in functional terms — "can a blind user, a deaf user, a
keyboard-only user actually work?" This slices the same findings by the
Section 508 Functional Performance Criteria (302.1–302.9), per the
modality→WCAG map in `ontology/modality-checks.md`.*

| Modality (508 FPC) | Coverage so far | Criteria failed | Findings | What it means for this user group |
|---|---|---|---|---|
| **Without vision** (302.1) | S1 ✓, S2 ✓, S3 in progress (NVDA only) | 1.1.1, 1.3.1, 1.3.3, 2.4.2, 2.4.3, 2.4.6, 4.1.2, 4.1.3 | T1-F1, T1-F2, T2-F1, T2-F2, V-F4, V-F5, V-F7–V-F11 | Can author a design end to end; cannot choose templates by name, revise existing work, or tell when operations finish. The most-affected group. |
| **With limited vision** (302.2) | Reflow measured on **all four views** (320-px equivalence, 2026-08-13); contrast/focus/hover items remain | 1.4.3, 1.4.13 | V-F1, V-F2 | **Reflow passes everywhere** — zero horizontal overflow on S1–S4, a genuine strength. Open: the editor goes panel-over-canvas at 320px (canvas reachability unverified); one contrast failure (3.96:1 link); the undismissable hover flyout; icon contrast and focus-at-zoom checks. |
| **Without color perception** (302.3) | S1–S4 all captured in grayscale | none found | — | Selected states survive grayscale on every view (filled pills, boxed selections, numeric badges, real checkmarks). Open: canvas selection highlight (not capturable by instrument), link hover cues. |
| **Without hearing / limited hearing** (302.4/.5) | S1–S4 all determined (R030 closed S3); **Learn (C11) untested** | none in the product's own UI | — | The editor's UI carries no audio content (N/A with evidence); no sound-alone feedback anywhere; no voice input (reviewer-confirmed). The live issue moved to §Concerns: **auto-caption capability exists for inserted video but professional caption files cannot be uploaded**. Learn's tutorial videos — Adobe's *own* content, where 1.2.2 applies directly — remain untested. |
| **Without speech** (302.6) | All views so far | n/a | — | No voice-input features observed. |
| **With limited manipulation/reach/strength** (302.7/.8) | Partial — physical-keyboard sweep pending | 2.4.1 (reviewer classification pending) | V-F3 | Everything reached so far is keyboard-operable (incl. full authoring), but every page visit costs ~15 tab stops of unrelated chrome with no skip mechanism — and the editor has no `main` landmark to bypass with. **2.5.8 target size verified Supports** — independent positive on a criterion the vendor never claimed. |
| **With limited language/cognitive/learning abilities** (302.9) | **Complete — all four views, Works** (R010, R034–R036) | none | — | **The product's strongest modality.** Navigation and identification consistent across every view; help in a consistent location; no unexpected context changes anywhere; nothing moving or blinking; everything labeled, iconed or tooltipped. Six criteria verified Supports on this evidence (3.2.1/3.2.2/3.2.3/3.2.4/3.2.6/2.2.2), two of them better than or absent from the vendor's ACR. Auth (3.3.8) and error-path criteria remain flow-scoped. |

Two honest caveats this table makes visible: the *worst-tested* modality
(low-vision at 400% zoom) is one of the *likeliest to fail* on a canvas
product, and the two N/A-looking rows (hearing) stop being N/A exactly
where the product meets media — neither should be read as "clear".

## Vendor ACR audit

### Coverage: the ACR does not address the target standard

The vendor's 2023 ACR is a **WCAG 2.1-era document** offered against a WCAG
2.2 AA procurement. The arithmetic identifies it exactly: 50 criteria
claimed; 1 obsolete (4.1.1 Parsing, removed in 2.2); the **6 criteria with
no claim at all are precisely the six WCAG 2.2 additions** — 3.2.6, 3.3.7,
2.4.11, 2.5.7, 2.5.8, 3.3.8 — the criteria protecting motor and cognitive
users. ~11% of the standard has no vendor position to verify or hold them
to. (Full arithmetic: `05` §Vendor evidence gap.)

### Reliability — claims vs verified (12 criteria verified to date)

| Criterion | Vendor claim | Verified | Direction | Note |
|-----------|--------------|----------|-----------|------|
| 2.4.1 | Supports | Does Not Support¹ | **worse** | no bypass for keyboard-only users; ¹reviewer classification decision pending |
| 2.4.2 | Partially Supports | Does Not Support | **worse** | one title product-wide; no view distinguishable |
| 1.3.3 | Supports | Partially Supports | **worse** | templates distinguishable only by visual thumbnail |
| 1.4.13 | Partially Supports | Does Not Support² | **worse** | flyout fails all three conditions; ²pointer confirmation pending |
| 1.4.3 | Does Not Support | Partially Supports | better | one confirmed failure (3.96:1 link); app bar measured 11–12:1 |
| 2.4.3 | Does Not Support | Partially Supports | better | S1 modal focus exemplary; failures are task-specific on S2 |
| 2.4.6 | Does Not Support | Partially Supports | better | headings genuinely good; one labelling defect in a modal |
| 4.1.2 | Does Not Support | Partially Supports | better | specific unnamed controls, not systemic mis-mapping |
| 1.1.1 | Partially Supports | Partially Supports | agree | vendor's own exception wording reproduced on S1 |
| 1.3.1 | Partially Supports | Partially Supports | agree | |
| 4.1.3 | Partially Supports | Partially Supports | agree | five-plus verified instances across three views |
| 1.4.12 | Supports | Supports | agree | S1 visually confirmed; S2–S4 by overflow metric |
| 3.2.1 / 3.2.3 / 3.2.4 / 2.2.2 | Supports | Supports | agree | cross-view reviewer closure, R034–R036 |
| 3.2.2 | Partially Supports | Supports | better | no context change on input anywhere |
| 3.2.6 | **no claim** | Supports | — | independent: help location consistent on every view |
| 2.1.4 | Supports | Does Not Support | **worse** | "T" shortcut; Settings has no disable/remap (V-F15) |
| 2.1.1 | Does Not Support | Partially Supports | better | authoring, navigation, move, z-order all keyboard-operable; rotation/non-text-resize fail (V-F14) |
| 1.4.10 | Partially Supports | Supports | better | zero horizontal overflow on all four views, measured |
| 2.5.8 | **no claim** | Supports | — | independent primary evidence; criterion absent from ACR |
| 2.5.7 | **no claim** | Partially Supports | — | independent: upload/move/z-order have alternatives; rotation and non-text resize do not (V-F14) |

### What this means for relying on this vendor's ACRs

The ACR is **stale against the applicable standard** and **imprecise in
both directions** — blanket "Does Not Support" ratings where testing found
narrow specific defects, and "Supports"/"Partially Supports" where testing
found product-wide failures. It is usable as a map of *where* to look, not
as evidence of *what is true*. Any agreement should require an ACR against
WCAG 2.2 and treat vendor ratings as unverified until tested.

## Results summary

| Outcome | Level A (of 31) | Level AA (of 24) | Total (of 55) |
|---------|-----------------|------------------|---------------|
| Supports | 4 | 5 | 9 |
| Partially Supports | 6 | 4 | 10 |
| Does Not Support | 3 | 1 | 4 |
| Not Applicable | 0 | 0 | 0 |
| Not Evaluated | 18 | 14 | 32 |

Full per-criterion record with evidence citations: `05-results.md`.

## Concerns outside the conformance target

**No way to author alternative text — a defect in the product's *output*,
not its interface (R016 O10).** The reviewer could find no way at all,
visually or by screen reader, to attach alt text to an image placed in a
design. This is deliberately **not** recorded as a WCAG finding: WCAG
governs Express's own UI, and no criterion requires an authoring tool to
support accessible output. The applicable requirements are **Section 508
§504.2/§504.3 (Authoring Tools)** / ATAG 2.0 B.2.3. Materiality depends on
output format: negligible for PNG/JPG, **material for PDF export and
webpage publishing**, where every artifact the campuses publish would carry
unlabelled images — an outward-facing, compounding harm affecting readers
who never touch Express.

**Video captions — the sibling concern, half-answered well (R030,
2026-08-13).** For user-inserted video the picture is better than for
images: the video edit window offers a **CC button with auto-generated
captions** — a real §504.2 capability, credited as such. The gap: **no
apparent way to upload professionally-authored caption files** (SRT/VTT)
or substitute corrected captions. Auto-generated captions are, as a class,
insufficient for published-content conformance (accuracy, speaker
identification, sound description), and CSU's standard captioning
workflows produce professional caption files Express cannot ingest.
Whether auto-captions are at least *editable in place* was not established.
Summary across the two concerns: **images — no capability at all; video —
partial capability with no professional-quality path.**

**Reviewer decisions required:** (1) extend this review's scope to 508
§504, or carry these as advisory notes beside the conformance statement;
(2) confirm via the export walk (W16) which output formats are offered and
**whether captions survive export/publish**; (3) spot-check whether
auto-generated captions are editable in place.

## Coverage & limitations of this review

**This is an interim report.** 23 of 55 criteria verified; **all 28
view×modality cells run** (matrix complete 2026-08-13). What remains is
task- and flow-scoped: T2's export walk; the criteria reachable only
through flows not yet walked (1.2.x via Learn's videos, 3.3.x error
handling, 3.3.8 via sign-in); measurement leftovers (per-view contrast,
focus-at-zoom, the editor's panel-at-320px check); and the standing
reviewer decisions (JAWS scope, 1.4.13 pointer confirmation, 2.4.1
classification, §504 scope).

| View | Done | Open |
|---|---|---|
| S1 Home | no-vision (NVDA), no-color, reflow/spacing measured, axe; NH/NS N/A | LV icon-contrast + focus-at-zoom; motor (8 checks); cognition (6); JAWS suspended |
| S2 Explore | no-vision + task T1, axe, reflow measured, grayscale, NH/NS N/A (evidence-backed) | motor; cognition |
| S3 Editor | axe, reflow measured (panel-over-canvas question open), grayscale chrome, NS N/A | no-vision close-out + T2 export; **no-hearing (insertable media — reviewer)**; motor; cognition |
| S4 Your stuff | axe, reflow measured, grayscale, NH/NS N/A (evidence-backed) | **no-vision (walkthrough W22–W26 ready — checkbox candidate + rename discrepancy)**; motor; cognition |

Standing caveats: **all screen-reader evidence is NVDA 2026.1.1 only** — 
whether JAWS is in scope is an open question (03 §1.3), and JAWS/NVDA
differences were observed (landmark exposure); the S3 test document holds a
single object, so document-scale reading is untested; grid counts are
floors (lazy loading); WAVE is instrument-blind on this product; automated
sweeps cannot see the canvas at all.

## Remediation exhibit (for contract negotiation)

| # | Defect (finding) | WCAG SC | Specific fix | Verify by |
|---|------------------|---------|--------------|-----------|
| 1 | Template grid announces as an orphaned table row; arrowing silent, items unnamed (T1-F2) | 1.3.1, 4.1.2 | Correct container semantics for `x-masonry` (valid grid or listbox pattern); name each item with its template name | axe `aria-required-parent` clean; NVDA arrow-navigation announces each item by name |
| 2 | Template thumbnails absent from accessibility tree (T1-F2) | 1.1.1 | Expose thumbnail with template name as alternative | NVDA `G`-walk finds named graphics on S2 |
| 3 | 17 of 18 grids unnamed product-wide (V-F11) | 1.3.1 | `aria-labelledby` each grid to its existing adjacent heading | AX-tree enumeration: every `role=grid` named |
| 4 | One document title product-wide (V-F8) | 2.4.2 | Per-view `document.title` ("Home — Adobe Express", …) | Titles differ across Home/Explore/Your stuff/Brands |
| 5 | Navigation not announced; focus stays on rail (T1-F1) | 2.4.3 | Move focus to the new view's start or announce arrival | NVDA announces view name on rail navigation |
| 6 | Silent completion: search, lazy-load, image insert, AI generate (T1-F2, T2-F2) | 4.1.3 | Status messages incl. result counts and generate progress/done/failed | NVDA hears each without focus moving |
| 7 | Create-chooser options unnamed in 6 of 7 tabs (T2-F1) | 4.1.2 | Accessible name per option in every category tab | NVDA reads distinct names in each tab |
| 8 | Unnamed controls: community button, page-nav "more", floating text toolbar; Italic lacks state (V-F4, V-F10, R015 O6) | 4.1.2 | `aria-label` each; `aria-pressed` on Italic | axe `aria-command-name` zero; NVDA announces name+state |
| 9 | Edit-mode textarea unnamed (R015 O8) | 4.1.2 | Accessible name identifying the object being edited | NVDA announces field name on entering edit mode |
| 10 | Canvas selection announces "Canvas (Graphic)" for every object (R015 O9, R016 O8) | 4.1.2, 1.3.1 | Selected object exposes name/type/content to AT | NVDA distinguishes text vs image objects by ear |
| 11 | No bypass before app-switcher chrome; editor lacks `main` (V-F3, R014 O3) | 2.4.1 | First-Tab skip link (all views) + `main` landmark in editor | First Tab reaches skip control; landmark list shows `main` on S3 |
| 12 | Hover flyout not hoverable/dismissible/persistent-safe (V-F1) | 1.4.13 | Standard hover-content behavior incl. Esc | Pointer + Esc re-test per 1.4.13 |
| 13 | Decorative inner graphics announced (V-F7) | 1.1.1 | `alt=""`/`aria-hidden` on decorative card images | `G`-walk hears named figures only |
| 14 | No alt-text authoring for placed images (R016 O10) | *508 §504.2/.3 (outside WCAG target)* | Alt-text field on images, carried into PDF/webpage output | Author alt text by keyboard; verify in exported artifact |
| 15 | Object rotation is pointer-drag only (V-F14) | 2.1.1, 2.5.7 | Rotation field in properties panel and/or modifier+arrow rotation | Rotate an object end-to-end by keyboard (B2) |
| 16 | Canvas objects and operations silent to AT; no way to survey a document by ear (R015 O9, R031 O3) | 4.1.2, 1.3.1 | Expose selected-object name/type/state; announce operation results; **provide an on-demand spoken canvas description** (reviewer recommendation: read back the objects, their content and arrangement, on command) | NVDA distinguishes objects and hears move/format results; a "describe canvas" action exists and is announced |
| 17 | Shortcut docs and implementation out of sync both ways: documented rename shortcut broken; working shortcuts undocumented (R031 O2/O6) | — (vendor doc accuracy) | Reconcile the shortcuts page with the implementation; surface an in-app shortcut reference | Every documented shortcut works; every working shortcut documented |
| 18 | "T" single-char shortcut with no known disable/remap (R031 O5 — pending Settings check) | 2.1.4 | Disable/remap setting, or focus-scope the shortcut | Toggle exists and works, or shortcut fires only with canvas focused |

## TAAP — Technology Accessibility Accommodation Plan

*(Completed only if the decision is Needs TAAP. Draft inputs from the
evidence, for the reviewer's use:)*

| Field | Value |
|-------|-------|
| Affected functionality | Choosing templates/options by name; revising existing designs; confirmation of async operations (incl. AI generation); alt-text authoring |
| Affected user groups | Screen reader users (primary); keyboard-without-AT users (2.4.1); low-vision pending testing |
| Accommodation provided | *(reviewer)* |
| Responsible party | *(reviewer)* |
| How users request it | *(reviewer)* |
| TAAP review date | *(reviewer)* |

### Vendor remediation roadmap

| Criterion | Issue | Vendor commitment | Target date |
|-----------|-------|-------------------|-------------|
| *(populate from the Remediation exhibit at negotiation)* | | | |

## Automated sweep record and triage disposition

Every sampled view receives an axe-core sweep (4.10.3, full ruleset, run
inside the authenticated session; raw JSON preserved per run). **Sweep
output is never findings** — each violation is human-confirmed into a
finding or dismissed in writing; each `incomplete` is routed to a manual
check. The full triage lives in each run's `run.md`; this table is the
disposition summary.

| View | Run | Violations | Incomplete | Passes | Disposition |
|---|---|---|---|---|---|
| S1 Home | R009 | 3 | 3 | 47 | 1 → corroborates V-F2 (contrast, independently measured); 1 → **V-F4** (unnamed button); 1 best-practice (`region`) held as observation. Incomplete: 8 of 15 contrast nodes **resolved as passes by measurement** (app-bar SVG, 11–12:1); rest routed to manual checks. |
| S2 Explore | R011 | 4 | 4 | 47 | 2 critical → **root cause of T1-F2** (`aria-required-parent`/`aria-allowed-attr` on the template grid); 1 → V-F4 scope widened to product-wide; 1 best-practice (`heading-order`) → supporting evidence for V-F9. |
| S3 Editor | R014 | 7 | 3 | 43 | 1 → **V-F10** (unnamed page-nav button); **4 contrast violations DISMISSED as instrument false positives** (axe assumed `#e9e9e9` background; rendered pixels measure 15.06:1 and 12.18:1); 4 best-practice (no `main`, no `h1`, 21 nodes outside landmarks, duplicate banner) → fed the S3 landmark analysis and V-F3 scoping. `video-caption` incomplete assessed out of 1.2.2 scope (muted preview). |
| S4 Your stuff | — | | | | **sweep pending** |
| (S1, WAVE) | R007 | 0 | — | — | **instrument-blind** — WAVE parsed only the light DOM of this shadow-DOM app; its clean result was recorded as N/A, not as a pass |

Two standing limits on automated evidence in this product, both demonstrated
in the record: sweeps are **wholly blind to the editor's canvas** (R014
reported nothing about the surface holding the user's document — pass counts
are not reassurance), and axe **contrast numbers are only trustworthy where
a DOM-resolvable background exists** (otherwise it can emit confident false
violations; verified by pixel measurement, R014 O2). Raw output:
`evidence/runs/R009|R011|R014/R###-axe.json`.

## Recommendation

*Drafted by the review process from the evidence above, for the reviewer to
adopt, amend, or reject — the Decision field remains the reviewer's alone.*

On the interim evidence, the pattern most consistent with the findings is
**Needs TAAP, conditioned on vendor commitments**, for three reasons.
First, no essential task is failed outright: a screen-reader user completed
template-based creation (with substantial burden) and authored a design
from scratch, so accommodation is workable rather than fictional. Second,
the barriers are overwhelmingly **feedback and naming defects with cheap,
additive fixes** — the fourteen-item remediation exhibit is dominated by
one-line ARIA attributes and status messages, with a working reference
implementation for the hardest item already present in Adobe's own
codebase — which makes a dated remediation roadmap a reasonable contractual
ask rather than wishful thinking. Third, the vendor's ACR is stale and
unreliable in both directions, so any agreement should require a
current-standard (WCAG 2.2) ACR and treat future vendor claims as
unverified until tested. **Approval is not supportable** while three
criteria stand at Does Not Support and the product's core choosing and
revising workflows exclude screen-reader users; **denial is not supported
either** on present evidence, since every tested task remains completable
and the remediation ask is modest. Two open items could move this
recommendation before the report goes FINAL: the untested low-vision 400%
reflow behaviour (a canvas product's likeliest structural failure), and the
Section 508 §504 alt-text question — if Express publishes PDF/webpages with
no alt-text capability and the vendor will not commit to adding it, the
output-side harm compounds across every campus artifact and weighs toward
denial for publishing-oriented procurements.

## Appendices

- Task-based test record and findings: `04-task-testing.md`
- Full per-criterion results (ACR-shaped technical record): `05-results.md`
- Evidence files: `evidence/` (runs R001–R016), including raw axe JSON per sweep
- Vendor ACR as received: `vendor-acr/`
