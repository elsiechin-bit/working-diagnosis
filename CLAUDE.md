Use powershell for Windows

## Git Workflow

The build process should remain simple, predictable, and reversible.

Principles:
- Commit small, coherent changes
- Keep commits readable and narrowly scoped
- Prefer incremental refinement over large rewrites
- Do not combine unrelated changes in one commit
- Avoid long-lived experimental branches
- Preserve a working main branch whenever possible

Before committing:
- Run local build checks
- Confirm Eleventy builds successfully
- Check for broken links, missing includes, and template errors
- Verify mobile layout for major UI changes
- Ensure Lighthouse and performance budgets still pass where relevant

Preferred workflow:
1. Make one focused change
2. Run local build
3. Review generated output
4. Commit with clear message
5. Push to GitHub
6. Verify GitHub Actions deployment

Commit style:
- Short and descriptive
- Present tense
- No vague messages like "stuff", "fixes", or "updates"

Good examples:
- refine article card spacing
- add hypertension handout metadata
- simplify calculator layout
- fix Nunjucks date filter
- improve mobile navigation contrast

Avoid:
- giant AI-generated commits
- automated mass rewrites without review
- committing broken builds
- mixing styling, architecture, and content changes together
- introducing dependencies casually
- rewriting stable systems unnecessarily

GitHub Actions should function as a safeguard, not the primary debugging environment.

The local build is the source of truth.

When debugging:
- fix root causes rather than layering patches
- avoid speculative refactors during bug fixing
- revert quickly if a change destabilises the system

The project should remain understandable after months away from the codebase.

Future maintainability matters more than short-term cleverness.

## GitHub Actions & Deployment

**Branch consistency is critical for deployment automation.**

The repository uses `master` as the default branch (not `main`). The GitHub Actions workflow in `.github/workflows/deploy.yml` must always be configured to trigger on the `master` branch:

```yaml
on:
  push:
    branches: [master]
```

If the workflow ever references `[main]` instead of `[master]`, commits to `master` will not trigger builds and the site will not deploy. This must be caught and corrected immediately.

**Verification checklist after any branch-related changes:**
- Confirm `.github/workflows/deploy.yml` line 5 reads `branches: [master]`
- Confirm `git branch` shows `* master` as the active branch
- After pushing, verify GitHub Actions runs within 1 minute on the Actions tab

**If workflows stop triggering:**
1. Check the workflow file branch configuration
2. Verify the push went to `master` (not accidentally to a different branch)
3. Check GitHub Actions logs for any configuration errors

## File Organization

- Drafts folder: Development artifacts, prototypes, experiments - not for version control
- Delete Later folder: Quarantine location for files awaiting final deletion review
- scripts/ folder: Active utilities referenced in npm build process - keep in git
- _site/: Build output directory - must be in .gitignore
- node_modules/: Dependencies - must be in .gitignore

## Cleanup and Temporary Files

- Design documents (materia-medica.html, design-brief.html, etc.) belong in Delete Later
- Docx and PDF design files belong in Delete Later
- Empty test files and build logs belong in Delete Later
- Public folder if empty should be removed from tree
- .gitignore correctly configured to ignore build artifacts and dependencies

## Git Lock File Handling

- If git operations fail with lock file errors (.git/index.lock, etc.), clean up locally with: Remove-Item -Force .git/*.lock
- Sandbox environment has permission restrictions - lock file cleanup must occur on the user's Windows machine

## Windows Workflow: Post-Action Cleanup

After each working session with the AI agent, run this PowerShell command in the project folder to clear any stuck git processes and lock files:

```powershell
Get-Process | Where-Object {$_.ProcessName -like "*git*"} | Stop-Process -Force; Remove-Item -Force .git/*.lock -ErrorAction SilentlyContinue
```

Copy and paste as-is — this safely terminates any background git processes and clears lock files without error output if they don't exist.

## Site Structure & Naming

- Top level: specialty folders (cardiovascular, dermatology, endocrinology, etc.) - one per medical domain
- Second level: topic folders using kebab-case (atrial-fibrillation, cvd-risk-stratification, heart-failure)
- URLs derive directly from folder structure; redundant permalinks should be removed
- Each specialty and topic folder contains index.md (not separate files)
- Folder names must align exactly with intended URLs (e.g., msk not musculoskeletal, gynaecology not sexual-reproductive-health)

## Content Structure & Front Matter

- Topic pages use front matter: title, layout (topic.njk), specialty, and description
- Core content sections: "Red Flags" and "Safety Netting" (via panic-strip include)
- Specialty landing pages list topics with links in topic-list format
- Breadcrumb navigation pattern: Library / Specialty / Topic
- Optional fields: dek (subtitle), pageType, ctags (content tags), changes, changes_date, date, sources

## Content Tags & Categorization

- Standard tags include: redflags, guidelines, hacks, controversy, medicolegal, patient
- New tags can be created as needed; they are not restricted to the standard set
- Each tag has a display label defined in .eleventy.js
- Tags appear in header with tag-row class and are slugified for styling

## Layouts & Templates

- Base layout: base.njk (HTML structure, header, footer)
- Topic layout: topic.njk (article container, header with metadata, sources section) — used for most topic and specialty pages
- Home layout: home.njk
- Additional layouts exist (note.njk, tool.njk) — their purpose should be documented
- New layouts can be created with user approval and added to _layouts/
- Layout selection is determined case-by-case based on content type and requirements
- Includes directory contains: footer, header, panic-strip, ticker, tools-aside
- Template engine: Nunjucks (marked as markdownTemplateEngine and htmlTemplateEngine in config)

## Build Process & Scripts

- Default build: eleventy + PDF generation (scripts/build-pdfs.js) + pagefind search indexing
- Alternative: build:nopdf for development (eleventy + pagefind, skip PDF generation)
- Start command runs eleventy --serve for live development
- assets/ folder passed through unchanged (passthrough copy in .eleventy.js)

## Filters & Utilities

- dateDisplay: formats dates as "long" format in NZ locale (e.g., "12 May 2026")
- dateISO: returns ISO date format (YYYY-MM-DD)
- readingTime: calculates reading time at 200 words/minute; thresholds are tunable — currently shows "1 min" for ≤1 min, "deep dive" for ≥20 min
- tagLabel: converts tag keys to display labels (redflags → "Red flags", etc.)

## CSS & Styling Consistency

- Use CSS custom properties (var(--color-name)) instead of hardcoded colors
- CSS variables and color names are currently undocumented — when adding new colors or styles, verify existing variables first, then ask user before creating new ones
- Maintain font consistency across layouts (serif-body for specific text elements)
- Card design patterns use gap spacing and rounded corners
- All hardcoded values that appear in multiple places should be extracted to variables
