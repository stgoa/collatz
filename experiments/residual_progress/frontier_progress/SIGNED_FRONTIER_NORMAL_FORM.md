# Exact cancellation of a finite signed pair frontier

**Status: written two-identity normalization theorem, exact finite compiler,
and bounded executable audit.** The construction terminates on every finite
integer request vector. Its output may contain unresolved pair currents.
It does not add a dispatcher rule or prove Collatz convergence. Its complete
kernel statement concerns precisely the two identities below, not all ordinary
Collatz comparisons. No novelty or formal-verification claim is made.

Use the odd Syracuse map S, absorbed at1, and killed atoms [1]=0. An ordinary
current row delta_x has divergence [x]-[S(x)]. Write W5={w>0:w=5 mod8},
P(w)=[3w]-[w], and F(x)=4x+1. The existing critical rank is rho(w)=nu(3w).
All currents and request coefficients below are signed integers.

The inputs being simplified are the full conditional current identities from
[R44](../returning_phase/RETURNING_FORWARD_INTERFACE.md), especially the
[R69 reset family](../arithmetic_progress/VALUATION_DEBT.md). The limitation
in Section6 uses the [R67 mixed block](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md)
and the strictly smaller pair-index bound in
[R41](../critical_inverse/CRITICAL_INVERSE.md).

## 1. Two complete pair identities

### Identity I

For every positive w=93 modulo512, put u=(9w-5)/64. Then u is positive,
u=5 modulo8, u=4 modulo9, and u<w. Conversely every positive W5 input
u=4 modulo9 gives a parent w=(64u+5)/9 in this domain. The actual ordinary
arrows satisfy

    w -> (8u+1)/3 -> 4u+1=F(u),
    3w -> 32u+3 -> 48u+5=F^2(3u).                    (1)

The valuation words on both displayed paths are respectively(3,1) and(1,1).
Since S(F^k(x))=S(x) for k>=1,

    S^3(w)=S(u),       S^3(3w)=S(3u).                (2)

Define the eight-row current

    C_I(w)=delta_(3w)+delta_(32u+3)+delta_(48u+5)+delta_u
            -delta_(3u)-delta_w-delta_((8u+1)/3)-delta_(4u+1).

Telescoping(1), including the last sibling row on each side, proves

    div C_I(w)=P(w)-P(u).                            (3)

The displayed rows are distinct throughout this domain. In particular the
smallest example is w93,u13, and the formula is valid at that endpoint.
The parent3w is selected, so rho(w)=(3w-1)/2, while
rho(u)<=3u<rho(w). This identity uses no absorption premise.

### Identity II

For every positive b=1285 modulo2048, put c=(b-5)/256 and a=9c. Then
c=5 modulo8, a is a positive W5 input divisible by9, and a<b. Conversely,
every positive W5 input a divisible by9 gives b=(256a+45)/9 in this domain.
The actual paths are

    b -> 48c+1 -> 36c+1=F(a),
    3b -> 1152c+23 -> 1728c+35 -> 2592c+53=F^3(h),
    h=(81c+1)/2=S(3a).                              (4)

The first two valuation words are(4,2) and(1,1,1); the last equality uses
v2(81c+1)=1. Thus

    S^3(b)=S(a),       S^4(3b)=S^2(3a).              (5)

Define the ten-row current

    C_II(b)=delta_(3b)+delta_(1152c+23)+delta_(1728c+35)
              +delta_(2592c+53)+delta_a
              -delta_(27c)-delta_((81c+1)/2)-delta_b
              -delta_(48c+1)-delta_(36c+1).

Telescoping(4) proves

    div C_II(b)=P(b)-P(a).                           (6)

Again all displayed rows are distinct, including the smallest c5,b1285,a45.
Here rho(b)=(3b-1)/2, and rho(a)<=3a<rho(b). Both identities are therefore
compatible with the old rho induction, but this note does not change its
dispatcher. The point is their joint action on signed requests.

## 2. A terminating normalization of the whole integer vector

The two parent guards are disjoint: their residues modulo512 are93 and261.
Define a partial child map d on W5 by

    d(w)=(9w-5)/64             if w=93 mod512;
    d(w)=9(w-5)/256            if w=1285 mod2048.     (7)

Every child is a positive W5 integer and d(w)<=9w/64<w. Repeatedly apply(7)
until it no longer applies, giving the unique terminal tau(w). Let C_w be
the sum of the corresponding ordinary currents. Then

    div C_w=P(w)-P(tau(w)).                          (8)

This is a terminating computation; no unknown trajectory is searched.
Both identities can be padded to common ordinary clocks(4,2) for the two
endpoints w and3w. A chain of r>=1 identities consequently satisfies

    S^(2r+2)(w)=S^2(tau(w)),
    S^(2r+2)(3w)=S^2(3tau(w)).                       (9)

Proof of composition: for one edge(9) is the padded version of(2) or(5).
If it holds for the next r-1 edges, apply S^(2r-2) to the first padded
identity, then use the inductive comparison. Absorption at1 makes padding
valid even if one of these finite paths has already reached1.

For any finitely supported integer vector c=(c_w), define

    N(c)_t=sum_(tau(w)=t) c_w,
    Gamma(c)=sum_w c_w C_w.                          (10)

Both signs and every multiplicity are retained. Equal terminal coefficients
are added, and only algebraically zero coefficients disappear. Equations(8)
give the exact source identity

    div Gamma(c)=sum_w c_w P(w)-sum_t N(c)_t P(t).   (11)

The normalizer is integer linear and idempotent, N^2=N. Its residual source
is explicit; a negative coefficient still requires the corresponding exact
pair current if that term survives.

There is also an order-independent whole-vector termination certificate.
Set

    Phi(c)=sum_w |c_w| w.                           (12)

If a nonzero coefficient k at parent w is replaced by k at its child u,
the triangle inequality gives

    Phi(new)-Phi(old)<=|k|(u-w)<0.                  (13)

Thus every sequence of nontrivial aggregate rewrites terminates. Every
rewrite preserves N(c); at termination all surviving indices are terminals,
so the final vector must be N(c). Its accumulated ordinary current may be
represented in different ways, but(11) remains exact. The supplied module
chooses a deterministic sum of per-index currents.

**Exact kernel scope.** Let V be the free integer module with basis e_w for
w in W5, and let R be generated by e_w-e_d(w) for exactly the guards(7).
Then V/R is the free integer module on the terminal indices, and

    c in R  if and only if  N(c)=0.                 (14)

Indeed each generator normalizes to zero; conversely telescoping each
finite chain writes c-N(c) as an integer combination of those generators.
If N(c)=0, Gamma(c) is a complete exact current for the requested source
without any supplied pair input. If N(c) is nonzero, no relation generated
by just(3),(6) removes it. This last statement does not exclude additional
ordinary arrows or identities outside this specified relation module.

## 3. Arbitrarily long words, with a complete positive parameter domain

Every finite word of the two inverse lifts has positive integer realizations.
Starting at a small child x, the inverse maps are

    I^(-1)(x)=(64x+5)/9,     II^(-1)(x)=(256x+45)/9. (15)

For a word of length r, write its composite as(Ax+B)/9^r, taking the labels
from the small child outward. Here A is a power of2. The single congruence

    Ax+B=0 mod9^r,       x=5 mod8                  (16)

is one complete positive progression modulo8*9^r. Final integrality implies
integrality at every inner stage: reduction modulo9^(r-1) cancels the outer
power-of-two coefficient, and induction repeats this argument. Each integer
stage remains5 modulo8. An integral inverse I imposes x=4 modulo9; inverse
II imposes x=0 modulo9, precisely the converse conditions in Section1.
Consequently every prescribed word really occurs, with the stated exact
currents and clocks. The initially chosen small child can itself be reducible;
(16) asserts the listed finite word, not a claim that its full chain ends there.

## 4. The whole R69 frontier cancels to one mandatory input

R69 supplies, for every H>=26, the complete positive CRT family

    v2(7153u+311195)=H,      u=13 mod81,
    w=(64u+5)/9.                                    (17)

Its already accepted R44 plan has the exact frontier

    P(u)+P(a)-P(b),
    a=(u-13)/72,       b=(32u-11)/81.               (18)

Write u=648c+13. The guard gives c=101 modulo128, so a=9c and b=256c+5.
Identity I applies to w with child u, and Identity II applies to b with
child a. The input u is terminal because u=437 modulo512 (in particular
u=53 modulo128). The input a is also terminal because a=13 modulo128.
Therefore

    N(e_u+e_a-e_b)=e_u,
    Gamma(e_u+e_a-e_b)=-C_II(b).                    (19)

In fact, if J_44 is the original full R44 current, the stronger row equality is

    J_44-C_II(b)=C_I(w).                            (20)

Here is a direct verification that keeps the absorption helpers. Write J_x
for the current part of the fixed formal absorption plan H_x, and
h=(81c+1)/2. The R41 recursion and elementary normalizers on this family give

    J_u=delta_u-delta_h-delta_(3a)+J_a,
    J_b=delta_b+delta_(48c+1)+delta_(36c+1)-delta_a+J_a,
    J_w=delta_w-delta_(3b)-delta_(1152c+23)+J_b.     (21)

The R44 upper comparison from3w to3u has current

    U=delta_(3w)+delta_(32u+3)+delta_(48u+5)-delta_(3u),
    J_44=U+J_u-J_w.                                (22)

Substitution of(21) into(22) yields(20) row for row, using
2592c+53=4u+1 and1728c+35=(8u+1)/3. Thus both lower pair obligations are
eliminated by an explicit current, rather than presumed known or dropped.
An exact supplied current only for P(u) completes P(w). This is a reduction
of the required input list of an already rho-valid rule, not new convergence
coverage or a resolution of P(u).

## 5. Finite compilation and stored checks

The [module](frontier_normal_form.py) exports bridge(w), normalize_pair(w),
normalize(coefficients), inverse_word(labels,index), and
compile_frontier(data,supplied). The final function verifies the complete
boundary and every nonzero supplied terminal current, including negative
terminal requests. Missing or malformed inputs are rejected.

Run the deterministic audit with

    python3 experiments/residual_progress/frontier_progress/check_frontier_normal_form.py

The [receipt](frontier_normal_form_audit.json) checks512 exact bridge instances,
4096 singleton normalizations,28 complete mixed-word families through32
listed edges,128 signed vectors,12 full R69 compressions through exact order256,
and6 complete R67 comparisons. It stores one entire input-free signed current
and one entire supplied-input conversion, with all input currents. These
finite checks support the implementation; Sections1–4 supply the universal
quantifiers. Ordinary absorption is searched only to prepare the explicitly
designated finite fixture inputs, with caps10000 arrows and4096 bits.
The normalizer itself searches no ordinary trajectory. Reachable dynamically
loaded local modules are included in the receipt's source hashes.

## 6. What this does not solve

For an R67 guarded input w, both w and its growing leading child v are53
modulo128. They are terminals for the two rules(7). The full R67 frontier is

    e_v+A_v-A_w,

where every index of a formal H_s request is strictly less than s. Since v>w,
every helper starts below v, and our normalization only decreases indices.
Thus N(e_v+A_v-A_w) retains the unique coefficient+1 at v. In particular

    Phi(N(e_v+A_v-A_w))>=v>w=Phi(e_w).              (23)

The same argument applies to each fixed finite repetition of that block.
Consequently even this exact whole-frontier cancellation does not make the
absolute-height potential(12) decrease on the R67 growth comparison. This is
a precise boundary of the present constructive mechanism. It leaves open
richer joint identities, another signed-frontier potential, or another rule
choice. A terminal pair in this normal form need not be a genuine unresolved
Collatz orbit; it is only unresolved by these two identities.
