# Scope & Sample — Essentials AI Learn

WCAG-EM 2.0 steps 1–3 (see `ontology/wcag-em.md`). Work through the sections in
order; WCAG-EM allows returning to an earlier step as exploration or testing
reveals new information.

> Seeded from enclosure `lms` (Learning management system / courseware — courses, assignments, quizzes, grades, discussions). Rows in Step 2 and the
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
| Product boundary | (proposed 2026-09-30 — confirm) Everything served at `https://learn.essentials-ai.com/` to a learner account: sign-in and password reset, My Courses, the course player and every lesson state inside it, My Certificates, My Profile, the account menu. |
| Easily missed inclusions | (proposed 2026-09-30 — confirm) **Lesson content is not served by the product host:** article lessons are cross-origin iframes from `https://mnowak-ai.github.io/ai-academics-articles/` (GitHub Pages) and videos are MP4 files on `https://mhgwkfdzuklcjykcirhx.supabase.co/…/course-media/`. Both are the vendor's own authored content and are **in scope** (the learner cannot complete the course without them). The Gamified course experience (a per-account toggle on My Courses) — same player and URL for this course; what it changes is unknown (ask vendor). The earned-certificate state of My Certificates (view/PDF/verification link) — not reachable until a course is completed. |
| Third-party content / services | (proposed 2026-09-30 — confirm) Google Fonts inside the article iframes. The vendor ACR says simulation activities send learners to ChatGPT / Claude / Copilot — **no such activity exists in the provisioned course**; if other courses are provisioned later, those tools stay out of scope but the in-course alternative the ACR promises is in scope. |
| Exclusions and justification | (proposed 2026-09-30 — confirm) Administrator / instructor tooling — not provisioned to the test account and excluded by the vendor ACR; the marketing site `essentials-ai.com` — not part of the purchased product. |

### 1.2 Conformance target

**Primary: WCAG 2.1 Level AA** — the ADA Title II baseline binding CSU as a
public entity. **Additionally evaluated: WCAG 2.2 Level AA** (the six added
criteria; 4.1.1 treated as met per the WCAG 2.2 erratum). Optionally note
higher-level (AAA) criteria observed as
advisory findings.

### 1.3 Accessibility support baseline

The minimum operating system + browser + assistive technology combinations the
product is expected to work with. Task testing (`04-task-testing.md`) runs
against these. Extend the baseline (add rows) if additional combinations are
used during evaluation.

| ID | OS | Browser | Assistive technology / input |
|----|----|---------|-----------------------------|
| B1 | Windows 11 | Chrome | JAWS (installed; not the instrument in use — see B5) |
| B2 | (any) | (any) | Keyboard only (no pointer) |
| B3 | (any) | (any) | 400% zoom / reflow |
| B4 | macOS | Safari | VoiceOver (optional) |
| B5 | Windows 11 | Chrome | **NVDA 2024.1** — stated by the reviewer 2026-09-30 as the screen reader for this review's no-vision runs (version recorded 2026-09-30, W1). The vendor ACR says its testing covered VoiceOver and NVDA; NVDA verifies that claim. |

### 1.4 Additional evaluation requirements (optional)

(e.g., report every occurrence rather than representative examples; analyze
specific user groups; involve users with disabilities.)

### 1.5 Testing tools

The declared instruments for this review — versions recorded before testing
starts, updated if they change. Capture conventions per tool:
`ontology/testing-tools.md`. Every test session is logged with
`review.py log-test`, which records the page/view, date, tool, and baseline,
and creates the run's evidence folder.

| Tool | Type | Version used | Purpose | Output captured per run |
|------|------|--------------|---------|-------------------------|
| JAWS (Freedom Scientific) | Screen reader — manual testing | | Walk task sequences and inspect views as a screen reader user | Action/announced/expected notes, speech history excerpts, screenshots |
| NVDA (NV Access) | Screen reader — manual testing (the instrument in use, B5) | NVDA 2024.1 (recorded 2026-09-30) — Chrome / Windows build strings still to record | Walk task sequences and inspect views as a screen reader user | Action/announced/expected notes, speech viewer excerpts, screenshots |
| WAVE (WebAIM) browser extension | Automated checker | | Sweep every sampled view and state | Summary counts, error list, annotated screenshots |
| axe-core (`scripts/axe_scan.py`, CDP) | Automated checker — assistant-run | axe-core 4.10.3 (vendored `tools/axe/axe.min.js`), Chrome 154.0.8037.58 debug profile (recorded 2026-09-30) | Sweep every sampled view and significant state; direct sweep of cross-origin article iframes from the signed-out profile | `R###-axe.json` (raw), `R###-axe.md` (rendered), one observation per rule in the run |
| view_probe (`scripts/view_probe.py`, CDP) | Structural measurement — assistant-run | Chrome 154.0.8037.58 (debug profiles on ports 9222 / 9223) + CDP (recorded 2026-09-30) | Answer the instrument-decidable checks per view (media absent → n/a, lang, title, target size, reflow, text spacing, autocomplete) before the reviewer session | `R###-probe.json` facts + outcomes in the run |

## Step 2 — Explore the target product

Seeded from the LMS archetype. Every row is a hypothesis: confirm it exists,
correct the details, delete what doesn't apply, and add what exploration
reveals. Test both student and instructor roles.

### 2.1 Common views

| ID | View | Location / path |
|----|------|-----------------|
| C1 | Sign in | `https://learn.essentials-ai.com/login` — confirmed 2026-09-30 (signed-out profile, port 9223): email + password form, "Show password" checkbox, "Forgot your password?" link, footer "Access is provisioned by your program administrator". No campus SSO, no self-registration. `/` and `/learning` redirect here when signed out. **Never load in the authenticated tab.** |
| C2 | Dashboard / course list — **"My Courses"** | `https://learn.essentials-ai.com/learning` — confirmed 2026-09-30: sidebar nav (My Courses / My Certificates / My Profile), "Course experience" tablist (**Classic** / **Gamified**, one course each; the choice persists per account and "progress in each is kept separately"), one course card "AI Foundations - Sonoma State University" with a "Start course" link. Restored to Classic after exploration. |
| C3 | Course home | Same page as C4 (confirmed 2026-09-30): the course player `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123` opens on the last-visited lesson with the course outline in a sidebar (4 section accordions, 21 lessons, per-section "0/n lessons", header progress bar 0 %). |
| C4 | Module / content page — **course player lesson** | `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123` — confirmed 2026-09-30. **Lessons are UI states: the URL never changes** (locators are `UI: My Courses → Start course → <section> → <lesson>`). Two lesson kinds only: (a) **video** ×12 — native `<video controls>` from Supabase storage, no text tracks, a `<details>` "Transcript" below; (b) **article** ×9 — cross-origin iframe from `mnowak-ai.github.io` with its own headings, accordion cards and a four-option "Quick Question". Every lesson ends in a "Complete & continue" button ("Complete lesson" on the last). Full lesson table: `crawl-map-2026-09-30.md`. |
| C5 | Assignment view + submission | **Absent** (confirmed 2026-09-30) — no assignment, upload or text-submission lesson in the provisioned course. |
| C6 | Quiz / exam | **Absent as a lesson type** (confirmed 2026-09-30). The only question in the course is the in-article "Quick Question" (C4b: four buttons, one attempt, feedback text). My Profile › Readiness says it "builds up as quizzes and assessments are answered" and the vendor ACR describes assessments and simulations — hypothesis: they exist in courses not provisioned to this account. Ask the vendor which courses Sonoma State will receive. |
| C7 | Grades | **Absent** (confirmed 2026-09-30) — nearest equivalents: the course-header progress bar and My Profile › Readiness ("Nothing measured yet"). |
| C8 | Discussion board | **Absent** (confirmed 2026-09-30). |
| C9 | Calendar / notifications | **Absent** (confirmed 2026-09-30) — no calendar, notification centre or preferences; every page carries one empty `role=alert` live region. |
| C10 | My Certificates | `https://learn.essentials-ai.com/certificates` — confirmed 2026-09-30: empty state ("No certificates yet… Open one to save it as a PDF or share the verification link") with a "Go to My Courses" link. Earned state unexplored — reachable only by completing the course. |
| C11 | My Profile / account | `https://learn.essentials-ai.com/profile` — confirmed 2026-09-30: three sub-views switched by plain buttons (Account / Readiness / Achievements — no tablist semantics): **Account** = avatar file upload, Full name field + Save changes, read-only email ("managed by your administrator"), New/Confirm password + Update password; **Readiness** = five-area readiness chart placeholder (svg); **Achievements** = certificates placeholder. |
| C12 | Password reset | `https://learn.essentials-ai.com/forgot-password` — confirmed 2026-09-30 (port 9223): email field, "Send reset link", "Back to sign in". The reset e-mail / set-password page is unexplored (would send mail — reviewer only). |
| C13 | Account menu | `UI: any signed-in view → "TU" avatar button` — confirmed 2026-09-30: `role=menu` with the user's name/e-mail/role and two menuitems, "Profile & sessions" (→ C11) and "Sign out". |

### 2.2 Essential functionality — user stories

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a learner, I need to open my course, move through its lessons in order, watch each video (with captions or an equivalent) and read each article, so that I can learn the material. *(confirmed 2026-09-30: video ×12 + article ×9 are the entire course)* | Core purpose |
| F2 | ~~Submit an assignment~~ — **not applicable** (confirmed 2026-09-30: no assignments in the product). | — |
| F3 | As a learner, I need to answer the in-article "Quick Question" and perceive whether I was right, so that I can check my understanding. *(rewritten 2026-09-30; no graded quiz exists in the provisioned course — see C6; extended-time accommodation moot until an assessment is provisioned)* | Only assessment-like interaction; feedback = 3.3.1 / 4.1.3 |
| F4 | As a learner, I need to see my progress through the course (section counts, progress bar, My Profile › Readiness), so that I know where I am. *(rewritten 2026-09-30; no grades exist)* | Core workflow |
| F5 | ~~Participate in discussions~~ — **not applicable** (confirmed 2026-09-30: no discussion feature). | — |
| F6 | ~~Instructor authoring~~ — **out of scope** (confirmed 2026-09-30: not provisioned; excluded by the vendor ACR). | — |
| F7 | As a learner, I need to mark each lesson complete ("Complete & continue") through to the end of the course and then view, download (PDF) and share my certificate, so that I get the credential the program promises. *(added 2026-09-30 — proposed; the certificate is the product's deliverable per the vendor ACR)* | High stakes: the credential |
| F8 | As a learner, I need to sign in with my provisioned e-mail and password, and reset my password when locked out, so that I can reach any of the above. *(added 2026-09-30)* | Gate to everything; 3.3.8 |
| F9 | As a learner, I need to manage my account (name, avatar, password) and switch between the Classic and Gamified course experiences, so that the product works the way I need. *(added 2026-09-30 — proposed)* | Secondary |

### 2.3 Variety of sample types

| Type | Description | Example views |
|------|-------------|---------------|
| Content pages | Vendor-authored static HTML articles rendered in a cross-origin iframe (headings, accordion cards, in-article question) | C4b article lessons (confirmed 2026-09-30) |
| Timed interactions | None observed (confirmed 2026-09-30) — no timers, no session-expiry warning seen | — |
| Rich text editors | None (confirmed 2026-09-30) — the only text inputs are plain fields (name, e-mail, passwords) | C1, C11, C12 |
| File upload | Avatar image only (confirmed 2026-09-30) | C11 Account |
| Data tables | None (confirmed 2026-09-30) | — |
| Threaded discussions | None (confirmed 2026-09-30) | — |
| Modals & notifications | Account menu (`role=menu`); an empty `role=alert` live region on every page; lesson-list drawer ("Hide lessons" / "Close lesson list") | C13, C3/C4 (confirmed 2026-09-30) |
| Video with transcript | Native `<video controls>` (no text tracks) + `<details>` "Transcript" | C4a video lessons (confirmed 2026-09-30) |
| Composite widgets | Course-outline accordion (aria-expanded), "Course experience" tablist, header progressbar, profile sub-view buttons | C2, C3, C11 (confirmed 2026-09-30) |

### 2.4 Technologies relied upon

| Technology / system | Version / notes |
|---------------------|-----------------|
| HTML / CSS / JavaScript / WAI-ARIA | Single-page React-style app with Tailwind utility classes and Radix-style menu/tab primitives; per-view `<title>`, `lang="en"`, skip link, banner/nav/main/complementary landmarks on every signed-in view (confirmed 2026-09-30). **Not Thinkific** — the vendor ACR's platform claims do not describe this product. |
| Rich text editor | None (confirmed 2026-09-30) |
| Embedded media players | Native HTML5 `<video controls preload="none" playsinline>` streaming MP4 from Supabase public storage; **no `<track>`**; prose transcript in a `<details>` (confirmed 2026-09-30) |
| PDF and office documents | None in the course (confirmed 2026-09-30); the certificate is described as saveable to PDF — unexplored |
| LTI / iframe embeds | Article lessons are `<iframe title="<lesson>">` from `mnowak-ai.github.io` (GitHub Pages, static HTML with Google Fonts, inline script for accordion/quiz/scroll-progress; no landmarks or ARIA) (confirmed 2026-09-30) |
| SSO (SAML/CAS) | None — local e-mail + password accounts provisioned by an administrator (confirmed 2026-09-30) |

### 2.5 Other relevant samples

| ID | View | Location / path |
|----|------|-----------------|
| A1 | Accessibility statement | **None in the product** (confirmed 2026-09-30); none on the marketing site either (`02-vendor.md`). |
| A2 | Help / student support | **None found on any view** (confirmed 2026-09-30) — no help link, support e-mail or contact in header, sidebar, footer or account menu. The vendor ACR claims (3.2.6) that "support contact information appears in a consistent location". |
| A3 | Authentication | Local sign-in C1 `/login` and password reset C12 `/forgot-password` (confirmed 2026-09-30); no SSO. |
| A4 | Accommodation settings (extra time, etc.) | None (confirmed 2026-09-30) — nothing timed exists to accommodate. |
| A5 | Notification preferences | None (confirmed 2026-09-30). |

### 2.6 Exploration notes (recon for testing — not yet findings)

Dated observations from exploration sessions (see
`ontology/assisted-exploration.md`): machine-extraction results, suspected
issues phrased as "verify X under check Y in a run", artifacts created during
exploration, and replication quirks (e.g., SPA views whose URL does not
change). Nothing here is a finding until a logged run verifies it.

**2026-09-30 — assisted exploration over CDP (`crawl-map-2026-09-30.md`; instruments: link harvest, `cdp_probe.py` AX summaries and JS walks, direct fetch of one article).** Progress was left at 0 % (no lesson completed, nothing submitted); the Course-experience tab was restored to Classic; the signed-out profile (port 9223) was created for C1/C12.

- **Extraction result:** the app exposes well to automation — landmarks, a skip link, named controls and headings on every view; `Accessibility.getFullAXTree` reports **no unnamed control on any view**. The article iframes are cross-origin: their inner tree is *not* in the host page's AX summary, so every article check needs the reviewer's AT (or the article URL opened directly).
- **Videos have no captions track** — 0 `<track>` / 0 `textTracks` on all 12 `<video>` elements. **Reviewer, 2026-09-30: the videos carry open captions burned into the picture** (so the captions claim under 1.2.2 is plausibly met, but not by a track). Still to verify in the S3 run: that the burned-in captions are accurate and complete for the whole video (1.2.2), that they stay legible at zoom/reflow and cannot be enlarged or restyled (1.4.4 / 1.4.12 — note, not a failure), and whether narration describes on-screen visuals as the ACR asserts (1.2.3 / 1.2.5). The untimed prose transcript in the `<details>` disclosure is the media alternative for 1.2.3.
- **In-article "Quick Question"** (`m1-article-04`): four `<button onclick>` options; result = CSS class `correct`/`wrong` on the buttons, `pointer-events:none` instead of `disabled`, feedback injected by `innerHTML` into a plain `div`. Verify under 4.1.3 (is the ✅/❌ feedback announced?), 3.3.1 / 1.4.1 (is right/wrong conveyed by more than colour and an emoji?), 4.1.2 (are the exhausted options exposed as unavailable?) on S4 with JAWS.
- **In-article accordion cards** are `<div onclick>` — not focusable, no role. Verify under 2.1.1 / 4.1.2 on S4 (keyboard: can the four cards be opened at all?).
- **Article iframe content has no landmarks or ARIA** and a `<title>` naming a different program ("AI in Business Certification"); the iframe's own `title` attribute is the lesson name. Verify under 2.4.1 / 2.4.2 how the frame is announced and navigated (JAWS frame list) on S4.
- **Article motion:** scroll-driven progress bar and IntersectionObserver fade-in reveals inside every article. Verify under 2.2.2 (nothing loops) and note for 2.3.3 (AAA, advisory).
- **Lesson list is rendered twice** in the DOM (sidebar + drawer, `nav "Course outline"` ×2). Verify under 2.4.3 / 1.3.1 / 2.4.1 on S3: does a screen-reader user meet 21 lessons twice? is the drawer copy hidden from the tab order when closed?
- **Lesson button accessible names** concatenate title and duration with no separator ("Icebreaker0m", "1Intro to the Course0/2 lessons"). Verify under the no-vision name/role check (4.1.2 / 2.5.3) on S3.
- **Profile sub-views** (Account / Readiness / Achievements) are plain buttons — no tablist, no `aria-selected`/`aria-current`; the selected one is styled by border only. Verify under 4.1.2 / 1.4.1 / 1.3.1 on S6.
- **Course-experience tabs** on S2 are a real `tablist`; the tab choice persists per account. Verify under 3.2.2 (does switching change context?) and 4.1.2.
- **"Complete & continue" advances progress** — the reviewer presses it, never the assistant; the run records which lesson was completed. **Nothing is timed**, so 2.2.1 is likely n/a on every view (view_probe to confirm).
- **No help or support contact anywhere** in the product (A2) although the ACR claims 3.2.6 Supports. Verify under the consistent-help check on S2–S6 (it is decided at the set-of-pages level).
- **Vendor ACR mismatch (for the 06 audit, not a finding):** the ACR describes a Thinkific-hosted program with quizzes, scenario simulations, third-party AI-tool activities, downloadable portfolio materials and a certificate; the provisioned product is a bespoke "AI Readiness OS" app whose only course holds 12 videos and 9 articles. Ask the vendor: which courses will Sonoma State's learners receive, and does any contain the assessments/simulations the ACR covers?
- **Replication quirks:** (a) lessons carry no URL — runs on S3/S4 use `UI:` locators through the outline; (b) the course player opens on the *last-visited* lesson, so a run must first select its lesson; (c) loading `/login` in the authenticated tab signs the reviewer out — C1/C12 are probed from port 9223 only; (d) the Gamified toggle is per-account state: every run records which experience was active.
- **Sign in button** renders grey (looks disabled) until both fields are filled — verify under 1.4.11 / 4.1.2 on S1 whether it is actually `disabled` and whether an empty submit produces an error (3.3.1).

## Step 3 — Select the representative sample set

If feasible (few views, or a document), evaluate the entire product and skip
sampling — record that decision here.

### 3.1 Structured sample set

Must reflect **all** of: common views (2.1), essential functionality (2.2),
sample types (2.3), technologies relied upon (2.4), and other relevant samples
(2.5). One sample may represent several of these — record what it represents.

**Removing a view from the sample later** (a scope decision by the reviewer,
e.g. "instructor-only views are out"): append ` — removed YYYY-MM-DD: <reason>`
to the view's name cell. Never delete the row — IDs are stable and the view's
runs and findings stay on record. The CLI, the SQLite mirror, coverage,
completion and the dashboard exclude removed views from the sample counts and
list them separately; record the decision in §1.1 *Exclusions* as well.

| ID | View / screen | Location / path | Represents (C/F/type/tech/A refs) |
|----|---------------|-----------------|-----------------------------------|
| S1 | Sign in — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/login` — signed-out profile (port 9223) only | C1; A3; F8; form, accessible authentication (3.3.8) |
| S2 | My Courses — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/learning` | C2; F9; tablist, course card, sidebar nav, account menu (C13) |
| S3 | Course player — video lesson "Icebreaker" — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123` via `UI: My Courses → Start course → 1 Intro to the Course → Icebreaker` | C3, C4a; F1, F4, F7; native video (no tracks), Transcript disclosure, outline accordion, progressbar, "Complete & continue" |
| S4 | Course player — article lesson "Using New Technology the Right Way" — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123` via `UI: My Courses → Start course → 3 AI & Ethics → Using New Technology the Right Way` (iframe `https://mnowak-ai.github.io/ai-academics-articles/m1-article-04-using-technology-the-right-way.html`) | C4b; F1, F3; cross-origin iframe article, accordion cards, "Quick Question", scroll/fade motion |
| S5 | My Certificates — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/certificates` | C10; F7; empty state now, earned state after completion |
| S6 | My Profile — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/profile` | C11; F9; forms, file upload, password change, pseudo-tabs, readiness chart |
| S7 | Password reset — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/forgot-password` — signed-out profile (port 9223) only | C12; A3; F8 |

### 3.2 Randomly selected sample set

Size: **10% of the structured sample set**, selected randomly from in-scope
views not already sampled. Record the selection method (crawler, full listing,
server logs…) so the selection is replicable. These are compared against the
structured set in `04-task-testing.md` §C.

| ID | View / screen | Location / path |
|----|---------------|-----------------|
| R1 | Course player — article lesson "Finding Hidden Scholarships with AI" — proposed 2026-09-30 — confirmed 2026-09-30 (reviewer: "the sample looks good") | `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123` via `UI: My Courses → Start course → 3 AI & Ethics → Finding Hidden Scholarships with AI` (iframe `…/m1-article-05-opening-doors-to-your-future.html`) |

**Selection method:** (proposed 2026-09-30) 7 structured samples → 10 % rounded up = 1. The product has no unsampled addressable views (every route is in §3.1), so the pool is the 19 lesson states not already sampled, in outline order as listed in `crawl-map-2026-09-30.md`; drawn with Python `random.Random(20260930).sample(pool, 1)`. Re-draw if the structured set changes.

### 3.3 Complete processes — task sequences

Expand each essential-functionality user story (2.2) into a process. Record
the **default sequence** (standard use case: no input errors, no optional
branches) and the **critical branch sequences** (commonly used or critical
alternatives; a branch ends where it re-enters the default sequence). Every
view in a sequence must be in the sample set. Record the action needed to move
from each step to the next so any evaluator can replicate the run.

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
