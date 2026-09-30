# axe sweep

Rendered from the raw axe JSON by `scripts/axe_report.py`. Recon, not findings: a violation becomes a finding only when the page's walk confirms it, and a clean sweep is not a pass (testing-tools.md §axe-core). Cross-origin iframes and closed shadow roots are invisible to axe — anything inside them is untested here.

| | |
|---|---|
| URL scanned | https://mnowak-ai.github.io/ai-academics-articles/m1-article-05-opening-doors-to-your-future.html |
| Scanned at | 2026-09-30T20:37:00.450Z |
| Engine | axe-core 4.10.3 |
| Browser | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 |
| Viewport | 1137 × 1153 |
| Rules run | default ruleset (all tags) |

## Summary

| Bucket | Rules | Nodes | Meaning |
|---|---|---|---|
| Violations | 2 | 20 | axe is confident these fail — each needs a human yes/no (W1) |
| Incomplete | 0 | 0 | axe could not decide — route to the modality that can (W2) |
| Passes | 13 | 206 | rules that ran and found nothing wrong on the nodes they apply to |
| Inapplicable | 75 | — | rules with nothing on this page to test |

### Violations by impact

- **moderate** (a barrier with a plausible workaround): `landmark-one-main` ×1, `region` ×19

## Violations

### `landmark-one-main` — Document should have one main landmark

- **Impact:** moderate (a barrier with a plausible workaround)
- **Criteria:** no WCAG criterion (axe best practice)
- **Nodes:** 1
- **Rule:** Ensure the document has a main landmark ([axe docs](https://dequeuniversity.com/rules/axe/4.10/landmark-one-main?application=axeAPI))
- **Status:** reported failure — confirm against this page's walk → finding, or dismiss with a written reason (W1)

1. **Element:** `<html lang="en">`
    - **Selector:** `html`
    - (all of) Document does not have a main landmark

### `region` — All page content should be contained by landmarks

- **Impact:** moderate (a barrier with a plausible workaround)
- **Criteria:** no WCAG criterion (axe best practice)
- **Nodes:** 19
- **Rule:** Ensure all page content is contained by landmarks ([axe docs](https://dequeuniversity.com/rules/axe/4.10/region?application=axeAPI))
- **Status:** reported failure — confirm against this page's walk → finding, or dismiss with a written reason (W1)

1. **Element:** `<div class="hero">`
    - **Selector:** `.hero`
    - (any of) Some page content is not contained by landmarks
2. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(1)`
    - (any of) Some page content is not contained by landmarks
3. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(2)`
    - (any of) Some page content is not contained by landmarks
4. **Element:** `<div class="section fade-in"> <div class="pull-quote"><p>Instead of you searching for scholarships, AI can search for you — and it's a lot better at it than hours of scrolling will ever be.</p></div> </div>`
    - **Selector:** `.section.fade-in:nth-child(3)`
    - (any of) Some page content is not contained by landmarks
5. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(4)`
    - (any of) Some page content is not contained by landmarks
6. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(5)`
    - (any of) Some page content is not contained by landmarks
7. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(6)`
    - (any of) Some page content is not contained by landmarks
8. **Element:** `<div class="section fade-in"> <div class="pull-quote"><p>Scholarship money adds up. Even winning a few smaller awards can meaningfully reduce your need for student loans — and that impact follows you for years after gra…`
    - **Selector:** `.section.fade-in:nth-child(7)`
    - (any of) Some page content is not contained by landmarks
9. **Element:** `<div class="section fade-in">`
    - **Selector:** `.section.fade-in:nth-child(8)`
    - (any of) Some page content is not contained by landmarks
10. **Element:** `<div class="quiz-label">🎯 Knowledge Check</div>`
    - **Selector:** `.quiz-label`
    - (any of) Some page content is not contained by landmarks
11. **Element:** `<h2>Quick Question</h2>`
    - **Selector:** `.quiz > h2`
    - (any of) Some page content is not contained by landmarks
12. **Element:** `<p class="quiz-question">Why are smaller, niche scholarships often a better strategy than only applying to large, well-known national scholarships?</p>`
    - **Selector:** `.quiz-question`
    - (any of) Some page content is not contained by landmarks
13. … and 7 more node(s) — see the JSON

## Incomplete (needs a human)

None reported.

## Passes

Rules that ran and found nothing wrong. A pass covers only what axe can see and only the nodes it matched — it is not a WCAG pass for the criterion.

| Rule | Criteria | Nodes checked |
|---|---|---|
| `aria-hidden-body` — aria-hidden="true" must not be present on the document body | 1.3.1, 4.1.2 | 1 |
| `button-name` — Buttons must have discernible text | 4.1.2 | 4 |
| `color-contrast` — Elements must meet minimum color contrast ratio thresholds | 1.4.3 | 3 |
| `document-title` — Documents must have <title> element to aid in navigation | 2.4.2 | 1 |
| `empty-heading` — Headings should not be empty | — | 8 |
| `heading-order` — Heading levels should only increase by one | — | 8 |
| `html-has-lang` — <html> element must have a lang attribute | 3.1.1 | 1 |
| `html-lang-valid` — <html> element must have a valid value for the lang attribute | 3.1.1 | 1 |
| `meta-viewport` — Zooming and scaling must not be disabled | 1.4.4 | 1 |
| `meta-viewport-large` — Users should be able to zoom and scale the text up to 500% | — | 1 |
| `nested-interactive` — Interactive controls must not be nested | 4.1.2 | 4 |
| `page-has-heading-one` — Page should contain a level-one heading | — | 1 |
| `region` — All page content should be contained by landmarks | — | 172 |

## Inapplicable

Rules with nothing to test on this page (no matching element). Useful as a structural fact: e.g. no `video-caption` here means the page holds no `<video>`.

`accesskeys`, `area-alt`, `aria-allowed-attr`, `aria-allowed-role`, `aria-braille-equivalent`, `aria-command-name`, `aria-conditional-attr`, `aria-deprecated-role`, `aria-dialog-name`, `aria-hidden-focus`, `aria-input-field-name`, `aria-meter-name`, `aria-progressbar-name`, `aria-prohibited-attr`, `aria-required-attr`, `aria-required-children`, `aria-required-parent`, `aria-roles`, `aria-text`, `aria-toggle-field-name`, `aria-tooltip-name`, `aria-treeitem-name`, `aria-valid-attr`, `aria-valid-attr-value`, `autocomplete-valid`, `avoid-inline-spacing`, `blink`, `bypass`, `definition-list`, `dlitem`, `duplicate-id-aria`, `empty-table-header`, `form-field-multiple-labels`, `frame-focusable-content`, `frame-tested`, `frame-title`, `frame-title-unique`, `html-xml-lang-mismatch`, `image-alt`, `image-redundant-alt`, `input-button-name`, `input-image-alt`, `label`, `label-title-only`, `landmark-banner-is-top-level`, `landmark-complementary-is-top-level`, `landmark-contentinfo-is-top-level`, `landmark-main-is-top-level`, `landmark-no-duplicate-banner`, `landmark-no-duplicate-contentinfo`, `landmark-no-duplicate-main`, `landmark-unique`, `link-in-text-block`, `link-name`, `list`, `listitem`, `marquee`, `meta-refresh`, `no-autoplay-audio`, `object-alt`, `presentation-role-conflict`, `role-img-alt`, `scope-attr-valid`, `scrollable-region-focusable`, `select-name`, `server-side-image-map`, `skip-link`, `summary-name`, `svg-img-alt`, `tabindex`, `table-duplicate-name`, `td-headers-attr`, `th-has-data-cells`, `valid-lang`, `video-caption`
