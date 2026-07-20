#!/usr/bin/env python3
"""
Module content source of truth for the Bimota DA Training site.
Run `python3 scripts/build_modules.py` (from repo root) after editing this
file to regenerate modules/*.html and the index.html module grid.

status: "verified"  -> written from an authoritative internal guide (PDF)
        "draft"      -> written from the block's source code only, not yet
                         reviewed against an authoring guide. Safe/accurate,
                         but may be missing authoring nuances a real guide
                         would cover — upgrade these section by section.
"""

MODULES = [
    # ---------------------------------------------------------------- 00-12: layout & content (draft)
    dict(num="00", slug="hero", title="Hero", category="layout", status="draft", minutes=4,
         summary="Full-width banner: background image/video, heading, subheading, optional CTA.",
         what="A full-width banner, almost always the first thing on a page: a background image or video, a heading, optional subheading, and a call-to-action button.",
         how="You give it one image (or a video link) and some text. The block stretches the image to fill the width of the screen, overlays your heading/text on top, and adds a pause/play button automatically if you used a video instead of an image.",
         when="Use once, at the very top of a page — landing pages, model pages, campaign pages.",
         fields=[("Image or video", "Background media. A still image, or a link ending in .mp4 for a looping background video."),
                 ("Heading", "Main title, shown large."),
                 ("Subheading / body text", "Optional short supporting line."),
                 ("CTA link", 'Optional button, e.g. "Discover Tesi H2".')],
         snippet="| Hero |  |\n|---|---|\n| ![Tesi H2 hero image](/media/tesi-h2-hero.jpg) | # Tesi H2<br>The next chapter in hub-center steering.<br>[Discover Tesi H2](/it/it/tesi-h2) |",
         images=[]),
    dict(num="01", slug="title", title="Title", category="layout", status="draft", minutes=2,
         summary="Section heading, with an optional pretitle and animated-line variant.",
         what='A section heading, used to introduce the content that follows it (e.g. "Models", "Technical Data").',
         how='Type a heading and, optionally, a short "pretitle" line above it. There is also a "line" variant that draws an animated vertical line next to the heading as the visitor scrolls past it.',
         when="Use above any section that needs its own heading — most pages use several Title blocks to break up the page.",
         fields=[("Pretitle", 'Optional small label above the heading, e.g. "OUR HERITAGE".'),
                 ("Heading", "The section title.")],
         snippet="| Title |  |\n|---|---|\n| Our Heritage |  |\n| ## Built in Rimini |  |",
         images=[]),
    dict(num="02", slug="text", title="Text", category="layout", status="draft", minutes=2,
         summary="Plain rich-text section — paragraphs, links, buttons, no special layout.",
         what="Plain rich-text content — paragraphs, links, and buttons — with no special layout of its own.",
         how="Whatever you type renders close to how you typed it: headings become styled headings, a bold sentence on its own becomes a styled pull-quote, and any linked \"button\" text becomes a real button.",
         when="Use for straightforward copy that doesn't need an image alongside it (for that, use Text with Image).",
         fields=[("Body copy", "Any mix of headings, paragraphs, links.")],
         snippet='| Text |  |\n|---|---|\n| ## A note from our founders<br>**"Every Bimota is built to be ridden, not just admired."**<br>Read more about our story below. |  |',
         images=[]),
    dict(num="03", slug="text-with-image", title="Text with Image", category="layout", status="draft", minutes=3,
         summary="Two-column text + image pairing, with a subtle scroll-shift effect.",
         what="A two-column section pairing a block of text with one or two images, side by side.",
         how="Put your text in one cell and your image(s) in the other. On desktop the images gently shift position as the visitor scrolls, creating a subtle parallax effect; on mobile they simply stack.",
         when="Use for storytelling sections — brand history, craftsmanship, behind-the-scenes content.",
         fields=[("Text column", "Heading + paragraph(s), optionally a link/button."),
                 ("Image column", "One or two images.")],
         snippet="| Text with Image |  |\n|---|---|\n| ## Built in Rimini<br>Every Bimota is hand-assembled in our Rimini workshop, continuing 50 years of craftsmanship. | ![Workshop photo](/media/workshop.jpg) |",
         images=[]),
    dict(num="04", slug="columns", title="Columns", category="layout", status="draft", minutes=3,
         summary="Flexible 2–4 column layout, with grid/gallery/download variants and ratio control.",
         what="A flexible layout block that arranges content into 2, 3, or 4 side-by-side columns.",
         how='The number of columns is simply however many cells you put in the row. Optional variants change the look: "grid" and "gallery" change spacing, "download" adds a top border (for download-link lists), and a "ratio-X-Y" class controls relative column widths (e.g. a wide text column next to a narrower image column).',
         when="Use for comparisons, download lists, or any content that needs simple side-by-side columns without full card styling.",
         fields=[("Column 1..N", "Each cell in the row becomes one column. Can hold text, images, or both.")],
         snippet="| Columns |  |\n|---|---|\n| ### Spec sheet | ### Owner's manual | ### Warranty terms |",
         images=[]),
    dict(num="05", slug="cards", title="Cards", category="layout", status="draft", minutes=3,
         summary="Responsive image + heading + text card grid — model overviews, feature grids.",
         what="A responsive grid of image + heading + text cards — the classic \"feature grid\" or \"model overview\" layout.",
         how="Each row you add becomes one card. Whichever cell contains only an image becomes the card's image; the other cell becomes its body text. The block automatically arranges all cards into a responsive grid.",
         when="Use for model overviews, feature highlights, or any \"pick one of these\" grid of items.",
         fields=[("Card image", "One image per card."), ("Card body", "Heading + short text per card.")],
         snippet="| Cards |  |\n|---|---|\n| ![DB Model](/media/db-model.jpg) | ### DB Series<br>Classic Bimota lines, modern engineering. |\n| ![Tesi Model](/media/tesi-model.jpg) | ### Tesi Series<br>Hub-center steering, reimagined. |",
         images=[]),
    dict(num="06", slug="teaser", title="Teaser", category="layout", status="draft", minutes=2,
         summary="Compact image + heading + copy teaser, for secondary callouts.",
         what="Very similar to Cards — an image + heading + text item — but styled more compactly, with a smaller heading, for teaser-style callouts rather than a full feature grid.",
         how="Same authoring pattern as Cards: one image cell + one text cell per row. The block gives every heading a consistent, slightly smaller style than Cards uses.",
         when="Use for secondary callouts (e.g. \"related content\") where Cards would feel too heavy.",
         fields=[("Teaser image", "One image per item."), ("Teaser body", "Heading + short text per item.")],
         snippet="| Teaser |  |\n|---|---|\n| ![Owners club photo](/media/club.jpg) | #### Join the Owners Club<br>Exclusive events for Bimota owners. |",
         images=[]),
    dict(num="07", slug="news-stories", title="News / Stories", category="layout", status="draft", minutes=2,
         summary="Card-style news/story feed, purpose-built heading size for news items.",
         what="A card-style list of news items or stories, visually similar to Cards but with its own heading size, purpose-built for news feeds.",
         how="Same row-based authoring as Cards: an image cell plus a text cell per news item.",
         when="Use on a News/Press page, or a \"Latest news\" section on the homepage.",
         fields=[("Story image", "One image per story."), ("Story body", "Heading + short summary per story.")],
         snippet="| News / Stories |  |\n|---|---|\n| ![WorldSBK photo](/media/wsbk.jpg) | ##### Bimota returns to WorldSBK<br>A new chapter for the brand on track. |",
         images=[]),
    dict(num="08", slug="feature", title="Feature", category="layout", status="verified", minutes=5,
         summary="Vertical feature slider for Product Pages, with auto-highlighted active slide.",
         source_doc="Feature Block guide (internal PDF)",
         what="This block can be used on <strong>Product Pages</strong> where you want to highlight the special features of the product. It's a <strong>vertical slider block</strong>.",
         how="",
         when="Use on Product Pages to walk visitors through a product's standout features, one at a time, in a vertical slider.",
         fields=[
             ("Title (line) row", "The section heading, required, rendered with an animated vertical line beside it."),
             ("Feature image", "One image per feature row \u2014 required for each feature."),
             ("Feature headline", "The bolded title for that feature, required, rendered with H5 styling."),
             ("Feature description", "Supporting paragraph text under the headline."),
             ("Active slide indicator", "Automatically highlights which feature/slide is currently active \u2014 nothing to configure."),
         ],
         snippet="| Title (line) |  |\n|---|---|\n| <<Enter Title here>> |  |\n\n| Feature |  |\n|---|---|\n| <<add image here>> | <<title>><br><<description>> |\n| <<add image here>> | <<title>><br><<description>> |\n| <<add image here>> | <<title>><br><<description>> |\n| <<add image here>> | <<title>><br><<description>> |",
         custom_sections=[
             ("Required sections",
              "<p>The block has the following sections:</p>"
              "<ul><li><strong>Title Component</strong> (mandatory)</li>"
              "<li><strong>Images</strong> for each feature</li>"
              "<li><strong>Features Headline</strong> (mandatory) \u2014 rendered with H5 styling</li>"
              "<li><strong>Description</strong> of each feature</li>"
              "<li><strong>Active slide number</strong> \u2014 automatically highlighted as the visitor scrolls/clicks through</li></ul>"),
             ("Adding the block to a page",
              "<p>Two ways to add it:</p>"
              "<ol><li><strong>Copy from an existing page</strong> \u2014 open an existing page under your respective country folder that already has a Feature block (e.g. a model page), copy the block, and paste it into your document.</li>"
              "<li><strong>Use the Library</strong> \u2014 in da.live, click <strong>Library</strong> in the block toolbar, then choose <strong>Feature</strong> from the list of available blocks.</li></ol>"
              "<p class=\"module-callout\">Always use a <strong>'section break'</strong> after each block to separate it from the previous block.</p>"),
             ("The block skeleton",
              "<p>Below is the empty skeleton you fill in \u2014 a <strong>Title (line)</strong> table, followed by the <strong>Feature</strong> table with one row per feature (image cell + title/description cell):</p>"
              "<div class=\"code-wrap\"><pre class=\"code-block\">Title (line)\n<<Enter Title here>>\n\nFeature\n<<add image here>> | <<title>>\n                     <<description>>\n<<add image here>> | <<title>>\n                     <<description>>\n<<add image here>> | <<title>>\n                     <<description>>\n<<add image here>> | <<title>>\n                     <<description>></pre></div>"
              "<p>You're not limited to four rows \u2014 add as many feature rows as you need, following the same two-cell pattern.</p>"),
         ],
         images=[("feature/img-000.png", "Copying the Feature block from an existing page under a country folder in da.live."),
                 ("feature/img-002.png", "The Feature block rendered on the page \u2014 image on the left, headline + description on the right, with the active-slide indicator.")]),
    dict(num="09", slug="highlight", title="Highlight", category="layout", status="draft", minutes=2,
         summary="Full-width image slider with a scale/zoom reveal effect.",
         what="A full-width image slider where each image scales/zooms subtly as it comes into view.",
         how="Add one image per slide. As the visitor scrolls the block into view, each image animates in with a gentle scale effect; the aspect ratio adapts automatically between mobile and desktop.",
         when="Use for a striking, editorial-style image showcase (e.g. a photo essay of a motorcycle in detail).",
         fields=[("Slide image", "One large image per slide.")],
         snippet="| Highlight |  |\n|---|---|\n| ![Detail 1](/media/detail1.jpg) |  |\n| ![Detail 2](/media/detail2.jpg) |  |",
         images=[]),
    dict(num="10", slug="gallery", title="Gallery", category="layout", status="verified", minutes=4,
         summary="Image container that alternates 1-image and 2-image rows on larger screens; stacks on mobile.",
         source_doc="Gallery Block guide (internal PDF)",
         what="The gallery component is a container for images. The rows alternate by having <strong>1 image</strong> and <strong>2 images</strong> for larger screens (&gt;768px). Images stack below one another for mobile devices.",
         how="",
         when="Use for photo galleries — event coverage, workshop tours, model detail shots — anywhere you want a simple alternating image layout.",
         fields=[
             ("Gallery header row", 'Just the word "Gallery" in the first cell — marks the block.'),
             ("Single-image row", "One image — displays as a large single image on desktop."),
             ("Two-image row", "Two images placed side by side in the same row — displays as a 2-up pair on screens wider than 768px. On mobile, every image in the gallery stacks full-width, one per row, in order."),
         ],
         snippet="| Gallery |  |\n|---|---|\n| ![Photo 1](/media/g1.jpg) |  |\n| ![Photo 2](/media/g2.jpg) | ![Photo 3](/media/g3.jpg) |",
         custom_sections=[
             ("Adding the block to a page",
              "<p>Two ways to add it:</p>"
              "<ol><li><strong>Copy from an existing page</strong> \u2014 open an existing page under your respective country folder that already has a Gallery block, copy it, and paste it into the document where you'd like the gallery, then add your preferred images in the columns.</li>"
              "<li><strong>Use the Library</strong> \u2014 in da.live, click <strong>Library</strong> in the block toolbar, then choose <strong>Gallery</strong> from the list of available blocks, and go to the specific file to edit it.</li></ol>"
              "<p class=\"module-callout\">Always use a <strong>'section break'</strong> after each block to separate it from the previous block.</p>"),
             ("The block skeleton",
              "<p>The empty skeleton is simply a <strong>Gallery</strong> header cell followed by a series of empty rows \u2014 add one image to a row for a full-width single image, or two images in the same row for a side-by-side pair. Keep alternating single/double rows to get the alternating layout shown below.</p>"),
             ("Desktop vs. mobile result",
              "<p>On desktop (&gt;768px), a page with a Gallery block set up as one large image followed by two smaller side-by-side images renders exactly that way \u2014 one full-width image, then a row with two images sharing the width equally.</p>"
              "<p>On mobile, the same content simply stacks: every image renders full-width, one directly below another, in the same top-to-bottom order they were authored in.</p>"),
         ],
         images=[("gallery/img-000.png", "Copying the Gallery block from an existing page, or inserting it from the da.live Library panel."),
                 ("gallery/img-002.png", "Desktop view: one full-width image followed by a two-image row."),
                 ("gallery/img-003.png", "Mobile view: every image in the gallery stacks full-width, in order.")]),
    dict(num="11", slug="carousel", title="Carousel", category="layout", status="draft", minutes=2,
         summary="Horizontally swipeable slide carousel.",
         what="A horizontally swipeable set of slides (touch/swipe on mobile, click-through on desktop).",
         how="Each row is one slide. The block handles swipe gestures and the sliding transition itself — you only provide the slide content.",
         when="Use where visitors should browse several items side-by-side, like a set of accessories or a photo set from an event.",
         fields=[("Slide content", "One row per slide — usually an image plus a short caption.")],
         snippet="| Carousel |  |\n|---|---|\n| ![Slide 1](/media/s1.jpg) | Caption for slide 1 |\n| ![Slide 2](/media/s2.jpg) | Caption for slide 2 |",
         images=[]),
    dict(num="12", slug="image", title="Image", category="layout", status="draft", minutes=1,
         summary="Standalone responsive image, or two side by side.",
         what="A standalone responsive image (or two images side by side).",
         how='Drop in one image for a normal full-width image, or two side by side for an automatic "wide row" pairing. A "sticky" variant makes the image stick in place briefly while the visitor scrolls past it.',
         when="Use for a simple image with no text needed, where Hero or Text with Image would be overkill.",
         fields=[("Image", "One image, or two for the side-by-side variant.")],
         snippet="| Image |  |\n|---|---|\n| ![Workshop detail](/media/workshop-detail.jpg) |  |",
         images=[]),

    # ---------------------------------------------------------------- 13-16: product & specs (draft)
    dict(num="13", slug="vehicle-selector", title="Vehicle Selector", category="product", status="draft", minutes=3,
         summary="Tabbed model picker: click a model name, see its image + description.",
         what="A tabbed model picker: a row of clickable model names, each showing its own image and description.",
         how="Each row becomes one tab. The heading in that row becomes the clickable tab label; the rest of the row (image, description) is what displays when that tab is active. The block builds the tab navigation and image/description panels itself.",
         when="Use on a \"Models\" overview page where visitors compare several motorcycles.",
         fields=[("Tab heading", "Becomes the clickable tab label (removed from the visible body text)."),
                 ("Tab image", "Shown when that tab is active."),
                 ("Tab description", "Shown alongside the image when that tab is active.")],
         snippet="| Vehicle Selector |  |\n|---|---|\n| ### Tesi H2<br>![Tesi H2](/media/tesih2.jpg)<br>Supercharged hub-center steering. |  |\n| ### KB4<br>![KB4](/media/kb4.jpg)<br>Naked, aggressive, road-focused. |  |",
         images=[]),
    dict(num="14", slug="specification", title="Specification", category="product", status="draft", minutes=2,
         summary="Punchy stat + label callouts next to supporting images.",
         what='A stats-style spec section, pairing bold stat values (e.g. "197 hp") with their labels (e.g. "Power"), next to supporting images.',
         how="Write each stat as a short paragraph with the value in **bold** — the block detects bold text and styles it as the big stat number, with the rest of the paragraph becoming the label underneath.",
         when="Use for a punchy, visual specs section (as opposed to a plain data table — see Specification Table).",
         fields=[("Stat paragraphs", "One paragraph per stat, value in **bold**."),
                 ("Images", "Supporting images shown alongside the stats.")],
         snippet="| Specification |  |\n|---|---|\n| **197 hp**<br>Power<br>**187 kg**<br>Dry weight | ![Tesi H2](/media/tesih2-spec.jpg) |",
         images=[]),
    dict(num="15", slug="specification-table", title="Specification Table", category="product", status="draft", minutes=3,
         summary="Categorized technical data table (engine, chassis, brakes...).",
         what='A categorized technical data table — the classic "full spec sheet" (engine, dimensions, brakes, etc.), grouped under category headings.',
         how="The first row is the table title. After that, whenever the first cell of a row has text, it starts a new category group; rows after it (with an empty first cell) are that category's label/value pairs.",
         when="Use on a model page's full technical-specifications section.",
         fields=[("Title row", "Heading for the whole table."),
                 ("Category cell", 'Starts a new group, e.g. "Engine".'),
                 ("Label / Value cells", 'One spec per row, e.g. "Power" / "197 hp".')],
         snippet="| Specification Table |  |\n|---|---|\n| ### Tesi H2 Specifications |  |\n| Engine |  |\n|  | Power | 197 hp |\n|  | Displacement | 998 cc |\n| Chassis |  |\n|  | Weight | 187 kg (dry) |",
         images=[]),
    dict(num="16", slug="table", title="Table", category="product", status="draft", minutes=1,
         summary="Plain HTML data table, no grouping or stat styling.",
         what="A plain, simple HTML data table — no categories, no special stat styling, just rows and columns.",
         how="Every row/cell you enter becomes a table row/cell, rendered as an ordinary table.",
         when="Use for simple tabular content that doesn't need Specification Table's grouping (e.g. a size/fit chart).",
         fields=[("Rows/cells", "Whatever you type, one table cell per authoring cell.")],
         snippet="| Table |  |\n|---|---|\n| Size | Height |\n| S | 165\u2013172 cm |\n| M | 172\u2013180 cm |",
         images=[]),

    # ---------------------------------------------------------------- 17-22: interactive & utility
    dict(num="17", slug="cta-buttons", title="CTA Buttons", category="interactive", status="verified", minutes=6,
         summary="Up to four call-to-action buttons per row, with style, new-tab, and alignment control.",
         source_doc="CTA-buttons guide (internal PDF)",
         what='The <strong>CTA Buttons</strong> block lets authors place up to <strong>four buttons in a row</strong>, with flexible alignment and styling options — the standard way to add one or more prominent action buttons anywhere on a page.',
         how='',  # replaced by custom sections below
         when='Use wherever you need one or more prominent action buttons together — end of a section, end of a page, or standalone.',
         fields=[
             ("How many links in the row", "Determines the column variant: single (1, default center), two, three, or four (the maximum)."),
             ("Link text formatting", "Bold = Primary button (solid fill). Italic = Secondary button (outline). Plain text = Tertiary button (text link). Applied automatically from how the link text is formatted."),
             ("Trailing + or ++", "+ opens the link in a new tab with a screen-reader-only \u201copens in a new tab\u201d notice. ++ does the same but also shows that notice visibly to every visitor."),
             ("Alignment", "Left / Center (default) / Right. If you don't see an alignment control in your da.live toolbar for this block, duplicate an existing CTA Buttons block that already has the alignment you need, or ask a developer."),
         ],
         snippet="| CTA Buttons |  |\n|---|---|\n| [Book a test ride](/it/it/test-ride) [Find a dealer+](/it/it/dealers) |  |",
         custom_sections=[
             ("1. Button styles",
              "<p>Button appearance follows the standard authoring convention \u2014 it acts just like formatting a link in any word processor:</p>"
              "<ul><li><strong>Primary</strong> \u2013 <strong>bold</strong> link \u2192 solid filled button</li>"
              "<li><strong>Secondary</strong> \u2013 <em>italic</em> link \u2192 outlined button</li>"
              "<li><strong>Tertiary</strong> \u2013 plain text link \u2192 simple text link, no button shape</li></ul>"
              "<p>These styles are applied <strong>automatically</strong> based on how the link text is formatted in the da.live authoring interface \u2014 you don't pick a style from a dropdown.</p>"
              "<p>To set it up: click the text you want to make a CTA button, click <strong>\u201cEdit link\u201d</strong>, then choose <strong>bold</strong>, <em>italic</em>, or leave it plain, and paste in the destination URL. It works exactly like adding a link in a Word document.</p>"),
             ("2. New-tab markers (+  and  ++)",
              "<p>Control new-tab behavior by adding <code>+</code> markers at the end of the link's visible label text:</p>"
              "<p><strong>Single plus (<code>+</code>)</strong> \u2014 e.g. <code>Discover+</code></p>"
              "<ul><li>Opens the link in a <strong>new tab</strong></li>"
              "<li>Adds a <strong>screen-reader-only</strong> ARIA label (not visible to sighted users)</li></ul>"
              "<p><strong>Double plus (<code>++</code>)</strong> \u2014 e.g. <code>Discover++</code></p>"
              "<ul><li>Opens the link in a <strong>new tab</strong></li>"
              "<li>Displays a <strong>visible note</strong> after the button, e.g. \u201c(opens in a new tab)\u201d</li>"
              "<li>Also adds the ARIA label for screen readers</li></ul>"
              "<p>Use <code>++</code> only when you specifically want that new-tab note visible to every visitor, not just screen-reader users. If no <code>+</code> is present, the link opens in the same tab \u2014 the screen reader will still read the button normally.</p>"),
             ("3. Column variants (1\u20134 buttons)",
              "<p>The number of links you put in the row determines the variant:</p>"
              "<ul>"
              "<li><strong>Single column</strong> (default center-aligned) \u2014 use when you only need one CTA.</li>"
              "<li><strong>Two columns</strong> (default center-aligned) \u2014 two CTAs displayed side by side.</li>"
              "<li><strong>Three columns</strong> (default center-aligned) \u2014 three CTAs in a row.</li>"
              "<li><strong>Four columns</strong> (default center-aligned) \u2014 the maximum: four CTAs in a row.</li>"
              "</ul>"),
             ("4. Alignment options",
              "<p>All multi-column variants support alignment overrides:</p>"
              "<ul><li><strong>Left aligned</strong></li><li><strong>Center aligned</strong> (default)</li><li><strong>Right aligned</strong></li></ul>"
              "<p>These let you match the button row to the surrounding content's alignment.</p>"),
             ("5. Accessibility notes",
              "<ul><li><code>+</code> and <code>++</code> markers automatically generate ARIA labels for screen readers.</li>"
              "<li><code>++</code> also displays a visible note for all users.</li>"
              "<li>Keep button text concise and descriptive.</li>"
              "<li>Avoid stacking too many CTAs \u2014 use the four-column variant only when necessary.</li></ul>"
              "<p class=\"text-secondary small\">A video walkthrough of this block (<code>bimota-howToUse-cta-buttons-block.webm</code>) is referenced in the internal authoring guide \u2014 ask your development contact for a copy if you'd like to see it in action.</p>"),
         ],
         images=[("cta-buttons/img-000.png", "Primary, secondary, and tertiary button styles side by side."),
                 ("cta-buttons/img-001.png", "Setting up a CTA link in da.live: select the text, choose \u201cEdit link\u201d."),
                 ("cta-buttons/img-007.png", "A three-column CTA Buttons row, center aligned.")]),

    dict(num="18", slug="country-selector", title="Country Selector", category="interactive", status="verified", minutes=5,
         summary="The header locale picker: countries, flags, and links to each localized site.",
         source_doc="Country Selector Block guide (internal PDF)",
         what="The <strong>Country Selector</strong> block is a custom block designed to display the list of countries where the Bimota website is available. Each country is represented with its national flag and linked to the corresponding localized version of the site, with respective language options. It gives visitors a clear, intuitive way to navigate to their regional Bimota site.",
         how="",
         when="It is placed once, in the <strong>global header</strong> \u2014 it is not something you add to individual pages.",
         fields=[
             ("Header row", '"Choose your country" heading cell, paired with a representative image (e.g. a bike photo).'),
             ("Region row", 'A region label, e.g. "Europe", followed by a bulleted list of countries in that region.'),
             ("Country bullet", "Flag + country name as a link to that locale's homepage, e.g. Italia (it) / Italy (en)."),
             ("metadata block", "A second table at the bottom of the same document with theme = country-selector-page. Required for the block to render correctly \u2014 don't remove it."),
         ],
         snippet="| Country Selector | countries |\n|---|---|",
         custom_sections=[
             ("Where it lives, and who can edit it",
              "<p>This block is <strong>admin-only</strong>. If you are an admin or have the required access, navigate to "
              "<a href=\"https://da.live/#/kawaind/bimota\" target=\"_blank\" rel=\"noopener\">da.live/#/kawaind/bimota</a>, "
              "then open the <code>index</code> document at the root of the project. That single document holds the entire country list shown in every page's header.</p>"),
             ("Adding a new country",
              "<ol>"
              "<li>Open the <code>index</code> document in da.live edit mode. You'll see a table named <strong>country-selector</strong> with a \u201cChoose your country\u201d header row, then one row per region (e.g. Europe) listing countries with their flags.</li>"
              "<li>Click into the region's cell (or add a new region row below the same table if it's a brand-new region), then use <strong>\u201cEdit block\u201d \u2192 add column</strong> if you need a new row/column for the country group.</li>"
              "<li>Click the <strong>\u201cList\u201d</strong> (bullet list) icon to add a new bullet point, and type the country name \u2014 e.g. <code>Japan</code>.</li>"
              "<li>Select that text and click <strong>\u201cEdit link\u201d</strong>. Paste in the homepage URL for that locale, e.g. <code>/jp/2_en</code> for the English version of the Japan site. You can add both language versions as separate bullets under the same country (e.g. \u201cJapan (en)\u201d and \u201cJapan (jp)\u201d).</li>"
              "<li>For the flag icon itself, follow the same pattern as an existing row in the table \u2014 copying an existing country's row is the safest way to match the exact flag format already in use.</li>"
              "</ol>"),
             ("Preview and publish",
              "<p>After reviewing the content, click <strong>Preview</strong>. Then navigate to the preview URL for the new locale, e.g. "
              "<code>https://da.live/edit#/kawaind/bimota/jp/2_en/index</code>, and click Preview again to confirm the updated Country Selector renders correctly with the new entry before publishing.</p>"),
         ],
         images=[("country-selector/img-002.png", "The country-selector table in da.live: \u201cChoose your country\u201d header, regions, and flagged country links."),
                 ("country-selector/img-005.png", "Adding a new country: Edit block \u2192 add column, then List to add the bullet."),
                 ("country-selector/img-006.png", "The published result \u2014 a new \u201cJapan\u201d entry appears under Europe alongside Italy and the UK.")]),

    dict(num="19", slug="dealer-locator", title="Dealer Locator", category="interactive", status="verified", minutes=5,
         summary="The full-width Woosmap-powered dealer map used at the top of the Dealer Page template.",
         source_doc="Dealer page \u2013 Dynamic Template Update (Woosmap-driven) guide (internal PDF)",
         what="The <strong>Dealer Locator</strong> block is the full-width interactive map at the top of the <strong>Dealer Page \u2013 Tabs</strong> template \u2014 a fully dynamic, Woosmap API-driven way of rendering dealer information, replacing the old setup where authors had to manually update columns and shift cells every time a dealer was added.",
         how="",
         when="Used once per Dealer Page, as part of the standard <strong>Dealer Page \u2013 Tabs</strong> template \u2014 you generally start a new dealer page from that template rather than adding this block by hand.",
         fields=[
             ("Metadata: Title", "Page title shown to visitors. Default: \u201cDealers\u201d."),
             ("Metadata: wooskey", "The global Woosmap API key for this site \u2014 the same key used by both the Dealer Locator and the Woosmap Dealers blocks below it on the page."),
             ("Dealer Locator size", "Fullwidth, Height: large \u2014 the configuration used in the standard template."),
         ],
         snippet="| dealer-locator (full-width, height-big) |  |\n|---|---|",
         custom_sections=[
             ("Why this template replaced the old manual setup",
              "<p>With the new <strong>Dealer Page \u2013 Tabs</strong> template:</p>"
              "<ul><li>Dealer data is <strong>automatically populated from Woosmap APIs</strong></li>"
              "<li><strong>No manual column updates</strong> are required on the page when a dealer is added, removed, or changed</li>"
              "<li>Navigation is simplified with <strong>tabs and accordions</strong>, even across many countries and dealers</li>"
              "<li>The page layout <strong>adapts automatically</strong> as more markets are added</li></ul>"),
             ("How the template is put together",
              "<p>Starting a new dealer page from the <strong>Dealer Page \u2013 Tabs</strong> template (as opposed to the older plain <strong>Dealer Page</strong> template) gives you three blocks stacked on the page, in this order:</p>"
              "<ol>"
              "<li><strong>Metadata block</strong> \u2014 sets the page Title (default \u201cDealers\u201d) and the global <code>wooskey</code> (your site's Woosmap API key).</li>"
              "<li><strong>Dealer Locator block</strong> \u2014 the full-width, large-height interactive map, using that same global Woosmap key.</li>"
              "<li><strong>Woosmap Dealers block</strong> (twice \u2014 once as \u201clocal dealers\u201d, once as \u201cglobal dealers\u201d) \u2014 see the dedicated <a href=\"woosmapdealers.html\">Woosmap Dealers module</a> for how those two variants work.</li>"
              "</ol>"),
             ("What this means for you going forward",
              "<p>You no longer need to manually update dealer lists, shift table columns, or maintain \u201cother country\u201d sections by hand \u2014 all dealer information is now fully dynamic and sourced directly from Woosmap. In practice:</p>"
              "<ul><li>Any dealer update made in Woosmap automatically reflects on the site \u2014 there's nothing to republish on the page itself.</li>"
              "<li>The page always shows <strong>local dealers first</strong>, based on the country the site is running in.</li>"
              "<li>Navigation remains clean and scalable, no matter how many markets or dealers are added in the future.</li></ul>"),
         ],
         images=[("dealer-woosmap/img-001.png", "The Dealer Page \u2013 Tabs template in da.live: metadata, dealer-locator, and woosmapdealers blocks stacked on the page.")]),

    dict(num="20", slug="woosmapdealers", title="Woosmap Dealers", category="interactive", status="verified", minutes=6,
         summary="Local + global dealer listings, auto-grouped by country/region, sourced from Woosmap.",
         source_doc="Dealer page \u2013 Dynamic Template Update (Woosmap-driven) guide (internal PDF)",
         what="The <strong>Woosmap Dealers</strong> block renders dealer listings sourced live from Woosmap, in one of two variants: <strong>local dealers</strong> (this country only) or <strong>global dealers</strong> (every other country, grouped by region). Together with the Dealer Locator map, this is what powers the Dealer Page \u2013 Tabs template.",
         how="",
         when="Used twice on a standard Dealer Page \u2013 Tabs template: once configured as local dealers, once as global dealers. See the <a href=\"dealer-locator.html\">Dealer Locator module</a> for how it fits into the full template.",
         fields=[
             ("Variant: country-dealers (local)", "Shows dealers only from the current site's country."),
             ("Variant: global-dealers", "Shows dealers from all other countries."),
             ("exclude_countries (global-dealers only)", "Country codes to hide entirely from the global section. Default: jp, ph. Any country code can be added here to exclude it."),
             ("dealer_idstore (global-dealers only)", "Specific dealer IDs to force-include even if their country is in exclude_countries. Default example: 990033, 990030, 990031 (2 PH dealers + 1 JP dealer kept visible despite the default exclusion above)."),
         ],
         snippet="| woosmapdealers (country-dealers) |  |\n|---|---|\n\n| woosmapdealers (global-dealers) |  |\n|---|---|\n| exclude_countries | jp, ph |\n| dealer_idstore | 990033, 990030, 990031 |",
         custom_sections=[
             ("Local Dealers \u2014 country-dealers variant",
              "<ul><li>Shows dealers <strong>only from the current country</strong> (the country the site/locale is running in)</li>"
              "<li>Display: a country title heading, the dealer list laid out in a <strong>maximum of 3 columns</strong>, with vertical separators between columns</li></ul>"),
             ("Global Dealers \u2014 global-dealers variant",
              "<ul><li>Shows dealers from <strong>all other countries</strong> besides the current one</li>"
              "<li><strong>Excludes</strong> any countries listed in <code>exclude_countries</code> (default: <code>jp</code>, <code>ph</code>) \u2014 any country code can be added here to hide it from this section</li>"
              "<li><strong>Includes</strong> any dealer IDs listed in <code>dealer_idstore</code> even if their country would otherwise be excluded (default example keeps 2 PH dealers and 1 JP dealer visible)</li>"
              "<li>Display: <strong>tabs by region</strong> (Europe, Americas, Asia, Oceania), with the <strong>first tab always the region of the current country</strong>, an <strong>accordion per country</strong> inside each region tab, and dealers listed in <strong>3 columns, alphabetically sorted</strong></li></ul>"),
             ("Why this matters for you as an author",
              "<p>You don't maintain any of this by hand. Once the block is configured with the right <code>exclude_countries</code> / <code>dealer_idstore</code> values (usually set up once by a developer per site), the \u201cOther Dealers\u201d section reorganizes itself automatically \u2014 by region, with the visitor's own region shown first \u2014 as dealers are added or removed in Woosmap.</p>"),
         ],
         images=[("dealer-woosmap/img-001.png", "The two Woosmap Dealers instances (local + global) as authored inside the Dealer Page \u2013 Tabs template.")]),

    dict(num="21", slug="fragment", title="Fragment", category="interactive", status="draft", minutes=2,
         summary="Reuse another page's content by reference — one edit updates everywhere.",
         what="Pulls in another page's content and drops it into the current page — a way to reuse the same content in multiple places.",
         how="You give it the path to another page (e.g. a page you maintain just to hold a promo banner). At render time, that page's content is fetched and inserted here, fully rendered blocks and all.",
         when="Use for anything repeated across many pages: promo banners, legal notices, shared callouts. Edit the source page once; every page using the Fragment updates automatically.",
         fields=[("Path", "The path to the page whose content should be included here.")],
         snippet="| Fragment |  |\n|---|---|\n| /fragments/promo-banner |  |",
         images=[]),
    dict(num="22", slug="form", title="Form", category="interactive", status="draft", minutes=3,
         summary="Configurable contact/lead forms, built from a linked field-definition sheet.",
         what="A configurable form (e.g. contact or lead-generation forms), built from field definitions kept in a separate data sheet rather than typed directly into the page.",
         how="You link the block to a form-definition sheet; that sheet lists each field's type, label, and whether it's required, plus where submissions should be sent. The block builds the actual HTML form, labels, and validation/error messages from that sheet.",
         when="Use for contact forms, test-ride requests, newsletter sign-ups — anywhere you need visitor input.",
         fields=[("Form sheet link", "Path to the linked form-definition document.")],
         snippet="| Form |  |\n|---|---|\n| /forms/contact-us |  |",
         images=[]),

    # ---------------------------------------------------------------- 23-25: site-wide (draft)
    dict(num="23", slug="header", title="Header", category="site", status="draft", minutes=1,
         summary="The site-wide nav bar, sourced from a shared /nav fragment.",
         what="The site-wide navigation bar shown at the top of every page (logo, menu, country selector).",
         how="It isn't placed by hand on individual pages — it's sourced automatically from a shared \"/nav\" fragment maintained once for the whole site.",
         when="You generally won't add this yourself; edit the shared nav content instead, and every page updates.",
         fields=[("(shared content)", "Maintained in the site's shared /nav document, not per-page.")],
         snippet="<!-- Not authored per-page — edit the shared /nav document instead. -->",
         images=[]),
    dict(num="24", slug="footer", title="Footer", category="site", status="verified", minutes=6,
         summary="The global footer: language selector, four link columns, legal links, SEO metadata.",
         source_doc="Footer Block guide (internal PDF)",
         what="The Footer block is a <strong>globally consistent component</strong> placed at the bottom of all pages on the Bimota website. It provides users with quick access to key navigational and informational links, enhancing both usability and site structure.",
         how="",
         when="One footer document per locale folder \u2014 edit the shared footer document for that locale, not individual pages.",
         fields=[
             (":logo-flag row", "The country/region/language selector: a flag icon, the current locale (e.g. \u201cItaly (en)\u201d), and a \u201cChange\u201d link pointing to #modal-country-selector."),
             ("columns block", "One column per footer section (Models, About Bimota, Resources, Social by default \u2014 add more as needed)."),
             ("Column header", 'The section title cell at the top of each column, e.g. "Models".'),
             ("Column links", "A bullet list of links under each header."),
             ("Legal links", "Privacy Policy / Cookie Policy links, placed after the columns block."),
             ("metadata: Robots", "Set to noindex, nofollow so the standalone footer document itself isn't indexed by search engines (see below)."),
         ],
         snippet="| :logo-flag |  |\n|---|---|\n\n| columns |  |\n|---|---|\n| Models | About Bimota | Resources | Social |\n| [KB998 Rimini](/it/it/kb998) [Tesi H2](/it/it/tesi-h2) | [Heritage](/it/it/heritage) [Contact us](/it/it/contact-us) | [Dealer Locator](/it/it/dealer) [Press](/it/it/press) | [X](https://x.com/bimota) [Facebook](https://facebook.com/bimota) |\n\n[Privacy](/it/it/privacy) [Cookie](/it/it/cookie)\n\n| Metadata |  |\n|---|---|\n| Robots | noindex, nofollow |",
         custom_sections=[
             ("The four content sections",
              "<p>The footer is composed of a language selector plus four content sections, each with a defined title:</p>"
              "<ul><li><strong>Models</strong> \u2014 links to Bimota's current products lineup</li>"
              "<li><strong>About Bimota</strong> \u2014 information about the brand, heritage, and company background</li>"
              "<li><strong>Resources</strong> \u2014 useful links to resources like ISO and quality documents, and the dealer locator</li>"
              "<li><strong>Social</strong> \u2014 icons/links to Bimota's official social media channels</li></ul>"
              "<p>Plus <strong>Legal Links</strong>: Privacy Policy and Cookie Policy. These support compliance with data protection regulations such as GDPR and keep users informed about their data.</p>"),
             ("Editing the footer for a locale",
              "<p>Navigate to the respective country's path where the footer document is available (e.g. <code>da.live/#/kawaind/bimota/jp/2_en</code>) and open the <strong>footer</strong> document to edit it. Near the top you'll find the <code>:logo-flag</code> row \u2014 the Country / Region / Language selector, e.g. a flag icon next to \u201cItaly (en)\u201d with a \u201cChange\u201d link. Below it is the <strong>columns</strong> block holding the four sections described above.</p>"),
             ("Adding a new column",
              "<ol><li>Open the footer document and click <strong>Edit block</strong>, then click the \u201cadd column\u201d icon in the block toolbar.</li>"
              "<li>Type the new section's title in the header cell (e.g. \u201cTest\u201d), and add your links as a bullet list underneath it.</li>"
              "<li><strong>Link every link</strong> under the new section: select the text, click <strong>Edit link</strong>, and paste the destination path (e.g. <code>/it/en/dealer</code>).</li>"
              "<li>Click <strong>Preview</strong>, then navigate to the locale's <strong>index</strong> page and click Preview there too, to confirm the new column appears correctly across the site (the footer is shared, so checking from a real content page confirms it's wired up correctly).</li></ol>"),
             ("Metadata: keeping the footer document out of search results",
              "<p>The footer document itself carries a small <strong>Metadata</strong> table with <code>Robots: noindex, nofollow</code>. This tag prevents search engines from indexing or crawling the standalone footer block URL in da.live. It ensures only full content pages are indexed, maintaining SEO hygiene and avoiding duplicate or irrelevant entries in search results. Don't remove this row when editing the footer.</p>"),
         ],
         images=[("footer/img-002.png", "The footer document in da.live: the :logo-flag selector and the columns block (Models / About Bimota / Resources / Social)."),
                 ("footer/img-003.png", "The footer as rendered on the live site."),
                 ("footer/img-006.png", "Adding a new column: Edit block \u2192 add column, then linking each item in the new section."),
                 ("footer/img-007.png", "The rendered footer after publishing, showing the new column in place.")]),
    dict(num="25", slug="error-page", title="Error Page", category="site", status="draft", minutes=1,
         summary="The 404 / page-not-found content.",
         what="The content shown on a 404 / page-not-found state.",
         how="Mostly plain content, with one automatic behavior: any \"home\" link on the page is automatically pointed at the correct site root, so it still works correctly across every locale folder.",
         when="One per site (or per locale, if translated); not something you add to regular pages.",
         fields=[("Message + home link", "Whatever explanatory text you want, plus a link back home.")],
         snippet="| Text |  |\n|---|---|\n| ## Page not found<br>[Back to home](/) |  |",
         images=[]),
]

CATEGORY_LABEL = {
    "layout": "Layout & content",
    "product": "Product & specs",
    "interactive": "Interactive & utility",
    "site": "Site-wide (not authored per page)",
}
