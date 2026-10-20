# C003 — Uniform denominator growth for changing repeated blocks

**Status: written proof with published inputs; independent lane, 2026-10-19.**
The fixed-block restriction in C002's unequal-slope argument can be removed.
The key is one fixed ambient group of rational 2/3-units, containing the
parameters of every block. This proves uniform bounded-denominator
finiteness for a class whose two words and their totals may all vary.
The asymptotic thresholds are ineffective. An all-size nonintegrality
claim for an expanding/contracting pair remains unproved here.

The clock is raw odd-only Syracuse on positive odd rationals, without
making 1 absorbing. No novelty or formal-verification claim is made.

## 1. Objects and results

For each nonempty positive valuation word z, write

```
A_z=sum(z), m_z=len(z), P_z=2^A_z, Q_z=3^m_z,
C_z=sum_(j=0)^(m_z-1) 3^(m_z-1-j)*2^(a_0+...+a_(j-1)),
D_z=P_z-Q_z.
```

The affine action is `(Q_z*x+C_z)/P_z`. If D_z>0, its fixed point
has exact displayed valuations and common reduced denominator
`d_z=D_z/gcd(C_z,D_z)`, as derived in R71 and C001.

Now allow both words u,v to vary. Put

```
a=A_u, r=m_u, b=A_v, s=m_v,
w=u^k v^ell, A=a*k+b*ell, M=r*k+s*ell,
Delta=a*s-b*r, K=D_u*C_v-D_v*C_u,
G_u(k)=(P_u^k-Q_u^k)/D_u,
G_v(ell)=(P_v^ell-Q_v^ell)/D_v.
```

Assume k,ell>=q, where q is a fixed integer at least 2, and
`D_w=2^A-3^M>0`. In particular A>=M. Define

```
lambda=log(2)/log(3),
gamma_q=(2-lambda)/q,
nu_q=1-gamma_q.
```

**Theorem 1 — Changing unequal-slope blocks.** If Delta!=0, then
uniformly over all such words and exponent pairs,

```
liminf_(A->infinity) log(d_w)/(A*log2) >= nu_q>0.        (T1)
```

Precisely, for every eta>0 there is A_0(q,eta) such that every member
of the declared class with A>=A_0 satisfies

```
d_w >= 2^((nu_q-eta)*A).                              (T2)
```

The threshold does not depend on u,v. Therefore every bounded denominator
layer contains only finitely many representations in this entire varying-word
class. This already holds for q=2.

**Theorem 2 — Changing proportional blocks.** If Delta=0, K!=0 and
k,ell>=2, then uniformly over all changing words,

```
liminf_(A->infinity) log(d_w)/(A*log2) >= eta_*>0,
eta_*=(5*log_3(2)-3)/14.                              (T3)
```

This threshold is also ineffective as proved here. For q>=3, a separate
elementary bound holds at every size:

```
d_w > (1/2)*2^(rho_q*A), rho_q=1/2-gamma_q>0.          (T4)
```

Thus the cube case also has effective bounded-layer finiteness on the
proportional branch. Neither result fixes the block lengths, sums or ratio.

For reference, the rates for the specified lower repetition thresholds are:

| q | gamma_q | Unequal-slope lower rate nu_q | Proportional lower rate |
| --- | --- | --- | --- |
| 2 | 0.6845351232 | 0.3154648768 | 0.0110463406, using the refined argument below. |
| 3 | 0.4563567488 | 0.5436432512 | 0.0436432512 |

Combining the theorems: **all nondegenerate two-block representations
with k,ell>=2 have uniform bounded-denominator finiteness**, with no
equal-total or fixed-word restriction. Nondegenerate means K!=0.
The combined conclusion remains ineffective; the global square bounds
use the published asymptotic estimates.
No optimality of these rates is claimed.

## 2. A uniform intercept and commutator bound

Positive valuations give `A_z>=m_z` and, for each prefix,
`A_j<=A_z-(m_z-j)`. Therefore

```
C_z <= 2^(A_z-m_z)*(3^m_z-2^m_z)
    < B_z,
B_z=2^(A_z-m_z)*3^m_z.
```

Also `B_z>=3^m_z` and `B_z>2^A_z`; hence
`|D_z|<B_z`, regardless of the sign of D_z. Thus

```
|K| <= |D_u|*C_v+|D_v|*C_u
    < 2*B_u*B_v
    = 2*2^(a+b)*(3/2)^(r+s).                         (1)
```

Since k,ell>=q,

```
a+b<=A/q, r+s<=M/q,
M*log3<A*log2.
```

It follows that

```
log |K| < log2+(A/q)*log2+(M/q)*log(3/2)
        < log2+gamma_q*A*log2.                       (2)
```

This bound is uniform in both words and includes an expanding block.
It is the step that replaces C002's assumption that K is a fixed constant.

## 3. One fixed ambient group gives a global gcd estimate

The primary imported theorem is Corvaja–Zannier, *A lower bound for the
height of a rational function at S-unit points*,
[full preprint math/0311030v2](https://arxiv.org/pdf/math/0311030),
Corollary 1, Eq. (1.3), with its proof on printed pp. 16–17.
The exact statement, local conventions and full-source audit are recorded
in [C002/INDEPENDENT_SLOPES.md](../unequal-slope-two-block-growth/INDEPENDENT_SLOPES.md).

For any fixed finitely generated group Gamma of rational pairs and
epsilon>0, all but finitely many multiplicatively independent pairs
(X,Y) in Gamma satisfy

```
sum_nu log^- max(|X-1|_nu,|Y-1|_nu)
    >= -epsilon*max(h(X),h(Y)).                       (CZ)
```

Use the single group

```
Gamma=(<2,3>)^2
     =<(2,1),(3,1),(1,2),(1,3)>,
X=2^(a*k)/3^(r*k), Y=2^(b*ell)/3^(s*ell).
```

This Gamma is fixed even while every word parameter changes. If
`X^i Y^j=1`, its 2- and 3-valuations give a homogeneous system with
determinant `k*ell*Delta`. Thus Delta!=0 makes every pair independent.

Let `L_u=2^(a*k)-3^(r*k)` and `L_v=2^(b*ell)-3^(s*ell)`. Both are
nonzero integers prime to 6. At 2, X−1 and Y−1 are units; at 3 their
absolute values exceed 1. The two local contributions are zero.
At every other finite prime p the contribution is
`-min(v_p(L_u),v_p(L_v))*log p`. The archimedean term e_infty is
nonpositive. The entire sum in (CZ) is consequently

```
-log gcd(|L_u|,|L_v|)+e_infty.
```

Therefore, outside the finite exceptional set,

```
log gcd(G_u(k),G_v(ell))
    <= log gcd(|L_u|,|L_v|)
    <= epsilon*H,
H=max(a*k*log2,r*k*log3,b*ell*log2,s*ell*log3).
```

On the positive-cycle domain,

```
(A/2)*log2 <= H <= max(A*log2,M*log3)=A*log2.           (3)
```

Hence the finite exceptional pairs have bounded A, and

```
log gcd(G_u(k),G_v(ell))=o(A)                          (4)
```

uniformly over all changing words, positive cycles and unequal slopes.

There is no hidden infinite preimage of an exceptional pair. A rational
X fixes its exponents `a*k` and `r*k` uniquely, and positive k must divide
both of these fixed integers; similarly Y fixes finitely many choices for
ell,b,s. There are finitely many positive composition words at each fixed
length and sum. Equivalently, the lower bound in (3) already bounds A
on the exceptional set, and bounded A permits finitely many representations.

## 4. Denominator size near the expansion/contraction boundary

C002 proves, using Proposition 1, Eq. (2.2), of the same primary source,
the global power-gap estimate

```
log(2^A-3^M)=A*log2-o(A),                             (5)
```

uniformly over all positive integers A,M with `2^A>3^M`.
Its proof uses `f(X,Y)=X/Y-1` on `(2^A,3^M)` and explicitly handles
the exceptional translates. None of its constants depends on u or v.
Thus it remains valid when the combined ratio approaches 1, and when
one block expands. It does not assume a fixed separation from 1.

The exact two-block elimination identities give, for
`g=gcd(C_w,D_w)`,

```
g divides |K|*gcd(G_u(k),G_v(ell)).                    (6)
```

In the positive domain Delta!=0 implies K!=0: if K=0, both block
differences have the same sign; they cannot both be negative. Their
positive rational fixed points would coincide, and deterministic exact
valuations would make the blocks powers of one common primitive word,
forcing equal slopes.

Combining (2), (4), (5) and (6) yields

```
log d_w >= (1-gamma_q)*A*log2-o(A)-log2.
```

This proves (T1)–(T2). Both the gcd and power-gap error estimates use
fixed ambient groups, so their thresholds are uniform in all word
parameters. The Subspace Theorem leaves the finite exceptional range
ineffective; no computable A_0 is obtained here.

## 5. Proportional slopes and a unified repeated-block class

### 5.1. An effective bound when both counts are at least three

In the proportional case use the reduced notation from
[C002/PROPORTIONAL.md](../equal-total-two-block-exclusion/PROPORTIONAL.md):
`a=a_0*r_0, r=b_0*r_0`, `b=a_0*s_0, s=b_0*s_0`, and
`U_0=2^a_0>V_0=3^b_0`. Put

```
L=r_0*k+s_0*ell, h=gcd(r_0*k,s_0*ell),
E=U_0^gcd(r_0,s_0)-V_0^gcd(r_0,s_0)>=1.
```

The elementary strong-divisibility proof supplies

```
d_w > E*U_0^(L-h)/|K|
    >= 2^(A/2)/|K|,
```

since `h<=L/2` and `A=a_0*L`. Using (2) proves (T4). No power-gap
estimate or Subspace Theorem is needed for this branch. For q=3,

```
rho_3=(2*log_3(2)-1)/6 > 1/24,
```

where the last inequality is the exact integer fact `2^8>3^5`.
Thus a simpler explicit bound is

```
d_w > 2^(A/24-1).                                   (7)
```

In particular `d_w<=d_0` implies `A<24*log_2(2*d_0)` in the
proportional q>=3 class. Once A is bounded, all positive word lengths,
valuation sums, letters and repetition counts have finite ranges.

### 5.2. The integer inequality that reaches two repetitions

The root supplied the following lemma; this lane independently checked
all of its cases. Let R,S be coprime positive integers and k,ell>=2.
Put `L=R*k+S*ell` and `H=gcd(R*k,S*ell)`. Then

```
5*(L-H+1) >= 7*(R+S).                                (8)
```

Write `R*k=H*p`, `S*ell=H*t`, where p,t are coprime positive integers.
If p+t>=4, then R+S<=L/2, and

```
5*(L-H+1)-7*(R+S)
    >= H*(3*(p+t)/2-5)+5 > 0.
```

If p=t=1, then R,S are coprime divisors of H, with R,S<=H/2.
When one is 1, say R=1, the bound H>=2S gives
`5*(H+1)>=10S+5>=7*(S+1)`.
When both are at least 2, H>=RS. Assume R<=S. If R=2 then S>=3,
and `5*(2S+1)-7*(2+S)=3S-9>=0`. If R>=3, the expression
`5RS+5-7R-7S` is positive already at R=S=3 and increases with
either variable. This proves (8) in that case.

The remaining case is p+t=3. By symmetry take p=1,t=2.
Then R divides H with R<=H/2, while S divides 2H with S<=H.
If R=H/2 and S=H, coprimality forces H=2,R=1,S=2; direct
substitution verifies (8). Otherwise either R<H/2, giving R<=H/3,
or S<H, giving S<=2H/3. Accordingly R+S<=4H/3 or R+S<=7H/6.
Both imply `7*(R+S)<10H<5*(2H+1)`, as required.

### 5.3. The uniform proportional square bound

Write the proportional block multipliers as `r_0=e*R`, `s_0=e*S`,
where R,S are coprime, and use L,H from (8). The total binary exponent
is now `A=a_0*e*L`. Retaining the factor

```
E=2^(a_0*e)-3^(b_0*e)>0
```

in C002's bound gives

```
log d_w > e*(L-H)*log U_0+log E-log |K|.               (9)
```

Set `c_0=2-log_3(2)`. The intercept estimate gives the more precise
bound, before replacing R+S by L/2,

```
log |K| < log2+c_0*e*(R+S)*log U_0.                  (10)
```

The global power-gap lemma also gives

```
log E=e*log U_0-o(A)                                 (11)
```

uniformly as total A grows. To justify this even when a_0*e stays
bounded: for every epsilon>0 the global gap bound extends to all
positive exponent pairs as

```
0 <= a_0*e*log2-log E <= epsilon*a_0*e*log2+C_epsilon.
```

Only finitely many smaller binary exponents need absorption into
C_epsilon, because positivity bounds their ternary exponents as well.
Since a_0*e<=A, this proves (11) with all quantifiers retained.

Let `T=L-H+1`, `B=R+S`. Equation (8) gives B<=5T/7. Also T>=L/2.
Because `c_0<7/5`, a consequence of `2^5>3^3`,

```
T-c_0*B >= (1-5*c_0/7)*T
          >= ((7-5*c_0)/14)*L
          = eta_* L.                                (12)
```

Combining (9)–(12) proves (T3). For a simpler positive comparison,
`2^8>3^5` gives `eta_*>1/112`.

Across both slope cases, all nondegenerate pairs with k,ell>=2 have
denominators tending uniformly to infinity with A. The common-word
exception cannot be removed: u and v may be powers of an actual cycle's
primitive word, retaining its denominator for arbitrary repetitions.

## 6. The determinant route is effective but does not supply the rate

For completeness, let

```
e_1=a*k, f_1=r*k, e_2=b*ell, f_2=s*ell,
T=|e_1*f_2-e_2*f_1|=k*ell*|Delta|,
H_0=gcd(|2^e_1-3^f_1|,|2^e_2-3^f_2|).
```

When Delta!=0, elementary elimination of the two power congruences,
valid modulo H_0 because 2 and 3 are units, proves

```
H_0 divides gcd(2^(T/gcd(f_1,f_2))-1,
               3^(T/gcd(e_1,e_2))-1).                 (13)
```

This includes prime powers, not only prime divisors. For example, raise
the first congruence to `f_2/gcd(f_1,f_2)` and the second to
`f_1/gcd(f_1,f_2)`; their quotient cancels the power of 3.
Canceling the powers of 2 gives the other divisibility.

Equation (13) is an exact computable bound for each instance, but the
displayed exponents need not be small relative to A. For instance
`u=(7), v=(9), k=11, ell=13` has A=194 while both exponents in (13)
are 286. The trivial upper bound `2^286-1` on that gcd exceeds the whole
raw denominator. This is not a counterexample to denominator growth;
it shows why this direct elimination plus the trivial size bound does
not prove the required uniform rate. Bounding that remaining common
divisor reintroduces a Diophantine gcd problem.

## 7. Independent audit of the contracting-block lattice argument

The root's separate elementary argument was independently checked.
Suppose D_u,D_v>0 and K!=0. Their distinct positive fixed points
`x_u=C_u/D_u`, `x_v=C_v/D_v` trap every block start of the mixed
cycle strictly between them. This follows directly by composing two
strict affine contractions with distinct fixed points.

Scale the cycle by its reduced denominator d. At successive starts
of a run of k copies of u, the resulting states y_i are integers.
Their nonzero differences satisfy

```
delta_i=y_(i+1)-y_i,
delta_(i+1)=(Q_u/P_u)*delta_i.
```

Since `gcd(P_u,Q_u)=1`, integrality of the k differences gives
`P_u^(k-1)|delta_0`. Meanwhile

```
|delta_0| < d*(D_u/P_u)*|x_v-x_u|
          = d*|K|/(P_u*D_v).
```

Therefore

```
d > P_u^k*D_v/|K|,
d > P_v^ell*D_u/|K|.                                 (14)
```

Choose the block with larger P, say P_u>=P_v, and suppose its count
k>=3. The intercept bound and D_u,D_v>=1 give

```
x_u<P_u^2/2^r, x_v<P_v^2/2^s,
|delta_0|<d*max(x_u,x_v)<d*P_u^2/2^min(r,s).
```

Together with `|delta_0|>=P_u^(k-1)>=P_u^2`, this proves
`d>2^min(r,s)>1`. The other repetition count need only be positive.
This is an all-size nonintegrality statement when both blocks contract.

If one block expands, its real fixed point is negative and the positive
mixed cycle is not trapped between the two fixed points. The preceding
interval bound is then unavailable. Theorem 1 covers uniform asymptotic
escape across that boundary, but does not remove every finite exceptional
case or establish d>1 at every size.

## 8. Controls, source scope and next obligation

* A genuinely expanding example is `u=(1)`, `v=(2)`, k=3, ell=5:
  `A=13, M=8`, `D_w=8192-6561=1631`, `C_w=10865`, and reduced
  denominator 1631. Its two block slopes differ, its first block expands,
  and both counts satisfy q=3. It is an exact illustration, not an
  asymptotic certificate.
* Taking both words as powers of (2) retains denominator 1; taking
  powers of (1,2,2), (1,3), or (4) retains denominators 5,7,13. All
  have K=0 and are excluded from the nondegenerate theorem.
* Two repeated motifs can contain arbitrarily many internal ascent and
  descent runs. Their number is not a bound on shortcut local minima;
  fixed-minimum-count cycle exclusions do not directly cover this class.

**Draft arithmetic correction.** The first draft misstated the numerical
intercept and reduced denominator of the worked example. Exact integer
recalculation gives `C_w=243*19+8*781=10865`,
`gcd(10865,1631)=1`, and denominator 1631. The corrected values are
used above. This was an example error in the current draft, not an error
in a historical result or in the general identities.

The imported primary results are exactly the two Corvaja–Zannier inputs
already inspected in C002. The group choice and word-size estimates are
this lane's derivation; the root supplied the integer lemma and
contracting-block argument, both independently checked above.
The affine composition and repetition algebra has established precedents, including
[Trümper's 2014 paper](https://onlinelibrary.wiley.com/doi/10.1155/2014/756917).
A bounded search also located an exact repeated-word 2-adic budget in
[author-hosted September 2026 notes](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/research/blind-2026-09-05/SymbolicNotes.md).
Those notes explicitly disclaim formal verification and are not a published
theorem imported here. They do not supply the contracting-pair denominator
bound. No priority conclusion follows from this limited search.

| Required field | Result |
| --- | --- |
| Objects | All positive rational cycles `u^k v^ell`, with both words allowed to vary; q is a lower bound on their repetition counts. |
| Structural gain | A fixed ambient S-unit group removes dependence on a fixed block catalogue. Unequal slopes and the refined proportional argument give uniform bounded-layer finiteness for all nondegenerate q=2 pairs. |
| Remaining gap | The unequal-slope threshold is ineffective; all-size d>1 for an expanding/contracting pair remains unproved. Arbitrary word patterns and the K=0 branch remain outside the conclusion. |
| Worked example | `(1)^3(2)^5` is a positive rational cycle with one expanding block and denominator 1631. |
| Known-cycle controls | Common primitive-word powers retain the actual denominator-1,5,7,13 cycles through K=0. |
| Cheapest meaningful next test | Independently audit the fixed ambient-group quantifiers and the B_z bound; then target the expanding/contracting finite-exception boundary without replacing uniformity by a larger finite catalogue. |
| Intermediate milestone | Uniform bounded-denominator finiteness for all nondegenerate two-block representations with k,ell>=2, even as the blocks vary. This is a strict structural subclass of cycle words. |
