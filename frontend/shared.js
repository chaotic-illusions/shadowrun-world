// Shared UI helpers — included by all app pages

// ── Polling helpers ───────────────────────────────────────────────────────────
let _pollPaused = false;
function pausePoll()  { _pollPaused = true;  }
function resumePoll() { _pollPaused = false; }
function startPolling(loadFn, intervalMs = 5000) {
  setInterval(() => { if (!_pollPaused) loadFn(); }, intervalMs);
}

// ── Auth constants ────────────────────────────────────────────────────────────

const LS_ADMIN = 'sr_admin_token';
const LS_USER  = 'sr_user_token';

let _authCtx = null;

function isAdmin() { return _authCtx?.is_admin === true; }
function isUser()  { return _authCtx?.is_user === true; }
// True only when the admin is actively in admin view (not switched to runner view)
function isAdminMode() { return isAdmin() && (sessionStorage.getItem('sr_view') || 'admin') === 'admin'; }
function userToken()  { return localStorage.getItem(LS_USER)  || null; }
function adminToken() { return localStorage.getItem(LS_ADMIN) || null; }

// ── Auth headers ──────────────────────────────────────────────────────────────

function authHeaders(extra = {}) {
  const h = { ...extra };
  const at = adminToken();
  const ut = userToken();
  if (at) h['X-Admin-Token'] = at;
  if (ut) h['X-User-Token']  = ut;
  return h;
}

// ── bootstrapAuth ─────────────────────────────────────────────────────────────

async function bootstrapAuth() {
  const at = localStorage.getItem(LS_ADMIN);
  const ut = localStorage.getItem(LS_USER);

  if (!at && !ut) {
    window.location.href = '/ui/login.html';
    return null;
  }

  try {
    const res = await fetch('/auth/verify', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ admin_token: at || null, user_token: ut || null }),
    });

    if (res.status === 401) {
      localStorage.removeItem(LS_ADMIN);
      localStorage.removeItem(LS_USER);
      window.location.href = '/ui/login.html';
      return null;
    }

    _authCtx = await res.json();
    _injectAuthLabel();

    if (_authCtx.is_default_password) {
      await _showAutoGenerateOverlay();
      return null;
    }

    if (!isAdmin()) {
      const style = document.createElement('style');
      style.textContent = '.gm-only { display: none !important; }';
      document.head.appendChild(style);
    }

    return _authCtx;
  } catch (e) {
    window.location.href = '/ui/login.html';
    return null;
  }
}

// ── Auth label (bottom-right, no logout) ─────────────────────────────────────

function _injectAuthLabel() {
  // Add Tokens nav link for all authenticated users
  const nav = document.querySelector('header nav');
  if (nav && !nav.querySelector('[href="manage-tokens.html"]')) {
    const a = document.createElement('a');
    a.href = 'manage-tokens.html';
    a.textContent = 'Tokens';
    if (window.location.pathname.endsWith('manage-tokens.html')) a.className = 'active';
    nav.appendChild(a);
  }

  // Bottom-right fixed label
  const label = document.createElement('div');
  label.id = 'auth-label';
  const viewMode0 = sessionStorage.getItem('sr_view') || 'admin';
  const role = isAdmin() ? (viewMode0 === 'admin' ? 'ADMIN' : 'RUNNER') : 'RUNNER';
  const tokenLabel = _authCtx.token_label ? `${_authCtx.token_label} // ` : '';
  label.style.cssText =
    'position:fixed;bottom:10px;right:14px;z-index:500;font-family:var(--font);' +
    'font-size:.7rem;letter-spacing:1px;color:var(--auth-label);pointer-events:none;';
  label.textContent = `[${tokenLabel}${role}]`;

  // Admin+user: show view toggle
  if (_authCtx.is_admin) {
    const toggleWrap = document.createElement('div');
    toggleWrap.style.cssText =
      'position:fixed;bottom:24px;right:14px;z-index:500;font-family:var(--font);' +
      'font-size:.7rem;letter-spacing:1px;';
    const viewMode = sessionStorage.getItem('sr_view') || 'admin';
    const nextMode = viewMode === 'admin' ? 'player' : 'admin';
    const toggleBtn = document.createElement('span');
    toggleBtn.style.cssText = 'color:var(--auth-toggle);opacity:0.85;cursor:pointer';
    toggleBtn.textContent = `[ ${viewMode === 'admin' ? 'SWITCH TO RUNNER VIEW' : 'SWITCH TO ADMIN VIEW'} ]`;
    toggleBtn.addEventListener('click', () => {
      sessionStorage.setItem('sr_view', nextMode);
      location.reload();
    });
    toggleWrap.appendChild(toggleBtn);
    document.body.appendChild(toggleWrap);

    // Apply player-view gm-only hiding
    if (viewMode === 'player') {
      const style = document.createElement('style');
      style.textContent = '.gm-only { display: none !important; }';
      document.head.appendChild(style);
    }
  }

  document.body.appendChild(label);
}

// ── Auto-generate admin token overlay ─────────────────────────────────────────

async function _showAutoGenerateOverlay() {
  // Pre-generate the token from the server
  let generatedToken = null;
  try {
    const res = await fetch('/auth/tokens', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Admin-Token': localStorage.getItem(LS_ADMIN) },
      body: JSON.stringify({ label: 'Admin Token', is_admin: true }),
    });
    if (res.ok) {
      generatedToken = (await res.json()).token;
    }
  } catch(_) {}

  const overlay = document.createElement('div');
  overlay.id = 'gen-token-overlay';
  overlay.style.cssText =
    'position:fixed;inset:0;background:rgba(0,0,0,.92);z-index:9999;' +
    'display:flex;align-items:center;justify-content:center;';

  if (!generatedToken) {
    overlay.innerHTML = `
      <div style="background:var(--bg-card);border:1px solid #1a3a1a;border-top:2px solid var(--red);padding:36px 40px;max-width:500px;width:100%">
        <div style="color:var(--red);font-size:.9rem;letter-spacing:3px;margin-bottom:12px">&gt;&gt; ERROR</div>
        <div class="dim-meta">Could not generate admin token. Check server logs.</div>
      </div>`;
    document.body.appendChild(overlay);
    return;
  }

  const card = document.createElement('div');
  card.style.cssText = 'background:var(--bg-card);border:1px solid #1a3a1a;border-top:2px solid var(--amber);padding:36px 40px;max-width:500px;width:100%';

  const heading = document.createElement('div');
  heading.style.cssText = 'color:var(--amber);font-size:.9rem;letter-spacing:3px;margin-bottom:6px';
  heading.textContent = '>> NEW ADMIN TOKEN GENERATED';

  const subheading = document.createElement('div');
  subheading.style.cssText = 'color:var(--text-dim);font-size:.65rem;letter-spacing:2px;margin-bottom:20px';
  subheading.textContent = 'SAVE THIS TOKEN — YOU WILL NEED IT TO LOG IN';

  const tokenDisplay = document.createElement('div');
  tokenDisplay.id = 'gen-token-display';
  tokenDisplay.style.cssText = 'font-family:var(--font);font-size:.8rem;letter-spacing:2px;color:var(--amber);background:var(--bg-input);border:1px solid #333;padding:14px 16px;word-break:break-all;cursor:pointer;margin-bottom:8px';
  tokenDisplay.textContent = generatedToken;
  tokenDisplay.addEventListener('click', () => {
    navigator.clipboard.writeText(generatedToken).then(() => {
      tokenDisplay.style.color = 'var(--green)';
      setTimeout(() => tokenDisplay.style.color = 'var(--amber)', 1000);
    });
  });

  const hint = document.createElement('div');
  hint.style.cssText = 'color:#444;font-size:.6rem;margin-bottom:24px';
  hint.textContent = 'Click the token to copy it to clipboard.';

  const confirmBtn = document.createElement('button');
  confirmBtn.style.cssText = 'width:100%;padding:11px;background:transparent;border:1px solid var(--green-dim);color:var(--green);font-family:var(--font);font-size:.8rem;letter-spacing:2px;cursor:pointer';
  confirmBtn.textContent = ">> I'VE SAVED IT — CONTINUE";
  confirmBtn.addEventListener('click', () => _confirmNewToken(generatedToken));

  card.append(heading, subheading, tokenDisplay, hint, confirmBtn);
  overlay.appendChild(card);
  document.body.appendChild(overlay);
}

function _confirmNewToken(token) {
  localStorage.setItem(LS_ADMIN, token);
  localStorage.setItem(LS_USER, token);
  document.getElementById('gen-token-overlay')?.remove();
  window.location.reload();
}


// ── Shared DOM helpers ───────────────────────────────────────────────────────

/** HTML-escape a string for safe insertion via innerHTML / template literals. */
function esc(s) {
  return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/** Flash an alert banner inside the given element. */
function showAlert(el, msg, isErr) {
  el.textContent = msg;
  el.className = `alert show ${isErr ? 'alert-err' : 'alert-ok'}`;
  el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Show a styled confirmation dialog. Returns a Promise<boolean>.
 * okLabel  – label for the confirm button (default 'Confirm')
 * okClass  – CSS class for the confirm button (default 'btn-red')
 */
function showConfirm(message, okLabel = 'Confirm', okClass = 'btn-red') {
  return new Promise(resolve => {
    let overlay = document.getElementById('_sharedConfirmOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = '_sharedConfirmOverlay';
      overlay.className = 'modal-overlay';
      overlay.style.zIndex = '700';
      overlay.innerHTML = `
        <div style="background:var(--bg-card);border:1px solid #1a2a1a;border-top:2px solid var(--red);
                    padding:28px 32px;width:100%;max-width:400px">
          <div style="font-size:.75rem;letter-spacing:2px;color:var(--red);margin-bottom:14px">&gt;&gt; CONFIRM ACTION</div>
          <div id="_sharedConfirmMsg" style="font-size:.8rem;color:var(--text-bright);margin-bottom:22px;line-height:1.6"></div>
          <div style="display:flex;gap:8px;justify-content:flex-end">
            <button id="_sharedConfirmOk" class="btn btn-red" style="min-width:90px"></button>
            <button id="_sharedConfirmCancel" class="btn btn-ghost">Cancel</button>
          </div>
        </div>`;
      document.body.appendChild(overlay);
    }

    const msg    = document.getElementById('_sharedConfirmMsg');
    const okBtn  = document.getElementById('_sharedConfirmOk');
    const cancel = document.getElementById('_sharedConfirmCancel');

    msg.textContent    = message;
    okBtn.textContent  = okLabel;
    okBtn.className    = `btn ${okClass}`;
    pausePoll();
    overlay.style.display = 'flex';

    function cleanup(result) {
      resumePoll();
      overlay.style.display = 'none';
      okBtn.removeEventListener('click', onOk);
      cancel.removeEventListener('click', onCancel);
      overlay.removeEventListener('click', onBackdrop);
      document.removeEventListener('keydown', onKey);
      resolve(result);
    }
    function onOk()      { cleanup(true);  }
    function onCancel()  { cleanup(false); }
    function onBackdrop(e) { if (e.target === overlay) cleanup(false); }
    function onKey(e)    { if (e.key === 'Escape') cleanup(false); }

    okBtn.addEventListener('click', onOk);
    cancel.addEventListener('click', onCancel);
    overlay.addEventListener('click', onBackdrop);
    document.addEventListener('keydown', onKey);
  });
}


// ── API fetch wrapper ────────────────────────────────────────────────────────

function apiFetch(url, opts = {}) {
  opts.headers = { ...authHeaders(), ...(opts.headers || {}) };
  if (opts.body) opts.headers['Content-Type'] = 'application/json';
  return fetch(url, opts);
}

/** Parse the error body from a failed API response and throw with a user-friendly message. */
async function apiThrow(res) {
  let msg = res.statusText || `HTTP ${res.status}`;
  try {
    const body = await res.json();
    if (typeof body.detail === 'string') msg = body.detail;
    else if (Array.isArray(body.detail)) msg = body.detail.map(e => e.msg || JSON.stringify(e)).join('; ');
  } catch(_) {}
  throw new Error(msg);
}


// ── Heat helpers ──────────────────────────────────────────────────────────────

function heatClass(h) {
  if (h <= 0) return 'heat-neutral';
  if (h <= 2) return 'heat-noticed';
  if (h <= 4) return 'heat-flagged';
  if (h <= 6) return 'heat-wanted';
  if (h <= 8) return 'heat-hot';
  return 'heat-nova-hot';
}

function heatLabelStr(h) {
  if (h <= 0) return 'Neutral';
  if (h <= 2) return 'Noticed';
  if (h <= 4) return 'Flagged';
  if (h <= 6) return 'Wanted';
  if (h <= 8) return 'Hot';
  return 'Nova Hot';
}

function heatColorStyle(heat) {
  if (heat <= 0) return '';
  if (heat <= 2) return 'color:var(--heat-noticed);';
  if (heat <= 4) return 'color:var(--heat-flagged);';
  if (heat <= 6) return 'color:var(--heat-wanted);';
  if (heat <= 8) return 'color:var(--heat-hot);';
  return 'color:var(--heat-nova);text-shadow:0 0 8px rgba(255,17,17,0.53);';
}


// ── Reputation helpers ────────────────────────────────────────────────────────

function repColorStyle(net_rep) {
  const delta = net_rep - 20;
  if (delta === 0) return '';
  if (delta > 0) {
    const pct = Math.min(1, delta / 20);
    const g = Math.round(160 + 95 * pct);
    return `color:rgba(0,${g},65,${0.7 + 0.3 * pct});`;
  } else {
    const pct = Math.min(1, Math.abs(delta) / 20);
    const opacity = 0.5 + 0.5 * pct;
    return `color:rgba(255,${Math.round(51 * (1 - pct))},${Math.round(51 * (1 - pct))},${opacity});`;
  }
}
