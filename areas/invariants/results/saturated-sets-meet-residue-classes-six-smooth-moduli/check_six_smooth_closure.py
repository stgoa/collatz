#!/usr/bin/env python3
"""Certificate for saturated-sets-meet-residue-classes-six-smooth-moduli.

Setting. T is the map n -> n/2 (n even), n -> 3n + d (n odd) on the positive integers, d odd and prime to 3
(d = 1 is the Collatz map). A set B is saturated if x in B iff T(x) in B. Then B is closed under the moves
    D  x -> 2x,     H  (x even) x -> x/2,     F  (x odd) x -> 3x + d,     I  (x even, x = d mod 3) x -> (x - d)/3,
and a nonempty B contains an odd element. The node proves by induction that for every k, b and every target
class (r mod 2^k, e mod 3^b) a saturated nonempty B has an element in that class. The proof is constructive: from an
odd start x0 it produces an element of the saturation of {x0} in the target class together with the moves reaching
it. This certificate instantiates that construction and REPLAYS every move, checking its legality and the final
residues.

V1  d = 1: for every odd x0 <= X0MAX, every k <= KMAX, b <= BMAX and every target class modulo 2^k 3^b, the
    construction returns a path of legal moves from x0 ending at a positive integer in the target class;
V2  the primitive-root lemma used by the base case: for every b <= BMAX + KMAX, every y mod 3^(b+1) with 3 not
    dividing y and every class eta = d mod 3 modulo 3^(b+1), some j with 1 <= j <= 2 * 3^b has 2^j y = eta;
V3  controls: the same construction for d in {5, 7, 13, 61} (odd x0 <= X0MAX_D, k <= KMAX_D, b <= BMAX_D), showing the
    argument is uniform in d prime to 6 (the obstruction for 3x+d lives at the primes dividing d, which the
    6-smooth moduli never see);
V4  bookkeeping: the number of inverse steps the construction uses for the targets modulo 2^k (b = 0) is at most k,
    and for the targets modulo 3^b (k = 0) it is exactly 1; the maxima per (k, b) are stored in the receipt;
V5  the receipt comparison. Exit 1 on any failure; --write-receipt regenerates six_smooth_closure.json.
Standard library only; deterministic."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "six_smooth_closure.json"
X0MAX, KMAX, BMAX = 99, 6, 3
X0MAX_D, KMAX_D, BMAX_D = 41, 4, 2
CONTROLS = (5, 7, 13, 61)
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def v2(n):
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v


def inv_mod(a, m):
    return 0 if m == 1 else pow(a, -1, m)


class Construction:
    """The proof's recursion for the map 3x+d. Elements are tracked exactly; moves are recorded as letters."""

    def __init__(self, d):
        self.d = d

    def base(self, x0, b, eps, size):
        """An odd element = eps (mod 3^b), with the moves from x0; the element is >= size."""
        d = self.d
        moves, x = [], x0
        if x % 3 == 0:          # forward step: 3x + d is prime to 3 since gcd(d, 3) = 1
            x = 3 * x + d
            moves.append("F")
        mod, period = 3 ** (b + 1), 2 * 3 ** b
        target = (d + 3 * eps) % mod
        j = None
        for t in range(1, period + 1):          # 2 is a primitive root modulo 3^(b+1): some t works (V2)
            if (pow(2, t, mod) * x) % mod == target:
                j = t
                break
        if j is None:
            raise RuntimeError("primitive root lemma failed")
        while 2 ** j * x < size:                 # extra full periods keep the class and make the element large
            j += period
        x = 2 ** j * x
        moves.extend("D" * j)
        if not (x % 2 == 0 and x % 3 == d % 3):
            raise RuntimeError("inverse step illegal in base case")
        x = (x - d) // 3
        moves.append("I")
        return x, moves

    def odd_target(self, x0, k, b, u, eps, size):
        """An element = u (mod 2^k), u odd, and = eps (mod 3^b), by induction on k."""
        d = self.d
        if k <= 1:
            return self.base(x0, b, eps, size)
        j = v2(3 * u + d)                        # >= 1 since u odd and d odd
        mod3 = 3 ** (b + 1)
        c = (inv_mod(2 ** j, mod3) * (d + 3 * eps)) % mod3      # y = c (mod 3^(b+1)) makes 2^j y = d + 3 eps
        if j >= k:
            y, moves = self.base(x0, b + 1, c, 3 * size + d)
        else:
            up = ((3 * u + d) >> j) % 2 ** (k - j)                # odd class modulo 2^(k-j)
            y, moves = self.odd_target(x0, k - j, b + 1, up, c, 3 * size + d)
        x = 2 ** j * y
        moves.extend("D" * j)
        if not (x % 2 == 0 and x % 3 == d % 3):
            raise RuntimeError("inverse step illegal in lift")
        x = (x - d) // 3
        moves.append("I")
        return x, moves

    def target(self, x0, k, b, r, eps):
        """An element = r (mod 2^k) and = eps (mod 3^b)."""
        M2 = 2 ** k
        r %= M2
        size = 3 ** (k + 2) * self.d
        if r == 0:
            c = (inv_mod(2 ** k, 3 ** b) * eps) % 3 ** b if b > 0 else 0
            y, moves = self.base(x0, b, c, size)
            return 2 ** k * y, moves + ["D"] * k
        v = v2(r)
        u = r >> v
        c = (inv_mod(2 ** v, 3 ** b) * eps) % 3 ** b if b > 0 else 0
        y, moves = self.odd_target(x0, k - v, b, u, c, size)
        return 2 ** v * y, moves + ["D"] * v


def replay(d, x0, moves):
    """Apply the moves from x0, checking legality; returns the final element or None."""
    x = x0
    for mv in moves:
        if mv == "D":
            x = 2 * x
        elif mv == "H":
            if x % 2:
                return None
            x //= 2
        elif mv == "F":
            if x % 2 == 0:
                return None
            x = 3 * x + d
        elif mv == "I":
            if not (x % 2 == 0 and x % 3 == d % 3 and x > d):
                return None
            x = (x - d) // 3
        else:
            return None
        if x <= 0:
            return None
    return x


def run(d, x0max, kmax, bmax):
    """Returns per-(k, b) maxima of inverse steps and of path length, or records failures."""
    con = Construction(d)
    stats = {}
    for k in range(kmax + 1):
        for b in range(bmax + 1):
            max_inv, max_len, count = 0, 0, 0
            for x0 in range(1, x0max + 1, 2):
                for r in range(2 ** k):
                    for eps in range(3 ** b):
                        x, moves = con.target(x0, k, b, r, eps)
                        y = replay(d, x0, moves)
                        if y is None or y != x or x % 2 ** k != r or x % 3 ** b != eps:
                            fail(f"d={d} x0={x0} k={k} b={b} target ({r}, {eps}): construction or replay wrong")
                            return stats
                        max_inv = max(max_inv, moves.count("I"))
                        max_len = max(max_len, len(moves))
                        count += 1
            stats[f"{k},{b}"] = {"targets": count, "max_inverse_steps": max_inv, "max_moves": max_len}
    return stats


def main():
    write = "--write-receipt" in sys.argv
    summary = {}
    # V1
    s1 = run(1, X0MAX, KMAX, BMAX)
    summary["V1"] = {"d": 1, "x0_max": X0MAX, "k_max": KMAX, "b_max": BMAX, "stats": s1}
    print(f"V1: d = 1, odd x0 <= {X0MAX}, k <= {KMAX}, b <= {BMAX}: {sum(v['targets'] for v in s1.values())} targets, "
          f"{len(failures)} failures")
    # V2
    bad = 0
    for b in range(BMAX + KMAX + 1):
        mod, period = 3 ** (b + 1), 2 * 3 ** b
        pows = [pow(2, t, mod) for t in range(1, period + 1)]
        for y in range(mod):
            if y % 3 == 0:
                continue
            hit = {(p * y) % mod for p in pows}
            for eta in range(1, mod, 3):      # classes = 1 mod 3; for d = 1 these are the inverse-step inputs
                if eta not in hit:
                    bad += 1
    if bad:
        fail(f"V2 primitive root lemma fails {bad} times")
    summary["V2"] = {"b_max": BMAX + KMAX, "failures": bad}
    print(f"V2: primitive-root lemma for 3^(b+1), b <= {BMAX + KMAX}: {bad} failures")
    # V3
    summary["V3"] = {}
    for d in CONTROLS:
        s = run(d, X0MAX_D, KMAX_D, BMAX_D)
        summary["V3"][str(d)] = {"x0_max": X0MAX_D, "k_max": KMAX_D, "b_max": BMAX_D,
                                 "max_inverse_steps": max(v["max_inverse_steps"] for v in s.values()) if s else None}
        print(f"V3: 3x+{d}: {sum(v['targets'] for v in s.values())} targets, failures so far {len(failures)}")
    # V4
    for k in range(KMAX + 1):
        inv = s1[f"{k},0"]["max_inverse_steps"]
        if k >= 1 and inv > k:
            fail(f"V4: targets modulo 2^{k} used {inv} > {k} inverse steps")
    for b in range(1, BMAX + 1):
        inv = s1[f"0,{b}"]["max_inverse_steps"]
        if inv != 1:
            fail(f"V4: targets modulo 3^{b} used {inv} inverse steps, expected 1")
    summary["V4"] = {"inverse_steps_mod_2^k": [s1[f"{k},0"]["max_inverse_steps"] for k in range(KMAX + 1)],
                     "inverse_steps_mod_3^b": [s1[f"0,{b}"]["max_inverse_steps"] for b in range(BMAX + 1)]}
    print("V4: inverse steps used modulo 2^k, k = 0..%d: %s; modulo 3^b, b = 0..%d: %s" %
          (KMAX, summary["V4"]["inverse_steps_mod_2^k"], BMAX, summary["V4"]["inverse_steps_mod_3^b"]))
    # V5
    if write:
        RECEIPT.write_text(json.dumps(summary, indent=1) + "\n")
        print("receipt written")
    elif not RECEIPT.exists():
        fail("V5 receipt missing")
    elif json.loads(RECEIPT.read_text()) != summary:
        fail("V5 summary differs from the receipt")
    if failures:
        print(f"{len(failures)} failure(s)")
        sys.exit(1)
    print("all checks passed")


if __name__ == "__main__":
    main()
