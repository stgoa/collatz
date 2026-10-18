# Resolve or retain the unique fifth-family rank defect

**Status: written compatibility classification, complete local decision
tables, and an infinite family unresolved by the fixed fifteen rules.**
This concerns the original rank `rho=nu(3w)`. It does not combine the rho
and sigma inductions without checking their actual requests, and it does
not prove universal current supply. The arbitrary-second-exponent interface
is exact, but the closed table below covers only second exponents2 and3.

Use the absorbed odd Syracuse map, `P(w)=[3w]-[w]`, and the unchanged formal
absorption plan `[s]=div H_s+sum A_s(v)P(v)`. Requests retain their signed
integer coefficients. Dependencies are [R43](../critical_rank/CRITICAL_IMAGE_RANK.md),
[R44](../returning_phase/RETURNING_FORWARD_INTERFACE.md),
[R51](../phase_rank/PHASE_RANK.md),
[R52](../returning_continuation/RETURNING_SECOND_BLOCK.md),
[R58](../exact_absorption_bound/EXACT_ABSORPTION_BOUND.md), and
[R59](../deferred_rank/DEFERRED_RANK.md). The fixed resolver is the
[fifteen-family dispatcher](../refined_rules/REFINED_RULES.md) at d265d94.
It never calls the new rules here.

## 1. Precisely where sigma and rho can disagree

Write E for the returning class: `u=5 mod8`, `u=3 mod9`, and selected3u.
The definitions give the exact relation

    rho(u)=(9 sigma(u)+5)/8  on E;     rho(u)=sigma(u) outside E.       (1)

Take any finite exact sigma-valid plan for P(w), meaning every nonzero
request satisfies sigma(u)<sigma(w), including negative coefficients.

**Compatibility theorem.** If w belongs to E, the same plan is necessarily
rho-valid. If w is outside E, its entire nondecreasing-rho frontier consists
precisely of the requests u in E satisfying

    ceil((8rho(w)-5)/9) <= sigma(u) < rho(w).                         (2)

Proof: on E the affine map in(1) is strictly increasing. For an E parent,
E children therefore have smaller rho, and non-E children have
rho(u)=sigma(u)<sigma(w)<rho(w). For a non-E parent, non-E children also
decrease rho; for an E child, (1) gives exactly(2). This proves both
directions, without assuming signs positive or discarding requests. Later
children introduced by a rho rewrite need not themselves remain in E.

Thus sigma-valid rules with E parents can safely be used in a rho proof.
This does not license the reverse implication or arbitrary mixed rules.
For a general non-E parent, (2) is a complete description of the requests
that must be resolved or cancelled before the original-rho test succeeds.

## 2. Exact interface for every failed fifth-exponent input

R58 classifies the failure of its complete fifth-exponent plan. Every
failure has, for an integer j>=0,

    w=4021+8192j,       Q=rho(w)=12063+24576j,
    u=8589+17496j,      R=rho(u)=12883+26244j.                       (3)

Its unique request at rank at least Q is P(u), with coefficient+1. The
failure condition makes u an E input. Put

    3u+1=2^a t,    a>=3,    t odd,
    r=(3^(a-1)t-1)/2.

Then u=3 mod81 and

    2187Q=2^(a+10)t-4651,    sigma(u)=f<Q<R,                        (4)

where f is the original fifth-block endpoint. The R44 current C_u has
boundary P(u)-A_r+A_nu(u), and contains the actual ordinary prefix
`1^(a-2),2` from R to r, of length a-1, together with its two elementary
normalizers and final H terms. Substitute C_u for the coefficient+1 at u
in the original R58 plan. Every original request other than u has rank
below f<Q. Every request of H_nu(u) is also below Q, since nu(u)<u/4 and
the general bound is(9nu(u)+5)/8.

**Exact high-frontier identity.** The complete first substituted plan's
coefficients at ranks at least Q are exactly those of A_r at those ranks.
No cancellation with an omitted lower term is being assumed.

There is an equally complete second interface. Normalize r to n. If n=1,
stop; if n=1 mod8, take its ordinary arrow; otherwise take the entire
R26 block at n. Write y for its raw endpoint and retain the full R52
current D_u. Substitution gives high frontier exactly A_y restricted to
rho>=Q. This holds for every a and every second-run exponent, whether the
child-local rank test passes or fails. The returned current is always
finite and exact; `status` is determined against the original Q from the
full signed coefficients.

This is a finite arithmetic interface using already proved terminating H
construction. It is not a theorem that either choice always succeeds.
The elementary normalizers remain currents with their own clocks. In
particular, no single ordinary path is claimed for the entire P(w) plan.

## 3. Complete first decision when the defect has a=3

The a=3 defect class is exactly j=2 mod4. Its endpoint satisfies

    r=73543+118098k,    k>=0,
    Q=(16384r-33667)/19683.                                      (5)

**First-stage iff theorem.** The complete first plan is strict in the
original Q if and only if r is noncanonical or r=1 mod8.

If r is noncanonical, nu(r)<r/2 and every H_r request is at most
(9r+1)/16<Q for r>=73543. If r=1 mod8, its first ordinary arrow reaches
s=(3r+1)/4. Since r=1 mod3, s=1 mod3, so R58 bounds all H_s requests by
s: a canonical s cannot be its divisible-by3 exception, and a noncanonical
s has all requests below s. Again s<Q by(5). Otherwise r is complementary
canonical with r=1 mod3. Its critical W5 request has rank exactly r>Q,
coefficient+1, and cannot cancel against smaller auxiliary requests.

This includes the whole successful subdomain

    j=6 mod8,   w=53173+65536k,
    u=113565+139968k,    r=191641+236196k.                         (6)

Here r=1 mod4. In the r1-mod8 half use s=(3r+1)/4; in the r5-mod8
half elementary normalization gives a stronger bound. Uniformly all
requests have rank at most143731+177147k, below Q=159519+196608k by
15788+19461k. The fixed dispatcher selects R44 at u on this whole branch.

## 4. Complete second decisions for A=2 and A=3

Remain in the failed a3 first branch, so r is complementary canonical.
Write r=2^A v-1, with d=v2(3^(A-1)v-1)>=2, and let y be the complete
R26 raw return and n=nu(y). Its quotient length is A+floor(d/2)-1;
ordinary common-tail clocks are(A+floor(d/2),1) for odd d and
(A+d/2-1,0) for even d. Append the two-arrow R-to-r prefix and retain
the parent and pair normalizers separately.

The following are iff decisions for the **entire signed plan at the original
rank Q**, not merely decisions at the larger child rank R.

| A | d | Strict original-rho condition |
|---|---|---|
|2|odd|always|
|2|even>=6|always|
|2|2 or4|y selected|
|3|odd|always|
|3|even>=8|always|
|3|4 or6|y selected|
|3|2|y selected and either n=1 mod8, or n=3 mod8 with no R58 exception at n|

In the last row selected y with n=7 mod8 fails. The R58 exception means
exactly `n=27 mod48`, `v2(3n-1)=4`, and noncanonical3z for z=(3n-1)/16.

### Quantitative consequence of complete W9 elimination

If n=3b is canonical, b in W9, n>=75, and the R58 exception is absent,
then every request of H_n has rank at most

    (243n+511)/256.                                             (7)

Indeed R58's proof bounds every nonexceptional local W9 input by
c<=(27b+13)/32. Local W5 ranks are at most3c. A recursive W9 input c
has, by R43, ranks at most(27c+5)/8, yielding(7). The retained upper
requests at depths6 and8 have ranks(27n+23)/32 and(81n+101)/128,
both smaller than(7). Increasing their even depth by2 changes this rank
from L to(3L+1)/4, so all deeper upper requests are smaller as well.
The additional H_b terms
have bound(3n+5)/8. The exceptional depth4 request is absent by hypothesis.
This uses the existing finite W9 recursion, with no assumption about its
requested currents.

### Proof of the table, including intercepts

For odd d, increasing d by2 multiplies the raw endpoint formula by3/4.
The largest relevant endpoints occur at d3:

    A2: y=(9r-3)/32;        A3: y=(27r+3)/64.

Even the general rank bound(9y+5)/8 is below Q in(5). For even d,
increasing d by2 changes its affine formula from y to(3y+1)/4. The
initial exact formulas are

    A2,d2,d4,d6: (9r+5)/8, (27r+23)/32, (81r+101)/128;
    A3,d2,d4,d6,d8:
      (27r+19)/16, (81r+61)/64, (243r+247)/256, (729r+997)/1024.

All even endpoints are3 mod4 and1 mod3. If canonical, they have a leading
critical W5 request of rank y. In the indicated small-even rows y>Q;
at d6(A2) or d8(A3), y<Q and larger d only improve this. If y is
noncanonical it is selected, with n=(y-1)/2. The general bound
(9n+5)/8=(9y+1)/16<Q handles every selected row except A3,d2.

In that last row n=(27r+3)/32 is canonical and divisible by3. If n1mod8,
the forward bound(27n+29)/32 is below Q. If n7mod8, its W5 lead has
rank n>Q. If n3mod8, it is a W9 critical root. With the R58 exception
its unique lead(9n+5)/8 exceeds Q. Without that exception, (7) gives

    max rho <= (6561r+17081)/8192 < Q.

All displayed comparisons are strict linear inequalities for r>=73543;
the checker independently verifies their slopes and endpoint signs.
The high-frontier identity in Section2 proves necessity in each failed
row as well as sufficiency in each successful row. No lower request is
discarded. Higher A are supported by the exact interface, but no complete
closed table for them is asserted here.

Each (A,d) has a complete nonempty CRT cylinder. Take odd v with

    v=(1+2^d)*3^(1-A) mod2^(d+1),
    v=14495*2^(-A) mod59049.                                  (8)

The moduli are coprime. Then r=2^A v-1 has the required a3 parent phase;
take the positive representatives with r>=73543 and recover
j=(2r-28988)/59049. The modulus2^(d+1) retains the extra valuation bit.

## 5. A whole family that the fixed fifteen-rule expansion cannot resolve

For every k>=0 set

    w=44981+2^24 k,      u=96069+35831808k.                    (9)

The original fifth plan fails and has precisely the high coefficient+1
at u. The defect has returning exponent4, first endpoint

    r=243175+90699264k,

and a second block(A,d)=(3,2), with endpoint

    y=410359+153055008k,  nu(y)=205179+76527504k.              (10)

Here r is complementary canonical7 mod32, y=23 mod32 is selected, and
nu(y)=3 mod8. R44 fails at r; R52 fails its bound(9nu(y)+5)/8, which
is strictly above rho(u). R55's first(A,d)=(3,2) plan is the same failed
first plan; its special second option requires A2 and does not apply.

R59 expands that first plan's leading R41 input and obtains exactly
current zero and request `{u:1}`. This is R44's full-run inverse undo,
including the auxiliary H and normalizer terms, not just an endpoint
identity. The original source is then protected. The other selected
rules do not apply: u=3 mod81 excludes R56/R57/R60, and its R46 spine
has D=1,j=1. R41's strict row excludes u3mod9. The nonselected rules,
including R58, are excluded by selected3u. Thus the fixed fifteen
dispatcher returns None at u for **every** k.

Further accepted expansions of the smaller requests cannot introduce rank
rho(u)>Q, so cannot cancel its coefficient. The original fifth-plan
macro therefore remains unresolved under this fixed resolver. Some
parents w in(9) have another accepted rule; no exclusion of those is
claimed. If k=81l, every parent itself is also outside all fifteen direct
domains: w=26 mod81 fixes R45's k4 depth1 and R50's next depth2; the
k8 depth is0, w is not divisible by3, and first exponent5 excludes R53.
R48 and R58 fail by construction; all remaining parent rules require
selected3w. This proves a full old-fifteen-excluded subprogression.

This is a failure of the specified resolver and initial plan. In particular
it does not say that the new two-block interface, another inverse word,
supplied history, or later rules cannot handle some members. No positive
nonabsorbing orbit is asserted.

## 6. Reproduction

`defect_resolution.py` retains exact current dictionaries, signed request
lists, original-rank status, complete first/second parameters and the fixed
resolver identity. `compile_plan` rejects any high frontier or missing
supplied current. `fixed_resolution` delegates to the existing R43 finite
closure with a cutoff and protected source; it does not introduce a new
rewriting theorem or recursively assume the new rules.

Run `python3 experiments/residual_progress/defect_resolution/check_defect_resolution.py`.
The adjacent receipt records the bounded table/cylinder audits, full
unfinished counterfamily fixture, negative checks and exact supplied-current
demonstrations. Finite checks test implementations; the written argument
provides the stated infinite quantifiers. Universal completion is open.

The stored replay checks13 exact affine inequalities,76 sigma-valid plans,
192 nonexceptional W9 roots,64 complete a3 first decisions,544 second
A2/A3 cells, four large exact cylinders through depth129 and index2^128,
and90 arbitrary-A interfaces. It checks63 members of the complete success
and failure families,16 fixed-resolver instances, and nine invalid or
missing-supply calls. Four actual substitutions at53173,118709,85941 and
15224757 use21 distinct supplied pairs and yield92,52,65 and59 rows.
Full inputs and outputs are retained for53173 and15224757, together with
the complete unfinished44981 fixture. Fixture discovery has cycle
detection and caps10000 odd steps/512 bits; fixed closure has a10000-node
cap. A cap supplies no certificate. Source hashes and the frozen resolver
hash are replayed by default.
