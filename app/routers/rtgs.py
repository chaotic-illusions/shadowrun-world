from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.rtg import RTG
from app.schemas.rtg import RTGCreate, RTGUpdate, RTGRead

router = APIRouter()


def _get_or_404(db: Session, rtg_id: int) -> RTG:
    rtg = db.query(RTG).filter(RTG.id == rtg_id).first()
    if not rtg:
        raise HTTPException(status_code=404, detail="RTG not found")
    return rtg


@router.get("/", response_model=list[RTGRead])
def list_rtgs(
    continent: str | None = Query(None),
    rating_color: str | None = Query(None),
    canonical: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(RTG)
    if continent:
        q = q.filter(RTG.continent == continent)
    if rating_color:
        q = q.filter(RTG.rating_color == rating_color)
    if canonical is not None:
        q = q.filter(RTG.canonical == canonical)
    return q.order_by(RTG.code).all()


@router.post("/", response_model=RTGRead, status_code=201)
def create_rtg(body: RTGCreate, db: Session = Depends(get_db)):
    rtg = RTG(**body.model_dump())
    db.add(rtg)
    db.commit()
    db.refresh(rtg)
    return rtg


@router.get("/code/{code}", response_model=RTGRead)
def get_rtg_by_code(code: str, db: Session = Depends(get_db)):
    rtg = db.query(RTG).filter(RTG.code == code).first()
    if not rtg:
        raise HTTPException(status_code=404, detail=f"RTG '{code}' not found")
    return rtg


@router.get("/{rtg_id}", response_model=RTGRead)
def get_rtg(rtg_id: int, db: Session = Depends(get_db)):
    return _get_or_404(db, rtg_id)


@router.patch("/{rtg_id}", response_model=RTGRead)
def update_rtg(rtg_id: int, body: RTGUpdate, db: Session = Depends(get_db)):
    rtg = _get_or_404(db, rtg_id)
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(rtg, field, value)
    db.commit()
    db.refresh(rtg)
    return rtg


@router.delete("/{rtg_id}", status_code=204)
def delete_rtg(rtg_id: int, db: Session = Depends(get_db)):
    rtg = _get_or_404(db, rtg_id)
    db.delete(rtg)
    db.commit()
