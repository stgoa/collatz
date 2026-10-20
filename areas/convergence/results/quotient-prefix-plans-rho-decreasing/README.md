---
id: quotient-prefix-plans-rho-decreasing
kind: result
title: "Quotient-orbit prefixes stopped below (8 rho(w) - 5)/9 are strict-rho plans for every W5 input"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; nu, T = nu S, P(w) = [3w] - [w], rho(w) = nu(3w), W5 = {w = 5 mod 8}; H_s
  the formal absorption plan with current J_s and signed requests A_s. For w in W5 put q = rho(w), z = nu(w), and
  suppose an actual finite quotient prefix reaches x = T^k(q) with 9x + 5 < 8q. Then J = N_(3w) + sum_(i<k) B_i +
  H_x - N_w - H_z (B_i the exact quotient bridges) has div J = P(w) - sum_u (A_x(u) - A_z(u)) P(u), and every
  nonzero signed request has rho(u) < rho(w), after cancellation; the first hitting time is optional. Consequently
  universal finite hitting of 9x + 5 < 8 rho(w) by the quotient orbit of rho(w), for every w in W5, would supply all
  W5 tripling currents by strong induction on rho, and with R40 imply Collatz; conversely Collatz implies it. This
  is an equivalent stopping-time formulation only: universal hitting is not proved, and the equivalence does not
  force every useful current construction to follow this prefix.
authors:
  - Claude side lane (Opus)
created: 2026-10-18
depends_on: [critical-image-rank-composition, sigma-rank-removes-absorption-overhead, absorption-defect-original-rank-resolution, elementary-bridge-quotient-normal-form, critical-nine-elimination]
certificates: [check_legacy_replay.py]
evidence:
  - "rho_prefix_plans.py, rho_prefix_plans.json: side-lane validation (2026-10-18 00:53): 3,600 complete stopping-prefix plans, 1,200 each at 24, 40 and 64 bits, all accepted by main's rho validator at 793e835; share needing at most 2, 4, 8, 16, 32 quotient steps 13.0%, 49.1%, 76.1%, 92.4%, 98.7%; largest prefix 79 steps. Finite measurements, not a bound on other inputs. Fails at its new path: it imports backward_word_rule from its own folder (now ../negative-cycle-backward-word/), which loads main's B11 modules (critical_rank/ and others) by their legacy paths. Passed at be73a66 as reviews/side_lane/rho_prefix_plans.py (archive/legacy-checker-run-be73a66.md, exit 0); its receipt is reproduced byte for byte by check_legacy_replay.py"
  - "side_lane_review_33c3829.md, side_lane_review_33c3829.json: the main lane's pinned review (2026-10-18) of side commit 33c3829: the written argument checked, and both probes (this one and r62_compatibility_check.py of absorption-defect-original-rank-resolution) reproduced unchanged in temporary storage with matching receipts"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-18
    link: side_lane_review_33c3829.md
    scope: "The whole written argument: exact boundary (2), the request bounds from R43 (equivalently R51 with R62) and from z < w/4, q > w, the optional first hitting time, and the equivalence with Collatz through R40 in both directions ('correct equivalent stopping-time formulation'); it does not establish universal finite hitting or that useful constructions must follow this prefix. Both probes reproduced unchanged under 90 s caps with matching receipts"
aliases: [R62-b]
tags: [convergence, outer-residual, tripling-pairs, critical-rank, stopping-time, side-lane]
---

# Quotient-orbit prefixes stopped below (8 rho(w) - 5)/9 are strict-rho plans for every W5 input

## Statement

Odd-only clock, 1 absorbing; `ν`, `T = νS`, `P(w) = [3w] − [w]`, `ρ(w) = ν(3w)`, `W5 = {w ≡ 5 mod 8}`; `H_s` the formal absorption plan, `div H_s = [s] − Σ A_s(u)P(u)`; `N_x` the elementary normaliser with `div N_x = [x] − [ν(x)]`; `B_i` the exact quotient bridge at `T^i(q)`.

For `w ∈ W5` put `q = ρ(w)`, `z = ν(w)`, and suppose an actual finite quotient prefix reaches `x = T^k(q)` with

    9x + 5 < 8q.                                                        (1)

Then

    J = N_(3w) + Σ_(i<k) B_i + H_x − N_w − H_z,
    div J = P(w) − Σ_u (A_x(u) − A_z(u)) P(u),                           (2)

and every nonzero signed request in (2) has `ρ(u) < ρ(w)`, including after equal terms cancel. The first hitting time is optional: any supplied prefix satisfying (1) works; its length and intermediate heights may be large.

**Consequence.** Universal finite hitting of (1) by the quotient orbit of `ρ(w)`, for every `w ∈ W5`, would supply all `W5` currents by strong induction on `ρ`, and with [`critical-nine-elimination`](../critical-nine-elimination/README.md) (R40) imply Collatz; conversely Collatz implies it, since every quotient orbit reaches 1 and `q ≥ 7`. This is an equivalent stopping-time formulation of the open target [`universal-w5-tripling-currents`](../../questions/universal-w5-tripling-currents.md), not a proof of it, and it does not show that every useful current construction must trace this prefix.

## Proof

Written by the side lane (feed entry 2026-10-18 00:53, "FINDING (written proof + validation)"), from the main lane's own theorems; checked by the main lane in [`side_lane_review_33c3829.md`](side_lane_review_33c3829.md).

**Requests of `H_x`.** [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) (R43) bounds every request of `H_x` by `(9x+5)/8`, which is `< q` by (1). Equivalently, [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md) (R51) gives `σ(u) ≤ ν(x) ≤ x`, and identity (1) of [`absorption-defect-original-rank-resolution`](../absorption-defect-original-rank-resolution/README.md) (R62) says `ρ(u) = (9σ(u)+5)/8` on `E` and `ρ(u) = σ(u)` off `E`; either way `ρ(u) ≤ (9x+5)/8 < ρ(w)`.

**Requests of `H_z`.** R43 gives `ρ(u) ≤ (9z+5)/8`. With `z < w/4` (since `w ≡ 5 mod 8`) and `q = ρ(w) > w`, this is below `q` for every `w ≥ 5`.

**Boundary.** The normalisers and quotient bridges telescope from `[3w]` through `[q] = [T^0(q)]` to `[x]`; adding `H_x − N_w − H_z` gives (2). For `w ∈ E` the target `(8ρ(w)−5)/9` equals `σ(w)`, so these are exactly the side lane's earlier `σ`-plans (feed 2026-10-17 23:43); for `w ∉ E` the threshold removes R62's window (2), the only place where `σ`-valid plans can fail the `ρ` test.

**Equivalence.** If (1) is hit for every `w ∈ W5`, strong induction on `ρ` supplies every `W5` tripling current, and R40 turns that into Collatz. Conversely, under Collatz every quotient orbit reaches 1, and `1` satisfies (1) because `q ≥ 7`. ∎

The finite validation (`rho_prefix_plans.py`) is evidence for the implementation only; the sampled prefix lengths do not bound other inputs.

## Certificates

[`check_legacy_replay.py`](check_legacy_replay.py) (written at the B12 migration; standard library). The legacy scripts of this folder load sibling modules by their pre-migration paths, so they no longer run here. This certificate calls `tools/legacy_replay.py`, which rebuilds the pre-migration layout in a temporary directory from `tools/legacy_paths.json`, runs the unmodified legacy scripts there without `-O` (as `scripts/verify_all.py` did at `be73a66`), and requires exit 0 and every copied file unchanged. It writes nothing in the repository. It replays: the side-lane probe `rho_prefix_plans.py` (about 30 s; 3,600 stopping-prefix plans built with the side lane's own step and accepted by main's `ρ` validator, receipt reproduced byte for byte). It imports `backward_word_rule.py`, now in [`negative-cycle-backward-word`](../negative-cycle-backward-word/README.md), and through it main's legacy modules. 

## Remarks

- **Main-lane decision** (33c3829): the sharper threshold is a useful correctness test for forward plans; its unproved hitting assertion is the central difficulty in another form. The same review reproduced the compatibility probe of R62.
- Related: the `σ`-plan precursor and the twelve-family measurements are in [`sigma-rank-removes-absorption-overhead`](../sigma-rank-removes-absorption-overhead/README.md) and [`twelve-family-rho-dispatcher`](../twelve-family-rho-dispatcher/README.md). The R40 equivalence is also the basis of the one-line target `u ↔ 18u + 5` in [`scaling-transfer-to-3x-plus-d`](../../../cycles/attempts/scaling-transfer-to-3x-plus-d/README.md).
- Novelty undetermined (none claimed).

## History

- Created from the side-lane feed entry of 2026-10-18 00:53 ("FINDING (written proof + validation): with target (8ρ(w) − 5)/9, plain quotient-orbit prefixes are strict-ρ plans for every W5 input") by the B12 migration (Claude, Opus 5.5); no legacy folder. Legacy ID: none (the plan's R62-b). The probe `reviews/side_lane/rho_prefix_plans.*` and the main lane's review `experiments/residual_progress/side_lane_review_33c3829.md` and `.json` moved here at commit `be73a66`; `check_legacy_replay.py` was added at the migration.
- Side lane (Claude, Opus), 2026-10-18; reviewed by the main lane (ChatGPT, Codex) in 33c3829, 2026-10-18, which also acknowledged it in the feed of 01:20.
