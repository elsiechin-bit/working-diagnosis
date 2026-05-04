/**
 * Workshop Gate — client-side passphrase protection for /workshop/ pages.
 *
 * HOW TO CHANGE THE PASSPHRASE:
 *   1. Open a terminal and run:
 *        node -e "const c=require('crypto');console.log(c.createHash('sha256').update('YOUR_NEW_PASSPHRASE').digest('hex'))"
 *   2. Paste the resulting hash into the HASH constant below.
 *   3. Commit and push.
 *
 * Current passphrase: workshop2026
 * (Change this before sharing the site with your inner circle.)
 */

(function () {
  // Only activate on /workshop/ pages
  if (!window.location.pathname.startsWith('/workshop/')) return;

  const HASH        = 'c5ac06037da727a075d2aa011844ac0b386776b027e1fc62ae45453c4a0b483d';
  const SESSION_KEY = 'wd_workshop_auth';

  // Already authenticated this session — step aside
  if (sessionStorage.getItem(SESSION_KEY) === HASH) return;

  // --- Build overlay ---------------------------------------------------
  const overlay = document.createElement('div');
  overlay.id = 'workshop-gate';
  overlay.style.cssText = [
    'position:fixed', 'inset:0', 'z-index:9999',
    'background:#F5F1E8',
    'display:flex', 'flex-direction:column',
    'align-items:center', 'justify-content:center',
  ].join(';');

  overlay.innerHTML = `
    <div style="
      max-width:400px; width:90%; padding:48px 40px;
      background:#EDE7D8; border:1px solid #D9D1BD; border-radius:4px;
      text-align:center;
    ">
      <p style="
        font-family:'JetBrains Mono',ui-monospace,monospace;
        font-size:0.65rem; letter-spacing:2px; text-transform:uppercase;
        color:#6B7A75; margin:0 0 24px;
      ">Working Diagnosis</p>

      <h1 style="
        font-family:'Fraunces',Georgia,serif;
        font-size:1.55rem; font-weight:500; color:#1A1F1C;
        margin:0 0 10px; letter-spacing:-0.01em;
      ">Clinician Workshop</h1>

      <p style="
        font-family:'Newsreader',Georgia,serif;
        font-size:0.95rem; color:#3A4540; margin:0 0 36px; line-height:1.5;
      ">This area is for registered clinicians only.</p>

      <form id="wg-form">
        <input
          id="wg-input"
          type="password"
          placeholder="Passphrase"
          autocomplete="current-password"
          style="
            display:block; width:100%; padding:11px 14px;
            font-family:'Newsreader',Georgia,serif; font-size:1rem;
            background:#F5F1E8; border:1px solid #D9D1BD; border-radius:3px;
            color:#1A1F1C; margin-bottom:10px;
            outline:none; box-sizing:border-box;
          "
        >
        <p id="wg-error" style="
          font-family:'Newsreader',Georgia,serif;
          font-size:0.88rem; color:#B8714F;
          margin:0 0 10px; display:none;
        ">Incorrect passphrase — try again.</p>
        <button type="submit" style="
          display:block; width:100%; padding:11px 14px;
          font-family:'JetBrains Mono',ui-monospace,monospace;
          font-size:0.7rem; letter-spacing:1.5px; text-transform:uppercase;
          background:#2F6B5C; color:#F5F1E8;
          border:none; border-radius:3px; cursor:pointer;
        ">Enter Workshop</button>
      </form>
    </div>
  `;

  // Attach after body is ready
  function attach() {
    document.body.appendChild(overlay);
    // Small delay to let fonts load
    setTimeout(function () {
      var input = document.getElementById('wg-input');
      if (input) input.focus();
    }, 80);
  }

  if (document.body) {
    attach();
  } else {
    document.addEventListener('DOMContentLoaded', attach);
  }

  // --- Hash helper (Web Crypto API) ------------------------------------
  async function sha256(str) {
    const buf = await crypto.subtle.digest(
      'SHA-256',
      new TextEncoder().encode(str)
    );
    return Array.from(new Uint8Array(buf))
      .map(function (b) { return b.toString(16).padStart(2, '0'); })
      .join('');
  }

  // --- Form submit handler ---------------------------------------------
  document.addEventListener('submit', async function (e) {
    if (e.target.id !== 'wg-form') return;
    e.preventDefault();

    var input = document.getElementById('wg-input');
    var error = document.getElementById('wg-error');
    var hash  = await sha256(input.value);

    if (hash === HASH) {
      sessionStorage.setItem(SESSION_KEY, HASH);
      overlay.remove();
    } else {
      error.style.display = 'block';
      input.value = '';
      input.focus();
    }
  });
})();
