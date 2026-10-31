---
id: mixed-rank-growing-blocks
kind: result
title: "Arbitrarily long growing blocks from two valid comparisons of different ranks, with an exact finite guard count"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; P(w) = [3w] - [w], rho(w) = nu(3w), sigma the separate rank. On the whole
  cylinder w = 40529845 mod 2^26, the accepted sigma fifth-exponent plan at w followed by the accepted rho R44
  returning plan at its high child u has the exact combined current D_(3w,3V) + J_V - J_w, with requests {V: 1} +
  A_V - A_w, V(w) = (531441 w + 311195)/524288 > w; every other request has rho < 3w, and D_(3w,3V) has quotient
  length 12 and ordinary common-tail clocks (13, 1). For every m the progression w = -311195/7153 mod 2^(26+19(m-1))
  admits m growing copies whose currents telescope (clocks (12m+1, 1)), and at any fixed positive guarded input the
  maximal guarded count is exactly 1 + floor((v2(7153 w + 311195) - 26)/19), exiting at valuation 7..25. These
  actual edges rule out a strictly decreasing potential with finitely many labels that is nondecreasing in height
  within each label. Unbounded arithmetic state, other rule choices, richer cancellation, nontermination of fixed
  dispatchers and infinite positive paths are not addressed; the terminal pair current stays missing.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [sigma-rank-removes-absorption-overhead, absorption-defect-original-rank-resolution, returning-forward-interface, rank-excess-absorption-classification, critical-nine-elimination, complementary-run-bridges]
certificates: [check_legacy_replay.py]
evidence:
  - "check_mixed_growth.py, mixed_growth.py, mixed_growth_audit.json: the legacy constructor and checker: 16 full macros, 12 complete prefixes through 16 copies (eight through four copies with every intermediate macro reconstructed), 27 arithmetic families through 256 copies and index 2^128, 76 exact guard exits, seven rejections, and the complete unfinished one- and two-copy currents (62 rows and six requests; 180 rows and 16 requests); the retained counterexample f = 1371 to extending the restricted absorption transport. Fails at its new path: mixed_growth.py loads ../defect_resolution/ (now ../absorption-defect-original-rank-resolution/) by its pre-migration folder name (and through it the R44, R51 and R52 modules); it is loaded in turn by the later legacy mixed_exit/, arithmetic_progress/ and finite_centres/ code. Passed at be73a66 as experiments/residual_progress/mixed_rank_recursion/check_mixed_growth.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran every residual-progress step before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a); replayed unchanged, with its receipt, by check_legacy_replay.py"
  - "../exponent-eleven-exit-continuation/batch_r61_r67_check.py: side-lane probe of R61, R65, R66 and R67 (see reviewed_by)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: ../exponent-eleven-exit-continuation/batch_r61_r67_check.py
    scope: "Finite only (side-lane feed entry 2026-10-18 06:14, VERIFIED), with the lane's own step, nu and selected: on G = {w = 40529845 (mod 2^26)} the map V(w) = (531441 w + 311195)/524288 grows, and the maximal number of consecutive V-steps from G equals 1 + floor((v2(7153 w + 311195) - 26)/19) in all 3,000 cases. The combined current, its cancellation and the potential obstruction were not rebuilt; the status stays written"
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (phases (3), the cancellation (7), the combined current (5) and word (6), the bounds (8), the repetition (10) to (13) and the finite-label pigeonhole); certificate re-run (exit 0); (5) and (7) re-computed row for row with the lane's own absorption plan on 14 cylinder members, the f = 1371 counterexample, m copies through m = 6 and the guard count on 3000 members; verdict HOLDS"
aliases: [R67]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, sigma-rank, mixed-rank, potential-obstruction]
---

# Arbitrarily long growing blocks from two valid comparisons of different ranks, with an exact finite guard count

## Statement

Odd-only clock, 1 absorbing; `ν`, `T = νS`, `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)`; `σ` the separate rank of [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md) (`σ = ρ` off the returning class `E`); formal plans `[x] = div J_x + Σ A_x(v)P(v)` with signed coefficients. Put `V(w) = (3^12 w + 311195)/2^19`.

1. **One block.** On the whole cylinder `w ≡ 40529845 (mod 2^26)`, the accepted `σ` fifth-exponent plan at `w`, followed by the accepted `ρ` R44 returning plan ([`returning-forward-interface`](../returning-forward-interface/README.md)) at its high child `u = (2187w+1209)/1024`, has the exact combined current `C_w = D_(3w,3V) + J_V − J_w` and requests `{V: 1} + A_V − A_w`, with `V(w) > w`; every other request has `ρ < 3w`. `D_(3w,3V)` has quotient length 12 and ordinary common-tail clocks `(13, 1)`.
2. **Repetition and guard.** For every `m ≥ 1`, the progression `w ≡ −311195/7153 (mod 2^(26+19(m−1)))` admits `m` growing copies; their currents telescope, with clocks `(12m+1, 1)`. At any fixed positive guarded input the maximal guarded count is exactly `1 + ⌊(v2(7153w + 311195) − 26)/19⌋`, and the exit valuation lies in `7..25`.
3. **Potential obstruction.** These actual edges rule out a strictly decreasing potential with finitely many labels that is nondecreasing in height within each label.

Not addressed: ranks with unbounded arithmetic state (the decreasing guard valuation is one), other rule choices, richer cancellation, nontermination of fixed-priority dispatchers, infinite positive paths. The terminal pair current stays missing.

## Proof

The legacy note "A complete growing block made from two valid rank comparisons" follows, lightly edited (title dropped, headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

**Status: written exact interface, maximal guarded repetition theorem, and
scoped obstruction to a common potential.** A sigma-decreasing comparison
followed by a rho-decreasing comparison can retain a larger nonreturning
pair, with coefficient+1 after every signed cancellation. The same two
choices can repeat for any prescribed finite length. Their guarded block
nevertheless has an exact finite stopping count on every positive input.
This does not prove nontermination of the mixed union or failure of a richer
rank. It supplies no unknown pair current and does not change any dispatcher.

Use absorbed odd Syracuse S, elementary minimum nu, quotient T=nu S,
P(w)=[3w]-[w], W5, and rho(w)=nu(3w). Formal absorption is

    [x]=div J_x + sum_v A_x(v)P(v),

with all integer signs retained. The sigma rank equals rho outside the
returning class E and is4w/3−1 on E. Dependencies are the
[separate sigma theorem](../sigma-rank-removes-absorption-overhead/README.md),
[complete defect interface](../absorption-defect-original-rank-resolution/README.md),
[returning forward current](../returning-forward-interface/README.md),
[exact absorption bound](../rank-excess-absorption-classification/README.md),
and [critical-nine elimination](../critical-nine-elimination/README.md).
The finite [mixed-dispatch survey](../../attempts/rho-sigma-rank-mixing/README.md) is not a
premise: it studied fixed priorities, whereas this theorem follows two
explicit available plan choices.

### 1. The whole arithmetic cylinder

Set

    A=531441=3^12, B=311195, M=524288=2^19, D=A−M=7153,
    V(w)=(Aw+B)/M.

The domain throughout this section is

    w=40529845 mod2^26, w>0.                              (1)

This is exactly w=−B/D mod2^26. For every member put

    q=3w,
    f=(729w+147)/256,
    u=(2187w+1209)/1024,
    R=(3u−1)/2,
    t=(3u+1)/64,
    r=(243t−1)/2,
    v=V(w), n=3v=(r−1)/4.                               (2)

All these are positive integers. The complete phase gives

    w=437 mod512, u=21 mod512 and3 mod81,
    f=27 mod128 and0 mod3,
    r=125 mod512, n=31 mod128.                           (3)

In particular q and n are nonselected canonical roots, w and v belong to
W5 outside E, u belongs to E, and

    sigma(u)=f < q < n < R=rho(u).                       (4)

The sigma fifth-exponent rule at w is therefore valid. Its unique request
above the original rho rank q is P(u), with coefficient+1. The R44 first
return at u has exact exponent a6 and is rho-valid. Its leading request
is P(v), which increases sigma from f to n.

The inequalities include their offsets:

    q−f=(39w−147)/256>0,
    R−q=(417w+2603)/2048>0,
    n−q=3(Dw+B)/M>0,
    R−n=(39u−307)/512>0.

Thus neither of these individual arrows is valid in both old ranks.
The first increases rho; the second increases sigma.

### 2. Exact combined current, not just an endpoint formula

**Theorem.** Substitute the entire R44 current at u into the entire
sigma fifth-exponent current at w. The resulting current C_w and signed
requests are exactly

    C_w = D_(q,n)+J_v−J_w,
    c_w = {v:1}+A_v−A_w,                               (5)

where div D_(q,n)=[q]−[n]. In particular

    div C_w=P(w)−sum_x c_w(x)P(x).

The coefficient of v is+1 and every other nonzero request has rho<q.
The comparison D_(q,n) has quotient length12 and ordinary common-tail
clocks(13,1). More precisely, its first twelve ordinary arrows have word

    W=(1,1,1,1,2,3,2,1,1,1,1,2),
    S^12(q)=F(n), F(x)=4x+1.                            (6)

Consequently S^13(q)=S(n). The whole P comparison also contains its formal
absorption currents; no single clock is assigned to those supplied terms.

#### Proof of the signed cancellation

The first full R26 block has parameters(5,3), so its first five ordinary
arrows have word1^4,2 and end at F(f). Its comparison to f is that path
plus the elementary sibling current [F(f)]−[f].

The following restricted identity of **actual formal plans** is the key:

    J_f=path(f→R)+J_R, A_f=A_R={u:1}+A_u.               (7)

Here f→R has ordinary word(1,2). To prove(7), put b=f/3, z=(3f−1)/16.
The W9 depth4 local plan consists of the two-arrow path f→R, minus the
two-arrow path b→h, followed by H_R−H_h, where h=2z+1.
The complete H_f plan adds H_b to this pair plan. Its lower part cancels:
b=9 mod16, its first successor y=(f+1)/4 is7 mod32 and canonical,
and h=(3f+7)/8 is11 mod16, canonical, and2 mod3. H_b takes the arrow
b→y, while H_h takes its exact inverse y→h. Hence
H_b=path(b→h)+H_h as both current and request vector. This proves(7).

The congruence f27mod128 is essential to this cancellation argument.
It is false for arbitrary R58 defects: f1371 gives R1543 and
A_f−A_R={29:1}. That concrete counterexample is retained in the receipt.

At the critical canonical R, elementary normalization gives

    J_R=−N_(3u)+J_u, A_R={u:1}+A_u.

The R44 current at u is
N_(3u)+path(R→r)+J_r−J_u, with requests A_r−A_u.
Adding the two complete currents therefore cancels J_u and N_(3u),
including all their signed rows. Since r=F(n), H_r=N_r+H_n and
n=3v is a direct W5 critical root, J_n=J_v and A_n={v:1}+A_v.
The fifth-block negative row at f cancels the first row of path(f→R).
The remaining ordinary word is exactly(6); the final sibling current is
[F(n)]−[n]. This gives(5) row for row, not merely after divergence.

The uniform absorption bound gives all other ranks at most

    max((9v+5)/8,(9w+5)/8)<3w=q.                        (8)

For the v term this reduces to

    (24M−9A)w > 9B+5M,
    24M−9A=7799943 >5422195=9B+5M,

so every positive integer w suffices. The w term is immediate. No lower
request can equal v or cancel its coefficient+1. Finally(3) makes n a
canonical direct W5 root; its R44 rank bound is exactly n<R, so the
second chosen rule is indeed an accepted old-rho comparison. ∎

### 3. Arbitrarily long prefixes and an exact finite maximum

For every integer m>=1 and i>=0 choose

    L=26+19(m−1),
    w0 = (−B D^(-1) mod2^L) + i 2^L,
    w_j=V^j(w0), 0<=j<=m.                             (9)

Every one of the first m parents obeys(1). The sequence is strictly
increasing, and its exact formula is

    D w_j+B = (A/M)^j(D w0+B).                         (10)

This is a complete infinite binary progression for at least m guarded
copies, not a finite-density inference. The binary precision retains the
extra information needed for every stated valuation and canonical endpoint.

For any positive input in(1), let H=v2(Dw+B). Its exact **maximal guarded**
copy count is

    m_max=1+floor((H−26)/19).                            (11)

After those copies the exit valuation v2(D w_exit+B) lies in7..25.
Indeed A is odd, so each copy removes exactly19 binary powers in(10).
The quantity Dw+B is positive and nonzero, so H is finite. This proves
finite termination of this specified guard. It does not show that all
mixed comparisons terminate or that the exit pair is recognized.
Other phases of either plan may remain applicable after this guard stops.

#### The complete finite-prefix source

After substituting m leading requests, every signed term telescopes:

    C^(m)=D_(3w0,3w_m)+J_(w_m)−J_(w0),
    c^(m)={w_m:1}+A_(w_m)−A_(w0).                      (12)

It has a unique largest request P(w_m), coefficient+1, of rank3w_m>3w0.
Every other rank is below3w_(m−1), by(8) applied to the last step.
The ordinary prefix word is W followed by m−1 copies of W with its first
valuation replaced by3. It ends at F(3w_m) after12m arrows, hence

    S^(12m+1)(3w0)=S(3w_m),  T^(12m)(3w0)=3w_m.       (13)

To verify the word, F(x) has the same successor as x and increases its
first valuation by2. Each earlier negative endpoint row cancels the next
positive starting row. This proves both(12) and the clocks without
assigning elementary bridges zero ordinary time.

No finite sequence of strict-rho expansions at the other requests can
cancel the highest coefficient+1. Each such expansion introduces ranks
below its own, hence below3w_m. This is scoped to that completed prefix
and expansions of its nonleading requests. It does not prohibit another
comparison at w_m, another representation of the original source, or a
rational signed-cycle solution involving different rows.

### 4. What common potentials this actually rules out

Suppose a potential uses finitely many labels, and within any fixed label
is nondecreasing as the positive critical height rho increases. It cannot
strictly decrease along **all** of the two chosen valid comparison edges
on their whole domains.

If there are l labels, take m=l in(9). Along the actual dependency path

    w0→u0→w1→u1→...→w_m

the first edge of each pair is the sigma rule and the second is the rho
rule already proved valid. Strict decrease along all edges would strictly
decrease the potential between every two nonreturning w_j. Among their
l+1 labels two agree, but their heights strictly increase by(10),
contradicting within-label monotonicity. This is the finite-label
pigeonhole argument for these actual signed dependencies, not an abstract
graph manufactured from the inequalities between rho and sigma.

The theorem does not exclude a rank with unbounded arithmetic state,
including the decreasing binary guard valuation in(11). It also does not
exclude a different rule choice, cancellation using another current's
internal history, or a common potential that is not height-monotone inside
finitely many labels. Fixed priority dispatchers may select other plans;
no assertion about their whole dependency graph is made. The seed in(9)
changes with m, and no infinite positive growing orbit has been asserted.

### 5. Reproduction and missing inputs

Run `python3 experiments/residual_progress/mixed_rank_recursion/check_mixed_growth.py`.
The checker verifies both individually accepted plans, their exact full
current sum, every retained signed coefficient, direct-prefix equality,
long arithmetic cylinders, exact maximality at all nineteen exit phases,
and ordinary/quotient clocks. Complete unfinished currents are stored for
one and two copies, as are both inputs of the first macro. The higher
terminal pair remains an explicit missing premise; no absorption discovery
is used. Missing supplies are rejected.

The checker uses sixteen full progression members and twelve full
repetition examples through m16. Eight examples through m4 explicitly
reconstruct every intermediate macro and verify row-for-row substitution;
the larger four use the closed current and independently check both clocks.
It separately checks twenty-seven long
arithmetic families through m256 and index2^128, and seventy-six exact
guard valuations. These are bounded implementation checks. The arguments
above provide the infinite quantifiers. Universal current supply, novelty,
and formal or human verification remain unestablished.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the legacy checker `check_mixed_growth.py` (about 5 s; the counts of section 5 of the note and the stored unfinished currents, compared with `mixed_growth_audit.json`). The commands in the legacy text name `experiments/residual_progress/mixed_rank_recursion/`.

## Remarks

- The finite mixed-dispatch survey [`rho-sigma-rank-mixing`](../../attempts/rho-sigma-rank-mixing/README.md) is not a premise: it studied fixed priorities, whereas this theorem follows two explicit plan choices.
- **Built on by** [`valuation-debt-reset-obstruction`](../valuation-debt-reset-obstruction/README.md) (R69), [`mixed-exit-growing-reentry`](../mixed-exit-growing-reentry/README.md) (R70), [`no-finite-affine-valuation-rank`](../no-finite-affine-valuation-rank/README.md) (R72), [`exit18-return-integer-cylinders`](../exit18-return-integer-cylinders/README.md) (R74), [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (R75, which avoids the forced detour through the larger `W5` request), [`uniform-fixed-word-pair-exclusion`](../uniform-fixed-word-pair-exclusion/README.md) (R76) and [`same-seed-factor-complexity-bound`](../same-seed-factor-complexity-bound/README.md) (R77).
- Novelty undetermined (none claimed).

## History

- Migrated from `experiments/residual_progress/mixed_rank_recursion/MIXED_GROWING_BLOCK.md` (legacy ID R67) at commit `be73a66`, by the B12 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical; `check_legacy_replay.py` was added at the migration. Legacy status: "written exact signed interface and scoped potential obstruction".
- Main lane (ChatGPT, Codex), 2026-10-18, from commit `a489973`. The batch's "independent model" proof and code reviews (archive/convergence-residual-progress/REPORT.md) were the main lane's own agents, not a different lane.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction ([`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md)).
