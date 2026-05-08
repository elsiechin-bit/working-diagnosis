<!DOCTYPE html>
<html lang="en-NZ">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Psychotropic Drug Selector  -  Working Diagnosis</title>
  <meta name="description" content="Interactive clinician reference: psychotropic drugs by indication, class, and patient factors. NZ-focused dosing, costs, interactions.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500;1,9..144,600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    /* === Tokens === */
    :root {
      --paper:      #F5F1E8;
      --paper-warm: #EDE7D8;
      --paper-deep: #E4DBC4;
      --ink:        #1A1F1C;
      --ink-soft:   #3A4540;
      --ink-mute:   #6B7A75;
      --green:      #2F6B5C;
      --green-deep: #1F4A3F;
      --ochre:      #B8714F;
      --rule:       #D9D1BD;
      --serif-display: 'Fraunces', Georgia, serif;
      --serif-body:    'Newsreader', Georgia, serif;
      --mono:          'JetBrains Mono', ui-monospace, 'SF Mono', Menlo, monospace;
    }

    * { box-sizing: border-box; }
    html, body { margin: 0; padding: 0; }

    body {
      font-family: var(--serif-body);
      font-size: 16px;
      line-height: 1.6;
      color: var(--ink);
      background: var(--paper);
      -webkit-font-smoothing: antialiased;
    }

    a { color: var(--green-deep); text-decoration: none; }
    a:hover { color: var(--green); }

    /* === Masthead === */
    .masthead {
      border-bottom: 1px solid var(--rule);
      padding: 22px 0 18px;
      background: var(--paper);
    }
    .masthead-row {
      max-width: 1080px;
      margin: 0 auto;
      padding: 0 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }
    .brand {
      font-family: var(--serif-display);
      font-weight: 600;
      font-size: 1.3rem;
      color: var(--ink);
      letter-spacing: -0.01em;
    }
    .brand em { font-style: italic; color: var(--green); }
    .primary-nav {
      display: flex;
      flex-wrap: wrap;
      gap: 18px;
    }
    .primary-nav a {
      font-family: var(--mono);
      font-size: 0.72rem;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--ink-mute);
    }
    .primary-nav a:hover { color: var(--green); }

    /* === Layout === */
    .wrap { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
    main { padding: 48px 0; }

    .page-header {
      margin-bottom: 40px;
      padding-bottom: 32px;
      border-bottom: 1px solid var(--rule);
    }
    .page-title {
      font-family: var(--serif-display);
      font-weight: 500;
      font-size: 3rem;
      line-height: 1.05;
      letter-spacing: -0.025em;
      margin: 0 0 16px;
    }
    .page-dek {
      font-size: 1.1rem;
      color: var(--ink-soft);
      margin: 0;
      max-width: 680px;
      line-height: 1.5;
    }

    /* === Filter panel === */
    .filters {
      margin-bottom: 20px;
      padding: 24px;
      background: var(--paper-warm);
      border: 1px solid var(--rule);
      border-radius: 4px;
    }

    .filter-row {
      display: flex;
      align-items: flex-start;
      gap: 16px;
      margin-bottom: 18px;
    }
    .filter-row:last-child { margin-bottom: 0; }

    .filter-label {
      font-family: var(--mono);
      font-size: 0.68rem;
      letter-spacing: 2.5px;
      text-transform: uppercase;
      color: var(--ochre);
      font-weight: 500;
      white-space: nowrap;
      min-width: 92px;
      padding-top: 7px;
    }

    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
    }

    .filter-pill {
      font-family: var(--mono);
      font-size: 0.7rem;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      padding: 5px 11px;
      border: 1px solid var(--rule);
      border-radius: 3px;
      background: var(--paper);
      color: var(--ink-mute);
      cursor: pointer;
      transition: border-color 0.1s, color 0.1s, background 0.1s;
      line-height: 1.2;
      user-select: none;
    }
    .filter-pill:hover {
      border-color: var(--green);
      color: var(--green-deep);
    }
    .filter-pill.active {
      background: var(--green-deep);
      border-color: var(--green-deep);
      color: var(--paper);
    }
    .filter-pill.active:hover {
      background: var(--green);
      border-color: var(--green);
    }

    /* === Active chips bar === */
    .chips-bar {
      display: none;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 16px;
      padding: 11px 16px;
      background: rgba(47, 107, 92, 0.05);
      border: 1px solid rgba(47, 107, 92, 0.2);
      border-radius: 3px;
    }
    .chips-bar.visible { display: flex; }

    .chips-label {
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--ink-mute);
      margin-right: 4px;
      white-space: nowrap;
    }

    .chips-list {
      display: flex;
      flex-wrap: wrap;
      gap: 7px;
      flex: 1;
    }

    .active-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--mono);
      font-size: 0.68rem;
      letter-spacing: 0.4px;
      padding: 3px 9px;
      background: rgba(47, 107, 92, 0.1);
      border: 1px solid rgba(47, 107, 92, 0.35);
      border-radius: 3px;
      color: var(--green-deep);
    }

    .chip-remove {
      display: inline-flex;
      align-items: center;
      cursor: pointer;
      color: var(--green);
      font-size: 0.9rem;
      line-height: 1;
      background: none;
      border: none;
      padding: 0;
      font-family: var(--mono);
    }
    .chip-remove:hover { color: var(--ochre); }

    .chips-clear {
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--ochre);
      cursor: pointer;
      background: none;
      border: none;
      padding: 0;
      white-space: nowrap;
      margin-left: auto;
    }
    .chips-clear:hover { color: var(--ink); }

    /* === Results row === */
    .results-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 12px;
    }
    .results-meta {
      font-family: var(--mono);
      font-size: 0.78rem;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--ink-mute);
    }
    .expand-all-btn {
      font-family: var(--mono);
      font-size: 0.65rem;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: var(--ink-mute);
      background: none;
      border: none;
      cursor: pointer;
      padding: 0;
    }
    .expand-all-btn:hover { color: var(--green); }

    /* === Table === */
    .table-wrapper {
      overflow-x: auto;
      border: 1px solid var(--rule);
      border-radius: 4px;
      margin-bottom: 48px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      background: var(--paper);
    }

    thead {
      background: var(--paper-warm);
      border-bottom: 2px solid var(--rule);
    }

    th {
      font-family: var(--serif-display);
      font-weight: 500;
      font-size: 0.95rem;
      text-align: left;
      padding: 16px;
      color: var(--ink);
      letter-spacing: -0.005em;
    }
    th.th-expand { width: 44px; padding: 16px 12px; }

    td {
      padding: 14px 16px;
      border-bottom: 1px solid var(--rule);
      font-size: 0.95rem;
      vertical-align: top;
    }

    .drug-row:hover td { background: rgba(47, 107, 92, 0.02); }
    .drug-row.is-expanded td {
      background: rgba(47, 107, 92, 0.03);
      border-bottom: none;
    }
    tbody tr:last-child td { border-bottom: none; }

    /* === Column styles === */
    .col-drug {
      font-family: var(--serif-display);
      font-weight: 500;
      color: var(--ink);
    }
    .drug-nzf {
      display: block;
      font-size: 1rem;
      margin-bottom: 3px;
    }
    .drug-brand {
      display: block;
      font-size: 0.82rem;
      color: var(--ink-mute);
      font-family: var(--serif-body);
      font-weight: 400;
    }
    .col-class {
      font-family: var(--mono);
      font-size: 0.72rem;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--ochre);
    }
    .col-indication {
      font-size: 0.9rem;
      color: var(--ink-soft);
    }
    .col-dose {
      font-family: var(--mono);
      font-size: 0.85rem;
      color: var(--ink-soft);
    }

    /* === Expand button === */
    .col-expand {
      width: 44px;
      padding: 14px 12px;
      text-align: center;
    }
    .expand-btn {
      width: 24px;
      height: 24px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: none;
      border: 1px solid var(--rule);
      border-radius: 3px;
      cursor: pointer;
      color: var(--ink-mute);
      font-family: var(--mono);
      font-size: 1rem;
      line-height: 1;
      transition: all 0.1s;
    }
    .expand-btn:hover {
      border-color: var(--green);
      color: var(--green);
    }
    .expand-btn.open {
      background: var(--green-deep);
      border-color: var(--green-deep);
      color: var(--paper);
    }

    /* === Detail row === */
    .detail-row { display: none; }
    .detail-row.open { display: table-row; }

    .detail-cell {
      padding: 0 20px 20px 20px;
      border-bottom: 1px solid var(--rule);
      background: rgba(47, 107, 92, 0.03);
    }

    .detail-inner {
      display: grid;
      grid-template-columns: 220px 1fr;
      gap: 0 32px;
      padding: 16px 0 4px;
      border-top: 1px dashed var(--rule);
    }

    .detail-col { display: flex; flex-direction: column; gap: 14px; }

    .detail-item {}
    .detail-label {
      display: block;
      font-family: var(--mono);
      font-size: 0.62rem;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--ochre);
      margin-bottom: 3px;
    }
    .detail-value {
      display: block;
      font-family: var(--serif-body);
      font-size: 0.9rem;
      color: var(--ink-soft);
      line-height: 1.45;
    }
    .detail-value.mono {
      font-family: var(--mono);
      font-size: 0.82rem;
    }

    /* === Pregnancy badges === */
    .badge-pregnancy {
      display: inline-block;
      padding: 4px 8px;
      background: var(--paper-warm);
      border: 1px solid var(--rule);
      border-radius: 3px;
      font-family: var(--mono);
      font-size: 0.78rem;
      font-weight: 500;
    }
    .badge-pregnancy.cat-a,
    .badge-pregnancy.cat-b {
      background: rgba(47, 107, 92, 0.1);
      border-color: var(--green);
      color: var(--green-deep);
    }
    .badge-pregnancy.cat-c {
      background: rgba(184, 113, 79, 0.1);
      border-color: var(--ochre);
      color: var(--ochre);
    }
    .badge-pregnancy.cat-d,
    .badge-pregnancy.cat-x {
      background: rgba(26, 31, 28, 0.1);
      border-color: var(--ink-soft);
      color: var(--ink);
    }

    /* === No results === */
    .no-results {
      text-align: center;
      padding: 48px 24px;
      color: var(--ink-mute);
      display: none;
    }
    .no-results p { font-size: 1.1rem; margin: 0; }

    /* === Footer === */
    .site-footer {
      margin-top: 64px;
      padding: 40px 0;
      border-top: 1px solid var(--rule);
      font-family: var(--mono);
      font-size: 0.75rem;
      letter-spacing: 0.5px;
      color: var(--ink-mute);
    }
    .site-footer .wrap { max-width: 1080px; margin: 0 auto; padding: 0 24px; }
    .site-footer p { margin: 0 0 6px; }
    .footer-meta { font-style: italic; }

    /* === Responsive === */
    @media (max-width: 768px) {
      .page-title { font-size: 2rem; }
      .filter-row { flex-direction: column; gap: 10px; }
      .filter-label { padding-top: 0; min-width: unset; }
      th, td { padding: 12px 8px; font-size: 0.85rem; }
      .detail-inner { grid-template-columns: 1fr; gap: 16px 0; }
    }

    @media print {
      .masthead, .filters, .chips-bar, .site-footer { display: none; }
      .page-header { border: none; padding: 0; margin: 0 0 24px; }
      table { font-size: 0.85rem; }
      td, th { padding: 8px; }
      .detail-row { display: table-row !important; }
      .expand-btn { display: none; }
    }
  </style>
</head>
<body>

  <header class="masthead">
    <div class="masthead-row">
      <a href="/" class="brand">
        <span>Working <em>Diagnosis</em>.</span>
      </a>
      <nav class="primary-nav" aria-label="Primary">
        <a href="/lifestyle-prevention/">Lifestyle</a>
        <a href="/msk/">MSK</a>
        <a href="/infectious-disease/">Travel</a>
        <a href="/mental-health/">Mental Health</a>
        <a href="/workshop/">Workshop</a>
      </nav>
    </div>
  </header>

  <main class="wrap">
    <div class="page-header">
      <h1 class="page-title">Psychotropic Drug Selector</h1>
      <p class="page-dek">Interactive reference for psychotropic agents. Filter by indication, drug class, and patient factors. Data: NZ formulations, dosing, costs, interactions, and pregnancy safety.</p>
    </div>

    <!-- Filters -->
    <div class="filters">
      <div class="filter-row">
        <div class="filter-label">Indication</div>
        <div class="filter-pills" id="indication-filter"></div>
      </div>
      <div class="filter-row">
        <div class="filter-label">Drug class</div>
        <div class="filter-pills" id="class-filter"></div>
      </div>
      <div class="filter-row">
        <div class="filter-label">Patient factor</div>
        <div class="filter-pills" id="factor-filter"></div>
      </div>
    </div>

    <!-- Active chips bar -->
    <div class="chips-bar" id="chips-bar">
      <span class="chips-label">Filtering by</span>
      <div class="chips-list" id="chips-list"></div>
      <button class="chips-clear" id="chips-clear">Clear all</button>
    </div>

    <!-- Results -->
    <div class="results-row">
      <div class="results-meta" id="results-meta"></div>
      <button class="expand-all-btn" id="expand-all-btn">Expand all</button>
    </div>

    <div class="table-wrapper" id="table-wrapper">
      <table id="drugs-table">
        <thead>
          <tr>
            <th>Drug</th>
            <th>Class</th>
            <th>Indication(s)</th>
            <th>Usual dose</th>
            <th>Pregnancy</th>
            <th class="th-expand"></th>
          </tr>
        </thead>
        <tbody id="drugs-tbody"></tbody>
      </table>
    </div>
    <div id="no-results-message" class="no-results">
      <p>No drugs match your filters. Try adjusting your selection.</p>
    </div>

  </main>

  <footer class="site-footer">
    <div class="wrap">
      <p><strong>Working Diagnosis</strong> &middot; Aotearoa New Zealand &middot; &copy; 2026</p>
      <p class="footer-meta">An internet workshop for general practice.</p>
      <p style="font-size: 0.7rem; margin-top: 12px; font-style: italic;">
        This tool is a clinician reference aid. All information should be verified against current NZF, UpToDate, and local guidelines before prescribing. Data current to May 2026; verify interactions and costs. Not for patient-facing use.
      </p>
    </div>
  </footer>

  <script>
    // === Drug database ===
    const drugs = [
      {
        id: 'sertraline',
        nzf: 'Sertraline',
        brand: 'Lustral, generics',
        class: 'SSRI',
        indications: ['depression', 'anxiety', 'ocd', 'ptsd', 'panic'],
        dose: '50-200 mg/day',
        onset: '2-4 weeks',
        halfLife: '26 hours',
        sideEffects: 'Sexual dysfunction, GI upset, insomnia, tremor, hyponatraemia',
        cyp450: 'Weak 2D6 inhibitor; substrate 3A4, 2B6',
        cost: '$5-8 (DHB) / $15-20 (private)',
        pregnancy: 'B3',
      },
      {
        id: 'citalopram',
        nzf: 'Citalopram',
        brand: 'Cipramil, generics',
        class: 'SSRI',
        indications: ['depression', 'anxiety'],
        dose: '20-40 mg/day',
        onset: '2-4 weeks',
        halfLife: '35 hours',
        sideEffects: 'Sexual dysfunction, GI upset, tremor, QT prolongation (high dose), hyponatraemia',
        cyp450: 'Weak 2D6 inhibitor; substrate 3A4, 2C19, 2B6',
        cost: '$4-7 (DHB) / $12-18 (private)',
        pregnancy: 'B3',
      },
      {
        id: 'fluoxetine',
        nzf: 'Fluoxetine',
        brand: 'Fluoxac, Prozac, generics',
        class: 'SSRI',
        indications: ['depression', 'anxiety', 'ocd', 'bulimia'],
        dose: '20-60 mg/day',
        onset: '3-5 weeks',
        halfLife: '4-6 days (active metabolite 7-15 days)',
        sideEffects: 'Activation, insomnia, sexual dysfunction, GI upset, hyponatraemia',
        cyp450: 'Strong 2D6 inhibitor; substrate 2D6, 3A4, 2B6, 2C9, 2C19',
        cost: '$4-7 (DHB) / $12-18 (private)',
        pregnancy: 'B3',
      },
      {
        id: 'paroxetine',
        nzf: 'Paroxetine',
        brand: 'Aropax, generics',
        class: 'SSRI',
        indications: ['depression', 'anxiety', 'ocd', 'panic', 'ptsd'],
        dose: '20-50 mg/day',
        onset: '2-4 weeks',
        halfLife: '21 hours',
        sideEffects: 'Sexual dysfunction, weight gain, sedation, anticholinergic effects, discontinuation syndrome',
        cyp450: 'Strong 2D6 inhibitor; substrate 2D6, 3A4',
        cost: '$5-9 (DHB) / $15-22 (private)',
        pregnancy: 'B3; increased risk of cardiac defects and neonatal withdrawal',
      },
      {
        id: 'escitalopram',
        nzf: 'Escitalopram',
        brand: 'Lexapro, generics',
        class: 'SSRI',
        indications: ['depression', 'anxiety'],
        dose: '10-20 mg/day',
        onset: '2-4 weeks',
        halfLife: '27-32 hours',
        sideEffects: 'Sexual dysfunction, GI upset, tremor, QT prolongation (high dose), hyponatraemia',
        cyp450: 'Weak 2D6 inhibitor; substrate 2C19, 3A4, 2D6',
        cost: '$6-10 (DHB) / $16-24 (private)',
        pregnancy: 'B3',
      },
      {
        id: 'venlafaxine',
        nzf: 'Venlafaxine',
        brand: 'Efexor, Efexor XR, generics',
        class: 'SNRI',
        indications: ['depression', 'anxiety', 'hot flushes'],
        dose: '75-375 mg/day (XR preferred)',
        onset: '2-4 weeks',
        halfLife: '5 hours (active metabolites 11-13 hours)',
        sideEffects: 'Hypertension, sexual dysfunction, GI upset, hyponatraemia, discontinuation syndrome, activation',
        cyp450: 'Substrate 2D6, 3A4; minor 2C9 inhibition',
        cost: '$6-12 (DHB) / $18-28 (private)',
        pregnancy: 'B3; monitor for withdrawal and hypertension',
      },
      {
        id: 'duloxetine',
        nzf: 'Duloxetine',
        brand: 'Cymbalta, generics',
        class: 'SNRI',
        indications: ['depression', 'anxiety', 'neuropathic pain'],
        dose: '60-120 mg/day',
        onset: '2-4 weeks',
        halfLife: '12 hours',
        sideEffects: 'Nausea, sexual dysfunction, hyponatraemia, hypertension, sedation',
        cyp450: 'Strong 1A2 inhibitor; substrate 1A2, 2D6',
        cost: '$8-14 (DHB) / $20-32 (private)',
        pregnancy: 'B3',
      },
      {
        id: 'mirtazapine',
        nzf: 'Mirtazapine',
        brand: 'Remeron, Aremis, generics',
        class: 'Tetracyclic',
        indications: ['depression', 'insomnia'],
        dose: '15-45 mg/day (often nocte)',
        onset: '2-4 weeks',
        halfLife: '20-40 hours',
        sideEffects: 'Weight gain, sedation, increased appetite, agranulocytosis (rare), metabolic effects',
        cyp450: 'Substrate 1A2, 2D6, 3A4; weak inhibitor',
        cost: '$4-8 (DHB) / $12-20 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'tricyclic-amitriptyline',
        nzf: 'Amitriptyline',
        brand: 'Elavil, generics',
        class: 'TCA',
        indications: ['depression', 'neuropathic pain', 'insomnia'],
        dose: '25-150 mg/day (often nocte)',
        onset: '2-4 weeks',
        halfLife: '31-46 hours',
        sideEffects: 'Anticholinergic (dry mouth, constipation, urinary retention), sedation, weight gain, cardiac conduction effects',
        cyp450: 'Substrate 2D6, 3A4, 1A2, 2C9; weak 2D6 inhibitor',
        cost: '$3-5 (DHB) / $8-12 (private)',
        pregnancy: 'B2; larger studies, generally safe but withdraw at term',
      },
      {
        id: 'tricyclic-nortriptyline',
        nzf: 'Nortriptyline',
        brand: 'Allegron, generics',
        class: 'TCA',
        indications: ['depression', 'neuropathic pain'],
        dose: '50-150 mg/day (nocte)',
        onset: '2-4 weeks',
        halfLife: '28-31 hours',
        sideEffects: 'Anticholinergic, sedation, cardiac conduction effects, orthostatic hypotension',
        cyp450: 'Substrate 2D6, 3A4, 1A2; modest 2D6 inhibitor',
        cost: '$3-6 (DHB) / $9-14 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'bupropion',
        nzf: 'Bupropion',
        brand: 'Wellbutrin, Aplenzin, generics',
        class: 'NDRI',
        indications: ['depression', 'smoking cessation', 'fatigue'],
        dose: '300-450 mg/day (XL)',
        onset: '3-5 weeks',
        halfLife: '21 hours',
        sideEffects: 'Insomnia, activation, dry mouth, seizure risk (high dose/risk factors), weight loss',
        cyp450: 'Strong 2D6 inhibitor; substrate 2B6, 2D6',
        cost: '$8-15 (DHB) / $22-35 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'quetiapine',
        nzf: 'Quetiapine',
        brand: 'Seroquel, generics',
        class: 'Antipsychotic (atypical)',
        indications: ['bipolar depression', 'psychosis', 'insomnia', 'anxiety (adjunct)'],
        dose: '50-800 mg/day (dose-dependent indication)',
        onset: '3-7 days (antipsychotic), 2-4 weeks (mood)',
        halfLife: '6 hours',
        sideEffects: 'Sedation, weight gain, metabolic effects, orthostatic hypotension, anticholinergic',
        cyp450: 'Substrate 3A4, 2D6; minimal inhibition',
        cost: '$6-12 (DHB) / $18-28 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'olanzapine',
        nzf: 'Olanzapine',
        brand: 'Zyprexa, Zyprexa Velotab, generics',
        class: 'Antipsychotic (atypical)',
        indications: ['bipolar mania', 'psychosis', 'bipolar maintenance'],
        dose: '5-20 mg/day',
        onset: '1-2 weeks (mania), 2-4 weeks (psychosis)',
        halfLife: '21-54 hours',
        sideEffects: 'Weight gain, metabolic syndrome, sedation, agranulocytosis (rare), anticholinergic',
        cyp450: 'Substrate 1A2, 2D6; minimal inhibition',
        cost: '$7-14 (DHB) / $20-32 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'risperidone',
        nzf: 'Risperidone',
        brand: 'Risperdal, Risperdal Consta (IM), generics',
        class: 'Antipsychotic (atypical)',
        indications: ['psychosis', 'bipolar mania', 'bipolar maintenance'],
        dose: '2-8 mg/day',
        onset: '1-2 weeks (mania), 2-4 weeks (psychosis)',
        halfLife: '3 hours (active metabolite 21 hours)',
        sideEffects: 'Extrapyramidal symptoms (dose-dependent), weight gain, prolactin elevation, metabolic effects, orthostatic hypotension',
        cyp450: 'Substrate 2D6, 3A4; minimal inhibition',
        cost: '$5-10 (DHB) / $15-25 (private)',
        pregnancy: 'B2; monitor for extrapyramidal effects in neonate',
      },
      {
        id: 'aripiprazole',
        nzf: 'Aripiprazole',
        brand: 'Abilify, Abilify Maintena (IM), generics',
        class: 'Antipsychotic (atypical)',
        indications: ['psychosis', 'bipolar mania', 'bipolar maintenance', 'depression (adjunct)'],
        dose: '10-30 mg/day',
        onset: '1-2 weeks (mania), 2-4 weeks (psychosis)',
        halfLife: '75 hours',
        sideEffects: 'Akathisia, insomnia, nausea, less weight gain than other atypicals, paradoxical anxiety',
        cyp450: 'Substrate 2D6, 3A4; minimal inhibition',
        cost: '$8-15 (DHB) / $24-36 (private)',
        pregnancy: 'B2',
      },
      {
        id: 'lithium',
        nzf: 'Lithium carbonate',
        brand: 'Lithicarb, Quilonum, generics',
        class: 'Mood stabiliser',
        indications: ['bipolar maintenance', 'bipolar mania (adjunct)', 'depression (augmentation)'],
        dose: '400-1200 mg/day (therapeutic level 0.6-1.0 mmol/L)',
        onset: '5-7 days (mania), 2-3 weeks (maintenance)',
        halfLife: '18-36 hours',
        sideEffects: 'Tremor, polyuria/polydipsia, weight gain, thyroid dysfunction, renal impairment, narrow therapeutic index',
        cyp450: 'Not metabolised; renal clearance',
        cost: '$2-4 (DHB) / $6-10 (private)',
        pregnancy: 'D; risk of Ebstein anomaly (1:2000 vs 1:20,000); requires careful risk-benefit and fetal imaging',
      },
      {
        id: 'valproate',
        nzf: 'Sodium valproate / Divalproex',
        brand: 'Epilim, Depakote, generics',
        class: 'Mood stabiliser',
        indications: ['bipolar mania', 'bipolar maintenance'],
        dose: '1000-2000 mg/day (level 50-100 mg/L)',
        onset: '3-7 days (mania)',
        halfLife: '9-18 hours',
        sideEffects: 'GI upset, weight gain, tremor, alopecia, hepatotoxicity (rare), pancreatitis, teratogenicity',
        cyp450: 'Inhibits 2C9, 2C19; substrate 2C9',
        cost: '$3-6 (DHB) / $10-18 (private)',
        pregnancy: 'X; high teratogenic risk (neural tube defects, developmental delay); contraindicated',
      },
      {
        id: 'lamotrigine',
        nzf: 'Lamotrigine',
        brand: 'Lamictal, generics',
        class: 'Mood stabiliser',
        indications: ['bipolar depression', 'bipolar maintenance'],
        dose: '100-300 mg/day (slow titration required)',
        onset: '2-4 weeks (depression), slower for mania',
        halfLife: '24-35 hours',
        sideEffects: 'Rash (Stevens-Johnson syndrome / TEN rare but serious), diplopia, tremor, GI upset, slow titration needed',
        cyp450: 'Substrate 2C19, UGT; minimal inhibition',
        cost: '$8-14 (DHB) / $22-32 (private)',
        pregnancy: 'B2; consider folic acid supplement',
      },
      {
        id: 'diazepam',
        nzf: 'Diazepam',
        brand: 'Valium, generics',
        class: 'Benzodiazepine',
        indications: ['acute anxiety', 'acute insomnia', 'acute agitation', 'alcohol withdrawal'],
        dose: '2-20 mg/day (divided)',
        onset: '15-45 min (PO); 1-5 min (IV)',
        halfLife: '20-70 hours (active metabolites longer)',
        sideEffects: 'Sedation, dependence, tolerance, cognitive impairment, respiratory depression (esp. IV), ataxia',
        cyp450: 'Substrate 2C19, 3A4; minimal inhibition',
        cost: '$2-4 (DHB) / $6-10 (private)',
        pregnancy: 'D; first trimester: cleft palate risk; third trimester: neonatal withdrawal',
      },
      {
        id: 'lorazepam',
        nzf: 'Lorazepam',
        brand: 'Ativan, generics',
        class: 'Benzodiazepine',
        indications: ['acute anxiety', 'acute insomnia', 'acute agitation', 'acute psychosis (adjunct)', 'seizures'],
        dose: '1-4 mg/day (divided)',
        onset: '15-30 min (PO); 1-3 min (IV)',
        halfLife: '10-20 hours',
        sideEffects: 'Sedation, dependence, tolerance, cognitive impairment, respiratory depression',
        cyp450: 'Not hepatically metabolised; glucuronidated (safe in hepatic impairment)',
        cost: '$3-6 (DHB) / $10-16 (private)',
        pregnancy: 'D; first trimester: cleft palate risk; third trimester: neonatal withdrawal',
      },
      {
        id: 'zopiclone',
        nzf: 'Zopiclone',
        brand: 'Imovane, generics',
        class: 'Z-drug (hypnotic)',
        indications: ['insomnia (short-term)'],
        dose: '5-7.5 mg nocte',
        onset: '15-30 min',
        halfLife: '5-6 hours',
        sideEffects: 'Metallic taste, next-morning sedation, dependence (short-term use), headache, complex sleep behaviours',
        cyp450: 'Substrate 3A4, 2C19; minimal inhibition',
        cost: '$4-7 (DHB) / $12-18 (private)',
        pregnancy: 'B2; avoid regular use; single dose may be acceptable for acute insomnia',
      },
    ];

    // === Filter options ===
    const indications = [...new Set(drugs.flatMap(d => d.indications))].sort();
    const classes     = [...new Set(drugs.map(d => d.class))].sort();
    const factors     = [
      'pregnancy-risk', 'renal-impairment', 'hepatic-impairment',
      'elderly', 'cyp-interactions', 'weight-neutral', 'anticholinergic-risk'
    ];
    const factorLabels = {
      'pregnancy-risk':       'Pregnancy (lower risk)',
      'renal-impairment':     'Renal impairment',
      'hepatic-impairment':   'Hepatic impairment',
      'elderly':              'Elderly / polypharmacy',
      'cyp-interactions':     'Minimal CYP interactions',
      'weight-neutral':       'Weight-neutral',
      'anticholinergic-risk': 'Lower anticholinergic burden',
    };

    // === State ===
    const activeFilters = { indication: new Set(), class: new Set(), factor: new Set() };
    const expandedRows  = new Set();
    let allExpanded     = false;

    // === Build filter pills ===
    function makePill(value, type, label) {
      const btn = document.createElement('button');
      btn.className = 'filter-pill';
      btn.textContent = label;
      btn.dataset.value = value;
      btn.dataset.type  = type;
      btn.addEventListener('click', () => toggleFilter(type, value, btn));
      return btn;
    }

    function buildFilters() {
      const indCont = document.getElementById('indication-filter');
      indications.forEach(ind =>
        indCont.appendChild(makePill(ind, 'indication', ind.charAt(0).toUpperCase() + ind.slice(1)))
      );

      const clsCont = document.getElementById('class-filter');
      classes.forEach(cls => clsCont.appendChild(makePill(cls, 'class', cls)));

      const facCont = document.getElementById('factor-filter');
      factors.forEach(fac => facCont.appendChild(makePill(fac, 'factor', factorLabels[fac])));
    }

    function toggleFilter(type, value, btn) {
      if (activeFilters[type].has(value)) {
        activeFilters[type].delete(value);
        btn.classList.remove('active');
      } else {
        activeFilters[type].add(value);
        btn.classList.add('active');
      }
      update();
    }

    function clearAll() {
      activeFilters.indication.clear();
      activeFilters.class.clear();
      activeFilters.factor.clear();
      document.querySelectorAll('.filter-pill.active').forEach(p => p.classList.remove('active'));
      update();
    }

    // === Active chips ===
    function renderChips() {
      const bar  = document.getElementById('chips-bar');
      const list = document.getElementById('chips-list');
      list.innerHTML = '';

      const total = activeFilters.indication.size + activeFilters.class.size + activeFilters.factor.size;
      if (total === 0) { bar.classList.remove('visible'); return; }
      bar.classList.add('visible');

      [
        ...Array.from(activeFilters.indication).map(v => ({ type: 'indication', value: v, label: v.charAt(0).toUpperCase() + v.slice(1) })),
        ...Array.from(activeFilters.class).map(v => ({ type: 'class', value: v, label: v })),
        ...Array.from(activeFilters.factor).map(v => ({ type: 'factor', value: v, label: factorLabels[v] })),
      ].forEach(({ type, value, label }) => {
        const chip = document.createElement('span');
        chip.className = 'active-chip';
        chip.innerHTML = `${label} <button class="chip-remove" data-type="${type}" data-value="${value}" title="Remove">&times;</button>`;
        chip.querySelector('.chip-remove').addEventListener('click', e => {
          e.stopPropagation();
          removeFilter(type, value);
        });
        list.appendChild(chip);
      });
    }

    function removeFilter(type, value) {
      activeFilters[type].delete(value);
      const pill = document.querySelector(`.filter-pill[data-type="${type}"][data-value="${value}"]`);
      if (pill) pill.classList.remove('active');
      update();
    }

    // === Drug filtering ===
    function getDrugFactors(drug) {
      const f = [];
      if (['B2', 'B3'].includes(drug.pregnancy))              f.push('pregnancy-risk');
      if (!drug.sideEffects.toLowerCase().includes('weight')) f.push('weight-neutral');
      if (!drug.sideEffects.toLowerCase().includes('anticholinergic')) f.push('anticholinergic-risk');
      if (!drug.cyp450.toLowerCase().includes('inhibitor'))   f.push('cyp-interactions');
      if (!drug.class.includes('TCA') && !drug.class.includes('Antipsychotic')) f.push('renal-impairment', 'hepatic-impairment');
      if (!drug.class.includes('Antipsychotic') && !drug.class.includes('Benzodiazepine')) f.push('elderly');
      return f;
    }

    function getFiltered() {
      return drugs.filter(drug => {
        const indOk = activeFilters.indication.size === 0 || [...activeFilters.indication].some(i => drug.indications.includes(i));
        const clsOk = activeFilters.class.size     === 0 || activeFilters.class.has(drug.class);
        const facOk = activeFilters.factor.size    === 0 || [...activeFilters.factor].every(f => getDrugFactors(drug).includes(f));
        return indOk && clsOk && facOk;
      });
    }

    // === Render table ===
    function renderTable(filtered) {
      const tbody      = document.getElementById('drugs-tbody');
      const metaEl     = document.getElementById('results-meta');
      const noResults  = document.getElementById('no-results-message');
      const tableWrap  = document.getElementById('table-wrapper');

      tbody.innerHTML = '';

      if (filtered.length === 0) {
        noResults.style.display = 'block';
        tableWrap.style.display  = 'none';
        metaEl.textContent = '';
        return;
      }

      noResults.style.display = 'none';
      tableWrap.style.display  = '';
      metaEl.textContent = `${filtered.length} drug${filtered.length !== 1 ? 's' : ''} shown`;

      filtered.forEach(drug => {
        const pregClass  = drug.pregnancy.charAt(0).toLowerCase();
        const isOpen     = expandedRows.has(drug.id);

        // Main row
        const row = document.createElement('tr');
        row.className = 'drug-row' + (isOpen ? ' is-expanded' : '');
        row.dataset.id = drug.id;
        row.innerHTML = `
          <td class="col-drug">
            <span class="drug-nzf">${drug.nzf}</span>
            <span class="drug-brand">${drug.brand}</span>
          </td>
          <td class="col-class">${drug.class}</td>
          <td class="col-indication">${drug.indications.map(i => i.charAt(0).toUpperCase() + i.slice(1)).join(', ')}</td>
          <td class="col-dose">${drug.dose}</td>
          <td><span class="badge-pregnancy cat-${pregClass}">${drug.pregnancy}</span></td>
          <td class="col-expand">
            <button class="expand-btn${isOpen ? ' open' : ''}" data-id="${drug.id}" aria-label="Show details" aria-expanded="${isOpen}">${isOpen ? '&#8722;' : '+'}</button>
          </td>
        `;

        // Detail row
        const detailRow = document.createElement('tr');
        detailRow.className = 'detail-row' + (isOpen ? ' open' : '');
        detailRow.id = `detail-${drug.id}`;
        detailRow.innerHTML = `
          <td class="detail-cell" colspan="6">
            <div class="detail-inner">
              <div class="detail-col">
                <div class="detail-item">
                  <span class="detail-label">Onset</span>
                  <span class="detail-value mono">${drug.onset}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">Half-life</span>
                  <span class="detail-value mono">${drug.halfLife}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">NZ cost</span>
                  <span class="detail-value mono">${drug.cost}</span>
                </div>
              </div>
              <div class="detail-col">
                <div class="detail-item">
                  <span class="detail-label">Main side effects</span>
                  <span class="detail-value">${drug.sideEffects}</span>
                </div>
                <div class="detail-item">
                  <span class="detail-label">CYP450</span>
                  <span class="detail-value mono">${drug.cyp450}</span>
                </div>
              </div>
            </div>
          </td>
        `;

        tbody.appendChild(row);
        tbody.appendChild(detailRow);
      });
    }

    // === Expand / collapse ===
    function toggleRow(id) {
      const btn       = document.querySelector(`.expand-btn[data-id="${id}"]`);
      const detailRow = document.getElementById(`detail-${id}`);
      const mainRow   = document.querySelector(`.drug-row[data-id="${id}"]`);
      if (!btn || !detailRow) return;

      if (expandedRows.has(id)) {
        expandedRows.delete(id);
        btn.classList.remove('open');
        btn.innerHTML = '+';
        btn.setAttribute('aria-expanded', 'false');
        detailRow.classList.remove('open');
        mainRow.classList.remove('is-expanded');
      } else {
        expandedRows.add(id);
        btn.classList.add('open');
        btn.innerHTML = '&#8722;';
        btn.setAttribute('aria-expanded', 'true');
        detailRow.classList.add('open');
        mainRow.classList.add('is-expanded');
      }
    }

    function toggleExpandAll() {
      const filtered = getFiltered();
      allExpanded = !allExpanded;
      document.getElementById('expand-all-btn').textContent = allExpanded ? 'Collapse all' : 'Expand all';
      filtered.forEach(d => { if (allExpanded) expandedRows.add(d.id); else expandedRows.delete(d.id); });
      renderTable(filtered);
    }

    // === Main update ===
    function update() {
      const filtered = getFiltered();
      allExpanded = false;
      document.getElementById('expand-all-btn').textContent = 'Expand all';
      renderTable(filtered);
      renderChips();
    }

    // === Event delegation ===
    document.getElementById('drugs-tbody').addEventListener('click', e => {
      const btn = e.target.closest('.expand-btn');
      if (btn) toggleRow(btn.dataset.id);
    });
    document.getElementById('chips-clear').addEventListener('click', clearAll);
    document.getElementById('expand-all-btn').addEventListener('click', toggleExpandAll);

    // === Init ===
    buildFilters();
    update();
  </script>

</body>
</html>
