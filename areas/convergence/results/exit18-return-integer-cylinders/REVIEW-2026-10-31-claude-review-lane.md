# Review of exit18-return-integer-cylinders

## What I checked

- Certificate, from the repository root with `python3 tools/run_certificates.py --node exit18-return-integer-cylinders`: `check_legacy_replay.py` PASS (51 s; replays `check_integer_prefix.py` and `batch_r73_r74_check.py` unmodified); exit 0, 51.0 s wall. Re-run after my frontmatter edits: PASS (47 s). Because the History warns that R77's legacy checker pins this note's hash, I also ran `python3 tools/run_certificates.py --node same-seed-factor-complexity-bound` after the edit: PASS (7 s); `tools/legacy_replay.py` maps the legacy note to `null` and restores its bytes from git at `be73a66`, so this README is not what the pin sees.
- By hand. §1: each return domain is the unique solution of `a·w + c ≡ 2^e·b (mod 2^(e+26))` with odd `a`; both reduce to `b (mod 2^26)` (for `V` this is `Y(b) ≡ 0 (mod 2^26)`, the guard's definition; for `R`, `v₂(Y(w)) = 37 ≥ 26`); (1) from `Y(V(w)) = (A/M)·Y(w)` and `R = 2V²`; `V(w) ∈ G` iff `v₂(Y(w)) ≥ 45`, `R(w) ∈ G` iff `v₂(Y(w)) = 37` (since `B` is odd), so the domains are disjoint; (2) from `v₂(Y(w0)) = 19m + 18 = 19(m − 1) + 37`. §2: necessity; integrality of every prefix (the full numerator equals the prefix numerator times the odd suffix multiplier plus a multiple of the prefix denominator); the backward step through the two complete return domains, which lie in `G`; positivity forwards; CRT with any odd modulus. §3: the composition of common tails (`ℓ_(i+1) ≥ 12 > c_i`, so `S^(ℓ_i + c_i + j)(3w_i) = S^(c_i + j)(3w_(i+1))` with `j = ℓ_(i+1) + c_(i+1) − c_i` gives the induction), hence (6) and the quotient clock `ℓ`; the request bounds from R67's single-block bound and R70's (17). §4: `a > 2^e` for every nonempty word since `3^12 > 2^19` and `3^24 > 2^37`; (7), (8); the fixed point is the 2-adic limit because `F_ω` maps the cylinder of `ω^(n+1)` into that of `ω^n`. §5: `2^m` disjoint cylinders of densities `2^(−26−e)` sum to `2^(−26) s^m`; one floor error each gives (9); with `u = X/2^26` and `m = ⌈log_(2/s) u⌉`, `u·s^m ≤ u·u^(α−1) = u^α` and `2^m ≤ 2u^α`, which is (10).
- Own script in my scratch folder (`recheck_words.py`, 0.2 s; own `S`, `ν`, `T`): the domains 2218391138229 (mod `2^45`) and 8515171531530858421 (mod `2^63`) recomputed, both `≡ b (mod 2^26)`; (1) and the two valuation criteria on 50 random guard members; (2) for `m = 1..6`; (3), (4) and completeness on 303 random words (lengths 1–10, 40, 100, 256) with two lifts each (every state an integer in `G`, strictly increasing, endpoint `(aw + c)/2^e`; flipping any one bit in positions `26..26+e` breaks the word); the realised itineraries of 100 random guard members lie in their words' classes; (6) and `T^ℓ(3w0) = 3w_k` on all tested words of length at most 12; (7), (8) on 200 random cycle words with random prefixes (negative, odd denominators, equal to the 2-adic point of `ω^n` for `n = 1, 2, 3`, negative eventually periodic starts); disjointness of the `2^m` cylinders, the exact density and the counting error below `2^m` for `m = 1..6` at `X = 2^50, 3^40, 2^70`; `α = 0.0500` and `3(X/2^26)^α = 19.49` at `X = 2^80`.
- Controls: all eleven fixture cycles of [`baseline-obligation-transfer-controls`](../baseline-obligation-transfer-controls/README.md) have `2^A > 3^m` and positive rational point `d·C_w/(2^A − 3^m)` equal to their first state, whereas every return word has `3^ℓ > 2^e`: the sign obstruction (7) concerns growing words only and never touches an actual cycle. The R70 arithmetic this node rests on fails under `3x+5` and `3x+13` (my review of `mixed-exit-growing-reentry`).

## What I did not check

- The formal absorption plans `H_x` and the helper bound `(9s + 5)/8` ([`critical-image-rank-composition`](../critical-image-rank-composition/README.md)); the request vectors in (5) are checked only in their algebra.
- The legacy constructor's signed current tables beyond the replay's exit 0.
- Bernstein and Lagarias (context only, not a premise).

## Findings

1. §5 (imprecision): `α` is left symbolic; since `2/s = 2^20/(1 + 2^(−18))`, `α = 0.0500` to four places, so the survivor bound is about `3(X/2^26)^(1/20)`, i.e. 19.5 at `X = 2^80`.
2. History (stale warning): "editing it makes that checker fail" no longer applies; the B18 replay restores the legacy note from git, and R77's certificate passes after this review's edits (see above).
3. §1 (imprecision): a `V` symbol is one R67 block whose output is still guarded, which forces `v₂(Y(w)) ≥ 45`, i.e. at least two further guarded copies; the table says "consumed precision 19" but not that `V` is never a maximal block. Consistent with (2), but worth stating.
4. Proof text (typo): spaces lost before numerals in the migrated legacy text.

## Verdict

HOLDS. The return domains, the complete-cylinder theorem, the composed clocks, the negative periodic points and the density and survivor bounds all re-derive and recompute; the scope (odd-only clock, absorbing at 1, the two named returns to the named guard, finite words, no claim that a survivor is excluded) is exactly what is proved.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
