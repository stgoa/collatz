---
id: expanding-negative-prefix-mersenne-exclusion
kind: result
title: Expanding negative Mersenne prefixes with smaller endpoints exclude denominator one
status: written
claim: >
  Raw odd-only valuation words. For every J>1 and positive odd
  g<=h, let A be a nonempty exact 3x+1 segment from -h to -g,
  with 3^len(A)>2^sum(A), and let B be a nonempty exact
  3x+(2^J-1) segment from -g to h, with last(B)>J.
  Reconstruct u=A[J-1]B[-J], v=AB[1], and put
  m=len(A)+len(B), S=sum(A)+sum(B). If 2^S>3^m, then
  den(uv)>1 under only the declared Laurent-Mignotte-Nesterenko
  two-logarithm bound. There is
  no upper bound on h, J, lengths, valuations or intermediate
  states. Every closed negative first segment satisfies the
  hypotheses, without a classification of negative cycles.
  The logarithm bound first forces any denominator-one candidate
  to have m<2^20. Exact finite two-sided gap checks then force
  a=len(A)<=15, m<=85 and h<9510. Its canonical integer state
  would be below 1825920<2^21, where a local descent closes
  the contradiction. EXT-1 and external convergence or period
  bounds are not used.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms]
certificates: [check_all_endpoints.py]
evidence:
  - "check_all_endpoints.json: exact intercept bounds, logarithm parameters and cutoff, two-sided finite gap bootstrap, local descent, negative-prefix controls and eleven actual positive cycles"
tags: [cycles, half-defects, signed-orbits, denominators, linear-forms, effective-bounds]
---

# Expanding negative Mersenne prefixes with smaller endpoints exclude denominator one

## Statement

Use the raw odd-only signed map
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers,
excluding zero numerators. Let `J>1`, `N=2^J`, and let
`g,h` be positive odd integers with `g<=h`. Suppose two nonempty exact
segments with positive valuation words `A,B` satisfy

```
A: -h -> -g under T_1,          3^len(A)>2^sum(A),
B: -g ->  h under T_(N-1),      last(B)>J.
```

The notation `A[t]` changes only the last letter by `t`.
Define the positive reconstructed words and their parameters by

```
u=A[J-1]B[-J],       v=AB[1],
a=len(A), P=sum(A), b=len(B), T=sum(B),
m=a+b,              S=P+T,
D=2^S-3^m>0,        eta=D/2^S,
q=den(uv).
```

The full word has length `2m` and total valuation `2S`.
Under the sole external input
[the explicit two-logarithm bound](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md),

```
q>1.
```

There is no restriction on the endpoint, either segment's
length, any valuation, or any intermediate signed state.
Primitivity is not required. In particular, every closed
negative first segment has `g=h` and expanding slope, so
all closed prefixes are covered without classifying negative
cycles. The theorem does not assert nonexistence of the
auxiliary signed segments. Cases with `g>h`, a nonexpanding
first slope, or other Mersenne normal-form parameters remain
outside its scope.

The [bounded-endpoint precursor](../closed-negative-prefix-mersenne-denominator-law/README.md)
uses EXT-1. We rederive its elementary prefix inequalities
below and bound both logarithmic gap signs using LMN instead.
EXT-1 is not an assumption of this proof or its dependency
chain. The precursor retains its distinct sole-EXT-1 route
for `h<=91`.

## Proof

### 1. Retain the exact endpoint and residual denominator

Suppose, for a contradiction, that `q=1`, and write `x` for
the canonical positive integer cycle state. The final letter
of `v` is `last(B)+1>=J+2>=4`, so the full word is not a
repetition of `(2)`. Its positive integer
cycle is nontrivial and all states are at least 3.

Put `alpha=log_2(3)`, `sigma=3^a/2^P`, `c=3^b/2^T`
and `lambda=sigma*c=1-eta`. The auxiliary endpoint equations
give the ordinary additive-one affine maps

```
F_A(t)=sigma*(t+h)-g,
F_B(t)=c*t+(h+c*g)/(N-1).
```

The intercept of `A` is positive, with
`C_A=h*3^a-g*2^P>0`; the assumed expansion gives
`a<=P<alpha*a`. In the closed case `g=h`, positivity
of this intercept itself supplies expansion. The
[normal-form reconstruction](../two-half-defect-mersenne-normal-form/README.md)
gives `F_u(t)=2c*F_A(t)+N*(h+c*g)/(N-1)` and
`F_u(x)=2x+h`. Expanding and collecting terms yields

```
2(N-1)D*x=h*D+3^b*F,
F=(2N-1)h*3^a-(N-2)g*2^P
 =(N+1)h*3^a+(N-2)C_A,      0<F<2N*h*3^a.           (1)
```

Since `x` is an integer and `gcd(D,3)=1`, equation (1)
gives `D|F`. Write `L=log_2(h/eta)`. Then

```
eta*3^m<D<=F<2N*h*3^a,
alpha*b<J+L+1.                                      (2)
```

The [state enclosure](../mersenne-join-state-enclosure/README.md),
with first Mersenne power 2, gives `x<3h/(2eta)`.
If `Y` is the odd integer state after `A[J-1]`, its
boundary equation is

```
3^a*(x+h)=2^P*(2^(J-1)*Y+g).
```

The right-hand parenthesis is odd. Thus, at precisely the
canonical cut being used,

```
v_2(x+h)=P,
2^P<=x+h<(5/2)*h/eta<4h/eta,
a<=P<L+2.                                           (3)
```

The positive cycle product gives
`2^(2S)<= (10/3)^(2m)<2^(7m/2)`, since all states are
at least 3 and `10^4<2^7*3^4`. Therefore `S<7m/4`.
Also `P>=a` and `T>=J+b`, so `S>=m+J` and `J<3m/4`.
Combine this with (2) and (3):

```
alpha*m-J<(1+alpha)(L+2),
L+2>((alpha-3/4)/(1+alpha))*m>3m/10,
h>eta*2^(3m/10-2).                                  (4)
```

The last comparison uses `alpha>3/2`, equivalent to
`3^2>2^3`. All statements so far are unconditional.

### 2. Remove the endpoint from the prefix bound

For any positive word `A` of length `a` and total `P`, let
`E_i` be its first `i` letters' sum. The remaining letters
give `E_i<=P-a+i`. Consequently

```
C_A=sum_(i=0)^(a-1) 3^(a-1-i)*2^E_i
   <=2^(P-a)*sum_(i=0)^(a-1) 3^(a-1-i)*2^i
   =2^(P-a)*(3^a-2^a)
   <2^(P-a)*3^a.                                    (5)
```

Define

```
epsilon=1-2^P/3^a>0,
G=log_2(1/eta),       E=log_2(1/epsilon).
```

Both gaps lie in `(0,1)`. Since `g<=h`, we have
`C_A=h*3^a-g*2^P>=h*(3^a-2^P)`. Thus (5) gives
`h<2^(P-a)/epsilon`. Combine this with (3)
to cancel both `h` and `P`:

```
2^P<4h/eta<2^(P-a+2)/(eta*epsilon),
a<G+E+2.                                             (6)
```

Also `log_2(h)<(alpha-1)*a+E`, using `P<alpha*a`.
By (4), `log_2(h)>3m/10-G-2`. Since `alpha<8/5`,
equation (6) yields

```
3m/10<G+2+(alpha-1)*a+E<(8/5)*(G+E+2),
m<(16/3)*(G+E+2).                                   (7)
```

This removes the need for an upper bound on `h`.

### 3. Bound both gap signs by the same external theorem

Using natural logarithms, define two strictly positive forms:

```
Lambda_plus=S*ln(2)-m*ln(3),
Lambda_minus=a*ln(3)-P*ln(2).
```

Their gaps are `eta=1-exp(-Lambda_plus)` and
`epsilon=1-exp(-Lambda_minus)`.
Specialize the [LMN statement](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md)
to bases 2 and 3, field degree 1, and logarithmic height
parameters `log B_1=1`, `log B_2=2`. These are valid since
the rational bases have heights `ln(2)<1`, `ln(3)<2`.
The parameter `b'` is `S/2+m` for the first form and
`P/2+a` for the second. We have

```
S/2+m<15m/8<2m,
P/2+a<2a<2m.                                        (8)
```

Thus each form satisfies

```
ln(Lambda)>-48.68*max(ln(2m)+0.14,21)^2.              (9)
```

For every `Lambda>0`,
`1-exp(-Lambda)>min(Lambda/2,1/2)`. On `[0,1]`
this follows by concavity and `1-exp(-1)>1/2`; above
1 it follows by monotonicity. Use this in (9), together
with `1/2<ln(2)<1`, to obtain

```
G<H(m),       E<H(m),
H(m)=1+98*max(log_2(m)+2,21)^2.                      (10)
```

Indeed `ln(2m)+0.14<log_2(m)+2`, and
`48.68/ln(2)<97.36<98`. The elementary logarithm
comparisons and coefficient arithmetic are checked by
exact rational enclosures in the certificate.

### 4. Obtain a uniform finite cutoff

Equations (7) and (10) imply

```
3m<32*(H(m)+1).                                      (11)
```

At `m=2^20`, `H(m)=1+98*22^2=47433`, and

```
3*2^20-32*(47433+1)=1627840>0.                       (12)
```

For `m>=2^20`, the active branch of `H` is
`1+98*(log_2(m)+2)^2`. The derivative of
`3m-32*(H(m)+1)` exceeds

```
3-12544*(log_2(m)+2)/m.
```

The ratio `(log_2(m)+2)/m` decreases in this range,
because `1/ln(2)<2<log_2(m)+2`. At the cutoff,
`12544*22<3*2^20`. Therefore (12) persists, contradicting
(11) for every `m>=2^20`. We conclude

```
m<2^20,       len(uv)=2m<2^21.                       (13)
```

### 5. Exact finite gaps reduce the state to a local descent

The certificate encloses `alpha=ln(3)/ln(2)` using the
positive rational series

```
ln(z)=2*sum_(j>=0) t^(2j+1)/(2j+1),
t=(z-1)/(z+1),       z=2,3.
```

After 80 terms, the tail is less than
`2*t^161/[161*(1-t^2)]`. Rounding the resulting ratio
outward to denominator `2^96` gives rational endpoints
`alpha_lo<alpha<alpha_hi`. For every integer
`1<=r<2^20`, exact integer division verifies that
`r*alpha_lo` and `r*alpha_hi` have the same floor `k`, and

```
r*alpha_lo-k>2^(-25),
1-(r*alpha_hi-k)>2^(-25).                            (14)
```

Thus both distances of `r*alpha` to its neighboring
integers exceed `2^(-25)` throughout this finite range.
Since `a<m<2^20`, we can apply (14) to `a` and `m`.
The integer inequalities `P<a*alpha` and `S>m*alpha`
imply `Lambda_minus,Lambda_plus>2^(-26)`, using
`ln(2)>1/2`. The elementary gap comparison used in
section 3 gives

```
eta,epsilon>2^(-27),       G,E<27.
```

Equations (6) and (7), retaining integer endpoints, yield
`a<=55` and `m<=298`. Two cheap exact power checks then
sharpen these bounds. The table lists inclusive ranges;
each row's gap bounds imply the next row's length bounds.

| Input bounds | Exact gap bounds | Consequent bounds |
|---|---|---|
| `a<=55, m<=298` | `epsilon,eta>2^(-9)` | `a<=19, m<=106` |
| `a<=19, m<=106` | `epsilon,eta>2^(-7)` | `a<=15, m<=85` |

For each tested exponent `r`, let `L_r=bit_length(3^r)-1`.
The smallest allowed negative gap is
`(3^r-2^L_r)/3^r`; the smallest allowed positive gap is
`(2^(L_r+1)-3^r)/2^(L_r+1)`. Comparing these rational
numbers with the stated powers of 2 proves the table,
without evaluating logarithms numerically.

For fixed `a`, the endpoint ceiling
`2^(P-a)*3^a/(3^a-2^P)` increases with `2^P`.
Its maximum for all `1<=a<=15` and `a<=P<alpha*a`
therefore occurs among `P=bit_length(3^a)-1`.
The certificate checks exactly that this maximum is

```
68024448/7153 < 9510,       at a=12, P=19.
```

By (5), the canonical state consequently satisfies

```
h<9510,
x<3h/(2eta)<3*9510*128/2=1825920<2^21.              (15)
```

Finally, the certificate checks that every odd seed
`3<=s<2^21` reaches a smaller positive odd integer under
`3x+1`. Induction on odd seeds shows that every positive
odd integer in that range reaches 1. The hypothetical
nontrivial integer cycle contains the state `x` in (15),
which is impossible. This proves `q>1` without an external
minimum, convergence computation or period bound.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/expanding-negative-prefix-mersenne-exclusion/check_all_endpoints.py
python3 -O areas/cycles/results/expanding-negative-prefix-mersenne-exclusion/check_all_endpoints.py
```

The [certificate](check_all_endpoints.py) checks its
[deterministic receipt](check_all_endpoints.json). Use
`--write-receipt` to regenerate it deliberately. It verifies
the intercept estimate on a stated finite grid, rational
series enclosures for the elementary logarithms, LMN
parameter constants, the cutoff and derivative comparisons,
all `2^20-1` fractional-gap intervals, the two finite power-gap
passes, the endpoint ceiling and descent below `2^21`,
and genuine closed and nonclosed negative prefixes with
their modified positive trajectories. These controls do not assert the
existence of an admissible complete signed join.

All eleven shared actual `3x+d` controls are replayed.
Their reduced denominators exceed one, so they fail the
supposition `q=1`. The external LMN theorem is not replayed
or formalized here.

## Remarks

The [closed-prefix denominator law](../closed-negative-prefix-mersenne-denominator-law/README.md)
supplied the endpoint identity and binary-divisibility idea.
Section 1 rederives those elementary steps directly from
the normal form and enclosure so the source graph separates
this theorem's sole LMN assumption from that node's
sole-EXT-1 bounded-endpoint exclusion. Neither result is
silently replaced.

The extra estimate is (5): together with `g<=h` and an
expanding first slope, it permits the endpoint to cancel
from the prefix bound. Applying one logarithm theorem to
both signs gives a bound covering every closed negative
cycle and the stated nonclosed prefixes. Even values of
`J` remain allowed: nonclosed prefixes need not have
`3` coprime to `h`. The argument does not show that the
auxiliary signed paths are impossible or exclude arbitrary
four-mismatch words.
Novelty of this scoped combination is undetermined.
Same-session scrutiny leaves the status `written`.

## History

- 2026-11-08: cancelled the endpoint using the expanding-prefix
  intercept and binary divisibility, then bounded both gap
  signs with LMN. Exact finite gap bootstraps and a local
  descent remove an external period input. Included nonclosed
  prefixes with `g<=h`. Kept this argument separate from the earlier
  bounded-endpoint result with its different external input.
