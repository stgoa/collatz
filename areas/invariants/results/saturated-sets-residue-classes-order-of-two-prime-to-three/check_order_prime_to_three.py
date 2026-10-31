#!/usr/bin/env python3
"""Certificate for saturated-sets-residue-classes-order-of-two-prime-to-three.

Setting: T the Collatz map on the positive integers, B a nonempty saturated set (x in B iff T(x) in B). Moves that
stay in B: double, halve (even), forward (odd: 3x+1), inverse (x = 4 mod 6: (x-1)/3). Two composite moves from an odd
z, both landing on an odd element:
    scaling   sigma_s(z) = 4^s z + (4^s - 1)/3     (forward, 2s doublings, inverse; legal for every odd z, s >= 1),
    inverse   iota_j(z)  = (2^j z - 1)/3           (j doublings, inverse; legal iff 2^j z = 1 mod 3).
In w = 3z + 1 the scaling is w -> 4^s w, so it steers z modulo 3^b freely (4 generates the units = 1 mod 3 modulo
3^(b+1)); when 3 does not divide ord_M'(2), s can be chosen with 4^s = 1 mod M' at the same time, so the steering
costs nothing modulo M'. On Z/M' the permutations sigma_s, iota_j generate a group containing the translation
w -> w + 1, hence transitive. This gives odd elements of B in every joint class modulo 3^b M', and the 2-adic lift
of the six-smooth theorem (j = 1 doublings and one inverse step per binary digit) gives every class modulo
2^k 3^b M'.
V1  for every M' <= MP_MAX with gcd(M', 6) = 1 and 3 not dividing ord_M'(2), every odd start x0 <= X0MAX, k <= KMAX,
    b <= BMAX and every target class modulo 2^k 3^b M': the construction returns a path of moves from x0; every move is
    replayed and checked for legality, and the end point for its residues;
V2  the group fact: for the same M', the permutations sigma_s (1 <= s <= ord(4)) and iota_j (1 <= j <= ord(2)) of Z/M'
    generate a transitive group (breadth-first search from 0 reaches every class), and the translation w -> w + 1,
    i.e. z -> z + 1/3, is checked to lie in the group generated (breadth-first search over the permutations);
V3  the hypothesis is used: for M' in {7, 19, 37, 73} (3 divides the order of 2) the free parity fix does not exist
    (no s with s = 1 mod 3 and 4^s = 1 mod M'); recorded, nothing claimed about those moduli here;
V4  control: for the map 3x+5 the same scalings and inverses act modulo 5 with translations by multiples of 5, i.e.
    trivially: the group generated is not transitive on Z/5 (the multiples of 5 are saturated for 3x+5), as it must be;
V5  receipt comparison. Exit 1 on failure; --write-receipt regenerates order_prime_to_three.json.
Standard library only; deterministic."""
import json
import sys
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "order_prime_to_three.json"
MP_MAX = 100
X0MAX, KMAX, BMAX = 21, 2, 1
DEEP = {5: (3, 2), 11: (3, 2), 25: (2, 2), 65: (2, 1)}    # a few moduli with deeper (k, b)
EXCLUDED = (7, 19, 37, 73)
failures = []


def fail(msg):
    failures.append(msg)
    print("FAIL:", msg)


def order(a, n):
    if n == 1:
        return 1
    k, x = 1, a % n
    while x != 1:
        x = x * a % n
        k += 1
    return k


def crt(r1, m1, r2, m2):
    """x = r1 mod m1, x = r2 mod m2 with gcd(m1, m2) = 1."""
    inv = pow(m1, -1, m2) if m2 > 1 else 0
    return (r1 + m1 * (((r2 - r1) * inv) % m2)) % (m1 * m2)


def group_words(Mp, d=1):
    """BFS over Z/Mp with the generators; returns parent pointers (word to every reachable class from 0) and the
    transitivity flag. Maps in z-coordinates: sigma_s(z) = 4^s z + d(4^s-1)/3, iota_j(z) = (2^j z - d)/3 (mod Mp)."""
    inv3 = pow(3, -1, Mp) if Mp > 1 else 0
    o2, o4 = order(2, Mp), order(4, Mp)
    gens = []
    for s in range(1, o4 + 1):
        f = pow(4, s, Mp)
        gens.append((("S", s), lambda z, f=f: (f * z + d * (f - 1) * inv3) % Mp))
    for j in range(1, o2 + 1):
        g = pow(2, j, Mp)
        gens.append((("I", j), lambda z, g=g: ((g * z - d) * inv3) % Mp))
    return gens


def bfs(Mp, gens, start):
    parent = {start: None}
    dq = deque([start])
    while dq:
        u = dq.popleft()
        for name, f in gens:
            v = f(u)
            if v not in parent:
                parent[v] = (u, name)
                dq.append(v)
    return parent


def word_to(parent, target):
    word = []
    v = target
    while parent[v] is not None:
        u, name = parent[v]
        word.append(name)
        v = u
    return list(reversed(word))


class Construction:
    def __init__(self, Mp):
        self.Mp = Mp
        self.o4 = order(4, Mp)
        if self.o4 % 3 == 0:
            raise ValueError("hypothesis fails")
        self.gens = group_words(Mp)

    def scale(self, z, s, moves):
        """sigma_s on the integer z (odd): forward, 2s doublings, inverse."""
        x = 3 * z + 1
        moves.append("F")
        x *= 4 ** s
        moves.extend("D" * (2 * s))
        if not (x % 2 == 0 and x % 3 == 1):
            raise RuntimeError("scaling inverse illegal")
        moves.append("I")
        return (x - 1) // 3

    def free_scale(self, z, s_mod3, moves, b_extra=0, s_mod3b=None):
        """A scaling with 4^s = 1 mod Mp and s in a prescribed class modulo 3 (or modulo 3^(b_extra))."""
        if s_mod3b is None:
            mod3b, r = 3, s_mod3 % 3
        else:
            mod3b, r = 3 ** b_extra, s_mod3b % 3 ** b_extra
        s = crt(0, self.o4, r, mod3b)
        if s == 0:
            s = self.o4 * mod3b
        return self.scale(z, s, moves)

    def inverse(self, z, j, moves):
        if z % 3 == 0:                       # a scaling with s = 1 mod 3 shifts z mod 3 by one
            z = self.free_scale(z, 1, moves)
        if (pow(2, j, 3) * z) % 3 != 1:      # fix the parity requirement: shift z mod 3 by the needed amount
            need = (pow(2, -j, 3) - z) % 3   # want z' = 2^(-j) mod 3; scaling shifts z by s mod 3
            z = self.free_scale(z, need, moves)
        x = 2 ** j * z
        moves.extend("D" * j)
        if not (x % 2 == 0 and x % 3 == 1):
            raise RuntimeError("inverse illegal")
        moves.append("I")
        return (x - 1) // 3

    def base(self, x0, b, eps, rho):
        """An odd element = eps mod 3^b, = rho mod Mp, with moves from the odd x0."""
        Mp = self.Mp
        moves, z = [], x0
        parent = bfs(Mp, self.gens, z % Mp)
        if rho % Mp not in parent:
            raise RuntimeError("not transitive")
        for name in word_to(parent, rho % Mp):
            kind, par = name
            z = self.scale(z, par, moves) if kind == "S" else self.inverse(z, par, moves)
        if z % Mp != rho % Mp:
            raise RuntimeError("word did not reach rho")
        # final 3-adic steering: 4^s (3z+1) = 1 + 3 eps mod 3^(b+1), with 4^s = 1 mod Mp
        mod = 3 ** (b + 1)
        w = (3 * z + 1) % mod
        target = (1 + 3 * eps) % mod
        s0 = None
        for s in range(3 ** b):
            if (pow(4, s, mod) * w) % mod == target:
                s0 = s
                break
        if s0 is None:
            raise RuntimeError("steering failed")
        z = self.free_scale(z, None, moves, b_extra=b, s_mod3b=s0)
        return z, moves

    def odd_target(self, x0, k, b, u, eps, rho):
        """Odd element = u mod 2^k (u odd), = eps mod 3^b, = rho mod Mp."""
        Mp = self.Mp
        if k <= 1:
            return self.base(x0, b, eps, rho)
        mod3 = 3 ** (b + 1)
        c3 = (pow(2, -1, mod3) * (1 + 3 * eps)) % mod3
        cp = (pow(2, -1, Mp) * (1 + 3 * rho)) % Mp if Mp > 1 else 0
        up = ((3 * u + 1) // 2) % 2 ** (k - 1)          # any class modulo 2^(k-1), odd or even
        y, moves = self.target(x0, k - 1, b + 1, up, c3, cp)
        x = 2 * y
        moves.append("D")
        if not (x % 2 == 0 and x % 3 == 1):
            raise RuntimeError("lift inverse illegal")
        moves.append("I")
        return (x - 1) // 3, moves

    def target(self, x0, k, b, r, eps, rho):
        Mp = self.Mp
        r %= 2 ** k
        if r == 0:
            c3 = (pow(2, -k, 3 ** b) * eps) % 3 ** b if b > 0 else 0
            cp = (pow(2, -k, Mp) * rho) % Mp if Mp > 1 else 0
            y, moves = self.base(x0, b, c3, cp)
            return 2 ** k * y, moves + ["D"] * k
        v = 0
        while r % 2 == 0:
            r //= 2
            v += 1
        c3 = (pow(2, -v, 3 ** b) * eps) % 3 ** b if b > 0 else 0
        cp = (pow(2, -v, Mp) * rho) % Mp if Mp > 1 else 0
        y, moves = self.odd_target(x0, k - v, b, r, c3, cp)
        return 2 ** v * y, moves + ["D"] * v


def replay(x0, moves, d=1):
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


def run(Mp, x0max, kmax, bmax):
    con = Construction(Mp)
    stats = {"targets": 0, "max_moves": 0, "max_inverse_steps": 0}
    for x0 in range(1, x0max + 1, 2):
        for k in range(kmax + 1):
            for b in range(bmax + 1):
                M = 2 ** k * 3 ** b * Mp
                for t in range(M):
                    r, eps, rho = t % 2 ** k, t % 3 ** b, t % Mp
                    x, moves = con.target(x0, k, b, r, eps, rho)
                    y = replay(x0, moves)
                    if y is None or y != x or x % M != t:
                        fail(f"Mp={Mp} x0={x0} k={k} b={b} target {t}: construction or replay wrong")
                        return stats
                    stats["targets"] += 1
                    stats["max_moves"] = max(stats["max_moves"], len(moves))
                    stats["max_inverse_steps"] = max(stats["max_inverse_steps"], moves.count("I"))
    return stats


def main():
    write = "--write-receipt" in sys.argv
    summary = {"V1": {}, "V2": {}, "V3": {}, "V4": {}}
    moduli = [m for m in range(5, MP_MAX + 1) if m % 2 and m % 3 and order(2, m) % 3 != 0]
    print(f"moduli M' <= {MP_MAX}, prime to 6, with 3 not dividing ord(2): {moduli}")
    for Mp in moduli:
        kmax, bmax = DEEP.get(Mp, (KMAX, BMAX))
        st = run(Mp, X0MAX, kmax, bmax)
        summary["V1"][str(Mp)] = {"k_max": kmax, "b_max": bmax, **st}
        if failures:
            break
    tot = sum(v["targets"] for v in summary["V1"].values())
    print(f"V1: {len(moduli)} moduli, {tot} targets replayed, {len(failures)} failures; max moves "
          f"{max(v['max_moves'] for v in summary['V1'].values())}, max inverse steps "
          f"{max(v['max_inverse_steps'] for v in summary['V1'].values())}")
    # V2: transitivity and the translation
    for Mp in moduli:
        gens = group_words(Mp)
        parent = bfs(Mp, gens, 0)
        trans = len(parent) == Mp
        diam = max(len(word_to(parent, v)) for v in parent)
        # the group generated, as a set of permutations, and the translation z -> z + 1/3 (w -> w + 1) in it
        ident = tuple(range(Mp))
        seen = {ident}
        dq = deque([ident])
        gen_perms = [tuple(f(z) for z in range(Mp)) for _, f in gens]
        while dq:
            perm = dq.popleft()
            for g in gen_perms:
                comp = tuple(g[perm[z]] for z in range(Mp))
                if comp not in seen:
                    seen.add(comp)
                    dq.append(comp)
        inv3 = pow(3, -1, Mp)
        translation = tuple((z + inv3) % Mp for z in range(Mp))
        has_translation = translation in seen
        summary["V2"][str(Mp)] = {"transitive": trans, "bfs_diameter": diam, "ord2": order(2, Mp), "ord4": order(4, Mp),
                                  "group_size": len(seen), "translation_in_group": has_translation}
        if not trans or not has_translation:
            fail(f"V2: group not transitive or translation missing for M' = {Mp}")
    print(f"V2: transitive on Z/M' with the translation in the group for all {len(moduli)} moduli; max BFS diameter "
          f"{max(v['bfs_diameter'] for v in summary['V2'].values())}; group sizes "
          f"{[v['group_size'] for v in summary['V2'].values()]}")
    # V3
    for Mp in EXCLUDED:
        o4 = order(4, Mp)
        exists = any(s % 3 == 1 and pow(4, s, Mp) == 1 for s in range(1, 3 * o4 + 1))
        summary["V3"][str(Mp)] = {"ord2": order(2, Mp), "ord4": o4, "free_parity_fix_exists": exists}
        if exists:
            fail(f"V3: unexpected free parity fix for M' = {Mp}")
    print("V3: excluded moduli", {m: summary["V3"][str(m)]["ord2"] for m in EXCLUDED}, "no free parity fix, as expected")
    # V4: 3x+5 modulo 5
    gens5 = group_words(5, d=5)
    parent5 = bfs(5, gens5, 0)
    summary["V4"] = {"3x+5 mod 5 reachable from 0": sorted(parent5.keys()), "transitive": len(parent5) == 5}
    if len(parent5) == 5:
        fail("V4: the 3x+5 control is transitive modulo 5")
    print("V4: 3x+5 modulo 5: reachable from 0 =", sorted(parent5.keys()))
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
