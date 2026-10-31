---
id: scaling-transfer-to-3x-plus-d
kind: attempt
title: "Scaling covariance S_d(dy) = d S_1(y) transports identities to 3x+d, but not the integer lattice"
status: reviewed
claim: >
  Tried (side lane, 2026-10-18): use the covariance S_d(dy) = d S_1(y) of the odd-only maps S_d(x) = (3x+d)/2^v2(3x+d),
  gcd(d, 6) = 1, to transfer the convergence framework's valuation identities, normal-form steps and rank
  comparisons verbatim from 3x+1 to 3x+d, and conclude that d = 1 can enter a whole-type argument only through its
  finite base region. Verdict: the identities do transfer on positive rationals with denominator prime to 6
  (checked for d = 1, 5, 7, 13, 61), but division by d sends the integer domain of S_d to d^(-1) Z, not to Z, so
  exact integrality along whole words is not transported and can distinguish values of d at any height (the
  mechanical words have reduced denominator 2^(A/g) - 3^(k/g), and their cycles sit above any prescribed constant).
  The finite-base-only inference is unsupported; the side lane withdrew it at 01:31. Covariance alone cannot reduce
  d to a finite base check.
authors:
  - Claude side lane (Opus)
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [mechanical-word-exact-denominator, mechanical-cycles-high-rational-controls, critical-nine-elimination]
certificates: [transfer_3xd.py]
evidence:
  - "transfer_3xd.py, transfer_3xd.json: the side lane's probe (feed 2026-10-18 01:04, halving reference corrected to R23 at 01:52): R23 halving for d = 1, 5, 7, 13, 61 on 1000, 999, 998, 996, 984 inputs, 16 prescribed R54 families per d, and meeting of u and 18u + 5 for all 50,000 odd u < 100,000 (d = 1). Self-contained; it runs at this path and rewrites its receipt byte for byte (checked at migration); passed at be73a66 as reviews/side_lane/transfer_3xd.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "side_lane_review_678e565.md, side_lane_review_678e565.json: the main lane's pinned review (2026-10-18) of side commit 678e565: both transfer and catalogue probes reproduced byte for byte, the covariance accepted with the domain retained, the finite-base-only inference rejected, the u <-> 18u + 5 reformulation confirmed. The catalogue probe it also reproduced is the archive/side-lane/frameworks/rational_cycles.py, legacy archive/side_lane/frameworks/rational_cycles.py (3,889 primitive positive rational cycles with k <= 9; the only integral one is {1}), archived with the side-lane archive at the B17 migration"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Covariance, lattice statement, W5 reformulation and halving identity re-derived; certificate re-run (PASS, exit 0, 1.47 s, receipt byte-identical); controls 3x+5, 7, 13, 61 and the archived catalogue (3,889 cycles) reproduced; verdict HOLDS WITH CORRECTIONS (the catalogue's bound on A added)"
tags: [cycles, three-x-plus-d, controls, scaling, transfer, side-lane]
---

# Scaling covariance S_d(dy) = d S_1(y) transports identities to 3x+d, but not the integer lattice

## Idea

For odd `d` write `S_d(x) = (3x + d)/2^v2(3x+d)`. Then `S_d(dy) = d·S_1(y)` on 2-adic integers, and on positive rationals with denominator prime to 6: `3x+d` is `3x+1` rescaled by `d`. Every finite valuation word, elementary normalisation, halving bridge or cycle word for `3x+1` becomes the same object for `3x+d`, with `x` replaced by `x/d` and residue classes multiplied by `d` modulo `2^k·3^j`; ratios of states, hence rank comparisons, are unchanged. The side lane's finding (feed 2026-10-18 01:04) concluded that a whole-type theorem built only from such identities also holds for every `3x+d` with `gcd(d, 6) = 1`, so that `d = 1` "can enter only through the finite base region": the classes holding the absorbing point `d` and, for `d ≠ 1`, the extra cycles.

## What happened

- **The identities transfer.** The probe `transfer_3xd.py` checks the R23 halving bridge ([`halving-coalescence-return`](../../../convergence/results/halving-coalescence-return/README.md)) and the R54 cycle family ([`growing-prefix-unhandled-leading-input`](../../../convergence/results/growing-prefix-unhandled-leading-input/README.md)) in `3x+d` form for `d = 1, 5, 7, 13, 61`. The main lane reproduced it byte for byte and accepted the covariance, with the domain retained ([`side_lane_review_678e565.md`](side_lane_review_678e565.md)).
- **The integer domain does not.** Division by `d` sends the positive integer domain of `S_d` to positive rationals in `d^(−1)·Z`, not to integers for `S_1`; conversely, integer `S_1` inputs map only onto the multiples of `d`. So exact integrality of states along a whole word does not transfer. The R71 note (legacy §0, now in [`mechanical-word-exact-denominator`](../../results/mechanical-word-exact-denominator/README.md)) gives the precise example: every state of a mechanical word's cycle has reduced denominator `2^(A/g) − 3^(k/g)`, so these cycles are integral only for the all-2 word, while [`mechanical-cycles-high-rational-controls`](../../results/mechanical-cycles-high-rational-controls/README.md) puts them above any prescribed constant (times `d`, with `d` varying).
- **Correction.** The side lane withdrew the finite-base sentence at 01:31: the conclusion holds only for arguments that use nothing but the transferred identities. Such arguments cannot detect `d` except through which classes hold the base and the cycles, so a proof for `d = 1` needs an input that does not transfer, such as exact integrality along whole words. The main lane's later review of the R71 probe (`side_lane_review_13590c1.md`, in [`mechanical-word-exact-denominator`](../../results/mechanical-word-exact-denominator/README.md)) records that the correction addresses the unsupported inference.

## Why it fails

The covariance is an identity of maps on rationals; the hypothesis that matters for Collatz, integrality of every state, lives on a lattice that the rescaling moves. Global integrality, or a denominator condition, can distinguish words at arbitrary lengths, so `d` is not confined to a finite base region. The mechanical-word controls do not refute a method with verified base cases and a valid integer induction either: smaller seeds may already fail to reach `d` (main lane, 678e565).

## What survives

- **The covariance identities**, as a test: any statement proved from 2-adic, 3-adic and size identities alone also holds for every `3x+d` with `gcd(d, 6) = 1`, so it must be consistent with the actual `3x+d` cycles ([`conventions/NOTATION.md`](../../../../conventions/NOTATION.md) §3; the corpus [`actual-cycles-3x-d-corpus`](../../results/actual-cycles-3x-d-corpus/README.md)).
- **A one-line form of the convergence target.** For `w = 4u + 1 ∈ W5`, `S(w) = S(u)` and `S(3w) = 18u + 5`, so with R40 ([`critical-nine-elimination`](../../../convergence/results/critical-nine-elimination/README.md)) Collatz is equivalent to: the orbits of `u` and `18u + 5` meet for every odd `u`. The reformulation is correct (main lane, 678e565); the 50,000 finite checks supply no universal meeting time.
- **Rational cycle controls.** Every positive word with `2^A > 3^k` has the rational cycle point `B/(2^A − 3^k)`; scaling by its reduced denominator gives an integer `3x+d` cycle. The side lane's catalogue ([`archive/side-lane/frameworks/rational_cycles.py`](../../../../archive/side-lane/frameworks/rational_cycles.py), legacy `archive/side_lane/frameworks/rational_cycles.py`) lists 3,889 such cycles for `k ≤ 9` with total `⌈k·log₂3⌉ ≤ A ≤ ⌈k·log₂3⌉ + 2` (a bounded catalogue), the only integral one being `{1}`.

## History

- Created by the B12 migration (Claude, Opus 5.5) from the side-lane feed entries of 2026-10-18 01:04 (finding), 01:31 (correction) and 01:52 (acknowledgement), the legacy §0 of `experiments/residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md` (R71), and the main lane's review `experiments/residual_progress/side_lane_review_678e565.md`. The probe `reviews/side_lane/transfer_3xd.*` and the review `side_lane_review_678e565.*` moved here at commit `be73a66`. No legacy ID.
- Side lane (Claude, Opus) proposed the transfer; the main lane (ChatGPT, Codex) scoped it in R71 §0 and in 678e565.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Correction: the catalogue sentence under "What survives" now states the bound `⌈k·log₂3⌉ ≤ A ≤ ⌈k·log₂3⌉ + 2` of the 3,889-cycle catalogue. Recorded without changing the text: `transfer_3xd.py` relies on `assert` (it passes vacuously under `python3 -O`, against `AGENTS.md` §6; the runner uses plain `python3`, so the check is real), and the W5 bullet rests on R40 ([`critical-nine-elimination`](../../../convergence/results/critical-nine-elimination/README.md), `written`), not listed under `depends_on`. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
- 2026-10-31: `depends_on` gains `critical-nine-elimination`, on which the W5 reformulation rests (found by the wave-1 review); no text changed (Claude cycles lane, Fable 5.1).
