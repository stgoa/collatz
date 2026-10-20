"""Two exact bridges from the missing 1-mod-8 pair domain to mixed pairs.

Recognition is partial. No forward absorption search occurs here.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('pair_one_mixed', HERE.parent/'paired_completion/mixed_pairs.py')
MIXED = module_from_spec(spec)
spec.loader.exec_module(MIXED)
OLD = MIXED.OLD
RUN, NORMAL = OLD.RUN, OLD.NORMAL
step, combine, divergence, prefix = OLD.step, OLD.combine, OLD.divergence, OLD.prefix


def reduction(w):
    if not isinstance(w, int) or w <= 0 or w % 8 != 1:
        raise ValueError('Require a positive integer w=1 modulo8')
    if w % 128 == 17:
        child = 3*(w-1)//16
        return dict(kind='A', w=w, child=child, clock_increment=1)
    if w % 256 == 105:
        child = (9*w-1)//16
        return dict(kind='B', w=w, child=child, clock_increment=2)
    return dict(kind='unresolved', w=w)


def local_current(w):
    data = reduction(w)
    if data['kind'] == 'unresolved':
        raise ValueError('The 1-mod-8 pair is outside the two branch domains')
    child = data['child']
    assert 0 < child < w and child % 8 == 3
    if data['kind'] == 'A':
        u = (w-1)//16
        left, lc = prefix(3*w, 1)
        right, rc = prefix(w, 1)
        h = 18*u+1
        assert left[-1] == NORMAL.F(h) and right[-1] == NORMAL.F(child)
        terminal = NORMAL.bridge(h)
        assert terminal['minimum'] == 3*child
        lc = combine((1,lc), (1,{left[-1]:1}), (-1,{h:1}),
                     (1,terminal['current']))
        rc = combine((1,rc), (1,{right[-1]:1}), (-1,{child:1}))
    else:
        assert child % 16 == 11 and NORMAL.canonical(child)
        left, lc = prefix(3*w, 2)
        right, rc = prefix(w, 2)
        assert left[-1] == 2*(3*child)+1 and right[-1] == 2*child+1
        lb, rb = NORMAL.bridge(left[-1]), NORMAL.bridge(right[-1])
        assert lb['minimum'] == 3*child and rb['minimum'] == child
        lc = combine((1,lc), (1,lb['current']))
        rc = combine((1,rc), (1,rb['current']))
    current = combine((1,lc), (-1,rc))
    expected = combine((1,{3*w:1}), (-1,{w:1}),
                       (-1,{3*child:1}), (1,{child:1}))
    assert divergence(current) == expected
    return dict(reduction=data, current=current)


def current(w):
    local = local_current(w)
    child = MIXED.current(local['reduction']['child'])
    result = combine((1,local['current']), (1,child['current']))
    assert divergence(result) == {3*w:1,w:-1}
    length = MIXED.merge_clock(child['plan'])+local['reduction']['clock_increment']
    return dict(reduction=local['reduction'], child_plan=child['plan'],
                current=result, clock=length)


def cylinder(kind, word=(), terminal_k=1):
    residue, modulus = MIXED.word_cylinder(word, terminal_k)
    if kind == 'A':
        target = (16*residue+3)*pow(3,-1,16*modulus)
    elif kind == 'B':
        if residue % 16 != 11:
            raise ValueError('Branch B requires a canonical child=11 modulo16')
        target = (16*residue+1)*pow(9,-1,16*modulus)
    else:
        raise ValueError('Unknown branch')
    return target % (16*modulus), 16*modulus


def exponent_cylinder(kind, word=(), terminal_k=1):
    residue, modulus = cylinder(kind,word,terminal_k)
    bits = modulus.bit_length()-1
    target, exponent = 1+8*residue, 2
    for j in range(4,bits+1):
        mod = 2**(j+3)
        if pow(3,exponent,mod) != target % mod:
            exponent += 2**j
        assert pow(3,exponent,mod) == target % mod
    return exponent+1, 2*modulus


def synthetic(kind, word=(), terminal_k=1, offset=0):
    r, m = MIXED.word_cylinder(word,terminal_k)
    odd, target = (3,0) if kind == 'A' else (9,5)
    if kind == 'B' and r % 16 != 11:
        raise ValueError('Branch B requires a canonical child')
    index = ((target-r)*pow(m,-1,odd)) % odd + offset*odd
    child = r+m*index
    if kind == 'A':
        return 1+16*child//3
    return (16*child+1)//9


def mersenne_bridge(a):
    if not isinstance(a,int) or a < 19 or a % 16 != 3:
        raise ValueError('Require a>=19 and a=3 modulo16')
    x,q,N = 2**a-1,2**(a-1)-1,12*2**(a-4)
    w = (3**(a-1)-1)//8
    pair = current(w)
    raw = RUN.bridge(x)
    assert raw['target'] == 3*w
    lower, rows = prefix(q,a-1)
    assert lower[-1] == w
    bridge = combine((1,raw['current']), (1,pair['current']), (-1,rows))
    assert divergence(bridge) == {x:1,q:-1}
    return dict(a=a,root=x,lower=q,N=N,w=w,clock=a+pair['clock'],
                old_normalized_return=NORMAL.normal_form(3*w),current=bridge)


def from_supplied_lower(a, lower_current, weight=1):
    if not isinstance(weight,int) or weight < 1:
        raise ValueError('Require a positive integer weight')
    data = mersenne_bridge(a)
    assert divergence(lower_current) == {data['lower']:1}
    signed = combine((weight,data['current']), (weight,lower_current))
    assert divergence(signed) == {data['root']:weight}
    actual = RUN.H.COMPLEMENT.extract_exact({data['root']:weight},
                                           {x:step(x) for x in signed})
    assert divergence(actual) == {data['root']:weight}
    return dict(data=data,current=actual)
