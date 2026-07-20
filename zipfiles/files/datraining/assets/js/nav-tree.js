/**
 * nav-tree.js — shared across index.html and every modules/*.html page.
 * Reads window.MODULES_DATA (assets/js/modules-data.js) and:
 *   - renders the JCR-tree sidebar (#tree-sidebar)
 *   - renders the path/progress bar (#jcr-path-bar)
 *   - renders the module grid on the index page (#module-grid), if present
 *   - tracks "reviewed" progress per module in localStorage
 */

(function navTree() {
  const STORAGE_KEY = 'bimotaTrainingProgress';
  const CATEGORY_LABEL = {
    layout: 'Layout & content',
    product: 'Product & specs',
    interactive: 'Interactive & utility',
    site: 'Site-wide (not authored per page)',
  };

  function getProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]');
    } catch (e) {
      return [];
    }
  }

  function setProgress(list) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(list));
  }

  function isDone(slug) {
    return getProgress().includes(slug);
  }

  function toggleDone(slug) {
    const list = getProgress();
    const idx = list.indexOf(slug);
    if (idx === -1) list.push(slug); else list.splice(idx, 1);
    setProgress(list);
    renderAll();
  }
  window.BimotaToggleModuleComplete = toggleDone;

  function renderPathBar() {
    const mount = document.getElementById('jcr-path-bar');
    if (!mount) return;
    const total = window.MODULES_DATA.length;
    const done = getProgress().filter((s) => window.MODULES_DATA.some((m) => m.slug === s)).length;
    mount.innerHTML = `
      <div class="container">
        <span class="diamond">&#9670;</span> /content/bimota-training
        <span class="progress-count">${done} / ${total} modules reviewed</span>
      </div>`;
  }

  function renderSidebar() {
    const mount = document.getElementById('tree-sidebar');
    if (!mount) return;
    const root = mount.dataset.root || '.';
    const current = mount.dataset.current || '';
    const byCategory = {};
    window.MODULES_DATA.forEach((m) => {
      byCategory[m.category] = byCategory[m.category] || [];
      byCategory[m.category].push(m);
    });

    let html = `
      <div class="tree-root">/content/bimota-training</div>
      <a class="tree-home" href="${root}/index.html">jcr:content [home]</a>`;

    Object.keys(CATEGORY_LABEL).forEach((cat) => {
      if (!byCategory[cat]) return;
      html += `<div class="tree-category-label">${CATEGORY_LABEL[cat]}</div>`;
      byCategory[cat].forEach((m) => {
        const done = isDone(m.slug);
        const active = current === m.slug ? 'active' : '';
        const markHtml = m.status === 'verified'
          ? '<span class="verified-mark" title="Verified against an authoring guide">&#10003;</span>'
          : '<span class="draft-mark" title="Draft — from block source, not yet reviewed">draft</span>';
        html += `<a class="tree-item ${active}" href="${root}/modules/${m.slug}.html">
          <span class="dot ${done ? 'done' : ''}"></span>
          <span class="num">${m.num}</span>
          <span class="text-truncate">${m.title}</span>
          ${markHtml}
        </a>`;
      });
    });

    html += `<div class="tree-legend">&#9679; filled = reviewed &middot; &#10003; = verified against a guide &middot; draft = pending review</div>`;
    mount.innerHTML = html;
  }

  function renderModuleGrid() {
    const grid = document.getElementById('module-grid');
    if (!grid) return;
    grid.innerHTML = window.MODULES_DATA.map((m) => {
      const statusBadge = m.status === 'verified'
        ? '<span class="badge badge-verified">Verified guide</span>'
        : '<span class="badge badge-draft">Draft</span>';
      const done = isDone(m.slug);
      return `
        <div class="col-md-6 col-lg-4">
          <a href="modules/${m.slug}.html" class="text-decoration-none text-body">
            <div class="card h-100 shadow-sm">
              <div class="card-body">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <span class="text-secondary font-monospace">${m.num}</span>
                  <div>${statusBadge} ${done ? '<span class="badge bg-secondary">Reviewed</span>' : ''}</div>
                </div>
                <h3 class="h6 mb-1">${m.title}</h3>
                <p class="small text-secondary mb-2">${m.summary}</p>
                <span class="badge bg-light text-dark border">${CATEGORY_LABEL[m.category]}</span>
                <span class="text-secondary small ms-1">${m.minutes} min read</span>
              </div>
            </div>
          </a>
        </div>`;
    }).join('');
  }

  function wireMarkComplete() {
    const btn = document.getElementById('mark-complete-btn');
    if (!btn) return;
    const { slug } = btn.dataset;
    function paint() {
      const done = isDone(slug);
      btn.textContent = done ? '\u2713 Marked as reviewed' : 'Mark this module as reviewed';
      btn.classList.toggle('btn-success', done);
      btn.classList.toggle('btn-outline-primary', !done);
    }
    btn.addEventListener('click', () => { toggleDone(slug); paint(); });
    paint();
  }

  function renderAll() {
    renderPathBar();
    renderSidebar();
    renderModuleGrid();
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderAll();
    wireMarkComplete();
  });
}());
