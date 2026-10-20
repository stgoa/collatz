"""Complete smaller-origin history queries within supplied ternary precision.

All forward exploration is restricted to a verified finite absorbing table.
The completeness theorem covers every inverse ray; no ray-index cap is used.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = spec_from_file_location('frontier_native_history', HERE.parent/'native_history/native_history.py')
H = module_from_spec(spec)
spec.loader.exec_module(H)
N, I, B = H.NORMAL, H.INVERSE, H.BASIS
combine, atoms, divergence = H.combine, H.atoms, H.divergence


def integer(x, lower=0):
    return isinstance(x, int) and not isinstance(x, bool) and x >= lower


def edge_branch(source, target):
    """Identify the unique complete inverse branch without a guessed ray cap."""
    if not N.canonical(source) or not N.canonical(target) or N.quotient_step(source) != target:
        raise ValueError('Require an actual canonical quotient edge')
    choices = []
    for kind, (a, b) in I.BASES[target % 3].items():
        base = (a*target+b)//3
        if kind == 'point':
            if source == base:
                choices.append((kind, 0))
        else:
            num, den = 9*source+7, 9*base+7
            if num % den:
                continue
            factor = num//den
            exponent = factor.bit_length()-1
            if factor > 0 and factor == 1 << exponent and exponent % 6 == 0:
                choices.append((kind, exponent//6))
    if len(choices) != 1:
        raise ValueError('The edge does not have one canonical inverse branch')
    return choices[0]


class FiniteHistory:
    """A supplied canonical edge table with verified absorption and coverage."""

    def __init__(self, rows, coverage):
        if not integer(coverage, 1):
            raise ValueError('Require a positive finite coverage cutoff')
        self.edges = dict(rows)
        if len(self.edges) != len(rows) or self.edges.get(1) != 1:
            raise ValueError('Require distinct source rows and the absorber')
        for x, y in self.edges.items():
            if not integer(x, 1) or not integer(y, 1) or not N.canonical(x):
                raise ValueError('Invalid canonical table state')
            if y not in self.edges or N.quotient_step(x) != y:
                raise ValueError('Incorrect or nonclosed supplied edge')
        absorbed = {1}
        for start in self.edges:
            seen, x = set(), start
            while x not in absorbed:
                if x in seen:
                    raise ValueError('A nonabsorbing cycle is not a valid history')
                seen.add(x)
                x = self.edges[x]
            absorbed.update(seen)
        self.origins = tuple(x for x in range(1, coverage+1, 2) if N.canonical(x))
        if any(x not in self.edges for x in self.origins):
            raise ValueError('The history omits a required canonical origin')
        self.coverage = coverage
        self._catalogues = {}

    def catalogue(self, target):
        if not integer(target, 2) or not N.canonical(target):
            raise ValueError('Require a canonical anchor target above1')
        if target in self._catalogues:
            return self._catalogues[target]
        out = []
        if target in self.edges:
            for origin in self.origins:
                path, x = [origin], origin
                while x not in (1, target):
                    x = self.edges[x]
                    path.append(x)
                if x != target:
                    continue
                word, slope = [], Fraction(1)
                for source, image in zip(path[-2::-1], path[:0:-1]):
                    kind, index = edge_branch(source, image)
                    alpha, _ = I.inverse_affine(image % 3, kind, index)
                    slope *= alpha
                    word.append((kind, index))
                assert slope >= Fraction(origin+1, target+1)
                out.append(dict(origin=origin, depth=len(word), slope=slope,
                                word=tuple(word), path=tuple(path)))
        self._catalogues[target] = tuple(out)
        return self._catalogues[target]

    def classify(self, threshold, target, anchor_target, depth):
        """Every canonical a<threshold reaching target in0..depth T arrows."""
        if not integer(threshold, 2) or not integer(target, 2) or not integer(depth):
            raise ValueError('Invalid threshold, target or depth')
        if not integer(anchor_target, 2) or not N.canonical(anchor_target):
            raise ValueError('Require a canonical anchor target above1')
        if not N.canonical(target) or target < anchor_target:
            raise ValueError('Require a canonical target no smaller than its anchor')
        if (target-anchor_target) % 3**depth:
            raise ValueError('Insufficient ternary precision')
        bound = Fraction((threshold+1)*(anchor_target+1), target+1)
        cutoff = (bound.numerator+bound.denominator-1)//bound.denominator-2
        if cutoff > self.coverage:
            raise ValueError('The supplied history does not cover the shadow cutoff')
        hits = []
        for row in self.catalogue(anchor_target):
            if row['origin'] > cutoff or row['depth'] > depth:
                continue
            actual, shadow, path = target, anchor_target, [target]
            for kind, index in row['word']:
                actual, _, _ = I.inverse_step(actual, kind, index)
                shadow, _, _ = I.inverse_step(shadow, kind, index)
                path.append(actual)
            predicted = row['origin']+row['slope']*(target-anchor_target)
            assert predicted.denominator == 1 and actual == predicted and shadow == row['origin']
            if actual < threshold:
                hits.append(dict(origin=row['origin'], lower=actual, depth=row['depth'],
                                 inverse_word=row['word'], forward_path=tuple(reversed(path))))
        return dict(threshold=threshold, target=target, anchor_target=anchor_target,
                    depth=depth, shadow_cutoff=cutoff, hits=hits)


def quotient_current(path):
    if not path or any(not N.canonical(x) for x in path):
        raise ValueError('Require a nonempty canonical path')
    out = {}
    for x, y in zip(path, path[1:]):
        if x == 1 or N.quotient_step(x) != y:
            raise ValueError('Incorrect quotient path')
        out = combine((1, out), (1, {x: 1}), (1, N.bridge(N.step(x))['current']))
    assert divergence(out) == atoms((1, path[0]), (-1, path[-1]))
    return out


def native_plan(seed, upper_path, hit):
    rank = B.rho(seed)
    if not upper_path or 3*seed != upper_path[0] or rank != 3*seed:
        raise ValueError('Require a critical parent with canonical upper root')
    q, lower = 3*seed, hit['lower']
    if lower >= q or hit['forward_path'][-1] != upper_path[-1]:
        raise ValueError('Require an actual smaller common-tail partner')
    up, down = quotient_current(upper_path), quotient_current(hit['forward_path'])
    high, low = B.absorption_plan(lower), B.absorption_plan(seed)
    current = combine((1, up), (-1, down), (1, high['current']), (-1, low['current']))
    coeff = combine((1, high['coefficients']), (-1, low['coefficients']))
    result = dict(seed=seed, rank=q, status='descending', rule='finite_history_frontier',
                  current=current, coefficients=coeff)
    B.validate(result)
    return result
