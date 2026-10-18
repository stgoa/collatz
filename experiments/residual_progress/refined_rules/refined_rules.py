"""Fifteen conditional families with the original critical-image rank.

The old twelve have exact priority. Deferred expansion keeps its fixed old
twelve resolver; it never calls this dispatcher. No sigma rule is used.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD = _load('refined_rules_old', 'selected_rules/selected_rules.py')
EXACT = _load('refined_rules_exact', 'exact_absorption_bound/exact_bound.py')
DEFERRED = _load('refined_rules_deferred', 'deferred_rank/deferred_rank.py')
CYCLE = _load('refined_rules_cycle', 'cycle_inverse/cycle_inverse.py')
RANK = OLD.RANK
ADDED = ((EXACT, 'R58_exact_absorption_bound'),
         (DEFERRED, 'R59_deferred_rank'),
         (CYCLE, 'R60_cycle_inverse'))


def one_step(w):
    """First validated strict-rho plan, or None retaining the obligation."""
    if not isinstance(w, int) or w <= 0 or w % 8 != 5:
        raise ValueError('Require a positive W5 input')
    data = OLD.one_step(w)
    if data is not None:
        RANK.validate_step(w, data)
        return data
    for module, rule in ADDED:
        data = module.one_step(w)
        if data is not None:
            RANK.validate_step(w, data)
            return dict(data, rule=rule, rank=RANK.rho(w))
    return None


def close(w, max_nodes=None):
    """Finite formal substitution; every unrecognized leaf stays explicit."""
    return RANK.close_plan(w, one_step, max_nodes=max_nodes)


def compile_plan(plan, supplied):
    """Require and verify exact currents for all remaining signed requests."""
    return RANK.compile_plan(plan, supplied)
