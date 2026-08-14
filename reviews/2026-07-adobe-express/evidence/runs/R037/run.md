# Test Run R037 — S3

| | |
|---|---|
| **Run ID** | R037 |
| **Date/time** | 2026-08-14 11:30 |
| **View / sample** | S3 |
| **Page URL / location** | https://new.express.adobe.com/id/urn:aaid:sc:US:b1ab530f-f097-4a5f-8a6f-b8923fa65115 |
| **Task / process** | T2 |
| **Modality** | no-vision |
| **Tool** | nvda |
| **Baseline** | B4 |
| **Tester** | reviewer (D. Fontaine), NVDA 2026.1.1 + Chrome 151.0.7922.138 |
| **Result** | Works with issues |

**Result reasoning.** The export flow itself is completable by a
screen-reader user: formats are reachable and labelled, the popover is
fully tabbable and Escape-dismissible, and download completion is
announced. Two unannounced dialogs and an undiscoverable Cancel are the
barriers (O1, O4). Scoped to the **export flow** — the *published output*
defect (O6) is not a barrier to this task and is recorded separately.

**Continuity:** continues the T2 walk begun in **R016** (steps 0–2, Chrome
150). Logged as a separate run rather than appended to R016 because the
browser version changed between sessions — R037 is the **first run on
Chrome 151.0.7922.138** (03 §1.5). Session ran W16 of
`session-S3-reviewer-walkthrough.md`.

## Checks (no-vision)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

This is a **task-step run** (T2 steps 3–5), not a view sweep. Rows the
export flow does not exercise are marked n/a and remain the property of the
S3 view-sweep runs R015/R016 — they are not answered here by inference.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NV1 — Page/view title identifies its purpose | n/a | Not exercised — no navigation in this step; see R015 |
| NV2 — Headings and landmarks exist, are hierarchical, and support navigation | n/a | Not exercised; see R015 O10/O11 |
| NV3 — Every control announces an accurate name, role, and value/state | **fail** | O1 (export popover not announced as a dialog), O4 (download dialog unannounced; its Cancel discoverable only by enumerating the button list). Partial credit recorded: format options *are* reachable and labelled (O2) |
| NV4 — Images announce appropriate alternatives; decorative images are silent | n/a | Not exercised in the export flow. **See O6** — the *published output* fails this comprehensively, but that is a different artifact, not this view |
| NV5 — Reading order matches the meaning of the visual order | n/a | Not exercised |
| NV6 — Form fields announce labels and instructions; errors are announced and identified | n/a | No form fields in the export flow; no error path triggered |
| NV7 — Dynamic updates (toasts, async results, validation) are announced without stealing focus | **partial** | O3 — download progress (beeps) and completion **are** announced, via the browser's own download UI. O4 — the app's own "downloading" dialog appearing is not announced |
| NV8 — Nothing is conveyed only by visual position, shape, or size | n/a | Not exercised |
| NV9 — Language of the view (and passages) is announced/pronounced from the correct language | n/a | Not exercised |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

- **O1 [classified]** (state: editor → Download/Share, export popover open):
  The export UI **is not announced as a dialog**. Reviewer supplied the
  markup: `<hz-themed-overlay theme="spectrum-two" open placement="bottom-start">`
  → `<sp-popover open>` → `<x-export-popover-content tabindex="0">`. No
  dialog role is conveyed. **But it is otherwise well-behaved**: "fully
  tabbable", Escape exits it cleanly, and the format options are reachable.
  So the defect is the missing role announcement — orientation, not
  operability.
  - Classified: NV3 / WCAG 4.1.2 / Minor → finding **T2-F3**

- **O2 [classified]** (state: export popover): **Formats offered are PDF,
  images, and MP4 (video)**, and they are reachable and labelled. This is
  the direct answer to the standing §504 scope question — the product does
  export **PDF** and does publish **webpages** (see O6), the two formats
  where the absence of alt-text authoring (R016 O10) is material rather
  than negligible.
  - Classified: evidence for §504 scope decision + NV3 partial credit

- **O3 [classified]** (state: download in progress → complete): **NVDA
  announces progress while the file downloads, with beeps, and announces
  completion when the download is initiated in the browser.** Recorded
  precisely because it **contradicts the expectation carried into this
  step**: four prior 4.1.3 failures made a silent export look near-certain,
  and it did not happen. **Attribution caveat, stated rather than glossed:**
  the progress and completion feedback comes from the **browser's own
  download UI**, not from Express. The user is genuinely informed, so the
  user-level need is met; but this is user-agent behaviour, so it is not
  evidence that the product emits status messages.
  - Classified: NV7 partial / **not** a 4.1.3 failure → no finding

- **O4 [classified]** (state: download dialog): A separate **"downloading"
  dialog opens and is not announced**. It contains a **Cancel** control
  "which would not be knowable unless a user inspects the button list" —
  so a user cannot readily abort an export in progress. This matters most
  on MP4, the long-running format.
  - Classified: NV3, NV7 / WCAG 4.1.2, 4.1.3 / Minor → finding **T2-F3**

- **O5 [classified]** (state: export as video): **Exporting as video does
  support CC** — captions survive the export path. This answers the third
  question W16 was built to settle and **extends R030 favourably**: the
  auto-caption capability found in the editor is not stranded there, it
  reaches the exported artifact.
  - Classified: §504.2 credit; supports 1.2.2 capability → no finding

- **O6 [classified]** (state: **published output**, `/publishedV2/` share
  link — a different artifact from the editor): **Documents shared via the
  publish link are not visible to screen readers at all — they announce as
  just "canvas graphic".** The published webpage carries none of the
  document's content in any perceivable form. Reviewer's conclusion,
  recorded in their own words: *"this tool should not be used to share
  content, especially in a course."*
  - Classified: WCAG 1.1.1, 1.3.1 / **Major** → finding **V-F16**
  - **Locator outstanding:** the exact `/publishedV2/…` URL is needed
    before this run is closed (every finding needs a replicable locator —
    CLAUDE.md). Reviewer to supply.
  - **Scope call outstanding:** whether published output falls inside this
    review's WCAG conformance target or is carried as §504/advisory is the
    reviewer's decision — it is the same standing §504 scope question,
    now with much sharper evidence behind it.

- **O7 [classified]** (state: export → PDF, then inspection of the exported
  file — reviewer, 2026-08-14): **PDF export offers an option to include
  tags, and the tagged output still does not pass accessibility checks.**
  On inspecting the exported PDF with the tags option set: **no alt text,
  no document title.** Reviewer's conclusion, adopted: *"PDF accessibility
  review would still be required even if the tags option were set."*
  - **Why this is worse than a plain missing feature.** A tags option is
    the visible sign of an accessibility capability, and it is the thing a
    vendor points at when asked whether their tool produces accessible
    output. Here it exists and is **insufficient on its own** — which is
    harder to detect than an absent feature, because a procurement reader
    sees the checkbox and reasonably assumes the problem is solved. The
    institution would be shipping PDFs it believes are conformant.
  - **The two defects have different causes, and the distinction is
    actionable:**
    - **No alt text** is *downstream of R016 O10* — there is no way to
      author alt text in the editor at all, so there is nothing for the
      tagger to carry into the file. Fixing the exporter alone cannot fix
      this; the authoring capability has to exist first.
    - **No document title** is a **pure exporter defect and cheap**. The
      product already knows the document's name — it is the one place in
      the product that retitles the browser tab (V-F8's sole exception).
      It simply is not written into the PDF's Title metadata. A PDF with
      no title fails 2.4.2 when published, and the value is already in
      hand.
  - **Recorded as a hypothesis, not a result** (reviewer's own framing):
    *"I'm sure more complex PDFs would have more issues."* Plausible — the
    test artifact was simple — but **untested**, and it must not be
    written up as a finding. Reading order, heading structure, table
    semantics and language metadata on a multi-element design are all
    unexamined. See the recommended follow-up below.
  - Classified: **508 §504.2/§504.3** (authoring tool must produce
    conformant output); bears on **1.1.1** and **2.4.2** *of the exported
    artifact* → finding **V-F17**. Scope call pending, as for V-F16.

## Notes

Session was W16 of `session-S3-reviewer-walkthrough.md` (T2 steps 3–5).
Instruments: NVDA 2026.1.1 + Chrome 151.0.7922.138, extensions disabled
(03 §1.5 hygiene note). The T2 document still lists as "Untitled - August
10, 2026 at 13.09.20", **not** "Test-With-Keyboard" — the R016 O11 rename
discrepancy remains unresolved and was visible throughout this session.

**T2's verdict is not set here.** W17 asks the reviewer for it; task
verdicts are the reviewer's call, not the assistant's.

## Evidence files in this folder

- (none captured — session was narrated; markup for O1 supplied by the
  reviewer and quoted inline above)

## Findings raised from this run

- **T2-F3** — export and download dialogs not announced; Cancel undiscoverable (O1, O4)
- **V-F16** — published output (`/publishedV2/`) is imperceptible to screen readers (O6)
- **V-F17** — tagged PDF export lacks alt text and document title (O7)
- No finding from O3 (feedback adequate via user agent) or O5 (CC survives video export — a credit)
