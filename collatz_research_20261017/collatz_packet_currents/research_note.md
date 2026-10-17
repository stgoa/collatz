# Exact-source packets and cancellation across unequal arrival times

## Status and main distinction

This note proves two elementary general results and supplies finite all-horizon certificates for a set of explicitly specified source cutoffs.

1. The uploaded packet reduction can be reconstructed directly from exact positive source cylinders. No homogeneous approximation or residue-profile table is needed. The remainder bound improves to
   \[
   6\binom bd+2\sum_{j<d}\binom bj.
   \]
2. Signed stopping work can be bounded by a finite table of weights on one-step Syracuse arrows. The table cancels contributions that visit the same integer at different elapsed times, not only contributions meeting simultaneously. A further finite exit-profile calculation uses those time differences to sharpen the bound.

For fourteen finite source cutoffs, such tables were constructed and their identities checked. Two of the complete tables are included and independently checked by a C++ program. Their bounds hold for **every future time horizon**, not just the finite times observed in an orbit scan.

**No bound uniform in the source cutoff is proved.** The finite table construction can require following unresolved trajectories; its successful termination on these examples is not an all-input theorem. The current-size/cost bounds are not inferred from the finite sample. Collatz and the programme's mean stopping-work target remain unproved. There is no Lean verification, independent human review, or publication-priority claim.

The telescoping identity used here is an elementary coboundary identity for a deterministic map. The new items being investigated are its exact-source packet application, the finite certificates, and whether their costs can be bounded arithmetically. Standard finite parity-cylinder theory is acknowledged in [1]; no analytic theorem from [2] is needed below.

## 1. Setting

Let
\[
 S(x)=\frac{3x+1}{2^{v_2(3x+1)}}
\]
on the positive odd integers. Thus S(1)=1. Let P push a finite signed integer measure through S and kill all contributions reaching 1. Write
\[
 \|\mu\|_1=\sum_{y>1}|\mu(y)|,
 \qquad \|P\mu\|_1\le\|\mu\|_1.
\]

For every integer N>=8 put
\[
 n_1=\lfloor(3N+1)/2\rfloor,\qquad n_2=\lfloor(3N+1)/4\rfloor,
\]
\[
 \nu_N(x)=1_{x\le n_1}(3\,1_{x\equiv5\pmod6}-1)
          +1_{x\le n_2}(3\,1_{x\equiv1\pmod6}-1),
 \quad x>1\text{ odd}.
\]
Each combined source weight has absolute value at most 2. The signed total has absolute value at most 8.

Let tau(x) be the first Syracuse hitting time of 1, possibly infinity, and set
\[
 h_L(x)=\min\{L,\tau(x)\},\qquad h_L(1)=0.
\]
For every finite signed measure,
\[
 H_L(\mu):=\langle\mu,h_L\rangle
 =\sum_{j=0}^{L-1}\langle1,P^j\mu\rangle.                 \tag{1.1}
\]
This is a finite identity, with no convergence assumption. The discrepancy in the uploaded programme obeys
\[
 3\mathcal E_T(N)=H_T(\nu_N).                             \tag{1.2}
\]

## 2. A source-exact packet construction

### 2.1 Finite cylinders

For a positive length-d valuation word w=(a_1,...,a_d), let A=sum a_i and
\[
 C_w=\sum_{j=0}^{d-1}3^{d-1-j}2^{a_1+\cdots+a_j}.
\]
Its exact positive sources and endpoints are
\[
 x_t=q_w+2^{A+1}t,\qquad
 y_t=e_w+2\cdot3^dt,\qquad t\ge0,                       \tag{2.1}
\]
where q_w is the least positive residue satisfying
\[
 3^dq_w+C_w\equiv2^A\pmod{2^{A+1}},
 \qquad e_w=(3^dq_w+C_w)/2^A.
\]
Both q_w and e_w are positive odd integers. The terminal congruence gives exact odd valuations throughout by the standard backward oddness/divisibility induction.

We exclude source 1 and any endpoint equal to 1. The admissible t start at
\[
 t_0=\begin{cases}0,&q_w>1\text{ and }e_w>1,\\1,&\text{otherwise}.\end{cases}
\]
For source component i, the remaining indices are a consecutive interval
\[
 t_0\le t\le\left\lfloor\frac{n_i-q_w}{2^{A+1}}\right\rfloor. \tag{2.2}
\]
If an intermediate iterate had reached 1, the endpoint would be 1 as well, since S(1)=1. Thus no absorbed source is being silently retained.

### 2.2 Group consecutive source lifts in threes

Split nu_N into its two source components with weights
\[
 w_1(c)=3\,1_{c=2}-1,\qquad
 w_2(c)=3\,1_{c=1}-1,
 \quad c\pmod3.
\]
Because 2^(A+1) is a unit modulo3, each consecutive triple t,t+1,t+2 in (2.2) contains each source residue modulo3 once. Its three weights are a permutation of (2,-1,-1), so they sum to zero. Its endpoint spacing is exactly 2*3^d.

Starting at t_0, retain as many consecutive triples as fit. At most two source lifts remain at the right endpoint of (2.2). Their combined absolute weight is at most 3: two consecutive terms of the cyclic weight pattern have absolute sum at most 3. With two components, the discarded weight is at most 6 per word.

Let \(\widehat\Pi_{d,N}\) be the sum of all these exact image packets for words with A<=b, where b=ceil(log2 N). Packets from different words or components may overlap. Their weights are added, never interpreted as probabilities. Each raw packet has the form
\[
 c_0\delta_y+c_1\delta_{y+2\cdot3^d}
                +c_2\delta_{y+4\cdot3^d},
 \quad c_0+c_1+c_2=0.                                  \tag{2.3}
\]

This family is generally different from the uploaded complete homogeneous-cell family Pi_(d,N). The hat distinguishes it. It keeps the exact ancestral valuation word and source interval of every raw packet.

### Theorem 2.1: exact decomposition and improved remainder

For every N>=8 and 1<=d<=b/2,
\[
 P^d\nu_N=\widehat\Pi_{d,N}+\widehat\eta_{d,N},
\]
with
\[
 \boxed{\|\widehat\eta_{d,N}\|_1
 \le D^*_{b,d}:=6\binom bd+2\sum_{j=0}^{d-1}\binom bj.}  \tag{2.4}
\]

**Proof.** There are binom(b,d) positive words of length d and total A<=b. The endpoint remnants from their two source intervals cost at most 6 per word, as just proved.

Among all odd residues modulo2^(b+1), the number whose first d valuation sum exceeds b is exactly sum_(j<d) binom(b,j). Indeed the complementary count is
\[
 \sum_{A=d}^b\binom{A-1}{d-1}2^{b-A}
 =\sum_{j=d}^b\binom bj.
\]
The support of nu_N is strictly below2^(b+1), and its combined coefficients have absolute value at most2. Hence the over-budget image has norm at most twice that exceptional-class count. Summing gives (2.4). QED.

No affine endpoint is approximated in this proof. The two error types are precisely the ungrouped source lifts and the over-budget source classes.

### Corollary 2.2: source-power reduction

For N>=512 set m=floor(2b/9). Then
\[
 \boxed{\|\widehat\eta_{m,N}\|_1\le16N^{7/9}.}            \tag{2.5}
\]
The constant is convenient, not claimed sharp. Use
\[
 D^*_{b,m}\le8\sum_{j=0}^m\binom bj,
 \quad H_2(2/9)<7/9,
 \quad 8^9 2^7<16^9.
\]
The entropy inequality follows from 9^9<2^9 7^7. Thus the remainder costs at most
\[
 16T N^{7/9}
\]
under all its subsequent exact iterates, without any termination assertion.

Because every packet has zero signed total, the same construction at all d<=m and monotonicity of D^*_(b,d) imply
\[
 \boxed{
 \left|3\mathcal E_T(N)-H_{(T-m)_+}(\widehat\Pi_{m,N})\right|
 \le T D^*_{b,m}.
 }                                                       \tag{2.6}
\]
The initial signed total is bounded by8<=D^*_(b,m). No early contribution is omitted.

For T<=ceil((b+1)N^(1/5)), equation (2.6) is bounded by
\[
 16(b+2)N^{44/45}=o(N).
\]
This improves the previous remainder, but it does NOT bound the retained packet work.

Exact binomial evaluations of the error bound divided by N, using the integer horizon upper bound (b+1)2^ceil(b/5), are approximately 9.289933, 2.327205, 0.103422, 0.000256211 and 1.1050e-9 at b=64,128,256,512,1024. These are certified finite expressions, not experiments with sources of those sizes.

## 3. Cancellation need not happen at equal elapsed times

### Proposition 3.1: common-tail lag formula

Suppose positive odd sources x_i, with signed coefficients c_i summing to zero, reach the same positive odd state z after verified path lengths d_i, without an earlier visit to1. A source may itself be z, with d_i=0. Put
\[
 \Phi(u)=\sum_i c_i\min(u,d_i),\qquad u\ge0.
\]
For every L>=0,
\[
 \boxed{\sum_i c_i h_L(x_i)
 =\Phi((L-\tau(z))_+).}                                 \tag{3.1}
\]
If tau(z)=infinity, the right side is defined as Phi(0)=0.

**Proof.** If tau(z) is finite, tau(x_i)=d_i+tau(z). For L<=tau(z) each term h_L(x_i)=L and the weighted sum is zero. Otherwise subtract the common tau(z) from min(L,d_i+tau(z)) and use sum c_i=0. If tau(z)=infinity, all sources have h_L=L and again cancel. QED.

Phi is piecewise linear and constant after max d_i. Its extrema occur among 0 and the finitely many d_i. Therefore verified finite paths to z give a bound for every future horizon, without following the orbit after z or assuming that it converges.

### An earlier difficult packet is nonpositive at every horizon

The uploaded packet
\[
 -\delta_{6929}-\delta_{6947}+2\delta_{6965}
\]
has a common meeting state23. Its arrival times are49,32,3. Hence
\[
 \Phi(u)=-\min(u,49)-\min(u,32)+2\min(u,3),
\]
and
\[
 \boxed{-75\le H_L(\mu)\le0\quad\text{for every }L.}      \tag{3.2}
\]
The 84 verified steps stop at23. No fact about the continuation from23 is needed for this deduction. This packet also occurs directly among the new source-exact packets: word (1,1), outer interval, lifts t=384,385,386 at N=4096.

Balance alone does not give the same sign for every packet. Another packet in the uploaded complete-cell family is
\[
 \delta_{55}+\delta_{73}-2\delta_{91}.
\]
Its sources reach91 at times8,9,0, so
\[
 \boxed{0\le H_L(\mu)\le17\quad\text{for every }L.}       \tag{3.3}
\]
It is used as a sign safeguard, not claimed to be one raw triple in the new grouping convention.

For the simplest illustration, if S(u)=z>1 then
\[
 0\le h_L(u)-h_L(z)\le1
\]
for all L. If z were to have a nonrepeating divergent orbit, the synchronous absolute mass of delta_u-delta_z would remain2 forever, while its signed stopping work would be zero. Therefore bounding total absolute residence can require much more than bounding the signed quantity actually needed.

## 4. Finite arrow-weight certificates

A finite signed table J on odd states >1 assigns J(y) to the arrow y->S(y). Call
\[
 \partial J=(I-P)J
\]
its signed divergence. This is a concrete finite identity to check, not an assumed solution of an infinite equation.

### Theorem 4.1: a current controls all future horizons

If a finite J satisfies mu=partial J, then for every integer L>=0,
\[
 \boxed{H_L(\mu)=\sum_y J(y)1_{\tau(y)\le L}.}            \tag{4.1}
\]
Consequently
\[
 -\|J^-\|_1\le H_L(\mu)\le\|J^+\|_1.                  \tag{4.2}
\]

**Proof.** Telescoping (1.1) gives H_L((I-P)J)=<1,J-P^LJ>. A source y contributes to P^LJ exactly when it has not yet hit1. This gives (4.1). Alternatively h_L(y)-h_L(Sy)=1_(tau(y)<=L), with h_L(1)=0. QED.

No assertion that all sources in supp J converge is needed. A certificate verifier computes S(y) once for each row, adds J(y) at y, subtracts J(y) at S(y)>1, and compares with mu. Thus a finite verified identity supplies an all-horizon conclusion.

This is an elementary coboundary/telescoping principle. It is not presented as a newly discovered general theorem. Its relevance here is that it preserves cancellations between different elapsed times, which the norm sum sum_j ||P^j mu|| would discard.

### Remainder version and one-sided cost

If
\[
 \mu=(I-P)J+\zeta,
\]
then
\[
 H_L(\mu)\le\|J^+\|_1+L\|\zeta^+\|_1.                 \tag{4.3}
\]
A negative residual requires no cost for an upper bound. This is strictly a signed upper-bound statement, not a claim that all residual absolute mass disappears.

## 5. Sharper bounds from exit profiles

Suppose the directed graph of states in supp J contains no cycle. Follow each y in supp J until its first exit z from supp J, and let d(y) be that path length. The exit may be1. All intervening states are explicitly in the finite table.

For each exit z define integer coefficients
\[
 v_z(k)=\sum_{\substack{y\in\operatorname{supp}J\\z(y)=z,\ d(y)=k}}J(y),
\]
and their cumulative profile
\[
 F_z(u)=\sum_{k\le u}v_z(k),\qquad u\ge0.
\]
Let U_z=max(0,max_u F_z(u)) and L_z=min(0,min_u F_z(u)). The maxima and minima need only the finitely many occurring integer levels.

### Theorem 5.1: exit-profile certificate

For mu=partial J,
\[
 \boxed{H_L(\mu)=\sum_z F_z((L-\tau(z))_+),}              \tag{5.1}
\]
with the zero interpretation for tau(z)=infinity. Thus
\[
 \boxed{\sum_z L_z\le H_L(\mu)\le\sum_z U_z.}            \tag{5.2}
\]
The upper cost C_+(J)=sum U_z is at most ||J^+||_1, and the lower cost is no worse than -||J^-||_1.

**Proof.** Before exit z the path contains no1, so tau(y)=d(y)+tau(z), also when the latter is infinite. Substitute this into (4.1), group by exit and distance, and then bound each resulting finite cumulative profile. QED.

This does not assume the different exits have independent continuations. The separate extrema give a safe bound even though those continuations can be correlated. Nor is the sum-of-extrema bound claimed sharp for the actual map.

The acyclicity condition concerns the finite current support and is itself checked. If a verified nontrivial cycle were present there, its contributions would require separate handling. No nontrivial cycle is assumed absent as an external fact.

## 6. Concrete current certificates

The source-exact packets were constructed for the ten dyadic cutoffs 2^9 through2^18 and for 513,999,4097,10001. For each, finite paths were explored to a small checked set and combined with signed weights. The construction aborts on an unresolved cycle or a path-cap exceedance; it is not presumed to terminate on arbitrary future inputs.

The resulting J was then verified solely by the one-step identity partial J=widehat Pi. This separates potentially expensive certificate discovery from simple certificate checking.

For example:

| N | Anchor m | Basic positive-current cost | Exit-profile lower bound | Exit-profile upper bound |
|---:|---:|---:|---:|---:|
| 4,096 | 2 | 4,352 | -1,406 | 2,364 |
| 16,384 | 3 | 15,256 | -3,957 | 4,085 |
| 65,536 | 3 | 58,599 | -16,698 | 6,902 |
| 262,144 | 4 | 226,776 | -57,661 | 63,824 |

Each bound applies to H_L(widehat Pi_(m,N)) for **every L>=0**. The source cutoffs are a finite list; no uniform-in-N estimate is inferred.

For N=262144 the exit-profile upper cost is less than N/4. The finite current has132998 nonzero rows and7045 exits. The verifier follows only the known edges inside this finite support to calculate its profiles. It need not continue the orbit from those exits to apply Theorem5.1.

The full construction was found using verified finite paths, often through a small core. We do not pretend those paths were available from a closed symbolic formula. Producing similar tables at all scales with a uniform cost bound is the outstanding mathematical problem.

### Complete finite-source error certificates

For the two included current tables, the anchor residual and the early signed totals were also computed exactly. Combine them with Theorem5.1 and pay the anchor residual at its maximum possible contribution; it need not be followed after the anchor.

At N=4096, m=2, the exact target horizon ceil(13*4096^(1/5)) is69. The early signed totals are -1,1, and the residual has positive/negative norms22,20. For every0<=T<=69,
\[
 -2746/3\le\mathcal E_T(4096)\le3838/3.
\]

At N=262144, m=4, the target horizon is231. The early signed totals are -1,1,1,2, and the residual has positive/negative norms209,202. For every0<=T<=231,
\[
 \boxed{-34504\le\mathcal E_T(262144)\le37090.}            \tag{6.1}
\]
These are proof certificates for named finite source cutoffs. They are not an asymptotic bound, a new convergence-verification record, or a trajectory scan through gigantic source values.

## 7. What a uniform extension would require

Let m=floor(2 ceil(log2 N)/9). If one could construct finite currents J_N satisfying
\[
 \widehat\Pi_{m,N}=(I-P)J_N,
 \qquad \mathcal C_+(J_N)=O(N),                           \tag{7.1}
\]
then (2.6) and (5.2) would give the one-sided O(N) discrepancy estimate on the programme's source-power time window.

A weaker, incomplete-current version would suffice:
\[
 \widehat\Pi_{m,N}=(I-P)J_N+\zeta_N,
\]
with
\[
 \mathcal C_+(J_N)=O(N),\qquad
 \|\zeta_N^+\|_1=O(N^{4/5}/\log N).                     \tag{7.2}
\]
No estimate on the negative residual is needed for that upper bound.

**Neither (7.1) nor (7.2) is proved uniformly.** These formulations specify what the finite certificate demonstrates on its named instances; introducing them is not counted as a solution of the missing estimate. A larger list of successful certificates cannot establish their asymptotic validity.

The new useful distinction is that the unknown future absorption time can be eliminated once finite relative arrivals or a finite arrow-weight identity are known. It is not necessary to bound every trajectory's future duration separately. Conversely, mere balance, sparse support, or a small synchronous norm does not guarantee a cheap current.

## 8. Verification and literature boundaries

- The uploaded packet certificate was extracted and rerun unchanged. Its finite assertions passed. No inherited analytic gamma-decay theorem is used in this note.
- The new Python programme verifies 5931 finite word constructions, 199560 zero-sum source triples, and1394084 actual prefix steps. It checks current identities at295058 nonzero current states across the named examples.
- Three finite common-tail witnesses are replayed only to their meeting states. The lag formula is tested against arbitrary hypothetical remaining delays, including infinity; these tests do not claim such alternative fates for the actual roots.
- A C++ verifier reconstructs the entire packet measures at N=4096 and N=262144 by direct iteration and grouping of source histories, without modular source inversion or the Python word-composition routine. It then checks every row of the stored current by one-step arithmetic and computes every exit profile by direct path following, without Python's memoized exit labels.
- The C++ reconstruction uses792570 prefix steps. It checks135734 current rows and3593975 within-support graph steps. All reported bounds, residual norms and finite-window endpoints agree.
- The decisive calculations use integers or exact fractions. Displayed decimal ratios are not proof inputs.

The current identity and lag formula are elementary deterministic-potential arguments, not a claim of a new general theory. Their Collatz application must still be compared with the literature. The finite exact-cylinder framework is classical [1]. Tao's transport analysis [2] is important context for why one cannot replace a pushed source distribution by independent random values, but no theorem from that paper is needed for the results above.

### References

[1] D. J. Bernstein and J. C. Lagarias, *The 3x+1 Conjugacy Map*, Canadian Journal of Mathematics48 (1996),1154--1169. https://websites.umich.edu/~lagarias/doc/bernstein.pdf

[2] T. Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi10 (2022),e12; arXiv:1909.03562. https://arxiv.org/abs/1909.03562

[3] Uploaded *A balanced-ternary-packet reduction on the source-power time window*. Its old homogeneous-cell packet family is not identified with the new source-exact family. The uploaded finite certificate was rerun; its whole historical proof corpus is not being newly certified here.
