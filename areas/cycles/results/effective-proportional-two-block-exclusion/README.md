---
id: effective-proportional-two-block-exclusion
kind: result
title: Effective denominator growth for two repeated blocks of proportional slope
status: written
claim: >
  Raw odd-only positive valuation words w=u^k v^ell, with nonempty u,v,
  k,ell>=2, proportional totals and lengths, D_w>0, and nonzero
  commutator K=D_u*C_v-D_v*C_u. Write A=sum(w), m=len(w), q=den(w).
  Conditional only on EXT-1, q>2^(7*A/96-172)/(m/4)^341,
  uniformly over both words and both repetition counts. Thus bounded
  denominator layers have an effective finite enumeration, and q=1
  would force A<2^17. With the separately declared convergence input
  through 2^71 and the repository's replayed cycle-length bound,
  den(w)>1 at every size. The common-primitive-word case K=0 is
  retained, not declared trivial; no primitive integer cycle word
  has such a proportional two-block representation with k,ell>=2.
authors:
  - Codex proportional-block research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [proportional-slope-two-block-bound, repeated-block-cancellation-bound, cycle-length-lower-bound-from-convergents, baseline-obligation-transfer-controls]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_effective_bound.py]
evidence:
  - "check_effective_bound.json: exact integer-lemma checks, proportional word identities, cutoff constants and actual-cycle controls"
tags: [cycles, denominators, repeated-blocks, proportional-slopes, effective-exclusion]
---

# Effective denominator growth for two repeated blocks of proportional slope

## Statement

Let `u,v` be nonempty positive valuation words, with

```
sum(u)*len(v)=sum(v)*len(u),
w=u^k v^ell,       k,ell>=2,
A=sum(w),         m=len(w),         D_w=2^A-3^m>0,
K=D_u*C_v-D_v*C_u,                  q=den(w).
```

Assume `K!=0`. The words, their lengths and their common average
valuation all vary; no finite catalogue is fixed. Conditional on
the replayed [gap EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
q > 2^(7*A/96-172)/(m/4)^341.                         (1)
```

This makes bounded-denominator finiteness effective for the whole
proportional class. In particular,

```
q=1  implies  A<2^17.                               (2)
```

Combining (2) with the repository's
[replayed cycle-length bound](../cycle-length-lower-bound-from-convergents/README.md),
which assumes [convergence below 2^71](../../../../sources/barina-2025-convergence-2-71.md),
excludes denominator one at every size in this nondegenerate class.
No Hercher bound or Corvaja--Zannier estimate is needed.

The assumption `K!=0` is essential. When `K=0`, the two words are
powers of one common primitive cycle word and repetition preserves
its denominator. This includes the trivial cycle and the actual
`3x+5,7,13,61` controls. It would also include repetitions of a
hypothetical nontrivial `3x+1` cycle; that case is not excluded here.
Consequently the statement for **primitive** word cycles needs no
separate commutator assumption: `K=0` would make `w` a proper power,
since both repetition counts are at least two.

## Proof

### 1. Exact proportional cancellation and a uniform intercept bound

Write

```
sum(u)=aR,  len(u)=bR,  sum(v)=aS,  len(v)=bS,
gcd(R,S)=1,     U=2^a,     V=3^b,
L=Rk+Sell,      H=gcd(Rk, Sell),      E=U-V.
```

One may take `a=gcd(sum(u),sum(v))` and
`b=gcd(len(u),len(v))`. Positivity of `D_w=U^L-V^L`
forces `U>V`, so both blocks contract. Also `A=aL`, `m=bL`
and `L>=4`.

The [exact proportional bound](../proportional-slope-two-block-bound.md)
gives `E|K` and

```
q > E*U^(L-H)/|K|.                                  (3)
```

Indeed its stronger form divides by the prime-to-6 part of `K/E`;
replacing that part by `|K|/E` only weakens the bound.

For any positive word `z` of length `n` and total `c`, prefix
positivity gives

```
C_z <= 2^(c-n)*(3^n-2^n) < B_z=2^(c-n)*3^n.
```

Here `0<D_z<2^c<B_z`. Since both terms in the commutator
are positive, their difference is smaller in absolute value
than their maximum. Thus, with `W=max(R,S)`,

```
|K| < max(D_u*C_v,D_v*C_u)
     <U^(R+S)*(3/2)^(b*W)
     <U^(R+S+c0*W),       c0=1-log_3(2)<3/8.        (4)
```

The last inequality uses `b*ln3<a*ln2`. Moreover `2^8>3^5`
implies `log_3(2)>5/8`, so `c0<3/8`. These bounds are uniform
in the shapes and common slope of the blocks.

### 2. An integer inequality for two repetitions

For coprime positive `R,S` and `k,ell>=2`, put `T=L-H+1`.
Then

```
96*T-96*(R+S)-36*max(R,S) >= 7*L.                  (5)
```

Write `Rk=Hp`, `Sell=Ht`, with `gcd(p,t)=1`. The difference
between the two sides of (5) is

```
Delta=89*L-96*H+96-96*(R+S)-36*max(R,S).
```

If `p+t>=5`, both `R+S` and `max(R,S)` are at most `L/2`,
so `Delta>=H*(23*(p+t)-96)+96>0`.

If `p+t=4`, coprimality lets us order the blocks so that
`p=1,t=3`. Then `R<=H/2`, `S<=3H/2`, so
`Delta>=14H+96>0`.

If `p+t=3`, order them so that `p=1,t=2`.
Here `R<=H/2` and `S<=H`. If both equalities hold,
coprimality forces `H=2,R=1,S=2`, and `Delta=78>0`.
Otherwise either `R<H/2`, whence `R<=H/3` because `R|H`,
or `S<H`, whence `S<=2H/3` because `S|2H`.
The first gives `Delta>=7H+96>0`; the second gives
`Delta>=35H+96>0`.

Finally, if `p=t=1`, order `R<=S`. Both divide `H`,
are at most `H/2`, and `H>=RS`. In this case
`Delta=82H+96-96R-132S`. For `R=1`, use `H>=2S`
to obtain `Delta>=32S>0`. For `R=2`, coprimality
forces `S>=3`; using `H>=2S` gives
`Delta>=32S-96>=0`. For `R,S>=3`, the lower bound
`82RS+96-96R-132S` is positive at `(3,3)` and increases
in both variables. This proves (5). Equality is attained
at `R=2,S=3,k=3,ell=2`.

Combining (4)-(5),

```
T-R-S-c0*W > T-R-S-(3/8)*W >=7*L/96.               (6)
```

This sharpens the commutator estimate in the elementary
proportional-square argument of
[the uniform two-block theorem](../two-block-uniform-denominator-growth/README.md).
The remaining step makes its power-gap input effective.

### 3. Apply EXT-1 at the base exponents

Apply EXT-1 to the positive integers `b,a`, not to the full word:

```
E=2^a-3^b >= U/(2^172*b^341).
```

Inserting this and (4) into (3), then using (6), gives

```
q > U^(T-R-S-c0*W)/(2^172*b^341)
  > 2^(7*A/96-172)/b^341
  >=2^(7*A/96-172)/(m/4)^341,
```

because `b=m/L<=m/4`. This proves (1). Since positive letters
give `m<=A`, the weaker lower bound with denominator `(A/4)^341`
also holds. Exponential growth against this polynomial supplies an
effective bound on `A` for each fixed ceiling on `q`. Bounded `A`
leaves finitely many positive words, splits and repetition counts.

### 4. The explicit denominator-one cutoff

At `A0=2^17`, the base-2 logarithm of the weaker bound is

```
7*A0/96-172-341*log_2(A0/4)=12811/3>0.                 (7)
```

For `A=A0*t`, `t>=1`, use `ln t<=t-1` and `ln2>1/2` to get
`log_2 t<=2(t-1)`. Therefore the same logarithm is at least

```
12811/3+(7*A0/96-682)*(t-1)>0,
```

since `7*A0>96*682`. Thus (1) excludes `q=1` whenever `A>=2^17`,
proving (2).

If a remaining word had denominator one, it would be an actual
positive odd `3x+1` cycle, possibly traversed several times. It
cannot represent the trivial cycle: that would make every letter
2 and `K=0`. Its primitive period is at most `m<=A<2^17`.
The replayed period bound, under its stated convergence input,
is `72,057,431,991>2^17`, a contradiction. This proves the
all-size exclusion for `K!=0`.

## Certificates

The standard-library [certificate](check_effective_bound.py) checks
the integer lemma, exact proportional cancellation, the rational
commutator estimate, cutoff constants, generated proportional words
and common-cycle controls. Its [receipt](check_effective_bound.json)
is deterministic. The universal inequalities are proved above;
finite word examples are implementation checks.

```
python3 areas/cycles/results/effective-proportional-two-block-exclusion/check_effective_bound.py
python3 -O areas/cycles/results/effective-proportional-two-block-exclusion/check_effective_bound.py
```

All eleven standard actual `3x+d` fixtures are replayed. Repeating
their own words makes `K=0` and preserves their reduced denominator;
those cases are retained. Neither the `3x+1` convergence input nor
its cycle-length consequence is applied to another addend.

## Remarks

The [previous uniform two-block theorem](../two-block-uniform-denominator-growth/README.md)
proved finiteness while both blocks vary, but left an ineffective
cutoff in its proportional-square branch. Its 2026-10-31 review
already identified EXT-1 as a way to make that branch effective.
This node carries out that step and its all-size exclusion;
the underlying cancellation method is credited to the existing
nodes. The positive-difference estimate and sharper integer lemma
above improve the explicit exponent. Novelty is undetermined.

The unequal-slope branch remains outside this proof. So do arbitrary
words without this repeated two-block representation. The separate
[two-periodic-stretch manuscript](../../../../sources/fourier-wren-2026-two-periodic-stretches.md)
has a different bounded-block-size exclusion; its theorems are
not assumed here. No comparison establishes a general record.

This node is `written`, with same-session scrutiny but no independent
review or complete Lean formalisation. Its denominator bound needs
only EXT-1; the all-size denominator-one conclusion additionally
uses the declared convergence input through the replayed period bound.

## History

- 2026-11-08: made the proportional-square bound effective using
  EXT-1 at the common base exponents and completed the resulting
  denominator-one exclusion. Existing merged claims are unchanged.
