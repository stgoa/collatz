"""Exact residual endpoint geometry for two maximum arcs of lengths 2+2 and 3+1.

Affine coefficient identities certify the inequality eliminations for all
parameters in the stated branches. Finite exact profiles check the ordering,
minimum and paired-endpoint formulas; they are not a cycle enumeration.
"""

from bisect import bisect_left
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


# Affine polynomials in (1,u,v), with exact rational coefficients.
def affine(constant=0, u=0, v=0):
    return tuple(map(F, (constant, u, v)))


def add(*values):
    return tuple(sum((value[i] for value in values), F()) for i in range(3))


def scale(weight, value):
    return tuple(F(weight)*coefficient for coefficient in value)


def subtract(left, right):
    return add(left, scale(-1, right))


def symbolic_checks():
    U, V = affine(u=1), affine(v=1)
    records = []

    def identity(name, gap_sum, height_sum, witness_count, margin, terms, domain):
        left = subtract(subtract(gap_sum, height_sum), affine(witness_count*margin))
        right = add(*(scale(weight, expression) for weight, expression, _, _ in terms))
        require(left == right, f"affine coefficient identity: {name}")
        require(all(weight > 0 for weight, _, _, _ in terms), "positive identity multipliers")
        require(any(strict for _, _, _, strict in terms), "strict positive slack retained")
        records.append(dict(name=name, domain=domain, witness_count=witness_count,
                            margin=str(margin), left_coefficients=list(map(str, left)),
                            positive_terms=[dict(weight=str(weight), coefficients=list(map(str, expression)),
                                                 slack=label, strict=strict)
                                            for weight, expression, label, strict in terms]))

    # Pair (2,2), v<u. J(u)=3/32*max(1,2-4v).
    gap22 = subtract(scale(2, U), V)
    common22 = [(F(1), subtract(U, V), "u-v", True),
                (F(1), subtract(U, affine(F(1, 4))), "u-1/4", False)]
    identity("22_lower_constant_height", gap22, affine(F(3, 32)), 1, F(1, 16),
             common22+[(F(1), affine(F(3, 32)), "3/32", True)],
             "1/4<=u<1/3, 0<v<u; constant branch of the paired maximum")
    identity("22_lower_affine_height", gap22, affine(F(3, 16), v=-F(3, 8)), 1, F(1, 16),
             common22+[(F(3, 8), V, "v", True)],
             "1/4<=u<1/3, 0<v<u; affine branch of the paired maximum")
    identity("22_upper_gap_v", V, affine(F(3, 32)), 1, F(5, 32),
             [(F(1), subtract(V, U), "v-u", True),
              (F(1), subtract(U, affine(F(1, 4))), "u-1/4", False)],
             "1/4<=u<1/3, u<v<=1/2, v<1-2u")
    identity("22_upper_gap_complement", affine(1, u=-2), affine(F(3, 32)), 1, F(5, 32),
             [(F(2), affine(F(1, 3), u=-1), "1/3-u", True),
              (F(1), affine(F(1, 12)), "1/12", True)],
             "1/4<=u<1/3, u<v<=1/2, v>1-2u")

    # Pair (3,1), the two sub-minima when 0<v<3u-1.
    half_minus_u = affine(F(1, 2), u=-1)
    u_above = affine(-F(4, 9), u=1)
    identity("31_lower_two_gaps_min_at_v", affine(2, u=-3), affine(F(9, 32), v=-F(3, 8)),
             2, F(7, 64),
             [(F(3), half_minus_u, "1/2-u", True), (F(3, 8), V, "v", True)],
             "4/9<u<1/2, 0<v<3u-1; post-minimum 4v-2")
    identity("31_lower_two_gaps_min_at_u", affine(2, u=-3),
             affine(F(15, 32), u=-F(3, 4), v=F(3, 8)), 2, F(7, 64),
             [(F(27, 8), half_minus_u, "1/2-u", True),
              (F(3, 8), affine(-1, u=3, v=-1), "3u-1-v", True)],
             "4/9<u<1/2, 0<v<3u-1; post-minimum 4u-3")
    identity("31_lower_single_gap", U, affine(F(3, 16), u=-F(3, 8), v=F(3, 8)),
             1, F(37, 144),
             [(F(1), u_above, "u-4/9", True),
              (F(3, 8), subtract(U, V), "u-v", True)],
             "4/9<u<1/2, 3u-1<v<u")

    gap31 = affine(-1, u=3)
    identity("31_middle_min_at_v", gap31, affine(u=F(3, 4), v=-F(3, 8)),
             1, F(7, 48),
             [(F(3), u_above, "u-4/9", True),
              (F(3, 8), half_minus_u, "1/2-u", True),
              (F(3, 8), subtract(V, U), "v-u", True)],
             "4/9<u<1/2, u<v<1-u, v<1/2")
    identity("31_middle_min_at_zero", gap31, affine(-F(3, 16), u=F(3, 4)),
             1, F(7, 48),
             [(F(3), u_above, "u-4/9", True),
              (F(3, 4), half_minus_u, "1/2-u", True)],
             "4/9<u<1/2, u<v<1-u, v>=1/2")
    identity("31_upper_two_gaps", affine(2, u=-3),
             affine(F(3, 16), u=-F(3, 8), v=F(3, 8)), 2, F(1, 16),
             [(F(27, 8), half_minus_u, "1/2-u", True),
              (F(3, 8), affine(u=2, v=-1), "2u-v", True)],
             "4/9<u<1/2, 1-u<v<2u")
    identity("31_final_single_gap", gap31, affine(-F(3, 32), u=F(3, 4)),
             1, F(5, 96),
             [(F(3), u_above, "u-4/9", True),
              (F(3, 4), half_minus_u, "1/2-u", True)],
             "4/9<u<1/2, 2u<v<1")
    require(len(records) == 11, "all residual affine identities")
    require(min(F(7, 64), F(37, 144), F(7, 48), F(1, 16), F(5, 96)) == F(5, 96),
            "31 uniform residual margin")
    require(F(1, 16) > F(1, 3952) and F(5, 96) > F(1, 3952),
            "both residual margins exceed the application error")
    return dict(coordinate_order=["1", "u", "v"], identities=records,
                uniform_margins={"2+2": "1/16", "3+1": "5/96"},
                scope="Exact affine identities with positive multipliers and explicitly positive branch slacks; no inference from the finite grid.")


def exact_profile(M, h, a, c, v):
    points = sorted([(i*h) % M for i in range(a)]+[(v+i*h) % M for i in range(c)])
    if len(set(points)) != a+c:
        return None, "overlapping_maxima"
    boundaries = [(-h) % M, ((a-1)*h) % M, (v-h) % M, (v+(c-1)*h) % M]
    if len(set(boundaries)) != 4:
        return None, "coincident_boundaries"
    r = a+c
    post = [r*x-M*(i+1) for i, x in enumerate(points)]
    minimum = min(post)
    ordered = sorted(boundaries)

    def shifted_before(x):
        # Zero is evaluated BEFORE its jump. F(0)=F(1-)=0.
        x %= M
        return r*x-M*bisect_left(points, x)-minimum

    pairs = {e: max(shifted_before(e), shifted_before(e+h)) for e in ordered}
    gaps = {e: (e-ordered[i-1]) % M for i, e in enumerate(ordered)}
    deficits = {e: 8*r*gaps[e]-3*pairs[e] for e in ordered}
    return dict(points=points, minimum=minimum, minimum_ties=post.count(minimum),
                boundaries=ordered, pairs=pairs, gaps=gaps, deficits=deficits), None


def grid_checks():
    periods = list(range(24, 161))+[216, 240]
    counts = {"candidates": 0, "overlapping_maxima": 0, "coincident_boundaries": 0,
              "pair22": 0, "pair31": 0, "tied_post_minima": 0,
              "22_lower": 0, "22_upper_gap_v": 0, "22_upper_gap_complement": 0,
              "31_lower_two_gaps": 0, "31_lower_single_gap": 0,
              "31_middle_low_v": 0, "31_middle_high_v": 0,
              "31_upper_two_gaps": 0, "31_final_single_gap": 0}
    digest = sha256()
    examples = {}
    minimum_deficits = {"pair22": None, "pair31": None}

    def record(M, h, a, c, v, result, branch):
        family = "pair22" if a == 2 else "pair31"
        counts[family] += 1
        counts[branch] += 1
        if result["minimum_ties"] > 1:
            counts["tied_post_minima"] += 1
        deficit = F(max(result["deficits"].values()), 32*M)
        margin = F(1, 16) if family == "pair22" else F(5, 96)
        require(deficit > margin, "uniform residual error lower bound")
        if minimum_deficits[family] is None or deficit < minimum_deficits[family][0]:
            minimum_deficits[family] = (deficit, [M, h, v])
        row = [M, h, a, c, v, result["minimum"], branch, result["boundaries"],
               [result["pairs"][e] for e in result["boundaries"]],
               [result["gaps"][e] for e in result["boundaries"]]]
        digest.update((json.dumps(row, separators=(",", ":"))+"\n").encode())
        if branch not in examples:
            examples[branch] = dict(M=M, h=h, v=v, maximum_positions=result["points"],
                                   scaled_post_minimum=result["minimum"],
                                   boundaries=result["boundaries"],
                                   gap_numerators=[result["gaps"][e] for e in result["boundaries"]],
                                   paired_height_numerators=[3*result["pairs"][e] for e in result["boundaries"]],
                                   height_denominator=32*M, required_error=str(deficit))

    for M in periods:
        for h in range(1, M//2+1):
            if 4*h >= M and 3*h < M:
                for v in range(1, M//2+1):
                    counts["candidates"] += 1
                    result, rejected = exact_profile(M, h, 2, 2, v)
                    if rejected:
                        counts[rejected] += 1
                        continue
                    P, G, z = result["pairs"], result["gaps"], result["minimum"]
                    if v < h:
                        branch = "22_lower"
                        require(result["boundaries"] == [h, v+h, M-h, M+v-h], "22 lower boundary order")
                        require(z == min(4*h-3*M, 4*v+4*h-4*M), "22 lower post-minimum")
                        require(P[h] == max(M, 2*M-4*v) and G[h] == 2*h-v, "22 lower witness formula")
                    else:
                        require(h < v < 2*h, "22 upper distinct-boundary interval")
                        require(z == 4*v-3*M and P[v-h] == M, "22 upper post-minimum and paired value")
                        if v < M-2*h:
                            branch = "22_upper_gap_v"
                            require(G[v-h] == v, "22 upper first gap formula")
                        else:
                            branch = "22_upper_gap_complement"
                            require(v > M-2*h and G[v-h] == M-2*h, "22 upper second gap formula")
                    record(M, h, 2, 2, v, result, branch)

            if 9*h > 4*M and 2*h < M:
                for v in range(1, M):
                    counts["candidates"] += 1
                    result, rejected = exact_profile(M, h, 3, 1, v)
                    if rejected:
                        counts[rejected] += 1
                        continue
                    P, G, z = result["pairs"], result["gaps"], result["minimum"]
                    A, B, C, D = M-h, 2*h, (v-h) % M, v
                    if v < h:
                        require(z == min(4*v-2*M, 4*h-3*M), "31 lower post-minimum")
                        require(P[A] == -z and P[D] == 4*v-M-z, "31 lower paired values")
                        if v < 3*h-M:
                            branch = "31_lower_two_gaps"
                            require(G[A]+G[D] == 2*M-3*h, "31 lower two-gap sum")
                            require(3*(P[A]+P[D]) <= 9*M, "31 lower paired sum below 9/32")
                        else:
                            branch = "31_lower_single_gap"
                            require(v > 3*h-M and z == 4*h-3*M and G[D] == h,
                                    "31 lower single-gap formula")
                            require(3*P[D] < 6*M, "31 lower single height below 3/16")
                    elif v < M-h:
                        require(h < v < M-h and z == min(-M, 4*v-3*M), "31 middle post-minimum")
                        require(G[B] == 3*h-M and P[B] == 8*h-3*M-z, "31 middle witness formula")
                        if 2*v < M:
                            branch = "31_middle_low_v"
                            require(P[B] == 4*(2*h-v), "31 middle low-v paired formula")
                        else:
                            branch = "31_middle_high_v"
                            require(P[B] == 8*h-2*M, "31 middle high-v paired formula")
                    elif v < 2*h:
                        branch = "31_upper_two_gaps"
                        require(M-h < v < 2*h and z == -M, "31 upper post-minimum")
                        require(G[A]+G[C] == 2*M-3*h and P[A] == 3*M-4*h and P[C] == 4*v-M,
                                "31 upper gap and paired-height sums")
                    else:
                        branch = "31_final_single_gap"
                        require(2*h < v < M and z == -M, "31 final post-minimum")
                        require(result["boundaries"] == [C, A, B, D], "31 final boundary order")
                        require(G[B] == 3*h-M and P[B] == 8*h-M, "31 final witness formula")
                    record(M, h, 3, 1, v, result, branch)

    require(all(counts[name] > 0 for name in counts), "all active branches and excluded degeneracies represented")
    return dict(period_range=[24, 160], extra_periods=[216, 240], counts=counts,
                examples=examples,
                minimum_observed_required_errors={name: dict(error=str(value), parameters=parameters)
                                                  for name, (value, parameters) in minimum_deficits.items()},
                profile_sha256=digest.hexdigest(),
                scope="Exact rational profiles with distinct maximum positions and four distinct boundaries. The grid tests formulas; it is not a general proof, a cycle census, or a rational-cycle control.")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="three-label-residual-geometry-v1",
                   source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                   symbolic_checks=symbolic_checks(), grid_checks=grid_checks())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    path = HERE/"check_residual_geometry.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded, "residual geometry receipt mismatch; regenerate explicitly")
    counts = receipt["grid_checks"]["counts"]
    print(json.dumps(dict(result="passed", affine_identities=len(receipt["symbolic_checks"]["identities"]),
                          pair22_profiles=counts["pair22"], pair31_profiles=counts["pair31"],
                          tied_post_minima=counts["tied_post_minima"]), sort_keys=True))


if __name__ == "__main__":
    main()
