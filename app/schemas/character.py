from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class CharacterBase(BaseModel):
    name: str
    is_pc: bool = True
    archetype: Optional[str] = None
    title: Optional[str] = None
    race: str = "Human"
    nationality: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    background: Optional[str] = None
    show_background: bool = False
    karma_total: int = 0
    karma_current: int = 0
    is_active: bool = True
    notes: Optional[str] = None
    owner_token: Optional[str] = None
    contact_skills: list[str] = []
    connection: int = 1
    organization_id: Optional[int] = None


CharacterCreate = CharacterBase


class CharacterUpdate(BaseModel):
    name: Optional[str] = None
    is_pc: Optional[bool] = None
    archetype: Optional[str] = None
    title: Optional[str] = None
    race: Optional[str] = None
    nationality: Optional[str] = None
    gender: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    background: Optional[str] = None
    show_background: Optional[bool] = None
    karma_total: Optional[int] = None
    karma_current: Optional[int] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None
    owner_token: Optional[str] = None
    contact_skills: Optional[list[str]] = None
    connection: Optional[int] = None
    organization_id: Optional[int] = None


class CharacterRead(CharacterBase):
    id: int
    created_at: datetime
    updated_at: datetime
    organization_name: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)


class CharacterSummary(BaseModel):
    id: int
    name: str
    is_pc: bool
    archetype: Optional[str] = None
    race: str
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
