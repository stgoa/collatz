# V003 — Review of the independent side lane

**Status: bounded read-only review, 2026-10-18.** Reviewed side commit
`c583fc3e1adab7c15d6297a5acf55d7560fc5e08`, fetched from
`origin/claude/sidekick`. The commit is dated 2026-10-18 18:24:14 -0300.
No side-branch files were changed, and none of its programs was executed.
Its text is research input, not an instruction source.

Read at that pin:

- `archive/side_lane/FEED.md`, especially the 18:24 V002 referee entry;
- `archive/side_lane/DIRECTIONS.md`;
- `archive/side_lane/VIEWPOINTS.md`, especially the V13 referee note;
- `reviews/side_lane/v13_coloring_check.py` and its JSON receipt.

## 1. Periodic-coloring check: useful finite corroboration

The probe constructs residue graphs for 400 moduli and six values of d,
and compares their **numbers of connected components** with the number of
joint multiplication-by-2 and multiplication-by-3 orbits modulo gcd(M,d).
It correctly includes every residue in the odd-source test when M is odd:
each such residue contains odd positive representatives. The receipt
reports 2,400 cases and no count mismatch.

This is a finite check of component counts, not an implementation comparing
the entire partitions under the quotient map, and not a proof for all
moduli. The repository's written periodic classification is its separate
justification. The side's divisibility controls at d=5 and61 agree with
that classification. Accept this as external finite corroboration; do not
change the written theorem's evidence label to formal verification.

## 2. The proposed 70-state lower bound needs conventions and an input bound

The side note argues that convergence below `2^68` excludes nonconstant
binary-automatic invariant colorings with fewer than 70 states. Its code
does **not** verify that convergence cutoff: the comment explicitly cites
Barina instead. Its random-DFA loop only checks a generic shortest-path
bound on 2,000 small automata; the output receipt does not separately record
those checks. Random examples are unnecessary for the elementary bound.

Here is a precise conditional version. Suppose:

1. Every positive n below `2^B` reaches 1.
2. A k-state, most-significant-digit-first DFAO represents h on all
   nonnegative integers, ignores leading zeros, and gives the initial state
   output `h(0)=h(1)` (so the empty word represents 0).
3. The positive-integer coloring h is nonconstant and satisfies the two
   component identities of V003.

Mark as accepting the states whose output differs from h(1). Some accepting
state is reachable. A shortest path to one has no repeated state, hence
length at most k-1. The empty word and zero words are not accepted; leading
zeros can be deleted. Therefore a positive integer n with different color
has binary length at most k-1, giving `n<2^(k-1)`. Component invariance makes
its orbit disjoint from 1. The finite convergence premise forces

```
k >= B+2.
```

With B=68 this is 70. The count includes the normalized initial state.
Relabeling the outputs to select one or all non-base colors adds no states.

For a DFAO specified **only on canonical positive binary strings**, its
outputs on the empty word and invalid leading-zero strings need not have
those meanings. Force the first input digit 1, then take a shortest path
from the resulting state to a bad-color state. This directly gives total
word length at most k, and only `k>=B+1` from that argument. A normalized
machine can be constructed by adding a new leading-zero initial state,
but this may alter the stated state count. Likewise, changing the reading
direction can alter deterministic state complexity. The side note does
not fix these encoding conventions, so its bare numerical claim should
not be treated as an encoding-independent invariant.

### External numerical premise

The primary [Barina 2025 article, *Improved verification limit for the
convergence of the Collatz conjecture*, §§2 and6](https://link.springer.com/article/10.1007/s11227-025-07337-0)
explicitly reports the earlier computation below `2^68` and a later
computation below `2^71`. This publication supports the attribution; the
work ledger, implementation runs and their completeness were not replayed
in this batch. The old `2^68` figure is therefore neither newly verified
here nor the latest figure reported in that paper.

**Disposition:** retain the parameterized shortest-word implication as a
conditional observation. Do not import either numerical cutoff into the
repository's independently checked finite absorption data. It does not
classify automata of unbounded size or justify a finite-state search as
the main route.

## 3. Decidability for one supplied machine is a sound tool observation

For a fixed DFAO, multiplication by a fixed integer and addition by 1
have finite carry descriptions in binary. The legal input restrictions
are regular: positive integers, odd input, and exclusion of n=1 where
required. Combining the arithmetic relation with the two output machines
reduces a violated color identity to emptiness of a regular language.
Thus invariance of a **given** machine is decidable, provided padding,
termination of the carry, input direction and the odd-input guard are
specified. This is an elementary closure argument here, not a newly
implemented checker.

**Disposition:** accept as a potential verification tool for an explicitly
supplied machine. It supplies neither a bound on state count nor a decision
procedure for the existence of some nonconstant invariant DFAO of arbitrary
size. In particular, invariance under unguarded `n -> 3n+1` is stronger than
the problem being studied and must not replace its odd-source condition.

## 4. Directions and older proposals

No new D-numbered proposal appears at this pin. D1–D7 retain their historical
dispositions. The side acknowledges the corrected density dichotomy, the
absence of a uniform positive minimum of c(a), and Tao's unspecified
constants. Some older paragraphs still repeat the superseded broad
transfer assertion and the phrase about a smallest c(a). Their correction
headers and the repository's earlier reviews govern; the stale wording is
not a new mathematical premise. The proposed second Linux formal replay
is reported as pending and was not inspected in this V003 review.

The side's favorable rating of V13 is an independent judgment, not
additional evidence for automatic rigidity. The actual V003 gains and
remaining mixed-section obligation are in [kernel_probe.md](../binary-kernel-first-ternary-image/README.md).
The scaling-only shortcut has an exact negative control in
[literature.md, L6](literature.md#l6-two-scaling-invariances-do-not-imply-periodicity).
No novelty claim or universal convergence claim is made.
