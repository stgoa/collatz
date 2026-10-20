---
id: height-denominator-candidate
kind: question
title: "Height–denominator candidate: does every ordered cycle with q ≤ L have B ≤ q − 1?"
status: open
claim: >
  Prove or refute: every primitive positive rational cycle of the raw odd-only 3x+1 map (written as a
  reduced odd numerator cycle 3n_i + q = 2^(a_i)·n_(i+1), q odd and coprime to 6) with q ≤ L = min n_i
  and circularly ordered normalised successor has maximum dyadic height B = max floor(log₂(n_i/L))
  at most q − 1. At q = 1 this forces B = 0, so the narrow classification would leave only the fixed
  point 1: every ordered nontrivial integer 3x+1 cycle would be excluded (unordered cycles untouched).
created: 2026-10-19
aliases: [C007]
tags: [cycles, dyadic-order, height, conjecture]
---

# Height–denominator candidate: does every ordered cycle with q ≤ L have B ≤ q − 1?

## Question

For a primitive positive rational raw odd-only cycle, write its odd numerators and reduced common denominator as `3n_i + q = 2^(a_i)·n_(i+1)`, with exact `a_i ≥ 1`; there is no absorber. Let `L = min n_i`, assume `q ≤ L`, and set `h_i = floor(log₂(n_i/L))`, `B = max h_i`. As in [`dyadic-order-lemma`](../../results/dyadic-order-lemma.md), require that successors preserve circular order after dividing each state by its height power of two. The candidate is

> Every such cycle satisfies `B ≤ q − 1`.     (H)

At `q = 1` this would force `B = 0`, i.e. `H < 2L`; the narrow classification and mechanical denominator theorem ([`narrow-cycles-are-mechanical`](../../results/narrow-cycles-are-mechanical/README.md)) would then leave only the trivial fixed point. No proof puts every possible integer cycle in the ordered class.

The exact missing step: with the weighted intercept `C_h = Σ_j 3^(m−1−j)·2^(P_j − h_j)`, `D·L = q·C_h` and `q = D/gcd(C_h, D)` for the reduced numerator realisation. A proof must control this full height-dependent congruence. Rewriting (H) as `gcd(C_h, D) ≤ D/(B+1)` is equivalent to the candidate, not progress on it.

## Why it matters

(H) is a statement for every denominator whose `q = 1` case is exactly the ordered-cycle target [`ordered-cycle-denominator-one`](../ordered-cycle-denominator-one.md); it is the kind of spectrum law across `3x+d` that the cycle programme asked for. It is one possible mechanism, not a required theorem or evidence that the route will succeed.

## Known progress

- **Exact arithmetic** ([`ordered-cycle-residue-law`](../../results/ordered-cycle-residue-law.md), formal): every numerator is a unit modulo `6q`; for fixed normalised word `c` and initial residue the modular dynamics `z_i ≡ L·3^i·2^(−P_i) (mod q)` loses the height profile entirely; and the min–top inequality `3(n_i − 2^B·L) > q(2^B − 1)` holds.
- **Two exact obstructions to shortcuts** ([`height-bound-via-residues-or-relaxation`](../../attempts/height-bound-via-residues-or-relaxation.md)): height levels need not occupy disjoint residue classes (the ordered `q = 5` cycle from 187 has raw residue 2 at all four heights 0–3); real order inequalities alone cannot force the integer conclusion (the ordered `q = 5` cycle from 347, divided by 5, satisfies all of them with additive term 1 and `B = 3`); and the pairwise min–top relaxation permits arbitrarily large `B`. Neither is a counterexample to (H).
- **Finite evidence** ([`ordered-cycle-height-census`](../../results/ordered-cycle-height-census.md)): (H) holds on every stored normalised cycle with `q ≤ L` in the combined C001/C007 set of 1,185 normalised cycles, including the 51 ordered ones and the unordered ones; the nearest ordered examples are the `q = 5` period-17 cycles with `B/(q − 1) = 3/4`; the newly found ordered `q = 29` cycle has ratio 1/4. Because (H) also holds on the unordered cycles, this broad finite success does not identify circular order as the decisive ingredient. Stronger logarithmic and half-linear candidates already fail on exact controls.
- **Matching mechanism, open.** Overlapping residue sets still admit distinct representatives in all 1,184 tested `q > 1` cycles ([`RESIDUE_MATCHING.md`](RESIDUE_MATCHING.md)); a universal matching theorem for ordered cycles would imply `B + 1 ≤ φ(q)`, but it is an open sufficient mechanism, `q = 1` was omitted, and a finite pass is not a proof.
- **Related restrictions.** [`ordered-cycle-sparse-forcing`](../../results/ordered-cycle-sparse-forcing/README.md) gives `q > (D/C_c)·2^(ceil(m/J)−1−B)`; as `J` grows with the period this puts no upper bound on `B` at fixed `q`.

## Suggested attacks

From the legacy report and notes:

- Couple the full divisibility `D | C_h` at `q = 1` with legal odd numerator heights and rank inequalities. A proof using only normalised order, the height coboundary and real positivity would also apply to the rational rescaling of the `q = 5` cycle, so it must use integer-lattice or full-divisibility information.
- Analyse the full integer gap or weighted-intercept congruence for an ordered profile with `B ≥ q`, beginning with the smallest case `q = 1`, `B = 1` (every nontrivial Collatz cycle has `H ≥ 4L`), retaining rank inequalities and exact odd outputs. Excluding ordered denominator-one cycles in the single band `B = 1` is a genuinely intermediate milestone, strictly weaker than the full target.
- A two-band calculation is useful only if it exposes an argument that can handle unrestricted height complexity. Another wider seed census has little discriminating value; new searches should be driven by a specific proposed obstruction or counterexample family.

## Evidence in this folder

- [`HEIGHT_DENOMINATOR.md`](HEIGHT_DENOMINATOR.md): the candidate, the modular lemma and the min–top inequality, with written proofs; [`INDEPENDENT_ARITHMETIC.md`](INDEPENDENT_ARITHMETIC.md): an independent main-lane probe and review of it. Both are pinned by SHA-256 in [`arithmetic_obstructions.json`](arithmetic_obstructions.json) (see History).
- [`check_height_denominator.py`](check_height_denominator.py), [`height_denominator_audit.json`](height_denominator_audit.json): the census checker and receipt; [`check_arithmetic_obstructions.py`](check_arithmetic_obstructions.py), [`arithmetic_obstructions.json`](arithmetic_obstructions.json): a second implementation checking the modular identity, the integer weighted intercept and the exact shortcut counterexamples (1,185 normalised cycles, 28,830 modular arrows, 99 relaxed pair examples). Neither runs at the new path: both load the corpus as `HERE.parent/'C001/actual_cycles.json'` (and the census checker also loads `experiments/phase6/cycle_fixtures.json` and `C006/order_rigidity_audit.json` by old path). They passed at `be73a66` as `experiments/cycle_spectrum/C007/check_height_denominator.py` and `check_arithmetic_obstructions.py` ([`archive/legacy-checker-run-be73a66.md`](../../../../archive/legacy-checker-run-be73a66.md)).
- [`RESIDUE_MATCHING.md`](RESIDUE_MATCHING.md), [`residue_matching_replay.json`](residue_matching_replay.json): the matching audit; its replay code is embedded in the note and reads the corpus by its old path.
- [`c007_height_check.py`](c007_height_check.py), [`c007_height_check.json`](c007_height_check.json): the side lane's REFEREE check. It needs the corpus path as argument (exit 1 bare at `be73a66` as `reviews/side_lane/c007_height_check.py`); with `areas/cycles/results/actual-cycles-3x-d-corpus/actual_cycles.json` it exits 0 and reproduces its receipt byte for byte (checked at migration).
- [`ROOT_REVIEW.md`](ROOT_REVIEW.md), [`SIDE_REVIEW.md`](SIDE_REVIEW.md): main-lane root review and the main lane's read of the side-lane feed; [`delivery_checks.json`](delivery_checks.json), [`historical_gate.json`](historical_gate.json): historical delivery receipt and historical finite gate.

## History

- Migrated from `experiments/cycle_spectrum/C007/` (legacy ID `C007`; `REPORT.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c007_height_check.{py,json}` moved here. All C007 scripts, receipts and notes stay together in this folder because the scripts locate each other's files by path (`check_arithmetic_obstructions.py` reads `height_denominator_audit.json` and hashes the two notes from its own folder). Parts became [`ordered-cycle-residue-law`](../../results/ordered-cycle-residue-law.md), [`ordered-cycle-height-census`](../../results/ordered-cycle-height-census.md) and [`height-bound-via-residues-or-relaxation`](../../attempts/height-bound-via-residues-or-relaxation.md).
- **Link repair in pinned notes (2026-10-19, B03 migration).** `HEIGHT_DENOMINATOR.md` and `INDEPENDENT_ARITHMETIC.md` linked to `../C005/` and `../C006/` legacy paths that no longer exist; the repository check forbids broken links, so only those link targets were repointed to the migrated notes. Their SHA-256 values pinned in `arithmetic_obstructions.json` (`2d01dd74…`, `b82c5801…`) therefore describe the `be73a66` versions; the checker that compares them already fails at its new path for the reasons above. No mathematical text changed.
- Main lane (ChatGPT/Codex), 2026-10-19. Two wording issues were corrected before publication: reduction of the numerator/denominator pair, rather than period primitivity alone, supplies `q = D/gcd(C_h, D)`; and repeated residue classes disprove disjointness of the full sets but not a choice of distinct representatives (the `q = 5` control admits one). The candidate `B ≤ q − 1` was retained as open, with no proof or counterexample claimed.
