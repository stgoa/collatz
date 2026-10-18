"""Three strictly shrinking paired-current branches, with explicit cylinders.

Recognition always terminates. Unhandled cases remain unresolved.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=spec_from_file_location('mixed_old_pairs',HERE.parent/'second_return/paired_return.py')
OLD=module_from_spec(spec);spec.loader.exec_module(OLD)
NORMAL=OLD.NORMAL
step,combine,divergence,prefix=OLD.step,OLD.combine,OLD.divergence,OLD.prefix


def reduction(w):
    if not isinstance(w,int) or w<=0 or w%8!=3:
        raise ValueError('Require a positive integer w=3 modulo8')
    h=NORMAL.valuation2(3*w-1)
    if h%2:
        k=(h-3)//2
        z=3**k*((3*w-1)//2**h)
        if z%8!=3:
            return dict(kind='unresolved',w=w,h=h,k=k,z=z,reason='odd h, z not3 modulo8')
        child=z
        result=dict(kind='O',w=w,h=h,k=k,z=z,child=child,sign=1)
    else:
        k=h//2-1
        z=3**k*((3*w-1)//2**h)
        if NORMAL.canonical(z):
            return dict(kind='terminal',w=w,h=h,k=k,z=z)
        if z%64==29:
            kind,child='E1',(3*z+1)//8
        elif z%128==101:
            kind,child='E2',(3*z+1)//16
        else:
            return dict(kind='unresolved',w=w,h=h,k=k,z=z,reason='even h, unhandled z')
        result=dict(kind=kind,w=w,h=h,k=k,z=z,child=child,sign=-1)
    assert child>0 and 2*child<w and child%8==3
    A,B,p=affine(result['kind'],k)
    assert A*w+B==2**p*child
    return result


def plan(w):
    origin,layers=w,[]
    while True:
        row=reduction(w)
        layers.append(row)
        if row['kind'] in ('terminal','unresolved'):
            return dict(origin=origin,accepted=row['kind']=='terminal',layers=layers)
        w=row['child']


def affine(kind,k):
    """Child=(A*w+B)/2^p. Domain is exactly child=3 modulo8."""
    if kind=='O' and isinstance(k,int) and k>=0:
        return 3**(k+1),-3**k,2*k+3
    if kind in ('E1','E2') and isinstance(k,int) and k>=1:
        return 3**(k+2),4**(k+1)-3**(k+1),2*k+(5 if kind=='E1' else 6)
    raise ValueError('Require O,k>=0 or E1/E2,k>=1')


def current(w):
    data=plan(w)
    if not data['accepted']:
        raise ValueError('This rule leaves the pair unresolved')
    result={}
    for row in reversed(data['layers']):
        v,k,z,kind=row['w'],row['k'],row['z'],row['kind']
        if kind=='terminal':
            result=OLD.pair_current(v)['current']
        elif kind=='O':
            child=row['child']
            left,L=prefix(3*v,k+1)
            right,R=prefix(v,k+1)
            assert left[-1]==6*child+1 and right[-1]==4*child+1
            partner=NORMAL.bridge(6*child+1)
            assert partner['minimum']==3*child
            L=combine((1,L),(1,partner['current']))
            R=combine((1,R),(1,{4*child+1:1}),(-1,{child:1}))
            local=combine((1,L),(-1,R))
            assert divergence(local)==combine((1,{3*v:1}),(-1,{v:1}),
                                               (-1,{3*child:1}),(1,{child:1}))
            result=combine((1,local),(1,result))
        else:
            child=row['child']
            left,L=prefix(3*v,k+1)
            assert left[-1]==child
            if kind=='E1':
                right,R=prefix(v,k+3)
                assert right[-1]==6*child+1
                partner=NORMAL.bridge(6*child+1)
                assert partner['minimum']==3*child
                R=combine((1,R),(1,partner['current']))
            else:
                right,R=prefix(v,k+4)
                assert right[-1]==step(3*child)
                R=combine((1,R),(-1,{3*child:1}))
            local=combine((1,L),(-1,R))
            assert divergence(local)==combine((1,{3*v:1}),(-1,{v:1}),
                                               (1,{3*child:1}),(-1,{child:1}))
            result=combine((1,local),(-1,result))
        assert divergence(result)=={v:-1,3*v:1}
    return dict(plan=data,current=result)


def merge_clock(data):
    if not data['accepted']:
        raise ValueError('The pair is unresolved')
    end=data['layers'][-1]
    length=end['k']+NORMAL.valuation2(2*end['z']+2)
    for row in reversed(data['layers'][:-1]):
        length+=row['k']+(1 if row['kind']=='O' else 2)
    return length


def word_cylinder(word,terminal_k=1):
    """Complete cylinder realizing this exact word, then z=1 modulo8."""
    residue,modulus=OLD.terminal_cylinder(terminal_k)
    for kind,k in reversed(word):
        A,B,p=affine(kind,k)
        modulus*=2**p
        residue=((2**p*residue-B)*pow(A,-1,modulus))%modulus
        assert residue%8==3
    return residue,modulus


def mersenne_cylinder(word,terminal_k=1):
    return OLD.mersenne_exponent_cylinder(*word_cylinder(word,terminal_k))


def mersenne_bridge(a):
    if not isinstance(a,int) or a<7 or a%16!=7:
        raise ValueError('Require a>=7, a=7 modulo16')
    x,q,N=2**a-1,2**(a-1)-1,12*2**(a-4)
    w=(3**(a-1)-1)//8
    paired=current(w)
    original=OLD.RUN.normalized_bridge(x)
    path,rows=prefix(q,a-1)
    assert path[-1]==w and original['target']==3*w>x and q<N
    result=combine((1,original['current']),(1,paired['current']),(-1,rows))
    assert divergence(result)=={q:-1,x:1}
    length=a+merge_clock(paired['plan'])
    return dict(a=a,N=N,root=x,lower_seed=q,w=w,old_return=3*w,
                plan=paired['plan'],current=result,merge_clock=length)


def from_supplied_lower(a,lower_current,weight=1):
    if not isinstance(weight,int) or weight<1:
        raise ValueError('Require a positive integer weight')
    data=mersenne_bridge(a)
    assert divergence(lower_current)=={data['lower_seed']:1}
    signed=combine((weight,data['current']),(weight,lower_current))
    assert divergence(signed)=={data['root']:weight}
    extracted=OLD.RUN.H.COMPLEMENT.extract_exact({data['root']:weight},
                                                {x:step(x) for x in signed})
    assert divergence(extracted)=={data['root']:weight}
    return dict(data=data,signed_current=signed,current=extracted)
