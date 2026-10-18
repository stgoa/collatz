"""Complete critical-nine elimination, conditional on exact critical-five inputs.

Every formal recursion decreases its unresolved 9-modulo16 index.  This does
not construct the requested 5-modulo8 currents or perform an orbit search.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('w9_tripling', HERE.parent / 'tripling_equivalence/tripling.py')
TRIPLING = module_from_spec(spec)
spec.loader.exec_module(TRIPLING)
NORMAL = TRIPLING.NORMAL
combine, atoms = TRIPLING.combine, TRIPLING.atoms
pair_source, divergence = TRIPLING.pair_source, TRIPLING.divergence


def clean(counter):
    return {x: c for x, c in sorted(counter.items()) if c}


def prefix(x, length):
    """Only the prescribed finite ordinary prefix; 1 is absorbing."""
    current = Counter()
    start = x
    for _ in range(length):
        if x != 1:
            current[x] += 1
        x = NORMAL.step(x)
    current = clean(current)
    assert divergence(current) == atoms((1, start), (-1, x))
    return x, current


def tripling_plan_bound(z):
    """Formal plans for 3z and z have every missing index <=(3z+1)/2."""
    NORMAL._odd(z)
    upper, lower = TRIPLING.plan(3*z), TRIPLING.plan(z)
    assert all(2*u <= 3*z+1 for u in upper['pairs'] + lower['pairs'])
    return upper, lower


def local_plan(w):
    """div(current)=P(w)-sum coefficient[u]*P(u), every u in critical W.

    Every 9-modulo16 child is strictly below w.  The only possible child >=w
    is a single positive 5-modulo8 input, identified by ``exception``.
    """
    if not isinstance(w, int) or w <= 0 or w % 16 != 9:
        raise ValueError('Require a positive w=9 modulo16')
    d = NORMAL.valuation2(9*w-1)
    assert d >= 4
    odd = bool(d % 2)
    k = (d-5)//2 if odd else (d-4)//2
    C = (9*w-1) >> d
    z = 3**k*C
    length = k+2
    left, left_current = prefix(3*w, length)
    right, right_current = prefix(w, length)
    current = combine((1, left_current), (-1, right_current))
    exceptional = None
    if odd:
        assert (left, right) == (NORMAL.F(3*z), NORMAL.F(z))
        # The sibling current [F(t)]-[t] has divergence delta_F(t)-delta_t.
        sibling = atoms((1, NORMAL.F(3*z)), (-1, 3*z),
                        (-1, NORMAL.F(z)), (1, z))
        current = combine((1, current), (1, sibling))
        upper, lower = tripling_plan_bound(z)
        assert 32*z <= 9*w-1
        assert all(2*u < w for u in upper['pairs'] + lower['pairs'])
        branch = 'odd_d'
    else:
        assert (left, right) == (6*z+1, 2*z+1)
        assert C % 9 == -pow(2**d, -1, 9) % 9
        assert C % 3 == 2 and z >= 5
        upper, lower = TRIPLING.plan(left), TRIPLING.plan(right)
        if NORMAL.canonical(3*z):
            assert all(2*u <= 3*z+1 for u in upper['pairs'] + lower['pairs'])
            assert all(u < w for u in upper['pairs'] + lower['pairs'])
            branch = 'even_d_canonical'
        else:
            u = 4*z+1
            assert upper['pairs'][0] == u
            assert upper['pairs'][1:] == TRIPLING.plan(z)['pairs']
            assert all(v < w and v < u for v in upper['pairs'][1:] + lower['pairs'])
            if NORMAL.canonical(z):
                assert upper['pairs'][1:] == lower['pairs']
            if k <= 2:
                assert u > w
                exceptional = u
                branch = 'low_even_d_expansion'
            else:
                assert (2**(2*k+4)-36*3**k)*C > 8
                assert u < w
                branch = 'high_even_d'
    current = combine((1, current), (1, upper['current']), (-1, lower['current']))
    coefficients = Counter(upper['pairs'])
    coefficients.subtract(lower['pairs'])
    coefficients = clean(coefficients)
    if exceptional is not None:
        assert coefficients[exceptional] == 1 and exceptional % 8 == 5
    assert all(TRIPLING.critical_domain(u) for u in coefficients)
    assert all(u < w or u == exceptional for u in coefficients)
    assert all(u < w for u in coefficients if u % 16 == 9)
    assert all(4*u <= 9*w+3 for u in coefficients)
    expected = pair_source(w)
    for u, c in coefficients.items():
        expected = combine((1, expected), (-c, pair_source(u)))
    assert divergence(current) == expected
    return dict(seed=w, d=d, k=k, C=C, z=z, branch=branch,
                prefix_length=length, endpoints=[left, right],
                positive_requests=upper['pairs'], negative_requests=lower['pairs'],
                coefficients=coefficients, exception=exceptional, current=current)


def five_plan(w, max_nodes=None):
    """Eliminate all critical-nine requests; return an exact finite formal plan.

    Only arithmetic normalization and prescribed finite prefixes are used.
    A resource cap, if provided, rejects the plan rather than supplying a leaf.
    The returned W5 inputs remain unproved premises.
    """
    if not TRIPLING.critical_domain(w):
        raise ValueError('Require a positive critical W index')
    memo, local = {}, {}

    def visit(x):
        if x % 8 == 5:
            return dict(current={}, coefficients={x: 1})
        if x in memo:
            return memo[x]
        if max_nodes is not None and len(local) >= max_nodes:
            raise RuntimeError('Formal-plan resource cap reached; no certificate claimed')
        data = local_plan(x)
        local[x] = data
        current = data['current']
        coefficients = Counter()
        for u, c in data['coefficients'].items():
            assert u % 8 == 5 or u < x
            child = visit(u)
            current = combine((1, current), (c, child['current']))
            for v, value in child['coefficients'].items():
                coefficients[v] += c*value
        answer = dict(current=current, coefficients=clean(coefficients))
        memo[x] = answer
        return answer

    answer = visit(w)
    assert all(u % 8 == 5 and 4*u <= 9*w+3 for u in answer['coefficients'])
    expected = pair_source(w)
    for u, c in answer['coefficients'].items():
        expected = combine((1, expected), (-c, pair_source(u)))
    assert divergence(answer['current']) == expected
    return dict(seed=w, current=answer['current'], coefficients=answer['coefficients'],
                nine_nodes=sorted(local), local_plans=local)


def compile_five_plan(data, supplied):
    """Substitute supplied exact integer P inputs; missing inputs are errors."""
    current = data['current']
    for u, c in data['coefficients'].items():
        if u not in supplied:
            raise ValueError('Missing exact critical-five current for '+str(u))
        rows = supplied[u]
        if any(not isinstance(x, int) or not isinstance(v, int)
               for x, v in rows.items()):
            raise ValueError('Critical-five currents must have integer rows')
        if divergence(rows) != pair_source(u):
            raise ValueError('Incorrect exact critical-five current for '+str(u))
        current = combine((1, current), (c, rows))
    assert divergence(current) == pair_source(data['seed'])
    return current
