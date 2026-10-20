"""S12 corollary: a denominator law for ANY mismatch count, from Denjoy-Koksma instead of the height ceiling.

For a primitive word w with a rotation h, gcd(h, m) = 1, having s mismatches:
    log2 den(w) > 1 + ceil((m-s)/s) log2 3 - (V_h + 2 delta) K(h/m) - lambda(w),
with V_h = sum over mismatches of |a_e - a_(e+h)|, delta = A - m log2 3, K = sum of partial quotients of h/m,
lambda(w) = log2(m 2^A / (3D)). (Longest run t >= ceil((m-s)/s); witness 2*3^t < H = L 2^B; S12's B <= Var K;
L <= m q 2^A/(3D).) Checked on (i) every primitive word over {1,2,3} up to length 12 and every coprime rotation,
(ii) actual 3x+q cycles (odd q < 2000), (iii) random near-critical 'low-variation' chain words up to m = 3200.
"""
import json
import math
import random
import sys
from itertools import product
from math import gcd
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402

L3 = math.log2(3)


def C_of(w):
    c = 0
    for k, a in enumerate(reversed(w)):
        c = 3**k + 2**a * c
    return c


def cf_sum(h, m):
    s, num, den = 0, h, m
    while num:
        a, r = divmod(den, num)
        s += a
        den, num = num, r
    return s


def log2_big(x):
    b = x.bit_length()
    return b - 53 + math.log2(x >> (b - 53)) if b > 60 else math.log2(x)


def check_word(w, stats, tag, hs=None):
    m, A = len(w), sum(w)
    D = 2**A - 3**m
    if D <= 0:
        return
    if any(w == w[p:] + w[:p] for p in range(1, m) if m % p == 0):
        return
    C = C_of(w)
    den = D // gcd(C, D)
    lq = log2_big(den) if den > 1 else 0.0
    delta = A - m * L3
    lam = math.log2(m / 3) + A - log2_big(D)
    for h in (hs if hs is not None else range(1, m)):
        if gcd(h, m) != 1:
            continue
        M = [e for e in range(m) if w[e] != w[(e + h) % m]]
        s = len(M)
        if s == 0:
            continue
        Vh = sum(abs(w[e] - w[(e + h) % m]) for e in M)
        bound = 1 + (-(-(m - s) // s)) * L3 - (Vh + 2 * delta) * cf_sum(h, m) - lam
        stats[tag + "_pairs"] = stats.get(tag + "_pairs", 0) + 1
        if bound > 0:
            stats[tag + "_nonvacuous"] = stats.get(tag + "_nonvacuous", 0) + 1
            key = tag + "_nonvacuous_min_slack"
            if key not in stats or lq - bound < stats[key][0]:
                stats[key] = (round(lq - bound, 2), m, s, round(bound, 1))
        if not lq > bound:
            stats.setdefault("violations", []).append((tag, m, h, s, round(lq, 2), round(bound, 2)))


def chain_word(m, h, arcs):
    w, k = [0] * m, 0
    for v, L in arcs:
        for _ in range(L):
            w[(k * h) % m] = v
            k += 1
    return w


def main():
    stats = {}
    for m in range(3, 13):
        for w in product((1, 2, 3), repeat=m):
            w = list(w)
            if w == min(w[i:] + w[:i] for i in range(m)):
                check_word(w, stats, "exhaustive")
    for q in range(1, 2000, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, 1001):
            if len(cyc) >= 3:
                check_word([step(x, q)[1] for x in cyc], stats, "actual")
    random.seed(12)
    for m in (200, 400, 800, 1600, 3200):
        A0 = math.ceil(m * L3)
        for _ in range(8):
            h = random.randrange(1, m)
            while gcd(h, m) != 1:
                h = random.randrange(1, m)
            # s arcs alternating between 1 and 2 with the total pinned to A0 (low variation: all jumps are 1)
            s = random.choice((4, 6, 8, 10))
            n2 = A0 - m
            cuts2 = sorted(random.sample(range(1, n2), s // 2 - 1)) if s > 2 else []
            twos = [b - a for a, b in zip([0] + cuts2, cuts2 + [n2])]
            n1 = m - n2
            cuts1 = sorted(random.sample(range(1, n1), s // 2 - 1)) if s > 2 else []
            ones = [b - a for a, b in zip([0] + cuts1, cuts1 + [n1])]
            arcs = [x for pair in zip([(1, o) for o in ones], [(2, t) for t in twos]) for x in pair]
            check_word(chain_word(m, h, arcs), stats, "lowvar", hs=[h])
    out = dict(stats)
    out["violations"] = stats.get("violations", [])
    for k, v in out.items():
        print(k, v if k != "violations" else len(v))
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1, default=str))
    return 0 if not out["violations"] else 1


if __name__ == "__main__":
    sys.exit(main())
