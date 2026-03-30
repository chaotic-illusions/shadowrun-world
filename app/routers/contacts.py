from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db, get_or_404, apply_update
from app.models.contact import Contact
from app.schemas.contact import ContactCreate, ContactUpdate, ContactRead

router = APIRouter()


@router.get("/", response_model=list[ContactRead])
def list_contacts(
    owner_id: int | None = Query(None, description="Filter by owning character ID"),
    organization_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    q = db.query(Contact)
    if owner_id is not None:
        q = q.filter(Contact.owner_id == owner_id)
    if organization_id is not None:
        q = q.filter(Contact.organization_id == organization_id)
    return q.order_by(Contact.name).all()


@router.post("/", response_model=ContactRead, status_code=201)
def create_contact(body: ContactCreate, db: Session = Depends(get_db)):
    contact = Contact(**body.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


@router.get("/{contact_id}", response_model=ContactRead)
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return get_or_404(db, Contact, contact_id)


@router.patch("/{contact_id}", response_model=ContactRead)
def update_contact(contact_id: int, body: ContactUpdate, db: Session = Depends(get_db)):
    contact = get_or_404(db, Contact, contact_id)
    apply_update(db, contact, body)
    return contact


@router.delete("/{contact_id}", status_code=204)
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = get_or_404(db, Contact, contact_id)
    db.delete(contact)
    db.commit()
