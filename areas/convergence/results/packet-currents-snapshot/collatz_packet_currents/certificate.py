#!/usr/bin/env python3
"""Exact-source packet and signed-current certificate.

The general remainder and current lemmas are proved in research_note.md.
The current-size bounds recorded here apply only to the named finite cutoffs.
No uniform O(N) current theorem or Collatz convergence claim is made.
Python 3.10+, standard library only; run without -O.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb
from pathlib import Path
import csv,hashlib,json,time

ROOT=Path(__file__).resolve().parent
COUNT=Counter()


def step(x:int)->tuple[int,int]:
    if x<=0 or x%2==0:
        raise ValueError('positive odd integer required')
    z=3*x+1
    a=(z&-z).bit_length()-1
    return z>>a,a


def push(mu:dict[int,int])->dict[int,int]:
    result=defaultdict(int)
    for y,c in mu.items():
        z,_=step(y)
        if z>1:result[z]+=c
    return {y:c for y,c in result.items() if c}


def add(*measures):
    z=defaultdict(int)
    for mu in measures:
        for y,c in mu.items():z[y]+=c
    return {y:c for y,c in z.items() if c}


def negative(mu):return {y:-c for y,c in mu.items()}
def norm(mu):return sum(abs(c) for c in mu.values())


def initial(N):
    n1=(3*N+1)//2;n2=(3*N+1)//4
    return {x:3*int(x%3==2)-1+(3*int(x%3==1)-1 if x<=n2 else 0)
            for x in range(3,n1+1,2)}


def words(total,depth):
    for cuts in combinations(range(1,total),depth-1):
        points=(0,)+cuts+(total,)
        yield tuple(points[i+1]-points[i] for i in range(depth))


def affine(w):
    A=C=0
    for a in w:C=3*C+(1<<A);A+=a
    return A,C


def source_packets(N:int,d:int):
    b=(N-1).bit_length()
    if not 1<=d<=b//2:
        raise ValueError('require 1<=d<=ceil(log2 N)/2')
    endpoints=((3*N+1)//2,(3*N+1)//4)
    p3=3**d
    packet=defaultdict(int);fringe=defaultdict(int)
    nwords=triples=0
    for A in range(d,b+1):
        period=1<<(A+1)
        inv=pow(p3,-1,period)
        for w in words(A,d):
            _,C=affine(w);nwords+=1
            q=(((1<<A)-C)*inv)%period
            e,rem=divmod(p3*q+C,1<<A)
            assert rem==0 and q>0 and q%2 and e>0 and e%2
            first=0 if q>1 and e>1 else 1
            for i,hi in enumerate(endpoints):
                last=(hi-q)//period
                size=max(0,last-first+1)
                full=size//3
                for index in range(full):
                    t=first+3*index
                    total_coeff=0
                    for j in range(3):
                        x=q+period*(t+j);y=e+2*p3*(t+j)
                        c=3*int(x%3==(2 if i==0 else 1))-1
                        packet[y]+=c;total_coeff+=c
                        assert 1<x<=hi and y>1
                    assert total_coeff==0
                    triples+=1
                local=[]
                for t in range(first+3*full,last+1):
                    x=q+period*t;y=e+2*p3*t
                    c=3*int(x%3==(2 if i==0 else 1))-1
                    fringe[y]+=c;local.append(c)
                assert len(local)<=2 and sum(map(abs,local))<=3
    assert nwords==comb(b,d)
    packet={y:c for y,c in packet.items() if c}
    fringe={y:c for y,c in fringe.items() if c}
    assert sum(packet.values())==0
    COUNT['words_constructed']+=nwords;COUNT['zero_sum_source_triples']+=triples
    return packet,fringe,nwords,triples


def actual_budget_split(N,d):
    b=(N-1).bit_length()
    mu=defaultdict(int);tail=defaultdict(int);short=defaultdict(int)
    high=0
    for x,c in initial(N).items():
        y=x;A=0
        for _ in range(d):y,a=step(y);A+=a;COUNT['source_prefix_steps']+=1
        if A>b:high+=1
        if y==1:continue
        mu[y]+=c
        (tail if A>b else short)[y]+=c
    clean=lambda m:{y:c for y,c in m.items() if c}
    mu,tail,short=map(clean,(mu,tail,short))
    assert high<=sum(comb(b,j) for j in range(d))
    assert norm(tail)<=2*sum(comb(b,j) for j in range(d))
    return mu,short,tail


def construct_current(mu:dict[int,int],core=31,path_cap=2000):
    # Explore only finite paths to the core. Abort on a new cycle or cap.
    # This constructs a certificate, not a theorem that the exploration must end.
    depth={x:0 for x in range(1,core+1,2)}
    nxt={};maxstate=0
    for src in mu:
        path=[];seen=set();y=src
        while y not in depth:
            if y in seen:raise RuntimeError(f'unresolved non-core cycle at {y}')
            if len(path)>=path_cap:raise RuntimeError('unresolved path cap')
            seen.add(y);path.append(y)
            z,_=step(y);nxt[y]=z;y=z
            maxstate=max(maxstate,y)
        d=depth[y]
        for y in reversed(path):d+=1;depth[y]=d
    incoming=defaultdict(int,mu);J={}
    for y in sorted(nxt,key=depth.get,reverse=True):
        c=incoming.pop(y,0)
        if c:J[y]=c;incoming[nxt[y]]+=c
    residual={y:c for y,c in incoming.items() if c and y>1}
    assert all(y<=core for y in residual)
    # Complete the finite small-core graph; total graph is still checked by edges.
    complete=defaultdict(int,J)
    for y,c in residual.items():
        seen=set()
        while y>1:
            if y in seen:raise RuntimeError('small core did not terminate')
            seen.add(y);complete[y]+=c;y,_=step(y)
    complete={y:c for y,c in complete.items() if c}
    assert add(complete,negative(push(complete)))==mu
    COUNT['current_identity_atoms']+=len(complete)
    return complete,dict(nonzero_current_states=len(complete),explored_states=len(nxt),
        longest_explored_prefix=max(depth.values()),largest_explored_integer=maxstate,
        pre_core_current_states=len(J),core_residual_states=len(residual))


def exact_current_check(mu,J):
    # Pure one-step verifier. No stopping-time or future-orbit routine is called.
    diff=defaultdict(int)
    for y,c in J.items():
        if not isinstance(c,int) or y<=1 or y%2==0:raise ValueError('invalid current row')
        diff[y]+=c
        z,_=step(y)
        if z>1:diff[z]-=c
    diff={y:c for y,c in diff.items() if c}
    assert diff==mu
    return sum(c for c in J.values() if c>0),-sum(c for c in J.values() if c<0)


def path_to(x,z,cap=1000):
    path=[]
    while x!=z:
        if x==1 or len(path)>=cap:raise RuntimeError('meeting point not certified')
        path.append(x);x,_=step(x)
    return path


def witness(ys,weights,root):
    assert sum(weights)==0
    paths=[path_to(y,root) for y in ys]
    delays=list(map(len,paths));knots=sorted(set([0]+delays))
    values=[sum(c*min(t,d) for c,d in zip(weights,delays)) for t in knots]
    J=defaultdict(int)
    for path,c in zip(paths,weights):
        for y in path:J[y]+=c
    J={y:c for y,c in J.items() if c}
    mu={y:c for y,c in zip(ys,weights) if c}
    up,down=exact_current_check(mu,J)
    # Test robustness on arbitrarily chosen unknown remaining times, including
    # a simulated infinite remaining time. This is arithmetic, not an assertion
    # that the actual root has any of these fates.
    for tail in [0,1,7,100,10000,None]:
        for L in range(151):
            lhs=sum(c*(L if tail is None else min(L,d+tail)) for c,d in zip(weights,delays))
            u=0 if tail is None else max(0,L-tail)
            rhs=sum(c*min(u,d) for c,d in zip(weights,delays))
            assert lhs==rhs and min(values)<=lhs<=max(values)
            COUNT['tail_independent_lag_checks']+=1
    return dict(sources=ys,weights=weights,meeting_state=root,delays=delays,
        knots=knots,profile_at_knots=values,uniform_lower=min(values),uniform_upper=max(values),
        current_positive=up,current_negative=down,paths_to_meeting=paths)


def write_current(N,d,mu,J):
    for name,data in [(f'packets_{N}.csv',mu),(f'current_{N}.csv',J)]:
        with (ROOT/'data'/name).open('w') as f:
            w=csv.writer(f);w.writerow(['state','weight']);w.writerows(sorted(data.items()))
    return dict(N=N,depth=d,packets=f'packets_{N}.csv',current=f'current_{N}.csv')


def remainder_examples():
    result=[]
    for b in [64,128,256,512,1024]:
        m=2*b//9
        D=6*comb(b,m)+2*sum(comb(b,j) for j in range(m))
        Told=(b+1)*(1<<((b+4)//5))
        value=Fraction(Told*D,1<<b)
        result.append(dict(b=b,m=m,D=str(D),time_upper=str(Told),
            error_over_N_exact=str(value),error_over_N_approx=float(value)))
    assert 9**9<2**9*7**7
    assert 8**9*2**7<16**9
    for b in range(9,1025):
        m=2*b//9
        D=6*comb(b,m)+2*sum(comb(b,j) for j in range(m))
        assert D**9<=16**9*2**(7*(b-1))
    COUNT['source_power_inequalities']+=1016
    return result


def main():
    start=time.monotonic()
    (ROOT/'data').mkdir(exist_ok=True)
    table=[];manifests=[]
    cutoffs=[2**b for b in range(9,19)]+[513,999,4097,10001]
    for N in cutoffs:
        b=(N-1).bit_length();d=2*b//9
        pi,fringe,nwords,ntriples=source_packets(N,d)
        mu,short,tail=actual_budget_split(N,d)
        assert add(pi,fringe)==short
        eta=add(mu,negative(pi))
        assert eta==add(fringe,tail)
        D=6*comb(b,d)+2*sum(comb(b,j) for j in range(d))
        assert norm(fringe)<=6*comb(b,d) and norm(eta)<=D
        J,info=construct_current(pi)
        up,down=exact_current_check(pi,J)
        # Verify the current/absorption identity under actual finite push for
        # selected small and large examples without using the formula to iterate.
        if N in (512,4096,262144):
            v=pi;acc=0
            for L in range(81):
                assert -down<=acc<=up
                if L<80:acc+=sum(v.values());v=push(v)
                COUNT['finite_all_horizon_sanity_checks']+=1
        record=dict(N=N,b=b,depth=d,word_count=nwords,raw_triples=ntriples,
            packet_norm=norm(pi),packet_atoms=len(pi),actual_remainder_norm=norm(eta),
            remainder_bound=D,uniform_signed_upper=up,uniform_signed_lower=-down,
            upper_over_N=float(Fraction(up,N)),**info)
        table.append(record)
        print(json.dumps(record),flush=True)
        if N in (4096,262144):manifests.append(write_current(N,d,pi,J))
    ws=[witness([6929,6947,6965],[-1,-1,2],23),
        witness([55,73,91],[1,1,-2],91),
        witness([13,5],[1,-1],5)]
    assert ws[0]['uniform_lower']==-75 and ws[0]['uniform_upper']==0
    assert ws[1]['uniform_lower']==0 and ws[1]['uniform_upper']==17
    assert ws[2]['uniform_upper']==1
    result=dict(status='Exact finite checks passed. No uniform-in-N current bound proved.',
        counts=dict(COUNT),table=table,witnesses=ws,remainder_examples=remainder_examples(),
        current_files=manifests,elapsed_seconds=round(time.monotonic()-start,3))
    # remainder_examples adds counters, so serialize final count state here.
    result['counts']=dict(COUNT)
    (ROOT/'certificate_results.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'lag_witnesses.json').write_text(json.dumps(ws,indent=2)+'\n')
    (ROOT/'remainder_examples.json').write_text(json.dumps(result['remainder_examples'],indent=2)+'\n')
    print('ALL EXACT ASSERTIONS PASSED',flush=True)
    print(json.dumps(dict(counts=dict(COUNT),elapsed_seconds=result['elapsed_seconds']),indent=2))

if __name__=='__main__':main()
