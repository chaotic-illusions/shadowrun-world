#!/usr/bin/env python3
"""
Seed script for Shadowrun World Engine.
Reads data/world_seed.json and populates the API in dependency order.

Usage:
    python seed.py [--url http://localhost:8000] [--file data/world_seed.json] [--admin-token <token>]
    python seed.py --upsert-rtgs-only [--url http://localhost:8000] [--file data/world_seed.json] [--admin-token <token>]
"""

import json
import os
import argparse
import httpx


ADMIN_PASSWORD = os.environ.get("BOOTSTRAP_ADMIN_KEY", "shadowrunner")


def post(client, path, payload):
    try:
        resp = client.post(path, json=payload)
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"ERROR {e.response.status_code} on POST {path}: {e.response.text}") from e
    except httpx.RequestError as e:
        raise RuntimeError(f"Connection failed for POST {path}: {e}") from e


def patch(client, path, payload):
    try:
        resp = client.patch(path, json=payload)
        resp.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"ERROR {e.response.status_code} on PATCH {path}: {e.response.text}") from e
    except httpx.RequestError as e:
        raise RuntimeError(f"Connection failed for PATCH {path}: {e}") from e


def get_json(client, path, params=None):
    try:
        resp = client.get(path, params=params)
        resp.raise_for_status()
        return resp.json()
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"ERROR {e.response.status_code} on GET {path}: {e.response.text}") from e
    except httpx.RequestError as e:
        raise RuntimeError(f"Connection failed for GET {path}: {e}") from e


def upsert_rtgs(client, data, rtg_ids):
    print("\n[0/7] RTGs")
    existing_rtgs = get_json(client, "/rtgs/")
    existing_by_code = {r.get("code"): r for r in existing_rtgs if r.get("code")}

    for rtg in data.get("rtgs", []):
        code = rtg["code"]
        existing = existing_by_code.get(code)
        if existing:
            patch(client, f"/rtgs/{existing['id']}", rtg)
            rtg_ids[code] = existing["id"]
            print(f"  ~ {code} ({rtg.get('region', '')}) -> updated id {existing['id']}")
            continue

        result = post(client, "/rtgs/", rtg)
        rtg_ids[code] = result["id"]
        print(f"  + {code} ({rtg.get('region', '')}) -> id {result['id']}")


def seed(base_url, seed_file, admin_token=None, upsert_rtgs_only=False):
    with open(seed_file, encoding="utf-8-sig") as f:
        data = json.load(f)

    rtg_ids = {}
    org_ids = {}
    location_ids = {}
    character_ids = {}

    token = admin_token or ADMIN_PASSWORD
    headers = {"X-Admin-Token": token}
    with httpx.Client(base_url=base_url, headers=headers, timeout=30.0) as client:
        if upsert_rtgs_only:
            upsert_rtgs(client, data, rtg_ids)
            print("\nDone. RTGs upserted successfully.")
            return
        _seed_data(client, data, rtg_ids, org_ids, location_ids, character_ids)


def _seed_data(client, data, rtg_ids, org_ids, location_ids, character_ids):
    upsert_rtgs(client, data, rtg_ids)

    print("\n[1/7] Organizations")
    for org in data.get("organizations", []):
        payload = {k: v for k, v in org.items() if k not in ("ally_names", "enemy_names")}
        payload["ally_ids"] = []
        payload["enemy_ids"] = []
        result = post(client, "/organizations/", payload)
        org_ids[org["name"]] = result["id"]
        print(f"  + {org['name']} -> id {result['id']}")

    for org in data.get("organizations", []):
        ally_ids = [org_ids[n] for n in org.get("ally_names", []) if n in org_ids]
        enemy_ids = [org_ids[n] for n in org.get("enemy_names", []) if n in org_ids]
        if ally_ids or enemy_ids:
            patch(client, f"/organizations/{org_ids[org['name']]}", {"ally_ids": ally_ids, "enemy_ids": enemy_ids})

    print("\n[2/7] Locations")
    for loc in data.get("locations", []):
        payload = {k: v for k, v in loc.items() if k != "controlling_org_name"}
        org_name = loc.get("controlling_org_name")
        payload["controlling_org_id"] = org_ids.get(org_name) if org_name else None
        result = post(client, "/locations/", payload)
        location_ids[loc["name"]] = result["id"]
        print(f"  + {loc['name']} -> id {result['id']}")

    print("\n[3/7] Characters")
    for char in data.get("characters", []):
        rep_data = char.pop("reputation", None)
        org_name = char.pop("organization_name", None)
        char["organization_id"] = org_ids.get(org_name) if org_name else None
        result = post(client, "/characters/", char)
        char_id = result["id"]
        character_ids[char["name"]] = char_id
        print(f"  + {char['name']} ({'PC' if char.get('is_pc') else 'NPC'}) -> id {char_id}")
        if rep_data is not None:
            rep_payload = dict(rep_data, character_id=char_id)
            rep_result = post(client, "/reputation/", rep_payload)
            print(f"    + reputation -> id {rep_result['id']}")

    print("\n[4/7] Contacts")
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

        if "name" not in payload:
            payload["name"] = npc_name or "Unknown"

        result = post(client, "/contacts/", payload)
        print(f"  + {payload['name']} (owner: {owner_name}) -> id {result['id']}")

    print("\n[5/7] Org Standings")
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
        result = post(client, "/reputation/standings", payload)
        print(f"  + {char_name} <-> {org_name} (standing {payload['standing']}) -> id {result['id']}")

    print("\n[6/6] Adventure Logs")
    for log in data.get("adventure_logs", []):
        payload = {k: v for k, v in log.items()
                   if k not in ("participant_names", "location_names", "org_names")}
        payload["participant_ids"] = [character_ids[n] for n in log.get("participant_names", []) if n in character_ids]
        payload["location_ids"] = [location_ids[n] for n in log.get("location_names", []) if n in location_ids]
        payload["org_ids"] = [org_ids[n] for n in log.get("org_names", []) if n in org_ids]
        result = post(client, "/runs/", payload)
        print(f"  + {log['title']} -> id {result['id']}")

    print("\nDone. World data seeded successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed the Shadowrun World Engine API")
    parser.add_argument("--url", default="http://localhost:8000", help="Base API URL")
    parser.add_argument("--file", default="data/world_seed.json", help="Path to seed JSON file")
    parser.add_argument(
        "--admin-token",
        default=None,
        help="Admin token/password for authenticated API calls (defaults to BOOTSTRAP_ADMIN_KEY env var)",
    )
    parser.add_argument(
        "--upsert-rtgs-only",
        action="store_true",
        help="Only upsert RTGs by code (non-destructive). Useful for applying RTG updates to an existing world DB.",
    )
    args = parser.parse_args()

    print(f"Seeding {args.file} -> {args.url}")
    try:
        seed(args.url, args.file, args.admin_token, upsert_rtgs_only=args.upsert_rtgs_only)
    except RuntimeError as e:
        print(f"  {e}")
        raise SystemExit(1) from e
