---
id: even-exit-smaller-target-cone
kind: result
title: "After an even complementary exit, the raw smaller target lies below the source exactly on an explicit cone"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; retained critical basis of R75. Let H >= 3, b >= 1, q = 2^H t - 1 divisible
  by 3, and 3^(H-1) t - 1 = 4^b u with u positive odd and n = 3^b u = 1 mod 8. Then w = q/3 is in W5, f = 2n+1 is
  selected, the ordinary path q -(1^(H-1),2^b)-> f is exact, S^(H+b+1)(q) = S(y) with y = (3n+1)/4, and the full
  comparison G = L_(H+b+1)(q) - e_y has boundary [q] - [y], ordinary clocks (H+b+1, 1) and quotient clock H+b.
  Exactly y < q iff 3^(H+b) < 2^(H+2b+2), with no small-source exception; on this cone G + J_y - J_w requests A_y
  - A_w, every rank below q, conditional on all signed inputs being supplied. Complete positive CRT cells realise
  every H >= 3, b >= 1, exact v3(q) = D >= 1 and both ternary units; for every H >= 4 the least closing b gives n
  > q > y. At H = 4, b = 1 the phase is w = 293 mod 512, and its subphase w = 293 mod 4608 lies outside all
  seventeen old direct predicates by domain analysis. The old R48 formal current already contains the step and its
  W5-only requests are also strict here: the gain is exact coverage beyond the old coarse bound, not a new local
  orbit identity. Outside the cone only the raw-target inequality fails (control q = 927).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, complementary-run-bridges, forward-blocks-low-exponent-tests, rank-excess-absorption-classification, seventeen-family-rho-dispatcher]
certificates: [check_legacy_replay.py]
evidence:
  - "check_even_exit_history.py, even_exit_history.py, even_exit_history_audit.json: the legacy constructor, checker and receipt: 640 arithmetic cells, 50 full plans, 256 minimal-H cells through H = 256, D = 32, 72 valid CRT memberships in 7680 attempts, 34 old-seventeen progression cases, 28 rejection controls, three supplied outputs with 29/79/73 rows. Fails at its new path: even_exit_history.py loads ../critical_basis/, ../nonselected_forward/ and ../resolved_rules/ (now ../common-critical-rank-basis/, ../forward-blocks-low-exponent-tests/, ../seventeen-family-rho-dispatcher/) by their pre-migration folder names; and Its receipt pins the SHA-256 of this node's legacy note EVEN_EXIT_HISTORY.md, now an edited README, so it fails at its new path and in a legacy replay. Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged)"
  - "r86_even_exit_check.py, r86_even_exit_check.json: side-lane probe (Claude side lane, 2026-10-18 05:13) of the raw-target cone. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/r86_even_exit_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py; the main lane reproduced it in side_lane_review_64a5981.md (in ../maximal-inverse-cycle-continuation/)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: r86_even_exit_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 05:13, VERIFIED, main 2a37f31), with the lane's own step, ν and selected: 'Inputs are built by CRT for every `H = 3..14` and `b = 1..8`, 1,152 cases in all': f = 2n + 1 selected with ν(f) = n, y = S(n) = (3n + 1)/4, S^(H+b+1)(q) = S(y), and 'y < q exactly when 3^(H+b) < 2^(H+2b+2), both inside the cone (396 cases) and outside it (756), with no small-source exception.' Per the main lane's review (side_lane_review_64a5981.md): no universal extrapolation, full current, old-seventeen exclusion or R87 repair. The status stays written"
aliases: [R86]
tags: [convergence, outer-residual, smaller-origin-history, even-exit, original-rank, crt-construction]
---

# After an even complementary exit, the raw smaller target lies below the source exactly on an explicit cone

## Statement

Odd-only clock, 1 absorbing, `T = νS`, `P(w) = [3w] − [w]`; the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75).

1. **Even-exit subtype.** Let `H ≥ 3`, `b ≥ 1` and positive odd `t` satisfy `q = 2^H t − 1 ≡ 0 (mod 3)`, `3^(H−1) t − 1 = 4^b u` with `u` positive odd, and `n = 3^b u ≡ 1 (mod 8)`. Then `w = q/3 ∈ W5`, `ρ(w) = q`; `f = 2n + 1` is selected with `ν(f) = n`; the ordinary path `q → f` has valuations `(1^(H−1), 2^b)`; with `y = (3n + 1)/4`, `S^(H+b+1)(q) = S(y)` and `T^(H+b)(q) = ν(y)`. The comparison `G = L_(H+b+1)(q) − e_y` has boundary `[q] − [y]`, ordinary clocks `(H + b + 1, 1)`, quotient clock `H + b`; it is the R26 current ([`complementary-run-bridges`](../complementary-run-bridges/README.md)) followed by the normaliser of `f`.
2. **Exact inequality.** `y < q` iff `3^(H+b) < 2^(H+2b+2)`, with no exceptional small parameter. On this cone `G + J_y − J_w` has requests `A_y − A_w`, all ranks below `q`; supplied exact currents for all signed coefficients give `P(w)`.
3. **CRT cells.** For every `H ≥ 3`, `b ≥ 1`, `D ≥ 1`, `c ∈ {1, 2}` a complete positive progression realises the subtype with `v3(q) = D` and `q/3^D ≡ c (mod 3)`. For every `H ≥ 4` the least closing `b` gives `n > q > y`.
4. **Outside the old dispatcher.** At `H = 4`, `b = 1` the phase is `w ≡ 293 (mod 512)`, with `n > q > y` and the old R48 direct test rejecting it; the subprogression `w ≡ 293 (mod 4608)` lies outside all seventeen old direct predicates of [`seventeen-family-rho-dispatcher`](../seventeen-family-rho-dispatcher/README.md).

The old R48 formal current ([`forward-blocks-low-exponent-tests`](../forward-blocks-low-exponent-tests/README.md)) already contains the free step, and its W5-only requests are strict here too (by [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md), R58): the gain is a larger exact validity domain for an existing comparison, not a new local orbit identity.

## Proof

The legacy note "A complete even-exit history cone after the obstructed rising prefix" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R86 — written conditional construction and exact raw-target classification.**
The construction covers every member of the parameter cone below, including
arbitrary first exponent H and exact ternary depth D. It supplies a smaller
future after an intermediate endpoint that can exceed the original source.
Every remaining current is an explicit supplied premise. The inequality
classifies the specified raw target, not all currents outside the cone.
The existing dispatcher and its resolvers are unchanged. No novelty is asserted.

Use absorbed odd Syracuse S, elementary minimum nu, T=nu S and
P(w)=[3w]-[w]. The default compiler uses the
[R75 retained critical basis](../common-critical-rank-basis/README.md), whose
formal absorption identity is

    [x]=div J_x+sum_v A_x(v)P(v),    rho(v)<=nu(x).        (1)

These are finite arithmetic plans, not supplied absorption currents.
All signs and multiplicities are retained; atoms and rows at1 are killed.

### 1. The whole even-exit subtype

Let H>=3, b>=1 and positive odd t satisfy

    q=2^H*t-1=0 mod3,
    3^(H-1)*t-1=4^b*u,    u positive odd,
    n=3^b*u=1 mod8.                                     (2)

Thus d=v2(3^(H-1)*t-1)=2b is exact. The congruence in (2) gives
`t=-3^H mod4`, so q is complementary canonical, w=q/3 belongs to W5,
and rho(w)=q. This is the even R26 endpoint subtype whose canonical half
is1 modulo8. It is a whole parameterized subtype, not a bounded sample.
Put

    f=2n+1,       y=(3n+1)/4.                            (3)

Here f is selected with exponent2, nu(f)=n, S(n)=y and y=1 mod3.
The first H-1 ordinary valuations from q are1. Their last state is
`2^(2b+1)*u+1`. The next b valuations are exactly2, ending at f:

    q --(1^(H-1),2^b)--> f.                             (4)

Indeed the states during the second run are
`2^(2(b-j)+1)*3^j*u+1`, 0<=j<=b. All sources in (4) are canonical;
the endpoint f is selected. Its next state is `3n+2=F(y)`, and
S(F(y))=S(y). Consequently

    S^(H+b+1)(q)=S(y),
    T^(H+b)(q)=nu(y).                                   (5)

The ordinary clocks are (H+b+1,1); the quotient clock is H+b.
The extra normalization is not assigned zero ordinary time.

Let L_m(x) be the ordinary m-arrow current. The entire bridge is

    G=L_(H+b+1)(q)-e_y,       div G=[q]-[y].              (6)

This is also the complete R26 current, followed by the normalizer of f
and the row e_n. The normalizer is
`e_f+e_(S(f))-e_n-e_y`, so the e_n rows cancel exactly. Formula (6)
retains the negative row and every coincident-row multiplicity. No unknown
future orbit is searched to construct it.

### 2. Exact success inequality, with all offsets

**Theorem.** On the entire domain (2),

    y<q  iff  3^(H+b)<2^(H+2b+2).                       (7)

There is no exceptional small positive parameter. Equality y=q is impossible.
Write `lambda=3^(H+b)/2^(H+2b+2)`. Direct substitution gives

    y-q=(lambda-1)q+lambda+1/4-(3/4)^(b+1).              (8)

If lambda<1, the right side is strictly below5/4. Since y-q is an even
integer, it is at most0. It cannot be0 because y=1 mod3 while q=0 mod3.
If lambda>1, both its first term and
`lambda+1/4-(3/4)^(b+1)>11/16` are positive. Equality lambda=1 is
excluded by prime factorization. This proves the iff, including every
intercept and every terminal unit.

When (7) holds, the complete conditional pair plan is

    C=G+J_y-J_w,       coefficients A_y-A_w.             (9)

Its boundary is `P(w)-sum_v (A_y(v)-A_w(v))P(v)`. Every remaining request
has rank at most max(nu(y),nu(w))<q. Thus supplied exact currents for
**all** nonzero signed coefficients give an exact P(w) current.
The compiler rejects missing or malformed supplies. This is a strict
original-rank statement; n itself may be higher than q.

Retaining W9 is sufficient, but not essential for this cone. In the old
expanded W5 absorption plan, [R58](../rank-excess-absorption-classification/README.md)
places an above-source request only at certain canonical multiples of3;
noncanonical sources have every request below the source. Since y=1 mod3,
all its old W5 requests also have rank at most y. The lower source w=5mod8
is noncanonical, so all its requests are below w<q. Moreover the old
formal absorption at f already contains its normalization and the free
arrow n->y. Thus this construction proves a larger exact validity domain
for an existing formal comparison than the old coarse endpoint test
recognized. It is not a new local orbit identity or a uniquely W9-based gain.

### 3. A complete CRT family at every H and exact D

For any H>=3,b>=1,D>=1, c in{1,2}, impose

    t=3^(1-H)*(1+4^b*3^(-b)) mod2^(2b+3),
    t=2^(-H)*(1+c*3^D) mod3^(D+1).                     (10)

In the first congruence `3^(-b)` is its inverse modulo8. These coprime
conditions define a complete positive progression, with period
`2^(2b+3)*3^(D+1)` in t and `2^(H+2b+3)*3^D` in w. They give exactly
(2), v3(q)=D and q/3^D=c mod3. Conversely every t in (2) with that exact
D and terminal unit belongs to this cell. The least positive t has u>0:
`3^(H-1)t-1>0`, and divisibility and oddness make u a positive integer.
No artificial large-source cutoff is needed.

For every H>=4 let b_H be the least positive b satisfying (7). It exists:
b=2H works because `3^(3H)<2^(5H+2)`. Every positive member of (10)
with b=b_H then satisfies the stronger relation

    n>q>y.                                              (11)

For H4, b_H=1 and the affine slope of n as a function of q is81/64.
For H>=5 the case b1 fails,
so b_H>1. Failure at b_H-1 means
`lambda_n=3^(H-1+b_H)/2^(H+2b_H)>1`. In both cases

    n-q=(lambda_n-1)q+lambda_n-(3/4)^b_H>0.

The second inequality in (11) is (7). This supplies a complete all-H
family after an initial rising prefix of unbounded length, with arbitrary
exact ternary depth. It does not contradict R85: the smaller target is
beyond that theorem's initial valuation-one future horizon.

### 4. A whole phase outside the old seventeen direct predicates

At H4,b1, (2) is exactly t=55 mod96, giving

    w=293+512l,       q=879+1536l,
    n=1113+1944l,     y=835+1458l,       l>=0.            (12)

All of (12) satisfies n>q>y, with ordinary clocks (6,1) and quotient
clock5. The old R48 endpoint bound is
`(27n+29)/32>q` throughout this phase, so its direct test rejects it.
The entire subprogression

    w=293+4608j,       j>=0,                             (13)

is outside **all seventeen old direct predicates**, for these exact reasons:

- 3w is nonselected. This excludes R41/R44/R46, R52, R55/R56/R57,
  R59 and R60/R64, whose applicable candidate domains are selected here.
- w=5 mod9, so 3 does not divide w and R47 is inapplicable. The active
  R45 k4 branch has exact h1 and its endpoint is0 mod3; it fails that
  predicate. The k8 branch has h0. In R50 the next depth is0, so it
  also fails.
- R48 rejects by the strict bound just calculated. R53 requires the
  first canonical endpoint to have exponent2; here n=1mod8 has exponent1.
- R58 and R62 require the fifth-exponent phase w=437mod512, disjoint
  from w=293mod512.

This exhausts the fixed dispatcher: its seven original arms, R52/R53,
R55/R56/R57, R58/R59/R60 and R62/R64. It is a domain proof, not an
extrapolation of the finite recognition probes. It does not say no other
previous supplied graph or conditional current can certify a member.
The dispatcher is not modified.

### 5. What the inequality does not classify

Outside (7), the specified raw target y is strictly above q. That does
**not** imply that (9) is invalid or that another history fails. Further
normalization or free absorption steps can still give lower requests.
The explicit control H5,b1,t29 has

    q927, n1761, y1321>q,       nu(S(y))=495<q.           (14)

Its full retained absorption plan already requests only lower ranks.
Accordingly the constructor labels this branch outside its raw-target
cone, preserves its exact current and requests, and does not certify it
under this rule. The proof does not claim all even exits are covered,
that repeated increasing returns terminate, or that terminal inputs are
universally supplied. Collatz remains open.

### 6. Reproduction

Run `python3 experiments/residual_progress/even_exit_history/check_even_exit_history.py`.
Default replay reconstructs the stored supplied inputs; it does not search
for their absorption. `--write-receipt` prepares only the designated
capped finite demonstrations. The receipt pins this proof and every
reachable local mathematical source module. The written CRT and inequality
proofs give the unbounded quantifiers; finite checks are separate evidence.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `r86_even_exit_check.py` (under 1 s, receipt reproduced byte for byte): 1,152 CRT inputs for `H = 3..14`, `b = 1..8`, the selected endpoint, the one-step target, the clocks and the raw inequality inside and outside the cone. The legacy checker `check_even_exit_history.py` is not replayed: it pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/even_exit_history/`.

## Remarks

- Outside the cone a larger raw target is not a missing current: at `H = 5`, `b = 1`, `t = 29` (`q = 927`) the raw `y = 1321 > q`, yet further formal normalisation succeeds.
- The cone is beyond the initial valuation-one horizon of [`bounded-history-clock-exclusion`](../bounded-history-clock-exclusion/README.md) (R85), so there is no conflict.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/even_exit_history/EVEN_EXIT_HISTORY.md` (legacy ID R86) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written conditional construction and complete raw-target classification".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `2a37f31`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
