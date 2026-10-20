"""Bounded independent arithmetic and exact-current audit of R55."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import selected_forward as M

HERE = Path(__file__).resolve().parent
OLD = M._load('selected_forward_old_nine', 'continued_rules/continued_rules.py')


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def finite_absorption(seed, cap=10000):
    current, x = {}, seed
    for _ in range(cap+1):
        if x == 1:
            assert M.divergence(current) == M.atoms((1, seed))
            return current
        if x in current or len(current) == cap or x.bit_length() > 512:
            raise RuntimeError('Finite fixture input remains unresolved: '+str(seed))
        current[x] = 1
        x = M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def raw(a, d, t):
    value = F(3**(d//2)*(3**(a-1)*t-1), 2**d)
    return value if d % 2 else 2*value+1


def affine_checks():
    """Check every affine expression displayed in both decision proofs."""
    first = []
    for t in (1, 11, 13, 323):
        for a, slope in ((2, 175), (3, 269), (4, 295)):
            q = 2**a*t-1
            assert q-(9*raw(a, 3, t)+5)/8 == F(slope*t-77, 64)
        q = 4*t-1
        assert raw(2, 2, t)-q == F(t+1, 2)
        assert q-raw(2, 4, t) == F(5*t-7, 8)
        assert q-(9*raw(2, 2, t)+1)/16 == F(47*t-25, 32)
        first.append(t)

    # (B,e,bound name,L,C,D) denotes q-bound=(L*q-C)/D.
    table = [
        (2,3,'odd',1319,1469,2048), (3,3,'odd',1909,3991,4096),
        (4,3,'odd',1631,11141,8192), (2,2,'raw',-17,85,64),
        (2,4,'raw',13,319,256), (2,2,'E3',295,829,1024),
        (3,6,'raw',-139,3479,2048), (3,8,'raw',1631,12485,8192),
        (3,2,'E1',1631,11717,8192), (3,2,'E3',-139,2711,2048),
        (3,2,'E7',13,159,256), (3,4,'E3',1631,9413,8192),
        (4,8,'raw',-3299,34447,16384), (4,10,'raw',6487,119725,65536),
        (4,2,'E1',-3299,32911,16384), (4,2,'E3',-2465,8581,4096),
        (4,2,'E7',-217,669,512), (4,4,'E1',6487,113581,65536),
        (4,4,'E3',-3299,28303,16384), (4,4,'E7',-139,2007,2048),
        (4,6,'E3',6487,95149,65536),
    ]
    for q in (F(0), F(1), F(91), F(4219)):
        n = (9*q+5)/8
        for b,e,kind,L,C,D in table:
            t = (n+1)/2**b
            y = raw(b,e,t);m = (y-1)/2
            bound = dict(raw=y,odd=(9*y+5)/8,E1=(27*m+29)/32,
                         E3=(9*m+5)/8,E7=m)[kind]
            assert q-bound == F(L*q-C,D)
            if q == 91:
                assert (q-bound > 0) == (L > 0)
    return dict(first_t_values=first, second_rows=table, second_q_values=[0,1,91,4219])


def audit():
    formulas = affine_checks()
    rows, two_rows, counts, two_counts = [], [], Counter(), Counter()
    unit2, new, undo, growth = [], [], [], []
    for w in range(5,32768,8):
        if not M.eligible(w):
            continue
        plan = M.forward_plan(w);data = plan['parameters']
        a,d = data['a'],data['d']
        counts[f'a{a}:w{w%3}:{plan["status"]}'] += 1
        if a in (2,3,4):
            assert (plan['status'] == 'descending') == M.small_exponent_domain(data)
        if w % 3 == 2:
            q = data['rank']
            assert q%9 == 7 and (q-1)%3 == 0 and (q-1)%9 != 0
            u = (q-1)//3
            assert u%3 == 2 and (4*u+2)%3 != 0
            assert OLD.one_step(w) is None
            unit2.append(w)
        if (a,d) == (2,2) and M.NORMAL.canonical(data['endpoint']):
            undo.append(M.even_undo(w))
            second = M.two_block_plan(w);s = second['blocks'][1]
            if s['a'] in (2,3,4):
                assert (second['status'] == 'descending') == M.two_block_domain(second)
            two_counts[f'b{s["a"]}:e{s["d"]}:{second["status"]}'] += 1
            two_rows.append([w,second['status'],s,digest(second['current']),sorted(second['coefficients'].items())])
        accepted = M.one_step(w)
        if accepted is not None:
            M.RANK.validate_step(w,accepted)
            if OLD.one_step(w) is None:
                new.append(w)
            if any(u>w for u in accepted['coefficients']):
                growth.append([w,[(u,M.rho(u),c) for u,c in sorted(accepted['coefficients'].items()) if u>w]])
        rows.append([w,plan['status'],a,d,data['endpoint'],data['minimum'],
                     plan['input_rank_bound'],digest(plan['current']),sorted(plan['coefficients'].items()),
                     accepted['rule'] if accepted else None])

    families = []
    for a in list(range(2,25))+[32,64,128]:
        for j in (0,1,7):
            family = M.long_family(a,j)
            w = family['seed'];plan = M.forward_plan(w)
            assert plan['status'] == 'descending' and OLD.one_step(w) is None
            families.append(dict(family=family,rows=len(plan['current']),
                                 requests=len(plan['coefficients']),current_hash=digest(plan['current'])))
    assert M.long_family(2)['seed_residue'] == 221
    assert M.long_family(2)['seed_period'] == 384
    assert M.long_family(2,d=5)['seed_residue'] == 29
    assert M.long_family(2,d=5)['seed_period'] == 1536

    phases = []
    for residue,period,a,d,blocks in ((221,384,2,3,1),(29,1536,2,5,1),
                                    (10357,13824,4,3,1),(2813,3072,2,2,2)):
        for j in range(32):
            w = residue+period*j
            plan = M.forward_plan(w) if blocks==1 else M.two_block_plan(w)
            assert plan['status'] == 'descending'
            assert (plan['parameters']['a'],plan['parameters']['d']) == (a,d)
            assert OLD.one_step(w) is None
            if blocks == 2:
                assert (plan['blocks'][1]['a'],plan['blocks'][1]['d']) == (2,3)
                assert M.forward_plan(w)['status'] == 'unresolved'
            if residue == 10357:
                k = (w+11)//3456
                assert k%4 == 3 and M.NORMAL.valuation2(2187*k-7) == 1
                q = plan['rank'];f = plan['parameters']['endpoint']
                assert f == (81*q+33)//128
                assert F(q)-F(9*f+5,8) == F(295*q-937,1024)
            phases.append([w,blocks,digest(plan['current'])])

    counterexamples = []
    for w, f, m, bound in ((58741,167275,167275,167275),
                          (86389,246007,123003,138379)):
        p = M.forward_plan(w);d = p['parameters']
        assert w%13824 == 3445 and (d['a'],d['d']) == (4,4)
        assert d['endpoint'] == f and d['minimum'] == m
        assert p['status'] == 'unresolved' and p['input_rank_bound'] == [bound,1]
        counterexamples.append([w,p['rank'],f,m,bound])
    assert M.parameters(3445)['d'] == 4
    assert M.forward_plan(3445)['status'] == 'descending'

    supplied, demos, tables = {}, [], []
    for w in (221,2813,3445,10357):
        p = M.one_step(w)
        for u in p['coefficients']:
            if u not in supplied:
                supplied[u] = M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current = M.compile_plan(p,supplied)
        assert M.divergence(current) == M.T.pair_source(w)
        demos.append(dict(seed=w,rule=p['rule'],requests=sorted(p['coefficients'].items()),
                          current_rows=len(current),current_hash=digest(current)))
        if w in (221,2813):
            tables.append(dict(seed=w,current=sorted(current.items()),
                               supplied=[dict(seed=u,current=sorted(supplied[u].items()))
                                         for u in sorted(p['coefficients'])]))
    failures = 0
    for action in (lambda:M.forward_plan(45),lambda:M.forward_plan(9),
                   lambda:M.two_block_plan(221),lambda:M.long_family(1),
                   lambda:M.long_family(8,d=3),
                   lambda:M.compile_plan(M.forward_plan(221),{}),
                   lambda:M.compile_plan(M.forward_plan(58741),{})):
        try:action()
        except ValueError:failures += 1
        else:raise AssertionError('Invalid input not rejected')
    return dict(status='PASS',scope='Selected forward exact currents; complete A2/A3/A4 and second-block tables; whole new CRT domains',
                selected_inputs=len(rows),selected_inputs_hash=digest(rows),categories=dict(sorted(counts.items())),
                two_block_inputs=len(two_rows),two_block_hash=digest(two_rows),two_block_categories=dict(sorted(two_counts.items())),
                selected_unit2_old_nine_exclusions=len(unit2),selected_unit2_hash=digest(unit2),
                newly_recognized_in_finite_window=len(new),newly_recognized_hash=digest(new),
                undo_checks=len(undo),undo_hash=digest(undo),index_growth_examples=growth,
                affine_formula_checks=formulas,long_family_examples=families,
                explicit_phase_checks=len(phases),explicit_phase_hash=digest(phases),
                refuted_wrong_phase_counterexamples=counterexamples,
                actual_substitutions=demos,stored_finite_current_tables=tables,
                supplied_pair_count=len(supplied),supplied_pairs_hash=digest(supplied),
                rejected_invalid_requests=failures,
                caps=dict(pair_seed_max=32767,family_a_values=list(range(2,25))+[32,64,128],
                          family_indices=[0,1,7],phase_indices=list(range(32)),
                          input_discovery_steps=10000,input_discovery_bits=512),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('selected_forward.py','check_selected_forward.py')})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args = parser.parse_args()
    result = json.loads(json.dumps(audit(),sort_keys=True))
    path = HERE/'selected_forward_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text()) == result,'Receipt differs; inspect before regenerating'
    print('PASS: selected forward interface, complete low-exponent and second-block tables, new whole CRT families, exact supplied-current substitutions')


if __name__ == '__main__':main()
