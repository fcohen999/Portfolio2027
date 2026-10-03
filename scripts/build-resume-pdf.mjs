// Builds Fiona_Cohen_Resume.pdf from resume.html's print styles.
// Run after editing the résumé:  node scripts/build-resume-pdf.mjs
// Needs Playwright (npm i -D playwright, or a global install).
import { chromium } from 'playwright';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const out = path.join(root, 'Fiona_Cohen_Resume.pdf');

const browser = await chromium.launch();
const page = await browser.newPage();
await page.goto(pathToFileURL(path.join(root, 'resume.html')).href, { waitUntil: 'networkidle' });
await page.evaluate(() => document.fonts.ready);
await page.emulateMedia({ media: 'print' });

// Guard the 8pt floor: fail the build if any visible text in the sheet is smaller.
const tooSmall = await page.evaluate(() => {
  const bad = [];
  for (const el of document.querySelectorAll('.sheet, .sheet *')) {
    const hasText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!hasText) continue;
    const pt = parseFloat(getComputedStyle(el).fontSize) * 0.75;
    if (pt < 7.995) bad.push(`${pt.toFixed(2)}pt  ${el.textContent.trim().slice(0, 50)}`);
  }
  return bad;
});
if (tooSmall.length) {
  console.error('Text below 8pt:\n' + tooSmall.join('\n'));
  process.exit(1);
}

await page.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true });
await browser.close();
console.log('Wrote ' + path.relative(process.cwd(), out));
