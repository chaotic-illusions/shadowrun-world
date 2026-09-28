"""Run-summary parser: the request it sends, and what survives the server-side checks."""
import asyncio
import json
from contextlib import asynccontextmanager
from types import SimpleNamespace

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.models.location import Location
from app.models.organization import Organization
from app.models.reputation import OrgStanding, Reputation
from app.routers.adventure_logs import _parse_world_context
from app.services import narrative_parser
from app.services.narrative_parser import check_result


SUMMARY = (
    "Cascade and Razor hit the Ares warehouse in Redmond for Mr. Johnson. "
    "A Lone Star patrol filmed Razor's face on the way out."
)
CONTEXT = {
    "participants": [{"id": 2, "name": "Cascade"}, {"id": 5, "name": "Razor"}],
    "organizations": [{"id": 3, "name": "Ares Macrotechnology"}, {"id": 11, "name": "Lone Star Security"}],
    "locations": [{"id": 25, "name": "The Barrens (Seattle)"}],
}


def _change(**kw):
    base = {"type": "heat", "character_id": 5, "delta": 2, "org_id": None, "reason": "Filmed.",
            "evidence": "filmed Razor's face"}
    return {**base, **kw}


def _record(**kw):
    base = {
        "title": "Warehouse", "objective": "Hit it", "result": "Done", "outcome": "partial_success",
        "employer": "Mr. Johnson", "outcome_tags": ["witnesses"], "consequence_tags": [],
        "location_ids": [], "org_ids": [], "proposed_changes": [], "questions": [],
    }
    return {**base, **kw}


def test_changes_for_non_runners_and_unknown_ids_are_dropped():
    result = check_result(_record(proposed_changes=[
        _change(),
        _change(character_id=99),                                    # not on the run
        _change(type="org_standing", org_id=4242, delta=-3),         # org not in context
        _change(type="street_cred", delta=0),                        # no change
    ]), CONTEXT, SUMMARY)

    assert [(c["type"], c["character_id"]) for c in result["proposed_changes"]] == [("heat", 5)]
    assert len(result["dropped"]) == 3


def test_names_come_from_the_world_context_not_the_model():
    result = check_result(_record(proposed_changes=[
        _change(type="org_standing", org_id=3, delta=-3, character_name="Somebody Else"),
    ]), CONTEXT, SUMMARY)

    change = result["proposed_changes"][0]
    assert change["character_name"] == "Razor"
    assert change["org_name"] == "Ares Macrotechnology"


def test_evidence_is_checked_against_the_summary():
    result = check_result(_record(proposed_changes=[
        _change(evidence="A Lone Star patrol  filmed Razor’s face"),
        _change(character_id=2, evidence="Cascade blew up the building"),
    ]), CONTEXT, SUMMARY)

    assert [c["evidence_found"] for c in result["proposed_changes"]] == [True, False]


def test_ids_are_filtered_and_both_tag_sets_are_stored_together():
    result = check_result(_record(
        location_ids=[25, 777], org_ids=[3, 11, 888],
        outcome_tags=["witnesses", "not_a_tag"], consequence_tags=["pc_identity_exposed", "made_up"],
    ), CONTEXT, SUMMARY)

    assert result["location_ids"] == [25]
    assert result["org_ids"] == [3, 11]
    assert result["outcome_tags"] == ["witnesses", "pc_identity_exposed"]
    assert "consequence_tags" not in result


class _FakeMessages:
    def __init__(self, calls, reply, stop_reason="end_turn"):
        self.calls, self.reply, self.stop_reason = calls, reply, stop_reason

    async def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            stop_reason=self.stop_reason,
            content=[SimpleNamespace(type="thinking", thinking=""),
                     SimpleNamespace(type="text", text=json.dumps(self.reply))],
        )


def _fake_client(monkeypatch, reply, stop_reason="end_turn"):
    calls = []
    messages = _FakeMessages(calls, reply, stop_reason)
    client = SimpleNamespace(messages=messages, beta=SimpleNamespace(messages=messages))
    monkeypatch.setattr(narrative_parser.anthropic, "AsyncAnthropic", lambda **_: client)
    monkeypatch.setattr(narrative_parser, "get_api_key", lambda: "test-key")
    monkeypatch.delenv("CLAUDE_MODEL", raising=False)
    return calls


def test_request_uses_structured_output_and_refusal_fallbacks(monkeypatch):
    calls = _fake_client(monkeypatch, _record(proposed_changes=[_change()]))

    result = asyncio.run(narrative_parser.parse_narrative(SUMMARY, CONTEXT))

    request = calls[0]
    assert request["model"] == "claude-opus-5"
    assert request["thinking"] == {"type": "adaptive"}
    assert request["output_config"]["format"]["schema"] is narrative_parser.RECORD_SCHEMA
    assert request["fallbacks"] == "default"
    assert "GM RUN SUMMARY" in request["messages"][0]["content"]
    assert result["proposed_changes"][0]["character_name"] == "Razor"


def test_a_refusal_is_reported_instead_of_parsed(monkeypatch):
    _fake_client(monkeypatch, {}, stop_reason="refusal")

    with pytest.raises(RuntimeError, match="declined"):
        asyncio.run(narrative_parser.parse_narrative(SUMMARY, CONTEXT))


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}")
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


def test_world_context_holds_runners_active_and_named_entities_only(tmp_path):
    async def scenario():
        async with _database(tmp_path / "ctx.db") as sessions:
            async with sessions() as db:
                runner = Character(name="Razor", is_pc=True)
                bystander_pc = Character(name="Cascade", is_pc=True)
                named_npc = Character(name="Kyle Morgan", is_pc=False, is_active=False)
                other_npc = Character(name="Josie Wells", is_pc=False)
                active_org = Organization(name="Lone Star Security", org_type="security contractor", is_active=True)
                named_org = Organization(name="Ares Macrotechnology", org_type="megacorp", is_active=False)
                quiet_org = Organization(name="Saeder-Krupp", org_type="megacorp", is_active=False)
                named_loc = Location(name="Redmond Warehouse", is_active=False)
                quiet_loc = Location(name="Club Penumbra", is_active=False)
                db.add_all([runner, bystander_pc, named_npc, other_npc, active_org, named_org,
                            quiet_org, named_loc, quiet_loc])
                await db.commit()
                db.add_all([
                    Reputation(character_id=runner.id, street_cred=3, heat=2),
                    OrgStanding(character_id=runner.id, organization_id=quiet_org.id, standing=-2),
                ])
                await db.commit()
                ids = dict(runner=runner.id, cascade=bystander_pc.id, named_org=named_org.id,
                           quiet_org=quiet_org.id, active_org=active_org.id, named_loc=named_loc.id)
            async with sessions() as db:
                ctx = await _parse_world_context(
                    db, "Razor hit the Redmond Warehouse for Ares Macrotechnology; Kyle Morgan watched.",
                    [ids["runner"]],
                )
                with pytest.raises(HTTPException):
                    await _parse_world_context(db, "anything", [])
            return ctx, ids

    ctx, ids = asyncio.run(scenario())
    assert [p["name"] for p in ctx["participants"]] == ["Razor"]
    assert ctx["participants"][0]["heat"] == 2
    assert ctx["participants"][0]["standings"][0]["org_id"] == ids["quiet_org"]
    # active + named + already-standing orgs; nothing else
    assert {o["id"] for o in ctx["organizations"]} == {ids["active_org"], ids["named_org"], ids["quiet_org"]}
    assert [loc["id"] for loc in ctx["locations"]] == [ids["named_loc"]]
    assert [p["name"] for p in ctx["people"]] == ["Kyle Morgan"]
