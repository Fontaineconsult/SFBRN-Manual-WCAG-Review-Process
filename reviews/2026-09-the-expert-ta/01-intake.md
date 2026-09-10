# Review Intake — The Expert TA

| | |
|---|---|
| **Review ID** | 2026-09-the-expert-ta |
| **Date opened** | 2026-09-08 |
| **Reviewer(s)** | Daniel Fontaine (SFBRN ATI Coordinator) — reviewer of record. Campus side: Zach Oshri (CSUEB ATI Coordinator, ICT questionnaire and VPAT review), Jonathan Hale (CSUEB IT Business Operations, procurement and TAAP) |
| **Status** | Intake → Testing → Decided |
| **Decision** | Pending (final: Approved / Needs TAAP / Denied — see `06-report.md`) |

## Procurement information

| Field | Value |
|-------|-------|
| Requisition / PO number | Not in thread — ATI review runs in P2P; offline ICT questionnaire submitted by Zach Oshri 2026-07-30 |
| Procurement type | New purchase — replaces MyOpenMath for intro physics (MyOpenMath stays active in Canvas 5 years for archived assignments) |
| Requesting department | Department of Physics, CSU East Bay |
| Requestor name | Jason Singley, Professor and Acting Chair (admin support: Natalie Granera) |
| Requestor email | jason.singley@csueastbay.edu |
| Anticipated users | Students (required for coursework) / Faculty (author and manage assignments). Not required for employee job duties. |
| Estimated user count | Not stated — all sections of PHYS 125, 126, 135, 136; request enrollment figures from the department |
| Criticality / impact | High — required, graded, student-facing coursework; students pay $35/semester; Canvas LTI enablement is blocked until this review clears |
| Contract timeline | Not stated; department is waiting and the vendor is pressing. Canvas admin team enables the LTI only after the review clears. |
| Notes | Source: email thread 2026-07-27 → 2026-09-01 saved at `evidence/email.txt`. Campus contacts: Manpreet (CSUEB Canvas admin, canvas@csueastbay.edu), Margaret Price (cc). Jonathan Hale began drafting a **Temporary Alternative Access Plan (TAAP)** on 2026-08-13 from the vendor's incomplete VPAT — signatures needed from Department Chair, Dean, and ADA Compliance Officer — with a faculty remediation list (avoid drag-and-drop labeling in required work; offer an equivalent accessible alternative at the same time; never require attempting the inaccessible format first; tell students how to report barriers). Vendor has offered a recorded Zoom walkthrough with JAWS/NVDA; campus accepted it as a supplement, not a substitute for the ACR. |

## Product information

| Field | Value |
|-------|-------|
| Product name | The Expert TA |
| Version reviewed | SaaS, continuously deployed (no public version number; record the build/date seen at first login) |
| Delivery model | Web application / SaaS (browser-only; no native mobile app found; Respondus LockDown Browser supported for secure exams) |
| Product URL | https://theexpertta.com/ (marketing) · https://login.theexpertta.com/Login.aspx (application login) |
| Test environment URL / access | **Obtained 2026-09-01** — vendor demo environment ("all features and controls available") via https://login.theexpertta.com/Login.aspx. Shared instructor account, username `csuit@csueastbay.com` (deliberately fake domain; several campus staff share it). Password is in `evidence/email.txt` only — do not copy it into review files. The account has instructor access to a course with a sample assignment; open the assignment name → "Take Assignment" to work it as a student. **Coverage limit:** this is direct login, not an LTI launch — the Canvas path (auto-provisioning, grade pass-back) cannot be tested until the campus enables the integration, which happens only after this review. Student self-registration with payment is also untested by this route. |
| Description | Textbook-independent online homework and assessment platform for introductory STEM and social-science courses (physics, astronomy, chemistry, biology, American government), sold by Expert TA, LLC (Tulsa, OK). Components: online homework with instructor-controlled hints, feedback and "true partial credit" grading of numeric and symbolic answers; question libraries (6,000+ physics problems, OpenStax-aligned collections); an eBook editor / eReader for customizable OpenStax-based texts; secure testing (exam authoring, Respondus LockDown Browser); self-publishing of lecture notes and lab manuals; problem-authoring tool; class-management and analytics for instructors. Question types listed by the vendor: true/false, multiple choice, multiple select, short answer, essay, drag-and-drop (ranking, sorting, labeling), numeric, symbolic math expression, click-on-image (hotspot), graded simulations, and a free-body-diagram drawing tool. LMS integration via LTI 1.1 and 1.3 (Canvas, Blackboard, Brightspace/D2L, Moodle) with grade pass-back. Pricing per student ($15–$20 with eBook); free for instructors. Web scout 2026-09-08 — all vendor-stated, nothing verified. |

## Intake checklist

- [x] Procurement information recorded — from the email thread; requisition number and enrollment count still outstanding
- [x] Vendor accessibility contact identified (see `02-vendor.md`) — generic address only, no named person
- [x] Vendor ACR/VPAT requested or received — VPAT dated 2026-05-05 received by campus (incomplete); completed ACR on VPAT 2.5Rev INT requested 2026-09-01; neither file is in `vendor-acr/` yet
- [x] Test account / environment access obtained — shared demo instructor account, 2026-09-01
- [ ] Review scope drafted (see `03-scope-and-sample.md`)
