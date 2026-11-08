"""Exact continuant, threshold and cycle-control checks; standard library only."""

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from math import comb, gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ARITHMETIC_CUTOFF = 1 << 34
PERIOD_CUTOFF_BITS = 1536


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def continuant(coefficients):
    previous, current = 0, 1
    for coefficient in coefficients:
        require(coefficient >= 1, "positive continued-fraction coefficient")
        previous, current = current, coefficient*current+previous
    return current


def convergents(coefficients):
    old_p, p, old_q, q = 1, 0, 0, 1
    rows = [(p, q)]
    for coefficient in coefficients:
        old_p, p = p, coefficient*p+old_p
        old_q, q = q, coefficient*q+old_q
        rows.append((p, q))
    return rows


def coefficients_of(k, m):
    require(0 < k < m and gcd(k, m) == 1, "reduced rational in (0,1)")
    answer = []
    while k:
        coefficient, remainder = divmod(m, k)
        answer.append(coefficient)
        m, k = k, remainder
    require(answer and answer[-1] >= 2, "canonical last coefficient")
    return tuple(answer)


def check_list(coefficients):
    require(coefficients and coefficients[-1] >= 2, "canonical continued fraction")
    rows = convergents(coefficients)
    k, m = rows[-1]
    require(0 < k < m and gcd(k, m) == 1, "convergent reducedness")
    require(coefficients_of(k, m) == coefficients, "canonical round trip")
    require(m == continuant(coefficients) and k == continuant(coefficients[1:]),
            "full numerator and denominator")
    require(m >= sum(coefficients), "coefficient-sum bound")
    require(m >= 1 << (len(coefficients)//2), "length bound")
    full_product = 1
    for coefficient in coefficients:
        full_product *= coefficient
    require(m >= full_product, "full-product monomial bound")
    for i, coefficient in enumerate(coefficients):
        for j, other in enumerate(coefficients):
            if i != j:
                require(m >= coefficient*other, "distinct coefficient-product bound")
        p, Q = rows[i]
        old_p, old_Q = rows[i-1] if i else (1, 0)
        R = continuant(coefficients[i+1:])
        F = continuant(coefficients[i:])
        require(m == Q*F+old_Q*R and k == p*F+old_p*R, "complete-tail decomposition")
        require(Q*old_p-p*old_Q == (-1)**i, "convergent determinant sign")
        require(Q*k-p*m == (-1)**i*R, "exact signed residue")
        require(m >= coefficient*Q*R, "large-coefficient product bound")
        require(sum(coefficients)-coefficient <= Q+R, "prefix and tail sums")
    return k, m, rows


def continuant_grid():
    lists = splits = first = last = single = 0
    checksum = sha256()
    for length in range(1, 8):
        for coefficients in product(range(1, 6), repeat=length):
            if coefficients[-1] < 2:
                continue
            k, m, rows = check_list(coefficients)
            checksum.update(f"{coefficients}:{k}:{m}\n".encode())
            lists += 1
            splits += length
            first += 1
            last += 1
            single += length == 1
    require(lists == 78124 and splits == 527344, "complete coefficient grid")
    return dict(lengths=[1, 7], coefficients=[1, 5], canonical_last_at_least=2,
                lists=lists, coefficient_splits=splits, first_coefficient_cases=first,
                last_coefficient_cases=last, single_coefficient_cases=single,
                exact_grid_sha256=checksum.hexdigest())


def large_coefficient_cases():
    pieces = [()]
    for length in range(1, 4):
        pieces.extend(product(range(1, 4), repeat=length))
    cases = []
    for prefix in pieces:
        for tail in pieces:
            if tail and tail[-1] == 1:
                continue
            Q, R = continuant(prefix), continuant(tail)
            smallest = max(2, (ARITHMETIC_CUTOFF+Q*R-1)//(Q*R))
            for large in (smallest, 1 << 40, 1 << 80):
                cases.append((tuple(prefix)+(large,)+tuple(tail), len(prefix)))
    for large in (1 << 34, 1 << 40, 1 << 80):
        for coefficients, index in [((large, 512), 0), ((512, large), 1),
                                    ((large, 2, 255), 0), ((2, large, 256), 1)]:
            cases.append((coefficients, index))
    qualifying = outside = first = last = single = 0
    max_j = max_Q = max_product = 0
    checksum = sha256()
    edges = []
    for coefficients, index in cases:
        k, m, rows = check_list(coefficients)
        require(m >= ARITHMETIC_CUTOFF, "large-case denominator range")
        if 512*sum(coefficients) < m:
            outside += 1
            continue
        coefficient = coefficients[index]
        require(coefficient == max(coefficients) and 1024*coefficient >= m,
                "extracted large coefficient")
        p, Q = rows[index]
        j = continuant(coefficients[index+1:])
        require(Q*j <= 1024 and sum(coefficients)-coefficient <= 1025,
                "first product and remaining-sum bounds")
        require(Q*j <= 512, "sharpened product")
        h = pow(k, -1, m)
        residue = j*h % m
        require(min(residue, m-residue) == Q and 0 < 2*Q < m,
                "short inverse multiple")
        require(1 <= j <= 512 and 1 <= Q <= 512 and 4*j <= 2048,
                "uniform multiplier and mismatch ceiling")
        checksum.update(f"{coefficients}:{k}:{m}:{j}:{Q}:{residue}\n".encode())
        qualifying += 1
        first += index == 0
        last += index == len(coefficients)-1
        single += len(coefficients) == 1
        max_j, max_Q, max_product = max(max_j, j), max(max_Q, Q), max(max_product, j*Q)
        if coefficient == 1 << 34 and coefficients in ((1 << 34, 512), (512, 1 << 34),
                                                      (1 << 34, 2, 255), (2, 1 << 34, 256)):
            edges.append(dict(coefficients=list(coefficients), numerator=k, denominator=m,
                              inverse=h, multiplier=j, short_distance=Q, product=j*Q))
    require(qualifying > 0 and first > 0 and last > 0 and single > 0,
            "large cases include both ends and singleton")
    require(max_j == max_Q == max_product == 512, "sharp product-edge examples")
    return dict(scope="Specified arithmetic examples, not a cycle census", total_cases=len(cases),
                qualifying_cases=qualifying, outside_complexity_hypothesis=outside,
                first_coefficient_cases=first, last_coefficient_cases=last,
                single_coefficient_cases=single, maximum_multiplier=max_j,
                maximum_distance=max_Q, maximum_product=max_product,
                exact_cases_sha256=checksum.hexdigest(), edge_examples=edges)


def poly_add(*polys):
    result = [0]*max(map(len, polys))
    for poly in polys:
        for i, coefficient in enumerate(poly):
            result[i] += coefficient
    while result and result[-1] == 0:
        result.pop()
    return result


def poly_mul(first, second):
    result = [0]*(len(first)+len(second)-1)
    for i, a in enumerate(first):
        for j, b in enumerate(second):
            result[i+j] += a*b
    return result


def poly_scale(value, poly):
    return [value*x for x in poly]


def poly_shift(poly, shift):
    result = [0]*len(poly)
    for degree, coefficient in enumerate(poly):
        for j in range(degree+1):
            result[j] += coefficient*comb(degree, j)*shift**(degree-j)
    return result


def constants():
    # Polynomial identities, followed by nonnegative coefficients after shifting
    # to the cutoff, certify both infinite dyadic inductions.
    first_difference = poly_add(poly_scale(2, poly_mul([2, 2], [1, 2])),
                                poly_scale(-1, poly_mul([4, 2], [3, 2])))
    require(first_difference == [-8, -2, 4], "first induction polynomial")
    first_shift = poly_shift(first_difference, 34)
    require(first_shift == [4548, 270, 4] and all(c >= 0 for c in first_shift),
            "positive first induction for every d>=34")
    first_margin = ARITHMETIC_CUTOFF-(1 << 19)*70*69
    require(first_margin > 0, "first dyadic base")
    product_contradiction = 512*513*1025
    require(product_contradiction == 269222400 < ARITHMETIC_CUTOFF, "512 product cutoff")
    require(3**2 > 2**3 and 3**32 < 2**51, "bounds for alpha")
    require(Fraction(2, 3) > Fraction(1, 2), "first atanh term proves ln2>1/2")
    require(Fraction(2, 387) < Fraction(1, 160), "minimum-129 drift constant")
    require(Fraction(51, 32)+Fraction(1, 160) == Fraction(8, 5), "rise factor")
    require(2**23 < 5**10 and 7*2049 < 10*1435, "rise power below 2^1435")
    require(1+Fraction(3, 5)*512 < 309, "short-offset intercept")
    require(Fraction(2*2048, 3) < 1 << 11, "end-witness multiplier")
    require(1435+11 == 1446 and 172+309 == 481 and 481+342 == 823,
            "combined height constants")
    second_difference = poly_add(poly_scale(2, [823, 342]),
                                 poly_scale(-1, poly_shift([823, 342], 1)))
    require(second_difference == [481, 342], "second induction polynomial")
    second_shift = poly_shift(second_difference, PERIOD_CUTOFF_BITS)
    require(all(c > 0 for c in second_shift), "positive second induction")
    dyadic_base = 823+342*PERIOD_CUTOFF_BITS
    require(dyadic_base == 526135 < 1 << 20 and 1446+20 < PERIOD_CUTOFF_BITS,
            "period cutoff base")
    return dict(arithmetic_cutoff_bits=34, maximum_initial_product=1024,
                maximum_final_product=512, first_dyadic_base_margin=first_margin,
                first_induction_polynomial=first_difference,
                first_induction_shifted_coefficients=first_shift,
                sharpened_product_contradiction_bound=product_contradiction,
                alpha_upper="51/32", minimum_state=129, rise_factor_upper="8/5",
                maximum_short_rotation_mismatches=2048, rise_exponent=2049,
                rise_power_upper_bits=1435, combined_upper_bits=1446,
                combined_height_polynomial=[481, 342], period_cutoff_bits=PERIOD_CUTOFF_BITS,
                second_induction_polynomial=second_difference,
                second_induction_shifted_coefficients=second_shift,
                final_dyadic_base_polynomial=dyadic_base,
                final_dyadic_base_upper_bits=1466)


def valuation(value):
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length()-1


def general_growth_constants():
    cutoff_bits = 40
    # All inequalities below are exact; the shifted coefficient signs
    # certify every subsequent dyadic band, not just sampled lengths.
    dominance = poly_mul(poly_mul(poly_mul([1, 1], [1, 1]), [1, 1]), [1, 2])
    dominance_difference = poly_add(poly_scale(2, dominance),
                                    poly_scale(-1, poly_shift(dominance, 1)))
    dominance_shift = poly_shift(dominance_difference, cutoff_bits)
    require(dominance == [1, 5, 9, 7, 2], "coefficient dominance polynomial")
    require(dominance_shift == [5015898, 505238, 19056, 319, 2]
            and all(x > 0 for x in dominance_shift), "all-band dominance induction")
    dominance_margin = (1 << cutoff_bits)-41**3*81
    require(dominance_margin == 1099506045175 > 0, "coefficient dominance base")

    minimum_k = poly_scale(2, poly_mul([1, 1], [2, 1]))
    minimum_k_difference = poly_add(poly_scale(2, minimum_k),
                                    poly_scale(-1, poly_shift(minimum_k, 1)))
    minimum_k_shift = poly_shift(minimum_k_difference, cutoff_bits)
    require(minimum_k_shift == [3276, 162, 2] and all(x > 0 for x in minimum_k_shift),
            "all-band K>=4(x+1) induction")
    minimum_k_margin = (1 << cutoff_bits)-2*41*42
    require(minimum_k_margin == 1099511624332 > 0, "K>=4(x+1) base")
    require(Fraction(3, 5)*Fraction(2, 3) == Fraction(2, 5), "short-offset slope")
    require(Fraction(7, 10)*Fraction(2, 3) == Fraction(7, 15), "rise exponent")
    require(342+Fraction(2, 5) < 343 and Fraction(7, 10) < 1,
            "general height envelope")

    height = poly_mul([1, 1], [516, 343])
    height_difference = poly_add(poly_scale(4, height),
                                 poly_scale(-3, poly_shift(height, 1)))
    height_shift = poly_shift(height_difference, cutoff_bits)
    require(height == [516, 859, 343], "height polynomial")
    require(height_shift == [497750, 26241, 343] and all(x > 0 for x in height_shift),
            "all-band height ratio below 4/3")
    height_base = Fraction(8, 9)*41*(516+343*40)
    require(height_base == Fraction(4669408, 9), "general height base")
    base_margin = 2**313*9**15-4669408**15
    require(base_margin > 0, "exact fifteenth-power base comparison")
    require(4**15 < 2**8*3**15, "height induction ratio")
    return dict(
        scope="Uniform K(k/m)<2*s(h)*m/log2(m), using the actual mismatch count",
        period_cutoff_bits=cutoff_bits,
        dominance_polynomial=dominance,
        dominance_induction_polynomial=dominance_difference,
        dominance_shifted_coefficients=dominance_shift,
        dominance_base_margin=dominance_margin,
        minimum_K_polynomial=minimum_k,
        minimum_K_induction_polynomial=minimum_k_difference,
        minimum_K_shifted_coefficients=minimum_k_shift,
        minimum_K_base_margin=minimum_k_margin,
        height_polynomial=height,
        height_ratio_difference=height_difference,
        height_shifted_coefficients=height_shift,
        height_base=str(height_base),
        height_fifteenth_power_base_margin=base_margin,
        height_ratio_numerator=4**15,
        height_ratio_denominator=3**15,
        left_side_dyadic_ratio=2**8,
    )


def local_minimum():
    rows, maximum_steps, maximum_peak = [], 0, 0
    for seed in range(3, 129, 2):
        current, steps, peak = seed, 0, seed
        checksum = sha256(f"{seed}\n".encode())
        while current != 1:
            require(steps < 10000, "unfinished local convergence")
            raw = 3*current+1
            current = raw >> valuation(raw)
            require(current > 0 and current % 2 == 1, "positive odd local state")
            peak = max(peak, current)
            checksum.update(f"{current}\n".encode())
            steps += 1
        rows.append(dict(seed=seed, odd_steps=steps, peak_odd_state=peak,
                         trajectory_sha256=checksum.hexdigest()))
        maximum_steps, maximum_peak = max(maximum_steps, steps), max(maximum_peak, peak)
    require(len(rows) == 63 and maximum_steps == 43, "local minimum coverage")
    return dict(odd_seeds=[3, 127], count=len(rows), maximum_odd_steps=maximum_steps,
                maximum_peak_odd_state=maximum_peak, conclusion="Every listed odd seed reaches 1",
                records=rows)


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    records = []
    arrows = subadditivity = runs = empty_runs = inverse_cases = 0
    for row in json.loads(path.read_text())["cycles"]:
        states, word, addend = row["states"], row["valuations"], row["d"]
        m = len(word)
        require(m == len(states) and len(set(states)) == m, "primitive actual fixture")
        for i, letter in enumerate(word):
            raw = 3*states[i]+addend
            require(valuation(raw) == letter and raw >> letter == states[(i+1) % m],
                    "actual fixture arrow")
            arrows += 1
        counts = [sum(word[i] != word[(i+d) % m] for i in range(m)) for d in range(m)]
        for d in range(m):
            for e in range(m):
                require(counts[(d+e) % m] <= counts[d]+counts[e], "mismatch subadditivity")
                subadditivity += 1
        for h in range(1, m):
            require(counts[h] > 0 and counts[h] == counts[-h], "nonzero symmetric mismatch count")
            if gcd(h, m) == 1:
                k = pow(h, -1, m)
                coefficients = coefficients_of(k, m)
                check_list(coefficients)
                inverse_cases += 1
            mismatches = [i for i in range(m) if word[i] != word[(i+h) % m]]
            maximum_run = 0
            for mismatch in mismatches:
                start = (mismatch+1) % m
                length = total = 0
                while word[(start+length) % m] == word[(start+length+h) % m]:
                    require(length < m, "agreement run must end")
                    total += word[(start+length) % m]
                    length += 1
                end = (start+length) % m
                z_start = states[(start+h) % m]-states[start]
                z_end = states[(end+h) % m]-states[end]
                require(z_start != 0 and z_end != 0, "primitive run differences")
                require(z_start % (1 << (total+1)) == 0, "exact binary run witness")
                witness = z_start//(1 << (total+1))
                require(z_end == 2*3**length*witness and witness != 0, "exact ternary run witness")
                require(max(states) > 2*3**length, "positive end-state witness")
                maximum_run = max(maximum_run, length)
                runs += 1
                empty_runs += length == 0
            require(maximum_run >= (m-1)//counts[h], "longest agreeing run")
        require(addend in (5, 7, 13, 61) and addend != 1, "control fails q=1 hypothesis")
        records.append(dict(addend=addend, odd_period=m, minimum=min(states),
                            failed_hypothesis="q=1; also below the period cutoff"))
    require(len(records) == 11 and arrows == 106 and empty_runs > 0,
            "all actual-cycle controls, including empty runs")
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), count=len(records),
                exact_arrows=arrows, mismatch_subadditivity_checks=subadditivity,
                agreeing_runs=runs, empty_agreeing_runs=empty_runs,
                coprime_inverse_checks=inverse_cases, records=records)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="inverse-cf-four-mismatch-v2", continuants=continuant_grid(),
                   large_coefficients=large_coefficient_cases(), constants=constants(),
                   local_minimum=local_minimum(), actual_controls=actual_controls(),
                   general_mismatch_growth=general_growth_constants())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    target = HERE / "check_inverse_complexity.json"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", continuant_lists=receipt["continuants"]["lists"],
                          coefficient_splits=receipt["continuants"]["coefficient_splits"],
                          large_coefficient_cases=receipt["large_coefficients"]["qualifying_cases"],
                          local_seeds=receipt["local_minimum"]["count"],
                          actual_cycles=receipt["actual_controls"]["count"]), sort_keys=True))


if __name__ == "__main__":
    main()
