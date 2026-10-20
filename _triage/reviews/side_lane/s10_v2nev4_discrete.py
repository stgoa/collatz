"""S10: discrete v2 != v4 words ([V][1^a][3^b][2^c]) at the model optima, checked against rotations up to 12h."""
# Discrete test of the v2 != v4 four-mismatch pattern: arcs along one h-chain from x = m-1:
# [V][1^a][3^b][2^c]  (v2 = 1, v3 = 3, v4 = 2), b and c small so the slope cost is small.
# P2 = x + (a+b)h = x - (c+1)h, P1 = x + a h = x - (b+c+1)h. Pick (b, c) placing P1, P2 near model targets.
import math, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from s8_multirotation_check import envelope, check_rotation
L3 = math.log2(3)
def build(m, h, a, b, c):
    x = m - 1; w = [1] * m
    for k in range(a + 1, a + b + 1): w[(x + k * h) % m] = 3
    for k in range(a + b + 1, m): w[(x + k * h) % m] = 2
    A = math.ceil(m * L3)
    V = A - (sum(w) - w[x])
    w[x] = V
    return w, V
def ones_runs_margin(w, y):
    m = len(w); worst = None; i = 0
    while i < m:
        if w[i] == 1:
            j = i
            while j < m and w[j] == 1: j += 1
            mg = y[j % m] - (1 + (j - i) * L3)
            worst = mg if worst is None else min(worst, mg)
            i = j
        else: i += 1
    return worst
def run(m, ell, hf, p1t, p2t, cmax=4000, bmax=4000, kmax=12):
    h = int(hf * m)
    while math.gcd(h, m) != 1: h += 1
    x = m - 1
    # choose c with P2 = x - (c+1)h closest to p2t, then b with P1 = x - (b+c+1)h closest to p1t
    c = min(range(1, cmax), key=lambda c: abs(((x - (c + 1) * h) % m) / m - p2t))
    b = min(range(1, bmax), key=lambda b: abs(((x - (b + c + 1) * h) % m) / m - p1t))
    a = m - 1 - b - c
    w, V = build(m, h, a, b, c)
    eps = math.log1p(1 / (3 * 2**71)) / math.log(2)
    y = [ell]
    for i in range(m - 1): y.append(y[-1] + L3 - w[i] + eps)
    if min(y) != y[0]: return {"note": "min not at 0"}
    res = {"h/m": round(h/m, 4), "b": b, "c": c, "P1": round(((x - (b+c+1)*h) % m)/m, 3), "P2": round(((x-(c+1)*h) % m)/m, 3), "V": V}
    margins = []
    for k in range(1, kmax + 1):
        for d in ((k * h) % m, (-k * h) % m):
            s, worst = check_rotation(w, y, d)
            margins.append((k if d == (k*h) % m else -k, s, worst[0]))
    res["worst_kh"] = min(margins, key=lambda r: r[2])
    res["mismatch_counts_k1..4"] = [r[1] for r in margins[:8]]
    res["ones"] = round(ones_runs_margin(w, y), 1)
    return res
m = 1_000_003
for ell in (172 + 342 * math.log2(m) - L3, 1000.0, 200.0):
    for (hf, p1t, p2t) in ((0.364, 0.418, 0.138), (0.5762, 0.2148, 0.6593), (0.6344, 0.7841, 0.502)):
        print(round(ell), (hf, p1t, p2t), run(m, ell, hf, p1t, p2t))
