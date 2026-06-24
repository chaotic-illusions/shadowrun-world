# Import all models here so Base.metadata is fully populated before create_all().
from app.models.associations import log_characters, log_locations, log_organizations  # noqa: F401
from app.models.character import Character  # noqa: F401
from app.models.contact import Contact  # noqa: F401
from app.models.location import Location  # noqa: F401
from app.models.organization import Organization  # noqa: F401
from app.models.reputation import Reputation, OrgStanding  # noqa: F401
from app.models.adventure_log import AdventureLog  # noqa: F401
from app.models.rtg import RTG  # noqa: F401
from app.models.auth import UserToken  # noqa: F401
from app.models.matrix_host import MatrixHost  # noqa: F401
from app.models.matrix_run import MatrixRun    # noqa: F401
from app.models.campaign import CampaignState  # noqa: F401
