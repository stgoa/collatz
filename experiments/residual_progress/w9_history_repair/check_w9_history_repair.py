"""Replay bounded W9 repairs, exact inverse undos and supplied currents."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType
import w9_history_repair as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ARROW_CAP, BIT_CAP = 10000, 2048


def rows(current):
    return [[x,c] for x,c in sorted(current.items())]


def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def step(x):
    if x == 1:
        return 1
    y = 3*x+1
    return y//(y & -y)


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


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError('Expected domain, cap, boundary or supply rejection')


def full(data):
    assert div(data['current']) == boundary(data)
    high = {v:c for v,c in data['coefficients'].items() if M.B.rho(v) >= data['threshold']}
    assert high == data['high']
    assert len(data['nodes']) <= 2
    assert (data['status'] == 'descending') == (not high)
    assert not high or (len(high) == 1 and next(iter(high)) % 8 == 5
                        and next(iter(high.values())) == 1)
    for i,node in enumerate(data['nodes']):
        assert div(node['current']) == boundary(node)
        assert M.N.valuation2(9*node['seed']-1) == node['d']
        if i:
            assert node['seed'] == data['nodes'][i-1]['leader']
            assert 16*node['seed'] < 9*data['nodes'][i-1]['seed']
    return [data['seed'],data['threshold'],data['status'],
            [[x['seed'],x['d'],x['decision_kind'],x['leader']] for x in data['nodes']],
            digest(rows(data['current'])),rows(data['coefficients'])]


def undo_full(w):
    data = M.even_upper_undo(w)
    assert div(data['current']) == boundary(data)
    assert div(data['inverse_plan']['current']) == boundary(data['inverse_plan'])
    x = 3*w
    for v in data['ordinary_inverse_word']:
        assert (3*x+1) % 2**v == 0 and (3*x+1) % 2**(v+1) != 0
        x = step(x)
    assert x == data['upper'] and data['inverse_origin'] == 3*w
    assert data['coefficients'][w] == 1
    # Independently form the lower ordinary path and the displayed result.
    x, lower = w, Counter()
    for _ in range(data['ordinary_inverse_length']):
        lower[x] += 1
        x = step(x)
    assert x == data['lower']
    a,b = M.B.absorption_plan(w),M.B.absorption_plan(x)
    current = M.combine((1,a['current']),(-1,dict(lower)),(-1,b['current']))
    coefficients = M.combine((1,{w:1}),(1,a['coefficients']),(-1,b['coefficients']))
    assert data['current'] == current and data['coefficients'] == coefficients
    return [w,data['d'],data['ordinary_inverse_word'],digest(rows(current)),rows(coefficients)]


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


def sources():
    pending,seen = [M],set()
    files = {Path(__file__).resolve(),HERE/'W9_HISTORY_REPAIR.md'}
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
    generic,thresholds,undos = [],[],[]
    kinds,terminal_types = set(),set()
    # Complete exact-depth binary cells, independently generated without the
    # R84 progression. Several original thresholds per source are checked.
    for d in list(range(4,21))+[32,64,128]:
        modulus = 2**(d+1)
        residue = ((1+2**d)*pow(9,-1,modulus)) % modulus
        for index in (0,1,2,3,7,15,2**32,2**96):
            w = residue+modulus*(4096+index)
            assert w % 16 == 9 and M.N.valuation2(9*w-1) == d
            for q in (((32*w)//33+1)|1, w, (5*w//4)|1, 2*w+1, 3*w):
                data = M.bounded_repair(w,q)
                generic.append(full(data))
                kinds.update(x['decision_kind'] for x in data['nodes'])
                for node in data['nodes']:
                    if node['forced'] is not None:
                        f = node['forced']
                        terminal_types.add('critical' if M.B.T.critical(f) else
                                           'one_mod8' if f % 8 == 1 else 'noncanonical')
            local = M.local_decision(w,w)
            if local['leader'] is not None:
                r = M.B.rho(local['leader'])
                for q in (r-2,r,r+2):
                    if q >= 11547 and q <= 3*w and 32*w < 33*q:
                        data = M.bounded_repair(w,q)
                        thresholds.append(full(data))
            if not d % 2 and not M.N.canonical(3*local['z']):
                undos.append(undo_full(w))
    # Explicit branch controls add small binary phases not forced by the
    # above depth-cell index list. This remains a prescribed finite check.
    for w in range(20009,21034,16):
        data = M.bounded_repair(w,w)
        generic.append(full(data))
        for node in data['nodes']:
            kinds.add(node['decision_kind'])
            if node['forced'] is not None:
                f = node['forced']
                terminal_types.add('critical' if M.B.T.critical(f) else
                                   'one_mod8' if f % 8 == 1 else 'noncanonical')
    assert kinds == {'odd_depth','even_noncanonical_upper','even_canonical_below',
                     'even_complementary_upper','even_forward_upper'}
    assert terminal_types == {'critical','one_mod8','noncanonical'}

    repairs,examined,skipped = [],0,0
    for k in list(range(512))+[869,1062,2917,5+16*2**32,5+16*2**96]:
        old = M.M.plan(k)
        examined += 1
        if old['status'] != 'unresolved' or old['leading'] % 16 != 9:
            skipped += 1
            continue
        data = M.repair_failed(k)
        record = full(data)
        # Independent complete signed substitution into the frozen R84 plan.
        current,coeff = old['current'],old['coefficients']
        for node in data['nodes']:
            current = M.combine((1,current),(1,node['current']))
            coeff = M.combine((1,coeff),(-1,{node['seed']:1}),(1,node['coefficients']))
        assert current == data['current'] and coeff == data['coefficients']
        repairs.append([k,record])
    assert any(len(row[1][3]) == 2 and row[1][2] == 'descending' for row in repairs)
    assert any(len(row[1][3]) == 2 and row[1][2] == 'unresolved' for row in repairs)
    strip_only = M.M.plan(8)
    assert strip_only['status'] == 'unresolved' and strip_only['leading'] % 16 == 9
    assert strip_only['normalizer']['F_exponent'] == 1
    assert not strip_only['normalizer']['selected_partner']
    assert 3*strip_only['leading'] <= (strip_only['stop_raw']-1)//4
    assert 33*11547-32*11706 == 6459
    assert 33*3*2**19-32*3**13 == 886176

    cells = []
    for d in list(range(4,25))+[32,64,128]:
        modulus = 2**(d+1)
        residue = ((2**d-105353)*pow(3**15,-1,modulus)) % modulus
        for index in (0,1,2**32):
            k = residue+modulus*index
            assert k % 16 == 5
            data = M.repair_failed(k)
            assert data['nodes'][0]['d'] == d
            cells.append([d,index,k,full(data)])

    counter = M.even_upper_undo(201)
    assert len(counter['current']) == 14 and counter['coefficients'] == {5:1,25:1,201:1}
    undos.append(undo_full(201))
    demonstrations = []
    for i,k in enumerate((5,38,53)):
        data = M.repair_failed(k)
        if stored is None:
            supplied = {v:pair_supply(v) for v in data['coefficients']}
        else:
            supplied = {int(v):dict(table) for v,table in stored['demonstrations'][i]['supplied'].items()}
        assert set(supplied) == set(data['coefficients'])
        for v,table in supplied.items():
            assert div(table) == {3*v:1,v:-1}
        output = M.compile_plan(data,supplied)
        assert div(output) == {3*data['seed']:1,data['seed']:-1}
        first = next(iter(supplied))
        reject(lambda:M.compile_plan(data,{}))
        reject(lambda:M.compile_plan(data,{**supplied,first:{}}))
        reject(lambda:M.compile_plan(data,{**supplied,first:{3:True}}))
        demonstrations.append(dict(k=k,seed=data['seed'],rank=data['rank'],
            current=rows(data['current']),coefficients=rows(data['coefficients']),
            supplied={str(v):rows(table) for v,table in sorted(supplied.items())},
            output=rows(output),output_rows=len(output)))

    good = M.repair_failed(5)
    w = 20009
    invalid = [lambda:M.local_decision(True,11547),lambda:M.local_decision(w,True),
        lambda:M.local_decision(w,11545),lambda:M.local_decision(w,20010),
        lambda:M.local_decision(w+2,w+2),lambda:M.local_decision(w,3*w+2),
        lambda:M.local_decision(33*11547,32*11547),
        lambda:M.local_decision(w,2*((32*w)//66)-1),
        lambda:M.local_decision(w,w,max_bits=True),lambda:M.local_decision(w,w,max_bits=16-1),
        lambda:M.bounded_repair(w,w,max_nodes=True),lambda:M.bounded_repair(w,w,max_nodes=0),
        lambda:M.repair_failed(38,max_nodes=1),lambda:M.repair_failed(-1),
        lambda:M.repair_failed(True),lambda:M.repair_failed(5,max_bits=16),
        lambda:M.repair_failed(0),lambda:M.repair_failed(1),
        lambda:M.even_upper_undo(True),lambda:M.even_upper_undo(25),
        lambda:M.even_upper_undo(9,max_bits=True),lambda:M.even_upper_undo(7983321),
        lambda:M.compile_plan(M.repair_failed(21),{}),
        lambda:M.compile_plan(dict(good,current={3:True}),{}),
        lambda:M.compile_plan(dict(good,current={3:1}),{}),
        lambda:M.compile_plan(dict(good,threshold=True),{}),
        lambda:M.compile_plan(dict(good,threshold=11547),{}),
        lambda:M.compile_plan(dict(good,threshold=good['rank']+1),{})]
    for i,call in enumerate(invalid):
        try:
            reject(call)
        except AssertionError as error:
            raise AssertionError('Rejection control '+str(i)+' did not reject') from error
    return dict(schema=1,status='PASS',scope='Bounded W9 reduction with every terminal current still a supplied premise.',
        generic_cases=len(generic),generic_hash=digest(generic),decision_kinds=sorted(kinds),
        forced_terminal_types=sorted(terminal_types),threshold_cases=len(thresholds),threshold_hash=digest(thresholds),
        R84_examined=examined,R84_skipped=skipped,R84_repairs=len(repairs),R84_hash=digest(repairs),
        exact_depth_cells=len(cells),cell_hash=digest(cells),undo_cases=len(undos),undo_hash=digest(undos),
        strip_only_control=dict(k=8,raw=strip_only['stop_raw'],leader=strip_only['leading']),
        nonzero_undo=dict(seed=201,current=rows(counter['current']),coefficients=rows(counter['coefficients'])),
        demonstrations=demonstrations,rejections=len(invalid)+9,
        supply_caps=dict(ordinary_arrows=ARROW_CAP,state_bits=BIT_CAP),source_hashes=sources())


def main():
    assert not sys.flags.optimize, 'Run without -O'
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    path = HERE/'w9_history_repair_audit.json'
    stored = None if args.write_receipt else json.loads(path.read_text())
    result = audit(stored)
    if args.write_receipt:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        assert result == stored, 'Receipt mismatch: inspect source and evidence changes'
    print('PASS: bounded W9 repair; '+json.dumps(dict(
        generic=result['generic_cases'],threshold=result['threshold_cases'],R84=result['R84_repairs'],
        cells=result['exact_depth_cells'],undos=result['undo_cases'],rejections=result['rejections'],
        supplied_rows=[d['output_rows'] for d in result['demonstrations']]),sort_keys=True))


if __name__ == '__main__':
    main()
