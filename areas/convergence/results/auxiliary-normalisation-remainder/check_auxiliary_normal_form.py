"""Terminating partial normalization by exact auxiliary predecessor chains.

The terminal positive mass is returned. This does not construct a complete
annular certificate. Run without Python optimization.
"""

from argparse import ArgumentParser
from collections import defaultdict
import heapq
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SPEC = importlib.util.spec_from_file_location(
    "auxiliary_arithmetic",
    ROOT / "experiments/annular_construction/arithmetic/check_arithmetic_reductions.py")
ARITH = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ARITH)
P = ARITH.PACKETS.push

# (lower/N, upper/N, residue, modulus, coefficient) in the first residual.
PROFILES = (
    (3, 6, 3, 12, 1),
    (3, 6, 7, 12, 1),
    (6, 12, 7, 12, 2),
    (12, 24, 7, 12, 3),
    (16, 32, 11, 16, 1),
    (24, 48, 7, 12, 1),
    (32, 64, 11, 16, 2),
    (16, 32, 7, 8, 1),
    (32, 64, 7, 8, 2),
)


def predecessor_chain(state):
    """Return q,...,r with exact forward path q -> ... -> r -> state."""
    residue = state % 18
    if residue in (5, 11):
        return ((2 * state - 1) // 3,)
    if residue == 13:
        return ((8 * state - 5) // 9, (4 * state - 1) // 3)
    if residue == 17:
        return ((4 * state - 5) // 9, (2 * state - 1) // 3)
    return ()


def checked_chain(state):
    chain = predecessor_chain(state)
    if chain:
        assert 3 <= chain[0] < state
        assert 9 * chain[0] < 8 * state
        assert all(ARITH.PACKETS.step(x) == y
                   for x, y in zip(chain, chain[1:] + (state,)))
    return chain


def first_pass(measure):
    current = defaultdict(int)
    residual = defaultdict(int, measure)
    for state, coefficient in measure.items():
        chain = checked_chain(state)
        if coefficient <= 0 or not chain:
            continue
        residual[state] -= coefficient
        residual[chain[0]] += coefficient
        for point in chain:
            current[point] -= coefficient
    current, residual = ARITH.clean(current), ARITH.clean(residual)
    assert ARITH.subtract(measure, residual) == ARITH.subtract(current, P(current))
    return current, residual


def normalize(measure):
    """Return the full nonpositive current, terminal residual and finite stats.

    Descending processing visits each odd residual vertex at most once.
    The explicit state cap follows from the proved strict decrease of q.
    """
    assert all(state > 1 and state % 2 and isinstance(c, int)
               for state, c in measure.items())
    residual = defaultdict(int, ARITH.clean(measure))
    queue = [-state for state in residual]
    heapq.heapify(queue)
    seen = set(residual)
    depth = defaultdict(int)
    current, flows = defaultdict(int), {}
    bound = max(residual, default=1)
    state_cap, visits = (bound - 1) // 2, 0
    while queue:
        state = -heapq.heappop(queue)
        visits += 1
        assert visits <= state_cap
        coefficient = residual[state]
        chain = checked_chain(state)
        if coefficient <= 0 or not chain:
            continue
        target = chain[0]
        residual[state] = 0
        residual[target] += coefficient
        flows[state] = coefficient
        depth[target] = max(depth[target], depth[state] + 1)
        if target not in seen:
            heapq.heappush(queue, -target)
            seen.add(target)
        for point in chain:
            current[point] -= coefficient
    current, residual = ARITH.clean(current), ARITH.clean(residual)
    assert all(value < 0 for value in current.values())
    assert all(value <= 0 or not predecessor_chain(state)
               for state, value in residual.items())
    assert ARITH.subtract(measure, residual) == ARITH.subtract(current, P(current))
    assert sum(measure.values()) == sum(residual.values())
    assert ARITH.positive_mass(residual) <= ARITH.positive_mass(measure)
    # Verify the decreasing-graph flow recursion independently of queue order.
    incoming = defaultdict(int)
    for state, flow in flows.items():
        incoming[predecessor_chain(state)[0]] += flow
    for state in set(measure) | set(incoming) | set(flows):
        expected = (max(measure.get(state, 0) + incoming[state], 0)
                    if predecessor_chain(state) else 0)
        assert flows.get(state, 0) == expected
        assert residual.get(state, 0) == measure.get(state, 0) + incoming[state] - expected
    return current, residual, {
        "visited_states": visits, "proved_state_cap": state_cap,
        "rewrite_vertices": len(flows), "maximum_lineage_depth": max(depth.values(), default=0),
    }


def count_residue(cutoff, lower, upper, residue, modulus):
    return ((upper * cutoff - 1 - residue) // modulus
            - (lower * cutoff - residue) // modulus)


def direct_leaf_counts(cutoff):
    terms = (
        (3, 6, 3, 12, 1),
        (16, 32, 27, 48, 1),
        (32, 64, 27, 48, 2),
        (16, 32, 15, 24, 1),
        (32, 64, 15, 24, 2),
    )
    counts = [count_residue(cutoff, a, b, r, m) for a, b, r, m, _ in terms]
    weighted = sum(count * term[-1] for count, term in zip(counts, terms))
    assert weighted == 21 * cutoff // 4
    return counts, weighted


def annular_first_profile(cutoff, original):
    residual = defaultdict(int, {
        state: coefficient for state, coefficient in original.items()
        if coefficient < 0 or state % 18 in (1, 7)
    })
    for lower, upper, residue, modulus, coefficient in PROFILES:
        start = lower * cutoff + 1
        start += (residue - start) % modulus
        for state in range(start, upper * cutoff, modulus):
            residual[state] += coefficient
    return ARITH.clean(residual)


def check_cutoff(cutoff):
    original = ARITH.ANNULAR.annular_measure(cutoff)
    first_current, first_residual = first_pass(original)
    assert first_residual == annular_first_profile(cutoff, original)
    current, residual, stats = normalize(original)
    follow_current, follow_residual, _ = normalize(first_residual)
    assert follow_residual == residual
    combined_current = defaultdict(int, first_current)
    for state, value in follow_current.items():
        combined_current[state] += value
    assert ARITH.clean(combined_current) == current
    counts, lower = direct_leaf_counts(cutoff)
    first_leaves = sum(max(0, c) for state, c in first_residual.items() if state % 3 == 0)
    terminal_leaves = sum(max(0, c) for state, c in residual.items() if state % 3 == 0)
    assert first_leaves == lower <= terminal_leaves
    assert all(state < 64 * cutoff for state, c in residual.items() if c > 0)
    assert all(state < 96 * cutoff for state in current)
    assert all(state < 144 * cutoff for state in residual)
    for state, value in residual.items():
        if state % 3 == 0:
            assert value >= 0 and current.get(state, 0) == -value
    # A literal nonnegative combination of Z_M, M<=N/2, cannot supply this atom.
    frozen = next(state for state in range(32 * cutoff + 1, 64 * cutoff, 2)
                  if state % 24 == 15)
    assert residual[frozen] >= 2 and frozen % 3 == 0
    return {
        "N": cutoff, "initial_positive_mass": ARITH.positive_mass(original),
        "first_pass_positive_mass": ARITH.positive_mass(first_residual),
        "terminal_positive_mass": ARITH.positive_mass(residual),
        "first_pass_leaf_counts": counts,
        "first_pass_positive_mass_at_multiples_of_3": first_leaves,
        "terminal_positive_mass_at_multiples_of_3": terminal_leaves,
        "maximum_positive_state": max(state for state, c in residual.items() if c > 0),
        "maximum_current_state": max(current), "current_rows": len(current),
        "terminal_positive_residues_mod18": sorted({state % 18 for state, c in residual.items() if c > 0}),
        "literal_half_scale_recursion_obstruction_state": frozen,
        **stats,
    }


def has_smaller_short_ancestor(state):
    """Complete length<=2 check: the proof excludes valuations above 2."""
    for valuation in (1, 2):
        numerator = (1 << valuation) * state - 1
        if numerator % 3:
            continue
        intermediate = numerator // 3
        assert intermediate > 1 and intermediate % 2
        if intermediate < state:
            return True
        for previous in (1, 2):
            numerator = (1 << previous) * intermediate - 1
            if numerator % 3:
                continue
            ancestor = numerator // 3
            assert ancestor > 1 and ancestor % 2
            if ancestor < state:
                return True
    return False


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    for state in range(3, 4098, 2):
        checked_chain(state)
        assert has_smaller_short_ancestor(state) == bool(predecessor_chain(state))
    cases = [check_cutoff(cutoff) for cutoff in range(8, 513, 8)]
    cases += [check_cutoff(cutoff) for cutoff in (768, 6144)]
    # The period-increment proof uses exactly these three boundary phases.
    floor_phases = [{"N": n, "counts": direct_leaf_counts(n)[0],
                     "sum": direct_leaf_counts(n)[1]} for n in (8, 16, 24)]
    receipt = {
        "status": "PASS", "cutoff_range": [8, 512, 8],
        "additional_cutoffs": [768, 6144], "cases": len(cases),
        "short_ancestor_classification_checked_through": 4097,
        "floor_phases": floor_phases,
        "selected_results": [cases[0], cases[1], cases[2], cases[11], cases[20], cases[47], *cases[-2:]],
        "normalization_terminates_universally": True,
        "universal_complete_annular_certificate": False,
        "whole_annulus_absorption_threshold_improved": False,
    }
    path = Path(__file__).with_name("auxiliary_normal_form_audit.json")
    if args.write_receipt:
        path.write_text(json.dumps(receipt, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == receipt
    print(json.dumps({"status": "PASS", "cases": len(cases),
                      "terminal_positive_mass_lower_bound": "21*N/4",
                      "complete_certificate": False}, indent=2))


if __name__ == "__main__":
    main()
