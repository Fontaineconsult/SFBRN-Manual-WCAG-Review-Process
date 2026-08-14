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
