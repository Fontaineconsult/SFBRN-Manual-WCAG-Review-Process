# Standard Testing Tools & Evidence Capture

The process's standard toolset and what evidence each tool must produce.
Declared per-review in `03-scope-and-sample.md` §1.5; every test session is
logged as a **run** (`review.py log-test`), which creates
`evidence/runs/R###/` for that session's evidence and records the page/view,
date, tool, and baseline. Findings in `04-task-testing.md` cite run IDs.

Neither tool is sufficient alone: automated checkers detect only the
machine-testable subset of WCAG failures, and screen reader testing only
covers what the tester drives. The two-tool strategy is: **WAVE sweeps every
sampled view** for machine-detectable issues; **JAWS walks every task
sequence** the way an actual screen reader user would. (See
`selecting-evaluation-tools.md` and the tools catalog in
`tools/wai-evaluation-tools.md`.)

## JAWS — manual assistive technology testing

**Role:** primary manual testing instrument. Used to walk the task sequences
(03 §3.3) step by step and to inspect sampled views.

**Record once per review** (03 §1.5): JAWS version and build, browser and
version, OS. Update if the version changes mid-review.

**Environment hygiene (learned 2026-08-04):** JAWS reads whatever shares the
focused window. Before a JAWS run, close or unfocus the Claude for Chrome
side panel (and DevTools, extra panes) so speech is product-only; when the
assistant panel must stay open, keep focus in the product tab and disregard
non-product speech when setting outcomes — note the contamination in the run.

**Testing pattern per run:**

1. Start a run (`log-test --tool jaws --view <sample> --url <page>`).
2. Follow the process sequence exactly as recorded in 03 §3.3 — same steps,
   same actions — using JAWS-typical interaction (virtual cursor, Tab,
   forms mode, headings/landmarks navigation).
3. In the run's `run.md` notes, record triplets of:
   - **Action** — the keystrokes/navigation used
   - **Announced** — what JAWS actually spoke (use the Speech History,
     `Insert+Space, H`, to copy exact output)
   - **Expected vs actual** — what a user needed at that moment
4. Screenshot any state where the visual UI and the announced experience
   diverge (name files `R###-<what>.png` inside the run folder).

**What JAWS testing decides:** task verdicts (can the sequence be completed?),
and findings for name/role/value, focus order, keyboard operability, labels,
status messages, and announcement of dynamic changes.

## axe-core — automated per-view sweep (primary)

**Role:** the standard automated checker, run on **every sampled view and
significant state**. Assistant-runnable, and it traverses open shadow DOM —
which WAVE cannot on this product class. Engine vendored at
`tools/axe/axe.min.js` (record the version in 03 §1.5; currently 4.10.3).

**Setup — dedicated testing profile (learned 2026-08-04):** Chrome 136+
ignores `--remote-debugging-port` on the *default* profile, and
session-restore relaunches drop the flag — so scans use a dedicated profile
the reviewer signs into once (also better hygiene: a stable, declared test
environment):

    chrome.exe --remote-debugging-port=9222 --user-data-dir=%LOCALAPPDATA%\sfbrn-a11y-chrome

The profile lives outside the repo — never commit or copy profile
contents. It normally persists signed-in across sessions, but **do not
assume it survives** (2026-08-06: the directory was simply gone between
sessions, and the relaunch landed on the IMS sign-in page). Pre-flight,
in this order:

1. Profile directory exists? (`%LOCALAPPDATA%\sfbrn-a11y-chrome`)
2. Port answers? (http://localhost:9222/json/version)
3. The target tab is **authenticated**, not the IMS sign-in page — check
   `http://localhost:9222/json` for a tab titled "Sign in" or a
   `auth.services.adobe.com` / `adobelogin.com` URL.

A missing directory or a sign-in page means the reviewer must sign in
once in that window before scanning — **the assistant never
authenticates** (CLAUDE.md browser rules). Scanning a signed-out tab
measures the login page, not the product.

The debug-profile window is a second Chrome, independent of the
reviewer's everyday one: launching it does not disturb the default
profile's session, and the two can be used side by side (extension work
on the signed-in default profile, axe sweeps on the debug profile).

**Run per view/state:**

    python scripts/axe_scan.py <review> --view S1 --url <URL>

- Logs the run itself (`--tool axe`, no modality) unless `--run R###`
  attaches to an existing one; `--tab TEXT` picks the tab when the URL is
  ambiguous (SPA views); `--tags wcag2a,wcag2aa,wcag22aa` restricts the
  ruleset; `--out PATH` does an ad-hoc scan with no run (recon only).
- Saves the **raw axe JSON** as `evidence/runs/R###/R###-axe.json` and
  prints a summary (violations by impact, incomplete items).

**A `violation` is not automatically true — verify contrast ones (learned
2026-08-06, R014 O2).** axe normally reports *incomplete* when it cannot
resolve a background, but for `color-contrast` it will sometimes substitute
an assumed background and emit a confident numeric **violation** instead. On
S3 it reported the editor header at **1.08:1** and **1.14:1**; sampling the
rendered pixels gave **15.06:1** and **12.18:1** — the real background was
`rgb(29,29,29)`, not the `#e9e9e9` axe assumed. Two fabricated serious 1.4.3
failures would have entered the ACR unchallenged.

- **The distinguishing signal:** walk the ancestors for an opaque
  background. If one exists, axe's number is reliable (S1's `.browse-text`
  3.96:1 was independently corroborated twice). If **no opaque background is
  found**, treat any axe contrast number — violation *or* incomplete — as
  unmeasured, and settle it by rendered-pixel sampling or eyedropper.
- Applies to contrast specifically. Name/role/structure rules
  (`aria-command-name`, `aria-required-parent`, …) inspect the DOM directly
  and have been accurate on this product.

**Reproducing a reviewer's keyboard path (learned 2026-08-06).** Use real
dispatched key events — CDP `Input.dispatchKeyEvent` with
`rawKeyDown`/`char`/`keyUp` — not `.click()` or `.focus()`. Programmatic
activation bypasses the application's own key handling and will land you
somewhere else: an attempt to follow a reviewer into a layer's edit UI
opened the page-level panel instead, and the resulting reading had to be
discarded. A tab walk driven this way also yields the **stop count** to a
control, which is evidence for 2.4.1/2.4.3 that nothing else provides.

**Probe every state, not one.** In a stateful application the accessibility
tree only describes the current state. An editable field created on entering
edit mode is genuinely absent from a snapshot taken beforehand — and
concluding "no mechanism exists" from that absence produced a false 2.1.1
Blocker on S3. If a mechanism might be modal, enter the mode and re-probe,
or ask the reviewer.

**Automated sweeps are blind to `<canvas>`.** On a canvas-rendering view the
sweep can return a clean-looking result while the entire user document is
unexposed — R014 reported 43 passes and *nothing at all* about a 2328×1145
canvas holding the document. Never read a sweep's pass count as reassurance
on such a view; the manual modality run carries the whole weight.

**Interpreting output** (the automated-sweep checks in
`modality-checks.md`): every `violations` entry is human-confirmed →
finding (citing the axe rule ID and the run) or dismissed with a reason;
`incomplete` entries are candidates for the matching modality's manual
checks; `passes`/`inapplicable` counts stay in the raw JSON for the record.
Sanity-check against the JAWS walk per W3 — axe handles open shadow roots,
but closed roots and cross-origin iframes are still invisible to it.

## WAVE — automated per-view sweep (secondary)

**Role:** reviewer-run automated checker for views WAVE can actually parse
(light-DOM pages: marketing/landing, documentation). Re-run after
significant state changes.

**Record once per review** (03 §1.5): WAVE extension version and browser.

**Testing pattern per run:**

1. Start a run (`log-test --tool wave --view <sample> --url <page>`).
2. Run the WAVE extension on the view/state.
3. Record in the run's notes the four summary counts: **Errors, Contrast
   Errors, Alerts, Features/Structural** — and list each distinct error type
   WAVE reports.
4. Capture two screenshots into the run folder: the page with WAVE icons
   overlaid, and the WAVE details panel.
5. **Confirm before reporting:** WAVE output is indicative, not a finding.
   Each WAVE error becomes a finding only after human confirmation, mapped to
   the WCAG criterion WAVE references (its details panel links each icon to
   the criterion).

**What WAVE testing feeds:** view-sweep findings (04 §B) — alt text, labels,
contrast, structure, ARIA misuse — and pointers for where JAWS testing should
dig deeper.

**Mandatory cadence (applies to the sweep, whichever instrument):** every
sampled view gets one automated sweep run (axe primary; WAVE where it can
parse), and significant states get re-runs. `review.py validate` fails while
any sampled view lacks one; `next` lists missing sweeps. Schedule the sweep
in the same session the view is first tested.

**Shadow-DOM blindness (learned 2026-08-04, Adobe Express R007):** the WAVE
extension may analyze only the light DOM of web-component apps. Signature:
**0 errors + "No heading structure" + "No page regions" alerts on a page
where JAWS reports structure** — that is non-penetration, not cleanliness,
and the AIM score is meaningless there. Handle it: sanity-check WAVE's
structure view against the JAWS walk (W3); if blind, set the sweep run's
Result to **N/A (instrument-blind)** with the contradiction noted, dismiss
the structure alerts, and do NOT read 0 errors as a pass. For automated
coverage of such views, a shadow-DOM-capable checker (axe DevTools, IBM
Equal Access — `tools/wai-evaluation-tools.md`) may be added to 03 §1.5 as a
secondary instrument; WAVE stays the declared standard for views it can
parse.

## The other instruments (one per remaining modality)

Tool names below are the exact `--tool` values `log-test` expects
(`MODALITY_DEFAULTS` in `review.py`). Each serves the matching checklist in
`modality-checks.md`.

### `zoom` — low-vision (baseline B3)

- **Canonical setup:** browser zoom 400% in a 1280px-wide window. The
  CSS-equivalent instrument — a **320 CSS px wide viewport** (WCAG 1.4.10's
  own equivalence) via window resize or DevTools device emulation — is
  accepted; record which was used in the run notes.
- **Text spacing (LV3):** apply the standard override to the page and re-read:
  `line-height 1.5× font size; paragraph spacing 2×; letter spacing 0.12×;
  word spacing 0.16×` (bookmarklet or injected CSS — record which).
- **Contrast (LV4/LV5):** WAVE contrast data and/or eyedropper measurement
  (e.g., Colour Contrast Analyser). Pick the method by what paints the
  background — the three cases are not interchangeable (learned 2026-08-06,
  R009 O8/O9):

  1. **Solid background colour** → computed-style sampling is reliable.
     Walk ancestors (crossing shadow boundaries) to the first fully opaque
     `background-color` and apply the WCAG relative-luminance formula.
  2. **Self-contained SVG or CSS gradient background** → **measure it
     exactly, don't reach for the eyedropper.** If the asset references no
     external resources, re-render it same-origin as a `data:` URI onto a
     canvas at the element's *rendered* size and `getImageData` under the
     text box. This is an exact measurement, and it is what an automated
     checker cannot do: axe reports these as *incomplete* ("background
     colour could not be determined due to a background image"), not as a
     pass or a fail. Sample a grid across the text box and report the worst
     ratio, not the centre. Fetching the asset cross-origin will be
     CORS-blocked and would taint the canvas — download it out-of-band and
     inline it instead.
  3. **Background painted by a pseudo-element, a non-hit-testable image, or
     any compositing you cannot resolve** → eyedropper, or rendered-pixel
     sampling via CDP `Page.captureScreenshot`. **Nothing else is valid
     here.** The trap: an ancestor walk in this case finds no painted
     background at all, silently falls back to white, and yields a
     confident-looking ratio (typically 21:1 for dark text) that is
     completely wrong. `elementsFromPoint` through the shadow roots returns
     transparent all the way down and will not save you either. If the walk
     reports "no background found", the honest output is *unmeasured* —
     discard the number rather than recording it.

  Before trusting any of the three, exclude translucent overlays: check
  every underlay/scrim element for `visibility`, `opacity`, and actual
  background alpha. A hidden-but-present `rgba(0,0,0,0.4)` scrim is common
  in SPA component libraries and would change every ratio on the view.
- **Evidence:** screenshots at reflow width (full view, scrolled states),
  with-text-spacing screenshot, any clipped/overlapping state.

### `grayscale` — no-color

- **Canonical setup:** OS color filter (Windows: Settings → Accessibility →
  Color filters → Grayscale, toggle `Win+Ctrl+C`).
- **Accepted proxy:** injected CSS `html { filter: grayscale(1) }` — visually
  equivalent for on-page content; record its use in the run notes.
- **Evidence:** grayscale screenshots of every state inspected; note each
  place color was the only differentiator.

### `keyboard` — motor (baseline B2)

- **Setup:** pointer set aside entirely; Tab / Shift+Tab / Enter / Space /
  arrows / Esc only.
- **Record the focus path** in the run notes: the sequence of elements focus
  visits, noting any unreachable control (MO1), inoperable control (MO2),
  trap (MO3), invisible indicator (MO4), or illogical order (MO5). Target
  size (MO9) may be measured via DevTools/element geometry.
- **Evidence:** screenshots of focus states — especially wherever the
  indicator is faint or missing.

### `inspection` — no-hearing, no-speech, cognition

- A structured pass against that modality's checklist; no special apparatus.
  `no-hearing`/`no-speech` are commonly **N/A** (no audio / no voice
  features on the view) — an N/A Result with a one-line justification is a
  complete, valid run and counts as coverage.

## Assistant-driven runs (Chrome automation)

The assistant (per `assisted-exploration.md` roles) may **drive** these
instruments itself: `axe` (scripts/axe_scan.py — the standard automated
sweep), `zoom` (window-resize reflow, injected text-spacing CSS),
`grayscale` (CSS proxy), `keyboard` (synthesized Tab-walk with
screenshots), and `inspection`. Two are **always reviewer-driven**: JAWS
(real AT behavior cannot be synthesized) and the WAVE extension (extension
UI is outside automation reach).

Conventions for an assistant-driven run:

- **Tester** field in `run.md`: `assistant (Claude, Chrome automation)`.
- Any instrument approximation (window-resize instead of browser zoom, CSS
  grayscale instead of OS filter, computed-style contrast sampling) is named
  in the run notes.
- Check outcomes from assistant-driven runs are working results: the
  reviewer spot-checks them (especially any **fail**) before the finding
  feeds `06-report.md`. Findings still cite the run and evidence files as
  usual.

Known instrument limits (learned 2026-08-04, Adobe Express trials):

- **CSS `zoom` is NOT a reflow instrument.** It magnifies without
  re-evaluating responsive breakpoints — layout does not reflow, producing
  false LV1/LV2 failures. Never judge reflow from it. If window resize is
  ignored (maximized/managed windows report success but the viewport doesn't
  change) and browser-zoom keystrokes are unavailable, LV1/LV2/LV7/LV8 go to
  the reviewer at real browser zoom; the assistant still covers
  LV3 (injected text-spacing CSS is the canonical method), LV4 (solid
  backgrounds only), and LV6.
- **Computed-style contrast sampling** is reliable only against solid
  ancestor backgrounds; gradient/image/indeterminate backgrounds need the
  reviewer's eyedropper.
- **Synthetic keyboard focus attribution can lie.** On shadow-DOM-heavy
  apps, `activeElement` queries between synthesized Tab presses may report
  BODY while focus visibly moves. Trust *presence* observations (a visible
  outline in a screenshot, a reached element); never conclude
  unreachable/no-indicator from automation alone — that conclusion needs a
  physical keyboard.
- **Synthetic hover teleports.** 1.4.13 "hoverable" fails observed via
  teleporting pointer need reviewer confirmation with continuous pointer
  travel.

## Evidence conventions

```
evidence/
  test-log.md          index of all runs (generated by log-test)
  runs/
    R001/
      run.md           run metadata + notes (generated, then filled in)
      R001-*.png       screenshots, exports for that run
```

- One run = one tool on one view/state (or one JAWS pass through one task
  sequence). Don't mix tools in a run.
- Name evidence files with the run prefix: `R003-export-dialog-wave.png`.
- Findings cite the run and file: `Evidence: evidence/runs/R003/…png (run R003)`.
- The run log satisfies WCAG-EM step 5.2 (record evaluation specifics): which
  page, when, with what tool, under which baseline — enough to replicate any
  result.
