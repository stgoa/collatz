"""Exact controls for a stalled reduction; no absence census or extrapolation."""

from fractions import Fraction
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RECEIPT = HERE / "check_small_gap.json"
SPECS = (
    {
        "name": "rational_sign_countercontrol",
        "J": 7, "r": 6, "h": 1,
        "A": [2], "B": [2, 8],
    },
    {
        "name": "large_positive_interface",
        "J": 9, "r": 8, "h": 1,
        "A": [2, 2, 2, 3, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1,
              2, 3, 3, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 2],
        "B": [2, 1, 3, 2, 4, 2, 1, 1, 1, 2, 1, 1, 3, 1,
              2, 1, 2, 1, 1, 1, 2, 1, 1, 4, 3, 2, 2, 12],
    },
)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def v2(value):
    require(value != 0, "zero numerator")
    value = abs(value)
    return (value & -value).bit_length() - 1


def trace(start, addend, word):
    require(start != 0 and start % 2 == 1, "nonzero odd initial state")
    states = [start]
    for exponent in word:
        require(exponent >= 1, "positive valuation")
        numerator = 3 * states[-1] + addend
        require(v2(numerator) == exponent, "exact odd-only valuation")
        state = numerator // (1 << exponent)
        require(state != 0 and state % 2 == 1, "nonzero odd output")
        states.append(state)
    return states


def intercept(word):
    total = constant = 0
    for exponent in word:
        require(exponent >= 1, "positive word")
        constant = 3 * constant + (1 << total)
        total += exponent
    return constant


def changed_last(word, change):
    require(bool(word), "nonempty segment")
    out = word[:-1] + [word[-1] + change]
    require(out[-1] >= 1, "positive altered boundary")
    return out


def reconstruct(spec, source_rows):
    J, r, h = spec["J"], spec["r"], spec["h"]
    A, B = spec["A"], spec["B"]
    require(J > r >= 1 and h > 0 and h % 2 == 1, "level and endpoint domain")
    require(A and B and B[-1] > J, "nonempty blocks and high terminal boundary")
    p, M, N = J - r, 1 << r, 1 << J
    a, b, P = len(A), len(B), sum(A)
    n = a + b
    states_A = trace(-h, M - 1, A)
    z = states_A[-1]
    require(z > 0, "positive interface")
    states_B = trace(z, N - 1, B)
    require(states_B[-1] == h, "signed return endpoint")
    u = changed_last(A, p) + changed_last(B, -J)
    v = A + changed_last(B, r)
    word = u + v
    C = intercept(word)
    D = (1 << sum(word)) - 3 ** len(word)
    require(D > 0, "positive reconstructed denominator")
    common = gcd(C, D)
    q, X = D // common, C // common
    require(q > 1 and q % 2 == 1, "control retains odd denominator greater than one")
    states = trace(X, q, word)
    require(states[-1] == X and min(states) > 0, "actual positive integer cycle")
    Xprime, Y, Z = states[n], states[a], states[n + a]
    require(Xprime == M * X + q * h, "opposite-half state")
    require(Z == N * Y - q * z, "interface state identity")
    CA = intercept(A)
    require(3 ** a * X + q * CA == (1 << (P + p)) * Y, "first A affine identity")
    require(3 ** a * Xprime + q * CA == (1 << P) * Z, "second A affine identity")
    numerator_t = (M - 1) * X + q * h
    require(v2(numerator_t) == P, "exact first binary divisibility")
    t = numerator_t >> P
    require(t > 0 and t % 2 == 1, "positive odd quotient")
    W0 = Z - (1 << p) * Y
    require(W0 == 3 ** a * t and W0 > 0, "initial power of three")
    difference_word = changed_last(B, -r)
    difference_states = trace(W0, -q * ((1 << p) - 1), difference_word)
    for i in range(b):
        require(difference_states[i] == states[n + a + i] - (1 << p) * states[a + i],
                "paired difference along common B prefix")
    final = M * (M - 1) * X - q * h
    require(difference_states[-1] == final, "coupled final difference")
    require(difference_word[-1] > p, "last difference valuation exceeds level gap")
    require(3 * difference_states[-2] - q * ((1 << p) - 1)
            == (1 << (B[-1] - r)) * final, "exact final numerator identity")
    matches = [row for row in source_rows
               if row["order"] == "LH" and row["J"] == J and row["r"] == r
               and row["h"] == h and row["A"] == A and row["B"] == B]
    require(len(matches) == 1, "unique existing control provenance")
    require(matches[0]["interface"] == z, "existing interface agrees")
    canonical = Fraction(X, q)
    require(Fraction(matches[0]["canonical_state"]) == canonical, "existing rational state agrees")
    return {
        **spec, "p": p, "interface": z, "u": u, "v": v,
        "signed_A_states": states_A, "signed_B_states": states_B,
        "canonical_state": str(canonical), "q": q, "X": X,
        "Xprime": Xprime, "Y": Y, "Z": Z, "t": t,
        "actual_cycle_states": states,
        "difference_addend": -q * ((1 << p) - 1),
        "difference_word": difference_word, "difference_states": difference_states,
        "coupled_final_difference": final,
        "source": "bounded-unequal-half-defect-exclusion/check_bounded_halves.json",
    }


def repeated_path_controls():
    prefix, loop = [1, 1, 3, 2], [1, 2]
    require(trace(9, -1, prefix) == [9, 13, 19, 7, 5], "positive transient")
    require(trace(5, -1, loop) == [5, 7, 5], "positive fixed cycle")
    C_loop = intercept(loop)
    require(C_loop == 5 and 3 ** len(loop) == 9 and (1 << sum(loop)) == 8,
            "loop map is (9w-5)/8")
    require(9 * 5 - C_loop == 8 * 5, "exact loop fixed point")
    samples = []
    for k in (0, 1, 2, 7, 25):
        word = prefix + loop * k
        states = trace(9, -1, word)
        require(states[-1] == 5 and min(states) > 0, "positive repeated path")
        require(len(word) == 4 + 2 * k and sum(word) == 7 + 3 * k, "family lengths and totals")
        require(word[-1] == 2 > 1 and states[0] == 3 ** 2, "isolated small-gap conditions")
        samples.append({"k": k, "word": word, "states": states,
                        "length": len(word), "valuation_total": sum(word)})
    return {
        "prefix": prefix, "loop": loop, "loop_affine_map": "(9w-5)/8",
        "loop_fixed_point": 5, "initial_power_of_three": 2,
        "representative_repeat_counts": [item["k"] for item in samples],
        "samples": samples,
        "scope": "All-k statement follows by the displayed fixed loop. Coupled Mersenne endpoints and D>0 are not asserted.",
    }


def actual_controls():
    fixture = ROOT / "areas/convergence/results/baseline-obligation-transfer-controls/cycle_fixtures.json"
    data = json.loads(fixture.read_text())
    out = []
    for row in data["cycles"]:
        states = trace(row["states"][0], row["d"], row["valuations"])
        require(states == row["states"] + [row["states"][0]], "shared actual cycle replay")
        require(min(states) == row["minimum"] > 0, "actual cycle minimum")
        C = intercept(row["valuations"])
        D = (1 << sum(row["valuations"])) - 3 ** len(row["valuations"])
        q = D // gcd(C, D)
        require(D > 0 and q > 1 and row["d"] * C == row["states"][0] * D,
                "normalized denominator and actual additive constant")
        out.append({"d": row["d"], "minimum": row["minimum"],
                    "period": len(row["valuations"]), "reduced_denominator": q})
    require(len(out) == 11, "eleven actual-cycle fixtures")
    return {"fixture_sha256": sha256(fixture.read_bytes()).hexdigest(), "cycles": out}


def certificate():
    source = ROOT / "areas/cycles/results/bounded-unequal-half-defect-exclusion/check_bounded_halves.json"
    rows = json.loads(source.read_text())["joins"]
    joins = [reconstruct(spec, rows) for spec in SPECS]
    small, large = joins
    require(small["q"] == 4069 and small["X"] == 1 and small["t"] == 1033,
            "small countercontrol constants")
    require(small["actual_cycle_states"] == [1, 509, 1399, 4133, 4117, 4105, 1],
            "displayed actual cycle")
    require(small["difference_states"] == [3099, 1307, -37], "displayed sign crossing")
    require(Fraction(small["canonical_state"]) < Fraction(1, 64 * 63),
            "rational sign shortcut fails")
    require(large["interface"] == 7527 > 512 and len(large["A"]) == 30
            and len(large["B"]) == 28 and large["B"][-1] == 12,
            "large interface constants")
    first_positive = next(i for i, state in enumerate(large["signed_A_states"]) if state > 0)
    require(first_positive < len(large["A"]), "first crossing is before the interface")
    require(large["canonical_state"] ==
            "1444813510101983474118931607/162254566700516117146743088684439",
            "displayed large-interface canonical state")
    return {
        "scope": "Exact controls for the small-level-gap signed-transient attempt; no finite absence claim.",
        "joins": joins,
        "existing_join_receipt_sha256": sha256(source.read_bytes()).hexdigest(),
        "large_interface_first_positive_step": first_positive,
        "repeatable_positive_paths": repeated_path_controls(),
        "actual_controls": actual_controls(),
    }


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: check_small_gap.py [--write-receipt]")
    result = certificate()
    serialized = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if sys.argv[1:] == ["--write-receipt"]:
        RECEIPT.write_text(serialized)
    else:
        require(RECEIPT.exists() and RECEIPT.read_text() == serialized, "receipt mismatch; regenerate explicitly")
    print("PASS: 2 exact joins; 5 fixed-loop representatives; 11 actual-cycle fixtures")


if __name__ == "__main__":
    main()
