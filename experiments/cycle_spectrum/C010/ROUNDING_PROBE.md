# C010 — Exact lowbit constraints after global gap integrality

**Status: written elementary equivalence and exact relaxation control.**
The raw positive odd-only clock has no absorber. This note does not exclude
any new denominator-one cycle. It independently audits the dyadic seam and
identifies exactly when the proposed lowbit/rounding condition supplies an
additional obligation.

## 1. The seam in C006 is correct

Let the sorted normalized states be `z_0<...<z_(m-1)<2z_0`, and
let their sorted height labels be `H_j`. Set `B=max H_j`,

```text
Z_j=2^B z_j,
U_j=2^(B-H_j),
G_j=Z_(j+1)-Z_j.
```

Use the extensions `Z_(j+m)=2Z_j`, `U_(j+m)=2U_j`, and therefore
`G_(j+m)=2G_j`. In particular the seam is
`G_(m-1)=2Z_0-Z_(m-1)` and `U_m=2U_0`; it is not a periodic seam.
For normalized rank shift `+s mod m`, the exact equations are

```text
2Z_(j+s)=3Z_j+qU_j,
2G_(j+s)=3G_j+q(U_(j+1)-U_j).
```

Consequently the finite-index equation is precisely C006 (G3):

```text
2^(1+1_{j>=m-s}) G_((j+s) mod m)
  = 3G_j+q(U_(j+1)-U_j).
```

The wrap coefficient depends on `j+s>=m`, including the equality
case. The final forcing is `q(2U_0-U_(m-1))`. No seam correction to
the historical C006 theorem is needed.

## 2. Integer gaps retain the whole state lattice

This is an independent derivation of the global gap change of coordinates.
Write `E` for the integer shift operator
`(EZ)_j=Z_(j+1)` with its final entry `2Z_0`. Then

```text
E^m=2I,
G=(E-I)Z,
(E-I)^(-1)=I+E+...+E^(m-1).
```

Thus `E-I` is unimodular. Explicitly,

```text
Z_0=sum_(j=0)^(m-1) G_j,
Z_j=sum_(k=0)^(m-1) G_k + sum_(k=0)^(j-1) G_k.
```

The two coordinate systems have exactly the same common reduced
denominator: each is an integer linear combination of the other.
Since `E-I` commutes with `2E^s-3I`, passing from the state equations
to all gap equations is an invertible integer operation. It can expose
positivity and local divisibility, but creates no second integrality
obstruction. Individual linear combinations may cancel more denominator
factors; using the complete collection recovers the original denominator.

## 3. Under legal positive valuations, lowbits are automatic

Assume `q` is a positive odd integer and `m>1`. Prescribe sorted nonnegative
height labels with `H_0=0`, and a single-cycle rank shift `1<=s<m`
with `gcd(s,m)=1`. On an arrow
from rank `j` to `k=(j+s) mod m`, put

```text
c_j=1+1_{j>=m-s},
a_j=c_j+H_j-H_k.
```

Suppose **every** `a_j>=1`, the total `D=2^A-3^m` is positive,
and the rational solution of the full gap system has all `G_j>0`.
The reconstruction above supplies
`0<Z_0<...<Z_(m-1)<2Z_0`. Define `n_j=Z_j/2^(B-H_j)`.
Multiplying each normalized arrow by the appropriate power of two
gives exactly

```text
3n_j+q=2^a_j n_k.
```

For the valuation word in chronological order, each rotated intercept
`C_(i)` is odd: its first summand is an odd power of three and every
later summand contains a positive power of two. Also `D` is odd.
The unique closed solution is therefore

```text
n_(i)=q C_(i)/D.
```

Now suppose the gap solution is integral. By Section 2 all `Z_j`
are integral. Because the denominators of the `n_j` are odd, multiplying
them by a power of two cannot remove any denominator. Thus every `n_j`
is an integer. It is an odd integer, since `q C_(i)` and `D` are odd.
It follows automatically that

```text
lowbit(Z_j)=2^(B-H_j)=U_j.
```

Equivalently, the complete family of partial-sum congruences is automatic:

```text
sum_k G_k + sum_(k<j) G_k = 2^(B-H_j) mod 2^(B-H_j+1).
```

In particular `v_2(sum_k G_k)=B`. These are exact binary carry
conditions, but the proof shows they follow from the full legal integral
system; imposing them again cannot create an extra denominator filter.

All valuations are exact, because the next odd state is odd. Moreover,
with `L=n_0=Z_0/2^B`, the inequalities for `Z_j` give
`2^H_j <= n_j/L < 2^(H_j+1)`, so these are the actual dyadic
heights and `L` is the actual minimum. Distinct normalized states
cannot give equal odd states: equal states have the same actual height.
Hence this construction gives a genuine simple raw odd cycle. The
parameter `q` in this construction need not be reduced: its actual
common rational denominator is still `D/gcd(C_(0),D)` after dividing
the raw states by `q`. Reduction and any common scaling must be checked
separately.

**Conclusion:** in the declared legal-height domain, positivity and
integrality of the full gap solution already force the exact odd
numerators, lowbit labels, heights, and valuation cylinders. Checking
lowbits remains useful for auditing a proposed profile, but after global
integrality it is not an independent exclusion mechanism. A new global
inequality could still show that no such positive integral solution exists
at `q=1`; this equivalence does not rule out that route.

## 4. Exact control when positive valuation legality is dropped

The familiar formal affine loop at `q=1`,

```text
4 -> 13 -> 5 -> 4,   a=(0,3,2),
```

has actual height list `(0,1,0)` relative to `L=4`, normalized
word `(1,2,2)`, and sorted coordinates

```text
Z=(8,10,13), U=(2,2,1), G=(2,3,3), s=2.
```

It satisfies all full integer gap equations, including the seam:

```text
2*3=3*2+0,
4*2=3*3-1,
4*3=3*3+3.
```

It also satisfies the state equations `2Z_(j+2)=3Z_j+U_j`.
But `lowbit(8)=8`, while its assigned `U_0=2`; the first numerator
is even and its first valuation is zero. Thus positive gaps and
normalized exponents in `{1,2}` do not replace the hypothesis
`a_j>=1`. This is an invalid odd-only loop, not a Collatz cycle.

## 5. Assessment

| Field | Outcome |
| --- | --- |
| Objects | Full sorted gap system, exact dyadic seam, lowbits, and prescribed legal heights. |
| Structural gain | Unimodular gap reconstruction; legal positive valuations make exact lowbits automatic after global gap integrality. |
| Translated unresolved gap | Exclude a positive integral solution for every nontrivial ordered legal `q=1` profile. |
| Worked example | The integral gap vector `(2,3,3)` gives the false affine loop only because a prescribed original valuation is zero. |
| Known-cycle controls | All actual `q=5,7,13` odd cycles satisfy their lowbit identities. The rank-order statements apply only in the ordered `q<=L` domain; raw `(5,11)` at `q=7` is outside that domain. |
| Cheapest meaningful next test | Test a proposed inequality using full profile order and legality; a new parity or lowbit check after the exact global lattice test cannot supply an independent condition. |
| Genuinely intermediate milestone | Exclusion of nontrivial ordered denominator-one cycles at arbitrary period and height remains open. |

No novelty, formal verification, or improvement to published cycle records
is claimed. This is an algebraic completeness result and a scope control,
not an additional cycle exclusion.
