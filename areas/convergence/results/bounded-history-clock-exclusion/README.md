# Arbitrarily delayed access to smaller histories, including every inverse ray

**R85 — written clock-bound theorem with exact finite checks.** The source
changes with the requested precision. This excludes uniform bounded-clock
history catalogues on the stated critical family, not unrestricted histories,
all signed currents, or absorption of any fixed positive source. It does not
complete the H17 exit type. No novelty is asserted.

Use the absorbed odd Syracuse map S and the canonical quotient T=nu S from
[R25](../bridge_normal_form/BRIDGE_NORMAL_FORM.md). A history comparison is
`T^d(p)=T^a(q)` (or its separately stated ordinary-clock counterpart).
Different clocks a,d are allowed. All sources and targets are positive.

## 1. The complete quotient-clock statement

**Theorem.** Let D>=1 and q be a positive canonical integer divisible by3^D.
Suppose the first J ordinary arrows all have valuation1 and all their states
are canonical. Write

    y_a=T^a(q)=S^a(q)=(3/2)^a(q+1)-1,       0<=a<=J.       (1)

For every a in this range, the complete set of canonical origins p<=q
reaching y_a in at most D+a quotient steps is exactly

    (p,d)=(q,a).                                          (2)

In particular there is no strictly smaller partner. Every inverse ray index
and every inverse word within the stated horizon is covered. The bound is
on clocks, not on the height of intermediate states or the ray index.
All displayed targets are at least q>=3, so absorption at1 introduces no
additional inverse branch in a path reaching them.

### The inverse formulas

The complete canonical inverse branches have base `(A*x+B)/3`, with rows

| x modulo3 | Point | Ray0 | Ray1 |
|---|---|---|---|
|0|none|(8,3)|(16,3)|
|1|none|(4,-1)|(32,19)|
|2|(2,-1)|(64,19)|(128,83)|

A ray at index L>=0 applies `z ->64^L*z+49(64^L-1)/63` to its base.
Write each branch as alpha*x+beta. For all branches and all ray indices,

    alpha>=2/3,       alpha-beta>=1,                        (3)

with strictness in the second inequality for rays. These are the complete
R25/R41 branches, not a truncated inverse search. For positive real x,

    alpha*x+beta >= (2x-1)/3.                              (4)

Indeed every base dominates the right side, and a ray increment equals
`(64^L-1)(base+7/9)>=0`: the smallest base at x>=0 is-1/3.

### Shadow proof, including the rational-shadow interval

Start any inverse word at y_a. Carry its exact affine representation

    x=lambda*q+c.

Initially lambda=(3/2)^a and c=lambda-1. At every inverse step,

    lambda'=alpha*lambda,       c'=alpha*c+beta,
    lambda'-c'=alpha*(lambda-c)-beta>=1                     (5)

whenever lambda-c>=1. Thus the last inequality holds throughout.
At total inverse depth d, the difference lambda*q has ternary valuation
at least D+a-d. Before each next step d<=D+a this is at least1. Therefore
actual and shadow states have the same residue modulo3, interpreted in
rationals with denominator prime to3 before the shadow becomes integral.

Until the first ray, the only possible inverse is the point branch. These
points exactly undo (1). Before reaching q they are above q; at depth a
they equal q. There is no point branch at q because3 divides q.

Suppose the first ray is chosen from y_k, k>=1, after a-k point undos.
For either ray index L its new affine coefficients are

    lambda=2^(e+6L-k)*3^(k-1),
    c=lambda-m_L,       m_L=(128*64^L+7)/9,                 (6)

where e=6 for Ray0 and e=7 for Ray1. Here m_L is an integer and m_L>=15.
The coefficient lambda is at least32*64^L, so c>0 immediately.

If lambda has a binary denominator, put t=k-e-6L>0. Each further inverse
branch raises its binary exponent by at least1. The first integral shadow
therefore occurs within t further steps, unless the prescribed word ends
sooner. The available ternary precision ensures integrality once the binary
denominator has disappeared. During this initial interval, (4) gives, for
0<=i<=t,

    c_i+1 >= (2/3)^i(c+1)
          >= 3^(e+6L-1)-(2/3)^t(m_L-1)
          >= 3^(e+6L-1)-m_L+1 >1.                         (7)

The positivity is uniform in L: `3^(e+6L-1)>=243*729^L`, whereas
`m_L-1=(128*64^L-2)/9`. The induction using (4) is valid because (7)
keeps each preceding shadow positive. Thus no negative rational shadow can
appear before the first integral one.

Once c is a positive integer, every next branch is integral because its
residue modulo3 agrees with the actual state. It remains positive: the point
branch is available only at c=2mod3 and sends its least positive input2 to1;
the smallest other case is the1mod3 ray at input1, also giving1. All other
base values and ray increments are positive. Canonicality of the shadow is
not required. Equation(5) now gives lambda>=c+1>=2.

If instead the first ray is chosen at q itself, its shadow is already the
positive integer `(16*64^L-7)/9`, and its slopes are `8*64^L/3` or
`16*64^L/3`. Their differences lambda-c are respectively
`(8*64^L+7)/9` and`(32*64^L+7)/9`, both at least1. The same integral-shadow
argument applies directly.

Consequently every state after the first ray has c>0 and lambda-c>=1,
so x=lambda*q+c>q. The point spine has exactly the sole equality (2).
This exhausts every inverse word and proves the theorem.

## 2. The ordinary-clock version needs no canonicality assumption

Suppose q>0 is odd,3^D divides q, and its first J ordinary valuations are1.
For every a<=J and every d<=D+a, the only positive odd p<=q satisfying
`S^d(p)=S^a(q)` is again p=q,d=a. This applies even when the displayed
ordinary prefix is not canonical.

For d<=a, the universal bound `S^d(p)+1<=(3/2)^d(p+1)` already proves the
claim. For d>a let E be the total valuation of the proposed lower word.
Since E>=d>a, inversion of the affine equality has the form

    p=lambda*q+c,       lambda=2^(E-a)*3^(a-d).             (8)

The clock bound gives3^(d-a)|q, so lambda*q and c are integers.
We must justify c>=0 without assuming its whole formal path is integral.
After k lower arrows, of cumulative valuation E_k, the actual-shadow
difference is

    2^(E-a-E_k)*3^(a-d+k)*q.                               (9)

If c were negative, every shadow would stay a negative integer while
E_k<=E-a. At the first noninteger shadow it would still be negative, since
its preceding state is a negative integer. The remaining number of arrows
is at most E-E_k<=a-1. Starting at any negative real, m positive-valuation
affine arrows end strictly below `(3/2)^m-1`: if a numerator stays negative
the result is negative; otherwise division by at least2 is maximized by the
valuation1 map. Thus this remaining tail cannot reach the prescribed
shadow target `(3/2)^a-1`. If there is no noninteger state, its final state
is still negative. This proves c>=0, including a=0.

Finally the same inverse word at upper source-1 starts from target-1.
Every inverse affine map `(2^e*x-1)/3` preserves x<=-1. Hence c-lambda<=-1,
so lambda>=c+1>=1 and p>=q. Equality in (8) would require lambda=1,c=0;
unique prime factorization then forces d=a,E=a, contrary to d>a. This
proves the ordinary theorem. Negative rational shadows were not silently
regarded as negative integers.

## 3. Positive critical families and the H17 implication

For any D>=1,J>=0 choose H>=max(J+1,3) and impose the coprime conditions

    q=0 modulo3^D,
    q=2^H*u-1 modulo2^(H+2),   u=-3^H modulo4.              (10)

The CRT gives an infinite positive progression. Its first J states are
canonical valuation-one states: the complementary unit condition is
preserved as the binary exponent falls, including the final1mod8 state
when that exponent is1. Also q/3=5mod8, so these are actual critical W5
inputs with original rank q.

For any fixed bounds A,B on future and partner clocks, take J=A and
D>=max(B,1). No smaller canonical origin can meet any of the first A future
targets within B quotient steps. Therefore no uniformly bounded-clock
smaller-history catalogue covers all these critical inputs, even allowing
all valuation words, all quotient inverse rays, and unequal times.
The source varies with A,B. This does not exclude a source-dependent
unbounded procedure, other signed comparisons, or Collatz convergence.

There is a direct but deliberately narrower H17 consequence. For any
r>=0,D>=1 impose

    b=(2^(9r+17)-223)*217^(-1) modulo2^(9r+18),
    b=0 modulo3^(D-1).                                    (11)

Again CRT gives infinitely many positive inputs. These are exactly H17
inputs with the stated binary exit order and at least the stated ternary
divisibility. They have b=9mod16, q=3b=11mod16, and a canonical first
valuation-one future `(3q+1)/2`. The theorem excludes smaller canonical
histories to q through depth D and to that first future through D+1.
It says nothing about the later native exit target. In particular it does
not contradict the [R83 all-return-count subfamilies](../native_growth_escape/NATIVE_GROWTH_ESCAPE.md),
which use later future targets and much longer partner words. No exclusion
of every unrestricted finite history at a fixed H17 input is claimed.

## 4. Original-rank and current scope

A supplied smaller history p<q meeting a target of q gives the exact
prefix difference with boundary[q]-[p]. At a critical parent w of rank q,
adding the full elementary normalizer and formal H_p-H_w in the
[R75 retained W5/W9 basis](../critical_basis/CRITICAL_BASIS.md) leaves signed
requests all below q. This uses that basis's bound by the source minimum,
not the older W5-only absorption bound. The present theorem says only that no history of the
specified clocks can provide that input. It does not assert that another
finite signed plan cannot cancel its frontier.

The fixed absorbed example q39 illustrates the distinction. Its first two
canonical valuation-one states are59 and89, and3 divides39, so the theorem
applies with D1,J2. Yet T^3(39)=33<39. The checker supplies a complete
finite P(13) current using explicit absorption paths. The next forward
phase is outside the two-target hypothesis; no fixed-seed nontermination
follows from the clock barrier.

## 5. Reproduction

Run `python3 experiments/residual_progress/history_cover_scope/check_history_barrier.py`.
Default replay compares the stored receipt; `--write-receipt` regenerates
only the declared finite checks. These include exhaustive small-origin
forward checks in both clocks, arbitrary supplied inverse words with large
rays, exact CRT phases, noncanonical ordinary controls, the supplied P13
current, and malformed-domain/cap rejections. No unbounded absorption
search or inverse scan is used. The proof supplies the unlimited-ray and
unlimited-parameter quantifiers; finite probes alone do not.

The stored replay covers62 quotient and126 ordinary domains, with3911 and
16008 origin instances respectively; the latter includes64 noncanonical
source domains. It checks196 critical CRT cells,60 H17 cells,200 inverse
words with ray indices through64,15 exact point-spine equalities, and1560
ordinary word candidates (70 legal). The inverse traces include24 positive
rational-shadow rows and2636 positive integer-shadow rows. A complete
9-row P13 current, its supplied paths, and23 rejection checks are retained.
