"""Replay R91's complete finite basin and exact positive transfer controls."""

import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

import shadow_precision as M

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SPEC = importlib.util.spec_from_file_location(
    "r91_history", HERE.parent / "history_cell_scope/history_cell_scope.py")
H = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(H)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def reject(call):
    try:
        call()
    except ValueError:
        return
    raise AssertionError("expected explicit invalid-domain rejection")


def audit():
    basin = M.classify()
    assert basin["cap_hits"] == 0
    assert basin["candidates"] == 1732883 and len(basin["hits"]) == 19
    assert M.BOUND == -M.ROOT + 12*M.A
    assert Fraction(12*M.D*M.A, M.A-M.M) == 12*M.A
    scores = []
    for u, d, e in basin["hits"]:
        n, cost = -u, 0
        for _ in range(d):
            assert n != M.ROOT
            n, a = M.step(n)
            cost += a
        assert n == M.ROOT and cost == e
        w = M.weight(d, e)
        assert w >= 1
        assert all(M.weight(d+12*j, e+19*j) == w for j in (1, 2, 7, 32))
        scores.append([u, d, e, str(w)])
    cycle, n, cost = [], M.ROOT, 0
    for _ in range(12):
        assert n not in [row[0] for row in cycle]
        nxt, a = M.step(n)
        cycle.append([n, nxt, a])
        n, cost = nxt, cost+a
    assert n == M.ROOT and cost == 19

    # Exercise every inverse branch, including large rays, independently
    # against the signed forward map and the branch inequalities in the proof.
    ray_checks = []
    for n, _, _ in cycle:
        for kind, a, b in M.BASES[n % 3]:
            for index in ((0,) if kind == "point" else (0, 1, 2, 8, 32)):
                p, e = M.inverse(n, kind, index)
                alpha = Fraction(2**e, 3)
                beta = Fraction(p, M.D) - alpha*Fraction(n, M.D)
                delta = alpha-beta-1
                assert alpha >= Fraction(2, 3) and beta >= Fraction(-1, 3)
                assert 0 <= delta < alpha
                assert M.step(p) == (n, e)
                ray_checks.append([n, kind, index, e, str(delta)])

    controls = []
    word_count = 0
    for r in (0, 1, 2, 4, 8, 16, 128):
        for index in (0, 1, 7):
            p = M.family(r, index)
            q, v0, target, horizon = (p[key] for key in ("Q", "v0", "target", "horizon"))
            assert 3*v0 > 2*q and H.nu(q) == q and H.nu(target) == target
            assert M.valuation(M.D*v0+M.B) >= 19*r+18
            center = M.D*v0+M.B
            assert center % 81 == 0 and center % 243 != 0
            assert center >= 81*2**(19*r+18)
            error = Fraction(243, 32)*2**(7*r)
            assert Fraction(3*v0, 2) > error
            x = q
            for _ in range(18+12*r):
                x = H.T(x)
            assert x == target  # A longer original history still exists.
            endpoints = []
            for depth in sorted({0, 1, 5, horizon-1, horizon}):
                for choice in (0, 1, 2):
                    actual, shadow, E = target, M.ROOT, 0
                    word = []
                    for j in range(depth):
                        assert actual % 3 == shadow % 3
                        options = M.BASES[shadow % 3]
                        kind, _, _ = options[(choice+j) % len(options)]
                        ray = 0 if kind == "point" else (choice+j) % 3
                        actual = H.inverse_step(actual, kind, ray)
                        shadow, e = M.inverse(shadow, kind, ray)
                        E += e
                        word.append([kind, ray])
                    lam = Fraction(2**E, 3**depth)
                    assert M.weight(depth, E) >= 1
                    assert lam*Fraction(M.A, M.M)**r >= 1
                    assert Fraction(actual)-Fraction(shadow, M.D) == lam*(target-Fraction(M.ROOT, M.D))
                    lower = lam*(target+1-Fraction(3, 2)**depth)
                    assert actual >= lower and lower > q
                    assert actual > q
                    endpoints.append([depth, choice, E, digest(word), digest(hex(actual))])
                    word_count += 1
            controls.append(dict(returns=r, index=index, horizon=horizon,
                                 original_clock=18+12*r, endpoints=endpoints))
    assert 243*(2**18-Fraction(M.D, 16)) > 3*M.B
    bad = [lambda: M.valuation(0), lambda: M.valuation(True),
           lambda: M.normalize(-M.D), lambda: M.normalize(1),
           lambda: M.normalize(-899840), lambda: M.normalize(-3*M.D),
           lambda: M.inverse(M.ROOT, "point"),
           lambda: M.inverse(M.ROOT, "ray0", -1),
           lambda: M.inverse(M.ROOT, "ray0", True),
           lambda: M.weight(-1, 2), lambda: M.weight(2, -1),
           lambda: M.family(-1), lambda: M.family(1, -1),
           lambda: M.family(True)]
    for call in bad:
        reject(call)
    files = [Path(__file__).resolve(), HERE/"shadow_precision.py",
             HERE/"independent_basin.cpp", HERE/"SHADOW_PRECISION.md",
             Path(H.__file__).resolve(),
             HERE.parent/"phi_exit_control/PHI_EXIT_CONTROL.md"]
    return dict(status="PASS", scope="Computer-assisted all-word rational slope bound and original-cell inverse exclusion through 12r+5; no all-depth positive exclusion or current supply.",
                basin=basin, scores=scores, root_cycle=cycle,
                inverse_ray_checks=len(ray_checks), inverse_ray_digest=digest(ray_checks),
                positive_families=len(controls), positive_words=word_count,
                positive_controls=controls, invalid_rejections=len(bad),
                source_sha256={str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in sorted(files)})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--cpp", action="store_true")
    args = parser.parse_args()
    result = audit()
    if args.cpp:
        compiler = shutil.which(os.environ.get("CXX", "c++"))
        if compiler is None:
            raise RuntimeError("C++17 compiler unavailable")
        with tempfile.TemporaryDirectory(prefix="collatz-r91-") as folder:
            executable = Path(folder)/"independent_basin"
            subprocess.run([compiler, "-O2", "-std=c++17", "-Wall", "-Wextra",
                            str(HERE/"independent_basin.cpp"), "-o", str(executable)],
                           check=True, timeout=60)
            independent = json.loads(subprocess.check_output([str(executable)], timeout=90))
            assert independent == result["basin"]
    receipt = HERE/"shadow_precision_audit.json"
    if args.write:
        receipt.write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
    else:
        assert json.loads(receipt.read_text()) == result
    print("PASS R91:", result["basin"]["candidates"], "origins,",
          len(result["scores"]), "hits,", result["positive_words"],
          "positive words; C++", "PASS" if args.cpp else "not requested")


if __name__ == "__main__":
    main()
