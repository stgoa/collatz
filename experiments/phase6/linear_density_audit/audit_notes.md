# C.1a: seed-uniform weighted-history audit

**Status:** written independent rederivation of the residue histogram bound
and its conditional mixing consequence. This is an audit of a published
manuscript ingredient, not a novelty claim, a complete independent check of
the linear-density theorem, or a Collatz proof. No Lean replay is asserted
here. This note belongs to P6-004.

## Primary sources and exact audit boundary

- Lech Mazur, [*Explicit Positive-Density Collatz Convergence in Logarithmic
  Time*, v2.1](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf),
  especially (2.3), (3.1)–(3.11). The website says v2.1 preserves the
  mathematical body of the v2.0 cited by the successor manuscript.
- Mazur, [*Positive Lower Density of Collatz Predecessors*, v1.0](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf),
  Proposition 3.1 and Appendix A.
- Terence Tao, [*Almost all orbits of the Collatz map attain almost bounded
  values*, Proposition 1.14](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/almost-all-orbits-of-the-collatz-map-attain-almost-bounded-values/1008CC2DF91AF87F66D190C5E01C907F).

The histogram estimate below is arithmetic. The variation conclusion uses
Tao's finite-distribution mixing estimate as an explicit external input.
The last-block selection, all-scale coverage, and complete formal import
closure remain separate dependencies of C.1a.

## 1. Clocks, histories, and scale parameters

Use the raw positive odd map

\[
 S(x)=(3x+1)/2^{v_2(3x+1)}.
\]

All histories considered below stay above 1. Thus their arrows also agree
with the repository's absorbed convention. A word is listed in **inverse
order**, from the fixed root outwards. Its depth counts odd arrows, while
its valuation sum counts the divisions by 2. Neither count is an ordinary
unaccelerated clock.

Let \(b_0\ge325\) be an integer, and put

\[
 b_{j+1}=b_j+\lfloor b_j/100\rfloor,
 \quad K_j=\lfloor j/100\rfloor,
 \quad m_b=\lceil b^{3/5}\rceil,
 \quad B(t)=\lceil t\log_2 3\rceil.
\]

In particular, **the cap is \(\lfloor j/100\rfloor\), not
\(\lfloor b_j/100\rfloor\)**. The enlarged caps in the explicit-constants
section are treated separately below.

At scale \(b\), write \(w_b=\lfloor3b/5\rfloor\),
\(\ell_b=b-w_b\), \(h_b=b+w_b\). The central shift makes the crossing
barrier

\[
 H_b(s)=2b+B((s-b)_+)-B((b-s)_+).
\]

A block is admitted only when it is an exact positive odd inverse path,
uses the specified first crossing after the lower-endpoint miss, has
\(\ell_b\le s\le h_b\), and has valuation sum
\(H_b(s)\le A\le H_b(s)+K_j\). Central blocks additionally have
\(|s-b|\le m_b\). Requiring some endpoints to be units modulo 3 only
restricts this family and cannot enlarge the counting upper bounds.

Fix any positive odd root \(M\ge16^{b_0}\). No convergence or nonreturn
hypothesis on \(M\) is used. A generation-\(n\) history consists of \(n\)
successive central blocks at the prescribed scales. Its full word retains
the complete valuation history and the block divisions.

## 2. Single-block bounds

For a block of depth \(s\), valuation sum \(A\), parent \(R\), and outer
source \(x\), write

\[
 R=\omega x+\beta,\qquad \omega=3^s2^{-A}.
\]

Each valuation is at least 1, so its affine offset satisfies

\[
 0\le\beta\le\sum_{i=1}^{s}3^{i-1}2^{-i}
 =(3/2)^s-1<2^b.
\tag{1}
\]

Here \(s\le8b/5\) and \((3/2)^8<2^5\). The ceiling losses in \(H_b\)
give

\[
 2^{-K_j-1}(3/4)^b\le\omega\le2(3/4)^b.
\]

If \(R\ge16^b\), then \(R-\beta\ge R/2\); consequently

\[
 \tfrac14(4/3)^bR\le x\le2^{K_j+1}(4/3)^bR.
\tag{2}
\]

Set \(e=\lfloor b/100\rfloor\). Since \((4/3)^5>4\), the lower
factor in (2) is at least \(16^e\) for \(b\ge200\). Therefore
\(x\ge16^eR\ge16^{b+e}\), and

\[
 \omega=(R-\beta)/x\le R/x\le16^{-e}.
\tag{3}
\]

These estimates keep every block endpoint in its required height range.
For an intermediate positive odd state \(z\) with at most \(h_b\) arrows
remaining to \(R\), the elementary bound \(S(z)\le2z\) gives
\(z\ge16^b2^{-h_b}>1\). Thus these particular paths do not encounter
the absorber.

## 3. Complete offsets and multiplicity before nonreturn

Write the affine relation of a complete history as

\[
 M=W x+\beta_h,\qquad W=3^D2^{-A},
\]

where \(D\) and \(A\) are its total depth and valuation sum. Products of
(3) telescope:

\[
 W\le16^{b_0-b_n}.
\tag{4}
\]

The contribution of block \(j\) to the complete offset is its offset
multiplied by the weights of the preceding blocks. Therefore (1), (3),
and \(b_j\ge b_0+j\) give the root-independent bound

\[
 0\le\beta_h
 <\sum_{j<n}16^{b_0-b_j}2^{b_j}
 \le2^{b_0}\sum_{j\ge0}2^{-3j}
 =\tfrac87 2^{b_0}<2^{b_0+1}.
\tag{5}
\]

The numerical value of \(M\) moves the interval of possible sources but
does not change its width.

Put

\[
 B_* =\sum_{j<n}b_j,\quad
 W_* =\sum_{j<n}m_{b_j},\quad
 K_* =\sum_{j<n}K_j.
\]

There are at most

\[
 P_n=(2W_*+1)(K_*+4n+1)
\tag{6}
\]

pairs \((D,A)\). Indeed \(|D-B_*|\le W_*\). Comparing each signed
ceiling in \(H_b\) to \((s-b)\log_2 3\), and then comparing the summed
linear term to \(B(D)-B(B_*)\), proves the safe bounds

\[
 2B_*+B(D)-B(B_*)-2n
 \le A\le
 2B_*+B(D)-B(B_*)+K_*+2n.
\]

The case \(n=0\) has only the empty history and also satisfies (6).

**Multiplicity point.** Fix \(D,A\). If two histories have the same
source integer \(x\), the deterministic length-\(D\) Syracuse orbit of
\(x\) fixes all its valuations. Its full word fixes every block division
by the prescribed first-crossing rule. Hence the histories coincide.
This uses uniqueness at fixed depth, not uniqueness of a hitting time.
Histories with different depths are retained in different groups, so a
periodic root would not invalidate this argument.

## 4. Named arithmetic lemma: seed-uniform residue histogram

Let \(H_{n,q}(y)\) be the sum of the weights of the generation-\(n\)
histories whose actual outer source is \(y\bmod3^q\). For every integer
\(q\) with \(0\le q\le2b_n\), every residue \(y\), and every positive
odd \(M\ge16^{b_0}\),

\[
 3^qH_{n,q}(y)
 \le P_n\left(2^{b_0+1}+16^{b_0}(9/16)^{b_n}\right).
\tag{7}
\]

**Proof.** Inside one \((D,A)\) group, \(W\) is constant. By (5), all
sources lie in an interval of length at most \(2^{b_0+1}/W\). Their
spacing in one residue class is at least \(3^q\). By the multiplicity
point there are at most \(2^{b_0+1}/(W3^q)+1\) histories in that group
and residue class. Their total weight, multiplied by \(3^q\), is at
most \(2^{b_0+1}+3^qW\). Apply (4), use \(3^q\le9^{b_n}\), and sum
over the at most \(P_n\) groups. This proves (7).

The second summand in (7) is the residue-count endpoint error. It has not
been dropped. Its control is exactly where the restriction \(q\le2b_n\)
is needed. The lemma allows \(q\) to grow with \(n\), inside this range.

Set

\[
 G=2013/2000,
 \quad C_{b_0}=6(4b_0^{3/5}+1)(2^{b_0+1}+16^{b_0}).
\]

Then every real function \(f\) on \(\mathbb Z/3^q\mathbb Z\) obeys

\[
 \left|\sum_y H_{n,q}(y)f(y)\right|
 \le C_{b_0}(n+1)^3G^n\langle|f|\rangle_q.
\tag{8}
\]

To check the displayed constant, use
\(b_j\le b_0(101/100)^j\),
\(W_*\le2n b_0^{3/5}G^n\), and \(K_*\le n(n+1)\).
The first factor in (6) is at most
\((4b_0^{3/5}+1)(n+1)G^n\); the second is at most
\(6(n+1)^2\). Also \((9/16)^{b_n}\le1\).
Finally use the triangle inequality and the uniform residue average.

## 5. Exactly how the mixing input is used

Let \(\rho_q\) be the manuscript's normalized finite Syracuse reference
law, with mean \(2/3\). Import the explicit hypothesis

\[
 \langle|\rho_q-\rho_m\circ\pi_{q,m}|\rangle_q
 \le(2/3)C_A m^{-A},\qquad 1\le m\le q.
\tag{9}
\]

For each fixed exponent \(A>0\), Tao's Proposition 1.14 supplies some
finite \(C_A\). Marginal compatibility identifies the coarse law with
\(\rho_m\). This assertion concerns a formal random affine offset, not
independent valuations on an actual integer orbit.

For a word \(w=(a_1,\ldots,a_d)\) in inverse order, its finite affine map is

\[
 F_w(z)=3^d2^{-A(w)}z+
 \sum_{i=1}^{d}3^{i-1}2^{-(a_1+\cdots+a_i)}
 \pmod {3^{t+d}}.
\]

It maps \(\mathbb Z/3^t\mathbb Z\) injectively into
\(\mathbb Z/3^{t+d}\mathbb Z\): changing the lift adds a multiple of
\(3^{t+d}\), and equality of two images forces equality modulo
\(3^t\). Define \(T_wg(y)\) as \(3^d2^{-A(w)}g(z)\) on its image
and zero off its image. Summing over that image and dividing by
\(3^{t+d}\) shows that its average absolute mass is exactly
\(2^{-A(w)}\) times that of its argument.

At a physical odd parent \(R\ge16^b\), a nonempty residue fiber also
has the intended arithmetic meaning. The congruence modulo \(3^d\)
successively makes \((2^{a_i}R_{i-1}-1)/3\) integral; division by 3
reduces the remaining congruence by one power. Each result is odd.
Every partial affine offset is smaller than \(2^b\) by (1), so these
integers are positive. Therefore their valuations are exactly the given
\(a_i\), and the final actual source has the residue in the fiber.
For \(k\ge1\), the factor \(\rho_k\) enforces a unit source; earlier
endpoints are units because each is the image of an odd Syracuse arrow.
This justifies the passage between residue transfers and actual paths.

If \(V\) is a finite
prefix-disjoint family of words of depth at most \(h\), put
\(p(V)=\sum_{w\in V}2^{-A(w)}\le1\), \(Q=h+k\). For
\(1\le\ell\le Q\),

\[
 \left\langle\left|\sum_{w\in V}T_{w,Q}\rho_k
            -\rho_\ell\circ\pi_{Q,\ell}\right|\right\rangle_Q
 \le\tfrac23\left(C_Ak^{-A}+C_A\ell^{-A}+1-p(V)\right).
\tag{10}
\]

There are three terms: replace each lifted \(\rho_k\) by
\(\rho_{Q-d}\) using (9); the exact independent reference law then
partitions into the disjoint prefix events and their omitted complement;
finally compare \(\rho_Q\) with \(\rho_\ell\) using (9). The first
replacement is multiplied by the prefix probabilities, whose sum is at
most 1. The omitted complement has average exactly
\((2/3)(1-p(V))\). Actual integer histories are used only when this
finite-residue expression is evaluated at physical endpoints.

For the central step, take

\[
 k_n=\lfloor b_n/4\rfloor,\qquad
 Q=h_{b_n}+k_{n+1},\quad k=k_{n+1},\quad\ell=k_n.
\]

The moving modulus is admissible because

\[
 Q\le(8/5+101/400)b_n<2b_n.
\tag{11}
\]

Pair (10) with the **same** nonnegative physical histogram
\(H_{n,Q}\), and use (8). No averaging over the fixed root is introduced
at this step, and no selection indicator from earlier blocks is removed.

## 6. Explicit summable variation majorant

For completeness the reference geometric variables have a direct
concentration bound. If \(E\) has \(\Pr(E=a)=2^{-a}\), then
\(\log\mathbb E e^{\theta(E-2)}=-\theta-\log(2-e^\theta)\).
For \(|\theta|\le1/4\), its second derivative is at most 6, hence its
value is at most \(4\theta^2\). Chernoff's inequality, with
\(|\theta|=\min(v/(8t),1/4)\), gives a bound at least as strong as

\[
 \Pr\{|E_1+\cdots+E_t-2t|>v\}
 \le2\exp\{-\min(v^2/(32t),v/8)\}.
\]

An early crossing or a late miss outside the central depth window forces
a deviation greater than \(m_b/3\). One may use
\(\log_2 3<8/5\), \(m_b\ge15\), and the signed ceiling error below 1
to check this, including the lower-endpoint miss. A union over at most
\(2b+2\) prefix depths gives the central-window loss below. Conditional
on a first crossing, geometric memorylessness gives an overshoot loss
of \(2^{-(K+1)}\). Thus, for the central prefix code at stage \(n\),

\[
 1-p_n\le(4b_n+4)e^{-m_{b_n}^2/(576b_n)}
                  +2^{-(K_n+1)}
 \le C_s b_n^{-6}+2^{-n/100},
\quad C_s=8\cdot35!\cdot576^{35}.
\tag{12}
\]

The second inequality uses the 35th exponential-series term and
\(m_b\ge b^{3/5}\). The central code is nonempty: the word
\((1,2,\ldots,2,3)\) of length \(b_n\) crosses at depth \(b_n\)
with zero overshoot. It is a reference word; integer admissibility is
handled by the transfer, not assumed for every root.

Let \(Z_n(M)\) be the original weighted sum of \(\rho_{k_n}\) over
the central generation-\(n\) histories. Since
\(k_n,k_{n+1}\ge b_n/8\) and
\(b_n\ge b_0(201/200)^n\), (8), (10), and (12) prove

\[
 |Z_{n+1}(M)-Z_n(M)|\le E_n,
\]

\[
 E_n=\tfrac23 C_{b_0}(n+1)^3
 \left[\frac{2C_6 8^6+C_s}{b_0^6}q_1^n+q_2^n\right],
 \quad q_1=G(200/201)^6<1,
 \quad q_2=G2^{-1/100}<1.
\tag{13}
\]

This is summable and independent of \(M\). Consequently \(Z_n(M)\)
has a nonnegative limit and its tail error is bounded by
\(\sum_{j\ge N}E_j\), uniformly over all the permitted integer roots.
This is a conditional analytic consequence of (9), with its arithmetic
multiplicity and moving-modulus parts established above.

The strict numerical comparisons can be checked entirely with integers:

- \(2013^5 100^3>2000^5 101^3\);
- \(2013\,200^6<2000\,201^6\);
- \(2013^{100}<2\,2000^{100}\);
- \(3^8<2^{13}\), \(4^5>4\,3^5\).

All five comparisons were evaluated exactly during this audit. They
verify constants, not the universal argument by finite experimentation.

## 7. Enlarged caps and remaining dependencies

For the later explicit construction, \(K_j=16+\lfloor j/100\rfloor\).
The histogram lemma (7) is unchanged; only its group count changes.
Using \(K_*\le17n(n+1)\) gives the valid replacement

\[
 C'_{b_0}=22(4b_0^{3/5}+1)(2^{b_0+1}+16^{b_0})
\]

in (8), because \(17n(n+1)+4n+1\le22(n+1)^2\).
The overshoot term in (12) acquires the extra factor \(2^{-16}\).
Thus root-uniform summability survives this cap change. This verifies the
structure of the Appendix A reuse; it does not check every later large
numerical constant in the explicit density recipe.

The following remain distinct from this lemma:

1. Terminal shifts depend on the actual physical endpoint and external
   scale; their grouping and retained indicators need their own estimate.
2. All sufficiently large external cutoffs need the overlap argument;
   generation-by-generation control alone is insufficient.
3. Counting distinct integer sources across different depths needs the
   separate nonreturn selection. The histogram proof does not grant that
   stronger injectivity.
4. The current note has not rebuilt the Lean development or checked all
   theorem-to-source dependencies. Reported external formal evidence and
   an independent replay must be distinguished.
5. No version of the actual-nonabsorbing-set upper estimate C.2a has been
   supplied by this argument. A positive lower density of a predecessor
   set is compatible with a nonprincipal cycle.

**Audit conclusion for this ingredient:** the paper's fixed-root
multiplicity and growing-modulus bounds survive independent derivation.
No missing nonreturn assumption or discarded residue endpoint term was
found in equations (3.9)–(3.10) or their central-variation use.
