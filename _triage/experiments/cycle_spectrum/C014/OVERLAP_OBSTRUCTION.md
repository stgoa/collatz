# C014 — All rotated residual resultants have the same odd obstruction

**Status: written elementary identity and exact infinite obstruction to a
resultant-size estimate.** No unrestricted denominator bound or cycle
exclusion is proved. The family below consists of primitive positive raw
odd-only cycles at their true reduced parameters. It does not disprove a
bound on those denominators. No novelty or formal-verification claim is
made.

## 1. Intrinsic whole-word polynomials

For a positive valuation word `w=(a_0,...,a_(m-1))`, define

```text
A=sum a_i,       P_j=sum_(i<j) a_i,
P_w(X)=sum_(j=0)^(m-1) 2^P_j X^(m-1-j),
Q(X)=X^m-2^A.
```

At X=3, `C_w=P_w(3)` and `D=-Q(3)=2^A-3^m`. For D>0 the
reduced rational-cycle denominator is `q=D/gcd(C_w,D)`. This is the
empty-background specialization of C013's exact polynomial construction.

Let G be the monic polynomial gcd of P_w,Q, and set

```text
Pbar_w=P_w/G,      Qbar=Q/G,      e=deg Qbar,
R_w=Res(Pbar_w,Qbar) != 0.
```

All polynomials are monic with integer coefficients. For a nonzero
integer z, write `z_(6)` for its positive part coprime to 6, obtained by
removing every factor of 2 and 3 from |z|.

## 2. Exact invariance under every cyclic cut

Let `Rw=(a_1,...,a_(m-1),a_0)` denote the one-position cyclic rotation.
The prefix coefficients give the polynomial identity

```text
2^a_0 P_(Rw)(X)=X P_w(X)-Q(X).                   (1)
```

Q has no zero root. Therefore P_w and P_(Rw) vanish at exactly the
same roots of Q. Since Q is squarefree, their monic gcd with Q is
the same G. Cancelling G in (1) yields

```text
2^a_0 Pbar_(Rw)=X Pbar_w-Qbar.                   (2)
```

Evaluate at each of the e roots of Qbar and take products. The monic
resultant formula gives

```text
2^(a_0 e) |R_(Rw)| = |Qbar(0)| |R_w|.            (3)
```

Since `G(0)*Qbar(0)=-2^A`, the nonzero integer `Qbar(0)` is a signed
power of 2. Consequently

```text
(R_(Rw))_(6)=(R_w)_(6).                         (4)
```

The same equality holds after any number of rotations. In particular,
collecting the residual resultants at every cut and taking their gcd,
after removing 2 and 3, produces exactly the same integer as one cut.
This is true for every positive word, with no mismatch-count or
primitivity hypothesis. It does not depend on a fixed block pattern.

Equation (4) concerns these scalar residual resultants. It does not
identify all cut polynomials, their Bezout coefficients or their
evaluated congruences; those retain information which a scalar
resultant can discard.

## 3. A fixed-distance family with quadratic residual-resultant height

Let t be any positive multiple of 6 and put

```text
ell=2t+1,
w_t=1^t 2^ell,
m=3t+1,       A=5t+2.
```

Here powers of valuation symbols denote repetition. These words satisfy

```text
2^A/3^m=(4/3)(32/27)^t>1,
A<2m,
3A-5m=1.
```

Thus D>0 and gcd(A,m)=1. A proper repeated word would give a common
divisor of A,m, so w_t is primitive. Rotation by one changes exactly
the two run boundaries; a nonzero rotation distance cannot be one
because the letter totals agree. Therefore the minimum nonzero
rotation distance is exactly two.

Each word realizes a primitive positive odd integer cycle at its
reduced q by dividing its rotated intercepts by their common gcd with
D. This construction does not claim q=1. It lies inside C011's existing
two-defect exclusion, which must continue to handle it correctly.

Because gcd(A,m)=1, Q is irreducible over the rationals, and hence
G=1 and e=m. To recall the elementary argument, a monic integer
factor of degree j would have nonzero constant term of absolute value
`2^(Aj/m)`, since every root has modulus `2^(A/m)`. Integrality forces
m to divide j. Gauss's lemma rules out a proper rational factor.
There is therefore no systematic polynomial factor left to remove.

### Exact resultant calculation

First take a general two-run word `1^a 2^b`, with a,b positive and
gcd(a,b)=1. Write m=a+b, A=a+2b. Summing the two geometric strings
in P gives the exact identity

```text
(X-2)(X-4)P(X)
  =(X-4)Q(X)+2^(a+1)(X^b-4^b).                 (5)
```

For roots beta of Q, multiplication of (5) gives

```text
|Res(P,Q)| |Q(2)Q(4)|
 =2^[(a+1)m] * |product_(Q(beta)=0)(beta^b-4^b)|.
```

The b-th powers of the m-th roots of unity are a permutation because
gcd(b,m)=1. It follows that the last product in absolute value is

```text
|(2^A)^b-(4^b)^m|=2^(Ab)(2^(ab)-1).
```

Also `|Q(2)|=2^m(2^b-1)` and
`|Q(4)|=2^A(2^a-1)`. Consequently

```text
|Res(P,Q)|
 =2^[a m+A(b-1)] * (2^(ab)-1)/[(2^a-1)(2^b-1)]. (6)
```

For a=t, b=ell=2t+1 this becomes

```text
|R_(w_t)|=2^(13t^2+5t) S_t,
S_t=(2^[t(2t+1)]-1)/[(2^t-1)(2^(2t+1)-1)].      (7)
```

The two denominator factors in S_t are coprime, since
gcd(t,2t+1)=1; both divide its numerator. Thus S_t is a positive odd
integer. It is also coprime to 3 when t is a multiple of 6.

For the last assertion, the elementary identity
`v_3(4^N-1)=1+v_3(N)` follows by first treating 3 not dividing N
with a geometric sum, then repeatedly factoring `x^3-1`; for
x=1 mod 3, the factor `x^2+x+1` has valuation exactly one.
Since ell is odd and ell=1 mod 3,

```text
v_3(2^(t ell)-1)=1+v_3(t/2),
v_3(2^t-1)=1+v_3(t/2),
v_3(2^ell-1)=0.
```

They cancel in the quotient. Therefore the exact residual part
coprime to 6 is

```text
(R_(w_t))_(6)=S_t.                              (8)
```

### Explicit growth and vacuity of the size bound

The numerator in S_t is greater than `2^[t(2t+1)-1]`, and the
product in its denominator is less than `2^(3t+1)`. Thus

```text
S_t > 2^(2t^2-2t-2),       D<2^(5t+2),
S_t/D > 2^(2t^2-7t-4)>1       for t>=6.          (9)
```

In particular `log S_t=Theta(t^2)=Theta(m^2)`, whereas
`log D=Theta(t)=Theta(m)`. For every fixed real K>0, eventually
`S_t>D^K` along these multiples of 6. The residual resultant height
cannot satisfy a bound `log((R_w)_(6))=O_s(m)` based only on a fixed
nonzero rotation distance s, even after all polynomial common factors
and all powers of 2 and 3 have been removed.

Here E=1 and G=1. The generic resultant-size bound is

```text
q >= D/(R_w)_(6)=D/S_t<1.                       (10)
```

It supplies no nontrivial denominator gain. By (4), using the size of
the gcd of all rotated residual resultants gives precisely the same
vacuous bound. This identifies the lost information exactly; it does
not rely on the weaker observation that a displayed coefficient bound
happens to be large.

## 4. Scope: exact modular use can still help

For this G=1 family, the implication
`gcd(C,D) divides (R_w)_(6)` remains valid. It also gives the
potentially stronger bound

```text
q >= D/gcd(D,(R_w)_(6)).                         (11)
```

The family does not refute useful estimates or exact calculations of
this last gcd. For example, direct exact evaluation gives actual
`gcd(C,D)=1` and `gcd(D,S_t)=1` at t=6,12,18,24. Equation (11) then
recovers q=D, even though (10) is vacuous. At t=3, outside the chosen
6-divisible subsequence, the actual cancellation is one but the gcd
of D with the resultant part coprime to 6 is seven. Thus the scalar
resultant can also introduce extra numerical possibilities.

These finite values are calibrations, not an assertion that the two
gcds agree or remain one throughout the infinite family. The exact
identity at X=3 obtained from (5) is

```text
C=2^(t+1)(4^ell-3^ell)-D,
gcd(C,D)=gcd(3^t-2^t,4^ell-3^ell)
        =gcd(3^t-2^t,4^(t+1)-3).
```

It provides a short independent calculation of the stated controls.
In particular it retains the two arc quantities that the single
resultant-size estimate had replaced by a much larger integer.

The extra factor seven at t=3 has an exact explanation. Here

```text
m=10, A=17, D=72023, C=P(3)=155129,
(R_w)_(6)=2359=7*337,
Q(3)=0 mod 7,       P(3)=2 mod 7,
Q(4)=0 mod 7,       P(4)=0 mod 7.
```

The common root detected by the resultant modulo seven is 4, while
the cycle numerator evaluates P at 3. The two residues are distinct.
Thus seven divides both D and the residual resultant without dividing
the actual cycle numerator. The polynomial gcd over the rationals
is still one. This is information lost by eliminating the evaluation
point, rather than merely an overestimate of an integer's size.

Numerical cancellation requires the specific root 3 of Q modulo each
prime dividing D. A scalar resultant can instead vanish because P
vanishes at another root of Q. Retaining that distinguished evaluation
point is therefore a concrete remaining obligation for an intrinsic
overlap method; (4) shows that adding more rotated scalar resultants
does not recover it.

The conclusion is limited to a proposed compression: intrinsic
whole-word polynomial gcd removal, scalar residual resultants at all
cyclic cuts, and a bound using their sizes. C011's arc-aware method
still applies. Coupled congruences, actual overlap relations, and
arithmetic control of `gcd(D,R_(6))`, with its distinguished root
X=3 retained, are not ruled out.

## 5. Candidate ledger and decision

1. **Objects:** intrinsic P_w,Q, their monic common factor G, all
   rotated residual resultants, and the exact reduced denominator.
2. **Structural gain:** the residual resultant part coprime to 6 is
   exactly invariant under every cyclic cut; an explicit primitive
   fixed-distance family has quadratic remaining resultant height.
3. **Translated unresolved gap:** a useful numerical bound needs
   arithmetic about its intersection with D, or relations discarded
   by the scalar resultant. It cannot charge the residual resultant
   by a linear-in-period cost at fixed mismatch count.
4. **Worked example:** w_t with t=6 has m=19, A=32, polynomial gcd
   one, residual resultant part S_t of 60 bits, and D of 32 bits.
5. **Known-cycle controls:** the identities apply to every raw cycle,
   including the existing q5/7/13 controls and nontrivial polynomial
   gcds. Repeated `(2)` is not excluded. The new family is already
   within C011, whose stronger arithmetic exclusion is preserved.
6. **Cheapest meaningful next test:** exact small resultant formulas,
   the general rotation identity, and evaluation of actual numerator
   gcd versus `gcd(D,R_(6))`, without a new cycle census.
7. **Intermediate milestone:** a uniform estimate of the evaluated
   intersection with D that uses actual shared arcs, or an overlap
   elimination retaining more than scalar resultants. No such general
   estimate is established here.

This is an obstruction to a particular proposed extension of C013,
not a new fixed-pattern cycle theorem or an impossibility claim about
all resultant methods. It improves no published cycle exclusion
record; the comparison is that C011 already handles this calibration
class while the proposed intrinsic size reduction does not.
