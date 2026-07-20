/**
 * Bimota DA Training Site — shared JS (Bootstrap version)
 * Vanilla JS, no build step. Bootstrap's JS bundle handles the navbar
 * toggler/collapse behavior; this file just injects markup + small helpers.
 */

const BIMOTA_PREVIEW_HOST = 'https://main--bimota--kawaind.aem.page';
const BLOCKS_MANIFEST_URL = `${BIMOTA_PREVIEW_HOST}/docs/library/blocks.json`;
const TEMPLATES_MANIFEST_URL = `${BIMOTA_PREVIEW_HOST}/docs/library/templates.json`;

function currentPageId() {
  const path = window.location.pathname;
  if (path.includes('/pages/blocks.html')) return 'blocks';
  if (path.includes('/examples/')) return 'examples';
  if (path.includes('/docs/')) return 'authors';
  if (path.includes('/modules/')) return 'home';
  return 'home';
}

function injectNav() {
  const mount = document.getElementById('site-nav');
  if (!mount) return;
  const page = currentPageId();
  const root = mount.dataset.root || '.';
  const isActive = (id) => (page === id ? 'active' : '');
  mount.innerHTML = `
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">
      <div class="container">
        <a class="navbar-brand fw-bold" href="${root}/index.html">DA Training <span class="accent">&middot; Bimota</span></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain" aria-controls="navMain" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navMain">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item"><a class="nav-link ${isActive('home')}" href="${root}/index.html">Modules</a></li>
            <li class="nav-item"><a class="nav-link ${isActive('blocks')}" href="${root}/pages/blocks.html">Full Blocks Library</a></li>
            <li class="nav-item"><a class="nav-link ${isActive('authors')}" href="${root}/docs/authors.html">Author Guide</a></li>
            <li class="nav-item"><a class="nav-link ${isActive('examples')}" href="${root}/examples/it_it.html">Examples</a></li>
          </ul>
        </div>
      </div>
    </nav>`;
}

function injectFooter() {
  const mount = document.getElementById('site-footer');
  if (!mount) return;
  mount.innerHTML = `
    <div class="container">
      Internal training resource for Bimota content authors &middot;
      Source of truth: <a href="https://github.com/kawaind/bimota" target="_blank" rel="noopener">github.com/kawaind/bimota</a> &middot;
      Preview: <a href="${BIMOTA_PREVIEW_HOST}" target="_blank" rel="noopener">${BIMOTA_PREVIEW_HOST}</a>
    </div>`;
}

function wireCopyButtons() {
  document.querySelectorAll('.code-wrap').forEach((wrap) => {
    if (wrap.querySelector('.copy-btn')) return;
    const codeEl = wrap.querySelector('pre.code-block');
    if (!codeEl) return;
    const btn = document.createElement('button');
    btn.className = 'btn btn-sm btn-outline-light copy-btn';
    btn.type = 'button';
    btn.textContent = 'Copy';
    btn.addEventListener('click', async () => {
      try {
        await navigator.clipboard.writeText(codeEl.textContent);
        btn.textContent = 'Copied!';
        btn.classList.replace('btn-outline-light', 'btn-success');
        setTimeout(() => {
          btn.textContent = 'Copy';
          btn.classList.replace('btn-success', 'btn-outline-light');
        }, 1500);
      } catch (err) {
        btn.textContent = 'Ctrl/Cmd+C';
      }
    });
    wrap.appendChild(btn);
  });
}

// ---------------------------------------------------------------------------
// Manifest fetching (see docs/authors.md "Finding and using blocks" for the
// live URLs). ASSUMPTION, stated explicitly: the manifest is assumed to
// expose { "data": [ {name, path, ...}, ... ] }, the common shape for
// AEM block-library documents. Verify against the live URL and adjust
// parseManifest() if it differs — nothing else needs to change.
// ---------------------------------------------------------------------------
async function fetchManifest(url) {
  const res = await fetch(url, { cache: 'no-store' });
  if (!res.ok) throw new Error(`Failed to fetch ${url}: ${res.status}`);
  return res.json();
}

function parseManifest(json) {
  if (Array.isArray(json)) return json;
  if (Array.isArray(json.data)) return json.data;
  const merged = [];
  Object.values(json || {}).forEach((val) => {
    if (Array.isArray(val)) merged.push(...val);
    else if (val && Array.isArray(val.data)) merged.push(...val.data);
  });
  return merged;
}

window.BimotaTraining = {
  BIMOTA_PREVIEW_HOST,
  BLOCKS_MANIFEST_URL,
  TEMPLATES_MANIFEST_URL,
  fetchManifest,
  parseManifest,
};

document.addEventListener('DOMContentLoaded', () => {
  injectNav();
  injectFooter();
  wireCopyButtons();
  const observer = new MutationObserver(() => wireCopyButtons());
  observer.observe(document.body, { childList: true, subtree: true });
});
