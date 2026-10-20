#!/usr/bin/env python3
"""Exact finite checks for the scoped arbitrary-target transport barrier."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "transport_audit.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def natural(x, name, lower=0):
    need(type(x) is int and x >= lower, f"invalid {name}")


def domain(d, x):
    natural(d, "d", 1)
    natural(x, "odd state", 1)
    need(gcd(d, 6) == 1 and x % 2 == 1, "unsupported d or state")


def raw_step(d, x):
    domain(d, x)
    v = 3 * x + d
    return v // (v & -v)


def valuation(d, x):
    domain(d, x)
    v = 3 * x + d
    return (v & -v).bit_length() - 1


def absorbed_step(d, x):
    domain(d, x)
    return 1 if x == 1 else raw_step(d, x)


def first_passage(d, n, cap=2000):
    domain(d, n)
    need(n > 1, "state 1 is excluded from D and E")
    natural(cap, "search cap")
    x, seen, path = n, {}, []
    for j in range(cap + 1):
        if 2 * x <= n:
            return dict(status="FOUND", endpoint=x, time=j, path=path + [x])
        if x in seen:
            cycle = path[seen[x]:]
            need(all(absorbed_step(d, u) == cycle[(i + 1) % len(cycle)]
                     for i, u in enumerate(cycle)), "invalid repeated cycle")
            need(all(2 * u > n for u in path), "cycle is not a no-half certificate")
            return dict(status="NO_HALF_CYCLE", cycle=cycle, path=path + [x])
        if j == cap:
            return dict(status="UNRESOLVED", reason="search cap", path=path + [x])
        seen[x] = len(path)
        path.append(x)
        x = absorbed_step(d, x)
    raise RuntimeError("unreachable")


def basin(d, n, cap=2000):
    domain(d, n)
    x, seen, path = n, {}, []
    for j in range(cap + 1):
        if x == 1:
            return dict(status="ABSORBED", path=path + [x])
        if x in seen:
            cycle = path[seen[x]:]
            need(all(raw_step(d, u) == cycle[(i + 1) % len(cycle)]
                     for i, u in enumerate(cycle)), "invalid basin cycle")
            return dict(status="NONABSORBING_CYCLE", cycle=cycle, path=path + [x])
        if j == cap:
            return dict(status="UNRESOLVED", reason="search cap", path=path + [x])
        seen[x] = len(path)
        path.append(x)
        x = absorbed_step(d, x)
    raise RuntimeError("unreachable")


def require_resolved(result):
    need(result["status"] != "UNRESOLVED", "unresolved capped search is not a certificate")


def family_counts(d, h, J, t):
    domain(d, h)
    natural(J, "last valuation", 3)
    natural(t, "cutoff multiplier", 1)
    need(h >= max(3, d), "target lower threshold too small")
    need(6 * t >= h, "empty target interval outside counted domain")
    residues, excluded = [], []
    for a in range(3, J + 1):
        residue3 = d * (-1)**a % 3
        r = 1 if residue3 == 1 else 5
        residues.append(r)
        excluded.append((h - 1 + 6 - r) // 6)
    H, C = (h - 1) // 2, sum(excluded)
    return dict(d=d, h=h, J=J, t=t, X=2**(J + 1) * t, Y=6 * t,
                H=H, C=C, residue_classes=residues,
                excluded_per_valuation=excluded, target_count=3 * t - H,
                selected_source_count=(J - 2) * t - C)


def source(d, a, y):
    domain(d, y)
    natural(a, "valuation", 3)
    need((2**a * y - d) % 3 == 0, "invalid inverse congruence")
    n = (2**a * y - d) // 3
    domain(d, n)
    need(n > 1 and y > 1 and 2 * y <= n, "one arrow does not half-descend")
    need(raw_step(d, n) == y and valuation(d, n) == a, "wrong exact inverse arrow")
    return n


def family_checks():
    rows, arrows = [], 0
    for d in (1, 5, 7, 13, 61):
        for h in (max(3, d), max(3, d) + 12):
            t0 = (h + 5) // 6
            for J in (3, 4, 6, 9, 12):
                for t in (t0, t0 + 1, 2 * t0 + 3):
                    row = family_counts(d, h, J, t)
                    targets = list(range(h, 6 * t + 1, 2))
                    need(len(targets) == row["target_count"], "target count mismatch")
                    need(all(2 * y <= row["X"] for y in targets), "target exceeds X/2")
                    witnesses, seen = [], set()
                    for a in range(3, J + 1):
                        chosen = [y for y in targets if (2**a * y - d) % 3 == 0]
                        need(len(chosen) == t - row["excluded_per_valuation"][a - 3],
                             "congruence-class count mismatch")
                        for y in chosen:
                            n = source(d, a, y)
                            need(n <= row["X"] and n not in seen,
                                 "source cutoff or multiplicity error")
                            seen.add(n)
                            result = first_passage(d, n, cap=1)
                            need(result["status"] == "FOUND" and result["time"] == 1
                                 and result["endpoint"] == y, "first-passage clock mismatch")
                            witnesses.append((a, y, n))
                    need(len(witnesses) == row["selected_source_count"], "total source count mismatch")
                    if d == 1 and h == 3:
                        need(row["C"] == J // 2 - 1 and
                             len(witnesses) == (J - 2) * t - J // 2 + 1,
                             "d1 specialization mismatch")
                    arrows += len(witnesses)
                    row["witness_sha256"] = hashlib.sha256(
                        json.dumps(witnesses, separators=(",", ":")).encode()).hexdigest()
                    rows.append(row)
    return dict(cases=len(rows), arrows=arrows, rows=rows)


def linear_gap_checks():
    rows = []
    for m in (0, 1, 2, 5, 10, 100):
        J = 3 * m + 3
        for t in (max(1, 2 * (J // 2 - 1 - m) + 1), 2**20):
            row = family_counts(1, 3, J, t)
            gap = row["selected_source_count"] - m * row["target_count"]
            need(gap == t + m - J // 2 + 1 and gap > 0, "linear gap identity failed")
            ratio = Fraction(gap, row["X"])
            rows.append(dict(m=m, J=J, t=t, X=row["X"], target_count=row["target_count"],
                             selected_source_count=row["selected_source_count"], gap=gap,
                             gap_over_X=[ratio.numerator, ratio.denominator],
                             limiting_gap_over_X=[1, 2**(J + 1)]))
    return rows


def sparse_checks():
    rows = []
    for p, q in ((1, 2), (4, 5), (83, 100)):
        j0 = (4 + q - p - 1) // (q - p)
        for j in (j0, j0 + 1, j0 + 4):
            J, t, X = (q - p) * j - 1, 2**(p * j), 2**(q * j)
            row = family_counts(1, 3, J, t)
            need(row["X"] == X and t**q == X**p, "sparse exponent identity failed")
            expected = ((q - p) * j - 3) * t - J // 2 + 1
            need(row["target_count"] == 3 * t - 1 and
                 row["selected_source_count"] == expected, "sparse count identity failed")
            samples = []
            for a in sorted({3, J, (J + 3) // 2}):
                r = 1 if a % 2 == 0 else 5
                first = 7 if r == 1 else 5
                last = 6 * t - (6 - r)
                for y in sorted({first, last}):
                    n = source(1, a, y)
                    need(n <= X, "sparse witness exceeds cutoff")
                    samples.append(dict(a=a, target=y, source=n))
            rows.append(dict(p=p, q=q, j=j, J=J, X=X, t=t,
                             target_count=row["target_count"], selected_source_count=expected,
                             sampled_exact_arrows=samples))
    return rows


def singleton_checks():
    rows = []
    for d, target, multiplier in ((1, 5, 10), (5, 19, 38)):
        previous = 0
        for j in (1, 2, 3, 8, 32, 128):
            n = (multiplier * 4**j - d) // 3
            need(n > previous and source(d, 2 * j + 1, target) == n,
                 "singleton formula failed")
            result = first_passage(d, n, cap=1)
            need(result["status"] == "FOUND" and result["endpoint"] == target,
                 "singleton first passage failed")
            rows.append(dict(d=d, target=target, j=j, source=n, exact_valuation=2 * j + 1))
            previous = n
    cycle = [19, 31, 49]
    need([raw_step(5, x) for x in cycle] == [31, 49, 19], "d5 control cycle failed")
    need([valuation(5, x) for x in cycle] == [1, 1, 3], "d5 cycle valuations failed")
    return dict(rows=rows, d5_cycle=cycle, d5_cycle_valuations=[1, 1, 3])


def integer_root(value, degree):
    natural(value, "root input")
    natural(degree, "root degree", 1)
    lo, hi = 0, 1 << ((value.bit_length() + degree - 1) // degree)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**degree <= value:
            lo = mid
        else:
            hi = mid
    if hi**degree <= value:
        lo = hi
    need(lo**degree <= value < (lo + 1)**degree, "integer-root bracket failed")
    return lo


def hereditary_checks():
    rows, count_checks, arrows = [], 0, 0
    for p, q in ((1, 2), (4, 5), (83, 100)):
        targets = []
        for j in range(1, 257):
            value = j**q
            floor_root = integer_root(value, p)
            ceil_root = floor_root + int(floor_root**p < value)
            y = 6 * ceil_root + 1
            need(y % 6 == 1 and (not targets or y > targets[-1]),
                 "hereditary target sequence failed")
            targets.append(y)
        for Y in sorted({1, 6, 7, 8, 31, 127, 511,
                         *[y + delta for y in targets[:24] for delta in (-1, 0, 1)]}):
            m = (Y - 1) // 6
            exact = integer_root(m**p, q)
            need(exact == sum(y <= Y for y in targets), "hereditary exact count failed")
            need(exact**q <= Y**p, "hereditary power bound failed")
            count_checks += 1
        for J in (4, 8, 12):
            Y = targets[31]
            X = (2**J * Y + 2) // 3
            threshold = 3 * X // 2**J
            chosen = [y for y in targets if y <= threshold]
            need(len(chosen) == integer_root(((threshold - 1) // 6)**p, q),
                 "hereditary cutoff mismatch")
            witness_set = set()
            for a in range(4, J + 1, 2):
                for y in chosen:
                    n = source(1, a, y)
                    need(n <= X and n not in witness_set, "hereditary source collision or cutoff")
                    witness_set.add(n)
            coefficient = J // 2 - 1
            need(len(witness_set) == coefficient * len(chosen), "hereditary multiplicity failed")
            arrows += len(witness_set)
            rows.append(dict(p=p, q=q, J=J, X=X, target_count=len(chosen),
                             selected_source_count=len(witness_set), multiplicity=coefficient))
    return dict(rows=rows, exact_count_checks=count_checks, sampled_exact_arrows=arrows,
                scope="cardinality-proportional transport; global growth-norm bounds not excluded")


def recurrence_checks():
    rows = []
    for d in (1, 5):
        passage = {n: first_passage(d, n) for n in range(3, 512, 2)}
        basins = {n: basin(d, n) for n in range(1, 512, 2)}
        for result in (*passage.values(), *basins.values()):
            require_resolved(result)
        bad = {n for n, result in basins.items() if result["status"] == "NONABSORBING_CYCLE"}
        exceptional = {n for n, result in passage.items() if result["status"] == "NO_HALF_CYCLE"}
        need(1 not in bad and 1 not in exceptional, "absorber entered exceptional set")
        need(exceptional <= bad, "finite E subset B check failed")
        lengths = []
        for n in sorted(bad):
            x, outer_steps = n, 0
            while passage[x]["status"] == "FOUND":
                y = passage[x]["endpoint"]
                need(y in bad and 2 * y <= x, "bad-set forward invariance failed")
                x, outer_steps = y, outer_steps + 1
            need(x in exceptional and 3 * 2**outer_steps <= n,
                 "outer descent endpoint or clock bound failed")
            lengths.append(outer_steps)
        cuts = []
        for X in (1, 3, 31, 127, 511):
            multiplicity = Counter(result["endpoint"] for n, result in passage.items()
                                   if n <= X and result["status"] == "FOUND")
            lhs = sum(n <= X for n in bad)
            E = sum(n <= X for n in exceptional)
            pulled = sum(value for y, value in multiplicity.items() if y in bad)
            need(lhs == E + pulled, "finite exact B/E recurrence failed")
            cuts.append(dict(X=X, bad=lhs, exceptional=E, pulled_back_bad=pulled))
        rows.append(dict(d=d, odd_seed_cutoff=511, search_cap=2000,
                         nonabsorbing_cycle_seeds=len(bad), complete_no_half_seeds=len(exceptional),
                         max_outer_steps=max(lengths, default=0), cuts=cuts,
                         scope="complete finite cycle/absorption classifications only"))
    return rows


def rejection_checks():
    cases = {
        "absorber excluded from first-passage domain": lambda: first_passage(1, 1),
        "even seed": lambda: first_passage(1, 4),
        "unsupported d": lambda: first_passage(3, 5),
        "boolean d": lambda: first_passage(True, 5),
        "too-small target threshold": lambda: family_counts(61, 3, 6, 2),
        "valuation below catalogue": lambda: family_counts(1, 3, 2, 2),
        "wrong inverse congruence": lambda: source(1, 3, 7),
        "wrong half-descent endpoint": lambda: source(61, 3, 11),
        "empty counted interval": lambda: family_counts(61, 61, 6, 1),
        "capped first-passage search": lambda: require_resolved(first_passage(1, 27, cap=0)),
        "capped basin search": lambda: require_resolved(basin(1, 27, cap=0)),
    }
    for label, action in cases.items():
        try:
            action()
        except ValueError:
            continue
        raise ValueError(f"invalid input accepted: {label}")
    return list(cases)


def audit():
    return dict(schema="phase6-stopping-transport-v1", status="PASS", node="S.2",
                proposed_label="barrier", general_families=family_checks(),
                linear_gap_examples=linear_gap_checks(), sparse_examples=sparse_checks(),
                hereditary_sparse_controls=hereditary_checks(),
                singleton_controls=singleton_checks(), recurrence_controls=recurrence_checks(),
                rejections=rejection_checks(),
                scope=("Arbitrary-target constant cardinality transport with uniform o(X) error "
                       "is impossible. Selected-source counts are lower bounds for full "
                       "first-passage mass. Actual bad-set-only, global growth-norm, weighted and "
                       "scale-dependent estimates remain outside this barrier."))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", type=Path)
    args = parser.parse_args()
    need(not sys.flags.optimize, "run without -O")
    result = audit()
    text = json.dumps(result, indent=2) + "\n"
    if args.write_receipt:
        args.write_receipt.write_text(text)
    else:
        need(result == json.loads(RECEIPT.read_text()), "transport receipt mismatch")
    print(text, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
