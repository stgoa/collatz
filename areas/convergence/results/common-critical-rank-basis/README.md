# A common decreasing compiler by retaining both critical pair types

**Status: written conditional compilation theorem and finite exact certificates.**
Every old sigma-valid W5 plan can be translated into a rho-valid plan in the
larger W5 union W9 source basis. Every old rho-valid W5 plan remains valid
without changes. The translation preserves all signs and retains missing
inputs; it does not make the original conflicting edges rho-valid unchanged.
The complete R67 guard then has a decreasing rule with an explicit W9 input.
This changes the induction universe and rule-selection policy. It adds no
coverage to the unchanged seventeen-family W5-only dispatcher and supplies
no universal currents. Collatz remains open; no novelty or formal-verification
claim is made.

Dependencies are the [critical bijection and formal plans](../tripling_equivalence/TRIPLING_EQUIVALENCE.md),
[complete W9 interface](../w9_closure/CRITICAL_NINE_ELIMINATION.md),
[critical-image rank](../critical_rank/CRITICAL_IMAGE_RANK.md),
[separate sigma rank](../phase_rank/PHASE_RANK.md),
[returning inverse](../critical_inverse/CRITICAL_INVERSE.md),
and [R67 mixed block](../mixed_rank_recursion/MIXED_GROWING_BLOCK.md).
The new proof combines these established source identities; it does not
import an external convergence result.

## 1. Keep the complete critical source basis

Use positive odd Syracuse S, absorbed at1, and killed atoms [1]=0. Define

    P(w)=[3w]-[w],
    W5={w>0:w=5 mod8},  W9={w>0:w=9 mod16},  W=W5 union W9,
    rho(w)=nu(3w).                                      (1)

R37 proves that rho bijects W onto the complementary canonical roots not2
modulo3. In particular rho(b)=3b on W9; on W5 it is3w if3w is canonical,
and(3w-1)/2 if3w is selected. Always w<rho(w)<=3w.

Write the original R37 formal absorption plan as

    [s]=div J_s+sum_v A_s(v)P(v),  v in W.               (2)

This is a finite arithmetic construction, with every requested pair retained.
It does not assert absorption of s. Its complete bound is

    A_s(v)!=0  implies  rho(v)<=nu(s).                   (3)

Indeed every step first normalizes the current state and then either takes
a strictly smaller ordinary successor, a strictly smaller inverse predecessor,
or requests its critical pair and continues from the smaller pair index.
The rank of a requested pair is exactly that step's canonical state. The
initial canonical state is nu(s), and all subsequent states are smaller.
This also proves finite termination of(2). There is no forced W9 elimination
and hence no9/8 inflation in(3).

This source universe is not a stronger universal existence assertion:
currents for every W imply currents for every W5 by restriction, while
currents for every W5 imply currents for W9 by R40's finite conditional
elimination. Both universal assertions are equivalent to Collatz by R37.
Their **ranked induction hypotheses differ**. A W9 input below the current
critical rank cannot simply be replaced by any W5 plan that requests a
higher critical rank.

## 2. Every returning W5 input has a smaller critical-nine interface

Let E be the complete returning domain: u in W5, u=3 modulo9, and selected3u.
Set

    q=(3u-1)/2=rho(u),
    n=(4u-3)/3=sigma(u),
    b=n/3=(4u-3)/9 in W9.                             (4)

Here n is canonical and27 modulo96, q is canonical, and n<q. The exact
ordinary path is

    n --(1)--> (3n+1)/2 --(2)--> q.                   (5)

Let G_n be its two-row path current, and let N_(3u) be the elementary
normalizer with divergence [3u]-[q]. With the critical plans(2), define

    C_u=N_(3u)-G_n+J_b-J_u,
    c_u={b:1}+A_b-A_u.                               (6)

**Theorem.** For every u in E,

    P(u)=div C_u+sum_v c_u(v)P(v),                    (7)
    c_u(b)=1,  rho(b)=n=sigma(u)<rho(u),
    c_u(v)!=0 and v!=b  implies  rho(v)<n.            (8)

**Proof.** Combining boundaries in(6) gives

    div C_u=[3u]-[q]+[q]-[n]+[b]-[u]
               -sum_v(A_b(v)-A_u(v))P(v),

which is(7) because n=3b. By(3), all A_b requests have rank at most nu(b)<=b<n.
Since u is5 modulo8, nu(u)<=(u-1)/4<n, so every A_u request also has rank<n.
Thus none cancels the direct coefficient+1 at b. Formula(5) follows by direct
substitution and the exact phase u=5 modulo8. Its endpoints are positive,
and all normalizer and H rows remain in(6). No unknown absorption is used. □

Only the inverse comparison in(5) has the stated two-arrow clock. The full
conditional current also contains normalizers and formal absorption currents;
it must not be labelled a two-arrow merger between3u and u.

## 3. Translate the whole sigma rule collection into one rho induction

Suppose a finite old W5 plan has exact source

    P(w)=div C+sum_u c(u)P(u),
    sigma(u)<sigma(w) for every nonzero signed c(u).  (9)

Its parent w can be inside or outside E. Replace each returning child u in E
once using(7), multiplied by its full signed integer coefficient c(u).
Keep each nonreturning child unchanged. Add equal request coefficients only
after all substitutions; discard only exact zeros.

**Translation theorem.** The resulting finite current and critical requests
have the same source P(w), and every nonzero request v satisfies

    rho(v)<sigma(w)<=rho(w).                         (10)

For a nonreturning child, rho(u)=sigma(u). Every returning child's replacement
has rank at most sigma(u), by(8). These facts prove(10), including negative
coefficients. Combining equal requests cannot introduce a higher index.
The translation performs finitely many complete substitutions, each with two
finite critical H plans. It never emits the discarded high-rho returning child
as an induction premise. Returning helpers of smaller rho may remain: they
are legitimate W inputs and require no recursive translation to prove(10).

Every old rho-valid W5 plan is already a plan in W, with exactly the same
current and request vector. Therefore all those old rho plans and all
**translated** sigma plans can be used in a single strict-rho compiler.
This does not claim that all original sigma edges and rho edges decrease
one rank unchanged. The high sigma edge was replaced by a different exact
conditional current.

As a concrete check, the old rho rule at4629 retains P(2197) with rank6591,
below rho(4629)=6943 but above sigma(4629)=6171. It remains a valid rule here.
It is correctly rejected as an input to the sigma translator. Thus this
compiler does not discard useful old rho rules merely to impose sigma on
the original W5 universe.

### Finite conditional closure

A rule-selection policy may return any finite exact plan whose critical
request ranks strictly decrease, or stop at an explicitly unresolved input.
Recursive expansion under this policy terminates as a finite conditional
plan: use induction on the positive integer rho, with finite branching at
every rule. All signed multiples of child currents are added, and all signed
request coefficients are retained. The result can still have a nonempty
terminal frontier. Terminating formal expansion does not supply that frontier.

A supplied-current compiler checks every terminal pair's exact boundary,
including pairs with negative coefficients, before substitution. Missing or
incorrect supplies are rejected. Optional resource caps reject the computation;
they do not certify any remaining input. This gives an executable common-rank
interface, not a universal rule selector or a convergence proof.

## 4. Exactly which W9 local branch remains blocked

For b in W9, retain the full critical requests in R40's local plan rather
than recursively eliminating every W9 request. Its only possible request
with index at least b is u=4z+1, with3z noncanonical, at d=v2(9b-1) in{4,6,8}.
Every other request v<b has rho(v)<=3v<3b=rho(b). The three exceptional
critical ranks, including offsets, are

| d | u | rho(u) |
|---|---|---|
| 4 | (9b+3)/4 | (27b+5)/8 |
| 6 | (27b+13)/16 | (81b+23)/32 |
| 8 | (81b+55)/64 | (243b+101)/128 |

For all b>=9 the d6 and d8 ranks are strictly below3b, since15b>23 and
141b>101. The d4 rank is strictly above3b. Thus the **entire** local W9
classification is: accept all branches except d4 with noncanonical3z;
in that branch retain the single higher request P(u), coefficient+1, as
unresolved and reject it as a decreasing rule.

The blocked d4 inputs are in exact bijection with E via(4):

    b -> u=(9b+3)/4,       u -> b=(4u-3)/9.           (11)

Indeed d4 gives z=(9b-1)/16 and u=4z+1; noncanonical3z is equivalent to
selected3u. Also u=3 modulo9. Conversely every u in E gives d4 and precisely
these phases. This is the unresolved return between the two source types.

Substituting(7) for the higher P(u) in this blocked W9 plan does not prove
progress. It returns the exact form

    P(b)=div K+P(b)+sum_(rho(v)<rho(b)) e(v)P(v).    (12)

The coefficient of P(b) is always+1. All old nonexceptional requests and
all helpers introduced by(7) have strictly lower rank, so none can cancel it.
The compiler rejects this self-request.

**The remaining lower identity need not be zero.** For u21,b9, K=0 and the
only request is P(9). But u453,b201 gives exactly

    requests={201:1,5:1,25:1},
    K=delta_5+delta_11+delta_13+delta_17+delta_19+delta_25+delta_29
       -delta_15-delta_23-delta_35-delta_53-delta_75-delta_85-delta_113.

Its divergence is -P(5)-P(25), as required by(12). The fourteen-row certificate
is stored and checked. Thus a universal row-for-row zero-current undo would
be false; the universal self-request statement is the sufficient obstruction.

## 5. The entire R67 guard has a decreasing rule in this basis

For every positive

    w=40529845 mod2^26,
    q=3w,   f=(729w+147)/256,   b=f/3=(243w+49)/256,  (13)

one has b in W9, f canonical, and w<f<q=rho(w). The first five ordinary
arrows from q have word(1,1,1,1,2) and end at F(f). Add the sibling current
delta_(F(f))-delta_f to obtain a finite comparison D_(q,f) with boundary
[q]-[f]. Its ordinary common-tail clocks are(6,1), and its canonical quotient
length is5. These clocks refer to q and f, not to the full pair current.

Use the critical H plans directly:

    C_G=D_(q,f)+J_f-J_w,
    P(w)=div C_G+sum_v(A_f(v)-A_w(v))P(v).           (14)

Because f=3b is canonical, its first critical request is P(b), followed by
H_b. Thus the complete frontier is

    {b:1}+A_b-A_w.                                  (15)

The leading request has rho(b)=f<3w. Every other request has rank at most
max(nu(b),nu(w))<f. This is a complete decreasing rule on the whole guard,
conditional on smaller **critical-basis** inputs.

In the old W5-only formal H_f expansion, the leading W9 input was eliminated
in favour of

    u=(3f+3)/4=(2187w+1209)/1024,
    rho(u)=(6561w+2603)/2048>3w.                     (16)

Its d4 elimination violates the new rho policy at b, and cannot be inserted
as a decreasing rule. Translating the old sigma plan also retains b with
coefficient+1 and only lower-rank helpers; the implementation checks both
constructions. Their lower currents need not be identified or discarded.

This explains the tactical distinction. R67 exhibited growth after two
particular choices of differently ranked plans; following both choices was
not required to prove the original source. Keeping its smaller W9 obligation
avoids that forced detour. The W9 obligation has not been solved: it is an
explicit earlier input in the enlarged induction, and its blocked branch is
exactly(11). Focusing only on eliminating the later growing R67 pair would
impose an unnecessary extra requirement on every possible constructor.

## 6. Executable interface, evidence, and remaining work

[critical_basis.py](critical_basis.py) exports:

- absorption_plan: finite critical H_s with bound(3);
- returning_conversion: the complete E interface(6);
- translate_sigma and retain_rho: the two justified imports;
- nine_candidate and blocked_nine: complete W9 rank classification and the
  self-request after attempted return;
- guarded_plan: the whole guard rule(14);
- validate, close_plan and compile_plan: exact signed boundaries, strict rank,
  conditional closure and checked supplied-current substitution.

The old dispatcher and old stored plan tables are unchanged. This module
defines no universal source-supply procedure. To make the enlarged induction
universal, decreasing valid rules or exact base certificates must still cover
every retained critical input, including the blocked W9 family. Previously
proved rho rules may be selected at W5 nodes; translated sigma rules may also
be selected. A prospective W9 rule must pass its own original-rank test.

Run the bounded audit from the repository root:

    python3 experiments/residual_progress/critical_basis/check_critical_basis.py

The [receipt](critical_basis_audit.json) checks512 critical H plans,
256 complete E conversions and their retained self-requests,512 W9 local
classifications,116 sigma translations from a declared256-input window,
32 unchanged old rho plans, and8 whole-guard cases with binary depths through159.
It also checks a negative E request with coefficient-3, the4629 incompatibility,
the453/201 nonzero undo, and a finite conditional closure with unresolved W9
leaves. Three complete supplied-current conversions retain all original inputs
and output tables. Invalid currents, missing supplies, false self-descent,
expanding W9 plans, wrong parents, Boolean coefficients/caps and exhausted
resource caps are rejected.

The only ordinary absorption searches prepare those designated finite fixture
inputs, with10000-arrow and4096-bit caps and cycle detection. The theorem and
symbolic compiler do not search for unknown absorption. The receipt pins every
reachable dynamically imported local source, including modules absent from
sys.modules. Universal quantifiers come from the written arguments above;
the finite receipt checks the implementation and its exact examples.
