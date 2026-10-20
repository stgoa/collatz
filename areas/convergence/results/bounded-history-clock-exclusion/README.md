---
id: bounded-history-clock-exclusion
kind: result
title: "No uniformly bounded pair of history clocks reaches every critical input, even over all inverse rays"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1, canonical quotient T = nu S. Let canonical q > 0 satisfy 3^D | q, D >= 1,
  and let its first J ordinary arrows have valuation 1 with every state canonical; y_a = T^a(q) = S^a(q) = (3/2)^a
  (q+1) - 1. For every a <= J, the only canonical origin p <= q reaching y_a in at most D+a quotient steps is q
  itself, at depth a; every inverse word and every ray index within that clock bound is included. The
  ordinary-clock version (S^d(p) = S^a(q), d <= D+a) holds for every positive odd q with the same divisibility and
  valuation-one prefix, without canonicality. For H >= max(J+1, 3), the coprime conditions q = 0 mod 3^D, q = 2^H
  u - 1 mod 2^(H+2), u = -3^H mod 4 give an infinite positive progression with q/3 in W5; so no fixed bounds on
  future and partner clocks cover all critical inputs, with the source depending on the bounds. A separate H17 CRT
  family excludes smaller histories to q through D and to its first future through D+1 only. No fixed-source
  nontermination, exclusion of arbitrary signed currents, unrestricted history failure or terminal supply follows.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [elementary-bridge-quotient-normal-form, decreasing-w5-phase-inverse-barrier, common-critical-rank-basis]
certificates: [check_legacy_replay.py]
evidence:
  - "check_history_barrier.py, history_barrier.py, history_barrier_audit.json: the legacy constructor, checker and receipt: 62 quotient and 126 ordinary domains with 3911/16008 origin instances, 196 critical and 60 H17 CRT cells, 200 inverse words with ray indices through 64, 15 equality spines, 1560 ordinary-word attempts, 23 rejections and the supplied nine-row P(13) current for q = 39. Fails at its new path: history_barrier.py loads ../bridge_normal_form/normal_form.py (now ../elementary-bridge-quotient-normal-form/) by its pre-migration path; and Its receipt pins the SHA-256 of this node's legacy note HISTORY_CLOCK_BARRIER.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "../later-target-twenty-step-descent/batch_r84_r85_check.py: side-lane probe of R84 and R85, replayed by this node's check_legacy_replay.py (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../later-target-twenty-step-descent/batch_r84_r85_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 04:36, VERIFIED, main 355c173): '**R85.** These are brute-force finite instances of the all-ray statement. Each has canonical `q = 2^H·u − 1` with `3^D ∣ q`, a valuation-1 prefix of length `J` with canonical states, and `u ≡ −3^H (mod 4)`. There are two instances for each `D ∈ {1, 2, 3}` and `J ∈ {1, ..., 4}`, so 24 in all, with `q` from 39 to 100095. For every `a ≤ J`, every canonical `p ≤ q` was tested against `y_a = (3/2)^a·(q + 1) − 1`. The only one reaching `y_a` within `D + a` quotient steps is `q` itself, at depth `a`.' The all-ray quantifier rests on the written shadow argument. The status stays written"
aliases: [R85]
tags: [convergence, outer-residual, smaller-origin-history, inverse-barrier, clock-bound, crt-construction]
---

# No uniformly bounded pair of history clocks reaches every critical input, even over all inverse rays

## Statement

Odd-only clock `S`, 1 absorbing; canonical quotient `T = νS` with the complete inverse branches of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25) and [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) (R41).

1. **Quotient clock.** Let `D ≥ 1` and let canonical `q > 0` be divisible by `3^D`, with its first `J` ordinary arrows of valuation 1 through canonical states; `y_a = T^a(q) = (3/2)^a(q + 1) − 1`. For every `0 ≤ a ≤ J`, the canonical origins `p ≤ q` reaching `y_a` in at most `D + a` quotient steps are exactly `(p, d) = (q, a)`. Every inverse word and ray index is covered; the bound is on clocks, not on intermediate heights.
2. **Ordinary clock.** For every positive odd `q` with `3^D | q` and a valuation-one prefix of length `J`, canonical or not, the only positive odd `p ≤ q` with `S^d(p) = S^a(q)`, `d ≤ D + a`, `a ≤ J`, is `p = q`, `d = a`.
3. **Critical families.** For `H ≥ max(J + 1, 3)`, `q ≡ 0 (mod 3^D)`, `q ≡ 2^H u − 1 (mod 2^(H+2))`, `u ≡ −3^H (mod 4)` define an infinite positive progression of canonical critical inputs with `q/3 ∈ W5`. Hence no fixed bounds on the future and partner clocks give a smaller-history comparison for every critical input; the source depends on the bounds.
4. **H17.** On `b ≡ (2^(9r+17) − 223)·217^(−1) (mod 2^(9r+18))`, `b ≡ 0 (mod 3^(D−1))`, smaller canonical histories are excluded to `q = 3b` through depth `D` and to its first future through `D + 1`; later exit targets are outside this corollary.

## Proof

The legacy note "Arbitrarily delayed access to smaller histories, including every inverse ray" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R85 — written clock-bound theorem with exact finite checks.** The source
changes with the requested precision. This excludes uniform bounded-clock
history catalogues on the stated critical family, not unrestricted histories,
all signed currents, or absorption of any fixed positive source. It does not
complete the H17 exit type. No novelty is asserted.

Use the absorbed odd Syracuse map S and the canonical quotient T=nu S from
[R25](../elementary-bridge-quotient-normal-form/README.md). A history comparison is
`T^d(p)=T^a(q)` (or its separately stated ordinary-clock counterpart).
Different clocks a,d are allowed. All sources and targets are positive.

### 1. The complete quotient-clock statement

**Theorem.** Let D>=1 and q be a positive canonical integer divisible by3^D.
Suppose the first J ordinary arrows all have valuation1 and all their states
are canonical. Write

    y_a=T^a(q)=S^a(q)=(3/2)^a(q+1)-1,       0<=a<=J.       (1)

For every a in this range, the complete set of canonical origins p<=q
reaching y_a in at most D+a quotient steps is exactly

    (p,d)=(q,a).                                          (2)

In particular there is no strictly smaller partner. Every inverse ray index
and every inverse word within the stated horizon is covered. The bound is
on clocks, not on the height of intermediate states or the ray index.
All displayed targets are at least q>=3, so absorption at1 introduces no
additional inverse branch in a path reaching them.

#### The inverse formulas

The complete canonical inverse branches have base `(A*x+B)/3`, with rows

| x modulo3 | Point | Ray0 | Ray1 |
|---|---|---|---|
|0|none|(8,3)|(16,3)|
|1|none|(4,-1)|(32,19)|
|2|(2,-1)|(64,19)|(128,83)|

A ray at index L>=0 applies `z ->64^L*z+49(64^L-1)/63` to its base.
Write each branch as alpha*x+beta. For all branches and all ray indices,

    alpha>=2/3,       alpha-beta>=1,                        (3)

with strictness in the second inequality for rays. These are the complete
R25/R41 branches, not a truncated inverse search. For positive real x,

    alpha*x+beta >= (2x-1)/3.                              (4)

Indeed every base dominates the right side, and a ray increment equals
`(64^L-1)(base+7/9)>=0`: the smallest base at x>=0 is-1/3.

#### Shadow proof, including the rational-shadow interval

Start any inverse word at y_a. Carry its exact affine representation

    x=lambda*q+c.

Initially lambda=(3/2)^a and c=lambda-1. At every inverse step,

    lambda'=alpha*lambda,       c'=alpha*c+beta,
    lambda'-c'=alpha*(lambda-c)-beta>=1                     (5)

whenever lambda-c>=1. Thus the last inequality holds throughout.
At total inverse depth d, the difference lambda*q has ternary valuation
at least D+a-d. Before each next step d<=D+a this is at least1. Therefore
actual and shadow states have the same residue modulo3, interpreted in
rationals with denominator prime to3 before the shadow becomes integral.

Until the first ray, the only possible inverse is the point branch. These
points exactly undo (1). Before reaching q they are above q; at depth a
they equal q. There is no point branch at q because3 divides q.

Suppose the first ray is chosen from y_k, k>=1, after a-k point undos.
For either ray index L its new affine coefficients are

    lambda=2^(e+6L-k)*3^(k-1),
    c=lambda-m_L,       m_L=(128*64^L+7)/9,                 (6)

where e=6 for Ray0 and e=7 for Ray1. Here m_L is an integer and m_L>=15.
The coefficient lambda is at least32*64^L, so c>0 immediately.

If lambda has a binary denominator, put t=k-e-6L>0. Each further inverse
branch raises its binary exponent by at least1. The first integral shadow
therefore occurs within t further steps, unless the prescribed word ends
sooner. The available ternary precision ensures integrality once the binary
denominator has disappeared. During this initial interval, (4) gives, for
0<=i<=t,

    c_i+1 >= (2/3)^i(c+1)
          >= 3^(e+6L-1)-(2/3)^t(m_L-1)
          >= 3^(e+6L-1)-m_L+1 >1.                         (7)

The positivity is uniform in L: `3^(e+6L-1)>=243*729^L`, whereas
`m_L-1=(128*64^L-2)/9`. The induction using (4) is valid because (7)
keeps each preceding shadow positive. Thus no negative rational shadow can
appear before the first integral one.

Once c is a positive integer, every next branch is integral because its
residue modulo3 agrees with the actual state. It remains positive: the point
branch is available only at c=2mod3 and sends its least positive input2 to1;
the smallest other case is the1mod3 ray at input1, also giving1. All other
base values and ray increments are positive. Canonicality of the shadow is
not required. Equation(5) now gives lambda>=c+1>=2.

If instead the first ray is chosen at q itself, its shadow is already the
positive integer `(16*64^L-7)/9`, and its slopes are `8*64^L/3` or
`16*64^L/3`. Their differences lambda-c are respectively
`(8*64^L+7)/9` and`(32*64^L+7)/9`, both at least1. The same integral-shadow
argument applies directly.

Consequently every state after the first ray has c>0 and lambda-c>=1,
so x=lambda*q+c>q. The point spine has exactly the sole equality (2).
This exhausts every inverse word and proves the theorem.

### 2. The ordinary-clock version needs no canonicality assumption

Suppose q>0 is odd,3^D divides q, and its first J ordinary valuations are1.
For every a<=J and every d<=D+a, the only positive odd p<=q satisfying
`S^d(p)=S^a(q)` is again p=q,d=a. This applies even when the displayed
ordinary prefix is not canonical.

For d<=a, the universal bound `S^d(p)+1<=(3/2)^d(p+1)` already proves the
claim. For d>a let E be the total valuation of the proposed lower word.
Since E>=d>a, inversion of the affine equality has the form

    p=lambda*q+c,       lambda=2^(E-a)*3^(a-d).             (8)

The clock bound gives3^(d-a)|q, so lambda*q and c are integers.
We must justify c>=0 without assuming its whole formal path is integral.
After k lower arrows, of cumulative valuation E_k, the actual-shadow
difference is

    2^(E-a-E_k)*3^(a-d+k)*q.                               (9)

If c were negative, every shadow would stay a negative integer while
E_k<=E-a. At the first noninteger shadow it would still be negative, since
its preceding state is a negative integer. The remaining number of arrows
is at most E-E_k<=a-1. Starting at any negative real, m positive-valuation
affine arrows end strictly below `(3/2)^m-1`: if a numerator stays negative
the result is negative; otherwise division by at least2 is maximized by the
valuation1 map. Thus this remaining tail cannot reach the prescribed
shadow target `(3/2)^a-1`. If there is no noninteger state, its final state
is still negative. This proves c>=0, including a=0.

Finally the same inverse word at upper source-1 starts from target-1.
Every inverse affine map `(2^e*x-1)/3` preserves x<=-1. Hence c-lambda<=-1,
so lambda>=c+1>=1 and p>=q. Equality in (8) would require lambda=1,c=0;
unique prime factorization then forces d=a,E=a, contrary to d>a. This
proves the ordinary theorem. Negative rational shadows were not silently
regarded as negative integers.

### 3. Positive critical families and the H17 implication

For any D>=1,J>=0 choose H>=max(J+1,3) and impose the coprime conditions

    q=0 modulo3^D,
    q=2^H*u-1 modulo2^(H+2),   u=-3^H modulo4.              (10)

The CRT gives an infinite positive progression. Its first J states are
canonical valuation-one states: the complementary unit condition is
preserved as the binary exponent falls, including the final1mod8 state
when that exponent is1. Also q/3=5mod8, so these are actual critical W5
inputs with original rank q.

For any fixed bounds A,B on future and partner clocks, take J=A and
D>=max(B,1). No smaller canonical origin can meet any of the first A future
targets within B quotient steps. Therefore no uniformly bounded-clock
smaller-history catalogue covers all these critical inputs, even allowing
all valuation words, all quotient inverse rays, and unequal times.
The source varies with A,B. This does not exclude a source-dependent
unbounded procedure, other signed comparisons, or Collatz convergence.

There is a direct but deliberately narrower H17 consequence. For any
r>=0,D>=1 impose

    b=(2^(9r+17)-223)*217^(-1) modulo2^(9r+18),
    b=0 modulo3^(D-1).                                    (11)

Again CRT gives infinitely many positive inputs. These are exactly H17
inputs with the stated binary exit order and at least the stated ternary
divisibility. They have b=9mod16, q=3b=11mod16, and a canonical first
valuation-one future `(3q+1)/2`. The theorem excludes smaller canonical
histories to q through depth D and to that first future through D+1.
It says nothing about the later native exit target. In particular it does
not contradict the [R83 all-return-count subfamilies](../history-beyond-prescribed-growth/README.md),
which use later future targets and much longer partner words. No exclusion
of every unrestricted finite history at a fixed H17 input is claimed.

### 4. Original-rank and current scope

A supplied smaller history p<q meeting a target of q gives the exact
prefix difference with boundary[q]-[p]. At a critical parent w of rank q,
adding the full elementary normalizer and formal H_p-H_w in the
[R75 retained W5/W9 basis](../common-critical-rank-basis/README.md) leaves signed
requests all below q. This uses that basis's bound by the source minimum,
not the older W5-only absorption bound. The present theorem says only that no history of the
specified clocks can provide that input. It does not assert that another
finite signed plan cannot cancel its frontier.

The fixed absorbed example q39 illustrates the distinction. Its first two
canonical valuation-one states are59 and89, and3 divides39, so the theorem
applies with D1,J2. Yet T^3(39)=33<39. The checker supplies a complete
finite P(13) current using explicit absorption paths. The next forward
phase is outside the two-target hypothesis; no fixed-seed nontermination
follows from the clock barrier.

### 5. Reproduction

Run `python3 experiments/residual_progress/history_cover_scope/check_history_barrier.py`.
Default replay compares the stored receipt; `--write-receipt` regenerates
only the declared finite checks. These include exhaustive small-origin
forward checks in both clocks, arbitrary supplied inverse words with large
rays, exact CRT phases, noncanonical ordinary controls, the supplied P13
current, and malformed-domain/cap rejections. No unbounded absorption
search or inverse scan is used. The proof supplies the unlimited-ray and
unlimited-parameter quantifiers; finite probes alone do not.

The stored replay covers62 quotient and126 ordinary domains, with3911 and
16008 origin instances respectively; the latter includes64 noncanonical
source domains. It checks196 critical CRT cells,60 H17 cells,200 inverse
words with ray indices through64,15 exact point-spine equalities, and1560
ordinary word candidates (70 legal). The inverse traces include24 positive
rational-shadow rows and2636 positive integer-shadow rows. A complete
9-row P13 current, its supplied paths, and23 rejection checks are retained.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r84_r85_check.py` from [`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md) (about 1 s, receipt reproduced byte for byte), whose 24 brute-force instances check statement 1 exhaustively on small sources. The legacy checker `check_history_barrier.py` was not replayed at the B13 migration, which predated restoring hash-pinned notes from git; it is now (see below and `evidence`). The command in the legacy text names `experiments/residual_progress/history_cover_scope/`.

At the B18-replay-revival migration [`check_legacy_replay.py`](check_legacy_replay.py) was extended to replay also `check_history_barrier.py`, which now passes in the legacy layout because rewritten notes are restored from git at `be73a66` (about 13 s in all). It checks finite steps only; the status is unchanged.

## Remarks

- The absorbed control `q = 39` satisfies the hypotheses with `D = 1`, `J = 2`, yet `T^3(39) = 33 < 39`: the barrier says nothing about fixed-seed nontermination.
- It does not contradict [`history-beyond-prescribed-growth`](../history-beyond-prescribed-growth/README.md) (R83), which uses later targets and much longer partner words; input-dependent unbounded procedures remain open.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/history_cover_scope/HISTORY_CLOCK_BARRIER.md` (legacy ID R85) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written clock-bound theorem, including exact positive critical families".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `355c173`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
