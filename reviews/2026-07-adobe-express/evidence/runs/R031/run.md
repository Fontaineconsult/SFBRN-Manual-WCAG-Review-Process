# Test Run R031 — S3

| | |
|---|---|
| **Run ID** | R031 |
| **Date/time** | 2026-08-13 14:28 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:1fd8af9a-87db-410e-8315-35fa3679dc86 |
| **Task / process** | — |
| **Modality** | motor |
| **Tool** | keyboard |
| **Baseline** | B2 |
| **Tester** | reviewer (D. Fontaine), physical keyboard, NVDA off |
| **Result** | Works with issues |

## Checks (motor)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| MO1 — Every interactive element can be reached with the keyboard | partial | O1 — chrome "generally keyboard accessible, if not slow"; canvas objects only via the layers list |
| MO2 — Every reached element can be operated (activate, select, dismiss) | fail | O4 — rotation cannot be performed by keyboard → V-F14; move and z-order operate |
| MO3 — Focus is never trapped; Esc/Tab always leads out of widgets and dialogs | partial | no trap narrated; not systematically swept |
| MO4 — A visible focus indicator exists at all times | partial | not per-stop confirmed; no missing-indicator report during the session |
| MO5 — Focus order follows the meaning and operation order of the view | partial | no anomalies narrated; not systematically swept |
| MO6 — Single-character shortcuts can be switched off or remapped | fail | O5/O7 — "T" active; Settings opened: **no disable/remap exists** → V-F15 (2.1.4). O2/O6: docs out of sync both directions |
| MO7 — Dragging and multipoint/path gestures have single-pointer, non-drag alternatives | fail | O4/O7 — rotation (all objects) and resize (non-text objects) are pointer-only → V-F14; translation, z-order, and text-size (via panel, silent steppers) have keyboard routes |
| MO8 — Pointer actions can be cancelled (up-event activation) | n/a | not testable under B2 (no pointer) |
| MO9 — Targets are ≥ 24×24 CSS px or adequately spaced | partial | not measured on S3 (S1 measured pass; editor rails/panels unmeasured) |
| MO10 — Nothing requires device motion (shake/tilt) without an alternative | n/a | desktop web |
| MO11 — A mechanism exists to bypass repeated blocks (skip link reachable on first Tab, or equivalent) before reaching the view's content | fail | no skip mechanism, and no `main` landmark on this view (R014 O3) — the S1 landmark mitigation does not exist here; V-F3 scope |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
Reviewer session 2026-08-13, physical keyboard, NVDA off (B2). Opened
alongside the S1 motor close-out; partial — canvas manipulation checks
remain.

- O1 [classified] (canvas objects, B2): **canvas items cannot be Tabbed to
  and can only be activated through the layers section** — the reviewer's
  words, independently confirming the R015 route under B2, *without* screen
  reader affordances. For a sighted keyboard-only user the layers panel is
  at least visible (unlike for the NVDA user, who could not discover it),
  but the only route to any object on the canvas remains a ~30-stop
  traversal to a small side list.
  - Classified: MO1 / WCAG 2.1.1 / partial (reachable, indirectly and
    onerously) — reinforces the consolidated S3 finding; no new ID.
- O2 [classified] (documented shortcuts, MO6): Adobe documents keyboard
  shortcuts at `helpx.adobe.com/express/web/get-started/keyboard-shortcuts`
  (03 §2.5 A2, now confirmed). **Some documented shortcuts do not work —
  rename, for one.** A keyboard user following the vendor's own
  documentation presses the shortcut and nothing happens, with no error or
  feedback. Not a WCAG SC failure on its own (rename remains achievable via
  Tab/arrows, R029 O3, so 2.1.1 holds) — recorded as a **vendor
  documentation-accuracy defect** for 06's reliability picture, and it
  compounds the discoverability story: the documented paths don't all work,
  and the working paths aren't documented.
  - Classified: MO6 / — / observation → 06 §Vendor audit note
- O3 [classified] (shortcut feedback): *"when using the shortcuts there is
  still no feedback as to state changes on the canvas."* Shortcut-triggered
  operations give no indication of what changed — **and this reviewer
  session was sighted**, which widens the silent-state pattern beyond
  screen-reader users: whatever these shortcuts change is not visibly
  confirmed either. Provisionally the 5th instance of the product's
  no-status-feedback pattern (4.1.3 family); **precision pending one
  clarification** — which state changes were invisible (selection? mode?
  the operation's effect?), asked at session close.
  - Classified: MO2/NV7-family / WCAG 4.1.3 candidate / pending
    clarification — folded into the pattern, no new ID yet.
  - **CLARIFIED same session:** *"no NVDA feedback — when moving an object
    on the canvas there is no feedback as to any state change of that
    object."* The silence is **AT-facing** (the earlier reading that even a
    sighted user lacked feedback is withdrawn). Moving an object announces
    nothing — position, state, or that anything happened. This extends the
    canvas-identity defect (R015 O9: selection announces only "Canvas")
    from *selection* to *operations*, and folds into the consolidated S3
    finding rather than a new ID.
  - **Reviewer design recommendation, recorded for 06:** an app of this
    kind needs a way for a blind user to request, on command, a **voiced
    representation of the canvas** — read-back of the objects, their
    content and arrangement. Entered in the remediation exhibit as the
    fuller form of the canvas-identity ask.
- O4 [classified] (MO7 — canvas manipulation by keyboard, the sitting's
  key question): **translation YES; rotation NO; z-order YES** (via a "…"
  menu in the edit nav area). *"Generally keyboard accessible, if not slow
  to use."* Resize was not narrated — one follow-up remains.
  - **Rotation is therefore pointer-drag only**: no keyboard route and no
    exposed alternative (no rotation field found). That is a **2.1.1
    Keyboard (Level A) failure** for a core canvas operation, and a 2.5.7
    gap on the same facts → **finding V-F14**.
  - Classified: MO7/MO2 / WCAG 2.1.1, 2.5.7 / Major → **V-F14**
- O5 [classified] (MO6 — single-character shortcuts): **"T is the only
  one — creates a text box."** A single-character shortcut is active in the
  editor. 2.1.4 requires such a shortcut be disable-able, remappable, or
  active only on component focus; **no disable/remap setting has been found
  so far — but Settings (C6) has never been opened**, so this is a
  candidate pending that one check, not a finding.
  - Classified: MO6 / WCAG 2.1.4 / **candidate** — resolve by opening
    Settings and looking for a shortcuts toggle.
- O6 [classified] (shortcut documentation, extends O2): **"quite a few
  hidden keyboard shortcuts that are not on the keyboard shortcut
  sheet"** — the inverse of O2's broken-documented-shortcut: working
  shortcuts exist undocumented, documented ones don't all work. The
  shortcut documentation and implementation are out of sync in both
  directions. Reviewer recommendation for 06: *"having more direct key
  commands would be very helpful."*
  - Classified: MO6 / — / vendor documentation-accuracy note → 06.
- O7 [classified] (resize + Settings, closing the run's open items;
  reviewer): **(a) Resize:** text objects can be resized via the text-size
  controls in the Edit panel when selected (requires tabbing back into the
  panel) — but **no size information is announced as the +/− steppers are
  used**, another instance of the value-silence family. Canvas-level
  resize (the corner-drag a mouse user has) is **not possible by keyboard
  at all**, which means **non-text objects — shapes, images — cannot be
  resized by keyboard whatsoever**; "only translate is available" for
  shapes. → **V-F14 broadened**: rotation (all objects) + resize (non-text
  objects) are pointer-only. **(b) Settings (C6, now opened — keyboard
  reachable, a positive): no keyboard-customization settings exist** — no
  disable, no remap. The 2.1.4 candidate therefore resolves: the "T"
  single-character shortcut cannot be turned off or remapped →
  **finding V-F15** (focus-scoping untested as a residual defense, noted).
  **(c) Reviewer recommendation** for the exhibit: *"exposing all
  orientation manipulation controls in the Edit pane would be a good
  idea"* — rotation, size and position fields in the properties panel.
  - Classified: MO7 / 2.1.1, 2.5.7 / Major → V-F14 (broadened); MO6 /
    2.1.4 / Minor → **V-F15**; stepper silence → the product feedback
    pattern (05 4.1.3 remarks).

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R031-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
