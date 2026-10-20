#!/usr/bin/env python3
"""Focused exact checks for complete critical-nine elimination."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import time

import w9_closure as M

HERE = Path(__file__).resolve().parent


def digest(rows):
    payload = json.dumps(sorted(rows.items()), separators=(',', ':')).encode()
    return hashlib.sha256(payload).hexdigest()


def capped_absorption(x, cap=10000):
    current, seen = Counter(), set()
    start = x
    for _ in range(cap):
        if x == 1:
            result = M.clean(current)
            assert M.divergence(result) == M.atoms((1, start))
            return result
        if x in seen:
            raise RuntimeError('Finite fixture encountered a nonabsorbing cycle')
        seen.add(x)
        current[x] += 1
        x = M.NORMAL.step(x)
    raise RuntimeError('Finite fixture cap reached; no absorption claim')


def supplied_pair(w):
    return M.combine((1, capped_absorption(3*w)), (-1, capped_absorption(w)))


def expect_error(kind, action):
    try:
        action()
    except kind:
        return
    raise AssertionError('Expected rejection was not raised')


def run():
    started = time.perf_counter()
    branches = Counter()
    maximum_requests = 0
    affine_table_checks = Counter()
    affine_table = {4: (9, 3, 4), 6: (27, 13, 16), 8: (81, 55, 64)}
    for w in range(9, 65536, 16):
        data = M.local_plan(w)
        branches[data['branch']] += 1
        maximum_requests = max(maximum_requests, len(data['coefficients']))
        if data['d'] in affine_table:
            a, b, denominator = affine_table[data['d']]
            assert denominator*(4*data['z']+1) == a*w+b
            if data['exception'] is not None:
                assert denominator*data['exception'] == a*w+b
            affine_table_checks[str(data['d'])] += 1

    for z in range(1, 8192, 2):
        M.tripling_plan_bound(z)

    synthetic = 0
    synthetic_branches = Counter()
    # Every prescribed valuation d, with eight exact admissible ternary phases.
    for d in range(4, 81):
        C = -pow(2**d, -1, 9) % 9
        if C % 2 == 0:
            C += 9
        for j in range(8):
            phase = C+18*j
            w = (2**d*phase+1)//9
            assert w % 16 == 9 and M.NORMAL.valuation2(9*w-1) == d
            data = M.local_plan(w)
            synthetic_branches[data['branch']] += 1
            synthetic += 1

    recursive = []
    for w in range(9, 4096, 16):
        data = M.five_plan(w)
        assert all(v % 8 == 5 for v in data['coefficients'])
        recursive.append((w, len(data['nine_nodes']), len(data['coefficients'])))

    expect_error(ValueError, lambda: M.local_plan(5))
    expect_error(RuntimeError, lambda: M.five_plan(9, max_nodes=0))
    nine = M.five_plan(9)
    assert nine['coefficients'] == {5: -1, 21: 1}
    expect_error(ValueError, lambda: M.compile_five_plan(nine, {}))
    expect_error(ValueError, lambda: M.compile_five_plan(nine, {5: {}, 21: {}}))

    certificates = []
    saved = None
    for w in [9, 25, 57, 121, 313, 569, 1321, 1561, 2041, 4073]:
        data = M.five_plan(w)
        supplied = {u: supplied_pair(u) for u in data['coefficients']}
        result = M.compile_five_plan(data, supplied)
        assert M.divergence(result) == M.pair_source(w)
        certificates.append(dict(seed=w, nine_nodes=len(data['nine_nodes']),
                                 inputs=len(supplied), rows=len(result),
                                 current_sha256=digest(result)))
        if w == 9:
            saved = dict(plan=data, inputs=supplied, current=result)

    elapsed = time.perf_counter()-started
    receipt = dict(
        status='PASS',
        claim_scope='Finite exact checks of a conditional W9-to-W5 compiler; no universal W5 supply',
        command='python3 experiments/residual_progress/w9_closure/check_w9_closure.py',
        local=dict(domain='w=9 modulo16, 9<=w<65536', count=sum(branches.values()),
                   branches=dict(branches), maximum_nonzero_requests=maximum_requests),
        low_valuation_affine_table=dict(formulas={str(d): list(row) for d, row in affine_table.items()},
                                        counts=dict(affine_table_checks)),
        tripling_bound=dict(domain='all odd 1<=z<8192', count=4096),
        high_valuations=dict(domain='4<=d<=80, eight admissible odd C phases each',
                             count=synthetic, branches=dict(synthetic_branches)),
        recursive=dict(domain='w=9 modulo16, 9<=w<4096', count=len(recursive),
                       maximum_nine_nodes=max(row[1] for row in recursive),
                       maximum_five_inputs=max(row[2] for row in recursive)),
        rejection_checks=4,
        actual_substitutions=certificates,
        actual_fixture_cap_per_seed=10000,
        elapsed_seconds=round(elapsed, 4),
    )
    return receipt, saved


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write', action='store_true', help='Refresh scoped receipt and current fixture')
    args = parser.parse_args()
    receipt, saved = run()
    if args.write:
        (HERE / 'w9_closure_audit.json').write_text(json.dumps(receipt, indent=2)+'\n')
        fixture = dict(seed=9, coefficients=saved['plan']['coefficients'],
                       local_current=saved['plan']['current'], inputs=saved['inputs'])
        (HERE / 'w9_inputs.json').write_text(json.dumps(fixture, indent=2)+'\n')
        with (HERE / 'w9_current.csv').open('w', newline='') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            writer.writerow(['odd_state', 'integer_current'])
            writer.writerows(sorted(saved['current'].items()))
    else:
        old = json.loads((HERE / 'w9_closure_audit.json').read_text())
        for key in receipt:
            if key != 'elapsed_seconds':
                assert receipt[key] == old[key], key
        fixture = json.loads((HERE / 'w9_inputs.json').read_text())
        assert fixture['seed'] == 9
        inputs = {int(u): {int(x): c for x, c in rows.items()}
                  for u, rows in fixture['inputs'].items()}
        assert inputs == saved['inputs']
        assert {int(u): c for u, c in fixture['coefficients'].items()} == saved['plan']['coefficients']
        assert {int(x): c for x, c in fixture['local_current'].items()} == saved['plan']['current']
        with (HERE / 'w9_current.csv').open(newline='') as stream:
            rows = {int(row['odd_state']): int(row['integer_current']) for row in csv.DictReader(stream)}
        assert rows == saved['current'] and M.divergence(rows) == M.pair_source(9)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
