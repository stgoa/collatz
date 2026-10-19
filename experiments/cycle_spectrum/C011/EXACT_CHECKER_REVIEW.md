# C011 — Independent checker and coupled-control review

**Status: source review and independent exact replay PASS.** Reviewed on
2026-10-19. This records finite arithmetic checks and the scope of the
review; it is not formal verification or an independent verification of
the imported analytic bounds used elsewhere in C011.

## Correction found and resolved

The first draft of `GENERAL_DEFECTS.md` omitted the factor
`2^abs(delta)-1` from its description of a constant-discrepancy plateau.
It also described the isolated arc itself as divisible by g, where the
unconditional conclusion is divisibility of `(2^k-1) C_arc`.
The issue was reported before acceptance and the author corrected both
sentences. The exact checkers and `ROTATION_DEFECTS.md` already retained
the factor; they required no correction.

For a plateau indexed by `a<=j<=b` with constant discrepancy delta,
factoring the intercept sum gives exactly

```
sign(delta) * 2^min(P_a,P'_a) * 3^(m-1-b)
    * (2^abs(delta)-1) * C_(w_a,...,w_b).
```

This also checks negative discrepancies without negative integer powers.
The final letter of the displayed arc is unused in its intercept, as in
the other C011 arc formulas. Since g is coprime to 6, powers of 2 and 3
may be removed from a divisibility statement. The remaining factor
`2^abs(delta)-1` requires its own coprimality argument if it is removed.

## New coupled-control checker

The complete source of `check_coupled_defects.py` was reviewed. The
following fresh replay completed with exit code 0 and `status: PASS`:

```
python3 experiments/cycle_spectrum/C011/check_coupled_defects.py
```

The checker recomputes weighted intercepts from the words, verifies
positive D and the expected gcd and reduced denominator, computes the
prefix discrepancies and every maximal nonzero plateau, and checks
both their sum and their nonzero individual residues modulo g. It
explicitly checks divisibility of every rotated intercept by g before
division. Thus the constructed integer states are exact quotients.
Every prescribed raw odd-only arrow is then verified, including the
closing arrow. Positive odd output states make each prescribed
valuation exact, and pairwise distinct states establish primitive
period. Stored-corpus membership is checked up to cyclic rotation.

The complete output is compared with the persisted receipt, including
the checker and actual-corpus source hashes. No receipt was regenerated
by this reviewer.

| q | g | Mismatches | Plateau residues modulo g | Full difference / g |
| --- | --- | --- | --- | --- |
| 97 | 5 | 3 | 1, 4 | 20 |
| 233 | 7 | 4 | 6, 1 | 1332 |
| 359 | 73 | 6 | 23, 19, 3, 28 | 284 |

An additional read-only calculation checked every rotated-intercept
quotient directly and compared the words with the actual source rows,
using the same rotation as the state comparison. For q97 the word
`(2,4,3)` rotates by two positions to the source word `(3,2,4)`;
matching source rows occur at d97, d485 and d679, with scalings 1, 5
and 7. The q233 and q359 words match their d233 and d359 rows without
rotation or scaling. These are stored actual cycles, not unattested
affine loops.

The corrected general identity and these controls support precisely
the failure of termwise divisibility outside the two-defect case.
They do not refute estimates that retain the coupled sums at all cuts.

## Original rotation-defect checker

The complete source of `check_rotation_defects.py` was reviewed, with
the remaining source read during this review. Its exact replay had
already completed independently with exit code 0 and `status: PASS`:

```
python3 experiments/cycle_spectrum/C011/check_rotation_defects.py
```

The current checker and receipt hashes are identical to those of that
completed replay; a second full replay was not needed. Source review
covered direct intercept construction, rotations, the extra factor in
the exact cut gcd, both oriented arcs and endpoint adjustments, all
three quadratic bounds, actual-cycle normalization, generated controls,
repeated-word handling, the marker family, rejection controls, source
pins and full receipt comparison. The checker reuses the C009
certificate/step helpers; this is source review and execution of the
checker, not an independently implemented second census.

The completed replay checked 1,185 normalized actual cycles and 28,831
normalized arrows, including 27,646 nontrivial rotations. It found 192
two-defect rotations in 108 cycles. All 192 passed the weak,
endpoint-adjusted and amplitude-free quadratic bounds; the two oriented
arcs supplied 384 identities. The finite controls also covered 51
generated family words, eight marker examples, 11 fixtures and four
rejection controls. It retained 2,494 rotations with an extra factor in
the single-cut gcd and two actual rotations with an extra factor in the
combined two-arc gcd. Thus neither gcd was silently identified with g.

The reviewer authored `ROTATION_DEFECTS.md` and supplied two of the new
coupled controls. This note therefore does not count as an independent
review of that authored theorem or an independent discovery of those
examples. It does provide independent source review and execution of
the checkers written by other agents, and review of the assembled
`GENERAL_DEFECTS.md` statement. Published Matveev/Hercher/Barina inputs
and their numerical application are outside this review.

## Final pins

SHA-256 values for the accepted files:

| File | SHA-256 |
| --- | --- |
| `GENERAL_DEFECTS.md` | `c1edc51a9714114c9cd92cc86c90b49031e035d7e392953aa3b1b06083a57ac7` |
| `check_coupled_defects.py` | `6d6cdf4ebdc75bee9b46638bf998748aa89f985c514296f1388f9b959e57a0bb` |
| `coupled_defect_controls.json` | `061810c3261b299f3db1ff941ae6b31498667dd442058a61387a330e97c41f94` |
| `check_rotation_defects.py` | `ba9a2b7fb269d619378c4c7b25d3cb6430e5a8078ea5658e0d81b71ba2d855ad` |
| `rotation_defect_audit.json` | `1eee49577e35bf5f28aac0ba2a572c8a863266575c4a0e2a4babf2f233d9844d` |
| `../C001/actual_cycles.json` | `28d067d3f82585a3701616adce3b57cae994541c4ddd3b4859d2bcf2307e44f2` |

No unresolved error was found in these accepted files within the
reviewed scope. Finite success does not prove an unrestricted rotation
bound, exclude all denominator-1 words, or establish novelty.
