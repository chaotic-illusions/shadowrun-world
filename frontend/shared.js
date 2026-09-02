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
// Play Sheet (renamed Dossier) lives in the CHARACTERS dropdown on desktop (_buildCharactersNavGroup
// below) -- but .nav-group dropdowns are hidden entirely on mobile (style.css), and Dossier is the
// one page people actually need mid-session on a phone, so it ALSO gets this flat, mobile-only
// link (style.css hides this copy above the mobile breakpoint so desktop doesn't show it twice).
// Built centrally (like the *NavGroup functions below) so every page's nav gets it in the same spot
// without hand-editing ~20 static <nav> blocks. Inserted right before Organizations, i.e. World
// State -> Dossier -> Organizations -> ...; falls back to appending at the end of nav if a page's
// nav has no Organizations link to anchor on. Also abbreviates "Organizations" to "Orgs" below the
// mobile breakpoint (matches isMobileViewport()'s breakpoint in this file) -- adding Dossier to an
// already-wrapping mobile nav needed the space back from somewhere, and Organizations was the
// longest label in the row.
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
// New Runner (the character-builder) + Dossier (the play sheet). Built centrally so every page
// shares one definition; New Runner and Dossier are visible to all users. Hardcopy is gone
// entirely now that Dossier's own Export Official PDF button covers what it did. Dossier ALSO
// gets its own flat top-level link (_buildDossierNavLink above) -- that copy is mobile-only (see
// style.css's nav > a[href="play-sheet.html"] rules) since .nav-group dropdowns are hidden
// entirely on mobile and Dossier needs to stay reachable there; this menu item is its desktop home.
function _buildCharactersNavGroup() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('.nav-group--chars')) return;
  const anchor = nav.querySelector('a[href="manage-characters.html"]');
  if (!anchor) return;

  const childDefs = [
    { href: 'manage-characters.html', label: 'Known Persons' },
    { href: 'character-builder.html', label: 'New Runner' },
    { href: 'play-sheet.html', label: 'Dossier' },
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

  // Remove any flat character-builder.html link FIRST -- before the group (whose menu also
  // links to the builder) is inserted, so the "New Runner" menu item is not swept up too.
  nav.querySelectorAll('a[href="character-builder.html"]').forEach(a => a.remove());
  // Splice the group where the flat Characters link sat, then drop the flat Characters link.
  nav.insertBefore(group, anchor);
  anchor.remove();
}

// -- TOOLS nav group -----------------------------------------------------------
// Folds Combat (the combat reference), Downtime, Sourcebooks, Archetypes and Tokens into one
// "TOOLS" dropdown. Every label is one word on purpose: a two-word item wraps at the menu's
// min-width, and a taller menu drags a scrollbar onto the page (see .nav-group-menu in style.css).
// Named TOOLS rather than the old "ADMIN CONTROL" because the group is not all admin: Tokens is
// where a player renames their own token, and Combat Reference is a lookup table both sides read.
// The GM-only children carry their own gm-only class instead.
//
// Unlike MATRIX/CHARACTERS, none of these have a guaranteed pre-existing flat link on every page
// (Downtime used to be injected by _injectAuthLabel(), Sourcebooks and Combat Reference are
// newer), so every child is built fresh from childDefs rather than relying on one always being
// present to fold in.
function _buildToolsNavGroup() {
  const nav = document.querySelector('header nav');
  if (!nav || nav.querySelector('.nav-group--tools')) return;

  const childDefs = [
    { href: 'combat-reference.html',   label: 'Combat' },
    { href: 'manage-downtime.html',    label: 'Downtime',    gmOnly: true },
    { href: 'manage-sourcebooks.html', label: 'Sourcebooks', gmOnly: true },
    { href: 'manage-archetypes.html',  label: 'Archetypes',  gmOnly: true },
    { href: 'manage-tokens.html',      label: 'Tokens' },
  ];

  const here = window.location.pathname;
  const onToolsPage = childDefs.some(d => here.endsWith(d.href));

  const group = document.createElement('div');
  group.className = 'nav-group nav-group--tools' + (onToolsPage ? ' active' : '');
  const toggle = document.createElement('button');
  toggle.type = 'button';
  toggle.className = 'nav-group-toggle';
  toggle.setAttribute('aria-haspopup', 'true');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.innerHTML = 'TOOLS <span class="nav-caret">&#9662;</span>';
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

  // Drop any pre-existing flat links for these pages (some older static navs still have them),
  // inserting the group where the first one sat so position stays stable; otherwise append to
  // the end of the nav, matching where Downtime/Tokens used to land.
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
    _buildToolsNavGroup();
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
  // Add New Runner (SR2 character builder) link right after Characters, for all users.
  if (nav && !nav.querySelector('[href="character-builder.html"]')) {
    const b = document.createElement('a');
    b.href = 'character-builder.html';
    b.textContent = 'New Runner';
    if (window.location.pathname.endsWith('character-builder.html')) b.className = 'active';
    const charsLink = nav.querySelector('a[href="manage-characters.html"]');
    if (charsLink) nav.insertBefore(b, charsLink.nextSibling);
    else nav.appendChild(b);
  }
  // Downtime, Sourcebooks and Tokens are added by _buildToolsNavGroup() instead of here.

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

/**
 * Show a read-only reference popup -- a rules-lookup card (spell/power/etc. mechanics) rather than
 * a data-entry dialog, so unlike showConfirm/showPrompt it has no Promise/result: just open, and the
 * player closes it themselves (X, backdrop click, or Escape). Its own self-contained overlay, wider
 * and taller than the confirm/prompt ones since reference text runs longer, with internal scrolling
 * so a long spell/power entry never grows past the viewport.
 * bodyHtml is trusted, pre-escaped markup the caller builds (mirrors gear-picker.js's inspector
 * pattern of esc()-ing every dynamic field before assembling the block) -- never pass raw user input.
 */
function showInfoModal(title, bodyHtml) {
  let overlay = document.getElementById('_sharedInfoOverlay');
  if (!overlay) {
    overlay = document.createElement('div');
    overlay.id = '_sharedInfoOverlay';
    overlay.className = 'modal-overlay';
    overlay.style.zIndex = '700';
    overlay.innerHTML = `
      <div style="background:var(--bg-card);border:1px solid #1a2a1a;border-top:2px solid var(--cyan);
                  padding:28px 32px;width:100%;max-width:520px;max-height:80vh;display:flex;flex-direction:column">
        <div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px;margin-bottom:14px">
          <div id="_sharedInfoTitle" style="font-size:.75rem;letter-spacing:2px;color:var(--cyan)"></div>
          <button id="_sharedInfoClose" class="row-x" title="Close">&#10005;</button>
        </div>
        <div id="_sharedInfoBody" style="font-size:.8rem;color:var(--text-bright);line-height:1.6;overflow-y:auto"></div>
      </div>`;
    document.body.appendChild(overlay);
  }
  document.getElementById('_sharedInfoTitle').textContent = title;
  document.getElementById('_sharedInfoBody').innerHTML = bodyHtml;
  const closeBtn = document.getElementById('_sharedInfoClose');
  pausePoll();
  overlay.style.display = 'flex';
  function cleanup() {
    resumePoll();
    overlay.style.display = 'none';
    closeBtn.removeEventListener('click', onClose);
    overlay.removeEventListener('click', onBackdrop);
    document.removeEventListener('keydown', onKey);
  }
  function onClose()     { cleanup(); }
  function onBackdrop(e) { if (e.target === overlay) cleanup(); }
  function onKey(e)      { if (e.key === 'Escape') cleanup(); }
  closeBtn.addEventListener('click', onClose);
  overlay.addEventListener('click', onBackdrop);
  document.addEventListener('keydown', onKey);
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

// ---- Ownership/prerequisite battery -- shared by play-sheet.html's post-chargen purchaseGear()
// and character-builder.html's chargen chargenBuyGear(), so both hosts enforce identical rules
// instead of chargen silently drifting from (or lacking) what play-sheet already checks. Every
// function here takes `gear` as an explicit argument (never a global CHAR/state), so either host
// can call it against its own gear object.
// Cybergun implants need a cyberarm to sit in -- SR2 allows at most one per arm (2 total),
// and never more than the number of arm-slot Cyber Limbs actually owned.
const CYBERGUN_NAMES = new Set(['Cybergun: Hold-Out Pistol','Cybergun: Light Pistol','Cybergun: Machine Pistol','Cybergun: SMG','Cybergun: Heavy Pistol','Cybergun: Shotgun']);
function ownedCybergunCount(gear){ return ((gear.cyber)||[]).filter(g => CYBERGUN_NAMES.has(g.n)).length; }

// ---- Ownership rules from the SR2 gear-quantity audit ----
// Armor, Cyberware, and Bioware are singular installs by default (one body slot each) -- buying a
// second copy of the identical catalog item is blocked. Weapons, Gear, Foci, Vehicles, and Matrix
// have no default cap. The tables below carry the named exceptions from that audit.
const SINGULAR_CATEGORIES = new Set(['armor','cyberware','bioware']);
// name -> hard count cap for items allowed multiples with a flat limit. Infinity = the cap/dedup is
// handled by bespoke logic elsewhere in purchaseGear (skillsofts, Reflex Recorder, Cybergun).
const OWNERSHIP_CAP = {
  'Ear Modification': 8,
  'Fingertip Compartment': 3,
  'Retractable Spur': 2,
  'Spur': 2,
  'Datasoft': Infinity,
  'Activesoft (General)': Infinity, 'Activesoft (Concentration)': Infinity, 'Activesoft (Specialization)': Infinity,
  'Knowsoft (General)': Infinity, 'Knowsoft (Concentration)': Infinity, 'Knowsoft (Specialization)': Infinity,
  'Linguasoft': Infinity,
  'Reflex Recorder (Concentration)': Infinity, 'Reflex Recorder (General)': Infinity,
  'Cybergun: Hold-Out Pistol': Infinity, 'Cybergun: Light Pistol': Infinity, 'Cybergun: Machine Pistol': Infinity,
  'Cybergun: SMG': Infinity, 'Cybergun: Heavy Pistol': Infinity, 'Cybergun: Shotgun': Infinity,
};
// Simple Replacement Limb and Cyber Limb occupy the same 4 limb slots (2 arms + 2 legs) and are
// mutually exclusive per slot -- capped as a combined group. Each purchase is tagged with a specific
// slot (Left/Right Arm/Leg -- play-sheet.html's assignLimbSlot prompts for it, character-builder.html
// auto-assigns the first free one) so arm-only/leg-only prerequisites elsewhere can tell which is
// which. Only a full Cyber Limb has "internal modification slots" per its own catalog text -- a
// Simple Replacement Limb explicitly has none -- so arm/leg-specific PREREQ checks below only ever
// count Cyber Limb, while the combined 4-slot cap counts both (they still occupy the same body slot).
const LIMB_GROUP = new Set(['Simple Replacement Limb','Cyber Limb']);
const LIMB_SLOTS = ['Left Arm','Right Arm','Left Leg','Right Leg'];
function ownedLimbSlots(gear, onlyName){
  return ((gear.cyber)||[]).filter(g => LIMB_GROUP.has(g.n) && (!onlyName || g.n === onlyName)).map(g => g.slot).filter(Boolean);
}
function ownedLimbGroupCount(gear){ return ownedLimbSlots(gear).length; }
function ownedCyberLimbSlotCount(gear, kind){ return ownedLimbSlots(gear, 'Cyber Limb').filter(s => s.endsWith(kind)).length; }
function ownedMagLimbSystemCount(gear){ return ((gear.cyber)||[]).filter(g => g.n === 'Magnetic Cyberlimb System').length; }

// ---- Cyberware/bioware "families": same body slot spread across separate catalog rows per
// level/rating-band (e.g. Boosted Reflexes Level 1/2/3). Buying a higher-ranked member of a family
// you already own replaces the old line in place; buying an equal-or-lower one is blocked. See
// familyReplaceOrBlock(). Order is ascending capability, not alphabetical.
const FAMILY_GROUPS = {
  cryptoCircuit: { bucket:'cyber', order: ['Crypto Circuit HD Level 1-4','Crypto Circuit HD Level 5-7','Crypto Circuit HD Level 8-9','Crypto Circuit HD Level 10'] },
  scrambleBreaker: { bucket:'cyber', order: ['Scramble Breaker HD Level 1-4','Scramble Breaker HD Level 5-7','Scramble Breaker HD Level 8'] },
  skillwirePlus: { bucket:'cyber', order: ['Skillwire Plus (R1-3)','Skillwire Plus (R4-6)','Skillwire Plus (R7-9)'] },
  damageCompensator: { bucket:'bio', order: ['Damage Compensator (R1-2)','Damage Compensator (R3-5)','Damage Compensator (R6-9)'] },
};
const FAMILY_BY_NAME = new Map();
Object.entries(FAMILY_GROUPS).forEach(([key, fam]) => fam.order.forEach((name, idx) => FAMILY_BY_NAME.set(name, { key, idx, bucket: fam.bucket })));
function hasFamily(gear, key){
  const fam = FAMILY_GROUPS[key];
  return (gear[fam.bucket]||[]).some(g => { const f = FAMILY_BY_NAME.get(g.n); return f && f.key === key; });
}
// Mutates gear (removes the outclassed line) only when the purchase is allowed to proceed as an
// upgrade. Returns a skip-reason string if blocked, else null.
function familyReplaceOrBlock(item, gear){
  const fam = FAMILY_BY_NAME.get(item.n);
  if (!fam) return null;
  const list = gear[fam.bucket] || [];
  const owned = list.find(g => { const f = FAMILY_BY_NAME.get(g.n); return f && f.key === fam.key; });
  if (!owned) return null;
  if (fam.idx <= FAMILY_BY_NAME.get(owned.n).idx) return `${item.n} (already own ${owned.n})`;
  gear[fam.bucket] = list.filter(g => g !== owned);
  return null;
}

// ---- Base-item prerequisites and mutual exclusions, from the CSV's explicit "Requires X" /
// "Blocks Y" / "incompatible with" notes only -- nothing inferred beyond what was written, except two
// points confirmed directly with the user: Dermal Sheath L3 vs. Dermal Plating is bidirectional, and
// Activesoft/Knowsoft's Softlink(+Skillwires) requirement is enforced even though the CSV review
// itself didn't flag it (the catalog's own item text states it). Hydraulic Jack's cyberleg
// requirement was found the same way (catalog text: "Must be installed in a cyberleg").
function hasItem(gear, name){ return ((gear.cyber)||[]).some(g => g.n === name) || ((gear.bio)||[]).some(g => g.n === name); }
// Cyberdecks live in gear.matrix (bucket "matrix", catalog cat:"deck"), not gear.cyber/gear.bio, so
// hasItem() (scoped to cyber/bio only) can't see them -- a dedicated matrix-scanning check instead.
function ownsCyberdeck(gear){ return ((gear.matrix)||[]).some(g => g.sub === 'Cyberdeck'); }
const EYE_ITEMS = ['Rangefinder','Video Link','Optical Magnification','Electronic Magnification','Retinal Clock','Protective Covers','Eye Datajack','Optical Scanning Datajack','Optical Scanning Datajack Emitter','Eye Light System','BrightLight Addition','Eye Dart','Eye Gun','Laser Tracker','Tool Laser','Laser Designator'];
const PREREQ = {
  ...Object.fromEntries(EYE_ITEMS.map(n => [n, g => hasItem(g,'Cyber Eye Replacement')])),
  'Tracking Mount': g => hasItem(g,'Cyber Eye Replacement') && hasItem(g,'Laser Designator') && ownedCyberLimbSlotCount(g,'Arm') > 0,
  'External Mount': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Smartlink': g => hasItem(g,'Display Link'),
  'Reflex Trigger': g => hasItem(g,'Wired Reflexes'),
  'Improved Hand Razors': g => hasItem(g,'Hand Razors') || hasItem(g,'Retractable Hand Razors'),
  'BrightLight One-Shot Flash-pak': g => hasItem(g,'BrightLight Addition'),
  'Video Link Internal Transmitter': g => hasItem(g,'Video Link'),
  'Video Link External Transmitter': g => hasItem(g,'Video Link'),
  'Video Link External Recorder': g => hasItem(g,'Video Link'),
  'Hearing Amplification': g => hasItem(g,'Cyber Ear Replacement') && hasItem(g,'Ear Modification'),
  'Spatial Recognizer': g => hasItem(g,'Cyber Ear Replacement') && hasItem(g,'Ear Modification'),
  'Balance Augmenter': g => hasItem(g,'Cyber Ear Replacement') && hasItem(g,'Ear Modification'),
  'Sense Link Internal Transmitter': g => hasItem(g,'Sense Link'),
  'Sense Link Receiver': g => hasItem(g,'Sense Link'),
  'Sense Link External Transmitter': g => hasItem(g,'Sense Link'),
  'Sense Link External Recorder': g => hasItem(g,'Sense Link'),
  'Dermal Plating': g => hasItem(g,'Cybertorso'),
  'Dermal Sheath': g => hasItem(g,'Cybertorso'),
  'Body Plating: Soft Armor (per level)': g => hasItem(g,'Cybertorso'),
  'Body Plating: Hard Armor (per level)': g => hasItem(g,'Cybertorso'),
  'Cyberarm Gyromount': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Hand Blade (Retractable)': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Shock Hand': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Cyberarm Taser': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'CyberSquirt': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Cyber Limb — Built-In Smartlink': g => ownedCyberLimbSlotCount(g,'Arm') > 0,
  'Foot Anchor': g => ownedCyberLimbSlotCount(g,'Leg') > 0,
  'Hydraulic Jack': g => ownedCyberLimbSlotCount(g,'Leg') > 0,
  'Orientation System': g => ownedCyberLimbSlotCount(g,'Arm') > 0 || ownedCyberLimbSlotCount(g,'Leg') > 0,
  'Cyber Limb — Built-In Device': g => ownedCyberLimbSlotCount(g,'Arm') > 0 || ownedCyberLimbSlotCount(g,'Leg') > 0,
  'Reaction Enhancer': g => hasItem(g,'Wired Reflexes'),
  'Activesoft (General)': g => hasItem(g,'Softlink') && hasFamily(g,'skillwirePlus'),
  'Activesoft (Concentration)': g => hasItem(g,'Softlink') && hasFamily(g,'skillwirePlus'),
  'Activesoft (Specialization)': g => hasItem(g,'Softlink') && hasFamily(g,'skillwirePlus'),
  'Knowsoft (General)': g => hasItem(g,'Softlink'),
  'Knowsoft (Concentration)': g => hasItem(g,'Softlink'),
  'Knowsoft (Specialization)': g => hasItem(g,'Softlink'),
  'Linguasoft': g => hasItem(g,'Softlink'),
};
const EXCLUDES = {
  'Boosted Reflexes': g => hasItem(g,'Vehicle Control Rig') || hasItem(g,'Wired Reflexes'),
  'Vehicle Control Rig': g => hasItem(g,'Boosted Reflexes'),
  'Wired Reflexes': g => hasItem(g,'Boosted Reflexes'),
  'Reaction Enhancer': g => hasItem(g,'Move-by-Wire System'),
  'Dermal Plating': g => hasItemAtRating(g,'Dermal Sheath',3) || hasOrthoskinAtRating(g,3),
  'Trauma Damper': g => hasItem(g,'Pain Editor'),
  'Pain Editor': g => hasItem(g,'Trauma Damper'),
};
// Shared duplicate-purchase check for "same item, different configuration is fine" cases (skillsoft
// chip, reflex recorder, Kit/Shop/Facility type, focus target, Power Focus rating) -- true if
// gear[bucket] already owns `name` with every [field, value, mode] tuple matching: 'ci' compares
// strings case-insensitively, 'num' compares numerically, anything else is a strict ===.
function dupeCheck(gear, bucket, name, checks){
  return (gear[bucket] || []).some(g => g.n === name && checks.every(([field, value, mode]) => {
    if (mode === 'ci') return String(g[field] || '').toLowerCase() === String(value || '').toLowerCase();
    if (mode === 'num') return Number(g[field]) === Number(value);
    return g[field] === value;
  }));
}
function hasItemAtRating(gear, name, minR){
  return ((gear.cyber)||[]).some(g => g.n === name && (Number(g.rating)||1) >= minR) ||
         ((gear.bio)||[]).some(g => g.n === name && (Number(g.rating)||1) >= minR);
}
function hasOrthoskinAtRating(gear, minR){ return hasItemAtRating(gear, 'Orthoskin', minR); }
// Orthoskin and Dermal Sheath only become incompatible with Dermal Plating at Rating 3 specifically
// (their own catalog text) -- not a plain EXCLUDES entry since the trigger is rating-conditional, not
// "owned at all". Checked both on a fresh purchase (ownershipBlocked) and an in-place upgrade
// (play-sheet.html's upgradeExistingSingular), same as every other rating change now that both go
// through re-buying.
// A rank-specific mutual exclusion: raising `itemName` to `targetRating` (>= minRating) is blocked
// if `excludesName` is already owned (any rating). Mirrors EXCLUDES' opposite-direction check
// (Dermal Plating -> hasItemAtRating(Dermal Sheath/Orthoskin, 3)) for the other two items in this
// three-way exclusion.
function ratingExclusionBlocked(itemName, targetRating, minRating, excludesName, gear){
  return targetRating >= minRating && hasItem(gear, excludesName) ? `${itemName} R${minRating} (incompatible with ${excludesName})` : null;
}
function orthoskinRatingBlocked(targetRating, gear){ return ratingExclusionBlocked('Orthoskin', targetRating, 3, 'Dermal Plating', gear); }
function dermalSheathRatingBlocked(targetRating, gear){ return ratingExclusionBlocked('Dermal Sheath', targetRating, 3, 'Dermal Plating', gear); }
// Combines the default-singular/quantity-cap rules with the prerequisite/exclusion tables above.
// PREREQ/EXCLUDES apply to every item, family members included (e.g. Boosted Reflexes is itself a
// family member AND excludes the VCR family) -- only the *default-singular quantity cap* is skipped
// for family members, since familyReplaceOrBlock (called separately) governs their ownership count.
function ownershipBlocked(cat, item, gear, rating){
  if (item.n === 'Orthoskin') {
    const orthoBlock = orthoskinRatingBlocked(rating || 1, gear);
    if (orthoBlock) return orthoBlock;
  }
  if (item.n === 'Dermal Sheath') {
    const sheathBlock = dermalSheathRatingBlocked(rating || 1, gear);
    if (sheathBlock) return sheathBlock;
  }
  // Cyberdeck Component (Hitcher Jacks, Vidscreen Display, ...) needs an owned Cyberdeck to plug
  // into -- matched by `sub`, not by name, so any future catalog addition is covered automatically
  // (same bespoke-check style as the Cybergun-needs-a-cyberarm rule below, rather than a PREREQ
  // entry, since PREREQ's hasItem() can't see gear.matrix at all).
  if (item.sub === 'Cyberdeck Component' && !ownsCyberdeck(gear)) return `${item.n} (needs an owned Cyberdeck)`;
  const prereq = PREREQ[item.n];
  if (prereq && !prereq(gear)) return `${item.n} (prerequisite not met)`;
  const excl = EXCLUDES[item.n];
  if (excl && excl(gear)) return `${item.n} (blocked by an incompatible item already installed)`;
  if (FAMILY_BY_NAME.has(item.n)) return null;
  if (LIMB_GROUP.has(item.n)) {
    return ownedLimbGroupCount(gear) >= 4 ? `${item.n} (max 4 limbs)` : null;
  }
  if (item.n === 'Magnetic Cyberlimb System') {
    const limbs = ownedLimbGroupCount(gear);
    if (limbs === 0) return `${item.n} (needs a Cyber Limb or Simple Replacement Limb)`;
    const cap = Math.min(4, limbs);
    return ownedMagLimbSystemCount(gear) >= cap ? `${item.n} (max ${cap} for your limbs)` : null;
  }
  if (!SINGULAR_CATEGORIES.has(cat)) return null;
  const cap = OWNERSHIP_CAP[item.n];
  if (cap === Infinity) return null;   // dedup/cap handled by bespoke logic below
  const bucket = GEAR_BUCKET[cat] || cat;
  const owned = gear[bucket] || [];
  if (cap === undefined) return owned.some(g => g.n === item.n) ? `${item.n} (already owned)` : null;
  return owned.filter(g => g.n === item.n).length >= cap ? `${item.n} (max ${cap})` : null;
}

// SR2 spell shorthand decoded to plain English -- shared by play-sheet.html's spell/power info
// popup (openSpellInfo) and character-builder.html's chargen spell browser (spellStatChips), so a
// player sees "Mana"/"Line of Sight"/"Sustained" in both places rather than a bare "M"/"LOS"/"S"
// only someone who already knows the rules can decode.
const SPELL_TYPE_LABEL = { M: 'Mana', P: 'Physical' };
const SPELL_RANGE_LABEL = { T: 'Touch', LOS: 'Line of Sight', Self: 'Self' };
const SPELL_DURATION_LABEL = { I: 'Instant', S: 'Sustained', P: 'Permanent' };
// Spell-learning nuyen cost by drain category (not karma). Availability = Force/acquisition time.
// Required test (Sorcery, TN = Force x2) is reference-only -- the app never rolls it. Shared by
// play-sheet.html's Manage Magic (Learn a Spell pricing) and the spell info popup's Drain line.
const SPELL_DRAIN_TABLE = {
  L: { label: 'Light',    nuyenPerForce: 50,   hours: 24 },
  M: { label: 'Moderate', nuyenPerForce: 100,  hours: 48 },
  S: { label: 'Serious',  nuyenPerForce: 500,  hours: 72 },
  D: { label: 'Deadly',   nuyenPerForce: 1000, days: 7 },
};
function spellDrainCode(spell){
  const m = /([LMSD])\s*$/.exec((spell && spell.drn) || '');
  return m ? m[1] : null;
}
function spellCostInfo(spell, force){
  const tier = SPELL_DRAIN_TABLE[spellDrainCode(spell)];
  if (!tier) return null;
  const f = Math.max(1, Number(force) || 1);
  const time = tier.days ? `${tier.days} day${tier.days === 1 ? '' : 's'}` : `${tier.hours} hours`;
  return { label: tier.label, force: f, nuyen: tier.nuyenPerForce * f, avail: `${f}/${time}`, tn: f * 2 };
}
// ---- Spell/power reference popup body-builders (showInfoModal) -- shared by play-sheet.html's
// openSpellInfo/openPowerInfo (owned = a CHAR.spells/.adept_powers line) and character-builder.html's
// chargenOpenSpellInfo/chargenOpenPowerInfo (owned = a state.spells/.powers line, same {name,force}/
// {name,lvl} shape) so the actual HTML only needs to exist once. `sp`/`pw` is the raw catalog item
// (desc/effect/target/etc. already in plain English -- this just surfaces it instead of leaving it
// locked in JSON only an admin token could read); `owned` is optional (omit to preview an
// unowned/not-yet-bought item, e.g. before buying a spell post-chargen).
function statRow(label, value){ return value ? `<div class="ps-stat-row"><span class="k">${esc(label)}</span><span class="v">${value}</span></div>` : ''; }
function spellInfoBody(sp, owned){
  if (!sp) return '<p class="empty-state">No catalog data for this spell.</p>';
  const info = owned ? spellCostInfo(sp, owned.force) : null;
  const effectList = (sp.effect || []).map(e => `<li>${esc(String(e))}</li>`).join('');
  return [
    owned ? statRow('Force (cast)', esc(String(owned.force ?? '—'))) : '',
    statRow('Category', esc(sp.cat || '—')),
    statRow('Type', esc(SPELL_TYPE_LABEL[sp.typ] || sp.typ || '—')),
    statRow('Range', esc(SPELL_RANGE_LABEL[sp.rng] || sp.rng || '—')),
    statRow('Duration', esc(SPELL_DURATION_LABEL[sp.dur] || sp.dur || '—')),
    statRow('Target', esc(sp.target || '—')),
    statRow('Area', esc(sp.area || '—')),
    statRow('Damage', sp.dmg ? esc(sp.dmg) : ''),
    statRow('Drain', `${esc(sp.drn || '—')}${info ? ` — <b>${esc(info.label)}</b> (Sorcery TN ${info.tn})` : (spellDrainCode(sp) ? ` — <b>${esc(SPELL_DRAIN_TABLE[spellDrainCode(sp)].label)}</b>` : '')}`),
    sp.desc ? `<p class="dim-meta mt-6">${esc(sp.desc)}</p>` : '',
    effectList ? `<ul class="mt-6" style="padding-left:18px">${effectList}</ul>` : '',
    `<p class="dim-meta mt-6">${esc(sp.src || '')}${sp.pg ? ` p.${esc(String(sp.pg))}` : ''}</p>`,
  ].join('');
}
function powerInfoBody(pw, owned){
  if (!pw) return '<p class="empty-state">No catalog data for this power.</p>';
  const effectList = (pw.effect || []).map(e => `<li>${esc(String(e))}</li>`).join('');
  return [
    owned && pw.rated ? statRow('Level', esc(String(owned.lvl ?? 1))) : '',
    statRow('Cost', pw.pp ? esc(String(pw.pp)) + ' PP' : ''),
    statRow('Activation', esc(pw.act || '—')),
    pw.tiers ? statRow('Tiers', esc(pw.tiers)) : '',
    pw.desc ? `<p class="dim-meta mt-6">${esc(pw.desc)}</p>` : '',
    effectList ? `<ul class="mt-6" style="padding-left:18px">${effectList}</ul>` : '',
    `<p class="dim-meta mt-6">${esc(pw.src || '')}${pw.pg ? ` p.${esc(String(pw.pg))}` : ''}</p>`,
  ].join('');
}

// ---- Situational bonuses too narrow/one-off to model as a first-class field -- CSV said to note
// them on the character instead. Shared by play-sheet.html's appendCharNote (writes CHAR.notes) and
// character-builder.html's chargenAppendNote (writes state.notes) -- each host supplies its own
// dedup/append wrapper since they write to different places, but the lookup table of what to say is
// identical either way.
const SITUATIONAL_NOTES = {
  'Olfactory Booster': g => `Olfactory Booster R${g.rating||1}: +1 die to smell Perception per level, +1 die to taste per 3 levels.`,
  'Hydraulic Jack': g => `Hydraulic Jack R${g.rating||1}: leaping distance/height x${g.rating||1}; falling-damage Power -${g.rating||1}.`,
  'Damage Compensator (R1-2)': g => `Damage Compensator R${g.rating}: ignore wound penalties (Physical and Stun) up to that level.`,
  'Damage Compensator (R3-5)': g => `Damage Compensator R${g.rating}: ignore wound penalties (Physical and Stun) up to that level.`,
  'Damage Compensator (R6-9)': g => `Damage Compensator R${g.rating}: ignore wound penalties (Physical and Stun) up to that level.`,
  // Just a note, not a mechanical piece of code -- both the actual damage-shifting effect and the
  // Damage-Compensator-threshold gate would need condition-monitor logic that doesn't exist yet.
  'Trauma Damper': () => `Trauma Damper: shifts one box of Physical damage to Stun instead, but only once an owned Damage Compensator's threshold has been exceeded (no effect without one). +2 TN to others' attempts to cause you pain. Incompatible with a Pain Editor.`,
  // Cyberware that's meant to grant a Weapons-table entry -- not auto-added there, just noted with
  // what it grants so it can be tracked by hand.
  'Hand Blade (Retractable)': () => `Hand Blade (Retractable): melee weapon, Reach 0, Damage (STR+3)L. Retracts into the limb when not in use.`,
  'Shock Hand': () => `Shock Hand: melee weapon, Reach 0, Damage 8S. Recharges between uses -- one strike per recharge.`,
  'Cyberarm Taser': () => `Cyberarm Taser: ranged weapon, Damage 8S. 10 charges before reload.`,
  'CyberSquirt': () => `CyberSquirt: ranged chemical injector, 10 shots of a chosen chemical/biological agent. Rigid armor reduces effect.`,
  'Cyberarm Gyromount': () => `Cyberarm Gyromount: 3 points Recoil Compensation for whatever weapon is mounted to it.`,
  'Toxin Extractor': g => `Toxin Extractor R${g.rating||1}: reduces blood-toxin attack Power by ${Math.floor((g.rating||1)/2)}.`,
  'Pathogenic Defense': g => `Pathogenic Defense R${g.rating||1}: +${g.rating||1} die resisting disease/allergens; reduces microbiological attack Power by ${Math.floor((g.rating||1)/2)}.`,
  'Nephritic Screen': () => `Nephritic Screen: +1 Body resisting toxins/pathogens; reduces blood-vectored toxin attack Power by 1.`,
  'Extended Volume': g => `Extended Volume R${g.rating||1}: +${[0,45,90,135][g.rating||1]||45}s breath-hold${(g.rating||1)>=3 ? ' (small stamina penalty at R3)' : ''}.`,
  // Activated/temporary, not a permanent mod -- applying it as an always-on attribute bonus would be
  // wrong (it only applies for 10-15 turns, then costs Stun Drain and fatigue).
  'Adrenal Pump': g => `Adrenal Pump R${g.rating||1}: on activation, ${g.rating===2?'+2 Quickness/+2 Strength/+1 Willpower/+4 Reaction':'+1 Quickness/+1 Strength/+1 Willpower/+2 Reaction'} for 10-15 turns, then Stun Drain and fatigue.`,
  // Knowledge/Language skills aren't tracked as a structured list on this sheet yet, so this bonus
  // has nowhere to attach -- noted instead of silently dropped.
  'Mnemonic Enhancer': g => `Mnemonic Enhancer R${g.rating||1}: +${Math.floor((g.rating||1)/2)} die to Knowledge/Language tests; -${g.rating||1} TN to recall tests.`,
  // Ballistic/Impact are wired into the Armor total (bioArmorBonus). The Body bonus described here is
  // specifically "for damage resistance tests," not a real Body attribute increase (unlike Cybertorso/
  // Cyberskull's flat +1 Body, which is a genuine structural replacement) -- noted rather than modeled
  // as a global attribute change that would also skew Encumbrance/karma costs.
  'Dermal Sheath': g => `Dermal Sheath R${g.rating||1}: +${g.rating||1} Body for damage-resistance tests only (armor already counted in the total).`,
  'Dermal Plating': g => `Dermal Plating R${g.rating||1}: +${g.rating||1} Body for damage-resistance tests only (armor already counted in the total).`,
  'Bone Lacing': g => `Bone Lacing R${g.rating||1} (${['Plastic','Aluminum','Titanium'][(g.rating||1)-1]||'Plastic'}): Unarmed Blow does (STR+${g.rating||1})M.`,
  'Orthoskin': g => (g.rating||1) >= 3 ? `Orthoskin R3: +TN to tactile Perception.` : '',
  // Weapon-granting cyberware not auto-added to the Weapons table (same treatment as Hand Blade/Shock
  // Hand/Cyberarm Taser/CyberSquirt above) -- noted with what it grants instead.
  'Hand Razors': () => `Hand Razors: Unarmed melee weapon, cyber-claws.`,
  'Retractable Hand Razors': () => `Retractable Hand Razors: Unarmed melee weapon, cyber-claws (concealable, retracts when not in use).`,
  'Improved Hand Razors': () => `Improved Hand Razors: Unarmed melee weapon, Damage (STR+2).`,
  'Spur': () => `Spur: melee weapon, Damage (STR+2), always extended.`,
  'Retractable Spur': () => `Retractable Spur: melee weapon, Damage (STR+2), retracts when not in use.`,
  'Oral Dart': () => `Oral Dart: ranged narcoject/toxin injector, 3 rounds, reload 1 min/dart, ammo x3 cost.`,
  'Oral Gun': () => `Oral Gun: ranged weapon, 4 rounds, reload 1 min/round, ammo x3 cost.`,
  'Oral Spur': () => `Oral Spur: melee weapon (tongue-mounted), extends/retracts as a free action.`,
  'Oral Whip': () => `Oral Whip: ranged melee weapon, Range 1m, Damage 6M.`,
  'Eye Dart': () => `Eye Dart: ranged narcoject/toxin injector, 1 round, reloads in 10 Combat Turns, ammo x3 cost.`,
  'Eye Gun': () => `Eye Gun: ranged weapon, 1 round (-1 damage, -1 recoil mod), reloads in 10 Combat Turns.`,
  'Tool Laser': () => `Tool Laser: Damage Code 4L beyond 1m; can't pierce Barrier Rating > 8.`,
  'Toxin Exhaler': () => `Toxin Exhaler: ranged toxin injector (Quickness Test to hit, +1 TN per half-meter, range capped at half unaugmented Body in meters).`,
  // Implanted lethal/self-destruct devices -- severe, non-obvious effects worth flagging clearly.
  'Kink Bomb': () => `Kink Bomb (Illegal): kills the wearer outright on detonation; can cause permanent neurological damage if it fails to kill.`,
  'Microbomb': () => `Microbomb: kills wearer and destroys identifying tissue, Power 8 Damage Level M blast.`,
  'Area Bomb': () => `Area Bomb: Power 10 Damage Level M blast beyond the wearer, -1 Power per meter of distance.`,
  'Cortex Bomb (Illegal)': () => `Cortex Bomb (Illegal): lethal explosive in a 1m radius, remote/signal/condition-triggered.`,
  // Resistance-test bonuses that have nowhere to attach (no toxin/pathogen/gas-attack mechanic on this
  // sheet) -- same treatment as Toxin Extractor/Pathogenic Defense/Nephritic Screen above.
  'Air Filtration': g => `Air Filtration R${g.rating||1}: opposes inhaled toxins with Rating ${g.rating||1}.`,
  'Blood Filtration': g => `Blood Filtration R${g.rating||1}: opposes blood-borne toxins with Rating ${g.rating||1}.`,
  'Ingested Toxin Filtration': g => `Ingested Toxin Filtration R${g.rating||1}: opposes ingested toxins with Rating ${g.rating||1}.`,
  'Tracheal Filter': g => `Tracheal Filter R${g.rating||1}: reduces gas/airborne attack Power by ${Math.floor((g.rating||1)/2)}.`,
  'Platelet Factory': () => `Platelet Factory: forces a clot against embolism/serious blood loss once daily; +1 TN to Body Tests per use (cumulative thrombosis risk).`,
  'Symbiotes': g => `Symbiotes R${g.rating||1}: heals in ${[90,70,50][(g.rating||1)-1]||90}% normal time${(g.rating||1)>=2 ? `; +${(g.rating||1)===2?50:100}% food intake` : ''}.`,
  'Suprathyroid Gland': () => `Suprathyroid Gland: requires roughly triple normal food/drink intake; tendency toward hyperactivity.`,
  // The -2 TN bonus has nowhere to attach (no attack-TN mechanic on this sheet); the Display Link
  // prerequisite is enforced separately in PREREQ.
  'Smartlink': () => `Smartlink: -2 TN on smartgun-equipped weapons.`,
  'External Mount': () => `External Mount: weapon mount, triple ammo cost for the external feed.`,
  'Articulate Arm': () => `Articulate Arm: 3 points Recoil Compensation for whatever weapon is mounted to it.`,
};

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
// Alpha:{ess:0.8,nuyen:3}}) since that table's shape/extra fields (chargen's book-gating) are
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
// Matrix Reaction/Initiative (VR2 "Response Increase"/"Initiative" rules, docs/vr2_rules.md
// L1273-1301/L1917-1926) -- ported from deck-workshop.html's inspector readout so play-sheet.html
// can show the same numbers for a jacked-in decker. Reality Filter adds an Initiative die but NOT
// Reaction (matches vr2_rules.md's Response Increase writeup); Tortoise decks ignore Response
// Increase's Reaction bonus entirely and cap Initiative at a flat 1D6.
function matrixReactionInitFormula(quickness, intelligence, deckType, respIncrease, realityFilter) {
  const ri = Number(respIncrease) || 0;
  const baseReaction = Math.ceil(((Number(quickness)||0) + (Number(intelligence)||0)) / 2);
  if (deckType === 'tortoise') return { matrixReaction: Math.max(1, Math.floor(baseReaction / 2)), initiativeDice: 1 };
  const effectiveRI = ri + (realityFilter ? 1 : 0);
  return { matrixReaction: baseReaction + ri * 2, initiativeDice: Math.max(1, 1 + effectiveRI + (deckType === 'hot' ? 1 : -1)) };
}

// -- SR2 weapon ranges ----------------------------------------------------------
// Range bands (metres) by weapon sub-type. Not in weapons.json, so they're looked up by class.
// Originally ported into play-sheet.html from tools/fill_sr2_sheet.py's RANGE_TABLE (still used
// for the PDF export); moved here when combat-reference.html needed the same bands, so the two
// pages can't drift -- same reasoning as the pool formulas above. Strength-based weapons
// (bows/thrown/crossbows) are computed from a strength passed in by the caller.
// Band target numbers are Short 4 / Medium 5 / Long 6 / Extreme 8.
const RANGE_TABLE = {
  'Hold-Out': ['0-5','6-15','16-30','31-50'], 'Hold-Out Pistol': ['0-5','6-15','16-30','31-50'],
  'Light Pistol': ['0-5','6-15','16-30','31-50'], 'Machine Pistol': ['0-5','6-15','16-30','31-50'],
  'Heavy Pistol': ['0-5','6-20','21-40','41-60'],
  'SMG': ['0-10','11-40','41-80','81-150'], 'Submachine Gun': ['0-10','11-40','41-80','81-150'],
  'Shotgun': ['0-10','11-20','21-50','51-100'],
  'Taser': ['0-5','6-10','11-12','13-15'],
  'Sport Rifle': ['0-30','31-60','61-150','151-300'],
  'Sniper Rifle': ['0-40','41-80','81-200','201-400'],
  'Assault Rifle': ['0-15','16-40','41-100','101-250'], 'Carbine': ['0-15','16-40','41-100','101-250'],
  'Light Machine Gun': ['0-20','21-40','41-80','81-150'],
  'Medium Machine Gun': ['0-40','41-150','151-300','301-500'],
  'Heavy Machine Gun': ['0-40','41-150','151-400','401-800'],
  'Assault Cannon': ['0-50','51-150','151-450','451-1300'],
  'Grenade Launcher': ['5-50','51-100','101-150','151-300'],
  'Missile Launcher': ['20-70','71-150','151-450','451-1500'],
  'Anti-Tank Guided Missile': ['20-350','351-750','751-1500','1501-5000'],
  'Mortar': ['150-300','301-1000','1001-4000','4001-6000'],
  'Laser Weapon': ['0-40','41-80','81-200','201-400'],
  'Vehicle Laser': ['0-50','51-150','151-450','451-1300'],
  'Light Anti-Armor Weapon': ['20-70','71-150','151-450','451-1500'],
  'Medium Anti-Armor Weapon': ['20-70','71-150','151-450','451-1500'],
  'Minigun': ['0-20','21-40','41-80','81-150'],
  'Sentry Gun': ['0-20','21-40','41-80','81-150'],
  'Surface-to-Air Missile': ['20-70','71-150','151-450','451-5000'],
  'Dart Pistol': ['0-5','6-15','16-30','31-50'], 'Dart Rifle': ['0-10','11-20','21-50','51-100'],
};
const NAME_RANGE = { 'Ballista Multi-Role Missile Launcher': ['20-100','101-500','501-2500','2501-5000'] };
const STR_RANGE_MULT = { Bow:[1,10,30,60], 'Throwing Knife':[1,2,3,5], Shuriken:[1,2,5,7], Grenade:[3,5,10,20], Thrown:[3,5,10,20] };
const CROSSBOW_MULT = { light:[2,8,20,40], medium:[3,12,30,50], heavy:[5,15,40,60] };

/** Strength-scaled bands, e.g. a Bow's [1,10,30,60] multipliers against Strength. */
function strRangeBands(mults, strength){
  const bands = []; let lo = 0;
  mults.forEach(m => { const hi = Math.max(0, Math.round((strength||0)*m)); bands.push(`${lo}-${hi}`); lo = hi + 1; });
  return bands;
}

// Condense "lo-hi" bands to a single "up to" number -- each band's floor is implied by the
// previous band's ceiling, so only Short keeps its own floor, and only when it's non-zero
// (indirect-fire weapons like grenade/missile launchers have a genuine minimum range). Matches
// tools/fill_sr2_sheet.py's _display_bands(), used for the same tables on the PDF export.
function displayBands(bands){
  return bands.map((band, i) => {
    const [lo, hi] = String(band).split('-');
    if (hi == null) return band;   // already a bare "-" placeholder
    return (i === 0 && lo !== '0') ? `${lo}-${hi}` : hi;
  });
}

/** Display bands for one weapon. `cat` is its weapons.json catalog row; `strength` only
 *  matters for the strength-scaled classes (bows, crossbows, thrown). */
function weaponRangeBands(w, cat, strength){
  let bands = NAME_RANGE[w.n] || RANGE_TABLE[cat.sub];
  if (!bands) {
    let mults = STR_RANGE_MULT[cat.sub];
    if (cat.sub === 'Crossbow') {
      const lname = (w.n || '').toLowerCase();
      const key = lname.includes('light') ? 'light' : lname.includes('heavy') ? 'heavy' : 'medium';
      mults = CROSSBOW_MULT[key];
    }
    if (mults) bands = strRangeBands(mults, strength);
  }
  return displayBands(bands || ['-','-','-','-']);
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
