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

# {(ip, credential_scope): (consecutive_failures, last_attempt_ts)}
_attempts: dict[tuple[str, str], tuple[int, float]] = {}


def _prune() -> None:
    """Remove entries that haven't been touched in STALE_AFTER seconds."""
    now = time.monotonic()
    stale = [key for key, (_, ts) in _attempts.items() if now - ts > STALE_AFTER]
    for key in stale:
        del _attempts[key]


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
    entries = [entry for (attempt_ip, _), entry in _attempts.items() if attempt_ip == ip]
    if not entries:
        return

    now = time.monotonic()
    remaining = max(
        min(BASE_DELAY * (2 ** (failures - 1)), MAX_DELAY) - (now - last_ts)
        for failures, last_ts in entries
    )

    if remaining > 0:
        if remaining > 5.0:
            # Long waits -> reject immediately instead of holding a connection
            raise HTTPException(
                status_code=429,
                detail=f"Too many failed attempts. Retry in {int(remaining)}s.",
            )
        await asyncio.sleep(remaining)


def record_failure(request: Request, scope: str = "any") -> None:
    """Call after a failed auth attempt to bump the backoff counter."""
    key = (_client_ip(request), scope)
    failures, _ = _attempts.get(key, (0, 0))
    _attempts[key] = (failures + 1, time.monotonic())


def record_success(request: Request, scope: str | None = "any") -> None:
    """Call after a successful auth to reset one scope, or every scope when ``scope`` is None."""
    ip = _client_ip(request)
    if scope is None:
        for key in [key for key in _attempts if key[0] == ip]:
            del _attempts[key]
        return
    _attempts.pop((ip, scope), None)


# -- Per-caller call-rate throttle (expensive authenticated endpoints) ---------
#
# Distinct from the auth backoff above: this is NOT failure-driven. It caps how often a
# *valid* caller may hit a CPU-heavy route (e.g. the sheaf live-preview generator), keyed
# per token so one runner -- or a leaked token -- cannot spam it. Plain sliding window.

CALL_WINDOW = 60.0     # sliding window, seconds
CALL_LIMIT = 30        # max calls per key per window (accommodates the live-preview UI)

# {key: [ts, ts, ...]} -- monotonic timestamps of recent calls still inside the window
_calls: dict[str, list[float]] = {}


def _throttle_key(request: Request, auth: dict | None = None) -> str:
    """Bucket key for the call-rate throttle, derived from authenticated context when present."""
    tok = auth.get("user_token") if auth else None
    if tok:
        return "tok:" + hash_token(tok)
    return "ip:" + _client_ip(request)


def _prune_calls() -> None:
    """Drop keys whose whole window has expired (keeps _calls from growing unbounded)."""
    now = time.monotonic()
    dead = [k for k, ts in _calls.items() if not ts or now - ts[-1] >= CALL_WINDOW]
    for k in dead:
        del _calls[k]


async def enforce_call_rate(request: Request, auth: dict | None = None) -> None:
    """FastAPI dependency -- throttle an expensive authenticated endpoint to CALL_LIMIT calls
    per CALL_WINDOW seconds per caller. Raises 429 when the window is full.

    Declared ``async`` on purpose: it runs on the event-loop thread (not the sync-dependency
    threadpool) and contains no ``await``, so the read-modify-write of the shared ``_calls`` map
    is atomic -- concurrent requests cannot interleave and over-admit past the limit.
    """
    _prune_calls()
    now = time.monotonic()
    key = _throttle_key(request, auth)
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
