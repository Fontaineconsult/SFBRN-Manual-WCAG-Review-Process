# Test Run R012 — S1

| | |
|---|---|
| **Run ID** | R012 |
| **Date/time** | 2026-08-06 12:46 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B4 |
| **Tester** | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 150.0.7871.187 |
| **Result** | Works with issues |

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O16 — "Adobe Express" announced; passes for S1 in isolation, but see the cross-view candidate |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | pass | O2, O5, O7 — headings match Chrome + JAWS (incl. h3 Recent); landmarks banner/Primary/navigation/**main** present. JAWS's `search` landmark absent in NVDA (recorded, not raised) |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O1 → V-F4 (community button, 1 control); O10 → V-F5 (10 identical "Browse templates"); O9 tab-label conflict open |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O14 → V-F7 ("Clickable Figure {name}, Unlabeled Graphic" — decorative image not hidden) |
| NV5 — Reading order matches the meaning of the visual order | pass | O3 — unscoped: O2 refuted, Recent is reachable after all |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | partial | O17 — search field announces its label as predicted; no error path exists on S1 to exercise |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | partial | O15 — modal open announces its entire contents until the user navigates; toasts/async not yet exercised |
| NV8 — Nothing is conveyed only by visual position, shape, or size | pass | reviewer: no |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | reviewer: no mispronunciation; consistent with `lang="en-US"` on the html element (03 §2.4) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: default, reviewer narration 2026-08-06, NVDA): "buttons
  remain unnamed" — **plural**. Confirms by ear what axe found by rule
  (R009 O2) and what the vendor's own ACR concedes (4.1.2 Does Not Support).
  - Corroboration from Chrome's accessibility tree (assistant, CDP
    `Accessibility.getFullAXTree` on verified S1): of 48 exposed interactive
    nodes, exactly **one** carries no accessible name —
    `<sp-action-button role="button" slot="trigger">`, the header community
    icon. So the tree accounts for one unnamed control, the reviewer heard
    more than one.
  - **RESOLVED same session (reviewer, on enumeration): "only control is
    Community unnamed."** The plural in the first narration was loose; there
    is exactly one. Three instruments now agree precisely — NVDA by ear,
    Chrome's accessibility tree, and axe-core — on **one** unnamed control,
    the header community icon.
  - Important negative result, worth recording because it was the worse
    hypothesis: NVDA is **not** failing to read names that Chrome exposes.
    The app's Spectrum web components map correctly to the platform
    accessibility API; the defect is a single missing label, not a systemic
    component-mapping failure. An assistant DOM-walk had estimated 11
    unnamed controls — that estimate was **wrong** (it missed how Spectrum
    exposes slotted names) and is discarded in favour of the AX tree.
  - Classified: NV3 / WCAG 4.1.2 / Major → **confirms finding V-F4**, scope
    = 1 control on S1.
- O2 [new] (state: default, reviewer narration, NVDA): **"I can't find
  Recent at all."** Reviewer questioned whether the assistant was reporting
  something that is not there.
  - Verified independently before treating this as a defect (assistant): the
    Recent bar **is** present and **is** exposed. Chrome's accessibility
    tree contains `role=heading level=3 name="Recent"` (`<h3>`), a
    `StaticText "Recent"`, and `role=link name="View all recent files"`
    (`<a>`) — none marked hidden. The DOM shows `x-home-recent-bar` visible,
    no `aria-hidden`, no `inert`, no `display:none` anywhere up the
    ancestor chain across shadow boundaries. It is also visible on screen as
    the bottom strip (screenshot, this session). **JAWS found it too** —
    R001 O3 recorded "Recent" as a level-3 heading in its outline.
  - **REFUTED same session — no defect.** On checking the Elements List the
    reviewer reported: *"headings match … I see, the Recent view is at the
    bottom of the screen and is H3."* NVDA exposes Recent exactly as Chrome
    and JAWS do. The initial "can't find" was a locating difficulty in a
    live session, not a failure of exposure.
  - **Method caveat, recorded for honesty:** the confirmation was made
    against a heading list the assistant supplied, which carries a
    leading risk. Two things offset it — the reviewer independently
    volunteered the position ("bottom of the screen") and the level ("is
    H3"), neither of which was asked for; and the count was reported as
    matching rather than merely present. If NV2 is ever contested, re-run it
    blind (ask for the list *before* showing one).
  - Why this mattered enough to chase: had it held, it would have reopened
    the shadow-DOM concern in 03 §2.6 and destroyed the basis for the V-F3
    amendment (which narrowed 2.4.1 to keyboard-only users because
    landmarks give screen-reader users an ARIA11 bypass). Instead the
    opposite is now true — see O5.
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 / pass — **no finding**; candidate
    withdrawn.
- O5 [classified] (derived from O2's resolution — the structural conclusion
  of this run): the heading structure is now confirmed by **two independent
  screen readers** (JAWS, R001 O3 on 2026-08-04; NVDA, here) plus Chrome's
  accessibility tree — same outline, same levels, `h1` "How would you like
  to start?", `h3` "Recent" included.
  - Consequence 1: the shadow-DOM opacity concern (03 §2.6) is closed for
    good. It was a **tooling artifact** of extraction-based automation, and
    this session reproduced that artifact a third time — the browser
    extension's `read_page` returned an entirely empty tree on a page whose
    AX tree holds 1,588 nodes. Extraction-based recon must never be used for
    AT-facing conclusions on this product.
  - Consequence 2: **finding V-F3's amendment holds.** Screen-reader users
    of either major reader get real structure, so the 2.4.1 barrier remains
    scoped to keyboard-only (non-AT) users, exactly as R001 O7 argued.
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 / pass — no finding
- O3 [classified] (state: default, reviewer narration, NVDA): "read order is
  strong." Reading order matches the meaning of the visual order.
  - Note the interaction with O2: the earlier NV5 concern (R001 O5) was
    specifically that "Recent" reads *third*, right after the greeting,
    despite being the visually-bottom strip. If NVDA never encounters Recent
    at all, that concern cannot have been exercised — so this pass covers
    the rest of the view, and the Recent-position question is **superseded
    by O2**, not answered by it.
  - Classified: NV5 / WCAG 1.3.2 / pass (scoped: excludes the Recent bar)
- O4 [new] (state: default, reviewer narration, NVDA): "all elements are
  reachable by keyboard **or through NVDA commands**."
  - **Cannot be recorded as a single outcome — the two halves land on
    different criteria and different users.** 2.1.1 Keyboard asks whether
    everything is reachable by keyboard *alone*, with no AT; NVDA's browse
    mode, quick-navigation keys and Elements List are assistive-technology
    affordances that a keyboard-only user without a screen reader does not
    have. This is precisely the distinction that finding V-F3 turns on
    (R001 O7 narrowed 2.4.1 to keyboard-only users because landmarks give
    screen-reader users a bypass that Tab alone does not).
  - **ANSWERED on the split question: "yes all reachable by keyboard
    alone."** So reachability holds without AT affordances — this is a
    genuine 2.1.1 signal, not a browse-mode artifact.
  - **Does not disturb finding V-F3.** 2.1.1 asks whether controls can be
    *reached*; 2.4.1 asks whether repeated blocks can be *bypassed*. Every
    control being Tab-reachable is fully compatible with a keyboard-only
    user still having to traverse ~15 app-bar stops on every page visit to
    get there. V-F3 stands unchanged, and the reviewer's 2.4.1 decision
    (failure vs advisory) is still open.
  - Recorded here as reviewer testimony under baseline B4. **Formal MO1
    closure stays with R004 (motor, B2)** — cross-referenced there rather
    than closed from a screen-reader session, since B2 is mouse-free by
    definition and this session was not.
- O6 [new] (state question raised by the reviewer, unresolved): reviewer
  noted *"there are no recent files in our account so new view appears, i
  guess?"* — i.e. the Recent strip may have been in its **empty state**.
  This does not affect O2's resolution (the heading is exposed either way),
  but it flags a **view state that has never been tested deliberately**.
  Evidence points the other way: axe (R009) captured a Recent file card with
  alt "Kaiser Permanente Mobile App - Letter Details", and two "Untitled"
  documents now exist from assistant sessions (03 §2.6), so the account does
  hold recent files.
  - Routed: confirm which state S1 was in during this run, and add the
    Recent bar's **empty vs populated** states to the enclosure if they
    differ structurally — an empty state that drops the heading entirely
    would change NV2/NV5 outcomes for a first-time user.
- O7 [classified] (state: default, reviewer narration, NVDA landmarks list):
  NVDA exposes **banner, Primary, navigation, main**. Recent files appear as
  links in the links list.
  - **`main` is present → finding V-F3's amendment now holds for both
    screen readers**, not JAWS alone. The ARIA11 landmark-bypass argument
    that narrowed 2.4.1 to keyboard-only users is confirmed across the two
    major readers, and the reviewer's 2.4.1 decision can be made on that
    settled basis.
  - **One cross-AT discrepancy, minor but real:** JAWS reported five
    landmarks including a **search** landmark (R001 O7); NVDA's list does
    not include it. Not a WCAG failure on its own — the search field is
    still reachable and named — but it means landmark-based navigation to
    search works for JAWS users and not NVDA users. Recorded, not raised.
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 / pass (completes NV2 with O5)
- O8 [classified] (state: **"Get started" modal** — the significant S1 state
  that no AT had previously touched; reviewer narration, NVDA): the modal
  behaves **well** on the things SPAs usually break:
  heading "Get started" exposed as an **H1**; focus moves into the dialog on
  open; **all elements inside are announced clearly**; **`Esc` closes it**;
  and every element inside is **reachable by keyboard alone**.
  - Notable in context: R002 O5 found the left-rail hover flyout ignores
    `Esc` entirely (finding V-F1). The modal handles `Esc` correctly, so the
    app's Esc handling is **inconsistent between components** rather than
    uniformly absent — which points at the flyout as the defect, not a
    platform-wide pattern.
  - Classified: NV3/NV7 partial, MO3 positive signal / pass — no finding.
    Still unrecorded for this state: whether focus is **trapped** while
    open, and **where focus returns** after `Esc`. Both are MO3/2.4.3
    questions and neither was narrated.
- O9 [new] (state: modal; **instrument conflict — do not resolve by fiat**):
  reviewer reports the category tabs announce as *"Unlabeled, tab"* in
  NVDA's elements list. Chrome's accessibility tree says the opposite: all
  **7** tabs carry correct accessible names — 'Standard & Suggested',
  'Social media and ads', 'Video', 'Photo', 'Document', 'Webpage', 'Print'
  (`sp-tab role="tab"`, verified via CDP `Accessibility.getFullAXTree`, 0
  unnamed controls anywhere in this state).
  - Two possibilities with very different severities: (a) NVDA's *elements
    list* renders tab entries without their label while the tab announces
    correctly **when focused** — a cosmetic AT quirk, no finding; or (b) the
    name genuinely fails to reach NVDA, in which case a 7-tab navigation
    control is unusable by name and this is a **Major 4.1.2** failure that
    axe and Chrome both miss.
  - **RESOLVED — benign branch (reviewer): "those labels do exist."** The
    tabs announce their labels correctly when focused; the "Unlabeled"
    rendering is confined to NVDA's elements-list view. Chrome's tree and
    the reviewer's ear now agree. **No finding.**
  - Kept in the record deliberately as an instrument lesson: an AT's
    *elements list* can render a control differently from what it announces
    on focus. Never raise a name finding from a list view alone — confirm on
    focus. Had this not been checked, a Major 4.1.2 would have been filed
    against a correctly-labelled 7-tab control.
- O13 [classified] (state: "Get started" modal; reviewer: **"focus is not
  trapped"**): the dialog does not contain keyboard focus. Tabbing past its
  last control moves focus out into the page behind **while the dialog is
  still open**.
  - Why this is a defect and not the MO3 pass it superficially resembles:
    MO3 asks that focus is never *trapped* — that a user can always get out
    — and that is satisfied. A modal dialog has the opposite obligation
    while open: it must **contain** focus, so the user cannot silently end
    up operating content the dialog is covering. Both properties are
    required; this app has the first and not the second.
  - Consequence for a screen-reader user: no boundary is announced, so they
    continue tabbing and begin hearing home-page controls with no signal
    that they have left the chooser — and the dialog is still open on top of
    what they are now operating.
  - Assistant attempted to measure whether the background is suppressed
    (`aria-hidden`/`inert`) to size the severity; **the measurement anchored
    on the wrong element and is discarded**. One usable signal survived: no
    `aria-hidden` or `inert` attribute was found anywhere in the sampled
    set, which sits oddly beside O12 (NVDA offering only a 'form' landmark
    while the modal is open). Unresolved.
  - **WITHDRAWN same session — no defect. Finding V-F6 retracted.** On the
    severity question the reviewer described the actual behaviour: *"cycling
    tab at the end moves to main browser controls then circles back to
    modal."* That is **correct modal focus containment** — focus cycles
    modal → browser chrome (outside the document) → back to the modal, and
    never reaches the page content behind. Nothing escapes.
  - **Assistant error, recorded rather than quietly deleted.** The reviewer's
    original phrase "focus is not trapped" was an answer to the MO3 check
    (*can you always get out?* — yes) and the assistant read it as *focus
    escapes into background content*, then compounded it by building a
    severity question on the false premise; the reviewer's "not sure what is
    meant by background controls" was the signal the premise was wrong.
    Lesson for this process: when a reviewer's phrase maps onto a checklist
    item's exact wording, read it as the answer to *that* check — do not
    re-interpret it into a finding. Confirm the behaviour before filing.
  - Classified: MO3 / WCAG 2.1.2, 2.4.3 / **pass** — no finding. Combined
    with O8 (focus moves in on open, `Esc` closes), the "Get started" modal
    now tests as **well-behaved on every focus property checked**.
- O14 [classified] (state: default, NV4 — reviewer walked graphics with
  `G`): images announce in the pattern **"Clickable Figure {name of figure},
  Unlabeled Graphic"**. The figure carries a name, and then an **unlabelled
  graphic** is announced inside it.
  - Reading: the wrapping figure supplies the meaningful alternative, so
    information is not lost — but the inner image is neither given an
    alternative nor marked decorative (`alt=""` / `aria-hidden`), so it is
    announced as "Unlabeled Graphic" noise on every card. Under 1.1.1,
    decorative images must be hidden from assistive technology; announcing
    an unnamed graphic beside a named figure is the documented failure.
  - **Corroborates the vendor's own ACR**, which concedes 1.1.1 Partially
    Supports and specifically cites *"The decorative image is not hidden
    from screen readers"* on another screen. Same defect class, now
    evidenced on S1.
  - Classified: NV4 / WCAG 1.1.1 / Minor → **new finding V-F7**. Minor
    rather than Major because the figure name carries the meaning; the cost
    is verbosity on every card, not lost information.
- O15 [new] (state: modal open; reviewer): **"on modal load the entire modal
  elements list is announced until the user begins nav."** Opening the
  chooser causes NVDA to read the dialog's whole contents before the user
  can act; navigating interrupts it.
  - Sits in tension with O8's positive result. Focus moving into a dialog is
    correct; announcing the *entire* contents is what happens when a
    dialog's accessible name or description resolves to its whole subtree
    rather than to its title — the H1 "Get started" exists, so the dialog
    may not be associated with it (`aria-labelledby`) and AT falls back to
    reading everything.
  - Not clearly a single SC failure, and deliberately **not raised as a
    finding**: verbosity is a real barrier but WCAG has no "too chatty" SC.
    Candidate criterion is 4.1.2 (dialog's name not correctly computed).
    Pairs with O11/O12 as a cluster of dialog-semantics weaknesses.
  - Routed: check whether the dialog element has `aria-labelledby` pointing
    at the "Get started" H1, and re-test after any fix.
- O16 [classified] (state: fresh load, NV1 — reviewer): NVDA announces
  **"Adobe Express"**. The reviewer added that more has been announced in
  past sessions — consistent with the JAWS load summary recorded in R001 O1
  ("3 headings, 2 regions, 1 link"), which NVDA does not emit by default.
  Not a product difference; an AT difference.
  - Classified: NV1 / WCAG 2.4.2 / pass — no finding **for S1 in isolation**
  - **Cross-view candidate raised, needs S2 to confirm:** the title appears
    to be the product name on *every* SPA view, not the view. Assistant
    observed the tab titled "Adobe Express" while on
    `/explore/templates?assetCollection=…` (S2) as well as on Home — while
    an opened document *does* retitle ("Untitled - August 06, 2026 at
    13.02.17"). If Home, Explore and Your stuff all announce "Adobe
    Express", then a screen-reader user gets **no announcement that the view
    changed**, and 2.4.2 (titles describe topic or purpose) is arguably
    failed for every view but the editor. This cannot be settled from S1 —
    it is a property of the set.
  - **CONFIRMED 2026-08-06 → finding V-F8.** Reviewer: *"Adobe Express is
    all that's announced as Title for every page."* Corroborated
    independently by the assistant navigating four views and reading
    `document.title` at each — Home, Explore/templates, Your stuff, Brands:
    **4 views, 1 distinct title ("Adobe Express")**. Documents retitle, main
    views do not. Recorded as a product-wide finding in 04 §B, and 2.4.2 set
    to **Does Not Support** — below the vendor's own "Partially Supports".
  - Worth keeping visible in the method notes: this defect is invisible to
    a per-view sweep *and* to every automated checker, because each view
    does have a title. It surfaced only because the reviewer moved between
    views and noticed the announcement never changed.
- O17 [classified] (state: default, NV6 — reviewer confirmed): the home
  search field announces its label. Matches the prediction from R010 O2
  (`aria-label="Search for templates and more"`, rotator `aria-hidden`), so
  the DOM evidence and the ear agree.
  - **Also closes the 2.5.3 candidate held in R001 O8 — as no finding.**
    That candidate rested on the visible rotating placeholder differing from
    the accessible name. Two things retire it: the reviewer heard a correct,
    stable label, and R010 O1 found the rotation is not running in steady
    state, so there is no persistent competing visible label to mismatch.
    Recorded as withdrawn rather than deleted; revisit only if the rotation
    is later observed running continuously.
  - Classified: NV6 / WCAG 3.3.2 / partial — no finding. Partial not pass:
    S1 offers **no error path**, so the "errors are announced and
    identified" half of NV6 is untestable on this view and must be covered
    in the P1/P2 task runs (§A), where invalid input actually occurs.
- O10 [classified] (state: modal; reviewer: "many generic 'Browse Templates'
  buttons with no meaningful name"): **confirmed and counted — exactly 10.**
  Ten `sp-button` controls, laid out in a grid, each with the accessible
  name **"Browse templates"** and the same visible text. Verified in the
  accessibility tree, so this is what a screen reader actually receives.
  - A user navigating by button list hears "Browse templates, button" ten
    times with nothing to distinguish them; the only thing that separates
    them is the category card each sits in, conveyed visually by proximity.
  - **2.5.3 Label in Name is NOT violated** — visible text and accessible
    name match exactly. The defect is that the label does not describe
    *which* templates, i.e. **2.4.6 Headings and Labels**. If the
    button→category association is not programmatically determinable,
    **1.3.1** is also implicated.
  - Classified: NV3 / WCAG 2.4.6 / Major → **new finding V-F5**
- O11 [new] (state: modal): **none of the "Get started" options appear in
  NVDA's elements view**, although they are reachable by keyboard and
  announced when reached (O8).
  - Not automatically a WCAG failure — elements-list enumeration is an AT
    affordance, not a WCAG requirement, and the controls are operable and
    named. But it removes the primary way screen-reader users survey a
    dialog's choices, forcing linear Tab traversal through a large grid.
    Likely cause: the options carry a role the elements list does not
    categorise.
  - Routed: pair with O9 — both are "exposed to Chrome, not surfaced by
    NVDA" symptoms and may share one root cause in the Spectrum components.
- O12 [new] (state: modal): with the modal open, NVDA's landmarks list shows
  only **'form'**. The dialog exposes no landmark structure of its own, and
  the page's banner/main/navigation landmarks are (correctly) not offered
  while the dialog is modal. Recorded as context for O11 — with no landmarks
  and no elements-list entries, linear Tab is the *only* way through this
  dialog for an NVDA user.

## Notes

**Result derivation:** fails at NV3 (V-F4 unnamed community button; V-F5 ten
identical "Browse templates" labels) and NV4 (V-F7 unlabelled decorative
graphic). None is Blocker-level — the view remains operable by a
screen-reader user with real friction — so per modality-checks.md the
Result is **Works with issues**, not Broken.

**Continues R001 under a different screen reader.** R001 (JAWS, B1) is
suspended at 2026-08-06 with NV1/NV2 filled; NV3–NV9 are carried here. JAWS
evidence is **not** transferable — the two readers differ in accessible-name
computation, ARIA state exposure, and shadow-DOM handling — so nothing from
R001 is copied forward as a pass.

Capture convention for NVDA (JAWS habits will mislead here):
- Exact wording comes from the **Speech Viewer** (NVDA menu `NVDA+N` →
  Tools → Speech Viewer), enabled *before* testing. NVDA has no
  speech-history recall equivalent to JAWS's `Insert+Space, H`.
- **`Insert+Space` means something different in NVDA** — it toggles
  browse/focus mode. Pressing the JAWS speech-history chord here silently
  drops out of browse mode and changes what every later keystroke does.

**Priority re-verification — the highest-value question in this run.**
R001 O3/O7 concluded that the near-empty automated accessibility tree was a
*tooling artifact*, because JAWS found a full 13-heading outline and five
landmarks (Apps[nav], banner, Primary[nav], main, search). That conclusion
now rests on one screen reader. If NVDA does **not** find the same
structure, the "resolved" shadow-DOM concern in 03 §2.6 reopens as a real
and serious finding, and the V-F3 landmark-bypass amendment (which narrowed
2.4.1 to keyboard-only users on the strength of ARIA11) loses its basis.
Compare NVDA's Elements List against R001's recorded JAWS outline before
anything else.

## Evidence files in this folder

- (screenshots/exports named R012-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
