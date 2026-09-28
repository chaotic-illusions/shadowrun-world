from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent


def test_manage_organizations_round_trips_divisions():
    source = (ROOT / "frontend" / "manage-organizations.html").read_text(encoding="utf-8")

    assert 'id="divisionBody"' in source
    assert "function addDivision(data)" in source
    assert "function getDivisions()" in source
    assert "(org.divisions || []).forEach" in source
    assert "divisions:    getDivisions()" in source
    assert "row._divisionData" in source


def test_world_state_round_trips_and_renders_divisions():
    html = (ROOT / "frontend" / "world-state.html").read_text(encoding="utf-8")
    source = (ROOT / "frontend" / "world-state.js").read_text(encoding="utf-8")

    assert 'id="oeDivisionBody"' in html
    assert "function oeAddDivision(data)" in source
    assert "function oeGetDivisions()" in source
    assert "(org.divisions || []).forEach" in source
    assert "const divisions = org.divisions || []" in source
    assert "divisions:    oeGetDivisions()" in source
    assert "'corporation':           'megacorp'" in source