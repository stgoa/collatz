"""Arbitrary-gcd phase checks with actual gQ-letter integer repetitions.

Finite controls test the written general proof, not absence of q=1 cycles.
The established exact phase/repetition helpers are shared within this node.
"""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path
import sys

from check_phase_blocks import (
    continued_fraction, crossed_events, family_spacing, intercept,
    repetition_identity, require, trace,
)


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def primitive(word):
    return all(word != word[d:]+word[:d] for d in range(1, len(word)))


def fold(word, h):
    m = len(word)
    g = gcd(h, m)
    M, d = m//g, h//g
    k = pow(d, -1, M)
    blocks = [tuple(word[g*i:g*(i+1)]) for i in range(M)]
    track = [blocks[(i*d) % M] for i in range(M)]
    s = sum(word[i] != word[(i+h) % m] for i in range(m))
    boundaries = [i for i in range(M) if track[i] != track[i-1]]
    require(2 <= len(boundaries) <= s, "block boundary count")
    require(all(track[(k*i) % M] == blocks[i] for i in range(M)),
            "inverse block clock")
    require(all(blocks != blocks[j:]+blocks[:j] for j in range(1, M)),
            "block primitivity follows from original word")
    changes_per_track = [sum(word[r+g*i] != word[r+g*((i+d) % M)]
                             for i in range(M)) for r in range(g)]
    require(sum(changes_per_track) == s and 1 not in changes_per_track,
            "residue-track mismatch accounting")
    if s == 4:
        require(sorted(x for x in changes_per_track if x) in ([4], [2, 2]),
                "complete four-mismatch track partition")
    return g, M, k, s, blocks, track, boundaries, changes_per_track


def phase_prefix(track, boundaries, k, p, Q, s, g):
    M = len(track)
    signed_j = Q*k-p*M
    j = abs(signed_j)
    require(j > 0 and j*Q < M and gcd(p, Q) == 1, "nonzero reduced phase with positive spacing")
    families = [{(boundary-i*k) % M for i in range(Q)} for boundary in boundaries]
    for family in families:
        family_spacing(family, M, Q, j)
    count = M//Q
    patterns = [tuple(track[(r*signed_j+i*k) % M] for i in range(Q))
                for r in range(count)]
    changes = [r for r in range(1, count) if patterns[r] != patterns[r-1]]
    used = changes[s] if len(changes) >= s+1 else count
    require(j*Q*(used+1) >= M, "prefix block-length lower bound")
    require(j*(g*Q*used+g*Q) >= g*M, "prefix actual odd-clock lower bound")
    if len(changes) >= s+1:
        selected = []
        for r in changes[:s+1]:
            events = crossed_events(families, (r-1)*signed_j, r*signed_j, M)
            require(events, "every change crosses a boundary")
            selected.append(min(events))
        require(len({x for _, x in selected}) == s+1, "disjoint event intervals")
        repeated = [(x, y) for i, x in enumerate(selected) for y in selected[i+1:]
                    if x[0] == y[0]]
        require(repeated, "s+1 changes repeat a boundary family")
        for (_, x), (_, y) in repeated:
            require(abs(x-y)*Q >= M-j*Q, "same-family spacing")
    regimes = []
    for pattern in patterns[:used]:
        raw = tuple(letter for block in pattern for letter in block)
        require(len(raw) == g*Q, "actual repeated word has length gQ")
        if regimes and regimes[-1][0] == raw:
            regimes[-1][1] += 1
        else:
            regimes.append([raw, 1])
    require(len(regimes) <= s+1, "at most s+1 repeated regimes")
    return signed_j, used, regimes, len(changes) >= s+1


def reduced_cycle(word):
    D = 2**sum(word)-3**len(word)
    if D <= 0:
        return None
    C = intercept(word)
    common = gcd(C, D)
    q, start = D//common, C//common
    states = trace(start, q, word)
    require(states[-1] == start and min(states) > 0
            and len(set(states[:-1])) == len(word), "primitive actual reduced cycle")
    cut = states[:-1].index(min(states))
    return word[cut:]+word[:cut], q, states[cut:-1]+states[:cut]


def update_case(word, h, summary, checksum, actual=None):
    g, M, k, s, blocks, track, boundaries, distribution = fold(word, h)
    coefficients, rows, reciprocal = continued_fraction(k, M)
    K = sum(coefficients)
    require(K <= M and reciprocal < 4, "continued-fraction sum controls")
    summary["rotations"] += 1
    summary["noncoprime_rotations"] += int(g > 1)
    summary["boundary_collisions"] += int(len(boundaries) < s)
    summary["larger_mismatch_counts"] += int(s > 4)
    summary["half_turns"] += int(M == 2)
    if s == 4:
        name = "one_four_track" if max(distribution) == 4 else "two_two_tracks"
        summary[name] += 1
    if M <= 27:
        require(K <= 27*len(coefficients), "short-track four-mismatch bound is vacuous")
        summary["short_track_vacuity"] += 1
    phases = [(p, Q) for p, Q, _ in rows]
    convergent_phases = set(phases)
    if M <= 12:
        for Q in range(1, M):
            for p in (Q*k//M, Q*k//M+1):
                if gcd(p, Q) == 1 and 0 < abs(Q*k-p*M)*Q < M and (p, Q) not in phases:
                    phases.append((p, Q))
    for p, Q in phases:
        signed_j, used, regimes, early = phase_prefix(track, boundaries, k, p, Q, s, g)
        summary["phases"] += 1
        summary["negative_phases"] += int(signed_j < 0)
        summary["initial_zero_over_one"] += int(p == 0 and Q == 1)
        summary["nonconvergent_phases"] += int((p, Q) not in convergent_phases)
        summary["early_stops"] += int(early)
        summary["maximum_regimes"] = max(summary["maximum_regimes"], len(regimes))
        unfolded = tuple(letter for block, count in regimes for _ in range(count)
                         for letter in block)
        require(unfolded == word[:g*Q*used], "grouped phase prefix equals raw chronology")
        if actual is not None:
            q, states = actual
            require(states[0] == min(states), "prefix starts at actual global minimum")
            extended = states+[states[0]]
            offset = 0
            for block, count in regimes:
                length = len(block)*count
                require(len(block) == g*Q < len(word), "proper actual repeated block")
                require(repetition_identity(block, count, extended[offset:offset+length+1], q),
                        "nonzero block difference from primitive cycle")
                summary["integer_repeated_regimes"] += 1
                summary["contracting_regimes"] += int(2**sum(block) > 3**len(block))
                summary["expanding_regimes"] += int(2**sum(block) < 3**len(block))
                offset += length
            # Exact powers verify B3, with the actual addend retained.
            if s <= 4:
                exponent = len(word)-27*abs(signed_j)*g*Q
                if exponent >= 0:
                    require(2**exponent < (states[0]+q)**(16*abs(signed_j)),
                            "exact four-mismatch phase bound")
                exponent = (K-27*len(coefficients))*g
                if exponent >= 0:
                    require(2**exponent < (states[0]+q)**64,
                            "exact four-mismatch complexity bound")
                summary["four_mismatch_cycle_bounds"] += 1
            # A finite rational relaxation also exercises arbitrary s.
            beta = F(8, 5)
            H = sum((beta**i for i in range(s+1)), F(0))
            Y_upper = (states[0]+q).bit_length()
            require(K < (beta*H+1)*len(coefficients)+4*H*Y_upper/g,
                    "general-s rational complexity relaxation")
        checksum.update(f"{word}:{h}:{g}:{s}:{p}:{Q}:{signed_j}:{used}\n".encode())


def blank_summary():
    return {name: 0 for name in (
        "words", "positive_reduced_cycles", "rotations", "noncoprime_rotations",
        "boundary_collisions", "larger_mismatch_counts", "half_turns",
        "one_four_track", "two_two_tracks", "short_track_vacuity", "phases",
        "negative_phases", "initial_zero_over_one", "nonconvergent_phases", "early_stops", "maximum_regimes",
        "integer_repeated_regimes", "contracting_regimes", "expanding_regimes",
        "four_mismatch_cycle_bounds",
    )}


def word_grids():
    summary = blank_summary()
    checksum = sha256()
    for alphabet, maximum in (((1, 2), 12), ((1, 3), 9)):
        for m in range(2, maximum+1):
            for word in product(alphabet, repeat=m):
                if not primitive(word):
                    continue
                summary["words"] += 1
                result = reduced_cycle(word)
                if result is not None:
                    rotated, q, states = result
                    summary["positive_reduced_cycles"] += 1
                    actual = (q, states)
                else:
                    rotated, actual = word, None
                for h in range(1, m):
                    if gcd(h, m) == 1 and m > 7:
                        continue
                    update_case(rotated, h, summary, checksum, actual)
    for key in ("noncoprime_rotations", "boundary_collisions", "larger_mismatch_counts",
                "one_four_track", "two_two_tracks", "negative_phases",
                "integer_repeated_regimes", "contracting_regimes", "expanding_regimes"):
        require(summary[key] > 0, f"coverage: {key}")
    return {"counts": summary, "parameter_sha256": checksum.hexdigest(),
            "grids": [{"alphabet": [1, 2], "periods": [2, 12]},
                      {"alphabet": [1, 3], "periods": [2, 9]}],
            "rotations": "Every noncoprime rotation; also every coprime rotation through period7.",
            "scope": "Primitive words only; D>0 words yield actual3x+q controls, with their true addend. No absence inference."}


def long_track_controls():
    summary = blank_summary()
    checksum = sha256()
    records = []
    for M in (37, 73, 131):
        for g in (2, 3, 5):
            active = [1]*(M//4)+[3]*(M//4)+[1]*(M//4)+[3]*(M-3*(M//4))
            for d in (1, 2, M-1):
                k = pow(d, -1, M)
                word = tuple(value for i in range(M)
                             for value in (active[(k*i) % M],)+(2,)*(g-1))
                require(primitive(word), "long control primitive")
                result = reduced_cycle(word)
                require(result is not None, "long control positive denominator")
                rotated, q, states = result
                require(q > 1, "long other-addend control")
                update_case(rotated, g*d, summary, checksum, (q, states))
                summary["words"] += 1
                summary["positive_reduced_cycles"] += 1
                records.append({"g": g, "M": M, "h_over_g": d,
                                "minimum_plus_q_bits": (min(states)+q).bit_length()})
    return {"counts": summary, "records": records,
            "parameter_sha256": checksum.hexdigest()}


def standard_cycles():
    path = ROOT/"areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    fixtures = json.loads(path.read_text())["cycles"]
    summary = blank_summary()
    checksum = sha256()
    arrows = 0
    for row in fixtures:
        word, q, states = tuple(row["valuations"]), row["d"], row["states"]
        require(trace(states[0], q, word) == states+[states[0]], "exact standard cycle")
        require(primitive(word), "standard cycle primitive")
        cut = states.index(min(states))
        word, states = word[cut:]+word[:cut], states[cut:]+states[:cut]
        for h in range(1, len(word)):
            update_case(word, h, summary, checksum, (q, states))
        summary["words"] += 1
        arrows += len(word)
    require(len(fixtures) == 11 and arrows == 106, "all standard fixtures")
    return {"cycles": len(fixtures), "exact_arrows": arrows, "counts": summary,
            "fixture_sha256": sha256(path.read_bytes()).hexdigest(),
            "parameter_sha256": checksum.hexdigest(),
            "scope": "Actual3x+5,7,13,61 states retain q in every shifted growth bound."}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    alpha_upper = F(8, 5)
    H4 = sum((alpha_upper**i for i in range(5)), F(0))
    require(H4 < 16 and alpha_upper*H4+1 < 27, "four-mismatch constants")
    receipt = {"schema": "arbitrary-gcd-phase-v1", "word_grids": word_grids(),
               "long_track_controls": long_track_controls(), "standard_cycles": standard_cycles(),
               "constants": {"H4_upper": str(H4), "alpha_H4_plus_one_upper": str(alpha_upper*H4+1)},
               "shared_helper_sha256": sha256((HERE/"check_phase_blocks.py").read_bytes()).hexdigest()}
    encoded = json.dumps(receipt, indent=2, sort_keys=True)+"\n"
    destination = HERE/"check_block_clock.json"
    if sys.argv[1:]:
        destination.write_text(encoded)
    else:
        require(destination.read_text() == encoded, "receipt mismatch; regenerate explicitly")
    print(json.dumps({"status": "passed", "grid_rotations": receipt["word_grids"]["counts"]["rotations"],
                      "grid_phases": receipt["word_grids"]["counts"]["phases"],
                      "long_controls": receipt["long_track_controls"]["counts"]["words"],
                      "standard_cycles": receipt["standard_cycles"]["cycles"]},
                     sort_keys=True))


if __name__ == "__main__":
    main()
