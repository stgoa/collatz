#!/usr/bin/env python3
"""Discovery only: SciPy proposes supports; exact rational checks certify them.

Install SciPy separately to regenerate the supplied multipliers. The proof
checker and CI have no SciPy dependency. Output may use different valid sparse
supports across SciPy versions; every combination is checked exactly.
"""
from fractions import Fraction as F
import json
from pathlib import Path
from scipy.optimize import linprog
from check_four_arcs import cells

def exact_weights(rows,support):
    matrix=[[F(rows[j][i]) for j in support]+[F(0)] for i in range(4)]
    matrix.append([F(1)]*len(support)+[F(1)])
    rank=0;pivots=[]
    for col in range(len(support)):
        r=next((r for r in range(rank,5) if matrix[r][col]),None)
        if r is None:continue
        matrix[rank],matrix[r]=matrix[r],matrix[rank]
        divisor=matrix[rank][col]
        matrix[rank]=[x/divisor for x in matrix[rank]]
        for i in range(5):
            if i!=rank:
                k=matrix[i][col]
                matrix[i]=[x-k*y for x,y in zip(matrix[i],matrix[rank])]
        pivots.append(col);rank+=1
    if rank!=len(support):raise RuntimeError('nonbasic support')
    weights=[F(0)]*len(support)
    for i,col in enumerate(pivots):weights[col]=matrix[i][-1]
    if any(x<0 for x in weights):raise RuntimeError('negative exact weight')
    if any(sum(weights[k]*rows[j][i] for k,j in enumerate(support)) for i in range(4)):
        raise RuntimeError('nonzero exact coefficients')
    gap=sum(weights[k]*rows[j][4] for k,j in enumerate(support))
    if gap>=0:raise RuntimeError('no exact contradiction')
    return weights,gap


def main():
    proofs=[]
    gaps=[]
    for case, (key, rows) in enumerate(cells()):
        eq=[[r[i] for r in rows] for i in range(4)]+[[1]*len(rows)]
        sol=linprog([r[4] for r in rows], A_eq=eq,
                    b_eq=[0,0,0,0,1], bounds=(0,None), method='highs')
        if not sol.success or sol.fun>=0:
            raise RuntimeError((case, sol.message, sol.fun))
        support=[i for i,x in enumerate(sol.x) if x>1e-9]
        weights,gap=exact_weights(rows,support)
        proofs.append([[j,w.numerator,w.denominator]
                       for j,w in zip(support,weights)])
        gaps.append(gap)
    result={'scope':'All 1440 wrap/order cells, R=3/8, epsilon<=1/193',
            'proofs':proofs,
            'minimum_contradiction':str(min(-x for x in gaps)),
            'max_support':max(map(len,proofs))}
    path=Path(__file__).resolve().with_suffix('.json')
    path.write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps({'cells':len(proofs),'max_support':result['max_support'],
                      'minimum_contradiction':result['minimum_contradiction']}))


if __name__ == '__main__':
    main()
