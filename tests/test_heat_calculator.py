"""Tests for the heat calculator and reputation decay system."""
import math
import pytest
from app.services.heat_calculator import (
    heat_label, standing_label, pc_rep_label, team_rep_label, pa_label,
    compute_heat, compute_ripple,
    decay_heat, decay_pa, decay_standing,
    LYING_LOW_DECAY_ACCEL,
)


# -- Label functions ----------------------------------------------------------

class TestHeatLabel:
    def test_neutral(self):
        assert heat_label(0) == "Neutral"

    def test_noticed(self):
        assert heat_label(1) == "Noticed"
        assert heat_label(2) == "Noticed"

    def test_nova_hot(self):
        assert heat_label(9) == "Nova Hot"
        assert heat_label(10) == "Nova Hot"

    def test_out_of_range(self):
        assert heat_label(15) == "Nova Hot"


class TestStandingLabel:
    def test_neutral_range(self):
        for v in (-2, -1, 0, 1, 2):
            assert standing_label(v) == "neutral"

    def test_hostile(self):
        assert standing_label(-10) == "hostile"
        assert standing_label(-7) == "hostile"

    def test_allied(self):
        assert standing_label(10) == "allied"
        assert standing_label(7) == "allied"


class TestRepLabels:
    def test_nobody_baseline(self):
        assert pc_rep_label(20) == "Nobody"

    def test_legend(self):
        assert pc_rep_label(40) == "Legend"

    def test_infamous(self):
        assert pc_rep_label(0) == "Infamous"

    def test_team_unknown(self):
        assert team_rep_label(20) == "Unknown"

    def test_pa_shadow(self):
        assert pa_label(0) == "Shadow"

    def test_pa_burned(self):
        assert pa_label(15) == "Burned"


# -- compute_heat -------------------------------------------------------------

class TestComputeHeat:
    def test_clean_success(self):
        h = compute_heat("success", [])
        assert 0 <= h <= 10
        assert h == 2  # base for success

    def test_loud_run(self):
        h = compute_heat("success", ["witnesses", "collateral_damage", "media_attention"])
        assert h > 2  # tags add heat

    def test_capped_at_10(self):
        h = compute_heat("critical_failure", [
            "witnesses", "collateral_damage", "public_scene",
            "media_attention", "casualties",
        ], employer_tier=6)
        assert h == 10

    def test_employer_tier_bonus(self):
        low = compute_heat("success", [], employer_tier=1)
        high = compute_heat("success", [], employer_tier=6)
        assert high > low

    def test_unknown_outcome(self):
        h = compute_heat("something_weird", [])
        assert h == 2  # defaults to base of 2


# -- Decay functions ----------------------------------------------------------

class TestDecayHeat:
    def test_no_decay_at_zero(self):
        assert decay_heat(0, 100) == 0.0

    def test_no_decay_at_zero_elapsed(self):
        assert decay_heat(5, 0) == 5.0

    def test_decays_over_time(self):
        original = 5
        decayed = decay_heat(original, 14)
        assert 0 < decayed < original

    def test_accelerated_decay(self):
        normal = decay_heat(5, 10, accel=1.0)
        fast = decay_heat(5, 10, accel=LYING_LOW_DECAY_ACCEL)
        assert fast < normal


class TestDecayPA:
    def test_shadow_unchanged(self):
        assert decay_pa(0, 100) == 0.0

    def test_decays(self):
        assert 0 < decay_pa(5, 14) < 5

    def test_accelerated(self):
        normal = decay_pa(5, 10, accel=1.0)
        fast = decay_pa(5, 10, accel=2.0)
        assert fast < normal


class TestDecayStanding:
    def test_neutral_unchanged(self):
        assert decay_standing(0, 100) == 0.0

    def test_positive_decays_toward_zero(self):
        result = decay_standing(8, 20)
        assert 0 < result < 8

    def test_negative_decays_toward_zero(self):
        result = decay_standing(-8, 20)
        assert -8 < result < 0


# -- Faction ripple -----------------------------------------------------------

class TestComputeRipple:
    @pytest.fixture
    def org_map(self):
        return {
            1: {"name": "Ares", "ally_ids": [2], "enemy_ids": [3]},
            2: {"name": "Knight Errant", "ally_ids": [1], "enemy_ids": []},
            3: {"name": "Shadowrunners Local", "ally_ids": [], "enemy_ids": [1]},
        }

    def test_basic_ripple(self, org_map):
        results = compute_ripple(1, +3, org_map)
        assert len(results) == 2

        ally_change = next(r for r in results if r["org_id"] == 2)
        assert ally_change["delta"] > 0  # ally gets positive ripple

        enemy_change = next(r for r in results if r["org_id"] == 3)
        assert enemy_change["delta"] < 0  # enemy gets negative ripple

    def test_no_ripple_for_zero_delta(self, org_map):
        assert compute_ripple(1, 0, org_map) == []

    def test_unknown_org(self, org_map):
        assert compute_ripple(999, 3, org_map) == []

    def test_negative_delta_reverses(self, org_map):
        results = compute_ripple(1, -3, org_map)
        ally_change = next(r for r in results if r["org_id"] == 2)
        assert ally_change["delta"] < 0  # ally takes negative hit too
