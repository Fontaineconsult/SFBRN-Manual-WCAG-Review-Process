# Test Run R016 — S3

| | |
|---|---|
| **Run ID** | R016 |
| **Date/time** | 2026-08-06 16:49 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:b1ab530f-f097-4a5f-8a6f-b8923fa65115 — the T2 document, resolved 2026-08-10 from the Your stuff listing. NOTE: it lists as "Untitled - August 10, 2026 at 13.09.20", not "Test-With-Keyboard" — see O11 |
| **Task / process** | T2 |
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
Task T2 (process P2, adapted): author a design from scratch — create blank,
add text, add an image, export. Reviewer-driven, NVDA 2026.1.1 / Chrome
150.0.7871.187, baseline B4.

**Artifact created by this run: "Test-With-Keyboard"** (recorded in 03 §2.6).

- O1 [classified] (W12 — create a blank document; reviewer): **the create
  flow is completable by keyboard/NVDA**, but the size/format options in the
  chooser **have no names**: every one announces as
  **"Clickable Figure Template Button"**.
  - **Scope corrected by the reviewer in the same session — the defect is
    the majority case, not the exception.** First stated as "the only view
    this happens is Standard and Suggested", then corrected to: *"the only
    view where we DO hear the template name is Standard and Suggested."*
    So **1 of the 7 category tabs announces names; the other 6 do not** —
    Social media and ads, Video, Photo, Document, Webpage, Print all
    announce their options as "Clickable Figure Template Button".
    (Assistant recorded the first version briefly and corrected it here;
    the tab list is from R014's enumeration of the chooser's 7 `sp-tab`
    controls.)
  - Consequence: **Standard & Suggested is the default landing tab**, so a
    user's first impression is of a working chooser. Every category they
    navigate to afterwards is unusable by name. That pattern — the default
    view works, the rest do not — is also why an automated sweep or a
    shallow manual pass would miss this entirely.
  - A screen-reader user can therefore create *a* document, and can choose
    meaningfully only from the one tab that happens to be open by default;
    in the other six they cannot tell one option from another.
    Structurally identical to T1-F2 on S2 ("can create a design from *a*
    template, but cannot choose *which*"), now recurring in the create flow
    and across six of seven categories.
  - Note this is a **different defect from V-F5**, which concerns the ten
    identically-named "Browse templates" buttons in the same modal. V-F5 is
    "many controls sharing one unhelpful name"; this is "controls with no
    name at all". Same modal, two distinct problems.
  - **Assistant corroboration attempted and failed — outstanding.** A CDP
    run navigated to Home successfully but could not reopen the chooser
    (the programmatic click reported success while the page stayed on
    Home — the same class of divergence recorded in R015 O7, where
    programmatic activation bypasses the app's own handling). No
    tab-by-tab name comparison was obtained. **The reviewer's account
    stands as the evidence**, which is the normal case in this process;
    the corroboration would only have added per-tab counts. Retry by
    driving the chooser with dispatched key events, or have the reviewer
    read two or three option names per tab.
  - Classified: NV3/NV4 / WCAG 1.1.1, 4.1.2 / Major → **task finding
    T2-F1**
- O2 [classified] (W12 — activation feedback; reviewer): *"when pressing
  enter on an on-focus template option, we are not told what it is, and are
  redirected into the new design window."* Activating a choice gives **no
  confirmation of what was chosen** before the view changes.
  - Compounds O1: not only can the user not tell the options apart before
    choosing, they get no confirmation of what they chose afterwards. There
    is no point in the flow at which the canvas size is stated.
  - Classified: NV3/NV7 / WCAG 4.1.2 / Major → feeds **T2-F1**
- O3 [classified] (W12 — arrival in the editor; reviewer): on creation NVDA
  announces **"Loading Document, Untitled, Untitled"** — *"although we are
  not told where focus is."*
  - **A partial positive, and the first announced view transition found in
    this review.** Contrast S1→S2 (T1-F1), where navigation announced only
    "current page, current page", and the search-result activation on S2
    (R013 O13), which announced nothing at all. Here *something* is spoken,
    and it names the document state.
  - Defects that remain: the announcement is **repetitive** ("Untitled,
    Untitled") and **focus placement is not stated**, so the user knows a
    document loaded but not where they are in it or what to do next.
  - Classified: NV7 / WCAG 4.1.3 / **partial pass** — recorded as a
    positive with caveats, not raised as a finding.
- O4 [classified] (W12 — renaming; reviewer): **"can be renamed directly
  using NVDA through button access"** — the document was renamed to
  **"Test-With-Keyboard"**.
  - **Clean positive.** Document naming is fully operable by keyboard and
    screen reader. Worth recording explicitly: the review must report what
    works as well as what fails, and this is a real capability in a flow
    that otherwise fares badly.
  - Classified: NV3/MO2 / pass — no finding
- O5 [classified] (W13 — add a text element and set its content; reviewer):
  **this step passes cleanly on every count.**
  - The **Text** control is *discoverable*: it appears in NVDA's forms and
    buttons lists **and** is reachable by Tab alone.
  - The Text panel is **structured with headings for each button type**.
  - Activating **"Add Your Text"** inserts a starter "Add Text" element on
    the canvas, and NVDA announces **"edit selected add text"** — real,
    specific feedback naming both the action and the object.
  - **Edit mode is entered automatically** on creating new text — no
    Tab→Enter→Enter route required.
  - **The text content can be confirmed by ear.**
  - Classified: NV3/NV7 / pass — no finding.
- O6 [classified] — **the decisive structural insight of this run: the
  editor's accessibility splits by *authoring* versus *revisiting*, not by
  feature.** Setting O5 beside the R015 results on the same view:

  | | Creating new content (this run) | Returning to existing content (R015) |
  |---|---|---|
  | Entry point | "Text" control, in NVDA's lists **and** Tab-reachable | layers list, in **no** NVDA list; Tab stop 32 |
  | Route | one button press | Tab → Enter → Enter, undocumented |
  | Announcement | **"edit selected add text"** | **"Canvas"**, identically for every object |
  | Edit mode | entered **automatically** | two manual Enters |
  | Content readable | **yes** | yes, but only once in edit mode |
  | Editing field | reached directly | `<textarea>` with **no accessible name** |

  - So the same view, same objects and same underlying editor behave very
    differently depending on how the user arrives. **A screen-reader user
    can author a design; they cannot readily revise one** — including their
    own work in a later session, or anything a colleague sends them.
  - **Why this matters for the procurement framing:** "the editor is
    inaccessible" is wrong and would be rebutted. The defensible claim is
    narrower and stronger — *authoring works; returning to existing content
    does not*. That also points at a specific remediation (name the layer
    rows and the editing field, announce object selection) rather than an
    open-ended one, and it explains why an evaluator who only creates test
    content would find nothing wrong.
  - Classified: NV3/NV5 — no new finding; **re-frames the existing R015
    findings and should shape T2's verdict and the report's wording.**
- O7 [classified] (W14 — insert an image; reviewer): both **"Add a photo"**
  and **"Generate with AI"** are findable by keyboard — but **"no feedback
  was provided as to if the image was successfully placed or generated."**
  - **The inconsistency is the finding.** One step earlier, in the same
    panel and the same flow, adding *text* announced **"edit selected add
    text"** (O5). Adding an *image* announces nothing at all. The product
    demonstrably knows how to report insertion; it does so for one content
    type and not the other.
  - **"Generate with AI" is the worse half.** Insertion is instantaneous, so
    silence is merely disorienting. Generation is an **asynchronous
    operation taking many seconds**, with no progress indication, no
    completion announcement, and no error path exercised. A screen-reader
    user has no way to distinguish "still working", "finished", and
    "failed", and 4.1.3 exists precisely for this case. This is also the
    product's most heavily promoted capability (03 §2.2 F8).
  - Classified: NV7 / WCAG 4.1.3 / Major → **task finding T2-F2**
- O8 [classified] (W14 — identifying what is selected; reviewer): *"only
  feedback is **'Canvas Graphic'** — not Image or text or video… it is not
  possible to tell which element is being edited."*
  - **Extends R015 O9 with a second object type and sharpens it.** With a
    text object the announcement was "Canvas"; with an image it is "Canvas
    Graphic". So a *generic role* is now exposed, but still **no identity**:
    not which object, not its content, not its alt text, not its position.
    Two objects of different types remain indistinguishable from one
    another, and from themselves on a later visit.
  - This is the concrete mechanism behind O6's authoring/revising split: a
    design containing several elements cannot be navigated by ear, because
    every element reports the same thing.
  - Classified: NV3/NV8 / WCAG 4.1.2, 1.3.1 / Major → strengthens
    **R015 O9**; scope widened from "text objects" to "all canvas objects".
- O9 [classified] (W14 — reaching the layers region; reviewer): *"I cannot
  find my way via navigation with the screen off to the layers region where
  we select each image/text layer; it is possible to tab into it, but that
  is very clunky."*
  - **Independent second confirmation of R015 O2/O3**, now under real task
    conditions and with the screen off rather than while investigating. The
    layers region is absent from NVDA's navigation views and reachable only
    by traversing the tab order (stop 32 when a panel is open).
  - Significant because the layers list is the **only** route to existing
    objects. Its undiscoverability is therefore not a convenience issue —
    it is what makes revisiting content impractical (O6).
  - Classified: NV2/NV5 / WCAG 1.3.1, 2.4.3 / Major → reinforces the
    consolidated S3 finding; no separate finding raised.
- O10 [classified] (W15 — alt text on an inserted image; reviewer):
  **"I see no way at all, even visually, to add alt text."** Checked
  sighted as well as by screen reader, so this is not a discoverability
  problem — the capability appears absent.
  - **This is not a WCAG finding, and must not be recorded as one.** WCAG
    2.2 governs the accessibility of *this product's own interface*. No
    success criterion requires an authoring tool to let its users attach
    alternative text to the content they produce. Filing it as 1.1.1 would
    be wrong and would be rebutted — 1.1.1 concerns Express's own images,
    which are covered separately by V-F7.
  - **The applicable requirement is Section 508 §504 Authoring Tools**,
    which this review's declared conformance target (WCAG 2.2 AA, 03 §1.2)
    does not currently include:
    - **§504.2 Content Creation or Editing** — an authoring tool shall
      provide a mode of operation to create or edit content conforming to
      WCAG Level A and AA, *"as applicable, to file formats supported by
      the authoring tool."*
    - **§504.3 Prompts** — shall provide a mode that *prompts* authors to
      create conforming content.
    (ATAG 2.0 Part B, notably B.2.3 "assist authors with managing
    alternative content for non-text content", is the equivalent standard.)
  - **Severity turns on output format, and that keeps the claim honest:**
    - **PNG / JPG export — little or no impact.** Raster formats carry no
      alt text; responsibility passes to wherever the image is published.
      Not Express's failure.
    - **PDF export — material.** A conforming PDF requires tagged content
      with alternative text. With no way to supply it, exported PDFs
      cannot conform.
    - **Webpage output — material.** Express publishes webpages; generated
      HTML images need `alt`. With no way to supply it, published pages
      cannot conform.
  - **Why it matters more than any other finding in this review, if it
    holds:** every other finding is a barrier to *one person operating the
    tool*. This one is a defect in the tool's *output* — it would mean every
    PDF and every webpage the institution publishes from Express carries
    unlabelled images, affecting readers who never touch Express and
    compounding with each artifact produced.
  - **Two reviewer decisions needed before this can be written up:**
    1. **Scope** — extend this review to 508 §504, or carry it as an
       advisory procurement note outside the WCAG conformance statement?
       §504 is plausibly in scope for a CSU ICT procurement even though the
       declared WCAG target does not reach it.
    2. **Confirm the output formats** — does Express's Download/Share offer
       PDF and/or Webpage publishing? Step 3 of this walk (W16) will show
       the export dialog and can settle it.
  - Classified: **not a WCAG criterion** — 508 §504.2 / §504.3 candidate,
    recorded in 06 as a procurement concern pending the scope decision.
- O11 [new] (state: Your stuff listing, read 2026-08-10 while resolving this
  run's durable URL): **the T2 document lists as "Untitled - August 10,
  2026 at 13.09.20", not "Test-With-Keyboard".** O4 records the reviewer
  renaming it by keyboard and the rename being announced as successful.
  - **Deliberately not interpreted** (per the lesson in testing-loop.md: an
    unexplained state change is not evidence of a defect — three assistant
    hypotheses died that way in R015). At least four readings fit:
    the rename did not persist; the listing caches stale names; the
    in-editor title and the file name are different fields; or the rename
    landed on a different document.
  - Why it matters if the first reading holds: a keyboard/AT user performed
    an operation, was told it succeeded, and the durable record does not
    show it — a feedback-integrity failure worse than silence (candidate
    4.1.3 / 3.3.x territory). But that is *if*.
  - **Reviewer question to settle it:** open the document and check its
    in-editor title, and/or rename it again watching the listing. Until
    then the durable URN (recorded in the header and 03 §2.6 registry) is
    the only trustworthy locator — which is precisely why display names
    must never serve as locators.
  - Classified: NV7 candidate — **CLOSED 2026-08-13 as unreproducible**
    (R029 O3): the reviewer renamed the document again, in both the listing
    and the canvas-edit surface; names now persist and display correctly in
    both. No feedback-integrity finding raised. Residual value: display
    names demonstrably drift, which is why the URN registry (03 §2.6) is
    the locator authority.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R016-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
