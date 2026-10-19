# C003 — Uniform denominator escape from repeated block spacing

**Status: written elementary proof; root and separate-lane review complete.** This note
uses positive valuation words for the raw odd-only `3x+1` map. State 1 is
not absorbing in the algebra. A rational cycle with reduced denominator
`d` becomes an integer cycle for the raw `3x+d` map after scaling every
state by `d`. The result restricts one structural class of cycle words;
it does not classify arbitrary Collatz cycle words or divergence.

## 1. Notation and exact affine trapping

For a nonempty valuation word `z=(a_0,...,a_(m-1))`, all `a_i>=1`, put

```
A_j=a_0+...+a_(j-1),  A_0=0,  A=A_m,
C_z=sum_(j=0)^(m-1) 3^(m-1-j) 2^A_j,
Q_z=2^A,  P_z=3^m,  D_z=Q_z-P_z.
```

The block action is `f_z(x)=(P_z*x+C_z)/Q_z`. We consider two words
`u,v` with **both** `D_u,D_v>0`. Set

```
Q=Q_u, P=P_u, S=Q_v, R=P_v,
a=C_u/D_u, b=C_v/D_v,
alpha=P/Q, beta=R/S,
K=D_u*C_v-D_v*C_u.
```

Thus `0<alpha,beta<1`, `a,b>0`, and
`|b-a|=|K|/(D_u*D_v)`. If `K=0`, the two blocks have the same fixed
point and, by deterministic exact valuations, are powers of the same
primitive cycle word in the same phase. We assume `K!=0` below.

For `w=u^k v^ell`, `k,ell>=1`, let `x` be the rational cycle state
before the first `u` and `y` the state before the first `v`. With
`t=alpha^k` and `z=beta^ell`, solving
`y=a+t(x-a)` and `x=b+z(y-b)` gives

```
x=a+(b-a)*(1-z)/(1-t*z),
y=a+t*(x-a).                                             (1)
```

The coefficient `(1-z)/(1-t*z)` lies strictly between 0 and 1.
Consequently `x`, `y`, and **every block-boundary state** during the
`u` and `v` repetitions lie strictly between `a` and `b`. The claim
here concerns block boundaries; no bound on all intermediate odd
states inside either block is needed.

The rational cycle is positive because
`Q^k*S^ell>P^k*R^ell`. Its reduced denominator is

```
d=den(w)=(Q^k*S^ell-P^k*R^ell)/gcd(C_w,Q^k*S^ell-P^k*R^ell).
```

Every rotated state has that same reduced denominator. Thus all
block-boundary values multiplied by `d` are integers; these are exact
states of the integer raw `3x+d` cycle.

## 2. Lattice spacing and the exact fixed-pair bounds

For `0<=i<=k`, set `n_i=d*f_u^i(x)`, an integer. For
`0<=i<k`, let `Delta_i=n_(i+1)-n_i`. Because `f_u` is affine with
slope `P/Q`,

```
Delta_i=(P/Q)^i*Delta_0.                                (2)
```

Here `gcd(P,Q)=1`, and `Delta_(k-1)` is an integer. The initial
difference is nonzero: `Delta_0=0` would imply `x=a`, contrary to
`K!=0` and (1). Equation (2) therefore forces

```
Q^(k-1) divides Delta_0,  |Delta_0|>=Q^(k-1).           (3)
```

On the other hand, (1) and `f_u(x)-x=-(D_u/Q)(x-a)` give the exact
quantity

```
|Delta_0|=
  d*|K|/(Q*D_v) * (1-beta^ell)/(1-alpha^k*beta^ell)
  < d*|K|/(Q*D_v).                                     (4)
```

Combining (3) and (4), then rotating the word to start with `v`,
proves two strict bounds for every `k,ell>=1`:

```
d > Q^k*D_v/|K|,       d > S^ell*D_u/|K|.              (5)
```

These bounds need no proportional valuation slopes and no gcd
estimate for two geometric sums. They also give effective finite
exponent ranges for each fixed contracting pair with `K!=0`.
The C002 S-unit argument still covers unequal-slope pairs containing
an expanding block and gives a stronger full leading rate there.

## 3. Uniform theorem over varying blocks and totals

Write `m_u=len(u)`, `m_v=len(v)`,
`M=max(m_u,m_v)`, and `Q_*=max(Q,S)`. Denote by `t_*` the repetition
count of a selected block attaining `Q_*`; when `Q=S`, select a block
whose count is at least 3 if one exists.

**Theorem.** If `K!=0` and `t_*>=3`, then

```
den(u^k v^ell) > 2^M * Q_*^(t_*-3) >= 2^M > 1.       (6)
```

The assertion is uniform over *all* positive contracting blocks,
including blocks with different lengths, totals and valuation slopes.
It excludes an ordinary integer `3x+1` cycle in this structural class.
In particular, it applies if both repetition counts are at least 3,
or if the block with the larger valuation total occurs at least 3 times
while the other block occurs at least once. Primitivity of the blocks
or the whole word is not assumed.

**Proof.** The positive valuations imply
`A_j<=A-(m-j)` and hence the universal intercept estimate

```
0<C_z<=Q_z*((3/2)^m-1)<Q_z*3^m/2^m.                  (7)
```

Because `D_z=Q_z-3^m` is a positive integer,
`Q_z/D_z=1+3^m/D_z<=3^m+1`. Its positive fixed point therefore obeys

```
x_z=C_z/D_z < F(m),
F(m)=(3^m+1)*3^m/2^m=(9/2)^m+(3/2)^m.            (8)
```

The function `F` strictly increases on positive integers. The block
of length `M` is contracting, so its binary power exceeds `3^M` and
`Q_*>=3^M+1`. Consequently

```
max(a,b)<F(M)<Q_*^2/2^M.                            (9)
```

All block-boundary states lie between `a` and `b`, so the first
difference for the `Q_*` block has absolute value less than
`d*|a-b|<d*Q_*^2/2^M`. Its lattice spacing from (3), applied to that
block after rotating if necessary, is at least `Q_*^(t_*-1)`.
Rearranging gives (6). The strict bound uses `K!=0` to ensure that
the difference is nonzero. This proves the theorem.

**Effective finiteness.** Fix a denominator ceiling `d_0`.
In this class, `d<=d_0` and (6) force `2^M<d_0`, so both block
lengths are bounded. Equations (3) and (8) give

```
Q_*^(t_*-1)<d*F(M)<=d_0*F(M),
Q_*^2<d_0*F(M).                                       (10)
```

Thus both binary powers and valuation totals are bounded explicitly.
There are finitely many positive valuation words with those length and
total bounds. For each pair, (5) bounds both repetition counts.
This is a finite enumeration procedure for every bounded denominator
layer of the stated class, even while the two blocks vary. No result
about the two-block words outside its hypotheses follows from this
finiteness statement.

## 4. Proportional-slope comparison

The original C003 candidate assumed proportional totals
`(sum(u),len(u))=(ar,br)` and `(sum(v),len(v))=(as,bs)`, with
`gcd(a,b)=1` and `U=2^a>V=3^b`. Put `T=V/2^b=(3/2)^b` and
`h=gcd(rk,s*ell)`. Equation (7) gives
`C_u<U^r*T^r` and `C_v<U^s*T^s`. Both `D_u,D_v` are positive, so

```
|K|=|D_u*C_v-D_v*C_u|
   <max(D_u*C_v,D_v*C_u)
   <U^(r+s)*T^max(r,s).                               (11)
```

The proportional cancellation theorem in
[C002](../C002/PROPORTIONAL.md) has `den>U^(rk+s*ell-h)/J_0`,
where `J_0<=|K|`. If `k,ell>=3`, then
`rk+s*ell-h>=max(rk,s*ell)>=3*max(r,s)`; since
`r+s<=2*max(r,s)`, (11) yields

```
den(u^k v^ell)>(U/T)^max(r,s)
                  =2^(b*max(r,s))*(U/V)^max(r,s)
                  >2^M.                              (12)
```

This independent elementary calculation adds a slope-ratio factor
under proportionality. Section 3 is stronger in scope: it allows
unrelated slopes and requires three repetitions only of a block with
maximal binary power. The condition `t_*>=3` is a sufficient threshold
for this spacing argument, not a proved optimal threshold for all
cycle words. The remaining `t_*=2` cases are not declared possible
integer cycles.

## 5. Worked example, controls and remaining gap

Take `u=(1,2,2)` and `v=(2)`. Then
`(Q,P,D_u,C_u)=(32,27,5,23)` and
`(S,R,D_v,C_v)=(4,3,1,1)`, so `K=-18`. The slopes and block
totals differ. For `w=u^3 v`, direct concatenation gives
`C_w=213341`, `D_w=72023`, `gcd(C_w,D_w)=1` and
`den(w)=72023`. The exact bound (5) reads
`den(w)>32^3/18`, and the uniform bound (6) reads
`den(w)>2^3`.

The `K=0` exception is necessary. If `u=v=(2)`, the rational fixed
point is 1 and its denominator remains 1 under every repetition.
Powers of `(1,2,2)`, `(1,3)` and `(4)` likewise preserve reduced
denominators 5, 7 and 13, so their actual `3x+d` cycle controls are
unaffected. This note uses the raw map; whether an integer realization
meets an absorber is a separate convention.

The theorem assumes both blocks contract. With an expanding block,
its fixed point is negative and the positive interval trapping in
(1)–(9) fails. The separate [C003 proof](UNEQUAL_PROBE.md) gives uniform
asymptotic denominator escape even with an expanding block when both
counts are at least two; its threshold is ineffective. That result
does not extend this elementary all-size exclusion to expanding blocks.
The theorem also does not cover arbitrary primitive words that lack
three consecutive copies of a maximal binary-power block.

| Required field | Outcome |
| --- | --- |
| Objects | Reduced denominators of raw positive rational cycles `u^k v^ell`; both blocks individually contracting. |
| Structural gain | Uniform `den>2^M` with one maximal binary-power block repeated at least three times; effective bounded-denominator finiteness even as both blocks vary. |
| Translated unresolved gap | An arbitrary primitive cycle word need not have that repeated-block decomposition; expanding blocks and two-copy maximal blocks are outside the uniform theorem. |
| Worked example | `(1,2,2)^3(2)` has unequal slopes and denominator 72023, satisfying both exact and uniform bounds. |
| Known-cycle controls | The common-fixed-point case `K=0` retains actual d1/5/7/13 cycles. |
| Cheapest meaningful next test | Replay the new bounds on all eligible actual-cycle decompositions and a bounded generated grid with unequal slopes and unequal totals; retain raw arrows and record ineligible cases. |
| Intermediate milestone | An all-varying-block denominator restriction for a structural class strictly broader than the proportional-slope class. |

The exact word conventions and rotation fact are in
[R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md).
The earlier two-block gcd theorem and its limits are in
[C002](../C002/PROPORTIONAL.md). No novelty, human publication review
or formal verification is claimed for this written proof.
