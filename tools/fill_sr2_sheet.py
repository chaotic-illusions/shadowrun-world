"""Fill the official SR2 fillable character sheet from a committed/draft character.

Review artifact for the character-builder -> PDF feature. The field mapping here is what will
later drive a commit-time "download filled sheet" step. Run standalone to produce a filled PDF:

    python tools/fill_sr2_sheet.py            # fills draft 22 (Cascade) -> docs/Cascade_SR2_Sheet.pdf

Vehicles/cyberdecks: the sheet has one block each, so a PRIMARY is chosen; the rest land in Game
Notes. Contacts are passed in because drafts do not persist contact rows (only committed PCs do).
"""
from __future__ import annotations

import json
import pathlib
import re
import sqlite3

from pypdf import PdfReader, PdfWriter

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "shadowrun.db"
TEMPLATE = ROOT / "docs" / "SR2_Official_Sheet_Fillable.pdf"
# Curated full-name -> short-name overrides (reviewed in docs/name_shortening_report.csv); anything
# not listed falls back to the drop-the-make heuristic.
NAME_OVERRIDES = json.loads((ROOT / "app" / "data" / "name_overrides.json").read_text(encoding="utf-8"))
# Weapon name -> short modifier note for the sheet's "Weapon N Mods" column (recoil comp, smartlink,
# laser sight, etc.). Reviewed in docs/gear_modifiers_report.csv.
WEAPON_MODS = json.loads((ROOT / "app" / "data" / "gear_modifiers.json").read_text(encoding="utf-8"))
# Item name -> concise sheet note for carried gear whose modifier does not fit a stat field.
GEAR_NOTES = json.loads((ROOT / "app" / "data" / "gear_notes.json").read_text(encoding="utf-8"))

EM_DASH = "\u2014"

# Program key -> display name (mirrors frontend/matrix-programs.js).
PROG_DISPLAY = {
    "analyze": "Analyze", "browse": "Browse", "crash": "Crash", "defuse": "Defuse",
    "deception": "Deception", "decrypt": "Decrypt", "disinfect": "Disinfect", "evaluate": "Evaluate",
    "mirrors": "Mirrors", "read_write": "Read/Write", "relocate": "Relocate", "scanner": "Scanner",
    "validate_pgm": "Validate", "compressor": "Compressor", "sleaze": "Sleaze", "attack": "Attack",
    "black_hammer": "Black Hammer", "hog": "Hog", "killjoy": "Killjoy", "lock_on": "Lock-On",
    "poison": "Poison", "restrict": "Restrict", "reveal": "Reveal", "slow": "Slow",
    "steamroller": "Steamroller", "armor": "Armor", "camo": "Camo", "cloak": "Cloak",
    "medic": "Medic", "restore": "Restore", "shield": "Shield",
}

# Standard SR2 firearm range bands (metres) by weapon sub-type -- the item catalog does not carry
# ranges, so they are looked up here by class. (Wire-up note: the app would need this same table.)
RANGE_TABLE = {
    "Hold-Out Pistol": ("0-5", "6-10", "11-15", "16-20"),
    "Light Pistol": ("0-5", "6-15", "16-30", "31-50"),
    "Heavy Pistol": ("0-5", "6-20", "21-40", "41-60"),
    "Machine Pistol": ("0-5", "6-15", "16-30", "31-50"),
    "SMG": ("0-10", "11-40", "41-80", "81-150"),
}

# Weapon sub-type -> sheet abbreviation (the "Type" column).
WEAPON_ABBR = {
    "Hold-Out Pistol": "HO", "Light Pistol": "LP", "Heavy Pistol": "HP", "Machine Pistol": "MP",
    "SMG": "SMG", "Submachine Gun": "SMG", "Assault Rifle": "AR", "Sniper Rifle": "SnR",
    "Sport Rifle": "SpR", "Rifle": "R", "Shotgun": "SG", "LMG": "LMG", "MMG": "MMG", "HMG": "HMG",
    "Light Machine Gun": "LMG", "Medium Machine Gun": "MMG", "Heavy Machine Gun": "HMG",
    "Grenade Launcher": "GL", "Missile Launcher": "ML", "Taser": "TAS",
}

# Cyberdeck persona attributes (Bod/Evasion/Masking/Sensor) by MPCP -- total = MPCP x 3.
BEMS_TABLE = {2: (2, 2, 1, 1), 3: (3, 2, 2, 2), 6: (5, 5, 4, 4), 8: (6, 6, 6, 6),
              10: (8, 8, 7, 7), 12: (9, 9, 9, 9)}

# Lifestyle tiers by level index -> (name, monthly cost).
LIFESTYLES = [("Street", 0), ("Squatter", 100), ("Low", 1000), ("Middle", 5000),
              ("High", 10000), ("Luxury", 100000)]


def _catalog(name):
    return json.loads((ROOT / "app" / "data" / "catalog" / f"{name}.json").read_text(encoding="utf-8"))


def _find(items, n):
    return next((x for x in items if x.get("n") == n), None)


def _stat(item, key):
    for s in (item or {}).get("stats", []) or []:
        if isinstance(s, list) and str(s[0]).lower() == key.lower():
            return s[1]
    return None


def _blankish(v):
    return v is None or str(v).strip() in ("", "-", EM_DASH, "None")


def _short_name(name):
    """Trim verbose descriptors for tight fields, keeping short variant qualifiers like (Turbo).

    'Form-Fitting Body Armor (Level 2, 60% of Body)' -> 'Form-Fitting Body Armor 2'
    'Honda-GM 3220 ZX (Turbo)'                        -> unchanged
    """
    name = name or ""
    m = re.search(r"\(Level\s+(\d+)", name)
    if m:
        base = re.sub(r"\s*\(.*\)\s*$", "", name).strip()
        return f"{base} {m.group(1)}"
    # Only strip a trailing parenthetical that is a long descriptor (contains a comma).
    if re.search(r"\s*\([^)]*,[^)]*\)\s*$", name):
        return re.sub(r"\s*\([^)]*,[^)]*\)\s*$", "", name).strip()
    return name.strip()


def _weapon_abbr(sub):
    return WEAPON_ABBR.get(sub, sub or "")


def _display_name(name):
    """Short display name for a gear item (weapons/cyberware/armor): a curated override if one exists,
    else the trimmed descriptor. Vehicles/decks use _short_model (drop-the-make) instead."""
    return NAME_OVERRIDES.get(name) or _short_name(name)


def _deck_bems(mpcp):
    if mpcp in BEMS_TABLE:
        return BEMS_TABLE[mpcp]
    base, rem = divmod(mpcp * 3, 4)
    return tuple(base + (1 if i < rem else 0) for i in range(4))


def _lifestyle_str(level):
    if level is None or not (0 <= level < len(LIFESTYLES)):
        return "Lifestyle: --"
    name, cost = LIFESTYLES[level]
    if cost >= 1000:
        per = f"{cost // 1000}k/mo"
    elif cost > 0:
        per = f"{cost}/mo"
    else:
        per = "no upkeep"
    return f"Lifestyle: {name} ({per})"


def _aug_magnitude(g):
    sb = g.get("skillBonus")
    if not sb:
        return 0
    per = sb.get("per")
    if per == "halfRating":
        return int(g.get("rating") or 1) // 2
    if per == "rating":
        return int(g.get("rating") or 1)
    return int(sb.get("flat") or 0)


def _skill_aug_bonus(skill, cyber_list):
    total = 0
    for g in cyber_list:
        sb = g.get("skillBonus")
        if not sb:
            continue
        mag = _aug_magnitude(g)
        if mag and (skill.get("group") in (sb.get("groups") or [])
                    or skill.get("name") in (sb.get("skills") or [])):
            total += mag
    return total


def _skill_top_tier(s):
    """Effective rating of the highest concentration/specialization tier (SR2 skill web)."""
    base = int(s.get("rating") or 0)
    conc = (s.get("conc") or "").strip()
    spec = (s.get("spec") or "").strip()
    if conc and spec:
        return base + 2
    if conc:
        return base + 1
    return base


def load_character(char_id, db_path=DB):
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    row = con.execute("SELECT * FROM characters WHERE id=?", (char_id,)).fetchone()
    con.close()
    if not row:
        raise SystemExit(f"character {char_id} not found")
    c = dict(row)
    for k in ("skills", "adept_powers", "spells", "gear", "priorities"):
        v = c.get(k)
        c[k] = json.loads(v) if isinstance(v, str) else (v if v is not None else ({} if k in ("gear", "priorities") else []))
    return c


def load_contacts(char_id, db_path=DB):
    """Owned contacts for a committed PC as (name, detail, type) tuples for the sheet. Tolerant of an
    older DB that predates the contact_type column (falls back to loyalty for the Contact/Buddy tier).
    Drafts have no Contact rows, so this returns [] for them."""
    con = sqlite3.connect(str(db_path))
    con.row_factory = sqlite3.Row
    has_type = any(r[1] == "contact_type" for r in con.execute("PRAGMA table_info(contacts)").fetchall())
    col = "contact_type" if has_type else "NULL AS contact_type"
    rows = con.execute(
        f"SELECT name, profession, loyalty, {col} FROM contacts WHERE owner_id=? AND is_active=1",
        (char_id,)).fetchall()
    con.close()
    out = []
    for r in rows:
        ctype = r["contact_type"] or ("Buddy" if (r["loyalty"] or 0) >= 3 else "Contact")
        out.append((r["name"], r["profession"] or "", ctype))
    return out


def build_fields(c, contacts, primary_vehicle=None, legal_name=None, assume_ri=0):
    """Map a character (+ contacts + chosen primary vehicle) to PDF form-field values."""
    gear = c.get("gear") or {}
    cyber = gear.get("cyber", [])
    # Resolve each cyber/bio line against the catalog so bonus fields (skillBonus, ballistic_bonus,
    # armorTbl, poolTbl) are available even when the stored gear line did not copy them.
    _cyb_cat = _catalog("cyberware")
    _bio_cat = _catalog("bioware")
    aug_all = ([{**(_find(_cyb_cat, g.get("n")) or {}), **g} for g in cyber]
               + [{**(_find(_bio_cat, g.get("n")) or {}), **g} for g in gear.get("bio", [])])
    fields = {}

    def put(key, value):
        if value is None:
            return
        fields[key] = str(value)

    def num(x):
        try:
            return int(x or 0)
        except (TypeError, ValueError):
            return 0

    B, Q, S, CH, INT, W = (num(c[k]) for k in
                           ("body", "quickness", "strength", "charisma", "intelligence", "willpower"))
    reaction = (Q + INT) // 2
    adept = c.get("adept_powers") or []

    def _power_level(nm):
        for p in adept:
            if (p.get("name") or p.get("n")) == nm:
                return num(p.get("lvl") or 1)
        return 0

    # Combat Pool: base (Q+I+W)/2, plus Combat Sense dice, minus a Heavy/Military armor penalty
    # (cp_penalty_per points of Ballistic above Quickness).
    armor_cat = _catalog("armor")
    worn = gear.get("armor", [])[:4]
    cp_pen = 0
    for a in worn:
        asrc = _find(armor_cat, a["n"]) or {}
        per = asrc.get("cp_penalty_per")
        if per and asrc.get("ballistic") is not None and num(asrc.get("ballistic")) > Q:
            cp_pen += (num(asrc.get("ballistic")) - Q) // per
    combat_pool = max(0, (Q + INT + W) // 2 + _power_level("Combat Sense") - cp_pen)

    # Identity ---------------------------------------------------------------
    handle = c.get("name") or "Unnamed"
    put("NAME", f"{handle} ({legal_name})" if legal_name else handle)
    put("RACE", c.get("race"))
    put("SEX", c.get("gender"))
    put("AGE", c.get("age"))
    put("DESCRIPTION", c.get("archetype"))
    put("NOTES", "\u00A5{:,}".format(num(c.get("nuyen"))))

    # Attributes -------------------------------------------------------------
    put("Body", B); put("Quickness", Q); put("Strength", S)
    put("Charisma", CH); put("Intelligence", INT); put("Willpower", W)
    put("Essence", f"{float(c.get('essence') or 0):.2f}")
    if num(c.get("magic_rating")) > 0:
        put("Magic", num(c.get("magic_rating")))
    put("Karma Pool", num(c.get("karma_pool")))
    put("Good Karma", num(c.get("good_karma")))
    put("Combat Pool", combat_pool)

    # Reaction / Initiative by mode: physical + matrix (deck) / rigging (VCR) / astral (mage).
    deck = next((d for d in gear.get("matrix", []) if d.get("mpcp")), None)
    mpcp = num(deck.get("mpcp")) if deck else 0
    vcr = 0
    for g in cyber:
        m = re.search(r"vehicle control rig level (\d)", (g.get("n") or "").lower())
        if m:
            vcr = max(vcr, int(m.group(1)))
    ri = num(deck.get("respIncrease")) if deck else 0
    if deck and not ri:
        ri = assume_ri
    modes = [(reaction, 1)]                             # physical (no wired reflexes here)
    if deck:
        modes.append((reaction + ri * 2, 1 + ri))      # matrix
    if vcr:
        modes.append((reaction + vcr * 2, 1 + vcr))    # rigging
    if c.get("magic_type") == "Full Mage":
        modes.append((INT, 1))                         # astral
    put("Reaction", " / ".join(str(m[0]) for m in modes))
    put("Initiative", " / ".join(f"{m[1]}D6" for m in modes))

    # Dice pools -------------------------------------------------------------
    def _pool_bonus(kind):
        """Sum a cyber/bioware dice-pool bonus (poolTbl[kind]) across installed augmentations."""
        total = 0
        for g in aug_all:
            tbl = (g.get("poolTbl") or {}).get(kind)
            if tbl:
                r = num(g.get("rating") or 1)
                total += tbl[min(r, len(tbl)) - 1]
        return total

    pools = []
    if mpcp:
        # SR2 Hacking Pool = (Intelligence + MPCP)/3, rounded down; a Math SPU (Shadowtech) then adds
        # floor(rating/2) directly to the pool (matches app/services/matrix_engine.hacking_pool).
        pools.append(("Hacking", (INT + mpcp) // 3 + _pool_bonus("hack")))
    if vcr:
        # SR2: a Vehicle Control Rig grants a Control Pool = rigging Reaction (reaction + VCR*2) + VCR level.
        pools.append(("Control", reaction + vcr * 2 + vcr))
    task = _pool_bonus("task")            # Task Pool comes entirely from cyber (e.g. Encephalon)
    if task:
        pools.append(("Task", task))
    for idx, (name, rating) in enumerate(pools[:3], start=1):
        put(f"Pool Name {idx}", name)
        put(f"Pool Rating {idx}", rating)

    # Skills: name carries the concentration; rating = highest tier + cyber skill bonus (Math SPU).
    for idx, s in enumerate(sorted(c.get("skills") or [], key=lambda x: x.get("name", ""))[:19], start=1):
        conc = (s.get("conc") or "").strip()
        spec = (s.get("spec") or "").strip()
        name = s.get("name", "")
        if conc:
            name += f": {conc}"
        if spec:
            name += f": {spec}"
        put(f"Skill Name {idx}", name)
        put(f"Skill Rating {idx}", _skill_top_tier(s) + _skill_aug_bonus(s, aug_all))

    # Armor ------------------------------------------------------------------
    # Bodyware/bioware armor (Dermal Plating/Sheath, Orthoskin, Bone Lacing) adds to worn armor;
    # sum the Ballistic/Impact bonuses and bump the FIRST worn armor line (user's choice).
    def _armor_bonus(g, which):
        tbl = (g.get("armorTbl") or {}).get(which)
        if tbl:
            r = num(g.get("rating") or 1)
            return tbl[min(r, len(tbl)) - 1]
        return num(g.get(f"{which}_bonus"))

    mystic = _power_level("Mystic Armor")   # adept Mystic Armor adds to both armor tracks
    body_b = sum(_armor_bonus(g, "ballistic") for g in aug_all) + mystic
    body_i = sum(_armor_bonus(g, "impact") for g in aug_all) + mystic

    for idx, a in enumerate(worn, start=1):
        src = _find(armor_cat, a["n"]) or {}
        put(f"Armor Type {idx}", _display_name(a["n"]))
        if src.get("ballistic") is not None or src.get("impact") is not None:
            b = num(src.get("ballistic")) + (body_b if idx == 1 else 0)
            i = num(src.get("impact")) + (body_i if idx == 1 else 0)
            put(f"Armor Rating {idx}", f"{b}/{i}")
    if not worn and (body_b or body_i):        # no worn armor, but cyber/bio grants some
        put("Armor Type 1", "Cyber/Bioware")
        put("Armor Rating 1", f"{body_b}/{body_i}")

    # Cyberware / bioware ----------------------------------------------------
    for idx, g in enumerate((cyber + gear.get("bio", []))[:16], start=1):
        name = g["n"]
        short = _display_name(name)
        rating = g.get("rating")
        if not rating:                       # surface a plain "Level N" (e.g. VCR) as the rating,
            m = re.search(r"[Ll]evel\s+(\d+)", name or "")   # unless the short name already shows it
            if m and m.group(1) not in short:
                rating = m.group(1)
        put(f"Cyberware Type {idx}", short)
        put(f"Cyberware Rating {idx}", rating if rating else "")

    # Weapons -- Conceal now folds in data-driven bonuses from the catalog:
    #   * armor with conceal_scope "beneath" (Lined Coat +2 flat; Secure Long Coat +50% for conceal>=4)
    #   * each Concealable Holster (conceal_scope "pistol") adds its bonus to ONE holstered pistol/taser
    weap_cat = _catalog("weapons")
    armor_items = [(_find(armor_cat, a["n"]) or {}) for a in gear.get("armor", [])]
    armor_flat = sum(num(a.get("conceal_bonus")) for a in armor_items
                     if a.get("conceal_scope") == "beneath" and a.get("conceal_bonus"))
    armor_pcts = [(num(a.get("conceal_bonus_pct")), num(a.get("conceal_min_rating") or 0))
                  for a in armor_items if a.get("conceal_scope") == "beneath" and a.get("conceal_bonus_pct")]
    holster_bonuses = [num((_find(weap_cat, w["n"]) or {}).get("conceal_bonus"))
                       for w in gear.get("weapons", [])
                       if (_find(weap_cat, w["n"]) or {}).get("conceal_scope") == "pistol"]

    slot = 0
    for wln in gear.get("weapons", []):
        src = _find(weap_cat, wln["n"]) or {}
        if src.get("cat") in ("accessory", "ammo"):
            continue
        slot += 1
        if slot > 5:
            break
        sub = src.get("sub") or wln.get("sub") or ""
        conceal = src.get("conceal")
        if isinstance(conceal, (int, float)):
            base = int(conceal)
            conceal = base + armor_flat
            for pct, minr in armor_pcts:
                if base >= minr:
                    conceal += (base * pct) // 100
            if ("pistol" in sub.lower() or "taser" in sub.lower()) and holster_bonuses:
                conceal += holster_bonuses.pop(0)   # one holster covers one pistol/taser
        else:
            conceal = "\u2014"   # heavy weapon / no concealability rating
        put(f"Weapon {slot} Name", _display_name(wln["n"]))
        put(f"Weapon {slot} Type", _weapon_abbr(sub))
        put(f"Weapon {slot} Mods", WEAPON_MODS.get(wln["n"]))
        put(f"Weapon {slot} Conceal", conceal)
        if not _blankish(src.get("reach")):
            put(f"Weapon {slot} Reach", src.get("reach"))
        put(f"Weapon {slot} Mode", src.get("mode"))
        put(f"Weapon {slot} Dmg", src.get("dmg"))
        put(f"Weapon {slot} Ammo", src.get("ammo"))
        bands = RANGE_TABLE.get(sub)
        if bands:
            put(f"Weapon {slot} Short", bands[0]); put(f"Weapon {slot} Med", bands[1])
            put(f"Weapon {slot} Long", bands[2]); put(f"Weapon {slot} Extreme", bands[3])

    # Melee-capable armor (Forearm Guards, Riot Shields) listed as weapon entries.
    for a in worn:
        mel = (_find(armor_cat, a["n"]) or {}).get("melee")
        if not mel or slot >= 5:
            continue
        slot += 1
        put(f"Weapon {slot} Name", _display_name(a["n"]))
        put(f"Weapon {slot} Type", "Melee")
        put(f"Weapon {slot} Dmg", mel.get("dmg"))
        if mel.get("reach") is not None:
            put(f"Weapon {slot} Reach", mel.get("reach"))
        if mel.get("mods"):
            put(f"Weapon {slot} Mods", mel.get("mods"))

    # Vehicle (primary block) ------------------------------------------------
    veh_cat = _catalog("vehicles")
    vehicles = gear.get("vehicles", [])
    primary = primary_vehicle or (vehicles[0]["n"] if vehicles else None)
    vsrc = _find(veh_cat, primary) if primary else None
    if vsrc:
        # Sheet field is narrow: drop the make (first word), keeping the model (+ any qualifier),
        # e.g. "Harley-Davidson Scorpion" -> "Scorpion", "Honda-GM 3220 ZX (Turbo)" -> "3220 ZX (Turbo)".
        put("Vehicle Type", _short_model(primary))
        put("Vehicle Handling", _stat(vsrc, "Handling"))
        put("Vehicle Speed", _stat(vsrc, "Speed"))
        put("Vehicle Body", _stat(vsrc, "Body"))
        put("Vehicle Armor", _stat(vsrc, "Armor"))
        put("Vehicle Sig", _stat(vsrc, "Sig"))
        pilot = _stat(vsrc, "Pilot")
        put("Vehicle Pilot", "" if _blankish(pilot) else pilot)
        put("Vehicle Notes", " | ".join(
            f"{k} {_stat(vsrc, k)}" for k in ("Accel", "Autonav", "Sensor", "Cargo", "Load")
            if _stat(vsrc, k) is not None))

    # Cyberdeck (primary block) ----------------------------------------------
    gear_cat = _catalog("gear")
    if deck:
        dsrc = _find(gear_cat, deck["n"]) or {}
        # Drop the make (first word), e.g. "Fuchi Cyber-6" -> "Cyber-6".
        put("Cyberdeck Type", _short_model(deck["n"]))
        put("Persona", _stat(dsrc, "MPCP"))
        put("Hardening", _stat(dsrc, "Hardening"))
        put("MEMORY", _stat(dsrc, "Active Mem"))
        put("STORAGE", _stat(dsrc, "Storage"))
        put("LOAD", _stat(dsrc, "Load"))
        put("IO", _stat(dsrc, "I/O"))
        put("RESPONSE", ri)
        bod, ev, mask, sen = _deck_bems(mpcp)
        put("Bod Rating", bod); put("Evasion Rating", ev)
        put("Masking Rating", mask); put("Sensors Rating", sen)

    # Contacts ---------------------------------------------------------------
    # Each contact is (name, detail, type) where type is Contact/Buddy/Gang/Tribe/Follower.
    # Gang/Tribe list the gang/tribe name; the rest list "handle - archetype (Type)".
    if contacts:
        lines = []
        for n, detail, ctype in contacts:
            if ctype in ("Gang", "Tribe"):
                lines.append(f"{ctype}: {n}")
            elif detail:
                lines.append(f"{n} - {detail} ({ctype})")
            else:
                lines.append(f"{n} ({ctype})")
        put("Contacts & Information", "\n".join(lines))

    # Character notes (page 2): extra vehicles, gear/tools, lifestyle --------
    cnotes = []
    other_veh = [v for v in vehicles if v["n"] != primary]
    if other_veh:
        cnotes.append("Vehicles: " + "; ".join(
            f"{_short_name(v['n'])} - {v.get('sub', '')}".strip(" -") for v in other_veh))
    tools = gear.get("gear", [])
    if tools:
        cnotes.append("Gear: " + "; ".join(
            (f"{g.get('kind', '')} {g['n']}").strip() for g in tools))
    # Concise mechanical notes for carried items whose modifier does not fit a dedicated field.
    mod_notes = []
    for bucket in ("weapons", "armor", "cyber", "bio", "gear"):
        for g in gear.get(bucket, []):
            note = GEAR_NOTES.get(g.get("n"))
            if note:
                mod_notes.append(f"{_display_name(g['n'])}: {note}")
    if mod_notes:
        cnotes.append("Mods: " + " | ".join(mod_notes))
    cnotes.append(_lifestyle_str(c.get("lifestyle_level")))
    put("Character Notes", "\n".join(cnotes))

    # Game notes: the deck's program library, "Name-Rating" ------------------
    progs = gear.get("programs", [])
    if progs:
        put("Game Notes Gear", ", ".join(
            f"{PROG_DISPLAY.get(p.get('prog'), p.get('prog'))}-{p.get('rating')}{p.get('dmg') or ''}"
            for p in progs))

    return fields


# Multiline note boxes keep the template's own font size so lines sit on the printed rules.
NOTE_FIELDS = {"Character Notes", "Contacts & Information", "Game Notes Gear", "Vehicle Notes"}
# Fields shown left-aligned instead of the template's centered default.
LEFT_JUSTIFY = {"NAME", "RACE", "SEX", "AGE"}


def _drop_make(name):
    """Drop the make (first token) from a make/model string: 'Fuchi Cyber-6' -> 'Cyber-6',
    'Honda-GM 3220 ZX (Turbo)' -> '3220 ZX (Turbo)'."""
    return name.split(maxsplit=1)[1] if " " in name else name


def _short_model(name):
    """PDF short name for a vehicle/deck: a curated override if one exists, else drop the make."""
    return NAME_OVERRIDES.get(name) or _drop_make(name)


def _field_size(name):
    """Auto-size (0) for variable-length name/type fields so long values shrink to fit the box (never
    run off the edge); a fixed medium size for short value fields (never huge)."""
    if re.match(r"(Skill Name|Armor Type|Cyberware Type) \d+$", name):
        return 0
    if re.match(r"Weapon \d+ Name$", name):
        return 0
    if re.match(r"Weapon \d+ ", name):    # Type/Conceal/Reach/Mode/ranges/Ammo/Dmg/Mods -- tight columns
        return 8
    if name in ("Vehicle Type", "Cyberdeck Type"):
        return 0
    if re.match(r"Pool Name \d+$", name):
        return 9   # narrow box: "Hacking"/"Combat" fit at 9pt
    return 10


def fill_pdf(fields, out_path, template=TEMPLATE):
    """Fill the form and normalize appearance: force a regular (non-bold) Helvetica on every filled
    field, auto-size long name/type fields so nothing runs off the edge, leave note boxes at their
    template size so text lines up with the printed rules, and left-justify NAME/SEX/AGE."""
    from pypdf.generic import NameObject, NumberObject, TextStringObject
    reader = PdfReader(str(template))
    writer = PdfWriter()
    writer.append(reader)

    def _tune(obj, inherited=None):
        name = str(obj.get("/T", inherited))
        # Note boxes are left untouched (keep template font + size) so they align with the rules.
        if name in fields and name not in NOTE_FIELDS:
            size = _field_size(name)
            da = str(obj.get("/DA") or "/Helv 0 Tf 0 g")
            # Force regular Helvetica (the template uses MyriadPro-Bold on the stat fields, which the
            # viewer renders as Helvetica-Bold -- that was the inconsistent bolding).
            newda = re.sub(r"/\S+\s+[\d.]+\s+Tf", f"/Helv {size} Tf", da)
            if "Tf" not in newda:
                newda = f"/Helv {size} Tf 0 g"
            obj[NameObject("/DA")] = TextStringObject(newda)
        if name in LEFT_JUSTIFY:
            obj[NameObject("/Q")] = NumberObject(0)   # left-justify (was centered)
        for kid in obj.get("/Kids", []) or []:
            _tune(kid.get_object(), name)

    # Tune DA + justification FIRST so the appearance streams pypdf bakes below use the new
    # (non-bold, correctly-sized) font -- otherwise the baked /AP keeps the template's bold font.
    for fld in writer._root_object["/AcroForm"]["/Fields"]:
        _tune(fld.get_object())
    for page in writer.pages:
        writer.update_page_form_field_values(page, fields, auto_regenerate=False)

    try:
        writer.set_need_appearances_writer(True)      # so viewers render the values
    except Exception:  # noqa: BLE001 -- older pypdf fallback
        from pypdf.generic import BooleanObject
        writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
    with open(out_path, "wb") as fh:
        writer.write(fh)


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Fill the SR2 AcroForm character sheet from a character in the DB.")
    ap.add_argument("--char-id", type=int, default=22, help="character id to render")
    ap.add_argument("--out", default=str(ROOT / "docs" / "Cascade_SR2_Sheet.pdf"), help="output PDF path")
    ap.add_argument("--legal-name", default="Casper Kincaide", help="legal name printed on the sheet")
    ap.add_argument("--primary-vehicle", default="Harley-Davidson Scorpion", help="vehicle to feature")
    ap.add_argument("--assume-ri", type=int, default=2,
                    help="assumed Response Increase levels (test aid; 0 for a normal character)")
    args = ap.parse_args()

    # Demo chargen contacts -- no CLI for these yet.
    CONTACTS = [
        ("Delta Six", "Decker", "Contact"),
        ("Mr. Fabulous", "Fixer", "Buddy"),
    ]

    char = load_character(args.char_id)
    fields = build_fields(char, CONTACTS, args.primary_vehicle, legal_name=args.legal_name, assume_ri=args.assume_ri)
    fill_pdf(fields, args.out)
    print(f"Wrote {args.out}  ({len(fields)} fields set)")
