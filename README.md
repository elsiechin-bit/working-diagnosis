# Working Diagnosis

An independent medical knowledge system curated by a practising New Zealand GP.

## Site Architecture

```
working-diagnosis/
│
├── 📁 Specialty Folders (medical domains)
│   ├── cardiovascular/
│   │   ├── atrial-fibrillation/
│   │   │   └── index.md ──→ /cardiovascular/atrial-fibrillation/
│   │   ├── heart-failure/
│   │   │   └── index.md ──→ /cardiovascular/heart-failure/
│   │   └── index.md ──→ /cardiovascular/
│   │
│   ├── dermatology/
│   │   ├── psoriasis/
│   │   │   └── index.md ──→ /dermatology/psoriasis/
│   │   └── index.md ──→ /dermatology/
│   │
│   ├── endocrinology/
│   ├── gastroenterology/
│   └── ... (other specialty folders)
│
├── 📁 Core Build & Config
│   ├── .eleventy.js          (Eleventy config, filters, passthrough copy)
│   ├── package.json           (npm scripts: start, build, build:nopdf)
│   ├── .github/
│   │   └── workflows/
│   │       └── deploy.yml     (GitHub Actions → GitHub Pages)
│   │
│   └── 📁 _site/              (Build output, .gitignored)
│       └── (generated HTML, CSS, search index)
│
├── 📁 Templates & Layouts
│   ├── _includes/
│   │   ├── header.njk
│   │   ├── footer.njk
│   │   ├── panic-strip.njk    (Red Flags & Safety Netting)
│   │   ├── ticker.njk
│   │   └── tools-aside.njk
│   │
│   └── _layouts/
│       ├── base.njk           (HTML structure)
│       ├── topic.njk          (article container, metadata)
│       ├── home.njk
│       └── note.njk, tool.njk (specialized layouts)
│
├── 📁 Scripts & Utilities
│   ├── scripts/
│   │   ├── build-pdfs.js      (PDF generation)
│   │   └── ... (other build utilities)
│   │
│   └── assets/                (passthrough copy: images, fonts, etc.)
│
├── 📁 Development & Drafts
│   ├── Drafts/                (prototypes, experiments)
│   ├── Delete Later/          (quarantine for final deletion review)
│   └── node_modules/          (.gitignored)
│
└── Configuration
    ├── README.md
    ├── CLAUDE.md              (project guidelines & build rules)
    └── .gitignore
```

## Build Pipeline

```
Source Files (Markdown)
        │
        ├─→ Eleventy (template engine: Nunjucks)
        │   ├─→ Render layouts
        │   ├─→ Apply filters (dateDisplay, readingTime, tagLabel)
        │   └─→ Generate HTML
        │
        ├─→ PDF Generation (scripts/build-pdfs.js)
        │   └─→ Generate PDFs from topics
        │
        ├─→ Pagefind (search indexing)
        │   └─→ Create search index
        │
        └─→ Output: _site/
            ├─→ HTML pages
            ├─→ CSS & assets
            ├─→ PDF files
            └─→ Search index

GitHub Actions (on push to main)
        └─→ Deploy to GitHub Pages
```

## URL Generation

URLs are derived directly from folder structure:

```
cardiovascular/
  └── index.md ──→ /cardiovascular/

cardiovascular/atrial-fibrillation/
  └── index.md ──→ /cardiovascular/atrial-fibrillation/

cardiovascular/heart-failure/
  └── index.md ──→ /cardiovascular/heart-failure/
```

**Rule:** Folder name = URL path segment. Redundant permalinks should be removed.

## Quick Start

```powershell
# Install dependencies
npm install

# Development: live reload (without PDFs for speed)
npm run start

# Full build: Eleventy + PDFs + search
npm run build

# Build without PDFs (development)
npm run build:nopdf
```

## Git Workflow

**Before committing:**
- Run local build checks: `npm run build`
- Confirm Eleventy builds successfully
- Check for broken links and template errors
- Verify mobile layout for major UI changes

**Commit style:**
- Short, descriptive, present tense
- Narrow scope (one focused change per commit)
- Good examples: "refine article card spacing", "add hypertension handout"
- Avoid: giant rewrites, mixed concerns, vague messages

**Deployment:**
- Commits to `main` trigger GitHub Actions automatically
- GitHub Actions builds and deploys to GitHub Pages
- **Critical:** `.github/workflows/deploy.yml` must reference `branches: [main]`

## Project Structure Reference

| Directory | Purpose |
|-----------|---------|
| `cardiovascular/`, `dermatology/`, etc. | Specialty folders (top level) |
| `*/*/` (e.g., `cardiovascular/atrial-fibrillation/`) | Topic folders (second level) |
| `_layouts/` | Page templates (Nunjucks) |
| `_includes/` | Reusable template components |
| `scripts/` | Build utilities (PDF generation, etc.) |
| `assets/` | Static files (images, fonts, CSS) |
| `Drafts/` | Development artifacts (not versioned) |
| `Delete Later/` | Quarantine for files awaiting final deletion |
| `_site/` | Build output (generated, .gitignored) |
| `node_modules/` | npm dependencies (.gitignored) |

## Content Structure

Each topic page uses:

**Front matter:**
```yaml
title: Topic Name
layout: topic.njk
specialty: cardiovascular
description: Brief description
dek: Optional subtitle
ctags: [tag1, tag2]  # content tags
```

**Core sections:**
- Red Flags (via panic-strip include)
- Safety Netting (via panic-strip include)
- Main content

**Layout:** `topic.njk` provides article container, header with metadata, and sources section.

## Development Notes

- **Template engine:** Nunjucks (both markdown and HTML)
- **CSS:** Uses CSS custom properties (`var(--color-name)`)
- **Filters:** dateDisplay (long format, NZ locale), dateISO, readingTime, tagLabel
- **Performance:** Reading time shows "1 min" for ≤1 min, "deep dive" for ≥20 min
- **Search:** Pagefind indexes built on each `npm run build`

## Windows Cleanup (Post-Session)

After working with the agent, clear stuck git processes and lock files:

```powershell
Get-Process | Where-Object {$_.ProcessName -like "*git*"} | Stop-Process -Force; Remove-Item -Force .git/*.lock -ErrorAction SilentlyContinue
```

---

**Working Diagnosis** combines clinical tools, patient education, medication references, essays, and experimental systems in one calm, thoughtful knowledge base.
