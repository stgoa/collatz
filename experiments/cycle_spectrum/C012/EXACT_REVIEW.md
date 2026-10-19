# C012 — Arithmetic and proof review

**Status: PASS within the stated scope.** This review independently reads
the two written arguments below. Its author also wrote the coupled-system
checker; the author run described here is therefore not an independent
replay of that checker. A separate review/replay is recorded in
[INDEPENDENT_CHECKER_REVIEW.md](INDEPENDENT_CHECKER_REVIEW.md).

No Collatz proof, unrestricted denominator bound, novelty claim or formal
verification is asserted. All cycle checks use the raw positive odd-only
map, with no absorbing state.

## Frozen material reviewed

| File | SHA-256 |
| --- | --- |
| [COUPLED_SYSTEM.md](COUPLED_SYSTEM.md) | `c71362d09e2480971fd473f902f47387d2c31a482852d3f6d964d6d9ad9c46c2` |
| [COUPLED_OBSTRUCTIONS.md](COUPLED_OBSTRUCTIONS.md) | `c9bfcf8fec24a56084a6e93230fdededec621ebc882cf422e570dd29a65ce9f3` |
| [check_coupled_system.py](check_coupled_system.py) | `bb0b9c27fc6ef0b116e302a369b33552f54c2a7efa4d94d4b44be8b9ea5e356c` |
| [coupled_system_audit.json](coupled_system_audit.json) | `033f8f950498c208c7e446e3c46f467d3894adb752c43bba61200b60aee107fc` |

The receipt separately pins every imported helper and input file. This
review does not audit the external analytic inputs of C011, the historical
full gate, the separate shared-arc checker, or any Lean development.

## 1. Complete coupled system

The block convention matters: every block ends at a mismatch. Its two
versions differ only at the last valuation, which is omitted from the
intercept. This gives a genuinely common vector c. Internal matching
arrows transport a difference by multiplication by `3/2^a`; this is a
unit modulo every divisor of D. Thus the block cuts retain the full-cut
difference congruences without asserting separate divisibility of the
entries of c.

I checked the orientation and coefficients of `B`, `W=D B^(-1)` and
`M=W'-W`. The inverse-difference identity gives

```
|det M| = D^(s-2) product |beta'_i-beta_i|.
```

Every beta difference is nonzero. The claim excludes zero-defect
rotations, while allowing nonzero rotations of repeated words. For
`s>=3`, adjugate elimination gives a divisibility already implied by
`g|D`. This is a failure of the specified elimination, not a theorem
against every use of coupled congruences.

The minor argument is also valid over composite D. Unit row ratios
modulo D write each W as an integer rank-one matrix modulo D. Therefore
M is a rank-at-most-two integer matrix plus D times an integer matrix.
Column multilinearity gives a factor `D^(k-2)` in every k-minor for
`k>=2`. No assertion of a rank factorization over a field replaces this
integer argument.

For the local Smith theorem, the hypothesis that every beta difference
is a unit modulo p is essential. It makes H invertible modulo p, so B
and B' have distinct right kernels and distinct left kernels. The two
rank-one adjugates therefore have a difference of rank exactly two.
The three-minor divisibility and determinant valuation then force the
local Smith valuations `(0,0,t,...,t)`, where `t=v_p(D)`. Unit-amplitude
defects satisfy the hypothesis at every prime dividing D. The theorem
describes free block-intercept coordinates; it does not erase the
additional requirement that the paired words are rotations.

## 2. Infinite primitive run family

For `(1^t 2^(2t))^(r-1) 1^t 2^(3t)`, the unique longest run of twos
proves primitivity. There are exactly 2r unit defects under shift one,
and the displayed totals give positive D. The determinant formula
reduces to `2^(A-r) D^(2r-2)`: exactly r block endpoints decrease by
one, and the other r increase by one.

Choosing t with `2^t=3^t=1 mod M0` makes each full run intercept and D
divisible by M0. Concatenation preserves that divisibility, proving
unbounded cancellation at each fixed r. These are actual reduced odd
cycles, because all rotated intercepts divided by g remain positive
odd integers and have the prescribed exact valuations. Unbounded g
alone says nothing about the proposed relative bound on `g/2^A`.

The finite checker verifies the stated seven-state example, its 4 by 4
matrix, the explicit determinant, all generated raw arrows, prescribed
moduli and the local prime-power ingredients. These finite examples do
not replace the all-size argument.

## 3. Arbitrary shared backgrounds

For `w_U=(3,U,4,U,5,U)`, with U containing t ones and 2t twos,
all three markers are
unique. Every nonzero rotation changes the entry at each original marker
position, while shift `3t+1` changes exactly those three entries. Thus the
minimum rotation distance is exactly three, and primitivity follows
without an assumed coprime shift. The construction permits
`gcd(shift,m)=3t+1`; omitting that case would change the problem. Its
totals are `m=9t+3,A=15t+12`. The displayed ratio gives positive D,
and `A<2m` holds exactly when t>2. Thus this counting family retains
the necessary total range of a hypothetical nontrivial q1 cycle,
without claiming that these conditions imply denominator one.

The corrected intercept `C_(5,2^n)=32*4^n-31*3^n` is congruent to one
modulo every prescribed prime other than 2 and 3 when n is a suitable
multiple of their `p-1`. It is odd, nonzero modulo 3 and greater than
one, so it has a prime factor outside the prescribed finite set. This
establishes escape from a fixed S-unit group, while correctly allowing
that this particular subfamily has a two-term expression. This separate
prime-escape illustration has A>2m; the argument does not use it as a
family inside the q1 total range.

The stronger counting argument uses integer exponents explicitly. At
fixed length and total, `v_2(C_U-3^(n-1))` recovers the first letter,
and recursion recovers all but the last; the fixed total recovers the
last. Hence the prescribed backgrounds have exactly `binom(3t,t)`
different intercepts. Each factor `(2t+j)/j` is at least 3 for
`1<=j<=t`, giving `binom(3t,t)>=3^t`. A fixed number of terms from fixed
rational generators, fixed coefficient choices and linearly bounded
integer exponents has only polynomially many possible sums. The
exponential count proves the claimed obstruction, including signed
terms and negative exponents. It does not exclude representations with
unbounded term count, new coefficients or much larger exponent height.

I also checked the new correlated-factor calibration. At the cut after
marker 1, the blocks `(V,3),(V,4),(V,1)` have common intercept
`E=3C_V+u`, giving `C_cut=E S` with
`S=alpha^2+8u alpha+128u^2`. Reduction of `alpha^3` modulo S yields
`D=64u^2(alpha-12u) mod S`. Substituting `alpha=12u` into S gives
`368u^2=16*23u^2`. Since D is coprime to 2u, this proves
`gcd(D,S)|23`, including the prime-power multiplicity. Consequently
`gcd(D,C_cut)<=23E`. This shows concretely why the separate-intercept
obstruction cannot be promoted to a prohibition on coupled arithmetic.

I requested that `e_j in Z` be written explicitly in this argument;
the pinned version includes that clarification. I found no remaining
arithmetic error in either pinned proof.

## 4. Exact finite scope and results

Author command:

```
python3 experiments/cycle_spectrum/C012/check_coupled_system.py --write
```

It completed with exit status zero and `PASS` on the pinned source,
including the saved JSON round-trip equality.
Default replay recomputes the result and compares it with the saved
receipt without writing.

### Failed replay and receipt-format repair

The first independent replay, against checker
`caf55dae71c07cbb671f327b961583b339214d8db20eb2747dfb93d50a64d384`,
completed the arithmetic but exited with status one at receipt equality.
Integer dictionary keys became strings on JSON reload, and tuple minor
indices became lists. That run is a **failed replay**, not PASS.

The repaired checker constructs those keys as strings and those indices
as lists. Author `--write` mode now also reloads the written JSON and
compares it with the computed object, so it cannot bypass that equality
check. The pinned repaired write passed this check. These changes do not
alter any mathematical calculation or finite count. The separate
independent review records the fresh default replay outcome.

- All 2,459 C001 source instances over 333 parameters retain their
  scaling and 36,912 raw arrows. C007's addition gives 1,185 normalized
  cycles and 28,831 normalized arrows. All 11 raw fixtures are retained.
- All 27,646 nonidentity actual rotations exercise 1,938,204 full-cut
  intercept identities and 969,102 coupled equations. No fixed point
  or zero-defect rotation is misclassified as a nonzero defect system.
- Twenty-eight actual matrices of sizes 2 through 8 have independently
  computed Bareiss determinants and 552 selected minors. This is bounded
  determinant coverage, not a determinant computation at every size.
- Twenty-five primitive generated run words have independently computed
  determinants and 603 selected minors. Five local profiles at primes
  5, 11 and 23 use `v_p(D)=2`, exhibit a unit two-minor and check all
  6,704 corresponding three-minors. These are genuine prime-power checks.
- Nine prescribed-modulus controls use M0 equal to 5, 7 or 25, for each
  of r equal to 2, 3 or 4. Twelve repetition controls retain 24 zero
  rotations, including repetitions of the denominator-one word `(2)`.
- Three explicit actual controls at q97, q233 and q359 retain their
  complete coupled systems and independently computed determinants.

The direct intercept sum is separate from the historical recurrence
helper. The matrix products are compared with independently reconstructed
rotated intercepts. Bareiss computes the selected determinants without
calling the determinant product formula. Local Smith valuations are
inferred from checked minors and determinant valuations, not produced
by an independent Smith-normal-form package.

## 5. Candidate inequality: no discriminating success

The exact candidate tested is

```
g^s 4^m < 2^(A s) 3^m.
```

All 27,646 actual tests and all 2,887 generated nonzero-rotation tests
pass, but **every pass already follows from the known reduced q**.
For the actual sample, `q>=5` and `m/s<=5`; in particular
`(4/3)^5=1024/243<5`. Together with `g/2^A<1/q`, this implies the
candidate immediately. The generated cases also satisfy the analogous
exact q comparison. They add no discriminating positive evidence for
the universal inequality.

The repetition diagnostic uses a strict inequality: equality at the
limiting ratio still leaves every finite repetition strictly below the
candidate threshold. An initial conservative equality flag was corrected
before the pinned write; it affected no recorded case.

The batch therefore supplies a written obstruction to determinant
elimination and to fixed-complexity treatment of arbitrary shared
intercepts. The relative-cancellation candidate remains open.
