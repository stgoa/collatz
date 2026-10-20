"""Bounded exact audit of deferred rank and its complete new domains."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import deferred_rank as M

HERE = Path(__file__).resolve().parent


def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorb(seed):
    rows,x = {},seed
    for _ in range(10001):
        if x == 1:
            assert M.divergence(rows) == M.atoms((1,seed))
            return rows
        if x in rows or len(rows) == 10000 or x.bit_length() > 512:
            raise RuntimeError('Capped demonstration input remains unresolved')
        rows[x] = 1;x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    records,new,counts,protected = [],set(),Counter(),[]
    for w in range(5,8192,8):
        if M.OLD.one_step(w) is not None:
            continue
        for kind,initial in M.candidates(w):
            result = M.defer(initial,max_nodes=32)
            counts[kind+':'+result['status']] += 1
            if result['status'] == 'descending':
                new.add(w)
                assert all(M.rho(u)<M.rho(w) for u in result['coefficients'])
            if result['blocked'].get(w) == 'original_source':
                assert result['coefficients'][w] == 1
                protected.append([w,kind])
            records.append([w,kind,result['status'],digest(result['current']),
                            sorted(result['coefficients'].items()),result['history']])
    assert new and protected

    first_examples,macro_examples,exclusions = [],[],[]
    for n in list(range(64))+[2**k for k in (16,32,64,128)]:
        d = M.first_family(n)
        assert d['rank']-d['successor'] == 18+78*n
        first_examples.append([n,d['seed'],digest(d['plan']['current']),sorted(d['plan']['coefficients'].items())])
    for l in list(range(128))+[24*2**k for k in (16,32,64,128)]:
        if not M.NORMAL.selected(3127+78732*l):
            continue
        d = M.macro_family(l)
        expected_states = [(1951,49152),(2927,73728),(4391,110592),(6587,165888),
                           (9881,248832),(7411,186624),(11117,279936),
                           (4169,104976),(3127,78732)]
        assert d['path'] == [a+b*l for a,b in expected_states]
        assert len(d['plan']['history']) == 1 and d['plan']['history'][0]['coefficient'] == 1
        macro_examples.append([l,d['seed'],d['child'],digest(d['plan']['current']),
                               sorted(d['plan']['coefficients'].items())])
    for j in list(range(32))+[2**k for k in (16,32,64,128)]:
        for d in (M.first_family(3*j),M.macro_family(24*j)):
            w = d['seed']
            assert w%3 == 2 and M.OLD.one_step(w) is None
            exclusions.append([w,digest(d['plan']['current'])])

    # A negative higher request cancels its own accepted current exactly;
    # the protected original P21 remains, demonstrating signed handling.
    child = M.OLD.one_step(1853)
    c = Counter(child['coefficients']);c[21]+=1;c[1853]-=1
    signed = dict(seed=21,current=child['current'],coefficients=dict(c))
    signed_result = M.defer(signed)
    assert signed_result['status'] == 'unresolved' and signed_result['current'] == {}
    assert signed_result['coefficients'] == {21:1}
    assert signed_result['history'][0]['coefficient'] == -1
    assert signed_result['blocked'] == {21:'original_source'}

    capped = M.defer(M.OLD.FORWARD.forward_plan(1301),max_nodes=0)
    assert capped['status'] == 'capped' and capped['remaining_high'] == [1853]
    assert capped['history'] == []
    assert M.defer(M.OLD.FORWARD.forward_plan(245),max_nodes=0)['status'] == 'descending'

    supplied,examples,tables = {},[],[]
    for w in (245,1301,3317,787733):
        initial = M.OLD.FORWARD.forward_plan(w)
        plan = M.defer(initial,max_nodes=32)
        assert plan['status'] == 'descending' and M.OLD.one_step(w) is None
        inputs = {}
        for u in plan['coefficients']:
            if u not in supplied:
                supplied[u] = M.combine((1,absorb(3*u)),(-1,absorb(u)))
            inputs[u] = supplied[u]
        current = M.compile_plan(plan,inputs)
        assert M.divergence(current) == M.RANK.T.pair_source(w)
        examples.append(dict(seed=w,rows=len(current),requests=sorted(plan['coefficients'].items()),
                             expansions=plan['history'],current_hash=digest(current)))
        if w in (245,1301):
            tables.append(dict(seed=w,plan=plan,supplied=inputs,current=current))

    bad = dict(seed=245,current={},coefficients={})
    failures = 0
    for action in (lambda:M.defer(bad),lambda:M.defer(M.OLD.FORWARD.forward_plan(245),max_nodes=-1),
                   lambda:M.macro_family(3),lambda:M.first_family(-1),
                   lambda:M.compile_plan(capped,{}),lambda:M.compile_plan(signed_result,{}),
                   lambda:M.compile_plan(M.first_family()['plan'],{})):
        try:action()
        except ValueError:failures+=1
        else:raise AssertionError('Invalid or missing premise was accepted')
    return dict(status='PASS',scope='Finite deferred-rank theorem and two complete new domains; unresolved frontiers retained',
                candidate_seeds=1024,initial_plans=len(records),plan_hash=digest(records),
                categories=dict(sorted(counts.items())),newly_descending_seeds=sorted(new),
                protected_source_cases=protected,first_family_examples=first_examples,
                macro_family_examples=macro_examples,complete_new_domain_examples=exclusions,
                signed_multiplier_example=signed_result,capped_example=capped,
                actual_substitutions=examples,stored_tables=tables,
                distinct_supplied_pairs=len(supplied),supplied_hash=digest(supplied),
                rejection_checks=failures,
                caps=dict(candidate_upper=8192,deferred_nodes=32,input_steps=10000,input_bits=512,
                          first_indices=[0,63],macro_indices=[0,127],large_power_max=128),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('deferred_rank.py','check_deferred_rank.py')},
                fixed_resolver_hash=hashlib.sha256((HERE.parent/'selected_rules/selected_rules.py').read_bytes()).hexdigest())


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=json.loads(json.dumps(audit(),sort_keys=True))
    p=HERE/'deferred_rank_audit.json'
    if args.write_receipt:p.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(p.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: deferred original-rank expansion, complete new domains, exact macro currents and protected unresolved inputs')


if __name__=='__main__':main()
