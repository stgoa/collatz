"""Sidekick probe: negative controls for the tripling-pair obligation (main R35, commit 1603bf3).

R35 reduces the residual to tripling pairs P(w) = delta_(3w) - delta_w (w = 3 mod 8) and
doubling pairs. A universal certificate for P(w) implies that w and 3w share a future
(possibly at the absorber). For maps 3x+d with nontrivial cycles, that statement
fails. Listed here: odd w = 3 (mod 8) below 4000 whose w and 3w lie in different basins
(nontrivial cycle vs trivial set). Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

sys.path[:0] = [str(Path(__file__).resolve().parents[2] / "collatz_research_20261017" / "negative_controls")]
from affine_controls import Basins  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    report = {}
    for d in (-1, 13, 61):
        basins = Basins(d)
        label = lambda x: "trivial" if basins(x) in basins.trivial() else basins(x)
        bad = [(w, label(w), label(3*w)) for w in range(3, 4000, 8) if label(w) != label(3*w)]
        assert bad
        report[str(d)] = dict(counterexamples_below_4000=len(bad), first=bad[:5])
    assert ("235" in json.dumps(report["61"]["first"]))
    out = dict(scope="Generic pair-merger statement fails on 3x+d with cycles; d = 1 untested by design.",
               controls=report, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
