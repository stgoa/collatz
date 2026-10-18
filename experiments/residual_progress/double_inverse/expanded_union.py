"""The earlier four-rule union plus R47, R48 and R50, with one common rank."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'critical_rank'))
import rules_union as OLD
import double_inverse as DOUBLE

RANK=OLD.RANK


def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module


MULTIPLE=load('union_multiple','nonselected_multiples/multiple_escape.py')
FORWARD=load('union_forward','nonselected_forward/nonselected_forward.py')


def one_step(w):
    data=OLD.one_step(w)
    if data is not None:return data
    data=MULTIPLE.decreasing_plan(w)
    if data is not None:
        rule='R47_nonselected_multiple'
    elif FORWARD.eligible(w):
        data=FORWARD.forward_plan(w)
        if data['status']=='descending':
            rule='R48_nonselected_forward'
        elif DOUBLE.recognized(w):
            data=DOUBLE.pair_plan(w);rule='R50_double_inverse'
        else:return None
    else:return None
    RANK.validate_step(w,data)
    return dict(data,rule=rule)


def close(w,max_nodes=None):
    return RANK.close_plan(w,one_step,max_nodes=max_nodes)
