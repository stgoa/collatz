"""Exact retained lower history and its first rational-shadow departure.

The outputs are comparison currents with an explicit two-atom residual.
They are not completed tripling-pair currents or absorption certificates.
Only Python's standard library is required.
"""

from collections import Counter

D = 7153
A = 3**12
M = 2**19
Q0 = 70506316836123
QP = 3 * 2**45
V0 = 67839005952677
VP = 2**18 * 3**18
Z0 = 471104208005
ZP = 2**14 * 3**16
UPPER_WORD = (1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 2)
LOWER_WORD = (2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 3, 2, 1, 5, 2, 3)
RETURN_WORD = (1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2)


def integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def v2(value):
    if type(value) is not int or value == 0:
        raise ValueError("valuation requires a nonzero integer")
    value = abs(value)
    return (value & -value).bit_length() - 1


def syracuse(value):
    integer(value, "source", 1)
    if value % 2 == 0:
        raise ValueError("source must be odd")
    if value == 1:
        return 1
    numerator = 3 * value + 1
    return numerator >> v2(numerator)


def clean(table):
    return {int(x): int(c) for x, c in sorted(table.items()) if c}


def combine(*terms):
    out = Counter()
    for multiplier, table in terms:
        for state, coefficient in table.items():
            out[state] += multiplier * coefficient
    return clean(out)


def divergence(current):
    out = Counter()
    for source, coefficient in current.items():
        out[source] += coefficient
        out[syracuse(source)] -= coefficient
    return clean(out)


def path(source, steps, max_steps=10000):
    integer(steps, "steps")
    integer(max_steps, "max_steps")
    if steps > max_steps:
        raise ValueError("explicit path cap exceeded; no result returned")
    integer(source, "source", 1)
    if source % 2 == 0:
        raise ValueError("source must be odd")
    states = [source]
    word = []
    current = Counter()
    for _ in range(steps):
        if source == 1:
            word.append(2)
            states.append(1)
            continue
        current[source] += 1
        word.append(v2(3 * source + 1))
        source = syracuse(source)
        states.append(source)
    return {"states": states, "word": word, "current": clean(current)}


def parameters(ell):
    integer(ell, "ell")
    q = Q0 + QP * ell
    v = V0 + VP * ell
    z = Z0 + ZP * ell
    assert v == 144 * z - 43
    assert q * 3**15 == 2**31 * z - 665034679
    n = v2(D * z - 53)
    assert n >= 14
    return {"ell": ell, "Q": q, "b": q // 3, "v": v, "z": z,
            "order": n, "returns": (n - 14) // 19,
            "upper_exit_order": 18 + (n - 14) % 19}


def psi(z):
    integer(z, "z", 1)
    if z % 2 == 0 or v2(D * z - 53) < 33:
        raise ValueError("one complete guarded return requires order >= 33")
    result, remainder = divmod(A * z - 53, M)
    assert remainder == 0 and result % 2 == 1 and result > z
    assert v2(D * result - 53) == v2(D * z - 53) - 19
    return result


def upper(z):
    return 864 * z - 257


def shadow_certificate():
    """Compute the complete positive rational orbit from 53/D."""
    seen = {}
    numerators = []
    word = []
    costs = [0]
    numerator = 53
    while numerator not in seen:
        if len(numerators) >= 1024:
            raise RuntimeError("rational certificate cap exceeded")
        seen[numerator] = len(numerators)
        numerators.append(numerator)
        raw = 3 * numerator + D
        exponent = v2(raw)
        word.append(exponent)
        costs.append(costs[-1] + exponent)
        numerator = raw >> exponent
    start = seen[numerator]
    return {"denominator": D, "numerators": numerators,
            "word": word, "costs": costs, "cycle_start": start,
            "cycle_length": len(numerators) - start,
            "cycle_cost": costs[-1] - costs[start],
            "maximum_numerator": max(numerators)}


def shadow_prefix(order, max_steps=10000):
    """The maximal exact shadow prefix: cumulative valuation cost < order."""
    integer(order, "order", 1)
    integer(max_steps, "max_steps")
    cert = shadow_certificate()
    numerator = 53
    cost = 0
    word = []
    while True:
        raw = 3 * numerator + D
        exponent = v2(raw)
        if cost + exponent >= order:
            return {"steps": len(word), "cost": cost, "word": word,
                    "numerator": numerator, "next_exponent": exponent,
                    "next_numerator": raw >> exponent,
                    "gap": order - cost,
                    "mode": "short" if cost + exponent > order else "long"}
        if len(word) >= max_steps:
            raise ValueError("explicit shadow-prefix cap exceeded; no result returned")
        word.append(exponent)
        cost += exponent
        numerator = raw >> exponent


def first_departure(z, max_steps=10000):
    integer(z, "z", 1)
    if z % 2 == 0 or D * z <= 53:
        raise ValueError("positive odd z above the rational centre is required")
    order = v2(D * z - 53)
    spec = shadow_prefix(order, max_steps)
    unit = (D * z - 53) >> order
    i, cost = spec["steps"], spec["cost"]
    raw = 3**i * 2**(order - cost) * unit + spec["numerator"]
    state, remainder = divmod(raw, D)
    assert remainder == 0 and state % 2 == 1
    actual_exponent = v2(3 * state + 1)
    if spec["mode"] == "short":
        assert actual_exponent == spec["gap"] < spec["next_exponent"]
        extra = None
    else:
        extra = v2(3**(i + 1) * unit + spec["next_numerator"])
        assert extra >= 1 and actual_exponent == spec["next_exponent"] + extra
    return {**spec, "order": order, "unit": unit, "state": state,
            "actual_exponent": actual_exponent, "extra": extra,
            "endpoint": syracuse(state)}


def family(order, extra=None, offset=0, max_steps=10000):
    """Realize every exact lower-order/departure row in the original cell.

    In a long row extra>=1 fixes the complete next valuation. In a short
    row it must be omitted, because the next valuation is already forced.
    """
    integer(order, "order", 14)
    integer(offset, "offset")
    spec = shadow_prefix(order, max_steps)
    if spec["mode"] == "short":
        if extra is not None:
            raise ValueError("short departure has no free extra valuation")
        precision = order + 1
        unit_residue = 1
    else:
        integer(extra, "extra", 1)
        precision = order + extra + 1
        modulus = 1 << (extra + 1)
        unit_residue = ((1 << extra) - spec["next_numerator"]) * pow(
            3**(spec["steps"] + 1), -1, modulus) % modulus
        assert unit_residue % 2 == 1
    modulus = 1 << precision
    z_residue = (53 + (1 << order) * unit_residue) * pow(D, -1, modulus) % modulus
    assert (z_residue - Z0) % (1 << 14) == 0
    ell_modulus = 1 << (precision - 14)
    ell_residue = ((z_residue - Z0) // (1 << 14)) * pow(3**16, -1, ell_modulus) % ell_modulus
    ell = ell_residue + ell_modulus * offset
    result = parameters(ell)
    departure = first_departure(result["z"], max_steps)
    assert departure["order"] == order
    assert spec["mode"] == "short" or departure["extra"] == extra
    return {**result, "ell_residue": ell_residue, "ell_modulus": ell_modulus,
            "precision": precision, "departure": departure}


def initial_identity(ell):
    data = parameters(ell)
    up = path(data["Q"], 18)
    low = path(data["b"], 16)
    assert tuple(up["word"]) == UPPER_WORD
    assert tuple(low["word"]) == LOWER_WORD
    assert up["states"][-1] == upper(data["z"])
    assert low["states"][-1] == data["z"]
    current = combine((1, up["current"]), (-1, low["current"]))
    residual = clean(Counter({upper(data["z"]): 1, data["z"]: -1}))
    assert combine((1, divergence(current)), (1, residual)) == {data["b"]: -1, data["Q"]: 1}
    return {**data, "current": current, "residual": residual,
            "ordinary_clocks": [18, 16]}


def paired_history(ell, returns=None, lower_after=1, max_steps=10000):
    """Advance the upper guard and the actual lower first-departure history.

    lower_after counts arrows from the last matching lower state, including
    its departing arrow. Values 0..12 have the proved original-Q bound.
    Every returned source coefficient remains explicit.
    """
    data = parameters(ell)
    if returns is None:
        returns = data["returns"]
    integer(returns, "returns")
    if returns > data["returns"]:
        raise ValueError("requested upper returns exceed the exact guard")
    integer(lower_after, "lower_after")
    if lower_after > 12:
        raise ValueError("the proved lower continuation window is 0..12")
    spec = first_departure(data["z"], max_steps)
    zr = data["z"]
    for _ in range(returns):
        zr = psi(zr)
    up = path(data["Q"], 18 + 12 * returns, max_steps)
    low = path(data["b"], 16 + spec["steps"] + lower_after, max_steps)
    assert up["states"][-1] == upper(zr)
    assert tuple(low["word"][:16]) == LOWER_WORD
    assert low["word"][16:16 + spec["steps"]] == spec["word"]
    assert low["states"][-1] < data["Q"] < up["states"][-1]
    current = combine((1, up["current"]), (-1, low["current"]))
    residual = clean(Counter({up["states"][-1]: 1, low["states"][-1]: -1}))
    assert combine((1, divergence(current)), (1, residual)) == {data["b"]: -1, data["Q"]: 1}
    return {**data, "used_returns": returns, "lower_departure": spec,
            "ordinary_clocks": [len(up["word"]), len(low["word"])],
            "upper_endpoint": up["states"][-1], "lower_endpoint": low["states"][-1],
            "current": current, "residual": residual}
