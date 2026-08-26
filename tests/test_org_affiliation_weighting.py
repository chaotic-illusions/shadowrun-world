"""Org-affiliation 2x rep weighting (apply-changes org_standing path).

Direct router-call style against a throwaway aiosqlite DB, same as
tests/test_character_lifestyle_flow.py -- no HTTP layer.
"""
import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.models.organization import Organization
from app.models.reputation import OrgStanding
from app.routers.adventure_logs import ApplyChangesRequest, apply_world_changes


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(
        f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5}
    )
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.exec_driver_sql("PRAGMA journal_mode=WAL")
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


async def _standing(sessions, pc_id, org_id):
    async with sessions() as db:
        return await db.scalar(
            select(OrgStanding).where(
                OrgStanding.character_id == pc_id, OrgStanding.organization_id == org_id
            )
        )


def _org_standing_change(pc_id, org_id, delta):
    return ApplyChangesRequest(
        changes=[{"type": "org_standing", "character_id": pc_id, "delta": delta, "org_id": org_id}]
    )


def test_org_standing_delta_doubles_only_for_affiliated_runner(tmp_path):
    async def scenario():
        async with _database(tmp_path / "aff.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Runner", is_pc=True)
                gang = Organization(name="Ancients", org_type="gang", affiliation_contact_type="Gang")
                corp = Organization(name="Ares", org_type="megacorp")
                npc = Character(name="Fixer", is_pc=False)
                db.add_all([pc, gang, corp, npc])
                await db.commit()
                pc_id, gang_id, corp_id, npc_id = pc.id, gang.id, corp.id, npc.id

            # No affiliation contact yet: +2 applies as +2.
            async with sessions() as db:
                await apply_world_changes(_org_standing_change(pc_id, gang_id, 2), db=db, _="admin")
            assert (await _standing(sessions, pc_id, gang_id)).standing == 2

            # Gang/tribe contact (npc_id NULL) = affiliated: +2 now applies as +4 (2x).
            async with sessions() as db:
                db.add(Contact(owner_id=pc_id, organization_id=gang_id, name="Ancients", contact_type="Gang"))
                await db.commit()
            async with sessions() as db:
                await apply_world_changes(_org_standing_change(pc_id, gang_id, 2), db=db, _="admin")
            assert (await _standing(sessions, pc_id, gang_id)).standing == 6  # 2 + 2*2

            # A person-contact (npc_id SET) who merely works for an org must NOT trigger the 2x.
            async with sessions() as db:
                db.add(Contact(owner_id=pc_id, organization_id=corp_id, npc_id=npc_id, name="Fixer"))
                await db.commit()
            async with sessions() as db:
                await apply_world_changes(_org_standing_change(pc_id, corp_id, 3), db=db, _="admin")
            assert (await _standing(sessions, pc_id, corp_id)).standing == 3  # not doubled

    asyncio.run(scenario())
