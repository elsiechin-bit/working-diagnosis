---
title: CHA₂DS₂-VASc Stroke Risk
layout: base
permalink: /workshop/tools/cha2ds2-vasc/
eleventyExcludeFromCollections: true
description: Stroke risk stratification in AF with NZ-specific anticoagulation scaffold
---

<style>
  /* ─── Form structure ───────────────────────────── */
  .form-section {
    margin-bottom: 32px;
  }

  .form-section-title {
    font-family: var(--serif-display);
    font-weight: 500;
    font-size: 20px;
    margin: 32px 0 18px;
    color: var(--ink);
    border-top: 1px solid var(--rule);
    padding-top: 24px;
  }
  
  .calc-container .form-section:first-of-type .form-section-title {
    border-top: none;
    padding-top: 0;
    margin-top: 0;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: flex;
    align-items: center;
    cursor: pointer;
    gap: 12px;
    padding: 12px;
    margin: 0 -12px;
    border-radius: 4px;
    transition: background 120ms ease;
  }

  .form-group label:hover {
    background: rgba(47, 107, 92, 0.05);
  }

  .form-group input[type="checkbox"],
  .form-group input[type="radio"] {
    width: 20px;
    height: 20px;
    cursor: pointer;
    accent-color: var(--green-deep);
  }

  .form-group input[type="number"] {
    font-family: var(--mono);
    font-size: 16px;
    padding: 8px 12px;
    border: 1px solid var(--rule);
    border-radius: 4px;
    width: 80px;
    color: var(--ink);
  }

  .form-group input[type="number"]:focus {
    outline: none;
    border-color: var(--green-deep);
    background: rgba(31, 74, 63, 0.02);
  }

  .form-label-text {
    flex: 1;
  }

  .form-label-text strong {
    display: block;
    font-weight: 500;
    margin-bottom: 3px;
  }

  .form-label-text small {
    display: block;
    font-size: 13px;
    color: var(--ink-mute);
    font-style: italic;
  }

  /* ─── Result box ───────────────────────────────── */
  .result-section {
    background: var(--paper-warm);
    border: 2px solid var(--rule);
    border-radius: 6px;
    padding: 32px;
    margin: 40px 0;
    display: none;
  }

  .result-section.active {
    display: block;
    animation: slideDown 300ms ease;
  }

  @keyframes slideDown {
    from {
      opacity: 0;
      transform: translateY(-12px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  .result-score {
    text-align: center;
    margin-bottom: 28px;
  }

  .score-label {
    font-family: var(--mono);
    font-size: 0.75rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--ochre);
    margin-bottom: 8px;
  }

  .score-number {
    font-family: var(--serif-display);
    font-weight: 600;
    font-size: 64px;
    line-height: 1;
    color: var(--ink);
    margin-bottom: 8px;
  }

  .score-max {
    font-family: var(--mono);
    font-size: 14px;
    color: var(--ink-mute);
  }

  .risk-category {
    padding: 16px;
    border-radius: 4px;
    margin-bottom: 20px;
    font-weight: 500;
  }

  .risk-low {
    background: rgba(47, 107, 92, 0.1);
    color: var(--green-deep);
    border-left: 4px solid var(--green-deep);
  }

  .risk-moderate {
    background: rgba(184, 113, 79, 0.1);
    color: var(--ochre);
    border-left: 4px solid var(--ochre);
  }

  .risk-high {
    background: rgba(58, 69, 64, 0.1);
    color: var(--ink-soft);
    border-left: 4px solid var(--ink-soft);
  }

  /* ─── Anticoagulation scaffold ─────────────────── */
  .anticoag-scaffold {
    background: #FFF8F0;
    border: 1px solid var(--ochre);
    border-radius: 6px;
    padding: 20px;
    margin: 24px 0;
    font-size: 16px;
    line-height: 1.6;
  }

  .anticoag-scaffold strong {
    color: var(--ochre);
    font-weight: 600;
  }

  .anticoag-scaffold p {
    margin: 0 0 12px;
  }

  .anticoag-scaffold p:last-child {
    margin-bottom: 0;
  }

  .anticoag-list {
    list-style: none;
    padding: 0;
    margin: 12px 0;
  }

  .anticoag-list li {
    padding: 6px 0;
    padding-left: 20px;
    position: relative;
  }

  .anticoag-list li::before {
    content: "→";
    position: absolute;
    left: 0;
    color: var(--ochre);
    font-weight: 600;
  }

  /* ─── Expandable sections ──────────────────────── */
  .collapsible {
    margin-top: 32px;
    border-top: 1px solid var(--rule);
    padding-top: 24px;
  }

  .collapsible-toggle {
    display: flex;
    align-items: center;
    justify-content: space-between;
    cursor: pointer;
    background: none;
    border: none;
    padding: 0;
    width: 100%;
    font-family: var(--serif-display);
    font-size: 18px;
    font-weight: 500;
    color: var(--ink);
    transition: color 120ms ease;
  }

  .collapsible-toggle:hover {
    color: var(--green-deep);
  }

  .collapsible-toggle::after {
    content: "�-�";
    display: inline-block;
    font-size: 12px;
    transition: transform 200ms ease;
    color: var(--ochre);
  }

  .collapsible-toggle.active::after {
    transform: rotate(90deg);
  }

  .collapsible-content {
    display: none;
    margin-top: 16px;
    padding-top: 16px;
  }

  .collapsible-content.active {
    display: block;
  }

  /* ─── Evidence & practice pearls ────────────────── */
  .evidence-item {
    margin-bottom: 24px;
  }

  .evidence-item h4 {
    font-family: var(--serif-display);
    font-weight: 500;
    font-size: 16px;
    margin: 0 0 8px;
    color: var(--ink);
  }

  .evidence-item p {
    margin: 0 0 8px;
    font-size: 16px;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  .evidence-citation {
    font-family: var(--mono);
    font-size: 12px;
    color: var(--ink-mute);
    margin: 8px 0 0;
    padding-left: 12px;
    border-left: 2px solid var(--ochre);
  }

  .pearl {
    background: rgba(47, 107, 92, 0.05);
    border-left: 4px solid var(--green);
    padding: 16px;
    margin: 16px 0;
    border-radius: 4px;
  }

  .pearl strong {
    display: block;
    color: var(--green-deep);
    margin-bottom: 6px;
    font-size: 15px;
  }

  .pearl p {
    margin: 0;
    font-size: 15px;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  .calc-container {
    max-width: 700px;
  }

  @media (max-width: 600px) {
    .score-number { font-size: 48px; }
    .result-section { padding: 24px; }
  }
</style>

<div class="calc-container" style="max-width: 700px; margin: 0 auto;">

<div style="margin-bottom: 48px; padding-bottom: 32px; border-bottom: 1px solid var(--rule);">
<div style="font-family: var(--mono); font-size: 0.72rem; letter-spacing: 3px; text-transform: uppercase; color: var(--ochre); margin: 0 0 14px;">GP Tools</div>
<h1 style="font-family: var(--serif-display); font-weight: 500; font-size: clamp(32px, 5vw, 48px); line-height: 1.1; letter-spacing: -0.025em; margin: 0 0 16px;">CHA₂DS₂-VASc<br>Stroke Risk</h1>
<p style="font-size: 1.1rem; color: var(--ink-soft); margin: 0; line-height: 1.5;">Estimate annual stroke risk in atrial fibrillation and scaffold anticoagulation decision-making.</p>
</div>

<form id="cha2ds2Form">

  <!-- C: Congestive heart failure -->
  <div class="form-section">
    <div class="form-section-title">C  -  Cardiac</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="chf" name="chf" value="1">
        <div class="form-label-text">
          <strong>Congestive heart failure</strong>
          <small>Or LVEF ≤40%</small>
        </div>
      </label>
    </div>
  </div>

  <!-- H: Hypertension -->
  <div class="form-section">
    <div class="form-section-title">H  -  Hypertension</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="htn" name="htn" value="1">
        <div class="form-label-text">
          <strong>Hypertension</strong>
          <small>On treatment or SBP >140 mmHg</small>
        </div>
      </label>
    </div>
  </div>

  <!-- A₂: Age -->
  <div class="form-section">
    <div class="form-section-title">A₂  -  Age</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="age75" name="age75" value="2">
        <div class="form-label-text">
          <strong>Age ≥75 years</strong>
          <small>2 points</small>
        </div>
      </label>
    </div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="age65to74" name="age65to74" value="1">
        <div class="form-label-text">
          <strong>Age 65-74 years</strong>
          <small>1 point</small>
        </div>
      </label>
    </div>
    <div class="form-group" style="margin-bottom: 0;">
      <label>
        <input type="radio" name="ageNote" value="note" style="visibility: hidden; position: absolute;">
        <div class="form-label-text">
          <small style="color: var(--ink-mute); font-style: normal; display: block; margin-top: 8px;">Both age categories are mutually exclusive  -  select only one.</small>
        </div>
      </label>
    </div>
  </div>

  <!-- D: Diabetes -->
  <div class="form-section">
    <div class="form-section-title">D  -  Diabetes</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="dm" name="dm" value="1">
        <div class="form-label-text">
          <strong>Diabetes mellitus</strong>
          <small>On medication or fasting glucose >126 mg/dL</small>
        </div>
      </label>
    </div>
  </div>

  <!-- S₂: Stroke / TIA / thromboembolism -->
  <div class="form-section">
    <div class="form-section-title">S₂  -  Stroke History</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="stroke2" name="stroke2" value="2">
        <div class="form-label-text">
          <strong>Prior stroke, TIA, or thromboembolism</strong>
          <small>2 points</small>
        </div>
      </label>
    </div>
  </div>

  <!-- VA: Vascular disease & Age (65-74) -->
  <div class="form-section">
    <div class="form-section-title">VA  -  Vascular & Age</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="vascular" name="vascular" value="1">
        <div class="form-label-text">
          <strong>Vascular disease</strong>
          <small>Prior MI, peripheral artery disease, or aortic plaque</small>
        </div>
      </label>
    </div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="age65" name="age65" value="1">
        <div class="form-label-text">
          <strong>Age 65-74 years</strong>
          <small>Alternative to age category above</small>
        </div>
      </label>
    </div>
  </div>

  <!-- Sc: Sex category (female) -->
  <div class="form-section">
    <div class="form-section-title">Sc  -  Sex Category</div>
    <div class="form-group">
      <label>
        <input type="checkbox" id="female" name="female" value="1">
        <div class="form-label-text">
          <strong>Female sex</strong>
          <small>Biological sex, not gender identity</small>
        </div>
      </label>
    </div>
  </div>

  <button type="submit" style="display: none;"></button>
</form>

<!-- Result display -->
<div class="result-section" id="resultSection">
  <div class="result-score">
    <div class="score-label">CHA₂DS₂-VASc Score</div>
    <div class="score-number" id="scoreDisplay">0</div>
    <div class="score-max">out of 9</div>
  </div>

  <div id="riskCategory"></div>

  <!-- Annual stroke risk table -->
  <div style="margin: 24px 0; padding: 16px; background: rgba(26, 31, 28, 0.03); border-radius: 4px;">
    <div style="font-family: var(--mono); font-size: 11px; letter-spacing: 1px; text-transform: uppercase; color: var(--ink-mute); margin-bottom: 12px;">Annual Stroke Risk</div>
    <div style="font-size: 16px; color: var(--ink); margin-bottom: 4px;"><strong id="annualRisk"> - </strong></div>
    <div style="font-size: 13px; color: var(--ink-mute); line-height: 1.5;">Based on large randomised trials (ARISTOTLE, ROCKET-AF, RE-LY, ENGAGE)</div>
  </div>

  <!-- Anticoagulation scaffold -->
  <div class="anticoag-scaffold">
    <strong>Anticoagulation decision scaffold:</strong>
    <div id="anticoagRecommendation"></div>
  </div>

  <!-- HAS-BLED prompt -->
  <div style="background: rgba(184, 113, 79, 0.05); border: 1px solid var(--ochre); border-radius: 4px; padding: 16px; margin-top: 20px;">
    <div style="font-family: var(--mono); font-size: 12px; letter-spacing: 1px; text-transform: uppercase; color: var(--ochre); margin-bottom: 8px;">Next step</div>
    <p style="margin: 0; font-size: 16px; color: var(--ink-soft);">If anticoagulation is being considered, assess <strong>bleeding risk with HAS-BLED</strong> (hypertension, abnormal renal/liver, stroke, bleeding, labile INR, elderly, drugs/alcohol). A HAS-BLED score ≥3 warrants further discussion but does not contraindicate anticoagulation.</p>
  </div>
</div>

<!-- Evidence & practice pearls sections -->
<div class="collapsible">
  <button class="collapsible-toggle" onclick="toggleCollapsible(event, 'evidence')">Evidence & Trial Data</button>
  <div class="collapsible-content" id="evidence">

    <div class="evidence-item">
      <h4>Score validation and prognostic accuracy</h4>
      <p>The CHA₂DS₂-VASc score was derived from large European cohorts (16,622 patients with AF across 29 studies) and validates the original CHA₂DS₂ scheme by stratifying intermediate-risk patients. It discriminates stroke risk across all age groups and has superior performance in younger patients (age <65) where it identifies truly low-risk individuals (annual stroke risk <1% without anticoagulation).</p>
      <div class="evidence-citation">Lip GYH, et al. Chest. 2010;137(2):263-272.</div>
    </div>

    <div class="evidence-item">
      <h4>ARISTOTLE (apixaban in AF)</h4>
      <p>Landmark trial (18,201 patients) showing apixaban superior to warfarin for stroke prevention in AF, with lower major bleeding and all-cause mortality. Baseline median CHA₂DS₂-VASc was 3.5; anticoagulation reduced stroke by 21% relative risk.</p>
      <div class="evidence-citation">Granger CB, et al. N Engl J Med. 2011;365(11):981-992.</div>
    </div>

    <div class="evidence-item">
      <h4>ROCKET-AF (rivaroxaban in AF)</h4>
      <p>Large trial (14,264 patients, median CHA₂DS₂-VASc 3.48) demonstrating rivaroxaban non-inferiority to warfarin for stroke/thromboembolism. In subgroup analysis, absolute stroke risk reduction was greater in higher-risk patients (CHA₂DS₂-VASc ≥4).</p>
      <div class="evidence-citation">Patel MR, et al. N Engl J Med. 2011;365(10):883-891.</div>
    </div>

    <div class="evidence-item">
      <h4>RE-LY (dabigatran in AF)</h4>
      <p>Trial of 18,113 patients showing dabigatran 110 mg BID superior to warfarin for major bleeding, and 150 mg BID non-inferior for stroke prevention. Demonstrates that DOAC efficacy is consistent across CHA₂DS₂-VASc risk strata.</p>
      <div class="evidence-citation">Connolly SJ, et al. N Engl J Med. 2009;361(12):1139-1151.</div>
    </div>

    <div class="evidence-item">
      <h4>ENGAGE AF-TIMI 48 (edoxaban in AF)</h4>
      <p>Trial of 21,105 patients with AF. Edoxaban 60 mg OD was non-inferior to warfarin for stroke/systemic embolism and superior for major bleeding. Showed consistent benefit across CHA₂DS₂-VASc risk strata in the 30-day DAPT window.</p>
      <div class="evidence-citation">Giugliano RP, et al. N Engl J Med. 2013;369(22):2093-2104.</div>
    </div>

    <div class="evidence-item">
      <h4>Sex as a biological risk factor in AF</h4>
      <p>Female sex independently increases stroke risk in AF beyond traditional factors, partly due to higher inflammatory markers and prothrombotic tendencies. The CHA₂DS₂-VASc includes female sex to better identify intermediate-risk women who would otherwise be classified as "low-risk" on CHA₂DS₂ alone.</p>
      <div class="evidence-citation">Andersson T, et al. Lancet. 2013;381(9879):1668-1676.</div>
    </div>

    <div class="evidence-item">
      <h4>Very low-risk AF and anticoagulation</h4>
      <p>In patients with CHA₂DS₂-VASc 0 or 1, absolute stroke risk is <1% per year without anticoagulation. Current international guidelines do not recommend routine anticoagulation in these patients, though individual factors (type of AF, reversibility of risk factors) may change practice.</p>
      <div class="evidence-citation">Kirchhof P, et al. Eur Heart J. 2019;40(32):2680-2769.</div>
    </div>

  </div>
</div>

<div class="collapsible">
  <button class="collapsible-toggle" onclick="toggleCollapsible(event, 'pearls')">Clinical Practice Pearls</button>
  <div class="collapsible-content" id="pearls">

    <div class="pearl">
      <strong>NZ-specific context: HealthPathways & Cardiac Society guidance</strong>
      <p>HealthPathways Canterbury recommends anticoagulation for CHA₂DS₂-VASc ≥2 in men and ≥3 in women, aligning with ESC 2019 guidance. The NZ Cardiac Society position supports this for paroxysmal, persistent, and permanent AF. Consider shared decision-making for borderline risk (score 1-2).</p>
    </div>

    <div class="pearl">
      <strong>DOAC vs. warfarin in primary care</strong>
      <p>DOACs (apixaban, rivaroxaban, dabigatran, edoxaban) are first-line in primary care AF. They avoid INR monitoring, have fewer drug interactions, and are superior to warfarin for reducing intracranial haemorrhage. Warfarin remains relevant only if: mechanical valve, severe CKD (eGFR <15), patient preference, or cost.</p>
    </div>

    <div class="pearl">
      <strong>When CHA₂DS₂-VASc = 1: be thoughtful</strong>
      <p>A score of 1 is the "grey zone." Most guidelines suggest anticoagulation for ≥2, but a single point (e.g., age 65-74 alone, or female sex alone) may not warrant it. Document your reasoning and consider whether that single factor is truly active (e.g., recent hypertension diagnosis vs. well-controlled).</p>
    </div>

    <div class="pearl">
      <strong>Reversible risk factors matter</strong>
      <p>If the only reason for a CHA₂DS₂-VASc ≥2 is hypertension that was just diagnosed and is being aggressively treated, consider delaying anticoagulation for 3-6 months while optimising BP, then recalculate. Similarly, if someone has AF triggered by acute coronary syndrome, reassess once acute phase is over.</p>
    </div>

    <div class="pearl">
      <strong>CKD modifies DOAC choice</strong>
      <p>In moderate-severe CKD (eGFR 15-60), all DOACs are usable but require dose adjustment. Dabigatran is contraindicated in eGFR <30. If eGFR <15, consider warfarin or specialist review. Always check current renal function before prescribing and annually thereafter.</p>
    </div>

    <div class="pearl">
      <strong>Hybrid approaches: DOAC dosing in borderline cases</strong>
      <p>For patients with CHA₂DS₂-VASc ≥2 but bleeding risk concerns, evidence supports using lower-dose DOACs in specific scenarios (age ≥60, weight <60 kg, creatinine >1.5). Document the rationale; this is not "underdosing" but risk-stratified dosing.</p>
    </div>

    <div class="pearl">
      <strong>Paroxysmal AF carries the same stroke risk</strong>
      <p>Many GPs assume paroxysmal AF is "lower risk" than persistent. This is incorrect - stroke risk is determined by CHA₂DS₂-VASc score, not AF type. However, some patients with AF triggered by treatable causes (alcohol, overweight, sleep apnoea) may have lower recurrence if triggers are addressed.</p>
    </div>

    <div class="pearl">
      <strong>Aspirin is no longer first-line in AF</strong>
      <p>Aspirin is inferior to anticoagulation for stroke prevention in AF and is no longer recommended as monotherapy in moderate-high-risk patients. It may still be used for secondary prevention if anticoagulation is truly contraindicated, but this is rare with modern DOACs.</p>
    </div>

  </div>
</div>

<div style="margin-top: 56px; padding-top: 24px; border-top: 1px solid var(--rule); font-size: 14px; color: var(--ink-mute);">
  <p><strong>Disclaimer:</strong> This calculator is a clinical decision-support tool, not a substitute for clinical judgment. CHA₂DS₂-VASc estimates group-level annual stroke risk; individual risk may vary. Always assess HAS-BLED (bleeding risk), renal function, drug interactions, and patient preferences before prescribing anticoagulation. Consult current HealthPathways, NZ Cardiac Society, or ESC guidelines for the most up-to-date recommendations.</p>
</div>

</div>

<script>
  // Risk stratification data
  const riskData = {
    0: { annualRisk: '<1%', category: 'Very low', color: 'low' },
    1: { annualRisk: '0.5-1%', category: 'Low to moderate', color: 'low' },
    2: { annualRisk: '1-1.5%', category: 'Low to moderate', color: 'moderate' },
    3: { annualRisk: '1.5-2%', category: 'Moderate', color: 'moderate' },
    4: { annualRisk: '2-2.5%', category: 'Moderate to high', color: 'moderate' },
    5: { annualRisk: '2.5-3.5%', category: 'Moderate to high', color: 'moderate' },
    6: { annualRisk: '3.5-4.5%', category: 'High', color: 'high' },
    7: { annualRisk: '4-6%', category: 'High', color: 'high' },
    8: { annualRisk: '6-7%', category: 'Very high', color: 'high' },
    9: { annualRisk: '7-9%', category: 'Very high', color: 'high' }
  };

  function calculateScore(event) {
    if (event) {
      event.preventDefault();
    }

    // Validate age selection
    const age75 = document.getElementById('age75').checked ? 2 : 0;
    const age65to74 = document.getElementById('age65to74').checked ? 1 : 0;

    if (age75 && age65to74) {
      alert('Select only one age category (≥75 or 65-74), not both.');
      return;
    }

    // Calculate score
    const chf = document.getElementById('chf').checked ? 1 : 0;
    const htn = document.getElementById('htn').checked ? 1 : 0;
    const dm = document.getElementById('dm').checked ? 1 : 0;
    const stroke2 = document.getElementById('stroke2').checked ? 2 : 0;
    const vascular = document.getElementById('vascular').checked ? 1 : 0;
    const female = document.getElementById('female').checked ? 1 : 0;

    let score = chf + htn + (age75 + age65to74) + dm + stroke2 + vascular + female;

    // Cap at 9
    score = Math.min(score, 9);

    // Display result
    displayResult(score);
  }

  function displayResult(score) {
    const data = riskData[score];
    const resultSection = document.getElementById('resultSection');
    const scoreDisplay = document.getElementById('scoreDisplay');
    const riskCategory = document.getElementById('riskCategory');
    const annualRisk = document.getElementById('annualRisk');
    const anticoagRecommendation = document.getElementById('anticoagRecommendation');

    // Update score
    scoreDisplay.textContent = score;

    // Risk category box
    let categoryText = '';
    if (score === 0) {
      categoryText = `<div class="risk-category risk-low"><strong>Very low risk.</strong> Routine anticoagulation not indicated.</div>`;
    } else if (score === 1) {
      categoryText = `<div class="risk-category risk-moderate"><strong>Low-to-moderate risk.</strong> Consider individual risk factors and shared decision-making.</div>`;
    } else if (score <= 3) {
      categoryText = `<div class="risk-category risk-moderate"><strong>Moderate risk.</strong> Anticoagulation recommended in most cases.</div>`;
    } else {
      categoryText = `<div class="risk-category risk-high"><strong>High risk.</strong> Anticoagulation strongly recommended.</div>`;
    }
    riskCategory.innerHTML = categoryText;

    // Annual stroke risk
    annualRisk.textContent = data.annualRisk + ' per year';

    // Anticoagulation recommendation scaffold
    let recommendation = '';
    if (score === 0) {
      recommendation = `
        <p style="margin-top: 12px;">Routine anticoagulation not recommended. Reassess yearly or if risk factors change.</p>
      `;
    } else if (score === 1) {
      recommendation = `
        <p style="margin-top: 12px;">Borderline risk. Individualise decision:</p>
        <ul class="anticoag-list">
          <li>If female or recent stroke/TIA: consider anticoagulation.</li>
          <li>If other factors are modifiable (e.g., recent HTN diagnosis): consider trial of optimised risk factor management.</li>
          <li>Document discussion with patient: absolute risk <1% per year without treatment.</li>
        </ul>
      `;
    } else if (score === 2) {
      recommendation = `
        <p style="margin-top: 12px;"><strong>Favours anticoagulation.</strong></p>
        <ul class="anticoag-list">
          <li>Recommend anticoagulation in most patients, particularly if female.</li>
          <li>Assess HAS-BLED for bleeding risk.</li>
          <li>If HAS-BLED ≥3: still consider anticoagulation; bleeding risk alone does not contraindicate it.</li>
        </ul>
      `;
    } else if (score <= 4) {
      recommendation = `
        <p style="margin-top: 12px;"><strong>Anticoagulation recommended.</strong></p>
        <ul class="anticoag-list">
          <li>DOAC (apixaban, rivaroxaban, dabigatran, edoxaban) is first-line.</li>
          <li>Assess renal function (eGFR) and adjust DOAC dose if necessary.</li>
          <li>Discuss HAS-BLED and bleeding risk; reassure that DOACs reduce intracranial bleeding vs. warfarin.</li>
        </ul>
      `;
    } else {
      recommendation = `
        <p style="margin-top: 12px;"><strong>Anticoagulation strongly recommended.</strong></p>
        <ul class="anticoag-list">
          <li>Stroke risk is substantial (annual risk ${data.annualRisk}); anticoagulation reduces absolute risk by ~50%.</li>
          <li>DOAC is first-line unless contraindications (mechanical valve, severe CKD <eGFR 15, or patient preference).</li>
          <li>Assess HAS-BLED; if ≥3, document discussion and individualise dosing if needed.</li>
          <li>Check renal function annually; adjust DOAC dose as eGFR declines.</li>
        </ul>
      `;
    }
    anticoagRecommendation.innerHTML = recommendation;

    // Show result section
    resultSection.classList.add('active');

    // Scroll to result
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  function toggleCollapsible(event, id) {
    event.preventDefault();
    const toggle = event.target;
    const content = document.getElementById(id);

    toggle.classList.toggle('active');
    content.classList.toggle('active');
  }

  // Auto-calculate when any field changes
  document.getElementById('cha2ds2Form').addEventListener('change', function() {
    calculateScore();
  });
</script>
