# Reviewer walkthrough — S1 Sign in (`https://learn.essentials-ai.com/login`)

Generated 2026-09-30 from `review.py gaps --view S1` after the automated work
(axe R006, probe R050–R056, assistant keyboard walk and contrast sampling).
Work top to bottom and narrate freely; the assistant records feedback in
place and writes it into the runs, findings and rollup in the same breath.
Every step names the page in words; the sample code is in brackets.

**Where this page already stands.** 39 rows were open this morning; **24 are
left**, all of them things only a person can judge. Answered by measurement
and inspection, with the basis in each run: title, language, no media, no
speech, no motion, target size, reflow, text spacing, orientation,
autocomplete, no animation, no single-key shortcuts, no drag, native
up-event controls, no repeated blocks, tab order (Email → Password → Show
password → Forgot your password?), focus-ring *presence* at 100 %, contrast
of every text (all pass except the Email placeholder at 3.5:1 — measured
fail awaiting you), no hover content, no images of text, no help offered,
no timer, no repeated entry. The Sign in button is natively **disabled**
until both fields hold a value, and the fields are **not inside a `<form>`**
— so submitting, Enter-to-submit and every error behaviour need your
credentials.

**Window to use.** The signed-out debug window (port 9223) is open on the
sign-in page and must **stay signed out** — probes for the sign-in views run
there. For the steps that need credentials (W6–W8, W13) use an **incognito
window of your everyday Chrome** so nothing persists. Close the assistant
side panel and DevTools before the JAWS steps so speech is product-only.

---

## Part 0 — Setup (unblocks the record)

### W1 — Tool versions for 03 §1.5
**Do:** Read off JAWS version and build (JAWS → Help → About), Chrome version
(`chrome://version`), Windows build.
**Tell me:** the three version strings.
**Feedback:** 2026-09-30 — **NVDA 2024.1** (baseline B5, 03 §1.3/§1.5). _Chrome and Windows build strings still pending._

## Part A — JAWS, no-vision (run R050) — the Sign in page [S1]

### W2 — Title, landmarks, headings (NV1 wording, NV2)
**Do:** Load `https://learn.essentials-ai.com/login` signed out. `Insert+T`
for the title. `R` / `Shift+R` to cycle landmarks, then `Insert+F6` for the
headings list, `H` to move by heading.
**Tell me:** the title as spoken; which landmarks JAWS finds (the tree shows
only a `main`); the headings list (expected: one heading, "Sign in", level 1).
Why it matters: NV2 decides 1.3.1 / 2.4.1 for this page; the sweep saw one
main landmark and one h1 and W3 needs JAWS to agree.
**Feedback:** 2026-09-30 — done: title "Sign in Readiness OS", "Main landmark", one heading "Sign in" level 1 → NV2 pass; W3 on the sweep pass.

### W3 — Every control on focus (NV3, NV6, CO3; settles axe R006 O1) — KEY STEP
**Do:** From the top, `Tab` through the four stops. At each, wait for JAWS
to finish, then `Insert+Space, H` to copy the speech history.
**Tell me:** exactly what is announced for (1) the Email field, (2) the
Password field, (3) the Show password checkbox, (4) the Forgot your
password? link — and whether the **Sign in button is announced at all**
while the fields are empty (it is disabled; expected: not a Tab stop).
Why it matters: the accessibility tree names the password field
**"Password Show password"** because its label wraps the checkbox's label
too — axe flagged this as `form-field-multiple-labels` (3.3.2). If JAWS says
"Password Show password edit", tell me whether that wording would mislead
a user; that decides W2 on the sweep and NV6/CO3 here.
**Feedback:** 2026-09-30 — done: all four stops recorded (R050 O13/O14) → NV3 pass; "Password Show password" ruled a **Minor finding → V-F2 (4.1.2)**; NV6 partial, CO3 pass.

### W4 — Reading order and images (NV4, NV5, NV8)
**Do:** `Ctrl+Home`, then `Down arrow` line by line to the bottom.
**Tell me:** the order things are read (logo → "AI Essentials" → "Readiness
· Learning · Growth" → Sign in → Email … → footer line "Access is
provisioned by your program administrator"?); what the logo is announced as
(expected: "AI Essentials graphic"); anything that only makes sense visually.
**Feedback:** 2026-09-30 — done: logo "AI Essentials" graphic; arrows follow the correct order; nothing position-only → NV4, NV5, NV8 pass.

### W5 — Links list (NV10)
**Do:** `Insert+F7`.
**Tell me:** the links listed (expected just "Forgot your password?") and
whether the text alone tells you where it goes.
**Feedback:** 2026-09-30 — done: only "Forgot your password?" → NV10 pass.

### W6 — A failed sign-in (NV7, NV12, CO4, CO8) — KEY STEP
**Do:** In the incognito window with JAWS running: type a wrong e-mail
(e.g. `nobody@example.edu`) and any password. Note whether the Sign in
button becomes available once both fields have text. Press **Enter** while
in the Password field. If nothing happens, `Tab` to Sign in and press
`Space`.
**Tell me:** (1) did Enter submit? (2) what JAWS announced when the error
came back — was it spoken automatically, did focus move, and where to?
(3) the error text: does it say which field and what to fix? (4) did typing
in a field change anything unexpectedly (a redirect, focus jump, form
reset)?
Why it matters: the page has an empty `alert` live region; if the error is
injected there JAWS should speak it unprompted. That is NV7/NV12 (4.1.3,
3.3.1) and CO4 (3.3.3). The vendor claims all four Support.
**Feedback:** 2026-09-30 — done: error "That email and password don't match an account. Check them and try again." spoken automatically, same as the visible text, focus did not move → NV7, NV12, CO4, CO8 written.

### W7 — Show password (NV3 state, MO2)
**Do:** `Tab` to the Show password checkbox, press `Space`, then `Shift+Tab`
to the Password field.
**Tell me:** the checkbox's announced state before/after; whether the
password is now announced as a normal edit (masking off); whether Space
toggled it (my synthetic Space did not, which may just be automation).
**Feedback:** 2026-09-30 — done: Space activates Show password → MO2 pass (with W12).

### W8 — A successful sign-in (NV7, CO8; sign-in process step 1)
**Do:** Enter the test account's credentials and press Enter.
**Tell me:** what JAWS announces on landing (expected new title "My Courses
· AI Readiness OS"); where focus lands on the new page; anything spoken
in between. Then **sign out** (avatar "TU" → Sign out) so the incognito
window is clean.
Why it matters: this is step 1 of the sign-in process P-sign-in that every
task starts with; the announcement on landing is 4.1.3 / 3.2.2 evidence.
**Feedback:** 2026-09-30 — done: "My Courses AI Readiness OS" announced on landing → NV7. _Remember to sign the incognito window out._

## Part B — Zoom, low-vision (run R051) — the Sign in page [S1]

### W9 — 400 % in a 1280 px window (LV2, LV7)
**Do:** Signed-out window, resize to 1280 px wide, `Ctrl+plus` to **400 %**.
`Tab` through the four stops at that zoom.
**Tell me:** whether anything is clipped, overlapped or cut off; whether the
whole page is one column with only vertical scrolling; whether each focus
ring is still visible and not hidden under anything at 400 %.
**Feedback:** 2026-09-30 — done: no render issues at 400 %; focus ring renders fine at 400 % → LV2, LV7 pass (R051); MO4 pass (R054).

### W10 — Two contrast calls (LV4 measured fail, LV5)
**Do:** At 100 %, with Colour Contrast Analyser or the DevTools eyedropper:
(a) the Email field's placeholder text "you@school.edu" — grey
rgb(139,135,149) on white; I measured **3.5:1** (needs 4.5:1).
(b) the **edge** of the Email and Password fields against the white card —
the border is 0.6 px rgb(234,230,242), ≈ 1.15:1; the field boundary is
essentially invisible until focused. Evidence: `R051-signin-1280.png`.
**Tell me:** (a) confirmed / exception / can't reproduce — and if confirmed,
Minor or Major (placeholder is the only format hint on the page);
(b) your 1.4.11 call on the field boundary: does the field need the border
to be identifiable, or does the label above suffice?
**Feedback:** 2026-09-30 — (a) confirmed → V-F1 (Minor, 1.4.3). (b) "label is fine for 1.4.11" → LV5 pass.

## Part C — Grayscale, no-color (run R056) — the Sign in page [S1]

### W11 — OS grayscale (NC1, NC3)
**Do:** `Win+Ctrl+C` (grayscale filter). Look at the page empty, then with
both fields filled (button enabled). `R056-grayscale.png` is the emulated
capture of the empty state.
**Tell me:** can you tell the disabled button from the enabled one without
colour (luminance change)? is anything else colour-only — required fields,
the link, an error message's red? Everything still operable?
**Feedback:** 2026-09-30 — done: "yes there is a difference in grey" → NC1, NC3 pass.

## Part D — Physical keyboard confirmations (run R054) — the Sign in page [S1]

### W12 — Focus indicators and operation with a real keyboard (MO4, MO2)
**Do:** Pointer aside. Reload, `Tab` through every stop; fill both fields,
`Tab` again to confirm the Sign in button is now a stop with a visible ring;
`Enter` in the Password field and `Space` on the button.
**Tell me:** a visible indicator at every stop, including the enabled Sign
in button; Enter submits from the Password field (the fields are not in a
`<form>`, so this is the thing to check); Space toggles Show password;
Enter activates Forgot your password?.
Evidence already in the run: `R054-tab01.png` … `R054-tab04.png` (rings at
100 % from the automated walk).
**Feedback:** 2026-09-30 — done: tab order as expected, Enter submits, Space toggles Show password, ring fine → MO2, MO4 pass.

## Part E — Cognition, inspection (run R055) — the Sign in page [S1]

### W13 — Consistency and authentication (CO1, CO6; CO3/CO4/CO8 come from W3/W6)
**Do:** Compare the sign-in page with the Reset your password page
(`/forgot-password`) and with the signed-in shell (My Courses). Try pasting
a password and using the browser's password manager on the Password field.
**Tell me:** are the two signed-out pages one design, and does the signed-in
product identify the same things the same way? Does signing in require
anything beyond e-mail + password (no CAPTCHA, no code to transcribe,
paste and autofill allowed)?
**Feedback:** 2026-09-30 — done: same design for reset; password manager and paste work, no CAPTCHA → CO1, CO6 pass.

## Part F — Sweep triage (run R006) — the Sign in page [S1]

### W14 — W1, W2, W3
No decision needed from you beyond W2/W3 above: the sweep reported **no
violations** (W1 passes trivially, noted), one incomplete
(`form-field-multiple-labels`, settled by W3's announcement), and structure
(one main, one h1) that W2 cross-checks. The assistant closes R006 from your
W2/W3 feedback.
**Feedback:** 2026-09-30 — W1, W2, W3 all pass; R006 closed.

---

## Close-out (assistant)

**2026-09-30:** every Feedback line above is filled. R006, R051, R054, R056 closed earlier; R050 closed Works with issues (V-F2), R055 closed Works. `close-page S1` run next; findings V-F1 (1.4.3) and V-F2 (4.1.2) rolled up in 05. Still owed for the record: Chrome and Windows build strings (W1).

### Original plan

1. Every Feedback line above filled or marked skipped, with the reason.
2. Write-back in order: R050 / R051 / R054 / R055 / R056 rows and
   observations → `close-run` for each with its Result → R006 W1–W3 → any
   finding into `04` §B (View S1) with a Plain summary → rollup in `05`
   (1.4.3 placeholder, 3.3.2 label wording, 3.3.1/3.3.3/4.1.3 from W6,
   2.4.7 from W9/W12, 1.4.11 from W10) → 03 §1.5 versions → 03 §2.6 recon
   items resolved.
3. `review.py close-page 2026-09-essentials-ai-learn S1` must pass before
   the next page is opened. `validate`, then regenerate both reports.
4. Next target: `review.py next` (expected S2 My Courses).
