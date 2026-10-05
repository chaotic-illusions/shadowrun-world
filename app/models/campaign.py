from sqlalchemy import Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.data.catalog import OFFICIAL_BOOKS
from app.db.base import Base


def _default_enabled_books() -> list:
    """All official sourcebooks on, for a brand-new campaign."""
    return list(OFFICIAL_BOOKS)


class CampaignState(Base):
    """Single-row store for campaign-wide clock state.

    The campaign tick (1 tick = 1 day) is the single source of truth for time
    passing in the world; heat / public-awareness / org-standing decay are all
    computed lazily from how many ticks have elapsed since each value was last
    stamped. Only the Downtime control advances this clock.
    """

    __tablename__ = "campaign_state"

    # Always a single row, id == 1.
    id: Mapped[int] = mapped_column(primary_key=True, default=1)
    # Absolute campaign clock, in ticks (days). Monotonically increasing.
    current_tick: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    # Enabled optional sourcebook toggles for the gear/spell catalogs (SR2 core is
    # always on and never listed here). Default: every official book on.
    enabled_books: Mapped[list] = mapped_column(JSON, nullable=False, default=_default_enabled_books)
    # One-time marker: existing PCs were backfilled to is_independent=True (runners default to
    # "Independent" affiliation). Prevents a startup backfill from re-flipping a deliberate "Unknown".
    pc_affiliation_backfilled: Mapped[bool] = mapped_column(default=False, nullable=False)
    # The team's Karma Pool (SR2 p.191); a new team starts with 2 (p.47). GM-edited only.
    team_karma: Mapped[int] = mapped_column(Integer, nullable=False, default=2)
