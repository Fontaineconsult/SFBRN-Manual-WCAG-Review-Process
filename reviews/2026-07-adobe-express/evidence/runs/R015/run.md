# Test Run R015 — S3

| | |
|---|---|
| **Run ID** | R015 |
| **Date/time** | 2026-08-06 15:46 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B4 |
| **Tester** | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | | |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | | |
| NV3 — Every control announces an accurate name, role, and value/state | | |
| NV4 — Images announce appropriate alternatives; decorative images are silent | | |
| NV5 — Reading order matches the meaning of the visual order | | |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | | |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | | |
| NV8 — Nothing is conveyed only by visual position, shape, or size | | |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [classified] (state: editor default, W1/NV2 — reviewer): **"the Canvas
  heading doesn't appear in NVDA, but I can detect it fine with headingsMap,
  and headingsMap says `Canvas [aria-label="Canvas"]`."**
  - **Reviewer is right; the DOM tool is the misleading one.** Verified in
    Chrome's accessibility tree (CDP `getFullAXTree`, 3,022 nodes): the tree
    exposes **15 headings and "Canvas" is not among them** — nor is "Daniel
    Fontaine", which also exists as an `h2` in markup. There *is* an AX node
    named "Canvas", but its **role is `Canvas`, not `heading`**.
  - So `<h2 aria-label="Canvas">Canvas</h2>` exists in the markup — which is
    all headingsMap reads — and never reaches assistive technology as a
    heading. **Instrument lesson worth carrying:** headingsMap and similar
    extensions parse *markup*; NVDA consumes the *accessibility tree*. On
    this product they disagree, and the tree is what matters. Do not use a
    markup-based outline tool to contradict what a screen reader reports.
  - Consequence: the one heading that would let a screen-reader user jump
    to the work surface is precisely the one not exposed. Two of the
    editor's markup headings are missing from the AT outline.
  - Classified: NV2 / WCAG 1.3.1 / Major → **candidate finding**, pending
    W5/W6 completion (heading + landmark walk) so it is raised once with
    full scope rather than piecemeal.
- O2 [classified] (state: editor default, W2 — **the key question**;
  reviewer): **"my main goal right now is figuring out how to navigate into
  the canvas to edit the Text Test and I can't find a way to do that."**
  - Corroborated structurally, and the picture is bad:
    - The `<canvas>` has **no `tabindex`, no `role`, no `aria-label`** and
      its parent `hz-canvas-input` has none either — so **the canvas cannot
      receive keyboard focus at all**. There is no "enter the canvas" to
      find.
    - **Nothing anywhere in the 3,022-node accessibility tree is named
      "Text Test."** The document's only object has no representation.
    - The one candidate route is a **layers list** — `hz-sortable-list`,
      `role="grid"`, 110×77px at the top right — whose `aria-label` is
      *"Reorder layers. Space to select. Forward: Command or Ctrl + right
      bracket, Backward: Command or Ctrl + left bracket."* But the container
      has **no `tabindex`**, and its three AX child rows are **all
      unnamed**.
  - So the mechanism that exists addresses **reordering**, not reading or
    editing; it is undiscoverable (the reviewer, an experienced NVDA user,
    did not find it); and even when reached its rows carry no names, so a
    user would hear unnamed rows rather than "Text Test".
  - **Not yet raised as a finding** — one thing must be ruled out first:
    whether Adobe Express documents a keyboard route (shortcuts panel) that
    exists but is undiscoverable. "Impossible" and "possible but with no
    discoverable affordance" are different severities, though both are
    serious. See the reviewer step below.
  - Classified: NV3/NV4 / WCAG 1.1.1, 1.3.1, 2.1.1, 4.1.2 / **Blocker
    candidate** — this is the finding the whole S3 run turns on.
- O3 [classified] (state: reviewer found a route, W2 continued): **"no way
  to get that via NVDA view, had to tab into it; pressing Enter activates
  the layer edit, a button region opens for editing the text, most of the
  buttons are unlabeled, activating the Edit button opens the Text edit
  window — but I still can't figure out how to edit the actual text."**
  - Assistant reproduced the path with **real dispatched key events** (an
    earlier attempt using programmatic `.click()` diverged onto the
    page-level "Edit page" panel and was discarded — programmatic clicks
    bypass the app's own key handling and must not be used to reproduce a
    keyboard path). Findings from the tab walk:
    - The layers item **is** in the tab order, at **tab stop 32** — after
      the entire top bar, the nine left-rail items, and any open panel.
      Reachable, but only by traversing the whole application first, and
      it is exposed nowhere in NVDA's element lists (hence "no way to get
      that via NVDA view").
    - **Tab stop 30 is an unnamed `div`** — a bare stop with no name.
    - Pressing **Enter on the layer moves focus to an unnamed `div`
      positioned at [0,0]** — an anonymous container, not the panel that
      opens. Focus management on activation is broken.
  - Classified: NV3/NV5/MO5 / WCAG 2.4.3, 4.1.2 / Major → feeds the
    consolidated S3 finding.
- O4 [classified] — **the decisive result: the "Text edit window" is a
  styling panel, not a content editor.** Enumerated every editable surface
  in the DOM and every editable node in the accessibility tree in that
  state:
  - **Exposed and correctly named:** combobox "Font family" (Source Sans
    3), combobox "Font style" (Regular), textbox "Font size" (82), textbox
    "Text styles" (Title), plus letter-spacing and alignment controls. The
    *formatting* of text is fully accessible.
  - **Not exposed at all:** any field holding the text **content**. The AX
    tree's complete list of editable nodes is those four styling controls —
    there is no `textbox`, no `contenteditable`, no `textarea` carrying the
    document's words. The literal string of the text object appears
    **nowhere in the DOM** — not as a text node, not as an `aria-label`,
    not as an input value.
  - **PARTLY CORRECTED by O8 — read this with that.** The conclusion drawn
    here ("cannot read or change what it says") was measured *before* text
    edit mode exists and is wrong as a general statement. What survives: in
    the **selected-but-not-editing** state, the styling panel is the only
    thing exposed, and the text content is not readable. What was wrong:
    entering edit mode creates a real editable field (O8).
  - Classified: NV3 / WCAG 1.1.1, 1.3.1 / Major (scoped to the at-rest and
    selected states) — superseded in part by O8
- O5 [**corrected — original reading withdrawn**] — the document text
  changed from "Text Test" to "**Textd** Test" during the session (observed
  in the assistant's independently-synced view of the same cloud document).
  - The assistant hypothesised *invisible editing* — that stray keystrokes
    were modifying the document with no feedback — and asked before writing
    it up. **Reviewer: "that was added with mouse."** The edit was
    deliberate and pointer-driven. **Hypothesis withdrawn; no such finding.**
  - Worth keeping as a discipline note: an unexplained state change is not
    evidence of a defect. Two consecutive assistant hypotheses on this run
    (this one, and the earlier programmatic-click reproduction) were wrong
    and were caught by asking rather than recording.
  - Classified: dismissed — reviewer-explained, no defect.
- O7 [classified] — **2.1.1 Keyboard is NOT failed. A keyboard route exists,
  and the assistant's Blocker framing is withdrawn.** Reviewer, having
  worked it out: *"you need to select the layer, press enter, focus moves to
  the layer object, if you hit enter it will enter the text edit mode."*
  - The route: **Tab to the layer (stop 32) → Enter → focus moves to the
    layer object → Enter again → text edit mode.** A double-Enter, with the
    first Enter moving focus onto the object rather than editing it.
  - **Withdrawn:** the assistant had concluded from the absence of any
    editable field in the DOM/AX tree (O4) that editing was pointer-only —
    a **2.1.1 Level A failure, Blocker**. That conclusion was wrong. The
    editable surface is created on demand when edit mode is entered, so it
    is absent from a tree snapshot taken beforehand. **Lesson: the absence
    of a control in a static snapshot does not prove the absence of a
    mechanism** — for modal/stateful UIs, probe each state, or ask.
  - **This is the third assistant hypothesis corrected by the reviewer on
    this run** (programmatic-click reproduction; invisible editing; now
    pointer-only editing). All three were caught before entering the
    record. The pattern is consistent and worth naming: structural probes
    are good at *what exists right now* and bad at *what is reachable*. On
    a stateful application, reachability is the reviewer's question, not
    the tool's.
  - **What survives, and it is still substantial** — the route is
    **undiscoverable**: it is announced nowhere, documented in no label,
    signalled by no affordance, and an experienced screen-reader user
    working deliberately took a long stretch of a testing session to find
    it. Discoverability is not itself a WCAG success criterion, so this is
    **not** automatically a failure — the live questions are whether entry
    into edit mode is *announced* and whether the text is *readable* once
    there (see the open item below). Severity and criteria stay open until
    those are answered.
  - Classified: NV3/NV7 — pending, **no finding raised yet**
- O6 [classified] (state: Text panel open, reviewer: *"it's just the Bold,
  Italics and Underline that don't announce anything"* — narrowing the
  earlier "most of the buttons are unlabeled"): enumerated both control
  clusters. **There are two separate Bold/Italic/Underline sets, and they
  differ:**

  | Control | Text panel (left, y≈402) | Floating toolbar (near canvas, y≈85) |
  |---|---|---|
  | Bold | `aria-label="Bold"`, `aria-pressed="true"` | **no `aria-label`** |
  | Italic | `aria-label="Italic"`, **no `aria-pressed`** | **no `aria-label`** |
  | Underline | `aria-label="Underline"`, `aria-pressed="false"` | **no `aria-label`** |

  - Two distinct defects fall out:
    1. **Italic never exposes its state.** Bold and Underline carry
       `aria-pressed`; Italic carries none, so a screen-reader user cannot
       tell whether italic is on or off — 4.1.2 requires *state* as well as
       name and role for a toggle.
    2. **The floating toolbar set carries no `aria-label` at all**, and the
       accessibility tree holds **9 unnamed button nodes** in this state.
       This is the likeliest source of the reviewer's "don't announce
       anything".
  - **RESOLVED — it is the floating toolbar.** Reviewer: *"when you click a
    layer to edit, a new button region opens with the text editing unlabeled
    buttons."* So the cluster that appears on entering layer edit is the
    one carrying **no `aria-label`**, matching the **9 unnamed button
    nodes** counted in the accessibility tree for that state. NVDA and the
    tree **agree**; the labels are genuinely absent. (Had it been the left
    Text panel — which *is* labelled — the finding would have been a
    tool/AT disagreement instead.)
  - So the defect is precisely: **the text-editing toolbar presented at the
    moment of editing is unlabelled**, while the equivalent controls in the
    left-hand Text panel are labelled. A screen-reader user who follows the
    editing flow lands on the unlabelled set.
  - Classified: NV3 / WCAG 4.1.2 / Major → **confirmed**, plus the separate
    Italic state defect (no `aria-pressed`). Both feed the consolidated S3
    finding once the edit-mode questions below are answered.
- O8 [classified] — **text edit mode DOES expose the content. The canvas is
  not a black box.** Assistant reproduced the reviewer's route with real key
  events (Tab to layer → Enter → Enter) and probed the tree *in that state*:

  | State | Editable surface exposed | Document text readable |
  |---|---|---|
  | At rest | none | **no** |
  | Layer selected (1× Enter) | none | **no** |
  | **Text edit mode (2× Enter)** | **`<textarea>`, focused** | **yes — carried as the field's value** |

  - In edit mode the DOM holds a real `<textarea>` containing the document
    text, it **has focus**, and the accessibility tree exposes it as
    `role=textbox` with the text as its **value**. A screen-reader user in
    this state can read and edit the text normally.
  - **The defect that remains here is narrow and specific: the textarea has
    no accessible name** — `aria-label` is null and the AX `name` is empty.
    The user hears the content but is never told what field they are in.
  - **What this settles, and what it does not:**
    - **Settles:** 2.1.1 Keyboard is **not** failed; the content is **not**
      permanently trapped in the canvas; 1.1.1 is **not** failed for text
      objects. The earlier Blocker framing is fully withdrawn.
    - **Does not settle:** reading the document *as a whole*. Content is
      exposed only **one object at a time, and only while editing it**.
      There is no exposed representation of the document to read through —
      to learn what a design says, a user must locate each object in the
      layers list and enter edit mode on each in turn. For a multi-object
      design that is a serious review/proofreading barrier, and it is the
      question a one-object test document cannot answer (03 §3.1 notes
      this limitation).
  - Classified: NV3/NV4 / WCAG 4.1.2 (unnamed field) / Major; the
    document-level reading question routed to a richer test document.
- O9 [classified] — **selecting a layer moves focus into the canvas and
  announces only the generic word "Canvas". A product defect, not an NVDA
  setting.** Reviewer, correcting an initial "nothing is announced":
  **"nothing is announced, just says *Canvas*."**
  - **"Canvas" is exactly what the tree predicts, and that is the problem.**
    The accessibility tree contains a single node `role=Canvas
    name="Canvas"` for the whole 2328×1145 drawing surface, and **no node
    of any kind for the individual objects in the document**. So selecting
    a layer moves focus into that one container, and NVDA correctly reads
    the only thing available to it: the container's name.
  - **Verbosity ruled out**, on three grounds:
    1. What is announced is *the container's real accessible name*, not a
       truncation or a suppressed detail — verbosity settings do not
       substitute a parent's name for a child's.
    2. `document.activeElement` after that Enter is an unnamed, role-less
       `<div>` at [0,0] (tab-walk probe), and the object itself has **no
       representation in the accessibility tree at all**.
    3. Verbosity governs *how much* detail NVDA reads about a node it can
       see; it cannot make a named, roled control silent. The same NVDA
       profile announced buttons, headings, comboboxes and the search field
       correctly throughout this session and R012/R013.
  - **Consequence — the announcement is identical for every object.**
    Whether the user selects the text object, an image, or a shape, they
    hear "Canvas". They are told nothing about *what* they selected: not
    its type, not its content, not its position, not its size, and not that
    the selection changed at all. Moving between layers gives no feedback
    that anything happened.
  - This is the state *between* the layers list and edit mode, and it is
    where a user decides whether they have the right object. Getting no
    feedback here is why the route feels unusable even though it works
    (O7): each step succeeds silently, so the user cannot tell progress
    from failure.
  - Classified: NV3 / WCAG 4.1.2 (name/role/value for the focused object),
    1.3.1 / **Major** → feeds the consolidated S3 finding
- O10 [classified] (state: editor, asset panel — reviewer, 2026-08-10):
  *"tables are regularly used for navigation elements, but the tables don't
  have a summary so I don't know what the table area is about — also I
  thought tables were not supposed to be used for navigation?"*
  - **Measured and confirmed: 12 grids on S3, 11 of them unnamed.** All
    eleven are `x-simple-row-scroller` (`role="grid"`, 281px wide) — the
    asset panel's content rows: Templates, Photos, Design assets, Icons,
    Shapes, Stickers, Backgrounds, Videos, Music, Sound effects, Charts.
    106 `gridcell` nodes sit inside them. The **only** named grid is the
    layers list (`hz-sortable-list`). Verified in both the DOM and the
    accessibility tree.
  - **Two distinct defects, and they should be written up separately:**
    1. **The grids have no accessible name** (no `aria-label`, no
       `aria-labelledby`). A user lands in "a grid/table" with no
       indication of what it holds — the reviewer's "I don't know what the
       table area is about". → **1.3.1**.
    2. **`role="grid"` is applied to non-tabular content.** These are
       horizontal card carousels with no meaningful row/column
       relationship, so the markup asserts a structure the content does not
       have, and burdens the user with grid navigation semantics for what
       is a list of choices. → **1.3.1** (relationships conveyed
       programmatically do not match the content).
  - **Correcting the reviewer's framing before it reaches the report** —
    this matters because the weaker version is easy for a vendor to rebut:
    these are **not** HTML `<table>` elements used for layout (the
    discouraged practice, which would need `role="presentation"`). They are
    ARIA `role="grid"`, a legitimate pattern that is being **misapplied**.
    The defensible claim is "grid semantics on non-tabular content, 11 of
    12 unnamed", not "tables used for navigation". Likewise "summary" is
    the obsolete HTML4 table attribute; the modern equivalent is
    `aria-label`/`aria-labelledby`.
  - **Remediation is cheap and that strengthens the finding:** each section
    already carries an adjacent `h3` ("Templates", "Photos", "Design
    assets"…) which *is* exposed to AT. One `aria-labelledby` per grid,
    pointing at the heading already present, would name all eleven. The
    information exists and simply is not wired up.
  - **Scope — likely product-wide, not S3-only.** `x-simple-row-scroller`
    also appears on S1 (the Recent bar, R009 node paths), and S2's template
    grid is the related `x-masonry` with an *orphaned* `role="row"`
    (R011 O1). The same component family underlies the asset rows here, the
    home rows, and the Explore grid. **Verify on S1/S2 before sizing**, then
    raise once as a product-wide finding rather than per view.
  - **SCOPE CHECK DONE 2026-08-10 — product-wide, and worse than S3 alone
    suggested.** Counted on each sampled view, verifying the landed view
    before measuring:

    | View | Grids | Named | Unnamed | Orphaned `role="row"` |
    |---|---|---|---|---|
    | S1 Home | 2 | 0 | 2 | 2 |
    | S2 Explore | 2 | 0 | 2 | 3 |
    | S3 Editor | 12 | 1 | 11 | — |
    | S4 Your stuff | 2 | 0 | 2 | 1 |
    | **Total** | **18** | **1** | **17** | on every view |

    Components involved: `x-home-row-scroller`, `x-simple-row-scroller`,
    `sp-grid`, `x-masonry`. **The single named grid in the entire product
    sample is the editor's layers list.**
  - **The orphaned-row defect is also product-wide.** `role="row"` with no
    `grid`/`table`/`rowgroup` ancestor appears on S1, S2 and S4 — the same
    defect that axe flagged as a critical `aria-required-parent` violation
    on S2's `x-masonry` and that was identified as the root cause of
    **T1-F2** (R011 O1). It is not confined to the template grid.
  - **Count caveat, stated so nobody over-reads it:** these are **floors,
    not totals**. S1/S2/S4 were measured shortly after navigation and these
    views lazy-load content on scroll, so more grids may exist than were
    counted. S3's 12 reflects a fully-rendered asset panel. The *ratio* —
    essentially none named — is the robust result.
  - Classified: NV2/NV3 / WCAG 1.3.1 / Major → **finding V-F11**
    (product-wide, 04 §B).

## Notes

Capture surface: `session-S3-reviewer-walkthrough.md` (Parts A and B are this
run). NVDA wording comes from the **Speech Viewer** (`NVDA+N` → Tools →
Speech Viewer), enabled before testing; `Insert+Space` is a JAWS chord and
toggles browse/focus mode in NVDA — avoid it.

**What automation could and could not establish before this run:**

- **Could not, and this is the point:** the axe sweep (R014) reported
  **nothing whatsoever about the canvas** — not a violation, not an
  incomplete, not even an inapplicable note — while returning 43 passes.
  The editor paints the whole document into one 2328×1145 `<canvas>` with no
  `role`, no `aria-label`, no `aria-hidden` and zero fallback children, and
  the visible "Text Test" object is **absent from the DOM** across 960 open
  shadow roots. **The principal risk on this view is structurally invisible
  to every automated checker.** R014's pass count must not be read as
  reassurance.
- **Could:** the editor has **no `main` landmark**, **no `h1`**, two
  unlabelled `<header>` banners, and **21 nodes** of content outside any
  landmark (vs 4 on S1). Confirmed independently by axe and the exploration
  DOM probe.
- **Carried in for confirmation:** V-F10, the page-navigation "more" button
  with no accessible name (R014 O1) — confirm **on focus**, not from the
  elements list (R012 O9 nearly produced a false finding that way).
- **Explicitly do not inherit from S1:** finding V-F3's amendment narrowed
  2.4.1 to keyboard-only users *because* S1 exposes a `main` landmark giving
  screen-reader users an ARIA11 bypass. S3 has no `main`, so that reasoning
  does not transfer — 2.4.1 must be assessed afresh here (W6/W7).
- **Contrast caution for later passes:** axe emitted two **false-positive**
  contrast violations on this view by assuming a background it could not
  resolve (claimed 1.08:1 and 1.14:1; rendered-pixel sampling gives 15.06:1
  and 12.18:1 — R014 O2). Measure, do not trust the tool, on S3.

## Evidence files in this folder

- (screenshots/exports named R015-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
