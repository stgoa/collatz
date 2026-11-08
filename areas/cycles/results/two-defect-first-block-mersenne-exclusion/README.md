---
id: two-defect-first-block-mersenne-exclusion
kind: result
title: Two non-one letters in the first low-to-high segment exclude denominator one
status: written
claim: >
  Raw odd-only clock. Let J>r>=1 and h,z be positive odd integers.
  Let nonempty positive words A,B give exact signed paths from -h to z
  under 3x+(2^r-1) and from z to h under 3x+(2^J-1), with last(B)>J.
  Suppose A has at most two letters greater than one, of arbitrary
  sizes and at arbitrary positions. Put u=A[J-r]B[-J], v=AB[r].
  If 2^(sum(A)+sum(B))>3^(len(A)+len(B)), then den(uv)>1 under
  the declared LMN and Chim logarithm bounds and the Barina input
  supporting the replayed odd-period theorem. The proof bounds the
  half-length m=len(A)+len(B) below 22579001791, hence the full odd
  word length 2m below 45158003582, contradicting the replayed lower
  period 72057431991. No primitivity assumption on uv is needed.
  The sizes, positions, levels, endpoints and entire word B are
  unbounded. Other first segments and high-to-low joins are outside
  this claim. The existing one-defect result retains its weaker,
  sole-LMN assumption set.
authors:
  - Codex first-block research lane (GPT-6 Astra; directed by Santiago Armstrong)
  - Codex main research lane (GPT-6 Astra; directed by Santiago Armstrong)
created: 2026-11-08
depends_on: [one-defect-first-block-mersenne-exclusion, cycle-length-lower-bound-from-convergents]
assumes: [laurent-mignotte-nesterenko-1995-two-logarithms, chim-2025-padic-two-logarithms, barina-2025-convergence-2-71]
certificates: [check_two_defects.py]
evidence:
  - "check_two_defects.json: exact two-defect prefixes, terminal reduction, branch bounds, p-adic specialization constants, rational logarithm and convergent bounds, period comparison and actual-cycle controls"
tags: [cycles, mersenne-endpoints, valuation-words, p-adic-logarithms, denominators]
---

# Two non-one letters in the first low-to-high segment exclude denominator one

## Statement

Write `W[d]` for increasing the final letter of a nonempty word
`W` by `d`. Let `J>r>=1`, `M=2^r`, `N=2^J`, and `p=J-r`.
Suppose positive odd integers `h,z` and positive valuation words
`A,B` give exact signed odd-only paths

```
T_(M-1)^A(-h)=z>0,    T_(N-1)^B(z)=h,    last(B)>J.
```

Assume that `A` has at most two letters greater than one. Set

```
a=len(A), b=len(B), P=sum(A), T=sum(B),
m=a+b, S=P+T, D=2^S-3^m>0,
u=A[p]B[-J],    v=AB[r].
```

Then `den(uv)>1`, conditional on the three declared inputs:
[LMN](../../../../sources/laurent-mignotte-nesterenko-1995-two-logarithms.md),
[Chim's p-adic theorem](../../../../sources/chim-2025-padic-two-logarithms.md),
and [Barina's convergence computation](../../../../sources/barina-2025-convergence-2-71.md)
as used by the repository's
[replayed odd-period theorem](../cycle-length-lower-bound-from-convergents/README.md).

The word `uv` has **full odd-only length `2m`**, not `m`.
It may be a repeated traversal: its least period is at most `2m`,
which is sufficient for the final contradiction. Nothing here
asserts that an arbitrary first segment has two defects, that
`B` has few defects, or that the auxiliary signed joins exist at
all parameters.

## Proof

### 1. Retain the first-block and second-block excesses

Suppose `den(uv)=1`. The normal-form correspondence supplies
positive odd integer `3x+1` states and canonical state `x`.
Use the notation and the exact boundary bounds from
[the one-defect proof, section 1](../one-defect-first-block-mersenne-exclusion/README.md):

```
alpha=log_2(3), lambda=3^m/2^S, eta=1-lambda,
G=log_2(1/eta), c_r=log_2(1+1/M)<1,
kappa=(lambda+1/M)/eta, K=kappa+1=2^(G+c_r),
E_A=P-a, E_B=T-J-b>=0.
```

That section does not restrict the number of defects. It proves

```
S<8m/5,      J<3m/5-E_A-E_B,
x<kappa*C_A/3^a,
m+E_B<alpha*a+r+G+c_r.
```

The minimum-35 input is its exact local descent; alternatively
it follows from the stronger declared convergence input here.
The last letter of `v` exceeds `J+r`, so the cycle is not the
fixed-point itinerary. Since `r<J`, the inequalities imply

```
(2/5)m+E_A+2E_B < alpha*a+G+c_r.                      (1)
```

Before the final modified arrow of `A[p]`, the ordinary additive-one
path from `x` follows the actual odd cycle. Its ordinary terminal
output `F_A(x)=2^p Y` is even, with `Y` the actual odd state.
The enclosure `x<kappa*C_A/3^a` remains essential below.

### 2. Exact two-defect coordinates and the terminal reduction

The case of at most one defect is already covered by the
[existing result](../one-defect-first-block-mersenne-exclusion/README.md).
For exactly two, write

```
A=1^(n-1) (e+1) 1^(ell-1) (f+1) 1^w,
n,ell>=1, e,f>=1, w>=0, a=n+ell+w, E_A=e+f.          (2)
```

If `w=0`, replace the terminal letter `f+1` by 1. The ordinary
output is multiplied by `2^f` and is still even. The resulting
prefix has only one non-one letter, the same length, and the
same `C_A/3^a`, because the intercept does not use the final
valuation. The local one-defect estimate in section 2 of the
predecessor proof therefore gives
`a<e/alpha+3G+6<=E_A/alpha+3G+6`. Its cancellation with (1)
gives `m<15G+27`. This uses only that local prefix estimate;
it does not pretend that the altered prefix forms a new signed
join with `B`.

Assume henceforth `w>=1`. Let `y1,y2` be the ordinary states
just after the first and second exceptional arrows. Both are
internal actual odd cycle states. There are positive integers
`t,s` with

```
t0=x+1=2^n*t,       t1=y1+1=2^ell*s,
3^n*t+2^e-1=2^(e+ell)*s,
t2=y2+1=(3^ell*s+2^f-1)/2^f,
v_2(t2)=w,         3^ell*s=2^f*y2+1.                (3)
```

The last valuation identity uses the even ordinary terminal
output, not an assumed odd output. In particular `n<=log_2(t0)`,
`ell<=log_2(t1)` and `w<=log_2(t2)`.

Put `rho=3/2` and

```
U1=2^e*rho^(-n),       U2=2^(e+f)*rho^(-n-ell).
```

Splitting the geometric intercept sum gives

```
C_A/3^a=1+(2^e-1)*rho^(-n)
          +2^e*(2^f-1)*rho^(-n-ell)-2^(e+f)*rho^(-a),
t0 < K*(1+U1+U2).                                    (4)
```

The exact shifted recurrences are

```
t1=1+2^(-e)*(rho^n*t0-1),
t2=1+2^(-f)*(rho^ell*t1-1).                          (5)
```

They imply `t1<=rho^n*t0<=t0^alpha` and
`t2<=rho^ell*t1<=t1^alpha`. These are inequalities for the
integer prefix, not for arbitrary normalized rational states.

### 3. Separate the three possible dominant terms

Choose a largest term among `1,U1,U2`; ties may use any case.

**The term 1 is largest.** Equation (4) gives `t0<3K`.
By (3)--(5),

```
a<(1+alpha+alpha^2)*log_2(3K)<6G+15.
```

Use `alpha<8/5`, `c_r<1` in (1), dropping nonnegative excesses:

```
m<27G+63.                                           (6)
```

**The term U1 is largest.** Equations (4)--(5) give
`t1=t0/U1+1-2^(-e)<3K+1<4K`. Also `t0>=2^n` gives
`alpha*n<e+log_2(3K)`. Consequently

```
a<e/alpha+(1/alpha+1+alpha)*log_2(K)+3+2alpha
 <E_A/alpha+4G+11,
m<19G+47.                                           (7)
```

The last line again follows from (1).

**The term U2 is largest.** Exact composition of (5) yields

```
t2=t0/U2+(1-2^(-e))*U1/U2+1-2^(-f)<3K+2<5K,
35<=y2=t2-1<4K.                                    (8)
```

The lower bound holds because `y2` is an internal state of a
nontrivial integer cycle. From (4) and `t0>=2^n`,

```
alpha*(n+ell)<e+f+ell+log_2(3K).
```

Together with `w<log_2(5K)`, this gives

```
alpha*a<E_A+ell+(1+alpha)*log_2(K)+alpha+alpha*log_2(5)
       <E_A+ell+3G+9,
m<(5/2)*ell+10G+25.                                 (9)
```

Here `alpha<8/5`, `log_2(5)<12/5` and `log_2(K)<G+1`
justify the conservative constants. This retains the extra
`ell`; size estimates alone have not eliminated it.

### 4. The p-adic input controls the remaining run

Equation (3) gives `3^ell | 2^f*y2+1`, so `3` does not divide
`y2`. Apply the precise rational specialization of
[Chim, Theorem 2.1](../../../../sources/chim-2025-padic-two-logarithms.md)
to the two 3-adic units `2` and `-1/y2`, with exponents `f,1`.
Their multiplicative independence follows by taking valuations
at 2 and then absolute values; `y2` is odd and exceeds 1.

Write `L3=ln(3)`. The specialized coefficient is
`13950*(1.5L3+4.85)/L3^2`, which is less than `100000`
because `1<L3<11/10`. The first term of Chim's maximum is

```
ln(f/ln(y2)+1/L3)+ln(L3)
 =ln(1+f*L3/ln(y2))<=ln(f+1).
```

Its other terms are below 1100 and 1287, respectively.
Thus the cited theorem implies

```
ell <= v_3(2^f*y2+1)
    <100000*(ln(f+1)+1300)*ln(y2).                  (10)
```

This is an application of an explicit theorem with variable
height `ln(y2)`, not an assumed uniform p-adic estimate.
From (8), `ln(y2)<(G+3)ln(2)<G+3`. The total budget gives
`f<m`, hence `f+1<=m` and `ln(f+1)<=ln(m)<log_2(m)`.
Equations (6), (7), (9) and (10), including the terminal case,
therefore imply the common bound

```
m < 250000*(log_2(m)+1300)*(G+3)+27G+63.             (11)
```

### 5. An exact finite gap replaces the asymptotic bound

The existing LMN specialization, using `S<8m/5`, gives

```
G<H(m),   H(m)=1+98*max(log_2(m)+2,21)^2.            (12)
```

Suppose `2^j<=m<2^(j+1)`, `j>=48`. Equations (11)--(12)
bound its right side by

```
R(j)=250000*(j+1301)*(4+98*(j+3)^2)
     +27*(1+98*(j+3)^2)+63.
```

At `j=48`, `R(j)=85965706382336<2^48`. The polynomial
`R` has positive coefficients and degree 3, so
`R(j+1)/R(j)<=(49/48)^3<2` for every `j>=48`.
Consequently (11) forces `m<2^48`.

The certificate constructs rational lower and upper bounds
for `ln(2),ln(3)` from 80 terms of the positive atanh series
and its geometric tail. They enclose `alpha` and certify

```
p/q=83130157078217/52449289519716 < alpha
   <p'/q'=683381996816440/431166034846567,
p'q-pq'=1,             q'>2^48,
q*alpha-p>2^-62.                                    (13)
```

No iteration through `2^48` denominators is needed. For any
integers `0<m<q'` and `S-m*alpha>0`, determinant 1 supplies
integers `u,v` with `(m,S)=u(q,p)+v(q',p')`. Write
`e0=q*alpha-p>0`, `e1=p'-q'*alpha>0`. Then
`S-m*alpha=v*e1-u*e0`. If `v<=0`, positivity forces `u<0`,
contradicting `m>0`. Thus `v>=1`; since `m<q'`, it follows
that `u<=-1`. Hence

```
S-m*alpha=|v|*e1+|u|*e0>e0>2^-62.                  (14)
```

This argument does not require `m>=q`.
With `Lambda=S*ln(2)-m*ln(3)` and `ln(2)>1/2`,
`Lambda>2^-63`. The elementary inequality
`eta=1-exp(-Lambda)>min(Lambda/2,1/2)` yields

```
eta>2^-64,      G<64.
```

Insert this and `log_2(m)<48` into (11):

```
m<22579001791,
full odd-word length 2m<45158003582.                 (15)
```

### 6. Compare full odd periods

The [replayed period theorem](../cycle-length-lower-bound-from-convergents/README.md),
using the declared Barina convergence input, says that every
nontrivial positive `3x+1` cycle has at least `72057431991`
odd states in its least period. This is the raw odd-only
clock, not the shortcut or full Collatz clock.

The cycle described by `uv` has least period at most its
full word length `2m`. Equation (15) is strictly below that
lower bound. This contradiction proves `den(uv)>1`.
No primitivity assumption on the constructed word was used.

## Certificates

The standard-library [checker](check_two_defects.py) and its
[generated receipt](check_two_defects.json) replay the finite
arithmetic: exact two-defect integer prefixes and their even
ordinary endpoints, terminal-defect reduction, all three branch
estimates, the rational constants for the Chim specialization,
the logarithm intervals and adjacent-convergent inequalities,
and the final comparison with the existing period receipt.

Genuine signed joins and all eleven standard `3x+5,7,13,61`
controls are replayed separately. Integer-prefix fixtures are
not represented as complete joins. The local `K` threshold
of a prefix is not substituted for the `K` of an unproved `B`.
The checker does not prove either external logarithm theorem
or rerun Barina's convergence computation.

```
python3 areas/cycles/results/two-defect-first-block-mersenne-exclusion/check_two_defects.py
python3 -O areas/cycles/results/two-defect-first-block-mersenne-exclusion/check_two_defects.py
```

Use `--write-receipt` to regenerate the deterministic receipt.

## Remarks

This extends the word-shape coverage of the
[one-defect result](../one-defect-first-block-mersenne-exclusion/README.md)
while keeping that result and its sole-LMN proof unchanged.
The new input is needed only in the second-dominant branch,
where an intermediate run leaves a genuine extra term `ell`.
Its divisibility is controlled by a published p-adic theorem
with the endpoint height retained explicitly.

The minimum and period arguments are specific to integer
`3x+1` cycles. Actual `3x+q` controls retain their addend, so
neither their normalized rational states nor their periods
are incorrectly subjected to the integer-cycle assumptions.
Novelty of this scoped combination is undetermined.

## History

- 2026-11-08: extended the first-segment exclusion to two arbitrary
  exceptional letters, with explicit additional Chim and Barina
  inputs. The full `2m` clock and the ordinary even terminal are
  retained. Same-session scrutiny is not independent review;
  status remains `written`.
