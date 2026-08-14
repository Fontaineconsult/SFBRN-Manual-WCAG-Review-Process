# Test Run R038 — S3

| | |
|---|---|
| **Run ID** | R038 |
| **Date/time** | 2026-08-14 12:39 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:a767278e-deed-4656-b424-f01495fad229 — **"Can-I-find-the-right-text"**, resolved 2026-08-14 (same day the artifact was created, per the CLAUDE.md rule). Five objects: three text boxes "text 1" / "text 2" / "text 3", plus a shape and a photo |
| **Task / process** | T2 |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B4 |
| **Tester** | reviewer (D. Fontaine), NVDA 2026.1.1 |
| **Result** | Works with issues |

**Result reasoning** (set 2026-08-14). Not *Broken*: a keyboard route to
every object and to its text content exists and was walked end to end
(O4), so the view remains usable by a screen-reader user. Not *Works*: no
object can be identified, layer rows announce an untranslated developer
string, the route in is undiscoverable, and reaching content requires
overriding the screen reader. **The run's Result is deliberately not the
task verdict** — a view being usable with issues is compatible with a task
being unachievable at realistic scale, and T2's verdict (W17) is the
reviewer's.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

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

Test design (reviewer): a new document with **five objects** — three text
boxes reading "text 1", "text 2", "text 3", plus **a shape and a photo**.
Task: **with screen reader only, find "text 2" and edit it.** The content
is self-labelling, which makes this a *generous* probe — the words
themselves distinguish the objects, if they can be read.

- **O1 [classified]** (route to the layers list — reviewer): **the only
  reliable route is worse and more indirect than previously recorded.**
  *"Find the Edit pages form in the form-fields elements list, then press
  the Edit page button, then tab into the re-order layers area."*
  - **Supersedes the R015 O3 description** ("Tab stop 32"). The route is
    not merely deep in the tab order — it runs **through NVDA's form-fields
    elements list to a control named "Edit page"**, which is not a name a
    user would associate with *selecting objects*. Nothing signposts it.
  - Classified: NV2/NV5 / WCAG 1.3.1, 2.4.3 / Major → **T2-F4**

- **O2 [classified]** (arrowing through layers — reviewer, exact speech):
  arrow keys **do** move between layers, and each item announces:

        not selected  @hz/shared-ui-components:sortable-list-press-space-to-grab  row 1  column 1
        …                                                                          row 1  column 5

  - **Two distinct defects in one announcement, both new and both
    concrete.**
    1. **An untranslated localisation key is being read to the user as the
       control's name.** `@hz/shared-ui-components:sortable-list-press-space-to-grab`
       is a developer message ID that should have resolved to human text
       ("press space to grab"). It reaches the screen reader raw. This is
       unambiguous, cheap to fix, and trivially reproducible — the kind of
       defect a vendor cannot dispute.
    2. **"row 1, column 1–5" — a vertical layer stack announced as a single
       row with five columns.** Direct, independent corroboration of
       **V-F11**: grid semantics applied to non-tabular content. A layer
       *stack* is one-dimensional and ordered by depth; announcing it as
       columns of one row misdescribes the structure and imposes grid
       navigation on a list.
  - **What is absent is the point: "no indication of what the layer is."**
    Five objects of three different types — text, shape, photo — are
    indistinguishable from each other in this list.
  - Classified: NV3 / WCAG 4.1.2, 1.3.1 / Major → **T2-F4**; corroborates
    V-F11

- **O3 [classified]** (Enter vs Space on a layer — reviewer): **Enter
  announces only "canvas graphic"**, as in R015 O9 and R016 O8. **Space
  yields more**: it sometimes enters edit mode directly, the **Edit pane
  opens and a summary of that pane is read**, which *"gives some indication
  what the object selected is"* — presumably because the pane's controls
  differ by object type (text vs image vs shape).
  - **A partial positive, and the first route found to object *type*.** But
    the reviewer's own qualifier is the finding: *"since objects carry no
    unique name, we don't know which is actually selected."* Type is
    inferable; **identity is not**. With three text boxes, knowing "this is
    a text object" does not distinguish text 1 from text 2 from text 3 —
    which is exactly the task.
  - **"Sometimes"** is itself recorded: the reviewer reports Space
    *sometimes* entering edit mode directly, so the behaviour is
    inconsistent rather than a reliable route.
  - Classified: NV3 / WCAG 4.1.2 / Major → **T2-F4**

- **O4 [OPEN — the severity-deciding question, not yet classified]**
  (reading the text content — reviewer): *"the only way to hear the text is
  to enter text edit mode directly on the canvas, **I can't figure out how
  to do that without a click**."*
  - **This is in apparent tension with R015 O7 and must not be recorded
    until reconciled.** R015 O7 established a keyboard route — **Tab to
    layer → Enter → Enter → text edit mode** — and on that basis a 2.1.1
    Level A Blocker was **withdrawn**. If the route no longer works, or
    does not work when reached via the layers list with several objects
    present, that withdrawal needs revisiting. If it still works and simply
    was not tried from this entry point, 2.1.1 stays withdrawn and this is
    a discoverability defect, not an operability one.
  - **The distinction decides T2's verdict**, so it is being asked rather
    than assumed: Major (burden) versus Blocker (task not completable)
    turns on it. See §Open question below.
  - **RESOLVED 2026-08-14 (reviewer): a keyboard route exists, but it
    requires defeating the screen reader.** *"To edit the text we need to
    use the passthrough key then hit enter again."* NVDA's pass-through
    (`NVDA+F2`, "pass next key through") sends the following keystroke
    straight to the application; Enter then works and text edit mode is
    entered.
  - **2.1.1 stays withdrawn — correctly, and for the second time.** The
    functionality *is* operable from the keyboard. Recording a Blocker
    here would have been the same error CLAUDE.md documents from
    2026-08-06, and it was avoided the same way: by asking instead of
    concluding. Worth naming the recurring shape — on this product, *"I
    can see no route"* has now been wrong every time it has been thought.
  - **But what the pass-through requirement means is itself the finding,
    and it is not small.** NVDA is intercepting Enter and the application
    never receives it. That happens when a control does not present itself
    to the AT as something warranting focus mode — an editable field, an
    application region, a proper grid. The product is not telling the
    screen reader what kind of thing has focus, so the user must manually
    override their AT to interact with it.
  - **This engages WCAG conformance requirement 4 — "only
    accessibility-supported ways of using technologies"** (04 §header;
    the review evaluates against all five, and this is the first time one
    of the non-Level requirements has been engaged). A technique that
    works *only when the user suppresses their assistive technology's
    normal behaviour* is a poor candidate for accessibility-supported.
    The keystroke reaches the application, so 2.1.1 is met; whether the
    method is accessibility-supported is a separate and weaker claim.
  - **Practical cost, which is what bears on the verdict:** the
    pass-through is (a) **undiscoverable** — nothing announces it, and the
    reviewer, an experienced NVDA user, needed a dedicated session to find
    it; (b) **expert-only** — it requires knowing an AT command most users
    never touch; and (c) **per-object** — it must be repeated for every
    object inspected, on top of a layers list that gives no identity and
    no record of what has already been visited.
  - Classified: NV3 / WCAG **4.1.2** (role not exposed, so focus mode is
    never triggered); conformance requirement 4 (accessibility-supported)
    / Major → **T2-F4**. **2.1.1 not failed.**

- **O5 [classified]** (the task itself): the reviewer set out to **find and
  edit "text 2"** among five objects. On the evidence above, the objects
  are reachable and their *type* is partly inferable, but **no object can
  be identified**, and reading an object's content — the only thing that
  would distinguish text 2 from text 1 and text 3 — was not achievable by
  keyboard in this session (O4, open).
  - **Scale note, which was the purpose of this run:** the barrier appears
    at **five objects**, and the mechanism does not improve with practice —
    the announcements are identical regardless of count, so there is no
    strategy a user could learn. The earlier one-object walk (R016) could
    not surface this because with a single object there is nothing to
    distinguish it *from*.
  - Classified: feeds **T2 verdict (W17)** — reviewer's call

- **O6 [classified]** (the structural consequence — reviewer, 2026-08-14):
  *"When we enter the edit mode, we get a readback of the text; however in
  order to get that readback, we need to enter that mode, which means in
  multiple layers, we need to do this dance until we find the right item to
  edit."*
  - **The crux, in one sentence: there is no read-only way to inspect the
    canvas.** Reading an object's content is only possible from inside
    **edit mode**. Identification is therefore not an inspection operation
    at all — it is an editing operation performed repeatedly on objects the
    user does not intend to change.
  - **Why this is worse than "slow".** A sighted user identifies an object
    by *looking* — a free, instantaneous, non-mutating act, performed on all
    five objects at once. The screen-reader equivalent is serial, costly and
    **mutating in kind**: to learn what an object says you must open it for
    editing. The asymmetry is not in speed but in the nature of the
    operation available.
  - **Structural exposure, recorded as such and NOT as an observed
    defect:** because inspection requires entering a mutable state, any
    stray keystroke during a search lands in document content. **This was
    not observed in this session**, and a prior hypothesis of exactly this
    shape ("invisible editing", R015 O5) was raised by the assistant and
    **withdrawn** when the reviewer explained the change had been made with
    the mouse. It is recorded here as a property of the interaction design —
    read-requires-write — not as a claim that data loss occurred. A
    deliberate test would be needed to make any stronger statement.
  - **This is the mechanism behind the scale claim**, stated precisely: the
    cost of finding a known object is *n/2 edit-mode entries on average*,
    each one a five-step probe, with no visited-state to bound the search.
    It does not merely grow with document size — the operation available is
    the wrong kind for the job.
  - Classified: NV3/NV5 / WCAG 4.1.2, 1.3.1 / Major → **T2-F4**; the
    decisive input to T2's verdict (W17)

## Open question — ANSWERED 2026-08-14 (see O4)

The route exists: **pass-through (`NVDA+F2`) then Enter**. 2.1.1 stays
withdrawn. The question was asked rather than assumed because the
inference *"no route visible in this state, therefore no route exists"* is
the documented 2026-08-06 error — and it would have been wrong again.

## The full cost of finding "text 2" — the run's actual result

Assembling O1–O4, this is what the reviewer's task required **per object**,
with five objects present and no way to know which is which in advance:

1. Open NVDA's **form-fields elements list**, find **"Edit page"** (a name
   that does not suggest object selection), activate it, Tab into the
   re-order layers area (O1).
2. Arrow to a layer. Hear `not selected @hz/shared-ui-components:sortable-list-press-space-to-grab row 1 column N` — an untranslated developer
   string and a grid coordinate, and **no indication of what the layer is**
   (O2).
3. Press Space — *sometimes* the Edit pane opens and its summary hints at
   the object's **type**, but never its **identity** (O3).
4. Press **`NVDA+F2`**, then **Enter**, to reach text edit mode and finally
   **read the content** — the only thing that distinguishes "text 2" from
   "text 1" and "text 3" (O4).
5. Exit, and repeat — **with no record of which layers have already been
   visited**, because every row announces identically.

**The task is completable.** It is a linear search with a five-step probe
per object, an expert AT command in the middle of it, and no
visited-state tracking — so a user cannot be certain they have covered
every object, or that they have not checked the same one twice.

**Two independent things make this fail to scale**, and it is worth keeping
them apart because they have different fixes: the **per-probe cost** (fixed
by exposing object identity in the layer rows) and the **absence of
visited-state** (fixed by the same thing — once rows carry names, the user
tracks position by name rather than by memory). Naming the layer rows would
collapse the whole procedure to a single arrow-key pass.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R038-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
