"""Replay the complete Phi exit alphabet and all signed original-Q premises."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType
import phi_exit_control as M

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
RECEIPT=HERE/'phi_exit_control_audit.json'

def rows(x):return [[u,c]for u,c in sorted(x.items())]
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def step(x):
    assert type(x)is int and x>0 and x%2
    if x==1:return 1
    y=3*x+1
    return y//(y&-y)
def order(x,p=2):
    assert type(x)is int and x>0
    k=0
    while x%p==0:k+=1;x//=p
    return k

def prefix(x,length,expected=None):
    current=Counter();values=[]
    for _ in range(length):
        y=3*x+1;values.append(order(y));current[x]+=1;x=step(x)
    if expected is not None:assert values==list(expected)
    return x,{u:c for u,c in current.items()if u!=1}

def div(current):
    result=Counter()
    for x,c in current.items():
        assert type(x)is int and x>1 and x%2 and type(c)is int and c
        result[x]+=c;result[step(x)]-=c
    return {x:c for x,c in result.items()if x!=1 and c}

def verify(plan):
    target=Counter({3*plan['seed']:1,plan['seed']:-1})
    for u,c in plan['coefficients'].items():
        assert type(u)is int and type(c)is int and c
        target[3*u]-=c;target[u]+=c
    assert div(plan['current'])=={u:c for u,c in target.items()if u!=1 and c}
    high={u:c for u,c in plan['coefficients'].items()if M.R.B.rho(u)>=plan['threshold']}
    assert high==plan['high'] and all(c>0 for c in high.values())
    assert (plan['status']=='descending')==(not high)
    return dict(seed=plan['seed'],threshold=plan['threshold'],status=plan['status'],
        current_hash=digest(rows(plan['current'])),requests=rows(plan['coefficients']),high=rows(high))

def stored_plan(plan):
    return dict(verify(plan),current=rows(plan['current']),comparison=rows(plan['comparison']),
                ordinary_clocks=plan['ordinary_clocks'])

def reject(call):
    try:call()
    except ValueError:return
    raise AssertionError('Invalid premise was not rejected')

def source_hashes():
    pending,seen=[M],set();files={Path(__file__).resolve(),HERE/'PHI_EXIT_CONTROL.md'}
    while pending:
        module=pending.pop()
        if id(module)in seen:continue
        seen.add(id(module));name=getattr(module,'__file__',None)
        if not name:continue
        path=Path(name).resolve()
        if not path.is_relative_to(ROOT):continue
        files.add(path)
        pending.extend(v for v in vars(module).values()if isinstance(v,ModuleType))
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(files)}

def audit():
    assert not sys.flags.optimize,'Run without optimization'
    assert M.A-M.M==M.D and sum(M.RAW_WORD)==19 and sum(M.CANONICAL_WORD)==18
    assert (-M.B*pow(M.D,-1,M.GUARD_MOD))%M.GUARD_MOD==M.GUARD
    returns=[]
    for r in(1,2,4,8,16):
      for i in(0,1):
        plan=M.repeat_comparison(r,i);verify(plan)
        data=plan['parameters'];q=data['Q'];sequence=plan['sequence']
        assert order(M.D*sequence[0]+M.B,3)==4
        for old,new in zip(sequence,sequence[1:]):
            assert prefix(6*old+1,12,M.RAW_WORD)[0]==6*new+1
            assert prefix(3*old,12,M.CANONICAL_WORD)[0]==6*new+1
            x=3*old
            for _ in range(12):x=M.R.N.quotient_step(x)
            assert x==3*new
            assert M.D*new+M.B==M.A*(M.D*old+M.B)//M.M
            assert order(M.D*new+M.B)==order(M.D*old+M.B)-19
            assert order(M.D*new+M.B,3)==order(M.D*old+M.B,3)+12
        assert order(6*(sequence[1]-sequence[0]),3)==5
        final=sequence[-1]
        left,lc=prefix(q,23+12*r);right,rc=prefix(3*final,5)
        assert left==right
        assert plan['comparison']==M.R.combine((1,lc),(-1,rc))
        x=q
        for _ in range(18+12*r):x=M.R.N.quotient_step(x)
        assert x==3*final
        assert plan['coefficients'][final]==1
        assert all(M.R.B.rho(u)<3*final for u in plan['coefficients']if u!=final)
        returns.append(dict(count=r,index=i,parameters=data,sequence=sequence,plan=stored_plan(plan)))
    table=[]
    for h in range(18,37):
        row=M.exit_row(h)
        alpha,beta=6*row['modulus'],6*row['residue']+1
        constant=1;exponent=0
        for a in row['word']:
            assert order(3*beta+1)==a<order(3*alpha)
            alpha,beta=3*alpha//2**a,(3*beta+1)//2**a
            constant,exponent=3*constant+2**exponent,exponent+a
        assert (alpha,beta)==(row['alpha'],row['beta'])
        assert (constant,exponent)==(row['affine_constant'],row['valuation_sum'])
        assert order(3*alpha)==row['min_next']<=order(3*beta+1)
        assert row['next_odd_coefficient']%2 and row['min_next']==h+2-exponent
        table.append(row)
    cases=[];full=[];modular=[];above_but_descending=[]
    for r in(0,1,4):
      for h in range(18,37):
       row=M.exit_row(h)
       for da in(0,1,3):
        a=row['min_next']+da
        plan=M.exit_comparison(r,h,a);data=plan['parameters'];other=M.exit_parameters(r,h,a,1)
        v0,q,y,ve=data['v'],data['Q'],plan['raw_test']['target'],data['exit_v']
        total=data['total_length'];word=row['word']+[a]
        assert order(M.D*v0+M.B)==19*r+h and order(M.D*ve+M.B)==h
        state=v0
        for _ in range(r):state=M.reenter(state)
        assert state==ve and M.maximum_reentries(state)==0
        end,current=prefix(q,total)
        assert end==y and current==plan['comparison']
        assert prefix(6*ve+1,len(word),word)[0]==y
        othery=M.raw_test(other)['target']
        assert othery-y==2*3**(total+1)
        assert other['index']-data['index']==data['index_modulus']
        assert data['index_modulus']==2**(data['total_valuation_sum']+1-45)
        assert (y<q)==plan['raw_test']['below_original']
        test=plan['raw_test'];assert test['rhs']>0
        assert (y<q)==(test['bracket']*v0>test['rhs'])
        shadow=Fraction(-1792529,M.D)
        for av in word:shadow=(3*shadow+1)/2**av
        p=plan['point_shadow'];assert(shadow.numerator,shadow.denominator)==(p['numerator'],p['denominator'])
        assert shadow.denominator%M.D==0 and shadow!=-1
        assert order(abs((Fraction(y)-shadow).numerator),3)>=p['ternary_precision']
        if p['point_depth']<p['ternary_precision']:assert order(y+1,3)==p['point_depth']
        record=dict(r=r,h=h,a=a,parameters=data,raw_test=test,point_shadow=p,plan=verify(plan))
        cases.append(record)
        if y>=q and not plan['high']:above_but_descending.append([r,h,a,y,q])
        if (r,h,da)in((0,18,0),(1,30,1),(4,36,3)):
            full.append(dict(r=r,h=h,a=a,plan=stored_plan(plan)))
            for z in(1,5,7,11,19):
                cert=M.ancestor_exponent(z,y,total+1)
                assert pow(2,cert['exponent_residue'],cert['modulus'])*z%cert['modulus']==(3*y+1)%cert['modulus']
                assert cert['period']==2*3**(total+1)
                modular.append(dict(target=z,anchor=y,power=total+1,certificate=cert))
    assert above_but_descending,'Keep a counterexample to necessity of the raw stop'
    # These are controls against broadening a guard or mixing the two clocks.
    good=102642092709
    assert M.reenter(good)>good and M.maximum_reentries(good)>=1
    assert prefix(6*good+1,16)[0]!=6*M.reenter(good)+1
    assert M.maximum_reentries(133797)==0
    assert prefix(6*133797+1,12,M.RAW_WORD)[0]%2==1
    badword=prefix(6*395941+1,12)[0]
    assert badword*2==(3*M.A*395941+1161985)//2**18
    invalid=[lambda:M.original(-1),lambda:M.original(True),lambda:M.order(0),lambda:M.order(True),
        lambda:M.order(3,5),lambda:M.guard_order(1),lambda:M.guard_order(True),
        lambda:M.reenter(133797),lambda:M.reenter(395941),
        lambda:M.repeat_parameters(-1),lambda:M.repeat_parameters(True),lambda:M.repeat_parameters(1,-1),
        lambda:M.repeat_comparison(1,max_arrows=True),lambda:M.repeat_comparison(1,max_arrows=34),
        lambda:M.exit_row(17),lambda:M.exit_row(37),lambda:M.exit_row(True),
        lambda:M.exit_parameters(-1,18,3),lambda:M.exit_parameters(0,18,2),
        lambda:M.exit_parameters(0,18,True),lambda:M.exit_parameters(0,18,3,-1),
        lambda:M.exit_comparison(0,18,3,max_arrows=29),lambda:M.exit_comparison(0,18,3,max_arrows=False),
        lambda:M.ancestor_exponent(3,7,2),lambda:M.ancestor_exponent(2,7,2),
        lambda:M.ancestor_exponent(True,7,2),lambda:M.ancestor_exponent(5,2,2),
        lambda:M.ancestor_exponent(5,7,0),lambda:M.ancestor_exponent(5,7,True)]
    for call in invalid:reject(call)
    return dict(schema=1,status='PASS',scope='Complete guarded exit control and conditional signed comparisons; no universal terminal supply.',
        return_cases=len(returns),returns=returns,exact_rows=table,exit_cases=len(cases),exit_hash=digest(cases),
        stored_exit_plans=full,modular_ancestor_controls=modular,raw_necessity_counterexamples=above_but_descending,
        explicit_rejections=len(invalid),source_hashes=source_hashes())

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true');args=parser.parse_args()
    result=audit()
    if args.write_receipt:RECEIPT.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert result==json.loads(RECEIPT.read_text()),'Receipt mismatch: inspect evidence and sources'
    print('PASS Phi exit control:',result['return_cases'],'returns;',len(result['exact_rows']),'rows;',
          result['exit_cases'],'full signed exit comparisons;',len(result['stored_exit_plans']),'stored exits;',
          len(result['modular_ancestor_controls']),'ancestor certificates;',result['explicit_rejections'],'rejections')
if __name__=='__main__':main()
