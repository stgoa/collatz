---
id: general-three-label-four-arc-exclusion
kind: result
title: Integer repetition bounds exclude the three-label equal-outer four-arc family
status: written
claim: >
  Raw odd-only 3x+1 clock. Let a,b,c>=1, m=1+a+b+c,
  gcd(h,m)=1, and let A,B,V be pairwise distinct positive
  integer valuation labels. Suppose a word read along a
  cyclic h-track is V,A^a,B^b,A^c. Under EXT-1,
  m>=2^48 and D_w>0 imply den(w)>1. With the additional
  declared Barina convergence input, D_w>0 implies
  den(w)>1 at every length in this specified family.
  The new branch is V>t=max(A,B), where the cycle product
  forces {A,B}={1,t}. Exact integer repetition, without
  an expanding-block hypothesis, gives
  m<16j log_2(L+1)+27jQ for every proper rational phase
  Qk-pm=+j or -j with gcd(p,Q)=1 and k=h^(-1) mod m.
  Summing over all proper convergents bounds the complete
  continued-fraction cost, rather than selecting one
  large coefficient. A minimum-state and exact-gap bootstrap
  closes the remaining lengths under the declared period
  input. Other four-mismatch patterns and noncoprime tracks
  remain outside the claim. The first length cutoff uses
  neither LMN nor the Chim estimate nor the Barina input.
authors:
  - Codex four-arc research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [background-maximum-four-arc-exclusion, paired-state-run-law, sparse-two-level-four-arc-exclusion, denjoy-koksma-height-bound, four-mismatch-inverse-continued-fraction-bound, cycle-length-lower-bound-from-convergents]
assumes: [musson-collatz-gap-all, barina-2025-convergence-2-71]
certificates: [check_bootstrap.py, check_family_controls.py]
evidence:
  - "check_family_controls.json: label-independent geometry, minimum-return runs, weighted discrepancy, actual reduced cycles and replayed geometric/period certificates"
  - "check_bootstrap.json: exact logarithm enclosure, continued-fraction gap, dyadic cutoff and sourced period comparison"
tags: [cycles, four-arcs, rotation-distance, continued-fractions, integer-repetition, effective-exclusion]
---

# Integer repetition bounds exclude the three-label equal-outer four-arc family

## Statement

Use the raw odd-only clock. Let `a,b,c>=1`,
`m=1+a+b+c`, and `gcd(h,m)=1`. Suppose that reading a
positive valuation word along a cyclic index track gives

```
V,A^a,B^b,A^c,                                      (1)
```

where `A,B,V` are pairwise distinct positive integers.
The exponents in (1) count letters. The unique `V`
makes this word primitive.

Under [EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
m>=2^48 and D_w>0  imply  den(w)>1.                  (2)
```

With the additional declared
[Barina convergence input](../../../../sources/barina-2025-convergence-2-71.md),
the same exclusion holds without a length restriction.
That corollary uses the
[replayed raw odd-period bound](../cycle-length-lower-bound-from-convergents/README.md)
`72057431991`; it does not rerun the external convergence
computation. The large-period theorem (2) uses only EXT-1
and local descent through 127. Neither conclusion uses
the LMN or Chim estimates.

The earlier
[background-maximum result](../background-maximum-four-arc-exclusion/README.md)
already handles `max(A,B)>V`. The new argument treats
`V>max(A,B)` for arbitrary background labels. It does not
exclude arbitrary four-mismatch words or noncoprime tracks.

## Proof

Assume `D_w>0` and `den(w)=1`. The rotated intercept
identity `2^(w_i) C_next=3C_rot+D_w`, with `D_w` odd,
gives positive odd integer states with these exact
valuations. Uniqueness of `V` makes the resulting
cycle primitive and nontrivial. Let its minimum and
maximum be `L,H`, and write

```
alpha=log_2(3), rho=3/2, Y=log_2(L+1), ell=log_2(L),
E=sum(w), eta=(2^E-3^m)/2^E, k=h^(-1) mod m,
K=the sum of the partial quotients of k/m.
```

Use the canonical finite continued fraction, whose last
partial quotient is at least two. Local descent of all
odd seeds from 3 through 127 gives `L>=129`. The product
identity and exact comparisons from the background-maximum
proof give

```
kappa=alpha+1/[3L ln(2)] < 8/5,
E<8m/5,
0<eta<m/(3L),
ell<172+342log_2(m),
Y<173+342log_2(m).                                  (3)
```

Here the last two inequalities use EXT-1,
`eta>=2^-172*m^-341`. The elementary bound on `kappa`
uses `3^32<2^51`, `ln(2)>1/2`, and
`2/387<1/160`. No imported minimum bound is used in (3).

### 1. The background label is bounded by the minimum state

If both background labels were at least two, then
`E>=2m-1>8m/5` for `m>=4`, contradicting (3).
Thus `{A,B}={1,t}` for some `t>=2`.
The branch `t>V` follows from the cited background-maximum
theorem: its EXT-1-only cutoff `2^43` is below (2), and
its separately sourced all-length corollary has the same
external inputs as ours. Hence suppose

```
V>t>=2,             u=t-1.                          (4)
```

Every non-one letter is then at least `t`. The minimum
starts a positive maximal ones run: a non-one arrow
would decrease it, and a preceding one-arrow would
have a smaller state. Let this run have length `l>=1`,
followed by a letter `e>=t`. Exact oddness at its end gives

```
L+1=2^(l+1)z,       z a positive odd integer,
l+1<=Y.
```

The state after the `e`-arrow is at least `L`. Multiplying
the `l+1` step ratios, with every input at least `L`, gives
`l+e<=kappa(l+1)`. Consequently

```
u=t-1 <= e-1 <= (kappa-1)(l+1) < (3/5)Y.             (5)
```

This bound does not require any information about the
rotation or the location of the singleton.

### 2. A weighted discrepancy complement

Replace `V` by the outer label `A` to obtain a template
`U` with labels `1,t`. Its high letters occupy one cyclic
track interval, its variation on the track is `2u`, and
its chronological rotation step is the original `k`.
Let `beta` be its mean. The discrete
[Denjoy--Koksma bound](../denjoy-koksma-height-bound/README.md)
gives, for every proper chronological factor,

```
|sum(factor)-beta*length|<=Delta,   Delta=2u(K-1).     (6)
```

We claim that, for `m>=2^22`,

```
uK>m/512.                                          (7)
```

Suppose otherwise, so `Delta<m/256`. If `beta<alpha`,
every template factor has affine slope at least
`2^-Delta`. The spike-free path from the state `n0`
immediately after `V` to the minimum therefore gives
`n0<=2^Delta L`, also when the path is empty.

The label-independent geometric obstruction from
[the two-rotation result](../sparse-two-level-four-arc-exclusion/README.md)
applies to either outer label. To state the transfer,
put the singleton at index `x=m-1`. The four boundaries
are `x,x-h,P1,P2`, where `P1=x+ah`, `P2=x+(a+b)h`.
The mismatch set at `2h` is contained in
`{x,x-2h,P1,P1-h,P2,P2-h}`: the omitted point `x-h`
compares two copies of the outer label. These are exactly
the geometric lists in the 1440-cell rational certificate;
their inequalities contain no valuation labels. Coincident
and artificial cuts are allowed, and primitivity keeps
the paired states distinct. Reversing `h` if needed for
this geometry does not change the original `k` in (6).

At `L>=129`, every step has base-3 logarithmic growth
less than `3/8`, by `194^8<27*129^8`. The rational
certificate then requires

```
[log_3(n0)+1]/m > 1/193.
```

But (3), `alpha>3/2`, and `Delta<m/256` give

```
[log_3(n0)+1]/m
 < [173+342log_2(m)]/m+1/384 < 1/193.                 (8)
```

The last inequality holds for every `m>=2^22`: on
`2^d<=m<2^(d+1)` its right side is at most
`[173+342(d+1)]/2^d+1/384`, decreasing with `d`,
and at `d=22` it is `56885/12582912<1/193`.

If instead `beta>=alpha`, every template suffix slope
is at most `2^Delta`. The actual word is componentwise
at least the template, so the same bound holds for its
suffix slopes. The additive intercept of a factor is
one third of the sum of its nonempty suffix slopes.
The path from the minimum to the maximum thus gives

```
H<2^Delta(L+m/3).
```

Set `G=2^172*m^341`; (3) gives `L<mG/3`, hence
`H<(2/3)2^Delta mG`. On the other hand, the four-mismatch
end witness gives `H>(2/3)3^(m/4)`. Therefore

```
(95/256)m < 172+342log_2(m),                         (9)
```

using `alpha>3/2` and `Delta<m/256`. This is impossible
for `m>=2^22` by the same dyadic comparison (already
the base margin is positive). Both cases prove (7).

### 3. The logarithmic inverse-complexity bound

The [integer-repetition theorem](../four-mismatch-inverse-continued-fraction-bound/README.md),
sections 7--9, applies to every primitive integer cycle with exactly
four mismatches under a coprime rotation, without restrictions on
label sizes or arc lengths. Write `k/m=[0;a1,...,an]` canonically,
so `n` counts the positive partial quotients, excluding the initial zero.
With `Y=log_2(L+1)` it gives, without external inputs,

```
K<27n+64Y,       n<=2log_2(m)+1.                     (14)
```

Its key step uses integer differences between repeated blocks.
For a positive block of length `Q<m` and total `S`, repeated
`N` times, `2^(S(N-1))` divides a nonzero difference of integer
states. This bounds the repeated segment from its starting state
whether its affine map expands or contracts. Four track boundaries
supply a long prefix with at most five repeated-block regimes for
every proper rational phase. Summing the resulting constraints over
all proper convergents yields (14); no search for a large coefficient
or expansion condition on the blocks is needed here.

### 4. The first cutoff and the exact-gap bootstrap

For `m>=2^22`, combine (5), (7), and (14):

```
m < (1536/5)Y(27n+64Y).                             (15)
```

For `2^d<=m<2^(d+1)`, (3) and (14) bound its right side by

```
P(d)=(1536/5)(342d+515)
       *[27(2d+3)+64(342d+515)].                    (16)
```

At `d=48`, `P(48)=28249216922112/5<2^48`.
Both linear factors have positive coefficients, so
`P(d+1)/P(d)<=((d+1)/d)^2<2` for `d>=48`.
Induction proves `P(d)<2^d` throughout that range,
contradicting (15). This proves (2) in the new branch.

For the all-length corollary only, now invoke the declared
Barina input and its replayed period theorem. They imply
`m>=72057431991>2^22`, so (7)--(15) apply. The theorem
just proved also gives `m<2^48`.

The certificate constructs a rational enclosure of
`alpha` from the positive series for the logarithms,
and verifies the consecutive convergents

```
p/q   =83130157078217/52449289519716 < alpha,
p'/q' =683381996816440/431166034846567 > alpha,
p'q-pq'=1, q'>2^48, q*alpha-p>2^-62.                (17)
```

Here is why (17) controls every positive gap in the
needed range, without assuming `m>=q`. Write the integers
`(m,E)=v(q,p)+w(q',p')` in this unimodular basis. If
`0<m<q'` and `E-m alpha>0`, then `w>=1` and `v<=-1`:
`w<=0` would force `v<0` from the positive gap and then
`m<0`, while `w>=1` and `m<q'` force `v<0`.
It follows that

```
E-m alpha > q*alpha-p > 2^-62.
```

Since `ln(2)>1/2`, this gives
`Lambda=E ln(2)-m ln(3)>2^-63` and
`eta=1-exp(-Lambda)>Lambda/(1+Lambda)>2^-64`.
The product bound in (3) now yields

```
L<m*2^64/3,       Y<112,       n<=97.
```

Substituting into (15),

```
m < (1536/5)*112*(27*97+64*112)
  =1683677184/5 < 72057431991.                       (18)
```

This contradicts the imported raw odd-period lower bound.
The exact logarithm enclosure and gap arithmetic in
(17) are reproduced in this node's certificate; they
do not import the LMN or Chim estimates. Together with
the already settled `t>V` branch, this proves the
all-length corollary for (1).

## Certificates

Run the standard-library certificates from the repository root:

```
python3 areas/cycles/results/general-three-label-four-arc-exclusion/check_bootstrap.py
python3 areas/cycles/results/general-three-label-four-arc-exclusion/check_family_controls.py
```

The [bootstrap checker](check_bootstrap.py) and generated
[receipt](check_bootstrap.json) independently verify the exact logarithm
bracket, numerical cutoff and sourced period comparison. The
[family checker](check_family_controls.py) and its generated
[receipt](check_family_controls.json) check the label reduction and
weighted template identities on 110,880 finite geometry words,
107,280 actual reduced cycles, 1,909 exact minimum-return segments,
and 868,496 proper discrepancy factors. The eleven standard
`3x+5,7,13,61` cycles retain their true addends. The geometric
certificate and continued-fraction period certificate are replayed;
the external Barina convergence computation is not rerun.

Both checkers run with `python3 -O`; failed checks raise exceptions
rather than relying on assertions. Use each script's
`--write-receipt` option to regenerate its receipt. The universal
claims rest on the written argument and declared dependencies,
not on finite absence searches. The general repeated-block and
phase checker lives with the inverse-complexity theorem.

## Remarks

The key replacement for the earlier
[two-level phase argument](../two-level-four-arc-phase-exclusion/README.md)
is the exact repetition bound in the inverse-complexity theorem. Larger background labels can make
short blocks contract; the present proof needs no uniform
expansion. The phase geometry supplies a long prefix with
only a few repeated blocks, and integer differences bound
its length starting at the minimum. Summing over all
convergents then controls the full discrepancy cost.

This is not the purely combinatorial bounded-period
reduction refuted in
[the sparse-rotation obstruction](../sparse-rotation-bounded-period-reduction-obstruction/README.md).
The period `Q` varies with the chosen convergent; only one
prefix is used, and the length estimate depends on integer
cycle states. Arbitrary positive rational cycles do not
provide the same bound in terms of their normalized minimum.

For `3x+d`, the exact repeated-block difference divisibility
still holds for integer states, but the growth comparison
uses `x+d`, not `x+1`. Normalizing the states by `d` loses
the integer lower bound on the nonzero difference. Likewise
the minimum and product estimates retain `d`. The actual
other-addend controls are therefore not excluded.

Novelty beyond the repository is undetermined. The
continued-fraction identities, discrepancy estimate and
integer difference law are classical or already present
here. Same-session mathematical and computational audits
do not confer independent-review or formal status.

## History

- 2026-11-08: combined the all-convergents phase estimate,
  weighted discrepancy complement and exact-gap bootstrap
  to cover all three distinct positive labels in the
  equal-outer coprime-track shape. Preserved the EXT-1-only
  `2^48` theorem separately from the all-length corollary
  using the declared convergence-derived period input.
