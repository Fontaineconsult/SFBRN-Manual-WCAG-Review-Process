# Scope & Sample — Adobe Express

WCAG-EM 2.0 steps 1–3 (see `ontology/wcag-em.md`). Work through the sections in
order; WCAG-EM allows returning to an earlier step as exploration or testing
reveals new information.

> Seeded from enclosure `creative-authoring-tool` (Web-based creative/design authoring tools (e.g., Adobe Express, Canva, Figma) — canvas editor, template gallery, export/share). Rows in Step 2 and the
> process skeletons are hypotheses — confirm, correct, or delete them
> during exploration.

## Step 1 — Define the evaluation scope

### 1.1 Scope of the product (principle of product enclosure)

The scope must enclose the **full product**: all views, states, and
functionality, without excluding specific parts. Define the boundary
unambiguously (URL patterns, app areas, screen lists) so that for any view it
is clear whether it is in scope.

| Field | Value |
|-------|-------|
| Product boundary | All authenticated app content at https://new.express.adobe.com/ — Home, Explore/Templates, Your stuff (`/your-stuff/…`), Brands (`/brands`), Schedule, Learn, Add-ons, and the editor (`/new?…` for new docs, `/id/urn:aaid:sc:…` for existing docs). Note: several views are SPA-routed without a distinct URL (e.g., Explore stays at `/`), so the boundary is defined by app surface, not URL alone. (proposed 2026-08-04 — confirm) |
| Easily missed inclusions | "Get started" modal (create-flow chooser); in-app account menu (Notifications, Settings, Generative AI credits, Legal notices); sign-in/SSO flow (Adobe IMS — SFSU enterprise account); Learn content; Add-ons marketplace; Schedule (social-post scheduler); keyboard-shortcuts reference if present |
| Third-party content / services | Adobe app-switcher bar (links out to Firefly, Photoshop, Lightroom, Acrobat, Fonts, Stock); "Manage account" → external account.adobe.com; template/stock content from Adobe Stock; SSO identity provider |
| Exclusions and justification | Proposed: other Adobe products reached via the app-switcher bar and account.adobe.com account management — separate products outside the procured ICT. The bar itself (as UI within Express pages) stays in scope. (confirm) |

### 1.2 Conformance target

**Primary: WCAG 2.1 Level AA** (50 criteria) — the compliance baseline that
binds CSU as a public entity under the revised ADA Title II rule.
**Additionally evaluated: WCAG 2.2 Level AA** (the six added criteria plus
the 4.1.1 removal) — reported alongside, since 2.2 is the current W3C
recommendation and the six additions protect motor and cognitive users.
Retargeted 2026-08-13 (was: 2.2 AA alone); all testing to date covers both
sets, so no evidence is invalidated. 4.1.1 Parsing (in 2.1, removed in 2.2)
is treated per the WCAG 2.2 erratum and ACT practice: met by modern
browsers' parsers; not separately tested. AAA criteria observed in passing
may be noted as advisory.

### 1.3 Accessibility support baseline

The minimum operating system + browser + assistive technology combinations the
product is expected to work with. Task testing (`04-task-testing.md`) runs
against these. Extend the baseline (add rows) if additional combinations are
used during evaluation.

| ID | OS | Browser | Assistive technology / input |
|----|----|---------|-----------------------------|
| B1 | Windows 11 | Chrome | JAWS |
| B2 | Windows 11 | Chrome | Keyboard only (no pointer) |
| B3 | Windows 11 | Chrome | 400% zoom / reflow |
| B4 | Windows 11 (build TBC) | Chrome 150.0.7871.187 | **NVDA 2026.1.1** — added 2026-08-06, the screen reader actually in use |

**Screen-reader baseline note (2026-08-06):** testing is being performed with
**NVDA**, not JAWS. B1 is retained rather than edited because runs already
recorded against it must keep their attribution, and because the two are not
interchangeable evidence — they differ in how they compute accessible names,
expose ARIA states, and handle shadow DOM, so "works in NVDA" does not
establish "works in JAWS" or vice versa. Open question for the reviewer:
**is JAWS in scope for this procurement at all?** If CSU/SFSU supports both,
B1 stays and its cells remain untested; if NVDA is the institutional
standard, B1 should be struck and this review's conformance statements
scoped to B4. Until answered, no-vision conclusions here are **NVDA-only**
and the report must say so.

### 1.4 Additional evaluation requirements (optional)

(e.g., report every occurrence rather than representative examples; analyze
specific user groups; involve users with disabilities.)

### 1.5 Testing tools

The declared instruments for this review — record exact versions before
testing starts. Capture conventions per tool: `ontology/testing-tools.md`.
Every test session is logged with `review.py log-test`, which records the
page/view, date, tool, and baseline, and creates the run's evidence folder.

| Tool | Type | Version used | Purpose | Output captured per run |
|------|------|--------------|---------|-------------------------|
| **NVDA (NV Access)** | Screen reader — manual testing (reviewer-driven), **baseline B4** | **2026.1.1** (recorded 2026-08-06) | Walk task sequences and inspect views as a screen reader user (no-vision) | Action/announced/expected notes, **Speech Viewer** excerpts, screenshots |
| JAWS (Freedom Scientific) | Screen reader — manual testing (reviewer-driven), baseline B1 | not in use as of 2026-08-06 — see §1.3 baseline note | Walk task sequences and inspect views as a screen reader user (no-vision) | Action/announced/expected notes, speech history excerpts, screenshots |
| axe-core via `scripts/axe_scan.py` | Automated checker — **primary sweep** (assistant-driven; shadow-DOM capable) | 4.10.3 (vendored `tools/axe/axe.min.js`) | Sweep every sampled view and state inside the authenticated session (CDP attach) | Raw `R###-axe.json` in the run folder + summary in run.md |
| WAVE (WebAIM) browser extension | Automated checker — secondary (reviewer-driven; light-DOM views only — blind on this app's shadow DOM, R007) | (record before first run) | Sweep views WAVE can parse (marketing/landing, docs) | Summary counts, error list, annotated screenshots |
| `zoom` — 400% reflow / 320 CSS px viewport + text-spacing override | Manual — low-vision (B3) | Chrome (record version) | LV checks: reflow, loss of content, text spacing, contrast, hover/focus persistence | Reflow + text-spacing screenshots, contrast measurements |
| `grayscale` — OS Color Filters (or CSS proxy on assistant-driven runs) | Manual — no-color | Windows 11 / Chrome | NC checks: nothing conveyed by color alone | Grayscale screenshots |
| `keyboard` — keyboard-only operation | Manual — motor (B2) | Chrome | MO checks: reach, operate, no traps, focus visibility/order | Focus-path notes, focus-state screenshots |
| `inspection` — structured checklist pass | Manual — no-hearing / no-speech / cognition | — | NH/NS/CO checks; N/A with justification where no relevant content | Notes |

**Browser version — recorded 2026-08-06, with a live warning.** All runs to
date (R001–R011) were executed on **Chrome 150.0.7871.187** — confirmed from
the binary's own version info and the running instance over CDP, not from
recollection. But **Chrome 151.0.7922.76 is already staged in the
Application directory** and takes effect the next time Chrome fully
restarts. Consequences to manage rather than discover later:

- The debug-profile window must not be casually restarted mid-session, or
  automated sweeps silently change instrument version between views —
  R009/R011 (150) would not be comparable with later runs (151).
- When the upgrade does land, **record it as a new version line here** and
  note the first run ID executed on it. A conformance record that says
  "Chrome 150" while half the runs were 151 is false.
- If a finding disappears after the upgrade, that is a browser-behaviour
  change, not a product fix — re-verify rather than withdrawing it.

**The upgrade landed — Chrome 151.0.7922.138, confirmed 2026-08-14** over
CDP (`/json/version`) on the debug-profile window, not from the staged
binary. It is a later build than the 151.0.7922.76 that was staged. The
version line, per the instruction above:

| Instrument version | Runs executed on it |
|---|---|
| Chrome 150.0.7871.187 | R001–R036 — every run recorded to date |
| Chrome 151.0.7922.138 | none yet; **the next run logged is the first** |

So the whole existing record is single-version and internally comparable,
and the boundary is exactly here. Two consequences for what comes next:
T2's export walk (W16) will be the first evidence gathered on 151, and any
re-measurement of an earlier result (the open contrast and focus-at-zoom
items) crosses the version boundary — note it in the run rather than
silently overwriting a 150-era number.

**Testing-profile hygiene — corrected 2026-08-14.** The dedicated profile
(`%LOCALAPPDATA%\sfbrn-a11y-chrome`) was created 2026-08-04 with four
extensions, none of which alter pages: Eye Dropper, Adobe Acrobat, Chrome
Web Store Payments, Google Docs Offline. On 2026-08-14 at 11:02, a Chrome
first-run sync prompt pulled **22 further personal extensions** into it —
including Stylus (injects CSS), SkipTo Landmarks and Landmark Navigation
(*add* skip links and landmarks), Freedom, Popup Blocker Pro, Postman
Interceptor and EditThisCookie. Folder mtimes place all 22 in that one
minute, so **no run in R001–R036 was affected** — the sweeps on 08-04,
08-06 and 08-10 predate it. The profile is now launched with
`--disable-extensions --disable-sync` (zero `chrome-extension://` targets
verified over CDP before use); nothing was uninstalled. Declared
environment for runs from here: Chrome 151.0.7922.138, extensions inert.

## Step 2 — Explore the target product

Seeded from the creative-authoring-tool archetype. Every row is a hypothesis:
confirm it exists, correct the details, delete what doesn't apply, and add
what exploration reveals.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Landing / marketing page (signed out) — hypothesis, not yet visited (session was already authenticated) | |
| C2 | Sign up / sign in — hypothesis; Adobe IMS SSO (SFSU enterprise account), not yet walked | |
| C3 | Home dashboard — **confirmed 2026-08-04**: search bar, "How would you like to start?" cards (Upload / Start new design / Edit photos / Set up brand kit / Generate presentation), Quick edits row, File formats row, Recent files strip, plus below-the-fold sections "Ways to create" and "Templates" (found via JAWS heading walk, R001 O6). Key state: "Get started" modal (create chooser: Create + Quick actions tabs, category list, size presets, Upload media) opened from "Start new design" | https://new.express.adobe.com/ |
| C4 | Template gallery / browse — **confirmed 2026-08-04** as "Explore" (left-rail Templates): content-type tabs (Templates, Photos, Videos, Design assets, Backgrounds, Text layouts, Webpage templates, Stickers), filter sidebar (Price/Output/Size/Type/Style/Mood/Region), category chips, infinite-scroll masonry grid | SPA view at `/` (no distinct URL observed) |
| C5 | Editor — **confirmed 2026-08-04**: own left rail (Search, Add content, Text, Upload, Your stuff, Brands, Templates, Styles, Add-ons), top bar (File menu, doc name, zoom, undo/redo, comments, Download, Share), template search panel ("Generate template" AI button, 20,000+ results), canvas with Edit page / Resize / Add page. New docs auto-named "Untitled - <date>" | `/new?width=…&height=…` (new); `/id/urn:aaid:sc:…` (existing docs) |
| C6 | Account / settings — **confirmed 2026-08-13**: Settings opened by the reviewer, **keyboard-reachable**; contains **no keyboard-customization options** (fed V-F15 / 2.1.4). Earlier (2026-08-04): account menu = Notifications, AI credits meter, premium notice, Settings, Install app, Legal notices, Sign out. Full account mgmt external (account.adobe.com) | account menu → Settings |
| C7 | Help / support — hypothesis; "?" icon in home top bar not yet opened | |
| C8 | Your stuff — **confirmed 2026-08-04**: tabs Files / Projects (NEW) / Libraries / Favorites, Folders, file cards grid, Create button, filter/sort/list-view toggles | `/your-stuff/files/recent?filter=express` |
| C9 | Brands — **confirmed 2026-08-04**: brand-kit setup; empty state with "Manual set up" and "Extract brand from upload (BETA)", Create brand / Browse shared brands, filter | `/brands` |
| C10 | Schedule (social-post scheduler) — **confirmed 2026-08-10** (crawl fingerprint): a **calendar surface** (`hz-calendar-slot` ×42), the heaviest non-editor view (796 shadow roots); `main` present; 2 headings; 1 unnamed grid; title still "Adobe Express" | `https://new.express.adobe.com/schedule` |
| C11 | Learn (tutorials) — **confirmed 2026-08-10**: redirects to a **video tutorial playlist** (`?playlist=playlist/express/get-started`, `x-tutorial-image` ×25). **Video content → no-hearing criteria (1.2.x) are live here**, as in the editor's asset panel; captions state unknown | `https://new.express.adobe.com/learn` |
| C12 | Add-ons (marketplace) — **confirmed 2026-08-10**: card marketplace (`hz-discover-add-on-card` ×30), **38 headings** (best-headed view in the product); 1 unnamed grid | `https://new.express.adobe.com/add-ons` |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a user, I need to create a new design from a template or blank canvas, so that I can start my work. | Core purpose |
| F2 | As a user, I need to edit content on the canvas (text, images, shapes), so that I can produce my design. | Core purpose |
| F3 | As a user, I need to upload and insert my own media, so that I can use my own assets. | Core workflow |
| F4 | As a user, I need to save, name, and find my work again, so that I can return to it. | Core workflow |
| F5 | As a user, I need to export or download the finished design, so that I can use it elsewhere. | Output of the product |
| F6 | As a user, I need to share my design or invite collaborators, so that others can view or edit it. | Collaboration |
| F7 | As a user, I need to sign up, sign in, and manage my account, so that I can access the product. | Gateway to everything |
| F8 | As a user, I need to generate content with AI (Generate presentation, Generate template, Firefly features with a credits meter), so that I can produce designs quickly. — added 2026-08-04: prominent throughout home + editor; confirm essentiality | Heavily promoted workflow |
| F9 | As a user, I need to run one-step quick actions (Remove background, Resize image, Convert to GIF, Generate QR code…), so that I can edit media without the full editor. — added 2026-08-04: home "Quick edits" row + modal "Quick actions" tab; confirm essentiality | Prominent standalone workflow |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Canvas editor | Custom-drawn editing surface with toolbars, side panels, context menus | Editor (C5) — confirmed |
| Gallery grid | Card grids, often infinite scroll, hover-revealed actions, skeleton loading placeholders | Explore (C4), editor template panel, Your stuff (C8), dashboard rows — confirmed |
| Modal dialogs | Create chooser, export, share, upload, confirmation dialogs | "Get started" modal (C3) confirmed; editor export/share expected |
| Forms | Auth, account, brand setup forms | Sign up (C2), Settings (C6), Brands manual set up (C9) |
| Marketing pages | Content-style pages with media | Landing (C1) — not yet visited |
| Transient UI | Toasts, tooltips, progress indicators, autosave notices, AI credits meter | Everywhere |
| Menus / overlays | Account menu, More flyout, scoped search bar (In:Templates / In:Files / In:Brands) | Home, all rail views — confirmed |
| Calendar / scheduler surface | Time-grid with slot cells, month/week navigation (`hz-calendar-*`) | Schedule (C10) — added 2026-08-10 from crawl; no sample yet covers this type |
| Video playlist / player | Tutorial playlists with embedded players | Learn (C11) — added 2026-08-10; no-hearing criteria live |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript | SPA; `lang="en-US"` set on html element |
| Web components / shadow DOM | **Observed 2026-08-04:** browser-extension accessibility-tree extraction returned a near-empty tree (single generic node); DOM walk shows one top-level shadow host wrapping the app. Must verify what JAWS/DevTools actually expose — high-priority recon for R001 |
| WAI-ARIA | Heavy use expected in custom widgets |
| Canvas / WebGL rendering | **Confirmed 2026-08-06, and the risk is realised.** The editor renders the document into a **single full-viewport `<canvas>`** (2328×1145) carrying **no `role`, no `aria-label`, no `aria-hidden`, and zero fallback child elements**. A text element reading "Text Test" that is plainly visible on the canvas **does not appear anywhere in the DOM** — not as text, not as an `aria-label` — across all 960 open shadow roots. The document's content therefore exists only as painted pixels. Recon, to be verified under NV3/NV4/NV5 in a run (see §2.6). |
| Drag and drop | Confirmed: "Drag and drop files" upload card on home; canvas manipulation. Check keyboard alternatives (2.5.7) |
| File upload / download | Confirmed: Upload card (home), Upload rail item (editor), Download button (editor) |
| Generative AI features | Firefly-based: Generate presentation / Generate template buttons, credits meter in account menu |
| Embedded media players | If video/animation features exist |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | |
| A2 | Keyboard shortcuts reference — **confirmed 2026-08-13** (reviewer): external help page, `https://helpx.adobe.com/express/web/get-started/keyboard-shortcuts.html`. No in-app panel found so far. Note (R031): some documented shortcuts do not work (e.g. rename) | external helpx.adobe.com |
| A3 | Help center / documentation | "?" icon in home top bar — not yet opened |
| A4 | Authentication (sign in, password reset, MFA) | Adobe IMS SSO; SFSU enterprise account — walk via sign-out/sign-in |
| A5 | Personal data / privacy settings | Settings in account menu — not yet opened |
| A6 | Payment / plan upgrade | Admin-managed on this account ("contact your admin to request access" for premium features) — upgrade flow may be absent; confirm |

### 2.6 Exploration notes (recon for testing — not yet findings)

Session 2026-08-04, signed in as fontaine@sfsu.edu (Chrome, exploration only):

- **Shadow-DOM opacity — RESOLVED 2026-08-04 (R001 O3, walkthrough W3):**
  automated extraction (accessibility tree, page text) returned essentially
  nothing, but JAWS reports real, properly-announced structure (3 headings,
  2 regions, 1 link on S1). The emptiness was a browser-extension tooling
  artifact. Consequence: extraction-based recon can under-report this app;
  AT-facing conclusions come from JAWS runs only.
- **Unlabeled link — REFUTED 2026-08-04 (R009 O7):** the Recent-file card
  link carries its name in an `sr-only` span (and the thumbnail has proper
  alt); the exploration DOM walk missed visually-hidden text. axe reports
  no violation there. Lesson: name-checks need the accessibility tree or
  axe, not raw text extraction.
- Template/asset grids load with skeleton placeholders (transient UI for
  status announcements — NV7).
- Creating a design is frictionless but silently creates a persistent
  "Untitled - <date>" doc (one now exists in Your stuff from this session —
  reusable as the P2 test document).
- Left-rail Templates (Explore) does not change the URL — **CORRECTED
  2026-08-06:** it does. The view is addressable as
  `/explore/templates?assetCollection=urn:aaid:sc:VA6C2:…` and was scanned
  directly at that URL (R011). The earlier note was written from a session
  that reached Explore by clicking the rail; S2 is replicable by URL.

**Exploration session 2026-08-06 — S3 Editor and S4 Your stuff (assistant
driving, per `assisted-exploration.md`). Mapping only; nothing here is a
finding until a run verifies it.**

- **Canvas exposure — the headline recon item.** The editor paints the whole
  document into one `<canvas>` (2328×1145) with **no `role`, no
  `aria-label`, no fallback children, and no `aria-hidden`**. The visible
  text element "Text Test" is **absent from the DOM entirely** across 960
  open shadow roots. → *Verify under **NV3, NV4 and NV5** in the S3
  no-vision run: with a screen reader, can the user perceive that the
  document contains a text object, read its content, select it, or know
  where it sits on the page?* If confirmed, this is the most serious defect
  available in the product, because it makes the **document itself** —
  not a control around it — imperceptible. Note it would also bear directly
  on task **P2** (edit and export), every step of which operates on canvas
  content.
- **No `main` landmark in the editor.** Landmarks found: `form`, `header`,
  `sp-action-group[toolbar]`, `sp-button-group[region]`. S1 exposed
  `main` plus four others, and that `main` is the entire basis for V-F3's
  amendment narrowing 2.4.1 to keyboard-only users (ARIA11 bypass).
  → *Verify under **NV2/MO11** in the S3 runs: if the editor has no `main`,
  the landmark-bypass argument does not transfer here, and 2.4.1 may be
  worse on S3 than the S1 evidence suggests.* Do not assume S1's finding
  scope applies to this view.
- **Editor headings** (11+): `h2` "Untitled…", `h2` "Daniel Fontaine",
  `h2` "Canvas", `h2` "Search", then `h3` per search-panel section
  (Templates, Photos, Design assets, Icons, Shapes, Stickers, Backgrounds,
  Videos, Music, Sound effects, Charts). **No `h1`.** A heading named
  "Canvas" exists, so the region is at least announceable even if its
  contents are not. → *Verify under NV2.*
- **S3's no-hearing cell will NOT be N/A** — unlike S1 and S2. The editor's
  asset panel offers **Videos, Music and Sound effects**, so captions,
  transcripts and audio alternatives (NH1–NH4 / 1.2.x) become live
  criteria for the first time in this review. Plan a real no-hearing run
  for S3 rather than reusing S1's N/A.
- **Editor scale:** 3,971 elements across **960 open shadow roots** (S1:
  1,751 / 303). Expect axe sweeps and any DOM-walking instrument to be
  slower and heavier here.
- **The editor *does* set a document title** ("Untitled - August 06, 2026 at
  13.02.17"), confirming the V-F8 nuance: the app is capable of meaningful
  titles and simply does not set them on its non-document views.
- **S4 Your stuff (visited in passing):** tabs Files / Projects (NEW) /
  Libraries / Favorites; "Files" heading with an add button; card grid;
  Create file; filter, sort and list-view toggles; scoped search showing an
  "In:Files" chip. Matches C8 as recorded. Three files present — see
  artifacts below.

**Systematic crawl 2026-08-10** (`scripts/crawl_map.py`, fingerprints in
`crawl-map-2026-08-10.md`): all seven candidate views visited read-only —
Home, Explore, Your stuff, Brands, **Schedule, Learn, Add-ons** (the last
three previously never opened; C10–C12 confirmed above). Cross-cutting
results: **title is "Adobe Express" on all 7 views** (V-F8 scope widened
from 4); **every grid on every view is unnamed** (V-F11 corroborated on 3
further views); every view exposes `main`. Harvest note: the left rail and
More menu are **JS-routed buttons, not links** — link harvesting cannot
discover them, so rail-reached views must be probed by URL or walked
manually. Sampling gap now visible: no sample covers the calendar type
(C10) or video playlist type (C11).

**Artifacts created by assistant-driven sessions (per CLAUDE.md browser
rules — record, don't hide):**

- 2026-08-04: one "Untitled - <date>" document, created during exploration
  and recorded as retained for P2. **CORRECTION 2026-08-06: it is gone.**
  Your stuff lists only three files and this is not among them. Either it
  was never persisted or it was removed between sessions. The S3 sample row
  pointed at it and has been re-pointed at a document that exists. Lesson
  for the enclosure: a sample locator that names "the doc from this session"
  is not replicable — record the durable ID.
- **2026-08-06, unattributed: a file named "sdcsdc"** (timestamped ~2 hrs
  before this exploration), and the "Untitled - August 06" document now
  contains a text element reading **"Text Test"** that was not placed by the
  assistant. Both are consistent with the reviewer's NVDA session having
  exercised the editor and a naming/search field, but that is **inference,
  not observation** — recorded as unattributed so the record stays honest.
  Reviewer to confirm provenance; keep or delete deliberately.
- **2026-08-06: a second document, "Untitled - August 06, 2026 at
  13.02.17"** (`/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86`,
  `taskID=instagram-portrait-post`). Created unintentionally in the
  **debug-profile** browser: a CDP `Page.navigate` to `https://new.express.
  adobe.com/` from the Explore view did not land on Home — the app resumed a
  pending template task and opened a new document instead. Two consequences
  worth carrying forward:
  1. **Instrument lesson:** navigating this SPA by URL does not guarantee
     the view you asked for. Any run must verify the landed view (title +
     URL) *before* measuring — an AX-tree capture taken on this document was
     briefly mistaken for Home and discarded.
  2. **Product observation (recon, not a finding):** a plain navigation to
     the site root silently created a persistent user artifact. Worth
     testing deliberately under CO8 (3.2.1/3.2.2 unexpected context change)
     and as a data-hygiene note — a screen reader user could land in an
     editor without having asked for one.
- **2026-08-10, reviewer-created, deliberate: the T2 test document** — a
  blank document authored by the reviewer entirely via keyboard/NVDA to
  walk task **T2** (run R016). Created and renamed without a pointer, which
  is itself a recorded positive (R016 O4). **Locator discrepancy, open:**
  the reviewer renamed it to "Test-With-Keyboard" and heard the rename
  succeed, but the Your stuff listing (read 2026-08-10) shows it as
  **"Untitled - August 10, 2026 at 13.09.20"** — see R016 O11 before
  drawing any conclusion. This is the T2 test document; keep it.

**Document registry (durable IDs, resolved 2026-08-10 from the Your stuff
listing — use these in run locators, never display names, which can drift):**

| Document (name as listed) | Durable locator (`https://new.express.adobe.com/id/<urn>`) | Role |
|---|---|---|
| Untitled - August 06, 2026 at 13.02.17 | `urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86` | **S3 sample** ("Text Test" doc) |
| Untitled - August 10, 2026 at 13.09.20 | `urn:aaid:sc:US:b1ab530f-f097-4a5f-8a6f-b8923fa65115` | **T2 test document** (R016; rename discrepancy above) |
| **Can-I-find-the-right-text** | `urn:aaid:sc:US:a767278e-deed-4656-b424-f01495fad229` | **R038 multi-object test document** — 5 objects (text 1/2/3, a shape, a photo), built 2026-08-14 for the authoring-at-scale walk that produced **T2-F4**. Also one of the five pages in the R040 WAVE sample. Resolved the day it was created |
| sdcsdc | `urn:aaid:sc:US:d0ad5936-2a17-4db7-a9e8-bb0fb8eb91a1` | unattributed (likely reviewer NVDA session 2026-08-06) |
| Kaiser Permanente Mobile App - Letter Details | `urn:aaid:sc:US:0e88a2b4-710d-4577-a664-0ef3d2dde1dc` | reviewer's real document — **do not open in tests** |

- All documents remain in Your stuff (S4). Do not delete them — deletion is
  outside assistant permissions, and they are now part of S4's tested state.
  As of 2026-08-10 the listing shows four, which makes S4 a usefully
  populated view for its own run rather than a near-empty one.
- **Rename discrepancy still unresolved as of 2026-08-14.** The T2 document
  loaded in R037 still carries the title "Untitled - August 10, 2026 at
  13.09.20", not "Test-With-Keyboard" — so the keyboard rename performed in
  R016 has still not surfaced in either the listing or the document title.
  W24 remains the open step.

**Published output — a state class this review has not sampled (added
2026-08-14, R037 O6).** The product publishes designs as **hosted webpages**
at `/publishedV2/…` share links, in addition to exporting PDF, image and
MP4 files. That surface is inside the declared product boundary (§1.1: "all
authenticated app content"), but no sample, run or sweep has ever reached
it, and the first observation of it produced **V-F16** — published pages
announce as "canvas graphic" and nothing else.

| Artifact class | Locator form | Status |
|---|---|---|
| Published page (share link) | `https://express.adobe.com/publishedV2/<id>` — **exact URL outstanding, reviewer to supply** | **Unsampled.** One observation (R037 O6 → V-F16). Needs a sample ID and its own runs if scoped in |

Two things to settle before this becomes testable, both the reviewer's:
whether published output is inside the WCAG conformance target or carried
as §504/advisory (06 §Concerns), and the durable locator — a published page
has a real, stable URL, so the replicable-locator rule is satisfiable here
and should be satisfied before V-F16 is relied on.

## Step 3 — Select the representative sample set

If feasible (few views, or a document), evaluate the entire product and skip
sampling — record that decision here.

### 3.1 Structured sample set

Must reflect **all** of: common views (2.1), essential functionality (2.2),
sample types (2.3), technologies relied upon (2.4), and other relevant samples
(2.5). One sample may represent several of these — record what it represents.

| ID | View / screen | Location / path | Represents (C/F/type/tech/A refs) |
|----|---------------|-----------------|-----------------------------------|
| S1 | Home dashboard (incl. "Get started" modal state) | https://new.express.adobe.com/ | C3; entry points for F1 (create from template/blank); start of P1; modal-dialog type |
| S2 | Explore / template gallery | `https://new.express.adobe.com/explore/templates` (CORRECTED 2026-08-10 — the 2026-08-04 note "SPA, URL stays `/`" was wrong; the view is URL-addressable and was scanned at this URL in R011/R013. Also reachable via left-rail Templates.) | C4; F1 (choose template); gallery-grid type; P1 step 2 — proposed 2026-08-04 |
| S3 | Editor ("Text Test" document) | **`https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86`** — the durable locator; use exactly this in run records. Reachable via Your stuff → "Untitled - August 06, 2026 at 13.02.17". Do **not** record the `?category=…&pageId=…` suffix seen in a live address bar: those are transient UI state (which side panel is open, which page is showing), not part of the document address. **CORRECTED 2026-08-06** — the previously-cited "blank square doc from this session" (2026-08-04) no longer exists, so the old locator was unreplicable. This document is better for testing anyway: it holds a text element reading "Text Test", so NV3/NV4/NV5 can be exercised against real document content, which a blank canvas cannot do. | C5; F2/F3/F5 (edit, upload, export); canvas + panels + export dialog; P1 step 3, all of P2 |
| S4 | Your stuff | `/your-stuff/files/recent?filter=express` | C8; F4 (save/find work); gallery-grid + folders; end of P2 verification — proposed 2026-08-04 |

Candidates not yet sampled (decide after remaining exploration): Brands (C9),
Schedule (C10), Learn (C11), Add-ons (C12), Settings/account menu (C6), Help
(C7/A3), sign-in flow (C2/A4), signed-out landing (C1).

### 3.1b Coverage baseline — what we actually tested, per enclosure area

**The audience-facing accounting** (adopted 2026-08-13 as the baseline for
the remainder of this review): every area of the enclosure, its locator,
and exactly what testing it has received. **Update this table in the same
write-back as every new run** — it is the "what did you actually do" answer
and feeds `06` §Coverage directly. Regenerate coverage facts from
`review.py matrix` / `runs`; never let this table contradict them.

| Area | Locator | Map status | Testing received | State |
|---|---|---|---|---|
| C3 = **S1 Home** (+ Get started modal) | `/` | confirmed | NVDA complete (R012); no-color (R003); axe (R009); WAVE blind (R007); low-vision reflow closed by measurement (R002 — LV5/LV7 reviewer); cognition/motor partial (R010/R004); JAWS suspended (R001) | **most-tested** |
| C4 = **S2 Explore** | `/explore/templates` | confirmed | NVDA + task T1 (R013); axe (R011); low-vision reflow (R018); no-color (R021); NH/NS N/A (R024/R025) | motor + cognition remain |
| C5 = **S3 Editor** | `/id/urn:aaid:sc:US:1fd8af9a…` | confirmed | axe (R014); NVDA sweep + task T2 in progress (R015/R016); low-vision reflow (R019 — panel-over-canvas question open); no-color chrome (R022); NS N/A (R026); **no-hearing determined (R030** — UI N/A; caption-capability findings to 06 §504) | T2 export + motor + cognition remain |
| C8 = **S4 Your stuff** | `/your-stuff/files/recent?filter=express` | confirmed | **NVDA complete (R029** — V-F12 confirmed, V-F13 new, rename discrepancy closed); axe (R017); low-vision reflow (R020); no-color (R023); NH/NS N/A (R027/R028) | motor + cognition remain |
| C9 Brands | `/brands` | confirmed | crawl fingerprint only | untested |
| C10 Schedule | `/schedule` | confirmed 08-10 | crawl fingerprint only | untested; calendar type unsampled |
| C11 Learn | `/learn` | confirmed 08-10 | crawl fingerprint only | untested; **no-hearing live here** |
| C12 Add-ons | `/add-ons` | confirmed 08-10 | crawl fingerprint only | untested |
| C6 Settings | account-menu overlay | partial | menu seen in exploration | Settings view unopened |
| C2 Sign-in (IMS) | `auth.services.adobe.com` | exists (seen 08-06) | none | **never walked — gates 3.3.8** |
| C1 Signed-out landing | — | hypothesis | none | unvisited |
| C7 Help | header "?" | hypothesis | none | unopened |

### 3.2 Randomly selected sample set

Size: **10% of the structured sample set**, selected randomly from in-scope
views not already sampled. Record the selection method (crawler, full listing,
server logs…) so the selection is replicable. These are compared against the
structured set in `04-task-testing.md` §C.

| ID | View / screen | Location / path |
|----|---------------|-----------------|
| R1 | | |

**Selection method:**

### 3.3 Complete processes — task sequences

Expand each essential-functionality user story (2.2) into a process. Record
the **default sequence** (standard use case: no input errors, no optional
branches) and the **critical branch sequences** (commonly used or critical
alternatives; a branch ends where it re-enters the default sequence). Every
view in a sequence must be in the sample set. Record the action needed to move
from each step to the next so any evaluator can replicate the run.

#### Process P1 — Create a design from a template — implements F1

**User story:** (copy from F1)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Home dashboard | Activate "Create" / template search |
| 2 | Template gallery | Select a template |
| 3 | Editor | Template opens on canvas |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | 2 | Start from blank canvas instead | 3 |

#### Process P2 — Edit and export a design — implements F2, F5

**User story:** (copy from F2/F5)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Editor | Select a text element, edit text |
| 2 | Editor | Insert an image from the asset panel |
| 3 | Editor | Activate "Download/Export" |
| 4 | Export dialog | Choose format, confirm |
| 5 | (download delivered) | Verify completion feedback |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P2-a | 2 | Upload own media, then insert | 3 |

#### Process P3 — Sign up and sign in — implements F7

**User story:** (copy from F7)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Sign up | Complete form / SSO, submit |
| 2 | Verification (email/MFA) | Complete verification |
| 3 | Home dashboard | Arrival state announced/focused correctly |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P3-a | 1 | Error path: submit with invalid input, recover | 2 |
| P3-b | 1 | Password reset flow | 3 |
