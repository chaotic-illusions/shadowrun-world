from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class VerifyRequest(BaseModel):
    admin_token: Optional[str] = None
    user_token: Optional[str] = None


class VerifyResponse(BaseModel):
    is_admin: bool
    is_user: bool
    is_default_password: bool
    user_token: Optional[str] = None
    token_label: Optional[str] = None


class UserTokenLabelUpdate(BaseModel):
    label: Optional[str] = None


class UserTokenCreate(BaseModel):
    label: Optional[str] = None
    is_admin: bool = False


class UserTokenRead(BaseModel):
    id: int
    label: Optional[str] = None
    is_admin: bool
    created_at: datetime
    model_config = {"from_attributes": True}


class UserTokenCreateResponse(BaseModel):
    id: int
    token: str
    label: Optional[str] = None
    is_admin: bool
    created_at: datetime
