"""Scramble IC + Data Bomb overhaul (2026-07-28) -- run-layer mechanics.

Covers the behaviours added in the Scramble/Data-bomb pass:
  * Exploding Scramble linked bombs for the Files datastore (files::entire) and the Access
    subsystem (access::entire / access::piece) -- vr2 L491.
  * A Poison Scramble reacting to EACH cybercombat attack against it (hit or miss) -- vr2 L493.
  * The Access-subsystem bomb trigger (graceful logoff / trap-door transit / validate passcode).
  * Analyze Icon revealing a file Scramble's variant.
  * Crash-a-Scramble in cybercombat: crashing ADDS the rating to the tally (vr2 L495), an Exploding
    Scramble detonates its linked bomb on the crash, and a Poison Scramble erases on the way down.
"""
from __future__ import annotations

import asyncio

from app.services import matrix_engine as eng
from app.routers import matrix_runs as mr
from app.schemas.matrix_run import RunScrambleAttackInput


# -- Linked-bomb creation ------------------------------------------------------

def test_link_exploding_bombs_files_entire_and_access():
    state = {"scrambles": [
        {"target_key": "files::entire", "rating": 6, "variant": "exploding"},
        {"target_key": "access::entire", "rating": 5, "variant": "exploding"},
        {"target_key": "access::piece::LTG", "rating": 4, "variant": "exploding"},
    ], "data_bombs": []}
    mr._link_exploding_scramble_bombs(state)
    by_target = {b["target"]: b for b in state["data_bombs"]}
    assert set(by_target) == {"files::__entire__", "access::__all__", "access::LTG"}
    # Each sentinel bomb records its linkage back to the scramble that spawned it.
    assert by_target["files::__entire__"]["linked_scramble"] == "files::entire"
    assert by_target["access::__all__"]["linked_scramble"] == "access::entire"
    assert by_target["access::LTG"]["linked_scramble"] == "access::piece::LTG"


def test_link_exploding_skips_poison_and_reuses_existing_bomb():
    state = {
        "scrambles": [
            {"target_key": "files::file::A", "rating": 6, "variant": "exploding"},
            {"target_key": "files::file::B", "rating": 6, "variant": "poison"},
        ],
        "data_bombs": [{"target": "files::A", "rating": 9}],   # designer-authored bomb on A
        "paydata": [{"id": "A", "name": "A"}, {"id": "B", "name": "B"}],
    }
    mr._link_exploding_scramble_bombs(state)
    # A's existing bomb serves as the linked bomb (not duplicated); B is Poison -> no bomb.
    assert [b["target"] for b in state["data_bombs"]] == ["files::A"]
    assert state["data_bombs"][0]["rating"] == 9


# -- Protected-file scoping ----------------------------------------------------

def test_scramble_protected_files_scopes():
    state = {"paydata": [
        {"id": "a", "name": "A"},
        {"id": "b", "name": "B", "destroyed": True},
        {"id": "c", "name": "C"},
    ]}
    entire = mr._scramble_protected_files(state, {"target_key": "files::entire"})
    assert {f["id"] for f in entire} == {"a", "c"}   # excludes an already-destroyed file
    one = mr._scramble_protected_files(state, {"target_key": "files::file::a"})
    assert [f["id"] for f in one] == ["a"]
    assert mr._scramble_protected_files(state, {"target_key": "access::entire"}) == []


# -- Poison reaction -----------------------------------------------------------

def test_scramble_poison_react_wipes_all_on_entire_success(monkeypatch):
    monkeypatch.setattr(
        eng, "scramble_failure_consequence",
        lambda **kw: {"data_destroyed": True, "key_data_lost": False, "message": ""})
    state = {"paydata": [{"id": "a", "name": "A"}, {"id": "b", "name": "B"}], "event_log": []}
    destroyed = mr._scramble_poison_react(
        state, {"computer_skill": 6},
        {"target_key": "files::entire", "rating": 6, "variant": "poison"})
    assert destroyed is True
    assert all(f.get("destroyed") for f in state["paydata"])
    assert any(e["type"] == "scramble_poison" and e["data_destroyed"] for e in state["event_log"])


def test_scramble_poison_react_survives_on_miss(monkeypatch):
    monkeypatch.setattr(
        eng, "scramble_failure_consequence",
        lambda **kw: {"data_destroyed": False, "key_data_lost": False, "message": ""})
    state = {"paydata": [{"id": "a", "name": "A"}], "event_log": []}
    destroyed = mr._scramble_poison_react(
        state, {"computer_skill": 6},
        {"target_key": "files::file::a", "rating": 6, "variant": "poison"})
    assert destroyed is False
    assert not state["paydata"][0].get("destroyed")


# -- Access-subsystem bomb trigger ---------------------------------------------

def test_trigger_access_subsystem_bomb(monkeypatch):
    fired = []
    monkeypatch.setattr(mr, "_detonate_data_bomb",
                        lambda *a, **k: fired.append(k.get("headline")) or {})
    monkeypatch.setattr(mr, "_get_decker_effective", lambda d, s: {"bod": 6})

    armed = {"data_bombs": [{"target": "access::__all__", "rating": 6}],
             "host_security_value": 6, "host_security_code": "Green"}
    assert mr._trigger_access_subsystem_bomb(armed, {}, op_label="graceful logoff") is True
    assert armed["data_bombs"] == [] and len(fired) == 1

    # A DEFUSED access bomb does not go off.
    defused = {"data_bombs": [{"target": "access::__all__", "rating": 6}],
               "defused_bombs": ["access::__all__"],
               "host_security_value": 6, "host_security_code": "Green"}
    assert mr._trigger_access_subsystem_bomb(defused, {}, op_label="validate passcode") is False
    assert len(defused["data_bombs"]) == 1

    # A Files bomb is NOT an access trigger.
    files_only = {"data_bombs": [{"target": "files::__entire__", "rating": 6}],
                  "host_security_value": 6, "host_security_code": "Green"}
    assert mr._trigger_access_subsystem_bomb(files_only, {}, op_label="graceful logoff") is False
    assert len(fired) == 1


# -- Analyze Icon variant reveal ----------------------------------------------

def test_analyze_icon_reveals_file_scramble_variant():
    state = {
        "scrambles": [{"target_key": "files::file::A", "rating": 6, "variant": "exploding"}],
        "paydata": [{"id": "A", "name": "A", "located": True}],
        "data_bombs": [], "event_log": [],
    }
    mr._apply_analyze_icon(state, target_file="files::A")
    scr = state["scrambles"][0]
    assert scr.get("discovered") and scr.get("variant_revealed")
    assert any(e["type"] == "scramble_analyzed" and e.get("variant") == "exploding"
               for e in state["event_log"])


# -- Crash a Scramble in cybercombat ------------------------------------------

class TestCrashScramble:
    def _decker(self):
        return {"name": "Static", "mpcp": 8, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6,
                "computer_skill": 6, "intelligence": 6, "utilities": {"attack": 8}}

    def _host(self):
        class _Host:
            config_json = {"security_code": "Green", "security_value": 6,
                           "acifs": [8, 9, 8, 10, 10]}
            ltg_address = None
            trap_doors_json = None
        return _Host()

    def _state(self, scrambles, data_bombs=None, paydata=None):
        st = mr._initial_state(self._decker(), self._host())
        st["logon_complete"] = True
        st["scrambles"] = scrambles
        if data_bombs is not None:
            st["data_bombs"] = data_bombs
        if paydata is not None:
            st["paydata"] = paydata
        st["pass_action_points"] = 4
        st["pass_free"] = 1
        st["hackingPool_remaining"] = 20
        st["hackingPool_total"] = 20
        return st

    class _FakeDB:
        async def commit(self):
            pass

        async def refresh(self, obj):
            pass

    def _crash(self, monkeypatch, state, ref, *, boxes):
        class _StubRun:
            id = 9
            host_id = 3
            status = "active"
            owner_token_hash = None
            decker_json = None
            state_json = None

        run = _StubRun()
        run.decker_json = self._decker()
        run.state_json = state

        async def _fake_get(db, run_id):
            return run

        def _fake_attack(**kw):
            return {
                "attack_roll": {"successes": 5, "ones": 0, "tn": 4, "dice": [5, 5, 5, 5, 5]},
                "resistance": {"resist_roll": {"successes": 0, "dice": []},
                               "final_damage_level": "Deadly", "boxes": boxes},
            }

        monkeypatch.setattr(mr, "_get_run_or_404", _fake_get)
        monkeypatch.setattr(mr, "_serialize_run", lambda r, a: r.state_json)
        monkeypatch.setattr(eng, "cybercombat_attack", _fake_attack)
        inp = RunScrambleAttackInput(scramble_ref=ref, hacking_pool_dice=0)
        auth = {"is_admin": True, "is_user": False, "user_token": None}
        asyncio.run(mr.crash_scramble(run_id=9, body=inp, auth=auth, db=self._FakeDB()))
        return run.state_json

    def test_crashing_scramble_adds_rating_to_tally(self, monkeypatch):
        state = self._state(
            [{"target_key": "files::file::A", "rating": 6, "variant": "poison", "discovered": True}],
            paydata=[{"id": "A", "name": "A"}])
        out = self._crash(monkeypatch, state, "scramble_1", boxes=10)
        assert out["security_tally"] >= 6                    # vr2 L495: crash adds the rating
        assert not out["scrambles"]                          # the crashed scramble is removed
        assert any(e["type"] == "scramble_crashed" for e in out["event_log"])

    def test_crashing_exploding_scramble_detonates_linked_bomb(self, monkeypatch):
        detonations = []
        monkeypatch.setattr(mr, "_detonate_data_bomb",
                            lambda *a, **k: detonations.append(k.get("headline")) or {})
        state = self._state(
            [{"target_key": "files::file::A", "rating": 6, "variant": "exploding", "discovered": True}],
            data_bombs=[{"target": "files::A", "rating": 6, "linked_scramble": "files::file::A"}],
            paydata=[{"id": "A", "name": "A"}])
        out = self._crash(monkeypatch, state, "scramble_1", boxes=10)
        assert detonations                                   # linked bomb went off on the crash
        assert not out["data_bombs"]                         # the linked bomb was consumed

    def test_poison_scramble_reacts_on_a_non_crashing_attack(self, monkeypatch):
        monkeypatch.setattr(
            eng, "scramble_failure_consequence",
            lambda **kw: {"data_destroyed": True, "key_data_lost": False, "message": ""})
        state = self._state(
            [{"target_key": "files::entire", "rating": 6, "variant": "poison", "discovered": True}],
            paydata=[{"id": "A", "name": "A"}, {"id": "B", "name": "B"}])
        out = self._crash(monkeypatch, state, "scramble_1", boxes=3)   # partial hit, no crash
        assert out["scrambles"]                              # still present (not crashed)
        assert any(e["type"] == "scramble_poison" and e["data_destroyed"] for e in out["event_log"])
        assert all(f.get("destroyed") for f in out["paydata"])   # files::entire poison wipes ALL
