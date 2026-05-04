---
applyTo: "app/auth/**,app/routers/auth.py"
---

# Auth Subsystem Reference

## Files
| File | Role |
|------|------|
| `app/auth/core.py` | `hash_token`, `generate_token`, `verify_admin_token`, `verify_user_token`, `is_default_admin_password` |
| `app/auth/dependencies.py` | FastAPI deps: `get_admin_token`, `get_any_token` — used in router `Depends()` |
| `app/auth/rate_limit.py` | In-memory exponential backoff per IP; `enforce_rate_limit`, `record_failure`, `record_success` |
| `app/routers/auth.py` | `/auth/verify`, `/auth/tokens` CRUD |

## Token Model
- Stored as SHA-256 hex (64 chars) in `UserToken.token_hash`
- Plaintext shown ONCE at creation, never again
- `generate_token(nbytes=24)` → `secrets.token_hex(nbytes)` → 48-char hex string
- `is_admin=True` on `UserToken` → grants admin role

## Bootstrap Flow
- `BOOTSTRAP_ADMIN_KEY` (default `shadowrunner`) is accepted as admin password **only** while `UserToken` table has no admin rows
- After first real token is created, bootstrap key is silently rejected
- `is_default_admin_password()` → True if no admin tokens exist yet (used to show warning in UI)

## Auth Dependency Chain
```
get_admin_token → verify_admin_token() → hash + DB lookup
get_any_token   → verify_admin_token() OR verify_user_token()
enforce_rate_limit → async; raises 429 after exponential backoff per IP
```

## Rate Limiter
- State: `_attempts: dict[str, tuple[int, float]]` — `{ip: (failure_count, last_fail_time)}`
- Delay: `min(BASE_DELAY * 2^(n-1), MAX_DELAY)` where `BASE_DELAY=1.0`, `MAX_DELAY=60.0`
- IP resolution: `X-Forwarded-For` header → first IP; falls back to `request.client.host`
- `record_success()` clears the IP entry

## Token Regeneration Side-Effect
When a token is regenerated, all `Character.owner_token` values matching the old hash are re-pointed to the new hash before the token record is updated.
