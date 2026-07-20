/**
 * Blocks Library logic.
 * Renders entirely from window.BLOCK_DATA (block-data.js) so the page works
 * immediately, offline or opened as a local file — no fetch required.
 * It then makes a best-effort attempt to enrich cards with a live preview
 * image from the manifest, but never blocks on it.
 */

(function blocksLib() {
  const accordion = document.getElementById('blocksAccordion');
  const statusLine = document.getElementById('status-line');
  const searchInput = document.getElementById('block-search');
  const categoryFilter = document.getElementById('category-filter');
  const noResults = document.getElementById('no-results');

  const CATEGORY_LABEL = {
    layout: 'Layout & content',
    product: 'Product & specs',
    interactive: 'Interactive',
    site: 'Site-wide',
  };

  function fieldsTable(fields) {
    if (!fields || !fields.length) return '';
    const rows = fields.map(([field, desc]) => `
      <tr><td class="fw-semibold" style="width:35%;">${field}</td><td>${desc}</td></tr>`).join('');
    return `<table class="table table-sm table-bordered mt-2"><tbody>${rows}</tbody></table>`;
  }

  function escapeHtml(str) {
    return str.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  }

  function renderAccordionItem(block, index) {
    const item = document.createElement('div');
    item.className = 'accordion-item block-card';
    item.dataset.name = block.name.toLowerCase();
    item.dataset.category = block.category;
    const collapseId = `collapse-${block.id}`;
    const headingId = `heading-${block.id}`;

    item.innerHTML = `
      <h2 class="accordion-header" id="${headingId}">
        <button class="accordion-button ${index === 0 ? '' : 'collapsed'}" type="button" data-bs-toggle="collapse" data-bs-target="#${collapseId}" aria-expanded="${index === 0}" aria-controls="${collapseId}">
          <span class="me-2 fw-bold">${block.name}</span>
          <span class="badge badge-category-${block.category} text-uppercase">${CATEGORY_LABEL[block.category]}</span>
        </button>
      </h2>
      <div id="${collapseId}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" aria-labelledby="${headingId}" data-bs-parent="#blocksAccordion">
        <div class="accordion-body">
          <p class="lead fs-6">${block.what}</p>
          <h3 class="h6 text-uppercase text-secondary mt-3">How it works</h3>
          <p>${block.how}</p>
          <h3 class="h6 text-uppercase text-secondary mt-3">When authors use it</h3>
          <p>${block.when}</p>
          ${block.fields && block.fields.length ? `<h3 class="h6 text-uppercase text-secondary mt-3">What you fill in</h3>${fieldsTable(block.fields)}` : ''}
          <h3 class="h6 text-uppercase text-secondary mt-3">Copy/paste snippet</h3>
          <div class="code-wrap">
            <pre class="code-block">${escapeHtml(block.snippet)}</pre>
          </div>
          <p class="mt-2 mb-0"><a href="https://github.com/kawaind/bimota/tree/main/blocks/${block.id}" target="_blank" rel="noopener">View source on GitHub →</a></p>
        </div>
      </div>`;
    return item;
  }

  function applyFilters() {
    const q = (searchInput.value || '').toLowerCase().trim();
    const cat = document.querySelector('input[name="cat"]:checked').value;
    let shown = 0;
    [...accordion.children].forEach((item) => {
      const matchesText = !q || item.dataset.name.includes(q);
      const matchesCat = cat === 'all' || item.dataset.category === cat;
      const visible = matchesText && matchesCat;
      item.style.display = visible ? '' : 'none';
      if (visible) shown += 1;
    });
    noResults.classList.toggle('d-none', shown > 0);
  }

  function renderAll() {
    accordion.innerHTML = '';
    window.BLOCK_DATA.forEach((block, i) => accordion.appendChild(renderAccordionItem(block, i)));
    applyFilters();
  }

  async function tryEnrichFromManifest() {
    if (!window.BimotaTraining) { statusLine.textContent = ''; return; }
    const { fetchManifest, parseManifest, BLOCKS_MANIFEST_URL } = window.BimotaTraining;
    try {
      const json = await fetchManifest(BLOCKS_MANIFEST_URL);
      const list = parseManifest(json);
      statusLine.textContent = list.length
        ? `Descriptions below are curated for training; ${list.length} block(s) also confirmed live at ${BLOCKS_MANIFEST_URL}.`
        : '';
    } catch (err) {
      statusLine.innerHTML = `Showing the curated block reference below (this works fully offline). `
        + `Live manifest check didn't succeed (${err.message}) — that's expected if this page was opened as a local file, `
        + `or if this network can't reach <code>main--bimota--kawaind.aem.page</code>.`;
    }
  }

  searchInput.addEventListener('input', applyFilters);
  categoryFilter.addEventListener('change', applyFilters);

  renderAll();
  tryEnrichFromManifest();

  // -----------------------------------------------------------------------
  // Try-it tool
  // -----------------------------------------------------------------------
  const TRY_DEFINITIONS = {
    hero: {
      label: 'Hero',
      fields: [
        { id: 'image', label: 'Background image URL', value: 'https://main--bimota--kawaind.aem.page/media/tesi-h2-hero.jpg' },
        { id: 'heading', label: 'Heading', value: 'Tesi H2' },
        { id: 'subheading', label: 'Subheading', value: 'The next chapter in hub-center steering.' },
        { id: 'ctaLabel', label: 'CTA label', value: 'Discover Tesi H2' },
        { id: 'ctaHref', label: 'CTA link', value: '/it/it/tesi-h2' },
      ],
      render: (v) => `
        <div class="eds-hero" style="background-image:linear-gradient(135deg, rgba(0,0,0,.55), rgba(0,0,0,.35)), url('${v.image}')">
          <h1 class="display-6">${v.heading}</h1>
          <p class="lead">${v.subheading}</p>
          <a class="btn btn-primary" href="${v.ctaHref}">${v.ctaLabel}</a>
        </div>`,
      snippet: (v) => `| Hero |  |\n|---|---|\n| ![${v.heading} hero image](${v.image}) | # ${v.heading}<br>${v.subheading}<br>[${v.ctaLabel}](${v.ctaHref}) |`,
    },
    cards: {
      label: 'Cards',
      fields: [
        { id: 'title1', label: 'Card 1 title', value: 'DB Series' },
        { id: 'body1', label: 'Card 1 text', value: 'Classic Bimota lines, modern engineering.' },
        { id: 'title2', label: 'Card 2 title', value: 'Tesi Series' },
        { id: 'body2', label: 'Card 2 text', value: 'Hub-center steering, reimagined.' },
      ],
      render: (v) => `
        <div class="row g-3">
          <div class="col-sm-6"><div class="eds-img-ph mb-2">image</div><h3 class="h5">${v.title1}</h3><p>${v.body1}</p></div>
          <div class="col-sm-6"><div class="eds-img-ph mb-2">image</div><h3 class="h5">${v.title2}</h3><p>${v.body2}</p></div>
        </div>`,
      snippet: (v) => `| Cards |  |\n|---|---|\n| ![](image1.jpg) | ### ${v.title1}<br>${v.body1} |\n| ![](image2.jpg) | ### ${v.title2}<br>${v.body2} |`,
    },
    'text-with-image': {
      label: 'Text with Image',
      fields: [
        { id: 'heading', label: 'Heading', value: 'Built in Rimini' },
        { id: 'body', label: 'Body text', value: 'Every Bimota is hand-assembled in our Rimini workshop, continuing 50 years of craftsmanship.' },
      ],
      render: (v) => `
        <div class="row g-3 align-items-center">
          <div class="col-sm-6"><h2 class="h4">${v.heading}</h2><p>${v.body}</p></div>
          <div class="col-sm-6"><div class="eds-img-ph">image</div></div>
        </div>`,
      snippet: (v) => `| Text with Image |  |\n|---|---|\n| ## ${v.heading}<br>${v.body} | ![](your-image.jpg) |`,
    },
    'cta-buttons': {
      label: 'CTA Buttons',
      fields: [
        { id: 'label1', label: 'Button 1 label', value: 'Book a test ride' },
        { id: 'href1', label: 'Button 1 link', value: '/it/it/test-ride' },
        { id: 'label2', label: 'Button 2 label (opens new tab)', value: 'Find a dealer' },
        { id: 'href2', label: 'Button 2 link', value: '/it/it/dealers' },
      ],
      render: (v) => `
        <a class="btn btn-primary me-2" href="${v.href1}">${v.label1}</a>
        <a class="btn btn-outline-primary" href="${v.href2}" target="_blank" rel="noopener">${v.label2} ↗</a>`,
      snippet: (v) => `| CTA Buttons |  |\n|---|---|\n| [${v.label1}](${v.href1}) [${v.label2}+](${v.href2}) |  |`,
    },
    'specification-table': {
      label: 'Specification Table',
      fields: [
        { id: 'title', label: 'Table title', value: 'Tesi H2 Specifications' },
        { id: 'label1', label: 'Row 1 label', value: 'Engine' },
        { id: 'value1', label: 'Row 1 value', value: 'Supercharged inline-4' },
        { id: 'label2', label: 'Row 2 label', value: 'Power' },
        { id: 'value2', label: 'Row 2 value', value: '197 hp' },
      ],
      render: (v) => `
        <h3 class="h5">${v.title}</h3>
        <table class="table table-bordered"><tbody>
          <tr><td>${v.label1}</td><td>${v.value1}</td></tr>
          <tr><td>${v.label2}</td><td>${v.value2}</td></tr>
        </tbody></table>`,
      snippet: (v) => `| Specification Table |  |\n|---|---|\n| ### ${v.title} |  |\n| Engine |  |\n|  | ${v.label1} | ${v.value1} |\n|  | ${v.label2} | ${v.value2} |`,
    },
  };

  function initTryInPage() {
    const select = document.getElementById('try-block-select');
    const fieldsMount = document.getElementById('try-fields');
    const preview = document.getElementById('try-preview');
    const snippetEl = document.getElementById('try-snippet');

    select.innerHTML = Object.entries(TRY_DEFINITIONS)
      .map(([key, def]) => `<option value="${key}">${def.label}</option>`).join('');

    function currentValues(def) {
      const values = {};
      def.fields.forEach((f) => {
        const el = document.getElementById(`try-field-${f.id}`);
        values[f.id] = el ? el.value : f.value;
      });
      return values;
    }

    function update() {
      const def = TRY_DEFINITIONS[select.value];
      const values = currentValues(def);
      preview.innerHTML = def.render(values);
      snippetEl.textContent = def.snippet(values);
    }

    function buildFields() {
      const def = TRY_DEFINITIONS[select.value];
      fieldsMount.innerHTML = def.fields.map((f) => `
        <div class="mb-2">
          <label for="try-field-${f.id}" class="form-label small fw-bold mb-1">${f.label}</label>
          <input id="try-field-${f.id}" type="text" class="form-control form-control-sm" value="${f.value}">
        </div>`).join('');
      fieldsMount.querySelectorAll('input').forEach((input) => input.addEventListener('input', update));
      update();
    }

    select.addEventListener('change', buildFields);
    buildFields();
  }

  initTryInPage();
}());
