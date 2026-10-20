"""Exact four-target history cell; no absorption or terminal-current search.

See HISTORY_CELL_SCOPE.md. All public constructors reject invalid domains.
Only standard-library arithmetic is used; currents kill row/state 1.
"""

from collections import Counter, deque
from fractions import Fraction

Q0, QP = 133704987, 3 * 2**33
N0, NP = 385940463, 64 * 3**19
WORD = (1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 2)
BASES = {
    0: {"ray0": (8, 3), "ray1": (16, 3)},
    1: {"ray0": (4, -1), "ray1": (32, 19)},
    2: {"point": (2, -1), "ray0": (64, 19), "ray1": (128, 83)},
}


def integer(value, name, minimum=0):
    if type(value) is not int or value < minimum:
        raise ValueError(f"{name} must be an integer >= {minimum}")
    return value


def odd(value):
    integer(value, "state", 1)
    if value % 2 != 1:
        raise ValueError("state must be odd")
    return value


def v2(value):
    integer(value, "valuation argument", 1)
    return (value & -value).bit_length() - 1


def S(x):
    odd(x)
    return 1 if x == 1 else (3 * x + 1) >> v2(3 * x + 1)


def selected(x):
    odd(x)
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    odd(x)
    while x % 8 == 5:
        x = (x - 1) // 4
    return (x - 1) // 2 if selected(x) else x


def T(x):
    odd(x)
    if nu(x) != x:
        raise ValueError("quotient source must be canonical")
    return nu(S(x))


def parameters(m, a=0):
    integer(m, "cell parameter")
    integer(a, "future index")
    if a > 3:
        raise ValueError("future index must be at most 3")
    Q, n = Q0 + QP * m, N0 + NP * m
    y = 3**a * (n + 1) // 2**a - 1
    return {"m": m, "a": a, "Q": Q, "b": Q // 3, "n": n,
            "v": n // 3, "raw": 2 * n + 1, "target": y,
            "anchor": 3**a * (N0 + 1) // 2**a - 1,
            "period": NP * 3**a // 2**a, "horizon": 19 + a}


def combine(*terms):
    out = Counter()
    for factor, current in terms:
        for x, coefficient in current.items():
            if x != 1:
                out[x] += factor * coefficient
    return {x: c for x, c in sorted(out.items()) if c}


def prefix(x, length):
    odd(x)
    integer(length, "prefix length")
    states, current = [x], Counter()
    for _ in range(length):
        if x != 1:
            current[x] += 1
        x = S(x)
        states.append(x)
    return {"states": states, "current": dict(sorted(current.items())), "end": x}


def divergence(current):
    out = Counter()
    for x, coefficient in current.items():
        odd(x)
        if type(coefficient) is not int:
            raise ValueError("current coefficients must be integers")
        if x != 1:
            out[x] += coefficient
            if S(x) != 1:
                out[S(x)] -= coefficient
    return {x: c for x, c in sorted(out.items()) if c}


def comparison(m):
    """The existing Q-to-n current, with full 23/5 ordinary prefixes."""
    p = parameters(m)
    upper = prefix(p["Q"], 23)
    lower = prefix(p["n"], 5)
    first = prefix(p["Q"], 18)
    raw = prefix(p["raw"], 5)
    assert first["end"] == p["raw"]
    assert upper["end"] == lower["end"] == raw["end"]
    current = combine((1, upper["current"]), (-1, lower["current"]))
    normalizer = combine((1, raw["current"]), (-1, lower["current"]))
    assert current == combine((1, first["current"]), (1, normalizer))
    assert divergence(current) == {p["Q"]: 1, p["n"]: -1}
    quotient = [p["Q"]]
    for _ in range(18):
        quotient.append(T(quotient[-1]))
    assert quotient[-1] == p["n"]
    return {"parameters": p, "quotient_states": quotient,
            "upper_states": upper["states"], "lower_states": lower["states"],
            "ordinary_clocks": [23, 5], "quotient_clock": 18,
            "normalizer": normalizer, "current": current}


def affine_successor(base, period):
    """Exact ordinary step on every base+period*m, m>=0."""
    odd(base)
    integer(period, "period", 1)
    a = v2(3 * base + 1)
    if 3 * period % 2**(a + 1):
        raise ValueError("cell does not fix the exact valuation bit")
    return (3 * base + 1) // 2**a, 3 * period // 2**a, a


def affine_normal(base, period):
    """Normalize a whole affine cell, rejecting unfixed binary decisions."""
    odd(base)
    integer(period, "period", 1)
    while True:
        if period % 8:
            raise ValueError("cell does not fix the F-root residue")
        if base % 8 != 5:
            break
        base, period = (base - 1) // 4, period // 4
    if base % 4 == 3:
        a = v2(base + 1)
        if period % 2**(a + 2):
            raise ValueError("cell does not fix the selected/complementary bit")
        if selected(base):
            base, period = (base - 1) // 2, period // 2
    return base, period


def affine_paths():
    """Finite exact phase checks certify the two paths for every m."""
    raw = [[Q0, QP]]
    valuations = []
    for _ in WORD:
        x, p, a = affine_successor(*raw[-1])
        raw.append([x, p])
        valuations.append(a)
    assert tuple(valuations) == WORD
    assert raw[-1] == [2 * N0 + 1, 2 * NP]
    quotient = [[Q0, QP]]
    for _ in range(18):
        x, p, _ = affine_successor(*quotient[-1])
        quotient.append(list(affine_normal(x, p)))
    assert quotient[-1] == [N0, NP]
    assert affine_normal(2 * N0 + 1, 2 * NP) == (N0, NP)
    return {"ordinary_word": valuations, "ordinary_states": raw,
            "quotient_states": quotient, "valuation_sum": sum(valuations)}


def inverse_step(x, kind, index=0):
    odd(x)
    integer(index, "ray index")
    if nu(x) != x or x == 1:
        raise ValueError("inverse target must be canonical and greater than 1")
    if kind not in BASES[x % 3] or (kind == "point" and index):
        raise ValueError("illegal inverse branch")
    A, B = BASES[x % 3][kind]
    p = (A * x + B) // 3
    if kind != "point":
        scale = 64**index
        p = scale * p + 49 * (scale - 1) // 63
    assert T(p) == x
    return p


def replay_word(target, word):
    x = odd(target)
    for kind, index in word:
        x = inverse_step(x, kind, index)
    return x


def anchor_tree(a, max_nodes=100000):
    """All inverse words through the horizon with possible origin <=Q0.

    The analytic forward bound truncates each infinite ray. A resource cap
    raises; it is never interpreted as complete enumeration.
    """
    p = parameters(0, a)
    integer(max_nodes, "node cap", 1)
    pending = deque([(p["anchor"], p["period"], [])])
    nodes, hits = [], []
    while pending:
        if len(nodes) >= max_nodes:
            raise RuntimeError("incomplete inverse enumeration: node cap reached")
        x, period, word = pending.popleft()
        depth = len(word)
        assert nu(x) == x and x > 1
        row = {"x": x, "period": period, "depth": depth,
               "word": word, "first_excluded": []}
        if x <= Q0:
            hits.append({"origin": x, "period": period, "depth": depth, "word": word})
        if depth < p["horizon"]:
            remaining = p["horizon"] - depth - 1
            bound = (Q0 + 1) * 3**remaining // 2**remaining - 1
            for kind, (A, B) in BASES[x % 3].items():
                assert (A * x + B) % 3 == 0 and A * period % 3 == 0
                child, child_period = (A * x + B) // 3, A * period // 3
                index = 0
                while child <= bound:
                    assert T(child) == x
                    pending.append((child, child_period, word + [[kind, index]]))
                    if kind == "point":
                        break
                    child, child_period = 64 * child + 49, 64 * child_period
                    index += 1
                if child > bound:
                    row["first_excluded"].append([kind, index, child, bound])
        nodes.append(row)
    nodes.sort(key=lambda row: (row["depth"], row["x"], row["word"]))
    hits.sort(key=lambda row: (row["depth"], row["origin"], row["word"]))
    return {"a": a, "horizon": p["horizon"], "anchor": p["anchor"],
            "period": p["period"], "states": len(nodes), "nodes": nodes, "hits": hits}


def cutoff(m):
    p = parameters(m)
    return Fraction((p["Q"] + 1) * (N0 + 1), p["n"] + 1)


def query(m, a=0, max_nodes=100000):
    """Return every canonical origin <=Q in the proved finite horizon."""
    p = parameters(m, a)
    tree = anchor_tree(a, max_nodes)
    limit = Fraction(QP * (N0 + 1), NP)
    assert Q0 + 1 <= cutoff(m) < limit < Q0 + 3
    out = []
    for hit in tree["hits"]:
        origin = replay_word(p["target"], hit["word"])
        if origin <= p["Q"]:
            out.append({"origin": origin, "depth": hit["depth"], "word": hit["word"]})
    return {"parameters": p, "complete": True, "origins": out}
