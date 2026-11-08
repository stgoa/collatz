---
id: one-defect-first-block-mersenne-exclusion
kind: result
title: One non-one letter in the first low-to-high segment excludes denominator one
status: written
claim: >
  Raw odd-only clock. Let J>r>=1 and h,z be positive odd integers.
  Let nonempty positive words A,B give exact signed paths from -h to z
  under 3x+(2^r-1) and from z to h under 3x+(2^J-1), with last(B)>J.
  Suppose A has at most one letter greater than one, of arbitrary size
  and at any position. Put u=A[J-r]B[-J], v=AB[r], changing only the
  indicated final letters. If 2^(sum(A)+sum(B))>3^(len(A)+len(B)),
  then den(uv)>1 under only the declared Laurent-Mignotte-Nesterenko
  input. The lengths, levels, endpoints and entire word B are unbounded.
  The finite closure uses exact gaps through half-length 431 and local
  descent below 2^17. Other first segments and high-to-low joins remain
  outside this claim.
authors:
  - Codex signed-endpoint research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [positive-interface-mersenne-exclusion, two-half-defect-mersenne-normal-form, mersenne-join-state-enclosure]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms]
certificates: [check_one_defect.py]
evidence:
  - "check_one_defect.json: exact finite prefixes, genuine signed joins and reduced cycles, logarithm intervals, finite minimum bounds, local descent and actual-cycle controls"
tags: [cycles, mersenne-endpoints, valuation-words, denominators]
---

# One non-one letter in the first low-to-high segment excludes denominator one

## Statement

Write `W[d]` for the word obtained by adding `d` to the final
letter of a nonempty word `W`. Fix integers `J>r>=1`, and put

```
M=2^r, N=2^J, p=J-r.
```

Suppose positive odd integers `h,z` and positive valuation words
`A,B` give exact signed odd-only paths

```
T_(M-1)^A(-h)=z>0,    T_(N-1)^B(z)=h,    last(B)>J.
```

Every signed arrow has its specified exact valuation. Assume
that `A` has at most one letter greater than one. Thus either
`A=1^a`, or

```
A=1^u (e+1) 1^w,    u,w>=0, e>=1,    a=u+w+1.
```

There is no bound on `e,u,w`, or on any letter or length of `B`.
Set

```
a=len(A), b=len(B), P=sum(A), T=sum(B),
m=a+b, S=P+T, D=2^S-3^m>0,
u_word=A[p]B[-J],    v_word=AB[r].
```

Under the sole external
[LMN input](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md),
`den(u_word v_word)>1`.
The claim concerns these low-to-high positive-interface normal
forms. It does not exclude arbitrary four-mismatch words or
first segments with two or more non-one letters.

## Proof

### 1. The cycle cut and the remaining excess

Suppose `den(u_word v_word)=1`. The word-cycle correspondence
and [normal form](../two-half-defect-mersenne-normal-form/README.md)
give positive odd integer states of `3x+1`, with canonical state
`x` satisfying `F_(u_word)(x)=Mx+h`. The full word has length
`2m` and total `2S`. Put

```
alpha=log_2(3), lambda=3^m/2^S, eta=1-lambda,
G=log_2(1/eta)>0, c_r=log_2(1+1/M)<1,
I_A=C_A/2^P, sigma=3^a/2^P,
E_A=P-a, E_B=T-J-b>=0.
```

The last letter of `v_word` exceeds `J+r`, so the word is not
a repetition of `(2)`. Local descent of the odd seeds from 3
through 33 shows that the minimum of this nontrivial cycle is
at least 35. The product identity and `106^5<2^8*35^5` give

```
S<8m/5,    J=S-m-E_A-E_B<3m/5-E_A-E_B.              (1)
```

Signed positivity and the exact
[state enclosure](../mersenne-join-state-enclosure/README.md)
give

```
h<(M-1)C_A/3^a,
x < h*(1+M*lambda)/[M*(M-1)*eta]
  < kappa*C_A/3^a,
kappa=(lambda+1/M)/eta,    K=kappa+1=(1+1/M)/eta.
                                                                    (2)
```

In particular `1<K<2^(G+1)`. The positive-interface
[second-boundary argument](../positive-interface-mersenne-exclusion/README.md)
retains the entire exponent `T-J=b+E_B`, rather than just `b`:

```
b+E_B < (alpha-1)*a+r+G+c_r,
m+E_B < alpha*a+r+G+c_r.                             (3)
```

For completeness, at the actual state `Y` after `A[p]`, subtraction
of the two `B` endpoint equations gives

```
3^b*((N-1)Y-z)=2^(T-J)*(M*(N-1)*x-h).
```

The right bracket is odd, hence the nonzero difference on the
left has exact binary valuation `T-J`. Both `(N-1)Y` and `z`
are positive and smaller than `(M+1)*(3/2)^a/eta`, by the
same enclosure. Their absolute difference is smaller than
their maximum, proving (3). No ordering of those two states
is required.

### 2. The modified terminal arrow matters

Before the last letter of `A`, the ordinary additive-one path
from `x` agrees with the actual cycle. Its ordinary final
output is

```
F_A(x)=2^p Y,
```

which is a positive even integer, since `p>=1` and `Y` is odd.
Thus a run of ones reaching the end of ordinary `A` ends at
an even state, not an odd one.

If `A=1^a`, then `C_A/3^a=1-(2/3)^a<1` and

```
x+1<K,    v_2(x+1)=a,    a<G+c_r.                  (4)
```

The valuation follows from
`F_A(x)+1=3^a*(x+1)/2^a`, whose left side is odd.

Now let `A=1^u(e+1)1^w`, with `e>=1`. Put `n=u+1`.
The first `u` actual arrows have valuation one, so

```
x+1=2^n t,    t>=1 an integer.
```

This also holds when `u=0`, since `x` is odd. After the ordinary
exceptional arrow, write its state as `y`. Exact composition gives

```
y=(3^n t-1)/2^e,
y+1=(3^n t+2^e-1)/2^e,
v_2(y+1)=w,    2^w<=y+1.                            (5)
```

For `w=0`, this `y` is the even ordinary output of `A`, so
`v_2(y+1)=0`. For `w>0`, the terminal run of `w` ones ends
at that even output, giving the same exact valuation. This
covers defects at the first or last position and `a=1`.

The intercept is a geometric sum split at the exceptional
letter:

```
C_A/3^a=1+(2^e-1)*(2/3)^n-2^e*(2/3)^a.
```

Combining it with (2), and discarding only negative terms,

```
x+1<K*[1+2^e*(2/3)^n],
U=3^n t<K*(3/2)^n+K*2^e.                            (6)
```

There are two cases.

- If `2^n>=2K`, then `x+1=2^n t>=2K`. The first
  inequality in (6) implies `U<2K*2^e`. Consequently
  `alpha*n<e+G+2`. Also (5) gives
  `2^w<=y+1<2K+1<3K`, hence `w<G+3`.
- If `2^n<2K`, then `n<G+2`. Equations (5)-(6) give
  `y+1<K*(3/2)^n/2^e+K+1<2K*(3/2)^n`:
  here `e>=1`, `K>1`, and `(3/2)^n>=3/2`.
  Therefore `w<alpha*G+2alpha` and
  `a=n+w<(alpha+1)G+2alpha+2<3G+6`.

Using `3/2<alpha<8/5`, both cases imply the convenient
common bound

```
a < e/alpha+3G+6.                                  (7)
```

For the all-ones case (4), (7) also holds with `e=E_A=0`.
In the one-defect case `e=E_A`. This is the amplitude-sensitive
step: the exceptional value is not bounded or discarded.

### 3. Cancel the defect amplitude

Since `r<J`, equations (1) and (3) imply

```
(2/5)m+E_A+2E_B < alpha*a+G+c_r.
```

Substitute (7), with `e=E_A`, and `alpha<8/5`, `c_r<1`:

```
(2/5)m+2E_B < (29/5)G+53/5,
m < (29/2)G+53/2 < 15G+27.                         (8)
```

The possibly arbitrarily large `E_A` cancels. Neither `B`
nor its number of non-one letters has been restricted.

### 4. LMN and the local finite closure

For `Lambda=S*ln(2)-m*ln(3)>0`, the
[declared LMN specialization](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md)
applies with `b'=S/2+m<2m`, by (1). As in the positive-interface
result, `eta=1-exp(-Lambda)>min(Lambda/2,1/2)` gives

```
G<H(m),    H(m)=1+98*max(log_2(m)+2,21)^2.           (9)
```

At `m=2^20`, `H=47433` and `15H+27=711522<1048576`.
For larger `m`, the difference `m-15H(m)-27` increases:
`H'(m)<392*(log_2(m)+2)/m`, and
`15*392*22<2^20`; the logarithmic ratio decreases thereafter.
Thus (8) forces `m<2^20`.

The certificate uses 80 terms of the positive atanh series
`ln(t)=2*sum_(j>=0)z^(2j+1)/(2j+1)`, `z=(t-1)/(t+1)`,
with the tail bounded by `2*z^161/[161*(1-z^2)]`. It verifies
the outward enclosure

```
125573666586150569315490533898/2^96 < alpha
 <125573666586150569315490533899/2^96.
```

For every `1<=k<2^20`, the multiplied endpoints have the
same floor and their distance below the next integer exceeds
`2^-25`. These are exact integer comparisons. Hence
`Lambda>2^-26`, `eta>2^-27`, and `G<27`. Equation (8), using
the coarser `15G+27`, now gives `m<432`, so `m<=431`.

For every `1<=k<=431`, put `V_k=bit_length(3^k)`. Exact
integer arithmetic verifies

```
3*2^17*(2^V_k-3^k)>k*2^V_k.                        (10)
```

If `X` is the minimum of the full `2m`-step cycle, then

```
eta < Lambda
    =(1/2)*sum_(i=0)^(2m-1) ln(1+1/(3x_i))
    <m/(3X).
```

Also `eta>=(2^V_m-3^m)/2^V_m`. Thus (10) forces `X<2^17`.
The certificate verifies that every odd seed `3<=s<2^17`
reaches a smaller positive odd integer. Induction on the
seeds shows convergence to 1, contradicting this nontrivial
cycle. This proves the stated exclusion with no imported
period or convergence bound and no EXT-1 input.

## Certificates

Run from the repository root:

```
python3 areas/cycles/results/one-defect-first-block-mersenne-exclusion/check_one_defect.py
python3 -O areas/cycles/results/one-defect-first-block-mersenne-exclusion/check_one_defect.py
```

The [certificate](check_one_defect.py) checks the exact
one-defect intercept and finite integer-prefix identities,
including first and last defects and even ordinary terminal
states. Those prefix checks are not claimed to be complete
signed joins. It separately replays five genuine signed
joins, their complete reduced `3x+q` cycles, and the eleven
standard `3x+5,7,13,61` fixtures. It also checks the rational
constants, all `2^20-1` logarithm intervals, 431 finite gap
comparisons, and every odd seed below `2^17`.

Its deterministic output must equal the
[generated receipt](check_one_defect.json); `--write-receipt`
regenerates that receipt. All checks remain active under
`python3 -O`.

## Remarks

The genuine control `r=3,J=5,h=1,A=(2,1,1),B=(6)` has
interface 11 and canonical normalized state `1/41`; its
reduced cycle has addend 41. The control
`r=6,J=7,h=1,A=(2),B=(2,8)` has interface 15 and normalized
state `1/4069`. Both meet the word-shape and endpoint
conditions and retain denominator greater than one.

The new integrality use is `x+1=2^(u+1)t` with integer
`t>=1`, and the exact binary valuation at the ordinary even
terminal output. These statements cannot be applied to a
normalized rational cycle by treating `x` as an odd integer.
The proof also uses the minimum-35 product bound only for
`3x+1`. Thus it preserves the nontrivial `3x+q` controls.

This result restricts one segment of a two-level signed join;
it does not bound the total number of exceptional letters in
the full cycle. In particular the global
[mechanical-edit](../mechanical-edit-denominator-law/README.md)
and [expanding-background](../expanding-background-defect-growth/README.md)
results do not directly supply this arbitrary-`B` conclusion.
The proof refines the earlier positive-interface argument by
retaining the excess `E_B` and cancelling the single defect's
amplitude. Novelty is undetermined.

## History

- 2026-11-08: derived the one-defect first-segment bound and
  amplitude cancellation; recorded the terminal parity correction
  and the LMN-only local closure. Same-session algebra audits are
  not an independent-session review or a formalisation.
