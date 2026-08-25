// Shared UI helpers -- included by all app pages

// -- Polling helpers -----------------------------------------------------------
let _pollPauseDepth = 0;
function pausePoll()  { _pollPauseDepth++; }
function resumePoll() { _pollPauseDepth = Math.max(0, _pollPauseDepth - 1); }
function startPolling(loadFn, intervalMs = 2500) {
  setInterval(() => { if (_pollPauseDepth === 0) loadFn(); }, intervalMs);
}

// -- Auth constants ------------------------------------------------------------

const LS_ADMIN = 'sr_admin_token';
const LS_USER  = 'sr_user_token';

let _authCtx = null;

function isAdmin() { return _authCtx?.is_admin === true; }
function isUser()  { return _authCtx?.is_user === true; }
// Matches the mobile breakpoint in style.css (portrait <=720px, or landscape phones up to 930px).
function isMobileViewport() {
  return window.matchMedia('(max-width: 720px), (max-width: 930px) and (orientation: landscape)').matches;
}
// True when the admin is actively in admin view (not switched to runner view). On mobile there's
// no runner-view toggle -- an admin always runs at the highest privilege available there.
function isAdminMode() {
  if (!isAdmin()) return false;
  if (isMobileViewport()) return true;
  return (sessionStorage.getItem('sr_view') || 'admin') === 'admin';
}
function userToken()  { return localStorage.getItem(LS_USER)  || null; }
function adminToken() { return localStorage.getItem(LS_ADMIN) || null; }

// -- Auth headers --------------------------------------------------------------

function authHeaders(extra = {}) {
  const h = { ...extra };
  const at = adminToken();
  const ut = userToken();
  if (at) h['X-Admin-Token'] = at;
  if (ut) h['X-User-Token']  = ut;
  // Admin previewing runner view: ask the server for the exact player payload so no GM-only data
  // ever reaches the browser. Presentation-only -- the admin token above still authorizes the call.
  if (isAdmin() && !isAdminMode()) h['X-Runner-View'] = '1';
  return h;
}

// -- Matrix decking nav gate ---------------------------------------------------
// Hides the Deck Workshop and Matrix Run nav links for players with no claimed PC that has
// deck skills, matching the same access check used by the deck-workshop interrupt overlay.
// (RTGs and Hosts stay visible -- they are read-only topology references for everyone.)
// Admins are exempt in BOTH views: an admin in runner view has no *claimed* PC (claiming
// needs a user token), but the decking pages let them pick any eligible decker, so never hide.
async function _applyMatrixRunNavGate() {
  if (isAdmin()) return;
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
      document.querySelectorAll('nav a[href="matrix-run.html"], nav a[href="deck-workshop.html"]')
        .forEach(a => { a.style.display = 'none'; });
    }
  } catch (_) {}
}

// -- MATRIX nav group ----------------------------------------------------------
// Folds the matrix-related flat nav links (RTGs, Hosts, Deck Workshop, Matrix Run and the
// GM-only Matrix Designer) into a single "MATRIX" dropdown group. Built here -- rather than in
// each page's static nav -- so every page shares one definition and the new Hosts link appears
// even on pages whose static nav predates it. The menu reveals on hover/focus (CSS) or click.
function _buildMatrixNavGroup() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('.nav-group')) return;

  const childDefs = [
    { href: 'manage-rtgs.html',     label: 'RTGs' },
    { href: 'matrix-hosts.html',    label: 'Hosts' },
    { href: 'matrix-designer.html', label: 'Matrix Designer', gmOnly: true },
    { href: 'deck-workshop.html',   label: 'Deck Workshop' },
    { href: 'matrix-run.html',      label: 'Matrix Run' },
    { href: 'matrix-aars.html',     label: 'Host AARs', gmOnly: true },
  ];

  const here = window.location.pathname;
  const onMatrixPage = childDefs.some(d => here.endsWith(d.href));

  const group = document.createElement('div');
  group.className = 'nav-group' + (onMatrixPage ? ' active' : '');
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'nav-group-toggle';
  toggle.setAttribute('aria-haspopup', 'true');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.innerHTML = 'MATRIX <span class="nav-caret">&#9662;</span>';
  const menu = document.createElement('div');
  menu.className = 'nav-group-menu';
  childDefs.forEach(d => {
    const a = document.createElement('a');
    a.href = d.href;
    a.textContent = d.label;
    let cls = d.gmOnly ? 'gm-only' : '';
    if (here.endsWith(d.href)) cls += (cls ? ' ' : '') + 'active';
    if (cls) a.className = cls;
    menu.appendChild(a);
  });
  group.appendChild(toggle);
  group.appendChild(menu);

  // Click toggles the menu (CSS already opens it on hover / keyboard focus).
  toggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = group.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('click', (e) => {
    if (!group.contains(e.target)) {
      group.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Splice the group in where the first flat matrix link sat, then drop the flats.
  const flats = childDefs
    .map(d => nav.querySelector(`a[href="${d.href}"]`))
    .filter(Boolean);
  if (flats.length) {
    nav.insertBefore(group, flats[0]);
    flats.forEach(a => a.remove());
  } else {
    nav.appendChild(group);
  }
}

// -- DOSSIER nav link -----------------------------------------------------------
// Play Sheet (renamed Dossier) used to live buried inside the CHARACTERS dropdown -- fine on
// desktop, but it's the one page people actually need mid-session on a phone, so it gets its own
// flat, always-visible link instead. Built centrally (like the *NavGroup functions below) so every
// page's nav gets it in the same spot without hand-editing ~20 static <nav> blocks. Inserted right
// before Organizations, i.e. World State -> Dossier -> Organizations -> ...; falls back to
// appending at the end of nav if a page's nav has no Organizations link to anchor on.
// Also abbreviates "Organizations" to "Orgs" below the mobile breakpoint (matches
// isMobileViewport()'s breakpoint in this file) -- adding Dossier to an already-wrapping mobile
// nav needed the space back from somewhere, and Organizations was the longest label in the row.
function _buildDossierNavLink() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('a[href="play-sheet.html"]')) return;

  const here = window.location.pathname;
  const a = document.createElement('a');
  a.href = 'play-sheet.html';
  a.textContent = 'Dossier';
  if (here.endsWith('play-sheet.html')) a.className = 'active';
  const orgsLink = nav.querySelector('a[href="manage-organizations.html"]');
  if (orgsLink) {
    nav.insertBefore(a, orgsLink);
    orgsLink.innerHTML = '<span class="nav-full">Organizations</span><span class="nav-abbr">Orgs</span>';
  } else {
    nav.appendChild(a);
  }
}

// -- CHARACTERS nav group ------------------------------------------------------
// Folds the flat "Characters" link into a "CHARACTERS" dropdown: Known Persons (the registry) +
// New Runner (the character-builder). Built centrally so every page shares one definition; New
// Runner is visible to all users. Play Sheet/Hardcopy used to live here too -- Play Sheet (now
// Dossier) is its own flat link now (_buildDossierNavLink above), and Hardcopy is gone entirely
// now that Dossier's own Export Official PDF button covers what it did.
function _buildCharactersNavGroup() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('.nav-group--chars')) return;
  const anchor = nav.querySelector('a[href="manage-characters.html"]');
  if (!anchor) return;

  const childDefs = [
    { href: 'manage-characters.html', label: 'Known Persons' },
    { href: 'character-builder.html', label: 'New Runner' },
  ];
  const here = window.location.pathname;
  const onCharsPage = childDefs.some(d => here.endsWith(d.href));

  const group = document.createElement('div');
  group.className = 'nav-group nav-group--chars' + (onCharsPage ? ' active' : '');
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'nav-group-toggle';
  toggle.setAttribute('aria-haspopup', 'true');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.innerHTML = 'CHARACTERS <span class="nav-caret">&#9662;</span>';
  const menu = document.createElement('div');
  menu.className = 'nav-group-menu';
  childDefs.forEach(d => {
    const a = document.createElement('a');
    a.href = d.href;
    a.textContent = d.label;
    if (here.endsWith(d.href)) a.className = 'active';
    menu.appendChild(a);
  });
  group.appendChild(toggle);
  group.appendChild(menu);

  toggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = group.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('click', (e) => {
    if (!group.contains(e.target)) {
      group.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Remove any flat "Dossier Intake"/"Builder" links FIRST -- before the group (whose menu also
  // links to the builder) is inserted, so the "New Runner" menu item is not swept up too.
  nav.querySelectorAll('a[href="character-builder.html"]').forEach(a => a.remove());
  // Splice the group where the flat Characters link sat, then drop the flat Characters link.
  nav.insertBefore(group, anchor);
  anchor.remove();
}

// -- ADMIN CONTROL nav group ---------------------------------------------------
// Folds Downtime, Sourcebooks and Tokens into one "ADMIN CONTROL" dropdown. Unlike MATRIX/
// CHARACTERS, none of these have a guaranteed pre-existing flat link on every page (Downtime
// used to be injected by _injectAuthLabel(), Sourcebooks is brand new), so every child is built
// fresh from childDefs rather than relying on one always being present to fold in. The group
// itself is visible to everyone -- Tokens is where a player renames their own token -- while
// Downtime and Sourcebooks are individually gm-only.
function _buildAdminNavGroup() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('.nav-group--admin')) return;

  const childDefs = [
    { href: 'manage-downtime.html',    label: 'Downtime',    gmOnly: true },
    { href: 'manage-sourcebooks.html', label: 'Sourcebooks', gmOnly: true },
    { href: 'manage-archetypes.html',  label: 'Archetypes',  gmOnly: true },
    { href: 'manage-tokens.html',      label: 'Tokens' },
  ];

  const here = window.location.pathname;
  const onAdminPage = childDefs.some(d => here.endsWith(d.href));

  const group = document.createElement('div');
  group.className = 'nav-group nav-group--admin' + (onAdminPage ? ' active' : '');
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'nav-group-toggle';
  toggle.setAttribute('aria-haspopup', 'true');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.innerHTML = 'ADMIN CONTROL <span class="nav-caret">&#9662;</span>';
  const menu = document.createElement('div');
  menu.className = 'nav-group-menu';
  childDefs.forEach(d => {
    const a = document.createElement('a');
    a.href = d.href;
    a.textContent = d.label;
    let cls = d.gmOnly ? 'gm-only' : '';
    if (here.endsWith(d.href)) cls += (cls ? ' ' : '') + 'active';
    if (cls) a.className = cls;
    menu.appendChild(a);
  });
  group.appendChild(toggle);
  group.appendChild(menu);

  toggle.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = group.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
  });
  document.addEventListener('click', (e) => {
    if (!group.contains(e.target)) {
      group.classList.remove('open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });

  // Drop any pre-existing flat links for these three pages (some older static navs still have
  // them), inserting the group where the first one sat so position stays stable; otherwise
  // append to the end of the nav, matching where Downtime/Tokens used to land.
  const flats = childDefs
    .map(d => nav.querySelector(`a[href="${d.href}"]`))
    .filter(Boolean);
  if (flats.length) {
    nav.insertBefore(group, flats[0]);
    flats.forEach(a => a.remove());
  } else {
    nav.appendChild(group);
  }
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

    _buildDossierNavLink();
    _buildMatrixNavGroup();
    _buildCharactersNavGroup();
    _buildAdminNavGroup();
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
  // Add Dossier Intake (SR2 character builder) link right after Characters, for all users.
  if (nav && !nav.querySelector('[href="character-builder.html"]')) {
    const b = document.createElement('a');
    b.href = 'character-builder.html';
    b.textContent = 'Dossier Intake';
    if (window.location.pathname.endsWith('character-builder.html')) b.className = 'active';
    const charsLink = nav.querySelector('a[href="manage-characters.html"]');
    if (charsLink) nav.insertBefore(b, charsLink.nextSibling);
    else nav.appendChild(b);
  }
  // Downtime, Sourcebooks and Tokens are added by _buildAdminNavGroup() instead of here.

  // Bottom-right fixed label
  const label = document.createElement('div');
  label.id = 'auth-label';
  const role = isAdmin() ? (isAdminMode() ? 'ADMIN' : 'RUNNER') : 'RUNNER';
  const tokenLabel = _authCtx.token_label ? `${_authCtx.token_label} // ` : '';
  label.style.cssText =
    'position:fixed;bottom:10px;right:14px;z-index:500;font-family:var(--font);' +
    'font-size:.7rem;letter-spacing:1px;color:var(--auth-label);pointer-events:none;';
  label.textContent = `[${tokenLabel}${role}]`;

  // Admin+user: show the runner-view toggle -- but not on mobile, where isAdminMode()
  // always runs at the highest privilege and there's no preview-as-runner control.
  if (_authCtx.is_admin && !isMobileViewport()) {
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
    if (!isAdminMode()) {
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

/** Format a nuyen amount for display. Three separately-maintained copies of this (play-sheet.html,
 *  gear-picker.js, character-builder.html) had quietly drifted to different formats (prefix vs.
 *  suffix, with/without a pinned locale) -- this is the one canonical version. */
function money(n) {
  return '¥' + (Number(n) || 0).toLocaleString('en-US');
}

/** HTML-escape a string for safe insertion into HTML text and quoted HTML attributes.
 *  Never interpolate data into inline JavaScript handlers; HTML entities are decoded before
 *  those handlers are compiled. Use data attributes and addEventListener instead. */
function esc(s) {
  return String(s ?? '')
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;')
    .replace(/"/g,'&quot;')
    .replace(/'/g,'&#39;')
    .replace(/`/g,'&#96;');
}

/** Flash an alert banner inside the given element. Pass noScroll to leave the page's scroll
 *  position untouched (e.g. for actions triggered from inside a modal, where jumping the
 *  background page to reveal the banner is disorienting rather than helpful). */
function showAlert(el, msg, isErr, noScroll) {
  el.textContent = msg;
  el.className = `alert show ${isErr ? 'alert-err' : 'alert-ok'}`;
  if (!noScroll) el.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Show a styled confirmation dialog. Returns a Promise<boolean>.
 * okLabel  - label for the confirm button (default 'Confirm')
 * okClass  - CSS class for the confirm button (default 'btn-green' -- the affirmative "yes")
 *
 * Button-color convention (app-wide): the affirmative primary is GREEN and Cancel is RED.
 * Destructive confirms therefore read "Confirm" (green) / "Cancel" (red) rather than a red
 * "Delete". Callers that need an amber/cyan action primary may still pass okClass explicitly.
 */
function showConfirm(message, okLabel = 'Confirm', okClass = 'btn-green') {
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
            <button id="_sharedConfirmOk" class="btn btn-green" style="min-width:90px"></button>
            <button id="_sharedConfirmCancel" class="btn btn-red">Cancel</button>
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
 *         inputType='text', placeholder='', min=null, max=null }
 */
// opts.options (string[]), when given, renders a <select> of those choices instead of a free-text
// <input> -- used for pick-one prompts like "which active skill is this Activesoft loaded with?".
function showPrompt(message, defaultVal = '', opts = {}) {
  const okLabel     = opts.okLabel     || 'OK';
  const okClass     = opts.okClass     || 'btn-green';
  const title       = opts.title       || '>> INPUT REQUIRED';
  const inputType   = opts.inputType   || 'text';
  const placeholder = opts.placeholder || '';
  const options     = opts.options;
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
    const okBtn   = document.getElementById('_sharedPromptOk');
    const cancel  = document.getElementById('_sharedPromptCancel');

    // The field node is cached/reused across calls; swap it between <input> and <select> as needed
    // so a previous call's kind doesn't leak into this one.
    let field = document.getElementById('_sharedPromptInput');
    const wantSelect = Array.isArray(options) && options.length > 0;
    if (wantSelect && field.tagName !== 'SELECT') {
      const sel = document.createElement('select');
      sel.id = '_sharedPromptInput';
      sel.style.marginBottom = '22px';
      field.replaceWith(sel); field = sel;
    } else if (!wantSelect && field.tagName !== 'INPUT') {
      const inp = document.createElement('input');
      inp.id = '_sharedPromptInput'; inp.type = 'text';
      inp.style.marginBottom = '22px';
      field.replaceWith(inp); field = inp;
    }

    titleEl.textContent = title;
    msgEl.textContent   = message;
    if (wantSelect) {
      field.innerHTML = options.map(o => `<option value="${esc(o)}">${esc(o)}</option>`).join('');
      field.value = defaultVal && options.includes(defaultVal) ? defaultVal : options[0];
    } else {
      field.type = inputType;
      // Optional numeric bounds / max length -- reset every call (the input node is cached and reused).
      if (opts.max != null) field.max = String(opts.max); else field.removeAttribute('max');
      if (opts.min != null) field.min = String(opts.min); else field.removeAttribute('min');
      if (opts.maxLength != null) field.maxLength = opts.maxLength; else field.removeAttribute('maxlength');
      field.placeholder = placeholder;
      field.value = defaultVal == null ? '' : String(defaultVal);
    }
    okBtn.textContent   = okLabel;
    okBtn.className     = `btn ${okClass}`;
    pausePoll();
    overlay.style.display = 'flex';
    setTimeout(() => { field.focus(); if (field.select) field.select(); }, 30);

    function cleanup(result) {
      resumePoll();
      overlay.style.display = 'none';
      okBtn.removeEventListener('click', onOk);
      cancel.removeEventListener('click', onCancel);
      overlay.removeEventListener('click', onBackdrop);
      field.removeEventListener('keydown', onKey);
      resolve(result);
    }
    function onOk()       { cleanup(field.value); }
    function onCancel()   { cleanup(null); }
    function onBackdrop(e){ if (e.target === overlay) cleanup(null); }
    function onKey(e) {
      if (e.key === 'Enter')  { e.preventDefault(); cleanup(field.value); }
      if (e.key === 'Escape') { e.preventDefault(); cleanup(null); }
    }

    okBtn.addEventListener('click', onOk);
    cancel.addEventListener('click', onCancel);
    overlay.addEventListener('click', onBackdrop);
    field.addEventListener('keydown', onKey);
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


// -- Matrix helpers ------------------------------------------------------------

// Hacking Pool = (Intelligence + floor(MathSPU/2) + MPCP) / 3, rounded down. A Math SPU adds half
// its rating (rounded down) to Intelligence for this pool only. Single source of truth for the
// frontend; canonical backend mirror is app/services/matrix_engine.py hacking_pool().
function computeHackingPool(intelligence, mpcp, mathSpu = 0) {
  const intel = Math.max(0, parseInt(intelligence, 10) || 0);
  const brain = Math.max(0, parseInt(mpcp, 10) || 0);
  const spu   = Math.max(0, parseInt(mathSpu, 10) || 0);
  return Math.floor((intel + Math.floor(spu / 2) + brain) / 3);
}


// -- Gear catalog helpers -------------------------------------------------------
// Shared by character-builder.html's chargen shop and gear-picker.js/play-sheet.html's post-chargen
// purchases, so both convert a catalog item into the same owned-gear-line shape and cost the same
// item the same way, without maintaining separate copies of the rules.

// Parse a leading number out of a value that may be a number, a formula string, a range
// ("15,000 - 60,000"), or null. Returns 0 when nothing numeric is present.
function parseNum(v) {
  if (typeof v === 'number') return v;
  if (typeof v !== 'string') return 0;
  const m = v.replace(/,/g, '').match(/-?\d+(\.\d+)?/);
  return m ? Number(m[0]) : 0;
}

// Pull a named row out of an item's stats:[[label,value],...] array (vehicles, cyberdecks).
function statVal(item, key) {
  const row = ((item && item.stats) || []).find(s => Array.isArray(s) && String(s[0]).toLowerCase() === key.toLowerCase());
  return row ? (parseNum(row[1]) || 0) : 0;
}
function vehicleStatBody(item) { return statVal(item, 'body'); }

// gear-picker.js's onPurchase entries come back tagged with the picker's own tab key (e.g.
// "cyberware", "matrix") -- map each to the owned-gear bucket / makeGearLine catalog name it
// actually belongs under. Shared by play-sheet.html and character-builder.html, the two hosts that
// mount the picker.
const GEAR_BUCKET =        { weapons:'weapons', armor:'armor', cyberware:'cyber', bioware:'bio', gear:'gear', matrix:'matrix', foci:'foci', vehicles:'vehicles' };
const GEAR_LINE_CATALOG =  { weapons:'weapons', armor:'armor', cyberware:'cyberware', bioware:'bioware', gear:'gear', matrix:'gear', foci:'foci', vehicles:'vehicles' };

// Convert a catalog item into the shape stored on a character's gear.{cyber,bio,weapons,armor,gear,
// vehicles} lines (character-builder.html:makeGearLine). grade is cyberware-only (bioware has no
// grades) and defaults to Standard -- callers that let the player pick a grade at purchase time
// (gear-picker.js) pass the chosen grade through explicitly.
function makeGearLine(item, catalogName, grade) {
  if (catalogName === 'cyberware') {
    const line = { n: item.n, sub: item.cat || '', grade: grade || 'Standard', baseEss: parseNum(item.ess), baseCost: parseNum(item.cost), src: item.src };
    if (item.cat === 'other') line.noGrade = true;   // software chips (skillsofts) carry no cyber grade
    if (item.soft) line.soft = item.soft;            // skillsoft type: 'active' | 'knowledge' | 'language'
    if (item.skillBonus) line.skillBonus = item.skillBonus;   // e.g. Math SPU: +floor(Rating/2) to matching skills
    if (item.mods) line.mods = item.mods;            // fixed attribute bonuses (e.g. Wired Reflexes: +Reaction, +Init dice)
    if (item.modsPer) line.modsPer = item.modsPer;   // per-rating attribute bonuses (e.g. Muscle Replacement: +Str/+Qui per level)
    if (item.poolTbl) line.poolTbl = item.poolTbl;   // dice-pool bonuses by rating (Task / Hacking / Combat)
    if (item.rated) {
      line.rated = true;
      line.maxRating = Number(item.maxRating) || 1;
      if (item.minRating) line.minRating = Number(item.minRating);
      line.rating = Number(item.minRating) || 1;
      line.essUnit = parseNum(item.ess);
      line.costUnit = parseNum(item.cost);
      if (Array.isArray(item.essTbl)) line.essTbl = item.essTbl.slice();
      if (Array.isArray(item.costTbl)) line.costTbl = item.costTbl.slice();
    }
    return line;
  }
  const line = { n: item.n, sub: item.sub || item.cat || '', cost: parseNum(item.cost), src: item.src };
  if (catalogName === 'bioware') {
    line.ess = parseNum(item.ess);
    if (item.mods) line.mods = item.mods;
    if (item.modsPer) line.modsPer = item.modsPer;
    if (item.poolTbl) line.poolTbl = item.poolTbl;
    if (item.rated) {
      line.rated = true;
      line.maxRating = Number(item.maxRating) || 1;
      if (item.minRating) line.minRating = Number(item.minRating);
      line.rating = Number(item.minRating) || 1;
      line.essUnit = parseNum(item.ess);
      line.costUnit = parseNum(item.cost);
      if (Array.isArray(item.essTbl)) line.essTbl = item.essTbl.slice();
      if (Array.isArray(item.costTbl)) line.costTbl = item.costTbl.slice();
      if (item.capBody) line.capBody = true;
    }
  }
  if ((catalogName === 'gear' || catalogName === 'weapons' || catalogName === 'armor') && item.rated) {
    line.rated = true;
    line.maxRating = Number(item.maxRating) || 1;
    line.rating = 1;
    if (item.costUnit != null) line.costUnit = Number(item.costUnit);
    if (Array.isArray(item.costTbl)) line.costTbl = item.costTbl.slice();
    if (Array.isArray(item.rateLabels)) line.rateLabels = item.rateLabels.slice();
  }
  if (item.cat === 'deck') line.mpcp = statVal(item, 'MPCP');
  if (catalogName === 'vehicles') { line.body = vehicleStatBody(item); line.rigger = false; }
  return line;
}

// Current nuyen cost of an owned gear line (rated weapons/armor/gear use their rating's costTbl slot).
// Rating is clamped into [1, maxRating] before indexing costTbl -- defends against a corrupted or
// out-of-range stored rating landing on an undefined table slot (or, worse, silently falling
// through to the flat costUnit*r multiply with an absurd r).
function gearLineCost(g) {
  if (!g.rated) return Number(g.cost) || 0;
  const r = Math.max(1, Math.min(Number(g.rating) || 1, Math.max(1, Number(g.maxRating) || 1)));
  if (Array.isArray(g.costTbl) && g.costTbl[r - 1] != null) return Number(g.costTbl[r - 1]) || 0;
  return (Number(g.costUnit) || 0) * r;
}

// -- Cyberware grade/Essence/cost math ------------------------------------------
// character-builder.html (chargen) and play-sheet.html (post-chargen Manage Cyberware/Buy Gear)
// each need "what does this cyberware line cost in Essence/nuyen at its grade and rating" -- this
// used to be two independently-maintained implementations that had quietly drifted (unclamped vs.
// clamped rating; whether add-on options get graded with the base or added after). One shared
// version here, each page supplies its own grade-multiplier table (e.g. {Standard:{ess:1,nuyen:1},
// Alpha:{ess:0.8,nuyen:2}}) since that table's shape/extra fields (chargen's book-gating) are
// page-specific, but the actual math never should be.

// Rating clamped into [minRating, maxRating] -- same defensive reasoning as gearLineCost above.
function clampedRating(g) {
  const lo = Number(g.minRating) || 1;
  return Math.max(lo, Math.min(Number(g.rating) || lo, Math.max(lo, Number(g.maxRating) || lo)));
}
// Pre-grade Essence cost at the line's (clamped) rating, including add-on options' Essence --
// options are graded together with the base cost, not added on afterward ungraded.
function cyberBaseEss(g) {
  let base;
  if (!g.rated) base = Number(g.baseEss) || 0;
  else {
    const lo = Number(g.minRating) || 1, r = clampedRating(g);
    base = (Array.isArray(g.essTbl) && g.essTbl[r - lo] != null) ? (Number(g.essTbl[r - lo]) || 0) : (Number(g.essUnit) || 0) * r;
  }
  return base + (g.options || []).reduce((s, o) => s + (Number(o.ess) || 0), 0);
}
// Pre-grade nuyen cost at the line's (clamped) rating, including add-on options' cost.
function cyberBaseCost(g) {
  let base;
  if (!g.rated) base = Number(g.baseCost) || 0;
  else {
    const lo = Number(g.minRating) || 1, r = clampedRating(g);
    base = (Array.isArray(g.costTbl) && g.costTbl[r - lo] != null) ? (Number(g.costTbl[r - lo]) || 0) : (Number(g.costUnit) || 0) * r;
  }
  return base + (g.options || []).reduce((s, o) => s + (Number(o.cost) || 0), 0);
}
// Grade-adjusted Essence: rounds UP to 2 decimals, with a 0.05 floor once any Essence is actually
// spent (SR2's minimum meaningful Essence cost) -- a plain multiply can round an Alpha-grade item
// below that floor.
function gradeEssenceCost(baseEss, essMult) {
  // The tiny epsilon keeps binary floating-point noise (e.g. 3*0.8 === 2.4000000000000004) from
  // pushing an exact value like 2.40 over the ceiling into 2.41.
  const v = Math.ceil((Number(baseEss) || 0) * essMult * 100 - 1e-9) / 100;
  return (Number(baseEss) || 0) > 0 ? Math.max(0.05, v) : 0;
}
function gradeNuyenCost(baseCost, nuyenMult) {
  return Math.round((Number(baseCost) || 0) * nuyenMult);
}
// Final Essence/nuyen cost of an owned cyberware line. gradeTable maps grade name -> {ess, nuyen}
// multipliers; g.noGrade items (e.g. skillsoft chips) skip grading entirely. Named gradedCyber* --
// not effCyberEss/effCyberCost -- because character-builder.html defines its own 1-arg wrappers
// under those exact names that close over its GRADES table and delegate to these; giving this
// function the same name character-builder wraps it under would make that wrapper call itself.
function gradedCyberEssence(g, gradeTable) {
  const base = cyberBaseEss(g);
  if (g.noGrade) return base;
  const mult = (gradeTable[g.grade || 'Standard'] || gradeTable.Standard).ess;
  return gradeEssenceCost(base, mult);
}
function gradedCyberCost(g, gradeTable) {
  const base = cyberBaseCost(g);
  if (g.noGrade) return base;
  const mult = (gradeTable[g.grade || 'Standard'] || gradeTable.Standard).nuyen;
  return gradeNuyenCost(base, mult);
}

// -- SR2 dice-pool formulas ------------------------------------------------------
// character-builder.html (chargen) and play-sheet.html (live play) each need these same five
// pool formulas and had drifted into separately-maintained copies. The formula lives here so it
// can't drift again; each page still gathers its own inputs (attribute totals, which
// bonuses/penalties apply, whether a prerequisite like "owns a cyberdeck" or "knows Sorcery" is
// met) and calls these with plain numbers -- that gating logic is page-specific (chargen's
// state.gear vs. the live sheet's CHAR.gear) and stays where it is.
function combatPoolFormula(quickness, intelligence, willpower, bonus) {
  return Math.floor(((Number(quickness)||0) + (Number(intelligence)||0) + (Number(willpower)||0)) / 2) + (Number(bonus) || 0);
}
function hackingPoolFormula(intelligence, mpcp, bonus) {
  return Math.floor(((Number(intelligence)||0) + (Number(mpcp)||0)) / 3) + (Number(bonus) || 0);
}
function controlPoolFormula(reactionValue, vcrLevel) {
  return (Number(reactionValue) || 0) + (Number(vcrLevel) || 0) * 2;
}
function astralPoolFormula(intelligence, willpower, charisma) {
  return Math.floor(((Number(intelligence)||0) + (Number(willpower)||0) + (Number(charisma)||0)) / 2);
}
function spellPoolFormula(intelligence, willpower, magicRating, bonus) {
  return Math.floor(((Number(intelligence)||0) + (Number(willpower)||0) + (Number(magicRating)||0)) / 3) + (Number(bonus) || 0);
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

// -- Custom tooltip (data-tip) -- appears after a short hover delay (Task 4) -------------------
(function () {
  const DELAY_MS = 1500;                 // hover this long before the tip appears (avoids flicker)
  let _tip = null, _timer = null, _target = null, _mx = 0, _my = 0;
  function tip() {
    if (!_tip) { _tip = document.createElement('div'); _tip.id = 'app-tooltip'; document.body.appendChild(_tip); }
    return _tip;
  }
  function place() {
    const t = tip(); const G = 14;
    let x = _mx + G, y = _my + G;
    if (x + t.offsetWidth  > window.innerWidth)  x = _mx - t.offsetWidth  - G;
    if (y + t.offsetHeight > window.innerHeight) y = _my - t.offsetHeight - G;
    t.style.left = Math.max(2, x) + 'px'; t.style.top = Math.max(2, y) + 'px';
  }
  function hide() {
    if (_timer) { clearTimeout(_timer); _timer = null; }
    _target = null;
    tip().classList.remove('tip-on');
  }
  document.addEventListener('mouseover', e => {
    const el = e.target.closest('[data-tip]');
    if (el === _target) return;            // still over the same tipped element -- nothing to do
    hide();                                // moved to a new target (or off one): reset + restart
    if (el && el.dataset.tip) {
      _target = el;
      _timer = setTimeout(() => {
        const t = tip();
        t.textContent = el.dataset.tip;
        t.classList.add('tip-on');
        place();
      }, DELAY_MS);
    }
  });
  document.addEventListener('mousemove', e => {
    _mx = e.clientX; _my = e.clientY;
    if (tip().classList.contains('tip-on')) place();
  });
  // A stale tip during a scroll is distracting -- drop it and let the hover re-arm.
  window.addEventListener('scroll', hide, true);

  // Touch fallback: mouseover never fires on touch devices, so data-tip content
  // would otherwise be unreachable. Tap shows it immediately (no hover delay);
  // tapping the same element again, or tapping elsewhere, dismisses it.
  // Disabled on mobile viewports -- a tap on a clickable card (e.g. the
  // world-state stat cards) surfaced the tooltip and ate the tap, requiring a
  // second tap just to dismiss it before the card's own action worked.
  document.addEventListener('touchstart', e => {
    if (typeof isMobileViewport === 'function' && isMobileViewport()) return;
    const touch = e.touches[0];
    _mx = touch.clientX; _my = touch.clientY;
    const el = e.target.closest('[data-tip]');
    const wasOn = _target === el && tip().classList.contains('tip-on');
    hide();
    if (el && el.dataset.tip && !wasOn) {
      _target = el;
      const t = tip();
      t.textContent = el.dataset.tip;
      t.classList.add('tip-on');
      place();
    }
  }, { passive: true });
})();
