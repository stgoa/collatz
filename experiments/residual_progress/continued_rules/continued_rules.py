"""The seven rho rules followed by the two complete forward continuations.

R51 uses another rank and is deliberately absent from this dispatcher.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'double_inverse'))
import expanded_union as OLD
RANK=OLD.RANK


def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module


RETURN=load('continued_return','returning_continuation/returning_continuation.py')
FORWARD=load('continued_forward','forward_continuation/forward_continuation.py')


def one_step(w):
    data=OLD.one_step(w)
    if data is not None:return data
    if RETURN.recognized(w):
        data=RETURN.continuation_plan(w);rule='R52_returning_continuation'
    else:
        data=FORWARD.one_step(w)
        if data is None:return None
        rule='R53_forward_continuation'
    RANK.validate_step(w,data)
    return dict(data,rule=rule,rank=RANK.rho(w))


def close(w,max_nodes=None):
    return RANK.close_plan(w,one_step,max_nodes=max_nodes)
