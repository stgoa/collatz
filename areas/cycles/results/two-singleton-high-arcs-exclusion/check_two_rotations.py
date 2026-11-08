"""Complete exact affine-cell proof for two singleton high positions.

The three cut families exhaust opposite and both aligned adjacent placements.
Every branch is checked on all vertices of its complete closed cell. Samples
select formulas; they never certify their validity. Rational duals prove the
finite geometric obstruction. Integer grids are additional controls only.
"""
from fractions import Fraction as F
from itertools import combinations, product
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
R = F(3, 8)
VALIDATIONS = 0

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def af(c=0, u=0, v=0):
    return tuple(map(F, (c, u, v)))

def add(a, b):
    return tuple(x+y for x, y in zip(a, b))

def scale(k, a):
    return tuple(k*x for x in a)

def sub(a, b):
    return add(a, scale(-1, b))

def value(a, p):
    return a[0]+a[1]*p[0]+a[2]*p[1]

def nonnegative(a, vertices, message):
    global VALIDATIONS
    require(all(value(a, p) >= 0 for p in vertices), message)
    VALIDATIONS += len(vertices)

def zero(a, vertices, message):
    nonnegative(a, vertices, message)
    nonnegative(scale(-1, a), vertices, message)

def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def solve(a, b):
    det = determinant(a)
    if not det:
        return None
    return tuple(determinant([[b[i] if j == k else a[i][j] for j in range(3)]
                              for i in range(3)])/det for k in range(3))

def clip(poly, line):
    out = []
    for i, p in enumerate(poly):
        q = poly[(i+1) % len(poly)]
        x, y = value(line, p), value(line, q)
        if x >= 0:
            out.append(p)
        if x*y < 0:
            t = x/(x-y)
            out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
    return list(dict.fromkeys(out))

def centroid(points):
    return tuple(sum(p[j] for p in points)/len(points) for j in range(2))

def area(poly):
    return sum(p[0]*poly[(i+1) % len(poly)][1]-p[1]*poly[(i+1) % len(poly)][0]
               for i, p in enumerate(poly))

RECT = [(F(0), F(0)), (F(1, 2), F(0)), (F(1, 2), F(1)), (F(0), F(1))]
BASE = [af(0, 1), af(F(1, 2), -1), af(0, 0, 1), af(1, 0, -1)]

def rawpoints(kind, j):
    if kind == "opposite":
        base = [af(), af(0, -1), af(0, 0, 1), af(0, -1, 1)]
    else:
        side = 1 if kind == "adjacent_plus" else -2
        base = [af(), af(0, -1), af(0, side), af(0, 0, 1)]
    return list(dict.fromkeys(add(p, af(0, -i)) for p in base for i in range(j)))

def normalize_line(line):
    if not any(line[1:]):
        return None
    pivot = next(x for x in line if x)
    return scale(1/pivot, line)

def dividing_lines(kind):
    if kind == "opposite":
        return [af(0, -1, 1), af(0, -2, 1), af(1, -1, -1), af(1, -2, -1)]
    lines = set()
    # Every raw coordinate and partner lies strictly between -4 and 4.
    # Coordinate equality modulo one is a difference hitting an integer.
    for j in (1, 2):
        raw = rawpoints(kind, j)
        expressions = raw+[add(p, af(0, j)) for p in raw]
        expressions += [sub(a, b) for a, b in combinations(raw, 2)]
        for expression in expressions:
            vals = [value(expression, p) for p in RECT]
            require(min(vals) >= -4 and max(vals) <= 4, "complete integer crossing range")
            for integer in range(-4, 5):
                line = normalize_line(sub(expression, af(integer)))
                if line is not None:
                    vals = [value(line, p) for p in RECT]
                    if min(vals) < 0 < max(vals):
                        lines.add(line)
    return sorted(lines)

def proper(kind, p):
    u, v = p
    return (0 < u < F(1, 2) and 0 < v < 1
            and len({value(x, p) % 1 for x in rawpoints(kind, 1)}) == 4)

def sign(x):
    return (x > 0)-(x < 0)

def all_cells(kind, lines):
    cells = [RECT]
    for line in lines:
        new = []
        for poly in cells:
            for direction in (-1, 1):
                pp = clip(poly, scale(direction, line))
                if len(pp) >= 3 and area(pp):
                    new.append(pp)
        cells = new
    # The finite arrangement consists of polygon interiors, open edges, and
    # vertices. Boundary strata with fewer than four h-cuts are excluded.
    edges = {tuple(sorted((p, poly[(i+1) % len(poly)])))
             for poly in cells for i, p in enumerate(poly)}
    vertices = {p for poly in cells for p in poly}
    candidates = cells+[list(e) for e in sorted(edges)]+[[p] for p in sorted(vertices)]
    output = {}
    for poly in candidates:
        sample = centroid(poly)
        if not proper(kind, sample):
            continue
        signature = tuple(sign(value(line, sample)) for line in lines)
        require(signature not in output, "each relatively open cell occurs exactly once")
        conditions = list(BASE)
        for s, line in zip(signature, lines):
            conditions.extend([scale(s, line)] if s else [line, scale(-1, line)])
        for condition in conditions:
            nonnegative(condition, poly, "cell vertices obey every domain half-plane")
        output[signature] = (poly, sample, conditions)
    return output

def affine_witnesses(kind, sample, vertices):
    result = []
    for j in (1, 2):
        keyed = {}
        for raw in rawpoints(kind, j):
            representative = sub(raw, af(value(raw, sample)//1))
            x = value(representative, sample)
            nonnegative(representative, vertices, "representative lower wrap boundary")
            nonnegative(sub(af(1), representative), vertices, "representative upper wrap boundary")
            if x == 0:
                zero(representative, vertices, "zero branch is identical on the whole stratum")
                representative = af()
            if x in keyed:
                zero(sub(representative, keyed[x]), vertices, "deduplication holds on the whole stratum")
            else:
                keyed[x] = representative
        points = [keyed[x] for x in sorted(keyed)]
        if j == 1:
            require(len(points) == 4, "four distinct genuine h boundaries")
        for a, b in zip(points, points[1:]):
            nonnegative(sub(b, a), vertices, "cut order holds over the complete cell")
        for i, endpoint in enumerate(points):
            gap = sub(endpoint, points[i-1])
            if i == 0:
                gap = add(gap, af(1))
            nonnegative(gap, vertices, "all circular gaps are nonnegative")
            raw = add(endpoint, af(0, j))
            raw_value = value(raw, sample)
            integer = raw_value//1
            if raw_value == integer:
                zero(sub(raw, af(integer)), vertices, "partner zero is an identity on the stratum")
                partner = af(1)  # pre-drop value, including wrap at one
            else:
                partner = sub(raw, af(integer))
                nonnegative(partner, vertices, "partner lower wrap boundary")
                nonnegative(sub(af(1), partner), vertices, "partner upper wrap boundary")
            current = af(1) if value(endpoint, sample) == 0 else endpoint
            high, other = sorted((current, partner), key=lambda x: value(x, sample), reverse=True)
            nonnegative(sub(high, other), vertices, "paired maximum branch over the complete cell")
            deficit = sub(gap, scale(R, high))
            result.append((f"j{j}:end={value(endpoint, sample)}", deficit))
    return result

def dual_certificate(conditions, witnesses):
    constraints = [((x[1], x[2], F(0)), -x[0]) for x in conditions]
    constraints += [((-x[1], -x[2], F(1)), x[0]) for _, x in witnesses]
    best = None
    for indices in combinations(range(len(constraints)), 3):
        matrix = [[constraints[k][0][i] for k in indices] for i in range(3)]
        weights = solve(matrix, [F(0), F(0), F(1)])
        if weights is None or min(weights) < 0:
            continue
        bound = sum(w*constraints[k][1] for w, k in zip(weights, indices))
        if best is None or bound > best[0]:
            best = bound, indices, weights
    require(best is not None and best[0] > 0, "positive nonnegative rational dual exists")
    bound, indices, weights = best
    lhs = tuple(sum(w*constraints[k][0][j] for w, k in zip(weights, indices)) for j in range(3))
    require(lhs == (0, 0, 1), "dual cancels both parameters and normalizes epsilon")
    require(sum(w*constraints[k][1] for w, k in zip(weights, indices)) == bound,
            "exact dual right side")
    return bound, [[k, str(w)] for k, w in zip(indices, weights) if w]

def direct_deficits(kind, p):
    u, _ = p
    output = []
    for j in (1, 2):
        points = sorted({value(x, p) % 1 for x in rawpoints(kind, j)})
        for i, e in enumerate(points):
            gap = e-points[i-1]+(1 if i == 0 else 0)
            partner = (e+j*u) % 1
            height = max(e if e else F(1), partner if partner else F(1))
            output.append(gap-R*height)
    return output

def controls(kind, lines, cells):
    count = crossings = 0
    covered = set()
    for denominator in range(5, 49):
        for h in range(1, (denominator+1)//2):
            for position in range(1, denominator):
                p = F(h, denominator), F(position, denominator)
                if not proper(kind, p):
                    continue
                signature = tuple(sign(value(line, p)) for line in lines)
                require(signature in cells, "integer grid belongs to a certified stratum")
                _, _, _, witnesses, bound = cells[signature]
                actual = direct_deficits(kind, p)
                calculated = [value(x, p) for _, x in witnesses]
                require(actual == calculated and max(actual) >= bound, "direct cut/partner arithmetic")
                covered.add(signature)
                count += 1
                crossings += signature.count(0) >= 2
    require(covered == set(cells), "all strata exercised by direct grid controls")
    return dict(profiles=count, intersection_profiles=crossings, all_strata_covered=len(covered),
                scope="All faithful integer pairs on denominators 5..48; controls, not the coverage proof.")

def build():
    global VALIDATIONS
    VALIDATIONS = 0
    rows = []
    expected = {"opposite": (8, 6, 1, F(5, 2384)),
                "adjacent_plus": (11, 9, 1, F(1, 168)),
                "adjacent_minus": (11, 9, 1, F(1, 232))}
    for kind in expected:
        lines = dividing_lines(kind)
        cells = all_cells(kind, lines)
        saved, counts = [], [0, 0, 0]
        ready = {}
        for signature, (poly, sample, conditions) in cells.items():
            dimension = 2 if len(poly) >= 3 else len(poly)-1
            counts[2-dimension] += 1
            witnesses = affine_witnesses(kind, sample, poly)
            bound, dual = dual_certificate(conditions, witnesses)
            ready[signature] = (poly, sample, conditions, witnesses, bound)
            saved.append(dict(signature=list(signature), dimension=dimension,
                              vertices=[[str(v) for v in p] for p in poly],
                              sample=list(map(str, sample)),
                              conditions=[list(map(str, x)) for x in conditions],
                              witnesses=[dict(name=name, deficit=list(map(str, x))) for name, x in witnesses],
                              epsilon_lower=str(bound), dual=dual))
        bound = min(item[4] for item in ready.values())
        require(tuple(counts)+(bound,) == expected[kind], "complete placement-specific cell counts and minimum")
        rows.append(dict(placement=kind, dividing_lines=[list(map(str, x)) for x in lines],
                         strata_counts=dict(open_cells=counts[0], open_segments=counts[1], points=counts[2]),
                         epsilon_lower=str(bound), cells=saved,
                         direct_controls=controls(kind, lines, ready)))
    sharp = F(129, 298), F(65, 298)
    deficits = direct_deficits("opposite", sharp)
    require(max(deficits) == F(5, 2384) and deficits.count(F(5, 2384)) == 3,
            "sharp dominating-sawtooth relaxation")
    return dict(scope="Exact two-rotation obstruction for all placements of two high singleton arcs; not a cycle existence claim.",
                coefficient="3/8", epsilon_lower="5/2384", total_strata=57,
                full_cell_vertex_sign_checks=VALIDATIONS, placements=rows,
                sharp_relaxation=dict(u=str(sharp[0]), v=str(sharp[1]), epsilon="5/2384",
                                      all_deficits=list(map(str, deficits)), active_witnesses=3,
                                      admissible_unequal_profile=False))

if __name__ == "__main__":
    data = build()
    path = HERE/"check_two_rotations.json"
    text = json.dumps(data, indent=2, sort_keys=True)+"\n"
    if "--write" in sys.argv:
        path.write_text(text)
    else:
        require(path.read_text() == text, "generated geometry receipt differs")
    print("PASS: 57 complete strata; full-cell affine checks; exact margin 5/2384")
