"""
Per-IP exponential backoff rate limiter for auth endpoints.

After a failed auth attempt the client must wait before retrying.
The delay doubles with each consecutive failure (1s → 2s → 4s → …)
up to a configurable cap.  A successful auth resets the counter.
Stale entries are pruned automatically.
"""
import asyncio
import time
from fastapi import Request, HTTPException


# ── Configuration ─────────────────────────────────────────────────────────────

BASE_DELAY = 1.0       # seconds after the first failure
MAX_DELAY = 30.0       # hard cap on backoff
STALE_AFTER = 300.0    # seconds of inactivity before an entry is pruned


# ── In-memory store ──────────────────────────────────────────────────────────

# {ip: (consecutive_failures, last_attempt_ts)}
_attempts: dict[str, tuple[int, float]] = {}


def _prune() -> None:
    """Remove entries that haven't been touched in STALE_AFTER seconds."""
    now = time.monotonic()
    stale = [ip for ip, (_, ts) in _attempts.items() if now - ts > STALE_AFTER]
    for ip in stale:
        del _attempts[ip]


def _client_ip(request: Request) -> str:
    """Best-effort client IP — respects X-Forwarded-For behind a reverse proxy."""
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


# ── Public API ───────────────────────────────────────────────────────────────

async def enforce_rate_limit(request: Request) -> None:
    """FastAPI dependency — sleeps or rejects if the caller is in backoff."""
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
            # Long waits → reject immediately instead of holding a connection
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
