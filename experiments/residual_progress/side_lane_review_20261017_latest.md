# Review of the residual-cylinder and induction side feed

Date: 2026-10-17. Reviewed commit:
`9a0c28d90e1554cfa967e7e0ea785a86dd1af04c` on `origin/claude/sidekick`.
The parent fetched this commit. Files were read and materialized in a
temporary directory; the branch was not checked out or modified.

**Status: reproduced finite computations, written arithmetic deductions,
and scope corrections.** No global termination or novelty claim follows.
The receipt is
[side_lane_review_20261017_latest.json](side_lane_review_20261017_latest.json).

## 1. Assessment of the proposed pivot

The residual-root formulation supplies a precise strong-induction task:
given absorption through `N`, certify the remaining outer roots. The
tested cylinder rules prove finite valuation prefixes that descend below
`N`, or merge into the known absorbed set. These are useful partial
certificates, and their coverage can be measured exactly at fixed bit
depth. Completing every remaining root still has the full logical
strength of the missing convergence argument.

The new `--merge` rule tests a particular additional mechanism: merger
with the **one-step image** of the absorbed interval. It does not exhaust
all comparisons with already absorbed seeds, longer common-tail
identities, the new halving-coalescence construction, or arbitrary signed
annular block certificates. Its undecided fraction cannot exclude those
other mechanisms.

The productive next obligation is a rule covering every complementary
root, with a proved end to any growing recursion. More finite cylinder
counts quantify the remaining task; they do not establish that endpoint.

## 2. The residual-support identity is exact for every allowed cutoff

Let `8|N`, `N>=8`, and let `R_N` be the profile in
[R17's retained-graph construction](complement/RETAINED_GRAPH_EXTENSION.md).
Write `S` for the odd-only map, absorbed at 1. Then

\[
\operatorname{supp}R_N=
\{x\text{ odd}:N<x<3N/2,\ x\equiv3\pmod4,
\ x\notin S([1,N]_{\rm odd})\cup S^2([1,N]_{\rm odd})\}.
\tag{1}
\]

Here is a direct proof, beyond the feed's six finite cutoffs.

- If `3|x`, no odd Syracuse predecessor exists, so the climber remains.
- If `x=2 modulo3`, the predecessor `(2x-1)/3` is odd and below `N`,
  so the root is removed by one-step lookback.
- A remaining climber has `x=7 modulo12`. Its smallest odd predecessor
  is `p=(4x-1)/3>N`. All larger predecessors exceed `3N/2`, whereas
  a first iterate of a seed at most `N` is below `3N/2`. Thus a two-step
  lookback can only use `p`, and requires `x<9N/8`.
- In that sliver, `p=2 modulo3` exactly when `x=31 modulo36`. Then
  `q=(2p-1)/3=(8x-5)/9<N`, so `S^2(q)=x`. If `p=0 modulo3`, it has
  no predecessor; if `p=1 modulo3`, its smallest predecessor exceeds
  `N`. These are respectively the surviving classes `x=7,19 modulo36`.

The endpoint `9N/8` is a multiple of9, so it is never one of those
`7 modulo12` roots. This exhausts the possible one- and two-step histories
and gives exactly the persisted support formula.

This is an identity of **supports**. The coefficient-2 roots in `R_N`
represent two original shell atoms; the unweighted induction set does
not encode that multiplicity. In particular,

\[
|\operatorname{supp}R_N|=23N/288+O(1),\qquad
\|R_N\|_1=25N/288+O(1).
\]

The independent script's six rows reproduce exactly and agree with main's
`residual_profile`, including both coefficients and support:

| `N` | Support | Mass | Roots divisible by3 |
|---:|---:|---:|---:|
| 96 | 7 | 7 | 4 |
| 768 | 61 | 66 | 32 |
| 6144 | 490 | 532 | 256 |
| 9216 | 736 | 800 | 384 |
| 49152 | 3925 | 4266 | 2048 |
| 98304 | 7850 | 8532 | 4096 |

Roots divisible by3 have no incoming odd arrows at any lookback depth.
This fact permits their forward orbits to merge with already absorbed
paths; it does not prohibit coalescence or current certificates.

## 3. What the cylinder dynamic programs prove

Condition on `x=3 modulo4`, so the first valuation is 1. An exact prefix
of `j` valuations with total `A` requires `A+1` bits. Its iterate is

\[
S^j(x)=(3^j x+C)/2^A,\qquad C>0.
\]

The descent rule accepts a determined prefix if

\[
3^{j+1}<2^{A+1}.
\tag{2}
\]

For `x<3N/2`, this implies `S^j(x)<N` once
`N>C/(2^A-(3/2)3^j)`. Thus each accepted cylinder is valid for all
sufficiently large cutoffs. At fixed bit depth there are only finitely
many accepted prefixes, so one can take a common threshold.

The merger rule also accepts if the last valuation `a` is odd and at
least3, and `3^j<=2^A`. Equality is impossible for positive `j`, so again
there is a strict slope margin. For sufficiently large `N`, the resulting
state `y` is below `3N/2`. An odd final valuation gives `y=2 modulo3`.
Its odd predecessor `(2y-1)/3<N` has valuation1 and is already absorbed.
Hence `y`, and then the original root, are absorbed conditionally on
the supplied lower-interval current. This inference is sound.

Each new valuation `a` has relative cylinder measure `2^-a`; the unresolved
tail after the available bits is summed geometrically. The exact dynamic
programs therefore count the tested prefix rules using rational arithmetic.
An independent direct enumeration of all residues agrees with **both**
dynamic programs for every `2<=m<=14`. The external script originally
brute-checked only the descent version at `m=8,10,12,14`.

| Bits `m` | Undecided: descent | Undecided: descent or one-step merger |
|---:|---:|---:|
| 16 | 24.76196% | 21.16699% |
| 32 | 7.04307% | 5.75875% |
| 64 | 1.05513% | 0.84344% |
| 96 | 0.21408% | 0.16831% |
| 128 | 0.04842% | 0.03808% |

The receipt retains the exact fractions. The observed descent-rate fit
from 64 to128 bits is `0.9529917869` per bit, and the merger-rate fit is
`0.9527509520`. Their ratio at128 bits is about `0.78655`. These are
finite numerical summaries; no limiting rate or limiting ratio is proved.

The factor `3/2` in (2) certifies descent below the shell's lower cutoff.
Ordinary descent below the starting seed needs only `3^j<2^A`. Thus the
feed's phrase that these are *exactly* the usual undecided stopping-time
cylinders should be understood as a description of the method, not a
literal equality of the two acceptance predicates. The merger extension
adds a further predicate.

## 4. The positive fixed-bit remainder is real; N^0.93 is an extrapolation

For every fixed `m>=2`, the class `x=-1 modulo2^m` has all its determined
valuations equal to1. It is rejected by both tested rules. Conditional
on `x=3 modulo4`, it has measure `2^(-(m-2))`. Consequently their exact
undecided fractions satisfy

\[
d_{\rm merge}(m)\ge2^{-(m-2)}>0.
\]

The ternary restrictions defining `R_N` are independent of these binary
classes by the Chinese remainder theorem, after conditioning on the
already fixed residue modulo4. For **fixed** `m`, ordinary progression
counts therefore give

\[
\#\{\text{undecided roots}}
=\frac{23}{288}d(m)N+O_m(1).
\tag{3}
\]

Thus this finite-prefix procedure leaves a positive linear remainder
at any fixed bit depth. The statement does not cover every theorem
whose hypotheses happen to use a fixed residue modulus: such a theorem
could supply additional, unbounded orbit comparisons within that class.

The proposed `N^0.93` conclusion substitutes `m` near `log_2 N` into a
rate fitted between64 and128 bits. Three additional arguments would be
needed to turn that into a theorem:

1. Prove an asymptotic or a sufficient uniform bound for `d(m)`; two
   finite bit ranges do not determine its asymptotic rate.
2. Control residue counts in the moving interval when the modulus grows
   with `N`. The elementary fixed-modulus error in (3) can be of order
   `2^m`, which is order `N` in that regime and overwhelms `N^0.93`.
3. Control the affine constants `C` and the required cutoff thresholds
   uniformly over the growing family of accepted prefixes. Fixed-class
   sufficiently-large-`N` statements alone do not provide that control.

The stored field named `asymptotic_rate_per_bit` is therefore relabeled
in this review as a **finite64-to128-bit fit**. Neither `N^0.93`, a common
exponential rate, nor a constant-factor merger improvement is imported
as a theorem. The finite data remain useful measurements of these rules.

## 5. The negative-map connection in the fixed-h theorem

The feed correctly reproduces the fixed-h theorem's 54 positive orbit
states, 22 candidate triples, and the two nontrivial `3c-1` cycles.
We independently compared its literal tables with main's regenerated
finite barrier and checked every negative-map arrow.

Its narrative that the obstruction lasts while the auxiliary `c` values
"sit in the 3x-1 cycles" reverses the role of those cycles. In the proof,
an **actual** first-integer value `c_0` must reach1 under `T_-` by reversing
its already established finite inverse history. A hypothetical small
positive shadow would force `c_0` into one of the listed cycle basins
away from1. That is impossible. The cycles are exclusion certificates
for hypothetical low-shadow candidates; they are not the actual allowed
auxiliary histories protecting the component.

After first integer arrival, the affine coefficient `c` can be rational;
it should not be described as following an unrestricted integer cycle.
The full arbitrary-depth conclusion rests on
[the written fixed-h proof](phase_depth/FIXED_H_DEPTH.md), not on the
feed's finite brute-force samples.

## 6. Read-only check of the sufficient-set pivot

Sections3–4 of [SUFFICIENT_SETS_AUDIT.md](sufficient_sets/SUFFICIENT_SETS_AUDIT.md)
are logically consistent after their correction. Ordering the five rays
from exponent9 gives successive ratios
`7/6,8/7,9/8,7/6,8/7`, all below `3/2`. A universal completion of `R'_N`
from supplied `U_N` would extend absorption through `3N/2`, supplying the
next cutoff. The verified base `U_6144` suffices for that conditional
induction, and every cutoff is divisible by512 as required by the
annular-block transfer.

Separate certificates for individual roots may reuse an already certified
positive source: absorption has no consumable multiplicity budget. Joint
capacity checking is required when blocks are summed and represented as
one submeasure of an annulus. The revised interface states both scopes
correctly. Its universal complementary-root construction remains open.

## 7. Reproduction and actual checks

The two external scripts were run unmodified against a temporary copy of
main's `affine_controls.py`. Their stored JSON receipts reproduce exactly.
Each process had a30-second wall-clock cap; all finished normally. The
`--merge` output also matches the table. Actual-root descent counts at
`N=6144,98304` reproduce their finite maxima48 and81.

To rerun the external computations without changing either branch, run
this from the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
import shutil, subprocess, sys, tempfile
repo=Path.cwd()
review=Path(tempfile.mkdtemp(prefix='collatz-side-review-'))
probe=review/'sidekick'/'probes'
probe.mkdir(parents=True)
dep=review/'collatz_research_20261017'/'negative_controls'
dep.mkdir(parents=True)
shutil.copy2(repo/'collatz_research_20261017/negative_controls/affine_controls.py',
             dep/'affine_controls.py')
ref='9a0c28d90e1554cfa967e7e0ea785a86dd1af04c'
for name in ('residual_vs_induction.py','residual_cylinder_core.py'):
    (probe/name).write_bytes(subprocess.check_output(
        ['git','show',f'{ref}:reviews/side_lane/{name}'],cwd=repo))
for args in (['residual_vs_induction.py'],['residual_cylinder_core.py'],
             ['residual_cylinder_core.py','--merge']):
    subprocess.run([sys.executable,str(probe/args[0]),*args[1:]],
                   cwd=review,check=True,timeout=30)
print(review)
PY
```

For the additional independent prefix check, import the materialized
`residual_cylinder_core.py` as a module and compare both dynamic-program
fractions with this direct enumeration for every `m=2,...,14`:

```python
from fractions import Fraction

def brute(m, merge):
    undecided = 0
    for start in range(3, 2**m, 4):
        x, j, A, success = start, 0, 0, False
        while A < m:
            z = 3*x + 1
            a = (z & -z).bit_length() - 1
            if A + a >= m:  # exact cylinders need the extra bit
                break
            x, j, A = z // 2**a, j + 1, A + a
            if (3**j*3 < 2**(A+1) or
                    (merge and a >= 3 and a % 2 and 3**j < 2**A)):
                success = True
                break
        undecided += not success
    return Fraction(undecided, 2**(m-2))
```

The review receipt records the pinned source hashes, main dependency hash,
exact rational fractions, finite fit values, six comparisons with main's
residual constructor, and the fixed-h barrier cross-check. No remote
branch, shared proof document, or executable implementation was changed.
