---
id: arbitrary-target-linear-transport-barrier
kind: result
title: No finite constant bounds first-half transport into arbitrary target sets with a uniform o(X) error
status: written
claim: >
  Fix positive odd d with gcd(d,6) = 1; S_d the odd-only map (3n+d)/2^v2(3n+d) absorbed at 1; for odd n > 1
  let L_d(n) be its first odd iterate <= n/2 (any finite input-dependent time) and M_(d,X)(y) the number of odd
  n, 1 < n <= X, with L_d(n) = y. For every fixed odd h >= max(3,d) and every finite kappa >= 0 there is no
  function e(X) = o(X) such that sum_(y in A) M_(d,X)(y) <= kappa |A| + e(X) for all large X and every target
  set A in {odd y : h <= y <= X/2}; explicit one-arrow sources n = (2^a y - d)/3, a = 3..J, give excess
  (J - 2 - 3 kappa) t at X = 2^(J+1) t. For d = 1 only: no bound kappa |A| + o(X^alpha) holds uniformly for
  arbitrary targets with |A| <= 3X^alpha, nor for subsets of the fixed set {6 ceil(j^(q/p)) + 1}, alpha = p/q,
  whose counts are at most Y^alpha at every cutoff Y. With e = 0, the single target 5 (d = 1) and the
  nonabsorbing target 19 (d = 5) have unboundedly many one-arrow first-half preimages. A scoped barrier for this
  named method only: bounds in a global growth norm, weighted or B-specific estimates are not addressed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [baseline-obligation-transfer-controls]
certificates: [check_transport.py, p6_002_transport_check.py]
evidence:
  - "transport_audit.json: the receipt of check_transport.py: 150 general cases / 2,640 arrows, 12 exact linear gaps, 9 sparse cases, 227 hereditary counts / 864 arrows, two finite basin classifications and 11 rejection checks; exploratory first-passage searches distinguish complete cycles from an exhausted cap, which counts as unresolved"
  - "verification.json: the main lane's P6-002 gate record (full python3 scripts/verify_all.py --cpp --transfer-controls, exit 0, 117 report fields, checked source hashes); its three 'independent model reviews' were the main lane's own agents, not independent"
  - "p6_002_transport_check.py, p6_002_transport_check.json: the side lane's independent probe (under reviewed_by); it imports nothing from the main lane and passes at its new path"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: p6_002_transport_check.py
    scope: "Side-lane feed 2026-10-18 16:32, CONFIRMED label barrier at main de32608: 'The proof is correct and elementary.' The probe (nothing imported from main) checks the construction in 1,122 cases (d in {1, 5, 7, 13, 61}, J = 3..8, t <= 40: every n(a, y) odd and below X_t with v2(3n + d) = a, S_d(n) = y and 2y < n, all sources distinct, the exact counts N_t and |A_t|), brute force at 78 cutoffs (the full transported mass into A_t, computed by iterating every odd n <= X_t with cycles detected for d = 5 and 61, is at least N_t), the sparse count formula (15) for alpha in {1/2, 1/3, 2/3, 3/4} and every Y <= 3*10^4 with one-arrow preimages, and both singleton controls. Observation: a target y has about log2(X/y)/2 one-arrow first-half preimages up to X, so the natural transport weight is logarithmic; weighted and B-specific transport stay open. Recorded with its proof verdict; the status stays written under this migration's rule for main-lane work"
aliases: [P6-002]
tags: [convergence, phase6, stopping-time, transport, barrier, 3x-plus-d]
---

# No finite constant bounds first-half transport into arbitrary target sets with a uniform o(X) error

## Statement

The named method is to iterate first-half descent with a constant linear bound on the number of sources transported into **every** target subset, with an error uniform over those subsets and `o(X)`. The theorem in §2 below refutes that bound for every finite constant, already with one ordinary odd arrow; the sparse refinements of §2 (at `d = 1`) and the zero-error singleton controls of §3 sharpen it. It does not refute a bound restricted to the actual nonabsorbing set, weighted counting, or estimates that depend on the target's scale or arithmetic structure.

This is a Phase 6 **barrier** for route node S.2, [`universal-w5-quotient-stopping`](../../questions/universal-w5-quotient-stopping.md). The legacy note records that a search of the frozen research proofs and results index found no earlier first-half transport statement with these quantifiers; earlier fixed-depth barriers address different methods. This is not a novelty claim.

## Proof

### 1. Definitions and the exact exceptional-set recurrence

In this section use ordinary `d=1` Syracuse, absorbed at 1. All times count
odd-only arrows. For each positive odd `n>1`, put

```
ell(n) = min{j>=1 : S^j(n)<=n/2}, if this set is nonempty;
L(n)   = S^ell(n)(n), when ell(n) exists.
```

Let D be the domain of L, let `E={odd n>1:n not in D}`, and let B be the
positive odd seeds which never reach 1. State 1 is not a member of D, E or
B. It remains a possible **target** of L. These definitions must not be
replaced by treating the failure to half-descend from 1 as nonabsorption.

Every member of E belongs to B: if an odd `n>1` reaches 1, then `n>=3` and
`1<=n/2`, so a first-half descent exists. For `n in D`, n belongs to B iff
L(n) belongs to B, since the latter is an actual finite forward iterate.
Consequently there is an exact disjoint decomposition

```
B = E disjoint-union {n in D:L(n) in B}.                 (1)
```

For integer `X>=1`, define

```
M_X(y) = #{odd n:1<n<=X, n in D, L(n)=y},
B(X)   = #(B intersect [1,X]),
E(X)   = #(E intersect [1,X]).
```

Since `L(n)<=n/2`, (1) gives the exact counting identity

```
B(X) = E(X) + sum_(y in B, y<=X/2) M_X(y).              (2)
```

There is also a finite outer recursion for each individual `n in B`:
repeatedly apply L while it is defined. After r such applications the
current seed is at most `n/2^r`. Each seed stays in B and is at least 3.
Hence the iteration must end at a member of E after at most
`floor(log_2(n/3))` applications. The times spent in the individual
Syracuse prefixes are finite but can depend without bound on their inputs.
This decreasing outer recursion neither decides membership in E nor
supplies L at a seed where it is undefined.

Thus B is precisely the inverse closure of E under this partial map.
A density estimate for E alone does not bound its inverse closure. The
remaining sections test one specific proposal for controlling that closure.
They do not assume that B or E is nonempty for d=1.

### 2. The proposed transport inequality

For transfer, fix any positive odd d with `gcd(d,6)=1`, and let `S_d` be
the odd map `(3n+d)/2^v2(3n+d)`, absorbed at 1. Define `L_d` on odd `n>1`
by the same first-half rule, with arbitrary finite input-dependent time.
Use `M_(d,X)` for its multiplicity function.

Choose any fixed odd `h>=max(3,d)`. Consider the following proposed
estimate, with a fixed finite real `kappa>=0` and a function `e(X)`:

```
sum_(y in A) M_(d,X)(y) <= kappa*|A| + e(X)             (3)
```

for every sufficiently large integer X and **every** target set
`A subset {odd y:h<=y<=X/2}`, where `e(X)/X -> 0`. The same e must work
for all A at each cutoff. A may depend on X. Allowing h larger than any
fixed excluded target range is part of the statement.

**Theorem.** For every such fixed d and h, (3) is false for every finite
kappa. In particular it fails for d=1 even with target 1 excluded. No
assumption about unbounded trajectories, convergence or the supply of
missing currents is used.

#### Exact construction

Fix an integer `J>=3`. For an integer `t>=ceil(h/6)`, set

```
X_t = 2^(J+1)*t,
Y_t = 6t,
A_t = {odd y:h<=y<=6t}.                               (4)
```

Every y in A_t is at most `3X_t/2^J<=X_t/2`. For each
`a in {3,...,J}`, retain the y satisfying

```
y = d*(-1)^a modulo 3,
n(a,y) = (2^a*y-d)/3.                                 (5)
```

The congruence makes n an integer. Its numerator is odd, so n is odd.
Moreover

```
n(a,y)-2y = ((2^a-6)*y-d)/3 >= y/3 > 0,
n(a,y) <= (2^J*6t-d)/3 < X_t.                         (6)
```

Here `a>=3` and `y>=d` supply the first inequality. The exact valuation
identity

```
3n(a,y)+d = 2^a*y,       y odd                        (7)
```

gives `v2(3n+d)=a` and `S_d(n)=y`. By (6), that first arrow already crosses
the half threshold. Therefore `L_d(n(a,y))=y` at time 1. In particular the
absorber convention never changes these arrows, as both endpoints exceed 1.

Distinct pairs `(a,y)` give distinct n: (7) recovers a as the exact
valuation and y as the odd part. Hence all of these sources can be added
with their full multiplicities; they are not repeated counts of one seed.

#### Exact counts, without an unspecified remainder

Let `r_a in {1,5}` be the odd residue modulo 6 whose residue modulo 3 is
`d*(-1)^a`. Put

```
c_a = #{positive odd y<h:y=r_a modulo 6},
C_(d,h,J) = sum_(a=3)^J c_a,
H = (h-1)/2.                                          (8)
```

These are fixed nonnegative integers. They can be evaluated exactly by
`c_a=floor((h-1+6-r_a)/6)`. Each class `r_a mod6` has exactly t positive
members through 6t. Thus the construction supplies exactly

```
N_t = (J-2)*t-C_(d,h,J)
```

distinct sources landing in A_t, while

```
|A_t| = 3t-H.                                         (9)
```

It follows that

```
sum_(y in A_t) M_(d,X_t)(y) - kappa*|A_t|
 >= (J-2-3*kappa)*t + kappa*H-C_(d,h,J).               (10)
```

Choose `J>3*kappa+2`. The coefficient of t is positive. Dividing (10)
by `X_t=2^(J+1)t` gives a strictly positive limiting lower bound
`(J-2-3*kappa)/2^(J+1)`. This contradicts (3) and `e(X_t)/X_t -> 0`.
The same argument works along t restricted to powers of 2, so the
contradiction does not require every integer cutoff. This proves the
theorem. It does not prohibit an error of size `cX` with a fixed positive
c, or an error that depends on A without a uniform `o(X)` bound.

At d=1 and h=3 the formulas simplify to

```
H=1,
C_(1,3,J)=floor(J/2)-1,
N_t=(J-2)t-floor(J/2)+1,
|A_t|=3t-1.                                           (11)
```

For a completely integer parameterization, choose any integer
`m>=kappa`, put `J=3m+3`, and use

```
N_t-m|A_t| = t+m-floor(J/2)+1.                         (12)
```

This grows linearly with t. A finite constant multiplying arbitrary-set
cardinality cannot absorb the many available inverse valuation classes.

#### Sparse targets at the parent cutoff

The same exact construction gives a further scoped consequence. Fix a
rational `alpha=p/q` with integers `0<p<q`. For every sufficiently large
integer j, put

```
t_j=2^(pj),   J_j=(q-p)j-1>=3,   X_j=2^(qj).
```

These satisfy `X_j=2^(J_j+1)t_j` and `t_j=X_j^alpha`. At d=1,h=3, (11)
therefore gives target sets with

```
|A_j|=3X_j^alpha-1,
sum_(y in A_j) M_(1,X_j)(y)
 >= ((q-p)j-3)X_j^alpha-floor(J_j/2)+1.                (13)
```

Thus for every finite kappa no bound `kappa*|A|+o(X^alpha)` can hold
uniformly for arbitrary targets satisfying only `|A|<=3X^alpha` at the
parent cutoff. The displayed expression is the exact number of selected
one-arrow witnesses and a **lower bound** for the full transported mass.
There may be additional sources arriving after one or more arrows.

This particular construction does not cover a hereditary hypothesis such as
`#(A intersect [1,Y])<=C*Y^alpha` for every smaller cutoff Y: our A_j is
a dense initial odd interval and fails that condition for any fixed C as
j grows. The next construction addresses cardinality-proportional bounds
even under that hypothesis, while retaining a distinction from global
growth-norm estimates. Here J grows with j;
this sparse construction is distinct from the preceding fixed-J proof
against a uniform `o(X)` error.

#### A fixed target set with hereditary sparsity

Still at d=1, fix the same rational `alpha=p/q in (0,1)` and define the
infinite set

```
H_alpha={6*ceil(j^(q/p))+1 : integer j>=1}.              (14)
```

Its entries are strictly increasing: the increment of `j^(q/p)` between
consecutive positive integers exceeds 1. For any integer `Y>=1`, put
`m=floor((Y-1)/6)`. Then the exact count is

```
#(H_alpha intersect [1,Y])
 = max{integer j>=0:j^q<=m^p}
 = floor(m^(p/q)).                                    (15)
```

Indeed `ceil(j^(q/p))<=m` iff `j^q<=m^p`. Consequently this count is at
most `Y^alpha` at every cutoff, and is asymptotic to `(Y/6)^alpha` as Y
tends to infinity. The set contains only numbers 1 modulo 6, all at
least 7; in particular the absorber is excluded.

Fix `J>=4` and now take

```
A_X=H_alpha intersect [1,floor(3X/2^J)].               (16)
```

Every finite A_X inherits the bound `#(A_X intersect [1,Y])<=Y^alpha`
for **all** Y. For each y in A_X, every even `a in {4,...,J}` has the
required d=1 congruence in (5). Equations (6)–(7) again supply distinct
one-arrow first-half preimages. Therefore

```
sum_(y in A_X) M_(1,X)(y)
 >= (floor(J/2)-1)*|A_X|,
|A_X| ~ (X/2^(J+1))^alpha.                            (17)
```

Given any finite kappa, choose J once so `floor(J/2)-1>kappa`, and then
let X grow. The excess over `kappa*|A_X|` is bounded below by a positive
constant times `X^alpha`. Thus no uniform estimate
`kappa*|A|+o(X^alpha)` holds even for arbitrary targets with hereditary
count bound `#(A intersect [1,Y])<=Y^alpha` at every Y.

This still does not refute a bound expressed using the **global growth
constant**, for example `C' X^alpha` when
`sup_Y #(A intersect [1,Y])/Y^alpha<=1`, rather than using the actual
smaller quantity `|A_X|`. In (17), increasing J also decreases the
coefficient of `X^alpha` in `|A_X|`. Nor does it refute an estimate that
uses additional structure of the actual nonabsorbing set B.

### 3. Fixed singleton controls for the zero-error version

There are also simpler obstructions to (3) with `e=0`. For ordinary
Collatz, for every integer `j>=1` put

```
n_j=(10*4^j-1)/3.
```

Then `3n_j+1=5*2^(2j+1)`, so `L_1(n_j)=5` at time 1. The n_j are
strictly increasing positive odd integers and `n_1=13>2*5`. At cutoff
`X=n_m`, the fixed set `{5}` therefore has at least m distinct first-half
preimages. This disproves every constant zero-error multiplicity bound.
It does **not** by itself disprove an `o(X)` error; the stronger result in
Section 2 uses target sets varying with X to do that.

For the transfer control d=5, put

```
u_j=(38*4^j-5)/3,       j>=1.
```

Then `L_5(u_j)=19` at time 1, and

```
19 -> 31 -> 49 -> 19
```

is an exact nonabsorbing odd cycle, with valuations `(1,1,3)`. All u_j are
nonabsorbing, so here the singleton target is genuinely in the bad set.
This control does not assume a nonabsorbing target exists at d=1. These
two families test the asserted arrows and actual integer multiplicities;
they are not a generalized canonical-rank argument.

## Certificates

- [`check_transport.py`](check_transport.py) (under a second): `python3 areas/convergence/results/arbitrary-target-linear-transport-barrier/check_transport.py` verifies actual one-arrow paths, exact valuation bits, all source multiplicities, the floor counts, the `d = 1` specialisation, the singleton controls and bounded instances of (1)–(2), and compares with [`transport_audit.json`](transport_audit.json). Exploratory first-passage searches distinguish complete cycles from an exhausted cap; a cap is unresolved and fails any expected certificate. No finite scan proves a universal search terminates; the proof of the obstruction is the explicit construction and count above.
- [`p6_002_transport_check.py`](p6_002_transport_check.py) (about 7 s) is the side lane's independent probe, with receipt [`p6_002_transport_check.json`](p6_002_transport_check.json).

## Remarks

**What is excluded, and what remains open.**

The exact d=1 recurrence (2) motivates trying to combine a bound on E(X)
with an estimate that transports every small target set at uniformly
bounded linear cost. For example, a power-count induction of the form
`B(X)<=A X^alpha+kappa B(X/2)` would require `kappa<2^alpha` for its usual
geometric-series contraction. Section 2 refutes the stronger premise
(3) from which one might try to derive such an inequality for arbitrary
targets, for **all** finite kappa, regardless of alpha.

The theorem does not refute a proved estimate restricted to the specific
set B, whose arithmetic structure could matter. It does not establish
that B is nonempty for d=1, or prohibit variable weights, a coefficient
depending on the target scale, different source windows, cancellation of
signed currents, bounds in a global power-growth norm, or other
first-passage distributions. In particular, it
does not refute every possible recurrence with the numerical form above;
it refutes the named arbitrary-target route to that recurrence.

All counterexample arrows take one odd step. Allowing arbitrarily long
input-dependent histories is already compatible with the definitions and
does not change the counterexamples. The theorem is not a fixed-depth
catalogue limitation.

**Transfer status:** the uniform `o(X)` obstruction (3)–(12) holds for every
fixed d in the declared domain, with the displayed d-dependent congruence
and finite lower threshold. The sparse refinements (13)–(17) are stated
and checked here for d=1 only. Section 1 is also stated only for d=1;
the d=5 singleton is a separate exact negative control. This is proposed
as a **barrier**, not as a d=1-specific non-transfer step.

**Closest published discussion:** Tao explicitly explains in
[Section 1.1](https://arxiv.org/html/1909.03562v3#S1.SS1) why almost-all
descent statements cannot simply be concatenated: the transported measure
may concentrate in an exceptional target set. His
[Proposition 1.11](https://arxiv.org/html/1909.03562v3#S1.SS3) establishes
first-passage stabilization for specified logarithmic input distributions.
That result concerns different distributions and bounds and is not the
arbitrary-target estimate refuted here. This note supplies an elementary
explicit obstruction for (3); it neither re-proves Tao's result nor claims
to close S.2.

The next method tested at S.2 was a global power-growth norm: [`growth-norm-transport-barrier`](../growth-norm-transport-barrier/README.md). A premise restricted to the actual nonabsorbing set is the open [`bad-set-half-descent-transport`](../../questions/bad-set-half-descent-transport.md).

## History

Migrated from `experiments/phase6/stopping_transport/STOPPING_TRANSPORT.md` (legacy batch `P6-002`, route node S.2), with `check_transport.py`, `transport_audit.json`, `verification.json` and the side-lane probe `reviews/side_lane/p6_002_transport_check.py` with its receipt, at commit `be73a66`. ChatGPT main lane, 2026-10-18, pushed as `de32608`; the batch read the side lane at `ade50f97bf187003f25fbc4d9e5430b53d2f2527`. Programme label **barrier**, confirmed by the side lane at `602386ca` (feed 16:32). A final scope correction during the main lane's own review confined the sparse refinements to `d = 1`; only the main `o(X)` obstruction is asserted for every supported fixed `d`. The batch's secondary attempt (a congruence-closure separation, already covered by the frozen Monks sufficient-sets audit, now [`five-ray-profile-completion-suffices`](../five-ray-profile-completion-suffices/README.md)) was graded **none/redundant**; see [`universal-w5-quotient-stopping`](../../questions/universal-w5-quotient-stopping.md).
