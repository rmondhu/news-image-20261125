// Measure the height of each page section so nothing hides behind the footer.
// Run from this directory:  node measure.mjs
const { chromium } = await import('/home/hatch/workspace/makefun/tools/node_modules/playwright/index.mjs');
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 }, deviceScaleFactor: 1 });
await page.goto('file:///home/hatch/workspace/makefun/entries/news-image-20261125/render.html', { waitUntil: 'load' });
await page.waitForTimeout(300);
const m = await page.evaluate(() => {
  const r = (sel) => {
    const el = document.querySelector(sel);
    if (!el) return null;
    const b = el.getBoundingClientRect();
    return { top: Math.round(b.top), bottom: Math.round(b.bottom), height: Math.round(b.height) };
  };
  const briefs = [...document.querySelectorAll('.brief')].map((el) => {
    const b = el.getBoundingClientRect();
    return Math.round(b.bottom);
  });
  const wrapped = [...document.querySelectorAll('.brief')].filter((el) => el.getBoundingClientRect().height > 20).length;
  return {
    head: r('.head'), strip: r('.strip'), chips: r('.chips'),
    leads: r('.leads'), feats: r('.feats'), map: r('.map'),
    also: r('.also'), foot: r('.foot'),
    briefCount: briefs.length, maxBriefBottom: Math.max(...briefs),
    wrappedBriefs: wrapped,
    scrollHeight: document.body.scrollHeight,
  };
});
console.log(JSON.stringify(m, null, 2));
await browser.close();
