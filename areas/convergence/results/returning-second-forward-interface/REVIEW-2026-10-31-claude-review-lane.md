# Review of returning-second-forward-interface

Independent review of [`README.md`](README.md) (legacy R52; authors: ChatGPT main lane, Codex). Inputs are taken from the `reviewed` nodes [`returning-forward-interface`](../returning-forward-interface/README.md) (the row, the word `1^(a−2), 2`, the endpoint table `B`), [`complementary-run-bridges`](../complementary-run-bridges/README.md) (the run bridge), [`critical-image-rank-composition`](../critical-image-rank-composition/README.md) (`ρ`, the bound `(9s+5)/8`) and [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (`ν`, `T`). Every number below comes from my own implementation (kept outside the repository) or from the proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node returning-second-forward-interface`: PASS, exit 0, 13.3 s wall (legacy replay of `check_returning_continuation.py`, receipt byte-identical).
- **Section 1 (interface (2)).** Telescoping: `([3w] − [q]) + ([q] − [r]) + ([r] − [n]) + ([n] − [f]) − ([w] − [z]) + ([f] − ΣA_f P) − ([z] − ΣA_z P) = P(w) − Σ(A_f − A_z)P`. Lower requests: `8ρ(u) ≤ 9z + 5 ≤ (9w+11)/4 < 4(3w−1) = 8q` because `39w > 27`. Quotient clock: `T^(a−1)(q) = ν(S^(a−1)q) = ν(r) = n`; then `T(n) = ν(f)` when `n ≡ 1 (mod 8)`, and `T^(A+⌊d/2⌋−1)(n) = ν(f)` for the run bridge (odd `d` ends at `4f+1`, `ν(4f+1) = ν(f)`). Machine check on all 910 returning inputs below 131,072: exact divergence (below `2^16`), every accepted plan has only `W5` requests with `ρ < q`, the ordinary clocks and the summed quotient clock; the seven (status, first test, second block) categories equal the receipt's (313, 168, 63, 121, 23, 85, 137); 184 inputs fail the first test and pass the second, 23 pass the first and fail the second (first examples 1605, 3261, 4629).
- **Section 2.** At `a = 3`: `t ≡ 3^3 (mod 4)` and `8t ≡ 10 (mod 27)` give `t ≡ 35 (mod 108)`; `2r + 1 = 9t` turns `t ≡ 8 (mod 27)` into `r ≡ 71·2^(−1) ≡ 157 (mod 243)` (the binary condition is just "`r` odd"). Complementary canonical `r ≡ 4 (mod 9)` has `B(r) = r > q = (8r−5)/9`, and the two other endpoint classes pass by R44's `a = 3` subdomain theorem, so R44 fails at `a = 3` exactly for complementary canonical `r`. Checked on all 113 such inputs below 131,072 and, conversely, on all 205 complementary canonical `r ≡ 157 (mod 243)` below 400,000 (`t = (2r+1)/9`, `w = (16r−1)/27` is returning with `a = 3`).
- **Section 3.** With `q = (2^(A+3)v − 13)/9`: the odd-`d` differences (4) re-derived as `((2^(A+9) − 3^(A+4))v − 949)/576`, giving 1319, 1909, 1631; the even-`d` nonselected differences `q − f` at `(A,d) = (2,2), (2,4), (3,6), (3,8), (4,8), (4,10)`; the selected generic differences (5) at `(2,2), (3,4), (4,6)`; the nine boundary differences (6) at `(3,2), (4,4), (4,2)` for `m ≡ 1, 3, 7 (mod 8)` (`m` canonical with `3 | m`: `m ≡ 3 (mod 8)` is `m/3 ∈ W9`, `m ≡ 7` is `m/3 ∈ W5`). All agree with the displayed expressions; monotonicity `f_(d+2) = 3(f_d − 1)/4 + 1` extends them. Machine check: the table equals the direct test `B(ν(f)) < q` on all 99 low-exponent inputs below 131,072 and on 1,152 members of my own CRT cells (`a = 3`, `A = 2, 3, 4`, `d = 2..17`, 24 indices each); every boundary case of (6) occurs (for example `(4,4)` selected with `m ≡ 7`: 3 members, rejected; `(3,2)` selected with `m ≡ 7`: 2 members, accepted).
- **Section 4.** In (8) the first congruence is `t ≡ 10·2^(−a) (mod 27)` with `v3(2r+1) = a − 1` exactly, and the second is `v2(3^(A−1)v − 1) = d`, giving `v ≡ 3^(A−1) ≡ −3^A (mod 4)`. `r ≡ 4 (mod 9)`, so `B(r) = r`; `q = c(2r+1) − 1 < r` because `2c − 1 < 0`; `q > cr` because `r + 1 > (3/2)^(a−1)`; `f < L(r+1) ≤ 4Lr/3`; (7) is `7L/3 ≤ c`; chain (10). Checked on 96 family members (`a = 3..12, 16, 32`; `A = 2, 3, 4, 8`; two indices), including the `w`-period `9·2^(a+A+d+2)`. R46 at the original `q`: `q ≡ 4 (mod 27)`, `D = 1`, `j = v3(2w) = 1` on every returning input, so its `j ≥ 2` predicate fails.
- **Receipt.** 910 inputs, 184 and 23, 99 low-exponent cases, 768 cells, 132 families, tables of 66, 46 and 58 rows: as Section 5 states.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3). The identities are `d`-uniform: for `3x+5` and `3x+13` the first run `1^(a−1), 2` of a complementary climber `x = 2^a t − d`, the run bridge and the R46 undo hold on all 8,192 complementary climbers below `2^16` for each `d`, and the actual cycles pass through them (`3x+5`: `23 → 23`; the 17-cycles contain complementary states whose endpoints lie on the cycle). The rank test and the table are specific to `3x+1` and conditional, so no control applies.

## What I did not check

- The domains of R45, R47 and R50; "outside all seven earlier direct domains" was verified by hand for R41 (`w ≡ 3 (mod 9)` is the returning row, outside `E_good`), R44, R46 and R48 (`3w` selected) only, and taken from the dispatcher nodes for the other three nonselected rules.
- The legacy module `returning_continuation.py` line by line.
- Universal coverage, open by the node's own statement.

## Findings

1. **Section 2 (imprecision).** "All `r` in (3) exceed or equal 157": 157 itself is `5 (mod 8)`, so not canonical; the least member of (3) is `r = 2587` (`w = 1533`). The consequence used, `v ≥ 11`, stays valid. No change.
2. **Section 1 (imprecision).** For the block "`n ≡ 1 (mod 8)`, quotient length 1", the ordinary arrow reaches `f = (3n+1)/4`, which need not be canonical; the quotient step reaches `ν(f)`, which is what the test `B(ν(f)) < q` uses. No change.
3. **Certificates (imprecision).** The only certificate replays an assert-based legacy checker without `-O`; disclosed in the node.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
