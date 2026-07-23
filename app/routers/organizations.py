from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.organization import Organization
from app.models.character import Character
from app.models.contact import Contact
from app.models.location import Location
from app.schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationRead, OrganizationSummary, LtgSecurityUpdate
from app.services.host_visibility import sync_org_reveals_to_hosts, sync_org_security_to_hosts
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


def _serialize_org(org: Organization, auth: dict) -> dict:
    """Serialize an org for a GET response, redacting decker-only secrets for non-admins.

    ``san_access_rating`` on a matrix_host LTG entry is a security rating players must discover
    in a run (Analyze Host). Until the entry's ``san_revealed`` flag is set, the rating is
    stripped from the payload so it cannot leak via devtools / the network tab.

    Redaction applies to non-admins AND to an admin previewing the player payload (UI "runner
    view" -> ``view_as_player``), so the preview matches exactly what a player receives. A real
    admin in admin view always gets the full data.
    """
    data = OrganizationRead.model_validate(org, from_attributes=True).model_dump()
    if auth.get("is_admin") and not auth.get("view_as_player"):
        return data
    data["notes"] = None
    data["ally_ids"] = list(data.get("revealed_ally_ids") or [])
    data["enemy_ids"] = list(data.get("revealed_enemy_ids") or [])
    data["leadership"] = [
        {key: value for key, value in entry.items() if key != "notes"}
        for entry in (data.get("leadership") or [])
        if isinstance(entry, dict)
    ]
    rebuilt = []
    for entry in (data.get("ltgs") or []):
        e = dict(entry)
        if e.get("visibility", "listed") != "listed" and not e.get("revealed"):
            continue
        e.pop("notes", None)
        if e.get("type") == "matrix_host" and not e.get("san_revealed"):
            e.pop("san_access_rating", None)
        rebuilt.append(e)
    data["ltgs"] = rebuilt
    return data


def _preserve_san_revealed(old_ltgs, new_ltgs):
    """Carry the persistent ``san_revealed`` discovery flag from old LTG entries onto the
    replacement list from a PATCH body. The GM editor never sends ``san_revealed``, so a naive
    replace would wipe a decker's discovery; matched by the (rtg, ltg) address key.
    """
    revealed = {
        (e.get("rtg"), e.get("ltg"))
        for e in (old_ltgs or [])
        if e.get("type") == "matrix_host" and e.get("san_revealed")
    }
    if not revealed:
        return new_ltgs
    rebuilt = []
    for entry in (new_ltgs or []):
        e = dict(entry)
        if e.get("type") == "matrix_host" and (e.get("rtg"), e.get("ltg")) in revealed:
            e["san_revealed"] = True
        rebuilt.append(e)
    return rebuilt


@router.get("/", response_model=list[OrganizationRead])
async def list_organizations(
    org_type: str | None = Query(None),
    is_active: bool | None = Query(None),
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(Organization)
    if org_type:
        q = q.where(Organization.org_type == org_type)
    if is_active is not None:
        q = q.where(Organization.is_active == is_active)
    result = await db.execute(q.order_by(Organization.tier.desc(), Organization.name))
    return [_serialize_org(o, auth) for o in result.scalars().all()]


@router.post("/", response_model=OrganizationRead, status_code=201)
async def create_organization(
    body: OrganizationCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = Organization(**body.model_dump())
    db.add(org)
    await db.commit()
    await db.refresh(org)
    return org


@router.get("/{org_id}", response_model=OrganizationRead)
async def get_organization(
    org_id: int,
    auth: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    org = await get_or_404(db, Organization, org_id)
    return _serialize_org(org, auth)


@router.patch("/{org_id}", response_model=OrganizationRead)
async def update_organization(
    org_id: int,
    body: OrganizationUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = await get_or_404(db, Organization, org_id)
    fields = body.model_dump(exclude_unset=True)
    old_ltgs = [dict(e) for e in (org.ltgs or [])] if "ltgs" in fields else None
    await apply_update(db, org, body, commit=False)
    # When the LTG list changes, propagate each matrix_host entry's "revealed" flag onto the
    # matching host rows so revealing a host on the org card also makes it runnable, and push
    # each entry's san_access_rating onto the matching host's config so security stays in sync.
    if "ltgs" in fields:
        # The GM editor never sends the decker-discovery flag, so preserve it across the replace.
        org.ltgs = _preserve_san_revealed(old_ltgs, org.ltgs)
        await sync_org_reveals_to_hosts(db, org)
        await sync_org_security_to_hosts(db, org)
    await db.commit()
    await db.refresh(org)
    return org


@router.patch("/{org_id}/ltg-security")
async def update_ltg_security(
    org_id: int,
    body: LtgSecurityUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Update san_access_rating for one LTG entry, identified by rtg+ltg keys."""
    org = await get_or_404(db, Organization, org_id)
    updated = []
    changed = False
    for entry in (org.ltgs or []):
        e = dict(entry)
        if e.get("rtg") == body.rtg and e.get("ltg") == body.ltg:
            e["san_access_rating"] = body.san_access_rating
            changed = True
        updated.append(e)
    if not changed:
        raise HTTPException(
            status_code=404,
            detail=f"No LTG entry with rtg='{body.rtg}' ltg='{body.ltg}' in org {org_id}",
        )
    org.ltgs = updated
    # Push the new rating onto the matching host's config so the designer, host registry, and
    # run engine agree with the org card (the host->org direction lives in matrix_hosts).
    await sync_org_security_to_hosts(db, org)
    await db.commit()
    return {"updated": True, "org_id": org_id, "new_rating": body.san_access_rating}


@router.delete("/{org_id}", status_code=204)
async def delete_organization(
    org_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    org = await get_or_404(db, Organization, org_id)
    # These FKs have no DB-level ondelete rule; with foreign_keys=ON a plain delete would
    # be blocked, so null the references first (SET NULL semantics). org_standings are
    # removed by the ORM cascade; matrix_host.owner_org_id is SET NULL at the DB level.
    await db.execute(sql_update(Character).where(Character.organization_id == org_id).values(organization_id=None))
    await db.execute(sql_update(Contact).where(Contact.organization_id == org_id).values(organization_id=None))
    await db.execute(sql_update(Location).where(Location.controlling_org_id == org_id).values(controlling_org_id=None))
    await db.delete(org)
    await db.commit()
