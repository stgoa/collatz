"""Exact original-rank comparisons using a retained smaller lower history.

These are conditional signed currents. Unknown terminal inputs are preserved;
no dispatcher is changed and no search for universal absorption is performed.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _load(name, relative):
    spec = spec_from_file_location(name, HERE.parent/relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

REPAIR = _load('retained_repair', 'w9_history_repair/w9_history_repair.py')
RUN = _load('retained_run', 'complementary_bridge/run_bridge.py')
B, N, OLD = REPAIR.B, REPAIR.N, REPAIR.B.SIGMA.RETURN
combine, atoms, divergence = B.combine, B.atoms, B.divergence
prefix = REPAIR.M.prefix


def integer(x, lower=0):
    if type(x) is not int or x < lower:
        raise ValueError('Require an integer at least '+str(lower))


def high(coefficients, threshold):
    return {u:c for u,c in coefficients.items() if B.rho(u) >= threshold}


def finish(seed, threshold, current, coefficients, **details):
    data = dict(seed=seed, rank=B.rho(seed), threshold=threshold,
                current=current, coefficients=coefficients, **details)
    B.check_boundary(data)
    data['high'] = high(coefficients, threshold)
    data['status'] = 'unresolved' if data['high'] else 'descending'
    return data


def history_nine(w, threshold, max_nodes=3):
    """Complete enlarged W9 window, with all lower-history inputs strict.

    Require Q<=3w and3w+1<4Q. The chosen upper prefix replaces the local
    subtraction of the later lower endpoint. At most three W9 nodes are used.
    """
    integer(w, 1); integer(threshold, 11547); integer(max_nodes, 1)
    if w % 16 != 9 or threshold % 2 != 1:
        raise ValueError('Require W9 and an odd original threshold')
    if threshold > 3*w or 3*w+1 >= 4*threshold:
        raise ValueError('Require Q<=3w and3w+1<4Q')
    local = B.nine_candidate(w)
    upper = prefix(3*w, local['prefix_length'])
    endpoint = upper['endpoint']
    hx, hw = B.absorption_plan(endpoint), B.absorption_plan(w)
    assert all(B.rho(u) < threshold for u in hw['coefficients'])
    current = combine((1, upper['current']), (1, hx['current']), (-1, hw['current']))
    coefficients = combine((1, hx['coefficients']), (-1, hw['coefficients']))
    first_high = high(coefficients, threshold)
    assert not first_high or (len(first_high) == 1 and next(iter(first_high.values())) == 1)
    child = next(iter(first_high), None)
    nodes = [dict(seed=w, d=local['d'], z=local['z'], endpoint=endpoint,
                  upper_prefix_length=local['prefix_length'])]
    if child is not None and child % 16 == 9:
        assert child == local['z'] and 16*child < 9*w and 4*child < 3*threshold
        if max_nodes == 1:
            raise ValueError('Node cap reached before the retained W9 child')
        rest = REPAIR.bounded_repair(child, threshold, max_nodes-1)
        current = combine((1, current), (1, rest['current']))
        coefficients = combine((1, coefficients), (-1, {child:1}), (1, rest['coefficients']))
        nodes += [dict(seed=r['seed'], d=r['d'], z=r['z']) for r in rest['nodes']]
    result = finish(w, threshold, current, coefficients, nodes=nodes,
                    first_high=first_high, upper_endpoint=endpoint,
                    upper_prefix_length=local['prefix_length'],
                    rule='retained_lower_history_nine')
    assert len(nodes) <= 3
    assert not result['high'] or (len(result['high']) == 1 and
           next(iter(result['high'].values())) == 1 and next(iter(result['high'])) % 8 == 5)
    return result


def remaining_cell(m):
    integer(m)
    v = 128646821+64*3**18*m
    q = 133704987+3*2**33*m
    E = 162818633+3**22*m
    d = 2+N.valuation2(E)
    assert v % 64 == 37 and v < q < 3*v
    assert 64*E == 81*v+11 and 32*E < 39*(q-1)
    return dict(m=m, k=85+16384*m, v=v, Q=q, E=E, d=d)


def depth_cell(d, index=0):
    """Every m with the exact first-run depth d; includes its extra bit."""
    integer(d, 2); integer(index)
    modulus = 2**(d-1)
    residue = ((2**(d-2)-162818633)*pow(3**22, -1, modulus)) % modulus
    m = residue+modulus*index
    assert remaining_cell(m)['d'] == d
    return dict(d=d, m=m, residue=residue, modulus=modulus)


def origin(m):
    """The full inherited R87+R44 plan, including its lower zero-source terms."""
    data = remaining_cell(m)
    original = REPAIR.repair_failed(data['k'])
    u = original['leading']
    child = OLD.forward_plan(u)
    assert child['parameters']['a'] == 4
    current = combine((1, original['current']), (1, child['current']))
    coefficients = combine((1, original['coefficients']), (-1, {u:1}),
                           (1, child['coefficients']))
    result = finish(original['seed'], data['Q'], current, coefficients,
                    parameters=data, rule='inherited_full_R87_R44')
    assert result['high'] == {data['v']:1}
    w, z = original['nodes'][0]['seed'], original['nodes'][0]['z']
    Y, r = 2*z+1, 6*data['v']+1
    hw, hy, hz, hb = (B.absorption_plan(s) for s in (w, Y, z, original['seed']))
    z5, r5 = (OLD.INVERSE.absorption_five_plan(s) for s in (z, r))
    D = combine((1, hw['current']), (-1, prefix(w,2)['current']), (-1, hy['current']))
    dc = combine((1, hw['coefficients']), (-1, hy['coefficients']))
    E = combine((1, hz['current']), (-1, z5['current']))
    ec = combine((1, hz['coefficients']), (-1, z5['coefficients']))
    expected = combine((1, prefix(data['Q'],18)['current']), (1,r5['current']),
                       (-1,hb['current']), (1,D), (1,E))
    expectedc = combine((1,r5['coefficients']),(-1,hb['coefficients']),(1,dc),(1,ec))
    assert current == expected and coefficients == expectedc
    assert all(B.rho(s)<data['Q'] for s in dc) and all(B.rho(s)<data['Q'] for s in ec)
    result['lower_relations'] = [dict(current=D, coefficients=dc), dict(current=E, coefficients=ec)]
    return result


def first_run(m, repair_nine=True):
    """Whole H4 family, exact original-Q decision for the complete formal plan."""
    data = remaining_cell(m)
    v,q,d,E = (data[k] for k in ('v','Q','d','E'))
    block = RUN.bridge(3*v)
    assert RUN.parameters(3*v)[0] == 4 and RUN.parameters(3*v)[2] == d
    f = block['target']
    b = d//2
    expected = (2*3**b*E//4**b if d%2 else 8*3**b*E//4**b+1)
    assert f == expected
    upper, lower = B.absorption_plan(f), B.absorption_plan(v)
    assert all(B.rho(u)<q for u in lower['coefficients'])
    current = combine((1,block['current']),(1,upper['current']),(-1,lower['current']))
    coefficients = combine((1,upper['coefficients']),(-1,lower['coefficients']))
    repaired = None
    initial_high = high(coefficients,q)
    if repair_nine and len(initial_high)==1:
        leader = next(iter(initial_high))
        if (initial_high[leader]==1 and leader%16==9 and 3*leader+1<4*q):
            repaired = history_nine(leader,q)
            current = combine((1,current),(1,repaired['current']))
            coefficients = combine((1,coefficients),(-1,{leader:1}),(1,repaired['coefficients']))
    result = finish(v,q,current,coefficients,parameters=data,endpoint=f,
                    comparison=block['current'],
                    ordinary_clocks=[len(block['left'])-1,len(block['right'])-1],
                    quotient_length=3+d//2, initial_high=initial_high,
                    repair=repaired, rule='complete_remaining_H4_comparison')
    if (d%2 and d>=9) or (not d%2 and d>=16):
        assert f<q and not result['high']
    if d==2:
        assert E%3==2
        assert all(B.rho(u)<q for u in B.absorption_plan(E)['coefficients'])
    return result


def coupled_parameters(index):
    integer(index)
    data = remaining_cell(2736+4096*index)
    C,beta = data['E'],(9*data['E']-1)//64
    s=(beta-5)//64
    assert C%128==121 and beta%64==5 and beta%9==8 and s%9==3
    X,Y,Z=18*beta+1,6*beta+1,(81*beta+7)//4
    assert prefix(data['Q'],25)['endpoint']==X
    assert prefix(data['Q'],27)['endpoint']==Z
    return dict(data,index=index,C=C,beta=beta,s=s,a=12*beta+1,b=4*beta+1,
                X=X,Y=Y,Z=Z)


def coupled_cancellation(index, inherited=False):
    """Eliminate the negative high pair by its complete retained history."""
    data=coupled_parameters(index)
    v,q,C,beta,a,b,X,Y=(data[k]for k in('v','Q','C','beta','a','b','X','Y'))
    hc,hv,hx,hy,hb=(B.absorption_plan(s) for s in(C,v,X,Y,b))
    local=B.nine_candidate(C)
    assert local['d']==6 and local['z']==3*beta
    V=prefix(C,3,(2,1,2))['current']
    U=prefix(3*C,3,(1,2,2))['current']
    p4=prefix(3*v,4,(1,1,1,2));f=p4['endpoint']
    assert f==6*C+1
    K=combine((1,p4['current']),(1,N.bridge(f)['current']))
    old=combine((1,K),(1,local['current']),(1,hc['current']),(-1,hv['current']))
    oldc=combine((1,local['coefficients']),(1,hc['coefficients']),(-1,hv['coefficients']))
    assert high(oldc,q)=={a:1,b:-1}
    negative=finish(b,q,combine((1,hc['current']),(-1,V),
                               (1,N.bridge(3*b)['current']),(-1,hb['current'])),
                    combine((1,hc['coefficients']),(-1,hb['coefficients'])),
                    rule='negative_high_pair_from_retained_history')
    assert negative['status']=='descending'
    current=combine((1,old),(-1,negative['current']))
    coefficients=combine((1,oldc),(1,{b:1}),(-1,negative['coefficients']))
    direct=combine((1,K),(1,U),(1,hx['current']),(-1,hv['current']))
    directc=combine((1,hx['coefficients']),(-1,hv['coefficients']))
    assert current==direct and coefficients==directc
    assert combine((1,K),(1,U))==prefix(3*v,7)['current']
    assert high(coefficients,q)=={a:1}
    result=finish(v,q,current,coefficients,parameters=data,negative_plan=negative,
                  old_current=old,old_coefficients=oldc,rule='coupled_history_cancellation')
    if inherited:
        original=origin(data['m'])
        full=combine((1,original['current']),(1,current))
        fullc=combine((1,original['coefficients']),(-1,{v:1}),(1,coefficients))
        hbase=B.absorption_plan(original['seed'])
        fresh=combine((1,prefix(q,25)['current']),(1,hx['current']),(-1,hbase['current']))
        freshc=combine((1,hx['coefficients']),(-1,hbase['coefficients']))
        v5=OLD.INVERSE.absorption_five_plan(v)
        F=combine((1,v5['current']),(-1,hv['current']))
        fc=combine((1,v5['coefficients']),(-1,hv['coefficients']))
        relations=original['lower_relations']+[dict(current=F,coefficients=fc)]
        assert full==combine((1,fresh),*[(1,r['current'])for r in relations])
        assert fullc==combine((1,freshc),*[(1,r['coefficients'])for r in relations])
        assert all(B.rho(u)<q for r in relations for u in r['coefficients'])
        result['inherited']=finish(original['seed'],q,full,fullc,lower_relations=relations,
                                  fresh_current=fresh,fresh_coefficients=freshc)
    return result


def raw_decision(raw,threshold):
    """The existing fourteen-template native decision on raw1mod3 below6Q."""
    if type(raw)is not int or raw<=0 or raw%6!=1 or raw-1>=6*(threshold-1):
        raise ValueError('Require positive raw1mod6 with raw-1<6(Q-1)')
    x,word,current=raw,'',{}
    while True:
        normal=N.bridge(x); n=normal['minimum']
        if n<threshold or B.T.critical(n):break
        assert word in REPAIR.M.TEMPLATES and n%8==1
        letter='A'if x%8==1 else'B'if x%16==3 else'C'
        step=REPAIR.M.transition(x,letter)
        current=combine((1,current),(1,step['current']))
        x=step['target'];word+=letter
    current=combine((1,current),(1,normal['current']))
    assert len(word)<=7 and divergence(current)==atoms((1,raw),(-1,n))
    return dict(raw=raw,word=word,endpoint=n,current=current,normalizer=normal)


def coupled_continuation(index):
    """Complete fixed-Q decision after the coupled cell's27-arrow prefix.

    A selected endpoint requires one W9 replacement. A canonical endpoint
    takes its full H3 block, the existing bounded native decision, and at
    most two W9 replacements. Any remaining positive W5 leader is explicit.
    """
    data=coupled_parameters(index)
    q,Z,beta,s=data['Q'],data['Z'],data['beta'],data['s']
    seed=q//3; low=B.absorption_plan(seed)
    comparison=prefix(q,27)['current'];extra={}
    if s%2:
        c=(27*beta+1)//8
        assert N.selected(Z) and N.normal_form(Z)==3*c and c%16==9
        assert 40*c>23*q and 12*c<7*q
        upper=B.absorption_plan(Z)
        current=combine((1,comparison),(1,upper['current']),(-1,low['current']))
        coefficients=combine((1,upper['coefficients']),(-1,low['coefficients']))
        assert high(coefficients,q)=={c:1}
        repair=REPAIR.local_decision(c,q)
        assert bool(repair['high'])==(repair['d'] in(4,6,8) and not N.canonical(3*repair['z']))
        assert repair['leader']is None or repair['leader']%8==5
        current=combine((1,current),(1,repair['current']))
        coefficients=combine((1,coefficients),(-1,{c:1}),(1,repair['coefficients']))
        extra=dict(branch='selected_Z',nine=repair)
    else:
        assert N.canonical(Z)
        a,t,d,u=RUN.parameters(Z);assert a==3
        assert d==2+N.valuation2(729*(s//2)+29)
        block=RUN.bridge(Z);g=block['target']
        assert g-1<6*(q-1)
        if g%3==1:
            native=raw_decision(g,q)
        else:
            assert d%2 and 2*g<3*q
            normal=N.bridge(g); n=normal['minimum']
            if n<q or B.T.critical(n):
                native=dict(raw=g,word='',endpoint=n,current=normal['current'],normalizer=normal)
            else:
                assert n==g and g%8==1
                after=N.step(g); tail=raw_decision(after,q)
                native=dict(tail,raw=g,word='free_A'+tail['word'],
                            current=combine((1,{g:1}),(1,tail['current'])))
        comparison=combine((1,comparison),(1,block['current']),(1,native['current']))
        upper=B.absorption_plan(native['endpoint'])
        current=combine((1,comparison),(1,upper['current']),(-1,low['current']))
        coefficients=combine((1,upper['coefficients']),(-1,low['coefficients']))
        before=high(coefficients,q)
        assert not before or(len(before)==1 and next(iter(before.values()))==1)
        repair=None
        if before:
            leader=next(iter(before))
            if leader%16==9:
                repair=REPAIR.bounded_repair(leader,q)
                current=combine((1,current),(1,repair['current']))
                coefficients=combine((1,coefficients),(-1,{leader:1}),(1,repair['coefficients']))
        extra=dict(branch='canonical_Z',d=d,raw_target=g,native=native,
                   block_ordinary_clocks=[len(block['left'])-1,len(block['right'])-1],
                   block_quotient_length=2+d//2,repair=repair)
    result=finish(seed,q,current,coefficients,parameters=data,**extra,
                  rule='complete_coupled_original_rank_continuation')
    assert not result['high']or(len(result['high'])==1 and
          next(iter(result['high'].values()))==1 and next(iter(result['high']))%8==5)
    return result


def extend_origin(m,child):
    original=origin(m)
    if child['seed']!=original['parameters']['v'] or child['threshold']!=original['threshold']:
        raise ValueError('Child does not match the original retained request and threshold')
    B.check_boundary(child)
    return finish(original['seed'],original['threshold'],
                  combine((1,original['current']),(1,child['current'])),
                  combine((1,original['coefficients']),(-1,{child['seed']:1}),
                          (1,child['coefficients'])),rule='full_inherited_substitution')


def compile_plan(data,supplied):
    B.check_boundary(data)
    integer(data.get('threshold'),11547)
    if data['threshold']%2!=1 or data['threshold']>B.rho(data['seed']):
        raise ValueError('Require an odd original threshold no larger than the source rank')
    if data.get('status')!='descending' or high(data['coefficients'],data['threshold']):
        raise ValueError('An original-rank high request is still unresolved')
    return B.compile_plan(data,supplied)
