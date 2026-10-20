# A bounded repair of every failed critical-nine history request

**Status: written proof and finite exact certificates.** This composes the
existing [R40 local identity](../w9_closure/CRITICAL_NINE_ELIMINATION.md) and
[R75 critical absorption plans](../critical_basis/CRITICAL_BASIS.md) at the
original threshold. It is a complete decision for the specified bounded
reduction, not supply of its terminal currents, a new local orbit identity,
or a change to the seventeen-family dispatcher. Collatz remains open.

## 1. Definitions and exact local identity

Use the positive odd Syracuse map S, absorbed at1, and kill atoms at1.
Write P(w)=[3w]−[w], W5={w>0:w=5 mod8}, W9={w>0:w=9 mod16},
and rho(w)=nu(3w), where nu is the elementary normal form. The retained
critical absorption plan is

    [s] = div J_s + sum_v A_s(v) P(v).                         (1)

Every v is in W5 union W9 and rho(v)<=nu(s). This is a finite formal
identity with unknown exact P(v) currents still explicit. All coefficients
below are signed integers; none may be dropped.

Let w be in W9. Set

    d=v2(9w−1)>=4,
    h=(d−5)/2 for odd d,  h=(d−4)/2 for even d,
    C=(9w−1)/2^d,  z=3^h C,  ell=h+2.

The prescribed ordinary prefixes from 3w and w each have ell arrows.
For odd d their endpoints are F(3z),F(z), where F(x)=4x+1. Add the two
signed sibling currents to obtain endpoints 3z,z. For even d the endpoints
are X=6z+1,Y=2z+1. Call the resulting comparison Gamma_w. Thus

    P(w)=div L_w + sum_v l_w(v)P(v),                         (2)
    L_w=Gamma_w+J_upper−J_lower,
    l_w=A_upper−A_lower.

These are exactly the existing R40 rows, including the ordinary-prefix
multiplicities, the odd-depth sibling rows and both absorption plans.
The implementation imports these rows rather than reconstructing a
different source. For even d, C=2 mod3 and z>=5.

## 2. Complete local decision at the original threshold

**Theorem.** Let Q>=11547 be odd, and let positive w in W9 satisfy

    Q<=3w,                 32w<33Q.                         (3)

The full vector l_w has at most one request of rank at least Q. If it
exists, its coefficient is exactly +1. The following table is exhaustive.
Here “critical” means canonical, equal to3 mod4, and not equal to2 mod3.

| Local case | Complete high-request test | Index of that request |
| --- | --- | --- |
| d odd | Never | None |
| d even, 3z noncanonical | 6z+1>=Q | 4z+1 in W5 |
| d even, 3z canonical, 3z<Q | Never | None |
| d even, 3z complementary canonical, 3z>=Q | Always | z, in W5 or W9 |
| d even, 3z=1 mod8, 3z>=Q | f=(9z+1)/4 is critical and f>=Q | (2f+1)/3 in W5 |

Every other request, including every negative coefficient, has rank
strictly below Q. “Complementary canonical” in the table is the canonical
3-modulo4 class. The last row's f is1 mod3, so there is no unhandled
critical2-modulo3 inverse case. Canonicality/normalization tests are the
complete arithmetic tests, not a finite sample of residues.

**Proof.** For odd d,

    3z<27w/32<891Q/1024<Q,

so (1) applied to 3z,z is strict. For even d, z<9w/16<Q. The lower
endpoint Y is always safe. If d=4, z=2 mod3 and Y is3 mod4 and2 mod3.
When Y is canonical its point inverse is

    (2Y−1)/3=(4z+1)/3=(3w+1)/4<Q.

Its formal plan is the negative inverse row followed by the plan at that
smaller origin. When Y is noncanonical it is selected and nu(Y)<=z<Q.
For d>=6 the direct bound

    Y <= (27w+29)/32 < Q                                    (4)

suffices; the last strict inequality follows from (3) and Q>=11547.

If 3z is noncanonical, X is the critical image of u=4z+1 in W5. Its
formal plan first requests P(u), at rank X, then H_u, whose normalization
is nu(z). This proves the second row, with all later upper requests
below Q. If 3z is canonical, X is its selected partner and normalizes
to3z. This proves the third row directly. If 3z is complementary
canonical, it is divisible3, so its first critical request is P(z),
followed by H_z. This proves the fourth row.

In the remaining case 3z=1 mod8, its next ordinary target is
f=(9z+1)/4. We have

    f <= (81w+7)/64,
    (3f+1)/4 <= (243w+85)/256 < Q.                          (5)

The second expression applies when f=1 mod8. If f is noncanonical,
nu(f)<=(f−1)/2<Q. If f is canonical and3 mod4, it is critical because
f=1 mod3. Its first request has index

    u=(2f+1)/3=(3z+1)/2 < Q,

rank f, and its remaining H_u requests are below Q. Equations (4),(5)
retain the intercepts: for example the last bound in (5) follows from
8019Q+2720<8192Q, already true for Q>=11547. No high upper request can
cancel against a lower request, since all lower requests are strict.
This proves the complete table. The same bounds show H_w is strict:
w=1 mod8 first moves to (3w+1)/4<Q. □

## 3. Two substitutions remove every high W9 request

**Theorem.** Under (3), apply (2) only to the unique request with rank
at least Q if it is in W9. Keep Q fixed throughout. After at most two
local substitutions the resulting exact signed vector has either no
request of rank at least Q, or exactly one W5 request of rank at least Q
with coefficient +1. Every other request has rank below Q.

**Proof.** A high W9 child occurs only in the fourth table row and is
the index z. For every even d,

    16z<9w.                                                (6)

If that child is still high, it satisfies (3): Q<=3z, and its index is
strictly smaller than w. Thus the same complete decision applies. Were
there two consecutive high W9 children w1,w2, (6) would give

    3w2 < (243/256)w < (8019/8192)Q < Q,

a contradiction. Consequently at most two substitutions are needed.
The exact replacement is

    current <- current + L_v,
    coefficients <- coefficients − {v:+1} + l_v.            (7)

The replaced coefficient is always +1. Previously retained requests
are already strict, so they cannot remove or change the unique higher
leader. They may cancel other lower requests; those cancellations are
performed with their exact integer coefficients. □

The number two bounds W9 substitutions, **not ordinary or quotient
clock depth**. Each local prefix has h+2 arrows, with h depending on
the input. The final current is a sum of signed local comparisons and
normalizers; no single ordinary path clock is asserted for that sum.
The theorem does not provide any of the final P(v) currents, including
the possible W5 leader. A finite output is conditional until every
remaining signed input has been supplied and checked.

## 4. Application to every failed W9 case of R84

The [complete thirteenth-target phase](../history_transition/HISTORY_TRANSITION.md)
starts with

    q=11547+3*2^19*k,   b=q/3,   R=70237+2*3^14*k,   k>=0.

All raw A/B/C states are1 mod3 and no larger than R. If its terminal
failed critical atom is n=3w with w in W9, the final normalization is
nontrivial, since n=0 mod3. At least one F stripping gives
nu(x)<=(x−1)/4; otherwise a selected halving gives nu(x)<=(x−1)/2.
Thus every nontrivial elementary normalization satisfies the latter
bound. A selected halving is not mandatory: k=8 stops at an F sibling
without a selected half. Hence

    3w <= (R−1)/2,
    w <= 11706+3^13*k,
    32w < 33q.                                             (8)

The last inequality is exact: its constant difference is6459 and its
k coefficient difference is886176. Also n>=q by failure. Thus the full
domain (3) holds with Q=q.

The original complete conditional vector is

    {w:+1}+A_w−A_b.                                        (9)

Its other ranks are below the ORIGINAL q, not just below n. Indeed
b<q, while w=1 mod8 and H_w starts at (3w+1)/4<q by (8).
The nonleading vectors in (9) therefore cannot cancel the higher
request. Compose (7) into the original R84 current, preserving its
13-to20 quotient comparison and its actual ordinary common-tail
clock metadata. The two-substitution theorem applies to **every**
failed R84 W9 leader, not only the initial selected subphase.

For example the whole initial subphase k=5 mod16 has

    w=11706+3^13*k,     q=(524288w−766101)/531441.

Every exact d>=4 occurs in its complete binary cell

    k=(2^d−105353)*(3^15)^(-1) mod 2^(d+1).                 (10)

The extra bit enforces v2(9w−1)=d; the cells automatically satisfy
k=5 mod16. The full table, rather than a sampled phase label, decides
all their canonical subbranches. Examples: k=5 is strict after one
substitution; k=38 after two. At k=21 the final W5 input18839525 has
rank56518575>q33041691. At k=1062 two substitutions leave W5 input
1607200797, rank2410801195>q1670393115. These failures are retained.

## 5. The natural upper inverse is an exact undo

This statement holds for **every positive w in W9** in the even-depth,
noncanonical-3z branch, independently of (3) or R84. Put

    X=6z+1, Y=2z+1, u=4z+1, D=h+1.

The named R46 maximal inverse test has

    v3(X−1)=D,
    4^D*(X−1)/3^D+2=(9w+3)/2,
    j=v3((9w+3)/2)=1.

Its inverse origin is exactly3w, and its ordinary word is
1 followed by D copies of2, length h+2. This is the existing upper
prefix U from3w to X. Let V be the existing lower prefix w to Y.

The complete conditional inverse plan for P(u) is

    P(u)=div(N_(3u)−U+J_(3w)−J_u)
                 +(A_(3w)−A_u).P.                         (11)

Here N denotes the exact elementary normalizer. Substitution of (11)
into (2), including every signed helper, yields **row for row**

    P(w)=div(J_w−V−J_Y)+({w:+1}+A_w−A_Y).P.                (12)

To verify this, 3w is critical0 mod3, so J_(3w)=J_w and
A_(3w)={w:+1}+A_w. Also X is the critical image of u, and
J_X=J_u−N_(3u), A_X={u:+1}+A_u. Insert these two identities
into the full currents; U cancels exactly. All remaining helpers in
(12) have rank below3w, and under (3) they are below Q by Section2.
The coefficient of P(w) remains +1, so this comparison does not close
the failed leaf at the original rank.

The lower relation in (12) is **not generally zero**. For w=201 the
current has14 nonzero rows and the vector is {201:+1,25:+1,5:+1}.
The receipt stores those rows. This is an undo of the specified inverse
word, not an exclusion of every possible smaller-origin history or
other signed comparison.

## 6. Reproduction and limitations

Run from the repository root without Python optimization:

    python3 experiments/residual_progress/w9_history_repair/check_w9_history_repair.py

The portable module exposes `local_decision`, `bounded_repair`,
`repair_failed`, `even_upper_undo`, and `compile_plan`. The first four
perform prescribed finite arithmetic and retain unresolved inputs.
`compile_plan` accepts only strict original-threshold plans and requires
every signed exact terminal current. Missing, malformed and wrong-boundary
supplies are rejected. The replay reads stored supplies; it does not
discover them. Receipt generation alone uses capped finite absorption
for its designated demonstration seeds.

The checker independently reconstructs divergence, checks generic Q/w
cases beyond R84, exact valuation cells and threshold boundaries, both
one- and two-substitution outcomes, the complete inverse undo and its
nonzero lower fixture, and full supplied outputs. Its finite checks
support the written argument; they neither prove universal supply nor
exhaust all possible W5 continuations. The complete remaining target is
still to supply every surviving current with an original-rank-valid,
terminating construction.

The stored receipt has865 generic Q/w cases,72 threshold-boundary cases,
72 exact-depth progression cells through depth128, and51 full inverse
undos. It examines R84 indices0 through511 plus five specified larger
indices and repairs all72 failed W9 cases found there. It covers all
five decision rows and all three forced-forward terminal types. The
three designated supplied conversions at k=5,38,53 produce166,49,61
current rows, with every input and output table stored. There are37
explicit rejection controls. Finite supply generation is capped at10000
ordinary arrows and2048 state bits per absorbed source. Default replay
uses the stored supplies and performs no absorption discovery.
