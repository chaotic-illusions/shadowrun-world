# Matrix Run -- System Operation Corrections

Working checklist for correcting the SR2/VR2.0 system operations against **RAW** in
[`vr2_rules.md`](../vr2_rules.md), subject to the user's amendments captured below.

## Workflow
- Corrections are processed **one at a time, each in a fresh context window** (subagent per item).
- An item is **done** when the app's behavior matches RAW in `vr2_rules.md`, *as amended by the
  user's correction* recorded here.
- Validate after each item: `python -m py_compile` changed files, `python -c "import app.main"`,
  `python -m pytest -q`, and `node --check` on extracted `<script>` blocks for frontend edits.
- Grounding run for manual verification: **matrix_runs.id = 1** (decker "Static", host "Test",
  Green-6, ACIFS 8/9/8/10/10, logged on, init 26). See `/memories/session/active-matrix-run.md`.

## Status legend
`[ ]` pending &nbsp; `[~]` in progress &nbsp; `[x]` done &nbsp; `[?]` blocked on open question

## Key source anchors
- Backend dispatch: [`app/routers/matrix_runs.py`](../app/routers/matrix_runs.py) `perform_action` (~L2550)
- Action economy gate: `_spend_pass_action` (~L662)
- Serializer / redaction: `_serialize_run` (~L202)
- Engine tests: [`app/services/matrix_engine.py`](../app/services/matrix_engine.py) `system_test` (L67)
- Frontend catalog: [`frontend/matrix-run.html`](../frontend/matrix-run.html) `ACTION_CATALOG` (~L1663),
  `ACTION_SUBSYSTEM` (~L1549), `ACTION_UTILITY` (~L1584), `performAction` (~L3440)

---

## 1. Analyze Host -- successes reveal one subsystem rating each; 5+ reveals all
- **Status:** `[x]` -- Extracted `_apply_analyze_host` (reveal-all when `net>=5` or `net>=hidden`,
  else bank `host_analyze_pending`) + `_reveal_host_ratings` two-phase picker; added
  `POST /{run_id}/reveal-host-ratings` (`RunRevealHostRatingsInput`); frontend selection modal +
  "Reveal subsystem ratings (N)" button; fixed the matrix_rules tip; `TestAnalyzeHostReveal` (8 tests).
- **RAW** (`vr2_rules.md` L1863): "For each success, decker chooses one piece of info: host
  Security Rating, one subsystem rating, or whether host is a VM. **7+ successes reveals all**
  available info. Decker must be logged on to the host (not the grid)."
- **USER OVERRIDE / SCOPE (Q&A):**
  - Threshold is **5+** net successes = reveal ALL (not RAW's 7+).
  - **VM status is NOT used in this app** -- hosts are hosts, physical or virtual. Do NOT model or
    reveal it (do NOT add an `is_vm` flag).
  - **Host Security Rating is already known** to the player (revealed when the host is revealed) --
    it is NOT part of the Analyze Host reveal set.
  - Therefore the revealable set is exactly the **5 ACIFS subsystem ratings**
    (Access, Control, Index, Files, Slave).
  - Fewer than 5 net successes: the player **chooses** which still-hidden ratings to reveal,
    **one per net success**, via a **selection modal (Option B, two-phase: roll -> pick)**.
- **Current behavior:** auto-reveals ACIFS ratings in FIXED order, one per net success; no player
  choice; no 5+ "reveal all" threshold. (`perform_action` analyze_host handler ~L3027)
- **Planned fix:**
  - Extract the analyze_host success logic into a pure helper. On success with `net` net successes
    and `U` still-hidden ratings: if `net >= 5` OR `net >= U` -> auto-reveal ALL hidden ratings (no
    modal); elif `1 <= net < U` -> bank `state["host_analyze_pending"] = {credits: net, turn}` and
    reveal nothing yet (a later roll REPLACES pending; auto-reveal clears it).
  - Add a `POST /{run_id}/reveal-host-ratings` endpoint (new `RunRevealHostRatingsInput{subsystems}`)
    + pure helper `_reveal_host_ratings(state, subsystems)` that validates the picks are valid ACIFS
    names, currently hidden, and number exactly `min(credits, U)`; reveals them; clears pending.
  - Frontend: when `host_analyze_pending.credits > 0`, present a selection modal listing the hidden
    subsystems; require exactly `min(credits, hiddenCount)` picks; submit via `apiFetch` then refresh.
    `renderHostRatings` already displays revealed ratings.
  - Fix the misleading tip in `app/services/matrix_rules.py` L370 (drop "security rating"/"VM
    status"; say it reveals one ACIFS subsystem rating per success, 5+ reveals all).
- **Acceptance:** 5+ (or net >= hidden count) auto-reveals all remaining; else a selection modal lets
  the player reveal exactly one hidden ACIFS rating per net success.

## 2. Analyze Security -- reveal tally (incl. this test) + alert status
- **Status:** `[x]` (verified -- no code change needed)
- **RAW** (L1863): "Reveals current Security Rating of the host, the decker's security tally
  (including tally points accrued by this test), and the host's alert status."
- **USER:** in addition to current tally (including this test's increase), also learn the **alert
  status**. (Confirms RAW.)
- **Current behavior:** snapshots `{tally, alert, turn}` into `security_known` and reports both.
  Appears to already satisfy this -- **verify** the tally shown includes this test's increase and
  alert is surfaced in the UI. (analyze_security handler ~L2990)
- **Acceptance:** matches RAW; mostly a verification item.
- **VERIFICATION (done):** All three RAW reveals present.
  1. *Security Rating:* always shown once logged on -- `run-sec-code`/`run-sec-value`
     (matrix-run.html L420, populated L2648-2649). Already-known premise from #1 holds.
  2. *Tally incl. this test:* generic tally bump `state["security_tally"] = old_tally +
     test["tally_increase"]` (matrix_runs.py L3057) runs BEFORE the analyze_security snapshot
     `{"tally": state["security_tally"], ...}` (L3154-3160), so the snapshot includes this test's
     own increase.
  3. *Alert status:* captured in snapshot (`alert`) and surfaced in the UI as `Last Scan -- Tally
     X, Alert Y (turn N)` (matrix-run.html L2671-2675) plus the alert badge (L2651).
  No code change required.

## 3. Analyze Subsystem -- restrict dropdown to subsystems that can hold defenses
- **Status:** `[x]`
- **RAW** (L1864): "Identifies anything out of the ordinary on the targeted subsystem: **trap
  doors, worm IC, scramble IC, and other defenses or system tricks.**" Trap doors sit on the
  concealing (non-Access) subsystem, typically Slave (L312-321). Scramble protects Access, Files,
  or Slave (L491). Access analysis also reveals this host's LTG-access status.
- **USER:** remove any subsystem from the dropdown that cannot contain these defenses -- selecting
  it just wastes player resources. Also: "What is host LTG status, and how is it presented?"
- **What "host LTG status" is:** each host may carry an `ltg_address`. `host_has_ltg = True` means
  the host is reachable **directly from the regular grid**; `False` means it is reachable **only via
  a direct line or a trap door** from another host. Analyze Subsystem on **Access** is the *only* way
  to learn this (`host_ltg_revealed` flips, then `host_has_ltg` is shown). This app does **not**
  implement scramble on Access, so this LTG-status reveal is Access's *sole* "out of the ordinary"
  payload.
- **DECISION (user):** keep **Files** and **Slave** (guaranteed -- they hold scramble/worms/trap
  doors). **Remove Control and Index** (no defenses live there -> no benefit). **Access** stays
  because it reveals host LTG status (its only payload); say the word if you'd rather drop it too and
  cut the list to Files/Slave.
- **Planned fix:** dropdown = **Access, Files, Slave**; remove Control and Index. Update
  `ACTION_SUBSYSTEM`/the subsystem picker for `analyze_subsystem` accordingly.
- **DONE:** subsystem picker (only used by Analyze Subsystem -- sole action with `subsystem:true`)
  trimmed to Access / Files / Slave in matrix-run.html (Control, Index, and the stray non-host
  Sensor option removed). `ACTION_SUBSYSTEM.analyze_subsystem` default changed `'control'` ->
  `'access'` so the auto-select lands on a valid option. Backend already accepts all subsystems and
  finds nothing on the removed ones, so no backend change needed. Validated: get_errors clean,
  text-hygiene passed.

## 4. Locate Paydata -- 1 paydata point per NET success (chosen at random)
- **Status:** `[x]`
- **RAW** (L1878 / L992): "Ongoing operation. **Each net success locates 1 Paydata Point.**
  Continues until stopped or all paydata found. Once located, paydata must be downloaded in its
  entirety." L992: successes determine how many points are discovered, up to the Paydata Points
  result; must download the file completely to gain 1 point.
- **USER:** each net success reveals **one** paydata point, **chosen at random** (not all-at-once).
- **Current behavior (BUG):** a single success reveals **all** undiscovered paydata at once.
  (locate_paydata handler ~L3100)
- **Planned fix:** reveal `min(net_successes, remaining)` random undiscovered paydata entries.
- **Acceptance:** N net successes -> N random files revealed; repeatable until all found.

## 5. Locate IC -- re-detect an IC that evaded you (depends on #19)
- **Status:** `[x]`
- **RAW** (L1884, L1998-1999): Locate IC is "System Test only -- IC is auto-located if the System
  Test succeeds; IC remains located unless it maneuvers to evade detection."
- **USER RULING (overrides RAW L1998's "Analyze Icon" wording + the old note below):** the
  re-detect vector for an evaded **IC** is **Locate IC**; for an evaded **decker** it is **Locate
  Decker** (symmetric). These operations re-acquire **only icons that have EVADED** (previously
  detected, then hid via the Evade Detection maneuver) -- they do **not** reveal never-seen /
  undiscovered icons. (Otherwise you could discover an entire system at once, against RAI; a
  never-seen icon instead betrays itself by acting.) A hit clears the evade tag and the icon is
  visible/targetable again (it then appears in the Attack target list). You cannot target an evaded
  icon by id -- you don't know where it went -- so the operation sweeps the evaded icons.
- **DONE** -- both re-detect operations implemented (`app/routers/matrix_runs.py`):
  - **`_apply_locate_ic(state, *, test_success)`** -- Locate IC: a System Test ONLY (no Sensor
    Test, RAW L1884). On success it re-detects EVERY currently-evaded IC (`evade_dir ==
    "hid_from_pc"`) via `_clear_evade(..., redetected=True)` (strips the evade markers so
    `_serialize_run`/`_redact_ic` shows the IC again and logs a RE-DETECT notice). Emits an
    `ic_relocate` `none`/`fail` event when there is nothing to re-locate or the test failed.
  - **`_apply_locate_decker(state, decker, *, test_success, scanner)`** -- Locate Decker: the
    Index System Test gates the attempt, then the #6 opposed Sensor Test vs the enemy's FULL
    Masking + Sleaze (`eng.pc_locate_decker_test`, Scanner reduces the TN) decides each
    re-acquisition; a located enemy has its evade cleared and `revealed` restored. Reuses the
    `scan_hit` / `scan_clear` / `scan_fail` events (existing frontend badges).
  - Dispatched from `perform_action` (`if body.action_type == "locate_ic" / "locate_decker"`).
    Both were already in the schema `ActionType` + the frontend ACTION_CATALOG; no target selector
    needed (sweep). No frontend change required (the `re_detect` RE-DETECT badge and `scan_*`
    badges already exist).
  - **Behavior change:** Locate Decker no longer reveals never-revealed *hunters* (it is now
    evaded-only). Enemy deckers still auto-reveal when they start hunting (the enemy turn sets
    `revealed=True`), so the PC is not blinded. The asymmetry (Locate IC = pure System Test;
    Locate Decker keeps the #6 opposed Sensor Test) is RAW-faithful -- L1884 is IC-specific.
  - Tests: `TestLocateReDetect` (8) in `test_vr2_matrix_scenarios.py` -- Locate IC re-detect /
    failed-test-leaves-hidden / no-evaded-none; Locate Decker re-detect / full-mask+sleaze (#6) /
    ignores-never-revealed-hunter / failed-Sensor-leaves-evaded / failed-Index-skips-Sensor.
- **Acceptance:** matches RAW L1884 + the user ruling; full suite green (530 tests).

## 6. Locate Decker -- compare Sensor Test vs enemy full (Masking + Sleaze)
- **Status:** `[x]`
- **RAW** (L1880): "Two-step: Index Test + Sensor Test. Locates other deckers whose **Masking <=
  decker's Sensor Test result. If target runs Sleaze, add its rating to target's Masking** for
  detection purposes."
- **USER:** compare Sensor result against the enemy's **full Masking + Sleaze** (NOT halved like a
  player's own Detection Factor). Keep the "None detected" message even on a failed test (good feature).
- **Also (per #19, DONE in #5):** Locate Decker re-detects an *evaded* decker -- a successful test
  now clears the enemy's `evaded` flag and restores `revealed` (see #5 `_apply_locate_decker`).
- **Current behavior (BUG, fixed):** `pc_locate_decker_test` used to compare against
  `enemy.detection_factor` (= **halved** masking+sleaze), understating the threshold.
  (engine `pc_locate_decker_test`; handler now `_apply_locate_decker`)
- **Fix:** uses enemy **Masking + Sleaze (full)** as the TN/threshold.

## 7. Validate Passcode -- simplified house rule
- **Status:** `[x]` -- DONE. Implemented the house rule exactly inline in `perform_action`
  (`matrix_runs.py`). The Validate Passcode System Test now rolls at **+2 TN**
  (`if action_type == "validate_passcode": tn_modifier += 2`); a **net success** sets both
  `has_legitimate_status` (IC Legitimate TN column, unchanged) and a new run-wide
  `passcode_tn_bonus` flag that applies **-2 TN to every OTHER System Test for the rest of the run**
  (`elif state.get("passcode_tn_bonus"): tn_modifier -= 2` -- the `if/elif` split means the buff
  never discounts the validate test itself). A **failed** plant sets `validate_passcode_attempted`;
  a guard placed **before** `_spend_pass_action` raises HTTP 400 on any retry (one-shot), and the
  security tally still rises by the host's opposed successes through the normal generic bump -- the
  engine's `tally_increase` IS the host successes and is already added on failure, so no separate
  tally code was needed. Frontend `matrix-run.html`: the `validate_passcode` action is gated
  `valid: s => !s.has_legitimate_status && !s.validate_passcode_attempted`, and a green
  `PASSCODE -2 TN` status badge shows while the buff is active. Tests: `TestValidatePasscode`
  (6 tests) drive the real `perform_action` and assert the +2/-2 TN math, both success flags, the
  one-shot lockout, and tally-on-fail.
- **RAW** (L1899): plants a fake passcode; Legitimate status; lasts 1D6 x successes days; deleted on
  active alert. (Full rules deeper -- user simplifies below.)
- **USER (authoritative house rule):**
  - Test TN is **+2**.
  - If **net successes >= 1**: **all other System Tests get -2 TN for the rest of the run.**
  - If the test **fails**: it **cannot be attempted again**, and the **security tally increases by
    the number of opposed (host) successes regardless.**

## 8. Decoy -- persistent decoy with its own 10-box Condition Monitor
- **Status:** `[x]` -- DONE. Verified the engine already implements the amended RAW and locked it in
  with tests. **USER DECISIONS (this pass):** at most ONE decoy (a new Decoy operation replaces the
  old one); keep the redirect at **1D6 <= successes**, because RAW's "ties go to the decoy" resolves
  a tie (d6 == successes) in the decoy's favour -- strict `<` would send ties to the *decker*,
  contradicting that clause. The OPEN Q is therefore resolved as **keep `<=`** (no behavior change).
  Extracted `_decoy_intercept` from the `perform_action` IC-attack loop (behavior-preserving) so the
  rule is unit-testable: a live decoy (Control successes recorded, its 10-box CM not yet full) draws
  a proactive IC attack on 1D6 <= successes; the decoy has NO defences and eats the IC's fully
  staged-up damage with no resistance roll (`stage_damage(base, atk_successes, +1)`), accruing boxes
  on its own 10-box Condition Monitor and being removed once it fills (successes + hp reset to 0).
  Trace IC never reach the check (the loop skips them first), so decoys stay correctly ineffective
  vs trace. **Pre-emptive summoning already works:** the Decoy action is ungated in `ACTION_CATALOG`
  and the decoy persists in run state, so a decoy summoned before combat intercepts proactive IC as
  they activate. Frontend already renders the `DECOY n/10` CM badge and logs `decoy_deployed` /
  `decoy_intercepted`. (The prior "Current behavior" note below was stale -- per-hit damage accrual
  and removal-at-10 were already implemented.) Tests: `TestDecoyIntercept` (6 tests) in
  `test_vr2_matrix_scenarios.py`.
- **RAW** (L1871): "Record Control Test successes; when proactive IC attacks the decker, roll 1D6 --
  if result < successes, IC attacks the decoy instead (ties go to the decoy). **Decoys have no
  defenses, take full damage, and disappear when their Condition Monitors fill.** Not effective
  against trace IC."
- **USER:** track that decoys take full damage -> each decoy needs its **own Condition Monitor**
  (10 boxes) and is removed once full. Allow **summoning a Decoy up front** so it can be targeted by
  proactive IC when they activate.

## 9. Dump Log -- REMOVE entirely
- **Status:** `[x]`
- **DECISION (user):** the host log only ever contains the player's own access, so Dump Log has no
  intel value -> **remove the operation entirely**: frontend `ACTION_CATALOG` entry, backend
  `_apply_dump_log` handler + dispatch, `_ACTION_COST["dump_log"]`, any `ACTION_UTILITY`/
  `ACTION_SUBSYSTEM` entries, and any tests/UI referencing it.
- **DONE** -- fully excised across backend, engine, schema, frontend, and tests:
  - Backend `app/routers/matrix_runs.py`: removed `_apply_dump_log` handler, its dispatch block in
    `perform_action`, the `_ACTION_COST["dump_log"]` entry, and the `access_log_dumped` state key
    (+ comment) from `_initial_state`.
  - Engine `app/services/matrix_engine.py`: removed the whole Dump Log section --
    `host_difficulty_tier`, `build_access_log_summary`, and the `_LOG_SIZE_MULTIPLIER` /
    `_LOG_USER_HANDLES` / `_LOG_FILE_NAMES` / `_LOG_PROGRAMS` flavour pools (used nowhere else).
  - Schema `app/schemas/matrix_run.py`: dropped `"dump_log"` from the `ActionType` literal (the
    action is now rejected at the request boundary).
  - Frontend `matrix-run.html`: removed the `ACTION_CATALOG` entry, the `ACTION_SUBSYSTEM` /
    `ACTION_UTILITY` map rows, the `run-access-log` panel element, the `renderAccessLog` function +
    its `renderRun` call, and the `log_dumped` event-log case. Trimmed "Dump Log" from the Validate
    utility tooltip (matrix-run + `deck-workshop.html`).
  - Tests `tests/test_vr2_matrix_scenarios.py`: removed the `TestDumpLog` class (10 tests) and
    repointed the trace-IC hunt driver (which used `dump_log` only as a generic vehicle) to
    `null_operation` (also Complex, no success handler -- a clean drop-in).
- **Acceptance:** Dump Log no longer appears in the picker; handler/cost/maps removed; suite green
  (504 passed, down 10 from 514; no other test touched).

## 10. Null Operation -- auto-run only during a multi-turn Download
- **Status:** `[x]` -- DONE.
- **RAW** (L1256-1266 I/O Speed; L1873 Download Data; L992 file size = data density; L1512-1515
  Compressor; L1892 Null Op "performed while waiting"): Download Data is an ongoing op transferring
  at the deck's **I/O Speed** (a transfer RATE). File size in Mp = its data density. A Compressor
  halves the transferred size within a Rating x 100 Mp cap.
- **DECISION (user):**
  - **Upload Data is OUT of scope** -- this app has no files to upload.
  - **Locate Paydata** stays a normal, repeatable action that remains available until all paydata is
    found (do **NOT** convert it into an auto-advancing background op) -- covered by #4.
  - **Download Data** becomes multi-turn for large files; on each **idle turn** the download forces,
    the app **auto-performs Null Operation** and adds any host successes to the tally.
- **USER RULING (this pass):**
  - Duration = `turns = ceil(stored_Mp / io_speed)`. The doc's earlier `.../3` was a doc
    extrapolation (it assumed io_speed was Mp/second) and is **NOT in RAW** -- rejected. This app's
    `io_speed` schema field is already **Mp per Combat Turn** (`schemas/matrix_run.py` L84), so the
    turn count is a direct ceiling with no `/3`.
  - `stored_Mp` = the **compressor-effective** footprint (halved within the Rating x 100 cap, else
    full) -- exactly `_compressed_store_size(...)`. A Compressor that can handle the file both
    shrinks its on-deck size AND shortens the transfer; an oversized file transfers full.
  - Transfer model = **background**: the starting Download is a Simple action (moves the first
    turn's worth); each subsequent **New Turn** auto-rolls a Null Operation (Control System Test,
    Computer skill, NO Hacking Pool), the host's Security Test adds to the tally, and the sheaf may
    wake. While a transfer runs the decker may take only **Free** actions and cannot start a second
    download.
  - Interruption (log off / dump / host crash) before completion **corrupts** the partial copy --
    no storage charged, no paydata credited (a Paydata Point needs the COMPLETE file, L992).
- **Current behavior (BUG, fixed):** `null_operation` had no handler and Download completed
  instantly in a single action regardless of file size or I/O Speed.
- **Fix:** in `app/routers/matrix_runs.py`, five module helpers -- `_download_turns`
  (`ceil(stored/io)`, legacy `io<=0` -> 1 turn), `_complete_download` (lands the file: marks it
  downloaded, charges the compressor-effective storage, writes the ledger entry, emits
  `data_downloaded`; idempotent), `_auto_null_operation` (Control System Test at Computer skill, no
  Hacking Pool; host successes add to tally), `_corrupt_active_download` (clears the transfer, emits
  `download_corrupted`), and `_tick_active_download` (auto Null Op -> decrement -> complete on 0, or
  corrupt if the source file was destroyed mid-transfer). `_initial_state` gains
  `active_download: None`. The Download Data success path computes `turns`; `turns <= 1` completes
  at once, else it sets `active_download` and emits `download_started`. A guard before
  `_spend_pass_action` refuses any non-Free op while a transfer runs (distinct message for a second
  `download_data`). `new_turn` ticks the transfer after the Hog loop; corruption hooks fire in
  `new_turn` (host crash / run end), `perform_action` (run end), and `graceful_logoff` (success).
  Front end (`matrix-run.html`): event badges for `download_started` / `null_operation` /
  `download_corrupted`, plus a download-in-progress banner (file, turns left, progress bar) in the
  paydata/storage panel. Tests: `TestDownloadMultiTurn` (19 cases) in
  `tests/test_vr2_matrix_scenarios.py`.
- **Deliberate minimal choices (noted, not gaps):** enemy deckers/IC are **not** independently
  driven inside the tick (the rising tally + sheaf is the escalation, matching the existing model
  that only drives NPCs in `perform_action`); the `/attack` endpoint is **not** blocked during a
  transfer (the decker must still be able to defend); the SV **inactivity** modifier (<10s base /
  <1min +1 / ...) is not modeled -- a background transfer is a single continuous op resolved in
  Combat Turns, so the base SV applies throughout.

## 11. Analyze Icon -- disable when there is no valid icon target
- **Status:** `[x]`
- **RAW** (L1863): "Scans **any icon**... reduce Control Test TN by Sensor Rating + Analyze utility;
  minimum TN 2." **Data-bomb** detection = Analyze Icon on the protected file/device (L463).
  (Scramble IC discovery is Analyze **Subsystem** -- see #17.)
- **USER:** at this point in the run no slave devices have been found, so the generic "Slave device"
  target is invalid -> **Analyze Icon should be disabled** until there is a real icon to scan.
  "I don't understand why you didn't catch this."
- **Current behavior:** `_analyzeIconTargets` falls back to a generic `slave::__device__` option
  when the host declares no named devices, so Analyze Icon is always offered. (~L1653)
- **Planned fix:** offer Analyze Icon only when there is a real target (a located file, or a
  **discovered** slave device); remove the generic fallback; disable with reason otherwise.

## 12. Swap Memory -- UI: swap-out picker, no HP dice, AP-gate the Perform button
- **Status:** `[x]` (frontend-only; backend `_apply_swap_memory` already supported `swap_out_program`)
- **RAW** (Swap Memory row): "Loads a utility from storage to active memory (or vice versa). **If
  insufficient active memory, first spend a Free Action to unload a program.** No tests required."
- **USER:** (a) surface a **swap-out selector** so an incoming program can replace an active one
  (currently impossible in UI); (b) **hide the HP dice** field for Swap Memory (no test);
  (c) the **Perform button must disable when there aren't enough Action Points** -- this is broken
  for **all** actions (Complex/Simple shown as performable with 0 AP).
- **DONE** (all in `frontend/matrix-run.html`, + 2 small `style.css` rules):
  - (a) New `#actionSwapOut` `<select>` (wrapper `#actionSwapOutWrap`, shown only when the catalog
    entry has `swapOut: true`). Populated from `_liveUtils()` (ACTIVE programs, rating > 0) with a
    default "(keep all active)" blank option; `performAction` sends the chosen key as
    `body.swap_out_program`. The existing load-in target still lists storage (`_storeProgs` ->
    `target_program`), so Swap Memory now drives `_apply_swap_memory` Mode 1 *with* a swap-out.
  - (b) `swap_memory` catalog entry flagged `noTest: true`; the HP Dice field got an id
    (`#actionHpWrap`) and `onActionTypeChange` hides it whenever `entry.noTest`.
  - (c) `onActionTypeChange` now computes `affordNow` (current pass), `canAdvance` (`current_pass <
    initiative_passes`) and `possible = affordNow || canAdvance`, gives Perform an id
    (`#actPerformBtn`), sets `btn.disabled = !possible` with a "click New Turn" `title`, and keeps
    the amber `act-cost-short` tag only while `!affordNow && possible` (i.e. "will start a new pass").
    New `.btn:disabled` CSS dims the button and neutralizes its hover glow.
- **AP-gate rationale:** the server auto-advances to the next initiative pass when the current pass
  can't afford an action (each pass refreshes to 2 AP + 1 Free), so an action is only truly
  impossible -- and Perform disabled -- when the current pass can't afford it AND no pass remains
  this Combat Turn. Disabling merely on current-pass exhaustion would break the multi-pass economy
  (the only way to a fresh pass is New Turn, which re-rolls initiative).
- **Note (out of scope):** RAW charges "a Free Action" to unload when active memory is full; the
  backend folds the swap-out into the single Simple Swap Memory action (no extra Free Action). Left
  as-is per the UI-only scope; flag if the extra Free-Action cost should be modeled.

## 13. Medic -- require BOTH persona damage AND Medic loaded in active memory
- **Status:** `[x]` (frontend gate; backend `_effective_medic` already no-ops when unloaded)
- **RAW:** Medic heals icon Condition Monitor boxes (defensive utility). Utilities must be in
  **active memory** to run.
- **USER:** Medic is currently disabled because there's nothing to heal; it should be disabled
  **if EITHER** there's no damage **OR** Medic isn't loaded in active memory. If persona took damage
  but Medic were still in storage, the app must **not** allow a Medic action.
- **Current behavior:** gated only on `persona_boxes > 0` (`_personaHurt`); ignores whether Medic is
  in active memory (Static's Medic-6 is in **storage**, rating 0 active).
- **Planned fix:** enable only when persona is damaged **and** the Medic utility is active (rating > 0).

## 14. Restore -- same gating as Medic
- **Status:** `[x]` (frontend gate; backend `_effective_restore` already no-ops when unloaded)
- **USER:** same as Medic -- disabled unless there is attribute damage **and** the Restore utility
  is loaded in active memory.
- **Current behavior:** gated only on `_attrHurt`; ignores active-memory presence (Restore-6 in storage).
- **Planned fix:** enable only when there is temporary attribute damage **and** Restore is active.

## 15. Steamroller -- tally reduced by Skulk; subject to suppression
- **Status:** `[x]` (verified by inspection -- no code change needed)
- **VERIFICATION:** `_apply_steamroller` crash path already does `skulk = max(0, sr_opts['skulk'])`;
  `if target.get("suppressed"): tally_increase = 0` else `tally_increase = max(0, ic_rating - skulk)`;
  `state["security_tally"] += tally_increase`. Matches RAW L416 (reduce tally by Skulk) + suppression
  (zeroed). Engine damage path covered by `tests/test_matrix_engine.py::TestSteamroller`.
- **RAW** (L416): "If the decker uses a utility with the **Skulk** option to destroy IC, **reduce the
  tally increase by the Skulk rating.**" Suppression (L418-424) avoids the tally increase entirely.
- **USER:** does the tally increase on Steamroller? It should be **reduced by the program's Skulk
  rating** and follow **normal suppression** rules.
- **Current behavior:** `_apply_steamroller` comment claims it adds the tar's rating to tally
  "unless Skulk-masked or suppressed" -- **verify** Skulk reduction + suppression actually apply.
- **Acceptance:** crash tally = tar rating - Skulk; suppression zeroes it (DF -1 while held).

## 16. Slow -- hung IC can be suppressed; else returns next turn
- **Status:** `[x]` -- extracted the suppress/release core into pure helper
  `_toggle_ic_suppression`; the suppress endpoint now accepts a HUNG IC (active + `hung_turn`),
  not just a crashed one, and leaves the tally untouched for a hung IC (Slow adds none) while
  keeping the crash refund/re-add. `new_turn` resume + DF cost were already correct.
- **RAW:** a slowed IC that loses all its actions **hangs** for the turn; suppression rules apply.
- **USER:** if the IC is hung it can be **suppressed** by normal rules; otherwise it **comes back
  next turn** (per RAW).
- **Current behavior:** `_apply_slow` sets `actions_lost`; `new_turn` clears it "unless suppressed."
  **Verify** a hung IC is suppressible and resumes next turn when not suppressed.

## 17. Decrypt File -- require scramble discovered via Analyze Subsystem (Files/Slave)
- **Status:** `[x]` -- DONE. Analyze Subsystem success on Files/Slave now marks any scramble on
  that subsystem `discovered=True` and emits a `scramble_found` event (new helpers
  `_scramble_subsystem` / `_scramble_label` in `matrix_runs.py`, alongside the existing trap-door
  reveal). `_serialize_run` surfaces `discovered_scrambles` for non-admins -- only
  `{target_key, subsystem, label}`, never the rating/variant (Poison/Exploding stay GM-only; raw
  `scrambles` is still popped). The Decrypt File handler now matches the target by full `target_key`
  among **discovered** scrambles (with a bare-name, case-insensitive fallback), so it targets the
  RIGHT scramble instead of falling back to `scrambles[0]`; when nothing discovered matches it
  refuses with a "No discovered scramble ... Analyze the Files/Slave subsystem first" event and runs
  no test / adds no tally. Failed-decrypt paydata lookup keys off the scramble's file name.
  Frontend `matrix-run.html`: `decrypt_file` gated on `_discoveredScrambles(s).length > 0` and offers
  a select of discovered scrambles (value = `target_key`); added a `scramble_found` badge and a
  `NO SCRAMBLE` badge for the refusal event. Tests: `TestScrambleDiscovery` (8 tests) in
  `test_vr2_matrix_scenarios.py`.
- **RAW** (Decrypt File row): "Defeats scramble IC protecting a specific file. **Must be performed
  before other operations on a scrambled file.**" Decrypt adds no tally (L495). Scramble IC is
  listed under **Analyze Subsystem** (L1864).
- **DECISION (user):** scramble IC is discovered by an **Analyze Subsystem** test on the subsystem
  that can hold it. In this app scramble exists **only on Files and Slave** (run 1: a Files scramble
  on "Lone Star IC Design" and a Slave scramble on "LAN to Payroll"); **Access scramble is NOT
  implemented.** Decrypt File must not be offered until the protecting scramble has been discovered.
- **Current behavior (BUGS):** frontend gates Decrypt on *any located paydata*, not on a discovered
  scramble; backend matches scramble by `target_key == target_file` but the UI sends the bare file
  name while scrambles are keyed `files::file::<name>`, so it silently falls back to `scrambles[0]`
  (the wrong scramble). Scrambles are never "discovered" -- they're always in state.
- **Planned fix:** extend the **Analyze Subsystem** success handler (Files/Slave) to mark scramble
  IC on that subsystem **discovered** (same place it already reveals trap doors -- see #3); gate
  Decrypt File on a **discovered** scramble; fix target-key matching (bare name <->
  `files::file::<name>` / `slave::piece::<name>`).

## 18. Compress File (missing) -- Compressor halves download size within Rating x 100 Mp
- **Status:** `[x]` (backend already auto-compresses on Download; added UI surfacing)
- **RAW** (Compressor, L1512): "Reduces size of data being transferred by **50%**. Max file size is
  **Program Rating x 100 Mp**. Decks must have sufficient active memory to hold the **uncompressed**
  size of the file. Files must be **decompressed before** being able to read or use them." Compressor
  is a **passive** utility applied during transfer -- there is no standalone "Compress File" operation
  in RAW.
- **USER:** with Compressor-3, files up to **300 Mp** compress to **50%** on **download** (e.g.
  170 Mp -> **85 Mp** stored). "This can and should apply to downloading paydata."
- **Current behavior:** `_compressed_store_size` already halves the stored size on Download within
  the Rating x 100 cap, and sets `compressed=True` (must Decompress before use).
- **DECISION (user):** **auto-compress on Download only** (RAW: Compressor is a passive transfer
  modifier -- no standalone op) and **surface it in the UI** (show the compressed download size, the
  Rating x 100 Mp cap, and the compressed / needs-decompress state). **No separate Compress File
  action.**
- **Planned fix:** verify the Download path applies Compressor (Rating x 100 cap, 50% size) when the
  utility is active; make the size reduction + "compressed, decompress before use" state visible in
  the download/paydata UI. Uncompressed size must still fit active memory during transfer.

## 19. Combat Maneuvers (NEW) -- Evade Detection, Parry Attack, Position Attack
- **Status:** `[x]` (unblocks #5; enhances #6)
- **RAW** (L1982-2000): a maneuver is an **opposed test**. The **maneuvering** icon rolls an
  **Evasion Test** (IC uses Security Value dice) vs TN = the opposing icon's **Sensor Rating**
  (**Cloak** reduces TN); the **opposing** icon rolls a **Sensor Test** vs TN = the maneuvering
  icon's **Evasion Rating** (**Lock-On** reduces TN). More successes for the maneuvering icon =
  success; net successes = magnitude. Non-IC programs without Evasion/Sensor cannot maneuver. Each
  maneuver is a **Simple Action** (L1958).
  - **Evade Detection:** the maneuvering icon vanishes from the opposition's view; re-detected after
    Combat Turns = net successes (each security-tally increase shortens that by 1 turn). Re-detect an
    evaded IC via **Analyze Icon**; an evaded decker/frame via **Locate Decker**. Cannot evade
    reactive IC during its location cycle.
  - **Parry Attack:** on a win, +net successes to the TN of attacks against the maneuvering icon
    until the opposing icon's next attack; lost if either icon performs an evade-detection maneuver.
  - **Position Attack:** on a win, either -net successes TN to the maneuvering icon's next attack OR
    +net successes Power; if the **opposing** icon wins, **it** gets the bonus instead (risky).
- **DECISION (user):** add all three maneuvers, available to **IC, player deckers, and enemy
  deckers**, wired in per the rules -- "spawn agents to build those maneuvers." Then #5 and #6 gain
  real purpose.
- **DONE** -- combat maneuvers built for the PC, IC, and revealed enemy deckers (full NPC use, the
  user-confirmed scope):
  - Engine `app/services/matrix_engine.py`: added `maneuver_test(...)` -- the shared opposed
    Evasion-vs-Sensor test (maneuvering Evasion dice vs the opposing Sensor Rating; opposing Sensor
    dice vs the maneuvering Evasion Rating; strict win, net successes = magnitude; Cloak / Lock-On
    TN reductions default to 0 -- neither utility is modeled in this app).
  - Router `app/routers/matrix_runs.py`: `_apply_maneuver` (PC initiates), `_resolve_npc_maneuver`
    + `_npc_maybe_maneuver` (IC / enemy initiate -- deterministic heuristic: badly wounded -> Evade,
    moderately wounded -> Parry, healthy vs a hurt PC -> Position; gated by the new
    `npc_combat_maneuvers` state flag, on by default), `_maneuver_target_lookup`, the evade
    lifecycle (`_evade_active` / `_evade_turns_remaining` / `_clear_evade` / `_sweep_evade_expiry`),
    and the attack-mod consumers (`_consume_attack_mods_vs_pc` / `_consume_attack_mods_vs_target`).
    Wired into `perform_action` dispatch, the proactive/reactive IC loop (evade-skip + NPC maneuver
    + attack-mod consumption), the enemy-decker turn, the PC attack path, and the new-turn evade
    sweep. `_ACTION_COST` marks all three Simple; maneuver state is stripped in the serializer's
    IC / enemy redaction so nothing GM-only leaks.
  - Schema `app/schemas/matrix_run.py`: `ActionType` += `evade_detection` / `parry_attack` /
    `position_attack`; `RunActionInput` += `maneuver_target` and `position_choice` ("tn" | "power").
  - Frontend `matrix-run.html`: three Simple-Action picker entries (opposing-icon target selector
    over active IC + revealed enemy deckers; Position Attack adds a -TN / +Power choice), plus
    EVADE / PARRY / POSITION event badges and a re-detection notice.
  - Tests: `TestCombatManeuvers` (18 tests) in `test_vr2_matrix_scenarios.py` -- evade hide + timer
    + tally-shortening + auto re-detect, the IC-loop skip gate, the reactive-trace-locate guard,
    no-target rejection, Parry (both directions) + consumption, Position tn/power/backfire +
    consumption, the three NPC heuristics + the dormant-flag case, revealed-enemy-decker parity,
    and the engine strict-win / net-success math.
- **Evade/re-detect state (consumed by #5):** on the target/actor icon -- `evaded` (bool),
  `evade_dir` ("lost_pc" = the PC hid, the icon keeps its place but cannot act until it re-detects;
  "hid_from_pc" = the NPC hid and drops off the PC's sensors), `redetect_turn` (absolute Combat Turn
  of automatic re-detection), `redetect_tally_base` (tally when it evaded -- every later tally point
  shortens the hidden window by a turn).
- **Acceptance:** matches RAW L1982-2000; the maneuver mechanic + automatic re-detect timer are
  complete and green (522 tests). The **manual** re-detect via Analyze Icon (IC) / Locate Decker
  (enemy) is item #5, which consumes the evade state above.

---

## Resolved decisions (from Q&A)
- **#3 Analyze Subsystem:** dropdown = Access, Files, Slave; remove Control, Index. ("Host LTG
  status" = whether the host is reachable from the regular grid vs only via a direct line/trap door;
  revealed by Analyze Subsystem on Access -- Access's only payload since Access scramble isn't
  implemented.)
- **#5 Locate IC:** restore + gate on real IC evasion (see #19), not removed.
- **#9 Dump Log:** remove entirely.
- **#10 Null Operation:** Upload out of scope; Locate Paydata stays a repeatable manual op;
  auto-Null-Op only during a multi-turn Download.
- **#17 Decrypt File:** scramble discovered via Analyze Subsystem (Files/Slave only).
- **#18 Compress File:** auto-compress on Download only + surface in UI; no standalone op.
- **#19 Combat Maneuvers:** NEW -- build Evade Detection / Parry Attack / Position Attack for IC,
  players, and enemy deckers; unblocks #5 and #6.

## Suggested execution order
1. Independent bug/behavior fixes: **#4, #6, #11, #13, #14, #15, #16, #18**
2. Analyze/discovery cluster: **#1, #2, #3, #17** (share the Analyze Subsystem/Icon handlers)
3. House rule + UI: **#7, #8, #12**
4. Removal: **#9**
5. Big features last: **#19** (maneuvers) -> then **#5**, and the Locate Decker re-detect part of #6
6. Multi-turn Download + auto Null-Op: **#10**
