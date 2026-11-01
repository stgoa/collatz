# Review of bounded-history-clock-exclusion

## What I checked

- Read the node, its dependencies [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (R25: canonical set, `ν`, `T`, the seven inverse base rows and the ray extension `p → 64p + 49`), [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) (R41), the H17 definition in [`native-growth-original-rank-exit-obstruction`](../native-growth-original-rank-exit-obstruction/README.md) (R79: `v2(217b + 223) = 9r + 17`), and the legacy scripts `history_barrier.py`, `check_history_barrier.py`.
- **Statement 1 (quotient clock), re-derived.** The point branch at `y_k` is `(2y_k − 1)/3 = y_(k−1)` because `2y_k − 1 = 3y_(k−1)`, which also gives `y_k ≡ 2 (mod 3)` for `k ≥ 1`; at `q ≡ 0 (mod 3)` there is no point branch. Every base row has `α − β ≥ 1` (equality only at the point) and a ray at index `L` has `α_L − β_L = 64^L(α − β − 7/9) + 7/9 > 1`; checked all seven rows and `L ≤ 5` in exact rationals, together with (4). Hence (5) keeps `λ − c ≥ 1`. The first-ray coefficients (6) were recomputed by exact affine composition for `k ≤ 8`, `L ≤ 3`: `λ = 2^(e+6L−k)·3^(k−1) = 32·64^L·(3/2)^(k−1)`, `c = λ − m_L`, `m_L = (128·64^L + 7)/9` an integer `≥ 15`, so `c > 0`; `(2/3)^t λ = 3^(e+6L−1) > m_L`, which is (7). Residue agreement of the actual state and the rational shadow needs `v_3(λq) ≥ D + a − d ≥ 1` before step `d + 1 ≤ D + a`; once the shadow is an integer it stays one and stays positive (point branch sends `2 → 1`, the `(4c − 1)/3` ray sends `1 → 1`, all other rows are positive at `c ≥ 0`). The first-ray-at-`q` case: `(16·64^L − 7)/9` is a positive integer, the differences `(8·64^L + 7)/9`, `(32·64^L + 7)/9` are `≥ 1`.
- **Statement 2 (ordinary clock), re-derived.** `d ≤ a`: `S^d(p) + 1 ≤ (3/2)^d(p + 1)`, equality only for `p = q` and all valuations 1. `d > a`: (8)–(9); the clock bound makes `λq` and `c` integers; the negative-shadow argument. The sentence "if a numerator stays negative the result is negative; otherwise division by at least 2 is maximized by the valuation 1 map" compresses a case analysis I completed: once a numerator `3x + 1` is nonnegative at a negative `x`, then `x ∈ [−1/3, 0)`, the next state lies in `[0, 1/2)`, and afterwards `x_(i+1) + 1 ≤ (3/2)(x_i + 1)`, so `m ≥ 0` arrows from a negative real end strictly below `(3/2)^m − 1` (also sampled on 20,000 random negative rationals, no violation). The inverse word applied at `−1` gives `c − λ ≤ −1`, and `λ = 1` forces `E = a`, `d = a` by unique factorisation.
- **Statement 3, re-derived.** The CRT class is the complementary climber `q = 2^H t − 1`, `t ≡ −3^H (mod 4)`; `S^j(q) = 2^(H−j)·3^j t − 1` with valuation-1 arrows for `j ≤ H − 2`, these states complementary canonical since `3^j t ≡ −3^(H−j) (mod 4)`, and the state at `j = H − 1` is `≡ 1 (mod 8)`; so `J ≤ H − 1` as required. `q ≡ 7 (mod 8)` needs `H ≥ 3` and gives `q/3 ≡ 5 (mod 8)`.
- **Statement 4, re-derived.** `b ≡ 9 (mod 16)` from `223 ≡ −1`, `217 ≡ 9`, `9^(−1) ≡ 9 (mod 16)`; `q = 3b ≡ 11 (mod 16)` is complementary with `a = 2`; `S(q) = (3q + 1)/2 ≡ 1 (mod 8)`; the congruence (11) says exactly `v2(217b + 223) = 9r + 17`.
- **Independent brute force** (my own `ν`, `S`, `T`; `canonical ⇔ ν-fixed` and `ν(S(x)) = ν(S(ν(x)))` checked to `2·10^5`): every `q ≤ 4000` with `3 | q`, every `D ≤ v_3(q)`, `J` maximal (`≤ 8`), all `p ≤ q` (canonical for the quotient clock), all `d ≤ D + a`: quotient clock 503 cases, ordinary clock 1000 cases, 0 violations. The two smallest members of the family (10) for `(D, J, H)` in `{(1,1,3), (1,2,3), (2,2,3), (2,3,4), (3,2,4), (1,4,5), (2,5,6), (1,6,7)}` (`q` from 39 to 3519): hypotheses and conclusion verified exhaustively. H17 cells `r = 0`, `D = 1, 2` (`b = 197513`, `459657`): hypotheses and conclusion verified exhaustively over all canonical `p ≤ q`; hypotheses only for `r = 1`, `D ≤ 3`.
- **Certificate.** `python3 tools/run_certificates.py --node bounded-history-clock-exclusion`: PASS, exit 0, wall 7.7 s (a second run 5.8 s). It replays `batch_r84_r85_check.py` and `check_history_barrier.py` unmodified in the legacy layout, receipts unchanged. The legacy checker brute-forces `q < 512` in both clocks, 196 critical and 60 H17 CRT cells and 200 inverse words with ray indices through 64, asserting shadow positivity and `x > q` along each trace.
- **Controls.** The node claims nothing about cycles. The analogue of Statement 2 for `S_d`, `d ∈ {5, 7, 13, 61}` (with `3^D | q` and a valuation-one prefix) also holds by brute force for `q ≤ 2000` (498 cases each, 0 violations), so the argument uses no property that the `3x+d` controls lack; nothing here excludes their actual cycles.
- The control `q = 39`: canonical, prefix `39, 59, 89`, `T^3(39) = 33`.

## What I did not check

- The completeness of the R25 inverse table (taken from that reviewed node).
- The SHA-256 pinning inside the legacy receipt, and the side-lane probe beyond its replay.
- §4 (original-rank scope), which cites R75 and R83 and makes no new claim.

## Findings

1. §1, "Before each next step `d ≤ D + a` this is at least 1": the ternary valuation of `λq` after `d` steps is `D + a − d`, which is `≥ 1` exactly when the next step is step `d + 1 ≤ D + a`. Right in substance; the index in the wording is off by one. Imprecision.
2. §2, negative-start lemma: stated in one compressed sentence (case analysis above). The lemma is true. Imprecision.
3. Statement 3: `H ≥ 3` is needed only for `q/3 ≡ 5 (mod 8)`; the clock theorem itself needs `H ≥ J + 1 ≥ 2`. Imprecision, harmless.
4. Statement 2 transfers verbatim to `3x+d` (checked for `d = 5, 7, 13, 61`); the node does not claim `d`-specificity, but readers should know the ordinary-clock barrier uses nothing special to `d = 1`. Remark.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
