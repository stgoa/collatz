#!/usr/bin/env python3
"""Construct complete binary cylinders excluding bounded prescribed mergers.

The proof is in CHILD_HISTORY_SCOPE.md. This is a scoped exclusion, not a
current constructor. Only the Python standard library is used.
"""
from fractions import Fraction
from pathlib import Path
import argparse
import hashlib
import json


Q0 = 70506316836123
QP = 3 * 2**45
D, B = 7153, 299947
VSTAR = Fraction(-B, D)
QSTAR = (2**27 * VSTAR - 213949807) / 3**17
ELLSTAR = (QSTAR-Q0) / QP
RAW_WORD = (1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2)
CHILD_TWO_WORD = (
    1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3,
    1, 2, 1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2, 2, 2,
    1, 3, 1, 1, 2, 6, 1, 6, 1, 1, 1, 1, 2, 1, 1, 1,
    1, 6, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 2, 1, 2, 2,
    1, 5, 1, 1, 2, 1, 2, 3, 1, 2, 5, 5, 2, 2, 1, 2,
    2, 1, 1, 2, 10, 2, 3, 1, 1, 4, 1, 1, 1, 1, 2, 1,
    5, 2, 3, 2, 1, 2, 1, 2, 1, 6, 1, 4, 3, 7, 6, 2)
HERE = Path(__file__).resolve().parent


def valuation2(x):
    x = Fraction(x)
    if not x:
        raise ValueError('The binary valuation of zero is not finite')
    n, d = abs(x.numerator), x.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def residue(x, bits):
    if type(bits) is not int or bits < 0:
        raise ValueError('Require a nonnegative integer bit count')
    x = Fraction(x)
    if x.denominator % 2 == 0:
        raise ValueError('Require a binary-integral rational')
    modulus = 2**bits
    return (x.numerator * pow(x.denominator, -1, modulus)) % modulus


def shadow_prefix(seed, length):
    if type(length) is not int or length < 0:
        raise ValueError('Require a nonnegative integer clock cap')
    x = Fraction(seed)
    if valuation2(x) != 0:
        raise ValueError('Require an odd rational seed with odd denominator')
    states, word, forms = [x], [], [(1, 0, 0)]
    coefficient, constant, total = 1, 0, 0
    for _ in range(length):
        a = valuation2(3*x+1)
        if a < 1:
            raise ValueError('The rational Syracuse branch is not odd')
        x = (3*x+1) / 2**a
        coefficient, constant = 3*coefficient, 3*constant+2**total
        total += a
        states.append(x)
        word.append(a)
        forms.append((coefficient, constant, total))
        assert x == (coefficient*seed+constant)/2**total
    return states, word, forms


def centers(digit):
    if type(digit) is not int or digit not in (0, 1, 2):
        raise ValueError('Require a ternary digit')
    jstar = (ELLSTAR-digit)/3
    qstar = Q0+QP*(digit+3*jstar)
    pstar = Q0+QP*jstar
    assert jstar.denominator % 2 and qstar < 0
    if digit < 2:
        assert qstar == QSTAR and pstar > 0
    else:
        assert qstar == QSTAR and pstar == Fraction(-799360888748662478376301, 34212577257)
    return jstar, qstar, pstar


def pack(x):
    x = Fraction(x)
    return [x.numerator, x.denominator]


def construct_progression(digit, cap, minimum_returns=0):
    """Every positive j in the returned cylinder has no merger at clocks<=cap.

    Prefix stability and exclusion of every affine equality root certify the
    entire cylinder. The return value is finite evidence, not a sample claim.
    """
    if type(cap) is not int or cap < 0:
        raise ValueError('Require a nonnegative integer clock cap')
    if type(minimum_returns) is not int or minimum_returns < 0:
        raise ValueError('Require a nonnegative integer return lower bound')
    jstar, qstar, pstar = centers(digit)
    qs, qw, qforms = shadow_prefix(qstar, cap)
    ps, pw, pforms = shadow_prefix(pstar, cap)
    assert all(x < 0 for x in qs)
    assert not set(qs).intersection(ps)
    max_cost = max(qforms[-1][2], pforms[-1][2])
    bits = max(0, max_cost+1-45, 19*minimum_returns)
    roots = set()
    constant_nonzero = 0
    for qa, qc, qe in qforms:
        for pa, pc, pe in pforms:
            slope = Fraction(qa*3*QP, 2**qe) - Fraction(pa*QP, 2**pe)
            intercept = Fraction(qa*(Q0+digit*QP)+qc, 2**qe) - Fraction(pa*Q0+pc, 2**pe)
            # A zero affine equation would be a uniform fixed-word merger.
            assert slope or intercept
            if not slope:
                constant_nonzero += 1
                continue
            root = -intercept/slope
            if root.denominator == 1 and root >= 0:
                root = int(root)
                roots.add(root)
                assert Fraction(root) != jstar
                bits = max(bits, valuation2(Fraction(root)-jstar)+1)
    base = residue(jstar, bits)
    modulus = 2**bits
    assert all(root % modulus != base for root in roots)
    assert bits+45 >= max_cost+1
    return dict(digit=digit, cap=cap, minimum_returns=minimum_returns, j_shadow=pack(jstar),
                q_shadow=pack(qstar), p_shadow=pack(pstar),
                bits=bits, residue=base, modulus=modulus,
                upper_word=qw, lower_word=pw,
                affine_equations=(cap+1)**2,
                constant_nonzero_equations=constant_nonzero,
                nonnegative_integer_roots=sorted(roots))


def integer_prefix(seed, cap):
    """Independent integer replay; no rational-word or affine helper is used."""
    if type(seed) is not int or seed <= 0 or seed % 2 != 1:
        raise ValueError('Require a positive odd seed')
    x, states, word = seed, [seed], []
    for _ in range(cap):
        numerator = 3*x+1
        a = (numerator & -numerator).bit_length()-1
        x = numerator >> a
        states.append(x)
        word.append(a)
    return states, word


def negative_shadow_certificate():
    states, word, _ = shadow_prefix(QSTAR, 30)
    assert states[18] == 6*VSTAR+1 == Fraction(-1792529, D)
    assert word[18:] == list(RAW_WORD)
    assert states[30] == states[18]
    assert all(x < 0 for x in states)
    assert QSTAR == Fraction(-515908491727, 11404192419)
    assert ELLSTAR == Fraction(-22852975802, 34212577257)
    assert valuation2(QSTAR-Q0) == 46
    _, _, child = centers(2)
    child_states, child_word, child_forms = shadow_prefix(child, 112)
    assert child_word == list(CHILD_TWO_WORD)
    assert all(x < 0 for x in child_states[:-1])
    assert child_states[-1] == Fraction(1663, D) > 0
    assert not set(states[:-1]).intersection(child_states[:-1])
    return dict(q_shadow=pack(QSTAR), ell_shadow=pack(ELLSTAR),
                prefix_word=word[:18], cycle_word=word[18:],
                cycle_source=pack(states[18]),
                cycle_length=12, cycle_cost=sum(word[18:]),
                third_child_shadow=pack(child), third_child_word=child_word,
                third_child_positive_endpoint=pack(child_states[-1]),
                third_child_cost=child_forms[-1][2],
                third_child_states=[pack(x) for x in child_states])


def audit():
    certificate = negative_shadow_certificate()
    cases, comparisons = [], 0
    for cap, returns in [(k, 0) for k in (0, 1, 2, 4, 8, 16, 32, 64, 128)] + [(16, r) for r in (1, 4, 16, 128)]:
        for digit in range(3):
            plan = construct_progression(digit, cap, returns)
            base, modulus = plan['residue'], plan['modulus']
            first = base if base > 0 else modulus
            for shift in (0, 1, 2, 7):
                j = first+shift*modulus
                ell = digit+3*j
                q, p = Q0+QP*ell, Q0+QP*j
                assert 0 < j < ell and p < q
                v = 67839005952677+2**18*3**18*ell
                assert valuation2(D*v+B) >= 19*returns+18
                qs, qw = integer_prefix(q, cap)
                ps, pw = integer_prefix(p, cap)
                assert qw == plan['upper_word'] and pw == plan['lower_word']
                assert not set(qs).intersection(ps)
                comparisons += 1
            cases.append(plan)
    rejections = 0
    for digit, cap in ((-1, 1), (3, 1), (True, 1), (0, -1), (0, True), (0, 1.5)):
        try:
            construct_progression(digit, cap)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('An invalid domain was accepted')
    for x in (0, False):
        try:
            valuation2(x)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('Zero valuation was accepted')
    for x in (Fraction(1, 2), Fraction(3, 4)):
        try:
            residue(x, 2)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('A nonintegral binary center was accepted')
    for invalid in (-1, True, 0.5):
        try:
            construct_progression(0, 1, invalid)
        except ValueError:
            rejections += 1
        else:
            raise AssertionError('An invalid return bound was accepted')
    hashes = {name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
              for name in ('CHILD_HISTORY_SCOPE.md', 'check_child_catalogue_scope.py')}
    return dict(status='PASS', scope='bounded clocks for the prescribed ternary child only',
                negative_shadow=certificate, progression_cases=len(cases),
                actual_integer_pairs=comparisons, rejections=rejections,
                cases=cases, source_hashes=hashes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='Regenerate the deterministic audit receipt')
    args = parser.parse_args()
    data = audit()
    receipt = HERE/'child_history_audit.json'
    if args.write:
        receipt.write_text(json.dumps(data, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    else:
        if json.loads(receipt.read_text(encoding='utf-8')) != data:
            raise AssertionError('Stored receipt differs from the complete deterministic replay')
    print('PASS:', data['progression_cases'], 'complete clock-cap cylinders;',
          data['actual_integer_pairs'], 'integer pairs;', data['rejections'], 'rejections')


if __name__ == '__main__':
    main()
