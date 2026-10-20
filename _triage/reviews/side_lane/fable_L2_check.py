"""Sidekick probe: independent check of L2/L3 on branch claude/explicit-tao (commit 88d2424,
experiments/explicit_tao/lemmas/L2_valuation_tail.md), with this branch's own code.

(1) The rate I(theta) = theta*log(2(theta-1)/theta) - log(theta-1) equals -min_{u>1}[theta log u - log(2u-1)]
    (checked by direct numerical minimisation) and the stated values I(1.5..1.9) are compared to it.
(2) Chernoff: P(A_n <= t) <= exp(-n I(t/n)) against the exact law P(A_n = A) = C(A-1,n-1)/2^A, n <= 60.
(3) Word count: #{words of length n with A <= t} = C(floor t, n) (hockey stick), n <= 30.
(4) L1 + L2' on actual integers: for X = 2^20, n in {6,8,10}, theta in {1.6,1.7,1.8}, d in {1,5}:
    #{odd N <= X : A_n(N) <= theta n} <= (X/2) exp(-n I(theta)) + C(floor(theta n), n).
(5) L3: S_d^n(N) = (3^n N + d C_w)/2^A with 0 < C_w/2^A <= (3/2)^n - 1; outside A <= theta n,
    S_d^n(N) < N(3/2^theta)^n + d(3/2)^n  (random odd N < 2^64, n <= 40, d in {1,5}).
Standard library. Run without -O.
"""
from fractions import Fraction as F
from math import comb, exp, log
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def I(theta):
    return theta*log(2*(theta - 1)/theta) - log(theta - 1)


def I_numeric(theta):
    best = float("inf")
    lo, hi = 1.0000001, 50.0
    for _ in range(200):          # golden-section on the convex function g(u) = theta log u - log(2u-1)
        m1 = lo + (hi - lo)*0.381966
        m2 = lo + (hi - lo)*0.618034
        g1 = theta*log(m1) - log(2*m1 - 1)
        g2 = theta*log(m2) - log(2*m2 - 1)
        if g1 < g2:
            hi = m2
        else:
            lo = m1
        best = min(best, g1, g2)
    return -best


def v2(n):
    return (n & -n).bit_length() - 1


def step(d, x):
    y = 3*x + d
    e = v2(y)
    return y >> e, e


def main():
    out = {}
    claimed = {1.5: 0.08530, 1.6: 0.05054, 1.7: 0.02663, 1.8: 0.01112, 1.9: 0.00263}
    vals = {}
    for th, c in claimed.items():
        a, b = I(th), I_numeric(th)
        assert abs(a - b) < 1e-9
        vals[str(th)] = {"I": round(a, 6), "claimed": c, "abs_diff": round(abs(a - c), 6)}
    out["rate_values"] = vals
    # (2) Chernoff vs exact law
    worst = 0.0
    for n in range(1, 61):
        for th in (1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.95):
            t = th*n
            p = sum(F(comb(A - 1, n - 1), 2**A) for A in range(n, int(t) + 1))
            bound = exp(-n*I(th))
            assert float(p) <= bound*(1 + 1e-12)
            if bound > 0:
                worst = max(worst, float(p)/bound)
    out["chernoff_max_ratio"] = round(worst, 6)
    # (3) word count
    for n in range(1, 31):
        for T in range(n, 3*n):
            assert sum(comb(A - 1, n - 1) for A in range(n, T + 1)) == comb(T, n)
    # (4) L2' on actual integers
    X = 2**20
    rows = []
    for d in (1, 5):
        prefix = {6: [], 8: [], 10: []}
        for N in range(1, X + 1, 2):
            x, A = N, 0
            for j in range(1, 11):
                if d == 1 and x == 1:
                    A += 2
                else:
                    x, e = step(d, x)
                    A += e
                if j in prefix:
                    prefix[j].append(A)
        for n in (6, 8, 10):
            for th in (1.6, 1.7, 1.8):
                cnt = sum(1 for A in prefix[n] if A <= th*n)
                bound = (X/2)*exp(-n*I(th)) + comb(int(th*n), n)
                assert cnt <= bound
                rows.append([d, n, th, cnt, round(bound, 1)])
    out["integer_counts"] = rows
    # (5) L3
    rng = random.Random(88)
    for _ in range(4000):
        d = rng.choice((1, 5))
        N = rng.randrange(3, 2**64) | 1
        n = rng.randrange(1, 41)
        x, A, Cw = N, 0, 0
        for j in range(n):
            Cw = 3*Cw + 2**A
            x, e = step(d, x)
            A += e
        assert 2**A * x == 3**n * N + d*Cw
        assert 0 < F(Cw, 2**A) <= F(3, 2)**n - 1
        for th in (1.6, 1.7):
            if A > th*n:
                assert x < N*(3/2**th)**n + d*(1.5)**n
    out["result"] = "PASS"
    (HERE / "fable_L2_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
