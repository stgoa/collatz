# C011 — Minimal rotational defects allow arbitrarily large cancellation

**Status: written exact counterfamily and elementary arithmetic proof.**
This note uses positive raw odd-only cycles, with no absorbing state.
The family consists of primitive positive rational `3x+1` cycles and
their reduced integer `3x+q` realizations. No denominator-one cycle is
produced, and no new unrestricted cycle exclusion or novelty is claimed.

## 1. Two unit mismatches already allow unbounded gcd

For each integer `t>=1`, take the positive valuation word

```text
w_t = 1^t 2^(2t),
m=3t,  A=5t,
D_t=2^(5t)-3^(3t)=32^t-27^t>0.
```

The symbols are valuations, so `2^(2t)` in the displayed *word*
means `2t` repetitions of the symbol 2. Against its left rotation
by one letter, the word differs at exactly two cyclic positions:
`t-1` and `3t-1`. The differences are `-1,+1`, respectively.
Thus the Hamming defect count is two, the maximum amplitude is one,
and the sum of absolute amplitudes is two. The shift is one and is
coprime to the period.

These defect sizes are minimal for a nonconstant word: a nonzero
rotation difference cannot have just one nonzero coordinate because
its coordinates sum to zero. The word is primitive, since it has
exactly one cyclic transition `1->2`; a nontrivial repeated word
would repeat that transition at least twice.

Composing the two constant-valuation blocks gives the exact intercept

```text
C_t=3^(3t)-2^(t+1)3^(2t)+2^(5t).
```

For example, the first block sends `x` to
`(3^t x+3^t-2^t)/2^t`, while the second sends `y` to
`(3^(2t)y+4^(2t)-3^(2t))/4^(2t)`. Their composition has
fixed point `x_t=C_t/D_t` and the stated intercept.

**Exact cancellation theorem.** Writing `g_t=gcd(C_t,D_t)`,

```text
g_t = gcd(2^(2t)-1, 3^t-2^t).                    (1)
```

**Proof.** Set `x=2^t` and `y=3^t`. Then
`D=x^5-y^3`, `C=y^3-2xy^2+x^5`, and
`C-D=2y^2(y-x)`. Since `gcd(D,2y)=1`,

```text
gcd(C,D)=gcd(D,y-x)
        =gcd(x^3(x^2-1),y-x)
        =gcd(x^2-1,y-x).
```

The final equality uses `gcd(x,y-x)=1`. This proves (1). QED.

## 2. Every supported modulus occurs as a cancellation divisor

For every positive integer `M` coprime to 6, some member of this
fixed-defect family has `M|g_t`. For `M>1`, take `t=phi(M)`,
where `phi(M)` is the number of units modulo `M`. Multiplication
by either 2 or 3 permutes those units. Multiplying the congruences
over that finite set and cancelling their unit product proves

```text
2^t = 3^t = 1 mod M.
```

Both entries of the gcd in (1) are therefore divisible by `M`.
For `M=1`, any `t` works. This is an elementary proof of the finite
unit-period fact used here; no analytic or external theorem is imported.

In particular, a prescribed product of arbitrarily many distinct
supported primes, with arbitrary prescribed powers, divides the
cancellation of some primitive word having just two unit defects.
The period and spacing of the defects grow. This is not a claim of
exponential gcd growth in the period.

An explicit fixed-prime subsequence is

```text
t_k=4*5^k,  k>=0,
v_5(g_(t_k))=k+1.                               (2)
```

Indeed, `v_5(2^8-1)=v_5(3^4-2^4)=1`. If positive integers
`X,Y` satisfy `5` not dividing `XY` and `v_5(X-Y)=a>=1`, the
binomial expansion of `X^5-Y^5` has first term of valuation `a+1`
and every remaining term of valuation at least `a+2`. Thus its
valuation is `a+1`. Iterating this elementary fact in both entries
of (1) proves (2). Other prime factors can also occur.

## 3. These are genuine reduced positive cycles

All letters are positive, and `D_t>0`, so the standard rotated
intercept construction supplies positive odd rational states. Each
rotated intercept and `D_t` is odd, and their common gcd is `g_t`.
Therefore

```text
q_t=D_t/g_t,
n_i=C_(i)/g_t
```

are positive odd integers satisfying every exact prescribed arrow
`3n_i+q_t=2^a_i n_(i+1)`. The odd successors make all valuations
exact. Reduction gives `gcd(n_0,q_t)=1`; any common factor of all
numerators would also divide `q_t`, so the numerator realization has
no remaining common scale. A repeated state would force a shorter
valuation period by deterministic exact arrows, contradicting the
primitive word argument. Thus the raw cycle has exactly `3t` states.

The minimum occurs before the first `1` block, and every rational
state exceeds one. Indeed,

```text
C_t-D_t=2*3^(2t)(3^t-2^t)>0.
```

Starting at `x_t>1`, the map `(3x+1)/2` strictly increases, and
`(3x+1)/4=1+(3/4)(x-1)` strictly decreases while remaining above
one. The latter block returns to the starting value. Hence
`min n_i=C_t/g_t>q_t`; this counterfamily even satisfies the domain
condition `q<=L`. Circular normalized successor order is **not**
asserted or required for the cancellation obstruction.

There is no denominator-one ambiguity. Formula (1) gives

```text
q_t >= (32^t-27^t)/(4^t-1) > 1.                 (3)
```

For the last inequality,
`32^t-27^t >= 5*27^(t-1) > 4^t > 4^t-1`.
Thus the reduced denominators grow, despite the arbitrarily large
cancellation. The family does not refute an estimate on `g_t/D_t`
or a denominator lower bound that retains the period and arc lengths.

## 4. Even bounded rotation-prefix discrepancy is insufficient

Let `a` be the word and `b_i=a_(i+1 mod m)` its left rotation.
For `0<=j<=m`, the prefix difference telescopes:

```text
sum_(i<j)(a_i-b_i)=a_0-a_j,
```

where `a_m=a_0`. Its values are only 0 and -1, independent of `t`.
Consequently all of the following stay bounded simultaneously:

| Quantity | Value on `w_t` |
| --- | --- |
| Rotation distance | 1 |
| Hamming mismatch count | 2 |
| Maximum mismatch amplitude | 1 |
| Sum of absolute mismatch amplitudes | 2 |
| Maximum absolute rotation-prefix difference | 1 |
| Valuation alphabet | `{1,2}` |
| Mean valuation | `5/3` |

In contrast, the two cyclic distances between the defects are `t`
and `2t`; their shortest containing cyclic arc has length `t`.
The primitive period is `3t`, the total exponent is `5t`, and the
discrepancy of a prefix from the mean valuation has maximum magnitude
`2t/3`. Prefix comparison with a rotation must therefore be distinguished
from discrepancy against a linear mean or from a bound on the defect
separation.

The sparse letter difference is not a sparse intercept difference.
If `C'_t` denotes the intercept of the left rotation, then

```text
2 C'_t = 3 C_t + D_t,
C'_t-C_t = 2^t(4^(2t)-3^(2t)).                  (4)
```

In the intercept sum, all `2t` positions of the `2` block change
their prefix exponent, producing that long geometric sum. The two
letter defects bound a long plateau of nonzero prefix difference.
Furthermore,

```text
gcd(D_t,C'_t-C_t)=g_t.                          (5)
```

This follows from (4), or from multiplying the difference by two and
using `gcd(D_t,2)=1`. Thus the example does not exploit an extra
rotation-cut factor: the one-step multiplier defect is `2-3=-1`.

## 5. Relation to the persisted programme and scope

This is a special case of the two-block setup in
[C002](../C002/INDEPENDENT_SLOPES.md), with fixed blocks `u=(1)`
and `v=(2)`, repetition counts `t,2t`, and determinant `K=-2`.
Both repetition counts grow. It is therefore not covered by C001's
constant bound for `u^k v` with the second block fixed. The `u`
block is expanding, but the full word has positive `D_t`.

C002's imported unequal-slope result implies subexponential cancellation
in `t` for these fixed blocks. Nothing here contradicts that result;
the arithmetic construction allows every prescribed finite modulus at
a suitably growing period. The exact identity (1) and this counterfamily
need no imported analytic theorem. The explicit bound (3) is reported
as a check on the obstruction's scope, not as a new general cycle theorem
or a novelty claim. Published cycle records are not improved here.

For example, exact computations give

| `t` | `m` | `g_t` | `q_t` when short |
| --- | --- | --- | --- |
| 1 | 3 | 1 | 5 |
| 2 | 6 | 5 | 59 |
| 3 | 9 | 1 | 13085 |
| 4 | 12 | 5 | 103427 |
| 6 | 18 | 35 | — |
| 12 | 36 | 455 | — |
| 20 | 60 | 275 | — |
| 24 | 72 | 44135 | — |
| 100 | 300 | 138875 | — |

At `t=1`, the raw `q=5` realization is `23->37->29->23`.
At `t=2`, the raw `q=59` realization is
`221->361->571->443->347->275->221`. These are constructed
actual generalized cycles, not conjectural positive integer `q=1`
cycles or claims of new census discoveries. Existing `d=5,7,13`
controls must separately be retained by the batch checker.

## 6. Decision in seven fields

| Field | Outcome |
| --- | --- |
| Objects | Primitive positive valuation words and their one-letter cyclic rotation differences, with exact cycle cancellation gcd. |
| Structural gain | Exact formula (1) and arbitrary prescribed cancellation divisors despite the minimum possible nonzero rotational defect count and amplitude. |
| Translated unresolved gap | A useful sparse-defect estimate must retain arithmetic or geometry of the long arcs, or bound cancellation relative to `D`, rather than count local mismatches alone. |
| Worked example | `t=12` has only two unit letter defects but cancellation `g=455`; (2) supplies unbounded exact powers of five. |
| Known-cycle controls | The constructed reduced cycles are positive, primitive, raw and exact; `t=1` is a genuine `3x+5` control. No statement excludes actual generalized cycles. |
| Cheapest meaningful next test | Derive the two-arc arithmetic identity with both long-block factors retained; compare a denominator bound against this fixed-unit-defect family. |
| Genuinely intermediate milestone | An intrinsic denominator restriction for unrestricted words under a genuinely restrictive defect condition, with a bound uniform in their period. It remains open here. |
