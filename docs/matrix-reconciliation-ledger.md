# VR2 Matrix Reconciliation Ledger

Human-readable mirror of the machine-checked scope in
[tests/matrix_scope_ledger.py](../tests/matrix_scope_ledger.py). That module is the
source of truth; this file is generated-by-hand to match it and is kept in sync. If the
two disagree, the `.py` wins and the contract test
([tests/test_matrix_reconciliation.py](../tests/test_matrix_reconciliation.py)) fails.

**Scope surfaces:** 30 programs, 10 program options, 19 IC, 12 host mechanics.
**Boundary:** 11 explicit exclusions (below) make "no gaps" provable against a defined scope.
**Status:** all reconciliation contract + numeric-oracle tests green; all 4 divergences
resolved (`status='fixed'`) -- see [the report](matrix-reconciliation-report.md).

The five requirements proven for every in-scope item:

| # | Requirement | Proven by |
|---|-------------|-----------|
| 1 | PRESENT in schema/catalog | `test_req1_*` -- ledger == `DeckerUtilities` / `ProgramOptions` / `IC_CATALOG`, and == the deck-workshop builder |
| 2 | REACHABLE via endpoint + UI control | `test_req2_*` -- every config field + invoke control found in `matrix-run.html`; every `ActionType` reachable or documented |
| 3 | CORRECT (success AND failure) vs a cited VR2 rule | `test_matrix_numeric_oracle.py` -- 25 engine primitives executed with scripted dice, both outcomes |
| 4 | ONE shared resolver per actor | `test_req4_*` -- shared seam primitives are single symbols; every exception is a pinned divergence |
| 5 | GUARDED against future gaps | `test_req5_*` -- a new builder entry cannot appear without a ledger row; every resolver must have an oracle row |

Actors that may share a mechanic (requirement 4): `pc_decker`, `enemy_decker`, `ic`, `dinab`.

VR2 line references point into [vr2_rules.md](../vr2_rules.md).

---

## 1. Programs (30)

`cfg` = run-UI config field id in `matrix-run.html`. `invoke` = the control that fires it
(`[]` = passive/automatic, proven reachable by the config field alone). `resolver` = engine
primitive in [app/services/matrix_engine.py](../app/services/matrix_engine.py) (or
`system_test`, the shared TN-reducer, or `passive`).

### Operational (12) -- all resolve through the shared `system_test` (except as noted)

| Program | slot | cfg | invoke | resolver | VR2 |
|---------|------|-----|--------|----------|-----|
| Analyze | analyze | cfg-u-analyze | console `analyze_ic` | system_test | 1447 |
| Crash | crash | cfg-u-crash | console `crash_host` | system_test | 1447 |
| Defuse | defuse | cfg-u-defuse | console `defuse_data_bomb` | data_bomb_defuse | 1447 |
| Deception | deception | cfg-u-deception | raw `doLogon` | system_test | 1447 |
| Decrypt | decrypt | cfg-u-decrypt | console `decrypt_file` | scramble_decrypt_test | 1447 |
| Disinfect | disinfect | cfg-u-disinfect | console `disinfect` | disinfect_test | 1447 |
| Evaluate | evaluate | cfg-u-evaluate | console `locate_paydata` | system_test | 1447 |
| Mirrors | mirrors | cfg-u-mirrors | console `decoy` | system_test | 1447 |
| Read/Write | read_write | cfg-u-read-write | console `download_data` | system_test | 1447 |
| Relocate | relocate | cfg-u-relocate | console `relocate` | system_test | 1447 |
| Scanner | scanner | cfg-u-scanner | console `locate_decker` | pc_locate_decker_test | 1447 |
| Validate | validate_pgm | cfg-u-validate | console `validate_passcode` | system_test | 1447 |

### Special (2)

| Program | slot | cfg | invoke | resolver | VR2 |
|---------|------|-----|--------|----------|-----|
| Compressor | compressor | cfg-u-compressor | console `decompress_file` | passive (size math) | 1510 |
| Sleaze | sleaze | cfg-u-sleaze | (passive) | detection_factor | 1510 |

### Offensive (10)

| Program | slot | cfg | invoke | resolver | VR2 |
|---------|------|-----|--------|----------|-----|
| Attack | attack | cfg-u-attack | endpoint `/attack` | cybercombat_attack | 2010 |
| Black Hammer | black_hammer | cfg-u-black-hammer | enemy_opt `black_hammer` | black_attack | 1526 |
| Hog | hog | cfg-u-hog | enemy_opt `hog` | hog_attack | 1526 |
| Killjoy | killjoy | cfg-u-killjoy | enemy_opt `killjoy` | black_attack | 1526 |
| Lock-On | lock_on | cfg-u-lock-on | (passive) | maneuver_test | 1587 |
| Poison | poison | cfg-u-poison | enemy_opt `poison` | attribute_attack_core | 1526 |
| Restrict | restrict | cfg-u-restrict | enemy_opt `restrict` | attribute_attack_core | 1526 |
| Reveal | reveal | cfg-u-reveal | enemy_opt `reveal` | attribute_attack_core | 1526 |
| Slow | slow | cfg-u-slow | console `slow` | slow_test | 1526 |
| Steamroller | steamroller | cfg-u-steamroller | console `steamroller` | steamroller_attack | 1526 |

### Defensive (6)

| Program | slot | cfg | invoke | resolver | VR2 |
|---------|------|-----|--------|----------|-----|
| Armor | armor | cfg-u-armor | (passive) | damage_resistance | 1587 |
| Camo | camo | cfg-u-camo | (passive) | passive (raises Trace TN) | 1587 |
| Cloak | cloak | cfg-u-cloak | (passive) | maneuver_test | 1587 |
| Medic | medic | cfg-u-medic | console `medic` | medic_heal | 1587 |
| Restore | restore | cfg-u-restore | console `restore` | restore_repair | 1587 |
| Shield | shield | cfg-u-shield | (passive) | shield_parry | 1587 |

---

## 2. Program options (10)

`schema` = `ProgramOptions` field carried into the run (or build-time-only). `carried` =
read by the engine at run time.

| Option | schema field | carried | consumer | VR2 |
|--------|--------------|---------|----------|-----|
| area | area | yes | attack / area_attack: hit up to [Area] targets, offset TN penalty | 1629 |
| chaser | chaser | yes | attack: negates Shift penalty (Shield then +2) | 1629 |
| dinab | dinab | yes | DINAB: autonomous Free-action run at skill = rating | 1629 |
| limit | limit_target | yes | restrict a utility to one target type ('ic'/'decker') | 1629 |
| oneshot | one_shot | yes | single-use copy consumed on use (reload via Swap Memory) | 1629 |
| penetration | penetration | yes | attack: negates Shield penalty (Shift then +2) | 1629 |
| skulk | skulk | yes | crashing IC: reduce the tally increase by [Skulk] | 1629 |
| targeting | targeting | yes | attack: -2 to-hit TN | 1629 |
| optimization | (none) | no | build-time size/cost only (design x2.0, actual x0.5) | 1655 |
| squeeze | (none) | no | build-time upload compression only (decompress before use) | 1655 |

---

## 3. IC (19)

Catalog keys in `matrix_rules.IC_CATALOG`, buildable in
[frontend/matrix-designer.html](../frontend/matrix-designer.html).

| IC | group / role | resolver | VR2 |
|----|--------------|----------|-----|
| Probe | white / reactive | probe_test | 481 |
| Killer | white | cybercombat_attack | 439 |
| Acid | white / Crippler (Bod) | crippler_attack | 431 |
| Binder | white / Crippler (Evasion) | crippler_attack | 431 |
| Jammer | white / Crippler (Sensor) | crippler_attack | 431 |
| Marker | white / Crippler (Masking) | crippler_attack | 431 |
| Tar Baby | white / reactive | tar_baby_test | 497 |
| Data Bomb | host config (file/slave) | data_bomb_defuse | 457 |
| Scramble | host config (access/file/slave) | scramble_decrypt_test | 487 |
| Blaster | gray | cybercombat_attack | 517 |
| Sparky | gray | cybercombat_attack | 527 |
| Acid-rip | gray / Ripper (Bod) | crippler_attack | 523 |
| Bind-rip | gray / Ripper (Evasion) | crippler_attack | 523 |
| Jam-rip | gray / Ripper (Sensor) | crippler_attack | 523 |
| Mark-rip | gray / Ripper (Masking) | crippler_attack | 523 |
| Tar Pit | gray / reactive | tar_baby_test | 536 |
| Worm | host config (ACIFS) | worm_attack | 544 |
| Trace | gray / reactive | trace_hunt_cycle_attack | 560 |
| Black IC | black (Lethal + Non-Lethal) | black_attack | 603 |

---

## 4. Host mechanics (12)

`schema` = Pydantic symbol proving it is modelled; `handler` = engine/router symbol that
resolves or tabulates it; `endpoint` = run endpoint that exercises it. Symbol existence is
asserted by `test_req1_host_mechanic_symbols_exist`.

| Mechanic | schema | handler | endpoint | VR2 |
|----------|--------|---------|----------|-----|
| security_code_value | SheaveSaveInput.security_code | rules.COMBAT_TN | start_run | 258 |
| acifs_ratings | SheaveSaveInput.acifs | rules.HOST_DIFFICULTY | perform_action | 35 |
| sheaf_steps_triggers | SheafStep.trigger | _activate_sheaf_step | new_turn | 817 |
| alerts | SheafEvent.type | rules.SHEAF_ALERT_TABLE | new_turn | 835 |
| scramble_ic | SheafEvent.type | eng.scramble_failure_consequence | perform_action | 487 |
| data_bomb | SheafEvent.type | eng.data_bomb_detonate | perform_action | 457 |
| worm_ic | SheafEvent.type | eng.worm_attack | perform_action | 544 |
| trap_ic | SheafEvent.surface_ic_type | _activate_sheaf_step | new_turn | 684 |
| constructs_party_ic | SheafEvent.components | _activate_sheaf_step | new_turn | 718 |
| bouncer | SheafEvent.new_security_code | _activate_sheaf_step | new_turn | 300 |
| trap_doors | RunTrapDoorInput.action | trap_door_action | trap_door_action | 312 |
| paydata_economy | SheaveSaveInput.acifs | rules.PAYDATA_TABLE | perform_action | 986 |

---

## 5. Numeric-oracle coverage (requirement 3)

[tests/test_matrix_numeric_oracle.py](../tests/test_matrix_numeric_oracle.py) executes
each resolver in-process with a scripted d6 stream (`_ScriptedD6`) and asserts the exact
result in **success and failure** against the cited VR2 rule. 25 engine primitives are
covered:

`roll_dice`, `system_test`, `detection_factor`, `damage_resistance`, `cybercombat_attack`,
`black_attack`, `attribute_attack_core`, `crippler_attack`, `hog_attack`, `medic_heal`,
`restore_repair`, `shield_parry`, `maneuver_test`, `slow_test`, `steamroller_attack`,
`tar_baby_test`, `data_bomb_defuse`, `data_bomb_detonate`, `worm_attack`, `disinfect_test`,
`scramble_decrypt_test`, `probe_test`, `trace_hunt_cycle_attack`, `pc_locate_decker_test`,
`hog_purge_test`.

Passive programs with no dice test of their own are proven separately:
`Camo` (raises the Trace Detection Factor TN) and `Compressor` (halves stored file size via
`mr._compressed_store_size`). `test_req5_every_program_has_a_numeric_proof` /
`test_req5_every_ic_has_a_numeric_proof` require every non-passive resolver to have an
oracle row, so a new resolver cannot ship without a numeric proof.

---

## 6. Exclusions (11) -- the provable boundary

Everything below is deliberately OUT of scope. The union of (in-scope surfaces) and
(exclusions) is what makes "no gaps" auditable.
`test_req5_excluded_items_are_truly_absent_from_the_builder` proves the excluded
programs/options are genuinely not buildable.

| Excluded | kind | rationale (short) | VR2 |
|----------|------|-------------------|-----|
| Sensitive (option) | option | not offered by the deck workshop (absent from OPTION_DEFS) | 1629 |
| Browse (program) | program | data discovery folded into Locate Paydata + Analyze | 1447 |
| Commlink (program) | program | no comm-relay play in the run engine | 1447 |
| Spoof (program) | program | slave-spoof operations not modelled | 1447 |
| Invalidate Passcode (half) | program | only the Validate half is modelled | 1447 |
| Locate File (program) | program | folds into Locate Paydata / Analyze Subsystem | 1447 |
| Track (program) | program | PC-side trace-back play out of scope | 1447 |
| Frames | actor | Frames not modelled as run actors; DINAB covers single-program autonomy | 1694 |
| Worm sub-variants (Data/Death/Tapeworm) | variant | flavor only; `worm_attack` resolves all worms identically | 544 |
| Psychotropic Black IC | variant | not a separate buildable option; both Black IC types use black_attack | 649 |
| UV Hosts / Reality Filters / Command Sets | feature | advanced systems with no builder surface / run control | 383 |

---

## 7. Divergences (4, all fixed) + fixed gaps

Full detail, VR2 citations, and the resolutions are in
[matrix-reconciliation-report.md](matrix-reconciliation-report.md). All four have been
ruled on and set to `status='fixed'` (each with a `resolution` note in `DIVERGENCES`).
Summary:

| id | kind | location | resolution |
|----|------|----------|------------|
| dinab_attack_ic_bypass | shared_resolver | `_dinab_attack_ic` | routed through `eng.cybercombat_attack` (`attacker_is_ic=False`) |
| area_attack_cybercombat_bypass | shared_resolver | `area_attack` | per-target damage via `eng.damage_resistance` + `_enemy_shield_parry`; single shared Attack Test kept per vr2 L1663 |
| bouncer_inert | buildable_not_resolved | `_activate_sheaf_step` | `SheafEvent.new_security_*` fields + `bouncer` branch upgrade host security; now a `HOST_MECHANICS` row + `TestBouncer` proof |
| logon_to_ltg_unsurfaced | backend_only | `ActionType` | vestigial action retired; documented in `test_coverage_matrix.py` |

**Also fixed this pass (pure wiring gap, per remediation policy):**
`purge_hog` -- fully-implemented backend action (`perform_action` `purge_hog` branch,
`eng.hog_purge_test`) had no run-UI control. Added a gated "Purge Hog" `ACTION_CATALOG`
entry in `matrix-run.html`; the reachability test now enforces its presence.
