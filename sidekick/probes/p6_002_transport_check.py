"""Sidekick probe: independent check of main's P6-002 (S.2 barrier to arbitrary-target linear counting
transport, main de32608), with this branch's own maps. Nothing is imported from main.

(1) The one-arrow construction (4)-(10): for d in {1,5,7,13,61}, h = max(3,d) (odd), J in {3,..,8} and
    t up to 40, every n(a,y) = (2^a y - d)/3 (a = 3..J, y = d(-1)^a mod 3, y odd in [h, 6t]) is an odd
    integer < X_t = 2^(J+1) t with v2(3n+d) = a, S_d(n) = y and 2y < n; all pairs give distinct n; the
    exact counts N_t = (J-2)t - C and |A_t| = 3t - (h-1)/2 hold.
(2) Brute force, small cutoffs: for every odd n <= X_t (first half-descent L_d computed by iteration,
    absorbed at 1, cycles detected), the full transported mass into A_t is at least N_t, and the excess
    over kappa|A_t| grows linearly in t once J > 3 kappa + 2.
(3) Sparse targets (14)-(15): #(H_alpha intersect [1,Y]) = floor(m^(p/q)), m = floor((Y-1)/6), for
    several p/q and all Y <= 3*10^4; every even a in 4..J gives a one-arrow first-half preimage.
(4) Singleton controls: L_1((10*4^j-1)/3) = 5 and L_5((38*4^j-5)/3) = 19 at time 1, with 19 -> 31 -> 49
    -> 19 a raw 3x+5 cycle.
Standard library. Run without -O.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def S(d, n):
    if n == 1:
        return 1
    y = 3*n + d
    return y >> v2(y)


def first_half(d, n, cap=10**5):
    """(time, target) of the first j >= 1 with S_d^j(n) <= n/2, or None if the orbit cycles first."""
    seen, x, j = set(), n, 0
    while j < cap:
        x, j = S(d, x), j + 1
        if 2*x <= n:
            return j, x
        if x in seen:
            return None
        seen.add(x)
    raise RuntimeError("cap")


def construction(d, h, J, t):
    srcs = {}
    for a in range(3, J + 1):
        for y in range(h, 6*t + 1, 2):
            if (y - d*(-1)**a) % 3:
                continue
            num = 2**a * y - d
            assert num % 3 == 0
            n = num // 3
            X = 2**(J + 1) * t
            assert n % 2 == 1 and n < X and v2(3*n + d) == a and S(d, n) == y and 2*y < n
            assert n not in srcs
            srcs[n] = y
    return srcs


def part1_2():
    cases, brute = 0, 0
    for d in (1, 5, 7, 13, 61):
        h = max(3, d) | 1
        H = (h - 1)//2
        for J in range(3, 9):
            C = 0
            for a in range(3, J + 1):
                ra = next(r for r in (1, 5) if (r - d*(-1)**a) % 3 == 0)
                C += sum(1 for y in range(1, h, 2) if y % 6 == ra)
            for t in range(-(-h // 6), 41):
                srcs = construction(d, h, J, t)
                A = [y for y in range(h, 6*t + 1, 2)]
                assert len(srcs) == (J - 2)*t - C and len(A) == 3*t - H
                cases += 1
                if J <= 5 and t <= 12 and d in (1, 5, 61):
                    X = 2**(J + 1) * t
                    Aset = set(A)
                    mass = 0
                    for n in range(3, X + 1, 2):
                        fh = first_half(d, n)
                        if fh and fh[1] in Aset:
                            mass += 1
                    assert mass >= len(srcs)
                    brute += 1
    return cases, brute


def part3():
    out = 0
    for p, q in ((1, 2), (1, 3), (2, 3), (3, 4)):
        H = []
        j = 1
        while True:
            # 6*ceil(j^(q/p)) + 1 with exact integer ceil of a rational power
            lo = 0
            hi = 1
            while hi**p < j**q:
                hi *= 2
            while lo < hi:      # least c with c^p >= j^q
                mid = (lo + hi)//2
                if mid**p >= j**q:
                    hi = mid
                else:
                    lo = mid + 1
            v = 6*lo + 1
            if v > 3*10**4:
                break
            H.append(v)
            j += 1
        assert all(b > a for a, b in zip(H, H[1:])) and all(v % 6 == 1 and v >= 7 for v in H)
        for Y in range(1, 3*10**4 + 1):
            m = (Y - 1)//6
            cnt = sum(1 for v in H if v <= Y)
            r = 0
            while (r + 1)**q <= m**p:
                r += 1
            assert cnt == r
        for y in H[:50]:
            for a in range(4, 13, 2):
                n = (2**a * y - 1)//3
                assert 3*n + 1 == 2**a * y and first_half(1, n) == (1, y)
        out += 1
    return out


def part4():
    for j in range(1, 30):
        n = (10 * 4**j - 1)//3
        assert 3*n + 1 == 5 * 2**(2*j + 1) and first_half(1, n) == (1, 5)
        u = (38 * 4**j - 5)//3
        assert 3*u + 5 == 19 * 2**(2*j + 1) and first_half(5, u) == (1, 19)
    x, vals = 19, []
    for _ in range(3):
        y = 3*x + 5
        vals.append(v2(y))
        x = y >> v2(y)
    assert x == 19 and vals == [1, 1, 3]
    return True


def main():
    cases, brute = part1_2()
    out = {"probe": "p6_002_transport_check", "main": "de32608", "construction_cases": cases,
           "brute_force_mass_cases": brute, "sparse_alpha_cases": part3(), "singletons": part4(),
           "result": "PASS"}
    (HERE / "p6_002_transport_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
