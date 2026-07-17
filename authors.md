# Bimota Author Guide — Building Pages with da.live

This guide is for **content authors** — no coding experience needed. It explains what da.live is, how to find and use content blocks, how to build a page for a specific country/language, and how to preview and publish your work.

If you get stuck, skip to the [Troubleshooting & FAQ](#troubleshooting--faq) section near the end.

---

## Contents

1. [What is DA (da.live)?](#what-is-da)
2. [How pages are organized (country/language)](#how-pages-are-organized)
3. [Finding and using blocks](#finding-and-using-blocks)
4. [Step-by-step: building a page](#step-by-step-building-a-page)
5. [Common block recipes (copy/paste)](#common-block-recipes)
6. [Localization: text, images, links, fallback](#localization)
7. [Previewing and publishing](#previewing-and-publishing)
8. [Proposing changes to the blocks repo](#proposing-changes-to-the-blocks-repo)
9. [Troubleshooting & FAQ](#troubleshooting--faq)
10. [Best practices](#best-practices)

---

## What is DA (da.live)? {#what-is-da}

**da.live** is Adobe's document-based authoring tool for **Adobe Edge Delivery Services** (also called Edge Delivery, EDS, or "Franklin/Helix" internally). Instead of a complex CMS, you author content as simple documents — think Google Docs — using **tables** to mark where a "block" (a pre-built, styled component) should appear.

For the Bimota project, the pieces fit together like this:

| Layer | What it is | Who touches it |
|---|---|---|
| **da.live document** | The page you author (headings, text, images, and block tables) | You (content author) |
| **Preview environment** | `https://main--bimota--kawaind.aem.page` — a live draft of your page | You, for review |
| **Production ("live") environment** | `https://main--bimota--kawaind.aem.live` and ultimately **www.bimota.com** | Published content only |
| **Blocks repo (code)** | [github.com/kawaind/bimota/blocks](https://github.com/kawaind/bimota/tree/main/blocks) — the JS/CSS that turns your table into a styled component | Developers |

You never touch code. You author a document, and the block's existing code automatically styles whatever you put in the table.

---

## How pages are organized (country/language) {#how-pages-are-organized}

Bimota pages live under a **`/{country}/{lang}/`** URL prefix, for example:

- `/it/it/` — Italy, Italian
- `/us/en/` — United States, English
- `/de/de/` — Germany, German

The same page **slug** (the part after the country/language) should exist under every locale you support, e.g.:

```
/it/it/tesi-h2
/us/en/tesi-h2
/de/de/tesi-h2
```

This lets the **Country Selector** block and the **Dealer Locator** block automatically detect the visitor's country/language from the URL and offer the right localized experience (see [Localization](#localization) below).

> **Assumption to verify:** this guide assumes every localized folder mirrors the same page slugs. If your project instead uses a shared `/global/` folder with redirects, check with your project lead and adjust the examples accordingly — the block markup itself doesn't change.

---

## Finding and using blocks {#finding-and-using-blocks}

Open the **[Blocks Library](../pages/blocks.html)** page in this training site. It loads two files live from the project, so it always reflects what's actually available:

- **Blocks manifest:** `https://main--bimota--kawaind.aem.page/docs/library/blocks.json`
- **Templates manifest:** `https://main--bimota--kawaind.aem.page/docs/library/templates.json`

For each block you'll see its name, a short description, a preview image (when available), and a **copy/paste snippet** you can drop straight into your da.live document. Use the **"Try in page"** panel to fill in sample fields and see a rendered preview before you commit to it.

The blocks currently available in the Bimota project (from the [public blocks repo](https://github.com/kawaind/bimota/tree/main/blocks)) include:

| Block | Use it for |
|---|---|
| Hero | Full-width banner at the top of a page (image/video + heading + CTA) |
| Cards | Grid of image + text cards (model overviews, feature grids) |
| Teaser | Compact image + heading + copy teaser |
| Text with Image | Two-column text/image section |
| Columns | Flexible 2–4 column layout |
| Feature | Slide-based callout with navigation dots |
| Highlight | Full-width scaling image slider |
| Gallery | Scroll-animated image gallery |
| Carousel | Swipeable slide carousel |
| Vehicle Selector | Tabbed motorcycle model picker |
| Specification / Specification Table | Technical spec data |
| Table | Plain data table |
| CTA Buttons | One or more call-to-action buttons |
| Country Selector | Locale picker (reads `/countries.json`) |
| Dealer Locator / Woosmap Dealers | Dealer/store finder maps |
| News / Stories | News/story card list |
| Title | Section heading |
| Fragment | Reusable content included by path (e.g. shared promo banners) |
| Form | Lead/contact forms |

Header and Footer are shared across the whole site (sourced from `/nav` and `/footer`) — you won't add these manually on a page.

---

## Step-by-step: building a page {#step-by-step-building-a-page}

1. **Open da.live** and navigate to the folder for your locale, e.g. `/it/it/`.
2. **Duplicate the closest existing page** to your new one where possible — it's faster than starting from a blank document and keeps formatting consistent.
3. **Add a Hero block** at the top: insert a table, type `Hero` in the first cell, then fill the row(s) below with your image and heading text (see recipe below).
4. **Add body blocks** (Cards, Text with Image, Specification, etc.) in the order you want them to appear on the page.
5. **Add localized links and images.** Always use assets and links that are correct for *this* locale — don't copy a link from the `/us/en/` version into `/it/it/` without checking it.
6. **Preview your page** at `https://main--bimota--kawaind.aem.page/it/it/your-page` (see [Previewing and publishing](#previewing-and-publishing)).
7. **Check it on mobile and desktop widths**, and check any images have meaningful alt text.
8. **Publish** once it looks right.

---

## Common block recipes (copy/paste) {#common-block-recipes}

These show the **table shape** you type directly into your da.live document. The left column of the first row is always the block's name. Everything below it is the block's content, one row per repeatable item (e.g. one row per card).

### Hero

| Hero | |
|---|---|
| ![Tesi H2 hero image](https://main--bimota--kawaind.aem.page/media/tesi-h2-hero.jpg) | # Tesi H2<br>The next chapter in hub-center steering.<br>[Discover Tesi H2](/it/it/tesi-h2) |

### Cards (one row per card)

| Cards | |
|---|---|
| ![DB Model](https://main--bimota--kawaind.aem.page/media/db-model.jpg) | ### DB Series<br>Classic Bimota lines, modern engineering. |
| ![Tesi Model](https://main--bimota--kawaind.aem.page/media/tesi-model.jpg) | ### Tesi Series<br>Hub-center steering, reimagined. |

### Text with Image

| Text with Image | |
|---|---|
| ## Built in Rimini<br>Every Bimota is hand-assembled in our Rimini workshop, continuing 50 years of craftsmanship. | ![Workshop photo](https://main--bimota--kawaind.aem.page/media/workshop.jpg) |

### CTA Buttons (append `+` to open a link in a new tab)

| CTA Buttons | |
|---|---|
| [Book a test ride](/it/it/test-ride) [Find a dealer+](/it/it/dealers) | |

> The trailing `+` on "Find a dealer+" makes that link open in a new tab and automatically adds an accessible "opens in a new tab" notice for screen-reader users. Use `++` if you also want that notice visible on screen.

### Specification Table

| Specification Table | |
|---|---|
| ### Tesi H2 Specifications | |
| Engine | Supercharged inline-4 |
| Power | 197 hp |
| Weight | 187 kg (dry) |

### Country Selector

| Country Selector | countries |
|---|---|

This variant reads its list of countries/regions automatically from `/countries.json` — you don't need to list them manually. Ask a developer to add a country there if a new market is missing.

### Fragment (reuse shared content)

| Fragment | |
|---|---|
| /fragments/promo-banner | |

Use this to pull in a shared block of content (like a seasonal promo banner) that's maintained once and reused across many pages, in any locale.

---

## Localization {#localization}

**Text.** Every locale gets its own fully translated copy — never machine-translate directly in the table without review. Keep headings short; some blocks (e.g. Teaser, News/Stories) apply fixed heading sizes so very long localized titles can wrap awkwardly.

**Images.** Swap hero/gallery images per locale where cultural relevance matters (e.g. a dealership photo, a local event). Where the same image is used everywhere, it's fine to reuse the same asset path across locales.

**Links.** Always point links to the equivalent page **within the same locale prefix**. For example, on `/de/de/tesi-h2`, a "Find a dealer" link should point to `/de/de/dealers`, not `/it/it/dealers` or `/us/en/dealers`.

**Country Selector fallback behavior.** When a visitor switches country/language, the Country Selector tries to send them to the *same page slug* under the new locale. If that page doesn't exist yet in the target locale, it falls back to that locale's homepage rather than a broken link. This means:

- If you haven't translated a page into a given locale yet, that's fine — visitors switching into that locale will land on the homepage instead of a 404.
- Once you do publish the translated page, the Country Selector will pick it up automatically (there's nothing extra to configure).

**Dealer Locator / Woosmap Dealers language.** These blocks infer their working language from the URL's locale segment (e.g. `/it/it/…` → Italian, `/us/en/…` → English). If you ever place one of these blocks on a page outside the normal `/{country}/{lang}/` pattern, confirm with a developer which language it will default to.

---

## Previewing and publishing {#previewing-and-publishing}

1. Save your changes in da.live.
2. Open the **preview URL** for your page: `https://main--bimota--kawaind.aem.page/{country}/{lang}/{page-slug}` — e.g. `https://main--bimota--kawaind.aem.page/it/it/tesi-h2`.
3. Review the page. Preview reflects your latest saved draft, not yet the live site.
4. When it looks right, use da.live's **Publish** action for the page.
5. Confirm the change on the **live** environment: `https://main--bimota--kawaind.aem.live/{country}/{lang}/{page-slug}`, and eventually on **www.bimota.com**.

**Cache note:** preview updates almost immediately after saving. The live/production environment and bimota.com may take a short time to reflect a publish while the edge cache refreshes — if you don't see your change instantly on the live domain, wait a minute and do a hard refresh before assuming something's wrong.

---

## Proposing changes to the blocks repo {#proposing-changes-to-the-blocks-repo}

Blocks themselves (their code, styling, and behavior) live in [github.com/kawaind/bimota/blocks](https://github.com/kawaind/bimota/tree/main/blocks) and are maintained by developers. As an author, you don't edit this repo directly, but you can propose changes:

1. **Describe what you need** (e.g. "Cards block needs a 4th column option") to your development contact, ideally with a link to the page/preview showing why.
2. A developer implements and tests the change in a feature branch, then opens a pull request against `main`.
3. Once merged, the change is live in **preview** almost immediately and propagates to **production** the same way any other content change does — you don't need to do anything extra on your existing pages, but you may want to double-check pages that use that block still look right.
4. **Versioning:** block changes aren't versioned per-page — every page using a block always gets the block's current code. If a change might affect existing content, the developer should check a sample of pages using that block before merging.
5. This training site's [Blocks Library](../pages/blocks.html) reads the live manifest, so once a new block is added and documented there, it appears here automatically — no extra step needed from you.

---

## Troubleshooting & FAQ {#troubleshooting--faq}

**My block isn't rendering / looks like plain text.**
Check that the block name in the first cell is typed correctly (case and spacing matter less than getting the word right, but a typo like "Hreo" won't match). Compare against the [Blocks Library](../pages/blocks.html) list.

**My image isn't showing.**
Confirm the image was actually inserted/uploaded in da.live rather than just linked as external text, and that it hasn't been deleted from the media library.

**A link goes to the wrong locale.**
Double check the link target includes the correct `/{country}/{lang}/` prefix for the page you're editing.

**I published but bimota.com still shows the old content.**
Give it a minute for edge caching to refresh, then hard-refresh your browser (Ctrl/Cmd+Shift+R). If it's still stale after a few minutes, flag it to a developer.

**The Country Selector sends visitors to the homepage instead of the translated page.**
That page slug likely doesn't exist yet in the target locale — see [Localization](#localization) above. Publish the translated page under that locale to fix it.

**Can I preview a page before publishing it?**
Yes — always use the `.aem.page` preview URL first. Never rely on "it looked fine in da.live" alone; block styling only fully applies on preview/live.

---

## Best practices {#best-practices}

- **Naming:** keep page slugs short, lowercase, hyphenated (e.g. `tesi-h2`, not `Tesi H2 Page`), and identical across every locale folder.
- **One hero per page**, placed first.
- **Alt text:** always add meaningful alt text to images — it's required for accessibility and helps search visibility.
- **Don't skip locales silently:** if a page truly won't be translated into a given market, tell your team lead so it's a deliberate decision, not an oversight discovered by a visitor via the Country Selector fallback.
- **Reuse Fragments** for any content block that repeats across many pages (promo banners, legal notices) instead of copy/pasting the same table everywhere — it means one edit updates every page at once.
- **Review on both preview and live** after publishing anything visible on the homepage or a Hero, since these are the highest-traffic surfaces.
- **Cache awareness:** for time-sensitive content (e.g. a launch-day promo), publish a little ahead of time and verify on the live URL, not just preview.

---

*This guide is maintained alongside the [Blocks Library](../pages/blocks.html) in the DA Training site. If something here doesn't match what you see in da.live, please flag it — manifests and block behavior can evolve as the project grows.*
