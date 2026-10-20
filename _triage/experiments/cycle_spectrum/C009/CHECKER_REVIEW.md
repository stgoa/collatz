# C009 checker and independent proof review

**Status: author excursion checks PASS; independent review of three written
proofs and independent replay of the root return-order checker PASS.**
The proposed automatic excursion compression is rejected. No new
nontrivial denominator-one cycle is excluded.

## Authorship and verification roles

This reviewer authored `check_excursions.py` and `excursions_audit.json`.
Their write and replay runs are **author checks**, not an independent
review of that implementation. The root agent separately reported its
independent replay of that checker. This note does not replace the root
review or the historical finite gate.

The three mathematical notes below and `check_return_order.py` were
written by other agents. I read their complete source, checked the
arguments and examples, and independently ran the return-order checker
without writing its receipt. No Lean or external formal replay is claimed.

## Findings and correction

One documentation error was reported before correction:
`FIRST_RETURN_ORDER.md` linked to `excursion_audit.json`, while the saved
receipt is `excursions_audit.json`. The root author corrected the link
and regenerated its small receipt. I checked that the corrected document
hash was present before replay. All local Markdown links in the three
reviewed notes now resolve.

**No mathematical error was found in the reviewed arguments.** This is an
agent proof review, not human review, formal verification, or a novelty
assessment.

## Mathematical review

### Exact endpoint reconstruction

Both [EXCURSION_ARITHMETIC.md](EXCURSION_ARITHMETIC.md) and
[INDEPENDENT_EXCURSION.md](INDEPENDENT_EXCURSION.md) retain positive odd
endpoints, positive valuations, positive odd q, and the complete segment
intercept. Reducing the endpoint equation at each prefix power of two
proves intermediate integrality. Positivity follows directly from the
prefix formula. Each next arrow has an even right side, so the preceding
intermediate state is odd; the final state is odd by hypothesis. These
facts prove exact valuations, rather than only divisibility.

The normalized weighted intercept equals the ordinary segment intercept
here because both endpoint heights are zero. The q13 example correctly
separates that intercept5 from the unweighted normalized-word intercept7.
No unweighted mechanical replacement is used in the proof.

### Complementary closure and Smith form

Eliminating the shared endpoint gives

```text
D*x = q*(3^r*C_E + 2^a*C_P),
D = 2^(a+b) - 3^(ell+r).
```

The right side is the original rotated full-word intercept. At q1,
`D|C` propagates to all rotations because D is odd, so the converse
integer reconstruction is justified. Oddness of C and D gives odd
integer quotients. The positivity hypothesis D>0 is retained.

For k compressed blocks, the cyclic coefficient determinant is
`(-1)^(k-1)*D`. At every prime dividing D, the indicated `(k-1)` minor
is a power of3 and hence a unit; at other primes the determinant is
already a unit. This proves that all but the last Smith factor are1.
For k1 the matrix is `[D]` and the empty minor is1, so the same argument
has the correct boundary case. The augmented maximal minors are the
determinant and the Cramer numerators at block starts; their gcd is
`gcd(D,q*g)` with `g=gcd(C,D)`. No additional independent integrality
condition is thereby obtained.

The notes correctly limit this conclusion: algebraic compression alone
adds no congruence. They do not prove that a future joint argument using
shape inequalities and divisibility is impossible.

### One-point deletion and actual controls

In [FIRST_RETURN_ORDER.md](FIRST_RETURN_ORDER.md), translating the deleted
rank to0 preserves circular order. The regular compressed shifts are
s and s-1; the predecessor through0 has shift2s-1, all modulo m-1.
For an interior shift, both regular groups are nonempty and have
unequal shifts. For s1 or s=m-1 every shift agrees. The m2 singleton
case is explicitly retained. The application requires the full ordered
cycle and the actual height labels; it does not assert realizability
of every abstract rank permutation.

The exact q13 core permutation `(2,0,3,1)` and q233 permutation
`(4,6,0,5,1,2,3)` agree with the stored excursion data. The q83
return 277→457→727→283 has slope27/32 and rises 6 because of its
positive intercept. The two q1 controls are correctly labeled open
paths; neither is counted as a cycle or used to refute a q1-specific
cyclic theorem.

## Source inspection and independent replay

`check_return_order.py` computes first returns directly, with a separate
check against the deletion formula and its multiplicities. It tests
all deleted ranks for each coprime shift through m=80, including m2.
The endpoint grid constructs odd starting residues modulo `2^(A+1)`
and then follows every exact raw arrow. It allows expanding segments,
as the reconstruction lemma does. The actual controls independently
check full closure, reduction, dyadic heights, sorted images, and
return affine equations using exact integers and rational numbers.
There are no floating-point decisions or omitted q1 endpoint cases.

After checking that the receipt's two dependency hashes matched the
current checker and corrected theorem file, I ran:

```sh
python3 experiments/cycle_spectrum/C009/check_return_order.py
```

**Result: PASS, exit 0.**

| Finite domain | Exact replay result |
| --- | ---: |
| Deletion permutations, 2<=m<=80, all coprime shifts and deleted ranks | 105388 |
| Directly followed retained-rank arrows | 6250510 |
| Nearest-neighbor cases preserving rotation | 6476 |
| Interior-shift cases losing rotation | 98912 |
| Positive odd endpoint pairs, lengths 1..5, valuations 1..4, q in {1,5,7,13}, three lifts | 16368 |
| Exact endpoint-reconstruction arrows | 76464 |

The finite deletion-row digest is
`9264139dd9832fac202db676d865bc81cd5508ffbaba3002d375e5675a385399`.
These checks exercise the written theorems; they are not their all-size
proofs and do not classify all Collatz cycles.

## Author excursion evidence

The final author runs were:

```sh
python3 experiments/cycle_spectrum/C009/check_excursions.py --write
python3 experiments/cycle_spectrum/C009/check_excursions.py
```

Both passed. The receipt preserves all 2,459 C001 source cycles across 333
parameters, the 1,275 nontrivial source scalings, all 11 fixtures, and the
C007 addition. There are 1,185 distinct normalized cycles, 2,593 first
returns and 28,831 prefix-cylinder checks. No new seed census or word
grid is run by this checker.

Among 52 ordered cycles, 177 returns contain 60 positive-height excursions:
48 descend and 12 rise; 50 have contracting slope and 10 expand. Two rise
while contracting. Twelve ordered cycles lose circular order on their
height-zero cores. All complements and complete return compositions are
checked. Six invalid-input controls are rejected. The finite receipt
keeps ordered, unordered q<=L, and q>L classes separate.

## Reviewed hashes

| File | SHA256 |
| --- | --- |
| `EXCURSION_ARITHMETIC.md` | `7d4a0f7413dea67be2f3fd6e6643ace2ccb8b2decee6dc17f2b77f10b27eabcd` |
| `INDEPENDENT_EXCURSION.md` | `b37655989a8f43a17ced1632a404fd34dfdb8d6d5dcadaa0d6533df1e3be58ac` |
| `FIRST_RETURN_ORDER.md` | `10a7f10d396a8631c197f3203af498467d92551ad35f4e9ded63c7c621d354fa` |
| `check_return_order.py` | `58b016702d0292a5294027dd75139b36dad171fc2e314971ae07a46fb2a59355` |
| `return_order_audit.json` | `ab4672a38fa2dc688d34ced57d3af0148eab1b821267eb44ed013b016eba5d34` |
| Author `check_excursions.py` | `a7631d433cd5952d8a27de3eb41addb8d01784da410064fb9e479d5cff3e17cb` |
| Author `excursions_audit.json` | `414c04dd9042d378674659f2ddf824a6228756f230ebe28fb2282795425f19e1` |
