"""Exact classification and concentration checks for two maximum arcs.

Coefficient identities check the unbounded algebra in the manuscript.
The collision-endpoint tables are complete only in their stated bounded
multiplicity range; the analytic convexity argument supplies the general
single-arc bound. Rational profile grids test conventions and block-span
identities, not existence or absence of integer Collatz cycles.
"""

from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ZERO = (0, 0, 0)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def constant(value):
    return {ZERO: F(value)} if value else {}


def variable(index):
    powers = list(ZERO)
    powers[index] = 1
    return {tuple(powers): F(1)}


def add(*polynomials):
    result = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            result[powers] = result.get(powers, F(0)) + coefficient
    return {powers: value for powers, value in result.items() if value}


def scale(value, polynomial):
    return {powers: F(value) * coefficient
            for powers, coefficient in polynomial.items()
            if value * coefficient}


def multiply(*polynomials):
    result = constant(1)
    for polynomial in polynomials:
        product = {}
        for first, x in result.items():
            for second, y in polynomial.items():
                powers = tuple(i + j for i, j in zip(first, second))
                product[powers] = product.get(powers, F(0)) + x * y
        result = {powers: value for powers, value in product.items() if value}
    return result


def equal(left, right, message):
    require(not add(left, scale(-1, right)), message)


def polynomial_checks():
    a, c, d = (variable(i) for i in range(3))
    r = add(a, c)
    difference = add(a, scale(-1, c))
    a2, c2 = multiply(a, a), multiply(c, c)
    both_cluster = add(multiply(r, r), scale(2, r),
                       scale(-2, multiply(r, add(r, constant(1)))),
                       scale(2, a2), scale(2, c2))
    equal(both_cluster, multiply(difference, difference),
          "both-cluster bound differs by (a-c)^2/(2r)")

    even = add(scale(4, multiply(a, r)), scale(-3, a2),
               scale(-6, multiply(a, c)), scale(6, c2), scale(-6, c))
    even_form = add(multiply(difference, difference), scale(5, c2), scale(-6, c))
    equal(even, even_form, "even mixed-regime polynomial")
    equal(add(scale(5, multiply(add(c, constant(2)), add(c, constant(2)))),
              scale(-6, add(c, constant(2)))),
          add(scale(5, c2), scale(14, c), constant(8)),
          "even mixed residual is positive for c>=2")
    equal(add(multiply(add(a, constant(-1)), add(a, constant(-1))), constant(-1)),
          multiply(a, add(a, constant(-2))), "even c=1 factorization")

    odd = add(even, scale(-3, a))
    odd_in_a_c = add(multiply(difference, difference), scale(5, c2),
                     scale(-3, difference), scale(-9, c))
    equal(odd, odd_in_a_c, "odd mixed-regime polynomial")
    odd_in_d_c = add(multiply(d, d), scale(-3, d), scale(5, c2), scale(-9, c))
    a_from_d = add(c, d)
    equal(add(multiply(a_from_d, a_from_d), scale(-2, multiply(a_from_d, c)),
              scale(6, c2), scale(-3, a_from_d), scale(-6, c)),
          odd_in_d_c, "odd substitution d=a-c")
    residual_c_ge_three = add(
        multiply(add(d, constant(-1)), add(d, constant(-2))),
        scale(5, multiply(add(c, constant(3)), add(c, constant(3)))),
        scale(-9, add(c, constant(3))), constant(-2),
    )
    equal(residual_c_ge_three,
          add(multiply(add(d, constant(-1)), add(d, constant(-2))),
              scale(5, c2), scale(21, c), constant(16)),
          "odd c>=3 positive residual after integer d bound")
    equal(add(multiply(d, d), scale(-3, d), constant(2)),
          multiply(add(d, constant(-1)), add(d, constant(-2))),
          "odd c=2 factorization")
    equal(add(multiply(d, d), scale(-3, d), constant(-4)),
          multiply(add(d, constant(-4)), add(d, constant(1))),
          "odd c=1 exceptional factorization")
    require(F(1, 4) - F(2, 3) * F(6103, 16383)
            == F(325, 196596) > 0, "strict height-obstruction margin")

    # With N>=1 and q>=2 this identity proves q-1<=N(q-2)+1.
    N, q = a, c
    equal(add(multiply(N, add(q, constant(-2))), constant(1),
              scale(-1, add(q, constant(-1)))),
          multiply(add(N, constant(-1)), add(q, constant(-2))),
          "spread endpoint remainder inequality")
    return {
        "exact_polynomial_identities": 10,
        "both_cluster_difference": "(a-c)^2/(2(a+c))",
        "even_mixed_polynomial": "(a-c)^2+5c^2-6c",
        "odd_mixed_polynomial": "(a-c)^2+5c^2-3(a-c)-9c",
        "odd_c2_factorization": "(d-1)(d-2), d=a-c odd>=1",
        "odd_c1_factorization": "(d-4)(d+1), d=a-1 even",
        "only_mixed_exception": [3, 1],
        "both_cluster_safe_total_minimum": 6,
        "height_margin": "325/196596",
        "scope": "Coefficient identities hold for all parameters. The manuscript supplies positivity from a>=c>=1, parity, and integer d, and the analytic order-cell argument.",
    }


def profile(points):
    """Return pre/post extremes of the unit-drop periodic profile."""
    jumps = Counter(point % 1 for point in points)
    size = sum(jumps.values())
    count = 0
    before_values, after_values = [], []
    for point, multiplicity in sorted(jumps.items()):
        before = size * point - count
        before_values.append(before)
        after_values.append(before - multiplicity)
        count += multiplicity
    require(count == size and size > 0, "nonempty complete profile")
    return max(before_values) - min(after_values)


def single_arc_checks():
    digest = sha256()
    clustered = endpoints = interiors = special_three = 0
    largest_normalized = F(0)
    for d in range(1, 39):
        for j in range(1, 17):
            u = F(j, 16 * d)
            points = [i * u for i in range(d)]
            value = profile(points)
            require(value == d * (1 - (d - 1) * u), "exact clustered single arc")
            clustered += 1
        if d == 1:
            continue
        cuts = {F(1, d), F(1, 2)}
        for denominator in range(2, d):
            for numerator in range(1, denominator // 2 + 1):
                u = F(numerator, denominator)
                if F(1, d) <= u <= F(1, 2):
                    cuts.add(u)
        ordered = sorted(cuts)
        values = []
        for u in ordered:
            jumps = Counter((i * u) % 1 for i in range(d))
            q = u.denominator
            N, remainder = divmod(d, q)
            uniform = Counter({F(i, q): N for i in range(q)})
            tail = Counter((i * u) % 1 for i in range(remainder))
            require(2 <= q <= d and N >= 1, "complete collision endpoint domain")
            require(jumps == uniform + tail, "uniform periods plus residual jumps")
            require(remainder <= q - 1 <= N * (q - 2) + 1,
                    "unbounded spread remainder inequality at every endpoint")
            value = profile(jumps.elements())
            require(value <= N + remainder <= F(d + 1, 2), "endpoint half bound")
            require(N + remainder <= (d + 1) // 2, "integral ceiling improvement")
            values.append(value)
            largest_normalized = max(largest_normalized, value / d)
            digest.update(f"{d}:{u}:{value}:{N}:{remainder}\n".encode())
            endpoints += 1
        for index in range(len(ordered) - 1):
            for t in (F(1, 3), F(1, 2), F(2, 3)):
                u = (1 - t) * ordered[index] + t * ordered[index + 1]
                value = profile([i * u for i in range(d)])
                require(value <= (1 - t) * values[index] + t * values[index + 1],
                        "finite interior convexity control")
                require(value <= (d + 1) // 2, "spread ceiling control")
                interiors += 1
    for j in range(97):
        u = F(1, 3) + F(j, 576)
        require(profile([F(0), u, 2 * u]) == 6 * u - 1,
                "exact three-point profile on [1/3,1/2]")
        special_three += 1
    return {
        "multiplicities": [1, 38],
        "cluster_controls": clustered,
        "complete_collision_endpoints": endpoints,
        "interior_convexity_controls": interiors,
        "three_point_exact_controls": special_three,
        "largest_endpoint_normalized_oscillation": str(largest_normalized),
        "profile_sha256": digest.hexdigest(),
        "scope": "Every collision-cell endpoint for 2<=d<=38 is checked. Interior and clustered grids are controls; the manuscript proves the formulas and convexity for unbounded d.",
    }


def upper_bound(a, c, u):
    """Analytic subadditive envelope, with the exact (3,1) refinement."""
    if (a, c) == (3, 1) and u >= F(1, 3):
        return 6 * u
    first = a * (1 - (a - 1) * u) if a * u <= 1 else F((a + 1) // 2)
    second = c * (1 - (c - 1) * u) if c * u <= 1 else F((c + 1) // 2)
    return first + second


def unsafe_intervals(a, c):
    lower, upper = F(1, a + c), F(1, 2)
    if lower == upper:
        return []
    threshold = F(2 * (a + c), 3)
    cuts = {lower, upper}
    for value in (F(1, a), F(1, c)):
        if lower < value < upper:
            cuts.add(value)
    ordered = sorted(cuts)
    for left, right in zip(ordered, ordered[1:]):
        x, y = (2 * left + right) / 3, (left + 2 * right) / 3
        slope = (upper_bound(a, c, y) - upper_bound(a, c, x)) / (y - x)
        intercept = upper_bound(a, c, x) - slope * x
        if slope:
            crossing = (threshold - intercept) / slope
            if left < crossing < right:
                cuts.add(crossing)
    ordered = sorted(cuts)
    intervals = []
    for left, right in zip(ordered, ordered[1:]):
        if upper_bound(a, c, (left + right) / 2) > threshold:
            lower_closed = upper_bound(a, c, left) > threshold
            upper_closed = right < upper and upper_bound(a, c, right) > threshold
            if intervals and intervals[-1][1] == left and lower_closed:
                previous = intervals.pop()
                intervals.append((previous[0], right, previous[2], upper_closed))
            else:
                intervals.append((left, right, lower_closed, upper_closed))
    for point in ordered:
        if point < upper and upper_bound(a, c, point) > threshold:
            require(any((left < point < right) or (point == left and lc)
                        or (point == right and rc) for left, right, lc, rc in intervals),
                    "no isolated unsafe boundary omitted")
    return intervals


def regime_checks():
    found = {}
    pairs = 0
    for total in range(2, 39):
        for c in range(1, total // 2 + 1):
            a = total - c
            intervals = unsafe_intervals(a, c)
            if intervals:
                found[(a, c)] = intervals
            pairs += 1
    expected = {
        (2, 1): [(F(1, 3), F(1, 2), True, False)],
        (2, 2): [(F(1, 4), F(1, 3), True, False)],
        (3, 1): [(F(4, 9), F(1, 2), False, False)],
        (3, 2): [(F(1, 5), F(5, 24), True, False)],
    }
    require(found == expected, "exact residual interval classification")
    require(pairs == 361, "all unordered arc pairs with total at most38")
    return {
        "unordered_pairs": pairs,
        "maximum_total": 38,
        "residual_intervals": [
            {"arc_lengths": list(pair), "lower": str(interval[0]),
             "upper": str(interval[1]), "lower_included": interval[2],
             "upper_included": interval[3]}
            for pair, intervals in sorted(found.items()) for interval in intervals
        ],
        "scope": "Exact rational piecewise-linear classification in the needed bounded range. The preceding symbolic inequalities cover all larger arc lengths.",
    }


def concentration_checks():
    digest = sha256()
    records = []
    for a, c, lower, upper, height in (
        (2, 1, F(1, 3), F(1, 2), 2),
        (3, 2, F(1, 5), F(1, 3), 3),
    ):
        candidates = overlaps = controls = blocks = 0
        maximum = F(0)
        for M in range(6, 49):
            for h in range(1, M // 2 + 1):
                u = F(h, M)
                if not lower <= u <= upper:
                    continue
                first = [F(i * h, M) % 1 for i in range(a)]
                for v_int in range(M):
                    candidates += 1
                    second = [F(v_int + i * h, M) % 1 for i in range(c)]
                    points = sorted(first + second)
                    total = a + c
                    if len(set(points)) != total:
                        overlaps += 1
                        continue
                    value = profile(points)
                    losses = []
                    for start in range(total):
                        for count in range(1, total + 1):
                            span = (points[(start + count - 1) % total] - points[start]) % 1
                            loss = count - total * span
                            if (a, c) == (2, 1) and count == 3:
                                require(span >= u and 3 - 3 * u <= 2,
                                        "three-point containing arc has span at leastu")
                            if (a, c) == (3, 2) and count == 4:
                                require(span >= u and 4 - 5 * u <= 3,
                                        "four points contain an orbit pair at separation at leastu")
                            if (a, c) == (3, 2) and count == 5:
                                require(span >= 2 * u and 5 - 10 * u <= 3,
                                        "five points contain the full three-point orbit segment")
                            require(loss <= height, "concentration block-loss bound")
                            losses.append(loss)
                            blocks += 1
                    require(value == max(losses) <= height, "oscillation equals maximum circular block loss")
                    maximum = max(maximum, value)
                    controls += 1
                    digest.update(f"{a}:{c}:{M}:{h}:{v_int}:{value}\n".encode())
        require(maximum == height and controls > 0 and overlaps > 0,
                "sharp concentration controls and rejected overlaps")
        records.append({
            "arc_lengths": [a, c], "denominators": [6, 48],
            "u_interval": [str(lower), str(upper)], "endpoints_included": True,
            "candidates": candidates, "overlapping_sets_rejected": overlaps,
            "distinct_profiles": controls, "circular_blocks": blocks,
            "maximum_oscillation": str(maximum),
            "normalized_upper": str(F(height, a + c)),
        })
    return {
        "records": records, "profile_sha256": digest.hexdigest(),
        "scope": "Finite exact controls of the circular-block identity and span bounds. No coprimality, faithful-boundary, or integer-cycle conclusion is asserted for this grid; the manuscript proves the bounds for every distinct maximum set in the stated intervals.",
    }


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]),
            "usage: checker [--write-receipt]")
    receipt = {
        "schema": "two-maximum-arc-classification-v1",
        "polynomial_checks": polynomial_checks(),
        "single_arc_checks": single_arc_checks(),
        "regime_checks": regime_checks(),
        "concentration_checks": concentration_checks(),
    }
    encoded = json.dumps(receipt, sort_keys=True, indent=2) + "\n"
    destination = HERE / "check_arc_classification.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded,
                "classification receipt differs; regenerate explicitly")
    print(json.dumps({
        "status": "passed",
        "collision_endpoints": receipt["single_arc_checks"]["complete_collision_endpoints"],
        "classified_pairs": receipt["regime_checks"]["unordered_pairs"],
        "concentration_profiles": sum(row["distinct_profiles"]
                                      for row in receipt["concentration_checks"]["records"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
