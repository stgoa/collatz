# Sparse cutoff criteria for right-aligned currents

Date: 2026-10-17. Status: written conditional proofs with exact finite checks.
Collatz and universal current construction remain open. No novelty claim is made.
The main result is the five-ray criterion in Section 2. The 21-ray and
30-ray arguments are retained as scoped alternatives from this investigation.

## 1. Definitions retained from the main reduction

Use the odd-only Syracuse map, absorb at 1, and let
`e(x)=1` precisely when the positive odd state `x` never reaches 1.
Write `B(u)=sum_{odd x<=u} e(x)`, with `e(1)=0`.
For every integer `N>=8`, retain the original two-component source `nu_N`
and the revised right-aligned depth-one packet measure `Pi_N` from the main
proof note. Its remainder is supported on the terminating core `{5,7,11,13}`.
Consequently, with

\[
n_0=\left\lfloor(N-1)/4\right\rfloor,\quad
n_1=\left\lfloor(3N+1)/2\right\rfloor,\quad
n_2=\left\lfloor(3N+1)/4\right\rfloor,
\]

\[
(\mathcal L f)(N)=f(n_0)+\tfrac13f(n_1)+\tfrac13f(n_2),
\qquad
d_N:=\langle e,\Pi_N\rangle
=\langle e,\nu_N\rangle
=3\bigl(B(N)-(\mathcal LB)(N)\bigr).                 \tag{1}
\]

These are exact identities, with no missing boundary constant. `Pi_N` is a
finite signed integer measure, so `d_N` is an integer.

## 2. Five explicit dyadic rays suffice

Let `(a_0,a_1,a_2,a_3,a_4)=(12,14,16,18,21)` and define

\[
G_5=\{a_i2^b:0\le i\le4,\ b\in\mathbb Z,\ b\ge3\}.
\]

**Theorem.** Each of the following is equivalent to Collatz:

- for every `M in G_5`, the packet work `H_L(Pi_M)` is bounded above over
  all integer horizons `L>=0`;
- for every `M in G_5`, there is a finite exact current for `Pi_M`;
- for every `M in G_5`, there is a finite current whose residual is
  everywhere nonpositive.

There is no uniform bound on certificate size, cost, or running time.
There are five selected cutoffs in each interval `[12*2^b,24*2^b)`.

**Proof.** It suffices to assume `d_M<=0` for every selected cutoff;
each of the three hypotheses implies this as in the main proof note.
The key arithmetic inequalities are

\[
\begin{array}{c|ccccc}
 i&0&1&2&3&4\\\hline
 a_i&12&14&16&18&21\\
 3a_i/2&18&21&24&27&63/2\\
 \text{chosen upper target}&18&21&2\cdot12&2\cdot14&2\cdot16.
\end{array}                                                   \tag{2}
\]

Write `i+3=5s+j`, with `0<=j<=4`. For `M=a_i2^b`, the upper target in
equation (2) is `M'=a_j2^(b+s)>=3M/2`. Its half is at least `3M/4`.
Every selected cutoff is divisible by 8, so the source recurrence has
`n_0=M/4-1`, `n_1=3M/2`, and `n_2=3M/4` exactly.

Define the comparison value on the selected grid by

\[
F(a_i2^b)=2^{(5b+i)/3}.
\]

Representations on this grid are unique. Use the same formula for the
finitely many lower exponents required below. Since `5s+j-i=3`, the
three upper targets have comparison values

\[
F(M/4)=2^{-10/3}F(M),\qquad
F(M')=2F(M),\qquad F(M'/2)=2^{1-5/3}F(M).                 \tag{3}
\]

Any of these target points with exponent below 3 is strictly below 96:
`M/4` at such exponents is at most 84, and `M'/2` at exponent 2 is
either 72 or 84. Every odd seed below 96 has been verified to terminate.
Consequently its `B` value is zero, so it causes no boundary error.

The function `F(M)` is bounded above and below by fixed positive multiples
of `M^(5/3)` on the five-ray grid. Thus `B(M)/F(M)->0` as `M` tends to
infinity through the grid. If any exceptional seed exists, the ratio has
a positive global maximum `C` at some selected cutoff `M` (the grid is
unbounded and eventually includes any exceptional seed in its count).
For target points in the selected grid use `B<=CF`; at lower target
points use `B=0<=CF`. Equations (1)--(3) and monotonicity give

\[
\begin{split}
CF(M)=B(M)&\le B(M/4-1)+\tfrac13B(3M/2)+\tfrac13B(3M/4)\\
&\le C\left[F(M/4)+\tfrac13F(M')+\tfrac13F(M'/2)\right]\\
&=CF(M)\left[2^{-10/3}+\tfrac23(1+2^{-5/3})\right].
\end{split}
\]

But `2^10=1024>1000=10^3` and `2^5=32>27=3^3`, so the bracket is

\[
\lambda_5=2^{-10/3}+\tfrac23(1+2^{-5/3})
<\tfrac1{10}+\tfrac23(1+\tfrac13)=\frac{89}{90}<1.
\]

This contradicts positivity of `CF(M)`. Conversely, Collatz gives finite
absorption of every packet and hence an exact finite current, as in the
main reduction. QED.

**Thirty initial cutoffs for multiplication-by-64 induction.** Write
`b=r+6k` with `r=3,...,8`. The five rays split into exactly 30 sequences
`N_k=a_i2^r64^k`. Their initial cutoffs are distinct, and the largest is
`21*2^8=5376`. Every packet endpoint at an initial cutoff is below 12096:
an odd source is at most `3N/2-1`, so its one-step endpoint is at most
`(3(3N/2-1)+1)/2=9N/4-1<=12095`.

The companion script verifies convergence of every odd seed below 12096
as part of its larger finite base check. There are 6048 such odd seeds,
all absorbed within 98 odd-only steps. Therefore exact currents exist
for all 30 initial packets by finite absorption: one may take
`J_N=sum_(j=0)^97 P^j Pi_N`. This establishes existence for these initial
cutoffs. **Thirty full current tables are not stored by this audit.**

The annular increment identities and any proposed inductive construction
are separate results. Universal certificates for the unbounded exponent
remain unproved. The five-ray theorem reduces the required family; it
does not supply those certificates or their termination argument.

## 3. General mesh maximum principle for the alternative criteria

**Lemma.** Let `p>1`, `U>=8`, and let `G` be an unbounded set of integer
cutoffs divisible by 4. Suppose:

1. every positive odd seed below `U` reaches 1;
2. for every integer `n>=U` there is `M in G` satisfying `n<=M<=alpha*n`;
3. `alpha^p lambda(p)<1`, where

\[
\lambda(p)=4^{-p}+\tfrac13(3/2)^p+\tfrac13(3/4)^p;
\]

4. `d_M<=0` for every `M in G`.

Then every positive integer reaches 1.

**Proof.** At a selected cutoff `M`, divisibility by 4 gives the exact cutoffs

\[
n_0=M/4-1,\quad n_1=3M/2,\quad n_2=3M/4.
\]

Therefore `L(n^p)(M)<lambda(p) M^p`. Also `B(n)<=n`, so
`B(n)/n^p -> 0`. If an exceptional seed exists, this ratio attains a positive
global maximum `C` at some integer `n>=U`. Choose `M` as in hypothesis 2.
By monotonicity of `B`, equation (1), and the definition of `C`,

\[
C n^p=B(n)\le B(M)\le(\mathcal LB)(M)
\le C(\mathcal L(n^p))(M)
<C\lambda(p)M^p\le C\lambda(p)\alpha^p n^p<Cn^p.
\]

This contradiction proves the lemma. Initial powers of 2 reduce the even
case to the odd case. Every comparison uses the same odd-only clock. QED.

## 4. Twenty-one-ray alternative

Let

\[
\begin{split}
A=\{&8192,8467,8751,9045,9348,9662,9986,10321,10668,11026,11396,\
    &11778,12173,12582,13004,13440,13891,14358,14839,15337,15852\}.
\end{split}
\]

Define

\[
G_{21}=\{a2^b:a\in A,\ b\in\mathbb Z,\ b\ge3\}.
\]

**Theorem.** Each of the following is equivalent to Collatz:

- for every `M in G_21`, the packet work `H_L(Pi_M)` is bounded above over
  all integer horizons `L>=0`;
- for every `M in G_21`, there is a finite exact current for `Pi_M`;
- for every `M in G_21`, there is a finite current whose residual is
  everywhere nonpositive.

No bound on the size, running time, or cost uniform in `M` is assumed.
There are 21 cutoffs in each multiplicative interval
`[8192*2^b,16384*2^b)`.

**Proof of the arithmetic constants.** Include the wraparound successor
`16384=2*8192` after the final mantissa `15852`. The maximum of the 21
successive ratios is the interior ratio

\[
\max_{0\le i<21}\frac{a_{i+1}}{a_i}
=\frac{10668}{10321}
<\alpha:=\frac{10337}{10000},\qquad a_{21}=16384.       \tag{4}
\]

This is a finite set of exact rational inequalities, reproduced by the
companion script. For an arbitrary integer `n>=65536`, take
`b=floor(log2 n)-13` and choose the least `a*2^b>=n` with `a in A`;
if no such mantissa exists, choose `8192*2^(b+1)`.
Here `b>=3`. The chosen cutoff is the least `M in G_21` above `n`, and
equation (4) implies `n<=M<=alpha*n`. The integer implementation uses the
bit length of `n`, so this construction requires no floating arithmetic.

Take `p=7/5`. Put

\[
t_1=\alpha/4,\quad t_2=3\alpha/2,\quad t_3=3\alpha/4,
\qquad
(r_1,r_2,r_3)=\frac1{10000}(5821,11918,9032).
\]

The three exact rational inequalities `t_i^2<r_i^5` imply
`t_i^(7/5)=t_i (t_i^2)^(1/5)<t_i r_i`. Hence

\[
\alpha^{7/5}\lambda(7/5)
=t_1^{7/5}+\tfrac13t_2^{7/5}+\tfrac13t_3^{7/5}
<t_1r_1+\tfrac13t_2r_2+\tfrac13t_3r_3
=\frac{399928193}{400000000}<1.                       \tag{5}
\]

The finite base consists of every odd seed below 65536. The companion
script verifies all 32768 such seeds by exact Syracuse iteration, with
cycle detection and a 10000-step cap. All reached 1; the largest observed
hitting time was 125, uniquely at seed 52527. This finite base check is a
computational certificate, separate from the universal argument.

Each of the three stated current/work hypotheses implies `d_M<=0` exactly
as in the main proof note. The mesh lemma, equations (4)--(5), and the
verified finite base therefore imply Collatz. Conversely, under Collatz
every finite packet is eventually absorbed and has a finite exact current;
an exact current is also a current with nonpositive residual and gives a
finite work bound. QED.

**Alternative construction consequence.** This theorem alone reduces the
universal constructor to the 21 fixed integer mantissas in `A`, with exponent
`b>=3`. Splitting `b=r+6k`, `r=3,...,8`, gives 126 fixed sequences under
multiplication of the cutoff by 64. This is a reduction of the family of
required cutoffs. It is still an infinite universal existence/termination
obligation. Finite certificates at some exponents do not establish it.

## 5. A simpler thirty-ray alternative

Set `G_30={m*2^b:30<=m<=59, b>=2}`. Its base is 120 and its mesh ratio
is `31/30`. Take `p=4/3`. If

\[
(u_1,u_2,u_3)=(31/120,31/20,31/40),\quad
(s_1,s_2,s_3)=(6369,11573,9186)/10000,
\]

the exact inequalities `u_i<s_i^3` give

\[
(31/30)^{4/3}\lambda(4/3)
<u_1s_1+\tfrac13u_2s_2+\tfrac13u_3s_3
=\frac{1199731}{1200000}<1.
\]

The same mesh lemma proves the three equivalent current/work criteria on
`G_30`. The verified finite base contains the odd seeds below 120, with
largest odd-only hitting time 43. This alternative has simpler mantissas
and a smaller finite base; the 21-ray result has fewer required families.
No optimality assertion about the number 21 is made.

## 6. Subunit defects and their exact scope

For any finite signed integer measure `mu`, its work is eventually affine:

\[
H_L(\mu)=L\langle e,\mu\rangle
 +\sum_{x:\tau(x)<\infty}\mu(x)\tau(x)
\]

once `L` exceeds the finitely many finite hitting times in its support.
Thus its limiting slope exists and is an integer. In particular, any of
the equivalent hypotheses above can be replaced by

\[
\limsup_{L\to\infty}\frac{H_L(\Pi_M)}L<1
\qquad\text{for every selected cutoff }M.              \tag{6}
\]

The strict bound may depend on `M`; there is no uniform margin below 1.
Integrality makes equation (6) equivalent to `d_M<=0`, which is equivalent
to boundedness above for this finitely supported packet. It is therefore
an alternative formulation rather than a weaker existence statement.

One certificate version permits **finite rational** currents and residuals
`Pi_M=(I-P)J_M+zeta_M` satisfying `||zeta_M^+||_1<1`. Invariance of `e`
annihilates the divergence and gives
`d_M=<e,zeta_M><1`, hence `d_M<=0`. This extension explicitly enlarges the
coefficient domain to the rationals. With integer residuals, subunit
positive mass simply means the residual is everywhere nonpositive.

The strict inequality is essential to this integrality argument. A budget
of one unresolved positive unit can leave `d_M=1`. Bounds such as
`||zeta_M^+||_1=o(M)` or a small percentage of total source mass need not
be below one and do not establish equation (6).

For completeness, a quantitative defect estimate follows from the same
proof. Let `d_M<=c_M` on a mesh with exponent `p`, ratio `alpha`, and
`q=alpha^p lambda(p)<1`. Assume `c_M>=0` and put

\[
D=\sup_{M\in G}\frac{c_M}{M^p}.
\]

After the same terminating finite base, the maximum-principle calculation
gives

\[
\sup_{n\ge1}\frac{B(n)}{n^p}
\le\frac{\alpha^pD}{3(1-q)}.                          \tag{7}
\]

Indeed, at a positive maximizer `n` and its next selected cutoff `M`,
`B(n)<=L B(M)+c_M/3`, and dividing by `n^p` proves equation (7).
A positive right-hand side controls this weighted exceptional count; it
does not prove that it vanishes.

## 7. Arbitrarily sparse arithmetic pairs for exact currents

This separate criterion permits exact currents only. Fix any integer
`d>=1`. For every integer `j>=0`, set

\[
N_j=2\cdot3^{d-1}(2j+1).
\]

Suppose exact finite currents exist at both `N_j` and `N_j-1` whenever
both cutoffs are at least 8. Then Collatz follows. These selected pairs
have asymptotic density `1/(2*3^(d-1))` among the integer cutoffs.

**Proof.** Each `N_j` is `2 mod 4`. For any `N=4k+2`, the second source
cutoff is unchanged from `N-1`, while the first adds only the odd state
`r=3N/2=6k+3`, with coefficient `-1`. Thus the exact source identity is

\[
\nu_N-\nu_{N-1}=-\delta_{3N/2}.                        \tag{8}
\]

Finite divergences pair to zero with `e`, and the core remainder also
pairs to zero. Subtracting the two exact-current identities therefore
gives `e(3N/2)=0`. Hence every odd multiple of `3^d` terminates. The only
possible omitted small multiples are 3 and 9, already verified to terminate.

Every odd `y` coprime to 3 has an odd inverse Syracuse lift divisible by
`3^d`. To see this, 2 has order `2*3^d` modulo `3^(d+1)`. An elementary
proof is the identity
`v_3(2^(2*3^k)-1)=k+1`: it holds at `k=0`, and if `z=1+3^r u` with
`3` not dividing `u`, then `v_3(z^3-1)=r+1` by expansion, for `r>=1`.
Euler's theorem and the even order modulo 3 then show that the order is
exactly `2*3^d`, the number of units of the modulus. Consequently there
is an exponent `1<=a<=2*3^d` for which `2^a y=1 mod 3^(d+1)`. The number

\[
x=(2^a y-1)/3
\]

is positive, odd, divisible by `3^d`, and satisfies `S(x)=y` with exact
valuation `a`. Its convergence forces convergence of `y`. An odd multiple
of 3 has a successor coprime to 3, completing the argument. QED.

**Limitation.** Subtracting two upper bounds, or two current identities
with nonpositive residuals, does not retain a nonpositive residual.
Equation (8) therefore does not justify this sparse arithmetic criterion
for one-sided currents. It also explains how exact paired certificates
already encode convergence of an arithmetic progression of individual
seeds; this sparsification alone supplies no constructor.

## 8. Reproduction and proof boundary

Run from the repository root, without Python optimization:

```sh
python3 experiments/current_construction/frontier/check_sparse_criteria.py
```

The script regenerates `sparse_criteria_audit.json`. It checks the five-ray
arithmetic transitions and strict `89/90` comparison, the complete
finite base below 65536 (covering the five-ray base and all 30 initial
packet supports), the exact rational power bounds, all repeating
mantissa gap ratios, 3905 selected grid boundary probes through exponent
64, the 30-ray constants, 249 source differences at `N=10,14,...,1002`,
and 1665 modular inverse lifts for `d=1,...,5` and odd `y<=999` coprime to 3.
The 21-ray constant bound and grid comparison also received a separate
exact rational arithmetic audit by another research agent. The five-ray
argument was independently checked by the parent research agent.

The general mesh and inverse-lift claims rest on the written arguments.
The finite experiments do not prove universal current existence. None
of these notes has received human peer review or formal verification.
