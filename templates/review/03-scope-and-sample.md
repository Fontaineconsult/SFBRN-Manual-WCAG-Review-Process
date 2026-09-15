# Scope & Sample — {{PRODUCT_NAME}}

WCAG-EM 2.0 steps 1–3 (see `ontology/wcag-em.md`). Work through the sections in
order; WCAG-EM allows returning to an earlier step as exploration or testing
reveals new information.

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
| B1 | Windows 11 | Chrome | JAWS |
| B2 | (any) | (any) | Keyboard only (no pointer) |
| B3 | (any) | (any) | 400% zoom / reflow |
| B4 | macOS | Safari | VoiceOver (optional) |

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
| WAVE (WebAIM) browser extension | Automated checker | | Sweep every sampled view and state | Summary counts, error list, annotated screenshots |
| view_probe (`scripts/view_probe.py`, CDP) | Structural measurement — assistant-run | Chrome (debug profile) + CDP | Answer the instrument-decidable checks per view (media absent → n/a, lang, title, target size, reflow, text spacing, autocomplete) before the reviewer session | `R###-probe.json` facts + outcomes in the run |

## Step 2 — Explore the target product

Before exploring, secure real access: a representative account, realistic
data, and configuration matching what campuses would use. Note cursory-check
observations (contrast, structure, navigation) for detailed testing later.

### 2.1 Common views

Views relevant to the entire product — entry points and views linked from all
others (header, navigation, footer).

| ID | View | Location / path |
|----|------|-----------------|
| C1 | | |

### 2.2 Essential functionality — user stories

Functionality that, if removed, fundamentally changes the use or purpose of
the product. Each row becomes a task cluster in `04-task-testing.md` and is
expanded into a process in §3.3 below.

| ID | User story | Why essential |
|----|-----------|---------------|
| F1 | As a (user), I need to (goal), so that (outcome). | |
| F2 | | |

### 2.3 Variety of sample types

Types (not instances) of views that differ in layout, structure, content,
components, technology, area, authorship, or dynamic behavior (dialogs, error
states, notifications).

| Type | Description | Example views |
|------|-------------|---------------|
| | | |

### 2.4 Technologies relied upon

Technologies relied upon for conformance (HTML, CSS, JavaScript, WAI-ARIA,
SVG, PDF…) plus systems worth noting (CMS, design system, front-end
framework), with versions where known.

| Technology / system | Version / notes |
|---------------------|-----------------|
| | |

### 2.5 Other relevant samples

Views specifically relevant to accessibility: accessibility features
documentation, help, settings/preferences/shortcuts, contact and support,
and sensitive functionality (authentication, personal data, payments).

| ID | View | Location / path |
|----|------|-----------------|
| A1 | | |

### 2.6 Exploration notes (recon for testing — not yet findings)

Dated observations from exploration sessions (see
`ontology/assisted-exploration.md`): machine-extraction results, suspected
issues phrased as "verify X under check Y in a run", artifacts created during
exploration, and replication quirks (e.g., SPA views whose URL does not
change). Nothing here is a finding until a logged run verifies it.

- (none yet)

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
| S1 | | | |

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

#### Process P1 — (name) — implements F1

**User story:** (copy from 2.2)

Default sequence:

| Step | View (sample ID) | Action to proceed to next step |
|------|------------------|--------------------------------|
| 1 | | |
| 2 | | |

Branch sequences:

| Branch | From step | Steps and actions | Re-enters default at |
|--------|-----------|-------------------|----------------------|
| P1-a | | | |
