# Matrix Event-Log Review Tracker

Working tracker for the reviewer pass over every `_append_event(...)` site in
`app/routers/matrix_runs.py`.

## Files

| File | Role | Rule |
|---|---|---|
| `docs/event-log-catalog-final.csv` | Current renders + your notes -- the working review form | Annotate THIS; a regen preserves the notes already in it |
| `docs/event-log-catalog-final.md` | Human-readable version of the above | Regenerate any time |
| `docs/event-log-catalog.csv` | Your original annotations (committed backup) | Frozen backup -- leave as-is |

Add more comments to `-final.csv`, then refresh the renders (notes are kept) with:

```
python tools/gen_event_catalog.py --suffix=-final
```

The generator round-trips reviewer notes from the OUTPUT file itself, so re-running never
drops the comments you have added.

## Scope

197 event sites reviewed; **136 carry a note**. Each note is filed below under ONE
primary category, with cross-references (`xref:`) where it spans more than one workstream.

**Status legend:** `TODO` | `WIP` | `DONE` | `VERIFIED` (checked, no change needed) |
`AUTO` (already corrected by the v2 regen -- no app change).

## Recommended order of attack

1. **Review on v2, not v1.** ~7 of your notes were reacting to catalog *mis-renders* that
   are already fixed in v2 (category H). Re-reading those rows in v2 will retire them.
2. **Batch the copy edits (A).** ~61 notes are pure wording / flavor / de-CAPS. Lowest
   risk, highest volume, no mechanics change. Knock these out first in one or two passes,
   then regen + run tests.
3. **Answer the clarifications (E).** ~15 "when does this fire / help me understand"
   notes. Resolving these re-classifies several CULL and DUP candidates (some become
   "keep", some become "confirmed dead").
4. **Verify + resolve the cull targets (B).** ~26 notes. Each needs the UI gate confirmed
   before removing the branch -- downgrade to an API guard if it is reachable via direct
   call, delete if truly dead.
5. **De-duplicate (C).** ~15 notes. Confirm the overlap, keep the RAW-correct one.
6. **Apply the view / redaction decisions (D)** and the **logic fixes (F)**, then the
   **AAR additions (G)**.

Each backend text/logic change needs a server restart (currently on port 9001) plus
`python -m pytest -q` -- watch for tests that pin event wording (e.g.
`test_matrix_reconciliation.py`).

---

## A. Text / flavor / de-CAPS (copy edits -- low risk)

**Status: DONE (2026-07-30).** All rows below applied in `app/routers/matrix_runs.py`;
suite green (1207 passed). Exceptions: row 177 already emitted "tally +X" (no change);
rows 180 and 194 got a player-friendly base line with the roll kept in the event payload --
a full admin/player split stays in workstream D. Row 134 uses "turns" (not "rounds").

| Row | Event | Location | Action |
|---|---|---|---|
| 10 | crash_host_complete | _complete_host_crash:10048 | Player: "Host crashed, dumped -- System Offline. Dump Shock: 3 (2 boxes). Run complete." (xref: E -- explain dump shock) |
| 13 | data_bomb | _detonate_data_bomb:4908 | "System alert detonated" -> "Data bomb detonated" |
| 15 | data_bomb | _apply_defuse_bomb:5307 | Admin: "Data bomb defused" + show opposed test + note tally increase (xref: H -- stray '3') |
| 19 | data_bomb_found | _apply_analyze_icon:5210 | Drop "device": "Defuse the bomb before attempting access." |
| 33 | decrypt | _apply_direct_action:8516 | "Decrypt success/failure -- and the attached data bomb detonates!" |
| 36 | decrypt | _apply_direct_action:8570 | "Decrypt failed and the Poison IC has erased all files on the host." |
| 37 | defense_pending | _park_pending_defense:6914 | Simplify wordy resist terminology (xref: E -- does hacking-pool resist auto-pop?) |
| 40 | dinab_attack | _dinab_strike_decker:4517 | Lose "this pass"; "just fails to take hold." |
| 42 | dinab_crashed | _crash_dinab:4267 | "The DINAB attack fumbled and the construct crashed." |
| 46 | download_started | _apply_file_action_result:8275 | "Downloading of <file> beginning. <N> turns until completion." |
| 48 | enemy_decker | _enemy_medic_heal:3278 | "but it fails" -> "but fails" |
| 49 | enemy_decker | _enemy_nerve_check:3301 | "Enemy Decker (Razor) is wounded (2/10) and their nerve breaks. They jack out, abandoning the hunt." |
| 50 | enemy_decker | _enemy_restore_repair:3603 | "but fails" (same fix as row 48) |
| 52 | enemy_decker | _apply_locate_decker:5919 | Remove "this pass." |
| 53 | enemy_decker | _apply_locate_decker:5941 | "Re-acquired target: <target>" |
| 54 | enemy_decker | _apply_locate_decker:5946 | "Re-acquire failed. <target> slips past your sensors." |
| 55 | enemy_decker | _drain_all_hog_infections:10883 | Say what got drained + new value (xref: E -- '2' = {frag}?) |
| 57 | enemy_decker | _enemy_purge_hog:10931 | "<target> purges your Hog program from their deck." |
| 59 | enemy_decker | _enemy_swap_reload:10964 | "<target> reloads {pretty}." |
| 60 | enemy_decker | _enemy_scan_pc:10992 | "<target> analyzes your icon and learns your weaknesses." |
| 63 | enemy_decker | _enemy_decker_take_turn:11082 | "... has located your position." (xref: E -- trigger = successful locate?) |
| 64 | enemy_decker | _enemy_decker_take_turn:11087 | "<enemy> has failed to locate you this turn." |
| 72 | file_decompressed | _apply_decompress:4788 | Just show total Mp used now (xref: E -- "storage untracked"?) |
| 73 | file_deleted | _apply_file_action_result:8243 | "File <name> erased from the host." |
| 76 | file_modified | _apply_file_action_result:8233 | "File <file> altered on the host successfully." |
| 82 | host_ltg_revealed | _apply_analysis_action_result:7902 | "... no LTG access." |
| 84 | ic_analyzed | _apply_analysis_action_result:7762 | Drop the Decrypt target-number part (xref: E -- failure state?) |
| 89 | ic_attack | _advance_npc_pass:7256 | "Trace IC has your data trail. <N> rounds until jackpoint located." |
| 90 | ic_attack | _advance_npc_pass:7268 | "Trace IC is hunting your data trail." |
| 91 | ic_attack | _advance_npc_pass:7282 | "Trace spoofed for one turn." |
| 92 | ic_attack | _advance_npc_pass:7304 | "Satlink traced. Physical location unknown. -1 to all Proactive IC TNs, +1 to all Security Tally increases." |
| 93 | ic_attack | _advance_npc_pass:7318 | "Jackpoint traced, physical location reported. -1 to all Proactive IC TNs, +1 to all Security Tally increases." |
| 94 | ic_attack | _advance_npc_pass:7333 | "Trace continues. <N> rounds until jackpoint located." |
| 98 | ic_attack | _advance_npc_pass:7533 | "Consciousness lost. Black IC attacking what's left of your persona!" (xref: E -- fires when dead/unconscious) |
| 107 | ic_relocate | _apply_locate_ic:5878 | Replace "pass" with "turn" |
| 117 | invalidate_passcode | _apply_control_action_result:8020 | "Host passcode table erased. All host icons considered intruders." |
| 118 | invalidate_passcode | _apply_control_action_result:8028 | "The host rejected your attempt to delete the passcode table." |
| 121 | jack_out_failed | jack_out:12059 | "You are unable to sever your connection to the host as the Black IC grabs your icon and holds fast." |
| 122 | logoff_fail | _apply_graceful_logoff:9788 | "The host rejected your logoff request." |
| 123 | logoff_success | _apply_graceful_logoff:9770 | "You complete your logoff from the host. Run complete." |
| 128 | maneuver | _resolve_npc_maneuver:5820 | "edge" -> "advantage" |
| 132 | new_pass | _open_next_decker_pass:10178 | Drop "actions refreshed"; keep "hacking pool restored" |
| 133 | new_turn | _announce_new_combat_round:10192 | Round number + HP restored only |
| 134 | null_operation | _tick_active_download:4681 | "Download continuing <N> rounds remaining." (xref: E -- rounds vs turns) |
| 137 | one_shot_wiped | _wipe_one_shot:1826 | If all copies wiped -> Tar Pit; drop "cannot be reloaded" (xref: E) |
| 144 | persona_crash | _advance_npc_pass:7551 | "The IC crashes your icon and increases its rating. Jack out now!" (xref: F -- UI lock) |
| 145 | persona_crash | _enemy_decker_take_turn:11309 | de-CAPS: "Persona Crashed" |
| 151 | purge_hog | _apply_direct_action:8457 | "You are unable to purge the Hog virus from your deck." |
| 154 | redirect_placed | _apply_control_action_result:8111 | "Host redirect successfully placed. Trace Factor +1." |
| 158 | relocate | _apply_control_action_result:8100 | "<IC-Rating> spoofed for this turn." |
| 162 | scramble_analyzed | _apply_analyze_icon:5195 | Simplify + de-CAPS ("Defuse first.") |
| 165 | scramble_found | _apply_analysis_action_result:7829 | Found -> defuse the bomb first -> decrypt if relevant |
| 170 | shutdown_detected | _process_host_shutdown_countdown:10147 | de-CAPS |
| 177 | suppression_released | _toggle_entry_suppression:4039 | Show "tally +X" instead of a bare number |
| 180 | tapeworm_payload_loss | _apply_tapeworm_run_end:10554 | Player: "the Tapeworm was unable to delete any data"; keep the roll admin-only (xref: D) |
| 181 | tapeworm_payload_loss | _apply_tapeworm_run_end:10570 | de-CAPS |
| 182 | tar_pit_corruption | _resolve_lurking_tar:10708 | "All copies of <utility> lost." |
| 185 | tar_steamrolled | _apply_steamroller:3824 | Drop "stays lurking"; show damage taken + condition |
| 188 | trap_door_found | _apply_analysis_action_result:7803 | Last sentence: "Destination unknown" |
| 189 | trap_door_return | _pop_host_stack:9913 | "Logged off <host>, returned to <parent host>" |
| 191 | validate_passcode | _apply_control_action_result:7994 | "... the host rejects your injected passcode" |
| 194 | worm_disinfected | _apply_disinfect:3711 | Player: "Disinfect Failed, MPCP not compromised. Security tally increased." |

---

## B. Cull / gating verification (verify UI gate -> remove or downgrade to API guard)

**Status: VERIFIED -- KEEP ALL (2026-07-30). 0 of 26 are dead code.** There is no
server-side action-legality gate (the `/action` endpoint dispatches by type), so these
branches are reached three ways:

1. **DINAB autonomous runs** bypass the UI entirely -- their "offline / no-target /
   nothing-to-do" line is the correct feedback when a DINAB fires with nothing to act on:
   rows **109, 129, 130, 148, 150, 159, 160, 183, 184, 192**.
2. **Direct `/action` calls** -- crash-preventing guards for an invalid call (no legality
   check upstream): rows **14, 23, 32, 51, 71, 106, 155, 156**.
3. **Legitimate outcome branches misread as no-ops**: **20** (Analyze Subsystem DOES
   surface datastore-wide / linked bombs; per-file bombs stay Analyze Icon), **75** (Locate
   File auto-targets KEY files; "none found" is a real result), **77** (re-Analyze Host),
   **178** (internal turn-end auto-accept of undecided suppressions -- not a UI action),
   **187** (trap-door entry). **81** stays in F (LTG-reveal gating).

Deleting any of these replaces a clean message with a KeyError/crash. If the goal is less
log noise, the safe follow-ups are (a) gate the action in the FRONTEND so it is not offered
when invalid, and/or (b) convert the pure API-only guards to HTTP 400 -- both are behavior
choices tracked separately, not deletions. No code removed.

| Row | Event | Location | Original hypothesis (all resolved -> KEEP, see status above) |
|---|---|---|---|
| 14 | data_bomb | _apply_defuse_bomb:5262 | Defuse only valid when a bomb is present -- confirm, then remove |
| 20 | data_bomb_found | _apply_analysis_action_result:7846 | Analyze-subsystem finding a file bomb should be impossible -- verify/remove |
| 23 | data_downloaded | _apply_file_action_result:8290 | Prevent re-download of an owned file (drop from valid list) -> remove event |
| 32 | decrypt | _apply_direct_action:8489 | Gated unless analyze performed -- verify/remove |
| 51 | enemy_decker | _apply_locate_decker:5913 | locate_decker should be gated when unavailable -- verify/cull |
| 71 | file_decompressed | _apply_decompress:4745 | Gate when nothing to decompress -> cull |
| 75 | file_located | _apply_file_action_result:8206 | Browse cannot target a named file -- likely unreachable (xref: C -- vs 74) |
| 77 | host_analyzed | _apply_analyze_host:4977 | Prevent re-analyze when nothing new -> cull |
| 81 | host_ltg_revealed | _apply_analysis_action_result:7892 | Only reveal if unknown; gate behind trap-door entry (xref: F) |
| 106 | ic_relocate | _apply_locate_ic:5872 | No IC to relocate -> unreachable? cull |
| 109 | ic_slowed | _apply_slow:3918 | Gated by action economy -> cull |
| 110 | ic_slowed | _apply_slow:3937 | No valid targets -> cull |
| 113 | ic_slowed | _apply_slow:4002 | Dead branch? cull |
| 129 | medic_heal | _apply_medic:3205 | Blocked by UI -> cull |
| 130 | medic_heal | _apply_medic:3212 | No medic / worn program -> cull |
| 148 | program_decompressed | _apply_decompress_program:4812 | Gated by action economy -- verify/cull |
| 150 | purge_hog | _apply_direct_action:8424 | Gated by action economy -- verify/cull |
| 155 | relocate | _apply_control_action_result:8060 | Gated when unavailable -> cull |
| 156 | relocate | _apply_control_action_result:8066 | Gated (would not relocate a suppressed IC) -> cull |
| 159 | restore_repair | _apply_restore:3518 | Gated when unavailable -> cull |
| 160 | restore_repair | _apply_restore:3523 | Gated when unavailable -> cull |
| 178 | suppressions_flushed | _flush_pending_suppressions:4092 | When does this fire? cull? |
| 183 | tar_steamrolled | _apply_steamroller:3771 | Gated by action list -> cull |
| 184 | tar_steamrolled | _apply_steamroller:3796 | Gated by action list -> cull |
| 187 | trap_door_entered | trap_door_action:9998 | Logon may be automatic on trap door -- where does this fire? (xref: E) |
| 192 | worm_disinfected | _apply_disinfect:3669 | Blocked by actions -> cull |

---

## C. Duplicate consolidation (verify overlap -> keep the RAW-correct one)

**Status: RESOLVED (2026-07-30).** One genuine consolidation (the logon block); the rest
are the same event type from **different code paths under different conditions** -- not
double-logs. Text fixes applied to 142/143/169.

| Row | Event | Location | Resolution |
|---|---|---|---|
| 43 | dinab_degraded | _dinab_resolve_failure:4285 | DISTINCT -- degrade = -1 (non-botch failure); crash = all-1s botch (rating->0). KEEP both. |
| 70 | enemy_shield_parry | _enemy_shield_parry:2951 | DISTINCT -- enemy-side Shield Test (gm_only) that wears the enemy's Shield program; not the resist roll. KEEP. |
| 100 | ic_attack | _black_ic_final_attack:12008 | DISTINCT flow -- same 2x-MPCP mechanic/text, but fires on jack-out (final attack) vs 98 on the IC's own pass. Both needed. KEEP. |
| 103 | ic_crashed | attack_ic:9301 | KEEP both -- 102 (`_apply_ic_crash`) is the shared helper for DINAB/area strikes; 103 is attack_ic's richer inline event. Different crash sources. |
| 112 | ic_slowed | _apply_slow:3975 | DISTINCT -- 111 = to-hit miss, 112 = opposed-resist loss. KEEP both. |
| 125 | logon | perform_action:8903 | DONE -- consolidated the duplicated logon block into `_complete_logon`; 124 = resume-after-defense path, 125 = direct path, now one emit site. |
| 136 | one_shot_spent | _spend_one_shot:1798 | MUTUALLY EXCLUSIVE -- 135 = multi-copy (`one_shot_active` dict) path; 136 = legacy fallback for runs without the dict. Never both fire; 136 is backward-compat. KEEP. |
| 142 | persona_crash | _resolve_ic_cybercombat:7026 | DE-CAPS'd. Not a duplicate -- the only NON-black-IC persona crash (Killer/Blaster/Sparky). KEEP. |
| 143 | persona_crash | _advance_npc_pass:7528 | DE-CAPS'd. Not a crit mechanic -- `crit` is the meat-monitor-full text; it's the Black-IC death announcement, distinct from 144 (icon crash). KEEP. |
| 163 | scramble_attack | crash_scramble:9429 | KEEP -- Scramble has unique reactions (Poison erase, Exploding bomb) not in the generic IC path. Unifying is an architectural refactor, not a de-dup. |
| 164 | scramble_crashed | crash_scramble:9460 | KEEP -- same as 163 (scramble crash carries the bomb/tally reactions). |
| 168 | shield_parry | _shield_parry:2922 | DISTINCT -- 168 = PC Shield Test (player-visible); 70 = enemy Shield Test (gm_only). KEEP both. |
| 169 | shutdown | _process_host_shutdown_countdown:10121 | DONE -- text aligned with the crash end-state ("Host shutdown, dumped -- System Offline. Dump Shock: N (M boxes). Run complete."). |
| 172 | shutdown_tick | _process_host_shutdown_countdown:10165 | DISTINCT -- secret-sensor tick (gm-only, decker unaware). Not a dup of 170 (detected) or 173 (warning). KEEP. |
| 173 | shutdown_warning | _process_host_shutdown_countdown:10133 | DISTINCT -- the host announces shutdown (final-warning turn). Not covered by 170 (secret sensor detect). KEEP. |

---

## D. View / redaction decisions (GM vs admin vs player)

**Status: DONE (2026-07-30).** Suite green (1207). Redaction rule confirmed: the `gm_only`
flag already scopes an event to the admin view, so the literal "GM:" / "(GM)" text prefixes
were redundant and were dropped.

| Row | Event | Location | Resolution |
|---|---|---|---|
| 6 | armor_wear | _wear_armor:3096 | DONE -- merged the two branches into one `_append_event`; enemy branch stays `gm_only` (admin), PC branch player-visible; dropped the "GM:" prefix. |
| 8 | bouncer_completed | _complete_pending_bouncer:5479 | DONE -- admin text now "Bouncer upgrade complete: {code} {value}." ("(GM)" dropped; stays `gm_only`); player `bouncer_warning` unchanged. |
| 56 | enemy_decker | _drain_all_hog_infections:10888 | DONE -- dropped "GM:" prefix ("Your Hog virus drains {target}'s program: ..."); stays `gm_only`. |
| 58 | enemy_decker | _enemy_purge_hog:10939 | DONE -- now player-visible: "{enemy} unsuccessfully attempts to purge your Hog program from their deck." |
| 61 | enemy_decker | _enemy_decker_take_turn:11046 | DONE -- now player-visible + simplified: "{enemy} re-emerges from hiding to resume the hunt." (fires when a hidden wounded Medic-carrier heals to the reengage threshold and drops its hide). |
| 69 | enemy_decker_injected | _spawn_enemy_decker:2209 | KEEP hidden (correct -- players must not learn a decker was dispatched). Final-disposition-in-AAR tracked in workstream G. |

---

## E. Clarifications

**Status: ANSWERED (2026-07-30).** Reclassifications: row 65 -> KEEP (it is the >=10
crash-out backstop, not an action); row 186 -> F (tar crash bumps tally but registers no
suppression offer). Rows 4 & 83 also got de-CAPS edits and are DONE.

| Row | Event | Location | Resolution |
|---|---|---|---|
| 3 | action | perform_action:8857 | VERIFIED -- redaction appends the tally line only when the tally actually increases |
| 4 | area_attack | area_attack:11865 | ANSWERED -- render artifact. Real output lists each target's damage level + boxes then a crash count (not just crashes). De-CAPS'd to "Area strike"/"crashed". DONE |
| 9 | crash_host_aborted | _process_crash_countdown:10073 | ANSWERED -- fires during the Crash Host countdown when the host's abort roll (Security Value vs decker MPCP) succeeds and cancels it. Reached via Crash Host -> end-of-turn processing. |
| 18 | data_bomb_defuse | _apply_defuse_bomb:5288 | ANSWERED -- `df["detonated"]` = decker rolled all 1s (botch); text already says "botched -- the protected bomb detonates." The net-successes in the catalog is a SAMPLE artifact (real botch = 0 decker successes). No change. |
| 39 | dinab_attack | _dinab_strike_decker:4497 | ANSWERED -- crippler branch (Poison/Restrict/Reveal). reduction>0 = "cripples {attr}"; reduction<=0 = "{name} resisted your DINAB" (yes, the resist case). |
| 41 | dinab_attack | _dinab_strike_decker:4539 | ANSWERED -- the straight Attack DINAB (persona damage via cybercombat), distinct from 39 (attribute cripplers). Trigger: util is neither a crippler nor hog. |
| 44 | dinab_op | _dinab_operate:4362 | ANSWERED -- catalog artifact. `_dinab_operate` runs OPERATIONAL DINABs vs a subsystem; the Attack utility routes to `_dinab_offense`, never here. Generator sampled util="attack". |
| 65 | enemy_decker | _enemy_decker_take_turn:11016 | ANSWERED / KEEP (not cull) -- this IS the >=10 crash-out backstop (enemy forced out, status="fled"), not the enemy attacking. It's the separate crash-out entry you wanted. |
| 83 | ic_activation | _spawn_trap_hidden:9036 | ANSWERED + DONE -- catalyst = crashing a Trap IC in cybercombat OR a Trap-Trace IC completing its location cycle. De-CAPS'd to "Trap triggered". |
| 85 | ic_analyzed | _apply_analysis_action_result:7781 | ANSWERED -- a failed Analyze logs the generic "Analyze IC -- FAILED" host_system_test line; ic_analyzed is only the success-side reveal. No separate failed event by design. |
| 87 | ic_attack | _resolve_ic_cybercombat:7034 | ANSWERED -- Blaster mechanic: when its hit crashes the persona (>=10 boxes) it makes an MPCP-damage test as the decker is dumped. "post-crash" = on the persona crash. |
| 88 | ic_attack | _resolve_ic_cybercombat:7057 | ANSWERED -- Sparky "discharge on crash" fires ONLY when the strike fills the persona monitor (>=10), not every attack. Same crash gate as Blaster. |
| 116 | icon_scanned | scan_enemy_decker:11681 | ANSWERED -- fires from the Scan Icon action vs a revealed enemy decker (Computer Test vs Masking); each net success reveals a hidden rating. The Analyze-Icon equivalent for a hostile decker. |
| 138 | paydata_aar | _finalize_paydata_haul:10652 | ANSWERED -- yes. Emits a generic player `paydata_secured` event PLUS a GM-only `paydata_aar` with the full per-file breakdown. Confirmed fine. |
| 186 | tar_steamrolled | _apply_steamroller:3847 | ANSWERED / -> F -- crashing tar adds its rating to the tally (minus Skulk) like any crash, BUT the Steamroller path does not register a suppression offer the way a normal Attack crash (`_apply_ic_crash`) does. Likely inconsistency -- moved to workstream F. |

---

## F. Logic / behavior fixes (real concerns)

**Status: RESOLVED (2026-07-30).** Suite green (1207). One found to be a non-bug (179);
one partial (157 -- text simplified, full modal flagged as a follow-up).

| Row | Event | Location | Resolution |
|---|---|---|---|
| 62 | enemy_decker | _enemy_decker_take_turn:11073 | DONE -- "A hostile decker ({name}) is hunting your icon." Dropped the misleading "Evade (Relocate/Redirect)" advice: those target trace IC, not enemy deckers. |
| 144 | persona_crash | _advance_npc_pass:7551 | DONE -- backend: added `icon_crashed` guard to the `/logoff` endpoint (the `/action` path already blocked it). Frontend: when `icon_crashed` the action console shows ONLY Jack Out. |
| 157 | relocate | _apply_control_action_result:8075 | DONE -- the release-then-suppress modal already exists (`checkSuppressionModal` + `_releaseCandidates`): at the DF floor it lists releasable suppressions with Release buttons and re-opens after a release so you can suppress the held trace. Log line trimmed to a concise record. |
| 166 | scramble_poison | _scramble_poison_react:477 | DONE -- "The Poison IC erased the protected data." / "The Poison IC attempted to erase the data, but failed." |
| 179 | swap_memory | _apply_direct_action:8328 | FIXED (generator, app was always correct) -- `_dict_assigns` now records tuple-unpack targets and the resolver renders a function-return description as dynamic. The catalog shows swap_memory as "(dynamic -- description returned by _apply_swap_memory())" instead of the misattributed purge text. |
| 186 | tar_steamrolled | _apply_steamroller:3847 | DONE -- crashing a tar now registers a suppression offer (like a crashed IC / Scramble), so the decker can absorb 1 DF to refund the tally; de-CAPS'd "CRUSHES". |

---

## G. AAR content

**Status: DONE (2026-07-30).** Added `_finalize_enemy_decker_aar` to the run-end hook
(`_finalize_run_end`); it emits a GM-only `enemy_decker_aar` summarizing every dispatched
decker's final disposition. Suite 1209 (2 regression tests added).

| Row | Event | Location | Resolution |
|---|---|---|---|
| 29 | decker_lethal | attack_enemy_decker:11562 | DONE -- the per-hit decker_lethal event already reports the fate (killed / knocked out / crashed); the new run-end `enemy_decker_aar` summarizes each decker's name + disposition for GM review. |
| 69 | enemy_decker_injected | _spawn_enemy_decker:2209 | DONE -- the new GM `enemy_decker_aar` lists every dispatched decker's final disposition (killed / knocked out / crashed / fled / evaded / still active). The injected event stays hidden. |
| 138 | paydata_aar | _finalize_paydata_haul:10652 | VERIFIED -- `_finalize_paydata_haul` emits the gm_only `paydata_aar` (per-file breakdown) + a generic player `paydata_secured`. Confirmed fine. |

---

## H. Catalog render artifacts (already corrected in v2 -- no app change)

These notes reacted to catalog mis-renders that the generator fix already resolved.
Re-read them in `docs/event-log-catalog-v2.csv` to confirm, then close.

| Row | Event | Location | Status |
|---|---|---|---|
| 16 | data_bomb | _apply_defuse_bomb:5320 | AUTO -- stray '3' was a render artifact |
| 25 | decker_attack | attack_enemy_decker:11604 | AUTO -- now renders "You strike <name> -- <level> (<boxes> boxes)" |
| 26 | decker_crippled | attack_enemy_decker:11452 | AUTO -- confirm generic across Marker/etc. in v2 |
| 27 | decker_hog | attack_enemy_decker:11412 | AUTO -- now renders the Hog line, not Crippler |
| 66 | enemy_decker | _enemy_decker_take_turn:11198 | AUTO -- now references the Hog program |
| 67 | enemy_decker | _enemy_decker_take_turn:11222 | AUTO -- now references the correct program |
| 68 | enemy_decker | _enemy_decker_take_turn:11290 | AUTO -- failure state of row 67, now correct |

---

## Category counts

| Cat | Workstream | Notes |
|---|---|---|
| A | Text / flavor / de-CAPS | 61 |
| B | Cull / gating verification | 26 |
| C | Duplicate consolidation | 15 |
| D | View / redaction | 6 |
| E | Clarifications | 15 |
| F | Logic fixes | 5 |
| G | AAR content | 3 |
| H | Render artifacts (no change) | 7 |
| | **Total noted rows** | **136** (of 197) |
