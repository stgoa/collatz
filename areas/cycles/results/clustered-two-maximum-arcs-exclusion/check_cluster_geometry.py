"""Exact geometric certificates for two strongly clustered maximum arcs.

The polynomial identities certify the parameter-independent elimination.
The finite profile grid checks the faithful pre/post-drop conventions and
all three strict orders; it is not the general proof or a cycle census.
"""

from bisect import bisect_left
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


HERE = Path(__file__).resolve().parent
VARIABLES = ("a", "c", "u", "epsilon", "v")
ZERO = (0,)*len(VARIABLES)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def constant(value):
    return {ZERO: F(value)} if value else {}


def variable(index):
    powers = list(ZERO)
    powers[index] = 1
    return {tuple(powers): F(1)}


def add(*polynomials):
    out = {}
    for polynomial in polynomials:
        for powers, coefficient in polynomial.items():
            out[powers] = out.get(powers, F())+coefficient
    return {powers: coefficient for powers, coefficient in out.items() if coefficient}


def scale(value, polynomial):
    return {powers: F(value)*coefficient for powers, coefficient in polynomial.items()
            if value*coefficient}


def multiply(*polynomials):
    out = constant(1)
    for polynomial in polynomials:
        product = {}
        for first, x in out.items():
            for second, y in polynomial.items():
                powers = tuple(a+b for a, b in zip(first, second))
                product[powers] = product.get(powers, F())+x*y
        out = {powers: coefficient for powers, coefficient in product.items() if coefficient}
    return out


def equal(left, right, message):
    require(not add(left, scale(-1, right)), message)


def polynomial_checks():
    a, c, u, epsilon, v = [variable(i) for i in range(len(VARIABLES))]
    r = add(a, c)
    R, q = F(3, 8), F(5, 8)
    # Each I is a positive-denominator multiple of gap-J-epsilon.
    first_B = add(scale(q, v), scale(-1, multiply(add(scale(q, c), constant(R)), u)),
                  scale(-1, epsilon))
    third_case1 = add(r, scale(-1, multiply(r, v)),
                      scale(-1, multiply(r, add(scale(q, a), constant(R)), u)),
                      scale(-R, a), scale(-1, multiply(r, epsilon)))
    last_case1 = add(multiply(a, r, u), constant(-R), scale(-1, multiply(r, epsilon)))
    T = add(scale(q, a), c, constant(R+R/q))
    L = add(scale(F(5, 8), multiply(a, a)), multiply(a, c), scale(-F(15, 64), a),
            scale(-F(3, 8), c), constant(-F(117, 320)))
    coefficient = add(scale(F(129, 40), a), c, constant(F(39, 40)))
    combined = add(multiply(a, third_case1), scale(1/q, multiply(a, r, first_B)),
                   multiply(T, last_case1))
    equal(combined, add(L, scale(-1, multiply(r, coefficient, epsilon))),
          "case1 positive weighted elimination identity")

    A, C = add(a, constant(-1)), add(c, constant(-1))
    positive = add(constant(F(3, 5)), scale(F(129, 65), A), scale(F(8, 13), C),
                   scale(F(5, 8), multiply(A, A)), multiply(A, C))
    equal(add(L, scale(-F(1, 104), coefficient)), positive,
          "case1 positive residual for all a,c>=1")

    last_case2 = add(r, scale(-1, multiply(r, v)), constant(-R),
                     scale(-1, multiply(r, epsilon)))
    second_combined = add(scale(1/q, multiply(r, first_B)), last_case2)
    second_residual = add(a, constant(-F(39, 40)),
                          scale(-F(13, 5), multiply(r, epsilon)))
    cluster_margin = add(constant(1), scale(-1, multiply(r, u)))
    equal(second_combined,
          add(second_residual, multiply(add(c, constant(F(3, 5))), cluster_margin)),
          "case2 elimination with strict cluster margin")
    require(F(39, 40)+F(13, 5)/104 == 1, "case2 residual at claimed error is a-1")

    first_A = add(constant(q), scale(-1, multiply(add(scale(q, a), constant(R)), u)),
                  scale(-1, epsilon))
    third_residual = add(scale(q, c), constant(-R), scale(-1, multiply(r, epsilon)))
    equal(multiply(r, first_A),
          add(third_residual, multiply(add(scale(q, a), constant(R)), cluster_margin)),
          "case3 elimination with strict cluster margin")
    require(q-R-F(1, 104) == F(25, 104) > 0, "case3 positive residual")

    rows = []
    for r_int in range(2, 39):
        for a_int in range(1, r_int):
            c_int = r_int-a_int
            residual = (F(3, 5)+F(129, 65)*(a_int-1)+F(8, 13)*(c_int-1)
                        +F(5, 8)*(a_int-1)**2+(a_int-1)*(c_int-1))
            require(residual > 0 and F(1, 104*r_int) >= F(1, 3952),
                    "finite maximum-multiplicity constants")
            rows.append([a_int, c_int, str(residual), str(F(1, 104*r_int))])
    require(len(rows) == 703 and 104*38 == 3952, "all a+c<=38 constants")
    require(F(1, 4) > F(1, 104), "case3 stronger error")
    return dict(variables=list(VARIABLES), exact_polynomial_identities=4,
                case1_positive_coefficients_in_a_minus_1_c_minus_1={
                    "1": "3/5", "a-1": "129/65", "c-1": "8/13",
                    "(a-1)^2": "5/8", "(a-1)(c-1)": "1"},
                case2_residual_at_error="a-1",
                case3_minimum_residual_at_error="25/104",
                maximum_multiplicity_range=[2, 38], parameter_pairs=len(rows),
                uniform_error="1/3952",
                finite_constant_sha256=sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest(),
                scope="Coefficient identities and positive factors prove the elimination for every a,c>=1; the finite table only sets the uniform r<=38 constant.")


def profile_checks():
    counts = dict(candidates=0, overlapping_maximum_sets=0, coincident_boundaries=0,
                  faithful_profiles=0, aligned_minima=0, tied_minimum_profiles=0,
                  original_second_arc_wraps=0, minima_at_first_arc_end=0,
                  minima_at_second_arc_end=0, case1=0, case2=0, case3=0)
    digest = sha256()
    examples = {}
    checked_r = set()

    def check(M, h, a0, c0, v0):
        counts["candidates"] += 1
        r = a0+c0
        require(a0 >= 1 and c0 >= 1 and 0 < r*h < M, "strict cluster parameters")
        first = [(i*h) % M for i in range(a0)]
        second = [(v0+i*h) % M for i in range(c0)]
        points = sorted(first+second)
        if len(set(points)) != r:
            counts["overlapping_maximum_sets"] += 1
            return
        boundaries = [(-h) % M, first[-1], (v0-h) % M, second[-1]]
        if len(set(boundaries)) != 4:
            counts["coincident_boundaries"] += 1
            return
        counts["faithful_profiles"] += 1
        checked_r.add(r)
        if any(second[i+1] < second[i] for i in range(c0-1)):
            counts["original_second_arc_wraps"] += 1
        post = [r*x-M*(i+1) for i, x in enumerate(points)]
        minimum = min(post)
        minima = [x for x, value in zip(points, post) if value == minimum]
        if len(minima) > 1:
            counts["tied_minimum_profiles"] += 1
        for cut in minima:
            require(cut in (first[-1], second[-1]), "global post-minimum is an arc end")
            if cut == first[-1]:
                a, c, arc_A, arc_B = a0, c0, first, second
                counts["minima_at_first_arc_end"] += 1
            else:
                a, c, arc_A, arc_B = c0, a0, second, first
                counts["minima_at_second_arc_end"] += 1

            def rotate(x):
                return (x-cut-1) % M+1

            arc_A = [rotate(x) for x in arc_A]
            arc_B = [rotate(x) for x in arc_B]
            v = arc_B[-1]
            require(arc_A == [M-(a-1-i)*h for i in range(a)], "aligned first arc")
            require(arc_B == [v-(c-1-i)*h for i in range(c)] and 0 < arc_B[0] <= v < M,
                    "other arc does not wrap across the global minimum")
            ordered = sorted(arc_A+arc_B)
            aligned_post = [r*x-M*(i+1) for i, x in enumerate(ordered)]
            require(min(aligned_post) == 0 and aligned_post[-1] == 0,
                    "aligned raw profile has minimum zero")
            require(r*ordered[0] >= M, "first maximum is at least 1/r beyond the minimum")

            def before(x):
                x = (x-1) % M+1
                return r*x-M*bisect_left(ordered, x)

            def paired(x):
                return max(before(x), before(x+h))

            RA, RB = M-a*h, v-c*h
            E = sorted((RA, RB, v, M))
            require(0 < RA < M and 0 < RB < v < M and len(set(E)) == 4,
                    "four distinct positive aligned boundaries")
            require(paired(M) == M, "last paired height is exactly R/r")
            if v < RA:
                case = "case1"
                require(RB < v < RA < M, "case1 strict order")
                require(paired(RB) == r*(v-(c-1)*h), "case1 first B paired value")
                require(paired(RA) == M*a-r*(a-1)*h, "case1 first A paired value")
            elif RB < RA:
                case = "case2"
                require(RB < RA < v < M, "case2 strict order")
                require(paired(RB) == r*(v-(c-1)*h), "case2 first B paired value")
            else:
                case = "case3"
                require(RA < RB < v < M, "case3 strict order")
                require(paired(RA) == r*(M-(a-1)*h), "case3 first A paired value")
            counts[case] += 1
            counts["aligned_minima"] += 1
            gaps = [(e-E[i-1]) % M for i, e in enumerate(E)]
            paired_values = [paired(e) for e in E]
            deficits = [8*r*gap-3*height for gap, height in zip(gaps, paired_values)]
            # Actual epsilon is max(deficits)/(8*r*M). This is >1/(104r).
            require(13*max(deficits) > M, "strict geometric error obstruction")
            row = [M, h, a0, c0, v0, cut, a, c, v, case, E, deficits]
            digest.update((json.dumps(row, separators=(",", ":"))+"\n").encode())
            if case not in examples:
                examples[case] = dict(M=M, h=h, a=a, c=c, v=v, boundaries=E,
                                      gap_numerators=gaps, profile_denominator=8*r*M,
                                      paired_height_numerators=[3*x for x in paired_values],
                                      required_error=str(F(max(deficits), 8*r*M)))

    for r in range(2, 39):
        M = 4*r+1
        for a in range(1, r):
            c = r-a
            for h in (1, 2, 3):
                for v in range(1, M):
                    check(M, h, a, c, v)
    # This faithful profile has two tied post-drop minima. Both choices
    # are normalized and checked, rather than silently choosing one.
    check(100, 1, 1, 1, 50)
    require(checked_r == set(range(2, 39)), "every multiplicity represented")
    require(all(counts[key] > 0 for key in ("case1", "case2", "case3",
                "minima_at_first_arc_end", "minima_at_second_arc_end",
                "tied_minimum_profiles", "original_second_arc_wraps",
                "overlapping_maximum_sets", "coincident_boundaries")),
            "active profile and rejected-boundary cases all represented")
    return dict(counts=counts, grid="2<=r<=38; a=1,...,r-1; M=4r+1; h in{1,2,3}; v=1,...,M-1",
                extra_tied_minimum_parameters=[100, 1, 1, 1, 50],
                examples=examples, profile_sha256=digest.hexdigest(),
                scope="Exact profiles of two disjoint finite orbit segments with four distinct boundaries; no integer cycle or universal enumeration claimed.")


def singleton_checks():
    R = F(3, 8)
    require((1-2*R)/4 == F(1, 16), "singleton first-order threshold")
    require((1-3*R+R*R)/(2*(2-R)) == F(1, 208), "singleton second-order threshold")
    require(F(1, 104*2) == F(1, 208), "cluster threshold matches singleton relaxation")
    u, v = F(1, 2), F(21, 26)
    E = [F(0), v-u, 1-u, v]

    def height(x, peak):
        x %= 1
        if x == 0:
            return R/2
        if x <= peak:
            return R*x
        return R*(x-F(1, 2))

    gaps = [(x-E[i-1]) % 1 for i, x in enumerate(E)]
    values = [max(height(x, v), height(x+u, v)) for x in E]
    require(gaps == [F(5, 26), F(4, 13), F(5, 26), F(4, 13)], "sharp control gaps")
    require(values == [F(3, 16), F(63, 208), F(3, 16), F(63, 208)],
            "sharp control pre-drop paired values")
    require(all(gap-value == F(1, 208) for gap, value in zip(gaps, values)),
            "all four sharp control witnesses")
    # v+u=1 is a branch boundary; at the wrap use the pre-drop value.
    wrap_u, wrap_v = F(2, 5), F(3, 5)
    require(wrap_u+wrap_v == 1 and height(wrap_u+wrap_v, wrap_v) == F(3, 16),
            "wrap boundary partner uses the pre-drop value")
    wrap_points = [F(0), wrap_v-wrap_u, wrap_v]
    wrap_values = [max(height(x, wrap_v), height(x+wrap_u, wrap_v)) for x in wrap_points]
    require(wrap_values == [F(3, 16), F(9, 40), F(9, 40)],
            "all three wrap-boundary paired maxima")
    return dict(R=str(R), thresholds=["1/16", "1/208"],
                sharp_relaxed_control=dict(u=str(u), v=str(v), boundaries=list(map(str, E)),
                                           gaps=list(map(str, gaps)), paired_heights=list(map(str, values)),
                                           each_gap_minus_height="1/208"),
                wrap_boundary_control=dict(u=str(wrap_u), v=str(wrap_v),
                                           endpoints=list(map(str, wrap_points)),
                                           paired_heights=list(map(str, wrap_values)),
                                           wrapped_partner_height="3/16"),
                scope="Exact rational continuous control, not a cycle; u=1/2 is outside the strict clustered regime.")


def main():
    require(sys.argv[1:] in ([], ["--write-receipt"]), "usage: script [--write-receipt]")
    receipt = dict(schema="clustered-two-maximum-arcs-geometry-v1",
                   source_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                   polynomial_checks=polynomial_checks(), profile_checks=profile_checks(),
                   singleton_checks=singleton_checks())
    encoded = json.dumps(receipt, sort_keys=True, indent=2)+"\n"
    path = HERE/"check_cluster_geometry.json"
    if sys.argv[1:]:
        path.write_text(encoded)
    else:
        require(path.read_text() == encoded, "geometry receipt mismatch; regenerate explicitly")
    print(json.dumps(dict(result="passed", polynomial_identities=receipt["polynomial_checks"]["exact_polynomial_identities"],
                          parameter_pairs=receipt["polynomial_checks"]["parameter_pairs"],
                          faithful_profiles=receipt["profile_checks"]["counts"]["faithful_profiles"],
                          aligned_minima=receipt["profile_checks"]["counts"]["aligned_minima"]), sort_keys=True))


if __name__ == "__main__":
    main()
