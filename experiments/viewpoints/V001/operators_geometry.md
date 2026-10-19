# V001 — Operators, orbit geometry, and potential theory

**Status: bounded viewpoint comparison; proposals, not new Collatz results.**
2026-10-18. This first pass supplies three candidate languages, elementary
worked examples, and tests that could reject an unhelpful translation.
All deterministic times count odd Syracuse arrows, with 1 absorbed.
Write \(S_d(n)=(3n+d)/2^{v_2(3n+d)}\) for odd \(n>1\), where
\(d>0\) is odd and coprime to 3; \(S=S_1\).

Relevant existing constraints are [R7](../../../archive/docs/RESULTS.md), the
[finite-cone compiler](../../residual_progress/duality/FINITE_CONE.md),
[arbitrary-target transport barriers](../../phase6/growth_norm_transport/GROWTH_NORM_TRANSPORT.md),
and the [actual-basin density audit](../../phase6/linear_density_audit/next_upper_attempt.md).
No new universal current supply, distribution estimate, or novelty claim
is supplied here. Published frameworks below are background; the proposed
Collatz applications have not inherited their conclusions automatically.

## A. Absorbing transfer operators and function spaces

**1. Objects.** On \(\Omega=\{3,5,7,\ldots\}\), define the killed
pushforward \(P:\ell^1(\Omega)\to\ell^1(\Omega)\) by
\((P\mu)(y)=\sum_{S(n)=y}\mu(n)\). Its dual on \(\ell^\infty\) is
\(Qf(n)=1_{S(n)>1}f(S(n))\). Both are contractions. With
\(h_o(X)=\sum_{n\le X,\ n\text{ odd}}1/n\), put
\(\nu_X(n)=1_{n\le X}/(nh_o(X))\), for \(n\in\Omega\).
Then \(\|P^H\nu_X\|_1\) is exactly the relative logarithmic mass
still unabsorbed after \(H\) arrows. The missing mass includes seed 1.

**2. Structural gain.** Killing retains the desired component and makes
survival a positive operator observable. It distinguishes convergence for
one specified family \(\nu_X\) from an operator-norm claim for every
input. Operator encodings of Collatz already exist: Neklyudov's
[primary paper, Sections 1–2](https://arxiv.org/html/2106.11859v1), uses
monomial transport for the shortcut map. That is background, not a spectral
theorem imported into this different odd, killed sequence-space model.

**3. Translated unresolved gap.** A useful estimate must control the
specific \(\nu_X\) uniformly as \(X\to\infty\), while retaining
arithmetical concentration. The Phase 6 counterexamples prohibit simply
choosing a power-growth norm and demanding contraction on all target sets.
Moreover, \(\|P^H\|=1\) for every fixed \(H\): successive integral
inverse branches, chosen above their parent and avoiding multiples of 3,
give absorbed seeds with arbitrarily long paths. Strong convergence on every point mass
would merely restate Collatz. A new space needs a proved estimate, not a
name such as “spectral gap.”

**4. Worked example.** Since \(13\to5\to1\),
\(P\delta_{13}=\delta_5\) and \(P^2\delta_{13}=0\).
For \(\mu=(\delta_{13}+\delta_5)/2\), survival mass is
\(1,1/2,0\). The finite matrix on these two states is nilpotent; this
certifies these states and says nothing about an omitted source.

**5. Cycle controls.** Under \(d=5\), the cycle
\(19\to31\to49\to19\) gives an invariant probability vector
\((\delta_{19}+\delta_{31}+\delta_{49})/3\) with eigenvalue 1.
Any proposed space that silently excludes this vector has changed the test.

**6. Cheapest meaningful test.** Write down one proposed norm completely
and test its asserted estimate on these point masses, the invariant cycle,
and the exact Phase 6 sparse-target witnesses. Then derive its action on
\(\nu_X\), including residue and cutoff errors. Reject a norm whose only
gain comes from discarding unsupported mass or assuming absorption.

**7. Intermediate milestone.** Obtain explicit \(X_0\) and computable
\(H(X)\) with \(\|P^{H(X)}\nu_X\|_1\le1/10\) for every integer
\(X\ge X_0\). This proves 90% logarithmic absorption, allows a remaining
bad basin, and is not Collatz-equivalent. It is an ambitious target, not an
estimate supplied by the current literature audit.

## B. Graph currents, cohomology, and orbit groupoids

**1. Objects.** Keep every positive odd integer, but make \(S_d\) a
partial map undefined at 1, so the absorber creates no artificial loop.
Use arrows \((x,k-l,y)\) whenever the defined iterates satisfy
\(S_d^k(x)=S_d^l(y)\). Compose by adding the integer clock differences.
Besides this clock cocycle, retain
\(A_k(x)-A_l(y)\), where \(A_k\) sums the exact valuations along
the \(k\)-arrow path. Extending both paths by the same tail preserves
both differences. The discrete space fits the local-homeomorphism
construction in [Armstrong, Brix, Carlsen and Eilers, Section 2.2](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/conjugacy-of-local-homeomorphisms-via-groupoids-and-calgebras/1F61F3AA4CD2F2F8D65988A9AF03A954).

**2. Structural gain.** Component quotients forget when paths meet and
whether a component contains a cycle. The groupoid retains meeting lags
and periodic isotropy, while arithmetic labels retain valuation history.
This can organize consistency of overlapping local comparisons. It does
not supply the comparisons: each arrow still requires an actual meeting.
Finite-current divergence and the zeroth component obstruction are already
R7. Renaming their cokernel “homology” adds no result.

**3. Translated unresolved gap.** One needs an arithmetic restriction or
gluing theorem that extracts something not already contained in supplied
paths. The clock and valuation labels alone do not control the affine
intercept. Nor does a compactification of the discrete state set preserve
integer reachability automatically. An all-input vanishing obstruction
would recreate the old universal-current obligation.

**4. Worked example.** The arrows \(13\to5\) and \(53\to5\) have
valuations 3 and 5. Their groupoid arrow \((13,0,53)\) has clock lag
zero and valuation difference \(-2\). Its ordinary current has divergence
\([13]-[53]\). Thus the extra label distinguishes histories whose meeting
time alone does not; it does not discover a previously unknown merger.

**5. Cycle controls.** The \(d=5\) cycle has nontrivial isotropy
\((19,3,19)\), with valuation sum 5. Its three-arrow affine map is
\(x\mapsto(27x+95)/32\), fixing 19. Dropping the intercept falsely
turns its multiplicative factor \(27/32\) into a progress argument.
The partial-map convention removes only the designated absorber's loop.

**6. Cheapest meaningful test.** On one frozen comparison and its inverse,
compute both cocycles and the full affine composition. Check whether a
proposed invariant detects any obstruction beyond the existing signed
current. If it is just an endpoint coboundary or the old component mass,
reject the claimed structural gain before introducing a C*-algebra.

**7. Intermediate milestone.** Investigate exclusion of positive \(d=1\)
cycles in the explicitly restricted cyclic word language generated by
valuation blocks \((1,3),(1,1,3),(1,1,1,3)\). Length is unbounded but
the language omits many possible cycles and all divergent trajectories.
The \(d=5\) control already belongs to it. First compare this target with
the frozen mechanical-word theorem R71 and existing literature; no novelty
or exclusion is asserted. The groupoid earns further attention only if its
labels help beyond elementary affine-word algebra.

## C. Potential theory, Dirichlet energy, and possible boundaries

**1. Objects.** Symmetrize the actual odd arrows, assigning conductance
\(1/n\) to the edge from \(n>1\) to \(S_d(n)\). Add parallel
conductances and ignore self-loops. Each vertex has finite total
conductance because its inverse branches grow geometrically. This defines
an auxiliary reversible walk, with energy
\(\mathcal E(f)=\sum_{n>1}(f(n)-f(S_d(n)))^2/n\).
For finite \(F\ni1\), let \(u_F(n)\) be its probability of hitting
1 before leaving \(F\), extended by zero outside. Every omitted incident
edge remains a boundary conductance.

**2. Structural gain.** Dirichlet problems provide comparison and energy
methods for a geometric observable. Conductance \(1/n\) matches the
logarithmic scale weighting. The framework is standard; see
[Doyle–Snell, Sections 1.3–1.4](https://math.dartmouth.edu/~doyle/docs/walkspdf/walks.pdf)
and [Lyons–Peres, Chapter 2](https://rdlyons.pages.iu.edu/prbtree/).
This walk is not a probabilistic model for forward Collatz. Its useful
one-sided link is elementary: a finite undirected path to 1 lies in the
absorbing functional-graph component, so
\(u_F(n)\le1_{\{n\text{ absorbs}\}}\).

**3. Translated unresolved gap.** An energy or boundary estimate must
give a quantitative lower bound on the logarithmic average of \(u_F\)
for growing \(F\). Recurrence within a component does not connect that
component to 1. Positivity at every vertex is again convergence-equivalent.
A Martin-boundary argument additionally needs the appropriate finite
Green kernel, or a specified discounted resolvent; transience cannot be
assumed. No Martin representation theorem is applied here.

**4. Worked example.** Take \(d=1,F=\{1,5\}\). The other neighbors
of 5 are \(x_j=(10\cdot4^j-1)/3\), \(j\ge0\). Therefore
\[
u_F(5)=\frac{1/5}{1/5+\sum_{j\ge0}1/x_j}\ge\frac9{29},
\]
because \(x_j\ge3\cdot4^j\) bounds the sum by \(4/9\).
This retains the entire infinite incoming boundary. Omitting it would
incorrectly report probability 1 for this finite-domain experiment.

**5. Cycle controls.** For \(d=5\), the component containing
\(19,31,49\) cannot meet 1, so its \(u_F\) values are zero for every
\(F\). Wiring that component's frontier to the absorbing boundary would
erase the control. The \(d=61\) nonprincipal cycle requires the same test.

**6. Cheapest meaningful test.** Derive a uniform geometric bound for
the omitted inverse-edge conductance, then compare two nested finite
Dirichlet domains while retaining every boundary term. Determine whether
the estimate improves with domain growth and survives both cycle controls;
a favorable finite plot alone supplies no all-scale conclusion.

**7. Intermediate milestone.** Exhibit explicit growing finite domains
\(F_X\) and \(X_0\) such that
\(\sum_{n\le X,\ n\text{ odd}}u_{F_X}(n)/n\ge h_o(X)/2\)
for every integer \(X\ge X_0\). This would prove a concrete 50%
logarithmic absorption bound while allowing bad components. It requests
an energy-based quantitative mechanism, not universal connectivity.

## First-pass judgment

Operators give the cleanest target observable. Potential theory offers
the most different toolset, at the cost of introducing an auxiliary process
whose estimates may be weaker. Groupoids preserve useful information but
have the greatest risk of restating existing algebra. These are priorities
for bounded tests, not a recommendation to abandon the integer graph or
begin an unrestricted proof campaign.

The subsequent [tiny-domain discrimination probe](potential_probe.md)
finds no demonstrated advantage over existing component certificates:
positive voltage is the same connectivity information, while quantitative
voltage loses mass through genuine boundary edges. Its possible value lies
in a still-missing uniform arithmetic bound, not in the reformulation itself.
