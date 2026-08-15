"""Read-only SR2 reference catalogs plus the per-campaign book-toggle setting.

Item catalogs (weapons/armor/cyberware/gear/spells/adept_powers/vehicles) are
filtered by the campaign's enabled sourcebooks; SR2 core is always included.
The chargen rules bundle and the book list are not book-filtered.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_admin_token
from app.data import catalog as cat
from app.dependencies import get_db
from app.schemas.catalog import (
    BookInfo,
    BookSettingsRead,
    BookSettingsUpdate,
    CoreBook,
    CyberwareCreate,
    FanBook,
)
from app.services.campaign import get_campaign_state

router = APIRouter()


def _book_settings(enabled: list[str]) -> BookSettingsRead:
    normalized = cat.normalize_enabled(enabled)
    enabled_set = set(normalized)
    return BookSettingsRead(
        core=CoreBook(code=cat.CORE_BOOK, name=cat.CORE_BOOK_NAME),
        official=[
            BookInfo(code=code, name=name, enabled=code in enabled_set)
            for code, name in cat.OFFICIAL_BOOKS.items()
        ],
        fan=FanBook(
            code=cat.FAN_TOGGLE,
            name=cat.FAN_TOGGLE_NAME,
            enabled=cat.FAN_TOGGLE in enabled_set,
            includes=[f"{code} ({name})" for code, name in cat.FAN_BOOKS.items()],
        ),
        enabled=normalized,
    )


@router.get("/books", response_model=BookSettingsRead)
async def get_books(db: AsyncSession = Depends(get_db)):
    """Return the toggleable book list with each book's enabled state."""
    state = await get_campaign_state(db)
    return _book_settings(state.enabled_books or [])


@router.put("/books", response_model=BookSettingsRead)
async def set_books(
    body: BookSettingsUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    """Set the campaign's enabled sourcebooks (admin only)."""
    normalized = cat.normalize_enabled(body.enabled)
    state = await get_campaign_state(db)
    state.enabled_books = normalized
    await db.commit()
    return _book_settings(normalized)


@router.get("/rules")
async def get_rules():
    """Return the SR2 chargen rules bundle (priorities, metatypes, totems, ...)."""
    return cat.get_rules()


@router.get("/skill-specs")
async def get_skill_specs():
    """Return the skill definitions plus the curated concentration/specialization overlay.

    ``skills`` is the read-only SR2 skill list (name, group, attr, concentrations);
    ``specs`` is the GM-editable map skill -> concentration -> [specializations].
    """
    skills = [
        {
            "n": s.get("n"),
            "attr": s.get("attr"),
            "group": s.get("group"),
            "conc": s.get("conc", []),
        }
        for s in cat.get_skills()
    ]
    return {"skills": skills, "specs": cat.get_skill_specs()}


@router.get("/vehicle-classes")
async def get_vehicle_classes():
    """Return the GM vehicle-classification overlay (vehicle name -> {skill, conc}),
    which drives the character builder's ``(SV)`` specialization expansion."""
    return {"classes": cat.get_vehicle_classes()}


@router.post("/cyberware", status_code=201)
async def add_cyberware(
    body: CyberwareCreate,
    _: str = Depends(get_admin_token),
):
    """Append one cyberware item to the catalog (admin data-entry). Returns the
    stored item and the new unfiltered catalog count."""
    try:
        item = cat.append_cyberware(body.to_item())
    except ValueError as exc:
        raise HTTPException(status_code=409, detail=str(exc))
    return {"item": item, "count": len(cat.get_catalog("cyberware"))}


@router.get("/{catalog_name}")
async def get_catalog_items(catalog_name: str, db: AsyncSession = Depends(get_db)):
    """Return the items of a catalog, filtered to the campaign's enabled books."""
    if catalog_name not in cat.ITEM_CATALOGS:
        raise HTTPException(status_code=404, detail="Unknown catalog")
    state = await get_campaign_state(db)
    items = cat.filter_catalog(catalog_name, state.enabled_books or [])
    return {"catalog": catalog_name, "count": len(items), "items": items}
