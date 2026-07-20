/**
 * scripts/screenshot.js
 *
 * Generates screenshots of the key training-site pages for docs/README use.
 *
 * Setup:
 *   npm install -D playwright
 *   npx playwright install chromium
 *
 * Run (site must already be served locally, e.g. `npx http-server . -p 8080`):
 *   node scripts/screenshot.js http://localhost:8080
 *
 * Output: ./screenshots/*.png (created if missing)
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const baseUrl = process.argv[2] || 'http://localhost:8080';
const outDir = path.join(__dirname, '..', 'screenshots');

const pages = [
  { name: 'home', path: '/index.html' },
  { name: 'blocks-library', path: '/pages/blocks.html' },
  { name: 'author-guide', path: '/docs/authors.html' },
  { name: 'readme', path: '/README.html' },
  { name: 'example-it-it', path: '/examples/it_it.html' },
  { name: 'example-us-en', path: '/examples/us_en.html' },
  { name: 'example-de-de', path: '/examples/de_de.html' },
];

async function main() {
  if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch();
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  for (const p of pages) {
    const url = `${baseUrl}${p.path}`;
    console.log(`Capturing ${url}`);
    try {
      await page.goto(url, { waitUntil: 'networkidle', timeout: 15000 });
      // Give client-side manifest fetches a moment to render.
      await page.waitForTimeout(800);
      await page.screenshot({ path: path.join(outDir, `${p.name}.png`), fullPage: true });
    } catch (err) {
      console.error(`Failed to capture ${url}: ${err.message}`);
    }
  }

  await browser.close();
  console.log(`Done. Screenshots in ${outDir}`);
}

main();
