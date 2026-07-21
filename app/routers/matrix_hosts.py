from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db
from app.models.matrix_host import MatrixHost
from app.models.organization import Organization
from app.schemas.matrix_host import (
    MatrixHostCreate, MatrixHostUpdate, MatrixHostRead, MatrixHostSummary,
)
from app.services.host_visibility import sync_host_reveal_to_org, sync_host_security_to_org
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


async def _get_or_404(db: AsyncSession, host_id: int) -> MatrixHost:
    result = await db.execute(select(MatrixHost).where(MatrixHost.id == host_id))
    host = result.scalars().first()
    if not host:
        raise HTTPException(status_code=404, detail="Matrix host not found")
    return host


def _dest_ids(trap_doors) -> set[int]:
    """Collect the destination host ids named in a trap_doors_json list."""
    ids: set[int] = set()
    for td in (trap_doors or []):
        if isinstance(td, dict):
            d = td.get("destination_host_id")
            if isinstance(d, int):
                ids.add(d)
    return ids


async def _recompute_trap_dest_flags(db: AsyncSession, affected_ids: set[int]) -> None:
    """Re-derive is_trap_door_dest for the given hosts from the live set of trap-door edges.

    A host is a trap-door destination IFF some host's trap_doors_json names it -- the flag is a
    pure derivation now (the manual toggles were removed). Call this whenever an edge set changes
    so a removed link drops the child's flag (and an added link sets it). Autoflush makes the
    pending in-session edits visible to the reference scan, so it reflects the just-saved state.
    """
    res = await db.execute(select(MatrixHost.trap_doors_json))
    referenced: set[int] = set()
    for (tds,) in res.all():
        referenced |= _dest_ids(tds)
    res2 = await db.execute(select(MatrixHost).where(MatrixHost.id.in_(affected_ids)))
    for dest in res2.scalars().all():
        should = dest.id in referenced
        if bool(dest.is_trap_door_dest) != should:
            dest.is_trap_door_dest = should


@router.get("/", response_model=list[MatrixHostSummary])
async def list_hosts(
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    is_admin = bool(auth.get("is_admin"))
    # A real admin sees the full GM listing; players -- AND an admin previewing runner view
    # (X-Runner-View) -- get the player payload. view_as_player can only REDUCE what is returned.
    show_gm = is_admin and not auth.get("view_as_player")
    q = select(MatrixHost).order_by(MatrixHost.name)
    if not show_gm:
        q = q.where(MatrixHost.is_visible_to_players == True)  # noqa: E712
    result = await db.execute(q)
    rows = result.scalars().all()
    if show_gm:
        return rows
    # Player view: trap-door topology is GM-only (the admin registry needs the edge list to draw
    # the parent/child tree, but players must never get it), and the host Security Rating (SC/SV)
    # stays hidden -- it is discovered in-run via Analyze Host, or shown on the org card once the
    # matching LTG entry is revealed (served reveal-aware by ltg-catalog). Strip both per summary.
    redacted = []
    for h in rows:
        s = MatrixHostSummary.model_validate(h)
        s.trap_doors_json = None
        s.san_rating = None
        redacted.append(s)
    return redacted


@router.post("/", response_model=MatrixHostRead, status_code=201,
             dependencies=[Depends(get_admin_token)])
async def create_host(body: MatrixHostCreate, db: AsyncSession = Depends(get_db)):
    host = MatrixHost(**body.model_dump())
    db.add(host)
    await db.commit()
    await db.refresh(host)
    return host


@router.get("/ltg-catalog")
async def ltg_catalog(
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    """Return all matrix_host LTG entries from the live organizations table."""
    # A real admin (not previewing runner view) sees the GM data; players -- and an admin who
    # toggled runner view -- get each entry's SC/SV rating only once it has been discovered
    # (san_revealed), mirroring the org-card redaction in organizations._serialize_org.
    show_secrets = bool(auth.get("is_admin")) and not auth.get("view_as_player")
    result = await db.execute(select(Organization).order_by(Organization.name))
    orgs = result.scalars().all()

    entries = []
    for org in orgs:
        for ltg in (org.ltgs or []):
            if ltg.get("type") != "matrix_host":
                continue
            rtg = ltg.get("rtg", "")
            ltg_code = ltg.get("ltg", "")
            full_address = f"{rtg} {ltg_code}".strip()
            san = ltg.get("san_access_rating", "")
            san_revealed = bool(ltg.get("san_revealed", False))
            entries.append({
                "org_id":           org.id,
                "org_name":         org.name,
                "rtg":              rtg,
                "ltg":              ltg_code,
                "full_address":     full_address,
                "id_code":          ltg.get("id_code"),
                "description":      ltg.get("description", ""),
                "visibility":       ltg.get("visibility", "listed"),
                "revealed":         bool(ltg.get("revealed", False)),
                "san_access_rating": san if (show_secrets or san_revealed) else "",
            })
    return entries


@router.get("/{host_id}", response_model=MatrixHostRead)
async def get_host(
    host_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    host = await _get_or_404(db, host_id)
    if not auth.get("is_admin") and not host.is_visible_to_players:
        raise HTTPException(status_code=404, detail="Matrix host not found")
    return host


@router.patch("/{host_id}", response_model=MatrixHostRead,
              dependencies=[Depends(get_admin_token)])
async def update_host(
    host_id: int, body: MatrixHostUpdate, db: AsyncSession = Depends(get_db)
):
    host = await _get_or_404(db, host_id)
    # A host is reachable if it has a grid address OR is a trap-door destination (reached through a
    # parent host's trap door). Capture that before applying so we can block an update that strips
    # reachability away -- only a trap-door destination may legitimately drop its LTG and go off-grid.
    was_reachable = bool((host.ltg_address or "").strip()) or bool(host.is_trap_door_dest)
    old_dest_ids = _dest_ids(host.trap_doors_json)
    updates = body.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(host, field, value)
    now_reachable = bool((host.ltg_address or "").strip()) or bool(host.is_trap_door_dest)
    if was_reachable and not now_reachable:
        raise HTTPException(
            status_code=400,
            detail=(
                "A non-trap-door host must keep an RTG/LTG address. Mark it as a trap-door "
                "destination first to take it off the grid."
            ),
        )
    # A host can only be revealed to players once it has a real grid address (RTG/LTG).
    # Revealing an address-less host would surface a non-runnable entry on the Matrix Run screen.
    if host.is_visible_to_players and not (host.ltg_address or "").strip():
        raise HTTPException(
            status_code=400,
            detail="Host must have an RTG/LTG address before it can be revealed to players.",
        )
    # Mirror a visibility/LTG-link change onto the org page's per-LTG "revealed" flag so the
    # two surfaces stay in sync (the org card and this host share one reveal state).
    if "is_visible_to_players" in updates or "ltg_address" in updates:
        await sync_host_reveal_to_org(db, host)
    # Security rating edited in the designer (config_json) -- or a re-link to a different LTG --
    # propagates onto the matching org LTG entry's san_access_rating so the org card, the host
    # registry, and the run engine all agree on one value.
    if "config_json" in updates or "ltg_address" in updates:
        await sync_host_security_to_org(db, host)
    # When trap doors are saved, re-derive the is_trap_door_dest flag for every host that just
    # gained or lost an inbound link (old destinations union new destinations). A host named as a
    # destination becomes a trap-door destination; one no longer named drops the flag -- so the
    # destination picker, the registry tree, and the reachability guard all stay consistent without
    # any manual toggle.
    if "trap_doors_json" in updates:
        affected = old_dest_ids | _dest_ids(host.trap_doors_json)
        if affected:
            await _recompute_trap_dest_flags(db, affected)
    await db.commit()
    await db.refresh(host)
    return host



@router.delete("/{host_id}", status_code=204,
               dependencies=[Depends(get_admin_token)])
async def delete_host(host_id: int, db: AsyncSession = Depends(get_db)):
    host = await _get_or_404(db, host_id)
    # Deleting a parent removes its trap doors, so re-derive its children's destination flag after
    # the row is gone (an off-grid child left with no inbound link surfaces as Unreachable).
    affected = _dest_ids(host.trap_doors_json)
    await db.delete(host)
    await db.flush()
    if affected:
        await _recompute_trap_dest_flags(db, affected)
    await db.commit()
