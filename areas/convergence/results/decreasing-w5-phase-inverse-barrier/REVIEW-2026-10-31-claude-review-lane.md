# Review of decreasing-w5-phase-inverse-barrier

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node decreasing-w5-phase-inverse-barrier`: PASS, exit 0, 5 s reported by the tool (5.5 s wall). It replays `check_critical_inverse.py` against `critical_inverse_audit.json`, unchanged.
- **Independent re-derivation** with my own `S`, `ν`, `T = νS`, planner and brute-force divergence (scratch folder; no repository code imported):
  - Section 1, for all 11,111 odd `q ≡ 4 (mod 9)` below 200,000: `h = v₃(2q+1) ≥ 2`, `p = 2^h(2q+1)/3^h − 1` satisfies `0 < p < q`, the word is exactly `1^(h−1), 2`, `S^h(p) = q`, the negated path current has divergence `[q] − [p]`, and whenever `q` is canonical every state of the path is canonical; `(8q−5)/9` has word `(1, 2)`; `q = 31` gives `p = 27`. Derivation: `x_j = 2^(h−j)3^j C − 1` gives `3x_j + 1 = 2(2^(h−j−1)3^(j+1)C − 1)` with odd bracket for `j ≤ h−2`, and `3x_(h−1) + 1 = 2(3^h C − 1) = 4q`. Canonicity of the path: `x_j` (`j ≤ h−2`) is canonical iff `C ≢ 3^h (mod 4)`, and `x_(h−1) ≡ 1 (mod 4)` is canonical iff `C ≡ 3^(h−1) (mod 4)`, the same condition.
  - Section 2, for all 683 `w ∈ E` below 32,768: `q = ν(3w) = (3w−1)/2 ≡ 4 (mod 9)` is complementary; `u = w/3^(h−1) ≡ 3^(h−1) ≡ −3^h (mod 4)`, so `p = 2^h u − 1` is complementary canonical with `p mod 3 ∈ {0, 1}`; `v` is the critical inverse, `ν(3v) = p`, `3v ≤ 2^(h+1)u − 1` and `9v < 8w` ((4), using `2^(h+1)/3^h ≤ 8/9`); boundary (5) by brute-force divergence. Classification table: `h ≥ 3` gives `p ≡ 7 (mod 8)`, hence `p/3 ≡ 5 (mod 8)` and `(2p+1)/3 ≡ 5 (mod 16)`; `h = 2` gives `p = 4u − 1` with `u ≡ 3 (mod 4)`, hence `p/3 ≡ 9 (mod 16)` and `(2p+1)/3 ≡ 5 (mod 8)`; the three rows are `9 | w`, `w ≡ 6 (mod 9)`, `w ≡ 3 (mod 9)`.
  - `W5`-only absorption plans for all odd `s < 2048`: every request in `W5` and below `s` (a `W9` request `b` has `3b ≤ s`, its `W5` leaves are `≤ (9b+3)/4 ≤ (3s+3)/4`).
  - Full `E` plans: 455 descending (all leaves `< w`) and 228 self-dependent (coefficient of `w` exactly `+1`, all other leaves `< w`); `w = 21` gives the zero current and `{21: +1}`; `w = 21 + 2304j`, `j ∈ {0, 1, 2, 7, 31, 127}`, is returning with `v₂(3w+1) = 6`. The characterisation "`w ∈ E`, `w ≡ 3 (mod 9)` ⟺ `u ≡ 7 (mod 24)` and `9u` selected" was verified for `u < 20,000` and derived: `3u ≡ 5 (mod 8)` gives `d = v₂(9v−1) = 2 + v₂(3u−1) = 4`, `z₀ = (3u−1)/4`, `4z₀ + 1 = w`, and `6z₀ + 1 = (9u−1)/2` is the canonical half of `9u`, so `3z₀` is noncanonical.
  - Section 4: the inverse affine table re-derived from R25's inverse theorem (`(4F^k(b) − 1)/3 = (4^(k+1)(3b+1) − 7)/9`, `k ≡ 1 − b (mod 3)`, `k → k+3` is `p → 64p + 49`) and checked against brute force: for every canonical `y < 3000`, the canonical `p < 400,000` with `T(p) = y` are exactly the table's points. (8): `a_j − b_j = 64^j(a − b − 7/9) + 7/9`, the base rows having `a − b = 5/3, 13/3, 5/3, 13/3, 1, 15, 15`. (9), (10) and `G_i > 0` on 2000 random inverse words with ray indices up to 40; the branch legality uses `3^(D−i+1) | λ_(i−1)(q−1)`. Barrier by exhaustive search: 740 canonical `q < 6000` with `q ≡ 1 (mod 3^D)`, `D ≤ 4`: every `T`-predecessor within `D` steps exceeds `q`, the least is `(4q−1)/3`, and every predecessor `≤ 4q+3` lies on the spine `(4/3)^i(q−1) + 1`. The ordinary-predecessor corollary follows from `T^d(ν(p)) = ν(S^d(p))` and `ν(p) ≤ p`.
  - Section 5, `D ≤ 8`: `q ≡ 7 (mod 32)` is complementary with exponent 3, `v₃(q−1) = D`, `w = (2q+1)/3 ≡ 5 (mod 64)`, `ν(3w) = q`, `3 ∤ w`.
- **Controls** (`3x+d`, `d ∈ {5, 7, 13, 61}`; actual cycles from odd seeds, minima 5, 19, 23, 187, 347 for `d = 5`; 5 for `d = 7`; 13, 131, 211, 227, 251, 259, 283, 287, 319 for `d = 13`; 61, 235 for `d = 61`):
  - Ancestor analogue (replace 1 by `d`: `9 | 2q+d`, `p = 2^h(2q+d)/3^h − d`, same word): holds for all 11,111 / 11,111 / 11,110 / 11,108 such `q < 200,000` with `p > 0`. The least odd not reaching the orbit of 1 (3, 7, 13, 61) is never in the forbidden class (2, 1, 7, 1 mod 9).
  - Barrier analogue (ordinary predecessors; the shadow sits at the fixed point `d`, `q ≡ d (mod 3^D)`): for every cycle element `q > d` with `D = v₃(q−d) ≥ 1` (12, 0, 14, 13 elements), no odd `p ≤ q` reaches `q` within `D` steps. The sharpest case is the `3x+5` cycle `{23, 37, 29}`: `23 ≡ 5 = d (mod 9)` gives `D = 2`, and the cycle returns to 23 only at depth 3. The depth restriction is exactly what keeps the barrier consistent with an actual cycle; a version without it would be refuted by this cycle.

## What I did not check

- The components theorem of R25 and the bijection and equivalence of R37 beyond the finite checks above; their certificates were not re-run by me (other reviewers).
- The negative-cycle remark (`negative-cycle-backward-word`).
- The receipt's exploration counts other than those reproduced above (the replay reproduces them all).

## Findings

1. Section 5 (imprecision). "For `D ≥ 2` these have `w ≡ 1 (mod 3)` and lie outside `E`": for `D = 1` one gets `w ≡ 2 (mod 3)`, still `3 ∤ w`, so the family lies outside `E` at every `D`. Weaker than what holds; no consequence.
2. Statement item 2 (imprecision). "uses only `W5` indices below `s`" is proved for `s > 3` and is vacuous for `s ∈ {1, 3}`, which the proof says and the Statement does not.
3. Section 3 (typo-level). `d = v₂(9v−1) = 4` is asserted without its one-line reason (`3u ≡ 5 (mod 8)`), supplied above.
4. Chain (remark, not a defect). Depends on `critical-nine-elimination` (reviewed in this wave), `critical-tripling-domain-equivalence` and `elementary-bridge-quotient-normal-form` (status `written`).

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
