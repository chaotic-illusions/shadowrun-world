// Shared UI helpers -- included by all app pages

// -- Polling helpers -----------------------------------------------------------
let _pollPaused = false;
function pausePoll()  { _pollPaused = true;  }
function resumePoll() { _pollPaused = false; }
function startPolling(loadFn, intervalMs = 2500) {
  setInterval(() => { if (!_pollPaused) loadFn(); }, intervalMs);
}

// -- Auth constants ------------------------------------------------------------

const LS_ADMIN = 'sr_admin_token';
const LS_USER  = 'sr_user_token';

let _authCtx = null;

function isAdmin() { return _authCtx?.is_admin === true; }
function isUser()  { return _authCtx?.is_user === true; }
// True only when the admin is actively in admin view (not switched to runner view)
function isAdminMode() { return isAdmin() && (sessionStorage.getItem('sr_view') || 'admin') === 'admin'; }
function userToken()  { return localStorage.getItem(LS_USER)  || null; }
function adminToken() { return localStorage.getItem(LS_ADMIN) || null; }

// -- Auth headers --------------------------------------------------------------

function authHeaders(extra = {}) {
  const h = { ...extra };
  const at = adminToken();
  const ut = userToken();
  if (at) h['X-Admin-Token'] = at;
  if (ut) h['X-User-Token']  = ut;
  return h;
}

// -- Matrix Run nav gate -------------------------------------------------------
// Hides the Matrix Run nav link for players with no claimed PC that has deck skills,
// matching the same access check used by the deck-workshop interrupt overlay.
async function _applyMatrixRunNavGate() {
  if (isAdminMode()) return;
  try {
    const [charRes, mineRes] = await Promise.all([
      apiFetch('/characters/'),
      apiFetch('/characters/mine'),
    ]);
    if (!charRes.ok || !mineRes.ok) return;
    const chars = await charRes.json();
    const mineData = await mineRes.json();
    const mineIds = new Set(mineData.ids || []);
    const eligible = chars.filter(c =>
      c.is_pc && c.is_active && mineIds.has(c.id) &&
      ((c.computer_skill_enabled  && (c.computer_skill_rating  || 0) >= 1) ||
       (c.software_skill_enabled  && (c.software_skill_rating  || 0) >= 1) ||
       (c.matrix_skill_enabled    && (c.matrix_skill_rating    || 0) >= 1))
    );
    if (!eligible.length) {
      document.querySelectorAll('nav a[href="matrix-run.html"]')
        .forEach(a => { a.style.display = 'none'; });
    }
  } catch (_) {}
}

// -- bootstrapAuth -------------------------------------------------------------

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

    _applyMatrixRunNavGate();

    return _authCtx;
  } catch (e) {
    window.location.href = '/ui/login.html';
    return null;
  }
}

// -- Auth label (bottom-right, no logout) -------------------------------------

function _injectAuthLabel() {
  const nav = document.querySelector('header nav');
  // Add Downtime nav link (GM-only via .gm-only -> hidden for players and in runner view)
  if (nav && !nav.querySelector('[href="manage-downtime.html"]')) {
    const d = document.createElement('a');
    d.href = 'manage-downtime.html';
    d.textContent = 'Downtime';
    d.className = 'gm-only';
    if (window.location.pathname.endsWith('manage-downtime.html')) d.className += ' active';
    nav.appendChild(d);
  }
  // Add Tokens nav link for all authenticated users
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

// -- Auto-generate admin token overlay -----------------------------------------

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
  subheading.textContent = 'SAVE THIS TOKEN -- YOU WILL NEED IT TO LOG IN';

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
  confirmBtn.textContent = ">> I'VE SAVED IT -- CONTINUE";
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


// -- Shared DOM helpers -------------------------------------------------------

/** HTML-escape a string for safe insertion via innerHTML / template literals.
 *  Also escapes ' and ` so it's safe inside single-quoted or backtick-quoted
 *  attribute/JS-string contexts (e.g. onclick="f('${esc(x)}')"). */
function esc(s) {
  return String(s ?? '')
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;')
    .replace(/'/g,'&#39;')
    .replace(/`/g,'&#96;');
}

/** Flash an alert banner inside the given element. */
function showAlert(el, msg, isErr) {
  el.textContent = msg;
  el.className = `alert show ${isErr ? 'alert-err' : 'alert-ok'}`;
  el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Show a styled confirmation dialog. Returns a Promise<boolean>.
 * okLabel  - label for the confirm button (default 'Confirm')
 * okClass  - CSS class for the confirm button (default 'btn-red')
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

/**
 * Show a styled prompt dialog with a single input field. Returns a
 * Promise<string|null> -- the entered value, or null when cancelled.
 * opts: { okLabel='OK', okClass='btn-green', title='>> INPUT REQUIRED',
 *         inputType='text', placeholder='' }
 */
function showPrompt(message, defaultVal = '', opts = {}) {
  const okLabel     = opts.okLabel     || 'OK';
  const okClass     = opts.okClass     || 'btn-green';
  const title       = opts.title       || '>> INPUT REQUIRED';
  const inputType   = opts.inputType   || 'text';
  const placeholder = opts.placeholder || '';
  return new Promise(resolve => {
    let overlay = document.getElementById('_sharedPromptOverlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = '_sharedPromptOverlay';
      overlay.className = 'modal-overlay';
      overlay.style.zIndex = '700';
      overlay.innerHTML = `
        <div style="background:var(--bg-card);border:1px solid #1a2a1a;border-top:2px solid var(--cyan);
                    padding:28px 32px;width:100%;max-width:420px">
          <div id="_sharedPromptTitle" style="font-size:.75rem;letter-spacing:2px;color:var(--cyan);margin-bottom:14px"></div>
          <div id="_sharedPromptMsg" style="font-size:.8rem;color:var(--text-bright);margin-bottom:14px;line-height:1.6"></div>
          <input id="_sharedPromptInput" type="text" style="margin-bottom:22px" />
          <div style="display:flex;gap:8px;justify-content:flex-end">
            <button id="_sharedPromptOk" class="btn btn-green" style="min-width:90px"></button>
            <button id="_sharedPromptCancel" class="btn btn-ghost">Cancel</button>
          </div>
        </div>`;
      document.body.appendChild(overlay);
    }

    const titleEl = document.getElementById('_sharedPromptTitle');
    const msgEl   = document.getElementById('_sharedPromptMsg');
    const input   = document.getElementById('_sharedPromptInput');
    const okBtn   = document.getElementById('_sharedPromptOk');
    const cancel  = document.getElementById('_sharedPromptCancel');

    titleEl.textContent = title;
    msgEl.textContent   = message;
    input.type          = inputType;
    input.placeholder   = placeholder;
    input.value         = defaultVal == null ? '' : String(defaultVal);
    okBtn.textContent   = okLabel;
    okBtn.className     = `btn ${okClass}`;
    pausePoll();
    overlay.style.display = 'flex';
    setTimeout(() => { input.focus(); input.select(); }, 30);

    function cleanup(result) {
      resumePoll();
      overlay.style.display = 'none';
      okBtn.removeEventListener('click', onOk);
      cancel.removeEventListener('click', onCancel);
      overlay.removeEventListener('click', onBackdrop);
      input.removeEventListener('keydown', onKey);
      resolve(result);
    }
    function onOk()       { cleanup(input.value); }
    function onCancel()   { cleanup(null); }
    function onBackdrop(e){ if (e.target === overlay) cleanup(null); }
    function onKey(e) {
      if (e.key === 'Enter')  { e.preventDefault(); cleanup(input.value); }
      if (e.key === 'Escape') { e.preventDefault(); cleanup(null); }
    }

    okBtn.addEventListener('click', onOk);
    cancel.addEventListener('click', onCancel);
    overlay.addEventListener('click', onBackdrop);
    input.addEventListener('keydown', onKey);
  });
}


// -- API fetch wrapper --------------------------------------------------------

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


// -- Manage-page auto-save -----------------------------------------------------
// Replaces a CRUD modal's Save/Cancel buttons with a debounced auto-save plus a
// quiet status line. A brand-new record is CREATED (POST) as soon as the required
// field(s) are valid; every later edit silently PATCHes. All page-specific logic
// (payload shape, list refresh, edit-mode flip) stays in the page via cfg.commit.
//
// cfg = {
//   overlayId,            // id of the .edit-overlay that wraps the modal
//   statusId,             // id to give the injected status <span>
//   foot(),              // () => the .edit-modal-foot element to host the status line
//   idleMsg,             // text shown while required fields are still blank
//   active(),           // () => bool : only arm when true (e.g. isAdminMode())
//   valid(),            // () => bool : required fields present
//   editingId(),        // () => current record id, or null/undefined for a new record
//   commit(isCreate),   // async () : POST (create) or PATCH (update). On create it MUST
//                       //   set the page's editingId + flip the modal to edit mode, and
//                       //   should refresh the list silently. Throw on failure.
// }
function makeManageAutoSave(cfg) {
  let timer = null, inFlight = false, pending = false, ready = false;

  function status(state) {
    const el = document.getElementById(cfg.statusId);
    if (!el) return;
    el.className = 'ws-save-status ' + state;
    el.textContent = state === 'saving' ? 'Saving...'
      : state === 'error' ? 'Save failed -- retrying...'
      : state === 'idle'  ? (cfg.idleMsg || 'Waiting for input...')
      : 'All changes saved OK';
  }

  function arm() {
    const foot = cfg.foot();
    if (!foot || (cfg.active && !cfg.active())) { ready = false; return; }
    let s = document.getElementById(cfg.statusId);
    if (!s) {
      s = document.createElement('span');
      s.id = cfg.statusId;
      s.className = 'ws-save-status';
      s.style.flex = '1';
      foot.insertBefore(s, foot.firstChild);
    }
    ready = true;
    status(cfg.valid() ? 'saved' : 'idle');
  }

  function disarm() { ready = false; clearTimeout(timer); }

  function schedule() {
    if (!ready) return;
    const ov = document.getElementById(cfg.overlayId);
    if (!ov || !ov.classList.contains('open')) return;
    if (!cfg.valid()) { clearTimeout(timer); status('idle'); return; }
    status('saving');
    clearTimeout(timer);
    timer = setTimeout(saveNow, 1000);
  }

  async function saveNow() {
    if (!ready || !cfg.valid()) return;
    if (inFlight) { pending = true; return; }
    inFlight = true;
    const isCreate = cfg.editingId() == null;
    try {
      await cfg.commit(isCreate);
      status('saved');
    } catch (e) {
      status('error');
    } finally {
      inFlight = false;
      if (pending) { pending = false; schedule(); }
    }
  }

  document.addEventListener('input',  e => { if (e.target.closest && e.target.closest('#' + cfg.overlayId)) schedule(); });
  document.addEventListener('change', e => { if (e.target.closest && e.target.closest('#' + cfg.overlayId)) schedule(); });

  return { arm, disarm, schedule };
}


// -- Heat helpers --------------------------------------------------------------

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


// -- Security rating helpers (SR2 "Color-N" format) ---------------------------
// Used by host/RTG/org editors. "Red-8" -> code "Red", value "8".

/** Parse a "Color-Value" string. Returns {code, value} (both strings); empty if unset/malformed. */
function parseSan(rating) {
  const s = String(rating || '');
  const i = s.indexOf('-');
  return i > -1 ? { code: s.slice(0, i), value: s.slice(i + 1) } : { code: '', value: '' };
}

/** <option> markup for the security-code selector (Blue/Green/Orange/Red/Black). */
function buildLTGCodeOpts(sel) {
  return ['', 'Blue', 'Green', 'Orange', 'Red', 'Black'].map(c =>
    `<option value="${c}"${c === sel ? ' selected' : ''}>${c || '--'}</option>`
  ).join('');
}

/** <option> markup for the security-value selector (2-14, host dice vs decker). */
function buildSecValOpts(selVal) {
  let opts = '<option value="">--</option>';
  for (let n = 2; n <= 14; n++) {
    opts += `<option value="${n}"${String(n) === String(selVal) ? ' selected' : ''}>${n}</option>`;
  }
  return opts;
}


// -- Reputation helpers --------------------------------------------------------

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


// -- Number stepper initializer ------------------------------------------------
// Initialization contract:
// 1) A single global call runs on DOMContentLoaded below.
// 2) Individual pages should call initNumSteppers(subtree) only after injecting
//    new number inputs at runtime (dynamic panels, rows, modals, etc.).
// Wraps every input[type=number] inside `root` with in-field up/down controls.
// Safe to call multiple times -- skips already-initialized inputs.
// Buttons fire once on press, then repeat after 400ms hold at 80ms intervals.
function initNumSteppers(root) {
  (root || document).querySelectorAll('input[type=number]:not(.ns-init):not(.no-stepper)').forEach(inp => {
    inp.classList.add('ns-init');
    const wrap = document.createElement('div');
    wrap.className = 'infield-num-wrap';

    // Preserve explicit inline widths (e.g. style="width:80px") so in-field
    // controls stay visually attached to compact numeric fields.
    const explicitWidth = (inp.style.width || '').trim();
    if (explicitWidth) {
      wrap.style.width = explicitWidth;
      inp.style.width = '100%';
    }

    inp.parentNode.insertBefore(wrap, inp);
    wrap.appendChild(inp);

    function makeStep(dir) {
      return function() {
        // A disabled input must never be steppable -- a disabled <button> suppresses real
        // user clicks, but programmatic/synthetic events still reach this handler. Guard
        // here so a locked form (e.g. a deck repair) cannot have its values changed.
        if (inp.disabled || inp.readOnly) return;
        const step = parseFloat(inp.step) || 1;
        const min  = inp.min !== '' ? parseFloat(inp.min) : -Infinity;
        const max  = inp.max !== '' ? parseFloat(inp.max) : Infinity;
        const autoAtMin = inp.dataset.autoAtMin === 'true' || inp.dataset.autoAtMin === '1';
        const raw = (inp.value || '').trim();
        const hasNumeric = raw !== '' && !Number.isNaN(parseFloat(raw));

        function emit() {
          inp.dispatchEvent(new Event('input', { bubbles: true }));
          inp.dispatchEvent(new Event('change', { bubbles: true }));
        }

        if (autoAtMin && dir < 0 && hasNumeric && Number.isFinite(min) && parseFloat(raw) <= min) {
          inp.value = '';
          emit();
          return;
        }

        if (autoAtMin && dir > 0 && !hasNumeric) {
          const seed = Number.isFinite(min) ? min : 0;
          inp.value = seed;
          emit();
          return;
        }

        const val  = hasNumeric ? parseFloat(raw) : (Number.isFinite(min) ? min : 0);
        const next = val + dir * step;
        if (next < min || next > max) return;
        inp.value = next;
        emit();
      };
    }

    function attachHold(btn, stepFn) {
      let holdTimer = null;
      let holdInterval = null;
      function start(e) {
        e.preventDefault();
        stepFn();
        holdTimer = setTimeout(() => {
          holdInterval = setInterval(stepFn, 80);
        }, 400);
      }
      function stop() {
        clearTimeout(holdTimer);
        clearInterval(holdInterval);
        holdTimer = holdInterval = null;
      }
      btn.addEventListener('mousedown', start);
      btn.addEventListener('mouseup', stop);
      btn.addEventListener('mouseleave', stop);
      btn.addEventListener('touchstart', start, { passive: false });
      btn.addEventListener('touchend', stop);
      btn.addEventListener('touchcancel', stop);
    }

    const ctrls = document.createElement('div');
    ctrls.className = 'infield-num-ctrls';

    const up = document.createElement('button');
    up.type = 'button';
    up.className = 'infield-num-btn';
    up.setAttribute('aria-label', 'Increase value');
    up.innerHTML = '&#9650;';
    attachHold(up, makeStep(1));

    const down = document.createElement('button');
    down.type = 'button';
    down.className = 'infield-num-btn';
    down.setAttribute('aria-label', 'Decrease value');
    down.innerHTML = '&#9660;';
    attachHold(down, makeStep(-1));

    ctrls.appendChild(up);
    ctrls.appendChild(down);
    wrap.appendChild(ctrls);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  initNumSteppers(document);
});

// -- Custom tooltip (data-tip) -------------------------------------------------
(function () {
  let _tip = null;
  function tip() {
    if (!_tip) { _tip = document.createElement('div'); _tip.id = 'app-tooltip'; document.body.appendChild(_tip); }
    return _tip;
  }
  document.addEventListener('mouseover', e => {
    const el = e.target.closest('[data-tip]');
    if (el) { tip().textContent = el.dataset.tip; tip().classList.add('tip-on'); }
    else     { tip().classList.remove('tip-on'); }
  });
  document.addEventListener('mousemove', e => {
    const t = tip();
    if (!t.classList.contains('tip-on')) return;
    const G = 14;
    let x = e.clientX + G, y = e.clientY + G;
    if (x + t.offsetWidth  > window.innerWidth)  x = e.clientX - t.offsetWidth  - G;
    if (y + t.offsetHeight > window.innerHeight) y = e.clientY - t.offsetHeight - G;
    t.style.left = x + 'px'; t.style.top = y + 'px';
  });
})();
