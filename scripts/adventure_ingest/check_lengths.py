"""Report spec string fields that exceed the API's max_length limits (dry runs do not catch these).

Usage: python scripts/adventure_ingest/check_lengths.py <slug>
"""
import importlib
import sys

LIMITS = {
    "org": {"name": 200, "org_type": 100, "headquarters": 200, "affiliation_contact_type": 50},
    "location": {"name": 200, "location_type": 100, "city": 100, "district": 100, "security_level": 50},
    "npc": {"name": 200, "archetype": 100, "title": 200, "race": 50, "nationality": 100, "gender": 50},
}


def main() -> None:
    slug = sys.argv[1]
    spec = importlib.import_module(f"scripts.adventure_ingest.specs.{slug}")
    bad = 0
    for kind, rows in (("org", spec.ORGS), ("location", spec.LOCATIONS), ("npc", spec.NPCS)):
        for row in rows:
            for field, limit in LIMITS[kind].items():
                val = row.get(field)
                if isinstance(val, str) and len(val) > limit:
                    bad += 1
                    print(f"{kind} {row['name']!r}: {field} is {len(val)} chars (max {limit})")
    for kind, updates in (("org", spec.ORG_UPDATES), ("location", spec.LOC_UPDATES), ("npc", spec.NPC_UPDATES)):
        for name, upd in updates.items():
            for field, val in (upd.get("set") or {}).items():
                limit = LIMITS[kind].get(field)
                if limit and isinstance(val, str) and len(val) > limit:
                    bad += 1
                    print(f"{kind} update {name!r}: set.{field} is {len(val)} chars (max {limit})")
    for s in ("ADVENTURE",):
        if len(getattr(spec, s)) > 100:
            bad += 1
            print(f"{s} longer than 100 chars")
    print("OK" if not bad else f"{bad} overlong field(s)")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    sys.path.insert(0, ".")
    main()
