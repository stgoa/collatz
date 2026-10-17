"""Exact merger-scope checks and independent sign/climb reproduction.

No universal absorption claim. The two annular orbit scans have explicit
path caps and verify every source reaches the already verified memoized tail.
"""

import argparse
from collections import defaultdict
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


NORMAL = load("scope_normal", HERE.parent / "bridge_normal_form/normal_form.py")
ANN = load("scope_annular", ROOT / "experiments/current_construction/recursive/check_annular_recursion.py")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def forward_union(N, cap=1000):
    known = {1}
    for x in range(1, N+1, 2):
        path, seen = [], set()
        while x not in known:
            assert x not in seen and len(path) < cap
            seen.add(x)
            path.append(x)
            x = NORMAL.step(x)
        known.update(path)
    return known


def sign_climb(N, cap=1000):
    measure = ANN.annular_measure(N)
    peak = {1: 1}
    longest_new_path = 0
    for source in measure:
        x, path, seen = source, [], set()
        while x not in peak:
            assert x not in seen and len(path) < cap
            seen.add(x)
            path.append(x)
            x = NORMAL.step(x)
        longest_new_path = max(longest_new_path, len(path))
        maximum = peak[x]
        for x in reversed(path):
            maximum = max(maximum, x)
            peak[x] = maximum
    thresholds = (1, 4, 16, 64, 128)
    table = {str(h): [sum(c for x, c in measure.items() if c > 0 and peak[x] >= h*x),
                      -sum(c for x, c in measure.items() if c < 0 and peak[x] >= h*x)]
             for h in thresholds}
    expected = {
        6144: [[152064,152064],[30453,30479],[7730,7725],[1891,1896],[955,931]],
        9216: [[228096,228096],[45758,45806],[11738,11712],[2908,2791],[1491,1402]],
    }
    assert list(table.values()) == expected[N]
    # Seek an actual capacity-safe positive/negative sibling pair whose
    # future climb is large but whose merger precedes that climb.
    by_successor = defaultdict(lambda: [[], []])
    for x, c in measure.items():
        if peak[x] >= 64*x:
            by_successor[NORMAL.step(x)][int(c < 0)].append(x)
    witnesses = []
    for target, (positive, negative) in by_successor.items():
        for p in positive:
            for q in negative:
                if target < min(p, q):
                    current = {p: 1, q: -1}
                    assert NORMAL.divergence(current) == current
                    witnesses.append(dict(positive=p, positive_capacity=measure[p],
                                          negative=q, negative_capacity=-measure[q],
                                          common_successor=target,
                                          positive_peak=peak[p], negative_peak=peak[q],
                                          current_rows=[[p, 1], [q, -1]]))
    witness = min(witnesses, key=lambda w: (w['common_successor'], w['positive'], w['negative'])) if witnesses else None
    return dict(N=N, source_atoms=len(measure), peak_rows=len(peak),
                longest_new_path=longest_new_path, cap_per_new_path=cap,
                positive_negative_mass_by_climb=table,
                source_peaks_sha256=digest([(x,peak[x]) for x in measure]),
                early_merger_of_high_climbers=witness)


def annular_coefficient(N, x):
    lower = 9*N//4
    for band in range(6):
        if lower*2**band < x < lower*2**(band+1):
            return dict(zip(ANN.RESIDUES, ANN.EXPECTED_ROWS[band])).get(x % 18, 0)
    return 0


def early_high_climber_families():
    rows = []
    for a in (19, 37, 55, 73, 109, 199):
        N, z = 12*2**(a-5), 2**a-1
        p = (4*z-1)//3
        q = 4*p+1
        assert (4*z-1) % 3 == 0
        assert p % 18 == 1 and q % 18 == 5
        assert annular_coefficient(N,p) == 1 and annular_coefficient(N,q) == -1
        assert NORMAL.step(p) == NORMAL.step(q) == z < p < q
        assert 3*z < 8*N
        current = {p: 1, q: -1}
        assert NORMAL.divergence(current) == current
        x = z
        for j in range(a):
            assert x == 3**j*2**(a-j)-1
            if j < a-1:
                assert NORMAL.valuation2(3*x+1) == 1
                x = NORMAL.step(x)
        assert x == 2*3**(a-1)-1 and x > 128*q
        rows.append(dict(a=a, N=N, positive=p, negative=q, common_successor=z,
                         proved_later_height=x, current_rows=[[p,1],[q,-1]]))
    return rows


def valuation_cylinder(word):
    A, offset, numerator = 0, 0, 1
    for a in word:
        offset = 3*offset+2**A
        numerator *= 3
        A += a
    modulus = 2**(A+1)
    residue = ((2**A-offset)*pow(numerator,-1,modulus)) % modulus
    return residue, modulus


def actual_escape_roots():
    rows = []
    for repeats in (1, 2, 4, 8, 16, 32):
        word = (1,1,1,1,1,2)+(1,2)*repeats+(1,)
        residue, modulus = valuation_cylinder(word)
        x = residue+modulus*((-residue*pow(modulus,-1,3)) % 3)
        x += 3*modulus
        choices = []
        for a in (12,14,16,18,21):
            b = ((x-1)//a).bit_length()-1
            if b >= 9:
                choices.append(a*2**b)
        N = max(choices)
        assert N < x < 3*N//2 and x % 12 == 3
        states, y = [x], x
        for a in word:
            assert NORMAL.valuation2(3*y+1) == a
            y = NORMAL.step(y)
            states.append(y)
        # The final extra valuation protects normalization at the preceding
        # state by S(y)<=3nu(y)+2; no assertion about the unused final nu.
        assert all(NORMAL.normal_form(y) > N for y in states[:-1])
        rows.append(dict(repeats=repeats, N=N, seed=x,
                         protected_ordinary_states=len(states)-1,
                         word=list(word), states_sha256=digest(states)))
    return rows


def run():
    f8 = forward_union(8)
    assert f8 == {1,3,5,7,11,13,17}
    assert 11 in f8 and NORMAL.normal_form(11) > 8
    assert 21 not in f8 and NORMAL.normal_form(21) <= 8
    bounds = 0
    for x in range(1, 32768, 2):
        q = NORMAL.normal_form(x)
        assert NORMAL.step(x) <= 3*q+2
        assert NORMAL.step(x) in (NORMAL.step(q), 3*q+2)
        bounds += 1
    # Fixed complementary escape cylinder: all five rising states are
    # canonical, the sixth state's slope exceeds3.
    escape = []
    for index in range(128):
        original = x = 191+256*index
        values = [x]
        for j, a in enumerate((1,1,1,1,1,2)):
            assert NORMAL.valuation2(3*x+1) == a
            assert NORMAL.canonical(x)
            x = NORMAL.step(x)
            values.append(x)
        assert 128*x == 729*original+665
        escape.append(values)
    climbs = [sign_climb(N) for N in (6144, 9216)]
    return dict(status="PASS", proof="MERGER_SCOPE.md",
                external_commit="ceb94fc372533e6fdc196595a817e8c01bc62d51",
                normal_form_successor_bound_checks=bounds,
                exact_incomparable_sets=dict(N=8, forward_union=sorted(f8),
                    forward_only=11, elementary_only=21),
                escape_prefix=dict(valuations=[1,1,1,1,1,2],
                    residue=191, modulus=256, iterate_slope="729/128",
                    iterate_intercept="665/128", representatives=128,
                    prefix_rows_sha256=digest(escape)),
                actual_required_ray_escape_examples=actual_escape_roots(),
                universal_early_cancellation_examples=early_high_climber_families(),
                independent_sign_climb_checks=climbs,
                finite_integer_survival_rate_claim=False,
                arbitrary_catalogue_obstruction_proved=False,
                universal_termination_proved=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    result = run()
    path = HERE / "merger_scope_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(result,indent=2)+"\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", successor_bound_cases=result['normal_form_successor_bound_checks'],
                          sign_climb_cutoffs=[r['N'] for r in result['independent_sign_climb_checks']],
                          early_merger_witnesses=[r['early_merger_of_high_climbers']
                              for r in result['independent_sign_climb_checks']]),indent=2))


if __name__ == "__main__":
    main()
