import pytest
from pydantic import ValidationError

from app.schemas.organization import OrganizationCreate, OrganizationUpdate


DIVISION_ID = "11111111-1111-4111-8111-111111111111"


def test_organization_accepts_valid_division():
    org = OrganizationCreate(
        name="Ares Arms",
        divisions=[{
            "id": DIVISION_ID,
            "name": "Seattle Division",
            "kind": "division",
            "visibility": "listed",
        }],
    )

    assert org.divisions[0].id == DIVISION_ID
    assert org.divisions[0].revealed is False


@pytest.mark.parametrize("field,value", [
    ("id", "not-a-uuid"),
    ("kind", "team"),
    ("visibility", "secret"),
])
def test_organization_rejects_invalid_division_values(field, value):
    division = {
        "id": DIVISION_ID,
        "name": "Seattle Division",
        "kind": "division",
        "visibility": "listed",
    }
    division[field] = value

    with pytest.raises(ValidationError):
        OrganizationCreate(name="Ares Arms", divisions=[division])


def test_organization_rejects_duplicate_division_ids_on_update():
    division = {
        "id": DIVISION_ID,
        "name": "Seattle Division",
        "kind": "division",
    }

    with pytest.raises(ValidationError, match="division ids must be unique"):
        OrganizationUpdate(divisions=[division, {**division, "name": "Second Division"}])