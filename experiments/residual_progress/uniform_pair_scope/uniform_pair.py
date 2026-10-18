"""Exact search for the specified whole-guard, fixed-word affine pair model.

This standalone module uses the ordinary odd Syracuse map, with S(1)=1.
It writes no files.  It does not test variable valuation words or subdomains.
"""
from fractions import Fraction

RESIDUE = 40529845
PERIOD = 1 << 26


def valuation2(value):
    if type(value) is not int or value <= 0:
        raise ValueError('A positive integer is required')
    return (value & -value).bit_length() - 1


def validate_state(state):
    """A nonconstant progression of positive odd integers on all n>=0."""
    if not isinstance(state, (tuple, list)) or len(state) != 2:
        raise ValueError('An affine coefficient and intercept are required')
    a, b = state
    if type(a) is not int or type(b) is not int:
        raise ValueError('Affine coefficients must be integers')
    if a <= 0 or a % 2 or b <= 0 or b % 2 != 1:
        raise ValueError('Require positive even slope and positive odd intercept')
    return a, b


def fixed_path(state):
    """Return every prefix with a valuation word fixed for all n>=0."""
    states, word = [validate_state(state)], []
    while True:
        a, b = states[-1]
        h = valuation2(3*b + 1)
        if h >= valuation2(a):
            return states, word
        states.append((3*a // (1 << h), (3*b + 1) // (1 << h)))
        word.append(h)


def follow_fixed_word(state, word):
    """Reject a claimed word at its first wrong or nonuniform valuation."""
    a, b = validate_state(state)
    if not isinstance(word, (list, tuple)):
        raise ValueError('The valuation word must be a finite list or tuple')
    for h in word:
        if type(h) is not int or h < 1:
            raise ValueError('Valuations must be positive integers')
        if h != valuation2(3*b + 1) or h >= valuation2(a):
            raise ValueError('This valuation does not hold on the whole progression')
        a, b = 3*a // (1 << h), (3*b + 1) // (1 << h)
    return a, b


def eligible_nonconstant_partner(a, b):
    """Whole-domain W5, positivity and strict smaller-height conditions."""
    return (type(a) is int and type(b) is int and 0 < a <= PERIOD
            and a % 8 == 0 and 0 < b < RESIDUE and b % 8 == 5)


def inverse_valuation_limit(slope, remaining):
    """All h compatible with slope<=PERIOD after <=remaining further steps."""
    if type(slope) is not int or slope <= 0:
        raise ValueError('The current slope must be a positive integer')
    if type(remaining) is not int or remaining < 0:
        raise ValueError('The remaining depth must be a nonnegative integer')
    limit = 0
    while slope*(1 << (limit + 1 + remaining)) <= PERIOD*3**(remaining + 1):
        limit += 1
    return limit


def enumerate_lower_partners():
    """Exhaust all possible lower fixed-word mergers, without a guessed cap."""
    lower, lower_word = fixed_path((PERIOD, RESIDUE))
    candidates, visited = {}, 0
    for parent_clock, endpoint in enumerate(lower):
        assert endpoint[0] % 3**parent_clock == 0
        assert endpoint[0] % 3**(parent_clock + 1) != 0
        frontier = {endpoint: []}
        for depth in range(parent_clock + 1):
            if not frontier:
                break
            new = {}
            for (a, b), inverse_word in sorted(frontier.items()):
                visited += 1
                if eligible_nonconstant_partner(a, b):
                    candidates.setdefault((a, b), dict(
                        parent_clock=parent_clock, child_clock=depth,
                        inverse_word=inverse_word))
                if depth == parent_clock:
                    continue
                remaining = parent_clock - depth - 1
                for h in range(1, inverse_valuation_limit(a, remaining) + 1):
                    aa, bb = (1 << h)*a, (1 << h)*b - 1
                    if aa % 3 or bb % 3 or bb <= 0:
                        continue
                    new[(aa // 3, bb // 3)] = inverse_word + [h]
            frontier = new
    return dict(lower_states=lower, lower_word=lower_word,
                visited_inverse_nodes=visited, candidates=candidates)


def construct_exclusion():
    """Return the complete finite certificate; raise if a merger is found."""
    result = enumerate_lower_partners()
    upper, upper_word = fixed_path((3*PERIOD, 3*RESIDUE))
    upper_lookup = {state: i for i, state in enumerate(upper)}
    checked = []
    for (a, b), witness in sorted(result['candidates'].items()):
        endpoint = follow_fixed_word((a, b), witness['inverse_word'][::-1])
        assert endpoint == result['lower_states'][witness['parent_clock']]
        child_upper, child_upper_word = fixed_path((3*a, 3*b))
        intersections = [[upper_lookup[state], i] for i, state in enumerate(child_upper)
                         if state in upper_lookup]
        if intersections:
            raise ArithmeticError('A joint fixed-word affine merger was found')
        slope = Fraction(a, PERIOD)
        offset = b - slope*RESIDUE
        checked.append(dict(
            coefficient=a, intercept=b,
            affine_in_w=[[slope.numerator, slope.denominator],
                         [offset.numerator, offset.denominator]],
            lower_comparison=witness, upper_word=child_upper_word,
            upper_terminal=list(child_upper[-1]), intersections=intersections))
    return dict(parent_residue=RESIDUE, parent_period=PERIOD,
                lower_states=[list(x) for x in result['lower_states']],
                lower_word=result['lower_word'],
                upper_states=[list(x) for x in upper], upper_word=upper_word,
                visited_inverse_nodes=result['visited_inverse_nodes'],
                candidate_count=len(checked), candidates=checked)
