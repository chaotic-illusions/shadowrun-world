"""The PDF export (tools/fill_sr2_sheet.py) prints the same armor and Reaction/Initiative as the play
sheet: Mystic Armor is Impact only; physical Reaction/Initiative take the greater of the cyber/bio
boost and the adept power; rigging gets only the VCR's bonuses."""
from tools.fill_sr2_sheet import build_fields


def _char(**over):
    c = {"id": 1, "name": "Test", "race": "Human", "gender": None, "age": None, "archetype": None,
         "body": 4, "quickness": 5, "strength": 4, "charisma": 3, "intelligence": 5, "willpower": 4,
         "essence": 6.0, "magic_rating": 0, "magic_type": None, "karma_pool": 1, "good_karma": 0, "nuyen": 0,
         "skills": [], "spells": [], "adept_powers": [], "gear": {}, "priorities": {}, "chargen_state": {}}
    c.update(over)
    return c


def test_mystic_armor_adds_impact_only():
    c = _char(magic_type="Adept", adept_powers=[{"name": "Mystic Armor", "rated": True, "lvl": 1}],
              gear={"armor": [{"n": "Lined Coat"}]})
    assert build_fields(c, [])["Armor Rating 1"] == "4/3"


def test_reaction_and_initiative_match_the_sheet():
    cyber = [{"n": "Vehicle Control Rig", "rating": 1, "modsPer": {"reaction": 2, "initDice": 1}},
             {"n": "Wired Reflexes", "rating": 1, "modsPer": {"reaction": 2, "initDice": 1}},
             {"n": "Muscle Replacement", "rating": 1, "modsPer": {"quickness": 1, "strength": 1}}]
    f = build_fields(_char(gear={"cyber": cyber}), [])
    # Physical (5+5)/2 + Wired 2 = 7, 2D6; rigging (5+5)/2 + VCR 2 = 7, 2D6 (no Wired Reflexes).
    assert f["Reaction"] == "7 / 7"
    assert f["Initiative"] == "2D6 / 2D6"

    adept = _char(magic_type="Adept", gear={"cyber": [cyber[1]]},
                  adept_powers=[{"name": "Increased Reaction", "rated": True, "lvl": 3},
                                {"name": "Increased Reflexes", "rated": True, "lvl": 2}])
    f = build_fields(adept, [])
    assert f["Reaction"] == "8" and f["Initiative"] == "3D6"   # the greater of cyber and power, never both
