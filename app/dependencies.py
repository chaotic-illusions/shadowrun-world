from collections.abc import AsyncGenerator
from typing import TypeVar
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import async_session

ModelT = TypeVar("ModelT")


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_or_404(db: AsyncSession, model: type[ModelT], obj_id: int) -> ModelT:
    result = await db.execute(select(model).where(model.id == obj_id))
    obj = result.scalars().first()
    if not obj:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return obj


async def apply_update(
    db: AsyncSession, obj, body, exclude: set | None = None, *, commit: bool = True
) -> None:
    """Apply a Pydantic partial-update body to an ORM object.

    When commit=False the caller is responsible for committing the session
    (useful when post-processing is needed before the transaction closes).
    """
    for field, value in body.model_dump(exclude_unset=True, exclude=exclude or set()).items():
        if hasattr(obj, field):
            setattr(obj, field, value)
    if commit:
        await db.commit()
        await db.refresh(obj)
