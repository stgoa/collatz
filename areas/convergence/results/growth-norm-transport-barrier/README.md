---
id: growth-norm-transport-barrier
kind: result
title: First-half transport cannot contract any power-growth norm on arbitrary targets, although its one-arrow part does
status: reviewed
claim: >
  Fix positive odd d with gcd(d,6) = 1; S_d = (3n+d)/2^v2(3n+d) on positive odd n, absorbed at 1, odd-arrow
  clock; L_d(n) the first iterate <= n/2 (any finite time); G_d(A) = {odd n > 1 : L_d(n) in A}; ||A||_alpha =
  sup_X #(A cap [1,X])/X^alpha (possibly infinite). (Theorem 1, d = 1) The one-arrow part Q(A) = {odd n > 1 :
  S_1(n) in A, 2S_1(n) <= n} satisfies ||Q(A)||_alpha < (10/13)||A||_alpha for every real 4/5 <= alpha < 1 and
  nonempty A of finite norm. (Theorem 2) For every supported d and real 0 < alpha <= 7/8 the fixed set
  {18 ceil(j^(1/alpha)) + 5d} has norm 18^(-alpha) and ||G_d(A)||_alpha >= K(alpha)||A||_alpha > (241/240)||A||_alpha,
  via the four exact first-half words (3), (5), (2,3), (1,5). (Theorem 3) For every supported d and real
  0 < alpha < 1 some fixed infinite A of finite positive norm has ||G_d(A)||_alpha > ||A||_alpha; hence no bound
  G_d(A)(X) <= kappa ||A||_alpha X^alpha + o(X^alpha) with kappa <= 1 holds for every finite-norm A, even with an
  A-dependent error. A scoped barrier for arbitrary targets only: whether ||G_d(A)||_alpha is finite is undecided,
  and estimates restricted to the actual nonabsorbing set, other norms or signed cancellation are not addressed.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [fixed-factor-stopping-explicit-constants, arbitrary-target-linear-transport-barrier]
certificates: [check_growth_norm.py, check_all_exponents.py, p6_003_growth_norm_check.py]
evidence:
  - "growth_norm_audit.json, all_exponents_audit.json: the receipts of the two checkers (1,920 four-word paths, 10,752 one-arrow norm checks, 276 independently enumerated small code words, 1,752 raw residue seeds, 390 inverse paths and residue counts, two exact large code masses at total valuation budgets 48 and 80 for alpha 19/20 and 99/100, two S.1 feed records, 29 rejections); the two large masses were also recomputed by the main lane with a separate dynamic program"
  - "verification.json: the main lane's P6-003 gate record (full python3 scripts/verify_all.py --cpp --transfer-controls, exit 0, 118 report fields, pinned report and checked sources); its 'independent model review' was the main lane's own agents, not independent"
  - "side_lane_review_e4f8231.json: the main lane's reproduction (2026-10-18) of the unmodified side-lane probe at side commit e4f82311 (source sidekick/probes/p6_003_growth_norm_check.py) in temporary storage under a 45 s cap: 27,773 target cases and 120,000 exact count comparisons, receipt matching byte for byte. Scope as recorded: 'Independent side probe reproduced unmodified in temporary storage; finite checks support the separately written proof. No universal Collatz conclusion.' A main-lane reproduction of a side-lane probe, not a review of this node"
  - "p6_003_growth_norm_check.py, p6_003_growth_norm_check.json: that side-lane probe (under reviewed_by); it imports nothing from the main lane and passes at its new path"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: p6_003_growth_norm_check.py
    scope: "Finite only (side-lane feed 2026-10-18 16:56, CONFIRMED label barrier at main 2e619a2; nothing imported from main): the four paths for d in {1, 5, 7, 13, 61} and every y = 5d (mod 18) below 10^5, 27,773 targets (exact words (3), (5), (2,3), (1,5), first-half descent to y at times 1, 1, 2, 2, all four distinct); the four integer inequalities (9) and 241/240, with K(alpha) on a grid (1.059 at 7/8, 1.023 at 0.9, 0.954 at 0.95, so Theorem 3 is needed near alpha = 1); the count formula (5) exactly for alpha in {1/2, 2/3, 7/8}, d in {1, 5}, every X <= 2*10^4, with integer roots; Theorem 3's mass bound by an exact dynamic program (p_90 = 0.99772, above 1 - delta_m - 2^(-L) for every split m = 9..15 of B = 90; for alpha = 0.9, p_B exceeds 2^(alpha-1) at B = 30) and the identity behind (15) termwise. The written proofs were not re-derived in the feed entry; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Theorems 1-3 re-derived line by line (constants, the four exact paths for d in {1, 5, 7, 13, 61} below 60000, first-crossing code masses p_48, p_80, p_90 by an independent DP, the inverse congruence (14) on 590 word/d cases, the count formulas); three certificates re-run (exit 0, 1.2 s). Verdict HOLDS; two imprecisions (Theorem 2 holds up to alpha about 0.9162, the exclusion of target 1 comes late in section 4), no correction to the claim"
aliases: [P6-003]
tags: [convergence, phase6, stopping-time, transport, growth-norm, barrier, 3x-plus-d]
---

# First-half transport cannot contract any power-growth norm on arbitrary targets, although its one-arrow part does

## Statement

The named method is a contraction of the ordinary power-growth norm under first-half transport for **every** target set. The one-arrow suboperator does contract this norm (Theorem 1). Four explicit paths of at most two odd arrows show expansion through `alpha = 7/8` (Theorem 2). A finite-cylinder argument extends the obstruction to every real `0 < alpha < 1` (Theorem 3). This supplies the global-growth-norm obstruction that [`arbitrary-target-linear-transport-barrier`](../arbitrary-target-linear-transport-barrier/README.md) left outside the scope of its cardinality comparison.

This is a Phase 6 **barrier** for route node S.2, [`universal-w5-quotient-stopping`](../../questions/universal-w5-quotient-stopping.md). It uses the S.1 calibration [`fixed-factor-stopping-explicit-constants`](../fixed-factor-stopping-explicit-constants/README.md) inside an actual S.2 attempt (equation (12)), as the programme's rule D6 required. No novelty or convergence claim is made.

## Proof

### 1. Definitions and quantifiers

Fix a positive odd integer d with gcd(d,6)=1. On positive odd integers use
S_d(n)=(3n+d)/2^v_2(3n+d), with 1 absorbed. For odd n>1, let L_d(n) be the
first iterate S_d^j(n)<=n/2, j>=1, when such an iterate exists. The clock
counts ordinary odd-only arrows. The definition allows arbitrary finite
input-dependent times; the witnesses below require at most two arrows.

For A contained in the positive odd integers greater than 1, write

```
A(X)       = #{y in A:y<=X},
||A||_alpha = sup_(integer X>=1) A(X)/X^alpha,
G_d(A)     = {odd n>1:L_d(n) exists and L_d(n) in A}.
```

The norm is allowed to be infinite. All contraction proposals below assume
the input norm is finite. For noninteger cutoffs A(u) means A(floor(u)).
State 1 is excluded from the target sets used here. It remains an allowed
first-half endpoint in the underlying map.

For d=1 define the one-arrow part

```
Q(A) = {odd n>1:S_1(n) in A and 2 S_1(n)<=n}.
```

Then Q(A) is a subset of G_1(A). An upper bound for Q does not bound G_1.

### 2. The one-arrow operator contracts

**Theorem 1.** For every real 4/5<=alpha<1 and every nonempty A with
finite norm,

```
||Q(A)||_alpha < (10/13) ||A||_alpha.                 (1)
```

For empty A both norms are zero, so the corresponding non-strict
inequality holds.

**Proof.** An arrow n->y with y>1 half-descends precisely when its exact
valuation a is at least 3. Indeed n=(2^a y-1)/3, and 2y<=n is equivalent
to (2^a-6)y>=1. Integrality requires y=5 mod6 for odd a, and y=1 mod6 for
even a. Let A_5 and A_1 be these two disjoint parts of A, and put Z=3X+1.
Pair a=2b+1 with a=2b+2, for b>=1. Exact valuations distinguish all sources,
so

```
Q(A)(X)
 = sum_(b>=1) [ A_5(Z/(2*4^b)) + A_1(Z/(4*4^b)) ]
 <= sum_(b>=1) A(Z/(2*4^b))
 <= ||A||_alpha Z^alpha 8^(-alpha)/(1-4^(-alpha)).    (2)
```

There is no Q source below 13: the smallest permitted odd-a source is
13->5, and the smallest even-a source is 37->7. Thus for X<13 the left
side is zero. For X>=13, Z/X<=40/13, and (2) implies

```
||Q(A)||_alpha <= (40/39)^alpha K_1(alpha)||A||_alpha,
K_1(alpha) = (3/8)^alpha/(1-4^(-alpha)).             (3)
```

For alpha>=4/5, (3/8)^alpha<1/2 because 3^4<2^7,
and 4^(-alpha)<1/3 because 3^5<4^4. Consequently K_1(alpha)<3/4.
Since alpha<1, (40/39)^alpha<40/39. Their product is strictly less
than (3/4)(40/39)=10/13, proving (1). These inequalities hold for every
real alpha in the stated interval, not only for checked rational samples.

### 3. Four paths force expansion for the full operator

**Theorem 2.** For every supported fixed d and every real
0<alpha<=7/8 there is a fixed infinite target set A_(alpha,d) with finite
norm such that

```
||G_d(A_(alpha,d))||_alpha
 >= K(alpha)||A_(alpha,d)||_alpha
 > (241/240)||A_(alpha,d)||_alpha,                   (4)

K(alpha) = (3/8)^alpha + (3/32)^alpha
           + (9/32)^alpha + (9/64)^alpha.
```

The conclusion allows the output norm to be infinite; it does not decide
whether that norm is finite, nor identify the full operator norm.

#### A fixed target set with an exact norm

Set

```
A_(alpha,d) = {18 ceil(j^(1/alpha))+5d : integer j>=1}.
```

Since alpha<1, these terms are strictly increasing. They are odd, exceed
5d, and are 5d modulo 18. For every integer X, put
m=max(0,floor((X-5d)/18)). Then

```
A_(alpha,d)(X) = floor(m^alpha).                    (5)
```

For X>=1 this is at most (X/18)^alpha. Moreover,
A_(alpha,d)(X)/X^alpha tends to 18^(-alpha). Hence

```
||A_(alpha,d)||_alpha = 18^(-alpha).                 (6)
```

The count (5) and limit use real powers in the proof. The checker uses
integer-root comparisons for rational alpha, with no floating arithmetic.

#### Exact first-half paths

For each target y in this set, the following four sources are positive
odd integers. The displayed words are their exact ordinary valuations.

| Source | Valuation word | Intermediate state, if any |
|---|---|---|
| n_3=(8y-d)/3 | (3) | — |
| n_5=(32y-d)/3 | (5) | — |
| n_23=(32y-7d)/9 | (2,3) | n_3 |
| n_15=(64y-5d)/9 | (1,5) | n_5 |

The congruence y=5d mod18 proves all integrality and oddness claims.
The equalities 3n_3+d=8y, 3n_5+d=32y,
3n_23+d=4n_3 and 3n_15+d=2n_5 prove exact valuations, since y,n_3,n_5
are odd. All states exceed 1, so absorption does not alter these paths.

The one-arrow paths half-descend because

```
n_3-2y=(2y-d)/3>0,  n_5-2y=(26y-d)/3>0.
```

For the two-arrow paths the first iterate is strictly above the original
half-threshold, and the second is strictly below it:

```
n_3-n_23/2=(16y+d)/18>0,
n_5-n_15/2=(128y-d)/18>0,
n_23-2y=(14y-7d)/9>0,
n_15-2y=(46y-5d)/9>0.                              (7)
```

Therefore the four endpoints are first-half endpoints, at times 1,1,2,2.
The families have distinct first valuations 3,5,2,1, so sources in different
families cannot coincide. Each formula is injective in y, so multiplicity
is preserved within each family as well.

#### Exact selected count and asymptotic lower bound

The number of selected sources through integer X is exactly

```
N_d(X) = A((3X+d)/8) + A((3X+d)/32)
         + A((9X+7d)/32) + A((9X+5d)/64).           (8)
```

This is a lower bound for G_d(A)(X), not an exact count of all its sources.
Using (5)–(6) gives

```
lim_(X->infinity) N_d(X)/(||A||_alpha X^alpha) = K(alpha).
```

Taking a lower limit for G_d and then its supremum proves the first
inequality in (4). Because every base in K lies in (0,1), K is decreasing
in alpha. At alpha=7/8 its four terms are strictly greater than
2/5, 1/8, 5/16 and 1/6, respectively. Raising to the eighth power reduces
these four assertions to the exact integer inequalities

```
3^7*5^8 > 2^29,  3^7 > 2^11,
3^14 > 8*5^8,    3^22 > 2^34.                       (9)
```

The lower bounds sum to 241/240. Monotonicity proves the second
inequality in (4) for every real 0<alpha<=7/8.

### 4. Every sublinear power exponent is obstructed

**Theorem 3.** For every supported fixed d and every real 0<alpha<1,
there is a fixed infinite target set A with finite positive growth norm and

```
||G_d(A)||_alpha > ||A||_alpha.                      (11)
```

The set depends on alpha and d. No single set is asserted to work for all
parameters. This is a finite existence construction, potentially very large;
it does not assume that an orbit search terminates.

#### Finite homogeneous first-crossing words

For a word w=(a_1,...,a_l) of positive valuations define

```
A_i=a_1+...+a_i,   s_i=3^i/2^A_i.
```

Call w a first-crossing word when s_i>1/2 for 1<=i<l and s_l<1/2.
Equality is impossible for i>=1 by unique prime factorization. Let F_B be
all such words with A_l<=B. This is a finite prefix-free family: no member
is a proper prefix of another. Write

```
p_B = sum_(w in F_B) 2^(-A_l).
```

In this cylinder calculation use the raw odd map, which does not absorb
at1, and its raw shortcut parity encoding from S.1. The exact valuation
cylinder of w is one odd residue modulo2^(A_l+1).
Its relative weight among odd residues is2^(-A_l), retaining the extra bit.
Prefix-freeness makes these cylinders disjoint. Equivalently these are
finite binary strings, conditioned on initial bit1, whose gaps between
successive1 bits are the valuations. No randomness is assumed along any
individual infinite integer orbit. These are not cylinder claims for the
map killed at1. The later finite target threshold proves that every selected
actual path avoids1, and therefore also follows the absorbed map S_d.

Here the S.1 calibration feeds this open-node attempt directly. Put
t=5m, m>=9, and choose L>=1. Among all binary strings at positions
0,...,t+L-1 with bit0 fixed to1, S.1 Sections2–3 show that the fraction
with more than3m ones in the firstt positions is at most

```
delta_m=(8/7)(16807/18432)^m.
```

The fraction with no1 at positions t,...,t+L-1 is2^(-L). Outside their
union, take the first1 at a position j>=t. The preceding odd word is
complete: it has at most3m valuations and total valuation j, with
j<=t+L-1. Its homogeneous slope is at most

```
3^(3m)/2^t=(27/32)^m<1/4,
```

where the last inequality for m>=9 follows from4*27^9<32^9. It therefore
contains a first-crossing prefix belonging to F_(t+L-1). Hence

```
p_(5m+L-1) >= 1-delta_m-2^(-L).                     (12)
```

The right side tends to1 as m and L grow. For any fixed alpha<1, choose
finite m,L making it greater than2^(alpha-1), and set B=5m+L-1. The
existence uses a positive gap1-2^(alpha-1); it applies to every real alpha
in the stated domain. All cylinders here remain finite.

#### Average over compatible integer target residues

For w of length l, the exact forward affine expression is

```
y=(3^l n+d b_w)/2^A_l,
b_empty=0,  b_(w,a)=3b_w+2^A_l.
```

Thus the inverse source is

```
n_w(y)=(2^A_l y-d b_w)/3^l.                         (13)
```

For an odd target y, all intermediate inverse states are integers exactly
when

```
y = d b_w (2^A_l)^(-1) mod3^l.                      (14)
```

To see sufficiency, unwind the last arrow. Congruence(14) modulo3 makes
its numerator divisible by3. Dividing and reducing the remaining congruence
modulo3^(l-1) gives the previous word's condition, inductively. Each inverse
state is odd because an even multiple of an odd state minus odd d is odd,
and division by odd3 preserves oddness. For sufficiently large positive y,
all these states are positive and exceed1. Then each arrow has exactly its
specified valuation, since its successor is odd. This is a direct proof for
each d, not a generalization imported from d=1.

Let K be the maximum length in F_B. Of the3^K odd residue classes modulo
M=2*3^K, exactly3^(K-l) satisfy(14). For each odd residue c modulo M put

```
W(c)=sum_(w in F_B compatible with c) s_l^alpha.
```

Uniform averaging is therefore the exact finite identity

```
(1/3^K) sum_c W(c)
 = sum_(w in F_B) 3^(-l) s_l^alpha
 = sum_(w in F_B) 2^(-A_l) s_l^(alpha-1)
 > 2^(1-alpha) p_B > 1.                            (15)
```

The strict inequality uses s_l<1/2 and alpha-1<0. Some odd residue c has
W(c)>1. This pigeonhole statement does not require enumerating every residue.

#### Restore the affine intercept and every first-passage clock

Choose a positive odd representative c of that residue sufficiently large.
For every compatible word and every y>=c, require

```
n_w(y)>2,
n_w(y)>d b_w/(2^(A_l-1)-3^l).
```

These are finitely many lower bounds with positive denominators, so such
a representative exists. Earlier prefix states are
s_i n+d b_i/2^A_i > n/2 >1, since s_i>1/2 and d,b_i>0. The final inequality
makes y<n/2; by further increasing c take y>1. Thus(13) gives an actual
first-half path of exactly l ordinary arrows, with no earlier absorption.
The affine terms are retained in both the threshold and the count.

Now define the fixed target set

```
A={M ceil(j^(1/alpha))+c : integer j>=1}.
```

It has exact count

```
A(X)=floor(max(0,floor((X-c)/M))^alpha),
||A||_alpha=M^(-alpha),
A(X)/X^alpha -> M^(-alpha).                        (16)
```

The upper bound follows from c>=0; the limit proves equality of the norm.
For each compatible word, sources through X correspond exactly to

```
A(s_l X+d b_w/2^A_l).
```

Different words have disjoint sources. Otherwise a single odd source
would have two different first-crossing valuation prefixes, which exact
valuations and prefix-freeness prohibit. Each inverse formula is injective
in y. Consequently the selected sources give the lower bound

```
G_d(A)(X) >= sum_(w compatible with c) A(s_l X+d b_w/2^A_l).
```

After division by ||A||_alpha X^alpha, the right side tends to W(c)>1.
This proves(11). It also rules out a bound with coefficient kappa<=1
and an error o(X^alpha), even if that error may depend on this fixed A.
The output norm may be infinite; this proof does not decide that question.

#### Finite compressed certificate

The checker computes p_B exactly by a recurrence on noncrossing prefixes
indexed by their length and total valuation. A transition appends a positive
valuation, records a word at its first crossing, or retains the noncrossing
prefix. Prefixes with the same indices have the same homogeneous slope,
so aggregating their integer multiplicities loses no information. A final
word of valuation sum A contributes its multiplicity times2^(B-A) to the
numerator over2^B. A separate small-cap word enumeration checks this count.
The recurrence certifies the average in(15), not a specific enumerated
maximizing target class. The proof supplies existence for every alpha;
finite rational samples are not extrapolated to that assertion.

## Certificates

Default invocations compare each deterministic result with its receipt and write no files; `--write-receipt PATH` regenerates one deliberately; unknown flags, including an unimplemented search cap, fail closed. No unbounded orbit search is used, so no capped search is treated as a certificate.

- [`check_growth_norm.py`](check_growth_norm.py) (under a second) checks the integer inequalities, exact inverse arrows and first-passage thresholds, source disjointness, rational-alpha count formulas at jump boundaries, the selected-source cutoff formula and finite one-arrow norm inequalities, and rejects malformed domains and corrupted witnesses; receipt [`growth_norm_audit.json`](growth_norm_audit.json).
- [`check_all_exponents.py`](check_all_exponents.py) (under a second) audits the compressed prefix-code recurrence, inverse residues, first-half paths and the S.1 parity feed, with exact masses at total valuation budgets 48 and 80 for `alpha = 19/20` and `99/100`; receipt [`all_exponents_audit.json`](all_exponents_audit.json). The winning target residue exists by finite averaging; the huge full catalogue is not materialised. These finite certificates confirm the averaging mechanism; the all-real quantifier rests on §4's written proof.
- [`p6_003_growth_norm_check.py`](p6_003_growth_norm_check.py) (under a second) is the side lane's independent probe, with receipt [`p6_003_growth_norm_check.json`](p6_003_growth_norm_check.json).

## Remarks

**Exact scope of the obstruction.**

For any fixed supported d, 0<alpha<1 and kappa<=1, it is impossible
to have

```
G_d(A)(X) <= kappa ||A||_alpha X^alpha + e_A(X),
e_A(X)=o(X^alpha),                                 (10)
```

for every finite-norm target set A. The fixed set in Theorem3 contradicts(10);
Theorem2 supplies the simpler four-word witness through alpha=7/8.
Thus a version whose error must additionally
be uniform over target sets also fails. A strict contraction of the norm
itself is a special case. The contradiction is asymptotic and has a
positive margin; it does not come from one small-cutoff anomaly.

On 4/5<=alpha<=7/8, Theorems 1 and 2 apply simultaneously at d=1:
Q contracts while G_1 expands this explicit set. One cannot transfer the
one-arrow estimate to the full first-half map.

This barrier concerns ordinary nonnegative counting with this specific
power-growth norm and **arbitrary** targets. The constructed targets are
not asserted to be nonabsorbing. The result does not rule out an estimate
restricted to the actual nonabsorbing set, a bound with constant greater
than one, another weight or norm, additional arithmetic restrictions,
different stopping rules, or a proof using cancellation. It proves neither
that the full G norm is finite nor that it is infinite. It does not decide
Collatz or the availability of universal currents. The full-operator
barrier transfers to every fixed supported d; Theorem 1 was proved here
only for d=1.

**Literature match and remaining obligation.**

This is a **barrier** for S.2's uniform arbitrary-target power-growth-norm
contraction. It transfers to every supported fixed d and is not a
non-transfer step. The S.1 fixed-half calibration supplies the finite code
mass in(12), thereby feeding an actual open-node attempt as required by D6.

Closest primary matches are Borovkov–Pfeifer's finite-horizon threshold
densities (Theorem3) and Tao's exact valuation lemma (Lemma2.1) and
geometric-cylinder discussion (Remark1.10). Tao's Section1.1 identifies
concentration in an exceptional set as a difficulty with iteration. See
[the primary paper](https://arxiv.org/html/1909.03562v3) and the
[scoped literature audit](../route-literature-transfer-audit.md). These sources
are contextual matches; the inverse congruences, affine thresholds and norm
obstruction above are proved directly. No claim of novelty is supplied.

Further arbitrary-target power exponents will not repair this method.
The next S.2 premise would have to use properties of the actual nonabsorbing
set, another specified norm, or signed cancellation. This theorem establishes
no concentration property of the actual nonabsorbing set and no convergence
result.

The B-specific premise this points to is the open [`bad-set-half-descent-transport`](../../questions/bad-set-half-descent-transport.md); its conditional consequences are [`bad-set-transport-bootstrap`](../bad-set-transport-bootstrap.md).

## History

Migrated from `experiments/phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md` (legacy batch `P6-003`, route node S.2), with `check_growth_norm.py`, `check_all_exponents.py`, both receipts, `verification.json`, `experiments/phase6/side_lane_review_e4f8231.json` and the side-lane probe `reviews/side_lane/p6_003_growth_norm_check.py` with its receipt, at commit `be73a66`. The folder's short index `README.md` is in [`archive/convergence-phase6/`](../../../../archive/convergence-phase6/). ChatGPT main lane, 2026-10-18, pushed as `2e619a2`; the batch read the side lane at `0ed286c5e92f739f610f4aad2d460d0afc63eab6`. One convention clarification came out of the main lane's review: parity cylinders use the raw map, and the finite target threshold then ensures the selected actual paths avoid 1 and follow the absorbed map. Programme label **barrier**, confirmed by the side lane at `e4f82311` (feed 16:56, [`archive/side-lane/FEED.md`](../../../../archive/side-lane/FEED.md)). The ledger then closed this uniform power-norm method: further exponent variants were not to be added.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof; the review records two imprecisions (Theorem 2's four-word witness expands for every `α` below `α_0 ≈ 0.9162`, where `K(α_0) = 1`, so `α ≤ 7/8` is a safe sub-range; in §4 the exclusion of the target 1 is stated after the two threshold bounds although it is needed, as `d = 1`, `w = (4)`, `n = 5 → 1` shows).
