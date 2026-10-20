"""Fixed-priority union of the four proved strict critical-rank rules.

Missing inputs stay explicit. This dispatcher never discovers an orbit or
supplies a current for an unrecognized pair.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import rank_closure as RANK

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = spec_from_file_location(name, HERE.parent/path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


RETURN = load('rank_return', 'returning_phase/returning_phase.py')
BASE = load('rank_base', 'nonselected_inverse/inverse_phases.py')
ESCAPE = load('rank_escape', 'inverse_escape/inverse_escape.py')


def one_step(w):
    RANK.NORMAL._odd(w)
    if w % 8 != 5:
        raise ValueError('Require a W5 pair')
    if RANK.INVERSE.eligible(w) and w % 9 != 3:
        data = RANK.INVERSE.phase_pair_plan(w)
        rule = 'R41_inverse_phase'
    elif BASE.decreasing_domain(w):
        data = BASE.decreasing_plan(w)
        rule = 'R45_nonselected_base'
    elif RETURN.returning(w):
        data = RETURN.forward_plan(w)
        if data['status'] != 'descending':
            return None
        rule = 'R44_returning_forward'
    elif ESCAPE.recognized(w):
        data = ESCAPE.pair_plan(w)
        rule = 'R46_inverse_escape'
    else:
        return None
    RANK.validate_step(w, data)
    return dict(data, rule=rule)


def close(w, max_nodes=None):
    return RANK.close_plan(w, one_step, max_nodes=max_nodes)
