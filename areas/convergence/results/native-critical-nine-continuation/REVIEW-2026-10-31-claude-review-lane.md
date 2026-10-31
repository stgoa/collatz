# Review of native-critical-nine-continuation

Independent review (Claude review lane, Fable 5.1), 2026-10-31. Notation as in the node; the plans `J_s`, `A_s` are the unexpanded critical plans of R75 (requests in `W5 ∪ W9`, ranks `≤ ν(s)`), `(L_c, l_c)` the R40 local plan without recursive W9 elimination. All recomputations use the review lane's own `S`, `ν`, `ρ`, currents and plans (`revlib.py`, checked against brute force), in `native_interface.py` and `d6_section.py`.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node native-critical-nine-continuation`: PASS, exit 0, 21 s wall (legacy `check_native_nine.py` and the side-lane probe `batch_r78_r80_check.py`). The receipt's counts equal the evidence string (383, 226, 150, 134, 30, 13, 16 other-A cases, 36 sources; outputs of 43/97/102 rows from 3/8/6 inputs).
- **Section 1, the lemma.** By hand: odd `D` gives ranks at most `3z ≤ (9M−3)/32`; even `D` with canonical `3z` at most `3z ≤ (9M−3)/16`; even `D` with noncanonical `3z` the single request `4z+1` of rank `6z+1`, equal to `(9M+5)/8`, `(27M+23)/32`, `(81M+101)/128` at `D = 4, 6, 8`, with `D → D+2` sending `L` to `(3L+1)/4`. On all 512 W9 `c < 2^13`: no violation of `ρ(v) ≤ (27M+23)/32` outside `D = 4` with noncanonical `3z`, 31 equality cases.
- **Section 2, the interface.** By hand from `t ≡ 191 (mod 1728)`: `3n+1 = 2(64t−5)/3`, then `16t−1 = q`, `24t−1`, `36t−1`, `54t−1`, and `2(81t−1) = 4r` with `r` odd because `t ≡ 3 (mod 4)`, so the word is `(1,2,1,1,1,2)`; `81t + 1 = 16(319 + 324j)` for `t = 63 + 64j` makes `r` selected with `ν(r) = (r−1)/2 = m = 3c`; `c ≡ 9 (mod 16)` and `u = (32t−1)/3 ∈ E` with `ρ(u) = q`. Checked on the first 200 members and on 44 members of the exact-depth cells (21) (`D = 4..24, 40, 64`): word, endpoint, selection, `ν(r) = m`, `b < c < n < m`, 35 distinct `(D, canonical 3z)` branches. Converse: among 4000 values `t ≡ 83 (mod 108)`, "`r` selected with `ν(r) = 3c'`, `c' ∈ W9`" holds exactly when `t ≡ 63 (mod 64)` (0 mismatches), because `27t ≡ 37 (mod 64)` iff `t ≡ 63`.
- **Plan (5) and decision (6).** Boundary `P(b) − Σ a_b P` re-verified with my divergence on all 244 members; the full vector has every rank below `n` exactly when not (`D ∈ {4, 6}` and `3z` noncanonical), and each failure has exactly one request above `n`, namely `4z+1` with coefficient `+1`. The five differences (7), (8) are exact rational identities (checked at three values of `t`, degree one) with the displayed signs at `t = 191`. The D4 return (9): `4z+1 ∈ E`, `(4(4z+1) − 3)/9 = c = (729b+223)/512`, `ρ(c) = m > n` (50 cases).
- **Section 3 (179 D6 members: cells (22) for `d = 2..20, 40, 64` and the residue `58249 (mod 65536)` with selected `3p`).** `p = 4z+1 = (729t+25)/64 = (19683b+12677)/8192`, `Q = 6z+1 = (2187t+11)/128 = (59049b+29839)/16384`, `ρ(p) = Q > n`, `p ≡ 2176 (mod 19683)`, `c = (16p−13)/27 ≡ 2 (mod 3)`, `v3(4c+1) = 3`, `v3(8c+1) = 0`, `b ≡ 58249 (mod 65536)`. The `k = 4` word `(1,1,1,2,1,1,4)` from `q = 16t−1` reaches `Q`, `2048(Q+17) = 2187(q+17)`, and the four-arrow `q → r` prefix plus `N_r` plus the three-arrow `(1,2,2)` prefix `m → Q` equals the seven-arrow path row for row. Plan (14) has the unique request above `n` at `u` with `+1`. Substituting it into (5) and converting `P(u)` through R75's returning identity (`(4u−3)/9 = b`) gives exactly `K = J_c − L − J_ℓ`, `ℓ = (Q+2)/3 = (27c+29)/32`, with requests `{b: 1} + A_c − A_ℓ`, and `K ≠ 0` on all 179 members. The `k = 8` endpoint `16c+1` normalises to `m` and leaves `c` with `+1`.
- **Section 4.** Plan (17) re-assembled from my run bridge at `Q` and checked equal to `G_9 + D_Q + J_f − L + J_c − J_ℓ − J_b` with vector `A_f + A_c − A_ℓ − A_b` on all 179 members (103 with `A = 2`). On `A = 2` the vector is strict exactly when `d` is odd, or even `d ≥ 6`, or `f` selected; the 26 failures (`d = 2, 4`, canonical `f`) have the single leader `(2f+1)/3` of rank `f > n`. The endpoint formulas `(9Q−3)/32`, `(9Q−3)/16`, `(9Q+5)/8`, `(27Q+23)/32`, `(81Q+101)/128` follow from R26 with `s = (Q+1)/4`; the five identities (19) are exact with the displayed signs at `Q = 209935`. Clocks (20) verified by iterating `S`.
- **Section 5.** Cells (21) give exact `D` with `b`-period `2^(D+10)`; cells (22) give `A = 2`, exact next depth `d`, selected `3p`, `b`-period `2^(d+17)`; `32788 ≡ (11 + 2·2187)·128^(−1) (mod 59049)`. `b = 58249` has canonical `3z`, so it is outside the guarded domain, and gives `Q = 209935`. At `b = 4187017`: `p = 10060189`, `Q = 15090283`, `(A, d) = (2, 4)`, `f = 12732427` canonical, `n = 12561051 < f < Q`.
- **Controls.** Under `3x+5` and `3x+13`, none of the first 200 members has first six valuations `(1,2,1,1,1,2)`; the interface is `3x+1` arithmetic and the node excludes no control cycle.

## What I did not check

- "The successful rows were already implicit in R52" ([`returning-second-forward-interface`](../returning-second-forward-interface/README.md), `written`): not re-derived; nothing in the decisions depends on it.
- The legacy module's `one_step` and `compile_plan` beyond the replayed receipt.
- Other `A` (the node leaves them unclassified; 76 of my 179 members have `A ≥ 3`).

## Findings

1. (imprecision) Section 3: "It implies the valid lower bound `Q ≥ 209935`". The bound comes from the residue class alone (`b = 58249` gives `Q = 209935` exactly) and is valid, but that member has canonical `3z`; the least `Q` among the 179 guarded members I built is 918523. All later sign statements only need `Q ≥ 209935`.
2. (imprecision) Section 2, "Relation to existing successful rules": the comparison with R44 and R52 is narrative and rests on a `written` node; it is not used by (6), (15) or (18).
3. (typo-level) Section 1 writes the odd-`D` endpoint pair as `(3z, z)` after the sibling currents of R40 are added; the text omits that step (R40 §3.1), which the implementation performs.

## Verdict

HOLDS. The lemma, the whole native interface and its converse, the decision (6), both D6 inverse alternatives with the exact row-for-row identities, the complete `A = 2` decision and the CRT cells were re-derived by hand and reproduced with independent code; the certificate passes. No correction to the text.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
