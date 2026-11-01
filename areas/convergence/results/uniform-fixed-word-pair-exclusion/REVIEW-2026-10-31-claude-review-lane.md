# Review of uniform-fixed-word-pair-exclusion

Independent review (Claude review lane, Fable 5.1, directed by Santiago Armstrong) of the claim, the Statement and the legacy proof §§1–6, with the guard taken from [`mixed-rank-growing-blocks`](../mixed-rank-growing-blocks/README.md) (`w ≡ 40529845 (mod 2^26)`).

## What I checked

- Certificates: `python3 tools/run_certificates.py --node uniform-fixed-word-pair-exclusion` exit 0, wall 6.07 s (`check_uniform_pair_recompute.py` PASS, under 1 s; `check_legacy_replay.py` PASS, 6 s).
- Hand derivations. §2: integrality at `n = 0, 1`; `0 < u(n) < w(n)` for all `n ≥ 0` is `β > 0`, `α ≥ 0`, `β < R`, `α ≤ P`; `W5` for all `n` is `β ≡ 5`, `α ≡ 0 (mod 8)`; `R ≡ 5 (mod 8)`. The fixed-valuation criterion for `an + b`: with `e = v₂(a)`, `d = v₂(3b+1)`, the valuation of `3an + 3b + 1` is `d` for every `n` iff `d < e` (for `d > e` the values at `n = 0, 1` differ; for `d = e` the quotient is odd at `n = 0` and even at `n = 1`), the successor is `(3a/2^d, (3b+1)/2^d)` with `v₂` of the slope reduced by `d ≥ 1`, so the maximal fixed word is finite; `S(1) = 1` has valuation 2, so an absorbed member fits the same formula; the constant case has slope 0 against `P·3^j/2^A > 0`. §3: equal affine tails force `α·3^ℓ/2^B = P·3^j/2^A`, hence `ℓ + v₃(α) = j ≤ 11`. §4: the inverse arrow `(2^h a/3, (2^h b − 1)/3)` has exact valuation `h` on the whole domain because `2^h(an + b)` has odd cofactor; the cap (4) because every later inverse step multiplies the slope by at least `2/3` and the final slope must be `≤ P`; deduplication and single witnesses are safe; a fixed word of length `m` from `3u` ends on the maximal fixed path of `3u`, so comparing the two maximal upper paths is complete. §5: the budget (5) from `α = 2^(26 − A + B) 3^(j − ℓ) ≤ 2^26`.
- Own code (scratch `r76_check.py`, a third enumeration: exact inverse length with the total-valuation budget, depth-first, own `v₂`): lower word `(5,2,1,2,1,1,4,2,1,1,3)`, total 23, terminal `(1417176, 855893)`; upper word of length 17, total 25, terminal `(774840978, 467958829)`; a two-point (`n = 0, 1, 2`) fixedness routine reproduces both paths; 3401 nodes visited; the same 43 candidate `(α, β)`; each lower witness replayed on affine states and on the integers `n = 0..3` (with `0 < u(n) < w(n)` and `u(n) ≡ 5 (mod 8)`); `ℓ + v₃(α) = j` on all 43; the 43 maximal upper paths from `3u` meet the parent's 18 upper states in 0 affine states. With `β ≤ R` allowed, the trivial partner `(P, R)` appears as a 44th candidate with `j = ℓ = 0`, so the strict inequality is what removes it. Positive control of the enumeration: an inverse-arrow progression taken from the parent's state `j = 3` (`α = 18874368`, `β = 11399021`, valuation 3) is found with witness `(j, ℓ) = (3, 1)`.
- Scope check: the model excludes mergers whose clock is uniform but whose intermediate valuations depend on `n`. Such mergers exist in nature: on `w ≡ 1681 (mod 2048)` one has `S^4(3w) = S^5(w)` for every member although the maximal fixed words have lengths 3 and 4 (review of [`missing-one-mod-8-pair-domain`](../missing-one-mod-8-pair-domain/README.md)); the node lists exactly this case under "Not excluded".
- Controls: not applicable. The claim is a finite exhaustive statement about valuation words of `3x+1` on one progression; it asserts nothing about cycles or about other `3x+d`.

## What I did not check

- The constructor's node count 1110 (implementation-specific; the certificate reproduces it); the pinned hash of the legacy note (handled by the replay).
- R67's derivation of the guard itself (reviewed separately).

## Findings

1. Statement, hypothesis 1, and the title's "W5 partner" — **imprecision**: `u(n) ≡ 5 (mod 8)` is required for every `n`, which forces `α ≡ 0 (mod 8)`; partners with `α ≡ 4 (mod 8)` whose members alternate residues are outside the model by this hypothesis, not by the search. The Statement is explicit; the title compresses it.
2. §4, "Keeping one lower witness for a candidate reached at different endpoints is also safe" — **imprecision**: safe for the exclusion (the upper test depends only on `(α, β)`), but the receipt's single witness per candidate is then not a complete list of lower mergers; nothing in the claim depends on that list.

No error or gap found; the enumeration is complete within the stated model, and the independent enumeration's count 3401 is reproduced exactly.

## Verdict

HOLDS.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
