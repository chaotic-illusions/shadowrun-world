# Refactor Notes

Living document of identified-but-deferred refactoring opportunities. Each item lists
the *why*, the *what*, and the *risks*, so a future agent can pick it up cold without
re-deriving the analysis.

When an item is acted on, **delete it from this file** rather than marking it done --
git history preserves the record, and a long list of "done" items dilutes the live
backlog.

---

## R1 -- Split `perform_action` in `app/routers/matrix_runs.py`

**Status:** deferred. Discussed in code review 2026-05-18; postponed to pre-release
cleanup so the function isn't churned while gameplay rules are still being tuned.

### Where
[`app/routers/matrix_runs.py`](../app/routers/matrix_runs.py) -- the `perform_action`
endpoint (currently ~600 LOC, starting around line 480). It is the central handler for
every decker system operation: logon, analyze, locate, control-slave, validate
passcode, decoy, relocate, redirect-datatrail, graceful-logoff path, etc., **plus**
the entire host-side IC response phase (probe rolls, trace hunt/locate cycles,
crippler/ripper handling, Black IC dual-resist, simsense overload, dump shock, Sparky
discharge).

### Why split
- Reading a single action's behavior requires scrolling past every other action's
  branch and the entire IC loop.
- The IC turn loop has 6+ nested cases (trace/crippler/Black/standard) and each case
  itself has post-resolution side-effects (persona crash -> Blaster/Sparky MPCP test
  -> dump shock -> run end). Hard to reason about; harder to add a new IC type to
  without disturbing the others.
- New action types ("crash host", "analyze IC", "edit file") will keep landing
  inside the same function unless there's a structural place to put them.

### Proposed shape
Keep `perform_action` as the orchestrator; extract three private helpers, each
operating on the same `state` dict in place (no new abstractions, no IC
class hierarchy -- just relocated code blocks):

1. **`_apply_action_specific_effects(state, body, test) -> None`**
   - Covers the `validate_passcode`, `decoy`, `relocate`, `redirect_datatrail`,
     `logon_to_host` blocks currently inline after the System Test resolves.
   - Pure side effects on `state` + `_append_event` calls.
   - ~80 LOC.

2. **`_run_probe_phase(state, det_factor, sec_code) -> None`**
   - The Probe IC loop (today around lines 600-622 of matrix_runs.py).
   - Calls `_check_sheaf_triggers` and `_activate_sheaf_step` reactively after
     probe-driven tally bumps.
   - ~30 LOC.

3. **`_run_proactive_ic_phase(state, decker, eff, sec_code, sec_value, hardening) -> None`**
   - The big one: the proactive IC initiative loop, including:
     - Trace hunt/locate/triggered cascade (report / dump / burn variants)
     - Crippler / Ripper attack and chip damage
     - Black IC dual-resist (Body + Bod), non-lethal Willpower path, persona/physical
       threshold checks, MPCP secondary attacks
     - Standard cybercombat (Killer/Blaster/Sparky/Construct)
     - Simsense overload check
     - Post-crash MPCP for Blaster/Sparky
     - Dump shock
   - Must respect the early-return / `break` semantics that today end the run when
     a threshold is crossed. The helper will need to return a bool ("run ended")
     so the orchestrator can stop the loop.
   - ~400 LOC.

### Risks / cautions
- **Don't change behavior.** This is pure relocation; every test outcome should be
  byte-identical. Diff the response JSON before/after on the same RNG seed if any
  test fixtures exist.
- **`break` becomes `return True`.** Several `break` statements end the IC loop
  early when persona/physical hits 10 boxes. After extraction these become
  `return True` from the IC phase helper, and the orchestrator must respect it.
- **Mutable state aliasing.** Today everything writes through the same `state` dict
  reference. Keep that -- passing `state` by reference (the only practical option in
  Python anyway) preserves it. Don't be tempted to introduce a wrapper class.
- **Event order matters.** Players read the event log top-to-bottom; relocation must
  preserve the exact `_append_event` sequence within and between phases.
- **The `_CRIPPLER_TARGET` map is currently defined inside `perform_action`** (line
  ~625). Hoist it to module scope when extracting the IC phase.

### When to act
After the gameplay rules stabilize (post-playtest), and ideally bundled with a
recorded-RNG regression test so the diff is verifiable. Not worth doing in isolation
just for line counts.

### Pointer in code
[`app/routers/matrix_runs.py:470`](../app/routers/matrix_runs.py#L470) carries a
comment referencing this note so future readers / agents picking up the file are
aware.
