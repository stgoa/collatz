---
id: half-defect-imbalance-growth
kind: result
title: Half-period defect magnitudes must have a linear imbalance
status: written
claim: >
  Raw odd-only positive integer 3x+1 cycles. Let the valuation word have
  length 2N and exactly four mismatches with its half-period rotation.
  Let p,q be the positive absolute changes at the two differing half-word
  positions, Delta=|p-q|, and M the minimum integer state. Without external
  inputs, N<36 log2(M)+7Delta; the local minimum threshold M>=2^17 is
  established by exact finite descent. Under the sole external gap
  input EXT-1, Delta<=N/8 is excluded at every length. More precisely,
  normalize cyclically to W=A B A[p] B[q], where brackets increase the
  final letter. If p<q, every global minimum must lie in the first A;
  if p>q, it must lie in the second B[q] and Delta>3N/4. Minimum locations
  are states before arrows in the named copies. A self-contained
  even-clock gap bootstrap and local descent below 18000000 replace
  the original Barina-dependent closure. Both signs, both magnitude
  orders and both parities are covered; equal magnitudes are excluded,
  and there is no upper bound on the common magnitude.
authors:
  - Codex arithmetic research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [half-defect-positive-order-exclusion]
assumes: [musson-collatz-gap-all]
certificates: [check_imbalance.py]
evidence:
  - "check_imbalance.json: exact four-case inequalities on actual cycles, intrinsic normalization, rational constants, full-even-clock gap bootstrap and complete local descent"
tags: [cycles, half-defects, denominators, imbalance, minimum-bounds]
---

# Half-period defect magnitudes must have a linear imbalance

## Statement

Let a positive odd integer cycle of the raw odd-only `3x+1` map
have valuation word `w` of length `2N`. Suppose its rotation by
`N` differs in exactly four positions. The two halves then differ
at exactly two positions. Let `p,q>=1` be the absolute differences
at those positions, and put `Delta=|p-q|`. Let `M` be the minimum
integer state. Then, without an external input,

```
N < 36 log_2 M + 7 Delta.                               (1)
```

The local computation below proves `M>=2^17`; it is not an
imported convergence assertion. The proof covers either sign
pattern of the half-word changes, both chronological magnitude
orders, and both parities. It also allows `Delta=0`.

Under [EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
Delta <= N/8    implies    N < 2^22.                     (2)
```

In fact EXT-1 alone excludes this entire regime at every length.
A complete internal gap bootstrap and local descent below
`18000000` give this stronger conclusion. In pure-word terms,
if `D_w=2^sum(w)-3^(2N)>0`, the four-mismatch and imbalance
conditions imply `den(w)>1` under EXT-1.

There is also an order-sensitive restriction. In the cyclic
double-increase form `A B A[p] B[q]` defined below, every global
minimum of a hypothetical integer cycle must occur in first `A`
when `p<q`, and in second `B[q]` when `p>q`. Locations mean states
before arrows in those copies; no unique minimum is assumed.
In the latter order the stronger bound `p-q>3N/4` is necessary.
These conclusions use only EXT-1 and the same internal finite checks.

There is no restriction on the smaller defect magnitude. The
remaining unequal cases are not excluded here.

## Proof

### 1. Normalization and the exact state ordering

Move the cyclic cut between the two changed positions when their
comparison signs are opposite. This reverses exactly one sign.
Exchange the two halves if both changes are negative. Finally cut
after the second changed position in chronological half-word order,
exchanging halves again if necessary.
The word now has the form

```
w = A B A[p] B[q],        a=len(A)>=1, b=len(B)>=1,
N=a+b,                   p,q>=1,                         (3)
```

where `[j]` increases only the last letter of a block. This
preserves the unordered pair of magnitudes, but does not prescribe
whether `p<q` or `p>q`. Both cases are handled below.

Write the boundary states as

```
x --A--> z --B--> y --A[p]--> t --B[q]--> x,
P=3^a, R=3^b, Q=2^sum(A), S=2^sum(B),
k=2^p, l=2^q, rho=PR/(QS).
```

For an actual cycle with any positive odd addend `d`, the
[paired-state identities](../half-defect-positive-order-exclusion/README.md)
give

```
x<y,     h=(y-x)/Q positive odd,
j=(z-t)/S nonzero odd.                                  (4)
```

At `d=1`, that result proves `j<0` when `p<q`. If `p>=q`,
its retained first-intercept identity

```
d(k-1)(l-1)C_A
 =[kQS(l-1)+PR(k-1)]j+PQ(l-k)h
```

forces `j>0`, since the last term is nonpositive. This conclusion
also holds for every positive `d`. Thus the required state orders
are established, rather than assumed from the defect magnitudes.

### 2. Ratio and interior-state estimates

The next estimates retain the actual addend `d` and apply to any
positive odd integer cycle with the indicated sign of `j`. Set

```
M=min(state), ell=log_2 M, alpha=log_2 3,
kappa=log_2(3+d/M), gamma=2^(kappa-1),
E=sum(w), T=sum(A)+sum(B), r0=y/x>1.
```

The product identity gives `E<=2kappa N`, while `T>=N`.
The second-half map has positive intercept and slope `rho/(kl)`,
so `r0<kl/rho`. Consequently

```
log_2 r0 < E-T-alpha N <= (2kappa-alpha-1)N.              (5)
```

Put `r=t/z>1` if `p<q,j<0`, and `r=z/t>1` if `p>=q,j>0`.
In the first case a positive affine map contracts the ratio of
two ordered positive inputs toward one, hence `r<r0/k<l/rho`.
In the second case the composite map `z -> y -> t` has slope
`rho/k` and positive intercept, hence `r<k/rho`. In both cases,

```
log_2 r < Delta/2+(E-2alpha N)/2
          <= Delta/2+(kappa-alpha)N.                    (6)
```

For a block of length `a`, total valuation `A0`, and starting
state `v`, its state before arrow `i`, `0<=i<a`, satisfies

```
state_i >= 3^i v/2^prefix_i >= (2^a/2^A0)v.              (7)
```

Indeed `prefix_i<=A0-(a-i)`. The estimate also applies to
the prefixes of a copy whose final letter has been increased;
those prefixes have not changed. Every actual arrow of valuation
`e` also satisfies

```
next <= gamma*current/2^(e-1).                          (8)
```

In particular, a remaining suffix of `B[q]`, starting at a
minimum and containing at most `b` arrows, ends at a state at
most `gamma^b M/l`. Keeping this terminal factor is essential.

### 3. The four locations of the minimum

Corresponding prefixes with the same letters preserve strict
state order. When `p<q,j<0`, all states in the first half `AB`
are smaller than their partners in the second half. When
`p>=q,j>0`, the smaller copies are first `A` and second `B[q]`.
Thus the minimum occurs in one of the following four cases;
ties cause no difficulty because any minimizing location works.

**Case A: `p<q`, minimum in first `A`.** Since
`y-x=Qh` and `t-z=S(-j)`, with `h,-j>=1`,
`x>Q/r0` and `z>S/r`. Equations (7),(8) give

```
M > 2^a/r0,              M > 2^b/(r gamma^a).           (9A)
```

**Case B: `p<q`, minimum in first `B`.** The same bound on
`z`, together with `y=x+Qh>Q`, gives

```
M > 2^b/r,               M > 2^a/gamma^b.               (9B)
```

**Case C: `p>=q`, minimum in first `A`.** Here
`z-t=Sj`, with `j>=1`, so `z>S`. Thus

```
M > 2^a/r0,              M > 2^b/gamma^a.               (9C)
```

**Case D: `p>=q`, minimum in second `B[q]`.** Since
`t>S/r`, its unchanged prefixes give the first bound below.
For the second, (8) gives `l*x<=gamma^b M`. The ordinary `B`
map sends `z,t` to `y,l*x`; positivity of its intercept gives
`y/(l*x)<z/t=r`. Because `y>Q`,

```
M > 2^b/r,               M > 2^a/(r gamma^b).           (9D)
```

These are exact bounds for actual states. No normalized rational
state is treated as an integer, and no control addend is replaced
by one.

### 4. A uniform inequality for integer cycles

Return to `d=1`. The word cannot be all `2`, so its cycle is
nontrivial. The certificate checks that each odd start below
`2^17` reaches a smaller positive odd start; induction, with
the base state `1`, proves convergence of that whole range.
A nontrivial cycle therefore has `M>=2^17`.

The exact integer comparisons

```
3^10000 > 2^15849,        393217^200 < 2^3717
```

give the fixed rational bounds

```
alpha > A0=15849/10000,
kappa <= log_2(3+1/2^17) < K0=317/200.
```

Set `c0=2K0-A0-1=5851/10000` and
`e0=K0-A0=1/10000`. Equations (5),(6) give

```
log_2 r0 < c0 N,        log_2 r < Delta/2+e0 N,
gamma < 2^(K0-1).                                      (10)
```

Taking logarithms of the two inequalities in each row of (9),
then eliminating `a` or `b=N-a`, gives the following fixed
linear inequalities. Every coefficient in the second column
is positive.

| Case | Coefficient `c` | Consequence |
|---|---:|---|
| A | `1-e0-K0*c0=145033/2000000` | `cN<(1+K0)ell+Delta/2` |
| B | `1-K0*e0=1999683/2000000` | `cN<(1+K0)ell+K0*Delta/2` |
| C | `1-K0*c0=145233/2000000` | `cN<(1+K0)ell` |
| D | `1-(K0+1)e0=1999483/2000000` | `cN<(1+K0)ell+(K0+1)Delta/2` |

In every row `36c>1+K0` and `7c` exceeds the displayed coefficient
of `Delta`. For the tightest row A, the positive slacks are
`12797/500000` and `15231/2000000`, respectively. Since
`ell>0` and `Delta>=0`, these exact comparisons prove (1).

An optional gap form makes the common-amplitude independence
explicit. With `eta=1-3^(2N)/2^E` and `G=log_2(1/eta)`, the
product identity gives `eta<2N/(3M)`, hence

```
N < 36(G+log_2 N)+7Delta.
```

For `N>=1024`, `36log_2 N<=N/2`, so
`N<72G+14Delta`. This reformulation needs no external gap bound.

### 5. A single finite closure using only EXT-1

We first prove a finite-closure lemma independent of the half-defect
shape: **under EXT-1, a nontrivial positive odd integer cycle with
displayed even length `2N` and minimum `M` cannot satisfy
`N<259log_2 M`.** The displayed length need not be the least period.

EXT-1 is applied at the full odd period `2N`:

```
eta >= 1/(2^172*(2N)^341).
```

Together with `M<2N/(3eta)`, this implies

```
ell < 172+342log_2(2N)=514+342log_2 N.                   (11)
```

If `N<259ell`, (11) gives

```
N < 133126+88578log_2 N.                                 (12)
```

For `2^j<=N<2^(j+1)`, `j>=22`, the lower endpoint exceeds
`133126+88578(j+1)`: the exact margin at `j=22` is
`2023884`, and its next-step increase is `2^j-88578>0`.
Thus `N<2^22`.

The next bound is a complete finite calculation on the **full even
clock**, including opposite-parity defects. The certificate proves

```
eta > 2^(-27) for every 1<=N<2^22 and 2^E>3^(2N).       (13)
```

Here is its exact construction. For `v=2,3`, put `z=(v-1)/(v+1)`.
The first 80 terms of `2 sum z^(2j+1)/(2j+1)` bound `ln(v)`
from below; adding `2z^161/(161(1-z^2))` bounds it from above.
This follows by integrating the positive geometric-series tail.
Taking the ratio and rounding outward proves

```
125573666586150569315490533898 / 2^96
  < alpha <
125573666586150569315490533899 / 2^96.
```

For each `N` in (13), both scaled endpoints of `2N*alpha` have
the same integer part. The upper endpoint's distance below the
next integer exceeds `2^71/2^96=2^(-25)`; its minimum numerator
is `14746683118183760512442`, at `N=190537`.
Thus `E-2N*alpha>2^(-25)`. Since `ln 2>1/2`, the positive
natural-log gap exceeds `2^(-26)`. The elementary estimate
`1-exp(-u)>=min(u/2,1/2)` for `u>0` proves (13).

Write `G=log_2(1/eta)`. The product estimate
`M<2N/(3eta)` gives `ell<log_2 N+G`. Now apply these strictly
rounded bounds:

| Input range | Exact gap bound | Consequence of `N<259ell` |
|---|---|---|
| `N<2^22` | `G<27` from (13) | `N<259*49=12691`, so `N<=12690` |
| `N<=12690<2^14` | `G<14` | `N<259*28=7252`, so `N<=7251` |
| `N<=7251<2^13` | `G<13` | `N<259*26=6734`, so `N<=6733` |

The last two gap rows are checked directly with
`P_N=9^N`, `E_N=bit_length(P_N)`, and
`eta_N=(2^E_N-P_N)/2^E_N`. This is the smallest possible
positive gap at that full odd length, so every larger total
valuation is covered. Finally, for every `1<=N<=6733`,

```
2N/(3eta_N) <= 17306923 < 18000000.                      (14)
```

The largest ceiling in (14) is attained at `N=6138`,
`E_N=19457`. The certificate proves complete local descent
below `18000000` by ascending induction on odd starts. Thus
the hypothetical nontrivial cycle cannot have the minimum
forced by (14). This proves the finite-closure lemma.
No external convergence or period computation enters it.

### 6. Minimum placement and the two imbalance cones

Let the four positive coefficients in the table be `c_A,...,c_D`.
In Case B the total-valuation budget gives

```
Delta <= p+q = E-2T < 2(K0-1)N.
```

Its row therefore implies

```
[c_B-K0(K0-1)]N < (1+K0)ell,
c_B-K0(K0-1) = c_C = 145233/2000000.
```

Both Cases B and C force `N<36ell`, and the finite-closure lemma
excludes them under EXT-1. Thus every minimum lies in first `A`
if `p<q`, and in second `B[q]` if `p>q`.

If `Delta<=N/8`, each of the four rows gives `N<259ell`.
For the tightest row A,

```
c_A-1/16 = 20033/2000000,
259*(c_A-1/16) > 1+K0.
```

The other rows have larger margins. The finite-closure lemma
therefore excludes all near-equal magnitudes, including equality.
This also establishes the original cutoff (2).

For `p>q`, only Case D remains. If `Delta<=3N/4`, its row gives

```
[c_D-3(K0+1)/8]N < (K0+1)ell,
86*[c_D-3(K0+1)/8] > K0+1.
```

Hence `N<86ell`, again excluded by the same lemma. This proves
the stronger order-sensitive condition `p-q>3N/4`.

For clarity, four half-period mismatches already force word
primitivity. If `w=V^r`, with `V` primitive, the mismatch count
of any rotation is `r` times the mismatch count in `V`. Hence
`r` divides `4`. If `r=2` or `4`, the half-period shift `N`
is a multiple of `len(V)`, so its mismatch count is zero.
Therefore `r=1`. An actual cycle with this word has least odd
period `2N`, since a repeated state would repeat its valuation
word as well.

This primitivity fact is preserved from the original argument,
but is not needed for the new finite closure. The reduced
integer-cycle correspondence, rederived in the
[paired-order node](../half-defect-positive-order-exclusion/README.md),
then gives the pure-word denominator statement.

## Certificates

Run `python3 areas/cycles/results/half-defect-imbalance-growth/check_imbalance.py`.
The default verifies its generated receipt; `--write-receipt`
regenerates it. The script uses exact integers and rational numbers,
works under `python3 -O`, and contains no floating-point inference.

It checks normalization and primitivity on a declared finite word
grid, all four raw inequalities (9) on actual reduced `3x+d`
cycles, every tied minimum, the fixed rational coefficients and
dyadic induction, the complete 4,194,303-member full-even-clock
interval calculation, the two exact-power bootstrap ranges,
and local descent below `18000000`. The finite word grids are
formula controls, not all-length absence arguments. The sole
external input EXT-1 is not rebuilt by these controls.
The normalization grid uses half lengths `2..5` and letters `1..3`,
giving 12,024 four-mismatch controls. The actual-cycle grid uses
block lengths and letters `1..3` and magnitudes `1..5`; its
eligible portion contains 24,772 cycles and 258,122 exact arrows.
All four minimum cases occur, including 7,534 equal-magnitude
and 10,038 opposite-parity controls. The local proof checks
8,999,999 odd starts strictly below `18000000`, excluding the base `1`.

The actual negative-order control `(1,1,2,3)` with `d=47`
and states `73,133,223,179` is retained. Reversing the defect
ordering gives further actual controls; the certificate tests
their raw inequalities using `gamma=(3+d/M)/2`. It never applies
the integer-cycle cutoff on `kappa` to a control whose normalized
minimum is too small. All eleven shared positive `3x+5`, `3x+7`,
`3x+13`, and `3x+61` cycles are also replayed.

## Remarks

The [equal-amplitude exclusion](../equal-amplitude-half-defect-exclusion/README.md)
already proves `Delta=0` with the same sole input EXT-1 and a
smaller internal local replay. Its claim is preserved. The present
law adds an unbounded unequal-amplitude regime and includes
opposite-parity defects, which the same-parity Mersenne
parametrization does not cover.

This does not settle the half-period four-mismatch question.
It leaves a quantitatively large imbalance and specifies the arc
containing every minimum. No upper bound on either absolute magnitude
is inferred from the ratio estimates. Novelty is undetermined.

## History

- 2026-11-08: strengthened the original result with the forced
  minimum location and the `p>q` cone `p-q>3N/4`. Replaced the
  original Barina-dependent final closure by a complete internal
  full-even-clock gap bootstrap and local descent below `18000000`.
  The earlier `Delta<=N/8` exclusion under EXT-1 plus Barina remains
  valid as a weaker historical conclusion; Barina and its period
  node are no longer assumptions or proof dependencies here.
- 2026-11-08: retained the smaller member of every paired common
  block, treated both magnitude orders and both minimum locations,
  and derived the uniform imbalance law. The terminal division in
  the second `B[q]` copy is retained explicitly. Same-session
  audits are not recorded as independent review.
