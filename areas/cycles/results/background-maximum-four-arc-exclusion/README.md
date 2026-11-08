---
id: background-maximum-four-arc-exclusion
kind: result
title: A larger background label excludes long equal-outer four-arc words
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a,b,c>=1, m=1+a+b+c,
  and gcd(h,m)=1. Read a positive valuation word along the
  cyclic index track x,x+h,... as V,A^a,B^b,A^c, where
  A,B,V are pairwise distinct positive integers and
  t=max(A,B)>V. Under EXT-1, m>=2^43 and D_w>0 imply
  den(w)>1. Both arrangements of the maximum background
  label are covered, with arbitrary label sizes and arc lengths.
  The unique V makes the word primitive. In a hypothetical
  integer cycle of this class with m>=2^22, the mean valuation
  forces {A,B}={1,t}, the rise and end witnesses force t>m/64,
  and t occurs at most 38 times. The resulting at most 39
  non-one letters contradict an elementary ones-run length
  bound at m>=2^43. The only external input is EXT-1;
  the minimum 129 is established by local computation.
  The branch V>max(A,B), other track patterns and smaller
  lengths are not excluded by this result.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [rise-lemma, denjoy-koksma-height-bound, paired-state-run-law]
assumes: [musson-collatz-gap-all]
certificates: [check_background_maximum.py]
evidence:
  - "check_background_maximum.json: exact constants and dyadic inductions, track geometry, local descent, integral ones-run identities and actual 3x+d controls"
tags: [cycles, four-arcs, rotation-distance, largest-letter, few-runs, effective-bounds]
---

# A larger background label excludes long equal-outer four-arc words

## Statement

All clocks are raw odd-only. Let `a,b,c>=1`,
`m=1+a+b+c`, and `gcd(h,m)=1`. Suppose that reading a
positive word `w` along the index track
`x,x+h,...,x+(m-1)h` gives

```
V, A^a, B^b, A^c,                                    (1)
```

where `A,B,V` are pairwise distinct positive integer labels.
The superscripts count letters. Assume

```
t=max(A,B)>V.
```

Then, under the effective gap
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m>=2^43 and D_w>0  imply  den(w)>1.                   (2)
```

Thus the maximum label lies in a background arc, rather
than at the distinguished singleton. It may be the outer
label `A` or the middle label `B`; the latter is allowed
even when `b=1`. No minimum alignment, bound on label
sizes, density restriction, imported period bound or
global convergence verification is assumed.

The result does not cover the opposite branch
`V>max(A,B)` or arbitrary four-mismatch words. It makes
no exclusion claim for `m<2^43`.

## Proof

Suppose `D_w>0` and `den(w)=1`. The word-cycle
correspondence supplies an integer `3x+1` cycle with
these exact valuations. Explicitly, the rotation identity
`2^(w_i) C_next=3C_rot+D_w` propagates divisibility by
the odd number `D_w`; the resulting states `C_rot/D_w`
are positive odd integers. The unique occurrence of `V`
makes the word primitive, hence its states are distinct.

Use `E=sum(w)` for the total, reserving `A,B` for labels.
Let `L,H` be the minimum and maximum state, and put

```
alpha=log_2(3), ell=log_2(L), height=log_2(H/L),
delta=E-alpha*m, eta=(2^E-3^m)/2^E,
kappa=alpha+1/[3L ln(2)].
```

### 1. Minimum, mean and the only possible labels

The certificate traces every odd seed from 3 through
127 to 1. Our primitive word has length at least four,
so its cycle is nontrivial and `L>=129`.

The cycle product gives

```
2^E <= (3+1/L)^m,
delta < m/[3L ln(2)] < m/258,                         (3)
```

using `ln(2)>2/3`. The latter follows, for example, from
the first positive term in
`ln(2)=2 sum_(j>=0) [1/((2j+1)3^(2j+1))]`.
The exact comparison `388^5<2^8*129^5` also gives

```
E<8m/5.                                              (4)
```

If both `A,B>=2`, the letters outside `V` already have
sum at least `2(m-1)`, and `V>=1`. Hence
`E>=2m-1>=7m/4>8m/5`, a contradiction for `m>=4`.
One of `A,B` is therefore 1. Their distinctness and the
hypothesis `t>V` now imply

```
{A,B}={1,t},       2<=V<t.                            (5)
```

The gap and the product also give

```
eta < ln(2^E/3^m) < m/(3L),
eta >= 2^-172*m^-341,
L<2^172*m^342/3,       ell<172+342log_2(m).            (6)
```

This is the only external-input step.

### 2. The maximum background label is linear in the period

Rotation by `h` crosses exactly the four track boundaries
in (1). Its mismatch count is four and its total letter
variation is

```
V_h=2|V-A|+2|A-B|<4t.                               (7)
```

For the log profile, the variation estimate from the
[Denjoy--Koksma height result](../denjoy-koksma-height-bound/README.md)
gives a bound `Delta<=V_h/2+delta` on every positive
partner-height difference. This particular estimate
does not use any continued-fraction bound: the partner
difference has mean zero, its maximum is at most half
its total variation, and that variation is at most
`V_h+2delta`.

The [rise lemma](../rise-lemma/README.md), applied from
minimum to maximum with four mismatches, yields

```
height <= (kappa^5-1)(ell+1+V_h/2+delta)
       < 10(ell+1+2t+m/258).                         (8)
```

For the numerical factor, `3^32<2^51`, `ln(2)>1/2`
and `2/387<1/160` give
`kappa<51/32+1/160=8/5`; then `(8/5)^5-1<10`.

Four mismatches leave an agreeing run of length
`u>=m/4-1`. The
[paired-state run law](../paired-state-run-law.md)
implies `H>2*3^u`. Since `alpha>3/2`,

```
ell+height > 3m/8-1.                                (9)
```

If `t<=m/64`, (8)--(9) would imply

```
(49/2064)m < 11ell+11
           < 11(172+342log_2(m))+11.                 (10)
```

For `2^d<=m<2^(d+1)`, `d>=22`, the opposite inequality
follows from

```
(49/2064)2^22-[11(172+342*23)+11]
  =1437715/129>0.
```

At the next dyadic index the left bound doubles while
the right increases by only `11*342`; the initial left
bound exceeds that increment. Thus (10) is impossible
for every `m>=2^22`, and

```
t>m/64.                                              (11)
```

Let `r` count occurrences of `t` in the whole word.
All other letters are 1 except the singleton `V`, so
`E-m=r(t-1)+(V-1)<3m/5`. If `r>=39`, (11) gives

```
E-m>39(m/64-1)>3m/5,
```

where the final margin at `m=2^22` is `196413/5>0`
and increases with `m`. Therefore `r<=38`, and the
number `s` of letters greater than one satisfies

```
s=r+1<=39.                                          (12)
```

### 3. A bounded number of non-one letters bounds the period

Cut the chronological cycle just after every letter
greater than one. Write these states as `x_i`, starting
with `x_0=L`. The minimum is such a cut because a
valuation-1 step strictly increases a positive state.
Between `x_i` and `x_(i+1)` there are `l_i>=0` ones,
followed by one letter `e_i>=2`. Thus
`m=sum_i(l_i+1)`, with `s` cuts.

The exact ones-run formula is

```
y_i+1=3^(l_i)(x_i+1)/2^(l_i),
```

where `y_i` is the state before the letter `e_i`.
Since `e_i>=2`, `y_i=1 mod4`, so there is a positive
odd integer `z_i` such that

```
x_i+1=2^(l_i+1)z_i,
x_(i+1)=(3^(l_i+1)z_i-1)/2^(e_i-1).                 (13)
```

Consequently

```
l_i+1 <= log_2(x_i+1),
x_(i+1)+1 <= [3^(l_i+1)z_i+1]/2
           < 3^(l_i+1)z_i
           <= (x_i+1)^alpha.                         (14)
```

The last inequality uses `z_i>=1` and `alpha>1`.
This includes consecutive non-one letters (`l_i=0`).
Iterating (14) from the minimum and summing the chunk
lengths gives

```
m < [(alpha^s-1)/(alpha-1)] log_2(L+1)
  < 2 alpha^s log_2(L+1).                            (15)
```

There are at least two cuts in this family, so the
strictness in the first inequality follows from at
least one strict recurrence in (14). The second uses
`alpha>3/2`.

For `s<=39`, `alpha<8/5` and `(8/5)^10<2^7` imply
`alpha^s<2^28`, since `7*39<10*28`. Also
`log_2(L+1)<ell+1<173+342log_2(m)`. Hence

```
m<2^29(173+342log_2(m)).                             (16)
```

This is impossible when `m>=2^43`. For
`2^d<=m<2^(d+1)`, `d>=43`, it would give
`2^d<2^29(515+342d)`. At `d=43`,

```
515+342*43=15221<16384=2^(43-29).
```

Doubling the left side preserves the reverse inequality
at every larger index, because
`2(515+342d)-(515+342(d+1))=173+342d>0`.
This proves (2).

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/background-maximum-four-arc-exclusion/check_background_maximum.py
python3 -O areas/cycles/results/background-maximum-four-arc-exclusion/check_background_maximum.py
```

The standard-library [checker](check_background_maximum.py)
verifies the exact constants and both dyadic inductions,
replays the local descent, checks both label arrangements
and their four-boundary variation on its finite grid,
and verifies (13)--(14) on finite exact integral runs.
It also replays the eleven shared actual `3x+5,7,13,61`
cycles, including their addend-aware run formulas and
paired-state witnesses. Its deterministic
[receipt](check_background_maximum.json) records all
finite ranges. Use `--write-receipt` to regenerate it.
No general exclusion is inferred from a word census.

## Remarks

This uses the existing largest-letter forcing mechanism
from the rise and variation bounds, not a new height
principle. The extra structural step is that a maximum
background label occupies an entire arc: once it has
linear size, the total valuation budget bounds its
multiplicity and leaves only finitely many non-one
letters. The ones-run closure is a classical few-runs
mechanism, written out here to retain exactly the local
minimum and gap hypotheses. No novelty for that tool
is claimed; novelty of this scoped combination is
undetermined.

The all-slope law in
[the mechanical-edit result](../mechanical-edit-denominator-law/README.md)
offers another closure after (12), by comparing with
the constant-one mechanical word. The direct proof
(13)--(16) avoids importing that node's separate
convergence-dependent consequences. It uses neither
an external minimum bound nor an external period bound.

For `3x+d`, the product, drift and run formulas retain
`d`. In particular (13) involves `x_i+d`, whose quotient
need not dominate the normalized addend as required
by (14). The actual controls are not excluded by
dividing their states by `d` and pretending integrality
is preserved.

The complementary branch `V>max(A,B)` remains outside
this result. In the special background alphabet `{1,2}`,
[the inverse-complexity corollary](../four-mismatch-inverse-continued-fraction-bound/README.md)
already supplies a different large-period cutoff for
that branch. Arbitrary background labels are not
covered by that corollary or by the present theorem.

## History

- 2026-11-08: combined the existing rise/variation
  forcing with the repeated background's valuation
  budget and an explicit ones-run closure. Same-session
  scrutiny does not confer independent-review status.
