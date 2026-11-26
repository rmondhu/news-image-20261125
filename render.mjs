// Render render.html to entry.png (1024x1024) with Playwright/Chromium.
// Run from this directory:  node render.mjs [out.png]
// Deterministic: fixed layout, no network, no random, no timestamps.
import fs from 'node:fs';
const { chromium } = await import('/home/hatch/workspace/makefun/tools/node_modules/playwright/index.mjs');
const out = process.argv[2] || 'entry.png';
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 1 });
await page.goto('file:///home/hatch/workspace/makefun/entries/news-image-20261125/render.html', { waitUntil: 'load' });
await page.waitForTimeout(300);
await page.screenshot({ path: out });
await browser.close();
console.log(out, fs.statSync(out).size);
