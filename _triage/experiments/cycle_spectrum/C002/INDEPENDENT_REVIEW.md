# C002 — Independent review of the proportional-slope argument

**Status: written mathematical review, 2026-10-19.** This records only the
independent literature lane's checks. It is separate from the root review,
the finite-data checks, and any external formal verification. No novelty
assessment is supplied.

Reviewed sources: [PROPORTIONAL.md](PROPORTIONAL.md), including the saved
uniform equal-total corollary, repaired sharp-example calculation and
reduced-slope normalization, and
[R71's mechanical-family proof](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md).
The unequal-slope note was authored by this reviewer and is **not** presented
as independently reviewed here.

## 1. Two issues found and corrected

1. The first version of the sharp example removed the factor 7 from
   `7(A+B)` before proving the common divisor coprime to 7. The repair
   uses `A=16^t=B=9^t mod 7`, so `11A+5B=2B!=0 mod 7`. The common
   divisor then divides A+B, and the rest of the gcd argument is valid.
   The denominator formula itself was correct.
2. Section 2 requires a reduced slope `(a,b)`, but the first version of
   the examples used full block totals directly. The repaired sharp
   example uses `(a,b)=(2,1), r=s=2`; the rotating family explicitly
   uses `c_0=gcd(A,m)` and translates the reduced exponents back to the
   full block powers. This matters when A and m are not coprime.

Both repairs were read in the saved source. No remaining error was found
in the proportional theorem or rotating-family proof.

## 2. Cancellation and the finite rectangle

I independently expanded both identities

```
D_u*C-C_u*D=Q^k*G_v(ell)*K,
D_v*C-C_v*D=-R^ell*G_u(k)*K.
```

The sign in the second identity and the chronological concatenation
order are correct. D is prime to 6, so the gcd g can be canceled past
Q^k and R^ell. Consequently

```
g divides K*gcd(G_u(k),G_v(ell)).
```

This is a divisibility bound, not an equality, and remains valid with
shared primes in D_u,D_v.

For proportional slopes, the proof correctly reduces
`gcd(U^i-V^i,U^j-V^j)` by Euclid's algorithm, using `gcd(U,V)=1`.
The common divisor E of the two block differences is removed before
bounding the geometric-sum gcd. Thus `g divides J_0*H_h`; removing the
2- and 3-primary factors of J is valid because both g and H_h are
prime to 6.

Since h divides L and L>=2h, the quotient H_L/H_h contains at least
two positive terms. This proves the strict lower bound
`den>U^(L-h)/J_0`, and hence the stated finite rectangle. The argument
works for unequal block lengths r and s. If U<V, the entire positive
domain is empty; no individual positive-cycle case was discarded.

## 3. Sharpness and the zero-commutator exception

For u=(1,3), v=(3,1), I checked the values
`C_u=5, C_v=11, D_u=D_v=7, K=42, J_0=1` and the repaired gcd proof.
It gives exactly

```
den(u^t v^t)=7*(16^t+9^t).
```

With the corrected reduced notation, L=4t and U=4; the denominator
has order `U^(L/2)`. A larger exponent cannot hold uniformly for the
whole class. The unique cyclic factor (3,3) also proves primitivity
for every positive t, so the sharpness does not come merely from
displaying a shorter cycle repeatedly.

When K=0, positivity makes the two block fixed points positive and
equal. Exact deterministic valuations imply that both blocks repeat
one primitive word in the same phase. Their combined denominator can
therefore stay constant. The examples with denominators 5,7,13 are
correct raw rational-cycle controls. The raw fixed point 1, obtained
from the valuation word (2), is another necessary exception. This
argument does not classify or exclude a hypothetical nontrivial
integer cycle hidden in the common-word case.

## 4. Rotating mechanical blocks, with both repetitions free

The bounds `3/2<A/m<5/3` are valid for every m>=13. Floor differences
then give the stated initial and final letters. For the cyclic
mechanical word, every length-two valuation sum is at least 3 and
every length-three sum at most 5. Hence it has neither (1,1) nor
(2,2,2).

For its left rotation, I checked the phase relation
`x_v=(3*x_u+1)/2` and `x_u<x_v<2*x_u`, using `x_u>m/6>1`.
Solving the two return equations gives the displayed formula for x.
Both block multipliers are strictly between 0 and 1, so every block
start lies strictly between x_u and x_v. A u-prefix therefore exceeds
its pure-cycle value. A v-prefix starts above `x_v/2`, and its positive
slope and nonnegative intercept preserve the factor-one-half lower
bound. Every odd rational state is consequently greater than m/12
for all k,ell>=1; no omitted separation hypothesis is required.

The rotation identity gives `J=(C_u+Delta)/2`. The term-by-term bound
`C_u<(2m/3)*3^m` and `Delta<C_u` give the stated denominator estimate.
For k+ell>=3 its lower bound tends to infinity with m, uniformly over
the two repetition counts.

There is exactly one new cyclic (2,2,2), at the u-to-v boundary, and
exactly one cyclic (1,1), at the v-to-u boundary. Same-block joins
create neither. The unique triple proves primitivity. The length-three
valuation factors with sums 4 and 6 prove failure of mechanical balance;
the shortcut factors 11011 and 01010 separately prove failure of
Christoffel balance in that clock.

Every state exceeds 1, so valuation 1 increases and valuation 2
decreases the odd-only state. The sole pair of adjacent 1s merges two
increasing runs. Thus the odd-only local-minimum count is
`(k+ell)*(2m-A)-1`. The shortcut count is `(k+ell)*(A-m)`, one for each
valuation-2 block. These formulas retain different clocks.

## 5. Independently checked strengthening for arbitrary equal-total blocks

The root proposed the following strengthening during review. I independently
checked the argument and then inspected its finalized statement and proof,
saved under Section 2's **Uniform equal-total corollary**. No issue was found
in that statement or in its bounded-denominator conclusion.

Let u,v be distinct positive valuation words of the same length m and
sum A, with U=2^A>V=3^m. Put `n=k+ell`, `h=gcd(k,ell)`, and assume
k,ell>=1 and n>=3. Equal totals make `J=C_v-C_u`. If J=0, the words
would have the same positive rational fixed point and exactly the same
return length; determinism would give u=v. Thus J!=0.

For **any** positive valuation word z with these totals, each prefix
sum obeys `A_j<=A-(m-j)`. Summing the resulting geometric bound gives

```
C_z <= 2^(A-m) * sum_(j=0)^(m-1) 3^(m-1-j)*2^j
    = 2^(A-m)*(3^m-2^m)
    = U*(V/2^m-1).
```

Both intercepts are positive, so

```
0<|J|<U*(V/2^m-1)<U*V/2^m.
```

The proportional theorem and `n-h>=2` yield the uniform bound

```
den(u^k v^ell) > U^(n-h)/|J|
               >= U^2/|J|
               > 2^m*U/V
               > 2^m.                                  (R)
```

This proof allows u,v,A,m to vary. In particular, `den<=d_0` forces

```
m<log_2(d_0),
2^A<d_0*3^m/2^m.
```

Thus m and A are explicitly bounded. There are only finitely many
positive valuation words at any permitted (A,m); for each remaining
distinct pair, the proportional theorem bounds k and ell. This proves
uniform, effective finiteness of the whole equal-total, distinct-block,
n>=3 class in every bounded denominator layer. It is stronger than
finiteness for an already fixed block pair.

An exact enumeration can use `2^m<d_0` and `2^(A+m)<d_0*3^m`, avoiding
rounding issues in logarithmic bounds, followed by the exact finite
rectangle for each surviving pair. No such enumeration was performed
as part of this review.

The hypotheses are material. Equal totals and n>=3 were used directly.
The same-word case J=0 retains actual cycle repetitions. This result
supplies neither a uniform theorem for arbitrary proportional blocks
of different totals nor a classification of arbitrary cycle words.

## 6. Review scope

The review checked the written equations, all exponent domains, positivity,
normalization, strict inequalities, clock conventions and the named cycle
exceptions. It found and documented two repairable proof-text issues.
It did not execute the author's finite checker, certify its stored data,
run a formal proof assistant, or search for priority. Those activities
must be reported separately if performed elsewhere.

The meaningful gain is a proved restriction on denominator layers with
stated word structure. Increasing a fixed catalogue is not, by itself,
an extension of these quantifiers to arbitrary words.
