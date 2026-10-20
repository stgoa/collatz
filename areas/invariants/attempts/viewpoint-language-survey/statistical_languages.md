# V002 — Occupation measures and information carried by integer ensembles

**Status: bounded exploratory comparison, not new mathematical results or a
novelty claim.** The examples are exact elementary calculations. The proposed
estimates remain open here. This pass reads the current standing and V001;
it changes no frozen proof, dispatcher, receipt or standing document.

Throughout, `S_d` acts on positive odd integers, with `S_d(1)=1`; time counts
odd arrows. Put `S=S_1`. The d=5 control is `19 -> 31 -> 49 -> 19`.
Probability laws below are positive laws on actual integer seeds, never signed
packet currents. Unsubscripted `log` is natural; Shannon examples use bits.
Existing constraints include [R31](../../../convergence/results/bounded-runs-exclude-finite-label-potentials/README.md),
[R49](../../../convergence/results/inverse-only-exclusions-short-forward/README.md), the
[integer-prefix result](../../../convergence/results/exit18-return-integer-cylinders/README.md)
and [P6-003](../../../convergence/results/growth-norm-transport-barrier/README.md).

## V11. Occupation measures: recurrence versus escape of mass

**1. Objects.** For an actual seed n, retain the empirical probability
`m_(n,T)=T^(-1) sum_(j=0)^(T-1) delta_(S^j(n))` on the discrete positive
odd integers. Its exact stationarity defect is
`S_*m_(n,T)-m_(n,T)=(delta_(S^T(n))-delta_n)/T`.
For an initial law `mu_X(n)=(1/n)/sum_(odd m<=X)(1/m)`, average these
measures over n. This is a time-occupation question, distinct from V4's
survival probability at a particular time.

**2. Structural gain.** Every orbit either enters a finite cycle or has no
repeated state. In the latter case it eventually leaves each finite set.
Its empirical mass on every finite set tends to zero. In the former case
the empirical law tends to the uniform law on that cycle. Consequently
countably additive invariant probability measures on this countable system
are mixtures of cycle laws. This identifies exactly what such measures
can detect. [Assani, Theorem 3.1](https://arxiv.org/html/2208.11675v2#S3.SS1)
gives the analogous cycle/basin/unbounded-orbit decomposition for the
**shortcut** Collatz clock.

**3. Translated gap.** The stationarity defect tends to zero without ensuring
tightness: all mass may escape. A pointwise limit can be the zero measure,
despite every empirical law having mass one. Compactifying the state space
can retain an artificial mass at infinity; it does not turn it into integer
recurrence. A finitely additive invariant mean similarly does not supply
countable additivity or tightness. An invariant cycle measure already exists
at 1 and says nothing about other seeds. A finite *invariant* measure
equivalent to counting measure would be too strong: even transient 3 cannot
carry positive invariant mass. Assani's Theorem 4.1 instead uses a finite
**nonsingular, power-bounded** measure equivalent to counting measure and
specifies the conservative part; it is an equivalence, not supplied progress.

**4. Exact example.** For `3 -> 5 -> 1`, when `T>=2`,
`m_(3,T)=(delta_3+delta_5+(T-2)delta_1)/T`, hence its limit is `delta_1`.
On any hypothetical nonrepeating orbit,
`m_(n,T)({1,3,...,2K-1})<=K/T`; each atom disappears. No divergent Collatz
example is asserted.

**5. Cycle controls.** For d=5 and `T=3r`,
`m_(19,T)=(delta_19+delta_31+delta_49)/3`. It is perfectly tight and invariant
but never reaches 1. Tightness addresses divergence; identifying the cycle
remains separate.

**6. Cheapest next test.** Write an attempted tightness bound with its exact
orders of X, T and the finite cutoff K. Reject an argument that obtains a
finite K only after fixing X, or exchanges these limits without a uniform
estimate. Also test whether its limiting probability simply discards the
escape mass.

**7. Partial milestone.** Prove
`lim_(K->infinity) liminf_(X->infinity) liminf_(T->infinity)
 E_(n~mu_X)[m_(n,T)([1,K])] >= 1/2`.
This would put at least half the asymptotic logarithmic seed mass into finite
cycles, allowing both other cycles and a remaining divergent basin. It is
weaker than absorption and is not supplied by an almost-bounded *minimum*
theorem. No uniform tightness estimate is currently identified.

**Selection:** useful diagnostic for precisely separating cycle mass and
escape; defer as a new route until a uniform tightness mechanism is proposed.

## V12. Conditional information of realized paths, rather than symbolic entropy

**1. Objects.** Draw N from a specified finite law on positive odd integers;
let `Y=S^k(N)` and record its exact k-arrow valuation word W. Use Shannon
entropy `H`, conditional entropy and collision mass `sum_y P(Y=y)^2`.
For fixed k, determinism gives `H(N)=H(Y)+H(N|Y)`. Retaining `(Y,W)`
recovers N through the exact affine inverse, so it retains all starting
information. At 1, use an explicit absorbing-step marker instead of falsely
applying a raw `3x+d` valuation rule.

**2. Structural gain.** This distinguishes loss through actual merging from
apparent randomness of a symbol sequence. Conditioning on survival or a
first-passage event changes the law and can change entropy; it is not a fresh
uniform sample. The useful object is the distribution of *realized integer
endpoints*, including their path-selection bias. In [Tao, Proposition 1.9,
Proposition 1.11 and §6](https://arxiv.org/html/1909.03562v7), finite-residue
equidistribution has stated hypotheses, first-passage distributions require
a separate stability theorem, and collision entropy enters the offset-mixing
argument. These are substantive arithmetic estimates, not a general entropy
decrease principle for individual Collatz trajectories.

**3. Translated gap.** A point seed has entropy zero throughout. For an
ensemble, decreasing entropy means fewer distinguishable endpoints, not
smaller endpoints or absorption. Independent geometric valuations are not
available after arbitrary conditioning. Exact word cylinders use
`2^(A+1)`, where A is the valuation sum; when this modulus outgrows the seed
range, finite-cylinder frequencies cannot be extrapolated. Haar-typical
2-adic words do not settle this integer realization problem. P6-003 also
precludes demanding the needed concentration bound for every target set.

**4. Exact example.** For uniform `N in {13,53}`, both sources reach 5 in one
arrow. Thus `H(N)=1` bit, `H(Y)=0`, and `H(N|Y)=1` bit. The valuations are
3 and 5, respectively; `N=(2^W*5-1)/3` restores the missing bit. This is
arithmetic merger information, not heat dissipated by an individual orbit.

**5. Cycle controls.** For d=5, uniform `N in {19,81}` likewise maps to the
single endpoint 31, with valuations 1 and 3. Entropy falls by one bit into
the nonabsorbing cycle. Uniform mass on the three cycle points is merely
permuted and retains entropy `log_2(3)`. Any claimed implication from entropy
loss to absorption fails these exact examples.

**6. Cheapest next test.** Specify a first-passage law and its failure symbol,
then locate the first step that assumes new independent bits or removes
conditioning. Compare the resulting statement with Tao's actual hypotheses
before numerical work. Reject a proposed entropy potential if its only
content is the deterministic identity above or frozen symbolic growth rates.

**7. Partial milestone.** One concrete candidate is as follows. Draw N
logarithmically on odd `[X,2X]`; stop at the first state `<=X^(1/4)`, capped
at `ceil(10 log X)` odd arrows, using a separate symbol `dagger` for failure.
For its actual endpoint law p_X, prove explicit `C,eta>0,X_0` such that,
for every integer `X>=X_0`,

`p_X(dagger) <= C X^(-eta)` and
`sum_(1<y<=X^(1/4), y odd) p_X(y)^2 <= C X^(-eta)`.

This asks for quantitative nonconcentration after a substantial descent;
mass already at 1 is retained separately. It supplies neither absorption of
the other endpoints nor universal convergence, and may hold for cycle
controls too. It is a proposed integer-ensemble estimate, not an asserted
new theorem or a verified consequence of Tao; a direct literature comparison
is the first gate.

**Selection:** retain this narrow statistical test. It has a measurable
arithmetic target beyond symbolic recoding, but no estimate has yet been
derived and no extended investigation is justified by the language alone.
