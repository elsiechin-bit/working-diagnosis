---
title: How the Site Works
layout: topic.njk
specialty: About
description: A guide to editing Working Diagnosis — the folder structure, build process, git workflow, and deployment pipeline.
dek: Everything you need to know to edit and publish changes to the site
---

## What This Site Is

Working Diagnosis is built on **Eleventy**, a static site generator. That means:

- **No database or admin panel.** Pages are markdown files stored in folders.
- **No automatic publishing.** You edit locally, run a build, commit to git, then GitHub deploys.
- **You own the source code.** Everything is in a GitHub repository; no proprietary vendor lock-in.
- **Simple and durable.** A static site is fast, secure, and doesn't depend on a CMS vendor staying in business.

The tradeoff: you need to use your computer's terminal and basic git commands. But the process is straightforward once you understand the pattern.

## The Folder Structure

Pages are organized by medical specialty, then topic:

```
working-diagnosis/
├── cardiovascular/
│   ├── atrial-fibrillation/
│   │   └── index.md          ← The page content
│   ├── heart-failure/
│   │   └── index.md
│   └── index.md              ← The specialty landing page
├── dermatology/
│   ├── acne/
│   │   └── index.md
│   └── index.md
├── guides/
│   └── editing-the-site/     ← You are here
│       └── index.md
```

**Key rule:** URLs derive directly from folder names. The folder `cardiovascular/atrial-fibrillation/` becomes the URL `/cardiovascular/atrial-fibrillation/`.

## How to Edit a Page

### 1. Open the file in your text editor

Find the topic you want to edit, open the `index.md` file. For example:
- To edit the atrial fibrillation page: open `cardiovascular/atrial-fibrillation/index.md`
- Use VS Code, Notepad, or any text editor.

### 2. Understand front matter

Every page starts with metadata wrapped in `---`:

```markdown
---
title: Atrial Fibrillation
layout: topic.njk
specialty: cardiovascular
description: Diagnosis and management of AF in primary care
dek: A practical approach to recognising and treating the most common arrhythmia
---

## Red Flags
[Your content here...]
```

**Fields:**
- `title`: Page title (appears in browser tab and header)
- `layout`: Which template to use (almost always `topic.njk`)
- `specialty`: Folder name (cardiovascular, dermatology, etc.)
- `description`: Short summary (appears in search results)
- `dek` (optional): Subtitle or extended description

### 3. Write the content

Use **Markdown** syntax:

```markdown
## Heading 2
### Heading 3

**Bold text** and *italic text*

- Bullet point
- Another point

1. Numbered item
2. Another item

[Link text](https://example.com)
```

The site supports standard Markdown. For **Red Flags** and **Safety Netting** sections, use the built-in include:

```markdown
## Red Flags
{% include "panic-strip.njk" %}
```

### 4. Save and run the build

Once you've made changes, build the site locally:

```powershell
npm run build
```

This command:
- Reads all your markdown files
- Processes templates and layouts
- Generates HTML in the `_site/` folder
- Builds the search index
- Generates PDFs (if enabled)

The build takes 10–20 seconds. If it succeeds, you'll see:

```
[11ty] Writing _site/cardiovascular/atrial-fibrillation/index.html (v3.0.0)
[11ty] Copied 147 files...
```

**If it fails**, read the error message carefully. Common issues:
- Broken Markdown syntax
- Missing front matter fields
- Typo in layout name

### 5. Preview locally

Start the development server:

```powershell
npm start
```

Then open http://localhost:8080 in your browser. Changes auto-reload as you save.

## Workflow: Edit → Build → Commit → Deploy

Here's the complete process for publishing a change:

### Step 1: Make your edits
Edit the markdown file, save it.

### Step 2: Run build
```powershell
npm run build
```
Wait for success. Check that no errors appeared.

### Step 3: Preview (optional)
```powershell
npm start
```
Browse to http://localhost:8080 and verify your changes look right. Press `Ctrl+C` to stop the server.

### Step 4: Commit to git
```powershell
git add .
git commit -m "describe your change in present tense"
```

**Good commit messages:**
- "add hypertension screening guidance"
- "clarify AF rate control targets"
- "fix broken link in heart failure page"

**Bad commit messages:**
- "stuff", "updates", "changes", "fixed things"

### Step 5: Push to GitHub
```powershell
git push origin main
```

This sends your changes to the repository.

### Step 6: Wait for deployment
GitHub Actions automatically:
1. Pulls your changes
2. Runs the build again (as a safety check)
3. Deploys the site to GitHub Pages (within 1–2 minutes)

Check the [Actions tab](https://github.com/your-repo/actions) to see deployment status. A green checkmark means success.

## Creating a New Page

### 1. Create the folder
```powershell
mkdir "cardiovascular\new-topic"
```

Use kebab-case (dashes, lowercase): `heart-failure`, not `HeartFailure`.

### 2. Create index.md
```powershell
# Create empty file
New-Item "cardiovascular\new-topic\index.md"
```

### 3. Add front matter and content
```markdown
---
title: [Page Title]
layout: topic.njk
specialty: cardiovascular
description: [One-line summary]
---

## Red Flags
{% include "panic-strip.njk" %}

## Safety Netting
[Content...]

## How to manage [topic]
[Content...]
```

### 4. Build and test
```powershell
npm run build
npm start
```

Visit http://localhost:8080/cardiovascular/new-topic/ to verify it works.

### 5. Commit and push
```powershell
git add .
git commit -m "add new-topic page"
git push origin main
```

## Troubleshooting

### Build fails with "cannot find module"
Solution: Install dependencies first.
```powershell
npm install
```

### Changes don't appear after pushing
Check the Actions tab on GitHub. If the build failed there, read the error log and fix locally before pushing again.

### localhost:8080 doesn't work
- Is the dev server running? Run `npm start` if not.
- Try a different port: `eleventy --serve --port 8081`
- Close and reopen your browser.

### Git says "permission denied" or "lock file error"
Run the cleanup command:
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*git*"} | Stop-Process -Force; Remove-Item -Force .git/*.lock -ErrorAction SilentlyContinue
```

Then try again.

## Key Concepts to Remember

**The local build is the source of truth.** If it builds locally without errors, the deployment will succeed.

**Commit small, coherent changes.** Don't bundle unrelated edits. It makes history readable and rolling back easier if needed.

**The main branch must stay working.** Avoid committing broken builds to main. Always test locally first.

**URLs are permanent.** Changing a folder name breaks all links to that page. Rename carefully, and set up redirects if needed.

**GitHub Actions is a safeguard, not a debugger.** Use local build as your primary tool. If something breaks, fix it locally, not in the GitHub UI.

## Next Steps

- **Edit an existing page.** Pick a typo or small improvement and follow the workflow.
- **Create a new topic page.** Add something you've been meaning to document.
- **Explore the template structure.** Look at `_layouts/topic.njk` to understand how pages are styled.
- **Check git history.** Run `git log --oneline` to see past changes and commit patterns.

The more you edit, the faster it becomes. Within a few edits, the workflow will feel automatic.
