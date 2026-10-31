# Review of binary-ternary-carry-frontier

## What I checked

- The whole node (claim, sections 1 to 5, What survives, History) and the V14 card [`base_conversion.md`](base_conversion.md), line by line.
- **Recomputation of the diagram** with my own implementation of rule (1) (`recompute_carry_frontier.py`, kept in the review lane's scratch folder outside the repository; 44 checks, all pass, 0.3 s):
  - the input column 10, 11 reads `(12)_3 = 5`; the three division sweeps give the output states 00,11 / 00,01 / 00,00 with bottom remainders 1, 0, 1, so the columns read `5 -> 2 -> 1 -> 0`, and each column is `floor(previous/2)` with remainder `previous mod 2` (checked out to `x = -9`);
  - the bottom sums are `...000101 = 5`;
  - with the bootstrap 01 at (0,0), the five horizontal rows (r, east state, r+s+c, completed state, emitted bit) are exactly as tabulated; every cell with `x <= -6` has total 0, state 00 and emits 0, so there are exactly five nonzero horizontal transitions (and six vertical ones); the emitted row is `...00010000` with its single 1 at `x = -5`, which reads `16 = 3*5 + 1`;
  - the 3 by 6 rectangle is `00 00 00 00 00 10 / 00 00 00 01 11 11 / 00 01 11 01 11 01`; the state at (-4, 0) is 01, so the first leading binary zero carries a 1, and replacing it by 00 would lose the emitted 1 at `x = -5`;
  - the columns with row 0 included read `(121)_3 = 16, (022)_3 = 8, (011)_3 = 4, (002)_3 = 2, (001)_3 = 1`: the shortcut arrows `5 -> 8 -> 4 -> 2 -> 1` (four arrows); the odd-only arrow `5 -> 1` has valuation 4;
  - read horizontally, the rows west of `x = 0` are `0, 1, 5, 16`, each `3 * previous + (trit at x = 0 in that row)`: the Horner evaluation of `(121)_3`, which is Theorem 16's anchor statement at (0,0) (north column 5, west row 101 = 5).
- **Section 4 arithmetic.** `3(2n+1)+1 = 2(3n+2)`, so `h(3n+2) = h(2n+1)` for every invariant colouring and `h(8) = h(5)` at `n = 2`; `3(4n+1)+1 = 4(3n+1)`, so `h(3n+1) = h(4n+1)` for `n >= 1`; `x = 5 + 32t -> (3x+1)/16 = 1 + 6t` with `v_2(3x+1) = 4` exactly for all `t < 10^4`; `x = 37` shares the five low bits of 5, has valuation 4 and endpoint 7; `5 + 2^B -> 1 + 3*2^(B-4)` with valuation 4 for `5 <= B < 40`, while `B = 4` (`x = 21`) has valuation 6, so `B >= 5` is needed as stated; `32 = 2^(4+1)` is the exact valuation cylinder of [`NOTATION.md`](../../../../conventions/NOTATION.md) section 1.
- **Primary source** (Stérin-Woods, arXiv:2007.06979v4, fetched 2026-10-31). The carry-propagation and forward-deduction rules of Definition 1 are rule (1): carry 1 iff sum + east sum + east carry is at least 2, new sum = that total mod 2. The "+1" bootstrap requires the immediately-west cell to be (1,undefined), the centre cell (0 or undefined, undefined) and every cell `i x EAST`, `i >= 1`, to have sum 0 or undefined and carry undefined: the node's wording is right, and (0,0), undefined with an undefined east ray, meets it. The states 00, 01, 10, 11 are the symbols 0, 0-bar, 1, 1-bar with trit values 0, 1, 1, 2. Definition 3 encodes a trit 1 as the symbol 1 when the nearest non-1 trit to its right is a 2, so `(12)_3` is "1, 1-bar" = states 10, 11, as section 2 says. Definitions 1, 3, 7, 8, Lemmas 5, 6, 15, Theorem 16 and section 3.2 exist with the content the node and the card use. The card's small-cycle milestone is the paper's Definition 29 and the open problem of its section 3.1 (`x = T^m(x)` with `0 < m <= ceil(log2 x)`, `x > 2`, shortcut map), as stated.
- **Card section 4.** The transducer on input 3 (bits 1, 1, 0, 0, least significant first) from state (0,1) outputs 0, 1, 0, 1 = `10 = 3*3 + 1` and ends in (0,0); the shortcut orbit `3 -> 5 -> 8 -> 4 -> 2 -> 1` has five arrows and the odd-only orbit `3 -> 5 -> 1` two.
- **Controls** ([`NOTATION.md`](../../../../conventions/NOTATION.md) section 3). The 3x+5 cycle `19 -> 31 -> 49 -> 19` is an actual odd-only cycle; the d = 5 analogue of the section 4 identity is `3(2n+1) + 5 = 2(3n+4)`, a different identity, so `h(3n+2) = h(2n+1)` is specific to d = 1, as the node's control discussion requires. The node makes no d-uniform claim and no exclusion claim; nothing in it would exclude the 3x+5 cycle. Side check: no shortcut cycle `T^k(x) = x` with `3 <= x < 2^16` and `k <= ceil(log2 x)` (the card's deferred milestone, which the node does not claim).
- **Certificates.** None listed. `python3 tools/run_certificates.py --node binary-ternary-carry-frontier` (run together with my other node): "0 certificate failure(s)", exit 0, 0.2 s. The two evidence scripts, not required, pass: [`verify_examples.py`](../../results/digit-count-invariant-colourings-constant/verify_examples.py) of digit-count-invariant-colourings-constant (function `check_carry_patch`, receipt key `carry_patch` in its `verification.json`), exit 0, 0.2 s; [`verify_examples.py`](../../results/periodic-invariant-colourings-classification/verify_examples.py) of periodic-invariant-colourings-classification (function `check_transducer`, receipt key `base_conversion`), exit 0, 0.1 s.
- **Links and schema.** Every relative link in `README.md` and `base_conversion.md` resolves (the feed archive, [`PROOF_REVIEW.md`](../../results/digit-count-invariant-colourings-constant/PROOF_REVIEW.md), the exit18 node, the archive index); `PROOF_REVIEW.md` does say the carry calculation was produced by that reviewer, as History states. The sections are the attempt sections in the required order.

## What I did not check

- The paper's general statements (Lemma 15, Theorem 16) were read, not re-proved; only the finite example was recomputed from the local rules.
- The legacy commits named in History (`cdfb143`, `2ac44ef`, `be73a66`) are not in this repository's history.
- Whether the test missed a frontier relation: the claim is scoped to one rectangle, and I did not try to find a relation beyond the affine arrow and the section identities.

## Findings

1. Sections 1 and 3, bootstrap predicate (imprecision, minor). The node states the west and east conditions of the "+1" rule but not the paper's condition on the centre cell itself, (0 or undefined, undefined). It is satisfied here, since (0,0) is undefined, so nothing changes.
2. Citations (imprecision, minor). `README.md` cites Definitions 1/3/8 and Lemmas 5/6/15, the card Definitions 1/3/7 and Lemma 5. Both lists are correct (Definition 7 places the binary input, Definition 8 the ternary input); they differ only in which items each note needed.
3. History (not checkable). The commit hashes cannot be resolved in this clone; they are legacy provenance only.

No error in any table, identity or number.

## Verdict

HOLDS. The "why it fails" analysis is correct: eliminating the internal cells of the rectangle leaves the Horner step `N -> 3N + t` fed by the ternary column and the affine arrow (2), and the only relation it yields for an invariant colouring is `h(8) = h(5)`, an instance of `h(3n+2) = h(2n+1)`. "What survives" claims only the checked fixture, the list of cut data, the paper's open problem (recorded, not adopted) and the side lane's verdict; nothing unproved.

Claude review lane (Fable 5.1; directed by Santiago Armstrong), 2026-10-31
