"""Replay strict lower histories, complete cells, signed repairs and supplies."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys
from types import ModuleType
import retained_history as M

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
ARROW_CAP,BIT_CAP=10000,2048
NORMALIZER=M._load('retained_normalizer_check','frontier_progress/frontier_normal_form.py')

def rows(x):return [[u,c]for u,c in sorted(x.items())]
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def step(x):
    if x==1:return 1
    n=3*x+1
    return n//(n&-n)
def div(current):
    out=Counter()
    for x,c in current.items():
        assert type(x)is int and x>1 and x%2 and type(c)is int and c
        out[x]+=c
        if step(x)!=1:out[step(x)]-=c
    return {x:c for x,c in out.items()if c}
def boundary(data):
    out=Counter({3*data['seed']:1,data['seed']:-1})
    for u,c in data['coefficients'].items():out[3*u]-=c;out[u]+=c
    return {x:c for x,c in out.items()if x!=1 and c}
def reject(call):
    try:call()
    except ValueError:return
    raise AssertionError('Expected explicit rejection')
def verify(data):
    assert div(data['current'])==boundary(data)
    high={u:c for u,c in data['coefficients'].items()if M.B.rho(u)>=data['threshold']}
    assert high==data['high'] and (data['status']=='descending')==(not high)
    return [data['seed'],data['threshold'],data['status'],rows(high),
            digest(rows(data['current'])),rows(data['coefficients'])]
def absorb(x):
    current={}
    while x!=1:
        if len(current)>=ARROW_CAP or x.bit_length()>BIT_CAP or x in current:
            raise RuntimeError('Designated supply exceeded its finite cap')
        current[x]=1;x=step(x)
    return current
def pair_supply(w):
    result=M.combine((1,absorb(3*w)),(-1,absorb(w)))
    assert div(result)=={3*w:1,w:-1}
    return result

def source_hashes():
    pending,seen=[M,NORMALIZER],set();files={Path(__file__).resolve(),HERE/'RETAINED_HISTORY.md'}
    while pending:
        module=pending.pop()
        if id(module)in seen:continue
        seen.add(id(module));filename=getattr(module,'__file__',None)
        if not filename:continue
        path=Path(filename).resolve()
        if not path.is_relative_to(ROOT):continue
        files.add(path)
        pending.extend(v for v in vars(module).values()if isinstance(v,ModuleType))
    return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(files)}

def audit(stored=None):
    generic=[];branches=set();node_counts=set();thresholds=[]
    for d in list(range(4,21))+[32,64,128]:
        modulus=2**(d+1)
        residue=((1+2**d)*pow(9,-1,modulus))%modulus
        for i in(0,1,2,3,7,15,2**32,2**96):
            C=residue+modulus*(4096+i)
            for Q in(((3*C+1)//4+1)|1,C,2*C+1,3*C):
                p=M.history_nine(C,Q)
                assert p['nodes'][0]['d']==d
                assert len(p['nodes'])<=3
                assert not p['high']or(len(p['high'])==1 and next(iter(p['high'].values()))==1 and next(iter(p['high']))%8==5)
                generic.append(verify(p));node_counts.add(len(p['nodes']))
                local=M.B.nine_candidate(C);z=local['z']
                branches.add('odd'if d%2 else'noncanonical'if not M.N.canonical(3*z)else'forward' if 3*z%8==1 else'critical')
                # Reconstruct every entire signed substitution independently.
                upper=M.prefix(3*C,local['prefix_length']);hx=M.B.absorption_plan(upper['endpoint']);hc=M.B.absorption_plan(C)
                current=M.combine((1,upper['current']),(1,hx['current']),(-1,hc['current']))
                coeff=M.combine((1,hx['coefficients']),(-1,hc['coefficients']))
                for node in p['nodes'][1:]:
                    child=M.REPAIR.local_decision(node['seed'],Q)
                    current=M.combine((1,current),(1,child['current']))
                    coeff=M.combine((1,coeff),(-1,{node['seed']:1}),(1,child['coefficients']))
                assert(current,coeff)==(p['current'],p['coefficients'])
    assert branches=={'odd','noncanonical','forward','critical'}
    for j in range(4,20):
        C,Q=585+4096*j,441+3072*j
        p=M.history_nine(C,Q)
        assert [x['seed']for x in p['nodes'][:3]]==[C,329+2304*j,185+1296*j]
        assert len(p['nodes'])==3
        generic.append(verify(p));node_counts.add(3)
    assert node_counts=={1,2,3}
    for C in(15401,16969,20009,12873):
        q0=(3*C+1)//4
        for Q in range(max(11547,q0-4)|1,q0+8,2):
            if 3*C+1<4*Q and Q<=3*C:thresholds.append(verify(M.history_nine(C,Q)))
            else:reject(lambda C=C,Q=Q:M.history_nine(C,Q))
    boundary_case=M.B.absorption_plan(15401)
    assert M.N.step(15401)==11551 and any(M.B.rho(u)==11551 for u in boundary_case['coefficients'])

    first=[];cells=[];origins=[]
    for d in list(range(2,19))+[32,64,128]:
        for i in(0,1,2**32):
            cell=M.depth_cell(d,i);m=cell['m'];data=M.first_run(m)
            assert data['parameters']['d']==d
            assert M.RUN.parameters(3*data['seed'])[0]==4
            x=3*data['seed']
            for _ in range(data['quotient_length']):x=M.N.quotient_step(x)
            assert x==M.N.normal_form(data['endpoint'])
            left,right=3*data['seed'],data['endpoint']
            for _ in range(data['ordinary_clocks'][0]):left=step(left)
            for _ in range(data['ordinary_clocks'][1]):right=step(right)
            assert left==right
            cells.append([d,i,cell['residue'],cell['modulus'],verify(data)])
    for m in list(range(64))+[16*2**32,16*2**96]:first.append(verify(M.first_run(m)))
    for m in(0,1,16,2736):
        data=M.origin(m);origins.append(verify(data))
        for relation in data['lower_relations']:
            target=M.combine(*[(-c,M.B.T.pair_source(u))for u,c in relation['coefficients'].items()])
            assert div(relation['current'])==target
        extended=M.extend_origin(m,M.first_run(m));verify(extended)
    assert M.first_run(10,False)['high']=={117740030521:1}

    coupled=[];cancellations=[];inherited=[];odd_failure=False;even_failure=False
    for i in list(range(64))+[2**32,2**32+1,2**96,2**96+1]:
        p=M.coupled_continuation(i);coupled.append(verify(p))
        if p['branch']=='selected_Z':odd_failure|=bool(p['high'])
        else:even_failure|=bool(p['high'])
    assert odd_failure and even_failure
    for i in(0,1,2,3,4,7,15,2**32,2**96):
        data=M.coupled_cancellation(i,inherited=i<3)
        verify(data);verify(data['negative_plan'])
        q=data['threshold'];params=data['parameters']
        assert data['old_coefficients'][params['b']]==-1
        assert all(M.B.rho(u)<q for u in data['negative_plan']['coefficients'])
        assert not NORMALIZER.bridge(params['a'])
        assert not NORMALIZER.bridge(params['b'])
        record=[i,verify(data),verify(data['negative_plan'])]
        cancellations.append(record)
        if'inherited'in data:
            full=data['inherited'];verify(full)
            delta=M.combine((1,full['current']),(-1,full['fresh_current']))
            dc=M.combine((1,full['coefficients']),(-1,full['fresh_coefficients']))
            inherited.append(dict(index=i,current=rows(delta),coefficients=rows(dc)))
            assert all(M.B.rho(u)<q for u in dc)
    assert inherited[0]['current'] and inherited[0]['coefficients']
    for i in(2,6,10,14):
        p=M.coupled_continuation(i)
        if p.get('d')==2:
            Z,g=p['parameters']['Z'],p['raw_target']
            assert g==(27*Z+19)//16 and 8*(2*g+1)//27-1==Z
            assert (2*g+1)%27==0 and (2*g+1)%81!=0
            v=p['parameters']['v']
            assert 2**18*g==3**13*v+1161985
    # Exact coefficient comparison refutes the proposed recurrent contraction.
    assert 3**12>2**19

    goodm=M.depth_cell(9)['m']
    designated=[M.history_nine(16969,12729),M.extend_origin(goodm,M.first_run(goodm)),M.coupled_continuation(1)]
    demonstrations=[]
    for i,data in enumerate(designated):
        assert not data['high'];verify(data)
        if stored is None:supplied={u:pair_supply(u)for u in data['coefficients']}
        else:supplied={int(u):dict(table)for u,table in stored['demonstrations'][i]['supplied'].items()}
        assert set(supplied)==set(data['coefficients'])
        for u,table in supplied.items():assert div(table)=={3*u:1,u:-1}
        output=M.compile_plan(data,supplied)
        assert div(output)=={3*data['seed']:1,data['seed']:-1}
        firstkey=next(iter(supplied))
        reject(lambda:M.compile_plan(data,{}))
        reject(lambda:M.compile_plan(data,{**supplied,firstkey:{}}))
        reject(lambda:M.compile_plan(data,{**supplied,firstkey:{3:True}}))
        demonstrations.append(dict(seed=data['seed'],threshold=data['threshold'],
            current=rows(data['current']),coefficients=rows(data['coefficients']),
            supplied={str(u):rows(table)for u,table in sorted(supplied.items())},
            output=rows(output),output_rows=len(output)))
    good=designated[0]
    invalid=[lambda:M.history_nine(True,12729),lambda:M.history_nine(16969,True),
        lambda:M.history_nine(16969,11545),lambda:M.history_nine(16969,12728),
        lambda:M.history_nine(16971,12729),lambda:M.history_nine(16969,3*16969+2),
        lambda:M.history_nine(15401,11551),lambda:M.history_nine(16969,12729,0),
        lambda:M.history_nine(16969,12729,True),lambda:M.history_nine(16969,12729,1),
        lambda:M.history_nine(16969,12729,2),lambda:M.depth_cell(1),lambda:M.depth_cell(True),
        lambda:M.remaining_cell(-1),lambda:M.remaining_cell(True),lambda:M.coupled_parameters(-1),
        lambda:M.coupled_parameters(True),lambda:M.raw_decision(9,11547),
        lambda:M.raw_decision(6*11547+1,11547),
        lambda:M.compile_plan(dict(good,current={3:True}),{}),
        lambda:M.compile_plan(dict(good,current={3:1}),{}),
        lambda:M.compile_plan(dict(good,threshold=True),{}),
        lambda:M.compile_plan(dict(good,threshold=12728),{}),
        lambda:M.compile_plan(dict(good,threshold=3*good['seed']+2),{}),
        lambda:M.compile_plan(M.coupled_continuation(4),{}),
        lambda:M.extend_origin(0,M.first_run(1))]
    for call in invalid:reject(call)
    return dict(schema=1,status='PASS',scope='Conditional larger W9 window and retained-cell histories; no universal current supply.',
        generic_cases=len(generic),generic_hash=digest(generic),branches=sorted(branches),node_counts=sorted(node_counts),
        threshold_cases=len(thresholds),threshold_hash=digest(thresholds),first_runs=len(first),first_hash=digest(first),
        exact_depth_cells=len(cells),depth_hash=digest(cells),full_origins=len(origins),origin_hash=digest(origins),
        coupled_decisions=len(coupled),coupled_hash=digest(coupled),signed_cancellations=len(cancellations),
        cancellation_hash=digest(cancellations),inherited_lower_relations=inherited,
        sharp_control=dict(source=16969,threshold=12729,nodes=[16969,9545,5369]),
        boundary_control=dict(source=15401,threshold=11551,coefficients=rows(boundary_case['coefficients'])),
        demonstrations=demonstrations,rejections=len(invalid)+9,supply_caps=dict(arrows=ARROW_CAP,bits=BIT_CAP),
        source_hashes=source_hashes())

def main():
    assert not sys.flags.optimize,'Run without optimization'
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write-receipt',action='store_true');args=parser.parse_args()
    path=HERE/'retained_history_audit.json'
    stored=None if args.write_receipt else json.loads(path.read_text())
    result=audit(stored)
    if args.write_receipt:path.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
    else:assert result==stored,'Receipt mismatch: inspect evidence and source changes'
    print('PASS retained histories: '+json.dumps({k:result[k]for k in('generic_cases','threshold_cases','first_runs','exact_depth_cells','full_origins','coupled_decisions','signed_cancellations','rejections')}))
    print('supplied output rows', [x['output_rows']for x in result['demonstrations']])
if __name__=='__main__':main()
