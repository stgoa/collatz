"""Shrinking signed bridges for the pair (3*w, w).

The arithmetic recognizer terminates, returning accepted or unresolved.
It proves no universal coverage or Collatz termination statement.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('paired_run_bridge', HERE.parent/'complementary_bridge/run_bridge.py')
RUN = module_from_spec(spec)
spec.loader.exec_module(RUN)
NORMAL = RUN.NORMAL
step, combine, divergence = RUN.step, RUN.combine, RUN.divergence


def prefix(seed, length):
    if length < 0:
        raise ValueError('Expected a nonnegative prescribed prefix length')
    path = [seed]
    for _ in range(length):
        path.append(step(path[-1]))
    return path, RUN.H.path_current(path)


def pair_plan(w):
    """Recognize a complete shrinking family; no forward search is used."""
    if not isinstance(w, int) or w <= 0 or w % 8 != 3:
        raise ValueError('Require positive w=3 modulo8')
    origin, layers = w, []
    while True:
        h = NORMAL.valuation2(3*w-1)
        if h % 2:
            return dict(origin=origin, accepted=False, layers=layers,
                        unresolved=w, reason='odd h', h=h)
        k = h//2-1
        assert k >= 1
        z = 3**k*((3*w-1)//2**h)
        layer = dict(w=w, h=h, k=k, z=z)
        if NORMAL.canonical(z):
            layer['kind'] = 'terminal'
            layers.append(layer)
            return dict(origin=origin, accepted=True, layers=layers)
        if z % 128 != 101:
            return dict(origin=origin, accepted=False, layers=layers,
                        unresolved=w, reason='unhandled z class', h=h, z=z)
        child = (3*z+1)//16
        assert child % 8 == 3 and 0 < child < w//4
        layer.update(kind='recursive', child=child)
        layers.append(layer)
        w = child


def pair_current(w):
    """Exact signed current with divergence delta_(3w)-delta_w, if accepted."""
    plan = pair_plan(w)
    if not plan['accepted']:
        raise ValueError('This arithmetic family leaves the pair unresolved')
    current = {}
    for layer in reversed(plan['layers']):
        v, k, z = layer['w'], layer['k'], layer['z']
        if layer['kind'] == 'terminal':
            left, left_rows = prefix(3*v, k)
            right, right_rows = prefix(v, k+1)
            assert left[-1] == 4*z+1 and right[-1] == 2*z+1
            left_rows = combine((1,left_rows), (1,{4*z+1:1}), (-1,{z:1}))
            normal = NORMAL.bridge(2*z+1)
            assert normal['minimum'] == z
            right_rows = combine((1,right_rows), (1,normal['current']))
            current = combine((1,left_rows), (-1,right_rows))
        else:
            child = layer['child']
            left, left_rows = prefix(3*v, k+1)
            right, right_rows = prefix(v, k+4)
            assert left[-1] == child and right[-1] == step(3*child)
            right_rows = combine((1,right_rows), (-1,{3*child:1}))
            local = combine((1,left_rows), (-1,right_rows))
            expected = combine((1,{3*v:1}), (-1,{v:1}),
                               (1,{3*child:1}), (-1,{child:1}))
            assert divergence(local) == expected
            current = combine((1,local), (-1,current))
        assert divergence(current) == combine((1,{3*v:1}), (-1,{v:1}))
    return dict(plan=plan, current=current)


def merge_clock(plan):
    """Prescribed l with S^l(3w)=S^(l+1)(w), for an accepted pair."""
    if not plan['accepted']:
        raise ValueError('The pair remains unresolved')
    terminal=plan['layers'][-1]
    length=terminal['k']+NORMAL.valuation2(2*terminal['z']+2)
    for layer in reversed(plan['layers'][:-1]):
        length+=layer['k']+2
    return length


def terminal_cylinder(k):
    """All w in this binary class have h=2k+2 and z=1 modulo8."""
    if not isinstance(k,int) or k < 1:
        raise ValueError('Require k>=1')
    h = 2*k+2
    modulus = 2**(h+3)
    residue = ((3**k+2**h)*pow(3**(k+1),-1,modulus)) % modulus
    return residue, modulus


def recursive_cylinder(depth):
    """Exactly depth copies of k=1, followed by terminal w=59 modulo128."""
    if not isinstance(depth,int) or depth < 0:
        raise ValueError('Require a nonnegative depth')
    bits = 8*depth+7
    modulus = 2**bits
    residue = ((7+256**depth*(229*59-7)*pow(27**depth,-1,modulus))
               * pow(229,-1,modulus)) % modulus
    assert residue % 8 == 3
    return residue, modulus


def mersenne_exponent_cylinder(w_residue, w_modulus):
    """Lift w=(3^(a-1)-1)/8 into a=7 mod16 by exact binary arithmetic."""
    if w_modulus < 8 or w_modulus & (w_modulus-1) or w_residue % 8 != 3:
        raise ValueError('Require a power-of-two modulus and w=3 modulo8')
    bits = w_modulus.bit_length()-1
    target = 1+8*w_residue
    exponent = 6
    # 3^(2^j)=1+2^(j+2) modulo2^(j+3), for j>=1.
    for j in range(4,bits+1):
        modulus = 2**(j+3)
        if pow(3,exponent,modulus) != target % modulus:
            exponent += 2**j
        assert pow(3,exponent,modulus) == target % modulus
    return exponent+1, 2**(bits+1)


def recursive_mersenne_cylinder(depth):
    return mersenne_exponent_cylinder(*recursive_cylinder(depth))


def synthetic_pair(depth, offset=0):
    """A small integer witness for any prescribed recursion depth."""
    if depth < 0 or offset < 0:
        raise ValueError('Require nonnegative depth and offset')
    odd = 27**depth
    residue = (7*pow(229,-1,odd)) % odd if odd != 1 else 0
    index = ((residue-59)*pow(128,-1,odd)) % odd if odd != 1 else 0
    v = 59+128*(index+offset*odd)
    w = v
    for _ in range(depth):
        assert (256*w-7) % 27 == 0
        w = (256*w-7)//27
    return w


def mersenne_bridge(a):
    """Bridge the actual R26 obstruction root to its smaller half-seed."""
    if not isinstance(a,int) or a < 7 or a % 16 != 7:
        raise ValueError('Require a>=7 and a=7 modulo16')
    x, q, N = 2**a-1, 2**(a-1)-1, 12*2**(a-4)
    w = (3**(a-1)-1)//8
    paired = pair_current(w)
    original = RUN.normalized_bridge(x)
    assert original['target'] == (3**a-3)//8 == 3*w > x
    assert original['target'] % 8 == 1 and q < N < x < 3*N//2
    lower_path, lower_rows = prefix(q,a-1)
    assert lower_path[-1] == w
    current = combine((1,original['current']), (1,paired['current']), (-1,lower_rows))
    assert divergence(current) == {q:-1,x:1}
    return dict(a=a,root=x,lower_seed=q,N=N,w=w,old_return=3*w,
                pair_plan=paired['plan'],current=current)


def from_supplied_lower(a, lower_current, weight=1):
    """Convert one supplied lower-seed certificate, with full multiplicity."""
    if not isinstance(weight,int) or weight < 1:
        raise ValueError('Require a positive integer weight')
    data = mersenne_bridge(a)
    assert divergence(lower_current) == {data['lower_seed']:1}
    signed = combine((weight,data['current']), (weight,lower_current))
    assert divergence(signed) == {data['root']:weight}
    edges = {x:step(x) for x in signed}
    actual = RUN.H.COMPLEMENT.extract_exact({data['root']:weight},edges)
    assert divergence(actual) == {data['root']:weight}
    assert all(c > 0 for c in actual.values())
    return dict(data=data,signed_current=signed,current=actual)
