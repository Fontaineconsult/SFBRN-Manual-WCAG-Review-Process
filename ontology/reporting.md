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
- **Coverage & limitations** ← `validate` + `matrix` + `coverage` output, instruments
  and baselines from `03` §1.3/§1.5, plus any standing caveats (e.g. a
  single-AT evidence base).
- **Findings by modality (508 FPC)** ← the modality→WCAG map in
  `modality-checks.md` × the coverage matrix × findings. Every modality gets
  a row even when N/A or untested — an absent row reads as "fine". Untested
  rows say what remains untested and why it matters ("S3's media assets
  make hearing non-N/A"), never just "pending".
- **Barriers at the TAAP threshold** ← the findings that individually
  prevent "Approved" (each substantially burdens an essential task for an
  affected group — the decision-bucket language applied finding by
  finding). One row per barrier with group, task, criteria, finding IDs;
  close with what does *not* reach the threshold so the list is a
  judgment, not an inventory. Feeds TAAP "Affected functionality" directly.
- **Dual conformance target**: the primary target is WCAG 2.1 AA (ADA
  Title II baseline); WCAG 2.2 AA is additionally evaluated. Results
  tables report the full 2.2 set with a stated 2.1-subset rollup, and the
  vendor-ACR coverage critique distinguishes "matches the 2.1 primary
  target" from "holds no position on the 2.2 additions."
- **Recommendation** ← last section before appendices. Drafted from
  evidence, explicitly labelled as for the reviewer to adopt/amend/reject;
  names the bucket the evidence points to, what would move it, and what the
  evidence does *not* support. The Decision field itself is never filled by
  the drafter.
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

## Prose style (reviewer-set, 2026-08-13)

- **Banned word:** "precisely" (use "exactly", "narrowly", or drop it).
- **Banned phrase:** "and that is what matters most" and its "matters
  most" variants — state the consequence, not its rank.
- **Never attribute intention to the developer.** Report what the product
  does, not why. "The same techniques are present in some components and
  absent from others" — not "this proves it is a choice, not a
  limitation." We observe behavior; we do not know minds or roadmaps.
- **No rhetorical framing devices.** Headers and asides like "framing that
  survives vendor rebuttal" argue with an imagined opponent. State what
  the evidence supports and what it does not; the reader draws the
  conclusion. Precision in the claims is the whole defense — it does not
  need to be announced.

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

## Second output: the WCAG-EM report (org-neutral, for use outside the CSU)

Added 2026-09-11. A review now produces **two** reports from the same
evidence base:

| | Internal review report (`06-report.md`) | WCAG-EM report (`<id>-wcag-em-report.html`) |
|---|---|---|
| Audience | CSU procurement, decision-maker, campus officers, negotiators | anyone outside the org: the vendor, other institutions, auditors, a public-records request |
| Shape | this doc's sections (decision, TAAP, ACR audit, remediation exhibit) | the W3C WCAG-EM Report Tool structure, verbatim |
| Carries | procurement context: decision, TAAP inputs, requisition, campus needs, vendor-ACR reliability | conformance evidence only |
| Never carries | — | the procurement decision, TAAP, requisition/department/requestor, cost or contract language, the vendor-ACR audit, internal-only caveats |
| Status | INTERIM / FINAL | same value, copied — an interim `06` can only yield an interim EM report |
| Source of truth | `01`–`05` | the same files; **no fact may exist only in the EM report** |

The internal report is the deliverable; the EM report is its **appendix**
in the W3C's interchange shape, so a reader who has never seen this process
can still verify scope, sample, method and per-criterion results. It is
generated, never authored: `python scripts/export_report.py <review>
--format wcag-em` fills `templates/review/wcag-em-report.html`
(**generator not yet written** — the template and this section come first so
the script has a contract to meet). Output:
`reviews/<id>/<id>-wcag-em-report.html`, generated output like the .docx —
regenerate, never hand-edit.

### Template provenance

The template is the WCAG-EM Report Tool's own HTML export (2.2 AA, 55
criteria, saved 2026-09-11) with values replaced by `{{…}}` placeholders and
one browser-extension artefact (`data-landmark-index`) stripped. The section
order, headings, guideline tables and result vocabulary are kept **exactly**
so the file is recognisably EM-conformant and comparable with reports from
other evaluators. Two additions are ours: a status line under the H1, and
the product name in `<title>`/H1.

### Derivation (mechanical, like `06`)

| EM section / placeholder | Filled from | Notes |
|---|---|---|
| `{{REPORT_CREATOR}}` | `01` Reviewer(s) | team name, not individuals' emails |
| `{{COMMISSIONER}}` | `01` Requesting department, org-level wording | "California State University, <campus>" — no requestor name/email, no PO |
| `{{REPORT_DATE}}`, `{{REPORT_STATUS}}`, `{{REVIEW_ID}}` | `06` header table | status is copied, never upgraded |
| `{{EXECUTIVE_SUMMARY}}` | `06` §Executive summary | with internal references (decision bucket, TAAP, campus) removed; states the task outcomes and the character of the barriers |
| `{{PRODUCT_NAME}}`, `{{PRODUCT_SCOPE}}` | `01` Product name + Version; `03` §1.1 boundary, inclusions, exclusions with justification | scope is the enclosure boundary, not the sample |
| `{{WCAG_VERSION}}`, `{{CONFORMANCE_TARGET}}` | `03` §1.2 | "2.2" / "AA (WCAG 2.1 AA primary target; 2.2 additions also evaluated)" — the dual target is stated, not hidden |
| `{{SUPPORT_BASELINE}}` | `03` §1.3 rows **actually used** | OS + browser + AT + versions, as a list; unused baseline rows are omitted |
| `{{ADDITIONAL_REQUIREMENTS}}` | `03` §1.4 | "None" when empty |
| Summary counts `{{N_*}}` | computed from the mapped results | `{{N_REPORTED}}` = 55 − Not checked |
| `{{R:x.y.z}}` | `05` Outcome via the mapping below | |
| `{{O:x.y.z}}` | `05` Task findings + Remarks, expanded | see "Observations" below |
| `{{SAMPLE_SET}}` | `03` §3.1 structured + §3.2 random | one list item per S/R row: ID, view name, durable locator, what it represents; random items flagged "(random)" with the selection method stated once |
| `{{TECHNOLOGY}}` | `03` §2.4 | technologies relied upon, with versions where known |
| `{{EVALUATION_SPECIFICS}}` | `03` §1.5 tools + versions; run count and date range from `evidence/runs`; coverage from `coverage` (principle and FPC tables) and `matrix`/`validate`; the sweep-triage summary from `06` §Automated sweep record | instrument blind spots demonstrated on this product are stated here, same as in `06` |

### Outcome mapping (ACR vocabulary → WCAG-EM result)

`05` keeps the fixed ACR vocabulary; the EM report uses the Report Tool's.
The mapping is one-way and is applied only by the generator:

| `05` Outcome | EM Result | Observations must open with |
|---|---|---|
| Supports | Passed | what was tested and where (sample IDs), so a pass is evidence, not silence |
| Partially Supports | Failed | "Partially supports —" then the failing functionality; the ACR distinction is preserved in the text because EM has no partial result |
| Does Not Support | Failed | "Does not support —" then the failing functionality |
| Not Applicable | Not present | why the criterion has no applicable content in the sample |
| Not Evaluated | Not checked | nothing (interim reports only; a FINAL report has zero) |
| Not Evaluated **and** Remarks record "Unmeasured" with the instrument that could not reach it | Cannot tell | the instrument limit, and what would resolve it |

`Cannot tell` is the only result the generator derives from Remarks rather
than Outcome; it is never written into `05` (the ACR vocabulary is fixed).

### Observations (the per-criterion cell)

Each cell is self-contained for a reader without repo access:

- the outcome phrase from the mapping table;
- one sentence per cited finding: **what** fails, **where** (sample ID and
  view name; the durable locator for the view), **for whom** (the modality
  blocked), and the finding ID in parentheses for traceability;
- the method: instrument and baseline (e.g., "NVDA 2026.2 / Chrome 152,
  B5"), never a tool-only claim — an axe result appears only as
  "confirmed under NVDA" or as the refuting measurement;
- for Passed: the sample items and method on which it passed.

Run IDs, evidence file names, reviewer quotations and internal caveats stay
in `04`/`05`; observations are prose, not pointers.

### Rules specific to the EM report

- **Org-neutral means org-neutral.** Nothing about the decision, TAAP,
  budget, requisition, department, or campus needs. If a fact is needed to
  understand a barrier, it belongs in the observation as product behaviour.
- **No positives lost.** Every Supports becomes a Passed with its evidence;
  a report that lists only failures misrepresents the product to outsiders
  just as it would to procurement.
- **Same status, same date** as the `06` it was generated with; regenerate
  both together.
- **Accessibility of the output**: the template's own markup (headings,
  `scope`d table headers, `aria-labelledby` tables, `lang`) is preserved;
  the generator adds no colour-only meaning and no scripts.


## Third output: the independently-verified ACR (2026-09-24)

`python scripts/export_acr.py <review> [--open]` writes
`reviews/<id>/<id>-acr.html`, a VPAT® 2.5-shaped Accessibility Conformance
Report.

**This does not reverse "Not a VPAT/ACR — deliberately" above.** That
section rules out shaping **`06`** like an ACR, and its three reasons still
hold — `06` carries a procurement decision, an audit of the vendor's own
ACR, and contract-ready remediation asks, none of which fit a per-criterion
grid. The ACR is a **third output alongside** `06` and the WCAG-EM report,
added at the reviewer's request for the case the other two cannot serve: a
counterparty who can only consume the standard grid — a campus procurement
office, an RFP response packet, or the vendor being handed verified results
in the format their own paperwork uses.

**What makes it legitimate rather than a self-attestation in disguise** is
stated in the document's own header, not just here: a vendor's ACR is a
**self-attestation**; this one is an **independent evaluation**, and every
conformance level in it derives from logged runs. Where the vendor's own
claim is known it is printed beside the verified level, for comparison, and
carries no weight in it.

### Derivation (from the database, never from prose)

Unlike `06` and the WCAG-EM report, which are derived from the stage files,
the ACR is generated **entirely from `reviews/<id>/<id>.sqlite`**. The
reviewer's instruction on 2026-09-24 was explicit: *"generating a industry
standard ACR from the data in the databse, never from your notes"*. So:

| ACR section | Source, in the mirror |
|---|---|
| Report information | `reviews`, `views` (including `removed`), `runs`, `tasks`, `findings` |
| Table 1 / Table 2 (Level A / AA) | `criterion_outcomes.outcome`, `.remarks`, `.task_findings`, `.vendor_claim`, joined to `wcag_criteria` for name, level and order |
| Evidence line under each criterion | counts of answered and failing `check_outcomes` rows on live views, via `check_criteria` |
| Chapter 3 (FPC) | `fpc` × `runs.result` × `check_outcomes`, per modality |
| Findings table | `findings` (live only) with `finding_criteria`, `finding_runs` |

**No cell is authored by hand**, and the script adds structure only — never
judgement. A remark is the `05` remark verbatim. The corollary is that the
ACR can only be as good as the extraction contract in `data-store.md`: if a
fact is not in an extracted field, it does not reach the report.

### Rules specific to the ACR

- **Untested is said out loud.** A criterion still `Not Evaluated` is
  printed as such; a functional performance criterion whose sampled views do
  not all carry a run Result is reported **Not Evaluated**, never inferred
  from the rows that happen to be answered. Silence must never read as a pass.
- **Conformance vocabulary is the ACR's, not ours.** Supports / Partially
  Supports / Does Not Support / Not Applicable / Not Evaluated — which is
  why `05` uses the same terms and no mapping is needed (contrast the
  WCAG-EM report, which needs §Outcome mapping).
- **Markdown is rendered, not printed.** `05` is authored in Markdown; the
  generator escapes first, then honours `**bold**` and `` `code` ``, and
  strips any marker left stranded by a trimmed cell. A counterparty must
  never see raw `**`.
- **Severity is the bare word.** The record keeps the reviewer's reasoning
  in the same field ("Minor (proposed …)"); the report's severity column
  prints the rating alone.
- **The report is itself accessible**, and is checked for it: `lang`,
  `scope`d headers on every table, headings in order, status carried by a
  **word** and not by colour alone, explicit background, dark mode guarded,
  no scripts and no network requests. An inaccessible accessibility report
  is not publishable.
- **A functional performance criterion is never reported "Not Evaluated"
  because a corner is missing.** Corrected 2026-09-24: the first version
  demanded every sampled view carry a run Result *and* zero blank rows, so
  302.1 printed "Not Evaluated" over **119 answered check rows and 46 failures**
  because one view lacked a Result. That misrepresents the work and, worse,
  understates the risk. The rule now: derive the level from the evidence that
  exists, and **state the coverage limit in the same cell** -- how many pages
  carry a completed result, how many rows are outstanding, and which pages are
  still owed, by name. "Not Evaluated" is reserved for a modality where
  nothing was tested at all.

- **No internal identifiers in reader-facing text.** Finding IDs, run IDs,
  observation numbers, walkthrough steps, check codes and view codes are the
  review's bookkeeping; a counterparty cannot resolve them and should never
  see them (reviewer, 2026-09-24: *"nobody reading this will know anything
  about the internal jargon like F-12 or V-36, don't put those in"*). The
  generator strips all of them and substitutes the **page name** wherever a
  view code appeared. The issues table is numbered per report rather than by
  finding ID.

- **One statement per block, and every statement says where.** Each criterion
  renders as a short lead plus one bullet per distinct finding, each opening
  with the page in words and its short path (`/Common/Calendar.aspx`), so a
  reader can go and look. Attribution clauses ("the reviewer found", "reviewer's
  ruling") are dropped: the document is already attributed in its header, and
  repeating it on every line puts narration between the reader and the fact.

- **Half the words of the record, and none of its housekeeping.** The `05`
  remarks are a working surface: they carry dates, provenance ("Decided … on
  the grayscale pass"), status markers (`[provisional — reviewer confirms]`)
  and attribution on every observation. A conformance report carries none of
  it — the reader wants what is wrong and where. The generator therefore
  strips dates, provenance openers, bracketed status markers and attribution
  clauses, then takes **the first complete statement only** for a lead and for
  each bullet. Measured on The Expert TA: 14,360 words → 7,016, a 52 % cut,
  with no conformance level or page reference lost.

- **Repeated statements are merged; long lists are capped.** Findings that say
  the same thing on different pages become one bullet naming both; more than
  three pages collapses to "X and N other pages". A criterion shows its **five
  worst** statements (Blocker, then Major, then Minor) and a line pointing at
  the issues table for the rest, which keeps every one.

- **Never publish a fragment.** Removing an identifier from the head of a
  sentence can orphan its verb ("CO10 fails on all 10 views" → "fails on all
  10 views"). The generator detects a lead-in that now starts lower-case and
  begins at the next complete sentence instead.

- **The report states facts; it does not quote the reviewer.** The record
  attributes and quotes because that is how a review file should read. A
  conformance report should not: "I have not encountered any keyboard traps"
  becomes *No keyboard traps encountered*. Quotation is kept for text the
  **product** shows — a button caption, a field label, an announcement —
  which is short and capitalised; the reviewer's own words are stated plainly.
  The distinction matters: the button called "I give up" must survive a pass
  that removes first person.

- **No check counts.** "30 checks recorded, 5 failing" describes how the review
  was run, not what the product does, and it belongs to the dashboard.

- **No evidence-accumulation narration.** The record grows top to bottom, so it
  says things like "now stand on both Class Management pages". A report is a
  statement of the product's state, read in any order; that phrasing is
  stripped.

- **Statements are whole sentences.** Length is controlled by taking **one
  sentence**, never by cutting one short: a clause-boundary trim produced
  fragments ("Tab reaches nothing in the row, and Enter."), and an ellipsis
  reads as if something was withheld. A sentence that ends inside a closing
  quote or a bold marker still counts as ending — that boundary is easy to
  miss and was, at first.

- **Standalone: no supplier claims anywhere.** The ACR reports what the
  evaluation found and nothing else. Comparing the supplier's ACR against
  verified results is a real and valuable job, but it is **`06`'s** job (see
  "Not a VPAT/ACR" above) and mixing it in here muddles a conformance
  statement with an audit. The header says so explicitly.

- **Not Applicable is a statement, not an argument.** No justification, no
  method, no cross-reference — "No audio-only or video-only prerecorded media
  in the sample." and stop. The generator takes the first clause of the record
  that stands on its own; where the record offers only a cross-reference ("As
  1.2.3"), a dangling pronoun or a check outcome, it falls back to "Not present
  in the evaluated sample", which asserts nothing beyond the level itself.

- **Never say it twice.** Where a criterion's lead repeats what one of its
  bullets says, the lead is dropped — the bullet is the better of the two
  because it names the page and the severity. Compared on content words so a
  paraphrase still counts.

- **Shaped to VPAT® 2.5Rev, WCAG edition.** The reviewer supplied the ITI
  template at `ontology/VPAT2.5Rev_WCAG_February2025.docx` on 2026-09-24; the
  generator follows its Essential Requirements for Authors: report title in
  the form "[Product] Accessibility Conformance Report", template version,
  product name, report date, product description, contact information, notes,
  evaluation methods, an applicable-standards table, the terms table, then
  Table 1 (Level A) and Table 2 (Level AA) with the columns **Criteria /
  Conformance Level / Remarks and Explanations**, then a legal disclaimer.
  Criterion names carry their level, as the template does:
  "1.1.1 Non-text Content (Level A)". The **report date is derived from the
  review's own identifier** (month and year), so the document stays
  deterministic.

  Two deliberate departures, both stated in the document: the **508 Functional
  Performance Criteria** are reported although the WCAG edition does not
  include them (the reviewer wants them kept), and Chapters 4–6 are **not**
  reported, being neither part of this edition nor evaluated.

- **A passing criterion is not argued.** `Supports` prints one standard
  sentence and nothing else. This was learned the hard way: mining the record
  for a sentence produced method ("Ten views walked with a keyboard"),
  fragments ("Passes on all 10 views") and, worst, text that read like a
  failure sitting under a passing level ("The probe measured newly clipping
  containers"). Every further rule traded one bad case for another. The level
  *is* the statement (reviewer, 2026-09-24: "don't justify it, don't tell us a
  story"). `Not Applicable` keeps a mined reason only because the record
  states absences cleanly ("no video on any sampled view"), with a standard
  fallback when it does not.

- **Nothing may point at what the report does not contain.** A statement that
  opens "The markup explains it:" or "This confirms that …" refers to
  something the record said and the report does not; such openings are
  stripped. The same applies to evidence filenames left behind when a run
  identifier is removed.

- **Vendor Roadmap (added 2026-09-24; named Priorities for remediation for
  half a day).** The procurement gate has
  two faces: what the **vendor** is expected to fix, and what the
  **department** does meanwhile. The ACR carries the first; the TAAP
  (`ontology/TAAP Version 3_2 051225.docx`) carries the second. At this stage
  of the gate the purpose is narrow — show that the position is known and
  monitored — so the section makes no demands and sets no dates.

  **Categories are derived, not authored**, from conformance level and
  outcome, so they carry over to any review unchanged:

  | Category | Rule |
  |---|---|
  | Needs Immediate Attention | Level A, Does Not Support |
  | Should be Prioritized | Level A, Partially Supports |
  | For Full Compliance | Level AA, Does Not Support |

  **The section states the requirement, not just the gap.** The CSU requires
  that ICT it acquires conform to **WCAG 2.1 Level AA**, and the roadmap says
  so, together with the fact that continued failure *may* jeopardize future
  acquisitions — "may", because the decision is the reviewer's and the
  procurement officer's, and this document does not make it.

  The report is evaluated against WCAG **2.2**; the requirement quoted is
  **2.1**. Those normally coincide — a product failing at this level fails on
  criteria that have been in the standard since 2.0 — and a first version
  closed the section with a computed sentence saying so. It was cut: the
  section is three sentences of requirement followed by the table, and the
  standards arithmetic belonged nowhere near it. Keep the check in mind when a
  review turns up a **2.2-only** failure, because the paragraph as written
  claims the list delivers 2.1 AA.

  Level A is the higher priority throughout: it is the floor of the standard.
  **Partial support at Level AA is deliberately excluded** — listing
  everything makes the section unusable, and it is already in the tables above.

  An earlier version grouped findings into hand-written engineering themes
  ("make every control a control", "retire layout tables"). It was dropped:
  the themes were bound to one product so the section would not generalise,
  and grouping by what a fix costs reads as a set of demands.

  **The cell is an instruction, not a summary.** By the time a reader reaches
  this section they know what is wrong — they have just read the criterion
  tables. What the section adds is the *work*: the authored `Remediation`
  field, below.

- **The `Remediation` field — what to do, per criterion.** Added 2026-09-24,
  after a first version of Priorities carried each criterion's worst finding
  sentence and read, correctly, as "just summaries of the findings". A
  restatement of the defect is not a plan.

  So each criterion the section publishes carries **one authored instruction**,
  stored as `criterion_outcomes.remediation` and extracted from a
  `- **Remediation:**` line in the `05` criterion block. The report prints it
  verbatim.

  **The rules, which are checked and not merely documented**
  (`REMEDIATION_RULES` in `scripts/review_db.py`, reported by
  `review_db.py check`):

  1. **Imperative.** "Give every informative image an `alt` attribute", not
     "images lack alternative text".
  2. **Covers all of that criterion's findings**, not the worst one. This is
     why the field sits on the criterion and not on the finding: 4.1.2 has
     eighteen findings and one fix.
  3. **Names the product's own working example where one exists.** This review
     kept finding that the vendor already does the right thing somewhere —
     headings on the solutions page, a symbol on the status marks, a label on
     the sign-in form, a confirmation on one of the three scoring controls.
     Pointing at it turns a demand into "do what you already do", which is both
     more actionable and more accurate.
  4. **Says what to build, never which framework or library to use.** How is
     the vendor's decision; naming a framework in a procurement document is
     both out of scope and easy to dismiss.
  5. **No internal identifiers, no dates, no attribution.**
  6. **At most 450 characters** — longer than a `Plain summary` because an
     instruction covering several findings needs the room, short enough that
     the table stays readable.

  **Required** on any criterion that is Does Not Support at either level, or
  Partially Supports at Level A — exactly the set Priorities publishes.
  Optional elsewhere. `review_db.py check` reports *remediation missing* and
  *remediation breaks a rule*; both count toward C11.

  **Derived from the findings, not from the report generator.** The
  instruction must be supportable by that criterion's own findings and
  remarks. As with `Plain summary`, the authoring happens once, into the
  record; the generator only selects and prints.

- **The `Plain summary` field — the one sentence written for a reader.**
  Added 2026-09-24 after three attempts to convert working notes into
  publishable prose mechanically. Every other field in a finding is a working
  field: informal, attributed, dated, full of identifiers. That is correct for
  a review file and wrong for a report, and no amount of stripping fixes it —
  each pass produced fragments ("Fails on all 10 views."), dangling references
  ("The pattern is one mechanism:") or the same sentence under two different
  criteria.

  So each finding carries **one authored sentence**, stored in the database as
  `findings.plain_summary` and extracted from a `| **Plain summary** | … |`
  row in the `04` finding block. The report uses it verbatim; it needs no
  cleaning because it was written for this purpose.

  **The rules, which are checked and not merely documented** (`PLAIN_RULES` in
  `scripts/review_db.py`, reported by `review_db.py check`):

  1. **One sentence**, ending in a full stop. Not two, not a fragment.
  2. **About the product, in the present tense** — not about the test, the
     reviewer, the tool, or when it happened.
  3. **States what is wrong _and_ what a user cannot do because of it.** The
     second half is what makes it useful to a procurement reader.
  4. **No internal identifiers** — no finding, run, observation, step, check
     or view codes. Name the page in words where the page matters.
  5. **No dates, no attribution, no quoting the reviewer.** Text the *product*
     shows may be quoted.
  6. **Plain language.** The reader is a procurement officer, not an engineer.
  7. **At most 200 characters**, so it fits a table cell.

  **Derived, not invented.** The sentence must be supportable by that
  finding's own `Observed` cell: it restates, it does not add. The authoring
  is the only writing in the pipeline, and it happens once, into the record —
  never in the generator.

  `review_db.py check` reports two integrity issues against these rules:
  *plain summary missing* (a live finding has none) and *plain summary breaks
  a rule* (naming which rule). Both count toward C11.

  **Where the report uses it**: as the statement in each criterion's bullets.
  Priorities uses the criterion-level `Remediation` instead — an early version
  put the worst finding's sentence there and three different criteria ended up
  quoting the same one.

- **Who produced it, and who to ask.** The standing note names the evaluating
  body and the reason the evaluation exists: *produced by the SFBRN Accessible
  Technology Initiative during a procurement requisition, to determine whether
  the product meets the CSU's accessibility requirements for acquisition.*
  "Acquisition" rather than "purchase" because it is the CSU's own term and
  covers licences and renewals, which is most of what passes this gate.

  The body is organisation identity, so it lives in `branding.json` under
  `body` (the article is part of the value; the Report-information cell strips
  it). The **reviewer of record and their contact address** are per-review, so
  they come from the record: `01-intake.md` `**Reviewer(s)**` (the name before
  the first parenthesis) and a `**Reviewer contact**` row added to the intake
  template, mirrored into `reviews.evaluator` / `reviews.evaluator_contact`.
  A conformance report nobody can ask a question about is worth less than one
  that names a person.

- **Interim, and what closes it.** `06`'s Report-status line is a template
  choice — `INTERIM (testing in progress) / FINAL` — until the reviewer
  resolves it; printed raw it showed the reader both at once, so the report
  prints the one that applies. An interim report also states **what would make
  it final**, or a reader cannot tell a provisional level from a settled one.

  The gate is the definition of done (`review_db.py completion`, C1–C12):
  every criterion decided and evidenced, every task cluster given a verdict,
  every run resulted, every check row answered, every view swept, every FPC
  exercised, every finding evidenced, the `04` §D coverage boxes checked and
  the integrity queries clean — C1–C11, all mechanical. **C12 is the
  reviewer's own act**: record the procurement decision in `06` (Approved /
  Needs TAAP / Denied) and set the report status to FINAL. The assistant never
  takes C12.

- **The report's name.** The document is
  **San Francisco Bay Region Network Manual Product Accessibility Evaluation**
  (`REPORT_NAME`), named for the process that produced it rather than the
  format it borrows. The product is the subject line under it, where the
  VPAT/ACR lineage is also stated.

- **Branding header.** The report goes out under an organisation's name, so
  the page opens with a header slot: logo, organisation, and an optional
  second line. It is filled from **`branding.json` at the repo root** (copy
  `branding.example.json`), so a regeneration never loses it, and overridden
  per-run by `--org` / `--unit` / `--logo`. With nothing configured the slot
  renders as an HTML comment and nothing else — no empty box and no
  placeholder text that could survive into a distributed document.

  The logo is **embedded as a data URI, not linked**. The report is mailed as
  one file and opened in Word; both lose a relative `src`. When the
  organisation name is also written out the image is marked decorative,
  otherwise it carries the name as its `alt` — and with the SFBRN wordmark
  above a heading that begins "San Francisco Bay Region Network", `alt` is
  correctly empty.

  **A raster sibling wins over an SVG.** Word's HTML importer does not render
  an SVG data URI — the header arrives as a broken image — while browsers and
  PDF want the vector. So a `logo.png` sitting next to the configured
  `logo.svg` is used automatically, and both renderers are served without a
  second config entry.

  The wordmark's text is near-black, which vanishes on the dark theme. It is
  given a white chip there rather than a CSS filter, which would have shifted
  the brand's own colours.

- **No legal disclaimer.** Removed 2026-09-24. It said the report was
  informational and not a warranty, which undercut the one thing the document
  is for. What remains is the colophon: the source-database hash, and the ITI
  service-mark attribution that VPAT's Essential Requirements oblige any
  report using the format to carry.

- **Styled for two renderers.** On screen it is a web page; opened or pasted
  into Word it becomes a document, and Word's HTML importer understands almost
  no modern CSS. So the stylesheet (lifted into the `CSS` constant, where it
  can be commented) obeys four rules: every colour that carries meaning is a
  literal hex, never a `var()` — Word drops `var()` silently and the
  conformance pills would keep their shape and lose their colour; no flexbox
  and no grid, so Report information is a table rather than a `dl`; column
  widths come from `<colgroup>`, which Word honours and CSS selectors it does
  not; and `thead { display: table-header-group }` plus
  `page-break-inside: avoid` keep headers repeating and rows whole across
  pages. `@page` sets the print margin. Spacing throughout is tight on
  purpose — this is a document to be read in a procurement file, not a
  landing page.

- **Deterministic**: no timestamps in the body, so a diff on the committed
  page means the review changed. Never hand-edit it — change `05` (or the
  runs behind it) and regenerate.
