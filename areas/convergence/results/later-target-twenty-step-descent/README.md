---
id: later-target-twenty-step-descent
kind: result
title: "The thirteenth-target transition of the 11547 family has a complete original-rank decision, with first descent as late as step 20"
status: written
claim: >
  Odd-only 3x+1 map S, absorbing at 1, T = nu S; retained critical basis of R75. For every q = 11547 + 3 2^19 k, k
  >= 0, the first thirteen ordinary valuations are exactly (1,2,1,1,1,1,1,2,2,1,1,2,2), with canonical sources and
  raw endpoint R = 70237 + 2 3^14 k; 4(R-1) < 25(q-1). For the full native plan prefix_13(q) + J_R - J_(q/3) with
  signed requests A_R - A_(q/3), the no-pair transitions above q are A(x) = (3x+1)/4, B(x) = (3x-1)/8, C(x) =
  (3x+1)/16 on exact guards; only fourteen above-threshold templates occur (A^j, j <= 6; A^i B A^j, i+j <= 2; C),
  and within seven transitions the procedure either reaches a normal form below q (then every signed request is
  below q) or exposes a unique highest critical request of rank >= q with coefficient +1 that the negative
  frontier cannot cancel: an if-and-only-if decision for this plan. The classes k = 12 mod 16 and k = 20 mod 32
  succeed, k = 1 mod 4 and k = 7 mod 8 fail; R81's cell meets the family exactly when 3^11 divides k. Every member
  keeps the old R44/R52 higher endpoint 55495 + 2^7 3^10 k. On k = 9954 mod 16384 the first quotient descent is
  exactly step 20; ordinary clocks are (ell+beta, beta) with ell = 13..20, no uniform twenty-step ordinary bound.
  Failed leaves and terminal supply stay open; not a whole-dispatcher nonrecognition claim.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, critical-tripling-domain-equivalence, fixed-word-history-cells, returning-forward-interface, returning-second-forward-interface]
certificates: [check_legacy_replay.py]
evidence:
  - "check_history_transition.py, history_transition.py, history_transition_audit.json: the legacy constructor, checker and receipt: 1024 full plans, 70 template instances covering all fourteen words, 144 progression cases, 20 sharp cases, 66 actual old failures, 26 rejections, three supplied outputs outside R81 with 148/153/172 rows. Fails at its new path: history_transition.py loads ../critical_basis/ and ../returning_continuation/ (now ../common-critical-rank-basis/, ../returning-second-forward-interface/) by their pre-migration folder names, and it is loaded in turn by the legacy w9_history_repair/ code (now ../failed-w9-leader-reduction/); and Its receipt pins the SHA-256 of this node's legacy note HISTORY_TRANSITION.md, now an edited README, so it fails at its new path and in a legacy replay. Not reached at be73a66: the scripts/verify_all.py gate stopped earlier, at residual_progress/history_frontier (archive/legacy-checker-run-be73a66.md); it passed in full at 9dbc71a; A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged)"
  - "batch_r84_r85_check.py, batch_r84_r85_check.json: side-lane probe (Claude side lane, 2026-10-18 04:36) of R84 and R85; bounded-history-clock-exclusion replays it from this folder. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/) and fibre_count_check from its own folder (now ../absorbed-fibre-uniform-counts/). Passed at be73a66 as reviews/side_lane/batch_r84_r85_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_b9203ff.md: the main lane's pinned review (2026-10-18) of side commits 49083cb and b9203ff: byte-identical reproductions of batch_r81_r83_check, r56_selected_inverse_check and batch_r84_r85_check, the coverage defect in the R81 probe's ternary-minimality branch (cited from fixed-word-history-cells), and the research decision after PR1"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r84_r85_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 04:36, VERIFIED, main 355c173), with the lane's own step and ν: '**R84, prefix.** On 3,000 random `k`, `q = 11547 + 3·2¹⁹·k` has first thirteen ordinary valuations exactly `(1,2,1,1,1,1,1,2,2,1,1,2,2)`. The raw endpoint is `R = 70237 + 2·3¹⁴·k`, and `4(R − 1) < 25(q − 1)`.' '**R84, sharp descent.** On 300 random `k ≡ 9954 (mod 16384)`, the first quotient step with `T^n(q) < q` is exactly `n = 20`.' 'R84's full decision procedure (the 14 templates and its success and failure classes) was not rebuilt.' The status stays written"
aliases: [R84]
tags: [convergence, outer-residual, smaller-origin-history, original-rank, decision-procedure, quotient-clock]
---

# The thirteenth-target transition of the 11547 family has a complete original-rank decision, with first descent as late as step 20

## Statement

Odd-only clock, 1 absorbing, `T = νS`; the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75), `[x] = div J_x + Σ A_x(v)P(v)`.

1. **Phase.** For every `q = 11547 + 3·2^19·k`, `k ≥ 0`, `b = q/3 ∈ W9`, the first thirteen ordinary valuations are exactly `(1,2,1,1,1,1,1,2,2,1,1,2,2)` (total 18), all sources canonical, ending at `R = 70237 + 2·3^14·k`; and `4(R − 1) < 25(q − 1)`.
2. **Complete decision.** For the plan `C_k = L_q + J_R − J_b`, requests `A_R − A_b`: above `q` the only no-pair transitions are `A(x) = (3x + 1)/4` (`x ≡ 1 mod 8`), `B(x) = (3x − 1)/8` (`x ≡ 3 mod 16`), `C(x) = (3x + 1)/16` (`x ≡ 5 mod 32`). Every raw state with normal form at least `q` follows one of fourteen templates `A^j` (`j ≤ 6`), `A^i B A^j` (`i + j ≤ 2`), `C`; within seven transitions the procedure stops. It succeeds iff every nonzero request of the whole plan is below `q`; otherwise a unique highest critical request of rank `≥ q`, coefficient `+1`, survives and the negative frontier (ranks `≤ b < q`) cannot cancel it.
3. **Initial rows.** `k ≡ 12 (mod 16)` and `k ≡ 20 (mod 32)` succeed entirely; `k ≡ 1 (mod 4)` and `k ≡ 7 (mod 8)` fail; the other rows are decided by 2.
4. **Sharpness.** On `k = 9954 + 2^14·t` the first quotient descent is exactly step 20. Successful leaves have quotient clock `ℓ = 13..20` and ordinary clocks `(ℓ + β, β)` with terminal padding `β`; no uniform twenty-arrow ordinary bound is asserted.
5. **Relation to earlier comparisons.** The family meets the cell of [`fixed-word-history-cells`](../fixed-word-history-cells/README.md) (R81) exactly when `3^11 | k`, so whole successful subprogressions are new. Every member keeps the old R44/R52 higher endpoint `f = 55495 + 2^7·3^10·k`, `ρ(v) = f > q` ([`returning-forward-interface`](../returning-forward-interface/README.md), [`returning-second-forward-interface`](../returning-second-forward-interface/README.md)); this is not a claim about the whole seventeen-family dispatcher.

## Proof

The legacy note "A complete thirteenth-target transition at the original rank" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**R84 — written complete decision for one conditional comparison.**
The entire binary target phase below has a finite arithmetic decision:
either its full signed request vector strictly decreases the original rank,
or an explicitly identified critical request survives with coefficient+1.
Two whole success progressions extend outside R81's fixed-word history cell.
The decision uses at most fourteen possible above-threshold affine states.
Its sharpness example takes twenty quotient arrows to first descent.
This does not cover every critical input, resolve its failed leaves, change
the seventeen-family dispatcher, or supply unknown terminal currents.
No new local orbit identity or novelty is asserted.

Use absorbed odd Syracuse S, elementary minimum nu and T=nu S. Retain
the [R75 critical basis](../common-critical-rank-basis/README.md)
W5 union W9, P(w)=[3w]−[w], rho(w)=nu(3w), and the exact identity

    [x]=div J_x+sum A_x(v)P(v),       rho(v)<=nu(x).       (1)

Both signs and every multiplicity are retained. All atoms at1 are killed.

### 1. The entire next normalization phase

For every integer k>=0 put

    q=11547+3*2^19*k,       b=q/3 in W9,
    R=70237+2*3^14*k.                                    (2)

The first thirteen **ordinary** valuations from q are exactly

    (1,2,1,1,1,1,1,2,2,1,1,2,2),                       (3)

with total18; all thirteen sources before the endpoint are canonical.
Consequently S^13(q)=R and T^13(q)=nu(R).

To check the whole phase, the first twelve anchor quotient states are

    17321,12991,19487,29231,43847,65771,
    98657,73993,55495,83243,124865,93649.

Their accumulated valuations are
(1,3,4,5,6,7,8,10,12,13,14,16). At step j their increments are
2^(19−A_j)*3^(j+1)*k. These preserve every displayed exact valuation
and canonical phase. The twelfth state is93649+8*3^13*k, equal to1 mod8;
its next valuation is exactly2 and gives R. The last normalization is
allowed to vary. In particular it must not be fixed at its anchor value8779.

Let L_q be the thirteen-arrow current. The chosen full conditional plan is

    C_k=L_q+J_R−J_b,       coefficients A_R−A_b.           (4)

Its boundary is P(b) minus that complete signed request source.
The negative frontier has every rank at most b<q. A critical request at
rank at least q in A_R therefore cannot cancel against it.

The following uniform inequality keeps the affine intercept:

    4(R−1)<25(q−1).                                      (5)

It holds separately for the constant and k coefficients in (2).

### 2. Fourteen possible above-threshold templates give an exact decision

At a raw state x, initially R, let n=nu(x).

1. If n<q, stop successfully.
2. If n>=q and n is critical (canonical3 mod4 and not2 mod3), stop
   unsuccessfully. Its unique highest request has rank n, coefficient+1.
3. Otherwise perform the applicable one of the following transitions:

| Letter | Exact guard | New raw state | Current boundary |
|---|---|---|---|
| A | x=1 mod8 | (3x+1)/4 | [x]−[A(x)] |
| B | x=3 mod16 | (3x−1)/8 | [x]−[B(x)] |
| C | x=5 mod32 | (3x+1)/16 | [x]−[C(x)] |

All raw states remain1 mod3. The complete currents for A and C are the
single row e_x. For B the current is

    e_x+e_(S(x))−e_(B(x)),                               (6)

since S²(x)=S(B(x)). It is N_x+e_(nu(x)); the same identity holds
for the A and C currents. Thus the transitions are exactly the
no-pair steps of the retained formal absorption algorithm.

**Theorem.** This decision stops after at most seven transitions, and is
successful if and only if the entire plan (4) has all nonzero critical
requests strictly below q. Every raw state whose normalized value is
still at least q belongs to one of the following fourteen word templates:

    A^j, 0<=j<=6;    A^i B A^j, i+j<=2;    C.             (7)

The empty word is included. The words are read in the actual order of
transitions. Only their legal guarded instances are used. A failed leaf
retains the unique highest critical request with coefficient+1; every
other request in (4) has strictly smaller rank than this leader.

**Proof.** Normalization strips inverse-F steps and may then halve a
selected base. If it strips at least two F steps, or one F step and a
selected-halving step, its shifted height is at most (x−1)/8. By (5)
this is already below q−1. Hence when n>=q at most one F step or one
selected-halving step has occurred. Since x=1 mod3, n then has residue
0 or1 modulo3. A complementary n is therefore critical, giving case2;
there is no above-threshold inverse-descent branch at residue2 mod3.

The only other canonical possibility is n=1 mod8. No normalization
gives guard A; selected-halving with no F step gives x=3 mod16 and
guard B; one F step with no halving gives x=5 mod32 and guard C.
Their formulas are exactly S(n). In every case S(n)=1 mod3.
This proves completeness of the transition table above the threshold.

The exact shifted-height contractions are

    A(x)−1=(3/4)(x−1),
    B(x)−1=(3/8)(x−3)<=(3/8)(x−1),
    C(x)−1=(3/16)(x−5)<=(3/16)(x−1).                     (8)

Seven A letters force below q, since25*3^7<4^8.
Two B letters force below q, because(25/4)(3/8)^2<1.
A C together with any other letter does so because
(25/4)(3/16)(3/4)<1. One B and at least three A letters do so
because(25/4)(3/8)(3/4)^3<1. These cover every word outside (7).

No pair is requested before the stopping state. If its normal form n<q,
all remaining requests are bounded by n. Otherwise it is critical and
the first pair has rank n; the next underlying seed is strictly below n,
so all later requests have smaller rank. The negative A_b frontier has
rank at most b<q<=n and cannot cancel this first pair. This proves both
directions, the unique-leader claim and termination of this exact decision.
It proves nothing about later choices at a failed critical leaf.

### 3. Exact currents and the two clocks

Let j be the number of transitions, x the final raw state, n=nu(x),
and ell=13+j. Add the explicit transition currents to L_q and then N_x;
call the result K. Telescoping gives

    div K=[q]−[n],
    C_k=K+J_n−J_b,       A_R−A_b=A_n−A_b.                (9)

The equality includes the actual current rows, not just their boundaries:
only the no-pair formal absorption steps were separated. All successful
leaves have T^ell(q)=n<q, with13<=ell<=20.

There is also an exact ordinary-prefix compression. Immediately before
N_x, the accumulated current is the ordinary ell-arrow prefix from q,
unless the last letter is B. In that case it is the ordinary
(ell+1)-arrow prefix minus e_x. This follows inductively from (6):
the next positive source row cancels the pending negative row.

Let d_F be the terminal inverse-F depth, and let a=v2(base+1) if
the terminal base is selected. Define the ordinary padding beta by

    beta=a       if the terminal base is selected;
    beta=1       if it is nonselected and (d_F>0 or the last letter is B);
    beta=0       otherwise.                              (10)

Then **row for row**

    K=prefix_(ell+beta)(q)−prefix_beta(n),
    S^(ell+beta)(q)=S^beta(n).                           (11)

For an F-normalization, S(x)=S(base); for selected normalization,
the exact halving identity has clocks(a,a). These facts and the
pending-row description prove (11), including a final B.
The empty negative prefix is allowed. Absorber rows are killed.

Thus ell is the quotient clock; the ordinary clocks are
(ell+beta,beta), with beta depending on the final normalization.
No uniform twenty-arrow ordinary bound is asserted.
Every exact current for a successful plan still requires all signed
terminal P(v) inputs in (9). Missing or malformed supplies are rejected.

### 4. Complete initial rows, and a sharp whole family

The following cases partition every k>=0:

| Parameter phase | Exact outcome for (4) |
|---|---|
| k=1 mod4 | failure |
| k=7 mod8 | failure |
| k=0 mod8 | success iff v=(R−1)/4 is selected |
| k=4 mod16 | success iff m=(3R+1)/16 is not critical |
| k=12 mod16 | success |
| k=2 mod4 | starts with A; use the complete decision |
| k=3 mod8 | starts with B; use the complete decision |

For k1 mod4, R7 mod8. A selected R normalizes to a complementary
canonical root0 mod3; a complementary R is already critical1 mod3.
Either root is at least(R−1)/2>q. For k7 mod8, R11 mod16 is
itself complementary canonical1 mod3 and above q.

For k0 mod8, exactly one F step reaches v3 mod4 and0 mod3.
If v is selected, its further halving gives normal form below q by (5).
Otherwise v is canonical critical and v>q. For k12 mod16,
R21 mod32 permits at least two F removals, immediately below q.

For k4 mod16, v=(R−1)/4 is1 mod8, so transition C reaches
m=(3R+1)/16. One has m>q and m1 mod3. If m is critical it is
the failed leader. A noncanonical m normalizes below q; if m1 mod8,
one A step goes below q. The latter assertions use
(m−1)<(75/64)(q−1), with a factor at most1/2 or3/4 respectively.
In particular k20 mod32 makes m1 mod4, so the entire progression
is successful. The inequalities v>q and m>q follow from positive
constant and k coefficients in R−4q−1 and3R+1−16q.

The seven-transition bound is attained throughout

    k=9954+2^14*t,       t>=0.                            (12)

Here R=1 mod2^15, so A^j(R) is canonical1 mod8 for0<=j<=6.
Exact affine inequalities give

    A^6(R)>q>A^7(R).                                     (13)

The coefficient and intercept of A^6(R)−q are both positive;
those of A^7(R)−q are both negative. Every one of the first twelve
targets from (3) is also above q, by the anchor values and their
positive slope differences. Therefore the **first quotient descent**
is exactly step20 on all of (12). Formula(10) retains its variable
ordinary padding. This is sharp for the specified forward descent,
not a lower bound for every other history or current construction.

### 5. Which earlier claims this extends

Membership of q from (2) in [R81's maximal paired-word
cell](../fixed-word-history-cells/README.md) is exactly3^11|k.
The successful full progressions k12 mod16 and k20 mod32 are not
confined to that cell. Adding, for example, k1 mod3 gives infinite
subprogressions wholly outside it. These comparisons reach a new
smaller future, rather than appending a common suffix to R81's partner.

Every k in (2) still has the old R44/R52 higher request. Its returning
input and first two prescribed endpoints are

    u=(3q+3)/4,       r=(6561q+8965)/1024,
    f=(19683q+27919)/4096=55495+2^7*3^10*k.               (14)

The first exponent is7, r1 mod8, and f is complementary canonical
and1 mod3. Therefore v=(2f+1)/3 belongs to W5 with

    rho(v)=f>rho(u)>q.                                   (15)

It occurs with coefficient+1 in both complete old plans; their smaller
helpers cannot cancel it. This proves a genuine extension of those
particular endpoint comparisons, not nonrecognition by the entire
seventeen-family dispatcher. R75/R37 already supplied the formal
identities used here. No new local orbit identity is claimed.

### 6. Reproduction and limitations

Run:

    python3 experiments/residual_progress/history_transition/check_history_transition.py

The default reconstructs stored supplied currents and verifies their
boundaries; it does not search for unknown absorption paths.
The --write-receipt option prepares only designated finite demonstrations
under stated arrow/bit caps. All failure coefficients and signs remain visible.
The receipt pins this proof and every reachable local source module.
No universal coverage, terminal-current supply or Collatz proof follows.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r84_r85_check.py` (about 1 s, receipt reproduced byte for byte): 3,000 thirteen-arrow prefixes, the inequality `4(R − 1) < 25(q − 1)`, and 300 sharp twentieth-step descents. The legacy checker `check_history_transition.py` is not replayed: it pins the hash of this node's note, now an edited README (see `evidence`). The command in the legacy text names `experiments/residual_progress/history_transition/`.

## Remarks

- Every failed W9 leader of this decision is reduced, at the same original rank, to at most one higher W5 input by [`failed-w9-leader-reduction`](../failed-w9-leader-reduction/README.md) (R87).
- R75 and R37 ([`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md)) already supply the formal identities; no new local orbit identity or novelty is claimed.

## History

- Migrated from `experiments/residual_progress/history_transition/HISTORY_TRANSITION.md` (legacy ID R84) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written complete decision for one conditional comparison; terminal currents remain supplied".
- The main lane's review `side_lane_review_b9203ff.md` (`experiments/residual_progress/`, 2026-10-18) moved here with the side-lane probe it reproduces; it also records the correction to the R81 probe's coverage, cited from [`fixed-word-history-cells`](../fixed-word-history-cells/README.md).
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `355c173`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
