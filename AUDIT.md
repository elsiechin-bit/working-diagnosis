---
title: Site audit - structural and visual inconsistencies
layout: false
permalink: false
eleventyExcludeFromCollections: true
---

# Working Diagnosis - site audit

Date: 2026-05-11. Scope: folder/pillar structure and visual/styling drift (the two categories you flagged). This is a read-only audit. Nothing has been moved, renamed, or rewritten yet. Sections 6 and 7 are the proposed fix plan, awaiting your sign-off.

---

## 1. Ground truth: what "consistent" should mean

The canonical visual identity, derived from `_data/site.json`, `_layouts/base.njk`, `_layouts/topic.njk`, `assets/style.css`, and `handouts/_TEMPLATE.md`:

- **Type stack.** Fraunces (display), Newsreader (body), JetBrains Mono (kickers, nav, labels). Inter is loaded by base.njk but is not used by current layouts; it appears to be vestigial.
- **Palette tokens (style.css §1).** `--paper #F5F1E8`, `--paper-warm #EDE7D8`, `--ink #1A1F1C`, `--ink-soft #3A4540`, `--ink-mute #6B7A75`, `--green #2F6B5C`, `--green-deep #1F4A3F`, `--ochre #B8714F`, `--rule #D9D1BD`, plus per-room accents (library=green-deep, workbench=clay, workshop=slate).
- **Kicker convention.** Mono caps, ochre, `❍ ` prefix. The "At a glance" aside is hard-coded with `&#10063;` (the same glyph) in `base.njk` line 35.
- **Layout binding.** All pages inherit `base.njk`, then pick `topic.njk`, `note.njk`, `tool.njk`, or `home.njk`. The base injects the masthead, the GP-Tools sidebar, the TOC column, search, and the footer. Inline `<style>` blocks are explicitly forbidden by the handout template (line 213).
- **Five content types.** topic, tool, note, debunk, reference. Topic uses `topic.njk`. Note uses `note.njk`. Tool uses `tool.njk`. (No `debunk.njk` or `reference.njk` currently exist - debunks are being modelled as handouts/topics, and references as field notes.)
- **Nav source of truth.** `_data/site.json` `nav` array. Pillar URLs there are the authoritative routes.

The two anchor reference files for content shape are `handouts/_TEMPLATE.md` (patient handouts) and `cardiovascular/atrial-fibrillation/index.md` (clinical topics, with the panic-strip pattern).

---

## 2. Inventory snapshot

After excluding `node_modules`, `_site`, and `.git`:

- **~243 content files** across the source tree.
- **Markdown topic pages**: 154 (about half use `pillar:` front matter, half use `specialty:` - see §4.1).
- **Markdown handouts (`/handouts/*/index.md`)**: ~210, mostly consistent.
- **Standalone `.html` pages**: 71 files contain inline `<style>` blocks. Most of those are legitimate workshop tools and guidelines (single-file interactive apps). About 25 are pillar pages, patient handouts, or stray landing pages that should not be standalone.
- **Off-brand typography (Plus Jakarta Sans + DM Serif Display)**: 15 files (§5.2).
- **Layout uses `topic.njk`**: standard. One file uses `layout: topic` (no extension) - `field-guide/index.md` - which still resolves but is inconsistent.

---

## 3. The `.eleventyignore` smell

`.eleventyignore` already contains seven collision rules and is truncated mid-comment ("Standalone .html pages (no .md sibling, excluded"). It is being used as a band-aid for problems that should be solved by deleting or merging the duplicates. Every pair below is currently being papered over in `.eleventyignore`:

- `library/index.html` and `library/index.md`
- `workshop/tools/cha2ds2-vasc/index.html` and `index.md`
- `geriatrics/falls/index.html` and `index.md`
- `geriatrics/osteoporosis/index.html` and `index.md`
- `musculoskeletal/low-back-pain/index.html` and `index.md`
- `sexual-reproductive-health/cervical-screening/index.html` and `index.md`
- `sexual-reproductive-health/endometriosis/index.html` and `index.md`

In every case the resolution is the same: keep the markdown, delete the HTML (the HTML versions are off-brand legacy mockups - see §5).

---

## 4. Folder and pillar structure: findings

### 4.1 Folder names diverge from published URLs via `permalink:` remap

The nav URLs in `_data/site.json` are NOT broken. Every page under three pillars sets a `permalink:` in its front matter that remaps the output URL away from the source folder name:

| Source folder | Output URL via permalink | Pages affected |
|---|---|---|
| `musculoskeletal/` | `/msk/*` | 31 of 31 topic pages plus index |
| `sexual-reproductive-health/` | `/gynaecology/*` | 14 of 14 topic pages plus index |
| `infectious-disease/` (subset) | `/travel/*` | 7 pages: fit-to-fly, altitude-illness, insect-bite-prevention, pre-travel-consult, returning-traveller, malaria, travellers-diarrhoea |

This means the build *output* is internally consistent and the nav URLs work, but the source tree is harder to read - the folder name doesn't tell you the URL, and you have to read each file's front matter to know where it lands. The third row (`/travel/*`) is the more interesting one: it carves a *partial* URL namespace out of `infectious-disease/`, splitting that pillar's content across two URL roots (`/infectious-disease/` for vaccines/shingles/covid; `/travel/` for everything trip-related). The library and consult-room chrome pages both list "Travel" pointing at `/infectious-disease/` - the pillar landing page - even though the actual travel content lives at `/travel/*`. There is no pillar landing at `/travel/`.

Smaller noise pattern: every `paediatrics/*/index.md` explicitly sets `permalink: /paediatrics/[slug]/`, which matches what Eleventy would do by default. These are redundant but harmless.

Recommended action in §6.1: pick one strategy (either rename folders to match URLs and drop the permalinks, or keep the indirection but document it explicitly). Plus: decide what to do about Travel as a content area - it's currently a half-built sub-pillar without proper navigation.

### 4.2 Orphan pillar folders not in the nav

Folders that exist at the source root but are not declared in `site.json`:

| Folder | Contents | Status | Recommendation |
|---|---|---|---|
| `neurology-mental-health/` | One `index.md` that says "This file is a leftover from a folder rename. It produces no output. Delete the parent folder once safe to do so." | Self-documented dead code | Delete the folder. |
| `field-guide/` | One `index.md`, layout duplicates `library/index.md` (lists pillar rows 1-5) | Overlaps with `library/` and `field-notes/`; nothing links to it | Delete or fold into the Library. |
| `junk-drawer/` | `index.html` + `strange-ailments/index.html`, both standalone, both off-brand styling | Not in nav, not linked from anywhere indexed | Move salvageable content to `/field-notes/` or `/drafts/`; delete the folder. |
| `myths/common-myths/` | One standalone off-brand HTML page | Overlaps with `handouts/health-myths/index.html` (also standalone, also off-brand) | Pick one canonical home for "debunks" (proposal in §6), delete the other. |
| `nutrition/eating-well/` | One standalone off-brand HTML page | Duplicates `handouts/eating-well/index.html` and `lifestyle-prevention/` content | Delete. |
| `sleep/osa/` | One standalone off-brand HTML page | Duplicates `respiratory/obstructive-sleep-apnoea/` and `handouts/snoring-sleep-apnoea/` | Delete. |
| `experiments/` | Stub `index.md`, gated by `assets/workshop-gate.js` | Intentional scratch space, no public links | Keep, but exclude from collections (already is). Move to `/workshop/experiments/` so all experimental stuff lives under one room. |
| `test_dir/` | (empty / unread) | Almost certainly accidental | Confirm empty, then delete. |

### 4.3 Stray top-level files

- `design-mockup.html` (16 KB) at site root. Uses `--paper:#f5ede0` and a completely different layout. Pure scratch. Move to `/drafts/` or delete.
- `CNAME` is legitimate (GitHub Pages).
- `.eleventy.js`, `package.json`, `.gitignore`, etc. are legitimate.

### 4.4 Handouts: pillar-inline vs centralised

The site has a clear convention - patient handouts live under `/handouts/[slug]/` and are linked from pillar topic pages via `<a href="/handouts/[slug]/">`. The `handouts/_TEMPLATE.md` file is unambiguous about this.

But eleven inline patient-facing pages live inside the parent pillar instead of in `/handouts/`:

| Path | Should be |
|---|---|
| `geriatrics/falls/patient-handout.html` | `/handouts/falls-prevention/` (already exists - this is a duplicate) |
| `mental-health/addiction/patient-handout.html` | `/handouts/addiction/` (doesn't exist yet - move and convert) |
| `mental-health/anxiety/patient-handout.html` | `/handouts/anxiety/` (already exists as `.md` - this is a duplicate) |
| `mental-health/perinatal/patient-handout.html` | `/handouts/postnatal-depression/` (close match exists) or create `/handouts/perinatal-mental-health/` |
| `mental-health/psychosis-bipolar/patient-handout.html` | `/handouts/bipolar-disorder/` (exists) - move and merge |
| `mental-health/youth/patient-handout.html` | `/handouts/youth-mental-health/` (create) |
| `paediatrics/fever/patient-handout.html` | `/handouts/childhood-fever/` (already exists - duplicate) |
| `infectious-disease/pre-travel-consult/patient-handout.html` | `/handouts/pre-travel-consult/` (create) |
| `sexual-reproductive-health/cervical-screening/patient-handout.html` | `/handouts/cervical-screening/` (already exists - duplicate) |
| `infectious-disease/patient-handout.html` | Orphan at pillar root, no parent topic. Probably a draft. Move to `/drafts/`. |
| `lifestyle-prevention/weight-loss-medications/handout.html` | `/handouts/weight-loss-medications/` (already exists - duplicate) |

For the seven cases where the `/handouts/` version already exists, the inline HTML is duplicated content competing with the canonical handout. For the three cases where it doesn't, move the file, convert it from inline-styled HTML to the `.md` template format, and update the parent topic's "Patient handouts" links.

### 4.5 Pillar landing pages: inconsistent format

The 17 specialty pillars in the nav need an `index.md` at the root of each folder. Status:

- **Have a proper `index.md` using `topic.njk`**: cardiovascular, dermatology, gastroenterology, geriatrics, immunology-allergy, infectious-disease, lifestyle-prevention, mental-health, musculoskeletal, neurology, occupational-health, oncology-palliative, paediatrics, renal-urology, respiratory, sexual-reproductive-health.
- **Endocrinology** has `index.md` but with only a title - effectively empty.
- All landing pages render as a flat `<ul class="topic-list">` of links. They are functional but visually identical to each other - the kicker, dek, and any pillar-specific scene-setting are missing on most. This is consistent (in a flat sense), but not on-brand: the pillar landing is the place where the "❍ ochre kicker + Fraunces italic accent" identity should land first.

---

## 5. Visual and styling drift: findings

There are three competing visual systems on the site right now.

### 5.1 System A (canonical): base.njk + style.css

What the home page, all markdown topic pages, all markdown handouts, and the field notes use. Fraunces / Newsreader / JetBrains Mono, paper `#F5F1E8`, ochre kicker with `❍ ` prefix. Pages inherit the masthead, GP-Tools sidebar, footer, search, and TOC from `base.njk`. This is what the site should look like.

### 5.2 System B (off-brand legacy): "Plus Jakarta Sans + DM Serif Display"

Fifteen standalone HTML pages use this combination, which appears nowhere in `style.css` or any layout. Their paper colour also drifts: most use `#EFF3E6` (greenish) instead of `#F5F1E8` (warm). These pages bypass `base.njk` entirely - they are full standalone HTML documents with their own inline `<style>` block, their own ad-hoc masthead, and no connection to the site's nav or search. Files:

```
drafts/design-brief.html
geriatrics/falls/index.html                (excluded via .eleventyignore - keep .md)
geriatrics/osteoporosis/index.html         (excluded - keep .md)
infectious-disease/immunisation/index.html (NOT excluded - this one renders)
infectious-disease/travel-health/index.html (NOT excluded - this one renders)
lifestyle-prevention/ibs/infographic.html
musculoskeletal/low-back-pain/index.html   (excluded - keep .md)
musculoskeletal/shoulder/essay.html
musculoskeletal/shoulder/index.html
myths/common-myths/index.html
neurology/tinnitus/index.html
nutrition/eating-well/index.html
sexual-reproductive-health/cervical-screening/index.html (excluded - keep .md)
sexual-reproductive-health/endometriosis/index.html      (excluded - keep .md)
sleep/osa/index.html
```

The ones not currently excluded by `.eleventyignore` render as off-brand pages on the live site. The ones already excluded are dead weight in the source tree.

### 5.3 System C (correct palette, bypasses layout): inline-styled handouts and chrome pages

A third pattern: pages that use the correct Fraunces / Newsreader / paper-`#F5F1E8` palette but still inline the entire stylesheet into a `<style>` block and bypass `base.njk`. This is what the patient-handout HTML files do, and also what `library/index.html` and `consult-room/index.html` do.

Two consequences:

- **Code duplication.** The same ~70 lines of CSS variables and masthead styling are pasted into each of these files. Any palette tweak requires editing every copy.
- **Site chrome divergence.** Because they hand-roll their own masthead, the nav they include differs from page to page. `library/index.html` and `consult-room/index.html` both hard-code their own primary-nav row that lists ten items - and that list includes the two broken URLs from §4.1 (`/msk/`, `/gynaecology/`) plus a duplicate entry for `/infectious-disease/` (used for both "Vaccines" and "Travel").

Files in this pattern:

```
consult-room/index.html
library/index.html
handouts/acc/index.html              (also uses a dark mode palette - #0d1117 - completely off-brand)
handouts/eating-well/index.html
handouts/health-myths/index.html
infectious-disease/patient-handout.html
geriatrics/falls/patient-handout.html
lifestyle-prevention/weight-loss-medications/handout.html
mental-health/*/patient-handout.html  (5 files)
paediatrics/fever/patient-handout.html
sexual-reproductive-health/cervical-screening/patient-handout.html
infectious-disease/pre-travel-consult/patient-handout.html
```

`handouts/acc/index.html` is the worst case - it uses a GitHub-style dark mode (`--bg: #0d1117`) and `layout: false`, totally unmoored from the site.

### 5.4 Front-matter inconsistency: `pillar:` vs `specialty:`

Of 154 markdown topic pages, 43 use `pillar:` and 111 use `specialty:`. `topic.njk` reads `specialty` (line 17) and ignores `pillar` entirely. So the 43 files with `pillar:` render without the specialty kicker.

The 43 files with the wrong field name are concentrated in: all of cardiovascular, all of gastroenterology, all of renal-urology, all of respiratory. Other pillars use the correct `specialty:` field.

This is a pure find-replace fix (rename `pillar:` to `specialty:` in those 43 files; the values are already the correct human-readable strings).

### 5.5 Other front-matter drift

- `layout: topic` (no `.njk`) in `field-guide/index.md`. Works, but inconsistent. Standardise to `layout: topic.njk`.
- Some topic pages set `pageType: handout` and use `topic.njk` (the handouts in `/handouts/`); the layout has special handling for this (`topic.njk` lines 9-14 add a Print button). This is intentional and fine - leaving a note here so it's not "fixed" by mistake.
- The kicker `❍ ` prefix is used inconsistently within markdown bodies (e.g. `geriatrics/falls/index.md` uses `❍ At a glance`, `❍ Risk factor assessment`, etc. as part of body content rather than as the head-of-page kicker rendered by the layout). The bigger question is whether this in-body usage is a stand-in for a missing layout feature, or a deliberate design.

### 5.6 Chrome nav inside the standalone pages

`library/index.html` and `consult-room/index.html` hand-roll their own primary-nav row instead of inheriting from `base.njk`. Two real problems live there:

- Both pages list "Vaccines" and "Travel" as separate items, both linking to `/infectious-disease/`. So clicking either one goes to the same place. (Travel topics actually live at `/travel/*` per §4.1, but there's no `/travel/` landing page.)
- Both pages are inconsistent with `site.json`. They show eleven items in a hardcoded order; `site.json` declares 24 items grouped by `inMasthead`. Two sources of truth.

The fix is in Priority 2 of §7 - delete these standalones and let `base.njk` render the nav from `site.json`. The duplicate "Vaccines/Travel" entry needs resolving regardless: either a real `/travel/` landing page gets built, or the Travel entry is removed and travel topics are linked from the Infectious Disease landing.

---

## 6. Proposed clean taxonomy

### 6.1 Resolve the folder-vs-URL gap

The right answer depends on which is the canonical name in your head:

- **Path A (align source to URL).** Rename folders `musculoskeletal/` → `msk/`, `sexual-reproductive-health/` → `gynaecology/`. Then strip the `permalink:` lines from every page (47 files). Source folder name once again matches URL. This is the cleaner long-term state but a bigger one-time change.
- **Path B (keep the indirection, document it).** Leave the folder names and permalinks alone. Add a short note to `_data/site.json` or `CLAUDE.md` explaining the convention, so future-you doesn't get confused. Cheaper but the source tree stays mildly confusing.

Recommend **Path A** if you intend to keep growing these pillars - the duplication of "musculoskeletal" in every permalink across 31 files is the kind of thing that drifts. Path B if you suspect you might rename the URLs again (e.g. moving Gynae back to a fuller scope) and want one knob to turn.

Same decision applies to `/travel/`: either rename `infectious-disease/` → `infectious-disease/` AND `travel/` (two folders), promote `/travel/` to a proper sub-pillar with its own landing page, AND make the chrome nav point both routes correctly; or fold the travel content back under `/infectious-disease/travel/*` and drop the `/travel/` URL space. Either is defensible; the current half-state isn't.

Smaller cleanup: the redundant `permalink: /paediatrics/[slug]/` lines on every paediatrics page can be removed (they duplicate the default behaviour) once you've decided Path A or B for the bigger pillars - keep the front matter pattern consistent.

### 6.2 Orphan folder disposition

- `neurology-mental-health/` - **delete**.
- `field-guide/` - **delete**. (Function duplicated by `library/`.)
- `junk-drawer/` - **delete**, after deciding whether `strange-ailments` content moves to `/field-notes/` or `/drafts/`.
- `myths/common-myths/` - **delete the standalone HTML**. Move "common health myths" content into `/handouts/health-myths/` and rebuild that page as a proper `.md` handout. (The `debunk` content type can be reintroduced later as a layout if you want it visually distinct - see §6.4.)
- `nutrition/eating-well/` - **delete**. Content lives in `/handouts/eating-well/` and `/lifestyle-prevention/`.
- `sleep/osa/` - **delete**. Covered by `respiratory/obstructive-sleep-apnoea/` and `handouts/snoring-sleep-apnoea/`.
- `experiments/` - **move under `/workshop/experiments/`** so all gated/experimental content sits under one room. Keep current passphrase gating.
- `test_dir/` - **delete** after confirming it's empty.

### 6.3 Stray top-level files

- `design-mockup.html` - **move to `/drafts/design-mockup.html`** (or delete if it's superseded).

### 6.4 Content-type taxonomy clarification

The custom instructions name five content types (topic, tool, note, debunk, reference) but the codebase only has three layouts (topic, tool, note). Options:

- **Option A (smallest change).** Keep `topic.njk` and use `pageType: debunk` / `pageType: reference` to differentiate styling via CSS only.
- **Option B.** Add `debunk.njk` and `reference.njk` layouts that extend `base.njk`. Useful only if these types need a distinctly different page structure (e.g. debunks could open with a "Claim / Verdict / Evidence" panel pattern).

Recommend **Option A** for now and revisit if a real distinction emerges.

### 6.5 Patient handout consolidation

`/handouts/` is the single home for patient-facing handouts. All inline `*/patient-handout.html` files should be either deleted (where a `/handouts/[slug]/` already exists) or converted to `.md` and moved (where they don't). The pillar topic pages link to the canonical handout via `<a href="/handouts/[slug]/">`.

---

## 7. Fix plan, in order of severity and effort

Priority 1 to 3 cleans up the structural mess and gets every page rendering through `base.njk`. Priority 4 and 5 are cosmetic polish that becomes much easier once everything inherits the layout.

### Priority 1 - Dead and mechanical (do first; near-zero risk)

| # | Action | Files | Risk |
|---|---|---|---|
| 1.1 | Delete `neurology-mental-health/` (self-documented dead) | 1 folder | Low |
| 1.2 | Delete `test_dir/` (confirmed empty) | 1 folder | Low |
| 1.3 | Move `design-mockup.html` to `/drafts/` | 1 file | Low |
| 1.4 | Rename `pillar:` -> `specialty:` in the 43 affected `.md` files | 43 files, mechanical | Low |
| 1.5 | Normalise `layout: topic` -> `layout: topic.njk` in `field-guide/index.md` (then see 2.x for disposition of field-guide itself) | 1 file | Low |
| 1.6 | Fix the duplicate "Vaccines/Travel" entries in `library/index.html` and `consult-room/index.html` (or wait for Priority 2 to delete those files entirely) | 2 files | Low |

### Priority 2 - Resolve the index.html/index.md collisions

`.eleventyignore` lists seven collision pairs. In each pair the `.md` is canonical and the `.html` is the off-brand legacy. **Delete the seven `.html` files**, then **remove the corresponding `.eleventyignore` entries**. After that:

- `geriatrics/falls/index.html` (delete)
- `geriatrics/osteoporosis/index.html` (delete)
- `musculoskeletal/low-back-pain/index.html` (delete)
- `sexual-reproductive-health/cervical-screening/index.html` (delete)
- `sexual-reproductive-health/endometriosis/index.html` (delete)
- `library/index.html` (delete; `library/index.md` becomes the only library page - rebuild it to look like the current HTML if any of that styling is worth keeping, but as a proper topic layout)
- `workshop/tools/cha2ds2-vasc/index.html` is the keep-this case; delete `workshop/tools/cha2ds2-vasc/index.md` instead (it's a tool, the HTML is canonical for interactive tools).

Note 2.x: the `library/index.html` deletion means the Library landing page falls back to `library/index.md`. The hand-coded primary-nav inside `library/index.html` should be replaced by `base.njk`'s nav anyway. If you want the rich "rooms + specialty grid" layout the HTML provides, port that into the home or library template properly rather than keeping the standalone file.

### Priority 3 - Off-brand standalone pages (System B and orphan content)

Decide per file: salvage or scrap. My recommendation in each row:

| File | Recommendation |
|---|---|
| `infectious-disease/immunisation/index.html` | Convert to `index.md` using `topic.njk`. Currently renders off-brand on the live site. |
| `infectious-disease/travel-health/index.html` | Convert to `index.md`. Note: this overlaps with `infectious-disease/pre-travel-consult/index.md`. Merge or pick one. |
| `infectious-disease/patient-handout.html` | Move to `/drafts/` (orphan, no parent topic). |
| `musculoskeletal/shoulder/index.html` and `essay.html` | Convert to `index.md` (essay can become a `.md` field note if it's reflective rather than clinical). |
| `lifestyle-prevention/ibs/infographic.html` | Either keep as a deliberately interactive infographic linked from the IBS topic page (in which case give it a `permalink` and make sure it's loaded through `base.njk` or a dedicated tool layout), or convert to inline figures in the parent `.md`. |
| `myths/common-myths/index.html` | Migrate to `/handouts/health-myths/index.md` (proper handout) and delete this folder + the existing off-brand `handouts/health-myths/index.html`. |
| `nutrition/eating-well/index.html` | Delete (duplicates `handouts/eating-well/`). |
| `sleep/osa/index.html` | Delete (duplicates `respiratory/obstructive-sleep-apnoea/`). |
| `junk-drawer/index.html` + `strange-ailments/index.html` | Decide whether the content is worth keeping. If yes, move to `/field-notes/` as `.md`. Then delete `junk-drawer/`. |
| `field-guide/index.md` | Delete (duplicates `library/index.md`). |
| `neurology/tinnitus/index.html` | Convert to `index.md` (tinnitus is a clinical topic that belongs in the Neurology pillar). |
| `drafts/design-brief.html` | Already in `/drafts/` and excluded - leave or delete at your discretion. |

### Priority 4 - Inline patient-handout files (System C)

For each file in §4.4:

- Where a matching `/handouts/[slug]/index.md` already exists, **delete** the inline `*/patient-handout.html` and ensure the pillar topic page links to `/handouts/[slug]/`. Seven files in this category.
- Where no matching handout exists, **convert** the inline HTML to a fresh `/handouts/[slug]/index.md` using the `_TEMPLATE.md` skeleton, then delete the inline file. Three files in this category (mental-health/addiction, mental-health/youth, infectious-disease/pre-travel-consult).
- Move `lifestyle-prevention/weight-loss-medications/handout.html` (a duplicate) - delete; the canonical `/handouts/weight-loss-medications/index.md` exists.

### Priority 5 - Stray standalone handouts (System C, under `/handouts/`)

- `handouts/acc/index.html` - **highest priority within this group**: this is a dark mode page on a paper-themed site. Rewrite as `handouts/acc/index.md`.
- `handouts/eating-well/index.html` - rewrite as `index.md`.
- `handouts/health-myths/index.html` - rewrite as `index.md` (merging from `myths/common-myths/` if you want to keep that content).

### Priority 6 - Pillar landing page polish

Once the structural fixes land, each pillar `index.md` should get:

- A real kicker (`❍ Cardiovascular`).
- A one-sentence scene-setter (`description` front matter renders as `dek`).
- The current `topic-list` of conditions.

This is presentational polish, low risk, high visual payoff. Defer until after Priorities 1-3.

---

## 8. Recommended order of operations

The fixes are largely independent, so they can be done in parallel, but if I'm sequencing them:

1. **Priority 1** (the dead-and-broken pass) - one commit, takes the load off `.eleventyignore` and gets the nav working.
2. **Priority 2** (collision deletes) - one commit, removes the `.eleventyignore` entries at the same time.
3. **Priority 3** (off-brand standalone pages) - one commit per pillar so diffs stay reviewable.
4. **Priority 4** (inline handouts) - one commit, mostly mechanical deletions plus three real handout writes.
5. **Priority 5** (stray /handouts/ HTML) - one commit per page; the ACC page especially needs care because the dark-mode content has to be re-cast in the paper palette.
6. **Priority 6** (pillar landing pages) - last, when nothing else is moving.

Each step keeps the build green; nothing in this plan creates a half-finished state where pages 404.

---

## 9. Risks

- **Inbound external links.** Any URL change (Priority 1.1, or any folder rename) breaks links from outside the site (RSS, Twitter, bookmarks). The proposed nav-URL fix in §6.1 changes only how `site.json` advertises the routes; the underlying folder paths don't move, so external links are unaffected.
- **The `library/index.html` rebuild.** That file currently renders a richer landing page than `library/index.md`. Worth deciding whether to port its content into the template, or whether to keep `library/index.html` until the markdown version is properly designed.
- **Workshop tools using `index.html`** are intentional and should not be touched. Confirmed: all the workshop guideline and tool pages use the canonical palette and Fraunces/Newsreader. They are inline-styled because they are interactive single-file apps. Leave them alone.
- **`handouts/acc/index.html`'s dark mode**: the content underneath may be substantial. Rewriting it as a paper-palette handout is a real piece of work, not a mechanical conversion.

---

## 10. Things I need from you before starting

Four decisions gate the work:

1. **Folder-vs-URL strategy for MSK, Gynae, and Travel (§6.1).** Path A (rename folders, drop permalinks - clean long-term) or Path B (keep the indirection, document it - cheaper)?
2. **Travel as a content area.** Currently the URL space `/travel/*` exists but has no landing page, no nav entry, and the chrome lists "Travel" pointing somewhere else. Promote to a real sub-pillar, or fold back under `/infectious-disease/`?
3. **`library/index.html` disposition.** Delete and use the markdown version as-is (which is currently a flat list), or first port the richer "rooms + specialty" layout into a proper template?
4. **Junk drawer, myths, nutrition, sleep, field-guide.** I recommend deleting all five and letting any worthwhile content move to `/field-notes/` or `/handouts/`. Confirm or call out anything you want preserved as a pillar.

Smaller decisions can be made at the per-commit level once the big four are locked in.

---

## 11. Out of scope for this audit

These items came up while auditing but were outside the two categories you flagged. Flagging them here so we don't lose them:

- The unused `Inter` font load in `base.njk`.
- The `debunk` and `reference` content types named in the project instructions but not implemented as layouts.
- The `❍ ` kicker pattern used in-body rather than as a layout-rendered head element on `geriatrics/falls/index.md` and possibly elsewhere. Worth deciding whether this is a feature (in-body section openers) or a workaround.
- `field-notes/migraine/index.njk` and `field-notes/tips/index.njk` use `.njk` directly rather than `.md` - check whether these are intentional templates or stale.

Happy to fold any of these into the plan if you want.
