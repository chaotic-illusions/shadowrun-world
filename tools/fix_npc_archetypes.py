#!/usr/bin/env python3
"""
One-off data-correction script: rewrites NPC archetype values that predate the
unified contact/NPC archetype catalog (see app/data/catalog/builder.json's
contact_archetypes) onto their correct catalog entries, and ensures two new
archetypes (Corporate Executive, Corporate Wage Slave) exist in the catalog.

Idempotent and safe to run against any environment (local or production) more
than once: catalog additions tolerate an already-exists 409, and each NPC
rename is guarded by an expected *current* value -- if an NPC's archetype has
already been fixed, or was independently changed to something else, the script
skips it and reports why rather than clobbering it.

Usage:
    python tools/fix_npc_archetypes.py --url http://localhost:8000 --admin-token <token>
    python tools/fix_npc_archetypes.py --url https://your-live-host --admin-token <token>
"""

import argparse
import httpx

NEW_ARCHETYPES = [
    ("Corporate Executive", "Corporate"),
    ("Corporate Wage Slave", "Corporate"),
]

# (npc name, expected current archetype, corrected archetype)
RENAMES = [
    ('"Blade" Kowalski',        "Ganger",             "Gang Member"),
    ("J0k3r",                   "Ganger",              "Gang Member"),
    ("Red Phoenix",             "Ganger",              "Gang Member"),
    ("Cedric 'Big C' Felton",   "Beat Cop",            "Street Cop"),
    ("Lt. Sonya Vasquez",       "Corporate Security",  "Corporate Security Guard"),
    ("Hana Mori",               "Decker",              "Corporate Decker"),
    ("Sister Ixtli",            "Shaman",              "Tribal Shaman"),
    ("Councilman Derek Walsh",  "Face",                "City Official"),
    ("Marisol",                 "Wage Slave",          "Corporate Wage Slave"),
]


def add_archetypes(client):
    print("\n[1/2] Catalog additions")
    for name, group in NEW_ARCHETYPES:
        try:
            resp = client.post("/catalog/contact-archetypes", json={"name": name, "group": group})
            if resp.status_code == 201:
                print(f"  + added {name!r} to {group}")
            elif resp.status_code == 409:
                print(f"  = {name!r} already in catalog, skipping")
            else:
                resp.raise_for_status()
        except httpx.HTTPStatusError as e:
            print(f"  ! ERROR {e.response.status_code} adding {name!r}: {e.response.text}")


def rename_npcs(client):
    print("\n[2/2] NPC archetype renames")
    npcs = client.get("/characters/").raise_for_status().json()
    by_name = {c["name"]: c for c in npcs if not c.get("is_pc")}

    for name, expected_old, new in RENAMES:
        char = by_name.get(name)
        if char is None:
            print(f"  ? {name!r} not found (not in this environment), skipping")
            continue
        current = char.get("archetype")
        if current == new:
            print(f"  = {name!r} already {new!r}, skipping")
            continue
        if current != expected_old:
            print(f"  ! {name!r} archetype is {current!r}, not the expected {expected_old!r} -- skipping (check manually)")
            continue
        resp = client.patch(f"/characters/{char['id']}", json={"archetype": new})
        if resp.status_code == 200:
            print(f"  ~ {name!r}: {expected_old!r} -> {new!r}")
        else:
            print(f"  ! ERROR {resp.status_code} updating {name!r}: {resp.text}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://localhost:8000")
    parser.add_argument("--admin-token", required=True)
    args = parser.parse_args()

    headers = {"X-Admin-Token": args.admin_token}
    with httpx.Client(base_url=args.url, headers=headers, timeout=30.0) as client:
        add_archetypes(client)
        rename_npcs(client)
    print("\nDone.")


if __name__ == "__main__":
    main()
