---
id: equal-total-two-block-exclusion
kind: result
title: Two different equal-total blocks repeated at least three times never give an integer cycle
status: formal
claim: >
  Raw odd-only clock. Let u ≠ v be nonempty positive valuation words of the same length m and the
  same total A, with U = 2^A > V = 3^m, and let k, ℓ ≥ 1 with k + ℓ ≥ 3. Then
  den(u^k v^ℓ) > 2^m·2^A/3^m > 2^m > 1, i.e. 2^A·2^m·gcd(C_w, D_w) < 3^m·D_w for w = u^k v^ℓ.
  There is no bound on m, A, the two words or the repetition counts; the blocks need not be
  primitive and different cyclic phases count as different words. In particular no such word is
  an integer cycle of 3x+1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [proportional-slope-two-block-bound]
lean:
  - LeanLane.Cyc.uniform_two_block_strong
  - LeanLane.Cyc.uniform_two_block
  - LeanLane.Cyc.gcd_dvd_K_mul_gcd
  - LeanLane.Cyc.gcd_pow_sub_pow
  - LeanLane.Cyc.C_injective
  - LeanLane.Cyc.two_pow_mul_C_le
certificates: [c002_two_block_check.py]
evidence:
  - "PROPORTIONAL.md: the written proof (section 1 identities, section 2 'Uniform equal-total corollary'); it also holds the proofs used by proportional-slope-two-block-bound and rotating-mechanical-two-block-family"
  - "check_two_blocks.py, two_blocks_audit.json: main-lane finite checker and receipt. Fails at its new path: it loads the corpus as HERE.parent/'C001/actual_cycles.json' and the fixtures from experiments/phase6/ (cycle_fixtures.json, now in ../../../convergence/results/baseline-obligation-transfer-controls/, byte-identical). Passed at be73a66 as experiments/cycle_spectrum/C002/check_two_blocks.py (archive/legacy-checker-run-be73a66.md)"
  - "c002_two_block_check.json: receipt of the side-lane check (rewritten identically on each run)"
  - "INDEPENDENT_REVIEW.md, ROOT_REVIEW.md: main-lane reviews; SIDE_REVIEW.md: the main lane's read of the side-lane feed"
  - "delivery_checks.json, full_gate.json: historical delivery receipt and historical finite gate"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    link: c002_two_block_check.py
    scope: "Side-lane feed (archive/side-lane/FEED.md, legacy archive/side_lane/FEED.md), entry 2026-10-19 00:26, REFEREE C002 at main e14a4e3: the uniform theorem re-derived by hand and checked on 434,350 exhaustive and 3,902 random cases; ingredients and exact examples checked; verdict correct"
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Lean unit C002-a verified (feed 00:45, update 00:50): uniform_two_block_strong proves the full bound under exactly C002's hypotheses; the Lean lane had also re-derived PROPORTIONAL.md sections 1-4 by hand and found no error (feed 00:26, update 00:31)"
    link: ../../../../archive/side-lane/FEED.md
aliases: [C002]
tags: [cycles, denominators, two-blocks, uniform, formal]
---

# Two different equal-total blocks repeated at least three times never give an integer cycle

## Statement

Let `u` and `v` be different nonempty positive valuation words, each of length `m` and total `A`, with `U = 2^A > V = 3^m`. For arbitrary `k, ℓ ≥ 1` with `k + ℓ ≥ 3`,

```
den(u^k v^ℓ) > 2^m · 2^A/3^m > 2^m > 1.
```

The proof retains exact integer valuations and uses the raw odd-only map, including its arrow at 1. There is no bound on `m`, `A`, the two words, or either repetition count. The two blocks need not themselves be primitive. Different cyclic phases count as different words here, and are allowed.

This is an exclusion of a specified structural class of cycles; an arbitrary cycle word need not have this form. The hypotheses `u ≠ v` and `k + ℓ ≥ 3` are essential to the proof; the result is not applied to identical blocks or to the remaining case `k = ℓ = 1`.

**Effective finiteness across the class** (immediate corollary, written; not separately formalised). If the reduced denominator is at most `d_0`, then `2^m < d_0` and `2^(A+m) < d_0·3^m`. Only finitely many totals and positive words remain, and for each pair the bound (8) of [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md) bounds both exponents. So bounded-denominator layers can be enumerated within the whole class, uniformly over varying blocks.

## Proof

Written proof: [`PROPORTIONAL.md`](PROPORTIONAL.md), "Uniform equal-total corollary". Summary (legacy report):

Write each block action as `(3^m·x + C_z)/2^A`. Exact suffix lengths (each `a_j ≥ 1` gives `A_j ≤ A − (m − j)`) give

```
0 < C_z ≤ 2^(A−m)·(3^m − 2^m) < U·V/2^m.          (U2)
```

Different equal-total words have different `C`: otherwise the same positive rational fixed point would have two different exact valuation histories of the same length. Set `J = C_v − C_u`, `n = k + ℓ` and `h = gcd(k, ℓ)`. Elimination and strong divisibility (`gcd(U^i − V^i, U^j − V^j) = U^gcd(i,j) − V^gcd(i,j)` for coprime `U, V`) give

```
den(u^k v^ℓ) > U^(n−h)/|J|.
```

Since `n ≥ 3` implies `n − h ≥ 2`, and `|J| < UV/2^m`, the claimed bound follows. No prime-factor distribution assumption is used.

## Certificates

- [`c002_two_block_check.py`](c002_two_block_check.py) (about 10 s; side lane, independent code): the uniform inequality on every case with `m ≤ 4`, `A ≤ 2m + 2`, `k, ℓ ≤ 6` plus random pairs with `m ≤ 9`; the ingredients `0 < C_z ≤ 2^(A−m)(3^m − 2^m)`, injectivity of `C` on equal-shape words and the intermediate bound; the exact examples of [`constant-cancellation-two-growing-blocks`](../../attempts/constant-cancellation-two-growing-blocks.md) for `t ≤ 40`; the `d = 59` cycle; and the rotating mechanical family for `13 ≤ m ≤ 30`, `k, ℓ ≤ 3`. It rewrites `c002_two_block_check.json` on every run, with identical content.

The main lane's checker [`check_two_blocks.py`](check_two_blocks.py) no longer runs at this path (see `evidence`). Its receipt [`two_blocks_audit.json`](two_blocks_audit.json) records:

| Check | Scope |
| --- | ---: |
| Stored actual cycles replayed | 2,459 across 333 parameters |
| Historical cycle fixtures retained | All 11 |
| Canonical two-block power decompositions | 37,271 |
| Actual decompositions with both repetitions at least 2 | 56 |
| Ordered generated block pairs | 7,056 |
| Generated exponent/word cases | 451,584 |
| Positive integer-cycle realizations | 433,074 |
| Distinct parameters of those realizations | 5,003 |
| Exact generated odd arrows | 10,623,694 |
| Positive common-fixed-point controls | 6,016 |
| Generated equal-total uniform bounds | 33,768 |
| Generated proportional-slope bounds | 44,544 |
| Rotating-mechanical examples | 590, including block lengths 256 and 512 |

Generated blocks have lengths 1–3, valuations 1–4 and both repetition counts 1–8; expanding blocks are included. Realizations can repeat the same primitive cycle: 427,028 cases have primitive displayed words and 6,046 have proper-power words. These are case counts, not distinct cycles. There are **zero eligible equal-total `k + ℓ ≥ 3` decompositions** in the canonical actual-cycle sample: the uniform inequality is exercised by the generated integer cycles and the rotating examples. The actual sample exercises 459 proportional bounds and the general elimination identity. The finite tests do not verify the imported asymptotic theorem of [`unequal-slope-two-block-growth`](../unequal-slope-two-block-growth/README.md).

## Lean

`lean/CycleSpectrum.lean`, Lean unit C002-a (legacy `lean/STATE.md`, now [`archive/lean-lane/STATE.md`](../../../../archive/lean-lane/STATE.md)):

- `LeanLane.Cyc.uniform_two_block_strong`: for nonempty `u ≠ v` with positive entries, `u.length = v.length`, `u.sum = v.sum`, `3^m < 2^A`, `k, ℓ ≥ 1`, `k + ℓ ≥ 3`, it proves `2^A · (2^m · gcd(C_w, D_w)) < 3^m · D_w` for `w = rep u k ++ rep v ℓ`. Dividing by `gcd · 3^m` this is exactly `den(w) > 2^m·2^A/3^m`. The hypotheses are the prose's; `v ≠ []` follows from equal length.
- `uniform_two_block`: the weaker `2^m · gcd < D_w`, i.e. `den(w) > 2^m`, as a corollary.
- Ingredients: `gcd_dvd_K_mul_gcd` (`g | |K|·gcd(G_u(k), G_v(ℓ))`, no coprimality premise), `gcd_pow_sub_pow` (strong divisibility for coprime integers), `C_injective` (via the dynamics-free `v₂` recursion: `v₂(C_z − 3^(m−1)) = a_0` when `m ≥ 2`), `two_pow_mul_C_le` ((U2)).

`C (a :: z) = 3^|z| + 2^a·C z` unfolds to the `C_w` of `conventions/NOTATION.md`; `D z = 2^Σz − 3^|z|`; `rep u k` is `u^k`. Axioms: `propext`, `Classical.choice`, `Quot.sound` (receipts `lean/receipts/CycleSpectrum.*`). The effective-finiteness corollary above is not separately stated in Lean.

## Remarks

- **Controls.** Identical-block repetitions (`K = 0`) preserve the `d = 1, 5, 7, 13` cycles; the theorem excludes them by hypothesis (`u ≠ v`), consistently with the controls. Actual cycles exercise the general and proportional identities; generated integer cycles exercise the uniform inequality.
- **Fixed-pair picture.** For arbitrary fixed `u, v` and `K = D_u·C_v − D_v·C_u`, the two elimination identities give `gcd(C_w, D_w) | |K|·gcd(G_u(k), G_v(ℓ))` when `K ≠ 0`. The common geometric factor is indispensable. The regimes:

| Block relation | Proved conclusion | Node |
| --- | --- | --- |
| Equal valuation-to-length ratios, `K ≠ 0` | Explicit exponential lower bound, retaining at least half the common exponent | [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md) |
| Unequal ratios | `log den(w) = sum(w)·log 2 − o(k+ℓ)` on the whole positive domain; ineffective | [`unequal-slope-two-block-growth`](../unequal-slope-two-block-growth/README.md) |
| `K = 0` and `D_w > 0` | Both blocks repeat the same primitive rational cycle from the same phase; its denominator persists | [`repeated-block-cancellation-bound`](../repeated-block-cancellation-bound/README.md), claim 4 |

- **Coverage.** The result excludes a stated class of words; it does not supply a decomposition of arbitrary cycle words into that class. The two-occurrence case `k = ℓ = 1` and unrelated block totals remain outside the uniform theorem. C001's constant cancellation bound does not survive two growing blocks: [`constant-cancellation-two-growing-blocks`](../../attempts/constant-cancellation-two-growing-blocks.md). The contracting-block theorem of [`contracting-two-block-effective-exclusion`](../contracting-two-block-effective-exclusion/README.md) covers further unequal-total classes, but not the counts `(1, 2)` covered here.
- **Family.** A primitive nonbalanced family with growing minima to which this applies: [`rotating-mechanical-two-block-family`](../rotating-mechanical-two-block-family.md).
- **Literature and novelty.** Trümper's 2014 T-word paper contains the concatenation, commutator and repetition formulas in its own notation. Novelty undetermined; no claim to improve a published record.
- **Legacy decision.** The main lane judged C002 progress through a uniform structural exclusion, the two-slope classification for fixed pairs, and the exact obstruction to bounded cancellation, and recommended seeking a restriction on how genuine cycle words can be assembled while their blocks vary, rather than a larger catalogue. Seven-field table of the legacy report: objects, exact denominator layers of positive rational cycles; structural gain, this theorem; translated gap, arbitrary primitive words need not have repeated-block structure; worked example, `(1,1,3)^t (1,2,2)^t` with denominator `5·(32^t + 27^t)`; cheapest next test, whether removing the equal-total hypothesis keeps an explicit uniform obstruction.

## History

- Migrated from `experiments/cycle_spectrum/C002/` (legacy ID `C002`; `REPORT.md`, proof `PROPORTIONAL.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). The side-lane check `reviews/side_lane/c002_two_block_check.{py,json}` moved here. The legacy report's other parts became [`proportional-slope-two-block-bound`](../proportional-slope-two-block-bound.md), [`unequal-slope-two-block-growth`](../unequal-slope-two-block-growth/README.md) (with `INDEPENDENT_SLOPES.md`), [`rotating-mechanical-two-block-family`](../rotating-mechanical-two-block-family.md) and [`constant-cancellation-two-growing-blocks`](../../attempts/constant-cancellation-two-growing-blocks.md).
- Main lane (ChatGPT/Codex), 2026-10-19. The root proposed the uniform equal-total corollary; two independent main-lane agents checked it before inclusion. Two draft issues were corrected before delivery (recorded in [`INDEPENDENT_REVIEW.md`](INDEPENDENT_REVIEW.md)): the sharpness example first removed the factor 7 before proving the common divisor coprime to 7; and the first examples used full block totals where the reduced slope `(a, b)` was required. The denominator formula itself was correct.
- Formalised by the Lean lane (Claude Lean lane, Fable) as unit C002-a, 2026-10-19 (`uniform_two_block` first, then the full bound `uniform_two_block_strong`).
