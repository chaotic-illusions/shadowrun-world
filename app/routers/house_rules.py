from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies import get_db, get_or_404, apply_update
from app.models.house_rule import HouseRule
from app.schemas.house_rule import HouseRuleCreate, HouseRuleUpdate, HouseRuleRead
from app.auth.dependencies import get_admin_token

router = APIRouter()


@router.get("/", response_model=list[HouseRuleRead])
async def list_house_rules(
    category: str | None = Query(None),
    is_active: bool | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    q = select(HouseRule)
    if category:
        q = q.where(HouseRule.category == category)
    if is_active is not None:
        q = q.where(HouseRule.is_active == is_active)
    result = await db.execute(q.order_by(HouseRule.category, HouseRule.title))
    return result.scalars().all()


@router.post("/", response_model=HouseRuleRead, status_code=201)
async def create_house_rule(
    body: HouseRuleCreate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rule = HouseRule(**body.model_dump())
    db.add(rule)
    await db.commit()
    await db.refresh(rule)
    return rule


@router.get("/{rule_id}", response_model=HouseRuleRead)
async def get_house_rule(rule_id: int, db: AsyncSession = Depends(get_db)):
    return await get_or_404(db, HouseRule, rule_id)


@router.patch("/{rule_id}", response_model=HouseRuleRead)
async def update_house_rule(
    rule_id: int,
    body: HouseRuleUpdate,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rule = await get_or_404(db, HouseRule, rule_id)
    await apply_update(db, rule, body)
    return rule


@router.delete("/{rule_id}", status_code=204)
async def delete_house_rule(
    rule_id: int,
    db: AsyncSession = Depends(get_db),
    _: str = Depends(get_admin_token),
):
    rule = await get_or_404(db, HouseRule, rule_id)
    await db.delete(rule)
    await db.commit()
