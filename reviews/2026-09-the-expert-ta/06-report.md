# Procurement Decision Record — The Expert TA

*Independent evaluation by the SFBRN Accessible Technology Initiative.*

**This file is not a report.** The two reports are generated from the
database and must never be hand-written:

| Output | Command | For |
|---|---|---|
| `2026-09-the-expert-ta-acr.html` / `.docx` | `python scripts/export_acr.py 2026-09-the-expert-ta --docx` | the supplier and the public |
| `2026-09-the-expert-ta-internal.html` / `.docx` | `python scripts/export_acr.py 2026-09-the-expert-ta --internal --docx` | the procurement team and the department, feeding a TAAP |

What lives here is the part no generator can produce: **the decision, why it
was taken, whether the vendor's own paperwork can be trusted, and what this
review did not cover.** Everything else — the criterion tables, the findings,
the functional-performance rollup, the remediation priorities, the user
limitations — is generated. If you find yourself writing any of it here, stop
and fix `05-results.md` instead, then regenerate.

## Procurement decision

| | |
|---|---|
| **Decision** | Approved with TAAP |
| **Decision date** | 2026-09-25 |
| **Decided by** | Daniel Fontaine (SFBRN ATI Coordinator), reviewer of record |
| **Rationale** | Answering and submitting a problem could not be completed with a screen reader, and five of the ten pages evaluated could not be used at all, so the product does not meet the CSU's WCAG 2.1 AA requirement on its own. The barriers are in how the controls are built rather than in the instructional content, and the vendor already implements the right pattern in several places, so a departmental alternative can carry affected students while remediation proceeds. |

**The decision is the reviewer's alone.** The assistant drafts the evidence
and may draft the rationale; it never sets the Decision field.

**The buckets** — apply the first one whose conditions all hold:

- **Approved** — the product may enter the campus ecosystem as it stands. No
  task verdict of **Fail**, no Blocker findings, and no "Does Not Support"
  outcome or Major finding that substantially burdens an essential task for
  any affected user group.
- **Approved with TAAP** — the product may be acquired only alongside a
  Temporary Alternative Access Plan. Task failures or Major barriers exist,
  but every essential task remains achievable through an alternative, and the
  vendor commits to remediation.
- **Do Not Purchase** — the product must not be acquired. One or more
  essential tasks are blocked for an affected user group with no workable
  alternative, or the vendor will not commit to remediation.

## Vendor ACR audit

*The section only an independent reviewer can write: is this vendor's
paperwork trustworthy? Nothing generates this, because it is a judgement
about a document rather than about the product.*

### Coverage

(Does the vendor's ACR address the conformance target at all? Standard and
version it was written against, criteria claimed vs in scope, obsolete
claims, unclaimed criteria — from `05` §Vendor evidence gap.)

### Reliability — claims vs verified

Every criterion where this review's outcome differs from the vendor's claim,
**in both directions** (query it, don't count by hand):

    python scripts/review_db.py query --review 2026-09-the-expert-ta \
      "SELECT sc, vendor_claim, outcome FROM criterion_outcomes
       WHERE review_id='2026-09-the-expert-ta' AND outcome <> 'Not Evaluated'
         AND vendor_claim NOT LIKE outcome || '%'"

| Criterion | Vendor claim | Verified | Direction | Note |
|-----------|--------------|----------|-----------|------|
| | | | worse / better than claimed | |

### What this means for relying on this vendor's ACRs

(1–3 sentences for procurement: over-claims, under-claims, blanket ratings,
staleness — the pattern, not the instances.)

## Coverage & limitations of this review

*The honesty box. What was not evaluated, and what that means for reading
the reports.*

(From `review_db.py completion` and `review.py coverage`: which views ×
modalities were tested and with which instruments; what remains untested;
standing caveats — a sample rather than the whole product, one browser and
one assistive-technology baseline, states that could not be reached with the
test account.)

## Concerns outside the conformance target

(Real product concerns WCAG does not cover — e.g. Section 508 §504
authoring-tool obligations for tools that produce content. Kept outside the
conformance statements; each needs a reviewer scope decision. Delete if
none.)

## Recommendation

*Drafted from the evidence for the reviewer to adopt, amend, or reject — the
Decision field above remains the reviewer's alone. One paragraph: which
bucket the evidence points to and why (task completability, remediation
outlook, vendor reliability); what would move the recommendation.*

## The record behind this

- Task-based test record and findings: `04-task-testing.md`
- Per-criterion results, the source both reports generate from: `05-results.md`
- Scope, sample and processes: `03-scope-and-sample.md`
- Evidence files, one folder per run: `evidence/runs/`
- Vendor ACR as received: `vendor-acr/`
- Live state of the review: `python scripts/review_db.py state 2026-09-the-expert-ta`
