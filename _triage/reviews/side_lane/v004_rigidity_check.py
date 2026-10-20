"""Sidekick probe: independent check of the elementary parts of main's V004 theorem (experiments/viewpoints/V004/
GLOBAL_RIGIDITY.md, main f54b741): every finite-valued binary-automatic h with h(2n)=h(n), h(3n+1)=h(n) (odd n>1)
is constant. The classical inputs (Eilenberg's finite-kernel characterization, Cobham's theorem) are not re-proved.

(a) Identities (2), (3), (4) as exact arithmetic path relations (3(4m+1)+1 = 4(3m+1), 3(2m+1)+1 = 2(3m+2),
    3(3u)+1 = 9u+1 = 3(3u)+1 ...), for m, u up to 10^5.
(b) Ternary closure of K_+ = {n -> h(2^a n + r): a>=1, 0<r<2^a}: for every a <= 14, 0 < r < 2^a, j in {0,1,2},
    the section n -> h(2^a(3n+j)+r) is rewritten into some (a', r') with a'>=1, 0<r'<2^a' (Case A via one Syracuse
    arrow of valuation v, Case B via doubling and (3)); the underlying integer relations are checked for n <= 40.
(c) The finish: b(4n+2) = b(n) for b(n)=h(2n+1) as an arithmetic identity; on Z/mZ (gcd(m,6)=1) the maps
    H(x)=3*4^{-1}x, J(x)=4x+1 satisfy H(J(x)) - J(H(x)) = 3/4 - 1 = -1/4, a unit (m <= 2000).
(d) 3x+5 control: the d=5 analogue h(3m+5)=h(4m+5) holds for the actual cycle labelling c_5 (n <= 2*10^5), while the
    d=1 identities h(3m+1)=h(4m+1) and h(3u)=h(16u+1) fail for c_5 (witnesses recorded): the identities are d-specific.
(e) d-uniform closure up to bounded shifts. For d in {1,5,7,13,61}, states (a, r0, sigma) stand for
    phi(n) = h(2^a (n+sigma) + r0), a >= 1, r0 odd in (0, 2^a). Each ternary section phi(3n+j) is rewritten by the
    d-analogues of Case A (3x+d = 2^v y) and Case B (h(3U) = h(16U+d)) into a state of the same kind. We record the
    largest |sigma| that occurs (0 for d = 1, i.e. main's exact positive-offset closure), the first index from
    which every rewrite is valid, and we test every rewrite on the actual cycle labelling c_d (a genuine nonconstant
    invariant colouring for d > 1) for a <= 7, 31 consecutive n.
(f) Finish for general d: on Z/mZ (m odd, 3 not dividing m, m <= 301) the residue graph with edges x ~ 4x+d and
    y ~ 3*4^{-1}*y has exactly as many components as <3,4> has orbits on Z/gcd(d,m)Z (translation by d/4 instead of
    1/4); adding the all-valuation edges x ~ 2^{-k}(3x+d) leaves exactly the <2,3>-orbits (V13's classification).
Standard library. Run without -O.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def part_a():
    for m in range(0, 10**5):
        assert 3*(4*m + 1) + 1 == 4*(3*m + 1)            # h(3m+1)=h(4m+1)
        assert 3*(2*m + 1) + 1 == 2*(3*m + 2)            # h(3m+2)=h(2m+1)
    for u in range(1, 2*10**5, 2):
        assert 3*(3*u) + 1 == 9*u + 1                    # h(3u)=h(9u+1)
        assert 9*u + 1 == 3*(3*u) + 1 and 12*u + 1 == 4*(3*u) + 1 and 16*u + 1 == 4*(4*u) + 1
    return True


def part_b(A=14):
    cases = {"A": 0, "B": 0}
    for a in range(1, A + 1):
        for r in range(1, 2**a):
            for j in range(3):
                c = 2**a * j + r
                assert 0 < c < 3 * 2**a
                if c % 3:
                    vv = 1 if c % 3 == 2 else 2
                    t = (2**vv * c - 1)//3
                    assert (2**vv * c - 1) % 3 == 0 and t % 2 == 1 and 1 <= t < 2**(a + vv)
                    a2, r2 = a + vv, t
                    for n in range(0, 41):
                        x = 2**(a + vv) * n + t
                        assert 3*x + 1 == 2**vv * (3 * 2**a * n + c)
                    cases["A"] += 1
                else:
                    tt = c // 3
                    ell = v2(tt)
                    u = tt >> ell
                    s = a - ell
                    assert ell < a and s >= 1 and 0 < u < 2**s and u % 2 == 1
                    a2, r2 = s + 4, 16*u + 1
                    assert 0 < r2 < 2**a2
                    for n in range(0, 41):
                        U = 2**s * n + u
                        assert U % 2 == 1 and 3 * 2**a * n + c == 2**ell * 3 * U
                        assert 16*U + 1 == 2**a2 * n + r2
                    cases["B"] += 1
                assert a2 >= 1 and 0 < r2 < 2**a2
    return cases


def part_c():
    for n in range(0, 10**5):
        assert 2*(4*n + 2) + 1 == 4*(2*n + 1) + 1      # b(4n+2) = h(8n+5) = h(4(2n+1)+1) = h(2n+1) = b(n)
    cnt = 0
    for m in range(5, 2001):
        if m % 2 == 0 or m % 3 == 0:
            continue
        i4 = pow(4, -1, m)
        for x in (0, 1, 2, m - 1):
            H = lambda y: (3 * i4 * y) % m
            J = lambda y: (4*y + 1) % m
            assert (H(J(x)) - J(H(x))) % m == (3*i4 - 1) % m
        assert (3*i4 - 1) % m == (-i4) % m          # 3/4 - 1 = -1/4, a unit
        cnt += 1
    return cnt


def cycle_label(d, N):
    lab = {}
    def T(x):
        y = 3*x + d
        return y >> v2(y)
    out = [0]*(N + 1)
    for n in range(1, N + 1):
        x = n >> v2(n)
        path, seen = [], set()
        while x not in lab and x not in seen:
            seen.add(x)
            path.append(x)
            x = T(x)
        if x in lab:
            L = lab[x]
        else:
            i = path.index(x)
            L = min(path[i:])
        for y in path:
            lab[y] = L
        out[n] = lab[n >> v2(n)]
    return out


def part_d():
    N = 2*10**5
    c = cycle_label(5, N)
    for m in range(0, (N - 5)//4):
        assert c[3*m + 5] == c[4*m + 5]
    fail1 = next(m for m in range(1, N//4) if c[3*m + 1] != c[4*m + 1])
    fail3 = next(u for u in range(1, N//16, 2) if c[3*u] != c[16*u + 1])
    return {"d5_analogue_holds_m_up_to": (N - 5)//4, "d1_identity_2_fails_at_m": fail1,
            "d1_identity_3_fails_at_u": fail3, "labels": [c[3*fail3], c[16*fail3 + 1]]}


def section(d, a, r0, sigma, j):
    """Rewrite n -> h(2^a (3n+j+sigma) + r0) as n -> h(2^a2 (n+sigma2) + r2); also return the relation's case."""
    s1, j1 = divmod(j + sigma, 3)
    c = 2**a * j1 + r0
    if c % 3:
        vv = 1 if (2 * c - d) % 3 == 0 else 2
        t = (2**vv * c - d) // 3
        assert (2**vv * c - d) % 3 == 0 and t % 2 == 1
        a2 = a + vv
        tau, r2 = divmod(t, 2**a2)
        return a2, r2, s1 + tau, "A", (vv, t)
    tt = c // 3
    ell = v2(tt)
    u = tt >> ell
    s = a - ell
    assert 0 <= ell < a and u % 2 == 1 and u < 2**s
    a2 = s + 4
    tau, r2 = divmod(16*u + d, 2**a2)
    return a2, r2, s1 + tau, "B", (s, u)


def part_e(N=2*10**5):
    out = {}
    for d in (1, 5, 7, 13, 61):
        S = 0
        while True:                      # smallest S with |sigma| <= S closed under sections, a <= 12
            ok = True
            for a in range(1, 13):
                for r0 in range(1, 2**a, 2):
                    for sigma in range(-S, S + 1):
                        for j in range(3):
                            if abs(section(d, a, r0, sigma, j)[2]) > S:
                                ok = False
                                break
                        if not ok:
                            break
                    if not ok:
                        break
                if not ok:
                    break
            if ok:
                break
            S += 1
        c = cycle_label(d, N) if d > 1 else None
        n0, tested = 0, 0
        for a in range(1, 13):
            for r0 in range(1, 2**a, 2):
                for sigma in range(-S, S + 1):
                    for j in range(3):
                        a2, r2, sg2, case, _ = section(d, a, r0, sigma, j)
                        assert 0 < r2 < 2**a2 and abs(sg2) <= S
                        # first n from which both evaluations are at positive arguments
                        k = 0
                        while 2**a * (3*k + j + sigma) + r0 < 1 or 2**a2 * (k + sg2) + r2 < 1:
                            k += 1
                        n0 = max(n0, k)
                        for n in range(k, k + 41):
                            y = 2**a * (3*n + j + sigma) + r0
                            x = 2**a2 * (n + sg2) + r2
                            if case == "A":          # 3x + d = 2^v y, x odd
                                assert x % 2 == 1 and 3*x + d == 2**(a2 - a) * y
                            else:                    # y = 2^ell * 3U and x = 16U + d, U odd
                                U = (x - d) // 16
                                assert (x - d) % 16 == 0 and U % 2 == 1 and y == 3*U << v2(y // (3*U)) \
                                    and (y // (3*U)) & (y // (3*U) - 1) == 0
                        if c is not None and a <= 7:
                            for n in range(k, k + 31):
                                y = 2**a * (3*n + j + sigma) + r0
                                x = 2**a2 * (n + sg2) + r2
                                if x <= N and y <= N:
                                    assert c[y] == c[x], (d, a, r0, sigma, j, n)
                                    tested += 1
        out[f"d={d}"] = {"max_abs_shift": S, "first_valid_index": n0, "cycle_label_rewrites_tested": tested,
                         "cycle_labels": sorted(set(c[1:]))[:8] if c is not None else "constant (d=1)"}
    return out


def orbits_mult(g, gens):
    seen, cnt = set(), 0
    for x in range(g):
        if x in seen:
            continue
        cnt += 1
        st = [x]
        seen.add(x)
        while st:
            y = st.pop()
            for k in gens:
                z = (k * y) % g
                if z not in seen:
                    seen.add(z)
                    st.append(z)
    return cnt


def components(m, edges):
    par = list(range(m))
    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for x, y in edges:
        rx, ry = f(x), f(y)
        if rx != ry:
            par[rx] = ry
    return len({f(x) for x in range(m)})


def part_f():
    from math import gcd
    rows, cases = {}, 0
    for d in (1, 5, 7, 13, 61, 35, 65):
        mism = []
        for m in range(1, 302, 2):
            if m % 3 == 0:
                continue
            i4, i2 = pow(4, -1, m) if m > 1 else 0, pow(2, -1, m) if m > 1 else 0
            E1 = [(x, (4*x + d) % m) for x in range(m)] + [(y, (3 * i4 * y) % m) for y in range(m)]
            g = gcd(d, m)
            comp1 = components(m, E1)
            pred1 = orbits_mult(g, (3, 4)) if g > 1 else 1
            E2 = E1 + [(x, (pow(i2, k, m) * (3*x + d)) % m) for x in range(m) for k in range(1, 3)]
            comp2 = components(m, E2)
            pred2 = orbits_mult(g, (2, 3)) if g > 1 else 1
            if comp1 != pred1 or comp2 != pred2:
                mism.append((m, comp1, pred1, comp2, pred2))
            cases += 1
        assert not mism, (d, mism[:5])
        g = d
        rows[f"d={d}"] = {"<3,4>-orbits on Z/dZ": orbits_mult(d, (3, 4)) if d > 1 else 1,
                          "<2,3>-orbits on Z/dZ": orbits_mult(d, (2, 3)) if d > 1 else 1}
    return {"moduli_checked": cases, "orbit_counts": rows}


def main():
    out = {"probe": "v004_rigidity_check", "main": "f54b741", "identities": part_a(),
           "ternary_closure_cases": part_b(), "finish_moduli_checked": part_c(), "control_d5": part_d(),
           "d_uniform_closure": part_e(), "d_uniform_finish": part_f(),
           "result": "PASS"}
    (HERE / "v004_rigidity_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
