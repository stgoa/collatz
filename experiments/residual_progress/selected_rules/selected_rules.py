"""Twelve conditional rule families with the original critical-image rank.

The old nine-rule dispatcher has priority.  Every additional step retains
its exact signed requests and strictly decreases rho; sigma is not used.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, relative):
    spec = spec_from_file_location(name, HERE.parent / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


OLD = _load('selected_rules_old', 'continued_rules/continued_rules.py')
FORWARD = _load('selected_rules_forward', 'selected_forward/selected_forward.py')
INVERSE = _load('selected_rules_inverse', 'selected_inverse/selected_inverse.py')
EXIT = _load('selected_rules_exit', 'selected_cycle_exit/selected_exit.py')
RANK = OLD.RANK


def one_step(w):
    """Return the first strict-rho plan, or None with no hidden premise."""
    if not isinstance(w, int) or w <= 0 or w % 8 != 5:
        raise ValueError('Require a positive W5 input')
    data = OLD.one_step(w)
    if data is not None:
        RANK.validate_step(w, data)
        return data
    for module, rule in ((FORWARD, 'R55_selected_forward'),
                         (INVERSE, 'R56_selected_inverse'),
                         (EXIT, 'R57_selected_cycle_exit')):
        data = module.one_step(w)
        if data is not None:
            RANK.validate_step(w, data)
            return dict(data, rule=rule, rank=RANK.rho(w))
    return None


def close(w, max_nodes=None):
    """Finite formal closure; every unrecognized leaf stays a signed input."""
    return RANK.close_plan(w, one_step, max_nodes=max_nodes)


def compile_plan(plan, supplied):
    """Substitute only supplied exact currents for the remaining inputs."""
    return RANK.compile_plan(plan, supplied)
