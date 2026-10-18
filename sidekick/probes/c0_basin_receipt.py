"""Sidekick probe wrapper: build and run c0_basin_classify.c on the R91 universe (validation) and on
main's deeper-window candidate universe (8), then write a JSON receipt.

Validation targets from R91 (main a94533a, shadow_precision/SHADOW_PRECISION.md): 1,732,883 eligible
origins, 19 in the c0 basin, maximum intermediate numerator 1,049,066,989,135, all weighted slopes >= 1.
Candidate universe: odd u with 7153 < u < 741545113, gcd(u, 7153) = 1, -u/7153 canonical
(deeper_window/CANDIDATE.md, (8)). Relevant boundary tails: c0-basin origins with first-hit depth
d0 = 5 mod 12; their cost m = E0 - 19 k0 (k0 = (d0-5)/12) must lie in {8,...,14} to satisfy (6)/(10).
Requires a C compiler (cc). Run from the repository root.
"""
from pathlib import Path
import json
import re
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent


def run(binary, U):
    out = subprocess.run([binary, str(U)], capture_output=True, text=True, check=True).stdout
    head = re.search(r"U=(\d+) eligible=(\d+) memohits=(\d+) maxpath=(\d+) maxnum=(\d+)", out)
    tail = re.search(r"basin=(\d+) not_basin=(\d+) unknown=(\d+) relevant\(d0=5 mod 12\)=(\d+) "
                     r"m_outside_8_14=(\d+) min_mu=([0-9.]+)", out)
    rel = [dict(u=int(a), d0=int(b), E0=int(c), k0=int(d), m=int(e))
           for a, b, c, d, e in re.findall(r"relevant u=(\d+) d0=(\d+) E0=(\d+) k0=(\d+) m=(\d+)", out)]
    return dict(U=int(head[1]), eligible=int(head[2]), max_path=int(head[4]), max_numerator=int(head[5]),
                basin=int(tail[1]), not_basin=int(tail[2]), unknown=int(tail[3]), relevant=int(tail[4]),
                min_weighted_slope=float(tail[6]), relevant_tails=rel)


def main():
    with tempfile.TemporaryDirectory() as tmp:
        binary = str(Path(tmp) / "c0b")
        subprocess.run(["cc", "-O2", "-o", binary, str(HERE / "c0_basin_classify.c"), "-lm"], check=True)
        small = run(binary, 7277133)
        big = run(binary, 741545113)
    assert (small["eligible"], small["basin"], small["max_numerator"], small["unknown"]) == (1732883, 19, 1049066989135, 0)
    assert small["min_weighted_slope"] >= 1.0 and big["unknown"] == 0 and big["min_weighted_slope"] >= 1.0
    cost_list = [t for t in big["relevant_tails"] if 8 <= t["m"] <= 14]
    hist = {}
    for t in big["relevant_tails"]:
        hist[t["m"]] = hist.get(t["m"], 0) + 1
    report = dict(scope="Classification of the c0 basin of the signed canonical quotient on -u/7153; R91 universe "
                        "(validation) and the deeper-window candidate universe (8).",
                  r91_validation={k: small[k] for k in ("U", "eligible", "basin", "unknown", "max_numerator",
                                                        "max_path", "min_weighted_slope")},
                  candidate_universe={k: big[k] for k in ("U", "eligible", "basin", "not_basin", "unknown",
                                                          "relevant", "max_numerator", "max_path", "min_weighted_slope")},
                  relevant_cost_histogram={str(k): v for k, v in sorted(hist.items())},
                  tails_with_cost_in_8_to_14=cost_list, status="PASS")
    (HERE / "c0_basin_receipt.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: report[k] for k in ("r91_validation", "candidate_universe", "relevant_cost_histogram")}, indent=2))
    print("tails with m in 8..14:", len(cost_list))


if __name__ == "__main__":
    main()
