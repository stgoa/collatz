"""Complete decreasing canonical inverse chains and their R26 application.

Every construction is finite arithmetic or follows a supplied finite graph.
The rule is partial and its certified targets lie inside R29 saturation.
"""
from fractions import Fraction as F
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("ancestry_run", HERE.parent / "complementary_bridge/run_bridge.py")
RUN = module_from_spec(spec)
spec.loader.exec_module(RUN)
NORMAL = RUN.NORMAL
step, combine, divergence = RUN.step, RUN.combine, RUN.divergence


def valuation3(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Expected a positive integer")
    exponent = 0
    while n % 3 == 0:
        n //= 3
        exponent += 1
    return exponent


def ancestry(q):
    """The unique minimum reached by strictly decreasing canonical inverses."""
    if not NORMAL.canonical(q):
        raise ValueError("Supply a canonical target")
    h = valuation3(q+1)
    p = 2**h*((q+1)//3**h)-1
    assert NORMAL.canonical(p) and (p+1) % 3
    descending, y = [q], q
    for _ in range(h):
        y = (2*y-1)//3
        assert NORMAL.canonical(y) and step(y) == descending[-1]
        assert y < descending[-1]
        descending.append(y)
    assert y == p
    current = {x: -1 for x in descending[1:] if x != 1}
    assert divergence(current) == combine((1, {q: 1}), (-1, {p: 1}))
    return dict(target=q, minimum=p, depth=h, descending=descending, current=current)


def canonical_class(p):
    """The whole finite canonical valuation-one component with minimum p."""
    if not NORMAL.canonical(p) or (p+1) % 3 == 0:
        raise ValueError("Supply a canonical inverse minimum")
    length = NORMAL.valuation2(p+1)
    states = [3**j*((p+1)//2**j)-1 for j in range(length)]
    assert states[-1] % 8 == 1
    assert all(NORMAL.canonical(x) and ancestry(x)["minimum"] == p for x in states)
    return states


def target(x):
    return ancestry(RUN.normal_target(x))["minimum"]


def bridge(x):
    run = RUN.normalized_bridge(x)
    inverse = ancestry(run["target"])
    current = combine((1, run["current"]), (1, inverse["current"]))
    assert divergence(current) == combine((1, {x: 1}), (-1, {inverse['minimum']: 1}))
    return dict(root=x, target=inverse["minimum"], old_target=run["target"],
                ancestry=inverse, run=run, current=current)


def selected_profile(N):
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError("Require 8|N and N>=8")
    remainder = RUN.H.COMPLEMENT.residual_profile(N)[2]
    return {x: c for x, c in remainder.items()
            if not RUN.H.selected(x) and target(x) < N}


def certify(N, lower_current):
    """Certify the entire selected profile from a supplied exact U_N current."""
    if divergence(lower_current) != RUN.H.LOCAL.count(N):
        raise ValueError("Supply an exact U_N current")
    selected = selected_profile(N)
    lower_edges = {x: step(x) for x, c in lower_current.items() if c}
    targets, arithmetic, explicit = {}, {}, set()
    for x, c in selected.items():
        data = bridge(x)
        p = data["target"]
        if p != 1:
            targets[p] = targets.get(p, 0)+c
        arithmetic = combine((1, arithmetic), (c, data["current"]))
        explicit.update(data["current"])
    known = RUN.H.COMPLEMENT.extract_exact(targets, lower_edges)
    signed = combine((1, arithmetic), (1, known))
    assert divergence(signed) == selected
    current = RUN.H.COMPLEMENT.extract_exact(selected, {x: step(x) for x in signed})
    assert set(current) <= set(lower_edges) | explicit
    preceding = {x: c for x, c in RUN.H.COMPLEMENT.residual_profile(N)[2].items()
                 if not RUN.H.selected(x)}
    remaining = combine((1, preceding), (-1, selected))
    return dict(N=N, selected=selected, remaining=remaining, current=current,
                target_source=targets, explicit_rows=sorted(explicit))


def certify_single(x, lower_current, weight=1):
    if not isinstance(weight, int) or weight < 1:
        raise ValueError("Require a positive integer weight")
    data = bridge(x)
    if divergence(lower_current) != ({} if data['target'] == 1 else {data['target']: 1}):
        raise ValueError("Supply an exact current for the identified lower seed")
    signed = combine((weight, data['current']), (weight, lower_current))
    assert divergence(signed) == {x: weight}
    current = RUN.H.COMPLEMENT.extract_exact({x: weight}, {y: step(y) for y in signed})
    return dict(data=data, signed_current=signed, current=current)


def _count(lo, hi, residue, modulus, exclude_one_mod_eight=False):
    if hi <= lo:
        return 0
    answer = NORMAL.canonical_count(hi, residue, modulus)-NORMAL.canonical_count(lo, residue, modulus)
    if exclude_one_mod_eight:
        first = (1+8*((residue-1)*pow(8, -1, modulus) % modulus)) % (8*modulus)
        answer -= max(0, (hi-first)//(8*modulus)+1)-max(0, (lo-first)//(8*modulus)+1)
    return answer


def _intersection(residue, modulus, h):
    power = 3**h
    common = gcd(modulus, power)
    if (residue+1) % common:
        return None
    # Both moduli are powers of three in the actual source formula.
    if modulus >= power:
        assert modulus % power == 0
        return residue, modulus
    assert power % modulus == 0
    return power-1, power


def cell_count(N, a, d):
    """Exact weighted CRT count of the extended rule on one R26 run cell."""
    x0, period = RUN.cylinder(a, d)
    f0 = RUN.target(x0)
    g = 2 if d % 2 else 4
    A = 3**(a-1+d//2)
    advance = g*A
    tmax = (3*N//2)//2**a
    fmax = ((1 if d % 2 else 2)*3**(d//2)*(3**(a-1)*tmax-1))//2**d+(0 if d % 2 else 1)
    if fmax < 1:
        return 0
    hmax, power = 0, 3
    while power <= fmax+1:
        hmax += 1
        power *= 3
    kmax = (fmax.bit_length()+1)//2 if d % 2 else 0
    intervals = ((1, F(N), F(3*N, 2), 3, 12),
                 (1, F(9*N, 8), F(3*N, 2), 7, 12),
                 (2, F(N), F(9*N, 8), 7, 36),
                 (2, F(N), F(9*N, 8), 19, 36))
    answer = 0
    for k in range(kmax+1):
        for partner in (False, True):
            scale = 4**k*(2 if partner else 1)
            offset = (4**(k+1)-1)//3 if partner else (4**k-1)//3
            for weight, low, high, r, m in intervals:
                qlow = (F(advance, period)*(low-x0)+f0-offset)/scale
                qhigh = (F(advance, period)*(high-x0)+f0-offset)/scale
                odd = A*(m//4)
                residue = ((A*(r-x0)-(period//g)*(offset-f0))
                           *pow((period//g)*scale, -1, odd)) % odd
                fixed = valuation3(residue+1)
                depth = valuation3(odd)
                options = [fixed] if fixed < depth else range(depth, hmax+1)
                for h in options:
                    upper = min(qhigh, F(3**h, 2**h)*(N+1)-1)
                    if upper <= qlow:
                        continue
                    lo = max(0, qlow.numerator//qlow.denominator)
                    hi = max(0, -((-upper.numerator)//upper.denominator)-1)
                    value = 0
                    for sign, exponent in ((1, h), (-1, h+1)):
                        congruence = _intersection(residue, odd, exponent)
                        if congruence is not None:
                            value += sign*_count(lo, hi, *congruence,
                                                 exclude_one_mod_eight=not d % 2 and not partner)
                    answer += weight*value
    return answer


def mass_formula(N):
    if not isinstance(N, int) or N < 8 or N % 8:
        raise ValueError("Require 8|N and N>=8")
    maximum_a = (3*N//2).bit_length()-1
    answer = 0
    for a in range(2, maximum_a+1):
        tmax = (3*N//2)//2**a
        dmax = (3**(a-1)*tmax-1).bit_length()-1
        for d in range(2, dmax+1):
            answer += cell_count(N, a, d)
    return answer


def large_return_family(h):
    """A complete binary family with inverse depth h and lower target <2x/3."""
    if not isinstance(h, int) or h < 2:
        raise ValueError("Require h>=2")
    k, b, d = (3**h-1)//2, h+1, 2*h+3
    M = h+2+3**h
    low, high = 2, 2*M
    while low+1 < high:
        middle = (low+high)//2
        if 3**(middle+1) < 2**(middle+M+1):
            low = middle
        else:
            high = middle
    a = low
    slope = F(3**a, 2**(a+M))
    assert F(4, 9) <= slope < F(2, 3)
    bits_t = d+2*k+3
    modulus_t = 2**bits_t
    residue_t = ((3**(b+1)+2**d*(4**(k+1)-1))
                 *pow(3**(a+b), -1, modulus_t)) % modulus_t
    residue, modulus = 2**a*residue_t-1, 2**(a+bits_t)
    correction = F(1, 3)-F(3**(h+1), 2**d)
    intercept = slope+F(2, 3)**h*(F(2, 3)+correction/4**k)-1
    assert -F(5, 9) < intercept < -F(7, 192)
    return dict(h=h, a=a, b=b, d=d, k=k, residue=residue, modulus=modulus,
                slope=slope, intercept=intercept)


def source_count(N, residue, modulus):
    """Exact full-weight actual R_N mass in one binary 3-mod4 cylinder."""
    if N < 8 or N % 8 or modulus < 4 or modulus & (modulus-1) or residue % 4 != 3:
        raise ValueError("Require an allowed cutoff and binary 3-mod4 cylinder")
    answer = 0
    for weight, low, high, r, odd in ((1,F(N),F(3*N,2),3,3),
                                    (1,F(9*N,8),F(3*N,2),7,3),
                                    (2,F(N),F(9*N,8),7,9),
                                    (2,F(N),F(9*N,8),19,9)):
        combined = (residue+modulus*((r-residue)*pow(modulus,-1,odd) % odd)) % (modulus*odd)
        answer += weight*RUN.H.COMPLEMENT.strict_count(low, high, combined, modulus*odd)
    assert abs(F(answer)-F(25*N,72*modulus)) <= 6
    return answer


def ray_witness(h, weight=1):
    data = large_return_family(h)
    modulus, residue = data['modulus'], data['residue']
    if weight not in (1, 2):
        raise ValueError("Require weight1 or2")
    N = 12*modulus*(8 if weight == 2 else 1)
    odd = 9 if weight == 2 else 3
    row = 7 if weight == 2 else 3
    combined = (residue+modulus*((row-residue)*pow(modulus,-1,odd) % odd)) % (modulus*odd)
    x = combined+modulus*odd*((N-combined)//(modulus*odd)+1)
    assert N < x < (F(9*N,8) if weight == 2 else F(3*N,2))
    assert RUN.H.TRANSFER.residual_coefficient(N,x) == weight
    return dict(N=N, root=x, weight=weight, family=data)
