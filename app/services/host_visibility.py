"""Keep Matrix host state in lockstep with the per-LTG entry GMs manage on the organizations
page: the player-visibility ``revealed`` flag and the ``san_access_rating`` security rating
(host config ``security_code``/``security_value`` <-> org LTG ``san_access_rating``).

A host is linked to an org's LTG entry purely by matching its ``ltg_address`` string to the
entry's ``"{rtg} {ltg}"`` full address -- the Matrix Designer never writes ``owner_org_id``,
so the address string is the only join key. Both directions are *materialized* (host row <->
org JSON) so the existing player filter (``matrix_hosts.list_hosts`` -> ``is_visible_to_players``)
stays the single authoritative gate and needs no join at read time.

Each function only mutates ORM objects; the calling router owns the commit. JSON columns are
reassigned wholesale (never mutated in place) -- in-place dict/list edits are unreliable in
async SQLAlchemy sessions.
"""
from __future__ import annotations

import re

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.matrix_host import MatrixHost
from app.models.organization import Organization

# "Code-Value" security rating as stored in an org LTG entry's san_access_rating (e.g. "Red-9").
_SAN_RATING_RE = re.compile(r"^\s*([A-Za-z]+)\s*-\s*(\d+)\s*$")


def _ltg_full_address(entry: dict) -> str:
    return f"{entry.get('rtg', '') or ''} {entry.get('ltg', '') or ''}".strip()


async def sync_host_reveal_to_org(db: AsyncSession, host: MatrixHost) -> None:
    """Push a host's ``is_visible_to_players`` onto its matching org LTG entry's ``revealed``."""
    addr = (host.ltg_address or "").strip()
    if not addr:
        return
    visible = bool(host.is_visible_to_players)
    result = await db.execute(select(Organization))
    for org in result.scalars().all():
        changed = False
        rebuilt = []
        for entry in (org.ltgs or []):
            e = dict(entry)
            if e.get("type") == "matrix_host" and _ltg_full_address(e) == addr:
                if bool(e.get("revealed", False)) != visible:
                    e["revealed"] = visible
                    changed = True
            rebuilt.append(e)
        if changed:
            org.ltgs = rebuilt


async def sync_org_reveals_to_hosts(db: AsyncSession, org: Organization) -> None:
    """Push each matrix_host LTG entry's ``revealed`` onto matching hosts' ``is_visible_to_players``."""
    by_addr: dict[str, bool] = {}
    for entry in (org.ltgs or []):
        if entry.get("type") != "matrix_host":
            continue
        addr = _ltg_full_address(entry)
        if addr:
            by_addr[addr] = bool(entry.get("revealed", False))
    if not by_addr:
        return
    result = await db.execute(select(MatrixHost))
    for host in result.scalars().all():
        addr = (host.ltg_address or "").strip()
        if addr in by_addr and bool(host.is_visible_to_players) != by_addr[addr]:
            host.is_visible_to_players = by_addr[addr]


def _host_security_rating(host: MatrixHost) -> str | None:
    """Composed "Code-Value" rating (e.g. "Red-9") from a host's config, or None if incomplete."""
    cfg = host.config_json or {}
    code = cfg.get("security_code")
    val = cfg.get("security_value")
    if code and val is not None:
        return f"{code}-{val}"
    return None


async def sync_host_security_to_org(
    db: AsyncSession, host: MatrixHost, *, mark_revealed: bool = False
) -> None:
    """Push a host's security rating onto its matching org LTG entry's ``san_access_rating``.

    ``san_access_rating`` is a GM/decker secret: it is redacted from the org payload for
    non-admins until the entry's ``san_revealed`` flag is set. Pass ``mark_revealed=True``
    when a decker actually discovers the host's security (e.g. Analyze Host in a run) so the
    rating becomes visible to players. GM/Designer edits leave ``mark_revealed`` False so
    they never leak an undiscovered rating.
    """
    addr = (host.ltg_address or "").strip()
    rating = _host_security_rating(host)
    if not addr or not rating:
        return
    result = await db.execute(select(Organization))
    for org in result.scalars().all():
        changed = False
        rebuilt = []
        for entry in (org.ltgs or []):
            e = dict(entry)
            if e.get("type") == "matrix_host" and _ltg_full_address(e) == addr:
                if (e.get("san_access_rating") or "") != rating:
                    e["san_access_rating"] = rating
                    changed = True
                if mark_revealed and not e.get("san_revealed"):
                    e["san_revealed"] = True
                    changed = True
            rebuilt.append(e)
        if changed:
            org.ltgs = rebuilt


async def sync_org_security_to_hosts(db: AsyncSession, org: Organization) -> None:
    """Push each matrix_host LTG entry's ``san_access_rating`` onto matching hosts' config security."""
    by_addr: dict[str, tuple[str, int]] = {}
    for entry in (org.ltgs or []):
        if entry.get("type") != "matrix_host":
            continue
        addr = _ltg_full_address(entry)
        m = _SAN_RATING_RE.match(entry.get("san_access_rating") or "")
        if addr and m:
            by_addr[addr] = (m.group(1), int(m.group(2)))
    if not by_addr:
        return
    result = await db.execute(select(MatrixHost))
    for host in result.scalars().all():
        addr = (host.ltg_address or "").strip()
        if addr not in by_addr:
            continue
        code, val = by_addr[addr]
        cfg = dict(host.config_json or {})
        if cfg.get("security_code") == code and cfg.get("security_value") == val:
            continue
        cfg["security_code"] = code
        cfg["security_value"] = val
        cfg["san_rating"] = f"{code}-{val}"
        host.config_json = cfg
