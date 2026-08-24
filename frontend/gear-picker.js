// Reusable SR2 gear catalog browser, mounted inside the play-sheet's Buy Gear modal
// (frontend/play-sheet.html). Each item buys immediately from its own inspector -- no separate
// shopping-cart/checkout step. State is a module-level singleton (not per-call locals) so
// reopening the modal within the same page session redraws instantly from already-loaded catalog
// data instead of refetching. Depends on shared.js (esc/apiFetch/showAlert/parseNum/makeGearLine)
// and catalog-taxonomy.js (grouping helpers) already being loaded on the page.
const initGearPicker = (function () {
  const CATS = [
    { k: "weapons",   label: "Weapons" },
    { k: "armor",     label: "Armor" },
    { k: "cyberware", label: "Cyberware" },
    { k: "bioware",   label: "Bioware" },
    { k: "gear",      label: "Gear",   src: "gear", pick: it => it.cat !== "deck" },
    { k: "matrix",    label: "Matrix", src: "gear", pick: it => it.cat === "deck" },
    { k: "foci",      label: "Foci",   src: "foci" },
    { k: "vehicles",  label: "Vehicles" },
  ];
  const FOCI_GROUP_ORDER = ["Spell Foci", "Spirit Foci", "Power Foci", "Weapon Foci"];
  const DOT = " · ";

  let root = null;
  let onPurchase = null;
  let alertTarget = null;        // opts.alertEl override -- falls back to #alert (play-sheet.html's convention)
  let DATA = {};                 // cat key -> [items]
  let dataLoaded = false;
  let curCat = "weapons";
  let filter = "";
  let selected = null;           // {cat, item}
  let selRating = 1;             // chosen rating for a rated selected item
  let selOpts = [];              // chosen add-on option names for the selected item
  let selGrade = "Standard";     // chosen cyberware grade for the selected item
  let VEHICLE_CLASSES = {};      // name -> {skill, conc}; GM overlay for vehicle piloting groups
  // Host page supplies these (play-sheet.html) so this shared component doesn't hardcode a
  // grade table or sourcebook-gating policy -- see gradedCyberEssence/gradedCyberCost in shared.js.
  let gradeTable = null;         // {GradeName: {ess, nuyen, book}} or null if the host doesn't offer grade choice
  let pickerEnabledBooks = new Set();
  let maxQtyFn = null;            // opts.maxQty(item, cat) -- how many more of this the host would actually let through

  function qs(sel) { return root.querySelector(sel); }
  function alertEl() { return alertTarget || document.getElementById("alert"); }
  // Cyberware only (bioware has no grade concept); skillsoft-style "other" cyberware items are
  // ungraded too (matches makeGearLine's item.cat === 'other' -> noGrade rule in shared.js).
  function isGradeable(it, cat) { return !!gradeTable && cat === "cyberware" && it && it.cat !== "other"; }
  // Defaults to unlimited for hosts that don't supply opts.maxQty (chargen, which has no ownership
  // caps at all). play-sheet.html supplies one so a max-1 item (most cyberware/bioware/armor) can't
  // have an obviously-wrong quantity typed into it.
  function maxQtyFor(it, cat) { return maxQtyFn ? Math.max(0, maxQtyFn(it, cat)) : Infinity; }
  // money() lives in shared.js now.

  // Cost of one unit of an item at a given rating (uses costTbl for rated items) plus any selected options.
  function unitCost(item, rating, opts) {
    let base = (item.rated && Array.isArray(item.costTbl) && item.costTbl[(rating || 1) - 1] != null)
      ? parseNum(item.costTbl[(rating || 1) - 1]) : parseNum(item.cost);
    if (Array.isArray(item.options) && Array.isArray(opts))
      item.options.forEach(o => { if (opts.includes(o.n)) base += parseNum(o.cost); });
    return base;
  }
  // Bonding Karma of one unit of a focus at a given rating (0 for non-magical items).
  function unitKarma(item, rating) {
    if (!item) return 0;
    if (item.rated && Array.isArray(item.karmaTbl) && item.karmaTbl[(rating || 1) - 1] != null)
      return parseNum(item.karmaTbl[(rating || 1) - 1]);
    return parseNum(item.karma);
  }
  function catDef(k) { return CATS.find(c => c.k === k) || { k, label: k }; }
  function catSrc(k) { const d = catDef(k); return d.src || d.k; }
  function findItem(cat, n) { return (DATA[catSrc(cat)] || []).find(x => x.n === n); }

  /* ---------- grouping helpers (shared taxonomy lives in catalog-taxonomy.js) ---------- */
  function gcItemRow(it) {
    const sel = selected && selected.item.n === it.n && selected.cat === curCat;
    const cost = it.rated ? "rated" : (it.cost != null ? money(parseNum(it.cost)) : "--");
    return `<div class="gc-item ${sel ? "is-sel" : ""}" data-pick="${esc(it.n)}"><span>${esc(it.n)}</span><span class="gc-item__c">${esc(cost)}</span></div>`;
  }
  function sortItems(list, byPrice) {
    return list.slice().sort(byPrice
      ? (a, b) => parseNum(a.cost) - parseNum(b.cost)
      : (a, b) => (a.n || "").localeCompare(b.n || ""));
  }
  function orderedSections(items, labelFn, order) {
    const groups = {};
    items.forEach(it => { const g = labelFn(it); (groups[g] = groups[g] || []).push(it); });
    const extra = Object.keys(groups).filter(g => !order.includes(g)).sort((a, b) => a.localeCompare(b));
    return [...order, ...extra].map(g => ({ label: g, items: groups[g] || [] }));
  }
  function labelSections(items, labelFn) {
    const groups = {};
    items.forEach(it => { const g = labelFn(it); (groups[g] = groups[g] || []).push(it); });
    return Object.keys(groups).sort((a, b) => a.localeCompare(b)).map(g => ({ label: g, items: groups[g] }));
  }
  function sectionsFor(def, items) {
    const k = def.k;
    if (k === "weapons") return orderedSections(items, weaponGroupLabel, WEAPON_GROUP_ORDER);
    if (k === "armor") return orderedSections(items, armorGroupLabel, ARMOR_GROUP_ORDER);
    if (k === "gear") return labelSections(items, gearGroupLabel);
    if (k === "foci") return orderedSections(items, it => it.sub || "Foci", FOCI_GROUP_ORDER);
    if (k === "matrix") {
      const isComp = it => it.sub === "Cyberdeck Component";
      return [{ label: "Cyberdecks", items: items.filter(it => !isComp(it)) },
              { label: "Cyberdeck Components", items: items.filter(isComp) }];
    }
    if (k === "cyberware") return orderedSections(items, cyberGroupLabel, CYBER_GROUP_ORDER);
    return [{ label: null, items }];
  }
  function renderVehicleGroups(items) {
    const groups = {};
    items.forEach(v => { const t = vehicleSkillCategory(v); (groups[t] = groups[t] || []).push(v); });
    return VEHICLE_SKILL_ORDER.map(t => {
      const list = groups[t] || [];
      if (!list.length) return "";
      const subs = {};
      list.forEach(v => { const s = v.sub || "Other"; (subs[s] = subs[s] || []).push(v); });
      const inner = Object.keys(subs).sort((a, b) => a.localeCompare(b)).map(s =>
        `<div class="gc-subcat">${esc(s)}</div>${sortItems(subs[s], true).map(gcItemRow).join("")}`).join("");
      return `<div class="gc-cat">${esc(t)}</div>${inner}`;
    }).join("");
  }

  /* ---------- tabs / list ---------- */
  function renderTabs() {
    qs("#gcTabs").innerHTML = CATS.map(c =>
      `<button type="button" class="tab ${curCat === c.k ? "is-active" : ""}" data-cat="${c.k}">${esc(c.label)}</button>`).join("");
    root.querySelectorAll("[data-cat]").forEach(b => b.onclick = () => {
      curCat = b.dataset.cat; selected = null; renderTabs(); renderList(); renderInspector();
    });
  }

  function renderList() {
    const def = catDef(curCat);
    const base = (DATA[def.src || def.k] || []).filter(def.pick || (() => true));
    const items = base
      // Attach-only items (Smartgun System, Gel-Pack Armor, ...) fold into an already-owned
      // weapon/armor line instead of being a standalone purchase -- they're bought from a control
      // on that owned line (Manage Weapons/Manage Armor), not browsed here.
      .filter(it => !it.attachToWeapon && !it.attachToArmor)
      .filter(it => { const q = filter.toLowerCase(); return !q || (it.n || "").toLowerCase().includes(q) || (it.sub || "").toLowerCase().includes(q); });
    qs("#gcCount").textContent = `${items.length} item${items.length === 1 ? "" : "s"}`;
    const byPrice = (curCat === "vehicles" || curCat === "matrix");
    let html;
    if (curCat === "vehicles") {
      html = renderVehicleGroups(items);
    } else {
      html = sectionsFor(catDef(curCat), items).map(sec => {
        const rows = sortItems(sec.items, byPrice).map(gcItemRow).join("");
        if (!rows) return "";
        return (sec.label ? `<div class="gc-cat">${esc(sec.label)}</div>` : "") + rows;
      }).join("");
    }
    html = html || `<p class="empty-state">No matches.</p>`;
    const list = qs("#gcList");
    list.innerHTML = html;
    list.querySelectorAll("[data-pick]").forEach(el => el.onclick = () => {
      const it = findItem(curCat, el.dataset.pick);
      selected = { cat: curCat, item: it };
      selRating = 1;
      selOpts = [];
      selGrade = "Standard";
      renderList(); renderInspector();
    });
  }

  /* ---------- inspector ---------- */
  const HIDE_KEYS = new Set(["n", "cat", "sub", "desc", "notes", "effect", "stats", "options"]);

  function statLine(it) {
    if (Array.isArray(it.stats) && it.stats.length)
      return it.stats.map(s => Array.isArray(s) ? `${esc(String(s[0]))} ${esc(String(s[1]))}` : esc(String(s))).join(DOT);
    const parts = [];
    const add = (k, v) => { if (v !== undefined && v !== null && v !== "") parts.push(`${k} ${esc(String(v))}`); };
    const isNA = v => v === null || v === "" || ["NA", "N/A", "-"].includes(String(v).toUpperCase());
    const addNA = (k, key) => {   // weapons/armor: always show the chip when the key is present; a dash means none / NA
      if (!(key in it)) return;
      const v = it[key];
      parts.push(`${k} ${isNA(v) ? "—" : esc(String(v))}`);
    };
    addNA("Conceal", "conceal");
    addNA("Reach", "reach");
    add("Dmg", it.dmg); add("Mode", it.mode); add("Ammo", it.ammo);
    add("Ballistic", it.ballistic); add("Impact", it.impact);
    return parts.join(DOT);
  }
  function fmtVal(v) {
    if (v === undefined) return "";
    if (v === null || v === "") return "—";   // present but N/A, e.g. Reach on a firearm -- match statLine()
    if (typeof v === "object") return esc(JSON.stringify(v));
    return esc(String(v));
  }
  function renderInspector() {
    const box = qs("#gcInsp");
    if (!selected) { box.innerHTML = `<p class="empty-state">Select an item to see its full stat block.</p>`; return; }
    const it = selected.item;
    const sl = statLine(it);
    const meta = [];
    const essLabel = selected.cat === "bioware" ? "Body Index" : "Essence";
    const gradeable = isGradeable(it, selected.cat);
    const gMult = gradeable ? (gradeTable[selGrade] || gradeTable.Standard) : null;
    if (it.rated) {
      const baseCost = unitCost(it, selRating);
      meta.push(`<span><b>Cost</b> ${money(gradeable ? gradeNuyenCost(baseCost, gMult.nuyen) : baseCost)}</span>`);
      if (Array.isArray(it.essTbl) && it.essTbl[selRating - 1] != null) {
        const baseEss = Number(it.essTbl[selRating - 1]);
        meta.push(`<span><b>${essLabel}</b> ${esc(String(gradeable ? gradeEssenceCost(baseEss, gMult.ess) : baseEss))}</span>`);
      }
    } else {
      if (it.cost != null) {
        const baseCost = unitCost(it, selRating, selOpts);
        meta.push(`<span><b>Cost</b> ${money(gradeable ? gradeNuyenCost(baseCost, gMult.nuyen) : baseCost)}</span>`);
      }
      if (it.ess != null) {
        const optEss = Array.isArray(it.options) ? it.options.reduce((a, o) => a + (selOpts.includes(o.n) ? (Number(o.ess) || 0) : 0), 0) : 0;
        const totEss = Math.round(((Number(it.ess) || 0) + optEss) * 100) / 100;
        meta.push(`<span><b>${essLabel}</b> ${esc(String(gradeable ? gradeEssenceCost(totEss, gMult.ess) : totEss))}</span>`);
      }
    }
    const kv = unitKarma(it, selRating);
    if (kv) meta.push(`<span><b>Bonding</b> <span class="text-amber">${kv} Karma</span></span>`);
    if (it.avail) meta.push(`<span><b>Avail</b> ${esc(String(it.avail))}</span>`);
    if (it.index != null) meta.push(`<span><b>Index</b> ${esc(String(it.index))}</span>`);
    if (it.legal) meta.push(`<span><b>Legal</b> ${esc(String(it.legal))}</span>`);
    if (it.src) meta.push(`<span><b>Source</b> ${esc(String(it.src))}${it.pg ? " p." + esc(String(it.pg)) : ""}</span>`);

    const notes = Array.isArray(it.notes) && it.notes.length
      ? `<div class="gc-blk"><h5>Notes</h5><ul>${it.notes.map(x => `<li>${esc(String(x))}</li>`).join("")}</ul></div>` : "";
    const effect = Array.isArray(it.effect) && it.effect.length
      ? `<div class="gc-blk"><h5>Effect</h5><ul>${it.effect.map(x => `<li>${esc(String(x))}</li>`).join("")}</ul></div>` : "";
    const optionsBlk = Array.isArray(it.options) && it.options.length
      ? `<div class="gc-blk"><h5>Options</h5><div class="gc-opts">${it.options.map(o => {
          const on = selOpts.includes(o.n);
          const bits = [money(parseNum(o.cost))];
          if (Number(o.ess)) bits.push(esc(String(o.ess)) + " Ess");
          if (o.index != null) bits.push("Index " + esc(String(o.index)));
          if (o.avail) bits.push("Avail " + esc(String(o.avail)));
          return `<label class="gc-opt"><input type="checkbox" class="chk-reveal" data-opt="${esc(o.n)}"${on ? " checked" : ""}>
            <span class="gc-opt__b"><span class="gc-opt__n">${esc(o.n)} <span class="gc-opt__c">${bits.join(DOT)}</span></span>
            ${o.desc ? `<span class="gc-opt__d">${esc(o.desc)}</span>` : ""}</span></label>`;
        }).join("")}</div></div>` : "";
    // Full data dump so nothing needed for the sheet is hidden.
    const rawRows = Object.keys(it).filter(k => !HIDE_KEYS.has(k) && !["cost", "ess", "avail", "index", "legal", "src", "pg"].includes(k))
      .map(k => `<tr><td>${esc(k)}</td><td>${fmtVal(it[k])}</td></tr>`).join("");
    const raw = rawRows ? `<div class="gc-raw"><table>${rawRows}</table></div>` : "";

    // Grade / Rating / Qty / Buy sit together as one action row -- whichever of the first three
    // doesn't apply to this item shows a greyed "-" instead of a live control.
    const gradeCtrl = gradeable
      ? (() => {
          const gopts = Object.keys(gradeTable).map(g => {
            const book = gradeTable[g].book;
            const locked = book && !pickerEnabledBooks.has(book);
            return `<option value="${esc(g)}" ${g === selGrade ? "selected" : ""} ${locked ? "disabled" : ""}>${esc(g)}${locked ? ` (needs ${esc(book)})` : ""}</option>`;
          }).join("");
          return `<select id="gcGrade" class="gc-rsel">${gopts}</select>`;
        })()
      : `<span class="gc-dash">&mdash;</span>`;
    const ratingCtrl = it.rated
      ? `<select id="gcRating" class="gc-rsel">${Array.from({ length: Math.max(1, Number(it.maxRating) || 1) }, (_, i) => i + 1)
          .map(r => `<option value="${r}" ${r === selRating ? "selected" : ""}>${r}</option>`).join("")}</select>`
      : `<span class="gc-dash">&mdash;</span>`;
    const qtyCap = maxQtyFor(it, selected.cat);
    const qtyCtrl = qtyCap > 1
      ? `<input type="number" id="gcQty" min="1" max="${qtyCap}" value="1" style="width:56px">`
      : `<span class="gc-dash">&mdash;</span>`;

    box.innerHTML = `
      <div class="gc-insp__n">${esc(it.n)}</div>
      <div class="gc-insp__sub">${esc(it.cat || "")}${it.sub ? " " + DOT + " " + esc(it.sub) : ""}</div>
      ${sl ? `<div class="gc-stat">${sl}</div>` : ""}
      <div class="gc-meta">${meta.join("")}</div>
      ${it.desc ? `<div class="gc-desc">${esc(it.desc)}</div>` : ""}
      ${effect}${optionsBlk}${notes}
      <div class="gc-add">
        <span class="gc-add__f"><b>Grade</b> ${gradeCtrl}</span>
        <span class="gc-add__f"><b>Rating</b> ${ratingCtrl}</span>
        <span class="gc-add__f"><b>Qty</b> ${qtyCtrl}</span>
        <button type="button" class="btn btn-green btn-sm" id="gcBuy" ${onPurchase && qtyCap >= 1 ? "" : "disabled"}>Buy</button>
        <span class="gc-buy-msg" id="gcBuyMsg"></span>
      </div>
      ${raw}`;
    const rsel = qs("#gcRating");
    if (rsel) rsel.onchange = () => { selRating = Number(rsel.value) || 1; renderInspector(); };
    const gsel = qs("#gcGrade");
    if (gsel) gsel.onchange = () => { selGrade = gsel.value; renderInspector(); };
    box.querySelectorAll("[data-opt]").forEach(cb => cb.onchange = () => {
      const nm = cb.dataset.opt;
      if (cb.checked) { if (!selOpts.includes(nm)) selOpts.push(nm); }
      else selOpts = selOpts.filter(x => x !== nm);
      renderInspector();
    });
    const buyBtn = qs("#gcBuy");
    if (buyBtn && onPurchase) buyBtn.onclick = async () => {
      const qtyEl = qs("#gcQty");
      const qty = qtyEl ? Math.max(1, Math.min(qtyCap, Number(qtyEl.value) || 1)) : 1;
      const rating = it.rated ? selRating : null;
      const opts = selOpts.slice();
      const grade = isGradeable(it, selected.cat) ? selGrade : undefined;
      buyBtn.disabled = true; buyBtn.textContent = "Buying…";
      try {
        // onPurchase returning false means the host silently skipped the purchase (ownership cap,
        // prerequisite, Essence/Body Index block, etc. -- play-sheet.html's purchaseGear does this
        // without throwing, since a block is an expected outcome, not an error). Anything else
        // (undefined included, for hosts like chargen's that never block) counts as success.
        const result = await onPurchase([{ cat: selected.cat, n: it.n, rating, qty, opts, grade, item: it }]);
        const msg = qs("#gcBuyMsg");
        if (msg && result !== false) {
          msg.textContent = "Purchased!";
          msg.classList.remove("is-show");
          void msg.offsetWidth;   // restart the fade animation on a repeat buy
          msg.classList.add("is-show");
        }
      } catch (e) {
        showAlert(alertEl(), `>> PURCHASE FAILED // ${e.message}`, true, true);
      } finally {
        buyBtn.disabled = false; buyBtn.textContent = "Buy";
      }
    };
  }

  /* ---------- boot ---------- */
  async function loadAll() {
    try {
      const srcs = [...new Set(CATS.map(c => c.src || c.k))];
      const results = await Promise.all(srcs.map(s =>
        apiFetch("/catalog/" + s).then(r => r.ok ? r.json() : { items: [] }).catch(() => ({ items: [] }))));
      srcs.forEach((s, i) => { DATA[s] = (results[i] && results[i].items) || []; });
      const vc = await apiFetch("/catalog/vehicle-classes").then(r => r.ok ? r.json() : null).catch(() => null);
      VEHICLE_CLASSES = (vc && vc.classes) || {};
      dataLoaded = true;
      renderTabs(); renderList(); renderInspector();
    } catch (e) {
      qs("#gcList").innerHTML = "";
      showAlert(alertEl(), `>> LOAD FAILED // ${e.message}`, true, true);
    }
  }

  // rootEl: container to mount into (its innerHTML is fully owned/replaced by this module).
  // opts.onPurchase(entries): async callback invoked with a single-item array
  // [{cat,n,rating,qty,opts,grade,item}] the moment "Buy" is clicked -- there's no cart/checkout step.
  // opts.gradeTable: {GradeName: {ess,nuyen,book}} -- omit to hide grade choice entirely (bioware-only
  // hosts, or a host that doesn't want grade selection). opts.enabledBooks: Set of sourcebook keys,
  // used only to grey out a book-gated grade (e.g. Alpha needs SSC), same as every other catalog item.
  // opts.alertEl: element to show a purchase-failure message in -- defaults to #alert (play-sheet.html
  // has one; a host without it, like character-builder.html, must pass its own).
  // opts.maxQty(item, cat): returns how many more of this item can actually be bought right now: 0
  // hides the Buy button (already owned, or an incompatible qty), 1 collapses the Qty control to a
  // dash (nothing to choose), >1 makes it an editable number capped at that value. Omit for unlimited.
  return function initGearPicker(rootEl, opts) {
    root = rootEl;
    onPurchase = (opts && opts.onPurchase) || null;
    gradeTable = (opts && opts.gradeTable) || null;
    pickerEnabledBooks = (opts && opts.enabledBooks) || new Set();
    alertTarget = (opts && opts.alertEl) || null;
    maxQtyFn = (opts && opts.maxQty) || null;
    if (opts && opts.initialCat && CATS.some(c => c.k === opts.initialCat)) {
      // A Manage-X panel's "Buy X" shortcut always names its own tab explicitly -- if that's a
      // *different* tab than whatever was last active, a leftover search term from browsing a
      // different category would be confusing (e.g. searched "vehicle" while buying Cyberware, then
      // opened the picker again from Manage Vehicles and landed on an empty-looking list).
      if (opts.initialCat !== curCat) filter = "";
      curCat = opts.initialCat;
      selected = null;
    }
    root.innerHTML = `
      <div class="tabs tabs--green" id="gcTabs"></div>
      <div class="gc-toolbar">
        <input type="text" id="gcSearch" placeholder="Search this category..." autocomplete="off">
        <span class="gc-count" id="gcCount"></span>
      </div>
      <div class="gc-grid gc-grid--2col">
        <div class="gc-panel">
          <h5 class="gc-panel__h">Items</h5>
          <div class="gc-list" id="gcList"><div class="loading">Loading catalog</div></div>
        </div>
        <div class="gc-panel">
          <h5 class="gc-panel__h">Inspector</h5>
          <div id="gcInsp"><p class="empty-state">Select an item to see its full stat block, then Buy.</p></div>
        </div>
      </div>`;
    qs("#gcSearch").value = filter;
    qs("#gcSearch").addEventListener("input", (e) => { filter = e.target.value; renderList(); });
    if (dataLoaded) { renderTabs(); renderList(); renderInspector(); }
    else { loadAll(); }
  };
})();
