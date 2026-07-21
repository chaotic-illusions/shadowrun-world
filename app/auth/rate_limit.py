"""
Per-IP exponential backoff rate limiter for auth endpoints.

After a failed auth attempt the client must wait before retrying.
The delay doubles with each consecutive failure (1s -> 2s -> 4s -> ...)
up to a configurable cap.  A successful auth resets the counter.
Stale entries are pruned automatically.
"""
import asyncio
import os
import time
from fastapi import Request, HTTPException

from app.auth.core import hash_token


# -- Configuration -------------------------------------------------------------

BASE_DELAY = 1.0       # seconds after the first failure
MAX_DELAY = 30.0       # hard cap on backoff
STALE_AFTER = 300.0    # seconds of inactivity before an entry is pruned

# X-Forwarded-For is client-spoofable. Only trust it when the app is explicitly told it
# sits behind a proxy that overwrites the header; otherwise an attacker could rotate XFF
# to get a fresh bucket per request and bypass the backoff. Default off (use peer IP).
_TRUST_PROXY = os.getenv("TRUST_PROXY_HEADERS", "").strip().lower() in ("1", "true", "yes", "on")


# -- In-memory store ----------------------------------------------------------

# {ip: (consecutive_failures, last_attempt_ts)}
_attempts: dict[str, tuple[int, float]] = {}


def _prune() -> None:
    """Remove entries that haven't been touched in STALE_AFTER seconds."""
    now = time.monotonic()
    stale = [ip for ip, (_, ts) in _attempts.items() if now - ts > STALE_AFTER]
    for ip in stale:
        del _attempts[ip]


def _client_ip(request: Request) -> str:
    """Client IP used as the rate-limit key.

    X-Forwarded-For is only honoured when TRUST_PROXY_HEADERS is set (the app is behind a
    proxy that overwrites it). Otherwise the header is attacker-controlled and would let a
    caller rotate it to dodge the backoff, so we fall back to the socket peer address.
    """
    if _TRUST_PROXY:
        forwarded = request.headers.get("x-forwarded-for")
        if forwarded:
            ip = forwarded.split(",")[0].strip()
            if ip:
                return ip
    return request.client.host if request.client else "unknown"


# -- Public API ---------------------------------------------------------------

async def enforce_rate_limit(request: Request) -> None:
    """FastAPI dependency -- sleeps or rejects if the caller is in backoff."""
    _prune()
    ip = _client_ip(request)
    entry = _attempts.get(ip)
    if not entry:
        return

    failures, last_ts = entry
    delay = min(BASE_DELAY * (2 ** (failures - 1)), MAX_DELAY)
    elapsed = time.monotonic() - last_ts

    if elapsed < delay:
        remaining = delay - elapsed
        if remaining > 5.0:
            # Long waits -> reject immediately instead of holding a connection
            raise HTTPException(
                status_code=429,
                detail=f"Too many failed attempts. Retry in {int(remaining)}s.",
            )
        await asyncio.sleep(remaining)


def record_failure(request: Request) -> None:
    """Call after a failed auth attempt to bump the backoff counter."""
    ip = _client_ip(request)
    failures, _ = _attempts.get(ip, (0, 0))
    _attempts[ip] = (failures + 1, time.monotonic())


def record_success(request: Request) -> None:
    """Call after a successful auth to reset the backoff counter."""
    ip = _client_ip(request)
    _attempts.pop(ip, None)


# -- Per-caller call-rate throttle (expensive authenticated endpoints) ---------
#
# Distinct from the auth backoff above: this is NOT failure-driven. It caps how often a
# *valid* caller may hit a CPU-heavy route (e.g. the sheaf live-preview generator), keyed
# per token so one runner -- or a leaked token -- cannot spam it. Plain sliding window.

CALL_WINDOW = 60.0     # sliding window, seconds
CALL_LIMIT = 30        # max calls per key per window (accommodates the live-preview UI)

# {key: [ts, ts, ...]} -- monotonic timestamps of recent calls still inside the window
_calls: dict[str, list[float]] = {}


def _throttle_key(request: Request) -> str:
    """Bucket key for the call-rate throttle: prefer the caller's (already auth-validated)
    token so the limit is per-token, falling back to the client IP when no token header is
    present. The token is keyed only by its SHA-256 hash -- never store the plaintext.
    """
    tok = request.headers.get("x-user-token") or request.headers.get("x-admin-token")
    if tok:
        return "tok:" + hash_token(tok)
    return "ip:" + _client_ip(request)


def _prune_calls() -> None:
    """Drop keys whose whole window has expired (keeps _calls from growing unbounded)."""
    now = time.monotonic()
    dead = [k for k, ts in _calls.items() if not ts or now - ts[-1] >= CALL_WINDOW]
    for k in dead:
        del _calls[k]


def enforce_call_rate(request: Request) -> None:
    """FastAPI dependency -- throttle an expensive authenticated endpoint to CALL_LIMIT calls
    per CALL_WINDOW seconds per caller. Raises 429 when the window is full.
    """
    _prune_calls()
    now = time.monotonic()
    key = _throttle_key(request)
    recent = [t for t in _calls.get(key, ()) if now - t < CALL_WINDOW]
    if len(recent) >= CALL_LIMIT:
        retry = int(CALL_WINDOW - (now - recent[0])) + 1
        _calls[key] = recent
        raise HTTPException(
            status_code=429,
            detail=f"Rate limit exceeded ({CALL_LIMIT} requests/{int(CALL_WINDOW)}s). "
                   f"Retry in {retry}s.",
        )
    recent.append(now)
    _calls[key] = recent
