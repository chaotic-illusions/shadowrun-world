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
    computer_skill_enabled: bool = False
    computer_skill_rating: int = Field(default=0, ge=0, le=20)
    software_skill_enabled: bool = False
    software_skill_rating: int = Field(default=0, ge=0, le=20)
    matrix_skill_enabled: bool = False
    matrix_skill_rating: int = Field(default=0, ge=0, le=20)
    computer_br_skill_enabled: bool = False
    computer_br_skill_rating: int = Field(default=0, ge=0, le=20)
    math_spu_enabled: bool = False
    math_spu_rating: int = Field(default=0, ge=0, le=4)
    intelligence: int = Field(default=0, ge=0, le=20)
    quickness: int = Field(default=0, ge=0, le=12)
    willpower: int = Field(default=0, ge=0, le=20)
    body: int = Field(default=0, ge=0, le=12)
    strength: int = Field(default=0, ge=0, le=20)
    charisma: int = Field(default=0, ge=0, le=20)
    essence: float = Field(default=6.0, ge=0, le=6)
    body_index: float = Field(default=0.0, ge=0, le=100)
    magic_rating: int = Field(default=0, ge=0, le=20)
    magic_type: Optional[str] = Field(default=None, max_length=50)
    tradition: Optional[str] = Field(default=None, max_length=50)
    totem: Optional[str] = Field(default=None, max_length=50)
    nuyen: int = Field(default=0, ge=0)
    karma_pool: int = Field(default=1, ge=0)
    good_karma: int = Field(default=0, ge=0)
    lifestyle_level: Optional[int] = Field(default=None, ge=0, le=5)
    lifestyle_permanent: bool = False
    is_draft: bool = False
    priorities: dict = {}
    skills: list = []
    spells: list = []
    adept_powers: list = []
    gear: dict = {}
    organization_id: Optional[int] = None


class CharacterCreate(CharacterBase):
    model_config = ConfigDict(extra='forbid')


class DossierContact(BaseModel):
    """A runner's chargen contact -> a real Contact row owned by the new PC."""
    model_config = ConfigDict(extra='forbid')
    name: str = Field(max_length=200)
    profession: Optional[str] = Field(default=None, max_length=100)
    connection: int = Field(default=1, ge=1, le=6)
    loyalty: int = Field(default=1, ge=1, le=6)


class DossierCommit(CharacterCreate):
    """Full chargen commit: the character sheet plus the contacts to create with it."""
    contacts: list[DossierContact] = []


class LifestylePurchase(BaseModel):
    """Buy/upgrade a lifestyle after chargen, paid from the character's nuyen."""
    model_config = ConfigDict(extra='forbid')
    level: int = Field(ge=0, le=5)
    permanent: bool = False
    months: int = Field(default=1, ge=0, le=120)  # months of upkeep to prepay (ignored if permanent)


class CharacterUpdate(BaseModel):
    model_config = ConfigDict(extra='forbid')
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
    computer_skill_enabled: Optional[bool] = None
    computer_skill_rating: Optional[int] = Field(default=None, ge=0, le=20)
    software_skill_enabled: Optional[bool] = None
    software_skill_rating: Optional[int] = Field(default=None, ge=0, le=20)
    matrix_skill_enabled: Optional[bool] = None
    matrix_skill_rating: Optional[int] = Field(default=None, ge=0, le=20)
    computer_br_skill_enabled: Optional[bool] = None
    computer_br_skill_rating: Optional[int] = Field(default=None, ge=0, le=20)
    math_spu_enabled: Optional[bool] = None
    math_spu_rating: Optional[int] = Field(default=None, ge=0, le=4)
    intelligence: Optional[int] = Field(default=None, ge=0, le=20)
    quickness: Optional[int] = Field(default=None, ge=0, le=12)
    willpower: Optional[int] = Field(default=None, ge=0, le=20)
    body: Optional[int] = Field(default=None, ge=0, le=12)
    strength: Optional[int] = Field(default=None, ge=0, le=20)
    charisma: Optional[int] = Field(default=None, ge=0, le=20)
    essence: Optional[float] = Field(default=None, ge=0, le=6)
    body_index: Optional[float] = Field(default=None, ge=0, le=100)
    magic_rating: Optional[int] = Field(default=None, ge=0, le=20)
    magic_type: Optional[str] = Field(default=None, max_length=50)
    tradition: Optional[str] = Field(default=None, max_length=50)
    totem: Optional[str] = Field(default=None, max_length=50)
    nuyen: Optional[int] = Field(default=None, ge=0)
    karma_pool: Optional[int] = Field(default=None, ge=0)
    good_karma: Optional[int] = Field(default=None, ge=0)
    lifestyle_level: Optional[int] = Field(default=None, ge=0, le=5)
    lifestyle_permanent: Optional[bool] = None
    is_draft: Optional[bool] = None
    priorities: Optional[dict] = None
    skills: Optional[list] = None
    spells: Optional[list] = None
    adept_powers: Optional[list] = None
    gear: Optional[dict] = None
    organization_id: Optional[int] = None


class CharacterRead(CharacterBase):
    id: int
    created_at: datetime
    updated_at: datetime
    organization_name: Optional[str] = None
    lifestyle_name: Optional[str] = None
    lifestyle_monthly_cost: int = 0
    lifestyle_paid_tick: Optional[int] = None
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
