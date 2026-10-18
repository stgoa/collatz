"""Independent exhaustive replay with a different total-valuation budget.

Default: compare the full recomputed result with the stored receipt.
--write-receipt: replace only uniform_pair_audit.json beside this script.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
import uniform_pair as U

HERE = Path(__file__).resolve().parent


def ord2(value):
    assert type(value) is int and value > 0
    order = 0
    while value % 2 == 0:
        value //= 2
        order += 1
    return order


def independent_path(pair):
    """Equal valuations at n=0,1 are equivalent to whole-domain fixedness."""
    a, b = pair
    states, word = [(a, b)], []
    while True:
        h0, h1 = ord2(3*b + 1), ord2(3*(a + b) + 1)
        if h0 != h1:
            return states, word
        bb = (3*b + 1) // (1 << h0)
        aa = (3*(a + b) + 1) // (1 << h1) - bb
        assert aa > 0 and aa % 2 == 0 and bb > 0 and bb % 2 == 1
        assert ord2(aa) == ord2(a) - h0
        a, b = aa, bb
        states.append((a, b))
        word.append(h0)


def independent_enumeration():
    # Deliberately separate constants and path computation from the constructor.
    residue, period = 40529845, 1 << 26
    lower, lower_word = independent_path((period, residue))
    upper, upper_word = independent_path((3*period, 3*residue))
    found, visited, final_words, budgets = {}, 0, 0, []
    for parent_clock, endpoint in enumerate(lower):
        parent_total = sum(lower_word[:parent_clock])
        for child_clock in range(parent_clock + 1):
            # alpha=2^(26-parent_total+B)*3^(parent_clock-child_clock).
            # This bounds the TOTAL inverse valuation B for an EXACT length.
            maximum = -1
            while ((1 << (maximum + 1))*3**(parent_clock - child_clock)
                   <= (1 << parent_total)):
                maximum += 1
            budgets.append([parent_clock, child_clock, maximum])
            if maximum < child_clock:
                continue
            stack = [(endpoint[0], endpoint[1], 0, ())]
            while stack:
                a, b, spent, word = stack.pop()
                visited += 1
                remaining = child_clock - len(word)
                if remaining == 0:
                    final_words += 1
                    assert a == (1 << (26 - parent_total + spent))*3**(
                        parent_clock - child_clock)
                    assert a <= period
                    if a % 8 == 0 and b % 8 == 5 and 0 < b < residue:
                        states, direct_word = independent_path((a, b))
                        assert states[child_clock] == endpoint
                        assert direct_word[:child_clock] == list(reversed(word))
                        found.setdefault((a, b), []).append(
                            [parent_clock, child_clock, list(word)])
                    continue
                for h in range(1, maximum - spent - (remaining - 1) + 1):
                    aa, bb = (1 << h)*a, (1 << h)*b - 1
                    if aa % 3 or bb % 3 or bb <= 0:
                        continue
                    aa, bb = aa // 3, bb // 3
                    assert aa % 2 == 0 and bb % 2 == 1
                    assert ord2(3*bb + 1) == h
                    stack.append((aa, bb, spent + h, word + (h,)))
    candidates = []
    for (a, b), witnesses in sorted(found.items()):
        child_states, child_word = independent_path((3*a, 3*b))
        intersections = [[i, j] for i, x in enumerate(upper)
                         for j, y in enumerate(child_states) if x == y]
        assert not intersections
        candidates.append(dict(coefficient=a, intercept=b, witnesses=witnesses,
                               upper_word=child_word,
                               upper_terminal=list(child_states[-1])))
    return dict(lower_states=[list(x) for x in lower], lower_word=lower_word,
                upper_states=[list(x) for x in upper], upper_word=upper_word,
                visited_nodes=visited, complete_inverse_words=final_words,
                total_valuation_budgets=budgets, candidates=candidates)


def digest(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def expect_error(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected a domain or fixed-word rejection')


def ordinary_path(seed, word):
    """Direct integer check, including the absorbed point1 with valuation2."""
    for h in word:
        raw = 3*seed + 1
        assert ord2(raw) == h
        seed = raw // (1 << h)
    return seed


def audit():
    direct, independent = U.construct_exclusion(), independent_enumeration()
    for key in ('lower_states', 'lower_word', 'upper_states', 'upper_word'):
        assert direct[key] == independent[key]
    expected_lower = [5, 2, 1, 2, 1, 1, 4, 2, 1, 1, 3]
    expected_upper = [1, 1, 1, 1, 2, 3, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2]
    assert direct['lower_word'] == expected_lower
    assert direct['upper_word'] == expected_upper
    assert direct['lower_states'][-1] == [1417176, 855893]
    assert direct['upper_states'][-1] == [774840978, 467958829]
    direct_keys = {(x['coefficient'], x['intercept']) for x in direct['candidates']}
    independent_keys = {(x['coefficient'], x['intercept']) for x in independent['candidates']}
    assert direct_keys == independent_keys and len(direct_keys) == 43
    assert direct['visited_inverse_nodes'] == 1110
    assert independent['visited_nodes'] == 3401 and independent['complete_inverse_words'] == 450
    by_key = {(x['coefficient'], x['intercept']): x for x in independent['candidates']}
    integer_checks = 0
    for row in direct['candidates']:
        a, b = row['coefficient'], row['intercept']
        other = by_key[(a, b)]
        assert row['upper_word'] == other['upper_word']
        assert row['upper_terminal'] == other['upper_terminal']
        witness = row['lower_comparison']
        j, ell = witness['parent_clock'], witness['child_clock']
        assert [j, ell, witness['inverse_word']] in other['witnesses']
        for n in (0, 1, 2, 17, 100000):
            child = a*n + b
            assert 0 < child < 40529845 + (1 << 26)*n and child % 8 == 5
            assert ordinary_path(child, witness['inverse_word'][::-1]) == ordinary_path(
                40529845 + (1 << 26)*n, expected_lower[:j])
            terminal = ordinary_path(3*child, row['upper_word'])
            assert terminal == row['upper_terminal'][0]*n + row['upper_terminal'][1]
            integer_checks += 1

    # The two-point fixedness criterion is proved in the note; these are
    # additional exact implementation checks, not its universal justification.
    small_paths = []
    for a in range(2, 33, 2):
        for b in range(1, 32, 2):
            first, second = U.fixed_path((a, b)), independent_path((a, b))
            assert first == second
            small_paths.append([a, b, first])
    # n=0 can be absorbed while the affine family remains nonconstant.
    assert U.fixed_path((8, 1)) == ([(8, 1), (6, 1)], [2])
    assert ordinary_path(1, [2]*8) == 1
    # Both equality and strict-reverse order cause a genuine valuation split.
    assert U.fixed_path((8, 13)) == ([(8, 13)], [])
    assert U.fixed_path((8, 5)) == ([(8, 5)], [])

    domain_cases = [(1 << 26, 5, True), (1 << 26, 40529837, True),
                    (8, 5, True), (0, 5, False), (1 << 26, 40529845, False),
                    ((1 << 26) + 8, 5, False), (-8, 5, False), (8, -3, False),
                    (8, 7, False), (4, 5, False), (8.0, 5, False), (True, 5, False)]
    for a, b, expected in domain_cases:
        assert U.eligible_nonconstant_partner(a, b) is expected
    invalid = [lambda: U.fixed_path((0, 5)), lambda: U.fixed_path((-8, 5)),
               lambda: U.fixed_path((7, 5)), lambda: U.fixed_path((8, 0)),
               lambda: U.fixed_path((8, 2)), lambda: U.fixed_path((8.0, 5)),
               lambda: U.fixed_path((True, 5)), lambda: U.fixed_path((8,)),
               lambda: U.valuation2(0), lambda: U.valuation2(-2),
               lambda: U.valuation2(True), lambda: U.inverse_valuation_limit(0, 1),
               lambda: U.inverse_valuation_limit(8, -1),
               lambda: U.follow_fixed_word((8, 1), [2, 2]),
               lambda: U.follow_fixed_word((8, 13), [3]),
               lambda: U.follow_fixed_word((8, 5), [4]),
               lambda: U.follow_fixed_word((8, 1), [1]),
               lambda: U.follow_fixed_word((8, 1), [0]),
               lambda: U.follow_fixed_word((8, 1), [True]),
               lambda: U.follow_fixed_word((8, 1), '2')]
    for action in invalid:
        expect_error(action)
    assert U.follow_fixed_word((8, 1), []) == (8, 1)

    result = dict(
        status='PASS',
        scope='All n>=0 on w=40529845+2^26*n; smaller affine W5 partner; four fixed ordinary valuation words only',
        constructor=direct,
        independent=dict(method='Exact inverse length with global total-valuation budget and two-point fixedness',
                         visited_nodes=independent['visited_nodes'],
                         complete_inverse_words=independent['complete_inverse_words'],
                         candidate_count=len(independent_keys),
                         full_enumeration_sha256=digest(independent)),
        domain_checks=dict(ordinary_integer_cases=integer_checks,
                           small_affine_paths=len(small_paths),
                           small_affine_paths_sha256=digest(small_paths),
                           partner_domain_cases=domain_cases,
                           invalid_input_rejections=len(invalid),
                           absorption_and_split_cases=3, empty_word_checked=True),
        source_hashes={name: hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                       for name in ('uniform_pair.py', 'check_uniform_pair.py', 'UNIFORM_PAIR_SCOPE.md')})
    return json.loads(json.dumps(result))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-receipt', action='store_true')
    args = parser.parse_args()
    result = audit()
    receipt = HERE/'uniform_pair_audit.json'
    if args.write_receipt:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n')
    else:
        if not receipt.exists():
            raise SystemExit('Missing receipt; explicitly use --write-receipt to create it')
        if result != json.loads(receipt.read_text()):
            raise SystemExit('FAIL: stored uniform-pair receipt differs from the complete replay')
    print('PASS: whole-guard fixed-word affine pair exclusion; 43 candidates; '
          '1110 constructor / 3401 independent nodes; no joint merger; 20 rejections')
