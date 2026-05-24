---
applyTo: "seed.py,tests/**"
---

# Seed Script & Test Suite Reference

## seed.py
- Uses `httpx.Client` (sync) with `base_url` and `headers={"X-Admin-Token": token}`
- Auth: `--admin-token` CLI arg overrides `BOOTSTRAP_ADMIN_KEY` env var (default `shadowrunner`)
- Seed order: RTGs -> Organizations -> (org ally/enemy links) -> Locations -> Characters -> Contacts -> Org Standings -> Adventure Logs
- `post(client, path, payload)` -- raises `RuntimeError` on `HTTPStatusError` or `RequestError`
- `patch(client, path, payload)` -- same error contract as `post`

## Test Suite
- Runner: `pytest -v`; all tests are **sync** (no async fixtures)
- `conftest.py` is empty -- no shared fixtures

### test_seed.py
- Mocks `httpx.Client` methods directly: `mock_client.post.return_value`
- Does NOT patch `urllib` -- seed.py uses httpx, not urllib
- Error cases: `httpx.HTTPStatusError` for 4xx/5xx, `httpx.ConnectError` for network failures

### test_auth.py
- Tests `hash_token` (deterministic, 64-char hex output) and `generate_token` (unique, correct length)
- No DB or HTTP calls -- pure unit tests

### test_rate_limit.py
- Uses `_attempts` dict directly to inspect state; `autouse` fixture calls `_attempts.clear()`
- `_mock_request(ip)` creates a `MagicMock` with `.client.host` and `.headers`
- Tests `record_failure`, `record_success`, backoff math, IP resolution

### test_heat_calculator.py
- Tests label functions, `compute_heat`, `decay_heat`, `decay_pa`, `decay_standing`, `compute_ripple`
- `compute_ripple` fixture: org 1 allied with 2, enemy of 3

### test_consequence_engine.py
- Tags must match names in `SINGLE_TAG_RULES` / `COMPOUND_TAG_RULES` in `app/data/consequence_tags.py`
- Tests compound rules fire before single-tag rules in output ordering
