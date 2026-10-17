"""Negative controls for the right-aligned packet criterion.

The maps T_d(x) = (3x+d)/2^v2(3x+d) on odd positive integers, with
d = 2^k - 3, all fix 1 (and every odd d >= 1 also fixes d). d = 1 is the
Syracuse map. For d = -1 (Collatz on negative integers) and d = 61 the
analogous conjecture is false: there are nontrivial cycles.

This script builds the right-aligned packets for T_d by direct enumeration,
independently of right_aligned_packets.py, and checks:

  * the valuation counting identity behind Lemma/Theorem 3, non-vacuously
    (with a nonzero exceptional indicator e);
  * the cutoffs N at which <e, Pi_N> > 0, so that no finite current with
    nonpositive residual exists and packet work grows linearly;
  * a finite obstruction certificate for each recorded control: explicit
    orbits from each atom to 1, to d, or into a listed cycle;
  * that a generic current checker accepts genuine d = 1 certificates and
    rejects the forward-truncation attempt at every horizon on a control.

Usage: python3 affine_controls.py            # run the audit, write the receipt
       python3 affine_controls.py --check C  # check a certificate JSON file C

Finite checks only; nothing here bears on the universal 3x+1 criterion except
as a test of its logic and of tools built for it. Standard library only.
Run without -O.
"""
from collections import defaultdict
from pathlib import Path
import json
import sys

ESCAPE = 1 << 64            # report, never silently truncate, a runaway orbit


def step(d, x):
    z = 3*x + d
    return z // (z & -z)


def valuation(d, x):
    z = 3*x + d
    return (z & -z).bit_length() - 1


class Basins:
    """Memoised terminal-cycle labels (minimum of the cycle) for T_d."""

    def __init__(self, d):
        self.d, self.label, self.cycles = d, {}, {}

    def __call__(self, x):
        label, path, seen, y = self.label, [], set(), x
        while y not in label:
            if y in seen:
                cycle = [y]
                z = step(self.d, y)
                while z != y:
                    cycle.append(z)
                    z = step(self.d, z)
                m = min(cycle)
                self.cycles[m] = cycle[cycle.index(m):] + cycle[:cycle.index(m)]
                for c in cycle:
                    label[c] = m
                break
            seen.add(y)
            path.append(y)
            y = step(self.d, y)
            if y > ESCAPE:
                raise RuntimeError(f"d={self.d}: orbit of {x} exceeded 2^64; unresolved")
        for p in path:
            label[p] = label[y]
        return label[y]

    def trivial(self):
        return absorbing(self.d)

    def e(self, x):
        """Exceptional indicator: the orbit ends in a nontrivial cycle."""
        return int(self(x) not in self.trivial())


def cutoffs(d, N):
    return (N - d)//4, (3*N + d)//2, (3*N + d)//4


def components(d, N):
    """(cutoff, residue mod 3 receiving coefficient +2) for both components."""
    _, n1, n2 = cutoffs(d, N)
    return ((n1, (2*d) % 3), (n2, d % 3))


def coefficient(x, target):
    return 3*int(x % 3 == target) - 1


def source(d, N):
    nu = defaultdict(int)
    for n, target in components(d, N):
        for x in range(3, n + 1, 2):
            nu[x] += coefficient(x, target)
    return {x: c for x, c in nu.items() if c}


def absorbing(d):
    """Trivial fixed points: 1, and d itself when d > 1 (T_d(d) = d)."""
    return {1} | ({d} if d > 1 else set())


def push(d, mu, absorb=frozenset({1})):
    """One-step pushforward discarding mass that lands in absorb.

    The packet identity P nu = Pi + eta discards only at 1. Work and
    currents use absorbing(d), so mass parked at the fixed point d is
    treated like mass at 1; both have e = 0, so pairings are unchanged."""
    out = defaultdict(int)
    for x, c in mu.items():
        y = step(d, x)
        if y not in absorb:
            out[y] += c
    return {y: c for y, c in out.items() if c}


def lift_classes(d, n):
    """Yield (a, q, period, t0, count) for sources 3 <= x <= n of valuation a.

    q is the least positive source of valuation a; lifts are q + period*t.
    t0 = 1 drops the single lift with endpoint 1 (necessarily t = 0)."""
    a = 1
    while True:
        period = 1 << (a + 1)
        q = ((1 << a) - d) * pow(3, -1, period) % period
        if q == 0:
            q = period
        if q > n and (1 << a) > 3*n + abs(d):
            return
        assert valuation(d, q) == a
        t0 = int(q == 1 or step(d, q) == 1)
        last = (n - q)//period if n >= q else -1
        yield a, q, period, t0, max(0, last - t0 + 1)
        a += 1


def packets(d, N, materialize=True):
    """Right-aligned depth-one packets: P nu_N = packet + eta."""
    packet, eta, triples = defaultdict(int), defaultdict(int), 0
    for n, target in components(d, N):
        for a, q, period, t0, count in lift_classes(d, n):
            leftover = count % 3
            y0 = (3*q + d) >> a
            for t in range(t0, t0 + leftover):
                eta[y0 + 6*t] += coefficient(q + period*t, target)
            triples += count//3
            if materialize:
                for t in range(t0 + leftover, t0 + count, 3):
                    total = 0
                    for j in range(3):
                        x, y = q + period*(t + j), y0 + 6*(t + j)
                        assert step(d, x) == y and y != 1 and 3 <= x <= n
                        c = coefficient(x, target)
                        packet[y] += c
                        total += c
                    assert total == 0
    clean = lambda m: {y: c for y, c in m.items() if c}
    return clean(packet), clean(eta), triples


def prefix_tables(basins, top):
    """Exceptional prefix counts by residue mod 3 over odd x <= u."""
    by_res = [[0]*(top + 1) for _ in range(3)]
    for x in range(1, top + 1):
        for r in range(3):
            by_res[r][x] = by_res[r][x - 1]
        if x % 2:
            by_res[x % 3][x] += basins.e(x)
    total = [sum(by_res[r][u] for r in range(3)) for u in range(top + 1)]
    return by_res, total


def identity_check(d, basins, by_res, total, N):
    """B(N) = B(n0) + B_r1(n1) + B_r2(n2) + edge.

    The edge adds sources x = 4z+d with z < 0 (no positive z) and removes
    images y whose valuation-1 or -2 preimage (2y-d)/3, (4y-d)/3 is < 1.
    It is empty for d = +-1."""
    n0, n1, n2 = cutoffs(d, N)
    (_, r1), (_, r2) = components(d, N)
    edge = sum(basins.e(x) for x in range(d - 4, 0, -8) if x <= N)
    edge -= sum(basins.e(y) for y in range(1, min(n1, (d + 3)//2) + 1, 2)
                if y % 3 == r1 and 2*y - d < 3)
    edge -= sum(basins.e(y) for y in range(1, min(n2, (d + 3)//4) + 1, 2)
                if y % 3 == r2 and 4*y - d < 3)
    rhs = (total[n0] if n0 > 0 else 0) + by_res[r1][n1] + by_res[r2][n2] + edge
    return total[N] == rhs


def pairing(d, basins, by_res, total, N):
    """<e, Pi_N> = <e, nu_N> - <e, eta_N>, using only prefix counts."""
    _, eta, _ = packets(d, N, materialize=False)
    nu = sum(3*by_res[r][n] - total[n] for n, r in components(d, N))
    return nu - sum(c*basins.e(y) for y, c in eta.items()), eta


def orbit_certificate(d, basins, y):
    """Explicit path from y to 1, to d, or into a listed cycle."""
    path, trivial, cycles = [y], basins.trivial(), basins.cycles
    while path[-1] not in trivial and not any(path[-1] in c for c in cycles.values()):
        path.append(step(d, path[-1]))
    return path


def check_obstruction(d, packet, cycles, certificates):
    """Re-verify a recorded obstruction using one-step arithmetic only."""
    on_cycle = {}
    for m, cycle in cycles.items():
        for i, c in enumerate(cycle):
            assert step(d, c) == cycle[(i + 1) % len(cycle)]
            on_cycle[c] = m
    trivial = absorbing(d)
    assert not trivial & set(on_cycle)
    pairing = 0
    for y, c in packet.items():
        path = certificates[y]
        assert path[0] == y and all(step(d, u) == v for u, v in zip(path, path[1:]))
        end = path[-1]
        assert end in trivial or end in on_cycle
        pairing += c*int(end in on_cycle)
    return pairing


def check_current(d, target, J, zeta):
    """Generic checker: target = (I-P)J + zeta with zeta <= 0, all finite.

    P absorbs at absorbing(d); target atoms at d (if any) need J(d) = their mass."""
    lhs, absorb = defaultdict(int), absorbing(d)
    for y, c in J.items():
        assert y > 1 and y % 2
        lhs[y] += c
        z = step(d, y)
        if z not in absorb:
            lhs[z] -= c
    for y, c in zeta.items():
        lhs[y] += c
    return (all(c <= 0 for c in zeta.values())
            and {y: c for y, c in lhs.items() if c} == target)


def truncation_attempt(d, mu, K):
    """J = sum_{j<K} P^j mu, zeta = P^K mu; exact iff the push dies by K."""
    J, current = defaultdict(int), dict(mu)
    for _ in range(K):
        for y, c in current.items():
            J[y] += c
        current = push(d, current, absorbing(d))
    return {y: c for y, c in J.items() if c}, current


def work_slope(d, mu, horizon):
    """H_L(mu) - H_(L-1)(mu) = <1, P^(L-1) mu> for L = 1..horizon."""
    slopes, current = [], dict(mu)
    for _ in range(horizon):
        slopes.append(sum(current.values()))
        current = push(d, current, absorbing(d))
    return slopes


CONTROLS = {-1: 20000, 61: 20000}          # map -> largest cutoff scanned
SURVEY = (-1, 5, 13, 29, 61, 125, 253, 509)


def check_certificate_file(path):
    """Check {"d", "N", "J", "zeta"} against an independently built Pi_N.

    J and zeta map odd states (JSON string keys) to integers. Exit status 0
    means Pi_N = (I-P)J + zeta with zeta <= 0, P absorbing at absorbing(d)."""
    cert = json.loads(Path(path).read_text())
    d, N = int(cert["d"]), int(cert["N"])
    target, _, _ = packets(d, N)
    target = {y: c for y, c in target.items() if y not in absorbing(d)}
    J = {int(y): int(c) for y, c in cert["J"].items() if int(c)}
    zeta = {int(y): int(c) for y, c in cert.get("zeta", {}).items() if int(c)}
    ok = check_current(d, target, J, zeta)
    print(json.dumps(dict(d=d, N=N, valid=ok, J_positive_cost=sum(c for c in J.values() if c > 0),
                          zeta_mass=sum(zeta.values()))))
    return ok


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    if len(sys.argv) == 3 and sys.argv[1] == "--check":
        sys.exit(0 if check_certificate_file(sys.argv[2]) else 1)
    report = dict(scope="Finite negative controls for maps 3x+d; not evidence "
                  "for or against universal 3x+1 current existence.")

    # 1. Independent agreement with the repository construction at d = 1.
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    import right_aligned_packets as repo
    for N in list(range(8, 3001)) + [4096, 10001, 65537, 262144]:
        mine, eta, _ = packets(1, N, materialize=N <= 3000 or N == 4096)
        theirs, their_eta, _ = repo.right_packets(N, materialize=N <= 3000 or N == 4096)
        assert eta == their_eta and (N > 4096 or mine == theirs), N
        if N <= 600:
            combined = defaultdict(int, mine)
            for y, c in eta.items():
                combined[y] += c
            assert {y: c for y, c in combined.items() if c} == push(1, source(1, N))
    report["d1_agreement"] = "packets and remainders equal the repository construction " \
        "for N=8..3000 and N=4096; remainders also for 10001, 65537, 262144"

    # 2. Survey: which maps look locally like Collatz, and does the criterion fire?
    survey = {}
    for d in SURVEY:
        basins = Basins(d)
        top = 3*cutoffs(d, 3000)[1] + 3*abs(d) + 16
        for x in range(1, top + 1, 2):
            basins(x)
        by_res, total = prefix_tables(basins, top)
        core, failing = set(), []
        for N in range(8, 3001):
            assert identity_check(d, basins, by_res, total, N), (d, N)
            p, eta = pairing(d, basins, by_res, total, N)
            core |= set(eta)
            if p > 0:
                failing.append(N)
        least = next(x for x in range(1, top, 2) if basins.e(x))
        if not any(basins.e(y) for y in core) and least > 15:
            # Locally Collatz-like maps: the least exceptional seed r = d mod 3
            # first enters component 2, with coefficient +2, at this cutoff.
            assert least % 3 == d % 3 and failing[0] == -(-(4*least - d)//3), d
        survey[d] = dict(
            nontrivial_cycles={m: len(c) for m, c in sorted(basins.cycles.items())
                               if m not in basins.trivial()},
            least_exceptional_seed=least,
            exceptional_seeds_below_16=[x for x in range(1, 16, 2) if basins.e(x)],
            core=sorted(core), exceptional_core=[y for y in sorted(core) if basins.e(y)],
            failing_cutoffs_8_3000=len(failing), first_failing_cutoff=failing[0] if failing else None)
    report["survey_N_8_3000"] = survey

    # 3. Controls: full scans, obstruction certificates, linear work, checker traps.
    controls = {}
    for d, nmax in CONTROLS.items():
        basins = Basins(d)
        top = 3*cutoffs(d, nmax)[1] + 3*abs(d) + 16
        by_res, total = prefix_tables(basins, top)
        failing, largest = [], (0, None)
        for N in range(8, nmax + 1):
            assert identity_check(d, basins, by_res, total, N), (d, N)
            p, _ = pairing(d, basins, by_res, total, N)
            if p > 0:
                failing.append(N)
                largest = max(largest, (p, N))
        recorded = []
        for N in sorted({failing[0], failing[len(failing)//2], largest[1]}):
            packet, eta, _ = packets(d, N)
            combined = defaultdict(int, packet)
            for y, c in eta.items():
                combined[y] += c
            assert {y: c for y, c in combined.items() if c} == push(d, source(d, N))
            certs = {y: orbit_certificate(d, basins, y) for y in packet}
            cycles = {m: c for m, c in basins.cycles.items() if m not in basins.trivial()}
            k = check_obstruction(d, packet, cycles, certs)
            assert k == pairing(d, basins, by_res, total, N)[0] > 0
            settle = max(len(path) for path in certs.values()) + 1
            slopes = work_slope(d, packet, settle + 50)
            assert all(s == k for s in slopes[settle:])
            for K in (0, 1, settle, 2*settle):
                J, zeta = truncation_attempt(d, packet, K)
                assert check_current(d, packet, J, {y: c for y, c in zeta.items() if c <= 0}
                                     ) is False
                assert any(c > 0 for c in zeta.values())
            recorded.append(dict(N=N, pairing=k, packet_atoms=len(packet),
                                 work_slope_from_L=settle))
        controls[d] = dict(cutoffs_scanned=[8, nmax], failing=len(failing),
                           first_failing=failing[0], largest_pairing=dict(N=largest[1],
                           value=largest[0]), certified=recorded,
                           nontrivial_cycles={m: c for m, c in sorted(basins.cycles.items())
                                              if m not in basins.trivial()})
    report["controls"] = controls

    # 4. The checker accepts genuine d = 1 certificates (exact currents).
    accepted = []
    for N in (8, 32, 100, 513):
        packet, _, _ = packets(1, N)
        J, zeta = truncation_attempt(1, packet, 200)
        assert not zeta and check_current(1, packet, J, {})
        accepted.append(N)
    report["checker_accepts_exact_d1_currents_at"] = accepted
    report["status"] = "PASS"

    path = Path(__file__).with_name("negative_controls_audit.json")
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
