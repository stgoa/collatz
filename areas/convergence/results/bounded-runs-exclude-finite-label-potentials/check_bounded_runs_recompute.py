"""Recompute the repeated bounded-run witnesses of bounded_runs_audit.json from first principles.

Written at the B10-residual-R25-R39 migration; the legacy scripts in this folder load
../bridge_normal_form/normal_form.py and ../complementary_bridge/run_bridge.py by
their pre-migration paths and no longer run.

Everything below uses this file's own odd-only Syracuse step, canonical-set test,
normal form nu (strip x -> (x-1)/4 on 5 mod 8, then x -> (x-1)/2 on a selected
climber) and normalized run return f_star(x) = nu(f(x)) of a complementary x
(f(x) = 3^((d-1)/2) w for odd d, 2 3^(d/2) w + 1 for even d). It checks:
  1. the affine prefix table of the word (1,2,1,1,1,1,2,2) (rows j, valuation,
     total, numerator, offset) against the receipt, 3^j > 2^A_j on every row,
     4513*27 + 9221 = 2^17, and the identity
     4513 Psi(x) + 9221 = (6561/2048)(4513 x + 9221) as an exact rational identity;
  2. the 57 cylinder samples (r = 1..16, 32, 64, 128; offsets 0, 1, 7): every
     ordinary valuation follows the word r times, every state is canonical and
     above its pair's start, the normalized returns have labels (a, d) = (2, 2),
     (5, 4) alternately and strictly increase, each pair ends at Psi(start); and the
     seed and endpoint bit lengths, row counts and the SHA-256 of the state and
     return sequences agree with the receipt;
  3. the 21 required-ray witnesses: N = 12 2^b, N < x < 3N/2, x = 3 mod 12, x
     complementary with f_star(x) > N, all 8r states canonical and above N, and the
     receipt's bit lengths and state hashes;
  4. the six finite-modulus label repetitions (moduli 8, 16, 27, 64, 81, 128).
It does not rerun the legacy constructor or its current bookkeeping (legacy checker,
evidence only). Standard library; no files are written.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
WORD = (1, 2, 1, 1, 1, 1, 2, 2)
FAILURES = []


def need(condition, message):
    if not condition:
        FAILURES.append(message)


def v2(n):
    return (n & -n).bit_length() - 1


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    t = (x + 1) >> a
    return t % 4 == pow(3, a, 4)


def canonical(x):
    return x % 8 == 1 or (x % 4 == 3 and not selected(x))


def nu(x):
    while x % 8 == 5:
        x = (x - 1) // 4
    return (x - 1) // 2 if selected(x) else x


def run_label_and_return(x):
    """R26 parameters (a, d) and the normalized return of a complementary x."""
    a = v2(x + 1)
    t = (x + 1) >> a
    v = 3**(a - 1) * t - 1
    d = v2(v)
    w = v >> d
    f = 3**(d // 2) * w if d % 2 else 2 * 3**(d // 2) * w + 1
    return (a, d), nu(f)


def fingerprint(values):
    return hashlib.sha256("\n".join(map(str, values)).encode()).hexdigest()


def cylinder(r):
    mod = 1 << (11 * r + 6)
    return (-9221 * pow(4513, -1, mod)) % mod, mod


def witness(x, r):
    states, returns = [x], [x]
    labels = []
    for _ in range(r):
        start = states[-1]
        need(start % (1 << 17) == 27, "pair start not 27 mod 2^17")
        for j, a in enumerate(WORD):
            q = states[-1]
            need(v2(3 * q + 1) == a, f"valuation at r={r}")
            y = (3 * q + 1) >> a
            need(canonical(y) and y > start, f"canonical/above start at r={r}")
            states.append(y)
            if j in (1, 7):
                origin = returns[-1]
                need(not selected(origin) and origin % 4 == 3, f"complementary origin at r={r}")
                label, target = run_label_and_return(origin)
                need(label == ((2, 2) if j == 1 else (5, 4)), f"label at r={r}")
                need(target == y and y > origin, f"normalized return at r={r}")
                labels.append(label)
                returns.append(y)
        need(2048 * states[-1] == 6561 * start + 9221, f"Psi at r={r}")
    need(states[-1] % 64 == 27, f"endpoint class at r={r}")
    return states, returns, labels


def main():
    receipt = json.loads((HERE / "bounded_runs_audit.json").read_text())

    # 1. Affine table and identities.
    table, A, C = [], 0, 0
    for j, a in enumerate(WORD, 1):
        C = 3 * C + 2**A
        A += a
        need(3**j > 2**A, f"3^j > 2^A at j={j}")
        table.append(dict(j=j, valuation=a, total=A, numerator=3**j, offset=C))
    need(table == receipt["affine_prefixes"], "affine prefix table")
    need((3**8, 2**A, C) == (6561, 2048, 9221), "final affine map")
    need(4513 * 27 + 9221 == 2**17 and 6561 - 2048 == 4513, "4513 identities")
    xs = Fraction(7, 3)
    psi = (6561 * xs + 9221) / 2048
    need(4513 * psi + 9221 == Fraction(6561, 2048) * (4513 * xs + 9221), "Psi identity")
    need(receipt["word"] == list(WORD) and receipt["fixed_point"] == "-9221/4513", "word and fixed point")

    # 2. Cylinder samples.
    samples = receipt["samples"]
    need(len(samples) == 57, "sample count")
    plan = [(r, o) for r in [*range(1, 17), 32, 64, 128] for o in (0, 1, 7)]
    need([(s["repeats"], s["offset"]) for s in samples] == plan, "sample list")
    for s in samples:
        r, o = s["repeats"], s["offset"]
        res, mod = cylinder(r)
        x = res + o * mod
        states, returns, _ = witness(x, r)
        rows = len(set(states[:-1]))
        need(s["bits"] == mod.bit_length() - 1 and s["seed_bits"] == x.bit_length(), f"bits r={r}")
        need(s["endpoint_bits"] == states[-1].bit_length() and s["rows"] == rows, f"endpoint/rows r={r}")
        need(s["states_sha256"] == fingerprint(states) and s["returns_sha256"] == fingerprint(returns), f"hash r={r}")

    # 3. Required-ray witnesses.
    rays = receipt["required_ray_samples"]
    plan = [(r, e) for r in (1, 2, 4, 8, 16, 32, 64) for e in (0, 1, 17)]
    need([(s["repeats"], s["extra_scale"]) for s in rays] == plan, "ray list")
    for s in rays:
        r, e = s["repeats"], s["extra_scale"]
        res, mod = cylinder(r)
        N = 12 * (1 << (mod.bit_length() - 1 + e))
        period = 3 * mod
        first = res + mod * ((-res * pow(mod, -1, 3)) % 3)
        x = first + period * ((N - first) // period + 1)
        need(N < x <= N + period < 3 * N // 2 and x % 12 == 3 and not selected(x), f"ray root r={r}")
        need(run_label_and_return(x)[1] > N, f"first return above N r={r}")
        states, _, _ = witness(x, r)
        need(all(y > N and nu(y) == y for y in states), f"ray states r={r}")
        need(s["N_bits"] == N.bit_length() and s["seed_bits"] == x.bit_length(), f"ray bits r={r}")
        need(s["states_sha256"] == fingerprint(states), f"ray hash r={r}")

    # 4. Finite-modulus label repetitions.
    found = []
    for modulus in (8, 16, 27, 64, 81, 128):
        r = modulus + 1
        res, _ = cylinder(r)
        _, returns, labels = witness(res, r)
        first, repeated = {}, None
        for i, (y, label) in enumerate(zip(returns, labels)):
            key = (*label, y % modulus)
            if key in first:
                need(y > first[key][1], f"repeat not higher, modulus {modulus}")
                repeated = dict(first=first[key][0], second=i, label=list(key))
                break
            first[key] = (i, y)
        found.append(dict(modulus=modulus, repeats=r, witness=repeated))
    need(found == receipt["finite_label_examples"], "finite-label examples")

    if FAILURES:
        print(f"FAIL: {len(FAILURES)} checks failed; first: {FAILURES[0]}")
        sys.exit(1)
    print("PASS: affine table, 57 cylinders, 21 required-ray witnesses and 6 finite-label "
          "repetitions recomputed against bounded_runs_audit.json")


if __name__ == "__main__":
    main()
