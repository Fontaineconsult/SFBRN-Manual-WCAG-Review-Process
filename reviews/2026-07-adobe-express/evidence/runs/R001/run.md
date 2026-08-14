# Test Run R001 — S1

| | |
|---|---|
| **Run ID** | R001 |
| **Date/time** | 2026-07-27 19:23 |
| **View / sample** | S1 |
| **Page URL / location** | https://new.express.adobe.com/ |
| **Task / process** | P1 |
| **Modality** | no-vision |
| **Tool** | jaws |
| **Baseline** | B1 |
| **Tester** | reviewer (D. Fontaine), **JAWS** — confirmed 2026-08-06 |
| **Result** | N/A |

**Result reasoning** (set 2026-08-14, at report close). **Run suspended
2026-08-06** when testing moved from JAWS to NVDA; NV1/NV2 stand as JAWS
evidence and NV3–NV9 continued under **R012 (NVDA, B4)**. Closed as
**N/A** rather than left unset, because the run will not be completed
under this review: JAWS was never confirmed in scope (03 §1.3), and the
report states plainly that **all screen-reader evidence is NVDA-only**.
The partial JAWS evidence it did produce is preserved below and was used —
R001 O7's landmark walk is what scoped V-F3 to keyboard-without-AT users,
and it remains the review's only cross-screen-reader corroboration.
**Reopen only if JAWS is brought into scope**, which would be a new run,
not a resumption of this one.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | pass | O1 |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | pass | O3 (sparse but proper; region identity pending) |
| NV3 — Every control announces an accurate name, role, and value/state | | |
| NV4 — Images announce appropriate alternatives; decorative images are silent | | |
| NV5 — Reading order matches the meaning of the visual order | | |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | | |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | | |
| NV8 — Nothing is conveyed only by visual position, shape, or size | | |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | | |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

- O1 [classified] (state: fresh page load, session 2026-08-04, walkthrough
  W2): JAWS announces title "Adobe Express" — identifies the product home;
  title-only announcement is expected behavior.
  - Classified: NV1 / WCAG 2.4.2 / pass — no finding
- O2 [classified] (state: same load): JAWS also spoke a lot of extra
  information from the Claude for Chrome extension UI (side panel sharing
  the browser window) — not from the product.
  - Dismissed: environment artifact. Mitigation for the rest of this run:
    keep focus in the product tab and close/unfocus the assistant side
    panel during JAWS steps; disregard non-product speech when setting
    outcomes.
- O3 [clarified] (state: default, walkthrough W3): Structure is real to
  JAWS → the near-empty extraction tree (03 §2.6) was a tooling artifact,
  resolved. Initial load announcement said "3 headings, 2 regions, 1 link";
  the full `H`-key walk found the complete outline, all reachable and
  properly announced:
  - Adobe Express
    - [2] Daniel Fontaine
      - [3] Recent
  - [1] How would you like to start?
    - [2] Upload · [2] Start new design · [2] Edit photos · [2] Set up
      brand kit · [2] Generate presentation · [2] Quick edits · [2] File
      formats · [2] Ways to create · [2] Templates
  Hierarchy quirks (not failures): greeting exposed as heading "Daniel
  Fontaine"; "Recent" nested under it at level 3. Pending: identity of the
  2 regions (a `main` region would give SR users a partial app-bar bypass —
  affects V-F3 scope; keyboard-only users unaffected either way).
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 / pass — no finding
- O5 [new] (state: default, walkthrough W3→W4): "Recent" is 3rd in reading
  order (right after the greeting) but visually the bottom sticky strip —
  candidate NV5 (1.3.2) divergence. Resolve in W4: when arrowing, does the
  Recent content interrupting greeting→start-cards disorient, or read as a
  sensible summary-first order?
- O6 [new] (state: default, walkthrough W3): Two page sections not in the
  visual exploration map surfaced via headings: "Ways to create" and
  "Templates" (below the fold). Enclosure C3 row updated.
- O7 [classified] (state: default, walkthrough W3): Landmark walk (`R`),
  supersedes the load announcement's "2 regions": **Apps [navigation],
  banner, Primary [navigation], main, search** — all reachable, sensibly
  labeled. Consequences: NV2 pass reinforced; the Adobe app bar is a
  labeled nav region and a `main` landmark exists → JAWS users can bypass
  repeated blocks via landmarks (WCAG sufficient technique ARIA11), so
  finding V-F3's affected users narrow to keyboard-only (non-AT) users.
  Whether 2.4.1 then still fails is a conformance-interpretation call —
  reviewer decision pending (05 remarks).
  - Classified: NV2 / WCAG 1.3.1, 2.4.6 / pass — no finding
- Note on initial-load counts: JAWS's page-load summary ("3 headings,
  2 regions, 1 link") undercounted reality in both W3 walks — don't set
  outcomes from load-announcement counts; walk the structure.
- O4 [new] (state: default, walkthrough W3): JAWS reports only 1 link, but
  the DOM holds 7 anchors (two "View all", "browse", the Recent-file card,
  app links). Either most render as buttons to AT (acceptable) or link
  content is missing from the virtual buffer (NV3 problem). Resolve in W5:
  `Insert+F7` links list + walk the Recent-file card and "View all".
- O8 [new] (state: default, search bar — DOM evidence from session
  2026-08-06, R010 O2; **needs JAWS confirmation in W5**): the home search
  input's accessible name is `aria-label="Search for templates and more"`,
  while the text a sighted user reads in the field is the rotating
  placeholder — "Search for *popular templates*" / "*seasonal templates*" /
  "*images*". The visible string is therefore **not contained in** the
  accessible name.
  - Two separate consequences, do not conflate them:
    (a) **Good for 4.1.2/NV3:** the name is stable and meaningful, and the
        rotator is `aria-hidden="true"` in no live region — a screen reader
        hears one consistent label, never the rotation. This also defuses
        the W8 "chatty rotating placeholder" concern (NV7).
    (b) **Candidate 2.5.3 Label in Name:** speech-input users say what they
        see. "Click "Search for popular templates"" would not match the
        accessible name, and the target string changes over time, so no
        fixed utterance works. Vendor claims Partially Supports for 2.5.3.
  - Held as a **candidate, not a finding** — whether a placeholder counts as
    a "label" under 2.5.3 is a judgment call (placeholders are not labels
    for 3.3.2 purposes, and 2.5.3 speaks of components "with labels"), and
    it turns on how long the rotation is actually visible (R010 O1). W5
    should capture what JAWS announces on the field; the 2.5.3 call is the
    reviewer's.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R001-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
