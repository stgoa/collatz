"""Sidekick probe: R49's all-depth inverse exclusions, and an exact census of ancestor-free states.

R49 (main ea3278e, inverse_scope/INVERSE_SCOPE.md): a canonical q > 1 has a strictly smaller
canonical ancestor at some positive depth iff q lies in Q_<q, the T-forward closure of the
canonical states below q. Anchors b = 39 and b = 135 are outside Q_<b, yet reach smaller absorbed
history in three quotient arrows: 39 -> 59 -> 89 -> 33 and 135 -> 203 -> 305 -> 57.

Checks with this branch's own nu/step (no main code):
  1. 39 and 135 are canonical, lie outside Q_<b, and have the stated three-arrow paths;
  2. census: process canonical q in increasing order up to X, keeping the set V of all states
     on T-orbits of smaller canonical states; q is ancestor-free iff q is not in V. Reports the
     count and share of ancestor-free canonical states below X, overall and by q mod 3.
Standard library. Run without -O.
"""
from collections import Counter
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu  # noqa: E402

X = 2*10**6


def T(q):
    return nu(step(1, q))


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    for b, path in ((39, [59, 89, 33]), (135, [203, 305, 57])):
        assert nu(b) == b
        q, seen = b, []
        for target in path:
            q = T(q)
            assert q == target
        assert path[-1] < b
    V, free, total, by3, checkpoints = {1}, [], 0, Counter(), {}
    for q in range(3, X, 2):
        if nu(q) != q:
            continue
        total += 1
        if q not in V:
            free.append(q)
            by3[q % 3] += 1
        x = q
        while x not in V:
            V.add(x)
            x = T(x)
        if total in (10**3, 10**4, 10**5) or q in (10**5 - 1, 10**6 - 1):
            checkpoints[q] = (total, len(free))
    assert 39 in free and 135 in free
    tot3 = Counter(q % 3 for q in range(3, X, 2) if nu(q) == q)
    report = dict(scope="R49 anchors and exact census of canonical states with no smaller canonical ancestor, below %d." % X,
                  canonical_states=total, ancestor_free=len(free), share=round(len(free)/total, 4),
                  first_ancestor_free=free[:20],
                  share_by_q_mod_3={str(r): round(by3[r]/tot3[r], 4) for r in sorted(tot3)},
                  checkpoints={str(k): dict(canonical=v[0], ancestor_free=v[1], share=round(v[1]/v[0], 4))
                               for k, v in sorted(checkpoints.items())},
                  status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
