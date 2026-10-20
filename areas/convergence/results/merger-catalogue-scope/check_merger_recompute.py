"""Recompute the finite parts of merger_scope_audit.json from first principles.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this
folder load ../bridge_normal_form/normal_form.py and
experiments/current_construction/recursive/check_annular_recursion.py by
their pre-migration paths and no longer run.

This script uses its own odd-only Syracuse step S (absorbing at 1) and its
own elementary normal form nu (strip x -> (x-1)/4 while x = 5 mod 8, then
apply at most one selected halving x -> (x-1)/2). It checks, against the
legacy receipt merger_scope_audit.json in this folder:

1. the successor bound S(x) in {S(nu(x)), 3 nu(x) + 2} for every odd
   x < 32768 (16384 cases);
2. the incomparable sets at N = 8: F_8 = {1,3,5,7,11,13,17}, 11 in F_8 with
   nu(11) > 8, 21 not in F_8 with nu(21) <= 8;
3. the escape cylinder (1,1,1,1,1,2), x = 191 mod 256: 128 representatives,
   every prefix state canonical, 128 S^6(x) = 729 x + 665, and the hash of
   the prefix rows;
4. the six actual required-ray escape roots (seed, cutoff, word, state
   hash, nu > N at every protected state);
5. the early-cancellation family a = 19, 37, 55, 73, 109, 199: p, q, the
   common successor z < p < q, 3z < 8N, the annular coefficients +1 at p
   and -1 at q, the a - 1 valuation-1 climb of z and its height
   2 3^(a-1) - 1 > 128 q;
6. both sign/climb tables (N = 6144 and 9216), with source and peak counts,
   the peak hash and the early-merger witness pair.

The six-band annular row table used in item 6 (and its two entries used in
item 5) is the published table of disjoint-annular-recursion (R6), copied
here as constants. No file is written. Exits 1 on any mismatch.
"""

from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent

# Six-band annular table of disjoint-annular-recursion (R6): residues mod 18
# and the coefficient rows of bands 0..5, band k = (2^k 9N/4, 2^(k+1) 9N/4).
RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = (
    (1, 0, 1, 0, -2, 0),
    (2, 1, -1, 1, -1, -2),
    (3, -1, -3, 2, 0, -1),
    (1, -3, -2, 3, 1, 0),
    (-1, -2, -1, 1, 2, 1),
    (0, -1, 0, -1, 0, 2),
)

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


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def annular_measure(N):
    lower = 9 * N // 4
    answer = {}
    for band, row in enumerate(ROWS):
        table = dict(zip(RESIDUES, row))
        for x in range(lower * 2**band + 1, lower * 2**(band + 1), 2):
            c = table.get(x % 18, 0)
            if c:
                answer[x] = c
    return answer


def annular_coefficient(N, x):
    lower = 9 * N // 4
    for band, row in enumerate(ROWS):
        if lower * 2**band < x < lower * 2**(band + 1):
            return dict(zip(RESIDUES, row)).get(x % 18, 0)
    return 0


def sign_climb(N, cap=1000):
    measure = annular_measure(N)
    peak = {1: 1}
    longest = 0
    for source in measure:
        x, path, seen = source, [], set()
        while x not in peak:
            if x in seen or len(path) >= cap:
                FAILURES.append(f"sign/climb path cap or cycle at N={N}, source {source}")
                return None
            seen.add(x)
            path.append(x)
            x = step(x)
        longest = max(longest, len(path))
        maximum = peak[x]
        for y in reversed(path):
            maximum = max(maximum, y)
            peak[y] = maximum
    table = {str(h): [sum(c for x, c in measure.items() if c > 0 and peak[x] >= h * x),
                      -sum(c for x, c in measure.items() if c < 0 and peak[x] >= h * x)]
             for h in (1, 4, 16, 64, 128)}
    by_successor = defaultdict(lambda: [[], []])
    for x, c in measure.items():
        if peak[x] >= 64 * x:
            by_successor[step(x)][int(c < 0)].append(x)
    witnesses = []
    for target, (positive, negative) in by_successor.items():
        for p in positive:
            for q in negative:
                if target < min(p, q):
                    witnesses.append(dict(positive=p, positive_capacity=measure[p],
                                          negative=q, negative_capacity=-measure[q],
                                          common_successor=target,
                                          positive_peak=peak[p], negative_peak=peak[q],
                                          current_rows=[[p, 1], [q, -1]]))
    witness = min(witnesses, key=lambda w: (w["common_successor"], w["positive"], w["negative"])) if witnesses else None
    return dict(N=N, source_atoms=len(measure), peak_rows=len(peak),
                longest_new_path=longest, cap_per_new_path=cap,
                positive_negative_mass_by_climb=table,
                source_peaks_sha256=digest([(x, peak[x]) for x in measure]),
                early_merger_of_high_climbers=witness)


def valuation_cylinder(word):
    A, offset, numerator = 0, 0, 1
    for a in word:
        offset = 3 * offset + 2**A
        numerator *= 3
        A += a
    modulus = 2**(A + 1)
    return ((2**A - offset) * pow(numerator, -1, modulus)) % modulus, modulus


def main():
    receipt = json.loads((HERE / "merger_scope_audit.json").read_text())

    # 1. Successor bound.
    cases = 0
    for x in range(1, 32768, 2):
        q = nu(x)
        check(step(x) in (step(q), 3 * q + 2), f"successor bound fails at {x}")
        cases += 1
    check(cases == receipt["normal_form_successor_bound_checks"], "successor-bound case count")

    # 2. Incomparable sets at N = 8.
    known = {1}
    for x in range(1, 9, 2):
        while x not in known:
            known.add(x)
            x = step(x)
    sets = receipt["exact_incomparable_sets"]
    check(sorted(known) == sets["forward_union"], "F_8")
    check(11 in known and nu(11) > 8 and 21 not in known and nu(21) <= 8, "incomparable witnesses")
    check((sets["forward_only"], sets["elementary_only"]) == (11, 21), "receipt witnesses")

    # 3. Escape cylinder.
    rows = []
    for index in range(128):
        x0 = x = 191 + 256 * index
        values = [x]
        for a in (1, 1, 1, 1, 1, 2):
            check(v2(3 * x + 1) == a and canonical(x), f"escape prefix at {x0}")
            x = step(x)
            values.append(x)
        check(128 * x == 729 * x0 + 665, f"escape affine map at {x0}")
        rows.append(values)
    check(digest(rows) == receipt["escape_prefix"]["prefix_rows_sha256"], "escape prefix hash")

    # 4. Actual required-ray escape roots.
    escape_rows = []
    for repeats in (1, 2, 4, 8, 16, 32):
        word = (1, 1, 1, 1, 1, 2) + (1, 2) * repeats + (1,)
        residue, modulus = valuation_cylinder(word)
        x = residue + modulus * ((-residue * pow(modulus, -1, 3)) % 3) + 3 * modulus
        N = max(a * 2**b for a in (12, 14, 16, 18, 21)
                for b in [((x - 1) // a).bit_length() - 1] if b >= 9)
        check(N < x < 3 * N // 2 and x % 12 == 3, f"escape root {repeats} not an R_N root")
        states, y = [x], x
        for a in word:
            check(v2(3 * y + 1) == a, f"escape root {repeats} word")
            y = step(y)
            states.append(y)
        check(all(nu(s) > N for s in states[:-1]), f"escape root {repeats} enters I_N")
        escape_rows.append(dict(repeats=repeats, N=N, seed=x, protected_ordinary_states=len(states) - 1,
                                word=list(word), states_sha256=digest(states)))
    check(escape_rows == receipt["actual_required_ray_escape_examples"], "escape roots differ from receipt")

    # 5. Early-cancellation family.
    family = []
    for a in (19, 37, 55, 73, 109, 199):
        N, z = 12 * 2**(a - 5), 2**a - 1
        p = (4 * z - 1) // 3
        q = 4 * p + 1
        check((4 * z - 1) % 3 == 0 and p % 18 == 1 and q % 18 == 5, f"a={a} residues")
        check(annular_coefficient(N, p) == 1 and annular_coefficient(N, q) == -1, f"a={a} coefficients")
        check(step(p) == step(q) == z < p < q and 3 * z < 8 * N, f"a={a} common successor")
        x = z
        for j in range(a - 1):
            check(x == 3**j * 2**(a - j) - 1 and v2(3 * x + 1) == 1, f"a={a} climb step {j}")
            x = step(x)
        check(x == 2 * 3**(a - 1) - 1 and x > 128 * q, f"a={a} climb height")
        family.append(dict(a=a, N=N, positive=p, negative=q, common_successor=z,
                           proved_later_height=x, current_rows=[[p, 1], [q, -1]]))
    check(family == receipt["universal_early_cancellation_examples"], "early-cancellation rows differ from receipt")

    # 6. Sign/climb tables.
    climbs = [sign_climb(N) for N in (6144, 9216)]
    check(climbs == receipt["independent_sign_climb_checks"], "sign/climb tables differ from receipt")

    if FAILURES:
        print("FAIL: " + "; ".join(FAILURES[:10]))
        sys.exit(1)
    print("PASS: 16384 successor bounds, F_8/I_8 incomparability, 128 escape representatives, "
          "6 required-ray escape roots, early cancellation at a = 19..199, "
          "sign/climb tables at N = 6144, 9216 agree with merger_scope_audit.json")


if __name__ == "__main__":
    main()
