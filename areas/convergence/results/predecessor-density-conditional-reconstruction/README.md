---
id: predecessor-density-conditional-reconstruction
kind: result
title: Conditional on Tao's mixing theorem, every target not divisible by 3 has predecessors of positive lower density, for every 3x+d with gcd(d,6) = 1
status: written
claim: >
  Assume Tao's finite-distribution mixing estimate (Proposition 1.14 of the corrected v7, for all 1 <= m <= q,
  with unspecified finite constants C_A). Fix d > 0 with gcd(d,6) = 1, the ordinary map C_d (n/2 on even n,
  3n+d on odd n) and the odd-only map S_d = (3n+d)/2^v2(3n+d). For every fixed positive integer target a with
  3 not dividing a there are constants c_(d,a) > 0 and X_(d,a) such that every integer X >= X_(d,a) has at least
  c_(d,a) X distinct positive odd starts below X whose C_d orbit reaches a; the constructed paths avoid 1 before
  a, so the same holds with absorption at 1, and for odd a in the S_d clock. No convergence or nonperiodicity of
  a is assumed and gcd(a,d) = 1 is not required; constants depend on d and a, and no uniform time bound,
  density limit or uniform coefficient is claimed. The restriction 3 not dividing a is necessary, and 3 | d is
  excluded. This is a written re-derivation of the qualitative chain of the Mazur manuscripts, not of their (or
  Lau's) explicit constants.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
assumes: [tao-2019-almost-all]
certificates: [check_audit.py]
evidence:
  - "audit_checks.json: the receipt of check_audit.py (three central histories, 64 histogram fibres, 10 marginal laws, eight signed transfer identities, 108 branch and tail checks, six density-mode cases for the C.2a attempt, four d-controls and six rejections). Finite arithmetic tests of the written ingredients; they neither check an infinite orbit nor run Lean"
  - "audit_notes.md: §§1-7, the seed-uniform weighted-history residue histogram (7)-(8), the explicit mixing transfer (10) and the summable variation majorant (13); transfer_scope.md: the corrected Tao v7 normalisation and the transfer to every d coprime to 6"
  - "verification.json: the main lane's P6-004 finite gate record (python3 scripts/verify_all.py --cpp --transfer-controls, exit 0, 119 report fields, pinned runner, checker and receipt bytes; an earlier run ended with exit 143 and an empty log, cause not established, not counted as PASS). Its 'independent model reviews' were the main lane's own agents, not independent"
aliases: [P6-C.1a-b]
tags: [convergence, phase6, predecessors, density, conditional, tao, 3x-plus-d]
---

# Conditional on Tao's mixing theorem, every target not divisible by 3 has predecessors of positive lower density, for every 3x+d with gcd(d,6) = 1

## Statement

Odd-only and ordinary clocks as defined in the claim; all inverse histories stay above 1, so they agree with the absorbed convention. Assume (T), Tao's Proposition 1.14 in the normalisation of [`transfer_scope.md`](transfer_scope.md) §1:

```
<|rho_q - rho_m o pi_(q,m)|>_q <= (2/3) C_A m^(-A),   1 <= m <= q,
```

with `rho_q = (2/3) 3^q mu_q` the normalised law of the finite Syracuse random variable, for fixed finite constants `C_6, C_2`. Then for every fixed `d > 0` with `gcd(d,6) = 1` and every positive target `a` with `3 ∤ a`, at least `c_(d,a) X` distinct positive odd starts below `X` reach `a`, for every integer `X ≥ X_(d,a)` ([`transfer_scope.md`](transfer_scope.md) §2; for `d = 1` equation (20) below, with `c_a = 9p/(1024 M 3^m)`).

This was Phase 6 route node C.1a's written audit of the manuscript chain of [`mazur-2026-predecessor-density`](../../../../sources/mazur-2026-predecessor-density.md): the qualitative argument is re-derived with every multiplicity, residue endpoint error, endpoint-dependent shift, separate terminal error and all-scale coverage retained, and with Tao's analytic estimate as the one explicit external input. It is not an independent proof of Tao's theorem, a check of Mazur's explicit-constant recipe or of Lau's constants, a Lean replay, or a novelty claim. The formal input actually adopted is [`lau-density-formal-replay`](../lau-density-formal-replay/README.md).

## Proof

The argument is in three parts.

1. **Histogram and variation** ([`audit_notes.md`](audit_notes.md), §§1–7): single-block bounds, complete offsets and multiplicity at fixed depth (no hitting-time uniqueness is used, so a periodic root would not break it), the named arithmetic lemma (7) bounding the seed-uniform residue histogram for every `q ≤ 2b_n` with the residue endpoint error kept, the exact use of the mixing input (10) with a moving modulus, and the summable root-independent variation majorant (13). The integer comparisons behind its constants were evaluated exactly. Its audit conclusion: the manuscript's fixed-root multiplicity and growing-modulus bounds survive independent derivation; no missing nonreturn assumption or discarded residue endpoint term was found in its equations (3.9)–(3.10).
2. **Terminal transport and the linear count**, below (the legacy `terminal_audit.md`).
3. **Corrected Tao input and the transfer to `3x+d`** ([`transfer_scope.md`](transfer_scope.md)): Proposition 1.14 of the corrected v7 holds for all `1 ≤ m ≤ q`; the oscillation sum gives (T) with no stray factor 2; multiplication by `d` conjugates the reference laws and transfers, every physical estimate changes in a controlled way, every permitted target supplies a nonreturn root, and the restrictions and cycle controls are in its §6.

### Sources and imported premise

The audited source is Mazur's
[*Explicit Positive-Density Collatz Convergence in Logarithmic Time*,
v2.1](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf),
Sections 5–6, followed by the arbitrary-target selection in
[*Positive Lower Density of Collatz Predecessors*, v1.0](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

The external analytic premise is the finite-distribution statement of
[Tao, Proposition 1.14](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F):

\[
 \langle|\rho_q-\rho_m\circ\pi_{q,m}|\rangle_q
 \le(2/3)C_A m^{-A},\qquad 1\le m\le q,
\tag{T}
\]

for fixed finite constants \(C_6,C_2\). Their existence is imported;
their gigantic explicit values in the later manuscript recipe are not
needed or certified by this note. The reference law is the normalized
finite law of the independent geometric affine offset, with mean \(2/3\),
zero on nonunits, and compatible marginals. It is not a probability law
asserted for an actual integer orbit.

Throughout this note use the original caps \(K_j=\lfloor j/100\rfloor\)
and any fixed integer \(b_0\ge325\). This suffices for an existential
linear lower bound; no target-one logarithmic-time bound is claimed.

### 1. Admissible scales and the endpoint-dependent shift

At scale \(b\), write

\[
 e_b=\lfloor b/100\rfloor,\quad w_b=\lfloor3b/5\rfloor,
 \quad r_b=2w_b-B(w_b)-2e_b.
\]

The full terminal barrier is

\[
 H_{b,u}(s)=2b+B((s-b)_+)-B((b-s)_+)+u-r_b,
 \quad 0\le u\le2r_b.
\]

For a physical parent \(R\ge16^b\), set

\[
 L_b(R)=\frac{(4/3)^bR}{4\,2^{r_b}},
 \qquad U_b(R)=2^{2r_b}L_b(R).
\tag{1}
\]

Suppose the external real scale \(X\) lies in \((L_b(R),U_b(R)]\).
Choose the least integer \(u\) with \(2^uL_b(R)\ge X\). Then

\[
 0\le u\le2r_b,\qquad X\le2^uL_b(R)<2X.
\tag{2}
\]

This choice depends on the actual parent, and it must remain inside the
counting argument.

Let \(\sigma_n=\sum_{j<n}(K_j+3)\). The single-block bounds in the
histogram audit show that the ratio of any two generation-\(n\)
endpoints is at most \(2^{\sigma_n}\). At a common external scale, the
real quantities \(\log_2(X/L_{b_n}(R))\) therefore range over an interval
of length at most \(\sigma_n\). Taking ceilings gives at most

\[
 J_n=\sigma_n+1\le5(n+1)^2
\tag{3}
\]

different shifts. For each fixed shift \(u\), restrict the physical
histogram to those actual endpoints selecting that shift. Its entries
are nonnegative and at most the entries of the original \(H_{n,q}\).
The same uniform histogram bound thus applies to each such restricted
histogram. No conditional probability normalization is made.

### 2. Two distinct terminal errors

#### 2.1 Unfiltered terminal transport

First retain every admissible first-crossing terminal word with cap
\(K_n\), without the additional depth restriction. For each shift its
reference rejection probability obeys

\[
 1-p_{b,u}\le4e^{-b/2560000}+2^{-(K_n+1)}.
\tag{4}
\]

Here is a direct check of the uniformity in \(u\). At the lower and upper
endpoints \(\ell=b-w_b\), \(h=b+w_b\), the barriers satisfy

\[
 H_{b,u}(\ell)-2\ell=u+2e_b\ge2e_b,
 \qquad 2h-H_{b,u}(h)=2r_b+2e_b-u\ge2e_b.
\]

Failure of the lower-endpoint miss or of crossing by \(h\) consequently
forces an absolute centered geometric deviation greater than \(e_b\).
Since \(e_b\ge b/200\) and the depths are at most \(2b\), the
concentration inequality in the histogram audit gives the first term
of (4). Geometric memorylessness at the crossing supplies the second.

For each shift apply the finite transfer comparison with
\(k=\ell=k_n\), \(Q=h_{b_n}+k_n<2b_n\). Pair with its restricted
physical histogram, then sum over the at most \(J_n\) shifts. This
compares the unfiltered terminal marked mass with \(Z_n(M)\), retaining
all preceding central restrictions.

The arithmetic inequality

\[
 4\cdot6!\cdot2560000^6
 \le C_s=8\cdot35!\cdot576^{35}
\]

shows that the same geometric majorant \(E_n\) established in the
histogram audit works after this grouping. Thus the unfiltered terminal
mass differs from \(Z_n(M)\) in absolute value by at most

\[
 J_nE_n.
\tag{5}
\]

This bound is uniform in the root and in every external scale admissible
for all generation-\(n\) endpoints.

#### 2.2 Removing terminal words that are too long

Now impose the additional predicate

\[
 2s\le H_{b,u}(s)+\lfloor b/8\rfloor.
\tag{6}
\]

If it fails, the sum \(A_{s-1}\) before the first crossing satisfies

\[
 A_{s-1}-2(s-1)\le-\lfloor b/8\rfloor<-b/16.
\]

Indeed the barrier is nondecreasing, so the previous partial sum is
strictly below the barrier at \(s\); integer rounding and the failure
of (6) give the displayed inequality. This also holds at the earliest
eligible depth because the lower-endpoint miss is part of the definition.

A union bound over the possible preceding depths gives the reference
probability bound

\[
 (4b+4)e^{-b/16384}.
\tag{7}
\]

For each fixed shift, the transfer of the rejected words is nonnegative
and has average exactly \(2/3\) times their reference probability.
Pairing it with the same restricted physical histogram is therefore
valid without any mixing replacement. The marked mass removed is at
most

\[
 W_n=\tfrac23 J_n C_{b_0}(n+1)^3 G^n
                 (4b_n+4)e^{-b_n/16384}.
\tag{8}
\]

For an explicit summable upper bound, put
\(D_s=8\cdot7!\cdot16384^7\). The seventh exponential-series term gives

\[
 W_n\le\tfrac23 J_n C_{b_0}(n+1)^3
              D_s b_0^{-6}q_1^n.
\tag{9}
\]

Both \(J_nE_n\) and this upper bound tend to zero. The transport error
(5) and the removed mass (8) are separate quantities; neither is paid
for by the other.

### 3. A favorable residue can be fixed before the root

Let \(p_j>0\) be the central reference-code probability. Its deficits
have a summable majorant in the histogram audit. Hence there is a fixed
number \(p>0\) such that every finite product satisfies

\[
 \prod_{j<N}p_j\ge p.
\tag{10}
\]

One elementary construction is to choose \(N_0\) so that the sum of all
deficits from \(N_0\) onward is at most \(1/2\), and take half the
positive product before \(N_0\). Finite-product expansion bounds all
later products from below by this number; earlier products are larger.

Choose \(N\) with \(\sum_{j\ge N}E_j\le p/4\). Composing the finite
central transfers through stage \(N\) gives a function on a fixed
ternary residue space. Its full average is
\((2/3)\prod_{j<N}p_j\), and it vanishes off the unit residues.
Its average over the units is therefore at least \(p\). Choose one
unit residue \(y\) where the function is at least \(p\).

For **every** odd representative \(M\ge16^{b_0}\) of this residue, the
physical transfer identity and uniform variation prove

\[
 Z_n(M)\ge3p/4\qquad(n\ge N).
\]

Choose a further stage threshold so that (5) and (8) are each at most
\(p/8\). The selected terminal marked mass, denoted \(\mathcal M_{n,X}\),
then satisfies

\[
 \mathcal M_{n,X}\ge p/2
\tag{11}
\]

for every later stage and every external scale admissible for all its
endpoints. The budget is exactly \(p-p/4-p/8-p/8=p/2\).
The residue and all these error thresholds were chosen before the
numerical representative \(M\). No assumption about its future orbit
was used.

### 4. All sufficiently large scales, with the overlap error retained

Write \(g=\log_2(4/3)\), so \(2/5<g<1/2\). For
\(b'=b+\lfloor b/100\rfloor\), rounding gives

\[
 r_b\ge(3g/5-1/50)b-g-1.
\]

Using \(b'\le101b/100\) therefore proves

\[
 r_b+r_{b'}-gb'>191b/5000-3.
\tag{12}
\]

Let \(R'\) be any next-generation endpoint, with parent \(P\), and
let \(R\) be any current-generation endpoint. Their spread and the
one-block upper bound imply

\[
 \frac{L_{b'}(R')}{U_b(R)}
 \le2^{\sigma_n+K_n+1+gb'-r_b-r_{b'}}.
\]

If \(\sigma_n+K_n\le\lfloor b_n/200\rfloor\), its exponent is
strictly smaller than

\[
 4-83b_n/2500<0\qquad(b_n\ge325).
\tag{13}
\]

Consequently **every** next lower endpoint is below **every** current
upper endpoint. This is stronger than merely overlapping the interval
along one selected history.

The sufficient condition holds at all sufficiently late stages:
\(\sigma_n+K_n\le4(n+1)^2\), whereas
\(b_n\ge b_0(201/200)^n\). One can choose a finite threshold with
\(b_0(201/200)^n\ge200(4(n+1)^2+1)\) afterward. For an explicit
search convention, choose its first successful \(n\ge400\); the ratio
\(((n+2)/(n+1))^2\le201/200\) for \(n\ge400\) guarantees that
success persists. Existence follows from exponential growth.

Choose a stage \(n_0\) beyond all the preceding thresholds. Its central
generation is nonempty by the positive bound on \(Z_{n_0}\). Let
\(X_*\) be larger than every upper endpoint at that finite generation.
For any real \(X>X_*\), choose the first stage \(n\ge n_0\) whose
upper endpoints are all at least \(X\). Such a stage exists because

\[
 U_{b_n}(R)\ge2^{b_n}\longrightarrow\infty
\]

uniformly in its endpoints. It is later than \(n_0\). Some upper
endpoint in the preceding generation was below \(X\). By (13), every
new lower endpoint is below that preceding endpoint, hence below \(X\).
Thus \(X\) belongs to \((L_{b_n}(R),U_{b_n}(R)]\) for every endpoint
of this generation. This proves the required all-scale quantifier,
including its strict lower and inclusive upper boundary conventions.

### 5. Reduced terminal words and distinct integer sources

Fix the root \(M\) now, and additionally suppose it has no positive
Syracuse return. Decrease the last valuation in inverse order by \(2j\)
until the terminal overshoot is 0 or 1. The new valuation is positive:
the preceding partial sum is below the barrier at the crossing. All
earlier valuations, central cuts, terminal depth, selected shift, and
predicate (6) remain unchanged.

The reduced path is still integral and odd, since the last exponent's
parity is unchanged modulo 3. If \(x\) is its reduced outer source and
\(\omega\) its full word weight, the original source and weight are

\[
 \Psi_j(x)=4^jx+(4^j-1)/3,\qquad4^{-j}\omega.
\tag{14}
\]

The first-crossing cuts and the fixed stage recover all block divisions
from the full word. The parent determines the shift from \(X\).
Therefore an original history is recovered from its reduced full word
and \(j\); no extra multiplicity of reduced histories is silently lost.
Nonnegativity permits enlarging the reconstruction image to all such
pairs.

With overshoot at most 1, the physical inverse bounds give

\[
 2^uL_b(R)\le x\le16\,2^uL_b(R),
 \qquad X\le x<32X.
\tag{15}
\]

Different full words ending at \(M\) now have different sources, even
across different depths. Otherwise the same deterministic orbit would
hit \(M\) at two times, forcing a positive return of \(M\); at one
time its valuations are unique. This stronger source injectivity is
used only here, after the root has acquired the nonreturn hypothesis.

The full affine identity gives \(x\omega\le M\). If \(v_w\) denotes
the weight of a reduced word with its retained selection indicators,
then \(0\le v_w\le\omega_w\le M/X\).

The modulus fits the scale before any residue count is applied. An
admitted parent satisfies \(R\ge16^b\), while \(r_b\le2b\), so

\[
 X>L_b(R)\ge16^b/(4\,3^b)\ge3^b\ge3^{k_n}.
\tag{16}
\]

The middle inequality holds for \(b\ge3\). It is not inferred from
equidistribution or a limiting density.

### 6. Removing the auxiliary residue weight

Choose an integer \(C_*\ge\max(1,(2/3)C_2)\). Choose an integer
\(m\ge1\) with

\[
 m^2\ge176MC_*/p,
\tag{17}
\]

and enlarge the stage threshold so \(k_n\ge m\). All these quantities
are fixed before the final counting cutoff varies.

Put \(\delta=|\rho_{k_n}-\rho_m\circ\pi|\) and
\(U=\sum_wv_w\). Each residue class modulo \(3^{k_n}\) contains at
most \(33X/3^{k_n}\) possible integers in \([X,32X)\), by (16).
Source injectivity and \(v_w\le M/X\) consequently give, for every
nonnegative residue function \(f\),

\[
 \sum_wv_w f(x_w)\le33M\langle f\rangle_{k_n}.
\tag{18}
\]

Each \(\Psi_j\) is a permutation of the full ternary residue group.
Thus (18) applies to \(\delta\circ\Psi_j\) with the same average.
The coarse bound \(\rho_m\le(2/3)3^m\), the geometric sum
\(\sum_{j\ge0}4^{-j}=4/3\), and (T) give

\[
 \mathcal M_{n,X}
 \le(8/9)3^m U+44MC_*/m^2.
\]

By (11) and (17),

\[
 U\ge\eta:=\frac{9p}{32\,3^m}>0.
\tag{19}
\]

The same selected weights remain in \(U\). Only the nonnegative error
term was enlarged to the possible sources in a residue class; no
selection mask or residue factor was simply deleted.

### 7. Choosing the root for an arbitrary target

Let \(a>0\) with \(3\nmid a\), for the ordinary map whose odd arrow
is \(3n+1\). Choose \(e\in\{1,2\}\) with \(2^ea\equiv1\pmod3\).
The positive odd integers

\[
 R_j=(2^{e+2j}a-1)/3\qquad(j\ge1)
\]

reach \(a\) after \(1+e+2j\) ordinary arrows. Their next odd value is
the odd part of \(a\), which need not be \(a\) itself.
The elementary valuation identity
\(v_3(4^h-1)=1+v_3(h)\) proves
\(v_3(R_{j+h}-R_j)=v_3(h)\). Hence these roots represent every
residue modulo a fixed power of 3, with arbitrarily large representatives
in each class.

Among predecessors of a fixed odd endpoint, periodic predecessors either
do not exist or belong to that endpoint's one finite cycle. Consequently
all sufficiently large members of this particular family have no
positive return. Select one in the favorable unit residue from §3, above
both the height requirement and this finite exceptional range. Denote it
by \(M\). This selection is existential; it uses no effective bound on
a hypothetical nonprincipal cycle.

Now fix \(m\), all stage thresholds, and \(X_*\) as above. For every
integer \(Y\) sufficiently large that \(X=Y/32>X_*\), §§4–6 supply
distinct odd sources in \([Y/32,Y)\), each reaching \(M\) and hence
\(a\). Since each selected word weight is at most \(M/X\), (19) gives

\[
 \#\{x:0<x<Y,\ x\text{ reaches }a\}
 \ge XU/M\ge c_aY,
 \qquad c_a=\frac{9p}{1024M\,3^m}>0.
\tag{20}
\]

The root, modulus \(m\), positive constant, and cutoff are fixed for
this target. Only the chosen generation and finite word family vary
with \(Y\). The argument actually produces odd sources; the stated
ordinary predecessor count includes them.

## Certificates

- [`check_audit.py`](check_audit.py) (under a second): `python3 areas/convergence/results/predecessor-density-conditional-reconstruction/check_audit.py` recomputes finite instances of the written ingredients (central histories, histogram fibres, marginal laws, signed transfer identities, branch and tail checks, the density-mode cases of [`c2a-two-level-residue-relaxation`](../../attempts/c2a-two-level-residue-relaxation.md), `d`-controls and rejections) and compares them with [`audit_checks.json`](audit_checks.json). These support the written ingredients; they do not certify the external theorem or any upper bound.

## Remarks

**Assessment and exact remaining dependencies.**

The qualitative chain closes **conditional on (T)** and the explicitly
defined finite reference law. The histogram and terminal-transfer steps
do not require convergence of the root; cross-depth source injectivity
is used only after the separate nonreturn selection. Growing-modulus
errors, endpoint-dependent shifts, two different terminal losses, and
all-large-cutoff coverage have each been paid for.

What this audit has not established:

- An independent proof or formal rebuild of Tao's mixing theorem and
  the complete Lean dependency closure. This note imports the published
  theorem with finite constants and states the normalization explicitly.
- The huge fully explicit constant recipe in Section 8 of the companion,
  the target-one ordinary time constant, or Lau's later explicit result.
  The constants in (20) retain the imported mixing constants and an
  existential choice of a nonreturn root.
- A transfer theorem for another additive parameter \(d\). The histogram
  arithmetic alone admits such variants; a full transferred statement
  requires its own analysis and controls.
- Any upper-density-one absorption estimate. A nonempty bad component
  having a positive lower density is compatible with its existence.

Thus this note can support a literature-qualified calibration of the
linear predecessor-density ingredient. It cannot supply the missing
upper estimate at C.2a or be reported as an independently formal-verified
Collatz result.

- **Controls.** For `d > 1` the multiples of `d` are an exact nonabsorbing sector of density `1/d` ([`baseline-obligation-transfer-controls`](../baseline-obligation-transfer-controls/README.md)); the transferred lower bound is consistent with them, and a bad component at any permitted `d` would have positive lower density. The mechanism therefore does not distinguish `3x+1` from the controls: it is not a non-transfer step.
- **Use.** With the formal input of [`lau-2026-positive-density`](../../../../sources/lau-2026-positive-density.md) instead of (T), the `d = 1` consequence is [`nonabsorbing-set-linear-lower-density`](../nonabsorbing-set-linear-lower-density/README.md).
- **Programme label none**, under the rule that a calibration re-derives a published result with explicit constants: here the constants stay Tao's unspecified ones. Confirmed by the side lane (feed 18:08).
- **Explicit constants elsewhere.** The audited formal library proves an explicit mixing estimate in place of (T), but only for 3-adic levels `m >= 2^80000`; how large its constants are is recorded in [`explicit-tao-via-formal-mixing-constants`](../../attempts/explicit-tao-via-formal-mixing-constants.md).

## History

Migrated from `experiments/phase6/linear_density_audit/terminal_audit.md` (legacy batch `P6-004`, route node C.1a), with `audit_notes.md`, `transfer_scope.md`, `check_audit.py`, `audit_checks.json` and `verification.json`, at commit `be73a66`. ChatGPT main lane, 2026-10-18. One link in `transfer_scope.md` was repointed from `terminal_audit.md` to this README at the migration.
