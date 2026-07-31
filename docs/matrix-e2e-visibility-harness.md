# Matrix Run -- End-to-End Visibility & Invariant Harness

> Status: **Phase 1 + Phase 2 foundation shipped.** Three files:
> `tests/matrix_visibility_invariants.py` (the shared canonical invariant battery),
> `tests/test_matrix_visibility_e2e.py` (targeted regressions for the known bugs), and
> `tests/test_matrix_visibility_fuzz.py` (the generative bug-discovery fuzzer).
> This document is the architecture and the roadmap. The code is the executable contract.

## 1. Why this exists (the gap)

We already have a **strong static** proof harness:

| Layer | File | Proves |
|-------|------|--------|
| Scope ledger | `tests/matrix_scope_ledger.py` | The enumerated set of buildable programs / options / IC / host mechanics (+ exclusions + pinned divergences). |
| Reconciliation | `tests/test_matrix_reconciliation.py` | Each mechanic is **present**, **reachable** (config field + invoke control, literal-token search of `matrix-run.html`), routed through **one seam**, and **guarded**. |
| Numeric oracle | `tests/test_matrix_numeric_oracle.py` | Each resolver is numerically correct in success **and** failure vs a cited VR2 rule. |
| Blind driver | `tools/sim_static_run.py` | The real engine can be driven end-to-end off the **player-redacted** serialization. |

What none of these check is the thing every recent playtest bug actually was:
**runtime, sequence-dependent visibility.** i.e. *what is revealed to whom, WHEN, and which
actions/targets/buttons are valid in each state.* Concretely, the Federated Bank punch-list:

| Bug | What broke | Category |
|-----|-----------|----------|
| B | Located files missing from the **admin** serialization -> admin Analyze Icon had no targets | admin/player parity |
| C | File **size + ENCRYPTED** leaked in the player view *before* Analyze Icon | progressive disclosure |
| D | **Invalidate Passcode (entire system)** not offered unless a Legitimate IC was visible | action availability |
| E | Discovered **Scramble** not shown until an unrelated Trace crashed | reveal timing |
| F | **Analyzed** files not removed from the Analyze Icon target list | target-list correctness |

Every one is a *stateful redaction / gating* fault. The static harness cannot see them because it
never drives a run and never diffs the **admin vs player** views of the same live state.

## 2. Core idea

Drive a **real run through the real endpoints**, deterministically, and after **every step**
capture **both** serializations of the identical state:

```
admin_state  = mr._serialize_run(RUN, AUTH_ADMIN )["state_json"]
player_state = mr._serialize_run(RUN, AUTH_PLAYER)["state_json"]
```

Then assert a **library of invariants** over `(admin_state, player_state, event_log, ctx)`. The
frontend renders deterministically from `player_state`, so asserting on the serialized player state
*is* asserting on "what the UI can possibly reveal" -- without a browser. (An optional Playwright
layer, Phase 3, closes the last gap for literal button/icon DOM presence.)

Determinism comes from seeding the three RNG surfaces the engine uses (same trick as
`sim_static_run.py`):

```python
random.seed(SEED); eng.random.seed(SEED); mr.random.seed(SEED)
```

## 3. Invariant categories

Each is a pure function; a scenario runs the whole battery after each step. `A` = admin view,
`P` = player view.

1. **Secrecy / redaction** -- no GM-only key ever reaches `P`.
   - `for k in mr._GM_ONLY_STATE_KEYS: assert k not in P`
   - `security_tally` / `host_security_code` / `host_security_value` absent from `P` until an
     Analyze Security / Analyze Host reveal flag is set.
   - `active_ic[].trap_hidden` in `P` is a bare `True` marker, never the concealed type/rating.

2. **Progressive disclosure** -- secrets appear only after the action that earns them. (Bug C)
   - Located file in `P`: `size_mp is None` and no ENCRYPTED reveal **until** `analyzed`.
   - After Analyze Icon on that file: `size_mp` is the real Mp and `encrypted` is truthful.
   - Host ACIFS ratings appear in `P.host_ratings_revealed` one-per-successful-Analyze-Host.

3. **Admin/player parity** -- `A` is a superset of what `P` may know. (Bug B)
   - `located_paydata` present for `A` whenever it is present for `P` (admin never has *fewer*
     targets than the player).
   - Every file id in `P.located_paydata` exists in `A.located_paydata` with a real `size_mp`.

4. **Action availability & target lists** -- the action a rule permits is offerable; the ones it
   forbids are not; target dropdowns are correct. (Bugs D, F)
   - Invalidate Passcode (entire system) is always in the target set once logged on.
   - A file that is `analyzed` is absent from the Analyze Icon target set (server truth mirrors the
     `_analyzeIconTargets` filter).
   - A file that is `encrypted` is absent from the Download target set; a `downloaded` file too.

5. **Reveal timing** -- a disclosure is visible the instant its flag flips, not a step later.
   (Bug E)
   - The moment a scramble's `discovered` flag is set, it appears in `P.discovered_scrambles`
     (independent of any IC being active/crashed).

6. **UI-control presence (state-implied)** -- cross-check `player_state` against the scope-ledger
   `invoke` tokens: if the rule says an action is available in this state, the state must carry the
   fields the control's `valid`/`target` predicate reads. Phase 3 upgrades this to real DOM checks.

## 4. Architecture

```
tests/matrix_visibility_invariants.py    the SHARED canonical battery (no test_ fns)
  |   check_no_gm_key_leak / check_security_hidden / check_trap_ic_redaction /
  |   check_progressive_disclosure / check_admin_parity / check_state_well_formed
  |   check_all(run, ctx) -- serialize BOTH views once, run the whole battery
  |
  +--> tests/test_matrix_visibility_e2e.py     (Phase 1: targeted regressions)
  |      synthetic reveal-bearing host + capable decker + seeded run setup
  |      - DIRECT-STATE tests: hand-built state -> real _serialize_run (B/C/E/F)
  |      - DRIVEN test: real perform_action(logon->locate->analyze), battery each step
  |      - STATIC contract: literal-token pins of the C/D/F/A run-UI fixes
  |
  +--> tests/test_matrix_visibility_fuzz.py    (Phase 2: generative discovery)
         per seed: RANDOM host (code/ACIFS/paydata/scramble variants/bombs/slaves/IC)
         + real logon + long RANDOM action script; check_all after EVERY step
```

Both harnesses import the **same** `check_all`, so a new invariant added to the shared module is
instantly enforced by every targeted regression **and** every fuzz seed. Determinism: the engine
draws from the global `random` stream (seeded, module intact so production `random.Random(local)`
still works); the fuzzer's own choices use a separate `random.Random` and it save/restores the
global state so it never perturbs neighbouring tests.

Two complementary styles, on purpose:

- **Direct-state** tests hand-build a state and call the **real** `_serialize_run`. Deterministic,
  fast, zero dice. They pin the exact redaction logic where B/C/E/F lived.
- **Driven / fuzzed** tests call the **real** `perform_action` / attack / new-turn endpoints under a
  fixed seed. They prove the whole stack wires together and that invariants hold on
  *engine-produced* states across a huge randomized space -- the discovery engine.

## 5. Roadmap

- **Phase 1 (shipped).** Shared invariant battery + dual-view capture; direct-state regressions for
  B/C/D/E/F; one driven logon->locate->analyze scenario; a static run-UI contract. Runs in the
  normal `pytest` suite, so CI catches any regression automatically.
- **Phase 2 foundation (shipped).** The generative fuzzer: a random host + a long random script per
  seed, replaying the full battery after every step (`tests/test_matrix_visibility_fuzz.py`,
  `FUZZ_SEEDS`). This is the "find the bugs I have not hit yet" engine. **To hunt deeper, widen
  `FUZZ_SEEDS`** (it is fast -- 16 seeds in ~2s) or raise the per-run step count; every added seed
  is a distinct host + script. A red run prints `seed=.. step=..` and reproduces exactly.
- **Phase 2 next.** Grow the battery (each new invariant instantly applies to every fuzz seed):
  action-availability (a rejected action was never offerable; Invalidate-all always offerable once
  logged on; encrypted/downloaded files excluded from the Download target set), reveal-timing
  (`discovered_scrambles` the instant the flag flips), and monotonic disclosure (a reveal never
  un-reveals). Fold `tools/matrix_outcome_probe.py` in as a distribution check.
- **Phase 3 (optional).** A thin **Playwright** layer: boot the app, log in as player and as admin,
  load `matrix-run.html` against a snapshotted run (`tools/snapshot_run.py`), and assert literal
  **button/card/badge** presence -- the only thing a headless state check cannot see (CSS/DOM).

## 6. How this "knocks out bugs and ships"

Every fixed bug becomes a **permanent invariant**, not a manual re-test. A new host, IC, program,
or redaction change must pass the entire battery in every captured state of every scenario. The
day-to-day loop becomes: reproduce a playtest report as a one-line scenario step + expected
disclosure, watch it fail, fix, watch it stay fixed forever.
