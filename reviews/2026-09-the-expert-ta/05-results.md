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
- **Task findings:** V-F12, V-F16 (Minor)
- **Remarks:** 2026-09-14 S1: the grids' expand controls are clickable images with no text alternative (V-F16). [provisional] 2026-09-10 NVDA on S3: the Problem 8 figure is hidden from AT (empty alt on an informative diagram; `G` finds no graphic). MathJax math is readable in browse mode (V-F10 withdrawn). Solutions-page figures with broken `alt=` markup (R014) still to be confirmed. Vendor-claim discrepancy.

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
- **Outcome:** Not Applicable (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-15 by the assistant; reviewer confirms] No audio-only or video-only prerecorded media in the sample: the probe found no media on 14 views as loaded, and the media the reviewer found (YouTube embeds in the Assignment Editor, R037 O6) are synchronized video with audio, which is 1.2.2/1.2.3/1.2.5.

### 1.2.2 Captions (Prerecorded) (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F26 (Major)
- **Remarks:** The only prerecorded video in the sample — YouTube embeds in the expanding area under Library on the Assignment Editor — has captions, but they are YouTube auto-generated (reviewer, 2026-09-15; R037 O6, NH1 partial). Captions exist for every video seen, hence Partially rather than Does Not Support. Vendor-claim discrepancy.

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 1.3.1 Info and Relationships (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F1, T1-F2, V-F1, V-F2 (Minor), V-F5, V-F7, V-F9, V-F11, V-F13, V-F30 (Minor), V-F28
- **Remarks:** 2026-09-14 S1 confirmed with NVDA (R015): no headings/landmarks, grids told apart by position, editors unlabelled — V-F1, V-F2, V-F7 now stand on both Class Management pages. [provisional — S1 and S2 confirmed; other views pending confirmation of axe results] 2026-09-10 NVDA on S2: no programmatic headings (visual titles are focusable divs); DevExpress grids carry identical generic captions (headers are associated per cell); popup form labels unassociated. axe reports the same pattern on all 14 sampled views (R001–R014, unconfirmed). Vendor-claim discrepancy.

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
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F31 (Major)
- **Remarks:** Decided 2026-09-21 on the reviewer's grayscale pass (W32), which is the human confirmation the four measured NC2 fails had been waiting for. Colour is the only visual carrier in four separate places, and two of them are information the student must act on: on **Take Assignment** the randomised variable values — the numbers that go into the calculation — and the hint deduction percentages that say what help costs (R109 O5); on **View Assignment Solutions** the same orange-red number token inside the worked solutions (R110 O5); on the **Calendar** the event bar carrying an assignment's name and the days it spans, which "fails totally" (R102 O3); on **Class Management** the headings that label the two grids (R099 O4). The problem-navigator **status marks pass** — carried by a symbol — which is both the exception and the fix. Extended 2026-09-21 to **View Printable Assignment** (the same `#FF6347` on the same randomised values, 10 of them) and **Student Practice Area** (the `#EFBB75` section heading) under the reviewer's ruling that the styles are shared, applied only after measuring which tokens each view actually uses. The same measurement **cleared** Sign in and Password reset: their only shared token is teal on headings and field labels, words that already say what they are, so NC1 passes there. Separately measured and still open for the reviewer's eye: NC2, links told from their surrounding text by colour only, failing on S4, S7, S8 and S13 (W41, W73) — those will add to this outcome, not change it. Vendor-claim discrepancy.


### 1.4.2 Audio Control (Level A)
- **Outcome:** Not Applicable (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-15 by the assistant] No audio plays automatically anywhere in the sample: the only media found (YouTube embeds under Library on the Assignment Editor, an instructor view now outside the sample) "do not autoplay" (reviewer, 2026-09-15; R037 O6), and the probe found no media on the student-facing views.

### 2.1.1 Keyboard (Level A)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F3 (Minor), V-F28 (Blocker for the Student Practice Area — 2026-09-15; outcome to be re-rated by the reviewer: a student-facing page whose content is unreachable by keyboard argues for Does Not Support)
- **Remarks:** Reviewer's ruling 2026-09-14: the Accessibility Mode page is accepted as a conforming alternate version, so the standard page's mouse-only row menu is a barrier, not a task stop — Partially Supports. In standard mode the assignment row's action menu — the only route to Take Assignment, View Grade Report and the other row actions — opens by mouse click only; nothing in the row is focusable and no key opens it (R015 O10). The Accessibility Mode page provides an operable Actions select + Go (R016 O13), so the functionality is reachable only after switching modes. Elsewhere the keyboard holds: on Take Assignment every widget exercised (symbol palette, keypad, drag-and-drop alternative form, free-body diagram) was operable without a mouse (R017 O20–O21, R018). Vendor-claim discrepancy.

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
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F18 (Minor)
- **Remarks:** 2026-09-21: **four** of the sampled views declare no `lang` — the password reset page (S14) joins them, measured the day it was sampled (R121 O6). Earlier, 2026-09-14: three of the fourteen sampled views declare no `lang` — Take Assignment (S3), Sign in (S7), the Edit Class popup (S11); the other eleven declare `en` (probe runs R015 … R093). Confirmed on the reviewer's delegation ("your call"); Minor because an English default voice masks it. Vendor-claim discrepancy.

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
- **Task findings:** V-F5, V-F13, V-F30 (Minor)
- **Remarks:** 2026-09-21: **NV6 now fails on every sampled view that has form fields** — S1, S2, S3, S12 and S14 (R015, R016, R017, R059, R121). The pattern is one mechanism: the application lays its forms out in tables and lets the surrounding table text stand in for a label, so the screen reader announces context rather than a name. Newest instance is the password-reset user-name field (V-F30), where the reviewer's ruling is that the table read-out does carry the meaning — "accessible, but not best practice" — which is why the criterion stays **Partially Supports** rather than dropping to Does Not Support: in each case a name of some sort reaches the user, just not the visible label. Earlier, [provisional] 2026-09-10 S11 popup forms: labels are unassociated table-cell text. Instructor pages show the same (axe R006 59 fields, unconfirmed — those views left the sample 2026-09-15).

### 3.3.7 Redundant Entry (Level A)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 4.1.2 Name, Role, Value (Level A)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** T1-F1, T1-F3, V-F3, V-F5, V-F6, V-F7, V-F8, V-F11, V-F13, V-F16, V-F30, V-F28
- **Remarks:** [provisional] 2026-09-10 S2: skip controls exposed as links though they act as buttons; per-row Actions select without a name; popup inputs without names. 2026-09-14 S1 (R015): the standard-mode row action menu has no control at all (T1-F3); the grids' expand glyphs are clickable images with no role or name (V-F16); the DevExpress editors confirmed unlabelled (V-F7). 2026-09-17, sweep triage closed on S1 and S3 (R001, R004): the unnamed answer radios are confirmed (V-F11, R017 O6/O9) and the unnamed jump-point buttons are confirmed (V-F8, R015 O9 / R017 O2) — both were the outstanding items here. **V-F29 was raised here on 2026-09-17 and withdrawn on 2026-09-21**: the header logo link is focusable inside `aria-hidden`, but the reviewer's NVDA announces it in full at that stop ("The ExperTa graphic visited link"), so name, role and state are exposed and 4.1.2 is not failed by it. It survives as an advisory only. Still open: unlabeled DevExpress editors on the instructor pages — those views were removed from the sample 2026-09-15, so they stay unconfirmed and are reported as instructor-facing. Vendor-claim discrepancy.

---

## Table 2: Success Criteria, Level AA

### 1.2.4 Captions (Live) (Level AA)
- **Outcome:** Not Applicable (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-15 by the assistant] No live audio or video in the product (NH2 n/a on every view; the discovered embeds are prerecorded).

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
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F17 (Minor)
- **Remarks:** 2026-09-14: the sign-in "User Name:" field carries no `autocomplete` token (measured, R098 O3); the reviewer confirms there is no app-specific autocomplete and that Chrome's password manager still fills the field, hence Minor. No other field in the sample collects the user's own data (the instructor pages hold class and assignment data). Vendor-claim discrepancy.

### 1.4.3 Contrast (Minimum) (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F23 (Major), V-F24 (Major — text inside the Problem 1 and 6 figure images)
- **Remarks:** Most body text and controls pass; the product's section-heading and caption colours (orange `#EFBB75` 1.74:1, `#E58F65` 2.48:1, `#DB715C` 3.21:1, teal `#48848C` 4.23:1), its grey 12 px notice text (`#808080` 3.94:1) and the coloured values students act on (deduction % `#FF9900` 2.14:1; red variable/MathJax values 2.94–3.99:1) fall below 4.5:1. Confirmed by eyedropper on Class Management 2026-09-15 (R019 O6); axe measured the same colours on 11 of 14 views; the remaining pages are confirmed one by one in walkthrough W43–W55. Vendor-claim discrepancy.

### 1.4.4 Resize Text (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F25 (Major)
- **Remarks:** Text resizes to 400 % without loss on Class Management (both modes), Take Assignment, View Grade Report and the Assignment Editor (LV2 pass, reviewer 2026-09-15). The Class Menu popups do not: above 175 % zoom the Edit Class popup's lower part and its Save / Cancel are unreachable because the page is scroll-locked behind the modal (R078 O5). Vendor-claim discrepancy.

### 1.4.5 Images of Text (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F24 (Major)
- **Remarks:** The problem figures on Take Assignment (and the same images on the solutions and printable views) are raster images containing mathematical text that blurs at 400 % zoom (R083 O6, reviewer 2026-09-15: "the blurry images do contain text, usually math"); the image form is not essential — the page renders its other mathematics as MathJax text. Confirmed again on View Grade Report, which repeats the figures (R030 O5). Class Management, both modes, has no images of text (R019, R024 LV9 pass). Vendor-claim discrepancy.

### 1.4.10 Reflow (Level AA)
- **Outcome:** Does Not Support
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F19 (Major), V-F25 (Major — the Edit Class popup is unreachable above 175 % zoom)
- **Remarks:** Product-wide: a fixed 1300 px container on every sampled page, so nothing reflows at 320 CSS px / 400 % zoom (LV1 measured fail on all 14 low-vision runs, 2026-09-11; reviewer confirmed at real 400 % zoom on Class Management and Take Assignment, 2026-09-15: "nothing is hidden or lost at 400%, but no reflow"). Content is not lost (LV2 pass on S1, S3), which is why the finding is Major rather than Blocker; the failure is the two-dimensional scrolling itself, which 1.4.10 forbids for non-exempt content. Vendor-claim discrepancy.

### 1.4.11 Non-text Contrast (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F27 (Minor)
- **Remarks:** Controls pass 3:1 on Class Management (both modes), Take Assignment and the Assignment Editor (LV5 pass, reviewer eyedropper 2026-09-15). On View Grade Report the grade tables' cell borders and on the Calendar the month grid's lines fall below 3:1 (R030 O8, R042 O8). Vendor-claim discrepancy.

### 1.4.12 Text Spacing (Level AA)
- **Outcome:** Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** The probe measured newly clipping containers under the override on four views (Class Management both modes: the assignment row's date cells lose their AM/PM and the "Weight" header a letter; Take Assignment: the assignment-code box empties; Calendar: a scrollbar covers half of each Saturday date) — photographed in `R019-textspacing-5.png`, `R083-textspacing-2.png`, `R042-textspacing-1.png`. The reviewer looked and ruled 2026-09-15: "no issues noted with text spacing" — not rated a loss of content or functionality. Ten views tolerate the override outright. Recorded as Supports on that ruling; the measurements stay in the runs (O3/O9 on R019, O3/O7 on R083, O3/O5 on R042, O3 on R024) should the ruling be revisited.

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
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F28
- **Remarks:** Focus is visible on every Tab stop of Take Assignment (R018, keyboard) and at 400 % zoom on Class Management, Take Assignment, View Grade Report, the Calendar and Sign in (LV7 pass, 2026-09-15). On the Student Practice Area "tabbing focus is lost outside of the initial buttons and dropdowns" (R063 O4) — focus goes nowhere visible once the grid should take it. Vendor-claim discrepancy.

### 2.4.11 Focus Not Obscured (Minimum) (Level AA)
- **Outcome:** Supports (provisional)
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:**
- **Remarks:** [provisional — drafted 2026-09-15 by the assistant; reviewer confirms] Nothing sticky or floating hides the focused element: at 400 % zoom the focus ring stayed visible and unobscured on Class Management (both modes), Take Assignment, View Grade Report, the Calendar and Sign in (LV7 pass, reviewer). The MO4 fail on the Student Practice Area (R063 O4, V-F28) is focus being *absent* on unfocusable content — a 2.4.7 / 2.1.1 defect, not an obscured indicator.

### 2.5.7 Dragging Movements (Level AA)
- **Outcome:** Not Evaluated
- **Vendor claim:**
- **Task findings:**
- **Remarks:**

### 2.5.8 Target Size (Minimum) (Level AA)
- **Outcome:** Partially Supports
- **Vendor claim:** Supports (2026-05-05 VPAT as reported by CSUEB — every answered criterion is Supports/N-A; file not yet imported)
- **Task findings:** V-F21 (Minor)
- **Remarks:** 2026-09-14, reviewer's rulings on the probe's measurements: the Class Management ⋮ menu beside the expand glyph (S1) and the Take Assignment problem-navigator links (S3) have no equivalent on their pages — confirmed; the Assignment Editor spinner/time arrows (S5) are exempt because the values can be typed directly. The other eleven views measured no undersized, unspaced targets. Vendor-claim discrepancy.

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
