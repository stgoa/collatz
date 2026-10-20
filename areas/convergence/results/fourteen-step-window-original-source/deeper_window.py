"""Exact finite inverse suffixes in the R92 original-source window.

The caller supplies a separately certified rational first-hit tuple [u,d,E].
This module does not claim completeness of a supplied basin table. The two
enumerators keep full affine intercepts and the original binary source guard.
All public result fields are JSON-compatible exact integers or integer pairs.
"""

from fractions import Fraction

D, B, A, M = 7153, 299947, 3**12, 2**19
ROOT = 899841
V0, VP = 67839005952677, 2**18 * 3**18
Q0, QP = 70506316836123, 3 * 2**45
TBOUND = 892688 + 12*A
BASES = {
    0: (("ray0", 3, 3), ("ray1", 4, 3)),
    1: (("ray0", 2, -1), ("ray1", 5, 19)),
    2: (("point", 1, -1), ("ray0", 6, 19), ("ray1", 7, 83)),
}


def _pair(value):
    return [value.numerator, value.denominator]


def guard(returns):
    """All ell with at least returns Phi reentries: residue mod modulus."""
    if type(returns) is not int or returns < 0:
        raise ValueError("return count must be a nonnegative integer")
    modulus = 2**(19*returns)
    offset = (D*V0+B)//2**18
    residue = (-offset * pow(D*3**18, -1, modulus)) % modulus
    return [residue, modulus]


def boundary(hit):
    """Convert a certified relevant [u,first_depth,first_cost] to x(ell)."""
    if (not isinstance(hit, (list, tuple)) or len(hit) != 3
            or any(type(n) is not int for n in hit)):
        raise ValueError("hit must contain three exact integers")
    u, depth, cost = hit
    if u <= D or u % 2 == 0 or depth < 5 or cost < 0 or depth % 12 != 5:
        raise ValueError("not an odd phase-5 first-hit row")
    k = (depth-5)//12
    m = cost-19*k
    if m not in range(8, 15):
        raise ValueError("cost phase must lie in 8..14")
    if u >= Fraction(D)+Fraction(2**m,243)*TBOUND:
        raise ValueError("outside the strict selective numerator bound")
    if (u*243-ROOT*2**m) % D:
        raise ValueError("incompatible inverse-word numerator residue")
    x0 = Fraction(2**m,243)*(3*V0+Fraction(ROOT,D))-Fraction(u,D)
    if x0.denominator != 1:
        raise ValueError("boundary intercept must be integral")
    return dict(u=u, depth=depth, cost=cost, k=k, m=m, x0=int(x0),
                period=2**(m+18)*3**14, score=_pair(Fraction(2**m,243)))


def comparison_interval(p0, period, strict=False):
    """Exact ell>=0 with 0<p0+period*ell <= Q(ell), or <Q if strict."""
    if type(p0) is not int or type(period) is not int or period <= 0:
        raise ValueError("an integral intercept and positive period are required")
    if type(strict) is not bool:
        raise ValueError("strict must be Boolean")
    low = max(0, (-p0)//period+1)
    high = None
    delta0, delta1 = p0-Q0, period-QP
    cap = -1 if strict else 0
    if delta1 > 0:
        high = (cap-delta0)//delta1
    elif delta1 < 0:
        low = max(low, (delta0-cap+(-delta1)-1)//(-delta1))
    elif delta0 > cap:
        return None
    if high is not None and low > high:
        return None
    return [low, high]


def first_guarded(interval, returns):
    residue, modulus = guard(returns)
    if interval is None:
        return None
    if (not isinstance(interval, (list, tuple)) or len(interval) != 2
            or type(interval[0]) is not int or interval[0] < 0
            or (interval[1] is not None and
                (type(interval[1]) is not int or interval[1] < interval[0]))):
        raise ValueError("expected an integral nonnegative interval")
    low, high = interval
    ell = residue+max(0,(low-residue+modulus-1)//modulus)*modulus
    return ell if high is None or ell <= high else None


def _terminal(data, x0, period, depth, cost, word):
    nonstrict = comparison_interval(x0, period)
    strict = comparison_interval(x0, period, True)
    return dict(
        depth=depth, cost=cost, p0=x0, period=period,
        score=_pair(Fraction(2**(data['m']+cost),3**(depth+5))),
        slope_ratio=_pair(Fraction(period,QP)),
        nonstrict_interval=nonstrict, strict_interval=strict,
        first_guarded=first_guarded(nonstrict,data['k']),
        strict_first_guarded=first_guarded(strict,data['k']),
        word=[list(symbol) for symbol in word],
        relation='Q' if (x0,period)==(Q0,QP) else
                 '(9Q+5)/8' if (8*x0,8*period)==(9*Q0+5,9*QP) else 'other',
    )


def _sort_rows(rows):
    return sorted(rows,key=lambda row:(row['depth'],row['cost'],row['p0'],
                                      row['period'],row['word']))


def pruned_suffixes(hit):
    """All necessary terminal suffixes, pruning only proved cost bounds.

    Legal complete inverse branches have form (2^e*x+b)/3. The optimistic
    lower slope after all remaining point steps is used only to discard a
    subtree that cannot have total normalized score below1/2 by depth14.
    """
    data = boundary(hit)
    m = data['m']
    stack = [(data['x0'],data['period'],0,0,())]
    nodes = pruned = 0
    terminal_rows = []
    while stack:
        x0, period, depth, cost, word = stack.pop()
        nodes += 1
        if 2**(m+cost+15-depth) >= 3**19:
            pruned += 1
            continue
        if depth and 2**(m+cost+1) < 3**(depth+5):
            terminal_rows.append(_terminal(data,x0,period,depth,cost,word))
        if depth == 14:
            continue
        assert period % 3 == 0
        for kind, base_cost, base_b in BASES[x0 % 3]:
            max_index = 0 if kind == 'point' else (21-cost-base_cost)//6
            for index in range(max_index+1):
                step_cost = base_cost+6*index
                if cost+step_cost > 21:
                    continue
                scale = 64**index
                b = scale*base_b+7*(scale-1)//3
                numerator = 2**step_cost*x0+b
                assert numerator % 3 == 0
                stack.append((numerator//3,period*2**step_cost//3,
                              depth+1,cost+step_cost,
                              word+((kind,index,step_cost,b),)))
    terminal_rows = _sort_rows(terminal_rows)
    return dict(boundary=data,nodes=nodes,pruned=pruned,
                terminal_rows=terminal_rows,
                successes=[row for row in terminal_rows if row['first_guarded'] is not None])


def unpruned_suffixes(hit):
    """Independent ray-iteration enumeration with only depth14/cost21 caps.

    No optimistic completion test or score test prunes this search. Every
    generated state is compared with Q, including ones whose score fails.
    Rays are generated by actual affine recurrence y->64y+49.
    """
    data = boundary(hit)
    queue = [(data['x0'],data['period'],0,0,())]
    nodes = 0
    terminal_rows, all_successes = [], []
    while queue:
        x0, period, depth, cost, word = queue.pop()
        nodes += 1
        if depth:
            row = _terminal(data,x0,period,depth,cost,word)
            if row['first_guarded'] is not None:
                all_successes.append(row)
            if Fraction(2**(data['m']+cost),3**(depth+5)) < Fraction(1,2):
                terminal_rows.append(row)
        if depth == 14:
            continue
        assert period % 3 == 0
        for kind, base_cost, base_b in BASES[x0 % 3]:
            numerator = 2**base_cost*x0+base_b
            assert numerator % 3 == 0
            y0, yp = numerator//3, period*2**base_cost//3
            step_cost, index, b = base_cost, 0, base_b
            while cost+step_cost <= 21:
                queue.append((y0,yp,depth+1,cost+step_cost,
                              word+((kind,index,step_cost,b),)))
                if kind == 'point':
                    break
                y0, yp = 64*y0+49, 64*yp
                b = 64*b+147
                step_cost += 6
                index += 1
    return dict(boundary=data,nodes=nodes,terminal_rows=_sort_rows(terminal_rows),
                successes=_sort_rows(all_successes))


def enumerate_suffixes(hit):
    """Default complete cost/depth enumeration, without optimistic pruning."""
    return unpruned_suffixes(hit)
