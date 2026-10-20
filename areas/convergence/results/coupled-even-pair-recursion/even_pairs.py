"""Exact d=4 half-seed bridges, including a coupled-pair recursion.

The recognizers are partial. All construction uses prescribed finite prefixes;
the only absorption input in a conversion is the explicitly supplied half seed.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('even_pair_one', HERE.parent/'pair_one/pair_one.py')
ONE = module_from_spec(spec)
spec.loader.exec_module(ONE)
MIXED, RUN, NORMAL = ONE.MIXED, ONE.RUN, ONE.NORMAL
step, combine, divergence, prefix = ONE.step, ONE.combine, ONE.divergence, ONE.prefix


def joint_plan(v):
    """Recognize C(v)=delta_(18v+3)-delta_v, with v=3 modulo4."""
    if not isinstance(v, int) or v <= 0 or v % 4 != 3:
        raise ValueError('Require positive v=3 modulo4')
    origin, layers = v, []
    while True:
        if v % 8192 == 39:
            return dict(origin=origin, accepted=True, layers=layers,
                        terminal=v, clock=len(layers)+5)
        if v % 32 != 19:
            return dict(origin=origin, accepted=False, layers=layers, unresolved=v)
        child = (3*v-1)//8
        assert 0 < child < v and child % 4 == 3
        layers.append(dict(parent=v, child=child))
        v = child


def joint_current(v):
    plan = joint_plan(v)
    if not plan['accepted']:
        raise ValueError('The coupled pair is unresolved')
    end = plan['terminal']
    left, L = prefix(18*end+3, 5)
    right, R = prefix(end, 7)
    assert left[-1] == right[-1]
    result = combine((1, L), (-1, R))
    for row in reversed(plan['layers']):
        parent, child = row['parent'], row['child']
        large = 18*child+3
        partner = 2*large+1
        fchild = NORMAL.F(child)
        assert step(18*parent+3) == partner and step(parent) == fchild
        assert NORMAL.canonical(large)
        elementary = NORMAL.bridge(partner)
        assert elementary['minimum'] == large
        local = combine((1, {18*parent+3: 1}), (1, elementary['current']),
                        (-1, {parent: 1}), (-1, {fchild: 1}), (1, {child: 1}))
        assert divergence(local) == combine((1, {18*parent+3: 1, child: 1}),
                                            (-1, {parent: 1, large: 1}))
        result = combine((1, local), (1, result))
    assert divergence(result) == {18*v+3: 1, v: -1}
    return dict(plan=plan, current=result, clock=plan['clock'])


def joint_cylinder(depth):
    """Exactly depth coupled rewrites followed by the full terminal cylinder."""
    if not isinstance(depth, int) or depth < 0:
        raise ValueError('Require a nonnegative integer depth')
    residue, modulus = 39, 8192
    for _ in range(depth):
        modulus *= 8
        residue = (8*residue+1)*pow(3, -1, modulus) % modulus
    return residue, modulus


def pair_plan(w):
    """Recognize delta_(18w+1)-delta_w on the two d=4 entry domains."""
    if not isinstance(w, int) or w <= 0 or w % 2 != 1:
        raise ValueError('Require a positive odd w')
    if w % 256 == 105:
        child = (9*w-1)//16
        plan = MIXED.plan(child)
        return dict(kind='B', w=w, child=child, accepted=plan['accepted'], plan=plan)
    if w % 128 == 17:
        child = 3*(w-1)//16
        plan = joint_plan(child)
        return dict(kind='A', w=w, child=child, accepted=plan['accepted'], plan=plan)
    return dict(kind='unresolved', w=w, accepted=False)


def pair_current(w):
    plan = pair_plan(w)
    if not plan['accepted']:
        raise ValueError('The even pair is unresolved')
    f, child = 18*w+1, plan['child']
    if plan['kind'] == 'B':
        first, second = ONE.current(w), MIXED.current(3*w)
        assert second['plan']['layers'][0]['kind'] == 'terminal'
        assert MIXED.merge_clock(second['plan']) == 3
        elementary = NORMAL.bridge(f)
        assert elementary['minimum'] == 9*w
        current = combine((1, elementary['current']),
                          (1, first['current']), (1, second['current']))
        clock = MIXED.merge_clock(first['child_plan'])
    else:
        joint = joint_current(child)
        large = 18*child+3
        assert step(f) == NORMAL.F(2*large+1)
        assert step(w) == NORMAL.F(child)
        elementary = NORMAL.bridge(step(f))
        assert elementary['minimum'] == large
        left = combine((1, {f: 1}), (1, elementary['current']))
        right = combine((1, {w: 1, NORMAL.F(child): 1}), (-1, {child: 1}))
        assert divergence(left) == {f: 1, large: -1}
        assert divergence(right) == {w: 1, child: -1}
        current = combine((1, left), (1, joint['current']), (-1, right))
        clock = joint['clock']
    assert divergence(current) == {f: 1, w: -1}
    # S^(clock+1)(f)=S^(clock+3)(w).
    return dict(plan=plan, current=current, clock=clock)


def bridge(x):
    raw = RUN.bridge(x)
    if raw['d'] != 4:
        raise ValueError('This constructor covers only d=4')
    a, w = raw['a'], raw['w']
    pair = pair_current(w)
    lower = (x-1)//2
    path, rows = prefix(lower, a-1)
    assert path[-1] == w
    current = combine((1, raw['current']), (1, pair['current']), (-1, rows))
    assert divergence(current) == {x: 1, lower: -1}
    assert NORMAL.normal_form(raw['target']) == 9*w
    return dict(root=x, lower=lower, a=a, w=w, kind=pair['plan']['kind'],
                child=pair['plan']['child'], current=current,
                clock=a+pair['clock']+2, old_normalized_return=9*w)


def parent_cylinder(kind, word=(), terminal_k=1, depth=1):
    if kind == 'B':
        return ONE.cylinder('B', word, terminal_k)
    if kind == 'A':
        if depth < 1:
            raise ValueError('The A entry needs at least one coupled rewrite')
        r, m = joint_cylinder(depth)
        return (16*r+3)*pow(3, -1, 16*m) % (16*m), 16*m
    raise ValueError('Require kind A or B')


def cylinder(a, kind, word=(), terminal_k=1, depth=1):
    if not isinstance(a, int) or a < 2:
        raise ValueError('Require a>=2')
    r, m = parent_cylinder(kind, word, terminal_k, depth)
    t = (16*r+1)*pow(3**(a-1), -1, 16*m) % (16*m)
    return 2**a*t-1, 2**a*16*m


def actual_source(a, kind, weight=1, word=(), terminal_k=1, depth=1):
    """One full-weight source on the required ray N=12*2^b."""
    if weight not in (1, 2):
        raise ValueError('Require residual weight1 or2')
    r, m = cylinder(a, kind, word, terminal_k, depth)
    bits = m.bit_length()-1
    N = 12*2**(bits+4)
    odd, source_residue = (3, 3) if weight == 1 else (9, 7)
    index = (source_residue-r)*pow(m, -1, odd) % odd
    first, period = r+m*index, m*odd
    low, high = (9*N//8, 3*N//2) if weight == 1 else (N, 9*N//8)
    x = first+period*((low-first)//period+1)
    assert low < x < high
    assert RUN.H.TRANSFER.residual_coefficient(N, x) == weight
    data = bridge(x)
    assert data['lower'] < N < x
    return dict(N=N, root=x, weight=weight, data=data)


def from_supplied_lower(x, lower_current, weight=1):
    if not isinstance(weight, int) or weight < 1:
        raise ValueError('Require a positive integer weight')
    data = bridge(x)
    if divergence(lower_current) != {data['lower']: 1}:
        raise ValueError('Supply an exact current for the smaller half seed')
    signed = combine((weight, data['current']), (weight, lower_current))
    assert divergence(signed) == {x: weight}
    current = RUN.H.COMPLEMENT.extract_exact({x: weight}, {u: step(u) for u in signed})
    assert divergence(current) == {x: weight}
    return dict(data=data, signed_current=signed, current=current)


def weighted_count(N, a, kind, word=(), terminal_k=1, depth=1):
    """Exact four-row R_N mass in one complete fixed cylinder."""
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError('Require N>=8 and 8|N')
    r, m = cylinder(a, kind, word, terminal_k, depth)
    rows = ((1, N, 3*N//2, 3, 3),
            (1, 9*N//8, 3*N//2, 7, 3),
            (2, N, 9*N//8, 7, 9),
            (2, N, 9*N//8, 19, 9))
    answer = 0
    for weight, low, high, source_residue, odd in rows:
        index = (source_residue-r)*pow(m, -1, odd) % odd
        first, period = r+m*index, m*odd
        count = max(0, (high-1-first)//period-(low-first)//period)
        answer += weight*count
    return answer
