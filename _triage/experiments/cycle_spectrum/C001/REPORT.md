# C001 — A fixed perturbation bounds cycle-denominator cancellation

**2026-10-18–19. Written theorem, exact finite experiments, novelty unclaimed.**
This is the first batch under the user's
[cycle-spectrum goal](../BRIEF.md). It proves a
restriction for repeated-block words, then applies it to an infinite
primitive, nonbalanced family. It does not exclude all Collatz cycles.

## 1. The mechanism and the gain

For a nonempty positive valuation word w, let

```
F_w(x)=(3^m*x+C_w)/2^A,
D_w=2^A-3^m.
```

When D_w>0, the word describes a genuine positive rational cycle and
`den(w)=D_w/gcd(C_w,D_w)`. These classical facts are derived in frozen
[R71](../../residual_progress/lattice_cycles/BALANCED_DENOMINATORS.md).

Fix two blocks u,v and repeat u k times before v. Put

```
K=D_u*C_v-D_v*C_u.
```

The [complete proof](REPETITION_SPECTRUM.md) gives:

> If K is nonzero, every cancellation factor
> `gcd(C_(u^k v),D_(u^k v))` divides the prime-to-6 part of |K|.
> That factor is periodic in k. Thus a growing word has only finitely
> many possible cancellation factors, all explicitly bounded.

The proof uses the exact identity
`D_u*C_w-C_u*D_w=2^(k*A_u)*K`. The denominator is coprime to2,
so its common divisor with C_w must divide K. A finite invertible
modular recurrence proves periodicity. No distribution assumption or
unproved prime-factor conjecture is involved.

If `gcd(D_u,D_v)=1`, the cancellation is exactly `gcd(D_w,K)`.
The common-fixed-point case K=0 is essential: in the positive domain,
the two blocks then repeat the same primitive cycle. It includes the
trivial Collatz cycle and repetitions of every genuine d>1 control.

### Exact example

For u=(1,1,3), v=(2), the cancellation is 7 when `k=3 mod6` and 1
otherwise. Hence

```
den((1,1,3)^k 2)=(4*32^k-3*27^k)/(7 if k=3 mod6 else 1).
```

This is an exact spectrum law for all k>=1. The first denominator is 47.
This particular family's rational minimum stays bounded; it is not the
reason for claiming scope beyond finite minimum checks.

## 2. An infinite class with unbounded minima and complexity

For m>=13, let `A=ceil(m log_2 3)`, evaluated exactly as the bit length
of `3^m`, and let u_m be the lower mechanical valuation word of length
m and total A. Consider

```
w=u_m^k 2,       k>=2.
```

For all these parameters, the theorem proves

```
den(w) > 3*(3^m)^(k-1)/(2m) > 1.
```

The word is primitive. It contains a unique cyclic 222 and also contains
121; its shortcut parity word is unbalanced. Thus it is outside the
mechanical family already treated in R71 and the Christoffel class in
Knight's published theorem.

Under the additional explicit condition `2*3^(km)<=2^(kA)`, every rational
cycle state is greater than m/10. For every m such a k exists; the proof
gives the sufficient choice

```
k >= max(2, ceil(3^m/(2^A-3^m))).
```

The numbers of local minima are different in the two clocks:

| Clock | Number of local minima under the height condition |
|---|---:|
| Odd-only Syracuse | k(2m-A) |
| Shortcut Collatz, as in the cited cycle records | k(A-m)+1 |

Both the minimum and the latter count can exceed any fixed cutoff.
This is an all-parameter result outside the direct hypotheses of
fixed-minimum-count records and the balanced class. It is not a claim
to have improved the general 91-minimum bound, nor a claim that this
family is absent from all earlier literature.

## 3. Actual integer cycles across many d

The independent [scanner](scan_cycles.py) follows raw positive odd
`3x+d` orbits: state 1 is not absorbing. The persisted
[data](actual_cycles.json) covers every positive d<=999 coprime to6,
starting from every positive odd seed<=5000.

| Quantity | Verified value |
|---|---:|
| Parameters d | 333 |
| Requested seeds | 832,500 |
| Distinct actual cycles found | 2,459 |
| Distinct cycles after reducing the denominator and scaling | 1,184 |
| Canonical two-block splits tested | 34,453 |
| Repeated-prefix decompositions tested | 2,371 |
| Capped or unprocessed seeds in this run | 0 |

Every cycle has its complete integer states, exact valuations, numerator,
denominator, scaling, discovery seed and replay certificate. All eleven
historical fixtures were independently rediscovered. The finite discovery
is not a complete census of cycles even for these fixed d.

Some controls, including the principal fixed point at d itself:

| d | Cycles found | Cycles with reduced denominator exactly d | Longest odd-only period |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 5 | 6 | 5 | 17 |
| 7 | 2 | 1 | 2 |
| 13 | 10 | 9 | 15 |
| 61 | 3 | 2 | 41 |
| 563 | 2 | 1 | 215 |

The tested decompositions use the orientation starting at the cycle's
smallest state; they are not an all-rotation decomposition census.
Denominator invariance itself is checked at every state. All divisions
and cycle arrows use exact integer arithmetic. Of the 2,013 nonfixed
cycles, 1,587 have a tested split with |K|<D_w; the bound permits the
actual d>1 denominator in every case. A bound need not be sharp to pass.

The [separate word experiment](spectrum_audit.json) tests 26,628 block
pairs and 239,345 positive word cycles, replaying 6,264,270 odd arrows.
Its finite box restricts u to `2^sum(u)>3^len(u)`; the general algebra
also permits negative D_u, but that extension is not covered by this box.
It checks 238,328 nonzero-K divisibilities and 212,522 exact coprime-block
formulas, plus 1,017 common-fixed-point repetitions. There are 3,235
distinct denominators in that word box. It also checks 128 certified
modular periods, the explicit mod6 law through k=256, and 306 perturbed
mechanical examples with m through 128 plus 256 and 512. Repeated words
and repeated denominators are counted honestly as test cases, not as
new primitive cycles.

## 4. A false strengthening killed exactly

Dropping `gcd(D_u,D_v)=1` from the exact gcd formula is false:

```
u=(3), v=(1,5), k=1,
D_u=5, D_v=55, K=-30,
C_w=49, D_w=485,
gcd(C_w,D_w)=1, but gcd(D_w,K)=5.
```

The actual d485 cycle is `49 -> 79 -> 361 -> 49`, with valuations
3,1,5. The divisibility theorem survives; the stronger equality does
not. No historical result was changed or found erroneous. During
derivation, an overly optimistic three-quarters height comparison was
discarded before adoption; the proved three-fifths comparison keeps
the extra exponent condition. The clock distinction was also checked
before finalizing the theorem.

Independent review corrected a draft sign overstatement: D_u>0 makes
D_(u^k v) positive for all sufficiently large k, not necessarily for
every k. For u=(2),v=(1,1,1),k=1 it is-49. The code already filters
nonpositive denominators; the written statement now keeps that domain.
The first default receipt replay also exposed a tuple/list serialization
mismatch. The saved representation was corrected and the default replay
then passed independently; no numerical cycle or theorem changed.

## 5. Literature, review and verification

The [primary-source audit](LITERATURE.md) identifies the affine
concatenation, commutator and repetition formulas as established work,
including Trümper 2014. The exact cancellation corollary was not located
in that bounded audit; this does not establish novelty. It checks
Knight's precise extremal meaning of “high”, and distinguishes
Simons–de Weger's updated version, Hercher's journal result and its
2026 corrigendum from an unverified newer record claim.

The [independent review](INDEPENDENT_REVIEW.md) audits the proof and
executable checks. Root separately checks the arithmetic argument and
the independent scanner, and reran its full discovery: every saved field
matched except elapsed time. No formal verification or human peer review
is claimed. Reproduce from the repository root:

```
python3 -B experiments/cycle_spectrum/C001/check_spectrum.py
python3 -B experiments/cycle_spectrum/C001/scan_cycles.py
python3 scripts/verify_all.py --cpp --transfer-controls
```

The first command regenerates the exact word receipt in memory and
compares it with the saved one. The second replays all saved cycle
certificates and their discovery paths; `--scan --output /tmp/cycles.json`
reruns discovery. Source hashes bind both receipts to their code. Run
without optimized Python. The [delivery receipt](delivery_checks.json)
records final verification and frozen-file checks.

## 6. What to aim at next

The fixed-perturbation mechanism is now understood. The next substantive
test is **two independently growing repeated blocks**, `u^k v^ell`.
Elimination leaves a common geometric divisor rather than a fixed
constant. Equal valuation slopes can produce exponential cancellation,
so a uniform bounded-cancellation claim would be false. The literature
audit identifies an existing S-unit gcd theorem to assess in the
unequal-slope case, with ineffective thresholds kept explicit.

This batch meets the spectrum-law and denominator-restriction milestones
at their stated scope. It supplies a family outside the cited fixed-count
and balanced hypotheses. The headline remains open because general
primitive words need not have either fixed-block form. The next batch
must test a sharper mechanism against the actual d-family data, not
recount this family as a new result.

The read-only side-lane assessment is in [SIDE_REVIEW.md](SIDE_REVIEW.md).
