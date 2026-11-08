"""Exact transfer checks for the second-largest four-mismatch restriction.

Local descent is replayed directly. The controls verify all arc orders, exact
template discrepancies, maximum profiles and integer agreement subintervals.
They preserve the actual 3x+q addend and are not an absence search.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
from math import gcd
from pathlib import Path
import sys

F = Fraction
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def valuation(value):
    require(value != 0, "valuation at zero")
    value = abs(value)
    return (value & -value).bit_length()-1

def continued_fraction_sum(k, m):
    result = 0
    while k:
        quotient, remainder = divmod(m, k)
        result += quotient
        m, k = k, remainder
    return result

def reduced_cycle(word):
    total = intercept = 0
    for letter in word:
        intercept = 3*intercept+2**total
        total += letter
    D = 2**total-3**len(word)
    if D <= 0:
        return None
    divisor = gcd(intercept, D)
    q, state = D//divisor, intercept//divisor
    states = []
    for letter in word:
        require(state > 0 and state % 2 == 1, "positive odd reduced state")
        states.append(state)
        raw = 3*state+q
        require(valuation(raw) == letter, "exact reduced valuation")
        state = raw >> letter
    require(state == states[0] and len(set(states)) == len(word), "primitive reduced closure")
    return q, states

def addend_runs(word, states, q):
    count = 0
    for start in range(len(word)):
        if word[start] != 1 or word[start-1] == 1:
            continue
        length = 0
        while word[(start+length) % len(word)] == 1:
            length += 1
            require(length < len(word), "ones run ends")
        x = states[start]
        e = word[(start+length) % len(word)]
        target = states[(start+length+1) % len(word)]
        require(valuation(x+q) == length+1, "addend-aware start congruence")
        z = (x+q) >> (length+1)
        require(z > 0 and z % 2 == 1 and 2**(e-1)*target == 3**(length+1)*z-q,
                "addend-aware exact ones-run identity")
        count += 1
    return count

def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = runs = 0
    for row in rows:
        word, states, q = row["valuations"], row["states"], row["d"]
        require(q in (5, 7, 13, 61), "standard actual addends")
        for i, letter in enumerate(word):
            raw = 3*states[i]+q
            require(valuation(raw) == letter and raw >> letter == states[(i+1) % len(states)],
                    "standard actual arrow")
            arrows += 1
        runs += addend_runs(word, states, q)
    require(len(rows) == 11 and arrows == 106, "all eleven shared controls")
    return dict(cycles=len(rows), exact_arrows=arrows, addend_ones_runs=runs,
                fixture_sha256=sha256(path.read_bytes()).hexdigest(),
                scope="The true addend is retained; normalized states are not treated as integers.")


def local_descent():
    seeds = steps = maximum_steps = peak = 0
    for initial in range(3, 2**17, 2):
        state, count = initial, 0
        while state >= initial:
            raw = 3*state+1
            state = raw >> valuation(raw)
            count += 1
            require(count < 10000, "local descent must terminate within the checked finite allowance")
            peak = max(peak, state)
        seeds += 1
        steps += count
        maximum_steps = max(maximum_steps, count)
    require(seeds == 65535, "every odd seed below 2^17 except one")
    return dict(odd_seeds=seeds, odd_steps=steps, maximum_steps=maximum_steps,
                maximum_odd_output=peak, bound_exclusive=2**17,
                scope="Every listed seed reaches a smaller positive odd value; no outside convergence computation.")


def constants():
    require(388**5 < 2**8*129**5 and 3**32 < 2**51 and 3**80 < 2**127,
            "mean and exact alpha bounds")
    require(2**3 < 3**2, "alpha greater than three halves")
    rise_base = F(49, 2064)*2**22 - (11*(172+342*23)+11)
    require(rise_base > 0, "maximum forcing at the first dyadic band")
    # For all j>=22, the positive affine right side at j+1 is less
    # than twice its value at j, while the left side exactly doubles.
    require(11*(172+342*24)+11 < 2*(11*(172+342*23)+11),
            "positive affine induction for maximum forcing")
    multiplicity_margin = 39*(F(2**22, 64)-1)-F(3, 5)*2**22
    require(multiplicity_margin == F(196413, 5) > 0 and F(39, 64) > F(3, 5),
            "uniform maximum count at most 38")
    profile_coefficient = 1-F(257, 258)*F(80, 127)
    spread_margin = F(1, 4)-F(2, 3)*profile_coefficient
    require(profile_coefficient == F(6103, 16383) and spread_margin == F(325, 196596),
            "spread-profile coefficient and margin")
    threshold = F(1, 1216)
    require(spread_margin > threshold and F(1, 1000) > threshold,
            "both spread and singleton cases cover the common threshold")
    cluster_rows = []
    for d in range(2, 39):
        require(F(1, 32*d) >= threshold, "every clustered multiplicity covers the threshold")
        cluster_rows.append(dict(multiplicity=d, error_lower=str(F(1, 32*d))))
    c0 = F(3, 2)*(threshold-F(1, 393216))
    require(c0 == F(6125, 4980736), "uniform error absorption")
    require(54+64*342 == 21942 and 27+64*173 == 11099,
            "continued-fraction coefficient extraction")
    require(2*21942 == 43884 and 2*(11099-1) == 22196 and 173+2 == 175,
            "exact explicit second-largest bound coefficients")
    simple_base = c0*2**23-(517+342*24)
    require(simple_base == F(30225, 19) > 0, "height absorbed at m=2^24")
    require(517+342*25 < 2*(517+342*24), "positive affine all-band induction")
    require(F(21942)+F(11098, 24) < 2**15 and c0 > F(1, 1024),
            "clean logarithmic denominator estimates")
    require(4*2**15*1024 == 2**27, "clean second-largest constant")
    return dict(rise_dyadic_margin=str(rise_base), multiplicity_margin=str(multiplicity_margin),
                maximum_multiplicity_upper=38, spread_margin=str(spread_margin),
                singleton_margin="1/1000", clustered_margins=cluster_rows,
                common_error_threshold=str(threshold), drift_error_upper="1/393216",
                linear_coefficient=str(c0),
                exact_U_bound=dict(numerator="(6125/4980736)*m-175-342*log2(m)",
                                   denominator="43884*log2(m)+22196", period_lower=2**22),
                simple_dyadic_margin=str(simple_base), simple_period_lower=2**24,
                simple_U_denominator_constant=2**27,
                combined_high_count_log_coefficient=str(F(3, 5)*2**27),
                scope="Necessary conditions under EXT1 only; no period or convergence import and no global cycle exclusion.")


def compositions(m):
    for d in range(1, m-2):
        for a in range(1, m-d-1):
            for b in range(1, m-d-a):
                yield d, a, b, m-d-a-b


def word_controls():
    # Fix V first, then permute the other three labels: all six cyclic orders.
    specs = [(m, lengths) for m in range(4, 11) for lengths in compositions(m)]
    # Larger denominator controls exercise all eleven nonidentity rotations
    # in the singleton branch, without a large composition census.
    specs += [(m, lengths) for m in (13, 17, 19)
              for lengths in ((1, 1, 1, m-3), (1, 2, 3, m-6), (2, 1, 2, m-5))]
    label_sets = [(1, 2, 3, 5), (1, 3, 7, 16), (1, 7, 16, 31)]
    geometries = cycles = arrows = runs = agreement_runs = factors = 0
    maximum_cases = dict(singleton=0, clustered=0, spread=0)
    cyclic_orders = {order: 0 for order in permutations(range(3))}
    generic_singletons = 0
    digest = sha256()
    for m, lengths in specs:
        d = lengths[0]
        for h in range(1, m):
            if gcd(h, m) != 1:
                continue
            step = min(h, m-h)
            K = continued_fraction_sum(pow(step, -1, m), m)
            for labels in label_sets:
                _, t, U, V = labels
                for order in cyclic_orders:
                    track_labels = (V,)+tuple(labels[j] for j in order)
                    track = [label for label, length in zip(track_labels, lengths) for _ in range(length)]
                    word = [0]*m
                    for i, label in enumerate(track):
                        word[i*h % m] = label
                    geometries += 1
                    cyclic_orders[order] += 1
                    require(all(any(word[i] != word[(i+s) % m] for i in range(m))
                                for s in range(1, m)), "single maximum arc gives primitivity")
                    cuts = {i for i in range(m) if word[i] != word[(i+step) % m]}
                    require(len(cuts) == 4, "exactly four mismatches")
                    variation = sum(abs(word[i]-word[(i+step) % m]) for i in range(m))
                    require(variation < 4*V, "all-order total variation bound")
                    template = [t if letter == V else letter for letter in word]
                    require(all(template[i] == t-(t-1)*(word[i] == 1)+(U-t)*(word[i] == U)
                                for i in range(m)), "all-order indicator decomposition")
                    template_variation = sum(abs(template[i]-template[(i+step) % m]) for i in range(m))
                    require(template_variation == 2*(U-1), "all six cyclic orders have exact template variation")
                    prefix = 0
                    deviations = []
                    for i, letter in enumerate(template):
                        deviations.append(m*prefix-sum(template)*i)
                        prefix += letter
                    require(max(deviations)-min(deviations) <= 2*m*(U-1)*(K-1),
                            "all-factor discrepancy from prefix span")
                    factors += m*(m-1)
                    maxima = {i for i, letter in enumerate(word) if letter == V}
                    last = next(i for i in maxima if (i+step) % m not in maxima)
                    expected = {(last-j*step) % m for j in range(d)}
                    require(maxima == expected, "contiguous maximum orbit segment after reversal")
                    fixed_cuts = {last, (last-d*step) % m}
                    require(fixed_cuts <= cuts and len(cuts-fixed_cuts) == 2,
                            "maximum endpoints and two arbitrary other cuts")
                    coords = [F(((i+1)-(last+1)-1) % m+1, m) for i in range(m)]
                    positions = {coords[i] for i in maxima}
                    Fd = [d*e-sum(p < e for p in positions) for e in coords]
                    for i in range(m):
                        require(Fd[(i+1) % m]-Fd[i] == F(d, m)-(i in maxima),
                                "pre-drop (i+1)/m profile increment, including wrap")
                    if d == 1:
                        maximum_cases["singleton"] += 1
                        require(all(x == e for x, e in zip(Fd, coords)), "singleton sawtooth has pre-drop one")
                        generic_singletons += m > 12
                    elif d*step < m:
                        maximum_cases["clustered"] += 1
                    else:
                        maximum_cases["spread"] += 1
                    cycle = reduced_cycle(word)
                    if cycle is None:
                        continue
                    q, states = cycle
                    cycles += 1
                    arrows += m
                    runs += addend_runs(word, states, q)
                    for j in range(1, min(11, m-1)+1):
                        refined = {((i-k*step) % m) for i in cuts for k in range(j)}
                        actual = {i for i in range(m) if word[i] != word[(i+j*step) % m]}
                        require(actual <= refined, "raw cuts refine every higher mismatch set")
                        ordered = sorted(refined)
                        for position, endpoint in enumerate(ordered):
                            previous = ordered[position-1]
                            gap = (endpoint-previous) % m
                            length = gap-1
                            for k in range(1, gap):
                                i = (previous+k) % m
                                require(word[i] == word[(i+j*step) % m], "artificial-gap agreement")
                            other = (endpoint+j*step) % m
                            require(abs(states[endpoint]-states[other]) % (2*3**length) == 0,
                                    "integer paired difference on an agreement subinterval")
                            require(max(states[endpoint], states[other]) > 2*3**length,
                                    "actual addend retained in the endpoint witness")
                            agreement_runs += 1
                    digest.update((repr((word, q, states))+"\n").encode())
    require(all(maximum_cases.values()) and all(cyclic_orders.values()) and generic_singletons > 0,
            "all arc orders and profile regimes tested")
    return dict(word_geometries=geometries, exact_cycles=cycles, exact_arrows=arrows,
                integral_ones_runs=runs, agreement_subintervals=agreement_runs,
                proper_factors_covered=factors, maximum_cases=maximum_cases,
                generic_denominator_singletons=generic_singletons,
                cyclic_orders={str(k): v for k, v in cyclic_orders.items()},
                digest_sha256=digest.hexdigest(), label_sets=label_sets,
                scope="All positive four-part compositions at m=4..10, plus three stated length patterns at m13,17,19; all coprime h, six cyclic orders and three label sets.",
                extra_patterns="(1,1,1,m-3), (1,2,3,m-6), (2,1,2,m-5)",
                normalization="Each positive-D word is an actual reduced 3x+q cycle; none is silently normalized to an integer 3x+1 cycle.")


def build():
    return dict(constants=constants(), local_descent=local_descent(),
                word_controls=word_controls(), standard_controls=standard_controls())

if __name__ == "__main__":
    data = build()
    path = HERE/"check_second_largest.json"
    text = json.dumps(data, indent=2, sort_keys=True)+"\n"
    if "--write" in sys.argv:
        path.write_text(text)
    else:
        require(path.read_text() == text, "generated receipt differs")
    print("PASS: exact second-largest and high-count bounds; all-order addend-aware controls")
