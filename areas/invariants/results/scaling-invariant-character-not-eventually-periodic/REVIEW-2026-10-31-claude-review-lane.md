# Review of scaling-invariant-character-not-eventually-periodic

## What I checked

- Read the node; [`literature.md`](../digit-count-invariant-colourings-constant/literature.md) §L6 and [`PROOF_REVIEW.md`](../digit-count-invariant-colourings-constant/PROOF_REVIEW.md) §§4–5 of the digit-count folder; [`binary-kernel-first-ternary-image`](../binary-kernel-first-ternary-image/README.md) §5.
- Re-derived the four statements:
  - `chi` is the Kronecker character `(−8/·) = (−2/·)`: multiplicative on the odd residues mod 8, and `3·{1, 3} = {3, 1}`, `3·{5, 7} = {7, 5} (mod 8)`, so `g(3n) = g(n)`; doubling keeps the odd part.
  - 2-kernel: for `r = 2^a u`, `u` odd, `a < e`, `2^e n + r = 2^a(2^(e−a) n + u)` with an odd bracket, so the section is `chi(2^(e−a) n + u)`, a function of `n mod 8` at most. Since `u < 2^(e−a)`, the kernel is exactly `{g, chi(2n+1), chi(4n+1), +1, −1}`: five functions (with `g(0) = +1`).
  - Not eventually periodic: for `M = 2^a m`, `u ∈ {1, 5}` with `chi(u) ≠ chi(m)`, `n = 2^(a+k) u`, `k ≥ 3`: `oddpart(n + M) = 2^k u + m ≡ m (mod 8)`.
  - Mixed sections: `Δ = 3^t − 3^s = 2^a D`, `K > a + 3`, `v` odd with `2^K v ≡ 1 (mod 3^t)` and `v ≡ 1` or `5 (mod 8)` by CRT, `n = (2^K v − 1)/3^t > 0`; `3^t(3^s n + 1) = 3^s 2^K v + Δ = 2^a(3^s 2^(K−a) v + D)`. The bracket is odd, `≡ D (mod 8)` because `16 | 2^(K−a)`, and positive also when `D < 0` because `3^s 2^K v ≥ 3^s > 3^s − 3^t`. Then `t` applications of `g(3n) = g(n)` give `g(3^s n + 1) = chi(D) ≠ chi(v) = g(3^t n + 1)`. Offset 1 is a ternary-kernel residue only for `t ≥ 1`, as the node says.
  - `g(3) = chi(3) = +1`, `g(10) = chi(5) = −1`.
- My script `check_scaling.py` (scratch folder, 14.0 s, exit 0): `chi(p) = (−2/p)` by Euler's criterion for the odd primes `p < 2000`; `g(2n) = g(3n) = g(n)` for `n ≤ 2·10^5` and `g(3^t n) = g(n)` for `t ≤ 6`; the section formula for every `e ≤ 10`, `r < 2^e` on 4,096 terms, with exactly 5 distinct sections; the node's non-period witnesses for every `M ≤ 400` at `k = 3, 10, 25`, plus a brute-force violation of each period `M ≤ 400` inside `[10^5, 10^5 + 2000)`; the mixed-section construction for all 56 ordered pairs `1 ≤ t ≠ s ≤ 8` (positivity, oddness and residue of the bracket, both values); brute force, the ten sections `n ↦ g(3^t n + 1)`, `t ≤ 10`, differ pairwise below `n = 50,000`, and the ternary kernel through depth `E = 0, …, 6` has at least `1, 3, 9, 27, 81, 243, 729` distinct elements on 300-term prefixes, so all `3^E` sections at each depth differ; `g(3) = +1`, `g(10) = −1`; `g(8n+1) = +1`.
- Certificates: none listed; `python3 tools/run_certificates.py --node scaling-invariant-character-not-eventually-periodic`: exit 0, 0.12 s, nothing to run. The evidence script `verify_examples.py` ran as a certificate of `digit-count-invariant-colourings-constant`: PASS, exit 0, under 1 s (its `scaling_control` key: 72 ordered mixed pairs for `t, s ≤ 9`, 256 non-period witnesses).
- Controls: the node is a `3x+1` counterexample about hypotheses, not a claim about cycles, so the `3x+d` cycle controls do not apply; I confirmed that `g` fails invariance exactly where stated, so no actual colouring of any `3x+d` is excluded.

## What I did not check

- Konieczny–Lemańczyk–Müllner, Lemma 8 and Theorem 1 (context only; the node checks the example directly).
- A DFAO for `g`; "2-automatic" was verified as finiteness of the 2-kernel, which is the area's definition.

## Findings

1. **Claim and Statement, "g is 2-automatic"** (imprecision, no change). Proved as finiteness of the 2-kernel; passing to an automaton is the finite-kernel characterisation, not listed under `assumes`. The area defines automatic by the finite kernel (V004, V007), and a direct automaton exists anyway (read the bits most significant first and remember the three bits ending at the last 1), so nothing is missing. The exact kernel size, 5, could be stated.
2. **Proof, positivity of the bracket when `D < 0`** (imprecision, no change). "Whose parenthesis is positive" is asserted without the reason; it is `3^s 2^(K−a) v + D ≥ 3^s 2^(K−a) − (3^s − 3^t)/2^a > 0`.
3. **Frontmatter `evidence` paths** (typo-level, no text change). Written relative to a node folder, so right after the move. Five body links got one more `../`, and the link to `monochromatic-cylinder-forces-constancy` now points at that node's `README.md`.

## Verdict

HOLDS. No correction to the content; link repair only, after the move into a folder.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
