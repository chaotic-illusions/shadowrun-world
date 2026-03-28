from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.location import Location
from app.schemas.location import LocationCreate, LocationUpdate, LocationRead

router = APIRouter()


def _get_or_404(db: Session, location_id: int) -> Location:
    loc = db.query(Location).filter(Location.id == location_id).first()
    if not loc:
        raise HTTPException(status_code=404, detail="Location not found")
    return loc


@router.get("/", response_model=list[LocationRead])
def list_locations(
    city: str | None = Query(None),
    location_type: str | None = Query(None),
    controlling_org_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(Location)
    if city:
        q = q.filter(Location.city.ilike(f"%{city}%"))
    if location_type:
        q = q.filter(Location.location_type == location_type)
    if controlling_org_id is not None:
        q = q.filter(Location.controlling_org_id == controlling_org_id)
    return q.order_by(Location.name).all()


@router.post("/", response_model=LocationRead, status_code=201)
def create_location(body: LocationCreate, db: Session = Depends(get_db)):
    loc = Location(**body.model_dump())
    db.add(loc)
    db.commit()
    db.refresh(loc)
    return loc


@router.get("/{location_id}", response_model=LocationRead)
def get_location(location_id: int, db: Session = Depends(get_db)):
    return _get_or_404(db, location_id)


@router.patch("/{location_id}", response_model=LocationRead)
def update_location(location_id: int, body: LocationUpdate, db: Session = Depends(get_db)):
    loc = _get_or_404(db, location_id)
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(loc, field, value)
    db.commit()
    db.refresh(loc)
    return loc


@router.delete("/{location_id}", status_code=204)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    loc = _get_or_404(db, location_id)
    db.delete(loc)
    db.commit()
