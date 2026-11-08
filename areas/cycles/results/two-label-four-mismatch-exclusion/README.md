---
id: two-label-four-mismatch-exclusion
kind: result
title: Two valuation labels exclude four mismatches at every rotation
status: written
claim: >
  Raw odd-only 3x+1 clock. Under EXT-1, a primitive nontrivial
  positive integer cycle whose valuation word uses exactly two
  distinct positive integers has at least six mismatches with
  every nonidentity rotation, including noncoprime rotations.
  Equivalently, a primitive positive word with exactly two labels,
  D_w>0 and 1<=s(h)<=4 for some 0<h<m has den(w)>1.
  The minimum-run argument and the rise and end witnesses first
  force m<69(log_2(L)+1), where L is the cycle minimum. EXT-1
  gives m<2^19; exact gap and local descent certificates close
  the remaining lengths. There is no label-size, density,
  coprimality or arc-pattern restriction, and no imported
  convergence or period bound. This does not exclude words
  using three or more labels or two-label words with all
  nonidentity mismatch counts at least six.
authors:
  - Codex arithmetic research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [rise-lemma, paired-state-run-law, doubled-word-cancellation-formula]
assumes: [musson-collatz-gap-all]
certificates: [check_two_labels.py]
evidence:
  - "check_two_labels.json: exact constants, all-length dyadic induction, rational logarithm intervals, two finite gap ranges, local descent and exact 3x+q controls"
tags: [cycles, two-labels, rotation-distance, noncoprime-rotations, minimum-runs, effective-bounds]
---

# Two valuation labels exclude four mismatches at every rotation

## Statement

Use the raw odd-only clock. Assume the effective positive gap
[EXT-1](../../../../sources/musson-collatz-gap-all.md). If a
primitive nontrivial positive integer `3x+1` cycle has length
`m` and exactly two distinct valuation labels, then

```
s(h)>=6 for every 0<h<m.                              (1)
```

The shift need not be coprime to `m`. Both label sizes, their
positions and their multiplicities are unrestricted.

In word language, let `w` be primitive, use exactly two positive
integer labels, and satisfy `D_w=2^(sum w)-3^m>0`. If some
nonidentity rotation has `1<=s(h)<=4`, then `den(w)>1`.
The [word-cycle correspondence](../doubled-word-cancellation-formula/README.md)
identifies denominator one with an integer `3x+1` cycle.

The proof establishes the conditional length bound

```
m<69(log_2(L)+1)                                      (2)
```

for a hypothetical cycle with `s(h)<=4`. EXT-1 reduces its
length below `2^19`; exact finite checks then give a local
contradiction. The only external input is EXT-1. In particular,
the proof does not import a global convergence verification or
an odd-period lower bound.

## Proof

Suppose such a cycle and shift exist. Write its states as
`n_i`, its valuations as `a_i`, and its total valuation as `A`.
Put

```
L=min_i n_i, H=max_i n_i,
ell=log_2(L), B=log_2(H/L), Y=log_2(L+1),
alpha=log_2(3), delta=A-alpha*m,
eta=(2^A-3^m)/2^A, kappa=alpha+1/[3L ln(2)].
```

Primitivity means the states are distinct. It also prevents
`s(h)=0`: if the valuations repeated with a proper period,
the increasing affine map of one period would have an
iterated fixed point, hence a fixed point, giving repeated
states. For two labels, a rotation has as many transitions
from the first label to the second as in the reverse direction,
so `s(h)` is even. It suffices to exclude `1<=s(h)<=4`.

### 1. The minimum bounds the common non-one valuation

The certificate proves that every positive integer below
`2^19` reaches 1. Only its small subrange, the odd seeds
`3,...,127`, is used at this stage. Thus a nontrivial cycle
has `L>=129`. For every state `n>=L`,

```
log_2(3+1/n)<kappa<8/5.                              (3)
```

Indeed, `3^32<2^51`, `ln(2)>1/2` and
`2/387<1/160` imply
`kappa<51/32+1/160=8/5`. The first positive term in
the atanh series for `ln(2)` also gives `ln(2)>2/3`.
The cycle product consequently gives

```
delta=sum_i log_2(1+1/(3n_i))<m/258.                  (4)
```

The outgoing valuation at the minimum is 1: a valuation at
least 2 would send `L>1` to a smaller state. Therefore the
two labels are `{1,t}` for an integer `t>=2`. Starting at
`L`, let `l>=1` be the first maximal run of valuation 1.
It is followed by valuation `t`. The exact ones-run identity
and the terminal valuation give

```
n_l+1=(3/2)^l(L+1),
v_2(n_l+1)=1,
v_2(L+1)=l+1,
l+1<=Y.                                              (5)
```

Here `a_l=t>=2` implies `n_l=1 mod 4`, which is precisely
the second identity. The segment of `l+1` steps ends at
`n_(l+1)>=L`, so multiplying its exact arrows yields

```
l+t <= sum_(i=0)^l log_2(3+1/n_i)
    < kappa(l+1).
```

Writing `u=t-1`, we obtain the bound independent of both
label multiplicities:

```
u<(3/5)(l+1)<(3/5)(ell+1).                           (6)
```

This use of the minimum and of the actual additive constant
1 is essential. Normalizing a `3x+q` cycle by dividing its
states by `q` does not preserve the integer witness (5).

### 2. Four mismatches force a short cycle

Fix the given shift `h`. Its total letter variation is exactly

```
V_h=sum_i |a_i-a_(i+h)|=s(h)u<=4u.                   (7)
```

For completeness, the partner-height estimate used by the
[rise lemma](../rise-lemma/README.md) needs no coprimality.
Set `mu_i=log_2(n_(i+h)/n_i)` and
`eps_i=log_2(1+1/(3n_i))`. The shift permutes all indices,
so `sum_i mu_i=0`. Subtracting two profile recurrences gives

```
mu_(i+1)-mu_i=a_i-a_(i+h)+eps_(i+h)-eps_i.
```

Thus the cyclic total variation is at most `V_h+2delta`.
A cyclic real sequence with mean zero has maximum at most
half its total variation. Consequently

```
max_i mu_i<=V_h/2+delta<=2u+delta.                   (8)
```

Apply the rise lemma from the minimum to the maximum, with
at most four mismatches and the uniform bound (8). Since
`(8/5)^5-1<10`, (3), (4) and (6) give

```
B <=(kappa^(s(h)+1)-1)(ell+1+2u+delta)
  <10(ell+1+2u+delta)
  <22(ell+1)+(5/129)m.                              (9)
```

The mismatches split the cyclic word into `s(h)` agreeing
runs, possibly empty. A longest run has length
`v>=m/s(h)-1>=m/4-1`. The
[paired-state run law](../paired-state-run-law.md) applies
also when `v=0`: its endpoint difference is a nonzero
integer multiple of `2*3^v`. Hence `H>2*3^v` and

```
ell+B>1+alpha*v>3m/8-1.                             (10)
```

For the last comparison, write
`1+alpha(m/4-1)=alpha*m/4+1-alpha` and use
`3/2<alpha<2`; this also handles `m<4`.
Combining (9) and (10),

```
(347/1032)m<23(ell+1),
m<(23736/347)(ell+1)<69(ell+1).                      (11)
```

Every step in this section holds for an arbitrary nonidentity
shift. No decomposition of the shift into one cyclic index
track has been assumed.

### 3. EXT-1 and an exact dyadic cutoff

The cycle product and `1-exp(-x)<x` give

```
eta<ln(2^A/3^m)<m/(3L).
```

EXT-1 gives `eta>=2^-172 m^-341`. Therefore

```
ell<172+342log_2(m),
m<69(173+342log_2(m)).                               (12)
```

If `2^d<=m<2^(d+1)` and `d>=19`, the right side in
(12) is below `69(515+342d)`. At `d=19`,

```
2^19-69(515+342*19)=40391>0.
```

The induction to the next band follows because twice
`515+342d` minus `515+342(d+1)` is `173+342d>0`.
Thus

```
m<2^19.                                              (13)
```

### 4. Finite gap bootstrap and local closure

This section uses integer and rational arithmetic only.
The certificate constructs 80-term atanh enclosures for
`ln(2)` and `ln(3)`. With `z=(v-1)/(v+1)`, the positive
tail after 80 terms is less than

```
2 z^161 / [161(1-z^2)].
```

The resulting enclosure for `alpha` lies strictly inside

```
125573666586150569315490533898 / 2^96
  < alpha <
125573666586150569315490533899 / 2^96.                (14)
```

For every integer `1<=m<2^19`, the scaled endpoints in
(14) have the same integer part. The distance from the
upper endpoint to the next integer, with denominator
`2^96`, has minimum numerator

```
7373341559091880256221, attained at m=190537,
```

which is greater than `2^71`. Thus `A-alpha*m>2^-25`
whenever `2^A>3^m` in this range. Since `ln(2)>1/2`,
the natural logarithmic gap exceeds `2^-26`.
The elementary inequality
`1-exp(-x)>min(x/2,1/2)` for `x>0` now gives

```
eta>2^-27,
L<m*2^27/3,
ell<46.
```

Equation (11) implies `m<3243`, hence `m<=3242`.
For an integer `j>=1`, set

```
A_j=bit_length(3^j), eta_j=(2^(A_j)-3^j)/2^(A_j).
```

At fixed length `j`, every allowed integer total has
`eta>=eta_j`. The certificate checks the following exact
finite bounds by clearing positive denominators:

| Lengths | Upper bound for `j/(3 eta_j)` | Largest ceiling and its length |
|---|---:|---:|
| `1<=j<=3242` | `<2^21` | `1166894` at `j=2966` |
| `1<=j<=1517` | `<2^19` | `330912` at `j=971` |

The first row and `eta<m/(3L)` imply `L<2^21`.
Using (11) again gives `m<69*22=1518`, so `m<=1517`.
The second row then gives `L<2^19`.

Finally the certificate checks every odd seed
`3<=n<2^19` in ascending order until its odd-only orbit
reaches an integer below `n`. Induction on the seed,
with 1 as the base case and even halvings automatic,
proves convergence for every positive integer below
`2^19`. This contradicts a nontrivial cycle with that
minimum. It proves (1) at every length.

## Certificates

[`check_two_labels.py`](check_two_labels.py), run from the
repository root, verifies [`check_two_labels.json`](check_two_labels.json);
`--write-receipt` regenerates it explicitly.
It checks the exact rational constants and dyadic induction,
the rational logarithm enclosure and all `524287` positive-gap
intervals, both finite power ranges, and the local descent.
It also replays exact reduced `3x+q` cycles from binary words,
including noncoprime four-mismatch shifts, integer ones-run
prefixes and all eleven standard `3x+5`, `3x+7`, `3x+13`
and `3x+61` fixtures.

The receipt records `4759` finite power comparisons,
`262143` local odd seeds with `913635` descent steps,
`1909` minimum-return prefixes, `1173` reduced cycles,
and `83116` paired-run checks. Among the binary-cycle
controls, `1643` shifts have exactly four mismatches and
are noncoprime to the period.

For example, the actual `3x+65455` cycle
`569,33581,83099,2459` has word `(1,1,7,7)`. The
shift `h=2` has four mismatches and `gcd(h,4)=2`.
Its minimum exceeds 129, but its non-one valuation
violates the `q=1` bound (6): `2^30>570^3`.
The actual-addend identity uses `n+65455`, not `n+1`.

The general proof is the argument above. The finite control
grids are not a proof by enumeration of all words. Their
actual addend `q` is retained throughout; the `q=1` minimum
and drift bounds are not imposed on generalized cycles.

## Remarks

- This combines the minimum ones-run witness with the
  existing [largest-letter variation method](../largest-letter-rho-reduction.md).
  Two labels make the height-driving variation depend on
  the same non-one valuation that the minimum controls.
- The proof does not use continued fractions, coprime
  rotation tracks, a four-arc classification, or the
  previously declared large convergence computation.
  It therefore complements the coprime three-label results.
- Novelty is undetermined. The constituent ones-run and
  rise arguments are already present in this repository;
  no priority claim is made for this combination.
- This node is written, not formal or independently
  reviewed. Same-session mathematical and certificate
  scrutiny does not change that status.

## History

- 2026-11-08: combined the minimum-run valuation bound with
  the rise and end witnesses for two labels, and closed
  the resulting finite range by exact gaps and local descent.
