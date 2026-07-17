/**
 * Blocks Library logic.
 * Loads BLOCKS_MANIFEST_URL / TEMPLATES_MANIFEST_URL live; falls back to the
 * FALLBACK_BLOCKS catalogue (mirrored from github.com/kawaind/bimota/blocks)
 * if the live fetch fails (offline, CORS, manifest moved, etc).
 */

(function blocksLib() {
  const grid = document.getElementById('blocks-grid');
  const templatesGrid = document.getElementById('templates-grid');
  const statusLine = document.getElementById('status-line');
  const searchInput = document.getElementById('block-search');
  const filterSelect = document.getElementById('block-filter');

  let allBlocks = [];

  function normalizeBlock(raw, index) {
    // Best-effort normalization across possible manifest field names.
    const name = raw.name || raw.title || raw.Name || `Block ${index + 1}`;
    const folder = raw.folder || raw.path || raw.id
      || String(name).toLowerCase().trim().replace(/\s+/g, '-');
    const description = raw.description || raw.Description || raw.desc || '';
    const preview = raw.preview || raw.image || raw.screenshot || raw.thumbnail || '';
    return {
      name, folder, description, preview, raw,
    };
  }

  function snippetFor(block) {
    return `| ${block.name} |  |\n` +
      `|---|---|\n` +
      `| <content for ${block.folder}> | <content> |\n\n` +
      `<!-- Type this table directly into your da.live document.\n` +
      `     See docs/authors.md for a filled-in example of this exact block. -->`;
  }

  function renderBlockCard(block) {
    const card = document.createElement('article');
    card.className = 'block-card';
    card.dataset.name = block.name.toLowerCase();
    card.dataset.folder = block.folder.toLowerCase();

    const img = block.preview
      ? `<img class="preview" src="${block.preview}" alt="${block.name} preview" loading="lazy">`
      : `<div class="preview" style="height:120px;display:flex;align-items:center;justify-content:center;background:var(--paper-dim);border-radius:6px;color:var(--ink-soft);font-size:.8rem;border:1px solid var(--line);">No preview image</div>`;

    card.innerHTML = `
      ${img}
      <h3>${block.name}</h3>
      <p class="desc">${block.description || 'No description provided in the manifest yet.'}</p>
      <details>
        <summary>Copy/paste snippet</summary>
        <div class="code-wrap">
          <pre class="code">${escapeHtml(snippetFor(block))}</pre>
        </div>
        <p><a href="https://github.com/kawaind/bimota/tree/main/blocks/${block.folder}" target="_blank" rel="noopener">View source →</a></p>
      </details>
    `;
    return card;
  }

  function renderTemplateCard(raw, index) {
    const name = raw.name || raw.title || `Template ${index + 1}`;
    const usesBlocks = raw.blocks || raw.uses || raw.components || [];
    const preview = raw.preview || raw.image || '';
    const card = document.createElement('article');
    card.className = 'card';
    card.innerHTML = `
      <h3>${name}</h3>
      ${preview ? `<img class="preview" src="${preview}" alt="${name} preview" loading="lazy" style="margin-bottom:10px;">` : ''}
      <p>${Array.isArray(usesBlocks) && usesBlocks.length
        ? `Uses: ${usesBlocks.map((b) => `<span class="badge">${b}</span>`).join(' ')}`
        : 'Block composition not specified in the manifest — open the template in da.live to inspect it.'}</p>
    `;
    return card;
  }

  function escapeHtml(str) {
    return str.replace(/[&<>]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  }

  function applyFilters() {
    const q = (searchInput.value || '').toLowerCase().trim();
    const filterVal = filterSelect.value;
    const allowedFolders = filterVal === 'all' ? null : filterVal.split(',');
    let shown = 0;
    [...grid.children].forEach((card) => {
      const matchesText = !q || card.dataset.name.includes(q) || card.dataset.folder.includes(q);
      const matchesFilter = !allowedFolders || allowedFolders.includes(card.dataset.folder);
      const visible = matchesText && matchesFilter;
      card.style.display = visible ? '' : 'none';
      if (visible) shown += 1;
    });
    statusLine.textContent = `Showing ${shown} of ${allBlocks.length} blocks.`;
  }

  async function loadBlocks() {
    const { fetchManifest, parseManifest, TEMPLATES_MANIFEST_URL, BLOCKS_MANIFEST_URL, FALLBACK_BLOCKS } = window.BimotaTraining;
    try {
      const json = await fetchManifest(BLOCKS_MANIFEST_URL);
      const list = parseManifest(json);
      if (!list.length) throw new Error('Manifest returned no rows');
      allBlocks = list.map(normalizeBlock);
      statusLine.textContent = `Loaded ${allBlocks.length} blocks live from ${BLOCKS_MANIFEST_URL}`;
    } catch (err) {
      allBlocks = FALLBACK_BLOCKS.map(normalizeBlock);
      statusLine.innerHTML = `Live manifest unavailable (${err.message}) — showing the offline catalogue mirrored from `
        + `<a href="https://github.com/kawaind/bimota/tree/main/blocks" target="_blank" rel="noopener">the blocks repo</a>. `
        + `Try opening <a href="${BLOCKS_MANIFEST_URL}" target="_blank" rel="noopener">the manifest directly</a> to confirm it's reachable from your network.`;
    }
    grid.innerHTML = '';
    allBlocks.forEach((b) => grid.appendChild(renderBlockCard(b)));
    applyFilters();

    try {
      const tJson = await fetchManifest(TEMPLATES_MANIFEST_URL);
      const tList = parseManifest(tJson);
      templatesGrid.innerHTML = '';
      tList.forEach((t, i) => templatesGrid.appendChild(renderTemplateCard(t, i)));
      if (!tList.length) throw new Error('empty');
    } catch (err) {
      templatesGrid.innerHTML = `<div class="callout warn">Templates manifest unavailable right now (${err.message}). `
        + `Open <a href="${TEMPLATES_MANIFEST_URL}" target="_blank" rel="noopener">${TEMPLATES_MANIFEST_URL}</a> directly, `
        + `or ask a developer which templates are current.</div>`;
    }

    initTryInPage();
  }

  searchInput.addEventListener('input', applyFilters);
  filterSelect.addEventListener('change', applyFilters);

  // ---------------------------------------------------------------------
  // Try-in-page tool — a hand-curated set of field definitions for the
  // most commonly authored blocks, grounded in the real block markup
  // (block.children = table rows, row.children = cells) used across the
  // Bimota blocks repo.
  // ---------------------------------------------------------------------
  const TRY_DEFINITIONS = {
    hero: {
      label: 'Hero',
      fields: [
        { id: 'image', label: 'Background image URL', type: 'text', value: 'https://main--bimota--kawaind.aem.page/media/tesi-h2-hero.jpg' },
        { id: 'heading', label: 'Heading', type: 'text', value: 'Tesi H2' },
        { id: 'subheading', label: 'Subheading', type: 'text', value: 'The next chapter in hub-center steering.' },
        { id: 'ctaLabel', label: 'CTA label', type: 'text', value: 'Discover Tesi H2' },
        { id: 'ctaHref', label: 'CTA link', type: 'text', value: '/it/it/tesi-h2' },
      ],
      render: (v) => `
        <div class="eds-hero" style="background-image:url('${v.image}')">
          <h1>${v.heading}</h1>
          <p>${v.subheading}</p>
          <a class="eds-cta" href="${v.ctaHref}">${v.ctaLabel}</a>
        </div>`,
      snippet: (v) => `| Hero |  |\n|---|---|\n| ![${v.heading} hero image](${v.image}) | # ${v.heading}<br>${v.subheading}<br>[${v.ctaLabel}](${v.ctaHref}) |`,
    },
    cards: {
      label: 'Cards',
      fields: [
        { id: 'title1', label: 'Card 1 title', type: 'text', value: 'DB Series' },
        { id: 'body1', label: 'Card 1 text', type: 'text', value: 'Classic Bimota lines, modern engineering.' },
        { id: 'title2', label: 'Card 2 title', type: 'text', value: 'Tesi Series' },
        { id: 'body2', label: 'Card 2 text', type: 'text', value: 'Hub-center steering, reimagined.' },
      ],
      render: (v) => `
        <div class="eds-cards">
          <div><div class="card-img">image</div><h3>${v.title1}</h3><p>${v.body1}</p></div>
          <div><div class="card-img">image</div><h3>${v.title2}</h3><p>${v.body2}</p></div>
        </div>`,
      snippet: (v) => `| Cards |  |\n|---|---|\n| ![](image1.jpg) | ### ${v.title1}<br>${v.body1} |\n| ![](image2.jpg) | ### ${v.title2}<br>${v.body2} |`,
    },
    'text-with-image': {
      label: 'Text with Image',
      fields: [
        { id: 'heading', label: 'Heading', type: 'text', value: 'Built in Rimini' },
        { id: 'body', label: 'Body text', type: 'text', value: 'Every Bimota is hand-assembled in our Rimini workshop, continuing 50 years of craftsmanship.' },
        { id: 'image', label: 'Image URL', type: 'text', value: '' },
      ],
      render: (v) => `
        <div class="eds-text-image">
          <div><h2>${v.heading}</h2><p>${v.body}</p></div>
          <div class="img-ph">${v.image ? `<img src="${v.image}" alt="" style="width:100%;height:100%;object-fit:cover;border-radius:8px;">` : 'image'}</div>
        </div>`,
      snippet: (v) => `| Text with Image |  |\n|---|---|\n| ## ${v.heading}<br>${v.body} | ![](${v.image || 'your-image.jpg'}) |`,
    },
    'cta-buttons': {
      label: 'CTA Buttons',
      fields: [
        { id: 'label1', label: 'Button 1 label', type: 'text', value: 'Book a test ride' },
        { id: 'href1', label: 'Button 1 link', type: 'text', value: '/it/it/test-ride' },
        { id: 'label2', label: 'Button 2 label (opens new tab)', type: 'text', value: 'Find a dealer' },
        { id: 'href2', label: 'Button 2 link', type: 'text', value: '/it/it/dealers' },
      ],
      render: (v) => `
        <div style="padding:30px 20px;">
          <a class="eds-cta" href="${v.href1}">${v.label1}</a>
          <a class="eds-cta" href="${v.href2}" target="_blank" rel="noopener" style="margin-left:10px;">${v.label2} ↗</a>
        </div>`,
      snippet: (v) => `| CTA Buttons |  |\n|---|---|\n| [${v.label1}](${v.href1}) [${v.label2}+](${v.href2}) |  |`,
    },
    'specification-table': {
      label: 'Specification Table',
      fields: [
        { id: 'title', label: 'Table title', type: 'text', value: 'Tesi H2 Specifications' },
        { id: 'label1', label: 'Row 1 label', type: 'text', value: 'Engine' },
        { id: 'value1', label: 'Row 1 value', type: 'text', value: 'Supercharged inline-4' },
        { id: 'label2', label: 'Row 2 label', type: 'text', value: 'Power' },
        { id: 'value2', label: 'Row 2 value', type: 'text', value: '197 hp' },
      ],
      render: (v) => `
        <div style="padding:20px;">
          <h3>${v.title}</h3>
          <table class="da-block-table">
            <tr><td>${v.label1}</td><td>${v.value1}</td></tr>
            <tr><td>${v.label2}</td><td>${v.value2}</td></tr>
          </table>
        </div>`,
      snippet: (v) => `| Specification Table |  |\n|---|---|\n| ### ${v.title} |  |\n| ${v.label1} | ${v.value1} |\n| ${v.label2} | ${v.value2} |`,
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
        <div class="field">
          <label for="try-field-${f.id}">${f.label}</label>
          <input id="try-field-${f.id}" type="text" value="${f.value}">
        </div>`).join('');
      fieldsMount.querySelectorAll('input').forEach((input) => input.addEventListener('input', update));
      update();
    }

    select.addEventListener('change', buildFields);
    buildFields();
  }

  loadBlocks();
}());
