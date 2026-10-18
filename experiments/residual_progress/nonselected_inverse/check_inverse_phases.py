"""Bounded audit of both complete base phases, signs and supplied substitution."""
import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import inverse_phases as M

HERE = Path(__file__).resolve().parent


def digest(rows):
    return hashlib.sha256(json.dumps(sorted(rows.items()), separators=(',', ':')).encode()).hexdigest()


def ordinary_clock(w, k, data):
    p, b, h = data['lower'], data['predecessor'], data['h']
    x = p
    for _ in range(h):
        assert M.NORMAL.valuation2(3*x+1) == 1
        x = M.NORMAL.step(x)
    assert x == b
    q = 3*w
    a = M.NORMAL.valuation2(q+1)
    clocks = (h+2, 1) if k == 8 else (h+a+2, a+1)
    assert M.NINE.prefix(p, clocks[0])[0] == M.NINE.prefix(q, clocks[1])[0]


def capped_absorption(seed, cap=10000):
    seen, rows, x = set(), Counter(), seed
    for _ in range(cap):
        if x == 1:
            result = M.NINE.clean(rows)
            assert M.divergence(result) == M.atoms((1, seed))
            return result
        if x in seen:
            raise RuntimeError('A nonabsorbing cycle was encountered in a finite fixture')
        seen.add(x)
        rows[x] += 1
        x = M.NORMAL.step(x)
    raise RuntimeError('Fixture cap reached; no absorption claim')


def supplied_pair(w):
    return M.combine((1, capped_absorption(3*w)), (-1, capped_absorption(w)))


def expect_error(kind, action):
    try:
        action()
    except kind:
        return
    raise AssertionError('Expected explicit rejection')


def audit():
    classes, status = Counter(), Counter()
    eligible = active = index_growth = tautologies = 0
    for w in range(5, 65536, 8):
        if not M.eligible(w):
            continue
        eligible += 1
        rows = [M.parameters(w, k) for k in (4, 8)]
        assert sum(p['h'] > 0 for p in rows) == (w % 3 != 0)
        assert M.decreasing_domain(w) == any(p['rank_shrinking'] for p in rows)
        assert M.index_decreasing_domain(w) == any(p['index_shrinking'] for p in rows)
        for p in rows:
            k = p['k']
            if not p['h']:
                continue
            active += 1
            data = M.pair_plan(w, k)
            classes[f'k{k},h{p["h"]},p{p["residue"]}'] += 1
            status[data['status']] += 1
            if data['status'] == 'descending':
                M.RANK.validate_step(w, data)
                index_growth += p['child'] > w
            if p['child_domain'] == 'W9':
                assert data['coefficients'] == {w: 1} and not data['current']
                tautologies += 1
    synthetic = []
    for k in (4, 8):
        for h in range(1, 25):
            for residue in (0, 1):
                Cmod3 = (residue+1)*pow(2**(h+1), -1, 3) % 3
                modulus = 3**(h+1)
                ternary = (3**h*Cmod3-1)*pow(k, -1, modulus) % modulus
                first = 13+32*((ternary-13)*pow(32, -1, modulus) % modulus)
                for index in (0, 1, 7):
                    w = first+32*modulus*index
                    p = M.parameters(w, k)
                    assert (p['h'], p['residue']) == (h, residue)
                    ordinary_clock(w, k, p)
                    data = M.pair_plan(w, k)
                    if data['status'] == 'descending':
                        M.RANK.validate_step(w, data)
                    synthetic.append(dict(k=k, h=h, residue=residue, index=index,
                                          w=w, child=p['child'], status=data['status'],
                                          sha256=digest(data['current'])))
    growth = []
    for w in (1613, 17101):
        data = M.decreasing_plan(w)
        v = data['parameters']['child']
        assert v > w and M.critical_rank(v) < M.critical_rank(w)
        growth.append(dict(w=w, child=v, rank=M.critical_rank(w), child_rank=M.critical_rank(v)))
    conversions, fixtures = [], {}
    for w in (101, 1613, 3493, 17101):
        data = M.decreasing_plan(w)
        supplied = {u: supplied_pair(u) for u in data['coefficients']}
        current = M.compile_plan(data, supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        conversions.append(dict(w=w, inputs=len(supplied), rows=len(current), sha256=digest(current)))
        if w == 1613:
            fixtures = dict(seed=w, plan=data, inputs=supplied, current=current)
    closures = []
    for w in (101, 1613, 3493, 17101):
        data = M.RANK.close_plan(w, lambda x: M.decreasing_plan(x) if M.decreasing_domain(x) else None,
                                 max_nodes=1000)
        assert all(not M.decreasing_domain(u) for u in data['coefficients'])
        closures.append(dict(w=w, expanded=data['expanded'], leaves=data['coefficients']))
    expect_error(ValueError, lambda: M.decreasing_plan(77))
    expect_error(ValueError, lambda: M.compile_plan(M.pair_plan(77, 4), {}))
    expect_error(ValueError, lambda: M.compile_plan(M.decreasing_plan(101), {}))
    expect_error(ValueError, lambda: M.parameters(21, 4))
    return dict(status='PASS', scope='Complete base-ray phase reduction; universal remaining inputs open',
                W5_candidates=8192, nonselected_candidates=eligible, positive_h_plans=active,
                classes=dict(sorted(classes.items())), statuses=dict(status),
                exact_zero_self_plans=tautologies, rank_decrease_with_index_growth=index_growth,
                symbolic_cases=synthetic, increasing_index_examples=growth,
                actual_substitutions=conversions, fixture_absorption_cap=10000,
                formal_closures=closures, rejection_checks=4), fixtures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result, fixture = audit()
    receipt = HERE/'nonselected_inverse_audit.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2)+'\n')
        inputs = dict(seed=fixture['seed'], coefficients=fixture['plan']['coefficients'],
                      local_current=fixture['plan']['current'], inputs=fixture['inputs'])
        (HERE/'w1613_inputs.json').write_text(json.dumps(inputs, indent=2)+'\n')
        with (HERE/'w1613_current.csv').open('w', newline='') as out:
            writer = csv.writer(out, lineterminator='\n')
            writer.writerow(('state', 'current'))
            writer.writerows(sorted(fixture['current'].items()))
    else:
        # Round-trip removes harmless integer-key differences in nested mappings.
        assert json.loads(receipt.read_text()) == json.loads(json.dumps(result))
        saved = json.loads((HERE/'w1613_inputs.json').read_text())
        inputs = {int(u): {int(x): c for x, c in rows.items()} for u, rows in saved['inputs'].items()}
        assert inputs == fixture['inputs'] and saved['seed'] == 1613
        assert {int(x): c for x, c in saved['local_current'].items()} == fixture['plan']['current']
        assert {int(x): c for x, c in saved['coefficients'].items()} == fixture['plan']['coefficients']
        with (HERE/'w1613_current.csv').open() as source:
            stored = {int(row['state']): int(row['current']) for row in csv.DictReader(source)}
        assert stored == fixture['current']
    print(f'PASS: {result["nonselected_candidates"]} nonselected inputs; '
          f'{result["positive_h_plans"]} complete plans; {len(result["symbolic_cases"])} symbolic cases; '
          f'{result["exact_zero_self_plans"]} exact self-returns; four supplied substitutions')


if __name__ == '__main__':
    main()
