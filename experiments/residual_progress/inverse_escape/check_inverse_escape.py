"""Bounded, read-only-by-default audit of the exact inverse escape rule."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
import inverse_escape as E

HERE = Path(__file__).resolve().parent


def digest(obj):
    return hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def table(rows):
    return [[x,c] for x,c in sorted(rows.items())]


def finite_absorption(seed, cap=10000):
    """Explicitly capped finite discovery, used only to demonstrate substitution."""
    x, rows = seed, {}
    for _ in range(cap+1):
        if x == 1:
            assert E.divergence(rows) == E.atoms((1,seed))
            return rows
        if x in rows or len(rows) == cap or x.bit_length() > 512:
            raise RuntimeError('Unresolved finite absorption input '+str(seed))
        rows[x] = 1
        x = E.NORMAL.step(x)
    raise AssertionError('Unreachable')


def audit():
    phases, phase_counts = [], Counter()
    for q in range(7,32768,2):
        if q % 3 == 1 and E.NORMAL.canonical(q):
            row = E.spine_bridge(q)
            phase_counts['descending' if row['descending'] else 'nondecreasing'] += 1
            phases.append([q,row['D'],row['j'],row['p'],digest(row['current'])])

    parameters = []
    for D,j in [(D,j) for D in range(1,13) for j in range(1,13)]+[
            (32,24),(64,46),(128,92),(256,182)]:
        for index in (0,1,7):
            witness = E.parameter_witness(D,j,index)
            row = E.spine_bridge(witness['q'])
            assert row['D'] == D and row['j'] == j
            parameters.append([D,j,index,witness['q'],witness['w'],row['p'],
                               row['descending'],digest(row['current'])])

    plans, plan_counts, children, examples = [], Counter(), Counter(), []
    for w in range(5,32768,8):
        if not E.recognized(w):
            continue
        row = E.pair_plan(w)
        par = row['parameters']
        plan_counts['new_D_ge_2' if par['D']>=2 else 'previous_D_1'] += 1
        children[str(par['p']%3)] += 1
        assert all(v<w and E.T.critical_image(v)<row['rho'] for v in row['coefficients'])
        if par['D']>=2:
            assert w % 3 == 1 and not E.C.eligible(w)
            if len(examples)<16:
                examples.append(w)
        plans.append([w,par['D'],par['j'],par['p'],table(row['coefficients']),
                      digest(row['current'])])

    supplied, compiled, stored = {}, [], []
    for w in examples:
        row = E.pair_plan(w)
        for v in row['coefficients']:
            if v not in supplied:
                supplied[v] = E.combine((1,finite_absorption(3*v)),(-1,finite_absorption(v)))
        current = E.compile_plan(row,supplied)
        assert E.divergence(current) == E.T.pair_source(w)
        compiled.append([w,table(row['coefficients']),len(current),digest(current)])
        if len(stored)<3:
            stored.append(dict(w=w,current=table(current)))
    rejection_count = 0
    demo = E.pair_plan(examples[0])
    for supplied_bad in ({}, {v:{} for v in demo['coefficients']}):
        try:
            E.compile_plan(demo,supplied_bad)
        except ValueError:
            rejection_count += 1
        else:
            raise AssertionError('Missing or invalid pair input accepted')

    # Independent exhaustive forward check: every candidate p<q<=8191 is
    # present in this source list. This tests the complete depth4 theorem.
    cap = 8191
    hits = {}
    for p in range(1,cap+1,2):
        if not E.NORMAL.canonical(p):
            continue
        y = p
        for depth in range(1,5):
            y = E.NORMAL.quotient_step(y)
            if p < y <= cap and y % 9 == 1:
                hits.setdefault(y,[]).append([p,depth])
    sharp = []
    for q in range(7,cap+1,2):
        if q % 9 != 1 or not E.NORMAL.canonical(q):
            continue
        expected = [[(64*q-73)//81,4]] if q % 81 == 10 else []
        actual = sorted(hits.get(q,[]))
        assert actual == expected
        sharp.append([q,actual])

    # Exhaust all branches at small depth with ray indices0 and1 only;
    # separately exercise large ray indices and independent full origin sets.
    inverse_rows = []
    for D in range(2,5):
        for k in (0,1,2):
            frontier = [((7,11,17)[k],[])]
            for depth in range(1,min(D+k,4)+1):
                next_frontier = []
                for shadow,word in frontier:
                    for kind in E.C.BASES[shadow%3]:
                        for ray_index in ((0,) if kind=='point' else (0,1)):
                            new_word = word+[(kind,ray_index)]
                            check = E.anchor_inverse_lift(D,1,k,new_word)
                            state = check['states'][-1]
                            inverse_rows.append([D,k,new_word,state['state'],state['shadow']])
                            next_frontier.append((state['shadow'],new_word))
                frontier = next_frontier
    large_rays = []
    for D,k,index in [(D,k,index) for D in (2,8,32,128)
                     for k in (0,1,2) for index in (0,8,128,1024)]:
        shadow, word = (7,11,17)[k], []
        for depth in range(1,D+k+1):
            kinds = E.C.BASES[shadow%3]
            kind = 'point' if 'point' in kinds and depth>1 else 'ray0'
            ray_index = index if depth==1 else 0
            shadow,_,_ = E.C.inverse_step(shadow,kind,ray_index)
            word.append((kind,ray_index))
        check = E.anchor_inverse_lift(D,1,k,word)
        large_rays.append([D,k,index,digest(check)])

    all_origins = []
    for D in range(2,7):
        witness = E.anchor_witness(D)
        q = witness['q']
        for k in (0,1,2):
            target, quotient_equal, ordinary_equal = witness['forward'][k], [], []
            for p in range(1,q+1,2):
                y = p
                for depth in range(1,D+k+1):
                    y = E.NORMAL.step(y)
                    if y == target:
                        ordinary_equal.append([p,depth])
                        assert p == q and depth == k
                if E.NORMAL.canonical(p):
                    y = p
                    for depth in range(1,D+k+1):
                        y = E.NORMAL.quotient_step(y)
                        if y == target:
                            quotient_equal.append([p,depth])
                            assert p == q and depth == k
            expected = [[q,k]] if k else []
            assert quotient_equal == ordinary_equal == expected
            all_origins.append([D,k,q,target,expected])

    # JSON round-trip is intentional: words contain nested pairs.
    result = dict(status='PASS',
        sources={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                 for name in ('inverse_escape.py','check_inverse_escape.py')},
        phases=dict(count=len(phases),classification=dict(phase_counts),sha256=digest(phases)),
        parameter_families=dict(count=len(parameters),sha256=digest(parameters)),
        conditional_plans=dict(count=len(plans),classification=dict(plan_counts),
                               child_residues=dict(children),sha256=digest(plans)),
        actual_substitutions=dict(count=len(compiled),distinct_inputs=len(supplied),
                                  cases=compiled,stored_currents=stored,rejections=rejection_count,
                                  discovery_cap=10000,discovery_bit_cap=512),
        complete_depth4=dict(targets=len(sharp),positive_cases=sum(bool(row[1]) for row in sharp),
                             origin_limit=cap,sha256=digest(sharp)),
        finite_inverse_words=dict(count=len(inverse_rows),ray_indices=[0,1],sha256=digest(inverse_rows)),
        large_ray_words=dict(count=len(large_rays),cases=large_rays),
        complete_origin_checks=all_origins,
        limitations=['Conditional inputs are not universally supplied.',
                     'Inverse-tree finite checks supplement the all-ray proof.',
                     'The fixed-precision obstruction is bounded per varying seed.'])
    return json.loads(json.dumps(result,sort_keys=True))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'inverse_escape_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        assert json.loads(path.read_text()) == result
    print('PASS inverse escape:',len(result['complete_origin_checks']),'full origin checks;',
          result['conditional_plans']['count'],'strict W5 plans;',
          result['actual_substitutions']['count'],'actual substitutions')


if __name__=='__main__':
    main()
