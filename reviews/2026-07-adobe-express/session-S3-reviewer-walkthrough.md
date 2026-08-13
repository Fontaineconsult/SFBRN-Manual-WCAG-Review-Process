# Reviewer Session Walkthrough — S3 Editor ("Text Test" document)

> ## ⏸ PAUSED 2026-08-06 — resume here
>
> **Next action: W12** — reviewer creates a blank document by keyboard/NVDA
> to begin task **T2** (run **R016**, already logged). Parts A/B produced
> R015; Part C is where we stopped.
>
> **State at pause**
>
> | | |
> |---|---|
> | Runs open | **R015** (S3 no-vision, checks unfilled — observations O1–O9 recorded) · **R016** (T2 authoring, not started) |
> | Tasks | T1 Pass with barriers · **T2 Not run** |
> | Instrument | NVDA 2026.1.1 / Chrome 150.0.7871.187, baseline **B4** |
> | Browsers | debug-profile Chrome on port 9222 was left open on the S3 document; the reviewer's own NVDA window is separate |
>
> **The three questions this walk exists to answer**, in priority order:
> 1. **W15 — can an inserted image be given alt text?** Untouched by any
>    run. Decides whether the product lets its users produce accessible
>    output at all — an outward-facing harm, not a single-user barrier.
> 2. **W14** — does anything announce that an inserted image landed?
> 3. **W16** — is export *completion* announced? (4.1.3 has already failed
>    twice on this product for exactly this pattern.)
>
> **Carry-forward from R015 — do not re-derive:** selecting any object
> announces only **"Canvas"**, identically for every object (O9); the route
> into an object is **Tab to layer → Enter → Enter**, announced nowhere
> (O7); the text-editing toolbar that appears is **unlabelled** (O6); the
> editing textarea has **no accessible name** (O8); Italic exposes no
> pressed state while Bold/Underline do (O6).
>
> **Withdrawn — do not resurrect:** 2.1.1 Keyboard is **not** failed (a
> keyboard route exists); text content **is** readable in edit mode; the
> canvas is **not** a permanent black box. Three assistant hypotheses were
> corrected by the reviewer here — see R015 O5/O7 and CLAUDE.md
> §"Why the assistant's probes mislead".


Ordered script for the reviewer-driven testing of S3, the editor. Built
2026-08-06 by mechanical derivation from the live sources (per
`ontology/testing-loop.md` §How to build one): `review.py gaps`, `validate`,
`next`, the R014 axe triage, and the exploration recon in `03` §2.6.

**Document under test** (durable locator — the `?category=…&pageId=…` suffix
in the address bar is transient UI state, not part of the address):

    https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86

Reachable via Your stuff → "Untitled - August 06, 2026 at 13.02.17". It
contains **one text object reading "Text Test"** — that object is the probe
for most of Part A.

Steps are `W#`. Say the step number when you start one. Skip or reorder
freely — just say so. Narrate however you like; the assistant maps it to the
checklist, asks only about gaps, and writes findings/rollup as you go.

**This is planned as several passes.** Part A and B are pass 1 (no-vision,
run R015, NVDA/B4). Parts D–G are later passes needing other instruments and
get their own runs, logged when you start them.

---

## Setup (once per session)

- **Speech Viewer on** before touching the page: `NVDA+N` → Tools → Speech
  Viewer. NVDA has no speech-history recall.
- **Do not press `Insert+Space`** — that is the JAWS speech-history chord; in
  NVDA it toggles browse/focus mode and will silently change what every
  later key does.
- Unfocus this assistant panel while listening (R001 O2: it gets read aloud
  along with the product).
- The editor is a **focus-mode-heavy application**. Expect to move between
  browse and focus mode more than on S1/S2; when something seems
  unreachable, say which mode you were in — that distinction matters for
  whether a barrier is real.

---

## Part A — R015: the canvas question (no-vision, NVDA, baseline B4)

**Why this part comes first.** The editor paints the entire user document
into a single `<canvas>` (2328×1145) that carries **no `role`, no
`aria-label`, no `aria-hidden` and zero fallback children**, and the visible
"Text Test" element **appears nowhere in the DOM** across all 960 open
shadow roots (03 §2.4, §2.6). The axe sweep (R014) reported *nothing at all*
about the canvas — 43 passes and not one line about it. **Automation cannot
answer this; only you can.** If the document is genuinely unexposed, it is
the most serious defect available in this product, because it makes the
user's own work imperceptible rather than merely awkward — and it lands on
every step of process P2 (edit and export).

### W1 — Entering the canvas (NV2, NV3) — KEY STEP

**Do:** From the top of the page, navigate down until you reach the canvas /
document area. Try both browse-mode arrowing and `Tab`.
**Tell me:** Is the canvas region announced at all? Is there any boundary —
do you know you have entered "the document"? There is an `h2` named
"Canvas" in the DOM; do you reach it, and does it help?
**Feedback:** _(pending)_

### W2 — Can you perceive the document's content? (NV3, NV4) — THE KEY STEP

**Do:** With the canvas focused/entered, try to find the text object. Arrow
around, `Tab`, and try NVDA object navigation if browse mode gives nothing.
**Tell me, precisely:**
- Is there **any** indication the document contains an object at all?
- Can you **read the words "Text Test"** by any means?
- Can you **select** the object, and does selection announce?
**Why it matters:** this single answer decides whether P2 (edit and export)
is walkable at all by a screen-reader user, and it is the difference between
"the editor has barriers" and "the editor's documents are unreadable
without sight."
**Feedback:** _(pending)_

### W3 — Object properties, if W2 found anything (NV3, NV8)

**Do:** With the text object selected, listen for what is exposed.
**Tell me:** Do you get its content, its type (text vs image vs shape), its
position or size, or its state (selected/locked)? Or just "graphic"/silence?
Anything conveyed **only** by visual position (NV8 / 1.3.3)?
**Feedback:** _(pending)_

### W4 — Pages and page navigation (NV3, NV7)

**Do:** Find the page navigation (bottom right: "Add page", and a page
strip). Try to determine how many pages the document has and which one you
are on.
**Tell me:** Is page count and current page announced? Does adding a page
announce anything?
**Feedback:** _(pending)_

---

## Part B — R015: editor structure and controls (same run)

### W5 — Headings (NV2)

**Do:** `NVDA+F7` → Headings; also walk with `H`.
**Expected from the DOM:** `h2` "Untitled…", `h2` "Daniel Fontaine", `h2`
"Canvas", `h2` "Search", then `h3` per asset-panel section (Templates,
Photos, Design assets, Icons, Shapes, Stickers, Backgrounds, Videos, Music,
Sound effects, Charts). **There is no `h1`.**
**Tell me:** Does that match? Is "Canvas" reachable as a heading?
**Feedback:** _(pending)_

### W6 — Landmarks (NV2) — KEY STEP

**Do:** `NVDA+F7` → Landmarks.
**Tell me:** What landmarks exist? Is there a **`main`**?
**Why it matters:** axe and the exploration probe **both** say the editor
has **no `main` landmark**, and that it has *two* unlabelled `<header>`
banners. On S1 the presence of `main` is the entire reason finding V-F3
narrowed 2.4.1 to keyboard-only users (screen-reader users could bypass via
ARIA11). **That reasoning does not transfer here.** If you confirm no
`main`, 2.4.1 is worse on S3 than on S1, for screen-reader users too — and
that is a finding S1's evidence cannot support.
**Feedback:** _(pending)_

### W7 — Reaching the work surface (MO11 / 2.4.1)

**Do:** Reload the editor. Count how many stops it takes to get from page
load to the canvas, and to the left rail.
**Tell me:** Is there any skip mechanism? How many stops? With no `main`
landmark (W6), what is your fastest route to the document?
**Feedback:** _(pending)_

### W8 — Confirm V-F10: the page-nav "more" button (NV3 / 4.1.2)

**Do:** Find the **page-navigation "more" menu button** (page strip area,
bottom of the canvas). Focus it.
**Tell me:** Exact speech on focus.
**Why it matters:** axe says it has no accessible name at all (R014 O1). Your
ear either confirms V-F10 or kills it. **Confirm on focus, not from the
elements list** — R012 O9 showed NVDA's list rendering nearly produced a
false finding on S1.
**Feedback:** _(pending)_

### W9 — Left rail and top bar (NV3)

**Do:** Tab the left rail (Search, Add content, Text, Upload, Your stuff,
Brands, Templates, Styles, Add-ons) and the top bar (File menu, zoom,
undo/redo, comments, Download, Share).
**Tell me:** Anything unnamed, wrongly named, or missing state (e.g. does
the zoom control announce its value? do toggles announce pressed state?).
**Feedback:** _(pending)_

### W10 — Asset panel (NV3, NV7)

**Do:** In the Search panel, use the content search field, and the
category/orientation selector on the left of it.
**Tell me:** Does the search field announce its label? Do results announce
when they load? Recall S2's grid was silent on both counts — is this panel
the same component or better?
**Note:** axe flagged `aria-orientation="vertical"` on
`x-asset-category-select` as possibly-ignored (R014 O4), and an unresolvable
`aria-controls` on the search input (R014 O5) — both resolve here.
**Feedback:** _(pending)_

### W11 — R015 verdict (NV1, NV5, NV6, NV9 + Result)

**Do:** Gut check. Also: what is announced on load (NV1)? Any
mispronunciation (NV9)?
**Tell me:** Works / Works with issues / Broken for a no-vision user, and
the one worst thing.
**Feedback:** _(pending)_

---

## Part C — task walk T2: author a design from scratch (run R016)

Cluster **T2** created and run **R016** logged 2026-08-06. Reviewer's
scenario: author a *new* document rather than edit a prepared one — this
also exercises the create flow and the empty-canvas state, which no run has
touched.

Carry forward from Part A/B (expect these to compound, not reappear fresh):
selecting an object announces only **"Canvas"** identically for every object
(R015 O9); the route into an object is **Tab to layer → Enter → Enter**,
announced nowhere (O7); the text-editing toolbar is **unlabelled** (O6); the
editing textarea has **no accessible name** (O8).

### W12 — Create a blank document (P1-a branch)

**Do:** From Home, create a **blank** document (not from a template).
**Tell me:** Can you complete it by keyboard/NVDA? Is the new document's
arrival announced — do you know you are now in an editor with an empty
canvas? (V-F8 says the title will not tell you.)
**Note:** this creates a persistent artifact; tell me its name so it is
recorded in 03 §2.6 with the others.
**Feedback:** _(pending)_

### W13 — Add a text element and set its content (P2 step 1)

**Do:** Use the rail's **Text** item to add text, then set the wording.
**Tell me:** Is the new element announced when added? Do you land in edit
mode automatically, or must you do the Tab→Enter→Enter route again? Can you
confirm what the text now says without using the mouse?
**Feedback:** _(pending)_

### W14 — Insert an image (P2 step 2) — KEY STEP

**Do:** From the asset panel, insert any image into the canvas.
**Tell me:**
- Can you find and choose an image by ear? (S2's template grid could not be
  navigated this way — is this panel the same component or better?)
- **Does anything tell you the image landed on the canvas?**
- Once inserted, can you tell it apart from the text object — or does it
  also announce only "Canvas"?
**Feedback:** _(pending)_

### W15 — Alt text on the inserted image — KEY STEP, and the one that matters most for procurement

**Do:** Try to give the inserted image **alternative text**. Look in the
right-hand properties/panel, a context menu, the toolbar that appears on
selection, or object settings.
**Tell me:** Is there an alt-text field at all? Can you reach and fill it
with the keyboard? Is it announced?
**Why it matters more than anything else in this walk:** this determines
whether the product lets *its users produce accessible output*. A design
tool whose users cannot add alt text means every artefact the institution
publishes with it carries inaccessible images — a compounding,
outward-facing harm rather than a barrier to one user. It also bears on
1.1.1 in a way no view sweep can reach, and no run so far has touched it.
**Feedback:** _(pending)_

### W16 — Export / download (P2 steps 3–5)

**Do:** Activate Download / Share, choose a format, confirm, and see it
through to the file arriving.
**Tell me:** Is the export dialog announced as a dialog? Are format options
reachable and labelled? Is progress announced? **Is completion announced**,
or does the file arrive silently? (4.1.3 has already failed twice on this
product for exactly this pattern — S2's search results and lazy grid.)
**Feedback:** _(pending)_

### W17 — T2 verdict

**Tell me:** Could you author and export a usable design end to end? Pass /
Pass with barriers / Fail, and the step where it was worst.
**Note the cascade:** as on T1, a Blocker-level failure at any step makes
S3's no-vision cell **Broken**, which under modality-checks.md forces this
task's verdict to **Fail** for no-vision users. That is a real possibility
here and it is your call, not the assistant's.
**Feedback:** _(pending)_

---

## Part D — later pass: no-hearing (**not N/A on this view**)

**First view in this review where no-hearing is live.** S1 and S2 were both
N/A; do **not** copy that forward. The asset panel offers **Videos, Music
and Sound effects** the user can insert, which are real media (NH1–NH4 /
1.2.1, 1.2.2, 1.2.4). axe already flagged a `<video>` in the panel, though
that one is a muted looping preview thumbnail and probably out of scope
(R014 O6) — the live question is insertable media, which no sweep touched.

**Feedback:** _(pending)_

---

## Part E — later pass: low-vision (400% zoom, baseline B3)

Reflow of a canvas application at 400% is the classic failure case, and
1.4.10 exempts some canvas content — expect judgement calls. Also carries
the S1 leftovers: LV5 (component/graphic contrast) was never completed
there. **Do not trust axe contrast numbers on this view** — R014 O2 produced
two false-positive contrast violations here by assuming a background;
measure with the eyedropper.

**Feedback:** _(pending)_

---

## Part F — later pass: motor (physical keyboard, baseline B2)

Canvas manipulation is the drag-and-drop risk area (2.5.7 / MO7): moving,
resizing and rotating objects. Check for single-pointer, non-drag
alternatives. Also MO6 — an editor is the most likely place in the product
for **single-character shortcuts** (2.1.4).

**Feedback:** 2026-08-13 (run R031, Works with issues) — translation YES,
z-order YES (via "…" menu), **rotation NO → finding V-F14 (2.1.1/2.5.7)**;
"generally keyboard accessible, if not slow to use". Object moves announce
nothing to AT (folds into the canvas-identity finding; reviewer
recommendation recorded: on-demand spoken canvas description). "T" is the
one single-char shortcut (creates text box) — 2.1.4 candidate pending a
Settings check. Shortcut docs out of sync both directions (documented
rename broken; undocumented working shortcuts exist). **Remaining: resize
by keyboard; the Settings disable/remap check.**

---

## Part G — later pass: cognition, no-color, no-speech

Lower priority; scheduled after the above. Note CO1/CO2 (consistency,
3.2.3/3.2.4/3.2.6) become answerable across S1/S2/S3 once this view is done
— they could not be answered from a single view.

**Feedback:** _(pending)_

---

## Close-out (assistant does; you watch)

- Every Feedback line filled or the step explicitly skipped
- R015 checks + observations written; Result derived and set
- Findings raised/confirmed/withdrawn in `04`; rollup updated in `05`
- Enclosure (`03`) updated if the walk reveals unmapped states
- `validate` and `matrix` re-run
- Decide: is S3 done enough to move to S4, or does P2 (Part C) come first?
