---
id: common-critical-rank-basis
kind: result
title: "Keeping both critical pair types lets sigma rules and rho rules share one strict rank after translation"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w], W = W5 u W9, rho(w) = nu(3w). R37's unexpanded critical
  absorption plan [s] = div Jhat_s + sum Ahat_s(v) P(v) requests only ranks <= nu(s). For every returning u in E,
  with q = (3u-1)/2, n = (4u-3)/3 = sigma(u), b = n/3 in W9, the current C_u = N_(3u) - D_(n,q) + Jhat_b - Jhat_u
  gives P(u) = div C_u + P(b) + sum (Ahat_b - Ahat_u) P, with unique highest request b (+1), rho(b) = n < q, all
  others below n. Replacing every signed returning child of any sigma-valid W5 plan by this identity yields a
  rho-valid plan in W; every old rho-valid W5 plan stays valid unchanged; so both collections can be used under one
  strict rank after translation (the original incompatible edges are not claimed to share a rank). On the whole R67
  guard, q = 3w compares to f = (729w + 147)/256 < q at ordinary clocks (6, 1), giving a decreasing plan whose unique
  highest input is the W9 pair f/3 of rank f. The local W9 rule is rho-valid except exactly at d = v2(9b-1) = 4 with
  3z noncanonical, where returning to E restores the self-request P(b) (+1); a universal zero-current undo is false
  (u = 453, b = 201). This enlarges the induction universe; it adds no W5-only coverage and supplies no terminal
  currents.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [critical-tripling-domain-equivalence, critical-nine-elimination, critical-image-rank-composition, sigma-rank-removes-absorption-overhead, decreasing-w5-phase-inverse-barrier, mixed-rank-growing-blocks]
certificates: [check_legacy_replay.py]
evidence:
  - "check_critical_basis.py, critical_basis.py, critical_basis_audit.json: the legacy constructor and checker: 512 critical H plans, 256 complete E conversions, 512 W9 local classifications, 116 sigma translations, 32 unchanged rho plans, eight whole-guard cases with binary depths through 159, the coefficient -3 request, the 4629 incompatibility, the 453/201 nonzero undo, a finite conditional closure, three supplied conversions (40, 86 and 15 rows) and the rejection checks; 32 reachable sources pinned. Fails at its new path: critical_basis.py loads ../phase_rank/ (now ../sigma-rank-removes-absorption-overhead/) and, through the shared loaders, the B10-B11 modules by their pre-migration folder names; it is loaded in turn by seven later legacy history folders. Passed at be73a66 as experiments/residual_progress/critical_basis/check_critical_basis.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "batch_r75_r77_check.py, batch_r75_r77_check.json: side-lane probe (Claude side lane, 2026-10-18 02:53) of R75's returning-class translation arithmetic and R77's same-seed bounds; same-seed-factor-complexity-bound replays it from this folder. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r75_r77_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r75_r77_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 02:53, VERIFIED, main e9effe1), with the lane's own step and selected: 3,000 random returning inputs u = 5 (mod 8), u = 3 (mod 9) with 3u selected: n = (4u-3)/3 = sigma(u) is an integer, b = n/3 = 9 (mod 16) lies in W9, the ordinary path n -> q = (3u-1)/2 has valuations (1, 2), and rho(b) = 3b = n < q. The u = 453 example and the current C_u rest on main's plans and were not rebuilt; reproduced by the main lane in side_lane_review_fcc7e88.md (in divergent-orbit-itinerary-complexity). The status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived with an independent implementation (basis bound on all 4096 plans, returning conversion on all 455 inputs below 2^16, bijection (11) below 2^17, the 453/201 fourteen-row current, the whole guard at the eight receipt moduli, translation of 340 sigma-valid plans) and compared row for row with the legacy module; certificate replayed (exit 0); 3x+d analogues tested. Verdict HOLDS; two notational imprecisions noted"
aliases: [R75]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, sigma-rank, critical-basis]
---

# Keeping both critical pair types lets sigma rules and rho rules share one strict rank after translation

## Statement

Odd-only clock, 1 absorbing, `[1] = 0`; `P(w) = [3w] − [w]`; `W5 = {w ≡ 5 mod 8}`, `W9 = {w ≡ 9 mod 16}`, `W = W5 ∪ W9`; `ρ(w) = ν(3w)`; `σ` the rank of [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md); `E` the returning class.

1. **Critical basis.** The unexpanded critical absorption plan of [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md) (R37), `[s] = div Ĵ_s + Σ Â_s(v)P(v)` with `v ∈ W`, requests only ranks `≤ ν(s)`.
2. **Returning interface.** For `u ∈ E` put `q = (3u − 1)/2`, `n = (4u − 3)/3 = σ(u)`, `b = n/3 ∈ W9`. With `C_u = N_(3u) − D_(n,q) + Ĵ_b − Ĵ_u`, `P(u) = div C_u + P(b) + Σ (Â_b − Â_u)P`; the unique highest request is `b` (`+1`), `ρ(b) = n < q`, all others below `n`.
3. **Translation.** Replacing every signed returning child of any `σ`-valid `W5` plan by 2 yields a `ρ`-valid plan in `W`; every old `ρ`-valid `W5` plan stays valid unchanged. Both collections can therefore be used under one strict `ρ` after translation. The original incompatible edges are not claimed to share a rank.
4. **Whole R67 guard.** On the guard of [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md), `q = 3w` has an ordinary comparison to `f = (729w + 147)/256 < q` at clocks `(6, 1)`; the critical plans give a decreasing rule whose unique highest input is the `W9` pair `f/3` of rank `f`.
5. **Blocked W9 branch.** The local `W9` rule is `ρ`-valid except exactly at `d = v2(9b − 1) = 4` with `3z` noncanonical; there, returning to `E` restores the self-request `P(b)` (`+1`). A universal row-for-row zero-current undo is false: `u = 453`, `b = 201` leaves `{201: 1, 5: 1, 25: 1}` and a nonzero 14-row current.

This enlarges the induction universe and the rule-selection policy. It adds no coverage to the unchanged seventeen-family `W5` dispatcher and supplies no terminal currents.

## Proof

The legacy note "A common decreasing compiler by retaining both critical pair types" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

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

Dependencies are the [critical bijection and formal plans](../critical-tripling-domain-equivalence/README.md),
[complete W9 interface](../critical-nine-elimination/README.md),
[critical-image rank](../critical-image-rank-composition/README.md),
[separate sigma rank](../sigma-rank-removes-absorption-overhead/README.md),
[returning inverse](../decreasing-w5-phase-inverse-barrier/README.md),
and [R67 mixed block](../mixed-rank-growing-blocks/README.md).
The new proof combines these established source identities; it does not
import an external convergence result.

### 1. Keep the complete critical source basis

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

### 2. Every returning W5 input has a smaller critical-nine interface

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

### 3. Translate the whole sigma rule collection into one rho induction

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

#### Finite conditional closure

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

### 4. Exactly which W9 local branch remains blocked

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

### 5. The entire R67 guard has a decreasing rule in this basis

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

### 6. Executable interface, evidence, and remaining work

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

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_critical_basis.py` (about 6 s; the counts of section 6 of the note and the stored supplied conversions, compared with `critical_basis_audit.json`) and the side-lane probe `batch_r75_r77_check.py` (under 1 s, receipt reproduced byte for byte). The commands in the legacy text name `experiments/residual_progress/critical_basis/`.

## Remarks

- **Hub.** `critical_basis.py` is imported by the legacy code of seven later nodes, which load it by its legacy path: [`native-critical-nine-continuation`](../native-critical-nine-continuation/README.md), [`immediate-self-loop-lower-relations`](../immediate-self-loop-lower-relations/README.md), [`native-growth-original-rank-exit-obstruction`](../native-growth-original-rank-exit-obstruction/README.md), [`high-smaller-origin-history`](../high-smaller-origin-history/README.md), [`fixed-word-history-cells`](../fixed-word-history-cells/README.md), [`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md) and [`even-exit-smaller-target-cone`](../even-exit-smaller-target-cone/README.md).
- The blocked `d = 4` W9 branch and the unresolved nonreturning `W5` inputs are the next supply obligation of [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md); re-expanding a `W9` input into a higher `W5` request recreates the old difficulty.
- [`uniform-fixed-word-pair-exclusion`](../uniform-fixed-word-pair-exclusion/README.md) (R76) excludes one fixed-word pair model; this construction uses an additional source type outside it.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/critical_basis/CRITICAL_BASIS.md` (legacy ID R75) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. The side-lane probe `reviews/side_lane/batch_r75_r77_check.*` (R75 and R77) moved here. Legacy status: "written source-basis and rule-translation theorem with an exact conditional compiler; terminal current supply remains open".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `e9effe1`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No text was changed; two notational imprecisions (D_(n,q) in the claim is G_n in the proof; the guard depths 26 to 159 are moduli exponents, the seeds have 26 to 160 bits) are recorded in the review.
