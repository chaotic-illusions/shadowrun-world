from typing import Optional, Union

from pydantic import BaseModel, ConfigDict, field_validator

from app.data import catalog as cat


class CoreBook(BaseModel):
    code: str
    name: str


class BookInfo(BaseModel):
    code: str
    name: str
    enabled: bool = False


class FanBook(BaseModel):
    code: str
    name: str
    enabled: bool = False
    includes: list[str] = []


class BookSettingsRead(BaseModel):
    core: CoreBook
    official: list[BookInfo]
    fan: FanBook
    enabled: list[str]


class BookSettingsUpdate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    enabled: list[str]

    @field_validator("enabled")
    @classmethod
    def _known_codes(cls, value: list[str]) -> list[str]:
        unknown = sorted(set(value) - cat.TOGGLEABLE_CODES)
        if unknown:
            raise ValueError(f"Unknown book codes: {', '.join(unknown)}")
        return value


_CYBER_CATS = {"headware", "bodyware", "eyeware", "earware", "limb", "other"}


class CyberwareCreate(BaseModel):
    """One cyberware item to append to the catalog (admin data-entry form).

    Mirrors the on-disk catalog shape. ``ess``/``cost``/``index`` accept a number
    or a formula string (e.g. ``"0.2/lvl"``, ``"4,500\u00a5/lvl"``). Rated items
    supply per-level ``essTbl``/``costTbl`` plus ``maxRating``; attribute-boosting
    items supply ``mods`` (fixed total) or ``modsPer`` (per level).
    """

    model_config = ConfigDict(extra="forbid")

    n: str
    cat: str
    ess: Union[int, float, str, None] = None
    cost: Union[int, float, str]
    avail: str = "-"
    index: Union[int, float, str] = 1
    desc: str = ""
    effect: list[str] = []
    src: str = "SHADOW"
    pg: Optional[int] = None
    rated: Optional[bool] = None
    maxRating: Optional[int] = None
    essTbl: Optional[list[float]] = None
    costTbl: Optional[list[float]] = None
    mods: Optional[dict[str, int]] = None
    modsPer: Optional[dict[str, int]] = None

    @field_validator("n")
    @classmethod
    def _name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("name is required")
        return value

    @field_validator("cat")
    @classmethod
    def _cat(cls, value: str) -> str:
        value = value.strip().lower()
        if value not in _CYBER_CATS:
            raise ValueError(f"cat must be one of: {', '.join(sorted(_CYBER_CATS))}")
        return value

    @field_validator("effect")
    @classmethod
    def _effect(cls, value: list[str]) -> list[str]:
        return [s.strip() for s in value if isinstance(s, str) and s.strip()]

    @field_validator("src")
    @classmethod
    def _src(cls, value: str) -> str:
        value = value.strip().upper()
        return value or "SHADOW"

    def to_item(self) -> dict:
        """Build the catalog dict in the canonical field order, dropping unset optionals."""
        item: dict = {
            "n": self.n,
            "cat": self.cat,
            "ess": self.ess,
            "cost": self.cost,
            "avail": self.avail,
            "index": self.index,
            "desc": self.desc,
            "effect": self.effect,
        }
        if self.mods:
            item["mods"] = self.mods
        if self.rated:
            item["rated"] = True
            if self.maxRating is not None:
                item["maxRating"] = self.maxRating
            if self.essTbl is not None:
                item["essTbl"] = self.essTbl
            if self.costTbl is not None:
                item["costTbl"] = self.costTbl
        if self.modsPer:
            item["modsPer"] = self.modsPer
        item["src"] = self.src
        if self.pg is not None:
            item["pg"] = self.pg
        return item


class ContactArchetypeCreate(BaseModel):
    """One contact/NPC archetype to append to an existing group in the shared
    ``contact_archetypes`` catalog (admin data-entry form)."""

    model_config = ConfigDict(extra="forbid")

    name: str
    group: str

    @field_validator("name")
    @classmethod
    def _name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("name is required")
        return value

    @field_validator("group")
    @classmethod
    def _group(cls, value: str) -> str:
        value = value.strip()
        known = cat.get_rules().get("contact_archetypes", {})
        if value not in known:
            raise ValueError(f"group must be one of: {', '.join(sorted(known))}")
        return value


class ArchetypeStarterSkillsUpdate(BaseModel):
    """Replace the suggested starter-skill list for one contact/NPC archetype
    (admin data-entry form). An empty list clears the template."""

    model_config = ConfigDict(extra="forbid")

    skills: list[str] = []
