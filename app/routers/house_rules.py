from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_or_404, apply_update
from app.models.house_rule import HouseRule
from app.schemas.house_rule import HouseRuleCreate, HouseRuleUpdate, HouseRuleRead

router = APIRouter()


@router.get("/", response_model=list[HouseRuleRead])
def list_house_rules(
    category: str | None = Query(None),
    is_active: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(HouseRule)
    if category:
        q = q.filter(HouseRule.category == category)
    if is_active is not None:
        q = q.filter(HouseRule.is_active == is_active)
    return q.order_by(HouseRule.category, HouseRule.title).all()


@router.post("/", response_model=HouseRuleRead, status_code=201)
def create_house_rule(body: HouseRuleCreate, db: Session = Depends(get_db)):
    rule = HouseRule(**body.model_dump())
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


@router.get("/{rule_id}", response_model=HouseRuleRead)
def get_house_rule(rule_id: int, db: Session = Depends(get_db)):
    return get_or_404(db, HouseRule, rule_id)


@router.patch("/{rule_id}", response_model=HouseRuleRead)
def update_house_rule(rule_id: int, body: HouseRuleUpdate, db: Session = Depends(get_db)):
    rule = get_or_404(db, HouseRule, rule_id)
    apply_update(db, rule, body)
    return rule


@router.delete("/{rule_id}", status_code=204)
def delete_house_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = get_or_404(db, HouseRule, rule_id)
    db.delete(rule)
    db.commit()
