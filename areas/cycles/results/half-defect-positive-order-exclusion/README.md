---
id: half-defect-positive-order-exclusion
kind: result
title: A forbidden paired-state order in two-defect half-period words
status: written
claim: >
  In the raw odd-only clock, let A,B be nonempty positive valuation words,
  let 1<=p<q, and let A[p],B[q] increase only their final letters.
  No positive odd integer 3x+1 cycle with word W=A B A[p] B[q] has its
  state after A greater than its state after A B A[p]. More generally,
  for an actual positive odd integer 3x+d cycle with positive odd d and
  boundary states x->z->y->t->x, put a=len(A), Q=2^sum(A), S=2^sum(B),
  k=2^p, l=2^q. Then H=(y-x)/Q is a positive odd integer and
  L=(z-t)/S is a nonzero odd integer. If L>0, then
  d>2^a*H*(l-k)/((k-1)*(l-1))>2^a/2^(p+1) and
  d>2^a*S/3^a; if q>=2p, also d>2^a/2^p.
  Equivalently, if D_W>0 and C_(rotate(W,len(A))) exceeds
  C_(rotate(W,2len(A)+len(B))), then den(W)>1.
  Both defect parities are allowed; the opposite paired-state order,
  equal magnitudes, and the reverse magnitude ordering are not excluded.
authors:
  - Codex arithmetic research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex root research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
certificates: [check_order_bound.py]
evidence:
  - "check_order_bound.json: polynomial identities, exact scalar bounds, small-state descent, reduced-cycle grid and shared actual-cycle controls"
tags: [cycles, half-defects, denominators, exact-arithmetic, paired-states]
---

# A forbidden paired-state order in two-defect half-period words

## Statement

All cycles use the raw odd-only map `n -> (3n+d)/2^v_2(3n+d)`.
The additive parameter is `d`; `p,q` are defect magnitudes. For a
nonempty positive valuation word, `[j]` increases only its last letter
by `j`. Let

```
W = A B A[p] B[q],       1 <= p < q,
a = len(A), b = len(B), n = a+b,
P = 3^a, R = 3^b, Q = 2^sum(A), S = 2^sum(B),
k = 2^p, l = 2^q.
```

The word has length `2n` and exactly four mismatches under its
half-period rotation. No primitivity, length, letter-size, or parity
assumption is made beyond those displayed.

Suppose a positive odd integer `3x+d` cycle, with positive odd `d`,
has boundary states

```
x --A--> z --B--> y --A[p]--> t --B[q]--> x.
```

Then `x<y`, and the two quantities

```
H = (y-x)/Q,             L = (z-t)/S                    (1)
```

are integers: `H` is positive odd, and `L` is odd and nonzero.
These letters denote paired differences here, not cycle extrema.
If the actual states satisfy **`z>t`**, equivalently `L>0`, then

```
d > 2^a H(l-k)/((k-1)(l-1)) > 2^a/2^(p+1),
d > 2^a S/P.                                            (2)
```

If also `q>=2p`, then `d>2^a/2^p`. In particular, the first
inequality would force `a<=p` at `d=1`, or `a<p` when `q>=2p`.
In fact the two retained inequalities together imply the stronger
conclusion:

**There is no such `3x+1` cycle with `z>t`.**

For a pure-word formulation, let
`D_W=2^sum(W)-3^len(W)>0` and
`den(W)=D_W/gcd(C_W,D_W)`, with the usual additive-one intercept.
The sign condition is exactly

```
C_(rotate(W,a)) > C_(rotate(W,2a+b)).                    (3)
```

Under (3), `den(W)>1`; the inequalities (2) also apply with
`d=den(W)` and with `H` from the reduced integer cycle.

## Proof

### 1. The exact paired differences

The affine composition for a word `U` is
`F_U(v)=(3^len(U)*v+d*C_U)/2^sum(U)`.
Increasing its last letter leaves `C_U` unchanged. Thus the four
boundary equations are

```
Qz = Px+dC_A,          Sy = Rz+dC_B,
kQt = Py+dC_A,         lSx = Rt+dC_B.                    (4)
```

The maps are strictly increasing on positive arguments, and
`F_(A[p]B[q])(v)<F_(AB)(v)` there. If `x>=y`, then
`y=F_(AB)(x)>=F_(AB)(y)>F_(A[p]B[q])(y)=x`, a contradiction.
Hence `x<y`.

Subtracting the two equations belonging to each repeated block gives

```
Q(z-kt)=P(x-y),          S(y-lx)=R(z-t).                 (5)
```

Since `P,R` are odd and `Q,S` are powers of two, these prove the
integrality in (1). The factors `z-kt` and `y-lx` are odd because
all four states are odd and `k,l` are even. Therefore `H,L` are
odd, `H>0`, and `L!=0`. In particular, neither quotient is an
extra integrality hypothesis.

Solving the two differences gives

```
x = (QH-RL)/(l-1),       t = (SL+PH)/(k-1),
y = x+QH,               z = t+SL.                       (6)
```

### 2. Keeping both positive terms

Substituting (6) into the first equation of (4) yields the identity

```
d(k-1)(l-1)C_A
  = [kQS(l-1)+PR(k-1)]L + PQ(l-k)H.                    (7)
```

For comparison, the other intercept satisfies

```
d(k-1)(l-1)C_B
  = [lQS(k-1)-PR(l-1)]H - RS(kl-1)L.                   (8)
```

Only (7) is needed for the exclusion. Under `p<q` and `L>0`,
every displayed summand in (7) is positive.

For every positive word `A`, the elementary intercept estimate is

```
2^a C_A < P Q.                                          (9)
```

Indeed, if `s_j` is the sum of its first `j` letters, then
`sum(A)-s_j>=a-j`, and

```
C_A/Q = sum_(j=0)^(a-1) 3^(a-1-j)2^(s_j-sum(A))
      <= sum_(j=0)^(a-1) 3^(a-1-j)2^(-(a-j))
       = (3/2)^a-1 < (3/2)^a.
```

Keeping the final term of (7), then using (9), gives

```
d > 2^a H(l-k)/((k-1)(l-1)).                            (10)
```

Since `l>=2k`, writing `l=2k+s`, `s>=0`, gives

```
2k(l-k)-(k-1)(l-1) = (k+1)s+3k-1 > 0.
```

Together with `H>=1`, this proves the first line of (2).
When `q>=2p`, write `l=k^2+s`; then
`k(l-k)-(k-1)(l-1)=s+k-1>0`, proving the sharper bound.

Keeping instead the first term of (7) gives

```
d > 2^a kSL/(P(k-1)) > 2^a S/P,                         (11)
```

which proves the second line of (2). Dropping this term would
lose the all-length contradiction below.

### 3. The integer-cycle contradiction without logarithms

Suppose now `d=1`. From (10), `a<=p`. From (11) and `sum(B)>=b`,

```
3^a > 2^a S >= 2^(a+b) = 2^n.
```

The exact inequality `3^5=243<256=2^8` therefore gives

```
5n < 8a.                                                (12)
```

Write `E=sum(W)=2(sum(A)+sum(B))+p+q`. Since `q>=p+1`,

```
E >= 2n+2a+1,             hence 4E > 13n.                (13)
```

The word cannot consist entirely of valuation `2`: its corresponding
last letters in `A` and `A[p]` differ. Thus its `3x+1` cycle is
nontrivial. Every positive odd state below `13` reaches `1`:

```
3 -> 5 -> 1,
7 -> 11 -> 17 -> 13 -> 5 -> 1,
9 -> 7 -> 11 -> 17 -> 13 -> 5 -> 1.
```

The remaining starts `1,5,11` occur in these chains. A raw cycle
containing any of them would be the fixed cycle at `1`, so every
state in the hypothetical cycle is at least `13`.
Multiplying its `2n` actual odd-only equations gives

```
2^E = product_i (3+1/x_i) <= (40/13)^(2n).
```

But the exact integer comparison

```
40^8 = 6553600000000
     < 6682466066432 = 2^13*13^8
```

implies, after raising the product inequality to the fourth power,

```
2^(4E)*13^(8n) <= 40^(8n) < 2^(13n)*13^(8n).
```

Hence `4E<13n`, contradicting (13). This uses only the displayed
finite descents and integer inequalities; there is no imported period,
convergence threshold, or logarithmic-form bound.

### 4. Word correspondence and the other sign

For completeness, let `G=gcd(C_W,D_W)`. The elementary rotation
identity

```
2^w_i C_(rotate(W,i+1)) = 3C_(rotate(W,i))+D_W
```

shows inductively that `G` divides every rotated intercept, since
`G` is odd. All these intercepts are positive odd integers. Thus
`x_i=C_(rotate(W,i))/G`, with `d=D_W/G`, gives a closed sequence
of positive odd integers with exactly the prescribed valuations.
This proves the pure-word statement and the equivalence (3).

The same equations (4)--(7) hold for all positive `p,q`.
If `p>q`, the last term in (7) is negative, while its left side is
positive, so necessarily `L>0`, for every positive addend `d`.
Combined with the exclusion just proved, a `3x+1` cycle in this
displayed double-increase form with `p!=q` would satisfy
`sign(L)=sign(p-q)`. This is a constraint on paired-state order,
not an exclusion of the reverse magnitude ordering.

## Certificates

Run `python3 areas/cycles/results/half-defect-positive-order-exclusion/check_order_bound.py`.
The default checks the generated receipt exactly; `--write-receipt`
regenerates it. All checks remain active under `python3 -O`.

The certificate verifies the polynomial identities (5), (7), (8),
the scalar positive-slack identities used in (10), and the exact
constants and small-state descents in the contradiction. It also
constructs reduced actual `3x+d` cycles for a declared finite grid
of positive blocks and defects, checking every arrow, quotient,
rotated-intercept sign and applicable bound. This grid is a control
of the formulas, not the proof of all-length exclusion.
The declared grid uses block lengths `1..3`, block letters `1..3`,
and both defect magnitudes `1..5`; its positive-gap portion contains
37,796 actual reduced cycles and 395,316 exact arrows, including
13,024 instances of the main positive-order bound.

Two particularly useful actual cycles are:

| Word | Addend `d` | Actual states `x,z,y,t` | `H` | `L` | Role |
|---|---:|---|---:|---:|---|
| `(1,1,2,3)` | 47 | `73,133,223,179` | 75 | -23 | Opposite-parity negative-order branch; not excluded |
| `(1,1,3,4)` | 431 | `89,349,739,331` | 325 | 9 | Positive-order branch with `d>1`; satisfies the bounds |

The first control even has every normalized state `x_i/d>1`.
The certificate also replays the eleven shared actual `3x+5`,
`3x+7`, `3x+13`, and `3x+61` fixtures with their true addends.

## Remarks

This result does not assume same-parity defects, unlike the
[two-segment Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md).
It also does not imply that an arbitrary half-defect normalization
has `p<q` in this order, or that its paired state difference is
positive. The negative-`L` control prevents either sign from being
silently discarded. No full half-period four-mismatch exclusion
is claimed. Novelty is undetermined.

The quadratic norm alone supplies no extra congruence. To see this,
put `X=R C_A`, `Y=Q C_B`, `alpha=PR`, `beta=QS`. For the two halves,

```
C_(AB)=X+Y,              C_(A[p]B[q])=X+kY,
D_W=kl beta^2-alpha^2,
F=kl(X+Y)^2-(X+kY)^2
 =(kl-1)X^2+2k(l-1)XY+k(l-k)Y^2.
```

The cycle divisibility implies `D_W | d^2 F`, by multiplying
`d(alpha C_(AB)+beta C_(A[p]B[q]))` by its conjugate and
cancelling the dyadic unit `beta^2`. Thus this norm condition
is a consequence of the original cycle equation, even when
`p+q` is odd. The useful new ingredient here is the sign of
the retained terms in (7), consistent with the warnings in
[coupled defect elimination](../coupled-defect-matrix-smith-form/README.md).

## History

- 2026-11-08: derived the exact paired quotients and retained-term
  denominator bounds while investigating opposite-parity half defects;
  retaining both positive terms gives the unconditional positive-order
  exclusion. Same-session mathematical and computational scrutiny does
  not constitute an independent review or a formal proof.
