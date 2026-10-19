"""Sidekick probe: independent check of main's delayed-release construction
(experiments/residual_progress/release/DELAYED_RELEASE.md, commit 65093c4).

Rebuilt from the statement only, with this lane's own A_N:
  1. for h = 2..12, both V in {47, 155}, and three members of each progression:
     the parameters (1)-(6), the six coefficients, the exact arrows u -> t -> v,
     the valuation word (1^r, 2^h, 3) from v to y_1, and the identity
     (I-P)J = mu with J <= 0 and at most 2h+5 rows;
  2. the same identity at the stated ladder cutoff N = 96*64^89 (X = 2^546), by
     point evaluation;
  3. the sharpened isolation lemma by brute force: for v_3(X-1) = h and
     2^max(h+5,10) | X, the depth-(h+1) component of 144N-1 is exactly the
     three-source chain. Cutoffs include N = 96 and N = 6144 on the ladder.
Finite checks only. Standard library. Run without -O.
"""
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1] / "collatz_research_20261017" / "negative_controls"
sys.path[:0] = [str(HERE), str(LANE)]
from affine_controls import step, valuation  # noqa: E402
from progress_measures_audit import increment, point_value  # noqa: E402
from depth_probe import UnionFind, v3  # noqa: E402


def parameters(h):
    r, lam = 0, 4*Fraction(4, 3)**h
    while lam > Fraction(27, 8):
        r, lam = r + 1, lam*Fraction(2, 3)
    return r, lam, Fraction(81, 32) < lam


def family_X(h, V, count=3):
    r, lam, ok = parameters(h)
    assert ok
    m3 = 3**(r + 4)
    U0 = pow(4, -(h + 1), m3)*(3**r*pow(2, -r, m3)*(V + 1) - 2) % m3
    M, b = 3**(h + r + 4), max(h + 5, 10)
    residue = (1 + 3**h*U0) % M
    X0 = (1 << b)*(residue*pow(1 << b, -1, M) % M)
    c = lam + 1 - 2*Fraction(2, 3)**r
    bound = max(Fraction(1024), (c + Fraction(1, 2))/(lam - Fraction(81, 32)))
    period = (1 << b)*M
    while X0 <= bound:
        X0 += period
    return r, [X0 + j*period for j in range(count)]


def certify(X, h, r, coefficient):
    """Check the five-source identity for one X; return the number of current rows."""
    assert v3(X - 1) == h and X % 1024 == 0
    N, U = 3*X//128, (X - 1)//3**h
    num = 2**r*(4**(h + 1)*U + 2)
    assert num % 3**r == 0
    v = num//3**r - 1
    t, u = (2*v - 1)//3, (4*((2*v - 1)//3) - 1)//3
    y1, y2, y3 = 3*X//2 - 1, 9*X//4 - 1, 27*X//8 - 1
    assert y1 < 72*N < t < y2 < u < v < y3
    assert [coefficient(z) for z in (u, t, v, y1, y2, y3)] == [-1, 0, -1, -2, 2, 2]
    assert step(1, u) == t and valuation(1, u) == 2 and step(1, t) == v and valuation(1, t) == 1
    path = [v]
    for a in [1]*r + [2]*h + [3]:
        assert valuation(1, path[-1]) == a
        path.append(step(1, path[-1]))
    assert path[-1] == y1 and len(set(path)) == len(path)
    assert step(1, y1) == y2 and step(1, y2) == y3
    J = defaultdict(int)
    J[u] -= 1; J[t] -= 1; J[y1] -= 4; J[y2] -= 2
    for p in path[:-1]:
        J[p] -= 2
    divergence = defaultdict(int)
    for x, c in J.items():
        divergence[x] += c
        divergence[step(1, x)] -= c
    mu = {u: -1, v: -1, y1: -2, y2: 2, y3: 2}
    assert {x: c for x, c in divergence.items() if c} == mu
    assert all(c <= 0 for c in J.values()) and len(J) <= 2*h + 5
    return len(J)


def isolated_through(X, D):
    """Brute force: is the depth-D component of 144N-1 exactly the chain y_1..y_(D+3)?"""
    N = 3*X//128
    A = increment(1, N)
    chain = [3**k*X//2**k - 1 for k in range(1, D + 4)]
    graph, positions = UnionFind(), list(A)
    for x in positions:
        graph.find(x)
    graph.find(1)
    for _ in range(D):
        positions = [1 if x == 1 else (graph.join(x, step(1, x)) or step(1, x)) for x in positions]
    root = graph.find(chain[2])
    members = {s for s in graph.parent if graph.find(s) == root}
    sources = sorted((s, c) for s, c in A.items() if graph.find(s) == root)
    return members == set(chain) and sources == sorted(zip(chain[:3], (-2, 2, 2))) \
        and graph.find(1) != root


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    qualifying = [h for h in range(2, 65) if parameters(h)[2]]
    assert all(h in qualifying or h + 1 in qualifying for h in range(2, 64))  # no two consecutive misses
    families = 0
    for h in [h for h in qualifying if h <= 12]:
        for V in (47, 155):
            r, Xs = family_X(h, V)
            for X in Xs:
                N = 3*X//128
                coefficient = lambda y, N=N: point_value(1, 64*N, y) - point_value(1, N, y)
                certify(X, h, r, coefficient)
            families += 1
    # stated ladder example: h = r = 2, X = 2^546, N = 96*64^89
    X = 2**546
    N = 3*X//128
    assert N == 96*64**89
    rows = certify(X, 2, 2, lambda y: point_value(1, 64*N, y) - point_value(1, N, y))
    # sharpened isolation lemma, brute force at D = h+1 (and record D = h+2)
    isolation = []
    for X in (4096, 13312, 68608, 234496, 483328, 2**18):
        h = v3(X - 1)
        assert X % (1 << max(h + 5, 10)) == 0
        assert isolated_through(X, h + 1), X
        isolation.append(dict(X=X, N=3*X//128, h=h, chain_exact_at_h_plus_1=True,
                              chain_exact_at_h_plus_2=isolated_through(X, h + 2)))
    report = dict(scope="Independent finite checks of main's delayed-release construction and "
                  "sharpened isolation lemma; the universal statements rest on main's written proof.",
                  qualifying_h_through_64=qualifying, families_checked=families,
                  ladder_example=dict(N="96*64^89", X="2^546", current_rows=rows),
                  isolation_brute_force=isolation, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
