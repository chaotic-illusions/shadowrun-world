# Shadowrun 2E — AI Narrative Parser Reference

This document is included in the Claude system prompt to ground narrative parsing
in campaign-specific mechanics.  Update it as the campaign evolves.

---

## Consequence Tags

Use these exact strings in `outcome_tags`.  Only include tags directly supported
by the narrative; do not infer tags not described.

| Tag | When to use |
|---|---|
| `witnesses` | Credible eyewitnesses to runner identities or activities |
| `collateral_damage` | Bystander injury, building damage, unprovoked property destruction |
| `public_scene` | Incident visible to ordinary citizens in a public space |
| `media_attention` | Newscast, social media, corporate press release about the event |
| `casualties` | Non-runner deaths that were incidental to the job |
| `wetwork` | Targeted killing that *was* the contract objective |
| `assassination` | High-profile or politically significant targeted killing |
| `magic_use` | Visible spellcasting or summoning witnessed by non-runners |
| `vehicle_chase` | High-speed pursuit through city streets or traffic |
| `data_theft` | Digital intrusion — no physical evidence, no witnesses |
| `extraction` | Person abducted or rescued — use `witnesses` too if seen |
| `bribery` | Officials or security paid off; leaves no public record |
| `false_flag` | Evidence planted to implicate a third party |
| `stealth` | Ghost run — no witnesses, no trace, no evidence left |

---

## Proposed Changes — Type Rules

### `street_cred`
Use for ALL run-related reputation changes based on skill and professionalism.

- Clean success vs. a difficult target: **+2 to +3**
- Routine success: **+1**
- Partial success / sloppy: **+0 to +1**
- Failure (word gets out): **−1 to −2**
- Do NOT use `notoriety` for failures — use negative `street_cred`.

### `notoriety`
Only for events that mark a runner as genuinely infamous — independent of run outcome.

- Civilian massacre: **+2 to +3**
- Betrayal of a Johnson or teammate: **+1 to +2**
- Documented atrocity or shadowrunner code violation: **+1**
- A run going wrong does NOT generate notoriety on its own.

### `public_awareness`
Only if the event made it into public consciousness — news, social feeds, corp bulletins.

- Local news / neighbourhood awareness: **+1**
- City-wide coverage, viral footage: **+2**
- Major international incident: **+3**
- Do NOT apply PA for shadow-community events invisible to ordinary citizens.

### `org_standing`
Scale: −5 (grievous harm) to +5 (major favour), 0 = neutral.

- Completed contract cleanly for a Johnson: **+1 to +2** to their org
- Collateral damage to org assets: **−1 to −2**
- Run directly targeted and harmed org: **−3 to −5**
- Provided intel or leverage that greatly helped org: **+3 to +4**
- Standing changes ripple: allies of the affected org get 40% of the delta (capped ±2), enemies get −40%.

### `heat`
Individual character exposure level (0–10 scale).

- Runner personally identified, filmed, or named in a report: **+2 to +3**
- Runner wanted by Lone Star / Knight Errant: **+2 to +4**
- Runner in the scene but kept anonymous: **+1**
- Runner not present or fully covered tracks: **0** (do not include)
- Runner successfully disappeared after prior exposure: **−1 to −2**
- Do NOT give heat to support runners who never attended the scene.

---

## Org Types and their Interests

Use org `org_type` to infer standing impact direction.

| org_type | Interests harmed by | Interests helped by |
|---|---|---|
| `megacorp` | Espionage, sabotage, extraction of their assets | Payment for contract work, protecting their assets |
| `gang` | Encroachment on territory, killing members | Defeating mutual rivals, payment |
| `law_enforcement` | Any illegal activity that makes news | Providing tips, taking down criminals they want down |
| `criminal` | Disrupting their operations, informing | Doing dirty work, moving contraband |
| `government` | Destabilization, embarrassing leaks | Deniable ops that serve their agenda |
| `fixer` | None specific | Successful runs (they brokered the contract) |
| `corp_sec` | Breaches they were guarding against | Nothing — they don't hire runners |
| `awakened_group` | Harming magical sites or metahumans | Protecting magical interests |
| `shadowrunner_crew` | Backstabbing, taking their contacts | Backing them up, sharing credits |

---

## Character Context Tips

- Match `character_name` exactly to the world context list.
- If the narrative says "the team" without naming individuals, apply changes to all PCs in the world context who could plausibly have participated.
- Do NOT apply changes to characters marked as NPCs unless the narrative explicitly names them performing the action.
- For contacts / NPCs acting as Johnsons, do NOT include them in `proposed_changes` — only include player characters and their faction standings.

---

## Outcome Selection Guide

| Narrative signal | Outcome |
|---|---|
| Objective complete, no heat | `success` |
| Objective complete, complications | `partial_success` |
| Objective failed, team extracted safely | `failure` |
| Objective failed AND major collateral / PC deaths / blown covers | `critical_failure` |
| Run called before contact / team walked away | `abandoned` |
