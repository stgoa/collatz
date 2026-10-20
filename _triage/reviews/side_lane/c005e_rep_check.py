"""Independent check of Lean C005-e (claude/lean-lane a7dcac0): repetition bookkeeping.

For random words z (letters 0..5, so D_z may be negative or zero-sum cases appear) and k = 1..6:
  D(z^k) = D(z) * G(2^sum z, 3^|z|, k) with G(Q, P, k) = sum_j Q^(k-1-j) P^j;
  C(z^k) * D(z) = C(z) * D(z^k)  (same fixed point, cleared form, no slope hypothesis);
  D(z^k) != 0 and D(z^k) | C(z^k)  =>  D(z) | C(z).
Also, on actual odd cycles of T_q listed k times over (q = 1, 5, 7, 13, 61): the least return time of
the minimum divides the listed period and the listed word is the k-fold power of one least period.
"""
import json
import random
import sys


def C(z):
    c = 0
    for k, a in enumerate(reversed(z)):
        c = 3**k + 2**a * c
    return c


def D(z):
    return 2**sum(z) - 3**len(z)


def G(Q, P, k):
    return sum(Q**(k - 1 - j) * P**j for j in range(k))


def step(n, q):
    x = 3 * n + q
    a = (x & -x).bit_length() - 1
    return x >> a, a


def main():
    rng = random.Random(55)
    n_id = n_desc = 0
    for _ in range(30000):
        z = [rng.randint(0, 5) for _ in range(rng.randint(1, 8))]
        for k in range(1, 7):
            zk = z * k
            assert D(zk) == D(z) * G(2**sum(z), 3**len(z), k)
            assert C(zk) * D(z) == C(z) * D(zk)
            n_id += 1
            if D(zk) != 0 and C(zk) % D(zk) == 0:
                assert D(z) != 0 and C(z) % D(z) == 0
                n_desc += 1
    # least period of listed-over cycles
    n_cyc = 0
    for q, starts in [(1, [1]), (5, [1, 5, 19, 23, 187, 347]), (7, [5, 7]), (13, [1, 13, 131, 211]), (61, [1, 61, 235])]:
        for x0 in starts:
            cyc, x = [], x0
            while True:
                cyc.append(x)
                x, _ = step(x, q)
                if x == x0:
                    break
            i0 = cyc.index(min(cyc))
            cyc = cyc[i0:] + cyc[:i0]
            p = len(cyc)
            word = [step(x, q)[1] for x in cyc]
            for k in range(1, 5):
                listed = cyc * k
                least = next(t for t in range(1, len(listed) + 1) if listed[t % len(listed)] == listed[0])
                assert least == p and len(listed) % least == 0
                assert [step(x, q)[1] for x in listed] == word * k
                n_cyc += 1
    out = {"probe": "c005e_rep_check", "lean": "claude/lean-lane a7dcac0",
           "identity_cases": n_id, "integral_power_cases_descending": n_desc,
           "listed_cycle_cases": n_cyc, "result": "PASS"}
    js = json.dumps(out, indent=1)
    print(js)
    if len(sys.argv) > 1:
        with open(sys.argv[1], "w") as f:
            f.write(js + "\n")


if __name__ == "__main__":
    main()
