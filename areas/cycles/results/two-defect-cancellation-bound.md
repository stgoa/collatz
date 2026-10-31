---
id: two-defect-cancellation-bound
kind: result
title: A two-defect rotation bounds the cancellation by both mismatch arcs, so q > (1 − 3^m/2^A)(2/√3)^m
status: reviewed
claim: >
  Raw odd-only clock; any positive valuation word w = (a_0, …, a_(m−1)), m ≥ 2, with total A,
  D = 2^A − 3^m > 0, g = gcd(C_w, D), q = D/g. Suppose a nonidentity rotation of w differs from w in
  exactly two positions. Then (i) the two differing entries are swapped values a, a + k (a, k ≥ 1),
  both lie on one cycle of the shift permutation, and w is primitive; (ii) cutting at the two
  mismatches into complementary arcs u, v (lengths summing to m, totals to A), g divides
  (2^k − 1)·gcd(C_u, C_v); (iii) g² < (2^k − 1)²·2^(A−m−k−2a+2)·3^m ≤ (2^k − 1)²·2^(A−m−k)·3^m, and with
  δ = A·log 2 − m·log 3, q > 2^((m−k)/2)·2·sinh(δ/2); (iv) without any amplitude restriction,
  g² < 2^(2A−2m)·3^m, i.e. q > (1 − 3^m/2^A)·(2/√3)^m; (v) if the two mismatches are adjacent,
  g | 2^k − 1, and the binary mask (w_i − a)/k is a mechanical word with coprime shift. For any
  rotation by r, gcd(D, C_(R_r w) − C_w) = g·gcd(q, 2^(P_r) − 3^r).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [mechanical-word-exact-denominator]
lean:
  - LeanLane.Cyc.two_arc_identity
  - LeanLane.Cyc.rotate_cut
  - LeanLane.Cyc.dvd_C_rotate_of_dvd
  - LeanLane.Cyc.two_arc_dvd
  - LeanLane.Cyc.intercept_bound_last
  - LeanLane.Cyc.two_defect_bound_sharp
  - LeanLane.Cyc.two_defect_bound
  - LeanLane.Cyc.two_defect_q_bound
  - LeanLane.RotationIdentity.rotation_identity_general
  - LeanLane.RotationIdentity.gcd_rotation_difference
evidence:
  - "two-defect-rotation-exclusion/ROTATION_DEFECTS.md, sections 1-4 and 6: the written proofs and the q = 5, 7, 13, 359 controls"
  - "two-defect-rotation-exclusion/c011_two_defect_check.py: side-lane certificate of that node, checking (i), (iii) and (iv) on every primitive positive word of length ≤ 9 with letters 1-5"
  - "two-defect-rotation-exclusion/rotation_defect_audit.json: 192 two-defect rotations with 384 oriented arc identities on stored cycles (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: two-defect-rotation-exclusion/c011_two_defect_check.py
    scope: "Feed 2026-10-19 04:08, REFEREE C011: swapped pair, den > 1 and both quadratic bounds in exact integer form on 33,360 two-defect rotations; update 04:44: Lean C011-a VERIFIED, receipts sha256 46b48a59… checked"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 04:14: ROTATION_DEFECTS.md read in full, no error; swap structure, automatic primitivity, two-arc identity, g | (2^k − 1)·gcd(C_u, C_v), the intercept bound, (5)-(9) and the adjacent-defect classification re-derived; Lean unit C011-a verified (iteration 32)"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, rotation-distance, two-defect, cancellation]
---

# A two-defect rotation bounds the cancellation by both mismatch arcs, so q > (1 − 3^m/2^A)(2/√3)^m

## Statement

Let `w = (a_0, …, a_(m−1))`, `m ≥ 2`, `a_i ≥ 1`, `P_j = Σ_(i<j) a_i`, `A = P_m`, `D = 2^A − 3^m > 0`, `g = gcd(C_w, D)`, `q = D/g`. The rotated intercepts over `D` are the rational cycle states; divided by `g` they form an actual `3x+q` cycle (NOTATION.md). Let the left rotation `R_r w`, `r ≢ 0 (mod m)`, differ from `w` in exactly two positions.

1. **Structure.** The two differing entries are swapped values `a` and `a + k`, `a, k ≥ 1` (rotation preserves the multiset). They lie on the same cycle of `i ↦ i + r` (the differences `a_(i+r) − a_i` sum to zero on each cycle); every other cycle carries a constant letter, and the active cycle has exactly two switches. A coprime shift gives a binary word; no binary hypothesis is needed below. Such a word is **primitive**: an `e`-fold repetition would have `e` times the mismatch count of the shorter word, which is 0 or at least 2.
2. **Two-arc divisibility.** Cut so the mismatches sit at positions 0 and `ℓ` with `w_0 = a`, `w_ℓ = a + k` (exchanging the compared words if needed). Then `C_(w') − C_w = (2^k − 1)·2^a·3^(m−1−ℓ)·C_u` with `u = (w_1, …, w_ℓ)`; recutting at the other mismatch gives the complementary arc `v = (w_(ℓ+1), …, w_(m−1), w_0)`, because **an intercept does not depend on its last valuation**. Since every rotated intercept is divisible by `g` and `g` is coprime to 6,

```
g | (2^k − 1)·gcd(C_u, C_v),     len(u) + len(v) = m,  Σu + Σv = A.            (2)
```

For an arbitrary rotation, exactly `gcd(D, C_(R_r w) − C_w) = g·gcd(q, 2^(P_r) − 3^r)` (3): a rotation difference can keep an extra factor of `q`, so (2) is a divisibility, not an equality.

3. **Uniform bound.** For a positive word `z` of length `l`, total `S` and last letter `b`, `C_z ≤ 2^(S−l−(b−1))·(3^l − 2^l) < 2^(S−l−(b−1))·3^l` (4). Applied to both arcs, which end in `a + k` and `a`,

```
g ≤ (2^k − 1)·√(C_u·C_v) < (2^k − 1)·√(2^(A−m−k−2a+2)·3^m) ≤ (2^k − 1)·√(2^(A−m−k)·3^m),      (5)
q > 2^(a−1+(m+k)/2)·[2 sinh(δ/2)]/(2^k − 1) ≥ 2^((m+k)/2)·[2 sinh(δ/2)]/(2^k − 1) > 2^((m−k)/2)·[2 sinh(δ/2)],   (6)
```

using `D/√(2^A·3^m) = 2 sinh(δ/2)`, `δ = A·log 2 − m·log 3 > 0`.

4. **No amplitude restriction.** One entry is at least `k + 1` and the rest are positive, so `k ≤ A − m`; then

```
g² < 2^(A−m+k)·3^m ≤ 2^(2A−2m)·3^m,   g < 2^A·(√3/2)^m,   q > (1 − 3^m/2^A)·(2/√3)^m.     (7)
```

5. **Adjacent defects.** If `ℓ = 1`, `C_u = 1` and `g | 2^k − 1` (10); at `k = 1`, `g = 1`. Here `gcd(r, m) = 1`, every letter is `a` or `a + k`, and the mask `b_i = (w_i − a)/k` equals the mechanical mask `floor(((i+1)t + φ)/m) − floor((it + φ)/m)` with `t = Σb_i`, `φ = m − 1 − t`, `rt ≡ 1 (mod m)`. For `k = 1` the word is the mechanical valuation word up to phase, already covered by R71's exact denominator `D` ([`mechanical-word-exact-denominator`](mechanical-word-exact-denominator/README.md)); for `k > 1`, or separated defects, the word need not be mechanical.

## Proof

[`ROTATION_DEFECTS.md`](two-defect-rotation-exclusion/ROTATION_DEFECTS.md) §§1–4 (legacy text, summarised above with every step). For (1), prefix sums of the two words differ by `k` exactly at `j = 1, …, ℓ`, giving the displayed difference. For (3), use `2^(P_r)·C_(R_r w) = 3^r·C_w + D·C_prefix`, divide `D` and `C_w` by `g`, and use `gcd(q, C_w/g) = 1`. For (4), `P_j ≤ S − (l − 1 − j) − b` term by term (the exponent is nonnegative; `l = 1` gives `C_z = 1`). For (5), multiply `b_(i+r) − b_i = 1_(i=0) − 1_(i=1)` by `i` and sum around the cycle to get `rt − m·Σ_(j<r) b_j = 1`; the mechanical mask satisfies the same difference equation (rotation by `r` changes its phase by one), so `b − b*` is invariant under a coprime shift, constant, of total zero, hence zero.

## Lean

Lean unit C011-a, `lean/CycleSpectrum.lean` (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../archive/lean-lane/STATE.md), iteration 32), axioms `propext`, `Classical.choice`, `Quot.sound` (two helpers subsets); receipts `lean/receipts/CycleSpectrum.*`. Not `formal`: the Lean statements are in the two-defect **normal form** `w = a :: (u₀ ++ (a+k) :: v₀)`, `w' = (a+k) :: (u₀ ++ a :: v₀)` with `w'` a rotation of `w`, and the reduction of an arbitrary two-defect rotation to that form (part 1), the real-analytic forms (6) and the adjacent classification (5) are not formalised; identity (3) is (below).

- `two_arc_identity`: `C_(w') − C_w = (2^k − 1)·2^a·3^|v₀|·C(u₀ ++ [a+k])`; `rotate_cut` gives the recut as a rotation, and `C_append_singleton` the last-letter remark.
- `dvd_C_rotate_of_dvd` (a common divisor of `C_w, D_w` coprime to 2 divides every rotated intercept) and `two_arc_dvd`: (2).
- `intercept_bound_last`: (4) in cleared form `2^(|z₀|)·C(z₀ ++ [b]) ≤ 2^(Σz₀)·(3^(|z₀|+1) − 2^(|z₀|+1))`.
- Identity (3), formal since 2026-10-31 in the library module [`lean/LeanLane/RotationIdentity.lean`](../../../lean/LeanLane/RotationIdentity.lean): `rotation_identity_general : r ≤ w.length → 2 ^ (w.take r).sum * C (w.rotate r) = 3 ^ r * C w + D w * C (w.take r)` and `gcd_rotation_difference : r ≤ w.length → Odd (D w) → D w ≠ 0 → (Int.gcd (D w) (C (w.rotate r) - C w) : ℤ) = Int.gcd (C w) (D w) * Int.gcd (D w / Int.gcd (C w) (D w)) (2 ^ (w.take r).sum - 3 ^ r)`, i.e. `gcd(D, C_(R_r w) − C_w) = g·gcd(q, 2^(P_r) − 3^r)` (`D_w` is odd for every positive word).
- `two_defect_bound_sharp`: (5), `g²·2^(|u₀|+|v₀|) < (2^k − 1)²·2^(Σu₀+Σv₀)·3^m`; `two_defect_bound`: (7), `g²·2^(2m) < 2^(2A)·3^m` (needs `a ≥ 1`); `two_defect_q_bound`: `D²·2^(2m) < q²·2^(2A)·3^m` for `D = g·q`, the cleared form of `q > (1 − 3^m/2^A)(2/√3)^m`.

## Remarks

- **Controls.** The actual `q = 359` cycle `n = (209, 493, 919, 779, 337, 685, 1207, 995)`, `w = (1,1,2,3,1,1,2,4)`, `C = 15257`, `D = 26207 = 73·359`, `g = 73`, has a unit-amplitude two-defect rotation by four; cutting at the 3 gives arcs `(1,1,2,4)` and `(1,1,2,3)`, both with intercept 73, so (2) is exact. It is not mechanical (four letters): unit amplitude and two mismatches do not force `g = 1` at arbitrary separation. The raw `q = 5` cycle `(19, 31, 49)` (word `(1,1,3)`, amplitude 2, `D = 5`, `g = 1`), the `q = 7` cycle `(5, 11)` (word `(1,3)`, `D = 7`, `g = 1`) and the `q = 13` cycle `(283, 431, 653, 493, 373)` (word `(1,1,2,2,2)`, unit amplitude, `D = 13`, `g = 1`) all satisfy the bounds at their true denominators. There is no `q ≤ L` restriction.
- **Uses.** (7) at `q = 1` with published inputs: [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md). Finiteness of bounded-denominator layers: [`two-defect-bounded-denominator-finiteness`](two-defect-bounded-denominator-finiteness.md). (7) is the `s = 2` case of the candidate in [`rotation-defect-denominator-candidate`](../questions/rotation-defect-denominator-candidate.md).
- **Novelty.** Undetermined (see [`two-defect-rotation-exclusion`](two-defect-rotation-exclusion/README.md)).

- **Sharpness and slack (2026-10-28).** The step `gcd(C_u, C_v) ≤ √(C_u·C_v)` behind (5) is attained within the factor `3 = 2^k − 1` by the two-marker family `(1, 2^(n−1), 3, 2^(n−1))`, where `C_u = C_v = 4^n − 3^n` and `g = 4^n − 3^n` exactly ([`two-marker-constant-background-exact-denominator`](two-marker-constant-background-exact-denominator/README.md)). On the near-critical words `A ≤ m·log₂3 + 1`, however, the exhaustive census [`few-arc-codings-denominator-census`](few-arc-codings-denominator-census/README.md) finds (7) below the true `q` by at least 4.4 bits at every `m`, 17 bits at `m = 17` and 50 bits at `m = 36`: there the arc intercepts are nearly coprime. The conjectured sharp form is [`half-cancellation-for-few-mismatch-words`](../questions/half-cancellation-for-few-mismatch-words.md).

## History

- Split from `experiments/cycle_spectrum/C011/` (legacy ID `C011`; `ROTATION_DEFECTS.md` §§1–4, 6) at commit `be73a66`, by the B04 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised in normal form by the Lean lane (Claude Lean lane, Fable) as C011-a, iteration 32.
- 2026-10-28: Remarks gain the sharpness witness and the census comparison (Claude cycles lane, Fable 5.1); the claim is unchanged.
- 2026-10-31: identity (3) formalised in `lean/LeanLane/RotationIdentity.lean` (Claude cycles lane, Fable 5.1); claim unchanged.
