"""S8 counterexample check: the S8 words against the witness inequalities of the rotations by k*h, k = +-1..+-12."""
import math, sys
sys.path.insert(0, 'sidekick/probes')
from s8_four_mismatch_map import build_word, LOG2_3, targeted
from s8_multirotation_check import envelope, check_rotation
eps = math.log1p(1 / (3 * 2**71)) / math.log(2)
phi = (1 + 5**0.5) / 2
alpha = 1 / (2 + 1 / (3 + 1 / phi))
m = 1_000_003
cases = [(172 + 342 * math.log2(m) - LOG2_3, math.sqrt(2) - 1, (0.64, 0.92), (0.2, 0.243), (1.6, 2, 3), 60),
         (71.0, alpha, (0.65, 0.86), (0.207, 0.241), (1.6, 2.0, 2.5), 25),
         (100.0, alpha, (0.645, 0.87), (0.2, 0.245), (1.6, 2.0, 2.5), 25)]
for ell, hf, p1w, p2w, bfs, span in cases:
    best = targeted(m, ell, eps, hf, p1w, p2w, bfs, span=span)
    h, a, b = best["h"], best["a"], best["b"]
    w, V, A = build_word(m, h, a, b)
    y = envelope(w, ell)
    rows = []
    for k in range(1, 13):
        d = (k * h) % m
        s, worst = check_rotation(w, y, d)
        rows.append((k, s, worst[0]))
        d2 = (-k * h) % m
        s2, worst2 = check_rotation(w, y, d2)
        rows.append((-k, s2, worst2[0]))
    print(f"ell={ell:.0f} h/m={h/m:.4f} b={b}:", [(k, s, mg) for k, s, mg in rows])
    print("   min margin over k*h rotations:", min(r[2] for r in rows))
