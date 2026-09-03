from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select, update as sql_update
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.location import Location
from app.models.contact import Contact
from app.schemas.location import LocationCreate, LocationUpdate, LocationRead
from app.auth.dependencies import get_admin_token, get_any_token

router = APIRouter()


def _is_privileged_view(ctx: dict) -> bool:
    """True only for a real admin NOT previewing runner view -- the full-data audience."""
    return bool(ctx.get("is_admin")) and not ctx.get("view_as_player")


def _serialize_location(location: Location, ctx: dict) -> dict:
    data = LocationRead.model_validate(location, from_attributes=True).model_dump()
    if not _is_privileged_view(ctx):
        data["notes"] = None
    return data


@router.get("/", response_model=list[LocationRead])
async def list_locations(
    city: str | None = Query(None),
    location_type: str | None = Query(None),
    controlling_org_id: int | None = Query(None),
    is_active: bool | None = Query(None),
    source_adventure: str | None = Query(None, description="Filter by published-adventure source"),
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    q = select(Location)
    if not _is_privileged_view(ctx):
        # Undiscovered/retired locations are GM-concealed; never ship them to players.
        q = q.where(Location.is_active == True)  # noqa: E712
    if city:
        q = q.where(Location.city.ilike(f"%{city}%"))
    if location_type:
        q = q.where(Location.location_type == location_type)
    if controlling_org_id is not None:
        q = q.where(Location.controlling_org_id == controlling_org_id)
    if is_active is not None:
        q = q.where(Location.is_active == is_active)
    if source_adventure:
        q = q.where(Location.source_adventure == source_adventure)
    result = await db.execute(q.order_by(Location.name))
    return [_serialize_location(location, ctx) for location in result.scalars().all()]


@router.post("/", response_model=LocationRead, status_code=201)
async def create_location(
    body: LocationCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    loc = Location(**body.model_dump())
    db.add(loc)
    await db.commit()
    await db.refresh(loc)
    return loc


@router.get("/{location_id}", response_model=LocationRead)
async def get_location(
    location_id: int,
    ctx: dict = Depends(get_any_token),
    db: AsyncSession = Depends(get_db),
):
    loc = await get_or_404(db, Location, location_id)
    # Undiscovered locations are GM-concealed -- hide existence from players (404, not 403).
    if loc.is_active is False and not _is_privileged_view(ctx):
        raise HTTPException(status_code=404, detail="Location not found")
    return _serialize_location(loc, ctx)


@router.patch("/{location_id}", response_model=LocationRead)
async def update_location(
    location_id: int,
    body: LocationUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    loc = await get_or_404(db, Location, location_id)
    await apply_update(db, loc, body)
    return loc


@router.delete("/{location_id}", status_code=204)
async def delete_location(
    location_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    loc = await get_or_404(db, Location, location_id)
    # Contact.location_id has no DB ondelete rule; null it so foreign_keys=ON does not
    # block the delete. (matrix_host.location_id is SET NULL at the DB level.)
    await db.execute(sql_update(Contact).where(Contact.location_id == location_id).values(location_id=None))
    await db.delete(loc)
    await db.commit()
