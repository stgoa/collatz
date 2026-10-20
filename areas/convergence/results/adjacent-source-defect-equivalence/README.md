---
id: adjacent-source-defect-equivalence
kind: result
title: "The whole returning absorption defect is an adjacent-source comparison, modulo strictly smaller helpers"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(u) = [3u] - [u], rho(u) = nu(3u). The R58 exceptional canonical seeds n,
  the returning inputs u in E and the positive canonical q = 31 mod 108 are in bijection (q = (9n+5)/8, u =
  (2q+1)/3), and n -> 8z+1 -> 6z+1 = q are two ordinary arrows of valuations 1 and 2. With D(q) = [q+2] - [q] there
  is an exact identity P(u) = div K - D(q) + sum c(v) P(v) in which every helper has rho(v) <= (3q+7)/4 < n =
  (8q-5)/9; so a supplied D(q) current gives P(u) and conversely, with the same strictly smaller helpers, and the
  two conversions compose to the identity row for row. The adjacent current remains a premise with coefficient -1.
  Eliminating returning requests from any finite H_s terminates and leaves nonreturning pairs and adjacent sources
  of native height at most nu(s); at the exceptional leading source the height equals nu(s), so this change of
  basis is not strict progress, and the transported old rule at 4629 raises a height from 6171 to 6591. Maximal
  inverse-(1,2) normalisation adds no W5 domain and does not define a quotient dynamics. No accepted domain is
  added and no adjacent current is supplied; a source gap of two bounds neither merger time nor certificate size.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [rank-excess-absorption-classification, decreasing-w5-phase-inverse-barrier, critical-image-rank-composition, sigma-rank-removes-absorption-overhead]
certificates: [check_legacy_replay.py]
evidence:
  - "check_adjacent_defect.py, adjacent_defect.py, adjacent_defect_audit.json: the legacy constructor and checker: 512 complete defect plans, 1024 mixed absorption plans, 4096 W5 inverse-normalisation cases, both counterexamples (4629 and the kappa quotient), eight invalid or missing-supply rejections and three bidirectional supplied conversions at u = 21, 93, 4629 (pair outputs 40, 15, 94 rows; adjacent outputs 45, 14, 104 rows). Fails at its new path: adjacent_defect.py loads ../critical_rank/ (now ../critical-image-rank-composition/), ../exact_absorption_bound/ (now ../rank-excess-absorption-classification/) and ../returning_phase/ (now ../returning-forward-interface/) by their pre-migration folder names; it is loaded in turn by the later legacy adjacent_recursion/ code (native-height-inverse-obstruction). Passed at be73a66 as experiments/residual_progress/defect_normal_form/check_adjacent_defect.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "../exponent-eleven-exit-continuation/batch_r61_r67_check.py: side-lane probe of R61, R65, R66 and R67 (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../exponent-eleven-exit-continuation/batch_r61_r67_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 06:14, VERIFIED), with the lane's own step, nu and selected: all 10,000 canonical q = 31 (mod 108) below about 2.16e6 satisfy the triple bijection n = (8q-5)/9, u = (2q+1)/3, z = (q-1)/6 = (3n-1)/16 = (u-1)/4, with n = 27 (mod 96), z = 5 (mod 18), 3z noncanonical, n an R58 exceptional seed, u a returning input, and the two ordinary arrows n ->(1) 8z+1 ->(2) 6z+1 = q. The adjacent identity, helper bounds and conversions were not rebuilt; the status stays written"
aliases: [R65]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, adjacent-source, absorption-defect]
---

# The whole returning absorption defect is an adjacent-source comparison, modulo strictly smaller helpers

## Statement

Odd-only clock, 1 absorbing; `ν`, `P(u) = [3u] − [u]`, `ρ(u) = ν(3u)`; formal plans `[x] = div J_x + Σ A_x(v)P(v)` with signed integer coefficients; killed atom `[1] = 0`.

1. **Domains.** The R58 exceptional canonical seeds `n` ([`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md)), the returning inputs `u ∈ E` and the positive canonical `q ≡ 31 (mod 108)` are in bijection: `q = (9n+5)/8`, `u = (2q+1)/3`, `z = (q−1)/6`; and `n → 8z+1 → 6z+1 = q` are two ordinary arrows with valuations `(1, 2)`.
2. **Adjacent identity.** With `D(q) = [q+2] − [q]`, `P(u) = div K − D(q) + Σ c(v)P(v)`, where every helper has `ρ(v) ≤ (3q+7)/4 < n = (8q−5)/9`. A supplied `D(q)` current gives `P(u)` and conversely, with the same smaller helpers; the two conversions compose to the original current row for row. The adjacent current stays a premise with coefficient `−1`.
3. **Mixed basis.** Eliminating returning requests from any finite `H_s` terminates and leaves nonreturning pairs and adjacent sources of native height at most `ν(s)`. At the exceptional leading source the height equals `ν(s)`, so the change of basis is not strict progress; the transported old R44 rule at `u = 4629` keeps `P(2197)` at rank `6591 > 6171`.
4. **Limits of simpler moves.** Maximal inverse-`(1,2)` normalisation adds no `W5` domain and is not a quotient dynamics (`κ(27) = κ(31)` but `κ(T27) ≠ κ(T31)`); the two static pair identities `P(z)`, `P(2z+1)` miss the upper component.

No accepted domain is added and no adjacent current is supplied. A constant source gap of two bounds neither merger time, nor exposure depth, nor certificate size.

## Proof

The legacy note "The complete absorption defect as an adjacent-source interface" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written triangular reformulation and exact conditional compiler.**
This covers the entire R58 exceptional branch, with every helper strictly
below its unexpanded height in the original rho order. It adds no accepted
pair domain and supplies no unknown adjacent current. A source gap of two
is not a bound on exposure depth, merger time, or certificate size.

Use absorbed odd Syracuse `S`, elementary minimum `nu`, `W5`,
`P(u)=[3u]-[u]`, and `rho(u)=nu(3u)`. Killed atoms have `[1]=0`.
Write the unchanged formal absorption plan as

    [x]=div J_x + sum_v A_x(v) P(v).

All coefficients are signed integers. The dependencies are the
[unique-excess theorem](../rank-excess-absorption-classification/README.md),
[returning inverse identity](../decreasing-w5-phase-inverse-barrier/README.md),
[original-rho compiler](../critical-image-rank-composition/README.md), and the
[separate sigma rank](../sigma-rank-removes-absorption-overhead/README.md).

### 1. Exact domains and the ordinary defect path

The following three domains are in bijection:

1. R58 exceptional canonical seeds n;
2. `u in E_return`, namely `u in W5`, `u=3 mod9`, and selected `3u`;
3. positive canonical `q=31 mod108`.

Their formulas are

    q=(9n+5)/8,   n=(8q-5)/9,
    u=(3n+3)/4=(2q+1)/3,
    z=(3n-1)/16=(q-1)/6=(u-1)/4.                    (1)

In particular n=27 mod96, z=5 mod18, `3z` is noncanonical,
`nu(u)=nu(z)`, and

    n --(1)--> 8z+1 --(2)--> 6z+1=q.                (2)

These are exactly two ordinary arrows, not merely two quotient arrows.

**Proof.** The R58 congruences and exact depth4 give n=27 mod96.
Substitution gives(1). The elementary complementarity theorem says
`6z+1=2(3z)+1` is canonical exactly when `3z` is noncanonical;
this is precisely selected `3u=2q+1`. Conversely every canonical
q31 mod108 gives the stated positive integers, the exact depth4, and
the same complementarity. Direct substitution proves both valuations
in(2). The image q is1 mod3 whereas every exceptional n is0 mod3.
Thus consecutive raw R58 defect lifts cannot form a longer chain. ∎

This last fact does not discharge P(u). Converting q to its formal H
plan requests P(u) again, and the old inverse returns the original n.

### 2. A complete adjacent-source theorem

For every q in the domain above define

    D(q)=[q+2]-[q],   a=nu(u)=nu(z),
    c(v)=A_(q+2)(v)-A_a(v),
    K=N_(3u)-N_u+J_(q+2)-J_a,                       (3)

where `div N_x=[x]-[nu(x)]`.

**Theorem.** The exact source identity is

    P(u)=div K - D(q) + sum_v c(v) P(v).             (4)

Every nonzero helper satisfies the uniform original-rho bound

    rho(v) <= (3q+7)/4 < n=(8q-5)/9.                (5)

The gap in the last inequality is `(5q-83)/36>=2`, since q>=31.
In particular the helper currents can be supplied by a strict induction
below the original unexpanded height n. The single adjacent input is
still missing and occurs with coefficient **minus one**.

**Proof.** The two normalizers have combined boundary
`P(u)-[q]+[a]`. Adding the two formal H currents in(3) gives
`P(u)+D(q)-sum c(v)P(v)`, proving(4) with both signs.

For the lower H input, a<=z and the existing general bound is

    rho(v) <=(9z+5)/8=(3q+7)/16 < n.

Put h=q+2, which is1 mod4. If h is1 mod8, its first ordinary arrow is
exactly valuation2, reaching y=(3q+7)/4. Here y=1 mod3. Every formal
H_y request has rho<=y: R58's unique exception is0 mod3, and normalizing
a noncanonical y only reduces the bound. If h is5 mod8, its elementary
minimum is at most `(h-1)/4=(q+1)/4`. The generic bound gives

    rho(v) <=(9q+29)/32 < (3q+7)/4.

These are precisely the two prescribed branches of H_h and prove(5)
for its complete signed request vector. Combining opposite coefficients
cannot introduce a higher request. Finally, q>=31 proves the strict
comparison with n including the integer offset. ∎

There is also an actual one-arrow descent from h=q+2 below n, since
`v2(3h+1)>=2` and

    S(h) <= (3q+7)/4 < n.                            (6)

This is one ordinary arrow with its actual valuation retained. It does
not give a path from q. Likewise(4) is an equality of finite currents
with missing premises, not a claim of a common-tail clock for P(u).
The supplied adjacent current can have arbitrarily large or unknown cost.

#### Checked conversion in both directions

Given exact currents C_D for D(q) and C_v for every nonzero helper,

    C_P=K-C_D+sum_v c(v) C_v                         (7)

has boundary P(u). Conversely, given an exact C_P and the same helper
currents,

    C_D=K-C_P+sum_v c(v) C_v                         (8)

has boundary D(q). Applying these two conversions consecutively recovers
the original supplied current row for row. The compilers check the
original pair boundary, the adjacent boundary, every helper boundary,
and integer coefficients. Missing or malformed supply is rejected.

Thus the complete returning defect and the adjacent comparison are
equivalent modulo strictly smaller old-rho inputs. This is an exact
remaining joint type. The constancy of the source gap does not prove
that its current exists universally.

### 3. Every formal absorption plan admits a height-bounded mixed basis

Replace an E_return request in H_s by(4), with its full signed multiplier,
and combine equal requests. Repeat at the largest remaining E_return
rank. Each replacement introduces only ordinary pair helpers of rank
strictly below n(u)<rho(u), together with the retained adjacent source.
Therefore this formal elimination terminates for every finite H_s.

Assign the native height `rho(v)` to each remaining nonreturning pair
P(v), and height `n(q)=(8q-5)/9` to D(q). Every final source has native
height at most `nu(s)`.

**Proof of the bound.** By R58 all original pair requests have rank at
most nu(s), apart from the unique possible exceptional request. Its
adjacent replacement has height exactly nu(s) and its helpers have
strictly smaller rank. Every other replacement starts at rank at most
nu(s), and all its new heights are smaller still. The same argument
applies to subsequent replacements. Largest-first strict integer rank
descent proves termination; it does not construct the retained adjacent
currents. The returned signed identity is checked in full. ∎

This gives an exact usable interface with original-height-bounded
dependencies. It is a change of conditional source basis. At an
exceptional n, the leading unknown is now `-D(q)` with native height n,
so the apparent excess has not become strict progress.

It also does not make all old-rho rules compatible with this basis rank.
The accepted R44 rule at u4629 requests P(2197) with coefficient+1.
Here q6943,n6171. Solving(4) for D(6943) and substituting that old rule
retains coefficient−1 at P(2197), whose rho is6591>6171. The new helpers
from(4) have rank at most5209 and cannot cancel this term. Thus even
the fully transported old rule violates the proposed height induction.
Every useful transferred rule must be checked in its chosen rank.

### 4. Why simpler normalization or two smaller pair identities do not close it

#### Maximal inverse-G normalization adds no W5 domain

For canonical q, the ordinary word(1,2) has inverse `(8q-5)/9` whenever
q=4 mod9. The predecessor is positive canonical and smaller. The maximal
count and minimum are exactly

    k=floor(v3(q+5)/2),
    kappa(q)+5=(8/9)^k(q+5).                          (9)

Each inverse lowers the ternary order by2. The actual R58 images have
k=1 exactly. For a W5 critical image, a nonselected q=3u has k=0.
In the selected case q=(3u-1)/2, `q+5=3(u+3)/2`. Every E_return input
has k=1 and zero remainder, but the converse fails: selected u=0 mod9
also has that count, for example u117. Every k>=1 case outside E_return
has u=0 or6 mod9, already in R41's accepted E_good domain; k>=2 forces
u=6 mod9. Thus extending this inverse normalization
does not add a new W5 domain. On the unresolved returning domain its
height is exactly the old sigma value n; the adjacent basis above makes
the unresolved source explicit instead of treating that height as supply.

Moreover kappa is not a quotient for T=nu S: kappa(27)=kappa(31)=27,
but kappa(T27)=41 and kappa(T31)=47. One cannot define its dynamics by
choosing an arbitrary representative. This is a limitation of that
proposed quotient, not of ordinary unequal-time current identities.

#### Static use of P(z) and P(2z+1) misses the upper component

For the entire actual z domain, q=6z+1 is canonical. It differs from
each elementary minimum of

    z, 3z, 2z+1, 6z+3.

The first three are smaller than q. The last minimum is either6z+3,
or at most3z+1 if noncanonical. Therefore the functional taking the
coefficient of the elementary q-class vanishes on P(z), P(2z+1),
and every elementary identity, but equals1 on `[q]-[z]`.
No linear combination of those boundary identities alone supplies the
joint comparison. A new dynamic comparison or another source type is
required; D(q) is the exact remaining type in(4).

This static statement does not limit inspecting internal rows of
supplied currents and extracting further paths. Their retained histories
may already connect q to a known component, which is additional evidence
not represented by these two pair boundaries alone.

### 5. Evidence and scope

`adjacent_defect.py` provides the complete-domain interface, both checked
conversions, and finite elimination of returning requests into the mixed
basis. No API discovers unknown absorption. The checker tests the domain
bijection, all signed source identities, strict helper heights, inverse-G
scope, the two concrete rank/quotient counterexamples and stored supplied
currents under finite path caps.

Run `python3 experiments/residual_progress/defect_normal_form/check_adjacent_defect.py`.
The receipt checks512 complete defect plans,1024 mixed absorption plans,
4096 W5 inverse-normalization cases, both exact counterexamples, and
eight invalid/missing-supply rejections. Three bidirectional conversions
at u21,93,4629 store all original and reconstructed currents and the
three distinct supplied helper pairs. Their pair outputs have40,15,94
rows, and their adjacent outputs have45,14,104 rows. Both round trips
recover the original current exactly. Finite fixture discovery has cycle
detection, a10000-step cap and a512-bit cap; symbolic APIs do not search.
The adjacent current remains a premise in every symbolic result. This is
not a sixteenth accepted rule, universal completion, a bounded-depth
certificate theorem, or a novelty claim.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_adjacent_defect.py` (about 7 s; the counts of section 5 of the note and the three stored bidirectional conversions, compared with `adjacent_defect_audit.json`). The commands in the legacy text name `experiments/residual_progress/defect_normal_form/`.

## Remarks

- **Continued in** [`native-height-inverse-obstruction`](../native-height-inverse-obstruction/README.md) (R68: an all-ray inverse barrier at the native height `n` and a fixed forward certificate on one family) and the failed-hypothesis audit [`retained-lower-currents-adjacent-source`](../../attempts/retained-lower-currents-adjacent-source.md). The adjacent domain remains open.
- Not a rule of [`seventeen-family-rho-dispatcher`](../seventeen-family-rho-dispatcher/README.md).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/defect_normal_form/ADJACENT_DEFECT_INTERFACE.md` (legacy ID R65) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written triangular equivalence and checked conversion in both directions; no new accepted domain".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `793e835`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
