---
permalink: false
eleventyExcludeFromCollections: true
---

# Patient handout template

Reverse-engineered from anxiety, high-blood-pressure, common-cold, sleep-hygiene,
gout-acute-attack, and (for the Reading list / Footnotes endmatter pattern)
gastroenteritis and vaping. Use this file as both a spec and a copy-paste skeleton
when building a new handout. This file is excluded from the build via
`permalink: false`, `eleventyExcludeFromCollections: true`, and an entry in
`.eleventyignore`.

---

## 1. File location and naming

Save as `handouts/[kebab-case-slug]/index.md` in the project root
(`C:\Users\Li\Documents\working-diagnosis`, not the GP Website subfolder).

Then update `handouts/index.md`: replace the matching
`<span class="hl-soon">coming soon</span>` placeholder with a real link.

---

## 2. Front matter (required, in this order)

```yaml
---
title: [Condition] - [angle or specifier]
layout: topic.njk
pageType: handout
description: [One-sentence plain-language summary, ~15 to 25 words.]
---
```

Title uses space-hyphen-space (no emdashes). Title is a noun phrase a patient
would recognise, not a clinical heading. Examples:

- "High blood pressure (hypertension) - what the numbers mean"
- "Gout - managing an acute attack"
- "Sleep hygiene - setting up for better sleep"

---

## 3. Body skeleton (copy-paste, then fill)

```html
<p class="handout-back"><a href="/handouts/">← All handouts</a></p>

<p>[Opening paragraph: define the condition in lay terms. Anchor in NZ context
where relevant (epidemiology, Maori/Pacific prevalence, NZ services). Set the
reader's expectation about scope.]</p>

<h2>[What it feels like / What the numbers mean / Typical symptoms and timeline]</h2>

<p>[Brief framing sentence introducing the list, if needed.]</p>

<ul>
  <li>[Symptom or feature, plain language]</li>
  <li>[Symptom or feature]</li>
</ul>

<h2>[Why this happens / Why it matters]</h2>

<p>[Mechanism or consequences, in lay terms. One or two paragraphs. Avoid
jargon; if a clinical term must appear, gloss it on first use.]</p>

<h2>[What actually helps / Things you can do yourself]</h2>

<ul>
  <li><strong>[Action or option].</strong> [One to three sentences. Specific,
  practical, NZ-relevant.]</li>
  <li><strong>[Action or option].</strong> [Same.]</li>
</ul>

<h2>Medicines</h2>

<p>[Pharmacological options written for laypeople. Be explicit about who the
medicines are and are not for. Use "Your GP will..." framing for any decision
that requires a clinician. PHARMAC realities matter (funded vs unfunded).]</p>

<h2>[When to see your doctor / When to get help quickly]</h2>

<p>[Lead-in sentence.]</p>

<ul>
  <li>[Red flag]</li>
  <li>[Red flag]</li>
</ul>

<p>[For acute conditions: explicit 111 / ED instruction. For mental health:
crisis numbers below.]</p>

<h2>Questions to ask your doctor</h2>

<ul>
  <li>[Question a patient might not think to ask]</li>
  <li>[Question]</li>
</ul>

<div class="topic-endmatter">

<div class="endmatter-col">

### Reading list

<ul class="endmatter-list">
  <li><a href="URL">Resource name</a> - one-line description.</li>
  <li><a href="URL">Resource name</a> - one-line description.</li>
</ul>

</div>

<div class="endmatter-col">

### Footnotes

<ol class="endmatter-refs">
  <li id="fn1">Author/Org. Title. Publisher; Year. <a href="URL">domain</a></li>
  <li id="fn2">Author/Org. Title. Publisher; Year. <a href="URL">domain</a></li>
</ol>

</div>

</div>
```

Use only the H2 sections that fit the topic. Order is approximate but generally:
phenomenology, mechanism, self-management, medicines, monitoring, what to avoid,
red flags, questions, endmatter.

---

## 3a. Endmatter convention: Reading list + Footnotes

The two-column endmatter at the bottom of every handout has two distinct jobs.
Keep them apart - they serve different readers.

**Reading list (left column)** is patient-facing. Curated NZ resources the reader
can follow up with: Healthify, BPAC patient information, KidsHealth, condition-
specific charities, helplines. Five to seven entries is the sweet spot. Each
entry is a hyperlinked title followed by a one-line description ("what this gives
you"). Order by usefulness, not alphabetically. Keep the 24/7 helpline as a
non-link entry with the number bolded if there is one (Healthline 0800 611 116,
Quitline 0800 778 778, etc.).

**Footnotes (right column)** is for verification. Vancouver-style numbered entries
keyed to in-text superscripts. The rule is tight: only footnote **numerical
claims** in the body - statistics, prevalence figures, dose thresholds, schedule
items, named regulatory limits. Do not footnote qualitative claims, opinions, or
clinical practice tips - those belong to the writer's judgement and to the
Reading list as a whole. If a handout has no footnoteable statistics, leave the
Footnotes column out and let the Reading list span the row.

**Inline superscript pattern** in the body:

```html
[claim with a number]<sup class="fnref"><a href="#fn1">1</a></sup>
```

The matching list item gets `id="fn1"`. CSS handles the `:target` highlight when
a reader clicks the marker.

**Footnote format** is light-Vancouver: `Author/Org. Title. Publisher; Year. <a
href="URL">domain</a>`. Where you do not have a confident volume/issue/page
number, do not invent one - the named work plus a verifiable URL is enough. Link
to the organisation root if a deep URL is uncertain. Italicise journal names with
`<em>`.

**Confident sources, by handout type:**

- Epidemiology / notifications: ESR annual report, MPI/NZ Food Safety, NZ Health
  Survey
- Immunisation: Immunisation Advisory Centre (IMAC), NZ Immunisation Handbook
- Cardiovascular thresholds: Heart Foundation NZ, BPAC, NZ Primary Care Handbook
- Medicines: NZ Formulary (NZF), Medsafe, BPAC
- Smoking / vaping: Public Health England 2015 update, RCP 2016, Cochrane Tobacco
  Addiction Group, Te Whatu Ora Vaping Facts, Smokefree Environments Regulations
- Public health control / exclusion periods: Te Whatu Ora Communicable Disease
  Control Manual

---

## 4. Mental health crisis block (mental health topics only)

Place near the end of the red-flags section, before references. Bold the numbers.

```html
<p>If you are in crisis or having thoughts of suicide, call <strong>1737</strong>
(free, 24/7) or <strong>Lifeline 0800 543 354</strong>, or go to your nearest
emergency department.</p>
```

---

## 5. Tone and voice rules

- Second person ("you"). Thoughtful-GP register. Not chatbot, not paternalistic.
- Conservative on claims; hedge where the evidence hedges ("modest evidence",
  "for many people", "tend to").
- Empowering where honest ("very treatable", "the good news is", "most people
  recover").
- Define every acronym on first use: URTI, NSAIDs, CBT, CBT-I, GORD, HRT, HPV.
- NZ-specific throughout: NZ medicines, PHARMAC funding status, NZ services
  (Quitline, ACC, 1737, BPAC, Healthify, HealthPathways), NZ population context.
- Hyphens with spaces around them in place of emdashes. NEVER use em or en
  dashes anywhere on this site.
- Bullets use **bold lead-in** when the item is an action, recommendation, or
  named option; plain bullets when the item is a symptom or red flag.
- No inline `<style>` blocks. Plain HTML tags only: `<p>`, `<h2>`, `<h3>`,
  `<ul>`, `<ol>`, `<li>`, `<strong>`, `<em>`, `<a>`, and the endmatter wrappers
  (`<div class="topic-endmatter">`, `<div class="endmatter-col">`,
  `<ul class="endmatter-list">`, `<ol class="endmatter-refs">`). Superscript
  footnote markers use `<sup class="fnref"><a href="#fnN">N</a></sup>`. The site
  stylesheet handles everything.
- Length: 500 to 800 words of body content. Longer only if the topic genuinely
  needs it.
- Never invent statistics, doses, or guideline thresholds. Source from BPAC,
  NZF, MoH, HealthPathways. If a specific number is needed and not yet
  confirmed, leave a clear `[TODO: confirm threshold from BPAC]` marker rather
  than guessing.

---

## 6. What NOT to include

- Not a diagnostic checklist. Patients are reading this either after a consult
  or to prepare for one.
- No "consult your doctor" boilerplate. Red flags belong in their own section;
  references in the references block.
- No emojis. No decorative kickers. The `❍` kicker pattern is for pillar
  landing pages, not individual handouts.
- No tracking, analytics, or third-party embeds.
- No clinical decision support framing. These are patient handouts, not
  clinician tools. Workshop tools live elsewhere.

---

## 7. NZ resource shortcuts (use these URLs verbatim)

General:
- Healthify NZ: https://healthify.nz/
- Health Navigator: https://www.healthnavigator.org.nz/
- BPAC patient information: https://bpac.org.nz/patients.aspx
- HealthEd: https://healthed.govt.nz/
- KidsHealth NZ: https://www.kidshealth.org.nz/
- MyMedicines NZ: https://www.mymedicines.nz/cdhb
- Medsafe consumer info: https://www.medsafe.govt.nz/consumers/educational-material.asp

Mental health:
- 1737 (free call/text): https://1737.org.nz
- anxiety.org.nz: https://www.anxiety.org.nz
- depression.org.nz: https://www.depression.org.nz
- Mental Health Foundation NZ: https://www.mentalhealth.org.nz
- Lifeline NZ: https://www.lifeline.org.nz

Cardiovascular:
- Heart Foundation NZ: https://www.heartfoundation.org.nz
- Stroke Foundation NZ: https://www.stroke.org.nz

Diabetes / endocrine:
- Diabetes NZ: https://www.diabetes.org.nz
- Thyroid NZ: https://www.thyroid.org.nz

MSK / injury:
- ACC: https://www.acc.co.nz/im-injured/
- Arthritis NZ: https://arthritis.org.nz

Respiratory:
- Asthma and Respiratory Foundation NZ: https://www.asthma.org.nz
- Lung Foundation NZ: https://www.lung.org.nz

Skin:
- DermNet: https://www.dermnet.com
- Melanoma NZ: https://www.skincancer.org.nz

Smoking / alcohol:
- Quitline: https://www.quit.org.nz (0800 778 778)
- Alcohol Drug Helpline: https://www.alcohol.org.nz

System / rights:
- Te Whatu Ora: https://www.tewhatuora.govt.nz
- Health and Disability Commissioner: https://www.hdc.org.nz

---

## 8. Deploy checklist

1. Create `handouts/[slug]/index.md`.
2. Update the matching list item in `handouts/index.md` (remove the
   `coming soon` span, wrap the link text in `<a href="/handouts/[slug]/">`).
3. Local preview: `npx @11ty/eleventy --serve` (port 8080 or 8081).
4. Sanity-check on screen: back link works, both endmatter columns render
   (Reading list left, Footnotes right at desktop width; stacked on mobile), each
   superscript marker (`¹ ² ³`) jumps to the matching footnote with the
   paper-warm `:target` highlight, no stray emdashes, no broken external links.
5. Commit and push from VS Code terminal:
   - `git add .`
   - `git commit -m "Add [slug] handout"`
   - `git push`
6. Live in ~90 seconds via GitHub Actions.
