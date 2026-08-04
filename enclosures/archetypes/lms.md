---
name: lms
description: Learning management system / courseware — courses, assignments, quizzes, grades, discussions
---

## Step 2 — Explore the target product

Seeded from the LMS archetype. Every row is a hypothesis: confirm it exists,
correct the details, delete what doesn't apply, and add what exploration
reveals. Test both student and instructor roles.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Sign in (often campus SSO) | |
| C2 | Dashboard / course list | |
| C3 | Course home | |
| C4 | Module / content page | |
| C5 | Assignment view + submission | |
| C6 | Quiz / exam | |
| C7 | Grades | |
| C8 | Discussion board | |
| C9 | Calendar / notifications | |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a student, I need to access course content including embedded media, so that I can learn the material. | Core purpose |
| F2 | As a student, I need to submit an assignment (incl. file upload), so that my work is graded. | High stakes |
| F3 | As a student, I need to take a quiz/exam — including with extended time accommodations, so that I can demonstrate learning. | High stakes; timing = 2.2.1 |
| F4 | As a student, I need to check my grades and feedback, so that I know my standing. | Core workflow |
| F5 | As a student, I need to participate in discussions, so that I can complete participation requirements. | Core workflow |
| F6 | As an instructor, I need to create/upload content and grade submissions, so that the course runs. | Staff-facing side |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Content pages | Instructor-authored rich text, embedded media, files | Modules |
| Timed interactions | Quiz timers, autosubmit, warnings | Quizzes |
| Rich text editors | Student/instructor input surfaces | Discussions, assignments |
| File upload | Submission flows | Assignments |
| Data tables | Gradebook, rosters | Grades |
| Threaded discussions | Nested replies, live updates | Discussion board |
| Modals & notifications | Due-date alerts, confirmations | Everywhere |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript / WAI-ARIA | |
| Rich text editor | Which one? Major interaction surface |
| Embedded media players | Captions / audio description support |
| PDF and office documents | Instructor-uploaded content |
| LTI / iframe embeds | Third-party tools inside courses |
| SSO (SAML/CAS) | Campus identity flow is part of scope |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | |
| A2 | Help / student support | |
| A3 | Authentication via SSO | |
| A4 | Accommodation settings (extra time, etc.) | |
| A5 | Notification preferences | |

## Process skeletons

#### Process P1 — Access course content — implements F1

**User story:** (copy from F1)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Sign in / SSO | Authenticate |
| 2 | Dashboard | Open a course |
| 3 | Course home | Open a module |
| 4 | Content page | Consume content incl. embedded media |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | 4 | Open an embedded PDF / document | 4 |

#### Process P2 — Submit an assignment — implements F2

**User story:** (copy from F2)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Course home | Open assignment |
| 2 | Assignment view | Start submission |
| 3 | Submission form | Upload file / enter text, submit |
| 4 | Confirmation | Success feedback perceivable and recorded |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P2-a | 3 | Error path: wrong file type / size, recover | 4 |

#### Process P3 — Take a quiz — implements F3

**User story:** (copy from F3)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | Course home | Open quiz |
| 2 | Quiz instructions | Start quiz |
| 3 | Question views | Answer each question type |
| 4 | Review/submit | Submit |
| 5 | Confirmation / results | Feedback perceivable |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P3-a | 3 | Timer warning appears — adjustable/extendable? (2.2.1) | 3 |
| P3-b | 2 | Extended-time accommodation applied | 3 |
