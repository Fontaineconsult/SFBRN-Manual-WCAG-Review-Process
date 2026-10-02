# Test Run R064 — S3

| | |
|---|---|
| **Run ID** | R064 |
| **Date/time** | 2026-10-02 13:36 |
| **View / sample** | S3 |
| **Page URL / location** | https://learn.essentials-ai.com/learning/03baa839-0ace-4e3b-9d4c-9c2077dcf123 — UI: My Courses → Start course → 1 Intro to the Course → Icebreaker (video lesson) |
| **Task / process** | — |
| **Modality** | no-hearing |
| **Tool** | inspection |
| **Baseline** | — |
| **Tester** | assistant (inspection); reviewer judges NH1 — assistant records |
| **Result** | Not set (→ Works / Works with issues / Broken / N/A — see ontology/modality-checks.md) |

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
| NH2 — Live audio content has captions | n/a | O2 — no live media in the product |
| NH3 — Audio-only content has a transcript | n/a | O2 — no audio-only content; the only media is video with audio |
| NH4 — No information or feedback is conveyed by sound alone (visual equivalent exists) | n/a | O2 — no information or feedback is conveyed by sound alone (no Audio API; all feedback visual/textual) |

## Observations

Raw narration captured during the session. One numbered entry per thing
noticed; lifecycle: new → clarified → classified → finding:<ID> or dismissed.

Format:
- O1 [new] (state: which view state): what happened
  - Classified: <check ID> / WCAG <SC> / <severity> → finding <ID> | dismissed: <reason>

(none yet)
- O2 [new] (state: inspection of the lesson's media): One `<video controls preload=none>` (Supabase MP4, 36.8 s, 0 text tracks, no poster) — prerecorded video with synchronized audio. No live media anywhere in the product. No audio-only content. No sound-only feedback: the product uses no Audio API (probe), and every state change on the view is visual/textual. The reviewer stated 2026-09-30 that the videos carry **open (burned-in) captions**; the transcript below the player is prose without timestamps.

## Notes

(JAWS: Action / Announced / Expected-vs-actual triplets — copy exact speech
from Speech History, Insert+Space then H. WAVE: summary counts — Errors,
Contrast Errors, Alerts, Features/Structural — plus each distinct error type.
Conventions: ontology/testing-tools.md.)

**Assistant, 2026-10-02 (inspection).** NH1 is the reviewer's: play the Icebreaker video with sound off and judge whether the burned-in captions are accurate and complete for the whole 37 s (and legible at 400 % — note for 1.4.4). This run is the no-hearing cell for S3 (the probe skipped it because a video exists).

## Evidence files in this folder

- (screenshots/exports named R064-<what>.png)

## Findings raised from this run

- (finding IDs recorded in 04-task-testing.md, or "none")
