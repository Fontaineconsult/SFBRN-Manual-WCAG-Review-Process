# Per-Criterion Results — Adobe Express

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
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.2 Captions (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.1 Info and Relationships (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.2 Meaningful Sequence (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.3 Sensory Characteristics (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.1 Use of Color (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:** S1 grayscale pass (R003) — selected states and badges survive; NC2 observation open (link hover/focus cues to confirm). Other views pending.

### 1.4.2 Audio Control (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.1.1 Keyboard (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Does Not Support (Web)
- **Task findings:**
- **Remarks:**

### 2.1.2 No Keyboard Trap (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.1.4 Character Key Shortcuts (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.2.1 Timing Adjustable (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.2.2 Pause, Stop, Hide (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:** S1: search-bar placeholder auto-rotates suggestions with no visible pause control (exploration observation) — verify duration/mechanism in cognition run.

### 2.3.1 Three Flashes or Below Threshold (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.1 Bypass Blocks (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (Web)
- **Task findings:** V-F3
- **Remarks:** S1: no skip link; ~15 Tab stops in the app bar before content (R004, keyboard confirmation pending W14). AMENDED per R001 O7: proper landmark set (Apps[nav]/banner/Primary[nav]/main/search) means SR users bypass fine — ARIA11 is a formally sufficient technique, which would make the vendor's "Supports" defensible. REVIEWER DECISION PENDING: keep as failure (no mechanism usable by keyboard-without-AT users) or reclassify Supports + advisory barrier. Outcome stands as Does Not Support only until that call is made.

### 2.4.2 Page Titled (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.3 Focus Order (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Does Not Support (Web)
- **Task findings:**
- **Remarks:**

### 2.4.4 Link Purpose (In Context) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.1 Pointer Gestures (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.2 Pointer Cancellation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.3 Label in Name (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.5.4 Motion Actuation (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.1.1 Language of Page (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.1 On Focus (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.2 On Input (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.6 Consistent Help (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 3.3.1 Error Identification (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.2 Labels or Instructions (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.7 Redundant Entry (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 4.1.2 Name, Role, Value (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F4
- **Remarks:** S1: header community button has no accessible name (axe `aria-command-name`, R009) — JAWS confirmation pending (W5). Also pending W5: aria-controls target existence on "More apps", account-button state toggling (R009 O5). Vendor admits failure; extent to be established across views.

---

## Table 2: Success Criteria, Level AA

### 1.2.4 Captions (Live) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.2.5 Audio Description (Prerecorded) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.4 Orientation (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.3.5 Identify Input Purpose (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.3 Contrast (Minimum) (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Does Not Support (Web)
- **Task findings:** V-F2
- **Remarks:** S1: "browse" link 3.96:1 at 11px — confirmed by two independent instruments (computed sample R002; axe-core violation R009, same node). Gradient-background text (app bar, 15 nodes axe marks incomplete) still needs eyedropper (W13). Vendor's own claim admits failure; scope appears narrower than claimed so far.

### 1.4.4 Resize Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.5 Images of Text (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.10 Reflow (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 1.4.11 Non-text Contrast (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Does Not Support (Web)
- **Task findings:**
- **Remarks:**

### 1.4.12 Text Spacing (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:** S1 pass under override (R002 O1; "Premium member" badge flicker to re-verify). Other views pending.

### 1.4.13 Content on Hover or Focus (Level AA)
- **Outcome:** Does Not Support
- **Vendor claim:** Partially Supports (Web)
- **Task findings:** V-F1
- **Remarks:** S1 left-rail hover flyout: not hoverable, not dismissible via Esc, persists stuck over content (R002, corroborated R003). Assistant-driven, pending reviewer confirmation with continuous pointer movement. Worse than vendor claim if confirmed.

### 2.4.5 Multiple Ways (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.6 Headings and Labels (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Does Not Support (Web)
- **Task findings:**
- **Remarks:**

### 2.4.7 Focus Visible (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**

### 2.4.11 Focus Not Obscured (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 2.5.7 Dragging Movements (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 2.5.8 Target Size (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 3.1.2 Language of Parts (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.3 Consistent Navigation (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.2.4 Consistent Identification (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.3 Error Suggestion (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Supports (Web)
- **Task findings:**
- **Remarks:**

### 3.3.8 Accessible Authentication (Minimum) (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Not covered by vendor ACR
- **Task findings:**
- **Remarks:**

### 4.1.3 Status Messages (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:** Partially Supports (Web)
- **Task findings:**
- **Remarks:**
