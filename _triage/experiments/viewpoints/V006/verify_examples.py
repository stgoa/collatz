#!/usr/bin/env python3
"""Bounded exact checks for V006. Universal claims remain written proofs."""

import argparse
import hashlib
import json
from itertools import combinations, product
from pathlib import Path


if not __debug__:
    raise RuntimeError("Run verification without Python optimization flags")


def weight(n):
    assert n >= 0
    return bin(n).count("1")


def power_color(t):
    assert t >= 0
    return int(t > 0 and t & (t - 1) == 0)


def adjacent_pairs(n):
    assert n >= 0
    return weight(n & (n >> 1))


def digest(rows):
    return hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


def next_power(threshold):
    p = 1
    while p <= threshold:
        p *= 2
    return p


def quadratic_checks():
    blocks = []
    for r in range(1, 7):
        modulus = 3**r
        length = 2 * 3 ** (r - 1)
        assert pow(2, length // 2, modulus) == modulus - 1
        for repetitions in range(1, 4):
            k = length * repetitions
            q, remainder = divmod(2**k - 1, modulus)
            assert remainder == 0 and q % 2 == 1
            assert weight(q) == k // 2
            assert weight(q - 1) == k // 2 - 1
            blocks.append((r, repetitions, k, weight(q)))

    depth = 6
    states = [(a, t) for a in range(depth + 1) for t in range(depth - a + 1)]
    witnesses = []
    for offset in (0, 3):
        for (a, t), (b, u) in combinations(states, 2):
            m, ell = 3**a, 3**b
            if t != u:
                p = next_power(2 * (offset + t + u + m.bit_length() + ell.bit_length() + 2))
                k = p - offset - t
                n = 2**k - 1
                assert weight(m * n) == weight(ell * n) == k
                c = 1
            else:
                assert a < b  # states are ordered by a, then t
                length = 2 * 3 ** (b - 1)
                capital_k = length
                while capital_k // 2 + weight(m - 1) - weight(ell - 1) <= 0:
                    capital_k += length
                c, remainder = divmod(2**capital_k - 1, ell)
                assert remainder == 0 and c > 0
                delta_m = weight(m * c - 1) - weight(m - 1)
                delta_ell = weight(ell * c - 1) - weight(ell - 1)
                assert delta_m == capital_k // 2 - 1 - weight(m - 1)
                assert delta_ell == capital_k - 1 - weight(ell - 1)
                gap = delta_ell - delta_m
                assert gap > 0
                p = next_power(2 * (capital_k + offset + t + abs(delta_m) + gap + 2))
                k = p - offset - t + delta_m
                assert k > capital_k
                n = 2**k - c
                assert weight(m * n) == k - delta_m
                assert weight(ell * n) == k - delta_ell
            assert n >= 0 and 2**k > max(m * c, ell * c)
            left = power_color(offset + t + weight(m * n))
            right = power_color(offset + u + weight(ell * n))
            assert left != right
            witnesses.append((offset, a, t, b, u, k, c, left, right))
    return {
        "balanced_blocks": len(blocks),
        "r_range": [1, 6],
        "block_repetitions": [1, 3],
        "joint_depth": depth,
        "states_per_offset": len(states),
        "offsets": [0, 3],
        "distinguishing_witnesses": len(witnesses),
        "blocks_sha256": digest(blocks),
        "witnesses_sha256": digest(witnesses),
    }


def pattern_checks():
    def z(n):
        return power_color(adjacent_pairs(n))

    rows, reachable_counts, accumulated = [], [], {(0, 0)}
    evaluations = 0
    for a in range(1, 9):
        for r in range(2**a):
            t = adjacent_pairs(r)
            epsilon = (r >> (a - 1)) & 1
            assert 0 <= t <= a - 1
            accumulated.add((t, epsilon))
            for n in range(128):
                assert z(2**a * n + r) == power_color(t + adjacent_pairs(n) + epsilon * (n % 2))
                evaluations += 1
        assert len(accumulated) <= 2 * a
        reachable_counts.append([a, len(accumulated)])

    for n in range(4096):
        assert z(2 * n) == z(n)
        assert z(8 * n + 5) == z(2 * n + 1)
    assert z(0) == z(1) == 0
    assert z(3) == 1 and z(10) == 0

    for t, epsilon in sorted(accumulated):
        k = next(k for k in range(1, 129) if power_color(t + k - 1) != power_color(t))
        n1 = 2 * (2**k - 1)
        n2 = sum(2 ** (2 * i) for i in range(1, k + 1))
        assert n1 % 2 == n2 % 2 == 0
        assert weight(n1) == weight(n2) == k
        assert adjacent_pairs(n1) == k - 1 and adjacent_pairs(n2) == 0
        left = power_color(t + adjacent_pairs(n1) + epsilon * (n1 % 2))
        right = power_color(t + adjacent_pairs(n2) + epsilon * (n2 % 2))
        assert left != right
        rows.append((t, epsilon, k, left, right))
    return {
        "section_depths": [1, 8],
        "section_evaluations": evaluations,
        "reachable_parameter_counts": reachable_counts,
        "identity_inputs": 4096,
        "no_digit_count_witnesses": len(rows),
        "witnesses_sha256": digest(rows),
        "full_guard_failure": {"source": 3, "image": 10, "colors": [1, 0]},
        "scope": "Explicit whole-section formulas justify upper bounds; finite witnesses distinguish the listed parameter states from digit-count functions.",
    }


def action_checks():
    def step(n, label):
        return n + 1 + label * power_color(n)

    def run(word, n):
        for label in word:
            n = step(n, label)
        return n

    reached = {0}
    for depth in range(33):
        assert len(reached) >= depth + 1
        assert reached <= set(range(2 * depth + 1))
        reached |= {step(n, label) for n in reached for label in (0, 1)}
    rows = []
    for depth in range(1, 8):
        words = list(product((0, 1), repeat=depth))
        p = next_power(4 * depth)
        for left, right in combinations(words, 2):
            k = next(i for i in range(depth) if left[i] != right[i])
            start = p - k
            x, y = run(left, start), run(right, start)
            assert x != y and abs(x - y) == 1
            rows.append((depth, left, right, k, x, y))
    return {
        "root_orbit_depth": 32,
        "transformation_word_depths": [1, 7],
        "pair_witnesses": len(rows),
        "witnesses_sha256": digest(rows),
        "scope": "Abstract maps T,U; not claimed to be affine section operators.",
    }


def cycle_controls():
    rows = []
    for d in (5, 61):
        color = lambda n: int(n % d == 0)
        assert color(1) == 0 and color(d) == 1
        value = 3 * d + d
        while value % 2 == 0:
            value //= 2
        assert value == d
        for n in range(1, 4 * d + 1):
            assert color(2 * n) == color(n)
            if n > 1 and n % 2:
                assert color(3 * n + d) == color(n)
        odd_color = lambda n: color(2 * n + 1)
        witness = next(n for n in range(d) if odd_color(3 * n) != odd_color(4 * n))
        rows.append({
            "d": d,
            "fixed_odd_cycle": [d],
            "checked_sources": 4 * d,
            "d1_root_identity_failure": {
                "n": witness,
                "colors_b3n_b4n": [odd_color(3 * witness), odd_color(4 * witness)],
            },
        })
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve()
    receipt = {
        "schema": 1,
        "status": "PASS",
        "scope": "Bounded exact examples and explicit distinguishing inputs. Universal proofs and the unresolved all-invariant target are separate.",
        "verifier_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
        "quadratic": quadratic_checks(),
        "pattern_control": pattern_checks(),
        "action_control": action_checks(),
        "d_controls": cycle_controls(),
    }
    path = source.with_name("verification.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
        print("PASS: wrote V006 bounded verification receipt")
    else:
        assert json.loads(path.read_text()) == receipt, "Receipt mismatch"
        print("PASS: V006 bounded checks match the unchanged receipt")


if __name__ == "__main__":
    main()
