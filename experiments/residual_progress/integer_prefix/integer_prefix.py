"""Exact integer cylinders for arbitrary mixed V/R return prefixes.

The two returns are conditional growing current comparisons.  Every helper
is retained.  Finite prefix realization is not infinite positive survival.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('integer_prefix_exit', HERE.parent/'mixed_exit/mixed_exit.py')
X = module_from_spec(spec)
spec.loader.exec_module(X)
M, NORMAL, RANK = X.M, X.NORMAL, X.RANK
combine, divergence, rho = X.combine, X.divergence, X.rho
BASE_BITS, BASE = 26, M.RESIDUE
BRANCHES = {'V': (M.A, M.B, 19, 12, 1),
            'R': (X.P, X.C, 37, 24, 6)}
V_RESIDUE = 2218391138229
CONDITIONAL_DENSITY = Fraction(1, 2**19) + Fraction(1, 2**37)


def checked_word(word, max_symbols=256):
    if not isinstance(word, str) or not word or any(c not in BRANCHES for c in word):
        raise ValueError('Require a nonempty string over V and R')
    if not isinstance(max_symbols, int) or max_symbols < 1 or len(word) > max_symbols:
        raise ValueError('The finite word exceeds the explicit symbol cap')
    return word


def affine(word, max_symbols=256):
    """Composition in chronological order: output=(a*w+c)/2**e."""
    checked_word(word, max_symbols)
    a, c, e, length = 1, 0, 0, 0
    for symbol in word:
        aa, cc, ee, steps, _ = BRANCHES[symbol]
        a, c, e = aa*a, aa*c+cc*2**e, e+ee
        length += steps
    assert a == 3**length and a > 2**e and c > 0 and c % 2
    return dict(word=word, multiplier=a, offset=c, exponent=e,
                quotient_length=length,
                ordinary_common_tail_clocks=[length+BRANCHES[word[-1]][4],
                                             BRANCHES[word[-1]][4]])


def cylinder(word, max_symbols=256):
    data = affine(word, max_symbols)
    bits = BASE_BITS+data['exponent']
    period = 2**bits
    residue = (2**data['exponent']*BASE-data['offset'])*pow(data['multiplier'], -1, period)%period
    assert residue > 0 and residue%2**BASE_BITS == BASE
    return dict(**data, bits=bits, period=period, residue=residue)


def base_eligible(seed):
    return isinstance(seed, int) and seed > 0 and seed % 2**BASE_BITS == BASE


def branch(seed):
    """The deterministic return symbol, or None when this subsystem exits."""
    if not base_eligible(seed):
        return None
    if seed % 2**45 == V_RESIDUE:
        assert NORMAL.valuation2(M.DIFFERENCE*seed+M.B) >= 45
        return 'V'
    if X.eligible(seed):
        assert NORMAL.valuation2(M.DIFFERENCE*seed+M.B) == 37
        return 'R'
    return None


def step(seed, symbol):
    if symbol not in BRANCHES or branch(seed) != symbol:
        raise ValueError('The requested complete return guard fails')
    a, c, e, _, _ = BRANCHES[symbol]
    target, remainder = divmod(a*seed+c, 2**e)
    assert not remainder and target > seed and base_eligible(target)
    return target


def family(word, index=0, max_symbols=256):
    if not isinstance(index, int) or index < 0:
        raise ValueError('Require a nonnegative progression index')
    data = cylinder(word, max_symbols)
    seed = data['residue']+data['period']*index
    states = [seed]
    for symbol in word:
        states.append(step(states[-1], symbol))
    assert 2**data['exponent']*states[-1] == data['multiplier']*seed+data['offset']
    return dict(**data, index=index, seed=seed, states=states, leading=states[-1])


def odd_lift(word, modulus, residue, index=0, max_symbols=256):
    """Append any initial odd-modulus condition by exact CRT."""
    if not isinstance(modulus, int) or modulus < 1 or modulus % 2 == 0:
        raise ValueError('Require a positive odd modulus')
    if not isinstance(residue, int) or not isinstance(index, int) or index < 0:
        raise ValueError('Require an integer residue and nonnegative index')
    data = cylinder(word, max_symbols)
    first = (residue-data['residue'])*pow(data['period'], -1, modulus)%modulus
    out = family(word, first+modulus*index, max_symbols)
    assert out['seed'] % modulus == residue % modulus
    return dict(**out, odd_modulus=modulus, odd_residue=residue % modulus,
                combined_period=data['period']*modulus)


def maximal_counts(counts, index=0, max_symbols=256):
    if not isinstance(counts, (list, tuple)) or not counts:
        raise ValueError('Require a nonempty finite list of maximal counts')
    if any(not isinstance(m, int) or m < 1 for m in counts):
        raise ValueError('Every maximal old-guard count must be positive')
    word = ''.join('V'*(m-1)+'R' for m in counts)
    data = family(word, index, max_symbols)
    position = 0
    for m in counts:
        old = M.maximum(data['states'][position])
        assert old['count'] == m and old['exit_valuation'] == 18
        position += m
    return dict(**data, maximal_counts=list(counts))


def rational_point(prefix, cycle, max_symbols=256):
    """The unique eventually periodic 2-adic itinerary point is negative."""
    cyclic = affine(cycle, max_symbols)
    point = Fraction(-cyclic['offset'], cyclic['multiplier']-2**cyclic['exponent'])
    if prefix:
        before = affine(prefix, max_symbols)
        point = (2**before['exponent']*point-before['offset'])/before['multiplier']
    assert point < 0 and point.denominator % 2
    return point


def rational_congruent(value, residue, modulus):
    if value.denominator % 2 == 0 or modulus < 1 or modulus & (modulus-1):
        raise ValueError('Require an odd denominator and a binary modulus')
    return (value.numerator-residue*value.denominator) % modulus == 0


def comparison(seed, word, max_symbols=256):
    """All actual comparison rows; no absorption or trajectory completion."""
    data = cylinder(word, max_symbols)
    if not isinstance(seed, int) or seed <= 0 or seed % data['period'] != data['residue']:
        raise ValueError('The complete word cylinder fails')
    states, current = [seed], {}
    for symbol in word:
        w = states[-1]
        target = step(w, symbol)
        if symbol == 'V':
            endpoint, prefix, valuation_word = M.path_current(3*w, 12)
            assert tuple(valuation_word) == M.WORD and endpoint == NORMAL.F(3*target)
            local = combine((1, prefix), (1, NORMAL.bridge(endpoint)['current']))
        else:
            local = X.comparison(w)['current']
        current = combine((1, current), (1, local))
        states.append(target)
    assert divergence(current) == RANK.atoms((1, 3*seed), (-1, 3*states[-1]))
    return dict(**data, seed=seed, states=states, leading=states[-1], current=current)


def plan(seed, word, max_symbols=256):
    """Retain the entire signed prefix frontier and the larger leading pair."""
    data = comparison(seed, word, max_symbols)
    target = data['leading']
    upper, lower = RANK.absorption_plan(target), RANK.absorption_plan(seed)
    current = combine((1, data['current']), (1, upper['current']), (-1, lower['current']))
    coefficients = combine((1, {target: 1}), (1, upper['coefficients']), (-1, lower['coefficients']))
    assert coefficients[target] == 1
    assert all(rho(v) < 3*data['states'][-2] for v in coefficients if v != target)
    expected = RANK.T.pair_source(seed)
    for v, c in coefficients.items():
        expected = combine((1, expected), (-c, RANK.T.pair_source(v)))
    assert divergence(current) == expected
    return dict(**{k:v for k,v in data.items() if k != 'current'}, rank=3*seed,
                current=current, coefficients=coefficients, status='unresolved',
                high={v:c for v,c in coefficients.items() if rho(v) >= 3*seed})


def compile_plan(data, supplied):
    """Missing leading or helper currents remain mandatory premises."""
    return RANK.NINE.compile_five_plan(data, supplied)


def capped_trace(seed, max_symbols=256, max_bits=10000):
    """A cap is unresolved; exiting this subsystem is not Syracuse descent."""
    if not isinstance(max_symbols, int) or max_symbols < 0:
        raise ValueError('Require a nonnegative explicit symbol cap')
    if not isinstance(max_bits, int) or max_bits < 1:
        raise ValueError('Require a positive bit cap')
    if not isinstance(seed, int) or seed <= 0:
        raise ValueError('Require a positive integer input')
    states, symbols = [seed], []
    for _ in range(max_symbols):
        if states[-1].bit_length() > max_bits:
            return dict(status='unresolved_bit_cap', states=states, word=''.join(symbols))
        symbol = branch(states[-1])
        if symbol is None:
            return dict(status='exit', states=states, word=''.join(symbols))
        states.append(step(states[-1], symbol))
        symbols.append(symbol)
    return dict(status='unresolved_symbol_cap', states=states, word=''.join(symbols))
