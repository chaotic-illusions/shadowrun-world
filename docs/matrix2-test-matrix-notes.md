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
- **Offensive programs (faithful to vr2 "Offensive Utilities")**: Trace is host IC, NOT a decker
  tool -- an enemy decker removes you only by CRASHING YOUR ICON in cybercombat (icon crash -> dump
  shock). A plain **Attack** does icon-only damage (no deck damage). Lethal programs **Black Hammer**
  (Physical) / **Killjoy** (Stun) are carried ONLY on deadly-force hosts (Red/Black, line 2310);
  rating = half Computer skill; they add biofeedback (Body resists) AND burn MPCP on an icon crash at
  DOUBLE the program rating (line 1537, "like Blaster IC"). Cybercombat dice = offensive-utility
  rating + Hacking Pool (line 2014), not Computer skill. `intent`: dump (Attack) / kill (lethal);
  escalates dump->kill at high tally ONLY if a lethal program is loaded. Scanner persona-rated so a
  sleazy PC keeps an evade window. (Hog / Poison / Restrict / Reveal also exist in the rules as
  decker programs -- not yet auto-loaded; future enhancement.)
- **Behaviour**: the enemy must LOCATE the PC first (Locate Decker / Scanner -- gives counterplay
  turns); on first contact the PC gets an ALERT (revealed) but progress is GM-only until pinpointed.
  Any forced exit (icon crash) inflicts DUMP SHOCK -- only the PC's own graceful logoff avoids it.
  Two-way: the PC can Strike Back and crash the enemy's icon.
- **Endpoints**: `POST .../enemy-decker` (GM inject, auto-scaled), `.../enemy-decker/act`
  (GM: locate then execute intent), `.../enemy-decker/attack` (PC strikes back).
- **Redaction**: enemy deckers GM-only until `revealed`; players then see name/tier/intent/condition
  only (never raw ratings). **UI**: HOSTILE DECKERS panel + Strike Back + event badges.
- VERIFIED live (faithful rework): Green-6 uses Attack only -> icon crash -> dump, mpcp_dmg stays 0
  (no deck damage from a plain Attack decker); Black-9 Black Hammer -> lethal biofeedback -> killed;
  PC strike-back crashed a Green-6 enemy. No fake "trace-dump"; no invented per-hit chip burn.

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

## Table audit (2026-06-01) + enemy-decker-sheaf confirmation
- **Decker-summon table:** there is NO generation table that auto-rolls an enemy decker. The sheaf
  tables (Alert -> Reactive/Proactive White, Reactive/Proactive Gray, Black, Trap, Crippler/Ripper)
  are IC-only. A decker arriving is an AUTHORED sheaf step (book example Host A step 37 "government
  decker arrives"). The `enemy_decker` sheaf event I added implements exactly that -> NOT redundant,
  kept.
- **IC table usage when generating:** Alert, Reactive/Proactive White, Reactive/Proactive Gray,
  Black, Trap, Crippler/Ripper, IC Ratings = all used. **IC Options + IC Defenses Tables were NOT
  used -> FIXED 2026-06-01** (added IC_OPTIONS_TABLE + IC_DEFENSE_TABLE; `_roll_ic_extras` merges
  Cascading/Expert + Armor/Shield/Shift onto generated combat IC; Shield/Shift already wired to the
  to-hit TN). Remaining nuance: constructs/party still get `defenses: []` (could roll the table too);
  the run applies Shield/Shift but not yet Armor-on-IC / Cascading / Expert (those are carried for
  the GM/UI -- run-side application is a later polish).

## >>> GAPS PLAN (2026-06-01) -- Hog/Swap Memory, enemy auto-act, action economy + initiative <<<

Context-safe resume plan for the current work. Status updated as each lands.

**A. Swap Memory operation [DONE 2026-06-01, verified live]**
- New run action `swap_memory` (Simple action): reload/restore a program. Clears
  `state["program_damage"][util]` (Hog/Tar Baby/One-Shot/degraded Armor/Shield recovery -> rating
  back to base). Needs a `target_program` (util key). No test (vr2 line 1896). Add to ActionType +
  a UI control. Backend: in perform_action, intercept `swap_memory` -> clear program_damage[target]
  (+ remove any Hog infection on it), emit event, early-return.

**B. Hog persistence + purge [DONE 2026-06-01, verified live]**
  (Live: Hog took hold drain 2/turn -> new_turn auto re-drained to next-highest program ->
   purge_hog Computer test TN 14 -> swap_memory restored the program. All wired + 4 tests.)
- Make Hog a PERSISTENT infection (vr2: re-drains each Combat Turn until the program crashes, then
  moves to next-highest). Track `state["hog_infections"] = [{id, rating}]`.
  - Enemy act program="Hog": if attack hits, ADD/refresh a hog infection (rating = Hog rating) and
    do the first drain (existing `eng.hog_attack` -> reduce highest running util in program_damage).
  - On `new_turn`: for each hog infection, re-drain the current highest running util (another
    MPCP-vs-Hog test); emit event.
- Hog **purge** action `purge_hog` (Complex action, vr2 line 1548): Computer (Hog rating - hardening)
  Test, TN += the infected program's ORIGINAL rating. Success: remove the hog infection AND crash
  (zero) the infected program (program_damage[name] = base rating). Then the decker reloads via Swap
  Memory. Add to ActionType + UI.

**C. Enemy decker AUTO-ACT (app-as-GM) [DONE 2026-06-01, verified live]**
  (Refactored /act -> `_enemy_decker_take_turn` helper, called automatically after the IC loop in
   perform_action; added sheaf `enemy_decker` event for auto-inject. Live: host sheaf dispatched the
   enemy, which auto-located then auto-attacked every player action -> icon crash, no manual calls.)
- Today IC auto-attack each player action (perform_action loop ~line 1077). The enemy decker only
  acts via manual /enemy-decker/act. Make it automatic: after the IC loop in perform_action (and on
  new_turn), iterate `state["enemy_deckers"]` (active) and run the same locate->intent logic the
  /act endpoint does. Refactor the /act body into a helper `_enemy_decker_take_turn(state, decker,
  enemy, run, ...)` and call it from both the endpoint AND the auto-loop. Optionally auto-INJECT via
  a sheaf event type `{type:"enemy_decker"}` so authored hosts spawn one at a tally threshold.
  Keep the manual endpoint for GM control. Single-user model = the app plays the host + enemy.

**D. Action economy + initiative [FOUNDATION DONE 2026-06-01; ENFORCEMENT still pending]**
- DONE (non-breaking, verified live): roll decker Matrix initiative on run start + each new_turn
  (`_roll_decker_initiative`; Reaction = `_decker_reaction` = ceil((Q+I)/2)); store
  `decker_initiative`, `initiative_passes` (= init//10 + 1), `current_pass`, `actions_this_turn`;
  tag every operation with its `action_cost` (Free/Simple/Complex via `_ACTION_COST` from
  rules.SYSTEM_OPERATIONS); new_turn event reports initiative+passes; run UI shows "Initiative N
  (P passes)". (Live: start init 19/2 passes -> new_turn re-roll 14/2 -> analyze_host cost Complex.)
- ENFORCEMENT [DONE 2026-06-01, verified live] -- per-pass action budget with auto-advance:
  `_spend_pass_action` in perform_action spends each op's cost (Simple=1 AP, Complex=2 AP, Free=the
  pass's 1 free) from the current initiative pass; when the pass can't afford it, auto-advances to
  the next pass (refresh 2 AP + 1 Free, emits `new_pass`); when ALL passes are spent -> 400 "start a
  New Turn" (re-rolls init). Budget in _initial_state + reset in new_turn; legacy runs unenforced.
  Run UI shows "Initiative N -- pass C/P, X AP + Y Free". Throwaway specs updated to New-Turn between
  ops. +6 tests. (Live: init 9/1 pass -> Complex spends 2 AP -> 2nd Complex BLOCKED -> New Turn
  re-rolled 10/2 passes -> Free action used the free slot not AP.)
- NPC INITIATIVE-PASS INTERLEAVING [DONE 2026-06-01]: the proactive IC attack loop + the enemy
  auto-act loop gate on `current_pass` -- each NPC acts at most ONCE per pass and only on passes its
  OWN initiative reaches (init//10+1), via an `acted_pass` marker. Probe IC still test per System Test.
- INITIATIVE [CORRECTED 2026-06-01 per review]: rolled ONCE per cybercombat encounter, NOT per
  Combat Turn. Decker rolls at run start; IC rolls (Rating + Nd6 by code) on activation; enemy decker
  rolls on entry using the SAME model as the PC. `new_turn` no longer re-rolls -- it refreshes the
  action budget + clears per-pass markers, so every actor acts again on its FIXED passes.
- DECKER INITIATIVE (vr2): Reaction + 1D6 + (RI: +1D6 & +2 Reaction per level, max +3D6/+6) +1D6 hot
  DNI +1D6 reality filter. Reaction = ceil((Quickness+Intelligence)/2) [NOT Willpower]. IC = Rating
  + Nd6 (Blue1/Green2/Orange3/Red4/Black5). Passes = init//10 + 1.
- ENEMY DECKER INITIATIVE SCALING [DONE 2026-06-01]: enemies use the PC initiative model with
  tier-scaled RI + Quickness/Intelligence (RI<=MPCP/4): Blue RI0 Q3/I4; Green RI1 Q4/I5; Orange RI1
  Q5/I6; Red RI2 Q6/I6; Black RI3 Q6/I8. So a Red/Black security decker keeps pace with a nova-hot
  player. Sample avg passes: player rookie ~1.7 / veteran 3 / nova-hot ~3.9; IC Blue1..Black~3.2;
  enemy decker Blue~1.7 / Green~2.3 / Orange~2.4 / Red~3.0 / Black~3.6.
- GAP D FULLY COMPLETE.
- ORIGINAL SEQUENCING NOTES (for the NPC-interleaving refinement):
  KEY SEQUENCING INSIGHT: today IC + enemy deckers act inside perform_action (once per player
  action). For a faithful pass model that must change, so do it in this order:
  1. Add per-pass budget to state: `pass_action_points` (2) + `pass_free` (1), reset each pass.
     perform_action looks up `_ACTION_COST[action]`: Free->pass_free, Simple->1 AP, Complex->2 AP;
     reject 400 ("out of actions this pass -- advance pass / new turn") when insufficient.
  2. Add `POST /{run_id}/next-pass`: if current_pass < initiative_passes -> current_pass++, refresh
     budget, and RUN the IC + enemy-decker turn for that pass (move the IC attack loop + the
     `_enemy_decker_take_turn` loop OUT of perform_action into a shared `_resolve_npc_pass(state,...)`
     helper called here + on new_turn). If current_pass == initiative_passes -> require new_turn.
  3. perform_action no longer auto-runs IC/enemy (they act on pass advances). new_turn re-rolls init,
     resets passes/budget, and resolves the first NPC pass.
  4. IC/enemy "act on the passes their OWN initiative reaches": store each NPC's initiative + compute
     its passes; in `_resolve_npc_pass`, only act NPCs whose init reaches the current global count.
  5. Frontend: show "Pass C/P -- Actions: AP left, Free left" + a "Next Pass" button; handle the
     400 reject. Update throwaway Playwright specs to advance passes / new turns.
  Engine fns (`decker_initiative_roll`, `ic_initiative_roll`) + `_ACTION_COST` + initiative state +
  the `_enemy_decker_take_turn` helper are all in place -- this is turn-loop restructuring + UI.
- ORIGINAL NOTES (kept for reference):
- vr2: a Combat Turn has multiple INITIATIVE PASSES in increments of 10. Initiative = Reaction +
  initiative dice; you act on your score, then -10, -10... (e.g. 22 -> 22,12,2). Each pass you get
  **2 Simple OR 1 Complex, plus 1 Free** action. Operations already carry an `action` cost
  (Free/Simple/Complex) in `app/services/matrix_rules.py` (the System Operations table). Currently
  NONE of this is tracked -- perform_action allows unlimited actions and new_turn just refreshes HP.
- Plan: add turn/pass state -- `current_turn`, `current_pass`, `decker_initiative`, `actions_left`
  ({simple:2, complex:1->shared budget, free:1}). On run start + new_turn, roll decker initiative
  (eng.decker_initiative_roll already exists), compute passes = (init // 10) + 1. perform_action
  decrements the action budget by the operation's cost (reject if none left); new_turn / "next pass"
  advances. IC/enemy deckers also get passes per their initiative (act on each pass their init
  reaches). This is a real turn-structure rework -- do it as its own session; engine fns
  (decker_initiative_roll, ic_initiative_roll) already exist; rules.SYSTEM_OPERATIONS has costs.
- Reaction = ceil((Quickness + Intelligence)/2) + response_increase (cap +3); DeckerStats already
  has quickness/intelligence/response_increase.

**E. IC Options/Defenses -- run-side application + constructs [DONE 2026-06-01, verified]**
- Generation rolls IC Options (Cascading / Expert Offense+ / Expert Defense+) and IC Defenses
  (Armor / Shielding / Shifting) onto combat IC + party components; constructs roll the Defenses
  Table; `_activate_sheaf_step` carries options/cascading/expert onto active IC (regular + party).
  - **Armor on IC** [CORRECTED 2026-06-01 per review]: Armor reduces the attack POWER (lowers the
    IC's resist TN by 2 -> the IC resists more easily), NOT the damage level. (Earlier wrong impl
    staged the level down 6M->6L; now keeps the level, eases the resist.)
  - **Expert** [CORRECTED]: the trade-off -- Offense +N adds N attack dice AND removes N from the
    IC's damage-resistance; Defense +N adds N resist dice AND removes N attack dice (value 1-3).
    Applied in attack_ic (resist pool) + the IC attack loop (attack pool). (`_ic_expert`)
  - **Cascading** [CORRECTED -- prior sheaf-step-on-crash was plain wrong]: a cascading IC that
    MISSES gains +1 attack Security Value (cumulative); a HIT the decker fully resists gains +1 to
    its Rating (cumulative); both capped by the Cascading IC Table (`_cascade_max_increase` by code,
    `_apply_cascade_outcome`). Applied in the standard cybercombat branch.
  - **Constructs**: DONE -- `_build_construct_or_party_event` rolls the IC Defenses Table (was []).
  - Verified live: generated Red-9 sheaves -> IC carry options/expert (e.g. Marker-10 Expert{defense,3}
    [Armor,Shielding]); constructs carry defenses.
  - Note: IC Armor power reduction is a fixed 2 (the IC Defenses Table lists "Armor" with no rating).

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

ALL of #1-#11 + #5 are DONE (backend + tests + run-UI + live-verified) AND the Playwright
user-perspective passes are GREEN (2026-06-01, isolated :8770). Specs in `D:\Code Projects\_sr_e2e\`:
- `run.spec.js` -- baseline run (logon + operations) PASS, no regressions.
- `newfeatures.spec.js` -- 6/6: KEY PAYDATA panel; decrypt vs Poison Scramble -> KEY DATA DESTROYED
  event + `[DESTROYED]` panel badge; data bomb detonation; HOSTILE DECKERS panel + Strike Back.
- `prog.spec.js` -- #3: program build options + buy/Import flow + persistence PASS.
- `stacked-trapdoor.spec.js` -- #1 stacked IC: 3 IC cards (Killer+Acid+Blaster) render together.
- `trapdoor.spec.js` -- #4: Front Door -> graceful logoff -> NEW run on Back Room + logon
  ("Trap-door transit complete"). PASS.
Also added a run-UI **Target (file/slave)** input so data bombs / scramble targeting are reachable
from the browser (newfeatures pass confirmed).

REMAINING (optional polish, all backend logic already done + unit-tested):
1. **Designer data-population**: author Shield/Shift IC flags (`ic.shield`/`ic.shift`) and confirm the
   designer writes paydata.is_key / scrambles.variant / data_bombs as the run reads them.
2. **Enemy-decker GM controls in the UI** (inject/act/program-pick buttons) for solo testing -- today
   those go through the API (the player-facing HOSTILE DECKERS panel + Strike Back already render).
3. **Nice-to-haves**: click-to-target Analyze IC (backend defaults work); PC-vs-enemy initiative order.

Env to re-run anything live: see the env note at the top + memory `project_matrix2_test_matrix`.
Test server launch = venv python via PowerShell Start-Process; admin token on every call.
