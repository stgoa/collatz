"""Exact Phi returns and the complete maximal-exit alphabet.

All formal currents retain their signed pair premises. No absorption search,
new dispatcher rule, or universal terminal-current supply is implemented.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location('phi_retained', HERE.parent/'retained_history/retained_history.py')
R = module_from_spec(SPEC)
SPEC.loader.exec_module(R)
A, B, M, D = 3**12, 299947, 2**19, 7153
GUARD, GUARD_MOD = 133797, 2**18
V0, VP = 67839005952677, 2**18*3**18
Q0, QP = 70506316836123, 3*2**45
RAW_WORD = (1,1,1,1,3,1,4,1,2,1,1,2)
CANONICAL_WORD = (1,1,1,2,1,1,4,1,2,1,1,2)


def integer(x, lower=0):
    if type(x) is not int or x < lower:
        raise ValueError('Require an integer at least '+str(lower))


def order(x, prime=2):
    integer(x, 1)
    if prime not in (2,3):
        raise ValueError('Only binary and ternary orders are used')
    answer = 0
    while x % prime == 0:
        answer += 1
        x //= prime
    return answer


def original(index):
    integer(index)
    data = R.remaining_cell(2736+4096*index)
    assert data['v'] == V0+VP*index and data['Q'] == Q0+QP*index
    assert 3**17*data['Q'] == 2**27*data['v']-213949807
    return dict(data, index=index)


def guard_order(v):
    integer(v, 1)
    if v % GUARD_MOD != GUARD:
        raise ValueError('Require the complete binary Phi guard')
    return order(D*v+B)


def maximum_reentries(v):
    return (guard_order(v)-18)//19


def reenter(v):
    if guard_order(v) < 37:
        raise ValueError('This source exits the guard')
    result = (A*v+B)//M
    assert M*result == A*v+B and result > v
    assert guard_order(result) == guard_order(v)-19
    return result


def repeat_parameters(count, index=0):
    """Complete original-cell starts allowing at least count re-entries."""
    integer(count); integer(index)
    precision = 19*count+18
    residue = (-B*pow(D,-1,2**precision)) % 2**precision
    modulus = 2**(19*count)
    first = ((residue-V0)//GUARD_MOD*pow(3**18,-1,modulus)) % modulus
    data = original(first+modulus*index)
    assert data['v'] % 2**precision == residue
    return dict(data, count=count, residue=residue, binary_precision=precision,
                index_residue=first, index_modulus=modulus)


def repeat_comparison(count, index=0, max_arrows=10000):
    integer(count); integer(max_arrows,1)
    if 23+12*count > max_arrows:
        raise ValueError('Ordinary prefix exceeds the explicit cap')
    data = repeat_parameters(count,index)
    q, v = data['Q'], data['v']
    sequence = [v]
    for _ in range(count):
        v = reenter(v)
        sequence.append(v)
    left, right = R.prefix(q,23+12*count), R.prefix(3*v,5)
    assert left['endpoint'] == right['endpoint']
    comparison = R.combine((1,left['current']),(-1,right['current']))
    hv,hb = R.B.absorption_plan(v),R.B.absorption_plan(q//3)
    result = R.finish(q//3,q,
        R.combine((1,comparison),(1,hv['current']),(-1,hb['current'])),
        R.combine((1,{v:1}),(1,hv['coefficients']),(-1,hb['coefficients'])),
        parameters=data, sequence=sequence, comparison=comparison,
        ordinary_clocks=[23+12*count,5], quotient_length=18+12*count,
        rule='guarded_Phi_comparison')
    assert result['coefficients'][v] == 1 and R.B.rho(v)==3*v>q
    assert all(R.B.rho(u)<3*v for u in result['coefficients']if u!=v)
    assert all(c>0 for c in result['high'].values())
    return result


def exit_row(h):
    """Maximal fixed ordinary prefix, then one arbitrary exact valuation."""
    integer(h,18)
    if h>36:
        raise ValueError('Residual guard order is between18 and36')
    modulus = 2**(h+1)
    residue = ((2**h-B)*pow(D,-1,modulus)) % modulus
    alpha,beta = 6*modulus,6*residue+1
    word=[];constant=1;exponent=0
    for _ in range(64):
        aa,bb=3*alpha,3*beta+1
        p,q=order(aa),order(bb)
        if q>=p:
            assert p==h+2-exponent
            return dict(h=h,residue=residue,modulus=modulus,word=word,
                length=len(word),valuation_sum=exponent,min_next=p,
                alpha=alpha,beta=beta,affine_constant=constant,
                next_odd_coefficient=aa//2**p,next_constant=bb//2**p)
        word.append(q)
        alpha,beta=aa//2**q,bb//2**q
        constant,exponent=3*constant+2**exponent,exponent+q
    raise RuntimeError('Unexpected fixed-prefix bound failure')


def exit_parameters(count,h,next_valuation,index=0):
    """Complete cell: exactly count returns, exact h, exact next valuation."""
    integer(count);integer(index);integer(next_valuation,1)
    row=exit_row(h)
    if next_valuation<row['min_next']:
        raise ValueError('Next valuation is below the complete row minimum')
    j=next_valuation-row['min_next']; tm=2**(j+1)
    tr=((2**j-row['next_constant'])*pow(row['next_odd_coefficient'],-1,tm))%tm
    exit_residue=row['residue']+row['modulus']*tr
    exit_precision=h+j+2
    ar,mr=A**count,M**count
    shift=B*(ar-mr)//D
    precision=19*count+exit_precision
    vresidue=((mr*exit_residue-shift)*pow(ar,-1,2**precision))%2**precision
    index_modulus=2**(precision-18)
    first=((vresidue-V0)//GUARD_MOD*pow(3**18,-1,index_modulus))%index_modulus
    data=original(first+index_modulus*index)
    v=(ar*data['v']+shift)//mr
    assert mr*v==ar*data['v']+shift and guard_order(v)==h
    assert maximum_reentries(data['v'])==count
    length=18+12*count+row['length']+1
    exponent=26+19*count+row['valuation_sum']+next_valuation
    assert exponent+1-45==precision-18
    return dict(data,count=count,h=h,next_valuation=next_valuation,row=row,
        exit_v=v,exit_residue=exit_residue,exit_precision=exit_precision,
        index_residue=first,index_modulus=index_modulus,
        total_length=length,total_valuation_sum=exponent,
        target_increment=2*3**(length+1))


def raw_test(data):
    """Exact y<Q inequality, not a necessity test for all formal currents."""
    r=data['count'];row=data['row'];a=data['next_valuation']
    ar,mr=A**r,M**r;shift=B*(ar-mr)//D
    ell,e,c=row['length'],row['valuation_sum'],row['affine_constant']
    den=mr*2**(e+a);cs=3*c+2**e
    num=6*3**(ell+1)*(ar*data['v']+shift)+mr*cs
    assert num%den==0
    bracket=2**27*den-6*3**(ell+18)*ar
    rhs=3**17*(6*3**(ell+1)*shift+mr*cs)+213949807*den
    return dict(target=num//den,bracket=bracket,rhs=rhs,
                below_original=bracket*data['v']>rhs)


def point_shadow(data):
    """Point-depth limit from a nonintegral rational centre; no ray exclusion."""
    shadow=Fraction(-1792529,D)
    word=data['row']['word']+[data['next_valuation']]
    for a in word:shadow=(3*shadow+1)/2**a
    assert shadow.denominator%D==0 and shadow!=-1
    depth=order(abs((shadow+1).numerator),3)
    return dict(numerator=shadow.numerator,denominator=shadow.denominator,
        point_depth=depth,ternary_precision=12*data['count']+4+len(word)+1)


def exit_comparison(count,h,next_valuation,index=0,max_arrows=10000):
    integer(max_arrows,1)
    data=exit_parameters(count,h,next_valuation,index)
    if data['total_length']>max_arrows:
        raise ValueError('Ordinary prefix exceeds the explicit cap')
    row=data['row'];word=row['word']+[next_valuation]
    tail=R.prefix(6*data['exit_v']+1,len(word),word)
    upper=R.prefix(data['Q'],data['total_length'])
    assert upper['endpoint']==tail['endpoint']
    test=raw_test(data);y=test['target'];q=data['Q']
    assert y==upper['endpoint'] and (y<q)==test['below_original']
    hy,hb=R.B.absorption_plan(y),R.B.absorption_plan(q//3)
    assert all(c>0 for c in hy['coefficients'].values())
    assert all(R.B.rho(u)<q for u in hb['coefficients'])
    result=R.finish(q//3,q,
        R.combine((1,upper['current']),(1,hy['current']),(-1,hb['current'])),
        R.combine((1,hy['coefficients']),(-1,hb['coefficients'])),
        parameters=data,raw_test=test,point_shadow=point_shadow(data),
        comparison=upper['current'],ordinary_clocks=[data['total_length'],0],
        rule='complete_Phi_exit_comparison')
    assert all(c>0 for c in result['high'].values())
    return result


def ancestor_exponent(target,anchor,power):
    """Modular certificate for the ancestor-cover statement, without huge 2^e.

    Return e modulo2*3^power with 2^e*target=3*anchor+1 mod3^(power+1).
    Taking a sufficiently large representative makes its predecessor enter
    the positive tail of the image progression. No absorption is inferred.
    """
    integer(target,1);integer(anchor,1);integer(power,1)
    if target%2!=1 or target%3==0 or anchor%2!=1:
        raise ValueError('Require an odd nonmultiple target and odd anchor')
    modulus=3**(power+1)
    wanted=(3*anchor+1)*pow(target,-1,modulus)%modulus
    exponent=0 if wanted%3==1 else 1
    period=2
    for k in range(1,power+1):
        candidates=[exponent+j*period for j in range(3)]
        matches=[e for e in candidates if pow(2,e,3**(k+1))==wanted%3**(k+1)]
        assert len(matches)==1
        exponent=matches[0];period*=3
    assert pow(2,exponent,modulus)*target%modulus==(3*anchor+1)%modulus
    return dict(exponent_residue=exponent,period=period,modulus=modulus)
