"""Bounded exact replay of the valuation-debt progress obstruction."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import valuation_debt as M

HERE=Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(json.dumps(data,sort_keys=True,separators=(',',':')).encode()).hexdigest()


def rows(data):
    return [[x,c] for x,c in sorted(data.items())]


def expect_error(action):
    try:action()
    except ValueError:return
    raise AssertionError('Expected rejection')


def mixed_exact_order(H,index=0):
    modulus=2**(H+1)
    w=(2**H-M.B_W)*pow(M.D,-1,modulus)%modulus+modulus*index
    assert M.NORMAL.valuation2(M.D*w+M.B_W)==H and M.MIXED.eligible(w)
    return w


def finite_absorption(seed):
    x,current=seed,{}
    while x!=1:
        if x in current or len(current)>=10000 or x.bit_length()>4096:
            raise RuntimeError('Designated supplied input unresolved within caps')
        current[x]=1;x=M.NORMAL.step(x)
    assert M.RANK.divergence(current)==M.RANK.atoms((1,seed))
    return current


def supplied_demo(H):
    data=M.obstruction(H)
    supplied={u:M.RANK.combine((1,finite_absorption(3*u)),(-1,finite_absorption(u)))
              for u in data['coefficients']}
    current=M.compile_plan(data,supplied)
    assert M.RANK.divergence(current)==M.RANK.T.pair_source(data['seed'])
    expect_error(lambda:M.compile_plan(data,{}))
    bad=dict(supplied);bad[next(iter(bad))]={}
    expect_error(lambda:M.compile_plan(data,bad))
    return dict(seed=data['seed'],child=data['leading'],H=H,
                supplied_pairs=len(supplied),current_rows=len(current),
                current_hash=digest(rows(current)),plan_current=rows(data['current']),
                coefficients=rows(data['coefficients']),
                supplied={str(u):rows(c) for u,c in sorted(supplied.items())},current=rows(current))


def audit():
    assert M.B_E-M.B_W==344992 and M.NORMAL.valuation2(344992)==5
    assert M.NORMAL.valuation2(13975032)==3
    assert 3**12>2**19 and 3**7<2**20 and 3**5<2**18
    assert Fraction(64,9)*Fraction(-M.B_W,M.D)+Fraction(5,9)==Fraction(-6626905,21459)
    transport=[]
    for H in (26,27,45,64,128,256):
        for index in (0,1):
            d=M.leading_transport(mixed_exact_order(H,index))
            for state in d['states']:
                other=M.B_W if state['phase']=='E' else M.B_E
                assert M.NORMAL.valuation2(M.D*state['seed']+other)==5
            transport.append(d)
    # Height can grow without changing the valuation state used in the proof.
    fixed_order=[M.leading_transport(mixed_exact_order(26,i)) for i in (2**32,2**128)]
    families=[]
    for H in (26,27,32,40,64,128,256,512):
        for index in (0,1,2**64):
            data=M.obstruction(H,index)
            f=data['family'];w,u=data['seed'],data['leading']
            assert M.NORMAL.valuation2(M.D*u+M.B_E)==5
            assert M.NORMAL.valuation2(M.D*w+M.B_W)==3
            expected=M.RANK.T.pair_source(w)
            for x,c in data['coefficients'].items():
                expected=M.RANK.combine((1,expected),(-c,M.RANK.T.pair_source(x)))
            assert M.RANK.divergence(data['current'])==expected
            assert M.RANK.rho(u)<data['rank']
            assert M.NORMAL.step(M.NORMAL.step(M.NORMAL.step(data['rank'])))==M.NORMAL.step(3*u)
            assert M.NORMAL.normal_form(M.NORMAL.step(M.NORMAL.normal_form(M.NORMAL.step(data['rank']))))==3*u
            families.append(dict(seed=w,child=u,H=H,index=index,
                                  parent_rank=data['rank'],child_rank=M.RANK.rho(u),
                                  parent_order=f['parent']['order'],child_order=f['child_debt']['order'],
                                  potential_ratio=f['potential_ratio'],
                                  coefficients=rows(data['coefficients']),current_hash=digest(rows(data['current']))))
    # Exact rational illustrations; the written proof covers all real powers.
    monomial=[]
    f=M.pole_family(26)
    for alpha in range(5):
        for beta in range(-3,4):
            block=Fraction(3**12,2**19)**alpha*Fraction(2)**(-19*beta)
            if beta<=0:assert block>=1
            else:
                reset=Fraction(f['child_debt']['form'],f['parent']['form'])**alpha*Fraction(2)**(beta*23)
                assert reset>1
            monomial.append([alpha,beta,block.numerator,block.denominator])
    demos=[supplied_demo(26),supplied_demo(40)]
    invalid=[lambda:M.phase(1),lambda:M.phase(-3),lambda:M.pole_family(25),
             lambda:M.pole_family(26,-1),lambda:M.leading_transport(21)]
    for action in invalid:expect_error(action)
    sources=[HERE/'valuation_debt.py',HERE/'check_valuation_debt.py']
    sources += [HERE.parent/p for p in ('mixed_rank_recursion/mixed_growth.py',
        'returning_phase/returning_phase.py','phase_rank/sigma_rank.py',
        'critical_rank/rank_closure.py')]
    result=dict(status='PASS',scope='Two natural rational-centre monomial/logarithmic potentials; no arbitrary-rank or universal-current no-go',
                leading_transports=transport,fixed_order_large_heights=fixed_order,
                full_family_plans=families,monomial_cases=len(monomial),monomial_hash=digest(monomial),
                supplied_demos=demos,rejections=len(invalid)+2*len(demos),
                caps=dict(supplied_arrow_limit=10000,supplied_bit_limit=4096,largest_checked_order=512),
                sources={str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources})
    return json.loads(json.dumps(result))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true')
    args=parser.parse_args();result=audit();path=HERE/'valuation_debt_audit.json'
    if args.write:path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    else:assert json.loads(path.read_text())==result
    print('PASS: valuation debt and complete reset family; '
          f"{len(result['leading_transports'])+len(result['fixed_order_large_heights'])} leading transports; "
          f"{len(result['full_family_plans'])} full signed plans; {result['monomial_cases']} rational cases; "
          f"{len(result['supplied_demos'])} supplied conversions")
