# Review of critical-nine-elimination

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node critical-nine-elimination`: PASS, exit 0, 17 s reported by the tool (18.3 s wall). It replays the legacy checker `check_w9_closure.py` (receipts `w9_closure_audit.json`, `w9_inputs.json`, `w9_current.csv` unchanged) and the side-lane probe `batch_r40_r41_check.py` (receipt byte-identical).
- **Independent re-derivation** with my own `S`, `ν`, selected/canonical test, bridge currents, R37 planner and brute-force divergence (script in my scratch folder; no repository code imported). Every displayed statement was re-derived and then tested:
  - (3): for `w ≡ 9 (mod 16)`, `9w+1 ≡ 2 (mod 16)` (valuation 1), `27w+5 = 248 + 432m ≡ 8 (mod 16)` (valuation 3, so 2 after the first halving), `3w+1 ≡ 12 (mod 16)` (valuation 2), `3(7+12m)+1 = 22+36m` (valuation 1); hence `S²(3w) = 3v−2`, `S²(w) = v`, `v = (9w+7)/8`, `v₂(v−1) = d−3`.
  - (4): `v ≡ 1 (mod 8)` gives `9v−5 ≡ 4` and `3v+1 ≡ 4 (mod 8)`, and `(9v−5)/4 = 3v'−2`. Since `v'−1 = 3(v−1)/4`, each iteration lowers `v₂(v−1)` by 2; after `k = (d−5)/2` resp. `(d−4)/2` iterations `v_k − 1 = (3/4)^k(9w−1)/8` equals `4z` resp. `2z` with `z = 3^k C`, so the endpoints are `(F(3z), F(z))` resp. `(6z+1, 2z+1)`.
  - `div E_z = [F(3z)] − [F(z)] − P(z)`, and (5), (7), (12): verified symbolically and by brute-force divergence for all 4096 `w ≡ 9 (mod 16)` below 65536 and for the 616 synthetic cases `4 ≤ d ≤ 80`. Branch counts 1344 / 1365 / 1365 / 22 and 11 / 154 / 304 / 147 reproduced; the maximum number of nonzero requests is 9.
  - Sharper tripling bound: for all odd `z < 8192`, every index of `I_(3z) ∪ I_z` is `≤ (3z+1)/2`, with the three cases as stated (2049 with `3z` noncanonical, 1024 with `3z ≡ 1 (mod 8)`, 1023 with `3z` complementary); the generic planner bound `u ≤ (2x+1)/3` and strictly decreasing requests for all odd `x < 20000`.
  - (6), (8), (9), (11) and the table: `u ≤ (3z+1)/2 ≤ (27w+29)/64 < w/2` for `w ≥ 9`; `C ≡ 2 (mod 3)`, `z ≥ 5`, `16z ≤ 9w−1`; `(3z+1)/2 ≤ (27w+13)/32 < w`; `u* < w ⟺ 36·3^k C + 9 < 2^(2k+4) C + 1`, bracket 52 at `k = 3`, next bracket `= 4·current + 36·3^k`; `(4z+3)/3 ≤ (9w+11)/12 < w`; `u*` equals `(9w+3)/4`, `(27w+13)/16`, `(81w+55)/64` at `k = 0, 1, 2` and exceeds `w` exactly there.
  - Section 4 recursion for all `w < 4096`: terminates, `W5` support, bound `(9w+3)/4`, exact divergence; at most 4 `W9` nodes and 6 `W5` inputs (receipt agrees). (13): `five_plan(9)` gives `{21: +1, 5: −1}`. (14): `five_plan(1561)` has no leaf, its `W9` nodes are 1561, 73, 41, 9, and its current is exactly `e_247 + e_4683 + e_5269 + e_7025 − e_659 − e_989 − e_1171 − e_1561 − e_1757`, with divergence exactly `P(1561)`.
  - Statement 2: "Collatz ⇒ currents" is the difference of two absorption paths. "Currents on `W5` ⇒ Collatz" is (1) plus R37's equivalence, whose two steps I re-derived: the strong induction with `div(J_w − N_(3w)) = [q] − [w]`, and the fact that a finite current with divergence `[x]` puts `x` and 1 in one component of the finite arrow graph (summing the divergence over a component avoiding 1 gives 0), so the forward orbits merge and `x` reaches 1.
- **Controls.** The identities are `3x+1`-specific (`W9` is chosen so that `3w ≡ 11 (mod 16)` is complementary). For `3x+5`, absorbing at its fixed point 1, the hypothesis of statement 2 fails as it must: 114 inputs `w ≡ 5 (mod 8)` below 2000 have `3w` and `w` in different cycle basins (first `w = 21`: `63` enters the cycle of 23, `21` the cycle of 19), so no finite `P(w)` current exists; `Collatz-5` is false (`3 → 7 → 13 → 11 → 19 → {19, 31, 49}`). The equivalence therefore does not transfer a false conclusion.

## What I did not check

- The certificates and proofs of `critical-tripling-domain-equivalence` (R37) and `elementary-bridge-quotient-normal-form` (R25) beyond the steps listed above; the components theorem of R25 is used through `ν`.
- The odd-`h` parameterization remark (R38) and the rank bounds of R43.
- Rejection paths of the legacy compiler beyond the four exercised by the replayed checker.

## Findings

1. Section 2, planner cases (imprecision). "If `q ≡ 1 (mod 8)` ... If `q ≡ 2 (mod 3)` ..." overlap on `q ≡ 17 (mod 24)`; the planner takes the first applicable case (as `critical_step` in `tripling.py` and the side lane's restatement do). Every bound holds under either choice; the text should say the cases are tried in order.
2. Statement item 3 (imprecision). "even `d` gives requests below `w` except one positive `W5` input `u* = 4z+1` when `3z` is noncanonical" reads as if the exception existed for every even `d`; by (11) `u* < w` for even `d ≥ 10`, so the exception is exactly `d ∈ {4, 6, 8}`, as the claim field and the table say. No mathematical consequence.
3. Section 3.2 (typo-level). "the first inverse step goes to `(4z+1)/3`" refers to the lower endpoint `2z+1` (which is `≡ 2 (mod 3)` when `k = 0`) without naming it.
4. Chain (remark, not a defect). Statement 2 rests on R37 (status `written`); this node's own argument is complete.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
