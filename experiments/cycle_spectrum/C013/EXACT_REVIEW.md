# C013 — Exact checks, author scope and controls

**Status: author finite run PASS, including saved-JSON equality.** This
note records the checker author's work. Independent source review and
fresh `--check` replay belong to
[INDEPENDENT_CHECKER_REVIEW.md](INDEPENDENT_CHECKER_REVIEW.md); the author
run is not relabelled as an independent replay. Written proofs,
imported logarithm estimates, finite checks and formal verification
remain distinct.

## 1. Frozen sources

| File | SHA-256 |
| --- | --- |
| [OVERLAP_THEORY.md](OVERLAP_THEORY.md) | `43c44f9ef6a2d9f42b1ce956a70d69db5f7c5b9582baf81b87c554aadb0605f9` |
| [OVERLAP_CONTROLS.md](OVERLAP_CONTROLS.md) | `66d6b4eee55410ceee5b8da2e3b509f6ac29f37f8e0993aa0534e2ef17688ec8` |
| [check_overlap.py](check_overlap.py) | `911b5adf0688c4e5954f95b3439902db221f118ead0ca7ce45ed7a5d793d84d5` |
| [overlap_audit.json](overlap_audit.json) | `21a5f84c35f8b15ebcbf88597ac50bf2fa68ed719750c079c915ec359fc2ec75` |

The compact receipt is approximately 36 KB. It pins the C012 and C009
helpers and all three input files. No historical mathematical file was
edited. The cycle clock is raw positive odd-only, with no absorber.

Author command, completed with exit status zero:

```
python3 experiments/cycle_spectrum/C013/check_overlap.py --write
```

Reproducible read-only replay:

```
python3 experiments/cycle_spectrum/C013/check_overlap.py --check
```

Both modes compare the computed object with the reloaded JSON. The
writer therefore exercises the same canonical-type equality that failed
in C012's first draft. Default invocation also performs the check.

## 2. Complete actual-cycle and paired-run coverage

The source coverage is 2,459 C001 instances over 333 parameters, with
36,912 raw arrows and 1,275 scaled instances. C007 adds one normalized
cycle, giving 1,185 normalized cycles and 28,831 normalized arrows.
All 11 fixtures retain their actual parameters, states, valuations and
scaling. Eight fixed points are outside the nonconstant-marker theorem.

For every one of 27,646 nonidentity rotations, the checker uses actual
state differences from the same primitive cycle. It verifies:

- 75,577 zero sums over the orbits of the selected shift;
- 969,102 maximal agreeing runs, including 334,590 of positive length;
- the exact identity `2^E z_end=3^t z_start` and the common nonzero
  integer multiplier in `z_start=2^(E+1)k`, `z_end=2*3^t k`;
- the diameter bound, the dyadic-height conversion and the rational
  denominator consequence retaining `2^(B+1)-1`;
- the cyclic pigeonhole bound on the longest agreeing run.

There are 5,242 unit multipliers, of which 4,202 occur on positive
runs. The sample's longest matching run has length 10. The tightest
positive-run diameter ratio is `137/128`, at q131, minimum 23, period
26, with run length 3 and valuation sum 10. The strongest displayed
height-dependent denominator lower bound is `40619/512`, at q755,
minimum 869, period 10. These extrema are only over the stored sample.

The finite denominator inequality is

```
6 D max(2^E,3^t) < m q 2^A (2^(B+1)-1).
```

It uses `eta=D/2^A`, not a floating-point evaluation of the larger
natural-logarithm quantity delta in the written theorem. No check
silently removes the height factor or replaces a diameter lower bound
with a minimum-state lower bound.

## 3. All actual polynomial gcds and the Fourier inequality

The checker computes polynomial gcds exactly on **all 1,185 actual
valuation words**, including all 762 with noncoprime totals. The other
423 have coprime totals; their calculated G is one, independently
calibrating the written irreducibility lemma. No actual polynomial case
is left uncomputed.

The implementation uses primitive integer pseudo-remainders, with exact
long division of P and Q by the returned monic G. It also checks that
the two quotient polynomials are coprime. This is exact rational
polynomial arithmetic without a symbolic-algebra dependency or a
floating Fourier transform.

Twenty actual cycles have nonconstant G. For example, q793 with minimum
259 has period 30, total 60 and `deg G=9`, so e is 21. Every actual
nonidentity rotation satisfies the exact integer inequality

```
s e(e-1) >= 2m.
```

The meaning of e as Fourier support and the uncertainty argument are
written proofs. Their universal validity is not inferred from the
27,646 finite inequality checks.

Both stored q5 cycles of period 17, with minima 187 and 347, have
total 27, G equal to one and e equal to 17, while the numerical gcd is
1,015,513. This preserves the distinction between polynomial and
numerical cancellation. The primitive marker word `(3,1,3,3,1,1)`
has G equal to `X+4` and e equal to 5, so polynomial cancellation is
not dismissed as merely a word repetition.

## 4. Common-background quantitative checks

For every nonfixed actual cycle, the empty-background specialization
checks the homogeneous extraction, the numerical residual-gcd identity
and the conservative uniform denominator inequality. All 1,177 such
lower bounds are below one. They are algebraic controls, not finite
evidence of a new exclusion on the actual sample.

For nonempty backgrounds the checker independently evaluates the
resultant by the frozen integer Bareiss implementation. It retains

```
h=gcd(Qbar_h,Pbar_h),
gcd(Qbar_h,E Pbar_h)=h*gcd(Qbar_h/h,E).
```

It checks that h divides the part of the resultant coprime to 6.
For the primitive six-marker control, the absolute resultant is
`2^41*3^4`, so that part is one. Three explicit nonempty controls give:

| U | q | G_h | h |
| --- | --- | --- | --- |
| `(2)` | 92833 | 25 | 1 |
| `(1,2)` | 11632565 | 59 | 1 |
| `(1,1,2,2,2,2)` | 734195049138649189 | 6283 | 1 |

The second background is expanding: `2^A_U=8<9=3^n`, while the full
word has positive D. It prevents importing a pure-block contraction
hypothesis. Backgrounds `(1)` and `(1,1)` for these markers have
negative full D and are explicitly excluded from positive-cycle counts.

For the conservative quantity

```
Rbound=r^[e(d+1)]*2^(2Te),
B_lower=(D/2^A)*2^[n(e-1)-d]/Rbound,
```

the checker uses only integer cross-multiplication to verify `q>B_lower`.
Four nonempty controls certify `B_lower>1`. Their background is
`(1,1,2,2,2)` repeated 10 or 20 times:

| Markers | n | Exact floor of B_lower | Every state greater than q? |
| --- | --- | --- | --- |
| `(3,4,5)` | 50 | 9928330 | No |
| `(3,4,5)` | 100 | 12599407636574732159741542015837396632 | Yes |
| `(3,1,3,3,1,1)` | 50 | 9918691869082759 | Yes |
| `(3,1,3,3,1,1)` | 100 | 16058598138437368231533039888995732223071588893835602879463098961882247255073 | Yes |

Thus the quantitative test is nonvacuous, including a three-marker
case whose states all exceed q. The six-marker control has a two-defect
rotation and is already in C011's class; it is not counted as a new
cycle exclusion. These controls do not imply that every sparse-rotation
word admits one repeated common background.

Constant-marker repetitions `(2)^k`, for k equal to 2, 3 and 5, retain
q equal to one and e equal to one. Their zero rotations remain outside
the nonzero-defect inequality and their constant markers outside the
quantitative theorem. The written scope preserves every repetition of
the trivial cycle, beyond these three finite controls.

## 5. Near-critical height obstruction

The three specified upper-pair controls give:

| (a,b) | Period | B | floor(L/q) | q bit length |
| --- | --- | --- | --- | --- |
| (27,17) | 51 | 6 | 20 | 78 |
| (65,41) | 123 | 12 | 72 | 191 |
| (485,306) | 918 | 76 | 814 | 1447 |

All 1,092 raw arrows and 1,089 nonidentity rotation distances are
checked. Each word is primitive and has minimum rotation distance
three. The checker independently reconstructs the exact affine U
formula and all three marker-state equations, verifies that the minimum
occurs immediately after a marker, and checks

```
256 L (Q^3-P^3) > 27 q Q^3,
H*2^u > L*3^u.
```

The selected shift has three matching runs of length b-1. The
common-background denominator extraction agrees with the same q after
rotation of the displayed cut. At the largest pair, even the coarse
uniform denominator bound is greater than one.

These three examples are not a proof of the limiting constants, the
balanced-subsequence construction or growth at all scales. Those are
separate arguments in the pinned theory note. In particular the
denominators grow; this is not a counterexample at bounded q.

## 6. Candidate stress: stopped for lack of discrimination

The bounded grid contains 243 distinct primitive words, built from
repeated and rotated known cycle blocks, a changed terminal valuation,
and the marker/run backgrounds. It checks 27,666 raw arrows and all
27,423 nonidentity rotation distances. The maximum m/s is 384.

For each word, only its strongest minimum-distance candidate test is
reported. All 243 pass, and all 243 already satisfy the comparison that
makes the candidate follow from q alone. Moreover, 102 have minimum
distance two and are already covered by C011. The grid was stopped;
no broad seed census or further expansion was performed.

This nondiscriminating result was redirected into the exact all-height
run audit and the common-background polynomial theorem. The original
arbitrary-rotation relative-cancellation candidate remains open. The
finite checks do not prove bounded-denominator finiteness, independently
verify the imported Matveev theorem, force unrestricted mismatch growth,
establish novelty or formally verify Collatz.
