"""Exact two-track geometry, local descent and full-clock cycle closure.

The complete geometric proof clips rational polygons, with no numerical solver,
discovery artifact, variable input path, or resource guard. Finite cycle controls
check the separate track and paired-state transfers; they are not an absence
search. All coordinates use the raw odd-only clock. The large-period
reduction uses the declared EXT-1 theorem; every remaining finite step is
recomputed here without importing a period bound or a predecessor checker.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations, product
from math import comb, gcd
from pathlib import Path
import json
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
ORDERS = tuple(range(3, 19))
R = F(37, 100)
EPSILON = F(1, 750)
ROW_SCALE = 3000
LOCAL_LIMIT = 18000000
FULL_PERIOD_LIMIT = 1 << 22
FINAL_PERIOD_LIMIT = 24000


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def evaluate(row, point):
    """The row means row[0]*x + row[1]*y + row[2] < 0."""
    return row[0]*point[0] + row[1]*point[1] + row[2]


def clip(polygon, row):
    """Intersect a rational convex polygon with the CLOSED row half-plane.

    A zero-area result excludes a strict solution in the initial open triangle.
    Boundary vertices and redundant rows are retained without tolerance tests.
    """
    if not polygon:
        return []
    result = []
    for first, second in zip(polygon, polygon[1:]+polygon[:1]):
        a, b = evaluate(row, first), evaluate(row, second)
        if a <= 0:
            result.append(first)
        if (a < 0 < b) or (b < 0 < a):
            ratio = a/(a-b)
            result.append(tuple(x+ratio*(y-x) for x, y in zip(first, second)))
    return result


def twice_area(polygon):
    return abs(sum(x[0]*y[1]-y[0]*x[1]
                   for x, y in zip(polygon, polygon[1:]+polygon[:1])))


def geometric_rows(order, numerator, first_levels, second_levels):
    """Enumerate all rows for 0<x<y<1, cut coordinates (level+phase)/M.

    Each row is exactly 3000*M times gap-R*paired_height-EPSILON.
    Distinct phases make the endpoint order lexicographic (level, track).
    The nonidentity partner has the same phase, so its larger level determines
    the paired maximum. Repeated cuts within a track are deduplicated exactly.
    """
    for j in range(1, order):
        require((j*numerator) % order != 0, "nonidentity geometric power")
        first = {(k-i*numerator) % order for k in first_levels for i in range(j)}
        second = {(k-i*numerator) % order for k in second_levels for i in range(j)}
        chain = sorted([(k, 0) for k in first]+[(k, 1) for k in second])
        for index, (level, track) in enumerate(chain):
            prior, prior_track = chain[index-1]
            coefficients = [0, 0]
            coefficients[track] += 1890
            coefficients[prior_track] -= 3000
            constant = (3000*(level-prior+(order if index == 0 else 0))
                        -1110*max(level, (level+j*numerator) % order)-4*order)
            yield j, (coefficients[0], coefficients[1], constant)


def check_polygon(order, numerator, first, second):
    polygon = [(F(0), F(0)), (F(1), F(1)), (F(0), F(1))]
    used = 0
    for j, row in geometric_rows(order, numerator, first, second):
        used += 1
        polygon = clip(polygon, row)
        if len(polygon) < 3 or twice_area(polygon) == 0:
            return used, j
    raise RuntimeError(f"Unclosed strict geometry: {(order, numerator, first, second)}")


def complete_geometry():
    counts = Counter()
    cases = []
    digest = sha256()
    for order in ORDERS:
        one_track = [(k, ()) for k in combinations(range(order), 4)]
        two_tracks = list(product(combinations(range(order), 2), repeat=2))
        families = one_track+two_tracks
        expected = comb(order, 4)+comb(order, 2)**2
        require(len(families) == expected, "complete 4 or 2+2 family enumeration")
        for numerator in range(1, order):
            if 2*numerator >= order or gcd(numerator, order) != 1:
                continue
            used = 0
            stop_rotations = Counter()
            for first, second in families:
                rows, stop = check_polygon(order, numerator, first, second)
                used += rows
                stop_rotations[stop] += 1
                digest.update(f"{order}:{numerator}:{first}:{second}:{rows}:{stop}\n".encode())
            counts["shifts"] += 1
            counts["families"] += expected
            counts["rows"] += used
            cases.append({"order": order, "numerator": numerator,
                          "one_track_families": len(one_track),
                          "two_track_families": len(two_tracks),
                          "families": expected, "checked_rows": used,
                          "last_needed_rotation": dict(sorted(stop_rotations.items()))})
    require(counts == {"shifts": 50, "families": 468340, "rows": 571465},
            "complete expected geometry counts")
    return {"orders": list(ORDERS), "coefficient": str(R), "epsilon": str(EPSILON),
            "counts": dict(sorted(counts.items())), "cases": cases,
            "survivors": 0, "cases_sha256": digest.hexdigest(),
            "scope": "Complete exact strict-cell exclusion, not a sampled search."}


def direct_deficits(order, numerator, cuts, coefficient=R):
    """Independent modular evaluation, retaining the pre-drop value f(0)=1."""
    h = F(numerator, order)
    result = []
    for j in range(1, order):
        refined = sorted({(c-i*h) % 1 for c in cuts for i in range(j)})
        values = []
        for index, end in enumerate(refined):
            previous = refined[index-1]
            gap = end-previous+(1 if index == 0 else 0)
            partner = (end+j*h) % 1
            values.append(gap-coefficient*max(end or F(1), partner or F(1)))
        result.append(values)
    return result


def phase_representation(order, cuts):
    groups = defaultdict(list)
    for cut in cuts:
        position = order*(cut % 1)
        level = position.numerator//position.denominator
        groups[position-level].append(level)
    require(len(groups) in (1, 2), "at most two track phases")
    phases = sorted(groups)
    levels = [tuple(sorted(groups[x])) for x in phases]
    require(sorted(map(len, levels)) in ([4], [2, 2]), "track boundary partition")
    if len(phases) == 1:
        return phases[0], (phases[0]+1)/2, levels[0], ()
    return phases[0], phases[1], levels[0], levels[1]


def direct_row_controls():
    counts = Counter()
    digest = sha256()
    for order in ORDERS:
        families = [(k, ()) for k in combinations(range(order), 4)]
        families += list(product(combinations(range(order), 2), repeat=2))
        # Exhaust all small patterns; the larger fixed grid checks the row
        # formula only. Complete geometric coverage is proved above.
        selected = families if order <= 6 else families[::max(1, len(families)//30)]
        for numerator in range(1, order):
            if 2*numerator >= order or gcd(numerator, order) != 1:
                continue
            for first, second in selected:
                rows = list(geometric_rows(order, numerator, first, second))
                for phase in ((F(2, 13), F(9, 13)), (F(5, 13), F(12, 13))):
                    cuts = [F(k, order)+phase[0]/order for k in first]
                    cuts += [F(k, order)+phase[1]/order for k in second]
                    direct = direct_deficits(order, numerator, cuts)
                    expected = [ROW_SCALE*order*(v-EPSILON) for group in direct for v in group]
                    actual = [evaluate(row, phase) for _, row in rows]
                    require(expected == actual, "direct modular gap versus generated affine row")
                    counts["row_evaluations"] += len(actual)
                    digest.update(f"{order}:{numerator}:{first}:{second}:{phase}:{actual}\n".encode())
                counts["patterns"] += 1
    require(counts == {"patterns": 1890, "row_evaluations": 670140}, "direct control coverage")
    return {"counts": dict(sorted(counts.items())), "cases_sha256": digest.hexdigest()}


def boundary_controls():
    counts = Counter()
    digest = sha256()
    shift = F(1, 10**7)
    for order in ORDERS:
        for numerator in range(1, order):
            if gcd(numerator, order) != 1:
                continue
            # Includes a zero phase, wrap at that phase, and a swap of which
            # phase is smaller after the common negative translation.
            cuts = [F(0), F(1, order), F(1, 3*order), F(4, 3*order)]
            variants = [cuts]
            if order >= 4:
                variants.append([F(i, order) for i in range(4)])
            for before_cuts in variants:
                after_cuts = [(c-shift) % 1 for c in before_cuts]
                phase = phase_representation(order, after_cuts)
                require(0 < phase[0] < phase[1] < 1, "generic phase after common left translation")
                before = direct_deficits(order, numerator, before_cuts)
                after = direct_deficits(order, numerator, after_cuts)
                for j in range(1, order):
                    require(len(before[j-1]) == len(after[j-1]), "common translation preserves collisions")
                    require(max(after[j-1]) <= max(before[j-1])+R*shift,
                            "one-sided pre-drop continuity control")
                h = F(numerator, order)
                reverse = direct_deficits(order, order-numerator, [(c+h) % 1 for c in before_cuts])
                require([sorted(v) for v in before] == [sorted(v) for v in reverse],
                        "orientation preserves gaps and swaps paired evaluations")
                counts["cases"] += 1
                digest.update(f"{order}:{numerator}:{before_cuts}:{before}:{after}\n".encode())
    require(counts["cases"] == 198, "all reduced orientation and boundary controls")
    quarter = [F(0), F(1, 4), F(1, 2), F(3, 4)]
    values = direct_deficits(2, 1, quarter)
    require(values == [[F(-3, 25), F(-11, 400), F(-3, 25), F(-11, 400)]],
            "exact order-two control")
    phase = phase_representation(2, quarter)
    require(phase[2:] == ((0, 1), (0, 1)), "two tracks at order two")
    return {"counts": dict(counts), "cases_sha256": digest.hexdigest(),
            "order_two_control": {"cuts": list(map(str, quarter)),
                                  "deficits": [[str(v) for v in row] for row in values],
                                  "maximum_deficit": str(max(values[0]))},
            "scope": "Finite transfer controls; order-two points are not asserted to be a cycle."}


def coefficient_regression_control():
    """The larger margin needs the sharper coefficient, not just a new EPSILON."""
    order, numerator = 18, 7
    x, y = F(3457, 5625), F(8933, 9000)
    cuts = sorted([F(k, order)+x/order for k in (8, 12)]
                  +[F(k, order)+y/order for k in (3, 17)])
    old = [max(group) for group in direct_deficits(order, numerator, cuts, F(3, 8))]
    current = [max(group) for group in direct_deficits(order, numerator, cuts)]
    require(max(old) == F(293, 270000) < EPSILON,
            "the old coefficient admits this structured strict control at the new margin")
    require(max(current) >= EPSILON, "sharper coefficient removes the control")
    require(phase_representation(order, cuts) == (x, y, (8, 12), (3, 17)),
            "regression control has precisely two tracks")
    return {"order": order, "numerator": numerator,
            "phases": [str(x), str(y)], "track_levels": [[8, 12], [3, 17]],
            "cuts": list(map(str, cuts)), "old_coefficient": "3/8",
            "old_maximum_by_rotation": list(map(str, old)),
            "old_maximum_deficit": str(max(old)),
            "old_margin_to_new_epsilon": str(EPSILON-max(old)),
            "current_maximum_by_rotation": list(map(str, current)),
            "current_maximum_deficit": str(max(current)),
            "scope": "An exact geometric control only, not a word or cycle construction."}


def actual_cycle(word):
    intercept, total = 0, 0
    for letter in word:
        require(letter >= 1, "positive valuation")
        intercept = 3*intercept+2**total
        total += letter
    discriminant = 2**total-3**len(word)
    require(discriminant > 0, "positive full discriminant")
    common = gcd(intercept, discriminant)
    q, state = discriminant//common, intercept//common
    states = []
    for letter in word:
        require(state > 0 and state % 2, "positive odd actual state")
        states.append(state)
        raw = 3*state+q
        require((raw & -raw).bit_length()-1 == letter, "exact raw odd valuation")
        state = raw >> letter
    require(state == states[0] and len(set(states)) == len(word), "primitive actual cycle")
    cut = states.index(min(states))
    return q, states[cut:]+states[:cut], word[cut:]+word[:cut]


def check_ramp(word, states, q):
    length, total, minimum = len(word), sum(word), min(states)
    require(states[0] == minimum, "minimum-state clock")
    for index, letter in enumerate(word):
        raw = 3*states[index]+q
        require(raw == 2**letter*states[(index+1) % length], "actual addend retained")
        require((raw & -raw).bit_length()-1 == letter, "exact actual valuation")
        require(states[index]*2**index*3**length <= minimum*3**index*2**total,
                "minimum-state ramp in exact integer powers")
    return length


def check_cycle_shift(word, states, shift):
    length = len(word)
    tracks = gcd(shift, length)
    order = length//tracks
    base = {i for i in range(length) if word[i] != word[(i+shift) % length]}
    require(len(base) == 4 and order in ORDERS, "actual four-mismatch shift")
    groups = defaultdict(list)
    for cut in base:
        groups[cut % tracks].append(cut)
    require(sorted(map(len, groups.values())) in ([4], [2, 2]), "actual track classification")
    for residue in range(tracks):
        path = [(residue+i*shift) % length for i in range(order)]
        changes = sum(word[i] != word[(i+shift) % length] for i in path)
        require(changes == len(groups.get(residue, [])), "track mismatch count")
        require(changes == 0 or changes >= 2, "nonconstant circular track has at least two changes")
    cuts = [F(i, length) for i in sorted(base)]
    x, y, first_levels, second_levels = phase_representation(order, cuts)
    reconstructed = {F(k, order)+x/order for k in first_levels}
    reconstructed |= {F(k, order)+y/order for k in second_levels}
    require(reconstructed == set(cuts), "actual cuts equal their phase/level description")
    prefix = [0]
    for letter in word+word:
        prefix.append(prefix[-1]+letter)
    counts = Counter()
    digest = sha256()
    for j in range(1, order):
        offset = j*shift % length
        require(offset != 0, "nonidentity paired shift")
        actual = {i for i in range(length) if word[i] != word[(i+offset) % length]}
        raw = [(c-i*shift) % length for c in base for i in range(j)]
        refined = sorted(set(raw))
        require(actual <= set(refined), "telescoping mismatch inclusion")
        counts["artificial_cuts"] += len(set(refined)-actual)
        counts["raw_coincidences"] += len(raw)-len(refined)
        for index, end in enumerate(refined):
            previous = refined[index-1]
            run = (end-previous) % length-1
            start = (previous+1) % length
            require(run >= 0, "refined run uses gap minus one")
            require(all(word[(start+i) % length] == word[(start+i+offset) % length]
                        for i in range(run)), "all refined agreement arrows")
            exponent = prefix[start+run]-prefix[start]
            first = states[(start+offset) % length]-states[start]
            last = states[(end+offset) % length]-states[end]
            require(first != 0 and first % 2**(exponent+1) == 0, "paired odd integer lattice")
            require(last == 2*3**run*(first//2**(exponent+1)), "exact paired endpoint identity")
            require(max(states[end], states[(end+offset) % length]) > 2*3**run,
                    "end witness on the correct state clock")
            counts["refined_runs"] += 1
            digest.update(f"{j}:{previous}:{end}:{run}:{exponent}:{first}:{last}\n".encode())
    require(all(states[i] == states[(i+order*shift) % length] for i in range(length)),
            "identity power is outside paired separation")
    return counts, "one_four" if len(groups) == 1 else "two_two", digest.hexdigest()


def cycle_words():
    for order in ORDERS:
        for step in range(1, order):
            if gcd(step, order) != 1:
                continue
            if order >= 4:
                for tracks, labels in product((1, 2, 3), ((1, 2, 3, 5), (1, 5, 3, 2))):
                    word = [2]*(tracks*order)
                    shift = tracks*step
                    track = list(labels[:3])+[labels[3]]*(order-3)
                    for i, letter in enumerate(track):
                        word[i*shift % len(word)] = letter
                    yield order, tracks, step, word, shift
            for tracks in (2, 3):
                word = [2]*(tracks*order)
                shift = tracks*step
                for residue, track in enumerate(([1]+[3]*(order-1), [2, 2]+[5]*(order-2))):
                    for i, letter in enumerate(track):
                        word[(residue+i*shift) % len(word)] = letter
                yield order, tracks, step, word, shift


def actual_controls():
    counts, by_order, by_tracks, by_shape = Counter(), Counter(), Counter(), Counter()
    digest = sha256()
    examples = {}
    for order, tracks, step, word, shift in cycle_words():
        q, states, word = actual_cycle(word)
        counts["arrows"] += check_ramp(word, states, q)
        details, shape, case_hash = check_cycle_shift(word, states, shift)
        counts.update(details)
        counts["actual_cycles"] += 1
        by_order[order] += 1
        by_tracks[tracks] += 1
        by_shape[shape] += 1
        examples.setdefault(shape, {"q": q, "states": states, "word": word,
                                    "shift": shift, "order": order, "gcd": tracks})
        digest.update(f"{order}:{tracks}:{step}:{word}:{q}:{case_hash}\n".encode())
    require(set(by_order) == set(ORDERS) and set(by_tracks) == {1, 2, 3}, "all orders and track clocks")
    require(set(by_shape) == {"one_four", "two_two"}, "both mismatch partitions")
    require(counts["actual_cycles"] == 788 and counts["artificial_cuts"] > 0,
            "deterministic actual-family coverage")
    fixture_path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    raw = fixture_path.read_bytes()
    fixtures = json.loads(raw)["cycles"]
    arrows = 0
    for fixture in fixtures:
        word, states, q = fixture["valuations"], fixture["states"], fixture["d"]
        require(q in (5, 7, 13, 61), "standard control addend")
        cut = states.index(min(states))
        arrows += check_ramp(word[cut:]+word[:cut], states[cut:]+states[:cut], q)
    require(len(fixtures) == 11 and arrows == 106, "all shared actual controls")
    return {"counts": dict(sorted(counts.items())), "orders": dict(sorted(by_order.items())),
            "shift_gcds": dict(sorted(by_tracks.items())), "track_shapes": dict(sorted(by_shape.items())),
            "examples": examples, "cases_sha256": digest.hexdigest(),
            "standard_cycles": len(fixtures), "standard_arrows": arrows,
            "fixture_sha256": sha256(raw).hexdigest(),
            "scope": "Actual primitive positive 3x+q cycles, retaining q. No absence inferred from controls."}


def cutoff_constants():
    """Exact rational constants for both dyadic and final full-period cuts."""
    require(3**12 > 2**19 and 3**63 < 2**100, "19/12<alpha<100/63")
    require(F(1)-F(63, 100) == R, "the actual ramp coefficient is below R")
    require(LOCAL_LIMIT > 2**17, "local replay supplies the weaker drift floor")
    base = (F(12, 19)*(172+342*23)+1)/FULL_PERIOD_LIMIT+F(1, 393216)
    coarse_margin = EPSILON-base
    require(coarse_margin == F(3591763, 29884416000) > 0,
            "dyadic m>=2^22 geometric contradiction")
    # For 2^d<=m<2^(d+1), the nonconstant error term is
    # N_d/(19*2^d), N_d=4104*d+6187. Its dyadic decrease holds
    # for every d>=22 because 2*N_d-N_(d+1)=4104*d+2083>0.
    require(12*342 == 4104 and 12*(172+342)+19 == 6187,
            "dyadic numerator coefficients")
    require(2*4104-4104 == 4104 and 2*6187-(4104+6187) == 2083,
            "dyadic difference identity")
    require(4104*22+2083 > 0, "positive and increasing dyadic difference")
    require(2**49 < 3*2**48, "eta bootstrap gives minimum below 2^48")
    final_base = F(595, 19*FINAL_PERIOD_LIMIT)+F(1, 393216)
    final_margin = EPSILON-final_base
    require(12*48+19 == 595, "ell<48 transfer numerator")
    require(final_margin == F(8083, 311296000) > 0,
            "all full periods m>=24000 excluded after bootstrap")
    return {"ramp_coefficient_strict_upper": str(R),
            "local_drift_error_upper": "1/393216",
            "EXT1_gap_constants": [172, 341],
            "EXT1_log_minimum_upper": "172+342*log2(m)",
            "initial_full_odd_period_strict_upper": FULL_PERIOD_LIMIT,
            "dyadic_numerator": [4104, 6187],
            "dyadic_difference": [4104, 2083],
            "dyadic_error_upper": str(base), "dyadic_strict_margin": str(coarse_margin),
            "bootstrap_log_minimum_strict_upper": 48,
            "final_full_odd_period_strict_upper": FINAL_PERIOD_LIMIT,
            "final_error_upper": str(final_base), "final_strict_margin": str(final_margin),
            "scope": "Full odd-period clock throughout; no imported period or convergence bound."}


def logarithm_bounds(value, terms=80):
    """Positive atanh series with an exact geometric upper bound on its tail."""
    require(value > 1 and terms >= 1, "positive logarithm series input")
    z = F(value-1, value+1)
    lower = 2*sum((z**(2*j+1)/(2*j+1) for j in range(terms)), F(0))
    tail = 2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    require(tail > 0, "positive geometric logarithm tail")
    return lower, lower+tail


def full_exponent_gap():
    """Check every full odd period below 2^22, using outward rational logs."""
    ln2low, ln2high = logarithm_bounds(2)
    ln3low, ln3high = logarithm_bounds(3)
    alpha_low, alpha_high = ln3low/ln2high, ln3high/ln2low
    scale = 1 << 96
    low_scaled, high_scaled = alpha_low*scale, alpha_high*scale
    low_num = low_scaled.numerator//low_scaled.denominator
    high_num = -(-high_scaled.numerator//high_scaled.denominator)
    require(F(low_num, scale) <= alpha_low < alpha_high <= F(high_num, scale),
            "outward dyadic logarithm rounding")
    require(high_num == low_num+1, "adjacent dyadic alpha endpoints")
    require(ln2low > F(1, 2) and ln2high < 1, "elementary gap-to-eta conversion")
    require(ln3low > 1, "rational series also certifies the drift comparison")
    low = high = 0
    minimum_complement, minimum_at = scale, 0
    threshold = 1 << 71
    for exponent in range(1, FULL_PERIOD_LIMIT):
        low += low_num
        high += high_num
        integer_part = low >> 96
        require(high >> 96 == integer_part, "alpha interval crosses an integer")
        complement = ((integer_part+1) << 96)-high
        require(complement > threshold, "full-exponent complementary gap exceeds 2^-25")
        if complement < minimum_complement:
            minimum_complement, minimum_at = complement, exponent
    require(minimum_complement == 7373341559091880256221 and minimum_at == 190537,
            "exact exhaustive complementary-gap minimum")
    # For gamma=ceil(alpha*m)-alpha*m, the scan gives gamma>2^-25.
    # Since 0<gamma<1 and 1/2<ln2<1, t=gamma*ln2 lies in(0,1),
    # and 1-exp(-t)>=t/(1+t)>t/2>gamma/4>2^-27.
    return {"series_terms": 80, "dyadic_denominator_bits": 96,
            "alpha_lower_numerator": low_num, "alpha_upper_numerator": high_num,
            "full_period_range": [1, FULL_PERIOD_LIMIT-1],
            "full_periods_checked": FULL_PERIOD_LIMIT-1,
            "complement_threshold_numerator": threshold,
            "minimum_complement_numerator": minimum_complement,
            "minimum_complement_at_full_period": minimum_at,
            "complement_strict_lower": "2^-25", "eta_strict_lower": "2^-27",
            "scope": "All ordinary integer exponents in the stated full-period range."}


def final_periods():
    """Exact powers close all remaining periods, including five large minima."""
    power = 1
    local_closed = 0
    candidates = []
    worst_error, worst_at = F(0), 0
    for period in range(1, FINAL_PERIOD_LIMIT):
        power *= 3
        total = power.bit_length()
        beta = 1 << total
        gap = beta-power
        require(gap > 0, "least positive full gap")
        numerator, denominator = period*beta, 3*gap
        # L<m/(3*eta), eta increases with the full valuation total, so
        # this least-total rational bound applies to every possible total.
        if numerator < LOCAL_LIMIT*denominator:
            local_closed += 1
            continue
        ceiling = -(-numerator//denominator)
        log_ceiling = ceiling.bit_length()
        require(numerator < (1 << log_ceiling)*denominator,
                "strict power-of-two upper bound for the cycle minimum")
        error = (F(12*log_ceiling, 19)+1)/period+F(1, 393216)
        require(error < EPSILON, "residual full-period geometric exclusion")
        candidates.append({"full_period": period, "least_full_total": total,
                           "minimum_upper_ceiling": ceiling,
                           "log_minimum_strict_upper": log_ceiling,
                           "geometric_error_strict_upper": str(error)})
        if error > worst_error:
            worst_error, worst_at = error, period
    require([row["full_period"] for row in candidates] == [12941, 13606, 14271, 14936, 15601],
            "exact residual full-period list")
    require(local_closed+len(candidates) == FINAL_PERIOD_LIMIT-1,
            "no gaps in final full-period coverage")
    require(worst_error == F(125681783, 96683556864) and worst_at == 12941,
            "worst residual geometric error")
    return {"full_period_range": [1, FINAL_PERIOD_LIMIT-1],
            "full_periods_checked": FINAL_PERIOD_LIMIT-1,
            "closed_by_local_minimum": local_closed,
            "residual_geometric_cases": candidates,
            "worst_error_strict_upper": str(worst_error), "worst_at_full_period": worst_at,
            "margin_at_worst_case": str(EPSILON-worst_error),
            "local_minimum_lower": LOCAL_LIMIT,
            "scope": "Every valuation total is covered by monotonicity of the positive gap."}


def local_descent():
    """Every positive odd seed below 18 million reaches a smaller odd seed."""
    steps = maximum = maximum_seed = peak = 0
    digest = sha256()
    require((3*1+1) >> 2 == 1, "induction base at the true 3x+1 fixed point")
    for seed in range(3, LOCAL_LIMIT, 2):
        state, count = seed, 0
        while state >= seed:
            raw = 3*state+1
            valuation = (raw & -raw).bit_length()-1
            state = raw >> valuation
            count += 1
            require(count <= 10000, "bounded local descent guard")
            peak = max(peak, state)
        require(state > 0 and state % 2 == 1 and state < seed, "strict lower odd output")
        steps += count
        if count > maximum:
            maximum, maximum_seed = count, seed
        digest.update(f"{seed}:{state}:{count}\n".encode())
    return {"map": "raw odd-only 3x+1", "odd_seed_range": [3, LOCAL_LIMIT-1],
            "odd_seeds": (LOCAL_LIMIT-2)//2, "odd_steps": steps,
            "maximum_descent_steps": maximum, "maximum_descent_seed": maximum_seed,
            "peak_odd_output": peak, "per_seed_guard": 10000,
            "descent_sha256": digest.hexdigest(), "nontrivial_cycle_minimum_lower": LOCAL_LIMIT,
            "scope": "Exact first descents; strong induction gives convergence to 1 below the stated bound."}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    result = {"schema": "non-half-period-four-mismatch-v2",
              "geometry": complete_geometry(), "direct_rows": direct_row_controls(),
              "boundary_controls": boundary_controls(),
              "coefficient_regression_control": coefficient_regression_control(),
              "actual_controls": actual_controls(), "cutoff_constants": cutoff_constants(),
              "full_exponent_gap": full_exponent_gap(), "final_periods": final_periods(),
              "local_descent": local_descent()}
    encoded = json.dumps(result, sort_keys=True, indent=2)+"\n"
    receipt = HERE/"check_non_half_period.json"
    if sys.argv[1:]:
        receipt.write_text(encoded)
    else:
        require(receipt.read_text() == encoded, "receipt mismatch; inspect before regenerating")
    print(json.dumps({"status": "passed", **result["geometry"]["counts"], "survivors": 0,
                      **result["actual_controls"]["counts"], "standard_cycles": 11,
                      "full_exponents_checked": result["full_exponent_gap"]["full_periods_checked"],
                      "final_periods_checked": result["final_periods"]["full_periods_checked"],
                      "local_odd_seeds": result["local_descent"]["odd_seeds"]}, sort_keys=True))


if __name__ == "__main__":
    main()
