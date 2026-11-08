"""Exact geometry, minimum-run, discrepancy and actual-cycle controls.

The finite grids below test the manuscript's transfers. They are not an
enumeration of the unbounded family. Reduced cycles keep their true addend.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations
import json
from math import gcd
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def v2(value):
    require(value > 0, "positive valuation argument")
    return (value & -value).bit_length()-1


def constants():
    require(194**8 < 27*129**8, "shared geometric slope below3/8")
    require(388**5 < 2**8*129**5, "cycle mean below8/5")
    require(3**2 > 2**3, "alpha above3/2")
    error = F(173+342*23, 2**22)+F(1, 384)
    require(error == F(56885, 12582912) < F(1, 193), "weighted expanding error")
    require(515-342 > 0, "dyadic error decreases from2^22 onward")
    require(F(2, 512)/F(3, 2) == F(1, 384), "weighted discrepancy transfer")
    margin = F(95, 256)*2**22-(172+342*23)
    require(margin == 1548442 > 0, "contracting-mean contradiction base")
    require(514-342 > 0, "contracting dyadic induction")
    return dict(minimum=129, weighted_complexity_coefficient=512,
                cutoff_bits=22, expanding_error_at_base=str(error),
                geometric_error_threshold="1/193", contracting_base_margin=str(margin))


def minimum_runs():
    cases = arrows = 0
    checksum = sha256()
    for length in range(1, 33):
        for odd in range(1, 128, 2):
            start = (1 << (length+1))*odd-1
            current = start
            for _ in range(length):
                require(v2(3*current+1) == 1, "exact initial ones run")
                current = (3*current+1)//2
            e = v2(3*current+1)
            end = (3*current+1) >> e
            require(e >= 2 and v2(start+1) == length+1, "maximal ones run")
            if start < 129 or end < start:
                continue
            require((1 << (length+e))*start**(length+1) <=
                    (3*start+1)**(length+1), "minimum-return segment product")
            require((1 << (5*(e-1))) < (start+1)**3,
                    "e-1 below(3/5)log2(start+1)")
            cases += 1
            arrows += length+1
            checksum.update(f"{start}:{length}:{e}:{end}\n".encode())
    require(cases > 0, "nonempty genuine minimum-return segments")
    return dict(ones_lengths=[1, 32], odd_quotients=[1, 127],
                minimum_return_segments=cases, exact_arrows=arrows,
                parameter_sha256=checksum.hexdigest(),
                scope="Exact integer orbit segments returning above their start; no cycle asserted.")


def cf_sum(k, m):
    total = 0
    while k:
        digit, remainder = divmod(m, k)
        total += digit
        m, k = k, remainder
    return total


def discrepancy():
    templates = factors = 0
    for m in range(3, 19):
        for k in range(1, m):
            if gcd(k, m) != 1:
                continue
            K = cf_sum(k, m)
            for high_count in range(1, m):
                base = [int((k*i) % m < high_count) for i in range(m)]
                prefix = [0]
                for bit in base+base:
                    prefix.append(prefix[-1]+bit)
                for t in (2, 3, 9, 100):
                    u = t-1
                    for start in range(m):
                        for length in range(1, m):
                            count = prefix[start+length]-prefix[start]
                            total = length+u*count
                            require(abs(m*total-(m+u*high_count)*length) <=
                                    2*m*u*(K-1), "weighted all-factor discrepancy")
                            factors += 1
                    templates += 1
    return dict(periods=[3, 18], high_labels=[2, 3, 9, 100], templates=templates,
                proper_factors=factors,
                scope="Finite transfer checks; the general discrepancy theorem is a declared dependency.")


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
        require(v2(raw) == letter, "exact reduced cycle valuation")
        current = raw >> letter
    require(current == states[0] and len(set(states)) == len(word),
            "primitive reduced cycle closes")
    return q, states


def check_cycle_runs(word, states, q):
    checks = 0
    for i, letter in enumerate(word):
        if letter != 1 or word[i-1] == 1:
            continue
        length = 0
        while word[(i+length) % len(word)] == 1:
            length += 1
            require(length < len(word), "positive run terminates")
        e = word[(i+length) % len(word)]
        x = states[i]
        following = states[(i+length+1) % len(word)]
        require(v2(x+q) == length+1, "addend-aware exact run valuation")
        odd = (x+q) >> (length+1)
        require((1 << (e-1))*following == 3**(length+1)*odd-q,
                "addend-aware run endpoint")
        checks += 1
    return checks


def family_controls():
    geometry = cycles = arrows = runs = 0
    classes = dict(background_maximum=0, singleton_maximum=0, both_backgrounds_above_one=0)
    minimum_q = None
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
                    for V, A, B in permutations(range(1, 7), 3):
                        track = [V]+[A]*a+[B]*b+[A]*c
                        word = [0]*m
                        for i, value in enumerate(track):
                            word[(i*h) % m] = value
                        mis1 = {i for i in range(m) if word[i] != word[(i+h) % m]}
                        mis2 = {i for i in range(m) if word[i] != word[(i+2*h) % m]}
                        E1 = {0, (-h) % m, (a*h) % m, ((a+b)*h) % m}
                        E2 = {0, (-2*h) % m, (a*h) % m, ((a-1)*h) % m,
                              ((a+b)*h) % m, ((a+b-1)*h) % m}
                        require(mis1 == E1 and len(E1) == 4 and mis2 <= E2,
                                "label-independent two-rotation geometry")
                        geometry += 1
                        if min(A, B) > 1:
                            require(sum(word) >= 2*m-1 > F(8*m, 5), "mean-label reduction")
                            kind = "both_backgrounds_above_one"
                        else:
                            t = max(A, B)
                            kind = "background_maximum" if t > V else "singleton_maximum"
                            if V > t:
                                template = word.copy()
                                template[0] = A
                                high = template.count(t)
                                require(sum(template) == m+(t-1)*high,
                                        "weighted binary-template total")
                                require(all(x <= y for x, y in zip(template, word)),
                                        "template lies below actual word")
                        result = reduced_cycle(word)
                        if result is None:
                            continue
                        q, states = result
                        require(q > 1, "finite family census denominator exceeds one")
                        classes[kind] += 1
                        cycles += 1
                        arrows += m
                        runs += check_cycle_runs(word, states, q)
                        minimum_q = q if minimum_q is None else min(minimum_q, q)
                        checksum.update(f"{m}:{a}:{b}:{c}:{h}:{V}:{A}:{B}:{q}\n".encode())
    require(all(classes.values()), "all three proof branches represented")
    return dict(periods=[4, 12], labels=[1, 6], geometry_words=geometry,
                reduced_cycles=cycles, exact_arrows=arrows, addend_run_checks=runs,
                branches=classes, minimum_reduced_addend=minimum_q,
                parameter_sha256=checksum.hexdigest(),
                scope="All ordered distinct labels in1..6, positive arc lengths and coprime steps in the stated finite period range; actual3x+q cycles keepq.")


def standard_controls():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    rows = json.loads(path.read_text())["cycles"]
    arrows = runs = 0
    for row in rows:
        word, states, q = row["valuations"], row["states"], row["d"]
        require(q in (5, 7, 13, 61), "standard addend")
        for i, letter in enumerate(word):
            raw = 3*states[i]+q
            require(v2(raw) == letter and raw >> letter == states[(i+1) % len(word)],
                    "standard exact arrow")
            arrows += 1
        runs += check_cycle_runs(word, states, q)
    require(len(rows) == 11 and arrows == 106, "complete standard fixture set")
    return dict(cycles=len(rows), exact_arrows=arrows, addend_run_checks=runs,
                fixture_sha256=sha256(path.read_bytes()).hexdigest(),
                scope="q retained; q1 minimum and drift ceilings are not applied to these controls.")


def local_descent():
    steps = maximum = 0
    for seed in range(3, 129, 2):
        value, length = seed, 0
        while value != 1:
            raw = 3*value+1
            value = raw >> v2(raw)
            length += 1
            require(length < 10000, "finite descent guard")
        steps += length
        maximum = max(maximum, length)
    require(maximum == 43, "descent fixture")
    return dict(seeds=63, odd_seed_range=[3, 127], odd_steps=steps, maximum_steps=maximum)


def replays():
    paths = [
        ("sparse-two-level-four-arc-exclusion", "check_four_arcs.py", "check_four_arcs.json"),
        ("cycle-length-lower-bound-from-convergents", "check_cycle_length_convergents.py",
         "cycle_length_convergents.json"),
    ]
    records = []
    for node, script_name, receipt_name in paths:
        relative = Path("areas/cycles/results")/node
        script, receipt = ROOT/relative/script_name, ROOT/relative/receipt_name
        before = receipt.read_bytes()
        command = [sys.executable]+(["-O"] if sys.flags.optimize else [])+[str(script)]
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
        require(result.returncode == 0, f"dependency replay failed: {node}\n{result.stdout}\n{result.stderr}")
        require(receipt.read_bytes() == before, "dependency receipt unchanged")
        records.append(dict(node=node, script_sha256=sha256(script.read_bytes()).hexdigest(),
                            receipt_sha256=sha256(before).hexdigest(), result="passed"))
    return records


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script[--write-receipt]")
    receipt = dict(schema="general-three-label-controls-v1", constants=constants(),
                   minimum_runs=minimum_runs(), discrepancy=discrepancy(),
                   family_controls=family_controls(), standard_controls=standard_controls(),
                   local_descent=local_descent(), dependency_replays=replays())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    path = HERE/"check_family_controls.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps(dict(result="passed", geometry_words=receipt["family_controls"]["geometry_words"],
                          family_cycles=receipt["family_controls"]["reduced_cycles"],
                          minimum_return_segments=receipt["minimum_runs"]["minimum_return_segments"],
                          discrepancy_factors=receipt["discrepancy"]["proper_factors"]), sort_keys=True))


if __name__ == "__main__":
    main()
