"""A prescribed high-history merger for a complete blocked W9 cylinder.

Only finite arithmetic prefixes and the native critical H plans are constructed.
Every unresolved pair current remains a supplied premise. No orbit search is
performed by this module, including its finite anchor verifier.
"""
from collections import Counter
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, relative):
    spec = spec_from_file_location(name, HERE.parent/relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


BASIS = load('native_history_basis', 'critical_basis/critical_basis.py')
SECOND = load('native_history_second', 'returning_continuation/returning_continuation.py')
INVERSE = SECOND.INVERSE
NORMAL, T = BASIS.NORMAL, BASIS.T
combine, atoms, divergence, rho = BASIS.combine, BASIS.atoms, BASIS.divergence, BASIS.rho
ANCHOR, LOWER, BINARY, TERNARY = 11547, 11391, 17, 12
WORD = (1,)*6+(2, 2)+(1,)*4+(2,)
BASE_PATH = (11391, 17087, 25631, 38447, 57671, 86507, 129761,
             97321, 72991, 109487, 164231, 246347, 369521, 277141)
PERIOD = 2**BINARY*3**TERNARY


def integer(value, minimum=0):
    return isinstance(value, int) and not isinstance(value, bool) and value >= minimum


def eligible(b):
    return integer(b, ANCHOR//3) and (3*b-ANCHOR) % PERIOD == 0


def family(depth=12, index=0):
    if not integer(depth, 12) or not integer(index):
        raise ValueError('Require integer depth>=12 and index>=0')
    q = ANCHOR+2**BINARY*3**depth*index
    p = LOWER+2**(BINARY+19)*3**(depth-12)*index
    assert 3**12*p == 2**19*q-309105
    return dict(depth=depth, index=index, seed=q//3, root=q, lower=p)


def prefix(seed, word):
    NORMAL._odd(seed)
    x, states, current = seed, [seed], Counter()
    for a in word:
        if not integer(a, 1) or x == 1 or NORMAL.valuation2(3*x+1) != a:
            raise ValueError('The prescribed ordinary valuation word fails')
        current[x] += 1
        x = NORMAL.step(x)
        states.append(x)
    current = combine((1, current))
    assert divergence(current) == atoms((1, seed), (-1, x))
    return dict(seed=seed, endpoint=x, states=states, current=current, word=list(word))


def parameters(b):
    if not eligible(b):
        raise ValueError('Require b=3849 modulo 2^17*3^11')
    q = 3*b
    p = (2**19*q-309105)//3**12
    y, u = (3*q+1)//2, (3*q+3)//4
    assert 0 < b < p < q < y
    assert all(NORMAL.canonical(x) for x in (p, q, y))
    assert b % 16 == 9 and NORMAL.valuation2(9*b-1) == 4
    z = (9*b-1)//16
    assert not NORMAL.canonical(3*z)
    assert BASIS.nine_candidate(b)['high'] == {u: 1}
    left, right = prefix(q, (1,)), prefix(p, WORD)
    assert left['endpoint'] == y
    assert right['endpoint'] == NORMAL.F_power(y, 2) == 16*y+5
    assert NORMAL.normal_form(right['endpoint']) == y
    assert all(NORMAL.canonical(x) and x > q for x in right['states'][1:-1])
    assert NORMAL.step(y) == NORMAL.step(right['endpoint']) == (9*q+5)//8 > q
    # The ordinary second endpoint is also canonical on this cylinder.
    assert NORMAL.canonical(NORMAL.step(y))
    return dict(seed=b, rank=q, lower=p, meeting=y, returning=u,
                upper=left, lower_path=right, ordinary_clocks=[2, 14],
                quotient_clocks=[1, 13])


def history_plan(b):
    data = parameters(b)
    q, p, y = data['rank'], data['lower'], data['meeting']
    x = data['lower_path']['endpoint']
    bridge = combine((1, data['upper']['current']), (-1, data['lower_path']['current']),
                     (-1, {x: 1}), (1, {y: 1}))
    assert divergence(bridge) == atoms((1, q), (-1, p))
    high, low = BASIS.absorption_plan(p), BASIS.absorption_plan(b)
    current = combine((1, bridge), (1, high['current']), (-1, low['current']))
    coefficients = combine((1, high['coefficients']), (-1, low['coefficients']))
    out = dict(seed=b, rank=q, current=current, coefficients=coefficients,
               parameters=data, bridge=bridge, status='descending', rule='native_high_history')
    assert all(rho(v) <= p < q for v in coefficients)
    BASIS.validate(out)
    return out


def old_endpoint_failures(b):
    """R44/R52 fail even before transport to the smaller original W9 rank."""
    data = parameters(b)
    q, u = data['rank'], data['returning']
    first, second = SECOND.OLD.forward_plan(u), SECOND.continuation_plan(u)
    n, f = (6561*q+8965)//1024, (19683*q+27919)//4096
    v = (2*f+1)//3
    assert first['parameters']['a'] == 7
    assert first['parameters']['endpoint'] == n and n % 8 == 1
    assert second['parameters']['endpoint'] == f and f % 32 == 7
    assert NORMAL.canonical(n) and NORMAL.canonical(f) and f > rho(u) > q
    assert first['status'] == second['status'] == 'unresolved'
    assert first['coefficients'][v] == second['coefficients'][v] == 1 and rho(v) == f
    # Native H retains this very same high request; the old overhead is not
    # the cause of these two failures.
    assert BASIS.absorption_plan(n)['coefficients'][v] == 1
    assert BASIS.absorption_plan(f)['coefficients'][v] == 1
    return dict(returning=u, first_endpoint=n, second_endpoint=f, higher_pair=v,
                higher_rank=f, first_status=first['status'], second_status=second['status'])


def five_frontier_plan(b):
    """The same merger also admits an old W5-only H frontier on this cylinder.

    The parent is still W9. This is not a modification to the W5 dispatcher,
    and shows that R75's improved general H bound is not necessary here.
    """
    native = history_plan(b)
    q, p = native['rank'], native['parameters']['lower']
    high, low = BASIS.RANK.absorption_plan(p), BASIS.RANK.absorption_plan(b)
    assert p % 512 == 127
    assert all(rho(v) <= p for v in high['coefficients'])
    assert all(8*rho(v) <= 9*b+5 < 8*q for v in low['coefficients'])
    out = dict(seed=b, rank=q,
               current=combine((1, native['bridge']), (1, high['current']), (-1, low['current'])),
               coefficients=combine((1, high['coefficients']), (-1, low['coefficients'])),
               status='descending', rule='native_high_history_five_frontier')
    assert all(v % 8 == 5 for v in out['coefficients'])
    BASIS.validate(out)
    return out


def verify_anchor(path=None):
    """Verify the stored complete lower-origin closure using only supplied edges."""
    data = json.loads(Path(path or HERE/'anchor_certificate.json').read_text())
    if data['anchor'] != ANCHOR:
        raise ValueError('Wrong anchor')
    rows = data['edges']
    edges = dict(rows)
    if len(edges) != len(rows) or any(not integer(x, 1) or not integer(y, 1) for x, y in rows):
        raise ValueError('Duplicate or invalid anchor rows')
    assert ANCHOR not in edges
    assert all(NORMAL.canonical(x) and NORMAL.quotient_step(x) == y and y in edges
               for x, y in edges.items())
    origins = [x for x in range(1, ANCHOR, 2) if NORMAL.canonical(x)]
    assert all(x in edges for x in origins)
    reached = {1}
    for x in origins:
        seen = set()
        while x not in reached:
            assert x not in seen
            seen.add(x)
            x = edges[x]
        reached.update(seen)
    assert reached == set(edges)
    return dict(anchor=ANCHOR, states=len(edges), maximum=max(edges), origins=len(origins))


def shadow_word(q, word):
    """Replay one legal all-ray inverse word; theorem covers every such word.

    The stored anchor must be verified separately before relying on the
    all-depth exclusion premise. This function does not search inverse words.
    """
    if not integer(q, ANCHOR+1) or not NORMAL.canonical(q) or (q-ANCHOR) % 3**len(word):
        raise ValueError('Require a larger canonical lift at sufficient ternary precision')
    actual, shadow, slope, records = q, ANCHOR, Fraction(1), []
    for depth, (kind, index) in enumerate(word, 1):
        old_gap = slope-Fraction(shadow+1, ANCHOR+1)
        actual, alpha, beta = INVERSE.inverse_step(actual, kind, index)
        shadow, _, _ = INVERSE.inverse_step(shadow, kind, index)
        slope *= alpha
        gap = slope-Fraction(shadow+1, ANCHOR+1)
        assert gap == alpha*old_gap+(alpha-beta-1)/(ANCHOR+1) > 0
        assert shadow >= ANCHOR and slope > 1 and actual > q
        assert actual == slope*(q-ANCHOR)+shadow
        records.append(dict(depth=depth, actual=actual, shadow=shadow,
                            slope=[slope.numerator, slope.denominator]))
    return records


def compile_plan(plan, supplied):
    if plan.get('status') != 'descending':
        raise ValueError('Require a descending native-history plan')
    BASIS.validate(plan)
    return BASIS.compile_plan(plan, supplied)
