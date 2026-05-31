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

## #5 Enemy decker injected into a host mid-run -- [GAP, build]
- No enemy-decker entity/injection path in `matrix_runs.py`. Build: an endpoint/state to add an
  opposing decker to a live run, with its own persona stats + a way to act against the player.

## #6 Paydata (discoverable + key) vs Scramble IC -- [PARTIAL engine, GAP on key-data-wipe UI]
- Paydata table + Scramble IC (Poison/Exploding variants) exist in designer; `Scramble`
  summary: "Poison variant destroys protected data on failed decrypt." Decrypt utility reduces
  the decrypt TN.
- GAP: the *consequence* of a Poison-Scramble wiping **key data** is not surfaced to the player
  (no "key data destroyed" event/UI). Build: on failed decrypt vs a Poison Scramble protecting
  key data, emit a clear destructive event + show it in the run log / paydata panel.

## #7 Worms, Data Bombs + Trap/Party/Construct -- [PARTIAL]
- [DONE] Trap IC (surface conceals hidden), Party IC (cluster_id + `_cluster_size`), Construct
  (single combined icon) -- `tests/test_vr2_matrix_scenarios.py::TestTrapPartyConstruct`.
- [PARTIAL] Worm + Data Bomb are in IC_CATALOG and place into the run, but their *unique*
  resolution (Worm infects MPCP / chip replacement; Data Bomb explodes for (rating)M on undefended
  access, +rating tally, Defuse utility) is not wired into the run action loop -> GAP to build +
  test. Disinfect (anti-worm) and Defuse (anti-bomb) utilities exist in the catalog.

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
**Status: design decision recorded; implementation = [TODO]** (gate IC rating display behind an
Analyze success flag on each active_ic entry).

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

**Implemented this step:** live Detection Factor (`_effective_detection_factor`) -> accounts for
Sleaze + crippler-reduced Masking + suppression count in one place. Committed, +4 tests.
**Still GAP for #11 (next):** jackpoint Access modifier + Console halving; suppress/release action
endpoint; linked-passcode -2; Shield/Shift to-hit penalty wiring; persona modes.

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

## Next session
Build the [GAP] features in priority order: #6 key-data-wipe event+UI, #5 enemy-decker
injection, #7 Worm/Data-Bomb run resolution, #9 Analyze-gated IC rating display, #11 satlink
jackpoint; then the [TODO] browser passes for #1/#3/#4 and the targeted #2/#3 size/cost sweep.
