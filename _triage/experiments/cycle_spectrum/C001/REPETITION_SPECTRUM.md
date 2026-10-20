# C001 — Denominator spectrum of a repeated word with one fixed defect

**Status: written proof; root and independent agent review passed.** The results
below concern positive odd rational cycles of the ordinary 3x+1 map in
the odd-only Syracuse clock, using its raw recurrence with no special
absorbing rule at 1. They give a denominator theorem for every
word of the form w = u^k v, where u and v are fixed nonempty positive
valuation words. They do not classify all valuation words or prove the
absence of nontrivial integer cycles.

## 1. Word convention and repetition

For a positive valuation word z = (a_0,...,a_(m-1)), put

    A_j = a_0+...+a_(j-1),  A_0=0,  A=A_m,
    C_z = sum_(j=0)^(m-1) 3^(m-1-j) 2^A_j,
    D_z = 2^A-3^m.

If D_z>0, the fixed point C_z/D_z is positive. All C_z and D_z are
odd, and D_z is prime to 3. The cyclic identities

    3 C_i + D_z = 2^a_i C_(i+1)

prove that the displayed valuations are exact, including after
fraction reduction. Thus the reduced denominator is

    den(z) = D_z / gcd(C_z,D_z),

and it is invariant under cyclic rotation. This is the R71 convention.

For u with Q=2^sum(u), P=3^len(u), D_u=Q-P, define

    G_k = sum_(i=0)^(k-1) Q^(k-1-i) P^i
        = (Q^k-P^k)/(Q-P).

The formula is valid even when D_u<0; Q-P cannot be zero. Direct
composition gives C_(u^k)=C_u G_k and D_(u^k)=D_u G_k. Therefore, if
D_u>0, repetition changes neither the rational fixed point nor its
reduced denominator. This cyclotomic cancellation must be removed
before treating a repeated word as a new cycle.

## 2. One fixed defect: bounded cancellation and periodic cancellation factors

Let u,v be nonempty words, write

    Q=2^sum(u),  P=3^len(u),  D_u=Q-P,
    S=2^sum(v),  R=3^len(v),  D_v=S-R,
    K=D_u C_v-D_v C_u,

and let w_k=u^k v, k>=1, with D_k=D_(w_k)>0. Then

    C_k = R C_u G_k + Q^k C_v,                       (1)
    D_k = S Q^k-R P^k,                              (2)
    D_u C_k-C_u D_k = Q^k K.                        (3)

Equation (3) follows on replacing D_u G_k by Q^k-P^k.
If g_k=gcd(C_k,D_k), then g_k is coprime to 6 and hence to Q. Equation
(3) proves

    g_k divides K.                                  (4)

In particular, when K is nonzero,

    den(w_k) = D_k/g_k >= D_k/|K|.                   (5)

For K!=0 the cancellation is bounded independently of k. If also
D_u>0, then D_k grows exponentially with k, so each fixed denominator,
including 1, occurs for only finitely many k in this family. This is a structural
exclusion for one fixed defect, not a universal cycle exclusion.

The zero case has an exact word interpretation. If K=0 and D_k>0,
then D_u and D_v have the same sign, because C_u,C_v>0. They cannot
both be negative: Q<P and S<R would imply D_k<0. Hence both are
positive and C_u/D_u=C_v/D_v. From that same positive rational
starting point, u and v are both exact returning valuation words.
Determinism makes the two infinite words uuu... and vvv... identical.
Their common least period divides both lengths, so u and v are
powers of one common primitive word. Conversely, such powers have
K=0. The denominator of w_k is then that primitive word's denominator.

There is a sharper formula when the two block differences are
coprime:

    gcd(D_u,D_v)=1  ==>  g_k=gcd(D_k,K).             (6)

To prove it, set H=gcd(D_k,K). Certainly g_k divides H. If a prime p
divided both H and D_u, then Q=P modulo p and
D_k=P^k(S-R)=P^k D_v modulo p. Since p is prime to 3, p would divide
D_v, contradicting the hypothesis. Thus gcd(H,D_u)=1. Reducing (3)
modulo H now gives H divides C_k, so H=g_k.

For shared primes, formula (6) need not hold. The always valid
two-sided divisibility statement is

    H/gcd(H,D_u) divides g_k divides H,  H=gcd(D_k,K).   (7)

Indeed, H divides D_u C_k by (3), and cancellation of
gcd(H,D_u) shows that H/gcd(H,D_u) divides C_k. Every possible
correction to (6) is therefore supported at primes dividing both
D_u and D_v. At a shared prime p, one has p|D_k for every k.
If p does not divide C_u, the first-order residue is particularly
explicit:

    C_k = P^(k-1) (R C_u k + P C_v) modulo p.       (8)

Thus p divides g_k at one residue class of k modulo p, rather than
automatically. Higher prime powers are handled by (1)-(3).

There is nevertheless an exact finite periodic law for every K!=0,
without a coprimality assumption. Remove all factors 2 and 3 from
|K| and call the result K_0. Since D_k is coprime to 6,
g_k divides K_0. If K_0=1, every g_k is 1. Otherwise put

    L=K_0 |D_u|,
    T=lcm(ord_L(Q),ord_L(P)).

The two multiplicative orders exist because L is coprime to 6.
Both Q^T and P^T are 1 modulo L. Consequently
G_(k+T)-G_k is divisible by K_0, and (1)-(2) show that C_k,D_k
are periodic modulo K_0. Hence

    g_(k+T)=g_k                                      (9)

whenever the denominators in question are positive. Euler's phi(L)
is a simpler, possibly larger explicit period. Evaluating one period
of (1)-(2) gives the exact denominator spectrum
D_k/g_k for every k with D_k>0. If D_u>0, all sufficiently
large k have D_k>0; small k still require the sign check.

Two examples show the necessity of the shared-prime clause and that
nontrivial periodic cancellation really occurs.

* For u=(3), v=(1,5), one has (C_u,D_u)=(1,5),
  (C_v,D_v)=(5,55), K=-30. At k=1, w=(3,1,5) has
  (C_1,D_1)=(49,485), so g_1=1 although gcd(D_1,K)=5.
  The naive coprime formula is false. For the smaller shared-prime
  illustration u=(3), v=(1,1,3), K=90; the prime 5 divides every
  D_k but divides C_k exactly when k=4 modulo 5.
* For u=(1,1,3), v=(2), one has (C_u,D_u)=(19,5),
  (C_v,D_v)=(1,1), K=-14. Formula (6) gives
  g_k=gcd(4*32^k-3*27^k,7). Modulo 7, the six values of D_k
  for k=0,...,5 are 1,5,5,0,6,4, so g_k=7 exactly when
  k=3 modulo 6, and otherwise g_k=1. This family is primitive
  for every k because valuation 2 occurs exactly once. Its rational
  minimum is bounded: with t=(27/32)^k, its start after v is
  [3*(19/5)*(1-t)+1]/(4-3t), strictly below 31/10. It does not
  supply high-cycle controls.

## 3. A primitive nonmechanical family with growing minima

The bounded-cancellation mechanism also applies when the repeated
block varies. For each integer m>=13, set

    V=3^m,  A=bit_length(V)=ceil(m log_2 3),
    U=2^A,  Delta=U-V,
    a_i=floor((i+1)A/m)-floor(iA/m),  0<=i<m,
    u_m=(a_0,...,a_(m-1)).

Then V<U<2V, so 0<Delta<V. This is R71's mechanical valuation
word, and every state of its rational cycle is greater than m/6.
In particular x_0=C_(u_m)/Delta>m/6>1.

For every k>=2, append the one-letter word v=(2) and write
w_(m,k)=u_m^k (2). Since U>V, the word has D_(m,k)>0 and therefore
gives a genuine positive odd rational cycle. The denominator and
primitivity conclusions below hold for every k>=2. The height and
local-minimum conclusions additionally use the condition

    U^k>=2 V^k.                                     (10)

A sufficient explicit choice is k>=ceil(V/Delta):
Bernoulli's inequality gives
(U/V)^k=(1+Delta/V)^k>=1+k Delta/V>=2.

**Denominator.** Here K=Delta-C_(u_m)<0. For each j<m,
the jth summand of C_(u_m) is less than 2*3^(m-1):
indeed 2^floor(jA/m)<=2^(jA/m)
<=3^j 2^(j/m)<2*3^j. Therefore

    C_(u_m)<(2m/3)V,  |K|<(2m/3)V<V^2.             (11)

Also D_(m,k)=4U^k-3V^k>V^k>=V^2. Equations (4)-(5)
give the explicit nonintegrality bound

    den(w_(m,k)) > 3 V^(k-1)/(2m) > 1.             (12)

No word in this family is a nontrivial d=1 integer cycle.

**Every state grows with m under (10).** The affine map of u_m has slope
q=V/U<1 and fixed point x_0. Assume (10), and let x be the cycle state immediately
after the appended valuation 2. The return equation gives

    x=[3*x_0*(1-t)+1]/(4-3t),  t=q^k<=1/2.         (13)

Since x_0>1, one has 1<x<x_0. Moreover

    x/x_0 > 3(1-t)/(4-3t) >= 3/5.                 (14)

At the start of each of the k copies of u_m, the state is
x_0+q^j(x-x_0), which is at least x. Every prefix map of u_m
has positive slope and nonnegative intercept. Hence every state
within each copy is at least 3/5 of the corresponding state of
the pure u_m cycle. R71's bound now gives

    every state of w_(m,k) > m/10 > 1.             (15)

The cycle minimum is unbounded as m grows, even though its reduced
denominator also grows. This is a rational and varying-d control,
not a fixed-d counterexample.

**Primitive and outside the balanced family.** Put alpha=A/m.
The integer inequalities 3^2>2^3 and 3^17<2^27 give

    3/2 < alpha < log_2 3 + 1/m
                 <= 27/17+1/13=368/221 < 5/3.  (16)

Floor differences show that u_m begins (1,2,1,2), ends (2,2),
has no cyclic (1,1), and has no cyclic (2,2,2). The latter two
facts also follow because any length-two or length-three factor
of the periodic mechanical word has valuation sum differing by at
most one from 2*alpha or 3*alpha. Appending (2) creates exactly one
cyclic (2,2,2) factor in w_(m,k). A proper repetition would repeat
that factor, so w_(m,k) is primitive, including up to cyclic rotation.
It also contains (1,2,1), with sum 4, and (2,2,2), with sum 6.
Mechanical words have length-three factor sums differing by at most
one. Thus w_(m,k) is not a mechanical valuation word or any rotation
of one.

In the shortcut parity clock, a valuation a contributes one 1 and
then a-1 zeros. The initial (1,2,1,2) gives the factor 11011,
with four ones in five positions; the unique (2,2,2) gives
01010, with two ones in five positions. The cyclic shortcut word
is not balanced and hence is outside the Christoffel family used
for high-cycle extremal controls. No claim about all nonbalanced
words follows.

Under (10), all states exceed 1. Odd-only steps with valuation 1
increase and steps with valuation 2 decrease. The 1s are isolated,
so the number of distinct odd-only local minima is

    k*(2m-A).                                       (17)

The shortcut clock has a different count: each valuation-2 block
has one even step, and the next odd state is a local minimum. Thus
its number of local minima is

    k*(A-m)+1.                                     (18)

The two clocks must not be interchanged when using published
local-minimum bounds.

## 4. Controls and limits

The theorem preserves actual generalized-map cycles. The primitive
valuation words (1,2,2), (1,3), and (4) have respectively
(C,D)=(23,5), (5,7), and (1,13). Scaling their rational cycles
gives integer cycles for 3x+d at d=5,7,13. If one chooses v=u
in the theorem, K=0 and repetition retains precisely those
denominators. There is no universal exclusion of positive
denominators 5,7,13.

The result controls one repeated block and one fixed defect. It
does not bound cancellation for arbitrary words with many changing
defects, and it cannot settle the full denominator spectrum. Its
useful intermediate conclusion is that a fixed noncommuting defect
cannot create indefinitely large cyclotomic cancellation; the
remaining gcd is a finite periodic function of the repetition
count. The varying mechanical-block construction shows this
conclusion applies beyond the balanced family while retaining
large-minimum rational controls.

The algebra of T-word concatenation, its commutator relation and its
repetition formula appear in Manfred Trümper, [The Collatz Problem in
the Light of an Infinite Free Semigroup](https://onlinelibrary.wiley.com/doi/10.1155/2014/756917),
Section 4. The exact odd-only gcd bound and the family above are
derived here; priority or novelty is not claimed. R71 supplies the
mechanical-word denominator and size bound used in Section 3.

The saved [finite receipt](spectrum_audit.json) from
[check_spectrum.py](check_spectrum.py) records 239,345 positive word
cycles, including 238,328 nonzero-K bounds and 212,522 coprime
exact-formula checks, plus 306 high-family cases. These finite checks
support the implementation but do not replace the universal proofs.
