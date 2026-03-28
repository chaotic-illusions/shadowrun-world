from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.house_rule import HouseRule
from app.schemas.house_rule import HouseRuleCreate, HouseRuleUpdate, HouseRuleRead

router = APIRouter()


def _get_or_404(db: Session, rule_id: int) -> HouseRule:
    rule = db.query(HouseRule).filter(HouseRule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="House rule not found")
    return rule


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
    return _get_or_404(db, rule_id)


@router.patch("/{rule_id}", response_model=HouseRuleRead)
def update_house_rule(rule_id: int, body: HouseRuleUpdate, db: Session = Depends(get_db)):
    rule = _get_or_404(db, rule_id)
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(rule, field, value)
    db.commit()
    db.refresh(rule)
    return rule


@router.delete("/{rule_id}", status_code=204)
def delete_house_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = _get_or_404(db, rule_id)
    db.delete(rule)
    db.commit()
