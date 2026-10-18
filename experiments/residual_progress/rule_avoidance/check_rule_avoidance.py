"""Bounded exact replay of the seven-rule avoidance family and full frontiers."""
import argparse
import hashlib
import json
from fractions import Fraction
from importlib.util import module_from_spec,spec_from_file_location
from pathlib import Path
import rule_avoidance as A

HERE=Path(__file__).resolve().parent


def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module


SIGMA=load('avoid_sigma','phase_rank/sigma_rank.py')
RETURN=load('avoid_return','returning_continuation/returning_continuation.py')
FORWARD=load('avoid_forward','forward_continuation/forward_continuation.py')


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def table(rows):
    return [[x,c] for x,c in sorted(rows.items())]


def audit():
    # Independently derive the exact affine table from the seven S arrows
    # and the selected halving at the fourth arrow.
    slope,offset=Fraction(1),Fraction(0)
    derived=[(slope,offset)]
    for i,a in enumerate((1,1,1,2,1,2,2)):
        slope,offset=3*slope/2**a,(3*offset+1)/2**a
        if i==3:slope,offset=slope/2,(offset-1)/2
        derived.append((slope,offset))
    for row,(slope,offset),shadow in zip(A.PREFIXES,derived,A.SHADOWS):
        numerator,constant,bits=row
        assert (slope,offset)==(Fraction(numerator,2**bits),Fraction(constant,2**bits))
        assert -17*slope+offset==shadow

    phase=[]
    for index in range(256):
        w=3445+3456*index
        row=A.entry((3*w-1)//2)
        assert row['w']==w and A.UNION.one_step(w) is None
        assert SIGMA.sigma(w)==A.RANK.rho(w) and SIGMA.one_step(w) is None
        assert not RETURN.recognized(w) and not FORWARD.OLD.eligible(w)
        phase.append([w,row['q'],row['D'],row['j']])

    families=[]
    repeat_values=list(range(1,13))+[16,32,64,128]
    for r in repeat_values:
        for index in (1,2,7):
            witness=A.witness(r,index)
            assert len(witness['states'])==7*r+1
            for x in witness['states']:
                if A.T.critical(x):
                    w=A.T.critical_inverse(x)
                    if w%8==5:
                        assert A.UNION.one_step(w) is None
                        assert SIGMA.sigma(w)==A.RANK.rho(w) and SIGMA.one_step(w) is None
                        assert not RETURN.recognized(w) and not FORWARD.OLD.eligible(w)
            families.append([r,index,witness['q'],witness['endpoint'],digest(witness['current'])])

    lookahead=[];nine=[];repeated=[];stored=[]
    for r in (1,2,3,4):
        for index in (1,2):
            for steps in range(7*r+1):
                row=A.lookahead_plan(r,steps,index)
                leading=SIGMA.sigma(row['lead'])
                assert leading==row['leading_rank']
                assert all(SIGMA.sigma(u)<leading for u in row['coefficients'] if u!=row['lead'])
                lookahead.append([r,index,steps,row['lead'],table(row['coefficients']),digest(row['current'])])
                if r==1 and index==1 and steps in (0,3,7):
                    stored.append(dict(seed=row['seed'],steps=steps,lead=row['lead'],
                                       coefficients=table(row['coefficients']),current=table(row['current'])))
            witness=A.witness(r,index)
            for cycle in witness['cycles']:
                row=A.nine_frontier(cycle['q'])
                nine.append([row['seed'],row['lead'],table(row['coefficients']),digest(row['current'])])
            row=A.repeat_plan(r,index)
            repeated.append([r,index,row['lead'],table(row['coefficients']),digest(row['current'])])

    # Actual finite expansion of smaller requests: the leading coefficient
    # survives both the old-rho and separate sigma compilers. Caps are guards.
    expansions=[]
    sample=A.lookahead_plan(1,3)
    for name,compiler,rank in (('rho',A.UNION.close,A.RANK.rho),('sigma',SIGMA.close,SIGMA.sigma)):
        current=sample['current'];coefficients={sample['lead']:1};expanded=0
        for u,c in sample['coefficients'].items():
            if u==sample['lead']:continue
            child=compiler(u,max_nodes=2000)
            expanded+=len(child['expanded'])
            current=A.combine((1,current),(c,child['current']))
            for v,d in child['coefficients'].items():
                assert rank(v)<rank(sample['lead'])
                coefficients[v]=coefficients.get(v,0)+c*d
        coefficients=A.NINE.clean(coefficients)
        assert coefficients[sample['lead']]==1
        expected=A.T.pair_source(sample['seed'])
        for v,c in coefficients.items():expected=A.combine((1,expected),(-c,A.T.pair_source(v)))
        assert A.divergence(current)==expected
        expansions.append(dict(rank=name,expanded_nodes=expanded,coefficients=table(coefficients),
                               current_hash=digest(current)))

    rejected=0
    for action in (lambda:A.family(0),lambda:A.family(1,0),lambda:A.entry(7),
                   lambda:A.one_cycle(5167),lambda:A.lookahead_plan(1,8),
                   lambda:A.RANK.validate_step(A.family(1)['w'],A.forward_plan(A.family(1)['q']))):
        try:action()
        except ValueError:rejected+=1
        else:raise AssertionError('Invalid input or increasing rule accepted')

    return dict(status='PASS',scope='Specified finite lookahead and rank-closure obstruction; no infinite positive avoiding orbit claimed',
                complete_phase_cases=len(phase),phase_hash=digest(phase),
                repeated_families=dict(count=len(families),repeat_values=repeat_values,indices=[1,2,7],sha256=digest(families)),
                lookahead_cases=len(lookahead),lookahead_hash=digest(lookahead),
                complete_nine_plans=len(nine),nine_hash=digest(nine),
                repeated_signed_plans=len(repeated),repeated_hash=digest(repeated),
                stored_unfinished_currents=stored,smaller_request_expansions=expansions,
                expansion_node_cap=2000,rejected_invalid_requests=rejected,
                source_hashes={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                               for name in ('rule_avoidance.py','check_rule_avoidance.py')})


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result=audit();path=HERE/'rule_avoidance_audit.json'
    if args.write_receipt:path.write_text(json.dumps(result,indent=2)+'\n')
    else:assert result==json.loads(path.read_text()),'Receipt mismatch; inspect before refreshing'
    print('PASS: 256 full-phase checks;48 repeated families;148 lookahead positions;20 W9 plans;two separately ranked expansions')


if __name__=='__main__':main()
