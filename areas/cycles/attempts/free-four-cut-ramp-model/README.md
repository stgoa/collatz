---
id: free-four-cut-ramp-model
kind: attempt
title: A free four-cut ramp model survives seventeen rotations
status: written
claim: >
  Tried to exclude four-mismatch rotations of primitive positive odd-only
  3x+1 cycles by a universal ramp with coefficient 3/8 and the first sixteen
  translated-cut witness tests. Verdict: this pure geometric relaxation is
  feasible even with zero error through seventeen rotations. One exact
  control has h=7/18 and cuts {2/9,61/128,799/1152,383/384}, with maximum
  deficit -7/9216. A second has rotation order 14751 and maximum deficit
  -11/10728. Both first fail the formal geometric test at rotation 18,
  which is nonidentity for the latter control. These are circle
  configurations, not cycle words or Collatz cycles. The anchored theorem,
  sharper ramp coefficients and longer-horizon approaches are unaffected.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex directing research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
certificates: [check_free_ramp.py]
evidence:
  - "check_free_ramp.json: exact circular gaps, paired values, first failing rotations and eleven actual-addend ramp controls"
tags: [cycles, rotation-distance, circle-geometry, multirotation, counterexample]
---

# A free four-cut ramp model survives seventeen rotations

## Idea

The [earlier multirotation attempt](../multi-rotation-four-mismatch-exclusion/README.md)
identified exact certificates and faithful profile transfer as remaining
requirements. The later
[anchored single-sawtooth theorem](../../results/single-sawtooth-multirotation-obstruction/README.md)
settled a prescribed cut pattern. This attempt instead freed all four cuts,
seeking a model applicable at the actual minimum of any positive cycle.

Work on the circle `[0,1)`. Define the pre-drop ramp

```
f(0)=1,        f(x)=x for 0<x<1,        R=3/8.
```

Let `0<h<1/2`, and let `C1` contain four distinct arbitrary cuts. For each
positive integer `j`, define

```
Cj = union {C1-i*h : 0<=i<j}, modulo 1,
```

with duplicates removed. For `e` in `Cj`, let `gap_j(e)` be the circular
length from its preceding distinct cut to `e`. The proposed inequalities are

```
gap_j(e) <= R*max(f(e),f(e+j*h)) + epsilon.          (1)
```

The attempted target was that (1) for `1<=j<=16`, with rational `h` of
rotation order greater than 16, forces `epsilon>=1/10000`.

## What happened

An exact rational cell search found a survivor. Direct fraction arithmetic,
independent of the search solver, verifies the two controls below. The
certificate contains only their exact checks; neither the discovery solver
nor a sampled absence claim is a proof dependency.

### A small strict zero-error control

Take

```
h=7/18,
C1={2/9,61/128,799/1152,383/384}
   ={256,549,799,1149}/1152.
```

The largest value of `gap_j(e)-R*max(f(e),f(e+j*h))`, over all cuts at each
rotation, is:

| j | Maximum deficit | j | Maximum deficit |
|---|---|---|---|
| 1 | -5/1152 | 10 | -205/9216 |
| 2 | -7/1024 | 11 | -631/9216 |
| 3 | -47/9216 | 12 | -973/9216 |
| 4 | -1351/9216 | 13 | -13/9216 |
| 5 | -7/9216 | 14 | -1357/9216 |
| 6 | -823/9216 | 15 | -421/9216 |
| 7 | -775/9216 | 16 | -589/9216 |
| 8 | -55/9216 | 17 | -1189/9216 |
| 9 | -1399/9216 | 18 | 155/9216 |

Thus every required inequality through 17 holds strictly even with
`epsilon=0`; the maximum deficit is `-7/9216`.
The formal geometric inequality fails at 18, but `18h=0` on the circle:
that identity rotation would not supply a paired-state witness in a cycle.

### A zero-error control of larger rotation order

Take

```
h=5734/14751,
C1={0,3283/14751,2347/4917,932/1341}.
```

Its reduced rotation order is `14751`. The maximum deficit through 17 is
`-11/10728`, again strictly negative. This control includes the pre-drop
point zero and has coincident raw translates from rotation 3 onward;
those translates are correctly deduplicated. Its first failing test is
rotation 18, with deficit `235/14751>0`. Here rotation 18 is nonidentity.

Every displayed value is reproduced in
[the generated receipt](check_free_ramp.json). Run:

```sh
python3 areas/cycles/attempts/free-four-cut-ramp-model/check_free_ramp.py
python3 -O areas/cycles/attempts/free-four-cut-ramp-model/check_free_ramp.py
```

## Why it fails

The universal ramp discards the relation between the minimum, the actual
valuation profile and the four mismatch cuts. The remaining sixteen-rotation
system admits the exact configurations above, even after adding the
seventeenth test and setting the error to zero. Increasing the precision of
its search cannot prove the proposed obstruction.

This does **not** refute the
[anchored theorem](../../results/single-sawtooth-multirotation-obstruction/README.md):
that result requires base cuts `{0,-h,p,q}` in the fixed ramp frame. Neither
control has the prescribed pair; in fact neither has any two base cuts
separated by `h`. Translating the cut set also changes its position relative
to the ramp. The discarded alignment cannot be silently restored.

These controls do not provide valuations, integral states or a cycle product.
They neither refute the four-mismatch exclusion question nor establish a
limit on every multirotation size argument.

## What survives

### The elementary ramp transfer is valid

Let `n_0,...,n_(m-1)` be a primitive positive odd-only `3x+1` cycle, rotated
so `n_0=L` is its minimum. Put `alpha=log_2(3)`, `ell=log_2 L`,
`E=sum w_i` and `delta=E-m*alpha`. Its positive valuations satisfy

```
log_2 n_i = ell+i*alpha-sum_(k<i)w_k
             +sum_(k<i)log_2(1+1/(3n_k))
          <= ell+(alpha-1)i+delta.                   (2)
```

Here `0<=i<m`, each `w_k>=1`, and the full positive logarithmic sum is
`delta`. Use the **state coordinate `i/m`**, rather than the pre-letter
coordinate `(i+1)/m` used in some weighted-profile nodes. Replacing the value
at zero by `f(0)=1` weakens the upper bound, so (2) gives

```
log_2 n_i <= ell+(alpha-1)m*f(i/m)+delta.
```

If `s(H)=4` and the order of the integer shift `H` modulo `m` is greater
than 16, use `h=H/m`, reversing `H` when necessary. In the following
argument restrict `1<=j<=16`, so every `jH` is nonidentity. The elementary inclusion

```
mis(jH) subset union {mis(H)-iH : 0<=i<j}
```

shows that `Cj` refines the actual mismatch cuts. Each gap `G` therefore
contains `mG-1` agreeing arrows, even if some of its endpoints are artificial
cuts. Since `jH` is nonidentity and the cycle is primitive, the paired odd
states differ. Coprimality of the powers of 2 and 3 makes the final absolute
difference at least `2*3^(mG-1)`. Their maximum is strictly larger.
Consequently

```
G < ((alpha-1)/alpha)*max(f(e),f(e+jh))
      +(ell+delta+alpha-1)/(alpha*m).
```

As `3/2<alpha<8/5`, the coefficient is less than `3/8`. Thus the model is a
valid necessary relaxation with, for example,

```
epsilon=(ell+delta+alpha)/(alpha*m).
```

Its feasibility, not this transfer, is the obstruction found here. No
external gap, convergence or period bound is used in this attempt's claim.

The certificate also checks (2) in exact integer powers on all eleven shared
actual `3x+5,7,13,61` fixtures, retaining each true addend. The ramp identity
extends to `3x+q` with its true logarithmic error; treating that error as the
`q=1` error would be invalid.

### A more selective target is still possible

A longer horizon might exclude configurations of sufficiently large rotation
order: the large-order control already fails at 18. Retaining a sharper
coefficient is another option. At zero error through 17, the exact smallest
coefficients that allow these two controls are respectively `94/253` and
`1216/3283`; both exceed `37/100`. The exact inequality `3^63<2^100`
gives `(alpha-1)/alpha<37/100`. Thus the controls do not refute a stronger
model using the actual coefficient `(alpha-1)/alpha` rather than `3/8`.
One can also retain structural alignment, actual profile drops, or arithmetic
constraints that the free ramp discards. This node makes no claim that either strategy
succeeds. Novelty is undetermined.

## History

- 2026-11-08: recorded the exact failure of the free sixteen-rotation ramp
  target, after sampled searches had found no countercontrol. Preserved the
  elementary cycle transfer and distinguished the anchored theorem and
  longer-horizon questions. Status remains `written`; same-session audits
  are not an independent review.
