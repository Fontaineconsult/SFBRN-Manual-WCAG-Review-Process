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

    chrome.exe --remote-debugging-port=9222 ^
        --user-data-dir=%LOCALAPPDATA%\sfbrn-a11y-chrome ^
        --disable-extensions --disable-sync --no-first-run --no-default-browser-check

**Every flag after the profile earns its place — do not shorten this
(learned 2026-08-14, the hard way).** Launched without them, Chrome shows
its first-run sign-in promo, completes a *sync* sign-in, and pulls the
reviewer's entire personal extension set into what the process calls a
"declared test environment": 22 extensions arrived in one minute. Several
change what an instrument measures — **Stylus** injects CSS (contrast and
reflow become fiction), **SkipTo Landmarks** and **Landmark Navigation**
*add* skip links and landmarks to the page, which is the exact subject of a
2.4.1 finding, and Freedom / Popup Blocker / Postman Interceptor /
EditThisCookie intercept or block. A scan run in that profile measures the
extensions as much as the product.

`--disable-extensions` is per-launch and non-destructive — nothing is
uninstalled — so it is safe to add unconditionally. `--disable-sync`
stops the set being re-pulled. Never remove a reviewer's extensions to
fix this; changing browser settings is the reviewer's call (CLAUDE.md
browser rules).

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
4. **No _store_ extension is live in the profile.** The test is not "zero
   `chrome-extension://` targets" — that rule was written in 2026-09-11
   against Chrome 152, where the browser's own component workers spun down
   after a few seconds. **On Chrome 153 they are persistent** (2026-09-17:
   Gemini in Chrome `admccjkmockfdflocgggjfgdacdodkdf`, Google Network
   Speech `fignfifoniblkonapihmkfakmlgkbkcf`, Google Hangouts
   `nkeimhogjdpnpccoofpliimaahmaaome`, Chrome PDF Viewer
   `mhjfbmdgcfjbbpaeojofohoefgiehjai`), so the old rule can never pass and
   would block every measuring session. `--disable-extensions` cannot switch
   them off, and they are harmless: measured on the product page, they inject
   no stylesheet and no DOM node.

   **Tell the two classes apart by where the code lives**, not by an ID list
   that rots with each Chrome release:

   | | store / policy extension | Chrome-bundled component |
   |---|---|---|
   | unpacked under `<profile>\Default\Extensions\<id>` | **yes** | no |
   | `location` in `Secure Preferences` | 1 | 5 |
   | code path | the profile | `…\Chrome\Application\<ver>
esources\` |
   | `--disable-extensions` stops it | yes | **no** |
   | verdict | **FAIL — discard the window** | fine, name it and go on |

   A store extension *running* is the failure: **Stylus** falsifies contrast,
   **SkipTo Landmarks** and **Landmark Navigation** add the very skip link and
   landmarks 2.4.1 and 1.3.1 are about, **HeadingsMap** reports headings the
   AT cannot reach. Relaunch with `--disable-extensions` and treat anything
   already measured in that window as suspect.

   **The profile still _holds_ them.** On 2026-09-17 the review profile had
   **21** store extensions unpacked — the 2026-08-14 sync residue, Stylus and
   SkipTo Landmarks among them. They are inert *only* while the launch carries
   `--disable-extensions`; pre-flight prints the count as a standing reminder,
   because the danger is the next launch that drops the flag. Folder mtimes
   under `…\sfbrn-a11y-chrome\Default\Extensions` say when each arrived,
   which is how you tell contaminated runs from clean ones.

`python scripts/preflight.py` runs 1–4 in one call (`--launch --url <product
home>` starts the browser with the full flag set when the port is dead;
`--anon` adds the signed-out profile on 9223) and exits 1 on any failure.
Added 2026-09-14 after the hand-typed `curl | python -c` check produced a
traceback instead of "port dead". A sign-in tab is printed as the
reviewer's next action; the script never authenticates.

**Changing the flags means restarting the browser, and only that browser.**
Filter by command line so the reviewer's everyday Chrome is untouched:

    Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" |
        Where-Object { $_.CommandLine -like "*sfbrn-a11y-chrome*" } |
        ForEach-Object { Stop-Process -Id $_.ProcessId -Force }

A bare `Stop-Process -Name chrome` kills the reviewer's own session.

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
- **Assistant-driven reflow (works — used 2026-08-13):** CDP
  `Emulation.setDeviceMetricsOverride` to 320×900 on the debug-profile
  Chrome. The 2026-08-04 blocker only applied to the extension channel.
  **`Page.captureScreenshot` pixels do NOT align with
  `getBoundingClientRect` coordinates on this product (2026-08-14).** With
  `fromSurface=true` the captured surface includes the Adobe cross-product
  app bar in its top ~55 px, but that bar sits outside the document's
  viewport coordinate space — so every rect samples **~56 px too high**,
  and controls in the Express bar get measured against the purple Adobe
  bar above them. `fromSurface=false` is not the fix: it ignores
  `Emulation.setDeviceMetricsOverride` and returns a differently-sized
  image (2112×1486 when 1280×900 was set). **Before trusting any
  pixel-sampled number, save the PNG and look at it**, and verify a known
  element's rect against what is visibly there. An automated 1.4.11 sweep
  was built on this basis, produced three successive wrong answers, and
  was abandoned — see R042 O6. **LV5 (UI component contrast) stays a
  reviewer eyedropper check**; the assistant's useful contribution is a
  correctly-rendered capture to sample from, not a ratio.

  **Any hand-written CDP client needs `suppress_origin=True` on
  `websocket.create_connection` (Chrome 151+, confirmed 2026-08-14).**
  Without it the handshake fails `403 Forbidden — Rejected an incoming
  WebSocket connection from the http://127.0.0.1:9222 origin`, and the
  error names a `--remote-allow-origins` flag that you do *not* need —
  suppressing the header is the fix. `scripts/axe_scan.py` already does
  this; copy its `CDP` class rather than writing a fresh client.
  Verify the landed view by *path* before measuring (host-substring
  matching once measured the wrong view). Reflow metric: scrollingElement
  scrollWidth vs 320. **Screenshot hang — cause found 2026-09-11:**
  `Page.captureScreenshot` hangs whenever the debug window is occluded or
  in the background (no frame is ever produced), not because a view is
  heavy. Call `Page.bringToFront` immediately before the capture — it then
  returns in well under a second, with vision-deficiency emulation on as
  well. (The window pops to the foreground on the reviewer's desktop; say
  so before a batch.) Keep the *metric* (scrollWidth delta) as the LV3
  outcome regardless; the screenshot is the visual confirmation.
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

## view_probe — instrument-answerable checks per view (assistant-run)

`python scripts/view_probe.py <review> --view S# --url URL [--dry-run]`
answers the checks listed in modality-checks.md §Assistant-answerable checks
and writes them into the view's runs. Run it on every sampled view before
the reviewer session; `--dry-run --facts-out FILE` shows what it would write.

**How each fact is measured, and its limits (state them in the run when they bite):**

- **Media / speech / motion / audio API / orientation lock** — DOM query of
  the view and its same-origin frames plus a regex scan of inline scripts and
  every external script the page can `fetch` with credentials. Cross-origin
  CDN scripts that refuse the fetch are listed as *unreadable* in the
  observation; an n/a for NS1/MO10/NH4 rests on the readable set only.
- **Reflow (LV1)** — `Emulation.setDeviceMetricsOverride` to 320 CSS px,
  read `scrollingElement.scrollWidth`, list elements whose right edge passes
  320. Only *data* tables (a `th`, a `caption`, or `role=grid/table`) count as
  exempt; layout tables do not. Metrics are cleared afterwards.
- **Text spacing (LV3)** — inject the standard override, compare the set of
  text containers with hidden/clip overflow whose scroll size exceeds their
  client size before and after. Newly clipped containers = fail. Overlap
  without clipping is not detected — the reviewer's zoom pass still looks.
- **Target size (MO9)** — bounding boxes of visible targets (links, buttons,
  inputs, ARIA widgets, `[onclick]` except table structure/containers, which
  are event delegation). Exceptions applied: inline-in-text links, native
  checkbox/radio (user-agent sized), spacing (no other target within a 24 px
  circle; ancestors/descendants are not neighbours). *Essential* and
  *equivalent* exceptions are the reviewer's call — the fail lists the pairs.
- **Autocomplete (CO9)** — personal-data fields recognised by name/id/label/
  placeholder; bare "name" fields are candidates only.
- **Wrong-view guard** — refuses if the landed path differs from the
  requested one; use a `UI: …` locator after reaching the view by hand.

**One session, one tab — and the assistant shares the browser.** Expert TA
allows a single session instance and enforces it by answering every request
with `WSInvalidAccess.aspx`, whose own text names the cause: *"You are using
Expert TA in more than one tab in your browser."* This is a **coordination**
hazard, not a navigation one: the assistant drives a tab over CDP while the
reviewer drives their own, and two tabs on the product host is all it takes.
2026-09-21 it broke a session mid-walk, and the reviewer reasonably read it as
their own paste failing — "I can't open it … this happens for all copy/paste
into the browser". The URL was fine; the session was not.

Rules that follow:

- **Never leave a second tab on the product host.** `crawl_map.CDP` attaches
  to an existing page tab and navigates *it* — keep it that way, and do not
  open new ones with `tabs_create`.
- **Check before driving** when the reviewer is also working: `/json` should
  list exactly one tab per product host. `preflight.py` now fails on a
  duplicate host and on any tab sitting on `WSInvalidAccess`.
- **Recovering:** close the extra tabs keeping the one the reviewer is in,
  then the reviewer reloads; if the session does not come back they sign in
  again. The assistant never signs in.
- A pasted deep link failing is **not** evidence that the link is wrong. Check
  for this error page before concluding anything about a URL or a route.

**Sign-in views need a second, signed-out profile.** Navigating the
authenticated tab to `Login.aspx` ended the Expert TA session on 2026-09-11
(the app redirected everything to sign-in afterwards; the assistant never
authenticates, so the reviewer had to sign in again). Probe such views with:

    chrome.exe --remote-debugging-port=9223 ^
        --user-data-dir=%LOCALAPPDATA%\sfbrn-a11y-chrome-anon ^
        --disable-extensions --disable-sync --no-first-run --no-default-browser-check
    python scripts/view_probe.py <review> --view S7 --url <sign-in URL> --port 9223

The anonymous profile holds no session, so the product's one-session rule
is not triggered.
