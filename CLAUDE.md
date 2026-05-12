Use powershell for Windows

## Version Control Rules

- Temporary analysis documents (audit reports, dated assessments) should not persist in git
- Design prototypes and mockups (HTML, design artifacts) should not persist in git
- Generated build outputs and logs should never be committed
- Empty directories should be moved to Delete Later folder rather than left in the tree
- All git rm operations must be followed by git commit to finalize removal from history

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