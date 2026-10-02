# Test Run R014 — S2

| | |
|---|---|
| **Run ID** | R014 |
| **Date/time** | 2026-09-30 14:06 |
| **View / sample** | S2 |
| **Page URL / location** | https://learn.essentials-ai.com/learning |
| **Task / process** | — |
| **Modality** | cognition |
| **Tool** | inspection (probe measurements kept: CO6, CO9, CO12) |
| **Baseline** | — |
| **Tester** | Daniel Fontaine (reviewer) + assistant (inspection O5); assistant records |
| **Result** | Works |

**Result reasoning.** Cognition inspection of My Courses (reviewer + assistant). Consistent shell across the signed-in views, no inputs, no help offered (A2), no timer, reachable several ways, tab switching stays in place and announces its state; the only state change is a reversible preference.

## Checks (cognition)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| CO1 — Navigation and component identification are consistent with the rest of the product | pass | O7 — navigation and components are consistent across the signed-in views — reviewer |
| CO2 — Help (if offered) appears in a consistent location | n/a | O5 — no help is offered on this view (A2 recorded; vendor claims 3.2.6) |
| CO3 — Labels and instructions make the required input clear | n/a | O5 — no input on the view |
| CO4 — Errors suggest how to fix the problem | n/a | O5 — no input, no error state |
| CO5 — Previously entered information is not demanded again | n/a | O5 — nothing is entered on the view |
| CO6 — Authentication does not require transcription or memorization (no cognitive-function test) | n/a | O2 — no password field and no sign-in form on the view — authentication happens elsewhere |
| CO7 — Time limits are adjustable/extendable; moving content can be paused | n/a | O5 — no time limit and no moving content |
| CO8 — Focus/input does not trigger unexpected context changes | pass | O6 — no unexpected change of context on focus or input — reviewer |
| CO9 — Fields collecting the user's own information (name, email, address, phone, …) carry the matching `autocomplete` purpose so browsers and AT can fill them | n/a | O3 — no field collects the user's own information (name/email/phone/address/… not present) |
| CO10 — Each view is reachable in more than one way (navigation plus search, site map, index, or related links) unless it is a step in a process | pass | O5 — reachable via sidebar navigation, the logo link and direct address |
| CO11 — Submissions with legal, financial, or data-changing consequences are reversible, checked for input errors, or confirmable before commit | n/a | O5 — the only submission is a reversible preference (Classic/Gamified) |
| CO12 — Nothing flashes more than three times per second (photosensitive-safety check; WCAG-only — no 508 FPC counterpart) | n/a | O4 — no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash |
**view_probe 2026-09-30:** answered CO6=n/a, CO9=n/a, CO12=n/a by measurement; facts in `R014-probe.json`.

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O2 [measured] (state: view as loaded, 2026-09-30 view_probe): no password field and no sign-in form on the view — authentication happens elsewhere
  - Classified: CO6 / WCAG 3.3.8 / measured → n/a
- O3 [measured] (state: view as loaded, 2026-09-30 view_probe): no field collects the user's own information (name/email/phone/address/… not present)
  - Classified: CO9 / WCAG 1.3.5 / measured → n/a
- O4 [measured] (state: view as loaded, 2026-09-30 view_probe): no CSS animation, animated image, marquee/blink, canvas, SVG animation or video on the view — nothing can flash
  - Classified: CO12 / WCAG 2.3.1 / measured → n/a
- O5 [new] (state: inspection): No form field on the view (nothing to label, no error possible). No help link or contact anywhere (03 §2.5 A2). No timer or moving content (probe). The view is reached from the sidebar "My Courses", the logo link, the account menu's "Profile & sessions" path back, and by direct address — more than one way. The only state-changing action is the Classic/Gamified preference, which is reversible by switching back; nothing legal, financial or data-destroying.
- O6 [classified] (reviewer, 2026-10-02): Switching Classic/Gamified with Enter announces "Selected" and keeps the user on the same page at the same place; opening the menu changes nothing until an item is chosen.
- O7 [classified] (reviewer, 2026-10-02): "Shell is consistent" — sidebar, header and avatar are identical on My Certificates and My Profile.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (inspection).** CO1 (consistency of the shell across the signed-in views) and CO8 (does switching Classic/Gamified change context unexpectedly — it keeps the same page, swaps the card list) stay with the reviewer.

## Evidence files in this folder

- (screenshots/exports named R014-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
