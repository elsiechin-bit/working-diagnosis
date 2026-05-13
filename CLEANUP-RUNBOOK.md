# Repo Cleanup Runbook — Execute on Your Machine

## What I Fixed ✅
1. **.gitignore** — Now properly excludes `_site/`, `node_modules/`, build artifacts
2. **CLAUDE.md** — Restored full project instructions (was corrupted)
3. **DELETE-LATER-CLEANUP.md** — Inventory of files to remove from git

## What You Need to Do on Windows

Run these commands in PowerShell in your project folder:

### Step 1: Clean up git state
```powershell
Get-Process | Where-Object {$_.ProcessName -like "*git*"} | Stop-Process -Force; Remove-Item -Force .git/*.lock -ErrorAction SilentlyContinue
```

### Step 2: Remove design/test files from git tracking (but keep locally)
```powershell
cd C:\Users\Li\Documents\working-diagnosis
git rm --cached "Delete Later\*" -r
```

### Step 3: Commit cleanup
```powershell
git commit -m "Remove design artifacts and test files from version control"
```

### Step 4: Test the build
```powershell
npm run build
```

If all passes → push to GitHub:
```powershell
git push origin main
```

## After This

- ✅ Repo is clean (no build artifacts in git history)
- ✅ .gitignore blocks future junk
- ✅ CLAUDE.md available for future sessions
- ✅ "Delete Later" stays as local sandbox, but doesn't clog git

Your repo will be maintainable again.
