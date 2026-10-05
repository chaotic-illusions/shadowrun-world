"""Karma awards (SR2 p.190), Karma Pool donations to Team Karma (p.191), and the GM-only Karma Pool."""

import asyncio
from contextlib import asynccontextmanager

import pytest
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.auth.core import hash_token
from app.db.base import Base
from app.models.campaign import CampaignState
from app.models.character import Character
from app.routers.characters import award_karma, donate_karma, update_character
from app.schemas.character import CharacterUpdate, KarmaAward, KarmaDonation

# Same throwaway-DB pattern as tests/test_character_permissions.py -- calls the real router
# functions directly.
RUNNER = {"is_admin": False, "is_user": True, "user_token": "runner-token", "view_as_player": False}
OTHER = {"is_admin": False, "is_user": True, "user_token": "other-token", "view_as_player": False}
GM = {"is_admin": True, "is_user": True, "user_token": "admin-token", "view_as_player": False}


@asynccontextmanager
async def _database(path):
    engine = create_async_engine(f"sqlite+aiosqlite:///{path.as_posix()}", connect_args={"timeout": 5})
    sessions = async_sessionmaker(engine, expire_on_commit=False)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    try:
        yield sessions
    finally:
        await engine.dispose()


async def _runner(sessions, **fields):
    async with sessions() as db:
        char = Character(name="Leadbelly", is_pc=True, owner_token=hash_token("runner-token"), **fields)
        db.add(char)
        await db.commit()
        return char.id


async def _team_karma(sessions):
    async with sessions() as db:
        state = await db.get(CampaignState, 1)
        return state.team_karma if state else None


def test_award_splits_one_in_ten_to_the_pool_against_the_running_total(tmp_path):
    async def scenario():
        async with _database(tmp_path / "award.db") as sessions:
            char_id = await _runner(sessions, karma_pool=2, good_karma=0)
            steps = []
            for amount in (3, 3, 3, 3, 10, 1):
                async with sessions() as db:
                    r = await award_karma(char_id, KarmaAward(karma=amount), db, RUNNER)
                    steps.append((r["good_karma"], r["karma_pool"]))
            # 3,6,9 earned: no Pool point yet; 12 crosses 10; 22 crosses 20; 23 doesn't.
            assert steps == [(3, 2), (6, 2), (9, 2), (11, 3), (20, 4), (21, 4)]

    asyncio.run(scenario())


def test_taking_back_an_award_takes_back_its_pool_share(tmp_path):
    async def scenario():
        async with _database(tmp_path / "takeback.db") as sessions:
            char_id = await _runner(sessions, karma_pool=2, good_karma=0)
            async with sessions() as db:
                r = await award_karma(char_id, KarmaAward(karma=10), db, RUNNER)
                assert (r["good_karma"], r["karma_pool"]) == (9, 3)
            async with sessions() as db:
                r = await award_karma(char_id, KarmaAward(karma=-5), db, RUNNER)
                # Net award of 5: below the 10 mark, so the Pool point goes back.
                assert (r["good_karma"], r["karma_pool"]) == (5, 2)
            async with sessions() as db:
                assert (await db.get(Character, char_id)).karma_earned == 5

    asyncio.run(scenario())


def test_take_back_is_limited_to_unspent_awarded_karma(tmp_path):
    async def scenario():
        async with _database(tmp_path / "takeback_limit.db") as sessions:
            char_id = await _runner(sessions, karma_pool=1, good_karma=0)
            async with sessions() as db:
                await award_karma(char_id, KarmaAward(karma=4), db, RUNNER)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:   # more than was ever awarded
                    await award_karma(char_id, KarmaAward(karma=-5), db, RUNNER)
                assert exc.value.status_code == 422
            async with sessions() as db:   # spent on a skill: a plain PATCH, count untouched
                await update_character(char_id, CharacterUpdate(good_karma=1), db, RUNNER)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await award_karma(char_id, KarmaAward(karma=-2), db, RUNNER)
                assert exc.value.status_code == 422
            async with sessions() as db:
                char = await db.get(Character, char_id)
                assert (char.good_karma, char.karma_earned) == (1, 4)

    asyncio.run(scenario())


def test_take_back_never_drops_the_pool_below_zero(tmp_path):
    async def scenario():
        async with _database(tmp_path / "takeback_donated.db") as sessions:
            char_id = await _runner(sessions, karma_pool=0, good_karma=0)
            async with sessions() as db:
                await award_karma(char_id, KarmaAward(karma=10), db, RUNNER)   # Pool 1
            async with sessions() as db:
                await donate_karma(char_id, KarmaDonation(points=1), db, RUNNER)  # Pool 0
            async with sessions() as db:
                r = await award_karma(char_id, KarmaAward(karma=-1), db, RUNNER)
                assert (r["good_karma"], r["karma_pool"]) == (9, 0)

    asyncio.run(scenario())


def test_award_of_zero_is_refused():
    with pytest.raises(ValueError):
        KarmaAward(karma=0)


def test_award_is_owner_or_admin_only(tmp_path):
    async def scenario():
        async with _database(tmp_path / "award_auth.db") as sessions:
            char_id = await _runner(sessions)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await award_karma(char_id, KarmaAward(karma=10), db, OTHER)
                assert exc.value.status_code == 403
            async with sessions() as db:
                r = await award_karma(char_id, KarmaAward(karma=10), db, GM)
                assert (r["good_karma"], r["karma_pool"]) == (9, 2)

    asyncio.run(scenario())


def test_donation_moves_pool_points_to_team_karma(tmp_path):
    async def scenario():
        async with _database(tmp_path / "donate.db") as sessions:
            char_id = await _runner(sessions, karma_pool=3)
            async with sessions() as db:
                r = await donate_karma(char_id, KarmaDonation(points=2), db, RUNNER)
                assert r["karma_pool"] == 1
            assert await _team_karma(sessions) == 4  # new team's 2 + the donation

    asyncio.run(scenario())


def test_donation_cannot_exceed_the_pool(tmp_path):
    async def scenario():
        async with _database(tmp_path / "donate_over.db") as sessions:
            char_id = await _runner(sessions, karma_pool=1)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await donate_karma(char_id, KarmaDonation(points=2), db, RUNNER)
                assert exc.value.status_code == 422
            async with sessions() as db:
                assert (await db.get(Character, char_id)).karma_pool == 1
            assert await _team_karma(sessions) == 2

    asyncio.run(scenario())


def test_donation_needs_at_least_one_point():
    with pytest.raises(ValueError):
        KarmaDonation(points=0)


def test_only_a_gm_sets_karma_pool_directly(tmp_path):
    async def scenario():
        async with _database(tmp_path / "pool_patch.db") as sessions:
            char_id = await _runner(sessions, karma_pool=1)
            async with sessions() as db:
                with pytest.raises(HTTPException) as exc:
                    await update_character(char_id, CharacterUpdate(karma_pool=9), db, RUNNER)
                assert exc.value.status_code == 403
            async with sessions() as db:
                r = await update_character(char_id, CharacterUpdate(karma_pool=4), db, GM)
                assert r["karma_pool"] == 4

    asyncio.run(scenario())
