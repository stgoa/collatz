"""Finite exact audit of all exits and the conditional re-entry comparison."""
import argparse
import hashlib
import json
from pathlib import Path
import mixed_exit as X

HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def iterate(seed,count,quotient=False):
    step = X.NORMAL.quotient_step if quotient else X.NORMAL.step
    for _ in range(count):seed=step(seed)
    return seed


def audit():
    assert (X.P,X.C,X.L,X.E)==(282429536481,328537586155,137438953472,144990583009)
    assert X.RESIDUE==-X.C*pow(X.E,-1,2**63)%2**63
    assert X.RESIDUE==((X.M.RESIDUE*X.L-X.C)*pow(X.P,-1,2**63))%2**63
    # Uniform original-parent helper bound for every w>=5, including offset.
    assert 5*(24*X.L-9*X.P)>9*X.C+5*X.L>0
    # The next exact returning comparison has a genuinely higher input.
    assert 3*X.A-128*6561==754515
    assert 3*X.B-128*2603==600401

    exits=[];full_exits=[]
    for count in (1,2,8):
        for e in range(7,26):
            for index in (0,1):
                f=X.exit_family(count,e,index)
                p=X.exit_parameters(f['seed'])
                assert p['exit']==f['exit'] and p['exit_unit']==f['exit_unit']
                exits.append([count,e,index,f['seed'],p['exit'],p['d'],p['endpoint']])
                if count==1 and index==0:
                    plan=X.exit_plan(f['seed'])
                    left,right=plan['ordinary_common_tail_clocks']
                    assert iterate(3*f['seed'],left)==iterate(p['endpoint'],right)
                    assert iterate(3*f['seed'],plan['quotient_length'],True)==p['minimum']
                    full_exits.append(dict(valuation=e,seed=f['seed'],d=p['d'],
                                           rows=len(plan['current']),requests=len(plan['coefficients']),
                                           high=len(plan['high']),current_hash=digest(plan['current']),
                                           coefficient_hash=digest(plan['coefficients'])))
    assert {row[1] for row in exits}==set(range(7,26))

    full_reentries=[]
    for count in (1,2,4,8):
        for index in (0,1):
            f=X.general_reentry_family(count,index)
            data=X.general_reentry_plan(f['seed'])
            assert data['leading']==f['leading']
            assert iterate(3*f['seed'],12*(count+1)+6)==iterate(3*f['leading'],6)
            assert iterate(3*f['seed'],12*(count+1),True)==3*f['leading']
            full_reentries.append(dict(count=count,index=index,seed=f['seed'],
                                        leading=f['leading'],rows=len(data['current']),
                                        original_high=len(data['high']),
                                        current_hash=digest(data['current']),
                                        coefficient_hash=digest(data['coefficients'])))

    plans=[];stored=[]
    for index in range(8):
        w=X.RESIDUE+2**63*index
        plan=X.plan(w,audit_composition=True)
        direct=X.general_reentry_plan(w)
        assert direct['current']==plan['current'] and direct['coefficients']==plan['coefficients']
        assert iterate(3*w,30)==iterate(3*plan['leading'],6)
        assert iterate(3*w,24,True)==3*plan['leading']
        plans.append(dict(seed=w,leading=plan['leading'],rows=len(plan['current']),
                          requests=len(plan['coefficients']),current_hash=digest(plan['current']),
                          coefficient_hash=digest(plan['coefficients'])))
        if index==0:stored.append(plan)

    repetitions=[]
    for count in (1,2,4,8):
        for index in (0,1):
            f=X.family(count,index)
            data=X.repeated_plan(f['seed'],count)
            assert data['states']==f['states']
            assert iterate(3*f['seed'],24*count+6)==iterate(3*data['leading'],6)
            assert iterate(3*f['seed'],24*count,True)==3*data['leading']
            if count<=2:
                full=X.plan(f['seed'],audit_composition=True)
                for w in f['states'][1:-1]:
                    full=X.M.substitute_leading(full,X.plan(w,audit_composition=True))
                assert full['current']==data['current'] and full['coefficients']==data['coefficients']
            repetitions.append(dict(count=count,index=index,seed=f['seed'],leading=data['leading'],
                                    rows=len(data['current']),requests=len(data['coefficients']),
                                    original_high=len(data['high']),explicit_composition=count<=2,
                                    current_hash=digest(data['current']),
                                    coefficient_hash=digest(data['coefficients'])))
            if count==2 and index==0:stored.append(data)

    arithmetic=[]
    for count in (1,2,4,8,16,32,64,128):
        for index in (0,1,2**64):
            f=X.family(count,index);actual=X.maximum(f['seed'])
            assert actual['count']>=count
            for j,w in enumerate(f['states']):
                assert (X.E*w+X.C)*X.L**j==X.P**j*(X.E*f['seed']+X.C)
                if j<count:
                    old=X.M.maximum(w)
                    assert old['count']==1 and old['exit_valuation']==18
            arithmetic.append(dict(count=count,index=index,seed=f['seed'],
                                   maximum=actual['count'],state_hash=digest(f['states'])))

    exact=[]
    for order in range(63,100):
        period=2**(order+1)
        w=(2**order-X.C)*pow(X.E,-1,period)%period
        data=X.maximum(w)
        assert data['valuation']==order and data['count']==1
        exact.append([order,w,data['terminal_valuation']])
    assert {x[2] for x in exact}==set(range(26,63))

    rejected=0
    for action in (lambda:X.exit_family(0,18),lambda:X.exit_family(1,6),
                   lambda:X.exit_family(1,26),lambda:X.family(0),
                   lambda:X.family(1,-1),lambda:X.plan(X.M.RESIDUE),
                   lambda:X.repeated_plan(X.RESIDUE,2),
                   lambda:X.compile_plan(stored[0],{}),
                   lambda:X.compile_plan(stored[0],{x:{} for x in stored[0]['coefficients']})):
        try:action()
        except (ValueError,AssertionError):rejected+=1
        else:raise AssertionError('Invalid or missing input accepted')

    return dict(status='PASS',scope='Complete exit parameters and conditional growing natural re-entry; its returning comparison fails rho, and no missing pair or new dispatcher rule is supplied',
                exit_parameter_cases=len(exits),exit_parameter_hash=digest(exits),
                complete_exit_plans=full_exits,general_reentry_plans=full_reentries,reentry_plans=plans,
                repeated_plans=repetitions,arithmetic_families=arithmetic,
                exact_maximum_cases=len(exact),exact_maximum_hash=digest(exact),
                stored_currents=stored,rejection_checks=rejected,
                caps=dict(exit_count=8,full_exit_count=1,reentry_progressions=8,
                          full_reentry_count=8,explicit_substitution_count=2,
                          arithmetic_reentry_count=128,index_bits=65,
                          ordinary_clock=24*8+6),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('mixed_exit.py','check_mixed_exit.py')})


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    data=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'mixed_exit_audit.json'
    if args.write_receipt:path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(path.read_text())==data,'Receipt differs; inspect before regenerating'
    print('PASS: 114 exit parameters, 19 full exits, 8 general re-entries, 8 audited re-entry plans, 8 repeats, 24 long families, 37 maxima')


if __name__=='__main__':main()
