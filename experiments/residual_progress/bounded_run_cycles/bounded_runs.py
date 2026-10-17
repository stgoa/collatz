"""Arbitrarily long growing run returns with only two fixed run labels.

All loops have a supplied finite repeat count. No absorption search is used.
"""

from collections import Counter
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = importlib.util.spec_from_file_location(name, HERE.parent / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


NORMAL = _load("bounded_run_normal", "bridge_normal_form/normal_form.py")
RUN = _load("bounded_run_return", "complementary_bridge/run_bridge.py")
WORD = (1, 2, 1, 1, 1, 1, 2, 2)
PHASE_SEED = 27
SLOPE_NUMERATOR = 6561
SLOPE_DENOMINATOR = 2048
OFFSET = 9221
FIXED_DENOMINATOR = 4513


def cylinder(repeats):
    if not isinstance(repeats, int) or repeats < 1:
        raise ValueError("Expected a positive repeat count")
    bits = 11 * repeats + 6
    modulus = 1 << bits
    residue = (-OFFSET * pow(FIXED_DENOMINATOR, -1, modulus)) % modulus
    assert residue % (1 << 17) == PHASE_SEED
    return residue, modulus


def cycle_return(x):
    numerator = SLOPE_NUMERATOR * x + OFFSET
    assert numerator % SLOPE_DENOMINATOR == 0
    return numerator // SLOPE_DENOMINATOR


def ray_root(repeats, extra_scale=0):
    """An actual weight1 complementary root on N=12*2^b, b>=9."""
    if not isinstance(extra_scale, int) or extra_scale < 0:
        raise ValueError("Expected a nonnegative scale increment")
    residue, modulus = cylinder(repeats)
    bits = modulus.bit_length() - 1
    N = 12 * (1 << (bits + extra_scale))
    period = 3 * modulus
    first = residue + modulus * ((-residue * pow(modulus, -1, 3)) % 3)
    x = first + period * ((N - first) // period + 1)
    assert N < x <= N + period < 3*N//2
    assert x % 12 == 3
    return N, x


def witness(x, repeats):
    residue, modulus = cylinder(repeats)
    if x <= 0 or x % modulus != residue:
        raise ValueError("Seed does not satisfy the sufficient cylinder")
    states = [x]
    block_returns = [x]
    cycle_starts = [x]
    current = Counter()
    labels = []
    for cycle in range(repeats):
        start = states[-1]
        assert start % (1 << 17) == PHASE_SEED
        for j, valuation in enumerate(WORD):
            q = states[-1]
            z = 3*q+1
            assert NORMAL.valuation2(z) == valuation
            current[q] += 1
            y = z >> valuation
            assert NORMAL.canonical(y)
            assert y > start
            assert NORMAL.quotient_step(q) == y
            states.append(y)
            if j in (1, 7):
                origin = block_returns[-1]
                a, _, d, _ = RUN.parameters(origin)
                expected = (2, 2) if j == 1 else (5, 4)
                assert (a, d) == expected
                assert RUN.normal_target(origin) == y
                assert y > origin
                labels.append((a, d))
                block_returns.append(y)
        assert states[-1] == cycle_return(start)
        assert (FIXED_DENOMINATOR*states[-1]+OFFSET)*SLOPE_DENOMINATOR == (
            SLOPE_NUMERATOR*(FIXED_DENOMINATOR*start+OFFSET))
        cycle_starts.append(states[-1])
    endpoint = states[-1]
    assert endpoint % 64 == PHASE_SEED
    assert NORMAL.divergence(current) == {x: 1, endpoint: -1}
    return dict(seed=x, endpoint=endpoint, states=states, labels=labels,
                block_returns=block_returns, cycle_starts=cycle_starts,
                current=dict(sorted(current.items())))
