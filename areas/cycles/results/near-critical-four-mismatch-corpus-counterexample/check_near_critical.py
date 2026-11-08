#!/usr/bin/env python3
"""Self-contained exact near-critical four-mismatch counterexample."""

import argparse
import json
from math import gcd
from pathlib import Path

WORD = (1,1,3,1,2,1,1,1,1,2,1,5)
STATES = (737,1253,2027,797,1343,1081,1769,2801,4349,6671,5077,7763)


def require(condition,message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    c,total=0,0
    for a in word:
        c=3*c+(1 << total)
        total+=a
    return c


def compute():
    w=WORD
    m,A=len(w),sum(w)
    C=intercept(w)
    D=(1 << A)-3**m
    G=gcd(C,D)
    e=gcd(A,m)
    require((m,A,C,D,G,e) == (12,20,1291961,517135,1753,4),'arithmetic mismatch')
    require(D>0 and m>=9 and min(w)>0,'counterexample misses scope')
    require(3**m < (1 << A) < 2*3**m,'word is not near-critical')
    require(G*G > (1 << A),'plain half bound is not violated')
    x,y=1 << (A//e),3**(m//e)
    phi4=x*x+y*y
    require((x-y)*(x+y)*phi4 == D,'homogeneous cyclotomic factorization')
    primitive_gcd=gcd(G,phi4)
    require(phi4 == 1753 and primitive_gcd == 1753,'wrong primitive factor')
    require(primitive_gcd*primitive_gcd > (1 << A),'primitive half bound is not violated')
    counts={str(h):sum(w[i]!=w[(i+h)%m] for i in range(m)) for h in range(1,m)}
    require(list(counts.values()) == [8,6,7,8,4,8,4,8,7,6,8],'rotation mismatch counts')
    require(min(counts.values()) == 4 and all(c>0 for c in counts.values()),
            'rotation distance or primitivity fails')
    minimizing=[int(h) for h,c in counts.items() if c==4]
    require(minimizing == [5,7] and all(gcd(h,m)==1 for h in minimizing),
            'wrong minimizing shifts')
    q=D//G
    require(q==295 and C//G==737 and gcd(C//G,q)==1,'wrong reduced cycle')
    require(len(set(STATES))==m and min(STATES)==737,'cycle is not primitive')
    arrows=[]
    for i,state in enumerate(STATES):
        require(state>0 and state%2==1,'invalid positive state')
        numerator=3*state+q
        valuation=(numerator & -numerator).bit_length()-1
        successor=numerator//(1 << valuation)
        require(valuation==w[i] and successor==STATES[(i+1)%m],'invalid exact cycle arrow')
        rotated=w[i:]+w[:i]
        require(intercept(rotated)==G*state,'rotated intercept disagrees with cycle')
        arrows.append(dict(start=state,valuation=valuation,end=successor))
    weak_left=G**4*4**m
    weak_right=2**(4*A)*3**m
    require(weak_left<weak_right,'weaker denominator candidate unexpectedly fails')
    return dict(word=list(w),m=m,A=A,C=C,D=D,G=G,e=e,
                homogeneous_phi4=dict(x=x,y=y,value=phi4),primitive_cancellation=primitive_gcd,
                near_critical_inequalities=dict(three_power=3**m,two_power=1 << A,
                                               twice_three_power=2*3**m),
                cancellation_square=G*G,primitive=True,rotation_distance=4,
                mismatch_counts=counts,minimizing_shifts=minimizing,
                reduced_denominator=q,states=list(STATES),arrows=arrows,
                weaker_denominator_candidate=dict(left=weak_left,right=weak_right,holds=True))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt',action='store_true')
    args=parser.parse_args()
    result=compute()
    receipt=Path(__file__).with_suffix('.json')
    if args.write_receipt:
        receipt.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:
        require(receipt.exists(),'Missing receipt.')
        require(json.loads(receipt.read_text())==result,'Receipt mismatch.')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
