"""Bounded exact checks for the complete returning-phase forward interface."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
import returning_phase as R

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def finite_absorption(seed, cap=10000):
    """Capped discovery only for the explicitly recorded finite demonstration."""
    current, x = {}, seed
    for _ in range(cap+1):
        if x == 1:
            assert R.divergence(current) == R.atoms((1,seed))
            return current
        if x in current or len(current) == cap or x.bit_length() > 512:
            raise RuntimeError('Finite demonstration input unresolved: '+str(seed))
        current[x] = 1
        x = R.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    bounds = []
    for s in range(1,4096,2):
        plan = R.INVERSE.absorption_five_plan(s)
        index_bound = R.absorption_bound(s)['bound']
        rank_bound = R.absorption_rank_bound(s)['bound']
        assert all(u <= index_bound and R.rho(u) <= rank_bound for u in plan['coefficients'])
        assert all(8*R.rho(u) <= 9*s+5 for u in plan['coefficients'])
        bounds.append([s,[index_bound.numerator,index_bound.denominator],
                       [rank_bound.numerator,rank_bound.denominator],
                       sorted(plan['coefficients'].items())])

    plans, undo, low_counts, categories, accepted = [], [], Counter(), Counter(), []
    index_only = []
    for w in range(5,32768,8):
        if not R.returning(w):
            continue
        plan = R.forward_plan(w)
        p = plan['parameters']
        a, t, r = p['a'], p['t'], p['endpoint']
        categories[str(a)+':'+plan['status']] += 1
        low3 = a == 3 and not (R.NORMAL.canonical(r) and r % 4 == 3)
        low4 = a == 4 and not R.NORMAL.canonical(r)
        if low3 or low4:
            assert plan['status'] == 'descending'
            assert all(u < w for u in plan['coefficients'])
            low_counts[str(a)] += 1
        if a == 3:
            assert t % 108 == 35
        if a == 4:
            assert t % 108 == 85
        if plan['normalized_upper'] > 1 and plan['normalized_upper'] % 8 == 1:
            R.stratum_inequality(p,forward=True)
        last, _ = R.NINE.prefix(p['canonical_upper'],a-2)
        assert last % 8 == 1 and R.NORMAL.canonical(last)
        for length in range(a-2):
            undo.append(R.check_undo(w,length))
        if plan['status'] == 'descending':
            accepted.append(w)
        elif plan['index_status'] == 'descending':
            index_only.append([w,plan['rank'],[[u,R.rho(u),c] for u,c in sorted(plan['coefficients'].items())]])
        plans.append([w,plan['status'],a,r,plan['input_bound'],plan['input_rank_bound'],
                      sorted(plan['coefficients'].items()),digest(plan['current'])])

    families = []
    for a in list(range(3,33))+[64,128]:
        for j in [0,1,7]:
            f = R.sibling_family(a,j)
            plan = R.forward_plan(f['seed'])
            assert plan['status'] == 'descending'
            assert all(u < f['seed'] and R.rho(u) < plan['rank'] for u in plan['coefficients'])
            R.check_undo(f['seed'],a-3)
            assert Fraction(9*f['lowered_endpoint']+5,8) < plan['rank']
            families.append(dict(family=f,current_hash=digest(plan['current']),
                                 input_count=len(plan['coefficients']),
                                 max_input_rank=max(map(R.rho,plan['coefficients']),default=0)))

    supplied, demonstrations, tables = {}, [], []
    for w in accepted[:12]:
        plan = R.forward_plan(w)
        for u in plan['coefficients']:
            if u not in supplied:
                supplied[u] = R.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current = R.compile_forward_plan(plan,supplied)
        assert R.divergence(current) == R.TRIPLING.pair_source(w)
        demonstrations.append(dict(seed=w,rank=plan['rank'],
                                   requests=sorted(plan['coefficients'].items()),
                                   rows=len(current),current_hash=digest(current)))
        if len(tables) < 2:
            tables.append(dict(seed=w,current=sorted(current.items())))

    rejections = 0
    good = R.forward_plan(accepted[0])
    for invalid in ({},{u:{} for u in good['coefficients']}):
        try:
            R.compile_forward_plan(good,invalid)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('Missing or incorrect premises were accepted')
    unresolved = next(R.forward_plan(w) for w in range(5,32768,8)
                      if R.returning(w) and R.forward_plan(w)['status'] == 'unresolved')
    try:
        R.compile_forward_plan(unresolved,{})
    except ValueError:
        rejections += 1
    else:
        raise AssertionError('An unresolved arithmetic criterion was accepted')
    for value in (5,9,69):
        try:
            R.forward_plan(value)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('An out-of-domain input was accepted')

    return dict(status='PASS',scope='Complete conditional returning interface; strict-rank subdomains; finite actual substitutions',
                bounds_checked=len(bounds),bounds_hash=digest(bounds),
                returning_inputs=len(plans),categories=dict(sorted(categories.items())),
                low_valuation_complete_domain_samples=dict(sorted(low_counts.items())),
                plan_hash=digest(plans),undo_checks=len(undo),undo_hash=digest(undo),
                old_index_only_unresolved=index_only,
                crt_family_examples=families,
                actual_demonstrations=demonstrations,actual_current_tables=tables,
                supplied_pair_count=len(supplied),supplied_pairs_hash=digest(supplied),
                rejected_invalid_requests=rejections,
                caps=dict(bound_seeds_max=4095,returning_seed_max=32767,
                          family_a_values=list(range(3,33))+[64,128],family_indices=[0,1,7],
                          actual_demonstration_count=12,input_discovery_steps=10000,input_discovery_bits=512),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ['returning_phase.py','check_returning_phase.py']})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = audit()
    # JSON canonicalization keeps the regenerated receipt comparable to tuples
    # used internally for sorted sparse rows.
    result = json.loads(json.dumps(result,sort_keys=True))
    path = HERE/'returning_phase_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: complete returning interface, exact undo loops, rank descent, long-run families, and12 supplied-current compilations')


if __name__ == '__main__':
    main()
