# V003 — Independent algebra and scope review

**Status: independent written review, 2026-10-18.** The elementary proofs
below pass at their stated scopes. This is not human peer review, formal
verification, an exhaustive literature review, or a proof of the full
binary-automatic invariant-coloring classification. No novelty is asserted.
The carry calculation was produced by this reviewer and separately
spot-checked by the coordinating agent; the kernel, cylinder, digit-count
and scaling arguments were independently rederived from other authors'
notes. The executable companion's carry and cycle/control checks were
reviewed independently, and its default receipt replay passed. Those finite
checks remain separate evidence from the written proofs.

## 1. Scope of each conclusion

| Note | Conclusion checked | What it does not supply |
|---|---|---|
| [Kernel probe](kernel_probe.md) | Both nonzero ternary sections are binary sections; the first ternary image of the whole finite binary kernel adds at most one function; the pure-zero ternary orbit is finite | Full closure under arbitrary mixed ternary words, or automaticity of an actual bad set |
| [Digit count](digit_sum.md) | Every invariant of the form F(s_2(n)) is constant, for an arbitrary color set and arbitrary F on positive digit counts | Classification of automata sensitive to bit positions, order or patterns |
| [Cylinder rigidity](cylinder_rigidity.md) | One eventually monochromatic dyadic residue class forces constancy, for fixed positive odd d coprime to3 | Existence of such a class for every automatic invariant; the stronger arbitrary-modulus d=1 statement for all d |
| [Literature L6](literature.md#l6-two-scaling-invariances-do-not-imply-periodicity) | Binary automaticity and invariance under doubling/tripling can coexist with infinitely many distinct mixed ternary sections | A counterexample satisfying the guarded Collatz identity or the kernel probe's full hypotheses |
| [Carry boundary](carry_boundary.md) | One complete integer conversion/carry patch, with exact tails, bootstrap and clocks | A new section relation, a finite bound on all frontier descriptions, or a generalized d=5 tile model |

The full class of finite-valued binary-automatic component invariants at
d=1 remains unclassified here. Proving that restricted class constant would
still not prove that a hypothetical nonabsorbing-set indicator belongs to it.

## 2. Kernel proof: domains and independent calculation

All coloring equations initially concern positive integers. The extension
h(0)=h(1) is bookkeeping for standard kernels, not an extra dynamical state.
At d=1, the omitted odd-source equation at1 is already a value equality:
h(4)=h(1) follows from doubling twice. Thus each exceptional n=0 occurrence
in the section formulas is valid without an outgoing absorbed arrow.

The two identities follow from

\[
 3(4m+1)+1=4(3m+1),\qquad
 3(2m+1)+1=2(3m+2).
\]

For g(n)=h(2^a n+r), its j-th ternary section has offset
c=2^a j+r in [0,3*2^a). If c is a ternary unit, the selected v in {1,2}
makes t=(2^v c-1)/3 a **positive odd** integer below 2^(a+v).
The odd input x=2^(a+v)n+t then satisfies

\[
 3x+1=2^v(3\cdot2^a n+c).
\]

Removing those v factors of2 is valid for colors even when additional
factors remain; v is not being misreported as an exact Syracuse valuation.
If 3 divides c, the section is a binary section of f_1(n)=h(3n).
The relations f_1(2n)=f_1(n) and f_1(2n+1)=h(32n+17) prove the stated
membership in K union {f_1}, including a=0 and c=0.

For f_t(n)=h(3^t n), the independently checked odd section is

\[
 f_t(2n+1)=h(2^{2t+3}n+2^{2t+2}+1).
\]

Its offset is within its binary modulus. Doubling invariance determines
f_t at every positive n from this odd section, and all f_t have the same
value at0. Thus the map from these functions to their odd sections is
injective and their number is at most |K|. Eventual periodicity here is
in the index t of a sequence of **functions**, not in the integer argument
of h.

The final mixed-pair equations also check. With
b_t(n)=f_t(2n+1), u_t(n)=f_t(3n+1), v_t(n)=f_t(3n+2), their binary sections
are respectively

\[
 (T_0b_t,v_t),\qquad (u_t,T_2b_t).
\]

This is a valid binary presentation. The proof correctly does not reapply
its first-image theorem to newly added functions as though they were
members of the original K. The conditional implication f_1 in K ⇒ full
ternary closure ⇒ constancy uses the published Cobham input; its first
premise has not been proved.

## 3. Partial classifications

**Digit count.** For k>=2, the two blocks of
n_k=32(2^k-1)+9 have weights k and2. In
3n_k+1=32(3*2^k-3)+28, the upper coefficient has k one-bits and the lower
block has3. This proves F(k+2)=F(k+3) for all k>=2. The exact sources
5,13,23 connect weights2→1,3→2,4→3. The proof never uses weight0.
The additional nonperiodicity argument for Thue–Morse uses positive inputs
2^L-M and the identity s_2(2^L-M)=L-s_2(M-1), with 2^L>M.

**Cylinder rigidity.** The K-bit shortcut parity word has affine intercept
b=d*sum_i 3^(j-i)2^(t_i). For j>0 its last summand is a ternary unit,
so b is invertible modulo3. Because2 generates the units modulo3^j,
the congruence 2^(K+s)a=b mod3^j has arbitrarily large solutions s.
The resulting n=(2^(K+s)a-b)/3^j lies in the original binary cylinder.
Taking n>2^K keeps every one of the first K states above1, after which
halvings reach a. The j=0 and K=0 cases are separate and valid.

Removing powers of2 and, when needed, taking one odd arrow gives every
color a positive odd representative coprime to3. This completes the
all-colors conclusion without silently restricting the target to a special
basin. The monochromatic class need only be constant beyond a finite
threshold, because the predecessor sources are arbitrarily large.
The reset-word consequence uses **most-significant-digit** reading and
appends the reset suffix to any positive prefix; it does not confuse that
automaton with a least-significant-digit kernel presentation.

## 4. Exact controls and the scoped barrier

For d=5 and61, h_d(n)=1_(d divides n) satisfies the full color equations.
Both are periodic and automatic. They have no monochromatic dyadic
cylinder, since each such class contains arbitrarily large multiples and
nonmultiples of d. They therefore do not contradict cylinder rigidity.
They do not factor through digit count: 3 and5 have equal weight2 but
different h_5 colors; 31 and61 have equal weight5 but different h_61 colors.

The d=1 section identity h(3m+1)=h(4m+1) fails for these controls already
at m=1 for d=5 and m=15 for d=61. The valid general-d version retains d:
h(3m+d)=h(4m+d), for m>=0. In particular one cannot transfer the d=1
periodic-rigidity conclusion unchanged. These colorings separate their
divisible sectors; they are not claimed to classify every nonprincipal
cycle basin.

The L6 character g(n)=chi(oddpart(n)) is an entirely different control.
It is invariant under multiplication by2 and3 and is binary-automatic,
but fails the actual odd arrow3→5. The proposed-period argument works
for every M=2^a m by selecting odd u with chi(u) different from chi(m)
and comparing 2^(a+k)u with that number plus M.

The pairwise separation of mixed sections is also exact. For t!=s,
Delta=3^t-3^s=2^a D can have either sign. Choosing K>a+3 and a sufficiently
large odd v by CRT gives a positive n=(2^K v-1)/3^t. The second odd part
is positive and D modulo8, while the first has color chi(v), chosen opposite
to chi(D). Pairwise separation also works at t=0, but the infinite
**canonical ternary-kernel** family uses t>=1: its offset1 must be strictly
below the modulus3^t. A fixed extension g(0)=+1 makes the usual n>=0
kernels explicit and leaves all these statements unchanged.

This establishes an actual counterexample to the **scaling-only** inference,
not merely a missing proof. It does not satisfy the guarded identities
needed for the kernel reduction. In particular it has constant binary
sections, such as g(8n+1)=+1.

## 5. Issues found and corrections

1. The carry note initially called both h(3n) and h(3n+1) missing. It now
   acknowledges the separately proved h(3n+1)=h(4n+1); its diagram adds no
   further relation.
2. Cylinder rigidity's final paragraph placed the L6 example next to the
   claim that automatic sequences may lack constant sections. That example
   has constant sections. The corrected paragraph uses Thue–Morse, whose
   sections are itself or its complement, for the latter claim. L6 retains
   its distinct role as the scaling/mixed-kernel counterexample.
3. The stale L6 link in that paragraph was corrected to its actual heading.
4. The L6 example now explicitly sets g(0)=g(1)=+1 for standard kernels.
   Its positive-domain proof does not depend on that convention.
5. The L6 canonical ternary-kernel family now starts at t=1, because
   offset1 is not a canonical residue at modulus3^0=1. The separation
   argument itself also permits t=0; its stronger indexing was unnecessary.

No algebraic correction was required in the kernel reduction, digit-count
classification, predecessor construction or L6 separation proof. Their
combination gives partial classifications, a narrower closure question and
a precise failed auxiliary inference. Full mixed-section closure and the
full binary-automatic invariant-coloring target remain open here.

## 6. Executable companion: reviewed coverage

The default invocation of [verify_examples.py](verify_examples.py) passed
against [verification.json](verification.json) without rewriting evidence.
Its receipt identifies the verifier's source hash and labels the result as
bounded exact arithmetic. This reviewer inspected the carry and cycle/control
functions in detail; the coordinating agent reviewed the other arithmetic
functions. A successful replay is not verification of every unbounded proof.

The carry check reproduces the complete 3-by-6 rectangle, three nonzero
column divisions and the subsequent zero-column rule, five horizontal
digit transitions and one zero-tail transition. It checks the lost-carry
counterexample, column values8,4,2,1, four shortcut arrows, one odd arrow
with valuation4, 17 exact low-bit cylinder samples and12 longer-prefix
ambiguity samples. The nonlocal bootstrap and entire infinite zero/undefined
boundary rays are **supplied boundary data**, as the receipt explicitly
states. No finite replay or parallel-update count is substituted for them.

The controls replay the actual d=5 cycle of length3 with total valuation5
and the d=61 cycle of length41 with total valuation66. Each has distinct
pre-return states, returns to its stated minimum, and avoids1. Additional
checks retain1 as absorber, distinguish the raw d=7 value at1, and confirm
the fixed points5 and61 in their respective maps.

For the two divisibility colorings the checker performs132 doubling/oddpart
comparisons, 66 absorbed odd-arrow comparisons and64 ordinary odd-source
comparisons. It separately exhibits the failed d=1 section transfers at
(d,m)=(5,1) and(61,15), and supplies252 CRT examples carrying both colors
inside the tested dyadic classes. These checks exercise the proved control
identities and their failed transfer; their finite ranges do not establish
the all-input statements independently of the written algebra.
