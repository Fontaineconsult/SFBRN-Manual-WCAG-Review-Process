---
name: web-app
description: Generic SaaS / line-of-business web application — auth, dashboard, records, forms, settings
---

## Step 2 — Explore the target product

Seeded from the web-app archetype. Every row is a hypothesis: confirm it
exists, correct the details, delete what doesn't apply, and add what
exploration reveals.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Sign in / SSO | |
| C2 | Dashboard / home | |
| C3 | Primary list view (records, items) | |
| C4 | Record detail view | |
| C5 | Create / edit form | |
| C6 | Search results | |
| C7 | Settings / profile | |
| C8 | Notifications | |
| C9 | Help / support | |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a user, I need to sign in (incl. SSO), so that I can access the application. | Gateway |
| F2 | As a user, I need to find a record via search or browse, so that I can work with it. | Core workflow |
| F3 | As a user, I need to create a new record, so that I can do my job. | Core workflow |
| F4 | As a user, I need to edit and save an existing record, so that data stays current. | Core workflow |
| F5 | As a user, I need to complete the product's primary end-to-end workflow, so that its purpose is fulfilled. | Core purpose — name it during exploration |
| F6 | As a user, I need to adjust settings / manage my profile, so that the product works for me. | Configuration |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Data tables | Sort, filter, paginate, row actions | List views |
| Forms | Multi-field, validation, required fields, date pickers | Create/edit |
| Modal dialogs | Confirmations, quick-create, detail overlays | Everywhere |
| Wizards | Multi-step flows with progress indication | Onboarding, setup |
| Dashboards | Cards, charts, stats | Home |
| Transient UI | Toasts, inline validation, loading states, empty states, error pages | Everywhere |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript | |
| WAI-ARIA | SPA frameworks: check focus management on route changes (4.1.3, 2.4.3) |
| SPA framework | Identify which (React/Angular/Vue…) |
| File upload / download | |
| Charts / data visualization | Check text alternatives |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | |
| A2 | Help / documentation | |
| A3 | Authentication (sign in, reset, MFA) | |
| A4 | Personal data / privacy settings | |
| A5 | Keyboard shortcuts reference | |

## Process skeletons

#### Process P1 — Sign in and reach the dashboard — implements F1

**User story:** (copy from F1)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Sign in | Enter credentials / SSO, submit |
| 2 | (MFA if present) | Complete challenge |
| 3 | Dashboard | Arrival state announced/focused correctly |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | 1 | Error path: invalid credentials, recover | 3 |
| P1-b | 1 | Password reset flow | 3 |

#### Process P2 — Find, open, and edit a record — implements F2, F4

**User story:** (copy from F2/F4)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Dashboard | Use search or navigate to list |
| 2 | List / search results | Open a record |
| 3 | Record detail | Activate edit |
| 4 | Edit form | Change a field, save |
| 5 | Record detail | Confirmation feedback perceivable |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P2-a | 4 | Error path: invalid input, correct it | 5 |

#### Process P3 — Primary end-to-end workflow — implements F5

**User story:** (name the product's actual core workflow during exploration)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | | |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P3-a | | | |
