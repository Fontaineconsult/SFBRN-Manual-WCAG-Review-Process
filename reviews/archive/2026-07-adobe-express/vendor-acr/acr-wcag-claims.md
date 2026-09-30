# Extracted WCAG claims — Adobe Express Accessibility Conformance Report

Source file: `adobe-express-webapp-2023-acr.html` (as received; see `02-vendor.md` for report metadata).
Extracted by `scripts/import_acr.py`. 50 criteria found.

## 1.1.1 Non-text Content (Level A)
**Claimed:** Web: Partially Supports

Web: The product provides sufficient text alternatives for most instances of active and informative images.
Exceptions include:
Functional image text alternative does not include essential text on image, present in ‘Layers’, ‘Search’ screens.
Functional image text alternative does not serve same purpose as image in ‘Generative AI - Text to Image’, 'Generative AI - Text Effects' screens.
The decorative image is not hidden from screen readers in ‘Comments’ screen.
Informative Images are missing alternate text in ‘Files - Grid View’, ‘Files - List View’, ‘Notifications / Share file Modal’, ‘Library Details’, ‘Add-ons’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Generate QR Code Dialog’, ‘Your Stuff - Files’, 'Brands' screens.
Informative Image text alternative does not present same info as image in ‘Create New File’, ‘Text/ Add Your Text’ screens.

## 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)
**Claimed:** Web: Partially Supports

Web: The product provides audio description or text transcripts for most of the video or audio only media. Exceptions include:
No text or audio description available for the video-only media in the ‘Discover Dialog’ screen.

## 1.2.2 Captions (Prerecorded) (Level A)
**Claimed:** Web: Supports

## 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)
**Claimed:** Web: Supports

## 1.2.4 Captions (Live) (Level AA)
**Claimed:** Web: Supports

## 1.2.5 Audio Description (Prerecorded) (Level AA)
**Claimed:** Web: Supports

## 1.3.1 Info and Relationships (Level A)
**Claimed:** Web: Partially Supports

Web: Most visual structure and relationship information is provided through element semantics or object information or are available in text. Exceptions include:
The content visually appears to be a data table but is not marked up as a table in ‘Schedule’ screen.
The group label is not associated with its checkboxes in ‘Report Abuse Modal’, ‘Resize’, ‘Video’ screens.
Group of form controls not associated with group label in ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Share to Social Media Modal’ screens.
The group label is not associated with its radio buttons in ‘Add-ons’, ‘Text - Animation’, ‘Video’ screens.
Heading levels are out of order in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Resize’, ‘Share to Social Media Modal’ screens.
Text inappropriately coded as a heading in ‘Home’ screen.
Visual heading text is not marked as heading in ‘Account Settings - All tabs (General / Account / About)’, ‘Brands & Libraries’, ‘Color Theme’, ‘Create New File’, ‘Files - List View’, ‘Left Navigation’, ‘Report Abuse Modal’, ‘Search’, ‘Text/ Add Your Text’, ‘You are Offline’ screens.
<ul> list does not directly contain <li> elements in ‘Home’ screen.
List or list item is not marked up properly in ‘Header’ screen.
Visual list is not marked up as list in ‘Generative AI - Text to Image’, ‘Report Abuse Modal’, ‘Resize’, ‘Share to Social Media Modal’, ‘Video’ screens.

## 1.3.2 Meaningful Sequence (Level A)
**Claimed:** Web: Partially Supports

Web: The product presents most content in a meaningful sequence.
Exceptions include:
Able to browse outside the modal content with screen reader in ‘Brands & Libraries’, ‘Files - List View’, ‘Quick Actions - Generate QR Code Dialog’, ‘Share to Social Media Modal’ screens.
aria-hidden="true" is used incorrectly in ‘Discover Dialog’, ‘Notifications / Share file Modal’ screens.
Correct reading order of dynamic content not determinable in ‘Comments’, ‘Create New File’, ‘Discover Dialog’, ‘Version History’ screens.
Hidden content is readable with a screen reader in ‘Ellipse’, ‘Home’, ‘Layers’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘View All Pages’ screens.
Informative (static) content is not readable by a screen reader in ‘Download’, ‘Header’ screens.
Informative content is not readable by a screen reader in ‘Create New File’ screen.
Reading order of static content changes meaning in ‘Add-ons’ screen.
Screen reader focus is lost or misplaced due to user interaction or content update in ‘Notifications / Share file Modal’ screen.

## 1.3.3 Sensory Characteristics (Level A)
**Claimed:** Web: Supports

Web: Instructions do not rely solely on sensory characteristics.

## 1.3.4 Orientation (Level AA)
**Claimed:** Web: Supports

Web: Content does not restrict its view and operation to a single display orientation.

## 1.3.5 Identify Input Purpose (Level AA)
**Claimed:** Web: Supports

## 1.4.1 Use of Color (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the functions of the product do not convey information through color alone.
Exceptions include:
Color alone is used to convey information in ‘Color Theme’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Quick Actions - Generate QR Code Dialog’, ‘Share to Social Media Modal’, ‘Text - Shadow’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Video - Effects’ screens.
Link contrast is not at least 3:1 with surrounding text in ‘Elements - Templates’, ‘Library Details’, ‘Media - Audio’, ‘Media - Photos/Videos’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Resize Image’, 'Brands' screens.

## 1.4.2 Audio Control (Level A)
**Claimed:** Web: Supports

Web: Audio content can be controlled by the user.

## 1.4.3 Contrast (Minimum) (Level AA)
**Claimed:** Web: Does Not Support

Web: Most of the text does not meet minimum contrast requirements. Examples include:
Text content lacks 4.5:1 contrast ratio in ‘Notifications / Share file Modal’, ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Comments’, ‘Generative AI - Text to Image’, ‘Header’, ‘Home’, ‘Library Details’, ‘Media - Audio’, ‘Media - Photos/Videos’, ‘Quick Actions - Animate From Audio’, ‘Quick Actions - Generate QR Code Dialog’, ‘Quick Actions - Resize Image’, ‘Resize’, ‘Schedule’, ‘Search’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’, ‘Video’, ‘Video - Adjustments’, ‘Your Stuff - Files’, 'Generative AI - Text Effects', 'Create New File' screens.
Link or button text lacks 4.5:1 contrast ratio on hover or focus in ‘Comments’, ‘Files - Grid View’, ‘Files - List View’, ‘Home’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’ screens.
Placeholder text lacks 4.5:1 contrast ratio in ‘Brands & Libraries’, ‘Comments’, ‘Library Details’, ‘Notifications / Share file Modal’, ‘Share to Social Media Modal’, 'Brands' screens.

## 1.4.4 Resize text (Level AA)
**Claimed:** Web: Partially Supports

Web: Most text can be resized using browser zoom, but content and functionality is lost in some product functions. Exceptions include:
Some part of the page content is lost when the page is zoomed to 200% in ‘Files - List View’ screen.
Functionality is lost at 200% zoom in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Comments’, ‘Create New File’, ‘Files - Grid View’, ‘Files - List View’, ‘Header’, ‘Home’, ‘Media - Audio’, ‘Quick Actions - Animate from Audio’, ‘Schedule’, ‘Search’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’, ‘Video’, ‘Media - Photos/Videos’ screens.

## 1.4.5 Images of Text (Level AA)
**Claimed:** Web: Supports

Web: The product uses text instead of images of text, except for branding elements that are considered essential.

## 1.4.10 Reflow (Level AA)
**Claimed:** Web: Partially Supports

Web: At the required width of 320 CSS pixels, most content is presented without loss of information or functionality, and without requiring scrolling in two dimensions. Exceptions include:
Functionality is lost at 320px width equivalent in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Comments’, ‘Create New File’, ‘Elements - Templates’, ‘Files - Grid View’, ‘Files - List View’, ‘Header’, ‘Home’, ‘Media - Audio’, ‘Media - Photos/Videos’, ‘Quick Actions - Animate from Audio’, ‘Schedule’, ‘Schedule Settings’, ‘Search’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’, ‘Video’ screens.

## 1.4.11 Non-text Contrast (Level AA)
**Claimed:** Web: Does Not Support

Web: Most of the meaningful non-text content does not meets sufficient color contrast requirements. Examples include:
Active user interface component lacks 3 to 1 contrast ratio in ‘Brands & Libraries’, ‘Comments’, ‘Ellipse’, ‘Files - Grid View’, ‘Files - List View’, ‘Image - Crop’, ‘Image - Erase’, ‘Notifications / Share file Modal’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Resize Image’, ‘Share to Social Media Modal’, ‘Text - Animation’, ‘Text - Shadow’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Video’, ‘Video - Adjustments’, ‘Video - Effects’ screens.
An icon lacks 3 to 1 contrast ratio in ‘Add-ons’, ‘Comments’, ‘Discover Dialog’, ‘Share to Social Media Modal’ screens.
Graphical object lacks 3 to 1 contrast ratio in ‘Text - Shapes’ screen.
State of active component lacks 3 to 1 contrast ratio in ‘Generative AI - Text to Image’, ‘Header’, ‘Home’, ‘Notifications / Share file Modal’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Schedule’, ‘Text - Shadow’, ‘Text - Shapes’, 'Generative AI - Text Effects' screens

## 1.4.12 Text Spacing (Level AA)
**Claimed:** Web: Supports

Web: The product supports the required text style properties without loss of content or functionality.

## 1.4.13 Content on Hover or Focus (Level AA)
**Claimed:** Web: Partially Supports

Web: In most of the product’s functionality, the additional content that is displayed on hover or focus is dismissible, hoverable or persistent. Exceptions include:
Hover content disappearing in ‘Brands & Libraries’, ‘Color Theme’, ‘Comments’, ‘Create New File’, ‘Ellipse’, ‘Files - Grid View’, ‘Files - List View’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Header’, ‘Image - Crop’, ‘Image - Erase’, ‘Left Navigation’, ‘Library Details’, ‘Media - Audio’, ‘Premium Content Badge’, ‘Quick Actions - Animate from Audio’, ‘Schedule’, ‘Schedule Settings’, ‘Share to Social Media Modal’, ‘Text - Fill Color’, ‘Text/ Add Your Text’, ‘Video’, ‘View All Pages’, ‘Your Stuff - Files’, 'Brands' screens.

## 2.1.1 Keyboard (Level A)
**Claimed:** Web: Does Not Support

Web: Most product functionality cannot be operated through a keyboard interface. Examples include:
Action cannot be performed with a screen reader turned on in ‘Add-ons’, ‘Ellipse’, ‘Explore Templates’, ‘Header’, ‘Left Navigation’ screens.
Device-dependent event handlers are used in ‘Add-ons’, ‘Brands & Libraries’, ‘Comments’, ‘Ellipse’, ‘Files - Grid View’, ‘Generative AI - Text to Image’, ‘Header’, ‘Left Navigation’, ‘Quick Actions - Resize Image’, ‘Schedule Settings’, ‘Share to Social Media Modal’, ‘Text - Animation’, ‘Text/ Add Your Text’, ‘Video’, ‘View All Pages’, 'Generative AI - Text Effects' screens.
Drag and drop feature is not keyboard accessible in ‘Layers’ screen.
Function cannot be performed by keyboard alone in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Discover Dialog’, ‘Elements - Templates’, ‘Explore Templates’, ‘Files - Grid View’, ‘Files - List View’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Home’, ‘Library Details’, ‘Media - Photos/Videos’, ‘Premium Content Badge’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Resize Image’, ‘Search’, ‘Share To Social Media Modal’, ‘Text - Shadow’, ‘Text/ Add Your Text’, ‘Video’, ‘View All Pages’, ‘Your Stuff - Files’, 'Brands' screens.
Link does not have an href value in ‘Library Details’, 'Brands' screens.

## 2.1.2 No Keyboard Trap (Level A)
**Claimed:** Web: Supports

Web: The product does not include keyboard traps.

## 2.1.4 Character Key Shortcuts (Level A)
**Claimed:** Web: Supports

Web: The product provides character key shortcuts and it activates only when the appropriate user interface component receives focus.

## 2.2.1 Timing Adjustable (Level A)
**Claimed:** Web: Partially Supports

Web: The product does not include functionality dependent on time limits. Exceptions include:
Content visually appears and disappears with no ability to adjust timing in ‘Comments’, ‘Quick Actions - Resize Image’ screens.

## 2.2.2 Pause, Stop, Hide (Level A)
**Claimed:** Web: Supports

## 2.3.1 Three Flashes or Below Threshold (Level A)
**Claimed:** Web: Supports

## 2.4.1 Bypass Blocks (Level A)
**Claimed:** Web: Supports

Web: The product provides a heading which allows users to bypass repeated blocks.

## 2.4.2 Page Titled (Level A)
**Claimed:** Web: Partially Supports

Web: The titles of most of the pages describe their purpose. Exceptions include:
Page <title> does not identify the purpose of the page in ‘Explore Templates’, ‘Files - Grid View’, ‘Files - List View’ ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Schedule’, ‘Schedule Settings’, 'Brands' screens.

## 2.4.3 Focus Order (Level A)
**Claimed:** Web: Does Not Support

Web: Most of the components does not receive the focus in a meaningful order. Examples include:
Hidden or empty element receives focus in ‘Add-ons’, ‘Elements - Templates’, ‘Ellipse’, ‘Explore Templates’, ‘Files - List View’, ‘Home’, ‘Layers’, ‘Media - Photos/Videos’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Search’, ‘Text/ Add Your Text’, ‘View All Pages’ screens.
Keyboard focus is lost or misplaced due to user interaction or content update in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Comments’, ‘Download’, ‘Text - Shadow’, ‘Text/ Add Your Text’ screens.
Keyboard focus is not maintained in modal in ‘Brands & Libraries’, ‘Files - List View’ screens.
Keyboard focus is not placed on opened modal in ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Resize Image’ screens.
Keyboard focus order is not logical in ‘Brands & Libraries’, ‘Comments’, ‘Create New File’, ‘Discover Dialog’, ‘Version History’ screens.
Modal is closed, focus is not returned to trigger in ‘Account Settings - All tabs (General / Account / About)’, ‘Brands & Libraries’, ‘Files - List View’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Generate QR Code Dialog’, ‘Quick Actions - Resize Image’, ‘Share to Social Media Modal’ screens.

## 2.4.4 Link Purpose (In Context) (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the links have a purpose that can be determined from the link text alone or from the programmatic context of the link. Exceptions include:
Purpose of link is not clear in context in ‘Home’ screen.

## 2.4.5 Multiple Ways (Level AA)
**Claimed:** Web: Supports

Web: Users can locate web pages in the product through the header and left navigation controls.

## 2.4.6 Headings and Labels (Level AA)
**Claimed:** Web: Does Not Support

Web: Most of the headings and labels are not descriptive. Examples include:
Buttons have same name but different actions in ‘Color Theme’, ‘Elements - Templates’, ‘Ellipse’, ‘Explore Templates’, ‘Files - List View’, ‘Home’, ‘Media - Audio’, ‘Media - Photos/Videos’, ‘Notifications / Share file Modal’, ‘Quick Actions - Animate from Audio’, ‘Schedule Settings’, ‘Search’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Version History’, ‘Your Stuff - Files’ screens.
Programmatic label does not convey purpose of control in ‘Account Settings - All tabs (General / Account / About)’, ‘Color Theme’, ‘Elements - Templates’, ‘Ellipse’, ‘Explore Templates’, ‘Files - Grid View’, ‘Files - List View’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Home’, ‘Image - Erase’, ‘Media - Photos/Videos’, ‘Quick Actions - Animate From Audio’, ‘Quick Actions - Generate QR Code Dialog’, ‘Quick Actions - Resize Image’, ‘Report Abuse Modal’, ‘Resize’, ‘Search’, ‘Share To Social Media Modal’, ‘Text - Animation’, ‘Text/ Add Your Text’, ‘Version History’, ‘Video’, ‘Your Stuff - Files’ screens.

## 2.4.7 Focus Visible (Level AA)
**Claimed:** Web: Partially Supports

Web: Most of the focusable elements have a visible keyboard focus indicator. Exceptions include:
Focus indicator is missing in ‘Brands & Libraries’, ‘Comments’, ‘Header’, ‘Image - Crop’, ‘Layers’, ‘Looping Animations’, ‘Notifications / Share file Modal’, ‘Quick Actions - Resize Image’, ‘Text - Animation’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Video - Effects’, ‘Your Stuff - Files’ screens.

## 2.5.1 Pointer Gestures (Level A)
**Claimed:** Web: Supports

## 2.5.2 Pointer Cancellation (Level A)
**Claimed:** Web: Supports

Web: Product functions that use a single pointer are completed when the user releases the pointer.

## 2.5.3 Label in Name (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the accessible names of the controls contain the text of their visible labels. Exceptions include:
Accessible name does not contain visible label in ‘Account Settings - All tabs (General / Account / About)’, ‘Ellipse’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Image - Erase’, ‘Notifications / Share file Modal’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Resize Image’, ‘Share to Social Media Modal’, ‘Text - Animation’, ‘Text - Shapes’, ‘Text/ Add Your Text’ screens.
Accessible name missing in ‘Files - Grid View’, ‘Files - List View’, ‘Quick Actions - Animate from Audio’, ‘Resize’, ‘Text - Fill Color’ screens.

## 2.5.4 Motion Actuation (Level A)
**Claimed:** Web: Supports

## 3.1.1 Language of Page (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the page’s language is programmatically determinable within the product. Exceptions include:
The <html> element does not have a lang attribute in ‘Library Details’ screen.

## 3.1.2 Language of Parts (Level AA)
**Claimed:** Web: Supports

## 3.2.1 On Focus (Level A)
**Claimed:** Web: Supports

Web: Components do not initiate a change of context when focused.

## 3.2.2 On Input (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the components change of context does not occur automatically on user input. Exceptions include:
Form field causes unexpected change in ‘View All Pages’ screen.

## 3.2.3 Consistent Navigation (Level AA)
**Claimed:** Web: Supports

Web: When navigational mechanisms are repeated in the product, such as the header navigation, they occur in a consistent relative order.

## 3.2.4 Consistent Identification (Level AA)
**Claimed:** Web: Supports

Web: Components with the same functionality are identified consistently.

## 3.3.1 Error Identification (Level A)
**Claimed:** Web: Partially Supports

Web: Most input errors are identified and described to the users in text. Exceptions include:
Form field with error not identified in ‘Account Settings - All tabs (General / Account / About)’, ‘Resize’ screens.
Input error is not described in text in ‘Text - Fill Color’ screen.

## 3.3.2 Labels or Instructions (Level A)
**Claimed:** Web: Partially Supports

Web: Labels are provided for most of the input fields.
Exceptions include:
Instructions missing for assistive technology users in ‘Image - Crop’ screen.
Navigation Instructions missing for the users in ‘Text/ Add Your Text’, 'Generative AI - Text to Image', 'Generative AI - Text Effects' screens.
Label is not persistent in ‘Brands & Libraries’, ‘Create New File’, ‘Header’, ‘Home’, ‘Notifications / Share file Modal’, ‘Share to Social Media Modal’, ‘Video’, ‘Text/ Add Your Text’, ‘Generative AI - Text to Image’, ‘Generative AI - Text Effects’ screens.
Visible label is missing in ‘Create New File’, ‘Files - Grid View’, ‘Files - List View’, ‘Resize’, ‘Share to Social Media Modal’, ‘Text - Fill Color’, ‘Text/ Add Your Text’, ‘Video’ screens.

## 3.3.3 Error Suggestion (Level AA)
**Claimed:** Web: Supports

Web: Where input errors are automatically detected, suggestions for correction are provided to the user.

## 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)
**Claimed:** Web: Supports

## 4.1.1 Parsing (Level A)
**Claimed:** Web: Partially Supports

Web: Most of the elements have proper start and end tags. Elements are nested according to their specifications. Elements do not contain duplicate attributes or duplicate IDs. Exceptions include:
Anchor or button nested inside other anchor or button in ‘Home’ screen.
ARIA role does not contain particular children in ‘Text - Fill Color’, ‘Library Details’, ‘Notifications / Share file Modal’, ‘Files - List View’, ‘Account Settings - All tabs (General / Account / About)’, 'Brands' screens.
Certain ARIA roles missing particular parents in ‘Brands & Libraries’, ‘Files - List View’ screens.
Interactive controls are nested in ‘Header’, ‘Create New File’, ‘Ellipse’ screens.
The page contains duplicate id attribute values in ‘Generative AI - Text to Image’, ‘Account Settings - All tabs (General / Account / About)’, ‘Library Details’, 'Generative AI - Text Effects', 'Brands' screens.

## 4.1.2 Name, Role, Value (Level A)
**Claimed:** Web: Does Not Support

Web: User interface components at most of the places do not provide programmatic name, role, state, or value information. Examples include:
Custom user interface component is not compatible with AT in ‘Image - Crop’ screen.
ARIA attributes are not allowed without role in ‘Share to Social Media Modal’ screen.
ARIA attributes need conform valid values in ‘Notifications / Share file Modal’ screen.
ARIA input fields need an accessible name in ‘Account Settings - All tabs (General / Account / About)’ screen.
Number of carousel slides is apparent visually but not programmatically in ‘Add-ons’ screen.
State of current carousel slide is not conveyed in ‘Add-ons’ screen.
Combo box is missing appropriate roles and/or attributes in ‘Account Settings - All tabs (General / Account / About)’, ‘Create New File’, ‘Header’, ‘Notifications / Share file Modal’, ‘Search’, ‘Text/ Add Your Text’ screens.
Dialog is missing appropriate role and/or attributes in ‘Brands & Libraries’, ‘Files - List View’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Generate QR Code Dialog’, ‘Quick Actions - Resize Image’, ‘Share to Social Media Modal’, 'Start from Your Content Modal’ screens.
Unallowed attributes are used in ‘Account Settings - All tabs (General / Account / About)’, ‘View All Pages’, ‘Notifications / Share file Modal’ screens.
Invalid ARIA attribute names are used in ‘Color Theme’ screen.
The element's role is incorrect in ‘Share to Social Media Modal’, ‘Media - Photos/Videos’ screens.
Slider is missing appropriate role and/or attributes in ‘Quick Actions - Animate from Audio’, ‘Video’ screens.
The element has missing or incorrect states or properties in ‘Create New File’, ‘Generative AI - Text Effects’, ‘Text - Shapes’, ‘View All Pages’ screens.
Tooltip content is not accessible to screen readers in ‘Brands & Libraries’, ‘Comments’, ‘Create New File’, ‘Ellipse’, ‘Generative AI - Text to Image’, ‘Header’, ‘Image - Erase’, ‘Left Navigation’, ‘Library Details’, ‘Premium Content Badge’, ‘Quick Actions - Animate from Audio’, ‘Schedule Settings’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’, ‘Video’, 'Generative AI - Text Effects', 'Brands' screens.
ARIA commands are missing an accessible name in ‘Brands & Libraries’, ‘Create New File’, ‘Text - Fill Color’, ‘Ellipse’, ‘Video - Effects’, ‘Library Details’, ‘Schedule’, ‘Files - Grid View’, ‘Files - List View’, ‘Header’, ‘Your Stuff - Files’, ‘Schedule Settings’, ‘Search’, ‘Elements - Templates’, ‘Account Settings - All tabs (General / Account / About)’, ‘Quick Actions - Resize Image’, ‘View All Pages’, ‘Brands’ screens.
Button disabled state is not conveyed in ‘Create New File’ screen.
Button does not have an accessible name in ‘Add-ons’, ‘Brands & Libraries’, ‘Color Theme’, ‘Comments’, ‘Elements - Templates’, ‘Generative AI - Text to Image’, ‘Layers’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Generate QR Code Dialog’, ‘Start from Your Content Modal’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Video’, ‘Text/ Add Your Text’, 'Generative AI - Text Effects' screens.
Button does not have a role in ‘Add-ons’, ‘Elements - Templates’, ‘Explore Templates’, ‘Files - Grid View’, ‘Files - List View’, ‘Home’, ‘Image - Crop’, ‘Layers’, ‘Library Details’, ‘Media - Photos/Videos’, ‘Premium Content Badge’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Resize Image’, ‘Search’, ‘Share to Social Media Modal’, ‘Text - Animation’, ‘Video’, ‘View All Pages’, ‘Your Stuff - Files’, 'Brands' screens.
Button is missing both a role and an accessible name in ‘Add-ons’, ‘Ellipse’, ‘Generative AI - Text to Image’, ‘Image - Crop’, ‘Library Details’, ‘Quick Actions - Animate from Audio’, ‘Schedule Settings’, ‘Share to Social Media Modal’, ‘Text/ Add Your Text’, ‘Version History’, ‘Video’, ‘Generative AI - Text Effects’, 'Brands' screens.
Button pressed state is not conveyed in ‘Comments’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Schedule’, ‘Text/ Add Your Text’ screens.
Button pressed state of the element is incorrect in ‘Text - Fill Color’ screen.
Form elements missing labels in ‘Files - List View’ screen.
Form field is not labeled in ‘Files - Grid View’, ‘Files - List View’, ‘Resize’, ‘Share to Social Media Modal’, ‘Text - Fill Color’, ‘View All Pages’ screens.
iframe does not have a title in ‘Add-ons’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’ screens.
Link does not have a role in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Header’, ‘Notifications / Share file Modal’, ‘Schedule Settings’ screens.
Expand/collapse state of the element is missing or incorrect in ‘Comments’, ‘Create New File’, ‘Elements - Templates’, ‘Files - Grid View’, ‘Files - List View’, ‘Generative AI - Text Effects’, ‘Header’, ‘Home’, ‘Library Details’, ‘Media - Photos/Videos’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Share to Social Media Modal’, ‘Start from Your Content Modal’, ‘Text - Fill Color’, ‘Text/ Add Your Text’, ‘Video’, ‘Video - Effects’, ‘Your Stuff - Files’, 'Brands' screens.
Selected state of the element is missing or incorrect in ‘Account Settings - All tabs (General / Account / About)’, ‘Brands & Libraries’, ‘Comments’, ‘Files - Grid View’, ‘Files - List View’, ‘Generative AI - Text Effects’, ‘Generative AI - Text to Image’, ‘Home’, ‘Layers’, ‘Media - Photos/Videos’, ‘Quick Actions - Animate From Audio’, ‘Quick Actions - Resize Image’, ‘Schedule’, ‘Share to Social Media Modal’, ‘Text - Animation’, ‘Text - Shadow’, ‘Text - Shapes’, ‘Text/ Add Your Text’, ‘Video - Effects’, ‘View All Pages’ screens.
The view options button value (33%) is not exposed to the screen reader users in ‘Create New File’ screen.

## 4.1.3 Status Messages (Level AA)
**Claimed:** Web: Partially Supports

Web: When status messages do not receive focus, the product does not provide the dynamic update to the assistive technology. Examples include:
Status message is not automatically announced in ‘Account Settings - All tabs (General / Account / About)’, ‘Add-ons’, ‘Color Theme’, ‘Comments’, ‘Download’, ‘Explore Templates’, ‘Files - List View’, ‘Quick Actions - Animate from Audio’, ‘Quick Actions - Convert To PDF/PNG/JPG Modals’, ‘Quick Actions - Generate QR Code Dialog’, ‘Resize’, ‘Search’, ‘Share to Social Media Modal’, ‘Text - Fill Color’, ‘Version History’ screens.
