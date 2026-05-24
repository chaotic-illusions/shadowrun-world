---
applyTo: "app/services/**,app/routers/**,app/models/**,app/schemas/**"
---

# Services, Routers & Models Reference

## Router Conventions
- All world-data routers registered in `main.py` with `dependencies=[Depends(get_any_token)]`
- Admin-only operations add `_: str = Depends(get_admin_token)` per-endpoint
- M2M relationships (e.g. participants, locations, orgs on AdventureLog) must be set on the **transient** object before `db.add()` -- setting them after flush triggers MissingGreenlet in async SQLAlchemy

## DB Session Pattern
```python
# Always via dependency injection
async def endpoint(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Model).where(...))
    rows = result.scalars().all()
```

## Key Services

### heat_calculator.py
- `decay_heat(value, elapsed_days, accel=1.0)` -- exponential half-life by tier
- `decay_pa(value, elapsed_days, accel=1.0)` -- same pattern for public awareness
- `decay_standing(value, elapsed_days)` -- positive decays 1.5x slower than negative
- `compute_ripple(org_id, delta, org_map)` -> list of `{org_id, delta}` at 40% magnitude, capped +/-2
- `LYING_LOW_DECAY_ACCEL = 2.0` -- applied when character is lying low
- Tiers: heat 0=Neutral,1-2=Noticed,3-4=Flagged,5-6=Wanted,7-8=Hot,9-10=Nova Hot

### consequence_engine.py
- `suggest(tags: list[str]) -> list[dict]` -- returns ordered suggestions by severity
- Checks COMPOUND_TAG_RULES first (multi-tag combos), then SINGLE_TAG_RULES
- Deduplicates suggestions by text; output includes `severity`, `suggestion`, `source_tags`
- Severity order: severe > significant > moderate > variable > low > positive

### narrative_parser.py
- `parse_narrative(narrative, world_context) -> dict` -- async, calls Anthropic API
- Lazy-imported at call site in `routers/adventure_logs.py` so missing API key causes 503, not startup crash
- `world_context` keys: `characters`, `organizations`, `reputation`, `standings`
- Returns: `title`, `objective`, `result`, `outcome`, `employer`, `outcome_tags`, `proposed_changes`

### campaign.py
- `current_tick(db)` -> `sum(AdventureLog.tick_count)` -- total elapsed campaign days

### secrets.py
- `get_api_key()` -> keyring first (Windows Credential Manager), then `ANTHROPIC_API_KEY` env var, else `None`

## Model Notes
| Model | Notable Fields |
|-------|---------------|
| `Character` | `is_pc`, `is_active`, `owner_token` (SHA-256 hash of owning user token) |
| `AdventureLog` | `tick_count` (1-5), `outcome_tags` (JSON), `changes_applied` (JSON), `heat` (int) |
| `Reputation` | `street_cred`, `notoriety`, `public_awareness`, `pa_updated_at`, `pa_stamped_tick` |
| `OrgStanding` | `standing` (-10 to +10), per character per org |
| `Organization` | `ally_ids` (JSON list), `enemy_ids` (JSON list) -- used for ripple calc |
| `MatrixHost` | `topology` (JSON), `is_visible` (bool -- player visibility toggle) |
| `UserToken` | `token_hash` (64-char hex), `is_admin` (bool), `label` |

## Schema Conventions
- All schemas use Pydantic v2 `model_config = ConfigDict(from_attributes=True)`
- `Create` schemas: input validation, required fields
- `Update` schemas: all fields `Optional`, used with `apply_update()` from `dependencies.py`
- `Read` schemas: include `id`, timestamps, nested relations as summaries
