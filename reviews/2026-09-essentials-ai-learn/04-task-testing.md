# Task-Based Testing — Essentials AI Learn

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
python scripts/review.py log-test <review> --view S1 --url <page-url> \
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
| **Plain summary** | (ONE sentence for the published report: what is wrong and what a user cannot do, present tense, no IDs, no dates, no reviewer, no tool names, ≤ 200 chars — rules in ontology/reporting.md) |
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

`review.py matrix <review>` shows the views × modalities grid and remaining
gaps; `validate` fails while cells are unrun or results unset.

Check the full view — all components and significant states — without
initiating processes (those are covered in §A). Repeated components (header,
navigation, footer) need re-checking only where they appear or behave
differently.

### View S1 — Sign in (`https://learn.essentials-ai.com/login`)

| | |
|---|---|
| **Baselines run** | B5 (NVDA 2024.1), B2 (keyboard), B3 (400 % zoom), grayscale; axe R006; probe R050–R056 |
| **Date tested** | 2026-09-30 |
| **Findings** | V-F1, V-F2 |

#### Finding V-F1

| | |
|---|---|
| **Where** | S1 Sign in page — the Email field's placeholder text "you@school.edu" |
| **Observed** | The placeholder is rgb(139,135,149) on the white field: **3.5:1**, below the 4.5:1 minimum for 13 px text (it passes only the 3:1 large-text threshold). Measured by computed-style sampling against the field's solid white background (R051 O5) and confirmed by the reviewer with a contrast tool on 2026-09-30 (R051 O11: "contrast issue with the placeholders in the input for email"). The placeholder is the only on-page example of the expected address format; the field's label "Email" itself passes at 9.36:1. The Password field has no placeholder. |
| **Plain summary** | The example address shown inside the sign-in page's email field is too faint against the white field for people with low vision to read. |
| **Affected users** | Low-vision users (faint placeholder text) |
| **WCAG criteria failed** | 1.4.3 |
| **Severity** | Minor |
| **Evidence** | `evidence/runs/R051/R051-signin-1280.png` (run R051, O5 measurement, O11 reviewer confirmation) |

#### Finding V-F2

| | |
|---|---|
| **Where** | S1 Sign in page — the Password field |
| **Observed** | The Password field and the "Show password" checkbox share one wrapping `<label>`, so the field's accessible name is "Password Show password". NVDA 2024.1 on focus (R050 O13): "Password Show password edit protected has auto complete blank". The visible label "Password" is contained in the name (2.5.3 holds) and the role/state are correct; the defect is that the field announces a neighbouring control's label as part of its own name. axe reported the pattern as `form-field-multiple-labels` (R006 O1). Reviewer's severity decision 2026-09-30: Minor. |
| **Plain summary** | The sign-in page's password field announces itself as "Password Show password", so screen-reader users hear a nearby checkbox's label mixed into the field's name. |
| **Affected users** | Screen reader users |
| **WCAG criteria failed** | 4.1.2 |
| **Severity** | Minor |
| **Evidence** | R050 O10, O13, O14 (NVDA speech-viewer output); R006 `R006-axe.md` (`form-field-multiple-labels`) |

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

Two assertions no query can make for you. Everything else the old checklist
asked for is now proved by the database — `review_db.py completion` covers
task verdicts (C3), view sweeps (C7) and finding evidence (C9), and
`review_db.py check` covers the rollup. A human ticking a box is weaker
evidence than the query, not stronger.

- [ ] Every branch sequence was walked, not just default sequences
- [ ] Random-vs-structured comparison completed (and sample extended if needed)
