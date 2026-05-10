---
title: Antenatal EDD & Screening
layout: tool.njk
permalink: /workshop/tools/edd/
eleventyExcludeFromCollections: true
specialty: Gynaecology
description: Calculate estimated due date and view your current position on the antenatal timeline with context-aware screening and supplementation guidance.
---

<!-- Input block -->
<div class="input-block">
  <h2>Calculate EDD</h2>

  <form id="eddForm">
    <div class="form-group">
      <label for="lmpDate">Last Menstrual Period (LMP)</label>
      <input type="date" id="lmpDate" name="lmpDate" required>
    </div>

    <div class="form-group">
      <label for="cycleLength">Menstrual Cycle Length (days)</label>
      <select id="cycleLength" name="cycleLength">
        <option value="28">28 days (standard)</option>
        <option value="26">26 days</option>
        <option value="29">29 days</option>
        <option value="30">30 days</option>
        <option value="32">32 days</option>
        <option value="35">35 days</option>
        <option value="custom">Custom</option>
      </select>
      <input type="number" id="customCycle" name="customCycle" min="21" max="45" placeholder="Enter cycle length" style="display: none; margin-top: 8px;">
    </div>

    <div class="button-group">
      <button type="submit" class="btn-primary">Calculate EDD</button>
      <button type="reset" class="btn-secondary">Clear</button>
    </div>
  </form>
</div>

<!-- Results -->
<div id="results" class="results">
  <div class="result-card">
    <div class="result-label">Estimated Due Date</div>
    <div class="result-value" id="eddDisplay"></div>
    <div class="result-meta" id="eddMeta"></div>
  </div>

  <!-- Horizontal timeline -->
  <div class="timeline-container">
    <div class="timeline-label">Pregnancy Timeline (hover notches for screening details)</div>
    <div class="timeline-bar">
      <div id="currentMarker" class="current-marker"></div>
      <div class="timeline-notches" id="timelineNotches"></div>
    </div>
    <div class="timeline-legend">
      <div class="legend-item">
        <div class="legend-dot past"></div>
        <span>Past screening</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot upcoming"></div>
        <span>Upcoming screening</span>
      </div>
      <div class="legend-item">
        <div class="legend-dot current"></div>
        <span>You are here</span>
      </div>
    </div>
  </div>

  <!-- Context-aware panels -->
  <div class="context-panels">
    <div id="suppPanel" class="context-panel">
      <h3>Current Supplementation</h3>
      <ul id="suppList" class="supp-list"></ul>
    </div>

    <div id="watchPanel" class="context-panel">
      <h3>What to Watch For</h3>
      <ul id="watchList" class="watch-list"></ul>
    </div>
  </div>

</div>

<div id="tooltip" class="tooltip"></div>

<script>
  // Set today's date as default FIRST (before any event listeners)
  function initializeDateInput() {
    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0');
    const day = String(today.getDate()).padStart(2, '0');
    const lmpDateInput = document.getElementById('lmpDate');
    if (lmpDateInput) {
      lmpDateInput.value = `${year}-${month}-${day}`;
      console.log('Date initialized to:', lmpDateInput.value);
    }
  }

  // Initialize as soon as DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeDateInput);
  } else {
    initializeDateInput();
  }

  const eddForm = document.getElementById('eddForm');
  const lmpDateInput = document.getElementById('lmpDate');
  const cycleLengthSelect = document.getElementById('cycleLength');
  const customCycleInput = document.getElementById('customCycle');
  const resultsContainer = document.getElementById('results');
  const tooltip = document.getElementById('tooltip');

  console.log('EDD Calculator initialized');

  // Screening events with full details
  const screeningEvents = [
    {
      week: 8,
      title: 'Booking Visit',
      shortTitle: 'Booking',
      details: 'Establish care, confirm dates, risk assessment, baseline bloods (FBC, U&Es, serology, VDRL, HIV, HBsAg, HAV).',
      supps: ['Folic acid 5 mg daily'],
      watch: ['Confirm LMP reliability', 'Nausea and vomiting severity', 'Baseline BP']
    },
    {
      week: 11,
      title: '11-13 Week Scan + Combined Screening',
      shortTitle: 'NT + Screening',
      details: 'Nuchal translucency, PAPP-A, β-hCG (if opted). Confirm/revise EDD if >3 days discrepancy.',
      supps: ['Folic acid 5 mg daily'],
      watch: ['Dating accuracy (>3 days = scan redates)', 'Nuchal translucency result', 'Screening risk discussion']
    },
    {
      week: 14,
      title: 'Second Trimester Begins',
      shortTitle: 'Q2 Begins',
      details: 'Continue routine care, monitor for spotting and pain.',
      supps: ['Folic acid 5 mg daily', 'Iron if Hb <110 g/L'],
      watch: ['Spotting or bleeding (threatened miscarriage vs normal)', 'Abdominal pain (round ligament vs pathology)', 'Severe nausea']
    },
    {
      week: 16,
      title: 'Second Trimester Serum Screening Window',
      shortTitle: 'Quad Screen',
      details: 'Quad screen (if not done combined); amniocentesis window opens if invasive testing desired.',
      supps: ['Folic acid 5 mg daily', 'Iron if anaemic'],
      watch: ['Serum screening results', 'Increased appetite', 'Show of pregnancy']
    },
    {
      week: 18,
      title: '18-20 Week Anatomy Scan',
      shortTitle: 'Anatomy Scan',
      details: 'Structural assessment, placenta location, amniotic fluid volume. Single deepest pocket >2 cm normal.',
      supps: ['Folic acid 5 mg daily', 'Iron if anaemic'],
      watch: ['Fetal anatomy (no major defects)', 'Placenta position (rule out praevia)', 'AFV adequacy']
    },
    {
      week: 22,
      title: 'Late Second Trimester Review',
      shortTitle: 'Review',
      details: 'Fetal growth, fundal height, maternal symptoms. Start anti-D if Rh-negative.',
      supps: ['Folic acid 5 mg daily', 'Iron if anaemic', 'Anti-D if Rh-negative'],
      watch: ['Fetal kick counts increasing', 'Lower back pain (normal but monitor)', 'Glucose tolerance (GDM risk soon)']
    },
    {
      week: 24,
      title: '24-28 Week GDM Screening + FBC',
      shortTitle: 'GDM + FBC',
      details: '75 g OGTT (fasting + 2-hour); repeat FBC. Iron supplementation review.',
      supps: ['Folic acid 5 mg daily', 'Iron if Hb <110 g/L', 'Calcium 1000 mg daily'],
      watch: ['Glucose tolerance (normal <7.8 mmol/L at 2h)', 'Hb trend (anaemia correction)', 'Thirst/polyuria (GDM signs)']
    },
    {
      week: 28,
      title: 'Third Trimester Review',
      shortTitle: 'Q3 Check',
      details: 'Repeat serology (syphilis, HIV, HBsAg if at risk). Anti-D if Rh-negative. Plan delivery location.',
      supps: ['Iron if anaemic', 'Vitamin D if deficient', 'Calcium 1000 mg daily', 'Iodine 150 µg daily'],
      watch: ['Braxton-Hicks increasing', 'Antenatal BP monitoring', 'Fetal movements present']
    },
    {
      week: 32,
      title: 'Growth + Presentation Scan (if indicated)',
      shortTitle: 'Growth Scan',
      details: 'Only if IUGR/oligo/high risk suspected. Abdominal circumference, Doppler if needed. Routine scans not MoH-funded.',
      supps: ['Iron if anaemic', 'Calcium 1000 mg daily'],
      watch: ['Fetal lie (head-down ideal)', 'Umbilical artery Doppler (if done)', 'Liquor volume']
    },
    {
      week: 36,
      title: '36 Week Appointment',
      shortTitle: '36-Week Check',
      details: 'Fetal presentation (palpation ± USS if breech). Plan for labour. Review risk factors and birth wishes.',
      supps: ['Iron if anaemic', 'Calcium 1000 mg daily', 'Vitamin D if deficient'],
      watch: ['Fetal lie (direct cephalic or transverse?)', 'Signs of labour onset (show, contractions)', 'Pre-labour rupture of membranes']
    },
    {
      week: 40,
      title: 'Due Date / Labour Onset',
      shortTitle: 'EDD',
      details: 'Expectant management until 42+0 weeks (NICE/RANZCOG); induction offered at 42 weeks in most units.',
      supps: ['Iron if needed', 'Continue calcium/vitamin D'],
      watch: ['Onset of labour (regular contractions, show, ROM)', 'Non-stress test if post-dates (NST/CTG)', 'Reduced fetal movement']
    },
    {
      week: 42,
      title: 'Post-term Cutoff',
      shortTitle: 'Post-Term',
      details: 'Induction or augmentation recommended. Perinatal mortality risk: 0.4/1000 (42 weeks) vs 0.2/1000 (41 weeks).',
      supps: [],
      watch: ['Induction timing', 'Fetal well-being monitoring', 'Delivery plan confirmed']
    }
  ];

  // Supplementation database
  const supplementationDB = {
    'Folic acid': {
      dose: '5 mg daily',
      start: 0,
      end: 12,
      indication: 'Before conception through 12/40'
    },
    'Iron': {
      dose: 'Start if Hb <110 g/L at booking; continue through postpartum',
      start: 8,
      end: 44,
      indication: 'Anaemia prevention/correction'
    },
    'Vitamin D': {
      dose: '2000 IU daily if deficient (25OH-vit D <50 nmol/L)',
      start: 8,
      end: 40,
      indication: 'If baseline testing shows deficiency'
    },
    'Iodine': {
      dose: '150 µg daily (in prenatal vitamins or Lugol\'s)',
      start: 0,
      end: 40,
      indication: 'Thyroid health and fetal neurodevelopment'
    },
    'Calcium': {
      dose: '1000 mg daily (dietary preferred; supplement if <800 mg/day)',
      start: 14,
      end: 40,
      indication: 'From Q2 onwards; bone health'
    }
  };

  // Watch-for items database
  const watchForDB = {
    '8-14': [
      'Confirm LMP reliability; use US dates if >2 weeks discrepancy',
      'Nausea/vomiting severity (hyperemesis threshold)',
      'Baseline BP and weight'
    ],
    '14-18': [
      'Spotting or bleeding (threatened miscarriage vs normal)',
      'Abdominal pain (round ligament vs pathology)',
      'Severe nausea (still present in ~30% at 16 weeks)'
    ],
    '18-24': [
      'Fetal anatomy on scan (major defects, cardiac)',
      'Placenta location (rule out praevia)',
      'Increased appetite and weight gain (normal ~0.5 kg/week Q2)'
    ],
    '24-28': [
      'GDM screening results (fasting + 2-hour glucose)',
      'Haemoglobin trend (iron response)',
      'Thirst/polyuria (GDM red flags)'
    ],
    '28-36': [
      'Braxton-Hicks frequency (false labour vs true)',
      'BP monitoring (pre-eclampsia early signs: headache, RUQ pain)',
      'Fetal movement patterns (kick counts reassuring)'
    ],
    '36-40': [
      'Fetal lie (head-down ideal for vaginal delivery)',
      'Signs of labour onset (regular contractions, show, ROM)',
      'Reduced fetal movement (report immediately)'
    ],
    '40-42': [
      'Onset of labour (regular contractions, show, rupture of membranes)',
      'Non-stress test if post-dates (NST/CTG reassurance)',
      'Induction discussion if reaching 42+0'
    ]
  };

  // Toggle custom cycle input
  cycleLengthSelect.addEventListener('change', (e) => {
    customCycleInput.style.display = e.target.value === 'custom' ? 'block' : 'none';
    customCycleInput.required = e.target.value === 'custom';
  });

  // Form submission
  eddForm.addEventListener('submit', (e) => {
    console.log('Form submit event triggered');
    e.preventDefault();

    const lmpDate = new Date(lmpDateInput.value);
    console.log('LMP Date:', lmpDate);

    let cycleLength = parseInt(cycleLengthSelect.value);

    if (cycleLengthSelect.value === 'custom') {
      cycleLength = parseInt(customCycleInput.value);
    }

    console.log('Cycle length:', cycleLength);

    // EDD = LMP + 280 days (40 weeks)
    const eddDate = new Date(lmpDate);
    eddDate.setDate(eddDate.getDate() + 280);

    // Calculate gestational age at today
    const today = new Date();
    const totalWeeks = (today - lmpDate) / (7 * 24 * 60 * 60 * 1000);
    const weeksToday = Math.floor(totalWeeks);
    const daysToday = Math.round((totalWeeks - weeksToday) * 7);

    // Display EDD
    displayEDD(eddDate, weeksToday, daysToday);

    // Generate timeline
    generateTimeline(lmpDate, eddDate, weeksToday, daysToday);

    // Generate context panels
    generateContextPanels(weeksToday, daysToday);

    resultsContainer.classList.add('active');
  });

  function displayEDD(eddDate, weeksToday, daysToday) {
    console.log('displayEDD called with:', { eddDate, weeksToday, daysToday });
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const formattedEDD = eddDate.toLocaleDateString('en-NZ', options);

    document.getElementById('eddDisplay').textContent = formattedEDD;
    document.getElementById('eddMeta').innerHTML = `
      <span style="display: block; margin-bottom: 4px;">
        Currently ${weeksToday} weeks ${daysToday} days gestation
      </span>
    `;
    console.log('EDD display updated');
  }

  function generateTimeline(lmpDate, eddDate, currentWeeks, currentDays) {
    const timelineNotches = document.getElementById('timelineNotches');
    const currentMarker = document.getElementById('currentMarker');
    const totalDays = 280;
    const currentDayOfPregnancy = currentWeeks * 7 + currentDays;
    const percentComplete = (currentDayOfPregnancy / totalDays) * 100;

    // Position current marker
    currentMarker.style.left = percentComplete + '%';

    timelineNotches.innerHTML = '';

    screeningEvents.forEach((event) => {
      const weekDays = event.week * 7;
      const position = (weekDays / totalDays) * 100;
      const isPast = event.week <= currentWeeks;

      const notch = document.createElement('div');
      notch.className = 'notch';
      notch.style.left = position + '%';
      notch.innerHTML = `
        <div class="notch-dot"></div>
        <div class="notch-label">${event.shortTitle}</div>
      `;

      // Show tooltip on hover
      notch.addEventListener('mouseenter', (e) => {
        tooltip.textContent = event.title;
        tooltip.classList.add('show');
        const rect = notch.getBoundingClientRect();
        tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
        tooltip.style.top = (rect.top - tooltip.offsetHeight - 8) + 'px';
      });

      notch.addEventListener('mouseleave', () => {
        tooltip.classList.remove('show');
      });

      timelineNotches.appendChild(notch);
    });
  }

  function generateContextPanels(weeksToday, daysToday) {
    const suppList = document.getElementById('suppList');
    const watchList = document.getElementById('watchList');
    const suppPanel = document.getElementById('suppPanel');
    const watchPanel = document.getElementById('watchPanel');

    suppList.innerHTML = '';
    watchList.innerHTML = '';

    // Find current supplementation
    const activeSupps = [];
    Object.entries(supplementationDB).forEach(([name, data]) => {
      if (weeksToday >= data.start && weeksToday <= data.end) {
        activeSupps.push({ name, ...data });
      }
    });

    if (activeSupps.length > 0) {
      suppPanel.classList.remove('empty');
      activeSupps.forEach((supp) => {
        const li = document.createElement('li');
        li.className = 'supp-item';
        li.innerHTML = `
          <span class="supp-name">${supp.name}</span>
          <span class="supp-dose">${supp.dose}</span>
        `;
        suppList.appendChild(li);
      });
    } else {
      suppPanel.classList.add('empty');
      suppList.innerHTML = '<li class="empty-message">No routine supplementation at this stage</li>';
    }

    // Find current watch items
    let watchRange = null;
    Object.keys(watchForDB).forEach((range) => {
      const [start, end] = range.split('-').map(Number);
      if (weeksToday >= start && weeksToday < end) {
        watchRange = range;
      }
    });

    if (watchRange && watchForDB[watchRange]) {
      watchPanel.classList.remove('empty');
      watchForDB[watchRange].forEach((item) => {
        const li = document.createElement('li');
        li.className = 'watch-item';
        li.textContent = item;
        watchList.appendChild(li);
      });
    } else {
      watchPanel.classList.add('empty');
      watchList.innerHTML = '<li class="empty-message">No routine monitoring at this stage</li>';
    }
  }

  // Logging complete
  console.log('Script fully loaded and ready');
</script>
