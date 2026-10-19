# C008 — Independent proof review and checker author replay

**Outcome: stated proofs pass this review; exact checker replay PASS.**
This reviewer independently examined the two proof drafts below and
authored the separate matching checker. Consequently the proof review
is independent of those drafts, while the software runs reported here
are **author** checks. Root's software replay and historical gate are
separate evidence. No formal verification or novelty is claimed.

## Proofs and claim scope

Reviewed snapshots:

| Document | SHA256 |
| --- | --- |
| [MATCHING_ARITHMETIC.md](MATCHING_ARITHMETIC.md) | `aefff8c4a83e236c341ecbd2c37e7b6d7cb41d2aa87c3459a44f9d722a2a53ad` |
| [INDEPENDENT_MATCHING.md](INDEPENDENT_MATCHING.md) | `21b37af7f124364e57b041a18cd8b96fec818a14a55451e7528d74aff1c3931e` |

The following arguments check out under their written hypotheses:

- The raw odd clock, exact positive valuations, primitive period,
  reduced denominator and `q<=L` order domain are retained. Oddness and
  reduction make the required residues units when the modulus exceeds
  one. The fixed point and modulus-one residue are not silently removed.
- The small-band normalized theorem through `B=2` and raw theorem
  through `B=1` correctly use two distinct height-zero residues and
  rising edges. The chronological two-color argument retains
  `gcd(A,m)=1` and rules out its residual two-letter positive-cycle
  possibility. Hall's singleton, pair and triple conditions are covered.
- The alternate rank proof obtains `t^m=2`, `t^A=3` by Bezout and
  correctly places normalized residues at sorted rank `j` as `Lt^j`.
  Its use of mechanical prefixes depends on the ordered minimum-state
  phase. For a divisor `Q>1`, `T=ord_Q(t)>=4` follows from the three
  explicit gcd obstructions. These arguments do not extend to `Q=1`.
- The inclusion-minimal Hall-deficiency lemma retains every proper
  subset and correctly proves deficit one and repeated membership of
  every neighboring residue.
- The cyclic-subgroup restriction is already implied by coprime totals;
  it is correctly separated from Hall. The explicit congruence arguments
  for 35, 65 and 91, the relation-lattice basis `(n,0),(a,b)`, and Smith
  factors `e,nb/e` are valid. No denominator-one exclusion follows.
  This reviewer did not run root's separate spectrum checker.

**Issue reported before correction:** the proposed next-test row
initially mentioned only minimal deficient sets of at least three
bands. A wider cycle can instead have a deficient pair of nonadjacent
bands; the projected `{1,3}` example illustrates this. The author
updated the row to retain that case. This was a roadmap omission, not
an error in a stated theorem.

The arithmetic author's withdrawn trial extending raw matching through
`B=2` to every divisor is explicitly retracted in the independent note.
The new exact control below verifies that failure. It does not refute
the stated raw `B<=1` theorem or full-reduced-denominator matching.

## Exact added control

The third projected control is an actual ordered cycle at reduced
`q=5,077,565`, with `m=17`, `A=27`, `L=365,289,811`, `B=2` and
numerator cancellation factor one. Every raw arrow, exact valuation,
height and normalized ordering was independently recomputed from its
valuation word.

Modulo the proper divisor 5, all three raw height neighborhoods are
`{1,4}`. Thus heights `{0,1,2}` have two neighbors and Hall deficit one.
The normalized projected graph matches, consistent with the normalized
`B<=2` theorem. Both full-denominator graphs also match.

For both numerical examples in the independent note, I additionally
checked the printed sorted height lists, gcd of all numerators, maximum
normalized coordinate, minimum cyclic adjacent gap, and every printed
full-denominator representative. All checks passed. The checks include
the wrap gap to `2L`.

## Receipt extension and final replay

Before the extension, the checker hash was
`d3d07a69fb1b76f75713656816cd2efbebe77deda2908a9806f1566466afd727`.
The only source change was inside `projected_controls()`. A direct
comparison of the source before and after that function verified every
other section unchanged. The old receipt's author hash and every input
dependency hash were checked before replacing its projected-control
block with the exact recomputation and updating its source hash.

This avoided repeating the unchanged profile grid merely to append one
control. A subsequent **full** replay then recomputed the entire receipt,
including the unchanged 946,001-profile grid, once:

```sh
python3 experiments/cycle_spectrum/C008/check_height_matching.py
```

Result: exit status **0**, output `status: PASS`, `mode: replay`.

| Recomputed coverage | Result |
| --- | ---: |
| Original source cycles / parameters | 2,459 / 333 |
| Scaled source instances | 1,275 |
| Original distinct normalized cycles plus C007 addition | 1,184 + 1 |
| Raw source arrows | 36,912 |
| Historical fixture controls | 11 |
| Ordered cases including q1 fixed point / nontrivial ordered cases | 52 / 51 |
| Full-q raw / normalized matching passes | 1,185 / 1,185 |
| Targeted positive profiles | 946,001 |
| Retained primitive cycles at reduced q<=31 / ordered among them | 13 / 11 |
| Retained raw-arrow checks | 96 |
| Retained cycles absent from existing evidence | 0 |
| Exact projected controls | 3 |

The 945,988 profiles with larger reduced denominator are screened out,
not counted as substantive matching evidence. Missing intermediate
height labels in 371 unordered cycles are explicit; their graphs cover
observed labels. All ordered graphs cover every height from zero to B.
Seven strict rejection probes and both q1/residue0 conventions had
passed before the control-only extension; their source was unchanged.

The printed numerical values in the independent note can be replayed
from the final exact receipt with this additional read-only check:

```python
from pathlib import Path
from math import gcd
import json
r = json.loads(Path('experiments/cycle_spectrum/C008/height_matching_audit.json').read_text())
cases = [
    (1, 860118109, 151913474,
     [426229,4961174,1182098,60469], [426229,4844783,2015023,483752]),
    (2, 703754011, 59822914,
     [340839,302968,128909], [340839,605936,335254]),
]
for index, maximum, minimum_gap, normalized_sdr, raw_sdr in cases:
    case = r['projected_controls']['cases'][index]
    c = case['cycle']
    B = c['B']
    Z = [n*2**(B-h) for n,h in zip(c['states'],c['heights'])]
    Z = [Z[i] for i in c['sorted_indices']]
    gaps = [b-a for a,b in zip(Z,Z[1:])] + [2*Z[0]-Z[-1]]
    assert max(Z) == maximum*2**B and min(gaps) == minimum_gap
    assert gcd(*c['states']) == 1
    for mode,sdr in [('raw',raw_sdr),('normalized',normalized_sdr)]:
        graph = next(x['graph'] for x in case['full_denominator_matching'] if x['mode']==mode)
        assert len(set(sdr)) == len(sdr)
        assert all(value in graph[str(h)] for h,value in enumerate(sdr))
print('PASS: both printed full-q assignments and cyclic gap controls')
```

## Frozen final artifacts

| Artifact | SHA256 |
| --- | --- |
| [check_height_matching.py](check_height_matching.py) | `f8d63a71dc57206386c35cfcadba62a29969f1405aa8be665fa39158e99d1f39` |
| [height_matching_audit.json](height_matching_audit.json) | `8be1fb6414481b333f36cd007e4542a2c9e009d6339afd7fb3771b6e79b7361a` |

Full-denominator Hall matching remains open. The exact failures concern
proper-divisor projections. The small-band and spectrum statements do
not exclude every ordered denominator-one cycle or settle the broader
all-cycle goal.
