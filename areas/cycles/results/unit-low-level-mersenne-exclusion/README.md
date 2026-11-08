---
id: unit-low-level-mersenne-exclusion
kind: result
title: Low-to-high Mersenne joins with unit low addend exclude denominator one
status: written
claim: >
  Raw odd-only valuation words. Let J>=2 and let h,g be positive
  odd integers. Suppose A is any nonempty exact 3x+1 segment
  from -h to -g, and B is a nonempty exact 3x+(2^J-1) segment
  from -g to h with last(B)>J. Reconstruct u=A[J-1]B[-J],
  v=AB[1], and suppose 2^(sum(A)+sum(B))>3^(len(A)+len(B)).
  Under the declared Laurent-Mignotte-Nesterenko two-logarithm
  bound, den(uv)>1. No endpoint order, first-slope condition,
  endpoint or level bound, length restriction, primitivity,
  near-criticality, external convergence computation or period
  input is assumed. A high-terminal-valuation intercept estimate
  gives h+1<(3/2)^len(B). A denominator-one candidate then has
  m=len(A)+len(B)<65*log_2(1/eta)+90. LMN and exact finite
  positive gaps force m<=1844 and a positive integer cycle
  minimum below 2^20, where complete local descent excludes a
  nontrivial cycle. This settles low-to-high r=1 normal forms,
  not the other order, higher low levels, or general four mismatches.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms]
certificates: [check_unit_low_level.py]
evidence:
  - "check_unit_low_level.json: terminal-intercept bound, exact signed and modified positive prefixes in every first-slope regime, one-sided fractional gaps, finite minimum bound, local descent and eleven actual-cycle controls"
tags: [cycles, half-defects, signed-orbits, denominators, linear-forms, effective-bounds]
---

# Low-to-high Mersenne joins with unit low addend exclude denominator one

## Statement

Use the raw odd-only signed map
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers,
excluding zero numerators and taking absolute values for the
valuation of a negative numerator. Let `J>=2`, `N=2^J`,
and let `h,g` be positive odd integers. Suppose two nonempty
exact segments with positive valuation words satisfy

```
A: -h -> -g under T_1,
B: -g ->  h under T_(N-1),      last(B)>J.
```

Write `A[t]` for changing only the final letter by `t`, and put

```
u=A[J-1]B[-J],       v=AB[1],
a=len(A), P=sum(A), b=len(B), T=sum(B),
m=a+b,              S=P+T,
D=2^S-3^m>0,        eta=D/2^S,       G=log_2(1/eta).
```

These are precisely the low-to-high `r=1` reconstructions in
the [Mersenne normal form](../two-half-defect-mersenne-normal-form/README.md).
Their positive word `uv` has length `2m` and total `2S`.
Under the sole external input
[LMN](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md),

```
den(uv)>1.
```

There is no upper bound on any endpoint, level, length,
valuation or intermediate state, and no comparison between
`g` and `h` or restriction on the first slope. Primitivity
is not needed. The theorem concerns the normalized rational
`3x+1` cycle; for the same word under `3x+d`, actual states
are `d` times the normalized states. The auxiliary signed
segments themselves are not asserted to be impossible.

Every signed `T_1` orbit starting negative stays negative,
so writing the interface as `-g` loses no `r=1` low-to-high
case. The result includes the earlier closed and expanding
negative-prefix subcases. The high-to-low order, low levels
`r>=2`, and arbitrary four-mismatch rotations remain outside
its scope.

## Proof

### 1. Retain the endpoint and residual denominator

Suppose `den(uv)=1`. Let `x` be the canonical positive odd
integer cycle state, and put

```
alpha=log_2(3),       sigma=3^a/2^P,
c=3^b/2^T,           lambda=sigma*c=1-eta.
```

The final letter of `v` is at least `J+2>=4`, so the word
cannot repeat the trivial `(2)` cycle. The certificate checks
that every odd seed from 3 through 33 reaches 1. Consequently
every state of this hypothetical nontrivial cycle is at least
35. This is a local calculation for `3x+1`, not an assumption
about the signed maps or other additive parameters.

The ordinary additive-one affine compositions satisfy

```
F_A(t)=sigma*(t+h)-g,
F_B(t)=c*t+(h+c*g)/(N-1),
C_A=h*3^a-g*2^P>0.
```

The normal-form reconstruction gives
`F_u(t)=2c*F_A(t)+N*(h+c*g)/(N-1)` and `F_u(x)=2x+h`.
Expanding these equations yields

```
2(N-1)D*x=h*D+3^b*F,
F=(2N-1)h*3^a-(N-2)g*2^P
 =(N+1)h*3^a+(N-2)C_A,      0<F<2N*h*3^a.          (1)
```

Thus `D|F`, because `x` is an integer and `gcd(D,3)=1`.
In particular `eta*3^m<D<=F`, giving

```
alpha*b<J+log_2(h)+G+1.                             (2)
```

These are the elementary endpoint identities used in the
[expanding-prefix result](../expanding-negative-prefix-mersenne-exclusion/README.md),
rederived here without its slope or endpoint-order hypotheses.
Neither (1) nor the divisibility requires `gcd(h,3)=1`.

The [state enclosure](../mersenne-join-state-enclosure/README.md)
with first Mersenne power 2 gives `x<3h/(2eta)`.
If `Y` is the positive odd state after `A[J-1]`, then

```
3^a*(x+h)=2^P*(2^(J-1)*Y+g).
```

Since `J>=2` and `g` is odd, the parenthesis is odd.
Therefore

```
v_2(x+h)=P,
2^P<=x+h<4h/eta,
P<log_2(h)+G+2.                                     (3)
```

### 2. The high terminal valuation bounds the endpoint

Let `w=last(B)>=J+1`, and let `E_i` be the sum of the first
`i` letters of `B`. The last letter and the other remaining
positive letters give

```
E_i<=T-w-b+1+i                 (0<=i<b).
```

Consequently the ordinary additive-one intercept obeys

```
C_B/2^T
 <=2^(1-w-b)*sum_(i=0)^(b-1) 3^(b-1-i)*2^i
 =2^(1-w)*((3/2)^b-1).
```

The signed endpoint equation for `B` is
`h+c*g=(N-1)C_B/2^T`. Since `w>=J+1`, this gives

```
h+c*g <= (1-2^(-J))*((3/2)^b-1),
h+1 < (3/2)^b,
log_2(h)<(alpha-1)*b.                               (4)
```

This terminal-intercept estimate holds without any first-slope
or denominator-one hypothesis. Combining (2) and (4), and
then (3), `a<=P`, and `alpha<8/5`, gives

```
b<J+G+1,
a<=P<(3/5)b+G+2.                                   (5)
```

### 3. Both segment lengths depend only on the positive gap

The cycle product and the minimum 35 give

```
2^(2S)<= (106/35)^(2m)<2^(16m/5),
S<8m/5,
```

where `106^5<2^8*35^5` is checked exactly. Also `T>=J+b`
and `P>=a`, so

```
J<=S-P-b<(3/5)(a+b).
```

Use this with (5) to obtain `(2/5)b<(3/5)a+G+1`.
Substituting the other inequality in (5) gives

```
(1/25)b<(8/5)G+11/5,
b<40G+55,
a<25G+35,
m<65G+90.                                          (6)
```

This positive coefficient is why the local minimum 35 is
useful: the rougher state floor 3 does not close this
length inequality. No first-slope condition was used.

### 4. LMN supplies a uniform finite cutoff

Let `Lambda=S*ln(2)-m*ln(3)>0`. The declared LMN statement
with bases 2 and 3, field degree 1, and logarithmic heights
1 and 2 gives

```
ln(Lambda)>-48.68*max(ln(b')+0.14,21)^2,
b'=S/2+m<9m/5<2m.
```

The elementary inequalities
`1-exp(-Lambda)>min(Lambda/2,1/2)` and `1/2<ln(2)<1`
therefore give

```
G<H(m),
H(m)=1+98*max(log_2(m)+2,21)^2.                     (7)
```

Indeed `ln(2m)+0.14<log_2(m)+2` and
`48.68/ln(2)<97.36<98`. The certificate checks these
constant comparisons through exact rational log enclosures.

At `m=2^22`, `H=56449` and

```
2^22-(65H+90)=525029>0.
```

For all larger `m`, the active logarithmic branch has

```
d/dm [m-65H(m)-90] > 1-25480*(log_2(m)+2)/m > 0.
```

The last inequality holds at the cutoff since
`25480*24<2^22` and persists because `(log_2(m)+2)/m`
decreases there. Equations (6) and (7) force

```
m<2^22.                                             (8)
```

### 5. Exact finite gaps force a small cycle minimum

The certificate uses 80 terms of

```
ln(z)=2*sum_(j>=0) t^(2j+1)/(2j+1),
t=(z-1)/(z+1),       z=2,3,
```

with tail at most `2*t^161/[161*(1-t^2)]`. Dividing the
resulting rational log enclosures and rounding outward to
denominator `2^96` gives `alpha_lo<alpha<alpha_hi`.
For every `1<=r<2^22`, exact integer division checks that
both endpoints of `[r*alpha_lo,r*alpha_hi]` have the same
floor `k` and that

```
1-(r*alpha_hi-k)>2^(-25).
```

Since `S>m*alpha`, this gives `Lambda>2^(-26)` and
`eta>2^(-27)`, hence `G<27`. Equation (6), keeping the
strict integer endpoint, gives

```
m<=1844.                                            (9)
```

For each integer `1<=r<=1844`, put

```
L_r=bit_length(3^r),
eta_r=(2^L_r-3^r)/2^L_r.
```

The certificate checks the exact integer inequality

```
3*2^20*(2^L_r-3^r)>r*2^L_r,
eta_r>r/(3*2^20).                                  (10)
```

This `eta_r` is the smallest positive gap for length `r`:
it increases with the allowed integer total. In particular,
the candidate's `eta` is at least `eta_m`.

Let `X` be the minimum state of the full `2m`-step integer
cycle. The cycle product gives, even if the word repeats,

```
eta < ln(2^S/3^m)
    = (1/2)*sum_(i=0)^(2m-1) ln(1+1/(3x_i))
    < m/(3X).
```

Together with (10), this forces `X<2^20`. The certificate
verifies that every odd seed `3<=s<2^20` reaches a smaller
positive odd integer under `3x+1`. Induction on odd seeds
implies convergence to 1 throughout this finite range.
The hypothetical nontrivial cycle contains `X`, a contradiction.
Thus `den(uv)>1` using LMN alone.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/unit-low-level-mersenne-exclusion/check_unit_low_level.py
python3 -O areas/cycles/results/unit-low-level-mersenne-exclusion/check_unit_low_level.py
```

The [certificate](check_unit_low_level.py) compares its output
with the [generated receipt](check_unit_low_level.json). Use
`--write-receipt` to regenerate it. It checks the terminal
intercept estimate on an explicit finite word grid, the endpoint
identity, genuine negative prefixes and their modified positive
trajectories in every first-slope and endpoint-order regime,
specified high-boundary signed second segments, all fractional
gap intervals in (8), every exact power comparison in (10),
and the complete local descent. Partial segment controls are
not claimed to be complete admissible joins. Guards abort on
an unfinished computation; no truncation is accepted.

All eleven standard positive odd-only `3x+d` cycles are replayed.
Their reduced denominators exceed one, so they do not meet the
contradictory hypothesis `q=1`. The local minimum and descent
arguments apply only to ordinary `3x+1`. LMN is cited, not
reproved or formally verified here. All finite checks use exact
standard-library arithmetic and remain active under `python3 -O`.

## Remarks

The [closed-prefix law](../closed-negative-prefix-mersenne-denominator-law/README.md)
and [expanding-prefix exclusion](../expanding-negative-prefix-mersenne-exclusion/README.md)
retain their stated proofs and inputs. The present argument
uses the second segment's high terminal valuation to bound
the endpoint, then combines a small local minimum calculation
with the residual-denominator divisibility. This removes
both the first-slope and endpoint-order restrictions.

The result does not prove that a normalized state is uniformly
below 1, or that signed joins do not exist. It excludes integer
cycles through a length bound and a complete finite calculation.
Novelty of the scoped combination is undetermined. Same-session
scrutiny does not change the `written` status. The general
[four-mismatch question](../../questions/rotation-distance-at-least-5.md)
remains open.

## History

- 2026-11-08: used the terminal-intercept budget to settle all
  low-to-high `r=1` normal forms, with LMN as the sole external
  input. No restriction on the first signed prefix's slope,
  endpoint order, or length is required.
