"""Replay the exact even-exit cone and its supplied finite certificates."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
from types import ModuleType
import even_exit_history as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = spec_from_file_location('even_exit_old17', HERE.parent/'resolved_rules/resolved_rules.py')
OLD = module_from_spec(spec)
spec.loader.exec_module(OLD)
spec = spec_from_file_location('even_exit_old48', HERE.parent/'nonselected_forward/nonselected_forward.py')
FORWARD = module_from_spec(spec)
spec.loader.exec_module(FORWARD)
ARROW_CAP, BIT_CAP = 10000, 1024


def rows(current):
    return [[x,c] for x,c in sorted(current.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def step(x):
    if x == 1:
        return 1
    value = 3*x+1
    return value//(value & -value)


def v3(x):
    count = 0
    while x % 3 == 0:
        x //= 3
        count += 1
    return count


def div(current):
    out = Counter()
    for x,c in current.items():
        assert type(x) is int and x > 1 and x % 2 and type(c) is int and c
        out[x] += c
        if step(x) != 1:
            out[step(x)] -= c
    return {x:c for x,c in out.items() if c}


def boundary(data):
    out = Counter({3*data['seed']:1,data['seed']:-1})
    for v,c in data['coefficients'].items():
        out[3*v] -= c
        out[v] += c
    return {x:c for x,c in out.items() if x != 1 and c}


def arithmetic(data):
    H,b,t,q,n,y = (data[k] for k in ('H','b','t','rank','n','y'))
    assert q == 2**H*t-1 and q % 3 == 0
    assert 4**b*data['u'] == 3**(H-1)*t-1
    assert n == 3**b*data['u'] and n % 8 == 1 and y == (3*n+1)//4
    lam = Fraction(3**(H+b),2**(H+2*b+2))
    assert y-q == (lam-1)*q+lam+Fraction(1,4)-Fraction(3,4)**(b+1)
    assert (y < q) == (lam < 1) == data['raw_descending']
    assert y != q and data['ordinary_clocks'] == [H+b+1,1]
    if 'D' in data:
        assert v3(q) == data['D'] and q//3**data['D'] % 3 == data['ternary_unit']
        assert data['t_period'] == 2**(2*b+3)*3**(data['D']+1)
        assert data['seed_period'] == 2**H*data['t_period']//3


def full(data):
    checked = M.plan(data['H'],data['b'],data['t'])
    arithmetic(checked)
    assert div(checked['current']) == boundary(checked)
    left,right = checked['rank'],checked['y']
    current = Counter()
    for _ in range(checked['ordinary_clocks'][0]):
        if left != 1:
            current[left] += 1
        left = step(left)
    for _ in range(checked['ordinary_clocks'][1]):
        if right != 1:
            current[right] -= 1
        right = step(right)
    current = {x:c for x,c in current.items() if c}
    assert current == checked['comparison'] and left == right == checked['ordinary_meeting']
    assert div(current) == {checked['rank']:1,checked['y']:-1}
    x = checked['rank']
    for _ in range(checked['quotient_length']):
        x = M.N.quotient_step(x)
    assert x == checked['terminal'] == M.N.normal_form(checked['y'])
    if checked['raw_descending']:
        assert all(M.B.rho(v) < checked['rank'] for v in checked['coefficients'])
    # Same entire current as the old formal R48 comparison, after the
    # deterministic W9 substitutions. No new orbit identity is inferred.
    if checked['H'] <= 12 and checked['b'] <= 12:
        old = FORWARD.forward_plan(checked['seed'])
        high,low = FORWARD.INVERSE.absorption_five_plan(checked['y']),FORWARD.INVERSE.absorption_five_plan(checked['seed'])
        expected_current = M.combine((1,current),(1,high['current']),(-1,low['current']))
        expected_coeff = M.combine((1,high['coefficients']),(-1,low['coefficients']))
        assert old['current'] == expected_current and old['coefficients'] == expected_coeff
        if checked['raw_descending']:
            assert all(FORWARD.rho(v) < checked['rank'] for v in expected_coeff)
    return checked


def absorption(x):
    current = {}
    while x != 1:
        if len(current) >= ARROW_CAP or x.bit_length() > BIT_CAP or x in current:
            raise RuntimeError('Designated finite supply exceeded the stated cap')
        current[x] = 1
        x = step(x)
    return current


def pair_supply(w):
    current = M.combine((1,absorption(3*w)),(-1,absorption(w)))
    assert div(current) == {3*w:1,w:-1}
    return current


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('Expected a domain, cap, or supply rejection')


def sources():
    pending,seen = [M,OLD,FORWARD],set()
    files = {Path(__file__).resolve(),HERE/'EVEN_EXIT_HISTORY.md'}
    while pending:
        module = pending.pop()
        if id(module) in seen:
            continue
        seen.add(id(module))
        filename = getattr(module,'__file__',None)
        if not filename:
            continue
        path = Path(filename).resolve()
        if not path.is_relative_to(ROOT):
            continue
        files.add(path)
        pending.extend(x for x in vars(module).values() if isinstance(x,ModuleType))
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}


def audit(stored=None):
    cells,plans,minimal,old = [],[],[],[]
    for H in range(3,13):
        for b in range(1,17):
            for D,unit,index in ((1,1,0),(1,2,1),(2,1,0),(3,2,7)):
                data = M.family(H,b,D,unit,index)
                arithmetic(data)
                successor = M.family(H,b,D,unit,index+1)
                assert successor['t']-data['t'] == data['t_period']
                assert successor['seed']-data['seed'] == data['seed_period']
                cells.append([H,b,D,unit,index,data['t'],data['raw_descending']])
            if b in (1,2,4,8,16):
                data = full(M.family(H,b,2,1))
                plans.append([H,b,data['seed'],data['status'],data['ordinary_clocks'],
                              digest(rows(data['current'])),rows(data['coefficients'])])
    for H in list(range(4,33))+[64,128,256]:
        b = M.least_closing_half(H)
        assert 1 <= b <= 2*H and 3**(H+b) < 2**(H+2*b+2)
        assert b == 1 or 3**(H+b-1) > 2**(H+2*(b-1)+2)
        for D in (1,2,8,32):
            for unit in (1,2):
                data = M.minimal_family(H,D,unit)
                arithmetic(data)
                assert data['n'] > data['rank'] > data['y']
                minimal.append([H,b,D,unit,data['t']])
    for index in list(range(32))+[2**32,2**64]:
        data = M.old_unrecognized_family(index)
        assert OLD.one_step(data['seed']) is None
        assert FORWARD.forward_plan(data['seed'])['status'] != 'descending'
        arithmetic(data)
        old.append([index,data['seed'],data['rank'],data['y']])
    # Completeness of the CRT cell for modest positive t, independent of CRT
    # generation. A local modular condition is tested in both directions.
    memberships = 0
    for H in range(3,8):
        for b in range(1,4):
            for t in range(1,1024,2):
                q,num = 2**H*t-1,3**(H-1)*t-1
                valid = q % 3 == 0 and num % 4**b == 0
                if valid:
                    u = num//4**b
                    valid = u > 0 and u % 2 == 1 and 3**b*u % 8 == 1
                if valid:
                    D = v3(q); unit = q//3**D % 3
                    cell = M.family(H,b,D,unit)
                    assert (t-cell['t_residue']) % cell['t_period'] == 0
                    memberships += 1
                else:
                    reject(lambda H=H,b=b,t=t:M.parameters(H,b,t))
    outside = full(M.parameters(5,1,29))
    assert outside['status'] == 'outside_raw_cone' and outside['y'] > outside['rank']
    assert M.N.normal_form(step(outside['y'])) == 495 < outside['rank']
    assert all(M.B.rho(v) < outside['rank'] for v in outside['coefficients'])
    reject(lambda:M.compile_plan(outside,{}))

    demonstrations = []
    for i,index in enumerate((0,1,2)):
        data = M.old_unrecognized_family(index)
        if stored is None:
            supplied = {v:pair_supply(v) for v in data['coefficients']}
        else:
            supplied = {int(v):dict(table) for v,table in stored['demonstrations'][i]['supplied'].items()}
        assert set(supplied) == set(data['coefficients'])
        for v,table in supplied.items():
            assert div(table) == {3*v:1,v:-1}
        compiled = M.compile_plan(data,supplied)
        assert div(compiled) == {3*data['seed']:1,data['seed']:-1}
        first = next(iter(supplied))
        reject(lambda:M.compile_plan(data,{}))
        reject(lambda:M.compile_plan(data,{**supplied,first:{}}))
        reject(lambda:M.compile_plan(data,{**supplied,first:{3:True}}))
        demonstrations.append(dict(seed=data['seed'],rank=data['rank'],y=data['y'],
                                   ordinary_clocks=data['ordinary_clocks'],quotient_length=data['quotient_length'],
                                   current=rows(data['current']),coefficients=rows(data['coefficients']),
                                   supplied={str(v):rows(table) for v,table in sorted(supplied.items())},
                                   output=rows(compiled),output_rows=len(compiled)))
    invalid = [lambda:M.parameters(2,1,55),lambda:M.parameters(True,1,55),
               lambda:M.parameters(4,0,55),lambda:M.parameters(4,1,54),
               lambda:M.parameters(4,1,0),lambda:M.parameters(4,1,1),
               lambda:M.parameters(4,1,55,8),lambda:M.family(4,1,0),
               lambda:M.family(4,1,1,0),lambda:M.family(4,1,1,True),
               lambda:M.family(4,1,1,index=-1),lambda:M.family(4,1,1,max_bits=8),
               lambda:M.minimal_family(3,1),lambda:M.least_closing_half(4,8),
               lambda:M.least_closing_half(10**9),lambda:M.old_unrecognized_family(-1),
               lambda:M.old_unrecognized_family(True),lambda:M.compile_plan(dict(M.plan(4,1,55),current={3:True}),{})]
    for call in invalid:
        reject(call)
    return dict(schema=1,status='PASS',scope='Exact raw-target cone; terminal currents remain supplied premises.',
                arithmetic_cells=len(cells),arithmetic_hash=digest(cells),full_plans=len(plans),full_hash=digest(plans),
                minimal_cells=len(minimal),minimal_hash=digest(minimal),crt_memberships=memberships,
                old17_cases=old,outside_cone_control=dict(seed=outside['seed'],rank=outside['rank'],y=outside['y'],
                current=rows(outside['current']),coefficients=rows(outside['coefficients'])),
                demonstrations=demonstrations,rejections=len(invalid)+10,
                supply_caps=dict(ordinary_arrows=ARROW_CAP,state_bits=BIT_CAP),source_hashes=sources())


def main():
    assert not sys.flags.optimize, 'Run without -O'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    path = HERE/'even_exit_history_audit.json'
    stored = None if args.write_receipt else json.loads(path.read_text())
    data = audit(stored)
    serialized = json.dumps(data,indent=2,sort_keys=True)+'\n'
    if args.write_receipt:
        path.write_text(serialized)
    else:
        assert json.loads(serialized) == stored, 'Receipt mismatch; investigate before refreshing'
    print('PASS: even-exit history cone; '+json.dumps(dict(
        cells=data['arithmetic_cells'],full_plans=data['full_plans'],minimal_cells=data['minimal_cells'],
        crt_memberships=data['crt_memberships'],old17_cases=len(data['old17_cases']),
        supplied_rows=[x['output_rows'] for x in data['demonstrations']],rejections=data['rejections']),sort_keys=True))


if __name__ == '__main__':
    main()
