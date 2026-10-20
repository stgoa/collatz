# C013 — Independent checker review and saved-receipt replay

**Outcome: PASS.** The reviewer inspected the checker source and its
imported arithmetic helpers, then independently ran the saved-receipt
replay after the author's final write. No source correction was needed.
The reviewer is independent of the checker author; the reviewer did
author OVERLAP_CONTROLS.md, whose separate proof review is recorded in
THEORY_REVIEW.md. This report is not formal verification.

## Final pins and replay

```text
check_overlap.py
911b5adf0688c4e5954f95b3439902db221f118ead0ca7ce45ed7a5d793d84d5

overlap_audit.json
21a5f84c35f8b15ebcbf88597ac50bf2fa68ed719750c079c915ec359fc2ec75

python3 experiments/cycle_spectrum/C013/check_overlap.py --check
Exit status: 0; printed status: PASS.
```

The replay recomputed the receipt and compared the entire parsed JSON
object with the saved file. It did not overwrite the receipt. The
reviewer separately checked the schema, status, checker hash, expected
top-level fields and every recorded source hash against the current
files. All matched.

| Input | SHA-256 |
| --- | --- |
| C001/actual_cycles.json | `28d067d3f82585a3701616adce3b57cae994541c4ddd3b4859d2bcf2307e44f2` |
| C007/height_denominator_audit.json | `b35a18cb4209b5d0afd104f5c9e38926dc2de5dbef890cc324cf05ae83ce4ceb` |
| C009/check_excursions.py | `a7631d433cd5952d8a27de3eb41addb8d01784da410064fb9e479d5cff3e17cb` |
| C012/check_coupled_system.py | `bb0b9c27fc6ef0b116e302a369b33552f54c2a7efa4d94d4b44be8b9ea5e356c` |
| experiments/phase6/cycle_fixtures.json | `3aeddd6c3eb2f9b4be54aa239b1ebd197fcabd3a215880e4a853470921e01fe2` |

The first four paths are under `experiments/cycle_spectrum/`. These
cover both imported helper modules and all three external data files.

## Source inspection

- The primitive pseudo-remainder algorithm preserves the rational
  polynomial gcd. Independent exact monic division checks both
  quotients, and a second gcd checks their coprimality. The program
  computes every actual polynomial gcd, including noncoprime totals;
  it does not substitute the coprime-totals theorem for that work.
- Homogeneous evaluation uses the correct degree for G, Pbar and
  Qbar. Extraction checks both D and C, then retains the residual
  gcd with E. The Sylvester determinant uses the imported exact
  Bareiss routine. Nonempty controls check the resultant bound and
  the divisibility after stripping its factors 2 and 3.
- The uniform denominator comparison is the exact integer form of
  `q>eta*2^[n(e-1)-d]/Rbound`, with `eta=D/2^A`. It does not use
  floating-point roots, logarithms or asymptotic estimates. Its
  recorded lower-bound floor and flag describe the conservative
  explicit bound actually checked.
- Every maximal agreeing run includes its cyclic seam, and empty
  runs are handled consistently. Nonzero even state differences,
  both endpoint divisibilities, equal integer multipliers, actual
  rotation-orbit zero sums, diameter bounds and the height-dependent
  denominator bound are checked. B is computed exactly from H/L.
- Reduced q and scaled raw d are kept separate. All original raw
  arrows and all eleven designated fixtures are replayed. Fixed
  points and repeated `(2)` remain allowed, and are excluded from
  the nonconstant-marker bound where required.
- The near-critical controls verify the stated finite domains,
  primitivity, all rotation distances, affine equations, post-marker
  minima and finite height inequalities. Their receipt explicitly
  leaves asymptotic limits, balanced subsequences and unboundedness
  to the written proof.

## Verified coverage and scope

| Check | Replayed count |
| --- | ---: |
| Source cycle instances across 333 parameters | 2,459 |
| Combined normalized cycles | 1,185 |
| Raw source arrows | 36,912 |
| Exact actual polynomial gcds | 1,185 |
| Noncoprime-total polynomial cases | 762 |
| Actual nonconstant polynomial common factors | 20 |
| Nonidentity rotations / Fourier inequalities | 27,646 |
| Rotation-orbit zero sums | 75,577 |
| Maximal agreeing runs, including empty runs | 969,102 |
| Positive-length agreeing runs | 334,590 |
| Empty-background uniform bounds | 1,177 |
| Fixed points outside the nonconstant-marker theorem | 8 |
| Structured stress words, all primitive | 243 |
| Near-critical upper-pair controls | 3 |
| Nonempty long backgrounds with certified lower bound greater than one | 4 |

All 243 structured candidate tests are already implied by their
existing denominators. The checker labels them nondiscriminating
and does not present those passes as new support for the proposed
unrestricted cancellation bound. The four positive quantitative
controls use background lengths 50 and 100 for each of the two
specified marker patterns; they exercise a nonvacuous instance of
the shared-background estimate, not arbitrary sparse rotations.

The primitive six-marker example retains its nonconstant polynomial
factor. The actual q5 period-17 control retains polynomial gcd one
and numerical gcd 1,015,513. Negative full-D backgrounds are
explicitly excluded. These controls guard the distinctions used in
the written argument.

No asymptotic result, imported logarithm theorem, unrestricted cycle
exclusion or novelty claim is inferred from this finite replay.
