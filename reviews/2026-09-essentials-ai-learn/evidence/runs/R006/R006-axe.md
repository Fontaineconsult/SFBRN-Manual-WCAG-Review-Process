# axe sweep — R006 (S1)

Rendered from the raw axe JSON by `scripts/axe_report.py`. Recon, not findings: a violation becomes a finding only when the page's walk confirms it, and a clean sweep is not a pass (testing-tools.md §axe-core). Cross-origin iframes and closed shadow roots are invisible to axe — anything inside them is untested here.

| | |
|---|---|
| URL scanned | https://learn.essentials-ai.com/login |
| Scanned at | 2026-09-30T20:33:25.409Z |
| Engine | axe-core 4.10.3 |
| Browser | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36 |
| Viewport | 1137 × 1153 |
| Rules run | default ruleset (all tags) |

## Summary

| Bucket | Rules | Nodes | Meaning |
|---|---|---|---|
| Violations | 0 | 0 | axe is confident these fail — each needs a human yes/no (W1) |
| Incomplete | 1 | 1 | axe could not decide — route to the modality that can (W2) |
| Passes | 35 | 66 | rules that ran and found nothing wrong on the nodes they apply to |
| Inapplicable | 54 | — | rules with nothing on this page to test |

## Violations

None reported.

## Incomplete (needs a human)

### `form-field-multiple-labels` — Form field must not have multiple label elements

- **Impact:** moderate (a barrier with a plausible workaround)
- **Criteria:** WCAG 3.3.2
- **Nodes:** 1
- **Rule:** Ensure form field does not have multiple label elements ([axe docs](https://dequeuniversity.com/rules/axe/4.10/form-field-multiple-labels?application=axeAPI))
- **Status:** axe could not decide — a human must; route to the modality run that can settle it (W2)

1. **Element:** `<input class="h-3.5 w-3.5 cursor-pointer accent-brand" type="checkbox">`
    - **Selector:** `.h-3\.5`
    - (none of) Multiple label elements is not widely supported in assistive technologies. Ensure the first label contains all necessary information.
    - Related: `<label class="mt-2 flex w-fit cursor-pointer items-center gap-2 text-xs text-muted hover:text-body"…`; `<label class="block">`

## Passes

Rules that ran and found nothing wrong. A pass covers only what axe can see and only the nodes it matched — it is not a WCAG pass for the criterion.

| Rule | Criteria | Nodes checked |
|---|---|---|
| `aria-allowed-attr` — Elements must only use supported ARIA attributes | 4.1.2 | 1 |
| `aria-allowed-role` — ARIA role should be appropriate for the element | — | 1 |
| `aria-conditional-attr` — ARIA attributes must be used as specified for the element's role | 4.1.2 | 1 |
| `aria-deprecated-role` — Deprecated ARIA roles must not be used | 4.1.2 | 1 |
| `aria-hidden-body` — aria-hidden="true" must not be present on the document body | 1.3.1, 4.1.2 | 1 |
| `aria-prohibited-attr` — Elements must only use permitted ARIA attributes | 4.1.2 | 1 |
| `aria-required-attr` — Required ARIA attributes must be provided | 4.1.2 | 1 |
| `aria-roles` — ARIA roles used must conform to valid values | 4.1.2 | 1 |
| `aria-valid-attr` — ARIA attributes must conform to valid names | 4.1.2 | 1 |
| `aria-valid-attr-value` — ARIA attributes must conform to valid values | 4.1.2 | 1 |
| `autocomplete-valid` — autocomplete attribute must be used correctly | 1.3.5 | 2 |
| `avoid-inline-spacing` — Inline text spacing must be adjustable with custom stylesheets | 1.4.12 | 1 |
| `button-name` — Buttons must have discernible text | 4.1.2 | 1 |
| `bypass` — Page must have means to bypass repeated blocks | 2.4.1 | 1 |
| `color-contrast` — Elements must meet minimum color contrast ratio thresholds | 1.4.3 | 2 |
| `document-title` — Documents must have <title> element to aid in navigation | 2.4.2 | 1 |
| `empty-heading` — Headings should not be empty | — | 1 |
| `form-field-multiple-labels` — Form field must not have multiple label elements | 3.3.2 | 2 |
| `heading-order` — Heading levels should only increase by one | — | 1 |
| `html-has-lang` — <html> element must have a lang attribute | 3.1.1 | 1 |
| `html-lang-valid` — <html> element must have a valid value for the lang attribute | 3.1.1 | 1 |
| `image-alt` — Images must have alternative text | 1.1.1 | 1 |
| `image-redundant-alt` — Alternative text of images should not be repeated as text | — | 1 |
| `label` — Form elements must have labels | 4.1.2 | 3 |
| `label-title-only` — Form elements should have a visible label | — | 3 |
| `landmark-main-is-top-level` — Main landmark should not be contained in another landmark | — | 1 |
| `landmark-no-duplicate-main` — Document should not have more than one main landmark | — | 1 |
| `landmark-one-main` — Document should have one main landmark | — | 1 |
| `landmark-unique` — Landmarks should have a unique role or role/label/title (i.e. accessible name) combination | — | 1 |
| `link-name` — Links must have discernible text | 2.4.4, 4.1.2 | 1 |
| `meta-viewport` — Zooming and scaling must not be disabled | 1.4.4 | 1 |
| `meta-viewport-large` — Users should be able to zoom and scale the text up to 500% | — | 1 |
| `nested-interactive` — Interactive controls must not be nested | 4.1.2 | 3 |
| `page-has-heading-one` — Page should contain a level-one heading | — | 1 |
| `region` — All page content should be contained by landmarks | — | 23 |

## Inapplicable

Rules with nothing to test on this page (no matching element). Useful as a structural fact: e.g. no `video-caption` here means the page holds no `<video>`.

`accesskeys`, `area-alt`, `aria-braille-equivalent`, `aria-command-name`, `aria-dialog-name`, `aria-hidden-focus`, `aria-input-field-name`, `aria-meter-name`, `aria-progressbar-name`, `aria-required-children`, `aria-required-parent`, `aria-text`, `aria-toggle-field-name`, `aria-tooltip-name`, `aria-treeitem-name`, `blink`, `definition-list`, `dlitem`, `duplicate-id-aria`, `empty-table-header`, `frame-focusable-content`, `frame-tested`, `frame-title`, `frame-title-unique`, `html-xml-lang-mismatch`, `input-button-name`, `input-image-alt`, `landmark-banner-is-top-level`, `landmark-complementary-is-top-level`, `landmark-contentinfo-is-top-level`, `landmark-no-duplicate-banner`, `landmark-no-duplicate-contentinfo`, `link-in-text-block`, `list`, `listitem`, `marquee`, `meta-refresh`, `no-autoplay-audio`, `object-alt`, `presentation-role-conflict`, `role-img-alt`, `scope-attr-valid`, `scrollable-region-focusable`, `select-name`, `server-side-image-map`, `skip-link`, `summary-name`, `svg-img-alt`, `tabindex`, `table-duplicate-name`, `td-headers-attr`, `th-has-data-cells`, `valid-lang`, `video-caption`
