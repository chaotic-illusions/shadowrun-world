# Matrix 2.0 -- VR2 Test Matrix Progress Notes

Started 2026-05-31, branch `matrix2`. Tracks the #1-#11 test matrix. Depth per decision:
**targeted + representative** (validate cost/size math + cumulative reductions across a
representative sample + all option types/key combos, not literally every combination).
Missing features: **build them**. Each validated fix/test committed locally.

Test server: isolated `:8770`, throwaway DB `data/_e2e_sess2.db`, decker **Nightlife**.
Never touches the real `:8000` instance.

> Env note (important for re-runs): background-Bash `python` is NOT on PATH (exit 127).
> Launch the test server via the venv python through PowerShell `Start-Process`
> (`.venv\Scripts\python.exe -m uvicorn app.main:app --port 8770`, with
> `DATABASE_URL`/`BOOTSTRAP_ADMIN_KEY` set in the PS session). Setup scripts MUST send the
> created admin token on EVERY call -- the bootstrap key stops working the instant the first
> admin token exists.

---

## Status legend
- [DONE] validated (test green or browser-confirmed)
- [PARTIAL] core validated; sub-item or UI pass remains
- [TODO] not yet started
- [GAP] feature/behaviour missing -> to build

---

## #1 Every IC type vs the decker -- [DONE] (engine), [TODO] (stacked browser pass)
- `tests/test_vr2_matrix_scenarios.py::TestEveryICType` -- catalog has all **19** canonical
  IC (Probe, Killer, Acid, Binder, Jammer, Marker, Tar Baby, Data Bomb, Scramble, Blaster,
  Sparky, Acid-rip, Bind-rip, Jam-rip, Mark-rip, Tar Pit, Worm, Trace, Black IC); each
  activates into run state (proactive -> active_ic; Tar Baby/Tar Pit -> lurking_ic); cripplers/
  rippers declare a target attribute; multiple IC stack in active_ic.
- Per-IC combat math (Killer/Blaster/Sparky cybercombat, crippler reduction, ripper chip,
  probe tally, trace hunt) already green in `tests/test_matrix_engine.py`.
- Cumulative crippler effects: `TestCumulativeCripplerEffects` -- two cripplers reduce two
  attributes independently, floored at 1.
- Remaining: a Playwright pass that forces each IC live (GM "generate IC successes") and shows
  the stacked condition-monitor / rating reductions in the browser.

## #2 Build every program + option permutations -- [DONE] (size/cumulative math)
- **Cumulative reduction VERIFIED** (the user's key ask): actual size = `rating^2 x mult`,
  then `x0.5` per Optimization, then `x0.5` per Squeeze -> **75% total reduction** (left with
  25%). Confirmed in `frontend/deck-builder.html` `computeProgramFootprint*` (lines ~1748-1751
  and ~1851-1854) and numerically (Analyze-6: 108 -> 54 -> 27).
- Design size: `x2.0` per Optimization, `x1.5` per One-Shot; effective-rating adders
  (area/dinab/chaser/penetration/targeting/skulk/limit/squeeze) all feed eff rating first.
- Prior E2E confirmed option permutations produce distinct programs (`Attack-6`,
  `Attack-6 [Optimization]`, `Attack-6 [Penetration, Targeting]`).
- Remaining (targeted sample, browser): walk a representative program of each cost multiplier
  (x1/x2/x3/x4) through all its allowed options; assert buyCost = designSize x PF(rating) and
  designDays = designSize x 2.

## #3 Purchase every program permutation -- [TODO]
- "Import Purchased Program" path exists (E2E earlier). Need a targeted pass importing the
  representative permutations from #2 and asserting persisted size/cost match build math.

## #4 Trap-door host: discover -> enter -> confirm new system -- [TODO]
- Schema support exists: `MatrixHost.trap_doors_json`; designer has trap-door sub-host UI.
- Need: build host A with a trap door to host B, drive the decker to discover (locate) and
  traverse it, assert the run context switches to host B.

## #5 Enemy decker injected into a host mid-run -- [DONE end-to-end, verified live]
- **Engine** (`matrix_engine.py`): `generate_enemy_decker(code, value)` -- tier-capped rubric
  (Blue->Black); skill/MPCP scale with security_value but never exceed the tier (a Blue-5 host
  yields Computer<=4, not 12). `enemy_locate_test` (opposed: enemy Computer vs PC Detection Factor,
  PC Evasion resists); `escalate_enemy_intent` (boot->dump->kill as the alarm rises).
- **Rubric**: Blue/Green=boot (trace-dump), Orange/Red=dump (cybercombat crash), Black=kill
  (Black Hammer lethal biofeedback). Scanner rated at persona level (not full skill) so a sleazy
  PC keeps an evade window.
- **Behaviour**: the enemy must LOCATE the PC first (gives counterplay turns); on first contact the
  PC gets an ALERT (revealed) but progress is GM-only until pinpointed. All forced exits (trace-dump
  or icon crash) inflict DUMP SHOCK -- only the PC's own graceful logoff avoids it (per the user's
  correct VR2 reading). Two-way: the PC can Strike Back and crash the enemy's icon.
- **Endpoints**: `POST .../enemy-decker` (GM inject, auto-scaled), `.../enemy-decker/act`
  (GM: locate then execute intent), `.../enemy-decker/attack` (PC strikes back).
- **Redaction**: enemy deckers GM-only until `revealed`; players then see name/tier/intent/condition
  only (never raw ratings). **UI**: HOSTILE DECKERS panel + Strike Back + event badges.
- VERIFIED live: Red-8 dump->persona crash->dumped; Black-9 Black Hammer->killed; PC strike-back
  crashed a Green-6 enemy. +12 tests.

## #6 Paydata (discoverable + key) vs Scramble IC -- [DONE end-to-end, verified live]
- Engine: `scramble_decrypt_test` (Computer Test vs Scramble rating - Decrypt utility, floor 2,
  success = no tally) + `scramble_failure_consequence` (Poison wipes protected data; key data ->
  permanent loss; Exploding -> linked data bomb; standard -> no destruction).
- Run wiring: `_initial_state` loads host `paydata` + `scrambles` (both GM-only redacted);
  `perform_action` intercepts `decrypt_file` (RunActionInput.target_file) and resolves vs the
  targeted Scramble's rating. Success removes the Scramble; failure vs a Poison Scramble marks the
  protected paydata `destroyed=True` and emits a `decrypt` event.
- **Player representation (the user's question):** a failed decrypt vs a Poison Scramble on KEY
  data emits the event **"KEY DATA DESTROYED -- the Poison Scramble wiped the protected file. It
  cannot be recovered."** with `key_data_lost: true` -- shown in the run event log. VERIFIED live
  2026-05-31 (rating-15 Poison vs pool 10/TN 14 -> 0 hits -> wipe). +8 tests.
- Remaining polish: a paydata panel in the run UI that greys out `destroyed` files; Exploding-
  Scramble -> data-bomb detonation hookup (needs #7 Data Bomb wiring); IC response on the decrypt turn.

## #7 Worms, Data Bombs + Trap/Party/Construct -- [PARTIAL]
- [DONE] Trap IC (surface conceals hidden), Party IC (cluster_id + `_cluster_size`), Construct
  (single combined icon) -- `tests/test_vr2_matrix_scenarios.py::TestTrapPartyConstruct`.
- [DONE end-to-end] Worm + Data Bomb resolution. Engine fns `data_bomb_defuse`/`data_bomb_detonate`/
  `worm_attack` (+ tests). WIRED into the run:
  - **Data Bomb**: `_initial_state` loads host `data_bombs` (GM-only) + `defused_bombs`.
    perform_action -- accessing a bombed target (download_data/edit_file/upload_data + target_file)
    attempts Defuse when the Defuse utility is supplied (disarm, no tally) else detonates
    ((rating)Moderate persona damage + tally += rating, one-shot). VERIFIED live (detonate ->
    'DATA BOMB ... Moderate damage; tally +6', 2 persona boxes).
  - **Worm**: now lurks (reactive ambush, GM-only). resolve_reactive_ic branches for Worm ->
    `worm_attack` vs MPCP (Disinfect utility defends); infection sets state mpcp_infected +
    chip_replacement_required (permanent) + worm_resolved event, else repelled (Worm keeps lurking).

## #8 Passive Alert -> +2 all subsystem ratings + player notice -- [DONE]
- `tests/test_vr2_matrix_scenarios.py::TestAlertEscalation`: `_subsystem_rating` adds +2 to ALL
  five subsystems under passive alert; the activation emits a player-facing event
  ("PASSIVE ALERT -- all subsystem ratings +2..."); does not re-trigger; Active Alert revokes
  Validate-Passcode + destroys decoy and emits its own notice; Active adds no second blanket +2.
- Remaining: confirm the browser run log renders the passive-alert notice prominently.

## #9 Enemy representation to the decker -- reasoning + recommendation
**Question:** are IC/host ratings shown to the player during a run?
**Reasoning:** VR2 is asymmetric -- a decker does NOT automatically know an IC's rating; they
learn it via an **Analyze** Test (or a Sensor success vs invisible Probe IC). Auto-revealing all
ratings removes the purpose of the Analyze utility and the tension of the unknown. BUT: showing
ratings *after* a successful Analyze (and showing the host security code/value, which the decker
can reasonably estimate) lets the player make the "am I out-classed?" call the user wants.
**Recommendation (matches the user's lean):** keep ratings hidden until earned --
- Host security code/value + subsystem (ACIFS) ratings: shown (decker can scout these).
- IC type + rating: hidden until an Analyze IC success reveals it; then display it on the IC card.
- Invisible Probe IC: hidden until a Sensor success.
This gives the "know if you're being out-classed" payoff without trivializing Analyze.
**Status: IMPLEMENTED (backend) 2026-05-31, then REFINED to the vr2 line-409 detection model.**
Reactive IC 'do not betray themselves' -- they are now invisible until detected, not shown as
"Unknown IC". Graduated detection (`_ic_detection_level` / `_redact_ic`):
  0 unaware -> hidden entirely (dropped from player list)   2 -> type known, rating hidden
  1 -> presence known ("Unknown IC")                        3 -> type + rating + location.
Proactive IC betray themselves by attacking -> default level 1. `_secret_sensor_test` (decker
Sensor vs IC rating) raises the level when a reactive IC acts and emits a graduated notice; the
Probe loop reports the tally change at the detected level (no leak at 0); reactive-IC activation
events are flagged `gm_only` and `_serialize_run` drops gm_only events for non-admins. Analyze IC
still forces full reveal. +7 tests. Remaining polish: frontend click-to-target an IC for Analyze.

## #10 Tar Baby / Tar Pit deck-wipe -- [DONE]
- `tests/test_vr2_matrix_scenarios.py::TestTarBabyTarPit`: Tar Baby win crashes BOTH the IC and
  the utility; Tar Pit additionally rolls vs MPCP and sets `all_copies_corrupted` (the full
  deck-wipe of that utility) on a hit, and leaves copies intact on a miss.
- Remaining: surface the "utility wiped from all storage -- reload via Swap Memory" consequence
  in the run UI.

## #11 -- COMPLETE MODIFIER INVENTORY (from full vr2_rules sweep 2026-05-31)

The user asked to find ALL detection/masking/test modifiers, not just satlink. Full list:

**Detection Factor inputs/modifiers:**
- Base = ceil-avg(Masking, Sleaze), or ceil(Masking/2) if no Sleaze. [WIRED]
- Marker / Mark-rip crippler reduces Masking -> lowers DF. [WIRED NOW -- live DF]
- Suppression: -1 DF per suppressed IC, floor 1; restored on release (+tally). [DF math WIRED NOW;
  the suppress/release *action* endpoint is still a separate TODO -- nothing sets suppressed=True yet]
- Masking persona Mode: +50% Masking (raises DF); other BEMS modes reduce it. [GAP -- modes unmodelled]

**Trace Factor (line 578): TF = Evasion - TraceIC + Redirects + Camo + Jackpoint + Bandwidth**
- Camo utility, redirects, trace_factor (jackpoint), bandwidth_modifier all feed `_compute_trace_tn`. [WIRED as fields]

**Jackpoint table (lines 201-216) -- Trace Factor AND Access modifier:**
- Legal -2/-2, Illegal 0/0, Satellite varies/+2 (Trace immunity, Reaction -2), Workstation -4/-4,
  Remote +4/+4, Console -6/halve Access Rating & Security Value.
- Trace side surfaces via `trace_factor`; **Access modifier side is NOT auto-applied to Access Tests.** [GAP]

**Other test modifiers found:**
- Linked passcode: -2 TN to Logon when using Deception (line 370). [GAP]
- Stealth option: crash-IC tally reduced by Stealth rating; Stealth-6+ = 0 tally (line 416). [verify wiring]
- Shield: +2 TN to hit IC (Penetration negates; +4 vs Chaser). Shift: +2 TN (Chaser negates; +4 vs Penetration) (681-682). [verify wiring in attack_ic]
- Bandwidth Trace modifier (optional): (bandwidth/base, floor) x -1 (218-222). [field exists]
- Metaphor non-conformance: +2 all TNs (GM judgement, 1024). [intentionally manual]

**Implemented:** live Detection Factor (`_effective_detection_factor` = Sleaze + crippler-reduced
Masking + suppression count); **suppress/release endpoint** `POST /matrix-runs2/{id}/suppress`
(suppress -1 DF/IC no tally; release restores DF + tally += rating); **jackpoint Access modifier**
(`access_modifier` Legal -2/Satellite +2/Workstation -4/Remote +4 on Access Tests) + **Console**
halving (round up). Complements existing `trace_factor` (jackpoint Trace side).
**Also implemented:** **Persona Modes** (`persona_mode`; `_get_decker_effective` +-50% multipliers);
**linked-passcode -2** to Logon (with Deception); **Console Security-Value halving** for Access Tests
(perform_action + graceful_logoff); **Shield/Shift +2 to-hit** (`_shield_shift_tn_modifier` with
Penetration/Chaser negation + extra-effectiveness, wired into attack_ic via RunAttackInput.
penetration/chaser). **#11 is now COMPLETE** -- every detection/masking/access/test modifier in
vr2_rules is accounted for. Data-population for Shield/Shift IC flags (`ic.shield`/`ic.shift`) is a
designer/sheaf concern (the run logic is ready).

## #11 Satlink + masking / detection-factor modifiers -- [PARTIAL: live DF done; jackpoint/modes gap]
- `tests/test_vr2_matrix_scenarios.py::TestDetectionAndTrace`: Detection Factor = round-up avg of
  Masking & Sleaze (M6/S8 -> 7); masking-only = ceil(M/2); a Marker crippler lowering Masking
  lowers DF; Trace TN incorporates trace_factor + bandwidth_modifier; redirects reduce it; floors
  at 2.
- GAP: the **Satellite Uplink jackpoint** specifics are not auto-modelled -- Access +2, partial
  Trace-IC immunity, Reaction -2 (signal lag), and the Computer-Test-to-establish (Satlink Target
  Number Table). The engine exposes the trace/bandwidth *fields* a satlink would set, but there's
  no jackpoint selector that applies the +2 access / -2 reaction / immunity automatically. To
  build: a jackpoint type on the run config that applies these per `vr2_rules.md` lines 201-216.

---

## Gap-scan: other vr2_rules behaviours worth covering (API + UI)
- Suppression (reduce Detection Factor by 1 per suppressed IC; restore on release, +tally) --
  rules present; verify run wiring + UI.
- Grid security tally persistence (same-RTG no reset, different-RTG resets, follows onto PLTG) --
  verify in run/LTG flow.
- Bandwidth Trace Modifier (optional rule) -- decker bandwidth vs base bandwidth.
- Swap Memory reload (after Tar Baby/Shield/Armor depletion).

## Committed this session
- Known UI backlog (U1/U4/U5/U6/U9/U10/U2) fixed; verified in browser (U1 10 dice, U9 logon,
  U10 operations auto-apply utility). See `docs/matrix2-ui-e2e-findings.md`.
- `tests/test_vr2_matrix_scenarios.py` -- 41 tests, all green (#1/#7/#8/#10/#11 engine layer).

## Frontend polish (run UI) -- DONE 2026-05-31
- Event-log badges for the new event types: decrypt (KEY DATA LOST / DATA WIPED / DECRYPT),
  data_bomb (DATA BOMB / BOMB DEFUSED), worm_resolved (WORM INFECT / REPELLED), ic_detected,
  ic_suppressed, ic_released.
- IC cards: `[ID n/3]` detection-progress badge for partially identified reactive IC (the
  backend already redacts type/rating below the detected level).
- Key Paydata objective panel: destroyed key files render as `[DESTROYED]` (red, strikethrough),
  driven by a `file_name` on the decrypt wipe event.

## Live integration smoke -- PASS 2026-05-31 (isolated :8770, all session code)
persona Masking mode DF=9; decrypt Poison Scramble -> KEY DATA DESTROYED (file_name "Black Files");
data bomb detonates on download; GM sees Probe IC; suppress endpoint drops DF + emits event.
No regressions across the combined #6/#7/#9/#11 feature set.

## >>> RESUME CHECKPOINT (2026-05-31, updated) <<<

User priority: **#11 (account for ALL modifiers), then #9, #7, #6; #5 later.** -- #6/#7/#9/#11 are
all DONE (backend + tests + run-UI polish + live-verified). Remaining is #5 + browser passes.

DONE & committed (all on `matrix2`; tests green = 70 in test_vr2_matrix_scenarios.py + 40 in
test_matrix_engine.py):
- **#11** live Detection Factor (`_effective_detection_factor`: Sleaze + crippler-masking +
  suppression -1/IC floor 1) + full modifier inventory documented above.
- **#9** reactive-IC detection model (line 409): reactive IC invisible until detected; graduated
  reveal 0/1/2/3 via `_ic_detection_level`/`_redact_ic`; `_secret_sensor_test`; gm_only event
  filtering; proactive IC default visible; Analyze forces full reveal.
- **#7** Data Bomb (detonate/defuse on file access, verified live) + Worm (lurks; resolve_reactive_ic
  -> MPCP infection) + engine fns. COMPLETE.
- **#6** Scramble decrypt + Poison KEY-DATA-DESTROYED wipe, wired into perform_action (decrypt_file
  + target_file), VERIFIED live.

ALL of #1-#11 + #5 are now DONE (backend + tests + run-UI + live-verified). PICK UP HERE:
1. **Browser passes** (Playwright, isolated :8770) -- the remaining "user-perspective" verification:
   #1 forced-IC stacked view; #3 program-purchase permutations; #4 trap-door discover->traverse
   (host has trap_doors_json + renderTrapDoorsPanel + enterTrapDoor in matrix-run.html -- check the
   traverse endpoint works); targeted #2/#3 size/cost sweep; and a UI pass exercising the new
   enemy-decker panel + Strike Back, decrypt key-data-wipe, data bomb, suppress.
2. **Designer data-population** so the new run logic gets exercised from authored hosts: Shield/Shift
   IC flags (`ic.shield`/`ic.shift`); ensure designer writes paydata.is_key / scrambles.variant /
   data_bombs as the run expects (the run reads config_json.{paydata,scrambles,data_bombs}).
3. **Optional**: enemy-decker GM controls in the UI (inject/act buttons) for solo testing; PC-vs-
   enemy initiative ordering; click-to-target Analyze IC (low value -- backend defaults work).
2. **#9 / #6 frontend polish**: run UI click-to-target an IC card for Analyze; paydata panel that
   greys out `destroyed` files; surface the new `data_bomb` / `worm_resolved` / `ic_detected` /
   `decrypt` events nicely in the run log.
3. **#5 enemy-decker injection** (low priority): endpoint/state to add an opposing decker to a live
   run with its own persona + a way to act against the player.
4. **[TODO] browser passes**: #1 forced-IC stacked view, #3 purchase perms, #4 trap-door traverse,
   targeted #2/#3 size/cost sweep.
5. **Exploding-Scramble -> Data-Bomb hookup**: a failed decrypt vs an Exploding Scramble should
   detonate its linked data bomb (consequence fn already returns `detonate_data_bomb`; wire it).

Env to re-run anything live: see the env note at the top + memory `project_matrix2_test_matrix`.
Test server launch = venv python via PowerShell Start-Process; admin token on every call.
