/**
 * build-pdfs.js
 *
 * Generates a PDF for every handout article in `_site/handouts/<slug>/`
 * by spinning up a tiny static server, pointing headless Chromium at each
 * page, and printing using the site's `@media print` stylesheet.
 *
 * Run AFTER `npx @11ty/eleventy` so `_site/` exists.
 *
 * PDFs land at `_site/handouts/<slug>/<slug>.pdf`, which is exactly the URL
 * the "PDF version" link in the handout layout points at.
 *
 * Requires: puppeteer (devDependency)
 */

const http = require('http');
const fs = require('fs');
const path = require('path');
const { URL } = require('url');

const SITE_DIR = path.join(__dirname, '..', '_site');
const HANDOUTS_DIR = path.join(SITE_DIR, 'handouts');

const MIME = {
  '.html': 'text/html; charset=utf-8',
  '.htm':  'text/html; charset=utf-8',
  '.css':  'text/css; charset=utf-8',
  '.js':   'application/javascript; charset=utf-8',
  '.mjs':  'application/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg':  'image/svg+xml',
  '.png':  'image/png',
  '.jpg':  'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif':  'image/gif',
  '.webp': 'image/webp',
  '.ico':  'image/x-icon',
  '.woff':  'font/woff',
  '.woff2': 'font/woff2',
  '.ttf':   'font/ttf',
  '.otf':   'font/otf',
  '.txt':   'text/plain; charset=utf-8',
  '.xml':   'application/xml; charset=utf-8',
  '.pdf':   'application/pdf'
};

// ---------- tiny static server -----------------------------------------------
function startServer(rootDir) {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      try {
        const reqUrl = new URL(req.url, 'http://localhost');
        let pathname = decodeURIComponent(reqUrl.pathname);
        // Resolve to a real file inside rootDir, blocking traversal
        let filePath = path.normalize(path.join(rootDir, pathname));
        if (!filePath.startsWith(rootDir)) {
          res.writeHead(403); return res.end('Forbidden');
        }
        if (fs.existsSync(filePath) && fs.statSync(filePath).isDirectory()) {
          filePath = path.join(filePath, 'index.html');
        }
        if (!fs.existsSync(filePath)) {
          res.writeHead(404); return res.end('Not found');
        }
        const ext = path.extname(filePath).toLowerCase();
        res.writeHead(200, { 'Content-Type': MIME[ext] || 'application/octet-stream' });
        fs.createReadStream(filePath).pipe(res);
      } catch (e) {
        res.writeHead(500); res.end(String(e));
      }
    });
    server.listen(0, '127.0.0.1', () => resolve(server));
  });
}

// ---------- main -------------------------------------------------------------
async function main() {
  if (!fs.existsSync(HANDOUTS_DIR)) {
    console.error('No _site/handouts/ found. Run `npx @11ty/eleventy` first.');
    process.exit(1);
  }

  let puppeteer;
  try {
    puppeteer = require('puppeteer');
  } catch (e) {
    console.error('Missing dependency: puppeteer.');
    console.error('Install with: npm install --save-dev puppeteer');
    process.exit(1);
  }

  const slugs = fs.readdirSync(HANDOUTS_DIR, { withFileTypes: true })
    .filter(d => d.isDirectory())
    .map(d => d.name)
    .filter(slug => fs.existsSync(path.join(HANDOUTS_DIR, slug, 'index.html')));

  if (slugs.length === 0) {
    console.error('No handout subdirectories with index.html found in _site/handouts/.');
    process.exit(1);
  }

  const server = await startServer(SITE_DIR);
  const { port } = server.address();
  const baseUrl = `http://127.0.0.1:${port}`;
  console.log(`Static server: ${baseUrl}`);

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });

  let written = 0;
  const failed = [];

  for (const slug of slugs) {
    const targetUrl = `${baseUrl}/handouts/${slug}/`;
    const outPath = path.join(HANDOUTS_DIR, slug, `${slug}.pdf`);
    process.stdout.write(`  ${slug} ... `);
    try {
      const page = await browser.newPage();
      await page.emulateMediaType('print');
      await page.goto(targetUrl, { waitUntil: 'networkidle0', timeout: 30000 });

      await page.pdf({
        path: outPath,
        format: 'A4',
        printBackground: true,
        preferCSSPageSize: true,
        margin: { top: '18mm', bottom: '18mm', left: '16mm', right: '16mm' }
      });

      await page.close();
      written += 1;
      console.log('ok');
    } catch (err) {
      failed.push({ slug, err: err.message });
      console.log('FAILED');
    }
  }

  await browser.close();
  server.close();

  console.log(`\n${written} of ${slugs.length} PDFs written.`);
  if (failed.length) {
    console.error('\nFailures:');
    failed.forEach(f => console.error(`  ${f.slug}: ${f.err}`));
    process.exit(1);
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
