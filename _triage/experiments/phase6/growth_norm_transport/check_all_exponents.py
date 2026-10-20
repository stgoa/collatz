#!/usr/bin/env python3
"""Exact finite-prefix-code audit for the all-alpha transport barrier."""
import argparse
from collections import defaultdict
from contextlib import redirect_stderr
from fractions import Fraction
import hashlib
import io
import json
from math import comb, gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "all_exponents_audit.json"


def need(condition, message):
    if not condition:
        raise ValueError(message)


def natural(x, name, lower=0):
    need(type(x) is int and x >= lower, f"invalid {name}")


def supported(d):
    natural(d, "d", 1)
    need(gcd(d, 6) == 1, "unsupported d")


def exponent(p, q):
    natural(p, "alpha numerator", 1)
    natural(q, "alpha denominator", 1)
    need(p < q and gcd(p, q) == 1, "alpha must be reduced and in (0,1)")


def raw_step(d, n):
    supported(d)
    natural(n, "odd state", 1)
    need(n % 2 == 1, "state must be odd")
    value = 3 * n + d
    divisor = value & -value
    return value // divisor, divisor.bit_length() - 1


def first_crossing_record(word):
    need(type(word) is tuple and bool(word), "empty or malformed word")
    A, b = 0, 0
    for j, a in enumerate(word, 1):
        natural(a, "valuation", 1)
        b = 3 * b + 2**A
        A += a
        if j < len(word):
            need(2**A < 2 * 3**j, "word has an earlier homogeneous half crossing")
    k = len(word)
    need(2**A > 2 * 3**k, "word does not cross homogeneous half")
    need(b % 2 == 1 and b % 3 != 0, "affine coefficient arithmetic failed")
    return k, A, b


def code_cells(B):
    """Count all first-crossing words of total valuation at most B."""
    natural(B, "total valuation budget", 1)
    live = {(0, 0): 1}
    crossed = defaultdict(int)
    for k in range(B):
        states = [(A, count) for (j, A), count in live.items() if j == k]
        for A, count in states:
            need(k == 0 or 2**A < 2 * 3**k, "nonlive state in DP")
            for a in range(1, B - A + 1):
                total = A + a
                key = (k + 1, total)
                if 2**total > 2 * 3**(k + 1):
                    crossed[key] += count
                else:
                    need(2**total < 2 * 3**(k + 1), "unexpected equality")
                    live[key] = live.get(key, 0) + count
    cells = [(k, A, count) for (k, A), count in sorted(crossed.items())]
    numerator = sum(count * 2**(B - A) for k, A, count in cells)
    need(0 <= numerator <= 2**B, "Kraft mass exceeds one")
    return cells, numerator


def brute_words(B):
    natural(B, "brute total valuation budget", 1)
    words = []

    def visit(prefix, A):
        k = len(prefix)
        for a in range(1, B - A + 1):
            word, total = prefix + (a,), A + a
            if 2**total > 2 * 3**(k + 1):
                first_crossing_record(word)
                words.append(word)
            else:
                visit(word, total)

    visit((), 0)
    need(len(set(words)) == len(words), "duplicate code word")
    for word in words:
        need(all(word[:j] not in words for j in range(1, len(word))),
             "code is not prefix-free")
    return words


def certify_mass(p, q, B):
    exponent(p, q)
    cells, numerator = code_cells(B)
    denominator = 2**B
    lhs = 2**(q - p) * numerator**q
    rhs = denominator**q
    need(lhs > rhs, "finite code mass is insufficient for this exponent")
    by_length = defaultdict(lambda: [0, 0])
    for k, A, count in cells:
        by_length[k][0] += count
        by_length[k][1] += count * 2**(B - A)
    mass = Fraction(numerator, denominator)
    return dict(alpha=f"{p}/{q}", total_valuation_budget=B,
                max_word_length=max(k for k, A, count in cells),
                cell_count=len(cells), word_count=sum(c for k, A, c in cells),
                mass_numerator=mass.numerator, mass_denominator=mass.denominator,
                common_denominator=denominator, common_numerator=numerator,
                exact_threshold=f"2^{q-p} * numerator^{q} > denominator^{q}",
                strict_integer_gap=lhs-rhs,
                length_rows=[dict(length=k, word_count=v[0], common_numerator=v[1])
                             for k, v in sorted(by_length.items())],
                cells_sha256=hashlib.sha256(
                    json.dumps(cells, separators=(",", ":")).encode()).hexdigest())


def small_code_checks():
    rows, total_words, cylinder_seeds = [], 0, 0
    for B in range(3, 11):
        words = brute_words(B)
        brute_cells = defaultdict(int)
        for word in words:
            brute_cells[len(word), sum(word)] += 1
        cells, N = code_cells(B)
        need(cells == [(k, A, count) for (k, A), count in sorted(brute_cells.items())],
             "compressed DP disagrees with word enumeration")
        need(N == sum(2**(B-sum(word)) for word in words), "Kraft count mismatch")
        total_words += len(words)
        rows.append(dict(B=B, words=len(words), numerator=N, denominator=2**B))
    for B in (3, 6, 9):
        words = set(brute_words(B))
        _, N = code_cells(B)
        for d in (1, 5, 61):
            found = 0
            for seed in range(1, 2**(B+1), 2):
                n, A, word = seed, 0, ()
                while A <= B:
                    n, a = raw_step(d, n)
                    A += a
                    word += (a,)
                    if A > B:
                        break
                    if 2**A > 2 * 3**len(word):
                        need(word in words, "integer cylinder word absent from code")
                        found += 1
                        break
                cylinder_seeds += 1
            need(found == N, "odd residue cylinder probability mismatch")
    return dict(rows=rows, enumerated_words=total_words,
                odd_residue_seeds=cylinder_seeds,
                modulus_convention="word total A uses modulus 2^(A+1), conditioned on odd source",
                encoding="raw S_d; no absorber modification of finite parity cylinders")


def inverse_word(d, word):
    supported(d)
    k, A, b = first_crossing_record(word)
    modulus3 = 3**k
    r = d * b * pow(2**A, -1, modulus3) % modulus3
    if r % 2 == 0:
        r += modulus3
    modulus = 2 * modulus3
    margin_denominator = 2**A - 2 * modulus3
    lower = max(3, d*b // margin_denominator + 1)
    y = r + modulus * max(0, (lower-r+modulus-1)//modulus)
    need(y >= lower and y % 2 == 1, "target representative failed")
    numerator = 2**A * y - d*b
    need(numerator % modulus3 == 0, "inverse residue failed")
    n = numerator // modulus3
    need(n > 2*y > 1 and n % 2 == 1, "inverse positivity or half margin failed")
    x, path = n, [n]
    for j, a in enumerate(word, 1):
        x, actual = raw_step(d, x)
        need(actual == a and x > 1, "wrong exact inverse valuation or absorber encountered")
        path.append(x)
        if j < k:
            need(2*x > n, "earlier actual half descent")
    need(x == y and 2*y < n, "incorrect final first-half endpoint")
    source_modulus = 2**(A+1)
    source_residue = (2**A-d*b) * pow(modulus3, -1, source_modulus) % source_modulus
    need(source_residue % 2 == 1 and n % source_modulus == source_residue,
         "extra-bit source cylinder failed")
    return dict(word=list(word), k=k, A=A, affine_b=b, d=d,
                target_modulus=modulus, target_residue=r, target=y, source=n,
                source_modulus=source_modulus, source_residue=source_residue,
                path=path)


def inverse_checks():
    words = brute_words(9)
    K = max(map(len, words))
    M = 2 * 3**K
    rows, samples, compatibility_tests = [], [], 0
    for d in (1, 5, 7, 13, 61):
        for word in words:
            row = inverse_word(d, word)
            count = sum(y % row["target_modulus"] == row["target_residue"]
                        for y in range(1, M, 2))
            need(count == 3**(K-row["k"]), "residue averaging multiplicity failed")
            compatibility_tests += 1
            rows.append(row)
            if word in ((3,), (1, 4), (2, 2)):
                samples.append(row)
    return dict(total_valuation_budget=9, max_length=K, words=len(words),
                exact_paths=len(rows), residue_compatibility_checks=compatibility_tests,
                common_target_modulus=M, samples=samples,
                all_paths_sha256=hashlib.sha256(
                    json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest())


def parity_feed_checks():
    rows = []
    for p, q, m, L in ((19, 20, 40, 12), (99, 100, 64, 12)):
        t, B = 5*m, 5*m+L-1
        bad = sum(comb(t-1, j) for j in range(3*m, t))
        exact_bad = Fraction(bad, 2**(t-1))
        mgf = Fraction(8, 7) * Fraction(16807, 18432)**m
        need(exact_bad <= mgf, "S.1 exact parity tail exceeds proved bound")
        need(4*3**(3*m) < 2**(5*m), "good-prefix quarter slope failed")
        lower = 1-mgf-Fraction(1, 2**L)
        need(lower > 0 and 2**(q-p)*lower.numerator**q > lower.denominator**q,
             "finite parity-feed mass does not exceed exponent threshold")
        rows.append(dict(alpha=f"{p}/{q}", m=m, parity_horizon=t, tail_window=L,
                         total_valuation_budget=B,
                         mgf_numerator=mgf.numerator, mgf_denominator=mgf.denominator,
                         mass_lower_numerator=lower.numerator,
                         mass_lower_denominator=lower.denominator,
                         exact_tail_bounded=True, strict_exponent_threshold=True))
    return rows


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--write-receipt", type=Path)
    return p


def rejection_checks():
    cases = {
        "empty word": lambda: first_crossing_record(()),
        "zero valuation": lambda: first_crossing_record((0,)),
        "boolean valuation": lambda: first_crossing_record((True,)),
        "noncrossing word": lambda: first_crossing_record((1,)),
        "earlier crossing": lambda: first_crossing_record((3, 1)),
        "unsupported d": lambda: inverse_word(3, (3,)),
        "negative d": lambda: inverse_word(-1, (3,)),
        "zero budget": lambda: code_cells(0),
        "alpha at one": lambda: certify_mass(1, 1, 48),
        "nonreduced alpha": lambda: certify_mass(38, 40, 48),
        "insufficient finite code": lambda: certify_mass(19, 20, 16),
    }
    for label, action in cases.items():
        try:
            action()
        except ValueError:
            continue
        raise ValueError(f"invalid case accepted: {label}")
    for flag in ("--unknown", "--max-words"):
        with redirect_stderr(io.StringIO()):
            try:
                parser().parse_args([flag, "0"])
            except SystemExit as error:
                need(error.code != 0, "unknown flag unexpectedly succeeded")
            else:
                raise ValueError("unknown truncation flag accepted")
    return [*cases, "unknown CLI flag", "unimplemented word-cap CLI flag"]


def audit():
    return dict(schema="phase6-all-exponents-transport-v1", status="PASS",
                research_status="WRITTEN_PROOF_FOCUSED_AUDIT",
                node="S.2", proposed_label="barrier",
                code_certificates=[certify_mass(19, 20, 48), certify_mass(99, 100, 80)],
                independent_small_code_checks=small_code_checks(),
                inverse_word_checks=inverse_checks(), parity_feed=parity_feed_checks(),
                rejections=rejection_checks(),
                scope=("Exact finite formal cylinder masses and inverse-word identities. "
                       "Residue-average existence does not provide an efficient winning-residue "
                       "constructor. No actual-orbit stochasticity, convergence, full-operator "
                       "norm finiteness, or actual-bad-set-only transport estimate is asserted."))


def main():
    args = parser().parse_args()
    need(not sys.flags.optimize, "run without -O")
    result = audit()
    output = json.dumps(result, indent=2) + "\n"
    if args.write_receipt:
        args.write_receipt.write_text(output)
    else:
        need(result == json.loads(RECEIPT.read_text()), "all-exponents receipt mismatch")
    print(output, end="")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
