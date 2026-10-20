"""Compile finite common-tail trees into universal affine current identities.

Generic identity validity and coverage of actual annular measures are separate
checks. The recorded examples cover finitely many atoms at each scale, not the
whole annulus. All discovery loops have explicit caps.
"""

import argparse
from collections import defaultdict
from fractions import Fraction
from math import gcd, lcm
import json
from pathlib import Path

from annular_components import ANNULAR, CURRENT, step

HERE = Path(__file__).resolve().parent


def compile_template(sources, max_depth=128):
    assert sources and sum(sources.values()) <= 0
    paths = {}
    for source in sources:
        assert source > 1 and source % 2
        path, seen, x = [], set(), source
        for _ in range(max_depth + 1):
            if x in seen:
                break
            path.append(x)
            seen.add(x)
            if x == 1:
                break
            x = step(x)
        paths[source] = path
    common = set.intersection(*(set(path) for path in paths.values()))
    if not common:
        return dict(status="unresolved", cap=max_depth)
    meeting = next(x for x in paths[min(sources)] if x in common)
    current, distances, valuations = defaultdict(int), {meeting: 0}, {meeting: 0}
    for source, coefficient in sources.items():
        path = paths[source][:paths[source].index(meeting) + 1]
        for x, y in reversed(list(zip(path, path[1:]))):
            numerator = 3 * x + 1
            a = (numerator & -numerator).bit_length() - 1
            assert numerator == (1 << a) * y
            d, A = distances[y] + 1, valuations[y] + a
            assert x not in distances or (distances[x], valuations[x]) == (d, A)
            distances[x], valuations[x] = d, A
            current[x] += coefficient
    maximum_depth = max(distances.values())
    rows = []
    for x in sorted(distances):
        rows.append(dict(state=x, distance=distances[x], accumulated_valuation=valuations[x],
                         slope=2**(valuations[x] + 1) * 3**(maximum_depth - distances[x]),
                         source_coefficient=sources.get(x, 0), current_coefficient=current.get(x, 0)))
    template = dict(status="compiled", source_mass=sum(sources.values()), meeting=meeting,
                    maximum_depth=maximum_depth, rows=rows,
                    generic_positive_current_cost=sum(max(0, c) for c in current.values()))
    instantiate(template, 0)
    return template


def instantiate(template, t):
    assert t >= 0 and isinstance(t, int)
    source, current, states = defaultdict(int), defaultdict(int), {}
    for row in template["rows"]:
        x = row["state"] + row["slope"] * t
        assert x > 0 and x % 2
        states[row["state"]] = x
        if x > 1:
            source[x] += row["source_coefficient"]
            current[x] += row["current_coefficient"]
    for row in template["rows"]:
        if row["state"] == template["meeting"]:
            continue
        assert step(states[row["state"]]) == states[step(row["state"])]
    residual = {}
    lifted_meeting = states[template["meeting"]]
    if template["source_mass"] and lifted_meeting > 1:
        residual[lifted_meeting] = template["source_mass"]
    source, current = CURRENT.clean(source), CURRENT.clean(current)
    check = defaultdict(int, CURRENT.divergence(current, step, 1))
    for x, c in residual.items():
        check[x] += c
    assert CURRENT.clean(check) == source
    assert all(c < 0 for c in residual.values())
    return source, current, residual


def coefficient_at(N, x):
    assert N > 0 and N % 8 == 0
    Q = 9 * N // 4
    if not Q < x < 64 * Q or x % 2 == 0:
        return 0
    band = (x // Q).bit_length() - 1
    return dict(zip(ANNULAR.RESIDUES, ANNULAR.EXPECTED_ROWS[band])).get(x % 18, 0)


def certify_scale_coverage(template, N0):
    """Find t=T*s so sources remain actual A_(N0*(1+s)) atoms for all s>=0."""
    assert N0 > 0 and N0 % 8 == 0
    Q0, modulus = 9 * N0 // 4, 1
    lower, upper, records = Fraction(0), None, []
    for row in template["rows"]:
        if not row["source_coefficient"]:
            continue
        x, slope, coefficient = row["state"], row["slope"], row["source_coefficient"]
        assert coefficient_at(N0, x) == coefficient
        band = (x // Q0).bit_length() - 1
        low, high = 2**band * Q0, 2**(band + 1) * Q0
        lower = max(lower, Fraction(low, slope))
        upper = Fraction(high, slope) if upper is None else min(upper, Fraction(high, slope))
        modulus = lcm(modulus, 18 // gcd(18, slope))
        records.append(dict(state=x, slope=slope, band=band,
                            coefficient=coefficient, base_lower=low, base_upper=high))
    T = ((lower.numerator + lower.denominator * modulus - 1)
         // (lower.denominator * modulus)) * modulus
    if T > upper:
        return dict(status="no_scale_match", lower=str(lower), upper=str(upper), modulus=modulus)
    for record in records:
        assert record["base_lower"] <= record["slope"] * T <= record["base_upper"]
        assert record["slope"] * T % 18 == 0
    for i, first in enumerate(records):
        for second in records[i + 1:]:
            difference = T * (first["slope"] - second["slope"])
            if difference:
                crossing = Fraction(second["state"] - first["state"], difference)
                assert crossing < 0 or crossing.denominator != 1
            else:
                assert first["state"] != second["state"]
    return dict(status="proved_linear_band_conditions", base_cutoff=N0,
                scale_parameter="N=N0*(1+s), t=T*s, integer s>=0", T=T,
                allowed_T_interval=[str(lower), str(upper)], residue_modulus=modulus,
                source_conditions=records,
                whole_annulus_covered=False)


def family_indices(N, residue):
    assert N > 0 and N % 8 == 0 and residue in (0, 3)
    first, last = (96, 120) if residue == 0 else (120, 152)
    lower = max(0, (N - last + 95) // 96)
    upper = (N - first) // 72
    return range(lower, max(lower, upper + 1))


def in_short_catalogue(N, point):
    """Independent inverse-membership check for the audited five-family catalogue."""
    families = ((12, 16, (7,), (0, 1)),
                (16, 18, (23, 71), (0, 2)),
                (24, 32, (7,), (0, 1, 2)),
                (32, 36, (23,), (0, 1, 2)),
                (48, 64, (7, 55), (0, 1, 2)))
    inverse_numerators = ((point, 1), (2 * point - 1, 3), (4 * point - 5, 9))
    for lower, upper, residues, positions in families:
        for position in positions:
            numerator, denominator = inverse_numerators[position]
            if numerator % denominator:
                continue
            x = numerator // denominator
            if lower * N < x < upper * N and x % 72 in residues:
                return True
    return False


def check_disjoint_two_class_family(template):
    source_rows = [r for r in template["rows"] if r["source_coefficient"]]
    progressions = [dict(state=r["state"] + residue * r["slope"],
                         period=9 * r["slope"], residue=residue,
                         original_state=r["state"])
                    for residue in (0, 3) for r in source_rows]
    pair_count = 0
    for i, first in enumerate(progressions):
        for second in progressions[i + 1:]:
            common = gcd(first["period"], second["period"])
            assert (first["state"] - second["state"]) % common != 0
            pair_count += 1
    example_counts = []
    for N in range(8, 4097, 8):
        source_total, current_total = {}, defaultdict(int)
        copies = 0
        for residue in (0, 3):
            indices = family_indices(N, residue)
            for s in indices:
                source, current, residual = instantiate(template, 9 * s + residue)
                assert not residual
                assert not source_total.keys() & source.keys()
                assert all(coefficient_at(N, x) == c for x, c in source.items())
                assert all(not in_short_catalogue(N, x) for x in source)
                source_total.update(source)
                for x, c in current.items():
                    current_total[x] += c
                copies += 1
            # The exact interval formula agrees with all five strict bands.
            for s in range(max(0, indices.start - 1), indices.stop + 2):
                source, _, _ = instantiate(template, 9 * s + residue)
                actual = all(coefficient_at(N, x) == c for x, c in source.items())
                assert actual == (s in indices)
        assert len(source_total) == 5 * copies
        assert sum(c for c in source_total.values() if c > 0) == 3 * copies
        assert CURRENT.divergence(CURRENT.clean(current_total), step, 1) == source_total
        assert sum(c for c in current_total.values() if c > 0) <= 3 * copies
        assert (copies > 0) == (96 <= N <= 152 or N >= 168)
        if N in (96, 112, 128, 144, 160, 168, 384, 768, 4096):
            example_counts.append(dict(N=N, copies=copies, source_atoms=5 * copies,
                                       removed_positive_mass=3 * copies,
                                       positive_current_cost=sum(c for c in current_total.values() if c > 0)))
    return dict(source_progressions=progressions, disjoint_progression_pairs=pair_count,
                residue_classes_mod9=[0, 3],
                admissibility={"0": "96+72s<=N<=120+96s", "3": "120+72s<=N<=152+96s"},
                copy_count_asymptotic="N/144+O(1)",
                nonempty_for="8|N and (96<=N<=152 or N>=168)",
                full_cutoffs_checked={"first": 8, "last": 4096, "step": 8},
                short_catalogue_capacity="disjoint from E,D,B,C,A; independently checked by inverse membership",
                examples=example_counts)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-receipt", action="store_true")
    args = parser.parse_args()
    examples = [
        ("five_source_cross_band", 96, {4591: -1, 6121: -1, 6887: 1, 10331: 2, 13775: -1}),
        ("three_source_cross_band", 168, {10087: -1, 15131: -1, 22697: 2}),
    ]
    output = []
    for name, N0, sources in examples:
        template = compile_template(sources)
        assert template["status"] == "compiled"
        coverage = certify_scale_coverage(template, N0)
        assert coverage["status"] == "proved_linear_band_conditions"
        for t in list(range(32)) + [10**6, 2**128]:
            instantiate(template, t)
        scale_parameters = list(range(32)) + [64**k - 1 for k in range(1, 21)]
        for s in scale_parameters:
            lifted, _, _ = instantiate(template, coverage["T"] * s)
            N = N0 * (1 + s)
            assert all(coefficient_at(N, x) == c for x, c in lifted.items())
        output.append(dict(name=name, template=template, coverage=coverage,
                           finite_generic_parameters_checked=34,
                           finite_scale_parameters_checked=len(scale_parameters)))
    two_class_family = check_disjoint_two_class_family(output[0]["template"])
    result = dict(status="PASS", templates=output, two_class_family=two_class_family,
                  universal_identities_proved=True,
                  whole_annular_current_construction_proved=False)
    path = HERE / "affine_templates.json"
    if args.write_receipt:
        path.write_text(json.dumps(result, indent=2) + "\n")
    else:
        assert json.loads(path.read_text()) == result
    print(json.dumps(dict(status="PASS", templates=[dict(name=x["name"],
                          meeting=x["template"]["meeting"],
                          maximum_depth=x["template"]["maximum_depth"],
                          source_slopes={str(r["state"]): r["slope"] for r in x["template"]["rows"] if r["source_coefficient"]},
                          scale_T=x["coverage"]["T"],
                          positive_current_cost=x["template"]["generic_positive_current_cost"])
                          for x in output]), indent=2))


if __name__ == "__main__":
    main()
