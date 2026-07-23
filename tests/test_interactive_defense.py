"""Interactive per-attack Hacking-Pool defense (the NPC phase pause + POST /defend).

The interactive-defense flow lets a decker spend Hacking Pool dice on an IC's cybercombat hit
BEFORE it resolves: perform_action -> _advance_npc_pass (with allow_defense_pause) rolls the IC
to-hit, and if it lands while state['interactive_defense'] is on it PARKS the strike in
state['pending_defense'] and returns. POST /defend then spends the chosen dice into the icon's Bod
resistance, resolves the SAME strike (reusing the parked to-hit -- no re-roll), and resumes the pass.

These tests cover the new surface only; RNG-identity of the extracted resolver is already guaranteed
by the wider suite (the feature is dormant unless interactive_defense is set, which no other test
sets). Rolls are made deterministic by monkeypatching app.services.matrix_engine.roll_dice.
"""
from __future__ import annotations

import asyncio
import datetime

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import RunDefendInput

_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
_PLAYER = {"is_admin": False, "is_user": True, "user_token": "player"}


class _RunStub:
    """Carries exactly the attributes MatrixRunRead.model_validate / _serialize_run read."""

    def __init__(self, decker: dict, state: dict):
        now = datetime.datetime.now(datetime.timezone.utc)
        self.id = 1
        self.host_id = 1
        self.status = "active"
        self.owner_token_hash = None
        self.decker_json = decker
        self.state_json = state
        self.created_at = now
        self.updated_at = now
        self.version = 1


class _FakeDB:
    async def commit(self):
        return None

    async def refresh(self, obj):
        return None

    async def execute(self, *a, **k):
        class _Empty:
            def scalars(self):
                return self

            def first(self):
                return None

            def all(self):
                return []
        return _Empty()


def _pc_decker(deck_mode="cool"):
    # No Shield / Armor utility, so the resolve path rolls exactly ONE pool -- the icon Bod resist --
    # which the tests intercept to prove Hacking Pool dice are added to it.
    return {
        "name": "Def Ghost",
        "bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6,
        "intelligence": 6, "quickness": 6, "willpower": 4, "body": 5,
        "computer_skill": 6, "hardening": 0, "deck_mode": deck_mode,
        "utilities": {"attack": 6},
    }


def _pc_state(sec="Green", sv=6, *, interactive=True, hp=6):
    return {
        "host_security_code": sec, "host_security_value": sv,
        "host_security_revealed": False,
        "detection_factor": 4, "decker_initiative": 10,
        "current_pass": 1, "security_tally": 0, "traces_completed": 0,
        "npc_combat_maneuvers": False,
        "logon_complete": True,
        "active_ic": [], "enemy_deckers": [], "event_log": [],
        "condition_monitor": {
            "persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0, "mpcp_damage": 0,
            "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0},
        },
        "program_damage": {},
        "interactive_defense": interactive,
        "pending_defense": None,
        "hackingPool_remaining": hp,
        "hackingPool_total": hp,
    }


def _killer(ic_id="k1", rating=6):
    return {"id": ic_id, "type": "Killer", "rating": rating,
            "status": "active", "initiative": 10, "boxes": 0}


def _to_hit(successes=3):
    return {"pool": 6, "tn": 4, "dice": [6, 5, 5, 3, 2, 1][:6], "successes": successes, "ones": 1}


# -- _defense_offer_wanted -----------------------------------------------------

def test_defense_offer_wanted_gates():
    base = {"interactive_defense": True, "hackingPool_remaining": 3, "pending_defense": None}
    assert mr._defense_offer_wanted(base, {"successes": 1}) is True
    # each precondition, individually, turns the offer off
    assert mr._defense_offer_wanted({**base, "interactive_defense": False}, {"successes": 1}) is False
    assert mr._defense_offer_wanted(base, {"successes": 0}) is False
    assert mr._defense_offer_wanted({**base, "hackingPool_remaining": 0}, {"successes": 1}) is False
    assert mr._defense_offer_wanted({**base, "pending_defense": {"ic_id": "x"}}, {"successes": 1}) is False


# -- _park_pending_defense -----------------------------------------------------

def test_park_pending_defense_shape():
    state = _pc_state()
    th = _to_hit(3)
    mr._park_pending_defense(
        state, _pc_decker(), _killer(), to_hit=th,
        ic_attack_pool=9, ic_target_status="intruding", atk_power_delta=0, atk_tn_delta=0,
        cluster_penalty=0, ic_category="white", sec_code="Green", sec_value=6,
        logon_completed=True,
    )
    pend = state["pending_defense"]
    assert pend is not None
    assert pend["ic_id"] == "k1"
    assert pend["attack_successes"] == 3
    assert pend["to_hit_roll"] == th
    assert pend["hp_available"] == 6
    assert pend["resume_logon_completed"] is True
    assert pend["ctx"]["ic_attack_pool"] == 9
    assert pend["ctx"]["sec_value"] == 6
    assert pend["ctx"]["ic_category"] == "white"
    assert any(e.get("type") == "defense_pending" for e in state["event_log"])


# -- _advance_npc_pass: parks (interactive) vs resolves inline (default) --------

def test_advance_npc_pass_parks_when_interactive(monkeypatch):
    # Force the to-hit to land. Park returns BEFORE any resistance roll, so a single landing result
    # is all that is consumed.
    monkeypatch.setattr(eng, "roll_dice",
                        lambda pool, tn=4: {"pool": pool, "tn": tn, "dice": [6, 6],
                                            "successes": 2, "ones": 0})
    state = _pc_state(interactive=True)
    state["active_ic"] = [_killer()]
    decker = _pc_decker()
    eff = mr._get_decker_effective(decker, state)
    mr._advance_npc_pass(state, decker, _RunStub(decker, state), eff=eff,
                         sec_code="Green", sec_value=6, det_factor=4, allow_defense_pause=True)
    # Paused: prompt set, and NOT a single box of damage applied yet (the strike is deferred).
    assert state["pending_defense"] is not None
    assert state["pending_defense"]["ic_id"] == "k1"
    assert state["condition_monitor"]["persona_boxes"] == 0
    assert not state.get("run_ended")


def test_advance_npc_pass_no_park_when_disabled(monkeypatch):
    # Same landing to-hit, but interactive_defense OFF -> the strike resolves inline (no pause).
    # First roll_dice = to-hit (lands, 2 successes); second = resistance (0 successes -> full hit).
    calls = {"n": 0}

    def _rd(pool, tn=4):
        calls["n"] += 1
        succ = 2 if calls["n"] == 1 else 0
        return {"pool": pool, "tn": tn, "dice": [], "successes": succ, "ones": 0}

    monkeypatch.setattr(eng, "roll_dice", _rd)
    state = _pc_state(interactive=False)
    state["active_ic"] = [_killer()]
    decker = _pc_decker()
    eff = mr._get_decker_effective(decker, state)
    mr._advance_npc_pass(state, decker, _RunStub(decker, state), eff=eff,
                         sec_code="Green", sec_value=6, det_factor=4, allow_defense_pause=True)
    assert state["pending_defense"] is None                                        # never paused
    assert any(e.get("type") == "ic_attack" for e in state["event_log"])           # resolved inline


# -- POST /defend --------------------------------------------------------------

def _pending_for(state, ic, th, *, sec_value=6):
    return {
        "ic_id": ic["id"],
        "attacker_label": f"{ic['type']}-{ic['rating']}",
        "attack_successes": th["successes"],
        "to_hit_roll": th,
        "power": ic["rating"],
        "hp_available": state["hackingPool_remaining"],
        "resume_logon_completed": False,
        "ctx": {
            "ic_attack_pool": sec_value, "ic_target_status": "intruding",
            "atk_power_delta": 0, "atk_tn_delta": 0, "cluster_penalty": 0,
            "ic_category": "white", "sec_code": state["host_security_code"], "sec_value": sec_value,
        },
    }


def _run_defend(monkeypatch, hp_spend):
    """Drive POST /defend against a pre-parked Killer strike, recording every resistance dice pool
    eng.roll_dice is asked to roll. Returns (run, recorded_pools)."""
    recorded: list[int] = []

    def _rd(pool, tn=4):
        recorded.append(pool)
        return {"pool": pool, "tn": tn, "dice": [], "successes": 0, "ones": 0}

    monkeypatch.setattr(eng, "roll_dice", _rd)

    decker = _pc_decker()
    state = _pc_state(interactive=True, hp=6)
    ic = _killer()
    ic["acted_pass"] = 1                      # already acted this pass -> resume skips it
    state["active_ic"] = [ic]
    state["pending_defense"] = _pending_for(state, ic, _to_hit(3))
    run = _RunStub(decker, state)

    async def _get(db, run_id):
        return run

    monkeypatch.setattr(mr, "_get_run_or_404", _get)
    asyncio.run(mr.defend(run_id=1, body=RunDefendInput(hacking_pool_dice=hp_spend),
                          auth=_ADMIN, db=_FakeDB()))
    return run, recorded


def test_defend_adds_hacking_pool_to_resistance(monkeypatch):
    run, pools = _run_defend(monkeypatch, 4)
    state = run.state_json
    assert 10 in pools                                    # icon Bod 6 + 4 Hacking Pool dice
    assert state["pending_defense"] is None               # prompt cleared
    assert state["hackingPool_remaining"] == 2            # 6 - 4 spent
    assert any(e.get("type") == "ic_attack" for e in state["event_log"])   # strike resolved


def test_defend_zero_hp_resists_with_bod_alone(monkeypatch):
    run, pools = _run_defend(monkeypatch, 0)
    state = run.state_json
    assert pools == [6]                                   # Bod alone, no Hacking Pool added
    assert state["hackingPool_remaining"] == 6            # nothing spent
    assert state["pending_defense"] is None


def test_defend_rejects_hp_over_remaining(monkeypatch):
    # Request more Hacking Pool dice than remain -> 400 (block, don't clamp), matching every other
    # spendable-resource path in the app. _spend_hp raises before the strike resolves.
    with pytest.raises(HTTPException) as ei:
        _run_defend(monkeypatch, 40)
    assert ei.value.status_code == 400


def test_defend_without_pending_400(monkeypatch):
    decker = _pc_decker()
    state = _pc_state(interactive=True)
    state["pending_defense"] = None
    run = _RunStub(decker, state)

    async def _get(db, run_id):
        return run

    monkeypatch.setattr(mr, "_get_run_or_404", _get)
    with pytest.raises(HTTPException) as ei:
        asyncio.run(mr.defend(run_id=1, body=RunDefendInput(hacking_pool_dice=1),
                              auth=_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400


# -- GM redaction of the pending prompt ----------------------------------------

def test_pending_defense_ctx_redacted_for_player():
    """The prompt is player-visible, but its internal ctx (host Security code/value) must be
    stripped server-side, and an UNANALYZED attacker's identity (type/rating) must be masked so it
    cannot leak through the prompt before an Analyze IC (M1)."""
    decker = _pc_decker()
    state = _pc_state(interactive=True)
    state["host_security_revealed"] = False
    ic = _killer()
    state["active_ic"] = [ic]
    state["pending_defense"] = _pending_for(state, ic, _to_hit(3))

    view = mr._serialize_run(_RunStub(decker, state), _PLAYER)
    pstate = view["state_json"]
    # host Security Rating stays hidden...
    assert "host_security_value" not in pstate
    # ...the pending prompt's internal ctx is stripped...
    pend = pstate["pending_defense"]
    assert "ctx" not in pend
    assert "resume_logon_completed" not in pend
    # ...and an unidentified IC's identity is masked: label -> "Unknown IC", raw to-hit roll gone.
    assert pend["attacker_label"] == "Unknown IC"
    assert "to_hit_roll" not in pend
    # The incoming force (successes + Power) is still shown so the player can size their defense.
    assert pend["attack_successes"] == 3
    assert pend["power"] == 6

    # Once the IC is identified (Analyze IC -> analyzed), the real label + roll are disclosed.
    ic["analyzed"] = True
    pend2 = mr._serialize_run(_RunStub(decker, state), _PLAYER)["state_json"]["pending_defense"]
    assert pend2["attacker_label"] == "Killer-6"
    assert "to_hit_roll" in pend2

    # An admin (GM) always sees the full ctx.
    gm = mr._serialize_run(_RunStub(decker, state), _ADMIN)
    assert gm["state_json"]["pending_defense"]["ctx"]["sec_value"] == 6


# -- Force-resolve a parked strike when the decker ends the run (logoff / jack out) -------------

def test_force_resolve_pending_defense_resolves_parked_strike(monkeypatch):
    """A parked IC strike must still resolve (Bod-only, no Hacking Pool) when the decker bails --
    you cannot dodge a landed hit's consequences by logging off / jacking out."""
    def _rd(pool, tn=4):
        return {"pool": pool, "tn": tn, "dice": [], "successes": 0, "ones": 0}  # decker resists 0
    monkeypatch.setattr(eng, "roll_dice", _rd)

    decker = _pc_decker()
    state = _pc_state(interactive=True)
    ic = _killer()
    ic["acted_pass"] = 1
    state["active_ic"] = [ic]
    state["pending_defense"] = _pending_for(state, ic, _to_hit(3))
    run = _RunStub(decker, state)

    ended = mr._force_resolve_pending_defense(state, decker, run)

    assert state["pending_defense"] is None                                   # prompt consumed
    assert any(e.get("type") == "ic_attack" for e in state["event_log"])      # strike resolved
    assert state["condition_monitor"]["persona_boxes"] > 0                    # the hit landed
    assert isinstance(ended, bool)


def test_jack_out_resolves_parked_strike_first(monkeypatch):
    """Jacking out while a defense is pending resolves the parked strike first (the L1 wiring),
    then completes the jack-out -- the decker does not escape the landed hit."""
    def _rd(pool, tn=4):
        return {"pool": pool, "tn": tn, "dice": [], "successes": 0, "ones": 0}
    monkeypatch.setattr(eng, "roll_dice", _rd)
    monkeypatch.setattr(mr, "_apply_dump_shock",
                        lambda *a, **k: {"final_level": "None", "boxes": 0})
    monkeypatch.setattr(mr, "_finalize_run_end", lambda state: None)

    decker = _pc_decker()
    state = _pc_state(interactive=True)
    ic = _killer()
    ic["acted_pass"] = 1
    state["active_ic"] = [ic]
    state["pending_defense"] = _pending_for(state, ic, _to_hit(3))
    run = _RunStub(decker, state)

    async def _get(db, run_id):
        return run
    monkeypatch.setattr(mr, "_get_run_or_404", _get)

    asyncio.run(mr.jack_out(run_id=1, auth=_ADMIN, db=_FakeDB()))

    # The parked strike was resolved before jack-out completed: prompt gone, hit logged, run ended.
    assert run.state_json["pending_defense"] is None
    assert any(e.get("type") == "ic_attack" for e in run.state_json["event_log"])
    assert run.state_json.get("run_ended") is True
