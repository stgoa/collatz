# Review of growing-prefix-unhandled-leading-input

Independent review of [`README.md`](README.md) (legacy R54; authors: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, 1 absorbing, `ν`, `T = νS`, `ρ(w) = ν(3w)`, the seven direct rules of [`two-inverse-phases-intermediate-increase`](../two-inverse-phases-intermediate-increase/README.md), the deterministic plan `H` of [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md) with the `W9` elimination of [`critical-nine-elimination`](../critical-nine-elimination/README.md), bounds of [`critical-image-rank-composition`](../critical-image-rank-composition/README.md). All numbers come from my own implementation (written from the node texts, not from the legacy libraries) or from the node's proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node growing-prefix-unhandled-leading-input`: PASS, exit 0, 4.75 s wall. It replays `check_rule_avoidance.py` unmodified with its receipt unchanged.
- **§1, the phase.** For the first 4,000 members `w ≡ 3445 (mod 3456)`: `w ∈ W5`; `3w + 1 ≡ 32·323 (mod 2^7·81)`, so `v2(3w+1) = 5` and `t ≡ 3 ≡ 3^5 (mod 4)`, `3w` selected; `w ≡ 1 (mod 3)`; `q = ρ(w) = (3w−1)/2 ≡ −17 (mod 5184)`, complementary with `v2(q+1) = 4`; `D = v3(q−1) = 2`, `u = −2 + 9h`, `j = v3(16u+2) = v3(6(24h−5)) = 1`. All seven rules fail by my own predicates (R41/R44 need `3 | w`, R45/R47/R48/R50 need nonselected `3w`, R46 needs `j ≥ 2`), the domains of R51, R52 and R53 fail, and `σ(w) = ρ(w)`. Conversely `q ≡ −17 (mod 5184)` gives `w = (2q+1)/3 ≡ 3445 (mod 3456)`.
- **§2, the table.** Re-derived the seven rows from the valuations `(1,1,1,2,1,2,2)` with the selected halving after the fourth arrow (`y = (81q+65)/32`, `v2(y+1) = 3`, unit `≡ 3 (mod 4)`, `(y−1)/2 = (81q+33)/64`), and `Ψ(q) + 17 = 2187(q+17)/2048` (`2187·17 = 37179`). Checked on 300 random `q ≡ −17 (mod 2^17)` up to `2^57`: every row, every valuation, canonicity and positivity of each state, `T^i(q)` by my own `T`, the labels `(4,2)` and `(2,4)`, the prefix current with divergence `[q] − [Ψ(q)]`. The modulus is sharp: sampling the classes `−17 (mod 2^k)` for `k = 10, …, 16` always finds a failure, `k = 17` none.
- **§3.** For `r ≤ 8` and `s ∈ {1, 2, 3, 7, 101}`: (5), every noninitial state `> q_0`, each cycle start `≡ −17 (mod 81)`, canonical endpoint with `v2 = 4`, and the full prefix current. Rows 0 and 7 are critical `W5` indices and row 4 is `W9` exactly under the ternary condition `q ≡ −17 (mod 81)` (see finding 1).
- **§4.** On 40 random family `q`: `v = (27q+11)/64 ∈ W9`, `v2(9v−1) = 6`, R40 endpoints `(Ψ(q), ℓ)` with `ℓ = (729q+2153)/2048` and `Ψ(q) = 3ℓ − 2`, `3z` noncanonical, my full `W9` elimination of `P(v)` has coefficient `+1` at `w' = (2Ψ(q)+1)/3` and every other request of rank `< Ψ(q)`; the bounds `(3q'+4)/4` on `H_(w')`, `(9ℓ+5)/8 = (3q'+11)/8` on `H_ℓ`, and `(9v+5)/8 = (243q+419)/512 < q'` (7) hold; `q < q' < T^4(q)`. Also `Ψ(q) ≡ 1 (mod 3)` for every `q` in the 2-adic class, so `w'` is always defined.
- **§5, (9).** For `r ≤ 3`, `s ∈ {1, 2}` and every `n ≤ 7r` (90 positions) I built `J_n` of (8) with my own currents: `div J_n = P(w_0) − Σ(A_x − A_z)P` exactly; the request of (9) has coefficient `+1`, rank `≥ q_0`, is the unique maximum in `ρ` and in `σ` (`σ = ρ` on the lead, which is not returning), has selected `3w` and `w ≡ 1 (mod 3)`, and every recognizer (seven rules, R51, R52, R53 domains) fails on it; `H_z` has ranks `< q_0` since `4z ≤ w_0 − 1`. The three stored unfinished currents of the receipt (`r = 1`, `s = 1`, `n = 0, 3, 7`, seed 7077877, leads 7077877, 7558261, 7558261) are identical to mine, rows and coefficients. The whole-cycle comparison (10) on 20 random family `q`: boundary exact, `w'` at `+1`, all auxiliary ranks `< q`, and `3q' + 4 < 4q ⇔ 1631q > 15281`.
- **§6.** R48's undo (12) `D = d/2`, `j = a − 1`, `p = q` on all 1,365 even canonical blocks with `w < 2^16`; `27 → 31 → 91` has labels `(2,2)`, `(5,4)`, and R46 accepts `w = 61` (`q = 91`, `D = 2`, `j = 4`, `p = 31`, `2^8 < 3^6`).
- **§7.** Domain predicates of R51 (returning or nonselected), R52 (returning), R53 (nonselected) fail on every lead.
- **Remark.** `T` extended to negative odd integers has exactly the cycles `{−1}`, `{−5, −7}`, `{−17, −25, −37, −55, −21, −31, −23}` on `|x| ≤ 4000`.
- **Receipt.** 256 phase cases, 48 families, 148 lookahead positions, 20 `W9` plans, 8 repeated signed plans, two auxiliary expansions (`ρ` and `σ`, 29 nodes each), 6 rejections, as the node says.
- **Controls.** The seven-row table is `d`-homogeneous: with `ν_d`, `T_d` it holds for `d = 5, 13` on 200 random `q ≡ −17d (mod 2^17)` each. The result is a scoped obstruction to a named procedure with retained premises; it excludes no orbit, so the actual cycles of `3x+5`, `3x+13` (all members below `2^17`, hence outside the class) are not touched.

## What I did not check

- The seven rules' code paths in `expanded_union.py`; I implemented each rule's domain and acceptance test from its node's statement.
- The later rules R55–R57 said to resolve parts of the phase.
- The side-lane probe `batch_r51_r54_check.py` (not re-run).

## Findings

1. **§2 versus §3 (imprecision).** The table is stated for every `q ≡ −17 (mod 2^17)`, a class that does not fix `q mod 3` (all three residues occur). Rows 0 and 7 are critical `W5` indices only under the ternary condition `q ≡ −17 (mod 81)`, which the phase (1) and the family (4) satisfy; row 4 is `W9` and `Ψ(q) ≡ 1 (mod 3)` unconditionally. The text places the `W5` reading in §3, so nothing is wrong; a reader applying §2 alone should know this.
2. **§2 (imprecision).** `2^17` is exactly the modulus needed for the seven-row table (it fails on the class modulo `2^16`); the text does not say whether it is sharp. No change.
3. **Statement 3 (imprecision).** "R52 and R53 do not apply at the lead" is a domain statement (R52 needs `w ≡ 3 (mod 9)`, R53 nonselected `3w`), as §7 says; the claim field's "(and with R52, R53)" should be read that way. No change.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
