from datetime import datetime, UTC
from typing import Optional
from sqlalchemy import String, Text, Integer, Float, ForeignKey, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base
from app.models.associations import log_characters

# SR2 lifestyle tiers, indexed by ordinal level (0=Street ... 5=Luxury).
LIFESTYLE_TIERS = ("Street", "Squatter", "Low", "Middle", "High", "Luxury")

# SR2 p.245 monthly upkeep per lifestyle tier, indexed like LIFESTYLE_TIERS.
LIFESTYLE_MONTHLY_COST = (0, 100, 1000, 5000, 10000, 100000)

# Upkeep is charged one "month" at a time; 30 ticks (days) == 1 month.
LIFESTYLE_UPKEEP_TICKS = 30

# Buying a lifestyle outright (never charged upkeep again) costs this many months.
LIFESTYLE_PERMANENT_MONTHS = 100


def lifestyle_monthly_cost_for(level: int | None, permanent: bool = False) -> int:
    """Canonical monthly upkeep for a lifestyle tier (0 for Street/unset/out-of-range/permanent).

    Single source of truth shared by the ORM property and the lifestyle service.
    """
    if permanent or level is None or not (0 <= level < len(LIFESTYLE_MONTHLY_COST)):
        return 0
    return LIFESTYLE_MONTHLY_COST[level]


class Character(Base):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    is_pc: Mapped[bool] = mapped_column(default=True)
    archetype: Mapped[str | None] = mapped_column(String(100), default=None)
    title: Mapped[str | None] = mapped_column(String(200), default=None)
    race: Mapped[str] = mapped_column(String(50), default="Human")
    nationality: Mapped[str | None] = mapped_column(String(100), default=None)
    gender: Mapped[str | None] = mapped_column(String(50), default=None)
    age: Mapped[int | None] = mapped_column(Integer, default=None)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    background: Mapped[str | None] = mapped_column(Text, default=None)
    show_background: Mapped[bool] = mapped_column(default=False)
    # Relative URL under the /uploads static mount (see app/main.py), e.g. "/uploads/portraits/<uuid>.jpg".
    portrait_url: Mapped[str | None] = mapped_column(String(500), default=None)

    # Services/skills this NPC can provide as a contact
    contact_skills: Mapped[list] = mapped_column(JSON, default=list)

    # NPC connection rating (1-6); not applicable to PCs
    connection: Mapped[int] = mapped_column(Integer, default=1)

    # Deck-programming skill controls (PC-focused).
    computer_skill_enabled: Mapped[bool] = mapped_column(default=False)
    computer_skill_rating: Mapped[int] = mapped_column(Integer, default=0)
    software_skill_enabled: Mapped[bool] = mapped_column(default=False)
    software_skill_rating: Mapped[int] = mapped_column(Integer, default=0)
    matrix_skill_enabled: Mapped[bool] = mapped_column(default=False)
    matrix_skill_rating: Mapped[int] = mapped_column(Integer, default=0)
    computer_br_skill_enabled: Mapped[bool] = mapped_column(default=False)
    computer_br_skill_rating: Mapped[int] = mapped_column(Integer, default=0)
    # Math SPU cyberware: adds floor(rating/2) to Intelligence for Hacking Pool. 0 when disabled.
    math_spu_enabled: Mapped[bool] = mapped_column(default=False)
    math_spu_rating: Mapped[int] = mapped_column(Integer, default=0)
    # GM authorization to buy Beta/Delta-grade cyberware post-chargen (narratively gated, never
    # player-writable -- see _PLAYER_WRITABLE_FIELDS in app/routers/characters.py). Defaults False
    # so no existing character is auto-approved.
    beta_grade_approved: Mapped[bool] = mapped_column(default=False)
    delta_grade_approved: Mapped[bool] = mapped_column(default=False)
    intelligence: Mapped[int] = mapped_column(Integer, default=0)
    quickness: Mapped[int] = mapped_column(Integer, default=0)
    willpower: Mapped[int] = mapped_column(Integer, default=0)
    body: Mapped[int] = mapped_column(Integer, default=0)
    strength: Mapped[int] = mapped_column(Integer, default=0)
    charisma: Mapped[int] = mapped_column(Integer, default=0)

    # SR2 character-sheet vitals, promoted from JSON so other tools (initiative
    # tracker, matrix run) can query them directly.
    essence: Mapped[float] = mapped_column(Float, default=6.0)
    body_index: Mapped[float] = mapped_column(Float, default=0.0)
    magic_rating: Mapped[int] = mapped_column(Integer, default=0)
    magic_type: Mapped[str | None] = mapped_column(String(50), default=None)
    tradition: Mapped[str | None] = mapped_column(String(50), default=None)
    totem: Mapped[str | None] = mapped_column(String(50), default=None)
    nuyen: Mapped[int] = mapped_column(Integer, default=0)
    karma_pool: Mapped[int] = mapped_column(Integer, default=1)
    good_karma: Mapped[int] = mapped_column(Integer, default=0)
    # Condition monitor: 10-box Physical/Stun tracks (boxes filled, 0-10) plus Physical Overflow
    # (boxes filled beyond the 10th Physical box; capped client-side at the Body attribute).
    physical_damage: Mapped[int] = mapped_column(Integer, default=0)
    stun_damage: Mapped[int] = mapped_column(Integer, default=0)
    physical_overflow: Mapped[int] = mapped_column(Integer, default=0)
    # Ordinal lifestyle tier (0=Street ... 5=Luxury); None until set. See LIFESTYLE_TIERS.
    lifestyle_level: Mapped[int | None] = mapped_column(Integer, default=None)
    # Lifestyle bought outright (100 months up front): never charged monthly upkeep again.
    lifestyle_permanent: Mapped[bool] = mapped_column(default=False)
    # Campaign tick through which lifestyle upkeep has been settled. None until the PC starts
    # "living" (stamped when a dossier is committed); the upkeep engine advances it 30 ticks at
    # a time as it charges rent. See app/services/lifestyle.py.
    lifestyle_paid_tick: Mapped[int | None] = mapped_column(Integer, default=None)
    # In-progress chargen draft: hidden from every character list until the wizard finalizes it.
    # Exists so the Deck Workshop can attach to a real row while the dossier is still being built.
    is_draft: Mapped[bool] = mapped_column(default=False)

    # Catalog-heavy, list-shaped chargen data stays JSON (plan S2).
    priorities: Mapped[dict] = mapped_column(JSON, default=dict)
    skills: Mapped[list] = mapped_column(JSON, default=list)
    spells: Mapped[list] = mapped_column(JSON, default=list)
    adept_powers: Mapped[list] = mapped_column(JSON, default=list)
    gear: Mapped[dict] = mapped_column(JSON, default=dict)

    # Cross-device/browser persisted deck-builder state (programs, loadouts, jobs).
    deck_builder_state: Mapped[dict] = mapped_column(JSON, default=dict)

    # Raw character-builder wizard state, stored verbatim so a saved draft round-trips losslessly
    # (contacts with type/gang, legal name, and every other free-text input). Structured columns
    # above still drive gameplay; this is the editable-input backup for resuming the wizard.
    chargen_state: Mapped[dict] = mapped_column(JSON, default=dict)

    organization_id: Mapped[int | None] = mapped_column(ForeignKey("organizations.id"), default=None)

    # When organization_id is null, distinguishes a deliberately unaffiliated NPC ("Independent",
    # is_independent=True) from one whose ties simply aren't known ("Unknown", the default).
    is_independent: Mapped[bool] = mapped_column(default=False)

    is_active: Mapped[bool] = mapped_column(default=True)
    notes: Mapped[str | None] = mapped_column(Text, default=None)
    # SHA-256 hash of the owning player's token
    owner_token: Mapped[str | None] = mapped_column(String(64), default=None, index=True)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC)
    )

    # Optimistic-lock counter (declared as version_id_col below), same pattern as MatrixRun. SQLAlchemy
    # adds `WHERE version = :old` to every UPDATE and raises StaleDataError (caught globally in
    # app/main.py -> 409) if a concurrent writer already bumped it -- prevents two overlapping PATCHes
    # (e.g. two browser tabs buying gear) from silently clobbering each other's whole-object `gear`/
    # `chargen_state` JSON replacement.
    version: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    organization: Mapped[Optional["Organization"]] = relationship(
        "Organization", foreign_keys=[organization_id]
    )

    @property
    def organization_name(self) -> str | None:
        return self.organization.name if self.organization else None

    @property
    def is_claimed(self) -> bool:
        return self.owner_token is not None

    @property
    def lifestyle_name(self) -> str | None:
        level = self.lifestyle_level
        if level is None or not (0 <= level < len(LIFESTYLE_TIERS)):
            return None
        return LIFESTYLE_TIERS[level]

    @property
    def lifestyle_monthly_cost(self) -> int:
        """Nuyen charged per month for the current lifestyle (0 for Street/unset/permanent)."""
        return lifestyle_monthly_cost_for(self.lifestyle_level, self.lifestyle_permanent)

    contacts: Mapped[list["Contact"]] = relationship(
        "Contact", foreign_keys="Contact.owner_id", back_populates="owner", cascade="all, delete-orphan"
    )
    reputation: Mapped[Optional["Reputation"]] = relationship(
        "Reputation", back_populates="character", uselist=False, cascade="all, delete-orphan"
    )
    org_standings: Mapped[list["OrgStanding"]] = relationship(
        "OrgStanding", back_populates="character", cascade="all, delete-orphan"
    )
    adventure_logs: Mapped[list["AdventureLog"]] = relationship(
        "AdventureLog", secondary=log_characters, back_populates="participants"
    )

    __mapper_args__ = {"version_id_col": version}
