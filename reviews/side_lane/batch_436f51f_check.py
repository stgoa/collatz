"""Sidekick probe: independent checks of main commit 436f51f (R37, R38, R39), plus
negative controls on R37's exact critical domain.

R37: W = {w = 5 mod 8} u {w = 9 mod 16}. The claim is that w -> nu(3w) is a bijection from W onto
     the complementary canonical roots q != 2 (mod 3), with inverse q/3 (q = 0 mod 3) or
     (2q+1)/3 (q = 1 mod 3). Checked: for every odd q < LIMIT that is canonical, a
     non-selected climber, and not 2 mod 3, the inverse lands in W and maps back to q;
     and for every w in W with nu(3w) < LIMIT, nu(3w) is such a root.
R38: for odd z, Q(z) - P(u) is an elementary coboundary, with u = z if 3z is canonical and
     u = 4z+1 otherwise. Checked as nu(6z+1) = nu(3u) and nu(z) = nu(u).
R39: for v = 19 (mod 32), t = (3v-1)/8 < 3v/8. The finite current for C(v) - C(t) is checked
     by the pairing 18v+3 ~ 18t+3 and v ~ t: each pair meets at a state other than 1
     within 3 steps on each side. The terminal cylinder
     v = 39 (mod 8192) has S^5(18v+3) = S^7(v).
Controls: on W itself, w and 3w lie in different basins for maps 3x-1, 3x+13, 3x+61.
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import Basins, step  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402

LIMIT = 200000


def in_W(w):
    return w % 8 == 5 or w % 16 == 9


def critical(q):
    return q % 2 == 1 and nu(q) == q and q % 4 == 3 and not selected(q) and q % 3 != 2


def iterate(x, k):
    for _ in range(k):
        x = step(1, x)
    return x


def meet_steps(a, b, cap=40):
    """Steps (i, j) to a common state other than 1, within cap steps each; else None."""
    pos, x = {}, a
    for i in range(cap + 1):
        if x == 1:
            break
        pos.setdefault(x, i)
        x = step(1, x)
    x = b
    for j in range(cap + 1):
        if x == 1:
            return None
        if x in pos:
            return pos[x], j
        x = step(1, x)
    return None


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    roots = [q for q in range(3, LIMIT, 2) if critical(q)]
    for q in roots:
        w = q//3 if q % 3 == 0 else (2*q + 1)//3
        assert (q % 3 == 0 or (2*q + 1) % 3 == 0) and in_W(w) and w < q and nu(3*w) == q, q
    hits = [nu(3*w) for w in range(1, LIMIT, 2) if in_W(w) and nu(3*w) < LIMIT]
    assert all(critical(q) for q in hits) and len(hits) == len(set(hits))
    for z in range(1, LIMIT, 2):
        u = z if nu(3*z) == 3*z else 4*z + 1
        assert nu(6*z + 1) == nu(3*u) and nu(z) == nu(u), z
    r39, r39_max = 0, 0
    for v in range(19, LIMIT, 32):
        t = (3*v - 1)//8
        assert (3*v - 1) % 8 == 0 and 8*t < 3*v
        a, b, c, d = 18*v + 3, v, 18*t + 3, t        # signs: +a, -b, -c, +d
        m1, m2 = meet_steps(a, c, cap=3), meet_steps(b, d, cap=3)    # 18v+3 ~ 18t+3, v ~ t
        assert m1 is not None and m2 is not None, v
        r39_max = max(r39_max, *m1, *m2)
        r39 += 1
    for v in (39, 39 + 8192, 39 + 5*8192):
        assert iterate(18*v + 3, 5) == iterate(v, 7)
    controls = {}
    for dd in (-1, 13, 61):
        B = Basins(dd)
        lab = lambda x: "trivial" if B(x) in B.trivial() else B(x)
        bad = [(w, lab(w), lab(3*w)) for w in range(1, 4000, 2) if in_W(w) and lab(w) != lab(3*w)]
        assert bad
        controls[str(dd)] = dict(count_below_4000=len(bad), first=bad[:3])
    report = dict(scope="Independent finite checks of main 436f51f (R37-R39) and controls on W.",
                  r37_roots_checked=len(roots), r37_images_checked=len(hits),
                  r38_z_checked=LIMIT//2, r39_v_checked=r39, r39_max_meet_steps=r39_max, controls_on_W=controls, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
