# Test Run R003 — S7

| | |
|---|---|
| **Run ID** | R003 |
| **Date/time** | 2026-09-10 10:35 |
| **View / sample** | S7 |
| **Page URL / location** | https://login.theexpertta.com/Login.aspx |
| **Task / process** | — |
| **Modality** | — |
| **Tool** | axe |
| **Baseline** | — |
| **Tester** | assistant (axe-core 4.10.3 over CDP, Chrome 151 debug profile); classification pending reviewer |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

## Checks (axe sweep)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| W1 — Every reported failure (axe **violations**; WAVE **Errors/Contrast Errors**) is human-confirmed → finding, or dismissed with a written reason in the run notes |  | O1–O6 recorded; reviewer to confirm |
| W2 — Every warning (axe **incomplete**; WAVE **Alerts**) is reviewed; relevant ones investigated in the matching modality | partial | O7 (bypass) → dismiss proposed (single-form page); O8 (two contrast incompletes, elmPartiallyObscuring) → low-vision run; O9 (link-in-text-block ×4) → no-color run on S7 |
| W3 — Structure output is sane and **cross-checked against the JAWS walk**: if the tool reports no/near-no structure where JAWS finds structure, the instrument didn't penetrate — set the sweep's Result to N/A (instrument-blind), dismiss its structure output, never read 0 findings as a pass (see testing-tools.md) |  | Cross-check with the JAWS walk of the sign-in page (few elements; expect agreement) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [new] (state: signed-out login page, no error shown): axe `html-has-lang` (serious) — `<html>` has no `lang`.
  - Proposed: W1 / WCAG 3.1.1 (A) / Minor — confirm (JAWS language) → finding
- O2 [new] (state: as O1): axe `image-alt` (critical) + `link-name` (serious) — the large login logo `img src="/images/loginlogo.png"` has no alt and is the only content of a link to theexpertta.com, so the link has no name.
  - Proposed: W1 / WCAG 1.1.1 + 2.4.4 (A) / Major (first focusable element, unnamed) — confirm with JAWS ("link graphic loginlogo"?) → finding
- O3 [new] (state: as O1): axe `color-contrast` (serious) — "User Name:" label `#3A7C89` on `#EDEDED` = **4.05:1** at 16 px bold (needs 4.5:1); background resolved to an opaque ancestor, number reliable.
  - Proposed: W1 / WCAG 1.4.3 (AA) / Minor — confirm by eyedropper → finding (check the Password label too; axe only flagged User Name)
- O4 [new] (state: as O1): `landmark-one-main`, `region`, `page-has-heading-one` (best practice) — no landmarks/headings.
  - Proposed: fold into the structure finding
- O5 [new] (state: as O1): the JavaScript/cookies warning text seen in exploration is present in the DOM; axe reports nothing on it.
  - dismissed: informational
- O6 [new] (state: as O1): passes 20 / inapplicable 65 in `R003-axe.json`.
  - dismissed: informational
- O7 [new] (state: as O1): axe **incomplete** `bypass`.
  - Proposed: dismiss — the page is one form with a short header; reviewer to agree
- O8 [new] (state: as O1): axe **incomplete** `color-contrast` ×2 (`elmPartiallyObscuring` — an overlapping element prevents axe from resolving the background).
  - Proposed: W2 → low-vision run, eyedropper on the help text block
- O9 [new] (state: as O1): axe **incomplete** `link-in-text-block` ×4 — the "contact us" / "here" links in the help paragraphs may be distinguished by colour only (they are bold, which may suffice).
  - Proposed: W2 → no-color run on S7 (1.4.1): is bold + colour enough, and is there a hover/focus underline?

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

axe-core 4.10.3, full ruleset, 2026-09-10 17:35 UTC. Counts: violations 7, incomplete 3, passes 20, inapplicable 65.
Reached by navigating the signed-in debug tab to https://login.theexpertta.com/Login.aspx; the page rendered the sign-in form (title "Expert TA - Login"). No credentials entered.

## Evidence files in this folder

- `R003-axe.json` — raw axe output (114,938 bytes)

## Findings raised from this run

- none yet — every observation above awaits reviewer confirmation (W1)
