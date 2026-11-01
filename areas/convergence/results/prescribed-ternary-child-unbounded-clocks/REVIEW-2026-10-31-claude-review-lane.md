# Review of prescribed-ternary-child-unbounded-clocks

Independent review (Claude review lane, Fable 5.1; directed by Santiago Armstrong). Scratch code: own exact rational Syracuse map, own cylinder constructor and integer replay; the receipt was compared with only at the end.

## What I checked

- **Certificate** (`python3 tools/run_certificates.py --node prescribed-ternary-child-unbounded-clocks`): `check_legacy_replay.py` PASS (8 s); exit 0, wall time 7.71 s (replays `r93_r94_check.py` and `check_child_catalogue_scope.py`, receipts byte-identical).
- **Centres (section 2).** `D = 3^12 − 2^19 = 7153`; `v* = −B/D` is the fixed point of `Φ`; `q* = (2^27 v* − 213949807)/3^17 = −515908491727/11404192419` with `11404192419 = 7153·3^13`; the cell identity `Q(ℓ) = (2^27 v0(ℓ) − 213949807)/3^17` holds as an affine identity (constant and slope); `ℓ* = −22852975802/34212577257`, `v2(ℓ*) = 1`, `v2(q* − Q0) = 46`; `j*_c = (ℓ* − c)/3` are negative binary-integral rationals with `Q(c + 3j*_c) = q*`; the three child centres equal the table, `p*_0, p*_1 > 0 > p*_2`.
- **Upper shadow (section 3).** 18 exact arrows from `q*` reach `6v* + 1 = −1792529/7153`; the word `(1,1,1,1,3,1,4,1,2,1,1,2)` (cost 19) returns to it; every state is negative. The orbit first repeats at step 28, equal to the state at step 16, so the shadow consists of 28 distinct states (16 preperiodic, 12 periodic); see Finding 1.
- **Third child.** From `p*_2` exactly 112 exact arrows (cost 227) reach `1663/7153 > 0`; all 112 earlier states are negative, none equals an upper state, the largest numerator has 80 bits. The children `p*_0`, `p*_1` stay positive (200 arrows checked; positivity is preserved by the map). Hence (3).
- **Sections 4–5, re-derived.** A word of cost `E` is one class modulo `2^(E+1)`; the slopes `3·QP` and `QP` have exact binary order 45, so `j ≡ j*_c (mod 2^N)` with `N + 45 ≥ E_max + 1` transfers both words; the endpoints (5) are affine in `j`; equality at `j*_c` would contradict (3), so no equation is identically zero; the nonnegative integer roots are excluded by (6). (7): `Dv0 + B = D·2^18·3^19 (j − j*_c)`, checked exactly, so `N ≥ 19R` gives `v2(L(v0)) ≥ 19R + 18` and, by R90's countdown, at least `R` complete re-entries.
- **Independent cylinder construction** for all 39 pairs `(c, K, R)` of the receipt: my bits, residue, modulus, nonnegative integer roots and both words coincide with `child_history_audit.json` in every case (e.g. `K = 128`: 216/207/213 bits for `c = 0, 1, 2`; `K = 16, R = 128`: 2432 bits). For each cylinder, five positive members `j` (shifts 0, 1, 2, 3, 11): `0 < j < ℓ`, `Q(j) < Q(ℓ)`, integer orbits follow the shadow words, no common state at clocks `≤ K` (195 pairs), `v2(Dv0 + B) ≥ 19R + 18`, and the number of complete `Φ` re-entries counted directly (`v ↦ (Av + B)/M` while `2^19 | L(v)`) is at least `R` for `R = 1, 4, 16, 128`.
- **Section 6.** `Q(2 + 3·(−1)) = Q(−1) = Q0 − QP < 0` as stated; the slope argument `3^(a+1) 2^B = 3^b 2^A ⇒ b = a+1, A = B` re-derived.
- **Controls.** The theorem excludes bounded clocks for one child rule on explicit `3x+1` integer families; it asserts nothing about cycles, so the `3x+d` fixtures do not bear on it.

## What I did not check

- R90's countdown theorem itself (a dependency); I counted re-entries directly instead.
- The internals of the legacy module beyond the replay; cylinders beyond `K = 128` and `R = 128` (the written argument covers them).

## Findings

1. Proof section 3 (and the side lane's "31 states"): the "18-arrow prefix" to `6v* + 1` enters the 12-cycle already at step 16; the shadow has 28 distinct states, not 30 or 31. Every statement made (the prefix reaches `6v*+1`, the cycle returns, all states negative, the child path is disjoint from all of them) remains true. Severity: imprecision.
2. Section 4, "N + 45 ≥ E_max + 1": the implementation uses exactly this and the receipt confirms it; the extra bit is needed because a word of cost `E` fixes the source modulo `2^(E+1)`. Severity: none (recorded).
3. Claim, "infinite positive binary progression": the cylinders for `(c, K) = (1, K ≤ 16)` and `(2, K ≤ 16)` have modulus 1 (bits 0), i.e. every positive `j` avoids a merger within 16 clocks; the claim's wording covers this degenerate case. Severity: none.

## Verdict

HOLDS. Centres, shadows, the 112-word certificate, the cylinder construction and the return-count transfer re-derive and recompute independently, and the claim's scope (bounded clocks for this child only; nothing against input-dependent clocks, other children or general currents) is what the proof delivers.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
