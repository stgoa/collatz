# Review of even-exit-smaller-target-cone

Independent review (wave 7). Definitions were followed into [`elementary-bridge-quotient-normal-form`](../elementary-bridge-quotient-normal-form/README.md) (`ν`, selected, complementary, canonical), [`common-critical-rank-basis`](../common-critical-rank-basis/README.md) (bound `ρ(v) ≤ ν(s)` on every request of the critical plan), [`complementary-run-bridges`](../complementary-run-bridges/README.md), [`forward-blocks-low-exponent-tests`](../forward-blocks-low-exponent-tests/README.md) and [`rank-excess-absorption-classification`](../rank-excess-absorption-classification/README.md). Every number below comes from my scratch code (outside the repository) or from the node's proof.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node even-exit-smaller-target-cone`: PASS, exit 0, 9.3 s wall (`check_legacy_replay.py` replays `r86_even_exit_check.py` and `check_even_exit_history.py` unchanged; every file byte-identical).
- **§1, re-derived.** `4^b | 3^(H−1)t − 1` gives `t ≡ 3^(H−1) ≡ −3^H (mod 4)`, so `q = 2^H t − 1` is a complementary root (`H ≥ 3`), hence canonical, `ν(q) = q` and `ρ(w) = q`; `q ≡ 7 (mod 8)` gives `w = q/3 ≡ 5 (mod 8)`. `S^j(q) = 3^j 2^(H−j) t − 1` for `j ≤ H − 1`, ending at `2^(2b+1)u + 1`; then `b` arrows of valuation exactly 2 through `2^(2(b−j)+1) 3^j u + 1` to `f = 2n + 1`. Since `(n+1)/2 ≡ 1 (mod 4)`, `f = 2^2·(n+1)/2 − 1` is selected with `a = 2`, so `ν(f) = n`; `S(f) = 3n + 2 = F(y)`, giving (5) and `div G = [q] − [y]`.
- **§2, re-derived.** Substituting `t = (q+1)/2^H` and `u = (3^(H−1)(q+1) − 2^H)/2^(H+2b)` gives (8) exactly; `y ≡ 1 (mod 3)` because `4y = 3n + 1`; the three cases of `λ` give (7) with `y ≠ q`. The boundary of (9) is `P(w) − Σ (A_y − A_w)P`, and every request has rank `≤ max(ν(y), ν(w)) ≤ max(y, w) < q` on the cone by the critical-basis bound.
- **§3, re-derived.** (10) from `u ≡ 3^(−b) (mod 8)` and `q ≡ c·3^D (mod 3^(D+1))`; the periods; `b_H ≤ 2H`; `n − q = (λ_n − 1)q + λ_n − (3/4)^b` with `λ_n = 81/64` at `H = 4` and `λ_n > 1` at `b_H` for `H ≥ 5` because (7) fails at `b_H − 1`.
- **§4, re-derived.** `t ≡ 23 (mod 32)` and `t ≡ 1 (mod 3)` give `t ≡ 55 (mod 96)`; (12); `(27n + 29)/32 − q = (1952 + 3336l)/32 > 0`. Exclusions from the rules' stated domains: nonselected `3w` excludes R41, R44, R46, R52, R55, R56, R60 and R64 (their claims require selected `3w`), and R57 (`q mod 5184 ∈ {879, 2607, 4335} ≠ 5167`); `3 ∤ w` excludes R47; R45: `v3(4w + 1) = 1` exactly since `4w + 1 ≡ 3 (mod 9)`, `C = (4w+1)/3 ≡ 1 (mod 3)`, so the endpoint `p = 4C − 1 ≡ 0 (mod 3)` is R45's zero-current branch, and `v3(8w + 1) = 0`; R50 (`k = 4`): `L = v3(8C − 1) = 0 < 3`; R53 needs `v2(n + 1) = 2`, here `v2(n + 1) = 1`; R58 and R62 need `w ≡ 437 (mod 512)`.
- **Independent computation** (scratch `recompute_r86.py`, own `S`, `ν`, `ρ`, `T = νS`, currents with the atom at 1 killed). 576 cell instances (`H = 3..10`, `b = 1..4`, `D = 1..3`, `c = 1, 2`, three members each): (2) with exact `v3(q) = D` and unit `c`, `w ∈ W5`, `q` complementary canonical, `ρ(w) = q`, `f` selected with exponent 2 and `ν(f) = n`, path word `(1^(H−1), 2^b)` with every source canonical, `S^(H+b+1)(q) = S(y)`, `T^(H+b)(q) = ν(y)`, `div G = [q] − [y]`, identity (8), the iff (7) (198 inside the cone, 378 outside, never `y = q`) and the `n − q` identity. The cell converse by brute force for six cells. (11) at `b_H` for every `H = 4..40` (`c = 1, 2`, `D = 1, 2`, two members each; `b_H = 1, 3, 4, 6, 7, 8, 10, 11, 13` for `H = 4..12`), and `n < q` at `H = 3`, so the restriction `H ≥ 4` is needed. Phase (12): brute force shows (2) at `H = 4`, `b = 1` is exactly `t ≡ 55 (mod 96)`; 40 members have `q, w, n, y` as displayed, `n > q > y`, the R48 bound above `q`, `3w` nonselected, `w ≡ 5 (mod 9)` iff `l ≡ 0 (mod 9)`. Control (14): `q = 927`, `n = 1761`, `y = 1321 > q`, `ν(S(y)) = 495`.
- **Dispatcher run** (scratch `probe_r86_dispatcher.py`: the unmodified legacy `resolved_rules.one_step` in a copy of the pre-migration layout). None of the first 200 members of `w ≡ 293 (mod 4608)` is recognised; 27 of the first 400 members of the coarse phase `w ≡ 293 (mod 512)` are (R45, R47 and R50 arms), all outside the subprogression, as the domain analysis predicts.
- **Controls.** The node excludes no cycle and claims nothing `d`-uniform; the `3x+d` controls do not apply. Its identities are `3x+1` congruences.

## What I did not check

- The formal plans `H_x` of R37/R40/R75 as implemented, and R58 beyond its reviewed statement.
- The domain predicate of R59 (deferred-original-rank-testing) from its own node; only the dispatcher's behaviour on 200 members and the node's statement that its candidates are selected.
- The 50 full plans and three supplied outputs of the legacy receipt, beyond the replay.

## Findings

1. Evidence field and §6 (imprecision): the "34 old-seventeen progression cases" of the legacy checker are arithmetic checks of the stated exclusion reasons (`w ≡ 5 mod 9`, `v2(n+1) = 1`, the R48 bound); they do not call the dispatcher. My probe does and confirms the claim on 200 members.
2. §1 (imprecision): "The congruence in (2) gives `t ≡ −3^H mod 4`" refers to the second line of (2), `4^b | 3^(H−1)t − 1`, not to `q ≡ 0 (mod 3)`.
3. §2 (imprecision): "all its old W5 requests also have rank at most `y`" uses R58 at the seed `y`; the residue reason given (`y ≡ 1 mod 3`, so `y` is never the exceptional `27 mod 48`) is the right one.
4. §§3–5 (typo): equality signs lost in the migrated text ("For H4, b_H=1", "H5,b1,t29", "q927, n1761, y1321"). Readable from context.

No error found.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
