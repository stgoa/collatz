"""Exact finite checks for sparse current criteria, led by the five-ray theorem.

This script does NOT construct currents at the infinite families of cutoffs.
The universal conditional arguments are given in the accompanying research
report; this file checks their numerical constants, finite base and arithmetic.
Run without Python optimization, because checks use assertions.
"""

from fractions import Fraction as F
import json
from pathlib import Path


MANTISSAS = [
    8192, 8467, 8751, 9045, 9348, 9662, 9986, 10321, 10668,
    11026, 11396, 11778, 12173, 12582, 13004, 13440, 13891,
    14358, 14839, 15337, 15852,
]
FIVE_MANTISSAS = [12, 14, 16, 18, 21]


def next_grid_cutoff(N):
    """Least member >=N in {a*2**b: a in MANTISSAS, b>=3}."""
    assert N >= 65536
    exponent = N.bit_length() - 1 - 13
    scale = 1 << exponent
    for a in MANTISSAS:
        if a * scale >= N:
            return a * scale
    return 2 * MANTISSAS[0] * scale


def syracuse(x):
    assert x > 0 and x % 2 == 1
    if x == 1:
        return 1
    value = 3 * x + 1
    return value // (value & -value)


def source(N):
    n1, n2 = (3 * N + 1) // 2, (3 * N + 1) // 4
    return {
        x: 3 * int(x % 3 == 2) - 1
        + (3 * int(x % 3 == 1) - 1 if x <= n2 else 0)
        for x in range(3, n1 + 1, 2)
    }


def main():
    base_times = {}
    for seed in range(1, 65536, 2):
        value = seed
        seen = set()
        for steps in range(10001):
            if value == 1:
                base_times[seed] = steps
                break
            assert value not in seen, (seed, value, "cycle")
            seen.add(value)
            value = syracuse(value)
        else:
            raise AssertionError((seed, "10000-step cap reached"))

    # Stronger main result: a phase-dependent comparison on five rays.
    five_edges = []
    for i, a in enumerate(FIVE_MANTISSAS):
        quotient, j = divmod(i + 3, 5)
        successor = FIVE_MANTISSAS[j] * 2**quotient
        assert 3 * a <= 2 * successor
        # Cubes of f(a_i*2**b)=2**((5*b+i)/3): successor/current = 2.
        assert 5 * quotient + j - i == 3
        five_edges.append({
            "from_mantissa": a,
            "to_mantissa": FIVE_MANTISSAS[j],
            "dyadic_shift": quotient,
        })
    assert 2**5 > 3**3  # 2**(-5/3) < 1/3.
    assert 2**10 > 10**3  # 2**(-10/3) < 1/10.
    assert F(1, 10) + F(2, 3) * (1 + F(1, 3)) == F(89, 90) < 1
    ladder_bases = [a * 2**r for a in FIVE_MANTISSAS for r in range(3, 9)]
    assert len(ladder_bases) == len(set(ladder_bases)) == 30
    assert max(ladder_bases) == 5376
    base_endpoint_limit = 9 * max(ladder_bases) // 4
    assert base_endpoint_limit == 12096
    assert all(x in base_times for x in range(1, base_endpoint_limit, 2))

    # Earlier 21-ray comparison, retained as an independently useful check.
    alpha = F(10337, 10000)
    gaps_21 = [F(b, a) for a, b in zip(MANTISSAS, MANTISSAS[1:] + [16384])]
    assert len(MANTISSAS) == 21 and len(set(MANTISSAS)) == 21
    assert max(gaps_21) == F(10668, 10321) < alpha
    arguments_21 = [alpha / 4, 3 * alpha / 2, 3 * alpha / 4]
    root_bounds_21 = [F(5821, 10000), F(11918, 10000), F(9032, 10000)]
    for argument, upper in zip(arguments_21, root_bounds_21):
        assert argument**2 < upper**5
    q_upper_21 = sum(
        x * upper / (1 if i == 0 else 3)
        for i, (x, upper) in enumerate(zip(arguments_21, root_bounds_21))
    )
    assert q_upper_21 == F(399928193, 400000000) < 1
    grid_probes = {65536, 65537}
    for exponent in range(3, 65):
        for mantissa in MANTISSAS:
            M = mantissa * 2**exponent
            grid_probes.update((M - 1, M, M + 1))
    grid_probes.discard(65535)
    for N in grid_probes:
        M = next_grid_cutoff(N)
        assert N <= M <= alpha * N
        assert M % 8 == 0
        assert (3 * M + 1) // 2 == 3 * M // 2
        assert (3 * M + 1) // 4 == 3 * M // 4
        assert (M - 1) // 4 == M // 4 - 1

    # Simpler 30-ray comparison: p=4/3 and mesh ratio delta=31/30.
    # q = (31/120)^(4/3) + (31/20)^(4/3)/3 + (31/40)^(4/3)/3.
    arguments = [F(31, 120), F(31, 20), F(31, 40)]
    cube_root_upper = [F(6369, 10000), F(11573, 10000), F(9186, 10000)]
    for x, upper in zip(arguments, cube_root_upper):
        assert x < upper**3
    q_upper = sum(
        x * upper / (1 if i == 0 else 3)
        for i, (x, upper) in enumerate(zip(arguments, cube_root_upper))
    )
    assert q_upper == F(1199731, 1200000) < 1

    # Each dyadic block has m=30,...,59, then the next starts at m=60.
    # The largest adjacent quotient is 31/30; this checks the full
    # finite list of ratios which repeats in every block.
    ratios = [F(m + 1, m) for m in range(30, 60)]
    assert max(ratios) == F(31, 30)
    grid = sorted(m * 2**b for b in range(2, 16) for m in range(30, 60))
    for M in grid:
        assert M % 4 == 0
        assert (3 * M + 1) // 2 == 3 * M // 2
        assert (3 * M + 1) // 4 == 3 * M // 4
        assert (M - 1) // 4 == M // 4 - 1

    # Adjacent pairs at N=4k+2 isolate precisely one odd multiple of 3.
    pair_checks = 0
    for N in range(10, 1003, 4):
        current, previous = source(N), source(N - 1)
        difference = {
            x: current.get(x, 0) - previous.get(x, 0)
            for x in current.keys() | previous.keys()
            if current.get(x, 0) != previous.get(x, 0)
        }
        assert difference == {3 * N // 2: -1}
        pair_checks += 1

    # Verify the elementary modular order and inverse lift for bounded d,y.
    inverse_checks = 0
    for d in range(1, 6):
        modulus = 3 ** (d + 1)
        order = 2 * 3**d
        powers = {pow(2, a, modulus): a for a in range(1, order + 1)}
        assert len(powers) == order
        assert all(r % 3 for r in powers)
        for y in range(1, 1000, 2):
            if y % 3 == 0:
                continue
            exponent = powers[pow(y, -1, modulus)]
            x = ((1 << exponent) * y - 1) // 3
            assert x > 0 and x % 2 == 1 and x % (3**d) == 0
            assert syracuse(x) == y
            inverse_checks += 1

    result = {
        "status": "PASS",
        "five_ray_criterion": {
            "mantissas": FIVE_MANTISSAS,
            "exponents": "all integers b>=3 (conditional theorem)",
            "comparison": "f(a_i*2^b)=2^((5b+i)/3), i=0,...,4",
            "comparison_growth_exponent": "5/3",
            "strict_contraction_upper": "89/90",
            "finite_base_odd_seeds": [1, 95],
            "base_max_syracuse_time": max(t for x, t in base_times.items() if x < 96),
            "successor_edges": five_edges,
            "base64_ladders": {
                "count": len(ladder_bases),
                "initial_cutoffs": sorted(ladder_bases),
                "largest_initial_cutoff": max(ladder_bases),
                "all_initial_packet_endpoints_below": base_endpoint_limit,
                "odd_endpoint_seeds_verified": base_endpoint_limit // 2,
                "max_endpoint_syracuse_time": max(t for x, t in base_times.items() if x < base_endpoint_limit),
                "exact_base_currents_exist_by_finite_absorption": True,
                "full_current_tables_stored": False,
            },
        },
        "twenty_one_ray_criterion": {
            "mantissas": MANTISSAS, "exponents": "all integers b>=3 (conditional theorem)",
            "finite_base_odd_seeds": [1, 65535],
            "base_max_syracuse_time": max(base_times.values()),
            "base_maximizers": [x for x, t in base_times.items() if t == max(base_times.values())],
            "mesh_ratio_upper": str(alpha), "maximum_actual_mesh_ratio": str(max(gaps_21)),
            "comparison_power": "7/5", "strict_contraction_upper": str(q_upper_21),
            "finite_grid_exponents_checked": [3, 64], "grid_probes_checked": len(grid_probes),
        },
        "thirty_ray_criterion": {
            "mantissas": [30, 59], "exponents": "all integers b>=2 (conditional theorem)",
            "finite_base_odd_seeds": [1, 119],
            "base_max_syracuse_time": max(t for x, t in base_times.items() if x < 120),
            "mesh_ratio": "31/30", "comparison_power": "4/3",
            "strict_contraction_upper": str(q_upper),
            "finite_grid_exponents_checked": [2, 15],
        },
        "paired_exact_criterion": {
            "source_differences_checked": pair_checks,
            "N_checked": {"first": 10, "last": 1002, "step": 4},
            "inverse_lifts_checked": inverse_checks,
            "inverse_parameters": {"d": [1, 5], "odd_y": [1, 999], "exclude_multiples_of_3": True},
        },
        "universal_current_existence_proved": False,
    }
    serialized = json.dumps(result, indent=2) + "\n"
    Path(__file__).with_name("sparse_criteria_audit.json").write_text(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
