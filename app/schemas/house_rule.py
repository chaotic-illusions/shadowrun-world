from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class HouseRuleBase(BaseModel):
    title: str
    category: Optional[str] = None
    source_reference: Optional[str] = None
    original_rule: Optional[str] = None
    modification: str
    reason: Optional[str] = None
    is_active: bool = True


class HouseRuleCreate(HouseRuleBase):
    pass


class HouseRuleUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    source_reference: Optional[str] = None
    original_rule: Optional[str] = None
    modification: Optional[str] = None
    reason: Optional[str] = None
    is_active: Optional[bool] = None


class HouseRuleRead(HouseRuleBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
