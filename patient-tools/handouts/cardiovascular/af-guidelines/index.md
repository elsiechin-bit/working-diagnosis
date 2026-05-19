---
title: AF Guidelines
layout: topic.njk
specialty: cardiovascular
description: New Zealand approach to atrial fibrillation management based on NHFA/CSANZ 2018 guidelines. Interactive decision trees for rate vs rhythm control, stroke risk assessment, and anticoagulation strategy.
dek: "2018 NHFA/CSANZ standards for AF management in primary care"
ctags: [guidelines, clinical-pathways]
---

<p class="topic-trail"><a class="topic-trail-sep" href="/library/">Library</a> <span class="topic-trail-sep">›</span> <a href="/cardiovascular/">Cardiovascular</a> <span class="topic-trail-sep">›</span> <span class="here">Atrial Fibrillation</span></p>

## CHA₂DS₂-VA Score Calculator

Use this interactive calculator to estimate stroke risk. Each point carries specific weight in predicting annual stroke risk.

<div class="interactive-box">
  <div class="score-calculator">
    <div class="checkbox-item">
      <input type="checkbox" id="c-checkbox" class="score-checkbox">
      <label for="c-checkbox"><strong>C</strong> - Congestive heart failure / LV dysfunction <span class="score-value">(1 point)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="h-checkbox" class="score-checkbox">
      <label for="h-checkbox"><strong>H</strong> - Hypertension <span class="score-value">(1 point)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="a1-checkbox" class="score-checkbox">
      <label for="a1-checkbox"><strong>A</strong> - Age ≥75 <span class="score-value">(2 points)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="d-checkbox" class="score-checkbox">
      <label for="d-checkbox"><strong>D</strong> - Diabetes mellitus <span class="score-value">(1 point)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="s-checkbox" class="score-checkbox">
      <label for="s-checkbox"><strong>S</strong> - Prior stroke, TIA, or thromboembolism <span class="score-value">(2 points)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="v-checkbox" class="score-checkbox">
      <label for="v-checkbox"><strong>V</strong> - Vascular disease (prior MI, PVD, aortic plaque) <span class="score-value">(1 point)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="a2-checkbox" class="score-checkbox">
      <label for="a2-checkbox"><strong>A</strong> - Age 65–74 <span class="score-value">(1 point)</span></label>
    </div>
    <div class="checkbox-item">
      <input type="checkbox" id="f-checkbox" class="score-checkbox">
      <label for="f-checkbox"><strong>f</strong> - Female sex <span class="score-value">(1 point)</span></label>
    </div>
  </div>
  <div class="score-result">
    <div class="total-score">
      <span class="score-label">Total Score:</span>
      <span class="score-number" id="totalScore">0</span>
    </div>
    <div class="score-interpretation">
      <p id="scoreInterpretation" class="interpretation-text"></p>
    </div>
  </div>
</div>

### Score Interpretation

- **Score 0–1**: Low risk (0–1% annual stroke risk) — consider aspirin or no anticoagulation based on clinical judgment
- **Score 2**: Moderate risk (2–3% annual stroke risk) — anticoagulation should be considered
- **Score ≥3**: High risk (≥4% annual stroke risk) — anticoagulation is recommended

## Anticoagulation Strategy

### NOAC-First Approach

Oral anticoagulants are the first-line agents. Choose based on renal function, drug interactions, and individual factors.

<div class="comparison-table">
  <div class="drug-card">
    <h4>Apixaban</h4>
    <p><strong>Dose:</strong> 5 mg BD</p>
    <p><strong>Renal adjustment:</strong> ≥2 of: age ≥60, weight ≤60 kg, creatinine ≥133 µmol/L → 2.5 mg BD</p>
    <p><strong>Note:</strong> Predictor of high drug interaction risk</p>
  </div>
  <div class="drug-card">
    <h4>Dabigatran</h4>
    <p><strong>Dose:</strong> 110 or 150 mg BD</p>
    <p><strong>150 mg preferred</strong> for stroke prevention</p>
    <p><strong>Note:</strong> Requires twice-daily dosing; lower GI side effects vs older agents</p>
  </div>
  <div class="drug-card">
    <h4>Edoxaban</h4>
    <p><strong>Dose:</strong> 60 mg daily (30 mg if weight ≤60 kg or creatinine ≥100 µmol/L)</p>
    <p><strong>Note:</strong> Once-daily dosing; good renal function profile</p>
  </div>
  <div class="drug-card">
    <h4>Rivaroxaban</h4>
    <p><strong>Dose:</strong> 20 mg daily with food</p>
    <p><strong>Renal adjustment:</strong> Creatinine >100 µmol/L → consider 15 mg</p>
    <p><strong>Note:</strong> Once-daily dosing; must be taken with food for optimal absorption</p>
  </div>
</div>

### Warfarin Alternative

Warfarin remains an option where NOACs are contraindicated or not tolerated.

- **Target INR:** 2–3
- **Monitoring:** Baseline INR, then at regular intervals; more frequent checks during initiation
- **Drug interactions:** Monitor closely with NSAIDs, antibiotics, and other anticoagulants

### Anticoagulation NOT Recommended

- **Aspirin monotherapy** is not effective for stroke prevention in AF and should not be used

## Rate vs Rhythm Control Strategy

Evidence shows both strategies have similar outcomes for most AF patients. Choice depends on symptoms and individual factors.

<table class="comparison-table">
  <thead>
    <tr>
      <th>Aspect</th>
      <th>Rate Control</th>
      <th>Rhythm Control</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Target Heart Rate</strong></td>
      <td>Resting <70 bpm, exercise <110 bpm</td>
      <td>Sinus rhythm restoration and maintenance</td>
    </tr>
    <tr>
      <td><strong>First-line Drugs</strong></td>
      <td>Beta-blockers or non-DHP CCBs</td>
      <td>Flecainide (paroxysmal) or amiodarone</td>
    </tr>
    <tr>
      <td><strong>Advantages</strong></td>
      <td>Simpler management; fewer drug interactions; oral anticoagulation always needed</td>
      <td>May improve symptoms; may reduce hospitalisations; requires same anticoagulation</td>
    </tr>
    <tr>
      <td><strong>Disadvantages</strong></td>
      <td>Ongoing AF burden; potential progressive atrial remodeling</td>
      <td>More complex; more drugs; more frequent monitoring; similar symptom outcomes to rate control</td>
    </tr>
    <tr>
      <td><strong>When to Consider Rhythm Control</strong></td>
      <td></td>
      <td>Symptomatic paroxysmal AF; young patients; those intolerant of persistent AF symptoms</td>
    </tr>
  </tbody>
</table>

## First-Line Rate Control Agents

<div class="comparison-table">
  <div class="drug-card">
    <h4>Beta-Blockers</h4>
    <p><strong>Examples:</strong> Bisoprolol, metoprolol, atenolol</p>
    <p><strong>Starting doses:</strong> Bisoprolol 1.25 mg daily; titrate to 2.5–5 mg daily</p>
    <p><strong>Advantages:</strong> Well-tolerated; also provide post-MI protection</p>
    <p><strong>Cautions:</strong> Avoid if LVEF <40% (use ACE-I + ivabradine or consider CCB)</p>
  </div>
  <div class="drug-card">
    <h4>Non-DHP Calcium Channel Blockers</h4>
    <p><strong>Examples:</strong> Verapamil, diltiazem</p>
    <p><strong>Doses:</strong> Verapamil 40–80 mg TDS; diltiazem 60 mg TDS</p>
    <p><strong>Advantages:</strong> Good rate control; also provide BP reduction</p>
    <p><strong>Cautions:</strong> Contraindicated if LVEF <40%; avoid with beta-blockers</p>
  </div>
  <div class="drug-card">
    <h4>Flecainide (for Rhythm Control)</h4>
    <p><strong>Dose:</strong> 50–100 mg BD</p>
    <p><strong>Indications:</strong> Paroxysmal AF in structurally normal hearts; "pill-in-pocket" strategy may be considered</p>
    <p><strong>Cautions:</strong> Contraindicated in structural heart disease or prior MI; proarrhythmic potential</p>
  </div>
</div>

## Lifestyle and Opportunistic Screening

- **Reduce alcohol consumption:** Heavy drinking increases AF risk and may worsen control
- **Weight management:** Obesity is a modifiable AF risk factor
- **Sleep apnea screening:** If present, treat—it can exacerbate AF
- **Exercise:** Regular moderate activity is safe and beneficial for AF patients
- **Stress reduction:** May help symptom management
- **Caffeine and stimulant reduction:** May reduce palpitation perception (not proven to reduce AF risk)
- **Thyroid screening:** Essential for AF; both hyper- and hypothyroidism can trigger AF

## When to Refer

- **Symptomatic paroxysmal AF:** Consider cardiology for rhythm control or ablation discussion
- **Persistent AF with poor rate control:** May need specialist assessment for alternative agents or ablation
- **AF with structural heart disease:** Requires cardiologist input
- **AF with borderline HF:** Early specialist involvement recommended
- **AF refractory to first-line agents:** Consider ablation referral
- **Young patients with AF:** Evaluate for underlying structural or electrical disorders

<section class="panic-strip">
  <div class="panic-tile dont-miss">
    <h3>Don't miss</h3>
    <ul>
      <li><strong>Thyroid dysfunction</strong> — present in ~10% of AF patients; screen with TSH</li>
      <li><strong>Structural heart disease</strong> — echo if any signs of HF or cardiac risk factors</li>
      <li><strong>Acute decompensation</strong> — AF with RVR + haemodynamic instability requires urgent hospital referral</li>
      <li><strong>Stroke in untreated high-risk patient</strong> — review anticoagulation indication immediately</li>
    </ul>
  </div>
  <div class="panic-tile safety-net">
    <h3>Safety net</h3>
    <ul>
      <li>Patients on anticoagulation should carry a card or medical alert to inform emergency services</li>
      <li>Baseline renal function is essential before starting anticoagulation; check at least annually</li>
      <li>Review anticoagulation necessity if paroxysmal AF reverts to sinus rhythm permanently</li>
      <li>Consider HAS-BLED score for bleeding risk before starting anticoagulation</li>
      <li>Advise patients to report symptoms of bleeding (melena, haematuria, unusual bruising)</li>
    </ul>
  </div>
</section>

<style>
.interactive-box {
  border-left: 4px solid var(--color-primary);
  padding: 1.5rem;
  background-color: var(--color-bg-secondary);
  border-radius: 4px;
  margin: 1.5rem 0;
}

.score-calculator {
  margin-bottom: 1.5rem;
}

.checkbox-item {
  display: flex;
  align-items: center;
  margin: 0.75rem 0;
  gap: 0.75rem;
}

.checkbox-item input[type="checkbox"] {
  width: 20px;
  height: 20px;
  cursor: pointer;
  margin: 0;
}

.checkbox-item label {
  cursor: pointer;
  margin: 0;
  font-size: 0.95rem;
}

.score-value {
  font-size: 0.85rem;
  color: var(--color-text-secondary);
}

.score-result {
  padding: 1rem;
  background-color: var(--color-bg-tertiary);
  border-radius: 4px;
}

.total-score {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 0.75rem;
}

.score-label {
  font-weight: 600;
  font-size: 1rem;
}

.score-number {
  font-size: 2rem;
  font-weight: bold;
  color: var(--color-primary);
}

.score-interpretation {
  font-size: 0.9rem;
  line-height: 1.5;
}

.interpretation-text {
  margin: 0;
  color: var(--color-text-secondary);
}

.comparison-table {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin: 1.5rem 0;
}

table.comparison-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1.5rem 0;
}

table.comparison-table th,
table.comparison-table td {
  border: 1px solid var(--color-border);
  padding: 0.75rem;
  text-align: left;
}

table.comparison-table th {
  background-color: var(--color-bg-secondary);
  font-weight: 600;
}

table.comparison-table tr:nth-child(even) {
  background-color: var(--color-bg-tertiary);
}

.drug-card {
  border: 1px solid var(--color-border);
  border-radius: 4px;
  padding: 1rem;
  background-color: var(--color-bg-tertiary);
}

.drug-card h4 {
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
  color: var(--color-primary);
}

.drug-card p {
  margin: 0.5rem 0;
  font-size: 0.9rem;
  line-height: 1.5;
}

.panic-strip {
  margin: 2rem 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1.5rem;
}

.panic-tile {
  border-left: 4px solid var(--color-warning);
  padding: 1.5rem;
  background-color: var(--color-bg-secondary);
  border-radius: 4px;
}

.panic-tile.dont-miss {
  border-left-color: var(--color-danger);
}

.panic-tile h3 {
  margin: 0 0 1rem 0;
  font-size: 1rem;
  font-weight: 600;
}

.panic-tile ul {
  margin: 0;
  padding-left: 1.25rem;
}

.panic-tile li {
  margin-bottom: 0.5rem;
  line-height: 1.5;
  font-size: 0.9rem;
}

@media (max-width: 640px) {
  .comparison-table {
    grid-template-columns: 1fr;
  }
  
  table.comparison-table {
    font-size: 0.85rem;
  }
  
  table.comparison-table th,
  table.comparison-table td {
    padding: 0.5rem;
  }
}
</style>

<script>
const scoreValues = {
  'c-checkbox': 1,
  'h-checkbox': 1,
  'a1-checkbox': 2,
  'd-checkbox': 1,
  's-checkbox': 2,
  'v-checkbox': 1,
  'a2-checkbox': 1,
  'f-checkbox': 1
};

function updateScore() {
  let total = 0;
  for (const [id, value] of Object.entries(scoreValues)) {
    const checkbox = document.getElementById(id);
    if (checkbox && checkbox.checked) {
      total += value;
    }
  }
  
  const totalScoreEl = document.getElementById('totalScore');
  const interpretationEl = document.getElementById('scoreInterpretation');
  
  if (totalScoreEl) {
    totalScoreEl.textContent = total;
  }
  
  if (interpretationEl) {
    let interpretation = '';
    if (total === 0 || total === 1) {
      interpretation = '<strong>Low risk:</strong> 0–1% annual stroke risk. Consider aspirin or no anticoagulation based on clinical judgment.';
    } else if (total === 2) {
      interpretation = '<strong>Moderate risk:</strong> 2–3% annual stroke risk. Anticoagulation should be considered.';
    } else {
      interpretation = '<strong>High risk:</strong> ≥4% annual stroke risk. Anticoagulation is recommended.';
    }
    interpretationEl.innerHTML = interpretation;
  }
}

document.addEventListener('DOMContentLoaded', function() {
  for (const id of Object.keys(scoreValues)) {
    const checkbox = document.getElementById(id);
    if (checkbox) {
      checkbox.addEventListener('change', updateScore);
    }
  }
  updateScore();
});
</script>
