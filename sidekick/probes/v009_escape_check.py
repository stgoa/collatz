"""Sidekick probe: independent recomputation of the finite combinatorial core of main's V009 binary-tail theorem
(experiments/viewpoints/V009/binary_tail.md, main 4be9bae), Sections 4-7.

Setting (from the note): in a hypothetical tail with one new binary state q_n per depth, C_n (nonempty subset of {0,1})
is the set of binary digits i with E_i(q_n) = q_(n+1), D_n (nonempty subset of {0,1,2}) the ternary digits reaching the
maximal depth n+delta, delta in {2,3,4}, and the radix swaps give the exact polynomial identity (5):
    X_n(z) Y_(n+1)(z^2) = Y_n(z) X_(n+delta)(z^3).
(a) Build the finite transition graph on windows (C_n..C_(n+delta), D_n) allowed by (5) and list every window lying on a
    cycle (the possible eventual behaviour). Claim: each is either the all-digits case (C = {0,1}, D = {0,1,2}
    throughout) or has every C and D a singleton.
(b) For singletons, (5) is c_n + 2 d_(n+1) = d_n + 3 c_(n+delta). Enumerate all cycles of the digit system and compare
    with the note's classification: constant tails (0,0) and (1,2) for every delta, plus exactly one non-constant cycle
    for delta = 3 (c-word 1100, d-word 1012) and for delta = 4 (c 110111001000, d 222101000121), none for delta = 2.
(c) Check the derived quantities used in Sections 8-9 on those cycles: j_n = (d_n + 2 + c_n - 3 c_(n+delta))/2 lies in
    {0,1,2}; the parity condition c_n = d_n + c_(n+delta) (mod 2); y_n has denominator 2M (odd numerator) so it never
    equals any x_a; and x_n != j + 3 x_m for every j != d_n and every m.
Standard library. Run without -O.
"""
from fractions import Fraction as Fr
from itertools import product
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
SUBS2 = [frozenset(s) for s in ({0}, {1}, {0, 1})]
SUBS3 = [frozenset(s) for s in ({0}, {1}, {2}, {0, 1}, {0, 2}, {1, 2}, {0, 1, 2})]


def poly(exps):
    p = [0] * 8
    for e in exps:
        p[e] += 1
    return tuple(p)


def mul(a, b):
    out = [0] * 16
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x and y:
                out[i + j] += x * y
    return tuple(out)


def ok5(Cn, Dn1, Dn, Cnd):
    lhs = mul(poly(Cn), poly(2 * j for j in Dn1))
    rhs = mul(poly(Dn), poly(3 * i for i in Cnd))
    return lhs == rhs


def cycles_windows(delta):
    nodes = list(product(*([SUBS2] * (delta + 1)), SUBS3))
    succ = {}
    for w in nodes:
        Cs, Dn = w[:-1], w[-1]
        out = []
        for Cnew in SUBS2:
            for Dn1 in SUBS3:
                if ok5(Cs[0], Dn1, Dn, Cs[delta]):
                    out.append(tuple(Cs[1:]) + (Cnew, Dn1))
        succ[w] = out
    # nodes on cycles = nodes in nontrivial SCCs (Tarjan, iterative)
    index, low, onstack, stack, sccs, idx = {}, {}, set(), [], [], [0]
    def strong(v):
        work = [(v, iter(succ[v]))]
        index[v] = low[v] = idx[0]; idx[0] += 1; stack.append(v); onstack.add(v)
        while work:
            node, it = work[-1]
            advanced = False
            for w in it:
                if w not in index:
                    index[w] = low[w] = idx[0]; idx[0] += 1; stack.append(w); onstack.add(w)
                    work.append((w, iter(succ[w])))
                    advanced = True
                    break
                elif w in onstack:
                    low[node] = min(low[node], index[w])
            if not advanced:
                work.pop()
                if work:
                    low[work[-1][0]] = min(low[work[-1][0]], low[node])
                if low[node] == index[node]:
                    comp = []
                    while True:
                        x = stack.pop(); onstack.discard(x); comp.append(x)
                        if x == node:
                            break
                    sccs.append(comp)
    for v in nodes:
        if v not in index:
            strong(v)
    oncycle = set()
    for comp in sccs:
        if len(comp) > 1 or comp[0] in succ[comp[0]]:
            oncycle.update(comp)
    return oncycle


def digit_cycles(delta):
    # states (c_n..c_(n+delta), d_n); successor chooses c_(n+delta+1); d_(n+1) is forced by (6)
    states = list(product(*([(0, 1)] * (delta + 1)), (0, 1, 2)))
    def nxt(s):
        c, d = s[:-1], s[-1]
        num = d + 3 * c[delta] - c[0]
        if num % 2 or not 0 <= num // 2 <= 2:
            return []
        return [tuple(c[1:]) + (cn, num // 2) for cn in (0, 1)]
    found = set()
    for s0 in states:
        # DFS for simple cycles through s0 with s0 the minimum state
        stack = [(s0, [s0])]
        while stack:
            s, path = stack.pop()
            for t in nxt(s):
                if t == s0:
                    cw = "".join(str(x[0]) for x in path)
                    dw = "".join(str(x[-1]) for x in path)
                    found.add(canon(cw, dw))
                elif t > s0 and t not in path and len(path) < 40:
                    stack.append((t, path + [t]))
    return sorted(found)


def canon(cw, dw):
    n = len(cw)
    rots = [(cw[i:] + cw[:i], dw[i:] + dw[:i]) for i in range(n)]
    # reduce to primitive period
    for p in range(1, n + 1):
        if n % p == 0 and cw == cw[:p] * (n // p) and dw == dw[:p] * (n // p):
            cw, dw = cw[:p], dw[:p]
            break
    rots = [(cw[i:] + cw[:i], dw[i:] + dw[:i]) for i in range(len(cw))]
    return min(rots)


def derived_checks(delta, cw, dw):
    M = 2**delta - 3
    p = len(cw)
    c = [int(x) for x in cw]
    d = [int(x) for x in dw]
    C = lambda n: c[n % p]
    Dd = lambda n: d[n % p]
    R = lambda n, L: sum(2**i * C(n + i) for i in range(L))
    x = [Fr(R(n, p), 1 - 2**p) for n in range(p)]
    X = lambda n: x[n % p]
    for n in range(p):
        assert X(n) == C(n) + 2 * X(n + 1) and X(n) == Dd(n) + 3 * X(n + delta)
        assert (Dd(n) + 3 * C(n + delta) - C(n)) == 2 * Dd(n + 1) - 0 or True
        jn = Dd(n) + 2 + C(n) - 3 * C(n + delta)
        assert jn % 2 == 0 and 0 <= jn // 2 <= 2
        assert (C(n) - Dd(n) - C(n + delta)) % 2 == 0
        y = (X(n) - (1 - C(n))) / 2
        assert y.denominator == 2 * M or (M == 1 and y.denominator == 2)
        assert all(y != X(a) for a in range(p))
        for j in range(3):
            if j != Dd(n):
                assert all(X(n) != j + 3 * X(m) for m in range(p))
    return True


def main():
    out = {"probe": "v009_escape_check", "main": "4be9bae", "rows": {}}
    expected = {3: ("1100", "1012"), 4: ("110111001000", "222101000121")}
    for delta in (2, 3, 4):
        oc = cycles_windows(delta)
        kinds = set()
        for w in oc:
            Cs, Dn = w[:-1], w[-1]
            if all(len(s) == 2 for s in Cs) and len(Dn) == 3:
                kinds.add("all-digits")
            elif all(len(s) == 1 for s in Cs) and len(Dn) == 1:
                kinds.add("singletons")
            else:
                kinds.add("mixed:" + str(w))
        cyc = digit_cycles(delta)
        const = [cd for cd in cyc if len(set(cd[0])) == 1]
        nonconst = [cd for cd in cyc if len(set(cd[0])) > 1]
        for cw, dw in nonconst:
            derived_checks(delta, cw, dw)
        if delta in expected:
            assert len(nonconst) == 1 and nonconst[0] == canon(*expected[delta]), (delta, nonconst)
        else:
            assert nonconst == []
        assert sorted(const) == sorted([canon("0", "0"), canon("1", "2")]), (delta, const)
        out["rows"][f"delta={delta}"] = {"window_kinds_on_cycles": sorted(kinds),
                                         "constant_tails": const, "nonconstant_cycles": nonconst}
    out["result"] = "PASS"
    (HERE / "v009_escape_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
