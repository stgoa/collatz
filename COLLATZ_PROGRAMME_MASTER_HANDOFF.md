# Collatz programme: master research handoff and proof-reconstruction map

**Checkpoint: exact-source ternary packets and finite signed-current certificates.**

This single file preserves the programme's reusable mechanisms, the dependencies needed to reconstruct their proofs, the decisive counterexamples, and the unresolved step. It is intentionally organized by mathematical dependence rather than by chat turn or sprint number. Several historical reports reused sprint numbers or described different artifact versions.

**Bottom line:** Collatz, logarithmic mean stopping work on the required source-power window, and uniform cheap-current construction are all **unproved**. The most useful current result is a source-exact reduction to balanced ternary packets, followed by finite certificates that cancel unknown common futures even when arrival times differ. The latest finite certificates were rerun while preparing this handoff. Nothing here upgrades an inherited candidate theorem to independent peer review or formal verification.

---

## 0. Read this first: the shortest useful description

### The objective

Prove that every positive integer reaches 1 under Collatz. A separate publication project gives free positive inverse-Syracuse coding and a relational PCP reduction; it is **not** undecidability of ordinary Collatz halting.

### The actual logical route now being pursued

1. Let `h_T(x)=min(T,tau(x))`, where `tau` is first odd-only hitting time of 1, possibly infinite. Prove mean truncated work `O(log X)` on odd seeds in `[X,2X)` for a horizon about `X^(1/5) log X`.
2. This leaves at most `O(X^(4/5))` permanent exceptions. A published inverse-basin lower bound of Krasikov--Lagarias says one exception would create roughly `X^0.84` exceptions, up to a logarithmic loss. The exponent gap would force emptiness.
3. An exact three-scale recurrence expresses prefix stopping work in terms of smaller/larger prefixes plus a signed ternary-residue discrepancy `E_T(N)`.
4. That discrepancy is exactly signed stopping work: `3 E_T(N)=H_T(nu_N)` for one explicit signed source measure `nu_N`.
5. At depth `m=floor(2 ceil(log2 N)/9)`, group actual source-cylinder lifts in threes. This gives
   
   `P^m nu_N = Pi_hat_N + eta_N`,
   
   where `Pi_hat_N` is a completely specified family of balanced ternary-spaced triples and `||eta_N||_1 <= 16 N^(7/9)`.
6. Paying the remainder for the entire horizon costs `O(log N * N^(44/45))=o(N)`. The only substantial local-window term left is `H_L(Pi_hat_N)`.
7. Bound that term by finite signed arrow weights `J`: if `Pi_hat_N=(I-P)J`, unknown common futures cancel. Finite exit profiles give all-horizon bounds without following exits to 1.
8. **Missing:** an arithmetic construction or uniform bound on the positive exit-profile cost, e.g. `C_+(J_N)=O(N)`, or a suitable incomplete-current replacement. Current tables found by following sample trajectories do not prove this. Also retain the source/time-domain bookkeeping required by the final recurrence comparison; a local-window estimate is not automatically a rectangular-domain estimate.

### What to preserve as the "secret sauce"

- Exact cylinder modulus **`2^(A+1)`**, not `2^A`.
- Three consecutive source lifts cycle the initial residue modulo 3 and therefore give a **zero-sum triple of actual endpoints**.
- Signed source weights encode a real stopping-work error; they are not probabilities.
- Cancellation can occur at the same state at **different elapsed times**. The unknown common tail can disappear algebraically.
- A finite certificate `mu=(I-P)J` can be checked by **one-step arithmetic**, independently of the search that discovered it.
- Bound the **one-sided signed cost**, not necessarily all absolute residence time. Negative residuals can be free for an upper bound.
- Preserve terminal survival and source multiplicities. First-descent survival is not backward invariant; deleting endpoint multiplicities destroys the argument.
- Keep the scalar source-scale recurrence's expanding branch and its boundary term. An induction that uses only smaller source sizes is invalid.
- The auxiliary analytic bulk is not an actual integer orbit law. Keep total valuation and the extra ternary digit in any mixing argument.
- A proposed theorem must remain useful after histories identify individual seeds. More within-cylinder averaging alone no longer attacks the frontier.

### Read order

For immediate continuation read Sections 1--9, then the executable skeleton in Section 10. Sections 11--15 preserve the analytic branch and the older discoveries and failures. Section 16 lists the actual available sources, archive checksums, and external dependencies.

---

## 1. Reliability, provenance, and what was checked for this handoff

Use the following labels conceptually:

- **CORE:** a complete elementary written proof is present in the supplied current notes and reconstructed here. Still not human-reviewed or Lean-verified.
- **FINITE:** an exact finite certificate, not a uniform source-size theorem.
- **ANALYTIC CANDIDATE:** an inherited extension of a published theorem that needs its own external audit.
- **HISTORICAL:** reported earlier in the conversation or old handoff; its original complete code/data were not available for a new audit here.
- **OPEN:** the statement is a research target, not a lemma.
- **REFUTED / SCOPED:** preserve the counterexample or hypothesis restriction; do not resurrect the overstatement.

For this handoff, the supplied `collatz_packet_currents_bundle.zip` was extracted into a separate audit directory. All **31 original manifest hashes** matched. `verify_stored_currents.py` was rerun successfully on the two complete tables, for `N=4096` and `N=262144`. It reconstructed the exact source packets, checked `(I-P)J=Pi_hat`, checked the finite exit profiles, recomputed the anchor remainder, and matched the stored independent C++ results. It did **not** run a new unresolved hitting-time search or recompile the C++ checker.

Other mounted post-handoff research notes were read to recover the critical dependencies. Their full computational histories were not all rerun for this compression. The earlier sprint claims below are explicitly separate from the current certificate chain.

Archive SHA-256 for the latest complete current package:

`025c8fafe25940951fe408b32b1ec806259725a6b4f8855d9f2b022911fe5447`

The executable kernel in Section 10 was also extracted from this Markdown and run successfully: it rebuilt finite packet decompositions at (N,d)=(32,1),(512,2),(4096,2) and verified both common-tail regression witnesses. This is a smoke test of the reconstruction recipe, not formal proof verification.

No claim of novelty follows from a derivation or a successful finite check. The user wants real leverage toward Collatz, not more objects renamed as breakthroughs.

---

## 2. Canonical notation and indispensable elementary algebra

### 2.1 Three clocks

Use the positive odd-only map

\[
S(x)=\frac{3x+1}{2^{a(x)}},\qquad a(x)=v_2(3x+1),\qquad S(1)=1.
\]

The shortcut map is `T(y)=y/2` on even inputs and `(3y+1)/2` on odd inputs. One Syracuse step with valuation `a` is exactly `a` shortcut steps. The unaccelerated map has odd step `3y+1`; do not conflate its clock with either of these.

Let `tau(x)` be the first Syracuse hitting time of 1, `tau(1)=0`, and allow infinity. Set

\[
h_L(x)=\min\{L,\tau(x)\},\qquad h_L(1)=0.
\]

For finite `L`, this is always computable by at most `L` actual odd steps. No global convergence assumption is involved.

### 2.2 Affine word formula

For a positive valuation word `w=(a_1,...,a_d)`, define

\[
A_j=\sum_{i=1}^j a_i,\quad A_0=0,\quad A=A_d,
\]
\[
C_w=\sum_{j=0}^{d-1}3^{d-1-j}2^{A_j},\qquad
G_w(x)=\frac{3^d x+C_w}{2^A}.
\]

The recursion is `C <- 3*C + 2^A`, then `A <- A+a`, starting at zero.

### 2.3 Exact cylinders, including the extra bit

There is one exact odd source residue modulo `M_w=2^(A+1)`:

\[
q_w=[(2^A-C_w)(3^d)^{-1}]_{2^{A+1}},\qquad 0<q_w<2^{A+1},
\]
\[
e_w=(3^d q_w+C_w)/2^A.
\]

Every positive source and endpoint are

\[
x_t=q_w+2^{A+1}t,\qquad y_t=e_w+2\cdot3^d t,\quad t\ge0. \tag{Cyl}
\]

**Proof reconstruction:** the terminal congruence is `3^d x+C_w == 2^A mod 2^(A+1)`. Divisibility successively makes all intermediate quotients integers; reading backwards from the odd terminal quotient forces every predecessor odd, hence every valuation exact. The forward affine numerators are positive, so the positive representatives remain positive. Equivalently induct using inverse branches `R_a(y)=(2^a y-1)/3` on odd 2-adic units.

The forgotten factor 2 was a genuine early failure mode. All current formulas use `2^(A+1)`.

### 2.4 Descent barriers and drift

Write `alpha=log2(3)`, `D_j=A_j-j alpha`, `r_w=3^d/2^A`, `F_w=C_w/2^A`.

If `r_w<1`, define

\[
\beta_w=\frac{F_w}{1-r_w}=\frac{C_w}{2^A-3^d}.
\]

Then

\[
G_w(x)\ge x\iff x\le\beta_w.
\]

For an actual orbit,

\[
x_n=2^{-D_n}\left(x_0+\frac13\sum_{j=0}^{n-1}2^{D_j}\right),
\]
\[
x_n=x_0\frac{3^n}{2^{A_n}}
\prod_{j=0}^{n-1}\left(1+\frac1{3x_j}\right). \tag{Product}
\]

A contractive coefficient is not actual descent. A block can descend early and rebound later. Keep first descent, first coefficient contraction, terminal hitting of 1, and rebound blocks distinct.

---

## 3. Why a mean-work theorem would prove Collatz

### 3.1 Terminal survivors, not first-descent survivors

For `X=2^b`, let

\[
I_b=\{x\text{ odd}:X\le x<2X\},\qquad |I_b|=X/2,
\]
\[
A_{b,t}=\{x\in I_b:\tau(x)>t\},\qquad M_{b,t}=|A_{b,t}|.
\]

These are sets of **initial seeds**. If several seeds have the same endpoint, count them all. Absorb only at 1.

For `f(y)=min(a(y),4)`, put `F_{b,t}=sum_{x in A_{b,t}} f(S^t x)` and

\[
V_{b,t}=\sum_{x\in A_{b,t}}\log_2 S^t(x)\ge0.
\]

The identity `log2(1)=0` gives exact removal bookkeeping:

\[
V_{b,t+1}-V_{b,t}
=\sum_{x\in A_{b,t}}\log_2\frac{S^{t+1}x}{S^t x}
\le\log_2(10/3)M_{b,t}-F_{b,t}.
\]

All active endpoints are odd and at least 3. The integer comparison `2^139 * 3^80 > 10^80` implies

\[
\log_2(10/3)<139/80=7/4-1/80.
\]

Truncating the valuation weakens an **upper** bound on growth; arbitrarily large divisions only help it. No uncontrolled moment assumption is needed.

### 3.2 The actual unproved target is mean truncated work

Take

\[
T_b=\left\lceil(b+1)X^{1/5}\right\rceil,
\qquad
W_b(T)=\sum_{t<T}M_{b,t}=\sum_{x\in I_b}h_T(x).
\]

The target is

\[
\boxed{W_b(T_b)=O((b+1)X).} \tag{MW, OPEN}
\]

This is `O(log X)` average truncated hitting time, not a count of just first descents.

Earlier it was formulated as

\[
L_b\ge\frac74W_b-CX^{2/5}\sqrt{T_bW_b}-D(b+1)X,
\quad L_b=\sum_{t<T_b}F_{b,t}. \tag{FH, OPEN}
\]

**FH and MW are equivalent at the level of existence of absolute constants.** FH implies MW by the potential inequality and `a sqrt(W) <= W/160+40a^2`. Conversely, if `W_b<=K(b+1)X`, then `L_b>=0` gives FH with `C=0,D=7K/4`. The flexible startup allowance did not make the original objective easier.

### 3.3 Inverse-basin amplification [external input]

Krasikov--Lagarias (2003), arXiv `math/0205002`, prove a fixed-root inverse-basin lower bound of exponent `0.84`: for each positive `r` not divisible by 3, at least `Y^0.84` integers up to `Y` eventually reach `r`, for sufficiently large `Y` depending on `r`. This is a published computer-assisted theorem, not reconstructed by the programme's scans. Recheck its exact formulation when formally importing it.

If a counterexample exists, choose an odd counterexample not divisible by 3 (take a Syracuse image if necessary). Every predecessor is exceptional. Stripping powers of two loses at most `1+floor(log2 Y)` preimages per odd part. Thus the count `B(Y)` of odd exceptions obeys

\[
B(Y)\ge\frac{Y^{0.84}}{1+\lfloor\log_2Y\rfloor}
\]

for all sufficiently large `Y`.

But MW implies

\[
M_{b,T_b}\le W_b(T_b)/T_b=O(X^{4/5}),
\]

hence `B(Y)=O(Y^0.8)`, a contradiction. This covers hypothetical nontrivial cycles as well as divergent orbits.

**Secret-sauce distinction:** a candidate source can be isolated in its own exact cylinder, but a real counterexample cannot be globally isolated. An aggregate power saving would suffice; perfect individual control is not logically necessary.

---

## 4. Exact stopping-work transport: the starting point of the current route

Define prefix sums

\[
Q_T(N)=\sum_{\substack{1\le x\le N\\x\text{ odd}}}h_T(x),
\quad
R_{r,T}(N)=\sum_{\substack{1\le x\le N\\x\equiv r\ (6)}}h_T(x),\ r=1,5.
\]

For dyadic `X`, `W_b(T)=Q_T(2X)-Q_T(X)`.

Put

\[
n_0=\left\lfloor\frac{N-1}{4}\right\rfloor,\quad
n_1=\left\lfloor\frac{3N+1}{2}\right\rfloor,\quad
n_2=\left\lfloor\frac{3N+1}{4}\right\rfloor,
\]
\[
c_N=\left\lfloor\frac{N+1}{4}\right\rfloor
+\left\lfloor\frac{N-1}{8}\right\rfloor+\mathbf1_{N\ge5}.
\]

### 4.1 Exact recurrence [CORE]

For `T>=1,N>=1`,

\[
\boxed{Q_T(N)=Q_T(n_0)+c_N+R_{5,T-1}(n_1)+R_{1,T-1}(n_2).} \tag{TR}
\]

**Rebuild proof by the first valuation:**

- `a=1`: sources `4j+3` map to `6j+5`; add one step per source.
- `a=2`: sources `8j+1>1` map to `6j+1>=7`; add one step per source.
- `a>=3`: sources `4z+1`, `z` odd, satisfy `S(4z+1)=S(z)`, hence the same truncated work for `z>1`. The exception `z=1` is `h_T(5)=1 != h_T(1)=0`, producing the indicator in `c_N`.

Define the exact discrepancy

\[
\mathcal E_t(N)=R_{5,t}(n_1)-\tfrac13Q_t(n_1)
+R_{1,t}(n_2)-\tfrac13Q_t(n_2).
\]

Then

\[
Q_T(N)=Q_T(n_0)+\tfrac13Q_{T-1}(n_1)+\tfrac13Q_{T-1}(n_2)
+c_N+\mathcal E_{T-1}(N). \tag{TR-E}
\]

The factors `1/3` are a reference decomposition, not a uniformity theorem. The error can be positive: `E_40(32)=15`, since the four sums are `98,249,13,39`, respectively. Sources 41 and 47 contribute disproportionately long work in one residue class.

### 4.2 Expanding-source boundary [CORE, conditional comparison]

The `n_1` branch is approximately `3N/2`; an induction assuming all children are smaller is false.

Let

\[
(\mathcal Lg)(N)=g(n_0)+\tfrac13g(n_1)+\tfrac13g(n_2),
\quad\Phi(N)=N\log_2N,\quad\Psi(N)=N^2+4N\log_2N.
\]

For `N>=32`,

\[
\mathcal L N\le N,\quad
\mathcal L\Phi<\Phi-N/6,\quad
\mathcal L\Psi<\Psi-(N-1)/6. \tag{Scale}
\]

To check the logarithmic inequality put `u_i=n_i/N`, use `u_0 in [1/5,1/4]`, `u_1<=49/32`, `u_2<=49/64`, and `49^8<2^45`. The normalized log contribution is below `-1357/7680<-1/6`.

For the quadratic part,

\[
\mathcal L(N^2)-N^2=
\begin{cases}
-N/2+1,&N=0\pmod4,\\
N/2+1/6,&N=1\pmod4,\\
-N/2+1/3,&N=2\pmod4,\\
2/3,&N=3\pmod4.
\end{cases}
\]

The log correction absorbs all positive rounding errors. The ideal power multiplier

\[
4^{-p}+\tfrac13(3/2)^p+\tfrac13(3/4)^p
\]

is strictly convex and equals 1 at `p=1,2`; it exceeds 1 for `p>2`. Thus the corrected quadratic reaches the endpoint of this scalar homogeneous-power method, not a universal obstruction to better comparisons.

If `E_t(n)<=Kn` for all `32<=n<=Y,0<=t<T_*`, then

\[
\boxed{Q_T(N)\le6N+6(K+1)N\log_2N+T\Psi(N)/Y}
\]

for `N<=Y,T<=T_*`. Prove by induction first on `T`, then `N`. For `N>Y`, `Q_T(N)<=TN<=T Psi(N)/Y`; for `N<32`, explicitly verify `Q_T(N)<=6N`; then apply TR-E and Scale.

At `N=2X`, `Y=ceil((2X)^(6/5))`, `T=T_b`, the boundary term is `O(X log X)`. Hence the stated **rectangular-domain** error hypothesis would imply MW.

**Uniformity guard:** an estimate only for `E_t(n)` with `t<=n^(1/5)log n` does not automatically give the rectangle `n<=Y,t<T_b`. Late times at smaller `n` still require control. The latest local packet/current reduction does not silently discharge this final domain bookkeeping. A weaker suitably accumulated recursion-tree error could suffice, but naming that accumulated error is not a bound on it.

---

## 5. Signed transport: the actual discrepancy as a finite measure

Work on odd states greater than 1. For a finite signed integer measure,

\[
(P\mu)(y)=\sum_{x>1:S(x)=y}\mu(x),\quad y>1;
\qquad\|\mu\|_1=\sum_y|\mu(y)|.
\]

Mass sent to 1 is killed. `P` is linear and nonexpansive. Opposite signs cancel only when they reach the same actual endpoint at the same elapsed step.

For integer `N>=8`, define

\[
\nu_N(x)=\mathbf1_{x\le n_1}(3\mathbf1_{x\equiv5\ (6)}-1)
+\mathbf1_{x\le n_2}(3\mathbf1_{x\equiv1\ (6)}-1),\quad x>1\text{ odd}.
\]

Its combined source weights have absolute value at most 2 and signed total of absolute value at most 8. For dyadic `N=2^b,b>=3`,

\[
\|\nu_N\|_1=N-1,\qquad\langle1,\nu_N\rangle=-1.
\]

For any finite signed `mu`, define

\[
H_L(\mu)=\langle\mu,h_L\rangle
=\sum_{j=0}^{L-1}\langle1,P^j\mu\rangle.
\]

Then the exact bridge is

\[
\boxed{3\mathcal E_T(N)=H_T(\nu_N).} \tag{Error}
\]

No convergence theorem is used. Signed weights are coefficients in a stopping-work functional, not a probability law or a percentage of convergent sources.

The norm loss under `P` equals mass absorbed at 1 plus twice the mass of opposite-sign contributions paired at common endpoints. But the norm need not decrease strictly, and norm residence is stronger than the signed quantity actually needed.

---

## 6. The current best reduction: exact-source ternary packets

This replaces the earlier homogeneous-cell packet construction. **Do not identify its individual packets with the older un-hatted family.**

Let `b=ceil(log2 N)` and `1<=d<=b/2`. Enumerate all positive words `w` of length `d` and total `A<=b`. There are exactly `binom(b,d)` of them.

For each word use Cyl. To exclude source 1 and every absorbed endpoint, take

\[
t_0=0\text{ if }q_w>1,e_w>1;\qquad t_0=1\text{ otherwise}.
\]

For source component `i=1,2`, retain lift indices

\[
t_0\le t\le\left\lfloor\frac{n_i-q_w}{2^{A+1}}\right\rfloor.
\]

Earlier absorption cannot be missed: if an intermediate state were 1, the final state would remain 1 under `S`.

### 6.1 Group consecutive lifts in threes

The first source component assigns weight `3*1_(x mod3=2)-1`; the second uses `3*1_(x mod3=1)-1`. Since `2^(A+1)` is a unit modulo 3, each consecutive lift triple visits all three source residues. Its endpoint packet is

\[
c_0\delta_y+c_1\delta_{y+2\cdot3^d}+c_2\delta_{y+4\cdot3^d},
\qquad (c_0,c_1,c_2)\text{ a permutation of }(2,-1,-1).
\]

Take complete triples beginning at `t_0`, separately within both source components. Add coincident weights across all words/components. Call the resulting measure `Pi_hat_(d,N)`.

There are at most two leftover lifts per component, of absolute weight at most 3. Thus the ungrouped edge cost is at most `6 binom(b,d)`.

Among the `2^b` odd classes modulo `2^(b+1)`, the number with first `d` valuation sum exceeding `b` is exactly

\[
\sum_{j=0}^{d-1}\binom bj.
\]

Rebuild by complement:

\[
\sum_{A=d}^{b}\binom{A-1}{d-1}2^{b-A}
=\sum_{j=d}^{b}\binom bj.
\]

The support of `nu_N` is below `2^(b+1)` and its weights are bounded by 2. This gives the complete over-budget cost.

### 6.2 Uniform remainder theorem [CORE]

\[
\boxed{P^d\nu_N=\widehat\Pi_{d,N}+\widehat\eta_{d,N},\quad
\|\widehat\eta_{d,N}\|_1\le
D^*_{b,d}:=6\binom bd+2\sum_{j=0}^{d-1}\binom bj.} \tag{Packets}
\]

No affine boundary has been approximated. The only errors are explicit leftover source lifts and over-budget source classes.

For `N>=512`, choose `m=floor(2b/9)`. Since

\[
H_2(2/9)<7/9,
\]

certified by `9^9<2^9*7^7`, the binomial estimate gives

\[
\boxed{\|\widehat\eta_{m,N}\|_1\le16N^{7/9}.} \tag{Remainder}
\]

Every packet has signed total zero. Apply the same bound at all early depths, and use nonexpansivity after the anchor:

\[
\boxed{
\left|3\mathcal E_T(N)-H_{(T-m)_+}(\widehat\Pi_{m,N})\right|
\le T D^*_{b,m}.
} \tag{Reduce}
\]

For `T<=ceil((b+1)N^(1/5))`, the right side is at most

\[
16(b+2)N^{44/45}=o(N).
\]

**Interpretation:** the entire worst-case lifetime of the remainder is now affordable at the desired local source-power horizon. The future signed packet work, not the mere existence of a boundary correction, is the unresolved term.

The packet sum can have large norm; zero signed mass is not positive-source convergence. Exact packet genealogy matters, not arbitrary triples with the same spacing.

---

## 7. The latest key mechanism: cancel an unknown shared future

### 7.1 Common-tail lag formula [CORE]

Suppose signed sources `(x_i,c_i)`, with `sum c_i=0`, reach one state `z` after verified lengths `d_i`, without hitting 1 earlier. Define

\[
\Phi(u)=\sum_i c_i\min(u,d_i),\quad u\ge0.
\]

Then, for every horizon `L`,

\[
\boxed{\sum_i c_i h_L(x_i)=\Phi((L-\tau(z))_+).} \tag{Lag}
\]

For `tau(z)=infinity`, interpret the right side as `Phi(0)=0`.

**Proof:** `tau(x_i)=d_i+tau(z)`. If `L<=tau(z)` all values are `L` and the signed sum vanishes. Otherwise subtract the common `tau(z)` and use `sum c_i=0`. The same cancellation holds if the common tail never reaches 1.

The extrema of `Phi` occur at `0` and the finite arrival lengths `d_i`. So finite paths to a meeting point certify all future horizons without continuing past that point.

**Key witness:**

\[
-\delta_{6929}-\delta_{6947}+2\delta_{6965}
\]

reaches `z=23` at times `(49,32,3)`. Therefore

\[
\Phi(u)=-\min(u,49)-\min(u,32)+2\min(u,3),
\quad -75\le H_L\le0\text{ for all }L.
\]

This packet is genuinely in the exact-source family at `N=4096,d=2`, word `(1,1)`, outer component, lifts `384,385,386`.

**Opposite-sign guard:** `delta_55+delta_73-2 delta_91` reaches 91 at `(8,9,0)`, giving `0<=H_L<=17`. It belongs to an older grouping; do not claim it is one raw triple in the new grouping. Balance alone does not fix the sign.

**Why absolute lifetime can be the wrong objective:** if `S(u)=z>1`, then `0<=h_L(u)-h_L(z)<=1`. If the tail of z were divergent, the synchronous norm of `P^j(delta_u-delta_z)` could remain 2 forever, yet its signed work would be zero.

### 7.2 Finite currents [CORE]

A current `J` is a finite signed table on odd states greater than 1, assigning `J(y)` to the arrow `y -> S(y)`. Its divergence is

\[
\partial J=(I-P)J.
\]

If

\[
\mu=(I-P)J,
\]

then telescoping gives

\[
\boxed{H_L(\mu)=\langle1,J-P^LJ\rangle
=\sum_yJ(y)\mathbf1_{\tau(y)\le L}.} \tag{Current}
\]

Consequently

\[
-\|J^-\|_1\le H_L(\mu)\le\|J^+\|_1
\quad\text{for every }L.
\]

A verifier needs one step from each stored row: add `J(y)` at `y`, subtract it at `S(y)>1`, and compare with `mu`. It does not need a global stopping-time oracle.

For an incomplete current,

\[
\mu=(I-P)J+\zeta
\quad\Longrightarrow\quad
H_L(\mu)\le\|J^+\|_1+L\|\zeta^+\|_1. \tag{One-sided}
\]

A negative residual costs nothing for the upper bound. This is why demanding a small absolute residual can waste information.

### 7.3 Finite exit profiles improve the cost [CORE]

Suppose the directed graph within `supp J` is acyclic. Verify this finite property; do not assume absence of nontrivial Collatz cycles globally.

For each row `y`, follow the known support arrows to the first exit `z` after `d(y)` steps. Define

\[
v_z(k)=\sum_{y:z(y)=z,\ d(y)=k}J(y),\quad
F_z(u)=\sum_{k\le u}v_z(k).
\]

Then

\[
\boxed{H_L((I-P)J)=\sum_zF_z((L-\tau(z))_+).} \tag{Exit}
\]

Include `0` among every profile's possible values. Thus

\[
\mathcal C_-(J):=\sum_z\min(0,\min F_z)
\le H_L\le
\mathcal C_+(J):=\sum_z\max(0,\max F_z).
\]

`C_+(J)<=||J^+||_1`. Exits need not have independent futures: separately maximizing their profiles is safe even if the actual futures are correlated. The bound is not necessarily sharp for those correlated futures.

### 7.4 Discovery is not verification

The stored currents were discovered by following a finite union of trajectories toward a small core, combining signed visits, and completing the checked core. The search aborts at an unresolved cycle or a cap. Its success for arbitrary source sizes is **not** proved.

Verification is different: check the finite divergence identity and the finite exit graph. No continuation beyond exits is needed. A cheap checker does not imply a uniformly cheap or always-successful constructor.

---

## 8. The strongest supplied finite certificates, and the active open problem

### 8.1 Actual freshly rerun tables [FINITE]

| Cutoff N | Anchor m | Packet atoms | Current rows | Exits | All-horizon packet lower | All-horizon packet upper |
|---:|---:|---:|---:|---:|---:|---:|
| 4096 | 2 | 1752 | 2736 | 176 | -1406 | 2364 |
| 262144 | 4 | 79516 | 132998 | 7045 | -57661 | 63824 |

These bound `H_L(Pi_hat_(m,N))` for **every L>=0**, at the named finite source cutoff. The latter upper bound is below `N/4`; it is not evidence sufficient for uniform `O(N)` cost.

At `N=4096`: early signed totals `(-1,1)`, anchor remainder positive/negative norms `(22,20)`, target horizon `69`, hence

\[
-2746/3\le\mathcal E_T(4096)\le3838/3\quad(0\le T\le69).
\]

At `N=262144`: early totals `(-1,1,1,2)`, remainder norms `(209,202)`, horizon `231`, hence

\[
\boxed{-34504\le\mathcal E_T(262144)\le37090\quad(0\le T\le231).}
\]

The residual is paid by its worst possible contribution, not followed. The latest bundle reports additional finite currents at fourteen cutoffs; complete stored tables are supplied for the two above.

### 8.2 Active sufficient local target [OPEN]

Construct finite `J_N` with

\[
\widehat\Pi_{m,N}=(I-P)J_N,\qquad\mathcal C_+(J_N)=O(N).
\]

Or allow

\[
\widehat\Pi_{m,N}=(I-P)J_N+\zeta_N,
\]
\[
\mathcal C_+(J_N)=O(N),\qquad
\|\zeta_N^+\|_1=O(N^{4/5}/\log N).
\]

Then Current, Exit and Reduce give a one-sided `O(N)` discrepancy on the natural source-power window. **Neither uniform estimate is proved.** Neither the sparse number of exits nor successful trajectory searches at finitely many cutoffs bounds the cost at all scales.

To connect this local target to the final mean-work comparison, retain the rectangular-domain warning from Section 4.2. A complete global proof must establish the necessary source/time uniformity or a direct accumulated recurrence-tree estimate. Do not write "cheap packet currents imply Collatz" without supplying that last domain step.

### 8.3 What would actually move the programme forward

Derive current weights or exit-profile bounds from **the packet's source interval and word arithmetic**, rather than running every sample orbit to a known core. Plausible formulations include cancellation between neighboring packets, source-scale recursive currents, or incomplete currents whose positive residual alone is affordable. These are suggestions, not results.

Mandatory hostile tests:

- Opposite arrival lags can change the sign (`6929,6947,6965` versus `55,73,91`).
- Balanced triples need not contract in synchronous norm.
- A packet's actual genealogical restriction must be used; arbitrary finite state collections can be selected to expand for arbitrarily long times.
- Certificate cost, not just finite representability by a current, is the missing quantitative input.

---

## 9. Exact-source current proofs: compact reconstruction checklist

To rebuild the current critical path without any old prose:

1. Prove Cyl, then the exact recurrence TR from the three first-valuation classes.
2. Define `nu_N`; verify `3 E_T(N)=H_T(nu_N)` by the finite layer-cake identity.
3. Enumerate words of length d and A<=b. In each component, determine the positive lift interval excluding source/endpoint 1.
4. Group complete triples of lifts. Use the source weights modulo 3 to prove every packet's total is zero; keep the at-most-two right leftovers.
5. Count the over-budget classes exactly. This proves Packets and the entropy-based `16N^(7/9)` bound.
6. Apply the construction at early depths as well, obtaining Reduce with no omitted initial mass.
7. For supplied `J`, verify `(I-P)J=Pi_hat`; compute acyclic support exits and level prefix sums. Prove Current and Exit by finite telescoping, including infinite exit hitting times.
8. For each finite N, combine early totals, exit-profile bounds, and signed remainder norms to get the stated complete finite-window error interval.
9. For a new uniform theorem, prove an a priori construction/cost bound and resolve its final source/time domain. Do not replace these steps by a successful finite search.

None of Steps 1--8 needs Tao's mixing extension, Rhin, mechanical words, or an assumed Collatz conjecture.

---

## 10. Executable minimal reconstruction kernel

Python 3.10+, standard library only. This is deliberately a **finite verifier and packet constructor**, not a current-discovery theorem. It can rebuild the core small examples without any archive. Large stored current tables still require the supplied data or a separate, explicitly terminating search.

```python
from collections import defaultdict
from math import comb


def clean(mu):
    return {x: c for x, c in mu.items() if c}


def add(*mus):
    out = defaultdict(int)
    for mu in mus:
        for x, c in mu.items():
            out[x] += c
    return clean(out)


def neg(mu):
    return {x: -c for x, c in mu.items()}


def step(x):
    if not isinstance(x, int) or x <= 0 or not (x & 1):
        raise ValueError('Expected a positive odd integer')
    z = 3*x + 1
    a = (z & -z).bit_length() - 1
    return z >> a, a


def push(mu):
    out = defaultdict(int)
    for x, c in mu.items():
        if x <= 1:
            raise ValueError('Signed measures exclude the absorbing state 1')
        y, _ = step(x)
        if y > 1:
            out[y] += c
    return clean(out)


def initial(N):
    n1, n2 = (3*N + 1)//2, (3*N + 1)//4
    return {
        x: 3*int(x % 3 == 2) - 1
           + (3*int(x % 3 == 1) - 1 if x <= n2 else 0)
        for x in range(3, n1 + 1, 2)
    }


def words_leq(depth, budget, prefix=()):
    if depth == 0:
        yield prefix
        return
    for a in range(1, budget - depth + 2):
        yield from words_leq(depth - 1, budget - a, prefix + (a,))


def cylinder(w):
    A = C = 0
    for a in w:
        if a < 1:
            raise ValueError('Positive valuations required')
        C = 3*C + (1 << A)
        A += a
    power = 3**len(w)
    period = 1 << (A + 1)
    q = (((1 << A) - C)*pow(power, -1, period)) % period
    e, rem = divmod(power*q + C, 1 << A)
    assert rem == 0 and q > 0 and e > 0 and q % 2 and e % 2
    return q, e, period


def exact_source_packets(N, depth):
    b = (N - 1).bit_length()
    if N < 8 or not 1 <= depth <= b//2:
        raise ValueError('Require N>=8 and 1<=depth<=ceil(log2 N)/2')
    out = defaultdict(int)
    count = 0
    for w in words_leq(depth, b):
        count += 1
        q, e, period = cylinder(w)
        first = 0 if q > 1 and e > 1 else 1
        for cutoff, target in (((3*N + 1)//2, 2), ((3*N + 1)//4, 1)):
            last = (cutoff - q)//period
            size = max(0, last - first + 1)
            for block in range(size//3):
                t = first + 3*block
                total = 0
                for j in range(3):
                    source = q + period*(t+j)
                    endpoint = e + 2*3**depth*(t+j)
                    weight = 3*int(source % 3 == target) - 1
                    assert 1 < source <= cutoff and endpoint > 1
                    out[endpoint] += weight
                    total += weight
                assert total == 0
    assert count == comb(b, depth)
    return clean(out)


def verify_decomposition(N, depth):
    b = (N - 1).bit_length()
    mu = initial(N)
    for _ in range(depth):
        mu = push(mu)
    packet = exact_source_packets(N, depth)
    remainder = add(mu, neg(packet))
    bound = 6*comb(b, depth) + 2*sum(comb(b, j) for j in range(depth))
    assert sum(packet.values()) == 0
    assert sum(abs(c) for c in remainder.values()) <= bound
    return packet, remainder


def check_current(mu, J):
    if any(x <= 1 or x % 2 == 0 or not isinstance(c, int) for x, c in J.items()):
        raise ValueError('Invalid signed current row')
    assert add(J, neg(push(J))) == clean(mu)
    return sum(max(c, 0) for c in J.values())


def exit_bounds(J):
    # Simple verifier, intentionally not optimized. Never follows past an exit.
    profiles = defaultdict(lambda: defaultdict(int))
    support = set(J)
    for source, weight in J.items():
        seen = set()
        y, distance = source, 0
        while y in support:
            if y in seen:
                raise ValueError('Cycle inside current support: handle separately')
            seen.add(y)
            y, _ = step(y)
            distance += 1
        profiles[y][distance] += weight
    lower = upper = 0
    for levels in profiles.values():
        running = lo = hi = 0
        for distance in sorted(levels):
            running += levels[distance]
            lo, hi = min(lo, running), max(hi, running)
        lower += lo
        upper += hi
    return lower, upper


def known_lag_current(sources, weights, delays, meeting):
    # Lengths are proposed finite witnesses and are checked exactly.
    assert sum(weights) == 0
    J = defaultdict(int)
    for source, weight, delay in zip(sources, weights, delays):
        y = source
        for _ in range(delay):
            assert y > 1
            J[y] += weight
            y, _ = step(y)
        assert y == meeting
    J = clean(J)
    mu = add(*({x: c} for x, c in zip(sources, weights)))
    check_current(mu, J)
    knots = {0, *delays}
    values = [sum(c*min(u, d) for c, d in zip(weights, delays)) for u in knots]
    return J, min(values), max(values)


if __name__ == '__main__':
    for N, d in ((32, 1), (512, 2), (4096, 2)):
        verify_decomposition(N, d)
    J, lo, hi = known_lag_current((6929, 6947, 6965), (-1, -1, 2), (49, 32, 3), 23)
    assert (lo, hi) == (-75, 0)
    J2, lo2, hi2 = known_lag_current((55, 73, 91), (1, 1, -2), (8, 9, 0), 91)
    assert (lo2, hi2) == (0, 17)
    print('Finite packet and common-tail checks passed.')
```

For a CSV current, parse every `(state,weight)` row exactly, reject duplicate rows, then use `check_current` and `exit_bounds`. Do not pass probabilities in place of the signed integers. For large tables, memoize exits and distances; still reject cycles explicitly. Computing a fifth-root time horizon should use integer comparison `(T-1)^5 < (b+1)^5*N <= T^5`, not a floating-point ceil.

---

## 11. The earlier analytic transport branch: preserve it, but isolate its risk

This branch is not required by the newest exact-source packet/current proofs. It is worth preserving because it controls the leading bulk and growing logarithmic time windows. The claimed analytic extension has a materially higher verification burden than the elementary current identities.

### 11.1 Periodic residue profiles [supplied complete induction proof]

For dyadic `N=2^b`, define `q_d=3^(d+1)`, `L_d=2*3^d`, and `Z_(d,b)=q_d*2^(b-1)`. The initial table `G_1(k,r)`, with `k` modulo 6 and unit columns `r=1,2,4,5,7,8 modulo9`, is

```
k=1:  0 -1  0 -1  0  2
k=2: -1  1  2 -2 -1  1
k=3:  1  3  1 -3 -2  0
k=4:  3  2  0 -1 -3 -1
k=5:  2  1 -1  1 -1 -2
k=6:  1  0 -2  0  1  0
```

Set `G_d(k,r)=0` for `k<=0` or `3|r`. Recursively,

\[
G_{d+1}(k,r)=
\sum_{\substack{1\le a<k\\2^a r\equiv1\ (3)}}
G_d\left(k-a,\frac{[2^ar]_{3^{d+2}}-1}{3}\right). \tag{G}
\]

Inductively,

\[
G_d(k+L_d,r)=G_d(k,r)\quad(k\ge1),\qquad
\sum_{j=0}^2G_d(k,r+j3^d)=0.
\]

For periodicity, group the extra `3L_d` summands in triples and use `v_3(2^{L_d}-1)=d+1`; the inverse residues cycle through the three old fibers. Also `G_d(k,r)=0` for `1<=k<d`.

The homogeneous spatial profile is

\[
B_{d,b}(y)=G_d(\lfloor\log_2(Z_{d,b}/y)\rfloor,y\bmod q_d)
\]

on its positive bands. Compute the band index exactly by integer bit length. The actual flow is

\[
P^d\nu_{2^b}=B_{d,b}+R_{d,b}.
\]

The correction is essential: `R_(6,5)=2 delta_137`. This comes from `floor(3^7/2^3)=273=3*91`, `S(91)=137`, and the relevant profile jump of 2.

To rebuild all corrections, for each depth d enumerate `v_h=floor(3^(d+2)/2^h)`. Keep `x_h=v_h/3` that are odd integers greater than 1, not divisible by 3, with `y_h=S(x_h)>1`. Inject

\[
J_{d,b}=\sum_h\bigl[G_d(b-1+h,x_h)-G_d(b-2+h,x_h)\bigr]\delta_{y_h},
\]

with residues interpreted modulo `q_d`, and set `R_(d+1,b)=P R_(d,b)+J_(d,b)`, `R_(1,b)=0`. The support is contained below `3^(d+1)` and has at most `(d-1)(d+4)` atoms. Sparse support does not control weights or lifetime.

### 11.2 Exact bulk coefficients and fixed-depth results

Let `H_(d,k)=sum_r |G_d(k,r)|`. Then

\[
\gamma_d=\frac18\sum_{k\ge1}2^{-k}H_{d,k}
=\frac{\sum_{k=1}^{L_d}2^{L_d-k}H_{d,k}}{8(2^{L_d}-1)}.
\]

For fixed d,

\[
\|P^d\nu_{2^b}\|_1=2^b\gamma_d+\varepsilon_{d,b\bmod L_d}.
\]

The signed total itself is periodic in b. It follows that for fixed `T>=2`, `E_T(2^b)` has period dividing `2*3^(T-1)` in b. This says nothing uniform when T grows with N.

Reported exact first-five-depth bounds for the specified initial family are

| d | Leading coefficient, approximate | Sharp uniform norm ratio | Equality N |
|---:|---:|---:|---:|
|1|11/14|13/15|16|
|2|0.6673361486|87/127|128|
|3|0.5728813680|38/63|64|
|4|0.5065674574|264/511|512|
|5|0.4540747257|39/85|256|

The first-step exact formula is

\[
\|P\nu_{2^b}\|_1=(11\cdot2^b+e_{b\bmod6})/14,
\quad(e_0,\ldots,e_5)=(-46,-22,-30,-4,6,-16).
\]

**Do not iterate these scalar factors.** `P^4 nu_16=-3 delta_13`, `P^5 nu_16=-3 delta_5` have equal norm. Also `||P^4 nu_32||=13`, `||P^9 nu_32||=7`, violating the proposed repeated `39/85` factor. The evolved family is different.

A faster exact row recurrence is

\[
G_{d+1}(k+1,r)=G_{d+1}(k,2r)
+\mathbf1_{2r\equiv1(3)}G_d\left(k,\frac{[2r]_{q_{d+1}}-1}{3}\right).
\]

The truncation bound `H_(d,k)<=10 binom(k-1,d-1)` gives

\[
0\le\gamma_d-\frac18\sum_{k=1}^{K}2^{-k}H_{d,k}
\le\frac54\,2^{-K}\sum_{j=0}^{d-1}\binom Kj.
\]

The stored calculation reached `d=12,K=120`, with `gamma_12` in `(0.254971958466153138,0.254971958466153139)`. Finite values do not prove decay.

### 11.3 Claimed superpolynomial bulk decay [ANALYTIC CANDIDATE]

The inherited note claims

\[
\boxed{\gamma_d\ll_p d^{-p}\text{ for every fixed }p>0,\qquad\sum_d\gamma_d<\infty.}
\]

Its external input is the **nonnegative paired-factor envelope** inside Tao's proof, not merely an unconditional marginal Fourier coefficient. Precisely audit equation (7.5), Lemma 7.2 and Proposition 7.3 of arXiv `1909.03562v7`, printed pages 34--35. Those passages were reportedly inspected in previous sprints; this handoff did not independently refresh the web source.

Reconstruction outline:

1. Let independent `a_i` have `Pr(a_i=k)=2^-k`. Preserve their total `A_d`. Reverse the offset if convenient:
   
   \[
   Z_d=\sum_{j=1}^d3^{j-1}2^{-(a_1+\cdots+a_j)}.
   \]
2. Pair variables with sums `B_j=a_(2j-1)+a_(2j)`. Conditional on these sums, a bounded weight `phi(A_d)` is fixed. Tao's product of **absolute conditional factors** still bounds the weighted characteristic function. For one missing variable at conductor `3^m`, adjoin a fictitious pair: its sum is 2 with probability `1/4`, with unit absolute factor. This costs at most 4, not a division by the probability of a rare specified total.
3. Conclude an unnormalized bound, uniform in bounded `phi`, for `E[phi(A_(m-1)) chi(Z_(m-1))]` at primitive characters modulo `3^m`.
4. To obtain joint total-variation control, use `n=d+1` and stop a prefix just above `h=floor(alpha*n-4L log2 n)`. Except on `O_L(n^-cL)+O(exp(-cn))`, its length `k<=0.9n`, sum `l<=alpha*n-3L log2 n`, and partial sums exceed `(7/4)j-L log2 n`.
5. Those conditions imply `0<2^l Z_k<C0*3^n*n^-2L<3^n`. Distinct words with fixed k,l have distinct integer numerators; recover their prefix sums by exact 2-adic denominator extraction. Each atom has probability `2^-l<=2n^(4L)/3^n`.
6. Conditional on this prefix, the tail remains independent. Preserve the specified **final total** using the indicator of the tail total; do not normalize it. Primitive-frequency Fourier coefficients are `O_B(n^-B)` by Step 3.
7. Plancherel plus the prefix max-atom bound gives `L2^2 <= O(n^(4L-2B)/3^n)`. Multiplying by `sqrt(3^n)` in Cauchy--Schwarz leaves `L1=O(n^(2L-B))`. Sum at most `O(n^3)` choices of k,l,tail-total, then choose L and B large enough.

This proves, if the argument survives audit, highest-digit averaging in the **joint law** `(A_d,Z_d mod 3^(d+1))`, with full l1 error `Delta_d <<_p d^-p`.

To link this to gamma, use the exact continuous signed source density `(1/6)w_c(u)du`, where

```
0 < u <= 3/4:  (w0,w1,w2)=(-2, 1, 1)
3/4 < u <=3/2: (w0,w1,w2)=(-1,-1, 2)
```

Its norm is 1 and `sum_c w_c(u)=0`. Transport by the auxiliary word to

\[
(v,r)=(3^d2^{-A}u,\ F_d+3^d2^{-A}c\bmod3^{d+1}).
\]

The word probability `2^-A` cancels the spatial Jacobian, giving density `G_d/(2*3^(d+1))`; its norm is exactly gamma. Averaging the highest ternary digit makes the output independent of c and annihilates the signed source. Therefore `gamma_d<=Delta_d`.

**Critical guards:** marginal offset mixing is insufficient; retain A exactly and one extra ternary digit. The auxiliary geometric law represents the leading bulk, not the law of a fixed integer orbit. This entire analytic extension is optional for the newest current route and deserves separate external review.

### 11.4 Boundary-window consequence and order of limits

An earlier elementary bound, for arbitrary integer cutoffs, was

\[
\left|\|P^d\nu_N\|_1-N\gamma_d\right|,
\quad |\langle1,P^d\nu_N\rangle|
\le4(b+2d+2)3^{(d+1)(d+2)/2}.
\]

At `m=floor(sqrt(b/2))`, this is at most `sqrt(2N)` for `b>=1024`. Nonexpansivity then gives, for every `d>=m`,

\[
\|P^d\nu_N\|_1\le N\gamma_m+\sqrt{2N}.
\]

With the analytic candidate, this proves arbitrary inverse-log savings through every **fixed polylogarithmic** time horizon, and an adaptive gamma-dependent window. It does not reach `N^(1/5)log N`: `d^-p` for every fixed p does not permit p to grow with N without controlling its constants.

The newer exact-source packet reduction fixes the remainder at the source-power horizon, but not the packet absorption contribution. Do not conflate these two advances into a full residence theorem.

---

## 12. Earlier direct-Collatz results worth retaining [mostly HISTORICAL]

These were reported with candidate proofs and finite certificates earlier in the conversation. Their older full archives are not all mounted here. They are not dependencies of Sections 4--10. Preserve proof ideas and scope, then recover the original notes before invoking numerical constants in a manuscript.

### 12.1 Multiplier barrier and least-source localization

For any contractive length-n word, terminal suffix sums satisfy `S_k>=k` for `k<n`, `S_n=A`. Thus

\[
F_w\le(3/2)^{n-1}-1+3^{n-1}2^{-A},
\]

maximized at fixed n,A by `(A-n+1,1,...,1)`. The ratio `beta_w/2^(A+1)` decreases with A, so maximize at `A=ceil(n alpha)`.

The reported sharp all-word barrier was

\[
\frac{\beta_w}{2^{A+1}}\le\frac{1121}{6656}<\frac14,
\]

attained by `(4,1,1,1,1)`. Its actual least source 165 descends to 161: barrier sharpness is not an integer exception.

Proof architecture: exact rational checks through n=127; for larger n use Rhin's bound on `H_n ln2-n ln3`, weakened to exponent 14, to obtain

\[
\frac{\beta_w}{2^{A+1}}<\frac{(2n)^{14}}{3\,2^n}.
\]

Hence every nonminimal lift of every contractive cylinder descends. Only `q_w` can fail.

A sharper **actual-exception** bound was reported:

\[
\frac{x}{2^{A+1}}\le\frac{589}{2^{28}},\qquad x>1,
\]

for realized contractive/non-descending blocks. Equality: `589`, length17, total27, endpoint593. It already descends at its first step to221.

Its proof used the same large-n envelope from n=130 onward; for n<=129 the minimum-state product bound restricted an intermediate odd minimum below3343, endpoint/source below425645, then an exhaustive list of148 exceptions was checked. This finite catalogue is an extra dependency, not supplied by the barrier inequality alone. The consequence was `A>=floor(log2 x)+18` for actual nontrivial exceptions.

### 12.2 First contraction and minimum-preserving blocks

If all `x_i>=x_0=x>1` through a contractive endpoint, multiplication of step ratios gives

\[
2^{H_n}\le(3+1/x)^n,
\qquad
x\le\frac1{2^{H_n/n}-3}<\frac{n(2n)^{14}}3.
\]

Thus true minimum-preserving exceptions have polynomial, not exponential, source envelopes at fixed n. The 148 historical short rebound blocks all already descended earlier; they are not first-passage failures.

The external Rozier--Terracol shortcut-CST verification through `V=2.8*10^19`, plus a Farey separation, reportedly gives the all-input first-contraction horizon `10,439,860,591` shortcut steps (`6,586,818,670` odd-step threshold). Fractions:

\[
\frac{9809721694}{6189245291}<\alpha<
\frac{10439860591}{6586818670}<\log_2(3+1/V)
<\frac{630138897}{397573379}.
\]

The exterior fractions have determinant1; any intermediate reduced rational has denominator at least the sum of exterior denominators. Rebuild the real inequalities with rational atanh-series log enclosures. Keep the exact clock, strict endpoints, and **external input-range verification** explicit; this was not a billions-step orbit scan.

### 12.3 Width--complexity collision theorem

For a contractive, non-descending genuine block of length N, suppose drift width

\[
\Omega_N=\max_iD_i-\min_iD_i<R
\]

with integer R>=1. Let `p_w(k)` count distinct length-k factors,

\[
m=\lceil\log_2N\rceil,\quad K=12m+2R+16,\quad
P_0=\max(R,p_w(K)).
\]

The reported theorem: either `N<K`, or

\[
\boxed{N<K+2^{23}R P_0^{15}.}
\]

Proof spine: non-descent plus Rhin bounds `x_0<2^(R+15)N^15`; width bounds all intermediate states by `2^(2R+16)N^15`. Every K-factor has source modulus larger than every state. Two identical factors among the first `P_0+1` starts then force **equal integers**, not merely equal residues. Their tail is periodic with period `ell<=P_0`. Width bounds `t|B-ell alpha|<R` over t periods; Rhin gives `|B-ell alpha|>(3P_0)^-14`. Bound t and hence N. No assumption that only the trivial cycle exists is used.

This is a restricted obstruction: large width or high complexity may evade it.

### 12.4 Mechanical and phase-switched families

At a drift-record endpoint, terminal sums obey `S_k>=H_k=ceil(k alpha)`. The affine offset obeys

\[
F_w\le U_n=\sum_{k=1}^n3^{k-1}2^{-H_k}<n/3.
\]

The maximum is the reversed critical mechanical word with increments `H_k-H_(k-1)`.

Reported all-length descent families include: the exact mechanical words; at most two positive contact defects `E_k=S_k-H_k` across the whole word; and common-phase suffix profiles

\[
S_k=\lfloor k\alpha+\theta\rfloor+1.
\]

A one-switch extension uses two phases on two intervals of suffix lengths, retaining only positive valuation increments. With r phase regions, width is <2 and factor complexity at most `rk+2`, so the general collision theorem gives

\[
N<K+2^{24}(rK+2)^{15},\quad K=12\lceil\log_2N\rceil+20.
\]

Large-length exclusions were combined with finite minimum-endpoint suffix covers to obtain the reported all-length results. The finite certificates are essential. Arbitrary binary contact profiles are **not** covered by the common-phase result. No theorem forces an arbitrary hypothetical counterexample into any such family.

### 12.5 Sparse divergent orbits and phase laws

The elementary collision mechanism can be rebuilt without any early constants. For positive odds below `2^b`, after k odd steps,

\[
\#S^k(\mathbb O\cap[1,2^b))
\le\sum_{j=k}^{b-1}\binom{b-1}{j}+3^k.
\]

Low total valuation `A<b` gives the exact binomial source count. High A forces endpoints below `2*3^k` by the universal affine-offset bound. On a nonrepeating orbit, `S^k` is injective on the orbit set, so the same expression bounds its occupation count.

Taking `b=5t,k=3t` gives a power saving with `G=3125/108<32`:

\[
\#(V\cap[1,32^t))\le2G^t.
\]

Shell summation proves `sum_n 1/x_n<infinity` on a nonrepeating positive orbit. This is in the classical Garcia--Tal coalescence/sparsity tradition; do not claim discovery of orbit sparsity.

Consequently the product in Product has `1<P_infinity<infinity`,

\[
\frac{3^n}{2^{A_n}}\to\infty,\qquad D_n\to-\infty,
\]

and

\[
\log_2x_n=\log_2(x_0P_\infty)+n\alpha-A_n-o(1).
\]

The odd-time binary significand asymptotically follows one irrational rotation. Similar natural bases are 3 for shortcut time and 6 for unaccelerated time. Leading-digit marginals are not mixing: fixed-lag Fourier correlations retain modulus1. No general decimal law or independence of low bits follows.

For finite distinct prefixes, pay the last k positions before using injectivity under `S^k` or `T^k`. Constants such as432 and480 appeared in different historical finite-prefix reconstructions; use a specific proof rather than silently interchanging them. These phase/sparsity results do not force descent and are not used by the current packet proof.

### 12.6 Exact survival cells and the eight-source theorem

Condition on one exact history w, a finite initial interval, and no descent below the source. Each survival condition is linear in the lift parameter t. Hence the surviving t's form a consecutive interval. Its current endpoints are `y+2*3^n*j`.

Their next valuations have a unique maximum at `j_*`; elsewhere

\[
a_j=1+v_2(j-j_*).
\]

Uniqueness: two equal maximal 2-adic valuations would force a still larger one at an intervening position. Subtraction from the unique peak proves the ruler law.

For m endpoints,

\[
\sum a_j=a_*+2(m-1)-s_2(j_*)-s_2(m-1-j_*),
\]

and each tail count differs from `m2^(1-h)` by less than1. All very large next valuations reside at one peak per cell. TV closeness alone does not control its unbounded height.

The historical theorem: groups of size m>=8 contract in next-step geometric mean. Use `sum a_j>=2m-s_2(m)`, `s_2(m)/m<=3/11`, and average correction <1/8 to bound growth by `alpha-141/88<0`. Seven can fail: endpoints `(11,17,23,29,35,41,47)` have valuation word `(1,2,1,3,1,2,1)` and next-step product ratio `1516489/1285309>1`.

This theorem applies to **one surviving arithmetic cell**, not arbitrary terminal-survivor unions. In a dyadic bin, histories become singletons by odd time b-1. That loss of averaging motivated the current cross-history route.

---

## 13. The independent positive inverse-Syracuse / PCP project

This is a separate theorem chain. It shares exact cylinder algebra with the convergence programme but supplies no direct forward-halting undecidability claim.

### 13.1 Free rational action

For odd rational 2-adic units, define `R_a(y)=(2^a y-1)/3`. Then

\[
F_0=R_2\circ R_3=(32y-7)/9,\qquad
F_1=R_3\circ R_2=(32y-11)/9.
\]

Use the convention `F_(b1...bm)=F_b1 o ... o F_bm`, so the leftmost bit is decoded first in forward time. The valuation blocks are `0 -> (2,3)`, `1 -> (3,2)`. The root 3 has next valuation 1, a delimiter outside both blocks.

Therefore

\[
F_u(3)=F_v(3)\iff u=v.
\]

Proof: distinct bits give different exact valuation blocks; a strict-prefix case encounters the marker valuation1 versus a continuing2/3. The maps keep the real-positive ray `[3,infinity)` positive. This is a rational free-action claim, not an integer-integrality claim.

### 13.2 Explicit positive-integer compiler

On `U={n>=1:n odd,3 does not divide n}`, set

\[
G_i(n)=\frac{2^{a_i(n\bmod9)}n-1}{3},
\]

with

| n mod 9 | 1 | 2 | 4 | 5 | 7 | 8 |
|---|---:|---:|---:|---:|---:|---:|
| a_0 | 4 | 3 | 6 | 3 | 4 | 5 |
| a_1 | 8 | 7 | 8 | 9 | 10 | 7 |

Every table entry has `2^a n == 4 or7 mod9`. Thus its output is integral, odd, positive, and not divisible by3. Also `G_i(n)>2n` and `S(G_i(n))=n` with exact valuation a.

Define `Gamma(empty)=1`, `Gamma(bw)=G_b(Gamma(w))`. The disjoint valuation bands `[3,6]` and `[7,10]` decode the bit; the marker1 has valuation2. Thus Gamma is injective, every codeword first reaches1 after its word length, and its bit size is linear in word length (`2^m<Gamma(w)<2^(10m)` for m>=1).

The codebook is decidable: repeatedly compute the exact next valuation, check its band and the table at the decoded successor modulo9, reject on mismatch, and stop at1. Every accepted step halves the integer or better, so the decoder terminates in `O(log x)` iterations. This is not the general Collatz decision problem.

### 13.3 Relational PCP reduction

Input: paired binary words `(u_i,v_i)`. Ask whether a nonempty index word `i_1...i_t` satisfies

\[
G_{u_{i_1}}\circ\cdots\circ G_{u_{i_t}}(1)
=G_{v_{i_1}}\circ\cdots\circ G_{v_{i_t}}(1).
\]

Injectivity makes this equivalent to equality of the two concatenated binary words: PCP. The elementary two maps are fixed, while the paired macro descriptions are input. Neary's five-pair PCP undecidability result is an external input for that restriction.

**What is hard:** the existential synchronized word relation. **What is easy:** every individual codepoint's orbit and membership in the codebook. Every point used by the reduction reaches1. Do not describe this as ordinary Collatz halting undecidability.

A cylinder alternative uses `kappa(0)=(1,1)`, `kappa(1)=(1,2)`, with terminal delimiter `(2)`. Two such terminated words are prefix-comparable iff the original binary words are equal. Exact positive cylinders intersect iff their valuation words are prefix-comparable. This gives the related synchronized cylinder-intersection formulation.

### 13.4 Every finite valuation word has an explicitly convergent completion

For a length-L word w with total A and numerator C_w, a terminal valuation b leading to1 requires

\[
X=\frac{2^A(2^b-1)-3C_w}{3^{L+1}},
\quad
2^b\equiv1+3C_w2^{-A}\pmod{3^{L+1}}.
\]

The right side lies in the subgroup `1 mod3`. Even powers of2 run through that subgroup, with exponent period `2*3^L`. Let b0 be the least positive even solution. Integrality of the whole inverse chain implies positive integral predecessors; `b>2` ensures the final pre-1 endpoint exceeds1 and prevents an earlier hit.

The reported optimal one-extra-step first-hit completion is

\[
b_{\min}(w)=
\begin{cases}b_0,&b_0>2,\\2+2\cdot3^L,&b_0=2,\end{cases}
\quad b_{\min}\le2\cdot3^L+2.
\]

The worst case is w consisting of L copies of2. For the all-one word, `b_min=3^L+1`. One explicit source is

\[
X_L=2^{L+1}\frac{2^{3^L}+1}{3^{L+1}}-1,
\]

with exact valuation word `(1^L,3^L+1)` ending at1. LTE proves integrality.

**Adversarial importance:** any finite symbolic pattern can occur in a convergent trajectory. Arbitrarily many expanding-looking steps can be followed by one huge valuation. A small frequency of such a tail atom does not make its contribution to mean drift small.

### 13.5 Fixed-root two-step padding and its limitation

For any odd root x with `3 does not divide x` and B>=7, choose the unique `a in{1,...,6}` with

\[
2^Bx\equiv3+2^a\pmod9,
\quad
z_B(x)=\frac{2^Bx-3-2^a}{9}.
\]

Then `S^2(z_B)=x` with valuations `(a,B-a)`, `z_B>x`, and

\[
z_{B+6}(x)=64z_B(x)+7(3+2^a).
\]

For a hypothetical nonrepeating orbit from x, put `B_(n,j)=H_(n+2)+j-A_n`, `delta_n=H_(n+2)-(n+2)alpha`. The full padded block has coefficient `2^(-delta_n-j)`. Its non-descent condition is exactly

\[
2^{-\delta_n-j}P_n\ge1-\frac{3+2^{a(B_{n,j},x)}}{2^{B_{n,j}}x}.
\]

Using finite `P_infinity` and irrational-rotation equidistribution, the canonical rooted event has density

\[
\min\{1,\max\{0,\log_2P_\infty-j\}\}.
\]

Its finite-order statistics agree in density with interval coding of the same irrational rotation. These are correlated descriptions of the original orbit, not additional independent constraints. Normalized padded sources tend to zero like `x/(18*2^{A_n})`; improving a fixed localization constant cannot exclude this construction.

The padding descends from z to x immediately. It is inapplicable to minimum-preserving first-descent bounds. Canonical rooted-event finiteness distinguishes eventual periodicity from nonrepetition, but would still allow nontrivial cycles. Global finiteness of all nontrivial paradoxical source-length pairs is a stronger condition.

---

## 14. Failures and scope restrictions that must not be lost

### 14.1 The empirically attractive constant-2 cohort inequality is false

For terminal survivors, the conjecture

\[
F_{b,t}\ge7M_{b,t}/4-2\sqrt{M_{b,t}}
\]

passed earlier finite scans but fails for the **entire** cohort at `b=27,t=306`:

\[
M=11,\quad F=12,\quad(7M-4F)^2=841>704=64M.
\]

Its endpoints are

`103,155,233,719,2051,6911,10367,15551,23327,34991,52487`.

Six occupy time-shifted positions along an expanding valuation-1 tail. All eleven sources converge. This refutes only the constant-2 strengthening, not the scale-dependent FH-style criterion. Do not fit a new numerical constant and call it a theorem.

### 14.2 Large synchronized subcohorts can all expand and then converge

Arbitrarily many distinct sources in one dyadic bin can be selected to reach one common explicit convergent tail at one time; that tail can contain an arbitrarily long run of valuation1. Inverse branching supplies the sources, and the all-one completion supplies the tail. These are selected subcohorts, not necessarily the full survivor set. Any proposed aggregate theorem must exploit the entire initial interval and retain weights.

A related exact two-step interpolation plants any finite multiset of odd unit targets in one sufficiently high dyadic bin, by varying admissible exponents `a0+6j`. It is a stress test, not evidence for a uniform distribution.

### 14.3 The modulus / grading / universality programme was oversold

The labels "Goldilocks" and "Langlands-Collatz" were research metaphors. No actual Langlands correspondence was constructed. The concrete useful bridge is between real height/order, exact binary itineraries, ternary inverse residues, and signed cancellation on the ordinary orbit graph; preserve those mechanisms rather than the label.

- A class-wide universal-termination decision procedure containing ordinary Collatz would decide the Collatz instance. This is a scope warning, **not a proof of logical equivalence**, undecidability, or impossibility of a decidability theorem.
- The multiplier grading `(v_2 M,v_3 M)->(v_2 M-A,v_3 M+length)` is not a monotone grading of the integer state. Affine offsets allow cycles. It cannot by itself rule out Turing universality or even cycles.
- Symbolic full shifts on the 2-adics do not supply positive-integer realization. Rephrasing the problem as intersection with the positive integers does not solve it.
- Building a machine whose target is a universal Diophantine polynomial imports undecidability into the predicate; it is not a reduction into ordinary Collatz.
- A conserved parameter plus time does not alone imply decidability: a computable predicate in `(parameter,time)` can still define an r.e.-complete existential set.
- Finite observed short stopping times do not disprove logical independence. Computational undecidability of an instance set and unprovability of one universal statement are different questions.
- Conway and Kurtz--Simon concern **generalized programmable Collatz classes**, not the ordinary fixed map. Their results must be cited when making minimal-universality claims.

### 14.4 Preserve only the scoped negative results

A valid finite-trace observation for a modulus-m rational-affine map written `(A_r x+B_r)/m` is:

\[
x\equiv y\pmod{m^{B+1}}
\Longrightarrow
\text{same residue-dispatch trace through B steps}.
\]

Induct because one application divides a same-branch difference by at most m. Consequently, a bounded-step **trace-dispatched** zero test of a freely varying prime-exponent register requires its prime to divide m; otherwise a suitable exponent period makes zero and nonzero configurations congruent modulo `m^(B+1)`. This is not a theorem for arbitrary encodings or unbounded-overhead decoding.

A second scoped algebraic theorem: if an injective encoding of two unbounded counters is incremented by two **fixed commuting rational affine maps**, their nontrivial slopes must be multiplicatively independent. Commutation gives a common fixed point unless both are translations; rational translations cannot inject two independent counters, and mixed translation/nontranslation forces an identity map. In the common-fixed-point case, multiplicative dependence creates two distinct counter pairs with equal images. Rank-one slopes are excluded **for this encoding model**. Rank two is not a universal-computation threshold for arbitrary Collatz encodings.

For a p-primary map with dispatch modulo p^E, the normal form is

\[
g(r+p^Ez)=s_r+p^{E_r}(z+t_r),\quad0\le s_r<p^{E_r}.
\]

Positivity on positive inputs forces `t_r>=0` for r!=0, `t_0>=-1`, and if `t_0=-1` then `s_0>=1`. This is a local positivity restriction, not a global no-computation theorem. Tail-preserving cases have a prefix-rewriting interpretation; do not assert an unrestricted carry-class theorem without recovering the actual literature and proof.

### 14.5 A discarded inverse-padding "no-go" is simply false

An exploratory historical branch claimed every positive inverse chain of m steps had total valuation `B>=2m-2`. Do not retain it. The actual forward chain

\[
31\to47\to71\to107\to161
\]

has four valuations all equal to1. Reversed, it is a positive four-step inverse chain with B=4<6, even keeping all states coprime to3. A transition of inverse residues modulo9 generally needs the old value modulo27, not merely a representative modulo9. This concrete counterexample also illustrates why finite residue graphs must be checked for lost precision before being used as global obstructions.

### 14.6 General statistical guards

- Zero Haar measure or small density does not exclude a fixed positive integer.
- Leading-bit Benford behavior does not randomize trailing bits or the valuation mod6 cocycle.
- Zero density of symbol errors does not imply low topological complexity, decidability, or eventual periodicity.
- Spatial sparsity gives a spatial reciprocal-tail bound, not an effective time-tail cutoff unless future minimum heights are known.
- Fixed-depth source asymptotics cannot be interchanged with a source-dependent long time horizon.
- Signed cancellation/absorption percentages are not percentages of integer seeds proved to terminate.
- "Internally proved and computationally audited" is not human peer review, Lean verification, or novelty assessment.

---

## 15. The next research instruction and proof priorities

### Primary job

Work on **uniform one-sided current/exit-profile cost for the full exact-source packet family**, not arbitrary triples and not independently randomized endpoints. The goal is a genuinely arithmetic proof that survives source identification and actual tail correlations.

A useful next step would be one of:

1. A closed recurrence constructing currents from neighboring source words/intervals with a provable total positive exit-profile cost.
2. An incomplete construction whose unresolved **positive** residual is small enough on the target window, without paying negative residuals unnecessarily.
3. A concrete obstruction to the proposed uniform cost bound, with a mathematically justified replacement.

All must preserve the exact pair of source components, their cutoffs, packet ancestry, and absorption at1. A larger list of discovered current tables alone is not the missing proof.

### Audit order

1. Recheck the small exact-source packet proof and the current/exit identities first. They are short, elementary, and independent of the riskier historical analytic chain.
2. Verify the two stored finite certificates using the minimal one-step checker, not by rerunning all tails to1.
3. If using analytic bulk decay, separately audit the bounded-total-weight extension of Tao's paired envelope and the joint total-variation proof; do not import only marginal mixing.
4. Before declaring a Collatz implication, check every source/time quantifier in the workload comparison, including the expanding branch and smaller-source late times.
5. Keep the inverse-PCP manuscript independent. Verify its delimiter, positivity, composition order, and exact problem interface. It can be valuable without being a convergence breakthrough.

### The instruction to a successor model

> Treat this file as a proof map, not as an authority that every inherited claim is true. Start from the latest exact-source packet/current definitions. Preserve the open uniform-current problem and the global source/time-domain gap. Rebuild the short lemmas from the executable skeleton and supplied archives. Seek a structural bound or a rigorous counterexample, not another fitted constant or larger scan. Keep each result's correctness, novelty, and leverage toward Collatz separate. Do not give up because the problem is longstanding, and do not claim closeness merely because many sprints have been completed.

---

## 16. Sources, archive map, and citation boundaries

### 16.1 Mounted sources used for this consolidation

The following filenames identify actual supplied proof/data packages. This Markdown is self-contained at the proof-sketch level but does not embed their large tables.

| Package | Main material preserved here |
|---|---|
| `collatz_programme_handoff.md` | Earlier terminal-survivor/inverse-amplification phase; historical theorem ledger |
| `collatz_next_step_transport_bundle.zip` | FH/MW equivalence, exact workload recurrence, positive discrepancy, first finite-domain comparison |
| `collatz_transport_green_bundle.zip` | Signed measure, first-step 11/14 law, exact recurrence-tree identity, corrected quadratic boundary |
| `collatz_signed_multistep_bundle.zip` | Full G_d recurrence, ternary-fiber cancellation, affine corrections, fixed-depth scale laws |
| `collatz_signed_bulk_mixing_bundle.zip` | Analytic candidate for joint highest-digit mixing retaining total valuation; superpolynomial gamma decay |
| `collatz_boundary_window_bundle.zip` | Complete finite-source error bound and conditional growing-polylog-window consequences |
| `collatz_ternary_packet_bridge_bundle.zip` | Earlier homogeneous packet decomposition, source-power remainder, absorption-imbalance target |
| `collatz_packet_currents_bundle.zip` | Current source-exact packet reduction, common-tail identities, complete stored finite currents and exit profiles |

The newest archive contains full stored packet/current tables for N=4096 and N=262144, all source code, the independent C++ verifier, and original audit output. Re-extract it rather than assuming the top-level uploaded directory contains every dependency.

The original prior-to-transport sprint archives were not all present. Historical claims in Sections 12--14 are preserved from the conversation and old handoff, not newly certified by this task. Recover those archives before reproducing their numerical catalogues.

### 16.2 Minimal reproduction of the latest checked evidence

After extracting the latest archive, from its root:

```sh
python verify_stored_currents.py
```

Run normal Python, not `python -O`, because exact assertions are the checks. This invokes source packet reconstruction, current divergence checks, and finite exit profiles, not the current-discovery search.

To rebuild independently:

```sh
g++ -O2 -std=c++17 -Wall -Wextra independent_verifier.cpp -o independent_verifier
./independent_verifier 4096 2 data
./independent_verifier 262144 4 data
```

The two current tables have 2,736 and 132,998 nonzero rows. Their finite all-horizon bounds cannot be recreated merely from the numbers in this handoff: recover the tables or regenerate verified currents. The short code in Section10 reconstructs the mathematical mechanism and regression witnesses without those tables.

### 16.3 External mathematical sources

These are the references **as used in the supplied programme**, not a freshly researched survey in this handoff task.

- **Bernstein--Lagarias**, *The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics 48 (1996), 1154--1169. Exact parity-cylinder background. Primary copy: `https://websites.umich.edu/~lagarias/doc/bernstein.pdf`.
- **Krasikov--Lagarias**, *Bounds for the 3x+1 Problem using Difference Inequalities*, Acta Arithmetica 109 (2003), 237--258; `arXiv:math/0205002`; DOI `10.4064/aa109-3-4`. Fixed-root inverse-basin exponent0.84 is the external amplification input, not reproved by our finite certificates.
- **Tao**, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi10 (2022), e12; `arXiv:1909.03562v7`. First-passage transport background. The analytic candidate specifically needs the nonnegative paired envelope around equation(7.5), Lemma7.2 and Proposition7.3, not just a marginal mixing statement.
- **Rhin**, *Approximants de Pade et mesures effectives d'irrationalite*, Seminaire de Theorie des Nombres, Paris1985--86, Progress in Mathematics71 (1987),155--164; printed p.160 inequality(7). Historical bound `|u0+u1 ln2+u2 ln3| >= H^-13.3`, `H=max(|u1|,|u2|)>=2`; the programme uses `u0=0` and often weakens to exponent14. Not needed by the newest packet/current route.
- **Rozier--Terracol**, *Paradoxical behavior in Collatz sequences*, `arXiv:2502.00948v5`. Rebound/coefficient-stopping distinctions and externally imported verified input range. Version-specific claims must be checked in that source.
- **Garcia--Tal**, *A note on the generalized 3n+1 problem*, Acta Arithmetica90 (1999),245--250. Prior synchronous-coalescence and orbit-sparsity framework.
- **Halbeisen--Hungerbuhler**, *Optimal bounds for the length of rational Collatz cycles*, Acta Arithmetica78 (1997),227--239; **Lopez--Stoll**, *The 3x+1 conjugacy map over a Sturmian word*, Integers9 (2009),141--162. Important prior art for mechanical words and rational cycles.
- **Lagarias--Soundararajan**, *Benford's law for the 3x+1 function*, Journal of the London Mathematical Society74 (2006),289--303; `arXiv:math/0509175`. Do not conflate their seed/time/base quantifiers with individual-orbit natural-base corollaries.
- **Neary**, *Undecidability in Binary Tag Systems and the Post Correspondence Problem for Five Pairs of Words*, STACS2015, LIPIcs30,649--661; DOI `10.4230/LIPIcs.STACS.2015.649`. External PCP restriction, not a theorem about ordinary forward Collatz.
- **Conway**, *Unpredictable iterations* (1972), and **Kurtz--Simon**, *The undecidability of the generalized Collatz problem* (2007). Mandatory background for generalized-map universality; do not transfer their conclusions to the ordinary fixed map.

### 16.4 Final epistemic boundary

The programme's strongest current unconditional mechanisms are exact finite arithmetic identities and reductions. Its strongest current complete all-horizon bounds are at named finite source cutoffs. The analytic bulk branch is an inherited proof candidate with external dependencies. The uniform current-cost theorem, the required global mean-work estimate, and Collatz remain open within this work.

The value to preserve is not the chronology or the number of claimed theorems. It is the chain

\[
\boxed{\begin{gathered}
\text{exact sources}\longrightarrow\text{signed error}\\
\longrightarrow\text{balanced actual packets}\\
\longrightarrow\text{relative arrivals / finite currents}\\
\longrightarrow\text{one-sided cost}
\end{gathered}}
\]

The missing arrow is a **uniform arithmetic cost estimate**, with the right global source/time domain. That is the next research problem.
