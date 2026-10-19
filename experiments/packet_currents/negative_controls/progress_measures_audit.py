"""Cross-audit of main commit ce56699 (R9, R10) and a control for its progress measures.

Part A (d = 1), using only affine_controls.py:
  * ||P A_N||_1 = ||R A_N||_1 = 171N/4 - |c_N| with |c_N| <= 3, where R collapses
    F-chains (F(x) = 4x+1) and c_N is the annular mass of the chain rooted at 1;
  * (R A_N)(p) = 2 at the 2N states p = -1 mod 36 in (32Q, 64Q);
  * c_80000 = 0, by an independent point evaluator for Pi_N(y);
  * the exposure potential Phi for A_96 is 17 at depths 20..27 and 0 at 28.

Part B (d = 61): the same quantities for the 64-fold increment
A'_N = Pi'_(64N) - Pi'_N of T_61. One-pass compression and early exposure
progress look similar, yet a positive component is permanent: it contains
the 41-cycle, so no further exposure can link it to an absorber. Progress
measures that behave alike on both maps cannot by themselves certify that
every positive plateau ends for 3x+1.

Finite checks only. Standard library only. Run without -O.
"""
from collections import defaultdict
from pathlib import Path
import json
import sys

from affine_controls import (Basins, absorbing, components, coefficient, cutoffs,
                             lift_classes, packets, push, step)


def increment(d, N):
    big, _, _ = packets(d, 64*N)
    small, _, _ = packets(d, N)
    A = dict(big)
    for y, c in small.items():
        A[y] = A.get(y, 0) - c
    return {y: c for y, c in A.items() if c}


def root(d, x):
    """Collapse x = F(z) = 4z+d (z odd, z >= 1) down to its F-chain root."""
    while (x - d) % 4 == 0 and (x - d)//4 >= 1 and ((x - d)//4) % 2:
        x = (x - d)//4
    return x


def collapse(d, mu):
    out = defaultdict(int)
    for x, c in mu.items():
        r = root(d, x)
        if r not in absorbing(d):
            out[r] += c
    return {y: c for y, c in out.items() if c}


def norm(mu):
    return sum(map(abs, mu.values()))


def positive(mu):
    return sum(c for c in mu.values() if c > 0)


def point_value(d, N, y):
    """Pi_N(y) from the lift structure alone, without building the measure."""
    total = 0
    for n, target in components(d, N):
        for a, q, period, t0, count in lift_classes(d, n):
            if (3*q + d) >> a > y:
                continue
            numerator = (y << a) - d
            if numerator % 3:
                continue
            x = numerator//3
            if x % 2 == 0 or (x - q) % period or x > n:
                continue
            t = (x - q)//period
            if t >= t0 + count % 3 and t < t0 + count:
                total += coefficient(x, target)
    return total


class DisjointSets:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        self.parent.setdefault(x, x)
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        self.parent[self.find(x)] = self.find(y)


def exposure(d, mu, depth_cap):
    """Phi by depth: positive mass of exposed components not touching A_d."""
    graph, positions, trace = DisjointSets(), list(mu), []
    for a in absorbing(d):
        graph.join(a, 1)
    for depth in range(depth_cap + 1):
        totals = defaultdict(int)
        for x, c in mu.items():
            totals[graph.find(x)] += c
        sink = graph.find(1)
        trace.append(sum(m for comp, m in totals.items() if comp != sink and m > 0))
        if depth < depth_cap:
            positions = [p if p in absorbing(d) else (graph.join(p, step(d, p)) or step(d, p))
                         for p in positions]
    return trace, graph


def part_a():
    cases = list(range(8, 513, 8)) + [768, 1024, 2048, 4096]
    for N in cases:
        Q = 9*N//4
        A = increment(1, N)
        PA, RA = push(1, A), collapse(1, A)
        chain, x = [], 1
        while x < 64*Q:
            if Q < x:
                chain.append(x)
            x = 4*x + 1
        c = sum(A.get(x, 0) for x in chain)
        assert abs(c) <= 3 and 4*(norm(PA) + abs(c)) == 171*N and norm(RA) == norm(PA), N
        survivors = [p for p in range(32*Q + 35 - (32*Q) % 36, 64*Q, 36)]
        assert len(survivors) == 2*N and all(RA.get(p) == 2 for p in survivors), N
    N, Q = 80000, 9*80000//4
    chain, x = [], 1
    while x < 64*Q:
        if Q < x:
            chain.append(x)
        x = 4*x + 1
    c80000 = sum(point_value(1, 64*N, y) - point_value(1, N, y) for y in chain)
    assert c80000 == 0
    for N in (8, 96, 1024):                     # point evaluator vs materialised measure
        mu, _, _ = packets(1, N)
        assert all(point_value(1, N, y) == c for y, c in mu.items())
        assert all(point_value(1, N, y) == 0 for y in range(3, 9*N//4 + 7, 2) if y not in mu)
    trace, _ = exposure(1, increment(1, 96), 28)
    assert trace[20:28] == [17]*8 and trace[28] == 0
    return dict(norm_formula_cases=len(cases), largest_N=cases[-1], c_80000=c80000,
                phi_A96_depth_20_to_28=trace[20:29])


def part_b():
    d, basins = 61, Basins(61)
    rows = []
    for N in (8, 16, 24, 32):
        A = increment(d, N)
        pairing = sum(c*basins.e(y) for y, c in A.items())
        PA = push(d, A, absorbing(d))
        RA = collapse(d, A)
        assert norm(RA) == norm(PA)
        row = dict(N=N, atoms=len(A), norm=norm(A), one_pass_ratio=round(norm(PA)/norm(A), 4),
                   positive_mass=positive(A), e_pairing=pairing)
        if pairing > 0:
            cap = 400
            trace, graph = exposure(d, A, cap)
            cycle = basins.cycles[235]
            # The surviving component contains the whole cycle: it is closed
            # under S, so later exposure cannot add an arrow leaving it.
            comp = graph.find(cycle[0])
            assert all(graph.find(c) == comp for c in cycle) and comp != graph.find(1)
            mass = sum(c for y, c in A.items() if graph.find(y) == comp)
            assert mass == pairing and trace[-1] >= mass > 0
            assert all(a >= b for a, b in zip(trace, trace[1:]))
            row.update(phi_depth_0=trace[0], phi_depth_25=trace[25], phi_at_cap=trace[-1],
                       cap=cap, permanent_component_mass=mass)
        rows.append(row)
    assert any(r["e_pairing"] > 0 for r in rows)
    d1 = increment(1, 96)
    reference = dict(N=96, one_pass_ratio=round(norm(push(1, d1))/norm(d1), 4),
                     ratio_formula="171/198 = 19/22 = 0.8636")
    return dict(map=d, increments=rows, d1_reference=reference)


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    report = dict(scope="Finite checks of ce56699's R9 norm formula and R10 exposure trace, "
                  "and the same measures on T_61. No progress lemma is proved or refuted for 3x+1.",
                  part_a=part_a(), part_b=part_b(), status="PASS")
    path = Path(__file__).with_name("progress_measures_audit.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
