"""Exact constants, track identities, ones-run controls and actual cycles."""

from fractions import Fraction as F
from hashlib import sha256
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
    require(value != 0, "valuation at zero")
    value = abs(value)
    return (value & -value).bit_length() - 1


def constants():
    mean_margin = 2**8 * 129**5 - 388**5
    require(mean_margin > 0, "mean valuation below 8/5 at minimum129")
    require(F(2, 3) > F(1, 2), "first positive log-series term")
    require(3 * 129 * F(2, 3) == 258, "drift denominator")
    require(3**2 > 2**3 and 3**32 < 2**51, "alpha bounds")
    require(F(2, 387) < F(1, 160), "rise drift bound")
    require(F(51, 32) + F(1, 160) == F(8, 5), "rise factor")
    require(F(8, 5)**5 - 1 < 10, "four-mismatch rise power")
    coefficient = F(3, 8) - F(20, 64) - F(10, 258)
    require(coefficient == F(49, 2064), "large-letter coefficient")
    first_base = coefficient * 2**22 - (11 * (172 + 342 * 23) + 11)
    first_increment = coefficient * 2**22 - 11 * 342
    require(first_base == F(1437715, 129) and first_base > 0,
            "large-letter dyadic base")
    require(first_increment > 0, "dyadic margin increases at all larger indices")
    multiplicity_slope = F(39, 64) - F(3, 5)
    multiplicity_margin = multiplicity_slope * 2**22 - 39
    require(multiplicity_slope == F(3, 320) and multiplicity_margin == F(196413, 5),
            "39 maximum letters exceed the total budget")
    require(multiplicity_margin > 0, "multiplicity base and all larger lengths")
    require(38 + 1 == 39, "non-one count includes the singleton")
    require(2**23 < 5**10 and 7 * 39 < 10 * 28,
            "alpha to the39 below2to28")
    require(28 + 1 == 29 and 172 + 1 == 173, "ones-run constants")
    require(173 + 342 == 515, "second dyadic numerator")
    final_numerator = 515 + 342 * 43
    require(final_numerator == 15221 < 2**14, "final dyadic base")
    # Twice the old numerator minus the next one is 173+342*d.
    require(2 * 515 - (515 + 342) == 173 and 2 * 342 - 342 == 342,
            "final induction identity")
    require(173 + 342 * 43 > 0 and 342 > 0,
            "final induction positive for every d>=43")
    require(29 + 14 == 43, "final cutoff bits")
    return dict(minimum_state=129, mean_power_margin=mean_margin,
                drift_denominator=258, alpha_upper="51/32", rise_upper="8/5",
                rise_power_margin=str(11 - F(8, 5)**5),
                large_letter_cutoff_bits=22, large_letter_denominator=64,
                large_letter_coefficient=str(coefficient), first_dyadic_margin=str(first_base),
                first_increment_margin=str(first_increment),
                maximum_label_count=38, non_one_count=39,
                multiplicity_margin=str(multiplicity_margin),
                ones_run_power_bits=28, length_coefficient_bits=29,
                final_dyadic_numerator=final_numerator, final_dyadic_margin=2**14-final_numerator,
                final_induction_shifted_coefficients=[173+342*43, 342],
                final_cutoff_bits=43)


def local_descent():
    rows = []
    for seed in range(3, 129, 2):
        state, steps, peak = seed, 0, seed
        checksum = sha256(f"{seed}\n".encode())
        while state != 1:
            require(steps < 10000, "unfinished local descent")
            raw = 3 * state + 1
            state = raw >> valuation(raw)
            require(state > 0 and state % 2 == 1, "positive odd descent")
            steps += 1
            peak = max(peak, state)
            checksum.update(f"{state}\n".encode())
        rows.append(dict(seed=seed, odd_steps=steps, peak=peak,
                         trajectory_sha256=checksum.hexdigest()))
    require(len(rows) == 63, "complete local range")
    return dict(seed_range=[3, 127], odd_seeds=len(rows),
                maximum_steps=max(row["odd_steps"] for row in rows), records=rows)


def integral_ones_runs():
    checksum = sha256()
    runs = arrows = empty = 0
    terminal_valuations = set()
    for n in range(1, 65):
        for z in range(1, 64, 2):
            start = 2**n * z - 1
            state = start
            for _ in range(n-1):
                raw = 3 * state + 1
                require(valuation(raw) == 1, "exact internal one")
                state = raw >> 1
                arrows += 1
            require(state == 2 * 3**(n-1) * z - 1, "ones-run endpoint")
            raw = 3 * state + 1
            e = valuation(raw)
            require(e >= 2, "next letter is non-one")
            target = raw >> e
            require(target == (3**n * z - 1) // 2**(e-1), "exact next-cut state")
            require((3**n * z - 1) % 2**(e-1) == 0, "exact next-cut quotient")
            require(valuation(start+1) == n and start+1 >= 2**n, "chunk length witness")
            require(target+1 <= F(3**n * z + 1, 2) < 3**n * z,
                    "exact rational half of the logarithmic recursion")
            require(target > 0 and target % 2 == 1, "odd positive target")
            checksum.update(f"{n}:{z}:{start}:{state}:{e}:{target}\n".encode())
            terminal_valuations.add(e)
            runs += 1
            arrows += 1
            empty += n == 1
    require(runs == 2048 and empty == 32 and max(terminal_valuations) > 2,
            "ones-run finite coverage")
    return dict(n_range=[1, 64], odd_z_range=[1, 63], runs=runs, exact_arrows=arrows,
                empty_ones_runs=empty, terminal_valuations=sorted(terminal_valuations),
                exact_runs_sha256=checksum.hexdigest(),
                scope="Integral positive 3x+1 segments; no assertion of closed cycles.")


def reduced_cycle(word):
    m, total = len(word), sum(word)
    D = 2**total - 3**m
    require(D > 0, "positive-D control")
    C = prefix = 0
    for i, letter in enumerate(word):
        C += 3**(m-1-i) * 2**prefix
        prefix += letter
    common = gcd(C, D)
    addend, state = D // common, C // common
    states = []
    for letter in word:
        states.append(state)
        raw = 3 * state + addend
        require(valuation(raw) == letter, "reduced-cycle valuation")
        state = raw >> letter
    require(state == states[0] and len(set(states)) == m, "primitive control closure")
    require(all(x > 0 and x % 2 == 1 for x in states), "positive odd reduced states")
    return addend, states


def check_chunks(states, word, addend):
    m = len(word)
    cuts = [(i+1) % m for i, letter in enumerate(word) if letter > 1]
    require(cuts, "control contains a non-one letter")
    counts = dict(chunks=0, empty_ones_runs=0, scaled_odd_quotient_below_addend=0)
    covered = 0
    for start in cuts:
        length = 0
        while word[(start+length) % m] == 1:
            require(length < m, "ones run terminates")
            length += 1
        end = (start+length) % m
        e = word[end]
        n = length+1
        x, y, target = states[start], states[end], states[(end+1) % m]
        require(valuation(x+addend) == n, "addend-aware exact chunk length")
        z = (x+addend) >> n
        require(z > 0 and z % 2 == 1, "positive odd scaled quotient")
        require(y+addend == 2 * 3**length * z, "addend-aware ones-run identity")
        require(2**(e-1) * target == 3**n * z-addend, "addend-aware next state")
        require(target+addend <= F(3**n * z+addend, 2), "addend-aware half bound")
        covered += n
        counts["chunks"] += 1
        counts["empty_ones_runs"] += length == 0
        counts["scaled_odd_quotient_below_addend"] += z < addend
    require(covered == m, "chunks partition the raw odd period")
    return counts


def track_grid():
    words = outer = middle = cycles = arrows = chunks = small_quotients = 0
    checksum = sha256()
    for m in range(4, 15):
        for h in range(1, m):
            if gcd(h, m) != 1:
                continue
            for a in range(1, m-2):
                for b in range(1, m-a-1):
                    c = m-1-a-b
                    for t in range(3, 7):
                        for V in range(2, t):
                            for A, B in ((1, t), (t, 1)):
                                track = [V]+[A]*a+[B]*b+[A]*c
                                word = [0]*m
                                for j, letter in enumerate(track):
                                    word[(m-1+j*h) % m] = letter
                                require(word.count(V) == 1 and max(word) == t > V,
                                        "unique nonmaximum singleton")
                                mismatches = sum(word[i] != word[(i+h) % m] for i in range(m))
                                variation = sum(abs(word[i]-word[(i+h) % m]) for i in range(m))
                                require(mismatches == 4, "exact four track mismatches")
                                require(variation == 2*abs(V-A)+2*abs(A-B) < 4*t,
                                        "exact label variation")
                                r = word.count(t)
                                require(r == (b if A == 1 else a+c), "maximum-label multiplicity")
                                require(sum(word)-m == r*(t-1)+V-1, "exact excess budget")
                                require(sum(letter > 1 for letter in word) == r+1,
                                        "number of non-one letters")
                                checksum.update(f"{m}:{h}:{a}:{b}:{c}:{V}:{A}:{B}:{variation}\n".encode())
                                words += 1
                                outer += A == t
                                middle += B == t
                                if m <= 8 and t <= 5 and 2**sum(word) > 3**m:
                                    addend, states = reduced_cycle(word)
                                    counts = check_chunks(states, word, addend)
                                    cycles += 1
                                    arrows += m
                                    chunks += counts["chunks"]
                                    small_quotients += counts["scaled_odd_quotient_below_addend"]
    require(words > 0 and outer == middle and cycles > 0 and small_quotients > 0,
            "both arrangements and actual addend-aware controls")
    return dict(lengths=[4, 14], maximum_label_range=[3, 6], singleton_range="2<=V<t",
                all_coprime_steps=True, all_positive_arc_lengths=True,
                track_words=words, outer_maximum=outer, middle_maximum=middle,
                track_sha256=checksum.hexdigest(), reduced_cycle_maximum_length=8,
                reduced_cycle_maximum_label=5, reduced_cycles=cycles, exact_cycle_arrows=arrows,
                exact_cycle_chunks=chunks, scaled_quotients_below_addend=small_quotients,
                scope="Geometry and actual reduced-cycle identities, not a finite absence claim.")


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    records = []
    arrows = runs = empty = chunks = small_quotients = 0
    for row in json.loads(path.read_text())["cycles"]:
        states, word, d = row["states"], row["valuations"], row["d"]
        m = len(word)
        require(m == len(states) and len(set(states)) == m, "primitive actual fixture")
        require(all(x > 0 and x % 2 == 1 for x in states), "positive odd fixture")
        for i, letter in enumerate(word):
            raw = 3 * states[i]+d
            require(valuation(raw) == letter and raw >> letter == states[(i+1) % m],
                    "actual fixture arrow")
            arrows += 1
        parts = check_chunks(states, word, d)
        chunks += parts["chunks"]
        small_quotients += parts["scaled_odd_quotient_below_addend"]
        for h in range(1, m):
            mismatches = [i for i in range(m) if word[i] != word[(i+h) % m]]
            require(mismatches, "primitive word has no invariant nonidentity rotation")
            longest = 0
            for mismatch in mismatches:
                start = (mismatch+1) % m
                length = total = 0
                while word[(start+length) % m] == word[(start+length+h) % m]:
                    require(length < m, "maximal agreement run terminates")
                    total += word[(start+length) % m]
                    length += 1
                end = (start+length) % m
                z_start = states[(start+h) % m]-states[start]
                z_end = states[(end+h) % m]-states[end]
                require(z_start != 0 and z_end != 0, "distinct paired states")
                require(z_start % 2**(total+1) == 0, "binary run witness")
                witness = z_start // 2**(total+1)
                require(z_end == 2 * 3**length * witness, "ternary run witness")
                require(max(states) > 2 * 3**length, "strict maximum-state witness")
                runs += 1
                empty += length == 0
                longest = max(longest, length)
            require(longest >= (m-1)//len(mismatches), "pigeonhole agreeing run")
        require(d in (5, 7, 13, 61), "standard addend controls")
        records.append(dict(addend=d, period=m, minimum=min(states), chunks=parts,
                            failed_hypothesis="The cycle addend is not1; no normalized integrality is assumed."))
    require(len(records) == 11 and arrows == 106 and small_quotients > 0,
            "all eleven standard controls and a q-scaling obstruction")
    return dict(records=records, fixture_sha256=sha256(path.read_bytes()).hexdigest(),
                actual_cycles=len(records), arrows=arrows, agreeing_runs=runs,
                empty_agreeing_runs=empty, chunks=chunks,
                scaled_quotients_below_addend=small_quotients)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    result = dict(schema="background-maximum-four-arc-v1", constants=constants(),
                  local_descent=local_descent(), integral_ones_runs=integral_ones_runs(),
                  track_geometry=track_grid(), actual_controls=actual_controls())
    encoded = json.dumps(result, indent=2, sort_keys=True)+"\n"
    receipt = HERE / "check_background_maximum.json"
    if sys.argv[1:]:
        receipt.write_text(encoded)
    else:
        require(receipt.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(status="passed", track_words=result["track_geometry"]["track_words"],
                          reduced_cycles=result["track_geometry"]["reduced_cycles"],
                          integral_ones_runs=result["integral_ones_runs"]["runs"],
                          local_seeds=result["local_descent"]["odd_seeds"],
                          actual_cycles=result["actual_controls"]["actual_cycles"]), sort_keys=True))


if __name__ == "__main__":
    main()
