from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


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
