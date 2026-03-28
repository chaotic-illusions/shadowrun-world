#!/usr/bin/env python3
"""
Seed script for Shadowrun World Engine.
Reads data/world_seed.json and populates the API in dependency order.

Usage:
    python seed.py [--url http://localhost:8000] [--file data/world_seed.json]
"""

import json
import sys
import argparse
import urllib.request
import urllib.error


def post(base_url: str, path: str, payload: dict) -> dict:
    url = f"{base_url}{path}"
    data = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  ERROR {e.code} on POST {path}: {body}")
        sys.exit(1)


def seed(base_url: str, seed_file: str) -> None:
    with open(seed_file, encoding="utf-8") as f:
        data = json.load(f)

    rtg_ids: dict[str, int] = {}
    org_ids: dict[str, int] = {}
    location_ids: dict[str, int] = {}
    character_ids: dict[str, int] = {}

    # ── 0. RTGs ───────────────────────────────────────────────────────────────
    print("\n[0/8] RTGs")
    for rtg in data.get("rtgs", []):
        result = post(base_url, "/rtgs/", rtg)
        rtg_ids[rtg["code"]] = result["id"]
        print(f"  + {rtg['code']} ({rtg.get('region', '')}) -> id {result['id']}")

    # ── 1. Organizations ─────────────────────────────────────────────────────
    print("\n[1/8] Organizations")
    org_name_map: dict[str, dict] = {o["name"]: o for o in data.get("organizations", [])}

    for org in data.get("organizations", []):
        payload = {k: v for k, v in org.items() if k not in ("ally_names", "enemy_names")}
        # Ally/enemy IDs resolved after all orgs are created
        payload["ally_ids"] = []
        payload["enemy_ids"] = []
        result = post(base_url, "/organizations/", payload)
        org_ids[org["name"]] = result["id"]
        print(f"  + {org['name']} -> id {result['id']}")

    # Patch ally/enemy relationships
    for org in data.get("organizations", []):
        ally_ids = [org_ids[n] for n in org.get("ally_names", []) if n in org_ids]
        enemy_ids = [org_ids[n] for n in org.get("enemy_names", []) if n in org_ids]
        if ally_ids or enemy_ids:
            url = f"{base_url}/organizations/{org_ids[org['name']]}"
            payload = json.dumps({"ally_ids": ally_ids, "enemy_ids": enemy_ids}).encode()
            req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"}, method="PATCH")
            with urllib.request.urlopen(req):
                pass

    # ── 2. Locations ─────────────────────────────────────────────────────────
    print("\n[2/8] Locations")
    for loc in data.get("locations", []):
        payload = {k: v for k, v in loc.items() if k != "controlling_org_name"}
        org_name = loc.get("controlling_org_name")
        payload["controlling_org_id"] = org_ids.get(org_name) if org_name else None
        result = post(base_url, "/locations/", payload)
        location_ids[loc["name"]] = result["id"]
        print(f"  + {loc['name']} -> id {result['id']}")

    # ── 3. Characters ─────────────────────────────────────────────────────────
    print("\n[3/8] Characters")
    for char in data.get("characters", []):
        result = post(base_url, "/characters/", char)
        character_ids[char["name"]] = result["id"]
        print(f"  + {char['name']} ({'PC' if char.get('is_pc') else 'NPC'}) -> id {result['id']}")

    # ── 4. Contacts ──────────────────────────────────────────────────────────
    print("\n[4/8] Contacts")
    for contact in data.get("contacts", []):
        owner_name = contact.get("owner_name")
        npc_name = contact.get("npc_name")
        org_name = contact.get("organization_name")
        loc_name = contact.get("location_name")

        if owner_name not in character_ids:
            print(f"  SKIP: owner '{owner_name}' not found in created characters")
            continue

        payload = {k: v for k, v in contact.items()
                   if k not in ("owner_name", "npc_name", "organization_name", "location_name")}
        payload["owner_id"] = character_ids[owner_name]
        payload["npc_id"] = character_ids.get(npc_name) if npc_name else None
        payload["organization_id"] = org_ids.get(org_name) if org_name else None
        payload["location_id"] = location_ids.get(loc_name) if loc_name else None

        # Use npc name as contact name if no explicit name given
        if "name" not in payload:
            payload["name"] = npc_name or "Unknown"

        result = post(base_url, "/contacts/", payload)
        print(f"  + {payload['name']} (owner: {owner_name}) -> id {result['id']}")

    # ── 5. Reputation ─────────────────────────────────────────────────────────
    print("\n[5/8] Reputation")
    for rep in data.get("reputation", []):
        char_name = rep.get("character_name")
        if char_name not in character_ids:
            print(f"  SKIP: character '{char_name}' not found")
            continue
        payload = {k: v for k, v in rep.items() if k != "character_name"}
        payload["character_id"] = character_ids[char_name]
        result = post(base_url, "/reputation/", payload)
        print(f"  + Reputation for {char_name} -> id {result['id']}")

    # ── 6. Org Standings ─────────────────────────────────────────────────────
    print("\n[6/8] Org Standings")
    for standing in data.get("org_standings", []):
        char_name = standing.get("character_name")
        org_name = standing.get("org_name")
        if char_name not in character_ids or org_name not in org_ids:
            print(f"  SKIP: '{char_name}' or '{org_name}' not found")
            continue
        payload = {
            "character_id": character_ids[char_name],
            "organization_id": org_ids[org_name],
            "standing": standing.get("standing", 0),
            "notes": standing.get("notes"),
        }
        result = post(base_url, "/reputation/standings", payload)
        print(f"  + {char_name} <-> {org_name} (standing {payload['standing']}) -> id {result['id']}")

    # ── 7. House Rules ────────────────────────────────────────────────────────
    print("\n[7/8] House Rules")
    for rule in data.get("house_rules", []):
        result = post(base_url, "/house-rules/", rule)
        print(f"  + {rule['title']} -> id {result['id']}")

    # ── 8. Adventure Logs ─────────────────────────────────────────────────────
    print("\n[8/8] Adventure Logs")
    for log in data.get("adventure_logs", []):
        payload = {k: v for k, v in log.items()
                   if k not in ("participant_names", "location_names", "org_names")}
        payload["participant_ids"] = [character_ids[n] for n in log.get("participant_names", []) if n in character_ids]
        payload["location_ids"] = [location_ids[n] for n in log.get("location_names", []) if n in location_ids]
        payload["org_ids"] = [org_ids[n] for n in log.get("org_names", []) if n in org_ids]
        result = post(base_url, "/runs/", payload)
        print(f"  + {log['title']} -> id {result['id']}")

    print("\nDone. World data seeded successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed the Shadowrun World Engine API")
    parser.add_argument("--url", default="http://localhost:8000", help="Base API URL")
    parser.add_argument("--file", default="data/world_seed.json", help="Path to seed JSON file")
    args = parser.parse_args()

    print(f"Seeding {args.file} -> {args.url}")
    seed(args.url, args.file)
