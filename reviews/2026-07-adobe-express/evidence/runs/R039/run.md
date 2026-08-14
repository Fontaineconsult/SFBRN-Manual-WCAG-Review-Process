# Test Run R039 — Learn

| | |
|---|---|
| **Run ID** | R039 |
| **Date/time** | 2026-08-14 13:31 |
| **View / sample** | Learn |
| **Page URL / location** | https://new.express.adobe.com/learn |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | reviewer (D. Fontaine) - cursory pass |
| **Result** | Works with issues |

**Result reasoning** (set 2026-08-14). Captions are present on Learn's
videos and on insertable media, so a deaf or hard-of-hearing user can use
the tutorial content — the primary no-hearing need is met. The issue is
**no audio description anywhere**, which fails 1.2.5 outright and 1.2.3
unless transcripts exist (unchecked). **Cursory basis** — presence/absence
of tracks only; caption accuracy, sync and speaker identification were not
assessed.

**When you set the Result, replace this cell with the bare term and
nothing else** — `Works`, `Works with issues`, `Broken` or `N/A`. `matrix`
matches the cell against those exact strings and prints anything else
verbatim, which blows the grid apart (hit 2026-08-14). Put the reasoning
in a `**Result reasoning.**` paragraph directly below this table — that is
where it belongs anyway, and there is no length limit there.

## Checks (no-hearing)

Outcome: pass / fail / partial / n/a — every row must get one before the
run's Result is set. Fails cite observation IDs.

| Check | Outcome | Observations |
|-------|---------|--------------|
| NH1 — Prerecorded video has accurate captions | | |
| NH2 — Live audio content has captions | | |
| NH3 — Audio-only content has a transcript | | |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | | |

## Observations

**Basis and its limits — read before citing this run.** Reviewer's own
framing: *"let's do this cursory."* This is a **survey pass**, not a full
media evaluation. It establishes presence and absence of caption and
audio-description tracks; it does **not** assess caption *accuracy*,
synchronisation, speaker identification, or sound description. Recorded
this way so a later reader knows exactly what it will and will not bear.
Covers **Learn's tutorial videos** (Adobe's own content, where 1.2.x
applies directly) and **insertable media** from the asset panel.

- **O1 [classified]** (Learn videos + insertable media — reviewer,
  2026-08-14): **videos contain captions.**
  - Closes the outstanding 1.2.2 question the report has carried since the
    matrix was completed — Learn's videos were the one place in the product
    where 1.2.2 applies to Adobe's *own* published content rather than to
    an authoring capability, and they are captioned.
  - Consistent with R030 (auto-captions available for user-inserted video)
    and R037 O5 (captions survive video export). **Captioning is the one
    media affordance this product handles consistently well.**
  - Classified: NH1/NH2 / WCAG **1.2.2** / pass — no finding

- **O2 [classified]** (same pass — reviewer): **no audio-described
  video.** No audio description track was found on any video.
  - **This fails two criteria, and they behave differently:**
    - **1.2.5 (AA) is failed cleanly.** It requires audio description
      specifically; no alternative is permitted. No AD → Does Not Support.
      This one is not in doubt.
    - **1.2.3 (A) is failed on present evidence but has an escape route
      that was not checked.** 1.2.3 accepts *either* audio description
      **or** a full media alternative (a transcript). Captions alone do not
      satisfy it — captions carry dialogue, whereas 1.2.3 exists to convey
      the *visual* information a non-sighted user misses. **If Learn
      provides transcripts, 1.2.3 rises to Supports.** Not checked in this
      cursory pass; named here as the specific thing that would change the
      outcome.
  - **Why it bites harder on this product than most.** Learn's videos teach
    a **visual design tool**. Their content is disproportionately visual —
    "drag this here, the panel looks like this" — which is exactly what
    audio description exists to convey. A blind user is the one most in
    need of instruction in a canvas application and the least served by an
    uncaptioned-for-vision tutorial.
  - Classified: NH3 / WCAG **1.2.3** (A), **1.2.5** (AA) / Major →
    recorded in 05; no separate finding raised at this depth

- **O3 [classified]** (audio in the product's own UI — carried from the
  completed no-hearing runs R024/R026/R027/R030, not newly tested): the
  product's interface emits **no audio of its own**, and the asset panel's
  video previews are **muted** (R014 O6). No auto-playing audio exists to
  control.
  - Classified: WCAG **1.4.2** / pass — Supports

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

## Evidence files in this folder

- (screenshots/exports named R039-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
