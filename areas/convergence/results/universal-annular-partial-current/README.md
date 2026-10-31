---
id: universal-annular-partial-current
kind: result
title: Every annulus A_N has an explicit partial current that removes positive mass 73N/48 + O(1), leaving the rest unresolved
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1; A_N the six-band annulus of disjoint-annular-recursion, for every N
  divisible by 8. (a) Five short-chain families E, D, B, C, A give a finite current J_cat,N ≤ 0 with
  A_N = (I − P)J_cat,N + Z_N, where Z_N is A_N with the chains' nonzero positions deleted, so
  ‖Z_N⁺‖₁ = 99N/4 − D(N) with D(N) an explicit floor count (D(N) = 3N/2 when 72 | N) and H_L(A_N) ≤ H_L(Z_N) at
  every horizon. (b) Adding all admissible copies of the five-source family of affine-common-tail-tree-lifting
  (C(N) = N/144 + O(1) of them, disjoint from the catalogue) gives a finite current J_N and residual Z_N with
  A_N = (I − P)J_N + Z_N, ‖J_N⁺‖₁ ≤ 3C(N) and ‖Z_N⁺‖₁ = 99N/4 − D(N) − 3C(N); the removed positive mass is
  73N/48 + O(1) out of 99N/4. Z_N is not nonpositive: this is a partial constructor, and the remaining
  positive mass is not handled.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [disjoint-annular-recursion, affine-common-tail-tree-lifting, finite-current-certificate-identity]
certificates: [check_partial_current_recompute.py, check_legacy_replay.py]
evidence:
  - "check_arithmetic_reductions.py, arithmetic_audit.json: the legacy checker of the catalogue (66 cases: every multiple of 8 through 512, and 768, 1536), of the root-collapse norm of annular-root-collapse-contraction and of the outer profile of outer-profile-closure-obstruction (cutoffs 8, 24, 96, 128, depths 0–4; c_80000). Fails at its new path: it loads experiments/current_construction/recursive/check_annular_recursion.py relative to the repository root (now ../disjoint-annular-recursion/check_annular_recursion.py, which itself no longer runs). Passed at be73a66 as experiments/annular_construction/arithmetic/check_arithmetic_reductions.py inside scripts/verify_all.py (archive/legacy-checker-run-be73a66.md: the gate ran these steps before stopping at residual_progress/history_frontier, and passed in full at 9dbc71a). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "combined_partial_current.py, combined_audit.json: the legacy reusable constructor build_combined_partial_current(N), returning the full current and residual, audited at N = 8, 72, 96, 160, 168, 384, 768, 6144. Fails at its new path: it loads check_arithmetic_reductions.py from its own folder (which fails as above) and ../components/affine_template_compiler.py (now ../affine-common-tail-tree-lifting/). Passed at be73a66 as experiments/annular_construction/arithmetic/combined_partial_current.py inside scripts/verify_all.py, as above. Later residual-progress scripts load it by its legacy path. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived Theorem (a) (valuations, residues, bands, disjointness, D(N), horizon inequality) and the five capacity bullets of Theorem (b) by hand; own annulus from Pi_(64N) - Pi_N, own catalogue and brute-force copy search check every statement for every 8 | N <= 1024 and N = 6144, 7200, 10008, 20000, the asymptotics over N <= 200000 and the horizons at N = 96; 3x+5, 3x+13 controls for the d = 1 arithmetic; both certificates passed; verdict HOLDS"
aliases: [R8]
tags: [convergence, packet-currents, annular, partial-current, constructive]
---

# Every annulus A_N has an explicit partial current that removes positive mass 73N/48 + O(1), leaving the rest unresolved

## Statement

All measures use the odd-only Syracuse map, absorption at 1, and the exact annulus `A_N = Π^R_(64N) − Π^R_N` of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md), with `8 | N` and `Q = 9N/4`. All inequalities below are strict. For each row of the table, take every integer `x` in the stated interval and residue classes, and put `x_1 = (3x+1)/2`, `x_2 = (9x+5)/4`. Each listed residue is 7 modulo 8, so both first valuations are exactly 1; the one-step row (E) uses only `x_1`.

| Family | Interval for x | x mod 72 | Actual coefficients at x, x_1, x_2 | Current coefficients at x, x_1 |
|---|---|---|---|---|
| E | 12N < x < 16N | 7 | (−3, 3), no x_2 term | (−3), no x_1 row |
| D | 16N < x < 18N | 23, 71 | (−1, 0, 1) | (−1, −1) |
| B | 24N < x < 32N | 7 | (−2, 1, 1) | (−2, −1) |
| C | 32N < x < 36N | 23 | (−3, 1, 2) | (−3, −2) |
| A | 48N < x < 64N | 7, 55 | (−1, −1, 2) | (−1, −2) |

**Theorem (a), the short-chain catalogue.** Let `μ_cat,N` be the sum of all listed signed chains and `J_cat,N` the sum of their current rows. Then

```
μ_cat,N = (I − P)J_cat,N,     J_cat,N ≤ 0,     A_N = (I − P)J_cat,N + Z_N,
```

where `Z_N` is exactly `A_N` with the chains' nonzero positions set to zero. With `C(a, b; r) = floor((bN − 1 − r)/72) − floor((aN − r)/72)` (the number of `aN < x < bN` with `x ≡ r mod 72`), the removed positive mass is

```
D(N) = 3C(12,16;7) + C(16,18;23) + C(16,18;71) + 2C(24,32;7) + 3C(32,36;23) + 2C(48,64;7) + 2C(48,64;55),
```

so `‖Z_N⁺‖₁ = 99N/4 − D(N)` and `‖Z_N‖₁ = 99N/2 − 2D(N)` exactly. For `72 | N`, `D(N) = 3N/2` and `‖Z_N⁺‖₁ = 93N/4`; in general `D(N) − 3N/2` is periodic under `N → N + 72` on multiples of 8. Since `J_cat,N ≤ 0`, `H_L(μ_cat,N) ≤ 0` and `H_L(A_N) ≤ H_L(Z_N)` for every horizon `L`, at zero positive cost.

**Theorem (b), the combined partial current.** Let `C(N)` be the number of admissible copies of the five-source family of [`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md), `M_N` their summed source measure and `K_N` their summed current. The supports of the catalogue chains and of all copies are pairwise disjoint, so with `J_N = J_cat,N + K_N` and `Z_N` equal to `A_N` with the union of both supports deleted,

```
A_N = (I − P)J_N + Z_N,     ‖J_N⁺‖₁ ≤ 3C(N),     ‖Z_N⁺‖₁ = 99N/4 − D(N) − 3C(N).
```

The removed positive mass `D(N) + 3C(N)` is `73N/48 + O(1)`. Remaining positive coefficients are returned, not discarded. The construction terminates for each `N` by bounded arithmetic loops, but it is a **partial** constructor.

## Proof

From §§1 and 5 of the legacy note `ARITHMETIC_RESULTS.md` and §4 of `AFFINE_COMPONENTS.md`, kept as written.

**Locations.** The coefficient table and the affine formulas put the chains in these places (state intervals in units of `N`, residues modulo 18):

| Family | x | x_1 | x_2 |
|---|---|---|---|
| E | (12,16), residue 7, band 2 | (18,24), residue 11, band 3 | not used |
| D | (16,18), residues 5 or 17, band 2 | (24,27), residue 17, band 3, coefficient 0 | (36,81/2), residue 17, band 4 |
| B | (24,32), residue 7, band 3 | (36,48), residue 11, band 4 | (54,72), residue 17, band 4 |
| C | (32,36), residue 5, band 3 | (48,54), residue 17, band 4 | (72,81), residue 17, band 5 |
| A | (48,64), residues 7 or 1, band 4 | (72,96), residue 11, band 5 | (108,144), residue 17, band 5 |

The half-step affine offsets cannot cross a displayed band boundary: the original interval endpoints are even integers and the permitted states are odd. In family D the upper endpoint `81N/2` is also even because `8 | N`. The residue restrictions similarly exclude the borderline cases. The nonzero columns are disjoint by interval or residue, and each affine map is injective; within family A the two input residues also have disjoint images. So no coefficient is spent twice. Zero intermediate points contribute no source measure.

**Currents.** For a chain with weights `(c_0, c_1, c_2)` summing to zero, the displayed current is `c_0·δ_x + (c_0 + c_1)·δ_(x_1)`, whose divergence is the chain. Every listed current coefficient is negative. This proves the identity and the sign claim using only the first two exact branches. The counts follow from the residue intervals. ∎ (a)

**Capacity against the five-source packing.** The five-source family has two parameter classes `t = 9s + r`, `r ∈ {0, 3}` ([`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md), §3). Its nonzero source supports are disjoint from the catalogue:

- The first five-source atom has band-4 residue 1 and is below `48N`; its distance below `48N` is at least 17, using the smallest admissible cutoff. It misses family A's input interval.
- The second has band-4 residue 1 or 7, but its residue modulo 72 is 1 or 25. The only catalogue inputs of these band-4 modulo-18 types require residue 7 or 55 modulo 72.
- The third has band-4 residue 11 and lies above `48N`. Family B's band-4 residue-11 images lie strictly between `36N` and `48N`.
- The fourth has band-5 residue 17 and lies in `81N < x < 108N`. At the largest admissible cutoff it exceeds `81N` by at least 611, and at the smallest it is below `108N` by at least 37. This separates it from family C's images in `(72N, 81N)` and A's images in `(108N, 144N)`.
- The fifth has band-5 residue 5, which is unused by the catalogue.

Each statement follows from the exact admissibility intervals, for both residue classes. Thus the combined removed positive mass is exactly `D(N) + 3C(N)`. The summed current has positive cost at most `3C(N)`, since the catalogue current is nonpositive and each five-source copy has positive cost 3. The remaining positive mass is exactly `99N/4 − D(N) − 3C(N)`. Finally `D(N) = 3N/2 + O(1)` and `C(N) = N/144 + O(1)` give `73N/48 + O(1)`. ∎ (b)

## Certificates

[`check_partial_current_recompute.py`](check_partial_current_recompute.py) (written at the migration, about 1 s, standard library, self-contained). For every multiple of 8 from 8 to 1024 and for `N = 6144` it rebuilds `A_N` from the six-band table and checks: every chain step is an actual Syracuse step with the stated annular coefficients; chains are disjoint; current rows are negative; the removed positive mass equals the floor formula `D(N)` (and `3N/2` when `72 | N`); every admissible five-source copy carries the stated coefficients and is disjoint from everything else; `C(160) = 0`; and `A_N = (I − P)J_N + Z_N` exactly, with `‖Z_N⁺‖₁ = 99N/4 − D(N) − 3C(N)` and `‖J_N⁺‖₁ ≤ 3C(N)`. Its values of `C(N)` at 96, 160, 168, 384, 768, 6144 agree with the legacy receipt `combined_audit.json`.

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B18-replay-revival migration; standard library) replays the unmodified legacy checks `check_arithmetic_reductions.py`, `combined_partial_current.py` in a temporary copy of the legacy layout built by `tools/legacy_replay.py`, requiring exit 0 and every file unchanged (about 22 s). It checks finite steps only; the status is unchanged.

## Remarks

- **The remaining obligation.** The residual's positive mass, about `93N/4`, is not handled. A complete current with everywhere nonpositive current coefficients is impossible: `H_53(A_96) = 699` and `H_9(A_384) = 42` ([`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md)), so positive cost must be allowed. The open targets are [`five-ray-annular-current-supply`](../../questions/five-ray-annular-current-supply.md) and the progress lemma [`annular-component-progress-lemma`](../../questions/annular-component-progress-lemma.md). The legacy line later extended this packing ([`release-source-packing`](../release-source-packing/README.md), legacy R16) to a removed mass of `1073N/432 + O(1)`.
- **Reusable entry point.** `build_combined_partial_current(N)` in `combined_partial_current.py` returns the full integer dictionaries of current and residual for every positive `N` divisible by 8; the finite template is read from its stored receipt in [`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md) and checked directly. No trajectory search is used. It needs its legacy layout to run.
- **The same note** also proved the one-pass compression [`annular-root-collapse-contraction`](../annular-root-collapse-contraction.md) (legacy §2) and the forward-transport obstruction [`outer-profile-closure-obstruction`](../outer-profile-closure-obstruction/README.md) (legacy §3); the legacy checker of this folder covers both.
- The A-family residue 7 rule was found independently in the component investigation of [`affine-common-tail-tree-lifting`](../affine-common-tail-tree-lifting/README.md); the catalogue adds its residue 55 counterpart and the other four families.
- Novelty undetermined.

## History

- Migrated from `experiments/annular_construction/arithmetic/ARITHMETIC_RESULTS.md` §§1, 4 (remaining-obligation paragraph) and 5, together with the cross-family capacity proof of `experiments/annular_construction/components/AFFINE_COMPONENTS.md` §4 (legacy ID R8), at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). The note's §2 became [`annular-root-collapse-contraction`](../annular-root-collapse-contraction.md) and §3 [`outer-profile-closure-obstruction`](../outer-profile-closure-obstruction/README.md). Scripts and receipts moved byte-identical; `check_partial_current_recompute.py` was added at the migration because the legacy scripts no longer run at their new paths. Legacy status: "written constructive proofs; exact capacity and divergence checks. Complete residual construction remains open".
- Main lane (ChatGPT, Codex), 2026-10-17, commit `ce56699`. The round report says "independent model reviews checked both capacity arguments"; those reviews were run by the main lane's own agents and are not counted as independent. No review from another lane is on record.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No corrections. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
