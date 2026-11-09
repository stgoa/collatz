"""Exact controls and finite steps for half-defect imbalance growth.

The README gives the unbounded four-case proof. This certificate checks
intrinsic normalization, its rational inequalities on actual 3x+d cycles,
the full-even-clock gap bootstrap, local descent and exact cutoff constants.
No finite absence is promoted to a universal claim. Standard library only;
default execution compares its receipt, --write-receipt regenerates it.
"""

from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import gcd
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIXTURES = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
LOCAL_LIMIT = 18_000_000
MEAN_LIMIT = 2**17
A0 = F(15849, 10000)
K0 = F(317, 200)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def digest_record(digest, record):
    digest.update((json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode())


def intercept(word):
    total = value = 0
    for letter in word:
        value = 3 * value + 2**total
        total += letter
    return value


def rotate(word, offset):
    return word[offset:] + word[:offset]


def raised(word, extra):
    return word[:-1] + (word[-1] + extra,)


def replay(word, d, states):
    require(len(word) == len(states) > 0 and d > 0 and d % 2, "cycle dimensions and addend")
    for i, (letter, state) in enumerate(zip(word, states)):
        require(letter > 0 and state > 0 and state % 2, "positive odd state")
        raw = 3 * state + d
        require((raw & -raw).bit_length() - 1 == letter, "exact valuation")
        require(raw == 2**letter * states[(i + 1) % len(word)], "actual cycle arrow")
    return len(word)


def actual_cycle(word):
    D = 2**sum(word) - 3**len(word)
    require(D > 0, "positive discriminant")
    common = gcd(D, intercept(word))
    d = D // common
    state = intercept(word) // common
    states = []
    for letter in word:
        states.append(state)
        raw = 3 * state + d
        require(raw % 2**letter == 0, "integral reduced step")
        state = raw // 2**letter
    require(state == states[0], "reduced closure")
    replay(word, d, states)
    for i, state in enumerate(states):
        require(intercept(rotate(word, i)) == state * common, "independent rotated-intercept check")
    return d, states


def primitive(word):
    return all(len(word) % size or word != word[:size] * (len(word) // size)
               for size in range(1, len(word)))


def normalize(word):
    N = len(word) // 2
    differences = [word[N + i] - word[i] for i in range(N) if word[N + i] != word[i]]
    require(len(differences) == 2, "exactly two half differences")
    for cut in range(len(word)):
        v = rotate(word, cut)
        changed = [i for i in range(N) if v[i] != v[i + N]]
        if changed[-1] != N - 1 or any(v[i + N] <= v[i] for i in changed):
            continue
        a = changed[0] + 1
        A, B = v[:a], v[a:N]
        p, q = v[N + a - 1] - v[a - 1], v[-1] - v[N - 1]
        require(A and B and p > 0 and q > 0, "positive nonempty canonical blocks")
        require(v == A + B + raised(A, p) + raised(B, q), "canonical reconstruction")
        require(sorted((p, q)) == sorted(abs(value) for value in differences), "magnitude preservation")
        return cut, A, B, p, q
    raise RuntimeError("normalization did not find the proved canonical cut")


def normalization_controls():
    counts = Counter()
    digest = sha256()
    for N in range(2, 6):
        for word in product(range(1, 4), repeat=2 * N):
            counts["words_examined"] += 1
            diffs = [word[i + N] - word[i] for i in range(N) if word[i + N] != word[i]]
            if len(diffs) != 2:
                continue
            require(sum(word[i] != word[(i + N) % (2 * N)] for i in range(2 * N)) == 4, "half mismatch count")
            require(primitive(word), "automatic primitivity control")
            cut, A, B, p, q = normalize(word)
            counts["four_mismatch_words"] += 1
            counts["same_sign_input" if diffs[0] * diffs[1] > 0 else "opposite_sign_input"] += 1
            counts["equal_magnitudes" if p == q else "unequal_magnitudes"] += 1
            digest_record(digest, [list(word), cut, list(A), list(B), p, q])
    return {"half_lengths": [2, 5], "letters": [1, 3],
            "counts": dict(sorted(counts.items())), "cases_sha256": digest.hexdigest(),
            "scope": "finite reconstruction and primitivity controls; the README proves both generally"}


def check_case(A, B, p, q, d, states):
    a, b = len(A), len(B)
    N = a + b
    P, R, Q, S = 3**a, 3**b, 2**sum(A), 2**sum(B)
    k, l = 2**p, 2**q
    x, z, y, t = states[0], states[a], states[N], states[N + a]
    require(x < y and (y - x) % Q == 0 and (z - t) % S == 0, "exact paired quotients")
    h, j = (y - x) // Q, (z - t) // S
    require(h > 0 and h % 2 and j % 2, "odd paired quotients")
    if p < q and j > 0:
        require(d > 1, "PR95 excludes this order only at addend one")
        return None
    require((p < q and j < 0) or (p >= q and j > 0), "eligible paired order")
    M = min(states)
    gamma = F(3 * M + d, 2 * M)
    rho = F(P * R, Q * S)
    r0 = F(y, x)
    r = F(t, z) if p < q else F(z, t)
    require(r0 > 1 and r > 1 and r0 < F(k * l, 1) / rho, "first ratio bound")
    require(r < F(l if p < q else k, 1) / rho, "second ratio bound")
    if p < q:
        require(r < r0 / k, "ratio contraction in A")
        require(all(states[i] < states[i + N] for i in range(N)), "smaller first-half states")
        allowed = set(range(N))
    else:
        require(F(y, l * x) < r, "ratio contraction in B")
        require(all(states[i] < states[i + N] for i in range(a)), "smaller first-A states")
        require(all(states[N + a + i] < states[a + i] for i in range(b)), "smaller second-B states")
        allowed = set(range(a)) | set(range(N + a, 2 * N))
    minima = [i for i, state in enumerate(states) if state == M]
    require(set(minima) <= allowed, "all tied minimum locations")
    case_names = []
    for i in minima:
        if p < q and i < a:
            case = "A"
            require(M > F(2**a, 1) / r0 and M > F(2**b, 1) / (r * gamma**a), "case A bounds")
            require(z <= gamma**(a - i) * M, "case A remaining growth")
        elif p < q:
            case = "B"
            require(M > F(2**b, 1) / r and M > F(2**a, 1) / gamma**b, "case B bounds")
            require(y <= gamma**(N - i) * M, "case B remaining growth")
        elif i < a:
            case = "C"
            require(M > F(2**a, 1) / r0 and M > F(2**b, 1) / gamma**a, "case C bounds")
            require(z <= gamma**(a - i) * M, "case C remaining growth")
        else:
            case = "D"
            require(M > F(2**b, 1) / r and M > F(2**a, 1) / (r * gamma**b), "case D bounds")
            require(l * x <= gamma**(2 * N - i) * M, "retained terminal-q factor")
        case_names.append(case)
    if M >= d * MEAN_LIMIT:
        require(2**N < M**36 * 2**(7 * abs(p - q)), "combined bound only at sufficient normalized minimum")
    return {"cases": case_names, "minimum": M, "addend": d,
            "boundaries": [x, z, y, t], "paired_h": h, "paired_j": j,
            "normalized_minimum": str(F(M, d)), "gamma": str(gamma),
            "r0": str(r0), "r": str(r)}


def actual_controls():
    words = [word for length in range(1, 4) for word in product(range(1, 4), repeat=length)]
    counts = Counter()
    examples = {}
    digest = sha256()
    for A in words:
        for B in words:
            for p in range(1, 6):
                for q in range(1, 6):
                    word = A + B + raised(A, p) + raised(B, q)
                    if 2**sum(word) <= 3**len(word):
                        counts["nonpositive_gap_skipped"] += 1
                        continue
                    d, states = actual_cycle(word)
                    result = check_case(A, B, p, q, d, states)
                    if result is None:
                        counts["opposite_state_order_skipped"] += 1
                        continue
                    counts["eligible_cycles"] += 1
                    counts["eligible_arrows"] += len(word)
                    counts["equal_magnitudes" if p == q else "opposite_parity" if (p + q) % 2 else "same_parity_unequal"] += 1
                    counts["tied_minimum_cycles"] += len(result["cases"]) > 1
                    for case in result["cases"]:
                        counts[f"case_{case}_minimum_locations"] += 1
                        if case not in examples:
                            examples[case] = {"A": list(A), "B": list(B), "p": p, "q": q,
                                              "word": list(word), **result}
                    digest_record(digest, [list(A), list(B), p, q, result])
    require(set(examples) == {"A", "B", "C", "D"}, "every minimum case represented")
    # A concrete negative-order control and the same cycle at a true odd-scaled addend.
    control_word = (1, 1, 2, 3)
    control_d, control_states = actual_cycle(control_word)
    require(control_d == 47 and control_states == [73, 133, 223, 179], "preserved opposite-parity control")
    scaled_states = [3 * state for state in control_states]
    replay(control_word, 3 * control_d, scaled_states)
    scaled = check_case((1,), (1,), 1, 2, 3 * control_d, scaled_states)
    require(scaled is not None and scaled["normalized_minimum"] == str(F(73, 47)), "normalization retained under scaling")
    fixtures = json.loads(FIXTURES.read_text())
    fixture_arrows = sum(replay(tuple(c["valuations"]), c["d"], c["states"]) for c in fixtures["cycles"])
    require({c["d"] for c in fixtures["cycles"]} == {5, 7, 13, 61}, "actual shared addends")
    return {"block_lengths": [1, 3], "block_letters": [1, 3], "defects": [1, 5],
            "counts": dict(sorted(counts.items())), "examples": examples,
            "case_digest_sha256": digest.hexdigest(), "scaled_control": scaled,
            "shared_fixture_count": len(fixtures["cycles"]), "shared_fixture_arrows": fixture_arrows,
            "fixture_sha256": sha256(FIXTURES.read_bytes()).hexdigest(),
            "scope": "raw rational inequalities keep actual d; no q1 minimum cutoff is imposed on general-d controls"}


def exact_constants():
    require(3**10000 > 2**15849, "lower alpha bound")
    require(393217**200 < 2**3717, "upper kappa bound at local minimum")
    c0, e0 = 2 * K0 - A0 - 1, K0 - A0
    require(c0 == F(5851, 10000) and e0 == F(1, 10000), "fixed ratio constants")
    # Coordinates are N, ell, a-or-b, Delta. Each raw row is strictly positive.
    first_a = (c0, F(1), F(-1), F(0))
    first_b = (e0, F(1), F(-1), F(1, 2))
    rows = {
        "A": (first_a, (e0 - 1, F(1), K0, F(1, 2))),
        "B": (first_b, (F(-1), F(1), K0, F(0))),
        "C": (first_a, (F(-1), F(1), K0, F(0))),
        "D": (first_b, (e0 - 1, F(1), K0, F(1, 2))),
    }
    expected = [F(n, 2000000) for n in (145033, 1999683, 145233, 1999483)]
    coefficients = {}
    for (name, (first, second)), c in zip(rows.items(), expected):
        combined = tuple(K0 * v + w for v, w in zip(first, second))
        require(combined[0] == -c and combined[1] == 1 + K0 and combined[2] == 0,
                "universal positive-multiplier elimination")
        ell_slack, delta_slack = 36 * c - (1 + K0), 7 * c - combined[3]
        require(c > 0 and ell_slack > 0 and delta_slack > 0, "uniform 36/7 coefficient bounds")
        coefficients[name] = {"coefficient": str(c), "delta_coefficient": str(combined[3]),
                              "ell_slack": str(ell_slack), "delta_slack": str(delta_slack)}
    # Reuse the four rows for placement and the two asymmetric cones.
    cA, cB, cC, cD = expected
    require(cB - K0 * (K0 - 1) == cC, "case B total-valuation reduction")
    require(36 * cC > K0 + 1, "both excluded minimum cases give N<36ell")
    cone_slacks = {}
    for name, c in zip(rows, expected):
        delta_coefficient = F(coefficients[name]["delta_coefficient"])
        reduced = c - delta_coefficient / 8
        require(reduced > 0 and 259 * reduced > K0 + 1, "near-equal N<259ell")
        cone_slacks[name] = str(259 * reduced - (K0 + 1))
    reverse_reduced = cD - 3 * (K0 + 1) / 8
    require(reverse_reduced > 0 and 86 * reverse_reduced > K0 + 1, "reverse-order N<86ell")
    require(36 < 259 and 86 < 259, "one common finite closure suffices")
    margin = 2**22 - (133126 + 88578 * 23)
    require(margin == 2023884 and 2**22 > 88578, "dyadic base and increasing increment")
    require(133126 == 259 * 514 and 88578 == 259 * 342, "EXT1 full-clock transfer")
    require(259 * 49 - 1 == 12690 and 259 * 28 - 1 == 7251 and 259 * 26 - 1 == 6733,
            "strict bootstrap integer endpoints")
    require(12690 < 2**14 and 7251 < 2**13, "bootstrap logarithm ranges")
    require(36 * 10 <= 2**9 and 2**10 > 144, "optional logarithm absorption base and derivative criterion")
    return {"A0": str(A0), "K0": str(K0), "c0": str(c0), "e0": str(e0),
            "integer_comparisons": {"three_base": 3, "three_exponent": 10000,
                                    "two_exponent_lower": 15849, "kappa_numerator": 393217,
                                    "kappa_power": 200, "kappa_two_exponent": 3717},
            "four_case_eliminations": coefficients,
            "case_B_after_total_budget": str(cC),
            "near_equal_cone_slacks": cone_slacks,
            "reverse_cone_reduced_coefficient": str(reverse_reduced),
            "reverse_cone_86_slack": str(86 * reverse_reduced - (K0 + 1)),
            "common_finite_closure_coefficient": 259,
            "bootstrap_half_endpoints": [12690, 7251, 6733],
            "half_period_cutoff": 2**22, "full_period_cutoff": 2**23,
            "dyadic_margin_at_22": margin, "dyadic_next_increment_lower": 2**22 - 88578}


def logarithm_bounds(value):
    z = F(value - 1, value + 1)
    lower = 2 * sum((z**(2 * i + 1) / (2 * i + 1) for i in range(80)), F(0))
    upper = lower + 2 * z**161 / (161 * (1 - z * z))
    return lower, upper


def full_even_gap_intervals():
    ln2lo, ln2hi = logarithm_bounds(2)
    ln3lo, ln3hi = logarithm_bounds(3)
    require(ln2lo > F(1, 2), "natural-log gap conversion")
    denominator = 1 << 96
    low_ratio, high_ratio = ln3lo / ln2hi * denominator, ln3hi / ln2lo * denominator
    lo = low_ratio.numerator // low_ratio.denominator
    hi = -(-high_ratio.numerator // high_ratio.denominator)
    require(lo == 125573666586150569315490533898 and hi == lo + 1, "certified dyadic alpha interval")
    low = high = 0
    minimum, minimum_at = denominator, 0
    digest = sha256()
    for N in range(1, 2**22):
        low += 2 * lo
        high += 2 * hi
        floor = low >> 96
        require(high >> 96 == floor, "full-even interval crosses an integer")
        complement = ((floor + 1) << 96) - high
        require(complement > 1 << 71, "positive fractional distance exceeds 2^-25")
        if complement < minimum:
            minimum, minimum_at = complement, N
        digest.update(f"{N}:{floor}:{complement}\n".encode())
    require(minimum == 14746683118183760512442 and minimum_at == 190537, "minimum full-even complement")
    return {"atanh_terms": 80, "tail_first_exponent": 161,
            "alpha_lower_numerator": lo, "alpha_upper_numerator": hi,
            "dyadic_denominator_exponent": 96, "half_length_range": [1, 2**22 - 1],
            "largest_full_even_length": 2**23 - 2, "comparisons": 2**22 - 1,
            "minimum_complement_numerator": minimum, "minimum_at_half_length": minimum_at,
            "fractional_distance_lower_bits": 25, "eta_lower_bits": 27,
            "cases_sha256": digest.hexdigest(),
            "scope": "exact intervals at full exponent 2N; no same-parity or integral half-total assumption"}


def finite_even_bootstrap():
    power = 1
    counts = Counter()
    digest = sha256()
    worst_num, worst_den, worst_at, worst_total = 0, 1, 0, 0
    for N in range(1, 12691):
        power *= 9
        total = power.bit_length()
        binary = 1 << total
        gap = binary - power
        require(gap > 0 and (gap << 14) > binary, "full gap through N12690 exceeds 2^-14")
        counts["eta_fourteen_comparisons"] += 1
        if N <= 7251:
            require((gap << 13) > binary, "full gap through N7251 exceeds 2^-13")
            counts["eta_thirteen_comparisons"] += 1
        if N <= 6733:
            numerator, denominator = 2 * N * binary, 3 * gap
            require(numerator < LOCAL_LIMIT * denominator, "local minimum ceiling for all remaining N")
            counts["minimum_comparisons"] += 1
            if numerator * worst_den > worst_num * denominator:
                worst_num, worst_den, worst_at, worst_total = numerator, denominator, N, total
        digest.update(f"{N}:{total}:{gap.bit_length()}\n".encode())
    ceiling = -(-worst_num // worst_den)
    require(ceiling == 17306923 and worst_at == 6138 and worst_total == 19457, "exact maximum minimum bound")
    require(ceiling < LOCAL_LIMIT, "strict local descent margin")
    return {"counts": dict(sorted(counts.items())), "power": "9^N=3^(2N)",
            "maximum_minimum_bound_ceiling": ceiling, "maximum_at_half_length": worst_at,
            "maximum_full_total_valuation": worst_total,
            "maximum_ratio_hex_sha256": sha256(f"{worst_num:x}/{worst_den:x}".encode()).hexdigest(),
            "cases_sha256": digest.hexdigest(), "local_descent_limit": LOCAL_LIMIT,
            "scope": "minimal positive full gap at each even odd-period length; all larger valuations have larger gaps"}


def local_descent():
    digest = sha256()
    total_steps = maximum_steps = worst_seed = 0
    for seed in range(3, LOCAL_LIMIT, 2):
        state, steps = seed, 0
        while state >= seed:
            raw = 3 * state + 1
            state = raw // (raw & -raw)
            steps += 1
            require(steps <= 10000, "bounded local descent computation")
        require(0 < state < seed and state % 2, "strict lower odd endpoint")
        if steps > maximum_steps:
            maximum_steps, worst_seed = steps, seed
        total_steps += steps
        digest.update(f"{seed}:{state}:{steps}\n".encode())
    require(total_steps == 31421072 and maximum_steps == 181 and worst_seed == 13421671,
            "independent complete descent counts")
    return {"strict_upper_limit": LOCAL_LIMIT, "odd_seeds": LOCAL_LIMIT // 2 - 1,
            "steps": total_steps, "maximum_steps": maximum_steps, "worst_seed": worst_seed,
            "cases_sha256": digest.hexdigest(), "base_state": 1,
            "meaning": "ascending odd-seed induction proves convergence below the limit; even starts reduce automatically"}

def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_imbalance.py [--write-receipt]")
    receipt = {"schema": "half-defect-imbalance-v2", "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
               "normalization": normalization_controls(), "exact_constants": exact_constants(),
               "actual_cycle_controls": actual_controls(),
               "full_even_gap_intervals": full_even_gap_intervals(),
               "finite_even_bootstrap": finite_even_bootstrap(), "local_descent": local_descent()}
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    output = HERE / "check_imbalance.json"
    if sys.argv[1:] == ["--write-receipt"]:
        output.write_text(encoded)
    else:
        require(output.read_text() == encoded, "receipt mismatch; inspect before regenerating")
    print(json.dumps({"status": "pass", "normalization": receipt["normalization"]["counts"],
                      "actual_cycles": receipt["actual_cycle_controls"]["counts"],
                      "local_odd_seeds": receipt["local_descent"]["odd_seeds"],
                      "even_gap_intervals": receipt["full_even_gap_intervals"]["comparisons"],
                      "finite_even_bootstrap": receipt["finite_even_bootstrap"]["counts"]}, sort_keys=True))


if __name__ == "__main__":
    main()
