# Critical-image rank permits larger pair indices

**Status: written bound and conditional composition theorem.** A larger pair
index need not block induction. The useful rank is the associated canonical
critical root. This does not supply a rule on every root or prove Collatz.

Use killed atoms at1 and odd-only Syracuse S. Write

```
P(w)=[3w]-[w],     rho(w)=nu(3w),
W5={positive w: w=5 mod8},     W9={positive w: w=9 mod16}.
```

R37 proves that rho bijects W5 union W9 onto the complementary canonical
roots not2 modulo3. For W9, rho(w)=3w. For W5 it is3w when3w is
canonical, and(3w-1)/2 when3w is selected. Thus w and rho(w) can order
two inputs differently.

## 1. Rank bound for complete W9 elimination

Every W5 request u in R40's finite `five_plan(w)`, w in W9, satisfies

```
8*rho(u) <= 27w+5 = 9*rho(w)+5.                       (1)
```

To prove this, first use the complete local R40 classification. Every
nonexceptional request u<w has rho(u)<=3u<3w. The exceptional request is
u=4z+1 with3z noncanonical, so3u is selected and rho(u)=6z+1. The exact
three cases are:

| d=v2(9w-1) | u | rho(u) |
|---|---|---|
|4|(9w+3)/4|(27w+5)/8|
|6|(27w+13)/16|(81w+23)/32|
|8|(81w+55)/64|(243w+101)/128|

The d6 and d8 ranks are strictly below3w for every w>=9, even though
their pair indices exceed w. Only d4 increases the critical rank.
All W9 children have smaller index. Apply strong induction to these children;
their bounds(27u+5)/8 are smaller than the parent's bound. Retain all signed
coefficients and cancellations. This proves(1) for the fully expanded plan.

## 2. Rank bound for a formal absorption input

The finite W5-only absorption plan of R41 for any positive odd seed s has
current H_s and signed coefficients a_s(u) satisfying

```
div H_s=[s]-sum a_s(u)P(u),
a_s(u) nonzero  =>  rho(u)<=(9s+5)/8.                 (2)
```

Indeed each directly requested W5 index has critical root at most s,
because the R37 seed decreases at every step. Each W9 request b similarly
comes from a critical root3b<=s. Replacing it by(1) gives rho(u)<=
(27b+5)/8<=(9s+5)/8. Signed cancellation cannot introduce a larger index.
This is an input bound; H_s still requires its missing pair currents.

In particular, if p is a complementary canonical root and v its critical
pair index, then v<=(2p+1)/3 and every absorption input for v obeys

```
rho(u)<=(9v+5)/8<=(3p+4)/4<p                         (3)
```

for p>4. If p2 modulo3, its free inverse descent goes to(2p-1)/3 and
the same strict bound holds. This is why a bridge to a smaller canonical
root can be used even when its new pair index exceeds the old one.

## 3. A common induction and a finite conditional compiler

Let A be any subset of W5 for which a specified rule supplies a finite
integer current J_w and finitely many signed integer requests c_w(u), with

```
div J_w=P(w)-sum c_w(u)P(u),
c_w(u) nonzero  =>  u in W5 and rho(u)<rho(w).         (4)
```

Then universal exact currents on W5 minus A suffice for Collatz. Strong
induction on the positive integer rho(w) supplies each omitted input using
(4), after which R40 and R37 apply. The converse follows from absorption.
Finite unions of rule domains can use any fixed priority: every chosen rule
strictly decreases the same rank, regardless of whether its pair index grows.
This is a sufficient-set theorem with explicit missing premises.

For any one starting pair, recursively substituting(4) terminates: the
branching is finite and the positive integer rank strictly decreases on
each expanded edge. Unhandled inputs remain leaves. Opposite coefficients
are combined exactly; signs or multiplicities must not be dropped. Supplying
all remaining exact leaf currents yields an exact current for the start.
Neither mathematical termination of this formal expansion nor any finite
sample proves that every leaf can be supplied.

`rank_closure.py` implements the bounds and this generic compiler. It checks
every rule's exact divergence and strict rank. Nondecreasing or malformed
rules are rejected, including a tautological self-request. An optional
resource cap rejects the computation rather than turning a leaf into a
certificate. Missing or incorrect actual inputs are rejected on substitution.

The existing R41 E_good rule is compatible with this rank: its child has
critical image p<q=rho(w), (3) handles the child's absorption input, and
nu(w)<=(w-1)/4 gives a strictly smaller rank for the other absorption input.
The returning E row still fails(4). Its self-request cannot be made smaller
by renaming the rank.

## 4. Executable union of the proved rules

`rules_union.py` chooses, in order, R41 E_good, the R45 nonselected base
phase, the accepted R44 returning forward interface, and the R46 inverse
escape. Each selected rule is checked against (4). The accepted domains
are specified in their proof notes, with the R44 rational bound retained
as its sufficient test. Let A be this union. Universal currents on W5
minus A suffice by Section3; every other requested current remains an
explicit premise. A rejected sufficient test is not a nonexistence result.

The finite mixed example w749 expands five rule instances across R41,
R45 and R46 and retains two leaf currents. Both supplied currents and the
final table are stored. At w1029, R44 and R46 compose and their signed
requests cancel completely, giving an exact current with no supplied
inputs. These are finite examples of the compiler. The unresolved P21
self-request is still rejected; its rank has not changed.

Run `python3 experiments/residual_progress/critical_rank/check_rank_closure.py`.
The [receipt](critical_rank_audit.json) checks2048 full W9 reductions,
4096 absorption bounds, the three exceptional affine rows, and all1024
W5 candidates below8192. Of those,195 have an accepted rule and58 expand
using more than one rule. Seven actual substitutions, including an empty
input set, verify final divergence. Missing/bad inputs, incorrect boundaries,
non-W5 children, a self-request and a resource cap are rejected. Input
path discovery is confined to bounded demonstration fixtures; it is absent
from the constructors. These counts do not estimate asymptotic coverage.

## Dependencies and scope

- [R37 critical domain](../tripling_equivalence/TRIPLING_EQUIVALENCE.md).
- [R40 complete W9 elimination](../w9_closure/CRITICAL_NINE_ELIMINATION.md).
- [R41 absorption compiler and returning branch](../critical_inverse/CRITICAL_INVERSE.md).

The common rank allows genuine intermediate increases in the pair parameter.
It does not repair every expanding branch: d4 exceptions in R40 still increase
rho, and the exact returning loop remains a loop. No universal construction,
new annular mass fraction, or novelty claim is supplied.
