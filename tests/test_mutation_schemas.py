"""Contract tests for non-auth, non-matrix mutation schemas."""

from datetime import date

import pytest
from pydantic import ValidationError

from app.schemas.adventure_log import AdventureLogCreate, AdventureLogUpdate
from app.schemas.campaign import AdvanceClockRequest
from app.schemas.character import CharacterCreate, CharacterUpdate
from app.schemas.contact import ContactCreate, ContactUpdate
from app.schemas.deck_builder_state import DeckBuilderStateUpdate
from app.schemas.location import LocationCreate, LocationUpdate
from app.schemas.organization import LtgSecurityUpdate, OrganizationCreate, OrganizationUpdate
from app.schemas.reputation import (
    OrgStandingCreate,
    OrgStandingUpdate,
    ReputationCreate,
    ReputationUpdate,
)
from app.schemas.rtg import RTGCreate, RTGUpdate


MUTATION_CASES = [
    (AdventureLogCreate, {
        "title": "Run",
        "session_date": date(2053, 1, 1),
        "objective": "Extract the target",
        "result": "Target extracted",
    }),
    (AdventureLogUpdate, {}),
    (AdvanceClockRequest, {"days": 1}),
    (CharacterCreate, {"name": "Switch"}),
    (CharacterUpdate, {}),
    (ContactCreate, {"name": "Fixer", "owner_id": 1}),
    (ContactUpdate, {}),
    (DeckBuilderStateUpdate, {}),
    (LocationCreate, {"name": "The Big Rhino"}),
    (LocationUpdate, {}),
    (OrganizationCreate, {"name": "Ares"}),
    (OrganizationUpdate, {}),
    (LtgSecurityUpdate, {"rtg": "NA/UCAS", "ltg": "SEA", "san_access_rating": "Orange-5"}),
    (ReputationCreate, {"character_id": 1}),
    (ReputationUpdate, {}),
    (OrgStandingCreate, {"character_id": 1, "organization_id": 1}),
    (OrgStandingUpdate, {}),
    (RTGCreate, {"code": "NA/UCAS", "region": "United Canadian and American States"}),
    (RTGUpdate, {}),
]


@pytest.mark.parametrize(("schema", "valid_data"), MUTATION_CASES)
def test_mutation_schemas_forbid_unknown_fields(schema, valid_data):
    with pytest.raises(ValidationError, match="Extra inputs are not permitted"):
        schema.model_validate({**valid_data, "unexpected_field": True})


@pytest.mark.parametrize(
    "field,value",
    [
        ("title", "x" * 301),
        ("outcome", "perfect_success"),
        ("payout", "x" * 301),
        ("heat", -1),
        ("heat", 11),
        ("tick_count", -1),
        ("employer", "x" * 201),
        ("participant_ids", list(range(51))),
        ("location_ids", list(range(51))),
        ("org_ids", list(range(51))),
    ],
)
def test_adventure_log_update_preserves_create_constraints(field, value):
    with pytest.raises(ValidationError):
        AdventureLogUpdate.model_validate({field: value})