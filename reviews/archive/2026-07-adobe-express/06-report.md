# ICT Accessibility Review Report — Adobe Express

Independent verification by the CSU System-level ICT accessibility review
team. This is **not a vendor VPAT/ACR**. The per-criterion record, with
the vendor's claim beside each tested result, is `05-results.md`.

| | |
|---|---|
| **Review ID** | 2026-07-adobe-express |
| **Report status** | FINAL |
| **Report date** | 2026-08-14 |
| **Reviewer(s)** | D. Fontaine |
| **Product & version** | Adobe Express (web app, new.express.adobe.com) |
| **Vendor ACR reviewed** | "Adobe Express Web App", 2023 — written against WCAG 2.1 |
| **Conformance target** | WCAG 2.1 AA (primary, ADA Title II baseline); WCAG 2.2 AA also evaluated |
| **Methodology** | WCAG-EM 2.0 (scope and sample: `03-scope-and-sample.md`) |
| **Instruments** | NVDA 2026.1.1 + Chrome 150/151; keyboard-only; 400% zoom and 320px reflow; axe-core 4.10.3; CDP pixel measurement |

## Procurement decision

| | |
|---|---|
| **Decision** | Needs TAAP |
| **Decision date** | 2026-08-14 |
| **Decided by** | D. Fontaine (reviewer) |
| **Rationale** | Both essential tasks completed, so accommodation works. Most barriers are missing names and missing announcements, which are cheap to fix. The vendor's ACR is stale and inaccurate in both directions. Four conditions apply. |

### Conditions

**1. Do not use Express to publish or share content.** A shared design
reads to a screen reader as "canvas graphic" and nothing else (V-F16).
This protects readers, who never chose the tool and cannot work around it.

**2. Check every exported PDF for accessibility before sending it.** The
"include tags" option does not produce a conformant file — no alt text, no
document title (V-F17).

**3. Deploy with SSO.** This review never tested Adobe's own sign-in, and
their ACR makes no claim about it.

**4. Require a vendor roadmap** against the remediation exhibit, and an
ACR written against WCAG 2.2.

## At a glance

| | |
|---|---|
| **Headline** | A screen-reader user can author a design. They cannot choose a template by name, find an object on a busy canvas, or tell when an operation ends. What the product publishes is not accessible. |
| **Essential tasks** | T1 create-from-template: **Pass with barriers**. T2 author-from-scratch: **Pass with barriers**. |
| **Criteria** | **55 of 55 evaluated** — 26 Supports · 14 Partially Supports · 5 Does Not Support · 10 Not Applicable |
| **Findings** | 23 active (0 Blocker · 18 Major · 5 Minor); 2 withdrawn and retained for the record |
| **Vendor ACR** | Written against WCAG 2.1 in 2023. It misstates about half the criteria tested, so it needs replacing. |
| **Coverage** | All 28 view×modality cells run, across 42 test runs. All screen-reader evidence is NVDA only. |

## Summary

The product works. What it publishes does not.

The basics hold up. Navigation stays consistent, the keyboard reaches
everything, the layout reflows at 400%, focus stays visible, and nothing
flashes or times out. A screen-reader user created a design, added text,
inserted an image and exported it.

The gaps cluster in one place: the product does not say what it is doing.
Templates carry no names. Canvas objects announce identically. Operations
finish in silence. A keyboard-only user cannot rotate or resize objects,
or select files in bulk.

Published output is the serious problem. A shared design conveys nothing
to a screen reader, and a tagged PDF carries no alt text or title. That
harm reaches **readers**, so no campus accommodation fixes it. Conditions
1 and 2 address this.

## Task outcomes

| Task | Verdict | Criteria failed | Findings |
|------|---------|-----------------|----------|
| T1 — Create a design from a template | **Pass with barriers** | 4.1.2, 1.1.1, 1.3.1, 2.4.3, 4.1.3, 1.3.3, 2.4.2 | T1-F1, T1-F2 |
| T2 — Author a design: text, image, export | **Pass with barriers** | 4.1.2, 1.1.1, 1.3.1, 2.4.3, 4.1.3 | T2-F1 – T2-F4 |

The reviewer considered **Fail** for both and rejected it. For T2 they
tested the harder case first: authoring a five-object design and finding
one named object by ear. The walk succeeded, so the task passes. It
succeeded slowly, so barriers stand. `04-task-testing.md` §A records the
reasoning.

## Functional Conformance Report

| Functional Performance Criterion | Conformance | Barriers | Criteria failed | Findings |
|---|---|---|---|---|
| **302.1 Without vision** | Partially Supports | Template and create-flow options expose no accessible name, and their thumbnails do not reach the accessibility tree. Canvas objects announce identically, so a specific object cannot be located. Status messages are absent across search, lazy loading, insertion, AI generation and filtering. One document title serves every view. Bulk file selection is unavailable. | 1.1.1, 1.3.1, 1.3.3, 2.4.2, 2.4.3, 2.4.6, 4.1.2, 4.1.3 | T1-F1, T1-F2, T2-F1, T2-F2, T2-F4, V-F4, V-F5, V-F7, V-F8, V-F9, V-F10, V-F11, V-F12, V-F13 |
| **302.2 With limited vision** | Partially Supports | Button and icon boundaries measure below 3:1 against their backgrounds on two views. One 11px link measures 3.96:1. At 320px the asset panel overlays the canvas. | 1.4.3, 1.4.11 | V-F2, V-F18 |
| **302.3 Without perception of colour** | Supports | No defect found. Selected states use shape and content: filled pills, boxed selection, checkmarks, numeric badges, and a bounding box with resize handles on the canvas. | — | — |
| **302.4 Without hearing** | Supports | The interface emits no audio. Learn's video content carries captions, and captions persist through video export. | — | — |
| **302.5 With limited hearing** | Supports | As 302.4. | — | — |
| **302.6 Without speech** | Supports | The product exposes no voice input. | — | — |
| **302.7 With limited manipulation** | Partially Supports | Rotation and non-text resize offer no keyboard, non-drag or single-pointer alternative. The file-card checkbox does not respond to the Space bar. The "T" shortcut cannot be disabled or remapped. | 2.1.1, 2.1.4, 2.5.1, 2.5.7 | V-F12, V-F14, V-F15 |
| **302.8 With limited reach and strength** | Partially Supports | No bypass mechanism. 19 tab stops of shared chrome precede content on every page. | 2.4.1 | V-F3 |
| **302.9 With limited language, cognitive and learning abilities** | Supports | No defect found. Navigation and component identification stay consistent across views, help occupies a consistent location, and no content moves or updates without user action. | — | — |
| **§504.2/.3 Authoring tool output** | **Does Not Support** | Published pages expose no content to assistive technology. Tagged PDF export omits alt text and document title. | *§504.2, §504.3* | V-F16, V-F17 |

Each barrier above prevents an Approved decision on its own, and requires
either accommodation under a TAAP or vendor remediation.

Two barriers warrant additional detail.

Locating a canvas object requires NVDA's pass-through key. The product
does not expose the focused element as editable, so the user must suspend
screen-reader command handling to enter text.

Rotation fails three criteria for three distinct reasons: no keyboard
route, no non-drag route, no single-pointer route. A properties panel with
typed values resolves all three.

Minor findings fall below this threshold and appear only in the
remediation list: V-F7, V-F9, V-F11, V-F19, T2-F3.

## Criteria verified as supported

- **Consistency and predictability.** Navigation, component
  identification and help location stay consistent across all four views.
  No content moves, updates or changes context without user action.
  (3.2.1, 3.2.2, 3.2.3, 3.2.4, 3.2.6, 2.2.2)
- **Reflow.** Zero horizontal overflow at 320px on all four views. (1.4.10)
- **Focus.** Visible indicators on every view, no keyboard traps, correct
  containment in dialogs, and focus remains unobscured at 400% zoom.
  (2.4.7, 2.1.2, 2.4.11)
- **Authoring path.** Blank document creation, keyboard rename, text
  insertion with announcement, and export all complete.
- **Export.** Format options reachable and labelled, Escape dismisses,
  download progress and completion announced.
- **Target size and pointer cancellation**, both measured across the
  interface. (2.5.8, 2.5.2)

## Output-side concerns (Section 508 §504)

WCAG governs the Express interface, not what Express produces. Section 508
§504.2/§504.3 governs authoring tools. These findings drove conditions 1
and 2.

| Output | Status |
|---|---|
| Images in a design | No alt-text field anywhere |
| PDF export | Tags option exists; output still fails |
| Published pages | No accessible content at all |
| Video captions | Auto-captions work and survive export |
| Audio description | None anywhere |

**Published pages expose no content.** A shared design announces as
"canvas graphic". The reviewer's assessment: *"this tool should not be
used to share content, especially in a course."* Every other finding in
this report affects people operating Express. This one affects people
receiving its output, who have no available workaround.

**The PDF tags option gives false assurance.** Its presence suggests
conformant output and discourages verification. The two defects have
separate causes. Alt text is absent upstream — the product provides no
field to author it, so the tagger has nothing to carry. The missing
document title is an exporter defect and cheap to correct, since Express
already holds the document name.

**Not yet tested.** The exported test file was simple. A multi-element
design exported with tags, checked against PDF/UA, would establish whether
further defects exist.

V-F16 rests on a single test session. It supports condition 1. A review
that brings published pages into its sample set requires dedicated runs
against them.

## Results summary

All five Does-Not-Support outcomes fall under WCAG 2.1, so every
conformance failure counts against the ADA Title II baseline.

| Outcome | Level A (of 31) | Level AA (of 24) | Total (of 55) |
|---------|-----------------|------------------|---------------|
| Supports | 14 | 12 | 26 |
| Partially Supports | 7 | 7 | 14 |
| Does Not Support | 3 | 2 | 5 |
| Not Applicable | 7 | 3 | 10 |
| Not Evaluated | 0 | 0 | 0 |

Ten criteria rate Not Applicable for one reason: Express collects no data
about its users. It has no forms, no checkout and no validated input.
Authentication runs through institutional SSO.

## Coverage and limits

All 55 criteria evaluated. All 28 view×modality cells run. Both essential
tasks walked and verdicted. 42 test runs across four sampled views plus
Learn and Brands.

**All screen-reader evidence is NVDA only.** JAWS never entered scope, and
the two behaved differently where compared. A JAWS user may meet different
barriers.

**Published output was never sampled.** See the caveat on V-F16 above.

**This review never tested Adobe's own sign-in.** The reviewer signs in
through institutional SSO, so authentication belongs to the identity
provider.
Deploying without SSO puts users on Adobe ID sign-in, where this review
holds no evidence and the vendor makes no claim. Condition 3 covers this.

**Automated scans form part of the testing process, but they miss most of
this.** Every sampled view received an axe-core sweep, and a human
confirmed or dismissed each result in writing — scan output never becomes
a finding on its own. The scans cannot see the editor canvas at all: the
editor sweep returned 43 passes and said nothing about the surface holding
the user's document. WAVE reported no contrast errors across five pages,
including the page carrying a confirmed 3.96:1 failure. Each run file
records the full triage.

## What Adobe must fix

Priority reflects how much a fix restores. **High** removes a barrier from
an essential task. **Medium** restores orientation. **Low** is correctness
and polish.

Two fixes carry unusual weight. Naming the layer rows (item 23) removes
the per-object search, tracks which objects a user has visited, and
creates the read-only inspection path the editor lacks. Accessible
published output (item 19) is the only structural item, and the only fix
whose absence harms people who never use the product.

| # | Priority | Defect | WCAG SC | Fix | Verify by |
|---|----------|--------|---------|-----|-----------|
| 1 | High | Template grid announces as an orphaned table row; arrowing silent, items unnamed (T1-F2) | 1.3.1, 4.1.2 | Valid grid or listbox semantics for `x-masonry`; name each item | axe clean; NVDA announces each item by name |
| 2 | Low | Template thumbnails absent from the accessibility tree (T1-F2) | 1.1.1 | Expose the thumbnail with the template name | NVDA `G`-walk finds named graphics on S2 |
| 3 | Medium | 17 of 18 grids carry no name (V-F11) | 1.3.1 | `aria-labelledby` each grid to its adjacent heading | Every `role=grid` has a name |
| 4 | Medium | One document title serves every view (V-F8) | 2.4.2 | Set `document.title` per view | Titles differ across Home, Explore, Your stuff, Brands |
| 5 | Medium | Navigation announces nothing; focus stays on the rail (T1-F1) | 2.4.3 | Move focus into the new view, or announce arrival | NVDA announces the view name |
| 6 | High | Silent completion: search, lazy load, image insert, AI generation, file filter (T1-F2, T2-F2, V-F13) | 4.1.3 | Status messages with result counts and progress states | NVDA hears each without focus moving |
| 7 | High | Create-chooser options unnamed in six of seven tabs (T2-F1) | 4.1.2 | Name every option in every tab | NVDA reads distinct names in each tab |
| 8 | Medium | Unnamed controls: community button, page-nav "more", floating text toolbar; Italic lacks state (V-F4, V-F10) | 4.1.2 | `aria-label` each; `aria-pressed` on Italic | axe `aria-command-name` clean |
| 9 | Medium | Edit-mode textarea unnamed (R015 O8) | 4.1.2 | Name the field with the object being edited | NVDA announces the field name |
| 10 | Low | Canvas selection announces "Canvas" for every object (R015 O9) | 4.1.2, 1.3.1 | Expose each object's name, type and content | NVDA tells text from image by ear |
| 11 | Medium | No skip mechanism; editor lacks `main` (V-F3) | 2.4.1 | Skip link on first Tab; `main` landmark in the editor | First Tab reaches the skip control |
| ~~12~~ | — | ~~Hover flyout~~ **withdrawn 2026-08-14** — reviewer confirmed correct behaviour | — | none | — |
| 13 | Low | Decorative inner graphics announced (V-F7) | 1.1.1 | `alt=""` or `aria-hidden` on decorative card images | `G`-walk hears named figures only |
| 14 | High | No alt-text field for placed images (R016 O10) | *§504.2/.3* | Alt-text field on images, carried into exports | Author alt text by keyboard; check the export |
| 15 | High | Rotation and non-text resize have no alternative (V-F14) | 2.1.1, 2.5.1, 2.5.7 | Transform panel with typed values for position, rotation and size | Rotate and resize by keyboard; single-pointer route exists |
| 16 | Low | Canvas objects and operations stay silent (R015 O9, R031 O3) | 4.1.2, 1.3.1 | Announce operation results; add an on-demand spoken canvas description | NVDA hears move and format results |
| 17 | Low | Shortcut documentation disagrees with the product in both directions (R031 O2/O6) | *(doc accuracy)* | Reconcile the shortcuts page; add an in-app reference | Every documented shortcut works |
| 18 | Low | "T" shortcut cannot be disabled or remapped (V-F15) | 2.1.4 | Add a shortcuts setting, or scope the shortcut to canvas focus | Toggle exists and works |
| 19 | High | Published pages convey nothing to assistive technology (V-F16) | 1.1.1, 1.3.1 | Render published content as real text and structure, or ship an accessible alternative | NVDA reads a published page end to end |
| 20 | Low | Export and download dialogs announce nothing; Cancel undiscoverable (T2-F3) | 4.1.2, 4.1.3 | `role="dialog"` with a name on both. The product's own delete modal already does this | NVDA announces both as named dialogs |
| 21 | High | Tagged PDF export omits the document title (V-F17) | *§504; 2.4.2 of the file* | Write the document name into PDF Title metadata | PDF/UA title check passes |
| 22 | High | Tagged PDF export carries no alt text (V-F17) — blocked by item 14 | *§504; 1.1.1 of the file* | Carry authored alt text through the tagger | Alt text survives in the exported PDF |
| 23 | High | Layer rows carry no object identity (T2-F4) | 4.1.2, 1.3.1 | Name each row: "text 2", "Photo — beach.jpg", "Rectangle" | NVDA names each object; selection needs no edit mode |
| 24 | Low | An untranslated string is spoken as a control name: `@hz/shared-ui-components:sortable-list-press-space-to-grab` (T2-F4) | 4.1.2 | Resolve the message key to its text | NVDA announces "press space to grab" |
| 25 | High | S4 card checkbox and action button unnamed; checkbox ignores Space (V-F12) | 4.1.2, 2.1.1 | Include the file name in each control name; handle Space | NVDA names each control; Space toggles selection |
| 26 | Medium | Ten chooser buttons share the name "Browse templates" (V-F5) | 2.4.6 | Name each for its category | NVDA lists ten distinct names |
| 27 | Medium | S2 exposes two headings, mis-levelled, on a browse-and-filter gallery (V-F9) | 1.3.1 | Heading structure matching the visible sections | Heading list reflects tabs, filters and results |
| 28 | High | Buttons and icons fall below 3:1 against their backgrounds on S1 and S3 (V-F18) | 1.4.11 | Raise control boundary or fill contrast to 3:1 | Eyedropper measurement clears 3:1 |
| 29 | Low | Zoom control shows "100%" but announces "View options" (V-F19) | 2.5.3 | Include the visible text in the accessible name | Speech input activates it by its visible label |

## Recommendation

**Procure with a TAAP, subject to the four conditions above.**

- No task failed. Both essential tasks completed, so accommodation works
  rather than pretends.
- Most fixes are one-line attributes and status messages. One item is
  structural: accessible published output.
- Adobe already implements the right pattern elsewhere in the product. A
  correct named list sits on the same view as the broken grid, and their
  delete dialog announces while their export dialog does not.
- The ACR fails as evidence. Require a WCAG 2.2 replacement.

**Approval does not fit.** Five criteria rate Does Not Support, three at
Level A, and screen-reader users cannot choose or revise designs.

**Denial does not fit either**, for internal design work. Every tested
task completed and the remediation ask is small.

**Publishing is the exception.** For sharing content to an audience, the
evidence supports no approval at any level until the vendor fixes
published output. Conditions 1 and 2 hold regardless of the roadmap.

## Appendices

- Task tests and findings: `04-task-testing.md`
- Per-criterion results: `05-results.md`
- Evidence: `evidence/` (runs R001–R042), including raw axe JSON
- Vendor ACR as received: `vendor-acr/`
