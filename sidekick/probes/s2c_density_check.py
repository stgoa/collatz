"""Independent check of Lean S2-c (claude/lean-lane 7602fe7): orbit exponent density.

For m, s with gcd(s, m) = 1, 1 <= s < m, q' >= 1, A = m q' + s, rank exponents e_r = q' + [r >= m - s],
orbit r_k = (r0 + k s) mod m, E(r0, t) = sum_(k<t) e(r_k):
  E(r0, t) + floor(r0/m) = t q' + floor((r0 + t s)/m)   (exact, E_eq_div)
  floor(t A / m) <= E(r0, t) for r0 < m                  (E_ge_mul_div)
"""
import json
import math
import random
import sys


def main():
    rng = random.Random(62)
    n = 0
    for _ in range(4000):
        m = rng.randint(2, 60)
        s = rng.randint(1, m - 1)
        if math.gcd(s, m) != 1:
            continue
        qp = rng.randint(1, 3)
        A = m * qp + s
        e = [qp + (1 if r >= m - s else 0) for r in range(m)]
        for r0 in range(m):
            E = 0
            for t in range(0, 3 * m):
                assert E + r0 // m == t * qp + (r0 + t * s) // m
                assert t * A // m <= E
                E += e[(r0 + t * s) % m]
                n += 1
    out = {"probe": "s2c_density_check", "lean": "claude/lean-lane 7602fe7", "cases": n, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
