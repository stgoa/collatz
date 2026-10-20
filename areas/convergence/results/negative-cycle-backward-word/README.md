---
id: negative-cycle-backward-word
kind: result
title: The backward word of the negative cycle -17 gives an exact seven-arrow ancestor and strict-rank plans on w = 718 mod 729
status: reviewed
claim: >
  Odd-only 3x+1 map S on positive odd integers. For every positive odd q = -17 mod 2187, p = (2048q - 2363)/2187
  is a positive odd integer with p < q and S^7(p) = q along the exact valuations (1,1,1,2,1,1,4) (q = 4374n -
  17, p = 4096n - 17, n >= 1). For w in W5 with 3w selected and q = nu(3w) = (3w-1)/2 in this class
  (equivalently w = 718 mod 729), with z = nu(w) and H_s the formal absorption plan, the current N_(3w) - path(p
  -> q) + H_p - N_w - H_z has divergence P(w) - A_p + A_z, and every request has sigma < sigma(w) = q (side
  lane) and, by the main-lane review, rho < q: a strict-rho conditional plan whose missing inputs remain
  premises. The domain is exactly the k = 4 domain of two-selected-inverse-choices, so the word gives an
  independent reading of that rule, not extra coverage. The negative cycle -17 explains the affine formula; it
  is not a positive source, and the side lane's enumeration of negative T-cycles (|x| <= 4000) is a finite
  observation that does not prove there are no others. Capped preimage-search rates are finite evidence under
  their caps only.
authors:
  - Claude side lane (Opus)
created: 2026-10-17
depends_on: [sigma-rank-removes-absorption-overhead, critical-image-rank-composition, two-selected-inverse-choices]
certificates: [check_legacy_replay.py]
evidence:
  - "backward_word_rule.py, backward_word_rule.json: side-lane probe (Claude side lane, 2026-10-17): part 1 checks the seven-step word on the R54 family q = 81*2^K s - 17 with 27 | s (12 records, plans validated by main's sigma validator, rho status recorded); part 2 is a measurement of a best-first preimage search (4,000-node budget, cap 64q) on inputs the continued dispatcher leaves unresolved. It imports main's code read-only. Fails at its new path: it imports sigma_rank and continued_rules from experiments/residual_progress/phase_rank/ and continued_rules/ by repository-relative path (now ../sigma-rank-removes-absorption-overhead/, ../low-block-continuation-prescribed-growth/). Passed at be73a66 as reviews/side_lane/backward_word_rule.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "The companion FINDING probe of the same feed entry, negative_cycle_shadows.py (enumeration of negative cycles of T and measurements near their 2-adic shadows), is in ../growing-prefix-unhandled-leading-input/"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-17
    link: side_lane_review_bae3969.md
    scope: "Pinned review of side-lane commit bae3969 (the 23:32 feed entry and backward_word_rule.py), repository base 8764158: the displayed backward word is correct (256 direct ordinary-word examples n = 1..256, every division checked), and its selected-W5 plan decreases rho throughout its exact domain, proved for every input, not only the 12 tested cases; the domain q = -17 (mod 2187) is exactly w = 718 (mod 729), R56's k = 4 domain, and all 12 published R54 family records (r in {1,2,3}, s in {27,54,81,135}) were reproduced and equal the pinned receipt. The probe's 900 random-input acceptance survey, the negative-cycle and returning surveys and the larger-budget percentage were not rerun; no density theorem or universal inverse-search obstruction follows"
tags: [convergence, outer-residual, tripling-pairs, critical-rank, selected-phase, inverse-rays, negative-cycle-shadow, side-lane]
---

# The backward word of the negative cycle -17 gives an exact seven-arrow ancestor and strict-rank plans on w = 718 mod 729

## Statement

Odd-only clock, `S(x) = (3x+1)/2^v2(3x+1)` on positive odd integers, 1 absorbing; `ν`, `ρ(w) = ν(3w)` and `σ` as in [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md); `H_s` the formal absorption plan with signed missing `W5` currents `A_s`.

1. **The word.** For every positive odd `q ≡ −17 (mod 2187)`, write `q = 4374n − 17` (`n ≥ 1`). Then `p = (2048q − 2363)/2187 = 4096n − 17` satisfies `0 < p < q` and `S^7(p) = q`, along the states `4096n−17, 6144n−25, 9216n−37, 13824n−55, 10368n−41, 15552n−61, 23328n−91, 4374n−17` with exact valuations `(1,1,1,2,1,1,4)`. The congruence and oddness of `q` already give `p ≡ −17 (mod 4096)`; no orbit continuation is assumed. Running backward, the inverse exponents are `(4,1,1,2,1,1,1)`.
2. **The plan.** For `w ∈ W5` with `3w` selected and `q = ν(3w) = (3w−1)/2` in this class (equivalently `w ≡ 718 (mod 729)`; then `w ≡ 1 (mod 3)` and `w` is not returning), with `z = ν(w)` and `I` the positive `p`-to-`q` path current, `J = N_(3w) − I + H_p − N_w − H_z` has divergence `P(w) − A_p + A_z`. Every request has `σ < q = σ(w)` (the side lane's argument), and, by the main-lane review, `ρ < q`: `p` is canonical, `≡ 7 (mod 8)`, every `H_p` request has `ρ ≤ p`, and every `H_z` request has `ρ ≤ (9z+5)/8 < q`. `J` is a strict-`ρ` conditional plan; its missing inputs remain premises.
3. **Overlap.** The domain is exactly the `k = 4` accepted domain of [`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md); the ancestor `p` is that rule's endpoint after three inverse point steps, and the rule goes at least as far. In the parametrisation `q = 81·2^K·s − 17` of [`growing-prefix-unhandled-leading-input`](../growing-prefix-unhandled-leading-input/README.md) the word applies exactly when `27 | s`.

The negative cycle `{−17, −25, −37, −55, −21, −31, −23}` of `T` (extended to negative integers) explains the affine formula; it is not a positive source. An arbitrary smaller ancestor need not decrease `ρ`.

## Proof

1. **The word.** Substitute `q = 4374n − 17` (`q` odd and `≡ −17 (mod 2187)` force this form) and check the seven divisions directly; the last is `3(23328n − 91) + 1 = 16(4374n − 17)` with odd quotient. Then `q − p = 278n > 0` and `p ≥ 4079`.
2. **Divergence.** `N_(3w)` has boundary `[3w] − [q]`, `−I` has `[q] − [p]`, `H_p` has `[p] − A_p`, and `−N_w − H_z` has `−[w] + A_z`.
3. **`σ` bound (side lane).** By [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md) every request of `H_s` has `σ ≤ ν(s)`; so every request has `σ ≤ max(p, z) < q`, and `σ(w) = q` since `w ≢ 3 (mod 9)`.
4. **`ρ` bound (main-lane review, section 2 of the review).** `p` is canonical and `≡ 7 (mod 8)`. If `p ≡ 0` or `1 (mod 3)`, its leading critical input is in `W5` with rank exactly `p` and the remaining requests have smaller rank ([`critical-image-rank-composition`](../critical-image-rank-composition/README.md)); if `p ≡ 2 (mod 3)`, the first free inverse step gives the bound `(3p+1)/4 < p`. Hence every `H_p` request has `ρ ≤ p < q`. Also `z < w/4`, so every `H_z` request has `ρ ≤ (9z+5)/8 < q`.
5. **Overlap (review section 3).** `q ≡ −17 (mod 2187)` iff `w ≡ 718 (mod 729)`. With `t = (q+17)/2187`, the `v` of R56 is `v = (32q − 23)/81 = 864t − 7`, and `4v + 1 = 27(128t − 1)`, so `h = v3(4v+1) ≥ 3`; when `h > 3` R56's maximal point block continues to `r + 1 = (2/3)^(h−3)(p + 1)`, so `r < p`.

The full review, with its reproduction script and pinned hashes, is [`side_lane_review_bae3969.md`](side_lane_review_bae3969.md).

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B11 migration; standard library). The legacy scripts in this folder load their sibling modules by pre-migration folder names, so they no longer run here. This certificate rebuilds the legacy directory layout in a temporary directory from the node folders that now hold those files, runs the unmodified legacy checks there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied receipt unchanged. It writes nothing in the repository. It replays: the side-lane probe `backward_word_rule.py` (about 2 s; its receipt, including the 12 R54-family records the main-lane review reproduced, is reproduced byte for byte). The probe's coverage part is a capped measurement; the certificate checks only that it is reproduced exactly.

## Remarks

- **Side-lane finding (feed 2026-10-17 23:32).** Extending `ν` to negative odd integers, `T = νS` has exactly three cycles on `|x| ≤ 4000`: `{−1}`, `{−5, −7}` and the 7-cycle above. The return map `Ψ` of [`growing-prefix-unhandled-leading-input`](../growing-prefix-unhandled-leading-input/README.md) belongs to the 7-cycle and `G` of [`low-block-continuation-prescribed-growth`](../low-block-continuation-prescribed-growth/README.md) to `{−5, −7}`; the R41 word at `h = 2`, `(8q−5)/9 = G^(−1)(q)`, is the backward word of `{−5, −7}`. This enumeration is finite and does not prove that no other negative cycle exists.
- **Measurements (finite, capped).** A best-first preimage search (4,000-node budget, cap `64q`) resolved 29/300, 31/300 and 3/300 of 40-bit inputs in three unresolved classes; raising the budget to 200,000 and the cap to `2^16 q` moved one rate only from 8.7% to 9.3%. None of these caps means permanent failure.
- **Withdrawn heuristic.** The 23:32 entry also argued, in a random-residue model with moment factor `M(θ) = 3^(θ−1)/(2^θ − 1)` (minimum about 0.9465 at the optimum), that "a positive fraction of `q ≡ 1 (mod 3)` have no smaller ancestor at all". The side lane withdrew that sentence at 23:46: a moment bound does not imply it. The main-lane review agrees that no positive-density or universal search-barrier conclusion is justified. The finite census in [`inverse-only-exclusions-short-forward`](../inverse-only-exclusions-short-forward/README.md) is the measured counterpart.
- An arbitrary smaller ancestor can give a `σ`-valid plan that fails `ρ`: in the probe's selected unit-1 sample, 31 plans were `σ`-valid and 30 decreased `ρ`.
- Novelty undetermined (none claimed).

## History

- Claude side lane (Opus), 2026-10-17, feed entry 23:32 (`archive/side_lane/FEED.md` after its migration; legacy `_triage/archive/side_lane/FEED.md`), side-lane commit `bae3969`, probe `reviews/side_lane/backward_word_rule.py`. One sentence of the entry was withdrawn at 23:46 (above).
- Reviewed by the main lane (ChatGPT, Codex) on 2026-10-17 in `experiments/residual_progress/side_lane_review_bae3969.md`, which proved the stronger `ρ` conclusion for every input of the domain and identified it with R56's `k = 4` class. The review's own links were repointed to node paths at the migration (it is not hash-pinned).
- Created as a node at the B11 migration (Claude, Opus 5.5) from the feed entry, the probe and the review; the migration plan had placed these items with R56 ([`two-selected-inverse-choices`](../two-selected-inverse-choices/README.md)). The Statement and Proof summarise the review's sections 1–3 without adding mathematics. `check_legacy_replay.py` was added at the migration.
