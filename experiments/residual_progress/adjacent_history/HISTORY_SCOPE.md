# What retained lower currents do and do not supply for the adjacent source

**Status: scoped failed-hypothesis audit.** No new accepted family or complete
recursion is claimed. This records why the current history attempt did not
escape the existing adjacent interface. It uses only the repository's
[R65 interface](../defect_normal_form/ADJACENT_DEFECT_INTERFACE.md),
[R68 separation](../adjacent_recursion/NATIVE_HEIGHT_SEPARATION.md), and
[finite supplied-history construction](../known_saturation/KNOWN_SATURATION.md).
The independent side feed is not a premise.

Use absorbed odd Syracuse S, elementary minimum nu, and
P(v)=[3v]-[v]. The remaining adjacent domain is canonical q=31 mod108,

    D(q)=[q+2]-[q],        n=(8q-5)/9.

Every input comparison in this note is with this original native height n.

## 1. The positive endpoint is already known from smaller pair inputs

R65 proves that the complete formal absorption plan H_(q+2) requests only
pairs with rho at most (3q+7)/4<n. Supplying those actual exact currents
therefore provides a finite absorption current H_+ for q+2. Its first
ordinary successor is also below n. No comparison for q has been supplied
by this step.

Let G be any finite graph of actual Syracuse arrows retained from valid
supplied currents and independently checked arithmetic bridges. Include
the rows of H_+ and the absorber1. Then the following are equivalent:

1. A finite current supported on G has divergence D(q).
2. q belongs to the component of G containing1.
3. The actual directed path from q to1 is entirely present in G.

For 1 implies2, a component containing q but not1 would have source sum
minus one: q+2 is in the absorbing component. A divergence has sum zero
on every finite nonabsorbing component. For 2 implies3, a finite graph with
at most one outgoing arrow per vertex cannot connect a directed cycle or
another terminal vertex to the absorber. The forward path is therefore
present and ends at1. For 3 implies1, let H_q be that path current and use
H_+-H_q. These are the existing finite-component arguments applied to the
whole adjacent source; they are not a new current-existence theorem.

This gives an exact test of what internal rows contribute. They can already
connect q to the supplied absorbing component, and that is useful evidence.
Unrelated zero-source cycle rows do not certify absorption. If the connection
is absent, further arithmetic bridges or exposure are still required. The
criterion does not say that every possible constructor must discover its
current by following the forward path, and it does not assert uniqueness
of arbitrary one-sided certificates.

Thus a joint comparison cannot finish here merely by declaring its positive
endpoint affordable. That endpoint is already affordable; the missing
connection is the negative endpoint q. Neither a bounded component search
nor unlimited entry into a known history has a new termination proof.

## 2. Lower pair rank is not automatically a full lower height interval

The premise "all supplied P(v) have rho(v)<n" must not silently become a
supplied U_(n-1) current. The fixed formal H construction can ask a larger
rank even at a smaller canonical seed. An exact example inside the adjacent
domain is

    q=1435, n=1275, u=957,
    s=1179<n,
    H_1179 has signed request vector {21:+1,885:+1},
    rho(21)=31, rho(885)=1327>1275.

The exceptional seed1179 has z=(3*1179-1)/16=221. Its upper request885
is returning, with critical image1327. All four numbers1179,1275,1327,1435
are canonical. The request at885 is absent from the stated strict-rank
input premise. This refutes the automatic use of that particular formal
compiler to obtain every absorption below n. It is **not** a logical
non-implication theorem: another proved comparison or actual supplied
history may independently certify1179.

For each supplied pair P(v), the lower partner v itself has formal requests
of rank at most(9v+5)/8<rho(v). With those smaller inputs actually available,
one can combine its absorption current with P(v) and extract absorption
of3v. This validates reuse of the supplied pair's absorbing history. It
does not authorize arbitrary other seeds below n without checking their
own dependencies. A mixed-basis induction also supplying every smaller
adjacent/native source is a stronger premise.

The example was checked against the frozen formal constructor with:

```python
import importlib.util
from pathlib import Path
p = Path('experiments/residual_progress/defect_normal_form/adjacent_defect.py')
s = importlib.util.spec_from_file_location('adjacent_audit', p)
a = importlib.util.module_from_spec(s)
s.loader.exec_module(a)
assert a.parameters(957)['height'] == 1275
assert a.RANK.absorption_plan(1179)['coefficients'] == {21: 1, 885: 1}
assert a.RANK.rho(885) == 1327
assert all(a.NORMAL.canonical(x) for x in (1179, 1275, 1327, 1435))
```

These finite checks passed on2026-10-18. No unknown absorption search was
used for them, and they do not replace the stated formal-plan scope.

## 3. Two tempting joint rewrites retain the same missing branch

If q=7 mod8, taking one ordinary arrow from each source gives

    D(q) = div(delta_(q+2)-delta_q) + [h]-[2h-3],
    h=(3q+7)/4.

The tempting replacement of2h-3 by h-2 is invalid throughout this branch.
Writing q=2^a*t-1 with a>=3 and t=-3^a mod4, its successor2h-3 is
canonical complementary, whereas h-2 is noncanonical. They are the two
opposite elementary cases, not a selected pair that may be halved.

If q=3 mod8, write q=4t-1 with t=3 mod4. The positive source q+2=F(t)
has a sibling comparison with t, so the remaining source is[t]-[q].
The two-arrow negative run reaches(9t-1)/2. Splitting a comparison with9t
into tripling pairs requests the second pair P(3t), whose critical rank
must still be checked against n; its index being smaller than q is not
enough. The old paired/returning interfaces already retain this issue.

R68 further proves that transporting the full R44 rule through R65 is
row-for-row the original endpoint comparison. None of these operations
creates a new decreasing native-height state. The next useful result
must provide an actual connection across a complete remaining arithmetic
type, or a new well-founded state that preserves every unresolved source.
