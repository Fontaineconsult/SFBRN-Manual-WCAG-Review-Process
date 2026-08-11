# ICT Accessibility Review Report — {{PRODUCT_NAME}}

Independent verification by the CSU System-level ICT accessibility review
team, serving campus RFPs and systemwide purchase agreements. This is **not
a vendor VPAT/ACR** — the vendor's self-attestation is audited in §Vendor
ACR audit; the per-criterion technical record is `05-results.md`.
Derivation rules: `ontology/reporting.md`.

| | |
|---|---|
| **Review ID** | {{REVIEW_ID}} |
| **Report status** | INTERIM (testing in progress) / FINAL |
| **Report date** | |
| **Reviewer(s)** | |
| **Product & version** | {{PRODUCT_NAME}} |
| **Vendor ACR reviewed** | (title, date, standard it was written against) |
| **Conformance target** | WCAG 2.2 Level AA |
| **Methodology** | WCAG-EM 2.0 (scope & sample: `03-scope-and-sample.md`) |
| **Instruments & baselines** | (from `03` §1.3/§1.5 — AT + versions actually used) |

## Procurement decision

| | |
|---|---|
| **Decision** | Approved / Needs TAAP / Denied |
| **Decision date** | |
| **Decided by** | |
| **Rationale** | (1–2 sentences tying the decision to the results below) |

**Decision buckets** — driven by the task verdicts in `04-task-testing.md`;
apply the first bucket whose conditions all hold:

- **Approved** — the product may enter the campus ecosystem. No task verdict
  of **Fail**, no Blocker findings, and no "Does Not Support" outcome or
  Major finding that substantially burdens an essential task for any affected
  user group.
- **Needs TAAP** — the product may be procured only with a Technology
  Accessibility Accommodation Plan. Task failures or Major barriers exist,
  but every essential task remains achievable through accommodation, and the
  vendor commits to a remediation roadmap.
- **Denied** — the product may not enter the campus ecosystem. One or more
  essential tasks are blocked for an affected user group with no workable
  accommodation, or the vendor will not commit to remediation.

## At a glance

*The RFP-comparable summary — same boxes for every product reviewed.*

| | |
|---|---|
| **Headline** | (one sentence: can the people this product is bought for use it?) |
| **Essential tasks** | (e.g. "2 tested: 1 Pass with barriers, 1 Fail") |
| **Criteria verified** | (evaluated / 55, with Supports / Partially / Does-Not counts) |
| **Findings** | (n total: n Blocker, n Major, n Minor; n product-wide) |
| **Vendor ACR coverage** | (does it address the target standard? missing criteria?) |
| **Vendor ACR reliability** | (n criteria worse than claimed / n better / n agree) |
| **Remediation outlook** | (mostly additive & cheap / structural / unknown) |
| **Coverage of this review** | (views × modalities done; key caveats) |

## Executive summary

(2–4 sentences, plain language: what was reviewed, headline result, what
drives the decision.)

## Character of the barriers

(The analytic narrative: what *kind* of product is this and what kind of
barriers does it have — operability vs feedback, systemic patterns vs
isolated defects, what works well. This is where the reviewer's synthesis
lives; claims cite finding IDs.)

## Task outcomes

One row per task cluster from `04-task-testing.md` §A — what users need to
do, whether they can, and what stands in the way:

| Task | User story | Verdict | WCAG criteria failed | Findings |
|------|-----------|---------|----------------------|----------|
| T1 | | Not run / Pass / Pass with barriers / Fail | | |

## Key findings, by user impact

Ranked by impact on the affected user group, not by criterion number. Each
entry: who is affected and how, where, the **root cause** where identified,
and the evidence trail. Positives that materially shape the decision are
listed too.

### 1. (title) — (finding IDs)

- **Impact:**
- **Where:**
- **Root cause (if identified):**
- **Evidence:**

## Findings by sensory/functional modality (Section 508 FPC)

*The same findings sliced by the Section 508 Functional Performance
Criteria (302.1–302.9) — procurement's vocabulary. Derive from the
modality→WCAG map in `ontology/modality-checks.md` and the coverage matrix;
one row per modality, every modality present even when the row is
N/A or untested (an absent row reads as "fine", which is never what an
untested modality means).*

| Modality (508 FPC) | Coverage so far | Criteria failed | Findings | What it means for this user group |
|---|---|---|---|---|
| Without vision (302.1) | | | | |
| With limited vision (302.2) | | | | |
| Without color perception (302.3) | | | | |
| Without hearing / limited (302.4/.5) | | | | |
| Without speech (302.6) | | | | |
| Limited manipulation/reach/strength (302.7/.8) | | | | |
| Limited language/cognitive/learning (302.9) | | | | |

## Vendor ACR audit

*The section only an independent reviewer can write: is this vendor's
paperwork trustworthy?*

### Coverage

(Does the ACR address the conformance target at all? Standard/version it was
written against, criteria claimed vs in scope, obsolete claims, unclaimed
criteria — from `05` §Vendor evidence gap.)

### Reliability — claims vs verified

Every criterion where this review's outcome differs from the vendor's claim,
**in both directions** (from `05`, Outcome ≠ Vendor claim):

| Criterion | Vendor claim | Verified | Direction | Note |
|-----------|--------------|----------|-----------|------|
| | | | worse / better than claimed | |

### What this means for relying on this vendor's ACRs

(1–3 sentences for procurement: over-claims, under-claims, blanket ratings,
staleness — the pattern, not the instances.)

## Results summary

Rollup from `05-results.md` (the full per-criterion record):

| Outcome | Level A (of 31) | Level AA (of 24) | Total (of 55) |
|---------|-----------------|------------------|---------------|
| Supports | | | |
| Partially Supports | | | |
| Does Not Support | | | |
| Not Applicable | | | |
| Not Evaluated | | | |

## Concerns outside the conformance target

(Real product concerns WCAG does not cover — e.g. Section 508 §504
authoring-tool obligations for tools that produce content. Kept outside the
conformance statements; each needs a reviewer scope decision. Delete if
none.)

## Coverage & limitations of this review

(Honesty box, from `validate`/`matrix`: which views × modalities were
tested with which instruments; what remains untested; standing caveats such
as single-AT evidence or sample-document limits. An INTERIM report must
make incompleteness impossible to miss.)

## Remediation exhibit (for contract negotiation)

Specific, verifiable asks — attachable to a purchase agreement. One row per
fix; "Verify by" names the re-test that proves delivery.

| # | Defect (finding) | WCAG SC | Specific fix | Verify by |
|---|------------------|---------|--------------|-----------|
| 1 | | | | |

## TAAP — Technology Accessibility Accommodation Plan

(Required when the decision is **Needs TAAP**; delete otherwise. Campus
accessibility officers build their local accommodation from this.)

| Field | Value |
|-------|-------|
| Affected functionality | (which tasks/features have barriers, per key findings) |
| Affected user groups | |
| Accommodation provided | (the equally effective alternate access, concretely) |
| Responsible party | |
| How users request it | |
| TAAP review date | |

### Vendor remediation roadmap

| Criterion | Issue | Vendor commitment | Target date |
|-----------|-------|-------------------|-------------|
| | | | |

## Automated sweep record and triage disposition

One row per sweep (from the sweep runs' `run.md` triage — sweep output is
never findings; every violation is confirmed or dismissed in writing, every
`incomplete` routed to a manual check). Include dismissed false positives
explicitly — they are evidence of triage rigor, and a vendor re-running the
tool will hit them too. Note any structural blind spots of the instrument
on this product (canvas, shadow DOM, unresolvable backgrounds).

| View | Run | Violations | Incomplete | Passes | Disposition |
|---|---|---|---|---|---|
| | | | | | |

## Recommendation

*Drafted from the evidence for the reviewer to adopt, amend, or reject —
the Decision field remains the reviewer's alone. One paragraph: which
bucket the evidence points to and why (task completability, remediation
outlook, vendor reliability); what would move the recommendation; explicit
about what approval/denial would require that the evidence does or does not
show.*

## Appendices

- Task-based test record and findings: `04-task-testing.md`
- Full per-criterion results (ACR-shaped technical record): `05-results.md`
- Evidence files: `evidence/`
- Vendor ACR as received: `vendor-acr/`
