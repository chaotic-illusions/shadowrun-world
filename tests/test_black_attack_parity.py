"""Black-family attack -- actor parity (Layer 2).

Proves the "same mechanic, same math, whoever fires it" guarantee for the Black family: every
Black-family strike -- enemy Black IC (lethal + non-lethal), an enemy decker's Black Hammer /
Killjoy, and the PC's own Black Hammer / Killjoy -- resolves through the SINGLE engine core
``eng.black_attack``. The core is direction-agnostic (it takes no "who is attacking" flag, so it
cannot branch on the actor); the deliberate, RAW-cited differences between actors live ONLY in the
rider ARGUMENTS the router hands the core:

  * base_damage_level -- the Black IC CONSTRUCT follows the host Security-Code table
    (``IC_DAMAGE_LEVEL[sec]``); the Black Hammer / Killjoy PROGRAMS use a fixed "Serious"
    (``_LETHAL_BASE_LEVEL``) regardless of host code. (The construct-vs-program split.)
  * meat_pool -- a PC target's flesh IS simulated, so the strike carries a second (meat) resistance
    test: Body->Physical for Black Hammer / lethal Black IC, Willpower->Stun for Killjoy /
    non-lethal Black IC. An enemy NPC's flesh is NOT simulated, so PC->enemy passes
    ``meat_pool=None`` -- an icon-only hit.
  * hardening -- the DEFENDER's Hardening reduces both resist Powers, whoever the defender is
    (the decker's Hardening vs an inbound black attack; the enemy's Hardening vs the PC's).

vr2_rules.md: Black IC ~L615-647 (lethal Body->Physical + Bod->icon; non-lethal Willpower->Stun +
Bod->icon; damage level by host Security Code); Black Hammer ~L1533 and Killjoy ~L1551 ("function
like black IC but from a decker"; Body AND Bod resist; Hardening reduces the resist TN).

Layer 1 (test_black_attack_oracle.py) pins the core's numbers; this file pins that all three call
sites feed that one core the correct rider arguments -- so no actor can silently drift onto a
different resolution.
"""
from __future__ import annotations

import asyncio
import random

import pytest

from app.services import matrix_engine as eng
from app.services import matrix_rules as rules
from app.routers import matrix_runs as mr
from app.schemas.matrix_run import RunEnemyAttackInput

# Reuse the sanctioned maximal-run harness (stable test infrastructure).
from tests.test_scenario_fuzz import _fresh_run, _FakeDB, _ADMIN


# -- Deterministic dice helper (mirrors the oracle's _ScriptedRandom) -----------

class _ScriptedRandom:
    def __init__(self, values):
        self._v = list(values)
        self._i = 0

    def randint(self, a, b):
        v = self._v[self._i % len(self._v)]
        self._i += 1
        return max(a, min(b, v))

    def choice(self, seq):
        return seq[0]

    def random(self):
        return 0.5

    def seed(self, *a, **k):
        pass

    def getstate(self):
        return None

    def setstate(self, s):
        pass


@pytest.fixture
def scripted(monkeypatch):
    def _install(values):
        monkeypatch.setattr(eng, "random", _ScriptedRandom(values))
    return _install


class _RunStub:
    status = "active"


# =============================================================================
# Layer 2a -- the engine core is direction-agnostic
# =============================================================================

@pytest.mark.parametrize("seq", [
    [4, 4, 4, 5, 5, 2, 2, 2, 2, 2, 2],
    [6, 3, 4, 1, 5, 6, 1, 1, 2, 3, 4],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
])
def test_engine_result_depends_only_on_numeric_inputs(scripted, seq):
    """Given identical numeric inputs and identical dice, ``black_attack`` returns the SAME result
    every time -- it carries no actor flag, so the caller's identity cannot change a number. This
    is what lets one core serve Black IC, enemy Black Hammer/Killjoy and PC Black Hammer/Killjoy."""
    kw = dict(attacker_pool=6, security_code="Green", target_status="intruding",
              base_damage_level="Serious", power=6, hardening=1, icon_bod=6, icon_armor=0,
              meat_pool=5)
    scripted(seq)
    first = eng.black_attack(**kw)
    scripted(seq)
    second = eng.black_attack(**kw)
    assert first == second


def test_meat_is_stun_flag_changes_only_the_label_not_the_math(scripted):
    """The Stun/Physical distinction (Killjoy / non-lethal Black IC -> Stun; Black Hammer / lethal
    Black IC -> Physical) is a routing label the caller carries -- it must NOT perturb the icon or
    meat damage the core computes from identical dice."""
    seq = [5, 5, 5, 4, 4, 2, 3, 1, 2, 6, 1]
    base = dict(attacker_pool=6, security_code="Green", target_status="intruding",
                base_damage_level="Serious", power=6, hardening=0, icon_bod=6, meat_pool=5)
    scripted(seq)
    phys = eng.black_attack(**base, meat_is_stun=False)
    scripted(seq)
    stun = eng.black_attack(**base, meat_is_stun=True)
    assert phys["icon"]["boxes"] == stun["icon"]["boxes"]
    assert phys["meat"]["boxes"] == stun["meat"]["boxes"]
    assert phys["meat_is_stun"] is False and stun["meat_is_stun"] is True


# =============================================================================
# Layer 2b -- every router call site feeds the core the correct rider args
# =============================================================================

def _canned(**kw):
    """A non-crashing ``black_attack`` result in the real shape (icon + meat, 1 box each so no
    crash / kill branch fires), echoing back the caller's base and stun-flag riders."""
    def _resist(pool):
        return {"effective_power": 5, "attacker_successes": 1, "shield_successes": 0,
                "staged_up_level": "Serious",
                "resist_roll": {"successes": 0, "ones": 0, "dice": [1], "tn": 5, "pool": pool},
                "final_damage_level": "Light", "boxes": 1}
    return {
        "attack_roll": {"successes": 1, "ones": 0, "dice": [4], "tn": 3, "pool": 6},
        "attack_tn": 3,
        "base_damage_level": kw.get("base_damage_level", "Serious"),
        "icon": _resist(6),
        "meat": _resist(4),
        "meat_is_stun": kw.get("meat_is_stun", False),
    }


def _capture(monkeypatch):
    """Patch the shared core to record the kwargs its caller hands it (returning a canned result so
    the caller completes) and return the dict the assertions read."""
    captured: dict = {}

    def _spy(**kw):
        captured.clear()
        captured.update(kw)
        return _canned(**kw)

    monkeypatch.setattr(eng, "black_attack", _spy)
    return captured


# -- Shared minimal PC-side fixtures (for the two NPC->PC directions) -----------

def _pc_state(sec="Green", sv=6):
    return {
        "host_security_code": sec, "host_security_value": sv,
        "current_pass": 1, "security_tally": 0,
        "active_ic": [], "enemy_deckers": [], "event_log": [],
        "condition_monitor": {"persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0,
                              "mpcp_damage": 0,
                              "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}},
        "program_damage": {},
    }


def _pc_decker(deck_mode="hot"):
    # body (5) != willpower (4) so the meat_pool assertion distinguishes Physical from Stun;
    # hardening 2 (nonzero) so the hardening rider is a real value, not a coincidental 0.
    return {"bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6, "intelligence": 5,
            "body": 5, "willpower": 4, "hardening": 2, "deck_mode": deck_mode,
            "computer_skill": 6, "utilities": {"armor": 0}}


# -- Site 1: enemy Black IC -> PC (mr._advance_npc_pass) -------------------------

def _drive_black_ic_vs_pc(monkeypatch, deck_mode, sec="Green"):
    captured = _capture(monkeypatch)
    monkeypatch.setattr(mr, "random", random.Random(13))
    state = _pc_state(sec=sec)
    state["active_ic"] = [{"id": "bic1", "type": "Black IC", "rating": 6,
                           "status": "active", "initiative": 10, "boxes": 0}]
    decker = _pc_decker(deck_mode=deck_mode)
    eff = mr._get_decker_effective(decker, state)
    mr._advance_npc_pass(state, decker, _RunStub(), eff=eff,
                         sec_code=state["host_security_code"],
                         sec_value=state["host_security_value"], det_factor=4)
    return captured, decker, eff


@pytest.mark.parametrize("deck_mode, is_stun, meat_attr", [
    ("hot", False, "body"),        # lethal Black IC   -> Body -> Physical
    ("cool", True, "willpower"),   # non-lethal Black IC -> Willpower -> Stun
])
def test_black_ic_vs_pc_uses_host_table_base_with_meat(monkeypatch, deck_mode, is_stun, meat_attr):
    """Black IC (the CONSTRUCT) bases its damage on the host Security-Code table and always drives a
    meat resistance test (biofeedback): hot deck -> Body/Physical, cool deck -> Willpower/Stun. The
    defender's Hardening reduces the resist Power; the icon resists with the decker's effective
    Bod."""
    captured, decker, eff = _drive_black_ic_vs_pc(monkeypatch, deck_mode, sec="Green")
    assert captured["base_damage_level"] == rules.IC_DAMAGE_LEVEL["Green"]   # host table, not fixed
    assert captured["meat_pool"] is not None                                # flesh IS simulated
    assert captured["meat_pool"] == decker[meat_attr]
    assert captured["meat_is_stun"] is is_stun
    assert captured["hardening"] == decker["hardening"]
    assert captured["icon_bod"] == eff["bod"]


def test_tortoise_deck_is_immune_to_black_ic(monkeypatch):
    """A tortoise deck has no ASIST/simsense link, so Black IC cannot reach the operator AS Black IC:
    it resolves as ordinary icon-only attack IC. black_attack (the biofeedback core) is never called,
    the meat condition monitors stay clean, and the jack-out gate (black_ic_engaged) is never armed."""
    monkeypatch.setattr(mr, "random", random.Random(13))

    def _boom(**kw):
        raise AssertionError("black_attack must not run for a tortoise deck")

    monkeypatch.setattr(eng, "black_attack", _boom)
    state = _pc_state(sec="Green")
    state["active_ic"] = [{"id": "bic1", "type": "Black IC", "rating": 6,
                           "status": "active", "initiative": 10, "boxes": 0}]
    decker = _pc_decker(deck_mode="tortoise")
    eff = mr._get_decker_effective(decker, state)
    mr._advance_npc_pass(state, decker, _RunStub(), eff=eff,
                         sec_code=state["host_security_code"],
                         sec_value=state["host_security_value"], det_factor=4)
    assert state["condition_monitor"]["physical_boxes"] == 0   # no lethal biofeedback
    assert state["condition_monitor"]["stun_boxes"] == 0       # no non-lethal biofeedback
    assert not state.get("black_ic_engaged")                   # no jack-out gate armed


# -- Site 2: enemy decker Black Hammer / Killjoy -> PC (mr._enemy_decker_take_turn) --

def _black_enemy(program, *, hardening=0):
    return {
        "id": "ed1", "name": "Red Security Decker", "tier": "Red",
        "mpcp": 9, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
        "computer_skill": 8, "intelligence": 6, "quickness": 6, "response_increase": 1,
        "deck_mode": "cool", "reality_filter": False,
        "utilities": {"attack": 6, "sleaze": 5, "scanner": 5},
        "programs": ["Attack"], "intent": "kill",
        "lethal_program": program, "lethal_rating": 6, "hardening": hardening, "bravery": 0,
        "detection_factor": 4, "located": True, "revealed": True, "status": "active",
        "condition_monitor": {"persona_boxes": 0, "stun_boxes": 0, "physical_boxes": 0,
                              "mpcp_damage": 0},
        "program_damage": {}, "nerve_checks_done": [], "locate_progress": 99,
    }


@pytest.mark.parametrize("program, is_stun, meat_attr", [
    ("Black Hammer", False, "body"),      # PROGRAM -> fixed Serious, Body -> Physical
    ("Killjoy", True, "willpower"),       # PROGRAM -> fixed Serious, Willpower -> Stun
])
def test_enemy_decker_vs_pc_uses_fixed_serious_with_meat(monkeypatch, program, is_stun, meat_attr):
    """The enemy decker's Black Hammer / Killjoy PROGRAM uses a fixed "Serious" base (NOT the host
    table) and drives the meat test exactly like Black IC -- Killjoy Stun, Black Hammer Physical.
    Hardening rider = the DECKER'S Hardening; the icon resists with the decker's effective Bod."""
    monkeypatch.setattr(mr, "random", random.Random(7))
    monkeypatch.setattr(eng, "random", random.Random(7))
    captured = _capture(monkeypatch)
    state = _pc_state(sec="Green")
    decker = _pc_decker()
    enemy = _black_enemy(program)
    mr._enemy_decker_take_turn(state, decker, _RunStub(), enemy)
    eff = mr._get_decker_effective(decker, state)
    assert captured["base_damage_level"] == mr._LETHAL_BASE_LEVEL        # fixed "Serious"
    assert captured["base_damage_level"] == "Serious"
    assert captured["meat_pool"] is not None
    assert captured["meat_pool"] == decker[meat_attr]
    assert captured["meat_is_stun"] is is_stun
    assert captured["hardening"] == decker["hardening"]
    assert captured["icon_bod"] == eff["bod"]


# -- Site 3: PC Black Hammer / Killjoy -> enemy decker (mr.attack_enemy_decker) --

def _boot_pc_vs_enemy(monkeypatch, program):
    rng = random.Random(20260706)
    monkeypatch.setattr(mr, "random", rng)
    monkeypatch.setattr(eng, "random", rng)
    run = _fresh_run()
    state = run.state_json
    run.decker_json["utilities"][program] = 5   # carry the black program
    enemy = next(e for e in state["enemy_deckers"]
                 if e.get("revealed") and e.get("status") == "active")

    async def _get(db, run_id, _r=run):
        return _r
    monkeypatch.setattr(mr, "_get_run_or_404", _get)
    return run, enemy


@pytest.mark.parametrize("program", ["black_hammer", "killjoy"])
def test_pc_vs_enemy_black_program_is_icon_only_serious(monkeypatch, program):
    """The PC's Black Hammer / Killjoy vs an enemy decker uses the SAME fixed "Serious" base and now
    ALSO simulates the NPC's flesh (``meat_pool`` set) so the strike can KO/kill the operator, not
    just crash the icon: Killjoy -> Willpower (Stun), Black Hammer -> Body (Physical). Hardening
    rider = the ENEMY'S Hardening; the icon resists with the enemy's Bod."""
    captured = _capture(monkeypatch)
    run, enemy = _boot_pc_vs_enemy(monkeypatch, program)
    asyncio.run(mr.attack_enemy_decker(
        run_id=1,
        body=RunEnemyAttackInput(enemy_id=enemy["id"], attack_pool=8,
                                 hacking_pool_dice=0, program=program),
        auth=_ADMIN, db=_FakeDB()))
    assert captured["base_damage_level"] == "Serious"
    if program == "killjoy":
        assert captured["meat_pool"] == int(enemy.get("willpower") or enemy.get("intelligence") or 4)
        assert captured["meat_is_stun"] is True
    else:
        assert captured["meat_pool"] == int(enemy.get("body") or enemy.get("bod") or 4)
        assert captured["meat_is_stun"] is False
    assert captured["hardening"] == int(enemy.get("hardening", 0) or 0)
    assert captured["icon_bod"] == max(1, int(enemy.get("bod", 1) or 1))
    assert captured["target_status"] == "legitimate"                     # enemy = legitimate resident


# =============================================================================
# Cross-site -- the ONE deliberate asymmetry: construct table vs program fixed
# =============================================================================

def test_construct_uses_host_table_but_program_uses_fixed_serious(monkeypatch):
    """On the SAME non-Red/Black host (Green -> IC_DAMAGE_LEVEL "Moderate"), the Black IC CONSTRUCT
    bases its damage on the host Security-Code table while the Black Hammer / Killjoy PROGRAMS use a
    fixed "Serious". This pins the single intentional actor asymmetry -- everything else about the
    black strike is shared."""
    construct, _d, _e = _drive_black_ic_vs_pc(monkeypatch, "hot", sec="Green")
    construct_base = construct["base_damage_level"]

    monkeypatch.setattr(mr, "random", random.Random(7))
    monkeypatch.setattr(eng, "random", random.Random(7))
    program_cap = _capture(monkeypatch)
    state = _pc_state(sec="Green")
    mr._enemy_decker_take_turn(state, _pc_decker(), _RunStub(), _black_enemy("Black Hammer"))
    program_base = program_cap["base_damage_level"]

    assert construct_base == rules.IC_DAMAGE_LEVEL["Green"] == "Moderate"
    assert program_base == "Serious"
    assert construct_base != program_base
