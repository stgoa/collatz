#!/usr/bin/env python3
"""Focused exact audit of the S.2 power-growth-norm barrier."""
import argparse
from contextlib import redirect_stderr
from fractions import Fraction
import hashlib
import io
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "growth_norm_audit.json"
WORDS = ((3,), (5,), (2, 3), (1, 5))
SLOPES = (Fraction(3, 8), Fraction(3, 32), Fraction(9, 32), Fraction(9, 64))


def need(condition, message):
    if not condition:
        raise ValueError(message)


def natural(x, name, lower=0):
    need(type(x) is int and x >= lower, f"invalid {name}")


def supported(d):
    natural(d, "d", 1)
    need(gcd(d, 6) == 1, "unsupported d")


def alpha(p, q):
    natural(p, "alpha numerator", 1)
    natural(q, "alpha denominator", 1)
    need(p < q and gcd(p, q) == 1, "alpha must be reduced and in (0,1)")


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
    need(lo**degree <= value < (lo + 1)**degree, "root bracket failed")
    return lo


def target(d, p, q, j):
    supported(d)
    alpha(p, q)
    natural(j, "target index", 1)
    v = j**q
    r = integer_root(v, p)
    return 18 * (r + int(r**p < v)) + 5 * d


def count_targets(d, p, q, X):
    supported(d)
    alpha(p, q)
    need(type(X) is int, "cutoff must be integer")
    m = max(0, (X - 5 * d) // 18)
    return integer_root(m**p, q)


def step(d, n):
    supported(d)
    natural(n, "odd state", 1)
    need(n % 2 == 1, "even state")
    if n == 1:
        return 1, None
    value = 3 * n + d
    divisor = value & -value
    return value // divisor, divisor.bit_length() - 1


def verify_path(d, n, word, endpoint):
    supported(d)
    natural(n, "source", 3)
    natural(endpoint, "target", 3)
    need(n % 2 == endpoint % 2 == 1, "even source or target")
    need(word in WORDS, "unrecognized valuation word")
    x, path = n, [n]
    for i, a in enumerate(word):
        x, actual = step(d, x)
        need(actual == a, "wrong exact valuation")
        path.append(x)
        if i + 1 < len(word):
            need(2 * x > n, "half descent happened before claimed endpoint")
    need(x == endpoint, "wrong endpoint")
    need(2 * endpoint <= n, "endpoint does not half-descend")
    return path


def sources(d, y):
    supported(d)
    natural(y, "target", 3)
    need(y > 5 * d and (y - 5 * d) % 18 == 0, "target outside source family")
    numerators = (8 * y - d, 32 * y - d, 32 * y - 7 * d, 64 * y - 5 * d)
    denominators = (3, 3, 9, 9)
    need(all(v % r == 0 for v, r in zip(numerators, denominators)),
         "inverse congruence failed")
    ns = [v // r for v, r in zip(numerators, denominators)]
    for n, word in zip(ns, WORDS):
        verify_path(d, n, word, y)
    return ns


def selected_count(d, p, q, X):
    natural(X, "source cutoff", 1)
    limits = ((3 * X + d) // 8, (3 * X + d) // 32,
              (9 * X + 7 * d) // 32, (9 * X + 5 * d) // 64)
    return sum(count_targets(d, p, q, Y) for Y in limits)


def exact_constants():
    lower = (Fraction(2, 5), Fraction(1, 8), Fraction(5, 16), Fraction(1, 6))
    comparisons = []
    for base, bound in zip(SLOPES, lower):
        lhs = base.numerator**7 * bound.denominator**8
        rhs = base.denominator**7 * bound.numerator**8
        need(lhs > rhs, "endpoint lower-bound comparison failed")
        comparisons.append(dict(base=str(base), lower_bound=str(bound),
                                lhs=lhs, rhs=rhs, positive_gap=lhs-rhs))
    need(sum(lower) == Fraction(241, 240), "expansion constant sum failed")
    need(3**4 < 2**7 and 3**5 < 4**4, "one-arrow constant failed")
    need(Fraction(3, 4) * Fraction(40, 39) == Fraction(10, 13),
         "one-arrow product failed")
    reduced = [[3**7 * 5**8, 2**29], [3**7, 2**11],
               [3**14, 8 * 5**8], [3**22, 2**34]]
    need(all(a > b for a, b in reduced), "reduced integer certificates failed")
    return dict(expansion_sum="241/240", expansion_comparisons=comparisons,
                reduced_comparisons=reduced,
                contraction_constant="10/13",
                contraction_comparisons=[[3**4, 2**7], [3**5, 4**4]])


def family_checks():
    rows, paths, arrows, jumps, cuts = [], 0, 0, 0, 0
    for d in (1, 5, 7, 13, 61):
        for p, q in ((1, 2), (4, 5), (5, 6), (7, 8)):
            ys = [target(d, p, q, j) for j in range(1, 97)]
            need(all(a < b for a, b in zip(ys, ys[1:])), "target order failed")
            witnesses, all_sources = [], set()
            for y in ys:
                for word, n in zip(WORDS, sources(d, y)):
                    need(n not in all_sources, "source collision")
                    all_sources.add(n)
                    witnesses.append((y, word, n))
            for y in ys[:24]:
                for word, n in zip(WORDS, sources(d, y)):
                    path = verify_path(d, n, word, y)
                    need(len(path) == len(word) + 1, "clock mismatch")
                    paths += 1
                    arrows += len(word)
                for X in (y - 1, y, y + 1):
                    count = count_targets(d, p, q, X)
                    need(count == sum(z <= X for z in ys), "target jump count failed")
                    need(18**p * count**q <= X**p, "input norm upper bound failed")
                    jumps += 1
            cutoffs = {1, 3, 12, 13}
            for y in ys[:8]:
                for n in sources(d, y):
                    cutoffs.update((n - 1, n, n + 1))
            for X in sorted(cutoffs):
                top_limit = max((3*X+d)//8, (3*X+d)//32,
                                (9*X+7*d)//32, (9*X+5*d)//64)
                need(top_limit < ys[-1], "finite target materialization is incomplete")
                expected = selected_count(d, p, q, X)
                actual = sum(n <= X for _, _, n in witnesses)
                need(actual == expected, "selected-source cutoff identity failed")
                cuts += 1
            rows.append(dict(d=d, alpha=f"{p}/{q}", checked_targets=24,
                             path_count=96, arrow_count=144,
                             jump_cutoffs=72, selected_count_cutoffs=len(cutoffs),
                             first_target=ys[0], first_sources=sources(d, ys[0]),
                             witness_sha256=hashlib.sha256(
                                 json.dumps(witnesses, separators=(",", ":")).encode()).hexdigest()))
    return dict(rows=rows, paths=paths, odd_arrows=arrows,
                target_jump_checks=jumps, selected_count_checks=cuts)


def q_formula(A, X):
    Z, b, result = 3 * X + 1, 1, 0
    while Z // (2 * 4**b) >= 3:
        result += sum(y % 6 == 5 and 2 * 4**b * y <= Z for y in A)
        result += sum(y % 6 == 1 and 4 * 4**b * y <= Z for y in A)
        b += 1
    return result


def q_checks():
    sets = [[], [3], [5], [7], [7, 13, 19], list(range(3, 66, 2)),
            [target(1, 4, 5, j) for j in range(1, 13)]]
    records, count_checks, norm_checks = [], 0, 0
    for A in sets:
        direct = 0
        norms = {f"{p}/{q}": max((Fraction(j**q, y**p)
                                  for j, y in enumerate(A, 1)), default=Fraction(0))
                 for p, q in ((4, 5), (7, 8), (9, 10))}
        for X in range(1, 513):
            if X > 1 and X % 2 == 1:
                y, _ = step(1, X)
                direct += int(y in A and 2 * y <= X)
            need(q_formula(A, X) == direct, "one-arrow count identity failed")
            need(X >= 13 or direct == 0, "source below 13")
            count_checks += 1
            for p, q in ((4, 5), (7, 8), (9, 10)):
                Cq = norms[f"{p}/{q}"]
                if A:
                    need(Fraction(13**q * direct**q) < 10**q * Cq * X**p,
                         "finite one-arrow growth norm inequality failed")
                else:
                    need(direct == 0 and Cq == 0, "empty-set convention failed")
                norm_checks += 1
        records.append(dict(targets=A, source_cutoff=512, one_arrow_sources=direct,
                            finite_input_norm_power={k: str(v) for k, v in norms.items()}))
    return dict(rows=records, exact_count_checks=count_checks, norm_checks=norm_checks,
                scope="finite audit of written all-cutoff theorem")


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write-receipt", type=Path)
    return p


def rejection_checks():
    cases = {
        "unsupported d": lambda: target(3, 4, 5, 1),
        "negative d": lambda: target(-1, 4, 5, 1),
        "boolean d": lambda: target(True, 4, 5, 1),
        "zero alpha": lambda: target(1, 0, 5, 1),
        "alpha at one": lambda: target(1, 1, 1, 1),
        "nonreduced alpha": lambda: target(1, 2, 4, 1),
        "wrong target congruence": lambda: sources(1, 25),
        "target below family": lambda: sources(1, 5),
        "wrong exact valuation": lambda: verify_path(1, 61, (5,), 23),
        "wrong endpoint": lambda: verify_path(1, 61, (3,), 25),
        "valid arrow fails half descent": lambda: verify_path(61, 9, (3,), 11),
        "unrecognized word": lambda: verify_path(1, 61, (3, 3), 23),
        "absorber as source": lambda: verify_path(1, 1, (3,), 23),
        "invalid root degree": lambda: integer_root(1, 0),
    }
    for label, action in cases.items():
        try:
            action()
        except ValueError:
            continue
        raise ValueError(f"invalid case accepted: {label}")
    for flag in ("--unknown", "--max-steps"):
        with redirect_stderr(io.StringIO()):
            try:
                parser().parse_args([flag, "0"])
            except SystemExit as error:
                need(error.code != 0, "unknown flag unexpectedly succeeded")
            else:
                raise ValueError("unknown or cap flag accepted")
    return [*cases, "unknown CLI flag", "unimplemented cap CLI flag"]


def audit():
    return dict(schema="phase6-growth-norm-transport-v1", status="PASS",
                research_status="WRITTEN_PROOF_FOCUSED_AUDIT",
                candidate_batch="P6-003", node="S.2", proposed_label="barrier",
                constants=exact_constants(), families=family_checks(),
                one_arrow=q_checks(), rejections=rejection_checks(),
                scope=("One-arrow d1 contraction for 4/5<=alpha<1. Full first-half "
                       "arbitrary-target growth-norm contraction is refuted for each fixed "
                       "supported d and 0<alpha<=7/8. Actual bad-set-only estimates, other "
                       "weights, and finiteness of the full operator norm are not decided."))


def main():
    args = parser().parse_args()
    need(not sys.flags.optimize, "run without -O")
    result = audit()
    output = json.dumps(result, indent=2) + "\n"
    if args.write_receipt:
        args.write_receipt.write_text(output)
    else:
        need(result == json.loads(RECEIPT.read_text()), "growth-norm receipt mismatch")
    print(output, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
