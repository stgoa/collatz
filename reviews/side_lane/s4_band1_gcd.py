"""S4: law hunt for g = gcd(C, D) on ordered band-1 cycles in the Collatz range (m < A < 2m).

Construction. Fix m and A = m + s with gcd(s, m) = 1. Ranks rotate by s; the normalised exponent at rank r
is c = 1 + [r >= m - s]. Letter positivity (a = c + h_i - h_(i+1) >= 1) forces the height-1 rank set S1 to be
a union of initial segments of the chains {sigma, sigma + s, sigma + 2s, ...} (sigma in [1, s)); rank 0 has
height 0. For every such profile with S1 non-empty: chronological heights h_i = [i s mod m in S1], letters
a_i = c_i + h_i - h_(i+1); keep the profile only if the rational cycle of a REALISES it (index 0 is the
minimum, actual heights = h, the normalised states rotate ranks by s and images keep order).
Record g = gcd(C, D), den = D/g, and for g > 1 the shortest relation: the least max(|u|, v) over
(u, v) != (0, 0), v >= 0, with 2^u = 3^v mod g.
"""
import itertools
import json
import math
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from jterm_gap_check import CD, rot  # noqa: E402


def realise(m, A, S1):
    s = A - m
    rank = [(i * s) % m for i in range(m)]
    h = [1 if r in S1 else 0 for r in rank]
    c = [1 + (1 if r >= m - s else 0) for r in rank]
    a = [c[i] + h[i] - h[(i + 1) % m] for i in range(m)]
    if min(a) < 1:
        return None
    C, D = CD(a)
    Cs = [CD(rot(a, i))[0] for i in range(m)]
    L = Cs[0]
    if min(Cs) != L:
        return None
    hh = []
    for x in Cs:
        k = 0
        while x >= 2**(k + 1) * L:
            k += 1
        hh.append(k)
    if hh != h:
        return None
    Z = [2**(1 - t) * x for t, x in zip(hh, Cs)]
    order = sorted(range(m), key=lambda i: Z[i])
    if [order.index(i) for i in range(m)] != rank:
        return None
    F = [3 * Z[i] + 2**(1 - hh[i]) * D for i in range(m)]
    if any(F[order[r + 1]] <= F[order[r]] for r in range(m - 1)):
        return None
    return a, C, D


def shortest_relation(g):
    best = None
    for v in range(0, 60):
        t = pow(3, v, g)
        for u in range(-60, 61):
            if (u, v) == (0, 0):
                continue
            lhs = pow(2, u, g) if u >= 0 else pow(pow(2, -u, g), -1, g)
            if lhs == t:
                key = max(abs(u), v)
                if best is None or key < best[0]:
                    best = (key, u, v)
        if best is not None and best[0] <= v:
            break
    return best


def profiles(m, s):
    chains = []
    for sigma in range(1, s):
        ch = list(range(sigma, m, s))
        chains.append(ch)
    for lens in itertools.product(*[range(len(ch) + 1) for ch in chains]):
        S1 = set()
        for ch, l in zip(chains, lens):
            S1.update(ch[:l])
        if S1:
            yield S1


def main():
    rng = random.Random(4)
    exhaustive_max_m, sample_max_m, samples_per = 18, 34, 3000
    gcount = Counter()
    rels = Counter()
    rows = []
    n_real = n_prof = 0
    max_ratio = 0.0
    for m in range(3, sample_max_m + 1):
        for A in range(m + 1, 2 * m):
            s = A - m
            if math.gcd(s, m) != 1 or 2**A <= 3**m:
                continue
            if m <= exhaustive_max_m:
                it = profiles(m, s)
            else:
                chains = [list(range(sig, m, s)) for sig in range(1, s)]
                def gen():
                    for _ in range(samples_per):
                        S1 = set()
                        for ch in chains:
                            S1.update(ch[:rng.randint(0, len(ch))])
                        if S1:
                            yield S1
                it = gen()
            for S1 in it:
                n_prof += 1
                r = realise(m, A, S1)
                if r is None:
                    continue
                a, C, D = r
                n_real += 1
                g = math.gcd(C, D)
                gcount[g] += 1
                if g > 1:
                    rel = shortest_relation(g)
                    rels[(g, rel[1], rel[2])] += 1
                    max_ratio = max(max_ratio, math.log(g) / math.log(D))
                    if len(rows) < 25:
                        rows.append((m, A, sorted(S1), g, D // g))
    out = {"probe": "s4_band1_gcd", "exhaustive_m_le": exhaustive_max_m, "sampled_m_le": sample_max_m,
           "profiles_tried": n_prof, "realised_band1_ordered": n_real,
           "g_distribution": {str(k): v for k, v in sorted(gcount.items())},
           "shortest_relation_(g,u,v)_with_2^u=3^v_mod_g": {f"{k}": v for k, v in sorted(rels.items())},
           "max_log_g_over_log_D": round(max_ratio, 4), "examples_g_gt_1_(m,A,S1,g,den)": rows}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
