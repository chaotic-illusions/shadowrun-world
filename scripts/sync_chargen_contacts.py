"""Make every runner's contacts say the same thing everywhere: Dossier, Known Persons and builder.

A runner's contacts live in the ``contacts`` table (what the Dossier shows); each individual
contact (Contact/Buddy/Follower) links (npc_id) to an NPC "person of interest" in Known Persons,
whose ``origin_pc_id`` points back at the runner, while Gang/Tribe contacts have no NPC. The
builder also keeps its own snapshot of the list in ``characters.chargen_state.contacts``.

Fixes (with --apply; a dry run otherwise):
  1. A contact row whose name/profession differs from its NPC's name/archetype takes the NPC's.
     Known Persons is where a contact is edited, and edits there have copied onto the contact row
     since 2026-10-01 -- older ones didn't.
  2. Each finished, builder-made runner's chargen_state.contacts := its contact rows (after 1).
     The snapshot drifted on older runners (contacts renamed or added on the Dossier later).
Reports (never changes -- needs a person to decide):
  - an individual contact with no NPC, or linked to a missing NPC or another runner's
  - an NPC that names a runner (origin_pc_id) but no contact of that runner points at it

Writes are guarded: a row is only updated if it still holds exactly what was read. Character rows
get their optimistic-lock version bumped so an open Dossier/builder tab can't write a stale copy.

Usage:  python scripts/sync_chargen_contacts.py <path/to/shadowrun.db> [--apply]
"""
import json
import sqlite3
import sys

PERSON_TYPES = {None, "", "Contact", "Buddy", "Follower"}


def type_for_loyalty(loyalty):   # mirrors app/routers/contacts.contact_type_for_loyalty
    loyalty = loyalty or 1
    return "Follower" if loyalty >= 6 else "Buddy" if loyalty >= 3 else "Contact"


def main(path, apply):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    problems, row_fixes, list_fixes = [], [], []
    pcs = db.execute("SELECT id, name, is_draft, chargen_state FROM characters WHERE is_pc = 1 ORDER BY id").fetchall()
    pc_ids = {r["id"] for r in pcs}

    for pc in pcs:
        contacts = []
        for c in db.execute("SELECT * FROM contacts WHERE owner_id = ? ORDER BY id", (pc["id"],)):
            c = dict(c)
            label = f'{pc["name"]} (#{pc["id"]}) contact "{c["name"]}"'
            if c["contact_type"] in PERSON_TYPES:
                npc = (db.execute("SELECT id, name, archetype, origin_pc_id FROM characters WHERE id = ?",
                                  (c["npc_id"],)).fetchone() if c["npc_id"] is not None else None)
                if c["npc_id"] is None:
                    problems.append(f"{label}: no Known Persons profile (NPC)")
                elif npc is None:
                    problems.append(f'{label}: links to missing NPC #{c["npc_id"]}')
                elif npc["origin_pc_id"] not in (None, pc["id"]):
                    problems.append(f'{label}: NPC #{npc["id"]} belongs to runner #{npc["origin_pc_id"]}')
                elif (c["name"], c["profession"] or "") != (npc["name"], npc["archetype"] or ""):
                    row_fixes.append((pc, dict(c), npc))
                    c["name"], c["profession"] = npc["name"], npc["archetype"]
            contacts.append(c)

        state = json.loads(pc["chargen_state"] or "{}")
        if pc["is_draft"] or not (state.get("prio") or {}):
            continue   # drafts have no rows yet; pre-wizard runners have no builder list
        snapshot = [{"name": c["name"] or "", "archetype": c["profession"] or "",
                     "type": c["contact_type"] or type_for_loyalty(c["loyalty"])} for c in contacts]
        if state.get("contacts") != snapshot:
            list_fixes.append((pc, state, snapshot))

    linked = {r[0] for r in db.execute("SELECT npc_id FROM contacts WHERE npc_id IS NOT NULL")}
    for npc in db.execute("SELECT id, name, origin_pc_id FROM characters WHERE is_pc = 0 AND origin_pc_id IS NOT NULL"):
        if npc["origin_pc_id"] not in pc_ids:
            problems.append(f'NPC "{npc["name"]}" (#{npc["id"]}): origin runner #{npc["origin_pc_id"]} no longer exists')
        elif npc["id"] not in linked:
            problems.append(f'NPC "{npc["name"]}" (#{npc["id"]}): names runner #{npc["origin_pc_id"]} but no contact points at it')

    skipped = 0
    print(f"1. Dossier entries that disagree with Known Persons: {len(row_fixes)}")
    for pc, c, npc in row_fixes:
        print(f'  - {pc["name"]}: "{c["name"]}" / "{c["profession"] or ""}" -> "{npc["name"]}" / "{npc["archetype"] or ""}"')
        if apply:
            cur = db.execute(
                "UPDATE contacts SET name = ?, profession = ? WHERE id = ? AND name IS ? AND profession IS ?",
                (npc["name"], npc["archetype"], c["id"], c["name"], c["profession"]))
            skipped += cur.rowcount != 1

    print(f"\n2. Builder contact lists out of step with the records: {len(list_fixes)}")
    for pc, state, snapshot in list_fixes:
        before = [c.get("name") for c in state.get("contacts") or [] if (c.get("name") or "").strip()]
        print(f'  - {pc["name"]} (#{pc["id"]}): {before} -> {[c["name"] for c in snapshot]}')
        if apply:
            state["contacts"] = snapshot
            cur = db.execute(
                "UPDATE characters SET chargen_state = ?, version = version + 1 WHERE id = ? AND chargen_state = ?",
                (json.dumps(state), pc["id"], pc["chargen_state"]))
            skipped += cur.rowcount != 1

    print("\nNeeds a person (not changed):" if problems else "\nLinks: every individual contact has its profile, and every profile its contact.")
    for p in problems:
        print("  -", p)

    if not apply:
        print("\nDry run -- rerun with --apply to write." if row_fixes or list_fixes else "\nNothing to fix.")
    elif skipped:
        db.rollback()
        print(f"\nROLLED BACK: {skipped} row(s) changed since they were read -- rerun.")
    else:
        db.commit()
        print("\nApplied." if row_fixes or list_fixes else "\nNothing to fix.")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--apply"]
    if len(args) != 1:
        sys.exit(__doc__)
    main(args[0], "--apply" in sys.argv)
