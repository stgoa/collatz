# C006 — Few height changes force large cycle gaps

**Progress; the all-cycle headline and the ordered-cycle exclusion remain
open.** The new result is a written denominator restriction for every
primitive ordered cycle in the declared domain. It does not assume a
repeated-block decomposition. With a classical logarithm bound, it gives
effective finiteness when denominator and height-change count are
bounded, with no separate height bound. No numerical cutoff or novelty is claimed.

## The mechanism and what it proves

Use the raw positive odd-only map, without absorption. Represent a
rational `3x+1` cycle by odd numerators `n_i` and common reduced
denominator `q`, so `3n_i+q=2^a_i n_(i+1)` with exact `a_i>=1`.
Let `m>1` be its primitive odd period, `A=sum a_i`, and `L=min n_i`.
Assume `q<=L` and that the normalized successor preserves circular
order. This domain includes every denominator-one cycle with that
order property.

Remove powers of two to put each state into `[L,2L)`. Retain its height
`h_i=floor(log_2(n_i/L))`, and put `B=max h_i`. In sorted normalized
order let `J` be one plus the number of adjacent height changes. The
extra one is the dyadic seam; it cannot be discarded.

For positive gaps scaled to integers, each edge without a height change
satisfies `2^c G_next=3G`, with `c` equal to one or two. The successor
rank shift visits every gap. Among its `J` runs there is one of length
at least `ceil(m/J)−1`; binary divisibility makes its first gap large.
The [proof](ORDER_RIGIDITY.md) gives

```
L > 2^(ceil(m/J)−1−B),
q > (D/C_lower(A,m)) 2^(ceil(m/J)−1−B),
q > (3 delta/m) 2^(ceil(m/J)−1−B),

D=2^A−3^m,  delta=A log 2−m log 3>0.
```

An exact run can improve the exponent from its length to the sum `E`
of its one/two exponents. This gives the rational bound
`q>(D/C_lower)2^(E−B)`, checked without floating-point logarithms.

There is a further elementary gain: chronological height can rise by at
most one at each odd step. Reaching height B from zero therefore visits
all B+1 height labels. A sorted list with that many distinct labels needs
at least B changes, so `B+1<=J`. A separate height bound is redundant.

The inspected statement of the classical two-logarithm theorem supplies
`delta>=c_0 m^(-K_0)` for effective absolute constants. Therefore:

- For any fixed upper bounds on `q,J`, only finitely many such cycles
  exist, effectively in principle, with no separate height bound.
- At fixed `q`, the number `J` is at least `sqrt(m)-O_q(log m)`;
  in particular it grows at least on the order of the square root of
  the period.
- At fixed `q,B`, the earlier stronger bound `J=Omega(m/log m)` remains.
  It also holds if `B=O(log m)`, with constants depending on that bound.

This is a restriction on the complexity of a possible cycle. It leaves
finite exceptions and profiles whose number of height changes grows. It does not exclude every ordered denominator-one cycle, or prove
finiteness at a fixed denominator without the change-count bound.

## A concrete gain and the comparison baseline

The actual `q=233` cycle

```
1663,2611,4033,3083,4741,1807,2827,4357
```

has valuations `(1,1,2,1,3,1,1,3)`, maximum height `B=1`, and `J=3`.
A zero-forcing run has length five and exponent sum eight. Thus
`q>208768/14501`, or `q>=15`. The height-histogram bound gives only
`q>=2` on that same profile. Both permit the actual cycle.

The histogram bound uses odd-state packing and a mechanical minimum
upper bound. A cyclic-prefix argument proves that upper bound for
**all** positive cycles, whether ordered or not. C006 explicitly records
it as a generic comparison, rather than crediting it to circular order.
The new gap argument uses the order hypothesis. Neither finite
comparison establishes novelty or domination over every existing bound.

## Failed shortcuts retained as exact controls

| Proposed shortcut | Exact obstruction |
| --- | --- |
| Mechanical normalized exponents and correct heights imply order | A primitive `q=1909`, period-seven cycle has both properties but two inversions. |
| One legal height defect preserves the mechanical unit gcd | A `q=233`, period-eight cycle with one height-one state has cancellation factor seven. |
| Some normalized pair has primitive odd gap at most q | The ordered `q=13` cycle `(227,347,527,797,601)` has minimum odd gap fifteen across all pairs. |
| A wide cycle loses at least one unit from the mechanical minimum | The `q=5` cycle `(19,31,49)` loses only `4/5`. |
| Ordered affine equations with integer coordinates suffice | `4→13→5→4` has q1 and ordered normalized equations, but an even state, a zero valuation and a nonexact final division. Strict validators reject it. |

The conjectural diagnostic `B<=q−1` survived the bounded sample. It has
no proof here and is not used in any result. The earlier q5 period-17
and q233 controls still rule out ignoring large intercept cancellation.

## Evidence and verification

- [ORDER_RIGIDITY.md](ORDER_RIGIDITY.md): definitions, proofs, controls,
  generic comparisons and the seven-field mechanism assessment.
- [INDEPENDENT_REVIEW.md](INDEPENDENT_REVIEW.md): separate argument
  review; its scope is distinct from formal verification.
- [check_order_rigidity.py](check_order_rigidity.py) and
  [order_rigidity_audit.json](order_rigidity_audit.json): exact finite
  checks and reproducible receipt. Coverage and root replay are recorded
  in [ROOT_REVIEW.md](ROOT_REVIEW.md).
- [LITERATURE.md](LITERATURE.md): inspected primary statement for the
  analytic corollary and scoped comparison with earlier results.
- [SIDE_REVIEW.md](SIDE_REVIEW.md): side input and Fable/Lean scope.
- [delivery_checks.json](delivery_checks.json): preservation, local-link
  and verification outcomes; [DELIVERY_STATUS.md](DELIVERY_STATUS.md)
  records publication separately.

The checker covers all 2,459 stored source cycles at 333 parameters,
their 1,184 distinct normalized cycles, and all eleven raw fixtures.
Fifty nontrivial normalized cycles satisfy the order domain, forty-six
of them wide. A separate exhaustive grid constructs 360,618 legal odd
cycles and distinguishes minimum-phase failure, height inconsistency
and order failure. Exactly 317,459 profiles meet the ordered domain.
Finite success is not a proof for untested periods or heights.

## Recommended high-level target

**Exclude denominator one for every nontrivial cycle whose normalized
successor preserves circular order, with no bound on period, height or
height-change count.** This is an intermediate target under the existing
all-cycle goal; it does not replace that goal. No proof places every
hypothetical integer cycle in the ordered class.

The next mechanism must use the actual height jumps and their locations
to obstruct total numerator cancellation, or convert the required
growth in height complexity into a contradiction specific to q1.
Extending a list of bounded scans alone does not meet this target.
Testing one-defect profiles for an all-period exclusion is a bounded
way to probe that arithmetic mechanism, with the q233 control retained.

Fable's reported Lean checks provide useful assurance for completed
algebra. Main has not independently replayed the latest reported
builds, and they supply no missing mathematical implication in C006.
