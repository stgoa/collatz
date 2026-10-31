---
id: fixed-word-history-cells
kind: result
title: "Every merger with two fixed exact valuation words lies in one maximal integer cell, with an exact smaller-origin test"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1. If positive odd anchors q0, p0 have exact ordinary valuation words alpha,
  beta (lengths a, b, totals A, B) with equal endpoints, then all positive odd pairs with the same exact words and
  a common endpoint are exactly q = q0 + M k, p = p0 + P k (k integer, q, p > 0), M = 2^(A+1) 3^max(b-a,0), P =
  2^(B+1) 3^max(a-b,0), and M is minimal; p < q holds for every k >= 0 if and only if p0 < q0 and P <= M (in
  general exactly when (q0 - p0) + (M - P) k > 0). If rho(w) = q for a critical input w in W5 u W9 and p < q, the
  full current N_(3w) + K + J_p - J_w (div K = [q]-[p]) requests A_p - A_w with every rank below q; every terminal
  current remains a premise. For R80's words (1,2) and (1^6,2,2,1^4,2,6) the entire cell is q = 11547 + 16 3^12 k,
  p = 11391 + 2^23 k, k >= 0 (gap 156 + 114448k, period 8192 times smaller than R80's), with ordinary clocks
  (2,14), quotient clocks (1,13) and peak 32q+17; its local W9 row is blocked exactly as stated by the phase test
  (17)-(18), and on k = 3072 mod 4096, outside the old cell, the R44/R52 requests stay genuinely high while the
  history plan is strict. Raw paired origins only; no universal word selection, terminal supply or seventeen-rule
  nonrecognition.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [common-critical-rank-basis, high-smaller-origin-history, returning-forward-interface, returning-second-forward-interface]
certificates: [check_legacy_replay.py]
evidence:
  - "check_history_lifting.py, history_lifting.py, history_lifting_audit.json: the legacy compiler, checker and receipt: 18 specifications, 189 lifts, 592 memberships, 191 native plans, 62 old-phase records with 38 genuine high requests, 19 rejections, three supplied outputs (b = 3849, 2838201, 8707133193) with 46/100/108 rows and their 5/7/12 input tables; 35 sources pinned. Fails at its new path: history_lifting.py loads ../critical_basis/ and ../returning_continuation/ (now ../common-critical-rank-basis/, ../returning-second-forward-interface/) by their pre-migration folder names; and Its receipt pins the SHA-256 of this node's legacy note HISTORY_LIFTING.md, now an edited README, so it fails at its new path and in a legacy replay at earlier migrations (before rewritten notes were restored from git). Passed at be73a66 as experiments/residual_progress/history_lifting/check_history_lifting.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); A replay at this migration, before the note was edited, passed (exit 0, receipt unchanged). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "batch_r81_r83_check.py, batch_r81_r83_check.json: side-lane probe (Claude side lane, 2026-10-18 04:08, coverage corrected 05:13) of R81 and R83; history-beyond-prescribed-growth replays it from this folder. Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ by repository-relative path (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/batch_r81_r83_check.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: batch_r81_r83_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 04:08, VERIFIED, main 1d58f50, coverage claim corrected at 05:13): '**R81, R80's cell.** ... It was checked for `k = 0..3000` and 300 random large `k`, 3,301 lifts in all. Every lift follows both words and meets, `S²(q) = S¹⁴(p)`, and the gap is `156 + 114448k`.' and 400 random anchor pairs with lifts k = 0..40; 'Halving the 2-part breaks some lift.' Per the 05:13 correction: 'Only binary minimality was tested by execution. Ternary minimality follows from coupled integrality instead.' Signed currents and the blocked-phase decision were not rebuilt (the main lane's review side_lane_review_b9203ff.md in later-target-twenty-step-descent found the coverage defect). The status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Cell theorem (3)-(6) re-derived and brute-forced on 150 random anchor pairs and on the actual 3x+5, 3x+7, 3x+13, 3x+61 cycles (d-uniform); R80 cell on 3101 lifts with fixed phases; blocked-phase test (17)-(18) against the direct R75 test for k <= 5000; k = 512j and k = 3072 mod 4096 endpoint failures; certificate re-run (PASS, exit 0, 9 s). Verdict HOLDS; two imprecisions and typos, no correction to the claim"
aliases: [R81]
tags: [convergence, outer-residual, smaller-origin-history, merger-cells, original-rank, critical-nine]
---

# Every merger with two fixed exact valuation words lies in one maximal integer cell, with an exact smaller-origin test

## Statement

Odd-only clock, 1 absorbing. A word means **exact** valuations; a word of total `A` has a cylinder modulo `2^(A+1)`, including the extra bit.

1. **Maximal cell.** Let positive odd `q0, p0` have exact words `α, β` of lengths `a, b` and totals `A, B`, with equal endpoints. Put `M = 2^(A+1)·3^max(b−a,0)`, `P = 2^(B+1)·3^max(a−b,0)`. All positive odd pairs with the same words and a common endpoint are exactly `q = q0 + M·k`, `p = p0 + P·k`, `k ∈ ℤ`, `q, p > 0`; `M` is minimal. Smaller origins occur at every `k ≥ 0` iff `p0 < q0` and `P ≤ M`; in general exactly when `(q0 − p0) + (M − P)k > 0`. Equal and expansive slopes are realised (`q = 739, p = 725`; `q = 21, p = 19`).
2. **Original-rank transport.** For a critical `w ∈ W5 ∪ W9` with `ρ(w) = q` and `p < q`, `C = N_(3w) + K + J_p − J_w` (`div K = [q] − [p]`) has `div C = P(w) − Σ c(v)P(v)`, `c = A_p − A_w`, every rank below `q`; all terminal currents remain premises.
3. **The R80 cell.** For `α = (1,2)`, `β = (1,1,1,1,1,1,2,2,1,1,1,1,2,6)` the entire cell is `q = 11547 + 16·3^12·k`, `p = 11391 + 2^23·k`, `k ≥ 0`, with `q − p = 156 + 114448k`, ordinary clocks `(2, 14)`, quotient clocks `(1, 13)` and peak `32q + 17`.
4. **Blocked phase.** On this cell the local W9 row is nonblocked for odd `k`; for even `k`, with `Z = 6496 + 3^14·k`, `H = v2(Z)`, it is blocked exactly when `Z/2^H ≡ 3^H (mod 4)`. On `k ≡ 3072 (mod 4096)`, outside the old R80 cell, the R44 and R52 plans keep a genuine higher request (also with native `H`), while the history plan of 2 is strict.

## Proof

The legacy note "Complete fixed-word history lifting at the original critical rank" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written arithmetic lifting theorem and conditional compiler.** This
classifies every positive integer merger with two prescribed ordinary
valuation words. It gives the maximal such cell for the R80 comparison and
an explicit larger blocked subdomain. It is not a universal history-hitting
or terminal-current-supply theorem, and no novelty is asserted.

Use the absorbed odd Syracuse map S, killed atoms [1]=0, and
`div e_x=[x]-[S(x)]`. For a finite valuation word alpha of length a and total
A, its affine formula is

    S^a(x)=(3^a*x+c_alpha)/2^A.                       (1)

The word means **exact** positive valuations at every arrow, not lower
bounds. Its cylinder has modulus2^(A+1), including the extra bit. The empty
word is allowed: a=A=c_alpha=0 and its cylinder is all odd integers.

The [retained critical basis](../common-critical-rank-basis/README.md) supplies
finite formal identities

    [s]=div J_s+sum_v A_s(v)P(v),
    P(v)=[3v]-[v], v in W5 union W9,
    A_s(v)!=0 => rho(v)<=nu(s).                       (2)

No unknown current is supplied by (2). Every remaining signed coefficient,
positive or negative, must be retained or supplied by a checked exact pair
current.

### 1. The exact cell, including the slope boundary

**Theorem.** Suppose positive odd anchors q0,p0 have exact valuation words
alpha,beta, of lengths a,b and totals A,B respectively, and their endpoints
agree. Define

    M=2^(A+1)*3^max(b-a,0),
    P=2^(B+1)*3^max(a-b,0).                           (3)

Then **all** positive odd integer pairs q,p with these same exact words and
the same endpoint are precisely

    q=q0+M*k,       p=p0+P*k,       k integer,
    q>0, p>0.                                      (4)

Here the endpoint may vary with k. The modulus M is minimal for the complete
q solution set. In particular the theorem supplies an exact CRT cylinder,
not merely one sufficient subprogression.

The slope and intercept of the origin relative to the target are

    lambda=P/M=2^(B-A)*3^(a-b),
    delta=p0-lambda*q0,       p=lambda*q+delta.       (5)

For the nonnegative part of (4), strict smaller origins occur for every k>=0
**if and only if** p0<q0 and P<=M. More generally they occur exactly when

    (q0-p0)+(M-P)*k>0,                               (6)

together with the two positivity conditions. Thus an expansive slope P>M
allows only finitely many nonnegative indices with p<q. Equal slope is
allowed if the intercept is strictly negative. These are necessary and
sufficient statements about the **raw smaller-origin condition for these
fixed words**. They are not necessary conditions for all signed-current
constructions or for a normalized origin nu(p)<q.

**Proof.** An exact word's source residue modulo2^(A+1) is unique: iterating
(1), each next exact valuation imposes the next congruence with odd
coefficient3^j, including its extra bit. Hence another source q for alpha
has `q-q0=2^(A+1)*j`. Equality of the two affine endpoints forces

    p-p0=2^(B-A)*3^(a-b)*(q-q0)
        =2^(B+1)*3^(a-b)*j.                         (7)

If b>a, integrality is equivalent to `3^(b-a)|j`. If a>=b no further
integrality condition is required. In either case the resulting difference
p-p0 is divisible by2^(B+1), so the beta word is also exact. This proves
necessity and sufficiency, and the step M in (3) is the smallest possible
positive difference of target solutions. Positivity is the only remaining
restriction. Equations(5)-(6) are then exact linear algebra. Since M,P>0,
both origins are positive at every k>=0. A linear difference positive at
all those indices requires positive initial difference and nonnegative
slope difference, proving the claimed iff. No absorption assumption enters.

For a fully explicit interval of all integer indices, positivity requires

    k>=max(-floor((q0-1)/M),-floor((p0-1)/P)).        (8)

For M>P, also require
`k>=floor(-(q0-p0)/(M-P))+1`. For M=P require q0>p0. For M<P require
`k<=floor((q0-p0-1)/(P-M))`. These formulas include empty and finite cells.

The equal-slope case is real: q739 has word(1,8) to13, and p725 has word
(7,2) to13. All q739+1024k and p725+1024k have gap14. Conversely q21 with
word(6) and p19 with word(1,3,1,2,3,4) meet at1 but have slope256/243;
only k0 is smaller among their nonnegative cell indices. These examples
prevent silently replacing P<=M by P<M or ignoring the intercept.

### 2. Full original-rank source transport

Let Q_alpha,Q_beta denote the exact prefix currents at a pair in (4), and
put

    K=Q_alpha-Q_beta,       div K=[q]-[p].            (9)

For any critical input w in W5 union W9 with rho(w)=q, assume p<q. Then

    C=N_(3w)+K+J_p-J_w,
    c=A_p-A_w,                                     (10)
    div C=P(w)-sum_v c(v)P(v).

Every nonzero request has rank at most max(nu(p),nu(w))<q. The elementary
normalizer N_(3w), all negative prefix rows, and all negative request
coefficients are retained. If exact currents for every nonzero request are
supplied, their signed substitution gives an exact finite current for P(w).
The compiler rejects missing, malformed or wrong-boundary premises.

The ordinary common-tail clocks of K are (a,b). This theorem does not
identify them with quotient clocks; any quotient claim needs its own
normalization argument. Also a complete finite conditional expansion does
not supply its terminal pair currents. The theorem introduces no dispatcher
priority or assumption that every target admits suitable words.

### 3. The maximal cell of the R80 high-history merger

Take

    q0=11547, p0=11391,
    alpha=(1,2),
    beta=(1,1,1,1,1,1,2,2,1,1,1,1,2,6).           (11)

The lengths are2,14 and totals3,22. Their affine formulas are

    S²(q)=(9q+5)/8,
    S¹⁴(p)=(3^14*p+5403385)/2^22.                  (12)

The theorem gives the **entire** positive fixed-word merger cell

    q=11547+16*3^12*k,
    p=11391+2^23*k,       k>=0.                     (13)

Both anchors are smaller than their periods, so negative k yields negative
origins. The corresponding pair input is

    b=q/3=3849+16*3^11*k in W9.

Moreover

    q-p=156+16*(3^12-2^19)*k=156+114448*k>0.        (14)

Thus every member of (13) has the strict original-rank conditional pair
current (10). This cell's target period is8192 times smaller than the
previous sufficient R80 period2^17*3^12. This is a comparison of exact
arithmetic cells, not an orbit probability or a new W5 coverage percentage.

The quotient clocks remain(1,13), meeting at y=(3q+1)/2. To check them,
use the R80 thirteen-arrow base path from p, with prefix totals A_j. The
j-th state now equals its base state plus

    3^j*2^(23-A_j)*k.                                (15)

For j<=12 these increments are divisible by512, preserving all the
canonical phases of the proper lower prefix; its last state is F²(y).
The target q=27 mod48 and y=1 mod8 are canonical. Hence the thirteen lower
quotient arrows meet the target's first quotient arrow at y. In the ordinary
clock the merger is still

    S²(q)=S¹⁴(p)=(9q+5)/8>q.                         (16)

The ordinary common state need not itself remain canonical on the enlarged
cell. No such assertion is needed. All proper lower states after p are above
q: their positive affine slopes relative to q are the same as in R80, and
the twelve exact inequalities `3^j*2^(19-A_j)>3^12` hold. The maximum is
32q+17. Thus this remains a high-history comparison rather than an asserted
direct descent of the displayed target prefix.

### 4. Exact blocked phase and a larger genuine old-failure subdomain

The whole cell (13) must **not** be labeled blocked. For k odd,
`v2(3q-1)>=5`, so the local W9 row is nonblocked. For k even its local depth
is4; put

    Z=6496+3^14*k,       H=v2(Z)>=1,       T=Z/2^H.   (17)

With z=(3q-1)/16 one has3z+1=Z. The local W9 row is blocked exactly when

    T=3^H modulo4.                                  (18)

For H1 this is the noncanonical inverse-F case3z=5 mod8; for H>=2 it is
the selected climber case. The complementary unit phase is canonical.
This proves a complete arithmetic decision for the local branch on (13),
with no finite canonicality extrapolation.

There is also an explicit larger subdomain where the two existing returning
endpoint comparisons retain a genuine high request, even with native H.
Take k=512j. Then (18) holds, its returning input u=(3q+3)/4 has a7, and

    r=(6561q+8965)/1024=1 mod8,
    f=S(r)=(19683q+27919)/4096
     =55495+2*3^21*j=1 mod3.                         (19)

Whenever f is canonical and3 mod4, it is a critical root whose first request
is v=(2f+1)/3 in W5, with rho(v)=f. The full R44 and R52 plans each retain
this request with coefficient+1. Their lower helpers lie below rho(u), and

    f-rho(u)=(15075q+25359)/4096>0,     rho(u)>q.      (20)

The same high request appears in the native H_r and H_f lists. These are
actual failed original-rank requests, not just failures of a loose upper
bound. The new history comparison (10) nevertheless uses only ranks below q.

For a simple complete progression disjoint from the old R80 cell, take

    j=6 mod8, equivalently k=3072 mod4096.             (21)

Then f=11 mod16, which is complementary canonical, so every positive member
of (21) has the stated genuine failures and the smaller-history comparison.
The old sufficient R80 cell corresponds to k=0 mod8192. More generally the
entire condition in(19) can be decided exactly from the canonical phase of
f; no claim of classification is made for other returning parameters, or
for every rule in the unchanged seventeen-family dispatcher.

### 5. Relation to earlier closure and inverse results

This is an arithmetic compiler for prescribed paired histories, not a new
logical notion of absorption.

- The [elementary-fibre theorem](../absorbed-fibre-uniform-counts/README.md)
  starts from one supplied finite cutoff and handles its infinite elementary
  closure. Here p grows with q; no fixed finite supply is asserted to cover
  the entire lifted cell.
- [R29 saturation](../supplied-path-saturation-core/README.md) already allows a
  checked bridge into supplied history. Equations(3)-(10) parameterize exact
  finite bridges on their maximal integer cell and prove their original-rank
  premises; they do not strengthen the abstract bridge inference.
- [R49 inverse lifting](../inverse-only-exclusions-short-forward/README.md) concerns complete
  ancestor exclusion. A path from a smaller origin to a future state of q
  does not imply a smaller ancestor of q itself. No new all-ray exclusion is
  claimed here.
- [R68](../native-height-inverse-obstruction/README.md) and
  [R80](../high-smaller-origin-history/README.md) already use fixed high paired
  histories. The general cell and slope theorem makes that construction
  reusable; (13) removes unnecessary precision from the R80 cell. The
  complement and universal existence of useful paired words remain open.

### 6. Reproduction and evidence

Run from the repository root:

    python3 experiments/residual_progress/history_lifting/check_history_lifting.py

The default reads stored terminal supplies and verifies every exact boundary;
it performs no absorption discovery. The deliberate --write option prepares
only the designated finite fixtures with step/bit caps. The receipt includes
source hashes, complete supplied tables and completed currents, and bounded
independent tests of exact-cell necessity, affine slopes, positive-index
intervals, canonical phases, both clocks and malformed-premise rejection.
Written algebra supplies the unbounded cell statements. Finite successful
lifts do not prove that every remaining input has such a comparison.

The stored audit covers18 anchored/reanchored specifications,189 positive
lifts,592 independent cell-membership tests,191 full native plans, and19
invalid-input checks. Its62 old-phase records include38 verified genuine
higher-request cases; these finite counts are not an acceptance-density
claim. The three supplied demonstrations are b3849, b2838201, and
b8707133193, producing46,100,108 current rows with all5,7,12 terminal-input
tables retained. The last example belongs to (21), outside the old R80
cell. The hash set pins35 reachable source/proof files. Fixture discovery
is capped at10,000 arrows and4,096 bits; default replay reads those supplies.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B13 migration; standard library). The legacy scripts load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `batch_r81_r83_check.py` (under 1 s, receipt reproduced byte for byte): 3,301 lifts of the R80 cell and 400 random merger cells with binary minimality. The legacy checker `check_history_lifting.py` was not replayed at the B13 migration, which predated restoring hash-pinned notes from git; it is now (see below and `evidence`). The command in the legacy text names `experiments/residual_progress/history_lifting/`.

At the B18-replay-revival migration [`check_legacy_replay.py`](check_legacy_replay.py) was extended to replay also `check_history_lifting.py`, which now passes in the legacy layout because rewritten notes are restored from git at `be73a66` (about 15 s in all). It checks finite steps only; the status is unchanged.

## Remarks

- The fixed-word restriction is essential: a single fixed pair of words cannot implement a ternary subdivision of the later coupled cell ([`common-tail-comparison-after-r92`](../../questions/common-tail-comparison-after-r92.md), Known progress), and one fixed word cannot give a smaller origin throughout the cell of [`four-target-history-classification`](../four-target-history-classification/README.md) (R88).
- The side lane's first feed entry claimed a ternary-minimality test that never executed; the main lane's review (`side_lane_review_b9203ff.md` in [`later-target-twenty-step-descent`](../later-target-twenty-step-descent/README.md)) found it and the side lane corrected it at 05:13. Ternary minimality rests on coupled integrality, as written in section 1.
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/history_lifting/HISTORY_LIFTING.md` (legacy ID R81) at commit `be73a66`, by the B13 migration (Claude, Opus 5.5). Note, scripts and receipts moved byte-identical; the note became this README, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Legacy status: "written maximal-cell theorem, conditional signed compiler and exact supplied-current audit".
- Main lane (ChatGPT, Codex), 2026-10-18, first committed in `1d58f50`. The batch's "independent" proof, source and default-replay reviews recorded in archive/convergence-residual-progress/REPORT.md were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No text was changed; the review records two imprecisions (why 512 fixes the phases in (15); 'nonblocked' in section 4 means rho-valid).
