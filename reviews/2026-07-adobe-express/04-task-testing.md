# Task-Based Testing — Adobe Express

WCAG-EM 2.0 step 4: evaluate the selected sample set. Testing clusters around
the **tasks** (user stories / complete processes from `03-scope-and-sample.md`
§3.3), so findings read as *"this task fails at this step, because of these
WCAG criteria."* The per-criterion rollup in `05-results.md` cites the finding
IDs recorded here — record each finding once, here only.

Evaluation is against all five WCAG 2 conformance requirements at the target
level (WCAG 2.2 AA): (1) conformance level, (2) full pages, (3) complete
processes, (4) only accessibility-supported ways of using technologies,
(5) non-interference.

**Finding IDs:** `T<task>-F<n>` for task findings (T1-F2 = task 1, finding 2);
`V-F<n>` for view-sweep findings.

**Severity:** **Blocker** — the task cannot be completed by an affected user
group; **Major** — completion is substantially burdened; **Minor** — barrier
with a reasonable workaround.

**Task verdicts:** **Pass** — completable by all baseline combinations without
significant barriers; **Pass with barriers** — completable, but Major or Minor
findings exist; **Fail** — not completable by at least one affected user group
within the accessibility support baseline.

**Test runs & evidence:** every test session is logged as a run *before*
testing starts:

```
python scripts/review.py log-test adobe --view S1 --url <page-url> \
    --modality no-vision --tool jaws --baseline B1 [--task T1] [--tester NAME]
```

This records which page/view was tested, when, with which tool and baseline
(the WCAG-EM "evaluation specifics" record), appends to `evidence/test-log.md`,
and creates `evidence/runs/R###/` with a `run.md` for notes — JAWS
action/announced/expected notes or WAVE summary counts — and the run's
screenshots/exports (`R###-*.png`). Capture conventions per tool:
`ontology/testing-tools.md`. Findings below cite run IDs and files in their
**Evidence** row.

---

## A. Task clusters (WCAG-EM step 4.2 — complete processes)

One cluster per process in 03 §3.3. Walk the default sequence, then each
branch sequence, with each baseline combination (03 §1.3). Evaluate the
content that changes along the process — form and dialog interaction, input
confirmations, error messages, and other feedback are all in scope.

### Task T1 — (name) — process P1

| | |
|---|---|
| **User story** | |
| **Verdict** | Not run / Pass / Pass with barriers / Fail |
| **Baselines run** | B1, B2, B3 |
| **Date(s) tested** | |

**Sequence notes:** (per-step observations; identify the step where each
barrier occurs)

#### Finding T1-F1

| | |
|---|---|
| **Where** | (step and view) |
| **Observed** | (what happens; steps to reproduce) |
| **Affected users** | (e.g., screen reader users, keyboard-only users) |
| **WCAG criteria failed** | (e.g., 3.3.2, 4.1.2) |
| **Severity** | Blocker / Major / Minor |
| **Evidence** | (files under `evidence/`) |

---

## B. View sweep (WCAG-EM step 4.1 — per-view modality checks)

Every sampled view (03 §3.1/§3.2) is checked under **every sensory/functional
modality** (Section 508 Functional Performance Criteria: no-vision,
low-vision, no-color, no-hearing, no-speech, motor, cognition) using the
standardized per-view checklists in `ontology/modality-checks.md`, plus a
WAVE sweep per view. One run per view×modality (`log-test --modality`), with
the run's **Result** set to Works / Works with issues / Broken / N/A.
Failures become findings below, citing the check ID (e.g., `MO4`) and run ID.

`review.py matrix adobe` shows the views × modalities grid and remaining
gaps; `validate` fails while cells are unrun or results unset.

Check the full view — all components and significant states — without
initiating processes (those are covered in §A). Repeated components (header,
navigation, footer) need re-checking only where they appear or behave
differently.

### View S1 — Home dashboard

| | |
|---|---|
| **Baselines run** | B3 (R002, partial), — (R003, R005, R006, R007 wave-blind, R009 axe), B2 (R004, partial); B1/JAWS in progress (R001, walkthrough W2–W3 done) |
| **Date tested** | 2026-08-04 (assistant-driven trials + axe sweep; reviewer walkthrough in progress) |
| **Findings** | V-F1, V-F2, V-F3, V-F4 |

#### Finding V-F1

| | |
|---|---|
| **Where** | S1 Home dashboard — left-rail hover flyout ("Get inspired" panel on rail items) |
| **Observed** | Hover content violates all three 1.4.13 conditions observed: moving the pointer onto the flyout dismissed it (not hoverable); Esc did not dismiss it (not dismissible); once stuck, it persisted indefinitely over page content through unrelated interactions. Assistant-driven (synthetic hover teleports) — confirm with continuous pointer movement. |
| **Affected users** | Low-vision magnification users (flyout obscures content they cannot reposition around); motor-impaired users relying on Esc |
| **WCAG criteria failed** | 1.4.13 |
| **Severity** | Major |
| **Evidence** | evidence/runs/R002/R002-flyout-hover.jpg, evidence/runs/R003/R003-grayscale-home.jpg (flyout still open minutes later) (runs R002, R003) |

#### Finding V-F2

| | |
|---|---|
| **Where** | S1 Home dashboard — Upload card, "browse" link ("Drag and drop files or browse") |
| **Observed** | 11px link text at 3.96:1 computed contrast against the card background (4.5:1 required). CONFIRMED by two independent instruments: computed-style measurement (R002) and axe-core `color-contrast` violation on the same `.browse-text` node (R009). Consistent with vendor ACR "Does Not Support" for 1.4.3. |
| **Affected users** | Low-vision users |
| **WCAG criteria failed** | 1.4.3 |
| **Severity** | Minor |
| **Evidence** | evidence/runs/R002/R002-upload-card-browse.png (run R002); evidence/runs/R009/R009-axe.json (run R009) |

#### Finding V-F3

| | |
|---|---|
| **Where** | S1 Home dashboard — page-level keyboard entry (Adobe cross-product app-switcher bar precedes all content) |
| **Observed** | No skip link on first Tab; ~15 observed Tab stops remained in the app-switcher bar region before any Express content. Assistant-driven with a focus-attribution caveat (run R004 O3) — reviewer keyboard confirmation still pending (W14). AMENDED 2026-08-04 (R001 O7): landmark walk found Apps[nav]/banner/Primary[nav]/main/search — SR users can bypass via landmarks (sufficient technique ARIA11), so the barrier is keyboard-only (non-AT) users. Reviewer decision pending: does 2.4.1 stand as a failure (no keyboard-reachable mechanism) or reclassify as advisory barrier with 2.4.1 = Supports? |
| **Affected users** | Keyboard-only users without AT (every page visit); screen reader users NOT affected (landmarks, R001 O7) |
| **WCAG criteria failed** | 2.4.1 |
| **Severity** | Major |
| **Evidence** | evidence/runs/R004/R004-tab5-focus.jpg, R004-tab15-plusbutton-focus.jpg (run R004) |

#### Finding V-F4

| | |
|---|---|
| **Where** | S1 Home dashboard — header, community/people icon button (`x-community-discovery-trigger` → icon-only `sp-action-button`) |
| **Observed** | axe-core `aria-command-name` violation (serious): the button exposes `role="button"` with no accessible name — its only content is an `aria-hidden` icon with an empty label. A screen reader user hears "button" with no purpose. Assistant-driven (axe, R009); JAWS confirmation pending (walkthrough W5: what announces on this control?). Vendor claims Does Not Support for 4.1.2 — consistent. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 |
| **Severity** | Major |
| **Evidence** | evidence/runs/R009/R009-axe.json (run R009, violations[0]) |

---

## C. Sample comparison (WCAG-EM step 4.3 — random vs structured)

Check that the random samples (03 §3.2) show no content types or findings
absent from the structured set. If they do, the structured sample was not
representative: return to step 3, extend the sample set, and test the
additions. Repeat until no new types or findings appear.

| Random sample | New content type? | New findings? | Action taken |
|---------------|-------------------|---------------|--------------|
| R1 | | | |

---

## D. Coverage check

Before moving to `05-results.md`:

- [ ] Every process in 03 §3.3 has a task cluster with a verdict
- [ ] Every branch sequence was walked, not just default sequences
- [ ] Every non-process sample has a view-sweep entry
- [ ] Every finding names at least one WCAG criterion, a severity, and evidence
- [ ] Random-vs-structured comparison completed (and sample extended if needed)
- [ ] `05-results.md` updated: every failed criterion cites finding IDs from this file
