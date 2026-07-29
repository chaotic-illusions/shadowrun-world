"""Rules-coverage audit for the VR2 Matrix run engine.

This is a *self-maintaining* contract test. It cross-references the rules surface
(the enumerations that describe what the game *can* do) against the implementation
(the code that makes it happen), so that adding a new action / utility / program
option / IC type WITHOUT wiring it up -- on both sides where the rules are
symmetric -- fails the suite loudly instead of silently falling through to a no-op.

The four surfaces it locks down:

  A. Actions      -- every ``ActionType`` is classified and has a declared cost.
  B. Utilities    -- every ``DeckerUtilities`` slot is classified by how it resolves.
  C. Options      -- every ``ProgramOptions`` field has a documented consumer.
  D. IC           -- every ``IC_CATALOG`` entry maps to an engine resolution path.
  E. Dual mechanics -- programs the rules model for BOTH the PC and the enemy
     (Attack / Cripplers / Hog) must resolve through a shared engine primitive, and
     the KNOWN_ASYMMETRIES scoreboard tracks which ones still apply their *state*
     divergently per direction (the class of bug this audit exists to kill).

The registries below are the *test-owned source of truth*. When you add something
to the schema or a catalog, you must add it here too (with a note on how it is
wired) or a coverage test fails. That is the point: it forces the "is this actually
reachable, and modelled once for both sides?" decision at the moment of change.
"""

from __future__ import annotations

import typing

from app.schemas.matrix_run import ActionType, DeckerUtilities, ProgramOptions
from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.routers import matrix_runs as mr


ACTIONS: set[str] = set(typing.get_args(ActionType))
UTILITIES: set[str] = set(DeckerUtilities.model_fields)
OPTIONS: set[str] = set(ProgramOptions.model_fields)
IC_TYPES: set[str] = set(rules.IC_CATALOG)


def _has(module, name: str) -> bool:
    return hasattr(module, name)


# =============================================================================
# A. ACTIONS  --  every requestable action is classified and costed
# =============================================================================
# role -> how the action resolves in perform_action:
#   system_op   : generic system_test (+ optional reveal/side-effect success block)
#   safe_exit   : dedicated graceful-logoff handler
#   memory      : swap / unload active-memory programs
#   repair      : self-directed program/persona repair
#   defuse      : disarm a data bomb
#   anti_ic     : offensive program aimed at a host IC (Slow / Steamroller)
#   autonomous  : DINAB (runs one carried program as a Free action)
#   maneuver    : cybercombat positioning (Evade / Parry / Position)
ACTION_ROLE: dict[str, str] = {
    "logon_to_host": "system_op",
    "analyze_host": "system_op",
    "analyze_ic": "system_op",
    "analyze_icon": "system_op",
    "analyze_security": "system_op",
    "analyze_subsystem": "system_op",
    "locate_paydata": "system_op",
    "locate_file": "system_op",
    "locate_ic": "system_op",
    "locate_decker": "system_op",
    "download_data": "system_op",
    "edit_file": "system_op",
    "null_operation": "system_op",
    "crash_host": "system_op",
    "validate_passcode": "system_op",
    "invalidate_passcode": "system_op",
    "decoy": "system_op",
    "redirect_datatrail": "system_op",
    "relocate": "system_op",
    "decrypt_file": "system_op",
    "decompress_file": "system_op",
    "graceful_logoff": "safe_exit",
    "swap_memory": "memory",
    "unload_program": "memory",
    "purge_hog": "repair",
    "medic": "repair",
    "restore": "repair",
    "disinfect": "repair",
    "defuse_data_bomb": "defuse",
    "steamroller": "anti_ic",
    "slow": "anti_ic",
    "dinab": "autonomous",
    "evade_detection": "maneuver",
    "parry_attack": "maneuver",
    "position_attack": "maneuver",
}

# Cost keys that intentionally are NOT ActionType members. Cybercombat attacks go
# through the dedicated /attack endpoint (pass-budget key "attack") and Scan Icon through
# the dedicated /enemy-decker/scan endpoint (pass-budget key "scan_icon"); trap-door entry uses
# its dedicated /trap-door/{id} endpoint; "attack_ic" is a vestigial key derived from the
# SYSTEM_OPERATIONS display table and is superseded by it.

_NON_ACTION_COST_KEYS: set[str] = {
    "attack", "attack_ic", "scan_icon", "logon_to_ltg", "trap_door_enter",
}


def test_action_role_registry_matches_schema():
    """Every ActionType is classified here, and nothing extra is."""
    assert set(ACTION_ROLE) == ACTIONS, (
        f"unclassified actions: {ACTIONS - set(ACTION_ROLE)}; "
        f"stale registry entries: {set(ACTION_ROLE) - ACTIONS}"
    )


def test_every_action_type_has_an_explicit_cost():
    """No ActionType may rely on the silent 'Complex' fallback in _spend_pass_action."""
    missing = ACTIONS - set(mr._ACTION_COST)
    assert not missing, f"actions with no declared cost (defaulting silently): {missing}"


def test_no_unexpected_orphan_cost_keys():
    """Every cost key is either an ActionType or a documented non-/action key."""
    orphans = set(mr._ACTION_COST) - ACTIONS - _NON_ACTION_COST_KEYS
    assert not orphans, f"cost keys with no action/endpoint: {orphans}"


def test_system_operations_table_maps_to_actions():
    """Every documented System Operation is implemented as an action (or the /attack endpoint)."""
    handled_elsewhere = {"attack_ic",       # Attack IC is the /attack endpoint, not an /action
                         "logon_to_ltg"}    # intentionally not a run action (a run starts on a host)
    for op in rules.SYSTEM_OPERATIONS:
        key = op["name"].lower().replace(" ", "_")
        assert key in ACTIONS or key in handled_elsewhere, (
            f"System Operation '{op['name']}' ({key}) has no ActionType"
        )


# =============================================================================
# B. UTILITIES  --  every deck program slot is classified by how it resolves
# =============================================================================
# role:
#   offensive     : opposed attack vs an enemy icon (deals damage / cripples)
#   self_repair   : heals/repairs the decker's own icon
#   defensive     : reduces incoming damage (resist / parry)
#   anti_ic       : defeats a specific IC family (Tar / proactive / Worm)
#   operational   : reduces the TN of / enables a System Operation
#   maneuver      : augments a combat-maneuver opposed test (Cloak / Lock-On)
#   passive       : build/trace-time only; no in-run active test of its own
UTILITY_ROLE: dict[str, str] = {
    # stealth / detection
    "sleaze": "passive",        # feeds Detection Factor
    "camo": "passive",          # feeds Trace Factor
    "scanner": "operational",   # Sensor aid for Locate Decker
    # operations
    "deception": "operational",
    "browse": "operational",
    "analyze": "operational",
    "evaluate": "operational",
    "decrypt": "operational",
    "defuse": "operational",
    "crash": "operational",
    "mirrors": "operational",
    "validate_pgm": "operational",
    "read_write": "operational",
    "relocate": "operational",
    # offense
    "attack": "offensive",
    "poison": "offensive",
    "restrict": "offensive",
    "reveal": "offensive",
    "hog": "offensive",
    "black_hammer": "offensive",
    "killjoy": "offensive",
    # anti-IC offense
    "steamroller": "anti_ic",
    "slow": "anti_ic",
    "disinfect": "anti_ic",
    # combat maneuvers (modify the Evade/Parry/Position opposed-test TNs; work for PC and enemy)
    "cloak": "maneuver",        # lowers the maneuvering icon's Evasion-test TN
    "lock_on": "maneuver",      # lowers the opposing icon's Sensor-test TN
    # defense
    "armor": "defensive",
    "shield": "defensive",
    # self-repair
    "restore": "self_repair",
    "medic": "self_repair",
    # special
    "compressor": "passive",    # download-size reduction only
}


def test_utility_role_registry_matches_schema():
    """Every DeckerUtilities slot is classified here, and nothing extra is."""
    assert set(UTILITY_ROLE) == UTILITIES, (
        f"unclassified utilities: {UTILITIES - set(UTILITY_ROLE)}; "
        f"stale registry entries: {set(UTILITY_ROLE) - UTILITIES}"
    )


# =============================================================================
# C. PROGRAM OPTIONS  --  every option is consumed somewhere in resolution
# =============================================================================
# Each option maps to a short note on where the engine/router reads it. The test
# only asserts coverage (a new option must be classified); the notes are for humans.
OPTION_CONSUMER: dict[str, str] = {
    "skulk": "crashing IC: reduces the tally increase",
    "area": "attack: offsets an IC cluster's TN penalty",
    "dinab": "DINAB: _effective_dinab / _apply_dinab autonomous run",
    "targeting": "attack: -2 to-hit TN",
    "penetration": "attack: defeats Shield",
    "chaser": "attack: defeats Shift",
    "one_shot": "single-use copy: consumed on use / Tar-wiped",
    "squeeze": "compressed: half storage; must decompress (Complex) after a mid-run swap-in",
    "limit_target": "restricts a utility to only 'ic' or 'decker' targets",
    "damage_level": "attack: the utility's own coded base Damage Level (not the host IC table)",
}


def test_option_consumer_registry_matches_schema():
    """Every ProgramOptions field has a documented consumer, and nothing extra is listed."""
    assert set(OPTION_CONSUMER) == OPTIONS, (
        f"unclassified options: {OPTIONS - set(OPTION_CONSUMER)}; "
        f"stale registry entries: {set(OPTION_CONSUMER) - OPTIONS}"
    )


# =============================================================================
# D. IC  --  every catalogued IC maps to an engine resolution path
# =============================================================================
IC_ROLE: dict[str, str] = {
    "Probe": "reactive_probe",
    "Killer": "proactive_attacker",
    "Acid": "crippler",
    "Binder": "crippler",
    "Jammer": "crippler",
    "Marker": "crippler",
    "Tar Baby": "reactive_tar",
    "Data Bomb": "reactive_bomb",
    "Scramble": "reactive_scramble",
    "Blaster": "proactive_attacker",
    "Sparky": "proactive_attacker",
    "Acid-rip": "ripper",
    "Bind-rip": "ripper",
    "Jam-rip": "ripper",
    "Mark-rip": "ripper",
    "Tar Pit": "reactive_tar",
    "Worm": "reactive_worm",
    "Trace": "trace",
    "Black IC": "proactive_attacker",
}

# role -> (module, engine-primitive that resolves it). Existence is asserted so a
# rename/deletion of a resolver is caught.
IC_ROLE_PRIMITIVE: dict[str, tuple[object, str]] = {
    "reactive_probe": (eng, "probe_test"),
    "proactive_attacker": (eng, "cybercombat_attack"),
    "crippler": (eng, "crippler_attack"),
    "ripper": (eng, "crippler_attack"),
    "reactive_tar": (eng, "tar_baby_test"),
    "reactive_bomb": (eng, "data_bomb_defuse"),
    "reactive_scramble": (eng, "scramble_decrypt_test"),
    "reactive_worm": (eng, "worm_attack"),
    "trace": (eng, "trace_hunt_cycle_attack"),
}


def test_ic_role_registry_matches_catalog():
    """Every IC_CATALOG entry is classified here, and nothing extra is."""
    assert set(IC_ROLE) == IC_TYPES, (
        f"unclassified IC: {IC_TYPES - set(IC_ROLE)}; "
        f"stale registry entries: {set(IC_ROLE) - IC_TYPES}"
    )


def test_every_ic_role_is_backed_by_a_primitive():
    """Each IC role names an engine resolver, and the resolver exists."""
    for ic, role in IC_ROLE.items():
        assert role in IC_ROLE_PRIMITIVE, f"IC role '{role}' ({ic}) has no primitive mapping"
        module, name = IC_ROLE_PRIMITIVE[role]
        assert _has(module, name), f"resolver {name} for IC role '{role}' is missing"


# =============================================================================
# E. DUAL MECHANICS  --  programs the rules model for BOTH sides
# =============================================================================
# The rules say Hog / the cripplers / cybercombat Attack work the same whoever
# fires them. Each MUST resolve dice through one shared engine primitive. Whether
# they also apply their *resulting state* through one shared path is tracked by
# ``shared_application``; the ones that do not (yet) are enumerated in
# KNOWN_ASYMMETRIES so the divergence is visible and burned down deliberately.
DUAL_MECHANICS: list[dict] = [
    {
        "name": "attack",
        "primitive": (eng, "cybercombat_attack"),
        "shared_application": True,
        "note": "all four directions (PC->IC attack_ic, PC->enemy, IC->PC, decker->PC) resolve "
                "icon damage through eng.cybercombat_attack: to-hit vs COMBAT_TN, Bod/SV resist "
                "vs Power = the attacker program/IC rating.",
    },
    {
        "name": "crippler",
        "primitive": (eng, "attribute_attack_core"),
        "shared_application": True,
        "note": "poison/restrict/reveal AND Acid/Binder/Marker/Jammer route through "
                "_resolve_attribute_attack + attribute_attack_core; only the actor label differs.",
    },
    {
        "name": "hog",
        "primitive": (eng, "hog_attack"),
        "shared_application": True,
        "note": "one _resolve_hog + _HogTarget seam + _drain_all_hog_infections loop drive both directions.",
    },
    {
        "name": "black",
        "primitive": (eng, "black_attack"),
        "shared_application": True,
        "note": "Black IC (lethal/non-lethal) AND the Black Hammer/Killjoy programs (enemy->PC and "
                "PC->enemy) resolve one Attack Test that stages BOTH the icon (Bod) and, when the "
                "target's flesh is simulated, the meat (Body/Willpower) through eng.black_attack. "
                "Actor differences are rider args only: construct base = IC_DAMAGE_LEVEL[sec] vs "
                "program base = fixed Serious; meat_pool present (PC target) vs None (enemy icon-only).",
    },
    {
        "name": "shield",
        "primitive": (eng, "shield_parry"),
        "shared_application": True,
        "note": "the PC decker (_shield_parry) AND an enemy security decker (_enemy_shield_parry) "
                "both route through one shared _shield_parry_core: roll the effective Shield vs the "
                "attacker's skill via eng.shield_parry, wear -1 Rating Point win or lose. Actor "
                "differences are display only -- event visibility (player shield_parry vs GM-only "
                "enemy_shield_parry) and which dict's program_damage holds the wear.",
    },
    {
        "name": "medic",
        "primitive": (eng, "medic_heal"),
        "shared_application": True,
        "note": "the PC decker (_apply_medic) AND an enemy security decker (_enemy_medic_heal) both "
                "route through one shared _medic_heal_core: roll the effective Medic vs the icon's "
                "current wound-level TN via eng.medic_heal, heal min(boxes, successes), wear -1 "
                "Rating Point win or lose. Actor differences are display + PC-only riders (DINAB "
                "pool_override, One-Shot, undamaged/offline info events) -- the heal math is shared.",
    },
    {
        "name": "restore",
        "primitive": (eng, "restore_repair"),
        "shared_application": True,
        "note": "the PC decker (_apply_restore) AND an enemy security decker (_enemy_restore_repair) "
                "both route through one shared _restore_repair_core: repair one persona attribute's "
                "TEMPORARY crippler damage in that actor's OWN condition-monitor ledger (TN = the "
                "recorded causing crippler rating, points = successes//2 capped by repairable damage, "
                "never below the permanent Persona-chip floor) via eng.restore_repair. Enemy cripple "
                "damage now uses the SAME ledger as the PC (base attr in enemy[attr] untouched; "
                "effective = base - persona_damage via _enemy_effective_attr), so the one core "
                "repairs either persona identically. Restore does NOT self-degrade -> no wear. Actor "
                "differences are display + PC-only riders (DINAB pool_override, One-Shot, undamaged/"
                "offline info events).",
    },
    {
        "name": "maneuver",
        "primitive": (eng, "maneuver_test"),
        "shared_application": True,
        "note": "combat maneuvers (Evade/Parry/Position) resolve for BOTH the PC (_apply_maneuver) "
                "and an IC/enemy decker (_resolve_npc_maneuver) through one eng.maneuver_test opposed "
                "Evasion-vs-Sensor test. Cloak lowers the maneuvering icon's Evasion TN; Lock-On lowers "
                "the opposing icon's Sensor TN -- read from whichever side (PC or enemy) carries them; "
                "IC carry neither.",
    },
]

# The dual mechanics whose STATE application is still direction-divergent. Fixing a
# mechanic means routing both directions through one resolver, flipping
# shared_application to True, and removing it here. When this set is empty every
# dual mechanic is modelled once.
KNOWN_ASYMMETRIES: set[str] = set()

# Per RAW, DINAB is an option offered by exactly these programs (Attack, Hog,
# Poison, Restrict, Reveal, Slow, Steamroller, Medic, Restore).
RAW_DINAB_CAPABLE: set[str] = {
    "attack", "hog", "poison", "restrict", "reveal",
    "slow", "steamroller", "medic", "restore",
}


def test_dual_mechanic_primitives_exist():
    """Each dual mechanic resolves dice through a real shared engine primitive."""
    for m in DUAL_MECHANICS:
        module, name = m["primitive"]
        assert _has(module, name), f"dual mechanic '{m['name']}' primitive {name} is missing"


def test_known_asymmetries_registry_is_accurate():
    """KNOWN_ASYMMETRIES must exactly equal the mechanics flagged not-yet-shared.

    Adding an asymmetric mechanic, or fixing one, forces an update here -- the
    scoreboard can never silently drift from the code's actual state.
    """
    flagged = {m["name"] for m in DUAL_MECHANICS if not m["shared_application"]}
    assert KNOWN_ASYMMETRIES == flagged, (
        f"undocumented asymmetry: {flagged - KNOWN_ASYMMETRIES}; "
        f"stale (now-shared?) entries: {KNOWN_ASYMMETRIES - flagged}"
    )


def test_code_dinab_set_matches_raw():
    """The router's DINAB routing tuples cover exactly the RAW DINAB-capable programs."""
    code_dinab = set(mr._DINAB_OFFENSIVE) | set(mr._DINAB_SELF_TARGETED) | set(mr._DINAB_ANTI_IC)
    assert code_dinab == RAW_DINAB_CAPABLE, (
        f"missing from code: {RAW_DINAB_CAPABLE - code_dinab}; "
        f"extra in code: {code_dinab - RAW_DINAB_CAPABLE}"
    )


# ------------------------------------------------------------------ dual-mechanic parity
# Hog is unified: a PC can carry it, and both directions resolve through one seam. These are
# hard asserts (promoted from the former xfail burn-down). attack / crippler remain tracked
# in KNOWN_ASYMMETRIES to be generalized through the same seam as each is next touched.

def test_every_dinab_program_is_a_carriable_pc_utility():
    """A program a PC can DINAB must be a program a PC can actually load."""
    assert RAW_DINAB_CAPABLE <= UTILITIES, (
        f"DINAB-capable but not carriable by a PC: {RAW_DINAB_CAPABLE - UTILITIES}"
    )


def test_hog_is_modelled_once_for_both_sides():
    """Hog must apply its viral state through one shared resolver, not per-direction."""
    assert "hog" not in KNOWN_ASYMMETRIES


def test_hog_applies_identically_in_both_directions(monkeypatch):
    """Behavioral parity: fire Hog enemy->PC and PC->enemy through the shared resolver with a
    forced hit, and assert both seed a structurally identical persistent infection and that one
    per-turn loop re-drains BOTH sides -- the property the unification exists to guarantee."""
    forced_hit = {
        "attack_roll": {"successes": 3, "ones": 0, "pool": 5},
        "resist_roll": {"successes": 0},
        "net": 4, "reduction": 2,
    }
    monkeypatch.setattr(mr.eng, "hog_attack", lambda **kw: dict(forced_hit))

    enemy = {"id": "e1", "name": "ICE", "status": "active", "mpcp": 4, "hardening": 0,
             "utilities": {"attack": 5, "sleaze": 4}}
    decker = {"name": "PC", "mpcp": 6, "hardening": 0, "utilities": {"attack": 6, "analyze": 5}}
    state = {"enemy_deckers": [enemy], "event_log": [], "program_damage": {}}

    r_enemy_to_pc = mr._resolve_hog(state, mr._hog_target_for_pc(state, decker),
                                    attacker_id="e1", attacker_pool=8, hog_rating=5, sec_code="Red")
    r_pc_to_enemy = mr._resolve_hog(state, mr._hog_target_for_enemy(state, enemy),
                                    attacker_id="pc", attacker_pool=8, hog_rating=6, sec_code="Red")

    # Both directions infect, with the same record shape.
    assert r_enemy_to_pc["infected"] and r_pc_to_enemy["infected"]
    infections = state["hog_infections"]
    assert len(infections) == 2
    required = {"id", "attacker_id", "target_id", "rating", "drain"}
    assert all(required <= set(i) for i in infections)
    assert {i["target_id"] for i in infections} == {"pc", "e1"}

    # First drain applied immediately, symmetrically (reduction 2 off each side's top program).
    assert sum(state["program_damage"].values()) == 2      # PC ledger took 2
    assert sum(enemy["utilities"].values()) == 9 - 2       # enemy utilities lost 2

    # ONE per-turn loop re-drains BOTH sides in a single pass.
    mr._drain_all_hog_infections(state, decker)
    assert sum(state["program_damage"].values()) == 4
    assert sum(enemy["utilities"].values()) == 9 - 4

    # An infection whose target is gone lapses on the next pass.
    enemy["status"] = "crashed"
    mr._drain_all_hog_infections(state, decker)
    assert {i["target_id"] for i in state["hog_infections"]} == {"pc"}
