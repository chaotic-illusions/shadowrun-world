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
- **The `enemy_decker` event handler is dormant -- nothing produces it, and it is being REMOVED.** The
  branch in `_activate_sheaf_step` (~L1074) fires only if a step literally contains
  `{"type": "enemy_decker"}`, but: `_generate_sheaf_impl` (matrix_engine.py ~L573) emits only IC /
  passive_alert / active_alert / shutdown; `world_seed.json` has **zero** enemy_decker entries; the
  `SheafEvent` schema (schemas/matrix_run.py ~L217) doesn't advertise the type (and drops the
  `name`/`intent` fields the handler reads); and no host/sheaf UI exposes it. **There is no
  hand-authored / GM-derived decker and there never will be** -- every decker is generated
  programmatically from ratings + dice (sections 5-6). The dead authored branch, its
  `enemy_decker_injected` "GM:" log wording, and the free-string escape hatch are all removed during
  implementation (task 2). **In normal play today no host spawns a decker at all.**
- **Stats scale to the TIER, not the host's number.** `security_code` (the color) picks the tier band;
  `security_value` (the number) does **not** touch MPCP/skill/program ratings. (Today's code caps them
  with `min(tier, security_value)` -- that cap is REMOVED, task 1. Nothing in SR2/VR2 ties a decker's
  MPCP or Computer skill to the host rating; a skilled decker can patrol a soft host.) Program ratings
  are also currently **fixed** -> every Red decker is a carbon copy of every other Red decker.

> **DECIDED (2026-07-03 / refined 2026-07-04):** add a **count-gated probabilistic spawn system** --
> see section 6. It is the **sole** spawner: after *any* sheaf step fires, the host rolls a tier-scaled
> chance to dispatch a fully-programmatic decker, capped per run. There is **no** hand-authored path to
> keep alive -- the dormant `enemy_decker` sheaf branch is deleted, not preserved (task 2).

---

## 3. Program deep-dive -- the three jobs

### HUNT (find the PC)
- **Scanner** (mult 3) -- lowers the TN on Locate Decker. Already used by `enemy_locate_test`.
- **Sleaze** (mult 3) -- passive; raises the enemy's own Detection Factor so the PC's
  `pc_locate_decker_test` (vs enemy Masking + Sleaze) is harder. Lets it lurk / ambush.
- ~~**Track**~~ -- **DROPPED (2026-07-04).** Once the PC or the enemy jacks out this app treats them
  as gone, so post-jack-out pursuit never matters. Not modeled, not carried by any tier.

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

### 3.1a Enemy deckers SEE THROUGH Validate Passcode (DECIDED 2026-07-04)

A PC's Validate Passcode plants a fake passcode that flips the PC to `legitimate` status
(`state["has_legitimate_status"]`), which swaps the attacker's `COMBAT_TN` column. Against a **skilled
human-equivalent hunter this does nothing** -- an enemy decker recognizes the intruder for what they
are and **always** attacks on the `intruding` column. This is already the code's behavior: every enemy
attack in `_enemy_decker_take_turn` passes `target_status="intruding"` hardcoded (icon attack
~L5570, crippler ~L5555). **KEEP it hardcoded** -- do NOT wire enemy-decker attacks to
`has_legitimate_status`. (Contrast: dumb **IC** still respects the fake passcode -- the IC path reads
`has_legitimate_status` at ~L3498 -- so Validate Passcode remains useful against IC but is worthless
against a decker. A nice built-in asymmetry, not a bug.)

Corollary of the corrected `COMBAT_TN` table (Red/Black intruding now 3): against a Red/Black enemy
decker the PC is hit on TN 3 whether or not they Validate -- so on the deadliest hosts a passcode
already can't help vs a decker for two independent reasons (decker ignores it AND the column barely
differs there).

### 3.1 Combat maneuvers -- ALREADY IMPLEMENTED for enemy deckers (verified 2026-07-04)

Enemy deckers (and IC) already INITIATE VR2 combat maneuvers -- this is **done**, no new work is
needed here beyond the Medic balancing in task 4. Both use the same heuristic:

- `_npc_maybe_maneuver(state, decker, eff, actor, *, is_ic)` (matrix_runs.py ~L3079), gated by
  `state["npc_combat_maneuvers"]` (fresh runs set it True in `_initial_state` ~L479; legacy/test
  states without the flag get no NPC maneuvers). Called for enemy deckers at ~L5500 (`is_ic=False`)
  and for IC at ~L3507 (`is_ic=True`). Resolution is `_resolve_npc_maneuver` -> `eng.maneuver_test`
  (Evasion-vs-Sensor opposed test; a decker maneuvers on its **Evasion** attribute).
- Deterministic priority by the actor's own icon damage (persona boxes):
  1. `boxes >= 7` -> **Evade Detection** (break contact, drop off the PC's sensors).
  2. `4 <= boxes <= 6` (no parry yet) -> **Parry Attack** (+net TN to the PC's next attack on it).
  3. `boxes <= 3` and the PC is already hurt (`pc_persona >= 2`, no position yet) -> **Position
     Attack** (-net TN on its next attack on the PC).

**Interaction with the new wounded-decker AI (section 3.2):** for enemy deckers the wounded logic in
`_enemy_decker_take_turn` (nerve-check flee + evade-to-heal) runs BEFORE `_npc_maybe_maneuver`, so the
shared maneuver's own `boxes >= 7` Evade branch is effectively IC-only for deckers. The generic Parry
(4-6) / Position (`<= 3`, PC hurt) branches still apply to a decker that chooses to stand and fight.

---

## 3.2 Wounded enemy-decker behavior (REPLACES the hard 7-box flee)

Today a decker jacks out the instant its icon hits `_ENEMY_RETREAT_BOXES = 7` -- a hard cutoff, so you
only ever need 7 boxes to make ANY decker leave and they all behave identically. This replaces that
with a graduated, individual model: an escalating nerve check, plus a hide-heal-return loop for
Medic-carriers.

**Per-instance bravery (nerve).** Each decker rolls a `bravery` value at generation (section 5.1),
tier-scaled so elite deckers hold their nerve longer. Higher bravery lowers its flee chance.

**Escalating nerve-check flee (7/8/9 -> 10 dumped).** Instead of a hard cutoff, when a wound first
pushes the icon to 7, 8, or 9 persona boxes the decker makes ONE nerve check at that threshold:

| Persona boxes | Base flee chance (before bravery) |
|---|---|
| 7 | 30% |
| 8 | 55% |
| 9 | 80% |
| 10 | dumped -- forced out (not a choice) |

- `flee_chance = clamp(base - 0.15 x bravery, 0.05, 0.95)`.
- Checked **once per newly-reached threshold** -- track `nerve_checks_done` on the enemy so a decker
  sitting at 7 boxes isn't re-rolled every turn; only a fresh wound to a new threshold triggers a check.
- On a failed nerve (flee): permanent jack-out (`status = "fled"`) -- the same terminal behavior as
  today, but now probabilistic and per-decker. A timid Blue decker usually bails at 7-8; a disciplined
  Black decker often fights into the 9-10 zone (some to the dump at 10).

**Hide-heal-return loop (Medic-carriers = Red/Black only).** A decker that HOLDS its nerve and carries
Medic doesn't just trade blows to the death -- it tactically disengages, heals, and comes back:

1. **Break contact:** when visible and `persona_boxes >= _ENEMY_WOUNDED_BOXES` (proposed 5) and the
   nerve check did not flee, it spends its action on **Evade Detection** to go hidden (drop off the
   PC's sensors) instead of attacking.
2. **Heal while hidden:** on its turns while hidden it runs **Medic** on its own icon (healing is not
   an attack, so it does NOT break the hide). This requires relaxing the current
   `if _evade_active(state, enemy): return` guard at the top of `_enemy_decker_take_turn` so a hidden
   Medic-carrier may still self-heal.
3. **Re-engage:** once healed to `persona_boxes <= _ENEMY_REENGAGE_BOXES` (proposed 3) it voluntarily
   clears its own evade (`_clear_evade(state, enemy, redetected=False)`) and resumes hunting/attacking
   next turn. If the PC re-detects it first (Locate Decker / timer) it is revealed again and re-decides
   (fight, re-hide, or flee) by the same rules.

**Non-Medic deckers (Blue/Green/Orange)** can't heal, so they have no hide-return loop: they stand and
fight, and the escalating nerve check alone decides when they bail. (A healless Evade only delays, so
the `boxes >= 7` maneuver Evade branch should be gated to Medic-carriers for deckers, or they simply
prefer Parry/attack.)

**Constants:** `_ENEMY_RETREAT_BOXES = 7` (hard flee) is REMOVED, replaced by the flee-chance table
above; add `_ENEMY_WOUNDED_BOXES` (evade-to-heal trigger, ~5) and `_ENEMY_REENGAGE_BOXES` (re-engage
heal target, ~3). `_apply_medic` (matrix_runs.py ~L1306) is PC-scoped (run-level condition_monitor);
the enemy needs a mirror that heals `enemy["condition_monitor"]["persona_boxes"]` via
`eng.medic_heal(medic_rating, wound_level)` using the enemy's own Medic rating and degrades it 1/use.

---

## 4. Standard loadout by tier

SURVIVE is **additive** up the tiers: Armor (Green) -> +Shield (Orange) -> +Medic (Red, and Black).

| Tier | HUNT | KILL | SURVIVE |
|---|---|---|---|
| **Blue** | Scanner, Sleaze | Attack | -- |
| **Green** | Scanner, Sleaze | Attack, Hog | Armor |
| **Orange** | Scanner, Sleaze | Attack, Hog, Reveal | Armor, Shield |
| **Red** | Scanner, Sleaze | Attack, Hog, Reveal, Poison, **Black Hammer** | Armor, Shield, Medic |
| **Black** | Scanner, Sleaze | Attack, Hog, Reveal, Poison, Restrict, **Black Hammer**, **Killjoy** | Armor, Shield, Medic |

---

## 5. Rating ranges (ACIFS-style variation)

Mirrors the host ACIFS approach (vr2 host subsystem ranges like `1D3 + 7`). Each program/stat rolls
**per-instance** inside its tier band, so two Red deckers differ.

**Bands are tier-only (decoupled from `security_value`).** The tier (Blue..Black, from the host's
`security_code`) is the ONLY input to the bands -- the host's numeric rating (`security_value`) has
ZERO effect on MPCP, Computer skill, or any program. A Red decker rolls the Red band whether it is
guarding a Red-4 or a Red-9 host. (This drops the current `min(tier, security_value)` cap -- see
task 1; the rules don't tie decker gear to host rating, and a good decker can watch a low host.)

**Anchor decision (RESOLVED 2026-07-04): today's fixed value is the CENTER of each band.** Variation
goes both ways -- a rolled decker may come out a step stronger OR weaker than today's fixed value
(clamped to the hard caps). Each band is `center - 1 .. center + 1` (a symmetric 1D3-style spread),
where `center` = the current `_ENEMY_DECKER_TIERS` value for stats that have one. (Rejected: the
"ceiling" model, which only ever softened deckers.)

**Hard caps that must always hold:** every program rating `<= MPCP`; Black Hammer / Killjoy
`<= ceil(Computer skill / 2)`; MPCP `<= 12` (canonical top-end deck -- a Black roll of 13 folds to 12);
attribute/program floors `>= 1`.

| Stat / Program | Blue | Green | Orange | Red | Black |
|---|---|---|---|---|---|
| MPCP | 3-5 | 5-7 | 6-8 | 8-10 | 11-13 |
| Computer skill | 3-5 | 4-6 | 5-7 | 7-9 | 9-11 |
| Persona (Bod/Evasion/Masking/Sensor) | 2-4 | 3-5 | 4-6 | 5-7 | 6-8 |
| Attack | 2-4 | 4-6 | 5-7 | 7-9 | 9-11 |
| Hog | -- | 3-5 | 4-6 | 5-7 | 6-8 |
| Reveal | -- | -- | 4-6 | 5-7 | 6-8 |
| Poison | -- | -- | -- | 5-7 | 6-8 |
| Restrict | -- | -- | -- | -- | 6-8 |
| Black Hammer | -- | -- | -- | 3-5 | 4-6 |
| Killjoy | -- | -- | -- | -- | 4-6 |
| Sleaze | 2-4 | 3-5 | 4-6 | 5-7 | 6-8 |
| Scanner | 2-4 | 3-5 | 4-6 | 5-7 | 6-8 |
| Armor | -- | 2-4 | 3-5 | 4-6 | 5-7 |
| Shield | -- | -- | 3-5 | 4-6 | 5-7 |
| Medic | -- | -- | -- | 3-5 | 4-6 |

(Bands are symmetric about today's value: e.g. Black MPCP center 12 -> 11-13 (folds to 12 by the cap);
Red Attack center 8 -> 7-9. `Hog/Reveal/Poison/Restrict` had no fixed rating before -- their centers are
assigned here, monotonic by tier. `Black Hammer/Killjoy` are additionally bounded by `ceil(skill/2)`,
which usually dominates.)

Roll each band as `center + randint(-1, +1)`, then clamp to `[1, cap]` (cap = MPCP for programs,
`ceil(skill/2)` for the lethal programs). Use the module `random` already imported in
`matrix_engine.py`; do NOT call `random.seed()` on the global RNG inside a request path (project rule).

### 5.1 Core decker stats (non-program bands)

A spawned decker needs a **full** stat block, not just programs -- Computer skill plus the deck/meat
stats that drive its tests and initiative. These formalize (and slightly extend) the per-instance
randomization `generate_enemy_decker` already does, so every dispatched decker is scaled to the host
tier but individually varied. Same anchor as section 5 (current fixed value = band CENTER).

| Stat | Blue | Green | Orange | Red | Black |
|---|---|---|---|---|---|
| MPCP (deck) | 3-5 | 5-7 | 6-8 | 8-10 | 11-13 |
| Computer skill | 3-5 | 4-6 | 5-7 | 7-9 | 9-11 |
| Bod / Evasion / Masking / Sensor (persona) | 2-4 | 3-5 | 4-6 | 5-7 | 6-8 |
| Intelligence | 3-5 | 4-6 | 5-7 | 5-7 | 7-9 |
| Quickness | 2-4 | 3-5 | 4-6 | 5-7 | 5-7 |
| Response Increase (`<= MPCP/4`) | 0-1 | 0-2 | 0-2 | 1-3 | 2-4 |
| Hardening (special-case, not centered) | 0 | 0 | 0 | 0-1 | 1-2 |
| Bravery / nerve (flee resistance) | 0-1 | 0-2 | 1-2 | 1-3 | 2-3 |

- **MPCP / Computer / persona** repeat section 5's table (the deck stats that also cap program
  ratings) -- kept here so the full block is in one place.
- **Reaction is derived, not rolled:** `Reaction = ceil((Quickness + Intelligence) / 2) + 2 x RI`
  (the existing initiative model). Do not band it separately.
- **Response Increase** is clamped to `[0, MPCP/4]` after the centered roll (vr2). **Hardening** and
  **Bravery** use the explicit bands above, NOT the generic center +-1 rule.
- **Deck mode** (hot/cool) and **reality filter** are already probabilistic in code and stay as-is
  (hot-chance Blue->Black `0.6 / 0.7 / 0.8 / 0.9 / 1.0`; reality-filter chance
  `0.0 / 0.1 / 0.25 / 0.5 / 0.75`).
- **Hardening** bands to Black `1-2` (user-approved 2026-07-04); Red `0-1`; Blue/Green/Orange `0`.
- **Bravery / nerve** (new -- drives section 3.2's escalating flee) is rolled once per decker,
  tier-scaled so elite deckers hold their nerve longer: `flee_chance = clamp(base - 0.15 x bravery, ...)`.

---

## 6. Enemy decker spawn system (count-gated probabilistic auto-spawn)

The sole enemy-decker spawner (there is no hand-authored path -- see section 2). After **any** sheaf
step activates, the host rolls a tier-scaled chance to dispatch a security decker, capped per run so a
host never floods the Matrix.

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
- Every decker in the run comes from this system (the authored path is deleted -- section 2 / task 2),
  so `len(state["enemy_deckers"])` is exactly the count this spawner has produced.
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
- **Create the shared spawn helper AND delete the dead authored branch.** Add
  `_spawn_enemy_decker(state, security_code, *, name=None)` (build via `generate_enemy_decker`, roll
  initiative, append to `enemy_deckers`, emit the GM-only `enemy_decker_injected` event) and route the
  new probabilistic path through it. **Remove** the `_activate_sheaf_step` `elif ev_type ==
  "enemy_decker"` branch (~L1074) and its `ev.get("name")`/`ev.get("intent")` reads -- nothing produces
  that event and nothing ever will.
- New helper `_maybe_spawn_enemy_decker(state, security_code)` in `matrix_runs.py`, called after each
  activated step inside `_check_and_activate_sheaf`: if `len(enemy_deckers) < enemy_decker_cap` and
  `random.random() < _ENEMY_DECKER_SPAWN[code]["chance"]` and not `run_ended`, call
  `_spawn_enemy_decker`.
- RNG: use the module `random` already imported; do NOT `random.seed()` the global RNG in a request
  path (project rule). For tests, monkeypatch `random` (see `_ScriptedRandom` in the scenario suite).

### Redaction / player view

A freshly spawned decker starts hidden (GM-only `enemy_decker_injected`) and only becomes visible
via its own hunt reveal or the PC's Locate Decker -- unchanged from today. `_redact_enemy_decker`
must strip the new fields (section 5.1 core stats, `bravery`, `nerve_checks_done`, and the
shield/armor/medic ratings) for players.

---

## 7. Implementation tasks (when approved)

1. **Range-based generation (CENTERED bands, TIER-ONLY).** In `matrix_engine.py`, replace the fixed
   scalars in `_ENEMY_DECKER_TIERS` with per-tier CENTERS (or `(min, max)` bands) per sections 5 + 5.1,
   and update `generate_enemy_decker` to roll each program/stat as `center + randint(-1, +1)` clamped to
   `[1, cap]` (cap = MPCP for programs, `ceil(skill/2)` for the lethal programs; MPCP itself clamped to
   12). **Delete the `security_value` cap** (`skill = min(tier["skill"], max(3, security_value))` /
   same for `mpcp`, ~L1048-1049) -- MPCP and Computer skill come from the tier band alone; keep the
   `security_value` parameter only for the decker's display name and any host-tally logic that already
   uses it. Add the per-instance `bravery` roll (section 5.1) to the returned dict. Keep the existing
   deck_mode/reality_filter randomization. Preserve the returned dict shape (`utilities`, `programs`,
   `intent`, `lethal_program`, `lethal_rating`, `condition_monitor`, etc.) so `_enemy_decker_take_turn`
   and `_redact_enemy_decker` keep working, and drop the "the GM decides whether to inject one"
   docstring language -- spawns are automatic now.

2. **Spawn system (section 6) + delete the authored path.** Add `_ENEMY_DECKER_SPAWN`, roll
   `enemy_decker_cap` once per run, add `_spawn_enemy_decker` + `_maybe_spawn_enemy_decker`, and call
   the latter after each activated step in `_check_and_activate_sheaf`. **Remove** the dead
   `_activate_sheaf_step` `enemy_decker` branch (~L1074); the `enemy_decker` type never needs adding to
   the `SheafEvent` schema. This spawner is the only source of enemy deckers.

3. **Model enemy DEFENSIVE utilities on Strike Back.** In `attack_enemy_decker` (matrix_runs.py),
   feed the enemy's **Shield** into the PC's attack as `shield_successes` (a Shield Test), apply
   **Armor** to the enemy's damage resistance, and have the enemy consume/degrade these like the PC's
   do (Shield loses 1 rating/use, Armor loses 1 rating/damage). Add the enemy utilities to the loadout
   in section 4 and the ranges in section 5.

4. **Wounded enemy-decker AI (section 3.2).** In `_enemy_decker_take_turn`, replace the hard
   `persona_boxes >= _ENEMY_RETREAT_BOXES` flee with: (a) the escalating nerve-check flee at 7/8/9
   boxes (once per newly-reached threshold via `nerve_checks_done`, `flee_chance = clamp(base - 0.15 x
   bravery, 0.05, 0.95)`, 10 = dumped); (b) a **Medic** self-heal mirror of `_apply_medic` that heals
   the enemy's own `condition_monitor`; and (c) the hide-heal-return loop for Medic-carriers -- Evade
   Detection at `>= _ENEMY_WOUNDED_BOXES`, heal while hidden (relax the `_evade_active` early-return so
   a hidden carrier can still Medic), re-engage at `<= _ENEMY_REENGAGE_BOXES`. Remove
   `_ENEMY_RETREAT_BOXES`; add `_ENEMY_WOUNDED_BOXES` / `_ENEMY_REENGAGE_BOXES`. Combat maneuvers
   themselves need NO new work (done -- section 3.1); just order the wounded logic before
   `_npc_maybe_maneuver`.

5. **Drop/repurpose `deception`.** Remove the vestigial `deception` utility from the enemy dict (or
   repurpose it explicitly).

6. **Redaction.** Ensure any new fields (core stats, `bravery`, `nerve_checks_done`, shield/armor/medic
   ratings) are stripped for players in `_redact_enemy_decker` -- the player should see only what
   Analyze/Scanner reveals.

7. **Tests.** Add coverage in `tests/test_vr2_matrix_scenarios.py` and/or `tests/test_matrix_engine.py`:
   generation stays within the centered bands and caps across all tiers; two generated deckers of the
   same tier can differ; enemy Shield/Armor actually reduce PC Strike Back damage; Medic heals; program
   caps never exceeded; **spawn: chance fires per step, never exceeds `enemy_decker_cap`, no spawn after
   run end**; **wounded AI: nerve-check flee escalates 7->8->9 and is checked once per threshold, higher
   bravery flees less, a Medic-carrier hides + heals + re-engages, 10 boxes = dumped** (monkeypatch
   `random`).

## 8. Open questions for the user (resolve before implementation)

_None outstanding -- all design questions are resolved._

_Resolved (2026-07-04):_
- **No `security_value` cap on MPCP/skill.** Bands are TIER-only (`security_code`); the host's number
  never scales the decker. Drops today's `min(tier, security_value)` cap (task 1) -- a skilled decker
  can patrol a low-value host. The only stat the value still informs is the display name / host tally.
- **Anchor: CENTERED.** Today's fixed value is the band CENTER (`center +-1`, clamped to caps), so a
  decker can roll a step above or below today -- rejected the ceiling model. Bands in sections 5 + 5.1
  recomputed accordingly.
- **No hand-authored / GM-derived decker -- ever.** Every decker is generated programmatically from
  ratings + dice. The dormant `_activate_sheaf_step` `enemy_decker` branch is DELETED (task 2), and the
  probabilistic spawner (section 6) is the sole source. All "authored path counts toward the cap"
  language is removed.
- **Wounded AI reworked (section 3.2):** the hard 7-box flee is replaced by an escalating nerve check
  at 7/8/9 boxes (-> 10 = dumped), softened by a per-instance `bravery` roll, plus a hide-heal-return
  loop for Medic-carriers (Red/Black) so a decker can Evade, heal, and re-attack. Makes each decker feel
  individual (some fight to the death).
- **Track: DROPPED entirely.** Once the PC or the enemy jacks out this app treats them as gone, so
  post-jack-out pursuit never matters. Removed from every loadout/range table and the take-turn tasks.
- **Loadout edits:** SURVIVE is now additive -- Green `Armor`; Orange `+Shield`; Red/Black `+Medic`
  (all three). Green Armor centered band `2-4`. KILL/attack programs unchanged.
- **Combat maneuvers already exist** for BOTH IC and enemy deckers (`_npc_maybe_maneuver`, section
  3.1). No new maneuver work.
- **Hardening** bands to Black `1-2`; Red `0-1`; others `0` (explicit, not centered).
