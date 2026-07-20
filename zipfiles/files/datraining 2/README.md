# Bimota DA Training Site

Internal training site teaching Bimota content authors how to build pages with **Adobe Edge Delivery Services (EDS)** and **da.live** — built with **Bootstrap 5** (via CDN, no build step) so it's easy for authors (not just developers) to navigate. Hosted on GitHub Pages at:

**https://sybrandlubbe.github.io/datraining/index.html**

## Download it as one site

This whole folder is the site — every page, style, and script. Two ways to get it as a single package:

1. **Zip download** (already provided alongside this README): unzip anywhere, then open `index.html` directly in a browser, or serve it locally (see below). No install, no build.
2. **Git clone**, if you'd rather work from source control:
   ```sh
   git clone https://github.com/sybrandlubbe/datraining.git
   ```

## What's here

```
.
├── index.html                   Module hub: JCR-tree sidebar + progress + module grid
├── modules/                     ⭐ One page per block (26), same layout as our AEM backend academy
│   ├── cta-buttons.html          Verified — from the CTA-buttons internal guide
│   ├── country-selector.html     Verified — from the Country Selector Block internal guide
│   ├── dealer-locator.html       Verified — from the Dealer Page (Woosmap-driven) internal guide
│   ├── woosmapdealers.html       Verified — from the same Dealer Page guide
│   └── ...22 more                Draft — accurate, written from block source, pending a guide
├── assets/
│   ├── css/custom.css           Brand color + Bootstrap overrides + JCR-tree sidebar layout
│   ├── js/
│   │   ├── app.js                Shared navbar/footer injection, copy buttons, manifest helpers
│   │   ├── nav-tree.js           Renders the sidebar tree, progress bar, and index module grid
│   │   └── modules-data.js       ⭐ GENERATED — do not hand-edit, see scripts/ below
│   └── img/modules/              Screenshots extracted from the internal authoring PDFs
├── pages/
│   ├── blocks.html              Full Blocks Library: all blocks in one accordion (alternate view)
│   ├── block-data.js            Content for the accordion view (kept in sync with modules/ by hand)
│   └── blocks-lib.js            Renders the accordion + search/filter + "Try it" tool
├── docs/
│   ├── authors.md               Full narrative Author Guide (source of truth, plain Markdown)
│   └── authors.html             Same guide, rendered with a sticky table-of-contents sidebar
├── examples/                    Full mock pages: /it/it, /us/en, /de/de
├── scripts/
│   ├── modules_data.py          ⭐ EDIT THIS to add/update a module's content
│   ├── build_modules.py         Regenerates modules/*.html + assets/js/modules-data.js
│   └── screenshot.js            Playwright script to generate screenshots of this site
├── .github/workflows/deploy.yml GitHub Actions: auto-deploy to GitHub Pages on push to main
└── README.md / README.html      This file (README.html is a styled, browsable version)
```

## Updating module content (section by section)

This site is meant to be built up incrementally as more internal authoring PDFs come in:

1. Open `scripts/modules_data.py` and find the module's entry (or add a new one).
2. Set `status="verified"` and add a `source_doc` + `custom_sections` (list of `(heading, html)` tuples) once you have an authoritative guide for that block. Drop any new screenshots in `assets/img/modules/<slug>/`.
3. Regenerate the site:
   ```sh
   python3 scripts/build_modules.py
   ```
4. This rewrites every file in `modules/` and `assets/js/modules-data.js`. Nothing else needs to change — the sidebar tree, progress bar, and index grid all read from that generated file automatically.

## Why Bootstrap

The site uses **Bootstrap 5** loaded from a CDN (`cdnjs.cloudflare.com`) for the navbar, grid, cards, accordion, forms, and buttons. This keeps every page visually consistent and familiar (navbar, cards, accordion) without writing custom layout CSS for each page — `assets/css/custom.css` only adds the Bimota brand color and a handful of small tweaks on top.

## Explaining each block

The heart of this training site is **`pages/blocks.html`**, an accordion with one entry per block. Each entry (content lives in `pages/block-data.js`) explains, for every real block in [github.com/kawaind/bimota/blocks](https://github.com/kawaind/bimota/tree/main/blocks):

- **What it does** — plain-English purpose
- **How it works** — what happens to the content you type, in non-technical terms
- **When authors use it** — the situations where this is the right block
- **What you fill in** — the specific fields/rows the block expects
- **Copy/paste snippet** — the exact da.live table shape to paste in

This renders **entirely offline** from `block-data.js` — it doesn't require reaching the live manifest to be useful, so it still works if this zip is opened locally or on a network without access to `main--bimota--kawaind.aem.page`. If that manifest *is* reachable, the page shows a small confirmation line at the top; if not, training content is unaffected.

## Source of truth

- Blocks (code): https://github.com/kawaind/bimota/tree/main/blocks
- Blocks manifest: https://main--bimota--kawaind.aem.page/docs/library/blocks.json
- Templates manifest: https://main--bimota--kawaind.aem.page/docs/library/templates.json
- Preview: https://main--bimota--kawaind.aem.page
- Live: https://main--bimota--kawaind.aem.live
- Public site: https://www.bimota.com/

> **Note on manifest field names:** the exact JSON shape returned by `blocks.json`/`templates.json` wasn't accessible from the environment this site was built in (network restrictions), so the block descriptions in `block-data.js` were written directly from the block source code in the public repo instead of the manifest. If you'd like the manifest's own descriptions/preview images pulled in too, open the manifest URL in a browser once to confirm its field names, then extend `blocks-lib.js` → `tryEnrichFromManifest()`.

## Local development

No build step required — it's static HTML/CSS/JS, plus Bootstrap from a CDN. Any static file server works:

```sh
npx http-server . -p 8080
# or
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html`. (Opening `index.html` directly via `file://` also works for browsing, though the "Copy" buttons and clipboard access work best served over http/https.)

## Pushing to GitHub Pages

1. Create (or reuse) the `sybrandlubbe/datraining` repository on GitHub.
2. Push this folder's contents to the `main` branch:
   ```sh
   git init
   git remote add origin https://github.com/sybrandlubbe/datraining.git
   git add .
   git commit -m "Bimota DA training site (Bootstrap)"
   git branch -M main
   git push -u origin main
   ```
3. In the repo's **Settings → Pages**, set the source to **GitHub Actions** (the included workflow handles the deploy — see below). Alternatively, set source to the `main` branch / root, since no build step is actually required.
4. The site will be live at `https://sybrandlubbe.github.io/datraining/index.html` within a few minutes.

## Generating screenshots

`scripts/screenshot.js` uses Playwright to capture each key page. See the script header for setup/run instructions.

## Testing & QA checklist

- [ ] `index.html` loads locally and every nav link resolves
- [ ] `pages/blocks.html` accordion opens/closes correctly and shows all blocks by default
- [ ] Search box and category filter both narrow the visible accordion items correctly
- [ ] "Try it" renders a live preview and an updated snippet for every block in the dropdown
- [ ] `docs/authors.html` renders the Markdown with a working sticky TOC
- [ ] All three example pages (`examples/it_it.html`, `us_en.html`, `de_de.html`) load and their cross-links to each other work
- [ ] GitHub Pages deployment succeeds (check the Actions tab) and the live URL matches local behavior
- [ ] Spot-check one page on a narrow (mobile) viewport width — the Bootstrap navbar should collapse into a toggler
