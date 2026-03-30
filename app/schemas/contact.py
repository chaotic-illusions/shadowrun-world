from typing import Optional
from pydantic import BaseModel, ConfigDict, field_validator


class ContactBase(BaseModel):
    name: str
    profession: Optional[str] = None
    race: Optional[str] = None
    loyalty: int = 1
    connection: int = 1
    description: Optional[str] = None
    notes: Optional[str] = None
    owner_id: int
    npc_id: Optional[int] = None
    location_id: Optional[int] = None
    organization_id: Optional[int] = None

    @field_validator("loyalty", "connection")
    @classmethod
    def rating_in_range(cls, v: int) -> int:
        if not 1 <= v <= 6:
            raise ValueError("Rating must be between 1 and 6")
        return v


ContactCreate = ContactBase


class ContactUpdate(BaseModel):
    name: Optional[str] = None
    profession: Optional[str] = None
    race: Optional[str] = None
    loyalty: Optional[int] = None
    connection: Optional[int] = None
    description: Optional[str] = None
    notes: Optional[str] = None
    npc_id: Optional[int] = None
    location_id: Optional[int] = None
    organization_id: Optional[int] = None

    @field_validator("loyalty", "connection", mode="before")
    @classmethod
    def rating_in_range(cls, v: int | None) -> int | None:
        if v is not None and not 1 <= v <= 6:
            raise ValueError("Rating must be between 1 and 6")
        return v


class ContactRead(ContactBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
