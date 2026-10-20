"""Scope of lower relations left by R75's immediate W9/E self-loop.

This reuses already decreasing W9 comparisons; it adds no dispatcher rule.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('lower_loop_basis', HERE.parent/'critical_basis/critical_basis.py')
B = module_from_spec(spec)
spec.loader.exec_module(B)


def classify(u):
    """Retain the exact self-request and identify its complete lower relation."""
    data = B.blocked_nine(u)
    b, y = data['seed'], u//3
    assert y == (3*b+1)//4 and y % 24 == 7
    sy = B.NORMAL.step(y)
    hy, hs = B.absorption_plan(y), B.absorption_plan(sy)
    current = B.combine((1, hy['current']), (-1, {y: 1}), (-1, hs['current']))
    lower = B.combine((1, hy['coefficients']), (-1, hs['coefficients']))
    assert current == data['current']
    assert lower == B.combine((1, data['coefficients']), (-1, {b: 1}))
    nonzero = u % 576 == 453
    result = dict(seed=u, nine_parent=b, middle=y, current=current,
                  lower_coefficients=lower, nonzero=nonzero)
    if not nonzero:
        assert not current and not lower
        return result
    v, z = (u-3)//18, (u-1)//4
    assert v % 32 == 25 and b == 8*v+1 and y == 6*v+1
    assert z == (9*v+1)//2 == B.NORMAL.step(3*v)
    hv, hz = B.absorption_plan(v), B.absorption_plan(z)
    assert current == B.combine((1, hv['current']), (-1, {3*v: 1}), (-1, hz['current']))
    assert lower == B.combine((1, {v: 1}), (1, hv['coefficients']), (-1, hz['coefficients']))
    assert lower[v] == 1
    assert all(B.rho(w) < 3*v for w in lower if w != v)
    plan = dict(seed=v, current=B.combine((-1, current)),
                coefficients={w: -c for w, c in lower.items() if w != v})
    B.validate(plan)
    result.update(target=v, successor=z, oriented_plan=plan)
    return result
