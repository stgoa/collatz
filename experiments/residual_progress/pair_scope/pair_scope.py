"""Exact half-seed comparisons and a hypothetical restricted-pair normal form.

No universal tripling or doubling bridge is assumed by the current constructor.
The augmented normal form classifies the explicitly named formal identity graph.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("pair_scope_run", HERE.parent / "complementary_bridge/run_bridge.py")
RUN = module_from_spec(spec)
spec.loader.exec_module(RUN)
NORMAL = RUN.NORMAL
step, combine, divergence = RUN.step, RUN.combine, RUN.divergence


def atoms(*terms):
    result = {}
    for coefficient, state in terms:
        if state != 1:
            result[state] = result.get(state, 0) + coefficient
    return {state: coefficient for state, coefficient in result.items() if coefficient}


def compare_half(x):
    """Expose exactly the R26 run and the smaller half's closing run."""
    data = RUN.bridge(x)
    a, d, w = data['a'], data['d'], data['w']
    q = (x - 1) // 2
    path = [q]
    for _ in range(a - 1):
        path.append(step(path[-1]))
    assert path[-1] == w
    current = combine((1, data['current']), (-1, RUN.H.path_current(path)))
    target = data['target']
    assert divergence(current) == atoms((1, x), (-1, q), (-1, target), (1, w))
    k = d // 2
    symbols = [('T', 3**j * w, 1) for j in range(k)]
    if d % 2 == 0:
        symbols.append(('D', 3**k * w, 1))
    boundary = {}
    for kind, u, coefficient in symbols:
        pair = atoms((coefficient, 3*u if kind == 'T' else 2*u+1), (-coefficient, u))
        boundary = combine((1, boundary), (1, pair))
    assert boundary == atoms((1, target), (-1, w))
    return dict(root=x, lower_seed=q, a=a, t=data['t'], d=d, w=w,
                target=target, half_path=path, current=current, symbols=symbols)


def augmented_normal_form(x):
    """Normal form if every formal pair 3w~w, w=3 mod8, is adjoined.

    This returns a graph label, NOT a current or a Collatz certificate.
    """
    q = NORMAL.normal_form(x)
    path = [q]
    while q % 24 == 9:
        old = q
        q = (q - 3)//6 if q % 48 == 9 else q//3
        assert 0 < q < old and NORMAL.canonical(q)
        path.append(q)
    return q, path


def mersenne_obstruction(a):
    """An infinite one-run comparison family outside the augmented graph."""
    if a < 19 or a % 16 != 3:
        raise ValueError('Require a>=19, a=3 modulo16')
    x = 2**a - 1
    N = 12 * 2**(a - 4)
    data = compare_half(x)
    w = data['w']
    assert data['d'] == 3 and w % 24 == 1 and data['target'] == 3*w
    expected = (3*w-1)//2 if w % 16 == 1 else 3*w
    left, left_path = augmented_normal_form(3*w)
    right, right_path = augmented_normal_form(w)
    assert left == expected and right == w and left != right
    assert len(left_path) == len(right_path) == 1
    assert data['lower_seed'] < N < x and 8*x > 9*N and 2*x < 3*N
    assert x % 12 == 7 and not RUN.H.selected(x)
    return dict(a=a, N=N, root=x, lower_seed=data['lower_seed'], w=w,
                target=3*w, left_minimum=left, right_minimum=right)
