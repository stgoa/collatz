"""Exact finite closure and controls for the Fibonacci four-arc family."""

from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 16


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def fibonacci(last):
    values = [0, 1]
    while len(values) <= last:
        values.append(values[-1] + values[-2])
    return values


def cf_sum(numerator, denominator):
    require(0 < numerator < denominator, "proper positive rational")
    total = 0
    while numerator:
        total += denominator // numerator
        numerator, denominator = denominator % numerator, numerator
    return total


def intercept(word):
    C = total = 0
    for letter in word:
        C = 3 * C + (1 << total)
        total += letter
    return C


def integer_hash(value):
    return sha256(format(value, "x").encode()).hexdigest()


def build(n, fib):
    m, h = fib[n], fib[n - 1]
    require(n >= 7 and gcd(m, h) == 1, "Fibonacci family domain")
    b = m // 10
    a = m - 2 * b - 1
    three = 3**m
    A = three.bit_length()
    M = A - m - 3 * b + 1
    require(a >= b >= 1 and M >= 4, "four distinct labels")
    track = [1] * a + [2] * b + [3] * b + [M]
    word, template = [0] * m, [0] * m
    for j, letter in enumerate(track):
        word[j * h % m] = letter
        template[j * h % m] = 1 if letter == M else letter
    require(min(word) > 0 and word.count(M) == 1, "positive primitive word")
    require(sum(word) == A and sum(template) == m + 3 * b, "exact totals")
    require(sum(x != y for x, y in zip(word, template)) == 1, "single positive edit")
    require(all(x >= y for x, y in zip(word, template)), "edit has no negative loss")
    require(three < 1 << A < 2 * three, "exact near-criticality")
    return word, template, dict(n=n, m=m, h=h, k=pow(h, -1, m), a=a, b=b, M=M, A=A)


def rotation_checks(word, template, row, exhaustive_factors):
    n, m, h, k = (row[x] for x in ("n", "m", "h", "k"))
    lengths = (row["a"], row["b"], row["b"], 1)
    spectra = []
    for shift in range(1, m):
        phase = shift * k % m
        distance = min(phase, m - phase)
        mismatch = sum(min(distance, length, m - length) for length in lengths)
        require(mismatch >= 4, "four distinct interval labels")
        if exhaustive_factors:
            require(mismatch == sum(word[i] != word[(i + shift) % m] for i in range(m)),
                    "direct mismatch spectrum")
        spectra.append(mismatch)
    require(min(spectra) == 4 and spectra[h - 1] == spectra[m - h - 1] == 4,
            "exact rotation distance")
    # Any mechanical alphabet has one or two adjacent values. Check every
    # possible adjacent pair that could meet this word's finite alphabet.
    candidate_lower = {max(1, x - 1) for x in set(word)} | set(word)
    alphabet_miss = min(sum(x not in (lower, lower + 1) for x in word)
                        for lower in candidate_lower)
    require(alphabet_miss >= row["b"], "mechanical distance from alphabet")

    # For all cyclic factors, the scaled deviation is a difference
    # of these prefix deviations (the full-period deviation is zero).
    # Both orientations occur, so the span is the largest absolute
    # deviation. This checks every factor in linear time.
    T = sum(template)
    Delta = 4 * (n - 2)
    prefix = 0
    deviations = [0]
    for length, letter in enumerate(template, 1):
        prefix += letter
        deviations.append(m * prefix - T * length)
    span = max(deviations) - min(deviations)
    require(span <= m * Delta, "all-factor DK discrepancy by prefix span")

    checks = factor_classes = direct_max = 0
    if exhaustive_factors:
        doubled = template + template
        for start in range(m):
            total = 0
            for length in range(1, m):
                total += doubled[start + length - 1]
                require(abs(m * total - T * length) <= m * Delta,
                        "DK template discrepancy")
                direct_max = max(direct_max, abs(m * total - T * length))
                checks += 1
        require(direct_max == span, "direct all-factor and prefix-span agreement")
        for length in range(1, m):
            classes = {tuple(doubled[start:start + length]) for start in range(m)}
            require(len(classes) <= 3 * length, "three-interval factor complexity")
            factor_classes += 1
    return dict(rotation_shifts=m - 1, direct_spectrum=exhaustive_factors,
                mechanical_alphabet_distance=alphabet_miss, discrepancy_checks=checks,
                all_factor_discrepancy_numerator=span, discrepancy_denominator=m,
                all_factors_checked_by_prefix_span=True,
                factor_complexity_lengths=factor_classes)


def reduced_cycle(word, q, common, C):
    current = C // common
    start = current
    minimum, maximum = start, start
    for letter in word:
        require(current > 0 and current % 2 == 1, "positive odd reduced state")
        raw = 3 * current + q
        require(raw % (1 << letter) == 0, "integral reduced arrow")
        current = raw >> letter
        require(current % 2 == 1, "exact reduced valuation")
        minimum, maximum = min(minimum, current), max(maximum, current)
    require(current == start, "actual reduced cycle closes")
    return minimum, maximum


def family_checks():
    fib = fibonacci(25)
    rows, spectrum_checks, factor_checks = [], 0, 0
    for n in range(7, 25):
        word, template, row = build(n, fib)
        m, A = row["m"], row["A"]
        require(m < CUTOFF, "finite residual length")
        C = intercept(word)
        two, three = 1 << A, 3**m
        D = two - three
        common = gcd(C, D)
        q = D // common
        require(q > 1, "finite denominator-one exclusion")
        low, high = reduced_cycle(word, q, common, C)
        t, Delta, T = (m - 2) // 4, 4 * (n - 2), sum(template)
        require(m - t >= 3 * t + 2, "clean-window pigeonhole")
        require(high > 2 * 3**t, "repeated-factor state separation")
        require(3 * high * (1 << T) <= (1 << Delta) * three * (3 * low + m * q),
                "template growth from minimum")
        require(3 * low * D < m * q * two, "cycle drift minimum bound")
        require(q * (1 << Delta) * three * m * two > 3**(t + 1) * D * (1 << T),
                "unsimplified denominator law")
        # q > 2^(m/10-4) * D/(2^A*m^9), with all positive
        # quantities raised to the tenth power to remove the root.
        require((16 * m**9 * q * two)**10 > (D**10) << m,
                "unconditional simplified denominator law")
        checks = rotation_checks(word, template, row, n <= 12)
        spectrum_checks += checks["rotation_shifts"]
        factor_checks += checks["discrepancy_checks"]
        row.update(checks)
        row.update(template_total=T, discrepancy_bound=Delta, repeated_length=t,
                   gcd=common, denominator_bits=q.bit_length(), denominator_greater_than_one=True,
                   denominator_hex_sha256=integer_hash(q), reduced_cycle_minimum_bits=low.bit_length(),
                   reduced_cycle_maximum_bits=high.bit_length(), actual_reduced_arrows=m,
                   word_sha256=sha256(json.dumps(word, separators=(",", ":")).encode()).hexdigest())
        if n <= 12:
            row["denominator"] = q
        rows.append(row)
    require(len(rows) == 18 and fib[24] == 46368 < CUTOFF < fib[25] == 75025,
            "complete finite Fibonacci residual")
    return dict(indices=[7, 24], rows=rows, exact_word_count=len(rows),
                next_index=25, next_length=fib[25], all_lengths_below=CUTOFF,
                spectrum_shifts=spectrum_checks, discrepancy_checks=factor_checks,
                direct_rotation_and_all_factor_indices=[7, 12],
                actual_reduced_arrows=sum(row["m"] for row in rows))


def arithmetic_checks():
    require(3**2 > 2**3 and 3**5 < 2**8, "exact logarithm bounds")
    fib = fibonacci(128)
    rows = []
    for n in range(3, 129):
        m, h = fib[n], fib[n - 1]
        require(gcd(m, h) == 1, "consecutive Fibonacci numbers coprime")
        k = pow(h, -1, m)
        expected = h if n % 2 == 0 else m - h
        require(k == expected and h * h % m == (-1)**n % m, "Cassini inverse")
        require(cf_sum(h, m) == cf_sum(k, m) == n - 1, "chronological CF cost")
        require(m * m >= 1 << (n - 2), "Fibonacci logarithmic lower bound")
        rows.append(dict(n=n, m=m, h=h, k=k, continued_fraction_sum=n - 1))
    require(CUTOFF // 2 - 5 * (176 + 350 * 16) == 3888, "cutoff margin times five")
    require(CUTOFF > 7000, "positive derivative beyond cutoff")
    return dict(Fibonacci_indices=[3, 128], inverse_and_cf_rows=rows,
                large_length_cutoff=CUTOFF, cutoff_margin_numerator=3888,
                cutoff_margin_denominator=5, derivative_threshold=7000)


def general_template_checks():
    """All stated finite parameters; this is a formula control, not a cutoff."""
    rows = []
    for m in range(6, 19):
        three = 3**m
        threshold = three.bit_length()
        templates = words = nonprimitive = 0
        for first in range(1, m - 1):
            for second in range(1, m - first):
                third = m - first - second
                F = first + 2 * second + 3 * third
                if 1 << F >= three:
                    continue
                track = [1] * first + [2] * second + [3] * third
                for k in range(1, m):
                    if gcd(k, m) != 1:
                        continue
                    template = [track[i * k % m] for i in range(m)]
                    Delta, t = 4 * (cf_sum(k, m) - 1), (m - 2) // 4
                    prefixes, total = [0], 0
                    for i, letter in enumerate(template, 1):
                        total += letter
                        prefixes.append(m * total - F * i)
                    require(max(prefixes) - min(prefixes) <= m * Delta,
                            "general three-interval discrepancy")
                    doubled = template + template
                    classes = {tuple(doubled[i:i + t]) for i in range(m)}
                    require(len(classes) <= 3 * t and m - t > len(classes),
                            "general clean-window factor count")
                    templates += 1
                    inverse = pow(k, -1, m)
                    for phase in (0, first, first + second):
                        position = phase * inverse % m
                        for extra in (0, 2):
                            A = threshold + extra
                            word = list(template)
                            word[position] += A - F
                            require(A > F and sum(word) == A, "general positive edit")
                            if any(all(word[i] == word[(i + shift) % m] for i in range(m))
                                   for shift in range(1, m)):
                                nonprimitive += 1
                                continue
                            D, C = (1 << A) - three, intercept(word)
                            q = D // gcd(C, D)
                            require(q * (1 << Delta) * m * three * (1 << A)
                                    > D * 3**(t + 1) * (1 << F),
                                    "general template denominator inequality")
                            words += 1
        rows.append(dict(length=m, templates=templates, primitive_positive_edits=words,
                         excluded_nonprimitive_edits=nonprimitive))
    return dict(lengths=[6, 18], template_arc_lengths="all positive triples summing to m",
                chronological_steps="all 1<=k<m coprime to m",
                template_total_condition="2^F<3^m",
                edited_track_phases="0, first arc length, first plus second arc lengths",
                edited_totals="ceil(m*log_2(3)) and that value plus 2",
                rows=rows, templates=sum(row["templates"] for row in rows),
                primitive_positive_edits=sum(row["primitive_positive_edits"] for row in rows))


def actual_controls():
    source = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(source.read_text())["cycles"]
    rows = []
    for cycle in fixtures:
        d, states, word = cycle["d"], cycle["states"], cycle["valuations"]
        require(len(states) == len(word) > 0 and min(states) == cycle["minimum"], "fixture shape")
        for i, (x, exponent) in enumerate(zip(states, word)):
            require(x > 0 and x % 2 == 1, "positive odd fixture")
            require(3 * x + d == (1 << exponent) * states[(i + 1) % len(states)],
                    "actual fixture arrow")
        rows.append(dict(d=d, minimum=min(states), odd_period=len(states)))
    require(len(rows) == 11 and {row["d"] for row in rows} == {5, 7, 13, 61},
            "eleven standard controls")

    word = [1, 1, 3, 1, 2, 1, 1, 1, 1, 2, 1, 5]
    C, D = intercept(word), (1 << sum(word)) - 3**len(word)
    common = gcd(C, D)
    require((C, D, common, D // common) == (1291961, 517135, 1753, 295), "known four-mismatch control")
    low, high = reduced_cycle(word, 295, common, C)
    require(low == 737 and low > 295, "normalized control minimum above one")
    require(min(sum(word[i] != word[(i + shift) % len(word)] for i in range(len(word)))
                for shift in range(1, len(word))) == 4, "known control rotation distance")
    require(len(word) < fibonacci(7)[7], "known control outside the family")
    return dict(fixture_sha256=sha256(source.read_bytes()).hexdigest(), cycles=rows,
                known_four_mismatch=dict(word=word, additive_parameter=295, minimum=low,
                                         maximum=high, cancellation=common, outside_family=True))


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="fibonacci-four-arc-spike-v1", arithmetic=arithmetic_checks(),
                   finite_family=family_checks(), general_templates=general_template_checks(),
                   actual_controls=actual_controls())
    target = HERE / "check_fibonacci_spike.json"
    encoded = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    family = receipt["finite_family"]
    print(json.dumps(dict(result="passed", finite_family_words=family["exact_word_count"],
                          spectrum_shifts=family["spectrum_shifts"],
                          discrepancy_checks=family["discrepancy_checks"],
                          actual_reduced_arrows=family["actual_reduced_arrows"],
                          standard_cycles=11), sort_keys=True))


if __name__ == "__main__":
    main()
