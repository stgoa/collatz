"""S7: no rotation with exactly three mismatches at q = 1 (for m >= m0), and controls on actual 3x+q cycles.

Part 1 (threshold). For a primitive q = 1 cycle of period m with minimum L, put ell = log2 L,
eps = log2(1 + 1/(3L)), kappa = log2(3/2) + eps. The S7 argument needs four inequalities:
  W: sigma_min >= 2 d_max - 1       (the two windows are disjoint and hold one mismatch each)
  A: ceil(m log2 3) - m >= 3 X*  (alignment e_a + h = e_b, by excess transfer)
  P: m - d_max >= t_max + 1      (the witness position does not wrap past the minimum)
  F: m - 3 > 2 t_max + tau_max   (the final count)
with t_max = ceil(T) - 1, T = (ell + (m-1) kappa - 1)/log2 3; t* = ceil((m-3)/3);
X* = (m-1) kappa - 1 - t* log2 3 + ell; d* = m - (1 + t* log2 3 - ell)/kappa, d_max = ceil(d*) - 1;
sigma_min = m - 2 (t_max + 1) (the minimum mismatch spacing); tau_max = ceil((ell + (t_max + 1) kappa - 1)/(1 - eps)) - 1.
Every condition gets harder as ell or eps grows, so we use the worst case ell = log2(2^172 m^342 / 3)
(L <= m 2^A/(3D) and gap_all) and eps at L = 2^71 (Barina). Floats: values stay below 1e8, so
rounding errors are below 1e-7; a safety slack of 1e-6 is added on the unfavourable side.

Part 2 (controls). Actual 3x+q cycles, odd q < 400 with 3 not dividing q: every rotation with
exactly three (and two) mismatches is checked for the exact, q-independent claims:
  (a) the sign changes of delta_i = n_(i+h) - n_i: one +-> - change in [j-h, m-h), one - -> + in [j, m),
      and with s = 3 exactly two changes in total;
  (b) every run end e satisfies |delta_e| >= 2*3^t and the signed witness n_z > 2*3^t;
  (c) the q-version ceiling n_z <= L*prod_(i<pos z) (3/2)(1 + q/(3 n_i)) (with the actual states);
  (d) whether alignment e_a + h = e_b holds and, when it does, the witness identity
      pos(z_c) = pos(x) - (t_o + 1) for the third run;
and reports where the asymptotic inputs fail (ell = log2 L is not small against m at q > 1).
"""
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from s1a_integer_cycle_check import cycles, step  # noqa: E402

LOG2_3 = math.log2(3)
SLACK = 1e-6


def conditions(m, ell, eps):
    kappa = math.log2(1.5) + eps
    T = (ell + (m - 1) * kappa - 1) / LOG2_3
    t_max = math.ceil(T + SLACK) - 1
    t_star = -(-(m - 3) // 3)
    X_star = (m - 1) * kappa - 1 - t_star * LOG2_3 + ell + SLACK
    d_star = m - (1 + t_star * LOG2_3 - ell) / kappa
    d_max = math.ceil(d_star + SLACK) - 1
    sigma_min = m - 2 * (t_max + 1)
    tau_max = math.ceil((ell + (t_max + 1) * kappa - 1) / (1 - eps) + SLACK) - 1
    A_minus_m = math.ceil(m * LOG2_3) - m
    return {
        "W": sigma_min - (2 * d_max - 1),
        "A": A_minus_m - 3 * X_star,
        "P": (m - d_max) - (t_max + 1),
        "F": (m - 3) - (2 * t_max + tau_max) - 1,  # >= 0 means strict inequality holds
        "t_max": t_max, "d_max": d_max, "sigma_min": sigma_min, "X_star": X_star, "tau_max": tau_max,
    }


def worst_ell(m):
    return 172 + 342 * math.log2(m) - LOG2_3


EPS71 = math.log2(1 + 1 / (3 * 2**71))


def threshold(m_hi=10_000_000):
    last_fail = None
    for m in range(4, m_hi + 1):
        r = conditions(m, worst_ell(m), EPS71)
        if min(r["W"], r["A"], r["P"], r["F"]) < 0:
            last_fail = m
    return last_fail


def part1():
    m_hi = 10_000_000
    last_fail = threshold(m_hi)
    m0 = last_fail + 1
    r0 = conditions(m0, worst_ell(m0), EPS71)
    samples = {}
    for m in [m0, 10**6, 17_087_915, 114_208_327_604, 137_500_000_000]:
        r = conditions(m, worst_ell(m), EPS71)
        samples[str(m)] = {k: (round(v, 3) if isinstance(v, float) else v) for k, v in r.items()}
    # which condition binds just below m0
    rb = conditions(last_fail, worst_ell(last_fail), EPS71)
    binding = [k for k in "WAPF" if rb[k] < 0]
    return {"m0": m0, "scan_to": m_hi, "binding_below_m0": binding, "at_m0": r0, "samples": samples}


def mismatches(a, h):
    m = len(a)
    return [i for i in range(m) if a[i] != a[(i + h) % m]]


def analyse_rotation(n, a, q, h):
    """n rotated so that n[0] = L is the minimum."""
    m = len(n)
    M = mismatches(a, h)
    s = len(M)
    delta = [n[(i + h) % m] - n[i] for i in range(m)]
    L = n[0]
    j = max(range(m), key=lambda i: n[i])
    out = {"s": s, "h": h, "m": m}
    # (a) sign changes, only at mismatches
    changes = [i for i in range(m) if (delta[i] > 0) != (delta[(i + 1) % m] > 0)]
    assert set(changes) <= set(M), "sign change at an agreeing position"
    win_b = [(j + k) % m for k in range(m - j)]
    win_a = [(j - h + k) % m for k in range(m - j)]
    pm = [i for i in changes if delta[i] > 0]
    mp = [i for i in changes if delta[i] < 0]
    out["a_ok"] = bool(set(pm) & set(win_a)) and bool(set(mp) & set(win_b))
    out["changes"] = len(changes)
    # (b), (c): run ends and witnesses
    Ms = sorted(M)
    runs = []
    for k, e in enumerate(Ms):
        prev = Ms[k - 1]
        t = (e - prev - 1) % m if s > 1 else m - 1
        z = (e + h) % m if delta[e] > 0 else e
        ok_b = abs(delta[e]) >= 2 * 3**t and n[z] > 2 * 3**t
        # q-version ceiling along the actual states from the minimum to z
        log_bound = math.log2(L) + sum(math.log2(1.5 * (1 + q / (3 * n[i]))) for i in range(z))
        ok_c = math.log2(n[z]) <= log_bound + 1e-9
        runs.append({"end": e, "t": t, "z": z, "pos_z": z, "b": ok_b, "c": ok_c})
    out["b_ok"] = all(r["b"] for r in runs)
    out["c_ok"] = all(r["c"] for r in runs)
    # (d) alignment and the witness identity at s = 3
    if s == 3 and len(changes) == 2 and pm and mp:
        e_a, e_b = pm[0], mp[0]
        out["aligned"] = (e_a + h) % m == e_b
        if out["aligned"]:
            x = e_b
            e_c = [e for e in Ms if e not in (e_a, e_b)][0]
            run_len = {r["end"]: r["t"] for r in runs}
            # forward order from x - h
            fwd = lambda u, v: (v - u) % m
            if fwd(e_a, x) < fwd(e_a, e_c):          # order 1: x-h, x, e_c
                z_c, t_o = (e_c + h) % m, run_len[e_a]   # t'' = run ending at x - h
            else:                                      # order 2: x-h, e_c, x
                z_c, t_o = e_c, run_len[x]               # t2 = run ending at x
            out["order"] = 1 if fwd(e_a, x) < fwd(e_a, e_c) else 2
            out["witness_identity"] = z_c == (x - (t_o + 1)) % m and x >= t_o + 1
    return out


def part2(q_max=400, N=3001):
    stats = {"cycles": 0, "rotations_s2": 0, "rotations_s3": 0, "a_fail": 0, "b_fail": 0, "c_fail": 0,
             "s3_changes_not_2": 0, "s3_aligned": 0, "s3_identity_fail": 0, "examples_s3": []}
    for q in range(1, q_max, 2):
        if q % 3 == 0:
            continue
        for cyc in cycles(q, N):
            i0 = cyc.index(min(cyc))
            n = cyc[i0:] + cyc[:i0]
            m = len(n)
            if m < 3:
                continue
            a = [step(x, q)[1] for x in n]
            stats["cycles"] += 1
            for h in range(1, m):
                s = len(mismatches(a, h))
                if s not in (2, 3):
                    continue
                r = analyse_rotation(n, a, q, h)
                stats["rotations_s%d" % s] += 1
                stats["a_fail"] += not r["a_ok"]
                stats["b_fail"] += not r["b_ok"]
                stats["c_fail"] += not r["c_ok"]
                if s == 3:
                    stats["s3_changes_not_2"] += r["changes"] != 2
                    if r.get("aligned"):
                        stats["s3_aligned"] += 1
                        stats["s3_identity_fail"] += not r["witness_identity"]
                    if len(stats["examples_s3"]) < 12:
                        A = sum(a)
                        stats["examples_s3"].append({
                            "q": q, "m": m, "h": h, "L": n[0], "H": max(n),
                            "log2L_over_m": round(math.log2(n[0]) / m, 3),
                            "aligned": r.get("aligned"), "order": r.get("order"),
                            "conds_at_actual_c": {k: round(v, 2) for k, v in conditions(
                                m, math.log2(n[0]), math.log2(1 + q / (3 * n[0]))).items()
                                if k in "WAPF"},
                        })
    return stats


def main():
    p1 = part1()
    print("Part 1: m0 =", p1["m0"], "(scan to", p1["scan_to"], "); binding just below:", p1["binding_below_m0"])
    for m, r in p1["samples"].items():
        print("  m =", m, {k: r[k] for k in ("W", "A", "P", "F", "t_max", "d_max", "sigma_min")})
    p2 = part2()
    print("Part 2:", {k: v for k, v in p2.items() if k != "examples_s3"})
    for ex in p2["examples_s3"]:
        print("  s=3 example:", ex)
    ok = (p2["a_fail"] == 0 and p2["b_fail"] == 0 and p2["c_fail"] == 0
          and p2["s3_changes_not_2"] == 0 and p2["s3_identity_fail"] == 0)
    out = {"part1": p1, "part2": p2, "exact_claims_ok": ok}
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=1, default=str))
    print("exact claims ok:", ok)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
