# Review of rational-basin-precision-barrier

Independent review of [`README.md`](README.md) with its dependencies [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25) and [`binary-return-exit-control`](../binary-return-exit-control/README.md) (R90), both `reviewed`. Scratch scripts (outside the repository): `review-work/rational-basin-precision-barrier/classify_basin.py`, `compare_hits.py`, `check_corollary.py`, `check_r90_input.py`.

## What I checked

- **Certificates.** `python3 tools/run_certificates.py --node rational-basin-precision-barrier --timeout 900`: both PASS, exit 0; `check_shadow_precision_recompute.py` 19 s, `check_legacy_replay.py` 19 s, 38.0 s wall in all.
- **Signed quotient (§2).** From the node's definitions only I wrote a second implementation on `x = −z/D`: `S` with the valuation of `3z − D`, the F-division test `z ≡ 3 (mod 8)` (i.e. `x ≡ 5 (mod 8)` since `D ≡ 1 (mod 8)`), the selected test `z ≡ 1 (mod 4)` with the unit of `(D − z)/2^a` compared to `3^a (mod 4)`, and the exponent `e = v + 2·(F divisions) + (halving)`. Its orbit of `c0` is the displayed 12-cycle, with the displayed `u` values and exponents `(1,1,1,3,1,2,2,1,2,1,1,3)`, sum 19.
- **Branch inequalities (5) and the inverse table.** The table equals R25's inverse table; `α ≥ 2/3`, `α − β ≥ 1`, `β ≥ −1/3` verified on the seven base branches and on ray indices `0, …, 6` (`α_L = 64^L α_0`, `β_L = 64^L β_0 + 7(64^L − 1)/9`, and `α_L − β_L = 64^L(α_0 − β_0 − 7/9) + 7/9 ≥ 1`). Hence every inverse state from `c0` is `< −1`.
- **Shadow legality.** On the 12 cycle states and the 19 hit origins, every table branch with the matching residue mod 3 (160 cases) gives a state with denominator `D`, below `−1`, canonical, that my `T` maps back with slope `2^e/3`; this is the step that lifts an actual inverse word to a legal shadow word.
- **Reduction (6)–(7).** Re-derived `t' = αt + Dδ` with `δ = α − β − 1 ∈ [0, α)`, the unrolling `t_d = λ_d t_0 + D Σ δ_j λ_d/λ_j`, the prefix-minimality bound `λ_d/λ_(j−1) < γ^(k_(j−1) − k_d)`, the depth counts (six prefixes with `k = 0`, twelve per later `k`), and `12 D γ/(γ − 1) = 12·3^12 = 6377292`; with `t_0 = 892688` this is `u < 7277133`. Only the first hit matters because `k(d + 12) = k(d) + 1` and a cycle adds `(12, 19)`.
- **Classification (§4), independently.** My classifier resolved every odd canonical `u` coprime to `7153` in `(7153, 7277133)` by forward iteration with memoisation and no cap: **1,732,883 origins, 19 reach `c0`, largest numerator visited 1,049,066,989,135, minimum first-hit score 1** (7 s). The 19 records `(u, d, E, μ)` agree row for row with the node's table, and each displayed `μ` equals `2^(E−19k) 3^(12k−d)`.
- **Corollary (§5).** `n0 > 2Q` coefficientwise (`3·67839005952677 > 2·70506316836123` and `2^18·3^19 > 3·2^46`); `v₃(L(v0)) = 4` and `v₂(L(v0)) = 19` at `ℓ = 0` (so `≥ 18` for every `ℓ`); (9) `n_r − c0 = γ^r(n0 − c0)` by hand from `D + M = A`; `v₃(n_r − c0) = 12r + 5`; (10) from `β_j ≥ −1/3`, `λ_j ≥ (2/3)^j`; (11) with the bracket `−c0 + γ^(−r)(c0 + 1) = (−c0 − 1)(1 − γ^(−r)) + 1 ≥ 1`; `(3/2)^(12r+5) = (243/32)·2^(7r)·γ^r`; (12) `243(2^18 − D/16) > 3B`; `k(12r + 5) = r`. At an `ℓ` with `v₂(L(v0)) = 76` (three guarded returns) my own integer `T = νS` confirms R90's `T^(18+12r)(Q) = n_r` and `S^(23+12r)(Q) = S^5(n_r)` for `r = 0, …, 3`, and `n0 + 1 − (243/32)2^(7r) > Q` there. The ordinary-history clause follows from `T^d(ν(p)) = ν(S^d(p))` and `ν(p) ≤ p`.
- **Controls.** Not applicable: the theorem is a finite classification at one rational centre of the `3x+1` quotient and claims nothing about integer cycles or `d`-uniformity. Consistency note: the affine composition of the 12 quotient steps has slope `3^12/2^19` and fixed point `c0 = −3B/(2^19 − 3^12)`, a negative rational, as the sign of `D_w` in `conventions/NOTATION.md` §2 predicts for `2^19 < 3^12`.

## What I did not check

- The C++ (`independent_basin.cpp`) and C (`c0_basin_classify.c`) classifiers: not compiled; my Python run replaces that comparison.
- R90's exit table and countdown beyond the identities used here; R25's component theorem (both `reviewed` this wave by the same lane in other sessions).
- The 306 positive inverse-word samples in the legacy receipt (evidence only).

## Findings

1. **§4, "Two independent exact implementations … C++ using positive magnitudes" (imprecision).** The certificate reruns only the Python classification; the C++ comparison needs `--cpp` and a compiler, as the Certificates section says. This review's classifier is now a second independent implementation with identical output.
2. **§5, hypothesis "at least `r` guarded returns" (imprecision).** At `ℓ = 0` the cell has `v₂(L(v0)) = 19`, hence `r = 0` only; the corollary for `r ≥ 1` concerns the members of the cell with `v₂(L(v0)) ≥ 19r + 18`, which exist by R90. The text says "suppose", which is correct, but a reader may take `ℓ = 0` as the running example.
3. **Title versus claim (imprecision).** The title says "within 12r + 5 steps" and the body's §6 "the excluded horizon"; the area overview's "12r + 19" refers to this node plus [`fourteen-step-window-original-source`](../fourteen-step-window-original-source/README.md). No change here.

## Verdict

**HOLDS.** The written reduction, the branch inequalities, the shadow legality, the centre identity and the positive corollary are correct as scoped; the computer-assisted classification is reproduced exactly by an independent implementation. No corrections to the claim.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
