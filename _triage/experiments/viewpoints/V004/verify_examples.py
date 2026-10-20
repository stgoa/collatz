#!/usr/bin/env python3
"""Bounded exact examples for V004; default replay never edits the receipt.

These tests do not prove the all-input classification or replay Cobham.
All orbit witnesses use the ordinary absorbed map unless labeled odd-only.
Use --write-receipt explicitly to regenerate verification.json.
"""

import argparse
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(value):
    return sha256(json.dumps(value, sort_keys=True,
                             separators=(",", ":")).encode()).hexdigest()


def valuation2(n):
    require(isinstance(n, int) and n > 0, "positive integer required")
    return (n & -n).bit_length() - 1


def validate_d(d):
    require(isinstance(d, int) and d > 0 and gcd(d, 6) == 1,
            "d must be a positive odd ternary unit")


def ordinary(n, d=1):
    validate_d(d)
    require(isinstance(n, int) and n > 0, "positive source required")
    if n == 1:
        return 1
    return 3 * n + d if n % 2 else n // 2


def odd_step(n, d=1):
    validate_d(d)
    require(isinstance(n, int) and n > 0 and n % 2,
            "positive odd source required")
    if n == 1:
        return 1, None
    raw = 3 * n + d
    a = valuation2(raw)
    return raw >> a, a


def path_to(source, target, cap, d=1):
    """An exact finite witness; exhausting the cap is unresolved, not success."""
    require(isinstance(cap, int) and cap >= 0, "nonnegative cap required")
    require(source > 0 and target > 0, "positive path endpoints required")
    states, seen = [source], {source}
    if source == target:
        return states
    for _ in range(cap):
        nxt = ordinary(states[-1], d)
        states.append(nxt)
        if nxt == target:
            return states
        require(nxt not in seen, "cycle before prescribed target")
        seen.add(nxt)
    raise ValueError("unresolved: finite path cap exhausted")


def ternary_image(a, r, j):
    require(isinstance(a, int) and a >= 1 and 0 < r < 2**a,
            "positive binary offset required")
    require(j in (0, 1, 2), "ternary digit required")
    c = 2**a * j + r
    if c % 3:
        v = 1 if c % 3 == 2 else 2
        t = (2**v * c - 1) // 3
        require(3 * t == 2**v * c - 1 and t % 2 == 1,
                "inverse affine source is not odd integral")
        return a + v, t, "unit", v
    t = c // 3
    ell = valuation2(t)
    u = t >> ell
    require(ell < a, "divisible offset lost its finite positive section")
    return a - ell + 4, 16 * u + 1, "divisible", ell


def check_sections():
    transformations, binary, paths = [], [], []
    branch_counts = {"unit": 0, "divisible": 0}
    arrows = max_clock = boundary_source1 = 0
    for a in range(1, 8):
        for r in range(1, 2**a):
            for digit in (0, 1):
                offset = 2**a * digit + r
                require(0 < offset < 2**(a + 1), "binary closure bound failed")
                for n in range(9):
                    require(2**a * (2 * n + digit) + r
                            == 2**(a + 1) * n + offset,
                            "binary section index identity failed")
                binary.append([a, r, digit, a + 1, offset])
            for j in range(3):
                out_a, out_r, branch, auxiliary = ternary_image(a, r, j)
                require(0 < out_r < 2**out_a, "positive output offset bound failed")
                branch_counts[branch] += 1
                transformations.append([a, r, j, out_a, out_r, branch])
                for n in range(9):
                    left = 2**a * (3 * n + j) + r
                    right = 2**out_a * n + out_r
                    if branch == "unit":
                        require(3 * right + 1 == 2**auxiliary * left,
                                "unit branch affine equation failed")
                        endpoint = left
                        if right == 1:
                            require(left in (1, 2), "source1 repair used outside its domain")
                            # The raw arrow1->4 is unavailable. The actual
                            # left path2->1 supplies the needed value equality.
                            endpoint = 1
                            boundary_source1 += 1
                    else:
                        ell = auxiliary
                        require(left % 2**ell == 0, "divisible branch normalization failed")
                        z = left // (3 * 2**ell)
                        require(z > 0 and z % 2 and right == 16 * z + 1,
                                "divisible branch positive odd source failed")
                        endpoint = 9 * z + 1
                    # These independently evaluated actual paths certify the value
                    # comparison, without assuming any candidate coloring constant.
                    p_left = path_to(left, endpoint, 16)
                    p_right = path_to(right, endpoint, 16)
                    arrows += len(p_left) + len(p_right) - 2
                    max_clock = max(max_clock, len(p_left) - 1, len(p_right) - 1)
                    paths.append([a, r, j, n, p_left, p_right])
    require(ternary_image(2, 1, 1)[:2] == (3, 3), "first worked example changed")
    require(ternary_image(2, 3, 0)[:2] == (6, 17), "second worked example changed")
    return {"a_range": [1, 7], "n_range": [0, 8],
            "all_positive_offsets": True, "all_ternary_digits": True,
            "binary_transformations": len(binary), "binary_index_checks": len(binary) * 9,
            "ternary_transformations": len(transformations), "branches": branch_counts,
            "common_endpoint_comparisons": len(paths), "ordinary_paths": 2 * len(paths),
            "ordinary_arrows": arrows, "maximum_ordinary_clock": max_clock,
            "path_cap": 16, "source1_identity_cases": boundary_source1,
            "transformations_sha256": digest(transformations), "paths_sha256": digest(paths)}


def components(modulus, d):
    """Build the relations independently as an undirected finite graph."""
    neighbors = [set() for _ in range(modulus)]
    for x in range(modulus):
        for left, right in ((x, (4 * x + d) % modulus),
                            (3 * x % modulus, 4 * x % modulus)):
            neighbors[left].add(right)
            neighbors[right].add(left)
    unseen, result = set(range(modulus)), []
    while unseen:
        todo, found = [min(unseen)], set()
        while todo:
            x = todo.pop()
            if x not in found:
                found.add(x)
                todo.extend(neighbors[x] - found)
        unseen -= found
        result.append(sorted(found))
    return result


def check_periodic_finish():
    period_lifts = []
    for period in range(1, 65):
        e = valuation2(period)
        odd_period = period >> e
        for n in (0, 1, 7, 30):
            left, right, k = n, n + odd_period, 0
            while left < 1000 or 2 * k < e:
                left, right, k = 4 * left + 2, 4 * right + 2, k + 1
            require(right - left == 4**k * odd_period
                    and (right - left) % period == 0,
                    "eventual-to-global odd period lift failed")
            period_lifts.append([period, n, odd_period, k, left, right])
    family_paths = []
    for x in range(1, 64, 2):
        common = 1 if x == 1 else 3 * x + 1
        family_paths.append([x, path_to(x, common, 8), path_to(4 * x + 1, common, 8)])
    graphs, commutators = [], 0
    for modulus in range(1, 256, 2):
        partition = components(modulus, 1)
        require(partition == [list(range(modulus))], "d1 residue relations disconnected")
        m, power3 = modulus, 0
        while m % 3 == 0:
            m //= 3
            power3 += 1
        # Check collapse of the3-part on entire congruence classes.
        if modulus > 1:
            multiplier = 3 * pow(4, -1, modulus) % modulus
            images = {}
            for x in range(modulus):
                image = pow(multiplier, power3, modulus) * x % modulus
                if x % m in images:
                    require(images[x % m] == image, "ternary factor collapse failed")
                images[x % m] = image
        if m > 1:
            inv4 = pow(4, -1, m)
            for x in range(m):
                hj = 3 * inv4 * (4 * x + 1) % m
                jh = (4 * (3 * inv4 * x) + 1) % m
                require((jh - hj) % m == inv4 and gcd(inv4, m) == 1,
                        "unit translation commutator failed")
                commutators += 1
        graphs.append([modulus, m, power3, len(partition)])
    return {"odd_moduli": [1, 255], "relation_graphs": len(graphs),
            "residue_vertices": sum(row[0] for row in graphs),
            "all_d1_graphs_connected": True, "commutator_residues": commutators,
            "period_lift_examples": len(period_lifts), "period_range": [1, 64],
            "eventual_cutoff_used": 1000, "F_identity_path_pairs": len(family_paths),
            "graphs_sha256": digest(graphs), "period_lifts_sha256": digest(period_lifts),
            "F_paths_sha256": digest(family_paths)}


def check_controls():
    colors, cycles, failures, graphs = [], [], [], []
    for d, start, expected_length, expected_sum in ((5, 19, 3, 5), (61, 235, 41, 66)):
        color = lambda n: int(n % d == 0)
        require(color(1) == 0 and color(d) == 1, "control coloring is not nonconstant")
        for n in range(1, 8 * d + 1):
            require(color(2 * n) == color(n), "control doubling invariance failed")
            if n % 2:
                endpoint, a = odd_step(n, d)
                require(color(endpoint) == color(n), "control absorbed odd invariance failed")
                if n > 1:
                    require(color(3 * n + d) == color(n), "control ordinary identity failed")
                colors.append([d, n, endpoint, a])
        states, valuations, seen, n = [], [], set(), start
        for _ in range(64):
            require(n > 1 and n not in seen, "cycle control stopped or repeated early")
            states.append(n)
            seen.add(n)
            n, a = odd_step(n, d)
            require(a is not None, "cycle used absorber instead of actual odd arrow")
            valuations.append(a)
            if n == start:
                break
        require(n == start, "unresolved: cycle control cap exhausted")
        require(len(states) == expected_length and sum(valuations) == expected_sum
                and min(states) == start, "known cycle data differ")
        require(odd_step(1, d) == (1, None) and odd_step(d, d)[0] == d,
                "absorber or nonabsorbing fixed-point control failed")
        cycles.append({"d": d, "states": states, "valuations": valuations,
                       "odd_length": len(states), "valuation_sum": sum(valuations),
                       "absorber": 1, "cap": 64})
        u = d
        require(color(3 * u) == 1 and color(16 * u + 1) == 0,
                "d1 closure identity incorrectly transferred to d-control")
        failures.append({"d": d, "u": u, "left": 3 * u, "right": 16 * u + 1,
                         "left_color": 1, "right_color": 0,
                         "failed_identity": "h(3u)=h(16u+1)"})
        partition = components(d, d)
        require(len(partition) > 1 and [0] in partition,
                "general-d graph lost divisibility control")
        for block in partition:
            require(len({color(x) for x in block}) == 1,
                    "control color is not constant on generated relations")
        graphs.append({"d": d, "modulus": d, "components": partition})
    return {"d_values": [5, 61], "doubling_checks": 8 * (5 + 61),
            "absorbed_odd_checks": len(colors), "ordinary_odd_checks": len(colors) - 2,
            "color_checks_sha256": digest(colors), "cycles": cycles,
            "identity_transfer_failures": failures, "control_relation_graphs": graphs}


def check_rejections():
    cases = [
        ("zero offset", lambda: ternary_image(3, 0, 0), "positive binary offset"),
        ("offset at modulus", lambda: ternary_image(3, 8, 0), "positive binary offset"),
        ("bad ternary digit", lambda: ternary_image(3, 1, 3), "ternary digit"),
        ("nonpositive valuation", lambda: valuation2(0), "positive integer"),
        ("even odd-clock source", lambda: odd_step(2), "positive odd source"),
        ("unsupported d", lambda: odd_step(5, 3), "ternary unit"),
        ("negative cap", lambda: path_to(3, 1, -1), "nonnegative cap"),
        ("exhausted path cap", lambda: path_to(27, 1, 1), "unresolved"),
        ("nonabsorbing target search", lambda: path_to(19, 1, 32, 5), "cycle"),
    ]
    checked = []
    for name, function, expected in cases:
        try:
            function()
        except ValueError as error:
            require(expected in str(error), "wrong rejection for " + name)
            checked.append(name)
        else:
            raise ValueError("invalid or unresolved case was accepted: " + name)
    return checked


def report():
    return {"schema": 1, "status": "PASS",
            "verifier_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
            "scope": "Bounded exact arithmetic and actual finite paths only. This replay does not prove positive-section closure at all depths, the full invariant classification, Cobham, or convergence.",
            "clock": "Ordinary absorbed arrows for closure witnesses; explicitly odd-only for cycle controls. Section depth is not an orbit clock.",
            "sections": check_sections(), "periodic_finish": check_periodic_finish(),
            "controls": check_controls(), "rejections": check_rejections()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    parser.add_argument("--receipt", type=Path, default=HERE / "verification.json")
    args = parser.parse_args()
    try:
        actual = report()
        if args.write_receipt:
            args.receipt.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n")
        else:
            require(json.loads(args.receipt.read_text()) == actual,
                    "receipt mismatch; no evidence was modified")
    except (ValueError, TypeError, OSError) as error:
        print("FAIL: " + str(error), file=sys.stderr)
        return 1
    print("PASS: V004 bounded section, actual-path, residue and cycle examples")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
