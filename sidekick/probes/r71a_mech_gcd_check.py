"""Independent check of R71 (BALANCED_DENOMINATORS.md section 2) as formalised in Lean R71-a.

Checks, exact integer arithmetic only:
  (a) mech_rotate: rotating the phase-l word by i letters gives phase (l + iA) mod m;
  (b) the jump index: exactly one j < m with m | jA + 1 when gcd(A, m) = 1, and j != 0 for m >= 2;
  (c) R71 (4): C(phase 1) - C(phase 0) = 3^(m-1-j) 2^floor(jA/m);
  (d) mech_gcd_one / mech_gcd_one_phase: gcd(C, D) = 1 for every phase when gcd(A, m) = 1;
  (e) gcd_rotate_eq on random words with positive total;
  (f) mech_D_ne_one: 2^A - 3^m != 1 for m >= 2 (any A);
  (g) controls outside the formal scope: the repeated case g = gcd(A, m) > 1 has
      gcd(C, D) = D / (2^(A/g) - 3^(m/g)) > 1 when D > 0 (so coprimality is necessary),
      which is R71 (3); and m = 1 has C = 1.
"""
import json
import math
import random
import sys


def C(z):
    # recursive form C(a::z) = 3^|z| + 2^a C(z), evaluated right to left
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def D(z):
    return 2**sum(z) - 3**len(z)


def mech(A, m, l):
    return [((j + 1) * A + l) // m - (j * A + l) // m for j in range(m)]


def rot(z, i):
    i %= len(z)
    return z[i:] + z[:i]


def main():
    out = {"probe": "r71a_mech_gcd_check", "source": "BALANCED_DENOMINATORS.md section 2",
           "lean": "claude/lean-lane 09d4319"}
    M = 40
    n_rot = n_jump = n_diff = n_gcd = n_rep = 0
    rep_examples = []
    for m in range(1, M + 1):
        for A in range(m, 2 * m + 8):
            g = math.gcd(A, m)
            words = [mech(A, m, l) for l in range(m)]
            Dv = 2**A - 3**m
            assert all(D(w) == Dv for w in words)
            # (a) rotations are phases
            for l in range(m):
                for i in range(m):
                    assert rot(words[l], i) == words[(l + i * A) % m]
                    n_rot += 1
            if g == 1:
                if m >= 2:
                    js = [j for j in range(m) if (j * A + 1) % m == 0]
                    assert len(js) == 1 and js[0] != 0, (A, m, js)
                    j = js[0]
                    n_jump += 1
                    assert C(words[1]) - C(words[0]) == 3**(m - 1 - j) * 2**(j * A // m)
                    n_diff += 1
                else:
                    assert C(words[0]) == 1
                for w in words:
                    assert math.gcd(C(w), Dv) == 1, (A, m, w)
                    n_gcd += 1
            elif Dv > 0:
                A0, m0 = A // g, m // g
                d = 2**A0 - 3**m0
                for w in words:
                    G = math.gcd(C(w), Dv)
                    assert Dv // G == d and G > 1, (A, m, w, G, d)
                    n_rep += 1
                if (m, A) == (6, 10):
                    rep_examples.append({"m": 6, "A": 10, "D": Dv, "reduced_den": d})
    out["mech_rotate_cases"] = n_rot
    out["jump_index_unique_nonzero_cases"] = n_jump
    out["R71_4_difference_cases"] = n_diff
    out["gcd_one_phase_words"] = n_gcd
    out["repeated_case_words_D_pos"] = n_rep
    out["repeated_example"] = rep_examples

    # (e) gcd_rotate_eq on random words with positive total
    rng = random.Random(71)
    n_e = 0
    for _ in range(20000):
        m = rng.randint(1, 12)
        w = [rng.randint(0, 4) for _ in range(m)]
        if sum(w) == 0:
            continue
        base = math.gcd(C(w), D(w))
        for i in range(m):
            assert math.gcd(C(rot(w, i)), D(w)) == base
        n_e += 1
    out["gcd_rotate_eq_random_words"] = n_e

    # (f) 2^A - 3^m != 1 for m >= 2, A <= 400 (the hypothesis A >= m is not needed)
    sols = [(A, m) for m in range(0, 200) for A in range(0, 400) if 2**A - 3**m == 1]
    assert sols == [(1, 0), (2, 1)], sols
    out["solutions_2A_minus_3m_eq_1"] = sols

    out["result"] = "PASS"
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
