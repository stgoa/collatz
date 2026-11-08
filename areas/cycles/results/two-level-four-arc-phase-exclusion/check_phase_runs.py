"""Exact phase, run and threshold certificate; Python standard library only."""

from fractions import Fraction as F
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CUTOFF = 1 << 34


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def valuation(value):
    require(value != 0, "valuation of zero")
    value = abs(value)
    return (value & -value).bit_length()-1


def constants():
    require(194**32 < (1 << 19)*129**32, "one-arrow logarithmic growth")
    require(3**53 > 1 << 84, "alpha lower bound")
    require(3**5 < 1 << 8 and 3**2 > 1 << 3, "alpha bounds")
    require(F(4, 3)**3 < 3, "residual binary contraction")
    require(F(1)-F(21, 53)/F(19, 32) == F(335, 1007), "density coefficient")
    require(F(1, 3)-F(335, 1007) == F(2, 3021), "density margin")
    require(3021*512+159*(32*(172+342)+13) == 4164051,
            "density dyadic intercept")
    require(159*32*342 == 1740096, "density dyadic slope")
    density_margin = 2*CUTOFF-(4164051+1740096*34)
    require(density_margin == 34296411053 > 0, "density base")
    require(2*4164051-(4164051+1740096) == 2423955 > 0,
            "density induction intercept")
    require(1740096 > 0, "density induction slope")
    require(3*(173+342)+511 == 2056, "phase dyadic intercept")
    require(3*342 == 1026, "phase dyadic slope")
    phase_at_base = F(2056+1026*34, 3*CUTOFF)
    require(193*phase_at_base == F(1782355, 12884901888) < 1,
            "two-rotation error below exact margin")
    require(2056-1026 == 1030 > 0, "phase induction intercept")
    for Q in range(2, 513):
        require(2*((Q+2)//3) <= Q, "at most half twos per block")
        require(3**(2*Q) > 2**(2*(Q+(Q+2)//3)), "every short block expands")
    require(CUTOFF//128 > 512 and 2*CUTOFF//3 > 512,
            "both track intervals exceed every short step")
    require(F(13, 5)*768 == F(9984, 5) < 2048, "two-run multiplier")
    run_margin = CUTOFF-2048*(515+342*34)
    require(run_margin == 17155000320 > 0, "two-run dyadic base")
    require(515-342 == 173 > 0 and 342 > 0, "two-run induction")
    require(72057431991 > CUTOFF, "separate imported period cutoff")
    return dict(cutoff_bits=34, cutoff=CUTOFF, minimum_state=129,
                alpha_lower="84/53", one_arrow_log2_upper="19/32",
                density_coefficient="335/1007", short_product_bound=512,
                density_dyadic_polynomial=[4164051, 1740096],
                density_base_margin=density_margin,
                density_induction_polynomial=[2423955, 1740096],
                phase_dyadic_numerator=[2056, 1026],
                phase_induction_polynomial=[1030, 1026],
                phase_error_times_193_at_base=str(193*phase_at_base),
                two_run_multiplier="9984/5", two_run_relaxed_multiplier=2048,
                two_run_dyadic_polynomial=[515, 342],
                two_run_induction_polynomial=[173, 342],
                two_run_base_margin=run_margin, separately_sourced_minimum_period=72057431991)


def phase_windows():
    cases = windows = positive = negative = 0
    checksum = sha256()
    for m in range(8, 101):
        for k in range(1, m):
            if gcd(k, m) != 1:
                continue
            for Q in range(2, min(13, m)):
                p = (Q*k+m//2)//m
                signed = Q*k-p*m
                j = abs(signed)
                if not j or gcd(p, Q) != 1:
                    continue
                maximum_b = (m-1)//3-j
                if maximum_b < 1:
                    continue
                for b in sorted({1, maximum_b}):
                    require(3*(b+j) < m, "strict expanded-arc hypothesis")
                    word = [int((i*k) % m < b) for i in range(m)]
                    for start in range(m):
                        count = sum(word[(start+t) % m] for t in range(Q))
                        require(count <= (Q+2)//3, "uniform-grid window count")
                        windows += 1
                    cases += 1
                    positive += signed > 0
                    negative += signed < 0
                    checksum.update(f"{m}:{k}:{Q}:{p}:{signed}:{b}\n".encode())
    require(windows == 1629414 and positive and negative, "phase grid coverage")
    return dict(periods=[8, 100], denominators=[2, 12],
                twos_lengths="1 and the largest integer satisfying 3(b+j)<m",
                phases="every chronological start; coprimality covers every track phase",
                cases=cases, windows=windows, positive_residue_cases=positive,
                negative_residue_cases=negative, parameter_sha256=checksum.hexdigest())


def large_phase_edges():
    rows = []
    checks = 0
    for Q in (2, 3, 4, 7, 16, 31, 128, 256, 512):
        for p in sorted({1, Q-1}):
            for j in sorted({1, 512//Q}):
                for sign in (-1, 1):
                    m = CUTOFF
                    while (p*m+sign*j) % Q or gcd((p*m+sign*j)//Q, m) != 1:
                        m += 1
                        require(m < CUTOFF+4096, "large rational phase construction")
                    k = (p*m+sign*j)//Q
                    require(0 < k < m and gcd(k, m) == 1, "large reduced phase")
                    require(Q*k-p*m == sign*j and Q*j <= 512,
                            "large exact phase relation")
                    b = (m-1)//3-j
                    require(3*(b+j) < m and b > m//128, "large nonsparse twos interval")
                    # Membership changes only at these interval endpoints. Their
                    # predecessors include the other side of each boundary.
                    phases = set()
                    for s in range(Q):
                        for endpoint in ((-s*k) % m, (b-s*k) % m):
                            phases.update((endpoint, (endpoint-1) % m))
                    maximum = 0
                    for phase in sorted(phases):
                        count = sum((phase+s*k) % m < b for s in range(Q))
                        require(count <= (Q+2)//3, "large phase endpoint count")
                        maximum = max(maximum, count)
                        checks += 1
                    rows.append(dict(m=m, k=k, p=p, Q=Q, signed_j=sign*j,
                                     b=b, boundary_phases=len(phases), maximum_twos=maximum))
    require(any(row["Q"] == 512 for row in rows), "denominator-512 edge")
    return dict(cases=len(rows), endpoint_phase_checks=checks, records=rows)


def positive_one_runs(word):
    m = len(word)
    require(any(letter != 1 for letter in word), "nonconstant word for run cuts")
    answer = []
    for start in range(m):
        if word[start] == 1 and word[start-1] != 1:
            length = 0
            while word[(start+length) % m] == 1:
                length += 1
                require(length < m, "ones run terminates")
            answer.append((start, length))
    return answer


def small_step_runs():
    templates = spikes = pairs = single = endpoint_spikes = 0
    checksum = sha256()
    for m in range(8, 82):
        for j in range(1, min(9, m)):
            if gcd(j, m) != 1:
                continue
            for b in sorted({j+1, m//3-1}):
                if not (j < b and j < m-b):
                    continue
                for sign in (-1, 1):
                    base = [2 if (sign*j*i) % m < b else 1 for i in range(m)]
                    base_runs = positive_one_runs(base)
                    require(len(base_runs) == j, "exact number of small-step binary runs")
                    lower, upper = (m-b)//j, (m-b+j-1)//j
                    require(all(lower <= length <= upper for _, length in base_runs),
                            "floor/ceiling binary run lengths")
                    templates += 1
                    for spike in range(m):
                        if base[spike] != 1:
                            continue
                        word = base.copy()
                        word[spike] = 3
                        runs = positive_one_runs(word)
                        require(runs, "a positive run survives the spike")
                        for i, (_, length) in enumerate(runs):
                            require(length+runs[(i+1) % len(runs)][1] >= lower-1,
                                    "two consecutive positive runs include full length")
                            pairs += 1
                        single += len(runs) == 1
                        endpoint_spikes += base[spike-1] == 2 or base[(spike+1) % m] == 2
                        spikes += 1
                        checksum.update(f"{m}:{j}:{b}:{sign}:{spike}:{runs}\n".encode())
    require(single and endpoint_spikes, "zero split and one-run boundary controls")
    return dict(periods=[8, 81], steps=[1, 8], signs=[-1, 1],
                twos_lengths="j+1 and floor(m/3)-1 when both intervals exceed j",
                spike_positions="every binary-one site", templates=templates,
                spiked_words=spikes, consecutive_run_pairs=pairs,
                one_surviving_run_cases=single, endpoint_spike_cases=endpoint_spikes,
                parameter_sha256=checksum.hexdigest())


def integral_runs():
    cases = 0
    maximum_last = 0
    for length in range(1, 33):
        for u in range(1, 64, 2):
            x = (1 << (length+1))*u-1
            current = x
            for _ in range(length):
                require(valuation(3*current+1) == 1, "exact initial ones")
                current = (3*current+1)//2
            e = valuation(3*current+1)
            require(e >= 2, "run ends at a non-one letter")
            following = (3*current+1) >> e
            require(following == (3**(length+1)*u-1)//(1 << (e-1)),
                    "exact terminal run formula")
            require((following+1)*2 <= 3**(length+1)*u+1,
                    "terminal valuation at least two")
            require(following+1 < 3**(length+1)*u, "strict intermediate bound")
            require((following+1)**5 < (x+1)**8, "rational relaxation of power chain")
            require(valuation(x+1) == length+1, "exact binary run-start valuation")
            maximum_last = max(maximum_last, e)
            cases += 1
    return dict(ones_lengths=[1, 32], odd_quotients=[1, 63], cases=cases,
                maximum_terminal_valuation=maximum_last,
                scope="integer orbit segments; not asserted to be cycles")


def local_minimum():
    checksum = sha256()
    steps = maximum = 0
    for seed in range(3, 129, 2):
        current, count = seed, 0
        checksum.update(f"{seed}:".encode())
        while current != 1:
            require(count < 10000, "unfinished local descent")
            raw = 3*current+1
            current = raw >> valuation(raw)
            checksum.update(f"{current},".encode())
            count += 1
        steps += count
        maximum = max(maximum, count)
    require(maximum == 43, "local descent longest trajectory")
    return dict(odd_seeds=[3, 127], count=63, odd_steps=steps,
                maximum_steps=maximum, trajectory_sha256=checksum.hexdigest())


def reduced_cycle(word):
    intercept = total = 0
    for letter in word:
        intercept = 3*intercept+(1 << total)
        total += letter
    D = (1 << total)-3**len(word)
    if D <= 0:
        return None
    common = gcd(D, intercept)
    q, current = D//common, intercept//common
    states = []
    for letter in word:
        states.append(current)
        raw = 3*current+q
        require(valuation(raw) == letter, "reduced exact valuation")
        current = raw >> letter
    require(current == states[0] and len(set(states)) == len(states),
            "primitive reduced cycle closes")
    return q, states


def check_addend_runs(word, states, q):
    count = 0
    for start, length in positive_one_runs(word):
        x = states[start]
        e = word[(start+length) % len(word)]
        following = states[(start+length+1) % len(word)]
        require(valuation(x+q) == length+1, "addend-aware binary start valuation")
        u = (x+q) >> (length+1)
        require((1 << (e-1))*following == 3**(length+1)*u-q,
                "addend-aware exact run equation")
        require((following+q)*2 <= 3**(length+1)*u+q,
                "addend-aware terminal bound")
        count += 1
    return count


def family_controls():
    words = arrows = run_checks = envelopes = 0
    q_min = None
    checksum = sha256()
    for m in range(4, 13):
        for a in range(1, m-2):
            for b in range(1, m-a-1):
                c = m-1-a-b
                if c < 1:
                    continue
                for h in range(1, m):
                    if gcd(h, m) != 1:
                        continue
                    k = pow(h, -1, m)
                    for V in (3, 4, 9, 20):
                        track = [V]+[1]*a+[2]*b+[1]*c
                        word = [0]*m
                        for i, letter in enumerate(track):
                            word[(i*h) % m] = letter
                        cycle = reduced_cycle(word)
                        if cycle is None:
                            continue
                        q, states = cycle
                        require(q > 1, "finite family controls do not have denominator one")
                        require(sum(word[i] != word[(i+h) % m] for i in range(m)) == 4,
                                "exact four mismatches")
                        words += 1
                        arrows += m
                        q_min = q if q_min is None else min(q_min, q)
                        run_checks += check_addend_runs(word, states, q)
                        for Q in range(2, m):
                            p = (Q*k+m//2)//m
                            j = abs(Q*k-p*m)
                            if not j or gcd(p, Q) != 1 or 3*(b+j) >= m:
                                continue
                            require(states[1]*3**(Q-1) < min(states)*4**(Q-1),
                                    "positive-addend post-spike envelope")
                            envelopes += 1
                        checksum.update(f"{m}:{a}:{b}:{c}:{h}:{V}:{q}\n".encode())
    require(envelopes > 0 and words > 0, "genuine family controls with phase envelopes")
    return dict(periods=[4, 12], spike_values=[3, 4, 9, 20],
                coverage="all positive arc lengths and coprime steps in this finite range, D>0",
                reduced_cycles=words, exact_arrows=arrows, addend_run_checks=run_checks,
                post_spike_envelopes=envelopes, minimum_reduced_addend=q_min,
                parameter_sha256=checksum.hexdigest(),
                failed_exclusion_hypothesis="q=1; these are actual integer 3x+q cycles")


def actual_controls():
    path = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = runs = witnesses = 0
    for row in rows:
        word, states, q = row["valuations"], row["states"], row["d"]
        m = len(word)
        require(len(set(states)) == m and q in (5, 7, 13, 61), "primitive standard control")
        for i, letter in enumerate(word):
            raw = 3*states[i]+q
            require(valuation(raw) == letter and raw >> letter == states[(i+1) % m],
                    "standard actual cycle arrow")
            arrows += 1
        runs += check_addend_runs(word, states, q)
        for h in range(1, m):
            cuts = [i for i in range(m) if word[i] != word[(i+h) % m]]
            require(cuts, "primitive control has a mismatch")
            for cut in cuts:
                start = (cut+1) % m
                length = total = 0
                while word[(start+length) % m] == word[(start+length+h) % m]:
                    total += word[(start+length) % m]
                    length += 1
                    require(length < m, "agreeing control run terminates")
                end = (start+length) % m
                difference = states[(start+h) % m]-states[start]
                require(difference % (1 << (total+1)) == 0 and difference != 0,
                        "binary paired-state witness")
                require(states[(end+h) % m]-states[end] ==
                        2*3**length*(difference//(1 << (total+1))), "ternary paired-state witness")
                require(max(states) > 2*3**length, "positive end witness")
                witnesses += 1
    require(len(rows) == 11 and arrows == 106, "all standard cycle fixtures")
    return dict(fixture_sha256=sha256(path.read_bytes()).hexdigest(), cycles=len(rows),
                exact_arrows=arrows, addend_run_checks=runs, paired_run_witnesses=witnesses,
                scope="the addend is retained; q=1 minimum and growth estimates are not applied")


def replay_dependencies():
    dependencies = [
        ("areas/cycles/results/sparse-two-level-four-arc-exclusion/check_four_arcs.py",
         "areas/cycles/results/sparse-two-level-four-arc-exclusion/check_four_arcs.json"),
        ("areas/cycles/results/cycle-length-lower-bound-from-convergents/check_cycle_length_convergents.py",
         "areas/cycles/results/cycle-length-lower-bound-from-convergents/cycle_length_convergents.json"),
    ]
    records = []
    for script, receipt in dependencies:
        before = (ROOT/receipt).read_bytes()
        command = [sys.executable]+(["-O"] if sys.flags.optimize else [])+[script]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        require(result.returncode == 0, f"dependency replay failed: {script}\n{result.stdout}\n{result.stderr}")
        require((ROOT/receipt).read_bytes() == before, "dependency replay changed its receipt")
        records.append(dict(script=script, script_sha256=sha256((ROOT/script).read_bytes()).hexdigest(),
                            receipt=receipt, receipt_sha256=sha256(before).hexdigest(),
                            outcome="passed; stored receipt unchanged"))
    period = json.loads((ROOT/dependencies[1][1]).read_text())["V3"]["2^71"]["least_m"]
    require(int(period) == 72057431991 > CUTOFF, "replayed period input for corollary")
    return dict(records=records, corollary_minimum_odd_period=int(period),
                external_convergence_computation_replayed=False)


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="two-level-phase-runs-v1", constants=constants(),
                   phase_windows=phase_windows(), large_phase_edges=large_phase_edges(),
                   small_step_runs=small_step_runs(), integral_runs=integral_runs(),
                   local_minimum=local_minimum(), family_controls=family_controls(),
                   actual_controls=actual_controls(), dependency_replays=replay_dependencies())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    target = HERE / "check_phase_runs.json"
    if sys.argv[1:]:
        target.write_text(encoded)
    else:
        require(target.read_text() == encoded, "receipt differs; inspect and regenerate")
    print(json.dumps(dict(result="passed", windows=receipt["phase_windows"]["windows"],
                          spiked_run_words=receipt["small_step_runs"]["spiked_words"],
                          family_cycles=receipt["family_controls"]["reduced_cycles"],
                          integral_runs=receipt["integral_runs"]["cases"],
                          standard_cycles=receipt["actual_controls"]["cycles"],
                          dependency_replays=len(receipt["dependency_replays"]["records"])),
                     sort_keys=True))


if __name__ == "__main__":
    main()
