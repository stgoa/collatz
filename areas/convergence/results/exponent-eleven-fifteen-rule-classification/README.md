---
id: exponent-eleven-fifteen-rule-classification
kind: result
title: "The whole exponent-eleven family under the fifteen-rule dispatcher, and an exact zero-current self-request"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; T = nu S, P(w) = [3w] - [w], rho(w) = nu(3w); the fifteen rules are exactly
  the dispatcher at d265d94 (with R59's fixed old-twelve inner resolver). On the whole R61 CRT family (r >= 16, A
  >= 5, K >= 0): the exit's leading pair v = f/3 lies outside all fifteen direct domains, and no strict-rho
  expansion of other requests creates or cancels its coefficient +1; R59's four candidates at the original w all
  retain an unproved high request (the protected original w or v); hence the original w is accepted by the
  fifteen-rule dispatcher iff R60's maximal-cycle/point threshold passes, with R60's exact table in the parameters
  h = v3(2^(11r+18) s - 19), k = floor(h/7), j. Every feasible table row has an infinite CRT progression inside
  each fixed (r, A, K) family, so accepted and rejected subrows are both infinite. The prescribed quotient inverse
  word of length 7r+6 from f returns exactly to q, and substituting its strict leading plan into the original exit
  plan gives current zero and request {w: 1} row for row; the alternate stop reproduces R56's first inverse node.
  These are exact undo identities for named paths, not barriers to other comparisons.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [exponent-eleven-exit-continuation, fifteen-family-rho-dispatcher, deferred-original-rank-testing, maximal-inverse-cycle-continuation, growing-prefix-unhandled-leading-input, selected-critical-five-forward-tables, two-selected-inverse-choices, rank-excess-absorption-classification, elementary-bridge-quotient-normal-form]
certificates: [check_legacy_replay.py]
evidence:
  - "check_refined_obstruction.py, refined_obstruction.py, refined_obstruction_audit.json: the legacy constructor and checker: the joint R63-R64 receipt: 3298 affine checks, 15 first-passing and 14 last-failing boundary inequalities, 43 complete signed plans (13 descending, 29 higher-leading failures, one exact self-return), nine old-cycle phase rows, 16 new CRT rows through r = 64, A = 32, K = 64, four complete dispatcher classifications, two exact leading-current undos, three supplied conversions (102, 215 and 1746 rows from 9, 15 and 42 supplied pairs) and 15 rejections. The constructor also serves lifted-inverse-ray-cycle (R64), which lists these files from this folder. Fails at its new path: refined_obstruction.py loads ../cycle_inverse/ (now ../maximal-inverse-cycle-continuation/), ../deferred_rank/ (now ../deferred-original-rank-testing/), ../exit_continuation/ (now ../exponent-eleven-exit-continuation/), ../refined_rules/ (now ../fifteen-family-rho-dispatcher/) and ../selected_inverse/ (now ../two-selected-inverse-choices/) by their pre-migration folder names. Passed at be73a66 as experiments/residual_progress/refined_obstruction/check_refined_obstruction.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Sections 1-5 re-derived (family arithmetic, the R58/R59/R60 exclusions at v, the four R59 candidates at w with their leading requests, the (h, k, j) parametrisation and CRT cells, the 7r+6 inverse word and the zero-current undo) and reproduced with independent code on members of five (r, A, K) families and 60 CRT cells; the fifteen-family dispatcher checked to accept exactly when R60 does; certificate re-run (PASS, exit 0, 83 s). Verdict HOLDS, two imprecisions, no correction"
aliases: [R63]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, dispatcher, exact-undo]
---

# The whole exponent-eleven family under the fifteen-rule dispatcher, and an exact zero-current self-request

## Statement

Odd-only clock, 1 absorbing; `T = νS`, `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)`; the fifteen rules are exactly [`fifteen-family-rho-dispatcher`](../fifteen-family-rho-dispatcher/README.md) at `d265d94`, including R59's fixed old-twelve inner resolver; no later rule is included. The family is the whole R61 CRT family of [`exponent-eleven-exit-continuation`](../exponent-eleven-exit-continuation/README.md): `r ≥ 16`, `A ≥ 5`, `K ≥ 0`, `q = 81·2^(11r+11)s − 17`, `w = (2q+1)/3`, `f = 2^A t − 1`, `v = f/3`.

1. **Leading pair.** `v` lies outside all fifteen direct domains; no strict-`ρ` expansion of the other requests can create or cancel its coefficient `+1`, even where auxiliary ranks exceed `q`.
2. **Original input.** All four R59 candidates at `w` keep an unproved high request (the protected `w`, or `v`), so the fifteen-rule dispatcher accepts `w` iff R60's maximal-cycle/point threshold passes ([`maximal-inverse-cycle-continuation`](../maximal-inverse-cycle-continuation/README.md)), with R60's table in `h = v3(2^(11r+18)s − 19)`, `k = ⌊h/7⌋`, `j`. Every feasible row has an infinite CRT progression inside each fixed `(r, A, K)`; accepted and rejected subrows are both infinite.
3. **Exact undo.** The prescribed quotient inverse word of length `7r+6` from `f` returns exactly to `q`; its leading plan is strict at `v`, but substituted into the original exit plan it gives current `{}` and request `{w: 1}`, row for row. The alternate stop reproduces R56's existing first inverse node ([`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md)).

These are exact identities for named paths, not barriers to other comparisons; [`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md) gives new descending comparisons inside every family.

## Proof

The legacy note "The complete exponent-eleven family under the fifteen-rule dispatcher" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written, conditional classification and exact dependency identity.**
The old R61 exclusion concerned twelve rules. On its entire CRT family, the
fifteen-rule dispatcher accepts the original pair exactly when R60 accepts;
the exit's leading pair remains outside all fifteen. A longer inverse-cycle
comparison lowers that leading pair exactly to the original input and gives
an explicit zero-current self-dependency after composition. The accompanying
[lifted-cycle construction](../lifted-inverse-ray-cycle/README.md) supplies genuinely new original-rank
descent on complete subrows. Universal completion remains open.

Use absorbed odd Syracuse S, its elementary quotient T=nu S, P(w)=[3w]-[w],
and rho(w)=nu(3w). Formal absorption H_x has current J_x and signed request
vector A_x, so div J_x=[x]-A_x. Requests are full integer pair coefficients.
The fifteen rules mean exactly the dispatcher at d265d94, including the fixed
old-twelve inner resolver in R59. No later rule is included by implication.

Dependencies: [R61](../exponent-eleven-exit-continuation/README.md),
[R59](../deferred-original-rank-testing/README.md),
[R60](../maximal-inverse-cycle-continuation/README.md),
[R54](../growing-prefix-unhandled-leading-input/README.md), and the
[fifteen-rule dispatcher](../fifteen-family-rho-dispatcher/README.md).

### 1. Entire input family

Take r>=16, A>=5, K>=0, M=7r+10, epsilon=2^r mod3, and every positive t with

    t = -9*3^(-A)                  mod 2^(3K+6),
    t = (3^M*epsilon-5)*2^(-A)     mod 3^(M+1).

Write

    s=(2^A*t+5)/3^M,
    q=81*2^(11r+11)*s-17,       w=(2q+1)/3,
    f=3^M*s-6=2^A*t-1,          v=f/3,
    v0=(32q-23)/81=2^(11r+16)*s-7.

Here s is positive odd, s=epsilon mod3, v0 is divisible by3, and q<f.
The two indices v and v0 are different. The former is the unresolved exit
pair; the latter parameterizes the old selected inverse rule.
R61 proves rho(w)=q, rho(v)=f, and failure of all twelve old predicates
at both w and v. Every finite prescribed K is allowed. The seed varies
with the chosen parameters; no infinitely growing positive orbit is asserted.

### 2. The leading input remains outside all fifteen

Since 3v=f is nonselected, R59 has no initial candidate at v, and R60 is
inapplicable. R58 requires v=437 mod512. This would give

    f+1=3v+1=288 mod512,

whose exact binary order is5. Hence A=5 and t=9 mod16 would be necessary.
But the first CRT condition gives t=13 mod16 when A=5. Thus R58 also fails.
This is an exhaustive exclusion of the three added predicates, combined
with R61's twelve-rule classification.

The full exit vector is

    A_f-A_nu(w) = {v:1}+A_v-A_nu(w).

Every other request has rank below f. Therefore applying any finite number
of strict-rho rules to other requests cannot create v or cancel its coefficient
+1. This remains true when f/q is large and some auxiliary ranks exceed q;
they are **not** assumed below the original rank. Supplied currents or a
different rule at v may resolve the request; the named dispatcher does not.

### 3. R59 cannot rescue the original input

R58 does not apply to selected3w. The old twelve already fail. R59 has four
candidates, all of which retain an unproved high request:

1. The R56 ray4 and ray8 candidates have depth0 because 3|v0. Both have
   coefficient+1 at the protected original w, all other ranks below q.
2. The R57 exit candidate has the leading v just classified. It is the unique
   highest request and is unrecognized by R59's fixed old-twelve resolver.
   Every subsequent permitted expansion has lower rank and cannot cancel v.
3. The R55 first-block candidate has exactly one request of rank at least q,
   namely w1=(2q1+1)/3 with q1=(2187q+2363)/2048, coefficient+1.
   The first block is(4,2), so the optional R55 second-block candidate is absent.

For the last assertion, R54's row-four W9 elimination gives that unique
leading w1. Its remaining absorption inputs have rank bounded respectively by

    (3q1+4)/4,  (3q1+11)/8,  (243q+419)/512,

and the original lower H_nu(w) bound; all are below q in this family.
For example the first inequality is equivalent to1631q>15281.

There are at least fifteen guarded cycles remaining at q1. Its old-nine and
R55 tests therefore fail. Its R56 ray4 parameter v1=(32q1-23)/81 satisfies

    4v1+1 = 27*(q+1)/16.

Because q=1 mod3, the right side has exact ternary order3. R56 therefore
accepts w1 and its endpoint is exactly

    16*(4v1+1)/27-1=q.

Its unique leading request is the original w, with coefficient+1. All other
requests of this child plan are below q: they are from H_w and H_nu(w1),
with w=(2q+1)/3, w1=(2q1+1)/3, and nu(w1)<w1/4. Their standard bounds are
respectively at most(3q+4)/4 and strictly below(9w1/4+5)/8, both below q.
The original coefficient cannot cancel with any lower request. R59 protects
w and returns unresolved. This is one exact accepted child substitution,
not an assertion that a larger search can never find a certificate.

Thus the entire fifteen-rule test at w is exactly R60's test.

### 4. Complete acceptance parameters and infinite pass/fail subrows

Let E=11r+18 and

    h=v3(2^E*s-19),   k=floor(h/7),   a=2048/2187.

For k>=1 put

    U=(2^E*s-19)/3^(7k),
    p=2^(11k+1)*U-17,
    j=v3(p+1)=v3(2^(11k-3)*U-1).

The original w is accepted by refined15 iff

| k | Accepted j |
|---|---|
| 0 | none |
| 1 through5 | j>=3 |
| 6 through11 | j>=2 |
| 12 through17 | j>=1 |
| 18 and higher | every j>=0 |

All remainders h-7k in0..6 are retained. A positive remainder forces j=0.
The table and every failure vector are R60's proved exhaustive classification.
For every fixed(r,A,K), every feasible row occurs in an infinite progression.

To prove this last quantifier, the binary condition on s is exactly

    s = (5+2^A*t2)*3^(-M) mod 2^(A+3K+6),
    t2 = -9*3^(-A) mod 2^(3K+6).                     (1)

For k>=1, remainder0 and j>=1, choose either e=1 or2 and impose

    U=2^(3-11k)*(1+3^j*e) mod3^(j+1),
    s=(19+3^(7k)*U)*2^(-E) mod3^(7k+j+1).          (2)

For j=0,remainder0, instead take 2^(11k-3)U=2 mod3. For remainder d=1..6
take U=3^d*e mod3^(d+1). The same latter construction with k=0 supplies
every h=1..6. Each ternary condition reduces to s=2^r mod3, as required.
Its modulus is coprime to (1), so CRT gives a full positive infinite progression.
Passing k1,j3 and failing k0,h1 already give both outcomes at every(r,A,K).

### 5. A strict leading descent that composes to an exact self-request

The complete quotient inverse theorem has branches ray0,ray1,point. From f,
apply

    ray1,point;
    (ray0,point,point,point,ray0,ray0,point)^r;
    ray0,point,point,point.                          (3)

The first two states are16f/3+1 and(32f+3)/9, with second shadow -21.
One seven-step block fixes -21 and multiplies its displacement by a.
The last four branches multiply that displacement by64/81 and change the
shadow to -17. Thus the final state is exactly

    (64/81)*a^r*(32/9)*(f+6)-17=q.

All divisions are integral with the prescribed residue at each step because
f+6=3^(7r+10)s. The complete inverse-branch theorem supplies positive
canonical states. This is7r+6 quotient arrows. Its exact ordinary current
is -D_(q,f), with common-tail clocks(1,7r+7) from(f,q); the elementary
normalizations are retained, not counted as zero ordinary time.

The resulting leading plan is

    L_v = -D_(q,f)-N_v+J_q-J_nu(v),
    c_v = A_q-A_nu(v),                              (4)

where div N_x=[x]-[nu(x)]. It is strict-rho at v: its leading input is w
of rank q<f; every other request is below f. It is conditional on those
inputs, including P(w).

When substituted into the original exit plan, (4) gives exactly

    current={},  coefficients={w:1}.                (5)

This follows row-for-row from J_x=N_x+J_nu(x),
J_f=J_v, A_f={v:1}+A_v, and J_q=-N_(3w)+J_w.
The forward current and its negative cancel. All auxiliary H and N currents
then cancel too. Equality (5) is stronger than a boundary-only equality, and
prevents mistaking a strict descent at the intermediate v for descent below q.

There is one other natural stopping phase. Use r+1 full seven-step blocks
after the first two inverses. The endpoint is

    3*2^(11r+16)*s-21=3v0=(32q-23)/27.

This is exactly R56's existing first inverse node. Its depth6 W9 elimination
has leading P(w) of rank q. Its two base rays are8v0+1 and16v0+1, the old
R56 choices. Hence this alternate stop also introduces no new comparison.
The [new result](../lifted-inverse-ray-cycle/README.md) takes a nonzero ray lift and a different
cycle rotation instead.

### 6. Reproduction and remaining scope

Run `python3 experiments/residual_progress/refined_obstruction/check_refined_obstruction.py`.
The checker verifies finite members of all parameter rows, actual dispatcher
outcomes, exact signed deferred plans, and the complete current cancellation.
The universal quantifiers follow from the arguments above, not from those
finite tests. All inverse words are prescribed; no universal orbit search or
termination claim is made. Novelty, human review, formal verification, and
universal coverage remain unestablished.

The stored finite receipt includes nine old-cycle phase rows, four complete
original/leading dispatcher classifications, and two exact leading-current
undos. One undo stores its full current, the original exit current, every
inverse state, and the resulting singleton self-request. Sixteen new CRT
members cover both18/24-arrow constructions, both terminal units, and parameter
choices through r64,A32,K64. These are finite implementation checks, not
coverage estimates or substitutes for the quantified CRT proofs.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_refined_obstruction.py` (about 75 s; the joint R63-R64 receipt `refined_obstruction_audit.json`, including the four dispatcher classifications and the two leading-current undos of this node). The commands in the legacy text name `experiments/residual_progress/refined_obstruction/`.

## Remarks

- The legacy folder `refined_obstruction/` held two notes on one constructor: this one (R63) and `LIFTED_CYCLE.md`, now [`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md) (R64). The scripts and the joint receipt live in this folder.
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/refined_obstruction/REFINED_ELEVEN.md` (legacy ID R63) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). The note, the joint constructor, checker and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. The companion note `LIFTED_CYCLE.md` became [`lifted-inverse-ray-cycle`](../lifted-inverse-ray-cycle/README.md). Legacy status: "written classification of the whole R61 CRT family under the fixed fifteen rules".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `793e835`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof; two imprecisions in section 3 (three bounds listed without saying which input each bounds; the R55 failure at w1 asserted without its computation) are recorded in the review ([`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md)).
