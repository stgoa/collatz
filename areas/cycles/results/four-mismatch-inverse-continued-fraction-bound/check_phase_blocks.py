"""Exact four-boundary phase and repeated-block checks; standard library only."""

from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value):
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length()-1


def continued_fraction(k, m):
    require(0 < k < m and gcd(k, m) == 1, "reduced chronological phase")
    coefficients = []
    a, b = m, k
    while b:
        quotient, remainder = divmod(a, b)
        coefficients.append(quotient)
        a, b = b, remainder
    require(coefficients[-1] >= 2, "canonical final coefficient")
    p_old, p, q_old, q = 1, 0, 0, 1
    rows = []
    for coefficient in coefficients:
        rows.append((p, q, coefficient))
        p_old, p = p, coefficient*p+p_old
        q_old, q = q, coefficient*q+q_old
    require((p, q) == (k, m), "continued-fraction reconstruction")
    denominators = [row[1] for row in rows]+[m]
    for i in range(len(denominators)-2):
        require(denominators[i+2] >= 2*denominators[i], "two-step denominator doubling")
    reciprocal_sum = sum((F(1, Q) for _, Q, _ in rows), F(0))
    require(reciprocal_sum < 4, "finite reciprocal denominator sum")
    require(m*m >= 1 << (len(coefficients)-1), "continued-fraction length bound")
    for p, Q, coefficient in rows:
        j = abs(Q*k-p*m)
        require(0 < Q < m and j > 0 and gcd(p, Q) == 1,
                "proper preceding convergent, including both endpoints")
        require(coefficient*Q*j <= m, "coefficient product bound")
        require(Q*j < m, "proper convergent phase spacing")
    return coefficients, rows, reciprocal_sum


def family_spacing(family, m, Q, j):
    ordered = sorted(family)
    require(len(ordered) == Q, "Q distinct boundaries in one family")
    gaps = [ordered[i+1]-ordered[i] for i in range(Q-1)]
    gaps.append(ordered[0]+m-ordered[-1])
    require(min(gaps)*Q >= m-Q*j, "translated grid-family spacing")
    return min(gaps)


def crossed_events(families, old, new, m):
    # For integer phases and labels on half-open arcs [left,right),
    # transitions in either direction use (min(old,new),max(old,new)].
    # In particular 0 -> -1 crosses the boundary at zero.
    lower, upper = min(old, new), max(old, new)
    events = []
    for color, family in enumerate(families):
        for boundary in family:
            lift = boundary+((lower-boundary)//m+1)*m
            if lift <= upper:
                events.append((color, lift))
    return events


def phase_data(word, k, p, Q):
    m = len(word)
    signed_j = Q*k-p*m
    j = abs(signed_j)
    require(j > 0 and Q*j < m and gcd(p, Q) == 1, "phase lemma hypotheses")
    boundaries = [i for i in range(m) if word[i] != word[i-1]]
    require(1 <= len(boundaries) <= 4, "at most four track boundaries")
    families = [{(boundary-s*k) % m for s in range(Q)} for boundary in boundaries]
    spacing = min(family_spacing(family, m, Q, j) for family in families)
    patterns = [tuple(word[(phase+s*k) % m] for s in range(Q)) for phase in range(m)]
    return signed_j, families, patterns, spacing


def check_phase_start(word, k, p, Q, start, data):
    m = len(word)
    signed_j, families, patterns, spacing = data
    j = abs(signed_j)
    number = m//Q
    sequence = [patterns[(start+r*signed_j) % m] for r in range(number)]
    changes = [r for r in range(1, number) if sequence[r] != sequence[r-1]]
    prefix_blocks = changes[4] if len(changes) >= 5 else number
    regime_count = 1+sum(r < prefix_blocks for r in changes)
    require(regime_count <= 5, "prefix contains at most five repeated-block regimes")
    require(j*Q*(prefix_blocks+1) >= m, "prefix length at least m/j-Q")
    event_checks = 0
    if len(changes) >= 5:
        selected = []
        for r in changes[:5]:
            old, new = start+(r-1)*signed_j, start+r*signed_j
            events = crossed_events(families, old, new, m)
            require(events, "each actual pattern change crosses a boundary")
            selected.append(min(events))
            event_checks += 1
        require(len({location for _, location in selected}) == 5,
                "half-open transition intervals have disjoint events")
        equal_color_pairs = [(x, y) for i, x in enumerate(selected) for y in selected[i+1:]
                             if x[0] == y[0]]
        require(equal_color_pairs, "five events have a repeated boundary family")
        for (_, x), (_, y) in equal_color_pairs:
            require(abs(x-y)*Q >= m-Q*j, "same-family lifted event separation")
        span = max(x for _, x in selected)-min(x for _, x in selected)
        require(span <= prefix_blocks*j and span*Q >= m-Q*j,
                "boundary separation transfers to the prefix span")
    return dict(events=event_checks, regimes=regime_count, prefix_blocks=prefix_blocks,
                full_prefix=prefix_blocks == number, negative=signed_j < 0,
                Q_one=Q == 1, minimum_family_spacing=spacing)


def four_arc_grid():
    label_patterns = ((1, 2, 3, 4), (9, 1, 3, 1), (1, 7, 1, 7))
    track_words = starts = events = full = negative = one = 0
    maximum_regimes = 0
    checksum = sha256()
    for m in range(4, 12):
        for a in range(1, m-2):
            for b in range(1, m-a-1):
                for c in range(1, m-a-b):
                    d = m-a-b-c
                    for labels in label_patterns:
                        word = [labels[0]]*a+[labels[1]]*b+[labels[2]]*c+[labels[3]]*d
                        require(sum(word[i] != word[i-1] for i in range(m)) == 4,
                                "four nonempty adjacent-distinct arcs")
                        track_words += 1
                        for k in range(1, m):
                            if gcd(k, m) != 1:
                                continue
                            _, rows, _ = continued_fraction(k, m)
                            for p, Q, _ in rows:
                                data = phase_data(word, k, p, Q)
                                for start in range(m):
                                    result = check_phase_start(word, k, p, Q, start, data)
                                    starts += 1
                                    events += result["events"]
                                    full += result["full_prefix"]
                                    negative += result["negative"]
                                    one += result["Q_one"]
                                    maximum_regimes = max(maximum_regimes, result["regimes"])
                                    checksum.update(f"{m}:{a}:{b}:{c}:{d}:{labels}:{k}:{p}:{Q}:{start}:{result['prefix_blocks']}\n".encode())
    require(events > 0 and negative > 0 and one > 0 and maximum_regimes == 5,
            "all endpoint, sign and five-regime cases occur")
    return dict(periods=[4, 11], arc_lengths="all four positive compositions",
                labels=[list(row) for row in label_patterns], track_words=track_words,
                phases="every start, every coprime step, every proper preceding convergent",
                phase_starts=starts, crossed_events=events, full_prefix_cases=full,
                negative_phase_cases=negative, denominator_one_cases=one,
                maximum_repeated_regimes=maximum_regimes, coverage_sha256=checksum.hexdigest())


def spike_grid():
    words = starts = replaced_ones = replaced_high = 0
    checksum = sha256()
    for m in range(4, 26):
        for high_count in sorted({1, m//2, m-1}):
            for high in (3, 17):
                base = [high]*high_count+[1]*(m-high_count)
                for spike in range(m):
                    word = base.copy()
                    word[spike] = high+1
                    boundaries = sum(word[i] != word[i-1] for i in range(m))
                    require(2 <= boundaries <= 4, "single-spike boundary count")
                    words += 1
                    replaced_ones += base[spike] == 1
                    replaced_high += base[spike] == high
                    for k in sorted({1, m-1, m//2, m//2+1}):
                        if gcd(k, m) != 1:
                            continue
                        _, rows, _ = continued_fraction(k, m)
                        for p, Q, _ in rows:
                            data = phase_data(word, k, p, Q)
                            for start in sorted({0, 1, m-1}):
                                result = check_phase_start(word, k, p, Q, start, data)
                                starts += 1
                                checksum.update(f"{m}:{high_count}:{high}:{spike}:{k}:{Q}:{start}:{result['prefix_blocks']}\n".encode())
    require(replaced_ones and replaced_high, "both spike arrangements")
    return dict(periods=[4, 25], high_counts="1,floor(m/2),m-1", high_labels=[3, 17],
                spike_label="high+1", spike_positions="every site",
                chronological_steps="coprime members of{1,m-1,floor(m/2),floor(m/2)+1}",
                starting_phases="0,1,m-1", track_words=words, phase_starts=starts,
                spikes_replacing_ones=replaced_ones, spikes_replacing_high=replaced_high,
                coverage_sha256=checksum.hexdigest())


def cf_sum_grid():
    cases = splits = first = final = duplicate = 0
    largest = F(0)
    checksum = sha256()
    for m in range(2, 257):
        for k in range(1, m):
            if gcd(k, m) != 1:
                continue
            coefficients, rows, reciprocal = continued_fraction(k, m)
            largest = max(largest, reciprocal)
            cases += 1
            splits += len(rows)
            first += rows[0][:2] == (0, 1)
            final += rows[-1][1] < m
            duplicate += len(rows) > 1 and rows[1][1] == 1
            checksum.update(f"{k}:{m}:{coefficients}:{reciprocal}\n".encode())
    require(first == final == cases and duplicate > 0, "CF edge coverage")
    return dict(denominators=[2, 256], all_reduced_numerators=True, rationals=cases,
                coefficient_splits=splits, initial_zero_over_one=first,
                final_proper_convergents=final, duplicated_initial_denominators=duplicate,
                maximum_reciprocal_sum=str(largest), coverage_sha256=checksum.hexdigest())


def intercept(word):
    C = total = 0
    for letter in word:
        C = 3*C+(1 << total)
        total += letter
    return C


def trace(start, q, word):
    states = [start]
    for letter in word:
        raw = 3*states[-1]+q
        require(valuation(raw) == letter, "exact positive prefix valuation")
        states.append(raw >> letter)
    return states


def repetition_identity(block, repeats, states, q):
    Q, E = len(block), sum(block)
    require(repeats >= 1 and len(states) == repeats*Q+1, "repeated prefix shape")
    first = states[Q]-states[0]
    if first == 0:
        return False
    final = states[-1]-states[-Q-1]
    exponent = E*(repeats-1)
    require((1 << exponent)*final == 3**(Q*(repeats-1))*first,
            "iterated exact block difference")
    require(first % (1 << exponent) == 0, "binary divisibility of initial difference")
    require(abs(first)*(1 << Q) < 3**Q*(states[0]+q), "strict initial difference size")
    require(1 << (repeats*Q) < 3**Q*(states[0]+q), "exact exponential length bound")
    require((states[-1]+q)*(1 << (repeats*Q)) <= 3**(repeats*Q)*(states[0]+q),
            "generic shifted positive-addend growth")
    require((states[-1]+q)**25 < (states[0]+q)**40*(1 << (24*Q)),
            "rational8/5 relaxation of the output-height bound")
    return True


def integral_prefixes():
    blocks = [block for Q in range(1, 5) for block in product(range(1, 4), repeat=Q)]
    blocks += [(1, 64), (17, 1, 1), (1, 1, 32, 1), (64,)]
    checked = fixed = arrows = 0
    checksum = sha256()
    for block in blocks:
        for repeats in range(1, 9):
            word = block*repeats
            E = sum(word)
            modulus = 1 << (E+1)
            residue = ((1 << E)-intercept(word))*pow(3**len(word), -1, modulus) % modulus
            require(residue > 0 and residue % 2 == 1, "odd cylinder representative")
            for lift in (0, 1):
                start = residue+lift*modulus
                states = trace(start, 1, word)
                if repetition_identity(block, repeats, states, 1):
                    checked += 1
                else:
                    require(all(states[i*len(block)] == states[0] for i in range(repeats+1)),
                            "zero difference is a fixed block control")
                    fixed += 1
                arrows += len(word)
                checksum.update(f"{block}:{repeats}:{lift}:{states[0]}:{states[-1]}\n".encode())
    require(checked > 0 and fixed > 0, "nonzero and fixed-point controls separated")
    return dict(block_lengths=[1, 4], ordinary_letters=[1, 3],
                additional_blocks=[[1, 64], [17, 1, 1], [1, 1, 32, 1], [64]],
                repetition_counts=[1, 8], cylinder_lifts=[0, 1],
                nonzero_difference_prefixes=checked, fixed_block_countercontrols=fixed,
                exact_arrows=arrows, coverage_sha256=checksum.hexdigest(),
                scope="genuine positive integer3x+1 prefixes; no nontrivial closed cycle is asserted")


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = repetitions = 0
    for row in rows:
        word, states, q = row["valuations"], row["states"], row["d"]
        m = len(word)
        require(len(set(states)) == m and q in (5, 7, 13, 61), "primitive standard cycle")
        require(trace(states[0], q, word) == states+[states[0]], "standard cycle arrows")
        arrows += m
        for start in range(m):
            for Q in range(1, m):
                block = tuple(word[(start+i) % m] for i in range(Q))
                N = 1
                while (N+1)*Q <= m and all(word[(start+N*Q+i) % m] == block[i] for i in range(Q)):
                    N += 1
                segment = [states[(start+i) % m] for i in range(N*Q+1)]
                require(repetition_identity(block, N, segment, q), "primitive control block difference")
                repetitions += 1
    require(len(rows) == 11 and arrows == 106 and repetitions > 0, "all standard controls")
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), cycles=len(rows),
                exact_arrows=arrows, repeated_segments=repetitions,
                scope="addendq retained in x+q; no q=1 minimum or period estimate applied")


def constants():
    require(3**5 < 2**8, "alpha below8/5")
    H5 = sum((F(8, 5)**i for i in range(5)), F(0))
    require(H5 == F(9881, 625) < 16, "five-regime Y coefficient")
    require(F(8, 5)*H5+1 == F(82173, 3125) < 27, "five-regime Q coefficient")
    require(16*4 == 64, "reciprocal-sum coefficient")
    return dict(alpha_upper="8/5", maximum_regimes=5, H5_upper=str(H5),
                Q_coefficient_upper=str(F(8, 5)*H5+1),
                phase_bound_coefficients=[16, 27], inverse_CF_bound_coefficients=[27, 64],
                reciprocal_preceding_denominator_sum_upper=4,
                crossing_convention="integer phases on[0,T): events in(min(old,new),max(old,new)]")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="four-boundary-phase-blocks-v1", constants=constants(),
                   four_arc_grid=four_arc_grid(), spike_grid=spike_grid(),
                   continued_fractions=cf_sum_grid(), integer_prefixes=integral_prefixes(),
                   actual_controls=actual_controls())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    target = HERE / "check_phase_blocks.json"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", generic_phase_starts=receipt["four_arc_grid"]["phase_starts"],
                          spiked_phase_starts=receipt["spike_grid"]["phase_starts"],
                          rational_phases=receipt["continued_fractions"]["rationals"],
                          integral_prefixes=receipt["integer_prefixes"]["nonzero_difference_prefixes"],
                          standard_cycles=receipt["actual_controls"]["cycles"]), sort_keys=True))


if __name__ == "__main__":
    main()
