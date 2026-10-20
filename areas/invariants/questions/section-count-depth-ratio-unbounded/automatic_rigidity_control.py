"""Sidekick probe: control experiment for main's proposed goal "full automatic rigidity" (docs/NEXT_GOAL_PROPOSAL.md,
main 8572962): every finite-valued binary-automatic h with h(2n)=h(n), h(3n+d)=h(n) (odd n>1) is constant (d=1).

Question tested (finite evidence only): for d = 5, 7, 13, the natural invariant coloring c_d(n) = "which cycle the orbit
of n ends in" is invariant. Is it 2-automatic? A sequence is 2-automatic iff its 2-kernel
{n -> c(2^e n + r) : e >= 0, 0 <= r < 2^e} is finite. We count distinct kernel elements, each truncated to its first W
terms, for e = 0..E. Saturation suggests (does not prove) automaticity; steady growth suggests non-automaticity.
Controls: the periodic colorings 1_{d|n} (automatic, kernel saturates) and Thue-Morse (automatic, kernel size 2).
If the cycle labelling is non-automatic for every d tested, the d-uniform statement "every automatic invariant coloring
is periodic" stays plausible, and V13's periodic classification (constant iff gcd(M,d)=1 orbits) would then give the
d=1 theorem. Standard library. Run without -O.
"""
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def v2(n):
    return (n & -n).bit_length() - 1


def cycle_labels(d, N):
    """label[n] = min of the cycle reached by n under the odd map (halving first), for 1 <= n <= N."""
    lab = {}
    def T(x):
        y = 3*x + d
        return y >> v2(y)
    out = [0]*(N + 1)
    for n in range(1, N + 1):
        x = n >> v2(n)
        path = []
        seen = {}
        while x not in lab and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = T(x)
            if len(path) > 10**6:
                raise RuntimeError("no cycle found")
        if x in lab:
            L = lab[x]
        else:
            cyc = path[seen[x]:]
            L = min(cyc)
        for y in path:
            lab[y] = L
        out[n] = lab[n >> v2(n)]
    return out


def kernel_sizes(seq, E, W):
    sizes = []
    for e in range(E + 1):
        elems = set()
        for e2 in range(e + 1):
            for r in range(2**e2):
                t = tuple(seq[2**e2 * k + r] for k in range(1, W + 1))
                elems.add(t)
        sizes.append(len(elems))
    return sizes


def main():
    E, W = 9, 60
    N = 2**E * (W + 2)
    out = {"probe": "automatic_rigidity_control", "main": "8572962", "E": E, "W": W, "rows": {}}
    for d in (5, 7, 13):
        lab = cycle_labels(d, N)
        distinct = sorted(set(lab[1:]))
        mult = [1 if n % d == 0 else 0 for n in range(N + 1)]
        out["rows"][f"d={d}"] = {
            "cycle_labels_seen": distinct[:12],
            "kernel_sizes_cycle_label": kernel_sizes(lab, E, W),
            "kernel_sizes_multiple_of_d": kernel_sizes(mult, E, W)}
    tm = [bin(n).count("1") % 2 for n in range(N + 1)]
    out["thue_morse_kernel_sizes"] = kernel_sizes(tm, E, W)
    out["result"] = "DONE"
    (HERE / "automatic_rigidity_control.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
