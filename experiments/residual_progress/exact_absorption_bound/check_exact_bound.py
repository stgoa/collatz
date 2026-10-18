"""Bounded replay of exact absorption-rank excess and the complete a5d3 rule."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import exact_bound as M

HERE = Path(__file__).resolve().parent
OLD = M.load('sharp_check_union','selected_rules/selected_rules.py')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorb(seed):
    current,x = {},seed
    for _ in range(10001):
        if x == 1:
            assert M.RANK.divergence(current) == M.RANK.atoms((1,seed))
            return current
        if x in current or len(current)==10000 or x.bit_length()>1024:
            raise RuntimeError('Demonstration input exceeded its finite cap')
        current[x]=1
        x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    seeds,exceptions = [],0
    for s in range(1,32768,2):
        plan=M.absorption_plan(s)
        bound=plan['sharp_bound']
        exceptions+=bound['exception'] is not None
        seeds.append([s,bound,sorted(plan['coefficients'].items())])

    nines=[]
    for v in range(9,32768,16):
        plan=M.RANK.nine_plan(v)
        n=3*v;bound=M.absorption_bound(n)
        high={u:c for u,c in plan['coefficients'].items() if M.RANK.rho(u)>n}
        expected={bound['exception']['index']:1} if bound['exception'] else {}
        assert high==expected
        assert all(M.RANK.rho(u)<n for u in plan['coefficients'] if u not in high)
        nines.append([v,high,digest(plan['current']),sorted(plan['coefficients'].items())])

    family,counts=[],Counter()
    for m in range(2048):
        w=437+512*m;plan=M.fifth_plan(w)
        strict=all(M.RANK.rho(u)<3*w for u in plan['coefficients'])
        assert strict==(plan['status']=='descending')
        assert plan['parameters']['ordinary_left_length']==6
        assert plan['parameters']['ordinary_right_length']==1
        assert plan['parameters']['quotient_length']==5
        counts[plan['status']]+=1
        family.append([m,plan['status'],plan['sharp_bound'],digest(plan['current']),
                       sorted(plan['coefficients'].items())])

    fresh=[]
    for k in list(range(64))+[2**j for j in (8,16,32,64,128)]:
        data=M.fresh_family(k);w=data['seed'];plan=M.fifth_plan(w)
        assert OLD.one_step(w) is None
        assert w%9==7 and plan['status']=='descending'
        m=data['index']*576+7
        assert plan['family_index']==m
        z=2147+157464*k
        assert 3*z%8==1 and M.NORMAL.canonical(3*z)
        fresh.append([k,w,digest(plan['current']),sorted(plan['coefficients'].items())])

    retained=M.fifth_plan(44981)
    assert retained['status']=='unresolved'
    assert {u:c for u,c in retained['coefficients'].items() if M.RANK.rho(u)>=134943}=={96069:1}

    supplied_all,tables={},[]
    for w in (4021,298933,593845):
        plan=M.fifth_plan(w);supplied={}
        for u in plan['coefficients']:
            if u not in supplied_all:
                supplied_all[u]=M.RANK.combine((1,absorb(3*u)),(-1,absorb(u)))
            supplied[u]=supplied_all[u]
        current=M.compile_plan(plan,supplied)
        assert M.RANK.divergence(current)==M.RANK.T.pair_source(w)
        tables.append(dict(plan=plan,supplied=supplied,current=current))

    failures=0
    for action in (lambda:M.absorption_bound(0),lambda:M.absorption_bound(2),
                   lambda:M.fifth_plan(5),lambda:M.fresh_family(-1),
                   lambda:M.compile_plan(retained,{}),
                   lambda:M.compile_plan(tables[0]['plan'],{}),
                   lambda:M.compile_plan(tables[0]['plan'],{u:{} for u in tables[0]['supplied']})):
        try:action()
        except (ValueError,RuntimeError):failures+=1
        else:raise AssertionError('Invalid or missing premise accepted')

    return dict(status='PASS',scope='Exact request-excess classification and conditional original-rho family; no universal supply',
                absorption_seeds=len(seeds),exceptional_normalized_seeds=exceptions,seed_hash=digest(seeds),
                nine_inputs=len(nines),nine_hash=digest(nines),
                fifth_inputs=len(family),fifth_counts=dict(counts),fifth_hash=digest(family),
                fresh_progression_cases=len(fresh),fresh_hash=digest(fresh),
                retained_failure=dict(seed=44981,child=96069,parent_rank=134943,child_rank=144103),
                actual_substitutions=tables,distinct_supplied_pairs=len(supplied_all),
                rejection_checks=failures,caps=dict(seed_upper_bound=32768,fifth_count=2048,input_steps=10000,input_bits=1024),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('exact_bound.py','check_exact_bound.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    data=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'exact_bound_audit.json'
    if args.write_receipt:path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert data==json.loads(path.read_text()),'Receipt differs; inspect before refreshing'
    print('PASS: exact absorption excess, complete fifth-family rho test and actual supplied currents')


if __name__=='__main__':main()
