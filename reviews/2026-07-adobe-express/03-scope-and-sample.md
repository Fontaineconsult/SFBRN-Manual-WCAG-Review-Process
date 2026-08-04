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
| Product boundary | (e.g., all content on https://product.example.edu) |
| Easily missed inclusions | (subdomains, mobile/language versions, admin areas, embedded shops) |
| Third-party content / services | |
| Exclusions and justification | (exclusions risk conflicting with WCAG full-page and complete-process conformance — record the reason for any) |

### 1.2 Conformance target

WCAG 2.2 Level AA. Optionally note higher-level (AAA) criteria observed as
advisory findings.

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
| JAWS (Freedom Scientific) | Screen reader — manual testing | (record before first run) | Walk task sequences and inspect views as a screen reader user | Action/announced/expected notes, speech history excerpts, screenshots |
| WAVE (WebAIM) browser extension | Automated checker | (record before first run) | Sweep every sampled view and state | Summary counts, error list, annotated screenshots |

## Step 2 — Explore the target product

Seeded from the creative-authoring-tool archetype. Every row is a hypothesis:
confirm it exists, correct the details, delete what doesn't apply, and add
what exploration reveals.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Landing / marketing page (signed out) | |
| C2 | Sign up / sign in | |
| C3 | Home dashboard (recent files, create button) — confirmed: all entry points into creating new projects | https://new.express.adobe.com/ |
| C4 | Template gallery / browse | |
| C5 | Editor (canvas, toolbars, panels) | |
| C6 | Account / settings | |
| C7 | Help / support | |

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

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Canvas editor | Custom-drawn editing surface with toolbars, side panels, context menus | Editor |
| Gallery grid | Card grids, often infinite scroll, hover-revealed actions | Templates, dashboard |
| Modal dialogs | Export, share, upload, confirmation dialogs | Editor, dashboard |
| Forms | Auth, account, payment/upgrade forms | Sign up, settings |
| Marketing pages | Content-style pages with media | Landing |
| Transient UI | Toasts, tooltips, progress indicators, autosave notices | Everywhere |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript | |
| WAI-ARIA | Heavy use expected in custom widgets |
| Canvas / WebGL rendering | Major risk area: canvas content is invisible to AT unless mirrored in the accessibility tree |
| Drag and drop | Check keyboard alternatives (2.5.7) |
| File upload / download | |
| Embedded media players | If video/animation features exist |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | |
| A2 | Keyboard shortcuts reference / panel | |
| A3 | Help center / documentation | |
| A4 | Authentication (sign in, password reset, MFA) | |
| A5 | Personal data / privacy settings | |
| A6 | Payment / plan upgrade | |

## Step 3 — Select the representative sample set

If feasible (few views, or a document), evaluate the entire product and skip
sampling — record that decision here.

### 3.1 Structured sample set

Must reflect **all** of: common views (2.1), essential functionality (2.2),
sample types (2.3), technologies relied upon (2.4), and other relevant samples
(2.5). One sample may represent several of these — record what it represents.

| ID | View / screen | Location / path | Represents (C/F/type/tech/A refs) |
|----|---------------|-----------------|-----------------------------------|
| S1 | Home dashboard | https://new.express.adobe.com/ | C3; entry points for F1 (create from template/blank); start of P1 |

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
