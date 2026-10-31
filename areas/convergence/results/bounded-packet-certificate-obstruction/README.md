---
id: bounded-packet-certificate-obstruction
kind: result
title: Some actual right-aligned packet needs more than H current rows, for every H
status: reviewed
claim: >
  Odd-only 3x+1 map, absorbing at 1; right-aligned packets of right-aligned-fixed-core-remainder. For every
  integer H ≥ 0, with K = 2H + 7, y = 9·2^K − 1 and N = 4·2^K + 5, the measure μ_y = 2δ_y − δ_(y+6) − δ_(y+12) is
  the last valuation-1 triple in source component 1 at cutoff N, and every finite exact current for μ_y, and
  every finite current with everywhere nonpositive residual for it (auxiliary states allowed), has strictly
  more than H nonzero rows. So no finite catalogue of per-triple templates with a uniformly bounded number of
  rows certifies every actual packet. Cancellation across packets in the aggregated measure, recursive
  templates with unbounded expansion and unrestricted certificate size are not excluded.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-17
depends_on: [right-aligned-fixed-core-remainder, orbit-component-current-criterion]
evidence:
  - "../orbit-component-current-criterion/verify_obstructions.py (a certificate of that node): checks the delayed-separation formulas at H = 0, 1, 2, 4, 8, 16, 32, 64, 128, verifies packet membership arithmetically without materialising the cutoff, and checks the local coalescence identity for t = 0, …, 9999; legacy receipt audit.json there"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Full argument re-derived (packet membership from the R2 definitions and by independent materialisation of the whole right-aligned construction for H <= 3, delayed separation and the perturbation formula for H <= 80, the functional-graph path argument, the local identity for t < 20000); the evidence script re-run (exit 0); no certificates listed. Verdict HOLDS; two imprecisions and no correction to the claim; the node was converted from a single file to a folder for this review"
aliases: [R7-b]
tags: [convergence, packet-currents, right-aligned, obstruction, certificate-size]
---

# Some actual right-aligned packet needs more than H current rows, for every H

## Statement

Odd-only clock, absorbing at 1; packets as in [`right-aligned-fixed-core-remainder`](../right-aligned-fixed-core-remainder/README.md). The conclusion concerns **individual triples**, even though those triples occur in the actual right-aligned family. It does not exclude cancellations across different triples in the aggregated measure `Π^R_N`.

**Theorem 2.** For every integer `H ≥ 0`, let `K = 2H + 7`, `y = 9·2^K − 1` and `N = 4·2^K + 5`. The measure

```
μ_y = 2δ_y − δ_(y+6) − δ_(y+12)
```

is the last valuation-1 triple in source component 1 at cutoff `N`, under the right-aligned construction. Any finite exact current for `μ_y`, or any finite current with everywhere nonpositive residual for it, has strictly more than `H` nonzero rows.

## Proof

From §3 of the legacy note `functional_graph_currents.md`, kept as written.

**Packet membership.** For valuation `a = 1`, source and endpoint lifts are `x_t = 3 + 4t`, `y_t = 5 + 6t`, `t ≥ 0`. Put `t = 3·2^(K−1) − 1`, so `y_t = y` and `t ≡ 2 (mod 3)`. The component-1 cutoff is `n_1 = floor((3N+1)/2) = 6·2^K + 8`. Its final lift is `t + 2`, since its source is `6·2^K + 7`, while the next source exceeds `n_1`. There are `t + 3 = 3·2^(K−1) + 2` lifts. Right alignment therefore leaves the first two and groups the rest into triples beginning at indices `2 mod 3`. The three source residues modulo 3 are `2, 0, 1`, giving the coefficients `2, −1, −1` claimed.

**Delayed separation.** Consider the integer base orbits starting at `−1`, `5` and `11`. Their exact valuations and states are

```
−1 → −1 → −1 → …            valuations 1, 1, 1, …
 5 →  1 →  1 → …            valuations 4, 2, 2, …
11 → 17 → 13 → 5 → 1        valuations 1, 2, 3, 4, then 2, 2, …
```

The last display uses the ordinary formula at 1, which fixes 1; the actual positive perturbations below never equal 1 within the window. For each base orbit let `z_j` be its state and `A_j` its accumulated valuation. For `0 ≤ j ≤ H`, each `A_j ≤ 2H + 2`. Exact branch arithmetic therefore gives

```
S^j(z_0 + 9·2^K) = z_j + 9·3^j·2^(K − A_j).
```

This follows by induction: before each division the perturbation is divisible by at least one more power of 2 than the base numerator's exact valuation. The displayed bound leaves at least five bits at every state. All the first `H + 1` states of `y` are thus `≡ −1 ≡ 31 (mod 32)`. The states from `y + 6` and `y + 12` have residues in `{1, 5, 11, 13, 17}` modulo 32. There is no equality between these orbit segments, and the segment from `y` does not reach the absorber 1.

**Separation bounds certificate size.** Suppose `J` had at most `H` nonzero rows. Form the finite undirected graph of its nonzero arrows, including their endpoints and the absorber if reached. Let `D` be the component containing `y`. If `D` contains neither negative source nor the absorber, summing the identity over `D` gives `2 = Σ_D μ_y = Σ_D ζ ≤ 0` (with `ζ = 0` in the exact case), impossible. So `D` has an undirected path from `y` to a negative source or to the absorber, with at most `H` edges. In a deterministic graph, any undirected simple path has its arrows directed toward a single meeting vertex: two arrows pointing away from an interior vertex would violate outdegree at most one. Its two endpoints therefore meet under forward iteration with each arrival time at most `H`; when one endpoint is the absorber, the other reaches it within `H` steps. This contradicts the separation just established. ∎

## Remarks

- **Purpose and scope.** A finite catalogue of per-triple current templates whose expansions each have a uniformly bounded number of rows cannot certify every actual right packet. Recursive templates with unbounded expansion, templates using cancellations across packets, and constructions with unrestricted certificate size are not excluded. The logarithmic lower bound is small relative to the arbitrary per-cutoff cost permitted by [`qualitative-current-criterion`](../qualitative-current-criterion.md); its purpose is to rule out an overly narrow local search strategy. Aggregated packets are studied in [`whole-packet-historical-certificates`](../whole-packet-historical-certificates/README.md); whether a uniform aggregate exposure depth exists is [`uniform-aggregate-exposure-depth`](../../questions/uniform-aggregate-exposure-depth.md).
- **A useful local identity remains valid.** For every integer `t ≥ 0`, set `x = 69 + 256t`. Then `S^2(x) = 5 + 18t` and `S^2(x + 6) = 85 + 288t = 16·S^2(x) + 5`. Because `3(16u + 5) + 1 = 16(3u + 1)`, their odd parts agree, so `S^3(x) = S^3(x + 6)`. This yields an exact current for `δ_x − δ_(x+6)` with at most six rows. The valuation of the third step need not be bounded or fixed on the whole cylinder. This is compatible with Theorem 2: the single residue cylinder is useful, but a bounded-size per-packet catalogue cannot cover all packets.
- **Complement.** Every certificate dominates the forced current pointwise ([`exact-current-minimality`](../exact-current-minimality.md)), and Theorem 2 shows that forced current is itself large for individual packets (PR1 lane, NOTE §10 in [`locally-collatz-like-control-barrier`](../locally-collatz-like-control-barrier/README.md)).
- Novelty undetermined.

## History

- Migrated from `experiments/current_construction/obstructions/functional_graph_currents.md` §§3–4 (part of the legacy R7 round) at commit `be73a66`, by the B08 migration (Claude, Opus 5.5). Legacy status: "written graph theorem, complete semidecision algorithm, and finite checks"; the note says these arguments "have not been human-reviewed or formally verified".
- Main lane (ChatGPT, Codex), 2026-10-17. The round report records an "independent model review" of the arbitrary-auxiliary-state version by the main lane's own agents; no review from another lane is on record.
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. No correction to the claim or proof. The node was converted from the single file `bounded-packet-certificate-obstruction.md` to this folder (`README.md` plus the review), its six relative links gained one `../`, and the inbound links elsewhere were repointed; the `evidence` path `../orbit-component-current-criterion/verify_obstructions.py`, which did not resolve from the single file, now resolves. The review records one further imprecision (`A_j ≤ 2j + 2` is the bound the base orbits give; `A_j ≤ 2H + 2` is what the proof uses).
