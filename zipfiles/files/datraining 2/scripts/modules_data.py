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
    dict(slug="hero", title="Hero", category="layout", status="verified", minutes=6,
         summary="Home Page countdown banner, or a plain product-page hero image/video.",
         source_doc="Hero Block guide (internal PDF)",
         what="This component can be used on the <strong>Home Page</strong>, where you could display a countdown, or on any <strong>product pages</strong> where a specific product image or video can be added.",
         how="",
         when="Home Page for a launch countdown, or any product page for a plain hero banner (image or video background).",
         fields=[
             ("Main content (required)", "Should be an image."),
             ("Headline", "Optional main heading text."),
             ("Subline", "Optional supporting text under the headline."),
             ("Button", 'Optional link to go to a page with more info, e.g. "Scopri :arrow-right:" \u2014 the :arrow-right: token renders an arrow icon.'),
             ("Time", "Only include this field if the Hero is a countdown timer \u2014 see the timestamp format below."),
         ],
         snippet="| Hero |  |\n|---|---|\n| <<add image here>> |  |\n| La Rivoluzione Continua \u2013 Manca poco alla presentazione bimota |  |\n| %TIME% |  |\n| Scopri :arrow-right: |  |\n| 2024-11-05T12:00:00Z |  |",
         custom_sections=[
             ("Countdown timer: date format",
              "<p>Mention the <strong>Time</strong> field only if this Hero is a countdown timer. The time must be in the format "
              "<code>YYYY-MM-DDTHH:mm:ss.sssZ</code>, where <code>Z</code> is the timezone offset \u2014 either the literal character "
              "<code>Z</code> (indicating UTC), or <code>+</code>/<code>-</code> followed by <code>HH:mm</code>, the offset in hours "
              "and minutes from UTC.</p>"
              "<ul><li><strong>Example \u2014 CET:</strong> to run a countdown till 09:00 AM CET on Nov 5, 2024, write "
              "<code>2024-11-05T09:00:00+01:00</code> (CET is UTC+1, so <code>+01:00</code> is added).</li>"
              "<li><strong>Example \u2014 AEDT:</strong> Australia's AEDT is UTC+11. For a countdown to 09:00 AM AEDT on Oct 25, 2025, "
              "write <code>2025-10-24T22:00:00Z</code> \u2014 because 09:00 AEDT on Oct 25 is 22:00 UTC on the <em>previous day</em>, Oct 24.</li></ul>"
              "<div class=\"module-callout\"><strong>Stage component with countdown only supports an image, not a video.</strong></div>"),
             ("Adding the block",
              "<p>Use the <strong>Library</strong> section from the da.live toolbar and choose <strong>Hero</strong> from the list of available blocks.</p>"),
             ("Non-countdown use: a plain hero banner on a product page",
              "<p>If you just want a hero banner on a PDP (product detail page) and <strong>not</strong> a countdown, choose and paste an image "
              "compatible for desktop, then paste another image below it for mobile. Copy the 'Hero' block from an already-existing page instead of "
              "starting from scratch \u2014 for example, <strong>all Product pages use a Hero block</strong>, so any of them is a good source to copy from.</p>"),
         ],
         images=[("hero/img-003.png", "The countdown Hero rendered on the live page, with the days/hours/minutes timer and 'Scopri' button."),
                 ("hero/img-005.png", "A plain (non-countdown) Hero banner on a product page, with separate desktop and mobile images.")]),
    dict(slug="title", title="Title", category="layout", status="draft", minutes=2,
         summary="Section heading, with an optional pretitle and animated-line variant.",
         what='A section heading, used to introduce the content that follows it (e.g. "Models", "Technical Data").',
         how='Type a heading and, optionally, a short "pretitle" line above it. There is also a "line" variant that draws an animated vertical line next to the heading as the visitor scrolls past it.',
         when="Use above any section that needs its own heading — most pages use several Title blocks to break up the page.",
         fields=[("Pretitle", 'Optional small label above the heading, e.g. "OUR HERITAGE".'),
                 ("Heading", "The section title.")],
         snippet="| Title |  |\n|---|---|\n| Our Heritage |  |\n| ## Built in Rimini |  |",
         images=[]),
    dict(slug="text", title="Text", category="layout", status="draft", minutes=2,
         summary="Plain rich-text section — paragraphs, links, buttons, no special layout.",
         what="Plain rich-text content — paragraphs, links, and buttons — with no special layout of its own.",
         how="Whatever you type renders close to how you typed it: headings become styled headings, a bold sentence on its own becomes a styled pull-quote, and any linked \"button\" text becomes a real button.",
         when="Use for straightforward copy that doesn't need an image alongside it (for that, use Text with Image).",
         fields=[("Body copy", "Any mix of headings, paragraphs, links.")],
         snippet='| Text |  |\n|---|---|\n| ## A note from our founders<br>**"Every Bimota is built to be ridden, not just admired."**<br>Read more about our story below. |  |',
         images=[]),
    dict(slug="text-with-image", title="Text with Image", category="layout", status="draft", minutes=3,
         summary="Two-column text + image pairing, with a subtle scroll-shift effect.",
         what="A two-column section pairing a block of text with one or two images, side by side.",
         how="Put your text in one cell and your image(s) in the other. On desktop the images gently shift position as the visitor scrolls, creating a subtle parallax effect; on mobile they simply stack.",
         when="Use for storytelling sections — brand history, craftsmanship, behind-the-scenes content.",
         fields=[("Text column", "Heading + paragraph(s), optionally a link/button."),
                 ("Image column", "One or two images.")],
         snippet="| Text with Image |  |\n|---|---|\n| ## Built in Rimini<br>Every Bimota is hand-assembled in our Rimini workshop, continuing 50 years of craftsmanship. | ![Workshop photo](/media/workshop.jpg) |",
         images=[]),
    dict(slug="columns", title="Columns", category="layout", status="draft", minutes=3,
         summary="Flexible 2–4 column layout, with grid/gallery/download variants and ratio control.",
         what="A flexible layout block that arranges content into 2, 3, or 4 side-by-side columns.",
         how='The number of columns is simply however many cells you put in the row. Optional variants change the look: "grid" and "gallery" change spacing, "download" adds a top border (for download-link lists), and a "ratio-X-Y" class controls relative column widths (e.g. a wide text column next to a narrower image column).',
         when="Use for comparisons, download lists, or any content that needs simple side-by-side columns without full card styling.",
         fields=[("Column 1..N", "Each cell in the row becomes one column. Can hold text, images, or both.")],
         snippet="| Columns |  |\n|---|---|\n| ### Spec sheet | ### Owner's manual | ### Warranty terms |",
         images=[]),
    dict(slug="cards", title="Cards", category="layout", status="draft", minutes=3,
         summary="Responsive image + heading + text card grid — model overviews, feature grids.",
         what="A responsive grid of image + heading + text cards — the classic \"feature grid\" or \"model overview\" layout.",
         how="Each row you add becomes one card. Whichever cell contains only an image becomes the card's image; the other cell becomes its body text. The block automatically arranges all cards into a responsive grid.",
         when="Use for model overviews, feature highlights, or any \"pick one of these\" grid of items.",
         fields=[("Card image", "One image per card."), ("Card body", "Heading + short text per card.")],
         snippet="| Cards |  |\n|---|---|\n| ![DB Model](/media/db-model.jpg) | ### DB Series<br>Classic Bimota lines, modern engineering. |\n| ![Tesi Model](/media/tesi-model.jpg) | ### Tesi Series<br>Hub-center steering, reimagined. |",
         images=[]),
    dict(slug="teaser", title="Teaser", category="layout", status="verified", minutes=6,
         summary="Card container with 2 background styles × 4 width ratios, unlimited cards.",
         source_doc="Teaser Block guide (internal PDF)",
         what="The teaser component is a container for cards. It has <strong>2 variations</strong> with respect to the background image (default, with-image) and <strong>4 variations</strong> for size ratios (default, one-two, two-one, one-one).",
         how="",
         when="Use for merchandising grids, related-content teasers, or any card set where you want control over the image/text balance. The teaser container can hold an <strong>unlimited number of cards</strong>.",
         fields=[
             ("Card image", "One image per card."),
             ("Card title", 'Bold heading, e.g. "Merchandising".'),
             ("Card description", "Supporting text under the title."),
             ("Price line (optional)", 'e.g. "59,99 Euro".'),
             ("Read More link", 'Rendered as a styled button with an arrow, e.g. "Read More :arrow-right:".'),
         ],
         snippet="| Teaser |  |\n|---|---|\n| ![Product](/media/product1.jpg) | **Merchandising**<br>Gear Up in Style \u2013 Explore Accessories and Merchandise<br>59,99 Euro<br>Read More :arrow-right: |\n| ![Product](/media/product2.jpg) | **Merchandising**<br>Gear Up in Style \u2013 Explore Accessories and Merchandise<br>Read More :arrow-right: |",
         custom_sections=[
             ("Adding the block",
              "<p>Two ways to add it: <strong>copy the component block</strong> from an existing page under your respective country folder, or use the <strong>Library</strong> section from the da.live tool and choose <strong>Teaser</strong> from the list available.</p>"),
             ("1. Teaser variant default",
              "<p>Block name: <code>Teaser</code>. Cards show the image above the text, on the default (light) background. Add as many image+text rows as you like \u2014 they arrange into a responsive row of cards.</p>"),
             ("2. Teaser variant image",
              "<p>Block name: <code>Teaser (image)</code>. Instead of the image sitting above the text, the card's <strong>image becomes the full background</strong> of the card, with the text content displayed <strong>on top of the image</strong>.</p>"),
             ("With-image ratio variants (3\u20135)",
              "<ul><li><strong>Teaser (image, one-two)</strong> \u2014 30%\u201360% width split</li>"
              "<li><strong>Teaser (image, two-one)</strong> \u2014 60%\u201330% width split</li>"
              "<li><strong>Teaser (image, one-one)</strong> \u2014 50%\u201350% width split</li></ul>"
              "<p>All three keep the image-as-background behavior from variant 2, just at different width proportions.</p>"),
             ("Default-background ratio variants (6)",
              "<p>The same width ratios are also available with the default (non-overlaid) background:</p>"
              "<ul><li><strong>Teaser (one-one)</strong> \u2014 50%\u201350%</li>"
              "<li><strong>Teaser (two-one)</strong> \u2014 60%\u201330%</li>"
              "<li><strong>Teaser (one-two)</strong> \u2014 30%\u201360%</li></ul>"),
         ],
         images=[("teaser/img-000.png", "Copying the Teaser block from an existing page in da.live."),
                 ("teaser/img-004.png", "Teaser variant default \u2014 image above text, light card background."),
                 ("teaser/img-007.png", "Teaser variant image \u2014 text overlaid on top of the card's background image."),
                 ("teaser/img-010.png", "A with-image ratio variant (30%\u201360% width split).")]),
    dict(slug="news-stories", title="News / Stories", category="layout", status="verified", minutes=6,
         summary="Card container for news/stories, in 4 layout variations (rows of three, rows of two, and two single-card splits).",
         source_doc="News and Stories Block guide (internal PDF)",
         what="The news and stories component is a container for cards. This can be used on the website news section or latest stories section. It contains images with description in <strong>4 different variations</strong>.",
         how="",
         when="Use on a News/Press page, or a \u201cLatest news\u201d / \u201cStories\u201d section \u2014 mix and match variations on the same page as needed.",
         fields=[
             ("Header row", "Sets the variant: News-stories (row-three), (row-two), (single, one-two), or (single, one-one)."),
             ("Image cell", "One image per card."),
             ("Pre title", 'Small label above the title, e.g. a date like "March 7th, 2024".'),
             ("Title", 'Bolded headline, e.g. "Behind the scenes".'),
             ("Description", "Supporting text, shown with an automatic \u201cRead More\u201d link/button."),
         ],
         snippet="| News-stories (row-three) |  |\n|---|---|\n| <<add image here>> | <<pre title>><br>**<<title>>**<br><<description>> |\n| <<add image here>> | <<pre title>><br>**<<title>>**<br><<description>> |\n| <<add image here>> | <<pre title>><br>**<<title>>**<br><<description>> |",
         custom_sections=[
             ("The 4 variations",
              "<ol><li><strong>News and stories - rows of three</strong></li>"
              "<li><strong>News and stories - rows of two</strong>, where the second card is bigger</li>"
              "<li><strong>News and stories - 1 card, 33% image + 66% text</strong></li>"
              "<li><strong>News and stories - 1 card, 50% text + 50% image</strong></li></ol>"),
             ("Adding the block",
              "<p>Use the <strong>Library</strong> section from the da.live tool and choose the relevant block from the list available. Or use the <strong>template folder</strong> in your specific country and navigate to the page inside which consolidates all available blocks \u2014 copy the News/Stories block from there and paste it into your desired document.</p>"),
             ("1. Rows of three",
              "<p>Block name: <code>News-stories (row-three)</code>. Add one image + pre title/title/description row per card; the block arranges every three cards into a row.</p>"),
             ("2. Rows of two (second card bigger)",
              "<p>Block name: <code>News-stories (row-two)</code>. Same row shape as above, but arranged two per row with the second card in each pair rendered larger.</p>"),
             ("3. Single card, image first (33% image + 66% text)",
              "<p>Block name: <code>News-stories (single, one-two)</code>. A single card where the image takes roughly a third of the width and the text two-thirds, image shown first.</p>"),
             ("4. Single card, text first (50% text + 50% image)",
              "<p>Block name: <code>News-stories (single, one-one)</code>. A single card split evenly between text and image, with the text column shown first (image on the right).</p>"),
             ("Mixing variations",
              "<p>You could also stack a mix &amp; match of different variations together on the same page to build a richer news/stories section.</p>"),
         ],
         images=[("news-stories/img-001.png", "Rows-of-three variant rendered live."),
                 ("news-stories/img-002.png", "Rows-of-two variant, with the second card rendered bigger."),
                 ("news-stories/img-003.png", "Single card, image-first (33% image + 66% text) variant."),
                 ("news-stories/img-004.png", "Single card, text-first (50% text + 50% image) variant.")]),
    dict(slug="feature", title="Feature", category="layout", status="verified", minutes=5,
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
    dict(slug="highlight", title="Highlight", category="layout", status="verified", minutes=4,
         summary="Scroll-animated image + headline + description callouts, with configurable animation timing.",
         source_doc="Highlights Block guide (internal PDF)",
         what="This component can be used on <strong>Product Pages</strong> or any content pages where you'd like to showcase highlights. It needs an image, a headline, and a description for each highlight, and holds a <strong>scroll-triggered animation</strong> behavior.",
         how="",
         when="Use on Product Pages or content pages to call out a handful of standout points (e.g. Efficiency, Exclusivity, High Quality) over a shared background image.",
         fields=[
             ("Block variant: Highlight (time-N)", "N sets the scroll animation duration in seconds \u2014 e.g. Highlight (time-2) or Highlight (time-7). The animation time is configurable this way."),
             ("Image row", "One shared image the highlights animate over."),
             ("Headline", "The title for each highlight point, e.g. \u201cEfficiency\u201d."),
             ("Description", "Supporting text under each headline."),
         ],
         snippet="| Highlight (time-2) |  |\n|---|---|\n| <<add image here>> |  |\n| <<Headline>> |  |\n| <<description>> |  |\n| <<Headline>> |  |\n| <<description>> |  |\n| <<Headline>> |  |\n| <<description>> |  |",
         custom_sections=[
             ("Adding the block to a page",
              "<p>Two ways to add it:</p>"
              "<ol><li><strong>Copy from an existing page</strong> \u2014 open an existing page under your respective country folder that already has a Highlight block and copy it.</li>"
              "<li><strong>Use the Library</strong> \u2014 in da.live, click <strong>Library</strong> in the block toolbar, then choose <strong>Highlight</strong> from the list of available blocks.</li></ol>"),
             ("Seeing it in action",
              "<p>The animation as the visitor scrolls can be seen in this reference video: <code>highlights-component.webm</code> (ask your development contact for a copy if you'd like to see it before publishing).</p>"),
         ],
         images=[("highlight/img-002.png", "The Highlight block rendered live \u2014 shared background image with an animated 'Efficiency' headline and description.")]),
    dict(slug="gallery", title="Gallery", category="layout", status="verified", minutes=4,
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
    dict(slug="carousel", title="Carousel", category="layout", status="draft", minutes=2,
         summary="Horizontally swipeable slide carousel.",
         what="A horizontally swipeable set of slides (touch/swipe on mobile, click-through on desktop).",
         how="Each row is one slide. The block handles swipe gestures and the sliding transition itself — you only provide the slide content.",
         when="Use where visitors should browse several items side-by-side, like a set of accessories or a photo set from an event.",
         fields=[("Slide content", "One row per slide — usually an image plus a short caption.")],
         snippet="| Carousel |  |\n|---|---|\n| ![Slide 1](/media/s1.jpg) | Caption for slide 1 |\n| ![Slide 2](/media/s2.jpg) | Caption for slide 2 |",
         images=[]),
    dict(slug="image", title="Image", category="layout", status="verified", minutes=5,
         summary="3 variants — single, two-image, and full-width sticky — each with a strict size/ratio checklist.",
         source_doc="Image Block guide (internal PDF)",
         what="The Image block can be used in sections of a webpage where you'd like to showcase pictures \u2014 on a homepage or any content page like a 'Heritage' page. It has <strong>3 variants</strong>.",
         how="",
         when="Use for a simple, deliberate photo moment \u2014 pick the variant based on whether you want one image, a paired comparison, or a full-width sticky background.",
         fields=[
             ("Image (single)", "One image. Ratio 16:9, minimum 1440 \u00d7 810px."),
             ("Image (two images)", "Two images side by side; the second is displayed smaller than the first. First image ratio 4:3, min 1440 \u00d7 1080px. Second image ratio 4:3, min 1440 \u00d7 1080px. They stack below each other only on viewport XS."),
             ("Image (sticky, full-width)", "One full-width image. Ratio 16:9, min 1440 \u00d7 810px. Stays sticky in the background while page content scrolls over it."),
             ("Section Metadata: Style = dark", "Optional companion block \u2014 add it after any block to switch that section's background to dark."),
         ],
         snippet="| Image |  |\n|---|---|\n| <<add image here>> |  |\n\n| Image |  |\n|---|---|\n| <<add image here>> | <<add image here>> |\n\n| Image (sticky) |  |\n|---|---|\n| <<add image here>> |  |\n\n| Section Metadata |  |\n|---|---|\n| Style | dark |",
         custom_sections=[
             ("The 3 variants",
              "<ul><li><strong>2 images</strong> \u2014 the second image is smaller than the first one</li>"
              "<li><strong>Single image</strong> \u2014 image ratio is 16:9</li>"
              "<li><strong>Full width image</strong> \u2014 stretches edge to edge</li></ul>"),
             ("1. Single image variant \u2014 UX checklist",
              "<p>Table: <code>Image</code> header row, then one row with <code>&lt;&lt;add image here&gt;&gt;</code>.</p>"
              "<p><strong>UX/UI checklist for this variant:</strong> Image ratio 16:9, 1440 \u00d7 810px (minimum).</p>"),
             ("2. Two images variant \u2014 UX checklist",
              "<p>Table: <code>Image</code> header row, then one row with two cells, each <code>&lt;&lt;add image here&gt;&gt;</code>.</p>"
              "<p><strong>UX/UI checklist:</strong> First image ratio 4:3, 1440 \u00d7 1080px (min). Second image ratio 4:3, 1440 \u00d7 1080px (min).</p>"
              "<p class=\"module-callout\">Images are displayed next to each other, <strong>except on Viewport XS</strong>, where they stack below each other.</p>"),
             ("3. Full-width sticky image variant \u2014 UX checklist",
              "<p>Table: <code>Image (sticky)</code> header row, then one row with <code>&lt;&lt;add image here&gt;&gt;</code>.</p>"
              "<p><strong>UX/UI checklist:</strong> Image ratio 16:9, 1440 \u00d7 810px (min).</p>"
              "<p class=\"module-callout\">The image <strong>stays sticky</strong> in the background while the rest of the page content scrolls over it.</p>"),
             ("Adding the block",
              "<p>Two ways to add it: <strong>copy the component block</strong> from an existing page under your respective country folder, or use the <strong>Library</strong> section from the da.live toolbar and choose the relevant variant from the list.</p>"),
             ("Bonus: a dark section background",
              "<p>Adding a <strong>Section Metadata</strong> block with <code>Style: dark</code> makes that section's background black. Add this at the end of a block (e.g. after an Image block) to make the background of that section dark.</p>"
              "<div class=\"code-wrap\"><pre class=\"code-block\">Section Metadata\nStyle | dark</pre></div>"),
         ],
         images=[("image/img-002.png", "Single image variant rendered on the page \u2014 16:9 ratio."),
                 ("image/img-004.png", "Two-image variant rendered side by side, the second smaller than the first.")]),

    # ---------------------------------------------------------------- 13-16: product & specs (draft)
    dict(slug="vehicle-selector", title="Vehicle Selector", category="product", status="draft", minutes=3,
         summary="Tabbed model picker: click a model name, see its image + description.",
         what="A tabbed model picker: a row of clickable model names, each showing its own image and description.",
         how="Each row becomes one tab. The heading in that row becomes the clickable tab label; the rest of the row (image, description) is what displays when that tab is active. The block builds the tab navigation and image/description panels itself.",
         when="Use on a \"Models\" overview page where visitors compare several motorcycles.",
         fields=[("Tab heading", "Becomes the clickable tab label (removed from the visible body text)."),
                 ("Tab image", "Shown when that tab is active."),
                 ("Tab description", "Shown alongside the image when that tab is active.")],
         snippet="| Vehicle Selector |  |\n|---|---|\n| ### Tesi H2<br>![Tesi H2](/media/tesih2.jpg)<br>Supercharged hub-center steering. |  |\n| ### KB4<br>![KB4](/media/kb4.jpg)<br>Naked, aggressive, road-focused. |  |",
         images=[]),
    dict(slug="specification", title="Specification", category="product", status="verified", minutes=6,
         summary="3 highlight specs + images + a button that opens the full Specification Table in a modal.",
         source_doc="Specification Block guide (internal PDF)",
         what="This component can be used on <strong>Product Pages</strong> where you could display a punchy summary of the vehicle specifications, with a button that opens the <strong>full</strong> specification table in a modal.",
         how="",
         when="Use once per product page, as the entry point into that model's full technical specifications.",
         fields=[
             ("Title (line): Section Headline (mandatory)", 'e.g. "Informazioni Tecniche" / "Technical Information".'),
             ("3 highlight specs", "Three short stat call-outs shown next to the images, e.g. Max Power, Max Torque, Weight."),
             ("3 images", "Three images of the model on a white background."),
             ("The button (mandatory)", 'e.g. "Show all specifications" / "Mostra tutto" \u2014 must link to the matching Specification Table\u2019s modal id.'),
             ("Linked Specification Table block", "A separate block elsewhere on the page whose header id matches the button\u2019s link, e.g. Specification Table (modal-specification-kb4)."),
         ],
         snippet="| Title (line) |  |\n|---|---|\n| <<specification section headline>> |  |\n\n| Specification |  |\n|---|---|\n| <<add a highlight spec>> | <<add image here>> |\n| <<add another highlight spec>> |  |\n| <<add another highlight spec>> |  |\n| <<add the button>> |  |\n\n| Specification Table (modal-specification-kb4) |  |\n|---|---|\n| <<enter vehicle model name>> |  |  |\n| Engine Specifications | <<enter the specification title>> | <<specification text>> |\n|  | <<enter the specification title>> | <<specification text>> |\n| <<enter the spec category>> | <<enter the specification title>> | <<specification text>> |",
         custom_sections=[
             ("Required sections",
              "<ul><li><strong>Section Headline</strong> (mandatory)</li>"
              "<li><strong>3 images</strong> of the model on a white background</li>"
              "<li><strong>3 highlight specifications</strong></li>"
              "<li>A <strong>table</strong> filled with specifications, plus a <strong>button</strong> that opens it</li></ul>"),
             ("Adding the block",
              "<p>Two ways to add it: <strong>copy the component block</strong> from an existing page under your respective country folder, or use the <strong>Library</strong> section from the da.live tool.</p>"),
             ("Linking the button to its Specification Table",
              "<p>For the button, link the page by adding the specification table's id at the end of the URL. For example: <code>/#modal-specification-kb4</code>. Select the button's text, click <strong>Edit link</strong>, and paste that fragment URL in. The linked <strong>Specification Table</strong> block elsewhere on the page must have a matching header, e.g. <code>Specification Table (modal-specification-kb4)</code> \u2014 the id after \u201cmodal-specification-\u201d must match exactly on both sides.</p>"),
             ("The Specification Table block",
              "<p>This is a separate block from Specification, authored as its own table:</p>"
              "<ul><li>First row: the block header with its modal id, e.g. <code>Specification Table (modal-specification-kb4)</code></li>"
              "<li>Next row: the vehicle model name, in bold</li>"
              "<li>Then category rows (e.g. \u201cEngine Specifications\u201d) that group the label/value spec rows beneath them, exactly like the <a href=\"specification-table.html\">Specification Table module</a></li></ul>"),
             ("Seeing it in action",
              "<p>A reference recording of the component's open/close behavior on the webpage: <code>screen-capture (32).webm</code> \u2014 ask your development contact for a copy if you'd like to see it before publishing.</p>"),
         ],
         images=[("specification/img-002.png", "The Specification block skeleton in da.live: highlight specs on the left, image on the right."),
                 ("specification/img-003.png", "Linking the button: editing its link to point at /#modal-specification-t\u2026"),
                 ("specification/img-004.png", "The rendered result \u2014 headline, three highlight stats, image, and a 'Mostra tutto' / Show all button.")]),
    dict(slug="specification-table", title="Specification Table", category="product", status="draft", minutes=3,
         summary="Categorized technical data table (engine, chassis, brakes...).",
         what='A categorized technical data table — the classic "full spec sheet" (engine, dimensions, brakes, etc.), grouped under category headings.',
         how="The first row is the table title. After that, whenever the first cell of a row has text, it starts a new category group; rows after it (with an empty first cell) are that category's label/value pairs.",
         when="Use on a model page's full technical-specifications section.",
         fields=[("Title row", "Heading for the whole table."),
                 ("Category cell", 'Starts a new group, e.g. "Engine".'),
                 ("Label / Value cells", 'One spec per row, e.g. "Power" / "197 hp".')],
         snippet="| Specification Table |  |\n|---|---|\n| ### Tesi H2 Specifications |  |\n| Engine |  |\n|  | Power | 197 hp |\n|  | Displacement | 998 cc |\n| Chassis |  |\n|  | Weight | 187 kg (dry) |",
         images=[]),
    dict(slug="table", title="Table", category="product", status="draft", minutes=1,
         summary="Plain HTML data table, no grouping or stat styling.",
         what="A plain, simple HTML data table — no categories, no special stat styling, just rows and columns.",
         how="Every row/cell you enter becomes a table row/cell, rendered as an ordinary table.",
         when="Use for simple tabular content that doesn't need Specification Table's grouping (e.g. a size/fit chart).",
         fields=[("Rows/cells", "Whatever you type, one table cell per authoring cell.")],
         snippet="| Table |  |\n|---|---|\n| Size | Height |\n| S | 165\u2013172 cm |\n| M | 172\u2013180 cm |",
         images=[]),

    # ---------------------------------------------------------------- 17-22: interactive & utility
    dict(slug="cta-buttons", title="CTA Buttons", category="interactive", status="verified", minutes=6,
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

    dict(slug="nba", title="NBA (Next Best Action)", category="interactive", status="verified", minutes=4,
         summary="Dark, full-width promo banner with 1–2 buttons — or a light variant.",
         source_doc="NBA Block guide (internal PDF)",
         what="This component can be used to showcase <strong>Next Best Actions</strong> in the webpage \u2014 a focused promo banner nudging the visitor toward one or two specific actions.",
         how="",
         when="Use anywhere you want a strong, focused call to action between content sections \u2014 e.g. \u201cUnlock Your Dream Ride\u201d prompting a test-ride booking or dealer search.",
         fields=[
             ("Block variant: NBA(dark, full-width)", "The default variant \u2014 forces a dark background, full width."),
             ("Block variant: nba (no modifier)", "The 'light' version \u2014 keeps the default light background instead of forcing dark."),
             ("Headline", 'e.g. "Unlock Your Dream Ride".'),
             ("Subtext", 'Supporting line, e.g. "Connect with a Dealer or Request Your Exclusive Offer".'),
             ("Button 1 (required)", "At least one button link is required."),
             ("Button 2 (optional)", "Up to one additional button \u2014 maximum of 2 buttons total."),
         ],
         snippet="| NBA(dark, full-width) |  |\n|---|---|\n| Unlock Your Dream Ride |  |\n| Connect with a Dealer or Request Your Exclusive Offer |  |\n| [Order your KB4 :arrow-right:](/it/it/kb4) [Find a dealer :arrow-right:](/it/it/dealers) |  |",
         custom_sections=[
             ("Features",
              "<ul><li>Will have a <strong>dark background</strong> (by default)</li>"
              "<li>Should have a <strong>minimum of 1 button and maximum of 2</strong></li></ul>"),
             ("Adding the block",
              "<p>Two ways to add it: <strong>copy the component block</strong> from an existing page under your respective country folder, or use the <strong>Library</strong> section from the da.live tool and choose <strong>NBA</strong> from the list of available blocks.</p>"),
             ("Two button-count variations",
              "<p><strong>1. With two buttons:</strong></p>"
              "<div class=\"code-wrap\"><pre class=\"code-block\">NBA(dark, full-width)\nUnlock Your Dream Ride\nConnect with a Dealer or Request Your Exclusive Offer\nOrder your KB4 :arrow-right:  Find a dealer :arrow-right:</pre></div>"
              "<p><strong>2. With one button:</strong></p>"
              "<div class=\"code-wrap\"><pre class=\"code-block\">NBA(dark, full-width)\nUnlock Your Dream Ride\nConnect with a Dealer or Request Your Exclusive Offer\nOrder your KB4 :arrow-right:</pre></div>"),
             ("Light version",
              "<p>You could also opt to keep the <strong>'light'</strong> version instead of the forced dark background \u2014 just use the plain block name <code>nba</code> (without the <code>(dark, full-width)</code> modifier) with the same headline/subtext/button rows.</p>"),
         ],
         images=[("nba/img-000.png", "Copying the NBA block from an existing page in da.live."),
                 ("nba/img-002.png", "The NBA block rendered live \u2014 dark full-width banner with two buttons."),
                 ("nba/img-004.png", "The light version of the NBA block, keeping the default light background.")]),

    dict(slug="country-selector", title="Country Selector", category="interactive", status="verified", minutes=5,
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

    dict(slug="dealer-locator", title="Dealer Locator", category="interactive", status="verified", minutes=5,
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

    dict(slug="woosmapdealers", title="Woosmap Dealers", category="interactive", status="verified", minutes=6,
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

    dict(slug="fragment", title="Fragment", category="interactive", status="draft", minutes=2,
         summary="Reuse another page's content by reference — one edit updates everywhere.",
         what="Pulls in another page's content and drops it into the current page — a way to reuse the same content in multiple places.",
         how="You give it the path to another page (e.g. a page you maintain just to hold a promo banner). At render time, that page's content is fetched and inserted here, fully rendered blocks and all.",
         when="Use for anything repeated across many pages: promo banners, legal notices, shared callouts. Edit the source page once; every page using the Fragment updates automatically.",
         fields=[("Path", "The path to the page whose content should be included here.")],
         snippet="| Fragment |  |\n|---|---|\n| /fragments/promo-banner |  |",
         images=[]),
    dict(slug="form", title="Form", category="interactive", status="draft", minutes=3,
         summary="Configurable contact/lead forms, built from a linked field-definition sheet.",
         what="A configurable form (e.g. contact or lead-generation forms), built from field definitions kept in a separate data sheet rather than typed directly into the page.",
         how="You link the block to a form-definition sheet; that sheet lists each field's type, label, and whether it's required, plus where submissions should be sent. The block builds the actual HTML form, labels, and validation/error messages from that sheet.",
         when="Use for contact forms, test-ride requests, newsletter sign-ups — anywhere you need visitor input.",
         fields=[("Form sheet link", "Path to the linked form-definition document.")],
         snippet="| Form |  |\n|---|---|\n| /forms/contact-us |  |",
         images=[]),

    # ---------------------------------------------------------------- 23-25: site-wide (draft)
    dict(slug="header", title="Header (Nav)", category="site", status="verified", minutes=6,
         summary="The site header — model names, images, and links — authored in a document named 'nav'.",
         source_doc="Nav or Header Block guide (internal PDF)",
         what="The site header lives in a document named <strong>'nav'</strong> in each locale folder, and contains the website's header elements: model names, images, and a few titles with links.",
         how="",
         when="Edit the shared 'nav' document for a locale to change what appears in that locale's header \u2014 not something you add to individual pages.",
         fields=[
             ("nav document", "One per locale folder (e.g. /jp/2_en/nav) \u2014 holds every header entry for that locale."),
             ("Model image", "Shown when that model/nav item is active or hovered. Click to copy or remove an image, then paste or drop a new one as preferred."),
             ("Model name / link text", "The visible label in the header, linked to its target page."),
             ("Hover effect", "Automatic on every model entry \u2014 nothing to configure."),
         ],
         snippet="<!-- Not authored per-page — edit the shared 'nav' document for the locale instead, e.g. /jp/2_en/nav -->",
         custom_sections=[
             ("Finding and opening the nav document",
              "<p>Navigate to the document named <strong>nav</strong> under the locale folder (e.g. <code>da.live/#/kawaind/bimota/jp/2_en</code>) and open it to view and modify it. Inside, you'll see various model names with images and a few titles with links \u2014 this becomes the header of the website. In a typical screenshot: the model's <strong>image</strong> is what's shown when that model is clicked, the model <strong>name</strong> is the linked label, and there's an automatic <strong>hover effect</strong> on each model entry.</p>"),
             ("Changing an existing model image",
              "<p>You can add or change existing images of the models directly in the nav document: click to copy or remove an image, then paste or drop a new image as preferred. A short reference video showing how this header looks live on the site: <code>header-nav.webm</code>.</p>"),
             ("Adding a brand-new nav option (e.g. \u201cRacing\u201d)",
              "<ol><li>Create a new page and name it (e.g. <code>racing-test</code>) in the same locale folder.</li>"
              "<li><strong>Preview</strong> the new page and copy its URL.</li>"
              "<li>Go back to the <strong>nav</strong> document, select the new option's text (e.g. \u201cRacing-test\u201d), click <strong>Edit link</strong>, and paste the page URL to link it.</li>"
              "<li>Click <strong>Preview</strong> again on the nav document.</li>"
              "<li>View the live page with the header to confirm the new nav item now appears and links correctly.</li></ol>"),
         ],
         images=[("header/img-004.png", "The nav document in da.live: model images, names, and links that make up the header."),
                 ("header/img-005.png", "The published site header showing a newly added 'Racing' / 'Racing-test' nav item.")]),
    dict(slug="footer", title="Footer", category="site", status="verified", minutes=6,
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
    dict(slug="error-page", title="Error Page", category="site", status="draft", minutes=1,
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
