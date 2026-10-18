"""Sidekick probe: R77's spacing mechanism for arbitrary odd-only orbits.

Claim (elementary written proof, likely known): let x_0 > 0 be odd with odd-only orbit x_n, and
let a valuation factor w = (v_1..v_L) with sum e occur at positions i < j along a non-repeating
segment of the orbit. The odd x whose next L valuations are exactly w form one class mod 2^(e+1)
(Terras), so x_j = x_i (mod 2^(e+1)) and max(x_i, x_j) >= 2^(e+1). Since x_n + 1 <= (3/2)^n (x_0 + 1),
    e + 1 < j log2(3/2) + log2(x_0 + 1).
Consequently a divergent orbit's valuation itinerary has factor complexity
    p(L) >= (L + 1 - log2(x_0 + 1)) / log2(3/2),   so liminf p(L)/L >= 1/log2(3/2) = 1.7095...
(strictly more than the Morse-Hedlund bound L + 1 for aperiodic words). R77's 18.285 is the same
argument inside its subsystem, where every symbol consumes at least 19 bits.

Check: on the orbits of all odd x_0 < 10^5 (up to absorption), every repeated factor of length
1..6 satisfies the congruence, the size inequality and the per-pair bound above. Standard library.
"""
from math import log2
from pathlib import Path
import json
import sys


def v2(n):
    return (n & -n).bit_length() - 1


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    pairs = 0
    for x0 in range(3, 10**5, 2):
        xs, vs, x = [x0], [], x0
        while x != 1:
            z = 3*x + 1
            v = v2(z)
            vs.append(v)
            x = z >> v
            xs.append(x)
        for L in range(1, 7):
            first = {}
            for i in range(len(vs) - L + 1):
                w = tuple(vs[i:i + L])
                if w in first:
                    i0 = first[w]
                    e = sum(w)
                    assert (xs[i] - xs[i0]) % 2**(e + 1) == 0 and xs[i] != xs[i0]
                    assert max(xs[i], xs[i0]) >= 2**(e + 1)
                    assert e + 1 < i*log2(1.5) + log2(x0 + 1)
                    pairs += 1
                else:
                    first[w] = i
    report = dict(scope="Spacing inequality for repeated valuation factors on all odd x0 < 1e5 (orbits up to 1).",
                  repeated_factor_pairs=pairs, complexity_constant=1/log2(1.5), status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
