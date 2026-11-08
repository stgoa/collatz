---
id: single-sawtooth-multirotation-obstruction
kind: result
title: Eleven rotations force an error in the single-sawtooth witness model
status: written
claim: >
  Pure circle geometry, with no orbit, map or clock assumption. Let
  0<h<1/2 be rational with reduced denominator greater than 12,
  let 0<p<q<1, and require the four base cuts {0,-h,p,q} modulo 1
  to be distinct. Define f(0)=1 and f(x)=x for 0<x<1. For each
  1<=j<=11 let C_j contain -i*h for 0<=i<=j and p-i*h,q-i*h for
  0<=i<j, all modulo 1, with duplicates removed. Write gap_j(e)
  for the circular gap from the preceding distinct cut to e.
  If every such gap satisfies gap_j(e)<=3/8*max(f(e),f(e+j*h))+epsilon,
  then epsilon>=1/1000. A complete exact rational branch certificate
  proves the open-cell obstruction; a pre-drop perturbation argument
  handles all faithful boundary configurations in the stated class.
  No Collatz cycle exclusion or transfer to integer states is claimed.
authors:
  - Codex directing research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex signed-endpoint formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
certificates: [check_sawtooth.py]
evidence:
  - "sawtooth_duals.json: exact rational nonnegative-combination proof data"
  - "check_sawtooth.json: complete solver-free branch replay and artifact hashes"
  - "explore_sawtooth_duals.py: optional NumPy/SciPy discovery, not used by CI or the proof replay"
tags: [cycles, circle-geometry, sawtooth, multirotation, exact-certificates]
---

# Eleven rotations force an error in the single-sawtooth witness model

## Statement

This is a theorem about a normalized function on the circle. It has no
map, orbit, integrality or clock hypothesis.

Use representatives in `[0,1)` and write `{x}` for fractional part. Let

```
0<h<1/2,   h rational with reduced denominator >12,
0<p<q<1,   {0,{-h},p,q} has four distinct points.
```

The last condition is called **faithfulness** here. In particular,
neither `p` nor `q` equals `1-h`. Define the pre-drop sawtooth

```
f(0)=1,        f(x)=x for 0<x<1.
```

Every argument of `f` below is reduced modulo 1. For `1<=j<=11`, put

```
C_j = {{-i*h}:0<=i<=j}
      union {{p-i*h},{q-i*h}:0<=i<j}.                 (1)
```

These are sets: coincident points are counted once. For `e` in `C_j`,
let `gap_j(e)` be the positive circular distance from the preceding
distinct point of `C_j` to `e`. All `C_j` contain at least two points.

For any real `epsilon`, if

```
gap_j(e) <= (3/8)*max(f(e),f({e+j*h}))+epsilon         (2)
```

holds for every `j=1,...,11` and every `e` in `C_j`, then

```
epsilon >= 1/1000.                                   (3)
```

Equivalently, at least one of the finitely many paired-end deficits
`gap_j(e)-(3/8)*max(f(e),f({e+j*h}))` is at least `1/1000`.
The coefficient `3/8` and the margin are part of the theorem; no
optimality of either is asserted.

## Proof

Write `eta=1/1000`. Suppose (2) holds with `epsilon<eta`. The proof
has two parts: an exact finite obstruction on all generic open cells,
followed by a limiting argument that preserves the pre-drop value.

### 1. Every generic branch is represented

Temporarily let `(h,p,q)` vary over the open region
`0<h<1/2, 0<p<q<1`. A generic point avoids every nonidentical affine
wrap, order or partner-comparison equality arising from (1) through
`j=11`. On a generic cell, all of the following choices are fixed:

- the integer subtracted from each raw endpoint and its partner;
- the larger of the two normalized endpoint values;
- the strict order of the normalized cuts.

The certificate constructs these choices exhaustively, rotation by
rotation. The raw endpoint and partner expressions are respectively

```
b-i*h,       b+(j-i)*h,
```

where `b=0, 0<=i<=j`, or `b=p,q, 0<=i<j`. A symbolically zero expression
is assigned the value `1`, exactly matching `f(0)`. Every other
expression `E` is assigned one of the branches

```
0<E-n<1,       n an integer.                         (4)
```

The possible integers are bounded without optimization software.
Evaluate `E` at the six vertices of the closed parameter region:

```
(h,p,q) in {0,1/2} x {(0,0),(0,1),(1,1)}.
```

If the minimum and maximum are `l,u`, every branch in (4) has
`floor(l)<=n<ceil(u)`. All integers in this range are visited.
Strict comparisons choose either endpoint as the larger one; an
identical comparison needs only one branch. Successive insertion
of each cut at every possible position enumerates all strict orders.

Once an order is fixed, the first gap is the first cut minus the last
cut plus 1; every other gap is the difference of successive cuts.
Thus every inequality

```
gap_j(e)-(3/8)*max(f(e),f({e+j*h})) < eta              (5)
```

is affine in `(h,p,q)`. Its row is retained when the search proceeds
to the next rotation. No intermediate survivor is discarded merely
because a numerical solver did not find a point.

### 2. Exact certificates discard every open branch

The rows have the form

```
A_i dot (h,p,q) < b_i.
```

To discard a branch the checker verifies rational weights satisfying

```
w_i>=0,       sum(w_i)=1,
sum(w_i*A_i)=0,       sum(w_i*b_i)<=0.                (6)
```

Taking this combination of strict inequalities would give
`0<sum(w_i*b_i)<=0`, a contradiction. The normalization ensures
that the weights are not all zero, including when the final right
side is exactly zero. Constant rows can also be rejected directly
when their right side is negative. Ignoring other constant rows
only enlarges a branch and cannot create a false contradiction.

The committed data supply 3,849 such exact combinations. The
standard-library replay visits 8,880 feasibility queries, verifies
every supplied combination, and leaves no branch after rotation 11.
If a branch has no stored combination, the checker treats it as
potentially feasible and continues enumerating it. It also requires
that every supplied combination was used. Thus the finite step is
a complete branch proof, not a sampled search for failures.

### 3. Boundary configurations preserve the pre-drop witnesses

It remains to show that an instance of (2) with `epsilon<eta` on a
wrap or collision boundary would give a strict generic instance
of (5), contradicting sections 1--2.

First hold `h` fixed and move `p` and `q` independently by sufficiently
small negative amounts. Choose these amounts generically, keeping
`0<p<q<1`. Every mixed endpoint or partner originally equal to an
integer now approaches that integer from the left. Its reduced
sawtooth value therefore tends to `1`, the required pre-drop value.
All other mixed values are continuous at the original point.

An `h`-only raw endpoint or partner is an integer multiple of `h`
with coefficient of absolute value at most 11. The reduced
denominator of `h` is greater than 12, so a nonzero such coefficient
cannot give an integer. The symbolically zero expressions remain
zero and retain value `1` exactly. After choosing the mixed
perturbations, a still smaller generic perturbation of `h` avoids
the remaining affine equalities without crossing any nonconstant
wrap boundary. All parameter inequalities and faithful base cuts
remain valid.

If several raw cuts coincide initially, they split into nearby
cuts. Each old positive gap is the limit of a gap ending at one of
the split cuts, and the paired heights tend to the original
pre-drop heights. The extra gaps tend to zero. Their deficits have
nonpositive limits, so they are strictly below the positive `eta`
for sufficiently small perturbations. The other deficits tend to
values at most `epsilon<eta`. There are only finitely many cuts and
rotations; choose the perturbations small enough for every one of
these strict inequalities at once.

This yields a generic point satisfying all (5), a contradiction.
The rational-denominator restriction is used here: it prevents
nonconstant `h`-only endpoints from requiring incompatible
one-sided approaches to zero. This proof does not silently extend
the statement to smaller denominators.

## Certificates

[`check_sawtooth.py`](check_sawtooth.py) uses only Python's standard
library and exact `Fraction` arithmetic. It reconstructs the complete
branch tree, reads [`sawtooth_duals.json`](sawtooth_duals.json), and
verifies (6) against the rows actually reconstructed. The data select
which combination to try; they cannot authorize a prune without the
coefficient and sign checks.

Each row key is the SHA-256 of compact JSON containing the reduced
integer numerator and positive denominator of every coefficient,
in row order. It does not depend on `Fraction.__repr__`, floating
point or a solver version. The hash selects data only: soundness
still comes from verifying the selected weights on the actual rows.
The generated receipt [`check_sawtooth.json`](check_sawtooth.json)
records the checker and data hashes, branch counts and zero survivors.

Run from the repository root with Python 3.10 or later:

```
python3 areas/cycles/results/single-sawtooth-multirotation-obstruction/check_sawtooth.py
python3 -O areas/cycles/results/single-sawtooth-multirotation-obstruction/check_sawtooth.py
```

The default command checks the committed receipt. The explicit
`--write-receipt` option regenerates it. The replay is also checked
with Python 3.12; no wall-clock information enters its receipt.

[`explore_sawtooth_duals.py`](explore_sawtooth_duals.py) is optional
discovery code and is not run by CI. It uses NumPy and SciPy to
suggest small supports, then checks the weights exactly before
writing data. The original discovery environment used Python 3.9.6,
NumPy 2.0.2 and SciPy 1.13.1; the repository scripts target Python
3.10 or later. No floating solver result is a proof assumption.
The committed solver-free replay is the verifier even if a different
discovery environment produces different valid supports.

To deliberately rediscover the proof data in an environment with
NumPy and SciPy installed:

```
python3 areas/cycles/results/single-sawtooth-multirotation-obstruction/explore_sawtooth_duals.py --write-proof-data
```

This overwrites the data and requires a fresh receipt and full replay.
The proof-data file is below 1 MB; it stores exact combinations rather
than a list of floating sample points.

## Remarks

This supplies the exact cell-certificate step proposed in
[`multi-rotation-four-mismatch-exclusion`](../../attempts/multi-rotation-four-mismatch-exclusion/README.md),
especially its "What survives" section. That earlier attempt recorded
grid evidence and the importance of the pre-drop convention. Its
merged claims and review history are unchanged. Novelty undetermined.

The present result is deliberately a geometric lemma. Applying it to
a valuation word would require a separate proof of the normalized
height envelope, the locations of its cuts, the error budget, and
the paired-end inequalities at every raw cut. If a raw cut set
refines the actual mismatch set, that transfer must use agreement
subintervals rather than assume every raw cut is an actual mismatch.
None of these cycle-transfer statements is proved here.

In particular this node assumes neither EXT-1 nor a published
convergence computation and claims no exclusion of any `3x+d` cycle.
It cannot be applied to the actual `3x+5,7,13,61` controls by silently
replacing their addend or assuming the missing profile transfer.

## History

- 2026-11-08: replaced the single-sawtooth model's sampled multirotation
  evidence by a complete rational branch certificate and an explicit
  pre-drop boundary-transfer argument. Kept the claim geometric and
  the status `written`; same-session checks are not an independent review.
