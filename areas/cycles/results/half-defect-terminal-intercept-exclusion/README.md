---
id: half-defect-terminal-intercept-exclusion
kind: result
title: A substantial terminal intercept excludes high-to-low half defects
status: written
claim: >
  Raw odd-only clock. Let J>r>=1, h positive odd, and z nonzero odd.
  Let nonempty positive words A,B give exact signed paths -h to z
  under 3x+(2^J-1) and z to h under 3x+(2^r-1), with last(A)>J-r
  and last(B)>r. Put u=A[-(J-r)]B[-r], v=AB[J], and suppose
  2^(sum(A)+sum(B))>3^(len(A)+len(B)). Define the positive terminal
  intercept fraction chi=1-3^len(B)*z/(2^sum(B)*h). If chi>=1/2,
  then den(uv)>1 under EXT-1 alone, for arbitrary levels, endpoints,
  lengths and valuations. No primitivity, convergence input, period
  bound or near-critical hypothesis is used. More generally,
  denominator one would force m<65*log2(1/(eta*chi))+90, where m is
  the half length and eta its positive power gap. The full odd word
  has length 2m. The conclusion concerns normalized 3x+1 states and
  preserves actual cycles of 3x+d for other positive odd addends.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure, half-defect-positive-order-exclusion, small-mersenne-endpoint-exclusion, baseline-obligation-transfer-controls]
assumes: [musson-collatz-gap-all]
certificates: [check_terminal_intercept.py]
evidence:
  - "check_terminal_intercept.json: complete exact power gaps, minimum comparisons and local descent; signed joins, all retained endpoint identities, loop insertion and eleven actual-cycle fixtures"
tags: [cycles, half-defects, signed-orbits, denominators, terminal-intercepts]
---

# A substantial terminal intercept excludes high-to-low half defects

## Statement

For a nonempty valuation word W, write W[t] for increasing only
its last letter by t. Use exact signed odd-only maps: every state
and every output is a nonzero odd integer, and each positive letter
is the full valuation of the nonzero numerator. Take

```
J>r>=1,  M=2^J,  N=2^r,  p=J-r,
A: -h -> z under 3y+(M-1),
B:  z -> h under 3y+(N-1),
h>0 odd, z nonzero odd, last(A)>p, last(B)>r.
```

The interface z may have either sign. Put

```
a=len(A), b=len(B), m=a+b, P=sum(A), T=sum(B),
D=2^(P+T)-3^m>0, lambda=3^m/2^(P+T), eta=1-lambda,
u=A[-p]B[-r], v=AB[J], c=3^b/2^T,
chi=(h-c*z)/h=(N-1)C_B/(2^T*h)>0.
```

Here C_B is the ordinary additive-one intercept. The complete
positive word uv has odd-only length 2m, total valuation 2(P+T), and
D_(uv)=(2^(P+T)+3^m)D. Under
[EXT-1](../../../../sources/musson-collatz-gap-all.md),

```
chi>=1/2  implies  den(uv)>1.                         (1)
```

This covers arbitrary levels and words, including all negative
interfaces in this high-to-low order, since z<0 gives chi>1.
Positive interfaces with chi<1/2 remain outside (1). The
low-to-high order is not part of this statement.

No primitivity assumption or external convergence computation is
used. The finite arithmetic and local descent are replayed here.
In particular, no LMN or imported period bound is used. Existing
negative-interface and bounded-level results keep their original
claims and source assumptions.

## Proof

### 1. Retain the sign of the divided endpoint identity

Suppose den(uv)=1. The [normal form](../two-half-defect-mersenne-normal-form/README.md)
gives a positive odd integer 3x+1 cycle, with canonical state x
and opposite half state M*x+h. Equivalently, the usual rotation
identity shows that C_(rotation_i(uv))/D_(uv) are positive odd
integers satisfying all exact arrows. Let Y be the state after
A[-p] and Z the state after A in the opposite half. The signed
first endpoint identity gives

```
Z=N*Y-z.
```

The word is A0 B0 A0[p] B0[J+r], with A0=A[-p] and B0=B[-r].
Both are positive and nonempty, and p<J+r. The unconditional
[paired-state order theorem](../half-defect-positive-order-exclusion/README.md)
therefore forces Y<Z. The second block's exact boundary equation is

```
3^b*((N-1)Y-z)=2^(T-r)*(M(N-1)x-h).
```

Consequently M(N-1)x-h>0. This is essential: it is not a sign
assumption on arbitrary rational cycles.

Write the ordinary additive-one affine maps of A and B as

```
F_A(t)=3^a*t/2^P+(3^a*h/2^P+z)/(M-1),
F_B(t)=c*t+(h-c*z)/(N-1).
```

Reconstruction gives F_u(t)=M*c*F_A(t)+N*(h-c*z)/(N-1)
and F_u(x)=M*x+h. Using (M-1)C_A=h*3^a+z*2^P and dividing
the complete integer identity by M-1 yields

```
M(N-1)D*x=hD+3^b*F0,
F0=(N+1)h*3^a-(M-N)C_A.                             (2)
```

There is no modular cancellation of M-1 here. Since gcd(D,3)=1,
D divides F0. The established sign and C_A>0 give

```
0<F0<(N+1)h*3^a<2N*h*3^a.
```

With alpha=log2(3) and G=log2(1/eta), D>eta*3^m implies

```
alpha*b < r+log2(h)+G+1.                             (3)
```

The subtraction in F0 is useful even at a positive interface.
It is the part of the earlier negative-interface argument that
continues to hold once the actual state ordering is retained.

### 2. Keep the terminal intercept fraction instead of discarding it

The first exact boundary identity is

```
3^a*((M-1)x+h)=2^(P-p)*((M-1)Y-2^p*z).
```

Its right parenthesis is odd, so the exact binary order of
(M-1)x+h is P-p>=a. The [state enclosure](../mersenne-join-state-enclosure/README.md)
gives, in either interface sign,

```
(M-1)x+h
 < [(N+1)(M-1)/(M(N-1))]*h/eta <4h/eta.
```

Thus

```
a<log2(h)+G+2.                                      (4)
```

Let w=last(B)>=r+1. Every earlier valuation is at least one.
Bounding each intercept summand by its suffix valuations gives

```
C_B/2^T <= 2^(1-w)*((3/2)^b-1),
chi*h=(N-1)C_B/2^T < (3/2)^b.
```

Set K=log2(1/chi), which may be negative when z<0. Then

```
log2(h)<(alpha-1)b+K.                               (5)
```

The cycle is nontrivial because its last valuation in v is at
least J+r+1>=4. The complete local descent below 2^20 in the
certificate implies its minimum X is at least 2^20, and in
particular at least 35. Since 106^5<2^8*35^5, its full 2m-step
product gives P+T<8m/5. Boundary positivity also gives
P>=a+J-r, T>=b+r, so J<3m/5.

Put E=G+K. From (3)--(5), alpha<8/5 and r<J,

```
b<r+E+1,       a<(3/5)b+E+2,
(2/5)b<(3/5)a+E+1.
```

Substitution, with no assumption on the sign of E, yields

```
b<40E+55, a<25E+35, m<65E+90.                      (6)
```

This is the stated necessary inequality
m<65*log2(1/(eta*chi))+90. If chi>=1/2, then K<=1 and

```
m<65G+155.                                         (7)
```

### 3. Close the half-length and minimum ranges exactly

EXT-1 applied to 3^m<2^(P+T) gives
G<=172+341*log2(m). If 2^j<=m<2^(j+1) with j>=19, (7)
would require

```
2^j < 65*(172+341*(j+1))+155.
```

At j=19 the left side exceeds the right by 69653, and the
margin increases by 2^j-22165>0 at every next j. Hence m<2^19.

For every integer 1<=n<2^19, the certificate sets

```
P_n=3^n, T_n=bit_length(P_n), beta_n=2^T_n,
gap_n=beta_n-P_n
```

and checks the exact inequality 2^24*gap_n>beta_n. Every allowed
half total is at least T_m, so eta>=gap_m/beta_m>2^-24.
Thus G<24 and (7) gives m<=1714.

For all 1<=n<=1714, a second complete check establishes

```
3*2^20*gap_n > n*beta_n.                             (8)
```

The largest ceiling of n*beta_n/(3*gap_n) is 583561, attained at
n=1636. This is below 2^20.

The gap is a HALF-clock gap: the full 2m-step cycle product gives

```
eta < -ln(1-eta)
    = (1/2)*sum_(i=0)^(2m-1) ln(1+1/(3*x_i))
    < m/(3X).
```

Equation (8) therefore forces X<2^20, contrary to the complete
local descent. This proves (1). These finite bounds are rechecked
by integer arithmetic here; they do not import the logarithmic
assumptions of an earlier theorem using similar bounds.

### 4. A quantitative restriction on the remaining positive interfaces

The [small-endpoint obstruction](../small-mersenne-endpoint-exclusion/README.md)
says that denominator one requires h>(M-1)/7. Since h is a positive
integer and M is a power of two at least four, this implies h>M/8.
Combining log2(h)>J-3 with (5), b<r+G+K+1 and alpha<8/5 gives

```
8*log2(1/chi)>5J-3r-3G-18.                           (9)
```

When the right side is positive, a surviving denominator-one
candidate must have an exponentially small terminal intercept
fraction. This is a necessary restriction, not an exclusion of
all positive interfaces.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/half-defect-terminal-intercept-exclusion/check_terminal_intercept.py
python3 -O areas/cycles/results/half-defect-terminal-intercept-exclusion/check_terminal_intercept.py
```

The [certificate](check_terminal_intercept.py) and generated
[receipt](check_terminal_intercept.json) check all 524287 positive
half gaps, all 1714 minimum comparisons, and every odd seed from
3 through 2^20-1 descending below itself. It also checks the exact
endpoint identities on genuine signed joins, reconstructs their
actual positive 3x+d cycles with d retained, and replays the eleven
standard fixtures. Finite join examples test the implementation;
they are not an absence census or the proof of the unbounded claim.

In particular, J=6,r=5,h=1,A=(2),B=(2,3,6) has z=15 and
chi=1643/2048>1/2. It reconstructs

```
u=(1,2,3,1), v=(2,2,3,12), d=8111,
5 -> 4063 -> 5075 -> 2917 -> 8431 -> 8351 -> 8291 -> 4123 -> 5.
```

This actual cycle is preserved. For general d the integer relation
is D|d*F0; the normalized state is 5/8111, not an integer state of
3x+1. The certificate retains this d factor. Other controls exercise
chi<1/2 and the opposite state-order sign.

## Remarks

The earlier [negative-interface theorem](../negative-interface-mersenne-exclusion/README.md)
covers both Mersenne orders under LMN. Here the high-to-low portion
with z<0 is included under EXT-1, and the new positive-interface
cone has arbitrary J and r. The [positive-interface result](../positive-interface-mersenne-exclusion/README.md)
uses level or level-ratio restrictions instead. Neither earlier
claim is rewritten. This result does not settle the general unequal
half-defect problem. Novelty undetermined.

A positive auxiliary cycle inserted into B has affine slope rho<1.
Keeping its endpoints and the required boundary valuations fixed
multiplies c by rho^k after k repeats,
so chi_k=1-rho^k*(1-chi). Therefore all sufficiently many such
repeats lie in chi_k>=1/2 and are excluded at denominator one by
(1). This follows from the same cone; it does not assert monotonicity
of the canonical rational state or exclude every smaller repeat count.

## History

- 2026-11-08: retained the divided endpoint identity in the high-to-low
  positive-interface branch using the paired-state order theorem,
  isolated the terminal intercept fraction, and closed chi>=1/2
  under EXT-1 by self-contained exact arithmetic. The finite power-gap
  bootstrap follows the method of the equal-amplitude result and is
  rerun here with the present half-length and minimum ranges.
