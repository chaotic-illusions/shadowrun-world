# Matrix 2.0 -- VR2 Rules Validation Report

Date: 2026-05-30. Validates that the Matrix 2.0 feature (host designer, deck/program
builder, matrix run engine) accurately represents `vr2_rules.md`. **Validation only --
no production code was changed** (one temporary `deepcopy` test-fix was applied to
confirm finding F1, then reverted). Revert point: commit `c5cbf25`.

> **Resolution (2026-05-30):** F1, F2, F3, F4, F6 are **fixed and validated** (F1 & F3
> re-confirmed live against the patched server; F4 via the engine suite; F2 by construction;
> F6 via schema + compile). F5 and F7 are documented/deferred (each needs a data-model or
> feature decision -- see notes). Details retained below for the record.

## How this was validated

1. **Engine unit suite** -- `tests/test_matrix_engine.py` (committed, `598a43b`): 44 cases
   cross-referencing `vr2_rules.md` tables/formulas against `matrix_engine.py` +
   `matrix_rules.py`. 43 pass, 1 `xfail` (F4 below).
2. **API integration validation** -- drove the live run engine on an isolated, fresh-DB
   server (`:8765`, throwaway `data/_e2e_*.db`) through full run scenarios: host+sheaf
   creation, run start, logon, operations, sheaf/alert/shutdown cascade, IC activation,
   cybercombat, graceful logoff, jack-out, and the GM-redaction/access-control paths.
3. Playwright (Node) harness installed under `D:\Code Projects\_sr_e2e\` (throwaway).

## Validated CORRECT (matches VR2)

- **Core math** (engine suite): Rule-of-Six dice, Detection Factor (`ceil((Masking+Sleaze)/2)`,
  example 6&8->7), Hacking Pool `(Int+MPCP)//3`, System Test (opposed, tie=fail, tally=host
  successes), damage staging (+1/2 successes) + Bod resistance (Armor reduces Power),
  Condition Monitor boxes (L1/M2/S3/D6), cybercombat TNs by status/code, IC damage levels,
  dump shock damage levels + cool/ICCM/tortoise modifiers, simsense TN table, IC initiative
  dice by code, crippler reduction (net/2), ripper chip (1/success), tar baby/tar pit,
  probe tally, trace hunt cycle, IC Ratings Table, and all sheaf allocation tables
  (alert/white/gray/black/trap/crippler-target).
- **Run loop** (API): logon sets `logon_complete`; security tally accrues host successes;
  sheaf triggers activate the correct IC at thresholds; multiple triggers crossed at once
  all fire; passive->active alert escalation; host shutdown at the shutdown step; crashing
  IC adds its rating to the tally; graceful logoff ends the run "escaped"; jack-out always
  applies dump shock.
- **Security (review fixes, re-validated live):** GM-only state is redacted server-side for
  non-admins (`trap_hidden` -> bare `True`; `lurking_ic`/`sheaf`/`host_acifs` stripped);
  non-owner users get 404 on someone else's run (existence not leaked).

## Findings

| # | Sev | Area | One-line |
|---|-----|------|----------|
| F1 | **HIGH** | run/cybercombat | Decker attacks that don't one-shot-crash the IC are silently discarded (not persisted). |
| F2 | **MED** | run/Sparky | Sparky physical damage is applied without the decker's Body resistance test. |
| F3 | **MED** | run/Black IC | Icon (persona) death is treated as decker death -- triggers the kill-the-decker consequences early. |
| F4 | LOW | sheaf gen | `SHEAF_INTERVALS` subsequent-step intervals are smaller than VR2 specifies. |
| F5 | LOW | run/simsense | The "+2 TN, hot deck DNI-only" simsense modifier is never applied. |
| F6 | LOW | host API | `MatrixHostCreate` can't set `is_visible_to_players`; a created host is always hidden until PATCHed. |
| F7 | INFO | engine | `decker_initiative_roll` lacks cool/tortoise modifiers and appears unused by the run loop. |

---

### F1 [HIGH] -- Decker cyber-attacks are not persisted unless they crash the IC

**VR2:** "Resolving Attacks" / "Icon Damage" / "Condition Monitors" -- a decker attacks an
IC, deals staged damage, fills the IC's 10-box Condition Monitor across multiple attacks
until it crashes.

**Observed (live, confirmed):** `POST /matrix-runs2/{id}/attack` returns 200 but, when the
hit does NOT immediately crash the IC, **no `decker_attack` event is logged and the IC's
box count does not change** -- confirmed by a fresh `GET` after the attack (boxes stayed 0).
The decker can never accumulate damage on an IC; only a single attack large enough to crash
it in one blow (>=10 boxes) takes effect.

**Root cause:** `attack_ic` (and the other run endpoints) do `state = dict(run.state_json)`
-- a **shallow** copy. The non-crash path mutates only *nested* objects (`target_ic["boxes"]`,
the `event_log` list), which are aliased to the loaded (committed) JSON. Because no top-level
scalar changes, SQLAlchemy's dict-equality comparison on the `JSON` column sees "no change"
and skips the UPDATE. `perform_action` is masked from this because it always bumps the
top-level `security_tally`; `attack_ic`'s crash path is masked because it bumps the tally
too -- but the non-crash path changes nothing top-level. This is the exact pitfall recorded
in the architecture memory ("don't mutate JSON nested-in-place; rebuild the object").

**Proposed solution (validated):** read run state with `copy.deepcopy(run.state_json)`
instead of `dict(...)` in the six run endpoints, so nested mutations are no longer aliased
to the committed snapshot and the reassignment is detected. I applied this temporarily and
re-ran the attack: the `decker_attack` event was logged and the IC went to 3 boxes. (Then
reverted.) Alternative: explicit `sqlalchemy.update(MatrixRun).values(state_json=state)`,
or wrap the column with `MutableDict`. Deepcopy is the smallest correct change and fixes all
run endpoints uniformly.

---

### F2 [MED] -- Sparky physical damage is not resisted

**VR2 "Sparky":** on persona crash, Sparky deals `(IC Rating)M` physical damage; "The decker
resists this damage normally (using physical Body attribute). Hardening reduces the Power."

**Observed (code review, `perform_action` Sparky branch):** the engine stages "Moderate" up
by the Sparky-test successes and adds the resulting boxes to the physical Condition Monitor
**directly, with no Body resistance roll** and no Hardening-reduced Power. The decker takes
the full staged-up damage unmitigated -- harsher than the rules.

**Proposed solution:** resolve the Sparky physical damage through
`eng.damage_resistance(bod=decker.body, power=ic_rating, armor_rating=hardening,
base_damage_level="Moderate", attacker_successes=sparky_test_successes)` and apply
`resistance["boxes"]`, mirroring how lethal Black IC's Body test is already handled.

---

### F3 [MED] -- Black IC: icon death handled as decker death

**VR2 "Lethal Black IC":** two distinct outcomes -- (a) "If the icon is killed before the
decker dies: the Matrix connection **remains intact**, the IC's effective rating increases
by 2, and the decker cannot fight back -- only attempt to jack out." (b) "If black IC kills
the decker [physical CM full]: connection drops; the IC attacks the MPCP as blaster at
double rating."

**Observed (code review, `perform_action` Black IC branch):** when the *persona* CM fills
(`persona_boxes >= 10`), the engine immediately ends the run, fires the double-rating MPCP
attack, and applies dump shock -- i.e. it applies the **kill-the-decker** consequences to an
**icon death**. Per VR2, icon death (with the decker's physical CM not yet full) should keep
the connection up, bump the IC +2, and restrict the decker to jack-out; the MPCP/dump
consequences belong only to the physical-CM-full case (which the engine does handle
separately).

**Proposed solution:** on `persona_boxes >= 10` with `physical_boxes < 10`, set an
"icon_crashed" state (IC effective rating +2, decker may only jack out) instead of ending the
run; reserve the MPCP-double-attack + dump-shock for the physical-CM-full branch.

---

### F4 [LOW] -- Sheaf trigger intervals shrink faster than VR2

**VR2 "Generating Trigger Steps":** every interval between trigger steps is `1D3 + modifier`
for the security code (Blue 5-7, Green 4-6, Orange 3-5, Red/Black 2-4) -- the same
distribution for all steps.

**Observed (engine suite, `xfail`):** `matrix_rules.SHEAF_INTERVALS` uses `first_range`
matching VR2 but an `interval_range` one lower at each bound (e.g. Blue first 5-7 but
interval 4-6). Subsequent triggers therefore cluster closer than the rules allow, making
sheaves escalate slightly too fast.

**Proposed solution:** set `interval_range == first_range` for each code (both = the VR2
"Trigger Step Range"). Removing the `xfail` in `tests/test_matrix_engine.py::
TestSheafGeneration::test_interval_range_matches_first_range` will then pass.

---

### F5 [LOW] -- Simsense "DNI-only +2 TN" never applied

**VR2 "Simsense Overload":** "Running hot with DNI-only interface: +2 to TN."

**Observed:** `eng.simsense_check` supports the `hot_dnil_only` parameter, but
`perform_action` never passes it, so the +2 is never applied. (The engine's ICCM `-2` and
the cool/tortoise immunity ARE applied.) Minor -- the data model has no "DNI-only" flag yet.

**Proposed solution:** add a decker "hot DNI-only" flag (deck/loadout) and pass it through,
or document that all hot decks are treated as having manual controls (no +2).

---

### F6 [LOW] -- Host can't be created visible to players in one step

**Observed:** `MatrixHostCreate` (schema) has no `is_visible_to_players` field, though
`MatrixHostUpdate` does. A host POSTed with that flag is created **hidden** (model default
False); a non-admin player then can't start a run on it (`start_run` -> 404) until an admin
PATCHes it visible. Surfaced immediately in E2E setup.

**Proposed solution:** if create-then-reveal is intended, this is fine (note it in the UI
flow). Otherwise add `is_visible_to_players` to `MatrixHostCreate` for parity with Update.

---

### F7 [INFO] -- `decker_initiative_roll` incomplete / unused

`eng.decker_initiative_roll` implements Response Increase / Reality Filter / hot-DNI dice but
omits the VR2 cool-deck `-1D6` and tortoise "only 1D6" modifiers, and the run loop does not
appear to call it (the run is turn-driven, not initiative-ordered for the decker). Either
wire it in with the missing modifiers or remove it as dead code.

---

## Not yet covered (checkpoint for continuation)

The run was exercised via the API (precise, fast). Still to validate, ideally via the
Playwright UI harness already installed:
- Per-IC-type **live** combat: cripplers/rippers (attribute reduction persists to logoff),
  tar baby/tar pit (utility crash + corruption), trace IC hunt->locate->trigger cascade,
  data bomb / scramble, constructs and party-IC clusters (penalty math).
- **Host designer** UI: ACIFS entry, quick-fill formulas, sheaf builder/preview, trap doors,
  org-security sync.
- **Deck/program builder** UI: MPCP/BEMS constraints (sum <= MPCP x 3, none > MPCP), program
  cost/build-time, loadout memory caps, persistence round-trip.
- Note: F1 means any prior manual cybercombat testing that "felt like the IC wouldn't die"
  was likely this bug -- worth re-testing after F1 is fixed.

## Harness / cleanup notes

- Throwaway: `D:\Code Projects\_sr_e2e\` (node_modules, Playwright, validation scripts) and
  `data/_e2e_test.db` / `data/_e2e_fix.db` (gitignored). Safe to delete.
- Throwaway uvicorn instances were started on `:8765`-`:8769` against throwaway DBs and then
  stopped; your real instance on `:8000` was never touched.

## Playwright UI smoke (2026-05-30)

Node `@playwright/test` + Chromium in `D:\Code Projects\_sr_e2e\` (config + `ui.spec.js` +
`token.txt` + `shot-*.png`). Loaded all four matrix pages authenticated (admin token injected
into localStorage):

| Page | Loads | Console errors | Controls | Notes |
|------|-------|----------------|----------|-------|
| matrix-designer | yes | 0 | 78 | renders |
| deck-builder | yes | 0 | 74 | has program + active/storage-memory + load controls |
| matrix-run | yes | 0 | 146 | host selector + deck/load-out dropdowns + deck-stat inputs render |
| manage-matrix (SR1) | yes | 0 | 23 | renders; delete control present |

So the pages load, wire up auth, and render without JS errors, and the deck-builder DOES
expose program active/storage-memory controls (one of the API-vs-UI concerns -- front-end
exists). matrix-run shows a real cross-page dependency: "No active programmer profile.
Activate one in Deck Builder first" -- a run needs a saved deck build from the Deck Builder.

## NEXT-SESSION CHECKPOINT (deep UI-vs-API E2E)

Done: fixes F1-F4,F6 committed (`8ba1126`); engine suite (`598a43b`); revert point
(`c5cbf25`); UI smoke (above). Remaining is the **interactive** UI-vs-API parity pass --
drive each workflow in the browser and assert the UI reflects/persists what the API does,
and that every API capability is reachable from the UI:

1. **Deck builder** (start here -- run depends on it): build a deck (assert MPCP/BEMS limits
   in the UI: sum BEMS <= MPCP x 3, no rating > MPCP), add/edit/delete programs, set/unset
   ratings, toggle programs active vs storage memory and verify the memory-cap math, save a
   deck build + program load-out, reload, confirm persistence (localStorage + backend
   `/characters/{id}/deck-builder-state`). Confirm there is a front-end for everything the
   deck/program API accepts.
2. **Host designer**: create a host (security code/value, ACIFS, quick-fill formulas), build
   + preview a sheaf, set trap doors, save; verify via API that config_json/sheaf/visibility
   persisted; check org-security sync.
3. **Matrix run** (now meaningful -- F1 fixed): select host + deck load-out, start, then
   exercise EACH System Operation (vr2 "System Operations Summary Table") and each IC type
   (cripplers/rippers/tar baby/tar pit/trace hunt->locate, construct, party IC, Black IC
   incl. the new icon-crash/jack-out path) -- confirm each is reachable from the UI and the
   rendered state matches the API state_json.

Harness run recipe: start a server on a spare port with a fresh DB + `BOOTSTRAP_ADMIN_KEY`,
create an admin token, write it to `_sr_e2e/token.txt`, set `baseURL` in
`playwright.config.js`, `cd _sr_e2e && npx playwright test`. Scratch dir + `data/_e2e_*.db`
are throwaway.
