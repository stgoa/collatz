# Review of critical-image-rank-composition

Independent review of [`README.md`](README.md) (legacy R43), its certificate and its displayed bounds, against the definitions of [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md), [`critical-tripling-domain-equivalence`](../critical-tripling-domain-equivalence/README.md), [`critical-nine-elimination`](../critical-nine-elimination/README.md) and [`decreasing-w5-phase-inverse-barrier`](../decreasing-w5-phase-inverse-barrier/README.md). Every number below was computed by my own scripts (an independent implementation of `ν`, the currents, the R37 plan, the R40 expansion and `H_s`, not the legacy libraries) or re-derived by hand.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node critical-image-rank-composition`: PASS, exit 0, 12 s (legacy replay of `check_rank_closure.py` and `batch_r43_r46_check.py`, every receipt byte-identical).
- **Preamble.** `3w ≡ 11 (mod 16)` for `w ∈ W9` is complementary with `a = 2`, so `ρ(w) = 3w`; for `w ∈ W5`, `3w ≡ 7 (mod 8)` is an F-root with `a ≥ 3`, so `ρ(w) = 3w` or `(3w−1)/2`. Checked for every `w ∈ W5 ∪ W9` below `2^16`, with the bijection onto the critical roots.
- **Section 1 (W9 bound).** Re-derived the table: `d = 4, 6, 8` give `z = (9w−1)/16, 3(9w−1)/64, 9(9w−1)/256` and `u* = 4z+1 = (9w+3)/4, (27w+13)/16, (81w+55)/64`. When `3z` is noncanonical, `6z+1` is complementary canonical (`r` is canonical iff `2r+1` is selected), `3u* = 2(6z+1)+1` is its selected partner, so `ρ(u*) = 6z+1 = (27w+5)/8, (81w+23)/32, (243w+101)/128`; the last two are below `3w` iff `15w > 23` and `141w > 101`, and the first exceeds `3w` always. Non-exceptional requests `u < w` give `ρ(u) ≤ 3u < 3w ≤ (27w+5)/8`. With my own fully expanded R40 plan (divergence `P(w) − Σ c_u P(u)` verified at every node): for all 16,384 `w ∈ W9` below `2^18`, every W5 request has `8ρ(u) ≤ 27w+5`; equality in exactly 4,096 cases, all the top-level `d = 4` exception; the requests with `ρ(u) > 3w` are exactly those 4,096. Exceptional rows seen: 4,096 (`d=4`), 1,023 (`d=6`), 255 (`d=8`), formulas exact in all. The receipt's rows `w = 9, 377, 825` give ranks 31, 955, 1,567 as stored.
- **Section 2 (absorption bound).** A direct W5 request has `ρ(u) = ν(seed) ≤ seed ≤ s`; a W9 request `b` has `3b ≤ seed ≤ s`, and its expansion has `8ρ(u) ≤ 27b+5 ≤ 9s+5`. Checked for all 65,536 odd `s < 2^17`: no violation; equality in 683 cases, each with `s` critical, `3 | s`, `s/3 ∈ W9` and `v2(9(s/3)−1) = 4`, so the bound is sharp.
- **Bound (3).** `v ≤ (2p+1)/3` gives `(9v+5)/8 ≤ (3p+4)/4 < p` iff `p > 4`; the least complementary canonical root is 7. Checked for all 10,923 critical `p < 2^17`; for the 5,461 complementary `p ≡ 2 (mod 3)` below `2^17`, `H_((2p−1)/3)` has ranks `≤ (3p+1)/4`.
- **Section 3 (composition).** Strong induction on the positive integer `ρ(w)` over `W5`, then R40 and R37: sound under the hypotheses `u ∈ W5` and `ρ(u) < ρ(w)`; finite branching and a well-founded rank give termination of the formal expansion. R41 `E_good` compatibility: `p < q` since `2^(h+1) < 3^h` for `h ≥ 2`; `H_v` ranks `< p` by (3); `H_z` ranks `≤ (9z+5)/8 ≤ (9w+11)/32 < (3w−1)/2 = q` because `39w > 27`. Checked with my own R41 plan for all 1,821 `E_good` inputs below `2^17` (requests in W5, all ranks `< q`) and all 910 returning inputs (coefficient `+1` at `w`, equal rank, so (4) rejects them). A generic strict-rank closure rebuilt with the two rules I implemented (R41 `E_good`, R44 forward): below 8,192 it accepts 148 inputs (115 by R41, the receipt's R41 count, 33 by R44), leaves always unresolved, no leaf-free closure with these two rules.
- **Section 4 counts** against `critical_rank_audit.json`: 2,048 W9 plans, 4,096 absorption plans, 195 accepted of 1,024, 58 mixed closures, `w = 749` (five expansions, leaves 125 and 701), `w = 1029` (R44 and R46, no leaves), seven substitutions, seven rejections.
- **Controls.** The identities used (sibling `S(4x+1) = S(x)`, halving, path words, the ancestor word) are plain `3x+d` arithmetic: checked for `d = 1, 5, 7, 13, 61` (about 16,000 halving cases per `d`, no failure). The node claims nothing `d`-specific, and its composition theorem is conditional, with a premise false for the controls (they have nonabsorbing cycles), so no control can refute it.

## What I did not check

- The R45 and R46 rules used by `rules_union.py` (other nodes), and the side-lane probe beyond its byte-identical receipt.
- The proofs of R37's equivalence and of R40's local identities beyond re-implementing what this node uses (my re-implementation did reproduce `div = P(w) − Σ c_u P(u)` for every W9 input tested).
- The side-lane measurement scripts (evidence only; not run).

## Findings

1. **Claim field, composition hypothesis (imprecision, corrected).** The frontmatter `claim` states the hypothesis as "all requested ranks strictly below rho(w)" and omits `u ∈ W5`, which the Statement (item 3), the proof (4) and the validator all require. The hypothesis is essential: at `w = 21` the R41 plan with its W9 request unexpanded asks for `v = 9` with `ρ(9) = 27 < 31 = ρ(21)` and for 5 (rank 7), yet R40's expansion of `P(9)` is `P(21) − P(5)`, which returns the parent; the same happens on all 455 returning inputs below `2^16` (`ρ(v) = 3v < ρ(w)` in every case). I inserted "every requested u in W5" into the claim; the meaning of the Statement is unchanged.
2. **Section 1, "only d = 4 can increase rank" (imprecision).** Argued for the local table only. It also holds for the fully expanded plan: W9 children satisfy `b ≤ (9w+11)/12` (R40, section 3), so a nested exceptional rank is at most `(243w+357)/96 < 3w` for `w ≥ 9`; numerically the largest nested exceptional rank below `2^16` is `0.635·3w`. No change.
3. **Sections 1 and 3 (imprecision).** Two one-line inequalities are used silently: `3w ≤ (27w+5)/8` (from `ρ(u) < 3w` to (1)) and `(9z+5)/8 ≤ (9w+11)/32 < (3w−1)/2` (the "other absorption input"). Both hold; recorded here.
4. **Statement item 2 (imprecision).** "complementary canonical root `p > 4` with pair index `v`" presupposes `p ≢ 2 (mod 3)`; the proof covers `p ≡ 2 (mod 3)` separately with the sharper `(3p+1)/4`. No change.

## Verdict

HOLDS WITH CORRECTIONS. Correction applied: the omitted hypothesis "every requested u in W5" added to the claim field (finding 1). Every displayed bound and the composition theorem are correct as stated in the Statement and proof; the certificate passed.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
