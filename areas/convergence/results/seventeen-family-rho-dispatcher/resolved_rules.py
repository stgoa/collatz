"""Seventeen conditional families with fixed prior resolvers and one rho.

Refined15 keeps exact priority. R62's optional resolver remains refined15;
R59 retains its old-twelve resolver. Neither may call this new dispatcher.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name,path):
    spec=spec_from_file_location(name,HERE.parent/path)
    module=module_from_spec(spec);spec.loader.exec_module(module)
    return module


OLD=load('resolved_old','refined_rules/refined_rules.py')
DEFECT=load('resolved_defect','defect_resolution/defect_resolution.py')
LIFTED=load('resolved_lifted','refined_obstruction/refined_obstruction.py')
RANK=OLD.RANK
ADDED=((DEFECT,'R62_defect_resolution'),(LIFTED,'R64_lifted_inverse'))


def one_step(w):
    if not isinstance(w,int) or w<=0 or w%8!=5:
        raise ValueError('Require a positive W5 input')
    old=OLD.one_step(w)
    if old is not None:
        RANK.validate_step(w,old)
        return old
    for module,name in ADDED:
        data=module.one_step(w)
        if data is not None:
            RANK.validate_step(w,data)
            return dict(data,rule=name,rank=RANK.rho(w))
    return None


def close(w,max_nodes=None):
    return RANK.close_plan(w,one_step,max_nodes=max_nodes)


def compile_plan(plan,supplied):
    return RANK.compile_plan(plan,supplied)
