"""Exact finite closure and controls for the sparse first-segment theorem."""

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 20
LOCAL_LIMIT = 1 << 17
MAX_HALF_LENGTH = 431
DESCENT_GUARD = 100000


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value):
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def intercept(word):
    result = total = 0
    for letter in word:
        require(letter >= 1, "positive valuation")
        result = 3*result+(1 << total)
        total += letter
    return result


def trace(start, addend, word):
    states = [start]
    for letter in word:
        require(states[-1] != 0 and states[-1] % 2 == 1, "nonzero odd input")
        raw = 3*states[-1]+addend
        require(raw != 0 and valuation(raw) == letter, "exact valuation")
        states.append(raw >> letter)
    require(states[-1] != 0 and states[-1] % 2 == 1, "nonzero odd endpoint")
    return states


def log_enclosure(value, terms):
    z = Fraction(value-1, value+1)
    low = 2*sum((z**(2*j+1)/(2*j+1) for j in range(terms)), Fraction())
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return low, low+tail


def constants():
    low2, high2 = log_enclosure(2, 32)
    low3, high3 = log_enclosure(3, 32)
    require(Fraction(1, 2) < low2 < high2 < 1, "bounds for ln2")
    require(0 < low3 < high3 < 2, "bounds for ln3")
    require(2**3 < 3**2 and 3**5 < 2**8, "three halves < alpha < eight fifths")
    require(Fraction(1217, 25)/low2 < 98, "LMN binary coefficient")
    require(Fraction(8, 5)/2+1 < 2, "LMN b-prime bound")
    minimum_margin = 2**8*35**5-106**5
    require(minimum_margin == 63344224 > 0, "minimum-35 product estimate")
    require(Fraction(8, 5)+1 < 3 and 2*Fraction(8, 5)+2 < 6,
            "small-n case length constants")
    require((3*Fraction(8, 5)+1)/Fraction(2, 5) == Fraction(29, 2),
            "amplitude cancellation slope")
    require((6*Fraction(8, 5)+1)/Fraction(2, 5) == Fraction(53, 2),
            "amplitude cancellation constant")
    require(Fraction(29, 2) < 15 and Fraction(53, 2) < 27,
            "conservative length bound")
    H = 1+98*22**2
    upper = 15*H+27
    derivative = 15*392*22
    require(H == 47433 and upper == 711522 < CUTOFF, "LMN cutoff")
    require(derivative < CUTOFF and 1/low2 < 22, "increasing cutoff difference")
    require(15*27+27-1 == MAX_HALF_LENGTH, "strict finite half-length cutoff")
    rows = []
    for seed in range(3, 34, 2):
        states = [seed]
        while states[-1] != 1:
            require(len(states) < DESCENT_GUARD, "unfinished minimum-35 trajectory")
            raw = 3*states[-1]+1
            states.append(raw >> valuation(raw))
        rows.append(dict(seed=seed, states=states))
    require(len(rows) == 16, "minimum-35 seed coverage")
    return dict(minimum_state=35, minimum_product_margin=minimum_margin,
                small_seed_trajectories=rows, logarithm_series_terms=32,
                ln2_bounds=[str(low2), str(high2)], ln3_bounds=[str(low3), str(high3)],
                lmn_coefficient="1217/25", logarithmic_heights=[1, 2],
                binary_gap_coefficient=98, half_length_cutoff=CUTOFF,
                H_at_cutoff=H, upper_at_cutoff=upper, cutoff_margin=CUTOFF-upper,
                derivative_margin_times_cutoff=CUTOFF-derivative,
                half_length_after_fractional_gaps=MAX_HALF_LENGTH,
                length_coefficients=["29/2", "53/2"],
                conservative_length_coefficients=[15, 27])


def fractional_gaps():
    low2, high2 = log_enclosure(2, 80)
    low3, high3 = log_enclosure(3, 80)
    low, high = low3/high2, high3/low2
    scale = 1 << 96
    lo, hi = (low*scale).__floor__(), (high*scale).__ceil__()
    require(Fraction(lo, scale) <= low < high <= Fraction(hi, scale),
            "outward alpha enclosure")
    require(hi == lo+1, "adjacent dyadic endpoints")
    lower = upper = 0
    minimum, minimum_at = scale, 0
    for k in range(1, CUTOFF):
        lower += lo
        upper += hi
        floor = lower >> 96
        require(upper >> 96 == floor, "alpha interval crosses an integer")
        complement = scale-(upper-(floor << 96))
        require(complement > 1 << 71, "positive fractional gap")
        if complement < minimum:
            minimum, minimum_at = complement, k
    require(minimum_at == 190537, "fractional minimum location")
    return dict(series_terms=80, dyadic_denominator_bits=96,
                alpha_lower_numerator=lo, alpha_upper_numerator=hi,
                checked_exponents=CUTOFF-1, exponents=[1, CUTOFF-1],
                threshold_numerator=1 << 71, fractional_distance_bits=25,
                natural_log_gap_bits=26, eta_bits=27,
                minimum_complement_numerator=minimum, minimum_complement_at=minimum_at)


def finite_minimum():
    maximum, maximum_at, maximum_total = Fraction(), 0, 0
    checksum = sha256()
    three = 1
    for m in range(1, MAX_HALF_LENGTH+1):
        three *= 3
        S = three.bit_length()
        two = 1 << S
        gap = two-three
        require(3*LOCAL_LIMIT*gap > m*two, "finite minimum-state comparison")
        bound = Fraction(m*two, 3*gap)
        if bound > maximum:
            maximum, maximum_at, maximum_total = bound, m, S
        checksum.update(f"{m}:{S}:{gap:x}\n".encode())
    require(maximum.__ceil__() == 99832 < LOCAL_LIMIT and maximum_at == 306,
            "finite minimum maximum")
    return dict(exponents=[1, MAX_HALF_LENGTH], comparisons=MAX_HALF_LENGTH,
                exact_gap_sha256=checksum.hexdigest(), maximum_bound=str(maximum),
                maximum_at=maximum_at, maximum_total=maximum_total,
                maximum_bound_ceiling=maximum.__ceil__(), local_limit_exclusive=LOCAL_LIMIT)


def local_descent():
    count = steps = longest = longest_seed = 0
    peak = 1
    for seed in range(3, LOCAL_LIMIT, 2):
        current, used = seed, 0
        while current >= seed:
            require(used < DESCENT_GUARD, "unfinished local descent")
            raw = 3*current+1
            current = raw >> valuation(raw)
            require(current > 0 and current % 2 == 1, "positive odd descent cut")
            peak = max(peak, current)
            used += 1
        count += 1
        steps += used
        if used > longest:
            longest, longest_seed = used, seed
    require(count == LOCAL_LIMIT//2-1, "complete local seed coverage")
    return dict(limit_exclusive=LOCAL_LIMIT, odd_seeds=count, odd_steps=steps,
                maximum_local_steps=longest, first_longest_seed=longest_seed,
                peak_odd_output=peak, per_seed_guard=DESCENT_GUARD,
                conclusion="Each odd seed 3<=s<limit reaches a smaller positive odd seed")


def cylinder_start(word):
    total, C = sum(word), intercept(word)
    modulus = 1 << (total+1)
    start = ((1 << total)-C)*pow(3**len(word), -1, modulus) % modulus
    require(start > 0 and start % 2 == 1, "positive exact cylinder representative")
    return start


def prefix_checks():
    # These are actual finite 3x+1 prefixes, not complete signed joins or cycles.
    # K is chosen to satisfy the one inequality used in the two-case argument.
    count = all_ones = first_defect = last_defect = single_letter = 0
    branches = dict(large_n=0, small_n=0)
    arrows = 0
    for u in range(7):
        for w in range(7):
            for e in tuple(range(1, 9))+(16, 27, 64):
                A = (1,)*u+(e+1,)+(1,)*w
                a, n = len(A), u+1
                C = intercept(A)
                ratio = Fraction(C, 3**a)
                formula = 1+((1 << e)-1)*Fraction(2, 3)**n-(1 << e)*Fraction(2, 3)**a
                require(ratio == formula, "one-defect intercept identity")
                for p in (1, 3):
                    modified = A[:-1]+(A[-1]+p,)
                    x = cylinder_start(modified)
                    states = trace(x, 1, modified)
                    ordinary_end = Fraction(3**a*x+C, 1 << sum(A))
                    require(ordinary_end == (1 << p)*states[-1] and ordinary_end % 2 == 0,
                            "even ordinary terminal state")
                    require((x+1) % (1 << n) == 0, "initial run divisibility")
                    t = (x+1) >> n
                    require(t >= 1 and valuation(x+1) == n, "positive initial quotient")
                    U = 3**n*t
                    y = Fraction(U-1, 1 << e)
                    require(y.denominator == 1 and y > 0 and valuation(y.numerator+1) == w,
                            "exact terminal-run valuation")
                    require(Fraction(3, 2)**w*(y+1)-1 == ordinary_end,
                            "ordinary terminal run")
                    require((1 << w) <= y+1, "terminal-run lower bound")
                    K = 2+2*x/ratio
                    require(K > 1 and x < (K-1)*ratio, "abstract enclosure comparison")
                    require(x+1 < K*(1+(1 << e)*Fraction(2, 3)**n),
                            "shifted-state bound")
                    require(U < K*Fraction(3, 2)**n+K*(1 << e), "two-case input")
                    if (1 << n) >= 2*K:
                        require(U < 2*K*(1 << e) and y+1 < 2*K+1 < 3*K,
                                "large-n case")
                        branches["large_n"] += 1
                    else:
                        require(y+1 < 2*K*Fraction(3, 2)**n, "small-n case")
                        branches["small_n"] += 1
                    first_defect += u == 0
                    last_defect += w == 0
                    single_letter += u == w == 0
                    arrows += a
                    count += 1
    for a in range(1, 13):
        A = (1,)*a
        ratio = Fraction(intercept(A), 3**a)
        require(ratio == 1-Fraction(2, 3)**a, "all-ones intercept")
        for p in (1, 3):
            modified = A[:-1]+(1+p,)
            x = cylinder_start(modified)
            states = trace(x, 1, modified)
            ordinary_end = Fraction(3**a*x+intercept(A), 1 << a)
            require(ordinary_end == (1 << p)*states[-1] and ordinary_end % 2 == 0,
                    "all-ones ordinary even output")
            K = 2+2*x/ratio
            require(valuation(x+1) == a and (1 << a) <= x+1 < K,
                    "all-ones terminal correction")
            all_ones += 1
            arrows += a
    require(all(branches.values()), "both cases exercised")
    return dict(scope="Finite exact 3x+1 prefixes with a chosen enclosure constant; not signed joins",
                u_range=[0, 6], w_range=[0, 6], defect_excesses=list(range(1, 9))+[16, 27, 64],
                terminal_raises=[1, 3], one_defect_prefixes=count, all_ones_prefixes=all_ones,
                first_position_defects=first_defect, last_position_defects=last_defect,
                single_letter_defects=single_letter, branches=branches, exact_arrows=arrows)


def genuine_joins():
    path = ROOT / "areas/cycles/results/bounded-unequal-half-defect-exclusion/check_bounded_halves.json"
    selected = [row for row in json.loads(path.read_text())["joins"]
                if row["order"] == "LH" and sum(v > 1 for v in row["A"]) <= 1]
    require(len(selected) == 5, "specified genuine controls")
    rows = []
    for row in selected:
        J, r, h = row["J"], row["r"], row["h"]
        A, B = tuple(row["A"]), tuple(row["B"])
        N, M = 1 << J, 1 << r
        z = trace(-h, M-1, A)[-1]
        require(z > 0 and trace(z, N-1, B)[-1] == h, "signed auxiliary paths")
        require(J > r >= 1 and B[-1] > J, "boundary hypotheses")
        uword, vword = list(A+B), list(A+B)
        uword[len(A)-1] += J-r
        uword[-1] -= J
        vword[-1] += r
        word = uword+vword
        a, b, P, T = len(A), len(B), sum(A), sum(B)
        m, S = a+b, P+T
        require(len(word) == 2*m and sum(word) == 2*S, "reconstructed totals")
        C, D = intercept(word), (1 << (2*S))-3**(2*m)
        require(D > 0, "positive cycle denominator")
        q, x = D//gcd(C, D), Fraction(C, D)
        X = q*x
        require(X.denominator == 1 and X.numerator % 2 == 1 and q % 2 == 1,
                "integer reduced cycle")
        states = trace(X.numerator, q, word)
        require(states[-1] == X and min(states) > 0, "positive reduced cycle closure")
        require(Fraction(states[m], q) == M*x+h, "canonical half closure")
        require(Fraction(row["canonical_state"]) == x, "source control state")
        lam = Fraction(3**m, 1 << S)
        eta = 1-lam
        kappa = (lam+Fraction(1, M))/eta
        require(x < kappa*Fraction(intercept(A), 3**a), "rational enclosure")
        defect = next(i for i, value in enumerate(A) if value > 1)
        n, e, w = defect+1, A[defect]-1, a-defect-1
        require((X.numerator+q) % (1 << n) == 0, "q-scaled initial divisibility")
        t = (X.numerator+q) >> n
        y = Fraction(3**n*t-q, 1 << e)
        require(y.denominator == 1 and valuation(y.numerator+q) == w,
                "q-scaled terminal-run parity")
        require(Fraction(3**a*X.numerator+q*intercept(A), 1 << P)
                == (1 << (J-r))*states[a], "actual even ordinary output")
        require(q > 1, "genuine control fails denominator-one hypothesis")
        rows.append(dict(J=J, r=r, h=h, interface=z, A=list(A), B=list(B),
                         half_length=m, half_total=S, normalized_state=str(x), denominator=q,
                         actual_start=X.numerator, actual_minimum=min(states),
                         arrows=len(word), failed_hypothesis="q=1"))
    require({41, 4069}.issubset(row["denominator"] for row in rows), "named controls")
    return dict(source_receipt_sha256=sha256(path.read_bytes()).hexdigest(), count=len(rows),
                arrows=sum(row["arrows"] for row in rows), records=rows,
                scope="Specified genuine signed joins, not an absence census")


def standard_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows, arrows = [], 0
    for row in json.loads(path.read_text())["cycles"]:
        d, states, word = row["d"], row["states"], row["valuations"]
        require(trace(states[0], d, word) == states+[states[0]], "standard control arrows")
        C, D = intercept(word), (1 << sum(word))-3**len(word)
        q = D//gcd(C, D)
        require(D > 0 and Fraction(C, D) == Fraction(states[0], d), "control cycle equation")
        require(q > 1 and d % q == 0, "control retains denominator")
        rows.append(dict(addend=d, odd_period=len(word), denominator=q,
                         failed_hypothesis="q=1"))
        arrows += len(word)
    require(len(rows) == 11 and {row["addend"] for row in rows} == {5, 7, 13, 61},
            "all standard fixtures")
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), count=len(rows),
                arrows=arrows, records=rows)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="one-defect-first-block-v1", constants=constants(),
                   finite_prefixes=prefix_checks(), genuine_joins=genuine_joins(),
                   fractional_gaps=fractional_gaps(), finite_minimum=finite_minimum(),
                   local_descent=local_descent(), standard_controls=standard_controls())
    target = HERE / "check_one_defect.json"
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", finite_prefixes=receipt["finite_prefixes"]["one_defect_prefixes"]
                          +receipt["finite_prefixes"]["all_ones_prefixes"],
                          genuine_joins=receipt["genuine_joins"]["count"],
                          fractional_intervals=CUTOFF-1, minimum_comparisons=MAX_HALF_LENGTH,
                          local_odd_seeds=receipt["local_descent"]["odd_seeds"],
                          standard_cycles=receipt["standard_controls"]["count"]), sort_keys=True))


if __name__ == "__main__":
    main()
