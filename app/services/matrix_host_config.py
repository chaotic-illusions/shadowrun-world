from __future__ import annotations

import copy
import uuid
from typing import Any


def normalize_host_config(
    config: dict[str, Any] | None,
    existing_config: dict[str, Any] | None = None,
) -> dict[str, Any] | None:
    """Return a copied host config with stable paydata IDs and ID-based file defenses."""
    if config is None:
        return None
    normalized = copy.deepcopy(config)
    scrambles = normalized.get("scrambles")
    if isinstance(scrambles, list):
        scrambles[:] = [
            scramble for scramble in scrambles
            if (
                isinstance(scramble, dict)
                and scramble.get("variant") in {"exploding", "poison"}
            )
        ]
    paydata = normalized.get("paydata")
    if not isinstance(paydata, list):
        return normalized

    existing_paydata = (existing_config or {}).get("paydata") or []
    used: set[str] = set()
    name_to_ids: dict[str, list[str]] = {}
    for index, item in enumerate(paydata):
        if not isinstance(item, dict):
            continue
        paydata_id = str(item.get("id") or "").strip()
        if not paydata_id and index < len(existing_paydata):
            previous = existing_paydata[index]
            if isinstance(previous, dict):
                paydata_id = str(previous.get("id") or "").strip()
        if not paydata_id or paydata_id in used:
            paydata_id = f"pd_{uuid.uuid4().hex}"
        item["id"] = paydata_id
        used.add(paydata_id)
        name = str(item.get("name") or "").strip().lower()
        if name:
            name_to_ids.setdefault(name, []).append(paydata_id)

    def resolve(reference: str) -> str:
        ref = str(reference or "").strip()
        if ref in used:
            return ref
        ids = name_to_ids.get(ref.lower()) or []
        return ids[0] if ids else ref

    has_embedded_defenses = any(
        isinstance(item, dict) and isinstance(item.get("defense"), dict)
        for item in paydata
    )

    bombs = normalized.get("data_bombs")
    if isinstance(bombs, list):
        if has_embedded_defenses:
            bombs[:] = [
                bomb for bomb in bombs
                if not (
                    isinstance(bomb, dict)
                    and str(bomb.get("target") or "").startswith("files::")
                )
            ]
        for bomb in bombs:
            if not isinstance(bomb, dict):
                continue
            target = str(bomb.get("target") or "")
            if target.startswith("files::"):
                bomb["target"] = "files::" + resolve(target[len("files::"):])
    else:
        bombs = []
        normalized["data_bombs"] = bombs

    if isinstance(scrambles, list):
        if has_embedded_defenses:
            scrambles[:] = [
                scramble for scramble in scrambles
                if not (
                    isinstance(scramble, dict)
                    and str(scramble.get("target_key") or "").startswith("files::file::")
                )
            ]
        for scramble in scrambles:
            if not isinstance(scramble, dict):
                continue
            target = str(scramble.get("target_key") or "")
            if target.startswith("files::file::"):
                scramble["target_key"] = "files::file::" + resolve(
                    target[len("files::file::"):]
                )
    else:
        scrambles = []
        normalized["scrambles"] = scrambles

    for item in paydata:
        if not isinstance(item, dict):
            continue
        defense = item.get("defense")
        if not isinstance(defense, dict):
            continue
        paydata_id = item["id"]
        bomb_rating = defense.get("data_bomb_rating")
        if bomb_rating is not None:
            bombs.append({"target": f"files::{paydata_id}", "rating": bomb_rating})
        scramble_rating = defense.get("scramble_rating")
        if scramble_rating is not None:
            scrambles.append({
                "target_key": f"files::file::{paydata_id}",
                "rating": scramble_rating,
                "variant": (
                    "poison" if defense.get("scramble_variant") == "poison" else "exploding"
                ),
            })

    if not bombs:
        normalized["data_bombs"] = None
    if not scrambles:
        normalized["scrambles"] = None
    return normalized