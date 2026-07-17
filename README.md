# Bimota DA Training Site

Internal training site teaching Bimota content authors how to build pages with **Adobe Edge Delivery Services (EDS)** and **da.live**. Hosted on GitHub Pages at:

**https://sybrandlubbe.github.io/datraining/index.html**

## What's here

```
.
├── index.html                 Landing page / quick start
├── assets/
│   ├── css/styles.css         Shared stylesheet (plain CSS, no build step)
│   └── js/app.js              Shared nav/footer injection, copy buttons, manifest fetch helpers
├── pages/
│   ├── blocks.html            Interactive Blocks Library (live manifest + "try in page")
│   └── blocks-lib.js          Logic for the Blocks Library page
├── docs/
│   ├── authors.md             ⭐ Full Author Guide (source of truth, plain Markdown)
│   └── authors.html           Styled HTML rendering of authors.md (uses marked.js via CDN)
├── examples/
│   ├── it_it.html              Full mock page: /it/it
│   ├── us_en.html               Full mock page: /us/en
│   └── de_de.html               Full mock page: /de/de
├── scripts/
│   └── screenshot.js           Playwright script to generate screenshots of this site
├── .github/workflows/deploy.yml GitHub Actions: auto-deploy to GitHub Pages on push to main
└── README.md                   This file
```

## Source of truth

This training site does **not** copy block code — it reads live from the actual project:

- Blocks (code): https://github.com/kawaind/bimota/tree/main/blocks
- Blocks manifest: https://main--bimota--kawaind.aem.page/docs/library/blocks.json
- Templates manifest: https://main--bimota--kawaind.aem.page/docs/library/templates.json
- Preview: https://main--bimota--kawaind.aem.page
- Live: https://main--bimota--kawaind.aem.live
- Public site: https://www.bimota.com/

If a block is added, renamed, or removed in the project, the Blocks Library page picks it up automatically — nothing in this repo needs to change. If the manifest is unreachable, the page falls back to an offline catalogue mirrored from the blocks repo (see `assets/js/app.js` → `FALLBACK_BLOCKS`) so the site is never blank.

> **Note on manifest field names:** the exact JSON shape returned by `blocks.json`/`templates.json` wasn't accessible from this build environment (network restrictions), so `pages/blocks-lib.js` normalizes several plausible field names (`name`/`title`, `description`/`desc`, `preview`/`image`/`thumbnail`, etc.). Open the manifest URLs directly in a browser once and adjust `normalizeBlock()` in `blocks-lib.js` if the real field names differ — the fetch/render pipeline itself doesn't need to change.

## Local development

No build step required — it's static HTML/CSS/JS. Any static file server works:

```sh
npx http-server . -p 8080
# or
python3 -m http.server 8080
```

Then open `http://localhost:8080/index.html`.

## Pushing to GitHub Pages

1. Create (or reuse) the `sybrandlubbe/datraining` repository on GitHub.
2. Push this folder's contents to the `main` branch:
   ```sh
   git init
   git remote add origin https://github.com/sybrandlubbe/datraining.git
   git add .
   git commit -m "Bimota DA training site"
   git branch -M main
   git push -u origin main
   ```
3. In the repo's **Settings → Pages**, set the source to **GitHub Actions** (the included workflow handles the build/deploy — see below). Alternatively, set source to the `main` branch / root if you'd rather skip Actions entirely, since no build step is actually required.
4. The site will be live at `https://sybrandlubbe.github.io/datraining/index.html` within a few minutes.

## Generating screenshots

`scripts/screenshot.js` uses Playwright to capture each key page. See the script header for setup/run instructions.

## Testing & QA checklist

Run through this before treating a change as done:

- [ ] `index.html` loads locally and every nav link resolves
- [ ] `pages/blocks.html` shows a "Loaded N blocks live from…" status line (not the fallback-catalogue warning) when you have network access to `main--bimota--kawaind.aem.page`
- [ ] Blocks Library search and category filter both narrow the visible cards correctly
- [ ] "Try in page" renders a live preview and an updated snippet for every block in the dropdown
- [ ] `docs/authors.html` renders the Markdown (check the browser console for fetch errors if not)
- [ ] All three example pages (`examples/it_it.html`, `us_en.html`, `de_de.html`) load and their cross-links to each other work
- [ ] GitHub Pages deployment succeeds (check the Actions tab) and the live URL matches local behavior
- [ ] Spot-check one page on a narrow (mobile) viewport width
