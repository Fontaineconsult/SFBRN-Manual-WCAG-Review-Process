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
| **Verdict** | Pass with barriers |
| **Baselines run** | B4 (NVDA 2026.1.1 / Chrome 150 then 151) — R016 steps 0–2, R037 export, R038 authoring at scale |
| **Date(s) tested** | 2026-08-06 (steps 0–2), 2026-08-14 (export; multi-object authoring) |

**Verdict — reviewer decision 2026-08-14 (W17).** Reviewer's words:
*"this requires TAAP and vendor roadmap, but pass."*

**Recorded as "Pass with barriers" rather than plain "Pass", and the
reason is stated so the reviewer can correct it in one word.** The task
vocabulary is fixed (CLAUDE.md): *Pass* means completable **without
significant barriers**, which by definition would support an **Approved**
procurement decision and no TAAP. The reviewer's own sentence requires a
TAAP and a vendor roadmap, and four findings stand against this task —
three of them Major (T2-F1, T2-F2, T2-F4) plus one Minor (T2-F3). *Pass
with barriers* — "completable, but Major or Minor findings exist" — is the
term that carries the reviewer's meaning. The judgement is theirs; only
the vocabulary was adjusted to match it.

**Why not Fail, given the reviewer was leaning that way earlier.** The
scale evidence came in (R038) and it cut both ways: authoring a
five-object design *is* completable by a screen-reader user — every step
was walked to completion, and the export flow proved the best-behaved in
the review. What R038 established is that it is **punishing**, not
impossible: a five-step probe per object, an expert AT command
(`NVDA+F2`) mid-sequence, and no visited-state tracking. Under
modality-checks.md, *Fail* requires the task to be **not completable** by
an affected group within the baseline; it was completed. The reviewer's
landing point — completable, but only with accommodation and vendor
commitment — is exactly what *Pass with barriers* plus **Needs TAAP**
encodes.

**Recorded so a later reader sees Fail was live and was decided, not
missed.** As with T1, the harsher verdict was available on this evidence.
The reviewer considered it explicitly on 2026-08-14 (*"I'm leaning toward
fail… authoring a meaningful document… would be nearly impossible at
scale for a blind user"*), commissioned W18 to test that claim rather than
assert it, and revised toward Pass with barriers once the walk completed.
That sequence — hypothesis, test, revision — is the strongest part of this
task's record.

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
- **Steps 3–5, export. Walked 2026-08-14 (run R037, B4/NVDA, Chrome 151).
  The best-performing step of the whole walk.** Export is completable by a
  screen-reader user: format options are reachable and labelled, the
  popover is fully tabbable, Escape dismisses it cleanly, and **download
  progress and completion are announced** (with beeps). Formats offered:
  **PDF, images, MP4**. Two barriers, both orientation rather than
  operability: neither the export popover nor the subsequent "downloading"
  dialog is announced *as* a dialog, and the download dialog's **Cancel**
  is discoverable only by enumerating the button list (T2-F3). One credit:
  **video export carries CC** (R037 O5).

**The 4.1.3 prediction failed here, and that is recorded deliberately.**
Four prior instances made a silent export look near-certain; instead the
user is informed. The honest qualifier: the feedback comes from the
**browser's** download UI, not from Express, so it satisfies the user need
without being evidence that the product emits status messages (R037 O3).

**What the export walk found instead is worse and lies outside the task.**
Asked to settle which output formats exist, the walk established that the
product publishes **webpages** — and that those published pages are
imperceptible to screen readers (**V-F16**). The task passes; its output
does not.

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

#### Finding T2-F3

| | |
|---|---|
| **Where** | Steps 3–5 — the export/download flow: the Download/Share popover, and the "downloading" progress dialog that follows it |
| **Observed** | **Two dialogs, neither announced as one.** The export UI is `<hz-themed-overlay open>` → `<sp-popover open>` → `<x-export-popover-content tabindex="0">` — markup supplied by the reviewer — and conveys no dialog role, so a screen-reader user is not told a dialog opened. A second "downloading" dialog then appears, likewise unannounced, and it contains a **Cancel** control that "would not be knowable unless a user inspects the button list" (R037 O1, O4). **Scope is deliberately narrow, because most of this flow works:** the popover is *fully tabbable*, Escape dismisses it cleanly, format options are reachable and labelled, and download progress and completion are announced. The defect is orientation — being told what opened — not operability. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 (dialog role not conveyed, on two dialogs); 4.1.3 (the downloading dialog's appearance is a status change that is not announced) |
| **Severity** | **Minor** — the task completes, every control is reachable, and Escape works. The sharper edge is the undiscoverable **Cancel**: on MP4 export, the long-running format, a user cannot readily abort an operation in progress. Sized Minor rather than Major because no step is blocked and a reachable workaround (Escape, or completing the export) exists in every case. |
| **Contrast with the rest of the product** | Worth stating in the report: this is the **best-behaved flow tested in the whole review**. Elsewhere the pattern is "the app did something and did not say so"; here the app does say so. The remaining gap is small and specific. |
| **Evidence** | R037 O1, O4 (reviewer, NVDA 2026.1.1, Chrome 151) |

#### Finding T2-F4

| | |
|---|---|
| **Where** | S3 Editor — locating and editing a **specific** object on a canvas holding several. Walked 2026-08-14 on a five-object document (three text boxes "text 1/2/3", a shape, a photo) with the task: **find "text 2" and edit it, screen reader only** (run R038). |
| **Observed** | **No canvas object can be identified.** Reaching one requires: NVDA's form-fields list → a control named **"Edit page"** → Tab into the re-order layers area (R038 O1). Arrowing the layers announces, for every object identically: `not selected @hz/shared-ui-components:sortable-list-press-space-to-grab row 1 column N` — **an untranslated localisation key read aloud as the control's name**, plus a grid coordinate, and **no indication of what the layer is** (O2). Enter gives "canvas graphic"; Space *sometimes* opens the Edit pane, whose summary hints at the object's **type** but never its **identity** (O3). Reading the content — the only thing separating "text 2" from "text 1" — requires **NVDA's pass-through (`NVDA+F2`) followed by Enter**, because the product never tells the screen reader that the focused thing warrants focus mode (O4). Then exit and repeat, **with no record of which layers have been visited**, since every row sounds the same. |
| **The crux — there is no read-only way to inspect the canvas** | Reading an object's content is possible **only from inside edit mode** (R038 O6). So identification is not an inspection operation at all — it is an *editing* operation, performed repeatedly on objects the user does not intend to change. A sighted user identifies all five objects by looking: free, instant, non-mutating, parallel. The screen-reader equivalent is serial, five steps per object, and mutating in kind. **The asymmetry is in the kind of operation available, not in its speed** — which is why the barrier does not simply grow with document size. Cost of finding a known object: *n/2 edit-mode entries on average*, with no visited-state to bound the search. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | **4.1.2** — canvas objects expose no name; layer rows expose a developer message ID as their name; role is not exposed in a way that triggers the AT's focus mode. **1.3.1** — a one-dimensional layer stack is announced as "row 1, column 1–5" (grid semantics on non-tabular content; corroborates V-F11). **2.4.3** — the route in runs through a control named for a different purpose. |
| **Structural exposure — recorded, not claimed** | Because inspection requires entering a *mutable* state, a stray keystroke during a search lands in document content. **This was not observed**, and a prior hypothesis of exactly this shape ("invisible editing", R015 O5) was raised and **withdrawn** when the reviewer explained the change had been made with a mouse. It is noted as a property of the interaction design — read-requires-write — not as evidence of data loss. A deliberate test would be needed to say more. |
| **Also engages conformance requirement 4** | *"Only accessibility-supported ways of using technologies."* A technique that works **only when the user suppresses their assistive technology's normal behaviour** is a poor candidate for accessibility support. Recorded distinctly from the criterion failures: the keystroke does reach the application, so **2.1.1 Keyboard is met** — the weaker claim is about the *method*, not about operability. First time this review has engaged one of the five conformance requirements beyond the criterion level. |
| **Severity** | **Major — with Fail available at the task level, and that is the reviewer's call (W17).** The task *is* completable, so this is not sized Blocker. What it costs: a five-step probe per object, an expert AT command mid-sequence, and no visited-state tracking, on a document of five objects — the smallest realistic size. |
| **2.1.1 was considered and is NOT failed — twice now** | Recorded so a later reader sees it was checked, not missed. The assistant's first 2.1.1 Blocker was withdrawn on 2026-08-06 when the reviewer found the Tab→Enter→Enter route; the same conclusion was available again here from *"I can't figure out how to do that without a click"*, and was again wrong. On this product, **"I can see no route" has been mistaken every time it has been thought** — the mechanism is created on demand or gated behind AT behaviour, not absent. |
| **Remediation — one fix collapses the whole procedure** | **Give each layer row an accessible name carrying the object's identity** ("text 2", "Photo — beach.jpg", "Rectangle"). The information exists; the row is where it belongs. That single change removes the per-object probe, supplies visited-state tracking for free (the user tracks by name, not memory), and makes the pass-through unnecessary for *identification*. Separately and trivially: **resolve the `@hz/shared-ui-components:sortable-list-press-space-to-grab` key to real text**, and expose the canvas surface with a role that triggers focus mode. |
| **Evidence** | R038 O1–O5 (reviewer, NVDA 2026.1.1); extends R015 O2/O3/O9 and R016 O8/O9 from one object to five |

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

#### Finding V-F1 — **WITHDRAWN 2026-08-14, not a defect**

| | |
|---|---|
| **Status** | **Retracted before reaching the report**, on reviewer confirmation with a real pointer. The ID is retained and never reused (IDs are stable once assigned). |
| **Was claimed** | That the S1 left-rail hover flyout violated all three 1.4.13 conditions — not hoverable (moving onto it dismissed it), not dismissible (Esc did nothing), and persistent over content through unrelated interactions. Recorded Major. |
| **Why it was wrong** | The evidence was **assistant-driven synthetic hover teleports** — the pointer was jumped between coordinates rather than moved continuously. That is not how a hover interaction works: a flyout that dismisses when the pointer *teleports* away can behave correctly when the pointer *travels* onto it along a path. The finding recorded this caveat at the time and explicitly requested pointer confirmation. |
| **Actual outcome** | Reviewer, 2026-08-14, with continuous pointer movement: **"no issues with hover, pass it."** (R002 O-LV17). LV6 passes. |
| **WCAG criteria failed** | none — withdrawn. **1.4.13 moves from Does Not Support to Supports**, which also removes one of the criteria previously recorded as *worse than the vendor claimed*. |
| **Severity** | none — withdrawn |
| **Why this is worth keeping in the record** | It is the **fourth** assistant hypothesis retired by reviewer testing on this review, after the 2.1.1 "pointer-only editing" Blocker, "invisible editing", and the claim that the editor lacks landmark bypass. All four were caught before reaching the report, each because the assistant recorded its own instrument's limitation and routed the item for confirmation. The pattern is now firm enough to state as method: **assistant-driven *interaction* findings on this product must be reviewer-gated**; assistant *measurement* (contrast, geometry, reflow, name comparison) has held up well. |
| **Evidence** | R002 O-LV17 (reviewer confirmation retracting the original reading); superseded: R002 O4/O5, evidence/runs/R002/R002-flyout-hover.jpg, evidence/runs/R003/R003-grayscale-home.jpg |

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
| **Observed** | **Reviewer-confirmed with a physical keyboard, 2026-08-13 (R004 O5): no skip link; 19 Tab stops to reach the left rail, 33 to reach the Recent strip.** The original assistant trial (~15 stops, focus-attribution caveat) is superseded by these hand counts. AMENDED 2026-08-04 (R001 O7): landmark walk found Apps[nav]/banner/Primary[nav]/main/search — SR users can bypass via landmarks (sufficient technique ARIA11), so the barrier is keyboard-only (non-AT) users. Reviewer decision pending: does 2.4.1 stand as a failure (no keyboard-reachable mechanism) or reclassify as advisory barrier with 2.4.1 = Supports? |
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

#### Finding V-F14

| | |
|---|---|
| **Where** | S3 Editor — canvas object manipulation |
| **Observed** | **Rotation and non-text resize cannot be done with the keyboard.** Reviewer-tested under B2 (R031 O4/O7): translation works, z-order works (via the "…" menu), and *text* can be resized through the Edit panel's size controls (with a defect of their own — the +/− steppers announce no resulting size). But **rotation (any object) and canvas resize (the corner-drag) have no keyboard route at all** — for shapes and images, "only translate is available." Core canvas operations are pointer-drag only with no alternatives exposed. |
| **Affected users** | Keyboard-only users, screen reader users, anyone who cannot perform precise drags (tremor, switch access) |
| **WCAG criteria failed** | **2.1.1 Keyboard (Level A)**; 2.5.7 Dragging Movements (AA — one of the six criteria the vendor ACR never addressed); **2.5.1 Pointer Gestures (Level A — added 2026-08-14)** |
| **Three criteria, three different reasons — added 2026-08-14 (R031 O8)** | Keep these distinct in negotiation, because a vendor can concede one and miss the others. **2.1.1** fails for want of a **keyboard** route. **2.5.7** fails for want of a **non-dragging** alternative. **2.5.1** fails for want of a **single-pointer non-path** alternative — rotation is performed by *"pressing and holding on the rotate button… then moving the finger in an arc"*, and the arc **is** the input, which is the defining property of a path-based gesture. The "essential" exception does not apply: a numeric angle field would do the same job, so the gesture is not intrinsic to the task. |
| **Severity** | Major — designs requiring rotated or resized non-text elements cannot be authored without a pointer, and cannot be authored *precisely* by anyone |
| **Remediation** | Reviewer's own formulation, adopted and sharpened 2026-08-14: a **dedicated transform panel** — *"a 'Translate' tool window that would allow, using a slider, X, Y, Z or Rotate, or resize"* — with typed/announced values. **One control closes all three criteria at once**, which makes it the highest-leverage item in the exhibit. The reviewer's own assessment of the ask: *"low hanging fruit for the dev."* |
| **Evidence** | R031 O4, O7, **O8** (reviewer, B2; O8's touch description is device-context evidence made outside the declared baselines — the *absence of an alternative* is the B2 result) |

#### Finding V-F15

| | |
|---|---|
| **Where** | S3 Editor — the "T" single-character shortcut (creates a text box) |
| **Observed** | A single-character key shortcut is active in the editor, and **no mechanism exists to turn it off or remap it**: Settings (C6) was opened and checked — it is keyboard-reachable (a positive) but contains no keyboard-customization options (R031 O5/O7). 2.1.4 requires single-character shortcuts be disable-able, remappable, or active only when the relevant component has focus. The focus-scoping defense is untested but implausible here, since the canvas cannot receive focus at all (R015 O2). |
| **Affected users** | Speech-input users (a spoken word containing "T"-adjacent recognition can fire it) and users with tremor or unintended keypresses — a text box appears unexpectedly mid-workflow |
| **WCAG criteria failed** | 2.1.4 Character Key Shortcuts (Level A) |
| **Severity** | Minor — one shortcut, reversible action; but it contradicts the vendor's claimed *Supports* |
| **Evidence** | R031 O5, O7 (reviewer, B2; Settings checked) |

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

### View S4 — Your stuff

| | |
|---|---|
| **Baselines run** | B4 NVDA (R029); axe (R017); low-vision reflow (R020); grayscale (R023); NH/NS N/A (R027/R028) |
| **Date tested** | 2026-08-13 |
| **Findings** | V-F12, V-F13 |

#### Finding V-F12

| | |
|---|---|
| **Where** | S4 Your stuff — the two per-card controls on every file card: the bulk-select **checkbox** and the card **action button** |
| **Observed** | Two defects on the same controls, found by different modalities. **(1) Naming:** neither control carries a unique accessible name — reviewer-confirmed by ear (R029 O2, NVDA): a user cannot tell **which file** the control belongs to. Predicted by axe (critical `label` violation, hidden `<label>` — R017 O4), confirmed on focus. **(2) Operability (added 2026-08-13, B2 — R033 O1): the checkbox does not respond to the Space bar** — the standard keyboard activation — so **bulk file selection is unavailable to keyboard-only users entirely**. The "…" menu operates but offers per-file actions, with no established bulk equivalent. Scope stays precise: the card **links are named and operable** — the defects are the two per-card controls. |
| **Affected users** | Screen reader users (naming); keyboard-only users (operability) |
| **WCAG criteria failed** | 4.1.2; **2.1.1 (Level A — added 2026-08-13)** |
| **Severity** | Major |
| **Remediation** | Include the file name in each control's accessible name ("Select *sdcsdc*", "Actions for *sdcsdc*") — the name is already on the card. |
| **Evidence** | R029 O2 (reviewer); R017 O4 + `R017-axe.json` (instrument) |

#### Finding V-F13

| | |
|---|---|
| **Where** | S4 Your stuff — filter (and scoped search) over the file list |
| **Observed** | Changing the filter updates the list with **no announcement of any kind** (R029 O4, reviewer, NVDA): no result count, no "list updated", nothing. A screen-reader user cannot tell their filter did anything. This is the **fourth verified instance** of the same product-wide defect: S2's lazily-loaded grid, S2's search results, S3's image insertion / AI generation (T1-F2, T2-F2), now S4's filter. Four instances across three views establishes the absence of status messages as a **product pattern**, not per-component slips. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.3 Status Messages |
| **Severity** | Major |
| **Evidence** | R029 O4 (reviewer) |

---

### Product output — artifact classes outside the sampled views (scope decision pending)

Found 2026-08-14 during the T2 export walk (R037). These are **not among
the four sampled views** — they are the artifacts the product *produces*
when a user exports or shares a design. Two classes are now evidenced: a
**hosted published page** (V-F16) and an **exported PDF** (V-F17). They are
recorded here because the evidence is firm and the findings are
consequential; **whether they sit inside this review's WCAG conformance
target is the reviewer's scope call**, and it is the same standing §504
question, now with much sharper evidence attached.

If the reviewer scopes them in, published pages need their own sample ID
and runs — a published page is a full page in the WCAG-EM sense, not a
state of S3 — and exported files need a document-conformance check
(PDF/UA) rather than a page sweep.

**The pattern across the three output-side findings is the argument.**
Images cannot be given alt text at all (R016 O10); the tagged PDF export
therefore carries none, and omits the document title as well (V-F17); and
published webpages convey nothing whatsoever (V-F16). Captions are the lone
counter-example — they exist and survive video export (R037 O5). So the
product's output story is not "one gap" but a consistent one: **the
accessibility affordances a user would need in order to publish
responsibly are largely absent, and where one exists it is incomplete.**

#### Finding V-F19

| | |
|---|---|
| **Where** | S3 Editor — the **zoom control** in the top bar: `<sp-action-button role="button" aria-label="View options" aria-haspopup="true">`, whose only visible text is the current zoom percentage |
| **Observed** | **Visible label and accessible name share no words.** The control displays "100%" (or "67%", etc. — it tracks the zoom level); its accessible name computes to **"View options"**. A speech-input user saying *"click one hundred percent"* would not activate it. Found by comparing visible text against computed accessible name across **64 controls on four views** — this is the **only** mismatch (R042 O7). |
| **Affected users** | Speech-input users (Dragon, Voice Control) primarily; also anyone matching what they hear to what they see |
| **WCAG criteria failed** | **2.5.3 Label in Name** |
| **Severity** | **Minor** — one control of 64; the value is dynamic so no user could rely on it as a stable name regardless; and zoom is reachable by other means |
| **Interpretive question — flagged, not decided** | 2.5.3 governs *labels*. The percentage is arguably a **value** (what the zoom currently is) rather than a **label** (what the control does), and on that reading the criterion is not engaged and S3 passes. Against that reading: it is the control's *only* visible text, so it is what a speech user sees and would say. **Recorded as a failure with the ambiguity stated** — the same treatment V-F14's 2.5.1 question received before the reviewer ruled. A reviewer decision either way is cheap here, because the severity is Minor on both readings. |
| **Context that makes the product look better, not worse** | All **25** controls whose `aria-label` overrides visible text — the only mechanism that can break this criterion — reproduce that text exactly ("Photos" → "photos", "Files" → "files", "Premium member" → "premium member"). The product handles Label in Name correctly and deliberately almost everywhere; this is a single slip, not a pattern. |
| **Remediation** | Include the visible text in the accessible name: `aria-label="100% — View options"`, updated as the zoom value changes. |
| **Evidence** | R042 O7 (assistant, four-view accessible-name comparison; control inspected individually to confirm role and `aria-haspopup`) |

#### Finding V-F18

| | |
|---|---|
| **Where** | **S1 Home and S3 the editor** — buttons and icon controls throughout both views. Measured by the reviewer with *Color Contrast Checker*, 2026-08-14 (R002 O-LV16). |
| **Observed** | **The text passes; the controls holding it do not.** Reviewer's words: *"home page all the text passes color contrast, but some of the button/icons holding the text don't when measured against the background. Same in the content edit view — text itself has enough contrast, but button doesn't."* So label text clears 4.5:1 while the **control's own boundary against the surrounding page falls below 3:1**. |
| **Affected users** | Low-vision users, and users in poor viewing conditions (glare, low-quality displays, older eyes) |
| **WCAG criteria failed** | **1.4.11 Non-text Contrast** |
| **Severity** | **Major** — it applies to buttons across two views including the product's core work surface, and it degrades the most basic affordance an interface offers: knowing that something is clickable |
| **Why this is a distinct defect and not a duplicate of V-F2** | 1.4.3 governs **text** against its background; 1.4.11 governs **the control's boundary** against what surrounds it. A button can carry perfectly legible 7:1 label text and still fail, because the user must first perceive **that a button is there at all**. That is why the reviewer's result — text passing, containers failing — is a clean 1.4.11 failure and touches 1.4.3 not at all. It is also easy to miss: a contrast tool pointed at the words returns a pass. |
| **Precision — what is deliberately not claimed** | **No ratio and no count.** The reviewer reported *"some"* controls failing without enumerating which or by how much, and inventing a number would be worse than having none. The finding is sized on the **pattern** — confirmed independently on two views, with different components on each. Enumeration is remediation work for the vendor, who has the design tokens. |
| **Assistant measurement was attempted and failed** | An automated rendered-pixel sweep was built and produced three successive wrong answers before being abandoned (R042 O6) — a ~56px coordinate offset between `getBoundingClientRect` and `Page.captureScreenshot`. **The reviewer's eyedropper answered in one pass what the instrument could not**, which is the hierarchy `ontology/testing-tools.md` prescribes. Worth stating in the report: this defect is invisible to every automated checker used in this review — axe found nothing of the kind, and WAVE reported zero contrast errors across five pages (R040). |
| **Remediation** | Raise button and icon-control boundaries (border, fill, or both) to **≥ 3:1 against their adjacent background** on both views. The likeliest offenders from the rendered capture: the app-bar icon buttons on the dark gradient, the search field's edge on near-white, and card boundaries measuring ~1.06:1 (`rgb(248,248,248)` on `rgb(255,255,255)`). Vendor should enumerate against their own design tokens — this is a token-level fix, not a per-component one. |
| **Evidence** | R002 O-LV16 (reviewer, Color Contrast Checker); rendered reference capture `evidence/runs/R002/R002-lv5-uicontrast-reference-1280.png` |

#### Finding V-F16

| | |
|---|---|
| **Where** | **Published output** — a design shared via the product's publish link (`/publishedV2/…`). A hosted webpage produced by Express, distinct from the editor and from an exported file. |
| **Observed** | **The published page is imperceptible to a screen reader.** The document's entire content announces as **"canvas graphic"** and nothing else — no text, no structure, no alternatives (R037 O6, reviewer, NVDA 2026.1.1). Whatever the author put in the design, a screen-reader reader of the published page receives none of it. The reviewer's own conclusion, recorded verbatim because it is a use-of-product judgement rather than a technical one: *"this tool should not be used to share content, especially in a course."* |
| **Affected users** | Screen reader users — **and note who they are**: not users of Express, but **readers of content published with it**, who never chose the tool and cannot work around it. |
| **WCAG criteria failed** | 1.1.1 (the entire page is non-text content with no text alternative); 1.3.1 (no programmatically determinable structure whatsoever) |
| **Severity** | **Major as recorded — and a reviewer sizing call, because Blocker is available.** No sampled task fails, since publishing is not a step in P1 or P2, which is the only reason this is not sized Blocker outright. If the reviewer scopes published output in and adds a share/publish process as a task, that task is **Fail** for no-vision users on this evidence. |
| **Relationship to the editor's canvas defect** | Same root class as R015 O9 / exhibit item 10 — content lives in a canvas with no accessibility representation — but with a **categorically wider blast radius**. In the editor it burdens one author; in published output it excludes every reader of every artifact the institution publishes. |
| **Why the export walk found it and nothing else could** | Automated sweeps are blind to canvas (R014 returned 43 passes and said nothing about it), and a per-view sweep of the four sampled views never reaches the publish path at all. It took walking the task to its actual end — the shared artifact — to surface it. |
| **Outstanding before this finding is closed** | (1) **Locator** — the exact `/publishedV2/…` URL, per the replicable-locator rule; reviewer to supply. (2) **Scope decision** — inside the WCAG target, or carried as §504/advisory. |
| **Evidence** | R037 O6 (reviewer, NVDA 2026.1.1, Chrome 151) |

#### Finding V-F17

| | |
|---|---|
| **Where** | **Exported PDF** — the PDF export path, with its **"include tags"** option enabled |
| **Observed** | The exporter offers an option to include tags, and **the tagged output still fails accessibility checks**: on inspection of the exported file, **no alt text and no document title** (R037 O7, reviewer, 2026-08-14). The reviewer's conclusion, adopted: *"PDF accessibility review would still be required even if the tags option were set."* |
| **Affected users** | Screen reader users **reading a PDF the institution publishes** — again not users of Express, but recipients downstream of it |
| **WCAG criteria failed** | **1.1.1** (untagged images carry no text alternative) and **2.4.2** (a PDF with no Title fails when published) — **of the exported artifact, not of the Express interface.** These count against this review's conformance target only if the reviewer scopes product output in; the scope call is the same one V-F16 raises |
| **Primary requirement** | **508 §504.2/§504.3** — authoring tools must be capable of producing conformant output. This is the requirement that applies to Adobe regardless of the scope call; the WCAG criteria above apply to whoever publishes the file |
| **Severity** | Major — but see the framing note; its significance is larger than its severity |
| **Why a partial capability is more dangerous than none** | A tags checkbox is the **visible sign** of accessibility support and the natural thing for a vendor to cite when asked whether their tool produces accessible output. Because it exists and is insufficient, the institution would publish PDFs it believes are conformant. An absent feature prompts a check; a present-but-incomplete one suppresses it. |
| **Two defects, two different causes — and only one is the exporter's fault** | **No alt text is downstream of R016 O10:** there is no way to author alt text anywhere in the editor, so the tagger has nothing to carry. Fixing the exporter cannot fix this — the authoring capability must exist first. **No document title is a pure exporter defect and cheap:** the product already knows the document's name (the editor is the one place in the product that retitles — V-F8's sole exception) and simply does not write it into the PDF's Title metadata. |
| **Recorded as hypothesis, not finding** | The reviewer's *"I'm sure more complex PDFs would have more issues"* is plausible and **untested** — the exported artifact was simple. Reading order, heading structure, table semantics and language metadata on a multi-element design are all unexamined. It must not reach the report as a result. |
| **Recommended follow-up if scoped in** | Export one deliberately complex design (headings, an image, a table, multiple text blocks) with tags enabled and run a PDF/UA conformance check. That single artifact would settle the reviewer's hypothesis either way. |
| **Evidence** | R037 O7 (reviewer, inspection of the exported file) |

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
| **Where** | Every SPA view in scope. Confirmed on **seven views** (crawl 2026-08-10): Home (S1), Explore (S2), Your stuff (S4), Brands, Schedule, Learn, Add-ons. |
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
| Brands (`/brands`) | No — card grid + header, same components as S1/S4 | No | None needed. Swept in the R040 WAVE sample and the 2026-08-10 crawl (03 §2.6); V-F8's title defect confirmed here, which is why the finding reads "every SPA view" rather than "the four sampled views" |
| Learn (`/learn`) | **Yes — tutorial video, the only Adobe-authored media in the product** | **Yes — 1.2.3/1.2.5 no audio description (R039 O2)**; 1.2.2 captions pass | **Sample extended.** Learn was tested rather than dismissed: R039 evaluates its media directly. That is the extension WCAG-EM step 4.3 requires, and it produced two Does Not Support outcomes no sampled view would have surfaced |
| Schedule, Add-ons | No — same shell and card patterns | No | None needed (crawl 2026-08-10) |

**Conclusion.** One random sample surfaced a content type absent from the
structured set — **Learn's tutorial video** — and the sample was extended
to cover it (R039), which is exactly the corrective step 4.3 prescribes.
No further iteration was required: the remaining random samples reuse
components already characterised on S1–S4, and the second pass produced no
new content types or findings.

---

## D. Coverage check

Before moving to `05-results.md`:

- [x] Every process in 03 §3.3 has a task cluster with a verdict — **T1 Pass with barriers, T2 Pass with barriers** (both reviewer-decided). P3 sign-in is out of scope: authentication is the institution's SSO, a different product (R041 O5)
- [x] Every branch sequence was walked, not just default sequences — P1-a (blank canvas) walked as T2 step 0 (R016 O1–O4); P2-a (upload own media) covered by the upload path under B2 (R004 O5) and the asset-panel insertion walk (R016 O7)
- [x] Every non-process sample has a view-sweep entry — S1, S2, S3, S4 each carry §B entries; **all 28 view×modality cells run** with Results set
- [x] Every finding names at least one WCAG criterion, a severity, and evidence — enforced by `review.py validate`, which passes clean. Note V-F17's criteria are of the *exported artifact*, with §504.2/.3 as the primary requirement, and V-F1/V-F6 are withdrawn with reasons recorded
- [x] Random-vs-structured comparison completed (and sample extended if needed) — §C above; **the sample was extended**: Learn's tutorial video was a content type absent from the structured set, and R039 tested it, producing the 1.2.3/1.2.5 outcomes
- [x] `05-results.md` updated: every failed criterion cites finding IDs from this file — **all 55 criteria carry an outcome**; 0 Not Evaluated
