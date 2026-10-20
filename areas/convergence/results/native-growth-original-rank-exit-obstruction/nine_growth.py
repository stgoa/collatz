"""Exact native-W9 growth and two scoped inverse undos.

All tables are conditional signed comparisons. No new accepted domain or
universal termination is claimed. No unrestricted absorption search is used.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent

def _load(name, path):
    spec = spec_from_file_location(name, HERE.parent / path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

B = _load('native_growth_basis', 'critical_basis/critical_basis.py')
INVERSE = _load('native_growth_inverse', 'nonselected_inverse/inverse_phases.py')
N, W = B.NORMAL, B.NINE
combine, atoms, divergence = B.combine, B.atoms, B.divergence


def _int(x, minimum=0):
    if not isinstance(x, int) or isinstance(x, bool) or x < minimum:
        raise ValueError('Require an integer at least ' + str(minimum))


def guarded(b):
    _int(b, 1)
    return b % 8192 == 905


def order(b):
    if not guarded(b):
        raise ValueError('Require b=905 modulo8192')
    return N.valuation2(217*b+223)


def return_count(b):
    return (order(b)-13)//9


def affine_iterate(b, count):
    _int(b, 1)
    _int(count)
    constant = 223*(729**count-512**count)//217
    numerator = 729**count*b+constant
    denominator = 512**count
    if numerator % denominator:
        raise ValueError('The affine iterate is not an integer')
    return numerator//denominator


def cylinder(count):
    """Exactly count complete re-entries are not asserted by this cylinder.

    This residue gives at least count complete returns, including the final
    guard. Exact counts are given by return_count or exact_family.
    """
    _int(count)
    modulus = 2**(13+9*count)
    constant = 223*(729**count-512**count)//217
    residue = (512**count*905-constant)*pow(729**count, -1, modulus) % modulus
    return residue, modulus


def exact_family(count, exit_order=17, offset=0):
    _int(count)
    _int(exit_order, 13)
    _int(offset)
    if exit_order > 21:
        raise ValueError('Require exit order between13 and21')
    h = 9*count+exit_order
    modulus = 2**(h+1)
    residue = (2**h-223)*pow(217, -1, modulus) % modulus
    b = residue+offset*modulus
    assert b > 0 and order(b) == h and return_count(b) == count
    return b


def prefix(x, length):
    N._odd(x)
    _int(length)
    current = {}
    for _ in range(length):
        if x != 1:
            current = combine((1, current), (1, {x: 1}))
        x = N.step(x)
    return x, current


def native_step(b):
    if not guarded(b):
        raise ValueError('Require the complete native a5 guard')
    c = (729*b+223)//512
    x, current = 3*b, {}
    for valuation in (1, 2, 1, 1, 1, 2):
        assert N.valuation2(3*x+1) == valuation
        current = combine((1, current), (1, {x: 1}))
        x = N.step(x)
    assert x == 6*c+1 and x % 32 == 23
    bridge = N.bridge(x)
    assert bridge['minimum'] == 3*c and len(bridge['left_prefix']) == 4
    current = combine((1, current), (1, bridge['current']))
    assert divergence(current) == atoms((1, 3*b), (-1, 3*c))
    assert c % 16 == 9 and c > b
    left, lp = prefix(3*b, 9)
    right, rp = prefix(3*c, 3)
    assert left == right and current == combine((1, lp), (-1, rp))
    return dict(seed=b, target=c, current=current, ordinary_clocks=[9, 3],
                quotient_clock=6, end_in_guard=(c % 8192 == 905))


def growth_plan(b, steps):
    _int(steps, 1)
    if steps > return_count(b)+1:
        raise ValueError('A source has left the native a5 guard')
    x, bridge, chain = b, {}, [b]
    for _ in range(steps):
        row = native_step(x)
        x = row['target']
        bridge = combine((1, bridge), (1, row['current']))
        chain.append(x)
    assert x == affine_iterate(b, steps)
    upper, lower = B.absorption_plan(x), B.absorption_plan(b)
    current = combine((1, bridge), (1, upper['current']), (-1, lower['current']))
    coefficients = combine((1, {x: 1}), (1, upper['coefficients']),
                           (-1, lower['coefficients']))
    assert coefficients[x] == 1
    assert all(B.rho(u) < 3*x for u in coefficients if u != x)
    left, lp = prefix(3*b, 6*steps+3)
    right, rp = prefix(3*x, 3)
    assert left == right and bridge == combine((1, lp), (-1, rp))
    out = dict(seed=b, target=x, chain=chain, bridge=bridge,
               current=current, coefficients=coefficients,
               ordinary_clocks=[6*steps+3, 3], quotient_clock=6*steps,
               status='unresolved')
    B.check_boundary(out)
    return out


def exit_phase(b):
    """Local R40 binary phase after the last guarded source, not global success."""
    h = order(b)
    if not 13 <= h <= 21:
        raise ValueError('Require a final guarded source')
    omega = (217*b+223)//2**h
    c = native_step(b)['target']
    d = N.valuation2(9*c-1)
    if h == 13:
        assert d == 4+N.valuation2(6561*omega-139)
        canonical_upper = None
    else:
        assert d == 4
        z = (9*c-1)//16
        if h in (14, 15):
            canonical_upper = omega % 4 == 3
        elif h == 16:
            k = N.valuation2(19683*omega-25)
            unit = (19683*omega-25)//(217*2**k)
            assert 3*z+1 == 2**(k+3)*unit
            canonical_upper = unit % 4 != pow(3, k+3, 4)
        else:
            canonical_upper = h == 17
        assert canonical_upper == N.canonical(3*z)
    return dict(seed=b, order=h, odd_part=omega, child=c, d=d,
                canonical_upper=canonical_upper)


def exit_plan(b):
    """Full exact H17 comparison, tested against its original rank3b."""
    r = return_count(b)
    if order(b) != 9*r+17:
        raise ValueError('Require final guarded order17')
    before = growth_plan(b, r+1)
    c = before['target']
    z, y, x = (9*c-1)//16, (9*c+7)//8, N.step(c)
    assert z % 8 == 5 and z % 9 == 5 and N.canonical(3*z)
    local = W.local_plan(c)
    assert local['d'] == 4 and local['z'] == z and not local['exception']
    hc, hy, hz, hb = [B.absorption_plan(v) for v in (c, y, z, b)]
    assert hc['coefficients'] == hy['coefficients']
    assert combine((1, hc['current']), (-1, hy['current'])) == {c: 1, x: 1}
    current = combine((1, before['bridge']), (1, local['current']),
                      (1, hc['current']), (-1, hb['current']))
    coefficients = combine((1, local['coefficients']), (1, hc['coefficients']),
                           (-1, hb['coefficients']))
    assert coefficients == combine((1, {z: 1}), (1, hz['coefficients']),
                                   (-1, hb['coefficients']))
    upper = combine((1, current), (-1, hz['current']), (1, hb['current']))
    left, lp = prefix(3*b, 6*r+12)
    right, rp = prefix(3*z, 4)
    assert left == right and upper == combine((1, lp), (-1, rp))
    assert coefficients[z] == 1
    assert all(B.rho(u) < 3*z for u in coefficients if u != z)
    assert (3*z < 3*b) == (r == 0)
    out = dict(seed=b, target=z, previous_target=c, returns=r,
               current=current, coefficients=coefficients,
               ordinary_clocks=[6*r+12, 4],
               status='descending' if r == 0 else 'unresolved')
    B.check_boundary(out)
    if r == 0:
        B.validate(out)
    return out


def standard_inverse_undo(b, ray):
    """k4 restores the previous comparison; k8 restores the exit itself."""
    if ray not in (4, 8) or isinstance(ray, bool):
        raise ValueError('Require base ray4 or8')
    out = exit_plan(b)
    z = out['target']
    inv = INVERSE.inverse_bridge(z, ray)
    data = inv['parameters']
    assert data['h'] == (1 if ray == 4 else 0)
    hp, hz = B.absorption_plan(data['lower']), B.absorption_plan(z)
    child = dict(seed=z,
                 current=combine((1, inv['current']), (1, hp['current']),
                                 (-1, hz['current'])),
                 coefficients=combine((1, hp['coefficients']),
                                      (-1, hz['coefficients'])))
    B.check_boundary(child)
    result = dict(seed=b,
                  current=combine((1, out['current']), (1, child['current'])),
                  coefficients=combine((1, out['coefficients']), (-1, {z: 1}),
                                       (1, child['coefficients'])))
    expected = growth_plan(b, out['returns']+1) if ray == 4 else out
    assert result['current'] == expected['current']
    assert result['coefficients'] == expected['coefficients']
    B.check_boundary(result)
    return dict(result, ray=ray, inverse_depth=data['h'],
                restored='pre_exit_growth' if ray == 4 else 'exit_comparison')


def return_composition(b):
    """R40 blocked child plus R75 conversion equals the direct return exactly."""
    if return_count(b) < 1:
        raise ValueError('Require at least one complete guarded re-entry')
    step = native_step(b)
    c = step['target']
    assert guarded(c)
    local = W.local_plan(c)
    assert local['d'] == 4 and local['exception'] is not None
    conversion = B.returning_conversion(local['exception'])
    hc, hb = B.absorption_plan(c), B.absorption_plan(b)
    coefficients = combine((1, local['coefficients']),
                           (-1, {local['exception']: 1}),
                           (1, conversion['coefficients']),
                           (1, hc['coefficients']), (-1, hb['coefficients']))
    current = combine((1, step['current']), (1, local['current']),
                      (1, conversion['current']), (1, hc['current']),
                      (-1, hb['current']))
    target = growth_plan(b, 1)
    assert current == target['current'] and coefficients == target['coefficients']
    return target
