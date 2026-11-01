# Review of short-delay-all-phase-obstruction

## What I checked

- Certificate [`check_legacy_replay.py`](check_legacy_replay.py) via `python3 tools/run_certificates.py --node short-delay-all-phase-obstruction`: PASS, exit 0, 6.5 s wall (the node says about 13 s).
- Notation against [`delayed-release-cancellation`](../delayed-release-cancellation/README.md) and [`depth-32-aggregate-exposure-obstruction`](../depth-32-aggregate-exposure-obstruction/README.md): `N = 3X/128`, `y_1 = 3X/2 − 1 = 64N − 1`, `y_2 = 96N − 1`, `y_3 = 144N − 1`; with `2^10 | X` and `X ≡ 1 (mod 3)` their residues mod 18 are 5, 17, 17 in bands 4, 5, 5, so the coefficients are `(−2, +2, +2)`.
- The exceptional classes from (4). `4^(h+1)U + 2 ≡ 0 (mod 3^(h+1))` has the unique solutions `U ≡ 16 (mod 27)` for `h = 2` (`10U ≡ 25`, `10^(−1) = 19`) and `U ≡ 31 (mod 81)` for `h = 3` (`13U ≡ 79`, `13^(−1) = 25`). Unit classes 18 and 54, hence 17/18 and 53/54, and 70 isolated classes.
- The attachment argument. `v = 2^h(4^(h+1)U + 2)/3^h − 1 = λX − c` with `λ = 4(8/9)^h`, `c = λ + 1 − 2(2/3)^h` (expanded with `X = 1 + 3^h U`): `λ = 256/81, c = 265/81` and `λ = 2048/729, c = 2345/729`; `y_2 < v < y_3` as soon as `X > 1472/139` resp. `X > 12928/3299`; `v` is odd and `≡ 2 (mod 3)`; the top-band coefficients at residues 5, 11, 17 are −1, −1, +2. Reversing from `y_1`: valuation 3 gives `4X − 3`; `h` inverse valuations 2 give `1 + 4^(i+1)·3^(h−i)·U`, ending at `4^(h+1)U + 1 = m − 1` with `m = 4^(h+1)U + 2 ≡ 0 (mod 3^(h+1))`; `h` inverse valuations 1 give `2^i m/3^i − 1`, ending at `v`. The forward valuations are exactly `(1^h, 2^h, 3)`, so the length-`D` path from the source `v` is exposed in `G_D` and the component is not the path.
- The translation argument of section 3. With `B = 2^max(D+4,10)`, `M = 3^K`, `T = BM`, the base `X_0 ∈ [T, 2T)` carries the symbolic lift; for `X = X_0 + jT` and `q = X/X_0` each registered state is `a + b + jΔ`, `Δ = aT/X_0`. Since the slopes are `X_0` times rationals with denominators at most `3^4` (`h = 2`) and `3^6` (`h = 3`), below `3^K`, `Δ` is an integer divisible by 6; this keeps oddness and the residue mod 3, the band is fixed by the affine inequalities, and equal coefficients at the three residues `a + b + jΔ (mod 18)` fix the coefficient, so the decision tree at `X_0` is reused verbatim. `B` and `M` coprime put every admissible `X ≥ 2T` in exactly one progression; the thresholds `2·2^10·3^5 = 497664` and `2·2^11·3^7 = 8957952` follow. I read `check_coverage.py`: `verify_additive_phase` checks exactly these facts for every chain and query row.
- The ladder. `X = 2^(24+162t)` gives `N = 3X/128 = 96·64^(2+27t)`; `v_3(X − 1) = 1 + v_3(12 + 81t) = 2`; the order of 2 mod 243 is 162, so `q = 2^(162t) ≡ 1 (mod 243)` and the lift at `N_0 = 393216` (receipt `K = 5`, 28 queries, 135 comparisons, 8 vertices) applies; `U ≡ 1 (mod 27) ≠ 16`.
- Coverage. Formula (2) of `delayed-release-cancellation` with `r = h` gives `U ≡ 70, 313 (mod 729)` for `h = 2` and `U ≡ 274, 1732 (mod 2187)` for `h = 3`: two of `2·3^(r+3)` unit classes, fraction `1/3^(r+3)`; the two classes differ by `4^(−h−1)·3^r·2^(−r)·108`, of ternary valuation `r + 3`. The scan table (459/17/10 and 1431/16/11; 10 + 11 = 21 certificates; 486 + 1458 = 1944 representatives) matches the receipt.
- Independent recomputation (`recompute_phases.py` with my own oracle, written from the definitions, in the review lane's scratch folder). For each of the 70 isolated classes the component of `y_3` at the members `j = 0, 1, 5, 23` of its progression (280 runs; the certificate uses `j = 0, 1, 2`) is exactly the path `y_1 → ⋯ → y_(D+3)` with sources `(−2, +2, +2)`. For the two exceptional classes at the same four members, `v` is a source of the component, the word `(1^h, 2^h, 3)` from `v` ends at `y_1`, and the component has more than three sources. The ladder members `t = 0, 1, 2` (`X = 2^24, 2^186, 2^348`) each give the 8-vertex path of mass 2 with 28 decisions; the certificate checks `t ≥ 1` only symbolically.
- Probe (not part of the claim). All 34 values `X < 2T` with `2^10 | X`, `v_3(X − 1) = 2`, `U ≢ 16 (mod 27)` also give the path.
- Controls. The claim is a finite statement about exposure graphs of the `3x+1` annulus, true or false independently of Collatz; no actual `3x+d` cycle bears on it and no `d`-uniformity is claimed. Not applicable.

## What I did not check

- The 70 symbolic traces beyond the certificate's regeneration and my numerical members; I did not re-derive the receipt hashes.
- The 21 partial-current certificates row by row (counts only).
- `family_parameters` of `delayed-release-cancellation` beyond formula (2) (that node was reviewed separately).

## Findings

1. (imprecision) The thresholds `X ≥ 497664` and `X ≥ 8957952` are `2T`; the proof's own argument already places every admissible `X ≥ T` in a progression (the only smaller member of the residue class is `X_0 − T < T`), and the probe found no failure below `T` either. The stated bound is sufficient, as claimed; no change.
2. (remark) The exceptional-class representatives in the receipt (`X = 409600` for `h = 2`, `X = 6400000` for `h = 3`) lie below the stated thresholds. The attachment inequality `y_2 < v < y_3` holds there too (it needs only `X > 11`, resp. `X > 4`), so the checks are valid, but they are not instances of the theorem as stated. Their component masses (0, 1, 29 for the three `h = 2` representatives) show how different the exceptional components are, consistent with the node's refusal to say more than "a further source attaches".
3. (typo, not changed) Legacy table cells and lines read `modulo27`, `modulo81`, `modulo243` (lost spaces); readable.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
