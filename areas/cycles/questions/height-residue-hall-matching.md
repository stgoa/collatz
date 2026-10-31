---
id: height-residue-hall-matching
kind: question
title: Do the height-band residue sets of every ordered cycle admit distinct representatives?
status: open
claim: >
  Prove or refute, for every primitive positive ordered cycle of the raw odd-only map (q ≤ L, m > 1,
  circular normalised successor order) with reduced odd denominator q coprime to 6: both the raw
  residue sets R_h = {n_i mod q : h_i = h} and the normalised sets Z_h = {2^(−h)·n_i mod q : h_i = h},
  h = 0, …, B, have systems of distinct representatives (q = 1 taking the sole residue 0). At q = 1
  this would force B = 0, so with the narrow-cycle classification it would exclude every nontrivial
  ordered integer 3x+1 cycle. Equivalent in strength at q = 1 to the ordered-cycle target; it is a
  sufficient mechanism, not a proved one.
created: 2026-10-19
tags: [cycles, dyadic-order, residues, hall-matching]
---

# Do the height-band residue sets of every ordered cycle admit distinct representatives?

## Question

In the notation of [`small-band-height-residue-matching`](../results/small-band-height-residue-matching/README.md), the **full Hall proposal** says that for every ordered primitive cycle both families `(R_h)` and `(Z_h)`, `h = 0, …, B`, admit distinct representatives modulo the reduced denominator `q`. For `q = 1`, take the sole residue class 0.

## Why it matters

At `q = 1` the proposal forces `B = 0`, i.e. `H < 2L`, and [`narrow-cycles-are-mechanical`](../results/narrow-cycles-are-mechanical/README.md) then excludes every nontrivial ordered integer cycle: a positive answer would settle [`ordered-cycle-denominator-one`](ordered-cycle-denominator-one.md). For the same reason the `q = 1` case is that target restated; residue information alone gives nothing there (all residues are 0). The side-lane referee of C008 (feed 2026-10-19 02:56) concluded that "no residue-matching argument can reach the denominator-one target", and the legacy report agrees that the modular equations alone are vacuous there. The main lane's C009 side review (`SIDE_REVIEW.md` in [`excursion-compression`](../attempts/excursion-compression/README.md)) calls the referee's sentence too broad if read as an impossibility theorem: a matching theorem proved with global information is not excluded. Either way, a proof would have to couple the matching with the weighted integer divisibility `D | C_h`.

## Known progress

- Small bands for `q > 1`: [`small-band-height-residue-matching`](../results/small-band-height-residue-matching/README.md) (normalised `B ≤ 2`, raw `B ≤ 1`, every divisor `Q > 1`), with the minimal-deficiency lemma.
- The sorted-rank law `z_[j] ≡ L·t^j (mod Q)` turns normalised matching into a matching of levels to rank classes modulo `T = ord_Q(t) ≥ 4` ([`ordered-cycle-sorted-rank-residues`](../results/ordered-cycle-sorted-rank-residues/README.md)); it does not remove the height shift from raw residues.
- Refuted reduction: [`primewise-height-residue-matching`](../attempts/primewise-height-residue-matching.md).
- Finite evidence: both full-`q` matchings pass on all 1,185 stored normalised cycles, including 51 nonfixed ordered cycles (receipt `height_matching_audit.json` in [`ordered-cycle-sorted-rank-residues`](../results/ordered-cycle-sorted-rank-residues/README.md)). Only 11 raw and 4 normalised ordered graphs have overlapping height sets; many passes follow from disjointness. A targeted screen of 946,001 profiles over 17 coprime totals through period 17 found only 13 with reduced `q ≤ 31`, all known: no new substantive evidence. The earlier matching receipt is in [`height-denominator-candidate`](height-denominator-candidate/README.md) (`RESIDUE_MATCHING.md`), where a universal matching theorem would imply `B + 1 ≤ φ(q)`.

## Suggested attacks

From the legacy C008 report:

- For an inclusion-minimal deficient set in a wider cycle, including a pair of nonadjacent bands, combine its repeated-residue requirement with the full rank-gap inequalities and the reduced-denominator equality `q = D/gcd(C_h, D)`; local propagation using only the modular arrow is insufficient.
- Proving further fixed-band `q > 1` cases is a diagnostic, not progress on the target. The legacy decision was to pivot to the full integer obstruction instead (this led to [`excursion-compression`](../attempts/excursion-compression/README.md)).
