# C010 — Independent arithmetic review

**Result: PASS within the stated written and finite scopes.** No mathematical
error was found in the two independently authored notes or the checker.
This is an agent review and a fresh exact replay, not a Lean proof, a human
referee report, or an assertion of novelty.

## Authorship and independence

The reviewer authored `ODD_ROUNDING.md`; checks of that note recorded here
are **author checks**, not independent review. The reviewer independently
read the root-authored [GAP_LATTICE.md](GAP_LATTICE.md), another agent's
[ROUNDING_PROBE.md](ROUNDING_PROBE.md), and the separate checker author's
[check_integer_gaps.py](check_integer_gaps.py). The reused C009 `step`,
`word_data`, and `certificate` routines were also inspected to establish
what their inputs actually certify.

## Written arguments checked

1. **Dyadic coordinate map.** For `E^m=2I`, the finite geometric sum is
   the exact integer inverse of `U=E-I`. The reconstruction
   `Z_j=sum G+sum_(i<j)G_i` retains the seam and gives a bijection
   between positive gaps and the full strict dyadic order cone.
   Unimodularity preserves the gcd of an integer vector and the least
   common denominator of a rational vector. This is a collective statement;
   an individual gap may cancel more factors.
2. **Ordered operator.** Both `U` and `K=2E^s-3I` are polynomials in
   `E`, so they commute. The cyclic determinant has absolute value
   `2^(m+s)-3^m` for coprime shift and period. The finite modular
   recurrence uses multiplier 4 exactly when `j+s>=m`; the case
   `j+s=m-1` uses the retained seam gap. C006's existing recurrence
   is correct. Summing it recovers the original minimum arrow, not an
   additional equation.
3. **Exact lowbits.** Integer scaled gaps give integer scaled states.
   Legal original valuations `a_i>=1` make each rotated intercept odd;
   the closed original states `q C_i/D` therefore have odd reduced
   denominators. Their scaled-state integrality forces original
   integrality, and the odd quotient forces the exact lowbit labels.
   Positive gaps recover the declared geometric heights and the actual
   minimum. This proof requires the stated positive-valuation condition;
   the `4 -> 13 -> 5 -> 4` affine loop violates it and is correctly
   rejected as an odd-only control.
4. **Scope.** An invertible reformulation supplies no independent
   congruence. It does not establish an impossibility theorem for global
   integer inequalities or cutting planes. Eliminating a supplied fixed
   fractional profile can certify its nonintegrality. The missing result
   is uniform over all legal ordered profiles. Both reviewed notes retain
   this distinction.
5. **Unbounded slack family.** Independently checked the appended extension
   of C004: coprimality makes every interior phase floor increase by one
   between phases 0 and `m-1`, while the leading term is unchanged. Thus
   the seam numerator is exactly `3^(m-1)`. Together with the existing
   strict interior monomial bound this makes every complete gap exceed
   `1/[6(2^epsilon-1)]`. C004's elementary coprime upper-approximation
   construction supplies `epsilon -> 0+` with unbounded periods. The
   zero-height profile gives pairwise lower bounds at most 2 and total
   bound `2m-1`, so arbitrary positive spacing slack is compatible with
   the exact rational cycle equations. Reduced denominator `D>1` is
   retained; `D` is 5 or 7 modulo 8 eventually. This is an extension of
   the old rational spacing obstruction, not a new integer-cycle
   exclusion or an impossibility theorem for arbitrary rounding cuts.
   The final quantitative consequence is also correct: with all heights
   zero, `(2m-1)D/B_0<2/K`, so this particular rounded denominator
   lower bound can tend to zero on the constructed family.

No historical mathematics was corrected by this review. In particular,
the possible seam mismatch was investigated and dismissed by exact index
calculation rather than silently changing the old recurrence.

## Author checks on the rounding note

The local upward-height numerator is the smallest positive odd `r`
satisfying `3r>q(2^k-1)`. Its increments `eta=6` for even `k`, and
`eta=2` or `4` for odd `k` according to `q mod 6`, give the displayed
formula exactly. A separate direct check covered all supported odd
`q<200` and `1<=k<=40`: 2,680 minimal-odd calculations passed.

Summing the local lower bounds includes the seam and gives
`q(C_h/D-V/3)>=Gamma`. The sharpness claimed is for isolated pairs,
not simultaneous attainability around a cycle. `Gamma` need not be dyadic;
its denominator can include a factor 3. The additive-one `q=5` rescaling
passes the lower inequalities while retaining denominator 5. Thus it is
an exact counterexample to the proposed relaxation's exclusion use,
not to integer Collatz or to all possible rounding arguments.

## Checker inspection and independent replay

Executed independently, without writing the receipt:

```text
python3 experiments/cycle_spectrum/C010/check_integer_gaps.py
```

The run completed with exit code 0 and `status=PASS`, `mode=replay`.
The generated result equalled the stored JSON in full.

Coverage inspected in the source and confirmed by this run:

- 2,459 stored raw cycle instances retain their actual additive parameter,
  scaling and all 36,912 raw arrows; the 1,185 distinct normalized cycles
  include the C007 addition. All 11 fixture controls are checked.
- All 1,185 normalized cycles, covering 28,831 arrows, satisfy the
  complete-gap inverse, gcd, lowbit and common-denominator checks.
- The ordered domain has 52 cycles, including the trivial fixed point:
  51 nonfixed, 47 wide, 474 adjacent sharp-rounding checks and 7,022
  proper circular pair checks. Raw `d=7,L=5` is retained but correctly
  outside `q<=L` for the ordered statements.
- Exactly 20 additive-one rescalings pass every circular pair bound;
  one is the integer fixed point and 19 retain denominator greater than
  one. Twenty-eight pass the odd-ceiled aggregate bound. These are
  relaxation-survival counts, not new cycles or positive evidence for a
  universal denominator law.
- The separate signed grid has 19,530 integer vectors, 78,120 rational
  vectors, 131,835 operator-commutation checks, 12 unimodular determinant
  checks and 46 coprime-rank determinant checks. The local rounding grid
  has 1,428 checks.
- Four generated mechanical examples have 355 raw arrows, 351 interior
  gap monomials, four exact seams, 95,351 phase-intercept summands and
  94,996 proper circular pair checks. Three additive-one shapes pass all
  pair bounds; the `(A,m)=(5,3)` shape has two failures. The generated
  examples retain reduced denominator `D` and are not new census
  discoveries. Their finite checks support, rather than replace, the
  written upper-approximation limit argument.
- Five malformed cycle/word inputs are rejected. The zero-valuation
  affine loop is preserved as a negative lowbit control.

The exact Gaussian determinant implementation is independent of the
closed determinant formula. Its finite grid supports the written argument;
it does not verify that argument for all matrix dimensions. Likewise,
the actual-cycle census checks consistency across the stored family and
does not provide completeness for unsearched words or denominators.

## Reviewed file hashes

| File | SHA-256 |
| --- | --- |
| `GAP_LATTICE.md` | `e8eed1e1a08aeefc1632ef4e762da8bc9182ee6456bb390a5e804c86c968ee64` |
| `ROUNDING_PROBE.md` | `62b9d2da833ce97fa1025e2bc22aafa6ee768c16e84c24044330beed8b76dbf2` |
| `ODD_ROUNDING.md` — author check | `4647d1b51ddf73e1e6a5b5161414c5368d3c9098baa115cd61748c52132a59ac` |
| `check_integer_gaps.py` | `87221a51c008668a8e36513096080cfc352ad16a86ba842976342a1c7deead78` |
| `integer_gap_audit.json` | `f26028a1d6c9f5f725e1d0bece4d1f3e44dc5dc895863c105433c9eed8d92d5c` |

**Conclusion:** the arithmetic supports the stated coordinate equivalence,
legal-profile lowbit consequence, necessary rounding bound and exact failure
of that bound to exclude every parameter-one rational shape. The ordered
integer-cycle target and the full nontrivial-cycle headline remain open.
No improvement to published cycle records follows from these results.
