"""S10 reach: single-chain s-mismatch models (s = 4, 5, 6) with a singleton V, random search against rotations up to 12h (~4 min)."""
# s-mismatch single-chain model with a singleton V at X = 1-: inner arc ends P_1..P_{s-2} free.
# Rotation k h mismatches: X, X - k h, P_i - l h (l < k), plus X - l h (1 <= l < k) when v_s != v_2.
import math, random, sys
SIG = math.log2(1.5); R = SIG / math.log2(3); X = 1.0 - 1e-9
def margin(points, d):
    pts = sorted(set(round(p % 1.0, 12) for p in points)); worst = 1e9
    for k, e in enumerate(pts):
        t = (e - pts[k - 1]) % 1.0 if len(pts) > 1 else 1.0
        z = max(e, (e + d) % 1.0); worst = min(worst, R * z - t)
    return worst
def pts_for(k, h, P, eq):
    pts = [X, (X - k * h) % 1.0] + [(p - l * h) % 1.0 for p in P for l in range(k)]
    if not eq: pts += [(X - l * h) % 1.0 for l in range(1, k)]
    return pts
def score(h, P, eq, K):
    return min(margin(pts_for(k, h, P, eq), (k * h) % 1.0) for k in range(1, K + 1))
def search(s, eq, K, restarts=60, iters=2500, seed=5):
    rnd = random.Random(seed); best = None
    for _ in range(restarts):
        h = rnd.random(); P = [rnd.random() for _ in range(s - 2)]
        sc = score(h, P, eq, K); step = 0.08
        for it in range(iters):
            h2 = (h + rnd.gauss(0, step)) % 1; P2 = [(p + rnd.gauss(0, step)) % 1 for p in P]
            s2 = score(h2, P2, eq, K)
            if s2 > sc: h, P, sc = h2, P2, s2
            if it % 400 == 399: step *= 0.6
        if best is None or sc > best[0]: best = (round(sc, 4), round(h, 4), [round(p, 3) for p in sorted(P)])
    return best
for s in (4, 5, 6):
    for eq in (True, False):
        for K in (1, 4, 12):
            print("s =", s, "v_s==v_2" if eq else "v_s!=v_2", "K =", K, search(s, eq, K))
            sys.stdout.flush()
