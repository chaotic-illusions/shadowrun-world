"""Unit tests for the lifestyle upkeep engine (app/services/lifestyle.py).

Pure, in-memory Character objects -- no DB. Covers first-sight stamping, monthly
charges, multi-month catch-up, eviction when rent can't be paid, permanent
lifestyles, and Street (free) upkeep.
"""
from app.models.character import Character
from app.services.lifestyle import monthly_cost, permanent_cost, settle_lifestyle


def _pc(level=None, nuyen=0, paid_tick=None, permanent=False):
    return Character(
        name="Runner", is_pc=True, lifestyle_level=level, nuyen=nuyen,
        lifestyle_paid_tick=paid_tick, lifestyle_permanent=permanent,
    )


def test_monthly_and_permanent_cost_tables():
    assert monthly_cost(0) == 0          # Street
    assert monthly_cost(2) == 1000       # Low
    assert monthly_cost(5) == 100000     # Luxury
    assert monthly_cost(None) == 0
    assert permanent_cost(2) == 100000   # 100 months of Low
    assert permanent_cost(4) == 1000000  # 100 months of High


def test_no_lifestyle_is_noop():
    pc = _pc(level=None, nuyen=5000)
    assert settle_lifestyle(pc, 90) is False
    assert pc.nuyen == 5000


def test_first_sight_stamps_without_charging():
    pc = _pc(level=3, nuyen=5000, paid_tick=None)
    assert settle_lifestyle(pc, 120) is True
    assert pc.lifestyle_paid_tick == 120  # paid "through now" -- no back-rent
    assert pc.nuyen == 5000


def test_charges_one_month():
    pc = _pc(level=2, nuyen=5000, paid_tick=0)   # Low, 1000/mo
    assert settle_lifestyle(pc, 30) is True
    assert pc.nuyen == 4000
    assert pc.lifestyle_paid_tick == 30


def test_partial_month_not_yet_charged():
    pc = _pc(level=2, nuyen=5000, paid_tick=0)
    assert settle_lifestyle(pc, 29) is False
    assert pc.nuyen == 5000
    assert pc.lifestyle_paid_tick == 0


def test_catches_up_multiple_months_and_carries_remainder():
    pc = _pc(level=2, nuyen=5000, paid_tick=0)   # Low, 1000/mo
    assert settle_lifestyle(pc, 95) is True       # 3 full months (90 ticks), 5 carried
    assert pc.nuyen == 2000
    assert pc.lifestyle_paid_tick == 90


def test_eviction_drops_a_tier_per_unaffordable_month():
    pc = _pc(level=3, nuyen=0, paid_tick=0)        # Middle 5000 -> can't pay
    # 3 months with no money: Middle -> Low -> Squatter -> Street, no charges.
    assert settle_lifestyle(pc, 90) is True
    assert pc.lifestyle_level == 0
    assert pc.nuyen == 0
    assert pc.lifestyle_paid_tick == 90


def test_street_is_free():
    pc = _pc(level=0, nuyen=0, paid_tick=0)
    assert settle_lifestyle(pc, 300) is True
    assert pc.lifestyle_level == 0
    assert pc.nuyen == 0
    assert pc.lifestyle_paid_tick == 300


def test_permanent_lifestyle_is_never_charged():
    pc = _pc(level=5, nuyen=100, paid_tick=0, permanent=True)  # Luxury, but bought outright
    assert settle_lifestyle(pc, 3650) is True     # keeps the stamp current
    assert pc.nuyen == 100
    assert pc.lifestyle_level == 5
    assert pc.lifestyle_paid_tick == 3650
