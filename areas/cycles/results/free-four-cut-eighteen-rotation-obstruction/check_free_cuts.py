"""Exact solver-free replay of the free four-cut eighteen-rotation model.

Every rational dual is checked before the complete generic tree is rebuilt.
No discovery metadata, floating-point solver, resource guard, or sampled
absence is used. Boundary transfer is the separate argument in README.md.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
from math import gcd
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
DIMENSION = 5
HORIZON = 18
R = F(3, 8)
EPSILON = F(1, 10000)
sys.setrecursionlimit(20000)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


@lru_cache(maxsize=None)
def primitive(row):
    """Positive normalization: never reverse the inequality's orientation."""
    divisor = gcd(*row)
    return tuple(value//divisor for value in row) if divisor else row


def add(left, right):
    return tuple(a+b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a-b for a, b in zip(left, right))


def scale(expression, value):
    return tuple(value*a for a in expression)


ZERO = (0,)*6
ONE = (0,)*5+(1,)
H = (1, 0, 0, 0, 0, 0)
BASE = tuple(tuple(int(j == i) for j in range(5))+(0,) for i in range(1, 5))


class ExactReplay:
    def __init__(self, raw):
        data = json.loads(raw)
        require(data['dimension'] == DIMENSION and data['horizon'] == HORIZON,
                'fixed free five-variable eighteen-rotation model')
        require(F(data['epsilon']) == EPSILON, 'fixed error threshold')
        self.rows = []
        self.row_ids = {}
        original_rows = []
        for row in data['rows']:
            require(len(row) == 6 and all(type(value) is int for value in row), 'integer affine row')
            row = tuple(row)
            require(primitive(row) == row and any(row[:5]), 'positive primitive nonconstant row')
            original_rows.append(row)
            self.intern(row)
        require(len(original_rows) == len(self.rows), 'unique mathematical row table')
        self.by_member = defaultdict(list)
        self.support_sizes = Counter()
        self.core_count = 0
        support_masks = set()
        gaps = []
        for core in data['cores']:
            combined = [F(0)]*6
            mass = F(0)
            mask = 0
            support = core['support']
            require(support, 'nonempty dual support')
            for identifier, value in support:
                require(type(identifier) is int and 0 <= identifier < len(original_rows), 'dual row index')
                weight = F(value)
                require(weight > 0, 'positive saved dual weight')
                mass += weight
                combined = [a+weight*b for a, b in zip(combined, original_rows[identifier])]
                mask |= 1 << identifier
            require(mass == 1, 'dual normalization')
            require(not any(combined[:5]), 'exact cancellation of all five variables')
            require(combined[5] == F(core['gap']) <= 0, 'exact nonpositive dual RHS')
            self.core_count += 1
            self.support_sizes[mask.bit_count()] += 1
            gaps.append(combined[5])
            if mask in support_masks:
                continue
            support_masks.add(mask)
            bits = mask
            while bits:
                bit = bits & -bits
                self.by_member[bit.bit_length()-1].append(mask)
                bits -= bit
        require(self.core_count > 0, 'proof contains exact duals')
        self.unique_supports = len(support_masks)
        self.gap_range = [str(min(gaps)), str(max(gaps))]
        self.stats = Counter()
        self.rotations = Counter()

    def intern(self, row):
        row = primitive(row)
        identifier = self.row_ids.get(row)
        if identifier is None:
            identifier = len(self.rows)
            self.row_ids[row] = identifier
            self.rows.append(row)
        return identifier

    def extend(self, previous, expressions):
        """previous has survived every core; check newly completed supports."""
        self.stats['extensions'] += 1
        result = previous
        added = []
        for expression in expressions:
            row = expression[:5]+(-expression[5],)
            if not any(row[:5]):
                if row[5] < 0:
                    self.stats['negative_constant_prunes'] += 1
                    return None
                # Ignoring a strict0<0 row only weakens pruning.
                continue
            identifier = self.intern(row)
            bit = 1 << identifier
            if not result & bit:
                result |= bit
                added.append(identifier)
        for identifier in added:
            for core in self.by_member.get(identifier, ()):
                if result & core == core:
                    self.stats['exact_core_prunes'] += 1
                    return None
        return result

    def rotation(self, rows, j, chain, layer, delta):
        """chain is ordered C_j; layer is the four newest cuts; delta={jh}."""
        self.rotations[j] += 1

        def insert_new(index, rows, ordered, next_layer, next_delta):
            if index == 4:
                self.rotation(rows, j+1, ordered, next_layer, next_delta)
                return
            difference = sub(layer[index], H)
            # old_layer-h lies(-1/2,1): only floors-1 and0 are possible.
            for offset in (1, 0):
                point = add(difference, scale(ONE, offset))
                wrapped = self.extend(rows, (scale(point, -1), sub(point, ONE)))
                if wrapped is None:
                    continue
                for rank in range(len(ordered)+1):
                    inequalities = []
                    if rank:
                        inequalities.append(sub(ordered[rank-1], point))
                    if rank < len(ordered):
                        inequalities.append(sub(point, ordered[rank]))
                    more = self.extend(wrapped, inequalities)
                    if more is not None:
                        insert_new(index+1, more, ordered[:rank]+(point,)+ordered[rank:],
                                   next_layer+(point,), next_delta)

        threshold = sub(ONE, delta)
        for split in range(len(chain)+1):
            inequalities = []
            if split:
                inequalities.append(sub(chain[split-1], threshold))
            if split < len(chain):
                inequalities.append(sub(threshold, chain[split]))
            for index, endpoint in enumerate(chain):
                witness = add(endpoint, delta) if index < split else endpoint
                gap = sub(endpoint, chain[index-1])
                if index == 0:
                    gap = add(gap, ONE)
                # This is exactly10000*(gap-(3/8)*witness-1/10000)<0.
                inequalities.append(sub(sub(scale(gap, 10000), scale(witness, 3750)), ONE))
            more = self.extend(rows, inequalities)
            if more is None:
                continue
            require(j < HORIZON, 'unpruned horizon branch: certificate incomplete or model feasible')
            # delta+h lies(0,3/2): only floors0 and1 are possible.
            for floor in (0, 1):
                next_delta = sub(add(delta, H), scale(ONE, floor))
                wrapped = self.extend(more, (scale(next_delta, -1), sub(next_delta, ONE)))
                if wrapped is not None:
                    insert_new(0, wrapped, chain, (), next_delta)

    def run(self):
        domain = [scale(H, -1), sub(scale(H, 2), ONE), scale(BASE[0], -1)]
        domain += [sub(BASE[i], BASE[i+1]) for i in range(3)]
        domain += [sub(BASE[-1], ONE)]
        initial = self.extend(0, domain)
        if initial is not None:
            self.rotation(initial, 1, BASE, BASE, H)
        return dict(dimension=DIMENSION, horizon=HORIZON, coefficient=str(R),
                    epsilon=str(EPSILON), checked_duals=self.core_count,
                    unique_supports=self.unique_supports, support_sizes=dict(sorted(self.support_sizes.items())),
                    dual_rhs_range=self.gap_range, rotations=dict(sorted(self.rotations.items())),
                    stats=dict(self.stats), unpruned_horizon_branches=0,
                    scope='Complete generic free-cut tree; every pruning uses a verified exact contradiction.')


def finite_controls():
    output = {}
    specifications = [
        ('order18', F(7, 18), ['2/9', '61/128', '799/1152', '383/384'], F(-7, 9216), F(155, 9216)),
        ('order14751', F(5734, 14751), ['0', '3283/14751', '2347/4917', '932/1341'], F(-11, 10728), F(235, 14751)),
    ]
    for name, h, texts, expected, failure in specifications:
        base = list(map(F, texts))
        require(len(set(base)) == 4 and 0 < h < F(1, 2), 'faithful finite control')
        rows = []
        for j in range(1, 19):
            raw = [(c-i*h) % 1 for c in base for i in range(j)]
            cuts = sorted(set(raw))
            deficits = [(e-cuts[k-1]) % 1 - R*max(e or F(1), (e+j*h) % 1 or F(1))
                        for k, e in enumerate(cuts)]
            rows.append(dict(j=j, raw_cuts=len(raw), distinct_cuts=len(cuts),
                             maximum_deficit=str(max(deficits))))
        require(max(F(row['maximum_deficit']) for row in rows[:17]) == expected < 0,
                'seventeen tests insufficient even at zero error')
        require(F(rows[17]['maximum_deficit']) == failure > EPSILON, 'eighteenth test fails')
        output[name] = dict(h=str(h), cuts=texts, rotation_order=h.denominator,
                            first_failure=18, eighteenth_is_identity=(18*h).denominator == 1,
                            rotations=rows)
    require(not output['order14751']['eighteenth_is_identity'], 'genuine nonidentity eighteenth control')
    return output


def fixed_shift_boundary_control():
    """A rational order30 wrap/collision point, with h kept exactly fixed."""
    h = F(11, 30)
    base = list(map(F, ['0', '2/15', '5/12', '19/30']))
    moved = [(cut-F(100+i, 10**8)) % 1 for i, cut in enumerate(base)]
    allowance = F(42, 10**8)
    original_collision_rotations = 0
    largest_increase = F(0)
    for j in range(1, 19):
        old_raw = [(cut-i*h) % 1 for cut in base for i in range(j)]
        old = sorted(set(old_raw))
        new_raw = [(cut-i*h) % 1 for cut in moved for i in range(j)]
        new = sorted(set(new_raw))
        require(len(new) == 4*j and all(new), 'perturbed cuts are nonzero and distinct')
        require(all((cut+j*h) % 1 for cut in new), 'perturbed partners avoid zero')
        def maximum(cuts):
            return max((end-cuts[index-1]) % 1-R*max(end or F(1), (end+j*h) % 1 or F(1))
                       for index, end in enumerate(cuts))
        old_max, new_max = maximum(old), maximum(new)
        require(new_max <= max(old_max, F(0))+allowance, 'one-sided boundary control')
        largest_increase = max(largest_increase, new_max-max(old_max, F(0)))
        original_collision_rotations += len(old) < len(old_raw)
    require(original_collision_rotations > 0, 'control exercises old coincidences')
    return dict(h=str(h), rotation_order=30, original_cuts=list(map(str, base)),
                shifted_cuts=list(map(str, moved)), horizons_checked=18,
                original_collision_rotations=original_collision_rotations,
                error_allowance=str(allowance), largest_observed_increase=str(largest_increase),
                scope='Finite control of the fixed-h boundary argument; the manuscript proves the general transfer.')


def main():
    require(sys.argv[1:] in ([], ['--write-receipt']), 'usage: checker [--write-receipt]')
    proof_path = HERE/'free_cut_duals.json'
    raw = proof_path.read_bytes()
    replay = ExactReplay(raw).run()
    require(replay['checked_duals'] == 4708 and replay['stats']['extensions'] == 29781
            and replay['stats']['exact_core_prunes'] == 27924, 'expected complete exact replay counts')
    result = dict(schema='free-four-cut-eighteen-v1', proof_sha256=sha256(raw).hexdigest(),
                  proof_bytes=len(raw), replay=replay, finite_controls=finite_controls(),
                  fixed_h_boundary_control=fixed_shift_boundary_control())
    encoded = json.dumps(result, sort_keys=True, indent=2)+'\n'
    receipt = HERE/'check_free_cuts.json'
    if sys.argv[1:]:
        receipt.write_text(encoded)
    else:
        require(receipt.read_text() == encoded, 'receipt mismatch; inspect before regenerating')
    print(json.dumps(dict(status='passed', checked_duals=replay['checked_duals'],
                         extensions=replay['stats']['extensions'], exact_prunes=replay['stats']['exact_core_prunes'],
                         horizon=HORIZON, survivors=0, finite_controls=2), sort_keys=True))


if __name__ == '__main__':
    main()
