"""Exact controls for a failed half-defect 3-adic cross-height argument.

The README proves the unbounded congruence and the redundancy of its
minimum-positive-multiple bound. This certificate reconstructs genuine
3x+d cycles, checks the exact corrected formulas and their scopes, and
exhibits a counterexample to the formula omitting both block intercepts.
No finite absence is used. Default invocation verifies the generated
receipt; --write-receipt regenerates it.
"""

from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
FIXTURE = (
    ROOT / "areas/convergence/results/baseline-obligation-transfer-controls"
    / "cycle_fixtures.json"
)
FIXTURE_SHA256 = "3aeddd6c3eb2f9b4be54aa239b1ebd197fcabd3a215880e4a853470921e01fe2"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def intercept(word):
    value = total = 0
    for letter in word:
        require(isinstance(letter, int) and letter >= 1, "positive valuation letter")
        value = 3 * value + 2**total
        total += letter
    return value


def order3(value):
    require(value != 0, "finite 3-adic order")
    value = abs(value)
    order = 0
    while value % 3 == 0:
        value //= 3
        order += 1
    return order


def exact_cycle(word, addend, start):
    require(addend > 0 and addend % 2 == 1, "positive odd actual addend")
    require(start > 0 and start % 2 == 1, "positive odd actual start")
    states = []
    state = start
    for letter in word:
        states.append(state)
        raw = 3 * state + addend
        require(raw % 2**letter == 0, "integral arrow")
        state = raw // 2**letter
        require(state > 0 and state % 2 == 1, "exact odd output")
    require(state == start, "cycle closes")
    require(len(set(states)) == len(states), "distinct states before closure")
    discriminant = 2**sum(word) - 3**len(word)
    require(discriminant > 0, "positive cycle discriminant")
    require(discriminant * start == addend * intercept(word), "full affine identity")
    return states


def analyze(A, B, p, q, scale):
    require(A and B and 1 <= p < q, "stated block and magnitude scope")
    require(scale > 0 and scale % 2 == 1, "odd scaling")
    a, b = len(A), len(B)
    n = a + b
    word = A + B + A[:-1] + (A[-1] + p,) + B[:-1] + (B[-1] + q,)
    discriminant = 2**sum(word) - 3**len(word)
    require(discriminant > 0, "positive discriminant for chosen control")
    common = gcd(discriminant, intercept(word))
    reduced_addend = discriminant // common
    addend = scale * reduced_addend
    start = scale * intercept(word) // common
    states = exact_cycle(word, addend, start)
    require(sum(word[i] != word[(i + n) % (2 * n)] for i in range(2 * n)) == 4,
            "four half-period mismatches")
    x, z, y, t = states[0], states[a], states[n], states[n + a]
    P, R = 3**a, 3**b
    Q, S = 2**sum(A), 2**sum(B)
    k, l = 2**p, 2**q
    CA, CB = intercept(A), intercept(B)
    require(Q * z == P * x + addend * CA, "first A boundary")
    require(S * y == R * z + addend * CB, "first B boundary")
    require(k * Q * t == P * y + addend * CA, "changed A boundary")
    require(l * S * x == R * t + addend * CB, "changed B boundary")
    require((y - x) % Q == 0 and (z - t) % S == 0, "paired quotients")
    H, J = (y - x) // Q, (z - t) // S
    require(H > 0 and H % 2 == 1 and J % 2 == 1, "nonzero odd quotients")
    require(k * Q * S * J == P * (k * x - y) + (k - 1) * addend * CA,
            "first exact block congruence")
    require(l * Q * S * H == R * (l * z - t) + (l - 1) * addend * CB,
            "second exact block congruence")
    r = min(a, b)
    modulus = 3**r
    bare = l * (k - 1) * H - k * (l - 1) * J
    corrected = l * (k - 1) * CA * H - k * (l - 1) * CB * J
    require(corrected % modulus == 0, "corrected cross congruence")
    require(CA % 3 and CB % 3, "ordinary intercepts are 3-adic units")
    clipped = None
    if addend % 3:
        require(min(order3(J), a) == min(order3(k - 1), a), "clipped J order")
        require(min(order3(H), b) == min(order3(l - 1), b), "clipped H order")
        clipped = {"J": min(order3(J), a), "H": min(order3(H), b)}

    normalized = None
    if J < 0 and (p + q) % 2:
        g0 = 2**gcd(p, q) - 1
        require(g0 == gcd(k - 1, l - 1), "common amplitude factor")
        require(g0 % 3 != 0, "common amplitude factor is a 3-adic unit")
        u = 2**(q - p) * ((k - 1) // g0)
        v = (l - 1) // g0
        require(u >= 2 and v >= 3, "amplitude-normalized coefficient floors")
        value = u * CA * H + v * CB * (-J)
        require(corrected == k * g0 * value and value % modulus == 0,
                "amplitude-normalized cross congruence")
        require(CA >= 3**(a - 1) and CB >= 3**(b - 1), "intercept floors")
        floor = 2 * 3**(a - 1) + 3 * 3**(b - 1)
        require(value >= floor >= 5 * 3**(r - 1) > modulus,
                "positive-multiple size floor is already automatic")
        normalized = {
            "g0": g0, "coefficients": [u, v], "value": value,
            "elementary_floor": floor, "common_length_floor": 5 * 3**(r - 1),
        }
    return {
        "A": list(A), "B": list(B), "p": p, "q": q,
        "word": list(word), "scale": scale, "reduced_addend": reduced_addend,
        "addend": addend, "states": states, "C_W": intercept(word),
        "D_W": discriminant, "H": H, "J": J, "C_A": CA, "C_B": CB,
        "modulus": modulus, "bare_cross": bare, "bare_residue": bare % modulus,
        "corrected_cross": corrected, "corrected_residue": corrected % modulus,
        "clipped_3adic_orders_if_addend_unit": clipped,
        "amplitude_normalized_cross_if_applicable": normalized,
    }


def standard_controls():
    raw = FIXTURE.read_bytes()
    require(sha256(raw).hexdigest() == FIXTURE_SHA256, "shared fixture hash")
    rows = json.loads(raw)["cycles"]
    require(len(rows) == 11 and {row["d"] for row in rows} == {5, 7, 13, 61},
            "all eleven standard actual cycles")
    summaries = []
    for row in rows:
        states = exact_cycle(tuple(row["valuations"]), row["d"], row["states"][0])
        require(states == row["states"], "exact shared states")
        require(min(states) == row["minimum"], "shared cycle minimum")
        summaries.append({"addend": row["d"], "minimum": min(states),
                          "odd_period": len(states), "exact_arrows": len(states)})
    return {"fixture_sha256": FIXTURE_SHA256, "cycles": summaries,
            "exact_arrows": sum(len(row["states"]) for row in rows),
            "scope": "actual-map controls, not asserted to lie in the half-defect branch"}


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "supported arguments")
    specifications = [
        ((1,), (1,), 1, 2),
        ((1, 1), (2, 1), 1, 2),
        ((1,), (1, 1, 1), 3, 6),
        ((2, 1), (1, 2), 2, 3),
        ((1, 2), (2, 1), 2, 4),
    ]
    controls = [analyze(*spec, scale) for spec in specifications for scale in (1, 3)]
    require(controls[0]["addend"] == 47 and controls[0]["bare_residue"] == 0,
            "single-arrow control hides the missing intercepts")
    witness = controls[2]
    require(witness["addend"] == 1631 and witness["bare_residue"] == 6,
            "genuine omitted-intercept counterexample")
    require(witness["states"] == [9145, 14533, 22615, 17369, 26869, 41119, 31247, 23843],
            "displayed exact actual cycle")
    require(witness["bare_cross"] == 24198 and witness["corrected_cross"] == 133938,
            "displayed exact cross expressions")
    require(controls[4]["amplitude_normalized_cross_if_applicable"]["g0"] == 7,
            "nontrivial amplitude-gcd cancellation exercised")
    require({row["J"] > 0 for row in controls} == {False, True}, "both paired orders")
    require(any(row["addend"] % 3 == 0 for row in controls), "nonunit addend controls")
    fixtures = standard_controls()
    data = {
        "result": "PASS", "scope": "failed height route; no denominator-one counterexample",
        "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "actual_half_defect_controls": len(controls),
        "actual_half_defect_arrows": sum(len(row["states"]) for row in controls),
        "controls": controls, "standard_controls": fixtures,
    }
    path = HERE / "check_cross_congruence.json"
    encoded = json.dumps(data, sort_keys=True, indent=2) + "\n"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded, "certificate receipt mismatch")
    print(json.dumps({"result": "PASS", "actual_half_defect_controls": len(controls),
                      "actual_half_defect_arrows": data["actual_half_defect_arrows"],
                      "standard_cycles": len(fixtures["cycles"]),
                      "bare_congruence_counterexample_addend": 1631}, sort_keys=True))


if __name__ == "__main__":
    main()
