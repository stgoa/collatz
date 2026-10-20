# V004 — Direct automaton route and independent closure audit

**Status:** bounded direct-automaton comparison; independent written audit of
the positive-offset kernel proof found in the parallel kernel investigation.
This note supplies no formal Lean verification or novelty claim.

## Seven-field comparison

1. **Objects.** A finite-output binary automaton for h, with
   h(2n)=h(n) for positive n and h(3n+1)=h(n) for odd n>1. Its binary kernel
   is represented by entire sequences, not states identified from samples.
2. **Structural gain.** A reset word in a most-significant-digit automaton
   gives a monochromatic cylinder and hence constancy. The positive-offset
   kernel construction below obtains an eventually periodic odd section
   without assuming any reset word or bounding the automaton size.
3. **Translated gap.** The initial direct route lacked an argument forcing
   synchronization or a monochromatic arithmetic progression. A finite
   automaton need not synchronize. The parallel closure proof bypasses this
   gap by establishing two-base automaticity of a specific section.
4. **Worked example.** The state g(n)=h(4n+3) has ternary-zero section
   h(12n+3)=h(64n+17). The positive offset 3 becomes 17; it cannot produce
   the uncontrolled zero-offset state h(3n).
5. **Known-cycle controls.** At d=5 or61, the periodic color 1_(d divides n)
   has no monochromatic dyadic cylinder but does have monochromatic ordinary
   arithmetic progressions. The +1 identities and arbitrary-progression
   sufficiency used below do not transfer unchanged to these maps.
6. **Cheapest meaningful next test.** Independently audit all closure cases,
   then the precise hypotheses and threshold handling of Cobham and the
   published progression theorem. A larger automaton catalogue is unnecessary.
7. **Intermediate milestone.** Constancy for the whole binary-automatic
   class, at arbitrary finite state count. This still does not establish
   that an actual component indicator is binary-automatic.

## 1. Why a direct reset argument was not enough

If a most-significant-digit automaton has a word sending every reachable
state to one state, appending that word to arbitrary positive prefixes gives
a monochromatic dyadic cylinder. The V003 progression argument then applies.
There is no general finite-automaton theorem that supplies such a word:
binary digit-sum parity has no constant binary section.

Studying a transition word of minimal image size only replaces an arbitrary
state set by a smaller image. It does not show that every output on that
image agrees. A minimal-rank or strongly-connected-component argument would
still need to use the full guarded Collatz equation to eliminate a
nontrivial residual output action. No such independent argument was obtained
in this bounded pass.

Likewise, regularity of every fixed-depth inverse language does not make its
unbounded union regular. Pumping individual predecessor words does not by
itself show that all states of a proposed invariant automaton have the
absorber's output. These are rejected proof steps, not barriers to every
automaton argument.

## 2. A tempting weaker scaling lemma needs the correct conclusion

The claim that every binary-automatic g satisfying
g(2n)=g(3n)=g(n) has a constant **dyadic** section is false:

```
g(n)=1_(5 divides n).
```

Multiplication by2 or3 preserves divisibility by5. Every dyadic residue
class contains multiples and nonmultiples of5 by the Chinese remainder
theorem. Thus no dyadic section is constant. This example is also an actual
invariant color for 3n+5 with1 absorbing.

A putative scaling lemma producing a constant arbitrary arithmetic
progression would evade this counterexample, but was not established in
this pass. The multiplicative-automatic classification cannot simply be
imported: invariance under multiplication by2 and3 does not assert
f(mn)=f(m)f(n) for coprime m,n. The stronger closure proof below makes this
unproved scaling lemma unnecessary.

## 3. Independent audit of the positive-offset closure

Extend h to0 by h(0)=h(1), and write

```
K+ = {n -> h(2^a n+r) : a>=1, 1<=r<2^a}.
```

Binary automaticity makes this family finite. It is closed under binary
sections because r+2^a j is positive and below2^(a+1), for j=0,1.

The previously established +1 identities imply

```
h(3m+1)=h(4m+1),
h(3m+2)=h(2m+1),             m>=0,
h(3u)=h(16u+1),             positive odd u.
```

For the last identity, use
h(3u)=h(9u+1)=h(12u+1)=h(16u+1).
The first odd source is3u>=3; the subsequent equalities use the first
displayed identity. Thus no forbidden odd source1 is needed here. In the
first two identities the omitted value equality at1 follows already from
h(4)=h(1).

Take a state h(2^a n+r) in K+ and ternary digit j in{0,1,2}. Put
c=2^a j+r. Then0<c<3*2^a, and its section is h(3*2^a n+c).

### Case A: 3 does not divide c

Choose v=1 if c=2 mod3, and v=2 if c=1 mod3. Set
t=(2^v c-1)/3. The integer t is odd, positive, and less than2^(a+v).
Odd-source invariance followed by removal of2^v gives

```
h(3*2^a n+c)=h(2^(a+v)n+t).
```

The right side is in K+. The smallest cases c=1 and c=2 both give t=1,
so a zero offset does not arise at the endpoint.

### Case B: 3 divides c

Write t=c/3=2^ell*u, with u positive odd. Since0<t<2^a, ell<a and
1<=u<2^(a-ell). Remove the common factor2^ell and apply the odd identity:

```
h(3*2^a n+c)
 = h(3*(2^(a-ell)n+u))
 = h(2^(a-ell+4)n+16u+1).
```

The new offset satisfies

```
17 <= 16u+1 <= 2^(a-ell+4)-15.
```

Thus it too is a valid strictly positive binary offset. The argument
2^(a-ell)n+u is positive odd for every n>=0, because a-ell>=1.

**Audit conclusion:** every ternary section of every member of K+ remains
in K+. This avoids the earlier zero-offset auxiliary function rather than
assuming its missing mixed sections are already controlled.

## 4. The published progression input really supplies the last step

The odd section b(n)=h(2n+1) belongs to K+. The finite family K+ is closed
under both binary and ternary sections, so b is automatic in both bases.
Cobham's theorem, applied to each of its finitely many color fibers, gives
one threshold N and one period M>=1 valid for b beyond N.

Choose n0>=N. Then h is constant on

```
2*n0+1 + 2*M*k,             k>=0.
```

To use a theorem stated for residues below their modulus, set A=2*n0+1
and choose a multiple D of2M with D>A. The whole positive residue class
A modD lies inside that monochromatic progression; no small unverified
members or eventual-period threshold are discarded.

[Monks–Monks–Monks–Monks, *Strongly sufficient sets and the distribution of
arithmetic sequences in the 3x+1 graph*, Theorem4.1](https://arxiv.org/html/1204.3904v2)
states that every positive target not divisible by3 admits a positive
backtrace into any residue class. This source statement was directly read
again during the present audit. Its bound concerns odd inverse branches;
no bound on total shortcut time is used here.

Every color has a representative not divisible by3: remove powers of2;
if the resulting odd number is divisible by3, it is at least3, and one
3u+1 arrow gives a ternary unit of the same color. The absorber1 already
is a ternary unit. Consequently every color agrees with the color on
A modD.

The source uses the raw shortcut map. Its even arrows preserve color by
h(2n)=h(n), and its odd arrows preserve color by the given equation and
doubling. At1, its raw arrow to2 also preserves color by h(2)=h(1).
This is a statement about equality of labels; it neither changes the
absorbing dynamics nor treats the raw cycle through1 as a nonconvergence
witness.

**Audit conclusion:** the theorem applies to the exact needed progression,
and the argument establishes constancy of the full finite-output binary-
automatic class, conditional only on the stated standard published inputs.
It does not assume regularity of an arbitrary Collatz component indicator.

## 5. Transfer controls and assessment

For either d=5 or61, let h_d(n)=1_(d divides n). It satisfies doubling
invariance and h_d(3n+d)=h_d(n), since3 is a unit modulo d. But the key +1
identity fails explicitly at positive odd u=d:

```
h_d(3d)=1,       h_d(16d+1)=0.
```

Its monochromatic progression d,2d,3d,... does not force constancy for
3n+d. Thus both the particular section algebra and the final progression
rigidity are correctly tied to the original +1 problem. No generalized
tile system or divergence theorem is asserted.

The direct state-synchronization route supplied no additional independent
proof. The positive-offset kernel route is preferred because it proves an
exact closure for every automaton size and uses progression sufficiency
only after producing a genuinely monochromatic progression. The earlier
attempt to close the entire ternary kernel was stronger than necessary.
