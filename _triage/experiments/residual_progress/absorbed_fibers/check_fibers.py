"""Finite exact checks of the uniform known-fibre count and certificates."""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import fibers as F

HERE = Path(__file__).resolve().parent


def digest(values):
    return hashlib.sha256(json.dumps(values, sort_keys=True).encode()).hexdigest()


def lower_current(N, cap=1000):
    result = Counter()
    for seed in range(3, N+1, 2):
        x, seen = seed, set()
        while x != 1:
            assert x not in seen and len(seen) < cap
            seen.add(x)
            result[x] += 1
            x = F.NORMAL.step(x)
    assert F.NORMAL.divergence(result) == dict.fromkeys(range(3, N+1, 2), 1)
    return dict(result)


def run():
    count = 0
    for limit in range(4097):
        actual = sum(F.NORMAL.canonical(q) for q in range(1, limit+1, 2))
        assert actual == F.NORMAL.canonical_count(limit)
        A = (limit+1).bit_length()-1
        assert abs(4*actual-limit) <= 4*A+2
        count += 1
    small = []
    for N in range(8, 129, 8):
        for X in range(N, 8*N+1, max(1, N//8)):
            actual = [x for x in range(X, 2*X) if x % 2 and F.known(x, N)]
            number, terms = F.band_count(N, X)
            assert number == len(actual)
            assert F.independent_band(N, X) == actual
            telescope, canonical, corrections = F.telescope_count(N, X)
            assert telescope == number
            small.append((N, X, number))
    boundaries = []
    for N in (9, 15, 17, 31, 63, 127):
        for X in (N, N+1, 2*N-1, 2*N, 2*N+1, 17*N+1, N*2**65+3):
            number, _ = F.band_count(N, X)
            telescope, canonical, corrections = F.telescope_count(N, X)
            assert number == telescope == len(F.independent_band(N, X))
            boundaries.append(dict(N=N, X=str(X), count=number,
                                   canonical_count=canonical,
                                   corrections=[list(v) for v in corrections]))
    large = []
    for N in (96, 384, 6144):
        for multiplier in (1, 2, 3, 17, 2**64, 2**512):
            X = N*multiplier
            number, terms = F.band_count(N, X)
            exact = F.independent_band(N, X)
            assert number == len(exact)
            L = N.bit_length()-1
            telescope, canonical, corrections = F.telescope_count(N, X)
            assert telescope == number
            assert abs(4*number-N) <= 4*(2*L+3)
            assert len(terms) <= L+4
            large.append(dict(N=N, multiplier_bits=multiplier.bit_length(),
                              multiplier_small=multiplier if multiplier < 100 else None,
                              count=number, nonempty_levels=len(terms),
                              canonical_count=canonical,
                              telescope_corrections=[list(v) for v in corrections],
                              states_sha256=digest(exact)))
    examples = []
    N = 96
    lower = lower_current(N)
    for q in (1, 7, 9, 11, 27, 57, 89):
        assert q <= N and F.NORMAL.canonical(q)
        for partner in (False, True):
            base = 2*q+1 if partner else q
            for exponent in (0, 1, 5, 128):
                x = F.NORMAL.F_power(base, exponent)
                result = F.certify(x, N, lower)
                assert result["minimum"] == q
                assert result["bridge_rows"] <= 2*(N+1).bit_length()+4
                examples.append(dict(q=q, partner=partner, exponent=exponent,
                                     seed_bits=x.bit_length(),
                                     output_rows=len(result["current"]),
                                     new_rows=len(result["new_rows"]),
                                     current_sha256=digest(result["current"])))
    return dict(status="PASS", scope="Conditional elementary closure; orbit hitting remains open",
                canonical_cutoff_checks=count, small_band_checks=len(small),
                small_band_sha256=digest(small), large_bands=large,
                odd_cutoff_boundary_bands=boundaries,
                lower_input_cap=1000, lower_input_N=N,
                conditional_certificates=examples,
                uniform_written_bound="abs(B_N(X)-N/4)<=2*floor(log2 N)+3 for integer X>=N>=8",
                convergence_proved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = run()
    path = HERE/"fiber_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == result
    print(f"PASS: {result['small_band_checks']} small bands, "
          f"{len(result['large_bands'])} high bands, "
          f"{len(result['conditional_certificates'])} conditional currents")


if __name__ == "__main__":
    main()
