"""Bounded audit of known saturation, minimum origins, and the finite core."""

import argparse
from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
import hashlib
import json
from pathlib import Path

import saturation as S

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location("saturation_run_bridge", HERE.parent / "complementary_bridge/run_bridge.py")
RUN = module_from_spec(spec)
spec.loader.exec_module(RUN)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def lower_current(N, cap=1000):
    result = Counter()
    for seed in range(3, N+1, 2):
        x, seen = seed, set()
        while x != 1:
            assert x not in seen and len(seen) < cap
            seen.add(x)
            result[x] += 1
            x = S.step(x)
    assert S.divergence(result) == dict.fromkeys(range(3, N+1, 2), 1)
    return dict(result)


def independent_band(bases, X):
    weights = bases if isinstance(bases, dict) else dict.fromkeys(bases, 1)
    states = {}
    for q, weight in weights.items():
        for base in (q, 2*q+1):
            ratio = (3*X+1+3*base)//(3*base+1)
            exponent = ((max(1, ratio)-1).bit_length()+1)//2
            x = S.NORMAL.F_power(base, exponent)
            assert x >= X
            assert exponent == 0 or S.NORMAL.F_power(base, exponent-1) < X
            if x < 2*X:
                assert x not in states
                states[x] = weight
    return states


def run():
    cutoffs = (8, 16, 24, 32, 64, 96, 168, 384, 768)
    inputs, cores = {}, {}
    records, extensions, band_records, certificates = [], [], [], []
    stored = None
    for N in cutoffs:
        lower = lower_current(N)
        core = S.from_lower_current(N, lower)
        inputs[N], cores[N] = lower, core
        Q = set(core["bases"])
        # An independent finite propagation computes minimum canonical origins.
        minimum = {q: None for q in Q}
        for origin in range(1, N+1, 2):
            if not S.NORMAL.canonical(origin):
                continue
            q, seen = origin, set()
            while q not in seen:
                assert q in Q and len(seen) <= len(Q)
                seen.add(q)
                minimum[q] = origin if minimum[q] is None else min(minimum[q], origin)
                if q == 1:
                    break
                q = core["quotient_edges"][q]
        assert minimum == {q: data["origin"] for q, data in core["origins"].items()}
        for q, witness in core["origins"].items():
            x = witness["origin"]
            for _ in range(witness["step"]):
                assert x in lower
                x = S.step(x)
            assert x == witness["state"] and S.NORMAL.normal_form(x) == q
        records.append(dict(N=N, canonical_inputs=S.NORMAL.canonical_count(N),
                            base_count=len(Q), maximum_base=max(Q),
                            raw_known_states=len(core["raw_known_states"]),
                            core_vertices=len(core["core_vertices"]),
                            core_new_states=len(set(core["core_vertices"])-set(core["raw_known_states"])),
                            maximum_core_depth=max(core["core_depths"].values()),
                            bases_sha256=digest(core["bases"]), origins_sha256=digest(core["origins"])))
        remainder = {x: c for x, c in RUN.H.COMPLEMENT.residual_profile(N)[2].items()
                     if not RUN.H.selected(x)}
        old = {x: c for x, c in remainder.items() if RUN.normal_target(x) <= N}
        enlarged = {x: c for x, c in remainder.items() if RUN.normal_target(x) in Q}
        assert old.keys() <= enlarged.keys()
        extra = []
        for x, c in enlarged.items():
            if x in old:
                continue
            data = RUN.normalized_bridge(x)
            result = S.certify_via_bridge(x, data["target"], data["current"], core, c)
            q = data["target"]
            root_base = S.NORMAL.normal_form(x)
            item = dict(root=x, weight=c, target=q, origin=core["origins"][q],
                        root_already_in_saturation=root_base in Q,
                        root_already_in_raw_paths=x in core["raw_known_states"],
                        root_origin=core["origins"].get(root_base),
                        current_rows=len(result["current"]),
                        current_sha256=digest(result["current"]))
            extra.append(item)
            if N == 384 and x == 415:
                stored = dict(N=N, **item, current=[[y, coefficient]
                             for y, coefficient in sorted(result["current"].items())])
        extensions.append(dict(N=N, preceding_mass=sum(remainder.values()),
                               original_removed=sum(old.values()),
                               saturated_removed=sum(enlarged.values()), extra=extra))

    for N, core in cores.items():
        for cutoff in cutoffs:
            if cutoff <= N:
                assert S.threshold_bases(core, cutoff) == cores[cutoff]["bases"]

    for N in (8, 96, 384, 768):
        core = cores[N]
        Q, M = core["bases"], max(core["bases"])
        for multiplier in (1, 2, 17, 2**64, 2**512):
            X = M*multiplier
            count, _ = S.band_count(Q, X)
            telescope, corrections = S.telescope_count(Q, X)
            actual = independent_band(Q, X)
            assert count == telescope == sum(actual.values())
            band_records.append(dict(N=N, multiplier_bits=multiplier.bit_length(),
                                     count=count, base_count=len(Q),
                                     corrections=[list(c) for c in corrections],
                                     states_sha256=digest(actual)))
        chosen = sorted(set(Q[:4] + Q[-4:]))
        for q in chosen:
            for partner in (False, True):
                for exponent in (0, 1, 16, 128):
                    x = S.NORMAL.F_power(2*q+1 if partner else q, exponent)
                    weight = 2 if partner else 1
                    result = S.certify_member(x, core, weight)
                    assert S.divergence(result["current"]) == ({} if x == 1 else {x: weight})
                    certificates.append(dict(N=N, base=q, partner=partner, exponent=exponent,
                                             rows=len(result["current"]),
                                             current_sha256=digest(result["current"])))

    sparse = {q: (2 if q % 3 == 0 else -1) for q in range(1, 2048, 2)
              if S.NORMAL.canonical(q) and q % 7 in (0, 1)}
    weighted_checks = []
    for multiplier in (1, 3, 31, 2**128):
        X = max(sparse)*multiplier
        actual = independent_band(sparse, X)
        count, _ = S.band_count(sparse, X)
        telescope, corrections = S.telescope_count(sparse, X)
        assert count == telescope == sum(actual.values())
        weighted_checks.append(dict(multiplier_bits=multiplier.bit_length(), mass=count,
                                    canonical_mass=sum(sparse.values()),
                                    corrections=[list(c) for c in corrections]))
    for k in range(33):
        assert S.band_count([1], 6*4**k)[0] == 0
        assert S.band_count([1], 3*4**k)[0] == 2
    assert stored is not None
    assert stored["weight"] == 2 and stored["target"] == 1579
    assert stored["origin"]["origin"] == 327
    assert stored["root_already_in_raw_paths"]
    assert stored["root_origin"] == dict(origin=327, step=4, state=415)
    assert all(item["root_already_in_saturation"]
               for record in extensions for item in record["extra"])
    receipt = dict(status="PASS", input_cap=1000, scope="Finite supplied-graph saturation; universal target entry remains open",
                   cutoffs=records, normalized_run_extensions=extensions,
                   high_bands=band_records, weighted_sparse_bands=weighted_checks,
                   conditional_certificates=certificates,
                   oscillation_cases=66, convergence_proved=False)
    return receipt, stored


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    receipt, stored = run()
    for path, value in ((HERE/"saturation_audit.json", receipt),
                        (HERE/"root415_current.json", stored)):
        if args.write_receipt:
            path.write_text(json.dumps(value, indent=2, sort_keys=True)+"\n")
        else:
            assert json.loads(path.read_text()) == value
    print(f"PASS: {len(receipt['cutoffs'])} supplied cutoffs, "
          f"{len(receipt['high_bands'])} high bands, "
          f"{len(receipt['conditional_certificates'])} member currents; weight2 root415 stored")


if __name__ == "__main__":
    main()
