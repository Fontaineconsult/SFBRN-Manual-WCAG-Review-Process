# Test Run R055 — S1

| | |
|---|---|
| **Run ID** | R055 |
| **Date/time** | 2026-09-30 14:09 |
| **View / sample** | S1 |
| **Page URL / location** | https://learn.essentials-ai.com/login |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | inspection (probe measurements kept: CO9, CO12) |
| **Baseline** | — |
| **Tester** | Daniel Fontaine (reviewer, NVDA session + inspection) + assistant (O4); assistant records |
| **Result** | Works |

**Result reasoning.** Cognition inspection of the sign-in page (reviewer with NVDA session plus assistant inspection). Consistent design with the reset page and the signed-in shell, clear labels, an error that says what to do, no unexpected context changes, no help offered (recorded as A2, not a failure here), no timer, no repeated entry, authentication by e-mail and password with password-manager fill and paste, no CAPTCHA.

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | pass | O6, O4 — signed-out pages share one design; components are identified consistently — reviewer |
| CO2 — Help (if offered) appears in a consistent location | n/a | O4 — no help is offered on this view (3.2.6 applies only where help exists; the absence is recorded as A2 in 03 §2.5 and against the vendor's 3.2.6 claim) |
| CO3 — Labels and instructions make the required input clear | pass | O7 — the two inputs are clearly labelled and the example address shows the expected format; the naming defect is recorded under NV6 / V-F2 |
| CO4 — Errors suggest how to fix the problem | pass | O5 — the error tells the user what to do ("Check them and try again"); a credential error cannot say more without weakening security (3.3.3 exception noted) — reviewer, NVDA 2024.1 |
| CO5 — Previously entered information is not demanded again | n/a | O4 — single one-step form; nothing is asked twice |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | pass | O6 — e-mail + password with password-manager fill and paste allowed, no CAPTCHA or memorisation test — 3.3.8 satisfied (reviewer) |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | O4 — no time limit and no moving content on the view |
| CO8 — Focus/input does not trigger unexpected context changes | pass | O5 — no change of context on focus or input; submit only on Enter/button, navigation only on success — reviewer |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | pass | O2 — 2 personal-data field(s) all carry autocomplete: Email=email; PasswordShow password=current-password |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | n/a | O4 — the sign-in page is a step in a process (2.4.5 exemption); reachable by direct address and by redirect |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | O4 — no legal, financial or data-changing submission |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | n/a | O3 — no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash |
**view_probe 2026-09-30:** answered CO9=pass, CO12=n/a by measurement; facts in `R055-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): 2 personal-data field(s) all carry autocomplete: Email=email; PasswordShow password=current-password
  - Classified: CO9 / WCAG 1.3.5 / measured → pass
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash
  - Classified: CO12 / WCAG 2.3.1 / measured → n/a
- O4 [new] (state: inspection of the sign-in view and the password-reset view (S7) side by side): The two signed-out views share one shell (logo, wordmark, tagline, centred card, footer line) and identical field/button styling; there is no navigation on either. No help link, support contact or help text exists on the view (or anywhere in the product — 03 §2.5 A2). No timer, session warning or moving content (probe: timerText empty, animations 0). Nothing on the view is a legal, financial or data-changing submission — signing in changes nothing. The view is reached by its own address and by redirect from every product URL when signed out; as the single entry step of the sign-in process it is exempt from 2.4.5.
- O5 [new] (reviewer, 2026-09-30, wrong password then correct credentials): Error text "That email and password don't match an account. Check them and try again." appears and is announced; focus stays put; typing and submitting caused no unexpected change of context — Enter submits (expected), success navigates to My Courses with its title announced (expected).
- O6 [classified] (reviewer, 2026-09-30): "Same design for reset" — the sign-in and password-reset pages share one design; the signed-in shell identifies My Courses / Certificates / Profile consistently (O4). Authentication: "password manager works and paste, no captcha" — the browser's password manager fills both fields, paste is not blocked, no CAPTCHA or transcription step; NVDA announces "has auto complete" on both fields (R050 O12).
- O7 [classified] (reviewer, 2026-09-30): Labels make the required input clear: Email (with the example address) and Password; the password field's extra announced words are a naming defect (V-F2, R050), not an instruction defect.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-09-30 (inspection).** CO1 (consistency with the product's signed-in shell), CO3 (do the labels make the input clear — note the password field's accessible name is "Password Show password", see R050), CO4 (error suggestions — needs a failed sign-in), CO6 (authentication: e-mail + password with browser autofill supported via `autocomplete=email` / `current-password`, a Show-password toggle, no CAPTCHA — reviewer judges 3.3.8) and CO8 (context changes on focus/input) stay with the reviewer.

## Evidence files in this folder

- (screenshots/exports named R055-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
