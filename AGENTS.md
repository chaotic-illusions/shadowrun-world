# Agent Working Guide -- Shadowrun World Engine

How to add code to this project safely. This is the **process / pitfalls / checklist**
guide. For *what the code is* (stack, models, services, auth), see the path-scoped
references in [.github/instructions/](.github/instructions/) and
[.github/copilot-instructions.md](.github/copilot-instructions.md). For the deferred-work
backlog, see [docs/refactor-notes.md](docs/refactor-notes.md).

Golden rule: **reuse before you write.** Most "new" UI styling, DB helpers, and auth
checks already exist. Search first; add second.

---

## 1. Check first (before writing anything)

| Need | Look here first | Don't |
|---|---|---|
| A color / spacing / layout style | `frontend/style.css` utilities: `.hidden`, `.text-dim/-cyan/-amber/-green/-red/-bright`, `.mb-*` / `.mt-*`, `.flex-*`, `.dim-label`, `.field-label`, `.modal-*` | add an inline `style=` for something a class already does |
| A JS helper (escape, fetch, alert, confirm, polling, number steppers) | `frontend/shared.js`: `esc`, `apiFetch`, `authHeaders`, `showAlert`, `showConfirm`, `startPolling`/`pausePoll`/`resumePoll`, `initNumSteppers`, `parseSan`, `buildLTGCodeOpts`/`buildSecValOpts` | re-implement escaping or auth-header logic |
| A DB load / update | `app/dependencies.py`: `get_db`, `get_or_404`, `apply_update` | hand-roll a PATCH loop |
| Auth on an endpoint | `app/auth/dependencies.py`: `get_admin_token`, `get_any_token` | re-derive token hashing |
| The shape of a new resource | an existing `models/` + `schemas/` + `routers/` trio | invent a new pattern |
| Refactoring a big/flagged area | `docs/refactor-notes.md` (e.g. R1 `perform_action`) | churn code that's deliberately deferred |

---

## 2. Backend (FastAPI + async SQLAlchemy 2.x + Pydantic v2)

- **Async everywhere.** `AsyncSession`, `await db.execute(...)`, `result.scalars()`.
- **Schemas:** input schemas use `model_config = ConfigDict(extra='forbid')`. Split
  `Create` / `Update` (all-Optional) / `Read` (`from_attributes=True`). PATCH via
  `apply_update(db, obj, body, exclude={...})`.
- **JSON columns** (`Mapped[dict|list]`): rebuild the whole object and **reassign the
  attribute**, or use `sqlalchemy.update(...).values(col=new_obj)`. Do NOT mutate a
  nested dict/list in place and rely on `flag_modified` -- it is unreliable in async
  sessions. (See `reference_app_architecture` memory + organizations `ltg-security`.)
- **Auth pattern:** world-data routers are registered in `main.py` with
  `dependencies=[Depends(get_any_token)]`; add `_: str = Depends(get_admin_token)` per
  endpoint for admin-only mutations. `get_any_token` returns
  `{is_admin, is_user, user_token}`.
- **Hide existence with 404, not 403.** When a non-owner must not even learn a row
  exists, raise 404 (see `matrix_runs._assert_run_access`). 403 leaks existence.
- **Owner-scoped access:** compare `hash_token(ctx["user_token"])` to the stored hash.
  Never return plaintext tokens -- `owner_token` is `Field(exclude=True)` in Read schemas.
- **GM / hidden gameplay data:** redact it **server-side** in the serializer for
  non-admins (see `matrix_runs._serialize_run`, `_GM_ONLY_STATE_KEYS`). The client's
  `.gm-only` CSS and `isAdmin()` are cosmetic -- the data is still in the payload unless
  the server strips it.
- **Player-writable JSON:** cap its size in the schema validator (see
  `deck_builder_state`, 256 KB).
- **Concurrent writers on a stateful row:** `MatrixRun` uses optimistic locking
  (`__mapper_args__ = {"version_id_col": version}` -> `StaleDataError` -> 409 handler in
  `main.py`). Don't bypass it with a raw UPDATE that skips the version bump.
- **RNG:** never call `random.seed()` on the global RNG inside a request path -- it makes
  every later roll in the process predictable. Use a local `random.Random(seed)` or
  save/restore `getstate()/setstate()` (see `generate_sheaf`).
- **M2M relations:** set them on the **transient** object before `db.add()`
  (otherwise MissingGreenlet in async).
- **New endpoint:** register the router in `main.py` with the correct auth dependency and
  confirm the URL prefix.
- **Rate limiter only trusts `X-Forwarded-For` when `TRUST_PROXY_HEADERS=1`**
  (`auth/rate_limit.py`); otherwise it keys on the socket peer IP. Set that env var ONLY
  when behind a proxy that overwrites the header -- enabling it on a directly-exposed app
  lets a caller rotate XFF to dodge the auth backoff.

---

## 3. Frontend (vanilla JS, no build step)

- `frontend/` is a **live mount** -- HTML/JS/CSS changes take effect immediately. Python
  (`app/`) is baked into the Docker image -- backend changes need `docker compose up --build`.
- **Always `esc()`** any server- or user-derived value placed into `innerHTML` or a
  template literal. Prefer `.textContent` for plain text. (XSS is otherwise trivial via
  names, notes, labels.)
- **Use `apiFetch`** (adds auth headers + content-type), not raw `fetch`, for API calls.
- **Inline styles:** check `style.css` first. Inline is acceptable ONLY for
  runtime-computed values (e.g. `style="color:${dynamicColor}"`). A fixed color/margin
  belongs in a class.
- **Inline color overriding a component class** is a known trap: the inline wins now, but
  merging it into the class may not (CSS source order). Don't blind-convert -- there's an
  enumerated list in the `project_matrix2_review` memory for the UI consistency pass.
- **ASCII-only source** (enforced by the pre-commit hook). Use HTML entities for glyphs:
  `&mdash;`, `&times;`, `&yen;`, `&ge;`, `&#9650;`. No pasted smart quotes / em dashes.
- **Reuse `shared.js`; don't shadow it.** `showAlert` and friends live in `shared.js`;
  some pages redefine their own copy (and then drift). Prefer the shared helper.
- **Re-edits leave dead code.** After refactoring a page, re-check for functions defined
  but never called (and orphaned section-header comments). For a `.js` paired with a
  `.html` (e.g. `world-state.js` / `world-state.html`), search BOTH files -- a `.js`
  function is usually called from inline handlers in the `.html`, so a single-file scan
  reports false positives.

### Dice rolls -- Rule of 6 (exploding sixes) ALWAYS applies

Every SR2 dice roll in this app uses the **rule of 6**: a die showing 6 is re-rolled and
the result **added** to that die's total, repeating while it keeps coming up 6. The
accumulated per-die total is what you compare to the target number -- so a 6 can chain to
beat a TN above 6 (e.g. vs TN 12 a die can roll 6+6+3=15). Without it, **any TN > 6 is
unbeatable** (a flat d6 maxes at 6) and the test silently always yields 0 successes.

- Backend canonical impl: `app/services/matrix_engine.py` `roll_dice(pool, tn)` -- it only
  explodes when `tn > 6` (for `tn <= 6` a 6 is already a success, so exploding can't change
  the success count; that's a valid optimization, not a different rule).
- Frontend: use `rollDicePool(dice, tn)` / `rollExplodingD6()` in `deck-builder*.html`. Do
  NOT hand-roll `Math.floor(Math.random()*6)+1` and compare to TN -- that skips the rule
  and breaks every high-TN test (this was the deck-construction and `rollProgrammingTask`
  bug fixed 2026-06-04). Reuse the helper for any new roll.

---

## 4. Database, migrations & deployment

- Startup runs `Base.metadata.create_all` -- this creates **missing tables** (fresh DB)
  but does **not** add columns to existing tables. So a new column needs BOTH:
  1. an Alembic migration in `alembic/versions/`, and
  2. (if runtime code touches it before the migration is applied) a startup-guard
     `ALTER TABLE ... ADD COLUMN` like `_ensure_matrix_run_version_column` in `main.py`.
- Keep a **single Alembic head**: after parallel branches, `alembic heads` must show one
  -- add a merge migration if it shows several.
- **Verify writes through the API, not the `.db` file** -- SQLite WAL mode can show stale
  reads from a direct file read.
- **SQLite FK enforcement is ON** (`PRAGMA foreign_keys=ON` in `db/session.py`), so
  declared `ondelete=` rules actually fire. Consequence: a FK with **no** `ondelete` and
  no ORM cascade will now **block** a parent delete. The org/location/character delete
  endpoints null such references first (SET NULL semantics) -- when you add a new FK,
  either give it an `ondelete=` rule or clean up referencing rows in the delete path, or
  the delete will 500.
- **`.dockerignore` exists -- keep it current.** The Dockerfile does `COPY . .` and Docker
  does NOT read `.gitignore`, so anything sensitive/bloaty (the `data/*.db`, `.git/`,
  `.venv/`) must be listed in `.dockerignore` or it gets baked into the image.
- `requirements.txt` is pinned -- bump deliberately (the `anthropic`/`aiofiles`/
  `pytest-asyncio` lines are bounded ranges, not exact). For a real (exposed) deployment
  also: run the container as non-root (`USER` -- not yet done), and revisit `CORS_ORIGINS`
  (`*` is safe with header auth) and the default `BOOTSTRAP_ADMIN_KEY=shadowrunner` before
  going past the default `127.0.0.1` binding.

---

## 5. Validate after (before saying "done")

Run these for the layers you touched:

```
python -m py_compile <changed .py files>     # syntax
python -m pytest -q                          # full suite (should stay green)
python -c "import app.main"                  # catches wiring / mapper config errors
python tools/check_text_hygiene.py           # ASCII / encoding (pre-commit also runs it)
```

- **Frontend JS** has no build step, so the syntax gate is: extract the `<script>` blocks
  and run `node --check` on them.
- **DB change:** confirm `alembic heads` is single; if you added a startup-guard, it must
  be idempotent (PRAGMA-check before ALTER).
- **Don't commit or push** unless asked. If you must branch, branch off `main`.

---

## 6. Common pitfalls (quick reference)

| Symptom | Cause | Fix |
|---|---|---|
| Style duplicated across pages | inline `style=` when a class exists | use the `style.css` utility/component class |
| Stored XSS via a name/note | `innerHTML` without `esc()` | wrap with `esc()` or use `.textContent` |
| JSON column change not saved | mutated nested dict/list in place | rebuild + reassign, or `sql_update().values()` |
| Other requests roll predictable dice | `random.seed()` on global RNG in a handler | local `random.Random` or save/restore state |
| Existing DBs break after deploy | new column, no startup guard | add Alembic migration + `_ensure_*` guard |
| Player sees GM secrets in devtools | relied on `.gm-only` / `isAdmin()` only | redact server-side in the serializer |
| Non-owner learns a row exists | returned 403 for a hidden resource | return 404 |
| `alembic upgrade` fails | multiple heads after branching | add a merge migration |
| Parent delete 500s | new FK with no `ondelete`/cleanup (FK enforcement is ON) | give it `ondelete=` or null refs in the delete path |
| Sensitive/bloaty files in the image | something not listed in `.dockerignore` (Docker ignores `.gitignore`) | add it to `.dockerignore` |
| Auth backoff bypassed when exposed | `TRUST_PROXY_HEADERS=1` without a real proxy | only set it behind a proxy that overwrites XFF |
| Two pages drift on one helper | redefined `showAlert` etc. instead of using `shared.js` | use the shared helper |
