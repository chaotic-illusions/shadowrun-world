"""Tests for the auth rate limiter."""
import time
import pytest
from unittest.mock import MagicMock
from fastapi import HTTPException

from app.auth.rate_limit import (
    record_failure, record_success, _attempts, _client_ip,
    BASE_DELAY, MAX_DELAY,
    enforce_call_rate, _calls, _throttle_key, CALL_LIMIT, CALL_WINDOW,
)


def _mock_request(ip: str = "127.0.0.1") -> MagicMock:
    req = MagicMock()
    req.client.host = ip
    req.headers = {}
    return req


def _tok_request(token: str | None = None, ip: str = "127.0.0.1") -> MagicMock:
    req = MagicMock()
    req.client.host = ip
    req.headers = {"x-user-token": token} if token else {}
    return req


@pytest.fixture(autouse=True)
def clear_state():
    """Reset the rate limiter state between tests."""
    _attempts.clear()
    _calls.clear()
    yield
    _attempts.clear()
    _calls.clear()


class TestClientIp:
    def test_direct(self):
        req = _mock_request("10.0.0.1")
        assert _client_ip(req) == "10.0.0.1"

    def test_forwarded_for_ignored_by_default(self):
        # X-Forwarded-For is client-spoofable, so it must be ignored unless the app is
        # explicitly told it sits behind a trusted proxy (TRUST_PROXY_HEADERS).
        req = _mock_request("10.0.0.1")
        req.headers = {"x-forwarded-for": "203.0.113.5, 10.0.0.1"}
        assert _client_ip(req) == "10.0.0.1"

    def test_forwarded_for_used_when_proxy_trusted(self, monkeypatch):
        monkeypatch.setattr("app.auth.rate_limit._TRUST_PROXY", True)
        req = _mock_request("10.0.0.1")
        req.headers = {"x-forwarded-for": "203.0.113.5, 10.0.0.1"}
        assert _client_ip(req) == "203.0.113.5"

    def test_empty_forwarded_for_falls_back_when_trusted(self, monkeypatch):
        monkeypatch.setattr("app.auth.rate_limit._TRUST_PROXY", True)
        req = _mock_request("10.0.0.1")
        req.headers = {"x-forwarded-for": " , "}
        assert _client_ip(req) == "10.0.0.1"

    def test_blank_forwarded_for_falls_back_when_trusted(self, monkeypatch):
        monkeypatch.setattr("app.auth.rate_limit._TRUST_PROXY", True)
        req = _mock_request("10.0.0.1")
        req.headers = {"x-forwarded-for": ""}
        assert _client_ip(req) == "10.0.0.1"


class TestRecordFailure:
    def test_first_failure(self):
        req = _mock_request()
        record_failure(req)
        assert "127.0.0.1" in _attempts
        failures, _ = _attempts["127.0.0.1"]
        assert failures == 1

    def test_consecutive_failures(self):
        req = _mock_request()
        record_failure(req)
        record_failure(req)
        record_failure(req)
        failures, _ = _attempts["127.0.0.1"]
        assert failures == 3

    def test_different_ips_independent(self):
        record_failure(_mock_request("1.1.1.1"))
        record_failure(_mock_request("2.2.2.2"))
        record_failure(_mock_request("2.2.2.2"))
        assert _attempts["1.1.1.1"][0] == 1
        assert _attempts["2.2.2.2"][0] == 2


class TestRecordSuccess:
    def test_clears_entry(self):
        req = _mock_request()
        record_failure(req)
        assert "127.0.0.1" in _attempts
        record_success(req)
        assert "127.0.0.1" not in _attempts

    def test_noop_when_clean(self):
        req = _mock_request()
        record_success(req)  # should not raise
        assert "127.0.0.1" not in _attempts


class TestBackoffCalculation:
    def test_delay_grows_exponentially(self):
        # After N failures, delay = BASE_DELAY * 2^(N-1)
        assert BASE_DELAY * (2 ** 0) == 1.0   # 1 failure  -> 1s
        assert BASE_DELAY * (2 ** 1) == 2.0   # 2 failures -> 2s
        assert BASE_DELAY * (2 ** 2) == 4.0   # 3 failures -> 4s
        assert BASE_DELAY * (2 ** 3) == 8.0   # 4 failures -> 8s

    def test_capped_at_max(self):
        delay = min(BASE_DELAY * (2 ** 99), MAX_DELAY)
        assert delay == MAX_DELAY


class TestCallRateThrottle:
    """Per-caller sliding-window throttle used by expensive authenticated endpoints
    (e.g. /rules/sheaf-preview)."""

    def test_allows_up_to_limit(self):
        req = _tok_request("tokenA")
        for _ in range(CALL_LIMIT):
            enforce_call_rate(req)  # should not raise
        assert len(_calls[_throttle_key(req)]) == CALL_LIMIT

    def test_blocks_over_limit(self):
        req = _tok_request("tokenA")
        for _ in range(CALL_LIMIT):
            enforce_call_rate(req)
        with pytest.raises(HTTPException) as exc:
            enforce_call_rate(req)
        assert exc.value.status_code == 429

    def test_tokens_have_separate_buckets(self):
        a = _tok_request("tokenA")
        b = _tok_request("tokenB")
        for _ in range(CALL_LIMIT):
            enforce_call_rate(a)
        # A is full, but B is a fresh bucket and must still be allowed.
        enforce_call_rate(b)  # should not raise
        assert len(_calls[_throttle_key(b)]) == 1

    def test_key_prefers_token_over_shared_ip(self):
        # Two callers sharing one IP but with different tokens must NOT share a bucket.
        a = _tok_request("tokenA", ip="10.0.0.9")
        b = _tok_request("tokenB", ip="10.0.0.9")
        assert _throttle_key(a) != _throttle_key(b)

    def test_key_never_contains_plaintext_token(self):
        req = _tok_request("supersecret")
        key = _throttle_key(req)
        assert "supersecret" not in key
        assert key.startswith("tok:")

    def test_falls_back_to_ip_without_token(self):
        req = _tok_request(None, ip="10.0.0.7")
        assert _throttle_key(req) == "ip:10.0.0.7"

    def test_window_expiry_allows_again(self):
        req = _tok_request("tokenA")
        for _ in range(CALL_LIMIT):
            enforce_call_rate(req)
        key = _throttle_key(req)
        # Backdate every recorded call to before the window -> they all prune on the next hit.
        _calls[key] = [t - CALL_WINDOW - 1 for t in _calls[key]]
        enforce_call_rate(req)  # window cleared -> allowed again
        assert len(_calls[key]) == 1
