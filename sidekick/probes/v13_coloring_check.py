"""Sidekick probe: independent check of main's V13 classification (experiments/viewpoints/V002/invariant_colors.md,
main cdfb143): every M-periodic coloring h with h(2n)=h(n) and h(3n+d)=h(n) (odd n>1) factors through
g=gcd(M,d) and is constant exactly on the orbits of multiplication by 2 and 3 in Z/gZ.

Method (own code): for each modulus M and d, build the residue graph on Z/MZ with edges r -- 2r and, for
residues containing odd n, r -- 3r+d; its connected components are exactly the degrees of freedom of
M-periodic invariant colorings. Compare the component count with the number of <x2,x3>-orbits on Z/gZ.
Also: the d=5 and d=61 colorings 1_{d|n} are invariant (n <= 10^5); the commutator A(B(n)) - B(A(n)) = d.
Side remark checked: a nonconstant 2-automatic invariant coloring needs more than 69 states, because a
k-state recognizer of a nonempty class accepts a binary word of length < k, and every n < 2^68 reaches 1
(verification by Barina, cited not re-run); this probe only checks the shortest-word bound on random DFAs.
Standard library. Run without -O.
"""
from math import gcd
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def f(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def u(self, a, b):
        a, b = self.f(a), self.f(b)
        if a != b:
            self.p[a] = b


def residue_components(M, d):
    s = DSU(M)
    for r in range(M):
        s.u(r, (2*r) % M)
        has_odd = (M % 2 == 1) or (r % 2 == 1)
        if has_odd:
            s.u(r, (3*r + d) % M)
    return len({s.f(r) for r in range(M)})


def orbit_count(g):
    s = DSU(g)
    for r in range(g):
        s.u(r, (2*r) % g)
        s.u(r, (3*r) % g)
    return len({s.f(r) for r in range(g)})


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    rows = 0
    mism = []
    for d in (1, 5, 7, 11, 13, 61):
        for M in range(1, 401):
            c = residue_components(M, d)
            o = orbit_count(gcd(M, d))
            if c != o:
                mism.append((d, M, c, o))
            rows += 1
            if d == 1:
                assert c == 1
    assert not mism, mism[:10]
    for d in (5, 61):
        for n in range(1, 10**5):
            h = lambda x: x % d == 0
            assert h(2*n) == h(n)
            if n % 2 == 1 and n > 1:
                assert h(3*n + d) == h(n)
    for d in (1, 5, 7, 61):
        for n in range(1, 1000):
            assert 2*(3*n + d) - (3*(2*n) + d) == d
    # shortest accepted word of a k-state DFA over {0,1} has length <= k-1 (sanity check on random DFAs)
    rng = random.Random(13)
    for _ in range(2000):
        k = rng.randrange(1, 12)
        delta = [[rng.randrange(k) for _ in range(2)] for _ in range(k)]
        acc = {q for q in range(k) if rng.random() < 0.2}
        if not acc:
            continue
        # BFS for shortest accepted word from state 0
        dist = {0: 0}
        frontier = [0]
        while frontier:
            nxt = []
            for q in frontier:
                for b in (0, 1):
                    t = delta[q][b]
                    if t not in dist:
                        dist[t] = dist[q] + 1
                        nxt.append(t)
            frontier = nxt
        reach = [dist[q] for q in acc if q in dist]
        if reach:
            assert min(reach) <= k - 1
    out = {"probe": "v13_coloring_check", "main": "cdfb143", "moduli_checked": rows,
           "orbit_classification_mismatches": len(mism),
           "examples": {f"d={d},M={M}": [residue_components(M, d), orbit_count(gcd(M, d))]
                        for d, M in ((1, 360), (5, 60), (61, 122), (7, 84), (13, 156))},
           "result": "PASS"}
    (HERE / "v13_coloring_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
