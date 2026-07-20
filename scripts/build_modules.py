#!/usr/bin/env python3
"""
Build script for the Bimota DA Training site's module pages.

Run from the site root:
    python3 scripts/build_modules.py

Regenerates:
    assets/js/modules-data.js   (lightweight index consumed by nav-tree.js)
    modules/*.html               (one static page per block/module)

Edit scripts/modules_data.py to add/update module content, then re-run this.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from modules_data import MODULES, CATEGORY_LABEL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES_DIR = os.path.join(ROOT, 'modules')
JS_DATA_PATH = os.path.join(ROOT, 'assets', 'js', 'modules-data.js')

os.makedirs(MODULES_DIR, exist_ok=True)


def esc(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def fields_table(fields):
    if not fields:
        return ''
    rows = ''.join(
        f'<tr><td class="fw-semibold" style="width:32%;">{f}</td><td>{d}</td></tr>'
        for f, d in fields
    )
    return f'''
      <h2 class="h5 mt-4">What you fill in</h2>
      <table class="table table-sm table-bordered">
        <tbody>{rows}</tbody>
      </table>'''


def images_html(images):
    if not images:
        return ''
    out = []
    for src, caption in images:
        out.append(f'''
      <img src="../assets/img/modules/{src}" alt="{esc(caption)}" class="module-shot img-fluid">
      <p class="module-shot-caption">{esc(caption)}</p>''')
    return ''.join(out)


def draft_body(m):
    return f'''
      <p class="lead fs-6">{m["what"]}</p>
      <h2 class="h5 mt-4">How it works</h2>
      <p>{m["how"]}</p>
      <h2 class="h5 mt-4">When authors use it</h2>
      <p>{m["when"]}</p>
      {fields_table(m["fields"])}
      {images_html(m.get("images", []))}
      <h2 class="h5 mt-4">Copy/paste snippet</h2>
      <div class="code-wrap">
        <pre class="code-block">{esc(m["snippet"])}</pre>
      </div>
      <p class="mt-3"><a href="https://github.com/kawaind/bimota/tree/main/blocks/{m["slug"]}" target="_blank" rel="noopener">View source on GitHub &rarr;</a></p>
      <div class="alert alert-warning mt-4" role="alert">
        <strong>Draft module.</strong> This page is written directly from the block's source code and is accurate,
        but hasn't been checked yet against an internal authoring guide the way the Verified modules have. If you
        have (or write) a guide for this block, share it so this page can be upgraded.
      </div>'''


def verified_body(m):
    sections = ''.join(
        f'<h2 class="h5 mt-4">{esc(title)}</h2>{html}'
        for title, html in m.get('custom_sections', [])
    )
    return f'''
      <p class="lead fs-6">{m["what"]}</p>
      {sections}
      {fields_table(m["fields"])}
      {images_html(m.get("images", []))}
      <h2 class="h5 mt-4">Copy/paste snippet</h2>
      <div class="code-wrap">
        <pre class="code-block">{esc(m["snippet"])}</pre>
      </div>
      <p class="mt-3"><a href="https://github.com/kawaind/bimota/tree/main/blocks/{m["slug"]}" target="_blank" rel="noopener">View source on GitHub &rarr;</a></p>
      <div class="alert alert-success mt-4" role="alert">
        <strong>Verified module.</strong> Written from {esc(m.get("source_doc", "an internal authoring guide"))}.
      </div>'''


PAGE_TMPL = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{num} {title} — Bimota DA Training</title>
<meta name="description" content="{summary_esc}">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/css/bootstrap.min.css">
<link rel="stylesheet" href="../assets/css/custom.css">
</head>
<body>
<div id="site-nav" data-root=".."></div>
<div class="jcr-path-bar" id="jcr-path-bar"></div>

<div class="training-shell">
  <nav class="tree-sidebar" id="tree-sidebar" data-root=".." data-current="{slug}"></nav>

  <main class="training-main">
    <div class="module-crumb">/content/bimota-training/blocks/{slug}</div>
    <div class="module-badges mb-2">
      <span class="badge bg-light text-dark border">{category_label}</span>
      {status_badge}
      <span class="text-secondary small ms-1">{minutes} min read</span>
    </div>
    <h1 class="h2">{title}</h1>
    <p class="text-secondary">{summary}</p>

    {body}

    <div class="mark-complete-row">
      <button type="button" class="btn btn-outline-primary" id="mark-complete-btn" data-slug="{slug}">Mark this module as reviewed</button>
    </div>

    <div class="module-nav-footer">
      <div>{prev_link}</div>
      <div>{next_link}</div>
    </div>
  </main>
</div>

<footer class="site-footer" id="site-footer"></footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.3/js/bootstrap.bundle.min.js"></script>
<script src="../assets/js/modules-data.js"></script>
<script src="../assets/js/app.js" defer></script>
<script src="../assets/js/nav-tree.js" defer></script>
</body>
</html>
'''


def build():
    for i, m in enumerate(MODULES):
        body = verified_body(m) if m['status'] == 'verified' else draft_body(m)
        status_badge = (
            '<span class="badge badge-verified">Verified guide</span>'
            if m['status'] == 'verified'
            else '<span class="badge badge-draft">Draft</span>'
        )
        prev_m = MODULES[i - 1] if i > 0 else None
        next_m = MODULES[i + 1] if i < len(MODULES) - 1 else None
        prev_link = (
            f'<a href="{prev_m["slug"]}.html">&larr; {prev_m["num"]} {esc(prev_m["title"])}</a>'
            if prev_m else ''
        )
        next_link = (
            f'<a href="{next_m["slug"]}.html">{next_m["num"]} {esc(next_m["title"])} &rarr;</a>'
            if next_m else '<a href="../pages/blocks.html">Back to full Blocks Library &rarr;</a>'
        )
        html = PAGE_TMPL.format(
            num=m['num'],
            title=esc(m['title']),
            slug=m['slug'],
            summary_esc=esc(m['summary']),
            summary=m['summary'],
            category_label=CATEGORY_LABEL[m['category']],
            status_badge=status_badge,
            minutes=m['minutes'],
            body=body,
            prev_link=prev_link,
            next_link=next_link,
        )
        out_path = os.path.join(MODULES_DIR, f"{m['slug']}.html")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'wrote {out_path}')

    # lightweight data file for nav-tree.js / index grid
    light = [
        dict(num=m['num'], slug=m['slug'], title=m['title'], category=m['category'],
             status=m['status'], summary=m['summary'], minutes=m['minutes'])
        for m in MODULES
    ]
    js = 'window.MODULES_DATA = ' + json.dumps(light, indent=2) + ';\n'
    with open(JS_DATA_PATH, 'w', encoding='utf-8') as f:
        f.write(js)
    print(f'wrote {JS_DATA_PATH}')
    print(f'\n{len(MODULES)} modules built '
          f'({sum(1 for m in MODULES if m["status"] == "verified")} verified, '
          f'{sum(1 for m in MODULES if m["status"] == "draft")} draft).')


if __name__ == '__main__':
    build()
