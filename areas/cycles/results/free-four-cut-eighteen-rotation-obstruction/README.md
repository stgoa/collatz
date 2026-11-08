---
id: free-four-cut-eighteen-rotation-obstruction
kind: result
title: Eighteen rotations force an error for four arbitrary cuts
status: written
claim: >
  Pure circle geometry, with no map, orbit, integrality or clock hypothesis.
  Let 0<h<1/2 and j*h be nonintegral for every 1<=j<=18; in particular,
  rational h may have any reduced denominator greater than 18. Let C be
  any four distinct points modulo 1. Put f(0)=1, f(x)=x for 0<x<1, and
  C_j=union(C-i*h:0<=i<j), with coincident cuts removed. If every circular
  gap ending at e in C_j satisfies gap_j(e)<=3/8*max(f(e),f(e+j*h))+epsilon
  for all 1<=j<=18, then epsilon>=1/10000. An exact rational certificate
  exhausts the generic five-variable branch tree; a one-sided cut
  perturbation at fixed h covers all boundary configurations. An exact
  rational control of rotation order 14751 satisfies all seventeen-rotation
  inequalities with strictly negative error. No cycle exclusion is claimed.
authors:
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex directing research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
certificates: [check_free_cuts.py]
evidence:
  - "free_cut_duals.json: exact nonnegative rational combinations of affine inequalities"
  - "check_free_cuts.json: complete standard-library replay, hashes and exact controls"
tags: [cycles, circle-geometry, multirotation, exact-certificates, four-cuts]
---

# Eighteen rotations force an error for four arbitrary cuts

## Statement

This result concerns points on a circle and a specified function. It has
no orbit, map or clock hypothesis. Write `{x}` for fractional part and set

```
0<h<1/2,       j*h is not an integer for 1<=j<=18,
f(0)=1,        f(x)=x for 0<x<1.                         (1)
```

For rational `h`, the condition in (1) is exactly that its reduced
denominator is greater than 18. Irrational `h` is also allowed. Every
argument of `f` is reduced modulo 1.

Let `C` be any four distinct points of the circle. For `j=1,...,18`, let

```
C_j = union { {{c-i*h}: c in C} : 0<=i<j }.              (2)
```

These are sets: coincident points are retained only once. For a point `e`
in `C_j`, `gap_j(e)` is the positive circular distance from the preceding
distinct point of `C_j` to `e`. Define its paired-end deficit by

```
D_j(e) = gap_j(e)-(3/8)*max(f(e),f({e+j*h})).             (3)
```

Then

```
max { D_j(e): 1<=j<=18, e in C_j } >= 1/10000.          (4)
```

Equivalently, simultaneous inequalities `D_j(e)<=epsilon` force
`epsilon>=1/10000`. The four cuts are free: none is required to be zero,
a translate of another cut, a maximum, or a distinguished orbit position.
No optimality of the coefficient or the positive margin is asserted.

Seventeen rotations do not suffice for the same conclusion, even at
zero error and within the rotation-order range in (1). An exact control is

```
h = 5734/14751,
C = {3283/14751, 2347/4917, 932/1341, 0}.                (5)
```

Its maximum deficit over `j=1,...,17` is `-11/10728`. At `j=18` its maximum
deficit is `235/14751>0`. This is a geometric configuration, not a cycle.

## Proof

Put `eta=1/10000`. We first exclude a strict generic configuration with
all `D_j(e)<eta`. We then show that any configuration violating (4)
can be perturbed to such a generic one.

### 1. The generic affine problem has five variables

Relabel the free cuts in increasing order. In generic configurations,
the five variables lie in

```
0<h<1/2,       0<c_1<c_2<c_3<c_4<1.                    (6)
```

For each `j`, no raw cut in (2) is zero, two raw cuts do not coincide,
and no partner `{e+j*h}` is zero. Also `j*h` is nonintegral. A generic
configuration therefore has exactly `4j` cuts in `C_j`.

Within a choice of wraps and circular orders, all cuts, gaps and paired
heights are affine expressions in these five variables. The replay
constructs every such choice without sampling the parameter region.
It carries three items from rotation `j` to rotation `j+1`:

- the sorted list of all normalized cuts in `C_j`;
- the four normalized cuts in the last layer `C-(j-1)h`;
- `delta_j={j*h}`, an affine expression constrained to `(0,1)`.

At `j=1`, the sorted list and last layer are `(c_1,c_2,c_3,c_4)`, and
`delta_1=h`. Suppose a last-layer cut has representative `e` in `(0,1)`.
Its successor-layer cut is `{e-h}`. Since `-1/2<e-h<1`, the only possible
representatives are

```
e-h,       e-h+1,                                      (7)
```

each constrained to `(0,1)`. Every possible insertion rank of this new
cut in the preceding sorted list is visited. Comparisons with its two
neighbors, or its one neighbor at an end, enforce that rank. The old
order is retained, so no compatible order is omitted. The four new
cuts are inserted one at a time.

Similarly `0<delta_j+h<3/2`, so the next normalized displacement is one
of

```
delta_j+h,       delta_j+h-1,                           (8)
```

again constrained to `(0,1)`. Thus (7)--(8), together with all insertion
ranks, exhaust the wrap and order choices at every rotation.

### 2. One split determines all paired heights

Fix a sorted list `e_1<...<e_(4j)` and `delta=delta_j`. In a generic cell,
no cut equals `1-delta`. Therefore

```
max(f(e),f({e+j*h})) = e+delta   if e<1-delta,
                      e         if e>1-delta.           (9)
```

The replay enumerates all `4j+1` positions of this threshold in the
sorted list. Its comparisons with the neighboring cuts determine the
branch in (9) for every cut simultaneously.

The gap ending at `e_i` is `e_i-e_(i-1)` for `i>1`, and the gap ending
at `e_1` is `1+e_1-e_(4j)`. The constraints

```
gap-(3/8)*paired_height < eta                           (10)
```

are now strict affine inequalities. They are retained, together with
all domain, wrap, order and threshold constraints, when later rotations
are processed. A completed rotation advances to the next one only if
no exact contradiction has yet been supplied.

### 3. Exact combinations close the whole branch tree

Represent every strict affine inequality as

```
a_i dot (h,c_1,c_2,c_3,c_4) < b_i.                     (11)
```

Rows are cleared to integer coefficients and divided by their positive
common divisor. Their signs are never reversed. For a finite set of rows,
a contradiction is certified by rational weights with

```
w_i>=0,       sum(w_i)=1,
sum(w_i*a_i)=0,       sum(w_i*b_i)<=0.                  (12)
```

Indeed, the weighted sum of (11) would give
`0<sum(w_i*b_i)<=0`. This also covers combinations whose final right side
is zero, because at least one strictly positive weight occurs.

The committed data contain 4,708 combinations of this form. The checker
validates every weight, coefficient cancellation and final right side
with exact rational arithmetic. When rebuilding the branch tree, it
may use a combination only if every row in its positive support is
present in the current branch. Previously learned combinations are
therefore reusable without trusting the branch in which they were found.

The complete replay makes 29,781 branch-extension queries and closes
27,924 of them with exact combinations. It has no surviving branch after
rotation 18. A branch without an available combination is kept and
extended; reaching the eighteenth rotation without a contradiction is
an explicit failure of the certificate. There is no sampling or search
limit in this replay. A negative constant right side can also close an
impossible constant row; ignoring other constant rows only weakens the
replay and cannot create a false contradiction.

Sections 1--2 show that any generic configuration satisfying all (10)
would follow at least one branch. Section 3 closes every such branch.
This proves the generic obstruction.

### 4. Fixed-h perturbations cover all collisions and wraps

Suppose now that (4) fails at a possibly nongeneric configuration. Since
there are finitely many deficits, they are all at most some
`epsilon<eta`. Keep `h` fixed throughout this step.

Move each of the four base cuts a sufficiently small negative distance,
with the four distances chosen generically. Equivalently, first apply a
common small left displacement and then much smaller independent
perturbations. Every expression `c_l+k*h` that was an integer approaches
that integer from the left. Its `f` value therefore tends to `1`, the
specified value at zero. All other endpoint and partner values vary
continuously at the original configuration.

The required genericity at fixed `h` is possible. Two raw cuts arising
from the same base cut in one `C_j` differ by `t*h` for an integer
`0<|t|<=j-1<=17`. They cannot coincide by (1). Coincidences arising from
different base cuts, as well as endpoint and partner wraps, are proper
affine hyperplanes in the four cut variables. A generic choice of the
four small left displacements avoids their finite union. The values
`delta_j` remain in `(0,1)` because `h` is unchanged. After relabeling the
perturbed cuts, (6) holds. Distinctness of the original four cuts is
preserved.

For completeness, consider a cluster of coincident raw cuts in an
original `C_j`. After perturbation, each old positive gap is approached
by one gap ending at a member of the corresponding split cluster. Its
endpoint and partner heights tend to the original values, including
the pre-drop value at zero. The extra gaps within a split cluster tend
to zero. Their deficits have nonpositive limits, because the paired
heights are nonnegative. Thus these new deficits are below the positive
`eta`, while each old positive-gap deficit tends to a value at most
`epsilon<eta`.

Only finitely many cuts, partners and rotations occur. All deficits are
therefore strictly below `eta` after a sufficiently small generic
perturbation. This contradicts section 3 and proves (4). In particular,
rational rotation orders 19 through 35 require no additional strata:
no perturbation of `h`, second anchor, or enlarged order hypothesis was
used.

### 5. The shorter-horizon control

The checker forms all sets `C_j` for (5), removes duplicates, computes
every circular gap, and evaluates both heights with exact fractions.
It returns

```
max_(1<=j<=17,e in C_j) D_j(e) = -11/10728,
max_(e in C_18) D_18(e) = 235/14751.                    (13)
```

The reduced denominator of `h` is 14751. Hence this control satisfies
(1) and proves that replacing eighteen by seventeen in (4) is false,
even with zero in place of the positive right side.

## Certificates

[`check_free_cuts.py`](check_free_cuts.py) is self-contained and uses only
Python's standard library. It reads the exact mathematical data in
[`free_cut_duals.json`](free_cut_duals.json), validates (12), and
independently reconstructs the entire five-variable branch tree described
above. It does not import a numerical solver or the discovery program.
The proof-data file is below 1 MB. Its row table, weights and gaps have
no machine paths, execution times or discovery-dependent branch claims.

The generated receipt [`check_free_cuts.json`](check_free_cuts.json)
records the proof-artifact hash, exact combination and branch counts, zero
survivors, and direct geometric controls. An additional order-30 control
checks the fixed-h, one-sided perturbation across wraps and coincident
cuts; it illustrates the boundary argument without replacing it.
The default command verifies
the committed receipt; `--write-receipt` regenerates it.

Run from the repository root with Python 3.10 or later:

```
python3 areas/cycles/results/free-four-cut-eighteen-rotation-obstruction/check_free_cuts.py
python3 -O areas/cycles/results/free-four-cut-eighteen-rotation-obstruction/check_free_cuts.py
```

Numerical linear programming was used only to discover useful supports.
The discovery environment used NumPy and SciPy. Neither a numerical
infeasibility report nor a claimed discovery status authorizes a replay
prune: the checked rational identity and the actual row inclusion do.
The mathematical finite step is the complete exact replay, independently
implemented from the branch description.

## Remarks

The multirotation strategy and the need to retain the pre-drop value
already occur in
[`multi-rotation-four-mismatch-exclusion`](../../attempts/multi-rotation-four-mismatch-exclusion/README.md).
The earlier exact result
[`single-sawtooth-multirotation-obstruction`](../single-sawtooth-multirotation-obstruction/README.md)
uses cuts of the special form `{0,-h,p,q}` and eleven rotations. The
present statement removes that cut alignment and checks eighteen
rotations instead. These links credit context; the proof above is
self-contained and uses neither result as an assumption. Novelty
undetermined.

This node supplies a geometric obstruction only. A cycle application
must separately prove its height envelope, the relation between raw cuts
and actual mismatches, agreement-subinterval witnesses at every raw cut,
and a sufficiently small error budget. It must also ensure that each
rotation used is nonidentity. No such cycle transfer is assumed here.
In particular no conclusion about `3x+1` or the actual `3x+5,7,13,61`
cycles follows by silently changing their addends or omitting those
additional hypotheses.

## History

- 2026-11-08: an exact rational countercontrol invalidated the proposed
  sixteen-rotation obstruction. Retaining eighteen rotations instead
  produced a complete rational branch certificate for four free cuts.
  Added the fixed-h boundary argument and the strict seventeen-rotation
  control. Status is `written`; independent implementations and audits
  within this authoring session are not an independent-session review.
