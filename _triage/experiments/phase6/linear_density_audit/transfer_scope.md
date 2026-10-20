# Corrected Tao input and transfer to positive odd additive parameters

**Status:** written statement-alignment audit and transfer proof, using
the imported mixing theorem and the arithmetic derivations in
[audit_notes.md](audit_notes.md) and [terminal_audit.md](terminal_audit.md).
This is not an independent proof of Tao's theorem or a formal replay.
The transferred statement concerns positive predecessor density, not
universal absorption. No novelty claim is made.

## 1. Corrected primary source and exact normalization

The primary record identifies
[arXiv:1909.03562v7](https://arxiv.org/abs/1909.03562v7) as Tao's revision
of 16 July 2026. Its
[full text](https://arxiv.org/html/1909.03562v7) states Proposition 1.14
for **all integers** \(1\le m\le q\), with an implied constant depending
only on the fixed exponent \(A>0\). The temporary regime
\(0.9q\le m\le q\) in Section 6 belongs to its proof, not to the final
theorem's hypotheses.

Let \(\mu_q\) be the probability law of the finite Syracuse random
variable in equation (1.22). Equation (1.23) gives exact marginal
compatibility:

\[
 \sum_{y\equiv z\ (3^m)}\mu_q(y)=\mu_m(z).
\tag{1}
\]

Equations (1.24) and (1.29), using reversal of an independent geometric
sequence, identify this law with the recursion used in the audit:

\[
 Y_0=0,\qquad
 Y_{q+1}=2^{-E_{q+1}}(3Y_q+1)\pmod{3^{q+1}},
 \qquad\Pr(E_i=a)=2^{-a}\ (a\ge1).
\]

Define \(\rho_q=(2/3)3^q\mu_q\), with the average over a residue group
normalized by its cardinality. Then direct algebra and (1) give

\[
\begin{aligned}
 \langle|\rho_q-\rho_m\circ\pi_{q,m}|\rangle_q
 &=\tfrac23\sum_{y\bmod3^q}
       |\mu_q(y)-3^{m-q}\mu_m(y\bmod3^m)|\\
 &=\tfrac23\operatorname{Osc}_{m,q}(\mu_q).
\end{aligned}
\tag{2}
\]

The oscillation here is exactly the full sum in Tao's equation (1.27).
Thus Proposition 1.14, equation (1.26), gives precisely the imported
estimate (T), with suitable finite constants \(C_6,C_2\). There is no
unresolved factor of 2 from conventions for total variation: (2) uses
the displayed oscillation sum directly. The factor \(2/3\) is inserted
once in the definition of \(\rho\), not once at each generation.

The endpoint \(m=q\) gives zero error. Small positive \(m\) are included
by the theorem; \(m=0\) is not imported. Means are over the full residue
group, and no conditioning or renormalization to its units is used.
The laws vanish on nonunits when \(q\ge1\), but their means are still
\(2/3\). This audit finds no mismatch between the corrected statement
and the specific mixing estimate used in the two notes.

## 2. Precise transferred statement

Fix an integer \(d>0\) with \(\gcd(d,6)=1\). Let

\[
 C_d(n)=\begin{cases}n/2&2\mid n,\\3n+d&2\nmid n,\end{cases}
 \qquad
 S_d(n)=\frac{3n+d}{2^{v_2(3n+d)}}\quad(n\text{ positive odd}).
\]

For every fixed positive integer target \(a\) with \(3\nmid a\), the
transferred argument gives constants \(c_{d,a}>0\) and \(X_{d,a}\)
such that every integer \(X\ge X_{d,a}\) has at least \(c_{d,a}X\)
distinct **positive odd** starts below \(X\) whose ordinary \(C_d\)
orbit reaches \(a\). The constructed paths do not visit 1 before
reaching \(a\), so this conclusion also holds when the ordinary map
is absorbed at 1. For odd \(a\), the corresponding odd-only conclusion
holds with either raw or absorbed \(S_d\).

No condition \(\gcd(a,d)=1\) is required. Constants may depend on both
fixed parameters. No uniform time bound, natural-density limit, or
uniform lower coefficient over targets or additive parameters is claimed.
This is a consequence of the same imported Tao theorem plus the
transferred arithmetic below.

## 3. Reference laws and finite transfers are conjugate

Multiplication by \(d\) is a permutation of every
\(G_q=\mathbb Z/3^q\mathbb Z\), commuting with reduction to lower
levels. Put

\[
 \mu_{q,d}(y)=\mu_q(d^{-1}y),\qquad
 \rho_{q,d}(y)=\rho_q(d^{-1}y).
\]

These are the finite laws associated to the affine update
\(z\mapsto(3z+d)/2^E\). They have the same means, unit support,
compatible marginals, and the **same constants** in (T), since all
relevant sums are simply permuted.

For a fixed inverse-order word \(w\), its weight remains
\(\omega_w=3^{|w|}2^{-A(w)}\). If \(F_{w,1}(z)=\omega_wz+\beta_w\)
denotes its finite affine injection, then

\[
 F_{w,d}(z)=\omega_wz+d\beta_w
           =dF_{w,1}(d^{-1}z).
\tag{3}
\]

The weighted transfers have the corresponding conjugacy. Their exact
average absolute-mass multiplier remains \(2^{-A(w)}\). Prefix codes,
their geometric probabilities, and the omitted-prefix average are
unchanged. Consequently every reference-transfer comparison in the
earlier notes holds for \(\rho_{q,d}\).

At an odd physical target, the inverse equation is
\(x=(2^aR-d)/3\). A nonempty fiber again forces successive integrality;
because \(d\) is odd, each resulting integer is odd. Positivity follows
from the height bounds in the next section, and then the specified
valuation \(a\ge1\) is exact. Unit support is preserved because
\(S_d(x)\equiv d2^{-a}\not\equiv0\pmod3\).

## 4. Every physical estimate has a controlled parameter change

Require the root height \(M\ge d16^{b_0}\), and maintain block-parent
height \(R\ge d16^b\). The single-block affine offset is now at most
\(d2^b\). Thus its subtraction still costs at most half of its parent,
and the same physical growth and weight estimates hold:

\[
 \tfrac14(4/3)^bR\le x\le2^{K+1}(4/3)^bR,
 \qquad \omega\le16^{-\lfloor b/100\rfloor}.
\]

The next endpoint is at least \(d16^{b+\lfloor b/100\rfloor}\).
The complete affine offset is at most \(d2^{b_0+1}\), while the full
weight still satisfies \(W\le16^{b_0-b_n}\). Hence the transferred
histogram bound is

\[
 3^qH_{n,q,d}(y)
 \le P_n\left(d2^{b_0+1}+16^{b_0}(9/16)^{b_n}\right),
 \qquad q\le2b_n.
\tag{4}
\]

In the subsequent norm bound replace \(C_{b_0}\) by

\[
 C_{b_0,d}
 =6(4b_0^{3/5}+1)(d2^{b_0+1}+16^{b_0}).
\tag{5}
\]

This is finite for each fixed \(d\) and independent of the numerical
root. No source multiplicity changes: a fixed source and fixed depth
still determine a unique deterministic valuation word, and its first
crossing rules still determine its cuts.

The central and terminal reference probabilities are unchanged. The
uniform variation and both terminal error bounds therefore persist
with (5), and retain their summability. The favorable ternary residue
can still be chosen before its numerical representative.

The admissible physical intervals \(L_b(R),U_b(R)\) use the same formulas
as before, with the larger actual parent \(R\). Endpoint ratios, the
number of possible shifts, and the all-scale overlap proof remain
unchanged. The counting-modulus check is stronger:

\[
 X>L_b(R)\ge d16^b/(4\,3^b)\ge3^b\ge3^{k_n}.
\]

Reducing the terminal overshoot by an even amount retains integrality,
since powers of 4 are 1 modulo 3. Its reconstruction map becomes

\[
 \Psi_{j,d}(x)=4^jx+d(4^j-1)/3,
\tag{6}
\]

with the same weight factor \(4^{-j}\). The translation is integral,
and multiplication by \(4^j\) is a unit modulo every power of 3.
Thus (6) permutes the full residue group and the same error-averaging
step applies. Finally, \(M=W x+d\beta\) still gives \(xW\le M\), so
the constants 33 and 44 in the distinct-source census are unchanged.

## 5. Every permitted target supplies the required root

Fix \(a>0\) with \(3\nmid a\). Choose an integer \(e\ge1\) such that
\(2^ea\equiv d\pmod3\) and \(2^ea>d\). Both conditions are possible
because increasing \(e\) by 2 preserves the first and makes the second
eventually true. Then

\[
 R_j=\frac{2^{e+2j}a-d}{3}\quad(j\ge0)
\tag{7}
\]

are positive odd integers, with an ordinary path of length
\(1+e+2j\) to \(a\). They all have the same next odd state, namely
the odd part of \(a\). Their differences satisfy

\[
 R_{j+h}-R_j=2^{e+2j}a(4^h-1)/3,
 \qquad v_3(R_{j+h}-R_j)=v_3(h).
\]

Therefore (7) contains arbitrarily large representatives of every
residue modulo any fixed power of 3. This uses \(3\nmid a\), not
coprimality of \(a\) with \(d\).

There is also a direct nonreturn argument: at most one member of (7)
can be periodic under the raw odd map. If two distinct members were
periodic, their common successor would put both in the same finite
cycle, which has only one cycle-predecessor of that successor. Thus
any favorable residue contains a nonreturn representative above the
required height. Select one as \(M\). Source injectivity across
different depths then follows exactly as in the terminal audit.

The leading inverse-history paths do not touch the absorber. For a
partial word of depth at most \(h_b\), write
\(R=W_i z+d\beta_i\). Both \(W_i\le2^b\) and \(\beta_i<2^b\),
so

\[
 z>d(8^b-1)>1.
\tag{8}
\]

The final ordinary path from the selected root to \(a\) starts with
\(3M+d=2^{e+2j}a\) and then only halves until it reaches \(a\).
It cannot visit 1 before that target. This explicitly establishes
the absorbed-map statement rather than assuming that arbitrary raw
predecessor paths survive absorption.

With this root fixed, choose the coarse modulus and stage threshold
as in the terminal audit. Its constant formula
\(c_{d,a}=9p/(1024M3^m)>0\) remains valid with the transferred
thresholds. All sufficiently large integer cutoffs are covered.

## 6. Restrictions and cycle controls

For \(3\nmid d\), a target divisible by 3 has no predecessor path
containing an odd ordinary step: every such step lands in a ternary
unit and subsequent halvings preserve that property. Its raw ordinary
predecessors are exactly \(2^ja\), \(j\ge0\), and have density zero.
Thus the target restriction is necessary.

If \(3\mid d\), multiplication by \(d\) is not invertible on the
ternary groups, the reference law is not the required permutation,
and even the conclusion for all ternary-unit targets fails. Negative
or even additive parameters are also outside this proof's positivity
and odd-valuation hypotheses.

For every odd \(d>1\), \(S_d(d)=d\). Moreover
\(S_d(dm)=dS_1(m)\) for positive odd \(m\), and all positive multiples
of \(d\) remain multiples of \(d\) under the ordinary map. They never
reach 1 and have natural density \(1/d\). The transferred predecessor
lower bound is compatible with these exact controls, including
\(d=5,7,13,61\).

For a hypothetical nonabsorbing component at any permitted fixed
\(d\), choosing a ternary-unit target in that component and applying
the absorbed predecessor statement forces a positive lower density
of nonabsorption. Thus upper-density-one absorption would imply
universal absorption for these maps as well. At \(d>1\) its premise
is false by the multiples-of-\(d\) control.

**Transfer conclusion:** the linear predecessor-density mechanism is
transferable under the exact positive-odd, ternary-unit hypotheses
above. It is not a step that distinguishes \(3x+1\) from the supported
cyclic controls. A successful proof at C.2a still needs an additional
property whose claimed upper estimate fails on those controls.
