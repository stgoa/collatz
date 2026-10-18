#!/usr/bin/env python3
"""Independent finite checks of the S.1 proof arithmetic and exact constants."""
import argparse
from fractions import Fraction
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import comb
from pathlib import Path
import sys

import calibration as C

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
RECEIPT = HERE / "calibration_audit.json"
FROZEN_FILES = {
    "experiments/residual_progress/bridge_normal_form/normal_form.py":
        "5839bf55351711875ae80b95d34eb5ec9580d95a11c9fe1a87cca7c686a83567",
    "experiments/residual_progress/tripling_equivalence/tripling.py":
        "8e00a5badd6c9b3c13f948c7b91e91dedc33209a44c9cbc13fb2765c76a067fb",
}


def load(name, relative):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def need(condition, message):
    if not condition:
        raise ValueError(message)


def shortcut_word(d, n, k):
    """Independent numerator recurrence, with no use of constructor stepping."""
    x, code, p, A, B = n, 0, 0, 1, 0
    for i in range(k):
        bit = x % 2
        code += bit << i
        if bit:
            p += 1
            A *= 3
            B = 3 * B + 2**i
            x = (3 * x + d) // 2
        else:
            x //= 2
    need(2**k * x == A * n + d * B, "affine numerator identity failed")
    need(A == 3**p, "wrong parity multiplier")
    need(0 <= B <= 3**k - 2**k, "uniform affine intercept bound failed")
    return code, p, x, A, B


def parity_checks():
    rows, word_count, lift_count, count_checks = [], 0, 0, 0
    for d in (1, 5, 7, 13, 61, 97):
        for k in range(1, 13):
            modulus, period = 2**k, 2**(k - 1)
            codes, bad, transcript = set(), [], []
            threshold = 3 * k // 5
            for residue in range(1, modulus, 2):
                code, p, x, A, B = shortcut_word(d, residue, k)
                codes.add(code)
                transcript.append((residue, code, p, x, A, B))
                if p > threshold:
                    bad.append(residue)
                for lift in (1, 3):
                    lifted = shortcut_word(d, residue + lift * modulus, k)
                    need(lifted[0] == code and lifted[2] == x + lift * A,
                         "parity cylinder lift failed")
                    lift_count += 1
                word_count += 1
            need(codes == set(range(1, modulus, 2)), "odd parity-vector bijection failed")
            expected_bad = sum(comb(k - 1, j) for j in range(threshold, k))
            need(len(bad) == expected_bad, "exact binomial bad-residue count failed")
            for X in (0, 1, 2, modulus - 1, modulus, modulus + 1, 3 * modulus + 5):
                count = sum(max(0, (X - r) // modulus + 1) for r in bad)
                bound = Fraction(expected_bad, period) * ((X + 1) // 2) + expected_bad
                need(count <= bound, "moving-cutoff cylinder bound failed")
                # A second direct path count checks the progression convention.
                direct = sum(shortcut_word(d, n, k)[1] > threshold
                             for n in range(1, X + 1, 2))
                need(direct == count, "direct cutoff count differs from cylinders")
                count_checks += 1
            rows.append(dict(d=d, k=k, words=period, bad_residues=expected_bad,
                             transcript_sha256=hashlib.sha256(
                                 json.dumps(transcript, separators=(",", ":")).encode()).hexdigest()))
    return dict(rows=rows, words=word_count, lifted_words=lift_count,
                cutoff_comparisons=count_checks)


def tail_checks():
    for m in range(1, 201):
        k = 5 * m
        B = sum(comb(k - 1, j) for j in range(3 * m, k))
        delta = Fraction(B, 2**(k - 1))
        t = Fraction(4, 3)
        independent_mgf = t * ((1 + t) / 2)**(k - 1) / t**(3 * m)
        need(independent_mgf == C.mgf_bound(m), "mgf constant identity failed")
        need(delta <= independent_mgf, "exact tail exceeds mgf bound")
        need((Fraction(27, 32)**m < Fraction(1, 4)) == (m >= 9),
             "incorrect minimum contraction exponent")
    return dict(m_first=1, m_last=200,
                at_m8=Fraction(27, 32)**8, at_m9=Fraction(27, 32)**9)


def parameter_checks():
    rows, boundary_checks = [], 0
    for d in (1, 5, 7, 13, 61, 97):
        for epsilon in (Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)):
            plan = C.parameters(d, epsilon)
            m, k, Z, E = plan["m"], plan["shortcut_horizon"], plan["Z"], plan["E"]
            need(C.mgf_bound(m) <= epsilon / 2, "selected m insufficient")
            need(m == 9 or C.mgf_bound(m - 1) > epsilon / 2,
                 "selected m not minimal")
            need(C.mgf_bound(plan["proved_m_search_limit"]) <= epsilon / 2,
                 "finite termination bound failed")
            need(Fraction(4 * d * 3**k, 2**k) <= Z and
                 Z - 1 < Fraction(4 * d * 3**k, 2**k), "Z ceiling failed")
            need(Fraction(2 * E, 1) / epsilon <= plan["M0"] and
                 plan["M0"] - 1 < Fraction(2 * E, 1) / epsilon,
                 "M0 ceiling failed")
            for X in (plan["X0"], plan["X0"] + 1, plan["X0"] + 2,
                      3 * plan["X0"] + 17):
                need(C.failure_bound(plan, X) <= epsilon * ((X + 1) // 2),
                     "explicit final density bound failed")
                boundary_checks += 1
            # Select genuine good residues, then lift past the large Z cutoff.
            good_samples = []
            for residue in range(1, 128, 2):
                code, p, _, _, _ = shortcut_word(d, residue, k)
                if p > 3 * m:
                    continue
                lift = max(0, (Z - residue + 2**k - 1) // 2**k)
                n = residue + lift * 2**k
                word = shortcut_word(d, n, k)
                need(word[0] == code and word[2] * 2 < n,
                     "good cylinder does not achieve shortcut half-descent")
                witness = C.half_descent(d, n, k)
                need(witness["found"] and witness["time"] <= word[1],
                     "odd-clock half-descent conversion failed")
                good_samples.append(dict(seed=n, odd_steps_in_shortcut=p, witness=witness))
                if len(good_samples) == 3:
                    break
            need(len(good_samples) == 3, "finite good-cylinder witnesses missing")
            rows.append(dict(parameters=plan, lifted_good_samples=good_samples))
    return dict(examples=rows, cutoff_boundary_checks=boundary_checks)


def clock_checks():
    count, halfway_cases, absorber_cases = 0, 0, 0
    for d in (1, 5, 7, 13, 61, 97):
        for n in range(1, 128, 2):
            for k in range(1, 13):
                _, p, endpoint, _, _ = shortcut_word(d, n, k)
                raw = n
                hit_absorber = raw == 1
                for _ in range(p):
                    raw = C.raw_odd(d, raw)
                    hit_absorber |= raw == 1
                oddpart = endpoint // (endpoint & -endpoint)
                need(raw == oddpart, "raw shortcut-to-odd clock identity failed")
                count += 1
                if 2 * endpoint < n:
                    witness = C.half_descent(d, n, p)
                    need(witness["found"], "absorbed half-descent witness missing")
                    halfway_cases += 1
                    absorber_cases += int(hit_absorber)
    # Small exceptional states really can fail forever; density is not absorption.
    exceptions = []
    for d, n in ((1, 1), (5, 19), (7, 5), (13, 131), (61, 235)):
        result = C.half_descent(d, n, 100)
        need(not result["found"], "known cycle minimum unexpectedly half-descends")
        exceptions.append(dict(d=d, seed=n, horizon=100, result=result))
    return dict(raw_clock_identities=count, half_descent_conversions=halfway_cases,
                conversions_with_absorber_visit=absorber_cases, retained_exceptions=exceptions)


def w5_checks():
    for relative, expected in FROZEN_FILES.items():
        need(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected,
             f"frozen proof input changed: {relative}")
    N = load("phase6_frozen_normal", "experiments/residual_progress/bridge_normal_form/normal_form.py")
    P = load("phase6_frozen_tripling", "experiments/residual_progress/tripling_equivalence/tripling.py")
    images, count, semiconjugacy, threshold_checks = set(), 0, 0, 0
    for w in range(5, 8193, 8):
        q = P.critical_image(w)
        need(q in (3 * w, (3 * w - 1) // 2) and w < q <= 3 * w,
             "critical image bound failed")
        need(q not in images and P.critical_inverse(q) == w,
             "critical W5 map not injective")
        images.add(q)
        ordinary, quotient = q, q
        for j in range(46):
            need(N.normal_form(ordinary) == quotient <= ordinary,
                 "same-index semiconjugacy failed")
            semiconjugacy += 1
            if 2 * ordinary <= q:
                need(9 * quotient + 5 < 8 * q, "half-descent does not imply threshold")
                threshold_checks += 1
            ordinary = C.absorbed_odd(1, ordinary)
            quotient = N.normal_form(C.absorbed_odd(1, quotient))
        count += 1
    for X in range(5, 8193):
        M = (X + 3) // 8
        need(M == len(range(5, X + 1, 8)), "W5 count endpoint mismatch")
        need((3 * X + 1) // 2 <= 18 * M, "W5 counting ratio failed")
        if X >= 13:
            need((3 * X + 1) // 2 <= 15 * M, "sharper W5 ratio failed")
    examples = []
    for epsilon in (Fraction(1, 2), Fraction(1, 10), Fraction(1, 100)):
        plan = C.w5_parameters(epsilon)
        for X in (plan["X0"], plan["X0"] + 1, plan["X0"] + 7, 2 * plan["X0"]):
            need(3 * X >= plan["ordinary"]["X0"], "pullback cutoff too small")
            need(C.failure_bound(plan["ordinary"], 3 * X) <= epsilon * ((X + 3) // 8),
                 "explicit W5 relative bound failed")
        examples.append(plan)
    return dict(inputs=count, semiconjugacy_checks=semiconjugacy,
                threshold_checks=threshold_checks, cutoff_checks=8188,
                sharp_ratio_global=18, sharp_ratio_from_13=15,
                frozen_input_sha256=FROZEN_FILES, examples=examples)


def rejection_checks():
    cases = {
        "zero d": lambda: C.parameters(0, Fraction(1, 2)),
        "even d": lambda: C.parameters(2, Fraction(1, 2)),
        "ternary d": lambda: C.parameters(3, Fraction(1, 2)),
        "boolean d": lambda: C.parameters(True, Fraction(1, 2)),
        "zero epsilon": lambda: C.parameters(1, Fraction(0)),
        "epsilon above one": lambda: C.parameters(1, Fraction(3, 2)),
        "inexact epsilon": lambda: C.parameters(1, 0.5),
        "boolean epsilon": lambda: C.parameters(1, True),
        "capped parameter construction": lambda: C.parameters(1, Fraction(1, 100), max_m=8),
        "zero tail exponent": lambda: C.mgf_bound(0),
        "even odd seed": lambda: C.half_descent(1, 2, 10),
        "negative odd horizon": lambda: C.half_descent(1, 3, -1),
    }
    for label, action in cases.items():
        try:
            action()
        except ValueError:
            continue
        raise ValueError(f"invalid case accepted: {label}")
    need(not C.half_descent(1, 3, 0)["found"], "zero horizon should be an exact failure")
    return list(cases)


def audit():
    return C.json_exact(dict(
        schema="phase6-stopping-calibration-v1", status="PASS", node="S.1",
        proposed_label="calibration", parity=parity_checks(), tail=tail_checks(),
        parameters=parameter_checks(), clocks=clock_checks(), w5=w5_checks(),
        rejections=rejection_checks(),
        scope=("Finite arithmetic checks accompanying a written quantitative stopping theorem. "
               "Fixed-factor stopping transfers for each supported fixed d; no absorption theorem "
               "or removal of every exceptional seed is claimed.")))


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
        need(result == json.loads(RECEIPT.read_text()), "calibration receipt mismatch")
    print(text, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
