"""Complete odd-h pair interface and exact scope of its ternary restriction.

No unknown orbit is searched. Input compilation uses supplied finite currents.
The high-h reduction is complete but may enter an unresolved tripling domain.
"""
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


NORMAL = _load('odd_interface_normal', 'bridge_normal_form/normal_form.py')
BOUNDED = _load('odd_interface_bounded', 'bounded_run_cycles/bounded_runs.py')
step, divergence = NORMAL.step, NORMAL.divergence


def combine(*terms):
    result = Counter()
    for coefficient, measure in terms:
        for x, value in measure.items():
            result[x] += coefficient * value
    return {x: value for x, value in sorted(result.items()) if x != 1 and value}


def delta(x):
    return {} if x == 1 else {x: 1}


def pair(w):
    return combine((1, delta(3*w)), (-1, delta(w)))


def Q(z):
    return combine((1, delta(6*z+1)), (-1, delta(z)))


def prefix(x, length):
    rows = Counter()
    for _ in range(length):
        if x != 1:
            rows[x] += 1
        x = step(x)
    return x, dict(sorted(rows.items()))


def ternary(n):
    if n <= 0:
        raise ValueError('Expected a positive integer')
    k = 0
    while n % 3 == 0:
        n //= 3
        k += 1
    return k, n


def zplus(z):
    NORMAL._odd(z)
    return ternary(z)[1] % 3 == 1


def critical(q):
    return NORMAL.canonical(q) and q % 4 == 3 and q % 3 != 2


def critical_target(z):
    NORMAL._odd(z)
    if z % 8 == 3:
        raise ValueError('The critical bijection excludes z=3 modulo8')
    q = NORMAL.normal_form(6*z+1)
    assert critical(q) and q > z
    assert q == (3*z if NORMAL.canonical(3*z) else 6*z+1)
    return q


def critical_index(q):
    if not critical(q):
        raise ValueError('Expected a critical canonical target')
    z = q//3 if q % 3 == 0 else (q-1)//6
    assert z > 0 and z % 2 and z % 8 != 3
    assert critical_target(z) == q
    return z


def covered_critical(q):
    """Exact image of the actual odd-h Zplus restriction, excluding z3mod8."""
    if not critical(q):
        return False
    return (ternary(q)[1] % 3 == 1 if q % 3 == 0
            else ternary(q-1)[1] % 3 == 2)


def chi(x):
    """Formal R35 static-catalogue label, not an absorption certificate."""
    q = NORMAL.normal_form(x)
    while q % 24 == 9:
        q = (q-3)//6 if q % 48 == 9 else q//3
    return q


def odd_parent(z):
    if not zplus(z):
        raise ValueError('Actual odd-h parameters require ternary unit1')
    k, C = ternary(z)
    w = (2**(2*k+3)*C+1)//3
    assert 3*w == 2**(2*k+3)*C+1 and w % 8 == 3 and w > z
    assert NORMAL.valuation2(3*w-1) == 2*k+3
    return w, k


def q_to_tripling(z):
    """Return div L=Q(z)-P(child), by complete elementary identities."""
    NORMAL._odd(z)
    r = NORMAL.valuation2(3*z+1)
    if NORMAL.canonical(3*z):
        child = z
        bridge = NORMAL.bridge(6*z+1)
        assert bridge['minimum'] == 3*z
        current = bridge['current']
        selected_length = r+1
        kind = 'direct'
    else:
        child = 4*z+1
        bridge = NORMAL.bridge(3*child)
        assert NORMAL.canonical(6*z+1) and bridge['minimum'] == 6*z+1
        sibling = combine((1, delta(child)), (-1, delta(z)))
        current = combine((1, sibling), (-1, bridge['current']))
        selected_length = r+2
        kind = 'F'
    assert divergence(current) == combine((1, Q(z)), (-1, pair(child)))
    return dict(z=z, child=child, kind=kind, current=current,
                selected_length=selected_length)


def odd_reduction(w):
    if w <= 0 or w % 8 != 3:
        raise ValueError('Expected positive w=3 modulo8')
    h = NORMAL.valuation2(3*w-1)
    if h % 2 == 0:
        raise ValueError('This interface concerns odd h only')
    k = (h-3)//2
    z = 3**k*((3*w-1)//2**h)
    assert odd_parent(z) == (w, k)
    left, L = prefix(3*w, k+1)
    right, R = prefix(w, k+1)
    assert left == 6*z+1 and right == 4*z+1
    sibling = combine((1, delta(right)), (-1, delta(z)))
    local = combine((1, L), (-1, R), (-1, sibling))
    assert divergence(local) == combine((1, pair(w)), (-1, Q(z)))
    child = q_to_tripling(z)
    current = combine((1, local), (1, child['current']))
    assert divergence(current) == combine((1, pair(w)), (-1, pair(child['child'])))
    if h >= 7:
        assert 8*child['child'] < 7*w
    return dict(w=w, h=h, k=k, z=z, child=child['child'],
                kind=child['kind'], current=current,
                selected_length=child['selected_length'],
                shrinking=child['child'] < w)


def parent_clock(data, child_clock):
    if child_clock < 0:
        raise ValueError('Expected a prescribed nonnegative child clock')
    return data['k']+1+max(child_clock, data['selected_length'])


def required_indices(limit):
    if not isinstance(limit, int) or limit < 1:
        raise ValueError('Expected a positive integer cutoff')
    return sorted(critical_index(q) for q in range(3, limit+1, 2) if critical(q))


def extract_path(source, current):
    """Use only nonzero supplied rows; finite divergence proves success."""
    rows = {}
    q = source
    for _ in range(len(current)+1):
        if q == 1:
            assert divergence(rows) == delta(source)
            return rows
        assert q in current and current[q] and q not in rows
        rows[q] = 1
        q = step(q)
    raise AssertionError('Finite supplied graph failed its positive-source claim')


def compile_inputs(limit, inputs):
    """Compile supplied exact/one-sided Q inputs into an exact U_limit current.

    An input current J must have Q(z)-div(J)<=0 pointwise. No new unknown
    future is exposed: extraction uses only existing nonzero current rows.
    """
    needed = required_indices(limit)
    for z in needed:
        residual = combine((1, Q(z)), (-1, divergence(inputs[z])))
        assert all(c <= 0 for c in residual.values())
    paths = {1: {}}
    for x in range(3, limit+1, 2):
        q = NORMAL.normal_form(x)
        if q < x:
            candidate = combine((1, NORMAL.bridge(x)['current']), (1, paths[q]))
        elif x % 8 == 1:
            target = step(x)
            assert target < x
            candidate = combine((1, delta(x)), (1, paths[target]))
        elif x % 3 == 2:
            target = (2*x-1)//3
            assert target < x and step(target) == x
            candidate = combine((1, paths[target]), (-1, delta(target)))
        else:
            z = critical_index(x)
            assert z < x
            candidate = combine((1, inputs[z]),
                                (-1, NORMAL.bridge(6*z+1)['current']),
                                (1, paths[z]))
        boundary = divergence(candidate)
        remainder = combine((1, boundary), (-1, delta(x)))
        assert all(c >= 0 for c in remainder.values())
        paths[x] = extract_path(x, candidate)
    current = combine(*((1, path) for path in paths.values()))
    assert divergence(current) == {x: 1 for x in range(3, limit+1, 2)}
    return dict(limit=limit, indices=needed, paths=paths, current=current)


def delayed_ray(repeats, extra_scale=0):
    """Actual weight2 roots avoiding the covered critical phase for8r steps."""
    if extra_scale < 0:
        raise ValueError('Expected nonnegative scale increment')
    residue, modulus = BOUNDED.cylinder(repeats)
    residue += modulus*((10-residue)*pow(modulus, -1, 27) % 27)
    period = 27*modulus
    N = 12*(modulus << (5+extra_scale))
    x = residue+period*((N-residue)//period+1)
    assert N < x < 9*N//8 and x % 36 == 19
    data = BOUNDED.witness(x, repeats)
    assert all(critical(q) and not covered_critical(q) for q in data['block_returns'])
    assert all(not covered_critical(q) for q in data['states'])
    assert all(q % 27 == 10 for q in data['cycle_starts'])
    assert all(q % 9 == 4 for q in data['block_returns'][1::2])
    return dict(N=N, weight=2, **data)
