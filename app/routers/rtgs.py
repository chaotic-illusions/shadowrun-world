from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.rtg import RTG
from app.schemas.rtg import RTGCreate, RTGUpdate, RTGRead
from app.auth.dependencies import get_admin_token

router = APIRouter()


@router.get("/", response_model=list[RTGRead])
async def list_rtgs(
    continent: str | None = Query(None),
    rtg_security_rating: str | None = Query(None),
    canonical: bool | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(RTG)
    if continent:
        q = q.where(RTG.continent == continent)
    if rtg_security_rating:
        q = q.where(RTG.rtg_security_rating == rtg_security_rating)
    if canonical is not None:
        q = q.where(RTG.canonical == canonical)
    result = await db.execute(q.order_by(RTG.code))
    return result.scalars().all()


@router.post("/", response_model=RTGRead, status_code=201)
async def create_rtg(
    body: RTGCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rtg = RTG(**body.model_dump())
    db.add(rtg)
    await db.commit()
    await db.refresh(rtg)
    return rtg


@router.get("/code/{code}", response_model=RTGRead)
async def get_rtg_by_code(code: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(RTG).where(RTG.code == code))
    rtg = result.scalars().first()
    if not rtg:
        raise HTTPException(status_code=404, detail=f"RTG '{code}' not found")
    return rtg


@router.get("/{rtg_id}", response_model=RTGRead)
async def get_rtg(rtg_id: int, db: AsyncSession = Depends(get_db)):
    return await get_or_404(db, RTG, rtg_id)


@router.patch("/{rtg_id}", response_model=RTGRead)
async def update_rtg(
    rtg_id: int,
    body: RTGUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rtg = await get_or_404(db, RTG, rtg_id)
    await apply_update(db, rtg, body)
    return rtg


@router.delete("/{rtg_id}", status_code=204)
async def delete_rtg(
    rtg_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rtg = await get_or_404(db, RTG, rtg_id)
    await db.delete(rtg)
    await db.commit()
