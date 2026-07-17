/**
 * Bimota DA Training Site — shared JS
 * Vanilla JS, no build step. Loaded on every page via:
 *   <script src="/assets/js/app.js" defer></script>
 *
 * Responsibilities:
 *  - Inject the shared top nav + footer (so we only maintain them once)
 *  - Wire up "Copy" buttons on any <pre class="code"> block
 *  - Provide fetchManifest()/renderBlockCard() helpers used by pages/blocks.html
 */

// ---------------------------------------------------------------------------
// Config — the two live manifests that are the single source of truth.
// These are da.live/AEM Edge Delivery Services "block library" documents,
// authored inside the Bimota project and published like any other page.
// ---------------------------------------------------------------------------
const BIMOTA_PREVIEW_HOST = 'https://main--bimota--kawaind.aem.page';
const BLOCKS_MANIFEST_URL = `${BIMOTA_PREVIEW_HOST}/docs/library/blocks.json`;
const TEMPLATES_MANIFEST_URL = `${BIMOTA_PREVIEW_HOST}/docs/library/templates.json`;

// ---------------------------------------------------------------------------
// Nav / footer injection
// ---------------------------------------------------------------------------
function currentPageId() {
  const path = window.location.pathname;
  if (path.endsWith('/pages/blocks.html')) return 'blocks';
  if (path.includes('/examples/')) return 'examples';
  if (path.endsWith('/docs/authors.md') || path.includes('authors')) return 'authors';
  return 'home';
}

function injectNav() {
  const mount = document.getElementById('site-nav');
  if (!mount) return;
  const page = currentPageId();
  const root = mount.dataset.root || '.';
  mount.innerHTML = `
    <div class="wrap">
      <a class="brand" href="${root}/index.html">DA Training <span>· Bimota</span></a>
      <ul>
        <li><a class="navlink ${page === 'home' ? 'active' : ''}" href="${root}/index.html">Home</a></li>
        <li><a class="navlink ${page === 'blocks' ? 'active' : ''}" href="${root}/pages/blocks.html">Blocks Library</a></li>
        <li><a class="navlink ${page === 'authors' ? 'active' : ''}" href="${root}/docs/authors.html">Author Guide</a></li>
        <li><a class="navlink ${page === 'examples' ? 'active' : ''}" href="${root}/examples/it_it.html">Examples</a></li>
      </ul>
    </div>`;
}

function injectFooter() {
  const mount = document.getElementById('site-footer');
  if (!mount) return;
  mount.innerHTML = `
    <div class="wrap">
      Internal training resource for Bimota content authors &middot;
      Source of truth: <a href="https://github.com/kawaind/bimota" target="_blank" rel="noopener">github.com/kawaind/bimota</a> &middot;
      Preview: <a href="${BIMOTA_PREVIEW_HOST}" target="_blank" rel="noopener">${BIMOTA_PREVIEW_HOST}</a>
    </div>`;
}

// ---------------------------------------------------------------------------
// Copy-to-clipboard for code blocks
// ---------------------------------------------------------------------------
function wireCopyButtons() {
  document.querySelectorAll('.code-wrap').forEach((wrap) => {
    if (wrap.querySelector('.copy-btn')) return;
    const codeEl = wrap.querySelector('pre.code');
    if (!codeEl) return;
    const btn = document.createElement('button');
    btn.className = 'copy-btn';
    btn.type = 'button';
    btn.textContent = 'Copy';
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(codeEl.textContent);
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1500);
      } catch (err) {
        btn.textContent = 'Press Ctrl/Cmd+C';
      }
    });
    wrap.appendChild(btn);
  });
}

// ---------------------------------------------------------------------------
// Manifest fetching
//
// ASSUMPTION (stated explicitly, verify against the live manifest and adjust
// the field names below if they differ): block-library and template-library
// documents published by the AEM block-library tooling expose a shape of:
//   { "data": [ { "name": "Hero", "path": "/path/to/example", ... }, ... ] }
// If the Bimota manifests instead expose a differently-shaped object (e.g.
// multiple named sheets), open the URL directly in a browser tab and update
// parseManifest() below to match — the fetch/render pipeline does not change.
// ---------------------------------------------------------------------------
async function fetchManifest(url) {
  const res = await fetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status}`);
  return res.json();
}

function parseManifest(json) {
  if (Array.isArray(json)) return json;
  if (Array.isArray(json.data)) return json.data;
  // Multi-sheet manifest: merge every array-valued sheet into one list.
  const merged = [];
  Object.values(json || {}).forEach((val) => {
    if (Array.isArray(val)) merged.push(...val);
    else if (val && Array.isArray(val.data)) merged.push(...val.data);
  });
  return merged;
}

// Fallback, offline catalogue mirrored from the public blocks repo
// (github.com/kawaind/bimota/tree/main/blocks) — used only if the live
// manifest can't be reached (e.g. no network, or CORS blocked in a given
// browser), so the training site is never a blank page.
const FALLBACK_BLOCKS = [
  { name: 'Hero', folder: 'hero', description: 'Full-bleed banner with heading, subheading, image/video background and an optional CTA. Used at the top of most landing pages.' },
  { name: 'Cards', folder: 'cards', description: 'Grid of image + text cards, e.g. model overview or feature highlights.' },
  { name: 'Teaser', folder: 'teaser', description: 'Image + heading + short copy teaser, similar to Cards but with a distinct h4 heading style.' },
  { name: 'Text with Image', folder: 'text-with-image', description: 'Two-column layout pairing rich text with one or two images that shift on scroll.' },
  { name: 'Columns', folder: 'columns', description: 'Configurable N-column layout (2–4 cols, grid/gallery/download variants, optional ratio classes).' },
  { name: 'Feature', folder: 'feature', description: 'Slide-based feature highlight with navigation dots, used for callouts within a page.' },
  { name: 'Highlight', folder: 'highlight', description: 'Full-width scaling image highlight slider.' },
  { name: 'Gallery', folder: 'gallery', description: 'Scroll-driven image gallery with intersection-based reveal animation.' },
  { name: 'Carousel', folder: 'carousel', description: 'Horizontally swipeable slide carousel.' },
  { name: 'Vehicle Selector', folder: 'vehicle-selector', description: 'Tabbed motorcycle model selector with image + description panes.' },
  { name: 'Specification', folder: 'specification', description: 'Technical spec block pairing stat labels/values with supporting images.' },
  { name: 'Specification Table', folder: 'specification-table', description: 'Categorised technical specification data table.' },
  { name: 'Table', folder: 'table', description: 'Generic HTML table block for simple tabular content.' },
  { name: 'CTA Buttons', folder: 'cta-buttons', description: 'One or more call-to-action buttons. Append "+" to link text to open in a new tab with an accessible warning.' },
  { name: 'Country Selector', folder: 'country-selector', description: 'Locale/country picker that redirects to the equivalent page under a different /{country}/{lang}/ prefix, backed by /countries.json.' },
  { name: 'Dealer Locator', folder: 'dealer-locator', description: 'Map-based dealer finder, localized by URL path (e.g. /it/it/ → Italian).' },
  { name: 'Woosmap Dealers', folder: 'woosmapdealers', description: 'WoosMap-powered dealer/store locator widget with region-based filtering.' },
  { name: 'News / Stories', folder: 'news-stories', description: 'Card-style list of news or story items with h5 headings.' },
  { name: 'Title', folder: 'title', description: 'Section heading block with optional pretitle and vertical line variant.' },
  { name: 'Text', folder: 'text', description: 'Plain rich-text section (no special decoration).' },
  { name: 'Image', folder: 'image', description: 'Standalone responsive image block.' },
  { name: 'Fragment', folder: 'fragment', description: 'Reusable content fragment, included by path — lets authors build shared sections (e.g. a promo banner) once and embed it on many pages.' },
  { name: 'Form', folder: 'form', description: 'Data-driven form block (contact/lead forms) built from configurable field definitions.' },
  { name: 'Header', folder: 'header', description: 'Site-wide navigation header, sourced from /nav (fragment), not placed manually on pages.' },
  { name: 'Footer', folder: 'footer', description: 'Site-wide footer, sourced from /footer (fragment), not placed manually on pages.' },
  { name: 'Error Page', folder: 'error-page', description: '404 / error state block.' },
];

window.BimotaTraining = {
  BIMOTA_PREVIEW_HOST,
  BLOCKS_MANIFEST_URL,
  TEMPLATES_MANIFEST_URL,
  fetchManifest,
  parseManifest,
  FALLBACK_BLOCKS,
};

document.addEventListener('DOMContentLoaded', () => {
  injectNav();
  injectFooter();
  wireCopyButtons();
  // Re-wire copy buttons if a page injects code blocks after load (e.g. blocks.html)
  const observer = new MutationObserver(() => wireCopyButtons());
  observer.observe(document.body, { childList: true, subtree: true });
});
