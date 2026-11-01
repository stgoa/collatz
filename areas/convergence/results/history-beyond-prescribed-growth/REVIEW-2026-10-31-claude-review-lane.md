# Review of history-beyond-prescribed-growth

Independent review (Claude review lane, Fable 5.1; directed by Santiago Armstrong). Scratch code: own `S`, `ν`, `T = νS`, `F`, `v2`, `v3`; nothing imported from the repository.

## What I checked

- **Certificate** (`python3 tools/run_certificates.py --node history-beyond-prescribed-growth`): `check_legacy_replay.py` PASS (9 s); exit 0, wall time 8.80 s. It replays `batch_r81_r83_check.py` and `check_growth_escape.py` with receipts byte-identical.
- **R79 inputs.** For every odd `b < 400,000`: `b ≡ 905 (mod 8192) ⇔ v2(217b+223) ≥ 13`; `Y(U(b)) = 729·Y(b)/512`; on the guard `U(b)` is an integer, `3b` has the word `(1,2,1,1,1,2)` to `6U(b)+1`, and `ν(6U(b)+1) = 3U(b)`. `v2(Y(b)) = 9r+17` gives `⌊(v2 − 13)/9⌋ = r` complete returns.
- **Rays (2), (3).** Re-derived from R25's inverse branches: ray 0 is `(4F^(3L)(2q+1) − 1)/3`, ray 1 is `(4F^(3L+1)(q) − 1)/3`; every `a ≡ 1 (mod 8)`; `p + 1 = (2/3)^h (a+1)` with `v2(p+1) = h+1`, the odd part `≡ 3^h ≡ −3^(h+1) (mod 4)`, so `p` is a complementary canonical climber for `h ≥ 1`, and `p ≢ 2 (mod 3)` by maximality.
- **All-ray witness** `b = 96797577`: `v2(Y(b)) = 26` (`r = 1`), `c = U²(b)`, `z = (9c−1)/16` with `z ≡ 5 (mod 8), (mod 9)`, `q = 3z` canonical, `Q = 290392731`, `J0 = 27`, `P0 = 16498700317341`, cutoff ratios 18683 (ray 0) and 9341 (ray 1), hence `L ≤ 2` on each ray; the six `(h, p)` pairs equal the table; each `a` is canonical with `T(a) = q`; ray 0 merges with `q` at clocks `(5, 4)`, ray 1 has `S(a) = F^(3L+1)(q)` with valuations `(2, 6L+3)`; all six fail `h ≥ 1 ∧ p < Q`; `S^18(3b) = S^4(q)` (the H17 clocks `(6r+12, 4)`). Re-derived (5)–(6): `p` odd `< Q` gives `2^(h+1) | p+1 ≤ Q−1`, so `h ≤ J0`, `a+1 ≤ P0`, `64^L ≤ (9P0−2)/(9a0+7)`.
- **Section 3.** (7): `144z + 16 = 81c + 7`. `C_s = 223(729^s − 512^s)/217` is an integer and `c = (729^s b + C_s)/512^s`. (9) as a polynomial identity; `3^d | B0 ⇔ 64^L ≡ 217/8272 (mod 3^d)`; `v3(64^n − 1) = 2 + v3(n)` (checked `n < 200`), so 64 generates the subgroup `≡ 1 (mod 9)` and the order of 64 modulo `3^d` is `3^(d−2)`; `217 ≡ 8272 ≡ 1 (mod 9)`, `v3(8272 − 217) = 2`. Brute force over all `L < 3^8` and `L < 3^14` gives the unique solutions `L = 740` (`s = 1`) and `L = 2028089` (`s = 2`), `h = 8148`, `22308995`. (10) checked as an exact rational identity on 160 random cell members. (12) gives `v2(Y(c)) = 8`, hence `v2(Y(b)) = 9r+17`.
- **Section 4.** Exact: `a + 1 = 9·64^L(729/512)^s (b + 223/217) + [64^L(7/9 − 2007/217) + 2/9]`, bracket negative for all `L ≥ 0`; `λ = 9·(131072/177147)^L/18^s`, `≤ 1/2`, with equality only at `(L, s) = (0, 1)`; `h = 11L + 8s ≥ 6s + 2`.
- **Materialised `r = 0` cells.** With my own CRT: modulus `2^19·3^8141` (12,923 bits); for both terminal units and indices 0, 1: `b` on the guard, `v2(Y(b)) = 17`, `c ≡ 137 (mod 1024)`, `q = 3z` canonical, `a` canonical with `T(a) = q`, `v3(a+1) = 8148` exactly with the prescribed unit, `p` complementary canonical, `0 < p < b/2` (in fact `p/b ≈ 2^(−323)`: 12,599 versus 12,922 bits), (15) holds, the word (16) (12 arrows) and the word (17) (8,153 arrows) both end at `M = (2187c + 925)/512 > 3b`; 8,165 rows as in the receipt.
- **Section 5 on 160 random members of the binary cell (12)**, `r = 0..3`, `L = 0..3`: word (16), `x = (81b+23)/16`, each six-arrow block `x ↦ (729x + 817)/512 = (81U(b)+23)/16`, tail `(1,1,3)`; from `q ≡ 231 (mod 1728)` the word `(1,1,2,1)` to `M`; word (17); `M > 3b`.
- **Critical pair index of `p`** (R37 bijection): for the witness pairs `p = 588709275` (`h = 1`, `p ≡ 11 mod 16`) the index is in `W9`, for `p = 3215137588615` (`h = 2`) and for the cell endpoint it is in `W5`, each with `ν(3w) = p`; on 6,720 random complementary canonical `p ≢ 2 (mod 3)`, `h = 1` splits `W5`/`W9` (1120/1167) and `h ≥ 2` is always `W5`, as section 1 says.
- **Controls.** The claim concerns explicit `3x+1` integer families and a named inference procedure, not cycles; the `3x+d` fixtures do not bear on it.

## What I did not check

- The internals of the formal plans `H_p`, `H_b`, `A_p`, `A_b` (R37/R75): I used only R75's stated property that requests have rank `≤ ν(s)` and the bijection `W → C`; the "only if" of the decision in section 2 rests on `H_p` starting with its own critical pair at coefficient `+1`, which I did not rebuild.
- The stored absorption tables of the receipt (31041/39181-arrow supplies, 129-row compiled current) beyond the legacy replay; for the witness I only confirmed that `b` and `Q` reach 1.
- Cells with `r ≥ 1` were not materialised (their moduli exceed `3^(2·10^7)`); only the parameters `(L, h)`, the binary condition (12), and the words were checked there.

## Findings

1. Section 4 / claim, "slope … `≤ 1/2`": correct but far from sharp; on the `r = 0` cells `p/b ≈ 2^(−323)`. Severity: none.
2. Statement item 1, "all indices `L` are decided by the finite cutoff": the cutoff (6) is derived from `p < Q` alone, so it is exhaustive for the decision as stated. Severity: none (recorded).
3. The claim's "exact point order `h` on the second quotient inverse ray": "second" means base `16z + 1` (ray 1); the proof says so. Severity: imprecision of wording only.

## Verdict

HOLDS. All displayed formulas (1)–(18), the witness, the uniqueness of `L`, the exact slope and intercept, and the two materialised `r = 0` cells re-derive and recompute; the scope (one procedure decided, an explicit infinite subfamily per `r`, every smaller input a premise, not coverage of the H17 type) matches the proof.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
