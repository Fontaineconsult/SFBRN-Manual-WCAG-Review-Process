# Vendor & Product Contacts — The Expert TA

## Vendor

| Field | Value |
|-------|-------|
| Company name | Expert TA, LLC |
| Website | https://theexpertta.com/ |
| Address | 1516 S. Boston Avenue, Suite 215, Tulsa, Oklahoma 74119 |

## Contacts

| Role | Name | Email | Phone | Notes |
|------|------|-------|-------|-------|
| Sales / account contact | Jack Cameron | jack@theexpertta.com | 918-346-8382 | Primary thread contact; created the demo account. Generic: main@theexpertta.com, +1 918.949.4190, website live chat |
| Accessibility contact | Jeremy Morton | jeremy@theexpertta.com | | Led the accessibility development initiative; compiled the 2026-05-05 VPAT. Public statement routes VPAT requests to main@theexpertta.com |
| Technical support | (none named) | support@theexpertta.com | +1 877.572.0734 | |

## Vendor ACR / VPAT

| Field | Value |
|-------|-------|
| ACR received | Yes, incomplete — VPAT dated 2026-05-05 received by CSUEB (Zach Oshri). Campus rejected it 2026-08-14 and 2026-08-19; on 2026-09-01 Jack Cameron said the incomplete items "are now filled in" but no revised file has reached this review. Zach Oshri requested a complete ACR on VPAT 2.5Rev INT the same day. |
| VPAT edition | Non-standard — not on an ITI template edition; campus has requested VPAT 2.5Rev INT (WCAG 2.2 + Revised 508) |
| VPAT version | Not stated in the document (no "Based on VPAT® Version 2.5Rev" line) |
| WCAG version claimed | The 2026-05-05 document covers the 50 WCAG 2.1 A/AA criteria (41 answered, 9 blank). Public pages conflict: accessibility statement (2019-08-12) targets **WCAG 2.0 AA**; support accessibility page claims **WCAG 2.1 AA compliant as of December 2025**. Nothing mentions WCAG 2.2. |
| Report date | 2026-05-05 |
| Authored by | Vendor internal — Jeremy Morton (no accessibility contact email listed in the document) |
| File | Not yet in `vendor-acr/` — obtain the 2026-05-05 file from Zach Oshri or Jonathan Hale, and the revised file when it arrives; then run `scripts/import_acr.py` |

## Vendor accessibility posture

| Field | Value |
|-------|-------|
| Public accessibility statement URL | https://theexpertta.com/about/accessibility-statement/ (2019) · https://theexpertta.com/support/accessibility/ (feature and limitation list) |
| Accessibility roadmap provided | No — remediation timeline for drag-and-drop labeling, hotspot, and vector practice requested 2026-08-13 and again 2026-09-01; unanswered as of the thread's end |
| Known issues list provided | Yes, partial — Jack Cameron (2026-08-17, relaying Jeremy Morton): three question types are not compliant: **drag-and-drop labeling** (54 physics questions), **hotspot / click-on-image** (0 in physics), **vector practice** (17). 6,719 of 6,790 physics questions (~99%) are claimed compliant. Mitigation offered: an instructor checkbox that filters out non-WCAG-AA questions. Campus concern (Jonathan Hale, 2026-08-13): drag-and-drop labeling contains images of text that do not scale independently. The public support page also lists advanced essay questions with a drawing interface as unsupported. |
| Willing to sign accessibility contract language | Unknown |
| Notes | **Defects in the 2026-05-05 VPAT (per Zach Oshri's 2026-09-01 review):** nine A/AA criteria have no row — 1.2.3, 1.2.5, 1.3.4, 1.3.5, 1.4.10, 1.4.13, 2.5.1, 2.5.2, 2.5.4; Section 508 chapters 3, 5, and 6 absent (~49 criteria); most ITI header elements missing, including Evaluation Methods and a contact email; every answered criterion is "Supports" or "Not Applicable", with non-template terms ("Platform Supports", "Content Supports with rare exceptions", "Supported with Exceptions"); remarks under 1.4.3 and 1.4.5 describe known exceptions while the outcome says Supports. Expect these to become vendor-claim discrepancies in `05`.<br>**Vendor-stated methodology (email, 2026-08-17):** accessibility made top priority two years ago; seven developers and eight separate testers used JAWS, NVDA, and VoiceOver on Mac and PC in all major browsers; no automated or simulated reports; vendor offers to show the test data.<br>**Vendor "above baseline" claims to verify:** context-specific menus surfaced while tabbing (modelled on ada.gov) to shorten keyboard paths; human-friendly spoken math ("cosine of forty five point two") switchable against literal readout; free-body-diagram drawing question claimed accessible; drag-and-drop sorting and ranking claimed compliant.<br>**Public-page claims (web scout 2026-09-08):** keyboard-only navigation; screen-reader compatible; alt text for all images; captions, transcripts, audio descriptions; MathJax accessibility extension over MathML; roster-level extended time. SOC 2 claimed. Login requires JavaScript and cookies. All of the above are claims to test, not results. |
