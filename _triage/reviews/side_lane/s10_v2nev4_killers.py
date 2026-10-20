"""S10: v2 != v4 grid with h offset off rationals (no trivial k h); histogram of the rotation that kills each point (~1 min)."""
# v2 != v4, rotations up to 12h, with h offset off exact rationals (no k h == 0 mod 1 for k <= 12),
# recording for each (h,2h)-feasible point the rotation k with the largest violation, and skipping any
# k with k h within 1e-6 of an integer (reported).
import sys
from collections import Counter
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s10_multirotation_lp import margin, pts_for, grid
OFF = 1.2345e-7
def near_int(x): return abs(x - round(x)) < 1e-6
n2, best, killers, skipped = 0, None, Counter(), 0
for h, p1, p2 in grid(0.0025, 0.005):
    h = h + OFF
    if margin(pts_for(1, h, p1, p2, False), h % 1.0) < 0: continue
    if near_int(2 * h) or margin(pts_for(2, h, p1, p2, False), (2 * h) % 1.0) < 0: continue
    n2 += 1
    ms = []
    for k in range(3, 13):
        if near_int(k * h): skipped += 1; continue
        ms.append((margin(pts_for(k, h, p1, p2, False), (k * h) % 1.0), k))
    mn, kk = min(ms)
    killers[kk] += 1
    if best is None or mn > best[0]: best = (round(mn, 4), round(h, 6), round(p1, 4), round(p2, 4), kk)
print("(h,2h)-feasible:", n2, " best min margin over 3h..12h:", best, " skipped trivial k:", skipped)
print("killing rotation histogram:", sorted(killers.items()))
