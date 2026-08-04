---
name: content-site
description: Informational / marketing / documentation website — navigation, articles, search, media, forms
---

## Step 2 — Explore the target product

Seeded from the content-site archetype. Every row is a hypothesis: confirm it
exists, correct the details, delete what doesn't apply, and add what
exploration reveals.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Home | |
| C2 | Section / topic landing pages | |
| C3 | Article / content detail | |
| C4 | Search results | |
| C5 | Contact | |
| C6 | Footer pages (legal, privacy, sitemap) | |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a visitor, I need to find information via the navigation, so that I can reach the content I need. | Core purpose |
| F2 | As a visitor, I need to find information via search, so that I can reach content directly. | Core purpose |
| F3 | As a visitor, I need to read/consume an article including its media, so that I get the information. | Core purpose |
| F4 | As a visitor, I need to submit the contact (or key) form, so that I can act on the information. | Primary conversion |
| F5 | As a visitor, I need to download and use provided documents, so that I can access offline content. | Common content type |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Article layouts | Headings, images, tables, long-form text | Content pages |
| Media | Video/audio players, captions, transcripts | Media-rich pages |
| Documents | PDFs and other downloads | Resource pages |
| Interactive components | Carousels, accordions, tab panels, mega-menus | Home, landing pages |
| Forms | Contact, newsletter, event registration | Contact |
| Embedded third-party | Maps, social feeds, chat widgets | Contact, home |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript | |
| Embedded media players | Which player? Captions/audio description support |
| PDF | Check tagged PDF |
| CMS | Identify which — affects consistency |
| Third-party embeds | Maps, chat, analytics overlays |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | |
| A2 | Contact / support | |
| A3 | Sitemap | |
| A4 | Language versions (if any) | |

## Process skeletons

#### Process P1 — Find content via navigation — implements F1

**User story:** (copy from F1)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Home | Open the main navigation, choose a section |
| 2 | Section landing | Choose an article |
| 3 | Article | Content readable, media accessible |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | 1 | Use search instead (F2) | 3 |

#### Process P2 — Submit the key form — implements F4

**User story:** (copy from F4)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Contact/form page | Complete all fields, submit |
| 2 | Confirmation | Success feedback perceivable |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P2-a | 1 | Error path: invalid/missing input, correct it | 2 |
