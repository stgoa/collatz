# Review of fixed-word-history-cells

Independent review of [`README.md`](README.md) (authors: ChatGPT main lane, Codex). Scope as in the node: odd-only `3x+1`, absorbing at 1, exact valuation words, the retained critical basis of [`common-critical-rank-basis`](../common-critical-rank-basis/README.md). Own scripts (own `ν`, `T`, canonical test, validated by brute force as described in my review of [`high-smaller-origin-history`](../high-smaller-origin-history/README.md)) live outside the repository; every number below comes from them or from the certificate.

## What I checked

- **Certificate.** `python3 tools/run_certificates.py --node fixed-word-history-cells`: PASS, exit 0, 9 s wall (concurrent with other nodes). It replays `batch_r81_r83_check.py` and `check_history_lifting.py` in the legacy layout, every file unchanged; the receipt counts (18 specifications, 189 lifts, 592 memberships, 191 native plans, 62 old-phase records with 38 genuine high requests, outputs of 46/100/108 rows, 19 rejections) match `evidence`.
- **Cylinder lemma (§1).** For 300 random exact words the odd integers following the word form one residue class modulo `2^(A+1)` (members whose path meets the absorber excepted).
- **Theorem (3)-(6), re-derived.** Each exact valuation `v` at `x` is the congruence `3x + 1 ≡ 2^v (mod 2^(v+1))`, so the word fixes `q mod 2^(A+1)` and `q − q0 = 2^(A+1) j`. Equal endpoints force `p − p0 = 3^a(q − q0)2^B/(3^b 2^A) = 2^(B+1) 3^(a−b) j`; for `b > a` integrality is exactly `3^(b−a) | j`, for `a ≥ b` nothing more, and `2^(B+1) | p − p0` keeps `β` exact. Conversely the endpoint increments `2·3^max(a,b) k` agree on both sides. Brute force on 150 random anchor pairs: the set of odd `q ≤ q0 + 12M` with exact word `α` for which some odd `p` with exact word `β` shares the endpoint (`p` solved exactly from the affine formula, no window on `p`) is exactly `{q0 + Mk}` with partners `p0 + Pk`, including negative `k` down to positivity. Examples: `(739, 725)` has `M = P = 1024` and constant gap 14; `(21, 19)` has `M = 2^7·3^5`, `P = 2^15`, slope `256/243`, and `k = 0` is the only index with `p < q`.
- **Statement 2.** `div(N_(3w) + K + J_p − J_w) = [3w] − [q] + [q] − [p] + [p] − [w] − Σ(A_p − A_w)P = P(w) − Σ c P`; ranks `≤ max(ν(p), ν(w)) < q` since `ν(p) ≤ p < q` and `ν(w) ≤ w < ρ(w) = q`.
- **The R80 cell (§3).** Affine data `(9, 5, 8)` and `(3^14, 5403385, 2^22)`; `M = 16·3^12 = 8503056`, `P = 2^23`, `M − P = 114448`, `2^17/2^4 = 8192`. For `k = 0..3000` and 100 random `k < 2^70`: both words exact (the fourteenth letter is 6 because `9q + 5 ≡ 8 (mod 16)` throughout), equal endpoints `(9q+5)/8`, `q − p = 156 + 114448k`, `p, q, y` canonical, the twelve lower states canonical and above `q`, peak `32q + 17`, `T(q) = y = T^13(p)`. The canonical type of each base state is decided modulo at most `2^9`, below every increment `2^(23−A_j)`, which is why (15) preserves the phases. Minimality: `11547 + 8·3^12` does not follow `(1, 2)`; `11547 + 16·3^11` has a non-integral partner.
- **Blocked phase (17)-(18)** for `k ≤ 5000: odd `k` gives `v2(3q − 1) ≥ 5`; even `k` gives `d = 4`, `Z = 6496 + 3^14 k = 3z + 1`, and the test `Z/2^H ≡ 3^H (mod 4)` agrees with "`3z` noncanonical" in all 2501 cases (1251 blocked, 1250 not).
- **§4, `k = 512j`** for `j < 400`: `H = 5`, blocked; `a = 7`; `r = (6561q + 8965)/1024 ≡ 1 (mod 8)` canonical; `f = S(r) = 55495 + 2·3^21 j ≡ 1 (mod 3)`; whenever `f` is critical (98 of 400 cases) the request `v = (2f+1)/3` is `5 (mod 8)` with `ρ(v) = f` and `f − ρ(u) = (15075q + 25359)/4096 > 0`, `ρ(u) = (9q+5)/8 > q`; for `j ≡ 6 (mod 8)` always `f ≡ 11 (mod 16)`, complementary canonical; `k ≡ 3072 (mod 4096)` never meets `k ≡ 0 (mod 8192)`.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3). The cell theorem is arithmetic of exact valuations and holds verbatim for `3x+d` with the same `M, P`: brute force with anchors on the actual cycles of `3x+5` (`19 →(1,1)→ 49`, `31 →(1)→ 49`: `M = 8`, `P = 12`; `23`, `37`), `3x+7` (`5 →(1,3)→ 5`, `11 →(3)→ 5`: `M = 32`, `P = 48`), `3x+13` (`211`, `323`; `131`, `203`) and `3x+61` (`235`, `383`) reproduces the predicted cells exactly. The node claims nothing about convergence, so this is as it should be.

## What I did not check

- R75's absorption plans and the receipt's 191 native plans and three supplied outputs; the R44/R52 plan coefficients beyond the leading request `v` (taken from [`returning-forward-interface`](../returning-forward-interface/README.md), reviewed, and [`returning-second-forward-interface`](../returning-second-forward-interface/README.md), written).
- The probe and the legacy checker ran only inside the replay.

## Findings

1. **§3, (15) (imprecision).** "divisible by 512, preserving all the canonical phases": what is needed is that each increment `2^(23−A_j)` is a multiple of the modulus `2^(a_j+2)` (or 8) deciding that state's canonical type; the largest such modulus is `2^9` at `j = 0`. The text asserts the conclusion without the comparison; I verified it.
2. **§4 (imprecision).** "For `k` odd, `v2(3q − 1) ≥ 5`, so the local W9 row is nonblocked" is correct because R75 blocks only `d = 4` with noncanonical `3z`; "nonblocked" means `ρ`-valid, which is not spelled out.
3. **Typos.** Missing spaces in the legacy text ("modulus2^(A+1)", "q739", "p725", "b3849").

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
