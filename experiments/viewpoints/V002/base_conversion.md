# V14 — Two-dimensional arithmetic diagrams and base conversion

**Status: exploratory comparison.** Primary source read: Stérin–Woods,
[*The Collatz process embeds a base conversion algorithm*, v4 (2022)](https://arxiv.org/html/2007.06979v4),
Definitions 1/3/7, Lemma 5, Theorem 16 and §3.2. No new theorem, novelty or
termination claim. This is a language comparison, not an implementation.

## 1. Objects

The paper's quasi-cellular automaton uses sum/carry states `(s,c)` on a square
grid. Its local arithmetic is

`s2=(s0+c0+s1) mod2`, `c1=1[s0+c0+s1>=2]`.

It also needs a **non-local bootstrap** for the +1 boundary. Thus calling the
given construction a purely local tile system would omit a rule. Rows encode
odd iterates; columns encode the shortcut map `T(n)=n/2` or `(3n+1)/2`.
Parallel automaton updates are a third clock. Its base `3'` digits are
`0,(bar0),1,(bar1)`, valued respectively `0,1,1,2`.

## 2. Structural gain over V1/V2

The same carry diagram computes binary multiplication/addition horizontally
and ternary division vertically. The base-conversion theorem identifies a
finite rectangle as ternary-to-binary conversion. This exposes which boundary
data are linked, rather than merely assigning two norms to one affine formula.

Our assessment: one can now ask about *compatible completions across a cut*,
or forbidden boundary patterns. That is a different organization of the
arithmetic from a parity shift or an endpoint ledger. It is useful only if
the cut description gives an estimate or exclusion that those descriptions
did not already supply.

## 3. Translated gap and boundary conditions

The paper separates a conversion rectangle from a complementary region
containing the unresolved forward computation. Our inference is that a finite
alphabet does not bound the information crossing its growing boundary.
Likewise, freezing each cell after finitely many changes does not bound how
many new cells are activated.

Finite binary inputs have a specified zero tail to the left. Allowing arbitrary
infinite binary boundaries admits 2-adic points, including noninteger rational
cycles. Local consistency of every finite patch therefore does not establish
one finite positive-integer boundary for an infinite diagram. This is the
same quantifier obstruction exposed by the repository's frozen
[integer-prefix theorem](../../residual_progress/integer_prefix/INTEGER_PREFIXES.md),
now visible geometrically. Any proposed tiling compactness argument must retain
the finite-support condition and the bootstrap boundary.

## 4. Exact small local-rule example

Apply Lemma 5's binary transducer to `w=11`, with two leading zeros. Start
at state `(s0,c0)=(0,1)`, read from the least significant end, and replace
the state by `(s1,c1)` after each digit:

| Input s1 | Previous state | Total s0+c0+s1 | Output s2 | New state |
|---|---|---:|---:|---|
| 1 | (0,1) | 2 | 0 | (1,1) |
| 1 | (1,1) | 3 | 1 | (1,1) |
| 0 | (1,1) | 2 | 0 | (0,1) |
| 0 | (0,1) | 1 | 1 | (0,0) |

The emitted least-first bits `0,1,0,1` give `1010_2=10=3*3+1`.
This is a transducer calculation, not four Collatz arrows. The shortcut orbit
`3 -> 5 -> 8 -> 4 -> 2 -> 1` takes five arrows; the odd orbit
`3 -> 5 -> 1` takes two. Neither number is an asserted parallel update count.

## 5. Known-cycle control

The **external arithmetic control** `S_5: 19 -> 31 -> 49 -> 19` must remain
possible for any purported generalization. No d=5 tile rules are defined or
verified here, so this cycle is not claimed to be an execution of the paper's
d=1 automaton. Changing +1 to +5 changes the boundary/carry mechanism; it
requires an actual construction. Generic claims such as “finite local states
force termination” already fail at the arithmetic level.

## 6. Cheapest next test

Take one small finite conversion rectangle and list every state required on
its frontier to determine the next region, including the bootstrap condition.
Compare that list with V2's exact guarded affine history. Reject a claimed
compression if it silently fixes an unknown boundary, permits an infinite
left tail, or merely redraws the full history. No simulator installation or
broad tiling search is justified yet.

## 7. Genuinely partial milestone

A concrete published target is the paper's **small-cycle question**: exclude
`T^k(x)=x` for every integer `x>2` and `1<=k<=ceil(log_2 x)`.
This is the shortcut clock and does not include the known 1–2 cycle. Resolving
this restricted target would leave all divergence and cycles whose periods
exceed the threshold at every member. The paper poses the question; this
card supplies no exclusion and makes no claim about its current novelty.
First check whether the two-dimensional boundary constraints contribute more
than the usual periodic affine-word equation.

**Selection:** retain one boundary-completion test. The simultaneous base
structure is substantive; the missing finite-integer boundary estimate remains
unresolved. The mere existence of the simulator does not earn a deep proof effort.
