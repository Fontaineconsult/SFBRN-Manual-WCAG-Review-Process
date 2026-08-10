# Task-Based Testing — Adobe Express

WCAG-EM 2.0 step 4: evaluate the selected sample set. Testing clusters around
the **tasks** (user stories / complete processes from `03-scope-and-sample.md`
§3.3), so findings read as *"this task fails at this step, because of these
WCAG criteria."* The per-criterion rollup in `05-results.md` cites the finding
IDs recorded here — record each finding once, here only.

Evaluation is against all five WCAG 2 conformance requirements at the target
level (WCAG 2.2 AA): (1) conformance level, (2) full pages, (3) complete
processes, (4) only accessibility-supported ways of using technologies,
(5) non-interference.

**Finding IDs:** `T<task>-F<n>` for task findings (T1-F2 = task 1, finding 2);
`V-F<n>` for view-sweep findings.

**Severity:** **Blocker** — the task cannot be completed by an affected user
group; **Major** — completion is substantially burdened; **Minor** — barrier
with a reasonable workaround.

**Task verdicts:** **Pass** — completable by all baseline combinations without
significant barriers; **Pass with barriers** — completable, but Major or Minor
findings exist; **Fail** — not completable by at least one affected user group
within the accessibility support baseline.

**Test runs & evidence:** every test session is logged as a run *before*
testing starts:

```
python scripts/review.py log-test adobe --view S1 --url <page-url> \
    --modality no-vision --tool jaws --baseline B1 [--task T1] [--tester NAME]
```

This records which page/view was tested, when, with which tool and baseline
(the WCAG-EM "evaluation specifics" record), appends to `evidence/test-log.md`,
and creates `evidence/runs/R###/` with a `run.md` for notes — JAWS
action/announced/expected notes or WAVE summary counts — and the run's
screenshots/exports (`R###-*.png`). Capture conventions per tool:
`ontology/testing-tools.md`. Findings below cite run IDs and files in their
**Evidence** row.

---

## A. Task clusters (WCAG-EM step 4.2 — complete processes)

One cluster per process in 03 §3.3. Walk the default sequence, then each
branch sequence, with each baseline combination (03 §1.3). Evaluate the
content that changes along the process — form and dialog interaction, input
confirmations, error messages, and other feedback are all in scope.

### Task T1 — Create a design from a template — process P1

| | |
|---|---|
| **User story** | As a user, I need to create a new design from a template or blank canvas, so that I can start my work. (F1, 03 §2.2 — the product's core purpose) |
| **Verdict** | Pass with barriers |
| **Baselines run** | B4 (NVDA 2026.1.1 / Chrome 150.0.7871.187) — run R013. B1 (JAWS), B2 (keyboard-only), B3 (zoom) not yet walked. |
| **Date(s) tested** | 2026-08-06 |

**Sequence to walk** (03 §3.3 P1). Every view is in the sample set:

| Step | View | Action to proceed |
|------|------|-------------------|
| 1 | S1 Home dashboard | Activate "Create" / template search |
| 2 | S2 Template gallery (Explore) | Select a template |
| 3 | S3 Editor | Template opens on canvas |

Branch **P1-a** from step 2: start from a blank canvas instead, re-entering
at step 3.

**Sequence notes** (walked 2026-08-06, B4/NVDA — run R013; barriers are
concentrated almost entirely at step 2):

- **Step 1, Home → activate Templates.** Operable. The failure is in
  *arrival*, not action: NVDA says "current page, current page", focus stays
  on the rail button, and the title does not change — no signal that a
  navigation happened at all → **T1-F1**.
- **Step 2, Explore / choose a template.** Where the task nearly breaks.
  The grid is not announced on entry; each template costs four tab stops
  with its name on a *different* stop from the item; arrowing between items
  is completely silent; items expose two conflicting roles; and the
  templates **have no identifiable name** → **T1-F2**. Heading navigation
  offers no help here either, because S2 exposes only two headings
  (V-F9). The surrounding chrome is fine — filters and content-type tabs
  are all reachable and announced (R013 O9) — so the defect is the grid
  itself, not the view.
- **Step 3, template opens.** Works. Selecting a template opens a modal
  whose `h2` carries the template's name, with reachable buttons
  (R013 O10). Notably this is where the name a user needed at step 2
  finally appears.

**Verdict reasoning.** Reviewer's judgement: *"we can complete, but it is
very hard to get to the templates area and navigate them."* Completable →
not *Fail*; substantial burden → **Pass with barriers**.

**The Fail case was considered and explicitly rejected — reviewer decision,
2026-08-06.** The user story is *create a design **from a template***, which
implies choosing a particular one; with no identifiable names (T1-F2) a
screen-reader user can create a design from *an arbitrary* template but
cannot deliberately select one. Sizing T1-F2 as a Blocker would have made
S2's no-vision cell **Broken**, which under modality-checks.md §Result
semantics *forces* this task's verdict to **Fail** for no-vision users. The
reviewer sized it **Major**, so the verdict stands at Pass with barriers.
Recorded so that a later reader can see Fail was available on this same
evidence and was a decision, not an oversight — and so that the S3 walk can
revisit it if the editor compounds the problem.

**Not yet walked:** branch P1-a (blank canvas instead of template), and
baselines B1/B2/B3. Barriers found here are AT-specific; the keyboard-only
and zoom walks may find different ones.

#### Finding T1-F1

| | |
|---|---|
| **Where** | Step 1 → 2 — navigating from S1 Home to S2 Explore via the left-rail Templates item |
| **Observed** | Activating the rail item announces only **"current page, current page"** — the nav item's own state, repeated. Focus **remains on the rail button**; it is not moved into the newly-rendered view. The document title does not change (it is "Adobe Express" on every view — V-F8). The reviewer's account: *"it is not clear we are on the templates page… we can inspect buttons and links to figure that out, maybe."* Three orientation mechanisms — title, focus, announcement — fail simultaneously, so the user receives no signal that a navigation occurred and must go exploring the page to deduce where they are. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 2.4.3 Focus Order (focus is left behind in the navigation while the main content is replaced); 2.4.2 Page Titled (via V-F8) |
| **Severity** | Major — the task remains completable, but the user must re-orient by inspection at every step of a multi-step process |
| **Evidence** | R013 O1 (reviewer, NVDA 2026.1.1) |

#### Finding T1-F2

| | |
|---|---|
| **Where** | Step 2 — S2 Explore, the lazily-loaded template grid: the exact control a user must operate to choose a template |
| **Observed** | Seven defects compounding on one control. (1) **The templates have no identifiable name** — the items a user chooses between cannot be told apart by ear. (2) **The thumbnails are absent from the accessibility tree entirely** — walking graphics with `G` finds *no graphics at all* on a view built from template images (R013 O12). Taken with (1), a template has **no perceivable identity whatsoever**: no name to hear, and no image to label. (3) Arrowing between items, the only efficient way through the grid, is **completely silent** — no announcement that focus moved to a new item. (4) Each item costs **four tab stops** (image → title → favourite → premium), so an item's *name* is a separate stop from the item itself. (5) Tabbing off the fourth stop **leaves the grid entirely, unannounced**. (6) Items expose **two conflicting roles** — announced as both a form element and a button. (7) The grid is **not announced on entry**, and lazily-loaded results arrive with no announcement. The name is not missing from the product — selecting a template reveals it as an `h2` (R013 O10) — it is simply not exposed at the point of choosing. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (no accessible name; conflicting roles); 1.1.1 (informative thumbnails carry no text alternative and are not exposed at all); 1.3.1 (grid structure and item boundaries not programmatically conveyed); 2.4.3 (focus order through each item and out of the grid); 4.1.3 (lazily-loaded results not announced); 1.3.3 (items distinguishable only by their visual thumbnail) |
| **Severity** | **Major** — reviewer decision 2026-08-06, taken with the Blocker option explicitly on the table (a Blocker here would have forced task T1 to Fail; see verdict reasoning above). The user can activate *a* template but cannot determine *which*; the reviewer judged that a severe burden rather than a barrier to completion. |
| **Vendor comparison** | Adobe claims 4.1.2 and 2.4.6 Does Not Support, and 1.3.1 / 4.1.3 Partially Supports. This is the strongest evidence found so far *supporting* their own negative claims — unlike S1, where independent testing repeatedly landed better than the ACR. |
| **A working reference exists in the same view** | The search field's results list — which opens below the search area and is a *different* component from the masonry grid — **is arrowable and its items are announced** (R013 O13, reviewer-confirmed as distinct from the grid). So the correct pattern is already implemented on this very view. The grid's silence is therefore not a platform limitation, not a constraint of web components, and not an NVDA quirk; it is a defect in one component with a working example beside it. This substantially raises what can reasonably be asked of the vendor in remediation. |
| **Root cause — identified 2026-08-06 (R011 O1, axe-core)** | The grid container is `<x-masonry role="row" aria-orientation="vertical">`. It declares **`role="row"` with none of its required parents present** (axe `aria-required-parent`, critical, wcag131: *"Required ARIA parents role not present: grid, rowgroup, table, treegrid"*), and `aria-orientation` is **not permitted** on that role (`aria-allowed-attr`, critical, wcag412). The results grid therefore announces itself as a table row belonging to no table. This single defect accounts for every symptom above: role semantics resolve incoherently inside an orphaned row (the dual form-element/button announcement); arrow-key navigation is silent because grid movement requires a valid grid ancestor; nothing is announced on entry because an orphaned `row` is not a landmark, region or list; and item boundaries carry no `row`/`gridcell` relationship. **This is the actionable form of the finding** — a vendor can fix "`role="row"` has no grid parent"; they cannot act on "the grid is hard to navigate". |
| **Evidence** | R013 O3–O8 (reviewer, NVDA 2026.1.1) — recorded **before** the axe triage, so the agreement is corroboration rather than confirmation bias. Root cause: R011 O1, `evidence/runs/R011/R011-axe.json`. |

### Task T2 — Author a design from scratch: add text, add an image, save — process P2

| | |
|---|---|
| **User story** | As a user, I need to edit content on the canvas (text, images, shapes) and export the finished design, so that I can produce and use my work. (F2 + F5, 03 §2.2 — the product's core purpose) |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B4 (NVDA 2026.1.1) — walk opening 2026-08-06 |
| **Date(s) tested** | |

**Sequence to walk** (03 §3.3 P2, adapted to the reviewer's chosen scenario
— authoring a *new* document rather than editing a prepared one, which
exercises the create flow and the empty-canvas starting state as well):

| Step | View | Action to proceed |
|------|------|-------------------|
| 0 | S1 / S2 | Create a new blank document (P1-a branch: blank canvas, not a template) |
| 1 | S3 Editor | Add a text element and set its content |
| 2 | S3 Editor | Insert an image from the asset panel |
| 3 | S3 Editor | Activate Download / Export |
| 4 | Export dialog | Choose a format, confirm |
| 5 | (download delivered) | Verify completion feedback |

Branch **P2-a** from step 2: upload own media, then insert.

**Why author from scratch rather than reuse the "Text Test" document
(reviewer's decision, 2026-08-06):** the existing test document holds a
single text object, which cannot exercise *adding* content, *inserting*
media, object-to-object navigation, or export. Authoring end to end is the
only way to answer whether a screen-reader user can actually produce
something — and it exercises the empty-canvas state, which no run has
touched.

**What is already known to sit on this path** (from R015, the S3 view
sweep — expect these to compound rather than appear fresh):

- Selecting an object announces only **"Canvas"**, identically for every
  object (R015 O9) — so step 2's "did my image land, and is it selected?"
  has no feedback mechanism.
- The route into editing an object is **Tab to layer → Enter → Enter**, and
  is announced nowhere (R015 O7).
- The text-editing toolbar that appears is **unlabelled** (R015 O6).
- The editing textarea itself has **no accessible name** (R015 O8).
- The editor has **no `main` landmark** and **no `h1`** (R014 O3).

**Unknown and specific to this walk:** whether an *inserted image* can be
given alt text at all — the single most consequential question for 1.1.1 in
an authoring tool, since it determines whether the product lets its users
produce accessible output. No run has touched it.

**Sequence notes** (walk in progress, run R016, B4/NVDA):

- **Step 0, create a blank document.** Completable by keyboard. Two
  barriers: option names are absent in **six of the seven** category tabs
  (T2-F1), and no confirmation is given of what was chosen. Arrival is
  announced — "Loading Document, Untitled, Untitled" — though focus
  placement is not. Renaming by keyboard works cleanly.
- **Step 1, add a text element. Passes on every count** (R016 O5): the
  control is in NVDA's lists *and* Tab-reachable, activation announces
  "edit selected add text", edit mode is entered automatically, and the
  content can be confirmed by ear.
- **Step 2, insert an image.** "Add a photo" and "Generate with AI" are both
  findable, but **neither reports success** (T2-F2) — and the same panel
  announced text insertion one step earlier. Selected objects announce only
  "Canvas Graphic": a generic role, no identity, so **the element being
  edited cannot be determined** (R016 O8). The layers region — the only
  route back to existing objects — is absent from NVDA navigation and
  reachable only by a long tab traversal (R016 O9).
- **Steps 3–5, export.** Not yet walked.

#### Finding T2-F1

| | |
|---|---|
| **Where** | Step 0 — the "Get started" create chooser, category tabs |
| **Observed** | Options in **six of the seven** category tabs announce as **"Clickable Figure Template Button"** with no distinguishing name — Social media and ads, Video, Photo, Document, Webpage, Print. Only **Standard & Suggested**, which is the tab open by default, names its options (R016 O1, reviewer, NVDA 2026.1.1). Activating a choice gives no confirmation of what was selected before the view changes (R016 O2). So a user gets a working first impression and finds every subsequent category unusable by name. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (controls without accessible names); 1.1.1 (the thumbnail is the only differentiator and carries no text alternative) |
| **Severity** | Major — the user can create *a* document but can meaningfully choose only from the default tab |
| **Note** | Distinct from V-F5, which concerns ten identically-named "Browse templates" buttons in the same modal. V-F5 is many controls sharing one unhelpful name; this is controls with no name at all. Assistant corroboration was attempted and failed (chooser would not reopen programmatically); reviewer testimony stands. |
| **Evidence** | R016 O1, O2 |

#### Finding T2-F2

| | |
|---|---|
| **Where** | Step 2 — inserting an image via "Add a photo", and generating one via "Generate with AI" |
| **Observed** | Both controls are findable by keyboard, but **neither reports whether the image was successfully placed or generated** (R016 O7). Nothing announces insertion, completion, or failure. The inconsistency is what makes this clear-cut: **one step earlier, in the same panel, adding *text* announced "edit selected add text"** — the product knows how to report insertion and does so for one content type and not the other. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.3 Status Messages |
| **Severity** | Major — and worse for **"Generate with AI"**, which is an asynchronous operation taking many seconds with no progress, completion or error announcement, so "still working", "finished" and "failed" are indistinguishable. That is also the product's most heavily promoted capability (03 §2.2, F8). |
| **Pattern** | Third instance of this exact defect in the review: S2's lazily-loaded template grid, S2's search results, and now image insertion/generation. All 4.1.3, all "the app did something and did not say so". |
| **Evidence** | R016 O7 |

---

## B. View sweep (WCAG-EM step 4.1 — per-view modality checks)

Every sampled view (03 §3.1/§3.2) is checked under **every sensory/functional
modality** (Section 508 Functional Performance Criteria: no-vision,
low-vision, no-color, no-hearing, no-speech, motor, cognition) using the
standardized per-view checklists in `ontology/modality-checks.md`, plus a
WAVE sweep per view. One run per view×modality (`log-test --modality`), with
the run's **Result** set to Works / Works with issues / Broken / N/A.
Failures become findings below, citing the check ID (e.g., `MO4`) and run ID.

`review.py matrix adobe` shows the views × modalities grid and remaining
gaps; `validate` fails while cells are unrun or results unset.

Check the full view — all components and significant states — without
initiating processes (those are covered in §A). Repeated components (header,
navigation, footer) need re-checking only where they appear or behave
differently.

### View S1 — Home dashboard

| | |
|---|---|
| **Baselines run** | B3 (R002, partial), — (R003, R005, R006, R007 wave-blind, R009 axe, R010 cognition partial), B2 (R004, partial); B1/JAWS in progress (R001, walkthrough W2–W3 done) |
| **Date tested** | 2026-08-04 (assistant-driven trials + axe sweep; reviewer walkthrough in progress); 2026-08-06 (assistant measurement pass — resolved axe-incomplete items, target-size geometry, animation inspection) |
| **Findings** | V-F1, V-F2, V-F3, V-F4 |

**Criteria positively evidenced on S1 (measured, no finding)** — recorded so
the report can show what was verified, not only what failed:

| Criterion | Basis | Run |
|---|---|---|
| 2.5.8 Target Size (Minimum) | 51 targets enumerated; 5 under 24px, all clear the spacing exception (nearest neighbour 104px) | R004 O4 |
| 1.4.3 Contrast — Adobe app bar | 8 labels measured 11.18:1–11.71:1 by canvas-sampling the background SVG | R009 O8 / R002 O6 |
| 2.2.2 Pause/Stop/Hide — steady state | 0 animations page-wide at 68s; rotator static across 16s + 27s windows (load window still open) | R010 O1 |
| 4.1.2 / 3.3.2 — search control | stable `aria-label`; rotator `aria-hidden`, not in a live region | R010 O2 |

**Open on S1, with the instrument named** (not deferred vaguely): 5 headings
over card art need rendered-pixel contrast sampling (R009 O9a); the rotation's
first ~16s after load needs a human watch (R010 O1); 2.5.3 Label in Name is a
live candidate on the search field (R001 O8); the reviewer walkthrough
W4–W18/W20 still gates R001, R002, R004 and R010.

#### Finding V-F1

| | |
|---|---|
| **Where** | S1 Home dashboard — left-rail hover flyout ("Get inspired" panel on rail items) |
| **Observed** | Hover content violates all three 1.4.13 conditions observed: moving the pointer onto the flyout dismissed it (not hoverable); Esc did not dismiss it (not dismissible); once stuck, it persisted indefinitely over page content through unrelated interactions. Assistant-driven (synthetic hover teleports) — confirm with continuous pointer movement. |
| **Affected users** | Low-vision magnification users (flyout obscures content they cannot reposition around); motor-impaired users relying on Esc |
| **WCAG criteria failed** | 1.4.13 |
| **Severity** | Major |
| **Evidence** | evidence/runs/R002/R002-flyout-hover.jpg, evidence/runs/R003/R003-grayscale-home.jpg (flyout still open minutes later) (runs R002, R003) |

#### Finding V-F2

| | |
|---|---|
| **Where** | S1 Home dashboard — Upload card, "browse" link ("Drag and drop files or browse") |
| **Observed** | 11px link text at 3.96:1 computed contrast against the card background (4.5:1 required). CONFIRMED by two independent instruments: computed-style measurement (R002) and axe-core `color-contrast` violation on the same `.browse-text` node (R009). Consistent with vendor ACR "Does Not Support" for 1.4.3. |
| **Affected users** | Low-vision users |
| **WCAG criteria failed** | 1.4.3 |
| **Severity** | Minor |
| **Evidence** | evidence/runs/R002/R002-upload-card-browse.png (run R002); evidence/runs/R009/R009-axe.json (run R009) |

#### Finding V-F3

| | |
|---|---|
| **Where** | S1 Home dashboard — page-level keyboard entry (Adobe cross-product app-switcher bar precedes all content) |
| **Observed** | No skip link on first Tab; ~15 observed Tab stops remained in the app-switcher bar region before any Express content. Assistant-driven with a focus-attribution caveat (run R004 O3) — reviewer keyboard confirmation still pending (W14). AMENDED 2026-08-04 (R001 O7): landmark walk found Apps[nav]/banner/Primary[nav]/main/search — SR users can bypass via landmarks (sufficient technique ARIA11), so the barrier is keyboard-only (non-AT) users. Reviewer decision pending: does 2.4.1 stand as a failure (no keyboard-reachable mechanism) or reclassify as advisory barrier with 2.4.1 = Supports? |
| **Affected users** | Keyboard-only users without AT (every page visit); screen reader users NOT affected (landmarks, R001 O7) |
| **WCAG criteria failed** | 2.4.1 |
| **Severity** | Major |
| **Evidence** | evidence/runs/R004/R004-tab5-focus.jpg, R004-tab15-plusbutton-focus.jpg (run R004) |

#### Finding V-F4

| | |
|---|---|
| **Where** | S1 Home dashboard — header, community/people icon button (`x-community-discovery-trigger` → icon-only `sp-action-button`) |
| **Observed** | The button exposes `role="button"` with no accessible name — its only content is an `aria-hidden` icon with an empty label. A screen reader user hears "button" with no purpose. **CONFIRMED BY REVIEWER 2026-08-06 (R012 O1, NVDA 2026.1.1, baseline B4):** narrated unprompted as buttons remaining unnamed, then confirmed on enumeration as *"only control is Community unnamed."* Three independent instruments agree: NVDA by ear, Chrome's accessibility tree (the sole unnamed interactive node of 48 exposed), and axe-core. Vendor claims Does Not Support for 4.1.2 — consistent. |
| **Affected users** | Screen reader users (confirmed for NVDA; JAWS untested on this control — R001 suspended before W5) |
| **WCAG criteria failed** | 4.1.2 |
| **Severity** | Major |
| **Scope** | One control, but on **every view — widened 2026-08-06**. Originally recorded as "one control on S1"; the S2 sweep found the identical node at the identical path (R011 O2), which established that it lives in the **persistent app header** (`af-headerbar` → `x-community-discovery-trigger`), not in S1's content. So a user meets it on every page of the product. The defect count does not grow; its reach does. The broader hypothesis — that Spectrum components mis-map names generally — was **tested and refuted**: every other interactive control on S1 carries a correct accessible name (R012 O1). An assistant DOM-walk estimate of 11 unnamed controls was wrong and is withdrawn. |
| **Evidence** | evidence/runs/R009/R009-axe.json (run R009, violations[0]); reviewer confirmation R012 O1 |

#### Finding V-F5

| | |
|---|---|
| **Where** | S1 — **"Get started" modal** (create chooser), opened from "Start new design". This is the modal state listed in the enclosure for S1, tested for the first time on 2026-08-06. |
| **Observed** | **Ten** `sp-button` controls in the chooser grid all carry the identical accessible name **"Browse templates"** — verified in Chrome's accessibility tree, so this is what the screen reader actually receives, not a DOM inference. Visible text matches the accessible name on every one. Navigating by button list, a screen reader user hears "Browse templates, button" ten times with nothing to tell them apart; the only thing distinguishing them is the category card each sits inside, which is conveyed visually by proximity. Reviewer narrated this independently as "many generic 'Browse Templates' buttons with no meaningful name" (R012 O10, NVDA 2026.1.1) before the count was taken. |
| **Affected users** | Screen reader users; also users of speech input and any user relying on a list-of-controls view rather than visual layout |
| **WCAG criteria failed** | 2.4.6 (labels do not describe purpose). 1.3.1 additionally if the button→category association is not programmatically determinable — **to be confirmed** |
| **Severity** | Major — the user can operate the control but cannot tell which of ten it is, so choosing a template category by screen reader is guesswork |
| **Not 2.5.3** | Explicitly checked and **excluded**: visible label and accessible name are identical, so Label in Name is satisfied. The defect is the label's content, not a mismatch. |
| **Evidence** | R012 O10 (reviewer, NVDA); accessibility-tree enumeration recorded in R012 (10/10 controls, `sp-button`, grid positions captured) |

#### Finding V-F6 — **WITHDRAWN 2026-08-06, not a defect**

| | |
|---|---|
| **Status** | **Retracted before reaching the report.** Raised on a misreading, withdrawn the same session on reviewer clarification. The ID is retained and never reused (IDs are stable once assigned). |
| **Was claimed** | That the "Get started" modal failed to contain focus, letting Tab escape into the page behind while the dialog was open (2.4.3, Major). |
| **Why it was wrong** | The reviewer's phrase "focus is not trapped" was an answer to the **MO3** check — *can you always get out of a widget?* — which the modal passes. The assistant re-read it as focus escaping into background content. On checking, the actual behaviour is *"cycling tab at the end moves to main browser controls then circles back to modal"*: focus cycles modal → browser chrome → modal and never reaches page content behind. That is **correct** modal containment. |
| **Actual outcome** | The modal contains focus correctly, moves focus in on open, and closes on `Esc` (R012 O8, O13) — it is well-behaved on every focus property tested. |
| **WCAG criteria failed** | none — withdrawn, no criterion failed |
| **Severity** | none — withdrawn |
| **Evidence** | R012 O13 (reviewer clarification retracting the original reading) |

#### Finding V-F7

| | |
|---|---|
| **Where** | S1 — card graphics throughout the home dashboard (walked with `G`) |
| **Observed** | Images announce in the pattern **"Clickable Figure {name of figure}, Unlabeled Graphic"** (R012 O14, NVDA). The wrapping figure supplies a meaningful name, then an inner image with no alternative and no decorative marking is announced as "Unlabeled Graphic". Information is not lost — the figure name carries the meaning — but every card emits an extra unnamed graphic announcement. Under 1.1.1, images that add nothing must be hidden from assistive technology (`alt=""` / `aria-hidden`). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.1.1 |
| **Severity** | Minor — verbosity on every card rather than lost information; the figure name provides the alternative |
| **Vendor corroboration** | Adobe's ACR concedes 1.1.1 Partially Supports and cites the same defect class in its own words — *"The decorative image is not hidden from screen readers"* — on a different screen. This finding evidences it on S1. |
| **Evidence** | R012 O14 (reviewer, NVDA) |

---

### View S2 — Explore / template gallery

| | |
|---|---|
| **Baselines run** | B4 (NVDA 2026.1.1) — R013; automated sweep R011 (axe-core, 4 violations / 4 incomplete, not yet triaged) |
| **Date tested** | 2026-08-06 |
| **Findings** | V-F9; plus T1-F2 (recorded in §A because it blocks a process step, not merely the view) |

#### Finding V-F9

| | |
|---|---|
| **Where** | S2 Explore — whole-view heading structure |
| **Observed** | The heading list contains **only two entries: "Explore" and "Filters"** — the reviewer's words, *"nothing useful."* S1 by comparison exposes ten headings including a level-1 (R012 O5), so this is not a product-wide pattern but a defect specific to this view. Explore is a browse-and-filter gallery with visible section structure — content-type tabs, filter groups, a results grid — none of which is reachable by heading navigation. For a screen-reader user, heading navigation is the primary way to survey and orient within an unfamiliar view, and on this view it yields almost nothing, which is a direct contributor to why step 2 of task T1 is so hard (T1-F2). |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1 — visually-conveyed section structure is not programmatically determinable |
| **Severity** | Major |
| **Corroboration** | axe independently flagged `heading-order` on `<h3>Filters</h3>` — an `h3` with no `h1` or `h2` above it (R011 O3). That rule is tagged best-practice rather than a WCAG criterion, so it is **not** the basis of this finding, but it establishes that S2's headings are not merely *sparse* — they are also **mis-levelled**, starting at level 3 with nothing above. |
| **Evidence** | R013 O2 (reviewer, NVDA 2026.1.1); R011 O3 (axe-core, supporting) |

---

### View S3 — Editor ("Text Test" document)

| | |
|---|---|
| **Baselines run** | automated sweep only so far — R014 (axe-core, 7 violations / 3 incomplete, triaged). No modality run yet. |
| **Date tested** | 2026-08-06 |
| **Findings** | V-F10 |

#### Finding V-F10

| | |
|---|---|
| **Where** | S3 Editor — the page-navigation "more" menu button (`sp-button#more-menu-button`, `data-testid="page-nav-more-menu-button"`, inside `x-mini-page-navigation`) |
| **Observed** | The control has **no accessible name by any mechanism** — no visible text for a screen reader, no `aria-label`, no `aria-labelledby`, no `title` (axe `aria-command-name`, serious, wcag2a/wcag412 — R014 O1). A screen reader user reaches a button and hears only "button", with no indication that it opens page-management options. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 |
| **Severity** | Major |
| **Relationship to V-F4** | **A distinct defect, not a recurrence.** V-F4 is the community icon in the shared *home* header; this is an editor-specific control on the page navigation. Same rule and criterion, different component and view — so this is the **second** unnamed control found in the product, and it establishes that unnamed icon-buttons are a pattern across teams rather than a single oversight. |
| **Status** | Assistant-driven (axe). **Reviewer confirmation by ear still wanted** in the S3 no-vision run — S1 showed axe and NVDA agreeing on names, but also showed an NVDA elements-list rendering that nearly produced a false finding (R012 O9), so names are confirmed on focus, not from a list. |
| **Evidence** | `evidence/runs/R014/R014-axe.json` (run R014, O1) |

---

### All sampled views — product-wide findings

Findings that are properties of the view *set* rather than of one view.
Recorded once here rather than repeated per view.

#### Finding V-F11

| | |
|---|---|
| **Where** | Every sampled view — S1 Home, S2 Explore, S3 Editor, S4 Your stuff. Components: `x-home-row-scroller`, `x-simple-row-scroller`, `sp-grid`, `x-masonry`. |
| **Observed** | Two related defects in how the product marks up its content rows and card collections. **(1) Grids are unnamed: 17 of the 18 grids found across the four sampled views carry no accessible name** — no `aria-label`, no `aria-labelledby`. The sole exception is the editor's layers list. A screen-reader user enters what is announced as a grid or table with no indication of what it contains; the reviewer's words: *"the tables don't have a summary so I don't know what the table area is about"* (R015 O10, NVDA 2026.1.1, corroborated in the DOM and the accessibility tree). **(2) `role="grid"` is applied to non-tabular content** — these are horizontal card carousels (template rows, asset rows, file lists) with no meaningful row/column relationship, so the markup asserts a structure the content does not have and imposes grid-navigation semantics on what is simply a list of choices. Separately, `role="row"` elements with **no `grid`/`table`/`rowgroup` ancestor** occur on S1 (2), S2 (3) and S4 (1) — the same orphaned-row defect axe flagged as a critical `aria-required-parent` violation on S2 and which is the root cause of T1-F2. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 1.3.1 — relationships conveyed through presentation are not correctly determined programmatically, in both directions: real grouping is unnamed, and a tabular structure is asserted where none exists |
| **Severity** | Major |
| **Precision note for the report** | These are **not** HTML `<table>` elements used for layout — that older discouraged practice would require `role="presentation"`. They are ARIA `role="grid"`, a legitimate pattern being **misapplied**. State it as "grid semantics on non-tabular content, 17 of 18 unnamed"; "tables used for navigation" is easy for a vendor to rebut and is not what the markup does. Likewise `summary` is the obsolete HTML4 table attribute; the modern equivalent is `aria-label`/`aria-labelledby`. |
| **Remediation is cheap, which strengthens the case** | Every one of these sections already has an adjacent heading that **is** exposed to AT — "Templates", "Photos", "Design assets", "Quick edits", "File formats". A single `aria-labelledby` per grid, pointing at the heading already present, would name all of them. The information exists and is simply not wired up. |
| **Counts are floors, not totals** | S1/S2/S4 were measured shortly after navigation and lazy-load on scroll, so more grids may exist. S3's 12 reflects a fully-rendered panel. The robust result is the ratio — essentially none are named. |
| **Evidence** | R015 O10 (reviewer observation + assistant enumeration across four views, 2026-08-10); R011 O1 (axe `aria-required-parent`, S2) |

#### Finding V-F8

| | |
|---|---|
| **Where** | Every SPA view in scope. Confirmed on Home (S1), Explore (S2), Your stuff (S4) and Brands. |
| **Observed** | The document title is the string **"Adobe Express"** on every view; it never changes as the user moves between them. Reviewer-reported with NVDA 2026.1.1 — *"Adobe Express is all that's announced as Title for every page"* — and independently corroborated by the assistant navigating four views and reading `document.title` at each: **4 views, 1 distinct title.** The single exception is an opened document, which does retitle (e.g. "Untitled - August 06, 2026 at 13.02.17"), showing the app *can* set titles and simply does not for its main views. |
| **Affected users** | Screen reader users above all — the title is the primary announcement of "where am I now", so moving Home → Explore → Your stuff produces no signal that the view changed at all. Also anyone using multiple tabs, browser history, or bookmarks, where every entry reads identically. |
| **WCAG criteria failed** | 2.4.2 Page Titled — titles must describe topic or purpose. "Adobe Express" names the product, not the view. |
| **Severity** | Major — it removes the standard orientation cue on every navigation in the product. Not a Blocker: each view's `h1`/heading structure is sound (R012 O5), so an oriented user can re-establish position by walking headings. |
| **Note on scope** | This is exactly the class of defect a per-view sweep can miss — each view in isolation *has* a title, and only comparing views reveals that they are all the same. Found because the reviewer noticed across views, not within one. |
| **Evidence** | R012 O16 (reviewer, NVDA, across views); assistant title comparison across S1/S2/S4/Brands recorded in R012 |

---

## C. Sample comparison (WCAG-EM step 4.3 — random vs structured)

Check that the random samples (03 §3.2) show no content types or findings
absent from the structured set. If they do, the structured sample was not
representative: return to step 3, extend the sample set, and test the
additions. Repeat until no new types or findings appear.

| Random sample | New content type? | New findings? | Action taken |
|---------------|-------------------|---------------|--------------|
| R1 | | | |

---

## D. Coverage check

Before moving to `05-results.md`:

- [ ] Every process in 03 §3.3 has a task cluster with a verdict
- [ ] Every branch sequence was walked, not just default sequences
- [ ] Every non-process sample has a view-sweep entry
- [ ] Every finding names at least one WCAG criterion, a severity, and evidence
- [ ] Random-vs-structured comparison completed (and sample extended if needed)
- [ ] `05-results.md` updated: every failed criterion cites finding IDs from this file
