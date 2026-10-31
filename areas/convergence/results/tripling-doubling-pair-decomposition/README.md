---
id: tripling-doubling-pair-decomposition
kind: result
title: After the run bridge, every complementary root reduces exactly to tripling and doubling pairs, and adjoining every restricted tripling relation still leaves an infinite actual family unconnected
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1. (Smaller-half comparison) For every complementary x = 2^a t - 1 (a >= 2,
  t = -3^a mod 4), q = (x-1)/2 and 3^(a-1) t - 1 = 2^d w: S^(a-1)(q) = w exactly, and with the run return f of
  complementary-run-bridges (f = 3^k w for d = 2k+1, f = 2 3^k w + 1 for d = 2k) the explicit current C_x has
  div C_x = [x] - [q] - [f] + [w], so the remaining comparison is exactly [f] - [w], which telescopes into tripling
  pairs T(u) = [3u] - [u] and, for even d, one doubling pair D(u) = [2u+1] - [u]. Only two formal types does not
  give a decreasing construction: the parameters can exceed x (for a = 5 mod 8, x = 2^a - 1, the D parameter
  9w is unbounded relative to x). Finite currents for D(u) at every odd u (equivalently at every noncanonical u)
  are equivalent to Collatz convergence by strong induction. (Restricted catalogue) Adjoining the formal edge
  3w -- w for every w = 3 mod 8 to the elementary identities (no arbitrary forward or inverse S arrows) adds exactly
  the quotient edges q -> (q-3)/6 (q = 9 mod 48) and q -> q/3 (q = 33 mod 48); the iterated parent label chi
  classifies the enlarged components, and complementary canonical vertices with a >= 3 are isolated. For every
  a = 3 mod 16, a >= 19, the actual coefficient-1 root x = 2^a - 1 at N = 12 2^(a-4) has post-run pair (3w, w),
  w = (3^(a-1)-1)/8 = 1 mod 24, with chi(3w) != chi(w). This excludes completion by that specified
  one-run-plus-static-catalogue mechanism. It is not logical insufficiency of the hypothetical pair relation in a
  theory allowing other arguments; universal pair existence remains open.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [elementary-bridge-quotient-normal-form, complementary-run-bridges]
certificates: [check_pair_scope_recompute.py, check_pair_domain_external.py, check_legacy_replay.py]
evidence:
  - "check_pair_scope.py, pair_scope.py, pair_scope_audit.json: the legacy local-current interface (compare_half, the augmented formal label, the counterfamily) and checker (the boundary (4) and decomposition (5) on every complementary root through 32767, 741 parameter cases, 4096 hypothetical edges, the bounded quotient through 32767, eight members of (7), seven even-return growth cases; no orbit search). Fails at its new path: pair_scope.py loads ../complementary_bridge/run_bridge.py (now ../complementary-run-bridges/, which itself no longer runs) by its pre-migration path. Passed at be73a66 as experiments/residual_progress/pair_scope/check_pair_scope.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "pair_merge_controls.py, pair_merge_controls.json: side-lane negative controls (Claude side lane, 2026-10-17 21:09, COUNTEREXAMPLE (generic form)): odd w = 3 mod 8 below 4000 whose w and 3w lie in different basins for 3x-1 (357), 3x+13 (100) and 3x+61 (30). Fails at its new path: it imports affine_controls from experiments/packet_currents/negative_controls/ (now ../locally-collatz-like-control-barrier/). Passed at be73a66 as reviews/side_lane/pair_merge_controls.py (archive/legacy-checker-run-be73a66.md, exit 0). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "PAIR_DOMAIN_REVIEW.md: the main lane's research-decision note on the side-lane pair-domain evidence (first committed with the R37-R39 batch, 436f51f; its sections record reviews at main 1603bf3 through a06ef3c), kept under its legacy name; its links were repointed at the migration, and two mentions of the later R43 material are code spans until that batch lands"
  - "pair_domain_external_review.json: the main lane's reproduction (at side-lane commit dbb0dea) of pair_merge_controls.py and batch_r33_r36_check.py (../mixed-shrinking-pair-rules/) with source hashes and four independently reconstructed control paths; side_lane_review_1a2dfc5.json: the main lane's reproduction (at side-lane commit 1a2dfc5) of batch_436f51f_check.py (../critical-tripling-domain-equivalence/), with three W5 control witnesses. Both are reviews of those side-lane probes, not of this result; check_pair_domain_external.py reads both"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (the smaller-half comparison and run return (1)-(4), the telescoping (5) and the D-equivalence, the quotient edge table and the forest argument for chi, the counterfamily (7)-(8)) and re-checked with independent code: (1)-(5) on all 32,768 complementary roots below 2^18, union-find on the 32,768 canonical vertices below 2^17 against chi, the counterfamily for all 49 exponents a = 3 mod 16 up to 787, the growth family to a = 293; all three certificates re-run (exit 0, 4.5 s); the 3x+5 and 3x+13 analogues of (1)-(5) hold and the D-equivalence analogue fails on them exactly where its hypothesis fails. HOLDS WITH CORRECTIONS: one garbled History sentence repaired, no change to the claim"
aliases: [R35]
tags: [convergence, outer-residual, pair-decomposition, tripling-pairs, doubling-pairs, scope, controls]
---

# After the run bridge, every complementary root reduces exactly to tripling and doubling pairs, and adjoining every restricted tripling relation still leaves an infinite actual family unconnected

## Statement

Odd-only clock, `S(1) = 1` for path algebra, state 1 killed; `[u]` is the killed point mass. `ν`, `B` from [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md); the run return `f` and its current `D_x` from [`complementary-run-bridges`](../complementary-run-bridges/README.md).

1. **Smaller-half comparison.** For complementary `x = 2^a t − 1`, `q = (x − 1)/2`, `3^(a−1)t − 1 = 2^d w`: `S^(a−1)(q) = w` (closing valuation `d + 1`), and `C_x = D_x − H_q` has `div C_x = [x] − [q] − [f] + [w]`. Any finite current for `[f] − [w]` added to `C_x` bridges `x` to `q`; with `q` absorbed by a supplied current this certifies `x` at its full weight.
2. **Two formal types.** With `T(u) = [3u] − [u]`, `D(u) = [2u + 1] − [u]` and `k = ⌊d/2⌋`: `[f] − [w] = Σ_(j<k) T(3^j w)` for odd `d`, plus `D(3^k w)` for even `d`. The parameters are unbounded, the R30 relation covers only `T(u)`, `u ≡ 3 (mod 8)`, and multiplication by 3 cycles residues, so consecutive summands cannot all use it when `k ≥ 2`. Finite currents for every `D(u)` (equivalently every noncanonical `u`) are equivalent to Collatz convergence. For `a ≡ 5 (mod 8)`, `a ≥ 13`, `x = 2^a − 1`, the `D` parameter `9w` has `9w/x → ∞`.
3. **Restricted catalogue.** Adjoining `3w — w` for every `w ≡ 3 (mod 8)` to the elementary identities adds exactly the quotient edges `q → (q − 3)/6` (`q ≡ 9 mod 48`) and `q → q/3` (`q ≡ 33 mod 48`); the iterated parent label `χ` of (6) classifies the enlarged components, including paths through larger intermediates, and complementary canonical vertices with `a ≥ 3` are isolated.
4. **Counterfamily.** For every `a ≡ 3 (mod 16)`, `a ≥ 19`, the actual coefficient-1 root `x = 2^a − 1` at `N = 12·2^(a−4)` has post-run pair `(3w, w)`, `w = (3^(a−1) − 1)/8 ≡ 1 (mod 24)`, and `χ(3w) ≠ χ(w)`. This excludes completion by that specified one-run-plus-static-catalogue mechanism. It is not logical insufficiency of the hypothetical pair relation in a theory allowing other arguments, and it asserts no nonconvergence.

Universal pair existence remains open. No novelty, human review or formal verification is claimed.

## Proof

The legacy note "What the paired relation covers, and what remains" follows, lightly edited (headings demoted one level, links pointed to nodes). Its commands name pre-migration paths; see Certificates.

2026-10-17. **Written exact identities and operation-set classification;
bounded executable checks.** Universal pair existence remains open. The
classification below grants a hypothetical pair relation solely to measure
the reach of that named identity catalogue. It does not claim that the pair
hypothesis is logically insufficient for Collatz when other arguments are
allowed. No novelty, human review, or formal verification is claimed.

Use the odd-only Syracuse map S, with S(1)=1 for path algebra and the state1
killed in measures and currents. All pair coefficients below are signed
integer coefficients. Write `[u]` for the killed point mass at u and
`div=I-P`. References are the [elementary normal form](../elementary-bridge-quotient-normal-form/README.md),
the [complete complementary run](../complementary-run-bridges/README.md),
and the [partial shrinking pair construction](../shrinking-paired-return-recursion/README.md).

### 1. The exact smaller-half comparison for every complementary root

Let

```
x=2^a t-1,  a>=2,  t>0 odd,  t=-3^a modulo4,
q=(x-1)/2=2^(a-1)t-1,
3^(a-1)t-1=2^d w,  d>=2,  w>0 odd.
```

The smaller path has the complete prescribed prefix

```
S^(a-1)(q)=w.                                           (1)
```

Its first a-2 valuations are1; its closing valuation is exactly d+1.
Indeed the last numerator is `2(3^(a-1)t-1)=2^(d+1)w`.
The statement includes a=2, when the initial run is empty.

The larger path has a-1 valuations1 followed by valuation2, giving

```
S^a(x)=3*2^(d-1)w+1.                                   (2)
```

Apply the exact valuation2 identity
`S(1+2^e c)=1+3*2^(e-2)c` for odd c and e>=3.
Writing k=floor(d/2), the complete return comparison is

```
d=2k+1: S^(a+k-1)(x)=4(3^k w)+1,   f=3^k w;
d=2k:   S^(a+k-1)(x)=2*3^k w+1,     f=2*3^k w+1.        (3)
```

In the odd case the sibling identity `S(4f+1)=S(f)` supplies a finite
signed current from x to f; in the even case the displayed path does so.
Call this explicit current D_x, with `div D_x=[x]-[f]`, and let H_q be the
path current in (1). The exact local comparison current is

```
C_x=D_x-H_q,
div C_x=[x]-[q]-[f]+[w].                               (4)
```

Thus the remaining comparison is precisely `[f]-[w]`. Adding any finite
current for it to (4) gives a bridge from x to its smaller half q. If q is
already absorbed by a supplied current, this certifies x. Every coefficient
may be multiplied by the actual source weight; no weight2 source is lost.
Independent root certificates can reuse a known lower-seed proof. This is
not a simultaneous source-capacity assertion for an annular submeasure.

The parameters are constrained: `2^d w+1` is divisible by `3^(a-1)`.
In particular w is1 modulo3 for odd d and2 modulo3 for even d. The checker
retains that integrality condition rather than sampling arbitrary triples.

### 2. Two formal pair types, without a universal construction

Define the two signed source types

```
T(u)=[3u]-[u],      D(u)=[2u+1]-[u],      u>0 odd.
```

Telescoping (3) gives the exact finite decomposition

```
d=2k+1: [f]-[w] = sum_(j=0)^(k-1) T(3^j w);
d=2k:   [f]-[w] = D(3^k w)+sum_(j=0)^(k-1) T(3^j w).   (5)
```

This is a reduction to two *formal types*, with unbounded parameters and
unbounded k. It is not a finite collection of already proved currents.
The R30 proposed universal relation covers only T(u) with u=3 modulo8.
Multiplication by3 cycles the base residues `(1,3)` and `(5,7)` modulo8;
successive summands in (5) therefore cannot all be assigned that relation
when k>=2. Known elementary doubling bridges cover D(u) when u is
canonical, but cannot simply be assumed on every remaining u.

**Equivalence warning.** Finite-current existence for D(u) for every
positive odd u is equivalent to Collatz absorption for every positive odd
integer. It remains equivalent if requested only at the noncanonical u,
because the canonical cases are already proved elementary identities.

Proof: assuming the D currents, use strong induction on odd x. If x=1 the
claim is settled. For x=1 modulo4 and x>1, `S(x)<x`, so one arrow and the
smaller input suffice. For x=3 modulo4, q=(x-1)/2 is positive odd and
smaller, and the D(q) current plus its already proved input suffices.
A finite exact signed current for the nonnegative source `[x]` forces its
finite functional-graph component to meet the absorber: otherwise summing
divergence on that component gives the contradiction1=0. Its existing
arrows consequently contain an actual path to1. Conversely, if all seeds
absorb, subtract the two finite path currents to obtain every D current.

Nor are the helper parameters automatically smaller than x. For
`a=5 modulo8`, a>=13, take x=2^a-1. Then d=4 and
`U=3^2 w=9(3^(a-1)-1)/16` in the D summand of (5). Here U/x tends to
infinity. Inducting on the original source height cannot assume this D(U)
merely because only two pair types occur.

### 3. Complete scope of adjoining every restricted tripling relation

Let B and nu be R25's canonical set and elementary normal form. Consider
the undirected graph generated by exactly:

- all elementary sibling and selected-halving identities, in both directions;
- the formal additional edge `3w -- w` for every positive w=3 modulo8.

No arbitrary forward S edge or inverse-S operation is included in this
identity graph. If the additional relations are later proved, its paths
become valid composed bridges, but they do not exhaust every possible bridge.

Quotient first by the complete elementary components. For w=3 modulo8,
the upper endpoint `3w` is1 modulo8 and hence canonical. The other endpoint
has exactly these two cases:

| w | q=3w | nu(w) | new quotient edge |
|---|---|---|---|
|3 modulo16|9 modulo48|(w-1)/2|q -- (q-3)/6|
|11 modulo16|33 modulo48|w|q -- q/3|

The first w is selected with a=2; the second is complementary with a=2.
Both lower endpoints are canonical. These are *all* added quotient edges,
not just selected examples.

Define the augmented label chi(x) by first taking nu(x), then repeatedly
applying

```
q -> (q-3)/6,  q=9 modulo48;
q -> q/3,      q=33 modulo48;                           (6)
```

until q is not9 modulo24. Every step strictly decreases a positive integer.
The label chi classifies the complete enlarged identity components.

To prove completeness, every possible added edge is in the table and joins
a canonical vertex to its unique smaller parent. Every elementary edge
has already been collapsed by nu. Following parents terminates; the two
ends of each edge have the same terminal label. Conversely every vertex
has its finite parent path to that label. Thus equality of labels is both
necessary and sufficient for connection, including paths through arbitrarily
large intermediate states.

In particular every complementary canonical vertex with a>=3 is7 modulo8
and is incident to **no** new quotient edge: upper endpoints are1 modulo8,
and lower endpoints are1 modulo8 or11 modulo16. Such a vertex is an isolated
quotient vertex in this enlarged graph. This statement concerns the named
static identity catalogue only. Advancing an actual Syracuse path may
reach another component and is a separate operation.

### 4. Infinite actual roots remain unresolved after the full first run

The preceding limitation persists after the R26 first run on an explicit
family. For every

```
a=3 modulo16, a>=19,
x=2^a-1, q=2^(a-1)-1, N=12*2^(a-4),
w=(3^(a-1)-1)/8, f=3w,                               (7)
```

x is an actual coefficient1 complementary R'_N root: N is a required
ray cutoff, q<N<x, `9N/8<x<3N/2`, x=7 modulo12, and a is odd.
Since `a-1=2 modulo16`, `3^(a-1)=9 modulo64`, so d=3 and w=1 modulo8.
Also w=1 modulo3; hence w=1 modulo24, already a terminal label for (6).

If w=1 modulo16, 3w is selected with a=2 and

```
nu(3w)=(3w-1)/2=1 modulo8 and1 modulo3.
```

This is another terminal label1 modulo24, strictly larger than w since
w>1. If w=9 modulo16, 3w=11 modulo16 is complementary canonical and is
again terminal for (6), distinct from w. Therefore in all cases

```
chi(f) != chi(w).                                    (8)
```

Granting *every* restricted relation T(v), v=3 modulo8, thus does not
complete the exact residual comparison (4) for this infinite family using
only the enlarged identity graph. This is an exact operation-set
counterfamily, not a failed capped merger search. Neither (8) nor the
checker asserts nonconvergence. Further forward/inverse arguments or
new pair relations remain available. No logical impossibility statement
about proving Collatz from an augmented theory follows from (8).

The new [missing-domain pair construction](../missing-one-mod-8-pair-domain/README.md)
illustrates this boundary concretely. It uses additional ordinary forward
arrows and reduces some w=1 modulo8 pairs to smaller parameters in the
3-modulo8 domain. In particular the exponent classes a=659 and1699
modulo4096 lie inside (7) and now have explicit smaller-seed mergers.
Their success is consistent with (8): the construction goes beyond the
static identity graph classified in Section3.

### 5. Executable evidence and remaining obligation

```
python3 experiments/residual_progress/pair_scope/check_pair_scope.py
```

The default checker is read-only and compares against
[pair_scope_audit.json](pair_scope_audit.json). `--write-receipt` regenerates
that receipt. It checks the exact current boundary (4) and decomposition
(5) on every complementary root through32767;741 integrality-preserving
parameter cases a2..20,d2..40;4096 hypothetical edges; the complete bounded
quotient graph through32767; eight members of (7); and seven growing
even-return helper cases. All loops have fixed bounds or a proved decreasing
integer. No orbit absorption or unknown merger is searched.

[pair_scope.py](pair_scope.py) exposes the local current with its unresolved
pair boundary. Its augmented normal form returns a *formal graph label*,
never a certificate asserting the hypothetical tripling relations.
The isolated graph and pair-type equivalence proofs do not rely on scans.

The constructive obligation is to prove valid currents for the unresolved
pair sources with a well-founded recursion that covers every branch.
R30 supplies such a recursion on selected branches. Formula (5) preserves
the exact remaining targets but supplies neither universal termination nor
a smaller parameter for every rewrite.

## Certificates

- [`check_pair_scope_recompute.py`](check_pair_scope_recompute.py) (written at the B10 migration, under 1 s, standard library). With its own `S`, canonical test, `ν` and `χ` it checks: the smaller prefix, the run return and the exact telescoping (5) for all 4096 complementary roots below 32768; the 741 parameter cases, the 4096 hypothetical edges and the 8192-vertex bounded quotient, each against the SHA-256 recorded in [`pair_scope_audit.json`](pair_scope_audit.json); and the eight counterfamily members and seven even-return growth samples field by field. It does not recompute the receipt's `comparison_hash`, which covers the legacy signed currents (legacy checker, evidence only).
- [`check_pair_domain_external.py`](check_pair_domain_external.py) (main lane, instant, standard library; it checks by `assert`, so run it without `-O`). It checks the seven saved finite control witnesses of [`pair_domain_external_review.json`](pair_domain_external_review.json) and [`side_lane_review_1a2dfc5.json`](side_lane_review_1a2dfc5.json): for maps `3x−1`, `3x+13`, `3x+61`, a tripling pair `(w, 3w)` whose endpoints enter different components (one an absorber, the other a nonabsorbing cycle), every arrow and closing cycle arrow, and the nonzero basin-indicator pairing, so no finite exact current exists for those control pairs. It passes at its new path. At `be73a66` it ran only inside `scripts/verify_all.py`, after the gate's stopping point at `residual_progress/history_frontier` (archive/legacy-checker-run-be73a66.md; the gate passed in full at `9dbc71a`).
- The command in the legacy text names `experiments/residual_progress/pair_scope/`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy checks `check_pair_scope.py`, `pair_merge_controls.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 21 s). It checks finite steps only; the status is unchanged.

## Remarks

- **Controls.** The side lane's `pair_merge_controls.py` (feed 2026-10-17 21:09) shows that the generic statement "`w` and `3w` share a future" fails at many `w ≡ 3 (mod 8)` below 4000 on `3x−1` (357), `3x+13` (100) and `3x+61` (30, on its 41-cycle; that map is locally Collatz-like). A rule certifying every tripling pair must therefore use arithmetic these maps lack; the statement for `d = 1` is not tested. The main lane's [`PAIR_DOMAIN_REVIEW.md`](PAIR_DOMAIN_REVIEW.md) records the scope corrections: the controls absorb both 1 and `d`, and R35 also needs tripling pairs beyond `3 (mod 8)`. The same controls fail on the critical domain `W` of [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md).
- **Beyond the static catalogue.** [`missing-one-mod-8-pair-domain`](../missing-one-mod-8-pair-domain/README.md) resolves the classes `a ≡ 659, 1699 (mod 4096)` inside the counterfamily (7) with additional ordinary arrows, consistently with item 4. The doubling pairs are the subject of [`coupled-even-pair-recursion`](../coupled-even-pair-recursion/README.md).
- No novelty is claimed.

## History

- Migrated from `experiments/residual_progress/pair_scope/PAIR_SCOPE.md` (legacy ID R35) at commit `be73a66`, by the B10 migration (Claude, Opus 5.5). Note, scripts and receipt moved byte-identical, with the side-lane probe `reviews/side_lane/pair_merge_controls.*` and the root files `experiments/residual_progress/PAIR_DOMAIN_REVIEW.md`, `check_pair_domain_external.py`, `pair_domain_external_review.json` and `side_lane_review_1a2dfc5.json`. The migration plan placed `side_lane_review_1a2dfc5.json` with R37; it sits here because `check_pair_domain_external.py` reads it from its own folder. `check_pair_scope_recompute.py` was added at the migration. Legacy status: "written identities, complete static component classification and scoped counterfamily".
- Main lane (ChatGPT, Codex), 2026-10-17, from commit `1603bf3`; `PAIR_DOMAIN_REVIEW.md` and its checker from `436f51f` onward. The batch report (archive/convergence-residual-progress/REPORT.md) records "independent model" proof and code audits for this batch; they were the main lane's own agents, so they do not count as an independent review. No side-lane verification of R35's own identities is on record; the side lane's controls are evidence, not a review.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Correction: the preceding History bullet had the batch-report sentence spliced into the file name `PAIR_DOMAIN_REVIEW.md`; reordered, no text removed. Two imprecisions are noted in the review (the growth example of Statement 2 also holds at `a = 5`; `check_pair_domain_external.py` checks by `assert` only); see [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
