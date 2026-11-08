"""Exact numerical closure and genuine cycle controls for two clustered arcs.

Basic valuation, reduced-cycle, and addend-aware run checks are reused from
contiguous-maximum-four-arc-exclusion/check_maximum_arc.py (Codex four-arc
lane, GPT-6 Astra). The universal logarithm-gap certificate is replayed
unchanged with source and receipt hashes; no external convergence run is
performed. Finite cycle controls are not an absence proof.
"""
from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import subprocess
import sys

F = Fraction
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
BOOTSTRAP = "areas/cycles/results/general-three-label-four-arc-exclusion/check_bootstrap.py"
BOOTSTRAP_SHA256 = "daf474215cac3782aea1990817c3fcbeaf05d65ad43cbe85156a2190b68c792d"
BOOTSTRAP_RECEIPT_SHA256 = "11f2af760caf5ee16cce5ea693306added37f2bda5b059a085d28e039287d263"

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


def constants():
    require(388**5 < 2**8*129**5, "mean below8/5")
    require(3**32 < 2**51 and F(2, 387) < F(1, 160), "kappa below8/5")
    require(F(51, 32)+F(1, 160) == F(8, 5), "kappa addition")
    require(2**3 < 3**2 and 3**80 < 2**127, "exact alpha comparisons")
    require(F(257, 258)-F(255, 256) == F(1, 33024) > 0,
            "profile coefficient below3/8")
    coefficient = F(3, 8)-F(20, 64)-F(10, 258)
    require(F(8, 5)**5 < 11 and coefficient == F(49, 2064), "rise forcing constants")
    base_margin = coefficient*2**22-11*(172+342*23)-11
    require(base_margin == F(1437715, 129) > 0, "maximum forcing dyadic base")
    require(coefficient*2**22 > 11*342, "maximum forcing dyadic induction")
    multiplicity_margin = (F(39, 64)-F(3, 5))*2**22-39
    require(multiplicity_margin == F(196413, 5) > 0, "at most38 maxima")
    require(104*38 == 3952, "uniform clustered error margin")
    require(3*2**17*F(2, 3) == 2**18 and F(1, 2**18)*F(2, 3) == F(1, 393216),
            "general local drift margin")
    require(F(1, 258)*F(2, 3) == F(1, 387), "isolated local drift margin")
    require(F(2**112, 3)+1 < 2**112 and 2*48+1 == 97, "post-gap height/digit bounds")
    records = []
    for name, margin, drift, expected_scale, expected_base, expected_final, bits in [
        ("clustered", F(1, 3952), F(1, 393216), F(64749568, 24329),
         F(7145023419698118656, 121645), F(425886010048512, 121645), 32),
        ("isolated", F(1, 208), F(1, 387), F(53664, 179),
         F(5921746640760288, 895), F(352971418176, 895), 29),
    ]:
        scale = 1/(F(3, 2)*(margin-drift))
        require(scale == expected_scale and margin > drift, "error absorption")
        x0, x1 = 515, 342
        z0, z1 = 27*3+64*x0, 27*2+64*x1
        polynomial = [scale*(x0+F(6, 5)*x0*z0+2),
                      scale*(x1+F(6, 5)*(x0*z1+x1*z0)),
                      scale*F(6, 5)*x1*z1]
        require(all(value > 0 for value in polynomial), "positive cutoff polynomial")
        initial = sum(value*48**i for i, value in enumerate(polynomial))
        require(initial == expected_base < 2**48, "initial cutoff comparison")
        require(F(49, 48)**2 < 2, "all larger dyadic bands")
        B = 112+F(6, 5)*112*(27*97+64*112)+2
        require(B == F(6577434, 5), "post-gap common numerator")
        final = scale*B
        require(final == expected_final < 2**bits, "final EXT1-only cutoff")
        require(final > 2**22, "small periods omitted by multiplicity already satisfy bound")
        records.append(dict(case=name, geometry_margin=str(margin), drift_upper=str(drift),
                            scale=str(scale), polynomial=[str(x) for x in polynomial],
                            preliminary_cutoff_bits=48, initial_upper=str(initial),
                            initial_margin=str(2**48-initial), induction_ratio="2401/2304",
                            post_gap_Y_upper=112, post_gap_n_upper=97, common_B=str(B),
                            full_period_upper=str(final), integer_period_upper=final.numerator//final.denominator,
                            EXT1_only_cutoff_bits=bits, final_dyadic_margin=str(2**bits-final)))
    return dict(maximum_forcing_coefficient=str(coefficient), maximum_forcing_base_margin=str(base_margin),
                maximum_count_margin=str(multiplicity_margin), maximum_count=38,
                maximum_count_minimum_period=2**22, cases=records)


def replay_bootstrap():
    path = ROOT/BOOTSTRAP
    receipt_path = path.with_suffix(".json")
    source, raw = path.read_bytes(), receipt_path.read_bytes()
    require(sha256(source).hexdigest() == BOOTSTRAP_SHA256, "pinned bootstrap source")
    require(sha256(raw).hexdigest() == BOOTSTRAP_RECEIPT_SHA256, "pinned bootstrap receipt")
    command = [sys.executable]
    if sys.flags.optimize:
        command.append("-O")
    command.append(str(path))
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    require(result.returncode == 0, "bootstrap replay failed: "+result.stdout+result.stderr)
    require(path.read_bytes() == source and receipt_path.read_bytes() == raw,
            "dependency replay must leave source and receipt unchanged")
    data = json.loads(raw)
    gap = data["exact_gap"]
    require(gap["eta_power"] == 64 and gap["positive_gap_power"] == 62,
            "universal arithmetic gap outputs")
    require(gap["upper_convergent"]["q"] > 2**48, "gap covers all preliminary lengths")
    require(data["final_comparison"]["declared_period_lower_bound"] == 72057431991,
            "separate full-period lower bound")
    require(72057431991 > 2**32, "Barina corollaries")
    return dict(source=BOOTSTRAP, source_sha256=BOOTSTRAP_SHA256,
                receipt_sha256=BOOTSTRAP_RECEIPT_SHA256, replay_status="passed",
                exact_gap_scope="Every integer0<m<2^48 with E-m*log2(3)>0; independent of the valuation word and Barina.",
                eta_power=64, lower_convergent=gap["lower_convergent"],
                upper_convergent=gap["upper_convergent"],
                imported_odd_period_lower=72057431991,
                external_convergence_replayed=False,
                source_scope="The dependency's separate Barina comparison is replayed, but only its universal arithmetic gap is used for the EXT1-only bound.")


def local_descent():
    digest = sha256()
    steps_total = peak = maximum = 0
    small_steps = small_maximum = 0
    for seed in range(3, 2**17, 2):
        state, steps = seed, 0
        while state >= seed:
            require(steps < 10000, "unfinished local descent")
            raw = 3*state+1
            state = raw >> valuation(raw)
            require(state > 0 and state % 2 == 1, "positive odd local output")
            digest.update(f"{seed}:{state}\n".encode())
            steps += 1
            peak = max(peak, state)
        steps_total += steps
        maximum = max(maximum, steps)
        if seed < 129:
            small_steps += steps
            small_maximum = max(small_maximum, steps)
    return dict(seed_range=[3, 2**17-1], odd_seeds=65535, exact_steps=steps_total,
                maximum_steps=maximum, maximum_output=peak, descent_sha256=digest.hexdigest(),
                isolated_subrange=dict(seed_range=[3, 127], odd_seeds=63,
                                       exact_steps=small_steps, maximum_steps=small_maximum),
                scope="Every seed descends below itself; strong induction gives convergence throughout the finite range.")


def family_controls():
    geometries = cycles = arrows = factors = runs = isolated = 0
    directions = [0, 0]
    digest = sha256()
    for m in range(4, 13):
        for a in range(1, m-2):
            for b in range(1, m-a-1):
                for c in range(1, m-a-b):
                    d, r = m-a-b-c, a+c
                    for h in range(1, m):
                        if gcd(h, m) != 1 or r*min(h, m-h) >= m:
                            continue
                        k = pow(h, -1, m)
                        K = continued_fraction_sum(k, m)
                        for t in (2, 3, 7):
                            for V in (t+1, t+9):
                                for A, B in ((1, t), (t, 1)):
                                    track = [V]*a+[A]*b+[V]*c+[B]*d
                                    word = [0]*m
                                    for j, letter in enumerate(track):
                                        word[(j*h) % m] = letter
                                    template = [A if letter == V else letter for letter in word]
                                    mismatch = {i for i in range(m) if word[i] != word[(i+h) % m]}
                                    expected = {((a-1)*h) % m, ((a+b-1)*h) % m,
                                                ((a+b+c-1)*h) % m, ((m-1)*h) % m}
                                    require(mismatch == expected and len(expected) == 4, "four distinct mismatch boundaries")
                                    variation = sum(abs(word[i]-word[(i+h) % m]) for i in range(m))
                                    require(variation == 2*(V-A)+2*(V-B) < 4*V, "variation independent of arc multiplicities")
                                    require(sum(word)-sum(template) == r*(V-A), "template edit identity")
                                    high = [i+1 for i in range(m) if word[i] == V]
                                    # State i has coordinate(i+1)/m, not i/m: pre-drop convention.
                                    profile = [r*(i+1)-m*sum(z < i+1 for z in high) for i in range(m)]
                                    for start in range(m):
                                        total = number = 0
                                        for length in range(1, m):
                                            index = (start+length-1) % m
                                            total += template[index]
                                            number += word[index] == V
                                            end = (start+length) % m
                                            require(profile[end]-profile[start] == r*length-m*number,
                                                    "exact wrapped pre-drop profile identity")
                                            require(abs(m*total-sum(template)*length) <= 2*(t-1)*(K-1)*m,
                                                    "inverse-clock weighted discrepancy")
                                            factors += 1
                                    geometries += 1
                                    isolated += r == 2
                                    directions[h > m//2] += 1
                                    cycle = reduced_cycle(word)
                                    if cycle is None:
                                        continue
                                    q, states = cycle
                                    require(q > 1, "finite controls have their actual nonunit addend")
                                    runs += addend_runs(word, states, q)
                                    cycles += 1
                                    arrows += m
                                    digest.update(f"{m}:{a}:{b}:{c}:{d}:{h}:{A}:{B}:{V}:{q}:{states}\n".encode())
    require(all(directions) and isolated > 0 and cycles > 0 and runs > 0, "control coverage")
    return dict(periods=[4, 12], all_positive_arc_lengths=True,
                track_steps="Every coprime h with(a+c)*min(h,m-h)<m; both orientations.",
                lower_labels=[2, 3, 7], maximum_values="t+1 and t+9", lower_arrangements="both",
                geometry_words=geometries, isolated_words=isolated, orientation_counts=directions,
                exact_proper_factors=factors, actual_reduced_cycles=cycles, exact_arrows=arrows,
                addend_ones_runs=runs, control_sha256=digest.hexdigest(),
                scope="Actual3x+q cycles verify transfer identities. Finite absence at q1 is not the proof.")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: checker [--write-receipt]")
    receipt = dict(schema="clustered-two-arcs-arithmetic-v1", constants=constants(),
                   bootstrap=replay_bootstrap(), local_descent=local_descent(),
                   family_controls=family_controls(), standard_controls=standard_controls())
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    destination = HERE/"check_clustered_arcs.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps(dict(status="passed", local_seeds=receipt["local_descent"]["odd_seeds"],
                          geometry_words=receipt["family_controls"]["geometry_words"],
                          actual_cycles=receipt["family_controls"]["actual_reduced_cycles"],
                          standard_cycles=receipt["standard_controls"]["cycles"],
                          integer_period_upper=[row["integer_period_upper"] for row in receipt["constants"]["cases"]]),
                     sort_keys=True))


if __name__ == "__main__":
    main()
