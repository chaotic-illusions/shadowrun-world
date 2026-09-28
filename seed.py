#!/usr/bin/env python3
"""
Seed script for Shadowrun World Engine.
Reads data/world_seed.json and populates the API in dependency order.

Usage:
    python seed.py [--url http://localhost:8000] [--file data/world_seed.json] [--admin-token <token>]
    python seed.py --upsert-rtgs-only [--url http://localhost:8000] [--file data/world_seed.json] [--admin-token <token>]
    python seed.py --export-db data/shadowrun_prod.db [--file data/world_seed.json]
"""

import argparse
import hashlib
import json
import os
import sqlite3
from pathlib import Path

import httpx

from app.schemas.adventure_log import AdventureLogCreate
from app.schemas.character import CharacterCreate
from app.schemas.location import LocationCreate
from app.schemas.matrix_host import MatrixHostCreate
from app.schemas.organization import OrganizationCreate, OrganizationDivision
from app.schemas.reputation import ReputationCreate
from app.schemas.rtg import RTGCreate


_ORG_RELATION_NAMES = {
    "ally_ids": "ally_names",
    "enemy_ids": "enemy_names",
    "revealed_ally_ids": "revealed_ally_names",
    "revealed_enemy_ids": "revealed_enemy_names",
}


def _decode_json_fields(values, fields):
    result = dict(values)
    for field in fields:
        value = result.get(field)
        if isinstance(value, str):
            result[field] = json.loads(value)
    return result


def _schema_payload(row, schema, json_fields=()):
    values = {field: row[field] for field in schema.model_fields if field in row.keys()}
    values = _decode_json_fields(values, json_fields)
    return schema.model_validate(values).model_dump(mode="json")


def _names_for_ids(ids, names_by_id, label):
    missing = [identifier for identifier in ids if identifier not in names_by_id]
    if missing:
        raise RuntimeError(f"Unknown {label} IDs: {missing}")
    return [names_by_id[identifier] for identifier in ids]


def _ids_for_names(names, ids_by_name, label):
    missing = [name for name in names if name not in ids_by_name]
    if missing:
        raise RuntimeError(f"Unknown {label} names: {missing}")
    return [ids_by_name[name] for name in names]


def _export_leadership(entries, npc_names_by_id):
    result = []
    for raw in entries or []:
        entry = dict(raw)
        character_id = entry.pop("character_id", None)
        if character_id in npc_names_by_id:
            entry["character_name"] = npc_names_by_id[character_id]
        result.append(entry)
    return result


def _export_division(division, org_names_by_id, npc_names_by_id):
    result = OrganizationDivision.model_validate(division).model_dump(mode="json")
    result["leadership"] = _export_leadership(result.get("leadership"), npc_names_by_id)
    for id_field, name_field in _ORG_RELATION_NAMES.items():
        result[name_field] = _names_for_ids(
            result.pop(id_field, []), org_names_by_id, f"division {name_field}"
        )
    return result


def _resolve_leadership(entries, character_ids):
    result = []
    for raw in entries or []:
        entry = dict(raw)
        character_name = entry.pop("character_name", None)
        if character_name:
            entry["character_id"] = _ids_for_names(
                [character_name], character_ids, "leadership character"
            )[0]
        result.append(entry)
    return result


def _resolve_division(division, org_ids, character_ids):
    result = dict(division)
    result["leadership"] = _resolve_leadership(
        result.get("leadership"), character_ids
    )
    for id_field, name_field in _ORG_RELATION_NAMES.items():
        result[id_field] = _ids_for_names(
            result.pop(name_field, []), org_ids, f"division {name_field}"
        )
    return OrganizationDivision.model_validate(result).model_dump(mode="json")


def export_world_data(database_path):
    """Return a portable, PC-free world seed from an existing SQLite database."""
    path = Path(database_path).resolve()
    uri = f"file:{path.as_posix()}?mode=ro&immutable=1"
    with sqlite3.connect(uri, uri=True) as database:
        database.row_factory = sqlite3.Row
        database.execute("PRAGMA query_only=ON")
        if database.execute("PRAGMA integrity_check").fetchone()[0] != "ok":
            raise RuntimeError("Source database integrity check failed")
        if database.execute("PRAGMA foreign_key_check").fetchall():
            raise RuntimeError("Source database has foreign-key violations")

        org_names_by_id = dict(database.execute("SELECT id, name FROM organizations"))
        location_names_by_id = dict(database.execute("SELECT id, name FROM locations"))
        npc_names_by_id = dict(database.execute(
            "SELECT id, name FROM characters WHERE is_pc = 0"
        ))
        host_names_by_id = dict(database.execute("SELECT id, name FROM matrix_hosts"))

        rtgs = [
            _schema_payload(row, RTGCreate)
            for row in database.execute("SELECT * FROM rtgs ORDER BY id")
        ]

        organizations = []
        for row in database.execute("SELECT * FROM organizations ORDER BY id"):
            payload = _schema_payload(
                row,
                OrganizationCreate,
                {
                    "leadership", "divisions", "ltgs", "ally_ids", "enemy_ids",
                    "revealed_ally_ids", "revealed_enemy_ids",
                },
            )
            payload["leadership"] = _export_leadership(
                payload.get("leadership"), npc_names_by_id
            )
            payload["divisions"] = [
                _export_division(division, org_names_by_id, npc_names_by_id)
                for division in payload.get("divisions", [])
            ]
            for id_field, name_field in _ORG_RELATION_NAMES.items():
                payload[name_field] = _names_for_ids(
                    payload.pop(id_field, []), org_names_by_id, name_field
                )
            organizations.append(payload)

        locations = []
        for row in database.execute("SELECT * FROM locations ORDER BY id"):
            payload = _schema_payload(row, LocationCreate)
            controlling_org_id = payload.pop("controlling_org_id", None)
            payload["controlling_org_name"] = (
                org_names_by_id[controlling_org_id] if controlling_org_id else None
            )
            locations.append(payload)

        reputations = {
            row["character_id"]: _schema_payload(row, ReputationCreate)
            for row in database.execute(
                "SELECT reputations.* FROM reputations "
                "JOIN characters ON characters.id = reputations.character_id "
                "WHERE characters.is_pc = 0 ORDER BY reputations.id"
            )
        }
        characters = []
        for row in database.execute(
            "SELECT * FROM characters WHERE is_pc = 0 ORDER BY id"
        ):
            payload = _schema_payload(
                row,
                CharacterCreate,
                {"contact_skills", "priorities", "skills", "spells", "adept_powers", "gear"},
            )
            payload.pop("owner_token", None)
            organization_id = payload.pop("organization_id", None)
            payload["organization_name"] = (
                org_names_by_id[organization_id] if organization_id else None
            )
            reputation = reputations.get(row["id"])
            if reputation:
                reputation.pop("character_id", None)
                payload["reputation"] = reputation
            characters.append(payload)

        contacts = []
        for row in database.execute(
            "SELECT contacts.* FROM contacts "
            "JOIN characters owner ON owner.id = contacts.owner_id "
            "WHERE owner.is_pc = 0 ORDER BY contacts.id"
        ):
            payload = dict(row)
            for field in ("id", "owner_id", "npc_id", "organization_id", "location_id"):
                payload.pop(field, None)
            payload["owner_name"] = npc_names_by_id[row["owner_id"]]
            payload["npc_name"] = npc_names_by_id.get(row["npc_id"])
            payload["organization_name"] = org_names_by_id.get(row["organization_id"])
            payload["location_name"] = location_names_by_id.get(row["location_id"])
            contacts.append(payload)

        org_standings = []
        for row in database.execute(
            "SELECT org_standings.* FROM org_standings "
            "JOIN characters ON characters.id = org_standings.character_id "
            "WHERE characters.is_pc = 0 ORDER BY org_standings.id"
        ):
            org_standings.append({
                "character_name": npc_names_by_id[row["character_id"]],
                "org_name": org_names_by_id[row["organization_id"]],
                "standing": row["standing"],
                "standings_updated_at": row["standings_updated_at"],
                "standings_stamped_tick": row["standings_stamped_tick"],
                "notes": row["notes"],
            })

        matrix_hosts = []
        for row in database.execute("SELECT * FROM matrix_hosts ORDER BY id"):
            payload = _schema_payload(
                row,
                MatrixHostCreate,
                {"config_json", "topology_json", "trap_doors_json"},
            )
            owner_org_id = payload.pop("owner_org_id", None)
            location_id = payload.pop("location_id", None)
            payload["owner_org_name"] = org_names_by_id.get(owner_org_id)
            payload["location_name"] = location_names_by_id.get(location_id)
            doors = []
            for raw_door in payload.get("trap_doors_json") or []:
                door = dict(raw_door)
                destination_id = door.pop("destination_host_id", None)
                door["destination_host_name"] = host_names_by_id.get(destination_id)
                doors.append(door)
            payload["trap_doors"] = doors
            payload.pop("trap_doors_json", None)
            matrix_hosts.append(payload)

        adventure_logs = []
        for row in database.execute("SELECT * FROM adventure_logs ORDER BY id"):
            payload = _schema_payload(
                row,
                AdventureLogCreate,
                {"outcome_tags", "consequences_active", "changes_applied", "changes_excluded"},
            )
            log_id = row["id"]
            payload.pop("participant_ids", None)
            payload.pop("location_ids", None)
            payload.pop("org_ids", None)
            payload["participant_names"] = [
                npc_names_by_id[character_id]
                for (character_id,) in database.execute(
                    "SELECT character_id FROM log_characters WHERE log_id = ? ORDER BY character_id",
                    (log_id,),
                )
                if character_id in npc_names_by_id
            ]
            payload["location_names"] = [
                location_names_by_id[location_id]
                for (location_id,) in database.execute(
                    "SELECT location_id FROM log_locations WHERE log_id = ? ORDER BY location_id",
                    (log_id,),
                )
            ]
            payload["org_names"] = [
                org_names_by_id[organization_id]
                for (organization_id,) in database.execute(
                    "SELECT organization_id FROM log_organizations WHERE log_id = ? ORDER BY organization_id",
                    (log_id,),
                )
            ]
            adventure_logs.append(payload)

        campaign_row = database.execute(
            "SELECT current_tick, enabled_books FROM campaign_state WHERE id = 1"
        ).fetchone()
        campaign_state = {
            "current_tick": campaign_row["current_tick"] if campaign_row else 0,
            "enabled_books": json.loads(campaign_row["enabled_books"] or "[]")
            if campaign_row else [],
        }
        if database.total_changes:
            raise RuntimeError("World export unexpectedly modified the source database")

    return {
        "_format_version": 2,
        "_comment": "Portable PC-free world seed generated from the verified production snapshot.",
        "_source_database_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "_excluded": [
            "player characters",
            "PC-owned contacts",
            "PC reputations",
            "PC organization standings",
            "PC adventure-log participant links",
            "authentication tokens",
            "transient Matrix runs",
        ],
        "campaign_state": campaign_state,
        "rtgs": rtgs,
        "organizations": organizations,
        "locations": locations,
        "characters": characters,
        "contacts": contacts,
        "org_standings": org_standings,
        "matrix_hosts": matrix_hosts,
        "adventure_logs": adventure_logs,
    }


def write_world_seed(database_path, seed_file):
    output = Path(seed_file)
    data = export_world_data(database_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(data, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return data


def resolve_admin_token(admin_token=None):
    token = (admin_token or os.environ.get("BOOTSTRAP_ADMIN_KEY", "")).strip()
    if not token:
        raise RuntimeError(
            "Admin credential required: pass --admin-token or set BOOTSTRAP_ADMIN_KEY"
        )
    return token


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


def put(client, path, payload):
    try:
        resp = client.put(path, json=payload)
        resp.raise_for_status()
        return resp.json() if resp.content else None
    except httpx.HTTPStatusError as e:
        raise RuntimeError(f"ERROR {e.response.status_code} on PUT {path}: {e.response.text}") from e
    except httpx.RequestError as e:
        raise RuntimeError(f"Connection failed for PUT {path}: {e}") from e


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
    print("\n[0/9] RTGs")
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
    token = resolve_admin_token(admin_token)
    with open(seed_file, encoding="utf-8-sig") as f:
        data = json.load(f)

    rtg_ids = {}
    org_ids = {}
    location_ids = {}
    character_ids = {}

    headers = {"X-Admin-Token": token}
    with httpx.Client(base_url=base_url, headers=headers, timeout=30.0) as client:
        if upsert_rtgs_only:
            upsert_rtgs(client, data, rtg_ids)
            print("\nDone. RTGs upserted successfully.")
            return
        _seed_data(client, data, rtg_ids, org_ids, location_ids, character_ids)


def _seed_data(client, data, rtg_ids, org_ids, location_ids, character_ids):
    upsert_rtgs(client, data, rtg_ids)

    # Archetype -> suggested contact-skill list (GM-editable catalog; see /catalog/rules).
    # NPCs below already carry hand-written, flavorful contact_skills, so this only ever
    # fills in a sane default for an NPC entry that omits contact_skills entirely.
    starter_skills = get_json(client, "/catalog/rules").get("archetype_starter_skills", {})

    print("\n[1/9] Organizations")
    for org in data.get("organizations", []):
        payload = {
            k: v for k, v in org.items()
            if k not in (*_ORG_RELATION_NAMES.values(), "leadership", "divisions")
        }
        payload["ally_ids"] = []
        payload["enemy_ids"] = []
        payload["revealed_ally_ids"] = []
        payload["revealed_enemy_ids"] = []
        payload["leadership"] = []
        payload["divisions"] = []
        result = post(client, "/organizations/", payload)
        org_ids[org["name"]] = result["id"]
        print(f"  + {org['name']} -> id {result['id']}")

    print("\n[2/9] Locations")
    for loc in data.get("locations", []):
        payload = {k: v for k, v in loc.items() if k != "controlling_org_name"}
        org_name = loc.get("controlling_org_name")
        payload["controlling_org_id"] = org_ids.get(org_name) if org_name else None
        result = post(client, "/locations/", payload)
        location_ids[loc["name"]] = result["id"]
        print(f"  + {loc['name']} -> id {result['id']}")

    print("\n[3/9] Characters")
    for configured in data.get("characters", []):
        char = dict(configured)
        rep_data = char.pop("reputation", None)
        org_name = char.pop("organization_name", None)
        char["organization_id"] = _ids_for_names(
            [org_name], org_ids, "character organization"
        )[0] if org_name else None
        if not char.get("is_pc") and "contact_skills" not in configured:
            template = starter_skills.get(char.get("archetype"))
            if template:
                char["contact_skills"] = list(template)
        result = post(client, "/characters/", char)
        char_id = result["id"]
        character_ids[char["name"]] = char_id
        print(f"  + {char['name']} ({'PC' if char.get('is_pc') else 'NPC'}) -> id {char_id}")
        if rep_data is not None:
            rep_payload = dict(rep_data, character_id=char_id)
            rep_result = post(client, "/reputation/", rep_payload)
            print(f"    + reputation -> id {rep_result['id']}")

    print("\n[4/9] Organization Relationships and Divisions")
    for org in data.get("organizations", []):
        payload = {
            "leadership": _resolve_leadership(org.get("leadership"), character_ids),
            "divisions": [
                _resolve_division(division, org_ids, character_ids)
                for division in org.get("divisions", [])
            ],
        }
        for id_field, name_field in _ORG_RELATION_NAMES.items():
            payload[id_field] = _ids_for_names(
                org.get(name_field, []), org_ids, name_field
            )
        patch(client, f"/organizations/{org_ids[org['name']]}", payload)

    print("\n[5/9] Matrix Hosts")
    host_ids = {}
    for configured in data.get("matrix_hosts", []):
        host = dict(configured)
        owner_name = host.pop("owner_org_name", None)
        location_name = host.pop("location_name", None)
        host.pop("trap_doors", None)
        host["owner_org_id"] = _ids_for_names(
            [owner_name], org_ids, "matrix host owner"
        )[0] if owner_name else None
        host["location_id"] = _ids_for_names(
            [location_name], location_ids, "matrix host location"
        )[0] if location_name else None
        host["trap_doors_json"] = None
        result = post(client, "/matrix-hosts/", host)
        host_ids[configured["name"]] = result["id"]
        print(f"  + {configured['name']} -> id {result['id']}")
    for configured in data.get("matrix_hosts", []):
        doors = []
        for raw_door in configured.get("trap_doors", []):
            door = dict(raw_door)
            destination_name = door.pop("destination_host_name", None)
            door["destination_host_id"] = _ids_for_names(
                [destination_name], host_ids, "trap-door destination"
            )[0] if destination_name else None
            doors.append(door)
        if doors:
            patch(
                client,
                f"/matrix-hosts/{host_ids[configured['name']]}",
                {"trap_doors_json": doors},
            )

    print("\n[6/9] Contacts")
    for contact in data.get("contacts", []):
        owner_name = contact.get("owner_name")
        npc_name = contact.get("npc_name")
        org_name = contact.get("organization_name")
        loc_name = contact.get("location_name")

        if owner_name not in character_ids:
            raise RuntimeError(f"Contact owner not found: {owner_name}")

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

    print("\n[7/9] Org Standings")
    for standing in data.get("org_standings", []):
        char_name = standing.get("character_name")
        org_name = standing.get("org_name")
        _ids_for_names([char_name], character_ids, "standing character")
        _ids_for_names([org_name], org_ids, "standing organization")
        payload = {
            "character_id": character_ids[char_name],
            "organization_id": org_ids[org_name],
            "standing": standing.get("standing", 0),
            "notes": standing.get("notes"),
        }
        result = post(client, "/reputation/standings", payload)
        print(f"  + {char_name} <-> {org_name} (standing {payload['standing']}) -> id {result['id']}")

    print("\n[8/9] Adventure Logs")
    for log in data.get("adventure_logs", []):
        payload = {k: v for k, v in log.items()
                   if k not in ("participant_names", "location_names", "org_names")}
        payload["participant_ids"] = [character_ids[n] for n in log.get("participant_names", []) if n in character_ids]
        payload["location_ids"] = [location_ids[n] for n in log.get("location_names", []) if n in location_ids]
        payload["org_ids"] = [org_ids[n] for n in log.get("org_names", []) if n in org_ids]
        result = post(client, "/runs/", payload)
        print(f"  + {log['title']} -> id {result['id']}")

    print("\n[9/9] Campaign Settings")
    campaign = data.get("campaign_state") or {}
    if "enabled_books" in campaign:
        put(client, "/catalog/books", {"enabled": campaign["enabled_books"]})
    target_tick = int(campaign.get("current_tick", 0))
    current_tick = int(get_json(client, "/campaign/clock")["current_tick"])
    if current_tick > target_tick:
        raise RuntimeError(
            f"Fresh campaign clock {current_tick} exceeds seed target {target_tick}"
        )
    if current_tick < target_tick:
        post(client, "/campaign/advance", {"days": target_tick - current_tick})

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
    parser.add_argument(
        "--export-db",
        default=None,
        help="Export a portable PC-free world seed from this SQLite database, then exit.",
    )
    args = parser.parse_args()

    if args.export_db:
        data = write_world_seed(args.export_db, args.file)
        print(
            f"Exported {len(data['organizations'])} organizations, "
            f"{len(data['locations'])} locations, {len(data['characters'])} NPCs, "
            f"{len(data['rtgs'])} RTGs, and {len(data['matrix_hosts'])} Matrix hosts "
            f"to {args.file}"
        )
        raise SystemExit(0)

    print(f"Seeding {args.file} -> {args.url}")
    try:
        seed(args.url, args.file, args.admin_token, upsert_rtgs_only=args.upsert_rtgs_only)
    except RuntimeError as e:
        print(f"  {e}")
        raise SystemExit(1) from e
