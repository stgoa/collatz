"""S8 robustness: the survivor words checked against the witness inequalities of every rotation by a convergent
denominator (x1, x2, x3) of h^-1/m with at most 60,000 mismatches, not only the four-mismatch rotation by h."""
import math, sys
sys.path.insert(0, 'sidekick/probes')
from s8_four_mismatch_map import build_word, mismatches, LOG2_3, targeted
eps = math.log1p(1 / (3 * 2**71)) / math.log(2)

def envelope(w, ell):
    y = [ell]
    for i in range(len(w) - 1): y.append(y[-1] + LOG2_3 - w[i] + eps)
    return y

def convergent_dens(num, den, k=40):
    a, b = num, den; qs = []; q0, q1 = 0, 1
    while b and len(qs) < k:
        c = a // b; a, b = b, a - c * b
        q0, q1 = q1, c * q1 + q0
        qs.append(q1)
    return qs

def check_rotation(w, y, d):
    m = len(w)
    M = [i for i in range(m) if w[i] != w[(i + d) % m]]
    if not M: return None
    worst = None
    Ms = M
    for k, e in enumerate(Ms):
        prev = Ms[k - 1]
        t = (e - prev - 1) % m
        z = (e + d) % m if y[(e + d) % m] > y[e] else e
        mg = y[z] - (1 + t * LOG2_3)
        if worst is None or mg < worst[0]: worst = (round(mg, 1), t, e, z)
    return len(M), worst

def run(m, ell, alpha, p1w, p2w, bfs, span):
    best = targeted(m, ell, eps, alpha, p1w, p2w, bfs, span=span)
    h, a, b = best["h"], best["a"], best["b"]
    w, V, A = build_word(m, h, a, b)
    y = envelope(w, ell)
    r = pow(h, -1, m)
    qs = convergent_dens(r, m)
    out = []
    for q in qs:
        for mult in (1, 2, 3):
            d = (q * mult) % m
            if d == 0: continue
            res = check_rotation(w, y, d)
            if res and res[0] <= 60000:
                out.append((d, res[0], res[1]))
    out.append(("h", 4, check_rotation(w, y, h)[1]))
    worst = min(out, key=lambda r: r[2][0])
    print(f"m={m} ell={ell:.0f} h/m={h/m:.4f} b={b}: rotations checked={len(out)}; worst={worst}")
    return out

phi = (1 + 5**0.5) / 2
alpha = 1 / (2 + 1 / (3 + 1 / phi))
m = 1_000_003
run(m, 172 + 342 * math.log2(m) - LOG2_3, math.sqrt(2) - 1, (0.64, 0.92), (0.2, 0.243), (1.6, 2, 3), 60)
run(m, 71.0, alpha, (0.65, 0.86), (0.207, 0.241), (1.6, 2.0, 2.5), 25)
run(m, 100.0, alpha, (0.645, 0.87), (0.2, 0.245), (1.6, 2.0, 2.5), 25)
