---
id: ordered-cycle-sorted-rank-residues
kind: result
title: Ordered cycles have sorted residues L·t^j mod q, so ⟨2,3⟩ mod q is cyclic and 35, 65, 91 never divide q
status: reviewed
claim: >
  Raw odd-only clock, no absorption. Let a primitive positive ordered cycle (q ≤ L, m > 1, circular
  normalised successor order) have reduced odd denominator q > 1 coprime to 6, totals (A, m) and
  rank shift s, so A = m + s and gcd(A, m) = 1. For every divisor Q > 1 of q, choose um + vA = 1 and
  t = 2^u·3^v mod Q: then t^m ≡ 2, t^A ≡ 3, and the sorted normalised states satisfy
  z_[j] ≡ L·t^j (mod Q) for 0 ≤ j < m, with ord_Q(t) ≥ 4. Consequently the subgroup ⟨2,3⟩ of
  (Z/qZ)^× is cyclic; more generally, if d | q and e(d) = gcd(ord_d(2), a, b) > 1 (b the least
  positive exponent with 3^b ∈ ⟨2⟩ mod d, 2^a ≡ 3^b), no such ordered cycle exists. In particular
  35, 65 and 91 never divide q. Nothing is said at q = 1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma, ordered-cycle-residue-law]
lean:
  - LeanLane.Cyc.exists_common_root
  - LeanLane.Cyc.zmod_common_root
  - LeanLane.Cyc.NarrowCycle.sum_a_range
  - LeanLane.Cyc.OddCycle.prefix_identity
  - LeanLane.Cyc.OddCycle.cycle_identity
  - LeanLane.Cyc.OddCycle.q_dvd_D
  - LeanLane.Cyc.OddCycle.sorted_residue_law
certificates: [check_legacy_replay.py]
evidence:
  - "MATCHING_ARITHMETIC.md: main written proofs (section 3: the cyclicity theorem, the relation lattice and the forbidden factors; sections 1-2 belong to small-band-height-residue-matching)"
  - "INDEPENDENT_MATCHING.md: independent main-lane proof of the sorted-rank law (R1), T ≥ 4, and the two primewise counterexamples"
  - "check_residue_spectrum.py, residue_spectrum_audit.json: main-lane relation-lattice checker (332 moduli up to 1000, 477,552 finite cells) and receipt. Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json' and C007's census by old path. Passed at be73a66 as experiments/cycle_spectrum/C008/check_residue_spectrum.py (archive/legacy-checker-run-be73a66.md). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "check_height_matching.py, height_matching_audit.json: main-lane matching checker and receipt (3.4 MB; all 1,185 normalised cycles, 2,459 source cycles, 11 fixtures, 946,001 screened profiles). Fails at its new path for the same reason (it also loads experiments/phase6/cycle_fixtures.json (now in ../../../convergence/results/baseline-obligation-transfer-controls/, byte-identical)). Passed at be73a66 as experiments/cycle_spectrum/C008/check_height_matching.py. Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "c008_residue_check.py, c008_residue_check.json: side-lane REFEREE check. Needs the corpus path as argument, so it fails bare (exit 1 bare at be73a66 as reviews/side_lane/c008_residue_check.py, archive/legacy-checker-run-be73a66.md). Run as python3 <this folder>/c008_residue_check.py areas/cycles/results/actual-cycles-3x-d-corpus/actual_cycles.json it exits 0 and reproduces its receipt byte for byte (checked at migration). Now replayed unmodified, with every file unchanged, by check_legacy_replay.py (B18-replay-revival migration)"
  - "check_delivery.py, delivery_checks.json: historical delivery check and receipt; the script is pinned to the historical commits that produced it and fails at HEAD by design (it failed at be73a66 too)"
  - "ARITHMETIC_REVIEW.md, CHECKER_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed; LITERATURE.md: bounded literature scope; historical_gate.json: historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c008_residue_check.py
    scope: "Feed 2026-10-19 02:56, REFEREE C008 at main 93117c0: sorted-rank law on all 50 ordered census cycles with q > 1, cyclicity of ⟨2,3⟩ mod q, noncyclicity mod 35, 65, 91, no ordered census cycle with those factors, and both primewise counterexamples reproduced. Feed 03:09: Lean C008-a statement match and receipts checked"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 03:01: C008 re-derived by hand with no error (sorted-rank law from P_i = floor(iA/m), ord(t) ≥ 4, ⟨2,3⟩ mod 35 ≅ Z/2 × Z/12 not cyclic); Lean unit C008-a verified (iteration 24)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [C008]
tags: [cycles, dyadic-order, residues, denominator-spectrum]
---

# Ordered cycles have sorted residues L·t^j mod q, so ⟨2,3⟩ mod q is cyclic and 35, 65, 91 never divide q

## Statement

Use raw positive odd-only cycles, no absorber. Let a primitive cycle satisfy `3n_i + q = 2^(a_i)·n_(i+1)`, `a_i ≥ 1`, with `q` reduced and coprime to 6, `L = min n_i`, `h_i = floor(log₂(n_i/L))`, `B = max h_i`, `z_i = n_i/2^(h_i)`. The **ordered domain** requires `q ≤ L`, `m > 1` and circular normalised successor order, equivalently increasing images `3z_i + q/2^(h_i)` in sorted `z` order ([`dyadic-order-lemma`](../dyadic-order-lemma.md)). There the normalised word is the lower mechanical word, `A = m + s` and `gcd(A, m) = 1`, where `s` is the successor rank shift.

1. **Sorted-rank law.** For every divisor `Q > 1` of `q`, choose integers `u, v` with `um + vA = 1` and put `t = 2^u·3^v mod Q`. Then

```
t^m ≡ 2,   t^A ≡ 3,
z_[j] ≡ L·t^j          (mod Q),   0 ≤ j < m,          (R1)
n_[j] ≡ L·t^(j + m·H_j) (mod Q),
```

where `z_[j]` is the `j`-th smallest normalised state and `H_j` its height. Normalised collisions occur exactly at equal rank classes modulo `T = ord_Q(t)`, and `T ≥ 4`.

2. **Cyclicity.** The subgroup `⟨2,3⟩` of `(Z/qZ)^×` is cyclic (it equals `⟨t⟩`).

3. **Forbidden factors.** For `d > 1` coprime to 6 put `n = ord_d(2)`, let `b` be the least positive integer with `3^b ∈ ⟨2⟩ mod d`, and `0 ≤ a < n` with `2^a ≡ 3^b (mod d)`. The relation lattice `{(A, m) : 2^A ≡ 3^m mod d}` is `Z(n, 0) + Z(a, b)`; with `e(d) = gcd(n, a, b)`,

```
e(d) > 1  and  d | q   ⇒   no ordered primitive cycle.          (5)
```

`⟨2,3⟩ mod d` has Smith invariant factors `e(d)` and `nb/e(d)`. In particular **35, 65 and 91 never divide `q`** in the ordered domain, at any period or height:

| `d` | `n = ord_d(2)` | `a` | `b` | `e(d)` |
| ---: | ---: | ---: | ---: | ---: |
| 35 | 12 | 10 | 2 | 2 |
| 65 | 12 | 4 | 4 | 4 |
| 91 | 12 | 0 | 6 | 6 |

The statement gives no conclusion at `q = 1`, where every residue is 0, and does not rule out prime reduced denominators, whose unit groups are cyclic.

## Proof

Written proofs: [`MATCHING_ARITHMETIC.md`](MATCHING_ARITHMETIC.md) §3 and [`INDEPENDENT_MATCHING.md`](INDEPENDENT_MATCHING.md) §1 (legacy text, lightly edited).

Since `Q | D = 2^A − 3^m`, `2^A ≡ 3^m (mod Q)`; Bezout gives `t^m = 2^(um)·3^(vm) = 2^(um+vA) = 2` and likewise `t^A = 3`, so `⟨2,3⟩ = ⟨t⟩`. The normalised arrow gives `z_i ≡ L·3^i·2^(−P_i) (mod Q)` from the phase at `L` ([`ordered-cycle-residue-law`](../ordered-cycle-residue-law.md)); substituting `3 = t^A`, `2 = t^m` gives `z_i ≡ L·t^(Ai − mP_i)`, and mechanicality `P_i = floor(iA/m)` gives `Ai − mP_i ≡ is (mod m)`, the sorted rank of phase `i`. Primitivity makes these ranks a permutation. Orders `T = 1, 2, 3` would make `Q` divide `gcd(2^T − 1, 3^T − 1) = 1`, so `T ≥ 4`.

For the forbidden factors: if `35 | q`, modulo 7 `2 = 3^2` and `ord_7(3) = 6` give `m ≡ 2A (mod 6)`, hence `m` even; modulo 5 `3 = 2^3` and `ord_5(2) = 4` give `A ≡ 3m (mod 4)`, hence `A` even, contradicting `gcd(A, m) = 1`. If `65 | q`, modulo 13 `3 = 2^4` gives `4 | A`, and modulo 5 then `4 | m`. If `91 | q`, modulo 13 gives `4 | A` and `A ≡ m (mod 3)`; modulo 7 gives `m` even and `m ≡ −A (mod 3)`, so 3 divides both. The lattice description: the image of 3 in `⟨2,3⟩/⟨2⟩` has order `b`, so every relation has `b | m`, and then `A ≡ a(m/b) (mod n)`; every relation has both coordinates divisible by `e(d)`.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C008-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md)), axioms `propext`, `Classical.choice`, `Quot.sound` (helpers subsets); receipts `lean/receipts/CycleSpectrum.*`. It covers parts 1 and 2 but not part 3, so the node is `reviewed`, not `formal`.

- `exists_common_root`: in any commutative group, `x^A = y^m` with `gcd(A, m) = 1` gives `t` with `t^m = x`, `t^A = y`. `zmod_common_root`: for `N` coprime to 6 with `N | 2^A − 3^m` and `gcd(A, m) = 1`, there is a unit `t` of `ZMod N` with `t^m = 2`, `t^A = 3`; so `⟨2,3⟩` is cyclic modulo every such `N` (part 2).
- `OddCycle.prefix_identity`, `OddCycle.cycle_identity` (`(2^A − 3^m)·n_0 = q·C_m`) and `OddCycle.q_dvd_D` (`q | 2^A − 3^m` for reduced cycles).
- `NarrowCycle.sum_a_range` (`P_i = floor(iA/m)`) and `OddCycle.sorted_residue_law`, the integer form of (R1): `2^(P_i)·z_[(ih) mod m] ≡ 3^i·z_[0] (mod q)`. The final substitution to `z_[j] ≡ L·t^j` is not written out in Lean.
- Not formalised: the forbidden factors 35, 65, 91 and the lattice test (5), `T ≥ 4`, and the counterexample cycles.

## Remarks

- **Scope.** This restricts the ordered spectrum for `q > 1`. Cyclicity is an elementary consequence of the coprime totals of ordered cycles ([`dyadic-order-lemma`](../dyadic-order-lemma.md)) and is not evidence for residue matching. At `q = 1` all residue information disappears, so no argument of this kind reaches [`ordered-cycle-denominator-one`](../../questions/ordered-cycle-denominator-one.md); the legacy report and the side-lane referee both say so.
- **Controls.** The ordered domain matters: the raw `q = 35` cycle `(13, 37, 73, 127)` has word `(1,1,1,5)`, totals `(8, 4)` and `L = 13 < q`; it lies outside the theorem and has the expected common factor in its totals. Actual cycles with factors 35, 65, 91 survive outside the ordered domain (receipt `residue_spectrum_audit.json`). For the ordered `q = 5`, period-17 cycle, `s = 10`, `A = 27`, `t ≡ 2 (mod 5)`, and the sorted residues repeat every four ranks.
- **Related.** The small-band matching theorem from the same batch: [`small-band-height-residue-matching`](../small-band-height-residue-matching.md); the refuted primewise route: [`primewise-height-residue-matching`](../../attempts/primewise-height-residue-matching.md); the open full matching proposal: [`height-residue-hall-matching`](../../questions/height-residue-hall-matching.md).
- **Novelty.** The side-lane referee calls cyclicity "a genuine, if elementary, new necessary condition in the spectrum law"; the legacy report claims no novelty. Novelty undetermined.

## History

- Migrated from `experiments/cycle_spectrum/C008/` (legacy ID `C008`; `REPORT.md`, proofs `MATCHING_ARITHMETIC.md` §3 and `INDEPENDENT_MATCHING.md` §1) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c008_residue_check.{py,json}` moved here. All C008 scripts, receipts and notes stay in this folder. Parts of the legacy report became [`small-band-height-residue-matching`](../small-band-height-residue-matching.md), [`primewise-height-residue-matching`](../../attempts/primewise-height-residue-matching.md) and [`height-residue-hall-matching`](../../questions/height-residue-hall-matching.md).
- Main lane (ChatGPT/Codex), 2026-10-19, main commit `93117c0`. Formalised in part by the Lean lane (Claude Lean lane, Fable) as C008-a, iteration 24.
- **Link repair in pinned notes (2026-10-19, B04 migration).** `MATCHING_ARITHMETIC.md` linked to `../C006/` and `../C007/` legacy paths; only those link targets were repointed to the migrated notes. Its SHA-256 pinned in `check_delivery.py`, `delivery_checks.json` and the review notes (`aefff8c4…`) therefore describes the `be73a66` version; `check_delivery.py` already fails by design. No mathematical text changed.
