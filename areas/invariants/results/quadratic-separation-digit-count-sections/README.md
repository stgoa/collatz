---
id: quadratic-separation-digit-count-sections
kind: result
title: Mixed sections of a non-eventually-periodic digit-count sequence are pairwise distinct, giving quadratic joint growth
status: formal
claim: >
  Let F be a sequence on the nonnegative integers (any value set) that is not eventually periodic, t_0 >= 0, s_2 the
  binary digit count, and Q_(a,t)(n) = F(t_0 + t + s_2(3^a n)) for a, t >= 0. Then the sequences Q_(a,t) are
  pairwise distinct; Q_(a,t) is reached from g = Q_(0,0) = F(t_0 + s_2(n)) by t binary digit-1 sections followed by
  a ternary digit-0 sections, so the family of sequences obtained from g by at most D binary or ternary section
  operations has at least (D+1)(D+2)/2 members for every D >= 0. Generic statement about sequences: no Collatz
  hypothesis, no Cobham, no finiteness of the value set.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
lean:
  - LeanLane.Quad.Q_injective
  - LeanLane.Quad.Q_mem_Reach
  - LeanLane.Quad.triangle_encard_le
  - LeanLane.Quad.card_triangle
  - LeanLane.Quad.reach_encard_ge
  - LeanLane.Quad.s2_mul_pow_sub
  - LeanLane.Quad.s2_mul_pow_sub_one
  - LeanLane.Quad.s2_balanced
  - LeanLane.Quad.three_pow_dvd
certificates: [verify_examples.py, check_legacy_replay.py]
evidence:
  - "overlap.md: the written theorem (section 2), the corollary (section 3, node digit-count-section-forces-quadratic-growth) and the adjacent-11 control; graph_interface.md: the complete joint section-graph interface (five digit transitions, six radix identities, three root identities); joint_literature.md: the primary-source audit (semigroups of linear growth, the T/U action control)"
  - "QUADRATIC_REVIEW.md, GRAPH_REVIEW.md, VERIFIER_REVIEW.md: main-lane independent agent reviews; side_review.md: the main lane's read of the side-lane feed at sidekick b999b7b"
  - "v006_quadratic_check.py, v006_quadratic_check.json: side-lane probe (64 sequences with a, t <= 7 distinct on a 400-term prefix for F the indicator of powers of 2; no nonconstant digit-count section among the sections of the actual 3x+5, 3x+13, 3x+61 cycle labellings with K <= 9, n < 2^13; the adjacent-11 control fails invariance at 3). It has no failure exit, so check_legacy_replay.py replays it and requires its receipt byte for byte"
  - "delivery_checks.json: historical delivery receipt; no script in the repository regenerates it"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    link: v006_quadratic_check.py
    scope: "Feed 22:26 (REFEREE V006, main ceebb93): theorem reproduced, the two digit-count lemmas checked (odd m < 1000, k <= 40; r <= 6); feed 23:55 and 00:02: Lean V006-a read from source and receipts, statement match in the unconditional form"
  - by: Claude Lean lane (Fable)
    date: 2026-10-18
    scope: "Iteration 8: overlap.md section 2 checked line by line (block identity (5), (6), the balanced quotient (7), both eventual-periodicity contradictions, the triangular count), no error; finite-valuedness never used; then Lean unit V006-a (iteration 10)"
aliases: [V006, V006-a]
tags: [invariants, digit-count, section-growth, quantitative-rigidity, formal]
---

# Mixed sections of a non-eventually-periodic digit-count sequence are pairwise distinct, giving quadratic joint growth

## Statement

For a sequence `F` on `N_0` that is **not eventually periodic** and `t_0 ≥ 0`, put `g(n) = F(t_0 + s_2(n))` and

```
Q_(a,t)(n) = F(t_0 + t + s_2(3^a n)),     a, t ≥ 0.
```

The `Q_(a,t)` are pairwise distinct entire sequences, and if `J_g(D)` counts the distinct sequences obtained from `g` by at most `D` binary or ternary section operations, then `J_g(D) ≥ (D+1)(D+2)/2` for every `D ≥ 0`.

The Collatz consequence (one digit-count section of a nonconstant invariant forces `kappa_h(K+4D) ≥ (D+1)(D+2)/2`) is the separate node [`digit-count-section-forces-quadratic-growth`](../digit-count-section-forces-quadratic-growth.md): it needs V005 and V004 to exclude eventually periodic `F`, and so inherits Cobham's theorem.

## Proof

The written proof is [`overlap.md`](overlap.md) §2: two digit-count formulas, (5) `s_2(m(2^k − c)) = k − δ_m(c)` with `δ_m(c) = s_2(mc − 1) − s_2(m − 1)` for `2^k > mc`, (6) `s_2(m(2^k − 1)) = k` for `2^k > m`, and (7) `s_2((2^K − 1)/3^r) = K/2` for `K` a positive multiple of `2·3^(r−1)` (complementary binary blocks, repeated without overlap). Evaluating `Q_(a,t) = Q_(b,u)` at `n = 2^k − 1` gives `t = u` (else `F` has a nonzero eventual period); for `a < b`, evaluating at `n = 2^k − c` with `c = (2^K − 1)/3^b` gives an eventual period `K/2 + s_2(3^a − 1) − s_2(3^b − 1) ≠ 0`, a contradiction. `Q_(a,t)` is reached in exactly `a + t` operations, and counting pairs `a + t ≤ D` gives the bound.

The legacy V006 report follows, lightly edited.

### 1. A quadratic theorem, with its hypothesis explicit

For any finite-valued F which is not eventually periodic, all sequences

```
n -> F(t+s_2(3^a n)),        a,t>=0,
```

are pairwise distinct. Each is obtained from F(s_2(n)) by t binary
digit-1 sections followed by a ternary digit-0 sections. Thus the joint
section family through depth D has at least(D+1)(D+2)/2 members.

The [complete proof](overlap.md) uses two arithmetic identities. The
digit count of m(2^k-1), for fixed positive odd m, is exactly k for all
sufficiently large k. Also `(2^K-1)/3^r` has exactly K/2 ones whenever
K is a positive multiple of2*3^(r-1). Complementary binary blocks prove
the latter fact. Choosing shifted inputs2^k-c then separates different
ternary exponents; equality would force a nonzero eventual period of F.

This gives a consequence beyond generic infinite-kernel growth. If a
hypothetical nonconstant Collatz invariant has even **one** positive
binary section

```
h(2^K n+r)=F(s_2(n)),       K>=1, 0<r<2^K,
```

then

```
kappa_h(K+4D) >= (D+1)(D+2)/2,       every D>=0.
```

V004's exact mixed-section formulas account for the factor4. If F were
eventually periodic, this section would be automatic, and V005 would
force h constant. Hence the nonperiodicity premise is justified in this
conditional application. For all N>=K, use D=floor((N-K)/4); the bound
has quadratic leading coefficient1/32.

**Missing coverage:** no argument proves that an arbitrary invariant
contains such a section. The all-invariant goal remains open. The
independent [quadratic review](QUADRATIC_REVIEW.md) checks the precise
theorem; root also checked the final proof and the control below.

## Certificates

- [`verify_examples.py`](verify_examples.py) (under a second): main-lane bounded checks against [`verification.json`](verification.json): 18 balanced blocks through `r = 6`; 756 explicit witnesses separating pairs among 28 mixed states at each of two offsets (with `F` the indicator of positive powers of 2); 65,280 exact adjacent-11-pair section evaluations; 15 equal-digit-count witnesses; 10,795 transformation-word witnesses through depth 7; the binary return identities through input 4095. Arbitrary-`F`, whole-function and all-depth claims rest on the written proof and the Lean unit.
- [`check_legacy_replay.py`](check_legacy_replay.py) (about 15 s): replays the side lane's [`v006_quadratic_check.py`](v006_quadratic_check.py) through `tools/legacy_replay.py`, requiring its receipt [`v006_quadratic_check.json`](v006_quadratic_check.json) byte for byte (the three parts listed under `evidence`).

## Lean

Lean unit V006-a, [`lean/QuadraticSeparation.lean`](../../../../lean/QuadraticSeparation.lean) (receipts `lean/receipts/QuadraticSeparation.*`; all reported declarations `propext`, `Classical.choice`, `Quot.sound`), namespace `LeanLane.Quad`: `s2 n := (Nat.digits 2 n).sum`; `EventuallyPeriodic F := ∃ N M, 0 < M ∧ ∀ n ≥ N, F (n+M) = F n`; `Q F t₀ a t` as in the prose. `s2_mul_pow_sub` is (5) in additive form (`s₂(m(2^k−c)) + s₂(mc−1) = k + s₂(m−1)`, hypotheses `0 < m, c`, `mc < 2^k`); `s2_mul_pow_sub_one` is (6); `s2_balanced r j` is (7) with `r+1` for the prose's `r` and `K = 2·3^r·j`, every multiple, by non-overlapping blocks; `three_pow_dvd` is `3^(r+1) | 2^(3^r) + 1`. `Q_injective` is the distinctness theorem with the prose's two steps. `Q_mem_Reach` is the operation count (`Reach g D` is the set reachable from `g` by at most `D` section operations, the prose's `J_D`); `triangle_encard_le`, `card_triangle` and `reach_encard_ge` give `(D+1)(D+2)/2 ≤ encard (Reach g D)` in `ℕ∞`. **Statement match:** exact, in the unconditional form with "`F` not eventually periodic" as hypothesis; finite-valuedness is not used. The Collatz corollary (§3 of `overlap.md`) and its depth accounting are not in this file.

## Remarks

### 2. The next structural shortcuts fail

#### Linear growth need not contain a digit-count section

Let N_11 count adjacent11 pairs and let F indicate positive powers of2.
The sequence z(n)=F(N_11(n)) has cumulative binary kernel count at most2D
for D>=1. It obeys doubling and z(8n+5)=z(2n+1), and every section has
an infinite binary kernel. Yet none of its sections depends only on
binary digit count. Whole-section formulas and equal-weight distinguishing
inputs prove these statements in [overlap.md](overlap.md).

The example fails full invariance at3: z(3)=1 and z(10)=0. It rejects
extraction from the reduced graph hypotheses, not extraction using the
complete Collatz equations or the active goal itself.

#### Linear orbit growth does not give linear semigroup growth

The [primary-source audit](joint_literature.md) examines a genuine theorem
on semigroups of linear growth. Its hypothesis counts transformations,
whereas our bound counts the orbit of one sequence. The explicit maps

```
T(n)=n+1,
U(n)=n+1+1_(n is a positive power of2)
```

have at most2D+1 states reachable from0 through depth D, but all2^D
words of length D define distinct transformations. A distinguishing input
near a large power of2 proves this exactly. These maps are an abstract
action control, not a claimed joint affine-section system.

The audit likewise separates rooted orbit counts from global word-pattern
counts and from the dimension of the full operator algebra. No applicable
general automatic-section theorem was found in this bounded search.

### 3. Decision: retain every radix identity in the overlap problem

The [graph interface](graph_interface.md) records the exact structure
that the controls above omit. Every joint section graph has five digit
transitions, six binary/ternary reordering identities, and compatible
outputs on zero transitions. The root has three additional identities
equivalent to the full Collatz coloring equations.

Conversely, those universal graph identities reconstruct actual sequences
in both bases. Whole-function distinguishability identifies the correct
vertices. This avoids assuming that a rooted orbit is a semigroup quotient.

Linear growth would force arbitrarily distant separating layers of a
fixed finite size. The next bounded probe is whether the full radix and
root identities force an automatic section in such a graph. Start with
the repeated one-vertex case as a discrimination test, then retain the
obligation to cover every possible bound. A proof for one layer size
alone would not complete the goal. No structure theorem for all linear
graphs is being assumed.

| Route | This batch's evidence | Decision |
|---|---|---|
| Distinguish mixed descendants | Exact quadratic theorem from one digit-count section | Retain; extraction remains unproved |
| Extract a digit-count ray from binary growth and return | Exact11-pair counterexample | Reject these reduced premises |
| Import linear-semigroup or low-pattern-complexity structure | Wrong counted object; exact action counterexample | Reject direct import |
| Use the full affine graph | Faithful representation and necessary small-layer condition | Preferred next bounded overlap test; no growth theorem yet |

### 4. Verification and controls

The [verifier](verify_examples.py) and [receipt](verification.json) check
18 balanced blocks through r=6;756 explicit witnesses separating pairs
among28 mixed states at each of two offsets;65,280 exact11-pair section
evaluations;15 equal-digit-count witnesses; and10,795 transformation-word
witnesses through depth7. The concrete mixed-state witnesses use F equal
to the indicator of positive powers of2. The binary return identities are
checked through input4095. Arbitrary-F, whole-function and all-depth claims
rest on the written proofs, not these finite samples.

The actual d5/d61 divisibility invariants and odd fixed cycles are retained.
The verifier exercises failure of the named d1 identity b(3n)=b(4n) on
those controls. The quadratic theorem itself is a generic digit-count
statement; the step excluding eventually periodic F uses the d1 theorem.
These checks do not address hypothetical divergence.

Root replay and [independent verifier review](VERIFIER_REVIEW.md) passed.
During development, the local Python version required replacing bit_count
with an equivalent elementary helper. The independent replay then exposed
a tuple/list serialization mismatch in the draft receipt comparison;
it was fixed and the final unchanged receipt replayed successfully. Neither
issue changed the mathematics. No frozen mathematical code/evidence was
edited, so the historical Phase6 gate was not rerun.

### 5. External input and completion audit

The [side review](side_review.md) records the fresh read-only sidekick pin
b999b7b. Its newest Lean density-dichotomy report is retained as external
verification input, with no new local replay or quantitative-growth premise.
Earlier V004 conditional-formalization scope and D-numbered dispositions
remain unchanged.

The completion requirement is still: for **every** nonconstant finite-valued
Collatz invariant, `sup_D kappa_h(D)/(D+1)=infinity`. This batch proves a
stronger bound only under an additional section hypothesis, and supplies
no extraction theorem covering the full class. Therefore completion is
unproven and the goal stays active. There is no external blocker.

The [delivery checks](delivery_checks.json) record links and exact frozen
comparisons separately from the mathematical review and bounded verifier.

### Scope notes

- The legacy report carried a dated **dependency clarification (V008)**: distinctness with `F` explicitly not eventually periodic is elementary; applying it to an arbitrary nonconstant invariant with a digit-count section excludes eventually periodic `F` via V005/V004 and therefore uses the published Cobham theorem. That application is the separate node [`digit-count-section-forces-quadratic-growth`](../digit-count-section-forces-quadratic-growth.md). The Lean lane raised the point (iteration 8) and the side lane posted it (feed 22:32).
- **No known instance.** The side lane found no nonconstant digit-count section among the actual `3x+5`, `3x+13`, `3x+61` cycle labellings it tested (feed 22:26); those genuine invariants have superlinear section counts, so the control neither supports nor refutes the extraction step that is still missing. The class of the theorem has no known member in any `3x+d`.
- Novelty: none claimed.

## History

- Migrated from `experiments/viewpoints/V006/REPORT.md` (legacy ID V006; Lean unit V006-a) at commit `be73a66`, by the B16 migration (Claude, Opus 5.5). The report text is kept under Proof (§1) and Remarks (§§2–5); Statement, Certificates and Lean added. The V006 notes and receipts moved here, with the side-lane check `reviews/side_lane/v006_quadratic_check.*`.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `ceebb93`; the second batch of the quantitative goal. Lean V006-a verified 2026-10-18/19 (Lean lane iteration 10, `claude/lean-lane` `6fbc3f8`, count closed in `f5a6d76`).
- **Link repair in kept notes (B16 migration, 2026-10-20).** In `GRAPH_REVIEW.md`, `graph_interface.md`, `joint_literature.md`, `overlap.md`, only link targets were changed: relative links to legacy paths now point to the corresponding nodes or to `archive/invariants-viewpoints/`. No text changed. Any `delivery_checks.json` hashes describe historical versions of these notes; no script in the repository checks them.
