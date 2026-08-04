---
name: creative-authoring-tool
description: Web-based creative/design authoring tools (e.g., Adobe Express, Canva, Figma) — canvas editor, template gallery, export/share
---

## Step 2 — Explore the target product

Seeded from the creative-authoring-tool archetype. Every row is a hypothesis:
confirm it exists, correct the details, delete what doesn't apply, and add
what exploration reveals.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Landing / marketing page (signed out) | |
| C2 | Sign up / sign in | |
| C3 | Home dashboard (recent files, create button) | |
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

## Process skeletons

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
