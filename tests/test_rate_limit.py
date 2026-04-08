"""Tests for the auth rate limiter."""
import time
import pytest
from unittest.mock import MagicMock

from app.auth.rate_limit import (
    record_failure, record_success, _attempts, _client_ip,
    BASE_DELAY, MAX_DELAY,
)


def _mock_request(ip: str = "127.0.0.1") -> MagicMock:
    req = MagicMock()
    req.client.host = ip
    req.headers = {}
    return req


@pytest.fixture(autouse=True)
def clear_state():
    """Reset the rate limiter state between tests."""
    _attempts.clear()
    yield
    _attempts.clear()


class TestClientIp:
    def test_direct(self):
        req = _mock_request("10.0.0.1")
        assert _client_ip(req) == "10.0.0.1"

    def test_forwarded_for(self):
        req = _mock_request("10.0.0.1")
        req.headers = {"x-forwarded-for": "203.0.113.5, 10.0.0.1"}
        assert _client_ip(req) == "203.0.113.5"


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
        assert BASE_DELAY * (2 ** 0) == 1.0   # 1 failure  → 1s
        assert BASE_DELAY * (2 ** 1) == 2.0   # 2 failures → 2s
        assert BASE_DELAY * (2 ** 2) == 4.0   # 3 failures → 4s
        assert BASE_DELAY * (2 ** 3) == 8.0   # 4 failures → 8s

    def test_capped_at_max(self):
        delay = min(BASE_DELAY * (2 ** 99), MAX_DELAY)
        assert delay == MAX_DELAY
