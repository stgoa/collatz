---
id: proportional-slope-two-block-bound
kind: result
title: Proportional-slope two-block words have an explicit exponential denominator bound
status: formal
claim: >
  Raw odd-only clock. Let u, v be nonempty positive words with Σu = a·r, |u| = b·r, Σv = a·s,
  |v| = b·s, U = 2^a > V = 3^b, H_j = U^j − V^j, E = H_gcd(r,s), and K = D_u·C_v − D_v·C_u. Then E
  divides K. For w = u^k v^ℓ (k, ℓ ≥ 1), M = rk, N = sℓ, L = M + N, h = gcd(M, N): if K ≠ 0, write
  K = E·J and let J_0 be |J| with all factors 2 and 3 removed. Then gcd(C_w, D_w) divides J_0·H_h,
  and den(w) ≥ H_L/(J_0·H_h) > U^(L−h)/J_0 ≥ U^max(M,N)/J_0 ≥ U^(L/2)/J_0. In particular
  den(w) ≤ d_0 forces U^max(rk, sℓ) < d_0·J_0, so every bounded denominator layer, 1 included,
  contains only finitely many exponent pairs (k, ℓ) for each fixed noncommuting pair.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: []
lean:
  - LeanLane.Cyc.E_dvd_commutator
  - LeanLane.Cyc.proportional_gcd_dvd
  - LeanLane.Cyc.proportional_den_lower
  - LeanLane.Cyc.proportional_rectangle
  - LeanLane.Cyc.gcd_dvd_K_mul_gcd
  - LeanLane.Cyc.gcd_pow_sub_pow
evidence:
  - "../equal-total-two-block-exclusion/PROPORTIONAL.md, sections 1-3: the written proof (identities (1)-(5), theorem (6)-(8), sharpness)"
  - "../equal-total-two-block-exclusion/two_blocks_audit.json: 44,544 generated and 459 actual proportional-slope bound checks (historical receipt; its checker no longer runs at the new path)"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "PROPORTIONAL.md sections 1-4 re-derived by hand with no error found (feed 2026-10-19 00:26, update 00:31); Lean unit C002-b part 1 verified (feed 17:21): (6)-(8) machine-checked"
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 17:21, VERIFIED Lean C002-b part 1: statement match of (6)-(8) and receipts checked; feed 00:26 REFEREE C002 checked the sharpness examples for t <= 40"
tags: [cycles, denominators, two-blocks, strong-divisibility, formal]
---

# Proportional-slope two-block words have an explicit exponential denominator bound

## Statement

For nonempty fixed words `u, v` put `Q = 2^sum(u)`, `P = 3^len(u)`, `D_u = Q − P`, `S = 2^sum(v)`, `R = 3^len(v)`, `D_v = S − R`, `G_u(k) = (Q^k − P^k)/D_u`, `G_v(ℓ) = (S^ℓ − R^ℓ)/D_v` and `K = D_u·C_v − D_v·C_u`. For `w = u^k v^ℓ`, `k, ℓ ≥ 1`:

```
C = R^ℓ·C_u·G_u(k) + Q^k·C_v·G_v(ℓ),           (1)
D = S^ℓ·Q^k − R^ℓ·P^k,                          (2)
D_u·C − C_u·D = Q^k·G_v(ℓ)·K,                   (3)
D_v·C − C_v·D = −R^ℓ·G_u(k)·K,                  (4)
g = gcd(C, D) divides K·gcd(G_u(k), G_v(ℓ))     (5)
```

when `D > 0`, with no coprimality assumption on `D_u, D_v`.

**Theorem (proportional slopes).** Assume `sum(u) = a·r`, `len(u) = b·r`, `sum(v) = a·s`, `len(v) = b·s`, `gcd(a, b) = 1`, `r, s ≥ 1`, and `U = 2^a > V = 3^b` (if `U < V` there is no positive rational cycle). Put `H_j = U^j − V^j`, `M = rk`, `N = sℓ`, `L = M + N`, `h = gcd(M, N)`, `e = gcd(r, s)`, `E = H_e`. Then `E | K`. If `K ≠ 0`, put `J = K/E` and let `J_0` be `|J|` with all factors 2 and 3 removed. For every `k, ℓ ≥ 1`,

```
g = gcd(C, H_L) divides J_0·H_h,                 (6)
den(w) = H_L/g ≥ H_L/(J_0·H_h) > U^(L−h)/J_0 ≥ U^max(M,N)/J_0 ≥ U^(L/2)/J_0,   (7)
den(w) ≤ d_0  ⟹  U^max(rk, sℓ) < d_0·J_0.        (8)
```

So no bounded denominator, including 1, persists as either repetition count tends to infinity.

## Proof

Written proof: `PROPORTIONAL.md` §§1–2 in [`equal-total-two-block-exclusion`](equal-total-two-block-exclusion/README.md) ([file](equal-total-two-block-exclusion/PROPORTIONAL.md)). Outline: `U, V` coprime make `H_j` a strong divisibility sequence, `gcd(H_i, H_j) = H_gcd(i,j)` (Euclid on `H_i = U^(i−j)H_j + V^j H_(i−j)`). Since `e | r, s`, `E | H_r, H_s`, hence `E | K`; `G_u(k) = H_M/H_r` divides `H_M/E` and `G_v(ℓ) = H_N/H_s` divides `H_N/E`, so their gcd divides `H_h/E`, and (5) gives `g | J·H_h`. Both `g` and `H_h` are coprime to 6, giving (6). `H_L/H_h` is a geometric sum with first term `U^(L−h)` and at least one further positive term (`L ≥ 2h`), so it exceeds `U^(L−h)`; and `h ≤ min(M, N)` gives `L − h ≥ max(M, N) ≥ L/2`. This proves (7), and (8) follows.

## Lean

`lean/CycleSpectrum.lean`, Lean unit C002-b part 1 (legacy `lean/STATE.md`), section `Proportional`:

- `LeanLane.Cyc.E_dvd_commutator`: `E | K` for proportional blocks.
- `proportional_gcd_dvd`: (6), with `K = E·J` given as a hypothesis and **any** factorisation `|J| = 2^α·3^β·J_0` (so `J_0` is at least the prime-to-6 part; the exact prime-to-6 part is one instance).
- `proportional_den_lower`: (7), for `K ≠ 0`, as the three inequalities `U^(L−h) < den(w)·J_0`, `U^max(rk, sℓ) < den(w)·J_0` and `U^L < (den(w)·J_0)²`.
- `proportional_rectangle`: (8).
- Ingredients: `gcd_dvd_K_mul_gcd` ((5), Lean unit C002-a) and `gcd_pow_sub_pow` (strong divisibility).

Hypotheses: positive letters, `u, v ≠ []`, the four proportionality equations, `3^b < 2^a`, `k, ℓ ≥ 1`. The prose's `gcd(a, b) = 1` is not needed. `den w = D_w/gcd(C_w, D_w)`. Axioms: `propext`, `Classical.choice`, `Quot.sound` (receipts `lean/receipts/CycleSpectrum.*`, all 742 theorems printed at that build).

## Remarks

- **The half-exponent is sharp** (written, not formalised; `PROPORTIONAL.md` §3). For `u = (1,3)`, `v = (3,1)`: total 4, length 2, `C_u = 5`, `C_v = 11`, `K = 42`; in reduced notation `(a, b) = (2, 1)`, `(r, s) = (2, 2)`, `U = 4`, `V = 3`, `E = 7`, `J = 6`, `J_0 = 1`. For `k = ℓ = t`, `den(u^t v^t) = 7·(16^t + 9^t)`. The word `(1,3)^t (3,1)^t` has exactly one factor `(3,3)`, so it is primitive, and its denominator is of order `U^(L/2) = 4^(2t)`: the exponent 1/2 in (7) cannot be increased uniformly. Checked for `t ≤ 40` by the side lane.
- **Equal block totals.** For `r = s` the key step is the exact identity `gcd(G_u(k), G_v(ℓ)) = (U^(r·gcd(k,ℓ)) − V^(r·gcd(k,ℓ)))/(U^r − V^r)`. The proof also covers `r ≠ s`, where a direct equal-base substitution would be invalid.
- **Scope.** This is a fixed-pair theorem: a finite verification rectangle for each fixed noncommuting pair, not a uniform finite layer over all varying pairs with different totals. For distinct equal-total words and at least three blocks the uniform statement is [`equal-total-two-block-exclusion`](equal-total-two-block-exclusion/README.md). The degenerate case `K = 0` (common primitive word; actual `d = 5, 7, 13` controls `u = v = (1,2,2), (1,3), (4)`) is claim 4 of [`repeated-block-cancellation-bound`](repeated-block-cancellation-bound/README.md). Unequal slopes: [`unequal-slope-two-block-growth`](unequal-slope-two-block-growth/README.md).
- **Novelty.** Trümper (2014) contains the concatenation, commutator and repetition formulas; the specific proportional-slope cancellation bound is derived here, and priority and novelty are not claimed.

## History

- Split from `experiments/cycle_spectrum/C002/` (legacy ID `C002`; `REPORT.md` §2, `PROPORTIONAL.md` §§1–3) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
- Corrected before delivery: the first sharpness example used full block totals rather than the reduced slope, and removed the factor 7 before proving coprimality to 7 (see `INDEPENDENT_REVIEW.md` §1 in the C002 folder). Formalised by the Lean lane as C002-b part 1, 2026-10-19, iteration 91.
