"""Regenerate docs/adventure-analysis/baseline-counts.md from the ingest specs.

Usage (repo root): python docs/adventure-analysis/tools/baseline_counts.py
"""
import glob
import importlib
import os
import re
import statistics as st
import sys

sys.path.insert(0, ".")
rows = []
for f in glob.glob("scripts/adventure_ingest/specs/*.py"):
    slug = os.path.basename(f)[:-3]
    if slug.startswith("_"):
        continue
    m = importlib.import_module(f"scripts.adventure_ingest.specs.{slug}")
    beats = m.TIMELINE.count("\n- ") + m.TIMELINE.count("\n* ")
    yr = re.match(r"\d{4}(-\d{4})?", m.YEAR)
    yr = yr.group(0) if yr else m.YEAR[:9]
    updates = len(m.NPC_UPDATES) + len(m.LOC_UPDATES) + len(m.ORG_UPDATES)
    rows.append((m.ORDER, m.ADVENTURE, yr, len(m.NPCS), len(m.LOCATIONS), len(m.ORGS), updates, beats, slug))
rows.sort()
out = [
    "# Baseline counts per adventure (auto-generated from the ingest specs)",
    "",
    "Counts are rows CREATED in the world database by each adventure's spec, plus appends to rows that "
    "already existed (\"Updates\"). \"Timeline beats\" is the number of bullets in the spec's TIMELINE, a "
    "rough proxy for the number of story beats the summary tracked, not the book's act count. Regenerate "
    "with docs/adventure-analysis/tools/baseline_counts.py.",
    "",
    "| # | Adventure | Year | NPCs | Locs | Orgs | Updates | Timeline beats | Spec / prep doc |",
    "|---|---|---|---|---|---|---|---|---|",
]
out += ["| " + " | ".join(str(x) for x in r) + " |" for r in rows]
n = len(rows)
out += [
    "",
    f"Totals across {n} adventures: NPCs {sum(r[3] for r in rows)}, locations {sum(r[4] for r in rows)}, "
    f"orgs {sum(r[5] for r in rows)}.",
    f"Medians: NPCs {st.median(r[3] for r in rows):.0f}, locations {st.median(r[4] for r in rows):.0f}, "
    f"orgs {st.median(r[5] for r in rows):.0f}, timeline beats {st.median(r[7] for r in rows):.0f}.",
]
with open("docs/adventure-analysis/baseline-counts.md", "w", encoding="ascii") as fh:
    fh.write("\n".join(out) + "\n")
print(out[-2])
print(out[-1])
