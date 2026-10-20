"""Self-contained recomputation of the pair decomposition and the restricted-catalogue scope of pair_scope_audit.json.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder
load ../complementary_bridge/run_bridge.py (and through it the R25 and R23 code)
by their pre-migration paths and no longer run. Standard library, exact
integers. Run from the repository root: python3 <this file>. Exits 1 on any
failure; writes nothing.

Checks, with its own odd-only Syracuse step S, selected/canonical tests and
normal form nu (strip (x-1)/4 while x = 5 mod 8, then halve once if selected):
  - for every complementary x = 3 mod 4 below 32768 (4096 roots): the smaller
    prefix S^(a-1)(q) = w, the run return (3), and that the formal sum (5) of
    tripling pairs T(u) = [3u] - [u] (and one doubling pair D(u) = [2u+1] - [u]
    for even d) telescopes exactly to [f] - [w]; the count equals the receipt's
    comparison_count (the receipt's comparison_hash covers the legacy currents
    and is not recomputed);
  - the 741 integrality-preserving parameter cases (2 <= a <= 20, 2 <= d <= 40):
    the root built from (a, d) has exactly these labels, and the SHA-256 of the
    rows [a, d, w, f] equals the receipt's parameter_hash;
  - the 4096 hypothetical edges 3w -- w (w = 3 mod 8, w < 32768): 3w is
    canonical and nu(w) is (3w-3)/6 or w as in the table of section 3; the
    hash of the rows [w, 3w, nu(w)] equals edge_hash;
  - the bounded quotient: union-find on the 8192 canonical q < 32768 with the
    added edges agrees with the augmented label chi of (6), every q = 7 mod 8 is
    isolated, and the hash of [q, chi(q)] equals finite_quotient_hash;
  - the eight members a = 19, 35, ..., 771 of the counterfamily (7), with
    chi(f) != chi(w), and the seven even-return growth samples, field by field
    against the receipt.
"""

import hashlib
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
failures = []


def require(ok, message):
    if not ok:
        failures.append(message)


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def v2(n):
    return (n & -n).bit_length() - 1


def S(x):
    if x == 1:
        return 1
    y = 3 * x + 1
    return y >> v2(y)


def climber(x):
    a = v2(x + 1)
    return a, (x + 1) >> a


def selected(x):
    a, t = climber(x)
    return x % 4 == 3 and t % 4 == pow(3, a, 4)


def canonical(q):
    return q % 8 == 1 or (q % 4 == 3 and not selected(q))


def nu(x):
    while x % 8 == 5:
        x = (x - 1) // 4
    if selected(x):
        x = (x - 1) // 2
    return x


def chi(x):
    q = nu(x)
    while q % 24 == 9:
        q = (q - 3) // 6 if q % 48 == 9 else q // 3
    return q


def parameters(x):
    a, t = climber(x)
    m = 3 ** (a - 1) * t - 1
    d = v2(m)
    w = m >> d
    k = d // 2
    f = 3 ** k * w if d % 2 else 2 * 3 ** k * w + 1
    return a, t, d, w, f


def add(measure, state, c):
    if state != 1:
        measure[state] = measure.get(state, 0) + c
        if measure[state] == 0:
            del measure[state]


def main():
    receipt = json.loads((HERE / "pair_scope_audit.json").read_text())

    count = 0
    for x in range(3, 32768, 4):
        if selected(x):
            continue
        a, t, d, w, f = parameters(x)
        q = (x - 1) // 2
        y = q
        for _ in range(a - 1):
            y = S(y)
        require(y == w, f"smaller prefix at {x}")
        k = d // 2
        z = x
        for _ in range(a + k - 1):
            z = S(z)
        require(z == (4 * f + 1 if d % 2 else f), f"run return at {x}")
        boundary = {}
        for j in range(k):
            u = 3 ** j * w
            add(boundary, 3 * u, 1)
            add(boundary, u, -1)
        if d % 2 == 0:
            u = 3 ** k * w
            add(boundary, 2 * u + 1, 1)
            add(boundary, u, -1)
        expected = {}
        add(expected, f, 1)
        add(expected, w, -1)
        require(boundary == expected, f"decomposition (5) at {x}")
        count += 1
    require(count == receipt["comparison_count"], "comparison count")

    rows = []
    for a in range(2, 21):
        for d in range(2, 41):
            m = 3 ** (a - 1)
            w = (-pow(2 ** d, -1, m)) % m
            if w % 2 == 0:
                w += m
            t = (2 ** d * w + 1) // m
            aa, tt, dd, ww, f = parameters(2 ** a * t - 1)
            require((aa, dd, ww) == (a, d, w), f"parameter case a={a} d={d}")
            rows.append([a, d, w, f])
    require(len(rows) == receipt["parameter_case_count"] and digest(rows) == receipt["parameter_hash"],
            "parameter cases")

    edges = []
    for w in range(3, 32768, 8):
        q = 3 * w
        lower = (q - 3) // 6 if q % 48 == 9 else q // 3
        require(canonical(q) and nu(w) == lower and chi(q) == chi(w), f"edge at w={w}")
        edges.append([w, q, lower])
    require(len(edges) == receipt["hypothetical_edge_count"] and digest(edges) == receipt["edge_hash"],
            "hypothetical edges")

    vertices = [q for q in range(1, 32768, 2) if canonical(q)]
    parent = {q: q for q in vertices}

    def find(q):
        while parent[q] != q:
            parent[q] = parent[parent[q]]
            q = parent[q]
        return q

    for q in vertices:
        if q % 24 == 9:
            lower = (q - 3) // 6 if q % 48 == 9 else q // 3
            u, v = find(q), find(lower)
            parent[max(u, v)] = min(u, v)
    for q in vertices:
        require(find(q) == chi(q), f"quotient label {q}")
        if q % 8 == 7:
            require(find(q) == q, f"isolated {q}")
    require(len(vertices) == receipt["finite_quotient_vertices"]
            and digest([[q, find(q)] for q in vertices]) == receipt["finite_quotient_hash"], "bounded quotient")

    family = []
    for a in (19, 35, 51, 67, 99, 195, 387, 771):
        x, N = 2 ** a - 1, 12 * 2 ** (a - 4)
        _, _, d, w, f = parameters(x)
        q = (x - 1) // 2
        left = (3 * w - 1) // 2 if w % 16 == 1 else 3 * w
        ok = (d == 3 and w % 24 == 1 and f == 3 * w and chi(3 * w) == left and chi(w) == w and left != w
              and q < N < x and 8 * x > 9 * N and 2 * x < 3 * N and x % 12 == 7 and not selected(x))
        require(ok, f"counterfamily a={a}")
        family.append(dict(a=a, N=N, root=x, lower_seed=q, w=w, target=f, left_minimum=left, right_minimum=w))
    require(family == receipt["infinite_family_samples"], "infinite_family_samples")

    growth = []
    for a in (13, 21, 29, 45, 77, 141, 269):
        x = 2 ** a - 1
        _, _, d, w, f = parameters(x)
        require(d == 4 and f == 18 * w + 1 and 9 * w > x, f"even return a={a}")
        growth.append([a, x, 9 * w])
    require(growth == receipt["even_return_growth_samples"], "even_return_growth_samples")

    if failures:
        print("FAIL: " + "; ".join(failures[:10]))
        sys.exit(1)
    print(f"PASS: decomposition for {count} complementary roots; 741 parameter cases, 4096 edges and the "
          "8192-vertex quotient match the receipt hashes; 8 counterfamily and 7 growth samples")


if __name__ == "__main__":
    main()
