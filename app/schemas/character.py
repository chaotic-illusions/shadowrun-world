from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CharacterBase(BaseModel):
    name: str = Field(max_length=200)
    is_pc: bool = True
    archetype: Optional[str] = Field(default=None, max_length=100)
    title: Optional[str] = Field(default=None, max_length=200)
    race: str = Field(default="Human", max_length=50)
    nationality: Optional[str] = Field(default=None, max_length=100)
    gender: Optional[str] = Field(default=None, max_length=50)
    age: Optional[int] = Field(default=None, ge=0, le=500)
    description: Optional[str] = None
    background: Optional[str] = None
    show_background: bool = False
    is_active: bool = True
    notes: Optional[str] = None
    owner_token: Optional[str] = Field(default=None, max_length=64)
    contact_skills: list[str] = []
    connection: int = Field(default=1, ge=1, le=6)
    organization_id: Optional[int] = None


CharacterCreate = CharacterBase


class CharacterUpdate(BaseModel):
    name: Optional[str] = Field(default=None, max_length=200)
    is_pc: Optional[bool] = None
    archetype: Optional[str] = Field(default=None, max_length=100)
    title: Optional[str] = Field(default=None, max_length=200)
    race: Optional[str] = Field(default=None, max_length=50)
    nationality: Optional[str] = Field(default=None, max_length=100)
    gender: Optional[str] = Field(default=None, max_length=50)
    age: Optional[int] = Field(default=None, ge=0, le=500)
    description: Optional[str] = None
    background: Optional[str] = None
    show_background: Optional[bool] = None
    is_active: Optional[bool] = None
    notes: Optional[str] = None
    owner_token: Optional[str] = Field(default=None, max_length=64)
    contact_skills: Optional[list[str]] = None
    connection: Optional[int] = Field(default=None, ge=1, le=6)
    organization_id: Optional[int] = None


class CharacterRead(CharacterBase):
    id: int
    created_at: datetime
    updated_at: datetime
    organization_name: Optional[str] = None
    is_claimed: bool = False
    # Pydantic V2: Field(exclude=True) prevents owner_token from appearing in API responses
    owner_token: Optional[str] = Field(default=None, exclude=True)
    model_config = ConfigDict(from_attributes=True)


class CharacterSummary(BaseModel):
    id: int
    name: str
    is_pc: bool
    archetype: Optional[str] = None
    race: str
    is_active: bool
    model_config = ConfigDict(from_attributes=True)
