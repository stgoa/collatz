"""S12: the Denjoy-Koksma height bound along a rotation chain, checked on actual 3x+q cycles (odd q < 2000).

For a cycle with log-profile y_p = log2 n_p and a rotation h with gcd(h, m) = 1, put mu(p) = y_(p+h) - y_p.
Then sum_p mu(p) = 0 and y(x + N h) - y(x) = sum_(k<N) mu(x + k h) (a Birkhoff sum of the rotation by h).
(1) Denjoy-Koksma: for every convergent denominator q of h/m (q < m) and every x, |sum_(k<q) mu(x+kh)| <= Var(mu),
    Var = cyclic total variation of mu.
(2) Ostrowski + (1): the log-height B = max y - min y <= Var(mu) * K(h/m), K = sum of partial quotients of h/m.
(3) Var(mu) <= V_h + 2 delta, V_h = sum over mismatches of |a_e - a_(e+h)|, delta = A - m log2 3 (total drift).
Checks (1) on every (cycle, rotation, convergent, start), and (2), (3) on every (cycle, rotation).
"""
import json
import math
import sys
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402


def cf(h, m):
    quots, dens, q0, q1 = [], [], 0, 1
    num, den = h, m
    while num:
        a, r = divmod(den, num)
        quots.append(a)
        q0, q1 = q1, a * q1 + q0
        dens.append(q1)
        den, num = num, r
    return quots, [q for q in dens if q < m]


def main():
    st = {"pairs": 0, "dk_checks": 0, "dk_viol": 0, "height_viol": 0, "var_viol": 0,
          "max_dk_ratio": 0.0, "max_height_ratio": 0.0}
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            m = len(cyc)
            if m < 3:
                continue
            y = [math.log2(x) for x in cyc]
            a = [step(x, q)[1] for x in cyc]
            B = max(y) - min(y)
            delta = sum(a) - m * math.log2(3)
            for h in range(1, m):
                if gcd(h, m) != 1:
                    continue
                mu = [y[(p + h) % m] - y[p] for p in range(m)]
                var = sum(abs(mu[(p + 1) % m] - mu[p]) for p in range(m))
                quots, dens = cf(h, m)
                K = sum(quots)
                Vh = sum(abs(a[e] - a[(e + h) % m]) for e in range(m))
                st["pairs"] += 1
                if var > Vh + 2 * delta + 1e-9:
                    st["var_viol"] += 1
                if B > var * K + 1e-9:
                    st["height_viol"] += 1
                st["max_height_ratio"] = max(st["max_height_ratio"], B / (var * K) if var * K else 0)
                for qd in dens:
                    for x in range(m):
                        S = sum(mu[(x + k * h) % m] for k in range(qd))
                        st["dk_checks"] += 1
                        if abs(S) > var + 1e-9:
                            st["dk_viol"] += 1
                        if var:
                            st["max_dk_ratio"] = max(st["max_dk_ratio"], abs(S) / var)
    st["max_dk_ratio"] = round(st["max_dk_ratio"], 4)
    st["max_height_ratio"] = round(st["max_height_ratio"], 4)
    print(st)
    Path(__file__).with_suffix(".json").write_text(json.dumps(st, indent=1))
    return 0 if st["dk_viol"] == st["height_viol"] == st["var_viol"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
