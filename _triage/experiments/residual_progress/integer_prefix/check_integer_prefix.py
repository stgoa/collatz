"""Bounded independent arithmetic/current audit of the two-return coding."""
import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path
from types import ModuleType

import integer_prefix as I

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def source_hashes():
    """Follow actual dynamic module objects, including unregistered imports."""
    pending, found = [I], {}
    while pending:
        module = pending.pop()
        source = getattr(module, '__file__', None)
        if source is None:
            continue
        path = Path(source).resolve()
        if REPO not in path.parents or path.suffix != '.py':
            continue
        key = str(path.relative_to(REPO))
        if key in found:
            continue
        found[key] = hashlib.sha256(path.read_bytes()).hexdigest()
        pending.extend(value for value in vars(module).values() if isinstance(value, ModuleType))
    own = Path(__file__).resolve()
    found[str(own.relative_to(REPO))] = hashlib.sha256(own.read_bytes()).hexdigest()
    return found


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def words(length):
    return [''.join(chars) for chars in product('VR', repeat=length)]


def backwards(word):
    """Pull back the terminal cylinder; independent of forward affine()."""
    residue, bits = I.BASE, I.BASE_BITS
    for symbol in reversed(word):
        a, c, e, _, _ = I.BRANCHES[symbol]
        bits += e
        residue = (2**e*residue-c)*pow(a, -1, 2**bits)%2**bits
    return residue, bits


def iterate(seed, count, quotient=False):
    step = I.NORMAL.quotient_step if quotient else I.NORMAL.step
    for _ in range(count):
        seed = step(seed)
    return seed


def count_cylinder(data, bound):
    return max(0, (bound-data['residue'])//data['period']+1)


def raw_rational_step(value, symbol):
    a, c, e, _, _ = I.BRANCHES[symbol]
    return (a*value+c)/2**e


def audit():
    assert I.cylinder('V')['residue'] == I.V_RESIDUE
    assert I.cylinder('R')['residue'] == I.X.RESIDUE
    assert I.cylinder('V')['bits'] == 45 and I.cylinder('R')['bits'] == 63
    assert I.X.RESIDUE%2**45 != I.V_RESIDUE
    assert I.X.L == I.M.DEN**2//2 and I.X.C == I.M.B*(I.M.A+I.M.DEN)

    prefixes = []
    for length in range(1, 9):
        for word in words(length):
            data = I.cylinder(word)
            assert (data['residue'], data['bits']) == backwards(word)
            for index in (0, 1, 7):
                family = I.family(word, index)
                for at, symbol in enumerate(word):
                    assert I.branch(family['states'][at]) == symbol
                    before = I.M.DIFFERENCE*family['states'][at]+I.M.B
                    after = I.M.DIFFERENCE*family['states'][at+1]+I.M.B
                    if symbol == 'V':
                        assert after*I.M.DEN == I.M.A*before
                    else:
                        assert (after+I.M.B)*I.X.L == I.X.P*before
                assert all(a < b for a, b in zip(family['states'], family['states'][1:]))
            prefixes.append([word, data['residue'], data['bits']])

    long_words = []
    for length in (16, 32, 64, 128, 256):
        samples = ['V'*length, 'R'*length, ('VR'*length)[:length],
                   ''.join('R' if bin(n).count('1')%2 else 'V' for n in range(length))]
        for word in samples:
            data = I.family(word)
            assert (data['residue'], data['bits']) == backwards(word)
            long_words.append(dict(length=length, word_hash=digest(word), bits=data['bits'],
                                   seed=str(data['seed']), state_hash=digest(data['states'])))

    crt = []
    for word in ('V', 'R', 'VR', 'RV', 'VVRRV', 'RVRVRV'):
        for modulus in (1, 3, 9, 81, 125, 729):
            for residue in (0, 1, modulus-1):
                data = I.odd_lift(word, modulus, residue)
                assert data['seed']%modulus == residue%modulus
                crt.append([word, modulus, residue, data['seed']])

    maximal = []
    for counts in ([1], [2], [9], [64], [1, 2], [2, 1], [3, 7, 2], [1]*16, [8, 1, 9, 2]):
        data = I.maximal_counts(counts)
        if len(counts) == 1:
            old = I.X.general_reentry_family(counts[0])
            assert (data['seed'], data['period'], data['leading']) == (old['seed'], old['period'], old['leading'])
        maximal.append(dict(counts=counts, seed=data['seed'], leading=data['leading'], bits=data['bits']))

    rationals = []
    for length in range(1, 6):
        for cycle in words(length):
            for prefix in ('', 'V', 'R', 'VR', 'RV'):
                point = I.rational_point(prefix, cycle)
                assert point < 0 and point.denominator%2
                probe = prefix+cycle*3
                data = I.cylinder(probe)
                assert I.rational_congruent(point, data['residue'], data['period'])
                current = point
                for symbol in prefix:
                    current = raw_rational_step(current, symbol)
                cyclic = current
                for symbol in cycle:
                    current = raw_rational_step(current, symbol)
                assert current == cyclic
                rationals.append([prefix, cycle, str(point)])

    density = []
    for length in range(1, 9):
        data = [I.cylinder(word) for word in words(length)]
        actual = sum((Fraction(1, row['period']) for row in data), Fraction(0))
        assert actual == Fraction(1, 2**26)*I.CONDITIONAL_DENSITY**length
        if length <= 6:
            for left in range(len(data)):
                for right in range(left):
                    common = 2**min(data[left]['bits'], data[right]['bits'])
                    assert data[left]['residue']%common != data[right]['residue']%common
        for bound in (2**26, 2**64, 2**128, 2**256+2**17):
            count = sum(count_cylinder(row, bound) for row in data)
            error = abs(count-bound*actual)
            assert error < 2**length
            density.append([length, bound, count, str(actual), str(error)])

    plans, stored = [], []
    for length in range(1, 5):
        for word in words(length):
            family = I.family(word)
            data = I.plan(family['seed'], word)
            left, right = data['ordinary_common_tail_clocks']
            assert iterate(3*data['seed'], left) == iterate(3*data['leading'], right)
            assert iterate(3*data['seed'], data['quotient_length'], True) == 3*data['leading']
            # Independent whole ordinary path difference must match every row.
            _, plus, _ = I.M.path_current(3*data['seed'], left)
            _, minus, _ = I.M.path_current(3*data['leading'], right)
            direct = I.combine((1, plus), (-1, minus))
            assert direct == I.comparison(data['seed'], word)['current']
            # Explicitly substitute complete old local plans, including helpers.
            composed = None
            for at, symbol in enumerate(word):
                seed = data['states'][at]
                local = I.M.macro(seed) if symbol == 'V' else I.X.plan(seed, audit_composition=True)
                composed = local if composed is None else I.M.substitute_leading(composed, local)
            assert data['current'] == composed['current']
            assert data['coefficients'] == composed['coefficients']
            try:
                I.compile_plan(data, {})
            except (ValueError, KeyError):
                pass
            else:
                raise AssertionError('A missing larger pair current was silently supplied')
            plans.append(dict(word=word, seed=data['seed'], leading=data['leading'],
                              rows=len(data['current']), requests=len(data['coefficients']),
                              original_high=len(data['high']), clocks=data['ordinary_common_tail_clocks'],
                              current_hash=digest(data['current']), request_hash=digest(data['coefficients'])))
            if word in ('VR', 'RV'):
                stored.append(data)

    cap_seed = I.family('VR'*8)['seed']
    caps = [I.capped_trace(cap_seed, 3), I.capped_trace(cap_seed, 10, 8),
            I.capped_trace(I.BASE, 3)]
    assert [row['status'] for row in caps] == ['unresolved_symbol_cap', 'unresolved_bit_cap', 'exit']
    rejected = 0
    for action in (lambda: I.cylinder(''), lambda: I.cylinder('X'),
                   lambda: I.cylinder('V'*257), lambda: I.family('V', -1),
                   lambda: I.odd_lift('V', 2, 0), lambda: I.maximal_counts([0]),
                   lambda: I.step(I.BASE, 'V'), lambda: I.plan(I.BASE, 'VR'),
                   lambda: I.capped_trace(0), lambda: I.capped_trace(1, -1)):
        try:
            action()
        except ValueError:
            rejected += 1
        else:
            raise AssertionError('An invalid input was accepted')

    return dict(status='PASS', source_hashes=source_hashes(),
                ranges=dict(all_words_through_length=8, progression_indices=[0,1,7],
                            long_word_lengths=[16,32,64,128,256], full_currents_through_length=4,
                            periodic_words_through_length=5, symbol_cap=256),
                counts=dict(prefix_words=len(prefixes), positive_prefix_realizations=3*len(prefixes),
                            long_words=len(long_words), odd_crt_cases=len(crt), maximal_count_lists=len(maximal),
                            eventually_periodic_points=len(rationals), density_counts=len(density),
                            full_current_compositions=len(plans), stored_full_currents=len(stored),
                            missing_supply_rejections=len(plans), cap_or_exit_checks=len(caps),
                            invalid_input_rejections=rejected),
                prefix_hash=digest(prefixes), long_words=long_words, crt_hash=digest(crt),
                maximal_counts=maximal, periodic_hash=digest(rationals), density_checks=density,
                plans=plans, stored_full_currents=stored, caps=caps,
                limits=['Finite prefix realization does not produce a fixed infinite positive seed.',
                        'No eventually periodic positive survivor; aperiodic survivors remain unresolved.',
                        'These growing comparisons are conditional and add no accepted dispatcher rule.',
                        'The larger leading pair and every signed helper remain required.'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    path = HERE/'integer_prefix_audit.json'
    normalized = json.loads(json.dumps(result, sort_keys=True))
    if args.write_receipt:
        path.write_text(json.dumps(normalized, indent=2, sort_keys=True)+'\n')
    else:
        assert normalized == json.loads(path.read_text()), 'The stored integer-prefix receipt differs'
    c = result['counts']
    print('PASS: integer-prefix coding; '+', '.join(f'{k}={v}' for k,v in c.items()))
