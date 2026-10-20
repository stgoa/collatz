---
id: narrow-cycle-spectrum-law
kind: result
title: "Narrow-cycle spectrum of 3x+d: one cycle per coprime (A, m) with 0 < 2^A − 3^m dividing d"
status: reviewed
claim: >
  Raw odd-only 3x+d map, d a positive odd integer, no absorption. Up to cyclic rotation, the
  primitive positive odd integer cycles with H < 2L are in bijection with the coprime pairs (A, m),
  A ≥ m ≥ 1, with 2^A > 3^m and D = 2^A − 3^m dividing d: the cycle has the mechanical word of
  (A, m) and states (d/D)·C_l over the mechanical phases l. At d = 1 only (A, m) = (2, 1), the fixed
  point 1, remains. This classifies the narrow subfamily; it does not solve D | d for arbitrary d.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-19
depends_on: [narrow-cycles-are-mechanical, mechanical-word-exact-denominator]
evidence:
  - "../narrow-cycles-are-mechanical/ROTATION_LATTICE.md, section 3 'Exact narrow-cycle spectrum': the written proof"
  - "../narrow-cycles-are-mechanical/c004_narrow_check.py, part (2): side-lane comparison with the corpus"
reviewed_by:
  - by: Claude side lane (Opus)
    date: 2026-10-19
    scope: "Feed 2026-10-19 01:06, REFEREE C004: 19 coprime pairs (A, m) with 0 < 2^A − 3^m <= 999; for every d <= 999 coprime to 6 all 551 predicted narrow cycles with minimum <= 5000 appear in the C001 corpus, and every narrow cycle in the corpus is predicted; judged a complete, data-verified law for the narrow part of the spectrum"
tags: [cycles, narrow-cycles, mechanical-words, 3x+d, spectrum]
---

# Narrow-cycle spectrum of 3x+d: one cycle per coprime (A, m) with 0 < 2^A − 3^m dividing d

## Statement

Fix a positive odd parameter `d` and consider raw positive odd integer cycles of `n → (3n+d)/2^v₂(3n+d)`. Up to cyclic rotation, every primitive cycle with `H < 2L` arises from exactly one coprime pair `(A, m)` with `A ≥ m ≥ 1`, `2^A > 3^m`, and

```
D = 2^A − 3^m divides d.                                   (10)
```

Its word is the mechanical word `a_j = floor((j+1)A/m) − floor(jA/m)` and its states are `(d/D)·C_l`, where `C_l` ranges through the mechanical phases. Conversely each such pair satisfying (10) gives a positive raw odd cycle of primitive period `m`. This includes `m = 1`, where every fixed cycle has valuation `A ≥ 2`. For the supported domain `gcd(d, 6) = 1` the scaling factor is also coprime to 6. At `d = 1` only `(A, m) = (2, 1)` survives.

The statement classifies this narrow subfamily; it does not enumerate all solutions of (10) for an arbitrary fixed `d`.

## Proof

From [`narrow-cycles-are-mechanical`](narrow-cycles-are-mechanical/README.md): a primitive narrow cycle with `m > 1` has a mechanical word with `gcd(A, m) = 1` and reduced denominator exactly `D`, so it is an integer `3x+d` cycle after scaling exactly when `D | d`. Conversely, R71 ([`mechanical-word-exact-denominator`](mechanical-word-exact-denominator/README.md)) gives `g = 1`, the phase words are distinct rotations when `m > 1`, and the scale `d/D` is odd. Written proof: [`ROTATION_LATTICE.md`](narrow-cycles-are-mechanical/ROTATION_LATTICE.md) §3, "Exact narrow-cycle spectrum".

## Remarks

- **Controls.** At `d = 5`, `(A, m) = (5, 3)` gives the cycle `(23, 37, 29)`; at `d = 13`, `(8, 5)` gives `319, 367, 421, 485, 557`. The actual corpus contains 105 source instances of narrow nontrivial cycles representing 11 normalised cycles, all mechanical with coprime totals and `g = 1` ([`narrow-cycles-are-mechanical`](narrow-cycles-are-mechanical/README.md), Certificates).
- **Not formalised.** The side lane's VERIFIED entries list the narrow spectrum law as not yet formal; the classification and `g = 1` it rests on are formal.
- R71 is [`mechanical-word-exact-denominator`](mechanical-word-exact-denominator/README.md) (legacy `BALANCED_DENOMINATORS.md`); linked at the B12 migration.

## History

- Split from `experiments/cycle_spectrum/C004/` (legacy ID `C004`; `REPORT.md` §1, `ROTATION_LATTICE.md` §3) at commit `be73a66`, by the B03 migration (Claude, Opus 5.5). Main lane (ChatGPT/Codex), 2026-10-19.
