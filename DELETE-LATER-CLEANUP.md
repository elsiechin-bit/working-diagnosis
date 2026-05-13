# Delete Later Cleanup — May 13, 2026

These files are marked for deletion (design artifacts, test files, handouts not in active use):

## Design Documents (remove from git)
- design-brief.html
- design-mockup.html
- content-prompts.html

## Handout & Reference Files (remove from git)
- cholesterol-handout.html
- handout-midlife-fat.html
- handout_middleage_fat.docx
- materia-medica.html
- materia-medica-booklet.docx
- materia-medica-booklet.pdf
- ayurveda.html

## Draft/Test Files (remove from git)
- chronic-pain.md
- eleventy-output.txt
- test_write

## Next Steps
1. Folder itself remains as local quarantine area
2. Add "Delete Later/" to .gitignore if you want to keep files locally
3. Remove all 13 files from git history with: `git rm --cached "Delete Later/*"`
4. Commit: `git commit -m "Remove design artifacts and test files from version control"`

**Rationale:** These are development artifacts, not published content. They bloat repo history and create confusion about what's current.
