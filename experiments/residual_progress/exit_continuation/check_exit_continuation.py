"""Bounded exact audit of the exponent11 full-block continuation obstruction."""
import argparse
import hashlib
import json
from pathlib import Path
import exit_continuation as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def quotient(seed,steps):
    for _ in range(steps):seed=M.NORMAL.quotient_step(seed)
    return seed


def audit():
    assert 3**111<2**176 and 3**118>2**187
    exits=[]
    for r in range(25):
        for s in range(1,16,2):
            data=M.eleven(r,s)
            original=M.EXIT.parameters(data['seed'])
            assert original['endpoint']==data['endpoint']
            assert original['current']==data['current']
            assert original['quotient_length']==data['quotient_clock']
            assert quotient(data['rank'],data['quotient_clock'])==M.NORMAL.normal_form(data['endpoint'])
            exits.append([r,s,data['rank'],data['endpoint'],digest(data['current'])])

    specifications=[(r,A,K,0) for r in (16,17,24,32) for A in (5,8) for K in (0,2)]
    specifications += [(16,5,2,1),(16,5,2,3),(16,16,8,0)]
    families,plans,fixtures=[],[],[]
    for r,A,K,index in specifications:
        data=M.family(r,A,K,index)
        rejections=M.rejection_parameters(data)
        first=M.family(r,A,K,0)
        assert data['seed']==first['seed']+index*data['seed_period']
        assert data['t']==first['t']+index*data['t_period']
        assert data['s']==first['s']+index*data['s_period']
        # Verify every prefix in the small rows and both ends of the long row.
        prefix_indices=range(K+1) if K<=2 else (0,K)
        for j in prefix_indices:
            plan=M.continued_plan(data,j)
            undone=M.undo_plan(data,plan)
            assert len(undone['undos'])==j+1
            assert plan['ordinary_clocks']==[plan['quotient_clock'],0]
            ordinary,path_current=M.EXIT.ordinary_path(data['rank'],plan['ordinary_clocks'][0])
            assert ordinary[-1]==plan['endpoint']
            assert quotient(data['rank'],plan['quotient_clock'])==plan['endpoint']
            # Complete arithmetic rows also agree with that single ordinary path.
            arithmetic=data['current']
            block=M.RUN.bridge(data['endpoint'])
            arithmetic=M.combine((1,arithmetic),(1,block['current']))
            x=block['target']
            for _ in range(j):
                block=M.RUN.bridge(x);x=block['target']
                arithmetic=M.combine((1,arithmetic),(1,block['current']))
            assert arithmetic==path_current
            assert M.UNION.one_step(undone['leading']) is None
            expected=M.T.pair_source(data['seed'])
            for u,c in undone['coefficients'].items():
                expected=M.combine((1,expected),(-c,M.T.pair_source(u)))
            assert M.divergence(undone['current'])==expected
            plans.append(dict(r=r,A=A,K=K,index=index,prefix=j,seed=data['seed'],
                              leading=undone['leading'],leading_rank=undone['leading_rank'],
                              before_rows=len(plan['current']),after_rows=len(undone['current']),
                              before_hash=digest(plan['current']),after_hash=digest(undone['current']),
                              requests_hash=digest(undone['coefficients'])))
            if (r,A,K,index,j)==(16,5,2,0,2):
                fixtures.append(dict(status='unfinished: positive higher-rank pair premise retained',
                                     parameters={k:v for k,v in data.items() if k!='current'},
                                     appended_current=sorted(plan['current'].items()),
                                     appended_requests=sorted(plan['coefficients'].items()),
                                     restored_current=sorted(undone['current'].items()),
                                     restored_requests=sorted(undone['coefficients'].items()),
                                     undo_schedule=undone['undos']))
        families.append(dict(r=r,A=A,K=K,index=index,seed=data['seed'],q=data['rank'],
                             f=data['endpoint'],g=data['first_extended_endpoint'],rejections=rejections))

    failures=0
    valid=M.family(16,5,0)
    for call in (lambda:M.eleven(-1,1),lambda:M.eleven(1,2),lambda:M.family(15,5,0),
                 lambda:M.family(16,4,0),lambda:M.family(16,5,-1),lambda:M.family(16,5,0,-1),
                 lambda:M.continued_plan(valid,1),lambda:M.continued_plan(valid,-1)):
        try:call()
        except ValueError:failures+=1
        else:raise AssertionError('Invalid input was accepted')

    return dict(status='PASS',scope='Whole exponent11 interface and scoped full-block inverse undo; no absorption supplied',
                whole_exit_cases=len(exits),exit_hash=digest(exits),families=families,
                continuation_plans=plans,unfinished_current_fixtures=fixtures,rejection_checks=failures,
                caps=dict(exit_repeats=[0,24],exit_odd_indices=[1,15],family_max_repeats=32,
                          family_max_A=16,family_max_low_blocks=8,
                          undo_substitutions_per_plan_at_most=9,no_absorption_discovery=True),
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('exit_continuation.py','check_exit_continuation.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result=json.loads(json.dumps(audit(),sort_keys=True))
    path=HERE/'exit_continuation_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert json.loads(path.read_text())==result,'Receipt differs; inspect before regenerating'
    print('PASS: 200 complete e11 exits, 19 CRT families, 40 exact continuation undos, one unfinished fixture')


if __name__=='__main__':main()
