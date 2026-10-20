# C002 — Two variable blocks with proportional valuation slopes

**Status: written proof with independent agent review.** This note treats
positive odd rational cycles of the raw 3x+1 map in the odd-only
Syracuse clock. The word has two fixed blocks but both repetition
counts vary: w=u^k v^ell. The theorem gives a uniform lower bound
on its reduced denominator when the two blocks have the same
valuation-to-length ratio. It is a restricted cycle result, not an
exclusion of all integer Collatz cycles.

## 1. Exact two-block identities

For a positive valuation word z=(a_0,...,a_(m-1)), write

    A_j=a_0+...+a_(j-1),  A_0=0,  A=A_m,
    C_z=sum_(j=0)^(m-1) 3^(m-1-j) 2^A_j,
    D_z=2^A-3^m.

If D_z>0, C_z/D_z is a positive rational cycle with exactly the
displayed odd-only valuations, and its reduced denominator is
D_z/gcd(C_z,D_z). The numerator and denominator are odd, D_z is
prime to 3, and cyclic rotation preserves the reduced denominator.
These facts and the exact valuation check are derived in R71.

For nonempty fixed words u and v, put

    Q=2^sum(u), P=3^len(u), D_u=Q-P,
    S=2^sum(v), R=3^len(v), D_v=S-R,
    G_u(k)=(Q^k-P^k)/D_u,
    G_v(ell)=(S^ell-R^ell)/D_v,
    K=D_u C_v-D_v C_u.

The geometric quotients are positive integers even if a block
difference is negative. For k,ell>=1, direct concatenation gives

    C=R^ell C_u G_u(k)+Q^k C_v G_v(ell),           (1)
    D=S^ell Q^k-R^ell P^k,                       (2)
    D_u C-C_u D=Q^k G_v(ell) K,                  (3)
    D_v C-C_v D=-R^ell G_u(k) K.                 (4)

The last two equations follow by substituting
D_u G_u(k)=Q^k-P^k and D_v G_v(ell)=S^ell-R^ell.
If D>0 and g=gcd(C,D), then g is coprime to 6. In particular it
is coprime to both Q^k and R^ell. Equations (3)-(4) imply that
g divides K G_v(ell) and K G_u(k). A Bezout combination of the
two geometric quotients proves the exact necessary divisibility

    g divides K*gcd(G_u(k),G_v(ell)).             (5)

When K=0 this reads 0 and gives no bound. For K!=0 it bounds the
cancellation by the common growth of the two repetition factors.
There is no assumption that D_u and D_v are coprime, and no
shared-prime shortcut is used.

## 2. Proportional-slope denominator theorem

Assume the block totals have the same reduced ratio:

    sum(u)=a*r,  len(u)=b*r,
    sum(v)=a*s,  len(v)=b*s,
    gcd(a,b)=1,  r,s>=1.

Set U=2^a, V=3^b, H_j=U^j-V^j. Then
Q=U^r, P=V^r, S=U^s, R=V^s. For positive k,ell,

    M=r*k,  N=s*ell,  L=M+N,  h=gcd(M,N),
    e=gcd(r,s),  E=H_e.

The whole-word difference is D=H_L. Positivity D>0 holds exactly
when U>V; if U<V, there is no positive rational cycle from these
words. Equality U=V is impossible for positive a,b.
Henceforth suppose U>V.

**Theorem.** E divides K. If K!=0, put J=K/E and let J_0 be the
positive integer obtained from |J| by removing all factors 2 and 3.
For every k,ell>=1,

    g=gcd(C,H_L) divides J_0 H_h,                 (6)
    den(w)=H_L/g >= H_L/(J_0 H_h)
           > U^(L-h)/J_0
           >= U^max(M,N)/J_0
           >= U^(L/2)/J_0.                       (7)

In particular, for fixed u,v with K!=0, every fixed upper bound
d_0 on the reduced denominator confines both repetition counts to
the finite rectangle

    U^max(r*k,s*ell) < d_0 J_0.                  (8)

Thus no bounded denominator, including 1, persists as either
repetition count tends to infinity.

**Proof.** Because U and V are coprime, their differences form a
strong divisibility sequence:

    gcd(H_i,H_j)=H_gcd(i,j).                      (9)

For i>j, the identity
H_i=U^(i-j)H_j+V^j H_(i-j), together with
gcd(V,H_j)=1, reduces the gcd to
gcd(H_j,H_(i-j)); Euclid's algorithm proves (9).

Since e divides both r and s, E divides H_r and H_s, hence K.
Furthermore

    G_u(k)=H_M/H_r divides H_M/E,
    G_v(ell)=H_N/H_s divides H_N/E.

Their gcd therefore divides

    gcd(H_M/E,H_N/E)=H_h/E

by (9). Equation (5) gives g divides K H_h/E=J H_h.
Both g and H_h are coprime to 6, so the factors 2 and 3 of J
can be removed; this proves (6).

The integer h divides L. The quotient H_L/H_h is a geometric
sum with first term U^(L-h) and at least one further positive
term, because L>=2h. It is strictly larger than U^(L-h).
Finally h<=min(M,N), so L-h>=max(M,N)>=L/2.
These facts prove (7). If den(w)<=d_0, its strict lower bound
implies (8). This proves the theorem.

For equal block lengths and totals (r=s), the key step is the exact
identity

    gcd(G_u(k),G_v(ell))
       = (U^(r*gcd(k,ell))-V^(r*gcd(k,ell)))
         /(U^r-V^r).

The proof above also covers r!=s, where a direct equal-base
substitution would be invalid.

**Degenerate case K=0.** Under U>V, both D_u and D_v are positive.
The equality K=0 says C_u/D_u=C_v/D_v. Both words are then exact
return words from the same positive rational starting point.
Determinism makes their infinite valuation words identical, so
u and v are powers of one common primitive word, starting in the
same phase. The whole word is a repetition of that primitive word,
and its reduced denominator is unchanged by k or ell. This case
must remain: u=v=(1,2,2), u=v=(1,3), and u=v=(4) retain
denominators 5, 7, and 13 respectively, furnishing actual
generalized 3x+d cycle controls. The d=1 branch is not classified
by this theorem.

### Uniform equal-total corollary

The fixed-pair constant in (7) can be eliminated when u and v are
*distinct* words with the same length m and valuation total A. Write
U=2^A, V=3^m, and suppose U>V. For k,ell>=1 set n=k+ell and
h=gcd(k,ell). Then, whenever n>=3,

    den(u^k v^ell)>U^(n-h)/|C_v-C_u|
                    >2^m*U/V>2^m>1.               (U1)

This is uniform while u,v,m,A,k,ell all vary. In particular, among
all such distinct equal-total block pairs and n>=3, only finitely
many representations have denominator at most any fixed d_0.

To prove this, the valuation bound a_j>=1 gives
A_j<=A-(m-j), so the intercept of *any* length-m word z with
total A obeys

    C_z<=sum_(j=0)^(m-1) 3^(m-1-j)2^(A-m+j)
       =2^(A-m)(3^m-2^m)
       =U*((3/2)^m-1)<U*V/2^m.                      (U2)

All intercepts are positive, hence |C_v-C_u|<UV/2^m.
The two words cannot have the same intercept unless they are
identical: they would have the same positive fixed point, and the
deterministic exact valuation sequence at that point would specify
both length-m words. Thus J=C_v-C_u is nonzero. In Section 2's
reduced notation, c=gcd(A,m), r=s=c, E=U-V and J=K/E=C_v-C_u;
equation (7), with its base raised to c, gives the first strict
inequality in (U1). Because n>=3, n-h>=2, and (U2) gives the second.

If den<=d_0, (U1) forces m<log_2(d_0) and
U<d_0*V/2^m. There are therefore finitely many possible pairs
(m,A), then finitely many words u,v for each pair. Once a pair is
fixed, (8) bounds k and ell. The argument makes no exclusion
at n=2.

## 3. The half-exponent is sharp

Let u=(1,3) and v=(3,1). Both have total valuation 4 and length
2, with Q=S=16, P=R=9, D_u=D_v=7,
C_u=5, C_v=11, and K=42. In the reduced-slope notation,
(a,b)=(2,1), (r,s)=(2,2), U=4, V=3, E=H_2=7,
J=6, and J_0=1.
Take k=ell=t>=1 and put A=16^t, B=9^t,
G_t=(A-B)/7. Formula (1) gives

    C=G_t(11A+5B),  D=G_t*7(A+B).                 (10)

The two bracketed factors are coprime. Modulo 7,
A=16^t and B=9^t have the same nonzero residue, so
11A+5B is 2B, not zero. A common divisor of
11A+5B and 7(A+B) is therefore coprime to 7
and must divide A+B. Subtracting 11(A+B) shows
that it divides 6B. It is coprime to B because
gcd(A,B)=1, so it divides 6. But A+B is odd
and is 1 modulo 3. Therefore

    g=G_t,  den(u^t v^t)=7(16^t+9^t).             (11)

The cyclic word (1,3)^t(3,1)^t has exactly one factor (3,3),
at the u-to-v boundary. It is therefore primitive, including
up to rotation. Its total proportional exponent is L=4t and
its denominator is of order U^(L/2)=4^(2t). The exponent 1/2 in (7)
cannot be increased uniformly for this class.

## 4. A primitive family with growing minima and both counts free

The bound has a nonmechanical family with every rational state
growing with the block size. Fix m>=13, let

    V=3^m, A=bit_length(V)=ceil(m log_2 3),
    U=2^A, Delta=U-V,
    u=(a_0,...,a_(m-1)),
    a_i=floor((i+1)A/m)-floor(iA/m),
    v=(a_1,...,a_(m-1),a_0).

Thus v is the one-letter left rotation of the R71 mechanical
word u. Its length and total equal those of u. If
c_0=gcd(A,m), the reduced-slope notation of Section 2 is
(a,b)=(A/c_0,m/c_0), r=s=c_0, with full-block
powers U=2^A and V=3^m. R71 proves that every state
of either pure rational cycle is greater than m/6.

Let x_u=C_u/Delta and x_v=C_v/Delta be their respective fixed
starting states. The rotation identity, with first valuation
a_0=1, gives

    x_v=(3x_u+1)/2,
    x_u<x_v<2x_u,  x_u>m/6>1.                     (12)

For k,ell>=1 set w=u^k v^ell, n=k+ell, and
h=gcd(k,ell). Its difference is U^n-V^n>0, so it is an exact
positive rational cycle.

**Height at every phase.** Both block maps have slope q=V/U<1
and fixed points x_u,x_v. Let x be the cycle state before the
first u and y the state before the first v. With
t=q^k and z=q^ell, the return equations are

    y=x_u+t(x-x_u),  x=x_v+z(y-x_v),
    x=x_u+(x_v-x_u)(1-z)/(1-tz).                   (13)

Hence x_u<x<x_v and x_u<y<x_v. Every intermediate block start also
lies in (x_u,x_v). A prefix of u is an affine map with positive
slope and nonnegative intercept; from a start greater than x_u
it exceeds the corresponding pure u-cycle state, hence m/6.
A prefix of v starts above x_u>x_v/2 and exceeds half the
corresponding pure v-cycle state, hence m/12. Therefore

    every state of w is greater than m/12 > 1.    (14)

This holds for all k,ell>=1 without a separation condition.

**Denominator.** Rotation gives

    J=C_v-C_u=(C_u+Delta)/2>0.                     (15)

The R71 term estimate gives C_u<(2m/3)V:
for 0<=j<m,
2^floor(jA/m)<=2^(jA/m)
<=3^j 2^(j/m)<2*3^j.
Since x_u>1, C_u>Delta, so J<C_u<(2m/3)V.
In the reduced notation, the theorem's exponents are
M=c_0 k, N=c_0 ell and h_theorem=c_0 h, so its
U_base^(L-h_theorem) is the full-block U^(n-h).
If n>=3, then n-h>=2. Equation (7) yields

    den(w)>U^(n-h)/J
          >3 V^(n-h-1)/(2m)>1.                    (16)

Thus this two-variable family has no d=1 integer cycle for
n>=3. Its reduced denominator and cycle minimum both grow
without bound as m grows, with k and ell free subject to n>=3.

**Primitivity and clock controls.** The elementary inequalities
3^2>2^3 and 3^17<2^27 imply

    3/2 < A/m < 27/17+1/13 < 5/3.

The mechanical word u begins (1,2,1,2), ends (1,2,2),
has no cyclic (1,1) and no cyclic (2,2,2). Its rotation v
begins (2,1,2) and ends (2,2,1). In w, the u-to-v
boundary creates exactly one cyclic (2,2,2), and the v-to-u
boundary creates exactly one cyclic (1,1). No same-block
boundary creates either. The unique (2,2,2) proves w is
primitive for every k,ell>=1. The factors (1,2,1) and
(2,2,2) have length three but valuation sums 4 and 6, so
w is not a mechanical word. In the shortcut parity encoding,
the factors (1,2,1,2) and (2,2,2) give 11011
and 01010, with four and two ones in five positions;
the word is not Christoffel-balanced.

All states exceed 1, so valuation-1 odd-only steps increase
and valuation-2 steps decrease. Each u and v has
2m-A valuation-1 letters. Exactly one cyclic pair of 1s
merges two increasing runs. Since w is primitive, its
number of distinct odd-only local minima is

    n*(2m-A)-1.                                    (17)

In the shortcut clock each valuation-2 block contributes
one even descent followed by an odd rise. The count there is

    n*(A-m).                                      (18)

These counts use different clocks and must not be exchanged.

## 5. Scope and sources

The general dual identity (5) requires no proportionality but
does not by itself bound the gcd of two unrelated geometric
quotients. The proportional theorem gives a finite verification
rectangle for each fixed pair of noncommuting blocks. It does
not give a uniform finite layer over all varying word pairs with
different totals. The equal-total corollary does give this
uniform finiteness for distinct words and at least three blocks.
K=0 can retain actual positive generalized-map
cycles, while a hypothetical d=1 cycle is still unresolved.
The rotating family supplies primitive, unbalanced rational cycles
with growing minima, not a fixed-d counterexample.

The word formulas and mechanical size bound are in
R71 (`experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md`, not yet migrated).
The one-defect predecessor is [C001](../repeated-block-cancellation-bound/REPETITION_SPECTRUM.md).
Manfred Trümper's [2014 T-word paper](https://onlinelibrary.wiley.com/doi/10.1155/2014/756917)
contains concatenation, commutator and repetition formulas in
its own notation. The specific proportional-slope cancellation
bound and rotating family above are derived here; priority and
novelty are not claimed. A finite test of selected words can
illustrate the formulas but cannot replace the universal proof.
