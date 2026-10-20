---
id: rise-lemma-denominator-law
kind: result
title: "A denominator law exponential in the mismatch count, for every rotation (the rise lemma's word form)"
status: reviewed
claim: >
  For every primitive positive valuation word w (period m, total A, D = 2^A − 3^m > 0, letters ≥ 1) with
  rational cycle x_p, log-height B = log₂(max x/min x) and minimum x_min, put κ_w = log₂3 + 1/(3x_min·ln 2),
  η = 1/(3x_min·ln 2), σ = log₂3 − 1 and λ(w) = log₂(m·2^A/(3D)). Then every rotation 0 < h < m, coprime to m
  or not, with s mismatches satisfies log₂ den(w) ≥ B/(κ_w^(s+1) − 1) − 1 − (σ + η)·|h|_m − λ(w).
  No gap, period or L/q hypothesis.
authors:
  - Claude side lane (Opus)
created: 2026-10-19
depends_on: [rise-lemma]
evidence:
  - "Checked by ../rise-lemma/s13_rise_lemma.py on exhaustive primitive words ({1,2,3}, m ≤ 9; {1,…,4}, m ≤ 7; 6,008 words, 39,512 checks, minimum margin 5.57 bits); see that node"
reviewed_by:
  - by: Claude Lean lane (Fable)
    date: 2026-10-19
    scope: "Feed S13 entry, update 17:40: adversarial review of S13 §§1-2 with no hole found; the uniform-Δ form of the lemma 'suffices for Corollaries 1-4'. The corollary's own algebra is not formalised"
    link: ../../../archive/side-lane/FEED.md
tags: [cycles, denominator, rise-lemma, 3x+d]
---

# A denominator law exponential in the mismatch count, for every rotation (the rise lemma's word form)

## Statement

Legacy S13 note, Corollary 4 (word form, any `q`). For a primitive positive word `w` with `D > 0`, take its rational cycle `x_p`, with height `B` (log₂ of the ratio of its largest to smallest element) and minimum `x_min`. Put `κ_w = log₂3 + 1/(3x_min·ln 2)`, `η = 1/(3x_min·ln 2)`, `σ = log₂3 − 1` and `λ(w) = log₂(m·2^A/(3D))`. For every rotation `h` with `s` mismatches,

```
log₂ den(w) ≥ B/(κ_w^(s+1) − 1) − 1 − (σ + η)·|h|_m − λ(w).
```

## Proof

The integer cycle `den(w)·x_p` is an odd cycle of `3x + den(w)` with the same profile, minimum `L = den(w)·x_min`, and `η = den(w)/(3L·ln 2) = 1/(3x_min·ln 2)`. Corollary 1 of [`rise-lemma`](rise-lemma/README.md), with `Δ = (σ + η)·|h|_m`, gives `B ≤ (κ^(s+1) − 1)(log₂ L + 1 + (σ + η)|h|_m)`, so `log₂ L ≥ B/(κ^(s+1) − 1) − 1 − (σ + η)|h|_m`. Finally `L ≤ m·q·2^A/(3D)` (S7's (F4), Lean `three_L_D_le`), that is `log₂ L ≤ log₂ den(w) + λ(w)`.

## Remarks

- This is the programme's third denominator law, after S9 ([`two-three-mismatch-denominator-laws`](two-three-mismatch-denominator-laws/README.md)) and S12 ([`denjoy-koksma-denominator-law`](denjoy-koksma-denominator-law/README.md)). It is exponential in `s`, where S12's is linear in `K(h/m)`, and it holds for every rotation, coprime or not.

## History

- Split from `experiments/cycle_spectrum/S13/RISE_LEMMA.md` §1, Corollary 4 (legacy ID `S13`; side-lane producer batch S13, 2026-10-19) at commit `be73a66`, by the B06 migration (Claude, Opus 5.5). The proof paragraph expands the note's one-line justification ("the integer cycle `den(w)·x_p` is an odd cycle of `3x + den(w)` with the same profile") with the steps it names.
- Side lane (Claude, Opus), feed 2026-10-19 17:32 (LEAD, S13, Corollary 4). Reviewed with the rest of §§1–2 by the Lean lane at 17:40.
