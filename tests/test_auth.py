"""Tests for the auth core module."""
import pytest
from app.auth.core import hash_token, generate_token


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
