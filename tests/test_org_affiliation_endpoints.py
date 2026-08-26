"""Org affiliation endpoints (affiliate/unaffiliate), enum validation, and contact-listing privacy.

Direct router-call style against a throwaway aiosqlite DB, same as
tests/test_org_affiliation_weighting.py -- no HTTP layer.
"""
import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from pydantic import ValidationError
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.db.base import Base
from app.models.character import Character
from app.models.contact import Contact
from app.models.organization import Organization
from app.models.reputation import OrgStanding
from app.routers.organizations import affiliate_runner, unaffiliate_runner
from app.schemas.organization import (
    AffiliateRunnerRequest, OrganizationCreate, OrganizationUpdate,
)


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


def test_affiliation_type_enum_validation():
    assert OrganizationCreate(name="X").affiliation_contact_type is None
    assert OrganizationCreate(name="X", affiliation_contact_type="Gang").affiliation_contact_type == "Gang"
    assert OrganizationUpdate(affiliation_contact_type="Tribe").affiliation_contact_type == "Tribe"
    with pytest.raises(ValidationError):
        OrganizationCreate(name="X", affiliation_contact_type="Bogus")
    with pytest.raises(ValidationError):
        OrganizationUpdate(affiliation_contact_type="corp")


def test_affiliate_keeps_accumulated_standing_and_rejects_non_gang(tmp_path):
    async def scenario():
        async with _database(tmp_path / "aff_ep.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Runner", is_pc=True)
                gang = Organization(name="Ancients", org_type="gang", affiliation_contact_type="Gang")
                corp = Organization(name="Ares", org_type="megacorp")
                db.add_all([pc, gang, corp])
                await db.commit()
                pc_id, gang_id, corp_id = pc.id, gang.id, corp.id

            # Runner already accumulated +5 standing before being linked.
            async with sessions() as db:
                db.add(OrgStanding(character_id=pc_id, organization_id=gang_id, standing=5))
                await db.commit()

            async with sessions() as db:
                await affiliate_runner(gang_id, AffiliateRunnerRequest(character_id=pc_id), db=db, _="admin")
            async with sessions() as db:
                ct = (await db.execute(select(Contact).where(
                    Contact.owner_id == pc_id, Contact.organization_id == gang_id
                ))).scalars().first()
                assert ct is not None and ct.npc_id is None and ct.contact_type == "Gang" and ct.name == "Ancients"
                s = (await db.execute(select(OrgStanding).where(
                    OrgStanding.character_id == pc_id, OrgStanding.organization_id == gang_id
                ))).scalars().first()
                assert s.standing == 5  # affiliate must NOT reset accumulated standing

            # A non-gang/tribe org cannot be affiliated.
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await affiliate_runner(corp_id, AffiliateRunnerRequest(character_id=pc_id), db=db, _="admin")
                assert exc.value.status_code == 400

    asyncio.run(scenario())


def test_affiliate_promotes_chargen_contact_without_duplicating(tmp_path):
    async def scenario():
        async with _database(tmp_path / "aff_promote.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Runner", is_pc=True)
                gang = Organization(name="Ancients", org_type="gang", affiliation_contact_type="Gang")
                db.add_all([pc, gang])
                await db.commit()
                pc_id, gang_id = pc.id, gang.id
                # Loose chargen gang contact: npc_id null, matching name, no org yet.
                db.add(Contact(owner_id=pc_id, name="Ancients", contact_type="Gang"))
                await db.commit()

            async with sessions() as db:
                await affiliate_runner(gang_id, AffiliateRunnerRequest(character_id=pc_id), db=db, _="admin")
            async with sessions() as db:
                contacts = (await db.execute(select(Contact).where(Contact.owner_id == pc_id))).scalars().all()
                assert len(contacts) == 1  # promoted the existing contact, not duplicated
                assert contacts[0].organization_id == gang_id and contacts[0].contact_type == "Gang"

    asyncio.run(scenario())


def test_unaffiliate_removes_contact_but_keeps_standing(tmp_path):
    async def scenario():
        async with _database(tmp_path / "unaff.db") as sessions:
            async with sessions() as db:
                pc = Character(name="Runner", is_pc=True)
                gang = Organization(name="Ancients", org_type="gang", affiliation_contact_type="Gang")
                db.add_all([pc, gang])
                await db.commit()
                pc_id, gang_id = pc.id, gang.id
            async with sessions() as db:
                await affiliate_runner(gang_id, AffiliateRunnerRequest(character_id=pc_id), db=db, _="admin")
            async with sessions() as db:
                s = (await db.execute(select(OrgStanding).where(
                    OrgStanding.character_id == pc_id, OrgStanding.organization_id == gang_id
                ))).scalars().first()
                s.standing = 7
                await db.commit()

            async with sessions() as db:
                await unaffiliate_runner(gang_id, pc_id, db=db, _="admin")
            async with sessions() as db:
                assert await db.scalar(select(func.count()).select_from(Contact).where(
                    Contact.owner_id == pc_id, Contact.organization_id == gang_id
                )) == 0
                s = (await db.execute(select(OrgStanding).where(
                    OrgStanding.character_id == pc_id, OrgStanding.organization_id == gang_id
                ))).scalars().first()
                assert s is not None and s.standing == 7  # standing survives losing membership

    asyncio.run(scenario())
