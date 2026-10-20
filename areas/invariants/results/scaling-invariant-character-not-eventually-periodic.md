---
id: scaling-invariant-character-not-eventually-periodic
kind: result
title: A binary-automatic character invariant under doubling and tripling need not be eventually periodic
status: written
claim: >
  Let chi be the character modulo 8 with chi(m) = +1 for m = 1, 3 and -1 for m = 5, 7 (m odd), and g(n) =
  chi(oddpart(n)) on the positive integers, g(0) = g(1). Then g is 2-automatic and satisfies g(2n) = g(3n) = g(n),
  every pure-zero ternary section g(3^t n) equals g, yet g is not eventually periodic and the sections
  n -> g(3^t n + 1), t >= 1, are pairwise distinct (so its ternary kernel is infinite). It is not a 3x+1 invariant
  (g(3) = +1, g(10) = -1). So binary automaticity plus the two scaling invariances, without the guarded additive
  identity h(3n+1) = h(n), do not imply eventual periodicity or a finite ternary kernel.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
evidence:
  - "../digit-count-invariant-colourings-constant/literature.md, section L6: the construction and both proofs"
  - "../digit-count-invariant-colourings-constant/verify_examples.py: V003's bounded replay includes the scaling control (key scaling_control of its receipt: exact witnesses for mixed-section pairs and non-periods)"
aliases: [V003-c]
tags: [invariants, automatic, counterexample, ternary-sections, controls]
---

# A binary-automatic character invariant under doubling and tripling need not be eventually periodic

## Statement

Write `n = 2^v m` with `m` odd and put

```
chi(m) = +1   for m ≡ 1 or 3 (mod 8),
chi(m) = −1   for m ≡ 5 or 7 (mod 8),
g(n) = chi(oddpart(n)),     g(0) = g(1) = +1.
```

Then `g` is 2-automatic and `g(2n) = g(3n) = g(n)`; every pure-zero ternary section `g(3^t n)` equals `g`. Nevertheless `g` is **not eventually periodic**, and the mixed sections `n ↦ g(3^t n + 1)`, `t ≥ 1`, are **pairwise distinct**. The full Collatz guard excludes it: `g(3) = +1` but `g(10) = −1`.

## Proof

From [`literature.md`](digit-count-invariant-colourings-constant/literature.md#l6-two-scaling-invariances-do-not-imply-periodicity) §L6 (V003).

**Automatic and scaling-invariant.** For a binary section `g(2^e n + r)`: `r = 0` leaves `g` unchanged; if `r = 2^a u > 0` with `u` odd and `a < e`, the section is `chi(2^(e−a) n + u)`, which modulo 8 gives finitely many functions. Doubling leaves the odd part unchanged; multiplication by 3 permutes `{1, 3}` and `{5, 7}` modulo 8, so `g(3n) = g(n)`. (With `chi = 0` on even integers this is the Dirichlet character modulo 8 associated with −8; the family is a special case of Konieczny–Lemańczyk–Müllner, *Multiplicative automatic sequences*, Lemma 8 and Theorem 1, but the example is checked directly.)

**Not eventually periodic.** Let `M = 2^a m`, `m` odd, be a proposed period. Choose `u ∈ {1, 5}` with `chi(u) ≠ chi(m)` and `n = 2^(a+k) u` with `k ≥ 3` arbitrarily large. Then `g(n) = chi(u)`, while `oddpart(n + M) = 2^k u + m ≡ m (mod 8)`, so `g(n + M) = chi(m) ≠ g(n)` beyond any threshold.

**Infinite ternary kernel.** For distinct `t, s ≥ 1` write `Δ = 3^t − 3^s = 2^a D` with `D` odd (possibly negative). Choose `K > a + 3` and, by the Chinese remainder theorem, a positive odd `v` with `2^K v ≡ 1 (mod 3^t)` and `chi(v) ≠ chi(D)` (`v ≡ 1` or `5 (mod 8)`), large enough that `n = (2^K v − 1)/3^t > 0`. Then `g(3^t n + 1) = g(2^K v) = chi(v)`, and `3^t(3^s n + 1) = 3^s 2^K v + Δ = 2^a(3^s 2^(K−a) v + D)`, whose parenthesis is positive, odd and `≡ D (mod 8)`; invariance under multiplication by `3^t` gives `g(3^s n + 1) = chi(D)`, the opposite value. (`t ≥ 1` makes offset 1 a valid ternary-kernel residue.) ∎

## Remarks

- **What it refutes.** Only a scaling-based completion of the V003 closure argument ([`binary-kernel-first-ternary-image`](binary-kernel-first-ternary-image.md) §5): a singleton pure-zero ternary orbit and both dilation invariances do not supply eventual periodicity. It does not refute the guarded problem, which was settled by [`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md). It identifies the information that must survive: the guarded additive identity and its effect on the mixed sections.
- `g` has constant binary sections (for example `g(8n+1) = +1`), so it also shows that refuting ternary-kernel finiteness needs no absence of constant sections; compare [`monochromatic-cylinder-forces-constancy`](monochromatic-cylinder-forces-constancy.md).
- Novelty: none claimed; the cited paper supplies the encompassing automatic family, not this Collatz-route counterexample.

## History

- New node by the B16 migration (Claude, Opus 5.5), from the V003 report §3 ("An exact obstruction to dropping the guards") and `experiments/viewpoints/V003/literature.md` §L6 (legacy ID V003) at commit `be73a66`; the note stays in [`digit-count-invariant-colourings-constant`](digit-count-invariant-colourings-constant/README.md)'s folder.
- Main lane (ChatGPT/Codex), 2026-10-18, main commit `2ac44ef`. Main-lane review only.
