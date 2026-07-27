"""Tests for the auth core module."""
import asyncio
from datetime import UTC, datetime

import pytest
from app.auth.core import hash_token, generate_token
from app.models.auth import UserToken
from app.models.character import Character
from app.models.matrix_run import MatrixRun
from app.routers import auth as auth_router
from app.routers import matrix_runs


class TestHashToken:
    def test_deterministic(self):
        assert hash_token("test") == hash_token("test")

    def test_different_inputs(self):
        assert hash_token("a") != hash_token("b")

    def test_returns_hex_string(self):
        h = hash_token("test")
        assert len(h) == 64  # SHA-256 hex = 64 chars
        assert all(c in "0123456789abcdef" for c in h)


class TestGenerateToken:
    def test_default_length(self):
        t = generate_token()
        assert len(t) == 48  # 24 bytes = 48 hex chars

    def test_custom_length(self):
        t = generate_token(16)
        assert len(t) == 32  # 16 bytes = 32 hex chars

    def test_unique(self):
        tokens = {generate_token() for _ in range(100)}
        assert len(tokens) == 100  # all unique


class TestTokenRegeneration:
    def test_migrates_character_and_matrix_run_ownership(self, monkeypatch):
        old_token = "old-token"
        new_token = "new-token"
        old_hash = hash_token(old_token)
        token = UserToken(
            id=1, token_hash=old_hash, label="Runner", is_admin=False,
            created_at=datetime.now(UTC),
        )
        character = Character(id=7, name="Static", is_pc=True, owner_token=old_hash)
        active_run = MatrixRun(id=10, owner_token_hash=old_hash, status="active")
        ended_run = MatrixRun(id=11, owner_token_hash=old_hash, status="crashed")

        class _Scalars:
            def __init__(self, rows):
                self.rows = rows

            def first(self):
                return self.rows[0] if self.rows else None

            def all(self):
                return self.rows

        class _Result:
            def __init__(self, rows):
                self.rows = rows

            def scalars(self):
                return _Scalars(self.rows)

        class _DB:
            def __init__(self):
                self.results = iter([
                    _Result([token]),
                    _Result([character]),
                    _Result([active_run, ended_run]),
                ])
                self.commits = 0

            async def execute(self, _query):
                return next(self.results)

            async def commit(self):
                self.commits += 1

            async def refresh(self, _obj):
                pass

        db = _DB()
        monkeypatch.setattr(auth_router, "generate_token", lambda _n: new_token)

        asyncio.run(auth_router.regenerate_token(token_id=1, db=db, _="admin"))

        new_hash = hash_token(new_token)
        assert token.token_hash == new_hash
        assert character.owner_token == new_hash
        assert active_run.owner_token_hash == new_hash
        assert ended_run.owner_token_hash == new_hash
        assert db.commits == 1
        matrix_runs._assert_run_access(
            active_run,
            {"is_admin": False, "is_user": True, "user_token": new_token},
        )
