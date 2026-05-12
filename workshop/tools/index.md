---
title: GP Tools
layout: base
permalink: /workshop/tools/
eleventyExcludeFromCollections: true
description: Interactive calculators and clinical decision support tools for primary care
---

<!DOCTYPE html>
<html lang="en-NZ">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GP Tools — Working Diagnosis</title>
<meta name="description" content="Interactive GP tools for clinical decision-making in primary care.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500;1,9..144,600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
</head>
<body>
<div class="page-wrapper">
  <header class="masthead">
    <div class="masthead-row">
      <div class="brand">Working <em>Diagnosis</em>.</div>
      <nav class="primary-nav">
        <a href="/library/">LIBRARY</a>
        <a href="/workbench/">WORKBENCH</a>
        <a href="/workshop/">WORKSHOP</a>
        <a href="/handouts/">HANDOUTS</a>
        <a href="/field-notes/">FIELD NOTES</a>
        <a href="/reading-list/">READING LIST</a>
        <a href="/about/">ABOUT</a>
        <button class="search-trigger" aria-label="Search" title="Search">⌘ SEARCH</button>
      </nav>
    </div>
  </header>

  <main class="main-content">
    <div class="topic-wrapper">
      <h1>GP Tools</h1>
      <p class="meta">Interactive calculators and decision support tools for clinical practice.</p>

      <div class="tools-grid">
        <div class="tool-card">
          <a href="/workshop/tools/adult-nzf/"><strong>Adult NZF Browser</strong></a>
          <p>Navigate the New Zealand Formulary for adults.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/af-risk/"><strong>AF Risk Assessment</strong></a>
          <p>CHA₂DS₂-VASc and HAS-BLED scoring for atrial fibrillation.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/anticholinergic-burden/"><strong>Anticholinergic Burden</strong></a>
          <p>Calculate cumulative anticholinergic load.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/antidepressant-weaning/"><strong>Antidepressant Weaning</strong></a>
          <p>Tapering schedules for safe discontinuation.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/benzo-conversion/"><strong>Benzodiazepine Conversion</strong></a>
          <p>Equivalent doses and switching guidance.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/cervical-screening/"><strong>Cervical Screening</strong></a>
          <p>NZ cervical screening guidelines and intervals.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/cha2ds2-vasc/"><strong>CHA₂DS₂-VASc Calculator</strong></a>
          <p>Stroke risk stratification for AF patients.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/copd/"><strong>COPD Assessment</strong></a>
          <p>Spirometry interpretation and GOLD staging.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/cts-6/"><strong>Carpal Tunnel Syndrome</strong></a>
          <p>CTS-6 diagnostic criteria and score.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/cv-risk/"><strong>CV Risk Assessment</strong></a>
          <p>Calculate cardiovascular disease risk.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/edd/"><strong>Expected Delivery Date</strong></a>
          <p>Calculate EDD from LMP and dating scan.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/geriatric-assessment/"><strong>Geriatric Assessment</strong></a>
          <p>Comprehensive geriatric screening tools.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/opioid-converter/"><strong>Opioid Converter</strong></a>
          <p>Equianalgesic dosing between opioids.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/paediatric-doses/"><strong>Paediatric Doses</strong></a>
          <p>Weights, doses, and paediatric formulae.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/psychotropic-selector/"><strong>Psychotropic Selector</strong></a>
          <p>Choose antidepressants and antipsychotics.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/rx-outside-nz/"><strong>Prescribing Outside NZ</strong></a>
          <p>What to prescribe when you're abroad.</p>
        </div>
        <div class="tool-card">
          <a href="/workshop/tools/steroid-equivalent/"><strong>Steroid Equivalents</strong></a>
          <p>Convert between different corticosteroids.</p>
        </div>
      </div>
    </div>
  </main>

  <footer class="footer">
    <p><strong>Working Diagnosis</strong> is one GP's hyperfunction project, made with a doable name.</p>
    <p><small>Not medical advice • • Not for use in emergencies • • Based on NZ/BPAC guidance</small></p>
  </footer>
</div>

<style>
.tools-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 40px;
}

.tool-card {
  padding: 20px;
  background: var(--warm);
  border: 1px solid var(--rule);
  border-radius: 4px;
}

.tool-card a {
  display: block;
  margin-bottom: 10px;
  color: var(--green-deep);
}

.tool-card a strong {
  font-weight: 600;
}

.tool-card a:hover {
  color: var(--green);
  text-decoration: underline;
}

.tool-card p {
  font-size: 0.95rem;
  color: var(--soft);
  margin: 0;
}

.topic-wrapper {
  max-width: 1280px;
  margin: 0 auto;
  padding: 40px 32px;
}

.topic-wrapper h1 {
  font-family: var(--font-d);
  font-size: 2.5rem;
  font-weight: 600;
  margin-bottom: 12px;
  color: var(--ink);
}

.meta {
  font-size: 1rem;
  color: var(--soft);
  margin-bottom: 0;
}
</style>
</body>
</html>
