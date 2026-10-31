---
id: saturated-sets-meet-residue-classes-small-moduli
kind: result
title: "Every saturated set of the 3x+1 map meets every residue class modulo every M ≤ 100"
status: written
claim: >
  Let T be the Collatz map on the positive integers (n → n/2 for even n, n → 3n+1 for odd n) and B a nonempty set
  with x ∈ B iff T(x) ∈ B (a union of orbit components, closed under T and under all inverse branches). Then for
  every modulus 1 ≤ M ≤ 100 and every residue r, B contains an element ≡ r (mod M). Proof: B contains an odd
  element and is closed under x → 2x, x → x/2 (x even), x → 3x+1 (x odd) and x → (x−1)/3 (x ≡ 4 mod 6); tracking
  residues modulo 2^(a_M+a)·3^(b_M+b)·M′ (M = 2^(a_M)3^(b_M)M′, a = halvings and b = inverse steps still allowed),
  a backward search shows that from every odd start class every class modulo M is reached, with at most 1 halving
  and at most 6 inverse steps (6 only for M ∈ {56, 64, 80}; powers of two 2^k need exactly k − 1 inverse steps for
  2 ≤ k ≤ 6, powers of three need one halving and one inverse step, odd M need one halving and at most 4 inverse
  steps). The same search run for the 3x+5 map fails at M = 5 for every budget, as it must (the multiples of 5 form
  a saturated set of 3x+5 that misses every other class). Nothing is claimed for M > 100, and no uniform bound on the number of inverse steps
  is proved.
authors:
  - Claude cycles lane (Fable 5.1; directed by Santiago Armstrong)
created: 2026-10-31
depends_on: []
certificates: [check_residue_closure.py]
evidence:
  - "residue_closure.json: the receipt; V1 the least budget (halvings, inverse steps) for every M ≤ 100, V2 the 3x+5 control"
tags: [invariants, residues, saturated-sets, orbit-components, finite-closure, profinite]
---

# Every saturated set of the `3x+1` map meets every residue class modulo every `M ≤ 100`

## Statement

Let `T` be the Collatz map on `Z_(>0)` and call `B ⊆ Z_(>0)` **saturated** if `x ∈ B ⟺ T(x) ∈ B`: `B` is a union of connected components of the Collatz graph, closed under the forward map and under every inverse branch (the question [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md) calls these unions of orbit components; `1` may or may not be in `B`).

**Theorem.** For every nonempty saturated `B`, every `1 ≤ M ≤ 100` and every residue `r (mod M)`, `B` contains an element `≡ r (mod M)`.

**The moves.** Saturation gives four moves that stay inside `B`: `x → 2x` (since `T(2x) = x`), `x → x/2` for even `x` (`T(x)`), `x → 3x + 1` for odd `x` (`T(x)`), and `x → (x − 1)/3` when `x ≡ 4 (mod 6)` (then `(x − 1)/3` is an odd positive integer with `T((x − 1)/3) = x`). Also `B` contains an odd element: halve any element until it is odd.

**Residue bookkeeping.** Write `M = 2^(a_M)·3^(b_M)·M′` with `gcd(M′, 6) = 1`. Knowing `x` modulo `L = 2^α·3^γ·M′` with `α, γ ≥ 1` determines `2x (mod L)`, whether `x` is even, `x/2 (mod L/2)`, `3x + 1 (mod L)`, whether `x ≡ 4 (mod 6)`, and `(x − 1)/3 (mod L/3)`. So after `i` halvings and `j` inverse steps from a start known modulo `L(0, 0) = 2^(a_M + a)·3^(b_M + b)·M′`, the element is known modulo `L(i, j) = 2^(a_M + a − i)·3^(b_M + b − j)·M′`, which still determines its class modulo `M` as long as `i ≤ a` and `j ≤ b`. Doublings and forward steps are free.

**The computation.** For each `M`, and the least budget `(a, b)` in the order of `a + b`, a backward search over the finite graph of states `(i, j, c mod L(i, j))` shows that from **every odd** start class `c (mod L(0, 0))` every target class `r (mod M)` is reachable. The least budgets found:

| `M` | budget `(a, b)` |
|---|---|
| `2^k`, `k = 1..6` | `(0, k − 1)` for `k ≥ 2`, `(0, 0)` for `k = 1` |
| `3^k`, `k = 1..4` | `(1, 1)` |
| odd `M` (50 moduli) | one halving (except `M = 1`), at most 4 inverse steps |
| even `M` (50 moduli) | no halving, at most 6 inverse steps (`56, 64, 80`) |
| all `M ≤ 100` | `a ≤ 1`, `b ≤ 6` |

Full table in [`residue_closure.json`](residue_closure.json).

**Control.** For the `3x+5` map (forward `x → 3x + 5`, inverse `x ≡ 2 (mod 6) → (x − 5)/3`) the multiples of 5 form a saturated set that misses every class `≢ 0 (mod 5)`, so the analogous statement is false at `M = 5`; the same search indeed fails there for every budget `a, b ≤ 4` (and proves `M = 2`, where nothing obstructs). The method is therefore not vacuous: it distinguishes `d = 1` from `d = 5` exactly where the statement does.

## Proof

Fix `M ≤ 100` and a nonempty saturated `B`. Take an odd `x_0 ∈ B` and let `c_0` be its class modulo `L(0, 0)`, an odd class. The certificate's search exhibits, for every target `r`, a sequence of moves from the state `(0, 0, c_0)` to a state whose class is `≡ r (mod M)`; applying the same moves to `x_0` gives elements of `B` (each move preserves `B`), and the residue bookkeeping above shows the final element is `≡ r (mod M)`. Since the search succeeds from every odd start class, it does not matter which odd element `B` contains. The search is exhaustive over the finite state space and is re-run by the certificate.

## Certificates

[`check_residue_closure.py`](check_residue_closure.py) (standard library, about 12 s): **V1** for each `M ≤ 100` the least budget `(a, b)`, `a, b ≤ 6`, with which the backward search succeeds from every odd start class (failing for all budgets would fail the certificate); **V2** the `3x+5` control; **V3** the receipt [`residue_closure.json`](residue_closure.json) (`--write-receipt` regenerates it). Finite statements only.

## Remarks

- **What it says about the question.** [`invariant-sets-meet-every-residue-class`](../../questions/invariant-sets-meet-every-residue-class.md) asks the statement for all `M`; this is the first positive evidence beyond the periodic classification, and the method is a proof for each individual `M` it handles. It does not give the general case: the budgets grow with the 2-adic part of `M` (`2^k` needs `k − 1` inverse steps), because each inverse step with a small exponent fixes one more binary digit of the element reached, while large exponents all land in the single class `−1/3 (mod 2^k)`. A general proof would have to show that these digit-by-digit constructions never get stuck; the computation shows they do not for `k ≤ 6`.
- **Heuristic reading (labelled).** The uniform `(1, 1)` budget for powers of three reflects that 2 is a primitive root modulo `3^k`: doubling an odd `3 ∤ x` reaches every unit class modulo `3^(k+1)`, and one inverse step `(2^t x − 1)/3` then reaches every class modulo `3^k`. The 2-adic side has no such generator (doubling kills 2-adic information), which is why inverse steps with small exponents are needed there. A proof for all `M` might combine the two mechanisms with the forward step `3x + 1`, which mixes 2-adically.
- **Scope.** `3x+1` only; the `3x+d` controls fail the statement whenever `d > 1`, since the multiples of `d` are saturated for `3x+d`. The theorem is about every saturated set at once, so it holds for the component of 1 and for the component of any hypothetical divergent orbit or nontrivial cycle. Novelty undetermined; the question's card expected "a bounded computation plus a V13-style argument", and this is the bounded computation.

## History

- Written 2026-10-31 by the Claude cycles lane (Fable 5.1), directed by Santiago Armstrong, as the first attack on the side lane's question S2.
