# Enemy (Security) Decker Loadout -- Implementation Spec

> **STATUS: PROPOSAL -- pending user review. DO NOT IMPLEMENT until the user approves.**
> This is a design/implementation spec for a future agent. Treat every table and task below as a
> draft the user still wants to revise. When approved, the user will say so explicitly; until then,
> read-only.

## 0. Context for the implementing agent

Everything here concerns the app-as-GM Matrix run engine. There is **no human GM** -- the app drives
every hostile (IC and enemy deckers). Relevant code:

- `app/services/matrix_engine.py`
  - `_ENEMY_DECKER_TIERS` (~L1010) -- fixed per-tier stat table (the thing this spec replaces/extends).
  - `generate_enemy_decker(security_code, security_value, *, name=None)` (~L1034) -- builds the enemy dict.
  - `enemy_locate_test(...)`, `pc_locate_decker_test(...)`, `escalate_enemy_intent(...)`, `hog_attack(...)`,
    `decker_attribute_attack(...)`, `cybercombat_attack(...)`.
- `app/routers/matrix_runs.py`
  - `_enemy_decker_take_turn(state, decker, run, enemy)` (~L5316) -- Phase 1 locate, Phase 2 execute program,
    plus the self-preservation "fled" branch already added.
  - `attack_enemy_decker` endpoint (~L5630) -- the PC's Strike Back against a revealed enemy.
  - `_activate_sheaf_step(...)` `enemy_decker` branch (~L1074) -- where a decker is spawned.
  - `_redact_enemy_decker(e)` (~L340) -- player-view redaction of enemy stats.

Validate after any change: `python -m py_compile ...`, `python -c "import app.main"`,
`python -m pytest -q`, `python tools/check_text_hygiene.py`.

---

## 1. Design principle (home-field advantage) -- MAKE THIS PERMANENT

Security deckers defend on **home turf**. They are authorized users, so subsystem ratings never
impede them and they need no Logon/Deception tricks. They do **not** perform intruder activities:

- NO data theft / Download Data, NO Evaluate/paydata hunting.
- NO Analyze Host / Analyze Icon / Analyze Security (they already know their own house).
- NO file cracking / Decrypt / Browse / Read-Write / Spoof-slave / Validate-passcode.

Their **entire** kit exists to do two things:

1. **HUNT** the intruder (find the PC's icon).
2. **DEFEAT** the intruder (crash the icon / deck / persona), while **SURVIVING** long enough to do so.

---

## 2. How enemy deckers are spawned TODAY (verified 2026-07-03)

Short answer to "is it random based on security sheaf tally?": **the timing is tally-driven, but the
spawn itself is authored, not random, and the auto-sheaf generator never adds one.**

Mechanics:

1. A host has a **sheaf** = an escalation script: a list of steps
   `[{"trigger": <tally_threshold>, "events": [...]}, ...]`.
2. Every operation that raises `state["security_tally"]` calls `_check_and_activate_sheaf`, which calls
   `_check_sheaf_triggers` (matrix_runs.py ~L835): any step whose `trigger <= tally` and not yet fired
   is activated (tracked in `sheaf_steps_triggered`, so each fires once).
3. If an activated step contains an `{"type": "enemy_decker"}` event, `_activate_sheaf_step`
   (matrix_runs.py ~L1074) calls `generate_enemy_decker(security_code, security_value, name=...)`,
   rolls its initiative once, and appends it to `state["enemy_deckers"]` with a GM-only
   `enemy_decker_injected` log entry.

Key consequences:

- **Trigger = security tally** crossing the authored step threshold. So *when* a decker appears is
  tally-gated.
- **The `enemy_decker` event handler is dormant -- nothing currently produces it.** The branch in
  `_activate_sheaf_step` (~L1074) fires only if a step literally contains `{"type": "enemy_decker"}`,
  but: `_generate_sheaf_impl` (matrix_engine.py ~L573) emits only IC / passive_alert / active_alert /
  shutdown; `world_seed.json` has **zero** enemy_decker entries; the `SheafEvent` schema
  (schemas/matrix_run.py ~L217) doesn't advertise the type (and drops the `name`/`intent` fields the
  handler reads); and no host/sheaf UI exposes it. The **only** way to author one today is for an admin
  to hand-write `{"type": "enemy_decker"}` into a host's saved sheaf JSON via `POST /hosts/{id}/sheaf`
  (`SheafEvent.type` is a free string). **In normal play no host spawns a decker at all.**
- **Stats scale to the host** (`security_code` picks the tier, `security_value` scales skill/MPCP) but
  program ratings are currently **fixed** -> every Red decker is a carbon copy of every other Red decker.

> **DECIDED (2026-07-03):** add a **count-gated probabilistic spawn system** -- see section 6. It
> becomes the **first and only** real spawner in normal play (the dormant authored path above stays
> supported but is unused). After *any* sheaf step fires, the host rolls a tier-scaled chance to
> dispatch a decker, capped per run; a rare hand-authored decker (if one is ever added) simply counts
> toward that cap with no special handling.

---

## 3. Program deep-dive -- the three jobs

### HUNT (find the PC)
- **Scanner** (mult 3) -- lowers the TN on Locate Decker. Already used by `enemy_locate_test`.
- **Sleaze** (mult 3) -- passive; raises the enemy's own Detection Factor so the PC's
  `pc_locate_decker_test` (vs enemy Masking + Sleaze) is harder. Lets it lurk / ambush.
- **Track** (mult 8) -- premium; traces a decker even before it jacks out. Red/Black flavor.
  **Not modeled yet.**

### KILL (defeat the PC)
- **Attack** (mult 2-5) -- always carried. Standard icon damage -> crash -> dump shock.
- **Hog** (mult 3) -- virus; crashes the target's highest-rated running program each turn. Softener.
  Already implemented in `_enemy_decker_take_turn` + `hog_attack`.
- **Poison / Restrict / Reveal** (mult 3) -- cripplers vs Bod / Evasion / Masking (decker versions of
  Acid / Binder / Marker IC). Reveal is a force-multiplier: it lowers PC Masking -> lowers PC Detection
  Factor -> makes the PC *easier to keep hunting*.
- **Black Hammer** (mult 20, Physical) / **Killjoy** (mult 10, Stun) -- lethal biofeedback ("black IC
  from a decker"). Rating capped at `ceil(Computer skill / 2)`. Deadly-force (Red/Black) hosts only.

### SURVIVE (endure Strike Back so it can keep hunting)
- **Shield** (mult 4) -- parries the PC's counterattacks.
- **Armor** (mult 3) -- soaks icon damage.
- **Medic** (mult 4) -- heals its own icon to stay in the fight.
- **All three are NOT modeled on the enemy today** -- when the PC strikes back
  (`attack_enemy_decker`), the enemy defends with `shield_successes=0`, no armor soak, no self-heal.
  This is the single biggest realism gap.

### EXCLUDED (intruder-only -- a defender never carries these)
Analyze, Browse, Crash, Decrypt, Defuse, Evaluate, Mirrors, Read/Write, Relocate, Spoof, Validate,
Compressor, Commlink, Slow (anti-IC), Steamroller (anti-tar).
`Deception` is currently in the enemy's utility dict but is **vestigial** (a home-turf decker is
authorized) -- drop it or repurpose it.

---

## 4. Standard loadout by tier

| Tier | HUNT | KILL | SURVIVE |
|---|---|---|---|
| **Blue** | Scanner, Sleaze | Attack | -- |
| **Green** | Scanner, Sleaze | Attack, Hog | -- |
| **Orange** | Scanner, Sleaze | Attack, Hog, Reveal | Shield, Armor |
| **Red** | Scanner, Sleaze, (Track) | Attack, Hog, Reveal, Poison, **Black Hammer** | Shield, Armor, Medic |
| **Black** | Scanner, Sleaze, Track | Attack, Hog, Reveal, Poison, Restrict, **Black Hammer**, **Killjoy** | Shield, Armor, Medic |

---

## 5. Rating ranges (ACIFS-style variation)

Mirrors the host ACIFS approach (vr2 host subsystem ranges like `1D3 + 7`). Each program/stat rolls
**per-instance** inside its tier band, so two Red deckers differ without either exceeding the tier
ceiling.

**Anchor decision (proposed): current fixed values become the CEILING of each band.** Difficulty
never creeps upward vs today -- variation only softens some deckers. (Alternative: center the band on
today's value. User to confirm.)

**Hard caps that must always hold:** every program rating `<= MPCP`; Black Hammer / Killjoy
`<= ceil(Computer skill / 2)`; attribute floors `>= 1`.

| Stat / Program | Blue | Green | Orange | Red | Black |
|---|---|---|---|---|---|
| MPCP | 3-4 | 5-6 | 6-7 | 8-9 | 10-12 |
| Computer skill | 3-4 | 4-5 | 5-6 | 7-8 | 9-10 |
| Persona (Bod/Evasion/Masking/Sensor) | 2-3 | 3-4 | 4-5 | 5-6 | 6-7 |
| Attack | 2-3 | 4-5 | 5-6 | 7-8 | 9-10 |
| Hog | -- | 3-4 | 4-5 | 5-6 | 6-8 |
| Reveal | -- | -- | 4-5 | 5-6 | 6-7 |
| Poison | -- | -- | -- | 5-6 | 6-7 |
| Restrict | -- | -- | -- | -- | 6-7 |
| Black Hammer | -- | -- | -- | 3-4 | 4-5 |
| Killjoy | -- | -- | -- | -- | 4-5 |
| Sleaze | 2-3 | 3-4 | 4-5 | 5-6 | 6-7 |
| Scanner | 2-3 | 3-4 | 4-5 | 5-6 | 6-7 |
| Shield | -- | -- | 3-4 | 4-5 | 5-6 |
| Armor | -- | -- | 3-4 | 4-5 | 5-6 |
| Medic | -- | -- | -- | 3-4 | 4-5 |
| Track | -- | -- | -- | 4-5 | 5-6 |

Roll each band with an ACIFS-style formula (e.g. `low + randint(0, span)` -- a `1D2`/`1D3`-style pick),
using a **local** `random.Random` or the module `random` already imported in `matrix_engine.py`.
Do NOT call `random.seed()` on the global RNG inside a request path (project rule).

### 5.1 Core decker stats (non-program bands)

A spawned decker needs a **full** stat block, not just programs -- Computer skill plus the deck/meat
stats that drive its tests and initiative. These formalize (and slightly extend) the per-instance
randomization `generate_enemy_decker` already does, so every dispatched decker is scaled to the host
tier but individually varied. Same anchor as section 5 (current fixed value = band ceiling).

| Stat | Blue | Green | Orange | Red | Black |
|---|---|---|---|---|---|
| MPCP (deck) | 3-4 | 5-6 | 6-7 | 8-9 | 10-12 |
| Computer skill | 3-4 | 4-5 | 5-6 | 7-8 | 9-10 |
| Bod / Evasion / Masking / Sensor (persona) | 2-3 | 3-4 | 4-5 | 5-6 | 6-7 |
| Intelligence | 3-4 | 4-5 | 5-6 | 5-6 | 7-8 |
| Quickness | 2-3 | 3-4 | 4-5 | 5-6 | 5-6 |
| Response Increase (`<= MPCP/4`) | 0 | 0-1 | 0-1 | 1-2 | 2-3 |
| Hardening | 0 | 0 | 0 | 0-1 | 1-2 |

- **MPCP / Computer / persona** repeat section 5's table (the deck stats that also cap program
  ratings) -- kept here so the full block is in one place.
- **Reaction is derived, not rolled:** `Reaction = ceil((Quickness + Intelligence) / 2) + 2 x RI`
  (the existing initiative model). Do not band it separately.
- **Deck mode** (hot/cool) and **reality filter** are already probabilistic in code and stay as-is
  (hot-chance Blue->Black `0.6 / 0.7 / 0.8 / 0.9 / 1.0`; reality-filter chance
  `0.0 / 0.1 / 0.25 / 0.5 / 0.75`).
- **Hardening** bands to Black `1-2` (user-approved 2026-07-04) -- elite Black deckers may exceed
  today's fixed ceiling of 1. All other tiers hold at today's values (Red `0-1`; Blue/Green/Orange 0).

---

## 6. Enemy decker spawn system (count-gated probabilistic auto-spawn)

Replaces the "authored-only" limitation from section 2. After **any** sheaf step activates, the host
rolls a tier-scaled chance to dispatch a security decker, capped per run so a host never floods the
Matrix.

### Spawn chance + per-run cap

| Tier | Chance per sheaf step | Per-run decker cap |
|---|---|---|
| Blue | 5% | 1 |
| Green | 10% | 1 |
| Orange | 15% | 1-2 |
| Red | 20% | 1-2 |
| Black | 25% | 2-3 |

- The chance is rolled **once each time a sheaf step fires**, for *any* step (IC step, alert step,
  even a bare step). At most **one** decker spawns per step, which paces them naturally.
- The **cap is the TOTAL** enemy deckers in the run from all sources. A `1-2` / `2-3` cap is rolled
  **once per run** (`randint(1, 2)` / `randint(2, 3)`) and stored in state (`enemy_decker_cap`) so it
  is stable for the whole run.
- Once `len(state["enemy_deckers"]) >= enemy_decker_cap`, the roll is skipped -- no more spawns.
- **The dormant authored `enemy_decker` path still works** and any such decker **counts toward the
  cap** (the cap counts `len(state["enemy_deckers"])` regardless of source). No host authors one today,
  so in practice this system is the sole spawner -- but a hand-authored decker, if ever added, needs no
  special-casing: it just occupies a cap slot.
- Skip the roll when the run has ended (e.g. the shutdown step) or on any step that itself ends the
  run.

### Each spawned decker

Built by `generate_enemy_decker` using the **band-based** programs (section 5) + core stats
(section 5.1). Every dispatched decker is tier-scaled but individually varied -- no two identical.

### Implementation sketch

- New table in `matrix_engine.py`:
  `_ENEMY_DECKER_SPAWN = {"Blue": {"chance": 0.05, "cap": (1, 1)}, "Green": {"chance": 0.10, "cap": (1, 1)}, "Orange": {"chance": 0.15, "cap": (1, 2)}, "Red": {"chance": 0.20, "cap": (1, 2)}, "Black": {"chance": 0.25, "cap": (2, 3)}}`.
- Roll the per-run cap once (in `_initial_state`, or lazily on the first sheaf activation) into
  `state["enemy_decker_cap"] = randint(*cap)`.
- **Factor the existing spawn body out of the `_activate_sheaf_step` `enemy_decker` branch** into a
  shared helper `_spawn_enemy_decker(state, security_code, *, name=None, intent=None)` (build via
  `generate_enemy_decker`, roll initiative, append to `enemy_deckers`, emit the GM-only
  `enemy_decker_injected` event). Both the authored branch and the new probabilistic path call it.
- New helper `_maybe_spawn_enemy_decker(state, security_code)` in `matrix_runs.py`, called after each
  activated step inside `_check_and_activate_sheaf`: if `len(enemy_deckers) < enemy_decker_cap` and
  `random.random() < _ENEMY_DECKER_SPAWN[code]["chance"]` and not `run_ended`, call
  `_spawn_enemy_decker`.
- RNG: use the module `random` already imported; do NOT `random.seed()` the global RNG in a request
  path (project rule). For tests, monkeypatch `random` (see `_ScriptedRandom` in the scenario suite).

### Redaction / player view

A freshly spawned decker starts hidden (GM-only `enemy_decker_injected`) and only becomes visible
via its own hunt reveal or the PC's Locate Decker -- unchanged from today. `_redact_enemy_decker`
must strip the new stat/utility fields (section 5.1 + defensive utilities) for players.

---

## 7. Implementation tasks (when approved)

1. **Range-based generation.** In `matrix_engine.py`, replace the fixed scalars in
   `_ENEMY_DECKER_TIERS` with `(min, max)` bands per sections 5 + 5.1, and update
   `generate_enemy_decker` to roll each program/stat within its band (respecting the MPCP and
   `ceil(skill/2)` caps). Keep the existing deck_mode/reality_filter randomization.
   Preserve the returned dict shape (`utilities`, `programs`, `intent`, `lethal_program`,
   `lethal_rating`, `condition_monitor`, etc.) so `_enemy_decker_take_turn` and `_redact_enemy_decker`
   keep working.

2. **Spawn system (section 6).** Add `_ENEMY_DECKER_SPAWN`, roll `enemy_decker_cap` once per run,
   factor out `_spawn_enemy_decker`, add `_maybe_spawn_enemy_decker`, and call it after each activated
   step in `_check_and_activate_sheaf`. Authored spawns must count toward the cap.

3. **Model enemy DEFENSIVE utilities on Strike Back.** In `attack_enemy_decker` (matrix_runs.py),
   feed the enemy's **Shield** into the PC's attack as `shield_successes` (a Shield Test), apply
   **Armor** to the enemy's damage resistance, and have the enemy consume/degrade these like the PC's
   do (Shield loses 1 rating/use, Armor loses 1 rating/damage). Add the enemy utilities to the loadout
   in section 4 and the ranges in section 5.

4. **Enemy self-heal + Track in the take-turn loop.** In `_enemy_decker_take_turn`, add a **Medic**
   self-heal option (heals its own icon boxes when wounded but not yet at the retreat threshold) and a
   **Track** hunt option for Red/Black. Balance vs the existing self-preservation "fled" branch:
   heal-and-stay when moderately hurt, flee when badly hurt (`persona_boxes >= _ENEMY_RETREAT_BOXES`).

5. **Drop/repurpose `deception`.** Remove the vestigial `deception` utility from the enemy dict (or
   repurpose it explicitly).

6. **Redaction.** Ensure any new fields (core stats, shield/armor/medic/track ratings) are stripped
   for players in `_redact_enemy_decker` -- the player should see only what Analyze/Scanner reveals.

7. **Tests.** Add coverage in `tests/test_vr2_matrix_scenarios.py` and/or `tests/test_matrix_engine.py`:
   generation stays within bands and caps across all tiers; two generated deckers of the same tier can
   differ; enemy Shield/Armor actually reduce PC Strike Back damage; Medic heals; program caps never
   exceeded; **spawn: chance fires per step, never exceeds `enemy_decker_cap`, authored deckers count
   toward the cap, no spawn after run end** (monkeypatch `random`).

## 8. Open questions for the user (resolve before implementation)

- **Anchor:** current values as the band CEILING (proposed) or band CENTER?
- **Track:** worth modeling now, or defer (it mainly matters for post-jack-out pursuit, which this app
  may not simulate yet)?
- **Loadout edits:** any programs to add/remove per tier before this is coded?

_Resolved:_ Hardening bands to Black `1-2` (2026-07-04). The spawn-interaction / double-spawn question
is dropped -- no host authors a decker today, and the per-run cap counts `len(enemy_deckers)` from all
sources, so a hand-authored decker (if ever added) just consumes a cap slot with no special-casing.
