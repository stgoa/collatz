"""Exact finite steps and addend-aware controls for two-label rotations.

The finite word grid tests transfers; it is not the general proof.
Run with --write-receipt to regenerate the deterministic receipt.
"""

from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd, prod
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 19
LOCAL_LIMIT = 1 << 19


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def v2(value):
    require(value != 0, "nonzero valuation input")
    value = abs(value)
    return (value & -value).bit_length() - 1


def constants():
    require(3**2 > 2**3 and 3 < 4, "three halves < alpha < two")
    require(3**32 < 2**51, "alpha below 51/32")
    require(F(2, 387) < F(1, 160), "minimum-129 kappa error")
    require(F(51, 32) + F(1, 160) == F(8, 5), "kappa ceiling")
    require(F(8, 5)**5 - 1 < 10, "four-mismatch rise factor")
    require(3 * 129 * F(2, 3) == 258, "drift denominator")
    require(10*(1+2*F(3, 5)) == 22, "minimum-run substitution")
    coefficient = F(3, 8) - F(10, 258)
    require(coefficient == F(347, 1032), "height elimination coefficient")
    length_constant = 23 / coefficient
    require(length_constant == F(23736, 347) < 69, "length constant")
    margin = CUTOFF - 69*(515+342*19)
    require(margin == 40391 > 0, "dyadic cutoff base")
    # At d=19+r, 2 f(d)-f(d+1)=173+342d=6671+342r.
    require(2*515-515-342 == 173 and 173+342*19 == 6671,
            "positive all-band induction polynomial")
    require(69*47 == 3243 and 69*22 == 1518, "integer bootstrap endpoints")
    return dict(minimum=129, kappa_ceiling="8/5", drift_denominator=258,
                rise_factor_ceiling=10, eliminated_coefficient=str(coefficient),
                length_constant=str(length_constant), rounded_length_constant=69,
                cutoff=CUTOFF, dyadic_base_exponent=19, dyadic_base_margin=margin,
                induction_polynomial_in_nonnegative_r=[6671, 342],
                first_finite_maximum=3242, second_finite_maximum=1517,
                local_limit=LOCAL_LIMIT)


def log_enclosure(value, terms):
    z = F(value-1, value+1)
    low = 2*sum((z**(2*i+1)/(2*i+1) for i in range(terms)), F())
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return low, low+tail


def gap_intervals():
    low2, high2 = log_enclosure(2, 80)
    low3, high3 = log_enclosure(3, 80)
    require(F(2, 3) < low2, "strict elementary ln2 lower bound")
    denominator = 1 << 96
    low = 125573666586150569315490533898
    high = low+1
    require(F(low, denominator) < low3/high2 and
            high3/low2 < F(high, denominator), "strict rational alpha enclosure")
    minimum, at = denominator, 0
    digest = sha256()
    for m in range(1, CUTOFF):
        low_floor = m*low // denominator
        high_floor, remainder = divmod(m*high, denominator)
        require(low_floor == high_floor, "certified alpha floor")
        complement = denominator-remainder
        require(complement > (1 << 71), "positive gap exceeds 2^-25")
        if complement < minimum:
            minimum, at = complement, m
        digest.update(f"{m}:{low_floor}:{complement}\n".encode())
    require(minimum == 7373341559091880256221 and at == 190537,
            "positive-gap extremum")
    return dict(series_terms=80, tail_exponent=161,
                alpha_denominator=denominator, alpha_numerators=[low, high],
                checked_lengths=[1, CUTOFF-1], checks=CUTOFF-1,
                minimum_complement_numerator=minimum, minimum_at=at,
                required_numerator=1 << 71, eta_lower_bound="2^-27",
                interval_sha256=digest.hexdigest())


def finite_gaps(maximum, state_limit, expected_at, expected_ceiling):
    power3 = 1
    worst, at = F(), 0
    digest = sha256()
    for m in range(1, maximum+1):
        power3 *= 3
        A = power3.bit_length()
        power2 = 1 << A
        D = power2-power3
        require(D > 0 and (1 << (A-1)) < power3, "minimal positive total")
        margin = 3*state_limit*D-m*power2
        require(margin > 0, "exact finite minimum-state bound")
        candidate = F(m*power2, 3*D)
        if candidate > worst:
            worst, at = candidate, m
        digest.update(f"{m}:{A}:{margin}\n".encode())
    ceiling = (worst.numerator+worst.denominator-1)//worst.denominator
    require(at == expected_at and ceiling == expected_ceiling, "finite gap extremum")
    return dict(lengths=[1, maximum], checks=maximum, strict_state_limit=state_limit,
                maximum_ceiling=ceiling, maximum_at=at,
                comparison_sha256=digest.hexdigest())


def local_descent():
    steps = longest = longest_seed = 0
    digest = sha256()
    for seed in range(3, LOCAL_LIMIT, 2):
        current, length = seed, 0
        while current >= seed:
            raw = 3*current+1
            current = raw >> v2(raw)
            length += 1
            require(length < 100000, "local descent guard")
        require(0 < current < seed and current % 2 == 1, "positive lower odd endpoint")
        steps += length
        if length > longest:
            longest, longest_seed = length, seed
        digest.update(f"{seed}:{current}:{length}\n".encode())
    return dict(odd_seed_range=[3, LOCAL_LIMIT-1], odd_seeds=LOCAL_LIMIT//2-1,
                steps=steps, maximum_steps=longest, maximum_at=longest_seed,
                descent_sha256=digest.hexdigest(),
                argument="Ascending induction reaches a previously verified smaller odd seed; 1 is the base case.")


def minimum_runs():
    accepted = arrows = descending = small = 0
    digest = sha256()
    for length in range(1, 33):
        for odd in range(1, 128, 2):
            start = (1 << (length+1))*odd-1
            current = start
            for _ in range(length):
                require(v2(3*current+1) == 1, "initial exact ones run")
                current = (3*current+1)//2
            e = v2(3*current+1)
            end = (3*current+1) >> e
            require(e >= 2 and v2(start+1) == length+1, "maximal ones-run witness")
            require((current+1)*(1 << length) == 3**length*(start+1),
                    "exact shifted ones-run composition")
            if start < 129:
                small += 1
                continue
            if end < start:
                descending += 1
                continue
            require((1 << (length+e))*start**(length+1) <= (3*start+1)**(length+1),
                    "minimum-return segment product")
            require((1 << (5*(e-1))) < (start+1)**3,
                    "common non-one valuation below three fifths log minimum")
            accepted += 1
            arrows += length+1
            digest.update(f"{start}:{length}:{e}:{end}\n".encode())
    require(accepted > 0 and descending > 0 and small > 0, "both active and excluded hypotheses")
    return dict(ones_lengths=[1, 32], odd_quotients=[1, 127], grid_segments=32*64,
                accepted_minimum_returns=accepted, accepted_arrows=arrows,
                below_minimum_floor=small, below_start_returns=descending,
                segment_sha256=digest.hexdigest(),
                scope="Genuine integer prefixes returning above their start, not asserted cycles.")


def reduced_cycle(word):
    C = total = 0
    for a in word:
        C = 3*C+(1 << total)
        total += a
    D = (1 << total)-3**len(word)
    if D <= 0:
        return None
    common = gcd(C, D)
    q, current = D//common, C//common
    states = []
    for a in word:
        states.append(current)
        raw = 3*current+q
        require(current > 0 and current % 2 == 1 and v2(raw) == a, "reduced exact arrow")
        current = raw >> a
    require(current == states[0] and len(set(states)) == len(word), "primitive reduced closure")
    return q, states


def check_addend_runs(word, states, q):
    count = 0
    for i, letter in enumerate(word):
        if letter != 1 or word[i-1] == 1:
            continue
        length = 0
        while word[(i+length) % len(word)] == 1:
            length += 1
            require(length < len(word), "finite cyclic ones run")
        endpoint = states[(i+length) % len(word)]
        require((endpoint+q)*(1 << length) == 3**length*(states[i]+q),
                "actual-addend ones-run composition")
        require(v2(states[i]+q) == length+1, "actual-addend start witness")
        count += 1
    return count


def binary_controls():
    pairs = [(1, 2), (1, 3), (1, 7), (1, 17), (2, 3), (2, 7)]
    geometry = cycles = arrows = rotations = paired = low_mismatch = noncoprime = exact_four = runs = 0
    examples = []
    digest = sha256()
    for m in range(2, 11):
        for mask in range(1, (1 << m)-1):
            bits = tuple((mask >> i) & 1 for i in range(m))
            # Exactly one representative per primitive rotation class.
            shifted = [bits[h:]+bits[:h] for h in range(1, m)]
            if any(bits >= other for other in shifted):
                continue
            for low, high in pairs:
                word = tuple(high if bit else low for bit in bits)
                geometry += 1
                actual = reduced_cycle(word)
                if actual is None:
                    continue
                q, states = actual
                require(q > 1, "finite binary controls retain their nonunit addend")
                cycles += 1
                arrows += m
                runs += check_addend_runs(word, states, q)
                for h in range(1, m):
                    mismatches = [i for i in range(m) if word[i] != word[(i+h) % m]]
                    s = len(mismatches)
                    require(s > 0 and s % 2 == 0, "positive even binary mismatch count")
                    require(sum(abs(word[i]-word[(i+h) % m]) for i in range(m)) == s*(high-low),
                            "exact two-label variation")
                    require(sum(word[i] < word[(i+h) % m] for i in range(m)) == s//2,
                            "balanced directional label changes")
                    ratios = [F(states[(i+h) % m], states[i]) for i in range(m)]
                    require(prod(ratios) == 1, "zero-sum partner log profile for arbitrary shift")
                    for i in range(m):
                        eps_ratio = F(3*states[(i+h) % m]+q, 3*states[(i+h) % m]) / F(3*states[i]+q, 3*states[i])
                        expected = F(2)**(word[i]-word[(i+h) % m])*eps_ratio
                        require(ratios[(i+1) % m]/ratios[i] == expected, "partner increment identity")
                    longest = 0
                    for start in range(m):
                        length = total = 0
                        while word[(start+length) % m] == word[(start+length+h) % m]:
                            total += word[(start+length) % m]
                            length += 1
                            require(length < m, "primitive agreement terminates")
                        longest = max(longest, length)
                        z0 = states[start]-states[(start+h) % m]
                        end = (start+length) % m
                        ze = states[end]-states[(end+h) % m]
                        require((1 << total)*ze == 3**length*z0, "paired run exact composition")
                        require(z0 != 0 and z0 % (1 << (total+1)) == 0, "paired start witness")
                        require(max(states) > abs(ze) >= 2*3**length, "paired endpoint witness, empty runs included")
                        paired += 1
                    require(s*(longest+1) >= m, "cyclic longest-run count")
                    rotations += 1
                    if s <= 4:
                        low_mismatch += 1
                        if gcd(h, m) > 1:
                            noncoprime += 1
                            if s == 4:
                                exact_four += 1
                            if s == 4 and len(examples) < 3:
                                examples.append(dict(word=list(word), shift=h, shift_gcd=gcd(h, m),
                                                     mismatches=s, q=q, states=states))
                    digest.update(f"{word}:{q}:{h}:{s}:{longest}\n".encode())
    require(exact_four > 0 and len(examples) == 3, "explicit noncoprime four-mismatch controls")
    counter_q, counter_states = reduced_cycle((1, 1, 7, 7))
    require(counter_q == 65455 and counter_states == [569, 33581, 83099, 2459],
            "explicit addend-retaining nontransfer control")
    require(min(counter_states) >= 129 and 2**30 > (min(counter_states)+1)**3,
            "minimum floor alone cannot transfer the q1 valuation bound")
    return dict(periods=[2, 10], label_pairs=pairs, primitive_necklaces=geometry,
                reduced_cycles=cycles, exact_arrows=arrows, rotations=rotations,
                paired_run_checks=paired, actual_addend_run_checks=runs,
                shifts_with_at_most_four_mismatches=low_mismatch,
                noncoprime_shifts_with_at_most_four_mismatches=noncoprime,
                noncoprime_shifts_with_exactly_four_mismatches=exact_four,
                noncoprime_examples=examples, control_sha256=digest.hexdigest(),
                q1_nontransfer_control=dict(q=counter_q, states=counter_states,
                                            word=[1, 1, 7, 7], shift=2,
                                            comparison="2^30 > 570^3"),
                scope="Finite exact positive 3x+q cycles. No q1 minimum or drift bound is transferred to q>1.")


def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = runs = 0
    for row in rows:
        q, states, word = row["d"], row["states"], row["valuations"]
        require(q in (5, 7, 13, 61), "standard actual addend")
        for i, a in enumerate(word):
            raw = 3*states[i]+q
            require(v2(raw) == a and raw >> a == states[(i+1) % len(word)], "standard exact arrow")
            arrows += 1
        runs += check_addend_runs(word, states, q)
    require(len(rows) == 11 and arrows == 106, "all standard fixtures")
    return dict(cycles=len(rows), exact_arrows=arrows, actual_addend_run_checks=runs,
                fixture_sha256=sha256(path.read_bytes()).hexdigest())


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="two-label-four-mismatch-v1",
                   source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                   constants=constants(), gap_intervals=gap_intervals(),
                   finite_gaps=[finite_gaps(3242, 1 << 21, 2966, 1166894),
                                finite_gaps(1517, 1 << 19, 971, 330912)],
                   local_descent=local_descent(), minimum_runs=minimum_runs(),
                   binary_controls=binary_controls(), standard_controls=standard_controls())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    path = HERE/"check_two_labels.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps(dict(result="passed", positive_gap_intervals=receipt["gap_intervals"]["checks"],
                          finite_gap_comparisons=sum(row["checks"] for row in receipt["finite_gaps"]),
                          local_odd_seeds=receipt["local_descent"]["odd_seeds"],
                          reduced_cycles=receipt["binary_controls"]["reduced_cycles"],
                          noncoprime_controls=receipt["binary_controls"]["noncoprime_shifts_with_at_most_four_mismatches"]),
                     sort_keys=True))


if __name__ == "__main__":
    main()
