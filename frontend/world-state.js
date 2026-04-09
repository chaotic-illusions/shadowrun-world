const API = '';
const YEAR_OFFSET = 24;  // years between real date and in-world date

let orgStore     = {};
let charMapStore = {};
let contactStore = [];   // raw contacts array, refreshed on loadAll
let nonNpcContactStore = {};  // merged contacts without character records, keyed by id
let locStore = {};              // location_id -> location object
let npcModalCharId = null;

// ── Archetype Edit Modal ──────────────────────────────────────
const ARCHETYPES = [
  { label: 'Street Samurai', cls: 'arch-samurai' },
  { label: 'Decker',         cls: 'arch-decker'  },
  { label: 'Rigger',         cls: 'arch-rigger'  },
  { label: 'Mage',           cls: 'arch-mage'    },
  { label: 'Shaman',         cls: 'arch-shaman'  },
  { label: 'Adept',          cls: 'arch-adept'   },
  { label: 'Custom',         cls: 'arch-custom'  },
];

let selectedArch = '';
let archModalCharId = null;

function selectArchOpt(label) {
  selectedArch = label;
  document.querySelectorAll('.arch-opt').forEach(el => {
    el.classList.toggle('arch-opt-selected', el.dataset.label === label);
  });
  const isCustom = label === 'Custom';
  const customInput = document.getElementById('archCustomInput');
  customInput.style.display = isCustom ? '' : 'none';
  if (isCustom) {
    if (!customInput.value) customInput.value = 'Hybrid';
    selectedArch = customInput.value;
    setTimeout(() => customInput.focus(), 30);
  }
}

function openArchModal(charId) {
  pausePoll();
  const current = charMapStore[charId]?.archetype || '';
  archModalCharId = charId;

  const named = ARCHETYPES.slice(0, -1).find(a => a.label.toLowerCase() === current.toLowerCase());
  const customInput = document.getElementById('archCustomInput');

  const archList = document.getElementById('archOptList');
  archList.innerHTML = '';
  ARCHETYPES.forEach(a => {
    const div = document.createElement('div');
    div.className = `arch-opt ${a.cls}`;
    div.dataset.label = a.label;
    div.textContent = a.label;
    div.addEventListener('click', () => selectArchOpt(a.label));
    archList.appendChild(div);
  });

  if (named) {
    selectedArch = named.label;
    customInput.style.display = 'none';
    customInput.value = '';
  } else {
    selectedArch = current || 'Hybrid';
    customInput.value = current || 'Hybrid';
    customInput.style.display = '';
  }

  document.querySelectorAll('.arch-opt').forEach(el => {
    el.classList.toggle('arch-opt-selected', el.dataset.label === (named?.label ?? 'Custom'));
  });

  document.getElementById('editModalTitle').textContent = 'Select Archetype';
  document.getElementById('editOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeEditModal() {
  resumePoll();
  document.getElementById('editOverlay').classList.remove('open');
  document.body.style.overflow = '';
  archModalCharId = null;
}

function editOverlayClick(e) {
  if (e.target === document.getElementById('editOverlay')) closeEditModal();
}

async function saveEditModal() {
  const val = selectedArch === 'Custom'
    ? document.getElementById('archCustomInput').value.trim()
    : selectedArch;
  if (archModalCharId && val !== (charMapStore[archModalCharId]?.archetype || '')) {
    await apiFetch(`${API}/characters/${archModalCharId}`, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({archetype: val || null})
    });
    loadAll();
  }
  closeEditModal();
}

// ── Tooltip definitions ───────────────────────────────────────
const PA_TIPS = {
  'Shadow':           'Unknown to the public — identity fully secure.',
  'Seen':             'Noticed — face has surfaced; word is starting to spread in certain circles.',
  'Recognized':       'Known — regularly recognized on the street or picked up in news feeds.',
  'In the Spotlight': 'Exposed — featured in media coverage; corp security may already have a file.',
  'Burned':           'Compromised — identity widely known; too hot to work openly without serious risk.',
};

const CONNECTION_TIPS = [
  '',
  'Connection 1 — Street-level only. Knows a handful of people; handles small-time requests with limited reach.',
  'Connection 2 — Neighborhood reach. Reliable within their own community; limited contacts outside it.',
  'Connection 3 — City-wide network. Can pull strings across Seattle and is trusted in their field.',
  'Connection 4 — Regional influence. Cross-sector contacts with access to restricted resources and information.',
  'Connection 5 — National reach. A major player operating in high-stakes circles with serious leverage.',
  'Connection 6 — Global or corporate-tier. Extraordinary access across borders — very few doors are closed.',
];

// ── Helpers ───────────────────────────────────────────────────
function tierLabel(n) {
  return ['','Street','Local','City','Regional','National','Global'][n] || `T${n}`;
}
function orgClass(t) { return `oc-${TYPE_GROUP[t] || 'other'}`; }

// ── Section collapse state ────────────────────────────────────
const collapsed = {};
function toggleSection(key) {
  // Ensure section is expanded and scroll to it
  const body = document.getElementById(`sec-body-${key}`);
  const head = document.getElementById(`sec-head-${key}`);
  if (body) body.style.display = '';
  collapsed[key] = false;
  if (head) head.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function toggleContactSections() {
  ['contacts', 'npcs'].forEach(key => {
    const body = document.getElementById(`sec-body-${key}`);
    if (body) body.style.display = '';
    collapsed[key] = false;
  });
  const head = document.getElementById('sec-head-contacts');
  if (head) head.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function toggleAllOrgs() {
  const orgKeys = ORG_ORDER.map(g => `org-${g}`)
    .filter(k => document.getElementById(`sec-body-${k}`));
  orgKeys.forEach(key => {
    const body = document.getElementById(`sec-body-${key}`);
    if (body) body.style.display = '';
    collapsed[key] = false;
  });
  const head = document.getElementById(`sec-head-org-${ORG_ORDER[0]}`);
  if (head) head.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ── Org description expand ────────────────────────────────────
const expandedOrgs = {};
function toggleOrgDesc(orgId) {
  expandedOrgs[orgId] = !expandedOrgs[orgId];
  const el  = document.getElementById(`oc-desc-${orgId}`);
  const btn = document.getElementById(`oc-xbtn-${orgId}`);
  if (el)  el.classList.toggle('oc-desc-expanded', expandedOrgs[orgId]);
  if (btn) btn.textContent = expandedOrgs[orgId] ? '[ collapse ]' : '[ expand ]';
}

// ── LTG Modal ─────────────────────────────────────────────────
function ratingClass(r) {
  const color = (r || '').split('-')[0].toLowerCase();
  return { blue:'r-blue', green:'r-green', orange:'r-orange', red:'r-red', black:'r-black' }[color] || 'r-green';
}

// ── Card Builders ─────────────────────────────────────────────
function buildOrgCard(org, orgMap) {
  const allyIds  = isAdminMode() ? (org.ally_ids  || []) : (org.revealed_ally_ids  || []);
  const enemyIds = isAdminMode() ? (org.enemy_ids || []) : (org.revealed_enemy_ids || []);
  const allies  = allyIds.map(id => orgMap[id]?.name).filter(Boolean);
  const enemies = enemyIds.map(id => orgMap[id]?.name).filter(Boolean);
  const longDesc = org.description && org.description.length > 160;
  return `
    <div class="org-card ${orgClass(org.org_type)}" onclick="openOrgEditModal(${org.id})" class="clickable" title="Click to edit">
      <div class="oc-head">
        <div class="oc-name">${esc(org.name)}</div>
        <div class="oc-tier">TIER ${org.tier} // ${tierLabel(org.tier)}</div>
      </div>
      <div class="oc-type">${esc(org.org_type || 'unclassified')}</div>
      ${org.headquarters ? `<div class="oc-hq">${esc(org.headquarters)}</div>` : ''}
      ${org.description
        ? `<div class="oc-desc" id="oc-desc-${org.id}">${esc(org.description)}</div>`
        : '<div class="oc-desc" style="color:#333">No public intel available.</div>'}
      ${longDesc ? `<div><button class="oc-expand-btn" id="oc-xbtn-${org.id}" onclick="event.stopPropagation();toggleOrgDesc(${org.id})">[ expand ]</button></div>` : ''}
      ${(allies.length || enemies.length) ? `
        <div class="oc-foot">
          ${allies.length  ? `<span class="rel-ally">▲ ALLIES: ${allies.map(esc).join(', ')}</span>` : ''}
          ${enemies.length ? `<span class="rel-enemy">▼ HOSTILE: ${enemies.map(esc).join(', ')}</span>` : ''}
        </div>` : ''}
    </div>`;
}

function archetypeClass(arch) {
  if (!arch) return 'arch-custom';
  const a = arch.toLowerCase();
  if (a.includes('samurai') || a.includes('street sam')) return 'arch-samurai';
  if (a.includes('decker'))   return 'arch-decker';
  if (a.includes('rigger'))   return 'arch-rigger';
  if (a.includes('shaman'))   return 'arch-shaman';
  if (a.includes('adept'))    return 'arch-adept';   // matches 'adept' and 'physical adept'
  if (a.includes('mage'))     return 'arch-mage';
  return 'arch-custom';
}

function editCharArchetype(charId) {
  openArchModal(charId);
}

function loyaltyDots(n, max) {
  return Array.from({length: max}, (_, i) =>
    `<span style="color:${i < n ? 'var(--amber)' : '#333'}">●</span>`
  ).join('');
}

// Merge raw contacts array: group by npc_id (or by name if no npc_id)
function mergeContacts(contacts) {
  const byNpc  = {};  // npc_id (int) -> merged
  const byName = {};  // name (lowercase) -> merged
  contacts.forEach(c => {
    const ownerEntry = { contact_id: c.id, owner_id: c.owner_id, loyalty: c.loyalty, connection: c.connection, is_active: c.is_active !== false };
    if (c.npc_id) {
      if (!byNpc[c.npc_id]) byNpc[c.npc_id] = { ...c, owners: [] };
      byNpc[c.npc_id].owners.push(ownerEntry);
    } else {
      const key = c.name.toLowerCase();
      if (!byName[key]) byName[key] = { ...c, owners: [] };
      byName[key].owners.push(ownerEntry);
    }
  });
  return [...Object.values(byNpc), ...Object.values(byName)];
}

// ── NPC Dossier Modal ─────────────────────────────────────────
function openNpcModal(charId) {
  const char = charMapStore[charId];
  if (!char || char.is_pc) return;
  pausePoll();
  npcModalCharId = charId;
  const race      = char.race || null;
  const archetype = char.archetype || null;
  const display   = char.title || archetype || null;
  const raceProf  = [race, display].filter(Boolean).join(' | ');
  const org = char.organization_id ? orgStore[char.organization_id] : null;

  document.getElementById('npcModalName').textContent = `Dossier // ${char.name}`;
  document.getElementById('npcModalBadge').innerHTML =
    raceProf ? `<span class="badge-race-prof">${esc(raceProf)}</span>` : '';

  const orgLine = `<div class="cc-org" style="margin-bottom:${char.nationality ? '4px' : '12px'}"><span class="cc-org-lbl">Affiliation</span><span class="cc-org-sep"> // </span>${org ? esc(org.name) : '[Unknown]'}</div>`;
  const nationalityLine = char.nationality
    ? `<div class="cc-org mb-12"><span class="cc-org-lbl">Nationality</span><span class="cc-org-sep"> // </span><span style="color:var(--text)">${esc(char.nationality)}</span></div>`
    : '';

  const contactSkills = (char.contact_skills || []);
  const isContact = contactStore.some(c => c.npc_id === charId);

  // Background: shown in player-visible section when show_background=true; GM section otherwise
  const revealBtn = char.background
    ? `<button class="npc-reveal-btn gm-only" onclick="toggleDataReveal(${charId},'show_background',${!!char.show_background})">${char.show_background ? '\u2299 Hide from Players' : '\u25cc Reveal to Players'}</button>`
    : '';
  const bgSection = char.background
    ? `<div class="npc-modal-section">
        <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:4px"><div class="npc-modal-sec-lbl" style="margin-bottom:0">Background</div>${revealBtn}</div>
        <div class="npc-modal-text">${esc(char.background)}</div>
      </div>`
    : '';
  const playerBg = char.show_background ? bgSection : '';
  const gmBg     = char.show_background ? '' : bgSection; // in GM section only when hidden from players

  document.getElementById('npcModalBody').innerHTML = `
    ${orgLine}
    ${nationalityLine}
    ${char.description ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Profile</div><div class="npc-modal-text">${esc(char.description)}</div></div>` : ''}
    ${playerBg}
    ${contactSkills.length && (isContact || isAdminMode()) ? `
      <div class="npc-modal-section">
        <div class="npc-modal-sec-lbl">Contact Services</div>
        ${contactSkills.map(s => `<div class="npc-skill">&#8250; ${esc(s)}</div>`).join('')}
      </div>` : ''}
    ${renderPromoteSection(charId)}
    <div class="npc-modal-gm gm-only">
      <div class="npc-modal-gm-banner">// GM EYES ONLY //</div>
      ${gmBg}
      <div id="npcNotesAlert" class="alert" style="margin-bottom:4px"></div>
      <div class="npc-modal-section">
        <div class="npc-modal-sec-lbl">GM Notes</div>
        <textarea id="npcNotesInput" rows="4" class="ws-notes-ta">${esc(char.notes || '')}</textarea>
      </div>
    </div>`;

  // Show footer (Save Notes / Cancel) for GMs only
  const foot = document.getElementById('npcModalFoot');
  if (isAdmin()) {
    foot.style.display = '';
    document.getElementById('npcNotesSaveBtn').onclick = () => saveNpcNotes(charId);
  } else {
    foot.style.display = 'none';
  }

  // NPC/POI dossier is always dark-purple regardless of affiliation
  const npcOverlayEl = document.getElementById('npcOverlay');
  ['oc-megacorp','oc-government','oc-syndicate','oc-gang','oc-fixer_network','oc-cult','oc-other']
    .forEach(c => npcOverlayEl.classList.remove(c));
  npcOverlayEl.classList.add('npc-overlay-default');

  document.getElementById('npcOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeNpcModal() {
  resumePoll();
  document.getElementById('npcOverlay').classList.remove('open');
  document.body.style.overflow = '';
}

async function saveNpcNotes(charId) {
  const note = document.getElementById('npcNotesInput')?.value.trim() || null;
  const res = await apiFetch(`${API}/characters/${charId}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ notes: note })
  });
  if (res.ok) {
    if (charMapStore[charId]) charMapStore[charId].notes = note;
    const a = document.getElementById('npcNotesAlert');
    if (a) { a.textContent = '// notes saved'; a.className = 'alert show'; setTimeout(() => a.className = 'alert', 2000); }
  }
}

// Generic boolean field reveal toggle — pass any PATCH-able boolean field name.
// Usage: toggleDataReveal(charId, 'show_background', currentBoolValue)
async function toggleDataReveal(charId, field, currentState) {
  const res = await apiFetch(`${API}/characters/${charId}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ [field]: !currentState })
  });
  if (res.ok) {
    if (charMapStore[charId]) charMapStore[charId][field] = !currentState;
    openNpcModal(charId);
  }
}

function npcOverlayClick(e) {
  if (e.target === document.getElementById('npcOverlay')) closeNpcModal();
}

document.addEventListener('keydown', e => { if (e.key === 'Escape') { closeNpcModal(); closeEditModal(); closeOrgEditModal(); closeLocEditModal(); closeCharEditModal(); } });

// ── Contact Promotion (NPC modal) ─────────────────────────────
function renderPromoteSection(charId) {
  const char = charMapStore[charId];
  const existing = contactStore.filter(c => c.npc_id === charId);
  const pcs = Object.values(charMapStore).filter(c => c.is_pc && c.is_active);
  const linkedIds = new Set(existing.map(c => c.owner_id));
  const available = pcs.filter(p => !linkedIds.has(p.id));

  const rows = existing.map(c => {
    const owner = charMapStore[c.owner_id];
    const ownerActive = owner?.is_active !== false;
    return `<div class="promote-row${ownerActive ? '' : ' promote-row-inactive'}">
      <span class="promote-runner">${owner ? esc(owner.name) : '#' + c.owner_id}${ownerActive ? '' : ' <span style="color:#555;font-size:0.6rem">(inactive)</span>'}</span>
      <span class="promote-meta">Loyalty ${c.loyalty}</span>
      <button class="promote-remove gm-only" onclick="removeContactLink(${c.id})" title="Remove link">✕</button>
    </div>`;
  }).join('');

  const addForm = available.length ? `
    <div class="promote-add-form gm-only" id="promoteAddForm" style="display:none">
      <select id="promoteOwnerSel" class="promote-select">
        ${available.map(p => `<option value="${p.id}">${esc(p.name)}</option>`).join('')}
      </select>
      <label class="promote-field-lbl">Loyalty
        <input type="number" id="promoteLoyalty" class="promote-num" min="1" max="6" value="1">
      </label>
      <button class="btn btn-green btn-sm" onclick="addContactLink()">Link</button>
      <button class="btn btn-ghost btn-sm" onclick="document.getElementById('promoteAddForm').style.display='none'">Cancel</button>
    </div>
    <button class="btn btn-amber btn-sm gm-only mt-6" onclick="document.getElementById('promoteAddForm').style.display=document.getElementById('promoteAddForm').style.display===''?'none':''">+ Link Runner</button>
  ` : (existing.length ? '<div class="promote-all-linked">All active runners already linked.</div>' : '<div class="promote-all-linked">No active PC runners found.</div>');

  const hasContent = existing.length > 0 || isAdminMode();
  return `<div class="npc-modal-section" id="promoteSectionWrap">
    ${hasContent ? '<div class="npc-modal-sec-lbl">Contact Relationships</div>' : ''}
    ${rows}
    ${addForm}
  </div>`;
}

async function addContactLink() {
  const char = charMapStore[npcModalCharId];
  if (!char) return;
  const ownerId = parseInt(document.getElementById('promoteOwnerSel').value);
  const loyalty = Math.min(6, Math.max(1, parseInt(document.getElementById('promoteLoyalty').value) || 1));
  const conn    = char.connection ?? 1;
  const res = await apiFetch(`${API}/contacts/`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      name: char.name,
      profession: char.archetype || null,
      race: char.race || null,
      owner_id: ownerId,
      npc_id: npcModalCharId,
      loyalty,
      connection: conn,
      organization_id: char.organization_id || null,
    })
  });
  if (!res.ok) { showAlert('Failed to create contact link.'); return; }
  const contactsRes = await apiFetch(`${API}/contacts/`);
  contactStore = await contactsRes.json();
  document.getElementById('promoteSectionWrap').outerHTML = renderPromoteSection(npcModalCharId);
  loadAll();
}

async function removeContactLink(contactId) {
  showConfirm('Remove this contact link?', async () => {
    await apiFetch(`${API}/contacts/${contactId}`, { method: 'DELETE' });
    const contactsRes = await apiFetch(`${API}/contacts/`);
    contactStore = await contactsRes.json();
    document.getElementById('promoteSectionWrap').outerHTML = renderPromoteSection(npcModalCharId);
    loadAll();
  });
}

// ── Non-NPC Contact Modal (contacts without a character record) ──
let nonNpcModalId = null;

function openNonNpcContactModal(contactId) {
  const merged = nonNpcContactStore[contactId];
  if (!merged) return;
  pausePoll();
  nonNpcModalId = contactId;
  const org = merged.organization_id ? orgStore[merged.organization_id] : null;
  const race = merged.race || null;
  const prof = merged.profession || null;
  const raceProf = [race, prof].filter(Boolean).join(' | ');
  const connVal = merged.connection ?? 1;

  document.getElementById('npcModalName').textContent = `Dossier // ${merged.name}`;
  document.getElementById('npcModalBadge').innerHTML =
    raceProf ? `<span class="badge-race-prof">${esc(raceProf)}</span>` : '';

  const orgLine = `<div class="cc-org mb-12"><span class="cc-org-lbl">Affiliation</span><span class="cc-org-sep"> // </span>${org ? esc(org.name) : '[Unknown]'}</div>`;

  const ownerRows = (merged.owners || []).map(o => {
    const ownerChar = charMapStore[o.owner_id];
    const name = ownerChar ? esc(ownerChar.name) : `#${o.owner_id}`;
    return `<div class="promote-row">
      <span class="promote-runner">${name}</span>
      <span class="promote-meta">Loyalty ${o.loyalty || 0}</span>
      <button class="promote-remove gm-only" onclick="removeNonNpcLink(${o.contact_id})" title="Remove link">✕</button>
    </div>`;
  }).join('');

  const connDisplay = `
    <div class="cc-connection-gm mb-12" title="${CONNECTION_TIPS[connVal] || ''}">
      <span class="cc-conn-lbl">Connection</span>
      <span class="cc-via-dots">${loyaltyDots(connVal,6)}</span>
      <span class="cc-via-num">${connVal}</span>
    </div>`;

  document.getElementById('npcModalBody').innerHTML = `
    ${orgLine}
    ${merged.description ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Profile</div><div class="npc-modal-text">${esc(merged.description)}</div></div>` : ''}
    ${connDisplay}
    ${ownerRows ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Contact Relationships</div>${ownerRows}</div>` : ''}`;

  document.getElementById('npcModalFoot').style.display = 'none';
  // Contact modal (non-NPC) is also always dark-purple
  const _nonNpcOverlay = document.getElementById('npcOverlay');
  ['oc-megacorp','oc-government','oc-syndicate','oc-gang','oc-fixer_network','oc-cult','oc-other']
    .forEach(c => _nonNpcOverlay.classList.remove(c));
  _nonNpcOverlay.classList.add('npc-overlay-default');
  document.getElementById('npcOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function removeNonNpcLink(contactId) {
  showConfirm('Remove this contact link?', async () => {
    await apiFetch(`${API}/contacts/${contactId}`, { method: 'DELETE' });
    const contactsRes = await apiFetch(`${API}/contacts/`);
    contactStore = await contactsRes.json();
    closeNpcModal();
    loadAll();
  });
}

async function toggleCharActive(charId, isActive) {
  await apiFetch(`${API}/characters/${charId}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({is_active: !isActive})
  });
  loadAll();
}

let _myCharIds = new Set();

function getMyCharIds() {
  if (isAdminMode()) return new Set();
  return _myCharIds;
}

async function toggleContactActive(contactId, currentlyActive) {
  await apiFetch(`${API}/contacts/${contactId}`, {
    method: 'PATCH',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ is_active: !currentlyActive })
  });
  loadAll();
}

async function patchNpcConnection(charId, currentVal) {
  showPrompt('Connection rating (1–6):', currentVal, async (raw) => {
    const n = parseInt(raw, 10);
    if (isNaN(n) || n < 1 || n > 6) { showAlert('Rating must be between 1 and 6'); return; }
    await apiFetch(`${API}/characters/${charId}`, {
      method: 'PATCH',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({connection: n})
    });
    loadAll();
  });
}

async function patchConnection(cardKey, currentVal, contactIds) {
  showPrompt('Connection rating (1–6):', currentVal, async (raw) => {
    const n = parseInt(raw, 10);
    if (isNaN(n) || n < 1 || n > 6) { showAlert('Rating must be between 1 and 6'); return; }
    await Promise.all(contactIds.map(cid =>
      apiFetch(`${API}/contacts/${cid}`, {
        method: 'PATCH',
        body: JSON.stringify({connection: n})
      })
    ));
    loadAll();
  });
}

function buildContactCard(merged, charMap, orgMap) {
  const org    = merged.organization_id ? orgMap[merged.organization_id] : null;
  const npc    = merged.npc_id ? charMap[merged.npc_id] : null;
  const skills = npc?.contact_skills || [];
  const race   = merged.race || npc?.race || null;
  const prof   = merged.profession || npc?.title || npc?.archetype || null;
  // Connection: from NPC character record if linked, else from contact record
  const connVal = npc ? (npc.connection ?? 1) : (merged.connection ?? 1);
  const contactIds = JSON.stringify((merged.owners || []).map(o => o.contact_id).filter(Boolean));
  const cardKey = `cc-${merged.npc_id || merged.name.replace(/\W+/g, '-')}`;

  const raceProf = [race, prof].filter(Boolean).join(' | ');
  const orgDisplay = org ? esc(org.name) : '[Unknown]';

  // Activity state: NPC must be active AND at least one owner row must be active
  const npcIsActive    = npc ? (npc.is_active !== false) : true;
  const hasActiveOwner = !merged.owners || merged.owners.length === 0 || merged.owners.some(o => o.is_active !== false);
  const isActive       = npcIsActive && hasActiveOwner;

  // Clickable only when NPC is active
  const clickHandler = isActive
    ? (merged.npc_id
        ? `onclick="openNpcModal(${merged.npc_id})" title="View dossier"`
        : `onclick="openNonNpcContactModal(${merged.id})" title="View contact"`)
    : '';

  // Active toggle (card-level) — admin only, acts on the NPC character record
  const contactToggleBtn = npc
    ? `<button class="card-active-btn gm-only ${isActive ? '' : 'card-inactive-btn'}" onclick="event.stopPropagation();toggleCharActive(${npc.id},${npcIsActive})" title="${npcIsActive ? 'Mark inactive' : 'Mark active'}">${npcIsActive ? '● active' : '○ activate'}</button>`
    : '';
  const contactOverlay = isActive ? '' : `<div class="card-inactive-overlay"><div class="card-inactive-lbl">Inactive</div></div>`;

  const myCharIds = getMyCharIds();
  const ownerRows = (merged.owners || []).map(o => {
    const ownerChar = charMap[o.owner_id];
    const name = ownerChar ? esc(ownerChar.name) : `#${o.owner_id}`;
    const rowActive = o.is_active !== false;
    const canToggleRow = isAdminMode() || myCharIds.has(o.owner_id);
    if (!rowActive) {
      return `
        <div class="cc-via-row cc-via-row-inactive">
          <span class="cc-via-name" style="color:var(--red)">${name} <span style="font-size:0.65rem;letter-spacing:1px">(INACTIVE)</span></span>
          ${canToggleRow
            ? `<button class="cc-via-toggle-btn" onclick="event.stopPropagation();toggleContactActive(${o.contact_id},false)" title="Reactivate">○ reactivate</button>`
            : `<button class="cc-via-toggle-btn cc-via-toggle-other" disabled title="Managed by another runner">○ inactive</button>`}
        </div>`;
    }
    return `
      <div class="cc-via-row">
        <span class="cc-via-name">${name}</span>
        <div class="cc-via-ratings">
          <span class="cc-via-lbl">Loyalty</span>
          <span class="cc-via-dots">${loyaltyDots(o.loyalty||0,6)}</span>
          <span class="cc-via-num">${o.loyalty||0}</span>
        </div>
        ${canToggleRow
          ? `<button class="cc-via-toggle-btn cc-via-toggle-active" onclick="event.stopPropagation();toggleContactActive(${o.contact_id},true)" title="Mark inactive">● active</button>`
          : `<button class="cc-via-toggle-btn cc-via-toggle-other" disabled title="Managed by another runner">● active</button>`}
      </div>`;
  });

  // Connection edit: NPC-linked patches the character; non-NPC patches the contact record
  const connEditBtn = npc
    ? `<button class="cc-conn-edit-btn" onclick="event.stopPropagation();patchNpcConnection(${npc.id},${connVal})">✎</button>`
    : `<button class="cc-conn-edit-btn" onclick="event.stopPropagation();patchConnection('${cardKey}',${connVal},${contactIds})">✎</button>`;

  return `
    <div class="contact-card cc-clickable" ${clickHandler}>
      ${contactToggleBtn}
      ${contactOverlay}
      <div class="cc-head">
        <div class="cc-name">${esc(merged.name)}</div>
      </div>
      ${raceProf ? `<div style="margin-bottom:6px"><span class="cc-race-prof">${esc(raceProf)}</span></div>` : ''}
      <div class="cc-org"><span class="cc-org-lbl">Affiliation</span><span class="cc-org-sep"> // </span>${orgDisplay}</div>
      <div class="cc-connection-gm" title="${CONNECTION_TIPS[connVal] || ''}">
        <span class="cc-conn-lbl">Connection</span>
        <span class="cc-via-dots">${loyaltyDots(connVal,6)}</span>
        <span class="cc-via-num">${connVal}</span>
      </div>
      <div class="cc-known-via-lbl">Known via</div>
      ${ownerRows.join('')}
      ${merged.description ? `<div class="cc-desc">${esc(merged.description)}</div>` : ''}
      ${skills.length ? `
        <div class="cc-skills">
          <div class="cc-skills-lbl">Services</div>
          ${skills.map(s => `<div class="cc-skill">&#8250; ${esc(s)}</div>`).join('')}
        </div>` : ''}
    </div>`;
}

const expandedLocs = {};
function toggleLocDesc(id) {
  expandedLocs[id] = !expandedLocs[id];
  const el  = document.getElementById(`lc-desc-${id}`);
  const btn = document.getElementById(`lc-xbtn-${id}`);
  if (el)  el.classList.toggle('lc-desc-expanded', expandedLocs[id]);
  if (btn) btn.textContent = expandedLocs[id] ? '[ collapse ]' : '[ expand ]';
}

function buildLocCard(loc, orgMap) {
  const ctrl = loc.controlling_org_id ? orgMap[loc.controlling_org_id]?.name : null;
  const longDesc = loc.description && loc.description.length > 100;
  return `
    <div class="loc-card" onclick="openLocEditModal(${loc.id})" class="clickable" title="View location">
      <div class="lc-name">${esc(loc.name)}</div>
      <div class="lc-type">${esc(loc.location_type || 'unknown')}</div>
      ${ctrl ? `<div class="lc-ctrl">${esc(ctrl)}</div>` : ''}
      ${loc.description ? `<div class="lc-desc" id="lc-desc-${loc.id}">${esc(loc.description)}</div>` : ''}
      ${longDesc ? `<div><button class="oc-expand-btn" id="lc-xbtn-${loc.id}" onclick="event.stopPropagation();toggleLocDesc(${loc.id})">[ expand ]</button></div>` : ''}
    </div>`;
}

let charRepStore = {};  // char_id -> {net_rep, net_rep_tier, pa, pa_tier}
const expandedNpcs = {};
function toggleNpcDesc(id) {
  expandedNpcs[id] = !expandedNpcs[id];
  const el  = document.getElementById(`npc-desc-${id}`);
  const btn = document.getElementById(`npc-xbtn-${id}`);
  if (el)  el.classList.toggle('npc-desc-expanded', expandedNpcs[id]);
  if (btn) btn.textContent = expandedNpcs[id] ? '[ collapse ]' : '[ expand ]';
}

function buildCharCard(char, orgMap = {}) {
  const race      = char.race || null;
  const archetype = char.archetype || null;
  // PCs: archetype is displayed directly (picker saves archetype, not title)
  // NPCs: title takes precedence (e.g. "Yakuza Underboss"), falling back to archetype
  const display   = char.is_pc ? (archetype || char.title || null) : (char.title || archetype || null);
  const raceProf  = [race, display].filter(Boolean).join(' | ');
  const rep = char.is_pc ? charRepStore[char.id] : null;
  const repStr = rep
    ? `<span style="${repColorStyle(rep.net_rep)}">${rep.net_rep_tier}</span>`
    : null;
  const paStr = rep ? rep.pa_tier : null;
  const heatVal = rep ? (rep.heat || 0) : 0;
  const heatStr = rep
    ? `<span class="${heatClass(heatVal)}" style="font-size:.6rem;letter-spacing:1px;border:1px solid;padding:1px 6px">${rep.heat_label || heatLabelStr(heatVal)}</span>`
    : null;
  const longDesc = !char.is_pc && char.description && char.description.length > 120;
  const isActive = char.is_active !== false;

  const isMine = char.is_pc && _myCharIds.has(char.id);
  const isUnclaimed = char.is_pc && !char.is_claimed;

  const canToggle = isAdminMode() || (char.is_pc && isMine);
  const toggleBtn = canToggle
    ? `<button class="card-active-btn ${isActive ? '' : 'card-inactive-btn'}${!char.is_pc ? ' gm-only' : ''}" onclick="event.stopPropagation();toggleCharActive(${char.id},${isActive})" title="${isActive ? 'Mark inactive' : 'Mark active'}">${isActive ? '● active' : '○ activate'}</button>`
    : '';
  const overlay = isActive ? '' : `<div class="card-inactive-overlay"><div class="card-inactive-lbl">Inactive</div></div>`;
  const claimBtn = char.is_pc && !isAdminMode() && isUnclaimed
    ? `<button class="btn btn-green ws-card-action" onclick="event.stopPropagation();claimChar(${char.id})">Claim</button>`
    : '';
  const ownerBadge = char.is_pc && isMine
    ? `<button class="btn ws-card-action" style="color:var(--red);border-color:var(--red)" onclick="event.stopPropagation();releaseChar(${char.id})">Release</button>`
    : '';

  const cardClass = `char-card ${char.is_pc ? 'is-pc' : (isActive ? 'npc-clickable' : '')}`;
  const clickAttr = char.is_pc && isAdminMode()
    ? `onclick="openCharEditModal(${char.id})" title="Edit character" style="cursor:pointer;position:relative"`
    : char.is_pc
      ? `style="cursor:default;position:relative"`
      : (isActive ? `onclick="openNpcModal(${char.id})" title="View dossier"` : '');

  return `
    <div class="${cardClass}" ${clickAttr}>
      ${toggleBtn}
      ${overlay}
      <div class="ch-name">${esc(char.name)}</div>
      ${char.is_pc
        ? `<div><span class="cc-race-prof ${archetypeClass(archetype)}${isAdminMode() ? ' badge-archetype-clickable' : ''}"${isAdminMode() ? ` onclick="event.stopPropagation();editCharArchetype(${char.id})" title="Click to change archetype"` : ''}>${esc(raceProf || archetype || 'UNKNOWN')}</span></div>`
        : (raceProf ? `<div><span class="cc-race-prof">${esc(raceProf)}</span></div>` : '')}
      ${!char.is_pc ? (() => { const org = char.organization_id ? orgMap[char.organization_id] : null; return `<div class="cc-org" style="margin-bottom:4px"><span class="cc-org-lbl">Affiliation</span><span class="cc-org-sep"> // </span>${org ? esc(org.name) : '[Unknown]'}</div>`; })() : ''}
      <div class="ch-meta">
        ${char.nationality ? `<div class="ws-nationality">${esc(char.nationality)}</div>` : ''}
        ${char.description
          ? char.is_pc
            ? `<div style="margin-top:6px;color:var(--text-dim)">${esc(char.description).substring(0,120)}${char.description.length>120?'…':''}</div>`
            : `<div class="npc-desc" id="npc-desc-${char.id}" style="margin-top:6px">${esc(char.description)}</div>
               ${longDesc ? `<div><button class="oc-expand-btn" id="npc-xbtn-${char.id}" onclick="event.stopPropagation();toggleNpcDesc(${char.id})">[ expand ]</button></div>` : ''}`
          : ''}
        ${repStr ? `<div class="ch-finance ws-ch-stat" style="margin-top:4px"><span style="color:var(--steel-blue)">STREET REP: </span>${repStr}</div>` : ''}
        ${paStr  ? `<div class="ch-finance ws-ch-stat" style="color:var(--steel-blue)" title="${PA_TIPS[paStr] || ''}">PUBLIC AWARENESS: ${paStr}</div>` : ''}
        ${heatStr && isAdminMode()
          ? `<div class="ch-finance ws-ch-stat"><span style="color:var(--steel-blue)">HEAT: </span>${heatStr} <span style="color:var(--text-dim);font-size:.58rem">(${heatVal})</span></div>`
          : heatStr && isMine
          ? `<div class="ch-finance ws-ch-stat"><span style="color:var(--steel-blue)">HEAT: </span>${heatStr}</div>`
          : ''}
      </div>
      ${claimBtn}${ownerBadge}
    </div>`;
}

function section(key, title, html, manageUrl) {
  const manageLink = manageUrl ? `<a href="${manageUrl}" class="sec-manage-link">Manage</a>` : '';
  return `
    <div class="section-head" id="sec-head-${key}">
      <span>${esc(title)}</span>
      <span class="flex-1"></span>
      ${manageLink}
    </div>
    <div id="sec-body-${key}">
      ${html}
    </div>
    <hr class="rule">`;
}

// ── Faction Reputation ────────────────────────────────────────
const _standingsStore = {};  // charId -> standings array; populated in buildFactionRepSection
const STANDING_TIERS = [
  [-10, -7, 'hostile'],
  [ -6, -3, 'unfriendly'],
  [ -2,  2, 'neutral'],
  [  3,  6, 'friendly'],
  [  7, 10, 'allied'],
];
function standingLabel(val) {
  val = Math.max(-10, Math.min(10, val || 0));
  for (const [lo, hi, label] of STANDING_TIERS) {
    if (val >= lo && val <= hi) return label;
  }
  return 'neutral';
}
function standingClass(label) {
  const map = { hostile: 'std-hostile', unfriendly: 'std-unfriendly', neutral: 'std-neutral', friendly: 'std-friendly', allied: 'std-allied' };
  return map[label] || 'std-neutral';
}

function buildFactionRepSection(activePcs, repStore, myCharIds) {
  const admin = isAdminMode();
  const cards = [];

  for (const pc of activePcs) {
    const repData   = repStore[pc.id] || {};
    const standings = repData.standings || [];

    if (admin) {
      // Admin: all PCs, all non-zero standings, with +/- controls + edit button
      const nonZero = standings.filter(s => s.standing !== 0);
      _standingsStore[pc.id] = standings;  // store for editor lookup
      const rows = nonZero.map(s => `
        <div class="faction-row">
          <span class="faction-org" title="${esc(s.org_name)}">${esc(s.org_name)}</span>
          <span class="${standingClass(s.label)}">${esc(s.label)}</span>
          <span class="faction-val">(${s.standing > 0 ? '+' : ''}${s.standing})</span>
        </div>`).join('');
      cards.push(`
        <div class="faction-pc-card">
          <div class="faction-pc-name" style="display:flex;justify-content:space-between;align-items:center">
            <span>${esc(pc.name)}</span>
            <button class="btn btn-sm" style="color:var(--cyan);border-color:#0a2a3a"
              onclick="openStandingEditor(${pc.id})">Edit</button>
          </div>
          ${nonZero.length
            ? rows
            : '<div class="dim-label">No recorded standings</div>'}
        </div>`);
    } else {
      // Runner: only my PCs, only explicitly non-neutral standings
      if (!myCharIds.has(pc.id)) continue;
      const notable = standings.filter(s => Math.abs(s.standing) > 2);
      if (!notable.length) continue;
      const rows = notable.map(s => `
        <div class="faction-row">
          <span class="faction-org" title="${esc(s.org_name)}">${esc(s.org_name)}</span>
          <span class="${standingClass(s.label)}">${esc(s.label)}</span>
        </div>`).join('');
      cards.push(`
        <div class="faction-pc-card">
          <div class="faction-pc-name">${esc(pc.name)}</div>
          ${rows}
        </div>`);
    }
  }

  if (!cards.length) {
    return admin
      ? '<div class="empty-lead" style="margin:10px 0">No faction standings on record for any active PC.</div>'
      : '<div class="empty-lead" style="margin:10px 0">No notable faction ties on record for your runners.</div>';
  }
  return `<div class="faction-grid">${cards.join('')}</div>`;
}

// ── Standing Editor ─────────────────────────────────────────
let _seCharId   = null;
let _seCharName = null;
let _seOrgData  = [];   // [{org_id, org_name, standing_id, standing}]

function openStandingEditor(charId) {
  pausePoll();
  const pc = charMapStore[charId];
  const charName = pc ? pc.name : `Character #${charId}`;
  const standings = _standingsStore[charId] || [];
  _seCharId   = charId;
  _seCharName = charName;
  // Merge existing standings with all active orgs
  const standingByOrg = {};
  for (const s of standings) standingByOrg[s.org_id] = s;
  _seOrgData = Object.values(orgStore)
    .filter(o => o.is_active)
    .sort((a,b) => a.name.localeCompare(b.name))
    .map(o => ({
      org_id:     o.id,
      org_name:   o.name,
      standing_id: standingByOrg[o.id]?.id ?? null,
      standing:   standingByOrg[o.id]?.standing ?? 0,
    }));
  document.getElementById('seTitle').textContent = `Faction Standings // ${charName}`;
  document.getElementById('sePcBadge').innerHTML = '';
  renderStandingEditor();
  document.getElementById('standingEditorOverlay').classList.add('open');
}

function renderStandingEditor() {
  const rows = _seOrgData.map((o, i) => {
    const val = o.standing;
    const cls = standingClass(standingLabel(val));
    return `
      <div class="faction-row ws-se-row">
        <span class="faction-org ws-se-org" title="${esc(o.org_name)}">${esc(o.org_name)}</span>
        <input type="number" class="se-val ws-se-input" data-idx="${i}"
          value="${val}" min="-10" max="10"
          oninput="seUpdateLabel(this,${i})">
        <span class="se-label ws-se-label ${cls}" id="se-lbl-${i}">${standingLabel(val)}</span>
      </div>`;
  }).join('');
  document.getElementById('seBody').innerHTML = rows ||
    '<div class="ws-empty" style="padding:16px">No active organizations found.</div>';
}

function seUpdateLabel(input, idx) {
  const val = Math.max(-10, Math.min(10, parseInt(input.value) || 0));
  input.value = val;
  _seOrgData[idx].standing = val;
  const lbl = document.getElementById(`se-lbl-${idx}`);
  if (lbl) {
    const l = standingLabel(val);
    lbl.textContent = l;
    lbl.className = `se-label ws-se-label ${standingClass(l)}`;
  }
}

function closeStandingEditor() {
  resumePoll();
  document.getElementById('standingEditorOverlay').classList.remove('open');
}

async function saveStandingEditor() {
  // Only send rows that differ from 0 or have an existing standing_id
  const changes = _seOrgData.filter(o => o.standing !== 0 || o.standing_id !== null);
  let errors = 0;
  for (const o of changes) {
    try {
      if (o.standing_id !== null) {
        // Update existing
        const r = await apiFetch(`${API}/reputation/standings/${o.standing_id}`, {
          method: 'PATCH',
          body: JSON.stringify({ standing: o.standing }),
        });
        if (!r.ok) await apiThrow(r);
        // Delete if zeroed out
        if (o.standing === 0) {
          await apiFetch(`${API}/reputation/standings/${o.standing_id}`, {
            method: 'DELETE',
          });
        }
      } else if (o.standing !== 0) {
        // Create new
        const r = await apiFetch(`${API}/reputation/standings`, {
          method: 'POST',
          body: JSON.stringify({
            character_id:    _seCharId,
            organization_id: o.org_id,
            standing:        o.standing,
          }),
        });
        if (!r.ok) await apiThrow(r);
      }
    } catch(e) {
      errors++;
      console.warn(`Standing save failed for ${o.org_name}:`, e);
    }
  }
  await loadAll();
  closeStandingEditor();
  if (errors) showAlert(`${errors} standing(s) failed to save — check console.`);
}

async function resetPcData() {
  showConfirm(
    'Reset ALL PC heat, reputation scores, and org standings to baseline? This cannot be undone.',
    async () => {
      try {
        const res = await apiFetch(`${API}/reputation/reset-pc-data`, {
          method: 'POST',
        });
        if (!res.ok) await apiThrow(res);
        await loadAll();
      } catch(e) {
        showAlert(`Reset failed: ${e.message}`);
      }
    },
    'Reset All PC Data'
  );
}

// ── Org grouping config ───────────────────────────────────────
// Maps every known org_type value → canonical display group
const TYPE_GROUP = {
  'megacorp':              'megacorp',
  'government':            'government',
  'nation-state':          'government',
  'security contractor':   'government',
  'corporation':           'government',
  'syndicate':             'syndicate',
  'crime syndicate':       'syndicate',
  'gang':                  'gang',
  'fixer_network':         'fixer_network',
  'cult':                  'cult',
  'political organization':'cult',
  'other':                 'other',
};
const ORG_ORDER  = ['megacorp','government','syndicate','gang','fixer_network','cult','other'];
const ORG_LABELS = {
  megacorp:   'Megacorporate Presence',
  government: 'Law Enforcement & Government',
  syndicate:  'Organized Crime — Syndicates',
  gang:       'Street Gangs',
  fixer_network: 'Fixer Networks',
  cult:       'Cults & Fringe Groups',
  other:      'Other Organizations',
};

// ── LTG / Org-edit helpers ────────────────────────────────────
const OE_VIS_ORDER   = { listed: 0, unlisted: 1, black: 2 };
const OE_COLOR_ORDER = { blue: 0, green: 1, orange: 2, red: 3, black: 4 };
function oeRatingSort(r) {
  if (!r) return 999;
  const [c, n] = r.toLowerCase().split('-');
  return (OE_COLOR_ORDER[c] ?? 5) * 100 + (parseInt(n) || 0);
}
const OE_VIS_OPTS = `<option value="listed">Listed</option><option value="unlisted">Unlisted</option><option value="black">Black</option>`;

const OE_RATING_OPTS = `
  <option value="Blue-3">Blue-3</option>
  <option value="Green-4">Green-4</option><option value="Green-5">Green-5</option><option value="Green-6">Green-6</option><option value="Green-8">Green-8</option>
  <option value="Orange-5">Orange-5</option><option value="Orange-6">Orange-6</option><option value="Orange-8">Orange-8</option><option value="Orange-9">Orange-9</option>
  <option value="Red-6">Red-6</option><option value="Red-8">Red-8</option><option value="Red-9">Red-9</option><option value="Red-10">Red-10</option>
  <option value="Black-8">Black-8</option><option value="Black-9">Black-9</option><option value="Black-10">Black-10</option><option value="Black-11">Black-11</option><option value="Black-12">Black-12</option>`;

  const OE_DEFAULT_RTG = 'NA/UCAS-SEA';

let oeRTGs = [];
let oeTelecomCount = 0;
let oeHostCount = 0;

// Load RTGs once at startup (they rarely change)
(async function() {
  try {
    const r = await apiFetch(`${API}/rtgs/`);
    oeRTGs = r.ok ? (await r.json()).sort((a, b) => a.code.localeCompare(b.code)) : [];
  } catch(e) { console.warn('RTG load failed', e.message); }
})();

function oeBuildRTGOptions(selected) {
  return '<option value="">— Select RTG —</option>' +
    oeRTGs.map(r => `<option value="${esc(r.code)}"${r.code===selected?' selected':''}>${esc(r.code)} — ${esc(r.region||'')}</option>`).join('');
}

function oeGenerateLTG() {
  const existing = new Set();
  Object.values(orgStore).forEach(o => (o.ltgs||[]).forEach(l => { if (l.ltg) existing.add(l.ltg.toUpperCase()); }));
  document.querySelectorAll('#oeHostBody [data-field="ltg"]').forEach(el => { if (el.value.trim()) existing.add(el.value.trim().toUpperCase()); });
  const HEX = '0123456789ABCDEF';
  let code;
  do { code = Array.from({length:5}, () => HEX[Math.floor(Math.random()*16)]).join(''); } while (existing.has(code));
  return code;
}

function oeFormatTelecom(input) {
  const digits = input.value.replace(/\D/g,'').slice(0,10);
  if (!digits.length) { input.value=''; return; }
  if (digits.length<=3) { input.value='('+digits; return; }
  if (digits.length<=6) { input.value='('+digits.slice(0,3)+') '+digits.slice(3); return; }
  input.value='('+digits.slice(0,3)+') '+digits.slice(3,6)+'-'+digits.slice(6);
}

function oeEnforceIdCode(input) {
  input.value = input.value.replace(/[^A-Za-z0-9\-]/g,'').slice(0,8).toUpperCase();
}

function oeAddTelecom(data) {
  const tbody = document.getElementById('oeTelecomBody');
  document.getElementById('oeEmptyTelecom')?.remove();
  oeTelecomCount++;
  const id = `oe_tc_${oeTelecomCount}`;
  const tr = document.createElement('tr');
  tr.id = id;
  const selVis = OE_VIS_OPTS.replace(`value="${data?.visibility||'listed'}"`, `value="${data?.visibility||'listed'}" selected`);
  tr.innerHTML = `
    <td><input type="text" placeholder="(206) 555-0100" data-field="number" value="${esc(data?.number||'')}" inputmode="tel"></td>
    <td><input type="text" placeholder="Main switchboard..." data-field="description" value="${esc(data?.description||'')}"></td>
    <td><select data-field="visibility">${selVis}</select></td>
    <td class="gm-only text-center"><input type="checkbox" data-field="revealed" ${data?.revealed ? 'checked' : ''} title="Reveal to players"></td>
    <td class="gm-only"><button type="button" class="btn btn-red" onclick="oeRemoveRow('${id}','oeTelecomBody','oeEmptyTelecom',5)">✕</button></td>`;
  const numInput = tr.querySelector('[data-field="number"]');
  numInput.addEventListener('input', () => oeFormatTelecom(numInput));
  tbody.appendChild(tr);
}

function oeAddHost(data) {
  const tbody = document.getElementById('oeHostBody');
  document.getElementById('oeEmptyHost')?.remove();
  oeHostCount++;
  const id = `oe_host_${oeHostCount}`;
  const tr = document.createElement('tr');
  tr.id = id;
  const ltgCode    = data?.ltg || oeGenerateLTG();
  const defaultRTG = data?.rtg ?? OE_DEFAULT_RTG;
  const selVis    = OE_VIS_OPTS.replace(`value="${data?.visibility||'listed'}"`, `value="${data?.visibility||'listed'}" selected`);
  const selRating = OE_RATING_OPTS.replace(`value="${data?.san_access_rating||''}"`, `value="${data?.san_access_rating||''}" selected`);
  tr.innerHTML = `
    <td><select data-field="rtg" style="min-width:160px">${oeBuildRTGOptions(defaultRTG)}</select></td>
    <td><input type="text" data-field="ltg" value="${esc(ltgCode)}" style="width:70px;color:var(--text-dim)" readonly title="Auto-generated LTG code"></td>
    <td><input type="text" placeholder="ID001" data-field="id_code" value="${esc(data?.id_code||'')}" style="width:105px"></td>
    <td><input type="text" placeholder="Description..." data-field="description" value="${esc(data?.description||'')}"></td>
    <td><select data-field="san_access_rating" style="width:110px">${selRating}</select></td>
    <td><select data-field="visibility" style="width:90px">${selVis}</select></td>
    <td class="gm-only text-center"><input type="checkbox" data-field="revealed" ${data?.revealed ? 'checked' : ''} title="Reveal to players"></td>
    <td class="gm-only"><button type="button" class="btn btn-red" onclick="oeRemoveRow('${id}','oeHostBody','oeEmptyHost',8)">✕</button></td>`;
  const idInput = tr.querySelector('[data-field="id_code"]');
  idInput.addEventListener('input', () => oeEnforceIdCode(idInput));
  tbody.appendChild(tr);
}

function oeRemoveRow(id, tbodyId, emptyId, cols) {
  document.getElementById(id)?.remove();
  const tbody = document.getElementById(tbodyId);
  if (!tbody.querySelector(`tr:not(#${emptyId})`)) {
    const tr = document.createElement('tr');
    tr.id = emptyId;
    tr.innerHTML = `<td colspan="${cols}" class="empty-lead">None defined</td>`;
    tbody.appendChild(tr);
  }
}

function oeGetTableData(tbodyId, emptyId, fields) {
  return Array.from(document.querySelectorAll(`#${tbodyId} tr:not(#${emptyId})`)).map(row => {
    const obj = {};
    fields.forEach(f => { const el = row.querySelector(`[data-field="${f}"]`); obj[f] = el ? (el.type === 'checkbox' ? el.checked : (el.value?.trim() || null)) : null; });
    return obj;
  }).filter(obj => Object.values(obj).some(v => v !== null && v !== false && v !== ''));
}

function oeGetLTGs() {
  const telecoms = oeGetTableData('oeTelecomBody', 'oeEmptyTelecom', ['number','description','visibility','revealed'])
    .map(t => ({ type:'telecom', ...t }))
    .sort((a,b) => (OE_VIS_ORDER[a.visibility]??9) - (OE_VIS_ORDER[b.visibility]??9));
  const hosts = oeGetTableData('oeHostBody', 'oeEmptyHost', ['rtg','ltg','id_code','description','san_access_rating','visibility','revealed'])
    .map(h => ({ type:'matrix_host', ...h }))
    .sort((a,b) => {
      const vd = (OE_VIS_ORDER[a.visibility]??9) - (OE_VIS_ORDER[b.visibility]??9);
      return vd !== 0 ? vd : oeRatingSort(a.san_access_rating) - oeRatingSort(b.san_access_rating);
    });
  return [...telecoms, ...hosts];
}

// ── Org Edit Modal ────────────────────────────────────────────
const PREDEFINED_ORG_TYPES = [
  'megacorp','corporation','security contractor',
  'government','nation-state',
  'crime syndicate','gang',
  'fixer_network','political organization','cult',
];

function onOeOrgTypeChange() {
  const val = document.getElementById('oe-org_type').value;
  document.getElementById('oe-org_type-custom-wrap').style.display = val === 'Custom' ? '' : 'none';
}

const OE_TIER_NAMES = {1:'Street Level',2:'Local / District',3:'City-Wide',4:'Regional',5:'National / AAA',6:'Global / AAA+'};
let oeTierVal = 1;
let oeEditingId = null;
let oeLeaderCount = 0;

function oeSetTier(n) {
  oeTierVal = n;
  document.getElementById('oeTierName').textContent = OE_TIER_NAMES[n] || '';
  document.querySelectorAll('[data-oe-tier]').forEach(d => d.classList.toggle('on', parseInt(d.dataset.oeTier) === n));
}

function oeAddLeader(data) {
  const tbody = document.getElementById('oeLeadBody');
  document.getElementById('oeEmptyLead')?.remove();
  oeLeaderCount++;
  const id = `oe_lead_${oeLeaderCount}`;
  const tr = document.createElement('tr');
  tr.id = id;
  tr.innerHTML = `
    <td><input type="text" placeholder="Name..." data-field="name" value="${esc(data?.name||'')}"></td>
    <td><input type="text" placeholder="CEO, Oyabun..." data-field="title" value="${esc(data?.title||'')}"></td>
    <td><input type="text" placeholder="Notes..." data-field="notes" value="${esc(data?.notes||'')}"></td>
    <td class="gm-only"><button type="button" class="btn btn-red" onclick="oeRemoveLeader('${id}')">✕</button></td>`;
  tbody.appendChild(tr);
}

function oeRemoveLeader(id) {
  document.getElementById(id)?.remove();
  const tbody = document.getElementById('oeLeadBody');
  if (!tbody.querySelector('tr:not(#oeEmptyLead)')) {
    const tr = document.createElement('tr');
    tr.id = 'oeEmptyLead';
    tr.innerHTML = '<td colspan="4" class="empty-lead">No executives defined</td>';
    tbody.appendChild(tr);
  }
}

function oeGetLeadership() {
  return Array.from(document.querySelectorAll('#oeLeadBody tr:not(#oeEmptyLead)')).map(row => {
    const obj = {};
    row.querySelectorAll('[data-field]').forEach(el => { obj[el.dataset.field] = el.value.trim() || null; });
    return obj;
  }).filter(r => r.name || r.title);
}

function oeGetChecked(listId) {
  return Array.from(document.querySelectorAll(`#${listId} input.rel-chk:checked`)).map(cb => parseInt(cb.value));
}

function oeGetRevealed(listId) {
  return Array.from(document.querySelectorAll(`#${listId} input.rev-chk:checked`)).map(cb => parseInt(cb.value));
}

function oeRenderRelations(currentOrgId) {
  const orgs = Object.values(orgStore).filter(o => o.id !== currentOrgId);
  const org = orgStore[currentOrgId];
  const allySet     = new Set(org?.ally_ids          || []);
  const enemySet    = new Set(org?.enemy_ids         || []);
  const revAllySet  = new Set(org?.revealed_ally_ids  || []);
  const revEnemySet = new Set(org?.revealed_enemy_ids || []);

  if (!isAdminMode()) {
    // Runner view: show only revealed relationships as read-only text
    [['oeAllyList', allySet, revAllySet], ['oeEnemyList', enemySet, revEnemySet]].forEach(([lid, set, revSet]) => {
      const visible = orgs.filter(o => set.has(o.id) && revSet.has(o.id));
      document.getElementById(lid).innerHTML = visible.length
        ? visible.map(o => `<div class="npc-skill">&#8250; ${esc(o.name)} <span class="ws-dim-tier">[T${o.tier}]</span></div>`).join('')
        : '<div class="ws-empty">None on record</div>';
    });
    return;
  }

  // Admin view: checkbox + reveal toggle per org
  [['oeAllyList', allySet, revAllySet], ['oeEnemyList', enemySet, revEnemySet]].forEach(([lid, set, revSet]) => {
    document.getElementById(lid).innerHTML = orgs.length
      ? orgs.map(o => `
        <label class="chk-item">
          <input type="checkbox" value="${o.id}" class="rel-chk" ${set.has(o.id) ? 'checked' : ''}>
          <span>${esc(o.name)} <span class="ws-dim-tier">[T${o.tier}]</span></span>
          <span style="margin-left:auto">
            <input type="checkbox" value="${o.id}" class="rev-chk" ${revSet.has(o.id) ? 'checked' : ''} title="Reveal to players">
          </span>
        </label>`).join('')
      : '<div class="ws-empty" style="padding:8px">No other organizations</div>';
  });
}

function renderOrgDossierView(org) {
  const allyIds  = (org.revealed_ally_ids  || []);
  const enemyIds = (org.revealed_enemy_ids || []);
  const allies   = allyIds.map(id => orgStore[id]).filter(Boolean);
  const enemies  = enemyIds.map(id => orgStore[id]).filter(Boolean);

  const typeLabel = (org.org_type || 'UNKNOWN').toUpperCase();
  const tier      = org.tier || 1;
  const isActive  = org.is_active !== false;
  const statusDot = isActive
    ? `<span class="text-green">&#9679; ACTIVE</span>`
    : `<span class="text-dim">&#9675; INACTIVE</span>`;

  // Leadership — two-column grid: name | title (aligned, close together)
  const leads = (org.leadership || []);
  const leadHtml = leads.length
    ? `<div class="dossier-cmd-grid">${leads.map(l =>
        `<span style="color:var(--text-bright);font-size:.75rem">&#8250; ${esc(l.name)}</span><span class="dossier-cmd-title">${esc(l.title||'')}</span>`
      ).join('')}</div>`
    : `<div class="ws-empty">None on record</div>`;

  // Relationships
  const makeRelList = orgs => orgs.length
    ? orgs.map(o => `<div class="npc-skill">&#8250; <span style="color:var(--text-bright)">${esc(o.name)}</span> <span class="ws-dim-tier">[T${o.tier}]</span></div>`).join('')
    : `<div class="ws-empty">None on record</div>`;

  // LTG/Network
  const visLtgs = (org.ltgs || []).filter(e => e.visibility === 'listed' || e.revealed);
  const telecoms = visLtgs.filter(e => e.type === 'telecom');
  const hosts    = visLtgs.filter(e => e.type === 'matrix_host');

  const disposBadge = v => {
    if (v === 'listed')   return `<span class="disp-listed">LISTED</span>`;
    if (v === 'unlisted') return `<span class="disp-unlisted">UNLISTED</span>`;
    if (v === 'black')    return `<span class="disp-black">BLACK</span>`;
    return `<span style="color:var(--text-dim);font-size:.65rem">${esc(v||'')}</span>`;
  };

  const telecomGridHeader = `
    <span class="dim-label">IDENTIFIER</span>
    <span class="dim-label">DESCRIPTION</span>
    <span></span>
    <span style="color:var(--text-dim);font-size:.62rem;letter-spacing:.07em;text-align:right">DISPOSITION</span>`;

  const hostGridHeader = `
    <span class="dim-label">IDENTIFIER</span>
    <span class="dim-label">DESCRIPTION</span>
    <span class="dim-label">RATING</span>
    <span class="dim-label" style="text-align:right">DISPOSITION</span>`;

  const telecomHtml = telecoms.length
    ? `<div class="dossier-net-grid">${telecomGridHeader}${telecoms.map(t =>
        `<span style="color:var(--cyan)">&#8250; ${esc(t.number)}</span>
         <span class="text-dim">${esc(t.description||'')}</span>
         <span></span>
         <span class="dossier-net-disp">${disposBadge(t.visibility)}</span>`
      ).join('')}</div>`
    : `<div class="ws-empty">No public telecom listings</div>`;

  const hostHtml = hosts.length
    ? `<div class="dossier-net-grid">${hostGridHeader}${hosts.map(h =>
        `<span><span class="text-amber">&#8250; ${esc(h.rtg)}</span><span class="text-dim"> // </span><span style="color:var(--green-dim)">${esc(h.ltg)}</span>${h.id_code?`<span style="color:var(--purple);font-size:.65rem"> [${esc(h.id_code)}]</span>`:''}</span>
         <span class="text-dim">${esc(h.description||'')}</span>
         <span>${h.san_access_rating ? `<span class="ltg-rating ${ratingClass(h.san_access_rating)}">${esc(h.san_access_rating)}</span>` : ''}</span>
         <span class="dossier-net-disp">${disposBadge(h.visibility)}</span>`
      ).join('')}</div>`
    : `<div class="ws-empty">No public matrix listings</div>`;

  return `
    <div style="padding:4px 0 12px">
      <div class="section-head mb-8">// Profile</div>
      ${org.headquarters ? `<div class="dossier-field"><span class="df-label">Headquarters</span><span class="df-val">${esc(org.headquarters)}</span></div>` : ''}
      ${org.description  ? `<div class="ws-dossier-desc">${esc(org.description)}</div>` : ''}

      <hr class="rule my-12">
      <div class="section-head mb-8">// Command Structure</div>
      <div class="mb-14">${leadHtml}</div>

      <hr class="rule my-12">
      <div class="section-head mb-8">// Political Relationships</div>
      <div class="grid2 mb-14">
        <div>
          <div class="ws-allies-hd">ALLIED</div>
          ${makeRelList(allies)}
        </div>
        <div>
          <div class="ws-enemies-hd">HOSTILE</div>
          ${makeRelList(enemies)}
        </div>
      </div>

      <hr class="rule my-12">
      <div class="section-head mb-8">// RTG/LTG Network Directory</div>
      <div class="mb-14">
        <div class="ws-sec-hd text-cyan">&gt;&gt; TELECOM</div>
        <hr class="rule ws-rule-tight">
        ${telecomHtml}
      </div>
      <div>
        <div class="ws-sec-hd text-amber">&gt;&gt; MATRIX HOSTS</div>
        <hr class="rule ws-rule-tight">
        ${hostHtml}
      </div>
    </div>`;
}

function openOrgEditModal(orgId) {
  const org = orgStore[orgId];
  if (!org) return;
  pausePoll();
  oeEditingId = orgId;

  const adminMode = isAdminMode();
  document.getElementById('oeTitle').textContent = `Intelligence Report // ${org.name}`;

  // Populate header badge: classification · tier · status
  const typeLabel = (org.org_type || 'UNKNOWN').toUpperCase();
  const tier = org.tier || 1;
  const isActive = org.is_active !== false;
  const statusDot = isActive
    ? `<span class="text-green">&#9679; ACTIVE</span>`
    : `<span class="text-dim">&#9675; INACTIVE</span>`;
  const badge = document.getElementById('oeDossierBadge');
  if (badge) badge.innerHTML = `
    <span class="ws-tier-row">
      <span class="cc-race-prof text-amber">${typeLabel}</span>
      <span class="dim-meta">&#183;</span>
      <span class="ws-tier-badge">TIER ${tier} // ${tierLabel(tier).toUpperCase()}</span>
    </span>`;

  if (!adminMode) {
    // Runner view: show dossier, hide the edit form
    document.getElementById('orgDossierView').innerHTML = renderOrgDossierView(org);
    document.getElementById('orgDossierView').style.display = '';
    document.getElementById('orgFormContent').style.display = 'none';
    document.getElementById('orgEditFoot').style.display = 'none';
    // Theme the org modal border/title to match the org card's left-border color
    const _orgEditEl = document.getElementById('orgEditOverlay');
    ['oc-megacorp','oc-government','oc-syndicate','oc-gang','oc-fixer_network','oc-cult','oc-other']
      .forEach(c => _orgEditEl.classList.remove(c));
    _orgEditEl.classList.add(orgClass(org.org_type));
    document.getElementById('orgEditOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
    return;
  }

  // Admin view: hide dossier, show form
  document.getElementById('orgDossierView').style.display = 'none';
  document.getElementById('orgFormContent').style.display = '';

  document.getElementById('oe-name').value = org.name || '';
  const oeOrgType = org.org_type || '';
  if (!oeOrgType || PREDEFINED_ORG_TYPES.includes(oeOrgType)) {
    document.getElementById('oe-org_type').value = oeOrgType;
    document.getElementById('oe-org_type-custom').value = '';
    document.getElementById('oe-org_type-custom-wrap').style.display = 'none';
  } else {
    document.getElementById('oe-org_type').value = 'Custom';
    document.getElementById('oe-org_type-custom').value = oeOrgType;
    document.getElementById('oe-org_type-custom-wrap').style.display = '';
  }
  document.getElementById('oe-headquarters').value = org.headquarters || '';
  document.getElementById('oe-description').value = org.description || '';
  document.getElementById('oe-notes').value = org.notes || '';
  const isActiveCb = document.getElementById('oe-is_active');
  isActiveCb.checked = org.is_active !== false;
  const lbl = document.getElementById('oeStatusLbl');
  lbl.textContent = isActiveCb.checked ? 'ACTIVE' : 'INACTIVE';
  lbl.style.color  = isActiveCb.checked ? 'var(--green)' : 'var(--text-dim)';
  oeSetTier(org.tier || 1);
  document.getElementById('oeLeadBody').innerHTML = '<tr id="oeEmptyLead"><td colspan="4" class="empty-lead">No executives defined</td></tr>';
  oeLeaderCount = 0;
  (org.leadership || []).forEach(l => oeAddLeader(l));
  oeRenderRelations(orgId);
  document.getElementById('oeTelecomBody').innerHTML = '<tr id="oeEmptyTelecom"><td colspan="5" class="empty-lead">No telecom numbers</td></tr>';
  document.getElementById('oeHostBody').innerHTML    = '<tr id="oeEmptyHost"><td colspan="8" class="empty-lead">No matrix hosts</td></tr>';
  oeTelecomCount = 0; oeHostCount = 0;
  (org.ltgs || []).forEach(e => {
    if (e.type === 'telecom')          oeAddTelecom(e);
    else if (e.type === 'matrix_host') oeAddHost(e);
  });
  document.getElementById('oeAlert').className = 'alert';
  document.getElementById('orgEditFoot').style.display = '';
  // Theme the org modal border/title to match the org card's left-border color
  const orgEditOverlayEl = document.getElementById('orgEditOverlay');
  ['oc-megacorp','oc-government','oc-syndicate','oc-gang','oc-fixer_network','oc-cult','oc-other']
    .forEach(c => orgEditOverlayEl.classList.remove(c));
  orgEditOverlayEl.classList.add(orgClass(org.org_type));
  document.getElementById('orgEditOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeOrgEditModal() {
  resumePoll();
  document.getElementById('orgEditOverlay').classList.remove('open');
  document.body.style.overflow = '';
  oeEditingId = null;
}

function setOeReadOnly(isReadOnly) {
  const body = document.getElementById('orgEditBody');
  body.querySelectorAll('input:not([type=checkbox]), textarea').forEach(el => { el.readOnly = isReadOnly; });
  body.querySelectorAll('select').forEach(el => { el.disabled = isReadOnly; });
  document.getElementById('orgEditFoot').style.display = isReadOnly ? 'none' : '';
}

async function saveOrgEdit() {
  const name = document.getElementById('oe-name').value.trim();
  if (!name) {
    const a = document.getElementById('oeAlert');
    a.textContent = 'ERROR // Designation is required.';
    a.className = 'alert show alert-err';
    return;
  }
  const payload = {
    name,
    org_type:     (() => { const v = document.getElementById('oe-org_type').value; return v === 'Custom' ? (document.getElementById('oe-org_type-custom').value.trim() || null) : (v || null); })(),
    tier:         oeTierVal,
    headquarters: document.getElementById('oe-headquarters').value.trim() || null,
    description:  document.getElementById('oe-description').value.trim() || null,
    notes:        document.getElementById('oe-notes').value.trim() || null,
    is_active:    document.getElementById('oe-is_active').checked,
    leadership:   oeGetLeadership(),
    ally_ids:            oeGetChecked('oeAllyList'),
    enemy_ids:           oeGetChecked('oeEnemyList'),
    revealed_ally_ids:   oeGetRevealed('oeAllyList'),
    revealed_enemy_ids:  oeGetRevealed('oeEnemyList'),
    ltgs:         oeGetLTGs(),
  };
  try {
    const res = await apiFetch(`${API}/organizations/${oeEditingId}`, {
      method: 'PATCH', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload),
    });
    if (!res.ok) await apiThrow(res);
    closeOrgEditModal();
    loadAll();
  } catch(e) {
    const a = document.getElementById('oeAlert');
    a.textContent = `>> TRANSMISSION FAILED // ${e.message}`;
    a.className = 'alert show alert-err';
  }
}

// ── Location Edit Modal ───────────────────────────────────────
let leEditingId = null;

function renderLocDossier(loc) {
  const orgName = loc.controlling_org_id ? (orgStore[loc.controlling_org_id]?.name || '') : '';
  const typeBadge = loc.location_type
    ? `<span class="cc-race-prof ws-loc-type">${esc(loc.location_type.toUpperCase())}</span>` : '';
  const orgLine = orgName
    ? `<div class="loc-org-line"><span class="cc-org-lbl">Controlling Organization ▸</span>&nbsp;<span class="text-amber">${esc(orgName)}</span></div>` : '';
  const fields = [
    ['City',           loc.city],
    ['District',       loc.district],
    ['Security Level', loc.security_level],
  ].filter(([,v]) => v).map(([lbl, val]) =>
    `<div class="loc-dossier-field"><span class="loc-dossier-lbl">${lbl}</span><span class="loc-dossier-val">${esc(val)}</span></div>`
  ).join('');
  const gmSection = isAdminMode() ? `
    <div class="npc-modal-gm">
      <div class="npc-modal-gm-banner">// GM EYES ONLY //</div>
      <div class="npc-modal-section">
        <div class="npc-modal-sec-lbl">Notes</div>
        <textarea id="le-dossier-notes" rows="4" class="ws-notes-ta" placeholder="GM notes...">${esc(loc.notes || '')}</textarea>
        <div id="leNotesFlash" class="ws-flash"></div>
      </div>
    </div>` : '';
  return `
    ${orgLine ? `<div class="mb-12">${orgLine}</div>` : ''}
    ${fields ? `<div class="loc-section">${fields}</div>` : ''}
    ${loc.description ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Intel</div><div class="npc-modal-text">${esc(loc.description)}</div></div>` : ''}
    ${gmSection}`;
}

function onLeLocTypeChange() {
  const val = document.getElementById('le-location_type').value;
  document.getElementById('le-location_type-custom-wrap').style.display = val === 'Custom' ? '' : 'none';
}

function openLocEditModal(locId) {
  const loc = locStore[locId];
  if (!loc) return;
  pausePoll();
  leEditingId = locId;
  document.getElementById('leTitle').textContent =
    isAdminMode() ? `Edit // ${loc.name}` : `Site Report // ${loc.name}`;
  // set type badge in header
  const badge = document.getElementById('leBadge');
  if (badge) badge.innerHTML = loc.location_type
    ? `<span class="cc-race-prof ws-loc-type">${esc(loc.location_type.toUpperCase())}</span>` : '';
  if (isAdminMode()) {
    document.getElementById('locDossierView').style.display = 'none';
    document.getElementById('locFormContent').style.display = '';
    document.getElementById('locEditFoot').style.display = '';
    document.getElementById('le-name').value = loc.name || '';
  // Populate type dropdown — handle Custom values
  const leLocTypeVal = loc.location_type || '';
  const leLocTypeSel = document.getElementById('le-location_type');
  const leLocTypeOpts = Array.from(leLocTypeSel.options).map(o => o.value);
  if (!leLocTypeVal || leLocTypeOpts.includes(leLocTypeVal)) {
    leLocTypeSel.value = leLocTypeVal;
    document.getElementById('le-location_type-custom').value = '';
    document.getElementById('le-location_type-custom-wrap').style.display = 'none';
  } else {
    leLocTypeSel.value = 'Custom';
    document.getElementById('le-location_type-custom').value = leLocTypeVal;
    document.getElementById('le-location_type-custom-wrap').style.display = '';
  }
    document.getElementById('le-city').value = loc.city || '';
    document.getElementById('le-district').value = loc.district || '';
    document.getElementById('le-security_level').value = loc.security_level || '';
    document.getElementById('le-description').value = loc.description || '';
    document.getElementById('le-notes').value = loc.notes || '';
    const sel = document.getElementById('le-controlling_org_id');
    sel.innerHTML = '<option value="">— Independent / Unknown —</option>' +
      Object.values(orgStore).map(o => `<option value="${o.id}"${o.id===loc.controlling_org_id?' selected':''}>${esc(o.name)}</option>`).join('');
    document.getElementById('leAlert').className = 'alert';
  } else {
    document.getElementById('locFormContent').style.display = 'none';
    document.getElementById('locEditFoot').style.display = 'none';
    const dv = document.getElementById('locDossierView');
    dv.innerHTML = renderLocDossier(loc);
    dv.style.display = '';
    if (isAdminMode()) {
      document.getElementById('locEditFoot').innerHTML =
        `<button class="btn btn-green" onclick="saveLocNotes()" style="flex:1;justify-content:center">>> Save Notes</button>
         <button class="btn" onclick="closeLocEditModal()" style="color:var(--text-dim);border-color:#222">Cancel</button>`;
      document.getElementById('locEditFoot').style.display = '';
    }
  }
  document.getElementById('locEditOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLocEditModal() {
  resumePoll();
  document.getElementById('locEditOverlay').classList.remove('open');
  document.getElementById('locDossierView').style.display = 'none';
  document.getElementById('locFormContent').style.display = '';
  document.body.style.overflow = '';
  leEditingId = null;
}

async function saveLocNotes() {
  const notes = document.getElementById('le-dossier-notes')?.value.trim() || '';
  const flash = document.getElementById('leNotesFlash');
  try {
    const res = await apiFetch(`${API}/locations/${leEditingId}`, {
      method: 'PATCH', headers: {'Content-Type':'application/json'}, body: JSON.stringify({ notes }),
    });
    if (!res.ok) await apiThrow(res);
    if (locStore[leEditingId]) locStore[leEditingId].notes = notes;
    if (flash) { flash.style.color = 'var(--green)'; flash.textContent = '// notes saved'; setTimeout(()=>flash.textContent='', 2500); }
  } catch(e) {
    if (flash) { flash.style.color = 'var(--red)'; flash.textContent = `>> ERROR // ${e.message}`; }
  }
}

async function saveLocEdit() {
  const name = document.getElementById('le-name').value.trim();
  if (!name) {
    const a = document.getElementById('leAlert');
    a.textContent = 'ERROR // Name is required.';
    a.className = 'alert show alert-err';
    return;
  }
  const ctrlVal = document.getElementById('le-controlling_org_id').value;
  let leLocType = document.getElementById('le-location_type').value;
  if (leLocType === 'Custom') leLocType = document.getElementById('le-location_type-custom').value.trim() || null;
  const payload = {
    name,
    location_type:      leLocType,
    city:               document.getElementById('le-city').value.trim() || null,
    district:           document.getElementById('le-district').value.trim() || null,
    security_level:     document.getElementById('le-security_level').value || null,
    controlling_org_id: ctrlVal ? parseInt(ctrlVal) : null,
    description:        document.getElementById('le-description').value.trim() || null,
    notes:              document.getElementById('le-notes').value.trim() || null,
  };
  try {
    const res = await apiFetch(`${API}/locations/${leEditingId}`, {
      method: 'PATCH', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload),
    });
    if (!res.ok) await apiThrow(res);
    closeLocEditModal();
    loadAll();
  } catch(e) {
    const a = document.getElementById('leAlert');
    a.textContent = `>> TRANSMISSION FAILED // ${e.message}`;
    a.className = 'alert show alert-err';
  }
}

// ── Character Edit Modal ──────────────────────────────────────
let ceEditingId  = null;
let ceFullArchHtml = null; // cached full archetype dropdown HTML, set on first openCharEditModal call

// Toggle read-only state on all dossier fields (except GM Notes, which is always editable)
function setCeDossierMode(readOnly) {
  const body = document.getElementById('charEditBody');
  if (readOnly) {
    body.classList.add('ce-view-mode');
    // Replace select fields with static text spans
    const archSel = document.getElementById('ce-archetype');
    const archVal = archSel.value === 'Custom'
      ? document.getElementById('ce-arch-custom').value
      : archSel.value;
    document.getElementById('ce-archetype-val').textContent = archVal || '—';
    document.getElementById('ce-archetype-val').style.display = 'block';
    archSel.style.display = 'none';
    document.getElementById('ce-arch-custom-wrap').style.display = 'none';
    const raceSel = document.getElementById('ce-race');
    document.getElementById('ce-race-val').textContent = raceSel.options[raceSel.selectedIndex]?.text || '—';
    document.getElementById('ce-race-val').style.display = 'block';
    raceSel.style.display = 'none';
    const orgSel = document.getElementById('ce-org_id');
    document.getElementById('ce-org_id-val').textContent = orgSel.options[orgSel.selectedIndex]?.text || '—';
    document.getElementById('ce-org_id-val').style.display = 'block';
    orgSel.style.display = 'none';
    // Hide type/active toggles (edit-only concept)
    document.getElementById('ceTypeActiveRow').style.display = 'none';
  } else {
    body.classList.remove('ce-view-mode');
    // Restore selects, hide static spans
    ['ce-archetype','ce-race','ce-org_id'].forEach(id => {
      document.getElementById(id).style.display = '';
      document.getElementById(id + '-val').style.display = 'none';
    });
    document.getElementById('ceTypeActiveRow').style.display = '';
  }
}

function onCeArchChange() {
  const sel = document.getElementById('ce-archetype');
  document.getElementById('ce-arch-custom-wrap').style.display = sel.value === 'Custom' ? '' : 'none';
}

function cePcToggle() {
  const isPC = document.getElementById('ce-is_pc').checked;
  document.getElementById('cePcLbl').textContent = isPC ? 'PC // Runner' : 'NPC';
  document.getElementById('ceNpcSection').style.display = isPC ? 'none' : '';
}

function openCharEditModal(charId) {
  const char = charMapStore[charId];
  if (!char) return;
  pausePoll();
  const archSel = document.getElementById('ce-archetype');

  // Cache the full archetype dropdown HTML the first time so we can restore it for NPC edit mode
  if (!ceFullArchHtml) ceFullArchHtml = archSel.innerHTML;

  ceEditingId = charId;

  // Populate common fields
  document.getElementById('ce-name').value             = char.name             || '';
  document.getElementById('ce-race').value             = char.race || 'Human';
  document.getElementById('ce-gender').value           = char.gender            || '';
  document.getElementById('ce-age').value              = char.age               || '';
  document.getElementById('ce-nationality').value      = char.nationality        || '';
  document.getElementById('ce-is_pc').checked          = char.is_pc             || false;
  document.getElementById('ce-is_active').checked      = char.is_active         !== false;
  document.getElementById('ce-description').value      = char.description        || '';
  document.getElementById('ce-background').value       = char.background         || '';
  document.getElementById('ce-notes').value            = char.notes              || '';
  document.getElementById('ce-connection').value       = char.connection         ?? 1;
  document.getElementById('ce-contact_skills').value   = (char.contact_skills || []).join('\n');

  const orgSel = document.getElementById('ce-org_id');
  orgSel.innerHTML = '<option value="">— Independent / Unknown —</option>' +
    Object.values(orgStore).map(o =>
      `<option value="${o.id}"${o.id === char.organization_id ? ' selected' : ''}>${esc(o.name)}</option>`
    ).join('');

  if (char.is_pc) {
    // ── DOSSIER MODE (PC) ─────────────────────────────────────
    document.getElementById('ceTitle').textContent = `Dossier // ${char.name}`;
    const ceRaceProf = [char.race, char.title || char.archetype].filter(Boolean).join(' | ');
    document.getElementById('ceBadge').innerHTML = ceRaceProf
      ? `<span class="cc-race-prof ${archetypeClass(char.archetype || '')}">${esc(ceRaceProf)}</span>` : '';

    const org = char.organization_id ? orgStore[char.organization_id] : null;
    const metaItems = [];
    if (char.gender)      metaItems.push(['Gender', char.gender]);
    if (char.age)         metaItems.push(['Age', char.age]);
    if (char.nationality) metaItems.push(['Nationality', char.nationality]);
    metaItems.push(['Affiliation', org ? org.name : '[Independent]']);

    const sep = `<span class="cc-org-sep" style="margin-bottom:2px">//</span>`;
    const metaHtml = metaItems.map(([lbl, val], i) =>
      `${i > 0 ? sep : ''}<div style="display:flex;flex-direction:column;gap:2px">` +
      `<span style="font-size:0.5rem;letter-spacing:2px;color:var(--green);text-shadow:var(--glow-green);text-transform:uppercase">${lbl}</span>` +
      `<span style="font-size:0.78rem;color:var(--text)">${esc(String(val))}</span></div>`
    ).join('');

    document.getElementById('ceFormBody').style.display = 'none';
    const pcBody = document.getElementById('pcDossierBody');
    pcBody.style.display = '';
    pcBody.innerHTML =
      `<div style="display:flex;gap:10px;align-items:flex-end;flex-wrap:wrap;margin-bottom:16px">${metaHtml}</div>` +
      (char.description ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Profile</div><div class="npc-modal-text">${esc(char.description)}</div></div>` : '') +
      (char.background  ? `<div class="npc-modal-section"><div class="npc-modal-sec-lbl">Background</div><div class="npc-modal-text">${esc(char.background)}</div></div>` : '') +
      `<div class="npc-modal-gm-banner gm-only">// GM EYES ONLY //</div>` +
      `<div class="field gm-only"><textarea id="pcNotesInput" rows="4" class="ws-notes-ta">${esc(char.notes || '')}</textarea></div>`;

    document.getElementById('ceSaveBtn').textContent = '>> Save Notes';
    document.getElementById('ceAlert').className = 'alert';
    document.getElementById('charEditOverlay').classList.add('open');
    document.body.style.overflow = 'hidden';
    return;

  } else {
    // ── EDIT MODE (NPC) ───────────────────────────────────────
    document.getElementById('pcDossierBody').style.display = 'none';
    document.getElementById('ceFormBody').style.display = '';
    document.getElementById('ceTitle').textContent = `Edit // ${char.name}`;
    document.getElementById('ceBadge').innerHTML = '';
    document.getElementById('ce-title-field').style.display = '';
    document.getElementById('ce-title').value = char.title || '';

    // Restore full archetype dropdown
    archSel.innerHTML = ceFullArchHtml;
    const arch = char.archetype || '';
    const known = Array.from(archSel.options).map(o => o.value);
    if (known.includes(arch)) {
      archSel.value = arch;
      document.getElementById('ce-arch-custom-wrap').style.display = 'none';
    } else {
      archSel.value = 'Custom';
      document.getElementById('ce-arch-custom-wrap').style.display = '';
      document.getElementById('ce-arch-custom').value = arch;
    }

    setCeDossierMode(false);
    document.getElementById('ceSaveBtn').textContent = '>> Save Changes';
    cePcToggle();
  }

  document.getElementById('ceAlert').className = 'alert';
  document.getElementById('charEditOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeCharEditModal() {
  resumePoll();
  document.getElementById('charEditOverlay').classList.remove('open');
  document.body.style.overflow = '';
  ceEditingId = null;
}

async function saveCharEdit() {
  const char = charMapStore[ceEditingId];

  // ── PC DOSSIER MODE: only save GM Notes ──────────────────────
  if (char?.is_pc) {
    try {
      const res = await apiFetch(`${API}/characters/${ceEditingId}`, {
        method: 'PATCH', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({ notes: document.getElementById('pcNotesInput').value.trim() || null }),
      });
      if (!res.ok) await apiThrow(res);
      closeCharEditModal();
      loadAll();
    } catch(e) {
      const a = document.getElementById('ceAlert');
      a.textContent = `>> TRANSMISSION FAILED // ${e.message}`;
      a.className = 'alert show alert-err';
    }
    return;
  }

  // ── NPC EDIT MODE: full save ──────────────────────────────────
  const name  = document.getElementById('ce-name').value.trim();
  const title = document.getElementById('ce-title').value.trim();
  if (!name || !title) {
    const a = document.getElementById('ceAlert');
    a.textContent = `ERROR // ${!name ? 'Name' : 'Title'} is required.`;
    a.className = 'alert show alert-err';
    return;
  }
  const archSel = document.getElementById('ce-archetype');
  const arch = archSel.value === 'Custom'
    ? document.getElementById('ce-arch-custom').value.trim()
    : archSel.value;
  const isPC = document.getElementById('ce-is_pc').checked;
  const orgVal = document.getElementById('ce-org_id').value;
  const race = document.getElementById('ce-race').value;
  const payload = {
    name,
    title:           title || null,
    archetype:       arch || null,
    race:            race || null,
    gender:          document.getElementById('ce-gender').value.trim() || null,
    age:             parseInt(document.getElementById('ce-age').value) || null,
    nationality:     document.getElementById('ce-nationality').value.trim() || null,
    is_pc:           isPC,
    is_active:       document.getElementById('ce-is_active').checked,
    organization_id: orgVal ? parseInt(orgVal) : null,
    description:     document.getElementById('ce-description').value.trim() || null,
    background:      document.getElementById('ce-background').value.trim() || null,
    notes:           document.getElementById('ce-notes').value.trim() || null,
  };
  payload.connection     = parseInt(document.getElementById('ce-connection').value) || 1;
  payload.contact_skills = document.getElementById('ce-contact_skills').value.split('\n').map(s => s.trim()).filter(Boolean);
  try {
    const res = await apiFetch(`${API}/characters/${ceEditingId}`, {
      method: 'PATCH', headers: {'Content-Type':'application/json'}, body: JSON.stringify(payload),
    });
    if (!res.ok) await apiThrow(res);
    closeCharEditModal();
    loadAll();
  } catch(e) {
    const a = document.getElementById('ceAlert');
    a.textContent = `>> TRANSMISSION FAILED // ${e.message}`;
    a.className = 'alert show alert-err';
  }
}

// ── Main data load ────────────────────────────────────────────
async function loadAll() {
  try {
    const [orgsRes, locsRes, charsRes, contactsRes, statsRes, mineRes] = await Promise.all([
      apiFetch(`${API}/organizations/`),
      apiFetch(`${API}/locations/`),
      apiFetch(`${API}/characters/`),
      apiFetch(`${API}/contacts/`),
      apiFetch(`${API}/runs/party-stats`),
      apiFetch(`${API}/characters/mine`),
    ]);
    for (const [label, res] of [['organizations', orgsRes], ['locations', locsRes], ['characters', charsRes], ['contacts', contactsRes]]) {
      if (!res.ok) throw new Error(`Failed to load ${label} (HTTP ${res.status})`);
    }
    const [orgs, locs, chars, contacts, stats, mineData] = await Promise.all([
      orgsRes.json(), locsRes.json(), charsRes.json(), contactsRes.json(),
      statsRes.ok ? statsRes.json() : Promise.resolve(null),
      mineRes.ok ? mineRes.json() : Promise.resolve({ids: []}),
    ]);
    _myCharIds = new Set(mineData.ids || []);

    // ── Wire party stats ──────────────────────────────────────
    if (stats) {
      charRepStore = stats.char_rep || {};
      const heatEl = document.getElementById('sb-heat');
      const repEl  = document.getElementById('sb-rep');
      if (heatEl) {
        heatEl.textContent = isAdminMode()
          ? `${stats.heat_label || 'Neutral'} (${stats.heat ?? 0})`
          : (stats.heat_label || 'Neutral');
        heatEl.style.cssText = heatColorStyle(stats.heat || 0);
      }
      if (repEl) {
        repEl.textContent = stats.team_rep_tier || 'Unknown';
        repEl.style.cssText = repColorStyle(stats.team_rep_score != null ? stats.team_rep_score : 20);
      }
    }

    const pcs        = chars.filter(c => c.is_pc);
    const activePcs  = pcs.filter(c => c.is_active !== false);
    const inactivePcs = pcs.filter(c => c.is_active === false);

    // Merge duplicate contact records (same npc_id) into single cards
    contactStore = contacts;
    // Only count contacts linked to ACTIVE PCs for categorization (inactive PCs hidden, data preserved)
    const activePcIds = new Set(pcs.filter(c => c.is_active).map(c => c.id));
    const activeContacts = contacts.filter(c => activePcIds.has(c.owner_id));
    const mergedContacts = mergeContacts(activeContacts);
    // Build lookup for non-NPC contacts (contacts without a character record)
    nonNpcContactStore = {};
    mergedContacts.forEach(m => { if (!m.npc_id) nonNpcContactStore[m.id] = m; });
    // NPCs who are NOT listed as an active contact's npc_id go in the Known Persons roster
    const contactNpcIds = new Set(activeContacts.map(c => c.npc_id).filter(Boolean));
    const npcs         = chars.filter(c => !c.is_pc && !contactNpcIds.has(c.id));

    document.getElementById('sc-orgs').textContent     = orgs.length;
    document.getElementById('sc-locs').textContent     = locs.length;
    document.getElementById('sc-chars').textContent          = activePcs.length;
    document.getElementById('sc-chars-inactive').textContent = inactivePcs.length;

    const orgMap  = Object.fromEntries(orgs.map(o => [o.id, o]));
    const charMap = Object.fromEntries(chars.map(c => [c.id, c]));
    orgStore     = orgMap;
    charMapStore = charMap;
    locStore     = Object.fromEntries(locs.map(l => [l.id, l]));

    // Active contact count: only merged contacts where NPC is active AND at least one owner row is active
    const activeContactCount = mergedContacts.filter(m => {
      const npc = m.npc_id ? charMap[m.npc_id] : null;
      return (npc ? npc.is_active !== false : true) &&
             (!m.owners || m.owners.length === 0 || m.owners.some(o => o.is_active !== false));
    }).length;
    document.getElementById('sc-contacts').textContent = activeContactCount;

    let html = '';

    // ── 1. Team (expanded) ────────────────────────────────────
    if (pcs.length)
      html += section('pcs', 'Team',
        `<div class="char-grid">${pcs.map(c => buildCharCard(c, orgMap)).join('')}</div>`
        + `<div class="gm-only" style="text-align:left;margin-top:12px"><button class="btn btn-red btn-sm" onclick="resetPcData()">&gt;&gt; RESET ALL PC DATA</button></div>`,
        'manage-characters.html');

    // ── 2. Contacts (expanded) ────────────────────────────────
    if (mergedContacts.length)
      html += section('contacts', 'Contacts',
        `<div class="contact-grid">${mergedContacts.map(c => buildContactCard(c, charMap, orgMap)).join('')}</div>`,
        'manage-characters.html');

    // ── 2.5 Faction Reputation ────────────────────────────────
    html += section('factions', 'Faction Reputation',
      buildFactionRepSection(activePcs, charRepStore, getMyCharIds()));

    // ── 3. Persons of Interest (expanded) ─────────────────────
    if (npcs.length)
      html += section('npcs', 'Persons of Interest',
        `<div class="char-grid">${npcs.map(c => buildCharCard(c, orgMap)).join('')}</div>`,
        'manage-characters.html');

    // ── 4. Organizations (collapsed) ─────────────────────────
    const activeOrgs = orgs.filter(o => o.is_active);
    const byGroup = {};
    activeOrgs.forEach(o => {
      const g = TYPE_GROUP[o.org_type] || 'other';
      (byGroup[g] = byGroup[g] || []).push(o);
    });
    ORG_ORDER.forEach(group => {
      const orgsInGroup = byGroup[group];
      if (!orgsInGroup?.length) return;
      orgsInGroup.sort((a,b) => b.tier - a.tier || a.name.localeCompare(b.name));
      html += section(`org-${group}`, ORG_LABELS[group] || group,
        `<div class="org-grid">${orgsInGroup.map(o => buildOrgCard(o, orgMap)).join('')}</div>`,
        'manage-organizations.html', true);
    });

    // ── 5. Locations (collapsed) ──────────────────────────────
    if (locs.length)
      html += section('locs', 'Known Locations',
        `<div class="loc-grid">${locs.map(l => buildLocCard(l, orgMap)).join('')}</div>`,
        'manage-locations.html', true);

    document.getElementById('worldContent').innerHTML =
      html || '<div class="loading">No world data found — run the seed script.</div>';

  } catch(e) {
    document.getElementById('worldContent').innerHTML =
      `<div class="alert alert-err show">>> CONNECTION FAILED // ${e.message}</div>`;
  }
}

async function claimChar(charId) {
  try {
    const res = await apiFetch(`${API}/characters/${charId}/claim`, {
      method: 'POST',
    });
    if (!res.ok) {
      const err = await res.json().catch(() => ({ detail: res.statusText }));
      throw new Error(err.detail);
    }
    await loadAll();
  } catch(e) {
    showAlert(`Claim failed: ${e.message}`);
  }
}

async function releaseChar(charId) {
  showConfirm('Release this character? You will lose ownership but all data is preserved.', async () => {
    try {
      const res = await apiFetch(`${API}/characters/${charId}/unclaim`, {
        method: 'POST',
      });
      if (!res.ok) {
        const err = await res.json().catch(() => ({ detail: res.statusText }));
        throw new Error(err.detail);
      }
      await loadAll();
    } catch(e) {
      showAlert(`Release failed: ${e.message}`);
    }
  }, 'Release');
}

// ── Styled dialog utilities (replace native confirm/alert/prompt) ────────
function showConfirm(message, onOk, confirmLabel = 'Confirm') {
  pausePoll();
  document.getElementById('srConfirmMsg').textContent = message;
  document.getElementById('srConfirmOkBtn').textContent = '>> ' + confirmLabel;
  document.getElementById('srConfirmOverlay').classList.add('open');
  document.getElementById('srConfirmOkBtn').onclick = () => {
    resumePoll();
    document.getElementById('srConfirmOverlay').classList.remove('open');
    if (onOk) onOk();
  };
  document.getElementById('srConfirmCancelBtn').onclick = () => {
    resumePoll();
    document.getElementById('srConfirmOverlay').classList.remove('open');
  };
}

function closeAlert() {
  resumePoll();
  document.getElementById('srAlertOverlay').classList.remove('open');
}

function showAlert(message) {
  pausePoll();
  document.getElementById('srAlertMsg').textContent = message;
  document.getElementById('srAlertOverlay').classList.add('open');
}

function showPrompt(message, defaultVal, onOk) {
  pausePoll();
  const overlay = document.getElementById('srPromptOverlay');
  // Use classList.add/remove('open') — ltg-overlay CSS controls visibility via opacity/pointer-events
  const input   = document.getElementById('srPromptInput');
  document.getElementById('srPromptMsg').textContent = message;
  input.value = defaultVal ?? '';
  overlay.classList.add('open');
  setTimeout(() => { input.focus(); input.select(); }, 50);
  document.getElementById('srPromptOkBtn').onclick = () => {
    resumePoll();
    overlay.classList.remove('open');
    if (onOk) onOk(input.value);
  };
  document.getElementById('srPromptCancelBtn').onclick = () => {
    resumePoll();
    overlay.classList.remove('open');
  };
  input.onkeydown = (e) => {
    if (e.key === 'Enter')  document.getElementById('srPromptOkBtn').click();
    if (e.key === 'Escape') document.getElementById('srPromptCancelBtn').click();
  };
}

bootstrapAuth().then(u => { if (u) { loadAll(); startPolling(loadAll); } });

(function() {
  function pad(n) { return String(n).padStart(2, '0'); }
  let lastDateStr = new Date().toDateString();
  function tick() {
    const t = new Date();
    const srYear = t.getFullYear() + YEAR_OFFSET;
    const month  = t.toLocaleString('en-US', { month: 'long' }).toUpperCase();
    document.getElementById('srDate').textContent    = `${month} ${t.getDate()} ${srYear}`;
    document.getElementById('liveClock').textContent = `${pad(t.getHours())}:${pad(t.getMinutes())}:${pad(t.getSeconds())}`;
    // Refresh world data at midnight so heat decay is recalculated
    const newDateStr = t.toDateString();
    if (newDateStr !== lastDateStr) {
      lastDateStr = newDateStr;
      loadAll();
    }
  }
  tick();
  setInterval(tick, 1000);
})();
