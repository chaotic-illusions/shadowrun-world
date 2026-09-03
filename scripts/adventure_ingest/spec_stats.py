"""Print depth metrics for one or more specs: python scripts/adventure_ingest/spec_stats.py slug [slug...]"""
import importlib
import sys

sys.path.insert(0, ".")
for slug in sys.argv[1:]:
    m = importlib.import_module(f"scripts.adventure_ingest.specs.{slug}")
    npcs, locs = m.NPCS, m.LOCATIONS
    avg = lambda rows, k: int(sum(len(r.get(k) or "") for r in rows) / max(len(rows), 1))
    print(
        f"{slug}: npcs {len(npcs)} locs {len(locs)} orgs {len(m.ORGS)} | npc desc {avg(npcs,'description')} "
        f"bg {avg(npcs,'background')} notes {avg(npcs,'notes')} | with bg {sum(1 for n in npcs if n.get('background'))}/{len(npcs)} "
        f"| loc desc {avg(locs,'description')} | org desc {avg(m.ORGS,'description')} | updates {len(m.ORG_UPDATES)}/{len(m.LOC_UPDATES)}/{len(m.NPC_UPDATES)}"
    )
