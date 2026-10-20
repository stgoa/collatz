---
id: ordered-cycle-residue-law
kind: result
title: Cycle numerators are units mod 6q, normalised residues forget heights, and the min–top inequality
status: formal
claim: >
  Raw odd-only 3x+q map, q odd, coprime to 6. For a cycle 3n_i + q = 2^(a_i)·n_(i+1) (a_i ≥ 1) with
  reduced numerators (gcd of all n_i equal to 1), started at n_0 = L = min n_i: every n_i is coprime to
  6q; with h_i = floor(log₂(n_i/L)), c_j = a_j + h_(j+1) − h_j and P_i = Σ_(j<i) c_j, the normalised
  mantissas satisfy z_i = n_i/2^(h_i) ≡ L·3^i·2^(−P_i) (mod q) for q > 1, independently of the height
  profile. If the cycle is ordered (sorted F increases with sorted z), every state n_j at height
  h_j ≥ 1 satisfies 3(n_j − 2^(h_j)·L) > q(2^(h_j) − 1).
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [dyadic-order-lemma]
lean:
  - LeanLane.Cyc.OddCycle.residue_law
  - LeanLane.Cyc.OddCycle.three_not_dvd
  - LeanLane.Cyc.OddCycle.dvd_succ_of_dvd
  - LeanLane.Cyc.OddCycle.dvd_all_of_dvd
  - LeanLane.Cyc.OddCycle.min_top
evidence:
  - "../questions/height-denominator-candidate/HEIGHT_DENOMINATOR.md, sections 2-3: the written proofs"
  - "../questions/height-denominator-candidate/INDEPENDENT_ARITHMETIC.md: independent main-lane review of the lemma (equation (A1) is the min-top inequality)"
  - "../questions/height-denominator-candidate/arithmetic_obstructions.json: 28,830 modular arrows checked on the 1,185 normalised cycles (historical receipt; its checker no longer runs at the new path)"
  - "../questions/height-denominator-candidate/c007_height_check.py, part (3): side-lane check of the modular identity"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed 2026-10-19 02:41, update 02:53: the Lean lane re-derived the modular lemma, the min-to-top inequality and the q = 5 height-residue sets with no error; Lean unit C007-a verified (update 02:46, iteration 21)"
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 02:28, REFEREE C007: the modular identity holds at all 28,823 states of every normalised census cycle with q > 1; feed 02:46: C007-a statement match and receipts checked"
tags: [cycles, residues, dyadic-order, formal]
---

# Cycle numerators are units mod 6q, normalised residues forget heights, and the min–top inequality

## Statement

Write a primitive positive rational `S_1` cycle as a reduced positive odd numerator cycle

```
3n_i + q = 2^(a_i)·n_(i+1),   a_i ≥ 1,   gcd(n_0, …, n_(m−1)) = 1,
```

with reduced odd denominator `q` coprime to 6, started at `n_0 = L = min n_i`, with `h_i`, `z_i = n_i/2^(h_i)`, `c_i` as in [`dyadic-order-lemma`](dyadic-order-lemma.md) and `P_i = Σ_(j<i) c_j`.

1. **Units.** Every numerator `n_i` is coprime to `6q`.
2. **Modular lemma.** For `q > 1`, in `Z/qZ`,

```
z_i = 2^(−h_i)·n_i ≡ L·3^i·2^(−P_i)   (mod q),          (2)
```

so the complete normalised residue orbit depends on `c`, `L mod q` and `i`, but **not** on the height profile.
3. **Min–top inequality.** If the cycle is ordered, every state `N` in height band `h ≥ 1`, written `N = 2^h·L + r` (`r` positive and odd), satisfies

```
3r > q(2^h − 1),    0 < r < 2^h·L.                       (3)
```

## Proof

[`HEIGHT_DENOMINATOR.md`](../questions/height-denominator-candidate/HEIGHT_DENOMINATOR.md) §§2–3. Numerators are odd by construction; reducing a predecessor equation mod 3 gives `2^(a_i)·n_(i+1) ≡ q (mod 3)`, so 3 divides no numerator; a prime `p | q` dividing one numerator divides its successor (2 is invertible mod `p`), hence all numerators, contrary to reduction. The normalised arrow is `2^(c_i)·z_(i+1) = 3z_i + q·2^(−h_i)`; reduce mod `q` and iterate from `z_0 = L`. For (3), compare `N`'s normalised image with that of the minimum: `F(N) − F(L) = [3r − q(2^h − 1)]/2^h`, which is positive by order (an instance of the inversion formula).

## Lean

`lean/CycleSpectrum.lean`, Lean unit C007-a, on the `OddCycle` structure (odd periodic numerators with `n_0` the positive minimum, exact arrows, heights):

- `LeanLane.Cyc.OddCycle.residue_law`: `2^(P_i)·Z_i ≡ 3^i·Z_0 (mod q)` for the scaled normalised states `Z_i = 2^(B−h_i)·n_i`; this is (2) in integer form, after inverting the powers of 2 modulo the odd `q`. It holds for every `q > 0`; neither order nor heights enter.
- `three_not_dvd`: `3 ∤ q ⇒ 3 ∤ n_i`; `dvd_succ_of_dvd`, `dvd_all_of_dvd`: a divisor of `q` coprime to 2 that divides one numerator divides all, so a reduced cycle has numerators coprime to `q`. With oddness this is claim 1.
- `min_top`: under the order hypothesis `Z_i < Z_j ⇔ F_i < F_j`, every state with `Z_0 < Z_j` satisfies `q(2^(h_j) − 1) < 3(n_j − 2^(h_j)·n_0)`; at `h_j ≥ 1` this is (3).

Axioms `propext`, `Classical.choice`, `Quot.sound` (`three_not_dvd`: `propext`, `Quot.sound`); receipts `lean/receipts/CycleSpectrum.*`.

## Remarks

- **What it shows about the candidate `B ≤ q − 1`.** (2) exposes a limit of a simple residue argument: residues at different height levels need not be disjoint, and (3) is compatible with `q ≤ L` for every `B ≥ q`. Neither proves or refutes [`height-denominator-candidate`](../questions/height-denominator-candidate/README.md); see [`height-bound-via-residues-or-relaxation`](../attempts/height-bound-via-residues-or-relaxation.md). The scope of "normalisation erases heights modulo `q`" is residues for a **fixed normalised word** `c`; heights are not erased from integer order inequalities or from `C_h`.

## History

- Split from `experiments/cycle_spectrum/C007/` (legacy ID `C007`; `HEIGHT_DENOMINATOR.md` §§2–3, `REPORT.md`) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19. Formalised by the Lean lane as C007-a, iteration 21.
