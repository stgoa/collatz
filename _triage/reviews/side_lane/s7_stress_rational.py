# S7 stress test, written by an independent review agent (2026-10-19); usage: python3 s7_stress_rational.py K mmax
# Stress test of the q-independent lemmas of S7 on ALL primitive words (rational cycles = integer 3x+D cycles).
# For each word a (length m, letters 1..K, 2^A > 3^m), the integer cycle for q = D = 2^A - 3^m has
# N_0 = sum_i 3^(m-1-i) 2^(a_0+...+a_(i-1)); states odd, distinct iff primitive.
import itertools, math, sys
from collections import Counter

def lyndon_words(K, m):
    # canonical rotation representatives: words equal to their minimal rotation and primitive
    for w in itertools.product(range(1, K+1), repeat=m):
        rots = [w[i:]+w[:i] for i in range(m)]
        if w == min(rots) and rots.count(w) == 1:
            yield list(w)

def cycle_states(a):
    m = len(a); A = sum(a); D = 2**A - 3**m
    S = 0; N0 = 0
    for i in range(m):
        N0 += 3**(m-1-i) * 2**S
        S += a[i]
    n = [N0]
    for i in range(m-1):
        x = 3*n[-1] + D
        assert x % 2**a[i] == 0 and (x >> a[i]) % 2 == 1
        n.append(x >> a[i])
    assert (3*n[-1]+D) == N0 * 2**a[-1]
    return n, D

stats = Counter()
fails = []
def note(tag, info):
    stats[tag] += 1
    if len(fails) < 30: fails.append((tag, info))

def run(K, mmax):
    for m in range(3, mmax+1):
        for w in lyndon_words(K, m):
            A = sum(w)
            if 2**A <= 3**m: continue
            n, q = cycle_states(w)
            i0 = n.index(min(n)); n = n[i0:]+n[:i0]; a = w[i0:]+w[:i0]
            L = n[0]; j = n.index(max(n)); d = m - j
            assert j != 0
            Xc = sum(x-1 for x in a[:j]); Xd = sum(x-1 for x in a[j:])
            W = set(range(j, m))
            for h in range(1, m):
                M = [i for i in range(m) if a[i] != a[(i+h) % m]]
                if len(M) != 3: continue
                stats['s3'] += 1
                delta = [n[(i+h) % m] - n[i] for i in range(m)]
                ch = [i for i in range(m) if (delta[i] > 0) != (delta[(i+1) % m] > 0)]
                if not set(ch) <= set(M): note('change_at_agreeing', (a, h))
                if len(ch) != 2: note('changes_not_2', (a, h)); continue
                pm = [i for i in ch if delta[i] > 0]; mp = [i for i in ch if delta[i] < 0]
                ea, eb = pm[0], mp[0]
                Wm = set((i - h) % m for i in W)
                if ea not in Wm or eb not in W: note('location', (a, h))
                # runs and witnesses
                Ms = sorted(M); run_end = {}
                for k, e in enumerate(Ms):
                    t = (e - Ms[k-1] - 1) % m
                    run_end[e] = t
                    z = (e+h) % m if delta[e] > 0 else e
                    if not (abs(delta[e]) >= 2*3**t and n[z] > 2*3**t): note('witness', (a, h, e))
                spac = min(t+1 for t in run_end.values())
                # Step 3 conditional lemmas (with actual spacing)
                if spac >= 2*d - 1:
                    stats['W_hyp'] += 1
                    if not (d <= h <= m - d): note('step3_disjoint', (a, h))
                if spac >= d:
                    stats['one_hyp'] += 1
                    if not (len(W & set(M)) == 1 and len(Wm & set(M)) == 1): note('step3_one', (a, h))
                # Step 4 conditional: windows disjoint, inside climb, one mismatch each
                if d <= h <= m - d and len(W & set(M)) == 1 and len(Wm & set(M)) == 1:
                    stats['step4_hyp'] += 1
                    Wp = set((i + h) % m for i in W)
                    if not (Wp <= set(range(j)) and Wm <= set(range(j))): note('climb_containment', (a, h))
                    if sum(a[i]-1 for i in W if i != eb) > Xc: note('step4_sum', (a, h))
                    if (ea + h) % m != eb:
                        stats['step4_unaligned'] += 1
                        if not (a[eb]-1 <= Xc and Xd <= 2*Xc): note('step4_transfer', (a, h))
                    else:
                        stats['step4_aligned'] += 1
                # Step 5 conditional: aligned
                if (ea + h) % m == eb:
                    x = eb; ec = [e for e in M if e not in (ea, eb)][0]
                    fwd = lambda u, v: (v - u) % m
                    if fwd(ea, x) < fwd(ea, ec):     # order 1
                        tau = run_end[ec]; z = (ec + h) % m; t_o = run_end[ea]; tau_o = run_end[x]
                        if not delta[ec] > 0: note('order1_sign', (a, h))
                    else:                             # order 2
                        tau = run_end[ec]; z = ec; t_o = run_end[x]; tau_o = run_end[ea]
                        if not delta[ec] < 0: note('order2_sign', (a, h))
                    if z != (x - (t_o + 1)) % m: note('step5_identity', (a, h))
                    if x >= t_o + 1:
                        stats['step5_nowrap'] += 1
                        if not z <= tau + tau_o + 1: note('step5_pos', (a, h))
                        if not n[z] > 2*3**tau: note('step5_wit', (a, h))
                        # q-version ceiling at z
                        lb = math.log2(L) + sum(math.log2(1.5*(1 + q/(3*n[i]))) for i in range(z))
                        if math.log2(n[z]) > lb + 1e-9: note('step5_ceiling', (a, h))
                    # P redundancy: under the window structure, no wrap should be automatic
                    if d <= h <= m - d and len(W & set(M)) == 1 and len(Wm & set(M)) == 1 and x < t_o + 1:
                        note('P_needed', (a, h))

K = int(sys.argv[1]); mmax = int(sys.argv[2])
run(K, mmax)
print(dict(stats)); print('fails:', fails[:10])
