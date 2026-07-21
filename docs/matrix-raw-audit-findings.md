# SR2 Matrix Engine -- RAW-vs-Implementation Audit Findings

Consolidated, deduped divergence list from the phase-3 sweep (5 clusters: C1 core, C3 IC-A, C4 IC-B,
C5 sheaves, C8 ops, C9 cybercombat). Each row cites `vr2_rules.md#Lnnn` + code line(s). Verdicts:
**FIX** = unambiguous internal inconsistency the maintainer should correct; **RULE** = a design/RAW
judgment call for the user to decide; **GAP** = not modeled (may be deliberate). The user reviews all
of these; nothing contested has been changed.

## A. Confirmed inconsistencies (recommend FIX)

| ID | Rule (vr2) | Code | Issue |
|----|-----------|------|-------|
| A1 | Trace in Location Cycle is reactive/immune to cybercombat (L565-566) | `attack_ic` matrix_runs.py L5828+ (no `trace_phase=="locate"` guard) | **VERIFIED.** `_apply_slow` (L2491) and `_apply_maneuver`/Evade (L3836) both block a locating trace, but `POST /attack` does not. A player can crash a trace mid-location-cycle -- and worse, crashing a locating **Trap Trace** this way wrongly "defuses" it (`_apply_ic_crash` skips `_spawn_trap_hidden` for traces), bypassing RAW where the trap should still spring on completion. Add the same location-cycle guard the two sibling actions use. |
| A2 | Analyze Security reveals the host's **Security Rating** + tally + alert (L1869) | `_apply_analyze_security` matrix_runs.py L5317-5333 | Snapshot stores only `tally` + `alert`; the Security Rating (code/value) is never surfaced. Add a `host_security_revealed` reveal on success (mirror Analyze Host). |
| A3 | Position Attack winner may choose -TN **or** +Power (L2004) | `_resolve_npc_maneuver` matrix_runs.py L3983 | **RESOLVED.** The PC path always offered the choice (`position_choice`). Extracted a shared NPC heuristic `_npc_position_bonus(state, net)` (+Power when the PC is at >=5 persona boxes, else -TN) and applied it in BOTH the NPC-initiated win AND the PC-initiated backfire (enemy seizes the position) branches, which previously hard-coded `{"tn_reduction": net}`. |

## B. RAW/design judgment calls (need a USER RULING)

| ID | Rule (vr2) | Code | Question |
|----|-----------|------|----------|
| B1 | Alert generation: roll **1D6 + (trigger steps already passed)** per step; Passive/Active Alert are the 8+ table outcomes (L843-858) | `_roll_alert_family` / `_generate_sheaf_impl` matrix_engine.py L507, L535, L733-768 | The app uses **2D6** (bell curve, range confirmed by `SHEAF_ALERT_TABLE` 1-12) with **no** step modifier, and places Passive/Active Alert at **deterministic** sheaf positions (`step//3`, `step*2//3`) rather than as rolled 8+ outcomes. Deliberate redesign or bug? Changes the shape/odds of every run. |
| B2 | Condition Monitor box-fill per damage level | `DAMAGE_BOXES` matrix_rules.py L42 | RESOLVED (user ruling 2026-07-10): **no conflict** -- the two tables measure different things (L2074 = per-damage-level BOXES L1/M2/S3/D6 that fill the 10-box monitor; L2228 = the security-monitor THRESHOLDS 1/3/6/10 at which levels escalate). Code's `DAMAGE_BOXES` (L1/M2/S3/D6) is correct; no change needed. |
| B3 | Analyze Host auto-reveal-all at **7+** successes (L1870) | `_apply_analyze_host` matrix_runs.py L3349 (`net >= 6`) | Already labeled "USER OVERRIDE of RAW" in the docstring. Confirm the 6 threshold is intended (not a bug). |

## C. Not modeled (confirm deliberate, or backlog)

| ID | Rule (vr2) | Note |
|----|-----------|------|
| C1 | Black IC jack-out hardening: after any Black IC hit, jack-out needs a Willpower(IC Rating) Test and the IC gets one last attack; ICCM alters this (L610-613) | **IMPLEMENTED (Wave 6).** Cybercombat sets `black_ic_engaged` on any Black IC hit; `jack_out` then requires a Willpower(Black IC Rating) Test (`-2` TN if `decker.iccm`); failure keeps the decker jacked in (Complex Action spent), success triggers one final `_black_ic_final_attack` (2x-rating MPCP burn if it drops the decker) before dump + end. |
| C2 | Tar Pit corrupts ALL copies (active + storage) on success; program gone for the run unless offline backup (L540-542) | **IMPLEMENTED (Wave 3).** `_wipe_all_copies` corrupts the active copy, adds the program to `one_shot_wiped` (Swap Memory cannot reload it), and drops all storage copies for the run. |
| C3 | Data Bomb triggers only after a **failed defuse** then a successful access; defuse attempts add tally via an opposed Security Test (L470, L473) | **IMPLEMENTED (Wave 3, per user ruling).** Defuse is now an OPPOSED System Test: host successes bump the security tally EVERY attempt; defuse succeeds only if `decker_succ > host_succ`; all-1s botch detonates; a clean defuse adds no bomb-rating tally. |
| C4 | Scramble Poison variant = separate Poison test on failed decrypt; Exploding variant booms on decrypt OR crash-without-defuse (L492-493) | **IMPLEMENTED (Wave 3).** Poison variant rolls an IC Poison Test (scramble rating dice vs TN = decker Computer skill) on failed decrypt -- data destroyed only on a success, safe on a miss. Exploding variant detonates the linked data bomb on a failed decrypt. |
| C5 | Worm infection test = host Security Value dice vs MPCP, hardening as a post-roll "successes must exceed hardening" threshold; per system-test-on-infested-subsystem timing (L548-550) | **IMPLEMENTED (Wave 4, per user ruling).** `worm_attack` rolls host Security Value dice vs MPCP TN; `net = successes - hardening`; MPCP infected when `net > 0` (successes exceed Hardening; sets `mpcp_infected`/`chip_replacement_required`). Disinfect no longer defends the infection roll. Timing kept as the existing per-turn lurking-IC model (house-rule note retained). |
| C6 | Worm variants Dataworm / Deathworm / Tapeworm (L554-559) | **DEFERRED** (needs user eyes): Deathworm (+2 attack/resist TN) & Tapeworm (run-end paydata loss) have real effects; Dataworm is narrative-only. Requires a `variant` field + designer UI + schema + infected-deck deck-builder remediation flow. |
| C7 | Improvised Attack (allocate Evasion/Bod -> Power, Computer Test vs Power) (L2040-2052) | Intentionally not modeled (user ruling 2026-07-10). |
| C8 | Crash Application operation (Simple; shuts down a host application, not IC) (L1874) | Intentionally not modeled (user ruling 2026-07-10). |
| C9 | Dump Log (L1876), Locate Frame (L1883), Logon to RTG (L1886) | Intentionally not modeled (user ruling 2026-07-10). |
| C10 | Host Reset / cross-run tally decay + re-entry starting tally (L957-976) | Intentionally not modeled (user ruling 2026-07-10). |
| C11 | Trace after jack-out: 1D6 turns remain to complete (L592) | Intentionally not modeled (user ruling 2026-07-10). |
| C12 | Host Shutdown rolling countdown + final-warning turn + secret per-turn Sensor test (L730-755) | **IMPLEMENTED (Wave 5).** The `shutdown` sheaf event now starts a countdown (1D6 per 2 pts of Security Value, +1D3 final-warning turn) resolved each Combat Turn in `_process_host_shutdown_countdown`: secret Sensor Test (TN = turns remaining) per turn, auto-warning on the final-warning turn, and a full dump (`_apply_dump_shock`) + run-end when it completes. |
| C13 | SAN types (Vanishing/Teleporting/Triggered) (L797-804); Slave Locate/Control/Edit operations (L1007-1015); UMS/sculpted (L1018-1032) | Intentionally not modeled (user ruling 2026-07-10). |
| C14 | Data Bomb detonation 1-DF suppress choice (L479); scramble-crash-adds-tally-unless-suppressed (L495) | **RESOLVED (reworked -- unified post-event ledger, no action cost).** Suppression is a post-event immediate query for ALL sources (crashed IC and data bomb). `_detonate_data_bomb` always applies the bomb-rating tally, then registers a `state['suppressions']` entry (`_register_suppression`); the detonation event carries `suppression_id`. The player may then, at any time on their turn and with NO action cost, `POST /suppress {ic_id=entry-or-IC id}` -> `_toggle_ic_suppression`/`_toggle_entry_suppression` to spend 1 Detection Factor to refund the tally (persona damage still lands), or Release (re-adds tally, one-way). Each active suppression costs 1 DF (`_effective_detection_factor`, floored 1). The old pre-declared `suppress_bomb` action field + `state['bomb_suppressions']` counter + frontend checkbox were removed. UI: crashed-IC Suppress button, SUPPRESSIONS panel, DF artifact, and a blocking suppress-decision modal. |
| C15 | Tortoise deck Black IC biofeedback lethality | **RESOLVED (user ruling -- full immunity).** A tortoise deck has no ASIST/simsense link, so Black IC cannot reach the operator AS Black IC: the inline cybercombat resolver gates `is_black = ic['type']=='Black IC' and deck_mode != 'tortoise'`, routing a tortoise's Black IC through the standard icon-only path (no biofeedback, no `black_ic_engaged` jack-out gate, no dump shock, no MPCP-final). `is_non_lethal` reverts to `== 'cool'`. Tortoise's other cons (half-Reaction+1D6 initiative, dump-shock immunity) are already modeled in matrix_engine. |
| C16 | SYSTEM_OPERATIONS reference table missing rows | **RESOLVED.** Added `Analyze Icon` (Control/Analyze/Free -- data-bomb detection) and `Decrypt File` (Files/Decrypt/Simple -- no-tally scramble break) to `matrix_rules.SYSTEM_OPERATIONS`, both already-working ActionTypes. |

## Confirmed MATCH (no action) -- highlights

Trace Factor formula + all six term signs (L578); Relocate single-target / spoof-for-turn / suppress
(L585-590, freshly corrected); both Trace completion effects (L590-591); Black IC dual-resistance +
2x-MPCP-blaster-on-kill + icon-crash-then-jackout-only (L619-641); Trap crash-triggers vs Trap-Trace-
defuse (L685-688); Cascade/Expert/Shield-Shift IC options (L693-717); all crippler/ripper/sparky/
blaster math (L433-534); Probe timing + newcomer-IC initiative gating (L485, freshly corrected);
sheaf multi-step simultaneous fire + Passive/Active alert subsystem/passcode effects (L835-873);
Detection Factor + Hacking Pool + System Test resolution + tally acceleration (L96-151); all
Cybercombat staging/armor/shield/wound/simsense/dump-shock math (L2062-2117); combat-maneuver
Cloak/Lock-On directions + tie-is-failure (L1987-1991).
</content>
