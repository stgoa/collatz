"""Independent audit of R2-R4 at d = 1 (the Syracuse map).

Uses the generic construction in affine_controls.py, not the repository's
right_aligned_packets.py, and checks the written statements directly from
their definitions:

  * Theorem 1, (3): 3 E_T(N) - H_(T-1)(Pi_N) = <1,nu_N> + H_(T-1)(eta_N),
    with E_T built from Q_T and R_(r,T), for every T up to extinction;
  * Theorem 1, (2): support in {5,7,11,13} and ||eta_N||_1 <= 6b for every
    N <= 10^5 and for sampled N up to 10^18;
  * (7): the dyadic core table for b = 3..1500;
  * Lemma 2: the three ratio bounds for N >= 16 and the constant 505/512;
  * the valuation partition in (6), non-vacuously, with orbit indicators;
  * the least-exception arithmetic, and that a least counterexample is never
    congruent to 2 mod 3 (so that argument alone always gives -1);
  * W(N) = sup_L H_L(Pi_N), a lower bound on ||J^+||_1 for any certificate;
  * certificate minimality: the archive's stored currents equal the time-
    aggregated forward push of their packets, and adding a nonnegative
    source only increases the current pointwise.

Finite checks only. Standard library only. Run without -O.
"""
from collections import defaultdict
from decimal import Decimal, getcontext
from pathlib import Path
import csv
import json
import random
import sys

from affine_controls import cutoffs, packets, push, source, step

D = 1
CORE_TAU = {5: 1, 7: 5, 11: 4, 13: 2}


def tau(x):
    t = 0
    while x != 1:
        x, t = step(D, x), t + 1
    return t


def h(x, T, cache):
    if x not in cache:
        cache[x] = tau(x)
    return min(T, cache[x])


def H(mu, T, cache):
    return sum(c*h(x, T, cache) for x, c in mu.items())


def discrepancy_3E(N, T, cache):
    """3 E_T(N) from (Q_T, R_(r,T)) exactly as written in Section 1."""
    _, n1, n2 = cutoffs(D, N)
    Q = lambda u: sum(h(x, T, cache) for x in range(1, u + 1, 2))
    R = lambda r, u: sum(h(x, T, cache) for x in range(1, u + 1, 2) if x % 6 == r)
    return 3*R(5, n1) - Q(n1) + 3*R(1, n2) - Q(n2)


def check_theorem1_transfer(nmax):
    cache, worst = {}, 0
    for N in range(8, nmax + 1):
        packet, eta, _ = packets(D, N)
        nu = source(D, N)
        mass = sum(nu.values())
        assert abs(mass) <= 8
        b = (N - 1).bit_length()
        horizon = max(h(x, 10**9, cache) for x in nu) + 2
        for T in range(1, horizon + 1):
            gap = discrepancy_3E(N, T, cache) - H(packet, T - 1, cache)
            assert gap == mass + H(eta, T - 1, cache), (N, T)
            assert abs(gap) <= 8 + 30*b
            worst = max(worst, abs(gap))
    return worst


def check_remainder(N):
    _, eta, _ = packets(D, N, materialize=False)
    b = (N - 1).bit_length()
    assert set(eta) <= set(CORE_TAU) and sum(map(abs, eta.values())) <= 6*b, N
    return eta


def check_dyadic(bmax):
    table = {0: {5: 2, 7: -1}, 1: {5: -1, 7: 1, 13: -1}, 2: {5: -1, 13: -2},
             3: {5: -1, 7: -1}, 4: {5: -1, 7: -2, 13: 2}, 5: {5: 2, 7: -3, 13: 1}}
    for b in range(3, bmax + 1):
        assert check_remainder(1 << b) == table[b % 6], b
        assert sum(source(D, 1 << b).values()) == -1 if b <= 14 else True
    for eta in table.values():
        for T in range(1, 8):
            corr = -1 + sum(c*min(T - 1, CORE_TAU[x]) for x, c in eta.items())
            assert -12 <= corr <= 1


def check_lemma2(nmax):
    getcontext().prec = 50
    worst = Decimal(0)
    for N in range(16, nmax + 1):
        n0, n1, n2 = cutoffs(D, N)
        assert 4*n0 <= N and 32*n1 <= 49*N and 64*n2 <= 49*N
        p = lambda n: Decimal(n) ** Decimal("1.5")
        ratio = (p(n0) + p(n1)/3 + p(n2)/3) / p(N)
        assert ratio < Decimal(505)/512
        worst = max(worst, ratio)
    # 1/8 + 343/(384 sqrt 2) + 343/1536 < 1/8 + 245/384 + 343/1536 = 505/512
    assert 7*7 < 2*5*5 and 192 + 980 + 343 == 1515 and 1515*512 == 505*1536
    return str(worst)[:12]


def check_partition_nonvacuous(nmax, targets):
    """For f = 1[z in orbit], f(x) = f(Sx) + 1[x = z], so the partition gives
    B_f(N) = B_f(n0) - 1[z<=n0] + B_f,5mod6(n1) + B_f,1mod6(n2) + 1[z<=N]."""
    for z in targets:
        top = 3*cutoffs(D, nmax)[1]
        f = [0]*(top + 1)
        for x in range(3, top + 1, 2):
            y = x
            while y != 1 and y != z:
                y = step(D, y)
            f[x] = int(y == z)
        pre = lambda u, r=None: sum(f[x] for x in range(1, u + 1, 2) if r is None or x % 6 == r)
        prefix = {None: [0]*(top + 1), 5: [0]*(top + 1), 1: [0]*(top + 1)}
        for r, arr in prefix.items():
            for x in range(1, top + 1):
                arr[x] = arr[x - 1] + (f[x] if x % 2 and (r is None or x % 6 == r) else 0)
        nonzero = 0
        for N in range(8, nmax + 1):
            n0, n1, n2 = cutoffs(D, N)
            rhs = (prefix[None][n0] - int(z <= n0) + prefix[5][n1] + prefix[1][n2]
                   + int(z <= N))
            assert prefix[None][N] == rhs, (z, N)
            nonzero += prefix[None][N] > 0
        assert nonzero > 0
    return list(targets)


def check_least_exception(rmax):
    for r in range(3, rmax + 1, 2):
        N = -(-(2*r - 1)//3)
        _, n1, n2 = cutoffs(D, N)
        assert n1 in (r, r + 1) and n2 < r
        # an odd r = 2 mod 3 has the smaller odd predecessor (2r-1)/3
        if r % 3 == 2:
            x = (2*r - 1)//3
            assert x % 2 and 1 <= x < r and step(D, x) == r


def sup_work(N, cache):
    """W(N) = sup_L H_L(Pi_N) and the extinction time of P^j Pi_N.

    For any finite J, zeta <= 0 with Pi = (I-P)J + zeta,
    H_L(Pi) <= ||J^+||_1, so W(N) lower-bounds every certificate's cost."""
    packet, _, _ = packets(D, N)
    work, best, current, j = 0, 0, packet, 0
    J = defaultdict(int)
    while current:
        for y, c in current.items():
            J[y] += c
        work += sum(current.values())          # H_(j+1) - H_j = <1, P^j Pi>
        best = max(best, work)
        current, j = push(D, current), j + 1
    cost = sum(c for c in J.values() if c > 0)  # forward current J = sum_j P^j Pi
    assert best <= cost
    return best, j, cost, max(tau(y) for y in packet)


def forward_aggregate(mu):
    """J = sum_j P^j mu, for a source whose push dies (all atoms terminate)."""
    J, current = defaultdict(int), dict(mu)
    while current:
        for y, c in current.items():
            J[y] += c
        current = push(D, current)
    return {y: c for y, c in J.items() if c}


def check_stored_currents():
    """Uniqueness in practice: the inherited currents are the forward aggregates."""
    data = Path(__file__).resolve().parents[1] / "collatz_packet_currents" / "data"
    rows = {}
    for N in (4096, 262144):
        read = lambda name: {int(r["state"]): int(r["weight"])
                             for r in csv.DictReader((data / f"{name}_{N}.csv").open())}
        J = read("current")
        assert forward_aggregate(read("packets")) == J, N
        rows[N] = len(J)
    return rows


def check_monotonicity(rng):
    """(I-P)K = extra >= 0 on an acyclic finite support forces K >= 0."""
    for N in (32, 100, 513):
        packet, _, _ = packets(D, N)
        J0 = forward_aggregate(packet)
        states = sorted(J0)
        for _ in range(20):
            extra = {rng.choice(states): rng.randrange(1, 4) for _ in range(5)}
            mu = defaultdict(int, packet)
            for y, c in extra.items():
                mu[y] += c
            J1 = forward_aggregate({y: c for y, c in mu.items() if c})
            assert all(J1.get(y, 0) >= J0.get(y, 0) for y in set(J0) | set(J1))


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    report = dict(scope="Independent finite audit of R2-R4 at d=1; universal current "
                  "existence is not tested.")
    report["theorem1_transfer"] = dict(cutoffs=[8, 160], all_T_to_extinction=True,
                                       largest_gap=check_theorem1_transfer(160))
    for N in range(8, 100001):
        check_remainder(N)
    rng = random.Random(20261017)
    sample = [rng.randrange(10**5, 10**18) for _ in range(3000)]
    sample += [(1 << b) + s for b in range(17, 61) for s in (-1, 1, 3)]
    for N in sample:
        check_remainder(N)
    report["theorem1_core_remainder"] = dict(every_N=[8, 100000], sampled_up_to="1e18",
                                             sampled=len(sample))
    check_dyadic(1500)
    report["dyadic_table"] = dict(b=[3, 1500])
    report["lemma2"] = dict(ratio_bounds_N_ge_16="algebraic, rechecked to 2*10^4",
                            max_ratio_16_to_2e4=check_lemma2(20000), constant="505/512")
    report["partition_nonvacuous"] = dict(
        orbit_targets=check_partition_nonvacuous(4000, (27, 31, 41, 47, 91, 103)),
        cutoffs=[8, 4000])
    check_least_exception(10**6)
    report["least_exception"] = dict(odd_r=[3, 10**6], note="r = 2 mod 3 is never a "
                                     "least counterexample, so this route yields -1")
    cache, rows = {}, []
    for N in list(range(8, 257)) + [384, 512, 768, 1024, 1536, 2048]:
        W, ext, cost, tmax = sup_work(N, cache)
        rows.append(dict(N=N, sup_work=W, extinction=ext, max_atom_tau=tmax,
                         forward_current_J_plus=cost))
    assert next(r for r in rows if r["N"] == 32)["sup_work"] >= 57
    report["sup_work_lower_bounds"] = rows
    report["stored_currents_equal_forward_aggregate"] = check_stored_currents()
    check_monotonicity(rng)
    report["certificate_monotonicity_spot_checks"] = dict(N=[32, 100, 513], trials=60)
    report["status"] = "PASS"
    path = Path(__file__).with_name("reduction_audit.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "sup_work_lower_bounds"},
                     indent=2, sort_keys=True))
    for r in rows[::24] + rows[-6:]:
        print(r)
    assert all(r["extinction"] == r["max_atom_tau"] for r in rows)


if __name__ == "__main__":
    main()
