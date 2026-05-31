# Matrix 2.0 -- Interactive UI E2E Findings (Session 2)

Date: 2026-05-31. Playwright (real Chromium) drive-through of the **full user journey** on
an isolated server (`:8770`, throwaway DB), using a baseline decker **Nightlife**
(Body 3, Quickness 3, Int 5, Willpower 4, Computer 10, Software 11, Computer B/R 5, no
Matrix spec). Goal: validate the UI matches the API and that every workflow is reachable
from the UI. Non-destructive; the real instance on `:8000` was untouched.

## End-to-end result: the journey completes

Built a cyberdeck, programs, and a load-out for Nightlife; created an easy host
(Federal Records Host A, `Blue-4/8/10/9/9/8`) in the designer; and **ran Nightlife through
it** -- logon + multiple operations resolved with correct VR2 mechanics. The pipeline works.

## What works (validated in the browser)

- **Deck builder:** MPCP/BEMS caps enforced with a live red warning (`CONSTRAINT VIOLATION:
  BOD (9) > MPCP (6) // PERSONA TOTAL (27) > MPCP x3 CAP (18)`); deck save persists to
  localStorage AND backend (`deck-builder-state.stores`).
- **Programs:** 35 utilities (all run-engine programs present); **build** (compile -> source
  + dated compile job, with a GM `FINISH` shortcut) and **buy** (Import Purchased Program)
  both work; per-program **options** reveal correctly (Attack -> area/dinab/skulk +
  chaser/oneshot/optimization/penetration/squeeze/targeting/limit + damage level); option
  **permutations** produce distinct programs (`Attack-6`, `Attack-6 [Optimization]`,
  `Attack-6 [Penetration, Targeting]`).
- **Load-out:** load a saved deck -> add programs (Active/Storage) -> Save Load-out; persists.
- **Host designer:** 7-step wizard (Identity/Security/Subsystems/Files&IC/Access/Sheaf/Review),
  live Host Summary, ACIFS validation blocks advancing on bad input, sheaf auto-generate
  (intervals reflect the F4 fix), full `config_json` persists on completion. Created exactly
  `Blue-4`, ACIFS `[8,10,9,9,8]`.
- **Matrix run:** logon, opposed System Tests with visible dice + success/fail + tally accrual
  (0->1->3->4->6), correct Detection Factor (5 = ceil((Masking 4 + Sleaze 6)/2)), correct
  Hacking Pool (3 = (Int 5 + MPCP 6)/3), condition monitors, event log, Action+Subsystem
  selectors, Perform Action / New Turn / Graceful Logoff / Jack Out, Active IC panel.

## Findings to fix (prioritized)

### U1 [MED] Decker skill not pulled from the character -- Nightlife ran with Computer ~4
In the run, Nightlife (Computer **10**) rolled only **4 dice** per System Test
(e.g. `Decker: [4,5,3,1] -> 0 hits`), and every operation failed. The run's `cfg-computer`
did not populate from the active character/profile (Hacking Pool *did* use Int 5, so some
profile data flows through, but not Computer skill). The decker should derive Computer skill
(and attributes) from the selected character. (Ties to the earlier F1.7 "authoritative-to-
character" finding.) **Proposed:** auto-fill `cfg-computer`/attributes from the active
programmer profile when a deck/character is selected; ideally make the run authoritative to
the Character rather than free-form.

### U2 [MED] Saved decks/load-outs don't appear in a fresh session (cross-device gap)
On a brand-new browser session, activating Nightlife in the deck-builder leaves localStorage
empty and the matrix-run **SAVED DECK BUILD / SAVED PROGRAM LOAD-OUT** dropdowns empty, even
though the data is in the backend (`deck-builder-state`). They only appear after a re-save/
reconcile in the deck-builder (which rehydrates localStorage). Saves sync *to* backend but a
new device/session does not hydrate *from* it on a plain activate+navigate. **Proposed:** on
profile activate (and on matrix-run load), hydrate decks/load-outs from
`/characters/{id}/deck-builder-state` into the in-memory stores.

### U3 [MED] Run requires a saved load-out, but offers manual inputs that can't start a run
The run will not start without a selected saved load-out ("Select a valid deck load-out
before starting a run"). Yet "Adjust Before Run" exposes a full manual deck-stat + utility
grid, implying you can configure and run ad hoc -- you cannot. Combined with U2, a fresh
session **cannot start any run**. **Proposed:** either allow starting from the manual config
(treat the Adjust grid as a valid ad-hoc load-out), or hide/disable it and clearly state a
saved load-out is required.

### U4 [MED] Start blocker detail is easy to miss
When a load-out exceeds the deck's memory, JACK IN silently no-ops; the specific reason
(`Invalid load-out for selected deck: Active 468/100 Mp, Storage 468/200 Mp`) is shown only
in a small `#runLoadoutStatus` line, while the click itself surfaces a generic message via
the page alert. **Proposed:** on JACK IN, show the specific eligibility reason in the page
alert; visibly disable the JACK IN button (greyed) with the reason as a tooltip.

### U5 [LOW] Run decker name defaults to "Ghost" instead of the character
The live run's Decker Status shows "Ghost" rather than "Nightlife". **Proposed:** default
`cfg-name` to the active profile's character name.

### U6 [LOW] Deck-builder can save a load-out that overflows the deck's memory
The planner warns on overflow but still lets you Save Load-out (e.g. 5x rating-6 programs =
468 Mp vs a 100 Mp deck); the run then rejects it. **Proposed:** block saving (or require
confirmation) for a load-out that exceeds the bound deck's Active/Storage memory.

### U7 [LOW / verify] Program size formula
Program size is computed as **rating^2 x multiplier** (5x rating-6 programs = 468 Mp). Confirm
this matches the VR2 program-size rules (vs a linear rating x multiplier). If intended, fine;
flagging because it drives the memory-cap math that gates runs.

### U8 [LOW-UX] Load-out "Add to Load" requires a deck loaded first (gate not surfaced)
Adding programs to a load-out silently no-ops until a saved deck is loaded
(`ensureDeckSelectedForLoad`). **Proposed:** surface the prerequisite ("Load a deck first")
near the Add-to-Load control.

## Fixes applied (2026-05-31) -- pending re-run verification

All in `frontend/matrix-run.html` (JS syntax-checked, hygiene clean; not yet re-run E2E):
- **U1 FIXED** + **U5 FIXED**: added `applyActiveCharacterToConfig()` (called on boot) that
  fetches the active profile's character and populates `cfg-name` (decker name), `cfg-computer`
  (Computer skill), and `cfg-intelligence/quickness/willpower/body` from the PC. Deck stats
  still come from the deck; skill/attributes now come from the character (so Nightlife uses
  Computer 10, not the default 4, and the run shows "Nightlife" not "Ghost").
- **U4 FIXED**: `startRun()` now surfaces the specific eligibility reason
  (`#runLoadoutStatus`, e.g. the memory-overflow detail) in the page alert instead of the
  generic "select a valid deck load-out".

Re-run 2026-05-31: **U1 CONFIRMED** -- Nightlife now rolls 10 dice (Computer 10), was 4.
U5 rides the same code path (name set with skill); confirm "Nightlife" in Decker Status.
U4 not yet exercised (needs an over-memory load-out to trigger).

Still open: **U2** (cross-session hydration), **U3** (manual config can't start a run / load-out
mandatory), **U6** (saving an over-memory load-out), **U7** (verify rating^2 size formula),
**U8** (Add-to-Load prerequisite hint).

### U9 [MED] FIXED 2026-05-31 (pending re-run) -- "Log On To Host" action does not apply the Deception utility
> Fix: both logon calls in matrix-run.html now pass `decker_json.utilities.deception` as
> `utility_rating` (was hardcoded 0). JS syntax-checked. Re-run run.spec.js -> logon should
> now succeed far more often. **U8 downgraded:** not a real bug -- `ensureDeckSelectedForLoad`
> opens a deck-selection modal; my automation bypassed it by calling addToLoadPlanner directly.

### U10 [MED] -- Operations (PERFORM ACTION) do not auto-apply the decker's utility
Re-run 2026-06-01 confirmed **U1** (10 dice) and **U9** (logon now succeeds -- Deception
applied). But every *operation* used the raw subsystem rating as TN because **UTIL RATING
defaults to 0** and isn't auto-filled from the load-out:
- analyze_host: 10 dice -> 2 hits (TN ~10 = raw Control; Analyze-6 would make TN 4 -> ~9 hits)
- analyze_security: 0 hits; locate_paydata: 1 hit (TN 9 raw Index, Evaluate not applied);
  null_operation: 3 hits (TN 10 raw Control).
This is the general case of U9: utilities are core to decking, so without them the decker
faces full TNs and mostly fails. **Proposed:** add an operation->utility map (mirror the
existing `ACTION_SUBSYSTEM` map in matrix-run.html; source = vr2 System Operations Summary,
e.g. Analyze Host->Analyze, Locate Paydata->Evaluate, Download/Edit->Read/Write, Crash Host->
Crash, Validate Passcode->Validate, Decoy->Mirrors, Relocate->Relocate, Redirect->Camo). On
action-select, auto-fill the UTIL RATING from the active load-out's rating for that utility
(editable, so a player can override). Note: tie-goes-to-host is correctly implemented
("FAILED (2 vs 2)").
Observed in re-run: logon rolled 10 dice all <= 4 and scored 0 hits, i.e. TN was the raw
Access rating (8). With the loadout's Deception-6 applied, the Access TN should drop to 2
(~7 hits). The dedicated **Log On To Host** action sends `utility_rating = 0` instead of the
decker's Deception rating, so logon is far harder than VR2 intends (Logon to Host uses the
Deception utility -- vr2_rules System Operations). **Proposed:** the logon action should pass
the decker's Deception utility as the System Test utility (auto-map operation -> utility from
the load-out), same for other operations' default utilities.

## Harness / cleanup
Throwaway Playwright specs in `D:\Code Projects\_sr_e2e\` (deck/prog/kit/loadout/designer/run
.spec.js + screenshots) and `data/_e2e_sess2.db`; test server on `:8770`. All safe to delete.

## Fix status (this session) -- known backlog cleared, all committed to matrix2

- **U1/U4/U5/U9** done (run uses character skill/name; blocker surfaced; logon applies Deception).
- **U10 FIXED** -- operations auto-fill UTIL RATING from the load-out (operation->utility map). Pending re-run.
- **U6 FIXED** -- deck-builder blocks saving a load-out that exceeds the active deck's memory.
- **U2 FIXED** -- matrix-run hydrates decks/load-outs from backend deck-builder-state on load (fill-only).
- **U7 verified** (size = rating^2 x mult). **U8 closed** (deck-selection modal exists).
- **U3 DOWNGRADED (clarity, not a blocker)** -- `getEffectiveLoadout()` = `_runLoadoutDraft ||
  getSelectedLoadout()`; "Adjust Before Run" builds a draft that satisfies eligibility, so a *saved*
  load-out isn't strictly required. Only optional discoverability polish remains.

Next: re-run run.spec.js to confirm U10/U2/U1/U9, then the #1-#11 VR2 test matrix (building missing
features per decision: enemy decker injected into a run, key-data-wipe UI, etc.).

### Re-run VERIFIED 2026-05-31 (Playwright, isolated :8770, fresh DB)
- **U1 CONFIRMED** -- Nightlife rolls **10 dice** (`[4,5,6,1,4,3,4,6,2,6] -> 7 hits`), was 4.
- **U9 CONFIRMED** -- Log On To Host succeeds with Deception applied (tally +3, "Logged on successfully").
- **U10 CONFIRMED** -- operations auto-fill UTIL RATING from the load-out: Analyze Host 7 hits,
  Analyze Security 4 hits, Null Operation 5 hits -- all succeeding (previously all failed at raw TN).
- Eligibility line reads "Load-out valid: Active 468/500 Mp, Storage 468/600 Mp"; JACK IN enabled; run POST 201.
- Env note: background-Bash `python` is not on PATH (exit 127); the test server must be launched via the
  venv python (`.venv\Scripts\python.exe`) through PowerShell `Start-Process`. Setup scripts must send the
  created admin token on EVERY call (bootstrap key is disabled the moment the first admin token exists).
