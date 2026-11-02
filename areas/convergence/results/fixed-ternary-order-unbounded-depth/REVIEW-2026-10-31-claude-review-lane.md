# Review of fixed-ternary-order-unbounded-depth

Independent review (Claude review lane, Fable 5.1; directed by Santiago Armstrong). Scratch code: own `S`, `T_−`, six-band table, union-find exposure graphs and a bounded inverse-history enumeration; nothing imported from the repository.

## What I checked

- **Certificates** (`python3 tools/run_certificates.py --node fixed-ternary-order-unbounded-depth`): `check_barrier_recompute.py` PASS (0 s), `check_legacy_replay.py` PASS (12 s, replays `check_fixed_h.py` and `fixed_h_check.py` with all files unchanged); exit 0, wall time 11.96 s.
- **Hypotheses of the theorem.** `2^10 | X ⇒ 8 | N = 3X/128`; `X ≡ 10 (mod 3^(D+2))`, `D ≥ 1 ⇒ v3(X − 1) = 2`; `X ≡ 1 (mod 9) ⇒ N ≡ 6 (mod 18)`, so `y_1 = 64N − 1 ≡ 5`, `y_2 = 96N − 1 ≡ 17`, `y_3 = 144N − 1 ≡ 17 (mod 18)` in bands 4, 5, 5 of the table of [`disjoint-annular-recursion`](../disjoint-annular-recursion/README.md): coefficients `−2, 2, 2`. `3y_j + 1 = 2y_(j+1)` with `y_(j+1)` odd for `j + 1 ≤ D + 3`; `y_4 = 216N − 1` is above the support.
- **Barrier lemma.** Orbits of the odd integers `1..33` reach 1 and their union has 54 elements (maximum 3077); over `u_0 = 2^s 3^r ≥ 4` exactly 22 triples satisfy `9u_0 < z_0 < 10u_0`, six with `c_0 = 1`, and the other twelve `c_0 ∈ {5, 7, 13, 19, 35, 47, 49, 63, 73, 109, 131, 163}` enter the `T_−` cycles `{5, 7}` or `{17, 25, 37, 55, 41, 61, 91}` by exactly the connecting paths listed; none reaches 1. Threshold check: `35/10 = 3.5 > 27/8`, whereas 33 would not suffice.
- **Section 3 re-derived.** Chain points are `−1 (mod 3)`, so the first inverse valuation is odd; valuation 1 stays on the chain and `(2y_1 − 1)/3 = X − 1`. With `x = uX − c`, `u' = 2^a u/3`, `c' = (2^a c + 1)/3`: while `A < k`, `3 | uX`, so admissibility is `3 | 2^a c + 1` and `c` stays an odd integer; `g_a(w) = (2^a w − 1)/3` is increasing in `w` and in `a` for `w > 0`, which gives `u − c > (3/2)^(k−l) − 1 ≥ 0` through the crossing (`l ≤ k − 2` there); before the crossing `u = 3^E(3/2)^s ≥ 9` and `x > 9(X − 1) > 27X/8 − 1`; at the crossing `u_0 = 3^r 2^s ≥ 4`, `1 < c_0 < u_0`, `T_−^l(c_0) = 1` because `3c' − 1 = 2^a c`; afterwards `x − z = u(X − 10)` is even with `v3 ≥ k − l + D + 2 ≥ 3`, so admissibility transfers, `z` stays a positive odd ancestor of `z_0`, `z ≥ 35`, and `x = u(X − 10) + z > zX/10 ≥ 7X/2 > 27X/8 − 1`.
- **Section 4 re-derived.** Arrows `y_j → y_(j+1)` are exposed for `j ≤ D + 2`; `(3x+1)/2 + 1 = (3/2)(x+1)` gives height `≤ (3/2)^(D−1)·144N − 1 = y_(D+2)` within `D − 1` steps of a source, so `y_(D+3)` has no exposed outgoing arrow; `X − 1` is a multiple of 3 with coefficient 0 and no predecessor; a component without 1 has `Σ (I − P)J = 0`.
- **Brute-force exposure graphs** (every nonzero source of `A_N`, first `D` arrows, union-find) at the least admissible `X`: `D = 1, 2` (`X = 22528`, `N = 528`, 17,622 sources), `D = 3` (`X = 105472`, `N = 2472`, 82,503 sources), `D = 4..7` (`X = 354304`, `N = 8304`, 277,146 sources, up to 433,035 arrows), and a second admissible `X` at `D = 1, 2`: the component of `144N − 1` is exactly the chain, with sources `(−2, 2, 2)`, mass 2, 1 absent; `|supp A_N| = 267N/8` and total 0 in every case.
- **Own inverse-history enumeration** (bound `B_r = ⌊3^r·144N/2^r⌋ − 1`, derived from the height bound above) from every chain vertex, `D = 1..12` at the least `X` (`N` up to 348,633,600) and on the ladder `X = 2^e` for `D = 1, 2, 3, 5, 8` (`e = 24, 24, 24, 996, 2454`): no off-chain source, and every off-chain state within the bound exceeds `144N − 1` (minimum ratio 1.185), the stronger statement behind (6) and (8).
- **Shadow bookkeeping** on all 66 first-step-departure histories of length `≤ D ≤ 8`: `x = uX − c`, `E ≥ 2`, the pre-crossing facts, `u_0`, `c_0`, `T_−^l(c_0) = 1`, `z_0 ≥ 35` and outside the 54-set, every later `z` an odd integer `≥ 35` outside the 54-set, and (8).
- **Section 5.** 2 has order `2·3^(D+1)` modulo `3^(D+2)`; `e_D` computed by my own digit lifting for `D = 1..64`, unique modulo `2·3^(D+1)` (brute force for `D ≤ 7`), divisible by 6, `≥ max(D+4, 10)`; `N = 96·64^(e/6 − 2)`.
- **Controls.** The theorem concerns the `3x+1` annulus; no cycle claim is made. The auxiliary map is the `d = −1` member of the family and is used only as a finite exclusion test; from odd seeds below `10^5` its cycles are exactly `{1}`, `{5, 7}`, `{17, …, 91}`, which the proof does not need.

## What I did not check

- The legacy inverse oracle's internals and the receipt's components for `D = 12` and the three ladder examples (replayed by the certificate only; my own enumeration covers `D ≤ 12` and five ladder depths).
- Depths beyond 12 numerically; the written argument covers them.

## Findings

1. Statement, barrier lemma: the second cycle is written with its seven elements and the return arrow, which is correct; the claim field calls both "nontrivial cycles of the auxiliary map `3c − 1`". Severity: none.
2. `check_fixed_h.py` and `fixed_h_check.py` (evidence) rely on `assert`; the certificate `check_barrier_recompute.py` collects failures explicitly, and the replay runs the legacy scripts without `-O` by design. Severity: none (hygiene note).
3. Section 3, "including the first step with `A ≥ k`": the integrality of `c` at that step needs `3 | uX` before the step, which holds because `l ≤ k − 2` at the crossing; the text states `l ≤ k`, which suffices. Severity: none.

## Verdict

HOLDS. The barrier lemma, the inverse-history argument, the component closure and the ladder quantifier re-derive and are confirmed by independent brute force and inverse enumeration; the scope (a bound on exposure depth as a function of `h` alone is refuted; no permanent component, no cutoff without eventual certificate) matches the proof.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
