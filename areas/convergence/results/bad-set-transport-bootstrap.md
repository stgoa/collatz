---
id: bad-set-transport-bootstrap
kind: result
title: What a half-descent transport inequality for the actual nonabsorbing set would give, and why it fails for 3x+d
status: written
claim: >
  Odd-only 3x+1 map S absorbed at 1; B the nonabsorbing positive odd seeds; for odd n > 1, L(n) the first odd
  iterate <= n/2, E = {odd n > 1 : L(n) undefined}, G(B) = {odd n > 1 : L(n) in B}; F, e, g the counts of B, E, G(B)
  through X weighted by fixed positive residue weights w_r modulo M; C_alpha(X) = max_(1<=Y<=X) F(Y)/Y^alpha (a
  finite maximum). (a) B = E disjoint-union G(B), so F = e + g. (b) Explicit S.1 input: for each supported d and
  integer X >= 32^9, E_d(X) <= (4 + 2d) X^(39/40). (c) Bootstrap: if the transport premise
  (P) g(X) <= kappa X^alpha C_alpha(floor(X/2)) holds for all X >= X0 with 0 <= kappa < 1, and e(X) <= D X^beta
  with beta < alpha, then B(X) <= (Cstar/w_min) X^alpha with Cstar = max(C0, D X0^(beta-alpha)/(1-kappa)); and (P)
  with e(X) = o(X) alone (even kappa < 2^(1-alpha)) gives B(X) = o(X). (d) For every fixed supported d > 1 the
  analogue of (P) is false for the actual nonabsorbing set B_d, because the odd multiples of d give
  limsup F_d(X)/X >= w_min/(2d) > 0 while S.1 gives e_d = o(X). Premise (P) itself is unproved for d = 1.
authors:
  - ChatGPT main lane (Codex)
created: 2026-10-18
depends_on: [fixed-factor-stopping-explicit-constants, arbitrary-target-linear-transport-barrier, baseline-obligation-transfer-controls]
tags: [convergence, phase6, stopping-time, transport, nonabsorbing-set, conditional, negative-control]
---

# What a half-descent transport inequality for the actual nonabsorbing set would give, and why it fails for 3x+d

## Statement

After [`arbitrary-target-linear-transport-barrier`](arbitrary-target-linear-transport-barrier/README.md) and [`growth-norm-transport-barrier`](growth-norm-transport-barrier/README.md) closed two arbitrary-target methods, the natural next premise is one restricted to the actual nonabsorbing set `B`, which is fully invariant (`1_B(n) = 1_B(S(n))`), unlike the constructed targets of those barriers. This node records the exact interface, the explicit input S.1 supplies, the conditional consequences of a transport inequality (P) for `B`, and the negative control proving that (P)'s `3x+d` analogue is false. The open premise itself is [`bad-set-half-descent-transport`](../questions/bad-set-half-descent-transport.md). Notation and the precise statements (a)–(d) are in the claim and in §§1–4 below; (S1b) is (b), the bootstrap (1)–(2) and the limsup argument (3) are (c), and §4 is (d).

The legacy note was "next-attempt design only": it earned no Phase 6 batch label and claims no transport estimate. Its derivations are complete and are recorded here as such.

## Proof

### 1. The distinction from arbitrary targets

Use ordinary odd-only Syracuse, absorbed at 1. All X below are integer cutoffs. Let B be the positive odd
integers that never reach 1. For n>1 let L(n) be the first odd iterate at
most n/2, when it exists; put E={odd n>1:L(n) is undefined}. Then

```
B = E disjoint-union G(B),
G(B) = {odd n>1:L(n) exists and L(n) in B}.
```

Unlike an arbitrary sparse target set, B is fully invariant:
1_B(n)=1_B(S(n)). The arbitrary-target residue-averaging theorem does not
prove that its constructed targets lie in B or satisfy this invariance.
It therefore does not refute a premise explicitly restricted to B.

Fix a finite modulus M and strictly positive weights w_r on its residue
classes. Let w_min and w_max be their minimum and maximum. Define

```
F(X) = sum_(n in B, n<=X) w_(n mod M),
e(X) = sum_(n in E, n<=X) w_(n mod M),
g(X) = sum_(n in G(B), n<=X) w_(n mod M),
C_alpha(X) = max_(integer 1<=Y<=X) F(Y)/Y^alpha,
```

with C_alpha(0)=0. For every finite X this maximum exists and is finite;
no global power-growth assumption is made. Exact disjointness gives
F(X)=e(X)+g(X). Positive finite weights give
w_min B(X)<=F(X)<=w_max B(X), so a finite weighted power norm has the same
growth exponent as an ordinary count. Merely choosing weights cannot
justify finiteness of either global norm.

### 2. A concrete transport premise

For example, fix alpha=99/100. Seek explicitly specified M, positive
rational weights, an integer X0>=2 and a rational 0<=kappa<1 such that
for the actual d=1 set B and every integer X>=X0,

```
g(X) <= kappa X^alpha C_alpha(floor(X/2)).           (P)
```

This is a proposed B-specific estimate, not a consequence of invariance
already proved here. It uses only a finite input maximum and therefore
does not hide the desired finite global norm in its hypotheses. The
whole first-half map, including arbitrary input-dependent odd clocks,
must be covered. A finite word catalogue alone does not establish (P).

#### Conditional power bootstrap with an explicit constant

Suppose additionally that, for constants D>=0 and 0<=beta<alpha,

```
e(X) <= D X^beta  for every integer X>=X0.          (E)
```

Set

```
C0 = max_(1<=Y<X0) F(Y)/Y^alpha,
D0 = D X0^(beta-alpha),
Cstar = max(C0, D0/(1-kappa)).                     (1)
```

Then C_alpha(X)<=Cstar for every integer X>=1, and hence

```
B(X) <= (Cstar/w_min) X^alpha.                    (2)
```

**Proof.** Fix X and choose an integer Y<=X attaining C_alpha(X).
If Y<X0, its value is at most C0. Otherwise, the exact decomposition,
(P), and (E) give

```
C_alpha(X) = F(Y)/Y^alpha
 <= D Y^(beta-alpha) + kappa C_alpha(floor(Y/2))
 <= D0 + kappa C_alpha(X).
```

Rearrangement proves the bound in (1). All quantities in this argument
are finite maxima at the chosen cutoff. There is no passage from an
infinite norm to an inequality of the form infinity<=infinity.

Without deciding membership in B, use
C0<=(w_max/2)(X0-1)^(1-alpha): there are at most Y/2 odd bad seeds through
Y, since 1 is excluded. Supplied verification of the initial interval can
sharpen this finite unconditional bound.

#### Explicit input from existing S.1, not a new calibration result

Put beta=39/40 and r=16807/18432. Exact integer checks give

```
32*16807^40 < 18432^40,
3^200 < 2^395.                                    (S1a)
```

For any supported fixed d and integer X>=32^9, take
m=floor(log_32 X)>=9 and k=5m. In S.1 let b_m be the exact number of bad
parity residue classes and delta=b_m/2^(5m-1). Its established bound is
delta<=(8/7)r^m. Also put Z=ceil(4d(3/2)^(5m)). The S.1 upper bound on
the number of seeds without half descent within k odd arrows is

```
delta*ceil(X/2) + b_m + ceil(Z/2).
```

The first inequality in (S1a) gives r^m<=32^(-m/40), hence

```
delta*ceil(X/2) <= (16/7) X^beta,
b_m <= (4/7) X^beta.
```

For the first bound use ceil(X/2)<=X, 32^m>X/32 and 32^(1/40)<2.
For the second use b_m=delta*32^m/2 and 32^m<=X. The second inequality
in (S1a) gives (3/2)^(5m)<=32^(m*beta)<=X^beta. Therefore
Z<=4d X^beta+1 and ceil(Z/2)<=2d X^beta+1. Summing, and using X^beta>=1,
proves

```
E_d(X) <= (4+2d) X^(39/40),   X>=32^9.             (S1b)
```

Here E_d excludes seed 1; the S.1 finite-horizon failure bound also counts
that seed, which only makes it an upper bound. No all-horizon search is
performed: E_d is contained in the failures at this particular finite
horizon k(X).

For ordinary d=1 and fixed bounded weights, (E) thus holds with
D=6w_max, beta=39/40. Increase X0 to include 32^9 and the proposed
transport threshold. With alpha=99/100, (1) becomes

```
Cstar = max(C0, 6w_max X0^(-3/200)/(1-kappa)),
C0 <= (w_max/2)(X0-1)^(1/100).                     (S1c)
```

Both integer comparisons in (S1a) were checked exactly. This derives a
convenient explicit consequence of existing S.1; it supplies none of
(P). The missing new step remains the proposed transport inequality,
including its all-cutoff quantifier and actual B-invariance.

#### A density consequence using only the existing S.1 input

In fact (P), together with e(X)=o(X), already implies F(X)=o(X).
This avoids requiring (E) for a density-only conclusion.

Let

```
L = limsup_(X->infinity) F(X)/X.
```

It is finite because F(X)<=w_max*ceil(X/2). For 0<alpha<1,

```
limsup C_alpha(X)/X^(1-alpha) = L.                 (3)
```

The lower inequality follows by taking Y=X. For the upper inequality,
given eta>0, all sufficiently large Y satisfy F(Y)/Y<=L+eta.
Their contributions to C_alpha(X)/X^(1-alpha) are at most L+eta;
the maximum over the finitely many earlier Y tends to zero. This proves
(3). Dividing F=e+g by X and using (P) now gives

```
L <= kappa*2^(alpha-1)*L.
```

The coefficient is strictly less than one, so L=0. S.1 supplies e=o(X):
E is contained in the no-half-descent set at every fixed finite horizon,
and its density can therefore be made arbitrarily small. Fixed bounded
weights preserve this conclusion. This density argument would even work
for kappa<2^(1-alpha); the sharper range in (P) gives the simple constant
(1) for the power bootstrap.

### 3. Why a finite residue vector is not automatically closed

Let B_u^(j)(X) count odd bad n<=X with n=u mod3^j. For d=1, exact inverse
arithmetic gives

```
B_u^(j)(X)
 = sum_(a>=1)
   B_((3u+1)2^(-a) mod3^(j+1))^(j+1)((3X+1)/2^a). (4)
```

There is no absorber term because 1 is not in B and raw S_1(1)=1.
The source residue requires one more ternary digit at the target.
For a general word of k odd arrows it requires k more ternary digits.
Also a=1 has target cutoff (3X+1)/2, larger than X. Thus (4) is not a
closed finite linear system on one fixed list of residues and decreasing
cutoffs.

The coarse count is the sum over three finer lifts. Replacing the lifts
by equal thirds requires a new distribution statement about B. Taking
the largest compatible lift can give an upper bound, but loses the
correlations one hoped would distinguish B from arbitrary targets.
Additional exact relations may permit rigorous finite inequalities; the
increase in precision is not an impossibility theorem for every finite
state method. A proposed matrix certificate must specify these lift
constraints, all advanced cutoff terms, and every omitted branch before
claiming an operator bound or a spectral-radius contraction.

Krasikov–Lagarias use finite residue difference inequalities with
minimization over finer ternary classes, and deal explicitly with advanced
arguments. Their certified conclusion is a lower bound on inverse-basin
growth, not an upper bound on B. A positive vector or spectral-radius
calculation must be tied to the correct inequality direction. See
[their primary paper, Sections 2–6](https://arxiv.org/html/math/0205002v1).

### 4. A negative control that tests the premise without assuming finite norm

For each fixed supported d>1, let B_d be the actual nonabsorbing odd set
for S_d absorbed only at 1. Every positive odd multiple of d belongs to
B_d: divisibility by d is invariant, and S_d(d)=d is an exact fixed cycle.
Thus, for any fixed strictly positive finite residue weights,

```
limsup F_d(X)/X >= w_min/(2d) > 0.                 (5)
```

Define E_d and G_d on n>1 exactly as above. Hitting 1 would half-descend
from every odd n>1, so the exact decomposition B_d=E_d disjoint-union
G_d(B_d) holds. S.1 gives E_d(X)=o(X), and therefore e_d(X)=o(X).
If the analogue of (P) held for this actual B_d, the argument (3) would
contradict (5). This refutes the analogue for every supported d>1, with
no assumption that the global alpha-norm is finite and no numerical
orbit scan. The finite input maxima in (P) remain well defined.

The d=5 cycle 19->31->49->19 provides an additional nonprincipal control
outside the multiples-of-d class, but its finite cycle alone does not
establish a growth-norm contradiction. The rigorous contradiction above
uses the entire invariant multiples-of-d set and S.1's density estimate.

In contrast, a theorem conditional on an already finite global
alpha-norm cannot be refuted merely by pointing to the multiples-of-d
set: that set has infinite alpha-norm for alpha<1 and would violate the
premise. The truncated form (P) avoids this loophole.

### 5. What would this give toward convergence?

The established Krasikov–Lagarias predecessor bound has exponent0.84.
An upper bound with exponent99/100 alone does not contradict it. If a
nonempty B contains an odd a not divisible by3, all predecessors of a
are nonabsorbing. Such an a exists after one ordinary odd arrow from
any bad seed. An odd upper bound B(X)<=C X^alpha gives the all-integer
upper bound

```
sum_(j>=0) B(X/2^j) <= C X^alpha/(1-2^(-alpha)).     (6)
```

Hence the established0.84 lower bound gives a contradiction only if the
upper exponent is strictly below0.84.

Likewise B(X)=o(X) implies that the all-integer nonabsorbing count is
o(X): in the same sum, first fix J and use B(X/2^j)=o(X) for j<J;
the remaining terms are bounded by the geometric tail O(X/2^J).
Let X tend to infinity and then let J tend to infinity.

**External candidate under separate audit, not a premise here:** Mazur's
2026 primary manuscript claims a positive lower density of predecessors
for every fixed target not divisible by3, and consequently positive lower
density of the nonabsorbing set if it is nonempty. The paper's statement
has been read; its analytic and formal dependencies have not been audited
in this note. The separate root audit is also inspecting Lau's refinement
at AxiomMath/CollatzPositiveDensity commit
`3a38bfbb70379e051b51155def1423846fab3a90`.
See [Mazur, Theorem1.1 and Corollary1.2](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf).

Conditional on verification of that stronger lower theorem, either (2)
with any alpha<1 or the density conclusion following (3) would rule out
a nonempty B. This strengthens the motivation to test (P), but supplies
none of its missing proof. With that external input, (P) would itself be
a Collatz-equivalent criterion: convergence makes B empty, while (P)
would force convergence. It must not be described as an easier theorem
merely because it has been written as a weighted inequality.

## Remarks

- **Recommendation of the legacy note.** Keep (P) as a precise open next attempt. Before searching for weights, write a sound finite inequality system that incorporates actual invariance, ternary-lift constraints and the complete first-half map. Test the same claimed reasoning on `B_d`, where §4 proves it must fail. Do not publish an additional weighted arbitrary-target barrier as if it settled this `B`-specific premise.
- **Not easier than Collatz.** With the audited linear lower bound of [`nonabsorbing-set-linear-lower-density`](nonabsorbing-set-linear-lower-density/README.md) (which postdates this note; §5 still calls the Mazur claim an external candidate under audit), either the power bound (2) for any `alpha < 1` or the density conclusion after (3) would rule out a nonempty `B`, so (P) would be a Collatz-equivalent criterion: convergence makes `B` empty, and (P) would force convergence. Writing it as a weighted inequality does not make it easier.
- The first attempt on the upper side, [`c2a-two-level-residue-relaxation`](../attempts/c2a-two-level-residue-relaxation.md), shows that the leading-coefficient relaxation of the exact residue system (§3's identity (4)) admits a positive-density profile, so it cannot prove (P).

## History

Migrated from `experiments/phase6/NEXT_ATTEMPT.md` at commit `be73a66`. ChatGPT main lane, 2026-10-18, prepared during the P6-003 verification and retained for the next side-lane review; no batch label. The two exact integer comparisons in (S1a) were checked exactly when it was written.
