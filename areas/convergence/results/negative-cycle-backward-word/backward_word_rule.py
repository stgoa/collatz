"""Sidekick probe: a backward-word (smaller-ancestor) rule in main's sigma framework.

If q = nu(3w) has an explicit S-ancestor p < q (a backward word p -> ... -> q), then
    P(w) = div(N_3w - path(p->q) + H_p - N_w - H_z) + requests(H_p) - requests(H_z),
with z = nu(w). R51 bounds every request of H_s by sigma <= nu(s), so all requests have
sigma <= max(p, z) < q = sigma(w) whenever w is not returning. The plan is built from
main's own bridge/absorption code and checked with main's sigma validator.

Checks (main at 8764158, read-only imports):
  1. R54 family q = 81*2^K*s - 17 with 27 | s: the 7-step backward word of the negative
     cycle -17 gives p = (2048q - 2363)/2187; the plan validates under sigma.
  2. Coverage of the rule (best-first search, node budget) on R54 phase members and on
     random selected w by class mod 3, restricted to inputs main's continued dispatcher
     (seven rules + R52 + R53) leaves unresolved. Measurement, not a check.
Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import heapq
import json
import random
import sys

ROOT = Path(__file__).resolve().parents[2]
RP = ROOT / "experiments" / "residual_progress"
sys.path[:0] = [str(RP / "phase_rank"), str(RP / "continued_rules")]
import sigma_rank as SIG  # noqa: E402
import continued_rules as CONT  # noqa: E402

T, NORMAL, RANK = SIG.T, SIG.NORMAL, SIG.RANK
combine, divergence = SIG.combine, SIG.divergence


def smaller_ancestor(q, budget=4000, cap=64):
    """Best-first search of the S-preimage tree of q for some p < q; returns the forward path."""
    heap, seen = [(q, (q,))], {q}
    while heap and budget:
        x, path = heapq.heappop(heap)
        budget -= 1
        if x % 3 == 0:
            continue
        v = 1 if x % 3 == 2 else 2
        while True:
            y = (2**v*x - 1)//3
            if y > cap*q:
                break
            if y not in seen:
                if y < q:
                    return (y,) + path
                seen.add(y)
                heapq.heappush(heap, (y, (y,) + path))
            v += 2
    return None


def plan(w, path):
    p, q = path[0], path[-1]
    assert NORMAL.normal_form(3*w) == q and all(NORMAL.step(a) == b for a, b in zip(path, path[1:]))
    walk = Counter({x: 1 for x in path[:-1] if x != 1})
    z = NORMAL.normal_form(w)
    hp, hz = SIG.absorption_plan(p), SIG.absorption_plan(z)
    current = combine((1, NORMAL.bridge(3*w)["current"]), (-1, dict(walk)), (1, hp["current"]),
                      (-1, NORMAL.bridge(w)["current"]), (-1, hz["current"]))
    coeff = Counter(hp["coefficients"])
    for u, c in hz["coefficients"].items():
        coeff[u] -= c
    data = dict(seed=w, current=current, coefficients={u: c for u, c in sorted(coeff.items()) if c},
                ancestor=p, depth=len(path) - 1)
    SIG.validate(w, data)
    data["rho_decreasing"] = all(RANK.rho(u) < RANK.rho(w) for u in data["coefficients"])
    return data


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    fam = []
    for r in (1, 2, 3):
        for s in (27, 54, 81, 27*5):
            K = 11*r + 6
            q = 81*2**K*s - 17
            w = (2*q + 1)//3
            assert w % 3456 == 3445 and CONT.one_step(w) is None
            path = smaller_ancestor(q)
            p7 = (2048*q - 2363)//2187
            assert path is not None and path[0] <= p7
            d = plan(w, path)
            fam.append(dict(r=r, s=s, depth=d["depth"], ancestor_is_minus17_word=path[0] == p7,
                            rho_decreasing=d["rho_decreasing"], requests=len(d["coefficients"])))
    rng = random.Random(7)
    cover = {}
    for label, gen in (
            ("R54 phase w=3445 mod 3456, 40 bits", lambda: 3445 + 3456*rng.randrange(2**28, 2**29)),
            ("selected 3w, w=1 mod 3, 40 bits", None), ("selected 3w, w=2 mod 3, 40 bits", None)):
        tally = Counter()
        while tally["unresolved_by_main"] < 300:
            if gen:
                w = gen()
            else:
                w = rng.randrange(2**39, 2**40)//8*8 + 5
                if not NORMAL.selected(3*w) or w % 3 != int(label.split("w=")[1][0]):
                    continue
            if CONT.one_step(w) is not None:
                continue
            tally["unresolved_by_main"] += 1
            path = smaller_ancestor(NORMAL.normal_form(3*w))
            if path is None:
                continue
            d = plan(w, path)
            tally["sigma_rule_accepts"] += 1
            tally["also_rho_decreasing"] += d["rho_decreasing"]
            tally["depth<=4"] += d["depth"] <= 4
        cover[label] = dict(tally)
    report = dict(scope="Backward-word sigma rule built from main's code; family checks plus coverage "
                        "measurement on inputs main's continued dispatcher leaves unresolved.",
                  r54_subfamily_27_divides_s=fam, coverage_of_unresolved=cover, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
