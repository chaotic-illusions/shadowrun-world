#!/usr/bin/env python3
"""
Decay simulator — shows per-tick evolution of heat, PA, and org standings.

Usage:
    python decay_sim.py [options]

Options:
    --heat INT          Starting heat value (0-10)          [default: 5]
    --pa INT            Starting public awareness (0-13)    [default: 4]
    --standing INT      Starting org standing (-10 to 10)   [default: 6]
    --ticks INT         Number of ticks (days) to simulate  [default: 60]
    --step INT          Days per displayed row               [default: 7]
    --lying-low         Apply 2× decay acceleration (lying low)

Examples:
    python decay_sim.py --heat 8 --pa 7 --standing -5 --ticks 90 --step 7
    python decay_sim.py --heat 6 --lying-low --ticks 30 --step 3
"""

import argparse
import math
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app.services.heat_calculator import (
    decay_heat, decay_pa, decay_standing,
    heat_label, pa_label, standing_label,
    LYING_LOW_DECAY_ACCEL,
)


def _bar(val: float, lo: float, hi: float, width: int = 20) -> str:
    frac = (val - lo) / (hi - lo) if hi > lo else 0.0
    filled = round(max(0.0, min(1.0, frac)) * width)
    return "[" + "█" * filled + "░" * (width - filled) + "]"


def simulate(heat: int, pa: int, standing: int, ticks: int, step: int, lying_low: bool):
    accel = LYING_LOW_DECAY_ACCEL if lying_low else 1.0
    accel_label = f" (lying low ×{accel:.0f})" if lying_low else ""

    print()
    print(f"  Decay Simulation{accel_label}")
    print(f"  Start: heat={heat} ({heat_label(heat)})  "
          f"pa={pa} ({pa_label(pa)})  "
          f"standing={standing:+d} ({standing_label(standing)})")
    print(f"  Ticks: {ticks} days  |  Step: {step} days/row")
    print()

    # Column widths
    W_DAY = 5
    W_VAL = 7
    W_LBL = 22
    W_BAR = 22

    # Header
    print(f"  {'Day':>{W_DAY}}  "
          f"{'Heat':>{W_VAL}} {'':>{W_LBL}} {'':>{W_BAR}}  "
          f"{'PA':>{W_VAL}} {'':>{W_LBL}} {'':>{W_BAR}}  "
          f"{'Standing':>{W_VAL}} {'':>{W_LBL}}")
    print("  " + "-" * (W_DAY + (W_VAL + 1 + W_LBL + 1 + W_BAR + 2) * 3))

    prev_heat = prev_pa = prev_standing = None

    for day in range(0, ticks + 1, step):
        h = decay_heat(heat, day, accel)
        p = decay_pa(pa, day, accel)
        s = decay_standing(standing, day, accel)

        hi = round(h, 2)
        pi = round(p, 2)
        si = round(s, 2)

        hl = heat_label(math.floor(hi))
        pl = pa_label(math.floor(pi))
        sl = standing_label(math.ceil(si))

        # Delta arrows
        def delta(cur, prev):
            if prev is None:
                return " "
            diff = cur - prev
            if abs(diff) < 0.01:
                return "="
            return "▼" if diff < 0 else "▲"

        dh = delta(hi, prev_heat)
        dp = delta(pi, prev_pa)
        ds = delta(si, prev_standing)

        hbar = _bar(hi, 0, 10)
        pbar = _bar(pi, 0, 13)
        sbar = _bar(abs(si), 0, 10)

        print(f"  {day:>{W_DAY}}  "
              f"{hi:>{W_VAL}.2f}{dh} {hl:<{W_LBL}} {hbar}  "
              f"{pi:>{W_VAL}.2f}{dp} {pl:<{W_LBL}} {pbar}  "
              f"{si:>+{W_VAL}.2f}{ds} {sl:<{W_LBL}}")

        prev_heat = hi
        prev_pa = pi
        prev_standing = si

    print()

    # Summary: days to cross each tier boundary
    print("  --- Tier crossings ---")
    _summarise_crossings("Heat",     heat,     ticks, accel, decay_heat,    heat_label,     [(0,0),(1,2),(3,4),(5,6),(7,8),(9,10)])
    _summarise_crossings("PA",       pa,       ticks, accel, decay_pa,      pa_label,       [(0,0),(1,3),(4,7),(8,12),(13,99)])
    _summarise_crossings("Standing", standing, ticks, accel, decay_standing,standing_label, [(-10,-7),(-6,-3),(-2,2),(3,6),(7,10)])
    print()


def _summarise_crossings(name, start_val, ticks, accel, fn, label_fn, tiers):
    if start_val == 0:
        print(f"  {name}: already at base (no decay)")
        return

    _int_fn = math.floor if name != "Standing" else math.ceil
    prev_label = label_fn(_int_fn(start_val))
    crossings = []
    for day in range(1, ticks + 1):
        val = fn(start_val, day, accel)
        lbl = label_fn(_int_fn(val))
        if lbl != prev_label:
            crossings.append((day, prev_label, lbl, round(val, 2)))
            prev_label = lbl

    if crossings:
        parts = [f"day {d}: {frm} → {to} ({v:+.2f})" for d, frm, to, v in crossings]
        print(f"  {name}: {' | '.join(parts)}")
    else:
        final = fn(start_val, ticks, accel)
        print(f"  {name}: stays '{prev_label}' entire window (value {final:.2f} at day {ticks})")


def main():
    p = argparse.ArgumentParser(description="Shadowrun decay simulator")
    p.add_argument("--heat",      type=int, default=5,  help="Starting heat (0-10)")
    p.add_argument("--pa",        type=int, default=4,  help="Starting public awareness (0-13)")
    p.add_argument("--standing",  type=int, default=6,  help="Starting org standing (-10 to 10)")
    p.add_argument("--ticks",     type=int, default=60, help="Days to simulate")
    p.add_argument("--step",      type=int, default=7,  help="Days per displayed row")
    p.add_argument("--lying-low", action="store_true",  help="Apply 2× decay acceleration")
    args = p.parse_args()

    simulate(
        heat=max(0, min(10, args.heat)),
        pa=max(0, min(13, args.pa)),
        standing=max(-10, min(10, args.standing)),
        ticks=args.ticks,
        step=args.step,
        lying_low=args.lying_low,
    )


if __name__ == "__main__":
    main()
