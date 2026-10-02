# Reviewer walkthrough — S3 Course player, video lesson "Icebreaker"

Page: `https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123`,
then in the outline: **1 Intro to the Course → Icebreaker**. Lessons have no
address of their own; the player opens on the last-visited lesson, so check
the heading says "Icebreaker" before you start. Classic experience.

Generated 2026-10-02 from `review.py gaps --view S3` after the automated work
(axe R001, probe R016–R021, no-hearing run R064, assistant keyboard walk,
contrast sampling, text-spacing evidence, tree recon). Narrate freely; the
assistant writes each answer into the runs as it lands.

**Where this page already stands.** 44 rows were open; **23 are left**.
Answered by measurement and inspection: title, language, reflow,
orientation, target size, every text's contrast (all solid backgrounds,
all pass), no hover content, no images of text, no shortcuts, no drag,
native controls, skip link, tab order, focus-ring presence, section and
Transcript toggles with Space, "Hide lessons" drawer, no inputs so no
labels/errors, no help, no timer, reachable several ways, no live or
audio-only media, no sound-only feedback. Sweep: no violations.

**Two measured items wait for your ruling:**

- **Text spacing (LV3).** The outline's lesson titles truncate with an
  ellipsis by design (long titles already read "How AI is Changing the Way
  St…" at normal spacing). With the 1.4.12 override 14 of 21 truncate; the
  probe counted 3 *newly* truncated. Nothing else clips. Evidence:
  `R017-icebreaker-text-spacing.png`. Is truncation of titles that the
  design already truncates a loss of content under 1.4.12?
- **Enter on a lesson button.** My synthetic Enter did not switch lessons
  (a pointer does). On My Courses the same automation limit turned out to
  be nothing. Please confirm with a real keyboard (W9).

**The vendor claim at stake on this page:** 1.2.2 captions (you reported
open captions burned in), 1.2.3 / 1.2.5 audio description ("narration
describes on-screen content" per the ACR), and the transcript as media
alternative.

---

## Part A — NVDA, no-vision (run R016) — Icebreaker lesson [S3]

### W1 — On load (NV7, NV3 current state)
**Do:** Open the course from My Courses → Start course; make sure Icebreaker
is the lesson shown (click it in the outline if not). Reload the page.
**Tell me:** what NVDA announces on load and where focus is (the start
point appears to be the current lesson's outline button — is "Icebreaker,
current" spoken?).
**Feedback:** _(pending)_

### W2 — Title, landmarks, headings (NV2; settles the sweep's W3)
**Do:** `Insert+T`; `D` through landmarks; `Insert+F7` → Headings.
**Tell me:** the title; the landmarks (expected: banner, navigation "Main",
main, complementary with a navigation "Course outline"); the headings list —
expected **only one**, h1 "Icebreaker" (the course title and the section
label are not headings). Is one heading enough to navigate this page, or
should the outline sections be headings?
**Feedback:** _(pending)_

### W3 — The outline on focus (NV3, NV8)
**Do:** `Tab` through the outline: a section button (e.g. "2 What is AI?")
and two lesson buttons.
**Tell me:** how a section announces (name + "0/8 lessons" + collapsed /
expanded?); how a lesson announces — the tree names it "Icebreaker 0m";
does the "0m" read sensibly? is the current lesson marked ("current")?
is a completed lesson distinguishable from an uncompleted one by name or
state, not just by icon?
**Feedback:** _(pending)_

### W4 — Open a lesson by keyboard (NV7, CO8; MO2) — KEY STEP
**Do:** `Tab` to "How AI is Changing the Way Students Learn", press
`Enter` (then `Space` if nothing). Then back to "Icebreaker" the same way.
**Tell me:** does the lesson change; what NVDA announces (new heading? the
page does not navigate — its title stays the course title); where focus is
afterwards.
**Feedback:** _(pending)_

### W5 — The video (NV3, NV11, NH1) — KEY STEP for the vendor claims
**Do:** `Tab` to the video; `Space` to play; `Tab` into the control bar and
through its buttons; pause. Then watch the whole 37-second video once
with sound off, and once with sound on.
**Tell me:** (a) how the video and its controls announce (play/pause,
seek, mute, fullscreen); (b) sound off: are the burned-in captions
accurate and complete for the whole video? (c) sound on: does the
narration describe what is on screen ("Best Friday Ever…", the alarm
clock), as the vendor's ACR claims, or is there visual content the audio
never mentions?
**Feedback:** _(pending)_

### W6 — The Transcript (NV3 state, NV11)
**Do:** `Tab` to "Transcript", `Space` to open, read it with the arrows,
`Space` to close.
**Tell me:** the announced state (collapsed/expanded); whether the
transcript matches the audio; whether it also describes the visuals (it is
the media alternative the ACR relies on for 1.2.3).
**Feedback:** _(pending)_

### W7 — Reading order, images, links (NV4, NV5, NV10)
**Do:** `Ctrl+Home`, `Down arrow` to the bottom. `Insert+F7` → Links.
**Tell me:** the order (header → outline → lesson body?); anything
announced as a graphic (there is no `<img>`; the video is "Icebreaker
video"); the links list (My Courses ×2, Certificates, Profile, skip link).
**Feedback:** _(pending)_

### W8 — "Complete & continue" (NV7, NV3; CO8, CO11)
**Do:** `Tab` to "Complete & continue". **Press it only if you are willing
to mark Icebreaker complete** — progress is recorded on the test account
and the run will say so. If you press it:
**Tell me:** what is announced; where focus lands (next lesson? its
heading?); whether the outline updates the completed state and how a
completed lesson now announces (feeds W3).
**Feedback:** _(pending)_

### W9 — Forms and errors (NV6, NV12)
No form on this page. Say "none".
**Feedback:** _(pending)_

## Part B — Zoom, low-vision (run R017) — Icebreaker lesson [S3]

### W10 — 400 % in a 1280 px window (LV2, LV7) and the LV3 ruling
**Do:** `Ctrl+plus` to 400 %. Open the outline (the "Lessons" drawer at
narrow widths), `Tab` through it, play a few seconds of video, open the
Transcript.
**Tell me:** anything lost, overlapped or clipped; the focus ring at every
stop; the burned-in captions' legibility at that zoom (note for 1.4.4: they
scale with the picture, not with text); and your **LV3 ruling** on the
truncated outline titles (see the top of this file).
**Feedback:** _(pending)_

### W11 — Component contrast (LV5)
**Do:** Eyedropper at 100 %: the progress bar track/fill, the current-lesson
highlight, the lesson status circles, the Transcript icon, the video's
control bar (user-agent).
**Tell me:** your 1.4.11 call. Evidence: `R017-icebreaker-1280.png`.
**Feedback:** _(pending)_

## Part C — Grayscale, no-color (run R021) — Icebreaker lesson [S3]

### W12 — OS grayscale (NC1, NC3)
**Do:** `Win+Ctrl+C`. Look at the outline (current lesson, completed vs not
if W8 was pressed), the progress bar, the video controls.
**Tell me:** are the current and completed states distinguishable without
colour (icon fill/shape, highlight block)? Everything operable?
**Feedback:** _(pending)_

## Part D — Physical keyboard (run R019) — Icebreaker lesson [S3]

### W13 — Focus ring and operation (MO4, MO2) — KEY STEP (with W4/W5)
**Do:** Pointer aside: `Tab` through outline, video, control bar,
Transcript, Complete; `Space` on a section to collapse/expand; `Enter`/
`Space` on a lesson; `Space`/arrows inside the video control bar.
**Tell me:** ring visible at every stop (screenshots `R019-walk*.png` say
yes); every control operates; nothing needs the mouse.
**Feedback:** _(pending)_

## Part E — Cognition (run R020) — Icebreaker lesson [S3]

### W14 — Consistency, context, flashing (CO1, CO8, CO12)
**Tell me:** is the player identical for the article lessons (S4, R1) —
same outline, header, Complete button; does opening a lesson or completing
one move you somewhere unexpected; does the video contain any flashing.
**Feedback:** _(pending)_

## Part F — No-hearing (run R064) and sweep (run R001)

### W15 — Captions (NH1) — from W5(b)
**Feedback:** _(pending — filled from W5)_

### W16 — Sweep W2 and W3
W2 closes from W5(b) (axe's `video-caption` warning is settled by your
captions judgement); W3 from W2 (structure).
**Feedback:** _(pending — filled from W2/W5)_

---

## Close-out (assistant)

1. Every Feedback line filled or skipped with a reason.
2. Write-back: R016 / R017 / R019 / R020 / R021 / R064 rows and
   observations → `close-run` each → R001 W2/W3 → findings into `04` §B
   (View S3) → rollup in `05` (1.2.2, 1.2.3, 1.2.5, 1.4.12, 2.1.1 as
   decided) → 03 §2.6 recon items (captions, duplicate outline, lesson
   names) resolved.
3. `close-page S3`, `validate`, regenerate both reports, `next` (S4, the
   article lesson, shares this player — its walk will be shorter).
