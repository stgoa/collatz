---
id: small-band-height-residue-matching
kind: result
title: Height-residue matching holds for ordered cycles with q > 1 in at most three (normalised) or two (raw) height bands
status: reviewed
claim: >
  Raw odd-only clock, no absorption. Let a primitive positive ordered cycle (q ≤ L, m > 1, circular
  normalised successor order) have reduced odd denominator q > 1 coprime to 6 and maximum dyadic
  height B. For each height h let R_h = {n_i mod q : h_i = h} (raw residues) and
  Z_h = {2^(−h)·n_i mod q : h_i = h} (normalised residues). If B ≤ 2, the family (Z_0, …, Z_B) has a
  system of distinct representatives; if B ≤ 1, so does (R_0, …, R_B). The same holds modulo every
  divisor Q > 1 of q. Moreover, in either graph an inclusion-minimal Hall-deficient set I of levels
  has neighbourhood of size exactly |I| − 1, each of whose residues occurs in at least two levels of
  I. Nothing is said at q = 1 or for B ≥ 3 (normalised) or B ≥ 2 (raw).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma, ordered-cycle-residue-law, ordered-cycle-sorted-rank-residues]
evidence:
  - "../ordered-cycle-sorted-rank-residues/MATCHING_ARITHMETIC.md, sections 1-2: the written proofs"
  - "../ordered-cycle-sorted-rank-residues/INDEPENDENT_MATCHING.md, section 2: an independent main-lane proof of the same corollary for every divisor Q > 1 of q, via the sorted-rank law and T ≥ 4"
  - "../ordered-cycle-sorted-rank-residues/height_matching_audit.json: both full-q matchings pass on all 1,185 stored normalised cycles (51 nonfixed ordered); historical receipt, its checker no longer runs at the new path"
reviewed_by:
  - by: Claude review lane (Fable 5.1; directed by Santiago Armstrong)
    date: 2026-10-31
    link: REVIEW-2026-10-31-claude-review-lane.md
    scope: "Re-derived the small-band theorem and the minimal-deficiency lemma modulo every divisor Q > 1 and tested them by brute-force Hall on all 50 ordered 3x+d control cycles (every divisor of q), on the boundary bands, and on the two period-17 counterexample cycles; HOLDS WITH CORRECTIONS: the q = 5 control of the Remarks identified by its minimum, links repaired after the move to a folder."
tags: [cycles, dyadic-order, residues, hall-matching]
---

# Height-residue matching holds for ordered cycles with q > 1 in at most three (normalised) or two (raw) height bands

## Statement

Notation as in [`ordered-cycle-sorted-rank-residues`](../ordered-cycle-sorted-rank-residues/README.md): a primitive positive ordered cycle `3n_i + q = 2^(a_i)·n_(i+1)` with `q ≤ L`, `m > 1`, reduced `q` coprime to 6, heights `h_i`, `B = max h_i`, normalised word `c_i = a_i + h_(i+1) − h_i ∈ {1, 2}` (the lower mechanical word, `gcd(A, m) = 1`). For each height `h`,

```
R_h = {n_i mod q : h_i = h},
Z_h = {2^(−h)·n_i mod q : h_i = h}.                 (1)
```

**Small-band theorem.** If `q > 1`, the normalised family `(Z_h)` has a full matching (distinct representatives) when `B ≤ 2`, and the raw family `(R_h)` has one when `B ≤ 1`. The same holds modulo every divisor `Q > 1` of `q`.

**Minimal-deficiency lemma.** In either residue graph, if a nonempty set `I` of height labels is inclusion-minimal with `|N(I)| < |I|`, then `|N(I)| = |I| − 1` and every residue in `N(I)` occurs in at least two levels of `I`.

## Proof

[`MATCHING_ARITHMETIC.md`](../ordered-cycle-sorted-rank-residues/MATCHING_ARITHMETIC.md) §§1–2 (legacy text, lightly edited); an independent version for every divisor `Q > 1` is [`INDEPENDENT_MATCHING.md`](../ordered-cycle-sorted-rank-residues/INDEPENDENT_MATCHING.md) §2.

Every numerator is a unit modulo `q` ([`ordered-cycle-residue-law`](../ordered-cycle-residue-law.md)). The normalised arrow gives `2^(c_i)·Z_(i+1) ≡ 3Z_i (mod q)` with `c_i ∈ {1, 2}`; equal residues at the ends of an arrow would force `q | 2^(c_i) − 3 = ±1`, impossible for `q > 1`, and the two possible successors `3·2^(−1)r`, `3·2^(−2)r` of one unit `r` differ. The chronological normalised residue orbit has at least **three** values: with exactly two, residues would alternate, `m` would be even, `c` would be constant on each parity class, so the normalised word would have period at most two; `gcd(A, m) = 1` then forces `m = 2`, and the only mixed two-letter word has `A = 3`, `2^A − 3^m = −1 < 0`; constant words contradict `gcd(A, m) = 1` for `m > 1`.

The minimum lies at sorted rank 0 with `c_0 = 1`; since `h_0 = 0` and `a_0 ≥ 1`, its successor also has height 0, and their residues differ, so `|Z_0| ≥ 2`. An arrow rising from height `h` to `h + 1` has `a_i = c_i − 1 ≥ 1`, so `c_i = 2`, and its endpoint residues differ; every adjacent pair of observed levels has such a rising arrow (the cycle starts at height 0 and rises by at most one per arrow). So `Z_h` and `Z_(h+1)` are not the same singleton. For `B = 2`, a deficient pair must have a one-element union: `{0,1}` and `{1,2}` are ruled out by the rising arrows, `{0,2}` by `|Z_0| ≥ 2`; a deficient triple would have a union of at most two residues, ruled out by the three-value result. For raw residues with `B = 1`, the minimum and its successor are both at height 0 with exact valuation `a_0 = 1`, so equal residues would force `q | 2 − 3`; a deficient pair would need all raw numerators in both bands to share one residue. QED.

The lemma: removing any one level of `I` leaves a Hall-satisfying proper subset, whose neighbourhood has at least `|I| − 1` elements and lies in `N(I)`; a residue in only one level would drop the neighbourhood to at most `|I| − 2` when that level is removed. QED.

## Remarks

- **Scope.** Every step needs `q > 1`; modulo 1 all residues coincide and the `±1` argument is vacuous, so nothing transfers to `q = 1`. The theorem does not establish the all-height proposal even for `q > 1` ([`height-residue-hall-matching`](../../questions/height-residue-hall-matching.md)).
- **The lemma does not propagate.** Minimal Hall failures can involve two nonadjacent bands when `B ≥ 3`. The ordered `q = 5`, period-17 control (minimum 187) has repeated raw residue 2 across heights 0–3 and identical raw residue 3 on all its band maxima, yet full raw and normalised matchings; so one canonical extremal state per band cannot prove the proposal.
- **Review status.** `written`: the proof was checked by main-lane review agents (`ARITHMETIC_REVIEW.md`: "PASS for the stated partial theorems"). The Lean lane's hand re-derivation of C008 (feed 03:01) lists the sorted-rank law and cyclicity, not this theorem, and the side-lane referee did not test it, so no independent review of this part is on record.
- **Novelty.** No novelty claimed in the legacy record; undetermined.

## History

- Split from `experiments/cycle_spectrum/C008/` (legacy ID `C008`; `REPORT.md`, `MATCHING_ARITHMETIC.md` §§1–2, `INDEPENDENT_MATCHING.md` §2) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. During the batch an initially considered raw `B = 2` extension to general divisors was retracted by the second counterexample of [`primewise-height-residue-matching`](../../attempts/primewise-height-residue-matching.md).
- 2026-10-31: reviewed by the Claude review lane (Fable 5.1; directed by Santiago Armstrong); status raised to reviewed. Corrections: the `q = 5` period-17 control of the Remarks identified by its minimum 187 (the other ordered `q = 5` period-17 cycle, minimum 347, does not have raw residue 3 on all band maxima); the node moved from `small-band-height-residue-matching.md` to this folder and its relative links and evidence paths repaired. Review: [`REVIEW-2026-10-31-claude-review-lane.md`](REVIEW-2026-10-31-claude-review-lane.md).
