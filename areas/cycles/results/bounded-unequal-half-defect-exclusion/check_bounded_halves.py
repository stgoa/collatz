"""Closed-graph certificate; arbitrary lengths follow from the README loop lemma."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
MAX_LEVEL = 12
# These guards only abort: a truncated graph or trace is never accepted.
RESOURCE_STATES = 500_000
RESOURCE_BITS = 1024


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def step(x, d):
    require(x != 0 and x % 2 == 1 and d > 0 and d % 2 == 1, "signed odd domain")
    numerator = 3 * x + d
    if numerator == 0:
        return None
    exponent = (abs(numerator) & -abs(numerator)).bit_length() - 1
    successor = numerator // (1 << exponent)
    require(exponent >= 1 and successor % 2 == 1 and successor != 0, "exact valuation")
    return exponent, successor


def guard(size, state):
    require(size < RESOURCE_STATES and abs(state).bit_length() <= RESOURCE_BITS,
            "RESOURCE GUARD: unfinished computation, certificate failed")


def positive_closure(seeds, d):
    edges = {}
    for seed in sorted(seeds):
        require(seed > 0 and seed % 2 == 1, "positive closure seed")
        x = seed
        while x not in edges:
            guard(len(edges), x)
            arrow = step(x, d)
            require(arrow is not None and arrow[1] > 0, "positive closure arrow")
            edges[x] = arrow
            x = arrow[1]
    for x, arrow in edges.items():
        require(step(x, d) == arrow and arrow[1] in edges, "graph not closed")
    return edges


def crossing_basin(level):
    d = (1 << level) - 1
    crossings = {}
    # All negative odd x=-a with 3x+d>0; zero numerators are excluded.
    for a in range(1, (d - 1) // 3 + 1, 2):
        arrow = step(-a, d)
        if arrow is not None and arrow[1] > 0:
            require(arrow[0] < level, "crossing valuation bound")
            crossings[-a] = arrow
    edges = positive_closure({y for _, y in crossings.values()}, d)
    return crossings, edges


@dataclass(frozen=True)
class Trace:
    states: tuple
    valuations: tuple
    cycle_start: int | None


TRACES = {}


def complete_trace(start, d):
    key = start, d
    if key in TRACES:
        return TRACES[key]
    seen, states, valuations = {}, [start], []
    x = start
    while x not in seen:
        guard(len(valuations), x)
        seen[x] = len(valuations)
        arrow = step(x, d)
        if arrow is None:
            result = Trace(tuple(states), tuple(valuations), None)
            break
        exponent, x = arrow
        valuations.append(exponent)
        states.append(x)
    else:
        result = Trace(tuple(states), tuple(valuations), seen[x])
    require(len(result.states) == len(result.valuations) + 1, "trace shape")
    for i, exponent in enumerate(result.valuations):
        require(step(result.states[i], d) == (exponent, result.states[i + 1]), "trace edge")
    if result.cycle_start is None:
        require(step(result.states[-1], d) is None, "unclosed trace")
    else:
        require(result.states[-1] == result.states[result.cycle_start], "cycle closure")
        require(len(set(result.states[:-1])) == len(result.states) - 1, "first repeat")
    TRACES[key] = result
    return result


def intercept(word):
    c, total = 0, 0
    for exponent in word:
        c = 3 * c + (1 << total)
        total += exponent
    return c


def affine(word, x=Fraction(1)):
    for exponent in word:
        x = (3 * x + 1) / (1 << exponent)
    return x


def reconstruct(A, B, J, r, order):
    p = J - r
    if order == "HL":
        u = A[:-1] + (A[-1] - p,) + B[:-1] + (B[-1] - r,)
        v = A + B[:-1] + (B[-1] + J,)
        s = J
    else:
        u = A[:-1] + (A[-1] + p,) + B[:-1] + (B[-1] - J,)
        v = A + B[:-1] + (B[-1] + r,)
        s = r
    require(min(u + v) >= 1 and len(u) == len(v), "positive equal-length halves")
    require(sorted(abs(a - b) for a, b in zip(u, v) if a != b) == [p, J + r], "two defects")
    require(sum(u) + sum(v) == 2 * (sum(A) + sum(B)), "combined total")
    return u, v, s


def prefix_with_loops(trace, end, repetitions):
    c = trace.cycle_start
    if c is None or end < c:
        require(repetitions == 0, "no insertion site")
        return trace.valuations[:end + 1]
    return (trace.valuations[:c] + trace.valuations[c:] * repetitions
            + trace.valuations[c:end + 1])


def loop_data(trace, end, d, offset, u, name):
    c = trace.cycle_start
    if c is None or end < c:
        return None
    cycle = trace.valuations[c:]
    entry = trace.states[c]
    require(entry > 0 and all(x > 0 for x in trace.states[c:]), "negative insertion cycle")
    slope = Fraction(3 ** len(cycle), 1 << sum(cycle))
    fixed = Fraction(entry, d)
    require(0 < slope < 1, "cycle is not contracting")
    require(affine(cycle, fixed) == fixed, "intrinsic additive-one fixed point")
    limit = affine(u[offset + c:], fixed)
    return dict(block=name, entry=entry, insertion_index=offset + c,
                word=cycle, slope=slope, fixed_point=fixed, limit=limit)


def serial_loop(loop):
    return {k: str(v) if isinstance(v, Fraction) else v for k, v in loop.items()}


def verify_join(J, r, order, h, first, i, second, k):
    A, B = first.valuations[:i + 1], second.valuations[:k + 1]
    z = first.states[i + 1]
    require(z > 0, "negative-interface join found: present proof does not cover it")
    u, v, s = reconstruct(A, B, J, r, order)
    n, S = len(u), sum(A) + sum(B)
    P = (1 << S) + 3 ** n
    require(intercept(v) == (1 << s) * intercept(u) - h * P, "normal-form identity")
    require(intercept(u + v) % P == 0, "plus cancellation")
    D = (1 << (2 * S)) - 3 ** (2 * n)
    require(D > 0, "base denominator sign")
    value, threshold = affine(u), (1 << s) + h
    require(value < threshold, "base affine bound")
    d1, d2 = ((1 << J) - 1, (1 << r) - 1) if order == "HL" else ((1 << r) - 1, (1 << J) - 1)
    loops = [loop_data(first, i, d1, 0, u, "A"),
             loop_data(second, k, d2, len(A), u, "B")]
    for loop in loops:
        if loop is not None:
            require(loop["limit"] <= threshold, "loop-limit affine bound")
    # Finite regression of the general convex identity and insertion placement.
    samples = 0
    for ta in ((0, 1, 2) if loops[0] else (0,)):
        for tb in ((0, 1, 2) if loops[1] else (0,)):
            AA, BB = prefix_with_loops(first, i, ta), prefix_with_loops(second, k, tb)
            uu, vv, ss = reconstruct(AA, BB, J, r, order)
            rho_a = loops[0]["slope"] ** ta if loops[0] else Fraction(1)
            rho_b = loops[1]["slope"] ** tb if loops[1] else Fraction(1)
            expected = rho_a * rho_b * value
            if loops[0]:
                expected += (1 - rho_a) * rho_b * loops[0]["limit"]
            if loops[1]:
                expected += (1 - rho_b) * loops[1]["limit"]
            require(affine(uu) == expected < threshold, "convex identity regression")
            PP = (1 << (sum(AA) + sum(BB))) + 3 ** len(uu)
            require(intercept(vv) == (1 << ss) * intercept(uu) - h * PP, "inserted endpoint identity")
            samples += 1
    canonical = Fraction(intercept(u + v), D)
    require(0 < canonical < 1, "normalized base state")
    return dict(J=J, r=r, order=order, h=h, interface=z, A=A, B=B,
                half_length=n, segment_total=S, base_value=str(value), threshold=threshold,
                canonical_state=str(canonical), loops=[serial_loop(x) for x in loops if x],
                convex_identity_samples=samples)


def digest(edges):
    return sha256(json.dumps(sorted(edges.items()), separators=(",", ":")).encode()).hexdigest()


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    controls = []
    for fixture in json.loads(path.read_text())["cycles"]:
        d, xs, word = fixture["d"], fixture["states"], tuple(fixture["valuations"])
        require(len(xs) == len(word) and min(xs) == fixture["minimum"], "fixture shape")
        for i, x in enumerate(xs):
            require(step(x, d) == (word[i], xs[(i + 1) % len(xs)]), "actual cycle replay")
        matches = []
        if len(word) % 2 == 0:
            n = len(word) // 2
            for cut in range(len(word)):
                rotated = word[cut:] + word[:cut]
                differences = [abs(a - b) for a, b in zip(rotated[:n], rotated[n:]) if a != b]
                if len(differences) == 2:
                    p, q = sorted(differences)
                    if p < q and (p + q) % 2 == 0 and p + q <= 2 * MAX_LEVEL:
                        matches.append(cut)
        require(not matches, "standard fixture enters claimed class")
        controls.append(dict(d=d, minimum=min(xs), period=len(word), matching_cuts=matches))
    # Actual cycles inside the claimed word class survive with denominator >1.
    inside = []
    for name, u, v, expected_d in [
        ("amplitudes_2_4", (2, 1, 1, 1, 3), (2, 1, 1, 3, 7), 361),
        ("amplitudes_1_5", (1, 2, 1, 1, 2, 1, 1, 2), (1, 2, 1, 1, 3, 1, 1, 7), 893),
    ]:
        word = u + v
        C, D = intercept(word), (1 << sum(word)) - 3 ** len(word)
        G = gcd(C, D)
        require(D // G == expected_d > 1, "inside-control denominator")
        states = [intercept(word[i:] + word[:i]) // G for i in range(len(word))]
        for i, x in enumerate(states):
            require(step(x, expected_d) == (word[i], states[(i + 1) % len(word)]), "inside-control arrows")
        require(Fraction(C, D) < 1, "normalized control state")
        inside.append(dict(name=name, d=expected_d, minimum=min(states), word=word,
                           canonical_state=str(Fraction(C, D))))
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), standard=controls, inside_class=inside)


def main():
    basins = {j: crossing_basin(j) for j in range(1, MAX_LEVEL + 1)}
    rows, joins = [], []
    for J in range(2, MAX_LEVEL + 1):
        for r in range(1, J):
            for order in ("HL", "LH"):
                first_level, second_level = (J, r) if order == "HL" else (r, J)
                d1, d2 = (1 << first_level) - 1, (1 << second_level) - 1
                bound_a, bound_b = (J - r, r) if order == "HL" else (0, J)
                cross1, graph1 = basins[first_level]
                positive_interfaces = {y for a, y in list(cross1.values()) + list(graph1.values()) if a > bound_a}
                second_graph = positive_closure(positive_interfaces, d2)
                h_positive = {y for a, y in second_graph.values() if a > bound_b}
                h_negative = {y for a, y in basins[second_level][1].values() if a > bound_b}
                candidates = h_positive | h_negative
                before = len(joins)
                for h in sorted(candidates):
                    first = complete_trace(-h, d1)
                    for i, a in enumerate(first.valuations):
                        if a <= bound_a:
                            continue
                        second = complete_trace(first.states[i + 1], d2)
                        for k, b in enumerate(second.valuations):
                            if b > bound_b and second.states[k + 1] == h:
                                joins.append(verify_join(J, r, order, h, first, i, second, k))
                rows.append(dict(J=J, r=r, order=order,
                                 positive_interface_seeds=len(positive_interfaces),
                                 second_graph_states=len(second_graph), second_graph_sha256=digest(second_graph),
                                 positive_interface_h=sorted(h_positive), negative_interface_h=sorted(h_negative),
                                 joins=len(joins) - before))
    counts = Counter(len(j["loops"]) for j in joins)
    require(len(rows) == MAX_LEVEL * (MAX_LEVEL - 1), "parameter coverage")
    require(len(joins) == 74 and dict(counts) == {0: 15, 1: 44, 2: 15}, "classification regression")
    require(not any(j["J"] == 2 and j["r"] == 1 for j in joins), "prior amplitudes-1-3 exclusion")
    require(sum(j["J"] == 3 and j["r"] == 2 for j in joins) == 1, "prior amplitudes-1-5 classification")
    require(sum(j["J"] == 3 and j["r"] == 1 for j in joins) == 2, "prior amplitudes-2-4 classification")
    receipt = dict(
        scope="All J=2..12, 1<=r<J, both segment orders; no word-length or repetition bound",
        all_closures_complete=True, all_traces_complete=True, accepted_truncations=0,
        parameter_cases=len(rows), base_joins=len(joins), negative_interface_joins=0,
        base_loop_count_distribution=dict(sorted(counts.items())),
        loop_limits=sum(counts[k] * k for k in counts),
        max_base_half_length=max(j["half_length"] for j in joins),
        max_join_h=max(j["h"] for j in joins),
        completed_traces=len(TRACES), max_trace_length=max(len(t.valuations) for t in TRACES.values()),
        trace_termination_counts=dict(Counter("cycle" if t.cycle_start is not None else "zero_numerator" for t in TRACES.values())),
        convex_identity_samples=sum(j["convex_identity_samples"] for j in joins),
        crossing_basins=[dict(level=j, crossing_seeds=len(c), states=len(g), sha256=digest(g))
                         for j, (c, g) in basins.items()],
        parameter_rows=rows, joins=joins, controls=actual_controls())
    (HERE / "check_bounded_halves.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: receipt[k] for k in ("parameter_cases", "base_joins", "loop_limits", "completed_traces",
                                            "max_trace_length", "convex_identity_samples", "accepted_truncations")}, sort_keys=True))


if __name__ == "__main__":
    main()
