"""Finite exact audits of complete defect tables and fixed-rule failures."""
import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import defect_resolution as M

HERE = Path(__file__).resolve().parent


def encode(value):
    if isinstance(value,F):
        return {'numerator':value.numerator,'denominator':value.denominator}
    raise TypeError(type(value).__name__)


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':'),default=encode).encode()).hexdigest()


def absorb(seed):
    x,current=seed,{}
    for _ in range(10001):
        if x==1:
            assert M.divergence(current)==M.RANK.atoms((1,seed))
            return current
        if x in current or len(current)==10000 or x.bit_length()>512:
            raise RuntimeError('Finite supplied fixture reached its cap')
        current[x]=1
        x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def affine_checks():
    # A*x+B < C*x+D for every x>=73543: check the slope and first point.
    Q=(F(16384,19683),F(-33667,19683))
    below=[(F(9,16),F(1,16)),(F(3,4),F(1,4)),
           (F(243,512),F(347,512)),(F(81,128),F(101,128)),
           (F(729,1024),F(997,1024)),(F(729,1024),F(613,1024)),
           (F(729,1024),F(1009,1024)),(F(6561,8192),F(17081,8192))]
    above=[(F(1),F(0)),(F(27,32),F(23,32)),
           (F(243,256),F(247,256)),(F(27,32),F(3,32)),
           (F(243,256),F(187,256))]
    for A,B in below:
        assert A<Q[0] and A*73543+B<Q[0]*73543+Q[1]
    for A,B in above:
        assert A>Q[0] and A*73543+B>Q[0]*73543+Q[1]
    return len(below)+len(above)


def audit():
    affine=affine_checks()
    sigma_cases=[]
    for w in range(5,2048,8):
        if not (M.RETURN.returning(w) or M.EXACT.FORWARD.eligible(w)):
            continue
        plan=M.SIGMA.forward_plan(w)
        if plan['status']=='descending':
            sigma_cases.append(M.sigma_frontier(plan))
    sigma_counter=M.sigma_frontier(M.SIGMA.forward_plan(44981))
    assert sigma_counter['high']=={96069:1}

    nine=[]
    for b in range(25,25+16*256,16):
        n=3*b
        if M.EXACT.absorption_bound(n)['exception']:
            continue
        plan=M.RANK.absorption_plan(n)
        assert all(256*M.rho(u)<=243*n+511 for u in plan['coefficients'])
        nine.append([n,digest(plan['coefficients'])])

    first=[]
    for j in range(2,258,4):
        w=4021+8192*j
        plan=M.a3_first_decision(w)
        assert (j%4)==2 and plan['parameters']['a']==3
        first.append([w,plan['status'],digest(plan['current']),sorted(plan['high'].items())])

    table_rows,categories=[],Counter()
    selected_tables={}
    for A in (2,3):
        for d in range(2,19):
            for index in range(16):
                cell=M.second_cell(A,d,index)
                plan=M.a3_second_decision(cell['seed'])
                cont=plan['continuation'];f,n=cont['endpoint'],cont['minimum']
                category=f'A{A}:d{d}:{plan["status"]}'
                categories[category]+=1
                table_rows.append([A,d,index,cell['seed'],plan['status'],digest(plan['current']),sorted(plan['high'].items())])
                if plan['status']=='descending' and A==2 and d==4:
                    selected_tables.setdefault('A2d4',plan)
                if (plan['status']=='descending' and A==3 and d==2 and n%8==3
                        and M.NORMAL.selected(f)):
                    assert M.EXACT.absorption_bound(n)['exception'] is None
                    selected_tables.setdefault('A3d2_nine',plan)
    assert set(selected_tables)=={'A2d4','A3d2_nine'}

    large=[]
    for A,d,index in ((2,64,2**64),(3,65,2**128),(2,128,0),(3,129,1)):
        cell=M.second_cell(A,d,index)
        plan=M.a3_second_decision(cell['seed'])
        large.append([A,d,index,cell['seed'],plan['status']])

    arbitrary=[]
    for A in range(4,13):
        for d in (2,3,4,6,9):
            for index in (0,1):
                cell=M.second_cell(A,d,index)
                plan=cell['plan']
                arbitrary.append([A,d,index,plan['status'],digest(plan['coefficients'])])

    families=[]
    indices=list(range(16))+[2**k for k in (8,16,32,64,128)]
    for index in indices:
        good=M.successful_family(index)
        families.append(['success',index,good['seed'],digest(good['plan']['current'])])
        for exclude in (False,True):
            bad=M.surviving_family(index,exclude_parent=exclude)
            families.append(['surviving',index,exclude,bad['seed'],bad['defect'],digest(bad['plan']['current'])])
    unfinished=M.surviving_family(0,exclude_parent=True)['plan']

    fixed=[]
    for j in range(32):
        w=4021+8192*j
        if M.EXACT.fifth_plan(w)['status']=='descending':
            continue
        result=M.fixed_resolution(w,max_nodes=10000)
        fixed.append([w,result['status'],result['expanded'],sorted(result['high'].items())])

    examples,tables,all_supplied=[],[],{}
    choices=[M.successful_family(0)['plan'],M.successful_family(1)['plan'],
             selected_tables['A2d4'],selected_tables['A3d2_nine']]
    for i,plan in enumerate(choices):
        supplied={}
        for u in plan['coefficients']:
            if u not in all_supplied:
                all_supplied[u]=M.combine((1,absorb(3*u)),(-1,absorb(u)))
            supplied[u]=all_supplied[u]
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.RANK.T.pair_source(plan['seed'])
        examples.append(dict(seed=plan['seed'],stage=plan['stage'],rows=len(current),
                             coefficients=plan['coefficients'],current_hash=digest(current),supplied_hash=digest(supplied)))
        if i in (0,3):
            tables.append(dict(plan=plan,supplied=supplied,current=current))

    rejected=0
    for action in (lambda:M.parameters(437),lambda:M.successful_family(-1),
                   lambda:M.second_cell(1,2),lambda:M.a3_first_decision(44981),
                   lambda:M.a3_second_decision(M.second_cell(4,2)['seed']),
                   lambda:M.fixed_resolution(44981,max_nodes=0),
                   lambda:M.compile_plan(unfinished,{}),
                   lambda:M.compile_plan(choices[0],{}),
                   lambda:M.compile_plan(choices[0],{u:{} for u in choices[0]['coefficients']})):
        try:action()
        except (ValueError,RuntimeError):rejected+=1
        else:raise AssertionError('Invalid/incomplete request accepted')

    return dict(status='PASS',scope='Exact fifth-defect interfaces, a3 low-second-exponent iff tables, and fixed-fifteen failures; universal supply open',
                affine_inequalities=affine,sigma_cases=sigma_cases,sigma_counter=sigma_counter,
                nonexceptional_nine_cases=len(nine),nonexceptional_nine_hash=digest(nine),
                first_cases=len(first),first_hash=digest(first),second_cases=len(table_rows),
                second_hash=digest(table_rows),second_categories=dict(sorted(categories.items())),
                large_exact_cells=large,arbitrary_second_cases=len(arbitrary),arbitrary_second_hash=digest(arbitrary),
                complete_family_cases=families,fixed_resolution_cases=fixed,
                unfinished_fixture=unfinished,actual_substitutions=examples,stored_tables=tables,
                distinct_supplied_pairs=len(all_supplied),supplied_hash=digest(all_supplied),rejection_checks=rejected,
                caps=dict(first_index_bound=258,second_A_bound=12,second_depth_bound=129,
                          fixed_nodes=10000,input_steps=10000,input_bits=512),
                fixed_resolver_hash=hashlib.sha256(Path(M.FIXED.__file__).read_bytes()).hexdigest(),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('defect_resolution.py','check_defect_resolution.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=json.loads(json.dumps(audit(),sort_keys=True,default=encode))
    path=HERE/'defect_resolution_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: fifth-defect compatibility, complete low-exponent decisions and fixed-fifteen obstruction')


if __name__=='__main__':main()
