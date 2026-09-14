# Per-Criterion Results — The Expert TA

The criterion-level **rollup** of the findings recorded in
`04-task-testing.md`. One block per WCAG 2.2 success criterion, grouped like
VPAT 2.5 WCAG-edition tables, so this file renders directly into ACR format.

Do not record new findings here — record them in `04-task-testing.md` and cite
their IDs in **Task findings** (e.g., `T1-F1, V-F3`). The **Outcome** must be
consistent with the cited findings: a criterion with a Blocker/Major finding on
essential functionality is at most Partially Supports; with no findings and
relevant content tested, Supports.

**Outcome vocabulary (ACR terms):**

- **Supports** — the functionality of the product has at least one method that meets the criterion without known defects or meets with equivalent facilitation.
- **Partially Supports** — some functionality of the product does not meet the criterion.
- **Does Not Support** — the majority of product functionality does not meet the criterion.
- **Not Applicable** — the criterion is not relevant to the product.
- **Not Evaluated** — not yet tested (initial state; must not remain in a final report).

For each criterion record: the **Outcome**; the **Vendor claim** (from their
ACR, `02-vendor.md`); **Task findings** (IDs from `04-task-testing.md` — which
tasks and views failed this criterion); and **Remarks** (what was tested, on
which sample items, with which tool/method — evidence lives with the findings).

---

## Table 1: Success Criteria, Level A

### 1.1.1 Non-text Content (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F12
- **Remarks:** [provisional] 2026-09-10 NVDA on S3: the Problem 8 figure is hidden from AT (empty alt on an informative diagram; `G` finds no graphic). MathJax math is readable in browse mode (V-F10 withdrawn). Solutions-page figures with broken `alt=` markup (R014) still to be confirmed. Vendor-claim discrepancy.

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.2.2 Captions (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.3.1 Info and Relationships (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F1, T1-F2, V-F1, V-F2 (Minor), V-F5, V-F7, V-F9, V-F11, V-F13
- **Remarks:** [provisional — S2 confirmed; other views pending confirmation of axe results] 2026-09-10 NVDA on S2: no programmatic headings (visual titles are focusable divs); DevExpress grids carry identical generic captions (headers are associated per cell); popup form labels unassociated. axe reports the same pattern on all 14 sampled views (R001–R014, unconfirmed). Vendor-claim discrepancy.

### 1.3.2 Meaningful Sequence (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.3.3 Sensory Characteristics (Level A)
- **Outcome:** Supports (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-14 by the assistant from the reviewer's 2026-09-10 narration; reviewer confirms at walkthrough W36] No instruction in the sampled views refers to shape, colour, size, position or sound alone (the vendor's jump-point and chord instructions name keys and controls). The NV8 fails on R016 (grids told apart only by order) and R017 (a math option identified only as "row 4 table 1"; the inserted hint findable only by its position) are *consequences* of missing structure and status messages, already rolled up under 1.3.1 (V-F2, V-F11) and 4.1.3 / 2.4.3 (V-F15) — not instructions that rely on sensory characteristics.

### 1.4.1 Use of Color (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.2 Audio Control (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.1.1 Keyboard (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.1.2 No Keyboard Trap (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:**  (V-F4 popup-escape finding withdrawn 2026-09-10 — no citation.) MO3 passed on S3 (R018); other views untested. 2026-09-10: an initial keyboard-trap report on the Class Menu popups was withdrawn — each popup has an exposed, working Cancel/Close button; only Esc is unsupported. Full check in the S11 motor run.

### 2.1.4 Character Key Shortcuts (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.2.1 Timing Adjustable (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.2.2 Pause, Stop, Hide (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.3.1 Three Flashes or Below Threshold (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.4.1 Bypass Blocks (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F1 (Major)
- **Remarks:**  2026-09-11 rollup correction (db integrity: V-F1 names 2.4.1; V-F3 does not): V-F1 fails 2.4.1 in combination with V-F3's skip controls. [provisional] 2026-09-10 NVDA on S2: the section skip links work (focus moves to the next section) and a top-of-page jump point exists, so a bypass mechanism is present in Accessibility Mode; the controls are links by role and confusingly worded (V-F3). Standard mode (S1) relies on the vendor's jump points alone — pending R015. Vendor claim not contradicted so far.

### 2.4.2 Page Titled (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.4.3 Focus Order (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F2, V-F8, V-F13, V-F15
- **Remarks:** [provisional] 2026-09-10 NVDA on S3: activating a problem link does not move focus into the problem; the vendor's jump-point menu mounts links outside the natural focus path and is itself a hidden tab stop. Vendor-claim discrepancy.

### 2.4.4 Link Purpose (In Context) (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:**
- **Task findings:** V-F3 (Minor)
- **Remarks:** 2026-09-11 rollup derived from V-F3 (S2 skip controls read as links whose text does not state their purpose; reviewer-confirmed 2026-09-10, R016 O4). Link purpose on S3 (NV10) and the remaining views still to be walked.

### 2.5.1 Pointer Gestures (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.5.2 Pointer Cancellation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.5.3 Label in Name (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F7
- **Remarks:** [provisional] 2026-09-10 NVDA on S2: the Classes and Class Menu selects' accessible names are an instruction sentence; the visible labels "Classes:" / "Class Menu:" are not part of the name. Vendor-claim discrepancy.

### 2.5.4 Motion Actuation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.1.1 Language of Page (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.2.1 On Focus (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.2.2 On Input (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.2.6 Consistent Help (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.3.1 Error Identification (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.3.2 Labels or Instructions (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F5, V-F13
- **Remarks:** [provisional] 2026-09-10 S11 popup forms: labels are unassociated table-cell text. Instructor pages show the same (axe R006 59 fields, unconfirmed).

### 3.3.7 Redundant Entry (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 4.1.2 Name, Role, Value (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F1, V-F3, V-F5, V-F6, V-F7, V-F8, V-F11, V-F13
- **Remarks:** [provisional] 2026-09-10 S2: skip controls exposed as links though they act as buttons; per-row Actions select without a name; popup inputs without names. Pending confirmation: unnamed answer radios (R004 O1), unnamed jump-point buttons (R001 O2), unlabeled DevExpress editors product-wide. Vendor-claim discrepancy.

---

## Table 2: Success Criteria, Level AA

### 1.2.4 Captions (Live) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.2.5 Audio Description (Prerecorded) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.3.4 Orientation (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.3.5 Identify Input Purpose (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.3 Contrast (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.4 Resize Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.5 Images of Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.10 Reflow (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.11 Non-text Contrast (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.12 Text Spacing (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.4.13 Content on Hover or Focus (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.4.5 Multiple Ways (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.4.6 Headings and Labels (Level AA)
- **Outcome:** Supports (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-14 by the assistant from the reviewer's 2026-09-10 narration; reviewer confirms at walkthrough W36] 2.4.6 requires that headings and labels *which exist* describe topic or purpose; it does not require headings. The sample has no programmatic headings at all (NV2 fail on R016, R017) — that is rolled up under 1.3.1 (V-F1, T1-F1) and 2.4.1. The visible section captions ("Classes", "Class Menu", "Class Assignments", "Class News"), the popup form labels (S11) and the assignment-editor labels are descriptive where present; the missing *association* of those labels is 1.3.1 / 3.3.2 / 4.1.2 (V-F5, V-F7, V-F13), not 2.4.6. Skip-control wording (V-F3) is rolled up under 2.4.4.

### 2.4.7 Focus Visible (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.4.11 Focus Not Obscured (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.5.7 Dragging Movements (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.5.8 Target Size (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.1.2 Language of Parts (Level AA)
- **Outcome:** Not Applicable (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-14 by the assistant; reviewer confirms at walkthrough W36] No passage or phrase in a language other than English was found in any sampled view (NV9 on R016, R017: nothing mispronounced with an English synthesizer voice; probe language facts on all 14 views). Mathematical notation is not a language change. The page-level `lang` defect on three views is 3.1.1.

### 3.2.3 Consistent Navigation (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.2.4 Consistent Identification (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.3.3 Error Suggestion (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 3.3.8 Accessible Authentication (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 4.1.3 Status Messages (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F9, V-F14 (Minor), V-F15
- **Remarks:** [provisional] 2026-09-10 NVDA on S3: the instruction read-out (Ctrl+Shift+5) is announced correctly via the alert region; the answer read-out (Ctrl+Shift+2) injects raw MathJax markup for math-bearing options, so the status message is unusable; on the drag-and-drop alternative form, placements are not announced and the read-back runs items together. Submission-result dialogs are announced correctly (R017 O10, O14). Vendor-claim discrepancy.
