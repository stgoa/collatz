---
id: negative-interface-mersenne-exclusion
kind: result
title: Signed Mersenne joins with negative interface exclude denominator one
status: written
claim: >
  Raw odd-only positive valuation words. For every J>r>=1 and
  positive odd h,g, take nonempty exact signed segments A,B
  joining -h to -g to h with Mersenne addends in either order.
  In low-to-high order require last(B)>J and reconstruct
  u=A[J-r]B[-J], v=AB[r]. In high-to-low order require
  last(A)>J-r and last(B)>r, and reconstruct
  u=A[-(J-r)]B[-r], v=AB[J]. Suppose
  2^(sum(A)+sum(B))>3^(len(A)+len(B)). Under the declared
  Laurent-Mignotte-Nesterenko two-logarithm bound, den(uv)>1.
  No level, endpoint, length or valuation bound, first-slope
  condition, endpoint ordering, primitivity, near-criticality,
  external convergence computation or period input is used.
  Exact division of the full endpoint identity removes the
  factor equal to the first addend and gives the same length
  bound and finite closure as the unit-low-level result.
  Positive interfaces remain outside this statement; the
  auxiliary signed joins are not asserted to be impossible.
authors:
  - Codex negative-interface research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure, unit-low-level-mersenne-exclusion]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms]
certificates: [check_negative_interface.py]
evidence:
  - "check_negative_interface.json: exact polynomial factorization, general-level signed and modified positive prefixes, positive-interface countercontrol, and hash-pinned replay of the predecessor certificate"
tags: [cycles, half-defects, signed-orbits, denominators, linear-forms, effective-bounds]
---

# Signed Mersenne joins with negative interface exclude denominator one

## Statement

Use the raw odd-only signed maps
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers,
excluding zero numerators. Let `J>r>=1`, put
`p=J-r`, and let `h,g` be positive odd integers.
Suppose two nonempty exact segments with positive valuation
words satisfy

```
A: -h -> -g under T_(M-1),
B: -g ->  h under T_(N-1).
```

For a word `A`, the notation `A[t]` changes only its final
letter by `t`. The ordered powers, boundary conditions and
positive reconstructions are those of the Mersenne normal form:

| Order | First power `M` | Second power `N` | Required valuations | `u` | `v` |
|---|---:|---:|---|---|---|
| Low to high | `2^r` | `2^J` | `last(B)>J` | `A[p]B[-J]` | `AB[r]` |
| High to low | `2^J` | `2^r` | `last(A)>p`, `last(B)>r` | `A[-p]B[-r]` | `AB[J]` |

Put

```
a=len(A), P=sum(A), b=len(B), T=sum(B),
m=a+b,              S=P+T,
D=2^S-3^m>0,        eta=D/2^S,       G=log_2(1/eta).
```

The complete word has length `2m`, total valuation `2S`,
and denominator `D_(uv)=(2^S+3^m)D`. Under the sole
external input [LMN](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md),

```
den(uv)>1.
```

There is no restriction on either level, endpoint, length,
valuation or intermediate state, and no first-slope or
endpoint-order assumption. Primitivity is not required.
The conclusion concerns the normalized rational `3x+1`
cycle; it does not exclude actual cycles for other addends.

This covers both Mersenne normal-form orders with negative
interface. The first segment can instead cross to a positive
interface; that case remains outside the theorem.
No nonexistence of the auxiliary signed segments is claimed.

## Proof

### 1. Divide the full endpoint identity before bounding it

Suppose `den(uv)=1`, and let `x` be its canonical positive
odd integer state. The last letter of `v` is at least
`J+r+1>=4`, so the word is not a repetition of the trivial
valuation word `(2)`. The local descent in the
[unit-low-level certificate](../unit-low-level-mersenne-exclusion/check_unit_low_level.py)
checks every odd seed through 33. Thus every state of this
hypothetical nontrivial `3x+1` cycle is at least 35.

Put `alpha=log_2(3)`, `sigma=3^a/2^P`, `c=3^b/2^T`
and `lambda=sigma*c=1-eta`. The signed endpoint identities
are

```
(M-1)C_A=h*3^a-g*2^P>0,
F_A(t)=sigma*t+(sigma*h-g)/(M-1),
F_B(t)=c*t+(h+c*g)/(N-1).
```

The normal-form reconstruction gives
`F_u(t)=M*c*F_A(t)+N*(h+c*g)/(N-1)` and
`F_u(x)=M*x+h`. Expanding yields

```
M(M-1)(N-1)D*x=h(M-1)D+3^b*F,
F=(MN-1)h*3^a-(N-M)g*2^P.
```

The first endpoint identity supplies the exact factorization

```
F=(M-1)F_0,
F_0=(N+1)h*3^a+(N-M)C_A.
```

Divide the entire equality by `M-1` to obtain

```
M(N-1)D*x=hD+3^b*F_0.                              (1)
```

This is an equality of integers; no modular cancellation or
coprimality between `D` and `M-1` is required. Hence
`D|F_0`, since `gcd(D,3)=1`. The negative interface gives
`0<(M-1)C_A<h*3^a`. If `M<N`, then

```
0<F_0<[(MN-1)/(M-1)]*h*3^a<2N*h*3^a.
```

If `M>N`, the coefficient `N-M` is negative, and instead

```
0<[(MN-1)/(M-1)]*h*3^a<F_0<(N+1)h*3^a<2N*h*3^a.
```

Using `D=eta*2^S>eta*3^m`, we conclude

```
alpha*b<log_2(N)+log_2(h)+G+1.                      (2)
```

Only the second block's level remains in this estimate.

### 2. The binary and terminal bounds are uniform in the levels

Let `Y` be the positive odd integer state after the modified
first block. In low-to-high order its boundary equation is

```
3^a*((M-1)x+h)
  =2^P*((M-1)2^(J-r)Y+g).
```

The parenthesis on the right is odd, since `J>r` and `g`
is odd, so `v_2((M-1)x+h)=P`. In high-to-low order,

```
3^a*((M-1)x+h)=2^(P-p)*((M-1)Y+2^p*g),
v_2((M-1)x+h)=P-p.
```

Here the parenthesis is again odd, and `last(A)>p` gives
`P-p>=a`. In either order the exact valuation is at least
`a`. Write `K=(M-1)x+h`. The
[state enclosure](../mersenne-join-state-enclosure/README.md)
gives `K<4h/eta` in both orders. More explicitly,

```
M<N: K<h*(M+1)/(M*eta)<=3h/(2eta),
M>N: K<h*(N+1)*(M-1)/(M*(N-1)*eta)<3h/eta.
```

For the second line, substitute its upper enclosure for `x`
and use `lambda<1` after combining the `+h` term. Since
`2^a<=2^v_2(K)<=K`, both cases give

```
a<log_2(h)+G+2.                                    (3)
```

For the second block, let `j_2=log_2(N)`, so
`w=last(B)>=j_2+1` in either order. Positivity
of its other letters gives the same terminal-intercept bound
as in the unit-low-level proof:

```
C_B/2^T <= 2^(1-w)*((3/2)^b-1).
```

Since `h+c*g=(N-1)C_B/2^T`, it follows that

```
h+c*g <= (1-2^(-j_2))*((3/2)^b-1),
h+1<(3/2)^b,
log_2(h)<(alpha-1)b.                                (4)
```

Combining (2)--(4), using `alpha<8/5`, gives

```
b<j_2+G+1<=J+G+1,       a<(3/5)b+G+2.               (5)
```

### 3. Transfer the arithmetic length and finite closure

The positive cycle product, with all states at least 35,
gives

```
2^(2S)<2^(16m/5),       S<8m/5,
```

because `106^5<2^8*35^5`. In low-to-high order,
`T>=J+b` and `P>=a`. In high-to-low order,
`P>=a+p` and `T>=b+r`. Thus `S>=m+J` in both cases,
so `J<(3/5)(a+b)`. Together with (5), this yields

```
(2/5)b<(3/5)a+G+1,
b<40G+55,       a<25G+35,       m<65G+90.            (6)
```

These are exactly the hypotheses used by sections 4--5 of
the [unit-low-level result](../unit-low-level-mersenne-exclusion/README.md).
That part of its proof is arithmetic in the positive half-gap
`eta=1-3^m/2^S`; it uses neither the first segment's addend
nor an assumption about its slope. For clarity, the chain is:

1. Since `S<8m/5`, LMN applied to
   `S*ln(2)-m*ln(3)>0` gives
   `G<H(m)=1+98*max(log_2(m)+2,21)^2`.
   Equation (6) then forces `m<2^22`.
2. Exact outward rational logarithm enclosures check every
   exponent `1<=m<2^22`, giving `eta>2^(-27)` and `G<27`.
   Thus (6), with its strict integer endpoint, gives `m<=1844`.
3. For each `1<=m<=1844`, put `L_m=bit_length(3^m)`.
   The exact checked inequality is
   `3*2^20*(2^L_m-3^m)>m*2^L_m`. Every allowed total
   has `eta>=1-3^m/2^L_m>m/(3*2^20)`.
4. If `X` is the minimum of the full `2m`-step cycle, its
   product gives `eta<ln(2^S/3^m)<m/(3X)`. Hence
   `X<2^20`. Complete local odd-seed descent below `2^20`
   excludes such a nontrivial `3x+1` cycle.

The half-length is `m` in each arithmetic bound, while the
cycle product has `2m` factors. All the finite assertions
in this chain are replayed by the attached certificate via
the pinned predecessor certificate. This proves `den(uv)>1`
with LMN alone.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/negative-interface-mersenne-exclusion/check_negative_interface.py
python3 -O areas/cycles/results/negative-interface-mersenne-exclusion/check_negative_interface.py
```

The [certificate](check_negative_interface.py) checks its
[deterministic receipt](check_negative_interface.json).
Use `--write-receipt` to regenerate it deliberately.
It verifies the polynomial factorization and divided identity,
genuine negative prefixes at levels above 1, their
modified positive trajectories and exact binary valuations,
and the uniform residual bounds without a first-slope or
endpoint-order restriction.

The certificate checks the committed source and receipt
hashes of the unit-low-level certificate, then executes it
and checks the receipt again. That replay covers the terminal
intercept estimate, LMN constants, all `4194303` finite gap
intervals, `1844` exact power comparisons, descent of all
`524287` odd seeds below `2^20`, and all eleven standard
positive cycles for `d=5,7,13,61`. The proof and finite data
are reused without copying a second interval enumeration.

Partial signed controls are not claimed to be complete
admissible joins. A genuine positive-interface reconstruction
is retained as an outside-scope control. All checks remain
active under optimized Python; a hash mismatch or unfinished
predecessor replay fails rather than accepting partial data.

## Remarks

The [unit-low-level theorem](../unit-low-level-mersenne-exclusion/README.md)
settles low-to-high `r=1`, where every negative start remains
negative under the first map. The new step is dividing the full
integer identity by `M-1` before estimating the residual
factor; a direct bound on `F` would leave an unnecessary
factor `M` and a level-dependent length inequality.

The negative interface is essential to this argument. For
`r=3,J=5,h=1`, the genuine segments with words
`A=(2,1,1)` and `B=(6)` go
`-1 -> 1 -> 5 -> 11 -> 1`. The interface is positive,
and the bound `h+1<(3/2)^len(B)` would read `2<3/2`.
Their reconstruction has normalized canonical state `1/41`
and reduced denominator 41. This does not contradict the
theorem; it shows that its terminal endpoint estimate cannot
be transferred to positive interfaces unchanged.

Positive interfaces need additional arguments. No general
four-mismatch or auxiliary-orbit
nonexistence claim is made. Novelty of this scoped extension
is undetermined. Same-session scrutiny leaves status `written`.

## History

- 2026-11-08: factored the full endpoint identity before
  taking a size bound, removing the first Mersenne power
  from the residual estimate. Both orders reuse the unit-level
  arithmetic closure with its existing sole LMN input.
