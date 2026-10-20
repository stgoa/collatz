"""Replay sigma bounds, incompatible rank edges, and exact finite currents."""
import argparse
import hashlib
import json
from pathlib import Path
import sigma_rank as M

HERE=Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def absorption(s):
    x,rows=s,{}
    for _ in range(10001):
        if x==1:
            assert M.divergence(rows)==M.atoms((1,s))
            return rows
        if x in rows or len(rows)==10000 or x.bit_length()>512:
            raise RuntimeError('Demonstration absorption input unresolved at cap')
        rows[x]=1
        x=M.NORMAL.step(x)
    raise AssertionError('Unreachable')


def reject(action,error=ValueError):
    try:action()
    except error:return
    raise AssertionError('Expected rejection')


def audit():
    nine=[]
    for b in range(9,16384,16):
        p=M.RANK.nine_plan(b)
        ranks=[M.sigma(u) for u in p['coefficients']]
        assert all(r<=3*b for r in ranks)
        nine.append([b,max(ranks,default=0)])
    bounds=[]
    for s in range(1,8192,2):
        p=M.absorption_plan(s)
        m=max((M.sigma(u) for u in p['coefficients']),default=0)
        assert m<=M.endpoint_bound(s)['bound']<=M.NORMAL.normal_form(s)
        bounds.append([s,m])
    assert M.absorption_plan(27)['coefficients'][21]==1 and M.sigma(21)==27
    family=[]
    for index in list(range(128))+[2**16,2**32,2**64,2**128]:
        witness=M.fifth_exponent_family(index)
        p=M.forward_plan(witness['seed'])
        assert p['status']=='descending'
        M.validate(p['seed'],p)
        family.append([index,p['seed'],M.sigma(p['seed']),digest(p['coefficients'])])
    bad=M.RETURN.forward_plan(4629)
    assert bad['status']=='descending' and bad['coefficients']=={5:-1,69:1,2197:1}
    assert M.RANK.rho(4629)==6943 and M.sigma(4629)==6171 and M.sigma(2197)==6591
    reject(lambda:M.validate(4629,bad))
    new=M.forward_plan(44981)
    assert M.OLD.one_step(44981) is None and new['status']=='descending'
    assert new['coefficients'][96069]==1
    assert M.sigma(44981)==134943 and M.sigma(96069)==128091 and M.RANK.rho(96069)==144103
    reject(lambda:M.RANK.validate_step(44981,new))
    counts={'old_accepted':0,'sigma_accepted':0,'both':0,'new_only':0,'old_only':0}
    plans=[]
    for w in range(5,8192,8):
        old=M.OLD.one_step(w)
        p=M.one_step(w)
        counts['old_accepted']+=old is not None
        counts['sigma_accepted']+=p is not None
        if old is not None and p is not None:counts['both']+=1
        if old is None and p is not None:counts['new_only']+=1
        if old is not None and p is None:counts['old_only']+=1
        if p is not None:
            M.validate(w,p)
            plans.append([w,p['rule'],sorted(p['coefficients'].items())])
    examples=[];fixture=None
    for w in (293,437,805,4021,44981):
        plan=M.close(w,max_nodes=10000)
        supplied={u:M.combine((1,absorption(3*u)),(-1,absorption(u))) for u in plan['coefficients']}
        current=M.compile_plan(plan,supplied)
        assert M.divergence(current)==M.T.pair_source(w)
        examples.append(dict(seed=w,expanded=plan['expanded'],leaves=sorted(plan['coefficients']),
                             rows=len(current),sha256=digest(current)))
        if w==44981:fixture=dict(seed=w,plan=plan,inputs=supplied,current=current)
    reject(lambda:M.compile_plan(new,{}))
    reject(lambda:M.sigma(9))
    reject(lambda:M.close(44981,max_nodes=0),RuntimeError)
    reject(lambda:M.forward_plan(3445))
    return dict(status='PASS',scope='Separate sigma induction; universal complement remains open',
                nine_plans=len(nine),nine_hash=digest(nine),absorption_plans=len(bounds),
                absorption_hash=digest(bounds),family=family,union_candidates=1024,
                union_counts=counts,union_hash=digest(plans),actual_substitutions=examples,
                rank_incompatibilities=[4629,44981],rejection_checks=6,
                caps=dict(nine_upper_bound=16384,absorption_upper_bound=8192,
                          union_upper_bound=8192,input_steps=10000,input_bits=512)),fixture


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args();result,fixture=audit()
    paths=[HERE/'sigma_rank_audit.json',HERE/'w44981_certificate.json']
    values=[result,fixture]
    if args.write_receipt:
        for p,v in zip(paths,values):p.write_text(json.dumps(v,indent=2)+'\n')
    else:
        for p,v in zip(paths,values):assert json.loads(p.read_text())==json.loads(json.dumps(v)),p
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
