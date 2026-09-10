# Assisted Exploration (WCAG-EM Step 2 with a browser-driving assistant)

How the assistant explores the product with browser automation (Claude in
Chrome) during WCAG-EM step 2, and writes what it finds back into the review's
`03-scope-and-sample.md`. First used in `2026-07-adobe-express` (2026-08-04).

**Division of labor.** In the testing loop (`testing-loop.md`) the *reviewer*
drives the product and the assistant structures. In exploration the roles can
flip: the assistant drives the browser to map views, while the reviewer
watches, answers scope questions, and confirms or rejects what gets written
into the enclosure. Exploration is mapping, not testing — no run is logged,
no check outcomes are recorded, and nothing observed here becomes a finding
until a real run verifies it.

## Preconditions

- The review is seeded from an enclosure; Step 2 tables hold hypotheses.
- The reviewer is signed in, in their own Chrome session, with the test
  account the review will use. The assistant never performs authentication,
  account creation, purchases, permanent deletions, or form submissions —
  those stay with the reviewer (walk C2/auth views together).
- Know that exploration can have side effects (e.g., creating a document via
  the create flow). Record any artifact created; reuse it as a test document
  or delete it deliberately.

## The pass

1. **Open the product root.** Screenshot; identify the primary navigation and
   the on-page entry points. Compare against the enclosure's hypothesized
   common views (C rows).
2. **Probe machine extraction once per app shell.** Try the accessibility-tree
   read, page-text extraction, and element find; then a JS DOM walk that
   pierces open shadow roots (collect links, labels, landmark structure).
   Dual purpose: harvest URLs/labels for the map, and record *how much the
   app exposes to automated extraction*. **Caveat:** the extension's view is
   not the AT view — an empty extraction tree is recon to verify with
   JAWS/DevTools in a run, never a finding by itself.
3. **Walk the primary navigation.** Batch click → wait → screenshot per nav
   item; capture each view's URL (or note that the SPA keeps the URL —
   replication steps for such views must describe UI actions, not URLs).
4. **Enter the core working surface** (editor, player, reader…) through the
   product's own create/open flow — this usually walks a process (P) branch
   for free and reveals the surface's own navigation, panels, and top bar.
5. **Open the overlays:** account menu, help, notification, "more" menus,
   create-flow modals. These reveal settings views, plan/licensing state,
   AI features, and scope-boundary edges (external account sites, sibling
   products).
6. **Write back immediately** (same session), in the review's
   `03-scope-and-sample.md`:
   - §1.1 boundary: propose product boundary, easily missed inclusions,
     third-party services, exclusions — marked `(proposed — confirm)`.
   - §2.1 common views: confirm/correct/delete hypothesis rows **in place**,
     keeping IDs stable; append new views as new C rows. Every confirmed row
     carries `confirmed <date>` and what was seen; unvisited rows stay
     explicitly marked as hypotheses.
   - §2.2 functionality: append newly observed candidate-essential
     functionality as new F rows, flagged for the reviewer to confirm
     essentiality.
   - §2.3 sample types / §2.4 technologies: confirm with example views;
     add observed technologies (shadow DOM, canvas, drag-drop, AI features).
   - §2.5 other samples: fill locations found (help icon, settings, auth).
   - §2.6 exploration notes: dated recon list — extraction results, suspected
     issues (each tied to the check it should be verified under, e.g. NV3),
     artifacts created, replication quirks.
   - §3.1: propose new S rows for confirmed views, marked `proposed <date>`.
7. **Reflect.** `review.py matrix` / `next` re-read the S table, so the
   coverage grid widens the moment the write-back lands. Report to the
   reviewer: views confirmed, views still unexplored, boundary questions
   awaiting their decision.

## Systematic mapping with `scripts/crawl_map.py` (added 2026-08-10)

The manual pass above stays the method; the crawler makes steps 2–3
systematic and repeatable:

1. **`harvest URL…`** — collect same-origin link targets from rendered
   pages (shadow-piercing). This is the *candidate* map. **Limits:** JS-
   routed navigation (rail buttons, menus) is invisible to harvesting —
   Adobe Express's entire left rail is — so harvest output is a floor, and
   menu-reached views must be probed by URL guess or walked manually.
2. **A human/agent promotes candidates to an allowlist.** Never auto-follow
   discovered links: on authenticated products a "link" can be an action
   (this product silently *creates a document* on some navigations). The
   script refuses action-shaped paths (`/new`, delete, checkout…) and
   document URLs by default, and reports any navigation that bounced
   instead of fingerprinting the wrong view.
3. **`map URL… [--out FILE]`** — fingerprint each allowlisted view: title,
   lang, landmarks (+`main` present?), heading outline, named/unnamed grid
   counts, unnamed controls, canvases, iframes, shadow-root count, custom-
   element histogram. The fingerprint is **enclosure content**: it fills
   §2.1 rows (confirmed, dated), reveals sample *types* (§2.3 — a calendar
   component histogram is how Schedule's type was caught), flags per-view
   risk before any run (no `main`, canvas present, grid counts), and shows
   product-wide patterns across views in one table.
4. **Write-back stays curated.** Crawl output is recon; work it into `03`
   by hand per the conventions below, keep the raw map file
   (`crawl-map-<date>.md`) beside the review, and never log runs or
   findings from it.

## Probing without the browser extension — `scripts/cdp_probe.py` (added 2026-09-10)

The pass above was written for Claude-in-Chrome. When only the debug-profile
Chrome is available (the axe setup in testing-tools.md), the same steps run
over CDP with two scripts: `crawl_map.py` for harvest/fingerprint, and
`cdp_probe.py` for everything the pass needs per view — frames, visible text,
visible controls, an accessibility-tree summary (role histogram + unnamed
controls, from `Accessibility.getFullAXTree`), an optional role/name dump,
a screenshot, an arbitrary `--js` expression, and a real key chord
(`--key 5 --ctrl --shift`) dispatched through `Input.dispatchKeyEvent`.
The AX summary is the instrument that matters: it is what the AT is given
(CLAUDE.md instrument hierarchy), so "6 unnamed radios" there is recon worth
a JAWS run, while a DOM-only check is not.

Lessons from `2026-09-the-expert-ta` (2026-09-10):

- **Harvest is a floor on WebForms apps too.** Root harvest found 9 links;
  the real navigation was DevExpress combo boxes and a row click-menu. Dump
  hidden menu items and `<select>` options (`--js` over `option`/`li`/
  listbox cells, visible or not) before walking — an app's own "accessibility
  mode" variant exposed every action URL as `<option value>`s.
- **Look for a mode toggle.** A button such as "Accessibility Page" can
  switch a view to a parallel version *and persist that per account*. Map
  both versions, restore the account to the state you found it in, and make
  every later run record which mode was active.
- **Never submit to inventory.** Question types, keypads, drag-and-drop and
  drawing widgets were inventoried by switching problems and reading
  `.sr-only` instruction text, live-region content and control counts — no
  answer submitted, no attempt consumed on the shared account.
- **Read the vendor's own scripts.** `fetch()` of the page's accessibility
  JS (same origin) listed every shortcut and announcement string in one
  call; a real key dispatch then confirmed the live-region output.
- Screenshots and the probe scripts' JSON go to the scratchpad; only the
  curated `crawl-map-<date>.md` stays beside the review.
- **One product tab, always.** The CDP client attaches to the tab already on
  the product (`--tab`, or the URL's host); it refuses to navigate a blank
  tab to the product. Expert TA invalidates the session the moment a second
  tab on its host appears (`/WSInvalidAccess.aspx`, "Multiple Session
  Instances") — that cost two session drops on 2026-09-10 before the cause
  was pinned. Recovery: close the duplicate, reload the original tab.

## Conventions

- Every statement written into Step 2 is either **confirmed (dated)** or an
  explicit **hypothesis** — never silently mixed.
- Recon observations live in §2.6 only, phrased as "verify X under check Y in
  a run", so `validate` stays honest and findings only ever cite runs.
- The assistant asks before anything side-effectful beyond navigation
  (submitting forms, accepting dialogs, anything in the testing-loop's
  reviewer lane).
- Screenshots taken during exploration are disposable working context; only
  run folders (`evidence/runs/R###/`) hold evidence files.

## Why bother recording extraction results

The step-2 extraction probe is cheap and pays twice: it maps the app, and it
gives an early signal on programmatic exposure (shadow DOM opacity, unlabeled
controls, missing landmarks) that shapes which view×modality cells the
reviewer should test first — exactly the prioritization `review.py next`
feeds on once vendor claims and the sample are in place.
