# axe sweep — R004 (S5)

Rendered from the raw axe JSON by `scripts/axe_report.py`. Recon, not findings: a violation becomes a finding only when the page's walk confirms it, and a clean sweep is not a pass (testing-tools.md §axe-core). Cross-origin iframes and closed shadow roots are invisible to axe — anything inside them is untested here.

| | |
|---|---|
| URL scanned | https://learn.essentials-ai.com/certificates |
| Scanned at | 2026-09-30T20:32:57.389Z |
| Engine | axe-core 4.10.3 |
| Browser | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 |
| Viewport | 1259 × 1096 |
| Rules run | default ruleset (all tags) |

## Summary

| Bucket | Rules | Nodes | Meaning |
|---|---|---|---|
| Violations | 1 | 1 | axe is confident these fail — each needs a human yes/no (W1) |
| Incomplete | 0 | 0 | axe could not decide — route to the modality that can (W2) |
| Passes | 38 | 132 | rules that ran and found nothing wrong on the nodes they apply to |
| Inapplicable | 51 | — | rules with nothing on this page to test |

### Violations by impact

- **moderate** (a barrier with a plausible workaround): `heading-order` ×1

## Violations

### `heading-order` — Heading levels should only increase by one

- **Impact:** moderate (a barrier with a plausible workaround)
- **Criteria:** no WCAG criterion (axe best practice)
- **Nodes:** 1
- **Rule:** Ensure the order of headings is semantically correct ([axe docs](https://dequeuniversity.com/rules/axe/4.10/heading-order?application=axeAPI))
- **Status:** reported failure — confirm against this page's walk → finding, or dismiss with a written reason (W1)

1. **Element:** `<h3 class="text-base font-semibold text-ink">No certificates yet</h3>`
    - **Selector:** `h3`
    - (any of) Heading order invalid

## Incomplete (needs a human)

None reported.

## Passes

Rules that ran and found nothing wrong. A pass covers only what axe can see and only the nodes it matched — it is not a WCAG pass for the criterion.

| Rule | Criteria | Nodes checked |
|---|---|---|
| `aria-allowed-attr` — Elements must only use supported ARIA attributes | 4.1.2 | 5 |
| `aria-allowed-role` — ARIA role should be appropriate for the element | — | 1 |
| `aria-conditional-attr` — ARIA attributes must be used as specified for the element's role | 4.1.2 | 5 |
| `aria-deprecated-role` — Deprecated ARIA roles must not be used | 4.1.2 | 1 |
| `aria-hidden-body` — aria-hidden="true" must not be present on the document body | 1.3.1, 4.1.2 | 1 |
| `aria-hidden-focus` — ARIA hidden element must not be focusable or contain focusable elements | 4.1.2 | 7 |
| `aria-prohibited-attr` — Elements must only use permitted ARIA attributes | 4.1.2 | 5 |
| `aria-required-attr` — Required ARIA attributes must be provided | 4.1.2 | 1 |
| `aria-roles` — ARIA roles used must conform to valid values | 4.1.2 | 1 |
| `aria-valid-attr` — ARIA attributes must conform to valid names | 4.1.2 | 5 |
| `aria-valid-attr-value` — ARIA attributes must conform to valid values | 4.1.2 | 5 |
| `avoid-inline-spacing` — Inline text spacing must be adjustable with custom stylesheets | 1.4.12 | 2 |
| `button-name` — Buttons must have discernible text | 4.1.2 | 2 |
| `bypass` — Page must have means to bypass repeated blocks | 2.4.1 | 1 |
| `color-contrast` — Elements must meet minimum color contrast ratio thresholds | 1.4.3 | 11 |
| `document-title` — Documents must have <title> element to aid in navigation | 2.4.2 | 1 |
| `empty-heading` — Headings should not be empty | — | 2 |
| `heading-order` — Heading levels should only increase by one | — | 1 |
| `html-has-lang` — <html> element must have a lang attribute | 3.1.1 | 1 |
| `html-lang-valid` — <html> element must have a valid value for the lang attribute | 3.1.1 | 1 |
| `image-alt` — Images must have alternative text | 1.1.1 | 1 |
| `image-redundant-alt` — Alternative text of images should not be repeated as text | — | 1 |
| `landmark-banner-is-top-level` — Banner landmark should not be contained in another landmark | — | 1 |
| `landmark-complementary-is-top-level` — Aside should not be contained in another landmark | — | 1 |
| `landmark-main-is-top-level` — Main landmark should not be contained in another landmark | — | 1 |
| `landmark-no-duplicate-banner` — Document should not have more than one banner landmark | — | 1 |
| `landmark-no-duplicate-main` — Document should not have more than one main landmark | — | 1 |
| `landmark-one-main` — Document should have one main landmark | — | 1 |
| `landmark-unique` — Landmarks should have a unique role or role/label/title (i.e. accessible name) combination | — | 4 |
| `link-name` — Links must have discernible text | 2.4.4, 4.1.2 | 6 |
| `list` — <ul> and <ol> must only directly contain <li>, <script> or <template> elements | 1.3.1 | 1 |
| `listitem` — <li> elements must be contained in a <ul> or <ol> | 1.3.1 | 3 |
| `meta-viewport` — Zooming and scaling must not be disabled | 1.4.4 | 1 |
| `meta-viewport-large` — Users should be able to zoom and scale the text up to 500% | — | 1 |
| `nested-interactive` — Interactive controls must not be nested | 4.1.2 | 3 |
| `page-has-heading-one` — Page should contain a level-one heading | — | 1 |
| `region` — All page content should be contained by landmarks | — | 44 |
| `tabindex` — Elements should not have tabindex greater than zero | — | 1 |

## Inapplicable

Rules with nothing to test on this page (no matching element). Useful as a structural fact: e.g. no `video-caption` here means the page holds no `<video>`.

`accesskeys`, `area-alt`, `aria-braille-equivalent`, `aria-command-name`, `aria-dialog-name`, `aria-input-field-name`, `aria-meter-name`, `aria-progressbar-name`, `aria-required-children`, `aria-required-parent`, `aria-text`, `aria-toggle-field-name`, `aria-tooltip-name`, `aria-treeitem-name`, `autocomplete-valid`, `blink`, `definition-list`, `dlitem`, `duplicate-id-aria`, `empty-table-header`, `form-field-multiple-labels`, `frame-focusable-content`, `frame-tested`, `frame-title`, `frame-title-unique`, `html-xml-lang-mismatch`, `input-button-name`, `input-image-alt`, `label`, `label-title-only`, `landmark-contentinfo-is-top-level`, `landmark-no-duplicate-contentinfo`, `link-in-text-block`, `marquee`, `meta-refresh`, `no-autoplay-audio`, `object-alt`, `presentation-role-conflict`, `role-img-alt`, `scope-attr-valid`, `scrollable-region-focusable`, `select-name`, `server-side-image-map`, `skip-link`, `summary-name`, `svg-img-alt`, `table-duplicate-name`, `td-headers-attr`, `th-has-data-cells`, `valid-lang`, `video-caption`
