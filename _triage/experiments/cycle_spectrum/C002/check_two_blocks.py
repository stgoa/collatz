#!/usr/bin/env python3
"""Exact finite C002 checks for two growing repeated valuation blocks.

Default recomputes the complete declared grids and compares the saved receipt.
--write regenerates that receipt. All cycles use the RAW odd recurrence at1.
"""

import argparse
from collections import Counter
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

if sys.flags.optimize:
    raise SystemExit("FAIL: optimized Python disables verification assertions")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTUAL = HERE.parent / "C001/actual_cycles.json"
SCANNER = HERE.parent / "C001/scan_cycles.py"
FIXTURES = ROOT / "experiments/phase6/cycle_fixtures.json"
BASELINE = "14441c0864ba67e73d32b24dc67afb4cd832921e"
MAX_BLOCK_LENGTH = 3
MAX_VALUATION = 4
MAX_REPETITION = 8


def require(test, message):
    if not test:
        raise ValueError(message)


def stream_add(hasher, value):
    hasher.update(json.dumps(value, separators=(",", ":"), sort_keys=True).encode())
    hasher.update(b"\n")


def word_data(word):
    """Direct polynomial sum, independent of the two-block composition."""
    require(word and all(type(a) is int and a >= 1 for a in word), "invalid valuation word")
    c, prefix = 0, 0
    for i, a in enumerate(word):
        c += 3**(len(word) - 1 - i) * 2**prefix
        prefix += a
    return c, 2**prefix, 3**len(word), prefix, len(word)


def raw_step(n, d):
    require(n > 0 and n % 2 and d > 0 and gcd(d, 6) == 1, "invalid raw odd input")
    z = 3 * n + d
    valuation = (z & -z).bit_length() - 1
    return z >> valuation, valuation


def period_length(word):
    prefix = [0] * len(word)
    for i in range(1, len(word)):
        j = prefix[i - 1]
        while j and word[i] != word[j]:
            j = prefix[j - 1]
        if word[i] == word[j]:
            j += 1
        prefix[i] = j
    period = len(word) - prefix[-1]
    return period if len(word) % period == 0 else len(word)


def actual_realization(word, c, d):
    require(d > 0, "only positive rational words have positive realizations")
    g = gcd(c, d)
    parameter, n = d // g, c // g
    initial = n
    states = []
    for a in word:
        require(n > 0 and n % 2 and gcd(n, parameter) == 1, "state is not reduced positive odd")
        states.append(n)
        n, actual = raw_step(n, parameter)
        require(actual == a, "realization has the wrong exact valuation")
    require(n == initial, "word realization does not close")
    primitive_length = period_length(word)
    require(len(set(states)) == primitive_length, "state period disagrees with valuation period")
    return parameter, states, primitive_length


def geometric(q, p, k):
    require(type(k) is int and k >= 1 and q != p, "invalid repetition parameters")
    qk, pk = q**k, p**k
    require((qk - pk) % (q - p) == 0, "nonintegral geometric factor")
    return (qk - pk) // (q - p), qk, pk


def two_block(udata, vdata, k, ell):
    cu, q, p, au, mu = udata
    cv, s, r, av, mv = vdata
    gu, qk, pk = geometric(q, p, k)
    gv, sl, rl = geometric(s, r, ell)
    du, dv = q - p, s - r
    K = du * cv - dv * cu
    c = rl * cu * gu + qk * cv * gv
    d = sl * qk - rl * pk
    require(du * c - cu * d == qk * K * gv, "first elimination identity failed")
    require(dv * c - cv * d == -rl * K * gu, "second elimination identity failed")
    g = gcd(c, d)
    require(gcd(g, 6) == 1, "word gcd must be prime to6")
    common = gcd(gu, gv)
    if K:
        require((K * common) % g == 0, "shared-geometric-factor bound failed")
        require(common % (g // gcd(g, K)) == 0, "reduced cancellation divisor failed")
    else:
        require(du * cv == dv * cu and du * c == cu * d, "common fixed-point identity failed")
        if d > 0:
            require(du > 0 and dv > 0, "positive common fixed point needs contracting blocks")
    determinant = au * mv - av * mu
    relation = ("equal" if (au, mu) == (av, mv) else
                "proportional_unequal" if determinant == 0 else "multiplicatively_independent")
    direction = ("contracting" if du > 0 else "expanding") + "/" + (
        "contracting" if dv > 0 else "expanding")
    proportional = None
    if determinant == 0:
        rr = gcd(au, mu)
        aa, bb = au // rr, mu // rr
        require(av % aa == 0 and mv % bb == 0 and av // aa == mv // bb,
                "proportional exponent reduction failed")
        ss = av // aa
        U, V = 2**aa, 3**bb
        e, h = gcd(rr, ss), gcd(rr * k, ss * ell)
        He, Hh = U**e - V**e, U**h - V**h
        require(K % He == 0, "commutator missing common exponent factor")
        J = K // He
        J0 = abs(J) if J else None
        if J0 is not None:
            for prime in (2, 3):
                while J0 % prime == 0:
                    J0 //= prime
        if d > 0:
            require(U > V, "positive proportional word needs contracting common slope")
            if K:
                require((J0 * Hh) % g == 0, "prime-to-six proportional cancellation divisor failed")
                require((d // g) * J0 > U**(rr * k + ss * ell - h),
                        "strict proportional denominator lower bound failed")
        proportional = dict(a=aa, b=bb, r=rr, s=ss, e=e, h=h, J=J, J0=J0,
                            H_h=Hh, positive_bound_checked=d > 0 and K != 0)
    equal_total_checked = relation == "equal" and q > p and K != 0 and k + ell >= 3
    if equal_total_checked:
        require(cu * 2**mu <= q * (p - 2**mu)
                and cv * 2**mu <= q * (p - 2**mu), "uniform block coefficient bound failed")
        require(abs(cv - cu) * 2**mu < q * (p - 2**mu), "strict coefficient-difference bound failed")
        require((d // g) * p > 2**(au + mu) and d // g > 2**mu,
                "uniform same-total denominator bound failed")
    return dict(C=c, D=d, gcd=g, K=K, G_u=gu, G_v=gv,
                common_geometric_gcd=common, slope_relation=relation,
                exponent_determinant=determinant, block_directions=direction,
                denominator=abs(d) // g, both_repetitions_grow=k >= 2 and ell >= 2,
                proportional=proportional, equal_total_uniform_bound_checked=equal_total_checked)


def decompositions(segment):
    """Every exact power presentation, including exponent1 and nonprimitive bases."""
    result = []
    length = len(segment)
    for exponent in range(1, length + 1):
        if length % exponent == 0:
            base = tuple(segment[:length // exponent])
            if base * exponent == tuple(segment):
                result.append((base, exponent))
    return result


def count_case(counts, groups, row, k, ell):
    counts["decompositions"] += 1
    counts["both_repetitions_at_least2"] += int(k >= 2 and ell >= 2)
    counts["baseline_k1_ell1"] += int(k == ell == 1)
    counts["nonzero_K"] += int(row["K"] != 0)
    counts["zero_K"] += int(row["K"] == 0)
    counts["positive_D"] += int(row["D"] > 0)
    counts["negative_D"] += int(row["D"] < 0)
    counts["cancellation_exceeds_abs_K"] += int(row["K"] != 0 and row["gcd"] > abs(row["K"]))
    counts["proportional_positive_nonzero_K_bounds"] += int(
        row["proportional"] is not None and row["D"] > 0 and row["K"] != 0)
    counts["equal_total_uniform_bounds"] += int(row["equal_total_uniform_bound_checked"])
    group = "|".join((row["slope_relation"], row["block_directions"],
                      "positive_D" if row["D"] > 0 else "negative_D"))
    groups[group] += 1


def check_actual_source():
    source = json.loads(ACTUAL.read_text())
    require(source["schema"] == "C001-actual-raw-cycles-v1", "wrong actual-cycle schema")
    require(source["sources"]["scanner_sha256"] == sha256(SCANNER.read_bytes()).hexdigest(),
            "C001 scanner source hash mismatch")
    require(source["sources"]["fixture_sha256"] == sha256(FIXTURES.read_bytes()).hexdigest(),
            "historical fixture hash mismatch")
    rows = source["cycles"]
    require(len(rows) == 2459 and len({row["d"] for row in rows}) == 333,
            "C002 requires the complete pinned C001 actual-cycle dataset")
    counts, groups = Counter(), Counter()
    digest = sha256()
    examples, constant_bound_failures, fixtures_seen, seen = [], [], {}, set()
    total_arrows = 0
    for cycle in rows:
        d, states, word = cycle["d"], cycle["states"], tuple(cycle["word"])
        require(states[0] == min(states) and len(set(states)) == len(states),
                "source cycle is not canonical and simple")
        require((d, tuple(states)) not in seen, "duplicate source cycle")
        seen.add((d, tuple(states)))
        require(len(states) == len(word), "source cycle lengths disagree")
        for i, state in enumerate(states):
            require(raw_step(state, d) == (states[(i + 1) % len(states)], word[i]),
                    "actual source arrow or valuation failed")
            total_arrows += 1
        c, q, p, A, m = word_data(word)
        D, g = q - p, gcd(c, q - p)
        require(D > 0 and states[0] * D == d * c, "actual cycle equation failed")
        den = D // g
        require(d % den == 0 and cycle["actual_scaling"] == d // den,
                "source scaling does not match denominator")
        require((cycle["C"], cycle["D"], cycle["A"], cycle["m"],
                 cycle["gcd_C_D"], cycle["reduced_denominator"]) == (c, D, A, m, g, den),
                "source coefficient metadata mismatch")
        require(all(d // gcd(n, d) == den for n in states), "source denominator changed on rotation")
        for fixture_id in cycle["fixture_ids"]:
            require(fixture_id not in fixtures_seen, "fixture identifier duplicated")
            fixtures_seen[fixture_id] = (d, states, list(word))
        for cut in range(1, len(word)):
            for u, k in decompositions(word[:cut]):
                for v, ell in decompositions(word[cut:]):
                    require(u * k + v * ell == word, "actual decomposition does not reconstruct word")
                    row = two_block(word_data(u), word_data(v), k, ell)
                    require((row["C"], row["D"], row["gcd"], row["denominator"])
                            == (c, D, g, den), "actual decomposition coefficient mismatch")
                    require(row["K"] != 0, "a simple source cycle cannot have two common-fixed-point blocks")
                    count_case(counts, groups, row, k, ell)
                    stream_add(digest, [d, states[0], cut, list(u), k, list(v), ell, row])
                    if k >= 2 and ell >= 2 and len(examples) < 16:
                        examples.append(dict(d=d, minimum=states[0], cut=cut,
                                             u=list(u), k=k, v=list(v), ell=ell, **row))
                    if row["gcd"] > abs(row["K"]):
                        require(k >= 2 and ell >= 2, "one-growing-block bound was contradicted")
                        constant_bound_failures.append(dict(d=d, minimum=states[0], cut=cut,
                                                            u=list(u), k=k, v=list(v), ell=ell, **row))
    fixtures = json.loads(FIXTURES.read_text())["cycles"]
    require(len(fixtures_seen) == len(fixtures) == 11, "fixture coverage mismatch")
    for index, fixture in enumerate(fixtures, 1):
        require(fixtures_seen.get(f"phase6_fixture_{index:02d}")
                == (fixture["d"], fixture["states"], fixture["valuations"]),
                "historical fixture identity mismatch")
    require(counts["baseline_k1_ell1"] == sum(len(row["word"]) - 1 for row in rows),
            "not every canonical cut has its baseline decomposition")
    return dict(source_cycles=len(rows), source_d_count=333, exact_source_arrows=total_arrows,
                historical_fixtures_verified=11,
                orientation="minimum-state canonical word only; no all-rotation claim",
                enumeration="every cut; every divisor exponent of each side, including nonprimitive bases",
                counts=dict(sorted(counts.items())), groups=dict(sorted(groups.items())),
                decomposition_sha256=digest.hexdigest(), both_growing_examples=examples,
                constant_bound_counterexamples=constant_bound_failures)


def check_generated():
    bases = [tuple(word) for length in range(1, MAX_BLOCK_LENGTH + 1)
             for word in product(range(1, MAX_VALUATION + 1), repeat=length)]
    base_data = [word_data(word) for word in bases]
    counts, groups, denoms = Counter(), Counter(), set()
    digest = sha256()
    examples = {}
    for ui, u in enumerate(bases):
        for vi, v in enumerate(bases):
            for k in range(1, MAX_REPETITION + 1):
                for ell in range(1, MAX_REPETITION + 1):
                    row = two_block(base_data[ui], base_data[vi], k, ell)
                    word = u * k + v * ell
                    c, q, p, _, _ = word_data(word)
                    require((row["C"], row["D"]) == (c, q - p),
                            "generated composition disagrees with direct polynomial sum")
                    count_case(counts, groups, row, k, ell)
                    states, primitive_length = [], None
                    if row["D"] > 0:
                        parameter, states, primitive_length = actual_realization(word, c, row["D"])
                        require(parameter == row["denominator"], "generated denominator mismatch")
                        denoms.add(parameter)
                        counts["exact_odd_arrows"] += len(states)
                        counts["primitive_word_realizations"] += int(primitive_length == len(word))
                        counts["proper_power_word_realizations"] += int(primitive_length < len(word))
                        if row["K"] == 0:
                            cu, qu, pu, _, _ = base_data[ui]
                            require(parameter == (qu - pu) // gcd(cu, qu - pu),
                                    "common-fixed-point denominator was not preserved")
                            counts["positive_common_fixed_point_checks"] += 1
                        category = "|".join((row["slope_relation"], row["block_directions"]))
                        if category not in examples:
                            examples[category] = dict(u=list(u), v=list(v), k=k, ell=ell,
                                                      primitive_length=primitive_length,
                                                      states=states, **row)
                    stream_add(digest, [ui, vi, k, ell, row, primitive_length, states])
    expected = len(bases)**2 * MAX_REPETITION**2
    require(counts["decompositions"] == expected, "generated grid incomplete")
    return dict(bounds=dict(base_lengths=[1, MAX_BLOCK_LENGTH], valuations=[1, MAX_VALUATION],
                            k=[1, MAX_REPETITION], ell=[1, MAX_REPETITION],
                            contracting_block_restriction=False),
                base_word_count=len(bases), ordered_block_pairs=len(bases)**2,
                requested_cases=expected, completed_cases=expected, unresolved_cases=0,
                counts=dict(sorted(counts.items())), groups=dict(sorted(groups.items())),
                distinct_realized_parameters=len(denoms), smallest_parameter=min(denoms),
                largest_parameter=max(denoms), arithmetic_sha256=digest.hexdigest(),
                examples={key: examples[key] for key in sorted(examples)},
                scope="Positive word realizations may repeat primitive cycles; distinct parameters are counted exactly.")


def check_equal_slope_obstruction():
    u, v = (1, 1, 3), (1, 2, 2)
    digest, examples = sha256(), []
    arrows = 0
    for t in range(1, 129):
        row = two_block(word_data(u), word_data(v), t, t)
        G = (32**t - 27**t) // 5
        require(row["K"] == 20 and row["G_u"] == row["G_v"] == G,
                "equal-slope geometric control failed")
        require(row["gcd"] == G and row["denominator"] == 5 * (32**t + 27**t),
                "equal-slope exact cancellation/denominator formula failed")
        d, states, primitive_length = actual_realization(u * t + v * t, row["C"], row["D"])
        require(primitive_length == 6 * t and len(set(states)) == 6 * t,
                "equal-slope control must be primitive")
        arrows += len(states)
        if t >= 2:
            require(row["gcd"] > abs(row["K"]), "fixed-K bound should already fail at t2")
        stream_add(digest, [t, row, states])
        if t <= 3:
            examples.append(dict(t=t, states=states, parameter=d, **row))
    return dict(u=list(u), v=list(v), checked_equal_repetitions=[1, 128],
                exact_odd_arrows=arrows, examples=examples, arithmetic_sha256=digest.hexdigest(),
                scope="Exact finite checks of an unbounded-cancellation family; denominator still grows and is never1.")


def mechanical(m):
    A = (3**m).bit_length()
    return tuple(((i + 1) * A) // m - (i * A) // m for i in range(m))


def check_rotating_mechanical():
    lengths = list(range(13, 129)) + [256, 512]
    repetition_pairs = [(1, 2), (2, 1), (2, 2), (3, 5), (8, 8)]
    digest, examples, arrows = sha256(), [], 0
    for m in lengths:
        u = mechanical(m)
        v = u[1:] + u[:1]
        cu, q, p, A, _ = word_data(u)
        cv, _, _, _, _ = word_data(v)
        require(u[:3] == (1, 2, 1) and u[-3:] == (1, 2, 2), "mechanical end pattern failed")
        require(2 * cv == 3 * cu + q - p and cu != cv, "rotated block coefficient failed")
        for k, ell in repetition_pairs:
            word = u * k + v * ell
            row = two_block(word_data(u), word_data(v), k, ell)
            d, states, primitive_length = actual_realization(word, row["C"], row["D"])
            require(primitive_length == len(word), "rotating-mechanical word is not primitive")
            h = gcd(k, ell)
            require(2 * m * d > 3 * p**(k + ell - h - 1),
                    "rotating-mechanical denominator lower bound failed")
            require(d > 1 and 12 * min(states) > m * d,
                    "rotating-mechanical positivity/nonintegrality/height failed")
            cyclic = word + word[:2]
            pairs11 = sum(cyclic[i:i + 2] == (1, 1) for i in range(len(word)))
            triples222 = sum(cyclic[i:i + 3] == (2, 2, 2) for i in range(len(word)))
            require(pairs11 == triples222 == 1, "the two boundary defects are not unique")
            odd_minima = sum(states[i] < states[i - 1] and states[i] < states[(i + 1) % len(states)]
                             for i in range(len(states)))
            shortcut_minima = sum(a >= 2 for a in word)
            require(odd_minima == (k + ell) * (2 * m - A) - 1,
                    "rotating-mechanical odd-only minimum count failed")
            require(shortcut_minima == (k + ell) * (A - m),
                    "rotating-mechanical shortcut minimum count failed")
            arrows += len(states)
            summary = dict(m=m, A=A, k=k, ell=ell, odd_arrows=len(states),
                           denominator_bits=d.bit_length(), cancellation_bits=row["gcd"].bit_length(),
                           minimum_numerator=min(states), denominator=d,
                           odd_only_minima=odd_minima, shortcut_minima=shortcut_minima)
            stream_add(digest, [summary, row])
            if m == 13 or m in (256, 512) and (k, ell) == (1, 2):
                examples.append(summary)
    return dict(lengths=lengths, repetition_pairs=[list(pair) for pair in repetition_pairs],
                completed_cases=len(lengths) * len(repetition_pairs), exact_odd_arrows=arrows,
                extra_exponent_separation_condition=False, arithmetic_sha256=digest.hexdigest(),
                examples=examples,
                scope="Exact finite primitive cycle realizations, height and two clock-specific minima counts; the all-m theorem is separate.")


def report():
    return dict(schema="C002-two-growing-blocks-v1", status="PASS",
                clock="Raw positive odd 3x+d; no absorption convention at1",
                baseline_commit=BASELINE,
                scope="Finite exact identities and positive integer-cycle realizations; no exhaustive cycle spectrum or convergence claim.",
                limits="Finite algebraic grids only; no unbounded trajectory search and no capped cases are represented as successes.",
                source_sha256={"check_two_blocks.py": sha256(Path(__file__).read_bytes()).hexdigest(),
                               "C001/actual_cycles.json": sha256(ACTUAL.read_bytes()).hexdigest(),
                               "C001/scan_cycles.py": sha256(SCANNER.read_bytes()).hexdigest(),
                               "phase6/cycle_fixtures.json": sha256(FIXTURES.read_bytes()).hexdigest()},
                actual_cycles=check_actual_source(), generated_words=check_generated(),
                equal_slope_control=check_equal_slope_obstruction(),
                rotating_mechanical=check_rotating_mechanical())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--receipt", type=Path, default=HERE / "two_blocks_audit.json")
    args = parser.parse_args()
    try:
        actual = json.loads(json.dumps(report()))
        if args.write:
            args.receipt.write_text(json.dumps(actual, indent=2, sort_keys=True) + "\n")
        else:
            require(actual == json.loads(args.receipt.read_text()), "saved receipt mismatch")
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(json.dumps(dict(status="PASS", actual_decompositions=actual["actual_cycles"]["counts"],
                          generated_counts=actual["generated_words"]["counts"],
                          generated_parameters=actual["generated_words"]["distinct_realized_parameters"]),
                     sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
