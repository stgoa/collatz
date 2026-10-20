"""Complete fixed thirteenth-target phase, with a bounded native-rank test.

The fourteen templates decide this conditional comparison only. Failed
leaders and every signed terminal input are retained; no dispatcher changes.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('transition_basis', HERE.parent/'critical_basis/critical_basis.py')
B = module_from_spec(spec)
spec.loader.exec_module(B)
N = B.NORMAL
combine, atoms, divergence = B.combine, B.atoms, B.divergence
WORD = (1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2)
TEMPLATES = tuple(['A'*j for j in range(7)] +
                  ['A'*i+'B'+'A'*j for i in range(3) for j in range(3-i)] +
                  ['C'])


def integer(x, minimum=0):
    if type(x) is not int or x < minimum:
        raise ValueError('Require an integer at least '+str(minimum))


def prefix(x, length, word=None):
    integer(x, 1)
    integer(length)
    if x % 2 != 1 or (word is not None and len(word) != length):
        raise ValueError('Require an odd source and the stated word length')
    rows, states = {}, [x]
    for j in range(length):
        if word is not None and N.valuation2(3*x+1) != word[j]:
            raise ValueError('Incorrect exact ordinary valuation word')
        rows = combine((1, rows), (1, atoms((1, x))))
        x = N.step(x)
        states.append(x)
    return dict(current=rows, states=states, endpoint=x)


def parameters(k):
    integer(k)
    q, raw = 11547+3*2**19*k, 70237+2*3**14*k
    b = q//3
    data = prefix(q, 13, WORD)
    assert data['endpoint'] == raw and all(N.canonical(x) for x in data['states'][:-1])
    assert b % 16 == 9 and B.rho(b) == q and raw % 3 == 1
    assert 4*(raw-1) < 25*(q-1)
    return dict(k=k, seed=b, rank=q, raw=raw, prefix=data)


def transition(x, letter):
    integer(x, 1)
    if x % 2 != 1 or x % 3 != 1:
        raise ValueError('Require a positive odd raw state equal to1 modulo3')
    if letter == 'A' and x % 8 == 1:
        y, current = (3*x+1)//4, atoms((1, x))
        assert N.step(x) == y
    elif letter == 'B' and x % 16 == 3:
        y = (3*x-1)//8
        current = combine((1, prefix(x, 2)['current']), (-1, atoms((1, y))))
        assert N.step(N.step(x)) == N.step(y)
    elif letter == 'C' and x % 32 == 5:
        y, current = (3*x+1)//16, atoms((1, x))
        assert N.step(x) == y
    else:
        raise ValueError('Incorrect guarded transition')
    assert y % 3 == 1 and 0 < y < x
    assert divergence(current) == atoms((1, x), (-1, y))
    factor = {'A': 4, 'B': 8, 'C': 16}[letter]
    assert factor*(y-1) <= 3*(x-1)
    return dict(letter=letter, source=x, target=y, current=current)


def decision(k):
    data = parameters(k)
    q, x = data['rank'], data['raw']
    word, steps = '', []
    current = data['prefix']['current']
    while True:
        normal = N.bridge(x)
        n = normal['minimum']
        if n < q:
            status = 'descending'
            break
        assert word in TEMPLATES and len(word) <= 6
        if B.T.critical(n):
            status = 'unresolved'
            break
        assert n % 8 == 1
        if x % 8 == 1:
            letter = 'A'
        elif x % 16 == 3:
            letter = 'B'
        elif x % 32 == 5:
            letter = 'C'
        else:
            raise AssertionError('The complete above-rank phase classification failed')
        row = transition(x, letter)
        assert row['target'] == N.step(n)
        current = combine((1, current), (1, row['current']))
        steps.append(row)
        word += letter
        x = row['target']
    current = combine((1, current), (1, normal['current']))
    ell = 13+len(word)
    if normal['selected_partner']:
        padding = N.valuation2(normal['base']+1)
    elif normal['F_exponent'] or word.endswith('B'):
        padding = 1
    else:
        padding = 0
    left, right = prefix(q, ell+padding), prefix(n, padding)
    assert left['endpoint'] == right['endpoint']
    assert current == combine((1, left['current']), (-1, right['current']))
    assert divergence(current) == atoms((1, q), (-1, n))
    assert len(word) <= 7
    return dict(data, status=status, word=word, steps=steps, stop_raw=x,
                terminal=n, normalizer=normal, comparison=current,
                quotient_length=ell, ordinary_clocks=[ell+padding, padding],
                ordinary_meeting=left['endpoint'])


def plan(k):
    data = decision(k)
    q, b, n = data['rank'], data['seed'], data['terminal']
    high, low = B.absorption_plan(n), B.absorption_plan(b)
    current = combine((1, data['comparison']), (1, high['current']), (-1, low['current']))
    coefficients = combine((1, high['coefficients']), (-1, low['coefficients']))
    result = dict(data, current=current, coefficients=coefficients,
                  rule='complete_thirteenth_target_phase')
    B.check_boundary(result)
    if data['status'] == 'descending':
        B.validate(result)
    else:
        leading = B.T.critical_inverse(n)
        assert coefficients[leading] == 1 and B.rho(leading) == n >= q
        assert all(B.rho(v) < n for v in coefficients if v != leading)
        result['leading'] = leading
    return result


def initial_row(k):
    """Exact complete initial rows; A/B entries use the bounded continuation."""
    data = parameters(k)
    r = data['raw']
    if k % 4 == 1:
        return dict(kind='critical_after_zero_or_one_halving', accepted=False)
    if k % 8 == 7:
        return dict(kind='complementary_raw', accepted=False)
    if k % 8 == 0:
        v = (r-1)//4
        return dict(kind='F_of_climber', accepted=N.selected(v), test_seed=v)
    if k % 16 == 4:
        m = (3*r+1)//16
        return dict(kind='C_then_complete_test', accepted=not B.T.critical(m), test_seed=m)
    if k % 16 == 12:
        return dict(kind='two_F_removals', accepted=True)
    if k % 4 == 2:
        return dict(kind='A_continuation', accepted=None)
    assert k % 8 == 3
    return dict(kind='B_continuation', accepted=None)


def sharp_family(index=0):
    integer(index)
    k = 9954+2**14*index
    data = decision(k)
    assert data['word'] == 'A'*7 and data['status'] == 'descending'
    assert data['quotient_length'] == 20
    x, q = data['rank'], data['rank']
    states = [x]
    for _ in range(20):
        x = N.quotient_step(x)
        states.append(x)
    assert all(x > q for x in states[1:-1]) and x < q
    return dict(data, sharp_index=index, quotient_states=states)


def old_failure(k):
    data = parameters(k)
    q = data['rank']
    u, r, f = (3*q+3)//4, (6561*q+8965)//1024, (19683*q+27919)//4096
    v = (2*f+1)//3
    assert N.valuation2(3*u+1) == 7 and r % 8 == 1 and N.step(r) == f
    assert f == 55495+2**7*3**10*k and f % 3 == 1 and N.canonical(f)
    assert B.rho(v) == f > B.rho(u) > q
    return dict(k=k, returning=u, first=r, second=f, leading=v,
                outside_R81=(k % 3**11 != 0))


def compile_plan(data, supplied):
    if data.get('status') != 'descending':
        raise ValueError('The original-rank comparison retains an unresolved leader')
    B.validate(data)
    return B.compile_plan(data, supplied)
