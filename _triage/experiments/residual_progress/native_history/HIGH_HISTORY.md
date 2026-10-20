# A high common tail supplies a decreasing critical-nine family

**R80 — written conditional family theorem and finite exact certificates.**
A complete arithmetic progression in the blocked W9 row has a smaller
canonical comparison seed whose history meets the target above its original
height. The comparison needs no descent along the displayed target prefix.
The same family defeats every smaller-origin inverse comparison through any
prescribed depth, with the seed varying with that depth. Terminal pair
currents remain supplied premises. This is neither universal W9 supply nor
a Collatz proof; no novelty or formal-verification claim is made.

Dependencies are the [native critical basis](../critical_basis/CRITICAL_BASIS.md),
the [complete inverse lifting theorem](../inverse_scope/INVERSE_SCOPE.md),
the [R44 returning interface](../returning_phase/RETURNING_FORWARD_INTERFACE.md), and
the [R52 second-block interface](../returning_continuation/RETURNING_SECOND_BLOCK.md).
Use ordinary odd-only Syracuse S, absorbed at1, killed atoms [1]=0,
F(x)=4x+1, and the canonical quotient T=nu S. All currents below use ordinary
S arrows, even when a quotient clock is also stated.

## 1. Complete cylinder and smaller origin

For integers D>=12 and t>=0 set

    q=11547+2^17*3^D*t,       b=q/3,
    p=11391+2^36*3^(D-12)*t,  y=(3q+1)/2.             (1)

Equivalently the full family is

    b=3849 modulo 2^17*3^11,
    q=11547 modulo 2^17*3^12,
    p=(2^19*q-309105)/3^12.                           (2)

The D=12 progression is the complete domain constructed here. Larger D
select subprogressions with a stronger inverse obstruction. All parameters
are positive integers and

    b<p<q<y,    rho(b)=q.                             (3)

Indeed q-p=156+(2^17*3^12-2^36)*3^(D-12)*t>0,
because 3^12=531441>524288=2^19. The other inequalities follow directly
from(1). All of p,q,y are canonical. In particular q=27 modulo96,
b=9 modulo32, and y=1 modulo8.

This lies entirely in R75's blocked local W9 branch. Put z=(3q-1)/16.
Then d=v2(9b-1)=4, and3z is selected, hence noncanonical. The latter phase
is already fixed by q=11547 modulo2048:3z=95 modulo128,
v2(3z+1)=5, and (3z+1)/32=3 modulo4. Thus its ordinary local continuation
has the higher E_return request u=(3q+3)/4, rather than a descending W9 rule.

## 2. Prescribed high merger, including every phase

The ordinary path from p has the exact word

    omega=(1,1,1,1,1,1,2,2,1,1,1,1,2),              (4)

of length13 and total valuation16. Its affine formula is

    S^13(p)=(3^13*p+1779283)/2^16
           =24q+13=16y+5=F^2(y).                    (5)

The complete base path and accumulated valuations A_j are:

| j | state at t=0 | A_j |
|---|---:|---:|
|0|11391|0|
|1|17087|1|
|2|25631|2|
|3|38447|3|
|4|57671|4|
|5|86507|5|
|6|129761|6|
|7|97321|8|
|8|72991|10|
|9|109487|11|
|10|164231|12|
|11|246347|13|
|12|369521|14|
|13|277141|16|

For each j the actual state is the displayed base plus

    3^j*2^(36-A_j)*3^(D-12)*t.                       (6)

Every increment is divisible by2^20. At the base states, direct substitution
checks the exact valuation in(4); each state through j=12 is canonical,
and its canonical phase is fixed modulo512. Thus(6) preserves every stated
valuation and canonical phase for all t. The last state has exactly two
inverse-F reductions to canonical y. There are no hidden normalization
branches in this argument. For j=1,...,12, the base state exceeds11547 and

    3^j*2^(19-A_j)>3^12.

These twelve finite integer slope comparisons establish that every displayed
intermediate smaller-origin state after p is greater than q. The maximum
is the j=12 state32q+17.

On the target side S(q)=y. Since S(F^2(y))=S(y), the actual common state is

    S^2(q)=S^14(p)=S(y)=(9q+5)/8>q.                  (7)

The ordinary common-tail clocks are therefore **(2,14)**. In the canonical
quotient the histories meet at y with clocks **(1,13)**. Both displayed
ordinary successors of q are canonical and greater than q. This is a
comparison with the high history of the smaller origin p; it does not
assume that q itself first descends, or that a lower-origin history is
available without its supplied absorption premise.

## 3. Exact signed current and original rank

Let L_p be the13-arrow current in(4), and x=F^2(y). Define

    K=delta_q-L_p-delta_x+delta_y.                    (8)

Its boundary is [q]-[p], because the last two current rows have boundary
[y]-[x]. The rows at x and y are both retained; equality of their successors
does not permit dropping their source contributions.

Write the native critical absorption plans from R75 as

    [s]=div J_s+sum_v A_s(v)P(v),
    P(v)=[3v]-[v], v in W5 union W9,
    A_s(v)!=0 => rho(v)<=nu(s).                       (9)

Set

    C_b=K+J_p-J_b,       c_b=A_p-A_b.                (10)

Then the full signed identity is

    P(b)=div C_b+sum_v c_b(v)P(v).                    (11)

Every nonzero request has rho(v)<=max(p,nu(b))=p<q=rho(b), including
negative coefficients. Equations(8)-(11) are a finite arithmetic constructor,
conditional on its exact smaller critical inputs. It applies directly at
the blocked W9 parent and preserves the original rank q throughout. The
compiler verifies every supplied pair current before substituting it.

R75 supplies a convenient common interface with no compulsory W9 elimination
overhead. The earlier [history scope audit](../adjacent_history/HISTORY_SCOPE.md)
correctly identified an obstacle to the particular old W5-only H compiler;
that general obstacle is absent from(9). **This particular merger does not
require that improvement.** Here p=127 modulo512, a complementary canonical
state with v2(p+1)=7. If p=0 or1 modulo3 its original H plan makes a direct
W5 request of rank p, followed by absorption at an index at most(2p+1)/3.
The old bound(9s+5)/8 on that smaller seed is below p. If p=2 modulo3,
its point predecessor s=(2p-1)/3 has old bound(3p+1)/4<p. Thus in all three
cases old H_p already has every rank at most p. Old H_b has bound
(9b+5)/8<q. The executable five_frontier_plan therefore uses the same K
with the old W5-only H_p-H_b plans and passes the same original-rank test.
Its parent is still W9, and this does not change the old W5 dispatcher.
Neither interface proves that all unknown orbits enter a supplied lower
history in bounded time.

## 4. Arbitrarily deep complete inverse exclusion on the same family

The stored [anchor certificate](anchor_certificate.json) is an exact table
Q of4892 canonical states, maximum3012713, with every canonical origin
below11547 included, every T edge internal to Q, and11547 excluded. The
checker verifies all edges arithmetically, traces only supplied table edges,
and confirms Q is exactly the forward closure of those smaller origins.
No search for an unknown orbit is part of default verification.

Consequently no smaller canonical origin reaches11547 at any depth: its
forward orbit would remain in Q. The analogous ordinary statement follows
from T nu=nu S. This is a finite invariant-set certificate of an all-depth
statement about this one anchor, rather than extrapolation of a depth cap.

R49's lifting theorem now applies. For t>=1 and every depth1<=d<=D,

    T^d(a)=q, a canonical  => a>q.                    (12)

Every ray and every nonnegative ray index is included. For completeness,
shadow any legal inverse word at a_0=q and c_0=11547. Its branches have
alpha>0 and alpha-beta>=1, strictly on a ray, and satisfy

    a_i=lambda_i*(q-11547)+c_i,
    G_i=lambda_i-(c_i+1)/11548
       =alpha_i*G_(i-1)+(alpha_i-beta_i-1)/11548.      (13)

The congruence modulo3^D makes each branch legal for the shadow through D.
Every shadow is an ancestor of11547, so c_i>=11547. The first branch is a
ray because11547=0 modulo3; hence G_i>0 and lambda_i>1 at every positive
depth. Formula(13) gives a_i>q. Semiconjugacy also rules out an ordinary
origin a<=q reaching q in1 through D ordinary arrows.

At t=0 the anchor itself has the all-depth exclusion. For t>0 the theorem
asserts only the indicated depth D. Increasing D changes q; it establishes
no permanently excluded positive trajectory. There is no conflict between
(7) and(12): p reaches the future state of q, and does not reach q itself.

## 5. Comparison with the existing returning rules

For the blocked higher request u=(3q+3)/4, R44 has a=7 and endpoint

    n=(6561q+8965)/1024=73993 modulo128.

It is canonical1 modulo8. R52's second prescribed endpoint is

    f=(19683q+27919)/4096=55495 modulo32.

It is canonical7 modulo32 and1 modulo3. Throughout(1), f>rho(u)>q.
Both actual old plans retain P(v) with coefficient+1 for
v=(2f+1)/3, rho(v)=f. The native H_n and H_f plans also retain this same
high request. Thus these two transported comparisons fail at the original
W9 rank q even after the basis improvement; their failure is not merely
the old9/8 formal-H bound. The local W9 endpoint(9q+5)/8 is also above q.

For the base example u8661, the unchanged seventeen-family W5 dispatcher
returns unresolved. The receipt records a small further finite comparison
with that dispatcher. These samples are not a universal nonrecognition
claim for the whole family, and the old W5 dispatcher is unchanged. This
result adds a proved native W9 comparison; it does not claim a new W5-only
coverage theorem or defeat every possible forward comparison.

## 6. Reproduction and remaining obligation

Run from the repository root:

    python3 experiments/residual_progress/native_history/check_native_history.py

Default replay reads the supplied anchor and designated exact pair currents,
reconstructs the conditional plans and output currents, and checks their
boundaries independently. The [receipt](native_history_audit.json) records
all tested parameters, hashes every reachable imported source and the proof
and anchor, and retains two complete supplied-current demonstrations.
Optional --write regenerates the receipt; only that mode performs bounded
ordinary absorption searches to prepare its designated finite supplies.

The whole-cylinder proof and the complete inverse theorem are the arguments
above. Bounded word tests illustrate their implementation. Missing smaller
pair inputs remain explicit, and the complement of this W9 cylinder remains
unresolved. A high common tail can supply progress where the stated direct
and inverse comparisons fail; universal availability of such a tail is not
proved.
