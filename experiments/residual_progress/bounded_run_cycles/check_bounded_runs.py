"""Reproduce finite witnesses for the repeated bounded-run theorem."""

import argparse
import hashlib
import json
from pathlib import Path
import bounded_runs as B

HERE = Path(__file__).resolve().parent


def fingerprint(values):
    return hashlib.sha256("\n".join(map(str, values)).encode()).hexdigest()


def run():
    assert B.FIXED_DENOMINATOR*27+B.OFFSET == 2**17
    prefix = []
    A, C = 0, 0
    for j, a in enumerate(B.WORD, 1):
        C = 3*C + 2**A
        A += a
        assert 3**j > 2**A
        prefix.append(dict(j=j, valuation=a, total=A, numerator=3**j, offset=C))
    assert (3**8, 2**A, C) == (6561, 2048, 9221)

    samples = []
    for repeats in list(range(1, 17)) + [32, 64, 128]:
        residue, modulus = B.cylinder(repeats)
        for offset in (0, 1, 7):
            x = residue + offset*modulus
            result = B.witness(x, repeats)
            samples.append(dict(repeats=repeats, offset=offset,
                                bits=modulus.bit_length()-1, seed_bits=x.bit_length(),
                                endpoint_bits=result["endpoint"].bit_length(),
                                rows=len(result["current"]),
                                states_sha256=fingerprint(result["states"]),
                                returns_sha256=fingerprint(result["block_returns"])))

    ray_samples = []
    for repeats in (1, 2, 4, 8, 16, 32, 64):
        for extra in (0, 1, 17):
            N, x = B.ray_root(repeats, extra)
            result = B.witness(x, repeats)
            assert x % 12 == 3 and N < x < 3*N//2
            assert not B.RUN.H.selected(x)
            assert B.RUN.normal_target(x) > N
            assert all(y > N for y in result["states"])
            assert all(B.NORMAL.normal_form(y) == y for y in result["states"])
            ray_samples.append(dict(repeats=repeats, extra_scale=extra,
                                    N_bits=N.bit_length(), seed_bits=x.bit_length(),
                                    states_sha256=fingerprint(result["states"])))

    finite_moduli = []
    for modulus in (8, 16, 27, 64, 81, 128):
        repeats = modulus+1
        residue, _ = B.cylinder(repeats)
        result = B.witness(residue, repeats)
        first = {}
        repeated = None
        # Labels contain both run parameters and the chosen fixed residue.
        for i, (x, label) in enumerate(zip(result["block_returns"], result["labels"])):
            key = (*label, x % modulus)
            if key in first:
                old_i, old_x = first[key]
                assert x > old_x
                repeated = dict(first=old_i, second=i, label=list(key))
                break
            first[key] = (i, x)
        assert repeated is not None
        finite_moduli.append(dict(modulus=modulus, repeats=repeats, witness=repeated))

    return dict(status="PASS", scope="Arbitrarily long finite growth; no divergent positive orbit claim",
                word=list(B.WORD), affine_prefixes=prefix,
                fixed_point="-9221/4513", samples=samples, required_ray_samples=ray_samples,
                finite_label_examples=finite_moduli)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    actual = run()
    path = HERE / "bounded_runs_audit.json"
    if args.write_receipt:
        path.write_text(json.dumps(actual, indent=2)+"\n")
    else:
        assert actual == json.loads(path.read_text())
    print(f"PASS: {len(actual['samples'])} cylinders, "
          f"{len(actual['required_ray_samples'])} required-ray witnesses, "
          f"{len(actual['finite_label_examples'])} finite-label examples")


if __name__ == "__main__":
    main()
