"""Bounded arithmetic and actual-current checks of the conditional compilers."""
import argparse
import hashlib
import json
from pathlib import Path
import tripling as T

HERE = Path(__file__).resolve().parent


def digest(rows):
    return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def absorption_current(x, step_cap=10000, bit_cap=512):
    """Finite demonstration only; a cap or cycle raises an unresolved error."""
    start, seen, current = x, set(), {}
    for _ in range(step_cap+1):
        if x == 1:
            assert T.divergence(current) == T.atoms((1, start))
            return current
        if x in seen or x.bit_length() > bit_cap or len(seen) == step_cap:
            raise RuntimeError('Unresolved bounded demonstration: '+str(start))
        seen.add(x)
        current[x] = current.get(x, 0)+1
        x = T.step(x)
    raise AssertionError('Unreachable cap branch')


def audit():
    local_rows = []
    for x in range(1, 16384, 2):
        for mode, advance in [('static', T.static_step), ('critical', T.critical_step)]:
            data = advance(x)
            if data['pair'] is not None and mode == 'critical':
                assert T.critical_domain(data['pair'])
            local_rows.append([mode, x, data['canonical'], data['lower'],
                               data['pair'], data['branch'], sorted(data['current'].items())])

    domain = [w for w in range(1, 32768, 2) if T.critical_domain(w)]
    images = [[w, T.critical_image(w)] for w in domain]
    assert len({q for _, q in images}) == len(domain)
    for w, q in images:
        assert T.critical_inverse(q) == w
    critical = [q for q in range(1, 32768, 2) if T.critical(q)]
    inverses = [[q, T.critical_inverse(q)] for q in critical]
    for q, w in inverses:
        assert T.critical_image(w) == q

    plans = []
    for x in range(1, 2048, 2):
        for mode in ['static', 'critical']:
            data = T.plan(x, mode)
            if mode == 'static' and data['pairs']:
                r = len(data['pairs'])
                assert 2*3**(r-1) <= 2**(r-1)*(x-1)
            plans.append([x, mode, data['pairs'],
                          [[r['seed'], r['lower'], r['branch']] for r in data['steps']],
                          sorted(data['current'].items())])

    sample_seeds = [1,3,7,11,17,23,27,31,41,47,63,95,111,255,659,1699,4755,5795,8191,65535]
    pair_inputs, compiled, tables = {}, [], []
    for x in sample_seeds:
        for mode in ['static', 'critical']:
            data = T.plan(x, mode)
            for w in data['pairs']:
                if w not in pair_inputs:
                    pair_inputs[w] = T.combine((1, absorption_current(3*w)),
                                               (-1, absorption_current(w)))
            result = T.compile_plan(data, pair_inputs)
            row = [x, mode, data['pairs'], len(result),
                   sum(abs(c) for c in result.values()), sorted(result.items())]
            compiled.append(row)
            if x in (27,31) and mode == 'critical':
                tables.append(dict(seed=x, mode=mode, pair_inputs=data['pairs'],
                                   current=[[u,c] for u,c in sorted(result.items())]))

    # A conditional plan must never silently turn an absent/incorrect premise
    # into a certificate, even when its arithmetic descent already terminates.
    rejecting_plan = T.plan(27)
    assert rejecting_plan['pairs']
    for supplied in [{}, {w: {} for w in rejecting_plan['pairs']}]:
        try:
            T.compile_plan(rejecting_plan, supplied)
        except ValueError:
            pass
        else:
            raise AssertionError('An unproved pair premise was accepted')

    return dict(status='PASS', clock='odd-only Syracuse, absorbing at1',
                scope='Written equivalence; no universal tripling current supplied',
                local_step_count=len(local_rows), local_step_hash=digest(local_rows),
                critical_domain_inputs=len(images), critical_domain_hash=digest(images),
                critical_inverse_inputs=len(inverses), critical_inverse_hash=digest(inverses),
                formal_plan_count=len(plans), formal_plan_hash=digest(plans),
                actual_compiled_examples=len(compiled), actual_compiled_hash=digest(compiled),
                supplied_pair_count=len(pair_inputs),
                supplied_pairs_hash=digest([[w, sorted(c.items())] for w,c in sorted(pair_inputs.items())]),
                actual_current_tables=tables,
                caps=dict(local_odd_max=16383, domain_odd_max=32767,
                          critical_odd_max=32767, plan_odd_max=2047,
                          sample_seeds=sample_seeds, demonstration_step_cap=10000,
                          demonstration_bit_cap=512),
                source_hashes={name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ['tripling.py', 'check_tripling.py']})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'tripling_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result, sort_keys=True, indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result, 'Receipt differs; inspect before regeneration'
    print('PASS: exact critical-domain bijection, conditional decreasing plans, and finite supplied-current examples')


if __name__ == '__main__':
    main()
