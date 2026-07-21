# Matrix-Run Action-Outcome Catalog

Complete cross-product of **every Matrix-run action x every target/enemy type x
{Success, Failure, Tie}**, showing what the **event log** and the **UI (DOM render)** would
show for each outcome. Built by static analysis of the actual code branches
(`app/routers/matrix_runs.py`, `app/services/matrix_engine.py`,
`app/services/matrix_rules.py`, `frontend/matrix-run.html`), with a live-execution
feasibility study and a working deterministic probe.

## Table of contents

- [How to reference an entry](#how-to-reference-an-entry)
- [ID ranges](#id-ranges)
- [Tie semantics (per engine)](#tie-semantics-per-engine)
- [Live-execution status](#live-execution-status)
- [Section A &mdash; PC Combat / Offensive Actions](#sec-a)
- [Section B &mdash; PC Utility / Hacking / System / Support](#sec-b)
- [Section C &mdash; Enemy / Opponent Actions vs the PC](#sec-c)
- [Section D &mdash; Live-Execution Feasibility](#sec-d)

---

## How to reference an entry

Every outcome row has a stable ID so you can call out a specific one to change:

- **A#** = PC combat / offensive actions (Section A)
- **B#** = PC utility / hacking / system / support actions (Section B)
- **C#** = enemy-vs-PC actions, grouped by opponent type (Section C)

Each numeric ID is one `(action x target/enemy-type)` pair and carries three outcome rows:
`.S` (Success), `.F` (Failure), `.T` (Tie). Example: **`A3.T`** = "attack vs Construct, tie";
**`C13.F`** = "enemy decker locate PC, failure". Pairs that cannot occur are written as a
single `N/A -- <reason>` line and consume no ID.

## ID ranges

| Section | Range | Contents |
|---|---|---|
| A -- PC combat | A1..A32 | attack_ic, area_attack, enemy-decker attack/black_hammer/killjoy/cripplers/hog, steamroller, slow, dinab combat, evade/parry/position maneuvers |
| B -- PC utility | B1..B34 | logon, analyze_*, locate_*, download/edit/decrypt/decompress, passcodes, decoy/redirect/relocate, memory ops, medic/restore/disinfect/purge, defuse, crash_host, scan, logoff, jack-out, new-turn, suppress, reveal-ratings, trap-door |
| C -- enemy vs PC | C1..C25 | enemy IC (probe/trace/cybercombat/black/crippler/ripper/tar/worm/data-bomb/scramble/maneuver), enemy decker (locate/escalate/attack/hog/cripplers/nerve/hide/medic/restore/maneuver), construct, party-IC |

## Tie semantics (per engine)

"Tie" = an opposed test whose **net successes == 0**. Each engine resolves that edge
differently, so every `.T` row states the exact rule:

- **`system_test`**: `success = decker_net >= 0 AND decker_succ > 0`. Equal successes (both > 0)
  **succeeds** (house rule: tie to decker); `0`-vs-`0` **fails**.
- **`cybercombat_attack` / `black_attack` / `damage_resistance`**: to-hit then defender staging
  -- **not** a win/lose opposed test, so `.T` = **N/A** for pure damage actions.
- **`attribute_attack_core`** (cripplers) / **`hog_attack`**: `net = max(0, atk - resist - shield)`;
  a tie yields `net 0` and **folds into Failure**.
- **`maneuver_test`**: `success = net > 0` strictly; a tie **fails** (except `position_attack`,
  which has a distinct three-way branch).
- **`tar_baby_test`**: a tie goes to the IC if the IC has >= 1 success, else mutual whiff.

## Live-execution status

The outcome-bearing core (every resolver that funnels through `matrix_engine.roll_dice`) was
**verified live and deterministically** via [tools/matrix_outcome_probe.py](../tools/matrix_outcome_probe.py)
(monkeypatch `roll_dice` to return scripted success counts). A representative sample
(`attack_ic`, `analyze_host` System Test incl. the tie->decker house rule, and an enemy
proactive Killer-IC attack) was captured with byte-for-byte real `event_log` dicts across
S/F/T. The remaining catalog entries are static-derived and keyed to the same shared
resolvers. See **Section D** for exactly what can and cannot be driven purely live (and why).

---

<a id="sec-a"></a>

## Section A &mdash; PC Combat / Offensive Actions

Static analysis of the SR2 Matrix run engine (`app/routers/matrix_runs.py` handlers +
`app/services/matrix_engine.py` primitives) and the render pipeline in
`frontend/matrix-run.html`. Every row was read off the actual branch, not inferred.

### Legend -- ID scheme

- IDs are `A<n>.<outcome>` where `<n>` is a sequential integer per **(action, target-type)**
  pair (starting at A1) and `<outcome>` is `S` (Success), `F` (Failure) or `T` (Tie).
- Each `A<n>` header names the action + target it covers. Pairs that cannot occur are written
  as a single `N/A -- <reason>` line with **no** ID consumed.
- Range used by this section: **A1..A32** (see the running index at the bottom).

### Legend -- Tie semantics (per engine)

The word "tie" means an opposed test whose **net successes == 0**. Each engine resolves that
edge differently, so the `.T` row states the exact rule that applies:

- **`system_test`** (`matrix_engine.py` ~L77): `success = decker_net >= 0 AND decker_succ > 0`.
  A decker-vs-host tie (equal successes, both > 0) **succeeds** (house rule: tie to the decker);
  a `0`-vs-`0` whiff **fails**. *(Not used by the pure-combat actions below except DINAB-operate,
  which is out of Section A scope.)*
- **`cybercombat_attack` / `damage_resistance` / `black_attack`** (to-hit then defender staging):
  **not an opposed win/lose test** -- the attacker rolls to-hit, the defender resists and stages
  the damage level. There is no equal-successes branch, so `.T` = **N/A** for every damage action
  (attack_ic, area_attack, enemy-decker plain attack / black_hammer / killjoy, steamroller). The
  meaningful split is Success = boxes inflicted (possibly a crash) vs Failure = fully staged down
  to no damage.
- **`attribute_attack_core`** (cripplers Poison/Restrict/Reveal; `matrix_engine.py` ~L817):
  `net = max(0, attack_succ - resist_succ - shield_succ)`, `reduction = net // 2`. A tie
  (attacker succ == resist+shield) yields `net 0 -> reduction 0`, which **folds into Failure**
  (no attribute loss). `.T` documents that fold.
- **`hog_attack`**: `net = max(0, attack_succ - resist_succ)`, infects only when
  `attack_succ > 0 AND reduction > 0`. A tie folds into Failure (no infection).
- **`slow_test`** (`matrix_engine.py` ~L994): after an unopposed to-hit, `net = decker_succ -
  ic_succ`; `net <= 0` (including a tie) = **resisted / Failure**.
- **`maneuver_test`** (`matrix_engine.py` ~L1414): `success = net > 0` (STRICTLY more). A tie
  (`man_succ == opp_succ`) **fails**. For `position_attack` the tie is a *distinct third branch*
  ("tied -- no advantage") separate from a backfire (`opp_succ > man_succ` -> the NPC seizes the
  positioning); for `evade_detection` / `parry_attack` a tie is just a plain failure.

Every SR2 roll uses `roll_dice` (rule-of-6: a die of 6 re-rolls and adds while TN > 6).

Shared UI note: every offensive endpoint ends with `commit -> _serialize_run -> return`; the
`submit*` handler in `matrix-run.html` then calls `renderRunState` (~L2999), which re-runs the
whole pipeline: `renderEventLog`/`renderEventEntry` (new entry prepended, reversed order),
`renderActiveIC` (~L3216, IC condition boxes via `renderConditionBoxesHTML(boxes,10,'ic')`),
`renderEnemyDeckers` (~L2521), `renderStage`/`renderConditionBoxes` (~L3818/L3029, PC persona/meat
monitors) and `renderAlertBadge` (~L3168, security-tally badge). `renderEventEntry` (~L3380) maps
`ev.type` to a CSS class + coloured badge; types with **no** `case` fall to the default
(`ev-neutral`, badge `#333`, text = `TYPE` upper-cased with spaces) -- this covers
`area_attack`, `maneuver`, `tar_steamrolled`, `ic_slowed`, `decker_hog`, `dinab_op`,
`dinab_attack`.

---

### A1 -- `attack_ic` vs enemy IC (`POST /{id}/attack`, handler ~L6388; UI `submitAttack` ~L4745)

Pool = `attack_pool + hacking_pool_dice`. To-hit TN = `COMBAT_TN[sec_code][target_status]`
(+ cluster + Shield/Shift + Parry + wound + Deathworm, -2 Targeting, floored 2). IC resists via
`cybercombat_attack` -> `damage_resistance`: `ic_resist_pool = sec_value + Expert(def) - Expert(off)`
dice vs Power (`attack_rating + cluster + position`), Armor reduces Power. Cumulative
`target_ic["boxes"] >= 10` => crash.

| ID | Action | Target type | Outcome | Roll / mechanic (pool vs TN, opposed rule, net/tie) | Event log entry (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|------------------------------------------------------|-------------------------------|-----------------|------------------------|
| A1.S | attack_ic | enemy IC | Success | To-hit succ > 0 and staged damage `boxes > 0`. Sub-case: cumulative `boxes >= 10` => crash. | Non-crash: `type:"decker_attack"`, "Attacked {type}-{rating}: N successes. Dealt {level} ({boxes} boxes). IC: b/10". Crash: `type:"ic_crashed"`, "{type}-{rating} CRASHED. Tally +{applied} -> {total}{skulk}" (Skulk masks tally). | `renderEventEntry`: decker_attack -> `ev-decker-atk`/ATTACK (blue); ic_crashed -> `ev-ic-crashed`/IC CRASH (green). `renderActiveIC` fills the IC's `renderConditionBoxesHTML`; on crash card greys (`status:"crashed"`) + attack button gone. `renderAlertBadge` bumps on crash. | Run active; icon not crashed; IC `status=="active"`; not an un-located trace; Attack not Limited to decker; One-Shot not spent. Simple action; spends HP + pass action. Crash spawns Trap hidden IC (`_spawn_trap_hidden`), sets `crash_pending`. |
| A1.F | attack_ic | enemy IC | Failure | To-hit rolled but defender staged the hit down to None: `boxes <= 0`. | `type:"decker_attack"`, "...: N successes. Fully resisted -- no damage. IC: b/10". | `ev-decker-atk`/ATTACK badge; IC condition boxes unchanged; no tally change; no crash. | Same preconditions; the pass action + HP are still spent even on a whiff. |
| A1.T | attack_ic | enemy IC | Tie | **N/A** -- unopposed to-hit + defender damage-staging (`cybercombat_attack`); no equal-successes branch exists. | -- | -- | Treat "tie" as fully-resisted (A1.F). |

**`attack_ic` vs enemy decker:** N/A -- deckers are struck via `POST /enemy-decker/attack` (A8-A12); `attack_ic` only resolves `state["active_ic"]`.

### A2 -- `attack_ic` vs Construct (IC subtype)

Construct is an IC whose `type == "Construct"` (rendered as a `construct` card). It flows through
the **same** `attack_ic` handler and `cybercombat_attack` seam as any IC -- identical mechanics to
A1; only the render category differs.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A2.S | attack_ic | construct | Success | As A1.S (to-hit succ > 0, `boxes > 0`; `>=10` crash). Construct carries no special resist unless it has Armor/Expert. | As A1.S (`decker_attack` / `ic_crashed`), label "Construct-{rating}". | `renderActiveIC` marks `cardCat = 'construct'`; boxes fill; crash greys the construct card. | Construct must be `status=="active"`. |
| A2.F | attack_ic | construct | Failure | As A1.F (`boxes <= 0`). | `type:"decker_attack"`, "...Fully resisted -- no damage." | construct boxes unchanged. | -- |
| A2.T | attack_ic | construct | Tie | **N/A** -- same damage-staging rule as A1.T. | -- | -- | -- |

### A3 -- `attack_ic` vs Party IC (clustered IC)

Party IC = IC with a `cluster_id`. `_cluster_size` adds a to-hit **penalty** (`atk_cluster_penalty
= max(0, cluster - Area)`) AND is folded into resist Power (`attack_power = attack_rating + cluster
+ position`), preserving Party-IC hardness. Otherwise identical to A1.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A3.S | attack_ic | party IC | Success | To-hit TN raised by cluster size; Power raised by cluster. `boxes > 0`; `>=10` crash. | As A1.S. | `renderActiveIC` sets `cardCat='party'` and shows the cluster/penalty count; boxes fill; crash greys card. | Single-target attack against one member; cluster penalty applies unless an Area utility offsets it (see A6). |
| A3.F | attack_ic | party IC | Failure | Cluster penalty makes the whiff / full-resist (`boxes <= 0`) more likely. | `type:"decker_attack"`, "...Fully resisted -- no damage." | boxes unchanged. | -- |
| A3.T | attack_ic | party IC | Tie | **N/A** -- damage-staging, no tie branch. | -- | -- | -- |

---

### A4-A7 -- `area_attack` (`POST /{id}/area-attack`, handler ~L8261; UI `submitAreaStrike` ~L4856)

Requires the Attack utility's **Area** option (`opt_area >= 1`) and 1..Area targets mixing active
IC and revealed enemy deckers. ONE Attack Test is rolled at the highest per-target TN; each target
counts successes from the **same** dice vs its own TN. Burst (`n >= 2`): to-hit `+n_targets`, Area
**bypasses the Party-IC cluster penalty**, +2 effective Armor to any target with Armor. Single
target collapses to a plain attack. IC resist via `damage_resistance`; enemy deckers resist via
Bod + Shield parry + Armor (exactly like the PC). One aggregate `area_attack` event lists all
targets.

### A4 -- `area_attack` vs enemy IC

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A4.S | area_attack | enemy IC | Success | One shared to-hit; this IC's `succ = count(dice >= its TN)`; `damage_resistance` -> `boxes > 0`; `boxes >= 10` => `_apply_ic_crash`. | `type:"area_attack"`, "AREA STRIKE (N successes) hits K icons [+P to-hit]: {type}-{rating} {level} ({b}b; CRASHED?)...; C crashed." | Default badge `AREA ATTACK` (`ev-neutral`); `renderActiveIC` updates each listed IC's boxes; crashed IC greyed; `renderAlertBadge` bumps for each crash. | Attack utility has Area; IC in `target_ids`; not Limited to decker; burst adds +2 Armor if IC has Armor. |
| A4.F | area_attack | enemy IC | Failure | This IC's successes staged down to `boxes <= 0`. | Same aggregate event; this IC shows "{type} None (0b)". | IC boxes unchanged in card. | Other targets in the same burst may still succeed. |
| A4.T | area_attack | enemy IC | Tie | **N/A** -- damage-staging (no equal-successes branch). | -- | -- | -- |

### A5 -- `area_attack` vs Construct

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A5.S | area_attack | construct | Success | As A4.S (construct is an IC target in the burst). | `area_attack` aggregate, "Construct-{rating} {level} ({b}b...)". | construct card boxes updated; crash greys it. | Construct `status=="active"`. |
| A5.F | area_attack | construct | Failure | `boxes <= 0` for this construct. | aggregate shows None (0b). | boxes unchanged. | -- |
| A5.T | area_attack | construct | Tie | **N/A** -- damage-staging. | -- | -- | -- |

### A6 -- `area_attack` vs Party IC

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A6.S | area_attack | party IC | Success | On a real burst `cluster = 0` (Area bypasses the Party penalty) so to-hit is easier; `boxes > 0`; crash => `_apply_ic_crash`. | `area_attack` aggregate. | multiple party members' boxes update in one redraw; crashes greyed. | Burst engaging several clustered members is the intended use of Area. |
| A6.F | area_attack | party IC | Failure | This member's successes staged to `boxes <= 0`. | aggregate None (0b). | boxes unchanged. | -- |
| A6.T | area_attack | party IC | Tie | **N/A** -- damage-staging. | -- | -- | -- |

### A7 -- `area_attack` vs enemy decker

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A7.S | area_attack | enemy decker | Success | Shared to-hit; enemy `_enemy_shield_parry` cancels successes, Armor (+2 on burst) reduces Power, then `damage_resistance` on `bod`. `boxes > 0`; `persona_boxes >= 10` => `status="crashed"`. | `type:"area_attack"` aggregate, "{name} {level} ({b}b; CRASHED?)". | `renderEnemyDeckers` updates the enemy persona monitor; crashed enemy card greyed. | Enemy must be `active` AND `revealed`; not Limited to IC; Armor wear tracked gm-only. |
| A7.F | area_attack | enemy decker | Failure | Shield parry + resist stage to `boxes <= 0`. | aggregate None (0b). | enemy monitor unchanged. | -- |
| A7.T | area_attack | enemy decker | Tie | **N/A** -- damage-staging + Shield parry (successes-subtract), no opposed tie. | -- | -- | -- |

---

### A8-A12 -- `attack_enemy_decker` (`POST /{id}/enemy-decker/attack`, handler ~L7960; UI `strikeEnemyDecker` ~L2588)

`program` selects the sub-mode. All target a revealed, active enemy decker/frame ONLY. Pool =
`attack_pool + hacking_pool_dice`. Simple action; consumes One-Shot / DINAB lock; combat maneuvers
(`_consume_attack_mods_vs_target`) fold into TN/Power.

**All five sub-modes vs enemy IC / construct / party IC:** N/A -- these programs "target enemy DECKERS/frames only; they are never routed through IC" (handler docstring; IC damage goes through A1-A6).

### A8 -- enemy-decker attack, `program="attack"` (plain icon crash)

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A8.S | attack (enemy decker) | enemy decker | Success | `cybercombat_attack` (attacker_is_ic=False): to-hit vs `COMBAT_TN[sec][enemy status]`, enemy Shield parry subtracts successes, Armor reduces Power=`attack util + position`, Bod resist. `boxes > 0`; `persona_boxes >= 10` => crash + "dumped". | `type:"decker_attack"`, success True, "You strike {name} -- {level} ({b} boxes). Enemy persona b/10." (+ " ...icon CRASHED -- dumped from the host." on crash). | `decker_attack` -> `ev-decker-atk`/ATTACK (blue). `renderEnemyDeckers` updates enemy persona boxes; crash greys card. | Enemy `active` + `revealed`; icon not crashed; Attack not Limited to IC. |
| A8.F | attack (enemy decker) | enemy decker | Failure | Shield parry + Bod resist stage to `boxes <= 0`. | `type:"decker_attack"`, "...{None} (0 boxes). Enemy persona b/10." | enemy monitor unchanged. | Pass action + HP still spent. |
| A8.T | attack (enemy decker) | enemy decker | Tie | **N/A** -- damage-staging; Shield parry is successes-subtract, not an opposed net test. | -- | -- | -- |

### A9 -- enemy-decker cripplers, `program in {poison, restrict, reveal}`

Poison->Bod, Restrict->Evasion, Reveal->Masking. Routed through `_resolve_attribute_attack` ->
`crippler_attack` -> `attribute_attack_core`: `net = max(0, atk - resist - shield)`,
`reduction = net // 2`, applied floored so attribute stays >= 1; lasts until the enemy logs off.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A9.S | crippler (enemy decker) | enemy decker | Success | `reduction > 0`: attribute cut by `applied = min(reduction, rating-1)`. Reveal also recomputes the enemy DF. | `type:"decker_crippled"`, success True, "{PROG} -- you cripple {name}'s {Attr} by X (now V, until it logs off)." | `decker_crippled` -> `ev-action-ok` + program-name badge (green). `renderEnemyDeckers` shows reduced attribute; a lower Masking may light the enemy up. | Enemy revealed; enemy Shield adds to its resist side. |
| A9.F | crippler (enemy decker) | enemy decker | Failure | `reduction == 0` (attacker <= resist+shield). | `type:"decker_crippled"`, success False, "{PROG} -- {name} resists your crippler; {Attr} holds." | `decker_crippled` fail -> `ev-neutral` + program badge (amber). No attribute change. | -- |
| A9.T | crippler (enemy decker) | enemy decker | Tie | Opposed `attribute_attack_core`: tie = `attack_succ == resist_succ + shield_succ` => `net 0 -> reduction 0`. **Folds into Failure** (A9.F) -- identical event/badge. | Same as A9.F ("...{Attr} holds."). | Same as A9.F. | A true equal-successes tie is possible here but is mechanically indistinguishable from a loss. |

### A10 -- enemy-decker `program="hog"`

`_resolve_hog` -> `hog_attack`: to-hit, then `resist = MPCP vs (hog_rating - hardening)`,
`net = max(0, atk - resist)`, `reduction = net // 2`. Infects only when `attack_succ > 0 AND
reduction > 0`; seeds a persistent infection drained each Combat Turn (`_drain_all_hog_infections`).

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A10.S | hog (enemy decker) | enemy decker | Success | `infected == True`: seed infection, apply first drain of `reduction` to the enemy's highest running program. | `type:"decker_hog"`, success True, "HOG -- your virus takes hold on {name}: it will drain R off its highest running program each Combat Turn until it purges or crashes." | Default badge `DECKER HOG` (`ev-neutral`). Per-turn drains later log gm-only `enemy_decker`/hog lines. | Enemy revealed; the specific drained program is GM detail. |
| A10.F | hog (enemy decker) | enemy decker | Failure | `attack_succ == 0` OR `reduction == 0` -> `infected == False`. | `type:"decker_hog"`, success False, "HOG -- your virus fails to take hold on {name} this pass." | Default badge; no infection recorded. | -- |
| A10.T | hog (enemy decker) | enemy decker | Tie | `net = max(0, atk - resist)`; a tie (atk == resist) => `net 0 -> reduction 0` => not infected. **Folds into Failure** (A10.F). | Same as A10.F. | Same as A10.F. | -- |

### A11 -- enemy-decker `program="black_hammer"` (lethal Physical)

`black_attack` with `_LETHAL_BASE_LEVEL` (Serious), `meat_pool=None` (NPC flesh not simulated ->
icon-only). Rating capped at `ceil(Computer/2)`. On icon crash: dump enemy + MPCP burn (blaster at
DOUBLE rating via `_roll_enemy_mpcp_damage`).

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A11.S | black_hammer | enemy decker | Success | To-hit vs host combat TN; Shield parry subtracts; Bod resist (Armor+Hardening reduce Power). `boxes > 0`; `persona_boxes >= 10` => crash. | Hit: `type:"decker_lethal"`, outcome "hit", "BLACK HAMMER -- you drive lethal Physical biofeedback into {name}: icon {level} ({b} boxes). Enemy persona b/10." Crash: outcome "crash", "BLACK HAMMER CRASHES {name}'s icon -- ...dumped... fries its MPCP: -H permanent." | `decker_lethal`: hit -> `ev-decker-atk` (red) BLACK HAMMER; crash -> `ev-ic-crashed` (green) BLACK HAMMER. `renderEnemyDeckers` updates persona; crash greys card. | Enemy revealed; `program` only vs deckers. Rating clamp noted if `carried > cap`. |
| A11.F | black_hammer | enemy decker | Failure | `boxes <= 0` (parried / resisted); no crash. | `type:"decker_lethal"`, outcome "hit", success False (boxes 0). | enemy persona unchanged. | -- |
| A11.T | black_hammer | enemy decker | Tie | **N/A** -- `black_attack` is to-hit + defender staging (no opposed tie). | -- | -- | -- |

### A12 -- enemy-decker `program="killjoy"` (lethal Stun)

Identical resolver to A11 (`black_attack`, `_LETHAL_BASE_LEVEL`), damage kind = Stun; on crash same
dump + MPCP burn.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A12.S | killjoy | enemy decker | Success | As A11.S with Stun label. | `type:"decker_lethal"` outcome "hit"/"crash", "KILLJOY -- you drive lethal Stun biofeedback into {name}: ..." | `decker_lethal` badge `KILLJOY` (red hit / green crash). Enemy persona updated. | Enemy revealed; deckers only. |
| A12.F | killjoy | enemy decker | Failure | `boxes <= 0`. | `type:"decker_lethal"` hit, boxes 0. | enemy persona unchanged. | -- |
| A12.T | killjoy | enemy decker | Tie | **N/A** -- damage-staging, no opposed tie. | -- | -- | -- |

---

### A13 -- `steamroller` (anti-tar) (`POST /{id}/action` `action_type="steamroller"`; UI `steamrollTar` ~L4398)

`_apply_steamroller` -> `steamroller_attack`: a one-way Deadly hit (Power = effective Steamroller
rating) on a lurking Tar Baby / Tar Pit; **immune** to the tar's crash backlash (never runs
`tar_baby_test`). Crash (fills the tar's full 10-box monitor) removes the tar and adds its rating to tally
unless Skulk-masked or the tar is suppressed.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A13.S | steamroller | tar IC | Success | To-hit `steamroller_pool` vs `COMBAT_TN[sec][target status]` (-2 Targeting); Deadly damage stages boxes onto the full 10-box tar CM. Crash sub-case: `total_boxes >= 10` -> tar removed, tally `+max(0, rating - skulk)` (0 if suppressed). | Crash: `type:"tar_steamrolled"`, destroyed True, "Steamroller-R CRUSHES {type}-{rating} ({level}). Tally +A -> {total}{note}". Hit-not-crash: destroyed False, "...hits ... for {level} (b/10) -- it holds and stays lurking." | Default badge `TAR STEAMROLLED` (`ev-neutral`). Lurking tar is server-redacted, so the card list only changes when the tar is removed; `renderAlertBadge` bumps on a non-suppressed crash. | Complex action; Steamroller must be loaded (`rating > 0`, else 400, no action spent). Target must be Tar Baby/Tar Pit -- any other IC type -> 400. |
| A13.F | steamroller | tar IC | Failure | To-hit missed or Deadly staged down so `boxes <= 0` (badly under-rated Steamroller). | `type:"tar_steamrolled"`, destroyed False, "...it holds and stays lurking." (returns `failed=True` for DINAB degrade). | Default badge; no tally change. | -- |
| A13.T | steamroller | tar IC | Tie | **N/A** -- Steamroller is explicitly one-way (no opposed test); it never runs `tar_baby_test`. | -- | -- | -- |

**`steamroller` vs enemy IC (non-tar) / construct / party IC / enemy decker:** N/A -- "Steamroller is a tar-only weapon"; a non-tar target is rejected with HTTP 400.

---

### A14-A16 -- `slow` (proactive IC) (`POST /{id}/action` `action_type="slow"`; UI `slowIC` ~L4434)

`_apply_slow`: unopposed to-hit (`decker_pool` vs `COMBAT_TN[sec][target status]`, -2 Targeting);
on a hit an opposed `slow_test` (`net = decker_succ - ic_succ`, `actions_lost = max(0,net)//2`, at
least 1 on a win). Losing all `_ic_passes` HANGS the IC for the turn.

### A14 -- `slow` vs enemy IC (proactive)

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A14.S | slow | enemy IC (proactive) | Success | To-hit succ > 0 AND opposed `slow_test` net > 0. `lost = max(1, actions_lost)`; remaining <= 0 => HANG (`hung_turn`), else slowed. | `type:"ic_slowed"`, outcome "slowed" or "hung": "Slow-R hits {type}-{rating}... it loses X action(s) (Y of Z remaining)." / "...it HANGS -- no actions left this Round". | Default badge `IC SLOWED` (`ev-neutral`). The IC card persists; its lost passes are honoured by the proactive-IC loop (fewer IC attacks next turn). | Complex action; Slow loaded (`rating > 0` else 400, no spend); target must be PROACTIVE (reactive => 400) and not suppressed; trace only if targetable. |
| A14.F | slow | enemy IC (proactive) | Failure | To-hit missed (0 hits) -> outcome "missed"; OR hit but `slow_test net <= 0` -> outcome "resisted". | `type:"ic_slowed"`, "missed"/"resisted": "...missed (0 hits vs TN T)" / "...the IC RESISTS the opposed Slow test (D vs I) -- no effect." | Default badge; IC keeps its speed. | Both return `failed=True` for DINAB degrade. |
| A14.T | slow | enemy IC (proactive) | Tie | Opposed `slow_test` tie (`decker_succ == ic_succ` => `net 0`) => outcome "resisted" -- **folds into Failure** (A14.F). | Same as the "resisted" A14.F event. | Same as A14.F. | Distinct from a missed to-hit but same net outcome. |

### A15 -- `slow` vs Construct

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A15.S | slow | construct | Success | As A14.S **iff** the construct's IC_CATALOG entry is `ic_type=="proactive"`. | `type:"ic_slowed"` "slowed"/"hung", "Slow-R hits Construct-{rating}...". | Default badge; construct's passes reduced. | A reactive construct is immune -> 400 (`_slow_target_eligibility`). |
| A15.F | slow | construct | Failure | To-hit missed or `slow_test` resisted. | `type:"ic_slowed"` "missed"/"resisted". | no change. | -- |
| A15.T | slow | construct | Tie | `slow_test` tie -> "resisted" -> folds into Failure (A15.F). | Same as A15.F resisted event. | Same. | -- |

### A16 -- `slow` vs Party IC

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A16.S | slow | party IC | Success | As A14.S; Slow has no cluster modifier (unopposed to-hit uses the base combat TN). Proactive member only. | `type:"ic_slowed"` "slowed"/"hung". | Default badge; that member's passes reduced. | Each clustered member is slowed individually. |
| A16.F | slow | party IC | Failure | missed / resisted. | `type:"ic_slowed"` "missed"/"resisted". | no change. | -- |
| A16.T | slow | party IC | Tie | `slow_test` tie -> "resisted" -> Failure (A16.F). | Same as A16.F. | Same. | -- |

---

### A17-A20 -- `dinab` combat use (`POST /{id}/action` `action_type="dinab"`)

Free action: runs ONE DINAB-equipped program autonomously at pool = effective DINAB rating.
Offensive `attack` targets an active IC (or an enemy by id); cripplers/hog/lethal-less strikes hit
a revealed enemy decker. A miss/fully-resisted run degrades DINAB (-1); an all-1s miss crashes it
(`_dinab_resolve_failure`). Black Hammer / Killjoy cannot carry DINAB.

### A17 -- `dinab` (attack) vs enemy IC

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A17.S | dinab attack | enemy IC | Success | `_dinab_attack_ic` -> shared `cybercombat_attack` at pool=eff, Power=eff(+cluster). `boxes > 0`; `>=10` crash. | Crash: `type:"ic_crashed"`, "DINAB Attack-E CRASHED {type}-{rating}. Tally +A -> total". Hit: `type:"dinab_attack"`, success True, "DINAB Attack-E hits {type}-{rating}: {level} ({b} boxes), IC b/10." | ic_crashed -> `ev-ic-crashed`/IC CRASH; dinab_attack -> default badge `DINAB ATTACK`. `renderActiveIC` boxes update. | DINAB rating > 0; program not already used by hand this pass (else 400). Crash spawns Trap hidden IC. |
| A17.F | dinab attack | enemy IC | Failure | To-hit `successes <= 0` (whiff) -> `failed=True` degrades DINAB; all-1s crashes DINAB. | `type:"dinab_attack"`, success False, "DINAB Attack-E hits {type}-{rating}: None (0 boxes)...". | default badge; IC boxes unchanged; DINAB rating may drop. | -- |
| A17.T | dinab attack | enemy IC | Tie | **N/A** -- damage-staging (same as A1.T). | -- | -- | -- |

### A18 -- `dinab` (attack) vs Construct

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A18.S | dinab attack | construct | Success | As A17.S (construct is an active IC target for DINAB attack). | `dinab_attack` / `ic_crashed` with Construct label. | construct card boxes update; crash greys. | Construct active. |
| A18.F | dinab attack | construct | Failure | whiff -> DINAB degrade. | `type:"dinab_attack"` success False. | no box change; DINAB may drop. | -- |
| A18.T | dinab attack | construct | Tie | **N/A** -- damage-staging. | -- | -- | -- |

### A19 -- `dinab` (attack) vs Party IC

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A19.S | dinab attack | party IC | Success | As A17.S; Power = eff + cluster (Party hardness preserved). | `dinab_attack` / `ic_crashed`. | party member boxes update. | Auto-targets first active IC if no id given. |
| A19.F | dinab attack | party IC | Failure | whiff -> DINAB degrade. | `type:"dinab_attack"` success False. | no change. | -- |
| A19.T | dinab attack | party IC | Tie | **N/A** -- damage-staging. | -- | -- | -- |

### A20 -- `dinab` (attack / crippler / hog) vs enemy decker

`_dinab_strike_decker`: `attack` -> icon damage; `poison/restrict/reveal` -> cripple; `hog` ->
drain. Failure = no boxes / no reduction / no infection.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A20.S | dinab strike | enemy decker | Success | attack: `boxes > 0`; crippler: `reduction > 0`; hog: infected. | `type:"dinab_attack"`, success True: e.g. "DINAB Poison-E crips {name} bod -> V." (attack/hog analogous). | default badge `DINAB ATTACK`; `renderEnemyDeckers` reflects damage/attribute drop. | Enemy revealed; else 400 "no revealed enemy decker". |
| A20.F | dinab strike | enemy decker | Failure | `reduction <= 0` / `boxes <= 0` / not infected -> `failed=True` degrades DINAB (all-1s crashes it). | `type:"dinab_attack"`, success False. | no change; DINAB rating may drop. | -- |
| A20.T | dinab strike | enemy decker | Tie | Crippler/hog path: opposed net == 0 folds into Failure (A20.F). Attack path: N/A (damage-staging). | Same as A20.F. | Same as A20.F. | -- |

---

### A21-A32 -- Combat maneuvers (`POST /{id}/action` `action_type in {evade_detection, parry_attack, position_attack}`, `_apply_maneuver` ~L4197)

Simple actions resolved by `eng.maneuver_test`: the PC is the maneuvering icon (Evasion dice/rating
= `eff.evasion`, Cloak lowers TN), the target is the opposing icon (Sensor). For IC the opposing
Sensor dice = host Security Value and Sensor Rating = IC rating; for an enemy decker Sensor
dice/rating = its `sensor`, and a Lock-On utility lowers the opposing Sensor TN. `success = net > 0`
(strictly). Construct / Party IC use the **same IC branch** (`opp_sensor_dice = sec_value`,
`opp_sensor_rating = ic rating`) -- no construct/party-specific rule -- so their rows mirror the
enemy-IC row. All maneuver events use `type:"maneuver"` -> default badge `MANEUVER` (`ev-neutral`);
`renderRunState` redraws but the effect is stored state (evade/parry/position flags) consumed by a
later attack, so there is no immediate condition-monitor change.

#### Evade Detection (A21-A24)
On a PC win the target `evaded`/`evade_dir="lost_pc"`, `redetect_turn = turn + net` (it loses your
trail for `net` turns, shorter as tally climbs); voids a pending Parry. Tie/loss = it keeps you in
sensors.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A21.S | evade_detection | enemy IC | Success | `maneuver_test` net > 0 (PC Evasion vs IC Sensor=`sec_value` dice / IC rating TN). | `type:"maneuver"`, maneuver "evade_detection", "Evade Detection SUCCESS vs {IC} (M vs O) -- it loses your trail for N Combat Turns...". | default `MANEUVER` badge; sets `evaded` flag; the IC still renders but won't attack until re-detected. | Need an active IC / revealed enemy; blank target picks first eligible. |
| A21.F | evade_detection | enemy IC | Failure | net <= 0 (loss). | `type:"maneuver"`, "Evade Detection FAILED vs {IC} (M vs O) -- it keeps you in its sensors." | default badge; no flag set. | -- |
| A21.T | evade_detection | enemy IC | Tie | `man_succ == opp_succ` => `net 0`, `success=False` -> **folds into Failure** (A21.F, same "FAILED" text). | Same as A21.F. | Same as A21.F. | evade/parry ties are plain failures. |
| A22.S | evade_detection | construct | Success | Same IC branch (opp Sensor = `sec_value` / construct rating). net > 0. | `type:"maneuver"` "Evade Detection SUCCESS vs Construct ...". | default badge; `evaded` set on construct. | Construct treated as IC. |
| A22.F | evade_detection | construct | Failure | net <= 0. | "Evade Detection FAILED vs Construct...". | no flag. | -- |
| A22.T | evade_detection | construct | Tie | net 0 -> Failure (A22.F). | Same as A22.F. | Same. | -- |
| A23.S | evade_detection | party IC | Success | Same IC branch; no cluster modifier in `maneuver_test`. net > 0. | "Evade Detection SUCCESS vs {IC}..." for the chosen member. | `evaded` set on that member. | Targets one member. |
| A23.F | evade_detection | party IC | Failure | net <= 0. | "Evade Detection FAILED...". | no flag. | -- |
| A23.T | evade_detection | party IC | Tie | net 0 -> Failure (A23.F). | Same as A23.F. | Same. | -- |
| A24.S | evade_detection | enemy decker | Success | PC Evasion vs enemy `sensor` dice/rating; enemy Lock-On lowers the opposing Sensor TN. net > 0. | `type:"maneuver"` "Evade Detection SUCCESS vs {name}...". | `evaded` set on enemy (PC hidden from it). | Enemy must be revealed. |
| A24.F | evade_detection | enemy decker | Failure | net <= 0. | "Evade Detection FAILED vs {name}...". | no flag. | -- |
| A24.T | evade_detection | enemy decker | Tie | net 0 -> Failure (A24.F). | Same as A24.F. | Same. | -- |

#### Parry Attack (A25-A28)
On a PC win: `state["pc_parry"] = {vs: target, bonus: net}` -> +net TN to the target's next attack
on the PC. Tie/loss = no guard.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A25.S | parry_attack | enemy IC | Success | `maneuver_test` net > 0. | `type:"maneuver"`, "Parry Attack SUCCESS vs {IC} (M vs O) -- +N TN to its next attack on you." | default `MANEUVER` badge; stores `pc_parry` (consumed by `_consume_attack_mods_vs_pc`). | Active IC. |
| A25.F | parry_attack | enemy IC | Failure | net <= 0. | "Parry Attack FAILED vs {IC} (M vs O)." | no bonus stored. | -- |
| A25.T | parry_attack | enemy IC | Tie | net 0 (`man==opp`) -> `success=False` -> **Failure** (A25.F). | Same as A25.F. | Same. | -- |
| A26.S | parry_attack | construct | Success | Same IC branch; net > 0. | "Parry Attack SUCCESS vs Construct...". | `pc_parry` vs construct. | -- |
| A26.F | parry_attack | construct | Failure | net <= 0. | "Parry Attack FAILED vs Construct...". | none. | -- |
| A26.T | parry_attack | construct | Tie | net 0 -> Failure (A26.F). | Same as A26.F. | Same. | -- |
| A27.S | parry_attack | party IC | Success | Same IC branch; net > 0. | "Parry Attack SUCCESS vs {IC}...". | `pc_parry` vs that member. | -- |
| A27.F | parry_attack | party IC | Failure | net <= 0. | "Parry Attack FAILED...". | none. | -- |
| A27.T | parry_attack | party IC | Tie | net 0 -> Failure (A27.F). | Same as A27.F. | Same. | -- |
| A28.S | parry_attack | enemy decker | Success | PC Evasion vs enemy `sensor`; net > 0. | "Parry Attack SUCCESS vs {name} -- +N TN...". | `pc_parry` vs enemy. | Enemy revealed. |
| A28.F | parry_attack | enemy decker | Failure | net <= 0. | "Parry Attack FAILED vs {name}...". | none. | -- |
| A28.T | parry_attack | enemy decker | Tie | net 0 -> Failure (A28.F). | Same as A28.F. | Same. | -- |

#### Position Attack (A29-A32)
On a PC win: `state["pc_position"]` = `{tn_reduction: net}` or `{power_bonus: net}` (player's
`position_choice`). **Distinct three-way**: win (net>0), **tie** (`man==opp` -> "no advantage"),
backfire (`opp>man` -> the enemy gains the positioning via `_npc_position_bonus`). So `.T` is a
genuine branch and `.F` = backfire.

| ID | Action | Target type | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|-------------|---------|-----------------|-----------------|-----------------|------------------------|
| A29.S | position_attack | enemy IC | Success | `maneuver_test` net > 0. Stores `pc_position` (-N TN or +N Power). | `type:"maneuver"`, "Position Attack SUCCESS vs {IC} (M vs O) -- {-N TN\|+N Power} on your next attack." | default `MANEUVER` badge; `pc_position` consumed by next PC attack (`_consume_attack_mods_vs_target`). | Active IC; `position_choice` = "power" or "tn" (default tn). |
| A29.F | position_attack | enemy IC | Failure (backfire) | `opp_succ > man_succ`: the IC gains the positioning (`target["position_bonus"]` via `_npc_position_bonus`: +Power if PC persona >= 5 boxes, else -TN). | "Position Attack BACKFIRED vs {IC} (M vs O) -- it gains {+X Power\|-X TN} on its next attack on you." | default badge; stores an enemy bonus (used against the PC next). | Risky maneuver. |
| A29.T | position_attack | enemy IC | Tie | `man_succ == opp_succ` => genuine "tied" branch: no advantage to either side. | "Position Attack tied vs {IC} (M vs O) -- no advantage gained." | default badge; **no** state flag stored. | Distinct from both S and F. |
| A30.S | position_attack | construct | Success | Same IC branch; net > 0. | "Position Attack SUCCESS vs Construct...". | `pc_position` stored. | -- |
| A30.F | position_attack | construct | Failure (backfire) | opp > man -> construct gains position. | "Position Attack BACKFIRED vs Construct...". | enemy bonus stored. | -- |
| A30.T | position_attack | construct | Tie | man == opp -> "no advantage". | "Position Attack tied vs Construct...". | no flag. | -- |
| A31.S | position_attack | party IC | Success | Same IC branch; net > 0. | "Position Attack SUCCESS vs {IC}...". | `pc_position` stored. | -- |
| A31.F | position_attack | party IC | Failure (backfire) | opp > man -> member gains position. | "Position Attack BACKFIRED vs {IC}...". | enemy bonus stored. | -- |
| A31.T | position_attack | party IC | Tie | man == opp -> "no advantage". | "Position Attack tied vs {IC}...". | no flag. | -- |
| A32.S | position_attack | enemy decker | Success | PC Evasion vs enemy `sensor`; net > 0. | "Position Attack SUCCESS vs {name}...". | `pc_position` stored. | Enemy revealed. |
| A32.F | position_attack | enemy decker | Failure (backfire) | opp > man -> enemy gains position. | "Position Attack BACKFIRED vs {name}...". | enemy bonus stored. | -- |
| A32.T | position_attack | enemy decker | Tie | man == opp -> "no advantage". | "Position Attack tied vs {name}...". | no flag. | -- |

---

### Running ID index

| ID | Action | Target |
|----|--------|--------|
| A1 | attack_ic | enemy IC |
| A2 | attack_ic | construct |
| A3 | attack_ic | party IC |
| A4 | area_attack | enemy IC |
| A5 | area_attack | construct |
| A6 | area_attack | party IC |
| A7 | area_attack | enemy decker |
| A8 | enemy-decker attack (plain) | enemy decker |
| A9 | enemy-decker cripplers (poison/restrict/reveal) | enemy decker |
| A10 | enemy-decker hog | enemy decker |
| A11 | enemy-decker black_hammer | enemy decker |
| A12 | enemy-decker killjoy | enemy decker |
| A13 | steamroller | tar IC |
| A14 | slow | enemy IC (proactive) |
| A15 | slow | construct |
| A16 | slow | party IC |
| A17 | dinab (attack) | enemy IC |
| A18 | dinab (attack) | construct |
| A19 | dinab (attack) | party IC |
| A20 | dinab (attack/cripple/hog) | enemy decker |
| A21 | evade_detection | enemy IC |
| A22 | evade_detection | construct |
| A23 | evade_detection | party IC |
| A24 | evade_detection | enemy decker |
| A25 | parry_attack | enemy IC |
| A26 | parry_attack | construct |
| A27 | parry_attack | party IC |
| A28 | parry_attack | enemy decker |
| A29 | position_attack | enemy IC |
| A30 | position_attack | construct |
| A31 | position_attack | party IC |
| A32 | position_attack | enemy decker |

#### N/A pairs (no ID consumed)

- `attack_ic` vs enemy decker -- deckers are struck via `/enemy-decker/attack` (A8-A12).
- enemy-decker attack / cripplers / hog / black_hammer / killjoy vs enemy IC, construct, party IC -- these programs target deckers/frames only, never routed through IC.
- `steamroller` vs enemy IC (non-tar), construct, party IC, enemy decker -- tar-only weapon; non-tar target => HTTP 400.

---

<a id="sec-b"></a>

## Section B &mdash; PC Utility / Hacking / System / Support

> **Static analysis only.** Every row below is derived from reading the actual code
> branches in `app/routers/matrix_runs.py` (`perform_action` ~L5266 onward and the
> dedicated endpoints) and `app/services/matrix_engine.py`. The server was **not** run.
> Where a description text is quoted it is the literal string emitted by `_append_event`.

### Legend

**ID scheme.** Each action gets a block `B<n>`; the three outcome rows are:
- `B<n>.S` -- **Success**
- `B<n>.F` -- **Failure**
- `B<n>.T` -- **Tie**

**Tie semantics (user-confirmed).** For an opposed `system_test`
(`matrix_engine.system_test` ~L77):
- `net = decker_successes - host_successes`.
- **Success** requires `net >= 0` **AND** `decker_successes > 0`.
- A **tie** is `net == 0`. By the engine rule, a `0-vs-0` tie (both whiff) is a
  **FAILURE** for the decker (`decker_successes > 0` fails), and the tally still rises by
  the host's successes (0 in the pure 0-v-0 case, but any `k-vs-k` tie with `k>0` succeeds
  because `net==0` and `decker_successes>0`). So in practice: a `k-vs-k` tie with `k>=1`
  is a **decker WIN** (house rule: tie goes to the decker); only the `0-vs-0` tie loses.
  Each `.T` row states which of these two tie-shapes it describes.
- For actions with **no opposed roll** (e.g. `unload_program`, `swap_memory`,
  `decompress_file`, `null_operation`, `suppress_ic`, `reveal_host_ratings`), the `.T`
  row is written **"Tie: N/A -- unopposed"** with an explanation.

**Enemy axis.** Nearly every Section-B action targets the **host**, a **file**, or the
**PC's own state** -- not an enemy icon. Where the `{enemy IC, enemy decker, construct,
party IC}` axis does not apply, the row says
`target = host/file/self; enemy axis N/A except reactive: <which>`. The **Provoked
opponent** column names the reactive hostiles a System Test can wake:
- **Probe IC** -- tests once per System Test the decker makes (`probe_test` ~L787), if it
  was already active (`_preexisting_ic_ids`). Adds tally on its own secret Sensor test.
- **Tar Baby / Tar Pit** (lurking) -- `_autofire_lurking_tar` ~L4748 ->
  `_resolve_lurking_tar` ~L7346, fires once **per utility use** (`utility_rating > 0`).
- **Worm** (lurking) -- resolves each Combat Turn in `new_turn`
  (`_resolve_lurking_worm` ~L7201); not fired by a single action.
- **Trace IC** -- drives its hunt/locate cycle in `_advance_npc_pass`, not by the action
  itself; a completed trace accelerates tally (`_bump_security_tally`).
- **Data Bomb** -- `_trigger_access_data_bomb` ~L3976 -> `_detonate_data_bomb` ~L3586, on
  a **successful** `download_data` / `edit_file` against a bombed target; also an
  Exploding Scramble on a failed `decrypt_file`.
- **Enemy decker / Construct** -- act in `_advance_npc_pass` after the action resolves;
  any spawned mid-action is held back one pass (`_preexisting_enemy_ids`, `acted_pass`).

**Shared post-test pipeline** (runs after the generic `system_test` for every
non-early-return action): `_bump_security_tally` -> build `log_entry` (`type:"action"`) ->
`_append_event` (~L748) -> `_check_and_activate_sheaf` -> `_autofire_lurking_tar` ->
Probe loop -> spawn-hold stamping -> `_advance_npc_pass`. This is why any generic action
can "provoke" a Tar/Probe/enemy even though it targets the host.

**Generic `system_test` roll.** decker pool = `computer_skill + hacking_pool_dice`;
decker TN = `max(2, subsystem_rating + extra_tn_modifier - utility_rating)`; host rolls
`security_value` dice vs `detection_factor`; `tally_increase = host_successes` (added
**every** attempt, success or fail). `roll_dice` (~L29) applies the **rule of 6** when
`tn > 6`.

**Action entry shape** (~L5685): `{type, action, subsystem, description, success,
decker_roll, host_roll, tally_increase, tally_total, action_cost, note, turn, init, ts}`.

---

### B1 -- logon_to_host  (`doLogon` ~L4478; Access System Test, Complex)

Target = host (Access subsystem). Opposed Access Test. Stolen linked passcode + Deception
utility grants `-2` TN. `logon_completed` is threaded into `_advance_npc_pass`.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B1.S | logon_to_host | host / access | Trace IC, Probe IC, enemy decker (all act in `_advance_npc_pass` after). Tar Baby only if a utility (Deception) was run. | Logon accepted; connection established. | `net>=0 & decker_succ>0`. pool `computer_skill+HP` vs `max(2, access + tn_mod - util)`; `console_access` halves host SV; `linked_passcode`+util => `-2` TN. tally `+host_succ`. | `type:"action"`, desc `"Logon To Host -- SUCCESS (D vs H successes). Tally +N -> T."` (+ `_advance_npc_pass` fires the logon-completed event). | `renderRunState`/`renderEventEntry`; `renderStage` flips to on-host; `renderActionArea` unlocks host ops. | Must not already be logged on; run active. |
| B1.F | logon_to_host | host / access | Same reactive set; tally rose so sheaf may wake more IC. | Rebuffed; tally rises; retry. | `net<0` OR `decker_succ==0`. tally `+host_succ`. | `type:"action"`, desc `"Logon To Host -- FAILED (...). Tally +N -> T."` | `renderAlertBadge`/`renderRunState` reflect higher tally; stays at logon stage. | Retryable. |
| B1.T | logon_to_host | host / access | Same. | `k-vs-k, k>=1` = **WIN** (house rule tie->decker). `0-vs-0` = **FAIL**. | `net==0`: success iff `decker_succ>0`. | As B1.S (k>=1) or B1.F (0-v-0). | As matching outcome. | Tie resolves via the `net>=0 & succ>0` rule. |

### B2 -- analyze_host  (Control System Test, Complex)

Target = host (ACIFS + Security Rating). `_apply_analyze_host` banks/reveals by net
successes.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B2.S | analyze_host | host / self-knowledge | target=host; enemy axis N/A except reactive: Probe IC, Tar Baby (if Analyze util run), post-test NPC pass. | Reveals subsystem ratings. `net>=6` or `>=hidden_count` reveals ALL; `1<=net<hidden` banks `host_analyze_pending`. | Generic `system_test`; reveal driven by `decker_net_successes`. tally `+host_succ`. | `type:"host_analyzed"` -- either `"... X 8, Files 6 revealed."` or `"Analyze Host succeeded -- choose N subsystem rating(s) to reveal."` (plus the generic `type:"action"` entry). | `renderHostRatings` (~L3187) fills ACIFS panel; banked case surfaces reveal-picker (see B33). | Security Rating reveal mirrors to org LTG (`sync_host_security_to_org`). |
| B2.F | analyze_host | host | Same reactive. | No reveal; tally rises. | `net<0`/`0-succ`. tally `+host_succ`. | Generic `type:"action"` FAILED entry only (no `host_analyzed`). | `renderHostRatings` unchanged; tally badge updates. | Retryable. |
| B2.T | analyze_host | host | Same. | `k-vs-k,k>=1` WIN -> reveal/bank; `0-v-0` FAIL. | `net==0` rule. | As B2.S / B2.F. | As matching. | -- |

### B3 -- analyze_ic  (Free; reveals an IC type+rating)

Target = an active IC's identity (not an attack). `enemy axis`: the "enemy" here is an
IC whose identity is being read.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B3.S | analyze_ic | active IC (identity) | Probe IC tests this System Test; Tar Baby if Analyze util run; NPC pass after. | Reveals target IC's `type`+`rating` (`ic["analyzed"]=True`). Targets `target_ic_id` else first un-analyzed active IC. | Generic `system_test` success. tally `+host_succ`. | `type:"ic_analyzed"` `"IC analyzed: <type> Rating <r> revealed."` (+ generic action entry). | `renderRunState` swaps the "Unknown IC" marker for real type/rating; `renderActionArea` enables typed targeting. | Free action. Redaction lifts once `analyzed`. |
| B3.F | analyze_ic | active IC | Same. | No reveal; IC stays "Unknown IC"; tally rises. | `net<0`/`0-succ`. | Generic action FAILED entry only. | IC card stays redacted. | Retryable. |
| B3.T | analyze_ic | active IC | Same. | `k-vs-k,k>=1` WIN reveal; `0-v-0` FAIL. | `net==0` rule. | As B3.S/B3.F. | As matching. | -- |

### B4 -- analyze_icon  (Free; Control test; data-bomb discovery)

Target = a located file or the Slave device. Scope-encoded (`files::<name>` /
`slave::<device>`). `_apply_analyze_icon`. Analyze utility also `-sensor` to TN.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B4.S | analyze_icon | file / slave device | target=file/device; enemy axis N/A except reactive: Probe IC, Tar Baby (Analyze util), NPC pass. The scanned bomb is NOT yet triggered (discovery only). | Reveals an undefused data bomb on the icon (`bomb["discovered"]=True`), or reports clear. TN `-= sensor` (extra). | Generic `system_test`; TN also `- eff.sensor` for analyze_icon. tally `+host_succ`. | `type:"data_bomb_found"` `"Analyze Icon on \"X\" -- DATA BOMB detected. Defuse it before..."` OR `type:"data_bomb_clear"` `"...nothing unusual; no data bomb..."` (+ generic action entry). | `renderRunState`/`renderDownloadsPanel` mark the file bombed; enables Defuse (B27). | Only bomb-discovery path (Analyze Subsystem no longer surfaces bombs). |
| B4.F | analyze_icon | file / device | Same reactive. | No discovery; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only (no data_bomb_found). | No bomb marker added. | Retryable. |
| B4.T | analyze_icon | file / device | Same. | `k-vs-k,k>=1` WIN -> discover/clear; `0-v-0` FAIL. | `net==0` rule. | As B4.S/B4.F. | As matching. | -- |

### B5 -- analyze_security  (Control test)

Target = host security posture. `state["host_security_revealed"]=True` + snapshot into
`security_known`.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B5.S | analyze_security | host / self-knowledge | target=host; enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. | Reveals Security Rating (code+value), current tally, alert status; snapshots `security_known`. | Generic `system_test` success. tally `+host_succ`. | `type:"security_analyzed"` `"Analyze Security -- Security Rating C-V, security tally T, alert status A (as of turn N)."` (+ generic action entry). | `renderAlertBadge` (~L3168)/`renderHostRatings` show revealed rating + known tally. | Snapshot is a point-in-time known value; the live tally may drift after. |
| B5.F | analyze_security | host | Same reactive. | No reveal; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | No security snapshot; badge tally updates. | Retryable. |
| B5.T | analyze_security | host | Same. | `k-vs-k,k>=1` WIN reveal; `0-v-0` FAIL. | `net==0` rule. | As B5.S/B5.F. | As matching. | -- |

### B6 -- analyze_subsystem  (Simple; Control test)

Target = one named subsystem. Reveals trap doors + scramble IC on that subsystem; on
`access` reveals host LTG status (a persisted DB edit).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B6.S | analyze_subsystem | host subsystem | target=subsystem; enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. | Reveals concealed trap doors (`d["discovered"]`), scramble IC (`s["discovered"]`) on that subsystem; `access` reveals LTG (`host_ltg_revealed`, may flip host visible + `sync_host_reveal_to_org`). | Generic `system_test` success. Label suffixed `" - <Subsystem>"`. tally `+host_succ`. | `type:"trap_door_found"` and/or `type:"scramble_found"` and/or `type:"host_ltg_revealed"` (has_ltg true/false) (+ generic action entry). | `renderTrapDoorsPanel` (~L2478) lists door; `renderHostRatings` shows LTG addr; scramble surfaced for Decrypt (B12). | Access-analysis DB reveal only on the first successful access analysis. |
| B6.F | analyze_subsystem | subsystem | Same reactive. | Nothing revealed; on `access` emits a themed blocked event. tally rises. | `net<0`/`0-succ`. | On access-fail: `type:"access_analysis_blocked"` `"Access subsystem analysis failed -- the host blocked the discovery attempt. You can try again."` (+ generic action FAILED). Other subsystems: generic only. | `renderRunState` shows blocked note; no reveals. | Retryable; does not leak whether an LTG exists. |
| B6.T | analyze_subsystem | subsystem | Same. | `k-vs-k,k>=1` WIN reveal; `0-v-0` FAIL. | `net==0` rule. | As B6.S/B6.F. | As matching. | -- |

### B7 -- locate_paydata  (System Test; ongoing)

Target = host Index/Files (paydata list). Reveals `min(net, remaining)` files at random
via a local `random.Random` (never seeds global RNG).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B7.S | locate_paydata | host / paydata index | target=host; enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. | Reveals `min(net, remaining)` undiscovered, non-destroyed paydata (`p["located"]=True`); if none left, "search complete". | Generic `system_test`; `net = max(1, decker_net_successes)`. Local RNG seeded from run id/turn/tally/count. tally `+host_succ`. | `type:"paydata_located"` `"Paydata located: Name (Mp), ..."` OR `"Search complete -- no further paydata found."` (+ generic action entry). | `renderDownloadsPanel` (~L2647) lists located files with size/is_key; enables Download (B10). | Repeatable until all paydata found. Full list stays GM-only. |
| B7.F | locate_paydata | host | Same reactive. | No new files; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | Downloads panel unchanged. | Retryable. |
| B7.T | locate_paydata | host | Same. | `k-vs-k,k>=1` WIN locate; `0-v-0` FAIL. | `net==0` rule. | As B7.S/B7.F. | As matching. | -- |

### B8 -- locate_ic  (System Test; re-acquire a slipped IC)

Target = a previously-detected, then-lost IC. `_apply_locate_ic`. Cannot reveal
never-seen icons.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B8.S | locate_ic | a slipped IC (esp. trace in locate cycle) | Probe IC, Tar Baby (util), NPC pass. | Re-acquires the icon (`ic["located"]=True`) so it can be attacked again. | Generic `system_test` success; `_apply_locate_ic(test_success=True, target_ic_id)`. tally `+host_succ`. | Event from `_apply_locate_ic` (locate result) + generic action entry. | `renderRunState` un-hides the IC; a re-acquired trace becomes targetable (`_trace_is_targetable`). | Only re-acquires icons already detected then lost (e.g. after Evade Detection or a trace entering its location cycle). |
| B8.F | locate_ic | slipped IC | Same reactive. | Not re-acquired; tally rises. | `net<0`/`0-succ`. | `_apply_locate_ic(test_success=False)` event + generic FAILED. | IC stays hidden/untargetable. | Retryable. |
| B8.T | locate_ic | slipped IC | Same. | `k-vs-k,k>=1` WIN acquire; `0-v-0` FAIL. | `net==0` rule. | As B8.S/B8.F. | As matching. | -- |

### B9 -- locate_decker  (Complex; System Test + opposed Sensor Test)

Target = a hostile decker that slipped you. `_apply_locate_decker` adds the #6 opposed
Sensor Test vs full Masking + Sleaze.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B9.S | locate_decker | **enemy decker** (re-acquire) | Enemy decker is the target; ALSO Probe IC, Tar Baby (util), NPC pass. | Re-acquires the enemy decker icon; opposed Sensor vs Masking+Sleaze also passed. | Generic `system_test` + `_apply_locate_decker(scanner=util)` opposed Sensor. tally `+host_succ`. | `_apply_locate_decker` event + generic action entry. | `renderRunState` re-reveals enemy icon; `renderActionArea` enables attack/scan (B28). | Only re-acquires an enemy decker already detected then lost. |
| B9.F | locate_decker | enemy decker | Same reactive. | Not re-acquired (System Test or Sensor Test lost); tally rises. | `net<0`/`0-succ` OR lost Sensor Test. | `_apply_locate_decker(test_success=...)` event + generic. | Enemy stays hidden. | Retryable. |
| B9.T | locate_decker | enemy decker | Same. | `k-vs-k,k>=1` WIN (then Sensor); `0-v-0` FAIL. | `net==0` rule for the System Test; Sensor Test is a separate opposed check. | As B9.S/B9.F. | As matching. | -- |

### B10 -- download_data  (System Test; ongoing transfer)

Target = a located file. Storage pre-check before spending the action. Multi-turn
transfers become a background `active_download` auto-running Null Operation each turn.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B10.S | download_data | file | target=file; enemy axis N/A except reactive: **Data Bomb** (`_trigger_access_data_bomb` on success), Probe IC, Tar Baby (util), NPC pass. | Pulls the file: single-turn -> `_complete_download` (bank + storage); multi-turn -> starts `active_download` (bg transfer, only Free actions allowed until done). | Generic `system_test` success; `stored` = compressor-effective size; `turns=ceil(stored/io)`. tally `+host_succ`. **Bombed target detonates** (see B27 mechanic). | `type:"download_started"` (multi-turn) OR `data_downloaded` (already had); `_trigger_access_data_bomb` may append `type:"data_bomb"`. (+ generic action entry). | `renderDownloadsPanel` shows progress bar; bg transfer disables Simple/Complex ops. | 400 pre-check if it won't fit storage (action not spent). |
| B10.F | download_data | file | Data bomb does NOT trigger on failure; Probe/Tar/NPC still. | No file pulled; tally rises. | `net<0`/`0-succ`. bomb inert on failure. | Generic action FAILED only. | Downloads panel unchanged. | Retryable. |
| B10.T | download_data | file | As B10.S (win) or B10.F (0-v-0). | `k-vs-k,k>=1` WIN pull (+bomb if bombed); `0-v-0` FAIL. | `net==0` rule. | As B10.S/B10.F. | As matching. | Aborting a bg transfer (logoff/host crash) corrupts it (`_corrupt_active_download`). |

### B11 -- edit_file  (System Test; sabotage)

Target = a located paydata file. Sub-modes: ERASE (`destroyed`) / MODIFY (`tampered`).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B11.S | edit_file | file | target=file; enemy axis N/A except reactive: **Data Bomb** (bombed file detonates on success), Probe IC, Tar Baby (util), NPC pass. | ERASE: `pd["destroyed"]=True`; MODIFY: `pd["tampered"]=True`. Denies clean data to the owner. | Generic `system_test` success; `edit_mode` selects erase/modify. tally `+host_succ`. Bombed file triggers `_trigger_access_data_bomb`. | `type:"file_deleted"` `"File \"X\" erased from the host -- the data is gone."` OR `type:"file_modified"` `"...corrupted/falsified."` (+ possible `data_bomb`, + generic action). | `renderDownloadsPanel` greys the destroyed/tampered file. | RAW create/copy sub-modes omitted (no consumer). |
| B11.F | edit_file | file | Data bomb inert on failure; Probe/Tar/NPC still. | No edit; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | File card unchanged. | Retryable. |
| B11.T | edit_file | file | As B11.S (win) / B11.F (0-v-0). | `k-vs-k,k>=1` WIN edit (+bomb); `0-v-0` FAIL. | `net==0` rule. | As B11.S/B11.F. | As matching. | -- |

### B12 -- decrypt_file  (Simple; vs Scramble IC, NOT the generic subsystem test)

Target = a **discovered** Scramble IC's protected data. Its rating IS the decrypt TN.
**Adds NO security tally.** Early-returns (never runs the generic `system_test`).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B12.S | decrypt_file | file (scramble) | target=file; enemy axis N/A except reactive: **Exploding Scramble's linked Data Bomb** on FAILURE only. (No generic post-test pipeline -- early return -- so Probe/Tar/NPC do NOT run here.) | Scramble decrypted (`scr` removed); data accessible. **No tally.** | `eng.scramble_decrypt_test(pool, scramble_rating, decrypt_util)`; not opposed by host SV. | `type:"decrypt", success:True` `"Scramble decrypted -- protected data accessible. No tally increase."` | `renderRunState`/`renderDownloadsPanel` mark data readable; enables Download. | Scramble must be `discovered` via Analyze Subsystem (B6) first, else refused with a "no discovered scramble" event. |
| B12.F | decrypt_file | file (scramble) | **Exploding Scramble** -> `_detonate_data_bomb`; a POISON scramble destroys protected data (`protected["destroyed"]`), key data = permanent loss. | Failed decrypt; possible data destruction / bomb detonation. **No decrypt tally** (bomb rating adds if it detonates). | `scramble_decrypt_test` fail; `scramble_failure_consequence(variant, is_key, rating, skill)`. | `type:"decrypt", success:False` (with `key_data_lost`, `data_destroyed`, `file_name`, `cons["message"]`); possible `type:"data_bomb"` from detonation. | `renderDownloadsPanel` greys destroyed file; `renderRunState` shows loss. | Poison/exploding variants punish failure. |
| B12.T | decrypt_file | file (scramble) | As above. | Not opposed by a `system_test`; the decrypt test is decker-vs-TN, not decker-vs-host. **Tie: N/A -- unopposed** (no `net==0` host comparison; outcome is pass/fail of `scramble_decrypt_test`). | -- | -- | -- | Uses its own decrypt primitive, no host security roll. |

### B13 -- decompress_file  (Complex; NO test -- storage bookkeeping)

Target = a downloaded compressed file. Pure storage math (`_apply_decompress`).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B13.S | decompress_file | self (deck storage) | target=self; enemy axis N/A except reactive: **none** -- early return, no System Test, no `_autofire_lurking_tar`, no NPC pass driven from here. | Expands a compressed stored file back to full size (`_apply_decompress`). | No roll. Needs the extra free Mp when storage tracked. tally unchanged. | `_apply_decompress` event describing the expansion (+ no generic action entry). | `renderMemoryPanel` (~L2763)/`renderDownloadsPanel` update storage usage. | 400 (action NOT spent) if it won't fit tracked storage. |
| B13.F | decompress_file | self | none reactive | Rejected pre-spend (won't fit) -> 400; no state change. | No roll. | HTTP 400, no event. | No change. | -- |
| B13.T | decompress_file | self | none | **Tie: N/A -- unopposed.** No opposed roll exists; this is pure bookkeeping. | -- | -- | -- | -- |

### B14 -- null_operation  (auto only; covers a background download)

There is **no manual `null_operation` action_type** in `perform_action`. It is emitted
automatically by `_auto_null_operation` / `_tick_active_download` while an `active_download`
runs. A Control System Test at Computer skill (no Hacking Pool), host opposed as normal.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B14.S | null_operation (auto) | host / control | target=host; enemy axis N/A except reactive: Probe/Trace/NPC via the turn cycle (this rolls a host opposed test that can wake the sheaf). | Auto op succeeds; download progresses; tally may rise. | `system_test(pool=computer_skill, control, SV, DF)`, **no Hacking Pool**. tally `+host_succ`. | `type:"null_operation"` with `success/decker_roll/host_roll/tally_increase/tally_total/file_name/turns_left` `"Auto Null Operation covers the ongoing download of \"X\" (SUCCESS)."` | `renderDownloadsPanel` decrements turns-left; `renderEventLog` shows the null-op line. | Only fires during a bg download; New Turn advances it. |
| B14.F | null_operation (auto) | host | Same. | Op "fails" but the transfer still ticks; tally rises. | `net<0`/`0-succ`. tally `+host_succ`. | Same `type:"null_operation"` with `success:False` `"...(FAILED)."` | Same panel; higher tally badge. | Failure does not corrupt the download by itself. |
| B14.T | null_operation (auto) | host | Same. | `k-vs-k,k>=1` WIN; `0-v-0` FAIL (per `net==0` rule). | `net==0` rule. | As B14.S/B14.F. | As matching. | The player cannot invoke this directly. |

### B15 -- crash_host  (Control/Crash System Test; starts a countdown)

Target = the host itself. On success starts `crash_host_countdown`; all IC `-2` rating
during it; host rolls SV vs decker MPCP each turn to abort.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B15.S | crash_host | host | target=host; enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. The countdown weakens ALL IC (`-2`). | Starts shutdown countdown `turns=ceil(10/net)`; `_apply_crash_ic_penalty`. Completing it = clean logoff (`_complete_host_crash`, no dump shock). | Generic `system_test` success; `successes=max(1,net)`. tally `+host_succ`. | `type:"crash_host_started"` `"Crash Host initiated -- host shutdown in N turn(s) (K successes). All IC ratings -2 during the countdown; the host rolls Security Value vs your MPCP each turn to abort."` (+ generic action entry). | `renderCrashCountdown` (~L3205) shows the timer; IC cards show `-2`. | Host may abort each turn (`_process_crash_countdown`) -> `_restore_crash_ic_penalty`. |
| B15.F | crash_host | host | Same reactive. | No countdown; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | No countdown widget. | Retryable. |
| B15.T | crash_host | host | Same. | `k-vs-k,k>=1` WIN start; `0-v-0` FAIL. | `net==0` rule. | As B15.S/B15.F. | As matching. | -- |

### B16 -- validate_passcode  (Control/Validate System Test)

Target = host security tables (plant a fake passcode -> Legitimate status for the PC).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B16.S | validate_passcode | host / self-status | target=host; enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. Affects how **IC** target the PC (Legitimate column). | `has_legitimate_status=True`; IC now hit the persona on the Legitimate to-hit column until logoff / active alert. | Generic `system_test` success. tally `+host_succ`. | `type:"validate_passcode", success:True` `"Validate Passcode successful -- Legitimate status granted: IC now attack your persona on the Legitimate to-hit column..."` (+ generic action entry). | `renderRunState` shows Legitimate badge; combat TNs shift. | Wiped on active alert / logoff. |
| B16.F | validate_passcode | host | Same reactive. | No status; tally rises; retry. | `net<0`/`0-succ`. | `type:"validate_passcode", success:False` `"Validate Passcode failed -- the host rejected the plant (tally +N). You can try again."` (+ generic). | No Legitimate badge. | Retryable. |
| B16.T | validate_passcode | host | Same. | `k-vs-k,k>=1` WIN grant; `0-v-0` FAIL. | `net==0` rule. | As B16.S/B16.F. | As matching. | -- |

### B17 -- invalidate_passcode  (Control/Validate System Test; `__all__` = +4 TN)

Target = host passcode tables. Flips Legitimate security icons (IC / enemy deckers) to
Intruding (PERMANENT). `__all__` flips every one at +4 TN.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B17.S | invalidate_passcode | host tables -> **IC & enemy deckers** | The flipped targets are IC / enemy deckers (revised to-hit column). Also Probe IC, Tar Baby (util), NPC pass. | `_invalidate_passcodes`: one named IC/decker, or ALL (`__all__`, +4 TN) flip Legitimate->Intruding, permanently. | Generic `system_test` success; `+4` TN if `target_ic_id==__all__`. tally `+host_succ`. | `type:"invalidate_passcode", success:True, whole_list, flipped` `"... N security icon(s) flip to Intruding: ..."` OR single-target text (+ generic action entry). | `renderRunState` updates each flipped icon's status; combat TNs revised. | Permanent (unlike PC's own Validate). |
| B17.F | invalidate_passcode | host tables | Same reactive. | No flip; tally rises; retry. | `net<0`/`0-succ`. | `type:"invalidate_passcode", success:False` `"Invalidate Passcode failed -- the host preserved its passcode tables (tally +N). You can try again."` (+ generic). | No status change. | Retryable. |
| B17.T | invalidate_passcode | host tables | Same. | `k-vs-k,k>=1` WIN flip; `0-v-0` FAIL. | `net==0` rule. | As B17.S/B17.F. | As matching. | Success with no Legitimate target still logs "no ... icon was affected". |

### B18 -- decoy  (System Test; deploy countermeasure persona)

Target = self (deploy a decoy). IC roll `1D6 <= successes` to hit the decoy instead
(`_decoy_intercept`).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B18.S | decoy | self | target=self (draws proactive IC attacks); enemy axis N/A except reactive: Probe IC, Tar Baby (util), NPC pass. Decoy interacts with **proactive IC** (not trace). | Deploys decoy: `decoy_successes = decker_roll.successes`, `decoy_hp=0`. Each proactive IC attack rolls `1D6 <= successes` to hit the decoy (10-box CM). | Generic `system_test` success; decoy strength = **decker roll successes** (not net). tally `+host_succ`. | `type:"decoy_deployed"` `"Decoy deployed with N success(es). Each proactive IC attack: roll 1D6 -- if result <= successes, IC hits decoy (10-box CM)."` (+ generic action entry). | `renderRunState` shows decoy + its 0/10 CM; `renderEventEntry` shows `decoy_intercepted` when it soaks a hit. | Decoy is NOT effective vs trace IC. Cleared on logoff/host crash. |
| B18.F | decoy | self | Same reactive. | No decoy; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | No decoy card. | Retryable. |
| B18.T | decoy | self | Same. | `k-vs-k,k>=1` WIN deploy; `0-v-0` FAIL. | `net==0` rule. | As B18.S/B18.F. | As matching. | -- |

### B19 -- redirect_datatrail  (Complex; System Test)

Target = self (datatrail). Each success increments `redirects_placed` (`-1` to Trace
Factor going forward).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B19.S | redirect_datatrail | self / datatrail | target=self (vs **Trace IC** effectiveness); Probe IC, Tar Baby (util), NPC pass. | `redirects_placed += 1` -> Trace Factor +1 going forward (traces locate the jackpoint less easily). | Generic `system_test` success. tally `+host_succ`. | `type:"redirect_placed"` `"Redirect placed. Trace Factor +1 going forward ... Total redirects this run: N."` (+ generic action entry). | `renderRunState` shows redirect count; trace hunt/locate rolls harder next cycle. | Cumulative. |
| B19.F | redirect_datatrail | self | Same reactive. | No redirect; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. | No change. | Retryable. |
| B19.T | redirect_datatrail | self | Same. | `k-vs-k,k>=1` WIN place; `0-v-0` FAIL. | `net==0` rule. | As B19.S/B19.F. | As matching. | -- |

### B20 -- relocate  (Simple; Control System Test vs ONE trace IC in its location cycle)

Target = a single trace IC (spoof this turn, or suppress in place, `-1 DF`). Only eligible
during a trace's **locate** cycle.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B20.S | relocate | **trace IC** (locate cycle) | The trace IC is the target; also Probe IC, Tar Baby (util), NPC pass. | Spoof (no trace progress this turn) OR suppress (`suppressed`, `suppress_mode:"trace"`, `-1 DF`). DF-floor edge holds the suppress offer (`relocate_suppress_pending`). | Generic `system_test` success; `suppress_trace` flag selects mode. tally `+host_succ`. | `type:"relocate"` (spoof) / `type:"ic_suppressed"` (suppress) with the corresponding text; or the DF-floor held-offer variant. (+ generic action entry). | `renderRunState`/`renderSuppressions` (~L4526) show the paused/spoofed trace. | Eligible only for a trace in `trace_phase=="locate"`; single-target. |
| B20.F | relocate | trace IC | Same reactive. | No spoof/suppress; tally rises. | `net<0`/`0-succ`. | Generic action FAILED only. (If success but no eligible trace, a `type:"relocate"` "no trace IC ..." note.) | No change. | Retryable. |
| B20.T | relocate | trace IC | Same. | `k-vs-k,k>=1` WIN; `0-v-0` FAIL. | `net==0` rule. | As B20.S/B20.F. | As matching. | -- |

### B21 -- swap_memory  (Simple; NO test -- memory bookkeeping; EARLY RETURN)

Target = self (deck active/storage memory). `_apply_swap_memory` (load / reload).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B21.S | swap_memory | self (deck memory) | target=self; enemy axis N/A except reactive: **none** -- early return, no System Test, no `_autofire_lurking_tar`, no NPC pass driven here. | Loads a stored program into active memory (Mode 1), or reloads a crashed/degraded active program from storage (Mode 3). | No roll. Active-cap enforced (400 if overflow). tally unchanged. | `type:"swap_memory"` with the mode description (e.g. `"Swap Memory -- loaded X (rating r) into active memory."`). | `renderMemoryPanel` updates active/storage lists + ratings. | A Tar-Pit-wiped program cannot be reloaded (400). |
| B21.F | swap_memory | self | none | "No program to load or reload" OR 400 on active-memory overflow / wiped copy. | No roll. | `type:"swap_memory"` `"Swap Memory -- no program to load or reload."` (or HTTP 400). | No change. | -- |
| B21.T | swap_memory | self | none | **Tie: N/A -- unopposed.** No opposed roll; pure memory bookkeeping. | -- | -- | -- | -- |

### B22 -- unload_program  (Free; NO test -- push active program to storage; EARLY RETURN)

Target = self (free active memory). Reuses `_apply_swap_memory` Mode 2.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B22.S | unload_program | self (deck memory) | target=self; enemy axis N/A except reactive: **none** -- early return. | Pushes an active program to storage (keeps its storage copy), freeing active memory. | No roll. tally unchanged. | `type:"swap_memory"` `"Swap Memory -- moved X from active memory to storage."` | `renderMemoryPanel` moves the program to storage list. | Reload later via Swap Memory (B21). |
| B22.F | unload_program | self | none | Named program not active -> "no program to load or reload" no-op. | No roll. | `type:"swap_memory"` no-op text. | No change. | -- |
| B22.T | unload_program | self | none | **Tie: N/A -- unopposed.** No opposed roll; the action has no host contest. | -- | -- | -- | Free Action -- available even during a bg download. |

### B23 -- purge_hog  (Complex; Computer Test vs a Hog virus; EARLY RETURN)

Target = self (own deck's Hog infection). `hog_purge_test`. Success removes infection AND
crashes the infected program.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B23.S | purge_hog | self (Hog on own deck) | target=self; enemy axis N/A except reactive: **none** -- early return, no host System Test, no `_autofire_lurking_tar`, no NPC pass. | Removes the Hog (`hog_infections` filtered), crashes the infected program (`pd[name]=base`, reload via Swap Memory). | `eng.hog_purge_test(computer_skill, hog_rating, infected_program_rating, hardening)`; not opposed by host SV. tally unchanged. | `type:"purge_hog"` `"Purged Hog-R (TN t) -- virus removed; the <Program> program is wiped (reload via Swap Memory)."` | `renderMemoryPanel`/`renderRunState` remove the Hog badge; crashed program greyed. | Only purges viruses on the PC's OWN deck (`target_id=="pc"`). |
| B23.F | purge_hog | self | none | Purge fails; Hog persists. | `hog_purge_test` fail. tally unchanged. | `type:"purge_hog"` `"Purge FAILED (TN t) -- Hog-R persists."` | Hog badge stays. | Retryable. If no Hog: "No Hog virus to purge." |
| B23.T | purge_hog | self | none | **Tie: N/A -- unopposed.** No host `system_test`; it is a decker Computer Test vs the Hog's own TN. | -- | -- | -- | -- |

### B24 -- medic  (Complex; self-targeted heal; EARLY RETURN)

Target = self (persona/icon Condition Monitor). `_apply_medic`. Medic degrades `-1` per
use.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B24.S | medic | self (icon CM) | target=self; enemy axis N/A except reactive: **none** -- early return, no host System Test / Tar autofire / NPC pass. | Heals persona boxes = Medic Test successes (TN by current wound level); Medic wears `-1`. | Medic Test at effective Medic rating vs Light 4 / Mod 5 / Serious 6; capped by current damage. tally unchanged. | `type:"medic_heal"` `"Medic-R treats the <wound> icon wound (TN t): K successes -- H boxes healed. Icon damage now D/10. Medic worn to r..."` | `renderRunState` updates persona CM + Medic rating in `renderMemoryPanel`. | No-op event if icon undamaged or Medic worn out / not loaded. |
| B24.F | medic | self | none | "icon undamaged" / "Medic offline" -> no heal (0 successes still logs a heal of 0). | Medic Test may yield 0 successes. tally unchanged. | `type:"medic_heal", healed:0` with the relevant note. | No CM change. | -- |
| B24.T | medic | self | none | **Tie: N/A -- unopposed.** Self-heal, no host contest. | -- | -- | -- | -- |

### B25 -- restore  (Complex; self-targeted defensive; EARLY RETURN)

Target = self (temporary crippler reductions to persona attributes, BEMS). Does NOT
degrade; cannot touch permanent Persona-chip damage.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B25.S | restore | self (persona BEMS) | target=self; enemy axis N/A except reactive: **none** -- early return. | Repairs temporary crippler reductions to a chosen persona attribute (`_apply_restore`). | `_apply_restore(target=target_program)`; no host opposed roll. tally unchanged. | `_apply_restore` event describing the restored attribute. | `renderRunState` bumps the restored BEMS value back up. | Cannot restore permanent Persona-chip (Ripper) damage. |
| B25.F | restore | self | none | Nothing to restore -> no-op event. | No host roll. tally unchanged. | `_apply_restore` no-op text. | No change. | -- |
| B25.T | restore | self | none | **Tie: N/A -- unopposed.** Self-targeted, no host contest. | -- | -- | -- | Does not self-degrade. |

### B26 -- disinfect  (Complex; System Test vs the worm's subsystem; EARLY RETURN)

Target = a subsystem hosting a lurking Worm. Success DESTROYS the Worm with **no tally
add**; failure risks the Worm Infection Test vs MPCP.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B26.S | disinfect | subsystem hosting a **Worm** | The Worm is the target; enemy axis N/A except reactive: **Worm** itself (infection risk on failure). Early return -> no generic Tar-autofire / NPC pass / Probe loop. | Destroys the targeted Worm lurking-IC (`_apply_disinfect`). **No tally add** (a disinfect is not a crash). | Disinfect System Test (TN reduced by carried Disinfect utility) vs subsystem rating. | `_apply_disinfect` success event (Worm destroyed, no tally). | `renderRunState` removes the Worm marker. | TN reduced by the Disinfect utility. |
| B26.F | disinfect | subsystem (Worm) | **Worm** -> Worm Infection Test vs MPCP may infect (permanent chip status). | Worm survives; risks the Worm Infection Test. | Disinfect fail -> infection roll (host SV vs MPCP, `-hardening`). | `_apply_disinfect` failure event; possible `worm_resolved`/infection event. | `renderRunState` shows Worm + any MPCP infection. | Retryable. |
| B26.T | disinfect | subsystem (Worm) | Worm. | Resolved via `_apply_disinfect`'s own test, not the generic host `system_test`. If it internally uses `system_test`, the `net==0` rule applies (`k-vs-k,k>=1` WIN, `0-v-0` FAIL); otherwise **Tie: N/A -- unopposed**. | `net==0` rule for the internal disinfect test. | As B26.S/B26.F. | As matching. | Does not degrade Disinfect per use. |

### B27 -- defuse_data_bomb  (Complex; opposed System Test vs the bomb's subsystem; EARLY RETURN)

Target = an armed Data Bomb (Files bomb -> Files test, Slave bomb -> Slave test). Success
disarms with **no bomb-rating tally** (but the opposed host successes DO add). All-1s
botch detonates.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B27.S | defuse_data_bomb | **Data Bomb** (file/device) | The bomb is the target; enemy axis N/A except reactive: the bomb (botch detonation) via `_detonate_data_bomb`. Early return -> no generic Tar/Probe/NPC pipeline. | Disarms the bomb (`data_bombs` filtered, `defused_bombs` appended). **No bomb-rating tally**; opposed host successes still add. | `eng.data_bomb_defuse(pool, subsystem_rating, defuse_util)`; opposed host roll `SV vs DF` adds tally; win = `decker_succ >= host_succ AND decker_succ>0`. | `type:"data_bomb", outcome:"defused"` `"Data bomb on T DEFUSED (opposed Computer Test TN t = ...; D vs H). No bomb-rating tally -- no suppression needed.<tally note>"` | `renderRunState`/`renderDownloadsPanel` clear the bomb marker; access is now safe. | Detect first via Analyze Icon (B4). Defuse subsystem derived from the bomb's scope. |
| B27.F | defuse_data_bomb | Data Bomb | **Bomb detonates on all-1s botch** (`_detonate_data_bomb`); otherwise stays primed. | `outcome:"primed"` (retry) OR botch -> detonation ((Rating)M vs persona, +rating tally, suppress offer). | Botch = all-1s decker roll. Non-botch fail leaves bomb armed; opposed host successes add tally. | `type:"data_bomb", outcome:"primed"` `"Defuse FAILED ... stays primed..."` OR (botch) `type:"data_bomb", outcome:"detonated"` `"... detonated -- <level> damage; tally +N ..."` | `renderSuppressions` shows the post-detonation suppress offer; persona CM updates. | The opposed-tally risk applies on EVERY attempt. |
| B27.T | defuse_data_bomb | Data Bomb | As above. | Opposed defuse: `decker_succ >= host_succ AND decker_succ>0`. **Tie** `decker_succ==host_succ==k, k>=1` = **WIN** (defused); `0-v-0` = FAIL (primed). | `net==0`-analog rule. | As B27.S / B27.F(primed). | As matching. | -- |

### B28 -- scan_enemy_decker  (`POST /enemy-decker/scan` ~L8192; `scanEnemyDecker` ~L2618; Scan Icon, Simple)

Target = a revealed **enemy decker** icon. Computer Test vs target Masking (+Sleaze
-Scanner). **Adds NO security tally** (passive read).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B28.S | scan_enemy_decker | **enemy decker** | The enemy decker is the target; no host System Test -> no Probe/Tar/NPC pipeline in this endpoint. | Reveals `min(3+ => all)` of the enemy's hidden ratings in `_SCAN_REVEAL_ORDER` (MPCP -> BEMS -> Response Increase); `scan_reveal` advances. | `roll_dice(computer_skill+HP, max(2, masking + (sleaze-scanner if sleaze>0 else 0) + wound))`. 3+ successes = full read. **No tally.** | `type:"icon_scanned", success:True` `"Scan Icon on <name>: MPCP r, Bod b ... -- icon fully scanned."` | `renderRunState` fills the enemy icon's stat card; `scanEnemyDecker` UI updates. | Target must be an active, **revealed** enemy decker (else 404). Simple action. |
| B28.F | scan_enemy_decker | enemy decker | Same. | No new ratings (0 successes / already full). | 0 successes or already max. No tally. | `type:"icon_scanned", success:False` `"Scan Icon on <name> reveals nothing new (no successes)."` | No card change. | Retryable. |
| B28.T | scan_enemy_decker | enemy decker | Same. | **Tie: N/A -- unopposed.** Not a host opposed `system_test`; it is a decker Computer Test vs a fixed TN (target Masking). Outcome is successes>=1 (reveal) vs 0 (nothing). | -- | -- | -- | Doubles as Analyze Icon for a hostile decker. |

### B29 -- graceful_logoff  (`POST /logoff` ~L6736; `submitLogoff` ~L4998; Access Test, Complex)

Target = host (Access). Also reachable as the `graceful_logoff` action_type (early-return
in `perform_action`). Success ends the run (traces cleared, no dump shock).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B29.S | graceful_logoff | host / access | target=host; enemy axis N/A except reactive: an active **Trace IC** raises the logoff TN by its rating (max). No post-test NPC pipeline (early return / dedicated endpoint). | Ends the run cleanly: `run_ended`, `end_reason:"graceful_logoff"`, traces cleared, passcode deleted, decoy cleared, `run.status="escaped"`. | `system_test(pool=computer_skill+HP, access, SV, DF, mod=-deception+trace_bonus)`; `console_access` halves SV. tally `+host_succ`. | `type:"logoff_success"` `"Graceful logoff successful. All traces cleared. Run complete."` | `renderStage` shows run complete; `renderRunState` disables ops. | Mid-transfer download is corrupted on success (`_corrupt_active_download`). |
| B29.F | graceful_logoff | host / access | Trace IC raises TN; tally rose (sheaf may wake IC). | Still logged on; tally rises; retry or jack out (dump shock). | `net<0`/`0-succ`. tally `+host_succ`. | `type:"logoff_fail"` `"Graceful logoff FAILED. Tally +N -> T. Still logged on -- try again or jack out (dump shock)."` | `renderAlertBadge` updates; still on host. | Retryable. |
| B29.T | graceful_logoff | host / access | Same. | `k-vs-k,k>=1` WIN escape; `0-v-0` FAIL. | `net==0` rule. | As B29.S/B29.F. | As matching. | -- |

### B30 -- jack_out  (`POST /jack-out` ~L8579; `doJackOut` ~L4497)

Target = self (emergency disconnect). Free before a Black IC hit; after one, a Complex
Willpower (Black IC Rating) Test.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B30.S | jack_out | self | target=self; enemy axis N/A except reactive: **Black IC** -- after a hit it lands one FINAL attack as you tear free (`_black_ic_final_attack`). | Disconnects; dump shock applied (`_apply_dump_shock`). Before a Black hit: instant Free disconnect. After: WP Test succeeded, then Black IC final strike. | Pre-Black: no test (Free). Post-Black: `roll_dice(willpower, max(2, black_rating - (2 if iccm)))`, success = `>0`. | `type:"jack_out"` (WP text) + dump-shock event; possibly Black IC final `ic_attack` + MPCP hit. | `renderStage` ends the run (dumped); persona/meat CM updated. | ICCM lowers TN by 2. |
| B30.F | jack_out | self | **Black IC** (blocks). | Only possible post-Black: WP Test failed -> still jacked in, Complex action spent. | `roll_dice(willpower, tn)` = 0 successes. | `type:"jack_out_failed"` `"Jack-out BLOCKED by Black IC R -- Willpower Test (TN t) failed (K successes). Still jacked in."` | Run continues; `renderActionArea` still shows only jack-out. | Retry next action. |
| B30.T | jack_out | self | Black IC. | **Tie: N/A -- unopposed.** The WP gate is decker-vs-fixed-TN (Black IC Rating), not an opposed host `system_test`; outcome is successes>=1 (free) vs 0 (blocked). | -- | -- | -- | Pre-Black jack-out has no roll at all. |

### B31 -- new_turn  (`POST /new-turn` ~L6997; `doEndTurn` ~L4486)

Target = turn/pass advance. Flushes pending suppressions, drives NPC passes, resolves
lurking Worms, ticks downloads/countdowns.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B31.S | new_turn | turn/pass state | ALL app-controlled hostiles act here: proactive/trace **IC**, **enemy deckers**/**constructs** (`_advance_npc_pass`); lurking **Worms** resolve (`_resolve_lurking_worm`); crash/shutdown countdowns tick. | Ends the current pass (hostiles on it act, budget+HP refresh) OR ends the Combat Turn (remaining hostile passes flush, next turn begins; pass count re-derived from wounds). | No decker roll of its own; drives the NPC/worm/countdown rolls. Pending suppressions auto-accepted (`_flush_pending_suppressions`). | Many events from the NPC pass, worm resolution, download ticks, countdown; run may end (`run.status = end_reason`). | `renderRunState`/`renderEventLog` refresh; `renderCrashCountdown`, `renderDownloadsPanel`, `renderSuppressions` all update. | Blocked if `run_ended`. A bg download running when the run ends is corrupted. |
| B31.F | new_turn | turn/pass state | Same hostiles -- a hostile on the leaving pass can kill the decker. | Run ends this turn (decker dumped/crashed) -> `run.status = end_reason`. | Hostile attacks resolve; download corrupted if active at end. | Kill/dump events from `_advance_npc_pass`. | `renderStage` shows the run over. | "Failure" = the turn advance kills the decker. |
| B31.T | new_turn | turn/pass state | Same. | **Tie: N/A -- unopposed.** `new_turn` makes no opposed decker System Test; it only sequences hostile actions. | -- | -- | -- | -- |

### B32 -- suppress_ic  (`POST /suppress` ~L8447)

Target = a crashed/hung IC or a non-IC suppression entry (data bomb). Toggle suppress /
release. No test, no action cost.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B32.S | suppress_ic (suppress) | a crashed/hung IC or data-bomb entry | target=IC/self; enemy axis N/A except reactive: **none** -- no host System Test, no NPC pass. | Suppress: absorb 1 Detection Factor to REFUND the crash/bomb rating tally (`_toggle_ic_suppression`). | No roll. DF `-1` (min 1). tally refunded by the entry's rating. | Suppression event (from `_toggle_ic_suppression`). | `renderSuppressions` (~L4526) updates the entry; DF/tally badges change. | Neither suppress nor release costs an action. |
| B32.F | suppress_ic (release) | a suppressed entry | none | Release: restore DF, re-add a crashed IC's / bomb's rating to the tally (a hung IC re-adds nothing). Released item can NEVER be re-suppressed. | No roll. DF `+1`; tally re-added. | Suppression release event. | `renderSuppressions` marks the entry released (locked). | DF cannot fall below 1. |
| B32.T | suppress_ic | entry | none | **Tie: N/A -- unopposed.** Pure toggle; no opposed roll. | -- | -- | -- | -- |

### B33 -- reveal_host_ratings  (`POST /reveal-host-ratings` ~L8478)

Target = self-knowledge (spend banked Analyze Host credits). No test. Phase two of B2.

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B33.S | reveal_host_ratings | host / self-knowledge | target=host-knowledge; enemy axis N/A except reactive: **none** -- no System Test, no NPC pass. | Reveals the chosen still-hidden ACIFS ratings and/or Security Rating from banked credits (`_reveal_host_ratings`). | No roll. Must pick exactly `min(credits, hidden_count)` valid, non-dup, currently-hidden items (else 400). | `type:"host_analyzed"` `"Analyze Host -- <Subsystem> <rating>, ... revealed."` | `renderHostRatings` fills the chosen ratings; picker closes. | Requires banked `host_analyze_pending` (from B2). Security reveal mirrors to org LTG. |
| B33.F | reveal_host_ratings | host | none | 400 -- no pending credits, wrong count, unknown/already-revealed/duplicate pick. No state change. | No roll. | HTTP 400, no event. | Picker shows validation error. | -- |
| B33.T | reveal_host_ratings | host | none | **Tie: N/A -- unopposed.** No opposed roll; deterministic reveal. | -- | -- | -- | -- |

### B34 -- trap_door_action  (`POST /trap-door/{td_id}` ~L6769; `enterTrapDoor`/`fileTrapDoor` ~L2911)

Target = a discovered trap door. `action="file"` (record) or `action="enter"` (Graceful
Logoff through the concealing subsystem, then a fresh run on the destination host).

| ID | Action | Target | Provoked opponent | Outcome | Roll / mechanic | Event log entry | UI / DOM effect | Preconditions / notes |
|----|--------|--------|-------------------|---------|-----------------|-----------------|-----------------|-----------------------|
| B34.S | trap_door_action | trap door / host transit | target=host; enemy axis N/A except reactive: an active **Trace IC** raises the transit logoff TN (via `_apply_graceful_logoff`). | FILE: `door["filed"]=True` (no roll, always succeeds). ENTER: graceful-logoff succeeds -> `run.status="escaped"`, `end_reason:"trap_door_transit"`, then a NEW linked run on the destination host is created and returned. | FILE: no roll. ENTER: `_apply_graceful_logoff(pool, deception)` Access Test (same `net==0` rule as B29). | FILE: `type:"trap_door_filed"`. ENTER success: `type:"trap_door_entered"` `"Entered trap door -- arrived at host \"X\". Logon to continue."` | `renderTrapDoorsPanel` (~L2478) marks filed; ENTER swaps to the new host run and `renderStage` resets to logon. | Door must be `discovered` (Analyze Subsystem, B6). ENTER needs a linked `destination_host_id` (else 400). |
| B34.F | trap_door_action | trap door | Trace IC raised the TN; tally rose. | ENTER: graceful-logoff FAILED -> transit aborted, still on the current host. (FILE never fails.) | `_apply_graceful_logoff` fail (`net<0`/`0-succ`); tally `+host_succ`. | `type:"logoff_fail"` (from the shared logoff helper); no `trap_door_entered`. | Stays on current host; `renderAlertBadge` updates. | Retry the transit. |
| B34.T | trap_door_action | trap door | Same. | ENTER: `k-vs-k,k>=1` WIN transit; `0-v-0` FAIL. FILE: unopposed (always succeeds). | `net==0` rule for the ENTER logoff. | As B34.S/B34.F. | As matching. | -- |

---

### Summary

- **ID range used: B1..B34** (each with `.S` / `.F` / `.T` rows = 102 outcome rows).
- **Opposed `system_test` actions** (net/tie rule applies): B1, B2, B3, B4, B5, B6, B7,
  B8, B9, B10, B11, B14, B15, B16, B17, B18, B19, B20, B29, and the ENTER path of B34
  (via `_apply_graceful_logoff`).
- **Unopposed / non-`system_test` actions** (`.T` = N/A -- unopposed): B12 (own decrypt
  primitive), B13, B21, B22, B23 (own Hog purge primitive), B24, B25, B28 (Computer Test
  vs fixed TN), B30 (WP gate), B31, B32, B33, and the FILE path of B34. B26/B27 use their
  own internal test helpers (B26 disinfect; B27 opposed defuse with a tie-to-decker rule).
- **Reactive opponents that a Section-B action can wake:** Probe IC (any System Test),
  Tar Baby / Tar Pit (any `utility_rating>0` op via `_autofire_lurking_tar`), Data Bomb
  (successful `download_data`/`edit_file`, botched/failed defuse, Exploding Scramble on a
  failed `decrypt_file`), Trace IC (raises logoff/transit TN; drives its own cycle in
  `_advance_npc_pass`), Worm (resolves in `new_turn`), and enemy deckers / constructs
  (act in `_advance_npc_pass` after any generic action; spawn-held one pass).
- **Early-return actions** that SKIP the generic post-test pipeline (no Tar autofire /
  Probe loop / NPC pass from within the handler): graceful_logoff, swap_memory,
  unload_program, medic, restore, disinfect, defuse_data_bomb, steamroller, slow,
  decompress_file, dinab, purge_hog, decrypt_file (plus the dedicated endpoints).

---

<a id="sec-c"></a>

## Section C &mdash; Enemy / Opponent Actions vs the PC

Static analysis of `app/routers/matrix_runs.py`, `app/services/matrix_engine.py`, and
`frontend/matrix-run.html`. Every action here is something an **enemy/opponent takes AGAINST the
PC** (the app plays the GM in `_advance_npc_pass` / `_enemy_decker_take_pass`). No server was run.

### Legend

- **ID scheme:** `C<n>.<O>` where `<n>` increments per (enemy action, opponent-type) pair and
  `<O>` is the outcome: `.S` = enemy SUCCEEDS against the PC, `.F` = enemy WHIFFS, `.T` = TIE.
- **Opponent types:** `IC` (enemy Intrusion Countermeasures -- lists acting subtypes), `DECKER`
  (enemy security decker AI), `CONSTRUCT` (`active_ic` `type="Construct"`), `PARTY-IC` (a cluster
  of `active_ic` sharing `cluster_id`).
- **TIE semantics (user-confirmed):** a tie is the opposed `net == 0` per that engine's specific
  rule; the rule is stated in the mechanic column of every `.T` row. When the enemy action is
  **unopposed** (the PC makes no counter-roll), the `.T` row reads *"N/A -- unopposed"* with an
  explanation.
- **Core mechanics referenced:**
  - `roll_dice(pool, tn)` (engine ~L29): rule-of-6 -- a die showing 6 re-rolls and adds ONLY when
    `tn > 6`; ones counted from the initial roll. **Every** roll below uses this.
  - `damage_resistance` (~L144): effective Power = `max(1, power - armor)`; Shield net successes
    cancel attacker successes 1:1 BEFORE staging; net-successes-first single staging by
    `(net_attacker - resist_successes)//2`; box tables `DAMAGE_BOXES` (meat 1/3/6/10) vs
    `ICON_DAMAGE_BOXES` (icon 1/2/3/6); wound mods `+1 TN / -1 init` at 1/3/6 filled boxes.
  - `attribute_attack_core` (~L817): `net = max(0, atk - resist - shield)`, `reduction = net//2`.
  - `maneuver_test` (~L1414): maneuvering must roll STRICTLY more; `net>0` required (ties fail).
  - `tar_baby_test` (~L891): a tie goes to the IC IF `ic_succ >= 1`, else a mutual whiff.
- **Event writer:** `_append_event` (~L748). **`gm_only: True`** events are redacted server-side
  for non-admins (`_serialize_run` / `_GM_ONLY_STATE_KEYS`); tally numbers stripped by
  `_redact_event_tally`.
- **UI surfacing (frontend/matrix-run.html):** `renderRunState` (~L2999) orchestrates;
  `renderEventLog` (~L3368) -> `renderEventEntry` (~L3380) per entry; `renderStage` (~L3818);
  `renderConditionBoxes` (~L3155) draws the PC persona/stun/physical monitors;
  `renderActiveIC` (~L3216); `renderEnemyDeckers` (~L2521); `renderAlertBadge` (~L3168);
  `renderSuppressions` (~L4526).

---

### Opponent type: ENEMY IC

Acting subtypes (driver `_advance_npc_pass` ~L4764, ordered by `initiative`): **Probe** (tests per
System Test, run by the caller ~L6204), **Trace** (hunt/locate cycle), **Killer / Blaster / Sparky**
(standard proactive cybercombat), **Black IC** (black strike), **Acid / Binder / Marker / Jammer**
(cripplers), the `-rip` **Rippers**, reactive **Tar Baby / Tar Pit** (`_resolve_lurking_tar`),
**Worm** (`_resolve_lurking_worm`), **Data Bomb** (`_detonate_data_bomb`), **Scramble** (Poison
variant, decrypt branch). Constructs and party-IC clusters are separate sections below.

#### C1 -- Probe IC test  (`eng.probe_test` ~L787; applied ~L6204)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C1.S | Probe examines data trail | IC (Probe) | Success | `roll_dice(ic_rating, det_factor)`; `tally_increase = successes`; then `_bump_security_tally`. Runs per PC System Test, once per pre-existing Probe. | `probe_ic` -- text scales with the GM secret Sensor Test level (`_secret_sensor_test`): L0 "Something is examining your data trail. Tally +X"; L3 "Probe-R IC is examining your data trail and reporting to host security." | `renderEventEntry` shows the probe line (tally clause redacted for non-admins); higher tally may cross a sheaf step -> `renderActiveIC` new IC; `renderAlertBadge` if status escalates. | Only Probe IC in `_preexisting_ic_ids` test the action that spawned them; suppressed Probes skip. |
| C1.F | Probe finds nothing | IC (Probe) | Failure | Same roll, `successes == 0` -> `tally_increase 0`; no `_bump_security_tally`. | No `probe_ic` event appended (guarded by `probe["tally_increase"] > 0`); a secret Sensor Test may still emit `ic_detected`. | Nothing new in event log for this Probe; PC monitors unchanged. | Probe stays invisible unless a Sensor Test raises `detection_level`. |
| C1.T | Probe tie | IC (Probe) | Tie: N/A -- unopposed | The PC makes no opposing roll; the Probe rolls vs the PC's Detection Factor (a static value, not a live PC roll). Outcome is binary success/no-success on `successes`. | -- | -- | Detection Factor derives from PC Masking; the PC never "rolls against" the Probe here. |

#### C2 -- Trace IC hunt cycle  (`eng.trace_hunt_cycle_attack` ~L801; branch ~L4830)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C2.S | Trace HUNT hit -> start location cycle | IC (Trace) | Success | `roll_dice(sec_value, trace_tn)` (`_compute_trace_tn`); `hit = successes > 0`. On hit: `locate_turns = max(1, 10 // successes)`, `trace_phase -> "locate"`. | `ic_attack` (`trace_phase: hunt_hit`) -- "Trace-R HUNT CYCLE HIT (N success(es)) -- Location Cycle: T turn(s) to trace." | `renderActiveIC` shows the trace IC entering its location countdown; event line in `renderEventLog`. | Trace acts every pass on its initiative; does NOT do cybercombat. `trace_tn` shrinks with live bandwidth. |
| C2.F | Trace hunt miss | IC (Trace) | Failure | Same roll, `successes == 0` -> `hit False`; stays in `hunt` phase. | `ic_attack` (`trace_phase: hunting`) -- "Trace-R hunt cycle: searching... (0 hits vs TN K)". | Event line only; no countdown started. | Repeats next pass until a hit. |
| C2.T | Trace hunt tie | IC (Trace) | Tie: N/A -- unopposed | The PC makes no opposing roll during the hunt; the trace rolls Security Value vs a computed Trace Factor TN. Result is hit/no-hit on successes. | -- | -- | The PC influences it only indirectly (Relocate/Redirect spoof raises the TN); no simultaneous PC roll to tie against. |

#### C3 -- Trace location cycle completion (jackpoint traced)  (branch ~L4830, `phase == "locate"`)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C3.S | Location cycle completes -> jackpoint traced | IC (Trace) | Success | Countdown: `trace_locate_remaining -= 1`; at `<= 0` -> `trace_phase="triggered"`, `traces_completed += 1`. Mechanical effect: all proactive IC hit at **-1 TN** and every later tally increase **+1** (`_completed_trace_count`). Fires `_spawn_trap_hidden`. | `ic_attack` (`trace_action: report`) -- "Trace: Jackpoint TRACED -- physical location reported... Proactive IC now hit at -1 TN; every further tally increase +1." (or the `physical_trace_immune` satellite variant). | `renderActiveIC` marks the trace `triggered`/dormant; subsequent enemy attacks show the -1 TN; a Trap Trace may reveal in `renderActiveIC`. | A spoofed-this-turn trace makes no progress (`trace_spoofed_turn`). |
| C3.F | Location cycle still counting | IC (Trace) | Failure | `remaining > 0` after decrement. | `ic_attack` (`trace_phase: locating`) -- "Trace-R location cycle: N turn(s) to trace completion." | Countdown line in event log; `renderActiveIC` shows remaining turns. | The PC can still spoof/crash the trace before completion. |
| C3.T | Trace completion tie | IC (Trace) | Tie: N/A -- unopposed | Completion is a deterministic COUNTDOWN, not a roll (the hunt hit already set `locate_turns`). No dice, no PC counter-roll. | -- | -- | The only PC lever is a Relocate spoof (skips one tick) -- still not an opposed roll. |

#### C4 -- Proactive cybercombat attack (Killer / Blaster / Sparky)  (`eng.cybercombat_attack` ~L261; branch ~L5058)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C4.S | IC hits PC icon | IC (Killer/Blaster/Sparky) | Success | `attack_roll = roll_dice(sec_value +expert +cascade, COMBAT_TN[sec][status] + cluster + parry - traces + wound_mod)`; `damage_resistance(bod=eff.bod, power=ic_rating(+cascade+position), armor, shield_succ)`; `boxes>0` fills persona. On persona 10: `persona_crash`; Blaster/Sparky add `_roll_mpcp_damage` (Sparky +2 TN + Body-resisted physical), then `_apply_dump_shock`, `run_ended`. | `ic_attack` -- "Killer-R attacks: A attack successes vs Rz resist. Damage: LEVEL (N boxes). Persona: P/10". Plus `persona_crash` / `dump_shock` on a crash; hot deck may add `simsense_overload`. | `renderConditionBoxes('persona'...)` fills; `renderActiveIC` shows the IC; `renderStage` redraws; on crash `renderRunState` locks actions to jack-out, `renderAlertBadge`. | `_shield_parry` (Computer/SV) subtracts successes; armor worn via `_wear_armor`; `_apply_cascade_outcome` on hit/full-resist. |
| C4.F | IC misses / fully resisted | IC (Killer/Blaster/Sparky) | Failure | `attack_roll successes == 0` (miss) OR staged down to `None` (`boxes == 0`) after resist. `_apply_cascade_outcome(hit=False)` raises the IC's attack SV; a fully-resisted hit raises its rating. | `ic_attack` -- same template with `N boxes = 0` and no crash follow-up. | `renderConditionBoxes` unchanged; `renderActiveIC` may show a cascaded higher rating next pass. | No dump shock, no MPCP burn. |
| C4.T | Attack successes == resist successes | IC (Killer/Blaster/Sparky) | Tie | Tie rule: `net_attacker - resist_successes == 0` -> single staging step is 0, so damage lands at the **base level** (a graze). Boxes = `ICON_DAMAGE_BOXES[base]` (>=1 unless base is None). The enemy still deals base-level damage on a tie. | `ic_attack` -- damage `LEVEL` equals the unstaged base (e.g. Moderate) with its box count. | Persona monitor fills by the base box count; same panels as C4.S but no staging up. | For cybercombat there is no "no-hit tie" -- equal successes = base damage lands; only 0 attack successes or a down-stage to None is a true whiff. |

#### C5 -- Black IC strike  (`eng.black_attack` ~L315; black branch ~L4968)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-----------------|-----------------|------------------------|
| C5.S | Black IC hits icon + operator | IC (Black IC) | Success | ONE `attack_roll` drives BOTH resists off the same successes: icon `bod` vs `power(rating+position+deathworm)-hardening` (armor protects); meat `body`(hot->Physical) / `willpower`(cool->Stun) vs same power (armor does NOT protect). Persona fills; meat fills Physical (lethal) or Stun (cool). Meat 10 -> `persona_crash` + 2x-rating MPCP burn + `run_ended` (`black_ic_lethal`/`_unconscious`). Icon 10 before meat -> `icon_crashed`, connection holds, IC rating +2. | `ic_attack` -- "Black IC (lethal) R: A atk successes. Body resist: L (N phys). Bod resist: L (M persona). Physical: x/10 Persona: y/10". Plus `persona_crash` (+MPCP) on death, or `persona_crash` "ICON CRASHED... connection holds... rating +2". | `renderConditionBoxes` for persona AND physical/stun; `renderStage`; `renderAlertBadge`; on death `renderRunState` ends run; the jack-out control gates behind Willpower(rating). | First successful Black IC hit sets `black_ic_engaged=True` -> jacking out becomes Complex + Willpower(Black IC rating) test (~L4990). Tortoise deck: Black IC degrades to icon-only C4 path. |
| C5.F | Black IC misses / fully resisted | IC (Black IC) | Failure | `attack_roll successes == 0` (miss) or both resists stage to None (0 boxes each). Note: a `successes>0` miss on damage still sets `black_ic_engaged` (a "hit" = successful Attack Test regardless of boxes). | `ic_attack` -- same template, 0/0 boxes; no crash. | Monitors unchanged; but the jack-out gate flag may now be set (control changes to Complex). | Distinguish: 0 attack successes = no engage; >0 successes but 0 boxes = engaged but no damage. |
| C5.T | Black IC tie | IC (Black IC) | Tie | Tie rule: for each resist, `net_attacker - resist_successes == 0` -> base-level (`IC_DAMAGE_LEVEL[sec]`) lands on that monitor (icon and/or meat) with no staging. Base-level biofeedback still applies. | `ic_attack` -- base level on both icon and meat lines. | Persona + physical/stun fill by base box counts; same panels as C5.S. | As with C4, equal successes deal base damage; only 0 successes / down-stage to None is a whiff. |

#### C6 -- Crippler IC attribute attack (Acid / Binder / Marker / Jammer)  (`_resolve_attribute_attack` ~L2179 -> `eng.crippler_attack` -> `attribute_attack_core` ~L817; branch ~L4930)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C6.S | Crippler reduces a PC BEMS attribute | IC (Acid/Binder/Marker/Jammer) | Success | `attack = roll_dice(sec_value, COMBAT_TN[sec][status] + parry + wound - traces)`; `resist = roll_dice(target_attr, ic_rating)`; `+shield` to resist; `net = max(0, atk - resist - shield)`, `reduction = net//2`. `applied = min(reduction, attr-1)` written to `condition_monitor.persona_damage[attr]` (floored at 1); `_record_crippler_rating` (Restore TN). Acid->Bod, Binder->Evasion, Marker->Masking, Jammer->Sensor (`_CRIPPLER_TARGET`). | `ic_attack` -- "Acid-R vs BOD: A atk / D def -> BOD -X." | `renderConditionBoxes` unaffected (this is attribute, not boxes), but `renderStage`/effective-attr readouts drop; the Detection Factor recomputes if Masking hit; Restore action becomes available. | Damage lasts until logoff (temporary); base attribute never mutated -- reduction lives in `persona_damage`. |
| C6.F | Crippler resisted | IC (crippler) | Failure | `atk successes == 0` (miss) OR `atk - resist - shield <= 0` -> `net 0`, `reduction 0`, `applied 0`. | `ic_attack` -- "...A atk / D def -> BOD -0." (no attribute change). | No stat change; event line only. | A `net == 1` also yields `reduction 0` (needs 2 net for 1 point). |
| C6.T | net == 0 (atk == resist + shield) | IC (crippler) | Tie | Tie rule: opposed `net = atk - resist - shield == 0` -> `reduction 0`, no attribute loss. A crippler tie is a whiff (indistinguishable in effect from a resisted failure). | `ic_attack` -- "BOD -0". | No change. | Per `attribute_attack_core` ties fail (needs strict net; and >=2 net for any point). |

#### C7 -- Ripper IC attribute + permanent chip attack  (`crippler_attack(is_ripper=True)`; branch ~L4930)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C7.S | Ripper reduces attribute + burns persona chip | IC (Ripper `-rip`) | Success | As C6 for the temp reduction; THEN on `net > 0` and `mpcp>0`: `ripper_roll = roll_dice(ic_rating, mpcp + hardening)`; `chip_damage = successes` added to `persona_chip_damage[attr]` (PERMANENT, Restore-proof floor). | `ic_attack` -- "...BOD -X. Ripper chip: BOD -C more (permanent)." | Same as C6 plus a permanent floor: Restore can never repair below `persona_chip_damage`; effective-attr readout drops further. | Chip capped at `room - applied`; permanent until a new MPCP chip. |
| C7.F | Ripper resisted | IC (Ripper) | Failure | `net == 0` -> no temp reduction AND no ripper roll (`net > 0` gate not met). | `ic_attack` -- "BOD -0." | No change. | The chip rider only fires when the base crippler landed damage. |
| C7.T | net == 0 | IC (Ripper) | Tie | Tie rule: `net = atk - resist - shield == 0` -> no reduction, ripper rider skipped. Whiff. | `ic_attack` -- "BOD -0." | No change. | Same tie rule as C6. |

#### C8 -- Tar Baby / Tar Pit reaction  (`_resolve_lurking_tar` ~L7346 -> `eng.tar_baby_test` ~L891)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C8.S | Tar crashes the utility the PC just ran | IC (Tar Baby/Tar Pit) | Success | `ic_roll = roll_dice(ic_rating, utility_rating)`, `util_roll = roll_dice(utility_rating, ic_rating)`; `ic_wins = ic_succ >= util_succ AND ic_succ > 0`. On win: utility AND the tar both crash (removed from `lurking_ic`); Tar Pit additionally rolls MPCP -> `all_copies_corrupted` -> `_wipe_all_copies`; else `_wipe_one_shot`. | `reactive_ic_resolved` (`outcome: ic_wins`) -- "Tar Baby-R triggered vs Attack-U. IC wins -- Attack and Tar Baby both crash." (+`tar_pit_corruption`). | `renderActiveIC` removes the lurking tar; the PC's utility roster shows the crashed/wiped program (reload via Swap Memory unless Tar Pit corrupted all copies). | Fires automatically on utility use (`_autofire_lurking_tar`), gated `utility_rating > 0`. |
| C8.F | Utility survives the tar | IC (Tar Baby/Tar Pit) | Failure | `ic_succ < util_succ` -> `ic_wins False`; tar stays lurking. | `reactive_ic_resolved` (`outcome: util_wins`) -- "...Utility wins -- Tar Baby remains lurking." | `renderActiveIC` keeps the lurking tar marker; utility intact. | Will trigger again on the next utility use. |
| C8.T | ic_succ == util_succ | IC (Tar Baby/Tar Pit) | Tie | Tie rule (`tar_baby_test`): a tie goes to the IC **if `ic_succ >= 1`** (`ic_wins` True -> both crash, = C8.S). A `0 == 0` tie is a **mutual whiff** (`ic_wins False`, = C8.F -- tar stays lurking). | The 0-0 tie logs the `util_wins` branch; a >=1 tie logs `ic_wins`. | Follows whichever branch the tie resolves to. | This is the explicit split-tie action. |

#### C9 -- Worm infection of the MPCP  (`_resolve_lurking_worm` ~L7201 -> `eng.worm_attack`)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C9.S | Worm infects MPCP (permanent) | IC (Worm / Deathworm / Tapeworm) | Success | `roll = roll_dice(host_security_value, mpcp_rating)`; `net = successes - hardening`; `infected = net > 0`. Sets `mpcp_infected`, `chip_replacement_required`, appends to `mpcp_infections` (variant-keyed); worm removed. Deathworm -> ongoing cybercombat TN +2; Tapeworm -> paydata erasure at run end. | `worm_resolved` (`outcome: mpcp_infected`) -- "Deathworm-R infected the MPCP -- chip replacement required (permanent). ... Infection Test: host Nd6 vs MPCP TN M, net K after Hardening-H." | `renderEventEntry` shows the infection; persistent deck status carries across runs; later cybercombat shows the Deathworm TN penalty (`_deathworm_tn_bonus`). | No security tally (worm has no IC rating). Fires each Combat Turn in `new_turn`. |
| C9.F | Worm repelled | IC (Worm) | Failure | `net <= 0` (`successes <= hardening`) -> `infected False`; worm stays lurking. | `worm_resolved` (`outcome: repelled`) -- "Worm-R infection repelled (host Nd6 vs MPCP TN M, net K after Hardening-H). Worm still lurking." | Event line; lurking worm marker persists. | Retries next Combat Turn. |
| C9.T | net == 0 (successes == hardening) | IC (Worm) | Tie: `net == 0` -> repelled | Tie rule: `net = successes - hardening`; a tie is `net == 0` (worm successes exactly equal Hardening). Since `infected = net > 0`, a tie is a **failure** (repelled). The PC does not roll -- Hardening acts as the static defence, so "opposed" here is worm successes vs Hardening. | Logs the `repelled` branch. | Same as C9.F. | Semi-opposed: no live PC roll, Hardening is the threshold; tie == fail. |

#### C10 -- Data Bomb detonation  (`_trigger_access_data_bomb` ~L3976 / `_detonate_data_bomb` ~L3586)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C10.S | Bomb detonates on PC persona | IC (Data Bomb) | Success | Fixed `(rating)M`: `data_bomb_detonate` -> `damage_resistance(bod, power=rating, armor, attacker_successes=0)` (Bod resists, armor cuts Power); Shield net successes stage the resolved level DOWN. Adds `rating` to security tally (`_bump_security_tally`) then `_check_and_activate_sheaf`; registers a suppression the PC may refund with 1 Detection Factor. | `data_bomb` (`outcome: detonated`) -- "DATA BOMB on <target> detonated -- LEVEL damage; tally +X -> T. You may spend 1 Detection Factor to suppress the IC and refund this tally." | `renderConditionBoxes('persona')` fills; `renderSuppressions` shows the refundable suppression entry; higher tally may spawn IC (`renderActiveIC`) / `renderAlertBadge`. | Triggered by a SUCCESSFUL Download/Edit access of an undefused bomb target; one-shot (bomb removed). Also fired by an all-1s botched defuse and an Exploding Scramble. |
| C10.F | Bomb inert / not triggered | IC (Data Bomb) | Failure | A FAILED access does not trigger (`test_success` False); a defused bomb (`defused_bombs`) is inert; a Bod resist staging the fixed Moderate down to None yields 0 boxes. | On a non-trigger: no `data_bomb` detonated event. On a 0-box resist: `data_bomb` detonated with `LEVEL = None`/0 boxes but tally still +rating. | If not triggered, nothing; if resisted to 0, persona unchanged but suppression/tally still logged. | The tally increase applies whenever it actually detonates, regardless of boxes. |
| C10.T | Data bomb tie | IC (Data Bomb) | Tie: N/A -- unopposed to-hit | The bomb's to-hit is **automatic** (`attacker_successes = 0`, fixed `(rating)M`) -- there is no attacker roll for the PC to tie against. The only variable is the PC's own Bod/Shield resistance (a solo defence roll, not an opposed contest). | -- | -- | Damage staging comes entirely from the defender's resist + Shield down-stage; no opposed net exists. |

#### C11 -- Scramble failure consequence (Poison Scramble)  (`eng.scramble_failure_consequence`; decrypt branch ~L5634)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C11.S | Poison Scramble destroys protected data | IC (Scramble, Poison variant) | Success | Triggered by a FAILED `scramble_decrypt_test`. Poison variant: `poison_roll = roll_dice(scramble_rating, max(2, decker_computer_skill))`; `data_destroyed = successes > 0`. Key data -> permanent mission loss (`protected["destroyed"]=True`, `key_data_lost`). Exploding variant instead fires `_detonate_data_bomb` (see C10). | `decrypt` (`success: False`, `data_destroyed`/`key_data_lost`) -- "KEY DATA DESTROYED -- the Poison Scramble's test succeeded (IC Rd6 vs TN = your Computer skill) and wiped the protected file." | `renderEventEntry` flags the loss; `file_name` lets the UI grey the destroyed file in the paydata list. | The Scramble's Poison Test fires ONLY after a failed decrypt; a successful decrypt removes the scramble with no tally (C-not-here). |
| C11.F | Poison test misses -- data safe | IC (Scramble) | Failure | Failed decrypt but `poison_roll successes == 0` -> `data_destroyed False`; data survives. Standard-variant scramble: no destruction at all. | `decrypt` (`success: False`, `data_destroyed: False`) -- "Decrypt failed, but the Poison Scramble's test missed (IC Rd6 vs TN P) -- the protected data survives. Try the decrypt again." | Event line; file intact in paydata list. | Decrypt adds NO security tally regardless (vr2 L495). |
| C11.T | Scramble poison tie | IC (Scramble) | Tie: N/A -- unopposed | The Poison Test is the IC rolling its rating vs a static TN (the decker's Computer skill value) -- the PC makes no counter-roll here (the PC's failed decrypt is a separate prior test). Result is binary on IC successes. | -- | -- | The decker's Computer skill sets the TN but is not a live opposing roll at this step. |

#### C12 -- IC combat maneuver vs the PC  (`_npc_maybe_maneuver` ~L4373 / `_resolve_npc_maneuver` ~L4290 -> `eng.maneuver_test` ~L1414)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C12.S | IC wins Evade / Parry / Position vs PC | IC (any attacking subtype) | Success | IC maneuvering = Security Value dice, rating = IC rating; PC opposing = Sensor dice/rating. `net = man - opp`, `success = net > 0`. Evade Detection -> IC hides (`evaded`, `redetect_turn`); Parry -> `parry_tn_bonus` (+TN to PC's next hit); Position -> `position_bonus` (-TN or +Power on IC's next hit). | `maneuver` (`initiator: npc`) -- e.g. "Killer breaks contact and slips out of your sensors (M vs O)." / "...+N TN to your next attack on it." / "...-N TN on its next attack on you." | `renderActiveIC` reflects a hidden/evaded IC or a guarded stance; the modifier applies to a later C4/C5 row. | Chosen by heuristic: Evade when boxes>=7 (IC-only), Parry at 4-6, Position when healthy & PC hurt. Gated by `state["npc_combat_maneuvers"]`. |
| C12.F | IC maneuver fails | IC | Failure | `net <= 0` incl. an opposing PC win. Position overreach where `opp > man` gifts the PC `pc_position` (-TN on PC's next attack). | `maneuver` -- "Killer tries to break contact but you hold the lock (M vs O)." / "...fails to set a guard." / "...you turn it around (-K TN on your next attack)." | Event line; a Position backfire grants the PC a bonus shown next attack. | -- |
| C12.T | net == 0 | IC | Tie | Tie rule (`maneuver_test`): the maneuvering icon must roll STRICTLY more; `net == 0` (equal successes) is a **failure** -- no advantage gained. | `maneuver` -- "...jockeys for position but gains no edge (M vs O)." / "...no advantage gained." | No modifier set; event line only. | Ties always fail maneuvers (explicit engine rule). |

---

### Opponent type: ENEMY DECKER

Driver `_enemy_decker_take_turn` (~L7647) / `_enemy_decker_take_pass` (~L7939, 2 action points).
Phase 1 = locate the PC; Phase 2 = execute a program (attack / lethal / Hog / crippler), gated by
wounded-AI self-preservation.

#### C13 -- Locate the PC  (`eng.enemy_locate_test` ~L1357; phase ~L7710)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C13.S | Enemy pinpoints the PC | DECKER | Success | `enemy_roll = roll_dice(computer_skill, max(2, pc_detection_factor - scanner))`; `pc_roll = roll_dice(pc_evasion, sensor)`; `progress_gain = max(0, enemy - pc)`. Cumulative `locate_progress >= ENEMY_LOCATE_THRESHOLD (3)` -> `located=True`; a crippler-carrier then `_enemy_scan_pc` pegs the weakest attribute. Complex action (2 AP). | `enemy_decker` (`outcome: located`) -- "<name> has PINPOINTED your icon and jackpoint." (+`scanned` warning if crippler). First contact also emits `hunting` ("ALERT -- a hostile decker is hunting your icon."). | `renderEnemyDeckers` shows the enemy as revealed/located; `renderAlertBadge`; a `scanned` event warns which attribute it will focus. | `revealed=True` set on first locate attempt (PC learns a decker hunts them). |
| C13.F | Enemy makes partial / no progress | DECKER | Failure | `progress_gain` adds but total `< 3` -> still hunting. | `enemy_decker` (`outcome: probing`, `gm_only`) -- "<name> probing: +G -> P/3 located." | GM-only line (redacted for players); `renderEnemyDeckers` still shows a hunting hostile after first contact. | Repeats until threshold. |
| C13.T | enemy successes == pc successes | DECKER | Tie: `progress_gain == 0` | Tie rule: `progress_gain = max(0, enemy_successes - pc_successes)`; equal successes -> `0` gain (a tie = no progress). Not a hard fail (cumulative), but this cycle advances nothing. | Same `probing` gm-only line with `+0`. | No change this pass. | The PC's Evasion vs the enemy Sensor is the live opposing roll here. |

#### C14 -- Intent escalation (dump -> kill)  (`eng.escalate_enemy_intent` ~L1456; ~L7798)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C14.S | Enemy turns lethal | DECKER | Success (escalates) | `security_tally >= threshold (12)` and `base_intent == "dump"` -> returns `"kill"`; if no lethal program loaded it reverts to `dump`. Selects `lethal_program` (Black Hammer/Killjoy) for Phase 2. | No standalone event -- surfaces via the subsequent attack's `outcome: kill` (C16). | `renderEnemyDeckers` may show intent/behaviour shift via the lethal attack that follows. | Black-tier deckers start at `kill`. |
| C14.F | Intent stays dump | DECKER | Failure (no escalation) | Tally `< 12` (or already `kill`, or no lethal program) -> intent unchanged. | -- | -- | Pure state logic. |
| C14.T | Escalation tie | DECKER | Tie: N/A -- unopposed | This is a deterministic threshold check on the security tally, not a roll or an opposed contest -- there is nothing for the PC to tie against. | -- | -- | -- |

#### C15 -- Attack program vs PC icon  (branch ~L7899, `eng.cybercombat_attack`)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C15.S | Enemy crashes/hurts PC icon (Attack) | DECKER | Success | `pool = attack_rating + hacking_pool`; `cybercombat_attack(pool, COMBAT_TN[sec][status] + parry + wound, target_bod=eff.bod, armor, ic_rating=power+position)`; `_shield_parry` (enemy skill = PC Computer). Boxes fill persona; persona 10 -> `_apply_dump_shock`, `icon_crashed`, `run_ended`, `run.status="dumped"`. Simple action (1 AP). | `enemy_decker` (`outcome: dump`) -- "<name> hits your icon with Attack -- LEVEL (N boxes). Persona P/10." + `persona_crash` on crash. | `renderConditionBoxes('persona')`; `renderEnemyDeckers`; on crash `renderRunState` ends run + `renderAlertBadge`. | Default when intent is `dump` (or `kill` w/o lethal program). |
| C15.F | Enemy Attack whiffs | DECKER | Failure | 0 attack successes or staged to None -> 0 boxes. | `enemy_decker` (`outcome: dump`) -- same template, 0 boxes; no crash. | Persona unchanged. | Shield parry can zero it out. |
| C15.T | attack successes == resist successes | DECKER | Tie | Tie rule (same as C4.T): `net_attacker - resist == 0` -> base-level (`IC_DAMAGE_LEVEL[sec]`) lands with no staging; base boxes still fill. Enemy deals base damage on a tie. | `enemy_decker` (`outcome: dump`) -- base LEVEL + boxes. | Persona fills by base box count. | No "no-hit tie" for damage; only 0 successes / down-stage to None is a whiff. |

#### C16 -- Lethal program vs PC (Black Hammer / Killjoy)  (branch ~L7899, `eng.black_attack`)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C16.S | Enemy drives lethal biofeedback | DECKER | Success | `black_attack(pool, base=_LETHAL_BASE_LEVEL(Serious), power=lethal_rating+position, hardening, icon_bod=eff.bod, icon_armor, meat_pool=body(Black Hammer->Physical)/willpower(Killjoy->Stun))`. Persona fills; meat fills Physical/Stun. Meat 10 -> `run_ended`, `run.status="killed"`. Icon 10 -> dump + 2x-rating MPCP burn (`_roll_mpcp_damage(...pool_multiplier=2)`), `run.status="dumped"`. | `enemy_decker` (`outcome: kill`) -- "KILLJOY -- <name> drives lethal biofeedback into you: icon L (N), Stun L (M). Persona x/10, Stun y/10." + `persona_crash` (+MPCP note) on crash. | `renderConditionBoxes` persona + physical/stun; `renderStage`; `renderAlertBadge`; run-end lock in `renderRunState`. | Only Red/Black-tier deckers carry lethal programs; `intent` forced to `kill`. |
| C16.F | Lethal program whiffs | DECKER | Failure | 0 attack successes or both resists down-stage to None. | `enemy_decker` (`outcome: kill`) -- same template, 0/0 boxes. | Monitors unchanged. | -- |
| C16.T | attack == resist (per monitor) | DECKER | Tie | Tie rule (as C5.T): each resist `net == 0` -> Serious base lands on that monitor with no staging. Base-level lethal biofeedback still applies to icon and/or meat. | `enemy_decker` (`outcome: kill`) -- base level on icon + meat. | Persona + physical/stun fill by base boxes. | -- |

#### C17 -- Hog virus vs PC deck  (`_resolve_hog` ~L7552; enemy branch ~L7860)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C17.S | Hog takes hold, drains PC programs | DECKER | Success | `hog_attack(pool, target_status, hog_rating, mpcp=decker.mpcp, hardening)`: `attack_roll` to hit, `resist = roll_dice(mpcp, max(2, hog-hardening))`, `net = max(0, atk-resist)`, `reduction = net//2`. On `atk successes>0 and reduction>0`: seed persistent `hog_infections` + immediate drain of the PC's highest running program (`_HogTarget.drain`); re-drains every Combat Turn (`_drain_all_hog_infections`). | `enemy_decker` (`outcome: hog`) -- "HOG -- <name>'s virus takes hold (drains K/turn): <Program> -X (CRASHED). Purge it or reload via Swap Memory." | `renderEnemyDeckers`; the PC utility roster shows the drained/crashed program; per-turn drain re-logs `enemy_decker`/`hog`. | Simple action; persistent until purged (`hog_purge_test`) or the program crashes. |
| C17.F | Hog fails to take hold | DECKER | Failure | `atk successes == 0` OR `reduction == 0` (net<2). | `enemy_decker` (`outcome: hog`) -- "HOG -- <name>'s virus fails to take hold this pass." | No infection seeded. | Retry next pass. |
| C17.T | atk == resist (net 0) | DECKER | Tie: `net == 0` -> no hold | Tie rule: `net = max(0, atk - resist)`; equal successes -> `net 0`, `reduction 0`, no infection (= C17.F). MPCP resist is the live opposing roll. | Logs the "fails to take hold" branch. | No change. | Also `net==1` fails (needs 2 net for 1 drain). |

#### C18 -- Crippler program vs PC (Poison / Restrict / Reveal)  (`_resolve_attribute_attack` ~L7868)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C18.S | Enemy cripples a PC attribute | DECKER | Success | Same `attribute_attack_core` as C6: `pool` vs to-hit, PC resists targeted attr vs program rating, `+shield`, `reduction = max(0,net)//2` -> `persona_damage[attr]`. Poison->Bod, Restrict->Evasion, Reveal->Masking (`_PROGRAM_ATTR`). Smart opener may FOCUS the PC's weakest attribute once (`_enemy_focus_program`). | `enemy_decker` (`outcome: poison`/`restrict`/`reveal`) -- "POISON -- <name> cripples your Bod by X (now V, until logoff)." | `renderStage`/effective-attr readout drops; Reveal recomputes Detection Factor; Restore action available. | Reveal on Masking also raises the PC's own detectability. |
| C18.F | Crippler resisted | DECKER | Failure | `reduction == 0` (0 attack successes or net<=1). | `enemy_decker` (`outcome: <prog>`) -- "POISON -- <name>'s crippler attack is resisted." | No change. | -- |
| C18.T | net == 0 | DECKER | Tie | Tie rule (as C6): opposed `net = atk - resist - shield == 0` -> `reduction 0`, no cripple. Whiff. | `enemy_decker` -- "...resisted." | No change. | Ties fail; needs >=2 net for a point. |

#### C19 -- Nerve check / flee  (`_enemy_nerve_check` ~L2131)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C19.S | Enemy's nerve breaks -> jacks out (PC gains reprieve) | DECKER | Success (for the enemy = escape; against the PC it ENDS the threat) | First time its icon reaches 7/8/9 persona boxes, `flee_chance = clamp(_ENEMY_NERVE_FLEE[threshold] - 0.15*bravery, 0.05, 0.95)`; `random.random() < flee_chance` -> `status="fled"`. Once per newly-reached threshold. | `enemy_decker` (`outcome: fled`) -- "<name> is wounded (B/10) and its nerve breaks -- it jacks out, abandoning the hunt." | `renderEnemyDeckers` removes/greys the fled decker; PC no longer targeted by it. | This is the enemy self-preserving, not an attack on the PC -- included as an enemy action that changes the fight. |
| C19.F | Enemy holds its nerve | DECKER | Failure (keeps fighting) | `random.random() >= flee_chance` -> stays `active`; proceeds to Medic/Restore/attack. | No flee event; may emit a Medic/Restore/attack instead. | Enemy keeps hunting; `renderEnemyDeckers` unchanged. | Higher bravery lowers flee chance. |
| C19.T | Nerve check tie | DECKER | Tie: N/A -- unopposed | A single probability check against `flee_chance`; no PC roll and no opposed net exists. | -- | -- | -- |

#### C20 -- Hide via Evade maneuver  (wounded-AI ~L7778 -> `_resolve_npc_maneuver` evade)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C20.S | Enemy breaks contact, drops off PC sensors | DECKER | Success | `maneuver_test` (enemy Evasion vs PC Sensor); `net>0` -> `evaded`, `revealed=False`, `redetect_turn = turn+net`. A Medic-carrier then heals while hidden and re-engages at `<= _ENEMY_REENGAGE_BOXES`. | `maneuver` (`initiator: npc`, evade) -- "<name> breaks contact and slips out of your sensors (M vs O)." | `renderEnemyDeckers` drops the enemy from view (hidden); the PC can no longer Strike Back until it re-detects. | Triggered when boxes >= `_ENEMY_WOUNDED_BOXES` and the enemy carries a Medic. |
| C20.F | PC holds the lock | DECKER | Failure | `net <= 0` -> stays visible/targetable. | `maneuver` -- "<name> tries to break contact but you hold the lock (M vs O)." | `renderEnemyDeckers` keeps the enemy revealed. | -- |
| C20.T | net == 0 | DECKER | Tie | Tie rule (`maneuver_test`): `net == 0` (equal successes) -> maneuver FAILS; the enemy stays in the open (= C20.F). | `maneuver` -- fail branch text. | Enemy remains visible. | Ties fail maneuvers. |

#### C21 -- Medic self-heal  (`_enemy_medic_heal` ~L2104)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C21.S | Enemy heals its own icon | DECKER | Success | `medic_heal(rating, wound_level)`: `roll_dice(rating, MEDIC_TN[wound])`; each success heals 1 persona box (capped by damage); Medic degrades 1 rating/use. | `enemy_decker` (`outcome: medic`, `gm_only`) -- "GM: <name> Medic-R treats its wound (TN K): H box(es) healed -- now B/10." | GM-only (redacted for players); `renderEnemyDeckers` shows lower damage; keeps the enemy in the fight. | No-op if icon undamaged or Medic worn/unloaded. Not an attack on the PC. |
| C21.F | Medic heals nothing | DECKER | Failure | `successes == 0` -> `healed 0` (roll still degrades Medic per the core). | `enemy_decker` (`outcome: medic`, `gm_only`) -- "...0 boxes healed -- now B/10." | GM-only; no visible change. | -- |
| C21.T | Medic tie | DECKER | Tie: N/A -- unopposed | Solo Medic Test vs a fixed wound-level TN; no PC counter-roll. | -- | -- | -- |

#### C22 -- Restore self-repair  (`_enemy_restore_repair` ~L2403)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C22.S | Enemy repairs a crippled attribute | DECKER | Success | `_restore_repair_core`: `restore_repair(rating, causing_rating=recorded crippler rating)`; every 2 successes repairs 1 point of temp `persona_damage` (never below the permanent chip floor). Masking repair recomputes stored Detection Factor. Complex action (2 AP). | `enemy_decker` (`outcome: restore`, `gm_only`) -- "GM: <name> runs Restore-R on its BOD (TN K): S successes -> P point(s) restored. BOD now V." | GM-only; `renderEnemyDeckers` shows the recovered attribute; a repaired Masking makes it harder to relocate. | Triggered when `_enemy_repairable_damage >= 2` and Restore loaded. |
| C22.F | Restore repairs nothing | DECKER | Failure | `points_repaired == 0` (successes < 2). Restore does NOT self-degrade. | `enemy_decker` (`outcome: restore`, `gm_only`) -- "...0 point(s) restored." | GM-only; no change. | Returns `None` (no-op) if nothing repairable. |
| C22.T | Restore tie | DECKER | Tie: N/A -- unopposed | Solo Restore Test vs the causing crippler's rating (a fixed TN); no PC counter-roll. | -- | -- | -- |

#### C23 -- Enemy decker combat maneuver vs PC (Parry / Position)  (`_npc_maybe_maneuver` is_ic=False ~L7822)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C23.S | Enemy sets a guard / seizes position | DECKER | Success | `maneuver_test` (enemy Evasion dice/rating vs PC Sensor); `net>0`. Parry -> `parry_tn_bonus` (+TN to PC's next hit on it); Position -> `position_bonus` (-TN or +Power on the enemy's next attack). | `maneuver` (`initiator: npc`) -- "<name> takes a defensive stance -- +N TN to your next attack on it." / "...-N TN on its next attack on you." | `renderEnemyDeckers`; the modifier applies to a later C15/C16 row (consumed via `_consume_attack_mods_vs_pc`). | Parry at 4-6 boxes, Position when healthy & PC hurt; deckers don't Evade here (handled by the wounded-AI hide loop). Gated by `npc_combat_maneuvers`. |
| C23.F | Enemy maneuver fails | DECKER | Failure | `net <= 0`; a Position overreach (`opp > man`) grants the PC `pc_position` (-TN next attack). | `maneuver` -- "...fails to set a guard." / "...you turn it around (-K TN on your next attack)." | Event line; a backfire helps the PC's next strike. | -- |
| C23.T | net == 0 | DECKER | Tie | Tie rule (`maneuver_test`): `net == 0` -> maneuver fails, no advantage. | `maneuver` -- "...no advantage gained." | No modifier set. | Ties fail maneuvers. |

---

### Opponent type: CONSTRUCT

A Construct is stored as an `active_ic` entry with `type="Construct"` (~L1328) plus
`construct_components` / `construct_defenses`. It runs the **standard proactive cybercombat path**
in `_advance_npc_pass` (~L5058), with two construct-specific differences: its attack pool and
Shield-parry skill use the **Construct's own `rating`** (not the host Security Value) --
`ic_attack_pool = ic["rating"]` and `ic_skill = ic["rating"]`.

#### C24 -- Construct proactive attack vs PC  (cybercombat / black paths, Construct rating drives the pool)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C24.S | Construct hits PC icon (+ meat if Black) | CONSTRUCT | Success | `cybercombat_attack(attacker_pool = ic["rating"] (+expert +cascade), COMBAT_TN[sec][status] + cluster + parry + wound - traces, target_bod=eff.bod, armor, ic_rating=rating+cascade+position)`; Shield parry TN = Construct rating. Persona fills; persona 10 -> `persona_crash` + dump shock. If the Construct's component is Black-flavoured it routes through the black branch (icon + meat, jack-out gate). | `ic_attack` -- "Construct-R attacks: A vs Rz. Damage: L (N boxes). Persona P/10." (or the Black IC lines if black). | `renderActiveIC` shows the Construct and its `construct_components`/`construct_defenses`; `renderConditionBoxes` fills; crash flow as C4/C5. | Construct uses its OWN rating for BOTH pool and defensive TN, unlike host-driven IC. |
| C24.F | Construct misses / resisted | CONSTRUCT | Failure | 0 attack successes or staged to None; `_apply_cascade_outcome(hit=False)` raises the Construct's SV/rating. | `ic_attack` -- 0 boxes. | Persona unchanged; a cascaded higher rating may show next pass. | -- |
| C24.T | attack == resist | CONSTRUCT | Tie | Tie rule (as C4.T): `net == 0` -> base-level damage lands with no staging. | `ic_attack` -- base LEVEL + boxes. | Persona fills by base boxes. | Same "no no-hit tie" for damage attacks. |

---

### Opponent type: PARTY IC (cluster)

A Party IC is a group of `active_ic` sharing a `cluster_id` (~L1351). Each member acts on its own
initiative through the same proactive path, but every member's attack carries a **cluster penalty**
`tn_modifier = _cluster_size(state, ic.get("cluster_id"))` (~L5069) added to the to-hit TN -- the
crowd of icons gets in each other's way. Otherwise the member resolves exactly like C4 (standard)
or C5 (a Black member).

#### C25 -- Party-IC member proactive attack vs PC  (cybercombat / black + `cluster_penalty`)

| ID | Enemy action | Opponent | Outcome | Roll / mechanic | Event log (type + text) | UI / DOM effect | Preconditions / notes |
|----|--------------|----------|---------|-----------------|-------------------------|-----------------|------------------------|
| C25.S | Cluster member hits PC icon | PARTY-IC | Success | Same as C4.S/C5.S but `tn_modifier` includes `cluster_penalty = _cluster_size(cluster_id)` (each additional icon in the cluster raises this member's to-hit TN). Damage/crash flow identical to the member's subtype (Killer/Blaster/Sparky -> C4; Black IC -> C5). | `ic_attack` -- standard member template; the higher effective TN just lowers hit odds (not separately labelled). | `renderActiveIC` shows each clustered member (shared `cluster_id`); `renderConditionBoxes`; crash flow per subtype. | The cluster penalty makes each member LESS accurate; the threat is volume of attacks, not per-hit power. |
| C25.F | Cluster member misses / resisted | PARTY-IC | Failure | As C4.F/C5.F, made more likely by the cluster TN penalty. | `ic_attack` -- 0 boxes. | Persona unchanged. | Larger clusters whiff more per member. |
| C25.T | attack == resist | PARTY-IC | Tie | Tie rule (as C4.T/C5.T): `net == 0` -> base-level damage lands with no staging (icon, plus meat for a Black member). | `ic_attack` -- base LEVEL + boxes. | Persona (and physical/stun for a Black member) fill by base boxes. | Cluster penalty affects the to-hit roll, not the tie definition. |

---

#### Coverage summary

ID range used: **C1 .. C25** (each with `.S` / `.F` / `.T` outcome rows = 75 outcome rows total).

- **IC:** C1 (Probe), C2 (Trace hunt), C3 (Trace locate completion), C4 (Killer/Blaster/Sparky
  cybercombat), C5 (Black IC), C6 (crippler), C7 (ripper), C8 (Tar Baby/Tar Pit), C9 (Worm),
  C10 (Data Bomb), C11 (Poison Scramble), C12 (IC combat maneuver).
- **DECKER:** C13 (locate), C14 (intent escalation), C15 (Attack), C16 (Black Hammer/Killjoy),
  C17 (Hog), C18 (Poison/Restrict/Reveal), C19 (nerve/flee), C20 (hide/evade), C21 (Medic),
  C22 (Restore), C23 (Parry/Position maneuver).
- **CONSTRUCT:** C24 (proactive attack, Construct rating drives the pool).
- **PARTY-IC:** C25 (cluster member attack with `cluster_penalty`).

---

<a id="sec-d"></a>

## Section D &mdash; Live-Execution Feasibility

**Question:** how much of a Matrix-run action-outcome catalog can be produced by *live*
execution -- actually running the engine and capturing the real `event_log` entries + run
state JSON the UI renders -- with Success / Failure / Tie forced deterministically?

**Answer (verdict up front):** the outcome-bearing core -- every resolver that funnels
through `matrix_engine.roll_dice` -- **can** be driven live and deterministically in-process.
The probe below does exactly that for three representative actions across S/F/T and captures
the byte-for-byte event dicts. A meaningful minority of catalog *entries* cannot be produced
purely live without heavy state scaffolding or are gated by the HTTP/DB/auth layer; those are
enumerated in section 4. Recommended strategy in section 5.

Probe script: [tools/matrix_outcome_probe.py](../tools/matrix_outcome_probe.py)
Run: `.\.venv\Scripts\python tools\matrix_outcome_probe.py` -- **ran successfully (exit 0)**.
No DB writes; the already-running uvicorn server is never touched.

---

### 1. How to force S / F / T deterministically -- decision + justification

Three options were on the table:

| Option | Verdict | Why |
|---|---|---|
| Seed a local `random.Random` | rejected | The outcome would still be a function of pool size, target number, and the rule-of-6 explosion. To force a *specific* success count you must reverse-engineer faces per pool -- brittle and different for every action. |
| Call engine functions directly, bypassing the router | partial | Good for pure primitives, but it would NOT produce the real `event_log` dicts the UI renders -- those are composed in the router endpoints, not the engine. |
| **Monkeypatch `matrix_engine.roll_dice` to return a scripted success count** | **chosen** | `roll_dice` is the *single* opposed-test primitive every resolver calls (`system_test`, `cybercombat_attack` -> `damage_resistance`, `attribute_attack_core`, `maneuver_test`, `tar_baby_test`, `shield_parry`, `medic_heal`, ...). Controlling its `successes` return directly forces the decker-vs-host / attacker-vs-defender result **regardless** of pool, TN, or rule-of-6. It is exact and call-order-addressable. |

The probe installs a `ScriptedRollDice` callable over `eng.roll_dice` that pops the next
scripted success count in call order and returns a coherent roll dict (pool honoured, a
plausible dice list synthesised, `ones = 0` so a data-bomb "all ones" detonation can never
fire by accident). It also pins `matrix_engine.random` and `matrix_runs.random` to a fixed
RNG so any *residual* non-`roll_dice` randomness (enemy nerve / spawn / choice) is stable.

**Execution layer:** the probe calls the **real async endpoint bodies**
(`mr.perform_action`, `mr.attack_ic`) and the **real app-as-GM driver**
(`mr._advance_npc_pass`) in-process -- not via HTTP -- with a fake run object and a no-op
`AsyncSession`, monkeypatching `_get_run_or_404` and `_serialize_run` so no DB or auth is
touched. The `event_log` entries produced are byte-for-byte what a real `POST` would persist
and the UI would render. Run state is built in memory by the real `_initial_state(decker,
host)` on a `SimpleNamespace` host.

Call order per action (what the script queue maps onto):
* **system_test op** (`analyze_host`): `[decker_roll, host_roll]`.
  Success rule (`matrix_engine.system_test`): `decker_net >= 0 AND decker_successes > 0`
  (house rule -- a tie goes to the decker; a 0-vs-0 mutual whiff still fails).
* **cybercombat** (`attack_ic`, and IC->decker): `[attack_roll, resist_roll]`.
  There is no discrete tie/fail branch -- damage = the program's base Damage Level staged by
  `(attacker_net - resist) // 2`, clamped to Deadly.

---

### 2. Enemy roster constructed live (in-memory state)

The probe builds one run state carrying every enemy-type category the engine recognises
(captured output):

```
active_ic types : ['Killer', 'Construct', 'Killer', 'Killer']
party cluster   : ['ic_party_a', 'ic_party_b']   (shared cluster_id -> Party-IC)
lurking_ic      : [('Worm', 'deathworm')]
enemy_deckers   : ['BlackHat']
```

---

### 3. Captured live outcomes (REAL event_log dicts + state deltas)

Everything below is copied verbatim from the probe run. Dice lists are the synthetic faces
the scripted `roll_dice` emits; `successes` is the forced value that drives the branch.

#### 3.1 ACTION 1 -- `attack_ic` (decker -> Killer-8 cybercombat)

**SUCCESS** (attack scores, IC fails to resist -> damage lands):
```json
{"type": "decker_attack", "ic_id": "ic_killer", "description": "Attacked Killer-8: 4 successes. Dealt Deadly (6 boxes). IC: 6/10", "attack_roll": {"pool": 8, "tn": 6, "dice": [6, 6, 6, 6, 2, 2, 2, 2], "successes": 4, "ones": 0}, "resist_roll": {"pool": 8, "tn": 6, "dice": [2, 2, 2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "final_damage_level": "Deadly", "boxes": 6, "ic_boxes": 6, "turn": 1}
```
state delta: `active_ic.0.boxes: 0 -> 6`

**FAILURE** (attack whiffs -> 0 successes):
```json
{"type": "decker_attack", "ic_id": "ic_killer", "description": "Attacked Killer-8: 0 successes. Dealt Light (1 boxes). IC: 1/10", "attack_roll": {"pool": 8, "tn": 6, "dice": [2, 2, 2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "resist_roll": {"pool": 8, "tn": 6, "dice": [6, 6, 6, 6, 2, 2, 2, 2], "successes": 4, "ones": 0}, "final_damage_level": "Light", "boxes": 1, "ic_boxes": 1, "turn": 1}
```
state delta: `active_ic.0.boxes: 0 -> 1`

**TIE** (equal successes, net 0):
```json
{"type": "decker_attack", "ic_id": "ic_killer", "description": "Attacked Killer-8: 2 successes. Dealt Serious (3 boxes). IC: 3/10", "attack_roll": {"pool": 8, "tn": 6, "dice": [6, 6, 2, 2, 2, 2, 2, 2], "successes": 2, "ones": 0}, "resist_roll": {"pool": 8, "tn": 6, "dice": [6, 6, 2, 2, 2, 2, 2, 2], "successes": 2, "ones": 0}, "final_damage_level": "Serious", "boxes": 3, "ic_boxes": 3, "turn": 1}
```
state delta: `active_ic.0.boxes: 0 -> 3`

> **Note:** cybercombat has NO "tie fails" branch. A net-0 exchange still deals the program's
> *base* Damage Level (here Serious), because damage stages from the base by net successes.
> Even the "failure" row deals Light (1 box) -- a whiffed attack that the defender fully
> resists is staged down to base-minus, not to zero. This is a real engine property worth
> catalouging, not a probe artefact.

#### 3.2 ACTION 2 -- `analyze_host` (System Test on Access; opposed decker-vs-host)

**SUCCESS** (decker net +2, successes > 0):
```json
{"type": "action", "action": "analyze_host", "subsystem": "access", "description": "Analyze Host -- SUCCESS (2 vs 0 successes). Tally +0 -> 0.", "success": true, "decker_roll": {"pool": 6, "tn": 8, "dice": [8, 8, 2, 2, 2, 2], "successes": 2, "ones": 0}, "host_roll": {"pool": 8, "tn": 3, "dice": [2, 2, 2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "tally_increase": 0, "tally_total": 0, "action_cost": "Complex", "turn": 1, "init": 30}
{"type": "host_analyzed", "revealed": [], "description": "Analyze Host succeeded -- choose 2 subsystem rating(s) to reveal.", "turn": 1, "init": 30}
```
state delta: (none -- reveal is a follow-up choice)

**FAILURE** (decker 0 successes; host scores 2 -> tally rises):
```json
{"type": "action", "action": "analyze_host", "subsystem": "access", "description": "Analyze Host -- FAILED (0 vs 2 successes). Tally +2 -> 2.", "success": false, "decker_roll": {"pool": 6, "tn": 8, "dice": [2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "host_roll": {"pool": 8, "tn": 3, "dice": [6, 6, 2, 2, 2, 2, 2, 2], "successes": 2, "ones": 0}, "tally_increase": 2, "tally_total": 2, "action_cost": "Complex", "turn": 1, "init": 30}
```
state delta: `security_tally: 0 -> 2`

**TIE -> decker** (net 0, decker successes > 0 -> SUCCESS by house rule):
```json
{"type": "action", "action": "analyze_host", "subsystem": "access", "description": "Analyze Host -- SUCCESS (2 vs 2 successes). Tally +2 -> 2.", "success": true, "decker_roll": {"pool": 6, "tn": 8, "dice": [8, 8, 2, 2, 2, 2], "successes": 2, "ones": 0}, "host_roll": {"pool": 8, "tn": 3, "dice": [6, 6, 2, 2, 2, 2, 2, 2], "successes": 2, "ones": 0}, "tally_increase": 2, "tally_total": 2, "action_cost": "Complex", "turn": 1, "init": 30}
```
state delta: `security_tally: 0 -> 2`

**TIE -> mutual whiff** (0-vs-0, the one tie that FAILS):
```json
{"type": "action", "action": "analyze_host", "subsystem": "access", "description": "Analyze Host -- FAILED (0 vs 0 successes). Tally +0 -> 0.", "success": false, "decker_roll": {"pool": 6, "tn": 8, "dice": [2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "host_roll": {"pool": 8, "tn": 3, "dice": [2, 2, 2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "tally_increase": 0, "tally_total": 0, "action_cost": "Complex", "turn": 1, "init": 30}
```
state delta: (none)

#### 3.3 ACTION 3 -- enemy proactive attack (app-as-GM: Killer-8 IC -> decker)

Driven by the real `_advance_npc_pass`.

**SUCCESS (for the IC)** -- it hits, decker fails to resist:
```json
{"type": "ic_attack", "ic_id": "ic_killer", "ic_type": "Killer", "ic_rating": 8, "description": "Killer-8 attacks: 4 attack successes vs 0 resist. Damage: Deadly (6 boxes). Persona: 6/10", "attack_roll": {"pool": 8, "tn": 3, "dice": [6, 6, 6, 6, 2, 2, 2, 2], "successes": 4, "ones": 0}, "resist_roll": {"pool": 6, "tn": 8, "dice": [2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "final_damage_level": "Deadly", "boxes": 6, "persona_total": 6, "turn": 1, "init": 24}
```
state delta: `condition_monitor.persona_boxes: 0 -> 6`

**FAILURE (for the IC)** -- decker resists; note the follow-on `simsense_overload` event fires live:
```json
{"type": "ic_attack", "ic_id": "ic_killer", "ic_type": "Killer", "ic_rating": 8, "description": "Killer-8 attacks: 0 attack successes vs 4 resist. Damage: Light (1 boxes). Persona: 1/10", "attack_roll": {"pool": 8, "tn": 3, "dice": [2, 2, 2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "resist_roll": {"pool": 6, "tn": 8, "dice": [8, 8, 8, 8, 2, 2], "successes": 4, "ones": 0}, "final_damage_level": "Light", "boxes": 1, "persona_total": 1, "turn": 1, "init": 24}
{"type": "simsense_overload", "description": "Simsense overload! Willpower test failed (TN 4). 1 Stun damage.", "roll": {"pool": 6, "tn": 4, "dice": [2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "turn": 1, "init": 24}
```
state deltas: `persona_boxes: 0 -> 1`, `stun_boxes: 0 -> 1`

**TIE** (net 0 -> base Serious):
```json
{"type": "ic_attack", "ic_id": "ic_killer", "ic_type": "Killer", "ic_rating": 8, "description": "Killer-8 attacks: 2 attack successes vs 2 resist. Damage: Serious (3 boxes). Persona: 3/10", "attack_roll": {"pool": 8, "tn": 3, "dice": [6, 6, 2, 2, 2, 2, 2, 2], "successes": 2, "ones": 0}, "resist_roll": {"pool": 6, "tn": 8, "dice": [8, 8, 2, 2, 2, 2], "successes": 2, "ones": 0}, "final_damage_level": "Serious", "boxes": 3, "persona_total": 3, "turn": 1, "init": 24}
{"type": "simsense_overload", "description": "Simsense overload! Willpower test failed (TN 7). 1 Stun damage.", "roll": {"pool": 6, "tn": 7, "dice": [2, 2, 2, 2, 2, 2], "successes": 0, "ones": 0}, "turn": 1, "init": 24}
```
state deltas: `persona_boxes: 0 -> 3`, `stun_boxes: 0 -> 1`

---

### 4. Coverage assessment -- what CAN and CANNOT be driven live this way

#### 4.1 CAN be driven live + deterministically (the majority)

Any action whose outcome is decided by one or a few `roll_dice` calls, resolved against
state you can build in a plain dict. Proven or trivially reachable by the same harness:

* **All cybercombat** -- `attack_ic`, IC->decker, decker->enemy-decker (shared
  `eng.cybercombat_attack`), plus the Black family (`eng.black_attack`: Black IC / Black
  Hammer / Killjoy) which take the same `[attack, resist(, meat)]` script shape.
* **All host System Test operations** -- Analyze (Host/Security/Subsystem/Icon), Locate
  (Paydata/IC/Decker), Validate/Invalidate Passcode, Edit File, Crash Host, Null Op, Decoy,
  Redirect Datatrail, Decrypt File -- every one routes through `eng.system_test`; script
  `[decker, host]`.
* **Attribute attacks / cripplers / rippers** (`eng.attribute_attack_core`), **Tar
  Baby/Tar Pit** (`eng.tar_baby_test`), **combat maneuvers** (`eng.maneuver_test`, ties
  fail), **defensive utilities** (`shield_parry`, `medic_heal`, `restore_repair`,
  disinfect/purge) -- all single-primitive, all scriptable by success count.
* **Trace IC hunt cycle** (`eng.trace_hunt_cycle_attack`) and **Probe IC** system-test
  reactions -- reachable through `perform_action` / `_advance_npc_pass` as shown.
* **Cascade / follow-on events** -- e.g. the `simsense_overload` and sheaf-triggered
  events fire live for free once the parent action runs (see 3.3). This is a strong reason
  to prefer live capture over hand-authoring: secondary events come along automatically.

#### 4.2 CANNOT be produced purely live without extra work -- and exactly why

* **Multi-step / multi-turn transfers.** `download_data` commits an ongoing Null-Op each
  turn; a completed download requires N `new_turn` advances plus a `storage_free_mp` ledger
  and a located, un-downloaded paydata row. Producible live, but needs a scripted *sequence*
  of calls, not a single forced roll. Same for **trap-door entry** (spawns a fresh linked
  run) and **graceful logoff** (ends the run and flips `run.status`).
* **Deep prior-state prerequisites.** Reveal-gated ops only emit their interesting event
  when the right precursor state exists: Defuse Data Bomb needs a *discovered* bomb; Decrypt
  File needs a *discovered* scramble; Restore/Disinfect need existing persona/MPCP damage;
  Suppress needs a crashed/hung IC. The roll is live; the *setup* is bespoke per entry.
* **HTTP/DB/auth-layer behaviours.** These are NOT reachable through the in-process engine
  path at all and can only be exercised via the real ASGI stack:
  - **Ownership gating / 404-not-403** (`_assert_run_access`) -- an auth concern; the probe
    deliberately patches it out.
  - **Optimistic-lock 409 (`StaleDataError`)** on `MatrixRun.version` -- requires two
    concurrent committing writers against the real DB; there is no meaningful "event_log
    outcome", it is an HTTP status.
  - **Rate-limiter backoff** -- middleware, IP-keyed, no run state.
* **Randomness the probe pins but a real run rolls freely.** Sheaf *activation* order,
  enemy-decker *spawn* chance, initiative, and the enemy AI nerve/flee model are driven by
  `random.random()` / `randint`, which the probe freezes for determinism. Their *S/F/T
  outcomes* are still forceable, but a faithful "as it happens in production" sample of the
  spawn/nerve branches means choosing which frozen value to install -- a catalog decision,
  not an engine limitation.

None of the 4.2 items are *blocked*; they simply need scripted call sequences or specific
seed state, so they cost more per catalog entry than the one-roll actions in 4.1.

---

### 5. Recommendation

**Static-derived catalog with a live-verified sample -- not a fully-live catalog.**

Rationale:

1. **The engine funnels through one primitive.** Because every outcome resolves through
   `roll_dice`, the *shape* of each event dict is highly regular. Once the live probe has
   captured a verified specimen per resolver (cybercombat, system_test, black_attack,
   attribute_attack, maneuver, tar_baby, trace, the defensive utilities -- ~10 primitives),
   the remaining ~40+ catalog entries are the same shapes with different labels/ratings.
   Deriving those statically from the specimens is cheap and exact.
2. **Live capture pays off precisely where hand-authoring is error-prone** -- the cascade
   events (simsense overload, sheaf steps, tally acceleration, dump shock) that a static
   author would forget. So capture those *live* for the representative sample.
3. **The 4.2 tail is expensive live.** Multi-turn transfers, reveal-gated ops, and the
   HTTP-only behaviours each need bespoke scaffolding; producing all of them live has a poor
   effort-to-coverage ratio.

**Concrete plan:** extend `tools/matrix_outcome_probe.py` into a fixture generator that runs
each of the ~10 primitives once per S/F/T (this proof already covers 3), dumps the real event
dicts to JSON, and let the catalog reference those verified specimens -- filling the long tail
by static templating keyed to the shared primitive, exactly as the existing
`tests/test_matrix_numeric_oracle.py` proves coverage by resolver key.

---

### Appendix -- reproduce

```
.\.venv\Scripts\python tools\matrix_outcome_probe.py
```
Deterministic, no DB writes, does not touch the running server. Exit code 0.

