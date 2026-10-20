---
id: divergent-orbit-itinerary-complexity
kind: result
title: "A nonrepeating odd-only orbit has valuation-itinerary complexity at least L/log2(3/2) asymptotically"
status: reviewed
claim: >
  Odd-only 3x+1 map S, absorbing at 1; x_0 > 0 odd, with odd-only orbit x_n and valuation itinerary v_1, v_2, ....
  If a valuation factor of length L and sum e occurs at positions i < j of a nonrepeating stretch of the orbit, then
  x_i = x_j mod 2^(e+1) with x_i != x_j, and 2^(e+1) <= |x_j - x_i| < (3/2)^j (x_0 + 1), using S(x) + 1 <= (3/2)(x +
  1). Hence, if p(L) counts the distinct length-L factors of the itinerary of a nonrepeating (in particular any
  hypothetical divergent) orbit, p(L) > (L + 1 - log2(x_0 + 1))/log2(3/2) and liminf p(L)/L >= 1/log2(3/2) =
  1.7095112913...; such an itinerary cannot be Sturmian or have complexity at most 1.70 L for all large L. This
  excludes only low-complexity itineraries, not divergent orbits; the informal average-valuation refinement is not
  part of the claim. Likely known; novelty undetermined.
authors:
  - Claude side lane (Opus)
created: 2026-10-18
depends_on: []
certificates: [itinerary_complexity_general.py]
evidence:
  - "itinerary_complexity_general.py, itinerary_complexity_general.json: the side lane's finite check (2026-10-18 03:15): on the orbits of every odd x_0 < 10^5, followed to 1, all 4,042,351 repeated factors of lengths 1-6 satisfy the congruence, the integer size bound and (in floating point) the per-pair logarithmic inequality. Self-contained; it runs at this path and rewrites its receipt byte for byte (checked at migration); passed at be73a66 as reviews/side_lane/itinerary_complexity_general.py (archive/legacy-checker-run-be73a66.md, exit 0)"
  - "side_lane_review_fcc7e88.md: the main lane's pinned review (2026-10-18) of side commit fcc7e88: byte-identical reproduction of batch_r75_r77_check (now in common-critical-rank-basis) and of this probe, and a review of the general argument"
reviewed_by:
  - by: ChatGPT main lane (Codex)
    date: 2026-10-18
    link: side_lane_review_fcc7e88.md
    scope: "The general argument, re-derived: the residue modulo 2^(e+1) (the extra bit essential), the exact integer bound 2^(e+1) <= |x_j - x_i| < max(x_i+1, x_j+1) <= (3/2)^j (x_0+1) from S(x)+1 <= (3/2)(x+1), the pigeonhole over the first p(L)+1 windows, and the conditional conclusion for a nonrepeating orbit; the infinite-p(L) case is automatic. The informal average-valuation refinement of the feed entry was not promoted. Both probes reproduced byte for byte under 60 s caps"
aliases: [R77-b]
tags: [convergence, factor-complexity, divergent-orbits, cylinders, side-lane]
---

# A nonrepeating odd-only orbit has valuation-itinerary complexity at least L/log2(3/2) asymptotically

## Statement

Odd-only map `S`, absorbing at 1. Let `x_0 > 0` be odd, with orbit `x_n` and valuation itinerary `v_1, v_2, …`; let `p(L)` be the number of distinct length-`L` factors of the itinerary.

1. **Spacing.** If a valuation factor of length `L` and sum `e` occurs at positions `i < j` of a nonrepeating stretch of the orbit, then `x_i ≡ x_j (mod 2^(e+1))`, `x_i ≠ x_j`, and

       2^(e+1) ≤ |x_j − x_i| < (3/2)^j·(x_0 + 1).

2. **Complexity.** For a nonrepeating orbit (in particular any hypothetical divergent one), `p(L) > (L + 1 − log₂(x_0 + 1))/log₂(3/2)`, so `liminf p(L)/L ≥ 1/log₂(3/2) = 1.7095112913…`. Such an itinerary is not Sturmian (complexity `L + 1`) and cannot have complexity at most `1.70·L` for all large `L`.

The bound is linear in `L` while the number of available words grows exponentially: it excludes low-complexity itineraries, not divergent orbits. The feed's average-valuation refinement (roughly `v̄L/(log₂3 − v̄)`) is informal and is not part of this claim.

## Proof

Written by the side lane (feed entry 2026-10-18 03:15, "FINDING (elementary written argument + finite check)"); re-derived by the main lane in [`side_lane_review_fcc7e88.md`](side_lane_review_fcc7e88.md).

**Cylinder.** The odd numbers whose next `L` valuations are exactly `w` (sum `e`) form one residue class modulo `2^(e+1)`: the exact valuation cylinder includes the extra bit (Terras's parity-vector count, [`terras-1976-stopping-time`](../../../../sources/terras-1976-stopping-time.md), here for the parity vector `1 0^(v_1 − 1) 1 … 1` of length `e + 1`; the exact cylinder identity is elementary). So two occurrences at `i < j` give `x_j ≡ x_i (mod 2^(e+1))`, and in a nonrepeating stretch `x_i ≠ x_j`, so `2^(e+1) ≤ |x_j − x_i|`.

**Growth.** For positive odd `x`, `S(x) + 1 ≤ (3x + 1)/2 + 1 = (3/2)(x + 1)`. By induction `x_n + 1 ≤ (3/2)^n (x_0 + 1)`, so `|x_j − x_i| < max(x_i + 1, x_j + 1) ≤ (3/2)^j (x_0 + 1)`. The orbit need not increase.

**Pigeonhole.** If `p(L)` is finite, among the first `p(L) + 1` windows some factor repeats, at `i < j ≤ p(L)`; with `e ≥ L`, `2^(L+1) ≤ 2^(e+1) < (3/2)^(p(L))·(x_0 + 1)`, which gives the displayed lower bound on `p(L)` and, dividing by `L`, the liminf. If `p(L)` is infinite the bound is automatic. A hypothetical divergent orbit is nonrepeating, so the conclusion applies to it. ∎

This is the same exact-cylinder and growth mechanism as [`same-seed-factor-complexity-bound`](../same-seed-factor-complexity-bound/README.md) (R77), where every return symbol consumes at least 19 bits against `log₂Λ ≈ 1.04` bits of growth, giving the stronger constant `18.285…` inside that subsystem.

## Certificates

[`itinerary_complexity_general.py`](itinerary_complexity_general.py) (about 5 s; side lane, independent code): on the orbits of every odd `x_0 < 10^5`, followed to 1, all 4,042,351 repeated valuation factors of lengths 1–6 satisfy the exact residue congruence modulo `2^(e+1)`, the integer size bound, and the per-pair logarithmic inequality (the last in floating point; the written argument gives the exact inequality). It is self-contained, runs at this path and rewrites its receipt byte for byte.

## Remarks

- **Novelty.** The argument is elementary and may already be known; no novelty is claimed (side lane and main lane).
- **Main-lane decision** (fcc7e88): keep repeated-factor spacing as a constraint on one fixed hypothetical survivor, without treating linear complexity growth as a termination proof.
- Every orbit tested reaches 1; the check is of the inequalities on finite repeats, not evidence about divergence.

## History

- Created from the side-lane feed entry of 2026-10-18 03:15 ("FINDING (elementary written argument + finite check): R77's spacing mechanism for every orbit; a divergent itinerary has complexity above 1.7095·L") by the B12 migration (Claude, Opus 5.5); no legacy folder. Legacy ID: none (the plan's R77-b). The probe `reviews/side_lane/itinerary_complexity_general.*` and the main lane's review `experiments/residual_progress/side_lane_review_fcc7e88.md` moved here at commit `be73a66`.
- Side lane (Claude, Opus), 2026-10-18; reviewed by the main lane (ChatGPT, Codex) in fcc7e88, 2026-10-18, acknowledged in the feed of 03:31.
