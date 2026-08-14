# Test Run R013 — S2

| | |
|---|---|
| **Run ID** | R013 |
| **Date/time** | 2026-08-06 14:18 |
| **View / sample** | S2 |
| **Page URL / location** | https://new.express.adobe.com/explore/templates |
| **Task / process** | T1 |
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
| NV1 — Page/view title identifies its purpose | fail | O1 — title stays "Adobe Express"; arriving at S2 announces nothing (V-F8) |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | fail | O2 — only "Explore" and "Filters" → V-F9 |
| NV3 — Every control announces an accurate name, role, and value/state | fail | O7 (templates unnamed), O6 (dual role), O5 (silent arrow nav) → T1-F2; O9 filters/tabs pass |
| NV4 — Images announce appropriate alternatives; decorative images are silent | fail | O12 — `G` finds **no graphics at all** on a view built from template thumbnails → T1-F2 |
| NV5 — Reading order matches the meaning of the visual order | fail | O4 — name is a separate tab stop from the item; leaving the grid unannounced |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | partial | O13 — search field labelled and reachable; no error path on S2 to exercise the errors half |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | fail | O3 (grid entry silent), O8 (lazy-loaded results not announced) |
| NV8 — Nothing is conveyed only by visual position, shape, or size | fail | O7 — templates are distinguishable only by their visual thumbnail |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | pass | reviewer: no mispronunciation |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
All observations from reviewer narration, NVDA 2026.1.1 / Chrome
150.0.7871.187, baseline B4, 2026-08-06. Assistant corroboration of the grid
(O6/O7) was attempted but the debug-profile browser had been closed; the
reviewer's account stands as the evidence.

- O1 [classified] (state: **P1 step 1 → 2**, activating Templates in the
  left rail): NVDA announces **"current page, current page"** — the nav
  item's own state, repeated. *"It is not clear we are on the templates
  page… focus remains on the template button in the nav area… it's not clear
  we are the new view."* To find out where you are, you must go inspecting
  buttons and links.
  - Three things fail together at this transition: the title does not change
    (V-F8), focus is not moved into the new view, and nothing is announced.
    Individually each is survivable; together the user is given **no signal
    at all** that a navigation occurred.
  - Classified: NV5/NV7 / WCAG 2.4.3, 2.4.2 / Major → **task finding
    T1-F1** (recorded in 04 §A — it is a barrier to the *process*, not a
    property of either view alone)
- O2 [classified] (state: S2 default, NV2): heading list contains **only
  "Explore" and "Filters"** — *"nothing useful."* For comparison S1 exposes
  ten headings including a level-1. A template gallery with visible
  category/section structure exposes two headings, so heading navigation —
  a screen-reader user's primary orientation tool — gives almost nothing.
  - Classified: NV2 / WCAG 1.3.1 / Major → **finding V-F9** (04 §B, S2)
- O3 [classified] (state: S2, entering the template grid): the lazily-loaded
  templates area is **not announced when entered**. No region, no label, no
  count — the user simply begins landing on items.
  - Classified: NV7 / WCAG 1.3.1, 4.1.3 → folded into **T1-F2**
- O4 [classified] (state: S2, per template item): each template costs
  **four tab stops** and the order is counter-intuitive: land on the
  image → Tab to hear its title → Tab reaches the heart/favourite
  button → Tab reaches the premium-access button → Tab **leaves the entire
  templates area, and it is not clear you have left**. So the *name* of a
  thing is a separate stop from the thing itself.
  - Classified: NV3/NV5 / WCAG 2.4.3, 1.3.1 → folded into **T1-F2**
- O5 [classified] (state: S2, grid): the workable pattern the reviewer found
  is *tab in, tab out, then arrow to the next item* — but **"you never hear
  that you've moved to a new item with the arrow key."** Arrow navigation
  through the grid is **silent**.
  - This is the most disabling single behaviour on the page: the only
    efficient way to move through the grid gives no feedback at all.
  - Classified: NV3/NV7 / WCAG 4.1.2, 1.3.1 → folded into **T1-F2**
- O6 [classified] (state: S2, grid): each template item is exposed **as both
  a form element and a button** in NVDA's element views — a single control
  presenting two conflicting roles.
  - Classified: NV3 / WCAG 4.1.2 → folded into **T1-F2**. Assistant
    corroboration outstanding (see header note).
- O7 [classified] (state: S2, grid) — **the core defect: "the templates have
  no identifiable name."** The items a user must choose between cannot be
  told apart by a screen reader.
  - Note the sharp contrast with O10: once a template is *selected*, its
    name is available as an `h2` in the resulting modal. The name exists in
    the product; it is simply not exposed at the point of choosing.
  - Classified: NV3 / WCAG 4.1.2, 2.4.6 / Blocker-candidate → **T1-F2**
- O8 [new] (state: S2, scrolling): scrolling down loads new items and they
  **do** appear in NVDA's element views — so lazily-added content is not
  lost. But *"I'm not sure how to scroll them to find anything reliably."*
  Arrival of new results is not announced (4.1.3), and with O5 and O7 there
  is no dependable way to search the grid by ear.
  - Vendor claims 4.1.3 Partially Supports; this is the S2 evidence against
    it. Folded into **T1-F2**.
- O9 [classified] (state: S2, filters and content-type tabs — NV3): **"all
  controls reachable and announced."** The filter sidebar (Price, Output,
  Size, Type, Style, Mood, Region) and the content-type tabs behave
  correctly.
  - Important for scoping: S2's failures are **specific to the template
    grid**, not general to the view. The surrounding chrome is sound.
  - Classified: NV3 / WCAG 4.1.2 / pass for these controls — no finding
- O10 [classified] (state: **P1 step 2 → 3**, selecting a template): a modal
  opens with an **`h2` carrying the template's name**, and its buttons are
  reachable. The final step of the task behaves correctly.
  - Classified: NV3/NV2 / pass — no finding. Also the evidence that the
    naming defect in O7 is an exposure failure, not missing data.
- O11 [classified] (state: whole walk — **the task-level judgement**):
  *"we can complete but it is very hard to get to the templates area and
  navigate them."* The task is **completable**, with substantial burden
  concentrated entirely at step 2.
  - Feeds the T1 verdict. See the open question recorded in 04 §A: whether
    "completable" holds when the user cannot tell the templates apart —
    i.e. whether what is completable is *"create a design from a template"*
    or only *"create a design from an arbitrary template"*.
- O12 [classified] (state: S2, NV4 — reviewer walked graphics with `G`):
  **"no graphics on the page (no next graphic) — but the grid is full of
  images."** The `G` key finds nothing, on a view whose entire content is
  template thumbnails.
  - This is the missing half of T1-F2, and it is worse than the naming
    defect alone. The thumbnail **is** the information — with no accessible
    name on the item (O7), the picture is the only thing that distinguishes
    one template from another. It is not merely unlabelled; it is **absent
    from the accessibility tree entirely**, so there is nothing to label and
    nothing to hear. A screen-reader user is given neither a name nor an
    image: the item has no perceivable identity at all.
  - Note the exact inversion between views: S1 announces *too much* about
    images ("Unlabeled Graphic" on every card, V-F7 / 1.1.1), while S2
    announces *nothing at all* about images that carry real information.
    Opposite failures of the same criterion.
  - Classified: NV4 / WCAG 1.1.1 / Major → folded into **T1-F2** as its
    sixth defect; 1.1.1 added to that finding's criteria.
- O13 [classified] (state: S2, NV6 — reviewer): the template **search field
  is labelled and reachable**. Three separate behaviours follow from
  searching, and they are not all bad:
  (a) **auto-loaded results do not announce** on arrival — no count, no
      "results updated" — confirming O8 and the 4.1.3 failure;
  (b) results **can be arrowed into and *are* announced** once there;
  (c) **activating a result does not announce the new page load.**
  - (b) **DISCREPANCY RESOLVED — no conflict (reviewer, same session):**
    *"I mean from the search area, a new results list opens below — not the
    same as the templates grid."* Two distinct components:
    - the **search results list** that opens below the search field —
      arrowable, and its items **are announced**;
    - the **`x-masonry` template grid** — arrowing is **silent** (O5).
    So O5 stands unqualified, and T1-F2's "silent arrow navigation" applies
    squarely to the grid.
  - **This is the most useful thing in the run for the report, and it makes
    the finding much harder to dismiss.** The same product, on the same
    view, contains a list that a screen-reader user *can* arrow through and
    hear — so the correct pattern is already implemented feet away from the
    broken one. The template grid's silence is therefore not a platform
    limitation, not a web-components constraint, and not an
    NVDA quirk: it is a defect in one component, with a working reference
    implementation in the same view. Combined with the root cause in R011 O1
    (`role="row"` with no grid parent), the fix is both identified and
    demonstrably achievable.
  - Recorded as a **positive result** for the search results list: items
    named, arrow navigation announced. No finding against it.
  - (c) is the **same defect as T1-F1** — a navigation occurring with no
    announcement — now observed at a second, unrelated transition. That
    makes it a product-wide pattern rather than a quirk of the rail
    navigation, and it strengthens V-F8 (title never changes) as the
    systemic cause.
  - Classified: NV6 / WCAG 3.3.2 / partial — labelling passes, no error
    path exists on S2 to exercise the second half of the check.

## Notes

**Result: Works with issues — settled by reviewer decision 2026-08-06.**
Six of nine checks fail (NV1, NV2, NV3, NV5, NV7, NV8), all sized Major, so
no Blocker is present and the run is not Broken.

The alternative was considered explicitly and rejected, and the reasoning is
kept because the report will need it. modality-checks.md §Result semantics
defines **Broken** as *"the view cannot be meaningfully used in this
modality"*, and adds that *"a Broken cell on a view used by an essential
task forces that task's verdict to Fail for the affected user group."* S2 is
step 2 of P1, which implements F1 — the product's core purpose — so sizing
T1-F2 as a Blocker would have forced **T1 = Fail** for no-vision users. The
case for that was real: S2 exists to let a user choose a template, and a
user who cannot tell templates apart is picking arbitrarily rather than
choosing.

**Reviewer's decision: Major, not Blocker** — consistent with the walk's own
outcome, *"we can complete, but it is very hard to get to the templates area
and navigate them."* The task is therefore **Pass with barriers**, and the
barriers are documented rather than fatal. Recorded as a decision, not a
default: a later reviewer reading this file can see that Fail was available
on the same evidence and was not taken.

**Dual-purpose run — the first task walk in this review.** It serves both
§B (S2's no-vision view sweep, NV1–NV9) and §A (task T1 / process P1, the
step 1 → step 2 transition and the step-2 template choice). Task-level
observations feed the T1 cluster in 04 §A; view-level ones stay here.

NVDA capture conventions: exact wording from the **Speech Viewer**
(`NVDA+N` → Tools → Speech Viewer), enabled before testing. Do **not** press
`Insert+Space` — in NVDA that toggles browse/focus mode rather than
recalling speech history.

**Three known findings sit directly on this path — watch whether they
compound rather than just recur:**

- **V-F8 (2.4.2)** — the title never changes between views. The step 1 → 2
  navigation is exactly where a user needs to know they have arrived
  somewhere new. Confirmed statically (4 views, 1 title); what is untested
  is the *lived* effect during a task.
- **V-F5 (2.4.6)** — ten identical "Browse templates" buttons. These were
  found in the S1 "Get started" modal; step 2 is the template-choosing
  step, so check whether the same pattern recurs in Explore itself.
- **V-F3 (2.4.1)** — no skip mechanism ahead of the Adobe app bar. On a
  single view this is one annoyance; across a three-step process it repeats
  at every step. **Whether that repetition is what turns T1 from "Pass with
  barriers" into "Fail" is a task-level judgement that no view sweep can
  make** — it is the main reason this walk matters.

Vendor claims in play for S2/no-vision (from `review.py next`): 1.1.1, 1.3.1,
1.3.2, 2.4.2, 2.5.3, 3.1.1, 3.3.1, 3.3.2, 4.1.3 all Partially Supports;
4.1.2 and 2.4.6 Does Not Support.

## Evidence files in this folder

- (screenshots/exports named R013-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
