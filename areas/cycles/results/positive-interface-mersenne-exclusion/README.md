---
id: positive-interface-mersenne-exclusion
kind: result
title: Positive-interface Mersenne joins have effective level exclusions
status: written
claim: >
  Raw odd-only valuation words. Fix J>r>=1 and positive odd integers h,z.
  Let nonempty exact signed segments A,B join -h to z to h, with
  Mersenne addends 2^J-1 then 2^r-1, or in the reverse order, and
  with the boundary valuations of the two-half-defect Mersenne normal
  form. Put m=len(A)+len(B), S=sum(A)+sum(B), D=2^S-3^m>0,
  eta=D/2^S, and G=log_2(1/eta). A denominator-one reconstruction
  necessarily has m<65G+25r+65 in high-to-low order and
  m<(13/5)(r+G)+1 in low-to-high order. In low-to-high order,
  every reduced denominator q satisfies the unconditional law
  q>eta*2^((m-log_2(1+2^(-r)))/(log_2(3)+1)-r). Under the declared
  Laurent-Mignotte-Nesterenko two-logarithm bound, every such
  reconstruction with 1<=r<=256, or with 8r<=5J in low-to-high
  order, or with 32r<=J in high-to-low order, has denominator
  greater than one,
  without an upper bound on J, the endpoints, lengths or valuations.
  Exact finite gaps give m<=8219 and a positive cycle minimum below
  2^23, where complete local descent excludes the candidate. No
  primitivity, near-criticality, external convergence or period
  bound is assumed. Negative interfaces and arbitrary four-mismatch
  rotations are outside this claim.
authors:
  - Codex formalisation research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms]
certificates: [check_positive_interface.py]
evidence:
  - "check_positive_interface.json: exact terminal budgets, canonical and boundary identities, genuine signed joins and reduced integer cycles, finite positive gaps, local descent and eleven actual-cycle controls"
tags: [cycles, half-defects, signed-orbits, denominators, linear-forms, effective-bounds]
---

# Positive-interface Mersenne joins have effective level exclusions

## Statement

Use the raw signed odd-only map
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers, with
zero numerators excluded and absolute values used when taking
the valuation of a negative numerator. Fix `J>r>=1`, put
`N=2^J`, `L=2^r`, and let `h,z` be positive odd integers.
Two nonempty exact segments join `-h -> z -> h` in one of
the following orders. As usual, `A[t]` changes only the last
letter of `A` by `t`.

| Order | Addends of A and B | Boundary conditions | Reconstructed halves |
|---|---|---|---|
| High to low | `N-1, L-1` | `last(A)>J-r`, `last(B)>r` | `u=A[-(J-r)]B[-r]`, `v=AB[J]` |
| Low to high | `L-1, N-1` | `last(B)>J` | `u=A[J-r]B[-J]`, `v=AB[r]` |

These are the positive-interface cases of the
[Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md).
Set

```
a=len(A), P=sum(A), b=len(B), T=sum(B),
m=a+b, S=P+T, D=2^S-3^m>0,
eta=D/2^S, G=log_2(1/eta), alpha=log_2(3).
```

The word `uv` has length `2m` and total valuation `2S`.
The main conclusion, under the sole external input
[LMN](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md), is

```
den(uv)>1 whenever at least one condition holds:
  1<=r<=256;
  low-to-high order and 8r<=5J;
  high-to-low order and 32r<=J.                       (1)
```

The higher level `J`, both endpoints and both segment lengths
are unrestricted. The argument first proves the following
necessary conditions for a hypothetical denominator-one word,
at every low level `r`:

```
high to low:  m<65G+25r+65,
low to high:  m<(13/5)(r+G)+1.                       (2)
```

There is also an unconditional denominator law in low-to-high
order. Put `q=den(uv)` and `c_r=log_2(1+2^(-r))`. Then

```
q > eta*2^((m-c_r)/(alpha+1)-r).                     (2a)
```

This law requires neither LMN nor a lower bound on normalized
states. It can be weak when the lower level grows with length.

The states in the proof are normalized `3x+1` cycle states.
For the same word under `3x+d`, actual states are `d` times
these normalized states. No primitivity is required. The
auxiliary signed joins can exist: the certificate retains
genuine examples and their positive-denominator cycles.
The two level-ratio conditions cover unbounded low levels.
The theorem does not exclude positive-interface pairs outside
these regions, negative interfaces, or arbitrary four-mismatch
rotations.

In high-to-low order with `r=1`, every admissible interface is
positive: a negative state under `T_1` stays negative and
cannot reach `h>0`. Thus (1) includes all high-to-low `r=1`
normal forms, complementing the earlier
[low-to-high result](../unit-low-level-mersenne-exclusion/README.md).

## Proof

### 1. Terminal intercepts and the cycle state

For any positive word `W` of length `k`, total `V`, and last
letter `w`, its ordinary additive-one intercept satisfies

```
C_W/2^V <= 2^(1-w)*((3/2)^k-1).                    (3)
```

Indeed, if `E_i` is its prefix total before letter `i`, then
`E_i<=V-w-k+1+i` for `0<=i<k`. Summing the intercept gives
(3), using `sum_(i=0)^(k-1)3^(k-1-i)2^i=3^k-2^k`.
In particular `C_W/2^V< (3/2)^k`.

Suppose for contradiction that `den(uv)=1`. Let `x` be the
positive odd integer at the canonical cut, and let `Y` be the
positive odd state after the modified first segment of `u`.
Put

```
sigma=3^a/2^P, c=3^b/2^T, lambda=sigma*c=1-eta,
R_a=(3/2)^a.
```

Both `Y` and the signed interface `z` are positive. Their
difference after the appropriate additive scaling may have
either sign; no ordering between them will be assumed.

The final letter of `v` is at least `J+r+1>=4`, so this
cannot be a repetition of the trivial `(2)` cycle. Exact
local descent verifies that all odd seeds from 3 through 33
reach 1. Hence every state of the hypothetical cycle is at
least 35. The product identity and `106^5<2^8*35^5` imply

```
2^(2S) <= (106/35)^(2m) < 2^(16m/5),
S<8m/5.                                             (4)
```

This minimum-state argument applies only to `3x+1`.

### 2. High-to-low order

Write the ordinary affine maps as `F_A(t)=sigma*t+C_A/2^P`
and `F_B(t)=c*t+C_B/2^T`. The signed endpoint equations are

```
sigma*h+z=(N-1)C_A/2^P,
h=c*z+(L-1)C_B/2^T,       0<c*z<h.
```

The first terminal bound `last(A)>=J-r+1` and (3) give

```
sigma*h+z < L*(R_a-1),
h<2^(P-a+r).                                        (5)
```

The normal-form closure is `F_u(x)=Nx+h`. The exact affine
identity underlying the
[state enclosure](../mersenne-join-state-enclosure/README.md)
gives, for `K=(N-1)x+h`,

```
K=[(NL-1)h-(N-L)c*z]/[N(L-1)eta]
 < L*h/[(L-1)eta] <= 2h/eta.                        (6)
```

At the actual cut after `A[-(J-r)]`,

```
3^a*((N-1)x+h)
 =2^(P-J+r)*((N-1)Y-2^(J-r)z).
```

The bracket is odd, since `Y,z` are odd and `J>r`. Therefore
`v_2(K)=P-J+r`. Equations (5) and (6) imply

```
2^(P-J+r)<=K<2^(P-a+r+1)/eta,
a<J+G+1.                                            (7)
```

The second cut supplies the additional divisibility needed
to bound `b`. Comparing the two exact compositions
`B[-r](Y)=Nx+h` and `T_(L-1)^B(z)=h` gives

```
3^b*((L-1)Y-z)=2^(T-r)*(N(L-1)x-h).                (8)
```

The bracket on the right is odd and nonzero. Consequently

```
v_2((L-1)Y-z)=T-r,
2^(T-r)<=|(L-1)Y-z|.                                (9)
```

To bound this difference, the enclosure gives
`x<(L+1)h/[N(L-1)eta]`, and `Y=(N/L)F_A(x)`. Using (3)
and (5),

```
(L-1)Y
 < (L+1)*sigma*h/(L*eta)+(L-1)*(R_a-1)
 < (L+1)*(R_a-1)/eta+(L-1)*(R_a-1)
 < 2L*R_a/eta.
```

Also `0<z<L*R_a<2L*R_a/eta`. Because both quantities in
(9) are positive, their absolute difference is strictly
less than their maximum, not their sum. Thus

```
T<(alpha-1)a+G+2r+1,
b<=T-r<(3/5)a+G+r+1.                               (10)
```

Here `alpha<8/5`, as follows from `3^5<2^8`. The boundary
conditions give `P>=a+J-r`, `T>=b+r`, hence `S>=m+J`.
Together with (4) and (7),

```
J<(3/5)(a+b),
(2/5)a<(3/5)b+G+1.
```

Substitute (10). The coefficient
`2/5-(3/5)^2=1/25` is positive, and gives

```
a<40G+15r+40,
b<25G+10r+25,
m<65G+25r+65.                                      (11)
```

### 3. Low-to-high order

For this section allow any reduced denominator `q=den(uv)`.
Keep `x,Y` as normalized states; `q*x,q*Y` are positive odd
integers and `q` is odd. Put `G_q=log_2(q/eta)`, so `G_q=G`
in the contradiction case. Now the signed endpoint equations are

```
sigma*h+z=(L-1)C_A/2^P,
h=c*z+(N-1)C_B/2^T,
```

so the unrestricted version of (3) gives
`h<(L-1)2^(P-a)<2^(P-a+r)`. The modified first segment
is `A[J-r]` and its endpoint is `Y=(L/N)F_A(x)`. Thus

```
3^a*((L-1)x+h)=2^P*((L-1)2^(J-r)Y-z).
```

After multiplication by the odd integer `q`, the bracket is
odd. Thus `v_2(q*((L-1)x+h))=P`. The exact enclosure
`x<h*(1+L*lambda)/[L(L-1)eta]` gives

```
2^P <= q*((L-1)x+h) < q*(1+1/L)*h/eta
     < q*(L-1/L)*2^(P-a)/eta < q*2^(P-a+r)/eta,
a<r+G_q.                                            (12)
```

Comparing `B[-J](Y)=Lx+h` with the signed `B` composition,

```
3^b*((N-1)Y-z)=2^(T-J)*(L(N-1)x-h).
```

After multiplying by `q`, the right bracket is odd and
nonzero, so `q*((N-1)Y-z)` has valuation exactly `T-J`. Put `b_A=C_A/2^P`. The sharper
enclosure `x<h*(1+L*lambda)/[L(L-1)eta]`, together with
`sigma*h=(L-1)b_A-z`, gives

```
L*F_A(x)
 < [(L+1)b_A-z*(1+L*lambda)/(L-1)]/eta
 < (L+1)*R_a/eta.
```

Both `(N-1)Y<L*F_A(x)` and `z<(L-1)R_a` are positive and
less than this last bound. Multiplying their difference by
`q` and using `c_r=log_2(1+2^(-r))<1` and `T>=J+b`, we get

```
b<=T-J<(alpha-1)*a+r+G_q+c_r,
m<(alpha+1)*(r+G_q)+c_r.              (13)
```

Rearrangement proves (2a). When `q=1`, (13) gives
`m<(13/5)(r+G)+1`, stronger than (11) for every `r>=1`,
`G>0`. It uses the positive interface explicitly; the difference
estimate cannot be applied unchanged across opposite signs.

The two unbounded level regions in (1) now have length bounds
independent of `r`. In either order, the boundary conditions
imply `S>=m+J`, so (4) gives `J<3m/5`. Thus

```
low to high, 8r<=5J:
  r<3m/8,  m<(39/40)m+(13/5)G+1,
  m<104G+40;

high to low, 32r<=J:
  25r<(15/32)m,  m<(15/32)m+65G+65,
  m<(2080/17)*(G+1).                               (14)
```

### 4. LMN and exact finite gaps

It remains to exclude (11) for `r<=256` and the two
length bounds (14). Let
`Lambda=S*ln(2)-m*ln(3)>0`. From (4), the declared
[LMN specialization](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md)
has `b'=S/2+m<2m` and gives

```
ln(Lambda)>-48.68*max(ln(b')+0.14,21)^2.
```

Using `eta=1-exp(-Lambda)>min(Lambda/2,1/2)` and
`1/2<ln(2)<1` yields

```
G<H(m),    H(m)=1+98*max(log_2(m)+2,21)^2.           (15)
```

This is the same positive-gap estimate used in the
[unit-low-level proof](../unit-low-level-mersenne-exclusion/README.md).
Here the finite steps are replayed for the stated regions.
At `m=2^23`, `H=61251`, and each of

```
65H+25*256+65,     104H+40,     (2080/17)*(H+1)
```

is strictly below `2^23`, as checked by integer arithmetic.
For all larger `m`, each difference from `m` increases.
Indeed `H'(m)<392*(log_2(m)+2)/m`; multiplying by any of
`65,104,2080/17` still gives less than 1 at the cutoff,
and the logarithmic ratio decreases thereafter. Therefore
all three regions force `m<2^23`.

The certificate encloses `ln(2)` and `ln(3)` by 80 terms of
the positive atanh series, with its geometric tail bound.
After outward rounding, it verifies

```
125573666586150569315490533898 / 2^96 < alpha
 < 125573666586150569315490533899 / 2^96.
```

For every integer `1<=k<2^23`, both endpoints after
multiplication by `k` have the same floor, and their distance
below the next integer exceeds `2^-25`. All comparisons are
exact integer comparisons. Thus `S>m*alpha` gives
`Lambda>2^-26`, `eta>2^-27`, and `G<27`. Equations (11) and (14) now
force, with strict rounding,

```
r<=256:          m<8220,        m<=8219;
low-to-high cone: m<2848,        m<=2847;
high-to-low cone: m<58240/17,    m<=3425.             (16)
```

For every integer `1<=k<=8219`, put
`V_k=bit_length(3^k)`. The certificate checks

```
3*2^23*(2^V_k-3^k)>k*2^V_k.                        (17)
```

The smallest possible positive gap at half-length `k` is
`eta_k=(2^V_k-3^k)/2^V_k`. If `X` is the minimum state of
the full `2m`-step cycle, the product identity gives

```
eta < ln(2^S/3^m)
    = (1/2)*sum_(i=0)^(2m-1) ln(1+1/(3x_i))
    < m/(3X).
```

Since `eta>=eta_m`, (17) forces `X<2^23`. The certificate
verifies complete local descent: every odd seed
`3<=s<2^23` reaches a smaller positive odd integer. Induction
on the seeds proves that every such seed reaches 1. This
contradicts the nontrivial cycle through `X`, proving (1).

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/positive-interface-mersenne-exclusion/check_positive_interface.py
python3 -O areas/cycles/results/positive-interface-mersenne-exclusion/check_positive_interface.py
```

The [certificate](check_positive_interface.py) compares its
deterministic output with the [generated receipt](check_positive_interface.json).
Use `--write-receipt` to regenerate it. It checks the algebraic
identities and terminal-intercept estimate, replays specified
genuine signed joins in both orders and their reduced positive
integer cycles, checks both exact boundary valuations with the
denominator scaling retained, and verifies all finite steps
(15)--(17) and the complete local descent. Every guard aborts
on an unfinished computation; bounded absence of signed joins
is neither computed nor used.

The eleven standard `3x+d` controls for `d=5,7,13,61` are
replayed. Their reduced denominators are greater than one,
so the contradiction assumption fails. The finite local
minimum and descent arguments are specifically for `3x+1`.
All checks use exact standard-library arithmetic and remain
active under `python3 -O`. LMN is cited, not reproved here.

## Remarks

The key extra restriction is the exact power of two in the
second-block start difference (8). Bounds on positive affine
intercepts alone do not impose that restriction. In the
`J=3,r=1,h=1` join `A=(2,1,1,3), B=(4)`, the reconstructed
cycle has denominator 361. Its actual modified first endpoint
is 1205 and its scaled auxiliary interface is 1805, giving
difference `-600` of valuation 3. The argument retains this
negative difference through its absolute value.

The endpoint-state enclosure and the earlier low-to-high
unit-level proof supply the setting and finite-gap strategy;
the second-block comparison treats positive interfaces in
both orders. Novelty of this scoped combination is undetermined.
No independent-session review or Lean formalisation is claimed.
The general [four-mismatch question](../../questions/rotation-distance-at-least-5.md)
remains open.

## History

- 2026-11-08: retained the exact second-block start difference
  to bound positive-interface Mersenne joins in both orders.
  Combined its low-level-dependent length bound with LMN,
  exact positive gaps and local descent to exclude `1<=r<=256`
  and the unbounded level regions `8r<=5J` in low-to-high order
  and `32r<=J` in high-to-low order.
