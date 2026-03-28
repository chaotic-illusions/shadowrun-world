from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationRead, OrganizationSummary

router = APIRouter()


def _get_or_404(db: Session, org_id: int) -> Organization:
    org = db.query(Organization).filter(Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")
    return org


@router.get("/", response_model=list[OrganizationRead])
def list_organizations(
    org_type: str | None = Query(None),
    is_active: bool | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(Organization)
    if org_type:
        q = q.filter(Organization.org_type == org_type)
    if is_active is not None:
        q = q.filter(Organization.is_active == is_active)
    return q.order_by(Organization.tier.desc(), Organization.name).all()


@router.post("/", response_model=OrganizationRead, status_code=201)
def create_organization(body: OrganizationCreate, db: Session = Depends(get_db)):
    org = Organization(**body.model_dump())
    db.add(org)
    db.commit()
    db.refresh(org)
    return org


@router.get("/{org_id}", response_model=OrganizationRead)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    return _get_or_404(db, org_id)


@router.patch("/{org_id}", response_model=OrganizationRead)
def update_organization(org_id: int, body: OrganizationUpdate, db: Session = Depends(get_db)):
    org = _get_or_404(db, org_id)
    for field, value in body.model_dump(exclude_unset=True).items():
        setattr(org, field, value)
    db.commit()
    db.refresh(org)
    return org


@router.delete("/{org_id}", status_code=204)
def delete_organization(org_id: int, db: Session = Depends(get_db)):
    org = _get_or_404(db, org_id)
    db.delete(org)
    db.commit()
