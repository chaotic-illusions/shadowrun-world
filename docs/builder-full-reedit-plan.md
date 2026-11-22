# Plan: full re-edit of a finished runner in the builder

Status: IMPLEMENTED (2026-11-21). Kept as the design record.

## Goal

"Edit in Builder" takes a finished runner back to the character builder with **nothing
locked**. The builder loads the runner **as it is now**, and everything earned in play counts as
part of character creation:

- current inventory, including gear, cyberware and bioware bought in play;
- spells and adept powers.

The player can add or remove anything. Whatever they don't remove stays.

This *replaces* today's locked Edit in Builder, including the gear sell-back added earlier
today. Selling back isn't needed once gear is freely editable. Pre-builder runners (no stored
build) still use Convert, unchanged.

## 0. Dossier advancement prices (separate small fix, can ship first)

- **Attributes:**
  - Raising costs the **new rating** in Good Karma. This replaces the "new rating x 2"
    placeholder in `play-sheet.html` `renderManageAttrs`.
  - The rating counted is the base plus metatype bonus. Cyberware and bioware bonuses never
    count toward the cost, as today.
  - Raises stop at the **racial maximum** (`rules.metatypes[<race>].max`, e.g. Troll Body 11).
    The button is disabled at the cap.
- **Skills:** unchanged; `shared.js` `skillKarmaCost` already matches the rules:
  - general skill: 2 x new rating;
  - Concentration: 1.5 x new rating, rounded up;
  - Specialization: 1 x new rating;
  - languages: 1 x, as now.
- Update the Manage Attributes help text (drop "illustrative cost only / placeholder").
- Tests: Manage Attributes charges the new rating and stops at the racial maximum.

## 1. What loads into the builder, and what it costs

| Part | Loaded from | Notes |
|---|---|---|
| Priorities, metatype, magic type, tradition, totem | stored build | all changeable |
| Attributes, skills | stored build (creation values) | Karma raises bought in play are refunded (section 3) |
| Spells, adept powers | **current sheet** | those learned in play are treated as bought at creation |
| Gear, cyberware, bioware, foci, programs | **current sheet** | those bought in play are treated as bought at creation |
| Contacts | current Contact records | edited in place (section 2) |
| Identity, lifestyle | stored build / sheet | all changeable |

- **Starting gear that's been used up isn't on the sheet, so it simply isn't there.** It can't
  be refunded or brought back.
- **Budgets:** the builder's normal creation budgets apply. Since play purchases now count
  toward creation budgets, a runner can load already over a budget (Resources, spell points,
  power points). Like today's edit, an overrun the runner **already had** doesn't block saving,
  as long as the edit doesn't make it worse. Removing something to get under budget always
  works.
- **Gear bought in play keeps its Dossier fields** through the round trip (equipped, rounds left,
  weapon ids, mounts, mods), so unchanged items come back exactly as they were.
- **Implant grades:** the creation check blocks Beta/Delta cyberware for players. An implant
  already on the sheet at a GM-approved grade stays allowed. Only *new* Beta/Delta lines are
  blocked, as at creation.
- **Essence, Body Index and magic rating** are recomputed by the builder from the full loadout,
  as at creation. The server's hard Essence and Body Index caps still apply.

## 2. Contacts: same records, edited in place

- **Editable:** existing contacts load into the Contacts step, fully editable (handle,
  archetype, type). Each row remembers its Contact id.
- **On save:**
  - **Changed row:** updates its Contact row (name, profession, contact_type). If it has a
    Known Persons NPC (`npc_id`), that NPC's name and archetype are updated too.
  - **Type changed** between a person type (Contact/Buddy/Follower) and Gang/Tribe: creates the
    NPC link, or unlinks it. An unlinked NPC stays as a Person of Interest.
  - **Removed row:** deletes the Contact row. Its NPC stays a Person of Interest, the same rule
    as deleting a runner.
  - **New row:** created as today.
- **Untouched:**
  - fields the builder doesn't show (connection, notes, description, location, organization);
  - contacts the GM has hidden from the player.
- **Loyalty:** changing the type sets that type's creation loyalty (Contact 1, Buddy 3,
  Follower 6), but never lowers a loyalty raised in play. An unchanged type keeps its loyalty.
- Creation contact rules (one Buddy, at most five Followers, two starting contacts) are checked
  by the builder. No extra server checks (we trust the players).

## 3. Karma: refund raises bought in play

- **What gets refunded:** attributes and skills load at their creation values, so whatever Karma
  bought the raises since creation comes back. It is priced with the section 0 rules, from the
  creation value up to the current sheet value:
  - attributes: the sum of each new rating along the way;
  - general skill: 2 x each new rating;
  - Concentration: 1.5 x each new rating, rounded up;
  - Specialization: 1 x each new rating;
  - languages: 1 x each new rating.
- **Recorded vs worked out:** where `chargen_state.advancement.karma` has a recorded spend for an
  item, the **larger** of the recorded amount and the worked-out price is refunded. The record
  only exists since 2026-11-21, so it can be partial (earlier raises unrecorded), or higher than
  today's price (attribute raises recorded at the old placeholder price).
- **Contacts the runner already had:** a contact with no stored type is shown as a Buddy (loyalty
  3+) or Follower (loyalty 6) by its loyalty. The one-Buddy / five-Follower limits allow as many
  as the runner had when loaded. Changing such a contact's type keeps all the loyalty above a
  plain Contact's 1 as raised in play.
- **Not refunded:** spells and powers learned in play, because they stay on the sheet as
  creation picks.
- **Result:** new Good Karma = current Good Karma + refund. Karma Pool keeps its current value.
  The advancement record is cleared after the refund, since the rebuilt sheet is the new
  baseline.
- **Review:** the Review screen lists each refunded item and its Karma.

## 4. Nuyen

- New nuyen = current nuyen + (new starting cash - starting cash of the build as loaded).
  Starting cash is leftover Resources at 10:1.
- So removing gear in the edit gives back its leftover-Resources value as cash, and adding gear
  costs it.
- Players or the GM fix the sheet by hand if it's out of whack.

## 5. Kept as-is

Notes, damage and condition monitors, portrait, GM approvals and flags, affiliation, reputation
and standings, Matrix runs, and deck workshop state.

## 6. Implementation outline

- **Server** (`app/routers/characters.py`, `app/schemas/character.py`):
  - The rebuild endpoint takes the full sheet, using the same creation schema as Convert,
    plus:
    - `contacts` with optional ids (edit/delete/create);
    - `karma_refund` (computed by the builder, trusted);
    - `nuyen_delta`;
    - `expected_version`.
  - It writes the sheet, applies the contact edits, and stores the new build.
  - The Beta/Delta check is relaxed for lines already on the sheet.
  - Locked-key restoring, `gear_sold` and the name+rating gear matching are removed.
- **Builder** (`frontend/character-builder.html`):
  - Edit mode loads the build plus the sheet's spells, powers, gear, foci and programs.
  - Drop the locks and step notes. Contacts carry ids.
  - Replace the "already over budget" exception with the "not worse" rule for Resources, spell
    points and power points.
  - Review lists the Karma refund per item, the nuyen change and contact changes.
- **Dossier** (`play-sheet.html`): the section 0 price fix; the Edit in Builder tooltip says
  everything is editable, Karma raises are refunded, and inventory, spells and powers carry over.

## 7. Tests

- **Server:**
  - contact rename, type change and delete hit the same records, and the NPC is updated or kept;
  - Karma and nuyen arithmetic;
  - an existing Delta implant is allowed but a new one is blocked for a player;
  - 409 on a stale version.
- **Browser:** a runner with a Wired Reflexes and a spell bought in play, plus skill raises, is
  rebuilt with a different priority split. Check:
  - the skill raises are refunded;
  - the Wired Reflexes and the spell carry over and count against budgets;
  - Reaction includes the implant;
  - removing a play-bought item frees Resources;
  - a contact is renamed in place.
- **Dossier:** the attribute raise costs the new rating and stops at the racial maximum.
