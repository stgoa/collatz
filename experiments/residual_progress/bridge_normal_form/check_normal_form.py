"""Bounded checks for the complete elementary-bridge normal form."""

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import normal_form as NF


HERE = Path(__file__).resolve().parent


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def run_checks():
    seed_bound = 32767
    normal_records = []
    strata = Counter()
    for x in range(1, seed_bound+1, 2):
        data = NF.normalization(x)
        q, k, partner = data["minimum"], data["F_exponent"], data["selected_partner"]
        assert q <= x and NF.normal_form(q) == q
        assert NF.F_power(2*q+1 if partner else q, k) == x
        assert NF.normal_form(NF.F(x)) == q
        assert NF.normal_form(NF.step(x)) == NF.quotient_step(q)
        exact_k = (NF.valuation2(3*x+1)-1)//2
        assert k == exact_k
        strata[k, partner] += 1
        normal_records.append((x, q))

    currents = []
    for x in range(1, 4096, 2):
        data = NF.bridge(x)
        q = data["minimum"]
        expected = {x: 1} if x != 1 else {}
        if q != 1:
            expected[q] = expected.get(q, 0)-1
        expected = {y: c for y, c in expected.items() if c}
        assert NF.divergence(data["current"]) == expected
        currents.append((x, data["current"]))
        if NF.canonical(x):
            qdata = NF.quotient_bridge(x)
            assert qdata["minimum"] == NF.quotient_step(x)

    # Every inverse point below a fixed height is checked, including targets
    # not reached by any point in that bounded range.
    inverse_bound = 16383
    direct = defaultdict(list)
    for q in range(1, inverse_bound+1, 2):
        if NF.canonical(q):
            direct[NF.quotient_step(q)].append(q)
    inverse_targets = 0
    for y in range(1, (3*inverse_bound+1)//2 + 1, 2):
        if NF.canonical(y):
            assert NF.predecessors_up_to(y, inverse_bound) == direct.get(y, [])
            point, rays = NF.predecessor_families(y)
            assert NF.least_predecessor(y) == min(rays if point is None else rays+(point,))
            for start in rays:
                assert NF.quotient_step(64*start+49) == y
            inverse_targets += 1

    greedy_failures = []
    for j in range(129):
        y, exact, greedy = 57+72*j, 203+256*j, 409+512*j
        assert NF.canonical(y)
        assert NF.least_predecessor(NF.least_predecessor(y)) == greedy
        assert NF.quotient_step(NF.quotient_step(exact)) == y
        assert NF.least_two_step_predecessor(y) == exact < greedy
        greedy_failures.append((j, y, exact, greedy))

    # Full counting checks, including arbitrary fixed odd progressions.
    progressions = [(m, r) for m in (1, 3, 9, 15) for r in range(m)]
    counting_cases = 0
    for m, r in progressions:
        explicit = 0
        for limit in range(4097):
            if limit and limit % 2 and limit % m == r and NF.canonical(limit):
                explicit += 1
            if limit % 8 == 0 or limit in (1, 3, 7, 4095):
                assert NF.canonical_count(limit, r, m) == explicit
                if limit:
                    a = (limit+1).bit_length()-1
                    assert abs(Fraction(explicit) - Fraction(limit, 4*m)) <= Fraction(2*a+1, 2)
                counting_cases += 1
    for (k, partner), count in strata.items():
        assert NF.stratum_count(seed_bound, k, partner) == count
    assert sum(NF.stratum_count(seed_bound, k, partner)
               for k in range(9) for partner in (False, True)) == (seed_bound+1)//2
    for m, r in ((3, 1), (9, 0), (15, 11)):
        direct_strata = Counter()
        for x in range(1, 4096, 2):
            if x % m == r:
                data = NF.normalization(x)
                direct_strata[data["F_exponent"], data["selected_partner"]] += 1
        for k in range(7):
            for partner in (False, True):
                assert NF.stratum_count(4095, k, partner, r, m) == direct_strata[k, partner]

    ascent_records = []
    exponents = list(range(3, 66, 2)) + [129, 257, 513, 1025]
    for a in exponents:
        x = 2**a - 1
        q = x
        assert NF.canonical(x)
        for j in range(a):
            assert q == 3**j * 2**(a-j) - 1
            assert NF.canonical(q)
            if j < a-1:
                assert q % 4 == 3 and not NF.selected(q)
                nxt = NF.quotient_step(q)
                assert nxt > q
                q = nxt
        assert q % 8 == 1
        if a >= 7:
            N = 12*2**(a-4)
            assert 9*N < 8*x < 12*N and x % 12 == 7
        ascent_records.append(dict(a=a, seed_bits=x.bit_length(), peak_bits=q.bit_length()))

    # Fiber1 is special under absorption, and is not assigned a common
    # hitting time.  Its two rays all absorb within two actual arrows.
    for k in range(33):
        for base in (1, 3):
            x = NF.F_power(base, k)
            assert NF.normal_form(x) == 1
            assert NF.step(NF.step(x)) == 1

    return dict(
        status="PASS",
        scope="Exact identities and bounded checks; quotient termination remains open",
        seed_bound=seed_bound, seeds=(seed_bound+1)//2,
        normal_form_hash=digest(normal_records), current_seeds=len(currents),
        current_hash=digest(currents), inverse_height_bound=inverse_bound,
        inverse_targets=inverse_targets, counting_cases=counting_cases,
        greedy_counterexample_count=len(greedy_failures),
        first_greedy_counterexample=list(greedy_failures[0]),
        greedy_counterexample_hash=digest(greedy_failures),
        ascent_cases=ascent_records,
        strata=[dict(k=k, selected_partner=partner, count=count)
                for (k, partner), count in sorted(strata.items())],
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt = run_checks()
    target = HERE / "normal_form_audit.json"
    if args.write_receipt:
        target.write_text(json.dumps(receipt, indent=2, sort_keys=True)+"\n")
    else:
        assert json.loads(target.read_text()) == receipt
    print(f"PASS: {receipt['seeds']} seeds, {receipt['current_seeds']} exact bridges, "
          f"{receipt['inverse_targets']} inverse targets, {receipt['counting_cases']} count checks")


if __name__ == "__main__":
    main()
