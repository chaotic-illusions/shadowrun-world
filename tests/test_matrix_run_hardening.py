from __future__ import annotations

import asyncio
from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from pydantic import ValidationError

from app.auth.core import hash_token
from app.routers import matrix_runs as mr
from app.schemas.matrix_run import (
    MatrixRunCreate,
    RunActionInput,
    RunTrapDoorInput,
    SheafGenerateInput,
    SheaveSaveInput,
)
from app.services import matrix_engine as eng


class _Host:
    def __init__(self, host_id: int, name: str):
        self.id = host_id
        self.name = name
        self.is_visible_to_players = True
        self.config_json = {"security_code": "Green", "security_value": 6}
        self.ltg_address = None
        self.trap_doors_json = []


class _DB:
    def __init__(self, character=None):
        self.character = character

    async def get(self, model, object_id):
        return self.character if self.character and self.character.id == object_id else None

    async def commit(self):
        return None

    async def refresh(self, obj):
        return None


def _decker() -> dict:
    return {
        "character_id": 7,
        "name": "Spoofed",
        "computer_skill": 1,
        "intelligence": 1,
        "quickness": 1,
        "willpower": 1,
        "body": 1,
        "mpcp": 6,
        "bod": 6,
        "evasion": 6,
        "masking": 6,
        "sensor": 6,
        "utilities": {},
    }


def test_player_decker_uses_owned_active_pc_identity_and_attributes():
    character = SimpleNamespace(
        id=7,
        name="Cipher",
        is_pc=True,
        is_active=True,
        owner_token=hash_token("player-token"),
        computer_skill_rating=8,
        intelligence=7,
        quickness=6,
        willpower=5,
        body=4,
    )
    result = asyncio.run(mr._authoritative_player_decker(
        _DB(character), {"user_token": "player-token"}, _decker()
    ))
    assert result["character_id"] == 7
    assert result["name"] == "Cipher"
    assert result["computer_skill"] == 8
    assert (result["intelligence"], result["quickness"], result["willpower"], result["body"]) == (7, 6, 5, 4)
    assert result["mpcp"] == 6


def test_admin_start_run_preserves_ad_hoc_decker(monkeypatch):
    captured = {}

    async def _host(db, host_id):
        return _Host(host_id, "Host")

    async def _gate(db, auth, decker):
        captured["gate"] = decker

    async def _create(db, auth, host, decker):
        captured["create"] = decker
        return SimpleNamespace(state_json={})

    monkeypatch.setattr(mr, "_get_host_or_404", _host)
    monkeypatch.setattr(mr, "_assert_no_unacknowledged_run", _gate)
    monkeypatch.setattr(mr, "_create_run", _create)
    monkeypatch.setattr(mr, "_serialize_run", lambda run, auth: run.state_json)
    body = MatrixRunCreate(host_id=1, decker=_decker())

    asyncio.run(mr.start_run(
        body=body,
        auth={"is_admin": True, "is_user": False, "user_token": None},
        db=_DB(),
    ))
    assert captured["gate"]["name"] == "Spoofed"
    assert captured["create"]["computer_skill"] == 1


@pytest.mark.parametrize("change", [
    {"character_id": None},
    {"owner_token": hash_token("someone-else")},
    {"is_pc": False},
    {"is_active": False},
])
def test_player_decker_rejects_missing_unowned_or_inactive_pc(change):
    character = SimpleNamespace(
        id=7,
        name="Cipher",
        is_pc=True,
        is_active=True,
        owner_token=hash_token("player-token"),
        computer_skill_rating=8,
        intelligence=7,
        quickness=6,
        willpower=5,
        body=4,
    )
    payload = _decker()
    if "character_id" in change:
        payload["character_id"] = change["character_id"]
    else:
        for key, value in change.items():
            setattr(character, key, value)
    with pytest.raises(HTTPException) as exc:
        asyncio.run(mr._authoritative_player_decker(
            _DB(character), {"user_token": "player-token"}, payload
        ))
    assert exc.value.status_code in (400, 404)


def test_pre_logon_guard_allows_only_logon_dispatch():
    with pytest.raises(HTTPException, match="Logon to Host"):
        mr._assert_logged_on({"logon_complete": False})
    mr._assert_logged_on({"logon_complete": True})


def test_event_log_retains_only_latest_750_entries():
    state = {"event_log": [], "current_turn": 1}

    for index in range(751):
        mr._append_event(state, {"type": "test", "index": index})

    assert len(state["event_log"]) == 750
    assert state["event_log"][0]["index"] == 1
    assert state["event_log"][-1]["index"] == 750


def test_generic_host_operation_is_blocked_before_logon(monkeypatch):
    run = SimpleNamespace(
        status="active",
        state_json={"logon_complete": False, "run_ended": False},
        decker_json=_decker(),
        owner_token_hash=None,
    )

    async def _run(db, run_id):
        return run

    monkeypatch.setattr(mr, "_get_run_or_404", _run)
    body = RunActionInput(action_type="analyze_host", subsystem="index")
    with pytest.raises(HTTPException, match="Logon to Host"):
        asyncio.run(mr.perform_action(
            run_id=1,
            body=body,
            auth={"is_admin": True, "is_user": False, "user_token": None},
            db=_DB(),
        ))


def test_host_stack_carries_deck_damage_and_only_pc_hog_infections():
    decker = _decker()
    source = _Host(1, "Source")
    destination = _Host(2, "Destination")
    state = mr._initial_state(decker, source)
    state.update({
        "program_damage": {"attack": 2},
        "dinab_damage": {"attack": 1},
        "one_shot_wiped": ["attack"],
        "hog_infections": [
            {"id": "pc-hog", "target_id": "pc", "rating": 6},
            {"id": "host-hog", "target_id": "enemy-1", "rating": 5},
        ],
    })

    deep = mr._push_host_stack(state, source, destination, decker)
    assert deep["program_damage"] == {"attack": 2}
    assert deep["dinab_damage"] == {"attack": 1}
    assert deep["one_shot_wiped"] == ["attack"]
    assert [item["id"] for item in deep["hog_infections"]] == ["pc-hog"]

    deep["hog_infections"].append({"id": "deep-host", "target_id": "enemy-2", "rating": 4})
    resumed, _ = mr._pop_host_stack(deep)
    assert {item["id"] for item in resumed["hog_infections"]} == {"pc-hog", "host-hog"}


def test_trap_destination_starts_with_fresh_full_action_budget():
    decker = _decker()
    state = mr._initial_state(decker, _Host(1, "Source"))
    state["pass_action_points"] = 0
    state["pass_free"] = 0
    destination = mr._push_host_stack(state, _Host(1, "Source"), _Host(2, "Destination"), decker)
    assert destination["pass_action_points"] == 2
    assert destination["pass_free"] == 1


def _trap_run() -> SimpleNamespace:
    state = mr._initial_state(_decker(), _Host(1, "Source"))
    state.update({
        "logon_complete": True,
        "pending_defense": {"ic_id": "killer"},
        "trap_doors": [{
            "id": "door-1",
            "discovered": True,
            "destination_host_id": 2,
        }],
    })
    return SimpleNamespace(
        id=1,
        host_id=1,
        status="active",
        state_json=state,
        decker_json=_decker(),
        owner_token_hash=None,
    )


def test_failed_trap_transit_resolves_defense_then_spends_complex_action(monkeypatch):
    run = _trap_run()
    order = []

    async def _run(db, run_id):
        return run

    async def _host(db, host_id):
        return _Host(host_id, "Source" if host_id == 1 else "Destination")

    def _force(state, decker, current_run):
        order.append("defense")
        state["pending_defense"] = None
        return False

    def _logoff(state, decker, **kwargs):
        order.append("logoff")
        assert state["pass_action_points"] == 0
        return False

    monkeypatch.setattr(mr, "_get_run_or_404", _run)
    monkeypatch.setattr(mr, "_get_host_or_404", _host)
    monkeypatch.setattr(mr, "_force_resolve_pending_defense", _force)
    monkeypatch.setattr(mr, "_apply_graceful_logoff", _logoff)
    monkeypatch.setattr(mr, "_serialize_run", lambda current_run, auth: current_run.state_json)

    result = asyncio.run(mr.trap_door_action(
        run_id=1,
        td_id="door-1",
        body=RunTrapDoorInput(action="enter"),
        auth={"is_admin": True, "is_user": False, "user_token": None},
        db=_DB(),
    ))
    assert order == ["defense", "logoff"]
    assert result["pass_action_points"] == 0
    assert run.host_id == 1


def test_successful_trap_transit_arrives_with_full_fresh_actions(monkeypatch):
    run = _trap_run()

    async def _run(db, run_id):
        return run

    async def _host(db, host_id):
        return _Host(host_id, "Source" if host_id == 1 else "Destination")

    def _force(state, decker, current_run):
        state["pending_defense"] = None
        return False

    monkeypatch.setattr(mr, "_get_run_or_404", _run)
    monkeypatch.setattr(mr, "_get_host_or_404", _host)
    monkeypatch.setattr(mr, "_force_resolve_pending_defense", _force)
    monkeypatch.setattr(mr, "_apply_graceful_logoff", lambda *args, **kwargs: True)
    monkeypatch.setattr(mr, "_serialize_run", lambda current_run, auth: current_run.state_json)

    result = asyncio.run(mr.trap_door_action(
        run_id=1,
        td_id="door-1",
        body=RunTrapDoorInput(action="enter"),
        auth={"is_admin": True, "is_user": False, "user_token": None},
        db=_DB(),
    ))
    assert run.host_id == 2
    assert result["pass_action_points"] == 2
    assert result["pass_free"] == 1


@pytest.mark.parametrize("step_count", [0, 65])
def test_sheaf_generator_rejects_out_of_range_step_count(step_count):
    with pytest.raises(ValueError, match="between 1 and 64"):
        eng.generate_sheaf(security_code="Green", security_value=6, step_count=step_count)
    with pytest.raises(ValidationError):
        SheafGenerateInput(security_code="Green", security_value=6, step_count=step_count)


def test_saved_sheaf_rejects_more_than_64_steps():
    step = {"trigger": 1, "events": []}
    with pytest.raises(ValidationError):
        SheaveSaveInput(
            security_code="Green",
            security_value=6,
            sheaf=[step for _ in range(65)],
        )