# VR2 Matrix Reconciliation Report

**Scope:** every buildable program, program option, IC, and host mechanic in the SR2
Matrix subsystem, verified in the `matrix-run` runtime.
**Companion:** [matrix-reconciliation-ledger.md](matrix-reconciliation-ledger.md) (the
enumerated scope) and [tests/matrix_scope_ledger.py](../tests/matrix_scope_ledger.py) (the
machine-checked source of truth).

---

## 1. Executive summary

The Matrix subsystem was reconciled against `vr2_rules.md` for all five requirements:
present in schema/catalog, reachable via endpoint + UI control, numerically correct in
success and failure, resolved through one shared resolver per actor, and guarded against
future drift.

- **Scope:** 30 programs, 10 options, 19 IC, 12 host mechanics -- plus **11 explicit
  exclusions** so "no gaps" is provable against a defined boundary, not merely asserted.
- **Tests:** `816 passed` (full suite), including **28** numeric-oracle tests, **18**
  reconciliation-contract tests, and a **Bouncer behavioral proof** added this pass. App
  imports clean; text hygiene clean.
- **Auto-fixed (1):** the `purge_hog` run-UI reachability gap (pure wiring -- see 4).
- **Resolved this pass (4):** every divergence in section 3 was ruled on and **fixed** in
  code; their `DIVERGENCES` status is now `fixed` and each carries a `resolution` note.

**Status:** all divergences resolved -- no open rulings remain.

---

## 2. What was proven, and how

| Req | Claim | Mechanism | Test artifact |
|-----|-------|-----------|---------------|
| 1 | Every buildable item is in the schema/catalog | ledger sets compared to `DeckerUtilities` / `ProgramOptions` / `IC_CATALOG` **and** to the deck-workshop builder (bijection) | `test_req1_*` |
| 2 | Every item is reachable | each `cfg-u-*` field + invoke control located in `matrix-run.html`; every `ActionType` is console-reachable, dedicated-control-reachable, or a documented exception | `test_req2_*` |
| 3 | Every resolver is numerically correct in **success and failure** | 25 engine primitives executed in-process with a scripted d6 stream; exact result asserted vs the cited VR2 rule | `test_matrix_numeric_oracle.py` (28 tests) |
| 4 | Multi-actor mechanics use **one** resolver | shared-seam primitives asserted single symbols; every known exception is a pinned, non-drifting divergence | `test_req4_*` |
| 5 | Future additions cannot skip 1-4 | a new builder entry with no ledger row fails req 1; a resolver with no oracle row fails req 5; scope and exclusions must stay disjoint | `test_req5_*` |

The oracle uses a scripted-dice harness (`_ScriptedD6`) that drains an exact face list and
errors on under/over-run, so each proof pins a specific roll -> specific outcome, honoring
the **rule of 6** (a die of 6 re-rolls and adds while TN > 6). Both a passing and a failing
scenario are asserted for every primitive.

**Requirement 4 shared seam** (single engine symbols, proven callable):
`cybercombat_attack`, `black_attack`, `attribute_attack_core`, `damage_resistance`,
`shield_parry`, `medic_heal`, `restore_repair`, `maneuver_test`. Enemy deckers and IC
already route through these (verified: `/enemy-decker/attack` and IC turns call
`eng.cybercombat_attack`). The exceptions are the two bypasses in section 3.

---

## 3. Divergences -- all resolved (4)

Each was pinned by `test_req4_divergences_are_pinned_and_nondrifting`: while a divergence's
status was `open`, the test asserted the divergent code was still present at the cited
location, so it could not be silently "resolved" by deleting the evidence. All four have
now been ruled on and set to `status='fixed'` in `DIVERGENCES` (each with a `resolution`
note); the pin now skips them, and the fixes below are covered by the tests cited.

### 3.1 `dinab_attack_ic_bypass` -- DINAB Attack vs IC hand-rolls cybercombat
- **Where:** `app/routers/matrix_runs.py :: _dinab_attack_ic`
- **VR2:** cybercombat resolution, `vr2_rules.md` L2010
- **Current behavior:** when a DINAB ("Decker In A Box", an in-scope actor) runs the Attack
  program against an IC, the strike is hand-rolled via `eng.roll_dice` + `eng.stage_damage`
  with its own TN/resist math -- it does **not** call the shared `eng.cybercombat_attack`
  that PC->IC, IC->PC, and decker->PC attacks all use.
- **Why it matters:** requirement 4. The DINAB->IC path can drift from the canonical
  cybercombat resolver (e.g. if TN modifiers, shift/shield handling, or staging change in
  one place but not the other). Note the DINAB->*decker* strikes already route through the
  shared `_resolve_attribute_attack`; only DINAB Attack-vs-IC is bespoke.
- **Question:** Should DINAB Attack-vs-IC be routed through `eng.cybercombat_attack` like
  every other actor (recommended for consistency), or is the simplified hand-roll an
  intentional DINAB house rule?
- **Resolution (fixed):** `_dinab_attack_ic` now routes through `eng.cybercombat_attack`
  (`attacker_is_ic=False`), mapping the IC's defense/offense expert dice and armor into the
  resolver's `target_bod` / `armor_rating` / `ic_rating` and folding cluster + shield/shift
  TN into `tn_modifier`. The failure signal (`failed`, `all_ones`) that drives
  `_dinab_resolve_failure` (degrade / crash) is preserved. `status='fixed'`.

### 3.2 `area_attack_cybercombat_bypass` -- Area burst hand-rolls, skips enemy Shield
- **Where:** `app/routers/matrix_runs.py :: area_attack`
- **VR2:** cybercombat resolution, `vr2_rules.md` L2010
- **Current behavior:** the Area-option burst resolves multi-target damage with its own
  `eng.roll_dice` + `eng.damage_resistance` math instead of `eng.cybercombat_attack`, and
  it does **not** invoke `_enemy_shield_parry` for enemy-decker targets (single-target
  attacks do).
- **Why it matters:** requirement 4, two bypasses in one endpoint -- the burst can diverge
  from single-target cybercombat, and enemy Shield is silently ignored on area hits.
- **Question:** Should the Area burst resolve each target through `eng.cybercombat_attack`
  and honor `_enemy_shield_parry` for enemy targets (recommended), or is the area path's
  simplified resolution / no-parry an intentional balance choice?
- **Resolution (fixed):** the burst keeps its single shared Attack Test (vr2 L1663
  mandates **one** test applied to all targets, so per-target re-rolls via
  `cybercombat_attack` would violate the rule), but each target's damage now stages through
  `eng.damage_resistance` -- the exact resistance seam `cybercombat_attack` uses -- so IC
  and enemy targets resolve on the same math as single-target cybercombat. Enemy-decker
  targets now call `_enemy_shield_parry(...)` and pass `shield_successes` into the resolver,
  closing the ignored-Shield gap. `status='fixed'`.

### 3.3 `bouncer_inert` -- host designer builds a Bouncer that the run engine ignores
- **Where:** `frontend/matrix-designer.html` (builds it) vs
  `app/routers/matrix_runs.py :: _activate_sheaf_step` (no handler)
- **VR2:** Bouncer / mid-run security upgrade, `vr2_rules.md` L300
- **Current behavior:** the designer can build a Bouncer sheaf event
  (`type='bouncer'`, `new_security_code`, `new_security_value`) -- a real VR2 rule that
  raises the host's security code/value mid-run. But `_activate_sheaf_step` handles only
  `ic` / `trap_ic` / `construct` / `party_ic`, and `SheafEvent` has no `new_security_*`
  fields, so a triggered Bouncer is **silently inert**: it is saved and can fire, but does
  nothing.
- **Why it matters:** a buildable, rules-real mechanic produces no runtime effect -- a
  "present but unreconciled" gap that a GM would reasonably expect to work.
- **Question:** Which resolution do you want?
  (a) **Implement** -- add `new_security_code` / `new_security_value` to `SheafEvent` and a
  `bouncer` branch in `_activate_sheaf_step` (+ startup guard if a stored column is needed),
  so a triggered Bouncer upgrades the live host security; or
  (b) **Remove** -- drop the Bouncer control from the designer so nothing unreconciled is
  buildable.
- **Resolution (fixed, option a):** `SheafEvent` gained `new_security_code` /
  `new_security_value` fields (so the payload survives the designer's `model_dump` save --
  the exact reason it was inert), and `_activate_sheaf_step` gained a `bouncer` branch that
  upgrades `state['host_security_code']` / `host_security_value` (falling back to current
  values on a malformed payload) and logs a `type='bouncer'` event. No migration is needed
  -- both are `state_json` keys, not DB columns. Bouncer is now a first-class row in
  `HOST_MECHANICS` and is covered by the `TestBouncer` behavioral proof (upgrade, malformed
  fallback, schema round-trip). `status='fixed'`.

### 3.4 `logon_to_ltg_unsurfaced` -- valid action with no run control
- **Where:** `app/schemas/matrix_run.py` `ActionType` has `logon_to_ltg`; no control exists
  in `frontend/matrix-run.html`
- **VR2:** LTG logon, `vr2_rules.md` L174
- **Current behavior:** `logon_to_ltg` is a valid `ActionType` with subsystem/utility map
  entries, but no run-UI control posts it (a run begins already on a host, so LTG-logon is
  not separately surfaced). It is reachable via the raw API but invisible in play.
- **Why it matters:** it is a vestigial action -- neither a used control nor a documented
  removal.
- **Question:** Surface a run control for `logon_to_ltg`, or retire the vestigial action
  from `ActionType`?
- **Resolution (fixed):** the vestigial `logon_to_ltg` was retired from the `ActionType`
  literal (a run always begins already on a host, so it was never surfaced). Its canonical
  `rules.SYSTEM_OPERATIONS` entry is retained as the VR2 reference, so the auto-generated
  `_ACTION_COST` key is now documented as intentionally-unsurfaced in
  `test_coverage_matrix.py` (`_NON_ACTION_COST_KEYS` + `handled_elsewhere`), alongside
  `attack_ic`. `status='fixed'`.

---

## 4. Auto-fixed this pass: `purge_hog` UI reachability gap

- **Nature:** pure wiring gap (fully-implemented backend, no run-UI control) -- the
  remediation policy authorizes fixing these without a ruling.
- **Backend (already present):** `perform_action` `purge_hog` branch calls
  `eng.hog_purge_test` (Complex action) to wipe a Hog virus infecting the PC's own deck.
- **Gap:** no run-UI control posted `action_type='purge_hog'`, so a player infected by an
  enemy Hog could not invoke the defensive purge.
- **Fix:** added a gated `ACTION_CATALOG` entry in `frontend/matrix-run.html`:
  - `_pcHogInfections(state)` helper (mirrors the backend filter: infections with
    `target_id == 'pc'`);
  - `{ v: 'purge_hog', l: 'Purge Hog (wipe virus)', cost: 'Complex', valid: ... }` enabled
    only when the PC's deck is infected, with a picker of infections;
  - the selected infection id is posted as `target_program`.
- **Ledger:** `UI_REACHABILITY_GAPS['purge_hog'].status` -> `fixed`; the reachability test
  now **requires** the control (no exception), so it cannot silently regress.

---

## 5. Minor findings (non-blocking)

1. **`ProgramOptions` docstring corrected (documentation only).** The class docstring
   (`app/schemas/matrix_run.py`) had stated that "Optimization / Squeeze / **Limit**" are
   "intentionally NOT carried," but `limit_target` **is** a carried run-time field (it
   restricts a utility to `ic`/`decker`); only Optimization and Squeeze are build-time-only.
   The docstring was corrected to list just Optimization and Squeeze. No behavior change.
2. **Worm sub-variants are flavor-only (documented exclusion).** `IC_CATALOG['Worm']` names
   the three book variants (Dataworm / Deathworm / Tapeworm), but no code branches on them;
   `worm_attack` resolves all worms identically. Excluded as narrative-only. If you want
   distinct per-variant mechanics, that is a new feature, not a reconciliation gap.

---

## 6. How future gaps are prevented (requirement 5)

- **Bijection with the builder:** `test_req1_ledger_mirrors_the_workshop_builder` requires
  the deck-workshop program/option sets to equal the ledger. A new workshop entry with no
  ledger row (or `EXCLUSIONS` entry) fails immediately.
- **Numeric gate:** `test_req5_every_program_has_a_numeric_proof` /
  `_every_ic_has_a_numeric_proof` require every non-passive resolver to appear in the
  executed oracle. A new resolver cannot ship without a success+failure proof.
- **Reachability gate:** `test_req2_every_action_type_is_reachable_or_documented` requires
  each `ActionType` to be reachable or listed as a documented exception in the ledger.
- **Non-drift pins:** each divergence is pinned while `open` (its divergent code asserted
  still-present, so it cannot be silently dropped); flipping a pin requires the atomic
  status change + code change. All four are now `fixed`, so the pins skip -- and the
  Bouncer fix is additionally locked in by `HOST_MECHANICS['bouncer']` (req 1 symbol guard)
  and the `TestBouncer` behavioral proof, so it cannot regress to inert.
- **Boundary integrity:** `test_req5_scope_and_exclusions_are_disjoint` and
  `_excluded_items_are_truly_absent_from_the_builder` keep the in-scope/excluded partition
  honest.

---

## 7. Deliverables index

| Deliverable | File |
|-------------|------|
| Machine-checked scope + exclusions ledger | [tests/matrix_scope_ledger.py](../tests/matrix_scope_ledger.py) |
| Human-readable ledger mirror | [docs/matrix-reconciliation-ledger.md](matrix-reconciliation-ledger.md) |
| Numeric oracle (success + failure, VR2-cited) | [tests/test_matrix_numeric_oracle.py](../tests/test_matrix_numeric_oracle.py) |
| Reconciliation contract / guard tests (req 1,2,4,5) | [tests/test_matrix_reconciliation.py](../tests/test_matrix_reconciliation.py) |
| This report | docs/matrix-reconciliation-report.md |
