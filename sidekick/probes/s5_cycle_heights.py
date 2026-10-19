"""S5 appendix data: dyadic heights B = floor(log2(H/L)) of actual reduced 3x+q cycles (odd q < 1000,
3 not dividing q, starts <= 3001, orbits capped at 6000 steps), against the period m. Data only; the sample
has small minima, while q = 1 cycles would have L > 2^71.
"""
import sys, math
from collections import defaultdict
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step
rows = []
for q in [q for q in range(1, 1000, 2) if q % 3 != 0]:
    for cyc in cycles(q, 3001, max_steps=6000):
        m = len(cyc)
        if m < 2 or math.gcd(q, min(cyc)) != 1: continue
        L, H = min(cyc), max(cyc)
        B = int(math.floor(math.log2(H / L)))
        rows.append((m, B, q, L))
rows.sort()
print("reduced cycles with m >= 2:", len(rows))
bym = defaultdict(int)
for m, B, q, L in rows: bym[m] = max(bym[m], B)
big = [r for r in rows if r[0] >= 50]
print("max B by m-bucket:")
for lo, hi in [(2,10),(10,30),(30,60),(60,100),(100,200),(200,400),(400,10**6)]:
    sel = [r for r in rows if lo <= r[0] < hi]
    if sel: print(f"  m in [{lo},{hi}): n={len(sel)}, max B={max(r[1] for r in sel)}, max B/m={max(r[1]/r[0] for r in sel):.3f}, max B/log2(m)={max(r[1]/math.log2(r[0]) for r in sel):.2f}")
print("tallest relative to m (B/m):", sorted(rows, key=lambda r: -r[1]/r[0])[:5])
