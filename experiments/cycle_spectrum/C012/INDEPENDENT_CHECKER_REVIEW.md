# C012 — Independent checker review and replay

**Final status: source review and independent replay PASS, 2026-10-19.**
One serialization defect was found by the first independent replay,
reported, and repaired before acceptance. No mathematical computation
changed in that repair.

## Failure found before acceptance

The original checker at SHA-256
`caf55dae71c07cbb671f327b961583b339214d8db20eb2747dfb93d50a64d384`
completed its arithmetic tests but failed the final receipt comparison.
The corresponding receipt hash was
`7c4113b43db0862925e9c177b2eea243a0f62dd9e316ff92a931c9020a2c3a43`.
Every source hash remained unchanged during the failed run.

Two Python-to-JSON type mismatches caused the failure:

- `determinant_counts_by_size` used integer dictionary keys; JSON reload
  supplied string keys.
- The local minor witnesses stored row and column index tuples; JSON
  reload supplied lists.

The checker author changed those fields to explicit string keys and
lists. Author `--write` mode now also checks the saved JSON against the
computed object, so it cannot bypass this round-trip check. The reviewer
inspected all three changes before the second replay.

## Accepted replay and source scope

The following command then completed independently with exit code 0 and
`status: PASS` at the final pins below:

```
python3 experiments/cycle_spectrum/C012/check_coupled_system.py
```

The reviewer read the complete checker and the reused C009
`require`, `step`, `word_data` and `certificate` helpers. Intercepts,
defect blocks, matrices and determinants are computed in the new
checker. The historical loader and raw-arrow certificate are reused;
this is not an independently implemented second cycle census.
The replay compared the complete computed receipt with the saved JSON,
including all source hashes. The reviewer did not regenerate receipts.

The reviewer authored `COUPLED_SYSTEM.md`. This note is therefore an
independent review and execution of another agent's checker, not an
independent proof review of that authored theorem. Historical full-gate
results and published analytic inputs are outside this review.

## Actual-cycle evidence and exact domains

The checker verifies 2,459 stored source instances, their words, exact raw
arrows and scaling, with 36,912 source arrows and 1,275 scaled instances.
After normalization and the one C007 addition it checks 1,185 cycles,
including 1,177 nonfixed cycles and 28,831 normalized arrows. All 11
historical fixtures remain explicit controls.

Every nonidentity rotation of the primitive nonfixed cycles is included:
27,646 rotations. For each one, blocks end at mismatch sites, their
interiors and intercepts agree, and both full-intercept matrix products
are compared with independently reconstructed cycle intercepts. The
common gcd divides every rotated intercept exactly; the integer-state
division is checked, as are all raw valuations and closure.

The receipt's `all_cut_identities=1938204` counts the two full-intercept
identities at each **block start**, across all rotations. Its 969,102
coupled equations are the corresponding differences. These counts do
not claim separate evaluation at every internal one-arrow cut; the
written proof explains why the block cuts retain those congruences.

Explicit controls retain the q97, q233 and q359 examples from C011, with
g equal to 5, 7 and 73 respectively. Their normalized states are checked
against the stored corpus up to rotation. No formal affine loop is used
as a substitute for an actual raw cycle.

## Checks that do not assume the asserted determinant formula

- The matrices are built from block products, and their action is
  checked against the actual full intercepts. This tests the cuts,
  coefficient order and wraparound.
- Determinants are evaluated by fraction-free Bareiss elimination,
  with exact intermediate divisions. They are then compared with the
  product formula, rather than being constructed from that formula.
  There are 28 such checks from the actual corpus, 25 from the generated
  family and three explicit C011 controls. Matrix size is bounded by 8
  for these determinant tests; it is not an all-size computation.
- Selected minors through size 4 are evaluated independently: 552
  corpus checks and 603 generated-family checks, plus the explicit
  controls. Their powers of D are checked by exact integer division.
- Separately from the checker, the reviewer evaluated the full Leibniz
  determinant sums for the displayed q97 three by three matrix and the
  four-defect example. The signed values were `-186240` and
  `-3731743744`, agreeing with the checker's absolute determinants
  without using either its Bareiss routine or its product formula.

The primitive run family supplies 25 generated words, including long
matching arcs. Each has a direct primitive-period and exact-arrow check.
Nine prescribed-modulus controls verify `M0|g` for M0 equal to 5, 7 or
25 at each r equal to 2, 3 or 4. The resulting gcds are:

| M0 | t | g at r=2 | g at r=3 | g at r=4 |
| --- | --- | --- | --- | --- |
| 5 | 4 | 5 | 35 | 65 |
| 7 | 6 | 91 | 7 | 1729 |
| 25 | 20 | 275 | 1925 | 3575 |

Five local profiles cover primes 5, 11 and 23 with `v_p(D)=2`, at matrix
sizes 4, 6 and 8. For each profile the checker finds an actual two by two
minor that is a unit modulo p, checks **every** three by three minor is
divisible by `p^2`, and evaluates the full determinant valuation.
Together these 6,704 three-minor checks and determinant valuations
certify the stated local Smith exponents in those finite cases. The
checker does not merely copy the expected rank or infer prime-power
behavior from a mod-p rank check alone.

Twelve repeated-word controls keep their 24 zero-defect shifts separate.
Every repetition of `(2)` retains denominator 1; constant words are not
mistaken for nonzero-mismatch cases.

## The candidate inequality receives no discriminating support here

All 30,533 tested nonzero rotations pass

```
g^s * 4^m < 2^(A*s) * 3^m.
```

All 30,533 also satisfy the independently recorded sufficient condition
`4^m <= q^s * 3^m`. Since `g=D/q < 2^A/q`, this already implies each
success. This includes both the 27,646 corpus rotations and the 2,887
generated/repeated controls. Thus these passes supply no discriminating
evidence for the proposed arbitrary-mismatch estimate. The useful
finite tests in this batch are the matrix, determinant, minor, local
Smith and actual-family controls described above.

No error remains within the reviewed scope. Finite checks do not prove
the candidate, an unrestricted denominator-1 exclusion, or novelty.

## Accepted SHA-256 pins

| File | SHA-256 |
| --- | --- |
| `COUPLED_SYSTEM.md` | `c71362d09e2480971fd473f902f47387d2c31a482852d3f6d964d6d9ad9c46c2` |
| `check_coupled_system.py` | `bb0b9c27fc6ef0b116e302a369b33552f54c2a7efa4d94d4b44be8b9ea5e356c` |
| `coupled_system_audit.json` | `033f8f950498c208c7e446e3c46f467d3894adb752c43bba61200b60aee107fc` |
| `../C009/check_excursions.py` | `a7631d433cd5952d8a27de3eb41addb8d01784da410064fb9e479d5cff3e17cb` |
| `../C001/actual_cycles.json` | `28d067d3f82585a3701616adce3b57cae994541c4ddd3b4859d2bcf2307e44f2` |
| `../C007/height_denominator_audit.json` | `b35a18cb4209b5d0afd104f5c9e38926dc2de5dbef890cc324cf05ae83ce4ceb` |
| `../../phase6/cycle_fixtures.json` | `3aeddd6c3eb2f9b4be54aa239b1ebd197fcabd3a215880e4a853470921e01fe2` |
