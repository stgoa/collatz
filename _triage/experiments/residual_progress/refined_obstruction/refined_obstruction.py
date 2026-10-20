"""Whole R61/refined15 classification and a lifted inverse-cycle comparison.

All currents retain signed missing pair inputs. The new inverse rule has its
own complete failure table; it does not assume any of those inputs supplied.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent/relative)
    result = module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


ELEVEN = load('refined_obstruction_eleven', 'exit_continuation/exit_continuation.py')
FIFTEEN = load('refined_obstruction_fifteen', 'refined_rules/refined_rules.py')
OLD = FIFTEEN.CYCLE
RANK, NORMAL, T, NINE = OLD.RANK, OLD.NORMAL, OLD.T, OLD.NINE
combine, atoms, divergence, rho = OLD.combine, OLD.atoms, OLD.divergence, RANK.rho
WORD = (1, 1, 2, 1, 1, 4, 1)
TAIL = (2, 7, 1, 4)
THRESHOLDS = ((6,13), (12,12), (19,11), (25,10), (31,9), (37,8),
              (43,7), (49,6), (56,5), (62,4), (68,3), (74,2), (80,1))


def point_threshold(k):
    if not isinstance(k, int) or k < 0:
        raise ValueError('Require a nonnegative cycle count')
    if k==0:
        return 14
    return next((j for end,j in THRESHOLDS if k <= end), 0)


def parameters(w):
    if not OLD.eligible(w):
        raise ValueError('Require w3445mod3456 and (16w-13)/27 divisible by3')
    data = OLD.OLD.parameters(w, 4)
    q, v = data['rank'], data['nine_index']
    b = 512*v+113
    h = RANK.INVERSE.valuation3(b+25)
    k, remainder = divmod(h, 7)
    p = 2**(11*k)*(b+25)//3**(7*k)-25
    j = RANK.INVERSE.valuation3(p+1)
    eta = 2**j*(p+1)//3**j-1
    assert p > 0 and eta > 0 and NORMAL.canonical(p) and NORMAL.canonical(eta)
    binary_order=3 if k else 1
    assert NORMAL.valuation2(p+1) == binary_order
    assert NORMAL.valuation2(eta+1) == binary_order+j and eta % 3 != 2
    if k:
        assert j == 0 if remainder == 0 else j >= 1
    else:
        assert j>=1
    if remainder>=2:assert j==1
    descending = j >= point_threshold(k)
    assert (eta < q) == descending and eta != q
    word = [1]*j+list(WORD)*k+list(TAIL)
    return dict(seed=w, rank=q, v=v, base=b, ternary_depth=h,
                cycles=k, remainder=remainder, point_depth=j,
                cycle_endpoint=p, endpoint=eta, word=word,
                ordinary_length=len(word), descending=descending)


def bridge(w):
    data = parameters(w)
    x, path, current = data['endpoint'], [data['endpoint']], Counter()
    for a in data['word']:
        assert NORMAL.valuation2(3*x+1) == a
        current[x] -= 1
        x = NORMAL.step(x)
        path.append(x)
    assert x == data['rank']
    current = combine((1,current))
    assert divergence(current) == atoms((1,x),(-1,data['endpoint']))
    return dict(parameters=data, path=path, current=current)


def pair_plan(w):
    inv = bridge(w)
    data = inv['parameters']
    q, eta, z = data['rank'], data['endpoint'], NORMAL.normal_form(w)
    high, low = RANK.absorption_plan(eta), RANK.absorption_plan(z)
    current = combine((1,NORMAL.bridge(3*w)['current']), (1,inv['current']),
                      (-1,NORMAL.bridge(w)['current']),
                      (1,high['current']), (-1,low['current']))
    coefficients = Counter(high['coefficients'])
    coefficients.subtract(low['coefficients'])
    coefficients = NINE.clean(coefficients)
    expected = T.pair_source(w)
    for u,c in coefficients.items():
        expected = combine((1,expected),(-c,T.pair_source(u)))
    assert divergence(current) == expected
    if data['descending']:
        status, leading = 'descending', None
    elif not data['cycles'] and data['point_depth']==1 and eta%3==0:
        status, leading = 'original_request', w
        assert coefficients[w] == 1
        assert all(rho(u)<q for u in coefficients if u != w)
        old = OLD.OLD.pair_plan(w,4)
        assert current == old['current'] and coefficients == old['coefficients']
    else:
        status, leading = 'higher_request', T.critical_inverse(eta)
        assert leading % 8 == 5 and coefficients[leading] == 1 and rho(leading) == eta > q
        assert all(rho(u)<eta for u in coefficients if u != leading)
    result = dict(seed=w, rank=q, parameters=data, current=current,
                  coefficients=coefficients, status=status, leading=leading)
    if data['descending']:
        RANK.validate_step(w,result)
    return result


def one_step(w):
    if not OLD.eligible(w) or not parameters(w)['descending']:
        return None
    return pair_plan(w)


def compile_plan(plan, supplied):
    if plan['status'] != 'descending':
        raise ValueError('The complete plan retains a nondecreasing request')
    RANK.validate_step(plan['seed'],plan)
    return RANK.compile_plan(plan,supplied)


def _crt(a, modulus_a, b, modulus_b):
    residue = a+modulus_a*((b-a)*pow(modulus_a,-1,modulus_b) % modulus_b)
    return residue, modulus_a*modulus_b


def parameter_family(k,j,remainder=0,unit=1,index=0):
    """Every feasible maximal-cycle/remainder/point row of the new rule."""
    if (not all(isinstance(x,int) for x in (k,j,remainder,unit,index))
            or k<0 or j<0 or not 0<=remainder<=6 or unit not in (1,2) or index<0
            or (k==0 and (j<1 or not remainder or (remainder>=2 and j!=1)))
            or (k and ((remainder==0 and j!=0) or (remainder==1 and j<1)
                       or (remainder>=2 and j!=1)))):
        raise ValueError('Incompatible exact lifted-cycle phase')
    binary = 2**19
    binary_u = (256*2041+69)*pow(3**(7*k),-1,binary)%binary
    if k==0:
        # Z=256v+57, b+1=2Z, while b+25=2(Z+12).
        if j>=2:
            if remainder!=1:raise ValueError('For k0,j>=2 the cycle depth is1')
            ternary=3**(j+1)
            ternary_u=(3**j*unit+12)%ternary
        elif remainder==1:
            ternary,ternary_u=9,6
        else:
            ternary=3**(remainder+1)
            ternary_u=3**remainder*unit
    elif remainder>=2:
        ternary=3**(remainder+1)
        ternary_u=3**remainder*unit
    elif remainder==0:
        ternary,ternary_u=3,unit
    else:
        ternary=3**(j+1)
        terminal=2 if j==1 else 1+3**(j-1)*unit
        ternary_u=3*(terminal*pow(2**(11*k-2),-1,3**j)%3**j)
    U0,period=_crt(binary_u,binary,ternary_u,ternary)
    U=U0+period*index
    v=(3**(7*k)*U-69)//256
    w=(27*v+13)//16
    actual=parameters(w)
    assert (actual['cycles'],actual['point_depth'],actual['remainder'])==(k,j,remainder)
    return dict(seed=w,U=U,U_residue=U0,U_period=period,index=index,
                parameters=actual)


def eleven_from_s(r,A,K,s):
    if (not all(isinstance(x,int) for x in (r,A,K,s))
            or r<16 or A<5 or K<0 or s<=0 or not s%2):
        raise ValueError('Require r>=16,A>=5,K>=0 and a positive odd s')
    M = 7*r+10
    numerator = 3**M*s-5
    if numerator % 2**A:
        raise ValueError('The required binary phase fails')
    t = numerator//2**A
    B = 2**(3*K+6)
    if s%3 != pow(2,r,3) or (t+9*pow(3**A,-1,B)) % B:
        raise ValueError('The complete R61 CRT phase fails')
    data = ELEVEN.eleven(r,s)
    f = data['endpoint']
    assert f == 2**A*t-1 and NORMAL.canonical(f)
    v = f//3
    assert rho(v) == f and ELEVEN.RUN.parameters(f)[:3] == (A,t,2)
    return dict(data,A=A,K=K,M=M,t=t,s=s,leading=v,
                first_extended_endpoint=(3**A*t-1)//2)


def _eleven_binary(r,A,K):
    if not all(isinstance(x,int) for x in (r,A,K)) or r<16 or A<5 or K<0:
        raise ValueError('Require r>=16,A>=5,K>=0')
    M, B = 7*r+10, 2**(3*K+6)
    t2 = -9*pow(3**A,-1,B) % B
    binary = 2**A*B
    sb = (5+2**A*t2)*pow(3**M,-1,binary) % binary
    return sb,binary


def old_cycle_family(r,A,K,k,j,remainder=0,unit=1,index=0):
    """Every feasible R60 parameter row inside each complete R61 CRT class."""
    sb,binary = _eleven_binary(r,A,K)
    if (not all(isinstance(x,int) for x in (k,j,remainder,unit,index))
            or k<0 or j<0 or not 0<=remainder<=6 or unit not in (1,2) or index<0
            or (k==0 and (j or not remainder)) or (remainder and j)):
        raise ValueError('Incompatible exact cycle/point phase')
    E = 11*r+18
    if k==0 or remainder:
        depth = 7*k+remainder
        ternary = 3**(depth+1)
        st = (19+3**depth*unit)*pow(2**E,-1,ternary)%ternary
    else:
        modulus_u = 3**(j+1)
        terminal = 2 if j==0 else 1+3**j*unit
        ur = terminal*pow(2**(11*k-3),-1,modulus_u)%modulus_u
        ternary = 3**(7*k+j+1)
        st = (19+3**(7*k)*ur)*pow(2**E,-1,ternary)%ternary
    s0,period = _crt(sb,binary,st,ternary)
    s = s0+period*index
    data = eleven_from_s(r,A,K,s)
    actual = OLD.parameters(data['seed'])
    assert (actual['cycles'],actual['point_depth'],actual['remainder']) == (k,j,remainder)
    return dict(data,s_residue=s0,s_period=period,cycle_parameters=actual)


def lifted_family(r,A,K,index=0,unit=1,cycles=0):
    """New18/24-arrow rows outside refined15 for every R61(r,A,K)."""
    sb,binary = _eleven_binary(r,A,K)
    if not isinstance(index,int) or index<0 or unit not in (1,2) or cycles not in (0,1):
        raise ValueError('Require nonnegative index,unit1/2,cycles0/1')
    if cycles==0:
        ternary=3**15
        st=(1735+3**14*unit)*pow(2**(11*r+24),-1,ternary)%ternary
        expected=(1,0,14)
    else:
        # h=8 => U=(256v+69)/3^8 is a unit.  j=13 iff
        # 2^9 U=1+3^12*unit modulo3^13.
        ternary = 3**21
        U = (1+3**12*unit)*pow(2**9,-1,3**13) % 3**13
        st = (1723+3**8*U)*pow(2**(11*r+24),-1,ternary)%ternary
        expected=(8,1,13)
    s0,period = _crt(sb,binary,st,ternary)
    s = s0+period*index
    data = eleven_from_s(r,A,K,s)
    new,old = parameters(data['seed']),OLD.parameters(data['seed'])
    assert (new['ternary_depth'],new['cycles'],new['point_depth']) == expected
    assert new['ordinary_length'] == (18 if cycles==0 else 24) and new['descending']
    assert old['ternary_depth'] == 1 and not old['descending']
    return dict(data,s_residue=s0,s_period=period,new_parameters=new,old_parameters=old)


def leading_inverse(data):
    """Complete prescribed inverse cycle: a strict leading descent back to q."""
    r,w,q,f,v = (data[x] for x in ('repeats','seed','rank','endpoint','leading'))
    cycle = ['ray0','point','point','point','ray0','ray0','point']
    word = ['ray1','point']+cycle*r+cycle[:4]
    x,states,current = f,[f],{}
    for kind in word:
        p,_,_ = RANK.INVERSE.inverse_step(x,kind)
        local = NORMAL.quotient_bridge(p)
        assert local['minimum'] == x
        current = combine((1,current),(-1,local['current']))
        x=p;states.append(x)
    assert x == q and len(word)==7*r+6
    assert current == combine((-1,data['current']))
    z = NORMAL.normal_form(v)
    high,low = RANK.absorption_plan(q),RANK.absorption_plan(z)
    J = combine((1,current),(-1,NORMAL.bridge(v)['current']),
                (1,high['current']),(-1,low['current']))
    c=Counter(high['coefficients']);c.subtract(low['coefficients']);c=NINE.clean(c)
    plan=dict(seed=v,rank=f,current=J,coefficients=c,status='descending')
    RANK.validate_step(v,plan)
    assert c[w]==1
    original=ELEVEN.EXIT.exit_plan(w)
    out=Counter(original['coefficients']);assert out.pop(v)==1;out.update(c)
    assert combine((1,original['current']),(1,J))=={} and NINE.clean(out)=={w:1}
    # The other natural stopping phase is precisely R56's existing node.
    p=f
    for kind in ['ray1','point']+cycle*(r+1):
        p=RANK.INVERSE.inverse_step(p,kind)[0]
    v0=OLD.parameters(w)['v']
    assert p==3*v0==(32*q-23)//27
    return dict(plan,original_seed=w,inverse_word=word,inverse_states=states,
                quotient_length=len(word),ordinary_common_tail_clocks=[1,7*r+7],
                alternate_endpoint=p,composed_current={},composed_coefficients={w:1})


def classify_fifteen(data,check_dispatcher=False):
    """Check the complete signed frontier, not just predicate membership."""
    w,q,v,f=(data[x] for x in ('seed','rank','leading','endpoint'))
    assert FIFTEEN.OLD.one_step(w) is None and FIFTEEN.OLD.one_step(v) is None
    assert FIFTEEN.EXACT.one_step(w) is None and FIFTEEN.EXACT.one_step(v) is None
    assert list(FIFTEEN.DEFERRED.candidates(v)) == [] and not OLD.eligible(v)
    summaries=[]
    for name,plan in FIFTEEN.DEFERRED.candidates(w):
        if name=='R57_exit':
            # Other high requests can exist when f/q is large.  They all have
            # rank below f, so strict-rho expansion can never cancel this +1.
            assert plan['coefficients'][v]==1
            assert all(rho(u)<f for u in plan['coefficients'] if u!=v)
            summaries.append(dict(recipe=name,leading=v,history=[],
                                  current=plan['current'],coefficients=plan['coefficients']))
            continue
        result=FIFTEEN.DEFERRED.defer(plan,max_nodes=8)
        assert result['status']=='unresolved'
        if name=='R55_first':
            q1=(2187*q+2363)//2048
            w1=(2*q1+1)//3
            assert len(result['history'])==1 and result['history'][0]['seed']==w1
            assert result['history'][0]['rule']=='R56_selected_inverse'
            leading=w
        elif name.startswith('R56_ray'):
            assert not result['history'];leading=w
        else:
            raise AssertionError('Unexpected deferred candidate')
        assert result['remaining_high']==[leading] and result['coefficients'][leading]==1
        assert all(rho(u)<q for u in result['coefficients'] if u!=leading)
        summaries.append(dict(recipe=name,leading=leading,history=result['history'],
                              current=result['current'],coefficients=result['coefficients']))
    assert [x['recipe'] for x in summaries]==['R55_first','R56_ray4','R56_ray8','R57_exit']
    old=OLD.parameters(w)
    if check_dispatcher:
        answer=FIFTEEN.one_step(w)
        assert (answer is not None)==old['descending']
        if answer:assert answer['rule']=='R60_cycle_inverse'
        assert FIFTEEN.one_step(v) is None
    return dict(seed=w,leading=v,leading_rank=f,rank=q,
                accepted=old['descending'],old_cycle_parameters=old,
                deferred=summaries)
