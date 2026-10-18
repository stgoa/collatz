"""Bounded exact audit of the whole nonselected two-run interface."""
import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
import nonselected_forward as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def finite_absorption(seed,cap=10000):
    rows,x={},seed
    for _ in range(cap+1):
        if x==1:
            assert M.divergence(rows)==M.atoms((1,seed))
            return rows
        if x in rows or len(rows)==cap or x.bit_length()>512:
            raise RuntimeError('Designated finite input remains unresolved: '+str(seed))
        rows[x]=1
        x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def affine_comparisons():
    """Check all intercepts displayed in the low-exponent proof separately."""
    def raw(a,d,t):
        scale=1 if d%2 else 2
        return F(scale*3**(d//2)*(3**(a-1)*t-1),2**d)+(0 if d%2 else 1)
    rows=[]
    for t in (1,5,7,17,139):
        q3,q4=8*t-1,16*t-1
        f32,f34,f36=raw(3,2,t),raw(3,4,t),raw(3,6,t)
        assert q3-F(9*raw(3,3,t)+5,8)==F(269*t-77,64)
        assert q4-F(9*raw(4,3,t)+5,8)==F(295*t-77,64)
        assert q3-f36==F(13*t-37,32)
        assert f32-q3==F(11*t+1,2) and f34-q3==F(17*t+7,8)
        assert q3-F(9*f32+1,16)==F(13*t-25,32)
        assert q4-raw(4,10,t)==F(1631*t-781,512)
        assert q4-raw(4,8,t)==F(-139*t-175,128)
        assert q4-F(9*raw(4,6,t)+1,16)==F(1631*t-589,512)
        for d,expected in ((4,(F(1631*t-733,512),F(-139*t-127,128),F(13*t-7,16))),
                           (2,(F(-139*t-163,128),F(-217*t-25,32),F(-17*t-1,4)))):
            n=(raw(4,d,t)-1)/2
            actual=(q4-(27*n+29)/32,q4-(9*n+5)/8,q4-n)
            assert actual==expected
            rows.append([t,d,[[x.numerator,x.denominator] for x in actual]])
    return rows


def audit():
    formulas=affine_comparisons()
    plans,categories,small_categories,undo=[],Counter(),Counter(),[]
    selected_multiples,index_growth=[],[]
    for w in range(5,32768,8):
        if not M.eligible(w):
            continue
        plan=M.forward_plan(w)
        data=plan['parameters']
        a,d,f,n=data['a'],data['d'],data['endpoint'],data['minimum']
        categories[f'a{a}:{plan["status"]}:multiple3={w%3==0}']+=1
        if a in (3,4):
            assert (plan['status']=='descending')==M.small_exponent_domain(data)
            small_categories[f'a{a}:d{d}:selected={M.NORMAL.selected(f) if d%2==0 else "odd"}:n{n%8}:{plan["status"]}']+=1
        if n>1 and n%8==1:
            M.stratum_test(data,forward=True)
        if d%2==0:
            assert M.OLD.absorption_rank_bound(f)['bound']<=f
            if M.NORMAL.canonical(f):
                undo.append(M.even_undo(w))
        if plan['status']=='descending':
            if w%3==0:
                assert not M.INVERSE.eligible(w) and not M.OLD.returning(w)
                assert w%27!=20 and w%243!=91 and not M.ESCAPE.recognized(w)
                selected_multiples.append(w)
            if any(u>w for u in plan['coefficients']):
                index_growth.append([w,[[u,M.rho(u),c] for u,c in sorted(plan['coefficients'].items()) if u>w]])
        plans.append([w,plan['status'],a,d,f,n,plan['input_rank_bound'],
                      sorted(plan['coefficients'].items()),digest(plan['current'])])

    families=[]
    for a in list(range(3,25))+[32,64,128]:
        for j in (0,1,7):
            data=M.long_family(a,j)
            plan=M.forward_plan(data['seed'])
            assert plan['status']=='descending' and data['seed']%3==0
            families.append(dict(family=data,rows=len(plan['current']),
                                 requests=len(plan['coefficients']),current_hash=digest(plan['current'])))
    assert M.long_family(3)['seed_residue']==45 and M.long_family(3)['seed_period']==384
    assert M.long_family(4)['seed_residue']==741 and M.long_family(4)['seed_period']==768
    explicit_phases=[]
    for residue,period,a in ((45,384,3),(741,768,4)):
        for j in range(16):
            w=residue+period*j
            data=M.forward_plan(w)
            assert data['status']=='descending' and data['parameters']['a']==a and data['parameters']['d']==3
            explicit_phases.append([w,digest(data['current'])])

    demo_seeds=list(dict.fromkeys([45,741]+selected_multiples[:10]+[x[0] for x in index_growth[:4]]))
    supplied,demos,tables={},[],[]
    for w in demo_seeds:
        plan=M.forward_plan(w)
        for u in plan['coefficients']:
            if u not in supplied:
                supplied[u]=M.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        demos.append(dict(seed=w,rank=plan['rank'],requests=sorted(plan['coefficients'].items()),
                          rows=len(current),current_hash=digest(current)))
        if w in (45,741,index_growth[0][0]):
            tables.append(dict(seed=w,current=sorted(current.items())))

    failures=0
    good=M.forward_plan(45)
    for action in (lambda:M.compile_plan(good,{}),
                   lambda:M.compile_plan(good,{u:{} for u in good['coefficients']}),
                   lambda:M.compile_plan(M.forward_plan(141),{}),
                   lambda:M.forward_plan(21),lambda:M.forward_plan(9),
                   lambda:M.long_family(2),lambda:M.long_family(6,d=3)):
        try:
            action()
        except ValueError:
            failures+=1
        else:
            raise AssertionError('Invalid request was not rejected')

    return dict(status='PASS',scope='Complete conditional nonselected interface; exact low-a test; multiple3 families; finite substitutions',
                nonselected_inputs=len(plans),plan_hash=digest(plans),categories=dict(sorted(categories.items())),
                low_a_categories=dict(sorted(small_categories.items())),
                accepted_multiples3=len(selected_multiples),index_growth_examples=index_growth,
                even_undo_checks=len(undo),even_undo_hash=digest(undo),
                affine_formula_checks=formulas,long_family_examples=families,
                explicit_phase_checks=len(explicit_phases),explicit_phase_hash=digest(explicit_phases),
                actual_substitutions=demos,actual_current_tables=tables,
                supplied_pair_count=len(supplied),supplied_pairs_hash=digest(supplied),
                rejected_invalid_requests=failures,
                caps=dict(pair_seed_max=32767,family_a_values=list(range(3,25))+[32,64,128],
                          family_indices=[0,1,7],input_discovery_steps=10000,input_discovery_bits=512),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ['nonselected_forward.py','check_nonselected_forward.py']})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'nonselected_forward_audit.json'
    if args.write_receipt:
        path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:
        assert json.loads(path.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: whole nonselected forward interface, complete a3/a4 classification, multiple3 families and actual current substitutions')


if __name__=='__main__':
    main()
