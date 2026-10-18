"""Finite audits of the written complete odd-h interface and its limitations."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

import odd_interface as M

HERE = Path(__file__).resolve().parent
CAP = 2000


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def finite_path(x):
    """Capped discovery for finite test inputs only, never the general constructor."""
    current = {}
    for _ in range(CAP):
        if x == 1:
            return current
        assert x not in current, 'Finite input discovery found a cycle'
        current[x] = 1
        x = M.step(x)
    raise AssertionError('Finite input discovery cap exhausted')


def check(write=False):
    classification = []
    for z in range(1, 16384, 2):
        row = M.q_to_tripling(z)
        assert M.divergence(row['current']) == M.combine((1, M.Q(z)), (-1, M.pair(row['child'])))
        assert (M.chi(6*z+1) == M.chi(z)) == (z % 8 == 3)
        if z % 8 != 3:
            q = M.critical_target(z)
            assert M.critical_index(q) == z
            assert M.covered_critical(q) == M.zplus(z)
        else:
            q = None
        classification.append((z, row['kind'], row['child'], q))

    critical_count = 0
    for q in range(1, 65536, 2):
        if M.critical(q):
            critical_count += 1
            assert M.critical_target(M.critical_index(q)) == q
    restrictions = []
    for k in range(33):
        for j in range(16):
            C = 6*j+1
            z = 3**k*C
            w, recovered = M.odd_parent(z)
            assert recovered == k and M.odd_reduction(w)['z'] == z
            restrictions.append((k, C, w, z))

    reductions, categories, clocks = [], Counter(), 0
    for w in range(3, 32768, 8):
        if M.NORMAL.valuation2(3*w-1) % 2 == 0:
            continue
        row = M.odd_reduction(w)
        categories[f"{'high' if row['h'] >= 7 else 'low'}_{row['kind']}_{row['shrinking']}"] += 1
        reductions.append((w, row['h'], row['child'], digest(row['current'])))
        if w < 2048:
            u = row['child']
            left, right = 3*u, M.step(u)
            for ell in range(CAP):
                if left == right:
                    break
                left, right = M.step(left), M.step(right)
            else:
                raise AssertionError('Finite merger-clock check exhausted its cap')
            length = M.parent_clock(row, ell)
            assert M.prefix(3*w, length)[0] == M.prefix(w, length+1)[0]
            clocks += 1
            doubled = {x: 2*c for x, c in row['current'].items()}
            assert M.divergence(doubled) == M.combine((2, M.pair(w)), (-2, M.pair(u)))

    expansions = []
    for j in (0, 1, 2, 7, 31, 127, 1023):
        for w, h, child in ((64*j+19, 3, 96*j+29),
                            (256*j+139, 5, 288*j+157)):
            data = M.odd_reduction(w)
            assert data['h'] == h and data['child'] == child > w
            assert data['kind'] == 'F'
            expansions.append((w, h, child))

    compilers = []
    stored_inputs = stored_output = None
    for limit in (64, 128, 512):
        inputs = {}
        for z in M.required_indices(limit):
            inputs[z] = M.combine((1, finite_path(6*z+1)), (-1, finite_path(z)))
            assert M.divergence(inputs[z]) == M.Q(z)
        for one_sided in (False, True):
            supplied = ({z: M.combine((1, J), (1, finite_path(3))) for z, J in inputs.items()}
                        if one_sided else inputs)
            result = M.compile_inputs(limit, supplied)
            compilers.append(dict(limit=limit, mode='one-sided' if one_sided else 'exact',
                                  input_count=len(inputs), output_rows=len(result['current']),
                                  input_hash=digest(supplied), output_hash=digest(result['current'])))
            if limit == 128 and not one_sided:
                stored_inputs = json.dumps(inputs, sort_keys=True, indent=2)+'\n'
                stored_output = 'source,coefficient\n'+''.join(f'{x},{c}\n' for x,c in result['current'].items())

    delays = []
    for repeats in (1, 2, 4, 8, 16, 32, 64, 128):
        for extra in (0, 3):
            row = M.delayed_ray(repeats, extra)
            assert all(M.NORMAL.normal_form(q) == q and q > row['N'] for q in row['states'])
            # Every decreasing valuation-one inverse chain stays above the known cutoff.
            for q in row['states']:
                h, _ = M.ternary(q+1)
                minimum = 2**h*(q+1)//3**h-1
                assert minimum > row['N']
            delays.append(dict(repeats=repeats, extra_scale=extra,
                               cutoff_bits=row['N'].bit_length(), weight=row['weight'],
                               ordinary_steps=8*repeats, run_returns=2*repeats,
                               prefix_hash=digest(row['states']), seed=str(row['seed']) if repeats <= 2 else None))

    receipt = dict(status='PASS', clock='odd-only Syracuse, absorbing at1',
                   scope='Complete arithmetic interfaces and scoped finite-delay obstruction; no universal Q supply',
                   classification_count=len(classification), classification_hash=digest(classification),
                   critical_targets_below65536=critical_count,
                   actual_parameter_cases=len(restrictions), parameter_hash=digest(restrictions),
                   odd_h_reduction_count=len(reductions), reduction_hash=digest(reductions),
                   reduction_categories=dict(sorted(categories.items())), merger_clock_count=clocks,
                   expansion_examples=expansions, finite_input_discovery_cap=CAP,
                   compilers=compilers, delayed_ray_cases=delays)
    products = {'odd_interface_audit.json': json.dumps(receipt, sort_keys=True, indent=2)+'\n',
                'compiler128_inputs.json': stored_inputs, 'compiler128_current.csv': stored_output}
    for name, contents in products.items():
        if write:
            (HERE/name).write_text(contents)
        else:
            assert (HERE/name).read_text() == contents, f'Stored evidence differs: {name}'
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = check(args.write_receipt)
    print(json.dumps({k: result[k] for k in ('status', 'classification_count', 'odd_h_reduction_count',
                                           'actual_parameter_cases', 'merger_clock_count')}, sort_keys=True))
