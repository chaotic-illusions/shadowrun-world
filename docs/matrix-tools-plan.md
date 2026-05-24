# Matrix Tools -- Internal Design Notes
> SR2 / VR2.0 rules. DO NOT touch manage-matrix.html (SR1 fallback).

## New Pages
| File | Purpose |
|------|---------|
| `frontend/matrix-designer.html` | GM host designer wizard (SR2 rules) |
| `frontend/matrix-run.html` | Player run simulator |

## New Backend Files
| File | Purpose |
|------|---------|
| `app/services/matrix_rules.py` | All VR2 rules tables (static data) |
| `app/services/matrix_engine.py` | Dice rolling, cybercombat, sheaf generation |
| `app/models/matrix_run.py` | MatrixRun DB model |
| `app/schemas/matrix_run.py` | Pydantic schemas |
| `app/routers/matrix_runs.py` | Run session API |

## API Endpoints (matrix_runs router, prefix /matrix-runs2)
```
POST /matrix-runs2/                       Start a new run (decker stats + host_id)
GET  /matrix-runs2/{id}                   Get run state
POST /matrix-runs2/{id}/action            Perform a decker action (system test)
POST /matrix-runs2/{id}/attack            Decker attacks an IC program
POST /matrix-runs2/{id}/logoff            Attempt graceful logoff
DELETE /matrix-runs2/{id}                 Abandon run
GET  /matrix-runs2/                       List runs (admin only)
GET  /matrix-runs2/rules/ic-info          IC catalog (full VR2 set)
GET  /matrix-runs2/rules/sheaf-preview    Preview auto-generated sheaf given params
POST /matrix-hosts2/{id}/sheaf            Save sheaf to a matrix host (designer)
POST /matrix-hosts2/generate2             Generate full host from wizard params
```

Note: matrix-hosts2 endpoints are for the SR2 designer and extend the existing /matrix-hosts router
by adding new routes (not replacing). Use prefix /matrix-hosts2 to avoid conflicts.

## MatrixRun state_json schema
```json
{
  "security_tally": 0,
  "alert_status": "none",
  "condition_monitor": {
    "persona_boxes": 0,
    "physical_boxes": 0,
    "mpcp_damage": 0,
    "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}
  },
  "active_ic": [
    {
      "id": "ic_001",
      "type": "Killer",
      "rating": 8,
      "category": "gray",
      "boxes": 0,
      "suppressed": false,
      "initiative": 15,
      "status": "active",
      "hunt_cycle_successes": 0
    }
  ],
  "current_turn": 1,
  "sheaf_steps_triggered": [0, 1],
  "detection_factor": 6,
  "event_log": [
    {"turn": 1, "type": "action", "description": "...", "dice": {...}}
  ],
  "logon_complete": false,
  "run_ended": false,
  "end_reason": null
}
```

## Decker JSON schema (input when starting run)
```json
{
  "name": "Ghost",
  "mpcp": 8,
  "bod": 6,
  "evasion": 6,
  "masking": 6,
  "sensor": 6,
  "computer_skill": 6,
  "intelligence": 5,
  "willpower": 5,
  "deck_mode": "hot",
  "iccm": false,
  "response_increase": 0,
  "utilities": {
    "attack": 6,
    "armor": 6,
    "sleaze": 0,
    "deception": 6,
    "browse": 6,
    "evaluate": 4,
    "analyze": 6,
    "decrypt": 4,
    "crash": 4,
    "mirrors": 4
  }
}
```

## MatrixHost config_json extension (sheaf)
Added to existing config_json:
```json
{
  "san_rating": "Red-9",
  "acifs": [15, 14, 16, 14, 16],
  "security_code": "Red",
  "security_value": 9,
  "owner_type": "corp",
  "sheaf": [
    {
      "trigger": 3,
      "events": [
        {"type": "ic", "ic_type": "Probe", "rating": 8}
      ]
    },
    {
      "trigger": 6,
      "events": [
        {"type": "ic", "ic_type": "Killer", "rating": 9},
        {"type": "passive_alert"}
      ]
    },
    {
      "trigger": 9,
      "events": [
        {"type": "ic", "ic_type": "Black IC", "rating": 10}
      ]
    },
    {
      "trigger": 12,
      "events": [
        {"type": "active_alert"}
      ]
    },
    {
      "trigger": 15,
      "events": [{"type": "shutdown"}]
    }
  ]
}
```

## Action types (POST /matrix-runs2/{id}/action)
```json
{
  "action_type": "logon_to_host|logon_to_ltg|analyze_host|analyze_ic|locate_file|
                  download_data|edit_file|control_slave|null_operation|...",
  "subsystem": "access|control|index|files|slave",
  "utility_rating": 6,
  "hacking_pool_dice": 2,
  "target_ic_id": null
}
```

## Dice resolution
- SR2: d6 dice pool, success = result >= TN (default TN=4, but Matrix uses host subsystem rating as TN)
- `roll_dice(pool, tn)` -> `{dice: [list], successes: int, ones: int}`
- Security test always runs alongside every system test: `(security_value) dice vs. detection_factor`
- Host successes on security test -> added to security tally

## Sheaf auto-generator algorithm
1. Parse security code -> get interval range
2. Start at base trigger (random within first trigger range)
3. For each step: next_trigger = prev_trigger + random(interval_min, interval_max)
4. Stop after 8-12 steps (complexity dependent)
5. IC selection pool changes by position:
   - Steps 1-2: Probe, passive cripplers
   - Steps 3-5: Killer/Blaster/Trace, Passive Alert somewhere here
   - Steps 6-8: Heavier IC, Black IC (if Orange+), Active Alert
   - Last step: Shutdown
6. Rating = security_value + random(-1, +2), clamped to [security_value-2, security_value+4]
7. Owner hint modulates IC pool (see matrix_engine.py SHEAF_IC_POOLS)
