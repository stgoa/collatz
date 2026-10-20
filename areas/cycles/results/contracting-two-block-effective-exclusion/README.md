---
id: contracting-two-block-effective-exclusion
kind: result
title: Contracting two-block words with a block repeated three times have denominator above 2^M
status: formal
claim: >
  Raw odd-only clock. Let u, v be nonempty positive valuation words with D_u, D_v > 0 and
  K = D_u·C_v − D_v·C_u ≠ 0, and w = u^k v^ℓ with k, ℓ ≥ 1; put Q = 2^Σu, S = 2^Σv, Q_* = max(Q, S),
  M = max(|u|, |v|). Then den(w) > Q^k·D_v/|K| and den(w) > S^ℓ·D_u/|K|. If a block attaining Q_*
  occurs t_* ≥ 3 times (the other at least once), then den(w) > 2^M·Q_*^(t_*−3) ≥ 2^M > 1, uniformly
  over all such blocks (lengths, totals and slopes may differ). In particular no such word is an
  integer cycle of 3x+1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
lean:
  - LeanLane.Cyc.fixed_pair_bound_u
  - LeanLane.Cyc.fixed_pair_bound_v
  - LeanLane.Cyc.uniform_bound_u
  - LeanLane.Cyc.uniform_bound_v
  - LeanLane.Cyc.uniform_bound_max_u
  - LeanLane.Cyc.two_pow_mul_C_lt
  - LeanLane.Cyc.K_bound
certificates: [c003_variable_blocks_check.py]
evidence:
  - "PROPORTIONAL_UNIFORM.md: the written proof (sections 1-3), effective enumeration (10), proportional comparison (section 4)"
  - "c003_variable_blocks_check.json: receipt of the side-lane check (rewritten identically on each run)"
  - "../two-block-uniform-denominator-growth/variable_blocks_audit.json: main-lane finite receipt (153,696 eligible checks of the strong contracting bound; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c003_variable_blocks_check.py
    scope: "Feed 2026-10-19 00:48, REFEREE C003 at main 7270d95: the effective contracting theorem reproduced on 142,144 exhaustive and 3,000 random eligible cases; worked example and the d = 499 obstruction replayed"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean unit C003-a verified (feed 01:19): (5) and (6) machine-checked as pure algebra from the commutator identities, with C003 section 2's hypotheses; statement match checked by the side lane"
    link: ../../../../archive/side-lane/FEED.md
tags: [cycles, denominators, two-blocks, effective, formal]
---

# Contracting two-block words with a block repeated three times have denominator above 2^M

## Statement

For a nonempty positive word `z`: `Q_z = 2^sum(z)`, `P_z = 3^len(z)`, `D_z = Q_z − P_z`. Take two words `u, v` with **both** `D_u, D_v > 0` (contracting blocks), `K = D_u·C_v − D_v·C_u ≠ 0`, and `w = u^k v^ℓ`, `k, ℓ ≥ 1`. Write `Q = Q_u`, `S = Q_v`, `Q_* = max(Q, S)`, `M = max(len(u), len(v))`, and let `t_*` be the repetition count of a block attaining `Q_*` (when `Q = S`, a block whose count is at least 3 if one exists).

1. **Fixed-pair bounds.** For every `k, ℓ ≥ 1`: `den(w) > Q^k·D_v/|K|` and `den(w) > S^ℓ·D_u/|K|`. (5)
2. **Uniform bound.** If `t_* ≥ 3` and the other block occurs at least once, then

```
den(u^k v^ℓ) > 2^M · Q_*^(t_*−3) ≥ 2^M > 1.        (6)
```

This is uniform over all positive contracting blocks, including different lengths, totals and valuation slopes; primitivity of the blocks or of the word is not assumed. It applies if both counts are at least 3, or if the block with the larger total occurs at least 3 times and the other at least once.

For example, `(1,2,2)^3 (2)` has `C = 213341`, `D = 72023`, `gcd = 1`; both blocks contract, and the uniform lower bound is 8.

## Proof

Written proof: [`PROPORTIONAL_UNIFORM.md`](PROPORTIONAL_UNIFORM.md) §§1–3. Its two ingredients are real interval trapping of block starts and integer lattice spacing after scaling by the cycle denominator:

- With fixed points `a = C_u/D_u`, `b = C_v/D_v`, slopes `α = P/Q`, `β = R/S < 1`, every block-boundary state of the cycle lies strictly between `a` and `b`, and `|b − a| = |K|/(D_u·D_v)`.
- Scaling by `d = den(w)` makes the block-boundary states integers; consecutive differences inside the `u`-run satisfy `Δ_i = (P/Q)^i·Δ_0` with `gcd(P, Q) = 1`, so `Q^(k−1) | Δ_0` and `|Δ_0| ≥ Q^(k−1)` (`Δ_0 ≠ 0` by `K ≠ 0`), while `|Δ_0| < d·|K|/(Q·D_v)`. This gives (5).
- Positive valuations give `0 < C_z < Q_z·3^m/2^m`, hence `x_z = C_z/D_z < F(m) = (9/2)^m + (3/2)^m`, `F` increasing, and `max(a, b) < F(M) < Q_*²/2^M`; the lattice spacing `Q_*^(t_*−1)` then gives (6).

## Certificates

- [`c003_variable_blocks_check.py`](c003_variable_blocks_check.py) (about 2 s; side lane, independent code): (6) exhaustively over contracting words of length ≤ 3 with entries ≤ 4 and counts up to 6, plus random larger words; the worked example; the `d = 499` obstruction of [`interval-trapping-expanding-blocks`](../../attempts/interval-trapping-expanding-blocks.md); and the coprime integer lemma used by [`two-block-uniform-denominator-growth`](../two-block-uniform-denominator-growth/README.md). It rewrites `c003_variable_blocks_check.json` on every run, with identical content.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C003-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md)):

- `LeanLane.Cyc.fixed_pair_bound_u`, `fixed_pair_bound_v`: for `D_u, D_v > 0` and `K ≠ 0`, `Q^k·D_v·gcd(C_w, D_w) < |K|·D_w`, and symmetrically; this is (5) in cleared form.
- `uniform_bound_u`, `uniform_bound_v`, `uniform_bound_max_u`: (6) in cleared form, `2^max(m_u, m_v)·Q_*^(k−3)·gcd < D_w`, for the block `u` attaining `Q_*`, `k ≥ 3`, `ℓ ≥ 1` (and the symmetric version); the tie `Q_u = Q_v` is covered by either lemma.
- Supporting: `two_pow_mul_C_lt`, `K_bound`, and the intercept/fixed-point bounds (7)–(9).

The Lean proofs are purely algebraic, from the commutator identities and `g | K·G_v(ℓ)`, `g | K·G_u(k)`, without the integrality of cycle states that the prose uses; the statements are those of C003 §2 with its hypotheses. Axioms: `propext`, `Classical.choice`, `Quot.sound` (receipts `lean/receipts/CycleSpectrum.*`).

## Remarks

- **Effective finiteness** (written; not formalised): for a ceiling `d_0`, `d ≤ d_0` and (6) force `2^M < d_0`, and `Q_*^(t_*−1) < d_0·F(M)`, `Q_*² < d_0·F(M)` (10); with (5) this is a finite enumeration procedure for every bounded denominator layer of the class, even while both blocks vary.
- **No ineffective cutoff.** Unlike [`two-block-uniform-denominator-growth`](../two-block-uniform-denominator-growth/README.md), this needs no S-unit input.
- **Scope.** Both blocks must contract. Interval trapping fails for expanding blocks, by an actual cycle: [`interval-trapping-expanding-blocks`](../../attempts/interval-trapping-expanding-blocks.md). The result covers unequal-total classes beyond [`equal-total-two-block-exclusion`](../equal-total-two-block-exclusion/README.md), but does not contain every equal-total case, since that result allows the counts `(1, 2)`. `K = 0` is excluded (powers of a common primitive word, e.g. the `d = 1, 5, 7, 13` controls).
- The proportional comparison (`PROPORTIONAL_UNIFORM.md` §4) is the elementary route to the proportional branch of [`two-block-uniform-denominator-growth`](../two-block-uniform-denominator-growth/README.md). Novelty undetermined.

## History

- Split from `experiments/cycle_spectrum/C003/` (legacy ID `C003`; `REPORT.md` §2, `PROPORTIONAL_UNIFORM.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c003_variable_blocks_check.{py,json}` moved here.
- Main lane (ChatGPT/Codex), 2026-10-19; the root supplied the contracting-block argument, independently checked by a separate main-lane agent. Report review required restating `K ≠ 0` explicitly in the standalone theorem and corrected an inclusion overstatement (this result does not contain every C002 equal-total case).
- Formalised by the Lean lane as C003-a, 2026-10-19. The Lean lane noted that the interval-trapping and lattice argument for (5) can be replaced by pure algebra.
