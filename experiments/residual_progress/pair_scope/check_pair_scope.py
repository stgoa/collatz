"""Bounded exact checks; no absorption or merger search is performed."""
import argparse
import hashlib
import json
from pathlib import Path
import pair_scope as P

HERE = Path(__file__).resolve().parent


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def audit():
    comparisons = []
    for x in range(3, 32768, 4):
        if P.RUN.H.selected(x):
            continue
        data = P.compare_half(x)
        comparisons.append([x, data['a'], data['d'], data['w'], data['target'],
                            sorted(data['current'].items())])
    parameter_cases = []
    for a in range(2, 21):
        for d in range(2, 41):
            odd_modulus = 3**(a-1)
            w = (-pow(2**d, -1, odd_modulus)) % odd_modulus
            if w % 2 == 0:
                w += odd_modulus
            t = (2**d*w+1)//odd_modulus
            data = P.compare_half(2**a*t-1)
            assert (data['a'], data['d'], data['w']) == (a, d, w)
            parameter_cases.append([a, d, w, data['target']])

    # The new edge's exact canonical endpoints, including both residue classes.
    pair_edges = []
    for w in range(3, 32768, 8):
        q = 3*w
        expected = (q-3)//6 if q % 48 == 9 else q//3
        assert P.NORMAL.canonical(q)
        assert P.NORMAL.normal_form(w) == expected
        assert P.augmented_normal_form(q)[0] == P.augmented_normal_form(w)[0]
        pair_edges.append([w, q, expected])

    # Independent exhaustive bounded graph comparison. Every descending edge
    # stays in this cutoff, so the symbolic normal form is fully represented.
    vertices = [q for q in range(1, 32768, 2) if P.NORMAL.canonical(q)]
    parent = {q: q for q in vertices}
    def find(q):
        while parent[q] != q:
            parent[q] = parent[parent[q]]
            q = parent[q]
        return q
    for q in vertices:
        if q % 24 == 9:
            lower = (q-3)//6 if q % 48 == 9 else q//3
            u, v = find(q), find(lower)
            parent[max(u, v)] = min(u, v)
    for q in vertices:
        assert find(q) == P.augmented_normal_form(q)[0]
        if q % 8 == 7:
            assert find(q) == q

    mersennes = [P.mersenne_obstruction(a) for a in [19,35,51,67,99,195,387,771]]
    even_height = []
    for a in [13,21,29,45,77,141,269]:
        data = P.compare_half(2**a-1)
        assert data['d'] == 4 and data['target'] == 18*data['w']+1
        U = 9*data['w']
        assert U > data['root']
        even_height.append([a, data['root'], U])

    return dict(status='PASS', clock='odd-only Syracuse, absorbing at1',
                scope='Finite exact checks of written identities; no universal pair premise certified',
                comparison_count=len(comparisons), comparison_hash=digest(comparisons),
                parameter_case_count=len(parameter_cases), parameter_hash=digest(parameter_cases),
                hypothetical_edge_count=len(pair_edges), edge_hash=digest(pair_edges),
                finite_quotient_vertices=len(vertices), finite_quotient_hash=digest([[q, find(q)] for q in vertices]),
                infinite_family_samples=mersennes, even_return_growth_samples=even_height,
                caps=dict(comparison_root_max=32767, a_max=20, d_max=40,
                          hypothetical_w_max=32767, quotient_vertex_max=32767),
                searches='None: every loop has a fixed bound or a proved decreasing positive integer')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'pair_scope_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2, sort_keys=True)+'\n')
    else:
        assert json.loads(path.read_text()) == result, 'Receipt differs; inspect before regenerating'
    print('PASS: general half-seed boundaries, finite pair types, hypothetical catalogue, and infinite counterfamily')


if __name__ == '__main__':
    main()
