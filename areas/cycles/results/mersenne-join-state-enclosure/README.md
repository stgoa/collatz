---
id: mersenne-join-state-enclosure
kind: result
title: Signed Mersenne joins have a uniform state enclosure in terms of endpoint and slope
status: written
claim: >
  Raw odd-only positive valuation words reconstructed from either order of
  the two-half-defect Mersenne normal form, with nonempty exact signed
  segments -h to z to h and the required boundary valuations. Let M-1
  and N-1 be their ordered positive Mersenne addends, K=min(M,N),
  R=max(M,N), n=len(A)+len(B), S=sum(A)+sum(B), and lambda=3^n/2^S.
  If D_(uv)>0, equivalently 0<lambda<1, the canonical normalized state
  x=C_(uv)/D_(uv) satisfies
  h*(1+R*lambda)/(M*(R-1)*(1-lambda)) < x <
  h*(1+K*lambda)/(M*(K-1)*(1-lambda)).
  This holds for both signs of z, without bounds on the levels or lengths.
  Any lower bound x>=X>0 forces
  lambda>(M*(K-1)*X-h)/(M*(K-1)*X+K*h).
  In particular, failure of this strict slope bound at X=1 excludes
  denominator one. Positive auxiliary-cycle insertions decrease the
  upper state bound. No external or near-critical hypothesis is used.
authors:
  - Codex cycle research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [two-half-defect-mersenne-normal-form, baseline-obligation-transfer-controls]
certificates: [check_state_enclosure.py]
evidence:
  - "check_state_enclosure.json: symbolic identities, affine controls of every interface sign, exact signed-word reconstructions and actual-cycle replay"
tags: [cycles, denominators, half-defects, signed-orbits, state-bounds, slope]
---

# Signed Mersenne joins have a uniform state enclosure in terms of endpoint and slope

## Statement

Use the raw odd-only maps
`T_d(y)=(3y+d)/2^v_2(3y+d)` on nonzero odd integers, with
zero numerators excluded and absolute values used for negative
numerators. Fix `J>r>=1`, put `p=J-r`, and take two nonempty
signed segments `A,B` joining `-h -> z -> h`, for a positive
odd integer `h`, in either exact normal form:

| Order | Addends in `A,B` | Boundary conditions | Reconstructed halves | `M,N` |
|---|---|---|---|---|
| High to low | `2^J-1, 2^r-1` | `last(A)>p`, `last(B)>r` | `u=A[-p]B[-r]`, `v=AB[J]` | `2^J,2^r` |
| Low to high | `2^r-1, 2^J-1` | `last(B)>J` | `u=A[p]B[-J]`, `v=AB[r]` | `2^r,2^J` |

Here `A[t]` changes only the last valuation by `t`.
The interface `z` may be negative or positive. Put

```
K=min(M,N),       R=max(M,N),
n=len(A)+len(B),  S=sum(A)+sum(B),
lambda=3^n/2^S,   x=C_(uv)/D_(uv).
```

Suppose `D_(uv)>0`, equivalently `0<lambda<1`. Then

```
 h*(1+R*lambda)                 h*(1+K*lambda)
------------------- < x < -------------------.      (1)
M*(R-1)*(1-lambda)         M*(K-1)*(1-lambda)
```

The state `x` is the normalized rational `3x+1` state at the
canonical cut. For the same word under `3x+d`, the actual state
is `d*x`.

**Slope consequence.** If `x>=X>0`, then

```
          M*(K-1)*X-h
lambda > ---------------.                          (2)
          M*(K-1)*X+K*h
```

In particular, if

```
          M*(K-1)-h
lambda <= -------------,                           (3)
          M*(K-1)+K*h
```

then `x<1` and the word has denominator greater than one.
When the numerator on the right is nonpositive, (3) supplies
no exclusion because `lambda>0`.

There are no upper bounds on the Mersenne levels, word lengths,
valuations or intermediate states. The result is an enclosure
and a sufficient exclusion criterion, not an assertion that
every join satisfies (3).

## Proof

**Exact affine relations.** Write the ordinary additive-one
compositions of the two nonempty segments as

```
F_A(t)=a*t+b,       F_B(t)=c*t+e,
a,b,c,e>0,         lambda=a*c.
```

Their signed auxiliary endpoint equations are

```
z=-a*h+(M-1)*b,       h=c*z+(N-1)*e.                (4)
```

Changing a word's final valuation by `t` multiplies its affine
output by `2^(-t)`. The boundary changes in either row of the
table therefore give

```
F_u(t)=M*c*F_A(t)+N*e.                              (5)
```

The [normal-form identity](../two-half-defect-mersenne-normal-form/README.md)
also gives `F_u(x)=M*x+h`. Set `T=c*z`. Since the two additive
intercepts are strictly positive, (4) implies

```
-lambda*h < T < h.                                 (6)
```

This interval uses neither a positive interface nor an immediate
negative-to-positive crossing.

Substitute `c*b=(T+lambda*h)/(M-1)` and
`e=(h-T)/(N-1)` in (5). After collecting terms,

```
M*(M-1)*(N-1)*(1-lambda)*x
  = h*(M-1)+M*lambda*h*(N-1)+(N-M)*T.               (7)
```

**Strict interpolation.** The expression for `x` in (7) is
affine in `T`. At the two endpoints of (6) it has the values

```
T=-lambda*h:  h*(1+N*lambda)/(M*(N-1)*(1-lambda)),
T=h:          h*(1+M*lambda)/(M*(M-1)*(1-lambda)).    (8)
```

More explicitly, put
`theta=(T+lambda*h)/(h*(1+lambda))`. Then `0<theta<1`,
and `x` is `(1-theta)` times the first expression in (8),
plus `theta` times the second.

For `R>K>1`,

```
(1+K*lambda)*(R-1)-(1+R*lambda)*(K-1)
  =(R-K)*(1+lambda)>0.                             (9)
```

Thus `(1+t*lambda)/(t-1)` strictly decreases with `t`.
The endpoint values in (8) are distinct, and their strict
convex combination gives (1) in either order.

**The slope condition.** Combining `x>=X` with the strict
upper bound in (1), and multiplying positive denominators,
gives

```
lambda*(M*(K-1)*X+K*h)>M*(K-1)*X-h,
```

which is (2). Its contrapositive at `X=1` proves (3),
including equality at the threshold. A normalized positive
state below 1 excludes denominator one.

**Persistence under positive cycle insertion.** The upper
function in (1) is strictly increasing in `lambda` on `(0,1)`:
for `0<lambda_1<lambda_2<1`, its difference is

```
h*(K+1)*(lambda_2-lambda_1)
-------------------------------------- > 0.
M*(K-1)*(1-lambda_1)*(1-lambda_2)
```

An auxiliary positive cycle returning to a state `y>0` has
ordinary affine fixed point `y/d>0`. Its positive additive
intercept forces its slope into `(0,1)`. Inserting copies
within either segment, while retaining the altered terminal
arrows, multiplies `lambda` by these contracting factors and
preserves `M,N,h`. Consequently, once (3) holds for a base
join, it holds after any finite number of such insertions.
Negative cycles are expanding and are not covered by this
last monotonicity conclusion; enclosure (1) itself still
applies whenever the reconstructed word has `D>0`.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/mersenne-join-state-enclosure/check_state_enclosure.py
python3 -O areas/cycles/results/mersenne-join-state-enclosure/check_state_enclosure.py
```

The [certificate](check_state_enclosure.py) writes
[its deterministic receipt](check_state_enclosure.json).
It verifies the endpoint, ordering and threshold polynomial
identities; tests exact positive affine data with negative,
zero and positive interfaces; and reconstructs specified
genuine signed joins in both orders, including larger endpoints
and repeated positive cycles. The abstract affine controls
audit the algebra; they are explicitly not claimed to be
valuation words, and a zero interface is outside the signed
normal-form domain.

All eleven shared actual `3x+d` fixtures are replayed. The
genuine word controls also replay their reduced integer cycles,
including the existing `3x+361` and `3x+893` examples. They
satisfy the enclosure in normalized states and retain their
denominators greater than one. No finite parameter census is
used to establish the unbounded theorem.

## Remarks

This is an elementary consequence of the two positive
weighted-intercept blocks, equivalently of (4). Its usefulness
is the explicit slope condition for either sign of the
interface. The [small-endpoint theorem](../small-mersenne-endpoint-exclusion/README.md)
instead excludes a region using only `M,h`, independently
of `lambda`. The two criteria address different parts of the
remaining normal-form problem; neither settles it entirely.

For a hypothetical integer `3x+1` cycle, any proved lower
bound on its states can be substituted for `X` in (2).
If the resulting right-hand side is positive and close to 1,
it confines the candidate to a correspondingly small positive
drift `-2*log_2(lambda)`. No general near-critical conclusion
is assumed or inferred when this bound is weak.

Moving to the other defect cut does not automatically provide
a second positive-addend representation. It follows `B` from
`z` to `h`, then the reflection of `A` from `h` to `-z`;
the latter segment has addend `-(M-1)`. The positivity used
in (6) cannot be transferred to that mixed-sign description
without a new argument.

Novelty is undetermined. This node supplies a reusable
enclosure, not a claim to exclude a previously uncovered
global class of hypothetical cycles. The general
[four-mismatch question](../../questions/rotation-distance-at-least-5.md)
remains open.

## History

- 2026-11-08: isolated the total-slope state enclosure while
  investigating larger signed endpoints. Same-session scrutiny
  does not change the `written` status (Codex cycle research lane,
  GPT-6 Astra; directed by Santiago Armstrong).
