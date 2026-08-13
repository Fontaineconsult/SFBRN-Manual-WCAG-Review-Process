# Test Run R010 — S1

| | |
|---|---|
| **Run ID** | R010 |
| **Date/time** | 2026-08-06 12:15 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | assistant (Claude, Chrome extension; DOM/animation instrumentation) |
| **Result** | Works |

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | pass | **closed 2026-08-13** — reviewer cross-view confirmation after S1–S4 all tested (R029 O5): consistent |
| CO2 — Help (if offered) appears in a consistent location | pass | **closed 2026-08-13** — consistent location across views (R029 O5); help *content* (C7) still unopened, which is a scope note, not a CO2 failure |
| CO3 — Labels and instructions make the required input clear | pass | O2 + 2026-08-13 cross-view: everything labeled/icon/tooltip |
| CO4 — Errors suggest how to fix the problem | n/a | no error path on S1 — task-scoped (T1/T2); routed |
| CO5 — Previously entered information is not demanded again | n/a | no multi-step re-entry on S1 — process-scoped |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | n/a | no authentication on S1 — sign-in flow C2/A4, unsampled |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | pass | O1 + 2026-08-13: reviewer blanket confirmation after dozens of loads — nothing moving or blinking; 2.2.1 long-idle noted at criterion level |
| CO8 — Focus/input does not trigger unexpected context changes | pass | closed 2026-08-13 — reviewer: no unexpected context changes across all sessions (R034-R036 closure) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [clarified] (state: default, steady state after load — CO7 / 2.2.2):
  the home search bar carries a **rotating placeholder** ("Search for
  *images*" → "*popular templates*" → "*seasonal templates*", the trailing
  word swapped inside `x-rotating-text`). Recorded in exploration (03 §2.6)
  and queued for W20 as a Pause/Stop/Hide question. Three instruments now
  disagree with the assumption that it rotates continuously:
  1. `document.getAnimations({subtree: true})` at 68 s after load:
     **0 animations total, 0 running, 0 with infinite iterations** —
     page-wide, not just the rotator. No CSS animation, CSS transition, or
     Web Animations API motion is active anywhere on S1.
  2. Deep text sampling of the rotator (shadow-piercing) every 500 ms for
     16.3 s: **no change**.
  3. Same after a fresh reload, every 800 ms from t=16.3 s to t=43.5 s
     (27 s): **no change**.
  The rotator retains the CSS classes `item animating-out` (word
  "templates") and `item animating-in` (word "images") **permanently** —
  they are stale leftovers, not evidence of motion in progress. This also
  explains axe's two `color-contrast` *incomplete* nodes ("partially
  obscured by another element", R009 O9b): both words are in the DOM at
  once, overlapping.
  - **Open sub-question (honest limit):** the first ~16 s after load could
    not be sampled — `navigate` returns only after load and the injection
    round-trip costs that window, so any rotation that runs and stops early
    is invisible to this instrument. 2.2.2 applies only to motion that
    **starts automatically and lasts more than 5 seconds**. If the rotation
    finishes within ~5 s of load, 2.2.2 does not apply at all and this
    closes as a pass.
  - Classified: CO7 / WCAG 2.2.2 / partial — no finding raised. Reviewer
    step (replaces W20's vague "pause-ability" item): **reload S1, watch the
    bold word in the search bar, and report how many times it changes and
    whether it settles — and roughly how long that takes.** Also unresolved
    under CO7: 2.2.1 time limits (needs a long idle session; not tested).
- O2 [classified] (state: default — CO3, and a 2.5.3 candidate): the search
  input's accessible name is `aria-label="Search for templates and more"` —
  stable, meaningful, and **not** the rotating text. The rotator itself is
  `aria-hidden="true"` and sits in no live region. Two consequences:
  (a) CO3/3.3.2 is satisfied for this control, and (b) the rotating
  placeholder is **not** announced, so the NV7 "chatty placeholder" worry
  queued in W8 is unfounded — worth confirming by ear, but the DOM says the
  rotator is invisible to AT.
  - Classified: CO3 / WCAG 3.3.2 / partial — no finding
  - **Spun off:** the *visible* text ("Search for popular templates") is not
    contained in the accessible name ("Search for templates and more").
    That is the shape 2.5.3 Label in Name guards against — a speech-input
    user saying "click Search for popular templates" would not match. Held
    as a **candidate**, not a finding: whether a rotating placeholder counts
    as a "label" under 2.5.3 is a judgment call, and the vendor claims
    Partially Supports for 2.5.3. Recorded in R001 O8 for the W5 JAWS pass,
    since 2.5.3 sits under NV3.

## Notes

Assistant-driven structured inspection, no reviewer present. Instrument:
Chrome extension, page-context JavaScript on the reviewer-authenticated
default-profile session (separate from the axe debug profile).

Scope limit that is intrinsic, not an oversight: **six of the eight
cognition checks cannot be answered from a single view.** CO1/CO2 are
consistency criteria (3.2.3/3.2.4/3.2.6) that need at least a second view
to compare against; CO4/CO5 need a multi-step process with an error path
(P1/P2); CO6 needs the sign-in flow (C2/A4), which is not yet sampled.
These stay blank deliberately — filling them from S1 alone would be
fabrication. Consequence: **S1's cognition cell cannot be closed until
either W20 runs or a second view is tested**, and the run Result stays
unset until then.

`getAnimations({subtree: true})` covers CSS animations, CSS transitions,
and the Web Animations API. It does **not** see `setInterval`-driven DOM
swaps, animated GIF/WebP, video, Lottie-on-canvas, or SVG SMIL. For the
rotator specifically the setInterval case is separately excluded by the two
text-sampling windows in O1; page-wide, the zero result is strong but not
total evidence of no motion.

## Evidence files in this folder

- (screenshots/exports named R010-<what>.png)

## Findings raised from this run

- none. Two items routed instead: the 2.2.2 load-window question (reviewer
  step, O1) and the 2.5.3 Label-in-Name candidate (R001 O8 → W5).
