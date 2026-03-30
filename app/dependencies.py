from collections.abc import Generator
from typing import Type, TypeVar
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.db.session import SessionLocal

ModelT = TypeVar("ModelT")


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_or_404(db: Session, model: Type[ModelT], obj_id: int) -> ModelT:
    obj = db.query(model).filter(model.id == obj_id).first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return obj


def apply_update(db: Session, obj, body, exclude: set | None = None) -> None:
    """Apply a Pydantic partial-update body to an ORM object, commit, and refresh."""
    for field, value in body.model_dump(exclude_unset=True, exclude=exclude or set()).items():
        setattr(obj, field, value)
    db.commit()
    db.refresh(obj)
