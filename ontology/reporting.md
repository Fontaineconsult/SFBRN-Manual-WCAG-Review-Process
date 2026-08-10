# The Review Report (06) — what it is and how it is derived

Added 2026-08-10, when the report's purpose was settled: the reviewing body
is an **internal CSU System-level team** reviewing ICT for all 23 campuses,
serving RFPs and systemwide purchase agreements. That decides the format.

## Not a VPAT/ACR — deliberately

A VPAT/ACR is a **vendor self-attestation**: the vendor's claims, in the
vendor's voice, structured per-criterion. This team is not the vendor; it is
the **verifier**. Producing an ACR-shaped report would discard the three
things only an independent reviewer can produce:

1. **A procurement decision** (Approved / Needs TAAP / Denied) with the
   evidence trail behind it.
2. **An audit of the vendor's ACR** — coverage (does it even address the
   target standard?) and reliability (where independent testing landed
   better or worse than claimed). This tells procurement whether this
   vendor's *future* paperwork can be trusted, which outlives any one
   product version.
3. **Contract-ready remediation asks** — specific, verifiable fixes that
   negotiators can attach to a purchase agreement as an exhibit, with a
   re-test method per item.

The per-criterion ACR-shaped rollup still exists — it is `05-results.md`,
and it remains the technical appendix and the working surface during
testing. The report cites it; it does not duplicate it.

## Audiences, and the section that serves each

| Audience | Needs | Section |
|---|---|---|
| CO procurement / RFP evaluators | comparable at-a-glance result across candidate products | **At a glance** + Decision |
| The decision-maker | evidence-backed decision rationale | Decision + Executive summary + Task outcomes |
| Campus accessibility officers (23 campuses) | what to accommodate while barriers stand | Key findings + TAAP inputs |
| Contract negotiators | what to demand and how to verify delivery | **Remediation exhibit** |
| Vendors receiving the report | precise, rebuttal-proof defect statements | Key findings (root causes, not symptoms) |
| The next reviewer of this product | what was and wasn't covered | Coverage & limitations |

## Derivation is mechanical (like walkthroughs — no invention)

Every section is filled from the live files, never from memory:

- **Task outcomes** ← `04` §A verdicts, verbatim.
- **Key findings** ← `04` findings, ranked by user impact, each carrying its
  **root cause** where one was identified (a vendor can act on
  "`role="row"` has no grid parent"; not on "the grid is hard to use") and
  its evidence run IDs.
- **Vendor ACR audit** ← `05` (every criterion where Outcome ≠ Vendor
  claim, in both directions — landing *better* than claimed is reported as
  prominently as worse; that is what makes the audit credible) + the
  coverage arithmetic from `05` §Vendor evidence gap.
- **Results summary** ← `05` outcome counts by level.
- **Remediation exhibit** ← findings that carry a specific fix; each row
  names its verification method (NVDA re-test step, axe rule, or
  measurement).
- **Coverage & limitations** ← `validate` + `matrix` output, instruments
  and baselines from `03` §1.3/§1.5, plus any standing caveats (e.g. a
  single-AT evidence base).
- **Automated sweep record** ← each sweep run's triage (W1–W3 checks in its
  `run.md`): per-view counts + disposition of every violation (confirmed →
  finding ID / dismissed with reason / **false positive, with the
  refuting measurement**). Dismissals and false positives are reported as
  prominently as confirmations — a vendor re-running the same tool will hit
  them, and the report pre-empting that is what makes the manual findings
  credible. Instrument blind spots demonstrated on this product (canvas,
  WAVE/shadow DOM, unresolvable backgrounds) are stated here, not buried.
- **Concerns outside the conformance target** ← anything real that WCAG
  does not cover (e.g. 508 §504 authoring-tool output). Kept **outside**
  the conformance statements so neither contaminates the other.

## Distribution format

`python scripts/export_report.py <review>` renders `06-report.md` to
`reviews/<id>/<id>-report.docx` (python-docx; no pandoc dependency). The
markdown is the system of record — **edit it and re-export; never hand-edit
facts into the Word file.** The export uses real Heading 1–3 styles and real
tables with repeating header rows (the accessible way to build a Word doc),
but run Word's own Accessibility Checker before official distribution, and
fill Word-side metadata (document title, author) there.

## Rules

- **The decision stays human.** The report scaffolds evidence and
  rationale; Decision / date / decided-by are the reviewer's alone, and the
  `| **Decision** |` row's placeholder text is the CLI's parse contract —
  keep the row shape intact.
- **Report status is explicit**: `INTERIM` while `validate` still lists
  gaps, `FINAL` only when it passes clean. An interim report states what is
  untested rather than implying completeness.
- **Positives are findings too.** What works (and where testing landed
  better than the vendor claimed) is stated with the same precision as
  failures — it is what makes the criticism credible and the comparison
  fair across RFP candidates.
- **No new facts in 06.** Everything cites a finding ID, run ID, or `05`
  entry. If the report needs a fact that exists nowhere else, the fact goes
  into the run/finding first.
