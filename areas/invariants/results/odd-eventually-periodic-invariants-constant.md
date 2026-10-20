---
id: odd-eventually-periodic-invariants-constant
kind: result
title: A 3x+1 invariant colouring whose odd values are eventually periodic is constant
status: formal
claim: >
  Let h be any colouring of the nonnegative integers (any colour set) with h(2n) = h(n) for all n and
  h(3n+1) = h(n) for odd n > 1. If n -> b(n) = h(2n+1) is eventually periodic (there are N and M > 0 with
  b(n+M) = b(n) for n >= N), then h(n) = h(1) for every n > 0. This strictly strengthens the periodic case of
  periodic-invariant-colourings-classification at d = 1. Elementary: no automaticity or Cobham.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: []
lean:
  - LeanLane.OddEP.odd_eventually_periodic_const
  - LeanLane.OddEP.period_of_eventually
  - LeanLane.OddEP.B1
  - LeanLane.OddEP.B2
  - LeanLane.OddEP.B4
evidence:
  - "binary-automatic-invariant-colourings-constant/README.md section 5: the written proof; its v004_rigidity_check.py part (c) checks that H o J - J o H = -1/4 is a unit for the 666 moduli m <= 2000 coprime to 6"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-18
    scope: "Feed 20:49: Lean V004-i read from source and receipts; statement match confirmed, and the Lean proof's different route (integer identities, period 3K to K, translation by 1/2) checked by hand"
    link: ../../../archive/side-lane/FEED.md
aliases: [V004-c]
tags: [invariants, colourings, periodic, rigidity, formal]
---

# A 3x+1 invariant colouring whose odd values are eventually periodic is constant

## Statement

Let `h(2n) = h(n)` for all `n` and `h(3n+1) = h(n)` for odd `n > 1`, with an arbitrary colour set. If `b(n) = h(2n+1)` is eventually periodic, then `h` is constant on the positive integers.

## Proof

The written proof is §5 of [`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md). By `h(4x+1) = h(3x+1) = h(x)` for positive odd `x`, `b(4n+2) = b(n)`. Let `M = 2^e L` (`L` odd) be an eventual period and `G(n) = 4n + 2`; for any `n`, choose `k` with `G^k(n)` past the cutoff and `2^e | 4^k`; the indices `G^k(n+L)` and `G^k(n)` differ by `4^k L`, a multiple of `M`, so `b(n+L) = b(n)`: `L` is a global period. Then `h(x) = q(x mod L)` for odd `x`, with `q(4x+1) = q(x)` and `q(3x) = q(16x+1) = q(4x)` on every residue. With `H(x) = 3·4^(−1) x` and `L = 3^(e3) m`, `gcd(m, 6) = 1`, `q` factors through `m`; on `Z/mZ` the maps `H` and `J(x) = 4x + 1` preserve `q` and `H(J(x)) = 3x + 3/4`, `J(H(x)) = 3x + 1`, so `q(y) = q(y + 1/4)` for every `y`, and the unit `1/4` generates `Z/mZ`. Hence `q` is constant, so `h` is constant on odd positive integers and, by doubling, on all positive integers. ∎

## Lean

Lean unit V004-i, [`lean/OddEventuallyPeriodic.lean`](../../../lean/OddEventuallyPeriodic.lean) (receipts `lean/receipts/OddEventuallyPeriodic.*`; axioms `propext`, `Classical.choice`, `Quot.sound`; `B1`, `B2`, `B4` only `propext`, `Quot.sound`), namespace `LeanLane.OddEP`: `odd_eventually_periodic_const` takes `0 < M`, `∀ n ≥ N, h(2(n+M)+1) = h(2n+1)` and the two colouring rules, and concludes `∀ n > 0, h n = h 1`. **Statement match:** exact; the hypotheses never constrain `h 0` (doubling at 0 is trivial), and no finiteness of the colour set is needed. The Lean route differs in form (integer identities `b(4n+2) = b(n)`, `b(3n+2) = b(2n+1)`, `b(4n) = b(3n)` (`B4`, `B2`, `B1`) instead of the residue map on `Z/LZ`; period `3K ⇒ K` by strong induction (`period_div_three`) instead of the `H^(e3)` descent; translation by `c = (L+1)/2`, i.e. by 1/2, instead of 1/4), but uses only consequences of the colouring rules and reaches the same statement. `period_of_eventually` is the eventual-to-global step.

## Remarks

- This is the elementary half of V004; Cobham's theorem enters only to make `b` eventually periodic ([`binary-automatic-invariant-colourings-constant`](binary-automatic-invariant-colourings-constant/README.md)).
- **Controls.** For `d = 5` or `61`, `1_{d|n}` is periodic, invariant and nonconstant: the `d`-version of the commutator translates by `d/4 ≡ 0 (mod d)` and cannot force constancy ([`periodic-invariant-colourings-classification`](periodic-invariant-colourings-classification/README.md)).

## History

- New node by the B16 migration (Claude, Opus 5.5) from §§2 and 5 of `experiments/viewpoints/V004/GLOBAL_RIGIDITY.md` (legacy ID V004) and the Lean unit V004-i in the legacy `lean/STATE.md`, at commit `be73a66`.
- Main lane (ChatGPT/Codex), 2026-10-18; Lean V004-i verified 2026-10-18 (Lean lane iteration 2, `claude/lean-lane` `d1e5b23`; side-lane check, feed 20:49).
