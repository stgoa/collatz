"""Sidekick probe: independent checks for main's R51-R54 batch (working copy, 2026-10-17 23:07).

R54 phase: every w = 3445 (mod 3456) has 3w selected, w = 1 (mod 3) and rho(w) = nu(3w) = -17
     (mod 5184).
R54 family: for q = 81*2^(11r+6)*s - 17 (r, s >= 1), the quotient map T = nu o S repeats a
     7-step word r times: T^(7k)(q) = Psi^k(q), with Psi(q) = (2187q+2363)/2048. Every
     noninitial prefix state exceeds q. The identity Psi(q)+17 = (2187/2048)(q+17) is checked.
R51 examples: rho/sigma values at w = 44981, 96069, 4629, 2197, using
     sigma(w) = 4w/3 - 1 on returning inputs (here the multiples of 3).
Standard library. Run without -O.
"""
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parents[1] / "experiments" / "packet_currents" / "negative_controls")]
from affine_controls import step  # noqa: E402
from fibre_count_check import nu, selected  # noqa: E402


def main():
    assert not sys.flags.optimize, "assertion-based checks: run without -O"
    phase = 0
    for w in range(3445, 3445 + 3456*400, 3456):
        assert w % 8 == 5 and selected(3*w) and w % 3 == 1 and (nu(3*w) + 17) % 5184 == 0, w
        phase += 1
    T = lambda y: nu(step(1, y))
    Psi = lambda q: (2187*q + 2363)//2048
    fam = 0
    for r in range(1, 6):
        for s in (1, 2, 3, 7):
            q0 = 81*2**(11*r + 6)*s - 17
            q = q0
            for _ in range(r):
                assert (2187*q + 2363) % 2048 == 0 and Psi(q) + 17 == 2187*(q + 17)//2048
                expect = Psi(q)
                y = q
                for _ in range(7):
                    y = T(y)
                    assert y > q0, (r, s)
                assert y == expect, (r, s)
                q = y
            fam += 1
    rho = lambda w: nu(3*w)
    vals = dict(rho_44981=rho(44981), rho_96069=rho(96069), sigma_96069=4*96069//3 - 1,
                sigma_4629=4*4629//3 - 1, rho_2197=rho(2197))
    assert vals == dict(rho_44981=134943, rho_96069=144103, sigma_96069=128091,
                        sigma_4629=6171, rho_2197=6591), vals
    report = dict(scope="Independent finite checks of main's R51/R54 claims (working copy).",
                  r54_phase_inputs=phase, r54_family_cases=fam, r51_values=vals, status="PASS")
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
