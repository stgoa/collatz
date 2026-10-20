"""Sidekick probe: independent checks of main's in-progress R93 (two-source history interface),
R94 (the prescribed child Q(floor(ell/3)) needs unbounded clocks) and the later-target ray probe,
first read from main's working copy on 61fd041 and committed unchanged as 9190ccf. This branch's own integer and
rational Syracuse code and normal form; nothing is imported from main.

R93
 (a) cell identities v=144z-43, Q=(2^31 z-665034679)/3^15, Y(z)=864z-257=6v+1, and the ordinary
     words Q->Y(z) (18 arrows, cost 26) and b=Q/3->z (16 arrows, cost 31) as affine identities in
     ell, plus direct iteration at sample ell;
 (b) Phi(144z-43)=144Psi(z)-43, 7153v+299947=144C(z), C(Psi z)=(A/M)C(z); the return word has
     constant 1792529 and fixes Y*=-1792529/7153; on actual cells it holds from Y(z) iff n>=15 and
     Psi(z) is an odd integer back in the guard n>=14 iff n>=33 (n=v2(7153z-53));
 (c) the rational orbit of 53/7153: 448 states, preperiod 71 (cost 146), cycle 377 (cost 739),
     entry 7817, max 819533<115*7153, every prefix 3^i<=2^E_i, 3^377<2^739;
 (d) every exact order n=14..N_MAX on the actual cell (least ell): forced prefix with formula (8),
     x_k<z+115, the short/long departure formulas, and S^t(x_i)<Q for t<=12; long branches with
     prescribed j via the stated congruence; phase shift i(n+739)=i(n)+377 for n>146; joint upper
     cases S^(18+12r)(Q)=Y(Psi^r z) with h=v2(7153 v_r+299947) and n=19r+h-4.
R94
 centers q*, ell*, j*_c, p*_c; the 18-prefix and 12-cycle at q* (all negative); the 112-arrow
 word from p*_2 to 1663/7153 (negative states, disjoint from the upper states); complete cylinders
 for c in {0,1,2}, caps K and return bounds R built here by affine-root exclusion, with
 brute-force replay (all clock pairs a,b<=K distinct; actual words equal the shadow words;
 v2(7153 v0+299947)>=19R+18) and the first actual meeting clocks of the least member;
 NEXT_TARGET's remark that p=q*+gamma^s(q-q*) is never an integer (exact ternary orders).
Later-target probe
 S^78(Q)=y (r=4, cost 122) and S^126(Q)=y (r=8, cost 198); canonical targets and high request
 ranks; ray cutoffs J and L from (4); every ray base a_L checked by T(a_L)=target; all maximal
 point endpoints exceed Q; the r=8 (L,h) table and min(p-Q).
Standard library. Run without -O.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import random

HERE = Path(__file__).resolve().parent


def v2(n):
    n = abs(n)
    return (n & -n).bit_length() - 1


def S_int(x):
    y = 3*x + 1
    e = v2(y)
    return y >> e, e


def S_rat(x):
    y = 3*x + 1
    e = v2(y.numerator)
    return y / (1 << e), e


def selected(x):
    if x % 4 != 3:
        return False
    a = v2(x + 1)
    return ((x + 1) >> a) % 4 == pow(3, a, 4)


def nu(x):
    while True:
        if x % 8 == 5:
            x = (x - 1)//4
        elif x > 1 and selected(x):
            x = (x - 1)//2
        else:
            return x


def T(x):
    return nu(S_int(x)[0])


def word_affine(w):
    """S along word w is x -> (3^k x + c) / 2^E."""
    c = E = 0
    for e in w:
        c = 3*c + (1 << E)
        E += e
    return len(w), c, E


Q0, QP = 70506316836123, 3 * 2**45
V0, VP = 67839005952677, 2**18 * 3**18
Z0, ZP = 471104208005, 2**14 * 3**16
WQ = (1, 2, 1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 3, 1, 2)
WB = (2, 1, 1, 2, 2, 1, 1, 2, 2, 1, 3, 2, 1, 5, 2, 3)
WR = (1, 1, 1, 1, 3, 1, 4, 1, 2, 1, 1, 2)
A, M = 3**12, 2**19
D, B = A - M, 299947
N_MAX = 1000


def Psi(z):
    return F(A*z - 53, M)


def C(z):
    return D*z - 53


def walk(x, steps):
    vals = []
    for _ in range(steps):
        x, e = S_int(x)
        vals.append(e)
    return x, vals


# ----------------------------------------------------------------------------- R93 (a), (b)
def r93_identities():
    assert D == 7153 and Q0 % 3 == 0 and QP % 3 == 0
    assert V0 == 144*Z0 - 43 and VP == 144*ZP
    assert 3**15 * Q0 == 2**31 * Z0 - 665034679 and 3**15 * QP == 2**31 * ZP
    k, c, E = word_affine(WQ)
    assert (k, E) == (18, 26)
    assert 3**18 * Q0 + c == (864*Z0 - 257) << E and 3**18 * QP == (864*ZP) << E
    k, c, E = word_affine(WB)
    assert (k, E) == (16, 31)
    assert 3**16 * (Q0//3) + c == Z0 << E and 3**16 * (QP//3) == ZP << E
    assert v2(QP) == 45 >= 26 + 1 and v2(QP//3) == 45 >= 31 + 1
    rng = random.Random(93)
    ells = [0, 1, 2, 3, 7] + [rng.randrange(1, 2**200) for _ in range(20)]
    for ell in ells:
        Q, z = Q0 + QP*ell, Z0 + ZP*ell
        y, vals = walk(Q, 18)
        assert tuple(vals) == WQ and y == 864*z - 257 == 6*(V0 + VP*ell) + 1
        y, vals = walk(Q//3, 16)
        assert tuple(vals) == WB and y == z
    assert (Q0//3) % 16 == 9 and (QP//3) % 16 == 0
    for z in (F(0), F(1), F(12345, 7)):
        assert F(A*(144*z - 43) + B, M) == 144*Psi(z) - 43
        assert D*(144*z - 43) + B == 144*C(z)
        assert C(Psi(z)) == F(A, M)*C(z)
    k, c, E = word_affine(WR)
    assert (k, E, c) == (12, 19, 1792529)
    for z in (F(0), F(1)):
        assert F(3**12*(864*z - 257) + c, M) == 864*Psi(z) - 257
    ystar = F(-1792529, D)
    assert 864*F(53, D) - 257 == ystar == 6*F(-B, D) + 1
    x, vals = ystar, []
    for _ in range(12):
        x, e = S_rat(x)
        vals.append(e)
    assert tuple(vals) == WR and x == ystar
    # no fixed word z -> Psi(z): forward intercept c/2^E > 0, Psi intercept -53/M < 0
    return len(ells)


# ----------------------------------------------------------------------------- R93 (c)
def lower_shadow():
    N, seen, orbit, vals = 53, {}, [], []
    while N not in seen:
        seen[N] = len(orbit)
        orbit.append(N)
        y = 3*N + D
        e = v2(y)
        vals.append(e)
        N = y >> e
    mu = seen[N]
    lam = len(orbit) - mu
    pre, cyc = sum(vals[:mu]), sum(vals[mu:])
    assert (len(orbit), mu, lam, pre, cyc, orbit[mu], max(orbit)) == (448, 71, 377, 146, 739, 7817, 819533)
    assert max(orbit) < 115*D and all(N > 0 and N % 2 == 1 for N in orbit)
    Epref = [0]
    for e in vals:
        Epref.append(Epref[-1] + e)
    for i in range(len(orbit) + 1):
        assert 3**i <= 2**Epref[i]
    assert 3**lam < 2**cyc
    assert (2**cyc - 3**lam) % D == 0      # 7817/7153 is a genuine rational 3x+1 cycle point
    return orbit, vals, Epref, mu, lam, cyc


# ----------------------------------------------------------------------------- R93 (d)
def r93_departures(sh):
    orbit, vals, Epref, mu, lam, cyc = sh

    def state(i):
        if i < len(orbit):
            return orbit[i], Epref[i]
        k, r = divmod(i - mu, lam)
        return orbit[mu + r], Epref[mu + r] + k*cyc

    def val(i):
        return vals[i] if i < len(orbit) else vals[mu + (i - mu) % lam]

    def dep_index(n):
        i = 0
        while True:
            Ni, Ei = state(i)
            if Ei < n <= Ei + val(i):
                return i
            i += 1

    c0 = C(Z0)
    m = D*ZP
    assert v2(c0) >= 14 and v2(m) == 14
    c0p, mp = c0 >> 14, m >> 14

    def ell_for(n, tau=None, jj=0):
        mod = 1 << (n - 13 + jj)
        target = (1 << (n - 14)) * (1 if tau is None else tau)
        return ((target - c0p) * pow(mp, -1, mod)) % mod

    # 2^43 - 3^27 slope and the value at the least z for (3/2)^12 (z+116) - 1 < Q
    assert 2**43 - 3**27 == 1170495537221
    gap = (2**43 - 3**27)*Z0 - 2**12*665034679 - 116*3**27 + 3**15*2**12
    assert gap == 551425372148651686473501

    def check(ell, n_expect=None, j_expect=None):
        Q, z = Q0 + QP*ell, Z0 + ZP*ell
        Cz = C(z)
        n = v2(Cz)
        t = Cz >> n
        assert t % 2 == 1 and n >= 14 and (n_expect is None or n == n_expect)
        i = dep_index(n)
        x = z
        for k in range(i):
            Nk, Ek = state(k)
            assert D*x == 3**k * (t << (n - Ek)) + Nk and x < z + 115
            x, e = S_int(x)
            assert e == val(k)
        Ni, Ei = state(i)
        assert D*x == 3**i * (t << (n - Ei)) + Ni and x < z + 115
        xi, e, a = x, val(i), n - Ei
        Nn = (3*Ni + D) >> e
        y, ea = S_int(xi)
        if a < e:
            kind = "short"
            assert ea == a and D*y == 3**(i + 1)*t + (Nn << (e - a))
        else:
            assert a == e
            jj = v2(3**(i + 1)*t + Nn)
            assert jj >= 1 and ea == e + jj and (D*y) << jj == 3**(i + 1)*t + Nn
            assert j_expect is None or jj == j_expect
            kind = "long"
        x = xi
        for tt in range(13):
            assert x < Q and (x + 1) << tt <= 3**tt * (xi + 1)
            x, _ = S_int(x)
        return n, i, kind

    kinds = {"short": 0, "long": 0}
    dep = {}
    for n in range(14, N_MAX + 1):
        nn, i, kind = check(ell_for(n), n_expect=n)
        kinds[kind] += 1
        dep[n] = (i, kind)
    long_cases = 0
    for n in range(14, 401):
        i = dep_index(n)
        Ni, Ei = state(i)
        e = val(i)
        if n - Ei != e:
            continue
        Nn = (3*Ni + D) >> e
        for jj in range(1, 9):
            tau = ((1 << jj) - Nn) * pow(3, -(i + 1), 1 << (jj + 1)) % (1 << (jj + 1))
            assert tau % 2 == 1
            check(ell_for(n, tau, jj), n_expect=n, j_expect=jj)
            long_cases += 1
    phase = 0
    for n in range(147, 147 + 2*cyc):
        i, j = dep_index(n), dep_index(n + cyc)
        Ni, Ei = state(i)
        Nj, Ej = state(j)
        assert j == i + lam and Ej - Ei == cyc and val(i) == val(j) and Nj == Ni
        phase += 1
    assert dep_index(146) < mu <= dep_index(147)
    # joint upper/lower cases: n = 19r + h - 4
    joint = 0
    for r in (0, 1, 2, 3, 4, 5, 8, 16, 32, 64, 128):
        for h in range(18, 37):
            n = 19*r + h - 4
            ell = ell_for(n)
            Q, z = Q0 + QP*ell, Z0 + ZP*ell
            zs = [z]
            for _ in range(r):
                nz = Psi(zs[-1])
                assert nz.denominator == 1 and nz.numerator % 2 == 1 and v2(C(nz.numerator)) >= 14
                zs.append(nz.numerator)
            nz = Psi(zs[-1])
            assert not (nz.denominator == 1 and nz.numerator % 2 == 1 and v2(C(nz.numerator)) >= 14)
            y, vals_up = walk(Q, 18 + 12*r)
            assert tuple(vals_up) == WQ + WR*r and y == 864*zs[-1] - 257
            assert v2(D*(144*zs[-1] - 43) + B) == h and r == (n - 14)//19 and h == 18 + (n - 14) % 19
            check(ell, n_expect=n)
            joint += 1
    # guard controls on actual cells: WR holds from Y(z) iff n >= 15; re-entry iff n >= 33
    controls = 0
    for n in range(14, 81):
        z = Z0 + ZP*ell_for(n)
        _, vals_up = walk(864*z - 257, 12)
        assert (tuple(vals_up) == WR) == (n >= 15)
        nz = Psi(z)
        assert (nz.denominator == 1 and nz.numerator % 2 == 1 and v2(C(nz.numerator)) >= 14) == (n >= 33)
        controls += 1
    return {"exact_orders": [14, N_MAX], "short": kinds["short"], "long": kinds["long"],
            "prescribed_long_j_cases": long_cases, "phase_checks": phase, "joint_cases": joint,
            "guard_controls": controls, "gap_at_least_z": gap}


# ----------------------------------------------------------------------------- R94
def r94():
    vstar = F(-B, D)
    qstar = (2**27 * vstar - 213949807) / 3**17
    assert qstar == F(-515908491727, 11404192419) and 11404192419 == D * 3**13
    for ell in (0, 1):
        assert Q0 + QP*ell == (2**27 * (V0 + VP*ell) - 213949807) / F(3**17)
    lstar = (qstar - Q0) / QP
    assert lstar == F(-22852975802, 34212577257) and lstar.denominator % 2 == 1
    assert v2(lstar.numerator) == 1 and v2((qstar - Q0).numerator) == 46
    assert V0 + VP*lstar == vstar
    table = {0: F(1608135207907736055411347, 34212577257),
             1: F(404387159579536788517523, 34212577257),
             2: F(-799360888748662478376301, 34212577257)}
    centers = {}
    for c in range(3):
        js = (lstar - c) / 3
        ps = Q0 + QP*js
        assert js < 0 and js.denominator % 2 == 1 and ps == table[c]
        assert Q0 + QP*(c + 3*js) == qstar
        for j in (0, 1):  # (7): D v0 + B = D 2^18 3^19 (j - j*_c) on ell = c + 3j
            assert D*(V0 + VP*(c + 3*j)) + B == D * 2**18 * 3**19 * (j - js)
        centers[c] = (js, ps)
    x, up, vals = qstar, [qstar], []
    for _ in range(18):
        x, e = S_rat(x)
        vals.append(e)
        up.append(x)
    assert tuple(vals) == WQ and x == F(-1792529, D)
    vals = []
    for _ in range(12):
        x, e = S_rat(x)
        vals.append(e)
        up.append(x)
    assert tuple(vals) == WR and x == F(-1792529, D) and all(s < 0 for s in up)
    upset = set(up)
    x, child = centers[2][1], [centers[2][1]]
    for _ in range(112):
        x, _ = S_rat(x)
        child.append(x)
    assert x == F(1663, D) and all(s < 0 for s in child[:112]) and child[112] > 0
    assert not set(child[:112]) & upset
    maxbits = max(abs(s.numerator).bit_length() for s in child)
    assert maxbits <= 80
    assert centers[0][1] > 0 and centers[1][1] > 0

    def shadow_word(x0, K):
        x, w = x0, []
        for _ in range(K):
            x, e = S_rat(x)
            w.append(e)
        return w

    def prefix_affines(w, s0, s1):
        """Endpoints after a=0..K arrows of word w from the source s0 + s1*j, as (slope, const)."""
        out, c, E = [], 0, 0
        out.append((F(s1), F(s0)))
        for k, e in enumerate(w, 1):
            c = 3*c + (1 << E)
            E += e
            out.append((F(3**k * s1, 1 << E), F(3**k * s0 + c, 1 << E)))
        return out, E

    rng = random.Random(94)
    cylinders = []
    plan = [(c, K, 0) for c in range(3) for K in (0, 1, 2, 4, 8, 16, 32, 64, 128)]
    plan += [(c, 16, R) for c in range(3) for R in (1, 4, 16, 128)]
    replays = 0
    for c, K, R in plan:
        js, ps = centers[c]
        wp, wc = shadow_word(qstar, K), shadow_word(ps, K)
        fp, Ep = prefix_affines(wp, Q0 + QP*c, 3*QP)
        fc, Ec = prefix_affines(wc, Q0, QP)
        roots = set()
        for al, be in fp:
            for ga, de in fc:
                if al == ga:
                    assert be != de
                    continue
                t = (de - be) / (al - ga)
                if t.denominator == 1 and t >= 0:
                    roots.add(t.numerator)
        N = max(0, max(Ep, Ec) + 1 - 45, 19*R)
        for t in roots:
            N = max(N, v2((t - js).numerator) + 1)
        mod = 1 << N
        rho = js.numerator * pow(js.denominator, -1, mod) % mod if N else 0
        members = [rho + mod*s for s in range(0, 3) if rho + mod*s > 0][:2]
        members += [rho + mod*rng.randrange(1, 2**64) for _ in range(2)]
        first_meet = None
        for j in members:
            ell = c + 3*j
            P, Ch = Q0 + QP*ell, Q0 + QP*j
            assert Ch < P and v2(D*(V0 + VP*ell) + B) >= 19*R + 18
            po, co = [P], [Ch]
            pw, cw = [], []
            for _ in range(K):
                x, e = S_int(po[-1])
                po.append(x)
                pw.append(e)
                x, e = S_int(co[-1])
                co.append(x)
                cw.append(e)
            assert pw == wp and cw == wc and not set(po) & set(co)
            replays += 1
            if first_meet is None:  # least member: first common state of the full trajectories
                cidx, x, b = {}, Ch, 0
                while x not in cidx:
                    cidx[x] = b
                    x, _ = S_int(x)
                    b += 1
                x, a = P, 0
                while x not in cidx:
                    x, _ = S_int(x)
                    a += 1
                first_meet = (a, cidx[x])
                assert max(first_meet) > K
        cylinders.append({"c": c, "K": K, "R": R, "N": N, "roots": len(roots),
                          "first_meeting_clocks_least_member": list(first_meet)})
    # NEXT_TARGET remark: p = q* + gamma^s (q - q*) has v3(p) = -13 (s > 0) or 12s - 13 (s < 0)
    def v3(x):
        x, k = F(x), 0
        n, d = x.numerator, x.denominator
        while n % 3 == 0:
            n //= 3
            k += 1
        while d % 3 == 0:
            d //= 3
            k -= 1
        return k
    gamma = F(A, M)
    scal = 0
    for s in [k for k in range(-12, 13) if k]:
        for q in [0, 1, -1, 3**30, -7*3**25] + [rng.randrange(-2**80, 2**80) for _ in range(30)]:
            pq = qstar + gamma**s * (q - qstar)
            assert pq.denominator != 1 and v3(pq) == (-13 if s > 0 else 12*s - 13)
            scal += 1
    return {"q_star": str(qstar), "ell_star": str(lstar), "child_word_max_bits": maxbits,
            "cycle_scaling_nonintegral_cases": scal,
            "cylinders": len(cylinders), "replayed_pairs": replays, "detail": cylinders}


# ----------------------------------------------------------------------------- later-target probe
def bases(y):
    r = y % 3
    if r == 0:
        return [(8*y + 3)//3, (16*y + 3)//3]
    if r == 1:
        return [(4*y - 1)//3, (32*y + 19)//3]
    return [(64*y + 19)//3, (128*y + 83)//3]


def ray_endpoints(Q, y):
    J = (Q - 1).bit_length() - 2
    Pmax = 3**J * (Q - 1) // 2**J
    out = []
    for ray, a0 in enumerate(bases(y)):
        assert nu(a0) == a0 and a0 % 8 == 1 and T(a0) == y
        cap = (9*Pmax - 2) // (9*a0 + 7)
        L, aL = 0, a0
        while 64**L <= cap:
            assert 9*aL + 7 == 64**L * (9*a0 + 7) and T(aL) == y
            h, u = 0, aL + 1
            while u % 3 == 0:
                u //= 3
                h += 1
            p = (2**h * (aL + 1)) // 3**h - 1
            x = p
            for _ in range(h):
                x, e = S_int(x)
                assert e == 1
            assert x == aL
            if h >= 1:
                assert p % 4 == 3 and p % 3 != 2
            out.append((ray, L, h, p))
            L, aL = L + 1, 64*aL + 49
    return J, out


def later_target():
    res = {}
    Q4 = 10700808724915244204246595675625106715
    y4 = 33053313160223488220607297455181106259
    y, vals = walk(Q4, 78)
    assert y == y4 and sum(vals) == 122
    z4 = nu(y4)
    assert z4 == 16526656580111744110303648727590553129 > Q4 and z4 % 8 == 1 and z4 % 3 == 2
    w4 = 8263328290055872055151824363795276565
    assert w4 % 8 == 5 and nu(3*w4) == 12394992435083808082727736545692914847 > Q4
    p4 = (2*z4 - 1)//3
    assert p4 == 11017771053407829406869099151727035419 > Q4 and T(p4) == z4
    w4b = 3672590351135943135623033050575678473
    assert 3*w4b == p4 and w4b % 16 == 9 and nu(p4) == p4
    J4, eps4 = ray_endpoints(Q4, z4)
    caps4 = [max(L for r_, L, h, p in eps4 if r_ == k) for k in (0, 1)]
    assert caps4 == [11, 10] and len(eps4) == 23 and all(p > Q4 for *_, p in eps4)
    res["r4"] = {"J": J4, "ray_caps": caps4, "endpoints": len(eps4)}
    Q8 = 210065029006409577911756714191833302426696026205209908227355
    y8 = 685003375529270486518611195608212623248313116517585840060299
    y, vals = walk(Q8, 126)
    assert y == y8 and sum(vals) == 198 and nu(y8) == y8 and y8 > Q8
    w8 = 304445944679675771786049420270316721443694718452260373360133
    assert w8 % 8 == 5 and nu(3*w8) == (2*y8 - 1)//3 == 456668917019513657679074130405475082165542077678390560040199
    J8, eps8 = ray_endpoints(Q8, y8)
    caps8 = [max(L for r_, L, h, p in eps8 if r_ == k) for k in (0, 1)]
    assert J8 == 196 and caps8 == [18, 17] and len(eps8) == 37
    assert all(p > Q8 for *_, p in eps8)
    pos = {k: [(L, h) for r_, L, h, p in eps8 if r_ == k and h >= 1] for k in (0, 1)}
    assert pos[0] == [(1, 1), (4, 3), (7, 1), (10, 1), (13, 2), (16, 1)]
    assert pos[1] == [(0, 2), (3, 1), (6, 1), (9, 2), (12, 1), (15, 1)]
    gap = min(p - Q8 for *_, p in eps8)
    assert gap == 12779628610659756684959685217341680145837611961091232688471660
    res["r8"] = {"J": J8, "ray_caps": caps8, "endpoints": len(eps8), "min_p_minus_Q": str(gap)}
    return res


def main():
    out = {"probe": "r93_r94_check", "main_base": "61fd041 + uncommitted R93/R94 working copy"}
    out["r93_identity_ells"] = r93_identities()
    sh = lower_shadow()
    out["r93_lower_shadow"] = {"states": len(sh[0]), "preperiod": sh[3], "cycle": sh[4],
                               "cycle_cost": sh[5], "D_divides_2^739-3^377": True}
    out["r93_departures"] = r93_departures(sh)
    out["r94"] = r94()
    out["later_target"] = later_target()
    out["result"] = "PASS"
    (HERE / "r93_r94_check.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps({k: v for k, v in out.items() if k != "r94"}, indent=1))
    print("r94:", {k: v for k, v in out["r94"].items() if k != "detail"})


if __name__ == "__main__":
    main()
