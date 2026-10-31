# Review of monochromatic-cylinder-forces-constancy

## What I checked

- Read the node; [`literature.md`](../digit-count-invariant-colourings-constant/literature.md) §L5 and [`PROOF_REVIEW.md`](../digit-count-invariant-colourings-constant/PROOF_REVIEW.md) §§3–4 of the digit-count folder; [`monks-2006-sufficiency`](../../../../sources/monks-2006-sufficiency.md); [`periodic-invariant-colourings-classification`](../periodic-invariant-colourings-classification/README.md) for the conventions (1 absorbing, identity only at odd `n > 1`).
- Re-derived the proof line by line:
  - With `T_d` the raw shortcut map and `d` odd, the parity word of the first `K` steps is a bijection between `Z/2^K Z` and `{0,1}^K`, and `T_d^K(n) = (3^j n + b)/2^K` with `b = d·Σ_i 3^(j−i) 2^(t_i)`. All summands but the last are divisible by 3, so `b ≡ d·2^(t_j) (mod 3)` is a unit when `j > 0`. The source residue solves `3^j r + b ≡ 0 (mod 2^K)`, uniquely since `3^j` is odd.
  - 2 is a primitive root mod `3^j`: `(1 + 3^l u)^3 = 1 + 3^(l+1)(u + 3^l u^2 + 3^(2l−1) u^3)` with the bracket `≡ u (mod 3)` for `l ≥ 1`, starting from `2^2 = 1 + 3`.
  - For `a` coprime to 3 and `j > 0`, `b·a^(−1)` is a unit mod `3^j`, so `s` exists in one class mod `2·3^(j−1)`, hence arbitrarily large. `n = (2^(K+s) a − b)/3^j` is an integer with `3^j n + b ≡ 0 (mod 2^K)`, so `n ≡ r`. The shortcut states satisfy `x_(t+1) ≥ x_t/2`, so `x_t ≥ n/2^t > 2` for `t < K` once `n > 2^K`: no odd arrow leaves 1, and the colour identities used are `h(n/2) = h(n)` and `h((3n+d)/2) = h(3n+d) = h(n)` at odd `n > 1`. The endpoint is `2^s a`, and `s` halvings reach `a`. The `j = 0` and `K = 0` cases are as stated.
  - Every colour has such a representative: `oddpart(m)`, and if that is not 1, one odd arrow lands on the odd part of `3n + d ≡ d (mod 3)`. Since the constant tail of the cylinder contains predecessors of `a`, `h(m) = h(a)` is the cylinder's colour. The scope (every positive odd `d` with `3 ∤ d`, one class mod `2^K` with `K ≥ 0`, eventually constant) is exactly what the proof delivers.
- My script `check_cylinder.py` (scratch folder, 2.7 s, exit 0): parity-word bijection, affine formula, unit intercept and uniqueness of the source residue for `d ∈ {1, 5, 7, 13, 61}`, `K ≤ 8` (2,555 words); order of 2 mod `3^j` equal to `2·3^(j−1)` for `j ≤ 10`; the predecessor construction for `K ≤ 6`, every class, 36 targets (odd, coprime to 3, including 187, 235, 347) and three values of `s` each: 68,580 paths, all in the prescribed class with `n > 2^K`, all `K` sources above 1 with `x_t·2^t ≥ n`, endpoint `2^s a`, then `a` (largest `s` = 2,919; sources up to 2,922 bits); colour representatives for every `m ≤ 10^5` and each `d`; the Remarks' Thue–Morse statements (sections are `t` or its complement for `a ≤ 6`, `t(5) ≠ t(16)`) and `g(8n+1) = +1`.
- Certificates: none listed; `python3 tools/run_certificates.py --node monochromatic-cylinder-forces-constancy`: exit 0, 0.14 s, nothing to run. The evidence script `verify_examples.py` ran as a certificate of `digit-count-invariant-colourings-constant`: PASS, exit 0, under 1 s (its `cylinders` key: `d ∈ {1, 5, 7, 13, 61}`, `K ≤ 5`, 3,780 paths).
- Controls ([`NOTATION.md`](../../../../conventions/NOTATION.md) §3): `1_(5|n)` and `1_(61|n)` are invariant with 1 absorbing and nonconstant, and every class mod `2^K`, `K ≤ 6`, contains both colours above `10^6` (254 classes), so they fail the hypothesis, as the node says. The absorbed cycle labelling of `3x+5` (labels 1, 5, 19, 23, 187, 347) is an invariant nonconstant colouring and shows at least two labels in every class mod `2^K`, `K ≤ 6`, within `(10^5, 2·10^5]`. The claim excludes no actual `3x+d` cycle; it says only that these colourings have no monochromatic dyadic class.

## What I did not check

- Monks's Theorem 1.1 and Monks–Monks–Monks–Monks Theorem 4.1, taken from the source node and `literature.md` §L5; the originals were not read.
- The remark on most-significant-digit DFAOs with a reset word, beyond noting that a synchronizing suffix `w` of length `K` makes `h` constant on `{n ≡ w (mod 2^K), n ≥ 2^K}`.

## Findings

1. **Frontmatter `evidence` and History, paths** (typo-level, no text change). The paths `../digit-count-invariant-colourings-constant/...` were written relative to a node folder, so they did not resolve from the single file and are right after the move. The three body links got one more `../`.
2. **Proof, "these bits depend exactly on the input modulo 2^K"** (imprecision, no change). What the argument needs is the bijection between residues and words, which the later "unique solution of `3^j r + b = 0 mod 2^K`" uses; both hold.
3. **Proof, "every state in the first K branches is at least n/2^K > 1"** (imprecision, no change). The bound actually available is `x_t ≥ n/2^t > 2` for `t ≤ K − 1`; the text's weaker bound suffices.
4. **Remarks, novelty** (none). The node claims no novelty, assigns the `d = 1` case to Monks, and correctly notes that the progression statement does not transfer to other `d` (the multiples of `d` form a monochromatic progression of `1_(d|n)`).

## Verdict

HOLDS. No correction to the content; link repair only, after the move into a folder.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
