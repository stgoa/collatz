"""Bounded exact replay of maximal selected cycles and all exit interfaces."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import selected_exit as M

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def clock_check(data):
    x = data['rank']
    for _ in range(data['quotient_length']):
        x = M.NORMAL.quotient_step(x)
    assert x == data['minimum']


def finite_absorption(seed, cap=10000):
    current,x = {},seed
    for _ in range(cap+1):
        if x == 1:
            assert M.divergence(current) == M.atoms((1,seed))
            return current
        if x in current or len(current) == cap or x.bit_length() > 4096:
            raise RuntimeError('Designated finite input unresolved: '+str(seed))
        current[x] = 1
        x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    exits, categories = [],Counter()
    for e in range(6,17):
        for s in range(1,64,2):
            q = 81*2**e*s-17
            w = (2*q+1)//3
            plan = M.exit_plan(w)
            data = plan['parameters']
            assert data['prefix']['repeats'] == 0
            assert data['exit']['e'] == e
            clock_check(data)
            tail = data['exit']
            categories[str((e,plan['status']))] += 1
            exits.append([w,e,tail['first']['d'],
                          None if tail['second'] is None else tail['second'].get('d'),
                          plan['status'],data['endpoint'],digest(plan['current'])])

    cycles = []
    for r in range(1,9):
        for e in range(6,17):
            for s in (1,3,17):
                q = 81*2**(11*r+e)*s-17
                data = M.cycle_prefix(q)
                assert data['repeats'] == r and data['exit_exponent'] == e
                assert data['endpoint'] == 81*3**(7*r)*2**e*s-17
                x,current = q,{}
                for _ in range(r):
                    block = M.CYCLE.one_cycle(x)
                    current = M.combine((1,current),(1,block['current']))
                    x = block['endpoint']
                assert current == data['current']
                cycles.append([r,e,s,x,digest(current)])

    forward = M.load('exit_audit_forward','selected_forward/selected_forward.py')
    inverse = M.load('exit_audit_inverse','selected_inverse/selected_inverse.py')
    families = []
    for r in list(range(13))+[16,32,64]:
        for extra in (0,4):
            for j in (0,3):
                for fresh in (False,True):
                    data = M.family(r,j,depth=2*r+5+extra,avoid_inverse=fresh)
                    plan = M.exit_plan(data['seed'])
                    detail = plan['parameters']
                    assert plan['status'] == 'descending'
                    assert detail['prefix']['repeats'] == r
                    assert detail['exit']['e'] == 12 and detail['exit']['second']['d'] == data['d']
                    assert detail['endpoint'] == data['endpoint']
                    assert detail['quotient_length'] == data['quotient_clock']
                    assert data['seed'] == data['seed_residue']+j*data['seed_period']
                    clock_check(detail)
                    path,current = M.ordinary_path(data['q'],data['left_clock'])
                    assert path[-1] == M.NORMAL.step(data['endpoint'])
                    assert M.combine((1,current),(-1,{data['endpoint']:1})) == detail['current']
                    assert M.CYCLE.UNION.one_step(data['seed']) is None
                    if fresh:
                        assert forward.one_step(data['seed']) is None
                        assert inverse.one_step(data['seed']) is None
                        assert inverse.parameters(data['seed'],4)['h'] == 0
                        assert inverse.parameters(data['seed'],8)['h'] == 0
                    families.append(dict(data,rows=len(plan['current']),requests=len(plan['coefficients']),
                                         current_hash=digest(plan['current'])))

    # A concrete failed sufficient bound survives: no whole-phase closure claim.
    q = 81*2**(11*10+16)-17
    unresolved = M.exit_plan((2*q+1)//3)
    assert unresolved['status'] == 'unresolved'
    assert unresolved['parameters']['minimum'] > q

    supplied, actual, tables = {},[],[]
    for r in (0,1,2):
        data = M.family(r,avoid_inverse=True)
        plan = M.exit_plan(data['seed'])
        for u in plan['coefficients']:
            if u not in supplied:
                supplied[u] = M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current = M.compile_plan(plan,supplied)
        assert M.divergence(current) == M.T.pair_source(data['seed'])
        actual.append(dict(seed=data['seed'],repeats=r,rows=len(current),
                           requests=sorted(plan['coefficients'].items()),current_hash=digest(current)))
        tables.append(dict(seed=data['seed'],current=sorted(current.items()),
                           supplied={u:sorted(supplied[u].items()) for u in plan['coefficients']}))

    failures = 0
    good = M.exit_plan(M.family(0)['seed'])
    for call in (lambda:M.family(-1),lambda:M.family(1,depth=5),lambda:M.family(1,depth=8),
                 lambda:M.exit_plan(13),lambda:M.exit_interface(81*2**17-17),
                 lambda:M.compile_plan(good,{}),
                 lambda:M.compile_plan(good,{u:{} for u in good['coefficients']}),
                 lambda:M.compile_plan(unresolved,{})):
        try:
            call()
        except ValueError:
            failures += 1
        else:
            raise AssertionError('Invalid input was accepted')

    return dict(status='PASS',scope='Complete finite exit interface and strict-rho progressions; universal input supply open',
                exit_cases=len(exits),exit_hash=digest(exits),categories=dict(sorted(categories.items())),
                maximal_cycle_cases=len(cycles),cycle_hash=digest(cycles),
                long_families=families,fresh_dispatcher_exclusions=sum(x['avoid_inverse'] for x in families),
                unresolved_example=dict(seed=unresolved['seed'],rank=q,
                                        endpoint=unresolved['parameters']['endpoint'],
                                        minimum=unresolved['parameters']['minimum']),
                actual_substitutions=actual,actual_current_tables=tables,
                distinct_supplied_inputs=len(supplied),supplied_hash=digest(supplied),rejection_checks=failures,
                caps=dict(exit_e=[6,16],exit_s=[1,63],maximal_repeats=[1,8],family_max_repeats=64,
                          input_discovery_steps=10000,input_discovery_bits=4096),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('selected_exit.py','check_selected_exit.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(audit(),sort_keys=True))
    path = HERE/'selected_exit_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: 352 complete exits, 264 maximal-cycle cases, 128 progression cases, 3 supplied-input conversions')


if __name__ == '__main__':
    main()
