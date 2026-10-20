"""Exact bounded checks of root-collapse/transport obstructions.

No assertion of universal termination or Collatz convergence is made.
All transport loops have explicit finite caps. Run without -O.
"""

from argparse import ArgumentParser
from collections import defaultdict
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "experiments/annular_construction/arithmetic/check_arithmetic_reductions.py"
SPEC = importlib.util.spec_from_file_location("transport_arithmetic", SOURCE)
ARITH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ARITH)
P = ARITH.PACKETS.push
R = lambda measure: ARITH.root_collapse(measure)[1]


def rows(measure):
    return [[state, weight] for state, weight in sorted(measure.items())]


def collapsed_transport_current(measure, steps):
    """Return J, Z with measure=(I-P)J+Z and Z=R P**steps measure.

    `steps` is a caller-supplied cap, not a search for eventual absorption.
    Remaining positive coefficients are returned in full.
    """
    if not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a nonnegative integer")
    current = defaultdict(int)
    pushed = dict(measure)
    for _ in range(steps):
        for state, weight in pushed.items():
            current[state] += weight
        pushed = P(pushed)
    residual = R(pushed)
    for state, weight in ARITH.subtract(pushed, residual).items():
        current[state] += weight
    current = ARITH.clean(current)
    assert ARITH.subtract(measure, residual) == ARITH.subtract(current, P(current))
    return current, residual


def surviving_sources(cutoff, steps):
    """Top-band sources proved to stay positive through `steps` P/R rounds."""
    assert cutoff > 0 and cutoff % 8 == 0 and steps >= 0
    modulus = 9 * (1 << (steps + 2))
    first_index = (72 * cutoff + 1) // modulus + 1
    last_index = 144 * cutoff // modulus
    sources = [modulus * index - 1 for index in range(first_index, last_index + 1)]
    expected_count = (4 * cutoff // (1 << steps)
                      - 2 * cutoff // (1 << steps))
    assert len(sources) == expected_count
    return sources


def check_conjugacy():
    count = 0
    for state in range(3, 4098, 2):
        if ARITH.f_root(state) != state:
            continue
        successor = ARITH.PACKETS.step(state)
        assert successor > 1 and successor % 3 != 0
        inverse = ((2 * successor - 1) // 3 if successor % 3 == 2
                   else (4 * successor - 1) // 3)
        assert inverse == state
        assert P(R(P({state: 1}))) == P(P({state: 1}))
        count += 1
    for state in range(3, 4098, 2):
        if state % 3 == 0:
            continue
        root = ((2 * state - 1) // 3 if state % 3 == 2
                else (4 * state - 1) // 3)
        assert ARITH.f_root(root) == root
        assert ARITH.PACKETS.step(root) == state
    return count


def check_survivors(cutoff, depth_cap=12):
    original = ARITH.ANNULAR.annular_measure(cutoff)
    measure = original
    collapsed_iteration = R(original)
    profiles = []
    all_survivors = {depth: surviving_sources(cutoff, depth)
                     for depth in range(depth_cap + 1)}
    for depth in range(depth_cap + 1):
        collapsed = R(measure)
        assert collapsed_iteration == collapsed
        assert R(collapsed) == collapsed
        assert P(collapsed) == P(measure)
        assert ARITH.norm(collapsed) == ARITH.norm(P(measure))
        assert ARITH.positive_mass(collapsed) == ARITH.positive_mass(P(measure))
        for target_depth in range(depth, depth_cap + 1):
            for source in all_survivors[target_depth]:
                state = 3 ** depth * (source + 1) // (1 << depth) - 1
                assert state % 4 == 3
                assert measure.get(state, 0) == collapsed.get(state, 0) == 2
        profiles.append({
            "depth": depth,
            "forced_positive_atoms": len(all_survivors[depth]),
            "transport_norm": ARITH.norm(measure),
            "collapsed_norm": ARITH.norm(collapsed),
            "collapsed_positive_mass": ARITH.positive_mass(collapsed),
        })
        measure = P(measure)
        collapsed_iteration = R(P(collapsed_iteration))
    current, residual = collapsed_transport_current(original, depth_cap)
    assert residual == R(iterate(original, depth_cap))
    return {"N": cutoff, "depth_cap": depth_cap, "profiles": profiles,
            "capped_current_rows": len(current)}


def iterate(measure, steps):
    for _ in range(steps):
        measure = P(measure)
    return measure


def check_annular_counterexamples():
    measure = ARITH.ANNULAR.annular_measure(96)
    selected = {}
    for depth in range(81):
        if depth in (0, 1, 2, 3, 78, 79, 80):
            selected[depth] = dict(measure)
        if depth < 80:
            measure = P(measure)
    assert ARITH.norm(selected[2]) == 3533
    assert ARITH.norm(selected[3]) == 3124
    assert 22 * ARITH.norm(selected[3]) > 19 * ARITH.norm(selected[2])
    before = R(selected[78])
    after = R(selected[79])
    assert R(P(before)) == after
    assert ARITH.norm(before) == ARITH.norm(after) == 13
    assert ARITH.positive_mass(before) == ARITH.positive_mass(after) == 4
    assert ARITH.norm(selected[79]) == ARITH.norm(selected[80]) == 13
    return {
        "N": 96,
        "initial_norms": [ARITH.norm(selected[depth]) for depth in range(4)],
        "repeated_19_over_22_fails_from_depth": 2,
        "plateau_transport_depths": [79, 80],
        "plateau_norm": 13,
        "plateau_positive_mass": 4,
        "raw_before_rows": rows(selected[79]),
        "raw_after_rows": rows(selected[80]),
        "collapsed_before_depth": 78,
        "collapsed_after_depth": 79,
        "collapsed_before_rows": rows(before),
        "collapsed_after_rows": rows(after),
    }


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = {
        "status": "PASS",
        "claim_scope": "written operator identities and scoped counterexamples",
        "root_states_checked": check_conjugacy(),
        "survivor_cases": [check_survivors(cutoff) for cutoff in (8, 96, 168, 384)],
        "counterexamples": check_annular_counterexamples(),
        "universal_termination_proved": False,
        "unbounded_search_used": False,
    }
    path = Path(__file__).with_name("root_transport_audit.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt, "stored receipt differs"
    print(json.dumps({"status": receipt["status"],
                      "survivor_cutoffs": [8, 96, 168, 384],
                      "depth_cap": 12, "counterexample_cutoff": 96,
                      "counterexample_depth_cap": 80,
                      "universal_termination_proved": False}, indent=2))


if __name__ == "__main__":
    main()
