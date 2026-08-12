/* =============================================================
   Character Builder engine (only on character-builder.html).
   Guided & flexible SR2 chargen wizard -> filled PDF export.
   Reads: builder-data.js + the catalogue data files + pdf-lib.
   ============================================================= */
(() => {
  "use strict";
  const root = document.getElementById("cb");
  if (!root) return;

  const LETTERS = ["A", "B", "C", "D", "E"];
  const PR = window.SR2_PRIORITY, META = window.SR2_METATYPES, MR = window.SR2_MAGIC_RULES;
  const CG = window.SR2_CHARGEN, ATTRS = window.SR2_ATTRS, ALABEL = window.SR2_ATTR_LABEL;
  const SKILLS = window.SR2_SKILLS || [];
  const STEPS = ["Priorities", "Metatype", "Attributes", "Magic", "Skills", "Resources", "Finish & Export"];
  const KEY = "sr2_builder_v1";

  /* ---------- helpers ---------- */
  const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  const money = (n) => (Number(n) || 0).toLocaleString("en-US") + "Y";
  const num = (v) => { const m = String(v ?? "").match(/-?\d+(\.\d+)?/); return m ? parseFloat(m[0]) : 0; };
  const clampNum = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

  /* ---------- state ---------- */
  function freshState() {
    return {
      step: 0,
      prio: { race: "", magic: "", attributes: "", skills: "", resources: "" },
      metatype: "Human",
      base: { body: 1, quickness: 1, strength: 1, charisma: 1, intelligence: 1, willpower: 1 },
      magicType: "Mundane",
      tradition: "", totem: "",
      spells: [], powers: [], foci: [], skills: [],
      deck: "", persona: { bod: 0, evasion: 0, masking: 0, sensors: 0 }, programs: [],
      gear: { weapons: [], armor: [], cyber: [], vehicles: [], other: [] },
      identity: { name: "", sex: "", age: "", desc: "", lifestyle: "Low" },
      contacts: [],            // [{ name, archetype, level: "Contact"|"Buddy" }]
      nativeLanguage: "",      // free, rating = Intelligence + 2 (SR2 p.45)
      streetDialect: "",       // Street lifestyle: free dialect at 1/2 Intelligence
      languages: [],           // [{ name, rating }] -- bought from the skill pool
    };
  }
  let state = mergeDefaults(load());
  // Fill in any keys missing from an older saved character (e.g. pre-Matrix
  // states have no deck/persona/programs) so new code never reads undefined.
  function mergeDefaults(loaded) {
    const s = freshState();
    if (!loaded || typeof loaded !== "object") return s;
    const out = { ...s, ...loaded };
    out.persona = { ...s.persona, ...(loaded.persona || {}) };
    out.gear = { ...s.gear, ...(loaded.gear || {}) };
    out.identity = { ...s.identity, ...(loaded.identity || {}) };
    out.base = { ...s.base, ...(loaded.base || {}) };
    out.prio = { ...s.prio, ...(loaded.prio || {}) };
    ["spells", "powers", "foci", "skills", "programs", "contacts", "languages"].forEach(k => { if (!Array.isArray(out[k])) out[k] = []; });
    ["weapons", "armor", "cyber", "vehicles", "other"].forEach(k => { if (!Array.isArray(out.gear[k])) out.gear[k] = []; });
    // Migrate pre-v2 contacts (plain strings) to objects.
    out.contacts = out.contacts.map(c => typeof c === "string"
      ? { name: c, archetype: "", level: "Contact" }
      : { name: c.name || "", archetype: c.archetype || "", level: c.level === "Buddy" ? "Buddy" : "Contact" });
    if (typeof out.nativeLanguage !== "string") out.nativeLanguage = "";
    if (typeof out.streetDialect !== "string") out.streetDialect = "";
    // Refresh each saved skill's linked attribute/group from the catalogue, so
    // data corrections (e.g. combat skills are Quickness-linked, SR2 p.69) apply
    // to characters that were saved before the fix.
    out.skills = out.skills.map(sk => {
      const d = (window.SR2_SKILLS || []).find(x => x.n === sk.name);
      return d ? { ...sk, attr: d.attr, group: d.group } : sk;
    });
    // Backfill rating/level on rated 'ware & powers saved before they were rated.
    out.gear.cyber.forEach(c => {
      const d = (window.CYBERWARE || []).find(x => x.n === c.n);
      if (d && d.rated && (c.rating == null)) { c.rating = 1; c.ess = d.essTbl[0]; c.cost = d.costTbl[0]; }
    });
    out.powers.forEach(p => {
      const d = (window.ADEPT_POWERS || []).find(x => x.n === p.name);
      if (d && d.rated) { if (p.lvl == null) p.lvl = 1; if (d.attrChoice && !p.attr) p.attr = "body"; }
    });
    return out;
  }
  function load() { try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(state)); } catch (e) {} flashSaved(); }
  function flashSaved() { const s = document.getElementById("cb-save"); if (s) { s.classList.add("is-on"); clearTimeout(flashSaved._t); flashSaved._t = setTimeout(() => s.classList.remove("is-on"), 700); } }

  /* ---------- catalogue resolution + archetypes ---------- */
  function findCat(arr, name) {
    if (!arr) return null;
    const n = String(name).toLowerCase();
    return arr.find(x => x.n.toLowerCase() === n) || arr.find(x => x.n.toLowerCase().includes(n)) || null;
  }
  function resolveGear(kind, name) {
    const map = { weapons: window.WEAPONS, armor: window.ARMOR, cyber: window.CYBERWARE, vehicles: window.GEAR, other: window.GEAR };
    const it = findCat(map[kind], name);
    const cost = it && typeof it.cost === "number" ? it.cost : 0;
    if (kind === "weapons") return it ? { n: it.n, sub: it.sub, conceal: it.conceal, reach: it.reach, mode: it.mode, ammo: it.ammo, dmg: it.dmg, notes: it.notes || [], cost } : { n: name, notes: [], cost: 0 };
    if (kind === "armor") return it ? { n: it.n, ballistic: it.ballistic, impact: it.impact, cost } : { n: name, cost: 0 };
    if (kind === "cyber") return it ? { n: it.n, ess: num(it.ess), cost } : { n: name, ess: 0, cost: 0 };
    if (kind === "vehicles") return it ? { n: it.n, sub: it.sub || it.cat, stats: it.stats || [], notes: it.notes || [], cost } : { n: name, stats: [], notes: [], cost: 0 };
    return it ? { n: it.n, sub: it.sub || it.cat, cost } : { n: name, cost: 0 };
  }
  function applyArchetype(key) {
    const a = window.SR2_ARCHETYPES[key]; if (!a) return;
    const filled = ["prio", "metatype", "base", "magicType", "skills", "spells", "powers", "gear"].some(() => state.skills.length || prioLettersUsed().length || state.gear.weapons.length);
    if (filled && !confirm(`Load the "${a.name}" starter kit? This replaces your current character.`)) return;
    const s = freshState();
    s.prio = { ...a.prio }; s.metatype = a.metatype; s.magicType = a.magicType; s.base = { ...a.base };
    s.tradition = a.tradition || ""; s.totem = a.totem || "";
    s.skills = (a.skills || []).map(([name, rating]) => { const d = SKILLS.find(x => x.n === name) || {}; return { name, rating, attr: d.attr || "", group: d.group || "" }; });
    s.spells = (a.spells || []).map(([name, force]) => { const sp = findCat(window.SR2_SPELLS, name); return sp ? { name: sp.n, type: sp.cat || sp.typ || "", drain: sp.drn || "", target: sp.rng || "", duration: sp.dur || "", force } : { name, type: "", drain: "", target: "", duration: "", force }; });
    s.powers = (a.powers || []).map(name => { const p = findCat(window.ADEPT_POWERS, name); if (!p) return { name, pp: 0 }; const np = { name: p.n, pp: num(p.pp) }; if (p.rated) { np.lvl = 1; if (p.attrChoice) np.attr = "body"; } return np; });
    s.deck = a.deck || "";
    s.persona = { bod: 0, evasion: 0, masking: 0, sensors: 0, ...(a.persona || {}) };
    s.programs = (a.programs || []).map(([name, rating]) => ({ name, rating, cost: 0 }));
    s.gear = {
      weapons: (a.gear.weapons || []).map(n => resolveGear("weapons", n)),
      armor: (a.gear.armor || []).map(n => resolveGear("armor", n)),
      cyber: (a.gear.cyber || []).map(n => resolveGear("cyber", n)),
      vehicles: (a.gear.vehicles || []).map(n => resolveGear("vehicles", n)),
      other: (a.gear.other || []).map(n => resolveGear("other", n)),
    };
    state = s; save(); render();
  }

  /* ---------- shop-item rendering (expandable detail + add) ---------- */
  function detailHTML(desc, bullets, statline) {
    let h = "";
    if (desc) h += `<p class="cb-det__desc">${esc(desc)}</p>`;
    if (bullets && bullets.length) h += `<ul class="cb-det__fx">${bullets.map(b => `<li>${esc(b)}</li>`).join("")}</ul>`;
    if (statline) h += `<p class="cb-det__stat">${statline}</p>`;
    return h || `<p class="cb-det__desc">No details.</p>`;
  }
  function shopRow(name, meta, detail, addAttr, taken, img) {
    const thumb = img ? `<img class="cb-shopitem__art" loading="lazy" src="${esc(img)}" alt="">` : "";
    return `<div class="cb-shopitem ${taken ? "is-taken" : ""}">
      ${thumb}
      <details class="cb-det"><summary><span class="cb-det__name">${esc(name)}</span><em>${esc(meta || "")}</em></summary>${detail}</details>
      <button type="button" class="cb-add" ${addAttr}>+</button></div>`;
  }
  const SHOP_ART_KIND = { weapons: "weapons", armor: "armor", cyber: "cyber", vehicles: "vehicle", other: "gear" };
  const shopArt = (tabKey, name) => (window.SR2_ART_LOOKUP ? window.SR2_ART_LOOKUP(SHOP_ART_KIND[tabKey] || tabKey, name) : null);
  function gearDetail(it, kind) {
    const bullets = it.effect || it.notes || [];
    let extra = "";
    if (kind === "weapons") extra = [it.dmg && ("Dmg " + it.dmg), it.mode && ("Mode " + it.mode), (it.conceal != null) && ("Conceal " + it.conceal), it.ammo && ("Ammo " + it.ammo)].filter(Boolean).join(" - ");
    else if (kind === "armor") extra = `Ballistic ${it.ballistic ?? "--"} - Impact ${it.impact ?? "--"}`;
    else if (kind === "cyber") {
      const e = num(it.ess);
      const proj = awakened() ? Math.max(0, Math.floor(CG.startEssence - (cyberEssence() + e))) : null;
      extra = `Essence ${it.ess ?? "--"}` + (proj != null ? ` - <span class="cb-warnpill">Magic -> ${proj}</span>` : "");
    }
    else if (kind === "vehicles") extra = (it.stats || []).map(s => `${s[0]} ${s[1]}`).join(" - ");
    const price = typeof it.cost === "number" ? money(it.cost) : (it.cost || "--");
    return detailHTML(it.desc, bullets, `${extra}${extra ? " - " : ""}Cost ${esc(price)}`);
  }
  const HELP = (href, label) => `<a class="cb-help" href="${href}" target="_blank" rel="noopener">${esc(label)} ?</a>`;

  /* ---------- derived calcs ---------- */
  const isMeta = () => state.prio.race === "A";
  function metatype() { return META[state.metatype] || META.Human; }
  const cyberDef = (name) => (window.CYBERWARE || []).find(x => x.n === name) || null;
  const powerDef = (name) => (window.ADEPT_POWERS || []).find(x => x.n === name) || null;
  const ratedEss = (it, r) => it && it.essTbl ? (it.essTbl[clampNum(r, 1, it.maxRating) - 1] || 0) : 0;
  const ratedCost = (it, r) => it && it.costTbl ? (it.costTbl[clampNum(r, 1, it.maxRating) - 1] || 0) : 0;
  /* PP cost of an adept power: rated powers cost by level (a flat table for
     Increased Reflexes, or escalating per-+1 tiers summed for the rest). */
  function powerPP(p) {
    const it = powerDef(p.name);
    if (!it || !it.rated) return Number(p.pp) || 0;
    const lvl = clampNum(p.lvl || 1, 1, it.maxLevel);
    if (it.ppTbl) return it.ppTbl[lvl - 1] || 0;
    if (it.ppTier) { let pp = 0; for (let i = 1; i <= lvl; i++) pp += it.ppTier[Math.min(i - 1, it.ppTier.length - 1)]; return pp; }
    return Number(p.pp) || 0;
  }
  /* Augmentation modifiers -- sum structured `mods` (fixed) and `modsPer`xrating
     (rated) from installed cyber/bioware, plus rated adept powers (modsPerxlevel,
     and modsAttrxlevel applied to the chosen attribute). Attribute keys feed back
     through finalAttr; `reaction`/`initDice` are flat derived-stat bonuses. All
     cumulative across every installed item / power. (SR2 reaction & attribute boosters.) */
  function augMods() {
    const t = {};
    const add = (k, v) => { if (k && v) t[k] = (t[k] || 0) + v; };
    state.gear.cyber.forEach(c => {
      const it = cyberDef(c.n); if (!it) return;
      if (it.mods) for (const k in it.mods) add(k, Number(it.mods[k]) || 0);
      if (it.rated && it.modsPer) { const r = clampNum(c.rating || 1, 1, it.maxRating); for (const k in it.modsPer) add(k, (Number(it.modsPer[k]) || 0) * r); }
    });
    state.powers.forEach(p => {
      const it = powerDef(p.name); if (!it || !it.rated) return;
      const lvl = clampNum(p.lvl || 1, 1, it.maxLevel);
      if (it.modsPer) for (const k in it.modsPer) add(k, (Number(it.modsPer[k]) || 0) * lvl);
      if (it.modsAttr && p.attr) add(p.attr, (Number(it.modsAttr) || 0) * lvl);
    });
    return t;
  }
  function finalAttr(a) {
    const mod = (metatype().mods || {})[a] || 0;
    const aug = augMods()[a] || 0;            // cyber/bioware can push past the natural max
    const max = (metatype().max || {})[a] || 6;
    const total = (state.base[a] || 1) + mod + aug;
    return clampNum(total, 1, Math.max(max, total));
  }
  const finalAttrs = () => { const o = {}; ATTRS.forEach(a => o[a] = finalAttr(a)); return o; };
  const reaction = () => Math.floor((finalAttr("quickness") + finalAttr("intelligence")) / 2) + (augMods().reaction || 0);
  const initDice = () => 1 + (augMods().initDice || 0);
  const combatPool = () => Math.floor((finalAttr("quickness") + finalAttr("intelligence") + finalAttr("willpower")) / 2);
  const cyberEssence = () => state.gear.cyber.reduce((t, c) => t + (Number(c.ess) || 0), 0);
  const essence = () => Math.max(0, CG.startEssence - cyberEssence());
  const awakened = () => state.magicType === "Full Mage" || state.magicType === "Adept";
  const magicRating = () => awakened() ? Math.floor(essence()) : 0;

  /* budgets */
  const attrBudget = () => PR.attributes[state.prio.attributes] || 0;
  const attrSpent = () => ATTRS.reduce((t, a) => t + (state.base[a] || 0), 0);
  const skillBudget = () => PR.skills[state.prio.skills] || 0;
  /* Skills + bought languages share the one pool (SR2 p.45); native language and
     a Street dialect are free, so only state.languages count here. */
  const languagesSpent = () => state.languages.reduce((t, l) => t + (Number(l.rating) || 0), 0);
  const skillSpent = () => state.skills.reduce((t, s) => t + (Number(s.rating) || 0), 0) + languagesSpent();
  const res = () => PR.resources[state.prio.resources] || { nuyen: 0, fp: 0 };
  /* Foci: each focus costs nuyen (from the nuyen budget) AND Force Points equal
     to its bonding Karma (SR2 p.137/p.263). Force Points stand in for bonding
     Karma at chargen. */
  const focusDef = (name) => (window.SR2_FOCI || []).find(f => f.n === name) || null;
  function focusNuyen(f, rating) {
    if (!f) return 0;
    if (f.nuyenFlat != null) return f.nuyenFlat;
    return (f.nuyenBase || 0) + (f.nuyenPer || 0) * (Number(rating) || 1);
  }
  function focusKarma(f, rating) {
    if (!f) return 0;
    if (f.karmaFlat != null) return f.karmaFlat;
    return (f.karmaPer || 0) * (Number(rating) || 1);
  }
  const fociNuyen = () => awakened() ? state.foci.reduce((t, x) => t + focusNuyen(focusDef(x.type), x.rating), 0) : 0;
  const fociFp = () => awakened() ? state.foci.reduce((t, x) => t + focusKarma(focusDef(x.type), x.rating), 0) : 0;

  /* Matrix / decking (SR2 pp.162-179; Hacking Pool & Detection Factor VR2.0 p.18).
     Deck is bought via the Matrix panel; programs cost memory (the real limit) +
     editable nuyen (SR2 has no flat program price). */
  const PROGRAMS = window.SR2_PROGRAMS || [], PERSONA = window.SR2_PERSONA || [], MX = window.SR2_MATRIX || {};
  const decks = () => (window.GEAR || []).filter(g => g.cat === "deck" && (g.stats || []).some(s => s[0] === "MPCP"));
  const deckDef = () => (window.GEAR || []).find(g => g.cat === "deck" && g.n === state.deck) || null;
  function deckStat(key) { const d = deckDef(); if (!d) return 0; const s = (d.stats || []).find(x => x[0] === key); return s ? Number(s[1]) || 0 : 0; }
  const mpcp = () => deckStat("MPCP");
  const programDef = (name) => PROGRAMS.find(p => p.n === name) || null;
  function programSize(p) { const def = programDef(p.name); return def ? (Number(p.rating) || 0) ** 2 * def.mult : 0; }
  const programsMp = () => state.programs.reduce((t, p) => t + programSize(p), 0);
  const personaTotal = () => PERSONA.reduce((t, pp) => t + (Number(state.persona[pp.n.toLowerCase()]) || 0), 0);
  const personaCap = () => mpcp() * (MX.personaCapMult || 3);
  const hackingPool = () => state.deck ? Math.floor((finalAttr("intelligence") + mpcp()) / 3) : 0;
  const detectionFactor = () => {
    const mask = Number(state.persona.masking) || 0;
    const sleaze = (state.programs.find(p => p.name === "Sleaze") || {}).rating || 0;
    return Math.ceil((mask + sleaze) / 2);
  };
  const deckNuyen = () => { const d = deckDef(); return d && typeof d.cost === "number" ? d.cost : 0; };
  const programsNuyen = () => state.programs.reduce((t, p) => t + (Number(p.cost) || 0), 0);

  /* Contacts: Contact 5,000Y / Buddy 10,000Y (SR2 p.46 Cost of Extras). The "two
     free contacts" (p.46) become a flat credit of 2 x Contact cost off the total. */
  const contactCost = (c) => c.level === "Buddy" ? (CG.buddyCost || 10000) : (CG.contactCost || 5000);
  const contactsGross = () => state.contacts.reduce((t, c) => t + contactCost(c), 0);
  const contactsCredit = () => (CG.freeContacts || 0) * (CG.contactCost || 5000);
  const contactsNuyen = () => Math.max(0, contactsGross() - contactsCredit());

  const nuyenSpent = () => {
    let t = 0;
    ["weapons", "armor", "cyber", "vehicles", "other"].forEach(k => state.gear[k].forEach(g => t += (Number(g.cost) || 0)));
    return t + fociNuyen() + deckNuyen() + programsNuyen() + contactsNuyen();
  };
  /* Pull a sheet-relevant stat from a vehicle, handling both the SR2-core
     (Body/Armor/Pilot separate) and Rigger-2 (B/A combined, Apilot) formats. */
  function vehStat(v, key) {
    const find = (k) => { const s = (v.stats || []).find(x => String(x[0]).toLowerCase() === k.toLowerCase()); return s == null ? null : s[1]; };
    if (key === "body") { const b = find("Body"); if (b != null) return b; const ba = find("B/A"); return ba != null ? String(ba).split("/")[0] : ""; }
    if (key === "armor") { const a = find("Armor"); if (a != null) return a; const ba = find("B/A"); return ba != null ? (String(ba).split("/")[1] ?? "0") : ""; }
    if (key === "pilot") { const p = find("Pilot"); if (p != null) return p; const ap = find("Apilot"); if (ap != null) return ap; const an = find("Autonav"); return an != null ? an : ""; }
    const direct = find({ handling: "Handling", speed: "Speed", sig: "Sig" }[key] || key);
    return direct == null ? "" : direct;
  }
  const fpBudget = () => res().fp;
  const fpSpent = () => (state.magicType === "Full Mage" ? state.spells.reduce((t, s) => t + (Number(s.force) || 0), 0) : 0) + fociFp();
  const ppBudget = () => state.magicType === "Adept" ? magicRating() : 0;
  const ppSpent = () => state.powers.reduce((t, p) => t + powerPP(p), 0);

  /* Concentration / Specialization effective ratings (SR2 p.70).
     Concentration: general -1, the group +1.
     Specialization: general -2, the group at base, the specific +2.
     Narrowing is free -- point cost stays the base rating. */
  function skillTiers(s) {
    const base = Number(s.rating) || 0;
    const conc = (s.conc || "").trim();
    const spec = (s.spec || "").trim();
    const lo = (n) => Math.max(0, n);
    if (conc && spec) return [
      { label: s.name, rating: lo(base - 2) },
      { label: `${s.name} (${conc})`, rating: lo(base) },
      { label: `${s.name}: ${spec}`, rating: lo(base + 2) },
    ];
    if (conc) return [
      { label: s.name, rating: lo(base - 1) },
      { label: `${s.name} (${conc})`, rating: lo(base + 1) },
    ];
    return [{ label: s.name, rating: lo(base) }];
  }
  function tierReadoutHTML(s) {
    const tiers = skillTiers(s);
    if (tiers.length === 1) return "";
    return tiers.map(t => `${esc(t.label)} <strong>${t.rating}</strong>`).join(" - ");
  }
  function updateTierReadout(i) {
    const el = document.getElementById("cb-tiers-" + i);
    if (el) el.innerHTML = tierReadoutHTML(state.skills[i]);
  }
  const CHARGEN_SKILL_MAX = 6; // SR2 p.45: no starting skill > 6 (before narrowing)
  /* Specialization suggestions: the specific items a skill can narrow to.
     Combat skills -> the matching weapon catalogue; Sorcery -> spells. */
  const SKILL_WEAPON_CAT = {
    "Firearms": "firearm", "Gunnery": "heavy", "Projectile Weapons": "projectile",
    "Armed Combat": "melee", "Throwing Weapons": "melee", "Demolitions": "explosive",
  };
  function specSuggestions(s) {
    if (s.name === "Sorcery") return (window.SR2_SPELLS || []).map(x => x.n);
    const cat = SKILL_WEAPON_CAT[s.name];
    if (cat) {
      const seen = new Set();
      return (window.WEAPONS || []).filter(w => w.cat === cat && w.n && !seen.has(w.n) && seen.add(w.n)).map(w => w.n);
    }
    return [];
  }

  /* priorities validity */
  function prioLettersUsed() { return Object.values(state.prio).filter(Boolean); }
  function prioDup() {
    const used = prioLettersUsed(); const seen = {}; let dup = false;
    used.forEach(l => { if (seen[l]) dup = true; seen[l] = 1; });
    return dup;
  }
  const prioComplete = () => prioLettersUsed().length === 5 && !prioDup();

  /* magic availability from priorities */
  function magicOptions() {
    const opts = ["Mundane"];
    const r = MR.rank[state.prio.magic]; if (!r) return opts;
    const meta = isMeta();
    const adeptT = MR.rank[meta ? MR.adept.metahuman : MR.adept.human];
    const fullT = MR.rank[meta ? MR.fullMage.metahuman : MR.fullMage.human];
    if (r <= adeptT) opts.push("Adept");
    if (r <= fullT) opts.push("Full Mage");
    return opts;
  }

  /* ---------- rendering ---------- */
  const stepEl = () => document.getElementById("cb-step");
  function render() {
    renderRail();
    renderStepBody();
    renderBudget();
    const prev = document.getElementById("cb-prev"), next = document.getElementById("cb-next");
    if (prev) prev.disabled = state.step === 0;
    if (next) next.disabled = state.step === STEPS.length - 1;
  }
  function renderRail() {
    const rail = document.getElementById("cb-rail");
    rail.innerHTML = STEPS.map((s, i) =>
      `<li class="cb-rail__item ${i === state.step ? "is-active" : ""} ${i < state.step ? "is-done" : ""}" data-step="${i}">
         <em>${String(i + 1).padStart(2, "0")}</em><span>${esc(s)}</span></li>`).join("");
  }

  function renderStepBody() {
    const fns = [stepPriorities, stepMetatype, stepAttributes, stepMagic, stepSkills, stepResources, stepFinish];
    stepEl().innerHTML = fns[state.step]();
    wireStep();
  }

  /* ===== STEP 0 -- PRIORITIES ===== */
  function stepPriorities() {
    const cats = [
      ["race", "Race / Metatype"], ["magic", "Magic"], ["attributes", "Attributes"],
      ["skills", "Skills"], ["resources", "Resources"],
    ];
    const cell = (cat, L) => {
      let v;
      if (cat === "attributes") v = PR.attributes[L] + " pts";
      else if (cat === "skills") v = PR.skills[L] + " pts";
      else if (cat === "resources") v = money(PR.resources[L].nuyen) + " - " + PR.resources[L].fp + " FP";
      else v = PR[cat][L];
      const chosen = state.prio[cat] === L;
      const taken = !chosen && prioLettersUsed().includes(L);
      return `<button type="button" class="cb-prio ${chosen ? "is-chosen" : ""} ${taken ? "is-taken" : ""}" data-cat="${cat}" data-letter="${L}">
        <span class="cb-prio__l">${L}</span><span class="cb-prio__v">${esc(v)}</span></button>`;
    };
    const kits = window.SR2_ARCHETYPES || {};
    const kitRow = `<div class="cb-kits">
      <span class="cb-kits__label">Quick start --</span>
      ${Object.entries(kits).map(([k, a]) => `<button type="button" class="cb-kit" data-kit="${k}" title="${esc(a.blurb)}">${esc(a.name)}</button>`).join("")}
      <span class="cb-kits__hint">load a kit, then tweak anything</span></div>`;
    return `
      <h3 class="cb-h">Step 1 - Assign Priorities ${HELP("priorities.html", "priority system")}</h3>
      <p class="cb-p">New to chargen? Load a <strong>starter kit</strong> below -- it fills in priorities, attributes, skills and gear you can then edit. Or assign each row a letter <strong>A-E</strong> yourself, using each letter once. <span class="cb-cite">(SR2 p.45)</span></p>
      ${kitRow}
      <div class="cb-priogrid">
        ${cats.map(([cat, label]) => `
          <div class="cb-priorow">
            <div class="cb-priorow__label">${esc(label)}</div>
            <div class="cb-priorow__cells">${LETTERS.map(L => cell(cat, L)).join("")}</div>
          </div>`).join("")}
      </div>
      <p class="cb-note">${prioComplete() ? "OK Priorities complete." : (prioDup() ? "WARNING Each letter must be used once -- you have duplicates." : "Assign all five rows.")}</p>`;
  }

  /* ===== STEP 1 -- METATYPE ===== */
  function stepMetatype() {
    const meta = isMeta();
    const list = meta ? ["Elf", "Dwarf", "Ork", "Troll", "Human"] : ["Human"];
    const card = (mt) => {
      const m = META[mt]; const mods = Object.entries(m.mods || {}).map(([k, v]) => `${v > 0 ? "+" : ""}${v} ${ALABEL[k]}`).join(", ") || "no modifiers";
      return `<button type="button" class="cb-meta ${state.metatype === mt ? "is-chosen" : ""}" data-mt="${mt}">
        <span class="cb-meta__name">${mt}</span>
        <span class="cb-meta__mods">${esc(mods)}</span>
        <span class="cb-meta__vis">Vision: ${esc(m.vision)}${m.notes && m.notes.length ? " - " + esc(m.notes.join("; ")) : ""}</span></button>`;
    };
    return `
      <h3 class="cb-h">Step 2 - Metatype</h3>
      <p class="cb-p">${meta ? "Race priority A unlocks metahumans." : "Race priority B-E means you're <strong>Human</strong>. Set Race = A on the Priorities step to play a metahuman."} <span class="cb-cite">(SR2 p.43, 45)</span></p>
      <div class="cb-metagrid">${list.map(card).join("")}</div>`;
  }

  /* ===== STEP 2 -- ATTRIBUTES ===== */
  function stepAttributes() {
    const m = metatype();
    const row = (a) => {
      const mod = (m.mods || {})[a] || 0, max = (m.max || {})[a] || 6;
      return `<div class="cb-attr">
        <label>${ALABEL[a]}</label>
        <div class="cb-stepper">
          <button type="button" class="cb-step-btn" data-attr="${a}" data-d="-1">-</button>
          <span class="cb-attr__base">${state.base[a]}</span>
          <button type="button" class="cb-step-btn" data-attr="${a}" data-d="1">+</button>
        </div>
        <span class="cb-attr__mod">${mod ? (mod > 0 ? "+" + mod : mod) : "--"}</span>
        <span class="cb-attr__final ${finalAttr(a) > max ? "is-over" : ""}">= ${finalAttr(a)}</span>
        <span class="cb-attr__max">max ${max}</span>
      </div>`;
    };
    const over = attrSpent() > attrBudget();
    return `
      <h3 class="cb-h">Step 3 - Attributes</h3>
      <p class="cb-p">Spend <strong>${attrBudget()}</strong> points (priority ${state.prio.attributes || "--"}). Racial modifiers apply on top for free; final can't exceed the racial max. <span class="cb-cite">(SR2 p.45)</span></p>
      <div class="cb-attrhead"><span>Attribute</span><span>Points</span><span>Racial</span><span>Final</span><span></span></div>
      ${ATTRS.map(row).join("")}
      <p class="cb-note ${over ? "is-warn" : ""}">${attrSpent()} / ${attrBudget()} points spent${over ? " -- over budget!" : ""}</p>
      <div class="cb-derived">
        <span>Reaction <strong>${reaction()}</strong></span>
        <span>Initiative <strong>${reaction()} + ${initDice()}D6</strong></span>
        <span>Combat Pool <strong>${combatPool()}</strong></span>
      </div>`;
  }

  /* ===== STEP 3 -- MAGIC ===== */
  /* Tradition (Hermetic / Shamanic) + mandatory totem for shamans. SR2 p.120. */
  function tradTotemHTML() {
    const trads = ["Hermetic", "Shamanic"];
    let html = `<div class="cb-magicsub">
      <div class="cb-magicsub__h">Tradition ${HELP("magic.html", "traditions & totems")}</div>
      <div class="cb-magictype">${trads.map(t =>
        `<button type="button" class="cb-pill ${state.tradition === t ? "is-chosen" : ""}" data-tradition="${t}">${t}</button>`).join("")}</div>`;
    if (!state.tradition) {
      html += `<p class="cb-help-line">Pick a tradition -- both buy from the same spell list, but a <strong>shaman must choose a totem</strong>. <span class="cb-cite">(SR2 p.47, 120)</span></p>`;
    } else if (state.tradition === "Hermetic") {
      html += `<p class="cb-help-line">Hermetic mages summon elementals from a Hermetic Circle and learn spells from a Hermetic Library -- <strong>no totem</strong>, no bonuses or geasa. (Workspace/library are nuyen gear, bought in Resources.) <span class="cb-cite">(SR2 p.263)</span></p>`;
    } else {
      const totems = window.SR2_TOTEMS || [];
      const sel = totems.find(t => t.n === state.totem);
      html += `<div class="cb-magicsub__h" style="margin-top:.6rem">Totem <span class="cb-req ${state.totem ? "is-ok" : "is-missing"}">${state.totem ? "OK " + esc(state.totem) : "required"}</span></div>
        <div class="cb-totemgrid">${totems.map(t =>
          `<button type="button" class="cb-totem ${state.totem === t.n ? "is-chosen" : ""}" data-totem="${esc(t.n)}">
             <span class="cb-totem__n">${esc(t.n)}</span><span class="cb-totem__env">${esc(t.env)}</span></button>`).join("")}</div>`;
      if (sel) {
        const perks = [
          sel.spells && `<li class="cb-perk cb-perk--good">${esc(sel.spells)}</li>`,
          sel.spirits && `<li class="cb-perk cb-perk--good">${esc(sel.spirits)}</li>`,
          sel.penalty && `<li class="cb-perk cb-perk--bad">${esc(sel.penalty)}</li>`,
        ].filter(Boolean).join("");
        html += `<div class="cb-totemcard">
          <div class="cb-totemcard__h">${esc(sel.n)} <em>${esc(sel.env)}</em></div>
          <ul class="cb-totemcard__perks">${perks || `<li class="cb-perk">No spell or conjuring modifiers.</li>`}</ul>
          <p class="cb-totemcard__geas"><strong>Geas:</strong> ${esc(sel.geas)}</p>
          <p class="cb-cite">SR2 pp.120-122</p></div>`;
      }
    }
    return html + `</div>`;
  }

  /* Foci shop -- costs nuyen AND Force Points (bonding Karma). SR2 p.137 / p.263. */
  function fociSectionHTML() {
    const all = window.SR2_FOCI || [];
    const allow = state.magicType === "Adept" ? all.filter(f => f.who === "both") : all;
    const chosen = state.foci.map((x, i) => {
      const f = focusDef(x.type); if (!f) return "";
      const ny = focusNuyen(f, x.rating), fp = focusKarma(f, x.rating);
      const rateCtrl = f.rated
        ? `<span class="cb-stepper cb-stepper--sm"><button type="button" class="cb-step-btn" data-focusrate="${i}" data-d="-1">-</button><span class="cb-attr__base">${x.rating}</span><button type="button" class="cb-step-btn" data-focusrate="${i}" data-d="1">+</button></span>`
        : `<span class="cb-line__f">Rating 1</span>`;
      const applies = f.applies
        ? `<div class="cb-focusline__applies"><label class="cb-focus"><span>Applies to</span><input type="text" class="cb-focus__in" data-focusapplies="${i}" value="${esc(x.applies || "")}" placeholder="${esc(f.applies)}"></label></div>`
        : "";
      return `<div class="cb-focusline">
        <div class="cb-line"><span class="cb-line__n">${esc(f.n)}</span>${rateCtrl}
          <span class="cb-line__f">${fp} FP</span><span class="cb-line__f">${money(ny)}</span>
          <button type="button" class="cb-x" data-delfocus="${i}">?</button></div>${applies}</div>`;
    }).join("");
    const shop = allow.map(f => {
      const idx = all.indexOf(f);
      const ny = focusNuyen(f, 1), fp = focusKarma(f, 1);
      const det = detailHTML(f.fx, null, `${f.applies ? "Applies to: " + f.applies + " - " : ""}Rating 1 = ${money(ny)} + ${fp} FP${f.rated ? " - scales with Rating" : ""}`);
      return shopRow(f.n, money(ny) + " + " + fp + " FP", det, `data-addfocus="${idx}"`);
    }).join("");
    return `<div class="cb-magicsub">
      <div class="cb-magicsub__h">Foci <span class="cb-dim">-- optional</span> ${HELP("magic-mechanics.html", "foci & bonding")}</div>
      <p class="cb-help-line">Each focus costs <strong>nuyen</strong> (from your Resources budget) <em>and</em> <strong>Force Points</strong> equal to its bonding Karma.${state.magicType === "Adept" ? " Adepts may bond only Weapon Foci." : ""} <span class="cb-cite">(SR2 p.137, p.263)</span></p>
      <div class="cb-chosen">${state.foci.length ? chosen : `<p class="cb-empty">No foci.</p>`}</div>
      <div class="cb-shop"><div class="cb-shoplist">${shop}</div></div></div>`;
  }

  function stepMagic() {
    const opts = magicOptions();
    const chooser = `<div class="cb-magictype">${opts.map(o =>
      `<button type="button" class="cb-pill ${state.magicType === o ? "is-chosen" : ""}" data-magictype="${o}">${o}</button>`).join("")}</div>`;
    if (state.magicType === "Mundane") {
      return `<h3 class="cb-h">Step 4 - Magic</h3>
        <p class="cb-p">Your priorities allow: <strong>${opts.join(" - ")}</strong>. Mundane characters skip this step. <span class="cb-cite">(SR2 p.45)</span></p>${chooser}`;
    }
    if (state.magicType === "Full Mage") {
      const spells = window.SR2_SPELLS || [];
      const q = (document.getElementById("cb-spell-search") || {}).value || "";
      const filt = spells.filter(s => !q || (s.n + " " + (s.cat || "")).toLowerCase().includes(q.toLowerCase())).slice(0, 40);
      return `<h3 class="cb-h">Step 4 - Magic -- Full Magician ${HELP("spells.html", "spell index")} ${HELP("magic-mechanics.html", "drain & casting")}</h3>
        <p class="cb-p">Magic Rating <strong>${magicRating()}</strong>. Buy spells with Force Points (each spell costs FP = its Force; max Force 6 at chargen). <span class="cb-cite">(SR2 p.46)</span></p>
        ${chooser}
        ${tradTotemHTML()}
        <div class="cb-magicsub__h">Spells</div>
        <div class="cb-chosen">${state.spells.length ? state.spells.map((s, i) =>
          `<div class="cb-line"><span class="cb-line__n">${esc(s.name)} <em>${esc(s.type || "")}</em></span>
             <span class="cb-line__f">Force <input type="number" min="1" max="6" value="${s.force}" data-spellforce="${i}" class="cb-mini"></span>
             <span class="cb-line__d">${esc(s.drain || "")}</span>
             <button type="button" class="cb-x" data-delspell="${i}">?</button></div>`).join("") : `<p class="cb-empty">No spells yet.</p>`}</div>
        <div class="cb-shop">
          <input type="search" id="cb-spell-search" class="cb-search" placeholder="Search spells..." value="${esc(q)}">
          <div class="cb-shoplist">${filt.map(s => {
            const idx = spells.indexOf(s);
            const det = detailHTML(s.desc, s.effect, `${s.cat || ""} - ${s.typ === "M" ? "Mana" : s.typ === "P" ? "Physical" : ""} - Drain ${s.drn || "--"} - Rng ${s.rng || "--"} - Dur ${s.dur || "--"}`);
            return shopRow(s.n, (s.cat || "") + " - " + (s.drn || ""), det, `data-addspell="${idx}"`);
          }).join("")}</div>
        </div>
        ${fociSectionHTML()}`;
    }
    // Adept
    const powers = window.ADEPT_POWERS || [];
    const q = (document.getElementById("cb-power-search") || {}).value || "";
    const filt = powers.filter(p => !q || p.n.toLowerCase().includes(q.toLowerCase())).slice(0, 40);
    return `<h3 class="cb-h">Step 4 - Magic -- Physical Adept ${HELP("adepts.html", "adept powers")}</h3>
      <p class="cb-p">Magic Rating <strong>${magicRating()}</strong> = <strong>${ppBudget()}</strong> Power Points to spend on adept powers. <span class="cb-cite">(SR2 p.169)</span></p>
      ${chooser}
      <div class="cb-magicsub__h">Adept Powers</div>
      <div class="cb-chosen">${state.powers.length ? state.powers.map((p, i) => {
        const it = powerDef(p.name);
        if (it && it.rated) {
          const lvl = clampNum(p.lvl || 1, 1, it.maxLevel);
          const attrSel = it.attrChoice ? `<select class="cb-mini" data-powerattr="${i}">${["body", "quickness", "strength"].map(a => `<option value="${a}" ${(p.attr || "body") === a ? "selected" : ""}>${ALABEL[a].slice(0, 3)}</option>`).join("")}</select>` : "";
          return `<div class="cb-line"><span class="cb-line__n">${esc(p.name)}</span>
            ${attrSel}
            <span class="cb-stepper cb-stepper--sm"><button type="button" class="cb-step-btn" data-powerlvl="${i}" data-d="-1">-</button><span class="cb-attr__base">${lvl}</span><button type="button" class="cb-step-btn" data-powerlvl="${i}" data-d="1">+</button></span>
            <span class="cb-line__f">${powerPP(p)} PP</span>
            <button type="button" class="cb-x" data-delpower="${i}">?</button></div>`;
        }
        return `<div class="cb-line"><span class="cb-line__n">${esc(p.name)}</span><span class="cb-line__f">${esc(p.pp)} PP</span><button type="button" class="cb-x" data-delpower="${i}">?</button></div>`;
      }).join("") : `<p class="cb-empty">No powers yet.</p>`}</div>
      <div class="cb-shop">
        <input type="search" id="cb-power-search" class="cb-search" placeholder="Search adept powers..." value="${esc(q)}">
        <div class="cb-shoplist">${filt.map(p => {
          const idx = powers.indexOf(p);
          const det = detailHTML(p.desc, p.effect, `Cost ${esc(p.pp)} - activation ${esc(p.act || "--")}`);
          return shopRow(p.n, p.pp, det, `data-addpower="${idx}"`);
        }).join("")}</div>
      </div>
      ${fociSectionHTML()}`;
  }

  /* ===== STEP 4 -- SKILLS ===== */
  function chosenSkillHTML(s, i) {
    const def = SKILLS.find(x => x.n === s.name) || {};
    const concList = def.conc || [];
    const concDlId = "cb-conc-dl-" + i, specDlId = "cb-spec-dl-" + i;
    const conc = s.conc || "", spec = s.spec || "";
    const specs = specSuggestions(s);
    const concDatalist = concList.length
      ? `<datalist id="${concDlId}">${concList.map(c => `<option value="${esc(c)}"></option>`).join("")}</datalist>`
      : "";
    const specDatalist = specs.length
      ? `<datalist id="${specDlId}">${specs.map(x => `<option value="${esc(x)}"></option>`).join("")}</datalist>`
      : "";
    const specPlaceholder = conc ? (specs.length ? "type or pick a specific" : "specific form") : "set a Concentration first";
    return `<div class="cb-skill">
      <div class="cb-line">
        <span class="cb-line__n ${s.group === "knowledge" ? "is-kn" : ""}">${esc(s.name)} <em>(${esc(s.attr)})</em></span>
        <span class="cb-stepper cb-stepper--sm">
          <button type="button" class="cb-step-btn" data-skill="${i}" data-d="-1">-</button>
          <span class="cb-attr__base ${s.rating >= CHARGEN_SKILL_MAX ? "is-max" : ""}">${s.rating}</span>
          <button type="button" class="cb-step-btn" data-skill="${i}" data-d="1">+</button>
        </span>
        <button type="button" class="cb-x" data-delskill="${i}">?</button>
      </div>
      <div class="cb-skill__focus">
        <label class="cb-focus"><span>Concentration</span>
          <input type="text" class="cb-focus__in" data-conc="${i}" value="${esc(conc)}" list="${concDlId}" placeholder="${concList.length ? esc(concList[0]) : "group"}">
        </label>
        <label class="cb-focus"><span>Specialization</span>
          <input type="text" class="cb-focus__in" data-spec="${i}" value="${esc(spec)}"${specs.length ? ` list="${specDlId}"` : ""} placeholder="${esc(specPlaceholder)}"${conc ? "" : " disabled title=\"Set a Concentration first -- a Specialization narrows a Concentration\""}>
        </label>
        ${concDatalist}${specDatalist}
        <span class="cb-tiers" id="cb-tiers-${i}">${tierReadoutHTML(s)}</span>
      </div>
    </div>`;
  }
  /* Languages (SR2 p.45, p.74): native free at Int+2; Street lifestyle adds a free
     local dialect at 1/2 Int; any other language is a knowledge skill from the pool. */
  function languagesSectionHTML() {
    const intel = finalAttr("intelligence");
    const nativeR = intel + 2;
    const street = state.identity.lifestyle === "Street";
    const dialectR = Math.floor(intel / 2);
    const dl = `<datalist id="cb-lang-dl">${(window.SR2_LANGUAGES || []).map(x => `<option value="${esc(x)}"></option>`).join("")}</datalist>`;
    const rows = state.languages.map((l, i) => `<div class="cb-line">
        <input type="text" class="cb-focus__in" data-langname="${i}" value="${esc(l.name)}" list="cb-lang-dl" placeholder="language">
        <span class="cb-stepper cb-stepper--sm">
          <button type="button" class="cb-step-btn" data-langrate="${i}" data-d="-1">-</button>
          <span class="cb-attr__base ${l.rating >= CHARGEN_SKILL_MAX ? "is-max" : ""}">${l.rating}</span>
          <button type="button" class="cb-step-btn" data-langrate="${i}" data-d="1">+</button>
        </span>
        <button type="button" class="cb-x" data-dellang="${i}">?</button>
      </div>`).join("");
    return `<div class="cb-langs">
      <div class="cb-magicsub__h" style="margin-top:1.1rem">Languages ${HELP("skills.html", "language skills")}</div>
      <p class="cb-help-line">Your <strong>native language</strong> is free at <strong>Intelligence + 2</strong> (read &amp; write included).${street ? " A Street lifestyle adds a free local dialect at 1/2 Intelligence." : ""} Any other language is a knowledge skill bought from the same skill pool above. <span class="cb-cite">(SR2 p.45, p.74)</span></p>
      <div class="cb-line">
        <span class="cb-line__n is-kn">Native language <em>(free)</em></span>
        <input type="text" class="cb-focus__in" data-nativelang value="${esc(state.nativeLanguage)}" list="cb-lang-dl" placeholder="e.g. English / Sperethiel">
        <span class="cb-line__f">Rating <strong>${nativeR}</strong></span>
      </div>
      ${street ? `<div class="cb-line">
        <span class="cb-line__n is-kn">Street dialect <em>(free)</em></span>
        <input type="text" class="cb-focus__in" data-dialect value="${esc(state.streetDialect)}" list="cb-lang-dl" placeholder="e.g. City Speak / Tunnel Talk">
        <span class="cb-line__f">Rating <strong>${dialectR}</strong></span>
      </div>` : ""}
      ${rows}
      <div class="cb-shop"><button type="button" class="cb-btn cb-btn--ghost" data-addlang>+ Add language</button></div>
      ${dl}
    </div>`;
  }

  function stepSkills() {
    const over = skillSpent() > skillBudget();
    const q = (document.getElementById("cb-skill-search") || {}).value || "";
    const avail = SKILLS.filter(s => !q || s.n.toLowerCase().includes(q.toLowerCase()));
    return `<h3 class="cb-h">Step 5 - Skills ${HELP("skills.html", "skills index")}</h3>
      <p class="cb-p">Spend <strong>${skillBudget()}</strong> skill points (priority ${state.prio.skills || "--"}); a skill at rating N costs N points. No starting skill may exceed <strong>6</strong> (the stepper caps there); only narrowing can push a rating higher. In SR2 every skill -- knowledge skills (italic) included -- comes from this same pool; only your native language is free (Intelligence + 2). <span class="cb-cite">(SR2 p.45)</span></p>
      <p class="cb-p">Optional narrowing (free -- cost stays the base rating): a <strong>Concentration</strong> picks a broad group (general -1 / that group +1). A <strong>Specialization</strong> narrows that group to one specific item (general -2 / group at base / the specific +2) -- so set the Concentration first, then the specific, e.g. <em>Firearms -> Pistols -> Ares Predator</em>. <span class="cb-cite">(SR2 p.70)</span></p>
      <div class="cb-chosen">${state.skills.length ? state.skills.map(chosenSkillHTML).join("") : `<p class="cb-empty">No skills yet.</p>`}</div>
      <p class="cb-note ${over ? "is-warn" : ""}">${skillSpent()} / ${skillBudget()} skill points${over ? " -- over budget!" : ""}${languagesSpent() ? ` (incl. ${languagesSpent()} on languages)` : ""}</p>
      ${languagesSectionHTML()}
      <div class="cb-shop">
        <input type="search" id="cb-skill-search" class="cb-search" placeholder="Search skills..." value="${esc(q)}">
        <div class="cb-shoplist">${avail.slice(0, 60).map(s => {
          const taken = state.skills.some(x => x.name === s.n);
          const det = `<p class="cb-det__stat">Linked to <strong>${esc(s.attr)}</strong> - ${esc(s.group)}</p><p class="cb-det__desc">${HELP("skills.html", "what this skill covers")}</p>`;
          return shopRow(s.n + (s.group === "knowledge" ? " (kn)" : ""), s.attr, det, `data-addskill="${esc(s.n)}"`, taken);
        }).join("")}</div>
      </div>`;
  }

  /* ===== STEP 5 -- RESOURCES (shopping) ===== */
  const SHOP_TABS = [
    { k: "weapons", label: "Weapons", data: () => window.WEAPONS || [] },
    { k: "armor", label: "Armor", data: () => window.ARMOR || [] },
    { k: "cyber", label: "Cyberware", data: () => window.CYBERWARE || [] },
    { k: "vehicles", label: "Vehicles", data: () => (window.GEAR || []).filter(g => g.cat === "vehicle" || g.cat === "drone") },
    { k: "other", label: "Gear", data: () => window.GEAR || [] },
  ];
  let shopTab = "weapons";

  /* Matrix / decking panel (lives inside the Resources step). */
  function matrixSectionHTML() {
    const dks = decks();
    const deckOptions = `<option value="">-- no deck --</option>` + dks.map(x => {
      const m = (x.stats.find(s => s[0] === "MPCP") || [])[1];
      return `<option value="${esc(x.n)}" ${state.deck === x.n ? "selected" : ""}>${esc(x.n)} - MPCP ${m} - ${money(x.cost)}</option>`;
    }).join("");
    let html = `<div class="cb-matrix">
      <div class="cb-magicsub__h">Matrix / Decking <span class="cb-dim">-- optional</span> ${HELP("matrix-mechanics.html", "how decking works")}</div>
      <p class="cb-help-line">Pick a cyberdeck (its price comes out of your nuyen budget), set persona programs, and load utilities. You also need a <strong>Datajack</strong> (Cyberware tab) to jack in. <span class="cb-cite">(SR2 p.172-178)</span></p>
      <label class="cb-deckpick"><span>Cyberdeck</span> <select data-deck>${deckOptions}</select></label>`;
    if (!state.deck) return html + `</div>`;
    html += `<div class="cb-deckstats">
      <span>MPCP <strong>${deckStat("MPCP")}</strong></span>
      <span>Hardening <strong>${deckStat("Hardening")}</strong></span>
      <span>Active <strong>${deckStat("Active Mem")}</strong> Mp</span>
      <span>Storage <strong>${deckStat("Storage")}</strong> Mp</span>
      <span>Load <strong>${deckStat("Load")}</strong></span>
      <span>I/O <strong>${deckStat("I/O")}</strong></span>
      <span>${money(deckNuyen())}</span>
    </div>`;
    const cap = personaCap(), tot = personaTotal(), pOver = tot > cap;
    html += `<div class="cb-magicsub__h" style="margin-top:.7rem">Persona Programs <span class="cb-req ${pOver ? "is-missing" : "is-ok"}">${tot} / ${cap} <span class="cb-dim">(3xMPCP)</span></span></div>
      <div class="cb-persona">${PERSONA.map(pp => {
        const key = pp.n.toLowerCase(); const v = Number(state.persona[key]) || 0;
        return `<div class="cb-personarow" title="${esc(pp.desc)}">
          <span class="cb-personarow__n">${esc(pp.n)}</span>
          <span class="cb-stepper cb-stepper--sm">
            <button type="button" class="cb-step-btn" data-persona="${key}" data-d="-1">-</button>
            <span class="cb-attr__base">${v}</span>
            <button type="button" class="cb-step-btn" data-persona="${key}" data-d="1">+</button>
          </span></div>`;
      }).join("")}</div>`;
    const memOver = programsMp() > deckStat("Storage");
    const chosen = state.programs.map((p, i) => {
      const def = programDef(p.name); const sz = programSize(p);
      return `<div class="cb-line"><span class="cb-line__n">${esc(p.name)} <em>${esc(def ? def.type : "")}</em></span>
        <span class="cb-stepper cb-stepper--sm"><button type="button" class="cb-step-btn" data-prograte="${i}" data-d="-1">-</button><span class="cb-attr__base">${p.rating}</span><button type="button" class="cb-step-btn" data-prograte="${i}" data-d="1">+</button></span>
        <span class="cb-line__f">${sz} Mp</span>
        <span class="cb-line__f">Y <input type="number" value="${Number(p.cost) || 0}" data-progcost="${i}" class="cb-mini cb-mini--w"></span>
        <button type="button" class="cb-x" data-delprog="${i}">?</button></div>`;
    }).join("");
    const owned = state.programs.map(p => p.name);
    const shop = PROGRAMS.map((p, idx) => {
      const det = detailHTML(p.fx, null, `${p.type} - size = Rating2 x ${p.mult} Mp`);
      return shopRow(p.n, p.type, det, `data-addprog="${idx}"`, owned.includes(p.n));
    }).join("");
    html += `<div class="cb-magicsub__h" style="margin-top:.7rem">Utility Programs <span class="cb-req ${memOver ? "is-missing" : "is-ok"}">${programsMp()} / ${deckStat("Storage")} Mp storage</span></div>
      <p class="cb-help-line">Each utility's memory = Rating2 x its multiplier. Programs sit in Storage; Active Memory (${deckStat("Active Mem")} Mp) caps how many run at once. SR2 sets no fixed program price -- they're written or bought as object code, so nuyen is yours to fill in. <span class="cb-cite">(SR2 p.174-177)</span></p>
      <div class="cb-chosen">${state.programs.length ? chosen : `<p class="cb-empty">No programs.</p>`}</div>
      <div class="cb-shop"><div class="cb-shoplist">${shop}</div></div>
      <div class="cb-deckderived">
        <span>Hacking Pool <strong>${hackingPool()}</strong> <em>(Int+MPCP)/3</em></span>
        <span>Detection Factor <strong>${detectionFactor()}</strong> <em>(Masking+Sleaze)/2</em></span>
      </div>`;
    return html + `</div>`;
  }

  /* Contacts panel (Cost of Extras, SR2 p.46): 2 free, then Contact 5k / Buddy 10k.
     Lives in Resources because it draws on the nuyen budget. */
  function contactsSectionHTML() {
    const dl = `<datalist id="cb-arch-dl">${(window.SR2_CONTACT_ARCHETYPES || []).map(x => `<option value="${esc(x)}"></option>`).join("")}</datalist>`;
    const rows = state.contacts.map((c, i) => `<div class="cb-line">
        <input type="text" class="cb-focus__in" data-cname="${i}" value="${esc(c.name)}" placeholder="name / handle">
        <input type="text" class="cb-focus__in" data-carch="${i}" value="${esc(c.archetype)}" list="cb-arch-dl" placeholder="archetype (Fixer, Street Doc...)">
        <button type="button" class="cb-tab ${c.level === "Buddy" ? "is-active" : ""}" data-clevel="${i}" title="Toggle Contact / Buddy">${esc(c.level)}</button>
        <span class="cb-line__f">${money(contactCost(c))}</span>
        <button type="button" class="cb-x" data-delcontact="${i}">?</button>
      </div>`).join("");
    const free = state.contacts.length <= (CG.freeContacts || 0);
    return `<div class="cb-contacts">
      <div class="cb-magicsub__h" style="margin-top:1rem">Contacts <span class="cb-dim">-- Cost of Extras</span> ${HELP("glossary.html", "how contacts work")}</div>
      <p class="cb-help-line">You start with <strong>${CG.freeContacts || 2} free contacts</strong>; beyond that a <strong>Contact</strong> is ${money(CG.contactCost || 5000)} and a <strong>Buddy</strong> ${money(CG.buddyCost || 10000)} (a closer, more reliable friend). Use them via Etiquette (TN 4) for info, gear &amp; favours. <span class="cb-cite">(SR2 p.46, p.200)</span></p>
      <div class="cb-chosen">${state.contacts.length ? rows : `<p class="cb-empty">No contacts yet -- add your 2 free ones.</p>`}</div>
      <div class="cb-shop"><button type="button" class="cb-btn cb-btn--ghost" data-addcontact>+ Add contact</button></div>
      <p class="cb-note ${contactsNuyen() > res().nuyen ? "is-warn" : ""}">${money(contactsGross())} gross - ${money(contactsCredit())} free credit = <strong>${money(contactsNuyen())}</strong> from nuyen${free ? " - all free so far" : ""}</p>
      ${dl}
    </div>`;
  }

  function stepResources() {
    const over = nuyenSpent() > res().nuyen;
    const lines = (k) => state.gear[k].length ? state.gear[k].map((g, i) => {
      const sub = k === "armor" ? `B${g.ballistic ?? "--"}/I${g.impact ?? "--"}`
        : k === "vehicles" ? [vehStat(g, "handling") && ("Hand " + vehStat(g, "handling")), vehStat(g, "speed") && ("Spd " + vehStat(g, "speed")), `B/A ${vehStat(g, "body")}/${vehStat(g, "armor")}`].filter(Boolean).join(" - ")
        : (g.sub || g.cat || "");
      if (k === "cyber") {
        const def = cyberDef(g.n);
        if (def && def.rated) { // rated 'ware: pick a rating, Essence & cost derive from it
          const r = clampNum(g.rating || 1, 1, def.maxRating);
          return `<div class="cb-line"><span class="cb-line__n">${esc(g.n)} <em>R${r}/${def.maxRating}</em></span>
            <span class="cb-stepper cb-stepper--sm"><button type="button" class="cb-step-btn" data-cyberrate="${i}" data-d="-1">-</button><span class="cb-attr__base">${r}</span><button type="button" class="cb-step-btn" data-cyberrate="${i}" data-d="1">+</button></span>
            <span class="cb-line__f">Ess ${g.ess}</span>
            <span class="cb-line__f">${money(g.cost)}</span>
            <button type="button" class="cb-x" data-delgear="cyber:${i}">?</button></div>`;
        }
        return `<div class="cb-line"><span class="cb-line__n">${esc(g.n)} <em>${esc(sub)}</em></span>
          <span class="cb-line__f">Ess <input type="number" step="0.1" value="${g.ess ?? 0}" data-essedit="${i}" class="cb-mini"></span>
          <span class="cb-line__f">Y <input type="number" value="${Number(g.cost) || 0}" data-costedit="cyber:${i}" class="cb-mini cb-mini--w"></span>
          <button type="button" class="cb-x" data-delgear="cyber:${i}">?</button></div>`;
      }
      return `<div class="cb-line"><span class="cb-line__n">${esc(g.n)} <em>${esc(sub)}</em></span>
        <span class="cb-line__f">Y <input type="number" value="${Number(g.cost) || 0}" data-costedit="${k}:${i}" class="cb-mini cb-mini--w"></span>
        <button type="button" class="cb-x" data-delgear="${k}:${i}">?</button></div>`;
    }).join("") : "";
    const owned = ["weapons", "armor", "cyber", "vehicles", "other"].map(k => {
      if (!state.gear[k].length) return "";
      const label = SHOP_TABS.find(t => t.k === k).label;
      return `<div class="cb-owned"><div class="cb-owned__h">${label}</div>${lines(k)}</div>`;
    }).join("") || `<p class="cb-empty">Nothing bought yet.</p>`;

    const tab = SHOP_TABS.find(t => t.k === shopTab);
    const q = (document.getElementById("cb-gear-search") || {}).value || "";
    // Vehicles/drones get their own tab; decks & programs live in the Matrix panel.
    const items = tab.data().filter(it => !(shopTab === "other" && ["deck", "program", "vehicle", "drone"].includes(it.cat)))
      .filter(it => !q || (it.n + " " + (it.sub || it.cat || "")).toLowerCase().includes(q.toLowerCase())).slice(0, 50);
    return `<h3 class="cb-h">Step 6 - Resources</h3>
      <p class="cb-p">Budget <strong>${money(res().nuyen)}</strong> (priority ${state.prio.resources || "--"}). Click items to buy; prices are editable (handy for per-level / ranged costs). Cyberware also deducts Essence. At chargen, ignore Availability/Street Index. <span class="cb-cite">(SR2 p.46)</span></p>
      <div class="cb-resgrid">
        <div class="cb-owned-wrap"><h4 class="cb-h4">Your loadout</h4>${owned}</div>
        <div class="cb-shop">
          <div class="cb-tabs">${SHOP_TABS.map(t => `<button type="button" class="cb-tab ${shopTab === t.k ? "is-active" : ""}" data-shoptab="${t.k}">${t.label}</button>`).join("")}</div>
          <div class="cb-shop__top">
            <input type="search" id="cb-gear-search" class="cb-search" placeholder="Search ${tab.label.toLowerCase()}..." value="${esc(q)}">
            ${HELP({ weapons: "weapons.html", armor: "armor.html", cyber: "cyberware.html", vehicles: "gear.html", other: "gear.html" }[shopTab], "full catalogue")}
          </div>
          <div class="cb-shoplist">${items.map(it => {
            const idx = tab.data().indexOf(it);
            const meta = (shopTab === "armor" ? `B${it.ballistic ?? "--"}/I${it.impact ?? "--"}` : (it.sub || it.cat || "")) + " - " + (typeof it.cost === "number" ? money(it.cost) : (it.cost || "--"));
            return shopRow(it.n, meta, gearDetail(it, shopTab), `data-buy="${shopTab}:${idx}"`, false, shopArt(shopTab, it.n));
          }).join("")}</div>
        </div>
      </div>
      <p class="cb-note ${over ? "is-warn" : ""}">${money(nuyenSpent())} / ${money(res().nuyen)} spent${over ? " -- over budget!" : ""} - Essence ${essence().toFixed(2)} / 6</p>
      ${matrixSectionHTML()}
      ${contactsSectionHTML()}`;
  }

  /* ===== STEP 6 -- FINISH & EXPORT ===== */
  function stepFinish() {
    const id = state.identity;
    const fa = finalAttrs();
    return `<h3 class="cb-h">Step 7 - Finish &amp; Export</h3>
      <div class="cb-form">
        <label>Name <input type="text" data-id="name" value="${esc(id.name)}"></label>
        <label>Sex <input type="text" data-id="sex" value="${esc(id.sex)}"></label>
        <label>Age <input type="text" data-id="age" value="${esc(id.age)}"></label>
        <label class="cb-form__wide">Description <input type="text" data-id="desc" value="${esc(id.desc)}"></label>
        <label>Lifestyle
          <select data-id="lifestyle">${CG.lifestyles.map(l => `<option ${id.lifestyle === l.name ? "selected" : ""}>${l.name}</option>`).join("")}</select>
        </label>
      </div>
      <div class="cb-summary">
        <div><h4>${esc(id.name || "Unnamed")} -- ${esc(state.metatype)} ${esc(state.magicType !== "Mundane" ? state.magicType : "")}${state.magicType === "Full Mage" && state.tradition ? esc(" - " + state.tradition + (state.tradition === "Shamanic" && state.totem ? " (" + state.totem + ")" : "")) : ""}</h4></div>
        <div class="cb-summary__grid">
          ${ATTRS.map(a => `<span>${ALABEL[a].slice(0, 3)} <strong>${fa[a]}</strong></span>`).join("")}
          <span>REA <strong>${reaction()}</strong></span><span>INIT <strong>${reaction()}+${initDice()}D6</strong></span>
          <span>CP <strong>${combatPool()}</strong></span><span>ESS <strong>${essence().toFixed(2)}</strong></span>
          <span>MAG <strong>${magicRating()}</strong></span>
        </div>
        <p class="cb-summary__line">${state.skills.length} skills - ${state.languages.length + (state.nativeLanguage ? 1 : 0)} languages - ${state.contacts.length} contacts - ${state.spells.length} spells - ${state.powers.length} powers - ${state.foci.length} foci - ${state.gear.weapons.length} weapons - ${state.gear.armor.length} armor - ${state.gear.cyber.length} cyber${state.gear.vehicles.length ? ` - ${state.gear.vehicles.length} vehicles` : ""}${state.deck ? ` - deck: ${esc(state.deck)} (${state.programs.length} programs)` : ""}</p>
      </div>
      <button type="button" id="cb-export2" class="cb-btn cb-btn--primary cb-btn--big">? Export filled PDF</button>
      <p class="cb-export-status" id="cb-export-status"></p>`;
  }

  /* ---------- budget panel ---------- */
  function meter(label, spent, budget, unit) {
    const over = spent > budget;
    const pct = budget ? Math.min(100, (spent / budget) * 100) : 0;
    return `<div class="cb-meter ${over ? "is-over" : ""}">
      <div class="cb-meter__top"><span>${label}</span><span>${spent}${unit || ""} / ${budget}${unit || ""}</span></div>
      <div class="cb-meter__bar"><i style="width:${pct}%"></i></div></div>`;
  }
  function renderBudget() {
    const b = document.getElementById("cb-budget");
    let html = `<div class="cb-budget__h">// BUDGETS</div>`;
    html += `<div class="cb-meter ${prioComplete() ? "" : "is-over"}"><div class="cb-meter__top"><span>Priorities</span><span>${prioLettersUsed().length}/5${prioDup() ? " WARNINGdup" : ""}</span></div></div>`;
    html += meter("Attributes", attrSpent(), attrBudget(), "");
    html += meter("Skills", skillSpent(), skillBudget(), "");
    html += `<div class="cb-meter ${nuyenSpent() > res().nuyen ? "is-over" : ""}"><div class="cb-meter__top"><span>Nuyen</span><span>${money(nuyenSpent())} / ${money(res().nuyen)}</span></div><div class="cb-meter__bar"><i style="width:${res().nuyen ? Math.min(100, nuyenSpent() / res().nuyen * 100) : 0}%"></i></div></div>`;
    if (awakened()) html += meter("Force Pts", fpSpent(), fpBudget(), "");
    if (state.magicType === "Adept") html += meter("Power Pts", ppSpent(), ppBudget(), "");
    html += `<div class="cb-budget__h" style="margin-top:.8rem">// DERIVED</div>
      <div class="cb-budget__stat"><span>Essence</span><strong>${essence().toFixed(2)}</strong></div>
      <div class="cb-budget__stat"><span>Magic</span><strong>${magicRating()}</strong></div>
      <div class="cb-budget__stat"><span>Reaction</span><strong>${reaction()}</strong></div>
      <div class="cb-budget__stat"><span>Initiative</span><strong>${reaction()}+${initDice()}D6</strong></div>
      <div class="cb-budget__stat"><span>Combat Pool</span><strong>${combatPool()}</strong></div>`;
    if (state.deck) html += `<div class="cb-budget__stat"><span>Hacking Pool</span><strong>${hackingPool()}</strong></div>`;
    const am = augMods();
    const augBits = [am.reaction ? `+${am.reaction} REA` : "", am.initDice ? `+${am.initDice} init ${am.initDice > 1 ? "dice" : "die"}` : "",
      ...ATTRS.filter(a => am[a]).map(a => `${am[a] > 0 ? "+" : ""}${am[a]} ${ALABEL[a].slice(0, 3)}`)].filter(Boolean);
    if (augBits.length) html += `<div class="cb-budget__note">cyber/bioware: ${augBits.join(", ")}</div>`;
    b.innerHTML = html;
  }

  /* ---------- event wiring ---------- */
  function wireStep() {
    const c = stepEl();
    // priorities
    c.querySelectorAll("[data-cat][data-letter]").forEach(btn => btn.onclick = () => {
      const cat = btn.dataset.cat, L = btn.dataset.letter;
      state.prio[cat] = state.prio[cat] === L ? "" : L;
      if (cat === "race" && state.prio.race !== "A") state.metatype = "Human";
      if (cat === "magic" || cat === "race") { if (!magicOptions().includes(state.magicType)) state.magicType = "Mundane"; }
      save(); render();
    });
    // archetype starter kits
    c.querySelectorAll("[data-kit]").forEach(btn => btn.onclick = () => applyArchetype(btn.dataset.kit));
    // metatype
    c.querySelectorAll("[data-mt]").forEach(btn => btn.onclick = () => { state.metatype = btn.dataset.mt; save(); render(); });
    // attribute steppers
    c.querySelectorAll("[data-attr][data-d]").forEach(btn => btn.onclick = () => {
      const a = btn.dataset.attr, d = +btn.dataset.d;
      state.base[a] = clampNum((state.base[a] || 1) + d, 1, 50); save(); render();
    });
    // magic type -- clear now-irrelevant magic state on switch
    c.querySelectorAll("[data-magictype]").forEach(btn => btn.onclick = () => {
      state.magicType = btn.dataset.magictype;
      if (state.magicType !== "Full Mage") { state.tradition = ""; state.totem = ""; }
      if (state.magicType === "Mundane") { state.foci = []; }
      if (state.magicType === "Adept") { state.foci = state.foci.filter(x => { const f = focusDef(x.type); return f && f.who === "both"; }); }
      save(); render();
    });
    // tradition / totem
    c.querySelectorAll("[data-tradition]").forEach(btn => btn.onclick = () => {
      state.tradition = btn.dataset.tradition;
      if (state.tradition !== "Shamanic") state.totem = "";
      save(); render();
    });
    c.querySelectorAll("[data-totem]").forEach(btn => btn.onclick = () => {
      state.totem = state.totem === btn.dataset.totem ? "" : btn.dataset.totem; save(); render();
    });
    // foci
    c.querySelectorAll("[data-addfocus]").forEach(btn => btn.onclick = () => {
      const f = (window.SR2_FOCI || [])[+btn.dataset.addfocus]; if (!f) return;
      state.foci.push({ type: f.n, rating: 1, applies: "" }); save(); render();
    });
    c.querySelectorAll("[data-delfocus]").forEach(btn => btn.onclick = () => { state.foci.splice(+btn.dataset.delfocus, 1); save(); render(); });
    c.querySelectorAll("[data-focusrate]").forEach(btn => btn.onclick = () => {
      const i = +btn.dataset.focusrate, d = +btn.dataset.d;
      state.foci[i].rating = clampNum((state.foci[i].rating || 1) + d, 1, magicRating() || 6); save(); render();
    });
    c.querySelectorAll("[data-focusapplies]").forEach(inp => inp.oninput = () => { state.foci[+inp.dataset.focusapplies].applies = inp.value; save(); });
    // spells
    c.querySelectorAll("[data-addspell]").forEach(btn => btn.onclick = () => {
      const s = (window.SR2_SPELLS || [])[+btn.dataset.addspell]; if (!s) return;
      state.spells.push({ name: s.n, type: s.cat || s.typ || "", drain: s.drn || "", target: s.rng || "", duration: s.dur || "", force: Math.min(s.maxForce || 6, 4) });
      save(); render();
    });
    c.querySelectorAll("[data-delspell]").forEach(btn => btn.onclick = () => { state.spells.splice(+btn.dataset.delspell, 1); save(); render(); });
    c.querySelectorAll("[data-spellforce]").forEach(inp => inp.onchange = () => { state.spells[+inp.dataset.spellforce].force = clampNum(num(inp.value), 1, 6); save(); render(); });
    // powers
    c.querySelectorAll("[data-addpower]").forEach(btn => btn.onclick = () => {
      const p = (window.ADEPT_POWERS || [])[+btn.dataset.addpower]; if (!p) return;
      const np = { name: p.n, pp: num(p.pp) };
      if (p.rated) { np.lvl = 1; if (p.attrChoice) np.attr = "body"; }
      state.powers.push(np); save(); render();
    });
    c.querySelectorAll("[data-delpower]").forEach(btn => btn.onclick = () => { state.powers.splice(+btn.dataset.delpower, 1); save(); render(); });
    c.querySelectorAll("[data-powerlvl][data-d]").forEach(btn => btn.onclick = () => {
      const p = state.powers[+btn.dataset.powerlvl], it = powerDef(p.name); if (!it) return;
      p.lvl = clampNum((p.lvl || 1) + (+btn.dataset.d), 1, it.maxLevel || 6); save(); render();
    });
    c.querySelectorAll("[data-powerattr]").forEach(sel => sel.onchange = () => { state.powers[+sel.dataset.powerattr].attr = sel.value; save(); render(); });
    // skills
    c.querySelectorAll("[data-addskill]").forEach(btn => btn.onclick = () => {
      const name = btn.dataset.addskill; if (state.skills.some(s => s.name === name)) return;
      const def = SKILLS.find(s => s.n === name) || { attr: "", group: "" };
      state.skills.push({ name, rating: 1, attr: def.attr, group: def.group, conc: "", spec: "" }); save(); render();
    });
    c.querySelectorAll("[data-skill][data-d]").forEach(btn => btn.onclick = () => {
      const i = +btn.dataset.skill, d = +btn.dataset.d;
      state.skills[i].rating = clampNum((state.skills[i].rating || 1) + d, 1, CHARGEN_SKILL_MAX); save(); render();
    });
    c.querySelectorAll("[data-delskill]").forEach(btn => btn.onclick = () => { state.skills.splice(+btn.dataset.delskill, 1); save(); render(); });
    // concentration / specialization (live readout, no full re-render so focus is kept)
    c.querySelectorAll("[data-conc]").forEach(inp => inp.oninput = () => {
      const i = +inp.dataset.conc;
      state.skills[i].conc = inp.value;
      const specInp = c.querySelector(`[data-spec="${i}"]`);
      if (specInp) {
        const on = !!inp.value.trim();
        specInp.disabled = !on;
        specInp.placeholder = on ? (specInp.getAttribute("list") ? "type or pick a specific" : "specific form") : "set a Concentration first";
        if (!on && state.skills[i].spec) { state.skills[i].spec = ""; specInp.value = ""; }
      }
      updateTierReadout(i); save();
    });
    c.querySelectorAll("[data-spec]").forEach(inp => inp.oninput = () => {
      const i = +inp.dataset.spec;
      state.skills[i].spec = inp.value;
      updateTierReadout(i); save();
    });
    // languages
    const nativeLang = c.querySelector("[data-nativelang]");
    if (nativeLang) nativeLang.oninput = () => { state.nativeLanguage = nativeLang.value; save(); };
    const dialect = c.querySelector("[data-dialect]");
    if (dialect) dialect.oninput = () => { state.streetDialect = dialect.value; save(); };
    const addLang = c.querySelector("[data-addlang]");
    if (addLang) addLang.onclick = () => { state.languages.push({ name: "", rating: 1 }); save(); render(); };
    c.querySelectorAll("[data-langname]").forEach(inp => inp.oninput = () => { state.languages[+inp.dataset.langname].name = inp.value; save(); });
    c.querySelectorAll("[data-langrate][data-d]").forEach(btn => btn.onclick = () => {
      const i = +btn.dataset.langrate, d = +btn.dataset.d;
      state.languages[i].rating = clampNum((state.languages[i].rating || 1) + d, 1, CHARGEN_SKILL_MAX); save(); render();
    });
    c.querySelectorAll("[data-dellang]").forEach(btn => btn.onclick = () => { state.languages.splice(+btn.dataset.dellang, 1); save(); render(); });
    // resources
    c.querySelectorAll("[data-shoptab]").forEach(btn => btn.onclick = () => { shopTab = btn.dataset.shoptab; render(); });
    c.querySelectorAll("[data-buy]").forEach(btn => btn.onclick = () => {
      const [tab, idx] = btn.dataset.buy.split(":");
      const it = SHOP_TABS.find(t => t.k === tab).data()[+idx]; if (!it) return;
      const cost = typeof it.cost === "number" ? it.cost : 0;
      if (tab === "weapons") state.gear.weapons.push({ n: it.n, sub: it.sub, conceal: it.conceal, reach: it.reach, mode: it.mode, ammo: it.ammo, dmg: it.dmg, notes: it.notes || [], cost });
      else if (tab === "armor") state.gear.armor.push({ n: it.n, ballistic: it.ballistic, impact: it.impact, cost });
      else if (tab === "cyber") state.gear.cyber.push(it.rated
        ? { n: it.n, rating: 1, ess: ratedEss(it, 1), cost: ratedCost(it, 1) }
        : { n: it.n, ess: num(it.ess), cost });
      else if (tab === "vehicles") state.gear.vehicles.push({ n: it.n, sub: it.sub || it.cat, stats: it.stats || [], notes: it.notes || [], cost });
      else state.gear.other.push({ n: it.n, sub: it.sub || it.cat, cost });
      save(); render();
    });
    c.querySelectorAll("[data-delgear]").forEach(btn => btn.onclick = () => { const [k, i] = btn.dataset.delgear.split(":"); state.gear[k].splice(+i, 1); save(); render(); });
    c.querySelectorAll("[data-costedit]").forEach(inp => inp.onchange = () => { const [k, i] = inp.dataset.costedit.split(":"); state.gear[k][+i].cost = num(inp.value); save(); render(); });
    c.querySelectorAll("[data-essedit]").forEach(inp => inp.onchange = () => { state.gear.cyber[+inp.dataset.essedit].ess = num(inp.value); save(); render(); });
    c.querySelectorAll("[data-cyberrate][data-d]").forEach(btn => btn.onclick = () => {
      const g = state.gear.cyber[+btn.dataset.cyberrate], def = cyberDef(g.n); if (!def) return;
      g.rating = clampNum((g.rating || 1) + (+btn.dataset.d), 1, def.maxRating);
      g.ess = ratedEss(def, g.rating); g.cost = ratedCost(def, g.rating); // Essence & cost track the rating
      save(); render();
    });
    // matrix / decking
    const deckSel = c.querySelector("[data-deck]");
    if (deckSel) deckSel.onchange = () => { state.deck = deckSel.value; save(); render(); };
    c.querySelectorAll("[data-persona][data-d]").forEach(btn => btn.onclick = () => {
      const key = btn.dataset.persona, d = +btn.dataset.d;
      state.persona[key] = clampNum((Number(state.persona[key]) || 0) + d, 0, personaCap() || 0); save(); render();
    });
    c.querySelectorAll("[data-addprog]").forEach(btn => btn.onclick = () => {
      const p = (window.SR2_PROGRAMS || [])[+btn.dataset.addprog]; if (!p) return;
      if (state.programs.some(x => x.name === p.n)) return;
      state.programs.push({ name: p.n, rating: 1, cost: 0 }); save(); render();
    });
    c.querySelectorAll("[data-delprog]").forEach(btn => btn.onclick = () => { state.programs.splice(+btn.dataset.delprog, 1); save(); render(); });
    c.querySelectorAll("[data-prograte][data-d]").forEach(btn => btn.onclick = () => {
      const i = +btn.dataset.prograte, d = +btn.dataset.d;
      state.programs[i].rating = clampNum((state.programs[i].rating || 1) + d, 1, 12); save(); render();
    });
    c.querySelectorAll("[data-progcost]").forEach(inp => inp.onchange = () => { state.programs[+inp.dataset.progcost].cost = num(inp.value); save(); render(); });
    // searches (re-render preserving value via the live DOM read)
    ["cb-spell-search", "cb-power-search", "cb-skill-search", "cb-gear-search"].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.oninput = () => { renderStepBody(); const n = document.getElementById(id); if (n) { n.focus(); n.setSelectionRange(n.value.length, n.value.length); } };
    });
    // contacts
    const addContact = c.querySelector("[data-addcontact]");
    if (addContact) addContact.onclick = () => { state.contacts.push({ name: "", archetype: "", level: "Contact" }); save(); render(); };
    c.querySelectorAll("[data-cname]").forEach(inp => inp.oninput = () => { state.contacts[+inp.dataset.cname].name = inp.value; save(); });
    c.querySelectorAll("[data-carch]").forEach(inp => inp.oninput = () => { state.contacts[+inp.dataset.carch].archetype = inp.value; save(); });
    c.querySelectorAll("[data-clevel]").forEach(btn => btn.onclick = () => {
      const i = +btn.dataset.clevel;
      state.contacts[i].level = state.contacts[i].level === "Buddy" ? "Contact" : "Buddy"; save(); render();
    });
    c.querySelectorAll("[data-delcontact]").forEach(btn => btn.onclick = () => { state.contacts.splice(+btn.dataset.delcontact, 1); save(); render(); });
    // identity
    c.querySelectorAll("[data-id]").forEach(inp => inp.oninput = () => {
      state.identity[inp.dataset.id] = inp.value;
      // Lifestyle gates the free Street dialect, so re-render to reflect it.
      if (inp.dataset.id === "lifestyle") { save(); render(); } else { save(); }
    });
    const exp = document.getElementById("cb-export2");
    if (exp) exp.onclick = exportPDF;
  }

  /* ---------- PDF export ---------- */
  function sheetBytes() {
    const bin = atob(window.SR2_SHEET_B64);
    const arr = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; i++) arr[i] = bin.charCodeAt(i);
    return arr;
  }
  async function exportPDF() {
    const status = document.getElementById("cb-export-status");
    if (status) status.textContent = "Building PDF...";
    try {
      const doc = await window.PDFLib.PDFDocument.load(sheetBytes());
      const form = doc.getForm();
      const M = window.SR2_PDFMAP;
      const helv = await doc.embedFont(window.PDFLib.StandardFonts.Helvetica);
      const MAX_FS = 10;
      // Auto-fit text to its box but never above MAX_FS, so short values in big
      // boxes don't balloon (pdf-lib's default size 0 grows to fill the field).
      const fitSize = (f, text, max) => {
        try {
          const r = f.acroField.getWidgets()[0].getRectangle();
          if (f.isMultiline()) return Math.min(max, 8);
          const w1 = helv.widthOfTextAtSize(String(text), 1) || 0.001;
          return Math.max(4, Math.min(max, (r.width - 4) / w1, r.height - 3));
        } catch (e) { return max; }
      };
      // Standard Helvetica uses WinAnsi encoding, which can't encode typographic
      // punctuation we use in the data (minus sign, en/em dashes, smart quotes,
      // ellipsis, <=/>=). Map those to ASCII so export never throws.
      const winAnsi = (s) => String(s)
        .replace(/[-----]/g, "-")
        .replace(/[''??]/g, "'")
        .replace(/[""??]/g, '"')
        .replace(/.../g, "...")
        .replace(/<=/g, "<=").replace(/>=/g, ">=")
        .replace(/ /g, " ");
      const set = (field, val, max) => {
        if (!field) return;
        try {
          const f = form.getTextField(field);
          const text = winAnsi(val == null ? "" : String(val));
          f.setText(text);
          if (text) f.setFontSize(fitSize(f, text, max || MAX_FS));
        } catch (e) {}
      };
      const fa = finalAttrs();
      set(M.identity.name, state.identity.name);
      set(M.identity.race, state.metatype);
      set(M.identity.sex, state.identity.sex);
      set(M.identity.age, state.identity.age);
      set(M.identity.description, state.identity.desc);
      ATTRS.forEach(a => set(M.attributes[a], fa[a]));
      set(M.attributes.essence, essence().toFixed(2).replace(/\.00$/, ""));
      set(M.attributes.magic, magicRating() || "");
      set(M.derived.reaction, reaction());
      set(M.derived.initiative, reaction() + " + " + initDice() + "D6");
      set(M.derived.combatPool, combatPool());
      set(M.derived.karmaPool, CG.startKarmaPool);
      set(M.derived.goodKarma, CG.startGoodKarma);
      // dice pools (3 generic rows) -- Magic Pool (= Magic Rating) and Hacking Pool
      const extraPools = [];
      if (awakened()) extraPools.push(["Magic", magicRating()]);
      if (state.deck) extraPools.push(["Hacking", hackingPool()]);
      extraPools.slice(0, M.pools.length).forEach(([nm, val], i) => { set(M.pools[i].name, nm); set(M.pools[i].value, val); });
      // skills -- each concentration/specialization expands to its own tiered row
      const skillRows = [];
      state.skills.forEach(s => skillTiers(s).forEach(t => skillRows.push({ name: t.label, rating: t.rating })));
      // Languages are knowledge skills -- they share the skills section of the sheet.
      const intel = finalAttr("intelligence");
      if (state.nativeLanguage) skillRows.push({ name: state.nativeLanguage + " (native)", rating: intel + 2 });
      if (state.identity.lifestyle === "Street" && state.streetDialect) skillRows.push({ name: state.streetDialect + " (dialect)", rating: Math.floor(intel / 2) });
      state.languages.forEach(l => { if (l.name) skillRows.push({ name: l.name + " (lang)", rating: Number(l.rating) || 0 }); });
      skillRows.slice(0, M.skills.length).forEach((r, i) => { set(M.skills[i].name, r.name); set(M.skills[i].rating, r.rating); });
      // spells
      state.spells.slice(0, M.spells.length).forEach((s, i) => {
        const r = M.spells[i]; set(r.name, s.name); set(r.type, s.type); set(r.drain, s.drain); set(r.target, s.target); set(r.duration, s.duration); set(r.force, s.force);
      });
      // armor
      state.gear.armor.slice(0, M.armor.length).forEach((a, i) => { set(M.armor[i].type, a.n); set(M.armor[i].rating, `B${a.ballistic ?? "--"}/I${a.impact ?? "--"}`); });
      // cyber
      state.gear.cyber.slice(0, M.cyber.length).forEach((cy, i) => { set(M.cyber[i].type, cy.n); set(M.cyber[i].rating, cy.ess || ""); });
      // weapons
      state.gear.weapons.slice(0, M.weapons.length).forEach((w, i) => {
        const r = M.weapons[i]; set(r.name, w.n); set(r.type, w.sub); set(r.conceal, w.conceal); set(r.reach, w.reach); set(r.mode, w.mode); set(r.ammo, w.ammo); set(r.damage, w.dmg); set(r.modifiers, (w.notes || []).join("; "));
      });
      // cyberdeck block + persona programs
      if (state.deck) {
        set(M.deck.type, state.deck);
        set(M.deck.persona, mpcp());
        set(M.deck.hardening, deckStat("Hardening"));
        set(M.deck.memory, deckStat("Active Mem"));
        set(M.deck.storage, deckStat("Storage"));
        set(M.deck.load, deckStat("Load"));
        set(M.deck.io, deckStat("I/O"));
        set(M.deck.response, deckStat("Response") || "");
        set(M.deck.bod, state.persona.bod || "");
        set(M.deck.evasion, state.persona.evasion || "");
        set(M.deck.masking, state.persona.masking || "");
        set(M.deck.sensors, state.persona.sensors || "");
      }
      // vehicle block -- primary vehicle in the box; the rest go to the gear list
      const veh = state.gear.vehicles;
      if (veh.length && M.vehicle) {
        const v0 = veh[0];
        set(M.vehicle.type, v0.n);
        set(M.vehicle.handling, vehStat(v0, "handling"));
        set(M.vehicle.speed, vehStat(v0, "speed"));
        set(M.vehicle.body, vehStat(v0, "body"));
        set(M.vehicle.armor, vehStat(v0, "armor"));
        set(M.vehicle.signature, vehStat(v0, "sig"));
        set(M.vehicle.pilot, vehStat(v0, "pilot"));
      }
      // contacts -> Contacts & Information lines (overflow to notes)
      const contactStr = (c) => [c.name || "(unnamed)", c.archetype && "-- " + c.archetype, "(" + c.level + ")"].filter(Boolean).join(" ");
      state.contacts.slice(0, M.contacts.length).forEach((c, i) => set(M.contacts[i], contactStr(c)));
      const exContacts = state.contacts.slice(M.contacts.length);
      // Game Notes/Gear list: gear + extra vehicles + utility programs + foci (overflow to notes)
      const gearLines = [];
      state.gear.other.forEach(g => gearLines.push(g.n));
      veh.slice(1).forEach(v => gearLines.push(`${v.n} (vehicle: Hand ${vehStat(v, "handling")}, B/A ${vehStat(v, "body")}/${vehStat(v, "armor")})`));
      state.programs.forEach(p => gearLines.push(`${p.name} R${p.rating} program`));
      state.foci.forEach(x => { const f = focusDef(x.type); gearLines.push(`${x.type}${f && f.rated ? " R" + x.rating : ""}${x.applies ? " (" + x.applies + ")" : ""} [focus]`); });
      gearLines.slice(0, M.gearList.length).forEach((g, i) => set(M.gearList[i], g));
      const exGear = gearLines.slice(M.gearList.length);
      // notes box: magic build summary + overflow
      const notes = [];
      notes.push("LIFESTYLE: " + state.identity.lifestyle);
      if (state.magicType !== "Mundane") {
        let mt = "MAGE TYPE: " + state.magicType + " (Magic " + magicRating() + ")";
        if (state.magicType === "Full Mage" && state.tradition) {
          mt += " -- " + state.tradition + (state.tradition === "Shamanic" && state.totem ? ", " + state.totem + " totem" : "");
        }
        notes.push(mt);
        if (state.tradition === "Shamanic" && state.totem) {
          const tt = (window.SR2_TOTEMS || []).find(t => t.n === state.totem);
          if (tt) notes.push("TOTEM " + tt.n + ": " + [tt.spells, tt.spirits, tt.penalty].filter(Boolean).join("; ") + ". Geas: " + tt.geas);
        }
      }
      if (state.powers.length) notes.push("ADEPT POWERS: " + state.powers.map(p => { const it = powerDef(p.name); const lvl = it && it.rated ? ` L${clampNum(p.lvl || 1, 1, it.maxLevel)}${p.attr ? " " + ALABEL[p.attr].slice(0, 3) : ""}` : ""; return `${p.name}${lvl} (${powerPP(p)}PP)`; }).join(", "));
      if (state.deck) notes.push(`CYBERDECK ${state.deck}: Detection Factor ${detectionFactor()} (programs listed under Game Notes/Gear)`);
      const exSk = skillRows.slice(M.skills.length); if (exSk.length) notes.push("MORE SKILLS: " + exSk.map(r => `${r.name} ${r.rating}`).join(", "));
      const exSp = state.spells.slice(M.spells.length); if (exSp.length) notes.push("MORE SPELLS: " + exSp.map(s => `${s.name} F${s.force}`).join(", "));
      if (exGear.length) notes.push("MORE GEAR: " + exGear.join(", "));
      if (exContacts.length) notes.push("MORE CONTACTS: " + exContacts.map(contactStr).join(", "));
      set(M.notes, notes.join("\n"), 8);
      form.updateFieldAppearances(helv);
      const out = await doc.save();
      const blob = new Blob([out], { type: "application/pdf" });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url; a.download = (state.identity.name || "shadowrunner").replace(/[^\w\- ]/g, "") + ".pdf";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 4000);
      if (status) status.textContent = "OK Downloaded " + a.download;
    } catch (e) {
      if (status) status.textContent = "WARNING Export failed: " + e.message;
      console.error(e);
    }
  }

  /* ---------- nav controls ---------- */
  function go(d) { state.step = clampNum(state.step + d, 0, STEPS.length - 1); save(); render(); window.scrollTo({ top: 0, behavior: "smooth" }); }
  document.getElementById("cb-prev").onclick = () => go(-1);
  document.getElementById("cb-next").onclick = () => go(1);
  document.getElementById("cb-reset").onclick = () => { if (confirm("Reset the whole character? This clears your saved progress.")) { state = freshState(); save(); render(); } };
  document.getElementById("cb-rail").onclick = (e) => { const li = e.target.closest("[data-step]"); if (li) { state.step = +li.dataset.step; save(); render(); } };
  const expBtn = document.getElementById("cb-export"); if (expBtn) expBtn.onclick = exportPDF;

  render();
})();
