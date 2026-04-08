from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class HouseRuleBase(BaseModel):
    title: str = Field(max_length=300)
    category: Optional[str] = Field(default=None, max_length=100)
    source_reference: Optional[str] = Field(default=None, max_length=200)
    original_rule: Optional[str] = None
    modification: str
    reason: Optional[str] = None
    is_active: bool = True


HouseRuleCreate = HouseRuleBase


class HouseRuleUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=300)
    category: Optional[str] = Field(default=None, max_length=100)
    source_reference: Optional[str] = Field(default=None, max_length=200)
    original_rule: Optional[str] = None
    modification: Optional[str] = None
    reason: Optional[str] = None
    is_active: Optional[bool] = None


class HouseRuleRead(HouseRuleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
