"""Recompute the finite saturation tables of saturation_audit.json from first principles.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this
folder load ../bridge_normal_form/normal_form.py and
../complementary_bridge/run_bridge.py by their pre-migration paths and no
longer run.

This script uses its own odd-only Syracuse step S (absorbing at 1), its own
elementary normal form nu (strip x -> (x-1)/4 while x = 5 mod 8, then apply
at most one selected halving x -> (x-1)/2) and its own quotient
T(q) = nu(S(q)). For the nine supplied cutoffs N = 8, 16, 24, 32, 64, 96,
168, 384, 768 (input paths followed with a 1000-step cap, as in the legacy
audit) it checks against the legacy receipt saturation_audit.json:

1. the saturated quotient Q_N = nu(Y_N), with its size, maximum, hash, and the
   hash of the least-origin witnesses (origin, step, state);
2. that Q_N is T-closed, that every T arrow does not increase the least
   origin, and that the nested smaller-cutoff tables equal the smaller Q_n;
3. the finite ordinary core W_Q = {S(q), 3q+2}: |W_Q| = 2|Q|, S(W_Q) in W_Q,
   max W_Q = 3 max Q + 2, its size, the number of core states not on the
   supplied paths, and the largest depth to 1;
4. the R26 extension masses: the complementary remainder of R_N, the mass
   with normalized return nu(f(x)) <= N, and the mass with nu(f(x)) in Q_N,
   together with the extra roots, their weights, targets and witnesses;
5. the 20 high-band counts #{odd x in [X, 2X): nu(x) in Q_N} for
   X = max(Q_N) times 1, 2, 17, 2^64, 2^512 at N = 8, 96, 384, 768, counted
   by walking each F-ray directly (count and state hash);
6. the stored weight-2 current at root 415 (root415_current.json): its
   divergence is exactly 2 delta_415, its rows form the actual path, the
   R26 return of 415 is 1579, and S^4(327) = 415, S^9(327) = 1579.

It does not rebuild the 224 member currents, the signed sparse bands or the
oscillation families (legacy checker, evidence only). No file is written.
Exits 1 on any mismatch.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
CUTOFFS = (8, 16, 24, 32, 64, 96, 168, 384, 768)
FAILURES = []


def check(condition, message):
    if not condition:
        FAILURES.append(message)


def v2(n):
    return (n & -n).bit_length() - 1


def step(x):
    n = 3 * x + 1
    return n >> v2(n)


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    t = (x + 1) >> a
    return t % 4 == (3 if a % 2 else 1)


def nu(x):
    while x % 8 == 5:
        x = (x - 1) // 4
    if selected(x):
        x = (x - 1) // 2
    return x


def canonical(x):
    return nu(x) == x


def T(q):
    return nu(step(q))


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def path_to_one(seed, cap=1000):
    path, x = [seed], seed
    while x != 1:
        x = step(x)
        path.append(x)
        if len(path) > cap:
            raise RuntimeError(f"input path cap exceeded at seed {seed}")
    return path


def depths_to_one(edges):
    depth = {1: 0}
    for start in sorted(edges):
        path, x = [], start
        while x not in depth:
            if x in path or x not in edges:
                return None
            path.append(x)
            x = edges[x]
        d = depth[x]
        for y in reversed(path):
            d += 1
            depth[y] = d
    return depth


def residual_profile(N):
    """R_N of retained-graph-complement-constructor (8 | N), with weights."""
    profile = {}
    for x in range(N + 1, (3 * N + 1) // 2, 2):
        if 2 * x >= 3 * N:
            continue
        w = 0
        if x % 12 == 3:
            w += 1
        if x % 12 == 7 and 8 * x > 9 * N:
            w += 1
        if x % 36 in (7, 19) and 8 * x < 9 * N:
            w += 2
        if w:
            profile[x] = w
    return profile


def run_return(x):
    """R26 return f(x) for a complementary root x = 2^a t - 1."""
    a = v2(x + 1)
    t = (x + 1) >> a
    m = 3**(a - 1) * t - 1
    d = v2(m)
    w = m >> d
    return 3**((d - 1) // 2) * w if d % 2 else 2 * 3**(d // 2) * w + 1


def band_states(Q, X):
    states = {}
    for q in Q:
        for base in (q, 2 * q + 1):
            x = base
            while x < X:
                x = 4 * x + 1
            if x < 2 * X:
                if x in states:
                    FAILURES.append(f"band state {x} counted twice")
                states[x] = 1
    return states


def main():
    receipt = json.loads((HERE / "saturation_audit.json").read_text())
    stored = json.loads((HERE / "root415_current.json").read_text())
    by_N = {r["N"]: r for r in receipt["cutoffs"]}
    ext_by_N = {r["N"]: r for r in receipt["normalized_run_extensions"]}
    quotients = {}

    for N in CUTOFFS:
        raw, witnesses = {1}, {}
        for seed in range(1, N + 1, 2):
            path = path_to_one(seed)
            raw.update(path)
            if not canonical(seed):
                continue
            for k, y in enumerate(path):
                q = nu(y)
                if q not in witnesses or (seed, k) < (witnesses[q]["origin"], witnesses[q]["step"]):
                    witnesses[q] = dict(origin=seed, step=k, state=y)
        Q = sorted(witnesses)
        check(set(Q) == {nu(y) for y in raw}, f"N={N}: Q_N differs from nu(Y_N)")
        quotients[N] = (Q, witnesses, raw)
        for q in Q:
            check(T(q) in witnesses, f"N={N}: Q_N not T-closed at {q}")
            if T(q) in witnesses:
                check(witnesses[T(q)]["origin"] <= witnesses[q]["origin"], f"N={N}: origin increases at {q}")
        check(depths_to_one({q: (1 if q == 1 else T(q)) for q in Q}) is not None, f"N={N}: quotient does not reach 1")
        W = {step(q) for q in Q} | {3 * q + 2 for q in Q}
        edges = {w: step(w) for w in W}
        check(len(W) == 2 * len(Q), f"N={N}: |W_Q| != 2|Q|")
        check(set(edges.values()) <= W, f"N={N}: W_Q not closed")
        check(max(W) == 3 * max(Q) + 2, f"N={N}: max W_Q")
        depth = depths_to_one(edges)
        check(depth is not None, f"N={N}: core does not absorb")
        mine = dict(N=N, canonical_inputs=sum(1 for x in range(1, N + 1, 2) if canonical(x)),
                    base_count=len(Q), maximum_base=max(Q), raw_known_states=len(raw),
                    core_vertices=len(W), core_new_states=len(W - raw),
                    maximum_core_depth=max(depth.values()) if depth else None,
                    bases_sha256=digest(Q), origins_sha256=digest(witnesses))
        check(mine == by_N.get(N), f"N={N}: cutoff record differs from receipt")

        remainder = {x: c for x, c in residual_profile(N).items() if not selected(x)}
        old = {x: c for x, c in remainder.items() if nu(run_return(x)) <= N}
        new = {x: c for x, c in remainder.items() if nu(run_return(x)) in witnesses}
        check(old.keys() <= new.keys(), f"N={N}: saturated rule loses a root")
        ext = ext_by_N.get(N, {})
        check((sum(remainder.values()), sum(old.values()), sum(new.values())) ==
              (ext.get("preceding_mass"), ext.get("original_removed"), ext.get("saturated_removed")),
              f"N={N}: extension masses differ from receipt")
        extra = [(x, c, nu(run_return(x)), witnesses[nu(run_return(x))]) for x, c in new.items() if x not in old]
        recorded = [(e["root"], e["weight"], e["target"], e["origin"]) for e in ext.get("extra", [])]
        check(sorted(extra, key=lambda e: e[0]) == sorted(recorded, key=lambda e: e[0]),
              f"N={N}: extra roots differ from receipt")

    for N in CUTOFFS:
        _, witnesses, _ = quotients[N]
        for n in CUTOFFS:
            if n <= N:
                nested = sorted(q for q, w in witnesses.items() if w["origin"] <= n)
                check(nested == quotients[n][0], f"nested table {n} inside {N}")

    bands = []
    for N in (8, 96, 384, 768):
        Q = quotients[N][0]
        for multiplier in (1, 2, 17, 2**64, 2**512):
            states = band_states(Q, max(Q) * multiplier)
            bands.append((N, multiplier.bit_length(), len(states), digest(states)))
    recorded = [(b["N"], b["multiplier_bits"], b["count"], b["states_sha256"]) for b in receipt["high_bands"]]
    check(bands == recorded, "high-band counts differ from receipt")

    current = {x: c for x, c in stored["current"]}
    divergence = Counter()
    for x, c in current.items():
        divergence[x] += c
        if step(x) != 1:
            divergence[step(x)] -= c
    check({x: c for x, c in divergence.items() if c} == {415: 2}, "root415 current divergence")
    check(len(current) == stored["current_rows"] == 48 and set(current.values()) == {2}, "root415 rows")
    check(run_return(415) == 1579 and nu(1579) == 1579, "R26 return of 415")
    y = 327
    orbit = [y]
    for _ in range(9):
        y = step(y)
        orbit.append(y)
    check(orbit[4] == 415 and orbit[9] == 1579, "S^4(327) = 415, S^9(327) = 1579")
    check(stored["origin"] == quotients[384][1][1579] and stored["root_origin"] == quotients[384][1][nu(415)],
          "root415 witnesses")
    check(digest(current) == stored["current_sha256"], "root415 current hash")

    if FAILURES:
        print("FAIL: " + "; ".join(FAILURES[:10]))
        sys.exit(1)
    print("PASS: 9 supplied cutoffs (Q_N, origins, core W_Q, R26 extension masses), "
          "nested tables, 20 high bands, weight-2 current at root 415 agree with the legacy receipts")


if __name__ == "__main__":
    main()
