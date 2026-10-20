"""Bounded original-rank repair of a complete class of critical-nine requests.

Only the positive high W9 request is replaced. Every signed lower request
and any unresolved W5 leader is retained. This is not universal supply.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('repair_transition', HERE.parent/'history_transition/history_transition.py')
M = module_from_spec(spec)
spec.loader.exec_module(M)
B, N = M.B, M.N
combine, atoms, divergence = B.combine, B.atoms, B.divergence


def integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise ValueError('Require an integer at least '+str(minimum))


def domain(w, threshold, max_bits=50000):
    integer(w, 1)
    integer(threshold, 11547)
    integer(max_bits, 16)
    if max(w.bit_length(), threshold.bit_length()) > max_bits:
        raise ValueError('Input exceeds the stated bit cap')
    if w % 16 != 9 or threshold % 2 != 1:
        raise ValueError('Require W9 and an odd original threshold')
    if threshold > 3*w or 32*w >= 33*threshold:
        raise ValueError('Require threshold <=3w and32w<33threshold')


def high_requests(data, threshold):
    return {v:c for v,c in data['coefficients'].items() if B.rho(v) >= threshold}


def local_decision(w, threshold, max_bits=50000):
    """Complete five-row decision for one full local R40 substitution."""
    domain(w, threshold, max_bits)
    data = B.nine_candidate(w)
    d, z = data['d'], data['z']
    leader, forced = None, None
    if d % 2:
        kind = 'odd_depth'
    elif not N.canonical(3*z):
        kind = 'even_noncanonical_upper'
        if 6*z+1 >= threshold:
            leader = 4*z+1
    elif 3*z < threshold:
        kind = 'even_canonical_below'
    elif 3*z % 8 != 1:
        kind = 'even_complementary_upper'
        leader = z
    else:
        kind = 'even_forward_upper'
        forced = (9*z+1)//4
        if B.T.critical(forced) and forced >= threshold:
            leader = (2*forced+1)//3
    high = {leader:1} if leader is not None else {}
    assert high_requests(data, threshold) == high
    if leader is not None and leader % 16 == 9:
        assert leader == z and 16*leader < 9*w
    out = dict(data, threshold=threshold, leader=leader, high=high,
               decision_kind=kind, forced=forced,
               status='unresolved' if high else 'descending')
    B.check_boundary(out)
    return out


def bounded_repair(w, threshold, max_nodes=2, max_bits=50000):
    """Replace at most two high W9 requests, always at the original threshold.

    A resource cap rejects rather than discarding a request. Local ordinary
    prefix lengths remain input dependent; two nodes is not a clock bound.
    """
    domain(w, threshold, max_bits)
    integer(max_nodes, 1)
    current, coefficients, nodes = {}, {w:1}, []
    leader = w
    while leader is not None and leader % 16 == 9:
        if len(nodes) >= max_nodes:
            raise ValueError('W9 substitution cap reached with an unresolved input')
        child = local_decision(leader, threshold, max_bits)
        assert coefficients[leader] == 1
        current = combine((1, current), (1, child['current']))
        coefficients = combine((1, coefficients), (-1, {leader:1}),
                               (1, child['coefficients']))
        nodes.append(child)
        leader = child['leader']
        assert high_requests(dict(coefficients=coefficients), threshold) == (
            {leader:1} if leader is not None else {})
        assert len(nodes) <= 2
    out = dict(seed=w, rank=B.rho(w), threshold=threshold,
               current=current, coefficients=coefficients, nodes=nodes,
               leading=leader, high={leader:1} if leader is not None else {},
               status='unresolved' if leader is not None else 'descending',
               rule='bounded_original_threshold_nine_repair')
    assert leader is None or leader % 8 == 5
    B.check_boundary(out)
    if leader is None:
        B.validate(out)
    return out


def repair_failed(k, max_nodes=2, max_bits=50000):
    """Compose the bounded repair into every R84 failed W9 leader."""
    integer(k)
    integer(max_bits, 16)
    if k.bit_length()+32 > max_bits:
        raise ValueError('Progression index exceeds the bit cap')
    original = M.plan(k)
    if original['status'] != 'unresolved' or original['leading'] % 16 != 9:
        raise ValueError('Require an R84 failed W9 leader')
    w, q = original['leading'], original['rank']
    upper, lower = B.absorption_plan(w), B.absorption_plan(original['seed'])
    assert original['coefficients'] == combine((1, {w:1}),
              (1, upper['coefficients']), (-1, lower['coefficients']))
    assert all(B.rho(v) < q for v in upper['coefficients'])
    assert all(B.rho(v) < q for v in lower['coefficients'])
    assert 3*w <= (original['raw']-1)//2 and 32*w < 33*q
    repair = bounded_repair(w, q, max_nodes, max_bits)
    current = combine((1, original['current']), (1, repair['current']))
    coefficients = combine((1, original['coefficients']), (-1, {w:1}),
                           (1, repair['coefficients']))
    out = dict(seed=original['seed'], rank=q, threshold=q, k=k,
               original_leader=w, original_quotient_length=original['quotient_length'],
               original_ordinary_clocks=original['ordinary_clocks'],
               current=current, coefficients=coefficients, nodes=repair['nodes'],
               leading=repair['leading'], high=repair['high'], status=repair['status'],
               rule='R84_original_rank_nine_repair')
    assert high_requests(out, q) == out['high']
    B.check_boundary(out)
    if out['status'] == 'descending':
        B.validate(out)
    return out


def even_upper_undo(w, max_bits=50000):
    """The complete named R46 inverse restores the positive W9 self-request.

    The remaining lower relation can be nonzero; no rows or coefficients are
    dropped. This excludes only this particular upper-prefix undo.
    """
    integer(w, 1)
    integer(max_bits, 16)
    if w % 16 != 9 or w.bit_length() > max_bits:
        raise ValueError('Require a positive W9 source within the bit cap')
    local = B.nine_candidate(w)
    d, h, z = local['d'], local['k'], local['z']
    if d % 2 or N.canonical(3*z):
        raise ValueError('Require the even noncanonical-upper branch')
    X, Y, u = 6*z+1, 2*z+1, 4*z+1
    D = h+1
    remainder = (X-1)//3**D
    assert (X-1) % 3**D == 0 and remainder % 3 != 0
    ternary = 4**D*remainder+2
    assert ternary == (9*w+3)//2 and ternary % 3 == 0 and ternary % 9 != 0
    origin = (2*ternary)//3-1
    assert origin == 3*w
    word = [1]+[2]*D
    upper = M.prefix(3*w, h+2, word)
    lower = M.prefix(w, h+2)
    assert upper['endpoint'] == X and lower['endpoint'] == Y
    three, u_abs = B.absorption_plan(3*w), B.absorption_plan(u)
    inverse_current = combine((1, N.bridge(3*u)['current']),
                              (-1, upper['current']), (1, three['current']),
                              (-1, u_abs['current']))
    inverse_coefficients = combine((1, three['coefficients']),
                                   (-1, u_abs['coefficients']))
    inverse_plan = dict(seed=u, current=inverse_current, coefficients=inverse_coefficients)
    B.check_boundary(inverse_plan)
    assert local['coefficients'][u] == 1
    current = combine((1, local['current']), (1, inverse_current))
    coefficients = combine((1, local['coefficients']), (-1, {u:1}),
                           (1, inverse_coefficients))
    w_abs, y_abs = B.absorption_plan(w), B.absorption_plan(Y)
    expected_current = combine((1, w_abs['current']), (-1, lower['current']),
                               (-1, y_abs['current']))
    expected_coefficients = combine((1, {w:1}), (1, w_abs['coefficients']),
                                    (-1, y_abs['coefficients']))
    assert current == expected_current and coefficients == expected_coefficients
    assert coefficients[w] == 1
    assert all(B.rho(v) < 3*w for v in coefficients if v != w)
    out = dict(seed=w, rank=3*w, d=d, z=z, upper=X, lower=Y,
               undone_input=u, D=D, j=1, inverse_origin=origin,
               ordinary_inverse_word=word, ordinary_inverse_length=h+2,
               current=current, coefficients=coefficients,
               inverse_plan=inverse_plan, status='unresolved', high={w:1})
    B.check_boundary(out)
    return out


def compile_plan(data, supplied):
    """Substitute all exact terminal currents only after strict-rank validation."""
    if data.get('status') != 'descending':
        raise ValueError('An unresolved high request is not a decreasing plan')
    domain(data.get('seed'), data.get('threshold'))
    B.validate(data)
    if any(B.rho(v) >= data['threshold'] for v in data['coefficients']):
        raise ValueError('A terminal request fails the original threshold')
    return B.compile_plan(data, supplied)
