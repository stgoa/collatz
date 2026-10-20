"""Exact checks of aggregate current duality and modular information loss.

The reflected-annulus obstruction is on NEGATIVE integers. It is not an
obstruction to currents for the positive Collatz annuli. Bounded-depth graph
failures apply only to the exposed edges, never to arbitrary future currents.
"""

from argparse import ArgumentParser
from collections import defaultdict
import csv
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
RESIDUES = (1, 5, 7, 11, 13, 17)
ROWS = (
    (1, 0, 1, 0, -2, 0), (2, 1, -1, 1, -1, -2),
    (3, -1, -3, 2, 0, -1), (1, -3, -2, 3, 1, 0),
    (-1, -2, -1, 1, 2, 1), (0, -1, 0, -1, 0, 2),
)


def step(x):
    assert x % 2 and x != 0
    value = 3 * x + 1
    return value // (value & -value)


def clean(mu):
    return {x: c for x, c in mu.items() if c}


def annulus(N):
    assert N > 0 and N % 8 == 0
    Q = 9 * N // 4
    answer = {}
    for j, row in enumerate(ROWS):
        coefficients = dict(zip(RESIDUES, row))
        for y in range((Q << j) + 1, Q << (j + 1), 2):
            c = coefficients.get(y % 18, 0)
            if c:
                answer[y] = c
    assert len(answer) == 267 * N // 8
    assert sum(answer.values()) == 0
    return answer


def combine(*terms):
    result = defaultdict(int)
    for coefficient, measure in terms:
        for x, c in measure.items():
            result[x] += coefficient * c
    return clean(result)


def count_odds(cutoff):
    return {x: 1 for x in range(3, cutoff + 1, 2)}


def source(N):
    n1, n2 = (3 * N + 1) // 2, (3 * N + 1) // 4
    return {x: 3 * int(x % 3 == 2) - 1
            + (3 * int(x % 3 == 1) - 1 if x <= n2 else 0)
            for x in range(3, n1 + 1, 2)}


def divergence(current):
    result = defaultdict(int)
    for x, c in current.items():
        result[x] += c
        y = step(x)
        if y != 1:
            result[y] -= c
    return clean(result)


def shell(t):
    return combine((1, count_odds(64 * t)), (-1, count_odds(t)))


def annular_scale_identity(N):
    assert N % 8 == 0
    F_N, F_quarter = shell(N), shell(N // 4)
    V = combine((1, source(64 * N)), (-1, source(N)))
    K = combine((1, V), (3, F_N), (-3, F_quarter))
    D = combine((3, F_N), (-3, F_quarter),
                (-1, shell(3 * N // 2)), (-1, shell(3 * N // 4)))
    assert D == combine((1, annulus(N)), (1, divergence(K)))
    return D, K


def check_projection(N, K):
    assert K >= 1 and N % (1 << (K + 2)) == 0
    mu, Q = annulus(N), 9 * N // 4
    for modulus in (1 << K, 3 << K):
        totals = defaultdict(int)
        band_totals = [defaultdict(int) for _ in range(6)]
        for x, c in mu.items():
            band = (x // Q).bit_length() - 1
            totals[x % modulus] += c
            band_totals[band][x % modulus] += c
        assert not clean(totals)
        assert all(not clean(row) for row in band_totals)
    return {"N": N, "K": K, "atoms": len(mu)}


class DisjointSets:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x], self.size[x] = x, 1
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]


def exposure_progress(mu, cap=128, scale_identity=None):
    graph = DisjointSets()
    graph.find(1)
    for x in mu:
        graph.find(x)
    positions, edges, trace = list(mu), {}, []
    prior = sum(max(c, 0) for c in mu.values())
    for depth in range(cap + 1):
        totals, counts = defaultdict(int), defaultdict(int)
        for x, c in mu.items():
            component = graph.find(x)
            totals[component] += c
            counts[component] += 1
        absorbed = graph.find(1)
        positive = {c: mass for c, mass in totals.items() if c != absorbed and mass > 0}
        potential = sum(positive.values())
        assert potential <= prior
        prior = potential
        row = {"depth": depth, "positive_component_mass": potential,
               "positive_components": len(positive)}
        if positive:
            witness = max(positive, key=lambda x: (positive[x], -x))
            # q is an exact finite-graph dual: constant on every exposed edge,
            # zero at the absorber, nonnegative, and has positive source pairing.
            assert witness != absorbed
            assert all((graph.find(x) == witness) == (graph.find(y) == witness)
                       for x, y in edges.items())
            pairing = sum(c for x, c in mu.items() if graph.find(x) == witness)
            assert pairing == positive[witness] > 0
            row["dual_witness_pairing"] = pairing
            row["dual_witness_source_count"] = counts[witness]
            if scale_identity is not None:
                D, K = scale_identity
                # Use membership in the actually exposed component. Unknown
                # vertices have q=0; never insert them into the exposed graph.
                def q(x):
                    return int(x in graph.parent and graph.find(x) == witness)
                scale_pairing = sum(c * q(x) for x, c in D.items())
                flux = sum(c * (q(x) - q(step(x))) for x, c in K.items())
                unexposed_flux = sum(c * (q(x) - q(step(x)))
                                     for x, c in K.items() if x not in edges)
                assert flux == unexposed_flux
                assert scale_pairing == pairing + flux
                row["scale_identity_pairing"] = scale_pairing
                row["unexposed_boundary_flux"] = flux
                if depth == 27:
                    row["dual_component_vertices"] = sorted(x for x in graph.parent if q(x))
                    row["dual_component_source_states"] = sorted(x for x in mu if q(x))
                    row["nonzero_flux_rows"] = [
                        {"state": x, "current_weight": c, "indicator_difference": q(x) - q(step(x))}
                        for x, c in sorted(K.items()) if q(x) != q(step(x))
                    ]
                    augmented = DisjointSets()
                    augmented.parent, augmented.size = dict(graph.parent), dict(graph.size)
                    for x in K:
                        augmented.join(x, step(x))
                    masses = defaultdict(int)
                    for x, c in mu.items():
                        masses[augmented.find(x)] += c
                    absorber = augmented.find(1)
                    positives = {component: mass for component, mass in masses.items()
                                 if component != absorber and mass > 0}
                    row["after_exposing_all_source_scale_current_rows"] = {
                        "positive_component_mass": sum(positives.values()),
                        "positive_components": len(positives),
                    }
                    if positives:
                        comp = max(positives, key=positives.get)
                        def q_after(x):
                            return int(x in augmented.parent and augmented.find(x) == comp)
                        new_flux = sum(c * (q_after(x) - q_after(step(x))) for x, c in K.items())
                        assert new_flux == 0
                        assert sum(c * q_after(x) for x, c in D.items()) == positives[comp]
                        row["after_exposing_all_source_scale_current_rows"].update({
                            "largest_positive_mass": positives[comp], "boundary_flux": new_flux})
        trace.append(row)
        if not positive:
            return {"status": "one_sided_feasible_on_exposed_graph", "depth": depth,
                    "edge_count": len(edges), "trace": trace}
        if depth == cap:
            break
        for i, x in enumerate(positions):
            if x == 1:
                continue
            y = step(x)
            edges[x] = y
            graph.join(x, y)
            positions[i] = y
    return {"status": "unresolved_at_cap", "depth": cap,
            "edge_count": len(edges), "trace": trace}


def write_or_check_table(filename, table, write):
    path = HERE / filename
    rows = sorted(table.items())
    if write:
        with path.open("w", newline="") as stream:
            writer = csv.writer(stream, lineterminator="\n")
            writer.writerow(["state", "weight"])
            writer.writerows(rows)
    else:
        with path.open(newline="") as stream:
            reader = csv.reader(stream)
            assert next(reader) == ["state", "weight"]
            assert [(int(x), int(c)) for x, c in reader] == rows


def reflected_counterexample(write):
    positive = annulus(96)
    mu = {-y: c for y, c in positive.items()}
    cycles = ((-1,), (-5, -7), (-17, -25, -37, -55, -41, -61, -91))
    for cycle in cycles:
        assert all(step(x) == y for x, y in zip(cycle, cycle[1:] + cycle[:1]))
    assert len(set().union(*map(set, cycles))) == sum(map(len, cycles))
    anchors = {cycle[0] for cycle in cycles}
    current, residual, counts = defaultdict(int), defaultdict(int), defaultdict(int)
    maximum_steps = 0
    for source, coefficient in mu.items():
        x, seen = source, set()
        for t in range(1001):
            if x in anchors:
                residual[x] += coefficient
                counts[x] += 1
                maximum_steps = max(maximum_steps, t)
                break
            assert x < 0 and x not in seen
            seen.add(x)
            current[x] += coefficient
            x = step(x)
        else:
            raise AssertionError((source, "1000-step cap"))
    current, residual = clean(current), clean(residual)
    assert residual == {-1: -20, -5: -73, -17: 93}
    reconstructed = defaultdict(int, residual)
    for x, c in current.items():
        reconstructed[x] += c
        reconstructed[step(x)] -= c
    assert clean(reconstructed) == mu
    assert sum(mu.values()) == 0
    for modulus in (2, 4, 8, 6, 12, 24):
        totals = defaultdict(int)
        for x, c in mu.items():
            totals[x % modulus] += c
        assert not clean(totals)
    write_or_check_table("reflected_annulus_96_current.csv", current, write)
    write_or_check_table("reflected_annulus_96_residual.csv", residual, write)
    return {"domain": "negative odd integers; NOT ordinary positive Collatz",
            "reflected_positive_annulus_cutoff": 96, "source_atoms": len(mu),
            "cycle_component_masses": residual, "cycle_component_source_counts": counts,
            "current_rows": len(current), "maximum_steps_to_anchor": maximum_steps,
            "all_horizon_work": 0, "exact_current_exists": False,
            "nonpositive_residual_current_exists": False,
            "positive_component_mass_potential": 93}


def independent_collapse_check(N):
    mu = annulus(N)
    grouped = defaultdict(int)
    pushed = defaultdict(int)
    for x, c in mu.items():
        root = x
        while root % 8 == 5:
            root = (root - 1) // 4
        grouped[root] += c
        successor = step(x)
        if successor != 1:
            pushed[successor] += c
    absorber_mass = grouped.pop(1, 0)
    norm = sum(abs(c) for c in grouped.values())
    assert norm == sum(abs(c) for c in pushed.values())
    assert norm == 171 * N // 4 - abs(absorber_mass)
    assert abs(absorber_mass) <= 3
    assert 22 * norm <= 19 * sum(abs(c) for c in mu.values())
    Q = 9 * N // 4
    surviving = [x for x in range(32 * Q + 1, 64 * Q, 2) if x % 36 == 35]
    assert len(surviving) == 2 * N
    assert all(grouped[x] == 2 for x in surviving)
    return {"N": N, "collapsed_norm": norm, "absorbed_signed_mass": absorber_mass,
            "certified_positive_outer_atoms": len(surviving)}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    for row in ROWS:
        assert sum(row[::2]) == sum(row[1::2]) == 0
    projections = [check_projection(12 * 2**max(3, K), K) for K in range(1, 9)]
    scale_cases = []
    for N in (8, 16, 96, 112, 128, 144, 168):
        D, K = annular_scale_identity(N)
        scale_cases.append({"N": N, "source_scale_measure_atoms": len(D),
                            "boundary_current_rows": len(K)})
    positive_scan = exposure_progress(annulus(96), scale_identity=annular_scale_identity(96))
    reflection = reflected_counterexample(args.write_receipt)
    independent_collapse = [independent_collapse_check(N)
                            for N in (8, 16, 24, 96, 112, 128, 144, 168, 512)]
    result = {"status": "PASS", "modular_projection_checks": projections,
              "annular_scale_identity_checks": scale_cases,
              "positive_annulus_exposure": {"N": 96, **positive_scan},
              "negative_reflected_annulus": reflection,
              "independent_19_over_22_collapse_checks": independent_collapse,
              "unbounded_aggregate_depth_proved": False,
              "universal_positive_current_construction_proved": False}
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    path = HERE / "duality_audit.json"
    if args.write_receipt:
        path.write_text(encoded)
    else:
        assert json.loads(path.read_text()) == json.loads(encoded)
    print(json.dumps({"status": "PASS", "projection_cases": len(projections),
                      "positive_annulus_N96_first_one_sided_depth": positive_scan["depth"],
                      "negative_component_masses": reflection["cycle_component_masses"]}, indent=2))


if __name__ == "__main__":
    main()
