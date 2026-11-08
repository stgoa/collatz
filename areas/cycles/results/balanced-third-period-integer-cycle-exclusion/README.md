---
id: balanced-third-period-integer-cycle-exclusion
kind: result
title: Balanced third-period four-mismatch words exclude integer cycles
status: formal
claim: >
  In the raw odd-only clock, let w be a finite word of positive integers
  of length 3g. Suppose w differs from its shift by g at exactly four
  positions. In each column (w_i,w_(i+g),w_(i+2g)), let U_i be the majority
  entry, and suppose sum(w)=3sum(U). Then no positive odd integer
  3x+1 cycle follows w with period |w|. If D_w>0, then D_w does not divide
  C_w, equivalently den(w)>1. The majority entries and two equal-opposite
  changes are derived from the mismatch condition; no placement, minimum
  period, length bound, or bound on the letters or changes is assumed.
  This formalization covers the integer-cycle exclusion, not the separate
  quantitative denominator bound for general positive addends.
authors:
  - Codex signed-endpoint formalisation lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [unaligned-balanced-third-period-exclusion]
assumes: [mathlib-065356127b1d]
lean:
  - LeanLane.BalancedThirdPeriod.no_positive_odd_cycle
  - LeanLane.BalancedThirdPeriod.discriminant_not_dvd_intercept
evidence:
  - "../../../../lean/receipts/BalancedThirdPeriod.build.txt: pinned library build"
  - "../../../../lean/receipts/BalancedThirdPeriod.axioms.txt: every new theorem's axiom report"
  - "../../../../lean/receipts/BalancedThirdPeriod.sha256.txt: compiled source hash"
tags: [cycles, denominators, third-period, balanced-defects, classification, lean]
---

# Balanced third-period four-mismatch words exclude integer cycles

## Statement

Use the shared valuation-word definitions

```
C_[] = 0,   C_(a::w) = 3^|w| + 2^a C_w,
D_w = 2^sum(w) - 3^|w|,
den(w) = D_w / gcd(C_w,D_w)       when D_w>0.
```

Let `w` be a positive-integer word of length `3g`. Count mismatches
between `w_i` and `w_((i+g) mod 3g)` over all `0<=i<3g`, and assume
that this count is four. For `0<=i<g`, let `U_i` be the majority of

```
(w_i, w_(i+g), w_(i+2g)).                              (1)
```

The mismatch condition implies that every column has a majority.
Assume the additional balance condition

```
sum(w)=3sum(U).                                       (2)
```

There is no positive odd integer sequence `x_i`, periodic with period
`|w|`, satisfying

```
2^(w_(i mod |w|)) x_(i+1) = 3x_i+1.                   (3)
```

Consequently, `D_w>0` implies `D_w` does not divide `C_w`, or
`den(w)>1`. These hypotheses themselves imply `g>=2`. There is no
primitivity assumption and no bound on `g`, the letters, or the defect
amplitude. The reduction to the two placements is part of the theorem.

This is the complete integer-cycle corollary of
[the balanced third-period denominator law](../balanced-third-period-denominator-law/README.md).
The quantitative general-addend bounds of that node are not asserted
as formal here.

## Proof

### 1. Recover the majority template and the signed changes

A three-entry cyclic column has zero, two, or three mismatches.
A nonconstant column contributes at least two. Four total mismatches
therefore force exactly two nonconstant columns, each contributing
two. Each of these columns has one outlier and two equal entries;
every other column is constant. Thus `U` is a positive word of length
`g`, and `w` differs from `U U U` at exactly two positions in distinct
columns modulo `g`.

Call the positions `p,n`. Summing all unchanged entries and using (2)
gives

```
w_p+w_n = U_(p mod g)+U_(n mod g).
```

Both differences are nonzero. After naming their signs, there is an
integer `delta>=1` with

```
w_p=U_(p mod g)+delta,
w_n+delta=U_(n mod g).                                (4)
```

This derives the signed balance from the intrinsic total condition;
(4) is not an additional hypothesis.

### 2. Recover the two cyclic placements

Rotate the word and template so that the positive change is at zero.
Let `j` be the negative change's new index. Then `0<j<3g`, and distinct
columns exclude `j=g,2g`.

If `j<g`, both changes lie in the first length-`g` block. If `j>2g`,
rotate again to the negative change; both changes then lie in the
first block. In either case a further block rotation gives

```
U U V,   |V|=|U|=g,   sum(V)=sum(U),   V!=U.          (5)
```

If `g<j<2g`, set `l=2g-j`, so `0<l<g`, and cut just after the
negative change's template position. The changed positions become
`l-1` and `2g-1`. Split the rotated template as `A B`, with `|A|=l`.
Writing `A=(u,a)`, `B=(v,b+delta)`, positivity gives `a,b>=1` and
positive, possibly empty prefixes `u,v`. The actual word is exactly

```
A[+delta] B A B[-delta] A B.                           (6)
```

The formal reconstruction checks the complete lists, including the
terminal positions and cyclic boundary cases. Rotating a cycle shifts
its state sequence and preserves positive odd states.

### 3. Exclude both placements

For (5), write `P=3^g`, `Z=2^sum(U)`, and
`Phi=P^2+PZ+Z^2`. Concatenation gives

```
D_(UUV)=(Z-P)Phi,
C_(UUV)-Phi C_U = Z^2(C_V-C_U).                        (7)
```

If a `3x+1` cycle follows `UUV`, the cycle equation gives
`D_(UUV) | C_(UUV)`. The powers of two and three are coprime, so
`gcd(Phi,Z)=1`, and (7) implies `Phi | C_V-C_U`. The positive-word
intercept bound is

```
2^g C_U < ZP,       2^g C_V < ZP.
```

Both intercepts are nonnegative and less than `Phi`; hence
`C_U=C_V`. Positive words of equal length and total with equal
intercepts are equal: their first exponents are recovered by the
power of two multiplying the odd intercept of the remaining nonempty
suffix, and induction recovers every letter; the equal total fixes
the last letter. Thus `U=V`, contradicting (5).

Placement (6) is excluded by the already formalized
[unaligned theorem](../unaligned-balanced-third-period-exclusion/README.md).
Its hypotheses are exactly those supplied by the reconstruction.
That arithmetic proof uses the retained positive terms in the cubic
factor relation and the elementary minimum-nine restriction for
nontrivial `3x+1` cycles. No external gap, convergence, or period bound
enters either branch.

Finally, if `D_w>0` and `D_w | C_w`, the formal integer-cycle
construction produces positive odd states satisfying (3), contradicting
the result just proved. This establishes the word-level conclusion.

## Certificates

The complete argument is checked in Lean; no finite search is used
as a replacement for the classification. The module includes two
actual positive-addend controls:

```
aligned:   [2,3,2,3,3,2],   q=32039, C=13847, D=32039;
unaligned: [3,3,2,2,2,3],   q=32039, C=12091, D=32039.
```

Both words have four mismatches under shift two, majority template
`[2,3]`, and total `15=3(2+3)`. Lean checks these facts and constructs
positive `3x+32039` cycles for both words. The exclusion is specific
to addend one and leaves these controls intact.

## Lean

The module is
[`LeanLane/BalancedThirdPeriod.lean`](../../../../lean/LeanLane/BalancedThirdPeriod.lean).

- `majorityTemplate` applies the explicit function
  `if a=b then a else if a=c then a else b` to each column (1).
  `column_bounds` proves that the all-distinct case cannot occur
  under the four-mismatch hypothesis.
- `balanced_pair_of_mismatches` derives the two distinct columns,
  unchanged positions, and the equal-opposite changes (4).
- `BalancedPair.rotate`, `aligned_decomposition`, `unaligned_cut`,
  and `reconstruct_unaligned` prove the placement reduction.
- `no_positive_odd_cycle` states (3) is impossible directly from
  positive `w`, `w.length=3*g`, `mismatches w g=4`, and (2).
  Neither `BalancedPair` nor a normal form is assumed by this theorem.
- `discriminant_not_dvd_intercept` has those same intrinsic word
  hypotheses and `D_w>0`, and concludes `not (D_w divides C_w)`.

`g` is a natural number in Lean; the hypotheses exclude zero and one.
The cycle theorem assumes integer states, positivity, oddness, and
period `|w|`, exactly as in the Statement. The word-level theorem
constructs those states rather than assuming them. The imported
unaligned theorem uses the same `Words.C`, `Words.D`, and
`CycleEquation.IsCycle` definitions.

The pinned library build and direct axiom reports are recorded in
[the build receipt](../../../../lean/receipts/BalancedThirdPeriod.build.txt),
[the axiom receipt](../../../../lean/receipts/BalancedThirdPeriod.axioms.txt),
and [the source hash](../../../../lean/receipts/BalancedThirdPeriod.sha256.txt).
Only `propext`, `Classical.choice`, and `Quot.sound` are allowed.
Mathlib dependencies use the pinned cache; this is not a claim that
every dependency was rebuilt from source. The complete Lean CI workflow
passed at commit `f2cd7caa93446343066a604bcce1be5a0258bcce`
(run `42535728956`), including the library and all Mathlib-only
standalone files.

## Remarks

This formalizes the placement reduction and the integer-cycle
corollary already written in the broader denominator-law node.
It does not promote that node's quantitative general-addend law.
The aligned intercept argument is a shared-definition version of
the repository's existing equal-total argument; the unaligned
arithmetic is reused without modification. Novelty is undetermined.

The general four-mismatch question remains open. Unbalanced
third-period words and shifts with other track lengths are outside
this claim.

## History

- 2026-11-08: Formalized the complete intrinsic balanced third-period
  integer-cycle exclusion, including column counting, recovery of
  the signed defects, cyclic placement reconstruction, and both
  arithmetic branches. The earlier quantitative denominator law
  and the unaligned formal node retain their existing scope.
- 2026-11-08: Promoted this scoped integer-cycle claim to `formal`
  after the complete Lean CI pass. The proof source and axiom receipts
  were unchanged by the status update.
