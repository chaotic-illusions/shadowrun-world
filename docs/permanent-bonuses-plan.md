# Permanent bonuses: track them apart from the base, apply them everywhere

Goal: every *permanent* bonus (adept powers, cyberware, bioware) is kept apart from the base
rating it sits on. Karma raises are priced on the base, and the bonus stacks on top. The one
exception is Improved Physical Attributes, where the book prices the raise on the total.
Temporary boosts (Attribute Boost, spells, drugs) are NOT tracked this way.

Status: implemented 2026-11-22 (answers to the open questions are at the bottom).

---

## What exists today

| Bonus | Tracked apart from base? | Shown on the play sheet? | Karma priced on base? |
|---|---|---|---|
| Cyber/bio attribute mods (Muscle Replacement, Encephalon...) | yes (`augAttr`) | in the stored total; "base (N total)" in Manage Attributes | yes |
| Cyber/bio skill dice with `skillBonus` (Math SPU, Synthacardium, Tailored Pheromones, Enhanced Articulation, Move-by-Wire) | yes | "+N (source)" note on the general skill only | yes |
| Reflex Recorder (+1 die, one chosen skill) | skill is stored on the line | NO | yes |
| Cyber/bio Reaction + Initiative dice (Wired/Boosted Reflexes, Synaptic Accelerator, Move-by-Wire) | builder only | NO: play sheet Initiative is always 1D6, Reaction is always (Q+I)/2 | n/a |
| Improved Physical Attributes | NO | NO: not applied anywhere, in builder or sheet | n/a |
| Improved Ability | NO | NO | yes (by accident) |
| Increased Reaction / Increased Reflexes | NO | NO | n/a |
| Combat Sense, Killing Hands, Mystic Armor | yes | yes (Combat Pool, unarmed damage, armor) | n/a |

## Which adept powers are permanent and touch a stat

- **Improved Physical Attributes**: permanent, +level to Body/Strength/Quickness.
- **Increased Reaction**: permanent, +level Reaction, no Initiative dice.
- **Increased Reflexes**: permanent, +1/+2/+3 Initiative dice.
- **Improved Ability**: permanent, +level dice to one general skill and equally to its
  Concentrations/Specializations.
- **Attribute Boost**: temporary. Not tracked.
- No other power adds to a skill or attribute. The rest add dice to specific situational tests
  (Body Control, Counterstrike, Iron Will, Flexibility, Rooting...). Those stay as reference text.
- Already applied: Combat Sense, Killing Hands, Mystic Armor.

---

## Batch 1: Skills (display only, Karma unchanged)

1. Improved Ability: show "+N (Improved Ability)" on the general skill AND on each of its
   Concentrations/Specializations (book: the dice carry over equally). Example: Unarmed Combat 5 /
   Boxing 7 with 1 die reads 5 / 7, each part showing +1 (rolls 6 / 8).
2. Reflex Recorder: show its +1 die on the recorded skill (General: the general skill; Concentration:
   that Concentration). It is cyberware the sheet already stores, just never displayed.
3. Karma raises in Manage Skills keep using the stored base rating. No change needed, just confirm
   by test.

## Batch 2: Improved Physical Attributes on attributes (book rule)

1. New shared helper: the IPA bonus for an attribute = the level on that attribute's IPA line.
2. Builder: `finalAttr` = natural + cyber/bio + IPA. So the committed attribute, Reaction, Combat Pool
   and the summary all include it. Attribute *points* are still spent on the base only.
3. Play sheet:
   - computes each attribute live as base + racial + cyber/bio + IPA, so an existing adept shows the
     right number immediately even before their stored value is corrected.
   - Manage Attributes shows the IPA bonus separately, like cyberware ("4 base, 6 total").
   - **Karma raise cost uses the total including IPA** (SR2 p.125), but NOT cyber/bio. Example:
     Strength 4 + IPA 2 -> raising to natural 5 costs 7 (the new total), not 5.
   - Saving writes the corrected total (including IPA) to the stored attribute column.
4. The Racial Maximum still caps the *natural* rating for Karma raises (see Q2).

## Batch 3: Reaction and Initiative on the play sheet

1. Physical Reaction = floor((Q+I)/2) + cyber/bio Reaction mods + Increased Reaction level.
   Q includes IPA, since Reaction is computed from the augmented attributes.
2. Physical Initiative dice = 1 + cyber/bio Initiative dice + Increased Reflexes level.
3. The builder already does the cyber/bio half. Add the two adept powers there too, so the builder
   summary and the sheet agree.
4. Rigging and Matrix stay as they are (assumption: reflex boosters don't apply there; Synaptic
   Accelerator's own text says it doesn't help with rigging or decking).
5. Stacking: see Q1.

## Batch 4: Existing characters (as built)

- Convention from now on: the stored attribute column ALWAYS includes Improved Physical
  Attributes, the same as cyber/bio. The builder commits it; every play-sheet write includes it;
  base fallbacks subtract it.
- One-time startup backfill (`app/main.py` `_backfill_adept_attrs_once`) adds each existing
  adept's IPA levels to the stored column, guarded by `campaign_state.adept_attrs_backfilled`
  (startup guard + Alembic migration `b3e7c1d9a420`) so a restart never adds them twice.
- Because the stored column is now always right, the play sheet reads it directly instead of
  computing attributes live (that keeps GM hand-edits of the column intact).
- Deploy note: run the rebuild/restart right after `git pull`. The frontend is a live mount, so a
  builder commit made in the gap would include IPA and then get it added again by the backfill.

## Tests

- Unit: the IPA bonus helper, the Karma cost with and without IPA.
- Browser: an adept with IPA Strength 2 + Increased Reflexes 1 + Wired Reflexes 1 + Improved Ability
  Unarmed 1 + a Reflex Recorder. Check the sheet's attributes, Reaction, Initiative, skill notes, the
  Manage Attributes cost, and what's saved.
- Builder: the committed attributes include IPA; the summary's Reaction/Initiative include the powers.

---

## Open questions

**Q1. Do Increased Reflexes / Increased Reaction stack with cyber/bio reflex boosters?**
The catalog's cyber/bio entries already say they don't stack with each other (Boosted Reflexes vs
Wired Reflexes; Synaptic Accelerator vs both; Move-by-Wire vs all). Nothing in our catalog text
covers adept power + cyberware. Options:
  a) stack fully
  b) don't stack: use whichever gives more
  c) block buying the second one
Also: is there a maximum number of extra Initiative dice?
> Answer: (b) per stat, whichever is greater wins: Reaction bonus = max(cyber/bio, Increased
> Reaction); extra Initiative dice = max(cyber/bio, Increased Reflexes). No maximum; purchases cap it
> naturally (around 5D6).

**Q2. Racial Maximum with IPA: does it cap the natural rating or the total?**
Proposal: Karma can raise the natural rating up to the Racial Maximum. IPA sits on top, so the
total can go past it (IPA itself goes up to 1.5x the Racial Maximum).
> Answer: yes, as proposed.

**Q3. Fix stored attributes for existing IPA adepts now, or let them correct on next save?**
> Answer: fix them now (one-time data migration).

**Q4. Pain Resistance** is permanent, but it changes wound modifiers, and the play sheet doesn't
compute wound modifiers at all yet. Leave it as reference text (proposal), or add wound modifiers
to the condition monitor as a separate job?
> Answer: reference text only.
