"""S10: four mismatches under the rotations h, 2h, 3h at once -- the continuous witness LP.

Model (the S7 structure, at s = 4): scaled positions in [0,1), minimum at 0, a single drop at x = 1-,
the aligned pair x - h, x of sign-change mismatches, and two inner mismatches P1, P2 (chain arcs
[V][v2...][v3...][v4...], every arc longer than k chain steps). Envelope y(p) = sigma p, sigma = log2(3/2)
(the most favourable slope for a hypothetical cycle), ell/m -> 0. The rotation by k h (chain shift k) has
mismatches at x, x - k h, P1 - i h, P2 - i h (0 <= i < k), plus x - i h (1 <= i < k) when v2 != v4.
Each run of each rotation must satisfy  t <= r * pos(witness),  r = sigma/log2 3, witness = the end or its
k h-partner, whichever is higher on the envelope (the end-witness inequality, formal for every rotation).
Default: coarse grid (h step 0.0025, p step 0.005, ~2 min). --fine adds the refinement (~5 min).
BUG FIXED 2026-10-19: the first version placed x - kh at 1 - kh instead of x - kh, so the partner of the run
ending there could wrap to the minimum; that made constraints spuriously hard. All S10 numbers are from the fix.
"""
import json
import math
import sys
from pathlib import Path

SIG = math.log2(1.5)
R = SIG / math.log2(3)


def margin(points, d):
    pts = sorted(set(round(p % 1.0, 12) for p in points))
    worst = 1e9
    for k, e in enumerate(pts):
        t = (e - pts[k - 1]) % 1.0 if len(pts) > 1 else 1.0
        z = max(e, (e + d) % 1.0)
        worst = min(worst, R * z - t)
    return worst


X = 1.0 - 1e-9   # the huge letter (the maximum): every shift of it must be taken from this same point


def pts_for(k, h, p1, p2, eq):
    pts = [X, (X - k * h) % 1.0]
    for i in range(k):
        pts += [(p1 - i * h) % 1.0, (p2 - i * h) % 1.0]
    if not eq:
        pts += [(X - i * h) % 1.0 for i in range(1, k)]
    return pts


def grid(step_h, step_p, hlo=0.0, hhi=1.0):
    h = hlo + step_h
    while h < hhi:
        p1 = step_p
        while p1 < 1:
            p2 = step_p
            while p2 < 1:
                if abs(p1 - p2) > 1e-9:
                    yield h, p1, p2
                p2 += step_p
            p1 += step_p
        h += step_h


def scan(eq, kfeas, step_h, step_p, hlo=0.0, hhi=1.0):
    """Points feasible for rotations h..kfeas*h; report their count, h-range, best margin at the next rotation."""
    count, hmin, hmax, best = 0, None, None, None
    for h, p1, p2 in grid(step_h, step_p, hlo, hhi):
        if all(margin(pts_for(k, h, p1, p2, eq), (k * h) % 1.0) >= 0 for k in range(1, kfeas + 1)):
            count += 1
            hmin = h if hmin is None else min(hmin, h)
            hmax = h if hmax is None else max(hmax, h)
            nxt = margin(pts_for(kfeas + 1, h, p1, p2, eq), ((kfeas + 1) * h) % 1.0)
            if best is None or nxt > best[0]:
                best = (round(nxt, 4), round(h, 4), round(p1, 4), round(p2, 4))
    return {"feasible_points": count, "h_range": [hmin and round(hmin, 4), hmax and round(hmax, 4)],
            "best_next_rotation_margin": best}


def main():
    fine = "--fine" in sys.argv
    out = {"model": "single drop, aligned pair, arcs longer than k, slope log2(3/2), ell/m -> 0"}
    out["v2==v4: h-feasible, best 2h margin"] = scan(True, 1, 0.0025, 0.005)
    out["v2!=v4: h-feasible, best 2h margin"] = scan(False, 1, 0.0025, 0.005)
    out["v2!=v4: (h,2h)-feasible, best 3h margin"] = scan(False, 2, 0.002, 0.005)
    if fine:
        out["fine v2!=v4: (h,2h)-feasible in [0.30,0.42], best 3h margin"] = scan(False, 2, 0.001, 0.0025, 0.30, 0.42)
    for k, v in out.items():
        print(k, ":", v)
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1))
    ok = (out["v2==v4: h-feasible, best 2h margin"]["best_next_rotation_margin"][0] < 0 and
          out["v2!=v4: (h,2h)-feasible, best 3h margin"]["best_next_rotation_margin"][0] < 0)
    print("model: rotations h, 2h, 3h exclude every configuration on the grid:", ok)
    return 0


if __name__ == "__main__":
    sys.exit(main())
