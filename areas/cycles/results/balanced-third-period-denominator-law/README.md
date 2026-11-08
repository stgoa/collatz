---
id: balanced-third-period-denominator-law
kind: result
title: Balanced third-period defects force a cubic-factor denominator bound
status: written
claim: >
  Raw odd-only valuation words. Let w be positive of length 3g, with exactly four
  mismatches under shift g, and suppose its two exceptional track entries differ
  from their respective majority entries by +delta and -delta, delta >= 1.
  Let U be the length-g majority template, P = 3^g, Z = 2^sum(U),
  Phi = P^2+PZ+Z^2, and d0 = gcd(2^delta-1,Phi). If D_w > 0, then
  (den(w)*d0)^2*P^2 > 2^(2g+delta)*Z. Thus den(w)>1 whenever d0=1,
  in particular for delta=1 or 2; den(w)=1 would require
  2^delta > (4/3)^g. The retained-positive-terms corollary additionally
  proves den(w)>1 for every delta>=1. No bound on length, background letters or delta,
  no primitivity hypothesis and no external input are used. This covers balanced
  third-period defects, not arbitrary four-mismatch words.
authors:
  - Codex residue research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [equal-total-two-block-exclusion]
certificates: [check_third_period.py]
evidence:
  - "check_third_period.json: exact structural, coupled-congruence and actual-cycle controls"
tags: [cycles, denominators, four-mismatches, noncoprime-rotations, third-period]
---

# Balanced third-period defects force a cubic-factor denominator bound

## Statement

All letters are positive integers and the clock is raw odd-only. For a word
`w` of length `m`, write

```
C_w = sum_(j=0)^(m-1) 3^(m-1-j) 2^(w_0+...+w_(j-1)),
D_w = 2^sum(w)-3^m,     den(w) = D_w/gcd(C_w,D_w)  when D_w>0.
```

Suppose `m=3g` and shift `g` has exactly four mismatches. The same condition
holds for shift `2g`; these are precisely the nonidentity shifts whose track
length is three. There are exactly two nonconstant tracks modulo `g`, each
with one exceptional entry and two equal majority entries. All other tracks
are constant. The majority entries define a unique positive word `U` of
length `g`. In particular `g>=2`.

Assume the two signed changes from `U^3` are `+delta` and `-delta`, where
`delta>=1`. This balance is an additional hypothesis. Put

```
P = 3^g,       Z = 2^sum(U),       Phi = P^2+PZ+Z^2,
q = den(w),    d0 = gcd(2^delta-1,Phi).
```

If `D_w>0`, equivalently `Z>P`, then

```
(q*d0)^2 P^2 > 2^(2g+delta) Z,                         (1)
q*d0 > 2^(g+delta/2) sqrt(Z)/P
     > 2^(delta/2) (4/3)^(g/2).                      (2)
```

Consequently `d0=1` excludes `q=1`. This includes every `delta=1` or `2`,
because `Phi` is coprime to `3`. More generally `q=1` would require

```
2^delta > (4/3)^g.                                    (3)
```

The theorem has no length or letter bound. It applies to rational `3x+1`
cycles and, after reduction, actual positive odd `3x+q` cycles. It does not
exclude the latter for `q>1`. No primitivity assumption is needed, and no
external gap, convergence or period input is used.

**Retained-positive-terms corollary (added 2026-11-08).** Every word in the
balanced third-period class above with `D_w>0` has `den(w)>1`, for every `delta>=1`.
Thus this entire specified class is excluded for positive integer cycles
of the raw odd-only `3x+1` map, unconditionally. The quantitative laws
(1)--(3) are retained; the new corollary also uses the small-state
restriction particular to `3x+1`.

## Proof

### 1. Two exceptional tracks and the two placements

A cyclic track of length three has either zero mismatches, two mismatches
(two equal entries and one different entry), or three mismatches (all
entries different). Four total mismatches therefore consist of two tracks
with two mismatches each. This proves the majority-template description.
The changes occur in distinct columns modulo `g`.

Locate the positive change at position `p` and let `d` be the forward
chronological distance to the negative change, with `0<d<3g`. Distinct
columns exclude `d=g,2g`. Balance gives

```
sum(w)=3 sum(U),       D_w=Z^3-P^3=(Z-P)Phi.           (4)
```

If `d<g` or `d>2g`, a cyclic cut places both changes inside one length-`g`
block. The word then consists of two identical majority blocks and one
different block of the same length and total. The
[equal-total two-block theorem](../equal-total-two-block-exclusion/README.md)
gives `q>2^g Z/P`. The decreased majority letter is at least `delta+1`, so
`sum(U)>=g+delta` and `Z>2^delta`. Squaring the existing bound proves (1).
This aligned case is a reuse of that theorem.

If `g<d<2g`, set `l=2g-d` and `n=d-g`. Both are positive and `l+n=g`.
Cut just after the majority-template position of the negative change,
and split each template block into words `A B` of lengths `l,n`. Then,
up to cyclic rotation, the actual word is

```
W = A[+delta] B  A B[-delta]  A B,                    (5)
```

where brackets change only the final letter of the indicated word.
In particular `last(B)>delta`. This unaligned case is treated below.

Cyclic rotation preserves the denominator: for a one-letter rotation `R`,
`2^(w_0) C_(Rw)=3C_w+D_w`. Since `D_w` is odd and coprime to `3`, this
identity preserves `gcd(C_w,D_w)`. Thus either placement can be analysed
at the stated cut.

### 2. The cubic residue

For the two nonempty words in (5), define

```
alpha=3^len(A), beta=3^len(B), Q=2^sum(A), S=2^sum(B),
C=C_A, E=C_B, P=alpha*beta, Z=Q*S,
X=beta*C, Y=Q*E, k=2^delta, R=P*X-Z*Y.
```

Changing a final letter leaves that block's intercept unchanged. Expanding
the six block contributions in (5) gives

```
C_W = X P^2 + k Y P^2 + k X PZ + k Y PZ + X Z^2 + Y Z^2
    = (X+kY)Phi + (k-1)Z R.                         (6)
```

By definition `D_w` divides `q C_W`. Since `Phi` divides `D_w` and is
coprime to `Z`, equation (6) implies `Phi | q(k-1)R`. Put

```
d1 = gcd(q(k-1),Phi).
```

Cancelling this gcd shows that `Phi/d1` divides `R`, hence
`d1 R=h Phi` for an integer `h`. The elementary primewise gcd inequality
also gives

```
d1 <= q gcd(k-1,Phi) = q*d0.                         (7)
```

### 3. The coupled positive lattice

Reduction of `d1 R=h Phi` modulo `Z` cancels powers of `3`; reduction
modulo `P` cancels powers of `2`. It follows that there are integers `t,s`
with

```
d1 C = h alpha + Z t,       d1 E = -h S + P s.       (8)
```

Substitution back into `d1 R=h Phi` gives the coupling equation

```
beta t-Q s=h.                                        (9)
```

Both `t` and `s` are strictly positive. If `h>=0`, the second equation
of (8) first gives `s>0`, then (9) gives `t>0`. If `h<=0`, the first
equation of (8) gives `t>0`, then (9) gives `s>0`. This argument retains
both signs of the residue `R`.

The intercepts of the two template rotations therefore satisfy

```
d1 C_AB = beta P t + Q Z s > Q Z,
d1 C_BA = alpha P s + S Z t > S Z.                  (10)
```

For any positive word `v` of length `g` and total `T`, every prefix of
length `j` has total at most `T-(g-j)`. Termwise summation gives

```
0<C_v <= 2^(T-g)(3^g-2^g) < 2^T 3^g/2^g.          (11)
```

Apply (11) to `BA`. Also apply it to the positive word `A B[-delta]`:
its intercept is still `C_AB`, but its total is `sum(AB)-delta`. Thus

```
C_AB < ZP/2^(g+delta),      C_BA < ZP/2^g.
```

Together with (10), these give

```
Q < d1 P/2^(g+delta),       S < d1 P/2^g,
Z=QS < d1^2 P^2/2^(2g+delta).                       (12)
```

Combining (7) and (12) proves (1). Since `Z>P=3^g`, (2) follows.
If `q=1`, then `d0<=2^delta-1<2^delta`; substituting this into (1)
and again using `Z>P` proves (3).

### 4. Retaining both positive terms excludes denominator one

The aligned placement is already excluded by section 1. Suppose an
unaligned word had `q=1`. Its rotated intercepts divided by `D_w` are
positive integers by the rotation identity in section 1. They are odd
because both intercepts and `D_w` are odd, so that identity gives a genuine
positive odd-only `3x+1` cycle with exactly the displayed valuations.

Now `d1=gcd(k-1,Phi)<k`. Retain both terms in the first identity of (10),
using `t,s>=1`, instead of using one term at a time:

```
beta P+QZ <= d1 C_AB < k C_AB < ZP/2^g.              (13)
```

It follows simultaneously that

```
Q < P/2^g,          beta < Z/2^g.                   (14)
```

Write `l=len(A)`, `n=len(B)`, `T=sum(AB)`, and `a0=log2(3)`.
Since `l+n=g`, `Q>=2^l`, and `beta=3^n`, (14) implies

```
l < (a0-1)g,       n > (2-a0)g,
T > g+a0 n > (1+2a0-a0^2)g > 41g/25.               (15)
```

The last strict inequality is exact: `1<a0<8/5` follows from
`2<3` and `3^5=243<256=2^8`, while

```
1+2a0-a0^2-41/25 = (8/5-a0)(a0-2/5) > 0.
```

On the other hand, this integer cycle has minimum at least `9`. A cycle
containing `1` is the all-`2` word, inconsistent with four mismatches.
The other smaller odd possibilities descend below themselves:

```
3 -> 5 -> 1,       5 -> 1,       7 -> 11 -> 17 -> 13 -> 5.
```

These are exact odd-only `3x+1` arrows, replayed by the certificate.
Thus a cycle minimum cannot be `3`, `5` or `7`. Multiplying the genuine
cycle equations, with all states `x_i>=9`, gives

```
2^(3T) = product_(i=0)^(3g-1) (3+1/x_i) <= (28/9)^(3g),
T/g <= log2(28/9) < 41/25.                           (16)
```

The final comparison is the integer inequality
`28^25 < 2^41*9^25`, verified exactly in the receipt. Equations (15) and
(16) contradict one another. Repeated cycles cause no problem: the
product uses the displayed `3g` odd arrows, and the exclusion of the
all-`2` word does not require a least-period assumption.

## Certificates

[`check_third_period.py`](check_third_period.py) reconstructs the majority
template and both placements, checks (6), (8)--(12), and constructs actual
reduced positive odd `3x+q` cycles. It checks the sharper final-letter
bound with its factor `2^delta`, including both signs of `h`. The receipt
[`check_third_period.json`](check_third_period.json) records the finite
ranges, counts and examples. These finite controls test the written
identities; they are not a search-based proof of the unbounded claim.

The retained-terms extension checks the `q`-scaled version of (13) on
every generated positive unaligned word, the three exact local descents,
the quadratic factorization in (15), and the integer power comparison
in (16). The finite descent is the only orbit computation of the
all-`delta` corollary; its three paths are displayed above.

All eleven shared actual `3x+5`, `3x+7`, `3x+13` and `3x+61` fixtures
are replayed with exact valuations. The certificate states which fixtures
meet the third-period and balance hypotheses. Generated examples inside
the theorem's class retain their actual denominator `q`; it is never
replaced by `1`.

Run from the repository root:

```
python3 areas/cycles/results/balanced-third-period-denominator-law/check_third_period.py
python3 -O areas/cycles/results/balanced-third-period-denominator-law/check_third_period.py
```

The default command verifies the committed receipt. The option
`--write-receipt` regenerates it deterministically.

## Remarks

The new coupling is between two exceptional columns of a third-period
template. The aligned placement already belongs to the
[equal-total two-block theorem](../equal-total-two-block-exclusion/README.md).
The [shared-background law](../shared-background-denominator-law/README.md)
instead puts varying markers in one column between copies of a common
background. The [coupled mismatch-cut system](../coupled-defect-matrix-smith-form/README.md)
does not by itself supply the positive lattice parameters in (8)--(9).
The half-period [Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md)
has a different quotient clock. Novelty is undetermined.

The imbalance of the two exceptional entries remains outside the theorem.
The original cubic bound retains the factor `d0` for balanced changes
with `delta>=3`. The added retained-terms corollary removes this obstruction
for denominator one throughout the balanced class. For general `3x+q`,
the product has `3+q/x_i` in place of `3+1/x_i`, and the local descent
restriction belongs specifically to `3x+1`; the actual `q>1` controls
therefore survive.
It does not resolve the general rotation-distance question.

## History

- 2026-11-08: derived the majority-track reduction and cubic-factor lattice
  law; retained the aligned case as an application of the existing
  two-block theorem. The final-letter positivity strengthens the bound by
  `2^delta`. Same-session mathematical checks by the directing and formal
  lanes do not change the `written` status.
- 2026-11-08: after the initial denominator law was merged, retained both
  positive lattice terms to exclude denominator one for every balanced
  change size. Added the exact small-state and slope comparisons; kept
  the original quantitative claim and proof. No external input or
  independent-session review status was added.
