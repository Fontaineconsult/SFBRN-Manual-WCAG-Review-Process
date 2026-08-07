# Reviewer Session Walkthrough — S1 Home dashboard (2026-08-04)

> ## ⏸ PARTLY SUPERSEDED — read before using
>
> **Testing moved from JAWS to NVDA on 2026-08-06.** Part A's steps were
> written in **JAWS keystrokes** (`R` for landmarks, `Insert+F6`,
> `Insert+Space,H` for speech history) and are **wrong for NVDA**: use `D`
> for landmarks, `NVDA+F7` for the Elements List, and the Speech Viewer
> (`NVDA+N` → Tools) for exact wording. **Never press `Insert+Space` in
> NVDA** — it toggles browse/focus mode.
>
> S1's **no-vision work is complete** under NVDA (run **R012**, Works with
> issues). Run R001 (JAWS) is **suspended** at NV1/NV2 pending the open
> question in `03` §1.3: *is JAWS in scope for this procurement at all?*
> Until that is answered, every no-vision conclusion in this review is
> **NVDA-only** and the report must say so.
>
> **Still open on S1** (needs instruments the reviewer was not in): R002
> low-vision 5 checks · R004 motor 8 checks · R010 cognition 6 checks.
> Cognition needs no setup — and CO1/CO2 (consistency) only became
> answerable once S2 and S3 were tested.


The ordered script for the reviewer-driven remainder of S1
(https://new.express.adobe.com/). Work top to bottom; narrate freely at each
step — the assistant records your feedback in the **Feedback** line, converts
it into observations/check outcomes in the named run, asks only about gaps,
and updates findings (04), the rollup (05), and the enclosure (03) as you go.
You don't need to phrase anything formally; "the flyout stayed open when I
moved onto it" is enough.

Steps are `W#`. Say the step number when you start one. Skip/reorder freely —
just say so.

---

## Setup

### W1 — Record tool versions (feeds 03 §1.5)

**Do:** Check versions: JAWS (Help → About), Chrome (`chrome://version`),
WAVE extension (extensions page), Windows build.
**Tell me:** The four version strings.
**Feedback:** _(pending)_

---

## Part A — R001: JAWS, no-vision (the priority run)

Baseline B1. Screen off or ignored; virtual cursor. Copy exact speech from
Speech History (`Insert+Space`, then `H`) for anything surprising.

### W2 — Page load and title (NV1)

**Do:** Load the page fresh with JAWS running. Listen to what is announced.
**Tell me:** What JAWS says on load; does the title identify the page?
**Feedback:** 2026-08-04 — Page loads; JAWS announces title "Adobe Express"
plus "a lot of other information" from the **Claude for Chrome** extension
UI sharing the browser window — not product content.
NV1 pass on the title itself; environment hygiene note recorded (close or
unfocus the assistant panel during JAWS steps so speech is product-only).

### W3 — Headings and landmarks sweep (NV2) — KEY STEP

**Do:** Press `H` repeatedly to walk headings, then `R` for landmarks/regions.
Also try `Insert+F6` (headings list) and `Insert+Ctrl+R` (regions list).
**Tell me:** Which headings/landmarks exist and in what order — or whether
the page is silent/empty to these keys.
**Why it matters:** Our automation saw a near-empty accessibility tree
(shadow DOM). This step decides whether that's real for AT. Also feeds
V-F3 (2.4.1): do landmarks give SR users a bypass?
**Feedback:** 2026-08-04 — Initial announcement: 3 headings, 2 regions,
1 link. Full `H`-key walk supersedes the count — outline (all reachable):
Adobe Express › [2] Daniel Fontaine › [3] Recent › [1] How would you like
to start? › [2] Upload / Start new design / Edit photos / Set up brand kit /
Generate presentation / Quick edits / File formats / Ways to create /
Templates. → Shadow-DOM concern RESOLVED as tooling artifact; rich, proper
heading structure. Notes: "Recent" sits 3rd in reading order but is
visually the bottom strip (NV5 question → W4); "Ways to create" and
"Templates" sections exist below the fold (enclosure updated). Regions
(`R` walk, supersedes "2 regions"): **Apps [navigation], banner, Primary
[navigation], main, search** — all reachable and labeled. → `main` exists
and the app bar is a labeled nav: SR users CAN bypass via landmarks
(ARIA11), so V-F3 narrows to keyboard-only users — reviewer decision
pending on whether 2.4.1 stands as a failure or becomes an advisory
barrier (see 05 remarks). Still open: 1 link vs 7 DOM anchors → W5.

### W4 — Virtual-cursor read-through (NV5, NV8)

**Do:** From the top, arrow down through the page in reading order.
**Tell me:** Does the read order match the visual order (search → greeting →
start cards → Quick edits → File formats → Recent)? Anything announced only
by position/shape?
**Feedback:** _(pending)_

### W5 — Controls: name/role/value (NV3) — includes trial follow-ups

**Do:** Tab through controls; also virtual-cursor over: the five start cards,
a few Quick edits cards, the left-rail items, the Recent-file card
(axe cleared it — sr-only name — quick sanity-hear only), and the
top-right icons. **axe follow-ups (R009): (a) the community/people icon
button — expected finding V-F4: announces as bare "button" with no name;
(b) the "More apps" button — open it, does the dialog announce; (c) the
account/avatar button — does expanded/collapsed state announce.**
**(d) added 2026-08-06 — the search field, a 2.5.3 Label in Name candidate
that needs your judgment, not just your ears.** Its accessible name is
`aria-label="Search for templates and more"`, but what a sighted user *reads*
in the field is the rotating placeholder — "Search for **popular templates**",
"**seasonal templates**", "**images**". The visible string is not contained in
the accessible name, and it changes over time, so a speech-input user has no
fixed utterance that matches ("click Search for popular templates" would
fail). Good news first: for JAWS this is *correct* behaviour — one stable
label, rotation never announced (rotator is `aria-hidden`). The 2.5.3
question is a separate call: does a rotating placeholder count as a "label"?
Placeholders are not labels for 3.3.2 purposes, and vendor claims Partially
Supports for 2.5.3. **Your call — I've held it as a candidate, not a
finding** (R001 O8).

**Tell me:** Any control announced with a wrong/missing name or role; exact
speech for (a)–(c); and your 2.5.3 verdict for (d).
**Feedback:** _(pending)_

### W6 — Images (NV4)

**Do:** `G` to walk graphics.
**Tell me:** Alt behavior — meaningful alternatives, silent decoratives, or
noise (filenames, "graphic" spam)?
**Feedback:** _(pending)_

### W7 — "Get started" modal via JAWS (NV3, NV7; feeds MO3)

**Do:** Activate "Start new design". Listen to the announcement; walk the
modal; press Esc.
**Tell me:** Is the dialog announced (role, title)? Is focus moved in? Does
Esc close it and is the return point announced? (Trial recon: Esc handling
looks weak elsewhere.)
**Feedback:** _(pending)_

### W8 — Dynamic updates (NV7) + language (NV9)

**Do:** Note anything announced spontaneously (toasts, skeleton loads).
Confirm pronunciation is English.
**Tell me:** Whether updates are announced, over-announced, or silent; any
language oddity.
**Note 2026-08-06 — the "chatty rotating placeholder" worry is probably
unfounded:** the rotator is `aria-hidden="true"` and sits in no live region,
and the search field has a stable `aria-label` ("Search for templates and
more") that is *not* the rotating text (R010 O2). Expect JAWS to announce
one fixed label and never the rotation — one sanity-hear is enough, no need
to hunt for it.
**Feedback:** _(pending)_

### W9 — R001 verdict

**Do:** Gut check the whole view: Works / Works with issues / Broken for a
no-vision user.
**Tell me:** Your verdict + the one worst thing.
**Feedback:** _(pending)_

---

## Part B — R002 completion: real zoom, low-vision

Baseline B3. Set window ~1280px wide (snap to half of the 4K screen is
fine — tell me the actual width), then `Ctrl+plus` to 400%. `Ctrl+0` resets.

### W10 — Reflow at 400% (LV1, LV2)

**Do:** At 400%, scroll the page.
**Tell me:** One-column reflow or two-dimensional scrolling? Anything
clipped, overlapped, or missing (compare: search, start cards, Quick edits,
File formats, Recent, left rail)?
**Feedback:** _(pending)_

### W11 — Focus visibility at zoom (LV7)

**Do:** Still at 400%, Tab through a dozen stops.
**Tell me:** Is the focus indicator always visible and unobscured?
**Feedback:** _(pending)_

### W12 — Confirm V-F1: the hover flyout (LV6 / 1.4.13) — KEY STEP

**Do:** At normal zoom, slowly hover a left-rail item until the "Get
inspired" flyout opens. Then (a) move the pointer *continuously* onto the
flyout; (b) with it open, press Esc; (c) move the pointer away and watch
whether it closes.
**Tell me:** What happens at each of (a), (b), (c). The trial saw: dismissed
on approach, Esc ignored, then stuck open indefinitely.
**Feedback:** _(pending)_

### W13 — Eyedropper contrast (LV4, LV5) — SHORTENED 2026-08-06

**Queue reduced from 15 nodes to 7 — do NOT re-measure the app bar.**
The 8 app-bar labels are settled by exact measurement (11.18:1–11.71:1,
R009 O8): the bar's background is a self-contained SVG, so it was
re-rendered on a canvas and sampled directly rather than estimated. They
pass with ~2.5× headroom.

**Do:** With CCA — only these:
1. The four start-card headings ("Start new design", "Edit photos", "Set up
   brand kit", "Generate presentation") and the "Ways to create" row
   heading. These are the ones no automated method can reach: the card
   colour is painted by a pseudo-element or non-hit-testable image, so
   ancestor-walking returns a bogus "white / 21:1".
2. The "browse" link — spot-check only (already 3.96:1 by two instruments).
3. Left-rail labels; one icon-only control against its background (LV5).
**Tell me:** The measured ratios.
**Feedback:** _(pending)_

---

## Part C — R004 confirmation: physical keyboard, motor

Baseline B2. Mouse out of reach.

### W14 — Confirm V-F3: first-Tab / skip link (MO11 / 2.4.1) — KEY STEP

**Do:** Reload, press Tab once. Then keep tabbing and count stops until
focus reaches Express content (left rail or search).
**Tell me:** Did a skip link appear? How many stops through the Adobe app
bar? (Trial: none, ~15 stops — confirm or refute; vendor claims Supports.)
**Feedback:** _(pending)_

### W15 — Full sweep: reach, operate, order, indicator (MO1/2/4/5)

**Do:** Tab the whole page to the Recent strip. Operate one thing of each
kind: a start card (Enter), a Quick edits card, a "View all" link, the
Recent-file card.
**Tell me:** Anything unreachable, inoperable, indicator-less, or in a weird
order.
**Feedback:** _(pending)_

### W16 — Modal keyboard behavior (MO3) + shortcuts (MO6)

**Do:** Open "Get started" with Enter; Tab around inside; Esc to close.
Then check: any single-character shortcuts active on this page?
**Tell me:** Trap/exit behavior; where focus returns; shortcut findings.
**Feedback:** _(pending)_

### W17 — Targets and gestures (MO7/8) — MO9 DONE 2026-08-06

**Skip the target eyeballing — it is measured.** All 51 interactive targets
on S1 were enumerated and sized (R004 O4): five are under 24px but every one
clears 2.5.8's spacing exception by 4× or more. MO9 = pass at desktop width.

**Do:** Only the two things geometry cannot answer:
1. Confirm the Upload card's drag-drop has the "browse" alternative (MO7 /
   2.5.7) and try click-and-slide-off on a card (MO8 / up-event cancel).
2. **At 400% zoom (fold into W10):** re-check whether those three "View all"
   links still stand clear of neighbouring controls. The spacing exception
   is a *layout* property — reflow can pack them together and turn a pass
   into a fail. This is the one way MO9 could still fail on S1.
**Tell me:** Any drag-only interaction, and whether the "View all" links
crowd at 400%.
**Feedback:** _(pending)_

---

## Part D — Short confirmations

### W18 — NC2 link cues (R003 follow-up)

**Do:** Hover and focus "View all" and "browse".
**Tell me:** Does a non-color cue (underline/weight) appear?
**Feedback:** _(pending)_

### W19 — WAVE sweep of S1 (new run — I'll log it when you start)

**Do:** Run the WAVE extension on the default view; then re-run with the
"Get started" modal open.
**Tell me:** The four summary counts (Errors, Contrast Errors, Alerts,
Features/Structural) per state + each distinct error type. Screenshot the
overlay and details panel into the run folder I name.
**Feedback:** 2026-08-04 — Logged as R007. Summary: 0 Errors, 0 Contrast
Errors, 3 Alerts ("No heading structure", "No page regions", Noscript),
1 Feature (Language), 2 Structural (hidden iframes ×2), 2 ARIA (hidden);
AIM 10/10. **Verdict: instrument-blind** — "no structure" is directly
contradicted by JAWS (13+ headings, 5 landmarks, W3), so WAVE analyzed only
the light-DOM shell; Result recorded as N/A, alerts dismissed, 0-errors NOT
treated as a pass. Ontology + CLAUDE.md updated (WAVE per-view cadence made
explicit; blindness signature + N/A semantics recorded; axe DevTools / IBM
Equal Access noted as shadow-DOM-capable secondary option — reviewer's call
whether to add one to 03 §1.5). Modal-state re-run: moot while blind.
Optional: WAVE overlay screenshots into R007 for the record.

### W20 — Cognition pass (run R010 already logged, partially filled)

**Do:** With me, walk CO1/CO2/CO4/CO5/CO6/CO8 conversationally. CO3 and CO7
are already part-answered (R010) — don't redo them.

**One precise measurement I could not take, worth doing first (CO7 / 2.2.2):**
reload S1 and watch the bold word in the search bar from the moment it
appears. **Tell me how many times it changes and roughly how long until it
settles.** Why it matters: 2.2.2 only applies to motion that starts
automatically and runs **more than 5 seconds**. Instruments say there is no
motion at all in steady state — 0 animations page-wide at 68s, and the text
held still across a 16s and a 27s window — but the first ~16s after load is
invisible to automation (the tool round-trip eats exactly that window), and
the rotator's `animating-in`/`animating-out` classes are stuck on
permanently, so they prove nothing either way. If it settles inside ~5s,
2.2.2 does not apply and this closes as a pass.

**Note:** CO1/CO2 (consistency, 3.2.3/3.2.4/3.2.6) genuinely *cannot* be
answered from S1 alone — they need a second view to compare against. They
will stay open until S2 or S3 is tested regardless of what we do here.
**Tell me:** Answers as we go.
**Feedback:** _(pending)_

### W21 — axe-core sweep of S1 (added 2026-08-04; supersedes WAVE for app views)

**Do:** (CORRECTED — Chrome 136+ ignores the debug flag on the default
profile.) The assistant launches the dedicated testing profile
(`--user-data-dir=%LOCALAPPDATA%\sfbrn-a11y-chrome --remote-debugging-port=9222`);
you sign into Adobe Express in that window once (profile persists). Then I run
`python scripts/axe_scan.py adobe --view S1 --url https://new.express.adobe.com/`
— it logs the run, executes axe-core 4.10.3 inside your authenticated tab
(shadow-DOM capable, unlike WAVE — see R007), saves the raw JSON, and I
record outcomes.
**Tell me:** Just "Chrome relaunched". (Pipeline already smoke-tested
end-to-end on a throwaway instance.)
**Feedback:** 2026-08-04 — DONE (run R009; raw output
`evidence/runs/R009/R009-axe.json`, 1.65 MB). Dedicated profile
required (Chrome 136+ ignores the flag on the default profile — docs
corrected; reviewer signed in once). Results: 3 violations / 3 incomplete /
47 passes. Highlights: `.browse-text` contrast violation **corroborates
V-F2**; unnamed community icon-button → **new finding V-F4** (4.1.2, JAWS
check added to W5); Recent bar sits outside all landmarks (best-practice —
explains W4's reading-order oddity); 15 gradient-contrast nodes = the W13
eyedropper queue; recon item "unlabeled Recent-file link" **refuted**
(name is in an sr-only span). Orphaned R008 (pre-fix connection failure)
marked aborted; script now connects before logging.

---

## Close-out (assistant does; you watch)

- All feedback recorded above and in runs R001–R004 + the two new runs
- Findings V-F1/V-F2/V-F3 confirmed, amended, or withdrawn per your feedback
- 05 rollup and 03 enclosure updated; `validate` re-run
- Decide: is S1 done enough to move to S2 (Explore) with `next`?
